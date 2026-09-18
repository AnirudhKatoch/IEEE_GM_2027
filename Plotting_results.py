import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import weibull_min

def Plotting_electrical(S,P,Q,Vs,Is,V_dc,pf,phi,T_env, Figures_dir, input_step):

    time_axis = np.arange(len(Is)) * input_step

    # -------------------------------------------------
    # Figure 1: Apparent, Active, Reactive Power (S, P, Q)
    # -------------------------------------------------

    fig1, ax1 = plt.subplots(3, 1, figsize=(6.4, 6), sharex=True)

    ax1[0].plot(time_axis,S)
    ax1[0].set_ylabel("S [VA]")
    ax1[0].set_title("Apparent Power (S)")
    ax1[0].grid(True)
    ax1[0].set_xlim(min(time_axis),max(time_axis))

    ax1[1].plot(time_axis,P)
    ax1[1].set_ylabel("P [W]")
    ax1[1].set_title("Active Power (P)")
    ax1[1].grid(True)
    ax1[1].set_xlim(min(time_axis), max(time_axis))

    ax1[2].plot(time_axis,Q)
    ax1[2].set_ylabel("Q [VAR]")
    ax1[2].set_xlabel("Time [s]")
    ax1[2].set_title("Reactive Power (Q)")
    ax1[2].grid(True)
    ax1[2].set_xlim(min(time_axis), max(time_axis))

    plt.tight_layout()
    plt.savefig(Figures_dir / "1_S_P_Q.png")
    plt.close(fig1)

    # -------------------------------------------------
    # Figure 2: Voltage and Current (Vs, Is)
    # -------------------------------------------------

    fig2, ax2 = plt.subplots(2, 1, figsize=(6.4, 6), sharex=True)

    ax2[0].plot(time_axis,Vs)
    ax2[0].set_ylabel("Vs [V]")
    ax2[0].set_title("Supply Voltage (Vs)")
    ax2[0].grid(True)
    ax2[0].set_xlim(min(time_axis), max(time_axis))

    ax2[1].plot(time_axis,Is)
    ax2[1].set_ylabel("Is [A]")
    ax2[1].set_xlabel("Time [s]")
    ax2[1].set_title("Supply Current (Is)")
    ax2[1].grid(True)
    ax2[1].set_xlim(min(time_axis), max(time_axis))

    plt.tight_layout()
    plt.savefig(Figures_dir / "2_Vs_Is.png")
    plt.close(fig2)

    # -------------------------------------------------
    # Figure 3: Power Factor and Phase Angle (pf, phi)
    # -------------------------------------------------

    fig3, ax3 = plt.subplots(2, 1, figsize=(6.4, 6), sharex=True)

    ax3[0].plot(time_axis,pf)
    ax3[0].set_ylabel("pf [-]")
    ax3[0].set_title("Power Factor")
    ax3[0].grid(True)
    ax3[0].set_xlim(min(time_axis), max(time_axis))

    ax3[1].plot(time_axis,phi)
    ax3[1].set_ylabel("phi [rad]")
    ax3[1].set_xlabel("Time [s]")
    ax3[1].set_title("Phase Angle (phi)")
    ax3[1].grid(True)
    ax3[1].set_xlim(min(time_axis), max(time_axis))

    plt.tight_layout()
    plt.savefig(Figures_dir / "3_pf_phi.png")
    plt.close(fig3)

    # -------------------------------------------------
    # Figure 4: DC Link Voltage (V_dc)
    # -------------------------------------------------

    fig4, ax4 = plt.subplots(figsize=(6.4, 4.8))

    ax4.plot(time_axis,V_dc)
    ax4.set_ylabel("V_dc [V]")
    ax4.set_xlabel("Time [s]")
    ax4.set_title("DC Link Voltage (V_dc)")
    ax4.grid(True)
    ax4.set_xlim(min(time_axis), max(time_axis))

    plt.tight_layout()
    plt.savefig(Figures_dir / "4_Vdc.png")
    plt.close(fig4)

    # -------------------------------------------------
    # Figure 5: Ambient Temperature (T_env)
    # -------------------------------------------------

    fig5, ax5 = plt.subplots(figsize=(6.4, 4.8))

    ax5.plot(time_axis,T_env-273.15)
    ax5.set_ylabel("T_env [C]")
    ax5.set_xlabel("Time [s]")
    ax5.set_title("Ambient Temperature (T_env)")
    ax5.grid(True)
    ax5.set_xlim(min(time_axis), max(time_axis))

    plt.tight_layout()
    plt.savefig(Figures_dir / "5_T_env.png")
    plt.close(fig5)

