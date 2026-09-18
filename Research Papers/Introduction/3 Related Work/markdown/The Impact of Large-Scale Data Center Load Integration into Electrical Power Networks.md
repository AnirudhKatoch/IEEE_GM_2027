2025 IEEE International Conference on Energy Technologies for Future Grids
Wollongong, Australia, December 7-11, 2025
The Impact of Large-Scale Data Center Load
Integration into Electrical Power Networks
1Md Sanwar Hossain, 2Md Moktadir Rahman, 1Md. Rabiul Islam, 1Danny Sutanto, and 1Kashem M. Muttaqi
1School of Electrical, Computer and Telecommunications Engineering, University of Wollongong, NSW, 2522, Australia
2Principal Engineer at Australian Energy Market Operator, NSW, 2000, Australia
msh085@uowmail.edu.au, mdmoktadir.rahman@aemo.com.au, mrislam@uow.edu.au, soetanto@uow.edu.au, kashem@uow.edu.au
Abstract—With the rapid advancement of information and times and 1284 times, respectively [1], [2]. The data center and
communication technology, data centers have experienced renewable energy sources are commonly identified as inverter-
exponential growth, resulting in a substantial increase in their based resources (IBRs), which require multiple
electrical load demand. It is projected that by 2030, global data inverters/converters.
center electricity demand could reach 321 TWh, assuming current
growth trends persist. As large-scale data centers continue to 350
expand, their integration into the power grid poses significant
300
challenges to grid stability and reliability. This research
investigates the impact of large-scale data center load penetration 250
on electrical power networks, with a particular focus on frequency 200
and voltage dynamics and operational integrity. Using historical
150
data and detailed PSCAD simulations based on the IEEE 14-bus
test system, this article presents a comprehensive analysis of how 100
increasing data center loads affect grid stability. The results reveal
50
that sudden high-capacity load fluctuations and disturbances can
lead to frequency deviations, voltage instability, and increased 0
2015 2000 2025 2030
stress on the electrical power network. Various operational
Fig. 1. Data center energy demand.
scenarios are examined, and strategic recommendations are
proposed to mitigate adverse effects and enhance the resilience of As IBRs become increasingly integrated into modern
future power grids facing high data center penetration. electrical networks, their large and often variable profiles pose
critical challenges to power system stability and reliability. The
Keywords—Data center load, frequency stability, inverter-based integration of large-scale data center loads can influence key
resources (IBRs), load regulation, power grid stability, voltage
grid parameters such as bus voltages, branch power flows, and
stability.
system frequency, thereby impacting overall grid performance
[3]. In extreme cases, power flow through grid branches may
I. INTRODUCTION
exceed design limitations, potentially resulting in overheating or
Over the past few decades, advancements in information and fire hazards, which pose serious risks to safe grid operation [4].
communication technology (ICT) have driven a rapid increase Additionally, unregulated frequency deviations due to abrupt
in computational tasks, including cloud computing, data load changes can lead to system instability, frequency collapse,
processing, and storage. Consequently, the demand for large- and even large-scale blackouts if not managed promptly [5].
scale data center infrastructure, encompassing cooling systems,
These emerging challenges highlight the pressing need for
data storage units, and uninterrupted power supplies (UPS), has
intelligent load regulation strategies to ensure the secure and
risen substantially. As reported in [1], the total energy
reliable integration of data centers into the power grid. A core consumption of data centers increased modestly by 6% between
issue lies in maintaining critical grid parameters, voltage,
2010 and 2018, from 194 TWh to 205 TWh. However,
frequency, and power factor within acceptable thresholds,
projections indicate a significant increase in future energy
collectively referred to as the power grid parameters.
demands, with estimates suggesting that global data center
electricity consumption could reach 321 TWh by 2030 if current Motivated by these concerns, this article investigates the
growth trends continue [1], [2]. The global electricity demand operational impact of large-scale data center loads on electrical
for data center load can be illustrated in Fig. 1. power networks and proposes a dynamic regulation strategy
tailored to mitigate their adverse effects. The key contributions
At the same time, due to the decrease of fossil fuel-based
of this work are summarized as follows:
energy sources, the influence of renewable energy sources such
as solar and wind energy is becoming more popular day by day. • Modeling of large-scale data center loads, with analysis
Therefore, the number of wind and photovoltaic installations has of their sudden load demand change on the normal
been rising constantly. In the past 20 years, from 1997 to 2016, operation and overall stability of the grid;
the global installed capacity of wind power increased from 7.64
GW to 468.99 GW, and the installed capacity of photovoltaic • Evaluation of the impact of large-scale data center loads
power increased from 0.23 GW to 301.47 GW, increasing by 60 on grid stability during network faults; and
979-8-3315-7640-0/25/$31.00 ©2025 IEEE
66110411.5202.99916GFTE/9011.01
:IOD
|
EEEI
5202©
00.13$/52/0-0467-5133-8-979
|
)GFTE(
sdirG
erutuF
rof
seigolonhceT
ygrenE
no
ecnerefnoC
lanoitanretnI
EEEI
5202
)hWT(
egasu
ygrenE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:19 UTC from IEEE Xplore. Restrictions apply.

• Formulation of practical recommendations for Power quality issues: The widespread use of power inverter-
characterizing and managing data center operations to based resources (non-linear characteristics due to the highly
enhance grid stability under realistic operating inductive load) in data centers leads to the generation of
conditions. harmonics, voltage flicker, and imbalanced loads, which
degrade power quality both within the facility and in the
The remainder of this article is structured as follows: Section
surrounding grid [10]. Harmonics, in particular, can lead to
II reviews the relevant literature, and Section III presents the
increased losses in transformers and conductors, overheating of
simulation setup in the PSCAD environment and highlights the
equipment, and malfunction of sensitive devices.
key factors. Section IV represents the regulation strategies for
data center load connection. Finally, Section V summarizes the Reactive power and grid congestion: Data centers often
main findings and outlines potential directions for future exhibit a low net power factor due to the inductive and
research. capacitive nature of internal equipment, increasing reactive
power demand from the grid. Furthermore, clustering of large
II. LITERATURE REVIEW data centers in specific geographic regions has led to localized
This section presents the literature review and background grid congestion, necessitating major infrastructure upgrades and
on data center load, focusing on its key characteristics, the new substation installations [10], [11].
challenges and impacts of integrating such loads (under sudden
In response, researchers have proposed a range of solutions,
load changes and fault conditions) into power grids, and the
including the deployment of on-site energy storage, grid-
existing policies governing their grid connection.
supportive inverter controls, and demand-side management
A. Characteristics of data center load. strategies to mitigate these impacts [11].
Data centers are specialized facilities designed to house C. Existing policies related to the data center load connection
computing infrastructure for digital services such as cloud to the grid
computing, storage, artificial intelligence (AI), and real-time
Given the critical importance of maintaining grid reliability,
data processing. One of the defining characteristics of data
several standards and policies have been established to regulate
center loads is their high-power density, with power demands
how data centers are connected to the grid and how they manage
ranging from a few megawatts in small-scale centers to over 100
their power consumption.
MW in hyperscale facilities [6], [7]. Unlike conventional loads,
data centers exhibit continuous, mission-critical, and non- Voltage, frequency, and power quality compliance:
interruptible demand profiles, with operations often maintained Regulatory authorities such as the Institute of Electrical and
24/7 to ensure service reliability. Electronics Engineers (IEEE) and International Electrotechnical
Commission (IEC) have developed technical standards like
Another notable feature is the low load variability at short
IEEE 519 (harmonic limits), IEEE 1547 (interconnection
timescales, which can shift dramatically during peak processing
standards), and IEC 61000 (electromagnetic compatibility),
periods such as AI model training or cloud traffic surges. These
which are mandatory or recommended for large-scale loads like
loads are also characterized by a low power factor and a high
data centers (IEEE, 2018; IEC, 2021) [12], [13]. These standards
prevalence of non-linear power electronics, such as UPS,
enforce strict compliance to ensure that grid-connected
rectifiers, inverters and variable-speed drives in cooling
equipment does not compromise voltage and frequency stability
systems, which can introduce harmonics and other power quality
[12], [13].
disturbances into the grid [8]. Existing literature has also noted
that cooling systems alone can account for 30–40% of a data Grid code requirements: National grid operators, such as the
center’s total power consumption, further influencing load Australian Energy Market Operator (AEMO) and the North
patterns [7], [8]. American Electric Reliability Corporation (NERC), have issued
grid codes requiring large customers to support grid stability
B. Challenges and impact of data center load integration into
through voltage ride-through, frequency response, and power
power grids
factor control (AEMO, 2023; NERC, 2021) [12], [13].
The large-scale integration of data center loads into electrical
Energy efficiency and sustainability initiatives: In addition
power networks presents multiple technical challenges,
to stability-focused policies, many governments have
particularly in the domains of voltage regulation, frequency
introduced energy performance targets and sustainability
control, and power quality.
certifications for data centers. These include mandates for power
Voltage and frequency instability: Due to their large and usage effectiveness (PUE) reporting, integration of renewable
concentrated power demands, data centers can cause significant energy sources, and participation in demand response programs
voltage drops in local distribution networks, particularly in weak to reduce peak demand impacts [12], [13].
or rural grids [2]. In areas where renewable energy penetration
Despite these policies, literature highlights a gap in region-
is high, their relatively inflexible demand can exacerbate
specific planning frameworks, particularly in fast-growing data
frequency fluctuations and reduce overall grid stability [9].
center markets where grid capacity may lag behind demand
Studies suggest that the ramping behavior of data centers,
growth. This underscores the need for proactive planning and
especially during backup transitions or equipment failure, can
real-time monitoring strategies to ensure reliable integration.
cause transient disturbances affecting frequency stability [9].
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:19 UTC from IEEE Xplore. Restrictions apply.

Fig. 2. IEEE 14-bus test system with modification.

III.   SIMULATION SETUP AND RESULTS ANALYSIS  The data center load is integrated at the 11 kV Bus, which is
tied to Bus 12 (138 kV) of the IEEE 14-bus system via a step-up
In this section, the simulation setup developed in PSCAD
transformer. This configuration enables the evaluation of the
v50 with time step of 5 µs, a widely used industry-oriented
|     |     |     |     | dynamic  | impact  of  | large-scale  data  center  | loads  on  the  |
| --- | --- | --- | --- | -------- | ----------- | -------------------------- | --------------- |
software for power system analysis, is presented along with the
transmission network and generation units. The setup reflects
corresponding results. The work emphasizes the critical aspects
|     |     |     |     | the  realistic  | interconnection  | of  data  centers,  | which  are  |
| --- | --- | --- | --- | --------------- | ---------------- | ------------------- | ----------- |
of data center behavior that directly influence power system
increasingly becoming significant contributors to grid demand.
stability under different operating conditions. Key performance
indicators, including frequency variation, voltage response, and
TABLE I.
power flow characteristics, are examined to assess the system’s  TERMINAL OPERATING PARAMETERS OF THE MODIFIED SYSTEM.
dynamic performance. The obtained results provide valuable  Voltage  Phase  Active  Reactive
Buses
insights into the stability margins of the test system, thereby  magnitude  angle  power  power
validating the effectiveness of the proposed modeling approach  Bus 1  146.30 kV  00.00°  2.324 pu  -0.166 pu
and highlighting its practical relevance for real-world power  Bus 2  144.22 kV  -04.98°  0.400 pu  0.436 pu
| system applications.  |     |     |     |        |             | -12.72°  0.000 pu  | 0.251 pu  |
| --------------------- | --- | --- | --- | ------ | ----------- | ------------------ | --------- |
|                       |     |     |     | Bus 3  | 139. 40 kV  |                    |           |
|                       |     |     |     | Bus 6  | 147. 65 kV  | -14.21°  0.000 pu  | 0.128 pu  |
For the stability assessment, the IEEE 14-bus test system has
|     |     |     |     | Bus 8  | 138.00 kV  | 00.00°  0.250 pu  | 0.000 pu  |
| --- | --- | --- | --- | ------ | ---------- | ----------------- | --------- |
been employed as the benchmark network as presented in Fig.

2. The modified terminal conditions are presented in Table I, and
The data center load is categorized into three distinct groups
transmission line parameters of test bus system used in this work
|     |     |     |     | to  capture  | its  heterogeneous  | nature.  The  | critical  load  |
| --- | --- | --- | --- | ------------ | ------------------- | ------------- | --------------- |
are detailed in [14]. In this modified configuration, Bus 1 is  (processors,  primary  storage,  and  protection  systems)  is
modeled as an infinite bus, and the synchronous condenser
|     |     |     |     | modeled  | as  mostly  | inductive,  while  the  | non-critical  load  |
| --- | --- | --- | --- | -------- | ----------- | ----------------------- | ------------------- |
originally connected at Bus 8 in [14] has been replaced with a
|     |     |     |     | (secondary  | storage  and  | other  IT  equipment)  | is  primarily  |
| --- | --- | --- | --- | ----------- | ------------- | ---------------------- | -------------- |
300 MVA salient pole synchronous generator representing a
|     |     |     |     | resistive.  | In  addition,  | a  ZIP  load  representing  | constant  |
| --- | --- | --- | --- | ----------- | -------------- | --------------------------- | --------- |
hydroelectric plant. The generator model is equipped with an
impedance (Z), constant current (I), and constant power (P)
| exciter,  power  | system  stabilizer,  | multimass  system,  | hydro  |     |     |     |     |
| ---------------- | -------------------- | ------------------- | ------ | --- | --- | --- | --- |
components is considered. For the simplified load model, the
governor, and hydro turbine to capture the dynamic behavior of  critical load is set at 60 MVA, the non-critical load at 20 MVA,
hydroelectric generation. Further technical specifications of the
and the ZIP load at 20 MVA (16+j12). Furthermore, the critical
synchronous generator model are provided in [15].
and non-critical loads are modeled as dc loads interfaced with

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:19 UTC from IEEE Xplore.  Restrictions apply.

the 11 kV Bus through an ac/dc converter, whereas the ZIP load  whereas the sudden addition of load results in a corresponding
remains connected to the bus under all conditions.  decrease. These abrupt load transitions introduce steep voltage
ramps, highlighting the sensitivity of the power system to rapid
| Two  | case  studies  | have  been  | designed  | to  evaluate  | the      |           |                  |               |                |
| ---- | -------------- | ----------- | --------- | ------------- | -------- | --------- | ---------------- | ------------- | -------------- |
|      |                |             |           |               | changes  | in  data  | center  demand.  | Nonetheless,  | the  observed  |
system’s transient response under disturbances. In Case I, the
frequency oscillations are more pronounced than the voltage
critical (60 MVA) and non-critical (20 MVA) loads are suddenly
oscillations, suggesting that frequency stability is more critically
disconnected from the 11 kV Bus at 5 s and reconnected at 5.43
impacted by sudden variations in large-scale data center loads in
ms, simulating abrupt load variations. In Case II, a three-phase
the power system.
short-circuit fault is applied at the 11 kV Bus at 5 ms, coinciding

| with the disconnection of the critical and non-critical loads. It is  |     |     |     |     |     | 1.2 |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assumed that the critical (60 MVA) loads are backed up by the  Load addition
local Uninterruptible Power Supply (UPS) system. The fault is
1.1
| cleared after 430 ms, and all loads are reconnected at 5.43 ms.  |     |     |     |     |     | )up( egatloV |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- |
These scenarios provide insight into the stability performance of
1.0
| the  system  | under  | both  load-shedding  |     | and  fault-induced  |     |     |     |     |     |
| ------------ | ------ | -------------------- | --- | ------------------- | --- | --- | --- | --- | --- |
disturbances, highlighting the critical role of dynamic load
0.9 Load removal
modeling in power system studies involving large-scale data
centers.
0.8
|     |     |     |     |     |     | 4.9 5 | 5.1 5.2 | 5.3 5.4 | 5.5 5.6 |
| --- | --- | --- | --- | --- | --- | ----- | ------- | ------- | ------- |
  The frequency response of the system under both case
Time (s)
studies is illustrated in Fig. 3 and Fig. 4. As observed in Fig. 3,

sudden variations in the data center load significantly affect  Fig. 5. Bus voltage response for the sudden removal and addition of load at 11
| system frequency, leading to noticeable oscillations. Large-scale  |     |     |     |     | kV Bus.  |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- |

| data center loads, due to their abrupt and dynamic nature, impose   |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rapid changes on the system, resulting in steep rising and falling  |     |     |     |     |     | 1.2 |     |     |     |
Fault: 430 ms
| ramps in frequency. Similar behavior is evident in both cases,  |     |     |     |     |     | 1.0          |       |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | ------------ | ----- | --- | --- |
| where the high rate of frequency deviation indicates potential  |     |     |     |     |     | )up( egatloV |       |     |     |
|                                                                 |     |     |     |     |     | 0.8          | Load  |     |     |
instability in the system. These findings highlight the necessity
Load
of effective frequency regulation mechanisms to mitigate such  0.6 removal
high ramp in frequency changes and ensure stable and reliable  addition
0.4
system operation in the presence of large data center loads in the
0.2
power system.
0
| 60.6 |     |     |     |     |     | 4.9 5 | 5.1 5.2 | 5.3 5.4 | 5.5 5.6 |
| ---- | --- | --- | --- | --- | --- | ----- | ------- | ------- | ------- |
Time (s)
60.4
| )zH( ycneuqerF |     |     | Load addition |     |     |     |     |     |     |
| -------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
60.2 Fig. 6. Bus voltage response for 3-phase short-circuit faults at 11 kV Bus.

60.0
|     |     |     |     |     |     | The data center is integrated at the 11 kV Bus, which is  |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
59.8 connected to Bus 12 of the IEEE 14-bus system. Bus 12 receives
Load removal
power primarily from Bus 6 and Bus 13, with the active a power
59.6
flows from Bus 6 to Bus 12 under both case studies illustrated
59.4 in Figs. 7–10. The results indicate that sudden removal and
| 4.9 | 5   | 5.1 5.2 | 5.3 | 5.4 5.5 | 5.6 |     |     |     |     |
| --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- |
Time (s) addition of the data center load significantly affect the active and
reactive power flow in the associated transmission lines. In
Fig. 3. System frequency response for the sudden removal and addition of load
particular, the majority of the load demand is supplied through
at 11 kV Bus.
the line between Bus 6 and Bus 12, emphasizing its critical role
70
in supporting the data center connection and highlighting the
impact of abrupt load variations on transmission line loading.
| 65             |     |     | Load addition |     |     |     |     |     |     |
| -------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| )zH( ycneuqerF |     |     |               |     |     |     |     |     |     |

| 60  |     |     |     |     |     | 60  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fault: 430 ms
)WM( rewop evitcA
| 55  | Load removal |     |     |     |     | 50  |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
40
50
30 Load
45
| 4.9 | 5   | 5.1 5.2 | 5.3 | 5.4 5.5 | 5.6 |     |     |     |     |
| --- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- |
20 removal
Time (s)
Load
10
Fig. 4. System frequency response for 3-phase short-circuit faults at 11 kV Bus.  addition
0

|     |     |     |     |     |     | 4.9 5 | 5.1 5.2 | 5.3 5.4 | 5.5 5.6 |
| --- | --- | --- | --- | --- | --- | ----- | ------- | ------- | ------- |
  The voltage responses for Case I and Case II are illustrated
Time (s)
in Fig. 5 and Fig. 6, respectively. Analysis of the results in Figs.
3–6 demonstrates that the sudden removal of data center load  Fig. 7. Active power flow between Bus 12 and Bus 6 for the sudden removal and
leads to an increase in both system frequency and voltage,  addition of load at 11 kV Bus.

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:19 UTC from IEEE Xplore.  Restrictions apply.

oscillations and ensure stable generator operation under large-
60
scale data center load disturbances.
50
40
30
20
10
0
4.9 5 5.1 5.2 5.3 5.4 5.5 5.6
Time (s)
Fig. 8. Active power flow between Bus 12 and Bus 6 for 3-phase short-circuit
faults at 11 kV Bus.
Fig. 11. Synchronous generator rotor speed for the sudden removal and addition
of load at 11 kV Bus.
Fig. 9. Reactive power flow between Bus 12 and Bus 6 for the sudden removal
and addition of load at 11 kV Bus.
Fig. 12. Synchronous generator rotor speed for 3-phase short-circuit faults at 11
kV Bus.
IV. RECOMMENDATION FOR REGULATION STRATEGIES
To ensure the secure and reliable operation of electrical
power networks under the increasing penetration of large-scale
data center loads, it is essential to establish comprehensive and
forward-looking regulation strategies. These regulations should
address the unique operational characteristics of data centers
while maintaining grid stability and performance under both
normal and disturbed conditions. The following
Fig. 10. Reactive power flow between Bus 12 and Bus 6 for 3-phase short-circuit
faults at 11 kV Bus. recommendations are proposed:
In this work, the rotor angle (δ) and speed (ω) of the A. Mandate disturbance ride-through capability.
synchronous generator are examined to assess the impact of data
Data centers should be required to maintain operation during
center load on its dynamic performance. The rotor angle and
grid disturbances such as voltage sags, swells, and frequency
speed are expressed by (1) and (2), respectively.
deviations. Implementing disturbance ride-through capability
(cid:1)(cid:2)
=((cid:6)−(cid:6) ) (1) ensures that data centers remain connected during transient
(cid:8)
(cid:1)(cid:3)
events, thereby avoiding sudden large-scale load drops that
(cid:1)(cid:10) (cid:11)
= ((cid:14) −(cid:14) −(cid:17) ((cid:6)−(cid:6) )) (2)
(cid:15) (cid:16) (cid:1) (cid:8) could destabilize the network.
(cid:1)(cid:3) (cid:12)(cid:13)
Here, (cid:6)
(cid:8)
, (cid:18), (cid:14)
(cid:15)
, (cid:14)
(cid:16)
, and (cid:17)
(cid:1)
denote the synchronous speed,
B. Require active and reactive power compensation facilities.
inertia constant, mechanical power, electrical power, and
Regulation should enforce the provision of both active and
damping ratio of the synchronous generator, respectively.
reactive power compensation systems (e.g., static synchronous
The rotor speed oscillations resulting from the sudden addition compensator (STATCOMs), synchronous condensers) at data
and removal of the data center load are illustrated in Fig. 11 and center sites. These facilities will support voltage stability and
Fig. 12 for Case I and Case II, respectively. As shown in Fig. 11, power quality by controlling power flows and maintaining a
abrupt load variations significantly increase the amplitude of desired power factor.
rotor speed oscillations, indicating a direct impact on generator
C. Protection system requirements with adequate performance
dynamics. If not properly regulated, these oscillations may
adversely affect the performance and stability of the margins.
synchronous generator, potentially leading to reduced Data center protection schemes should be designed with
operational reliability. Therefore, appropriate control strategies defined performance capabilities and appropriate safety margins
are required to mitigate the ramping behavior of rotor speed to ensure coordination with the overall grid protection system.
)WM(
rewop
evitcA
Fault: 430 ms
Load
removal
Load
addition
90
80
70
60
50
40
30
4.9 5 5.1 5.2 5.3 5.4 5.5 5.6
Time (s)
)RAVM(
rewop
evitcaeR
Load
addition
Load
removal
80
Fault: 430 ms
60
40
20
0
4.9 5 5.1 5.2 5.3 5.4 5.5 5.6
Time (s)
)RAVM(
rewop
evitcaeR
377.3
377.2
377.1
377.0
376.9
376.8
376.7
0 2 4 6 8 10 12 14 16 18 20
Time (s)
Load
removal Load
addition
)s/dar(
deeps
rotoR
Removal of load at 5s
Addition of load at 5.43 s
377.3
377.2
377.1
377.0
376.9
376.8
376.7
0 2 4 6 8 10 12 14 16 18 20
Time (s)
)s/dar(
deeps
rotoR
Fault applied at 5s and cleared at 5.43 s.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:19 UTC from IEEE Xplore. Restrictions apply.

This will help in isolating faults efficiently without causing stress on grid infrastructure for both cases (removal and addition
unnecessary disconnections or cascading failures. of loads). As data center electricity demand is expected to rise
sharply, potentially reaching 321 TWh by 2030, these impacts
D. Pre-connection network impact assessment.
are likely to intensify if not properly addressed. To ensure a
Before any data center is connected to the grid, a stable and resilient power grid, it is crucial to adopt proactive
comprehensive grid impact study must be conducted. This study strategies such as demand-side management, advanced grid
should assess whether the connection would degrade existing control techniques, and infrastructure upgrades. Based on the
grid conditions, such as voltage stability, thermal limits, fault findings, this work suggests valuable recommendations for
level tolerances, or sub-synchronous oscillation. Also, it is utility operators, planners, and policymakers in designing robust
important to accurately model the data center loads for the pre- frameworks to accommodate the accelerating load demands of
connection stuides. The connection should only proceed if the future data centers while maintaining the security and efficiency
study confirms no adverse impact. of the power system. Further studies need to be carried out to
E. Incorporate phase measurement unit (PMU)-based
understand the impact of rapid growing data center load
implementations on the highly penetrated renewable energy
monitoring
networks operated by grid following and grid forming convert
To enhance observability and situational awareness, PMU- systems.
based monitoring systems should be integrated at points of
interconnection with data centers. These devices provide high- ACKNOWLEDGEMENT
resolution, time-synchronized measurements that help operators
This work was supported by the Australian Research
detect dynamic disturbances and implement corrective actions
Council (ARC) Discovery Project, DP200103405.
in real time.
F. Analyze active power recovery following fault clearance
REFERENCES
[1] M. Koot, F. Wijnhoven, “Usage impact on data center electricity needs:
The behavior of data center loads during post-fault recovery
A system dynamic forecasting model,” Appl. Ener., vol. 291, no. 116798,
must be thoroughly examined during connection studies. pp. 1–13, Mar.2021.
Specifically, the rate and magnitude of active power recovery [2] P. Luo, X. Wang, Y. Li, “The impact of datacenter load regulation on the
should be captured to ensure that sudden surges do not create stability of integrated power systems,” Sus. Ener. Tech. Assess., vol. 42,
secondary disturbances. no. 100875, pp.1–11, Dec. 2020.
[3] D. Liu, C. K. Tse, J. Yang and X. Zhang, “Revealing cascading failure
G. Define active power ramp rate limits during disturbances vulnerability in evolving power grids with increasing penetration of
inverter-based resources,” IEEE Trans. Cir. Syst., vol. 72, no. 9, pp.
Regulations should specify permissible ramp rates for active 5192–5204, Sep. 2025.
power during voltage disturbances and recovery as well for [4] R. Mittal, Z. Miao, L. Fan and D. Ramasubramanian, “Oscillation risks
normal grid condtion. This will prevent abrupt power injections of grid-following and grid-forming inverter-based resources in series-
compensated networks,” IEEE Trans. Power Del., vol. 40, no. 4, pp.
or withdrawals that can stress grid components and compromise
2426–2438, Aug. 2025.
stability during dynamic conditions.
[5] Y. Gu and T. C. Green, “Power system stability with a high penetration
of inverter-based resources,” Proc. IEEE, vol. 111, no. 7, pp. 832–853,
H. Validate site-specific simulation models with actual
Jul. 2023.
performance [6] M. Albright et al., “Characteristics and risks of emerging large loads”
Large load task force white paper, North American Electric Reliability
A critical regulatory requirement should be the validation of
Company (NERC), Jul. 2025.
data center load simulation models using on-site performance
[7] M. Dayarathna, Y. Wen and R. Fan, “Data center energy consumption
data. This model validation process ensures that planning and modeling: A survey,” IEEE Commu. Sur. Tutor., vol. 18, no. 1, pp. 732–
operational studies reflect real-world behavior, enhancing the 794, First quart. 2016.
accuracy of grid impact assessments and control strategies. [8] J. Sun, S. Wang, J. Wang and L. M. Tolbert, “Dynamic model and
converter-based emulator of a data center power distribution system,”
By adopting and enforcing these regulatory strategies, IEEE Trans. Power Electron., vol. 37, no. 7, pp. 8420–8432, Jul. 2022.
[9] S. A. Shezan, M. F. Ishraque, K. Ahmad, M. N. Hasan, G. Shafiullah and
system operators and policymakers can better accommodate
M. M. Rahman, “Performance evaluation of constant voltage and reactive
large-scale data center loads without compromising grid
power control strategies for renewable-integrated grid-connected EV
security, stability, or operational resilience. These charging stations,” IEEE Trans. Ind. Appl., pp. 1–10, Jun. 2025.
recommendations support a coordinated and proactive approach [10] W. Si, J. Fang, X. Chen, T. Xu, and S. M. Goetz, “Transient angle and
to future grid planning in the context of rapidly growing digital voltage stability of grid-forming converters with typical reactive power
control schemes,” J. Emer. Selec. Topics Power Electron., vol. 13, no. 3,
infrastructure.
pp. 2917–2927, Jun. 2025.
V. CONCLUSIONS
[11] M. Mirmohammad and S. P. Azad, “Control and stability of grid-forming
inverters: A comprehensive review,” Energies, vol. 17, no. 13, 2024.
This work has demonstrated that the growing integration of [12] J. D. Wilson, Z. Zimmerman, and R. Gramlich, “Strategic industries
large-scale data center loads into electrical power networks surging: Driving US power demand” Grid Strategies, Dec. 2024.
[13] “Power system stability guideline,” Australian Energy Market Operator
presents considerable challenges to grid stability and operational
(AEMO), ver. 1, pp.1–15, Oct. 2023. Access on Sep. 2025.
reliability. Through comprehensive analysis using PSCAD [14] IEEE 14 bus system. PSCAD Models and Examples, Access on Sep. 2025.
simulations on the IEEE 14-bus test system, it is evident that [Online available]: https://www.pscad.com/knowledge-base/article/26.
significant data center penetration can cause frequency [15] Salient and non-salient models for synchronous generator. PSCAD
fluctuations with high ramp, voltage instability, and increased Models and Examples, Access on Sep. 2025. [Online available]:
https://www.pscad.com/knowledge-base/article/29.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:19 UTC from IEEE Xplore. Restrictions apply.