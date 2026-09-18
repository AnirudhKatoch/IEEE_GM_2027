(cid:19)(cid:17)(cid:19)(cid:23)(cid:1)(cid:42)(cid:38)(cid:38)(cid:38)(cid:1)(cid:51)(cid:86)(cid:83)(cid:66)(cid:77)(cid:1)(cid:38)(cid:77)(cid:70)(cid:68)(cid:85)(cid:83)(cid:74)(cid:68)(cid:1)(cid:49)(cid:80)(cid:88)(cid:70)(cid:83)(cid:1)(cid:36)(cid:80)(cid:79)(cid:71)(cid:70)(cid:83)(cid:70)(cid:79)(cid:68)(cid:70)(cid:1)(cid:9)(cid:51)(cid:38)(cid:49)(cid:36)(cid:10)
Dynamic Modeling of Large Data Centers
Integrated Electric Grid With Impact Analysis and
Oscillatory Behavior Assessment
Md Hasnain Arifin, Student Member, IEEE, Sadique Faisal Khan, Student Member, IEEE,
Sukumar Kamalasadan, Fellow, IEEE, Michael Smith, Senior Member, IEEE,
Yashodhan P. Agalgaonkar, Senior Member, IEEE, and Ravindra Singh, Senior Member, IEEE
Abstract—This paper presents an integrated modeling frame- utilization,workloadpatterns,andcoolingrequirements.Vari-
work that captures both the electrical behavior of data cen- ations in server workload may change power consumption
ters and the distinctive operational features of interconnected
by nearly 100%, resulting in rapid changes in load demand
power grids. A detailed data center model is developed, in-
that can influence grid stability and power quality [3]. At the
corporating server clusters, power electronic interfaces, and
standby generation, with particular focus on load dynamics bulk power system level, the increasing penetration of large
during demand response events, backup power transitions, and data center loads introduces several operational and planning
power quality disturbances. The model is coupled with an challenges as these facilities often connect at transmission
electrical circuit representation of variable IT loads, capturing
voltage levels and may exhibit rapid ramping characteristics
the dynamic characteristics of AI training workloads. Using
due to power electronic controls and computational workload
this integrated framework, the impact of data center operations
on grid performance is evaluated, including voltage variations, cycles. Recent grid reliability assessments have highlighted
loss-of-load events, and fault conditions. In addition, grid-level that emerging large loads, including hyperscale data centers,
oscillationsassociatedwithhighpenetrationofdatacenterloads can create stability risks related to frequency response, rotor
areexamined.Resultsindicatethatrapidvariationsindatacenter
angle stability, voltage stability, and converter-driven interac-
loadcan:(a)shiftexistingand/ordevelopnewoscillatorymodes,
tions [4].
(b)increaseharmonicdistortion,(c)reducesystemdamping(up
to 52%), and (d) induce frequency deviations with a maximum Furthermore, most IT equipment in modern data centers
of approximately 0.36Hz. These findings highlight the potential relies on switched-mode power supplies and other power-
impact of large-scale data center dynamics on grid stability. electronicinterfaces,causingtheloadtobehaveasanonlinear
IndexTerms—EMTmodeling,Datacentermodeling,Informa- source of current distortion. These nonlinear characteristics
tionTechnology(IT)loadmodeling,DatacenterUninterruptible introduceharmoniccurrentsintotheelectricalnetwork,which
Power System (UPS) modeling, Data center modeling for EMT
may lead to increased thermal stress in transformers, ad-
studies.
ditional power losses, and voltage waveform distortion in
I. INTRODUCTION
both distribution and transmission systems [5], [6]. With the
THE rapid growth of large-scale data centers has sig-
widespread adoption of high-frequency switching converters
nificantly increased electricity demand and introduced
and power factor correction circuits, harmonic components
newoperationalchallengesformodernpowersystems.Recent
and interharmonics may propagate through the network and
studiesindicatethatlarge-scalecomputingfacilitiescanreach
interact with other power electronic devices [7].
hundreds of megawatts or even gigawatt-scale loads, mak-
In addition to harmonic distortion, dynamic interactions
ing them comparable to large industrial consumers in power
between converter-based loads and the power system can
systems [1]. Consequently, their integration into transmission
influence electromechanical oscillations. As data centers in-
and distribution networks requires careful assessment of their
creasinglyrelyonpowerelectronics,theiraggregatedbehavior
electrical characteristics and system-level impacts.
may affect low-frequency oscillation modes of interconnected
Unlike traditional industrial loads, data centers are dom-
power systems. The interaction between converter control
inated by power-electronic equipment such as switched-
systems, UPS architectures, and grid dynamics may either
mode power supplies, uninterruptible power supplies (UPS),
damp or amplify oscillatory modes depending on the control
variable-speed drives, and inverter-based cooling systems.
strategies and system conditions. Although extensive research
These converter-based components introduce nonlinear be-
has investigated oscillation phenomena caused by inverter-
havior, harmonic distortion, and dynamic load variability in
based generation [8], [9], relatively limited work has focused
the power system [2]. In addition, the electrical demand of
on the impact of renewable energy and large computational
data centers can fluctuate significantly depending on server
loads on electromechanical oscillation behavior [10].
Modern data centers also employ complex internal electri-
The first, second, third, and fourth authors are with the Power,
Energy, and Intelligent Systems Laboratory (PEISL), University of cal infrastructures including utility transformers, switchgear,
North Carolina at Charlotte, Charlotte, NC 28223 USA. (e-mail: automatictransferswitches,UPSsystems,standbygenerators,
arifin@charlotte.edu, skhan77@charlotte.edu, skamalas@charlotte.edu,
and power distribution units. During grid disturbances such
Michael.Smith@charlotte.edu). The fifth author is a senior member of
IEEE.(email:yashodhan.agalgaonkar@nlr.gov).Thesixthauthoriswiththe as transient faults or voltage sags, UPS systems temporarily
National Rural Electric Cooperative Association (NRECA), 4301 Wilson support critical loads while backup generators start up, pre-
Blvd,Arlington,VA282203USA.(e-mail:Ravindra.Singh@nreca.coop.)
venting service interruptions [11], [12]. However, interactions
979-8-3195-4573-2/26/$31.00 ©2026 IEEE (cid:18)
DOI 10.1109/REPC71040.2026.00010
01000.6202.04017CPER/9011.01
:IOD
| EEEI
6202©
00.13$/62/2-3754-5913-8-979
|
)CPER(
ecnerefnoC
rewoP
cirtcelE
laruR
EEEI
6202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:19 UTC from IEEE Xplore. Restrictions apply.

between these power electronic devices and the external grid
may introduce dynamic phenomena that are not yet fully
understood. Also, data centers can potentially participate in
demand response programs, load shifting strategies, and fre-
quency regulation services [13], [14].
Thispaperinvestigatestheimpactoflarge-scaledatacenter
loads on power system dynamics, with a focus on low-
frequency oscillation modes, harmonic distortion, and grid
integration challenges. The work is based on our earlier work
in the direction for analyzing grid stability and mitiation with
power electronic based energy sources [15]. The study first
reviews the electrical characteristics and internal infrastruc-
ture of modern data centers. Next, the dynamic interactions
betweendatacenterloadsandpowersystemoscillatorymodes
Fig.1.Onelinediagramofthedynamicdatacentermodel.
are analyzed. Finally, the paper discusses key operational
and planning challenges associated with integrating large
computational loads into modern power systems. The main andgovernor.ExpandingontheelementsshowninFig.1,the
contributions of this work are summarized as follows: datacenter’spowerelectronicscanberepresentedasaPower
• Development of a grid-integrated electromagnetic tran- Supply Unit (PSU) comprising a Power Factor Converter
sient (EMT) modeling framework for large-scale data (PFC) and an isolated DC-DC converter. Additionally, a UPS
centers, including dynamic models of key power elec- consisting of double-conversion (AC/DC and DC/AC) units
troniccomponentssuchasPSUs,PDUs,andUPSsystems is modeled as backup support. The present study primarily
including AC–DC, DC–DC, and DC–AC converters), focuses on data center load dynamics and therefore cooling
along with analysis of UPS system operational modes. loads are not considered.
• Investigationofdisturbance-drivendynamicresponsesof A. Modeling of PSU
large data center loads under multiple operating scenar-
There are two main parts in PSU a) 480 V AC to 480 V
ios, including temporary grid voltage drops, grid-to-UPS
DC converter, and b) a DC-DC isolated converter, 480 V
transitions, and UPS-to-grid reconnection events.
DC to 48 V DC, for the IT load. For the 480 V AC-to-
• Evaluation of system-level impacts of large-scale data
480 V DC conversion, the output-voltage regulation loop first
center loads with bulk power grid, including frequency generates I lref to determine the duty cycle. This duty cycle,
deviationanalysis,settlingcharacteristics,electromechan- d,isessentialforgeneratingthePWMsignalrequiredforthe
ical oscillation modes, damping ratios, and harmonic
converter’s control to maintain the desired DC voltage. The
distortion.
associated equations are given below:
• Comparative assessment of constant data center loads
I =K (V −V )+...
andAItrainingworkloadprofilestoidentifyhowrapidly lref P (cid:2) ref meas
varying computational loads influence modal character- ... K I t (V −V )dt (1)
istics, oscillation damping, and harmonic distortion in T ref meas
0
interconnected power systems.
(cid:2)
low T s h . e S r e e c m tio a n in I in I g di s s e c c u t s i s o e n s s th o e f t g h r i i s d p in a t p e e g r ra a t r e e d o d r a g t a a n c iz e e n d ter as EM fo T l- d=K P1 (I lref −I l )+ K T I1 t (I lref −I lmeas )dt (2)
0
modelingframework.SectionIIIdescribesthetestsystemand where I lref is the PFC inductor reference current, V ref is
test case scenarios. Section III-A showcases the simulation the desired reference voltage for PFC, K P,K I, are the PID
results, which includes discussion in Section III-B. Then, the parameters. V meas, & I lmeas are measured PFC voltage and
conclusions are presented in Section IV.
measured PFC inductor current, respectively.
II. GRIDINTEGRATEDDATACENTERMODELING TheDC-DCisolatedconverteralsousesavoltageregulation
FRAMEWORK loop, like the AC-DC converter, to sequentially generate the
Fig.1showstheone-linediagramofthedynamicdatacenter diode current reference and the duty cycle to create a PWM
model. The data center includes a Power Supply Unit (PSU), signalforconvertercontrol,exceptitusesalineartransformer
PowerDistributionUnit(PDU),UninterruptiblePowerSupply to isolate the primary and secondary sides.
(UPS), Cooling Load, and IT loads, including IT racks. It B. Modeling of Data Center load
connects to the electric grid through a 480 V bus, which is
ForITloadmodeling,avariableresistanceisrepresentedas
stepped up by a medium-voltage transformer (480 V/13 kV).
the data center load at the PSU 48 V terminal. The resistance
Thetransmissionsystemandgenerationstationarerepresented value, R, corresponding to the desired IT load power is
as an additional voltage step-up to 230 kV and connection to
obtained as,
the generation station via a transmission line. The generation
V2
station consists of a station step-down transmission and a R= dc (3)
P
dynamic, full-order generator model with excitation system IT
(cid:19)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:19 UTC from IEEE Xplore. Restrictions apply.

