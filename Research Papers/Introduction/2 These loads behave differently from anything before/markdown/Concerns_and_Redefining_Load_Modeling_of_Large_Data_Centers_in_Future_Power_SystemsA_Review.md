2026 IEEE Green Technologies Conference (GreenTech)
Concerns and Redefining Load Modeling of Large
Data Centers in Future Power Systems—A Review
Sachinth Viththarachchige, Demy Alexander, Sarangan Rajendran, Arun Manoharan, and Visvakumar Aravinthan
Department of Electrical and Computer Engineering
Wichita State University
Wichita, KS, USA
sachinth@ieee.org
Abstract—The exponential rise of generative artificial intel- (CAGR) of 22% from 2023 to 2030, where the generative AI
ligence is driving an unprecedented surge in hyperscale data workloads will be the key driver with a CAGR of 39% alone
center capacity, creating novel stability challenges for future
[5].
power systems. Traditional load modeling approaches, largely
With these trends, comes a host of risks and challenges
based on induction motor and static load counterparts, are
inadequate for capturing the complex, control-driven dynamics to the power system stability and reliability. The grid has
of modern rectifier-interfaced data center facilities. This pa- already started experiencing some signs of stress that a set
per discusses data center behavior from a system perspective, of large DC loads can cause. For instance, on July 10, 2024,
identifying critical risks such as transient instability caused by
a fault on a 230 kV transmission line led to a subsequent
weak fault ride-through capabilities and oscillatory instability
sudden disconnection of 1500 MW of DC load from the driven by periodic artificial intelligence workload patterns. We
critiqueexistingstaticandcompositeloadmodelsandsuggestthe grid [6] that nearly initiated a byte blackout in the Dominion
requirement of a decision framework for selecting appropriate EnergyserviceareaofPJMinterconnection.Thisincidentwas
modelingdomains,basedonthecharacteristicsofthephenomena flaggedasanextremeoutlieragainsttypicalloadswingsinthe
under study. Finally, the paper outlines urgent industry needs,
region [7]. From a recent whitepaper from North American
emphasizing standardized blackbox modeling to overcome intel-
Electric Reliability Corporation (NERC) [8], Figure 2 shows
lectualpropertybarriersandthenecessityofhigh-resolutionfield
data for model validation to ensure power system integrity. the frequency response of the eastern internconnection during
Index Terms—Data centers, Load modeling, Oscillations, this incident in a six-minute window. The frequency had risen
Power system dynamics, Power system stability above the upper deadband of +0.036 Hz and stayed above
it for nearly a minute, which is a clear indication of the
I. INTRODUCTION
severity of the event in terms of stability of the bulk power
The generative artificial intelligence (AI) boom has in- system (BPS). Similar incidents related to large loads have
evitably led to an upcoming proliferation of large scale data been reported in the ERCOT region too [8].
centers(DCs)bothnationallyandglobally.Enablingtechnolo- These factors of rapid growth of large DC loads and their
gieslikebigdataanalytics,highperformancecloudcomputing emerging impacts on power system stability have made it
have caused this growing trend in demand for large DCs.
UnprecedentedloadgrowthdrivenbygenerativeAIhasshifted
the focus from existing enterprise-type DCs to hyperscale
facilities. Such a facility could easily consume 100 MW, if
not multiples of hundreds MW of electric power on a regular
basis [1]. Hence, the modern DCs are becoming key players
in future power systems.
Currently, the USA is the global leader in terms of the
number of the active DCs and the amount of data traffic
handledbythem.NorthernVirginia,Atlanta(Georgia),Dallas
(Texas), Silicon Valley (California) are some of the notable
hotspotsforconstructionofnewDCsintheUS[2].According
to a recent study by western electricity coordinating council
(WECC), DCs make up for 78% of the new large load
interconnectionrequestsqueueintheregion[3].Thetotalload
demand from these upcoming DCs is over 90% of the current
system peak demand. Similarly, 73% of the 2025 large load
queueintheERCOTregioncompriseofDCs[4].Asshownin
Fig. 1, the McKinsey & Company predicts that the global DC
capacity demand will rise at an compound annual growth rate Fig.1. Estimatedglobaldatacentercapacitydemand[5]
/26/$31.00 ©2026 IEEE
44617411.6202.58286hceTneerG/9011.01
:IOD
| EEEI
6202©
00.13$/62/6-4285-5133-8-979
|
)hceTneerG(
ecnerefnoC
seigolonhceT
neerG
EEEI
6202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:18 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
Fig.3. Componentsinatypicaldatacenter[10]
1) Server farm: The core of a DC, consisting of racks of
Fig. 2. Frequencyplot for Easterninterconnection duringthe 1500MW of servers that handle ICT service.
primarilydatacenterloadtransferincident[8] 2) Power supply equipment: This includes power condi-
tioning devices like uninterruptible power supply (UPS)
systems, power distribution units (PDUs). The primary
imperativetostudytheirdynamiccharacteristicsandbehavior
source of power is typically the utility grid that is
from a system perspective. We are reaching a point where the
connected to the DC through a high voltage or medium
traditional load modeling approaches would not be sufficient
voltage transformer. This utility connection is usually
to capture the dynamic phenomena associated with such large
connected to the UPS system with a bypass switch to
loads [9]. It is crucial to repurpose and enhance existing load
ensure continuous power supply to the DC in case of
models or develop new ones that can accurately represent the
grid disturbances.
behavioroflargeDCloadsundervariousoperatingconditions.
3) Backup generation: While UPS units are meant to pro-
This paper aims to provide insights into the requirement of
videtheDCwithpowerforshortperiodsoftime,backup
newdynamicloadmodelingapproachesforlargeDCloadsin
generationfromdieselgenerationmayprovidepowerfor
future power systems. It is noteworthy that this paper focuses
prolonged periods in case of utility grid failures.
on the system perspective of large DC loads rather than the
4) Energy storage: To match with the high flexibility of
efficiency or effectiveness of the internal DC operations.
the overall load demand from a DC, battery systems are
The paper is organized as follows: Section II discusses
usuallyusedasfurtherbackup,thatmaybecoupledwith
the technical characteristics of a large DC load. Section III
renewable energy sources.
delves into the dynamic phenomena and system stability risks
5) Cooling system: It is common for a DC to have a water
associated with large DC loads. Section IV explores load
chiller plant-based cooling system accompanied by a
modelingconsiderationsforlargeDCloads.SectionVoutlines
computer room air handler (CRAH). CRAH ensures
gaps and future needs pertaining to this area. Finally, Section
that the ambient temperature of the servers is within
VI concludes the paper.
an acceptable range.
II. TECHNICALCHARACTERISTICSOFALARGEDATA Amongtheelectricalelementslistedabove,theserverfarm,
CENTERLOAD and the cooling (air conditioning) system constitute the major
portionofalargeDCload.DependingonthescaleoftheDC,
A. Electrical Infrastructure of a Data Center
power consumption by the servers can be as high as 80% of
ADCconsistsofseveralkeycomponentsthatworktogether the total load of the DC facility [11].
to ensure efficient data processing, storage, and management.
B. Utility Grid Interface Behavior
These components include servers, networking equipment,
storage systems, cooling systems, power supply units, and After the PDUs distribute ac power towards the server
more. Figure 3 depicts a simplified configuration of a typical farm, power supply units (PSUs) convert ac power to dc
DC. Regardless of the type (conventional enterprise DCs or power by means of rectifiers, and feed the power to servers
hyperscaleDCs),thefundamentalcomponentsremainsimilar, [12]. However, some modern DCs may have dc PDUs. These
although the scale and complexity may vary significantly. A rectifier-basedelectronicloadsemploystringentpowerquality
DCprimarilyconsistsofthefollowingcomponentsthateither requirements such that the DC is set to switchover from
consume or supply electrical power [10]: the utility grid to local UPS-based power in case of grid
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:18 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
disturbances that cause voltage sags in the grid. This voltage 1) Inherent dynamics of the DC that encompass large
sensitivity that enforce power quality requirements in the DC rectifier-based electronic load elements, and control and
facility limits the fault ride-through (FRT) capability of the protection dynamics.
DC facility [11]. 2) FRT capability of the DC that is governed by power
|                |          |     |                 |          |     |     | quality | enforcement |     | or over-sensitive |     | power | condition- |
| -------------- | -------- | --- | --------------- | -------- | --- | --- | ------- | ----------- | --- | ----------------- | --- | ----- | ---------- |
| C. AI Workload | Profiles |     | and Consumption | Patterns |     |     |         |             |     |                   |     |       |            |
|                |          |     |                 |          |     |     | ing     | equipment.  |     |                   |     |       |            |
The behavior of AI workload profiles is a key factor that 3) Variability of AI workloads that is governed by user
| distinguishes | a hyperscale |     | AI DC | from a conventional |     | DC. |          |           |     |     |     |     |     |
| ------------- | ------------ | --- | ----- | ------------------- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- |
|               |              |     |       |                     |     |     | activity | patterns. |     |     |     |     |     |
The magnitude of load fluctuations of a single large DC or a Some of the prominent stability risks that emerge from
| few large | DCs could | be  | multiple | hundreds MW, | if  | not well |               |     |             |     |     |     |     |
| --------- | --------- | --- | -------- | ------------ | --- | -------- | ------------- | --- | ----------- | --- | --- | --- | --- |
|           |           |     |          |              |     |          | above factors | are | as follows, |     |     |     |     |
over1000MW,reflectinglargeandundesirableloadswingson
|     |     |     |     |     |     |     | A. Transient | Stability |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | --- | --- | --- | --- |
theBPSinthenearfuture[3].TheseAIworkloadpatternsare
governedbythefundamentalnatureofAIprocessesdrivenby As briefly discussed in Section I, Eastern interconnection
graphical processing units (GPUs). This can be conceptually and ERCOT have experienced massive load swing incidents
illustrated as shown in Fig. 4. that is caused by weak FRT behavior of large DC loads.
| The AI | workload | patterns | could | even vary | between | the |     |     |     |     |     |     |     |
| ------ | -------- | -------- | ----- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
TheintegrationofhyperscaleDCsintroducesdistincttransient
stages of AI computing [13]: Training, Fine-tuning, and In- stability risks driven by the voltage sensitivity of these facili-
ference. This can be observed in Fig. 5 that shows these ties.Unliketraditionalindustrialloadsdominatedbyinduction
various AI computing patterns on a single GPU, where a motors (IMs), which may stall but often remain connected
large DC would have hundreds of thousands of such GPUs. duringvoltagesags,rectifier-interfacedDCstendtoswitchover
AI workloads differ significantly from traditional cloud com- fromthegridtolocalpowersupply.Figure6showsapositive-
puting. Training workloads cause sustained high demand with sequence, phasor domain simulation results of two generators
periodicfluctuations,whileinferenceworkloadscreatebursty, losing synchronism and attaining a rotor angle instability due
stochastic power spikes. to a post-fault tripping of a nearby DC load [8].
III. DYNAMICPHENOMENAANDSYSTEMSTABILITY B. Oscillatory Stability
RISKSOFLARGEDATACENTERLOADS The integration of hyperscale DCs introduces novel oscil-
We can identify three facets of large DC loads that could latory stability risks that differ fundamentally from traditional
create the problems in the power grid: load behaviors. These risks manifest through two primary
|        |                                           |     |     |     |     |     | mechanisms:          | negative         |         | damping         | or resonance |            | caused by the    |
| ------ | ----------------------------------------- | --- | --- | --- | --- | --- | -------------------- | ---------------- | ------- | --------------- | ------------ | ---------- | ---------------- |
|        |                                           |     |     |     |     |     | control interactions |                  | of      | rectifier-based | power        | electronic | loads            |
|        |                                           |     |     |     |     |     | with the             | grid, and        | forced  | oscillations    | driven       | by         | the periodic     |
|        |                                           |     |     |     |     |     | nature of            | AI computational |         | workloads       | [8].         | We         | can categorize   |
|        |                                           |     |     |     |     |     | them as              | subsynchronous   |         | oscillations    | (SSOs).      |            |                  |
|        |                                           |     |     |     |     |     | 1) Resonance-based   |                  |         | oscillations:   | In           | 2017,      | low frequency    |
|        |                                           |     |     |     |     |     | resonance            | phenomenon       |         | of ∼11          | Hz was       | observed   | in a set of      |
|        |                                           |     |     |     |     |     | Meta DCs             | [12],            | which   | was clearly     | visible      | as         | an envelope      |
| Fig.4. | VariabilityandrampingofAIdemandprofile[3] |     |     |     |     |     |                      |                  |         |                 |              |            |                  |
|        |                                           |     |     |     |     |     | Fig. 6. Simulation   |                  | of loss | of synchronism  | of           | generators | after post-fault |
Fig.5. DifferentAIcomputingloadpatternsinasingleGPU[13] trippingofnearbydatacenter[8]
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:18 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
waveform in one of the representative measurement scopes these currents cause non-linear voltage drops across system
as shown in Fig. 7, in both current and voltage waveforms. impedances, resulting in voltage distortion that can propa-
The study [14] takes this subsynchronous resonance concern gate to neighboring industrial and residential customers [13].
onestepfurtherbyinvestigatinga∼14.7–14.8Hzoscillations In addition to low frequency resonance that was discussed
coming from a DC in Dominion Energy’s power system. Fur- previously, high frequency resonance phenomena have been
thermore,withthehelpofnon-paramtetricspectralanalysison observed in recent field observations in the 5–10 kHz range
historical data of similar grid instances, using power spectral [1]. Regardless of the range of these low or high frequency
|     |     |     |     |     | critical | mode | of the DC |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
densities (PSDs), the study frames a resonances, they can easily lead to catastrophic instability
in the range of 10–11 Hz with significantly low damping to when subjected to grid disturbances. Other power quality
be the root cause of the oscillations at ∼14.7–14.8 Hz. concernslikevoltageflickerarealsobecomingmorecommon
2) Forced oscillations: Unlike traditional stochastic loads, with the penetration of new large DC loads [8].
| AI training | and | fine-tuning |     | workloads | exhibit | highly | struc- |                                            |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --------- | ------- | ------ | ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|             |     |             |     |           |         |        |        | IV. LOADMODELINGCONSIDERATIONSFORLARGEDATA |     |     |     |     |     |     |     |
tured,periodicpowerconsumptionprofilesdrivenbysynchro-
CENTERLOADS
| nized Graphics |     | Processing | Unit | (GPU) | operations |     | [8]. Using |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ---- | ----- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
a modified WECC 179-bus system with multiple DCs having The anticipated rapid penetration of hyperscale DC loads
|            |             |     |           |      |              |     |          | necessitates | a   | fundamental |     | shift | in load | modeling | prac- |
| ---------- | ----------- | --- | --------- | ---- | ------------ | --- | -------- | ------------ | --- | ----------- | --- | ----- | ------- | -------- | ----- |
| stochastic | AI workload |     | profiles, | [15] | demonstrates |     | that DC- |              |     |             |     |       |         |          |       |
induced forced oscillations are not merely local; they can also tices. While traditional modeling frameworks have sufficed
|              |               |      |                |          |        |         |         | for decades,      |     | the distinct | electrical |                  | characteristics  |           | of DCs |
| ------------ | ------------- | ---- | -------------- | -------- | ------ | ------- | ------- | ----------------- | --- | ------------ | ---------- | ---------------- | ---------------- | --------- | ------ |
| manifest     | as inter-area |      | oscillation    | patterns | as     | shown   | in Fig. | 8,                |     |              |            |                  |                  |           |        |
|              |               |      |                |          |        |         |         | as highlighted    |     | by preceding |            | sections—largely |                  | dominated | by     |
| where GENROU |               | 9–12 | are generators |          | of the | system. |         |                   |     |              |            |                  |                  |           |        |
|              |               |      |                |          |        |         |         | power electronics |     | rather       | than       | rotating         | machines—require |           | new    |
C. Power Quality and Harmonics methodologies to capture their interaction with the BPS [9].
Historically,powersystemmodelingprioritizedthedetailed
| Unlike | linear | loads, | DCs rely | heavily | on non-linear |     | compo- |                |     |               |            |     |       |       |          |
| ------ | ------ | ------ | -------- | ------- | ------------- | --- | ------ | -------------- | --- | ------------- | ---------- | --- | ----- | ----- | -------- |
|        |        |        |          |         |               |     |        | representation |     | of generation | resources, |     | while | loads | were ap- |
nents,specifically,rectifier-basedPSUsforITserverracksand
|                     |             |          |        |            |          |          |             | proximated    | using              | simplified      |             | static          | representations. |             | Planners     |
| ------------------- | ----------- | -------- | ------ | ---------- | -------- | -------- | ----------- | ------------- | ------------------ | --------------- | ----------- | --------------- | ---------------- | ----------- | ------------ |
| variable            | frequency   | drives   | (VFDs) | for        | cooling  | systems, | which       |               |                    |                 |             |                 |                  |             |              |
|                     |             |          |        |            |          |          |             | relied on     | constant           | impedance,      |             | current,        | and              | power       | (ZIP) mod-   |
| draw non-sinusoidal |             | currents |        | and inject | harmonic |          | distortions |               |                    |                 |             |                 |                  |             |              |
|                     |             |          |        |            |          |          |             | els, assuming |                    | these algebraic |             | representations |                  | were        | sufficient   |
| into the            | grid. These | raise    | power  | quality    | concerns |          | originating |               |                    |                 |             |                 |                  |             |              |
|                     |             |          |        |            |          |          |             | for bulk      | system             | assessments.    |             | This paradigm   |                  | shifted     | following    |
| from large          | DCs         | [1].     | If not | mitigated  | by       | active   | filtering,  |               |                    |                 |             |                 |                  |             |              |
|                     |             |          |        |            |          |          |             | the August    | 10,                | 1996,           | WECC        | blackout,       | which            | revealed    | that         |
|                     |             |          |        |            |          |          |             | static models |                    | failed to       | capture     | the             | delayed          | voltage     | recovery     |
|                     |             |          |        |            |          |          |             | caused        | by the             | stalling        | of IMs      | [16].           | In response,     |             | the industry |
|                     |             |          |        |            |          |          |             | developed     | the                | composite       | load        | model           | (CLM).           | This        | framework    |
|                     |             |          |        |            |          |          |             | combines      | static             | load components |             | with            | differential     |             | equation-    |
|                     |             |          |        |            |          |          |             | based IM      | models,            | allowing        | planners    |                 | to simulate      | the         | transient    |
|                     |             |          |        |            |          |          |             | response      | of motor-dominated |                 |             | industrial      | and              | residential | loads        |
|                     |             |          |        |            |          |          |             | [17]. While   | the                | CLM             | represented | a               | significant      | advancement |              |
formotorloads,itrepresentselectronicloadsmerelyasastatic
constantpowercomponent.Thisrepresentationisincreasingly
|     |     |     |     |     |     |     |     | inadequate | for   | modern     | hyperscale |     | DCs, where | server        | racks |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---------- | ---------- | --- | ---------- | ------------- | ----- |
|     |     |     |     |     |     |     |     | fed by     | power | electronic | rectifiers |     | constitute | approximately |       |
80–90%ofthetotalload,withcoolingmotorscomprisingonly
|     |     |     |     |     |     |     |     | the remaining |                 | minority       | share.      |             |            |            |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------- | -------------- | ----------- | ----------- | ---------- | ---------- | ---------- |
|     |     |     |     |     |     |     |     | The           | core limitation |                | of applying |             | existing   | industrial | load       |
|     |     |     |     |     |     |     |     | models        | to DCs          | lies in        | the source  |             | of their   | dynamic    | behav-     |
|     |     |     |     |     |     |     |     | ior. The      | transient       | response       | of          | traditional | industrial |            | facilities |
|     |     |     |     |     |     |     |     | is governed   |                 | by the physics |             | of IMs,     | which      | is         | consistent |
Fig.7. Measuredlowfrequencyresonanceinadatacenterin2017[12] across manufacturers and well-understood. In contrast, the
|     |     |     |     |     |     |     |     | response         | of a | DC is | governed | by   | the proprietary |          | control |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | ----- | -------- | ---- | --------------- | -------- | ------- |
|     |     |     |     |     |     |     |     | (and protection) |      | logic | of its   | PSUs | and UPS         | systems. | Be-     |
causethesedevicesaresoftware-defined,theirbehaviorduring
|     |     |     |     |     |     |     |     | grid disturbances—such |     |     | as FRT, | current | limiting, |     | and voltage |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ------- | ------- | --------- | --- | ----------- |
recovery—canvaryvastlydependingonthemanufacturerand
|     |     |     |     |     |     |     |     | the specific | programming |        | of              | the active | front-end |         | rectifiers. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------ | --------------- | ---------- | --------- | ------- | ----------- |
|     |     |     |     |     |     |     |     | Current      | static      | models | fail to         | capture    | these     | complex | control     |
|     |     |     |     |     |     |     |     | loops, often | predicting  |        | unrealistically |            | fast      | fault   | recovery or |
|     |     |     |     |     |     |     |     | failing to   | simulate    | the    | disconnection   |            | of loads  | during  | voltage     |
Fig.8. Inter-areaoscillationbetweengenerators,inducedbydatacenters[15] sags. Consequently, high-fidelity modeling for DCs requires
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:18 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
moving beyond physics-based assumptions to control-based system. More accurate EMT models derived for operational
representations [3], [8], [18]. planning may be used to parametrize phasor domain models
The selection of the appropriate modeling domain depends to capture the slower dynamics which are of concern for
onthebandwidthofthephenomenabeingstudied.Thechoice BPS stability studies. The article [18] suggests a conceptual
may come in three different approaches: phasor domain, threshold whichwouldactasametrictodecidewhendetailed
electromagnetic transient (EMT), and hybrid approach [13]: models are needed so that the required dynamics would be
1) Phasor domain modeling: For BPS reliability studies captured with confidence. Inspired by [18] and [19], Fig. 9
| focusing | on electromechanical |     | dynamics | (0.1–10 | Hz), aggre- |            |                 |      |                 |                |
| -------- | -------------------- | --- | -------- | ------- | ----------- | ---------- | --------------- | ---- | --------------- | -------------- |
|          |                      |     |          |         |             | presents a | simple decision | tree | indicating when | to use each of |
gated phasor-domain models are generally sufficient. These above approaches.
models can represent the aggregate active and reactive power Modeling every individual server rack within a hyperscale
response of the facility to fundamental frequency voltage DC facility is computationally prohibitive. Effective modeling
variations. relies on aggregating components based on the hierarchy of
| 2) EMT | modeling: | For | assessments | involving | fast control |                |       |              |         |                     |
| ------ | --------- | --- | ----------- | --------- | ------------ | -------------- | ----- | ------------ | ------- | ------------------- |
|        |           |     |             |           |              | the facility’s | power | distribution | system. | For instance, thou- |
interactions, high-frequency resonance, low-frequency reso- sands of single-phase PSUs and three-phase UPS units can
nance (SSO), or weak grid interconnects, detailed EMT mod- be aggregated into a single equivalent converter model that
els are required. EMT simulation is particularly critical for captures the facility’s total electronic load dynamics [18].
evaluating protection systems and assess the capability of The CLM design philosophy can be adapted to aggregate
| the load | that it can | ride-through |     | unbalanced | faults without |             |            |        |               |                 |
| -------- | ----------- | ------------ | --- | ---------- | -------------- | ----------- | ---------- | ------ | ------------- | --------------- |
|          |             |              |     |            |                | either load | components | within | a DC facility | for plant-level |
tripping. studies, or multiple coherent DCs for BPS-level assessments.
3) Hybrid modeling: To trade-off between computational To address the AI workload concerns of large DC load
burden and accuracy, transmission planners and operational modeling, investigating the fusion of continuous and event-
planners may employ a hybrid approach using voltage-dip driven dynamics via a stochastic process-based approach [20]
contours.Inthismethodology,detaileddynamicmodels(CLM
|         |             |      |          |         |                   | would be | transformative. |     |     |     |
| ------- | ----------- | ---- | -------- | ------- | ----------------- | -------- | --------------- | --- | --- | --- |
| or EMT) | are applied | only | to loads | located | within a specific |          |                 |     |     |     |
voltage-dipthreshold(e.g.,>70%dip)relativetoafault,while
|     |     |     |     |     |     |     |     | V. FUTURENEEDS |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- |
loadsoutsidethiscontourremainrepresentedbyefficientstatic
models [19]. The integration of hyperscale DCs represents a paradigm
Ingeneral,theparamountimportanceiscapturingallcritical shift for grid planning (both long term and operational plan-
dynamicswithintheparticularpowersystemassessment.EMT ning), yet the industry lacks the standardized frameworks
approachcouldbecomeanoverkillduetoduetoitsdemanding required to model these loads with the same rigor applied to
modeling effort and high computational burden for a large generationresources.Toensurereliability,thefollowingfuture
Fig.9. Decisiontreetoselectbetweenphasor,EMT,andhybridloadmodelingapproaches
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:18 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
needs regarding data transparency, interconnection processes, REFERENCES
| and model | validation | must | be  | addressed. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[1] G.Ramani,Z.Hussain,W.Brown,andQ.Alsafasfeh,“Challengeswith
A primary barrier to accurate large DC load modeling is ModernDataCenters,DesignConsiderationsandRecommendedPower
theproprietarynatureofDCequipment.UnlikestandardIMs, System Studies,” in 2025 IEEE/IAS 61st Industrial and Commercial
PowerSystemsTechnicalConference(I&CPS),May2025,pp.1–7.
| the dynamic | response |     | of a DC | is governed |     | by the | proprietary |          |        |              |     |         |             |        |          |
| ----------- | -------- | --- | ------- | ----------- | --- | ------ | ----------- | -------- | ------ | ------------ | --- | ------- | ----------- | ------ | -------- |
|             |          |     |         |             |     |        |             | [2] CBRE | Group, | Inc., “North |     | America | Data Center | Trends | H1 2025: |
controllogicofPSUsandUPSunits,whichmanufacturersare AI and Hyperscaler Demand Lead to Record-Low Vacancy,” August
oftenreluctanttodiscloseduetointellectualproperty(IP)con- 2025. [Online]. Available: https://www.cbre.com/insights/reports/north-
america-data-center-trends-h1-2025
cerns. To overcome IP barriers, future standards should adopt [3] R. Quint, J. Zhao, and K. Thomas, “An Assessment of Large Load
frameworks similar to those used by the Australian Energy InterconnectionRisksintheWesternInterconnection,”WesternElectric-
Market Operator (AEMO) [21]. AEMO guidelines explicitly ityCoordinatingCouncil,ElevateEnergyConsulting,TechnicalReport,
Feb.2025.
| allow and | outline | procedures |     | for blackbox-ing, |     | compiling, | or  |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | --- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[4] S.Kimball,“Red-hotTexasisgettingsomanydatacenterrequeststhat
encrypting EMT models. This approach allows manufacturers experts see a bubble,” cnbc.com. https://www.cnbc.com/2025/12/12/ai-
data-center-flood-texas-on-massive-scale.html,(accessedDec.12,2025).
| to protect | their control |     | algorithms | while | providing |     | power sys- |                    |     |           |     |              |     |        |                |
| ---------- | ------------- | --- | ---------- | ----- | --------- | --- | ---------- | ------------------ | --- | --------- | --- | ------------ | --- | ------ | -------------- |
|            |               |     |            |       |           |     |            | [5] B. Srivathsan, |     | M. Sorel, | and | P. Sachdeva, | “AI | power: | Expanding data |
templannerswithafunctionalmodelthataccuratelyrepresents
|              |             |     |      |           |     |             |        | center | capacity | to meet | growing | demand,” | McKinsey |     | & Company, |
| ------------ | ----------- | --- | ---- | --------- | --- | ----------- | ------ | ------ | -------- | ------- | ------- | -------- | -------- | --- | ---------- |
| the device’s | interaction |     | with | the grid. | In  | the absence | of de- |        |          |         |         |          |          |     |            |
October2024.
|               |        |     |       |           |         |              |     | [6] North | American | Electric | Reliability |     | Corporation, | “Incident | Review: |
| ------------- | ------ | --- | ----- | --------- | ------- | ------------ | --- | --------- | -------- | -------- | ----------- | --- | ------------ | --------- | ------- |
| tailed models | during | the | early | screening | phases, | transmission |     |           |          |          |             |     |              |           |         |
ConsideringSimultaneousVoltage-SensitiveLoadReductions,”NERC,
| operators | can utilize | targeted |     | questionnaires |     | to gather | critical |     |     |     |     |     |     |     |     |
| --------- | ----------- | -------- | --- | -------------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
IncidentReview,Jan.2025.
technical data. [7] “Byte Blackouts: How large data center loads are surfacing new is-
The pace of DC deployment significantly outstrips the sues,” blog.gridstatus.io. https://blog.gridstatus.io/byte-blackouts-large-
data-center-loads-new-issues-pjm/,(accessedNov.10,2025).
| timeline | for transmission |     | planning |     | and model | development. |     |           |       |             |                  |     |     |       |             |
| -------- | ---------------- | --- | -------- | --- | --------- | ------------ | --- | --------- | ----- | ----------- | ---------------- | --- | --- | ----- | ----------- |
|          |                  |     |          |     |           |              |     | [8] Large | Loads | Task Force, | “Characteristics |     | and | Risks | of Emerging |
While DCs can be built and energized in 12 to 24 months, LargeLoads,”NorthAmericanElectricReliabilityCorporation(NERC),
transmission infrastructure often requires 5 to 10 years to Whitepaper,Jul.2025.
[9] IndustryTechnicalSupportLeadershipCommittee(ITSLC)TaskForce,
complete. To manage this disparity, future planning frame- “Data Center Growth and Grid Readiness,” IEEE Power & Energy
works may need to adopt connect and manage approaches or Society,TechnicalReportPES-TR131,May2025.
expedited study timelines. [10] R.Rahmani,I.Moser,andM.Seyedmahmoudian,“ACompleteModel
forModularSimulationofDataCentrePowerLoad,”arXiv:1804.00703,
Thereisacriticallackofevent-basedmeasurementdatafor Mar.2018,Available:https://arxiv.org/abs/1804.00703.
large DC loads, which hinders the ability to extrapolate the [11] P.Mitra,“TransmissionPlanningandLargeDataCenters[ViewPoint],”
IEEEElectrificationMagazine,vol.11,no.3,pp.90–92,Sep.2023.
| load dynamics | and        | validate | simulation |      | models.       | Without | high-     |              |        |              |     |        |           |       |              |
| ------------- | ---------- | -------- | ---------- | ---- | ------------- | ------- | --------- | ------------ | ------ | ------------ | --- | ------ | --------- | ----- | ------------ |
|               |            |          |            |      |               |         |           | [12] J. Sun, | M. Xu, | M. Cespedes, |     | and M. | Kauffman, | “Data | Center Power |
| resolution    | field data | from     | actual     | grid | disturbances, |         | engineers |              |        |              |     |        |           |       |              |
SystemStability—PartI:PowerSupplyImpedanceModeling,”CSEE
JournalofPowerandEnergySystems,vol.8,no.2,pp.403–419,Mar.
| cannot | verify if | the dynamic |     | behavior | predicted |     | by models |     |     |     |     |     |     |     |     |
| ------ | --------- | ----------- | --- | -------- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
2022.
matches reality.
|     |     |     |     |     |     |     |     | [13] X. | Chen, X. | Wang, | A. Colacelli, |         | M. Lee, | and L. | Xie, “Elec-    |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ----- | ------------- | ------- | ------- | ------ | -------------- |
|     |     |     |     |     |     |     |     | tricity | Demand   | and   | Grid          | Impacts | of AI   | Data   | Centers: Chal- |
VI. CONCLUSION lenges and Prospects,” arXiv:2509.07218, Nov. 2025, Available:
https://arxiv.org/abs/2509.07218.
|               |                  |          |            |             |                      |       |            | [14] C. Mishra, |          | L. Vanfretti, | J. Delaree, |           | T. J. Purcell, | and       | K. D. Jones,  |
| ------------- | ---------------- | -------- | ---------- | ----------- | -------------------- | ----- | ---------- | --------------- | -------- | ------------- | ----------- | --------- | -------------- | --------- | ------------- |
| The           | proliferation    | of       | hyperscale |             | data centers—spurred |       | by         |                 |          |               |             |           |                |           |               |
|               |                  |          |            |             |                      |       |            | “Understanding  |          | the inception |             | of 14.7Hz | oscillations   |           | emerging from |
| the estimated | 39%              | compound |            | annual      | growth               | rate  | of global  |                 |          |               |             |           |                |           |               |
|               |                  |          |            |             |                      |       |            | a data          | center,” | Sustainable   | Energy,     | Grids     | and            | Networks, | vol. 43, p.   |
| generative    | AI workloads—has |          |            | transformed |                      | these | facilities |                 |          |               |             |           |                |           |               |
101735,Sep.2025.
|              |              |             |           |          |          |               |            | [15] M.-S.  | Ko and | H. Zhu,        | “Wide-Area        |     | Power System | Oscillations | from       |
| ------------ | ------------ | ----------- | --------- | -------- | -------- | ------------- | ---------- | ----------- | ------ | -------------- | ----------------- | --- | ------------ | ------------ | ---------- |
| into pivotal | participants |             | in future | power    | systems. |               | This paper |             |        |                |                   |     |              |              |            |
|              |              |             |           |          |          |               |            | Large-Scale |        | AI Workloads,” | arXiv:2508.16457, |     |              | Aug. 2025,   | Available: |
| highlights   | how          | traditional | load      | modeling |          | is inadequate | for        |             |        |                |                   |     |              |              |            |
https://arxiv.org/abs/2508.16457.
| capturing | the complex, |     | control-driven |     | dynamics |     | inherent | in  |     |     |     |     |     |     |     |
| --------- | ------------ | --- | -------------- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[16] A.Arif,Z.Wang,J.Wang,B.Mather,H.Bashualdo,andD.Zhao,“Load
Modeling—AReview,”IEEETransactionsonSmartGrid,vol.9,no.6,
| large rectifier-interfaced |     |     | data | center | loads. | As evidenced | by  |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ---- | ------ | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.5986–5999,Nov.2018.
| recent grid | disturbances, |     | high | voltage | sensitivity |     | and weak |               |     |            |               |     |       |           |      |
| ----------- | ------------- | --- | ---- | ------- | ----------- | --- | -------- | ------------- | --- | ---------- | ------------- | --- | ----- | --------- | ---- |
|             |               |     |      |         |             |     |          | [17] Modeling | and | Validation | Subcommittee, |     | “WECC | Composite | Load |
fault ride-through capabilities present substantial transient Model Specification,” Western Electricity Coordinating Council
stability risks to bulk power systems. Moreover, the inherent (WECC),Specificationsguide,Apr.2021.
|           |            |     |              |     |            |       |          | [18] P. Mitra, | J.  | Lu, and     | L. Sundaresh, |      | “Emerging | Loads:     | Modeling for |
| --------- | ---------- | --- | ------------ | --- | ---------- | ----- | -------- | -------------- | --- | ----------- | ------------- | ---- | --------- | ---------- | ------------ |
| nature of | GPU-driven |     | AI computing |     | introduces | novel | oscilla- |                |     |             |               |      |           |            |              |
|           |            |     |              |     |            |       |          | Transmission   |     | Reliability | Studies,”     | IEEE | Power     | and Energy | Magazine,    |
tory challenges, specifically forced oscillations and resonance vol.23,no.5,pp.35–43,Sep.2025.
phenomena. Addressing these vulnerabilities necessitates a [19] D.Ramasubramanian,P.Mitra,R.O’Keefe,J.Fonseka,B.Jayasekara,
|     |     |     |     |     |     |     |     | M. Dewadasa, |     | and A. | Isaacs, | “Modeling | of  | Load for | Transmission |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------- | --------- | --- | -------- | ------------ |
fundamental shift toward high-fidelity, control and protection- Systems Analysis: Aggregate versus detailed and positive sequence vs
based dynamic load modeling frameworks that leverage pha- electromagnetictransient[Feature],”IEEEPowerandEnergyMagazine,
sor, electromagnetic transient, or hybrid domains. Ultimately, vol.23,no.4,pp.81–98,Jul.2025.
[20] F.M.Mele,R.Za´rate-Min˜ano,andF.Milano,“Modelingloadstochastic
| maintaining | long-term |     | grid | security | depends | on  | overcoming |       |           |         |         |            |     |                   |     |
| ----------- | --------- | --- | ---- | -------- | ------- | --- | ---------- | ----- | --------- | ------- | ------- | ---------- | --- | ----------------- | --- |
|             |           |     |      |          |         |     |            | jumps | for power | systems | dynamic | analysis,” |     | IEEE Transactions | on  |
intellectual property barriers through standardized blackbox PowerSystems,vol.34,no.6,pp.5087–5090,2019.
|     |     |     |     |     |     |     |     | [21] AEMO | Operations, | “Power |     | System | Model Guidelines,” |     | Australian |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------ | --- | ------ | ------------------ | --- | ---------- |
modeling,andestablishingrigorousvalidationprotocolsusing
|                 |       |       |               |     |       |               |     | Energy | Market | Operator | (AEMO), | Australia, | Guidelines |     | Version 2.0, |
| --------------- | ----- | ----- | ------------- | --- | ----- | ------------- | --- | ------ | ------ | -------- | ------- | ---------- | ---------- | --- | ------------ |
| high-resolution | event | data. | Standardizing |     | these | methodologies |     |        |        |          |         |            |            |     |              |
Jul.2023.[Online].Available:https://aemo.com.au
| is essential             | for | ensuring | power     | system | integrity |         | amidst the |     |     |     |     |     |     |     |     |
| ------------------------ | --- | -------- | --------- | ------ | --------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| rapid, technology-driven |     |          | evolution |        | of global | demand. |            |     |     |     |     |     |     |     |     |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:18 UTC from IEEE Xplore.  Restrictions apply.