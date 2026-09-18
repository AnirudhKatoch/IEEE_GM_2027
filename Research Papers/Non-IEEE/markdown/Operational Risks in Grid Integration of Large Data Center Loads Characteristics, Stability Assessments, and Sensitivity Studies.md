1
Operational Risks in Grid Integration of Large Data
Center Loads: Characteristics, Stability
Assessments, and Sensitivity Studies
Kyung-Bin Kwon∗, Sayak Mukherjee∗, Veronica Adetola
Abstract—This paper investigates the dynamic interactions the North American Electric Reliability Corporation (NERC)
betweenlarge-scaledatacentersandthepowergrid,focusingon Large Load Task Force recently highlighted critical reliability
reliabilitychallengesarisingfromsuddenfluctuationsindemand.
challenges from emerging LDDLs like AI training facilities
WiththerapidgrowthofAI-drivenworkloads,suchfluctuations,
[7].
alongwithfastramppatterns,areexpectedtoexacerbatestressed
grid conditions and system instabilities. We consider a few Modelingofdatacenterloadshasalsobeenafocusofrecent
open-source AI data center consumption profiles from the MIT research works. A substantial body of literature examines the
supercloud datasets, along with generating a few experimental long-term dynamics of data centers, with a primary focus
HPC job-distribution-based inference profiles. Subsequently, we
on heat transfer and thermodynamic aspects [8], [9]. Such
developanalyticalmethodologiesforreal-timeassessmentofgrid
research emphasizes the internal operation of LDDLs rather
stability, focusing on both transient and small-signal stability
assessments.Energy-flow-likemetricsfornonlineartransientsta- than their dynamic interactions with the power grid. [10]
bility,formulatedbycomputinglocalizeddatacenterbuskinetic- introduces a dynamic load model for voltage and reactive
like flows and coupling interactions with neighboring buses over powercontroltailoredtodatacenters,while[11],[12]analyze
varying time windows, help provide operators with real-time
data center behavior from the converter dynamics point of
assessmentsoftheregionalgridstressinthedatacenterhubs.On
view. [13] presents a dynamic load model for transient sta-
the other hand, small-signal stability metrics, constructed from
analyticalstatematricesundervariableoperatingconditionsdur- bility assessments. While transient stability analysis has been
ing a fast ramping period, enable snapshot-based assessments of well-established in power systems literature [14]–[17], these
datacenterloadfluctuationsandprovideenhancedobservability methods primarily address conventional load and generation
intoevolvinggridconditions.Byquantifyingthestabilityimpacts
patterns.TheuniquerapidloadtransitionscharacteristicofAI
of large data center clusters, studies conducted in the modified
data centers present fundamentally different transient stabil-
IEEE benchmark 68−bus model support improved operator
situational awareness to capture risks in reliable integration of ity challenges that remain largely underexplored in existing
large data center loads. research. These rapid and substantial load variations can
also trigger inappropriate responses from local controllers of
Keywords: AI Data Centers, Grid Integration, Large Dy-
inverter-based resources and other generation assets, poten-
namic Digital Loads, Stability Studies with Data Centers,
tiallyleadingtolarge-scalesysteminstabilities.Arecentstudy
Real-time Situational Awareness.
led by Dominion Energy documented a real-world case of
such oscillatory behavior driven by data center loads [18].
I. INTRODUCTION
[19] presents the risks of forced oscillations in the Western
AI data centers are rapidly becoming major electricity
US power grid in the presence of cyclical load consumption
consumers,withU.S.datacenterscomprising4.4%ofnational
patterns of data centers. In addition, [20] develops a dynamic
electricity use in 2023 and projected to reach 9 − 12% by
power profiling approach for AI-centric loads and analyzes
2030 [1], [2]. This sharp growth, driven by the adoption of
their potential to induce wide-area grid oscillations. The Ac-
generative AI like large language models (LLMs) [3]–[5],
curate modeling of behaviors like Fault-Ride-Through (FRT)
introduces frequent energy fluctuations. Classified as large
[13] is also essential for developing mitigation strategies,
dynamic digital loads (LDDLs), their massive demand and
such as storage-based smoothing [21] and workload shifting.
sudden load swings pose serious challenges to grid stability
The high-frequency power fluctuations from AI workloads
and reliability, thus risking national energy security. LDDL
are distinct from conventional demand, requiring advanced
characteristics stem from server rack operations like training
methods to assess their grid impact.
and inference [6], creating sharp load ramps. These ramps
A significant gap persists in creating a comprehensive
stressgridtransfercapabilities,leadingtocongestionandboth
framework for real-time grid stability assessment under LD-
transient and small-signal stability issues. Recognizing this,
DLs. Current research is often limited to isolated component
modeling or post-event analysis. A pressing need exists for
Authors are with the Pacific Northwest National Laboratory, Rich-
land, WA 99352, USA, Emails: {kyung-bin.kwon, sayak.mukherjee, veron- analytical methods to quantitatively evaluate stability in real-
ica.adetola}@pnnl.gov,∗ contributedequally. time, linking AI workload patterns to actionable reliability
The research is supported by the Energy and Environment Directorate’s metrics. Such a framework would enable system operators to
Laboratory Directed Research at Pacific Northwest National Laboratory
proactively manage grid security. This paper addresses this
(PNNL). PNNL is operated by Battelle for the U.S. Department of Energy
underContractDEAC05-76RL01830. void by proposing real-time assessment tools to characterize
5202
tcO
82
]YS.ssee[
3v73450.0152:viXra

2
and quantify the stability risks posed by LDDLs. parallelprocessing.Atypicalhigh-performanceAIserverinte-
Contributions:Thepaperaimstocharacterizevariousforms grates multiple GPUs interconnected through high-bandwidth
ofinteractionsbetweenthepowergridanddatacenters,driven links such as NVLink, for example, configurations with 8
by large, sudden fluctuations in demand. Its primary objective NVIDIA H100 GPUs provide massive throughput for training
istoquantitativelyassessreliabilityconcerns,suchasstressed and inference workloads. Each GPU is equipped with high-
grid conditions and system instabilities, that are likely to bandwidth memory (HBM), ensuring rapid data access to
become more significant with the growing integration of AI- match the compute intensity.
driven data centers. Thermal management is critical, as the dense integration of
• First, we consider generating critically stressed grid con- accelerators and CPUs generates significant heat. Advanced
ditionsbyintegratinglarge-scaledatacenterclusterswith cooling solutions, including optimized air-flow designs and
theIEEEBenchmark68-busmodelthatincorporatesboth liquid-coolingsystems,aredeployedtomaintainstableoperat-
power electronics-based and synchronous generation re- ingconditions.Thecomputenodearchitectureiscarefullybal-
sources. Realistic load fluctuations, reflecting AI training anced across GPUs, CPUs, memory, and storage subsystems
and inference workloads, have been simulated to stress to maximize data throughput and end-to-end performance. At
the system and trigger potential instability events. We scale, multiple servers are organized within racks, forming
provide a description of the grid integration modeling tightly coupled clusters capable of supporting demanding
and generation of high-performance computing-based AI AI workloads ranging from multi-trillion-parameter model
inference profiles, along with considering open source training to latency-sensitive inference tasks. This rack-level
data profiles such as MIT supercloud datasets [22]. organization characterizes modern AI data centers, enabling
• Subsequently, we focus on the development of the an- both efficiency and resilience at the system scale.
alytical methodologies that consider the development of
real-time assessment metrics, such as energy-flow-based
metrics for nonlinear transient stability. We formulate B. Available Open-Source LDDL Profiles
the energy flow-based methodology for the regional data
center hub by computing localized LDDL bus’ kinetic- The LDDL profiles utilized in this study are derived from
like energy flow, along with computing coupling flows the open-source MIT supercloud dataset [22], [23], which
with the neighbor buses. These metrics are computed captures real-world power consumption from a heterogeneous
over varying time windows and can provide essential computing cluster. This data includes the training and infer-
observability over current grid conditions. ence runs of various large language models (LLMs), whose
• Small-signal stability-based metrics have been developed workloads are known for highly variable power demands,
with snapshot-based assessments for capturing the im- featuring both abrupt fluctuations and gradual changes. Such
pacts of sharp ramp increases in the data center hubs. dynamic behavior makes these profiles excellent for assessing
Thesmall-signalmetricsutilizetheanalyticalstatematrix power system stability.
constructions over variable operating conditions during From this source, we curate three distinct operational sce-
the critical changes in the LDDL consumptions. The narios, depicted in Fig. 1, to model the behavior of three
assessment studies and methodologies help to enhance different LDDLs. Each dataset introduces unique disturbances
understanding of grid–data center interactions and sup- to the system:
port improvements in operational stability. By providing
• Dataset A [21]–[23] (Figs. 1(a)–1(c)): This dataset
operators with improved situational awareness, the find-
models short-term, high-intensity inference tasks. The
ings will enable stability-informed decisions for resource
profilesarecharacterizedbysharp,high-magnitudepower
dispatch, while also offering data center owners action-
events. LDDL 1 and LDDL 2 experience abrupt spikes
able recommendations to strengthen reliability.
reaching peaks significantly higher than the nominal
The rest of the paper is organized as follows. Section II steadycondition.LDDL3exhibitsasmallerstepincrease
describes the details on AI operations, availability of open with minor subsequent fluctuations.
source datasets, HPC job-scheduling based inference pattern • DatasetB[22](Figs.1(d)–1(f)):Thisscenariorepresents
generation and grid integration of the LDDLs. Subsequently, a transition to a sustained high-consumption phase, such
we present the real-time assessment methodologies based on as the start of a model training session. LDDL 1 and
both nonlinear transient and small-signal stability with high LDDL 2 show sharp step increases to noisy plateaus.
consumption of LDDLs and sharp ramps in Section III. The In contrast, LDDL 3 enters a state of persistent, high-
methods also accompany a detailed numerical simulation in frequency oscillations with a peak-to-peak amplitude of
that section. Concluding remarks are provided in Section IV. nearly 20%.
These diverse and realistic load profiles introduce substan-
II. LDDLCHARACTERISTICSANDINTEGRATION tial disturbances, providing a robust framework for assessing
theimpactofLDDLdemandfluctuationsonsystemdynamics.
A. AI Data Center Operations and Hardware
A consistent observation across all datasets is that LDDL 1
AI compute nodes rely on accelerator-centric architectures, and LDDL 2 tend to exhibit greater load volatility compared
where GPUs serve as the primary engines for large-scale to LDDL 3.

3
|     |     | (a) |     |     |     |     |     | (b) |     |     |     |     | (c) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig. 1: Load profiles for three LELs across three distinct operational datasets: (a) Dataset A, featuring abrupt power events
typicalofinferencetasks;(b)DatasetB,showingsustainedhighconsumptionandoscillations;and(c)DatasetC,characterized
| by gradual, | stair-like | load | increases |     | from scheduled |     | jobs. |     |     |     |     |     |     |     |
| ----------- | ---------- | ---- | --------- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
C. HPC Job Scheduling-based Experimental Inference Pro- D. Grid Integration of the LDDLs
files
|     |     |     |     |     |     |     |     |     | Data | center | units are | integrated | with the | grid via a set of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --------- | ---------- | -------- | ----------------- |
WeconsiderPoisson-likeHPCjobarrivalsfortheinference interconnection architectures, as depicted in Fig. 2. The data
tasks in an AI data center [24]–[27]. Let us consider the data center is integrated to the utility grid via one or more high to
center, where there are M servers per rack with N racks. medium-voltage feeders and step-down substation transform-
| P denotes |     | the idle | power | in kW | for each | of  | the servers, |     |                                                       |     |     |     |     |     |
| --------- | --- | -------- | ----- | ----- | -------- | --- | ------------ | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
| base      |     |          |       |       |          |     |              |     | ers.Subsequently,LDDLusesanuninterruptiblepowersupply |     |     |     |     |     |
and P denotes the kW/server at full load. Let the AI job (UPS) that acts as a buffer between the AI workloads and the
peak
arrival rate be η per second, and the average duration is γ grid. Mostly, the common architecture of the UPS is to use
seconds. Considering the time step of ∆t, the probability of a dual-conversion with rectifier and inverter, and the output
job arrival in the small interval of η∆t is computed, and then AC is fed to the data center’s dedicated power distribution
compared with a random number generator. Subsequently, if units (PDUs), which then provide the power to different
the AI workload has arrived, then the jobs are assigned to components within the LDDL, such as servers and cooling
the idle server, which will then consume the full load. The loads. Currently, the industry is considering utilizing grid-
duration of the job can follow a Gaussian distribution with interactive UPS technology that can incorporate grid-forming
| mean γ, | and standard |     | deviation | of  | γ seconds. | Therefore, |     | for |     |     |     |     |     |     |
| ------- | ------------ | --- | --------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
| the active | servers | we will | have | for | the i−th | GPU | unit in | the |     |     |     |     |     |     |
| ---------- | ------- | ------- | ---- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
j−th rack as, Algorithm 1: Data Center Inference Job Emulation
|     |       |     |     |      |             |     |     |     |     | Input: | T,dt,η,γ,M,N,P |     | ,P        | ,α ,α |
| --- | ----- | --- | --- | ---- | ----------- | --- | --- | --- | --- | ------ | -------------- | --- | --------- | ----- |
|     |       |     |     |      |             |     |     |     | 1:  |        |                |     | peak idle | 1 2   |
| P   | (t)=P | +P  |     | ,t=t | ,1,..,N(γ,γ |     | ),  | (1) |     |        |                |     |           |       |
GPUi,j idlei,j peaki,j init 1 2: Initialize: server_states←0, P cool ←0
|     | (cid:88) |     |     |     | (cid:88) |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P (t)= P (t), P (t)= P (t) (2) 3: Initialize arrays for results
| rackj   |        | GPUi,j      |         | AI    |              | rackj |             |     |     |                     |      |       |      |     |
| ------- | ------ | ----------- | ------- | ----- | ------------ | ----- | ----------- | --- | --- | ------------------- | ---- | ----- | ---- | --- |
|         |        |             |         |       |              |       |             |     |     | for step=0          | to T | −1 do |      |     |
|         | i      |             |         |       | j            |       |             |     | 4:  |                     |      |       |      |     |
|         |        |             |         |       |              |       |             |     | 5:  | t←step·dt           |      |       |      |     |
| Let us  | assume | the desired | cooling |       | power        | P     | is set to   | be  |     |                     |      |       |      |     |
|         |        |             |         |       |              | cool  |             |     |     | if η·dt>random(0,1) |      |       | then |     |
| the α P | , then | we can      | also    | write | the dynamics |       | for cooling |     | 6:  |                     |      |       |      |     |
1 AI
|     |     |     |     |     |     |     |     |     | 7:  | Find | idle servers |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | --- | --- |
power as:
|      |         |      |       |     |         |      |       |     | 8:  | if  | idle servers | exist | then           |             |
| ---- | ------- | ---- | ----- | --- | ------- | ---- | ----- | --- | --- | --- | ------------ | ----- | -------------- | ----------- |
|      |         |      |       |     |         |      |       |     |     |     | Assign job   | with  | duration N(γ,γ | ) to random |
| P    | (t+1)=P |      | (t)+α | (α  | P (t)−P |      | (t)), | (3) | 9:  |     |              |       |                | 1           |
| cool |         | cool |       | 2 1 | AI      | cool |       |     |     |     |              |       |                |             |
idle server
| where α | is the | coefficient | capturing |     | the speed | of  | the cooling |     | 10: | end | if  |     |     |     |
| ------- | ------ | ----------- | --------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
2
| response,  | and | α is the      | cooling | ratio | (e.g., | 0.15). | The | total |     |     |     |     |     |     |
| ---------- | --- | ------------- | ------- | ----- | ------ | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
|            |     | 1             |         |       |        |        |     |       | 11: | end | if  |     |     |     |
| LDDL power | is  | then computed |         | as:   |        |        |     |       | 12: | P   | ←0  |     |     |     |
AI
|     |     |     |     |     |     |     |     |     |     | for each | server | do  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | --- | --- |
13:
|     |     | P LDDL | (t)=P | AI (t)+P | cool | (t) |     | (4) |     |     |             |      |            |                |
| --- | --- | ------ | ----- | -------- | ---- | --- | --- | --- | --- | --- | ----------- | ---- | ---------- | -------------- |
|     |     |        |       |          |      |     |     |     | 14: | if  | running job | then |            |                |
|     |     |        |       |          |      |     |     |     | 15: |     | Add P       | to P | , decrease | job time by dt |
Alg. 1 shows the process of generating the inference profiles peak AI
| of AI data | centers | based | on  | HPC | job distribution |     | routines |     | 16: | else |     |     |     |     |
| ---------- | ------- | ----- | --- | --- | ---------------- | --- | -------- | --- | --- | ---- | --- | --- | --- | --- |
for inference tasks. This gives us another dataset for our grid 17: Add P to P
|                  |              |        |             |                |              |     |           |     |     |      | idle     | AI  |      |      |
| ---------------- | ------------ | ------ | ----------- | -------------- | ------------ | --- | --------- | --- | --- | ---- | -------- | --- | ---- | ---- |
|                  |              |        |             |                |              |     |           |     |     | end  | if       |     |      |      |
| reliability      | experiments. |        |             |                |              |     |           |     | 18: |      |          |     |      |      |
|                  |              |        |             |                |              |     |           |     | 19: | end  | for      |     |      |      |
| • Dataset        | C            | (Figs. | 1(g)–1(i)): |                | This dataset |     | simulates | a   |     |      |          |     |      |      |
|                  |              |        |             |                |              |     |           |     | 20: | P    | ←P ·N    |     |      |      |
| gradual,         | ramp-up      |        | in load,    | characteristic |              | of  | scheduled |     |     | AI   | AI       |     |      |      |
|                  |              |        |             |                |              |     |           |     |     | P    | ←P +α·(α |     | P −P | )    |
|                  |              |        |             |                |              |     |           |     | 21: | cool | cool     |     | 1 AI | cool |
| high-performance |              |        | computing   | (HPC)          | jobs.        | All | three     | LD- |     |      |          |     |      |      |
|                  |              |        |             |                |              |     |           |     | 22: | P    | ←P       | +P  |      |      |
DLs exhibit a stair-like increase, with their loads incre- LDDL AI cool
|          |     |           |       |             |     |            |         |     |     | end for |              |         |     |     |
| -------- | --- | --------- | ----- | ----------- | --- | ---------- | ------- | --- | --- | ------- | ------------ | ------- | --- | --- |
| mentally |     | rising to | their | peak values |     | from their | nominal |     | 23: |         |              |         |     |     |
|          |     |           |       |             |     |            |         |     | 24: | Output: | P AI ,P cool | ,P LDDL |     |     |
steady-state.

4
|     |     |     |     |     |     |     | are       | the droop      | gain        | and      | the time  | constant    | of            | the low-pass | filter     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | ----------- | -------- | --------- | ----------- | ------------- | ------------ | ---------- |
|     |     |     |     |     |     |     | in        | the inverter’s |             | power    | control   | loop,       | respectively. |              |            |
|     |     |     |     |     |     |     | In        | addition       | to          | this     | localized | component,  |               | we consider  | the        |
|     |     |     |     |     |     |     | potential |                | energy-like | quantity |           | dissipating |               | through      | the trans- |
|     |     |     |     |     |     |     | mission   | lines          | connected   |          | to the    | bus.        | This          | is captured  | by the     |
|     |     |     |     |     |     |     | coupling  |                | energy      | flow,    | Ec(t):    |             |               |              |            |
i
1
|     |     |     |     |     |     |     |     |     | Ec(t)= |     | (cid:88) |          |     | (t))2, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------- | -------- | --- | ------ | --- |
|     |     |     |     |     |     |     |     |     |        |     | b        | (θ (t)−θ |     |        | (6) |
|     |     |     |     |     |     |     |     |     | i      |     | 2        | ij i     | j   |        |     |
j∈Ni
|     |     |     |     |     |     |     | where     | N           | is the | set of          | buses | adjacent   | to     | bus i,           | and b is  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------ | --------------- | ----- | ---------- | ------ | ---------------- | --------- |
|     |     |     |     |     |     |     |           |             | i      |                 |       |            |        |                  | ij        |
|     |     |     |     |     |     |     | the       | susceptance |        | of the          | line  | connecting | buses  | i                | and j. By |
|     |     |     |     |     |     |     | combining |             | these  | two components, |       | we         | define | a representative |           |
Fig. 2: Grid integration overview of LDDL. energy-like function that captures the accumulated stress over
|     |     |     |     |     |     |     | a time | window |     | T =[t,t+∆t |     | ]:  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ---------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |        |        |     | t          |     | w   |     |     |     |
(cid:88)
operationstosupportthegrid,thatcanprovidestablevoltages E (t)= (E l(t′)+w·E c(t′)), (7)
|     |     |     |     |     |     |     |     |     | i   |     | i   |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andfrequencies,supportblackstartcapabilities,andenablein- t′∈Tt
tegratinglocalgenerationresourcessuchasPV,andintegrating where w is a weighting coefficient that balances the relative
advancedcoordinatedstoragetechnologies.Modelingtheload
|     |     |     |     |     |     |     | contributions |     | of  | the local | and | coupling | energy | terms. | We use |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --------- | --- | -------- | ------ | ------ | ------ |
characteristics of LDDL is also an active area of research, the nominal load consumption amount to scale the coupling
| with NERC’s | Large | Load | Taskforce | is  | discussing | different |     |     |     |     |     |     |     |     |     |
| ----------- | ----- | ---- | --------- | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
energy flow.
| modeling | approximations. |     | The dynamic | nature | of  | the LDDL |     |        |             |     |        |     |                |     |          |
| -------- | --------------- | --- | ----------- | ------ | --- | -------- | --- | ------ | ----------- | --- | ------ | --- | -------------- | --- | -------- |
|          |                 |     |             |        |     |          | The | energy | definitions |     | in (5) | and | (6), following |     | from the |
consumption has been described in the previous section; apart system stability theory, are always non-negative. For practical
| from servers | and | cooling, | the rest | of the | LDDL | components |     |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | -------- | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
indicatordesign,astheyquantifythemagnitudeofadeviation
canbeaggregatedasZIPloads.Inthisstudy,wefocusmainly but not its direction, we slightly modify these definitions to
onintegratingvariousdynamicpowerconsumptionpatternsin
|     |     |     |     |     |     |     | formulate |     | a directional |     | energy-like |     | function. | The | directional |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ----------- | --- | --------- | --- | ----------- |
P ,andthensubsequentlyconsideraninterfacingdroop-
| LDDL |     |     |     |     |     |     | local | energy-like |     | flow, | Eld(t), | is defined | as: |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | ----- | ------- | ---------- | --- | --- | --- |
i
| controlled | grid-forming | dynamics |     | mimicking | provision | for |     |     |     |     |     |     |     |     |     |
| ---------- | ------------ | -------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
storage, interactive UPS, and installation of local generation. Eld(t)= M ·|ω (t)−ω (t)|·(ω (t)−ω (t)),
|     |     |     |     |     |     |     |     | i   |     | eqi | i   | 0   | i   |     | 0 (8) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
2
| We also | model the | power | distribution | unit | with | a first-order |     |     |     |     |     |     |     |     |     |
| ------- | --------- | ----- | ------------ | ---- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
filter that interfaces between the UPS and AI servers. and similarly, the directional coupling energy-like flow from
|     |     |     |     |     |     |     | bus | i, Ecd(t), | is  | given | by: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
i
1 (cid:88)
III. ANALYTICSFORREAL-TIMESITUATIONAL Ecd(t)= b ·|θ (t)−θ (t)|·(θ (t)−θ (t)).
|     |                                  |     |     |     |     |     |     | i   |     | ij  | i   | j   | i   |     | j (9) |
| --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
|     | AWARENESSANDNUMERICALEXPERIMENTS |     |     |     |     |     |     |     | 2   |     |     |     |     |     |       |
j∈Ni
| A. Nonlinear | Transient | Behavior |     |     |     |     |         |        |            |            |       |             |        |     |              |
| ------------ | --------- | -------- | --- | --- | --- | --- | ------- | ------ | ---------- | ---------- | ----- | ----------- | ------ | --- | ------------ |
|              |           |          |     |     |     |     | Lastly, | we     | can define | the        | total | directional | energy |     | function for |
|              |           |          |     |     |     |     | a time  | window |            | T =[t,t+∆t |       | ] as        |        |     |              |
This section analyzes the nonlinear transient response of t w
the power system, specifically when LDDLs are subjected to (cid:88)
|     |     |     |     |     |     |     |     |     | Ed(t)= |     | (Eld(t′)+w·Ecd(t′)), |     |     |     | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------------- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     |     | i      |     | i                    |     | i   |     |      |
asuddenloadincrease.Toquantifytheimpactoftheseevents,
t′∈Tt
| we employ | an energy | function | framework. |     | This | approach, |     |     |     |     |     |     |     |     |     |
| --------- | --------- | -------- | ---------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
analogous to analyzing the kinetic energy of a conventional These directional metrics provide not only the magnitude
|             |            |          |     |            |        |           | of  | the energy | flow | but | also its | direction, |     | indicating | whether |
| ----------- | ---------- | -------- | --- | ---------- | ------ | --------- | --- | ---------- | ---- | --- | -------- | ---------- | --- | ---------- | ------- |
| synchronous | generator, | provides | an  | insightful | metric | for eval- |     |            |      |     |          |            |     |            |         |
uating the system’s response in the presence of dynamically energy is being absorbed by or injected into the bus and
|     |     |     |     |     |     |     | its | connecting | lines. | For | instance, | a   | positive | directional | local |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --------- | --- | -------- | ----------- | ----- |
responsiveelementslikeLDDLs.Byderivinganenergyfunc-
|     |     |     |     |     |     |     |     | (E  | ld(t) | > 0) |     | (ω  | (t)−ω | (t)) | > 0. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | ----- | ---- | ---- |
tionfortheGFMinverterwithinanLDDL’sgridinterface,we energy i signifies that i 0 This
canestablishaclearrelationshipbetweenloadfluctuationsand implies the inverter at bus i is operating at a frequency above
nominal,behavingasifitpossessesexcesskinetic-likeenergy
| the inverter’s | dynamic | behavior, | enabling |     | a detailed | analysis |     |     |     |     |     |     |     |     |     |
| -------------- | ------- | --------- | -------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
of transient phenomena. that it will tend to release back into the system. Conversely,
|           |              |          |               |     |        | l(t)   | a negative |       | value           | (E ld(t) | <      | 0) indicates | a      | frequency | deficit      |
| --------- | ------------ | -------- | ------------- | --- | ------ | ------ | ---------- | ----- | --------------- | -------- | ------ | ------------ | ------ | --------- | ------------ |
| For an    | LDDL at      | bus i∈L, | the localized |     | energy | flow E |            |       |                 | i        |        |              |        |           |              |
|           |              |          |               |     |        | i      | ((ω        | (t)−ω | (t))            | < 0),    | where  | the LDDL     |        | bus is    | in a deficit |
| at time t | is expressed | as:      |               |     |        |        |            | i     | 0               |          |        |              |        |           |              |
|           |              |          |               |     |        |        | phase      | of    | its oscillation |          | and is | absorbing    | energy | from      | the grid.    |
1
El(t)= (t))2, The interpretation of the coupling energy is analogous. A
|     |     | M   | eqi (ω i (t)−ω | 0   |     | (5) |          |      |     |               |     |     |         |               |     |
| --- | --- | --- | -------------- | --- | --- | --- | -------- | ---- | --- | ------------- | --- | --- | ------- | ------------- | --- |
|     | i   | 2   |                |     |     |     |          |      |     |               |     |     | Ecd(t), |               |     |
|     |     |     |                |     |     |     | positive | term | in  | the summation |     | for |         | corresponding | to  |
i
where M represents the equivalent inertia of the inverter’s θ > θ , indicates that bus i is pushing active power towards
|     | eqi |     |     |     |     |     | i   | j   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
control scheme (e.g., different forms of GFM control) and the neighboring bus j, while a negative term implies power
ω (t)isthenominalfrequency.Forthedroop-controlledGFM flow in the opposite direction.
0
inverters used in our interactive LDDL model, this equivalent To operationalize this comprehensive framework, we detail
mp,
inertia is calculated as: M eq =2H eq = where m p and τ the procedure for calculating all defined energy metrics from
τ

5
Algorithm 2: Energy Flow Based Analytics for Tran-
sient Stability Analysis
1: Input: Set of LDDL buses L, adjacency sets N i , line
susceptances b , equivalent inertias M .
ij eqi
2: Input: Weighting coefficient w, time window duration
∆t .
w
3: Input: Time-series data: ω i (t) and θ i (t) for t∈[0,T]
and relevant buses.
4: Initialize: Arrays for El(t), Ec(t), Eld(t), Ecd(t),
i i i i
E (t), and Ed(t).
i i
5: for t in time steps from 0 to T do
6: for each bus i∈L do
7: ∆ω i (t)←ω i (t)−ω 0 (t)
8: E i l(t)← 1 2 M eqi ∆ω i (t)2
9: E i ld(t)← 1 2 M eqi |∆ω i (t)|∆ω i (t)
10: Ec(t)←0; Ecd(t)←0
i i
11: for each neighbor j ∈N i do
12: ∆θ ij (t)←θ i (t)−θ j (t)
13: E i c(t)←E i c(t)+ 1 2 b ij (∆θ ij (t))2 Fig. 3: IEEE 68-bus system with an LDDL cluster.
14: E i cd(t)←E i cd(t)+ 2 1b ij |∆θ ij (t)|∆θ ij (t)
15: end for
T =[t−∆t ,t]
t w ity, as shown in Fig. 4. The system frequency exhibits large,
1 1 1 8 6 7 : : : if c E E u i i d r ( r ( t e t ) ) n ← t ← tim (cid:80) (cid:80) e t t t t ′ t ′ = = ≥ t t − − ∆ ∆ ∆ t t t w w w ( ( E E th i l i l ( e d t n ( ′ t ) ′) + + w w ·E ·E i c( i c t d ′ ( ) t ) ′)) e o c r o f r m a a t b l i l c in t fl e h d u re c r e t e u a a L c t D i t o iv D n e s L p s ( o F c w ig r e e . r a 4 t d e (a e ) m s ) i . g an n W d ifi h s c i ( l a e F n i t t g h . s e t 4 r a e (c c s ) s ti ) v ( f e F u i r p g t o h . w e 4 r e ( r a b m ) s ) p , p i l k t i h e fy e s
19: else system instability. This is reflected in the local directional
20: E i (t)←0; E i d(t)←0 energy flow (Fig. 4(d)), which shows significant fluctuations
21: end if between 10–12 seconds, corresponding to the primary peak
22: end for load period. The total directional energy flows (local and
23: end for coupling) in Fig. 4(e) confirm this transient stress. The bar
24: Output: El,Ec,Eld,Ecd,E,Ed. graphsinFig.4(f),whicharesnapshotsofthetotaldirectional
energyflow,revealcriticaldynamics:attimes,allthreeLDDLs
contributenegativelyinunison,magnifyingsysteminstability,
system measurement data. Algorithm 2 outlines the computa- while at other moments, their opposing positive and negative
tional steps for quantifying both instantaneous and accumu- flows create a partial cancellation effect.
lated transient stress on each LDDL bus. The outputs of this DatasetB:Thisscenariodemonstratesthesystem’sreaction
algorithm serve as the primary analytics for our numerical to sustained and oscillatory load changes (Fig. 1(d)-(f)). The
experiments. system initially enters a stressed steady-state with persistent
frequency fluctuations (Fig. 5(a)) driven by the oscillatory
B. Experiments with Transient Simulations load of LDDL 3. To investigate stability limits, we simulate
ToanalyzetheimpactofLDDLloadsonthepowersystem, a collapse scenario by amplifying the load fluctuations by
we design a test system based on the IEEE 68-bus system 1.6 times. As shown in Fig. 5(g), the system frequency
depicted in Fig. 3 [28] in phasor domain. The system is destabilizes and collapses after 12 seconds. This collapse is
modified with inverter and LDDL installations and consists markedbyadramaticsurgeinthetotaldirectionalenergyflow,
of 16 generators and 35 loads with local GFM-inverter-based with magnitudes reaching several orders of magnitude higher
generation/storage, with components in a 100 MVA base. than normal operating conditions (Fig. 5(h)). The snapshot in
Here, an LDDL cluster is established in Area 2, distributed Fig. 5(i) corroborates this, with energy flow metrics reaching
across nodes 9, 36, and 37, referred to as LDDL 1, LDDL 2, extreme values that are significantly elevated compared to
and LDDL 3, respectively. The total LDDL loads are 35.5%, stable operation. This demonstrates that a system collapse
35.2%, and 37.1% of the total system load for the three drives the proposed energy flow metrics to very high values,
test cases, respectively. The dynamic responses of the power serving as a clear indicator of catastrophic instability. Even
system to the three LDDL load datasets (from Fig. 1) are during this event, instances of opposing flows among the
illustrated in Fig. 4, Fig. 5, and Fig. 6. Each dataset reveals LDDLs can be observed.
distinct stability characteristics directly linked to the nature of DatasetC:InstarkcontrasttotheerraticbehaviorinDataset
its load profile. A, the gradual, stair-step load increases from Dataset C result
Dataset A: The sharp, periodic load spikes characteristic of in a visually more stable system response (Fig. 6). This is
inference tasks (Fig. 1(a)-(c)) induce severe transient instabil- becausetheslow-changingactiveandreactivepowerdemands

6
|     |     | (a) |     |     |     |     |     | (b) |     |     |     | (c) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (d) |     |     |     |     |     | (e) |     |     |     | (f) |     |     |
Fig.4:DatasetAsimulationresult:(a)Systemfrequency,(b)LDDLbusactivepower,(c)LDDLbusreactivepower,(d)LDDL
bus local directional energy flow, (e) total directional energy flow trajectory, and (f) Snapshot of total directional energy flow.
(Figs. 6(b) and 6(c)) allow the grid’s control mechanisms to tion vary gradually in conventional grids, these eigenvalue-
adapt.Consequently,thesystemfrequency(Fig.6(a))exhibits based estimates remain valid over extended time horizons,
well-damped,regularoscillationswithaconsistentperiodicity offering a dependable representation of system dynamics and
of approximately 2-3 seconds, maintaining overall stability. stability margins. In contrast, rapid increases or decreases in
The local directional energy flow (Fig. 6(d)) also reflects this, LDDL demand can induce abrupt shifts in operating points,
showingsmoothtransitionsratherthansharpspikes.However, causing eigenvalue trajectories to move quickly. Such move-
the total directional energy flows (Fig. 6(e)) reveal a different ments may result in temporary reductions in damping or even
dynamic: it displays significant, low-frequency oscillations the appearance of poorly damped oscillatory modes, which
with wide deviation ranges that follow the system’s natural can remain undetected if stability is assessed only at a few
oscillatory modes. The snapshots in Fig. 6(f) confirm this isolated operating points.
behavior, showing the LDDLs’ energy flows oscillating in To overcome this limitation, a snapshot-based analysis
unison at a slower pace with relatively consistent amplitudes. framework is required. By evaluating the system at multiple
| This comparison |     | provides |     | a crucial | insight: | the | rate | of           |     |      |         |            |               |     |
| --------------- | --- | -------- | --- | --------- | -------- | --- | ---- | ------------ | --- | ---- | ------- | ---------- | ------------- | --- |
|                 |     |          |     |           |          |     |      | points along | the | LDDL | ramping | trajectory | and computing |     |
change of the LDDL load determines the type of system the corresponding eigenvalue spectra, operators can track the
stress,actingasadisturbanceinthetransientsimulation.Rapid evolution of critical modes and their damping characteristics
| load variations |     | (Dataset | A)  | trigger | high-frequency |     | transient |         |            |          |       |             |     |          |
| --------------- | --- | -------- | --- | ------- | -------------- | --- | --------- | ------- | ---------- | -------- | ----- | ----------- | --- | -------- |
|                 |     |          |     |         |                |     |           | in real | time. This | approach | makes | it possible | to  | identify |
instability with erratic frequency deviations, sustained oscil- regions where stability margins are most vulnerable and to
| latory loads | (Dataset |     | B) can | lead to | system | collapse | under |             |         |          |            |             |     |         |
| ------------ | -------- | --- | ------ | ------- | ------ | -------- | ----- | ----------- | ------- | -------- | ---------- | ----------- | --- | ------- |
|              |          |     |        |         |        |          |       | gain deeper | insight | into the | underlying | mechanisms, |     | such as |
extreme conditions, while slow ramps (Dataset C) prevent convertercontroldynamics,networkinteractions,orprotection
sharptransientinstabilitybutexciteslow-moving,system-wide responses, that influence these variations. The enhanced visi-
oscillatorymodesvisibleintheenergyflowmetrics.Thisindi-
|     |     |     |     |     |     |     |     | bility provided |     | by snapshot-based |     | methods supports | proactive |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------------- | --- | ---------------- | --------- | --- |
catesthatevenwhenthesystemmaintainsfrequencystability, mitigation, including adjustments to ramping schedules, fine-
| it can still | experience |     | considerable | stress | that | manifests | in the |           |            |             |     |                |              |     |
| ------------ | ---------- | --- | ------------ | ------ | ---- | --------- | ------ | --------- | ---------- | ----------- | --- | -------------- | ------------ | --- |
|              |            |     |              |        |      |           |        | tuning of | controller | parameters, | or  | the deployment | of stabiliz- |     |
directionalenergyflowpatterns,makingthesemetricsvaluable ing resources such as damping controllers and energy storage
indicators for comprehensive stability assessment. systems,therebyimprovinggridresilienceunderfast-changing
|     |     |     |     |     |     |     |     | load conditions. |          |            |       |           |      |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | ---------- | ----- | --------- | ---- | ---- |
|     |     |     |     |     |     |     |     | Let us           | consider | the grid’s | state | variables | as x | ∈ Rn |
C. System-wideSmall-signalImpacts:Snapshot-basedAssess-
Rr,
ments including LDDL interface states, algebraic variables p ∈
|                  |     |           |     |        |         |           |        | control | inputs u | ∈ Rm, | and LDDL | input variables | v   | ∈ Rs |
| ---------------- | --- | --------- | --- | ------ | ------- | --------- | ------ | ------- | -------- | ----- | -------- | --------------- | --- | ---- |
| The small-signal |     | stability |     | of the | grid is | sensitive | to the |         |          |       |          |                 |     |      |
sharprampingbehaviorofLDDLs.Undertraditionaloperating such as load consumptions, thereby, the dynamical equation
|                   |        |            |               |           |             |          |          | can be compactly |     | written         | as: |     |     |      |
| ----------------- | ------ | ---------- | ------------- | --------- | ----------- | -------- | -------- | ---------------- | --- | --------------- | --- | --- | --- | ---- |
| conditions,       | system | operators  |               | typically | monitor     | the      | system   | at               |     |                 |     |     |     |      |
| a fixed operating |        | point      | and evaluate  |           | the damping | of       | dominant |                  |     |                 |     |     |     |      |
|                   |        |            |               |           |             |          |          |                  |     | x˙ =f(x,u,p,v), |     |     |     | (11) |
| modes, such       | as     | inter-area | oscillations. |           | Since       | load and | genera-  |                  |     |                 |     |     |     |      |

7
|     |     | (a) |     |     |     |     | (b) |     |     |     |     | (c) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (d) |     |     |     |     | (e) |     |     |     |     | (f) |     |     |     |
|     |     | (g) |     |     |     |     | (h) |     |     |     |     | (i) |     |     |     |
Fig.5:DatasetBsimulationresult:(a)-(f)Systemresponseunderstandardload.(g)-(i)Systemcollapsescenariowith1.6xload
fluctuation. Subplots show (a) System frequency, (b) Active power, (c) Reactive power, (d) Local directional energy flow, (e)
totaldirectionalenergyflowtrajectory,(f)Snapshotoftotaldirectionalenergyflow,(g)Frequencycollapse,(h)totaldirectional
| energy flow | trajectory |     | during collapse, |     | and (i) Snapshot |     | during | collapse. |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------------- | --- | ---------------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
and the power flow as: The Jacobians in the state matrix are denoted as:
|     |     |               |     |     |     |     |      |     | ∂f  |       | ∂f    | ∂g    |       | ∂g  |     |
| --- | --- | ------------- | --- | --- | --- | --- | ---- | --- | --- | ----- | ----- | ----- | ----- | --- | --- |
|     |     | g(x,p,u,v)=0, |     |     |     |     | (12) |     |     |       |       |       |       |     |     |
|     |     |               |     |     |     |     |      | A = | |   | ,A =  | | ,A  | =     | | ,A  | =   | | . |
|     |     |               |     |     |     |     |      | 11  | ∂x  | α0 13 | ∂p α0 | 23 ∂p | α0 21 | ∂x  | α0  |
where f(.) denotes the nonlinear dynamics, and g(.) denotes (18)
| the nonlinear | power | flows. | Linearizing |     | along the | initial oper- |     |                                     |      |          |          |        |               |      |      |
| ------------- | ----- | ------ | ----------- | --- | --------- | ------------- | --- | ----------------------------------- | ---- | -------- | -------- | ------ | ------------- | ---- | ---- |
|               |       |        |             |     |           |               |     | Thestatematrixatthatoperatingpointα |      |          |          |        | isdenotedas:A |      | =    |
|               |       |        |             |     |           |               |     |                                     |      |          |          |        | 0             |      | 0    |
| ating point,  | we    | get,   |             |     |           |               |     |                                     | A−1A |          |          |        |               |      |      |
|               |       |        |             |     |           |               |     | (A 11 −A                            | 13   | 21 ). As | the data | center | loads vary    | over | time |
23
∆x˙ =A ∆x+A ∆u+A ∆p+A ∆v, (13) during a ramping behavior, the operating conditions are also
|     | 11  |     | 12  | 13  | 14  |     |     |     |     |        |        |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | α α ,α | ,...,α |     |     |     |     |
0=A ∆x+A ∆u+A ∆p+A ∆v, (14) varied from 0 to 1 2 k resulting in the following
|     | 21  |     | 22  | 23  | 24  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sequenceofstatematricesforoneparticularrampingcondition
We have,
|          |     |         |     |         |     |     |      | within | a small       | time window | dictated | by  | k˜ as the | upper | bound |
| -------- | --- | ------- | --- | ------- | --- | --- | ---- | ------ | ------------- | ----------- | -------- | --- | --------- | ----- | ----- |
| ∆p=−A−1A |     | ∆x−A−1A |     | ∆u−A−1A |     |     |      |        |               |             |          |     |           |       |       |
|          |     | 21      |     | 22      | 24  | ∆v  | (15) | on the | time indices: |             |          |     |           |       |       |
|          | 23  |         | 23  |         | 23  |     |      |        |               |             |          |     |           |       |       |
Therefore, the dynamical model can be captured as: A={A ,A ,...,A },k ≤k˜. (19)
|         |     |      |        |     |         |     |     |     |     |     | 0 1 | k   |     |     |     |
| ------- | --- | ---- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ∆x˙ =(A | −A  | A−1A | )∆x+(A |     | −A A−1A | )∆u |     |     |     |     |     |     |     |     |     |
11 13 21 12 13 21 As these state matrices are functions of the operating condi-
|        |          | 23      |         |                |               | 23  |      |                                                      |         |             |     |     |     |     |     |
| ------ | -------- | ------- | ------- | -------------- | ------------- | --- | ---- | ---------------------------------------------------- | ------- | ----------- | --- | --- | --- | --- | --- |
|        |          | A−1A    |         |                |               |     |      | tions,whichareinturnfunctionsoftheLDDLloadvariables, |         |             |     |     |     |     |     |
| +(A    | 14 −A    | 13      | 21 )∆v, |                |               |     | (16) |                                                      |         |             |     |     |     |     |     |
|        |          | 23      |         |                |               |     |      | we can                                               | capture | the changes | as: |     |     |     |     |
| We can | consider | without |         | any additional | supplementary |     |      |                                                      |         |             |     |     |     |     |     |
≤k˜.
| control | action as: |     |     |     |     |     |     |     | A={A | (v ),A | (v ),...,A | (v  | )},k |     | (20) |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ---------- | --- | ---- | --- | ---- |
|         |            |     |     |     |     |     |     |     |      | 0 0    | 1 1        | k   | k    |     |      |
A−1A A−1A Therefore, the LDDL consumption impacts the dynamics in
| ∆x˙ =(A | 11 −A | 13  | 21 )∆x+(A | 14  | −A 13 | 21 )∆v, |      |           |     |         |         |               |           |     |     |
| ------- | ----- | --- | --------- | --- | ----- | ------- | ---- | --------- | --- | ------- | ------- | ------------- | --------- | --- | --- |
|         |       | 23  |           |     |       | 23      |      |           |     |         |         |               |           |     |     |
|         |       |     |           |     |       |         | (17) | two ways: | the | forcing | term in | the dynamical | equation, |     | and |

8
(a) (b) (c)
(d) (e) (f)
Fig.6:DatasetCsimulationresult:(a)Systemfrequency,(b)LDDLbusactivepower,(c)LDDLbusreactivepower,(d)LDDL
bus local directional energy flow, (e) Total directional energy flow trajectory, and (f) Snapshot of total directional energy flow.
the perturbation in the state matrices due to the perturbation Proposition 2: Suppose that the spectra converge in the Haus-
in the operating conditions. From the operating condition α i dorff sense: σ(A n ) − d −H→ Σ. The safe set of eigenvalues S
to α i+1 , the perturbation in the state matrices caused by the is then a subset of Σ, defined by system constraints such as
LDDL consumption change δv :(v i+1 −v i ) is given as: ℜ(λ) < 0. Under bifurcations, Σ may contain eigenvalues
∂A outside the safe region, even though Hausdorff convergence
∆A i = ∂v iδv,A i+1 =A i +∆A i (21) holds, i.e, S ⊆Σ.
i
Alg. 3 describes the snapshot-based small-signal stability
Proposition 1: Considering a compact set ofLDDL consump-
metric-based monitoring algorithm.
tion ramp V = {v ,v ,...,v } converging to v∗ with state
0 1 k
matrix A∗, the perturbation in the eigenvalues of the state
Algorithm 3: Snapshot-Based Small-Signal Stability
matrix is given by,
Analysis under LDDL Ramp
∆λ =
w
i
∗(∂
∂
A
vi
iδv)v
i , (22) 1 Inputs: Dynamic model f(.), ramp profile v(t),
i w i ∗v i thresholds ζ min ,m min .
and such a sequence converges within the compact set of 2 Outputs: Stability margins, critical modes,
eigenvalues to a limiting stable load condition v∗ of a par- visualization data.
ticular ramp. 3 Define snapshot set {v(t k )}N k=1 along ramp.
The proposition follows from recalling the convergence of 4 for k =1,...,N do
spectra in terms of the Hausdorff metric distance. Let (X,d) 5 Solve steady-state equilibrium: x∗(t k )← power
be a metric space, and let A,B ⊂ X be nonempty compact flow.
(cid:12)
sets. The Hausdorff distance [29], [30] between A and B is 6 Linearize system: A k ←∂f/∂x(cid:12) (x∗(tk),v(tk)) .
defined by 7 Compute eigenvalues {λk i } of A k .
(cid:26) (cid:27) 8 Evaluate metrics:
d H (A,B)=max a su ∈A p b i ∈ n B f d(a,b), b s ∈ u B p a i ∈ n A f d(a,b) . 1 9 0 S D p a e m ct p r i a n l g ab ra s t c i i o s : sa: m k =−max i ℜ(λk i ).
F pl o a r ne thi C s , an o a r lys m is o , re the sp u e n c d ifi er c l a y l i l n y g , m no e n tr e i m c p s t p y ac c e o i m s p th le e x co su m b p s l e e t x s ζ k,min =min i √ (ℜ(λ − k) ℜ )2 ( + λk i (ℑ ) (λk))2 .
i i
of C with the distance metric as d = |γ 1 − γ 2 |, where 11 Identify critical mode λ∗ k achieving ζ k,min .
γ 1 ,γ 2 ∈ C. We have the sequence (A k ) with spectra σ(A k ), 12 Compute participation factors for λ∗ k .
and A∗ with spectrum σ(A∗), which will have σ(A k ) → 13 if m k ≤m min or ζ k,min ≤ζ min then
σ(A∗)in the Hausdorff sense with d H (cid:0) σ(A k ),σ(A∗) (cid:1) −→0. 14 Flag snapshot v(t k ) as critical.
However, this only considers the set convergence, and the 15 end
system may be subjected to bifurcations; therefore, the safe 16 end
set will be a subset of the compact convergent set.

9
|     |     | (a) |     |     |     |     |     | (b) |     |     |     | (c) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (d) |     |     |     |     |     | (e) |     |     |     | (f) |     |     |
Fig. 7: Small-signal Analysis result: damping ratio trajectory of (a) Scenario A, (b) Scenario B, (c) Scenario C and the
eigenvalue realpart example (−25% and +15%) of (d) Scenario A, (e) Scenario B, (f) Scenario C
D. Numerical Experiments with Small-Signal Studies the 0.65 Hz mode significantly improves, rising from around
1.2%toover5%.However,thedampingofthe0.41Hzmode
| To demonstrate  |     | the       | efficacy | of the   | snapshot-based |       | small-  |                |           |      |          |            |          |              |
| --------------- | --- | --------- | -------- | -------- | -------------- | ----- | ------- | -------------- | --------- | ---- | -------- | ---------- | -------- | ------------ |
|                 |     |           |          |          |                |       |         | simultaneously | degrades. | This | opposing |            | behavior | highlights a |
| signal analysis |     | framework |          | outlined | in Alg.        | 3, we | conduct |                |           |      |          |            |          |              |
|                 |     |           |          |          |                |       |         | key challenge: | a change  | that | is       | beneficial | for one  | mode may     |
numericalexperimentsonamodifiedIEEE68-bustestsystem.
|                |     |       |           |           |     |     |           | be detrimental | to another. |     | As seen | in Fig. | 7(e), | despite the |
| -------------- | --- | ----- | --------- | --------- | --- | --- | --------- | -------------- | ----------- | --- | ------- | ------- | ----- | ----------- |
| We investigate |     | three | different | scenarios | for | the | placement |                |             |     |         |         |       |             |
improveddampingofonemode,aneigenvalueassociatedwith
| of LDDLs,        | designated |        | as          | scenarios      | A, B, | and C.         | For each |             |               |        |          |         |          |              |
| ---------------- | ---------- | ------ | ----------- | -------------- | ----- | -------------- | -------- | ----------- | ------------- | ------ | -------- | ------- | -------- | ------------ |
|                  |            |        |             |                |       |                |          | a different | mode becomes  |        | unstable | at the  | +15%     | load point.  |
| scenario,        | we vary    | the    | LDDL        | load from      | −25%  | (representing  |          |             |               |        |          |         |          |              |
|                  |            |        |             |                |       |                |          | Here also,  | participation | factor | analysis | shows   | that     | the inverter |
| a load decrease) |            | to     | +15%        | (representing  | a     | load increase) | of       |             |               |        |          |         |          |              |
|                  |            |        |             |                |       |                |          | angles at   | the boundary  | of     | area     | 1 and 2 | at buses | 1,3, and 8   |
| its nominal      | value      | and    | analyze     | the trajectory |       | of the         | system’s |             |               |        |          |         |          |              |
|                  |            |        |             |                |       |                |          | cause this  | bifurcation.  |        |          |         |          |              |
| dominant         | inter-area | modes. |             |                |       |                |          |             |               |        |          |         |          |              |
| Scenario         | A:         | LDDLs  | are located | at             | buses | 9,36, and      | 37. The  |             |               |        |          |         |          |              |
results of the analysis are presented in Fig. 7(a) and Fig. 7(d). Scenario C: LDDLs are connected at buses 3,4, and 18,
First, Fig. 7(a) reveals a critical trend: as the LDDL load in the middle of Area 1 (referring to Fig. 3). Similar to
increases, the damping ratios of the 0.63 Hz and 0.40 Hz Scenario B, we reduce the nominal loads to 70% from the
| modes progressively |     |     | decrease. | The | damping | of the | 0.40 Hz |           |                           |     |     |        |           |          |
| ------------------- | --- | --- | --------- | --- | ------- | ------ | ------- | --------- | ------------------------- | --- | --- | ------ | --------- | -------- |
|                     |     |     |           |     |         |        |         | values in | Fig. 1 (16.48,12.79,17.05 |     |     | p.u.). | This case | provides |
mode, in particular, deteriorates from approximately 1.15% to another distinct result. Here, an increase in LDDL load leads
below 0.5%, a level considered critically low for secure grid to a dramatic improvement in the damping of the 0.64 Hz
operation. This degradation culminates in instability, as con- mode, as its damping ratio dramatically increases from 1.5%
firmedbyFig.7(d).Thesystemremainsstableata−25%load to nearly 16% in Fig. 7(c). This suggests that, at certain
| decrease. | In contrast, |     | at a +15% | load | increase, | an  | eigenvalue |            |       |          |     |        |        |              |
| --------- | ------------ | --- | --------- | ---- | --------- | --- | ---------- | ---------- | ----- | -------- | --- | ------ | ------ | ------------ |
|           |              |     |           |      |           |     |            | locations, | LDDLs | can make | the | system | stable | for specific |
crossesintotheright-halfplane(highlightedinred),rendering inter-area oscillations. However, a closer look at the full
the system unstable. Participation factor analysis shows that spectrum in Fig. 7(f) reveals that even in this scenario, a
| the unstable | mode |     | is impacted | by  | the inverter |     | angles | at  |     |     |     |     |     |     |
| ------------ | ---- | --- | ----------- | --- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
different,previouslywell-dampedmodeisdriventoinstability
buses 12 and 25, showing complex interactions caused by the by the increased loading. This shows the critical importance
integrated data centers with existing grid components. of the snapshot-based framework; focusing only on the most
Scenario B: LDDLs are placed at buses 15, 16, and 20 in prominent or historically problematic modes can obscure
Area 1 as indicated in Fig. 3. To compute a feasible power emerging threats from other parts of the eigenvalue spectrum.
flow solution with a nominal value of LDDL, we reduce the Similar to the previous scenarios, participation factor analysis
load of these three buses to 80% of the load represented in reveals that the angles of the data center at bus 3 and the
Fig. 1, such as 17.95,14.95 and 23.83 p.u. The analysis for inverteratbus12havethemostimpactontheunstablemode,
thisscenarioillustratesthelocation-dependentnatureofLDDL demonstratinghowLDDLintegrationatdifferentlocationscan
impacts.UnlikescenarioA,Fig.7(b)showsthatincreasingthe shift the sources of system instability across various network
| LDDL load | has | a mixed | effect | on damping. |     | The damping | of  | components. |     |     |     |     |     |     |
| --------- | --- | ------- | ------ | ----------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |

10
|     |     | IV. | CONCLUSION |     |     |     |     |                                                                 |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |            |     |     |     |     | [8] A.H.Khalaj,T.Scherer,andS.K.Halgamuge,“Energy,environmental |     |     |     |     |     |     |     |
andeconomicalsavingpotentialofdatacenterswithvariouseconomiz-
| This paper | investigated |     | the | stability | implications | of  | large |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --------- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ersacrossaustralia,”Appliedenergy,vol.183,pp.1528–1549,2016.
dynamic digital loads (LDDLs), with a particular focus on [9] H. An and X. Ma, “Dynamic coupling real-time energy consumption
AI-driven data centers. For nonlinear transient behavior, we modelingfordatacenters,”EnergyReports,vol.8,pp.1184–1192,2022.
|            |                   |     |     |         |              |      |     | [10] I.Drovtar,M.Leinakse,K.Tuttelberg,andJ.Kilter,“Utilizingdemand |     |                |     |         |     |          |               |
| ---------- | ----------------- | --- | --- | ------- | ------------ | ---- | --- | ------------------------------------------------------------------- | --- | -------------- | --- | ------- | --- | -------- | ------------- |
| introduced | energy-flow-based |     |     | metrics | that capture | both | lo- |                                                                     |     |                |     |         |     |          |               |
|            |                   |     |     |         |              |      |     | response                                                            | in  | load modelling | for | voltage | and | reactive | power control |
calized and coupling stress at data center buses. The results studies,”IEEETransactionsonPowerSystems,2024.
showed that abrupt spikes create severe frequency deviations, [11] J. Sun, S. Wang, J. Wang, and L. M. Tolbert, “Dynamic model and
|           |              |     |              |      |           |     |       | converter-based |     | emulator | of a | data center | power | distribution | system,” |
| --------- | ------------ | --- | ------------ | ---- | --------- | --- | ----- | --------------- | --- | -------- | ---- | ----------- | ----- | ------------ | -------- |
| sustained | oscillations |     | can escalate | into | collapse, | and | grad- |                 |     |          |      |             |       |              |          |
IEEETransactionsonPowerElectronics,vol.37,no.7,pp.8420–8432,
| ual ramps | excite | slower | oscillatory |     | modes. | These | insights |     |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ----------- | --- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
2022.
highlight how the proposed energy-flow analytics provide a [12] H.Suryanarayana,L.Qi,Y.Zhang,T.Jiang,S.Colombi,andH.Han-
fine-grained view of transient stress that conventional sta- dlin,“Systemmodelingandfaultstudiesindatacenterpowerdistribu-
tion,”inCIRED2021-The26thInternationalConferenceandExhibition
| bility measures |     | fail to | reveal. | For small-signal |     | behavior, | we  |                                     |     |     |     |     |                        |     |     |
| --------------- | --- | ------- | ------- | ---------------- | --- | --------- | --- | ----------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- |
|                 |     |         |         |                  |     |           |     | onElectricityDistribution,vol.2021. |     |     |     |     | IET,2021,pp.1435–1439. |     |     |
developed a snapshot-based analysis framework that tracks [13] A.Jimenez-RuizandF.Milano,“Datacentermodelfortransientstability
eigenvaluetrajectoriesduringrapidloadramps.Thisapproach analysisofpowersystems,”arXivpreprintarXiv:2505.16575,2025.
|          |               |     |       |                    |     |         |     | [14] H.-D. | Chang, | C.-C. Chu, | and | G. Cauley, | “Direct | stability | analysis of |
| -------- | ------------- | --- | ----- | ------------------ | --- | ------- | --- | ---------- | ------ | ---------- | --- | ---------- | ------- | --------- | ----------- |
| revealed | how different |     | modes | can simultaneously |     | improve | or  |            |        |            |     |            |         |           |             |
electricpowersystemsusingenergyfunctions:theory,applications,and
deteriorate in damping, depending on location and loading perspective,”ProceedingsoftheIEEE,vol.83,no.11,pp.1497–1529,
| conditions,  | showing      | the     | importance   | of              | continuous | monitoring   |     | 1995.      |          |           |           |                |     |                   |            |
| ------------ | ------------ | ------- | ------------ | --------------- | ---------- | ------------ | --- | ---------- | -------- | --------- | --------- | -------------- | --- | ----------------- | ---------- |
|              |              |         |              |                 |            |              |     | [15] H.-D. | Chiang,  | F. F. Wu, | and       | P. P. Varaiya, | “A  | bcu method        | for direct |
| rather than  | single-point |         | assessments. |                 | The main   | contribution |     |            |          |           |           |                |     |                   |            |
|              |              |         |              |                 |            |              |     | analysis   | of power | system    | transient | stability,”    |     | IEEE Transactions | on         |
| of this work |              | lies in | advancing    | stability-aware |            | assessment   |     |            |          |           |           |                |     |                   |            |
powersystems,vol.9,no.3,pp.1194–1208,1994.
| tools that | bridge | transient | and | small-signal | domains, | offering |     |            |        |              |           |                   |           |          |             |
| ---------- | ------ | --------- | --- | ------------ | -------- | -------- | --- | ---------- | ------ | ------------ | --------- | ----------------- | --------- | -------- | ----------- |
|            |        |           |     |              |          |          |     | [16] T. L. | Vu and | K. Turitsyn, | “Lyapunov |                   | functions | family   | approach to |
|            |        |           |     |              |          |          |     |            |        |              |           | IEEE Transactions |           | on Power | Systems,    |
operators deeper situational awareness of evolving risks from transient stability assessment,”
vol.31,no.2,pp.1269–1277,2015.
datacenterintegration.Futureworkwillextendthesemethods
|     |     |     |     |     |     |     |     | [17] S.Backhaus,R.Bent,D.Bienstock,M.Chertkov,andD.Krishnamurthy, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
byincorporatingdetaileddynamicsofLDDLsandcoordinated “Efficient synchronization stability metrics for fault clearing,” arXiv
storage, and by validating the proposed metrics with real-time preprintarXiv:1409.4451,2014.
measurements to enable their integration into operator-facing [18] C. Mishra, L. Vanfretti, J. Delaree Jr, T. Purcell, and K. D. Jones,
|     |     |     |     |     |     |     |     | “Understanding |     | the inception |     | of 14.7 hz | oscillations | emerging | from a |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ---------- | ------------ | -------- | ------ |
decision-support platforms. datacenter,”SustainableEnergy,GridsandNetworks,p.101735,2025.
|     |     |     |     |     |     |     |     | [19] S. Biswas, | A.          | C. Varghese, | K.       | Chatterjee, | S. Nekkalapu, |                    | B. Ross, and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------- | ------------ | -------- | ----------- | ------------- | ------------------ | ------------ |
|     |     |     |     |     |     |     |     | J. Follum,      | “Evaluating |              | the risk | to bulk     | power         | system reliability | from         |
ACKNOWLEDGMENT
largeloadinducedoscillations,”AuthoreaPreprints,2025.
The research is supported by the Energy and Environment [20] M.-S.KoandH.Zhu,“Wide-areapowersystemoscillationsfromlarge-
scaleaiworkloads,”arXivpreprintarXiv:2508.16457,2025.
| Directorate’s | Laboratory |     | Directed | Research | at  | Pacific | North- |                |     |             |     |             |     |                |     |
| ------------- | ---------- | --- | -------- | -------- | --- | ------- | ------ | -------------- | --- | ----------- | --- | ----------- | --- | -------------- | --- |
|               |            |     |          |          |     |         |        | [21] S. Kundu, | K.  | Chatterjee, | R.  | R. Hossain, | S.  | P. Nandanoori, | and |
west National Laboratory (PNNL). The authors would like V.Adetola,“Managingrisksfromlargedigitalloadsusingcoordinated
to thank Soumya Kundu, Sai Pushpak Nandanoori, Ramij R. grid-formingstoragenetwork,”arXivpreprintarXiv:2508.11080,2025.
|            |           |         |       |             |           |          |     | [22] S. Samsi, | M.  | L. Weiss,  | D.       | Bestor, B.   | Li, M. | Jones,  | A. Reuther,  |
| ---------- | --------- | ------- | ----- | ----------- | --------- | -------- | --- | -------------- | --- | ---------- | -------- | ------------ | ------ | ------- | ------------ |
| Hossain,   | and Bowen |         | Huang | at Pacific  | Northwest | National |     |                |     |            |          |              |        |         |              |
|            |           |         |       |             |           |          |     | D. Edelman,    |     | W. Arcand, | C. Byun, | J. Holodnack |        | et al., | “The mit su- |
| Laboratory | for       | sharing | LDDL  | consumption | profile   | examples |     |                |     |            |          |              |        |         |              |
perclouddataset,”in2021IEEEHighPerformanceExtremeComputing
and helpful discussions related to this work. Authors would Conference(HPEC).
IEEE,2021,pp.1–8.
|     |     |     |     |     |     |     |     | [23] Y.Li,M.Mughees,Y.Chen,andY.R.Li,“Theunseenaidisruptionsfor |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
alsoliketothankLongVuandBrettRossatPacificNorthwest
powergrids:Llm-inducedtransients,”arXivpreprintarXiv:2409.11416,
NationalLaboratoryforhelpfulsuggestionsanddiscussionson
2024.
the LDDL research. [24] Z.Zhou,J.Sun,andG.Sun,“Automatedhpcworkloadgenerationcom-
biningstatisticalmodelingandautoregressiveanalysis,”inInternational
|     |     |     |            |     |     |     |     | SymposiumonBenchmarking,MeasuringandOptimization. |     |            |     |            |              |     | Springer,    |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ------------------------------------------------- | --- | ---------- | --- | ---------- | ------------ | --- | ------------ |
|     |     |     | REFERENCES |     |     |     |     | 2023,pp.153–170.                                  |     |            |     |            |              |     |              |
|     |     |     |            |     |     |     |     | [25] S. Herbein,                                  |     | D. H. Ahn, | D.  | Lipari, T. | R. Scogland, |     | M. Stearman, |
[1] W.E.C.Council,“Anassessmentoflargeloadinterconnectionrisksin
M.Grondona,J.Garlick,B.Springmeyer,andM.Taufer,“Scalablei/o-
thewesterninterconnection,”2024.
awarejobschedulingforburstbufferenabledhpcclusters,”inProceed-
| [2] J. Aljbour, | T.  | Wilson, | and P. Patel, | “Powering | intelligence: | Analyzing |     |      |             |     |               |           |     |                     |     |
| --------------- | --- | ------- | ------------- | --------- | ------------- | --------- | --- | ---- | ----------- | --- | ------------- | --------- | --- | ------------------- | --- |
|                 |     |         |               |           |               |           |     | ings | of the 25th | ACM | International | Symposium |     | on High-Performance |     |
artificialintelligenceanddatacenterenergyconsumption,”EPRIWhite ParallelandDistributedComputing,2016,pp.69–80.
Paperno.3002028905,2024.
|             |        |           |          |                                   |     |     |     | [26] D.Zhang,M.S.Raj,B.Xie,S.Di,andD.Dai,“Cross-systemanalysis |                  |     |                |     |                |           |       |
| ----------- | ------ | --------- | -------- | --------------------------------- | --- | --- | --- | -------------------------------------------------------------- | ---------------- | --- | -------------- | --- | -------------- | --------- | ----- |
| [3] OpenAI, | “Gpt-4 | technical | report,” | https://arxiv.org/abs/2303.08774, |     |     |     |                                                                |                  |     |                |     |                |           |       |
|             |        |           |          |                                   |     |     |     | of job                                                         | characterization |     | and scheduling |     | in large-scale | computing | clus- |
2023,accessed:2025-09-16.
|                 |     |             |             |     |           |          |          | ters,”            | in 2024 | IEEE | International         | Parallel | and | Distributed | Processing |
| --------------- | --- | ----------- | ----------- | --- | --------- | -------- | -------- | ----------------- | ------- | ---- | --------------------- | -------- | --- | ----------- | ---------- |
| [4] H. Touvron, |     | T. Lavril,  | G. Izacard, | X.  | Martinet, | M.-A.    | Lachaux, |                   |         |      |                       |          |     |             |            |
|                 |     |             |             |     |           |          |          | Symposium(IPDPS). |         |      | IEEE,2024,pp.716–727. |          |     |             |            |
| T. Lacroix,     |     | B. Rozière, | N. Goyal,   | E.  | Hambro,   | F. Azhar | et al.,  |                   |         |      |                       |          |     |             |            |
“Llama:Openandefficientfoundationlanguagemodels,”arXivpreprint [27] B.Li,Y.Fan,M.Dearing,Z.Lan,P.Rich,W.Allcock,andM.Papka,
arXiv:2302.13971,2023. “Mrsch:Multi-resourceschedulingforhpc,”in2022IEEEInternational
|     |     |     |     |     |     |     |     | ConferenceonClusterComputing(CLUSTER). |     |     |     |     |     | IEEE,2022,pp.47–57. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | ------------------- | --- |
[5] M.Awais,M.Naseer,S.Khan,R.M.Anwer,H.Cholakkal,M.Shah,
|     |     |     |     |     |     |     |     | [28] B.PalandB.Chaudhuri,RobustControlinPowerSystems. |     |     |     |     |     |     | Springer |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- |
M.-H.Yang,andF.S.Khan,“Foundationmodelsdefininganewerain
Science&BusinessMedia,2006.
| vision: | a survey | and | outlook,” IEEE | Transactions |     | on Pattern | Analysis |     |     |     |     |     |     |     |     |
| ------- | -------- | --- | -------------- | ------------ | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
andMachineIntelligence,2025. [29] D. Kraft, “Computing the hausdorff distance of two sets from their
[6] D.Huang,R.Dong,andX.Wang,“Modelingandanalysisofdemand distance functions,” International Journal of Computational Geometry
response strategies for datacenters in smart grid environment,” in The &Applications,vol.30,no.01,pp.19–49,2020.
2nd International Conference on Computing and Data Science, 2021, [30] M. Gil’, “A new inequality for the hausdorff distance between spectra
oftwomatrices,”RendicontidelCircoloMatematicodiPalermoSeries
pp.1–6.
[7] NERCLargeLoadsTaskForce,“Characteristicsandrisksofemerging 2,vol.70,no.1,pp.341–348,2021.
largeloads,”NorthAmericanElectricReliabilityCorporation(NERC), [31] P. Kundur et al., “Power system stability,” Power system stability and
| WhitePaper,July2025. |     |     |     |     |     |     |     | control,vol.10,no.1,pp.7–1,2007. |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |

11
[32] W.Du,“Modelspecificationofdroop-controlled,grid-forminginverters DC power distribution unit (and fast dynamics of rectifier).
(regfm_a1),”PacificNorthwestNationalLaboratory(PNNL),Richland, It effectively mimics the energy buffering (dynamic filtering)
WA(UnitedStates),Tech.Rep.,2023. effect of interfacing elements on the PAI. The active and
j
reactive power balance at each bus j =1,...,N is expressed
APPENDIXA
as:
ADDITIONALMODELINGDETAILS:
 
We consider a bulk power system which includes syn-  (cid:88) N 
0=P −Re V (V B )∗ −V2G , (25a)
chronous generators (SGs), grid-forming inverters (GFMs), ej j jk jk j j
 
k=1,k̸=j
andlargedynamicdigitalloads(LDDLs).WeutilizetheIEEE
 
68−busbenchmarkmodelsinphasordomainwiththenetwork  (cid:88) N 
0=Q −Im V (V B )∗ −V2B , (25b)
parameters are obtained from the standard data set [28] with ej j jk jk j j
 
additional modifications to interconnect inverters and LDDLs. k=1,k̸=j
The dynamics of each SG are governed by the classical where P and Q are the net active and reactive power
ej ej
swingequationsthataresufficientforpoweroscillationrelated injectionsatbusj.Forabusj withanLDDL,theseinjections
stability studies and frequency dynamics [31]: are negative consumptions, i.e., P =−P and Q =−Q .
ej j ej j
δ˙ =ω −ω , (23a) The terms G j and B j denote the shunt conductance and
i i 0 susceptanceatbusj,andB isthesusceptanceofthelossless
ω˙ = 1 [D (ω −ω )+P −P ], (23b) jk
i Mi i 0 i i ei line between buses j and k. In compact form, the network
where δ and ω denote the rotor angle and frequency of equations are:
i i
generator i, P i is the mechanical input power, and P ei is the 0=g(x s ,x l ,V), (26)
electrical output power. The constants M and D represent
i i wherex andx arethestatevectorsfortheSGsandLDDLs,
s l
the inertia and damping coefficients, respectively. The IEEE
respectively, and V is the vector of bus voltage magnitudes.
68−bustestsystemismodifiedtoincludeGFMIBRsonselect
buses.Thereareatotalof35suchinverterseachataloadbus
APPENDIXB
with few of them only contains the LDDLs (to create the AI
ADDITIONALDETAILSONTHEDIRECTIONALENERGY
data center hub). Each LDDL at bus j ∈ L is modeled as a
FLOWNUMERICALS
grid-interactive load whose power consumption is modulated
by an interfacing inverter which mimics installations of inter- Fig. 8 illustrates the directional coupling energy flow, local
active UPS, storage or local generation to support the LDDL. directional energy flow at neighboring buses, and the corre-
The control structure for the interfacing inverter is adapted sponding rate of change of frequency (RoCoF) across three
from droop-based principles to regulate power exchange with representativeoperationalscenarios.Panels(a)–(c)correspond
the grid, more specifically REGFM A1 model [32] developed to Scenario A, panels (d)–(f) correspond to Scenario B,
at PNNL. The corresponding dynamic equations are: and panels (g)–(i) correspond to Scenario C. Each scenario
representsadistinctloadbehavioratthedatacenter:(A)sharp
δ˙ j =ω j −ω 0 , (24a) inference-type spikes, (B) sustained oscillatory consumption,
ω˙ = 1(cid:2) ω −ω +m (Pset−PL−P ) (cid:3) , (24b) and (C) gradual high-performance computing (HPC)-style
V˙e j = τ 1 j (cid:2) V 0 set− j V −V pj e+ j m (Q j set−Q j ) (cid:3) , (24c) ramping. The plots provide a comparative view of how these
j τj j j j qj j j operational differences manifest in the dynamic energy flow
E˙ =kpvV˙e+kivVe, (24d) patterns and frequency responses.
j j j j j
P˙L = 1 (PAI −PL). (24e) In Scenario A [Figs. 8(a)–(c)], the data center undergoes
j TLj j j rapid and high-magnitude fluctuations that cause pronounced
Here, δ and ω are the voltage angle and frequency of the variations in both the directional coupling energy and local
j j
inverterinterface.ThevariablesV andE denotetheterminal directional energy flow. These quantities exhibit sharp peaks
j j
and internal voltage magnitudes of the inverter, and Ve is an and fast oscillations, reflecting strong transient interactions
j
auxiliary state for the voltage controller. The parameters m between the data center bus and its neighboring nodes. The
pj
andm aretheP-ω andQ-V droopcoefficients,whilekpv RoCoF trace also shows abrupt changes aligned with these
qj j
and kiv are the proportional and integral gains of the voltage energy flow spikes, indicating that the system experiences
j
control loop. The setpoints Pset, Qset, and Vset are the short but intense frequency disturbances following each load
j j j
desired active power consumption, reactive power exchange, spike.Thestrongtemporalalignmentamongthethreemetrics
and terminal voltage magnitude, respectively. The variables highlights the impulsive nature of the load events in this
P and Q are the active and reactive power consumed by scenario.
j j
the other local loads at the inverter terminals and grid if InScenarioB[Figs.8(d)–(f)],thesystemresponsebecomes
the inverter interfaces a local generation, and the LDDL dominated by sustained oscillatory components. The direc-
consumption is captured as PAI. In equation (24e), PL is tional coupling energy exhibits slower but persistent oscilla-
j j
the intermediate state representing the power consumed by tions of larger amplitude compared to Scenario A, suggesting
the internal power electronics of the load. This first-order prolonged energy exchanges between interconnected buses.
filter, with time constant T , models the aggregate dynamic The local directional energy flow at the neighboring buses
Lj
properties of the interfacing power electronics, such as the follows a similar trend but remains at smaller magnitudes,

12
|     |     | (a) |     |     |     |     |     | (b) |     |     | (c) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (d) |     |     |     |     |     | (e) |     |     | (f) |     |
|     |     | (g) |     |     |     |     |     | (h) |     |     | (i) |     |
Fig.8:DirectionalcouplingandlocalenergyflowcharacteristicsunderScenariosA,B,andC.Subplotsshow(a)–(c)directional
coupling energy flow, (d)–(f) local directional energy flow of neighboring nodes near the data center bus, and (g)–(i) rate of
change of frequency (RoCoF). Scenarios A, B, and C correspond to distinct data center operational patterns characterized by
sharp inference spikes, sustained oscillatory consumption, and gradual HPC-style ramp-up behaviors, respectively.
indicating that nearby inverters and local buses experience acteristics of the data center load directly influence the shape
comparable yet attenuated responses. The RoCoF waveform andintensityofbothdirectionalandlocalenergyflows,aswell
shows quasi-periodic oscillations that persist throughout the astheircorrespondingfrequencyresponses.WhileScenarioA
time window, corresponding to the sustained load fluctuations is marked by fast impulsive interactions, Scenario B exhibits
characteristic of this scenario. Overall, Scenario B represents persistent oscillations, and Scenario C shows gradual, well-
a condition where continuous oscillatory stress rather than damped dynamics. The similar temporal patterns but smaller
impulsive events governs the system dynamics. amplitudesintheneighboringnodesfurtherindicatethatlocal
inverter-connectedbusesexperiencecomparablebutattenuated
| In Scenario |     | C [Figs. | 8(g)–(i)], | the | gradual | ramp-up | in data |     |     |     |     |     |
| ----------- | --- | -------- | ---------- | --- | ------- | ------- | ------- | --- | --- | --- | --- | --- |
centerloadresultsinmuchsmoothertemporalprofilesforboth directional energy flow behaviors relative to the main data
|     |     |     |     |     |     |     |     | center bus. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
couplingandlocaldirectionalenergyflows.Thevariationsare
| moderate | and | evolve over | longer | time | scales, | indicating | that |     |     |     |     |     |
| -------- | --- | ----------- | ------ | ---- | ------- | ---------- | ---- | --- | --- | --- | --- | --- |
APPENDIXC
the system adapts to the changing load with minimal abrupt PARTICIPATIONFACTORANALYSISDETAILS
transients.Thelocaldirectionalenergyflowattheneighboring
|     |     |     |     |     |     |     |     | The participation |     | factors [28] | utilized in Section | III.D are |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | ------------------- | --------- |
nodesagainfollowsthesameoverallpatternasthatofthedata
|             |     |              |     |               |            |       |          | computed    | using     | both right | and left eigenvectors | to identify |
| ----------- | --- | ------------ | --- | ------------- | ---------- | ----- | -------- | ----------- | --------- | ---------- | --------------------- | ----------- |
| center bus, | but | with smaller |     | magnitudes.   | The        | RoCoF | trace    |             |           |            |                       |             |
|             |     |              |     |               |            |       |          | which state | variables | contribute | most significantly    | to each     |
| shows small | and | well-damped  |     | oscillations, | reflecting |       | a stable |             |           |            |                       |             |
frequency response under gradual load variations. Compared eigenvalue (mode). For a power system with state matrix A,
|          |          |       |            |          |                |         |      | theparticipationfactorp |                | ofthei-thstatevariableinthek-th |     |     |
| -------- | -------- | ----- | ---------- | -------- | -------------- | ------- | ---- | ----------------------- | -------------- | ------------------------------- | --- | --- |
| with the | previous | two   | cases,     | Scenario | C demonstrates |         | that |                         |                | ik                              |     |     |
|          |          |       |            |          |                |         |      | mode is                 | mathematically | defined                         | as: |     |
| slowly   | varying  | loads | cause less | severe   | transient      | stress, | pro- |                         |                |                                 |     |     |
ducing smoother and more regular energy flow trajectories. |ϕ ψ |
ik ik
|     |     |     |     |     |     |     |     |     |     | p ik = (cid:80)n |     | (27) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---- |
Taken together, these results show that the temporal char- |ϕ ψ |
|     |     |     |     |     |     |     |     |     |     |     | j=1 jk jk |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |

13
| TABLE | I: Participation |     | factors | for | the | most unstable | mode | in          |           |     |         |                |         |
| ----- | ---------------- | --- | ------- | --- | --- | ------------- | ---- | ----------- | --------- | --- | ------- | -------------- | ------- |
|       |                  |     |         |     |     |               |      | in Scenario | B showing | the | highest | contributions, | showing |
Scenario A
complexinteractionscausedbytheintegrateddatacenterswith
|                    |          |     |     |           |       |     |          | existing        | grid components. | For | Scenario | B, the     | inverter angles |
| ------------------ | -------- | --- | --- | --------- | ----- | --- | -------- | --------------- | ---------------- | --- | -------- | ---------- | --------------- |
| EigenvalueRealPart |          |     |     | Component | State | Bus | PF       |                 |                  |     |          |            |                 |
|                    |          |     |     |           |       |     |          | at the boundary | of area          | 1   | and 2 at | buses 1,3, | and 8 cause     |
|                    | 0.090124 |     |     | Inverter  | Delta |     | 12 0.487 |                 |                  |     |          |            |                 |
0.090124 Inverter Delta 25 0.336 thisbifurcation.Notably,ScenarioCexhibitsamorebalanced
0.090124 Inverter Delta 18 0.038 participation between data centers and inverters, with the data
|     | 0.090124 |     |     | Inverter | Delta |     | 21 0.021 |     |     |     |     |     |     |
| --- | -------- | --- | --- | -------- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- |
centeratbus3havingthehighestparticipationfactorof0.393,
|     | 0.090124 |     |     | Datacenter | Delta |     | 9 0.020 |                  |     |              |     |        |                  |
| --- | -------- | --- | --- | ---------- | ----- | --- | ------- | ---------------- | --- | ------------ | --- | ------ | ---------------- |
|     |          |     |     |            |       |     |         | closely followed | by  | the inverter | at  | bus 12 | with 0.379. This |
TABLEII:Participationfactorsforthemostunstablemodein analysisprovidescriticalinsightsfortargetedcontrolstrategies
| Scenario           | B                  |                    |           |               |          |                    |          | and system | reinforcement | planning. |     |     |     |
| ------------------ | ------------------ | ------------------ | --------- | ------------- | -------- | ------------------ | -------- | ---------- | ------------- | --------- | --- | --- | --- |
| EigenvalueRealPart |                    |                    |           | Component     | State    | Bus                | PF       |            |               |           |     |     |     |
|                    | 0.065186           |                    |           | Inverter      | Delta    |                    | 3 0.406  |            |               |           |     |     |     |
|                    | 0.065186           |                    |           | Inverter      | Delta    |                    | 1 0.280  |            |               |           |     |     |     |
|                    | 0.065186           |                    |           | Inverter      | Delta    |                    | 8 0.195  |            |               |           |     |     |     |
|                    | 0.065186           |                    |           | Inverter      | Delta    |                    | 27 0.036 |            |               |           |     |     |     |
|                    | 0.065186           |                    |           | Datacenter    | Delta    |                    | 20 0.018 |            |               |           |     |     |     |
| TABLE              | III: Participation |                    |           | factors       | for the  | most               | unstable | mode       |               |           |     |     |     |
| in Scenario        | C                  |                    |           |               |          |                    |          |            |               |           |     |     |     |
| EigenvalueRealPart |                    |                    |           | Component     | State    | Bus                | PF       |            |               |           |     |     |     |
|                    | 0.109327           |                    |           | Datacenter    | Delta    |                    | 3 0.393  |            |               |           |     |     |     |
|                    | 0.109327           |                    |           | Inverter      | Delta    |                    | 12 0.379 |            |               |           |     |     |     |
|                    | 0.109327           |                    |           | Inverter      | Delta    |                    | 16 0.055 |            |               |           |     |     |     |
|                    | 0.109327           |                    |           | Inverter      | Delta    |                    | 26 0.052 |            |               |           |     |     |     |
|                    | 0.109327           |                    |           | Inverter      | Delta    |                    | 23 0.022 |            |               |           |     |     |     |
| where              | ϕ                  | and ψ              | represent |               | the i-th | elements           | of       | the k-     |               |           |     |     |     |
|                    | ik                 |                    | ik        |               |          |                    |          |            |               |           |     |     |     |
| th right           | and                | left eigenvectors, |           | respectively, |          | and                | n is the | total      |               |           |     |     |     |
| number             | of state           | variables          |           | [31].         | The      | right eigenvectors |          | ϕ          |               |           |     |     |     |
k
| satisfy   | Aϕ k          | = λ k ϕ | k , while   | the          | left eigenvectors |              | ψ k       | satisfy |     |     |     |     |     |
| --------- | ------------- | ------- | ----------- | ------------ | ----------------- | ------------ | --------- | ------- | --- | --- | --- | --- | --- |
| ψTA=λ     | ψT.           |         |             |              |                   |              |           |         |     |     |     |     |     |
| k         | k             | k       |             |              |                   |              |           |         |     |     |     |     |     |
| The       | computational |         | procedure   |              | involves          | element-wise |           | multi-  |     |     |     |     |     |
| plication | of the        | right   | eigenvector |              | with              | the complex  | conjugate |         |     |     |     |     |     |
| of the    | corresponding |         | left        | eigenvector, | followed          |              | by taking | the     |     |     |     |     |     |
absolute value:
|     |     |     | P=|Φ⊙Ψ| |     |     |     |     | (28) |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
whereΦandΨarematricescontainingrightandlefteigen-
| vectors   | as columns,   |                  | ⊙ denotes |              | element-wise |                 | multiplication, |        |     |     |     |     |     |
| --------- | ------------- | ---------------- | --------- | ------------ | ------------ | --------------- | --------------- | ------ | --- | --- | --- | --- | --- |
| and ·     | represents    | complex          |           | conjugation. |              | Each            | column          | of the |     |     |     |     |     |
| resulting | participation |                  | factor    | matrix       | is           | then normalized |                 | such   |     |     |     |     |     |
| that the  | sum           | of participation |           | factors      |              | for each        | mode            | equals |     |     |     |     |     |
unity.Thisnormalizationensuresthatparticipationfactorscan
beinterpretedastherelativecontributionofeachstatevariable
| to the             | corresponding |             | eigenmode,  |                | facilitating | the           | identification |          |     |     |     |     |     |
| ------------------ | ------------- | ----------- | ----------- | -------------- | ------------ | ------------- | -------------- | -------- | --- | --- | --- | --- | --- |
| of dominant        |               | system      | components  |                | in modal     | behavior.     |                |          |     |     |     |     |     |
| The                | participation |             | factor      | analysis       | reveals      | the           | dominant       | state    |     |     |     |     |     |
| variables          | contributing  |             | to the      | most           | unstable     | eigenmode     |                | across   |     |     |     |     |     |
| three              | different     | scenarios.  | Tables      |                | I, II, and   | III           | present        | the top  |     |     |     |     |     |
| five participating |               | state       | variables   |                | for the      | most critical | unstable       |          |     |     |     |     |     |
| mode               | in each       | scenario,   | focusing    |                | on           | the rotor     | angle          | states   |     |     |     |     |     |
| (Delta)            | that exhibit  |             | the highest | participation  |              | factors.      |                |          |     |     |     |     |     |
| The                | results       | demonstrate |             | that rotor     | angle        | deviations    |                | (Delta)  |     |     |     |     |     |
| of inverters       | and           | data        | centers     | are            | the primary  |               | contributors   | to       |     |     |     |     |     |
| system             | instability   | across      |             | all scenarios. |              | In Scenarios  |                | A and    |     |     |     |     |     |
| B, inverter-based  |               | resources   |             | dominate       | the          | participation |                | factors, |     |     |     |     |     |
| with               | buses 12      | and         | 25 in       | Scenario       | A,           | and           | buses 3        | and 1    |     |     |     |     |     |