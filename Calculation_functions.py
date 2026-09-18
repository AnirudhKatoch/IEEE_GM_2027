import numpy as np
import numexpr as ne
from pathlib import Path
import rainflow
import pandas as pd
import shutil

class Calculation_functions_class:


    @staticmethod
    def compute_power_flow(P,
                           Q,
                           V_dc,
                           Vs,
                           M,
                           single_phase_inverter_topology,
                           inverter_phases,
                           modulation_scheme,
                           N_parallel):

        """
        Compute apparent power S, RMS current Is, and phase angle phi

        Parameters
        ----------
        P : array
            Active power per sec [W]
        Q : array
            Reactive power per sec [VAr]
        V_dc : array
             DC-side phase voltage per sec [V]
        Vs : array
             RMS AC-side phase voltage per sec [V]
        M : float
            Modulation index [-]
        single_phase_inverter_topology : {"half","full"}
            Inverter topology (affects Vs limit for single-phase).
        inverter_phases : {1,3}
            Number of phases. If 3, Vs is interpreted as PHASE RMS (i.e., V_ll/sqrt(3)).
        modulation_scheme : {"spwm","svm"}
            Modulation strategy used for generating inverter switching signals.

        Vs, Is, phi, V_dc, pf, M, S
        Returns
        -------

        Vs : array
             RMS AC-side phase voltage per sec [V]
        Is : array
            RMS current per sample [A].
        phi : array
            Phase angle between voltage and current per sample [rad]
        V_dc : array
            DC-side  voltage per sec [V]
        pf : array
            Power factor per sec [-].
        M : float
            Modulation index [-]
        S : array
            Apparent power per sample [VA].


        """

        P = P / N_parallel
        Q = Q / N_parallel

        pf = np.zeros_like(P, dtype=float)
        Is = np.zeros_like(P, dtype=float)  # [A] Inverter RMS current
        phi = np.zeros_like(P, dtype=float)  # [rad] Phase angle

        S = np.sqrt(P ** 2 + Q ** 2) # [VA] Inverter RMS apparent power

        # Case 1: P = 0 AND Q != 0 → pf = 0
        m_P0_Qnz = (P == 0) & (Q != 0)
        pf[m_P0_Qnz] = 0.0

        # Case 2: P != 0 AND Q = 0 → pf = ±1
        m_Pnz_Q0 = (P != 0) & (Q == 0)
        pf[m_Pnz_Q0] = np.sign(P[m_Pnz_Q0]) * 1.0

        # Case 3: General case (both P and Q nonzero)
        m_general = (P != 0) & (Q != 0)
        pf[m_general] = np.abs(P[m_general] / S[m_general])
        pf[(m_general & (Q < 0))] *= -1


        if inverter_phases == 1:
            if single_phase_inverter_topology == "full":
                Vs_theoretical = (M * V_dc) / np.sqrt(2.0)
            elif single_phase_inverter_topology == "half":
                Vs_theoretical = (M * V_dc) / (2.0 * np.sqrt(2.0))
        elif inverter_phases == 3:
            if modulation_scheme == "svm":
                # Space vector PWM (or 3rd harmonic injection)
                Vs_theoretical = (M * V_dc) / np.sqrt(6.0)  # [V RMS phase]
            elif modulation_scheme == "spwm":  # "spwm"
                # Sinusoidal PWM
                Vs_theoretical = (M * V_dc) / (2.0 * np.sqrt(2.0))

        if Vs.size == 0:
            Vs = Vs_theoretical.copy()

        else:
            indices = np.where(Vs > Vs_theoretical)[0]
            if indices.size > 0:
                raise ValueError(
                    f"Invalid input: AC phase RMS voltage exceeds the theoretical limit "
                    f"Vs must not be greater than {np.max(Vs_theoretical)}.")


        # masks
        m0 = pf == 0  # zero power factor
        mneg = pf < 0  # inductive
        mpos = pf > 0  # capacitive

        # ---- pf == 0 branch ----
        # P[i] = 0
        P[m0] = 0.0

        # S[i] = sqrt(P[i]^2 + Q[i]^2)  (with P already zeroed where m0)
        S[m0] = np.sqrt(P[m0] ** 2 + Q[m0] ** 2)

        # Is[i] = S[i] / Vs[i]
        with np.errstate(divide='ignore', invalid='ignore'):
            Is[m0] = S[m0] / (Vs[m0] if inverter_phases == 1 else (3.0 * Vs[m0]))

        # phi: 0 if S==0 else ±pi/2 depending on sign of Q
        phi[m0] = 0.0
        nz = m0 & (S != 0)
        phi[nz] = np.where(Q[nz] > 0, np.pi / 2, -np.pi / 2)

        # ---- pf != 0 branch ----
        abspf = np.abs(pf)
        mnz = ~m0  # pf != 0

        # S[i] = P[i] / abs(pf[i])
        S[mnz] = P[mnz] / abs(pf[mnz])

        # Is[i] = S[i] / Vs[i]
        with np.errstate(divide='ignore', invalid='ignore'):
            Is[mnz] = S[mnz] / (Vs[mnz] if inverter_phases == 1 else (3.0 * Vs[mnz]))

        # phi[i] = ± arccos(abs(pf[i]))
        phi[mneg] = -np.arccos(abspf[mneg])  # inductive
        phi[mpos] = np.arccos(abspf[mpos])  # capacitive

        # Q[i] = ± sqrt(S[i]^2 - P[i]^2) for pf != 0
        # (Note: numerical noise can make the radicand slightly negative; clip at 0.)
        rad = (S[mnz] ** 2 - P[mnz] ** 2)
        root = np.sqrt(rad)
        idx_mnz = np.where(mnz)[0]
        Q[idx_mnz[mneg[mnz]]] = -root[mneg[mnz]]
        Q[idx_mnz[mpos[mnz]]] = root[mpos[mnz]]

        return Vs, Is, phi, V_dc, pf, M, S

    @staticmethod
    def check_max_package_current_limit(Is,M, max_IGBT_current, max_diode_current):
        """
        Check that inverter RMS currents do not exceed device package limits.

        Parameters
        ----------
        Is : array
            RMS current on the AC side [A].
        max_IGBT_current : float
            Maximum allowable RMS current rating of the IGBT [A].
        max_diode_current : float, optional
            Maximum allowable RMS current rating of the diode [A].

        Raises
        ------
        ValueError
            If IGBT or diode RMS currents exceed their device ratings.
        """

        I_s_rms  = np.max(Is)
        Maximum_IGBT_current = 0.5 * I_s_rms * np.sqrt(1.0 + ((8.0 * M * 1.0) / (3.0 * np.pi)))
        Maximum_Diode_current = 0.5 * I_s_rms * np.sqrt(1.0 - ((8.0 * M * 1.0) / (3.0 * np.pi)))


        #print("Maximum_IGBT_current",Maximum_IGBT_current)

        # ---- IGBT CHECK ----
        if np.any(Maximum_IGBT_current > max_IGBT_current):
            raise ValueError(
                f"IGBT RMS current limit exceeded: "
                f"max allowed {max_IGBT_current} A"
            )

        if np.any(Maximum_Diode_current > max_diode_current):
                raise ValueError(
                    f"Diode RMS current limit exceeded: "
                    f"max allowed {max_diode_current} A"
                )


    @staticmethod
    def check_vce(V_dc, max_V_CE):
        """
        Check if collector–emitter voltage exceeds the maximum allowed value.

        Parameters
        ----------

        V_dc : float or np.ndarray
            DC link voltage (single value or array of values).
        max_V_CE : float
            Maximum allowed collector–emitter voltage.

        Raises
        ------
        UserWarning
            If the collector–emitter voltage exceeds max_V_CE.
        """
        V_CE = V_dc

        violations = np.where(V_CE > max_V_CE)[0]

        if violations.size > 0:
            raise ValueError(
                f"Collector–emitter voltage exceeded! "
                f"Maximum allowed: {max_V_CE}, but got values up to {V_CE.max()}. "
                "Please reduce the DC voltage or update the IGBT specifications."
            )

        return V_CE

    @staticmethod
    def Instantaneous_modulation(M, omega, t, phi):

        """
        Calculate the inverter modulation function m(t).

        Parameters
        ----------
        M : float
            Modulation index of the inverter [-] (typically 0.8–1.0 for PV inverters).
        omega : float
            Angular frequency of the AC grid [rad/s] (ω = 2πf).
        t : array
            Time instant [s].
        phi : float
            Phase angle of the inverter output current relative to the voltage [rad].

        Returns
        -------
        m : float
                Instantaneous modulation function [-].

        """

        m = (M * np.sin(omega * t + phi) + 1) / 2

        return m

    @staticmethod
    def IGBT_and_diode_current(Is, t, m, omega):

        """
        Calculate the instantaneous IGBT and diode currents in one inverter leg

        Parameters
        ----------
        Is : float
            RMS value of the inverter output current [A].
        t : array
            Time instant [s].
        m : array
            Instantaneous modulation function [-], typically between 0 and 1.

        Returns
        -------
        is_I : array
            Instantaneous IGBT current [A]. (Non-negative only, conduction blocked when negative.)
        is_D : array
            Instantaneous diode current [A]. (Non-negative only, conduction blocked when negative.)
        """

        base = np.sqrt(2) * Is * np.sin(omega * t) * m
        is_I = np.maximum(base, 0)
        is_D = np.maximum(-base, 0)

        return is_I, is_D

    @staticmethod
    def Switching_losses(V_dc, is_I, t_on, t_off, f_sw, is_D, I_ref, V_ref, Err_D):

        """
        Calculate the IGBT and diode switching power losses.

        Parameters
        ----------
        V_dc : float
            DC-link voltage of the inverter [V].
        is_I : array
            Instantaneous current through the IGBT [A].
        t_on : float
            Effective IGBT turn-on time [s].
        t_off : float
            Effective IGBT turn-off time [s].
        f_sw : float
            Inverter switching frequency [Hz].
        is_D : array
            Instantaneous current through the diode [A].
        I_ref : float
            Reference test current for diode reverse recovery [A].
        V_ref : float
            Reference test voltage for diode reverse recovery [V].
        Err_D : float
            Reverse recovery energy per switching event for the diode [J].

        Returns
        -------
        P_sw_I : array
            Instantaneous IGBT switching power loss [W].
        P_sw_D : array
            Instantaneous diode switching power loss [W].

        """

        is_I = np.ascontiguousarray(is_I, dtype=np.float64)
        is_D = np.ascontiguousarray(is_D, dtype=np.float64)

        # IGBT

        # E_on_I = ((np.sqrt(2) / (2 * np.pi)) * V_dc * is_I * t_on)
        # E_off_I = ((np.sqrt(2) / (2 * np.pi)) * V_dc * is_I * t_off)

        c1 = (np.sqrt(2) / (2 * np.pi))
        c2 = (np.sqrt(2) / np.pi)

        P_sw_I_expr = ne.evaluate("(( c1 * V_dc * is_I * t_on) + ( c1 * V_dc * is_I * t_off)) * f_sw",
                                  local_dict=dict(c1=c1, V_dc=V_dc, is_I=is_I, t_on=t_on, t_off=t_off, f_sw=f_sw), )
        P_sw_I = ne.evaluate("where(P_sw_I_expr > 0.0, P_sw_I_expr, 0.0)", local_dict=dict(P_sw_I_expr=P_sw_I_expr))

        # Diode

        P_sw_D_expr = ne.evaluate("((c2 * (is_D * V_dc) / (I_ref * V_ref)) * Err_D * f_sw)",
                                  local_dict=dict(c2=c2, V_dc=V_dc, is_D=is_D, f_sw=f_sw, I_ref=I_ref, V_ref=V_ref,
                                                  Err_D=Err_D), )
        # P_sw_D = np.maximum(P_sw_D, 0)
        P_sw_D = ne.evaluate("where(P_sw_D_expr > 0.0, P_sw_D_expr, 0.0)", local_dict=dict(P_sw_D_expr=P_sw_D_expr))

        return P_sw_I, P_sw_D

    @staticmethod
    def Conduction_losses(is_I, R_IGBT, V_0_IGBT, M, pf, is_D, R_D, V_0_D):

        """
        Calculate conduction losses of the inverter’s IGBT and diode.

        Parameters
        ----------
        is_I : array
            Instantaneous value of the inverter output current flowing through the IGBT [A].
        R_IGBT : float
            Effective on-resistance of the IGBT conduction model [Ohm].
        V_0_IGBT : float
            Effective knee voltage of the IGBT [V].
        M : float
            Modulation index of the inverter [-].
        pf : float
            Power factor of inverter output current [-].
            (negative = inductive load, current lags voltage;
             positive = capacitive load, current leads voltage).
        is_D : array
            Instantaneous value of the inverter output current flowing through the diode [A].
        R_D : float
            Effective dynamic resistance of the diode [Ohm].
        V_0_D : float
            Effective forward knee voltage of the diode [V].

        Returns
        -------
        P_con_I : array
            Instantaneous conduction loss of the IGBT [W].
        P_con_D : array
            Instantaneous conduction loss of the diode [W].
        """

        is_I = np.ascontiguousarray(is_I, dtype=np.float64)
        is_D = np.ascontiguousarray(is_D, dtype=np.float64)
        pf = np.ascontiguousarray(pf, dtype=np.float64)

        c1 = np.sqrt(2 * np.pi)
        c2 = (3 * np.pi)
        c3 = np.pi

        # IGBT

        # P_con_I = (((is_I ** 2 / 4.0) * R_IGBT) + ((is_I / np.sqrt(2 * np.pi)) * V_0_IGBT) +
        #           ((((is_I ** 2 / 4.0) * (8 * M / (3 * np.pi)) * R_IGBT) + (
        #                   (is_I / np.sqrt(2 * np.pi)) * (np.pi * M / 4.0) * V_0_IGBT)) * abs(pf)))
        # P_con_I = np.maximum(P_con_I, 0)

        P_con_I_expr = ne.evaluate("(((is_I ** 2 / 4.0) * R_IGBT) + ((is_I / c1) * V_0_IGBT) + "
                                   "((((is_I ** 2 / 4.0) * (8 * M / c2) * R_IGBT) +"
                                   " ((is_I / c1) * (c3 * M / 4.0) * V_0_IGBT)) * abs(pf)))",
                                   local_dict=dict(is_I=is_I, R_IGBT=R_IGBT, V_0_IGBT=V_0_IGBT, M=M, pf=pf, c1=c1,
                                                   c2=c2, c3=c3), )
        P_con_I = ne.evaluate("where(P_con_I_expr > 0.0, P_con_I_expr, 0.0)",
                              local_dict=dict(P_con_I_expr=P_con_I_expr))

        # Diode

        # P_con_D = ((((is_D ** 2 / 4.0) * R_D) + ((is_D / np.sqrt(2 * np.pi)) * V_0_D)) -
        #           ((((is_D ** 2 / 4.0)) * ((8 * M / (3 * np.pi)) * R_D)) + (
        #                       (is_D / np.sqrt(2 * np.pi)) * (np.pi * M / 4.0) * V_0_D)) * abs(pf))
        # P_con_D = np.maximum(P_con_D, 0)

        # Diode

        P_con_D_expr = ne.evaluate("((((is_D ** 2 / 4.0) * R_D) + ((is_D / c1) * V_0_D)) -"
                                   " ((((is_D ** 2 / 4.0)) * ((8 * M / c2) * R_D)) + "
                                   "((is_D / c1) * (c3 * M / 4.0) * V_0_D)) * abs(pf))",
                                   local_dict=dict(is_D=is_D, R_D=R_D, V_0_D=V_0_D, M=M, pf=pf, c1=c1, c2=c2, c3=c3), )
        P_con_D = ne.evaluate("where(P_con_D_expr > 0.0, P_con_D_expr, 0.0)",
                              local_dict=dict(P_con_D_expr=P_con_D_expr))

        return P_con_I, P_con_D

    @staticmethod
    def create_simulation_folders(sim_name=None, base="Results"):
        """
        Creates:
            Results/
                <sim_name>/  or  Simulation_N/
                    df_electrical_loss/
                    df_thermal/
                    Figures/
                    df_lifetime_IGBT/
                    df_lifetime_Diode/
                    df_electrical/
                    df_lifetime_IGBT_MC/
                    df_lifetime_Diode_MC/

        - sim_name given: folder is named after it. If it already exists, it is
          deleted and recreated, so old chunk files cannot mix with the new simulation.
        - sim_name not given: original behaviour, next free Simulation_N is created.

        Returns:
            sim_dir, df_electrical_loss_dir, df_thermal_dir, df_lifetime_IGBT_dir,
            df_lifetime_Diode_dir, df_electrical_dir, Figures_dir,
            df_lifetime_IGBT_MC_dir, df_lifetime_Diode_MC_dir
        """

        base_dir = Path(base)
        base_dir.mkdir(exist_ok=True)

        if sim_name is not None:
            # --- folder named after the profile ---
            sim_dir = base_dir / sim_name
            if sim_dir.exists():
                shutil.rmtree(sim_dir)  # start clean for this profile
            sim_dir.mkdir()

        else:
            # --- detect existing Simulation_N folders ---
            existing = []
            for p in base_dir.iterdir():
                if p.is_dir() and p.name.startswith("Simulation_"):
                    try:
                        existing.append(int(p.name.split("_")[1]))
                    except (IndexError, ValueError):
                        pass

            # --- choose next folder number ---
            next_n = max(existing) + 1 if existing else 1
            sim_dir = base_dir / f"Simulation_{next_n}"
            sim_dir.mkdir(exist_ok=True)

        # --- create subfolders ---
        df_electrical_loss_dir = sim_dir / "df_electrical_loss"
        df_thermal_dir = sim_dir / "df_thermal"
        Figures_dir = sim_dir / "Figures"
        df_lifetime_IGBT_dir = sim_dir / "df_lifetime_IGBT"
        df_lifetime_Diode_dir = sim_dir / "df_lifetime_Diode"
        df_electrical_dir = sim_dir / "df_electrical"
        df_lifetime_IGBT_MC_dir = sim_dir / "df_lifetime_IGBT_MC"
        df_lifetime_Diode_MC_dir = sim_dir / "df_lifetime_Diode_MC"

        for d in (df_electrical_loss_dir, df_thermal_dir, Figures_dir, df_lifetime_IGBT_dir,
                  df_lifetime_Diode_dir, df_electrical_dir, df_lifetime_IGBT_MC_dir, df_lifetime_Diode_MC_dir):
            d.mkdir(exist_ok=True)

        return (sim_dir, df_electrical_loss_dir, df_thermal_dir, df_lifetime_IGBT_dir,
                df_lifetime_Diode_dir, df_electrical_dir, Figures_dir,
                df_lifetime_IGBT_MC_dir, df_lifetime_Diode_MC_dir)




    @staticmethod
    def rainflow_algorithm(temp, dt):
        """
        Compute ΔT, T_mean, t_on for each rainflow cycle of a temperature signal.

        Parameters
        ----------
        temp : 1D array
            Temperature signal (e.g. Tj_igbt) [K or °C].
        dt : float
            Time step [s] of the signal (e.g. 0.001).

        Returns
        -------
        dT : 1D array
            Cycle ranges ΔT.
        Tmean : 1D array
            Cycle mean temperature.
        t_on : 1D array
            Heating time per cycle [s], defined as |end_idx - start_idx| * dt.
        count : 1D array
            Cycle count (usually 0.5 or 1.0).
        """
        temp = np.asarray(temp, dtype=float)

        cycles = list(rainflow.extract_cycles(temp))
        if len(cycles) == 0:
            return (np.empty(0), np.empty(0), np.empty(0), np.empty(0))

        cycles = np.array(cycles, dtype=float)
        dT = cycles[:, 0]
        Tmean = cycles[:, 1]
        count = cycles[:, 2]
        starts = cycles[:, 3].astype(int)
        ends = cycles[:, 4].astype(int)

        # Option A: compute t_on via sample distance * dt
        thermal_cycle_period = np.abs(ends - starts) * dt

        # (equivalent to np.abs(ends - starts) / steps_per_sec)

        return dT, Tmean, thermal_cycle_period, count


    @staticmethod
    def cycles_to_failure_lesit(deltaT,  # ΔT_j   : array or scalar
                                Tmean,  # T_jm   : array or scalar (K)
                                thermal_cycle_period,  # : array or scalar (s)
                                A0,
                                A1,
                                T0_K,
                                lambda_K,  # T0_K, λ
                                alpha,
                                Ea_J,
                                kB_J_per_K,  # activation energy, Boltzmann
                                C,
                                gamma,
                                k_thickness):  # k_thickness for IGBT or diode

        """

        Parameters
        ----------
        deltaT : array
                Junction temperature swing per cycle ΔTj [K].
        Tmean : array
            Mean (medium) junction temperature per cycle Tjm [K].
        thermal_cycle_period : array
            Heating time per cycle ton [s]
        A0 : float
            Technology coefficient A0 [-]
        A1 : float
            Factor A1 for the low-ΔT extension [-].
        T0_K : float
            Reference temperature T0 for the low-ΔT extension [K].
        lambda_K : float
            Decay constant λ for the low-ΔT extension [K].
        alpha : float
            Coffin–Manson exponent α (typically negative) [-].
        Ea_J : float
            Activation energy Ea [J]. **Use Joules, not eV.**
        kB_J_per_K : float
            Boltzmann constant k_B [J/K].
        C : float
            Time-shape coefficient C [-] in the ton-scaling term.
        gamma : float
            Time-shape exponent γ [-] in the ton-scaling term.
        k_thickness : float
            Chip thickness factor kthickness [-], accounting for
            chip thickness / technology (e.g. 1.0, 0.65, 0.5, 0.33).

        Returns
        -------
        Nf : ndarray
            Cycles-to-failure estimate per cycle Nf [-].
        """

        # Make sure inputs are float64 and contiguous (good for numexpr)
        deltaT = np.ascontiguousarray(deltaT, dtype=np.float64)
        Tmean = np.ascontiguousarray(Tmean, dtype=np.float64)
        thermal_cycle_period = np.ascontiguousarray(thermal_cycle_period, dtype=np.float64)

        if np.any(Tmean <= 0):
            raise ValueError("Tmean contains 0 K or negative values, which is not physically possible.")

        # Arrhenius temperature factor: exp(Ea / (kB * Tmean))
        c_arrhenius = ne.evaluate("exp(Ea_J / (kB_J_per_K * Tmean))",
                                  local_dict=dict(Ea_J=Ea_J, kB_J_per_K=kB_J_per_K, Tmean=Tmean))

        # exp_low = exp( - (ΔT - T0_K) / λ )
        exp_low = ne.evaluate("exp(-(deltaT - T0_K) / lambda_K)",
                              local_dict=dict(deltaT=deltaT, T0_K=T0_K, lambda_K=lambda_K))

        Nf = ne.evaluate(
            "A0 * (A1 ** exp_low) * "
            "(deltaT ** (alpha - exp_low)) * "
            "c_arrhenius * "
            "((C + thermal_cycle_period**gamma) / (C + 2.0**gamma)) * "
            "k_thickness",
            local_dict=dict(A0=A0, A1=A1, alpha=alpha, C=C,
                            gamma=gamma, k_thickness=k_thickness, deltaT=deltaT, exp_low=exp_low,
                            c_arrhenius=c_arrhenius, thermal_cycle_period=thermal_cycle_period))
        return Nf

    @staticmethod
    def miners_rule(Nf, count, Is, input_step, f):
        Nf = np.asarray(Nf, dtype=float)
        count = np.asarray(count, dtype=float)

        # Filter out invalid entries
        mask = (Nf > 0) & np.isfinite(Nf) & np.isfinite(count)
        Nf = Nf[mask]
        count = count[mask]

        # Damage over one mission: D = Σ (count_i / Nf_i)
        D = np.sum(count / Nf)

        # Number of times the mission can be repeated before failure
        Nf_eq = np.inf if D == 0 else 1.0 / D

        mission_seconds_total = len(Is) * input_step  # Is has one value per input step
        seconds_per_year = 365 * 24 * 3600

        lifetime_years = Nf_eq * mission_seconds_total / seconds_per_year

        # Equivalent grid-frequency cycles to failure (target for Monte Carlo)
        cycles_per_year = seconds_per_year * f
        Nf_target_MC = cycles_per_year * lifetime_years

        return Nf_eq, lifetime_years, Nf_target_MC

    @staticmethod
    def read_datafames(df_dir):
        df_dir = Path(df_dir)

        # If df_dir is relative, make it relative to this file's directory
        if not df_dir.is_absolute():
            base_dir = Path(__file__).resolve().parent
            df_dir = base_dir / df_dir

        if not df_dir.exists():
            raise FileNotFoundError(f"Directory does not exist: {df_dir}")

        all_files = sorted(df_dir.glob("df_*.parquet"))
        if not all_files:
            raise ValueError(f"No parquet files matching 'df_*.parquet' in {df_dir}")

        df_list = [pd.read_parquet(f) for f in all_files]
        full_df = pd.concat(df_list, ignore_index=True)
        return full_df

    @staticmethod
    def check_igbt_diode_temp_limits(Tj_igbt, Tj_diode,max_IGBT_temperature,max_Diode_temperature):

        if  (np.max(Tj_igbt) > max_IGBT_temperature):
            raise ValueError(f"IGBT junction temperature exceeded! "
                             f"Max temperature is {np.max(Tj_igbt - 273.15)} Celsius.")

        if  (np.max(Tj_diode) > max_Diode_temperature):
            raise ValueError(f"Diode  junction temperature exceeded! "
                             f"Max temperature is {np.max(Tj_diode - 273.15)} Celsius.")


    @staticmethod
    def residual_deltaT_MC(deltaT, Nf_target, Tmean, thermal_cycle_period,
                           A0, A1, T0_K, lambda_K, alpha, Ea_J, kB_J_per_K,
                           C, gamma, k_thickness):

        # Arrhenius temperature factor: exp(Ea / (kB * Tmean))
        c_arrhenius = ne.evaluate("exp(Ea_J / (kB_J_per_K * Tmean))",
                                  local_dict=dict(Ea_J=Ea_J, kB_J_per_K=kB_J_per_K, Tmean=Tmean))

        # exp_low = exp( - (ΔT - T0_K) / λ )
        exp_low = ne.evaluate("exp(-(deltaT - T0_K) / lambda_K)",
                              local_dict=dict(deltaT=deltaT, T0_K=T0_K, lambda_K=lambda_K))

        Nf = ne.evaluate(
            "A0 * (A1 ** exp_low) * "
            "(deltaT ** (alpha - exp_low)) * "
            "c_arrhenius * "
            "((C + thermal_cycle_period**gamma) / (C + 2.0**gamma)) * "
            "k_thickness",
            local_dict=dict(A0=A0, A1=A1, alpha=alpha, C=C,
                            gamma=gamma, k_thickness=k_thickness, deltaT=deltaT, exp_low=exp_low,
                            c_arrhenius=c_arrhenius, thermal_cycle_period=thermal_cycle_period))

        return Nf - Nf_target

    @staticmethod
    def normal_distributio_MC(Tj_mean_MC, deltaT_MC, thermal_cycle_period_MC, A0, A1, T0_K, lambda_K, alpha, Ea_J,
                              kB_J_per_K, C, gamma, k_thickness, normal_distribution, number_of_samples):

        """
        Create Monte Carlo samples for ALL stress parameters and ALL
        lifetime-model parameters using a normal distribution.

        Parameters are interpreted as the *nominal values* around which
        the samples are drawn.
        """

        def normal_distribution_function(variable, normal_distribution, number_of_samples):
            sigma = normal_distribution * abs(variable)
            samples = np.random.normal(variable, sigma, number_of_samples)
            return samples

        # --------------------------------------------
        # Generate samples for equivalent stress values
        # --------------------------------------------

        Tj_mean_samples = normal_distribution_function(Tj_mean_MC, normal_distribution, number_of_samples)
        deltaT_samples = normal_distribution_function(deltaT_MC, normal_distribution, number_of_samples)
        thermal_period_samples = normal_distribution_function(thermal_cycle_period_MC, normal_distribution,
                                                              number_of_samples)

        # --------------------------------------------
        # Generate samples for lifetime-model parameters
        # --------------------------------------------
        A0_samples = normal_distribution_function(A0, normal_distribution, number_of_samples)
        A1_samples = normal_distribution_function(A1, normal_distribution, number_of_samples)
        T0_K_samples = normal_distribution_function(T0_K, normal_distribution, number_of_samples)
        lambda_K_samples = normal_distribution_function(lambda_K, normal_distribution, number_of_samples)
        alpha_samples = normal_distribution_function(alpha, normal_distribution, number_of_samples)
        C_samples = normal_distribution_function(C, normal_distribution, number_of_samples)
        gamma_samples = normal_distribution_function(gamma, normal_distribution, number_of_samples)
        k_th_samples = normal_distribution_function(k_thickness, normal_distribution, number_of_samples)

        Ea_J_samples = np.full(number_of_samples, Ea_J)
        kB_samples = np.full(number_of_samples, kB_J_per_K)

        return {"Tj_mean": Tj_mean_samples, "deltaT": deltaT_samples, "thermal_period": thermal_period_samples,
                "A0": A0_samples, "A1": A1_samples, "T0_K": T0_K_samples, "lambda_K": lambda_K_samples,
                "alpha": alpha_samples, "Ea_J": Ea_J_samples, "kB_J_per_K": kB_samples, "C": C_samples,
                "gamma": gamma_samples, "k_thickness": k_th_samples}