(cid:2)
K t
D=K P3 (I Lref −I L )+ T I3 (I Lref −I Lmeas )dt (5)
0
where I Lref is the rectifier inductor reference current, V dcref
isthedesiredDCreferencevoltageforrectifier,allK P,K I are
thePIDparameters.V dcmeas,&I Lmeas aremeasuredrectifier
voltage & measured rectifier inductor current.
(a)5sAITrainingProfile[4] (b)ModelGeneratedAITrainingProfile The 800 V DC battery is associated with the inverter
Fig.2.AItrainingdatacenterprofile. to regulate the desired AC voltage as well as the required
powerwhenneeded.WithadesiredACvoltagemagnitudeM,
desired angle θ and desired frequency f, the input frequency
where V dc represents the DC bus voltage and P IT denotes whichcanbepresentedasf(k),isfirstconvertedintoangular
the IT load power. For a specified P IT value, the equivalent
frequency,
resistance can be calculated directly from (3), allowing the
desired data center load profile to be derived. ω(k)=2πf(k). (6)
Torepresentlarge-scaledatacenteroperation,thePSU–load
subsystemisscaledusinganequivalentparallelaggregationof A discrete-time integrator with sampling period T s computes
the accumulated phase angle,
multiple units. This scaling approach preserves the electrical
behavior of individual racks while enabling representation of θ i (k)=θ(k−1)+ω(k)T s . (7)
high aggregated load levels. Fig. 2 illustrates the AI training
workload used in this study. Fig. 2a shows the reference In order to avoid angle divergence from one electrical cycle,
5 s AI training power profile reported in [4], while Fig. 2b mod operation is used.
presentsthecorrespondingmodel-generatedloadprofileusing θ m (k)=mod(θ(k), 2π) (8)
anelectriccircuitmodel.Thegeneratedprofilecloselyfollows
the dynamic characteristics of the reference workload and is Theinputangleφ(k) isconvertedfromdegreestoradiansas,
used to represent rapidly varying AI computational demand. π
C. UPS Modeling and Modes of Operation in Data Centers φ i (k)=φ(k) 180◦ . (9)
Uninterruptible Power Supply (UPS) systems constitute a Thethree-phaseangledisplacementiscalculatedasfollowing:
⎡ ⎤
fundamentalcomponentofmoderndatacenters,ensuringhigh
0
availability and power quality for mission-critical information ⎢ ⎥
technology(IT)loads.UPSoperatingmodesinfluenceenergy Δφ abc =⎣−2 3 π⎦. (10)
efficiency,powerconditioningcapability,andriskofexposure +2π
3
to voltage or frequency disturbances. Fig. 3 illustrates UPS
Theinstantaneousphaseofeachphaseisthenobtainedbythe
modes of operation.
following equation:
θ abc (k)=θ m (k)+φ i (k)+Δφ abc . (11)
Finally,foragivendesiredvoltagemagnitudeinputM(k),the
generated three-phase voltages can be expressed as,
u abcref =M(k) sin(θ abc (k)). (12)
This generated u abcref is used for controlling the average
model three-level neutral-point-clamped (NPC) converter (in-
verter).
Fig.3.ModesofoperationofUPS. III. TESTSYSTEM,SIMULATIONRESULTSAND
UPS modeling can be categorized into three major parts. DISCUSSIONS
a) AC-DC Conversion model using a 480 V AC to 800 V The study is conducted using the standard Kundur two-
DC converter, b) 800 V DC battery model, and c) DC-AC Area power system [16] shown in Fig. 4. The two Areas
Conversion model with a controller for 800 V DC to 480 V areinterconnectedthroughlongtransmissionlinesandsupply
AC conversion. aggregated loads for Area-1 at bus-7 and for Area-2 at bus-9.
FortheAC-DCconverter(Rectifier),firstI Lref isgenerated, For this study, all Area-1 measurements are from bus-7, and
which is used to generate the duty cycle, D, for the PWM all Area-2 measurements are from bus-9. The Area-1 load is
signal.ThePWMsignalisthenusedfortheconvertercontrol represented as 867 MW conventional load combined with a
to regulate the desired dc voltage. The associated equations 100 MW data center load connected through the distribution
are given below: interface shown in Fig. 1. Area-2 load comprises the original
I =K (V −V )+... aggregated load of 1767 MW.
Lref P2 dcref dcmeas
(cid:2)
K t (4) To evaluate the dynamic interactions between the power
... T I2 (V dcref −V dcmeas )dt system and the data center load, three disturbance scenarios
0 are considered:
(cid:20)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:19 UTC from IEEE Xplore. Restrictions apply.