def Plotting_lifetime(df_IGBT, df_Diode, Nf_igbt_eq, lifetime_years_igbt, Nf_diode_eq, lifetime_years_diode, Figures_dir):

    # -------------------------------------------------
    # Figure 6: IGBT and Diode Lifetime
    # -------------------------------------------------

    fig6, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6), sharex=False)

    ax1.plot(df_Diode["Nf_diode"])
    ax1.set_yscale("log")  # <-- LOG SCALE
    ax1.set_ylabel("Nf Diode")
    ax1.set_title("Diode – Number of cycles to failure")
    ax1.grid(True)

    ax2.plot(df_IGBT["Nf_igbt"])
    ax2.set_yscale("log")  # <-- LOG SCALE
    ax2.set_xlabel("Cycle index")
    ax2.set_ylabel("Nf IGBT")
    ax2.set_title("IGBT – Number of cycles to failure")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(Figures_dir / "6_IGBT_and_Diode_number_of_cycles_separate.png")
    plt.close(fig6)

    # -------------------------------------------------
    # Figure 7: DeltaT Comparison
    # -------------------------------------------------

    fig7, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6), sharex=False)

    ax1.plot(df_Diode["deltaT_diode"])
    ax1.set_ylabel("ΔT Diode [C]")
    ax1.set_title("Diode – Temperature Swing (ΔT)")
    ax1.grid(True)

    ax2.plot(df_IGBT["deltaT_igbt"])
    ax2.set_xlabel("Cycle index")
    ax2.set_ylabel("ΔT IGBT [C]")
    ax2.set_title("IGBT – Temperature Swing (ΔT)")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(Figures_dir / "7_DeltaT_IGBT_and_Diode.png")
    plt.close(fig7)

    # -------------------------------------------------
    # Figure 8: Tmean Comparison
    # -------------------------------------------------

    fig8, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6), sharex=False)

    ax1.plot(df_Diode["Tmean_diode"] - 273.15)
    ax1.set_ylabel("Tmean Diode [C]")
    ax1.set_title("Diode – Mean Temperature (Tmean)")
    ax1.grid(True)


    ax2.plot(df_IGBT["Tmean_igbt"] - 273.15)
    ax2.set_xlabel("Cycle index")
    ax2.set_ylabel("Tmean IGBT [C]")
    ax2.set_title("IGBT – Mean Temperature (Tmean)")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(Figures_dir / "8_Tmean_IGBT_and_Diode.png")
    plt.close(fig8)

    # -------------------------------------------------
    # Figure 9: Thermal Cycle Period
    # -------------------------------------------------

    fig9, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6), sharex=False)

    ax1.plot(df_Diode["thermal_cycle_period_diode"])
    ax1.set_ylabel("Period Diode [s]")
    ax1.set_title("Diode – Thermal Cycle Period")
    ax1.set_ylim(0, 0.2)
    ax1.grid(True)

    ax2.plot(df_IGBT["thermal_cycle_period_igbt"])
    ax2.set_xlabel("Cycle index")
    ax2.set_ylabel("Period IGBT [s]")
    ax2.set_title("IGBT – Thermal Cycle Period")
    ax2.set_ylim(0, 0.2)
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(Figures_dir / "9_ThermalCyclePeriod_IGBT_and_Diode.png")
    plt.close(fig9)

    # -------------------------------------------------
    # Figure 10: Cycle Count
    # -------------------------------------------------

    fig10, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 6), sharex=False)

    ax1.plot(df_Diode["count_diode"])
    ax1.set_ylabel("Count Diode")
    ax1.set_title("Diode – Cycle Count")
    ax1.grid(True)

    ax2.plot(df_IGBT["count_igbt"])
    ax2.set_xlabel("Cycle index")
    ax2.set_ylabel("Count IGBT")
    ax2.set_title("IGBT – Cycle Count")
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(Figures_dir / "10_CycleCount_IGBT_and_Diode.png")
    plt.close(fig10)

    # -------------------------------------------------
    # Figure 11: Equivalent Nf Comparison (Twin Y-Axis)
    # -------------------------------------------------

    fig11, ax_left = plt.subplots(figsize=(6.4, 4.8))

    # Bar positions
    x_left = 0  # IGBT
    x_right = 1  # Diode

    # Plot IGBT bar on left axis
    ax_left.bar(x_left, Nf_igbt_eq, width=0.5, color="C0")
    ax_left.set_ylabel("IGBT Equivalent Nf")

    # Create right axis
    ax_right = ax_left.twinx()

    # Plot Diode bar on right axis
    ax_right.bar(x_right, Nf_diode_eq, width=0.5, color="C1")
    ax_right.set_ylabel("Diode Equivalent Nf")

    # Set title
    ax_left.set_title("IGBT vs Diode – Equivalent Number of Cycles to Failure")

    # Set x-ticks and labels
    ax_left.set_xticks([x_left, x_right])
    ax_left.set_xticklabels(["IGBT", "Diode"])

    # Grid on the left axis only
    ax_left.grid(axis="y")

    plt.tight_layout()
    plt.savefig(Figures_dir / "11_Equivalent_Nf_TwinAxis.png")
    plt.close(fig11)

    # -------------------------------------------------
    # Figure 11a: Minimum Equivalent Nf (limiting device)
    # -------------------------------------------------

    if Nf_igbt_eq <= Nf_diode_eq:
        Nf_min, device_min, color_min = Nf_igbt_eq, "IGBT", "C0"
    else:
        Nf_min, device_min, color_min = Nf_diode_eq, "Diode", "C1"

    fig11a, ax11a = plt.subplots(figsize=(6.4, 4.8))

    ax11a.bar(0, Nf_min, width=0.5, color=color_min)
    ax11a.set_xticks([0])
    ax11a.set_xticklabels([device_min])
    ax11a.set_ylabel("Equivalent Nf")
    ax11a.set_title(f"Limiting device: {device_min} (Nf = {Nf_min:.3e})")
    ax11a.grid(axis="y")

    plt.tight_layout()
    plt.savefig(Figures_dir / "11a_Nf.png")
    plt.close(fig11a)

    # -------------------------------------------------
    # Figure 12: Lifetime (Years) with Twin Y-Axis
    # -------------------------------------------------

    fig12, ax_left = plt.subplots(figsize=(6.4, 4.8))

    # Bar positions
    x_left = 0  # IGBT
    x_right = 1  # Diode

    # Plot IGBT bar on left axis
    ax_left.bar(x_left, lifetime_years_igbt, width=0.5, color="C0", label="IGBT")

    # Create right axis
    ax_right = ax_left.twinx()

    # Plot Diode bar on right axis
    ax_right.bar(x_right, lifetime_years_diode, width=0.5, color="C1", label="Diode")

    # Set axis labels
    ax_left.set_ylabel("IGBT Lifetime [years]")
    ax_right.set_ylabel("Diode Lifetime [years]")

    # Set title
    ax_left.set_title("IGBT vs Diode – Lifetime in Years ")

    # Set x-ticks and labels
    ax_left.set_xticks([x_left, x_right])
    ax_left.set_xticklabels(["IGBT", "Diode"])

    # Grid only for left axis
    ax_left.grid(axis="y")

    plt.tight_layout()
    plt.savefig(Figures_dir / "12_Lifetime_Years_TwinAxis.png")
    plt.close(fig12)

    # -------------------------------------------------
    # Figure 12a: Lifetime of Switch (Minimum of IGBT/Diode)
    # -------------------------------------------------

    # Switch lifetime = the smaller of the two
    lifetime_years_switch = min(lifetime_years_igbt, lifetime_years_diode)

    fig12a, ax = plt.subplots(figsize=(6.4, 4.8))

    # Simple single bar
    ax.bar(0, lifetime_years_switch, width=0.5, color="C2", label="Switch")

    # Labels and title
    ax.set_ylabel("Switch Lifetime [years]")
    ax.set_title("Switch Lifetime (Min of IGBT & Diode)")

    # X-axis label
    ax.set_xticks([0])
    ax.set_xticklabels(["Switch"])

    # Grid for readability
    ax.grid(axis="y")

    plt.tight_layout()
    plt.savefig(Figures_dir / "12a_Lifetime_Switch.png")
    plt.close(fig12a)

