arXiv is now an independent nonprofit! Learn more (https://info.arxiv.org/about)  ×
Why HTML?
(https://info.arx
iv.org/about/ac
|              | RReeppoorrtt | BBaacckk  ttoo   | DDoowwnnllooaadd |
| ------------ | ------------ | ---------------- | ---------------- |
| cessible_HTM | IIssssuuee   | AAbbssttrraacctt | PPDDFF           |
L.html)
License: CC BY 4.0 (https://info.arxiv.org/help/license/index.html#licenses-available)
arXiv:2512.08076v1 [eess.SY] 08 Dec 2025

Mitigation of Datacenter Demand
Ramping and Fluctuation using
Hybrid ESS and Supercapacitor
Min-Seung Ko and Hao Zhu
Jae Woong Shim
Chandra Family Department of Electrical
Department of Electrical Engineering
& Computer Engineering
Sangmyung University
The University of Texas at Austin
Seoul, South Korea
Austin, TX, USA
jaewshim@smu.ac.kr
{kms4634500, haozhu}@utexas.edu
Abstract
This paper proposes a hybrid energy storage system (HESS)-based control
framework that enables comprehensive power smoothing for hyperscale AI data-
centers with large load variations. Datacenters impose severe ramping and fluctu-
ation-induced stresses on the grid frequency and voltage stability. To mitigate
such disturbances, the proposed HESS integrates a battery energy storage sys-
tem (BESS) and a supercapacitor (SC) through coordinated multi-timescale con-
trol. A high-pass filter (HPF) separates the datacenter demand into slow and fast
components, allocating them respectively to the ESS via a leaky-integral con-
troller and to the SC via a phase-lead proportional-derivative controller enhanced
with feedforward and ramp-tracking compensation. Adaptive weighting and repeti-
tive control mechanisms further improve transient and periodic responses. Case
studies verify that the proposed method effectively suppresses both ramping and
fluctuations, stabilizes the system frequency, and maintains sustainable state-of-
charge (SoC) trajectories for both ESS and SC under prolonged, stochastic train-
ing cycles.
Index Terms: : Battery energy storage system, co-located load, datacenter,
power smoothing, supercapacitor.
I Introduction
Hyperscale AI datacenters have emerged as a critical load demand, driven by
the rapid proliferation of large language models (LLMs) and other computation-
ally intensive AI workloads [1]. Although securing sufficient energization capac-

ity remains an immediate concern, these power-hungry computing facilities
have already led to significant challenges in grid reliability and stability. In par-
ticular, training LLM-typed large-scale AI models can require several hundred
MW per site, and thus these workloads dominate the overall load patterns of
hyperscale datacenters [2]. They are known to produce large and irregular
power fluctuations, quickly becoming a major new threat to both local and grid-
wide stability. Consequently, datacenter demand patterns are predominately
characterized by abrupt ramping events and periodic fluctuations. Ramping be-
havior can cause severe local voltage stress, especially under weak-grid condi-
tions. Meanwhile, periodic and sustained power fluctuations, with the character-
istic frequency tied to the underlying large AI model training, can excite reso-
nant oscillatory modes throughout the grid interconnection, as shown by our re-
cent work[3].
To enhance grid stability under increasing variability of datacenter loads, sev-
eral mitigation strategies for power smoothing have been investigated. The rack
 
level has mainly considered capacitive frequency-locking mechanisms, while
energy storage systems (ESSs) are identified for the datacenter-wide mitiga-
tion. However, as demonstrated in [4], these ESS-based solutions alone are in-
sufficient to tackle the sharp transients induced by the start/end of AI workloads
due to their inherent slower response timescales. Meanwhile, strengthening the
grid infrastructure is also a viable approach, such as using grid-forming control
of co-located storage to suppress sustained oscillations caused by fluctuating
loads [5]. Nevertheless, prior research has not fully addressed the physical lim-
itations of standalone ESSs, and it remains a challenge to develop effective
mitigation strategies that can simultaneously suppress the ramping and fluctu-
ating demands of AI datacenters.

 
To address this research gap, we propose a hybrid energy storage system
(HESS) by co-locating a supercapacitor (SC) with an ESS to attain power
smoothing across multiple timescales. Similar HESS solutions have been used
to smooth intermittent renewable power generation, with applications in wind
farms [6] and solar plants [7]. Although these approaches are effective for slow
or quasi-periodic variations, they largely rely on instantaneous power-error
feedback and thus provide limited and insufficient treatment for large fast ramp
events, typical of AI datacenter loads.

 

Hence, this paper develops an adaptive HESS control framework that com-
bines frequency-based power decomposition and a look-ahead compensation
approach to systematically mitigate load ramps in addition to fluctuations. We
use the SC to tackle high-frequency and sharp transients and the ESS to regu-
late slower variations and maintain the long-term energy balance. In parallel, a
Kalman-filter (KF) observer is introduced to estimate the instantaneous slope
and jerk in the demand profile, enabling a predictive feedforward that prepares
the SC ahead of steep ramps and improves transient tracking beyond pure
feedback control. The SC control loop employs a phase-lead proportional-deriv-
ative (PD) controller, while the ESS loop employs a leaky integral controller for
sustained correction and suppression of low-frequency changes. A unified SoC-
reference manager is further used to ensure energy sustainability with minimal
deviation from the desired grid power reference. Collectively, these elements
can effectively suppress both ramping and oscillatory transients for enhancing
the stability of grid operations.

 
II System Modeling of AI Datacenters
We first present the modeling of power fluctuations induced by AI training work-
loads in hyperscale AI datacenters. Fig. 1(a) illustrates the example measure-
ments of the GPU-level power trace, which exhibit both quasi-periodic fluctua-
tions and abrupt ramping patterns. The fluctuation component is primarily
driven by cyclic variations with approximately 0.05 Hz, arising from the iterative
gradient computation inherent to the training process. Within these dominant
cycles, higher-frequency sub-fluctuations and stochastic variations also exist,
reflecting the fine-grained computational dynamics of GPUs. In terms of ramp
behavior, the measured trace clearly demonstrates full-range transitions be-
tween idle and peak operating conditions due to the high GPU utilization.

 

(a)
(b)
Figure 1:Schematic diagrams of (a) realistic GPU power consumption from [4]
and (b) synthetic datacenter demand.
Based on these measurement characteristics, we have synthetically generated
the aggregate power demand of an AI datacenter. An example of the generated
profile is illustrated in Fig. 1(b). Unlike the GPU-level trace, the datacenter-level
load has additional components beyond the server-computing loads. Moreover,
in large-scale LLM training, multiple GPUs are synchronized by the training cy-
cle to produce coherent load variations. Accordingly, the synthetic datacenter
load demand retains the dominant fluctuation with some modifications to reflect
the aggregated behavior. The sub-fluctuation component becomes more regu-
lar, resulting in smoother high-frequency oscillations. In addition, even after the
training terminates, a non-zero baseline power is preserved to account for per-
sistent non-computational loads. After aggregation, the two dynamic variations,
namely periodic fluctuations and ramping patterns, are the most dominant in
the total datacenter power profile.

 

To address both dynamic variations simultaneously, we propose co-located hy-
brid resources composed of a battery ESS (BESS) and a supercapacitor (SC)
in the AI datacenter. The proposed hybrid energy storage system (HESS) is
connected to the same point of interconnection (POI) in parallel with the data-
center, as illustrated in Fig. 2. The total power supply by the grid at time 𝑡,
𝑃 (𝑡), can be represented as
grid
|     |     | 𝑃  (𝑡) | = 𝑃 |  (𝑡)+𝑃  (𝑡)+𝑃 |     |  (𝑡) |     |     |
| --- | --- | ------ | --- | ------------- | --- | ---- | --- | --- |
|     |     | grid   | DC  | ESS           | SC  |      |     | (1) |
where 𝑃  stands for the datacenter load. The outputs of BESS and SC, 𝑃
DC ESS
and 𝑃 , indicate the discharged power when they have positive values. The
SC
HESS is operated under the constraints on power, ramp, and state of charge
|                       |     |          |      | , and SoCmin |     |       | SoCmax |       |
| --------------------- | --- | -------- | ---- | ------------ | --- | ----- | ------ | ----- |
| (SoC), as given by |𝑃 |     | | ≤ 𝑃max | , |𝑅 | | ≤ 𝑅max     |     | ≤ SoC | ≤      | , re- |
|                       |     | (⋅)      | (⋅)  | (⋅) (⋅)      |     | (⋅)   | (⋅)    | (⋅)   |
spectively. Here, the subscript symbol (⋅) can represent either BESS or SC and
𝑅 stands for ramp rate. Based on the standard modeling approaches in [6],
each device is represented by a first-order dynamic system in the following
Laplace form in the 𝑠-domain:
1
|     |     | 𝑃  (𝑠) = | 𝐺  (𝑠) 𝑈 |  (𝑠) = |  𝑈  |  (𝑠) |     |     |
| --- | --- | -------- | -------- | ------ | --- | ---- | --- | --- |
|     |     | (⋅)      | (⋅)      | (⋅)    |     | (⋅)  |     | (2) |
|     |     |          |          | 𝜏      | 𝑠+1 |      |     |     |
(⋅)
𝑈  (𝑠)
with  denoting  the  controller  output  for  managing  the  corresponding
(⋅)
| power output 𝑃 |  (𝑠). Here, the parameter 𝜏 |     |     |                                         |     |     |     |     |
| -------------- | --------------------------- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
|                | (⋅)                         |     |     | (⋅)  stands for the given time constant |     |     |     |     |
related to the dynamic speed of each device. In particular, BESS tends to have
a much larger capacity than SC, while the SC can provide a faster response to
load deviation than BESS. Hence, the parameter settings should follow the be-
low orderings:
𝑃˙max 𝑃˙max
|     | 𝑃max | ≫ 𝑃max, |     | ≪ , and |  𝜏  | ≫ 𝜏 . |     |     |
| --- | ---- | ------- | --- | ------- | --- | ----- | --- | --- |
|     |      | ESS SC  | ESS | SC      | ESS | SC    |     | (3) |

|    |     |     |     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Figure 2:Configuration of the co-located datacenter with HESS.
III Power Smoothing via HESS Control Designs
The goal of proposing to co-locate HESS in datacenters is to attain power
smoothing of 𝑃 (𝑡) by utilizing the two heterogeneous and complementary re-
DC
sources. As discussed in Section II, SC has a much faster response than
BESS, motivating us to design power command signals of different frequency
ranges that can match the two resources. We first define Δ (𝑡) = 𝑃 (𝑡)−𝑃0 as
DC DC
the deviation from its DC frequency component
𝑃0
. Thus, the SC power com-
DC
mand uses the higher-frequency component of Δ (𝑡), while the remaining is as-
signed to the BESS, as given by
𝑠
𝑃ref0
= 𝐺 (𝑠) Δ (𝑠) = Δ (𝑠)
SC HPF (4)
𝑠+2 𝜋 𝑓
𝑐
𝑃ref0 = (1−𝐺 (𝑠)) Δ (𝑠),
(5)
ESS HPF
where 𝑓 denotes the cutoff frequency for the high-pass filtering (HPF). This
𝑐
way, the SC responds to the rapid variations and transient spikes, while the
BESS compensates for slower deviations by using a larger energy capacity
than SC. Examples of the filtered signals are illustrated in Fig. 3.

 
In the event of severe ramping or sharp fluctuations, the SC with the HPF sig-
nal would still exhibit some relative response delay that hinders a timely re-

sponse. To address this issue, we incorporate an additional ramp-related term
into the SC control loop, as
^
|     |     | 𝑃ref1 | = 𝐺 |  (𝑠) Δ (𝑠)+𝜔 |     |  𝑇  𝑅    |  (𝑠), |     |
| --- | --- | ----- | --- | ------------ | --- | -------- | ----- | --- |
|     |     | SC    |     | HPF          |     | ramp eff | DC    | (6) |
^
where 𝑅  (𝑠) is the estimated ramp rate with an adaptive scaling factor 𝜔
| DC  |     |     |     |     |     |     |     | ramp , |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
which will be discussed soon. In addition, the look-ahead horizon, 𝑇  is se-
eff
lected to be close to 𝜏
, the SC’s time constant, for this command signal to
SC
lead a single time step. As illustrated in Fig. 3(b), this enhanced SC command
design can provide more adequate reference values for ramp conditions.
| To estimate the ramp rate 𝑅 |     |     | ^   |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
 in (6), we employ a discrete-time Kalman filter
|     |     |     |     | DC  |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
(KF). For a discrete timestep 𝑘 with a sampling interval 𝑇
𝑠 , the KF state vector
⊤
| is defined as 𝐳KF |     | = [Δ¯, | 𝑅   | ] . Here, Δ¯ |     |                                        |     |     |
| ----------------- | --- | ------ | --- | ------------ | --- | -------------------------------------- | --- | --- |
|                   | 𝑘   |        | DC  |              |     |  represents a slow-varying baseline of |     |     |
the deviation signal Δ (𝑡) and its rate of change defines the ramp rate 𝑅 . Using
DC
a time-varying baseline allows the KF to capture the slow drift handled by the
^
ESS, so that 𝑅
DC  reflects the actual fast component that the SC must compen-
sate for. Then, the KF relies on a second-order stochastic model expressed as
1𝑇
|     | 𝐳KF | =   | 𝑠] 𝐳KF | +𝐰  | ,   | Δ = [10] 𝐳KF | +𝑣 . |     |
| --- | --- | --- | ------ | --- | --- | ------------ | ---- | --- |
|     |     |     | [      |     |     |              |      | (7) |
|     | 𝑘+1 |     | 0 𝜙    | 𝑘   | 𝑘   | 𝑘            | 𝑘 𝑘  |     |
Here, the parameter 𝜙 is chosen to have a very slow ramp dynamics, while 𝐰
𝑘
and 𝑣
𝑘  denote the process and measurement noises, respectively. By using the
nonlinear KF estimation approach in [8], one can update both states recursively
^ ^
to obtain Δ ¯  and 𝑅 . In addition, we design an adaptive update for the parame-
DC
| ter 𝜔 = | 𝛾   | ⋅𝛾  |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
 by forming two scalar variables related to ramp and jerk,
| ramp | ramp | jerk |     |     |     |     |     |     |
| ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
respectively, as given by
−1
|     |      |            |     | ^    |     |         | ^    |     |
| --- | ---- | ---------- | --- | ---- | --- | ------- | ---- | --- |
|     |      |            |     | |𝑅   | |   |         | |𝑅 | |     |
|     |      |            |     |      | DC  |         | DC   |     |
|     | 𝛾    | = Sigmoid( |     |      | ),  | 𝛾 = (1+ | ) .  | (8) |
|     | ramp |            |     |      |     | jerk    |      |     |
|     |      |            |     | 𝑠ref |     |         | 𝐴ref |     |
In (8), the Sigmoid function uses the logistic function, while the two parameters
𝑠ref  and 𝐴ref
 are predefined by the reference slope and jerk, respectively. This
way, the ramp term 𝛾  is activated only when the estimated ramp exceeds
ramp
𝑠ref . In addition, the value of 𝛾
 is reduced during rapidly changing ramps,
jerk
thereby mitigating the potential overshoot in the control response.

|    |     |     |     |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

(a)
(b)
Figure 3:Command signals (a) in overall timeframe and (b) during ramp.
Lastly, a dynamic SoC command manager is introduced to ensure the long-
term SoC balance of both BESS and SC. A slowly varying offset 𝑞ref
 biases the
(⋅)
BESS  and  SC  commands  according  to  their  SoC  deviation
| 𝐸SoC (𝑠) = SoC | ∗ −SoC |                             |     |     |
| -------------- | ------ | --------------------------- | --- | --- |
| (⋅)            | (⋅)    | (⋅) . The offset evolves as |     |     |
𝑘
𝑞,(⋅)
|     |     | 𝑞ref (𝑠) = − |  𝐸SoC (𝑠), |     |
| --- | --- | ------------ | ---------- | --- |
(9)
|     |     | (⋅) 𝑠+1/𝑇 | (⋅) |     |
| --- | --- | --------- | --- | --- |
𝑞
and decays exponentially within a small deadband. Here, 𝑘  and 𝑇
𝑞 𝑞  are the
gain and time constant of the bias filter, respectively. The final power com-
mands are adjusted as
|     | 𝑃ref | = 𝑃ref0 +𝑞ref , | 𝑃ref = 𝑃ref1 +𝑞ref. |      |
| --- | ---- | --------------- | ------------------- | ---- |
|     |      | ESS ESS         | SC SC               | (10) |
ESS SC
This slow biasing loop maintains sustainable SoC trajectories and prevents
long-term drift without disturbing the fast HPF-based power control.

|    |     |     |     |    |
| --- | --- | --- | --- | --- |

III-A Design of BESS and SC Controllers
To accurately track the command signals given in (10), we will design the con-
troller outputs for BESS and SC, namely 𝑈  and 𝑈  [cf. (2)]. Due to SC’s fast
|     |     |     |     | ESS | SC  |     |
| --- | --- | --- | --- | --- | --- | --- |
timescales, it adopts a proportional–derivative (PD) controller to provide phase
lead compensation, while BESS employs an integral controller to address slow
variations and maintain the long-term energy balance. This complementary de-
sign allows the HESS to achieve coordinated control across multiple frequency
bands.

 
To improve tracking ability during the ramp, the enhanced SC control structure
consists of three components: PD controller, feedforward (FF), and ramp track-
ing (RK). Using the SC power tracking error 𝜖 = 𝑃ref −𝑃 , one sets the SC
|     |     |     |     |     | SC SC SC |     |
| --- | --- | --- | --- | --- | -------- | --- |
controller to be
| 𝑈   |  (𝑠) = | 𝐶  (𝑠) 𝜖 |  (𝑠)+𝑈 |  (𝑠)+𝑈 |  (𝑠). |      |
| --- | ------ | -------- | ------ | ------ | ----- | ---- |
| SC  |        | PD       | SC     | FF,SC  | RK    | (11) |
We discuss each of the three terms here. First, the derivative action within the
PD control can amplify high-frequency noise if left unregulated. To mitigate this
effect, a first-order derivative filter is used to find
2𝜋 𝑓  𝑠
𝑑
|     | 𝐶  (𝑠) | = 𝐺 |  (𝑠) (𝑘 +𝑘 |           | )   | (12) |
| --- | ------ | --- | ---------- | --------- | --- | ---- |
|     | PD     |     | HPF 𝑝      | 𝑑 𝑠+2 𝜋 𝑓 |     |      |
𝑑
with the derivative cutoff frequency 𝑓
𝑑 . Note that the PD controller has incorpo-
rated 𝐺  (𝑠) in (4) to focus on the high-frequency range. Second, although the
HPF
ramp component is implicitly included by the PD structure, a pure feedback
control may still lag during abrupt, sharp transients. Therefore, we incorporate
𝑈  (𝑠) to provide partial delay compensation and improve the match with the
FF,SC
SC reference at the beginning phase, given by
|     |      |       | 1            |     | 𝑃  (𝑠) |     |
| --- | ---- | ----- | ------------ | --- | ------ | --- |
| 𝑈   |  (𝑠) | = (𝑠+ | ) (𝑃ref (𝑠)− |     | SC ).  |     |
(13)
|     | FF,SC |     | 𝜏   | SC  | 𝑒𝑠 𝑇 |     |
| --- | ----- | --- | --- | --- | ---- | --- |
|     |       |     | SC  |     | 𝑠    |     |
By reducing the burden on the feedback loop and mitigating phase lags inher-
ent in the converter dynamics, this FF term helps to suppress overshoot while
preserving adequate phase margin. Last, the RK term is used to address any
remaining mismatch between the desired and actual ramp profiles, as
|     |     |        | ^            | ^   |       |      |
| --- | --- | ------ | ------------ | --- | ----- | ---- |
|     | 𝑈   |  (𝑠) = | 𝑘  (𝑅  (𝑠)−𝑅 |     |  (𝑠)) |      |
|     | RK  |        | RK DC        |     | SC    | (14) |

with the coefficient 𝑘 determining the correction gain. This compensator in-
RK
jects a corrective action based on the slope error between the commanded and
measured power trajectories. To recap, the PD term responds to instantaneous
errors and the FF term mitigates delay-induced mismatch, while the RK term
ensures accurate tracking of sharp ramp segments, especially when the SC
output lags behind the desired trajectory.
Similarly to SC, the BESS controller also consists of three components, the in-
tegral (I) controller, the FF loop, and the repetitive controller (RC), as expressed
by
𝑈 (𝑠) = (𝐶 (𝑠)+𝐶 (𝑠)) 𝜖 (𝑠)+𝑈 (𝑠).
ESS 𝐼 RC ESS FF,ESS (15)
First, the main feedback controller is implemented as a leaky I controller to pre-
vent the windup issue:
1
𝐶 (𝑠) = 𝑘
𝐼 𝐼 (16)
𝑠+1/𝑇
leak
where 𝑇 sets the leakage time constant and 𝑘 is the integral gain. This for-
leak 𝐼
mulation ensures good steady-state accuracy while maintaining a bounded
control effort even under long-term energy imbalance conditions. In practice,
this leaky I control also contributes to the energy-neutral operation of BESS by
gradually restoring its SoC to the mid-level target. Second, the RC filter is intro-
duced to suppress quasi-periodic deviations in the BESS tracking error that
may persist due to the coupling with SC. The discrete comb filter [9] is selected,
which is approximated in the s-domain by
𝜔
RC
𝐶 (𝑠) = 𝑘
RC RC𝑠+𝜔 (17)
RC
where 𝑘 is the compensation gain and 𝜔 corresponds to the dominant peri-
RC RC
odic frequency. This RC filter actively rejects repeating frequency components,
thereby mitigating interaction-induced oscillations between the SC and BESS.
Finally, the FF term for BESS is formulated with the same structure as in (13)
with different parameters, in order to reduce any delay-induced mismatch.

  
 

IV Experimental Settings and Results
To investigate the impact of power smoothing through the HESS, we conduct
case studies on the synthetic simplified 1 GW system. For simplicity, we as-
sume a single-machine grid based on the swing equation and first-order gover-
nor dynamics. The deviation of datacenter demand is assumed to be 50 MW.
Detailed parameter values of the grid and HESS adopted for the experiment
are shown in Table I. Specifically, we set the charge/discharge efficiency 𝜂 iden-
tical for both processes, as well as for BESS and SC. To ensure realistic behav-
ior, HESS controllers are implemented using the discrete-time formulation with
𝑇 = 10 ms. Furthermore, Δ(𝑡) shows large energy near 0.05 Hz and 0.15 Hz,
𝑠
as shown in Fig. 4(a). Notice that these frequencies correspond to the domi-
nant and sub-periodic variations in Fig. 3(a), respectively. To ensure that BESS
can handle these large oscillatory components, we set the cutoff frequency at
𝑓 = 0.2 Hz.
𝑐

 
Table I:Example of the Grid and HESS parameters
| Grid Parameters | HESS Parameters |       | BESS SC |
| --------------- | --------------- | ----- | ------- |
| 𝐻               |                 | 𝑃     |         |
|                 | 6               |  (MW) | 30 10   |
max
𝑃˙
| 𝐷   | 3   |  (MW/s) | 15 100 |
| --- | --- | ------- | ------ |
max
| 𝑅     |      | 𝜏   |           |
| ----- | ---- | --- | --------- |
| droop | 0.05 |     | 0.25 0.02 |
| 𝑇     | 0.3  | 𝜂   | 0.97      |
𝑔
𝐻: Inertia constant, 𝐷: Frequency-dependent damping, 𝑅 droop: Governor droop rate, 𝑇
𝑔: Governor time
constant, 𝜂: Charge/discharge efficiency

(a)
(b)
Figure 4:Schematic diagrams of (a) wavelet analysis results of Δ (𝑡) and (b) power
spectral density analysis results of command signals
Figure 5:Open-loop bode plots of BESS and SC controllers.

To examine the frequency-domain characteristics of the designed command
signals, a power spectral density (PSD) analysis is conducted, as shown in Fig.
4(b). The PSD of Δ(𝑡) exhibits a dominant concentration of energy at very low
frequencies. However, a non-negligible portion remains at higher frequencies,
confirming the need for multi-band control. With the chosen 𝑓 , the BESS pri-
𝑐
marily covers frequencies below approximately 0.2 Hz, while SC responds
dominantly to components above 0.4 Hz. This frequency separation enables
the HESS to handle distinct dynamic regimes of the datacenter load. The open-
loop Bode plots in Fig. 5 further illustrate these complementary roles. For the
SC loop, the transition from the basic PD to the proposed configuration pro-
gressively suppresses the low-frequency gain while maintaining an adequate
mid-high frequency response; HPF and derivative filters also improve phase
behavior and enhance robustness. In contrast, the BESS loop maintains a
dominant low-frequency response, where the leaky I control prevents the drift,
and the RC selectively boosts the gain near 0.05 Hz for improved rejection on
periodic disturbance.

 

(a)
(b)
Figure 6:Schematic diagrams of (a) power output and SoC level, and (b) total
supplied power and frequency.

Figure 7:Long-term simulation results with dynamic SoC command manager.
The resulting responses of the BESS and SC outputs to their respective com-
mand signals are depicted in Fig. 6(a), while Fig. 6(b) presents the total power
supply and grid frequency with and without the HESS. Both BESS and SC
closely follow their command trajectories, maintaining the grid-supplied power
nearly constant and minimizing frequency deviations. During ramp-up events, a
slight mismatch between the SC command and its actual output can be ob-
served due to its physical power limit. This constraint leads to a transient in-
crease in grid-supplied power, causing a momentary frequency dip.
Nonetheless, these transient deviations are brief and remain within acceptable
operating limits. In addition, although we do not implement the SoC manager in
this experiment, SoCs of both components remain highly stable throughout the
10 min simulation, exhibiting less than 0.03% variation. The BESS effectively
recharges during idle periods, restoring its SoC toward the nominal operating
level. However, both devices exhibit a gradual downward trend over longer
horizons, suggesting potential energy imbalance during extended operation or
prolonged training cycles.

 
To further evaluate this long-term performance, we conduct an additional simu-
lation using a more realistic datacenter training profile characterized by longer
active and idle periods. The corresponding results are shown in Fig. 7. As ob-
served, the SoC trajectories exhibit a gradual drift toward the upper limit, as a

result of the sustained positive net energy injection during extended training
phases. To mitigate this imbalance, we incorporate baseline correction of the
desired demand and apply a dynamic SoC command manager during idle inter-
vals. Notice that the frequency during the idle period experiences small devia-
tions because of the change in reference from the SoC manager. With these
enhancements, both components maintain their SoC within a narrow range of
approximately 0.05%, while the system frequency remains tightly regulated
around the nominal 60 Hz. These results confirm that the proposed scheme en-
sures sustainable operation and long-term stability even under prolonged and
stochastic load variations.
V Conclusion

This work presents a coordinated hybrid control framework for power smooth-
ing of AI datacenter loads using co-located BESS and SC units. By decompos-
ing the demand signal through HPF, the controller effectively distributes control
actions across complementary timescales: the BESS manages slow fluctua-
tions and energy balancing, while the SC rapidly compensates for transient
ramps. The inclusion of feedforward delay compensation, ramp-tracking, and
repetitive control terms further enhances dynamic performance without violating
power or SoC constraints. Simulation results confirm that the proposed HESS
substantially reduces power and frequency deviations compared with stand-
alone operation, while maintaining device sustainability during long-duration
training.

 
References
[1] NERC Large Load Task Force, “Characteristics and risks of emerging
large loads,” North American Electric Reliability Corporation (NERC),
Tech. Rep., 2025.
[2] J. Aljbour, T. Wilson, and P. Patel, “Powering intelligence: Analyzing
artificial intelligence and data center energy consumption,” EPRI White
Paper no. 3002028905, Tech. Rep., 2024.

[3] M.-S. Ko and H. Zhu, “Wide-area power system oscillations from large-
scale AI workloads,” arXiv preprint arXiv:2508.16457, 2025.
[4] E. Choukse et al., “Power stabilization for AI training datacenters,”
arXiv preprint arXiv:2508.14318, 2025.
[5] S. Kundu, K. Chatterjee, R. R. Hossain, S. P. Nandanoori, and V.
Adetola, “Managing risks from large digital loads using coordinated
grid-forming storage network,” arXiv preprint arXiv:2508.11080, 2025.
[6] V. T. Nguyen and J. W. Shim, “Virtual capacity of hybrid energy storage
systems using adaptive state of charge range control for smoothing
renewable intermittency,” IEEE Access, vol. 8, pp. 126 951–126 964,
2020.
[7] J. Xiao, P. Wang, and L. Setyawan, “Hierarchical control of hybrid
energy storage system in DC microgrids,” IEEE Transactions on
Industrial Electronics, vol. 62, no. 8, pp. 4915–4924, 2015.
[8] F. Orderud, “Comparison of Kalman filter estimation approaches for
state space models with nonlinear measurements,” in Proc. of
Scandinavian Conference on Simulation and Modeling, 2005, pp. 1–8.
[9] T. Chmielewski, W. Jarzyna, D. Zieliński, K. Gopakumar, and M.
Chmielewska, “Modified repetitive control based on comb filters for
harmonics control in grid-connected applications,” Electric Power
Systems Research, vol. 200, p. 107412, 2021.
Experimental support, please view the build logs for errors. Generated by L A T E xml (http
s://math.nist.gov/~BMiller/LaTeXML/).
Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance
accessibility and mobile support. To report errors in the HTML that will help us improve conversion
and rendering, choose any of the methods listed below:
Click the "Report Issue" ( ) button, located in the page header.
Tip: You can select the relevant text first, to include it in your report.
Our team has already identified the following issues (https://github.com/arXiv/html_feedback/issues). We
appreciate your time reviewing and reporting rendering errors we may not have found yet. Your
efforts will help us improve the HTML versions for all readers, because disability should not be a

barrier to accessing research. Thank you for your continued support in championing open access for
all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML
maintain a list of packages that need conversion (https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-
packages-for-LaTeXML), and welcome developer contributions (https://github.com/brucemiller/LaTeXML/issue
s).