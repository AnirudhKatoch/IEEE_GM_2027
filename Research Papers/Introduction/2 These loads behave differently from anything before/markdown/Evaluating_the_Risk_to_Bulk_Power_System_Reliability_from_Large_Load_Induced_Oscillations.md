Evaluating the Risk to Bulk Power System
Reliability from Large Load Induced Oscillations
Shuchismita Biswas, Antos C. Varghese, Kaustav Chatterjee, Sameer Nekkalapu, Brett Ross, and Jim Follum
Pacific Northwest National Laboratory
Richland, USA
shuchismita.biswas@pnnl.gov
Abstract—Unexpected operations of large loads (LL) like hy- posemultiplereliabilityrisks.High-amplitudeoscillationsmay
perscaledatacentersmaythreatengridreliability.Computation- causeincorrectprotection/controlactionsleadingtocascading
cycle-driven load fluctuations may introduce forced oscillations
failures. High-frequency oscillations may cause flicker or
(FOs) that can get amplified due to resonance with natural
interact with turbine torsional modes, increasing generator
modes of the power system. Planning studies informing the load
interconnectionprocessescurrentlydonotaccountfortheseLL- fatigue.Powerswingsmaybeamplifiedawayfromthesource
induced oscillations, leaving a gap in the reliability evaluations. due to resonance if the FO frequency is close to a system
To address this, we propose a simulation-based risk assessment mode [5]. Besides the risk of inadvertent protection actions,
framework that quantifies the wide-area grid reliability impact
resonance further complicates the problem of locating and
of LL-induced oscillations as a function of FO frequency and
isolating the FO source.
source location. The framework is illustrated using a 240-bus
transmissionnetworkmodelwith13potentialLLinterconnection The threat of oscillatory instability is well recognized and
locations. Multiple reliability metrics are computed, including grid operators employ various solutions to monitor and miti-
the extent of spatial propagation of FOs, risks of modal reso- gateFOsduringoperations[5],[6].Itisassumedthattheseos-
nance,andtheseverityofoscillationamplification.Theproposed
cillations occur when control equipment malfunction, and are
methodology enables system planners to pinpoint high-risk LL
notafeatureofnormalloadoperations.Therefore,thesystem-
interconnectionpoints,FOfrequenciesofconcern,anddetermine
targeted mitigation strategies. widereliabilityimpactofload-inducedoscillationsistypically
IndexTerms—largeelectricload,datacenter,forcedoscillation, not studied during planning. However, given the cyclic nature
reliability of large computational loads, assessing the impact of FOs has
I. INTRODUCTION
become critical at the planning stage itself.
The power grid is experiencing an era of rapid load growth
At present, there is a lack of established study procedures
duetotheincreaseinenergydemandfromdatacenters,driven
to evaluate the wide-area reliability impact of load-induced
by a global race for dominance in artificial intelligence (AI).
low-frequencyoscillations.Toaddressthisgap,thispaperpro-
Forecasts estimate that data center energy usage may grow
poses a simulation-based, readily automatable risk-evaluation
from ∼4.4% of the total US electricity consumption in 2023
methodology that quantifies the impact of FOs as a function
to∼12%by2028[1].Gridoperatorsworldwidearegrappling
of their frequencies and source location. Oscillation impact
with large load (LL) interconnection requests and the unique
is quantified by several metrics like the spatial spread of
operationalrisksposedbythedynamicbehavioroftheseloads.
FOs, risk of modal resonance, and the severity of oscillation
Hyperscale data centers can consume hundreds of MW at a
amplification. Using the proposed framework, high-risk LL
single load site, with GW-scale plants also being planned [2].
interconnection points and critical oscillation frequencies are
Their power demand can be cyclic, characterized by periodic
identified in the reduced 240-bus model of the Western Elec-
consumptionburstsandcool-downperiods.Traditionally,grid
tricity Coordinating Council (WECC) system [7]. Simulations
planning has not accounted for risks posed by the widespread
verify that the degree of oscillation amplification observed is
deployment of such hyperscalers. Thus, unexpected LL be-
directly correlated with modal observability at the source.
havior can threaten reliability by introducing or exacerbating
The remaining paper is organized as follows. Section II de-
grid disturbances [3]. The North American Electric Relia-
scribes how generic load models can be used to simulate FOs
bility Corporation (NERC) Large Load Task Force recently
in positive sequence studies. The proposed risk assessment
published a white paper outlining key reliability concerns
methodology is presented in Section III and used to study
posed by emerging LLs like AI-training facilities [4]. The
the impact of LL-induced oscillations on the 240-bus WECC
paper identifies several high-priority risks, including forced
model in Section IV. Section V discusses findings, outlines
oscillations (FOs) driven by periodic AI workloads.
future research directions, and concludes this paper.
Powersystemoscillationsmaybenaturalorforced.Natural
oscillations occur when system modes are excited by tran- II. MODELINGDATACENTERBEHAVIOR
sient disturbances or random load fluctuations, while FOs are
The major load components in a typical data center include
driven by periodic external disturbances. They persist in the
(a) servers, (b) cooling load for removing heat dissipated in
system as long as the external forcing function is present and
server racks, and (c) auxiliary load like lighting. Data centers
are equipped with uninterruptible power supplies (UPS) to
ThePacificNorthwestNationalLaboratory(PNNL)isoperatedbyBattelle
fortheDOEunderContractDOE-AC05-76RL01830. protect voltage-sensitive equipment and may also have back-
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
92226511.6202.22084DT/9011.01
:IOD
|
EEEI
6202©
00.13$/62/6-9655-5133-8-979
|
)D&T(
noitisopxE
dna
ecnerefnoC
noitubirtsiD
dna
noissimsnarT
SEP/EEEI
6202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:16 UTC from IEEE Xplore. Restrictions apply.

TABLEI
LOADCOMPOSITIONINTHECMLDMODELUSEDTOREPRESENTDATACENTERDYNAMICS
CMLD DataCenter
Description TypicalParameterSetting
Component Component
MotorA 3ϕmotorswithconstanttorquecompressors CoolingLoad FMA=0.09
MotorB 3ϕmotorswithvariabletorquecompressors(fans) N/A FMB=0
MotorC 3ϕmotorswithvariabletorquecompressors(pumps) N/A FMC=0
MotorD 1ϕmotorload N/A FMD=0
ElectronicLoad Powerelectronicloads Serverload&CRAH FEL=0.89,PFEL=1
StaticLoad GenericZIPload Miscellaneousload PFs=1,P1e=0,P2e=0,P1c=1,P2c=0
example, in the Python API for Siemens PTI PSS/E v35, the
load change 6() command can be used.
2) CompositeLoadModel(CMLD): CMLDmodelsconsist
of several motor, electronic, and static load components.
NERC recently conducted an industry-wide survey with de-
velopers and vendors to understand load composition within
Fig.1. Cyclicpowerconsumptionpatternsoflargecomputationalloads a data center [16]. Based on the findings, the CMLD com-
up generation. Several high-fidelity device-level data center position in Table I is recommended for modeling typical data
models have been developed [8], [9], but these are not well- center dynamics. Once the appropriate CMLD parameters are
suited for interconnection-scale planning studies where net- configured, periodic load fluctuations can be simulated using
works with thousands of buses need to be modeled. Current the same approach as the ZIP model.
industry practice represents data center power consumption
III. METHODOLOGY
with standard PQ or voltage-dependent loads that do not cap-
ture behavior like load ramps and delayed reconnection after Sustained FOs pose reliability risks ranging from operator
grid disturbances. Ongoing modeling efforts are attempting to confusiontorelaymisoperations.TheriskishigherwhenFOs
integrate these data center-specific features, but these models propagate to wide areas instead of having a localized impact.
are not yet available in commercial simulation engines [10], Thewide-areaspreadislikelywhentheFOfrequencyisinthe
[11]. Thus, system-level planning studies must still rely on electromechanical range (0.1−1 Hz) and the source exhibits
generic load models like ZIP (constant impedance, current, high participation in natural modes [5]. Resonance-driven
power)andcompositeloadmodel(CMLD)[12].Heedingthis amplification may occur if the source LL is sited close to a
constraint, this work utilizes generic load models to emulate generator with high modal participation, and its consumption
the LL cyclic consumption pattern, as elaborated next. periodicity matches the frequency of that mode. This work
formulates a simulation-based methodology to express the
A. Cyclic Consumption Pattern
reliability risk from LL-induced FOs in the electromechanical
Data center power consumption can be irregular, dictated
range as a function of FO frequency and load location. The
by the computational workload. In AI-training facilities, syn-
proposedmethodcanbeintegratedwithtransmissionplanning
chronized(de)activationoflargearraysofgraphicalandtensor
workflows and is summarized in Algorithm 1.
processing units creates a cyclic demand pattern character-
Considerthataplannerwishestoassesstheimpactofload-
ized by quick bursts of consumption followed by cool-down
induced FOs at different frequencies from locations in their
periods. The demand swings may be as high as from 10%
territory where interconnection requests are expected. Two
to 100% of full load [13]. AI-training load cycles may also
typesofimpactsaretobecaptured:(a)amplificationofpower
be bi-periodic. Slower variations (0.1–1 Hz) reflect rest-to-
swingswithintheplanner’sfootprint,and(b)oscillationspread
compute transitions, and faster fluctuations (5–30 Hz) within
beyond their area. It is cumbersome to record all output vari-
compute phases occur due to rapid switching of individual
ables in interconnection-scale simulations. Hence, to quantify
modules [13]. These load consumption patterns have been
theimpactoutsidetheplanningarea,oscillationamplitudesfor
illustrated in Fig. 1. Oscillations can also originate from
only major tie-lines and generators can be checked. Planners
auxiliary equipment. FOs at cryptocurrency mining facilities
may choose to examine all elements within their area or use
caused by communication and firmware failures have been
a generation capacity or voltage-based screening criteria (e.g.,
reported [4]. In a data center within Dominion Energy’s
inspect all transmission lines with voltages higher than 230
footprint, power consumption bursts every second were found
kV). Model accuracy is critical for accurate risk assessment.
toexcitea14.7-HzmodecausedbyUPScontrolsettings[14].
Assessment using multiple planning cases representative of
B. Simulating FOs with Generic Load Models different seasonal loading conditions and contingencies can
1) ZIP Model: ZIP models comprise a combination of help provide a comprehensive picture of grid vulnerability.
constant impedance, current, and power components [15]. The candidate set of frequencies may comprise ranges
FOs can be simulated by periodically scaling load values specified by data center developers if available, or some
during dynamic simulation. Popular positive sequence simu- frequencies in the electromechanical range can be selected. If
lators offer commands to automate such implementations. For poorly damped system modes are observable in the territory,
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:16 UTC from IEEE Xplore. Restrictions apply.