def Plotting_electrical_loss(df_electrical_loss, Figures_dir):

    # -------------------------------------------------
    # Figure 13: IGBT & Diode Total Power Losses (P_I, P_D)
    # -------------------------------------------------

    fig13, ax = plt.subplots(figsize=(6.4, 4.8))

    #print("P_I",np.sqrt(np.mean(df_electrical_loss["P_I"] ** 2)))
    #print("P_D", np.sqrt(np.mean(df_electrical_loss["P_D"] ** 2)))

    ax.plot(df_electrical_loss["time"], df_electrical_loss["P_I"], label="P_I (IGBT)")
    ax.plot(df_electrical_loss["time"], df_electrical_loss["P_D"], label="P_D (Diode)")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Power Loss [W]")
    ax.set_title("Total Power Losses – IGBT & Diode")
    ax.legend(loc="best")
    ax.grid(True)
    ax.set_xlim(min(df_electrical_loss["time"]),max(df_electrical_loss["time"]))

    plt.tight_layout()
    plt.savefig(Figures_dir / "13_PowerLoss_P_I_P_D.png")
    plt.close(fig13)

    # -------------------------------------------------
    # Figure 14: IGBT & Diode Currents (is_I, is_D)
    # -------------------------------------------------

    fig14, ax = plt.subplots(figsize=(6.4, 4.8))

    #print("is_I",np.sqrt(np.mean(df_electrical_loss["is_I"] ** 2)))
    #print("is_D", np.sqrt(np.mean(df_electrical_loss["is_D"] ** 2)))

    ax.plot(df_electrical_loss["time"], df_electrical_loss["is_I"], label="is_I (IGBT)")
    ax.plot(df_electrical_loss["time"], df_electrical_loss["is_D"], label="is_D (Diode)")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Current [A]")
    ax.set_title("Device Currents – IGBT & Diode")
    ax.legend(loc="best")
    ax.grid(True)
    ax.set_xlim(min(df_electrical_loss["time"]), max(df_electrical_loss["time"]))

    plt.tight_layout()
    plt.savefig(Figures_dir / "14_Currents_is_I_is_D.png")
    plt.close(fig14)

    # -------------------------------------------------
    # Figure 15: IGBT & Diode Switching Losses (P_sw_I, P_sw_D)
    # -------------------------------------------------

    fig15, ax = plt.subplots(figsize=(6.4, 4.8))

    ax.plot(df_electrical_loss["time"], df_electrical_loss["P_sw_I"], label="P_sw_I (IGBT)")
    ax.plot(df_electrical_loss["time"], df_electrical_loss["P_sw_D"], label="P_sw_D (Diode)")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Switching Loss [W]")
    ax.set_title("Switching Losses – IGBT & Diode")
    ax.legend(loc="best")
    ax.grid(True)
    ax.set_xlim(min(df_electrical_loss["time"]), max(df_electrical_loss["time"]))

    plt.tight_layout()
    plt.savefig(Figures_dir / "15_SwitchingLosses_P_sw_I_P_sw_D.png")
    plt.close(fig15)

    # -------------------------------------------------
    # Figure 16: IGBT & Diode Conduction Losses (P_con_I, P_con_D)
    # -------------------------------------------------

    fig16, ax = plt.subplots(figsize=(6.4, 4.8))

    ax.plot(df_electrical_loss["time"], df_electrical_loss["P_con_I"], label="P_con_I (IGBT)")
    ax.plot(df_electrical_loss["time"], df_electrical_loss["P_con_D"], label="P_con_D (Diode)")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Conduction Loss [W]")
    ax.set_title("Conduction Losses – IGBT & Diode")
    ax.legend(loc="best")
    ax.grid(True)
    ax.set_xlim(min(df_electrical_loss["time"]), max(df_electrical_loss["time"]))

    plt.tight_layout()
    plt.savefig(Figures_dir / "16_ConductionLosses_P_con_I_P_con_D.png")
    plt.close(fig16)

