import numpy as np
from Calculation_functions import Calculation_functions_class


class Input_parameters_class:

    def __init__(self):

        Profile_size = 2

        # ----------------------------------------#
        # Model Parameters
        # ----------------------------------------#

        self.dt = 0.001                   # Simulation step size
        self.input_step = 0.02            # Simulation step size
        self.chunk_seconds = int(86400)   # chunking to reduce the RAM usage
        self.Plotting_electrical_flag = True # True False
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

        self.A0 = 2.9e9            # Technology Coefficient
        self.A1 = 60              # Factor of Low ΔTj Extension
        self.T0_K = 40            # Initial Temperature for Low ΔTj Extension [K]
        self.lambda_K = 17        # Drop Constant of Low ΔTj Extension [K]
        self.alpha = -4.3         # Coffin-Manson Exponent
        self.Ea_J = 4.50e-20      # Activation Energy [J]
        self.kB_J_per_K = 1.38e-23 # Boltzmann Constant [J/K]
        self.C = 1                # Time Coefficient
        self.gamma = -0.75        # Time Exponent
        self.k_thickness = {"IGBT":1, "Diode":0.5} # Standard 600–1200 V IGBT chip (default)
        #  k_thickness = 1.00   → Standard IGBT chips (600 V / 1200 V classes)
        #  k_thickness = 0.65   → Thick-chip IGBT (1700 V class)
        #  k_thickness = 0.50   → Rectifier / diode chips (typically thicker silicon)
        #  k_thickness = 0.33   → SiC MOSFET / SiC diode chips (much thinner)

        # ----------------------------------------#
        # Package max limits
        # ----------------------------------------#

        self.max_V_CE = 600  # [V] Maximum collector–emitter voltage
        self.max_IGBT_current = 50          # [A] Maximum IGBT Current
        self.max_IGBT_temperature = 448.15  # [K] Maximum IGBT temperature
        self.max_Diode_current = 30         # [A] Maximum Diode Current limit
        self.max_Diode_temperature = 448.15 # [K] Maximum Diode temperature
        self.IGBT_max_life = 15 # years
        self.Diode_max_life = 15  # years

        # ----------------------------------------#
        # Miscellaneous
        # ----------------------------------------#

        self.f = 50                                                               # [Hz] Grid frequency
        self.omega = 2 * np.pi * self.f                                           # [rad/s] Angular frequency of the grid (ω = 2πf)

        # ----------------------------------------#
        # Thermal Parameters
        # ----------------------------------------#

        self.deltaT_min = 30             # As LESIT model is invalid below 30 K hence we are going to clamp any value below 30 K as 30 K
        self.T_env = np.full(Profile_size, 298.15, dtype=np.float64)  # [K] Ambient Temperature
        self.thermal_model = "fastest"  # "transient", "fast" or "fastest"

        # IGBT

        # Source: Infineon IKW50N60H3 datasheet, Fig. 21 (Foster RC coefficients)

        self.r_I = np.array([7.0e-3, 3.736e-2, 9.205e-2, 1.2996e-1, 1.8355e-1])  # [K/W] Thermal resistance
        self.tau_I = np.array([4.4e-5, 1.0e-4, 7.2e-4, 8.3e-3, 7.425e-2])        # [s] Thermal time constant
        self.cap_I = self.tau_I / self.r_I                                       # [J/K] Thermal capacitance

        # Diode

        # Source: Infineon IKW50N60H3 datasheet, Fig. 22 (Foster RC coefficients)

        self.r_D = np.array([4.915956e-2, 2.254532e-1, 3.125229e-1, 2.677344e-1, 1.951733e-1])  # [K/W] Thermal resistance
        self.tau_D = np.array([7.5e-6, 2.2e-4, 2.3e-3, 1.546046e-2, 1.078904e-1])               # [s]   Thermal time constant
        self.cap_D = self.tau_D / self.r_D                            # [J/K] Thermal capacitance


        # Thermal Paste

        # Case-to-sink thermal interface
        # Source:  (Thermal Grizzly Kryonaut)

        self.r_paste = np.array([0.0032])  # [K/W] Thermal resistance
        self.tau_paste = np.array([1e-3])  # [s]   Thermal time constant, this value is always almost zero for thermal pastes
        self.cap_paste = self.tau_paste / self.r_paste  # [J/K] Thermal capacitance

        # Heat Sink

        # Sink-to-ambient heat sink
        # Source: Cooling Innovation 3-121211U
        r_sink_dic = {1:2.0, 2:1.14, 3:0.83, 4:0.66}  # These are different thermal resistance values at different air flows in m/s
        r_sink = float(r_sink_dic[2])
        #r_sink = 4
        Weight = 19/1000 # kg

        specific_heat = 900 # J/kg K
        Thermal_capacitance = Weight * specific_heat

        self.r_sink = np.array(r_sink)  # [K/W] Thermal resistance
        self.tau_sink = np.array([Thermal_capacitance * r_sink])  # [s]   Thermal time constant
        self.cap_sink = np.array([Thermal_capacitance])    # [J/K] Thermal capacitance

        # ----------------------------------------#
        # Switching losses
        # ----------------------------------------#

        # IGBT

        self.f_sw = 10 * 1000  # [Hz] Inverter switching frequency
        self.t_on = 60e-9      # [s] Effective turn-on time = td(on) + tr ≈ 23 ns + 37 ns (td is delay period and tr is rising time)  [Note: Value is temperature dependent, author assumes constant temp of 25°C] [Page 5 datasheet]
        self.t_off = 259e-9    # [s] Effective turn-off time = td(off) + tf ≈ 235 ns + 24 ns (td is delay period and tf is fall time) [Note: Value is temperature dependent, author assumes constant temp of 25°C] [Page 5 datasheet]

        # Diode

        self.I_ref = 30.0   # [A] Reference test current for diode reverse recovery  [Note: Value is temperature dependent, author assumes constant temp of 25°C] [Page 6 datasheet]
        self.V_ref = 400.0  # [V] Reference test voltage for diode reverse recovery  [Note: Value is temperature dependent, author assumes constant temp of 25°C] [Page 6 datasheet]

        Q_rr = 0.88e-6                  # [C] reverse recovery charge #  [Note: Value is temperature dependent, author assumes constant temp of 25°C] [Page 5 datasheet]
        self.Err_D = Q_rr * self.V_ref  # [J] Reverse recovery energy per switching event

        # ----------------------------------------#
        # Conduction losses
        # ----------------------------------------#

        # IGBT

        I_I_Conduction_losses = np.array([25, 50, 100])            # Current in Amps    [Note: Value is temperature and current dependent, author assumes constant current of 50 A and temp of 25°C] [Fig 8]
        V_I_Conduction_losses = np.array([1.425, 1.800, 2.500])    # Vce(sat) in Volts   [Note: Value is temperature and current dependent, author assumes constant current of 50 A and temp of 25°C] [Fig 8]

        self.R_IGBT, self.V_0_IGBT = np.polyfit(I_I_Conduction_losses, V_I_Conduction_losses, 1)
        # R_IGBT # [Ohm] Effective on-resistance for conduction model
        # V_0_IGBT #  [V]   Effective knee voltage

        # Diode

        I_D_Conduction_losses  = np.array([15, 30, 60])        # diode current in A         Note: Value is temperature and current dependent, author assumes constant current of 50 A and temp of 25°C] [Fig 28]
        V_D_Conduction_losses  = np.array([1.35, 1.65, 2.1])  # diode forward voltage in V Note: Value is temperature and current dependent, author assumes constant current of 50 A and temp of 25°C] [Fig 28]

        self.R_D, self.V_0_D = np.polyfit(I_D_Conduction_losses, V_D_Conduction_losses, 1)
        # V_0_D  # [V]    Effective forward knee voltage
        # R_D # [Ohm]  Effective dynamic resistance

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

        self.P = np.full(Profile_size, 48790)  # [W]   Inverter RMS Active power  [Will always be positive] # Rated power = 48790
        self.Q = np.full(Profile_size, 0)  # [VAr] Inverter RMS Reactive power [Negative is inductive and positive is capacitive]

        self.Vs = np.full(Profile_size, 230)  # [V] Inverter phase RMS AC side voltage
        self.V_dc = np.full(Profile_size, 600)  # [V] Inverter DC side voltage

        self.M = 1 # [-] Inverter modulation index # Modulation cannot be above 1 as model does not take into account. +

        self.inverter_phases = 3   # 1 or 3 (single-phase or three-phase)
        if self.inverter_phases not in (1, 3):
            raise ValueError("phases must be 1 or 3")

        self.modulation_scheme = "svm"  # options: "spwm" or "svm" , the type of modulation once can choose for three phase inverters."svm" is  Space Vector PWM (or Third-Harmonic Injection) and "spwm" is Sinusoidal PWM (reference = pure sine).
        if self.modulation_scheme not in ("spwm", "svm"):  # when inverter_phases == 1 this variable is invalid.
            raise ValueError("modulation_scheme must be 'spwm' or 'svm'")

        self.single_phase_inverter_topology = "full"  # options: "half" or "full"  # One can choose is the single phase inverter half bridge or full bridge
        if self.single_phase_inverter_topology not in ("half", "full"):  # when inverter_phases == 3 this variable is invalid.
            raise ValueError("single_phase_inverter_topology must be 'half' or 'full'")

        self.N_parallel = 1 # This variable defines the number of switches in parallel per leg

        self.Vs, self.Is, self.phi, self.V_dc, self.pf, self.M, self.S = Calculation_functions_class.compute_power_flow(P=self.P,
                                                                                  Q=self.Q,
                                                                                  V_dc=self.V_dc,
                                                                                  Vs=self.Vs,
                                                                                  M=self.M,
                                                                                  single_phase_inverter_topology=self.single_phase_inverter_topology,
                                                                                  inverter_phases=self.inverter_phases,
                                                                                  modulation_scheme=self.modulation_scheme,
                                                                                  N_parallel= self.N_parallel)

        # Check max package current limits along with  collector–emitter voltage limits (basically voltage on DC side)
        Calculation_functions_class.check_max_package_current_limit(Is=self.Is, M=self.M, max_IGBT_current=self.max_IGBT_current,max_diode_current=self.max_Diode_current)
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