| Algorithm | 1   | Reliability | Impact | Assessment |     | Methodology |     |     |     |     |     |     |     |     |     |
| --------- | --- | ----------- | ------ | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLEII
Define base power flow and dynamic models DOMINANTMODESINTHE240-BUSWECCMODEL
1:
2: location list← list of candidate LL locations Frequency(Hz) 0.38 1 0.75 1.3
f list← list of candidate oscillation frequencies DampingRatio(%) 18 7.5 7.5 5.3
3:
| 4: tie    | lines←   | list        | of tie-lines | connecting |       | areas     |           |     |     |     |     |     |     |     |     |
| --------- | -------- | ----------- | ------------ | ---------- | ----- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5: source | list     | ←           | list of      | buses and  | lines | to be     | inspected |     |     |     |     |     |     |     |     |
| within    | source   | area        |              |            |       |           |           |     |     |     |     |     |     |     |     |
| 6: A←100  |          | MW, step←20 |              | MW         |       |           |           |     |     |     |     |     |     |     |     |
| 7: for    | location | in          | location     | list do    |       |           |           |     |     |     |     |     |     |     |     |
| 8:        | Add a    | LL model    | at           | location   | bus   |           |           |     |     |     |     |     |     |     |     |
| 9:        | for f    | in f list   | do           |            |       |           |           |     |     |     |     |     |     |     |     |
|           | Simulate |             | FO with      | frequency  | f and | amplitude | A         |     |     |     |     |     |     |     |     |
10:
| 11: | Compute |            | amplification | factor     | for | all elements |     | in  |     |     |     |     |     |     |     |
| --- | ------- | ---------- | ------------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tie | lines   | and source |               | list using | (1) |              |     |     |     |     |     |     |     |     |     |
>
| 12: | for | elements  | where          | amplification |               | threshold | do  |        |                                                  |     |     |     |     |     |     |
| --- | --- | --------- | -------------- | ------------- | ------------- | --------- | --- | ------ | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| 13: |     | Configure | protection     |               | settings      |           |     |        |                                                  |     |     |     |     |     |     |
|     |     |           |                |               |               |           |     | Fig.2. | Largeloadlocationsmodeledinthe240-bustestsystem. |     |     |     |     |     |     |
|     |     | while     | Any protection |               | not activated | do        |     |        |                                                  |     |     |     |     |     |     |
14:
|     |     |            |            |     |         |           |     | voltage,       | and zone | 3 distance      |     | protection. |                | Existing | remedial |
| --- | --- | ---------- | ---------- | --- | ------- | --------- | --- | -------------- | -------- | --------------- | --- | ----------- | -------------- | -------- | -------- |
| 15: |     | A←(A+step) |            |     |         |           |     |                |          |                 |     |             |                |          |          |
|     |     |            |            |     |         |           |     | action schemes |          | and out-of-step |     | relays      | for generators |          | can also |
| 16: |     | Rerun      | simulation |     | with FO | amplitude | A   |                |          |                 |     |             |                |          |          |
end while be represented. Once the protection elements are configured,
17:
oscillationswithincreasingamplitudesmaybesimulateduntil
| 18: | end     | for |     |     |     |     |     |          |                |     |             |          |     |          |          |
| --- | ------- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ----------- | -------- | --- | -------- | -------- |
|     |         |     |     |     |     |     |     | at least | one protection |     | is engaged, | yielding |     | an upper | limit on |
|     | end for |     |     |     |     |     |     |          |                |     |             |          |     |          |          |
19:
|     |     |     |     |     |     |     |     | permissible | oscillation |     | amplitudes. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----------- | --- | --- | --- | --- |
20: end for
IV. RESULTS
|           |             |     |        |              |     |      |           | This | section | describes | findings | from | applying | the | proposed |
| --------- | ----------- | --- | ------ | ------------ | --- | ---- | --------- | ---- | ------- | --------- | -------- | ---- | -------- | --- | -------- |
| then such | frequencies |     | should | be included. | For | each | candidate |      |         |           |          |      |          |     |          |
location and oscillation frequency, FOs can be simulated per risk assessment framework to the 240-bus WECC model [7].
the process described in Section II-B. The next step is to All simulations were performed using PSS/E, and the work-
calculate the amplification factor i.e. the maximum power flow was automated using the Python API.
| swing         | observed | at     | a location | relative | to       | the source. | The |             |        |             |      |       |           |     |           |
| ------------- | -------- | ------ | ---------- | -------- | -------- | ----------- | --- | ----------- | ------ | ----------- | ---- | ----- | --------- | --- | --------- |
|               |          |        |            |          |          |             |     | A. Test     | System | Description |      |       |           |     |           |
| amplification |          | factor | A i for    | element  | i may be | calculated  | as: |             |        |             |      |       |           |     |           |
|               |          |        |            |          |          |             |     | The 240-bus |        | reduced     | WECC | model | comprises |     | about 140 |
Pmax−Pmin GW of generation with a realistic fuel-mix. Due to the ag-
|     |     | A   | =   | i   | i   |     | (1) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i gregation of generators, detailed generator interactions cannot
|        |       |        | Pmax   | −Pmin         |        |     |           |             |     |             |               |     |            |      |           |
| ------ | ----- | ------ | ------ | ------------- | ------ | --- | --------- | ----------- | --- | ----------- | ------------- | --- | ---------- | ---- | --------- |
|        |       |        | source |               | source |     |           |             |     |             |               |     |            |      |           |
|        |       |        |        |               |        |     |           | be observed | in  | this model. | Additionally, |     | inferences |      | from this |
| As the | power | system | can    | be linearized | around | an  | operating |             |     |             |               |     |            |      |           |
|        |       |        |        |               |        |     |           | model may   | not | directly    | translate     | to  | the full   | WECC | system.   |
point,thepowerswingamplitudeobservedatalocationscales
|     |     |     |     |     |     |     |     | Nevertheless, | because |     | the model | is  | publicly | available, | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | --- | --------- | --- | -------- | ---------- | --- |
linearlywiththesourceoscillationamplitude.Asstepchanges
|     |     |     |     |     |     |     |     | dissemination | of  | observations |     | and their | implications |     | is easy. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | --------- | ------------ | --- | -------- |
likethoseobservedduringAItrainingcyclesmayexcitemulti-
|                |              |              |           |             |                   |                   |             | As the          | oscillation   | excitation     |             | risk   | is correlated |           | with the      |
| -------------- | ------------ | ------------ | --------- | ----------- | ----------------- | ----------------- | ----------- | --------------- | ------------- | -------------- | ----------- | ------ | ------------- | --------- | ------------- |
| ple system     | modes,       | the          | observed  | outputs     | are               | a superimposition |             |                 |               |                |             |        |               |           |               |
|                |              |              |           |             |                   |                   |             | properties      | of the        | system’s       | natural     | modes, |               | the modes | of the        |
| of different   | frequencies. |              | Computing |             | the amplification |                   | factor      |                 |               |                |             |        |               |           |               |
|                |              |              |           |             |                   |                   |             | 240-bus         | system        | were estimated |             | using  | the procedure |           | outlined      |
| as described   | in           | (1) is       | simple    | and avoids  | the               | signal            | processing  |                 |               |                |             |        |               |           |               |
|                |              |              |           |             |                   |                   |             | in [17].        | The estimated |                | frequencies | and    | damping       |           | ratios of the |
| steps required |              | to isolate   | specific  | frequencies |                   | from the          | output.     |                 |               |                |             |        |               |           |               |
|                |              |              |           |             |                   |                   |             | observed        | dominant      | modes          | are         | listed | in Table      | II.       |               |
| Amplification  |              | factors      | may       | be used     | to rank-order     |                   | grid el-    |                 |               |                |             |        |               |           |               |
|                |              |              |           |             |                   |                   |             | B. Observations |               |                |             |        |               |           |               |
| ements         | for further  | examination. |           | From        | a wide-area       |                   | reliability |                 |               |                |             |        |               |           |               |
perspective,powerswingsabove20MWconcernsystemoper- Thirteen locations across the system were selected as po-
atorsandmaybechosenasathreshold.Thereliabilityimpact tential LL sites, as shown in Fig. 2. LLs were represented
ofload-inducedFOsmaybequantifiedusingseveralmeasures, by the ZIP model. Three types of load perturbations were
such as, maximum amplification observed inside/outside the simulated for each site - (i) 0.5 Hz square wave, (ii) 1 Hz
source area (a measure of amplification severity), number of square wave, and (iii) bi-periodic load pattern with the slow
grid elements whose amplification factor is above a threshold and fast frequencies as 0.1 and 1 Hz, respectively. Maximum
(a measure of spatial propagation), or a combination thereof. FO amplification observed for each site is summarized in Fig.
Planners may also want to determine amplitude limits be- 3. Fig. 4 offers a closer look at the impact of FOs injected
yond which protection activation is likely. Configuring relays fromtheHALLENlocationinNevada-onlyelementswhere
|     |     |     |     |     |     |     |     | A >0.2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
for all buses and lines in interconnection-scale models is very i are plotted. Itcan beseen thatthe FOspatial spread
laborious, and hence we propose setting protection elements is wider at lower frequencies.
only where A is higher than a threshold. Modeled protec- Fig.3offersseveralinsights.First,oscillationamplification,
i
tion functions could include under/over frequency, under/over and hence the reliability risk is higher for 1-Hz oscillations
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:16 UTC from IEEE Xplore.  Restrictions apply.