def Plotting_thermal(df_thermal, Figures_dir):

    # -------------------------------------------------
    # Figure 17: Junction Temperatures (Tj_igbt, Tj_diode)
    # -------------------------------------------------

    #print("Tj_igbt",np.sqrt(np.mean((df_thermal["Tj_igbt"]-273.15) ** 2)))
    #print("Tj_diode", np.sqrt(np.mean((df_thermal["Tj_diode"]-273.15) ** 2)))

    fig17, ax = plt.subplots(figsize=(6.4, 4.8))

    ax.plot(df_thermal["time"], df_thermal["Tj_igbt"] - 273.15, label="Tj_IGBT [°C]")
    ax.plot(df_thermal["time"], df_thermal["Tj_diode"] - 273.15, label="Tj_Diode [°C]")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Temperature [°C]")
    ax.set_title("Junction Temperatures – IGBT & Diode")
    ax.legend(loc="best")
    ax.grid(True)
    ax.set_xlim(min(df_thermal["time"]), max(df_thermal["time"]))

    plt.tight_layout()
    plt.savefig(Figures_dir / "17_JunctionTemperatures_IGBT_Diode.png")
    plt.close(fig17)

    # -------------------------------------------------
    # Figure 18: Case and Heat Sink Temperatures (T_case, T_sink)
    # -------------------------------------------------

    #print("T_case",np.sqrt(np.mean((df_thermal["T_case"]-273.15) ** 2)))
    #print("T_sink", np.sqrt(np.mean((df_thermal["T_sink"]-273.15) ** 2)))

    fig18, ax = plt.subplots(figsize=(6.4, 4.8))

    ax.plot(df_thermal["time"], df_thermal["T_case"] - 273.15, label="T_case [°C]")
    ax.plot(df_thermal["time"], df_thermal["T_sink"] - 273.15, label="T_sink [°C]")

    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Temperature [°C]")
    ax.set_title("Case & Heat Sink Temperatures")
    ax.legend(loc="best")
    ax.grid(True)
    ax.set_xlim(min(df_thermal["time"]), max(df_thermal["time"]))

    plt.tight_layout()
    plt.savefig(Figures_dir / "18_Tcase_Tsink.png")
    plt.close(fig18)

