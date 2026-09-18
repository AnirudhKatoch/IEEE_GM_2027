2026 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE)
Challenges of Centralized Remote Power Smoothing
Strategies for AI Data Center Loads
∗ ∗ ∗ ∗
Abdullah Alfarra , Abdallah F. El-Hamalawy , Ahmed Abd Elaziz Elsayed , Hany E.Z. Farag
∗
EECS Department, York University, Toronto, Ontario, Canada
AbstractÐThe rapid expansion of the Artificial Intelligence In this regard, existing AI workload power smoothing tech-
(AI) industry has driven large-scale growth of AI-oriented Data niques can be broadly categorized into three groups: 1)
Centers (AIDCs) and their integration into power systems. In
software-basedmethods,2)GPU-levelpowerrampcontrol,and
additiontotheirhighenergydemand,AIDCsrelyonaccelerator-
3) hardware-based smoothing using Energy Storage Systems
based infrastructure, including GPUs, TPUs, and NPUs, which
exhibit significant power variability due to the synchronized (ESS) [5]. Software-based approaches attempt to introduce
nature of AI training workloads. This synchronized operation virtual or dummy computational loads on accelerator infras-
produces fast and large power fluctuations that propagate to the tructure during transitions between computational stages. The
regional grid and affect power system frequency stability. There-
objective is to reduce abrupt power drops by maintaining a
fore,thispaperinvestigatestheimpactofultra-fastvaryingAIDC
moreconstantutilizationlevel.However,thisstrategyoftenre-
loads on power system stability under different power smoothing
strategiesandhighlightsthenewchallengesthatdistinguishAIDC ducesoveralltrainingenergyefficiencyandintroducescommu-
loads from traditional large industrial demand. Results show nication and monitoring overhead due to the additional coordi-
that AIDC operation increases frequency deviation and Rate-of- nationandkernel-levelmodificationsrequiredinAIworkloads.
Frequency-Change(ROFC)by20.15%and153.29%,respectively,
Similarly, GPU-based power ramp constraint methods enforce
even when the AIDC represents only 40% of a traditional load.
controlled power transitions at the device level. When GPU
Applying local smoothing reduces these increases to 4.43% and
5.26%,respectively,butrequiresoversizingdedicatedlocalEnergy powerfallsbelowaspecifiedthresholdduringtrainingorwhen
Storage Systems (ESS). In contrast, Centralized Remote Power entering idle states, artificial burn loads are introduced and
Smoothing reduces ESS capacity requirements but exhibits a powerisreducedgraduallytosatisfyramp-ratelimits.Although
notableperformancedegradationduetothehighermagnitudeand
effectiveinlimitingfastpowerchanges,thisapproachincreases
frequencyofAIDCpowerfluctuations.Thesefindingsdemonstrate
thermalstress,leadstoadditionalpowerlosses,andaccelerates
thatconventionalsmoothingapproachesarenotfullyadequatefor
the emerging dynamic behavior of AIDC loads. hardware aging, thereby shortening GPU lifetime. The third
Index TermsÐAI Data Center, AI Training Workload, Power category relies on external hardware-based smoothing using
Smoothing, Remote Power Smoothing, Frequency Regulation ESS. In this approach, fast charge±discharge cycles buffer the
AIDC load, effectively filtering short-term power fluctuations.
I. INTRODUCTION While technically effective, this solution introduces substantial
capital cost and accelerated ESS degradation, primarily due to
Recent advances in artificial intelligence (AI) have trans- theextremelyhighcyclingfrequency,whichcanreachmillions
formed it from an academic discipline into a trillion-dollar of cycles per year [5].
industrial sector, driving rapid expansion of AI-oriented data
Recalling the ESS technologies commonly used for smooth-
center (AIDC) infrastructure and associated electricity demand
ing the power output of Renewable Energy Sources (RESs),
[1].Asaresult,globaldatacenter(DC)electricityconsumption
several storage options are available, such as battery ESSs,
is projected to increase from 415 TWh in 2024 to nearly
flywheel ESSs, and supercapacitors [6]. Although these tech-
945TWhby2030,accountingforapproximately10%ofglobal
nologies have proven effective in smoothing RES power pro-
electricity demand growth [2]. Beyond their large energy re-
files, they require additional capital investment and further quirements,AIDCsexhibituniqueelectricalcharacteristicsthat
considerations when used with AIDCs. Specifically, given the
distinguish them from conventional loads. They rely heavily
high cycling frequency associated with AIDCs, the use of
on hardware accelerators such as Graphic Processing Units
local ESSs for power smoothing is expected to experience
(GPUs), Tensor Processing Units (TPUs), and Neural Process-
significant degradation, resulting in a substantially reduced ingUnits(NPUs),whichoperateatextremelyhighpowerden-
lifetime. Further, the large magnitude of power fluctuations
sities and experience rapid transitions between computational
increases the likelihood of oversizing local ESSs associated
states. These workload-driven transitions produce significant
withAIDCs,therebyresultinginhighercapitalandoperational
short-term power fluctuations, with ramp rates reaching up to
costs.
±1.9 p.u./sec [3]. When such fast power variability is coupled
with the rapidly increasing peak demand of AIDCs, projected To reduce the heavy reliance on local ESSs, a recent study
to grow from 751 MW in 2025 to 3.3 GW by 2027, these [7], conducted by some of the work’s authors, proposes a
facilities begin to resemble large, highly dynamic industrial Centralized Remote Power Smoothing (CRPS) configuration
loads, which creates a compounded stress on regional power in which the smoothing burden of different Fluctuating Power
systems [4]. Addressing this emerging challenge requires new SourcesandLoads(FPSLs),includingRESsandlargevariable
operational strategies and power smoothing approaches. loads, is addressed collectively. In this configuration, power
979-8-3315-8840-3/26/$31.00 ©2026 IEEE 30
39301611.6202.05186ECECC/9011.01
:IOD
|
EEEI
6202©
00.13$/62/3-0488-5133-8-979
|
)ECECC(
gnireenignE
retupmoC
dna
lacirtcelE
no
ecnerefnoC
naidanaC
EEEI
6202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:26:24 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE)
III. LOCALVERSUSCENTRALIZEDREMOTEPOWER
| 1   |     |     | 0.7 |     |     |     |     |     |     |     |           |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
| (a) |     |     |     |     |     |     |     |     |     |     | SMOOTHING |     |     |     |     |
| 2   |     |     |     | (b) |     |     |     |     |     |     |           |     |     |     |     |
0.8 0.6
| xednI UPG 3 |     |     | ).u.p( rewoP |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therearetwopowersmoothingconfigurations:conventional
| 4   |     |     | 0.5 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.6 local power smoothing and the recently proposed CRPS [7].
| 5   |     |     | 0.4 |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Stage I Stage Thissectionsummarizesthetwoapproachesandhighlightsthe
6
|     |          |     | 0.4 0.3 |         | II  |     |             |     |          |                 |     |     |     |     |     |
| --- | -------- | --- | ------- | ------- | --- | --- | ----------- | --- | -------- | --------------- | --- | --- | --- | --- | --- |
| 7   |          |     |         |         |     |     | differences |     | in their | implementation. |     |     |     |     |     |
|     | Stage II |     |         | Stage I |     |     |             |     |          |                 |     |     |     |     |     |
| 8   |          |     | 0.2     |         |     |     |             |     |          |                 |     |     |     |     |     |
0.2
10 20 30 (p.u.) 10 20 30 40 A. Conventional Local Power Smoothing
Time (Sec)
Time (Sec)
|             |             |          |          |      |         |       |     | The conventional |     | local | power | smoothing |     | is typically | per- |
| ----------- | ----------- | -------- | -------- | ---- | ------- | ----- | --- | ---------------- | --- | ----- | ----- | --------- | --- | ------------ | ---- |
| Fig. 1: LLM | AI training | workload | on GB200 | node | a) GPUs | power |     |                  |     |       |       |           |     |              |      |
synchronization within the node, b) Aggregated GB200 node power. formed by associating each FPSL with an SF connected to the
|     |     |     |     |     |     |     | same | bus. | In this | configuration, |     | assuming | there | are N | FPSLs, |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ------- | -------------- | --- | -------- | ----- | ----- | ------ |
thepoweroutputofeachFPSL,Pt
,issmoothedthrough
FPSL,n
measurements from the FPSLs are transmitted to the re- power injection from its associated SF. The smoothing power
gionalcontrolcenterviaahigh-speedcommunicationnetwork. setpoint of each SF is computed as the difference between the
smoothedpowertarget,Pt
Then, a central CRPS controller calculates the total required ,andtheFPSLpower,suchthat:
ref,n
smoothing power and distributes the smoothing burden among ∗,t t −Pt ∀t∈T
|     |     |     |     |     |     |     |     | P   | =P  | ref,n | FPSL,n |     |     | ∧ n∈N. | (1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --- | ------ | --- |
SF,n
multiple Smoothing Facilities (SFs) geographically dispersed This setpoint represents a power reference for the SF and is
| acrossthepowergrid.TheparticipatingSFsincludeESSs,fast |     |     |     |     |     |     |          |     |          |        |     |        |       | Pt  |          |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------ | --- | ------ | ----- | --- | -------- |
|                                                        |     |     |     |     |     |     | distinct |     | from the | actual | SF  | output | power | ,   | which is |
dispatchable loads, and generating units. The CRPS approach SF,n
|     |     |     |     |     |     |     | subject |     | to dynamic | behavior |     | and operational |     | constraints. | Con- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---------- | -------- | --- | --------------- | --- | ------------ | ---- |
is proposed as an ancillary service that fulfills smoothing sequently, the SF output power may deviate from its setpoint,
| requirements | by leveraging |     | existing | facilities | across | the power |              |     |        |           |     |            |     |      |            |
| ------------ | ------------- | --- | -------- | ---------- | ------ | --------- | ------------ | --- | ------ | --------- | --- | ---------- | --- | ---- | ---------- |
|              |               |     |          |            |        |           | particularly |     | during | transient |     | conditions | or  | when | saturation |
grid, thereby avoiding the need to establish new local infras- limits are reached. The smoothed power target, P∗t, can be
n
tructure at each FPSL. Yet, the previous work [7] considered computed using different methods; one common approach is
| only FPSLs | of conventional |     | varying   | loads | and RESs,  | without |          |           |       |          |         |      |      |             |       |
| ---------- | --------------- | --- | --------- | ----- | ---------- | ------- | -------- | --------- | ----- | -------- | ------- | ---- | ---- | ----------- | ----- |
|            |                 |     |           |       |            |         | to       | calculate | it as | a moving | average | over | a    | time window | τ, as |
| addressing | the potential   | of  | smoothing | the   | ultra-fast | power   | follows: |           |       |          |         |      |      |             |       |
| variations | of AIDCs using  | the | proposed  | CRPS  | approach.  |         |          |           |       | 1 t      |         |      |      |             |       |
|            |                 |     |           |       |            |         |          |           | t     |          | t       |      | ∀t∈T |             |       |
|            |                 |     |           |       |            |         |          | P         | =     |          | P       | dt   |      | ∧ n∈N.      | (2)   |
As such, this paper is the first to highlight the differences ref,n τ Z FPSL,n
t−τ
betweensmoothingthewell-knownpowerfluctuationsofRESs
|             |              |       |     |                |       |       | B.  | Centralized |     | Remote | Power | Smoothing |     |     |     |
| ----------- | ------------ | ----- | --- | -------------- | ----- | ----- | --- | ----------- | --- | ------ | ----- | --------- | --- | --- | --- |
| and varying | conventional | loads | and | the ultra-fast | large | power |     |             |     |        |       |           |     |     |     |
variationsofAIDCs.Additionally,thisworkisthefirsttoassess The CRPS is a prospective ancillary service that is sup-
the effectiveness and identify the challenges of the recently posedtosmooththepowerfluctuationsofdifferentintermittent
proposed CRPS approach in mitigating the AIDCs’ ultra-fast sourcesandloadsinacollectivemannerincorporationwiththe
power variations. existing Automatic Generation Control (AGC). Unlike conven-
|     |     |     |     |     |     |     | tional | local | smoothing, |      | in the | CRPS, | there  | is no | dedicated |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---------- | ---- | ------ | ----- | ------ | ----- | --------- |
|     |     |     |     |     |     |     | SF     | for   | each FPSL. | Yet, | the    | power | of all | FPSLs | is sent   |
II. AIDATACENTERWORKLOADSANDPROBLEM via a fast, large-scale communication network to the regional
DESCRIPTION
|     |     |     |     |     |     |     | control   |     | center, | which collectively |                  | calculates |               | the total | required |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ------------------ | ---------------- | ---------- | ------------- | --------- | -------- |
|     |     |     |     |     |     |     | smoothing |     | power   | and                | then distributes |            | the smoothing |           | power to |
AI training workloads represent a new class of loading different participating SFs. As such, the CRPS approach can
conditions in AIDC infrastructure. In addition to their high meet smoothing requirements by leveraging existing facilities
power densities and intensive reliance on accelerator-based (e.g., ESSs) across the power grid, thereby avoiding the need
hardware, these workloads operate in a highly synchronized to establish new local SFs for each FPSL. Additionally, CRPS
manner. Specifically, large numbers of accelerators transition benefits from aggregating the power profiles of multiple FP-
|                |         |          |             |     |         |           | SLs, | as  | the power | of  | one FPSL | may | increase | while | another |
| -------------- | ------- | -------- | ----------- | --- | ------- | --------- | ---- | --- | --------- | --- | -------- | --- | -------- | ----- | ------- |
| simultaneously | between | distinct | operational |     | phases, | including |      |     |           |     |          |     |          |       |         |
computation, communication, and information storage stages. decreases, resulting in lower overall power fluctuations and
This synchronized operation amplifies aggregate power swings reduced smoothing requirements.
atthefacilitylevel,asmanydeviceschangepowerstatesatthe Fig. 2 shows a portion of a power grid (controlled area),
same time rather than independently. Fig. 1 illustrates the AI Area , and the corresponding AGC and CRPS controller. As
i
trainingworkloadofaLargeLanguageModel(LLM)executed shown in the figure, the system has G conventional generators
onaGB200node[8].AsshowninFig.1(a),GPUswithinthe participating in AGC, N FPSLs, and M SFs participating in
node operate in a highly synchronized manner, transitioning CRPS. The N FPSLs send their power measurement to the
collectively between high and low power stages, including regional control center (i.e., CRPS controller), and the M
computational (Stage I) and communication (Stage II) stages. SFs receive the smoothing power setpoints from the controller.
When this synchronized behavior is aggregated at the node As indicated in the figure, the CRPS controller acts as a
level,itproducesburstsinpowerdemandandsignificantshort- feedforward component that mitigates the power disturbances
term power variations over very small time scales, as depicted employed by the FPSLs before being reflected to the system’s
in Fig. 1 (b). frequency. Further, in this way, AGC requirements are limited
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:26:24 UTC from IEEE Xplore.  Restrictions apply.
31

2026 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE)
|     |     |     | Fig. | 2: Architecture |     | of the | centralized | power smoothing |     | ancillary | service. |     |     |     |     |
| --- | --- | --- | ---- | --------------- | --- | ------ | ----------- | --------------- | --- | --------- | -------- | --- | --- | --- | --- |
to other non-measurable disturbances rather than being con- responsible for following the CRPS controller setpoints; if an
sumed by the measurable fluctuations of the FPSLs. SF is unable to do so, it should indicate that it is unavailable
The CRPS controller calculates the total fluctuating power for participation in CRPS during the given assignment period.
Pt Consequently, the grid operator can assign smoothing tasks to
| injected | into the | system, | ,   | by summing | the | power | outputs |     |     |     |     |     |     |     |     |
| -------- | -------- | ------- | --- | ---------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
FP
| of the N | FPSLs | at time | t as follows: |     |     |     |     | other available |     | SFs. |     |     |     |     |     |
| -------- | ----- | ------- | ------------- | --- | --- | --- | --- | --------------- | --- | ---- | --- | --- | --- | --- | --- |
N
|     |     | t   | t       | ∀t∈T. |     |     |     |     |     |                       |     |     |     |     |     |
| --- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
|     |     | P = | P       |       |     |     | (3) |     | IV. | CASESTUDIESANDRESULTS |     |     |     |     |     |
|     |     | F P | F PSL,n |       |     |     |     |     |     |                       |     |     |     |     |     |
X=1
|                           |                 | n         |       |                           |     |                  |           | To evaluate    |        | the operational |     | challenges |         | associated | with         |
| ------------------------- | --------------- | --------- | ----- | ------------------------- | --- | ---------------- | --------- | -------------- | ------ | --------------- | --- | ---------- | ------- | ---------- | ------------ |
| Then the                  | total smoothing |           | power | requirement               |     | (i.e., smoothing |           |                |        |                 |     |            |         |            |              |
|                           |                 |           |       |                           |     |                  |           | smoothing      | the    | high-magnitude  |     | ultra-fast |         | power      | fluctuations |
| powersetpoint),denotedbyP |                 |           | ∗,t   | ,isdefinedasthedifference |     |                  |           |                |        |                 |     |            |         |            |              |
|                           |                 |           | C R   | P S                       |     |                  |           |                |        |                 |     |            |         |            |              |
|                           |                 |           |       |                           | t   |                  |           | characteristic | of     | the AIDCs,      |     | six case   | studies | were       | conducted    |
| between                   | the total       | smoothed  | po    | w e r target              | P   | and              | the total |                |        |                 |     |            |         |            |              |
|                           |                 |           |       |                           | ref |                  |           | on the IEEE    | 39-bus | benchmark       |     | system     | shown   | in         | Fig. 3. As   |
| fluctuating               | power           | as below: |       |                           |     |                  |           |                |        |                 |     |            |         |            |              |
∗,t t −Pt ∀t∈T illustratedinthefigure,threeFPSLsareconnectedtobuses16,
|     | P   | =P  |     |     |     |     | (4a) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
CRPS ref FP 32, and 38. The FPSLs at buses 32 and 38 correspond to wind
where,
powerplants,whereastheFPSLatbus16representsaload.In
t
|     |     | 1   |     |     | ∀t∈T. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P t = P t dt (4b) Cases 1, 3, and 5, this load is modeled as a conventional load
|     |     | ref τ | Z   | FP  |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t−τ of 300 MW, whereas in Cases 2, 4, and 6, it is modeled as an
Here, τ denotes the smoothing time window in seconds. AIDC load of 120 MW. Seven SFs are optionally connected
The total smoothing power setpoint, P ∗,t , is then dis- to buses 16, 32, 38, 4, 7, 22, and 39, depending on the case
CRPS
|     |     |     |     |     |     |     |     | study. Specifically, |     | Cases | 1 and | 2 represent |     | the base | scenarios |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ----- | ----------- | --- | -------- | --------- |
tributedamongtheMSFsbasedontheirratedassignedpower
for smoothing. As such, the contribution of each SF m (i.e., without any power smoothing configuration; therefore, none of
∗,t ∗,t the SFs are in operation. Cases 3 and 4 employ conventional
| P ) | in P | is calculated |     | as a | percentage | of  | its rated |     |     |     |     |     |     |     |     |
| --- | ---- | ------------- | --- | ---- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
SF,m CRPS local power smoothing, in which only the SFs at buses 16,
| assigned | power, | Prate , | allocated | for | CRPS, | relative | to the |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | --------- | --- | ----- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
SF,m
|             |       |             |     | M     |     |          |     | 32, and | 38 are | active. | In Cases | 5   | and 6, | CRPS | is utilized; |
| ----------- | ----- | ----------- | --- | ----- | --- | -------- | --- | ------- | ------ | ------- | -------- | --- | ------ | ---- | ------------ |
| total rated | power | of all SFs, |     | Prate | as  | follows: |     |         |        |         |          |     |        |      |              |
m=1 SF,m accordingly, only the remote SFs at buses 4, 7, 22, and 39 are
|     |     | Prate | ∗,Pt |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
P
P ∗,t = SF,m CRPS ∀ m∈M∧t∈T (5) in operation. Table I summarizes the conducted case studies.
|     | SF,m | M   |       |     |     |     |     |                                                    |     |     |     |     |     |     |     |
| --- | ---- | --- | ----- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |      |     | Prate |     |     |     |     | Thepowerprofilesoftheconventionalloadatbus16andthe |     |     |     |     |     |     |     |
|     |      | m=1 | SF,m  |     |     |     |     |                                                    |     |     |     |     |     |     |     |
It is worth notinPg that, unlike conventional local smoothing two wind power plants at buses 32 and 38 are based on real,
strategies, introducing CRPS as an ancillary service does not high-resolution power data for a conventional load and wind
require explicitly accounting for the energy limits of partici- power plants in Ontario, Canada [7]. The power profile of the
pating SFs in the CRPS controller. This is because each SF is AIDCloadatbus16ismodeledasacompositeofITandnon-
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:26:24 UTC from IEEE Xplore.  Restrictions apply.
32

