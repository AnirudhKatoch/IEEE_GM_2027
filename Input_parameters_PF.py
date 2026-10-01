import numpy as np
from Calculation_functions import Calculation_functions_class

class Input_parameters_class_PF:

    def __init__(self, P, Q, S, Vs, Is, V_dc, pf, phi, M):

        # ---- electrical operating point from PowerFactory, per module, one value per input step ----
        self.P = np.asarray(P, dtype=np.float64)        # [W]   active power
        self.Q = np.asarray(Q, dtype=np.float64)        # [var] reactive power, negative = inductive
        self.S = np.asarray(S, dtype=np.float64)        # [VA]  apparent power
        self.Vs = np.asarray(Vs, dtype=np.float64)      # [V]   phase RMS voltage
        self.Is = np.asarray(Is, dtype=np.float64)      # [A]   RMS current
        self.V_dc = np.asarray(V_dc, dtype=np.float64)  # [V]   DC-link voltage
        self.pf = np.asarray(pf, dtype=np.float64)      # [-]   signed power factor
        self.phi = np.asarray(phi, dtype=np.float64)    # [rad] phase angle
        self.M = float(M)                               # [-]   modulation index

        Profile_size = len(self.Is)                     # used further down (T_env etc.)
        if any(len(x) != Profile_size for x in (self.P, self.Q, self.S, self.Vs, self.V_dc, self.pf, self.phi)):
            raise ValueError("P, Q, S, Vs, Is, V_dc, pf, phi must all have the same length")

        self.inverter_phases = 3  # 1 or 3 (single-phase or three-phase)
        if self.inverter_phases not in (1, 3):
            raise ValueError("phases must be 1 or 3")

        self.modulation_scheme = "svm"  # "spwm" or "svm"
        if self.modulation_scheme not in ("spwm", "svm"):
            raise ValueError("modulation_scheme must be 'spwm' or 'svm'")

        self.single_phase_inverter_topology = "full"  # "half" or "full"
        if self.single_phase_inverter_topology not in ("half", "full"):
            raise ValueError("single_phase_inverter_topology must be 'half' or 'full'")

        self.N_parallel = 1  # switches in parallel per leg

        # ----------------------------------------#
        # Model Parameters
        # ----------------------------------------#

        self.dt = 0.001  # Simulation step size
        self.input_step = 0.02  # Simulation step size
        self.chunk_seconds = int(86400 * 2)  # chunking to reduce the RAM usage
        self.Plotting_electrical_flag = True  # True False
        self.Plotting_lifetime_flag = True
        self.Plotting_electrical_loss_flag = True
        self.Plotting_thermal_flag = True
        self.Plotting_Monte_Carlo_flag = True
        self.T0_init = None  # None for first chunk
        self.Cauer_model_accuracy = 1e-3  # 1e-3 is the optimum balance between accuracy and computation

        if abs(self.input_step / self.dt - round(self.input_step / self.dt)) > 1e-9:
            raise ValueError("input_step must be an integer multiple of dt")

        # -----------------------------
        # Power Cycle Model Parameters
        # -----------------------------

        # A. Wintrich, "Power Cycle Model for IGBT Product Lines," Semikron Danfoss International, Nuremberg, Germany,
        # Application Note AN 21-001, Rev. 02, Jul. 2024.

        self.A0 = 2.9e9  # Technology Coefficient
        self.A1 = 60  # Factor of Low ΔTj Extension
        self.T0_K = 40  # Initial Temperature for Low ΔTj Extension [K]
        self.lambda_K = 17  # Drop Constant of Low ΔTj Extension [K]
        self.alpha = -4.3  # Coffin-Manson Exponent
        self.Ea_J = 4.50e-20  # Activation Energy [J]
        self.kB_J_per_K = 1.38e-23  # Boltzmann Constant [J/K]
        self.C = 1  # Time Coefficient
        self.gamma = -0.75  # Time Exponent
        self.k_thickness = {"IGBT": 1, "Diode": 0.5}  # Standard 600–1200 V IGBT chip (default)
        #  k_thickness = 1.00 → IGBT ≤ 1200 V
        #  k_thickness = 0.65 → 1700 V IGBT and CAL (freewheeling) diodes
        #  k_thickness = 0.50 → rectifier diodes / thyristors
        #  k_thickness = 0.33 → SiC ≤ 1200 V
        #  2300 V (FF1800R23IE7) is not covered by AN 21-001; 0.65 (1700 V class) used as
        #  closest documented value, likely optimistic. Sensitivity case: 0.5

        # ----------------------------------------#
        # Package max limits
        # ----------------------------------------#

        # Infineon Technologies AG, "FF1800R23IE7: PrimePACK™3+ B-series module with TRENCHSTOP™ IGBT7 and emitter
        # controlled 7 diode and NTC," Final Datasheet, Rev. 1.40, Jun. 2026. [Online]. Available: https://www.infineon.com
        # Source: Infineon FF1800R23IE7 datasheet, Rev. 1.40, Tables 3–6 (Inverter)

        self.max_V_CE = 2300  # [V] V_CES, collector-emitter voltage
        self.max_IGBT_current = 1800  # [A] I_CN, implemented collector current
        self.max_IGBT_temperature = 423.15  # [K] T_vj op = 150 °C (175 °C only for short overload)
        self.max_Diode_current = 1800  # [A] I_F, continuous DC forward current
        self.max_Diode_temperature = 423.15  # [K] T_vj op = 150 °C
        self.IGBT_max_life = 150000  # years
        self.Diode_max_life = 150000  # years

        # ----------------------------------------#
        # Miscellaneous
        # ----------------------------------------#

        self.f = 60  # [Hz] Grid frequency
        self.omega = 2 * np.pi * self.f  # [rad/s] Angular frequency of the grid (ω = 2πf)

        # ----------------------------------------#
        # Thermal Parameters
        # ----------------------------------------#

        self.T_env = np.full(Profile_size, 273.15 + 25, dtype=np.float64)  # [K] Ambient Temperature
        self.thermal_model = "fastest"  # "transient", "fast" or "fastest"

        # Infineon Technologies AG, "FF1800R23IE7: PrimePACK™3+ B-series module with TRENCHSTOP™ IGBT7 and emitter
        # controlled 7 diode and NTC," Final Datasheet, Rev. 1.40, Jun. 2026. [Online]. Available: https://www.infineon.com

        # IGBT
        # Source: datasheet Fig. "Transient thermal impedance, IGBT, Inverter" (Foster r_i, τ_i), Σr_i = R_thJC = 17.7 K/kW

        self.r_I = np.array([0.68, 13.2, 2.84, 0.988]) * 1e-3  # [K/W] (datasheet in K/kW)
        self.tau_I = np.array([0.0022, 0.0457, 0.259, 3.31])  # [s]
        self.cap_I = self.tau_I / self.r_I  # [J/K]

        # Diode
        # Source: datasheet Fig. "Transient thermal impedance, Diode, Inverter" (Foster r_i, τ_i), Σr_i = R_thJC = 39.3 K/kW

        self.r_D = np.array([2.17, 24.9, 9.69, 2.52]) * 1e-3  # [K/W] (datasheet in K/kW)
        self.tau_D = np.array([0.0026, 0.038, 0.172, 2.17])  # [s]
        self.cap_D = self.tau_D / self.r_D  # [J/K]

        # Thermal Paste
        # Case-to-heatsink interface
        # Source: datasheet Table 4 / Table 6, R_thCH per IGBT = 10.4 K/kW, per diode = 15.4 K/kW (grease λ = 1 W/(m·K))
        # IGBT and diode paths share one case node in the model -> parallel combination

        self.r_paste = np.array([(10.4 * 15.4) / (10.4 + 15.4) * 1e-3])  # [K/W] = 0.0062 K/W
        self.tau_paste = np.array([1e-3])  # [s] grease stores almost no heat (placeholder)
        self.cap_paste = self.tau_paste / self.r_paste  # [J/K]

        # Heat Sink
        # Fischer Elektronik GmbH & Co. KG, "LA 10 150 24: Cooling aggregate with axial fan,"
        # Data sheet. [Online]. Available: https://www.fischerelektronik.de
        # 160 mm × 83 mm × 150 mm, hollow-fin profile, fan ebmpapst 8314H (24 V DC, 80 m³/h),
        # thermal resistance 0.2–0.055 K/W
        # Two aggregates per half-bridge module: one heat sink per switch -> R and C used directly
        # (lateral coupling through the module baseplate neglected)
        # Heat sink mass not given in datasheet (only fan weight) -> estimated from profile envelope:
        #   m = rho · L · (fill · W · H),  fill = aluminium share of cross-section (assumption, 0.25–0.35)

        R_heatsink = 0.125  # [K/W] LA 10 150 24 datasheet (middle value)

        W = 0.160  # [m] width (datasheet)
        H = 0.083  # [m] height (datasheet)
        L = 0.150  # [m] length (datasheet)
        fill = 0.30  # [-] aluminium share of cross-section (assumption, 0.25–0.35)
        rho_al = 2700  # [kg/m³] aluminium density
        c_al = 900  # [J/(kg·K)] aluminium specific heat

        A_cross = fill * W * H  # [m²] ≈ 0.0040 m²
        m_heatsink = rho_al * A_cross * L  # [kg] ≈ 1.61 kg
        Thermal_capacitance = m_heatsink * c_al  # [J/K] ≈ 726 J/K, half per switch

        self.r_sink = np.array([2 * R_heatsink])  # [K/W] = 0.40 K/W per switch
        self.cap_sink = np.array([Thermal_capacitance])  # [J/K] ≈ 726 J/K
        self.tau_sink = self.cap_sink * self.r_sink  # [s] ≈ 290 s

        # ----------------------------------------#
        # Switching losses
        # ----------------------------------------#

        # Infineon Technologies AG, "FF1800R23IE7: PrimePACK™3+ B-series module with TRENCHSTOP™ IGBT7 and emitter
        # controlled 7 diode and NTC," Final Datasheet, Rev. 1.40, Jun. 2026. [Online]. Available: https://www.infineon.com
        # All values at T_vj = 25 °C (model reference temperature), inductive load

        # IGBT
        # Source: datasheet Table 4, I_C = 1800 A, V_CC = 1200 V, V_GE = ±15 V, R_Gon = 0.1 Ω, R_Goff = 1.5 Ω, T_vj = 25 °C

        self.f_sw = 1000  # [Hz] switching frequency (1–2 kHz typical for 1500 V / MW-class modules)
        self.t_on = 0.602e-6  # [s] t_d(on) + t_r = 0.53 µs + 0.072 µs
        self.t_off = 1.725e-6  # [s] t_d(off) + t_f = 0.955 µs + 0.77 µs

        # Diode
        # Source: datasheet Table 6, V_CC = 1200 V, I_F = 1800 A, V_GE = -15 V, T_vj = 25 °C

        self.I_ref = 1800.0  # [A] test current
        self.V_ref = 1200.0  # [V] test voltage
        self.Err_D = 0.240  # [J] E_rec, reverse recovery energy per pulse (given directly in datasheet)

        # ----------------------------------------#
        # Conduction losses
        # ----------------------------------------#

        # Infineon Technologies AG, "FF1800R23IE7: PrimePACK™3+ B-series module with TRENCHSTOP™ IGBT7 and emitter
        # controlled 7 diode and NTC," Final Datasheet, Rev. 1.40, Jun. 2026. [Online]. Available: https://www.infineon.com

        # IGBT
        # Source: datasheet Fig. "Output characteristic (typical), IGBT, Inverter", V_GE = 15 V, T_vj = 25 °C

        I_I_Conduction_losses = np.array([600, 1200, 1800])  # [A]
        V_I_Conduction_losses = np.array([1.27, 1.56, 1.80])  # [V]

        self.R_IGBT, self.V_0_IGBT = np.polyfit(I_I_Conduction_losses, V_I_Conduction_losses, 1)

        # Diode
        # Source: datasheet Fig. "Forward characteristic (typical), Diode, Inverter", T_vj = 25 °C
        # 1800 A point from Table 6 (V_F typ. = 3.25 V); 600 A and 1200 A read from figure

        I_D_Conduction_losses = np.array([600, 1200, 1800])  # [A]
        V_D_Conduction_losses = np.array([2.08, 2.78, 3.25])  # [V]

        self.R_D, self.V_0_D = np.polyfit(I_D_Conduction_losses, V_D_Conduction_losses, 1)

        '''

        The following electrical inputs are required run the electro-thermal simulation:

        - Is  : RMS phase current on the AC side of the inverter (inverter output current)
        - V_dc: DC-link voltage supplied to the inverter
        - phi : Phase angle between voltage and current
        - pf  : Power factor
        - M   : Modulation index

        These values may be provided directly by the user, or they can be computed from a
        full inverter setup using mission-profile data. Using the inverter setup is often
        preferred, since voltage, current, and power-factor information can be extracted
        directly from realistic operating conditions (Mission profiles of Active and reactive power).

        It is also possible to bypass the inverter model entirely and supply the
        instantaneous device currents (is_I and is_D) directly along with above mentioned values directly.
        In that case, minor modifications to the code are required, but the approach is fully supported.

        '''

        # Check max package current limits along with  collector–emitter voltage limits (basically voltage on DC side)
        Calculation_functions_class.check_max_package_current_limit(Is=self.Is, M=self.M,
                                                                    max_IGBT_current=self.max_IGBT_current,
                                                                    max_diode_current=self.max_Diode_current)
        Calculation_functions_class.check_vce(self.V_dc, self.max_V_CE)

        self._standardize()

    def _standardize(self):
        """Convert all arrays to contiguous float64 and all floats to float64."""

        for name, value in self.__dict__.items():

            # Convert numpy arrays → contiguous float64
            if isinstance(value, np.ndarray):
                self.__dict__[name] = np.ascontiguousarray(value, dtype=np.float64)

            # Convert Python floats → float64
            elif isinstance(value, float) or isinstance(value, int):
                self.__dict__[name] = float(np.float64(value))

            # Convert lists into arrays
            elif isinstance(value, list):
                arr = np.ascontiguousarray(value, dtype=np.float64)
                self.__dict__[name] = arr