Fig.3. MaximumamplificationobservedinsideandoutsidesourcezonewhenFOsareinjectedfromLLsatdifferentWECClocations
Fig.4. Gridelementswhereoscillationshigherthan20MWarerecordedwhen100MWloadperturbationsareintroducedfromtheHALLENbus
| than 0.5-Hz   | ones.         | This        | is expected | as          | a dominant   |                | mode          | exists       |                          |         |                |                    |           |
| ------------- | ------------- | ----------- | ----------- | ----------- | ------------ | -------------- | ------------- | ------------ | ------------------------ | ------- | -------------- | ------------------ | --------- |
| at 1 Hz.      | Further,      | the         | 1-Hz FO     | has         | the highest  |                | amplification |              |                          |         |                |                    |           |
| when injected | from          | locations   |             | in the      | Southwest.   | This           | suggests      |              |                          |         |                |                    |           |
| that if       | LLs in        | this region | were        | to          | oscillate    | at             | 1 Hz,         | they         |                          |         |                |                    |           |
| could pose    | a significant |             | risk        | to grid     | reliability, |                | necessitating |              |                          |         |                |                    |           |
| mitigation    | measures.     |             | Fig. 3      | also shows  |              | that the       | oscillation   |              |                          |         |                |                    |           |
| amplification | risk          | increases   | in          | the (0.1,1) |              | Hz bi-periodic |               | per-         |                          |         |                |                    |           |
| turbation     | case,         | possibly    | because     | additional  |              | locations      |               | in the       |                          |         |                |                    |           |
|               |               |             |             |             |              |                |               | Fig. 5. 1-Hz | mode shape plot.         | Circles | mark generator | locations.         | Radii are |
|               |               |             |             |             |              |                |               | proportional | to mode shape magnitudes |         | (measure       | of observability). | Arrows    |
hydro-richPacificNorthwestshowhighexcitabilityat0.1Hz.
showmodeshapeangles.Generatorswithsimilaranglesswingtogether.
| 1) 1              | Hz Mode:       | Fig.        | 3 shows    | that         | resonance-driven |                |            | am-  |     |     |     |     |     |
| ----------------- | -------------- | ----------- | ---------- | ------------ | ---------------- | -------------- | ---------- | ---- | --- | --- | --- | --- | --- |
| plification       | occurs         | when        | 1-Hz       | oscillations |                  | are simulated  |            | from |     |     |     |     |     |
| LLs in            | the Southwest. |             | To         | explain      | this             | phenomenon,    |            | the  |     |     |     |     |     |
| corresponding     |                | mode shape  | plot       | may          | be               | inspected      | (Fig.      | 5).  |     |     |     |     |     |
| As seen           | from the       | figure,     | the 1-Hz   | mode         | is               | observable     | mainly     |      |     |     |     |     |     |
| in the Southwest, |                | with        | generators | in           | Nevada           | swinging       | against    |      |     |     |     |     |     |
| those in          | Southern       | California, |            | Arizona,     | and              | New            | Mexico.    | The  |     |     |     |     |     |
| mode shape        | magnitude,     |             | a measure  |              | of mode          | observability, |            | is   |     |     |     |     |     |
| highest           | in the         | H ALLEN     | bus,       | and          | amplification    |                | is highest |      |     |     |     |     |     |
| when a            | FO is injected |             | from this  | location.    |                  | The power      | swings     |      |     |     |     |     |     |
atdifferentgeneratorsinresponsetoa1-Hzperturbationfrom
| H ALLEN | is  | presented | in Fig. | 6.  | A linear | relationship |     | is  |     |     |     |     |     |
| ------- | --- | --------- | ------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
observedbetweentheFOsource’smodeshapemagnitudeand
|     |     |     |     |     |     |     |     | Fig. 6. Oscillations | observed | in generator | power | outputs when | 1 Hz, 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | -------- | ------------ | ----- | ------------ | --------- |
observed maximum amplification for oscillations injected at MWloadperturbationsareintroducedfromtheHALLENbus.Meanvalues
modal frequency, as shown in Fig. 7. This is a useful insight, subtractedforeasyvisualization.
becausetransmissionplannerscanusemodeshapemagnitudes
|     |     |     |     |     |     |     |     | South (N-S) | mode, is | the most | geographically | widespread. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | -------------- | ----------- | --- |
as an initial screening criterion for identifying risky load Hence, to simulate a particularly concerning resonance case,
| cycling | frequencies | when | data | center | interconnection |     | requests |          |                   |          |     |           |           |
| ------- | ----------- | ---- | ---- | ------ | --------------- | --- | -------- | -------- | ----------------- | -------- | --- | --------- | --------- |
|         |             |      |      |        |                 |     |          | a 100-MW | load perturbation | matching |     | this mode | frequency |
are received at a location. was introduced from a LL placed at the CANADA bus in the
2) FOFrequenciesNearSystemModes: The0.38-Hzmode BritishColumbia(BC)zone.TheCANADAbuswasobserved
in the 240-bus model, representative of the WECC North- to have a high mode shape magnitude for the N-S mode. Sys-
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:16 UTC from IEEE Xplore.  Restrictions apply.