2026 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE)
AIDC Power Category Distribution
Others (Cx-C) (2.3%)
Standard Multi-tenant
Cooling & Chiller
|     |     |     |     |     |     |     |     |     |  (Cx-B) (24.0%) |     |     |     |  Systems (17.0%) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ---------------- | --- | --- |
LLM Training
(Cx-A) (56.7%)
Standard Multi-tenant (Cx-B)
LLM Training (Cx-A)
Cooling & Chiller Systems
Others (Cx-C)
|     |     |     |     |     |     |     |     | Fig. 4: AIDC | Power | load | distribution | summary | of  | the AIDC | at bus |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ---- | ------------ | ------- | --- | -------- | ------ |
16.
|                |      |         |        |             |     |         |        | seconds | of each | simulationwere |     | excluded | to eliminate |     | start-up |
| -------------- | ---- | ------- | ------ | ----------- | --- | ------- | ------ | ------- | ------- | -------------- | --- | -------- | ------------ | --- | -------- |
| Fig. 3: Single | line | diagram | of the | IEEE 39-bus | New | England | bench- |         |         |                |     |          |              |     |          |
transients.Also,inthisstudy,thepowerflowacrossthetielines
| mark system | [9]. |     |     |     |     |     |     |            |     |        |             |            |     |                  |     |
| ----------- | ---- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ----------- | ---------- | --- | ---------------- | --- |
|             |      |     |     |     |     |     |     | connecting | the | system | to adjacent | controlled |     | areas is assumed |     |
TABLE I: Summary of the simulation case studies constant.Consequently,theAreaControlError(ACE)becomes
CaseNo. TypeofLoadatBus16 SmoothingTechnique directly proportional to the system frequency deviation ∆F.
|       |     |                  |     |     |       |     |     | Hence,                                   | two key | metrics | are    | utilized to  | assess       | the smoothing |        |
| ----- | --- | ---------------- | --- | --- | ----- | --- | --- | ---------------------------------------- | ------- | ------- | ------ | ------------ | ------------ | ------------- | ------ |
| Case1 |     | Conventionalload |     |     | None  |     |     |                                          |         |         |        |              |              |               |        |
|       |     |                  |     |     |       |     |     | performance                              | and     | the     | effect | of the power | fluctuations |               | on the |
| Case2 |     | AIDCload         |     |     | None  |     |     |                                          |         |         |        |              |              |               |        |
| Case3 |     | Conventionalload |     |     | Local |     |     |                                          |         |         |        |              |              |               |        |
|       |     |                  |     |     |       |     |     | electric                                 | grid.   |         |        |              |              |               |        |
| Case4 |     | AIDCload         |     |     | Local |     |     |                                          |         |         |        |              |              |               |        |
|       |     |                  |     |     |       |     |     | 1) CumulativeAbsoluteFrequencyDeviation: |         |         |        |              |              | Thefirstmet-  |        |
| Case5 |     | Conventionalload |     |     | CRPS  |     |     |                                          |         |         |        |              |              |               |        |
Case6 AIDCload CRPS ric is the cumulative absolute frequency deviation, |∆F|,
|     |     |     |     |     |     |     |     | which quantifies |         | the          | total magnitude | of        | frequency  | exPcursions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ------------ | --------------- | --------- | ---------- | ----------- | --- |
|     |     |     |     |     |     |     |     | from the         | nominal | steady-state |                 | value. It | is defined | as:         |     |
IT loads. The IT load is partitioned into three sectors: i) Cx- T
A, which represents 56.7% of the AIDC load and is allocated |∆F|= |f −f(t)|, (6)
n
to LLM training workloads; ii) Cx-B, which represents 24% X X=t1
t
|             |      |     |             |     |             |              |     | where T | denotes | the | total | number of | time | samples | in the |
| ----------- | ---- | --- | ----------- | --- | ----------- | ------------ | --- | ------- | ------- | --- | ----- | --------- | ---- | ------- | ------ |
| of the AIDC | load | and | corresponds |     | to standard | multi-tenant |     |         |         |     |       |           |      |         |        |
customerworkloadsandiii)Cx-C,whichrepresents2.3%ofthe evaluated period, t1 is the first time sample after 100 seconds
|                                                    |         |        |            |     |           |            |     | of simulation, |     | f(t) is      | the system | frequency | at  | sample t, | and f |
| -------------------------------------------------- | ------- | ------ | ---------- | --- | --------- | ---------- | --- | -------------- | --- | ------------ | ---------- | --------- | --- | --------- | ----- |
| AIDCloadandcorrespondstootherITloads.Thenon-ITload |         |        |            |     |           |            |     |                |     |              |            |           |     |           | n     |
|                                                    |         |        |            |     |           |            |     | is the nominal |     | steady-state | frequency. |           |     |           |       |
| accounts                                           | for 17% | of the | total load | and | primarily | represents | the |                |     |              |            |           |     |           |       |
facility’s cooling and chiller systems. The LLM power profile 2) Sum of Absolute Rate of Change of Frequency: The
|     |     |     |     |     |     |     |     | second metric |     | assesses | frequency | volatility | by  | calculating | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --------- | ---------- | --- | ----------- | --- |
(i.e.,Cx-A)isadoptedfrom[8]forNVIDIAGB200node.The
powerprofileforotherIToperations(i.e.,Cx-B,andCx-C)and sum of the absolute rate of change of the system’s frequency
|         |         |             |      |     |             |         |     | |dF|, | and it | is defined | as: |     |     |     |     |
| ------- | ------- | ----------- | ---- | --- | ----------- | ------- | --- | ----- | ------ | ---------- | --- | --- | --- | --- | --- |
| cooling | systems | was derived | from | the | operational | records | of  | a dt  |        |            |     |     |     |     |     |
T
Canadian-based DC solutions provider. The total composition P dF ∇f(t)
| of the DC | power | is summarized |     | in Fig. | 4.  |     |     |     |     |           | =                    |                 | ,        |     | (7) |
| --------- | ----- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --------- | -------------------- | --------------- | -------- | --- | --- |
|           |       |               |     |         |     |     |     |     |     |           | (cid:12) dt (cid:12) | (cid:12) ∆t     | (cid:12) |     |     |
|           |       |               |     |         |     |     |     |     |     | X(cid:12) | (cid:12)             | t X=t1 (cid:12) | (cid:12) |     |     |
Based on the above load composition, the Power Usage (cid:12) (cid:12) (cid:12) (cid:12)
where∇denotesthen(cid:12)ume(cid:12)ricalgrad(cid:12)ientop(cid:12)eratorand∆tisthe
| Effectiveness | (PUE), | defined |     | as the | ratio of | the total | AIDC |     |     |     |     |     |     |     |     |
| ------------- | ------ | ------- | --- | ------ | -------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
simulationsamplingintervalusedfornumericaldifferentiation.
| power consumption   |          | to   | its IT power | consumption, |            | is      | calculated |              |            |       |        |                 |       |                 |     |
| ------------------- | -------- | ---- | ------------ | ------------ | ---------- | ------- | ---------- | ------------ | ---------- | ----- | ------ | --------------- | ----- | --------------- | --- |
|                     |          |      |              |              |            |         |            | Taken        | together,  | these | two    | metrics provide |       | a comprehensive |     |
| to be approximately |          | 1.2. | This         | value is     | consistent | with    | industry   |              |            |       |        |                 |       |                 |     |
|                     |          |      |              |              |            |         |            | quantitative | assessment |       | of the | impact of       | power | fluctuations    | on  |
| benchmarks          | reported | by   | leading      | providers,   |            | such as | Schneider  |              |            |       |        |                 |       |                 |     |
systemstability,whiletheaccompanyingtime-seriesfiguresof-
Electric[10],indicatingthatthegeneratedAIDCpowerprofile
feraqualitativevisualizationthatfurthervalidatesandclarifies
| is realistic | and aligned |           | with current | AIDC | power       | infrastructure |        |             |        |     |       |           |             |     |     |
| ------------ | ----------- | --------- | ------------ | ---- | ----------- | -------------- | ------ | ----------- | ------ | --- | ----- | --------- | ----------- | --- | --- |
|              |             |           |              |      |             |                |        | the dynamic | nature | of  | these | frequency | variations. |     |     |
| practices.   | The         | generated | profile      | is   | then scaled | up             | to 120 |             |        |     |       |           |             |     |     |
MW,reflectingtheactualpowerdemandrequirementsofhigh-
|              |             |            |          |     |     |     |     | B. Cases    | 1 and      | 2: The | ºAI     | Stability Penaltyº |              |      |       |
| ------------ | ----------- | ---------- | -------- | --- | --- | --- | --- | ----------- | ---------- | ------ | ------- | ------------------ | ------------ | ---- | ----- |
| density      | AI training | facilities | [11].    |     |     |     |     |             |            |        |         |                    |              |      |       |
|              |             |            |          |     |     |     |     | The initial | comparison |        | between | the                | conventional | load | (Case |
| A. Smoothing | Performance |            | Measures |     |     |     |     |             |            |        |         |                    |              |      |       |
1)andtheAIDCload(Case2)underscoresthecriticalstability
This section defines the performance indices and quanti- challenges inherent in integrating AIDC into the grid. Despite
tative measures utilized to facilitate a rigorous comparative the AIDC load representing only 40% of the conventional
analysis across the evaluated case studies. To ensure accurate load’s nominal magnitude, its impact on grid stability is dis-
measurement of the smoothing performance, the initial 100 proportionately severe.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:26:24 UTC from IEEE Xplore.  Restrictions apply.
33