|     |     |     |     |     |     |     | f          |     | f        |          |          |     |          |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | -------- | -------- | --- | -------- |
|     |     |     |     |     |     |     | where rise | and | drop are | the peak | positive | and | negative |
deviationsoffrequency,respectively,andf
|     |     |     |     |     |     |     |     |     |     |     | nom | isthenominal |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
(60Hz).
system frequency
Pleasenotethatconstantdatacenterloadmeansafullscale
|     |     |     |     |     |     |     | dynamic | model | of the data | center | with constant | AI  | training |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | ------ | ------------- | --- | -------- |
profile.
Fig.4.One-linediagramoftheKundurTwo-AreaSystem.
| • Temporary |     | Voltage | Sag: | A short-duration |     | voltage sag |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ---- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
of 0.75 pu is applied for three cycles at the middle of (a)GridVoltage(Temp. (b)GridVoltage (c)GridVoltage(UPSto
|         |      |        |           |        |      |                | VoltageDropinGrid) |     | (Three-PhaseFaultinGrid) |     | GridTransition) |     |     |
| ------- | ---- | ------ | --------- | ------ | ---- | -------------- | ------------------ | --- | ------------------------ | --- | --------------- | --- | --- |
| the tie | line | at the | grid side | at t = | 15 s | for a constant |                    |     |                          |     |                 |     |     |
data center load study and at t=16 s for an AI training Fig.5.GridVoltagewithconstantdatacenterload.
datacenterloadprofilestudy.Duringthisevent,thedata
centerremainsconnectedtothegrid,andnogrid-to-UPS
| switching                                          | occurs.        |            |          |              |            |             |                    |     |     |     |     |     |     |
| -------------------------------------------------- | -------------- | ---------- | -------- | ------------ | ---------- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- |
| • Grid-to-UPS                                      |                | Transition |          | with Load    | Loss:      | A three-    |                    |     |     |     |     |     |     |
| phase                                              | fault          | is applied | for      | three cycles | at         | the Area-1  |                    |     |     |     |     |     |     |
| bus                                                | on the         | grid side  | at       | t = 30       | s, causing | the grid    |                    |     |     |     |     |     |     |
| voltage                                            | to temporarily |            | collapse | to zero.     | The        | data center |                    |     |     |     |     |     |     |
| immediatelytransitionstoUPSoperation.Asaresult,the |                |            |          |              |            |             | (a)Area-1Frequency |     |     |     |     |     |     |
grid experiences a temporary loss of the 100 MW data (Temp.VoltageDropin (b)Area-1Frequency (c)Area-1Frequency(UPS
|        |      |                     |     |     |     |     | Grid) |     | (Three-PhaseFaultinGrid) |     | toGridTransition) |     |     |
| ------ | ---- | ------------------- | --- | --- | --- | --- | ----- | --- | ------------------------ | --- | ----------------- | --- | --- |
| center | load | until reconnection. |     |     |     |     |       |     |                          |     |                   |     |     |
• UPS-to-GridReconnection:Att=50s,thedatacenter Fig.6.Area-1(Bus7)Frequencywithconstantdatacenterload.
| reconnects        | from    | UPS            | operation  | back               | to the       | utility grid. |                     |     |                    |     |                        |     |     |
| ----------------- | ------- | -------------- | ---------- | ------------------ | ------------ | ------------- | ------------------- | --- | ------------------ | --- | ---------------------- | --- | --- |
| These disturbance |         | scenarios      | allow      | assessment         | of           | the dynamic   |                     |     |                    |     |                        |     |     |
| response          | of the  | grid–data      | center     | interaction        |              | under voltage |                     |     |                    |     |                        |     |     |
| disturbances,     | load    | disconnection, |            | and                | reconnection | events,       |                     |     |                    |     |                        |     |     |
| with a constant   |         | and an         | AI-trained | data               | center       | load profile. |                     |     |                    |     |                        |     |     |
|                   |         |                |            |                    |              | (50 μs        |                     |     |                    |     |                        |     |     |
| The test          | system  | was modeled    |            | in MATLAB/Simulink |              |               |                     |     |                    |     |                        |     |     |
| discrete time     | step).  |                |            |                    |              |               |                     |     |                    |     |                        |     |     |
| A. Simulation     | Results |                |            |                    |              |               | (a)Area-2Frequency  |     |                    |     |                        |     |     |
|                   |         |                |            |                    |              |               | (Temp.VoltageDropin |     | (b)Area-2Frequency |     | (c)Area-2Frequency(UPS |     |     |
Forthesimulationdemonstration,twodatacenterloadtypes Grid) (Three-PhaseFaultinGrid) toGridTransition)
are used. The first is a constant load, and the second is an Fig.7.Area-2(Bus9)Frequencywithconstantdatacenterload.
| AI training | profile    | mentioned | in  | [4]. For   | this study | frequency |       |          |             |      |         |     |     |
| ----------- | ---------- | --------- | --- | ---------- | ---------- | --------- | ----- | -------- | ----------- | ---- | ------- | --- | --- |
|             |            |           |     |            |            |           | 2) AI | Training | Data Center | Load | Profile |     |     |
| response    | at various | points    | are | evaluated. |            |           |       |          |             |      |         |     |     |
ThedynamicresponsesofthesystemundertheAItraining
| 1) Constant | Data | Center | Load |     |     |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The dynamic responses of the system under constant data data center load profile are illustrated in Figs. 8–10. These
center load and disturbance scenarios described in Section III figures present the variations of grid voltage and system
are illustrated in Figs. 5–7, which show the variations in grid frequency at Areas 1 and 2 under the considered disturbance
events,withtheAItrainingdatacenterloadprofile.Thecorre-
| voltage and | system | frequency |     | at Areas | 1 and | 2 during the |     |     |     |     |     |     |     |
| ----------- | ------ | --------- | --- | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
spondingfrequencydeviationcharacteristicsandsettlingtimes
| considered | disturbance |     | events, | with the data | center | load held |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------- | ------------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
aresummarizedinTableI,whilethemodalcharacteristicsand
| constant | (100 MW). | The | corresponding |     | frequency | deviation |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
characteristics and settling times are summarized in Table I, harmonic distortion under these scenarios are summarized in
| while the | modal      | characteristics |     | and harmonic |     | distortion as- | Table II. |     |     |     |     |     |     |
| --------- | ---------- | --------------- | --- | ------------ | --- | -------------- | --------- | --- | --- | --- | --- | --- | --- |
| sociated  | with these | events          | are | summarized   | in  | Table II. The  |           |     |     |     |     |     |     |
B. Discussions
| percentage | change | in system | frequency |     | due to | a disturbance |     |     |     |     |     |     |     |
| ---------- | ------ | --------- | --------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
1) FrequencyDynamicResponseUnderDisturbanceEvents
| is calculated | by        | summing | the         | maximum | rise and    | drop of the |               |          |             |              |                 |              |      |
| ------------- | --------- | ------- | ----------- | ------- | ----------- | ----------- | ------------- | -------- | ----------- | ------------ | --------------- | ------------ | ---- |
|               |           |         |             |         |             |             | The frequency |          | deviation   | and settling | characteristics |              | sum- |
| frequency     | deviation | and     | normalizing | it to   | the nominal | system      |               |          |             |              |                 |              |      |
|               |           |         |             |         |             |             | marized       | in Table | I highlight | several      | important       | observations |      |
| frequency     | f nom.    | This is | expressed   | as:     |             |             |               |          |             |              |                 |              |      |
regardingthedynamicimpactofdatacenterloaddisturbances
|     |     |     | f rise +f | drop   |     |      | on the power | system. |             |            |           |              |            |
| --- | --- | --- | --------- | ------ | --- | ---- | ------------ | ------- | ----------- | ---------- | --------- | ------------ | ---------- |
|     | Δf  | =   |           | ×100%, |     | (13) |              |         |             |            |           |              |            |
|     |     | %   | f         |        |     |      |              |         |             |            |           |              |            |
|     |     |     | nom       |        |     |      | • Maximum    |         | frequency   | deviation: | Area-2    | consistently |            |
|     |     |     |           |        |     |      | demonstrates |         | the largest | frequency  | deviation |              | across all |
(cid:21)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:19 UTC from IEEE Xplore.  Restrictions apply.