def Plotting_Monte_Carlo(df_lifetime_igbt_MC, df_lifetime_diode_MC, Figures_dir):

    # -------------------------------------------------
    # Figure 19: Weibull PDF for IGBT Lifetime
    # -------------------------------------------------

    lifetimes_igbt = df_lifetime_igbt_MC["Lifetime_igbt_MC"].values

    # If all values are identical → add tiny variation (0.1%)
    if np.std(lifetimes_igbt) < 1e-12:
        lifetimes_igbt = lifetimes_igbt + np.random.normal(loc=0.0, scale=0.0001 * lifetimes_igbt[0], size=len(lifetimes_igbt))

    # --- Fit Weibull distribution (IGBT) ---
    beta_igbt, _, eta_igbt = weibull_min.fit(lifetimes_igbt, floc=0.0)

    # --- x-range (use full lifetime range for IGBT) ---
    t_min_igbt, t_max_igbt = np.quantile(lifetimes_igbt, [0.0, 1.0])
    t_vals_igbt = np.linspace(t_min_igbt, t_max_igbt, 500)

    # --- Weibull PDF for IGBT ---
    pdf_vals_igbt = ((beta_igbt / eta_igbt) * (t_vals_igbt / eta_igbt) ** (beta_igbt - 1) * np.exp(-(t_vals_igbt / eta_igbt) ** beta_igbt))

    # --- Build the plot (IGBT) ---
    fig19, ax19 = plt.subplots(figsize=(6.4, 4.8))

    # Histogram (PDF-normalized)
    ax19.hist(lifetimes_igbt, bins=40, range=(t_min_igbt, t_max_igbt), density=True, alpha=0.75, color="salmon", edgecolor="black")

    # Overlay Weibull PDF
    ax19.plot(t_vals_igbt, pdf_vals_igbt, 'k-', linewidth=2, label="Weibull PDF")

    ax19.set_xlabel("Lifetime of IGBT [years]")
    ax19.set_ylabel("Lifetime distribution f(x)  (PDF)")
    ax19.set_title("IGBT – Lifetime Distribution and Weibull PDF")
    ax19.grid(True)
    ax19.legend(loc="best")

    ax19.set_xlim(t_min_igbt, t_max_igbt)

    plt.tight_layout()
    plt.savefig(Figures_dir / "19_weibull_pdf_hist_IGBT.png")
    plt.close(fig19)

    # -------------------------------------------------
    # Figure 20: Weibull PDF for Diode Lifetime
    # -------------------------------------------------

    lifetimes_diode = df_lifetime_diode_MC["Lifetime_diode_MC"].values

    # If all values are identical → add tiny variation (0.1%)
    if np.std(lifetimes_diode) < 1e-12:
        lifetimes_diode = lifetimes_diode + np.random.normal(loc=0.0, scale=0.0001 * lifetimes_diode[0], size=len(lifetimes_diode))

    # --- Fit Weibull: shape = beta_diode, scale = eta_diode ---
    beta_diode, _, eta_diode = weibull_min.fit(lifetimes_diode, floc=0.0)

    # --- x-range for plotting (same idea as for IGBT) ---
    t_min_diode, t_max_diode = np.quantile(lifetimes_diode, [0, 1])
    t_vals_diode = np.linspace(t_min_diode, t_max_diode, 500)

    # --- Weibull PDF ---
    pdf_vals_diode = ((beta_diode / eta_diode) * (t_vals_diode / eta_diode) ** (beta_diode - 1) * np.exp(-(t_vals_diode / eta_diode) ** beta_diode))

    # --- Build the plot (Fig. 20 style) ---
    fig20, ax = plt.subplots(figsize=(6.4, 4.8))

    # Histogram of lifetimes, normalized (PDF)
    ax.hist(lifetimes_diode, bins=40, range=(t_min_diode, t_max_diode), density=True, alpha=0.75, color="salmon", edgecolor="black")

    # Overlay Weibull PDF
    ax.plot(t_vals_diode, pdf_vals_diode, "k-", linewidth=2, label="Weibull PDF")

    ax.set_xlabel("Lifetime [years]")
    ax.set_ylabel("Lifetime distribution f(x)  (PDF)")
    ax.set_title("Diode – Lifetime Distribution and Weibull PDF")
    ax.grid(True)
    ax.legend(loc="best")

    ax.set_xlim(t_min_diode, t_max_diode)

    plt.tight_layout()
    plt.savefig(Figures_dir / "20_weibull_pdf_hist_diode.png")
    plt.close(fig20)

    # -------------------------------------------------
    # Figure 21: Weibull PDF for Switch Lifetime
    # -------------------------------------------------

    # Element-wise minimum: switch fails when either IGBT or Diode fails
    lifetimes_igbt_MC = df_lifetime_igbt_MC["Lifetime_igbt_MC"].values
    lifetimes_diode_MC = df_lifetime_diode_MC["Lifetime_diode_MC"].values

    lifetimes_switch = np.minimum(lifetimes_igbt_MC, lifetimes_diode_MC)

    # If all values are identical → add tiny variation (0.01%)
    if np.std(lifetimes_switch) < 1e-12:
        lifetimes_switch = lifetimes_switch + np.random.normal(loc=0.0, scale=0.0001 * lifetimes_switch[0], size=len(lifetimes_switch))

    # --- Fit Weibull distribution (Switch) ---
    beta_switch, _, eta_switch = weibull_min.fit(lifetimes_switch, floc=0.0)

    # --- x-range (use full lifetime range for Switch) ---
    t_min_switch, t_max_switch = np.quantile(lifetimes_switch, [0.0, 1.0])
    t_vals_switch = np.linspace(t_min_switch, t_max_switch, 500)

    # --- Weibull PDF for Switch ---
    pdf_vals_switch = ((beta_switch / eta_switch) * (t_vals_switch / eta_switch) ** (beta_switch - 1) * np.exp(-(t_vals_switch / eta_switch) ** beta_switch))

    # --- Build the plot (Switch) ---
    fig21, ax21 = plt.subplots(figsize=(6.4, 4.8))

    # Histogram (PDF-normalized)
    ax21.hist(lifetimes_switch, bins=40, range=(t_min_switch, t_max_switch), density=True, alpha=0.75, color="salmon", edgecolor="black")

    # Overlay Weibull PDF
    ax21.plot(t_vals_switch, pdf_vals_switch, 'k-', linewidth=2, label="Weibull PDF")

    ax21.set_xlabel("Lifetime of Switch [years]")
    ax21.set_ylabel("Lifetime distribution f(x)  (PDF)")
    ax21.set_title("Switch – Lifetime Distribution and Weibull PDF")
    ax21.grid(True)
    ax21.legend(loc="best")

    ax21.set_xlim(t_min_switch, t_max_switch)

    plt.tight_layout()
    plt.savefig(Figures_dir / "21_weibull_pdf_hist_switch.png")
    plt.close(fig21)