2026 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE)
TABLE II: System frequency performance comparison for Cases 1±6
Case Study Smoothing Technique P|∆F| (Hz)a P|dF| (Hz/s)a
dt
Case 1: Conventional load None 221.8480 48.2125
Case 2: AIDC load None 266.5611 122.1126
Case 3: Conventional load Local 158.9107 38.8544
Case 4: AIDC load Local 165.9077 40.2270
Case 5: Conventional load CRPS 162.2975 39.2837
Case 6: AIDC load CRPS 183.2945 120.4919
a
ThefrequencydeviationsandrateofchangearetheabsolutesumoverthesimulationperiodasdefinedinIV-A.
Fig.5:ComparisonofsystemdynamicsbetweenCases1and2:a)sum
of power output of all FPSLs (P ), b) resultant system frequency Fig. 6: Comparison of the total smoothed power output of all FPSLs
deviation, and c) rate of change o
F
f
P
frequency.
and SFs (i.e., P
FP
+P N
n=1
P
SF,n
) for: a) Cases 1 and 3, and b)
Cases 2 and 4.
As illustrated in Fig. 5, the AIDC load exhibits high-
frequency, high-amplitude fluctuations that are absent in the
conventional load profile. These volatile dynamics exacerbate
frequency excursions, as evidenced by the frequency deviation
andrateofchangeoffrequencymetrics.Quantitatively,TableII
confirmsthattheAIloadincreasesthe |∆F|andthe |dF|
dt
by 20.15% and 153.29%, respectively.P P
C. Cases 3 and 4: AIDC Effect with Local Smoothing
Local smoothing was integrated into the system for both the
conventional load and the AIDC load, designated as Case 3
Fig. 7: Comparison of system dynamics between Cases 3 and 4:
and Case 4, respectively. The objective of this comparison is
a) net smoothed power output of all FPSLs and SFs (i.e., P +
t
A
o
ID
ch
C
ar
p
a
o
c
w
te
e
ri
r
ze
pro
th
fi
e
le
m
re
a
l
x
a
i
t
m
iv
u
e
m
to
a
a
ch
c
i
o
e
n
v
v
ab
en
le
tio
im
na
p
l
ro
lo
v
a
e
d
m
.
ent in the P N n=1 P SF,n ),b)resultantsystemfrequencydeviation,andc)r F at P eof
change of frequency.
The resultant smoothed power profiles are shown in Fig. 6.
AlthoughthepowerprofilesinCases3and4appeareffectively
smoothedcomparedwithCases1and2,respectively,Fig.7(a) spectralfootprintonthegridfrequencythatismoredifficultto
shows that the net smoothed power in Case 4 exhibits notable suppress than that of conventional loads and RESs.
high-frequency,low-amplituderipplesthatareabsentinCase3.
Further,asshowninFig.7(b)and(c),thefrequencydeviation
D. Cases 5 and 6: AIDC Effect with Centralized Smoothing
and rate of change under AIDC loading (Case 4) display
similarlow-amplituderipples,indicatingthattheAIDC’shigh- The CRPS approach recently proposed by [7] is applied in
frequency components are not fully suppressed. Cases5and6,replacingtheconventionallocalsmoothingused
Quantitative metrics detailed in Table II support this obser- in Cases 3 and 4. While [7] reported negligible differences
vation; the |∆F| and the |dF| for the AIDC are greater between local smoothing and CRPS, the integration of AIDC
dt
than those Pof the conventioPnal load by 4.43% and 5.26%, load introduces substantially higher volatility than previously
respectively. anticipated.AsillustratedinFig.8,althoughthepowerappears
These results highlight that, despite the high investments effectively smoothed in subplot (a), the system frequency
required for local smoothing of AIDCs discussed earlier in deviation and rate of change in subplots (b) and (c) exhibit
section I, the inherent volatility of AIDC demand leaves a substantial fluctuations.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:26:24 UTC from IEEE Xplore. Restrictions apply.
34