TABLEI
Frequencydynamiccharacteristicsunderdifferentdatacenterloadprofilesandeventscenarios(percentagechangeofnominalfrequency60Hz)
Case
|     | DataCenterLoad |     | Parameters |     |                  |     |           |     |     |     |     |
| --- | -------------- | --- | ---------- | --- | ---------------- | --- | --------- | --- | --- | --- | --- |
|     |                |     |            |     | TemporaryVoltage |     | GridtoUPS |     |     |     |     |
UPStoGridEvent
|     |     |     |     |     | DropatGridEvent | +LoadLossEvent |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------- | -------------- | --- | --- | --- | --- | --- |
Area-1:FrequencyDeviation(R-D) 0.18–0.04Hz(0.37%) 0.24–0.11Hz(0.58%) 0.025–0.19Hz(0.36%)
|     |     |     | Area-1:SettlingTime |     | 5s  |     | 11s |     |     | 12s |     |
| --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ConstantDataCenterLoad
Area-2:FrequencyDeviation(R-D) 0.22–0.06Hz(0.47%) 0.36–0.07Hz(0.72%) 0.04–0.14Hz(0.30%)
|     |     |     | Area-2:SettlingTime |     | 4.5s |     | 10s |     |     | 12s |     |
| --- | --- | --- | ------------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
Area-1:FrequencyDeviation(R-D) 0.17–0.04Hz(0.35%) 0.22–0.12Hz(0.57%) 0.04–0.14Hz(0.30%)
| AITrainingDataCenterProfile |     |     | Area-1:SettlingTime |     | 4s  |     | 10s |     |     | 7s  |     |
| --------------------------- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Area-2:FrequencyDeviation(R-D) 0.22–0.06Hz(0.47%) 0.36–0.07Hz(0.72%) 0.04–0.14Hz(0.30%)
|        |          |       | Area-2:SettlingTime |     | 4s  |     | 10s |     |     | 7s  |     |
| ------ | -------- | ----- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|        | =⇒       | =⇒    |                     |     |     |     |     |     |     |     |     |
| Note:R | RiseandD | Drop. |                     |     |     |     |     |     |     |     |     |
TABLEII
Modalcharacteristicsandharmonicdistortionunderdifferentdatacenterloadprofilesandeventscenarios
|     | Parameters | LoadCondition |     |                |                  | Events |           |     |     |            |     |
| --- | ---------- | ------------- | --- | -------------- | ---------------- | ------ | --------- | --- | --- | ---------- | --- |
|     |            |               |     | StandardKundur |                  |        | GridtoUPS |     |     |            |     |
|     |            |               |     |                | TemporaryVoltage |        |           |     |     | UPStogrid  |     |
|     |            |               |     | Systemwith     |                  |        |           | +   |     |            |     |
|     |            |               |     | RingDown       | DropatGrid       |        |           |     |     | Transition |     |
LoadLoss
Mode(Hz) ConstantDataCenter 0.65,1.13,1.18 0.64,1.11,1.15 0.63,1.1, 1.27 0.64,1.11, 1.29
AITrainingProfile (SpotLoad) 0.64, 0.97,1.13, 2.3 0.63,1.1, 1.27 0.65, 1.01, 1.83, 3.24
DampingRatio(%ζ) ConstantDataCenter 2.3,10.85,8.32 2.2,9.88,8.34 2.4,10.7,0.6 1.9,9.94,0.55
AITrainingProfile (SpotLoad) 1.41,2.1,8.46,2.65 1.95,10.81,1.22 1.1,3,3.01,3.25
|       | THD(%)                    | ConstantDataCenter |                                | 0.7        | 2.2        |        | 3.58    |                 |     | 3.38        |            |
| ----- | ------------------------- | ------------------ | ------------------------------ | ---------- | ---------- | ------ | ------- | --------------- | --- | ----------- | ---------- |
|       |                           | AITrainingProfile  |                                | (SpotLoad) | 2          |        | 3.07    |                 |     | 2.53        |            |
| Note: | indicatesmodeshifting,and |                    | indicatesnewlyintroducedmodes. |            |            |        |         |                 |     |             |            |
|       |                           |                    |                                |            | scenarios. | During |         | the Grid-to-UPS |     | transition, | a load-    |
|       |                           |                    |                                |            | loss       | event  | results | in a frequency  |     | deviation   | of approx- |
0.36 Hz.
|     |     |     |     |     | imately   |     |      | These       | findings  | suggest  | that Area-2 |
| --- | --- | --- | --- | --- | --------- | --- | ---- | ----------- | --------- | -------- | ----------- |
|     |     |     |     |     | undergoes | the | most | significant | transient | response | during      |
disturbances.
|                      |     |                |     |                      | • Most | severe     | disturbance | event:      | Among | the        | three distur- |
| -------------------- | --- | -------------- | --- | -------------------- | ------ | ---------- | ----------- | ----------- | ----- | ---------- | ------------- |
|                      |     |                |     |                      | bance  | scenarios, | the         | Grid-to-UPS |       | transition | with load     |
| (a)GridVoltage(Temp. |     | (b)GridVoltage |     | (c)GridVoltage(UPSto |        |            |             |             |       |            |               |
VoltageDropinGrid) (Three-PhaseFaultinGrid) GridTransition) lossproducesthelargestfrequencyexcursionsacrossthe
Fig.8.GridVoltagewithAITrainingDataCenterLoad. system, indicating that the sudden disconnection of the
|     |     |     |     |     | data       | center | load, along | with        | the       | Grid-to-UPS | transition, |
| --- | --- | --- | --- | --- | ---------- | ------ | ----------- | ----------- | --------- | ----------- | ----------- |
|     |     |     |     |     | introduces | the    | most        | significant | transient | imbalance.  |             |
• Settlingtimecharacteristics:Thelongestsystemrecovery
timesarealsoobservedduringtheGrid-to-UPStransition
|     |     |     |     |     | following | a   | load-loss | event, | with | system | stabilization |
| --- | --- | --- | --- | --- | --------- | --- | --------- | ------ | ---- | ------ | ------------- |
10–11s.
|     |     |     |     |     | occurring | in              | approximately |            |      |      |                 |
| --- | --- | --- | --- | --- | --------- | --------------- | ------------- | ---------- | ---- | ---- | --------------- |
|     |     |     |     |     | Overall,  | the Grid-to-UPS |               | transition | with | load | loss represents |
(a)Area-1Frequency
(Temp.VoltageDropin (b)Area-1Frequency (c)Area-1Frequency(UPS the disturbance condition that produces the most pronounced
Grid) (Three-PhaseFaultinGrid) toGridTransition) system frequency dynamics, with Area-2 experiencing the
Fig.9.Area-1(Bus7)FrequencywithAITrainingDataCenterLoadProfile. largest deviations among the studied locations.
|     |     |     |     |     | 2) Oscillation    |                 | Modes   | and Harmonic |          | Characteristics |             |
| --- | --- | --- | --- | --- | ----------------- | --------------- | ------- | ------------ | -------- | --------------- | ----------- |
|     |     |     |     |     | The modal         | characteristics |         | and          | harmonic | distortion      | summa-      |
|     |     |     |     |     | rized in          | Table II        | provide | insight      | into     | the oscillatory | behavior    |
|     |     |     |     |     | and power-quality |                 | impacts | associated   |          | with data       | center load |
integration.
|     |     |     |     |     | Baseline | modes | of  | oscillation: | The | third | column in Ta- |
| --- | --- | --- | --- | --- | -------- | ----- | --- | ------------ | --- | ----- | ------------- |
•
bleIIprovidesoscillationmodesoftheStandardKundur
(a)Area-2(Bus9)
Frequency(Temp.Voltage (b)Area-2Frequency (c)Area-2Frequency(UPS systemwitharingdownevent.Duringthisevent,afault
DropinGrid) (Three-PhaseFaultinGrid) toGridTransition) (ring down event) is initiated and the oscillation modes
Fig.10.Area-2(Bus9)FrequencywithAITrainingDataCenterLoad are evaluated. For this a spot P−Q load is used instead
Profile. of the dynamic model of the data-center and data center
|     |     |     |     |     | load. | The modes | of  | oscillation | are  | being | seen (including |
| --- | --- | --- | --- | --- | ----- | --------- | --- | ----------- | ---- | ----- | --------------- |
|     |     |     |     |     | 0.64  | Hz, 1.11  | Hz  | 1.15        | Hz). |       |                 |
and
(cid:22)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:19 UTC from IEEE Xplore.  Restrictions apply.