Fig.7. Max.oscillationamplificationvs.modeshapemagnitudeofsource
TABLEIII
OSCILLATIONVIOLATIONS(>20MW)FOR100MWLOADPERTUB.
HALLENat1Hz CANADAat0.38Hz Fig.8. Gridelementswhere>20MWoscillationsareobservedwhen0.38
Category
P-Gen P-Flow P-Gen P-Flow Hz,100MWloadperturbationsareintroducedfromtheCANADAbus
| #Inst.>20MW |     |     | 11  | 8   | 8   |     | 13  |           |      |          |     |           |     |        |         |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------- | --- | --------- | --- | ------ | ------- |
|             |     |     |     |     |     |     |     | The paper | also | outlines | how | to select | a   | subset | of grid |
#InstOutside
|     |     |     | 10  | 5   | 6   |     | 11  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SourceZone elements whose protection settings must be configured to
Max.p-pAmplitude determine oscillation amplitudes that do not trigger relays.
| inSourceZone(MW) |     | 280.93 |     | 122.83 | 149.06 | 161.58 |     |              |            |     |          |                |     |     |         |
| ---------------- | --- | ------ | --- | ------ | ------ | ------ | --- | ------------ | ---------- | --- | -------- | -------------- | --- | --- | ------- |
|                  |     |        |     |        |        |        |     | This greatly | simplifies |     | workflow | by eliminating |     | the | need to |
Max.p-pAmplitude
Outside 139.57 58.45 98.25 75.48 configureanddebugthousandsofelementsininterconnection-
SourceZone(MW) scale models while still capturing the impacts of LL-induced
| Max.AmplitudeLocn. |     |     |     | MEAD– | CANAD | NORTH– |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
HALLEN power swings. In future work, the authors aim to investigate
| inSourceZone |     |     |     | HALLEN | G1  | CANADA |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Max.AmplitudeLocn. MEAD– CMAIN MALIN– thepotentialoflow-frequencyoscillation-inducedrelaymisop-
CORONADO
OutsideSourceZone VICTORVYL GM MERIDIAN erations with realistic interconnection-scale models.
REFERENCES
| tem elements | where | appreciable |     | power | swings | are observed |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | ----------- | --- | ----- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
forthisscenarioareplottedinFig.8.Largeoscillationshigher [1] A.Shehabietal.,“2024UnitedStatesdatacenterenergyusagereport,”
LawrenceBerkeleyNationalLaboratory,Tech.Rep.,2024.
| than 100 | MW peak-to-peak |     | are | observed | on key | transmission |     |             |        |             |     |           |           |       |            |
| -------- | --------------- | --- | --- | -------- | ------ | ------------ | --- | ----------- | ------ | ----------- | --- | --------- | --------- | ----- | ---------- |
|          |                 |     |     |          |        |              |     | [2] T. Fist | and A. | Datta, “How | to  | build the | future of | AI in | the United |
linesintheNorthwestcorridorconnectingCanada,thePacific
States,”InstituteforProgress,Tech.Rep.,Oct.2024.
Northwest, and Northern California. Moreover, power swings [3] “Incident review - considering simultaneous voltage-sensitive load re-
ductions,”NERC,Tech.Rep.,Jan.2025.
| greater than | 20 MW | are    | observed | in   | generators      | as far | south |                                                                      |     |     |     |     |     |     |     |
| ------------ | ----- | ------ | -------- | ---- | --------------- | ------ | ----- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|              |       |        |          |      |                 |        |       | [4] “Characteristicsandrisksofemerginglargeloads:Largeloadstaskforce |     |     |     |     |     |     |     |
| as Arizona,  | even  | though | the N-S  | mode | is well-damped. |        |       |                                                                      |     |     |     |     |     |     |     |
whitepaper,”NERC,Tech.Rep.,Jul.2025.
TableIIIlistswherehighamplificationisobservedwhen1- [5] NERC Synchronized Measurements Working Group, “Recommended
Hzand0.38-HzFOsareintroducedfromLLsintheHALLEN oscillationanalysisformonitoringandmitigationreferencedocument,”
NERC,Tech.Rep.,Nov.2021.
and CANADA buses, respectively. The highest oscillation [6] K.Chatterjeeetal.,“Onlinemonitoringapplicationsenabledbyphasor
amplification observed for the 0.38 Hz case is lower, perhaps measurementunits:technicalassistancetothepowersectorsofSoutheast
attributable to the very high damping factor in the examined Asia,”PacificNorthwestNationalLaboratory(PNNL),Tech.Rep.,2023.
|     |     |     |     |     |     |     |     | [7] H. Yuan, | R.  | S. Biswas, | J. Tan, | and Y. Zhang, | “Developing |     | a reduced |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ------- | ------------- | ----------- | --- | --------- |
case. Despite this, large power swings are observed in fewer 240-bus WECC dynamic model for frequency response study of high
elementsforthe1-Hzcasecomparedtothe0.38-Hzcase,due renewableintegration,”inIEEEPEST&D,2020,pp.1–5.
|              |              |     |               |     |        |           |     | [8] M. Dayarathna |     | et al., “Data | center | energy | consumption | modeling: | A   |
| ------------ | ------------ | --- | ------------- | --- | ------ | --------- | --- | ----------------- | --- | ------------- | ------ | ------ | ----------- | --------- | --- |
| to the wider | geographical |     | observability |     | of the | N-S mode. |     |                   |     |               |        |        |             |           |     |
survey,”IEEECommun.Surv.Tutor.,vol.18,no.1,pp.732–794,2016.
|     |     |     |     |     |     |     |     | [9] S. Nekkalapu |     | et al., “Synthesis |     | of load and | feeder | models | using point |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------ | --- | ----------- | ------ | ------ | ----------- |
V. CONCLUSION onwavemeasurementdata,”IEEEOpenAccessJournalofPowerand
Energy,vol.8,pp.198–210,2021.
| This | paper presents |     | a simulation-based |     | methodology |     |     | to                                                                   |     |     |     |     |     |     |     |
| ---- | -------------- | --- | ------------------ | --- | ----------- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|      |                |     |                    |     |             |     |     | [10] A.Jimenez-RuizandF.Milano,“Datacentermodelfortransientstability |     |     |     |     |     |     |     |
automate the assessment of risks from LL-induced forced analysisofpowersystems,”arXivpreprintarXiv:2505.16575,2025.
|     |     |     |     |     |     |     |     | [11] K.Sreenivasacharetal,“Datacenterloadmodeling-modelvalidation,” |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
oscillations.Theframeworkstreamlinestheprocessforscreen-
NERCLoadModelingWorkingGroupPresentation,2024.
| ing potential | LL  | interconnection |     | points | to identify | high-risk |     |                   |     |            |            |      |       |             |        |
| ------------- | --- | --------------- | --- | ------ | ----------- | --------- | --- | ----------------- | --- | ---------- | ---------- | ---- | ----- | ----------- | ------ |
|               |     |                 |     |        |             |           |     | [12] “Reliability |     | guideline: | Developing | load | model | composition | data,” |
locationswhereFO–naturalmoderesonanceandthewide-area NERC,Tech.Rep.,Mar.2017.
propagation/amplificationofinducedoscillationsareprobable. [13] Tesla,“Batterystorageapplicationsatdatacenters,”Apr.2025,NERC
LargeLoadsTaskForcePresentation.
The proposed approach is used to evaluate the reliability [14] C. Mishra, L. Vanfretti, J. Delaree Jr, T. Purcell, and K. D. Jones,
impact of LL-induced oscillations over a range of frequencies “Understanding the inception of 14.7 hz oscillations emerging from a
from 13 points in the 240-bus WECC model. Insights from datacenter,”SustainableEnergy,GridsandNetworks,p.101735,2025.
|     |     |     |     |     |     |     |     | [15] S. M. | H. Rizvi, | S. K. Sadanandan, |     | and | A. K. Srivastava, |     | “Real-time |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----------------- | --- | --- | ----------------- | --- | ---------- |
this study can help transmission planners initiate detailed parameter tracking of power-electronics interfaced composite ZIP load
studies or recommend oscillation mitigation measures for model,”IEEETrans.SmartGrid,vol.13,no.5,pp.3891–3902,2021.
|           |                 |        |            |             |     |             |     | [16] NERC   | Load | Modeling   |                 | Working | Group,          | “Data | Center     |
| --------- | --------------- | ------ | ---------- | ----------- | --- | ----------- | --- | ----------- | ---- | ---------- | --------------- | ------- | --------------- | ----- | ---------- |
| high-risk | interconnection |        | locations. | The         | LL  | operators   | can |             |      |            |                 |         |                 |       |            |
|           |                 |        |            |             |     |             |     | Information |      | Collection | Questionnaire,” |         | 2025, [Online]. |       | Available: |
| also be   | educated        | on the | wide-area  | reliability |     | risks posed | by  |             |      |            |                 |         |                 |       |            |
https://www.nerc.com/comm/RSTC/LMWG/Data
loadvariationsatcertainfrequencies,promptingsoftware-side [17] D. J. Trudnowski et al., “Characterizing the oscillatory properties of
bulkelectricsystems,”IEEEAccess,vol.13,pp.32883–32900,2025.
| mitigation | measures | where | possible. |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | -------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:16 UTC from IEEE Xplore.  Restrictions apply.