2026 IEEE Canadian Conference on Electrical and Computer Engineering (CCECE)
theultra-fastandhigh-magnitudepowerfluctuationsassociated
with AIDC loads.
V. CONCLUSION
This paper evaluated the grid stability impacts of the ultra-
fast, high-magnitude power variations introduced by AIDCs
dominated by NVIDIA GB200 nodes during LLM training.
Simulation studies on the IEEE 39-bus system confirmed that
AI training workloads exhibit a distinctly more volatile electri-
calsignaturethanconventionalindustrialloads.Resultsshowed
that although on-site local smoothing techniques improve the
AIDC power profile, their performance remains inferior to
Fig. 8: Comparison of system dynamics between Case 5 and Case
6: a) net smoothed power output of all FPSLs and SFs (i.e., P + that of traditional industrial demand, indicating that existing
FP
P M m=1 P SF,m ) b) resultant system frequency deviation, and c) rate smoothingapproachesareinsufficienttoaddresstheuniquedy-
of change of frequency. namicsofAItrainingloads.Furthermore,theCRPSframework
demonstratedlimitedeffectivenessinmitigatingtheseultra-fast
transients,withthefrequencyrateofchangeimprovingbyonly
1.33% compared to the unsmoothed case, revealing a clear
technical limitation of current centralized strategies. Overall,
the findings provide a critical warning: as high-density AIDC
training continues to scale, both traditional and centralized
smoothing architectures must be fundamentally enhanced to
preserve regional grid stability.
REFERENCES
[1] I. E. AGENCY, ªEnergy and ais.º https://www.iea.org/reports/
energy-and-ai,Apr.2025. Accessed:2025-1-1.
[2] S.Chen,ªDatacentreswillusetwiceasmuchenergyby2030Ðdriven
Fig. 9: System performance comparison for Cases 4 and 6: a) net by ai.º Nature, https://www.nature.com/articles/d41586-025-01113-z,
Apr.2025. Accessed:2025-1-15.
smoothed power output of all FPSLs and SFs, b) resultant system
[3] P. R. Houle Gan, ªBalance of power: A full-stack ap-
frequency deviation, and c) rate of change of frequency.
proach to power and thermal fluctuations in ml infrastruc-
ture.º Google, https://cloud.google.com/blog/topics/systems/
mitigating-power-and-thermal-fluctuations-in-ml-infrastructure, Feb.
This observed discrepancy between the smoothed power 2025. Accessed:2025-1-17.
[4] B. Smith, ªMade in wisconsin: The world’s most powerful ai data-
profiles and the corresponding system frequency fluctuations
center.ºMicrosoft,https://blogs.microsoft.com/on-the-issues/author/brad-
can be attributed to the different losses experienced by the smith-2/,Sept.2025.
power injected from FPSLs and that injected by the SFs, as [5] A.Jimenez-RuizandF.Milano,ªDatacentermodelfortransientstability
analysisofpowersystems,ºarXivpreprintarXiv:2505.16575,2025.
well as to the geographical displacement of remote SFs, which
[6] A. F. El-Hamalawy, H. E. Farag, R. Medal, C. MacNeil, E. Ahmed,
mayintroduceminorpowerpropagationdelays.Althoughthese D.Sohm,andI.El-Samahy,ªAreal±worldcasestudyforsmoothingwind
effects are present in the case of RESs and conventional power output using flywheel energy storage,º in 2024 IEEE Canadian
ConferenceonElectricalandComputerEngineering(CCECE),pp.507±
loads (i.e., Case 5), they become more pronounced under
511,IEEE,2024.
AIDC loading (i.e., Case 6) due to the significantly higher [7] A. F. El-Hamalawy, H. E. Farag, E. Ahmed, D. Sohm, and I. El-
magnitude and frequency of power fluctuations compared with samahy, ªA novel framework for centralized remote power smoothing
as a prospective ancillary service,º IEEE Transactions on Sustainable
scenariosinvolvingonlyRESsandconventionalloadvariations.
Energy,2025.
Quantitativemetricsfurthersubstantiatetheseobservations:the [8] A.A.E.Elsayed,A.A.Al-Obaidi,andH.E.Farag,ªCharacterizationof
|∆F| and the |dF| for the AIDC case (i.e., Case 6) high-resolutionaidatacentertrainingworkloadsonsingleandmultiple
dt gpunodes,º2025.
aPre higher than thPose of Case 5 by 12.96% and 207.69%,
[9] I. C. for a Smarter Electric Grid (ICSEG), ªIeee 39-bus system.º https:
respectively, as detailed in Table II. //icseg.iti.illinois.edu/ieee-39-bus-system/,2025. Accessed:2025-10-01.
While the results from Cases 3 and 4 confirmed that AIDC [10] Schneider Electric and NVIDIA, ªAi reference designs to enable adop-
tion:AcollaborationbetweenSchneiderElectricandNVIDIA,ºExecu-
loaddegradespowerqualitywhenitissmoothedlocallyon-site,
tiveReportSPD EB1 EN,SchneiderElectric,92025.
the performance of CRPS in Case 6 was further deteriorated [11] Skeleton Technologies, ªAi data center power smoothing ± why is
when compared by Case 4 as shown in Fig. 9. GrapheneGPUdifferent?,ºSkeletonBlog,82025.
These findings underscore the critical nature of AIDC
smoothing and serve as a critical warning regarding the lim-
itations of smoothing architectures in general and centralized
smoothing (i.e., CRPS) specifically. Despite the benefits of the
CRPS approach as a prospective ancillary service for reducing
AGC energy requirements and needed SFs infrastructure, as
noted in [7], its current form may be insufficient to address
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:26:24 UTC from IEEE Xplore. Restrictions apply.
35
Powered by TCPDF (www.tcpdf.org)