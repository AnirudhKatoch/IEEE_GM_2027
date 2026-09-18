from Input_parameters import Input_parameters_class
import numpy as np
from Calculation_functions import Calculation_functions_class
from Electrical_model import compute_IGBT_and_Diode_power_losses
import time
from Thermal_model import simulate_igbt_diode_cauer_transient,simulate_igbt_diode_cauer_fast,simulate_igbt_diode_cauer_fastest
import pandas as pd
from Plotting_results import Plotting_lifetime,Plotting_electrical,Plotting_electrical_loss,Plotting_thermal, Plotting_Monte_Carlo
Calculation_functions = Calculation_functions_class()

def mother_function(Load,sim_name):

    start_time = time.time()

    # ----------------------------------------#
    # Input parameters
    # ----------------------------------------#

    params = Input_parameters_class(Load=Load)

    dt = params.dt; chunk_seconds = params.chunk_seconds; input_step = params.input_step
    Plotting_electrical_flag = params.Plotting_electrical_flag; Plotting_lifetime_flag = params.Plotting_lifetime_flag; Plotting_electrical_loss_flag = params.Plotting_electrical_loss_flag; Plotting_thermal_flag = params.Plotting_thermal_flag; Plotting_Monte_Carlo_flag = params.Plotting_Monte_Carlo_flag;

    A0 = params.A0; A1 = params.A1; T0_K =  params.T0_K; lambda_K = params.lambda_K; alpha = params.alpha; Ea_J = params.Ea_J; kB_J_per_K = params.kB_J_per_K; C = params.C; gamma = params.gamma; k_thickness = params.k_thickness

    max_IGBT_temperature = params.max_IGBT_temperature; max_Diode_temperature = params.max_Diode_temperature

    f = params.f; omega = params.omega; T0_init = params.T0_init; IGBT_max_life = params.IGBT_max_life; Diode_max_life = params.Diode_max_life

    Cauer_model_accuracy = params.Cauer_model_accuracy; T_env = params.T_env
    thermal_model = params.thermal_model
    r_I =params.r_I; cap_I = params.cap_I; r_D = params.r_D; cap_D = params.cap_D; r_paste = params.r_paste; cap_paste = params.cap_paste; r_sink = params.r_sink; cap_sink = params.cap_sink

    f_sw = params.f_sw; t_on = params.t_on; t_off = params.t_off; I_ref = params.I_ref; V_ref = params.V_ref; Err_D = params.Err_D
    R_IGBT = params.R_IGBT; V_0_IGBT = params.V_0_IGBT; R_D = params.R_D; V_0_D = params.V_0_D

    S = params.S; P = params.P; Q = params.Q; pf = params.pf; Vs = params.Vs; Is = params.Is; V_dc = params.V_dc; phi = params.phi; M = params.M

    sim_dir, df_electrical_loss_dir, df_thermal_dir, df_lifetime_IGBT_dir, df_lifetime_Diode_dir, df_electrical_dir, Figures_dir, df_lifetime_IGBT_MC_dir, df_lifetime_Diode_MC_dir = Calculation_functions.create_simulation_folders(sim_name)

    # ----------------------------------------#
    # Chunking setup
    # ----------------------------------------#

    samples_per_step = int(round(input_step / dt))  # e.g. 20 for dt=0.001, input_step=0.02
    steps_per_chunk = int(round(chunk_seconds / input_step))  # input steps per chunk
    N_steps = len(Is)  # number of input steps
    n_chunks = int(np.ceil(N_steps / steps_per_chunk))

    for chunk_idx in range(n_chunks):

        step_start = chunk_idx * steps_per_chunk
        step_end = min(step_start + steps_per_chunk, N_steps)

        # print(f"\n--- Chunk {chunk_idx+1}/{n_chunks} ---")

        Is_chunk = Is[step_start:step_end]
        phi_chunk = phi[step_start:step_end]
        V_dc_chunk = V_dc[step_start:step_end]
        pf_chunk = pf[step_start:step_end]
        T_env_chunk = T_env[step_start:step_end]


        # ----------------------------------------#
        # Electrical calculations
        # ----------------------------------------#

        # Temporary containers for 1-second segments of power losses and electrical outputs
        P_I_list     = []; P_D_list     = []; is_I_list    = []; is_D_list    = []
        P_sw_I_list  = []; P_sw_D_list  = []; P_con_I_list = []; P_con_D_list = []

        for i,(Is_i, phi_i, V_dc_i, pf_i) in enumerate(zip(Is_chunk, phi_chunk, V_dc_chunk, pf_chunk)):

            P_I_sec, P_D_sec, is_I_sec, is_D_sec, P_sw_I_sec, P_sw_D_sec, P_con_I_sec, P_con_D_sec = compute_IGBT_and_Diode_power_losses(Is=Is_i, phi=phi_i, V_dc=V_dc_i, pf=pf_i, dt=dt,
                                                                                                                                         M=M, omega=omega, t_on=t_on, t_off=t_off, f_sw=f_sw, I_ref=I_ref, V_ref=V_ref, Err_D=Err_D,
                                                                                                                                         R_IGBT=R_IGBT, V_0_IGBT=V_0_IGBT, R_D=R_D, V_0_D=V_0_D,input_step=input_step)

            # Append each 1-second result of power losses and electrical outputs
            P_I_list.append(P_I_sec); P_D_list.append(P_D_sec); is_I_list.append(is_I_sec); is_D_list.append(is_D_sec)
            P_sw_I_list.append(P_sw_I_sec); P_sw_D_list.append(P_sw_D_sec); P_con_I_list.append(P_con_I_sec); P_con_D_list.append(P_con_D_sec)

        # Concatenate into final full length arrays of power losses and electrical outputs
        P_I = np.concatenate(P_I_list); P_D = np.concatenate(P_D_list); is_I = np.concatenate(is_I_list); is_D = np.concatenate(is_D_list)
        P_sw_I = np.concatenate(P_sw_I_list); P_sw_D = np.concatenate(P_sw_D_list); P_con_I = np.concatenate(P_con_I_list); P_con_D = np.concatenate(P_con_D_list)

        # ----------------------------------------#
        # Thermal calculations
        # ----------------------------------------#

        T_env_samples = np.repeat(T_env_chunk, samples_per_step)

        if thermal_model in ("transient", "fast"):

            model_function = (simulate_igbt_diode_cauer_transient if thermal_model == "transient"
                              else simulate_igbt_diode_cauer_fast)

            time_local, T_i, T_d, T_p, T_s = model_function(
                r_I=r_I, cap_I=cap_I, r_D=r_D, cap_D=cap_D,
                r_paste=r_paste, cap_paste=cap_paste, r_sink=r_sink, cap_sink=cap_sink,
                P_I=P_I, P_D=P_D, T_env=T_env_samples, dt=dt,
                method="BDF", rtol=Cauer_model_accuracy, atol=1e-6, debug=False, T0_init=T0_init)

            # last state of this chunk -> start of next chunk
            T0_init = np.concatenate([T_i[:, -1], T_d[:, -1], T_p[:, -1], T_s[:, -1]])

            Tj_igbt = T_i[0, :]
            Tj_diode = T_d[0, :]
            T_case = T_p[0, :]
            T_sink = T_s[0, :]

            del T_i, T_d, T_p, T_s

        elif thermal_model == "fastest":
            time_local, Tj_igbt, Tj_diode, T_case, T_sink, T0_init = simulate_igbt_diode_cauer_fastest(
                r_I=r_I, cap_I=cap_I, r_D=r_D, cap_D=cap_D,
                r_paste=r_paste, cap_paste=cap_paste, r_sink=r_sink, cap_sink=cap_sink,
                P_I=P_I, P_D=P_D, T_env=T_env_samples, dt=dt, T0_init=T0_init)
        else:
            raise ValueError("thermal_model must be 'transient', 'fast' or 'fastest'")

        time_global = time_local + step_start * input_step

        #Calculation_functions.check_igbt_diode_temp_limits(Tj_igbt=Tj_igbt,Tj_diode=Tj_diode,max_IGBT_temperature=max_IGBT_temperature,max_Diode_temperature=max_Diode_temperature)

        df_electrical_loss_chunk = pd.DataFrame({"time": time_global, "P_I": P_I, "P_D": P_D, "is_I": is_I, "is_D": is_D, "P_sw_I": P_sw_I, "P_sw_D": P_sw_D, "P_con_I": P_con_I, "P_con_D": P_con_D})
        df_electrical_loss_chunk.to_parquet(df_electrical_loss_dir / f"df_{chunk_idx + 1}.parquet", index=False,engine="pyarrow")

        df_thermal_chunk = pd.DataFrame({"time": time_global, "Tj_igbt": Tj_igbt, "Tj_diode": Tj_diode, "T_case": T_case, "T_sink": T_sink, })
        df_thermal_chunk.to_parquet(df_thermal_dir / f"df_{chunk_idx + 1}.parquet", index=False,engine="pyarrow")

        # Delete all large electrical arrays
        del P_I, P_D, is_I, is_D, P_sw_I, P_sw_D, P_con_I, P_con_D
        del P_I_list , P_D_list , is_I_list , is_D_list , P_sw_I_list , P_sw_D_list , P_con_I_list , P_con_D_list

        # Delete thermal arrays
        del T_case, T_sink

        # Delete dataframes
        del df_electrical_loss_chunk
        del df_thermal_chunk

        # Delete input chunks
        del Is_chunk, phi_chunk, V_dc_chunk, pf_chunk, T_env_chunk

        # Delete time arrays
        del time_local, time_global

        deltaT_igbt, Tmean_igbt, thermal_cycle_period_igbt, count_igbt = Calculation_functions.rainflow_algorithm(Tj_igbt,dt)
        deltaT_diode, Tmean_diode, thermal_cycle_period_diode, count_diode = Calculation_functions.rainflow_algorithm(Tj_diode, dt)

        #deltaT_igbt = np.clip(deltaT_igbt, 20,200)
        #deltaT_diode = np.clip(deltaT_diode, 20,200)

        # Delete thermal arrays
        del Tj_igbt, Tj_diode

        # ----------------------------------------#
        # Lifetime calculations
        # ----------------------------------------#

        Nf_igbt = Calculation_functions.cycles_to_failure_lesit(deltaT=deltaT_igbt, Tmean=Tmean_igbt,
                                                                      thermal_cycle_period=thermal_cycle_period_igbt, A0=A0,
                                                                      A1=A1, T0_K=T0_K, lambda_K=lambda_K, alpha=alpha,
                                                                      Ea_J=Ea_J, kB_J_per_K=kB_J_per_K, C=C, gamma=gamma,
                                                                      k_thickness=k_thickness["IGBT"])

        Nf_diode = Calculation_functions.cycles_to_failure_lesit(deltaT=deltaT_diode, Tmean=Tmean_diode,
                                                                      thermal_cycle_period=thermal_cycle_period_diode, A0=A0,
                                                                      A1=A1, T0_K=T0_K, lambda_K=lambda_K, alpha=alpha,
                                                                      Ea_J=Ea_J, kB_J_per_K=kB_J_per_K, C=C, gamma=gamma,
                                                                      k_thickness=k_thickness["Diode"])

        df_lifetime_IGBT_chunk = pd.DataFrame({"deltaT_igbt": deltaT_igbt, "Tmean_igbt": Tmean_igbt, "thermal_cycle_period_igbt": thermal_cycle_period_igbt, "count_igbt":count_igbt, "Nf_igbt": Nf_igbt})
        df_lifetime_IGBT_chunk.to_parquet(df_lifetime_IGBT_dir / f"df_{chunk_idx + 1}.parquet", index=False, engine="pyarrow")

        del deltaT_igbt, Tmean_igbt, thermal_cycle_period_igbt, count_igbt, Nf_igbt, df_lifetime_IGBT_chunk

        df_lifetime_Diode_chunk = pd.DataFrame({"deltaT_diode": deltaT_diode, "Tmean_diode": Tmean_diode, "thermal_cycle_period_diode": thermal_cycle_period_diode,"count_diode":count_diode,"Nf_diode": Nf_diode})
        df_lifetime_Diode_chunk.to_parquet(df_lifetime_Diode_dir / f"df_{chunk_idx + 1}.parquet", index=False,engine="pyarrow")

        del deltaT_diode, Tmean_diode, thermal_cycle_period_diode, Nf_diode, count_diode, df_lifetime_Diode_chunk

    # ----------------------------------------#
    # Electrical saving and plotting
    # ----------------------------------------#

    if Plotting_electrical_flag == True:
        Plotting_electrical(S=S,P=P,Q=Q,Vs=Vs,Is=Is,V_dc=V_dc,pf=pf,phi=phi,T_env=T_env,Figures_dir=Figures_dir, input_step=input_step)
    df_electrical = pd.DataFrame({ "S":S, "P":P, "Q":Q, "pf":pf, "Vs":Vs, "Is": Is, "V_dc":V_dc, "phi":phi, "T_env":T_env})
    df_electrical.to_parquet(df_electrical_dir / f"df.parquet", index=False,engine="pyarrow")
    del S, P, Q, pf, Vs , V_dc, phi, T_env, df_electrical

    # ----------------------------------------#
    # Lifetime saving and plotting
    # ----------------------------------------#

    df_IGBT = Calculation_functions.read_datafames(df_dir=df_lifetime_IGBT_dir)
    Nf_igbt = df_IGBT["Nf_igbt"].to_numpy()
    count_igbt = df_IGBT["count_igbt"].to_numpy()
    Nf_igbt_eq, lifetime_years_igbt_actual, Nf_target_igbt_MC = Calculation_functions.miners_rule(Nf=Nf_igbt, count=count_igbt, Is=Is, input_step=input_step, f=f)
    lifetime_years_igbt = np.minimum(lifetime_years_igbt_actual, IGBT_max_life)

    df_IGBT.loc[df_IGBT.index[0], ["Nf_igbt_eq","lifetime_years_igbt", "Nf_target_igbt_MC", "lifetime_years_igbt_actual"]] \
        = [float(Nf_igbt_eq),float(lifetime_years_igbt),float(Nf_target_igbt_MC),float(lifetime_years_igbt_actual),]
    df_IGBT.to_parquet(df_lifetime_IGBT_dir / "df_IGBT_final.parquet",index=False,engine="pyarrow")


    df_Diode = Calculation_functions.read_datafames(df_dir=df_lifetime_Diode_dir)
    Nf_diode = df_Diode["Nf_diode"].to_numpy()
    count_diode = df_Diode["count_diode"].to_numpy()
    Nf_diode_eq, lifetime_years_diode_actual, Nf_target_diode_MC = Calculation_functions.miners_rule(Nf=Nf_diode, count=count_diode, Is=Is, input_step=input_step, f=f)
    lifetime_years_diode = np.minimum(lifetime_years_diode_actual, Diode_max_life)

    df_Diode.loc[df_Diode.index[0], ["Nf_diode_eq", "lifetime_years_diode", "Nf_target_diode_MC", "lifetime_years_diode_actual"]] \
        = [float(Nf_diode_eq), float(lifetime_years_diode), float(Nf_target_diode_MC), float(lifetime_years_diode_actual),]
    df_Diode.to_parquet(df_lifetime_Diode_dir / "df_Diode_final.parquet",index=False,engine="pyarrow")

    del Is

    if Plotting_lifetime_flag == True:
        Plotting_lifetime(df_IGBT=df_IGBT, df_Diode=df_Diode, Nf_igbt_eq=Nf_igbt_eq, lifetime_years_igbt=lifetime_years_igbt, Nf_diode_eq=Nf_diode_eq, lifetime_years_diode=lifetime_years_diode,Figures_dir=Figures_dir)
    del lifetime_years_igbt,lifetime_years_diode,Nf_igbt_eq,Nf_diode_eq,df_IGBT,df_Diode,Nf_igbt,count_igbt,Nf_diode,count_diode

    # ----------------------------------------#
    # Electrical loss plotting
    # ----------------------------------------#

    if Plotting_electrical_loss_flag == True:
        df_electrical_loss = Calculation_functions.read_datafames(df_dir=df_electrical_loss_dir)
        Plotting_electrical_loss(df_electrical_loss=df_electrical_loss, Figures_dir=Figures_dir)
        del df_electrical_loss

    # ----------------------------------------#
    # Thermal plotting
    # ----------------------------------------#

    df_thermal = Calculation_functions.read_datafames(df_dir=df_thermal_dir)
    if Plotting_thermal_flag == True:
        Plotting_thermal(df_thermal=df_thermal, Figures_dir=Figures_dir)

    '''
    # ----------------------------------------#
    # Monte carlo calculations
    # ----------------------------------------#

    Tj_igbt_mean_MC = np.mean(df_thermal["Tj_igbt"])
    thermal_cycle_period_igbt_MC = 1/f
    Tj_diode_mean_MC = np.mean(df_thermal["Tj_diode"])
    thermal_cycle_period_diode_MC = 1/f
    del df_thermal

    deltaT_igbt_MC = brentq(Calculation_functions.residual_deltaT_MC,1.0, 150.0, args=(Nf_target_igbt_MC, Tj_igbt_mean_MC, thermal_cycle_period_igbt_MC,A0, A1, T0_K, lambda_K, alpha, Ea_J, kB_J_per_K,C, gamma, k_thickness["IGBT"]))
    deltaT_diode_MC = brentq(Calculation_functions.residual_deltaT_MC,1.0, 150.0, args=(Nf_target_diode_MC, Tj_diode_mean_MC, thermal_cycle_period_diode_MC,A0, A1, T0_K, lambda_K, alpha, Ea_J, kB_J_per_K,C, gamma, k_thickness["Diode"]))

    Igbt_MC_distribution_MC = Calculation_functions.normal_distributio_MC(Tj_mean_MC=Tj_igbt_mean_MC, deltaT_MC=deltaT_igbt_MC,
                                                    thermal_cycle_period_MC = thermal_cycle_period_igbt_MC,
                                                    A0=A0, A1=A1, T0_K=T0_K, lambda_K=lambda_K, alpha=alpha, Ea_J=Ea_J,
                                                    kB_J_per_K=kB_J_per_K, C= C, gamma=gamma, k_thickness=k_thickness["IGBT"],
                                                    normal_distribution = 0.01, number_of_samples=10000)

    Diode_MC_distribution_MC = Calculation_functions.normal_distributio_MC(Tj_mean_MC=Tj_diode_mean_MC, deltaT_MC=deltaT_diode_MC,
                                                    thermal_cycle_period_MC = thermal_cycle_period_diode_MC,
                                                    A0=A0, A1=A1, T0_K=T0_K, lambda_K=lambda_K, alpha=alpha, Ea_J=Ea_J,
                                                    kB_J_per_K=kB_J_per_K, C= C, gamma=gamma, k_thickness=k_thickness["Diode"],
                                                    normal_distribution = 0.01, number_of_samples=10000)

    Nf_igbt_MC = Calculation_functions.cycles_to_failure_lesit(deltaT=Igbt_MC_distribution_MC["deltaT"], Tmean=Igbt_MC_distribution_MC["Tj_mean"],
                                                               thermal_cycle_period=Igbt_MC_distribution_MC["thermal_period"],
                                                               A0=Igbt_MC_distribution_MC["A0"], A1=Igbt_MC_distribution_MC["A1"],
                                                               T0_K=Igbt_MC_distribution_MC["T0_K"], lambda_K=Igbt_MC_distribution_MC["lambda_K"],
                                                               alpha=Igbt_MC_distribution_MC["alpha"], Ea_J=Igbt_MC_distribution_MC["Ea_J"],
                                                               kB_J_per_K=Igbt_MC_distribution_MC["kB_J_per_K"],
                                                               C=Igbt_MC_distribution_MC["C"], gamma=Igbt_MC_distribution_MC["gamma"],
                                                               k_thickness=Igbt_MC_distribution_MC["k_thickness"])

    Nf_Diode_MC = Calculation_functions.cycles_to_failure_lesit(deltaT=Diode_MC_distribution_MC["deltaT"], Tmean=Diode_MC_distribution_MC["Tj_mean"],
                                                               thermal_cycle_period=Diode_MC_distribution_MC["thermal_period"],
                                                               A0=Diode_MC_distribution_MC["A0"], A1=Diode_MC_distribution_MC["A1"],
                                                               T0_K=Diode_MC_distribution_MC["T0_K"], lambda_K=Diode_MC_distribution_MC["lambda_K"],
                                                               alpha=Diode_MC_distribution_MC["alpha"], Ea_J=Diode_MC_distribution_MC["Ea_J"],
                                                               kB_J_per_K=Diode_MC_distribution_MC["kB_J_per_K"],
                                                               C=Diode_MC_distribution_MC["C"], gamma=Diode_MC_distribution_MC["gamma"],
                                                               k_thickness=Diode_MC_distribution_MC["k_thickness"])

    Lifetime_igbt_MC_actual  = Nf_igbt_MC/(3600*24*365*f)
    Lifetime_igbt_MC = np.minimum(Lifetime_igbt_MC_actual, IGBT_max_life)

    df_lifetime_igbt_MC = pd.DataFrame(Igbt_MC_distribution_MC)
    df_lifetime_igbt_MC["Nf_igbt_MC"] = Nf_igbt_MC
    df_lifetime_igbt_MC["Lifetime_igbt_MC"] = Lifetime_igbt_MC
    df_lifetime_igbt_MC["Lifetime_igbt_MC_actual"] = Lifetime_igbt_MC_actual
    df_lifetime_igbt_MC.to_parquet( df_lifetime_IGBT_MC_dir / f"df.parquet", index=False,engine="pyarrow")

    Lifetime_diode_MC_actual  = Nf_Diode_MC/(3600*24*365*f)
    Lifetime_diode_MC = np.minimum(Lifetime_diode_MC_actual, Diode_max_life)

    df_lifetime_diode_MC = pd.DataFrame(Diode_MC_distribution_MC)
    df_lifetime_diode_MC["Nf_Diode_MC"] = Nf_Diode_MC
    df_lifetime_diode_MC["Lifetime_diode_MC"] = Lifetime_diode_MC
    df_lifetime_diode_MC["Lifetime_diode_MC_actual"] = Lifetime_diode_MC_actual
    df_lifetime_diode_MC.to_parquet( df_lifetime_Diode_MC_dir/ f"df.parquet", index=False,engine="pyarrow")


    if Plotting_Monte_Carlo_flag == True:
        Plotting_Monte_Carlo(df_lifetime_igbt_MC=df_lifetime_igbt_MC,df_lifetime_diode_MC=df_lifetime_diode_MC, Figures_dir=Figures_dir)

    del df_lifetime_igbt_MC, Igbt_MC_distribution_MC, Nf_igbt_MC, Lifetime_igbt_MC, df_lifetime_diode_MC, Diode_MC_distribution_MC, Nf_Diode_MC, Lifetime_diode_MC
    '''

    end_time = time.time()
    print("Execution time all code:", end_time - start_time, "seconds")