• Shift in dominant oscillation modes: Compared to the loads introduce additional oscillatory interactions and power
originaltwoareamodelwithoutdatacenterload(named quality impacts that should be considered in grid integration
as the baseline Kundur system), shifts in oscillation studies.
frequencies are observed after integrating the data center Future work will focus on extending the proposed EMT
load. The dominant inter-area mode near0.65 Hz varies modeling framework to larger interconnected power systems
between approximately 0.63 and 0.65 Hz across distur- with multiple large-scale data centers and on developing co-
bancescenarios.Inaddition,severalexistingmodesabove ordinated control strategies for devices and power electronic
1 Hz shifts (such as 1.11 Hz shift to approximately interfaces to enhance oscillation damping.
0.97 Hz and 1.01 Hz, 1.15 Hz shifts to 1.13 Hz,
1.29 Hz shifts to 1.83 Hz) as shown in Table II, due ACKNOWLEDGMENT
totheeffectofconverter-baseddatacenterloaddynamic This work was partly supported by the Electrical and
characteristics with varying grid conditions. Computer Engineering Department at UNC Charlotte, and
• Emergence of additional oscillation modes: Additional NRECA.
oscillation modes appear when the system is exposed to
theAItrainingdatacenterloadprofileunderdisturbances. REFERENCES
Higher-frequency oscillations at 2.3 Hz and 3.24 Hz [1] A. Shehabi, S. Smith, D. Sartor, R. Brown, M. Herrlin, J. Koomey,
appear during disturbances, which is associated with E.Masanet,N.Horner,I.Azevedo,andW.Lintner,“UnitedStatesdata
centerenergyusagereport(2016),”DOI,vol.10,p.1372902,2016.
interactions among converter-based data center equip-
[2] S.Chalise,A.Golshani,S.R.Awasthi,S.Ma,B.R.Shrestha,L.Ba-
ment, disturbance transitions, and the rapidly varying AI jracharya, W. Sun, and R. Tonkoski, “Data center energy systems:
training load pattern. Currenttechnologyandfuturedirection,”in2015IEEEPower&Energy
SocietyGeneralMeeting. IEEE,2015,pp.1–5.
• Reduction in damping of the system: Under the data
[3] G. Zhabelova, A. Yavarian, and V. Vyatkin, “Data center power dy-
center load condition, particularly under the AI training namicswithinthesettingsofregionalpowergrid,”in2015IEEE20th
loadprofile,anoticeablereductioninthedampingofthe Conference on Emerging Technologies & Factory Automation (ETFA).
IEEE,2015,pp.1–5.
dominant inter-area oscillation mode has been observed.
[4] North American Electric Reliability Corporation, “Characteristics
Forexample,thedampingratioofthe0.65Hz inter-area and risks of emerging large loads,” North American
mode reduces from 2.3% to about 1.1% (approximately Electric Reliability Corporation, Atlanta, GA, USA,
52%) under the considered disturbance scenarios. White Paper, July 2025. [Online]. Available: https:
//www.nerc.com/globalassets/who-we-are/standing-committees/rstc/3_
• Increase of Harmonic distortion: The presence of doc_white-paper-characteristics-and-risks-of-emerging-large-loads.pdf
converter-based data center loads introduces harmonics [5] J.ArrillagaandN.R.Watson,Powersystemharmonics. JohnWiley
&Sons,2004.
as summarized in Table II compared with the baseline
[6] X.Wang,F.Blaabjerg,Z.Chen,andW.Wu,“Modelingandanalysisof
Kundur system due to the power-electronic interfaces harmonicresonanceinapowerelectronicsbasedACpowersystem,”in
associated with data center loads. 2013IEEEEnergyConversionCongressandExposition. IEEE,2013,
pp.5229–5236.
These observations indicate that while the dominant elec- [7] S.Rönnberg,M.Bollen,A.Larsson,andM.Lundmark,“Anoverview
tromechanical oscillation mode of the system remains largely of the origin and propagation of supraharmonics (2-150 kHz),” in
NordicConferenceonElectricityDistributionSystemManagementand
preserved,theintegrationofdatacenterloadsintroducesshifts
Development:08/09/2014-09/09/2014,2014.
in oscillation frequencies, reduced damping, increased har- [8] F. A. Hasnain, S. J. Hossain, and S. Kamalasadan, “A novel hybrid
monic distortion, and additional higher-frequency oscillation deterministic-stochasticrecursivesubspaceidentificationforelectrome-
chanicalmodeestimation,classification,andcontrol,”IEEETransactions
modes due to the AI training load pattern.
onIndustryApplications,vol.57,no.5,pp.5476–5487,2021.
IV. CONCLUSIONSANDFUTUREWORK [9] F.AlHasnain,A.Sahami,andS.Kamalasadan,“Anonlinewide-area
directcoordinatedcontrolarchitectureforpowergridtransientstability
Thispaperpresentedagrid-integratedelectromagnetictran- enhancement based on subspace identification,” IEEE Transactions on
sient (EMT) modeling framework to analyze the impact of IndustryApplications,vol.57,no.3,pp.2896–2907,2021.
[10] P. P. Gyang, P. Chakraborty, L. Meegahapola, and X. Yu, “Dynamic
large-scale data center loads on power system dynamics. The modeling of a data center for power system stability studies,” IEEE
model incorporates major data center subsystems, including TransactionsonPowerSystems,2025.
PSUs, PDUs, UPS systems, cooling loads, and IT loads, [11] I. IEC et al., “Uninterruptible power systems (UPS)-part 3: method
of specifying the performance and test requirements,” Uninterruptible
enablingadetailedrepresentationofconverter-drivenloadbe- powersystems(UPS)-Part,vol.3,2011.
havior.SimulationstudiesontheKundurtwo-Areabenchmark [12] C. Cottuli and J.-F. Christin, “Comparison of static and rotary UPS,”
system under three disturbance scenarios, temporary voltage Whitepaper(92),APCwhitepaper,SchneiderElectric,2008.
[13] W. E. Gnibga, A. Blavette, and A.-C. Orgerie, “Renewable energy in
drop, grid-to-UPS transition with load loss, and UPS-to-grid datacenters:Thedilemmaofelectricalgriddependencyandautonomy
reconnection, show that AI training load profiles introduce costs,”IEEEtransactionsonsustainablecomputing,vol.9,no.3,pp.
additional higher-frequency oscillatory modes and slightly 315–328,2023.
[14] P. Ren, W. Sun, Y. Wang, and G. Harrison, “Grid frequency stability
reduce damping ratios under certain disturbances. Frequency supportpotentialofdatacenter:Aquantitativeassessmentofflexibility,”
deviations remain within acceptable limits across all events, IEEETransactionsonIndustryApplications,2026.
with the UPS transition providing rapid stabilization at the [15] F. Al Hasnain, M. S. Hasan, M. H. Arifin, S. Kamalasadan, and
M.Smith,“Oscillationidentificationandfrequencydampingcontroller
PCC. The results also indicate increased harmonic distortion designforbatteryenergystoragesystemusingsubspaceidentification,”
compared with the baseline Kundur system due to converter- IEEETransactionsonIndustryApplications,vol.60,no.3,pp.4796–
based load characteristics. Overall, while the fundamental 4809,2024.
[16] P. Kundur, N. J. Balu, and M. G. Lauby, Power System Stability and
electromechanical dynamics remain intact, large data center Control. NewYork:McGraw-Hill,1994,vol.7.
(cid:23)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:19 UTC from IEEE Xplore. Restrictions apply.