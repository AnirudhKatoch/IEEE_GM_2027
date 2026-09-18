AI Load Dynamics–A Power Electronics Perspective
Yuzhuo Li1, and Yunwei Li1
1Department of Electrical and Computer Engineering
University of Alberta, Edmonton, Canada
Email: yuzhuo@ualberta.ca, yunwei.li@ualberta.ca
Abstract—AsAI-drivencomputinginfrastructuresrapidlyscale, 100kW and even reach to 350kW per cabinet. This progression
discussionsarounddatacenterdesignoftenemphasizeenergycon- reflects both the increasing computational demands of modern
sumption, water and electricity usage, workload scheduling, and
AI algorithms and the relentless pursuit of improved training
thermal management. However, these perspectives often overlook
efficiency. The economic implications are substantial, with
thecriticalinterplaybetweenAI-specificloadtransientsandpower
electronics.Thispaperaddressesthatgapbyexamininghowlarge- power infrastructure representing a significant portion of total
scale AI workloads impose unique demands on power conversion datacentercapitalexpenditure.Moreover,thedynamicnatureof
chains and, in turn, how the power electronics themselves shape AIworkloads—characterizedbyrapidtransitionsbetweencom-
thedynamicbehaviorofAI-basedinfrastructure.Weillustratethe
putational phases—places unprecedented demands on power
fundamentalconstraintsimposedbymulti-stagepowerconversion
delivery systems. As shown in Fig. 1, GPUs have a different
architectures and highlight the key role of final-stage modules in
defining realistic power slew rates for GPU clusters. Our analysis power profile compared to traditional Central Processing Units
shows that traditional designs, optimized for slower-varying or (CPUs), further emphasizing the unique power dynamics AI
CPU-centric workloads, may not adequately accommodate the accelerators introduce. Empirical measurements also confirm
rapid load ramps and drops characteristic of AI accelerators.
that heterogeneous AI workloads can easily drive dynamic
To bridge this gap, we present insights into advanced converter
power swings [6].
topologies, hierarchical control methods, and energy buffering
techniques that collectively enable robust and efficient power Current industry practice reveals several critical challenges.
delivery. By emphasizing the bidirectional influence between AI First, the complex interaction between multiple power conver-
workloads and power electronics, we hope this work can set a sion stages, spanning facility-level AC-DC conversion to point-
good starting point and offer practical design considerations to
of-load regulation, creates cascaded dynamic limitations that
ensurefutureexascale-capabledatacenterscanmeetthestringent
constrain system response capabilities. Second, the need for
performance, reliability, and scalability requirements of next-
generation AI deployments. sophisticated energy storage distribution and protection coordi-
nation schemes introduces additional complexity and potential
I. INTRODUCTION bottlenecks. Third, the integration of advanced cooling solu-
tions requires careful consideration of power delivery system
The rapid evolution of artificial intelligence (AI) workloads
dynamics.
has fundamentally transformed the landscape of data center
These challenges are exacerbated by the rapid pace of
powerinfrastructure[1],[2].ContemporaryAItrainingclusters
AI hardware evolution. The transition from traditional CPU
(for Large Language Models (LLMs) from OpenAI, Google,
or CPU/GPU architectures to specialized AI accelerators has
Meta,etc.)nowroutinelyconsumepoweratmegawattscales(or
driven substantial increases in both power density and dynamic
even beyond) while exhibiting unprecedented power dynamics
range. For instance, modern AI accelerators can exhibit power
during operation [3]. This paradigm shift necessitates a com-
variations exceeding 50% of their thermal design power (TDP)
prehensivere-examinationofpowerdeliveryarchitectures,with
withinmilliseconds,whilenext-generationdevicesareexpected
particular emphasis on the fundamental limitations imposed by
to push these boundaries even further. This trend necessitates
cascaded power conversion chains. Understanding these con-
sophisticated power delivery architectures capable of handling
straints is critical not only for current deployments but also for
both steady-state power requirements and rapid transient re-
the strategic development of next-generation AI infrastructure.
sponses.
Research Questions:
Understandingandoptimizingthesepowerdynamicsrequires
• What is the fundamental timescale bottleneck in AI data careful consideration of multiple interacting constraints. Power
center power chains?
conversionchainsandworkloadpatternscontributesignificantly
• Howdoeseachpowerconversionstagecontributetolimit- to system response capabilities. This interaction of multiple
ing overall power ramp rates in Graphics Processing Unit
constraints has profound implications for the design and op-
(GPU) clusters?
eration of AI infrastructure, particularly as the industry moves
The scale and sophistication of AI workloads continues to towardever-largertrainingclustersandmoredynamicworkload
accelerate, straining both electricity supply and facility design. patterns.
Projections indicate that AI could drive a steep surge in U.S.
data-center power demand in the coming decade [4]. Indeed,
II. GPURACK/CLUSTERHARDWARE
EPRI’scomprehensiveanalysisshowsthatAI-centricinfrastruc- The evolution of GPU cluster configurations demonstrates a
tures can significantly elevate overall power consumption [5]. consistent trajectory toward increased power density capabili-
Training clusters have evolved from traditional configurations ties, presenting significant challenges in data center design and
consuming 10-20kW per rack to advanced designs exceeding operation. Contemporary deployments span a broad spectrum
5202
beF
6
]RA.sc[
2v74610.2052:viXra

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
|     |     |     |     |     |     |     |     | how hierarchical |     | power      | distribution |       | and advanced |          | cooling | can    |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ------------ | ----- | ------------ | -------- | ------- | ------ |
|     |     |     |     |     |     |     |     | be integrated.   |     | Similarly, | Vertiv’s     | 360AI | concept      | outlines |         | multi- |
rackscalingforAIinfrastructures[12].Thesereferencedesigns
|     |     |     |     |     |     |     |     | provide      | validated     | architectures    |                | for           | scalable      | AI              | infrastructure |         |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ---------------- | -------------- | ------------- | ------------- | --------------- | -------------- | ------- |
|     |     |     |     |     |     |     |     | deployment,  | incorporating |                  | comprehensive  |               |               | solutions       | for            | power   |
|     |     |     |     |     |     |     |     | delivery     | and system    | management.      |                |               |               |                 |                |         |
|     |     |     |     |     |     |     |     | 2) Power     | Distribution  |                  | Architecture   |               |               |                 |                |         |
|     |     |     |     |     |     |     |     | Figure       | 2 shows       | a representative |                |               | industrial    | reference       |                | design  |
|     |     |     |     |     |     |     |     | featuring    | hierarchical  |                  | power          | distribution  |               | and cooling     |                | strate- |
|     |     |     |     |     |     |     |     | gies. The    | power         | architecture     |                | in multi-rack |               | implementations |                |         |
|     |     |     |     |     |     |     |     | demonstrates |               | sophisticated    | hierarchical   |               | organization. |                 | The            | pri-    |
|     |     |     |     |     |     |     |     | mary power   | distribution  |                  | infrastructure |               | utilizes      | Medium-Voltage  |                |         |
Fig. 1: Different Power Consumption Features of GPU vs. CPU AC (MVAC) utility feeds, complemented by parallel 3MVA
| Operation | for same | AI Computation |     | Task. |     |     |     |              |     |     |           |         |     |       |        |     |
| --------- | -------- | -------------- | --- | ----- | --- | --- | --- | ------------ | --- | --- | --------- | ------- | --- | ----- | ------ | --- |
|           |          |                |     |       |     |     |     | transformers | and | 3MW | generator | systems | per | power | train. | The |
systemincorporatesN+1redundantmediumvoltageswitchgear
|                  |     |            |     |         |       |             |     | and a 480V | Low-Voltage |     | AC  | (LVAC) | distribution |     | backbone |     |
| ---------------- | --- | ---------- | --- | ------- | ----- | ----------- | --- | ---------- | ----------- | --- | --- | ------ | ------------ | --- | -------- | --- |
| from traditional |     | several-kW |     | compute | racks | to advanced | AI- |            |             |     |     |        |              |     |          |     |
organizedinfourparallel3MWpowertrainsconfiguredina3+1
| ready solutions |           | exceeding | 100kW              | power           | consumption |          | per rack  |                   |                |               |           |             |               |           |             |        |
| --------------- | --------- | --------- | ------------------ | --------------- | ----------- | -------- | --------- | ----------------- | -------------- | ------------- | --------- | ----------- | ------------- | --------- | ----------- | ------ |
|                 |           |           |                    |                 |             |          |           | distributed       | redundant      | arrangement.  |           | And         | the           | major     | computation |        |
| [7]. Industrial |           | reference | guides             | further         | detail      | advanced | cooling   |                   |                |               |           |             |               |           |             |        |
|                 |           |           |                    |                 |             |          |           | racks feature     | NVL72          | architecture  |           | as          | detailed      | in Figure | 3.          |        |
| solutions       | and       | validated | power-distribution |                 | topologies  |          | [8], [9]. |                   |                |               |           |             |               |           |             |        |
|                 |           |           |                    |                 |             |          |           | 3) Implementation |                | Scales        |           |             |               |           |             |        |
| This section    | presents  | a         | systematic         | analysis        |             | of these | configu-  |                   |                |               |           |             |               |           |             |        |
|                 |           |           |                    |                 |             |          |           | The 904kW         |                | configuration |           | exemplifies | sophisticated |           |             | system |
| rations,        | examining | their     | architectural      | characteristics |             | and      | opera-    |                   |                |               |           |             |               |           |             |        |
|                 |           |           |                    |                 |             |          |           | integration       | methodologies, |               | combining |             | eight         | compute   | racks       | at     |
tionalconstraintsacrossthreeprimaryscalesofimplementation.
|                |     |               |     |     |     |     |     | 73kW each     | with | eight              | network | infrastructure |        | racks | at            | 40kW |
| -------------- | --- | ------------- | --- | --- | --- | --- | --- | ------------- | ---- | ------------------ | ------- | -------------- | ------ | ----- | ------------- | ---- |
| A. Single-Rack |     | Architectures |     |     |     |     |     |               |      |                    |         |                |        |       |               |      |
|                |     |               |     |     |     |     |     | each. Scaling |      | this architecture, |         | the            | 1808kW |       | configuration |      |
1) NVL Series Implementation demonstrates comprehensive multi-rack implementation strate-
|           |     |                |     |         |          |         |      | gies, incorporating |     | sixteen | compute |     | racks at | 73kW | each | along- |
| --------- | --- | -------------- | --- | ------- | -------- | ------- | ---- | ------------------- | --- | ------- | ------- | --- | -------- | ---- | ---- | ------ |
| The NVL36 |     | configuration, |     | with up | to 2700W | for the | com- |                     |     |         |         |     |          |      |      |        |
plete Grace Blackwell Superchip (GB200), implements a com- side sixteen network infrastructure racks. The 7392kW imple-
mentationrepresentsastate-of-the-arthigh-densityGPUcluster
| prehensive | design | supporting |     | 9 servers | with | 4 GPUs | each. |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ---------- | --- | --------- | ---- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisarchitectureincorporatesenhancedpowerdeliverysystems architecture utilizing sophisticated multi-tier power distribution
| integrated     | with  | Cooling       | Distribution | Units          | (CDUs), | achieving     |         | topology.            |     |            |               |        |     |              |     |      |
| -------------- | ----- | ------------- | ------------ | -------------- | ------- | ------------- | ------- | -------------------- | --- | ---------- | ------------- | ------ | --- | ------------ | --- | ---- |
| a total rack   | power | capacity      | of           | 73kW. Building |         | upon this     | foun-   |                      |     |            |               |        |     |              |     |      |
|                |       |               |              |                |         |               |         | C. Large-Scale       |     | Deployment | Projections   |        |     |              |     |      |
| dation, the    | NVL72 | configuration |              | doubles        | the     | compute       | density |                      |     |            |               |        |     |              |     |      |
|                |       |               |              |                |         |               |         | 1) Workload-Specific |     |            | Architectures |        |     |              |     |      |
| to accommodate |       | 18 servers    | with         | 4 GPUs         | each.   | This advanced |         |                      |     |            |               |        |     |              |     |      |
|                |       |               |              |                |         |               |         | Deployments          |     | spanning   | from          | 10,000 | up  | to 1,000,000 |     | GPUs |
designimplementsdualpowerdeliverypaths,enhancingsystem
reliability through sophisticated power management systems require rethinking both facility power and data pipelines. Ad-
|         |             |       |     |       |     |     |     | ditionally, | some | workloads | are | shifting | to  | smaller | edge | sites |
| ------- | ----------- | ----- | --- | ----- | --- | --- | --- | ----------- | ---- | --------- | --- | -------- | --- | ------- | ---- | ----- |
| capable | of handling | 132kW | per | rack. |     |     |     |             |      |           |     |          |     |         |      |       |
2) Ultra-High-Density Implementations [13], while enterprise High-Performance Computing (HPC)
Theultra-high-densityconfiguration,exemplifiedbytheHPE orchestration must unify large AI workflows [14]. Training-
|         |          |       |            |         |     |         |           | intensive | deployments |     | demonstrate |     | distinctive | requirements |     | in  |
| ------- | -------- | ----- | ---------- | ------- | --- | ------- | --------- | --------- | ----------- | --- | ----------- | --- | ----------- | ------------ | --- | --- |
| Cray EX | platform | [10], | represents | another |     | current | state-of- |           |             |     |             |     |             |              |     |     |
the-art in GPU computing infrastructure. This implementation powerinfrastructuredesign,implementingsustainedhigh-power
|          |                  |     |         |     |          |     |         | operation | optimization |     | with direct | liquid | cooling | solutions |     | pre- |
| -------- | ---------------- | --- | ------- | --- | -------- | --- | ------- | --------- | ------------ | --- | ----------- | ------ | ------- | --------- | --- | ---- |
| supports | an unprecedented |     | density | of  | 224 GPUs | per | cabinet |           |              |     |             |        |         |           |     |      |
with a total power capacity of 350kW. The system architecture dominating the thermal management strategy. These systems
comprises eight compute chassis per cabinet, each supporting typicallyemploy3+1or4-to-make-3redundancyschemascom-
|               |     |              |              |     |     |                |     | plemented | by  | sophisticated | management |     | systems. |     |     |     |
| ------------- | --- | ------------ | ------------ | --- | --- | -------------- | --- | --------- | --- | ------------- | ---------- | --- | -------- | --- | --- | --- |
| eight compute |     | blade slots, | complemented |     | by  | four redundant |     |           |     |               |            |     |          |     |     |     |
power shelves with dedicated PDUs in a quad power input Inference-focused deployments present contrasting architec-
|     |     |     |     |     |     |     |     | tural requirements, |     | emphasizing |     | dynamic |     | load | profile | man- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | --- | ------- | --- | ---- | ------- | ---- |
configuration.
|          |     |                |     |          |         |          |     | agement | capabilities | through |     | hybrid | cooling | implementations. |     |     |
| -------- | --- | -------------- | --- | -------- | ------- | -------- | --- | ------- | ------------ | ------- | --- | ------ | ------- | ---------------- | --- | --- |
| The node |     | implementation |     | in these | systems | utilizes | the |         |              |         |     |        |         |                  |     |     |
EX254n blade architecture, featuring a dual-node design that These systems typically employ N+1 redundancy schemas with
rapidfailovermechanisms,supportedbyadvancedloadbalanc-
| integrates | four | GH200 | superchips | per | node. | Each node | incor- |     |     |     |     |     |     |     |     |     |
| ---------- | ---- | ----- | ---------- | --- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
poratesa72-coreArmNeoverseV2GraceCPU,optimizedwith ing systems. System characteristics reflect variable workload
|     |     |     |     |     |     |     |     | patterns, | requiring | sophisticated |     | variable | thermal | load | manage- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------------- | --- | -------- | ------- | ---- | ------- | --- |
128GBLPDDR5XDRAM,andquadSlingshot-11NetworkIn-
|     |     |     |     |     |     |     |     | ment systems |     | and network |     | architectures |     | optimized | for | low- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --- | ------------- | --- | --------- | --- | ---- |
terfaceCard(NIC)implementation.Thisconfigurationachieves
maximum density while maintaining thermal stability through latencyresponse.Storagesubsystemsareengineeredspecifically
|               |            |            |           |         |     |     |     | for high | Input/Output |             | operations | per | second         | performance |              | to  |
| ------------- | ---------- | ---------- | --------- | ------- | --- | --- | --- | -------- | ------------ | ----------- | ---------- | --- | -------------- | ----------- | ------------ | --- |
| advanced      | management | systems.   |           |         |     |     |     |          |              |             |            |     |                |             |              |     |
|               |            |            |           |         |     |     |     | support  | rapid        | data access | patterns   |     | characteristic |             | of inference |     |
| B. Multi-Rack |            | Industrial | Reference | Designs |     |     |     |          |              |             |            |     |                |             |              |     |
operations.
1) Reference Architecture Overview Hybrid architectures must accommodate training-intensive
Industrial-scale GPU reference designs, such as Schneider’s racks where sustained high-power operation dominates, as
EcoStruxure RD109 (7.392MW for IT load) [11], demonstrate well as dynamic inference loads prone to frequent ramp-ups
2

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
|     |               |     | TABLE      | I: GPU Cluster | Power | Configurations |     |     |               |     |     |     |     |
| --- | ------------- | --- | ---------- | -------------- | ----- | -------------- | --- | --- | ------------- | --- | --- | --- | --- |
|     | Configuration |     | TotalPower | GPUType        |       | GPUPower       |     |     | SystemDensity |     |     |     |     |
Single-RackConfigurations
TraditionalA100 32kW NVIDIAA100 400W/GPU 8servers×8GPUs=64GPUs
TraditionalH100 34kW NVIDIAH100 700W/GPU 6servers×8GPUs=48GPUs
NVL36Liquid-Cooled 73kW GB200 1,200W/GPU 9servers×4GPUs=36GPUs
NVL72Liquid-Cooled 132kW GB200 1,200W/GPU 18servers×4GPUs=72GPUs
Fig. 2: GPU cluster reference design implementation demonstrating comprehensive power distribution architecture (from Schneider RD109,
7392kW for IT racks, total power consumption approximately 10.5MW including cooling infrastructure)
|     |     |     |     |     | allocation      |             | mechanisms.                     |              | The             | thermal       | management    |                  | integration  |
| --- | --- | --- | --- | --- | --------------- | ----------- | ------------------------------- | ------------ | --------------- | ------------- | ------------- | ---------------- | ------------ |
|     |     |     |     |     | combines        |             | multiple                        | cooling      | approaches,     |               | incorporating |                  | variable     |
|     |     |     |     |     | thermal         |             | load handling                   |              | capabilities    |               | with Cooling  |                  | Distribution |
|     |     |     |     |     | Unit            | capacity    |                                 | optimization | algorithms.     |               | Temperature   |                  | gradient     |
|     |     |     |     |     | management      |             | systems                         | ensure       | uniform         |               | thermal       | conditions       | across       |
|     |     |     |     |     | the             | deployment, |                                 | critical     | for maintaining |               | consistent    |                  | performance  |
|     |     |     |     |     | characteristics |             | under                           | varying      |                 | workload      | conditions.   |                  |              |
|     |     |     |     |     |                 | III.        | WORKLOADPATTERNCHARACTERIZATION |              |                 |               |               |                  |              |
|     |     |     |     |     |                 | Modern      | AI                              | workloads    | present         | unique        |               | challenges       | for data     |
|     |     |     |     |     | center          | power       | infrastructure                  |              | that            | fundamentally |               | differ           | from tra-    |
|     |     |     |     |     | ditional        |             | computing                       | loads.       | To              | understand    | these         | challenges,      | we           |
|     |     |     |     |     | must            | first       | examine                         | how          | AI              | accelerators  |               | like GPUs        | operate      |
|     |     |     |     |     | and             | why         | their power                     | consumption  |                 | patterns      |               | are distinctive. | This         |
sectionprovidesacomprehensiveanalysisofthesepatternsand
|                    |            |              |            |            | their     | implications |           | for power |              | system | design. | All      | experimental |
| ------------------ | ---------- | ------------ | ---------- | ---------- | --------- | ------------ | --------- | --------- | ------------ | ------ | ------- | -------- | ------------ |
|                    |            |              |            |            | waveforms |              | presented | in        | this section |        | were    | captured | on a single  |
| Fig. 3: A possible | NVL72 rack | architecture | showcasing | integrated |           |              |           |           |              |        |         |          |              |
compute and power distribution systems in-labworkstationrunningUbuntu20.04LTSwithCUDA12.x,
equippedwithanAMDRyzen55500(3.6GHzbase)processor,
|     |     |     |     |     | 32GB | DDR4 | (2×16GB |     | G.Skill | RipjawsV |     | at 3200MT/s), | an  |
| --- | --- | --- | --- | --- | ---- | ---- | ------- | --- | ------- | -------- | --- | ------------- | --- |
[15]. It requires complex power and cooling infrastructures NVIDIA RTX4090 GPU (standard reference design with a
capable of accommodating diverse workload characteristics. 16-pin PCIe 5.0 connector), and a 1000W MPG PCIe 5.0
These systems implement multi-tier power distribution topolo- Gold (80+ Gold) power supply unit. The workload software
gies featuring modular power subsystems and dynamic power included two primary AI models—GPT-2 (124M parameters,
3

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
a Generative Pretrained Transformer model from OpenAI) bi-directional converter topologies that can absorb or quickly
under PyTorch for training experiments and LLaMA-3.1 (8B curtailinputpower.Themillisecond-levelzoominSubfigure5d
parameters, LLM model from Meta) for inference tests viaa highlights that at least a few AC cycles are involved in stabi-
customscript.ATektronixDPO-seriesoscilloscope,configured lizing current after the GPU load drop, indicating a need for
with Hall-effect current probes on the GPU motherboard (Ch1) carefully tuned control loops.
| and Power | Supply  | Unit       | (PSU) | input  | (Ch2)    | alongside      | single- |                  |     |             |       |             |     |     |
| --------- | ------- | ---------- | ----- | ------ | -------- | -------------- | ------- | ---------------- | --- | ----------- | ----- | ----------- | --- | --- |
|           |         |            |       |        |          |                |         | B. Understanding |     | AI Workload | Power | Consumption |     |     |
| phase AC  | voltage | monitoring |       | (Ch3), | recorded | all waveforms. |         |                  |     |             |       |             |     |     |
Each figure in this section provides time-synchronized captures At their core, modern AI workloads, particularly LLMs, are
|              |      |              |          |          |     |             |        | built upon | fundamental   |             | operations   | including | matrix      | multipli-   |
| ------------ | ---- | ------------ | -------- | -------- | --- | ----------- | ------ | ---------- | ------------- | ----------- | ------------ | --------- | ----------- | ----------- |
| over various | zoom | levels,      | enabling | detailed |     | observation | of the |            |               |             |              |           |             |             |
|              |      |              |          |          |     |             |        | cations,   | attention     | mechanisms, | and          | data      | movement    | operations. |
| GPU’s rapid  | load | transitions. |          |          |     |             |        |            |               |             |              |           |             |             |
|              |      |              |          |          |     |             |        | When an    | LLM processes |             | information, |           | it performs | successive  |
A. Transient Measurements matrix transformations and self-attention computations across
a) During GPT-2 Training Checkpoints multiple layers, each contributing to the overall power demand.
As illustrated in Figure 4, the GPU motherboard current These operations create a characteristic power consumption
patternthatcanbedecomposedintothreeprimarycomponents:
| experiences | abrupt, | multi-ampere |         | surges      | associated | with  | model      |         |         |       |        |       |          |          |
| ----------- | ------- | ------------ | ------- | ----------- | ---------- | ----- | ---------- | ------- | ------- | ----- | ------ | ----- | -------- | -------- |
| checkpoint  | events. | Subfigure    |         | 4a captures | an         | early | load drop  |         |         |       |        |       |          |          |
|             |         |              |         |             |            |       |            | P (t)=P |         | (t)+P |        | (t)+P |          | (t). (1) |
|             |         |              |         |             |            |       |            | op      | compute |       | memory |       | transfer |          |
| around      | 14.5s;  | one can      | observe | the current | plunging   |       | from near- |         |         |       |        |       |          |          |
peak values to an almost idle state within milliseconds. This Thecomputecomponent,P compute (t),representspowercon-
sudden negative transient underscores the need for fast PSU sumed by matrix operations and attention computations, which
controltoavertovervoltageontheinternalDCbus.Meanwhile, can demand up to 90% of peak power during intensive calcu-
Subfigure 4b zooms to the final checkpoint event at a 10s lations. Modern LLMs implement these computations through
|            |         |       |         |        |     |          |          | specialized | tensor | processing | units | that perform |     | highly parallel |
| ---------- | ------- | ----- | ------- | ------ | --- | -------- | -------- | ----------- | ------ | ---------- | ----- | ------------ | --- | --------------- |
| timescale, | showing | rapid | current | swings |     | when the | training |             |        |            |       |              |     |                 |
process is intentionally halted. By narrowing the view further operations. The memory component, P memory (t), captures the
to 500ms in Subfigure 4c and eventually to a millisecond-level power required for accessing model weights and activations.
|     |     |     |     |     |     |     |     | With current | LLM | architectures | exceeding |     | hundreds | of billions |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --------- | --- | -------- | ----------- |
captureinSubfigure4d,weseehowswiftlytheGPUtransitions
from full compute load to near idle across merely a few AC ofparameters,thiscomponentbecomesincreasinglysignificant.
|         |     |     |     |     |     |     |     | The transfer | component, |     | P        | (t), accounts |     | for data move- |
| ------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | -------- | ------------- | --- | -------------- |
| cycles. |     |     |     |     |     |     |     |              |            |     | transfer |               |     |                |
Although local energy buffering partially smooths these mentpower,particularlycriticalindistributedtrainingscenarios
spikes, the magnitude and speed of these current changes wheremodelparallelismnecessitatessubstantialcommunication
|         |        |             |     |             |     |                   |     | between | GPUs. |     |     |     |     |     |
| ------- | ------ | ----------- | --- | ----------- | --- | ----------------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
| go well | beyond | traditional |     | CPU-centric | or  | transaction-based |     |         |       |     |     |     |     |     |
workloads. When extrapolated to multi-rack or multi-megawatt Comment [C]: The combined effect of P (t) and
compute
|               |     |           |      |              |     |        |          | P      | (t) frequently |     | manifests | as rapid | load | transients in |
| ------------- | --- | --------- | ---- | ------------ | --- | ------ | -------- | ------ | -------------- | --- | --------- | -------- | ---- | ------------- |
| HPC clusters, |     | such fast | load | fluctuations | can | stress | upstream | memory |                |     |           |          |      |               |
powerdistribution,controlloops,andprotectivedevices.Hence, Figures 4 and 5. When large parameter blocks are read/written
GPU-centricsystemsdemandnotonlyhigheraveragepowerbut during an attention step or inference request, memory power
|          |            |     |        |             |        |                |     | surges coincide | with | intense | compute | kernels, |     | further amplify- |
| -------- | ---------- | --- | ------ | ----------- | ------ | -------------- | --- | --------------- | ---- | ------- | ------- | -------- | --- | ---------------- |
| also the | capability | to  | handle | large di/dt | events | on millisecond |     |                 |      |         |         |          |     |                  |
timescales, as predicted by the formal analysis in Section V. ing peak demands.
| Comment | [A]:           | In Subfigure |        | 4c, we | observe | that   | the GPU  |             |          |          |     |     |     |     |
| ------- | -------------- | ------------ | ------ | ------ | ------- | ------ | -------- | ----------- | -------- | -------- | --- | --- | --- | --- |
|         |                |              |        |        |         |        |          | C. Training | Workload | Dynamics |     |     |     |     |
| current | varies between |              | nearly | 0A and | around  | 25–30A | in rapid |             |          |          |     |     |     |     |
Trainingoperationsrepresentoneofthemostdemandingsce-
| succession. | Such | wide | swings | within | a fraction | of  | a second |            |                |     |          |        |       |                 |
| ----------- | ---- | ---- | ------ | ------ | ---------- | --- | -------- | ---------- | -------------- | --- | -------- | ------ | ----- | --------------- |
|             |      |      |        |        |            |     |          | narios for | power delivery |     | systems. | During | these | operations, the |
highlightthelimitationsofsmall-signalcontrolassumptionsand
|            |        |           |        |              |        |             |     | aggregate | power consumption |     | follows | a   | characteristic | pattern: |
| ---------- | ------ | --------- | ------ | ------------ | ------ | ----------- | --- | --------- | ----------------- | --- | ------- | --- | -------------- | -------- |
| underscore | the    | need for  | robust | large-signal | design | approaches. |     |           |                   |     |         |     |                |          |
| b)         | During | LLaMA-3.1 |        | 8B Inference |        |             |     |           |                   |     |         | N   |                |          |
(cid:88)
Figure 5 shows how inference-driven load transitions differ P train (t)=P base + α i f i (t)+ϵ(t), (2)
from training checkpoints, yet still generate rapid current tran- i=1
sients on the same RTX-4090 GPU. Subfigure 5a captures the where the baseline power P base often hovers around 60–70%
moment the model begins processing a new inference request, of peak load to maintain readiness for the next compute cycle.
| ramping | the current | from | a   | baseline | level to | roughly | 20–25A |               |      |          |     |       |            |           |
| ------- | ----------- | ---- | --- | -------- | -------- | ------- | ------ | ------------- | ---- | -------- | --- | ----- | ---------- | --------- |
|         |             |      |     |          |          |         |        | The summation | term | captures | the | power | variations | from dif- |
in under 200ms. This spike in load indicates the shift from ferent training phases, with α reflecting each phase’s intensity
i
idle/standby operations to active compute. and f (t) describing its duration or time-varying profile. The
i
Subfigures 5b–5c illustrate the load-down sequence, with stochastic term ϵ(t) accounts for minor fluctuations due to
repeated downward spikes in GPU current leading to near-idle micro-batching or asynchronous background tasks.
operation. Meanwhile, the PSU input voltage (Ch3, red trace) A typical training session proceeds through several distinct
remains relatively stable, confirming that local capacitors and phases,eachwithuniquepowercharacteristics.Duringforward
PSUcontrolloopseffectivelysmoothsomeofthefastestedges. propagation,theacceleratormaintainshighbutrelativelysteady
However, the abrupt negative transients still pose overvoltage power consumption as it processes data through the neural
risks if not properly managed—mirroring the training check- network layers. The backward propagation phase introduces
point concerns. more variability, as error gradients are computed and memory
Comment [B]: As discussed further in Section V, handling reads/writes intensify. This can lead to short bursts of full-load
these rapid load drops requires energy storage solutions or operation and subsequent partial idling between optimization
4

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
| (a) Initial | capture | showing | the first | load drop | around | 14.5s. Checkpoints |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | --------- | --------- | ------ | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
induceasuddendropfrompeakcurrenttonear-idle,underscoringtheabrupt (b) Closer view (10s scale) of the last checkpoint event, where training is
natureofAItrainingworkloadtransitions. intentionallyinterrupted,causingrapidup/downcurrentsurges.
(c)Detailedcapture(500msscale)focusingonthesteeptransitionsastheGPU
goesfromfullcomputeloadtonearidle.SeveralfundamentalACcyclesare (d)Millisecond-levelzoomofthefinalinterruptevent,pinpointingtheinstan-
visibleinthePSUcurrentwaveform. taneousswingsinGPUmotherboardcurrentacrossjustafewACcycles.
Fig.4:Progressivezoom-inofGPUcurrenttransientsduringGPT-2(124M)trainingcheckpoints.(a)illustratesthefirstloaddrop,while(b)–(d)
progressively zoom into the last interrupted training phase, where rapid up/down surges occur within a span of several AC cycles. Waveform
| from top | to bottom: | current | of the | GPU mother | board, | PSU | current, | PSU voltage. |     |     |     |     |     |     |
| -------- | ---------- | ------- | ------ | ---------- | ------ | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
steps. Together, these behavior patterns can induce the “saw- where P represents the baseline draw, and each term P (t)·
|     |     |     |     |     |     |     |     |     | idle |     |     |     |     | k   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
tooth” or “spiky” load profiles evident in Figure 4. R (t)modelsaspecificrequesttype’spowerdemandandarrival
k
pattern.
| Comment    | [D]:   | It is      | important | to distinguish |     | between | this    |         |      |                   |            |          |     |           |
| ---------- | ------ | ---------- | --------- | -------------- | --- | ------- | ------- | ------- | ---- | ----------------- | ---------- | -------- | --- | --------- |
|            |        |            |           |                |     |         |         | Comment | [E]: | In many inference | scenarios, | requests |     | arrive in |
| “baseline” | during | a training |           | loop—where     | the | GPU     | remains |         |      |                   |            |          |     |           |
rapidbursts,causingGPUloadtooscillatebetweenidle(orlow
| at elevated | clocks | to      | rapidly  | process | the next | batch—and |     | a      |               |              |         |       |      |     |
| ----------- | ------ | ------- | -------- | ------- | -------- | --------- | --- | ------ | ------------- | ------------ | ------- | ----- | ---- | --- |
|             |        |         |          |         |          |           |     | power) | and near-peak | consumption. | Figures | 5c–5d | show | how |
| true idle   | state  | when no | training | is      | running. | In many   | HPC |        |               |              |         |       |      |     |
quicklythesystemreturnstoidleoncearequestcompletes,with
| environments, |              | the “idle” | portion | of a training |          | cycle still | draws     |           |            |                |        |     |              |     |
| ------------- | ------------ | ---------- | ------- | ------------- | -------- | ----------- | --------- | --------- | ---------- | -------------- | ------ | --- | ------------ | --- |
|               |              |            |         |               |          |             |           | negative  | transients | that may reach | 80–90% | of  | peak current | in  |
| a substantial | fraction     | of         | peak    | power (often  | 60–70%), |             | precisely |           |            |                |        |     |              |     |
|               |              |            |         |               |          |             |           | under one | second.    |                |        |     |              |     |
| because       | the hardware | does       | not     | downclock     | fully    | between     | mini-     |           |            |                |        |     |              |     |
batches.Bycontrast,atrulyidleGPU(withnoactivetrainingor
|     |     |     |     |     |     |     |     | Comment | [F]: | Closer inspection | of our | inference | waveforms |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ----------------- | ------ | --------- | --------- | --- |
inference tasks) may draw significantly less power, potentially reveals that the baseline current may hover around 5A and
nearer to 5–10A on the motherboard rail, depending on the can briefly approach 10A. This baseline likely stems from the
GPU’s internal power management. GPU maintaining elevated clock states or memory readiness,
evenwhennominally“idle.”Inpractice,oneseesrepeatedshort
D. Inference Workload Characteristics burstsfrom5–10Aupto25–30A,followedbyabruptdropsthat
|     |     |     |     |     |     |     |     | occur within | tens | of milliseconds. | The | power supply’s |     | internal |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ---------------- | --- | -------------- | --- | -------- |
Inference workloads present a different set of challenges, bufferingensurestheinputcurrent(Ch2)andACvoltage(Ch3)
particularly in production environments handling multiple si- remainrelativelystable,butonthemotherboardrail(Ch1),these
multaneous requests. The power consumption during inference transitions can appear as rapid spikes and dips that challenge
| can be | characterized | as: |     |     |     |     |     | traditional | control    | assumptions. |            |     |         |      |
| ------ | ------------- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------ | ---------- | --- | ------- | ---- |
|        |               |     |     |     |     |     |     | While       | individual | inference    | operations | may | consume | less |
M
(cid:88) powerthanatrainingstep,latencydemandscantriggerfrequent
|     | P   | (t)=P | +   | P   | (t)·R | (t), | (3) |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
inf idle k k transitions.Batchingcanenhanceefficiencybyprocessingmul-
k=1
5

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
(a)Initialcaptureshowingtheinferenceload-uptransitionforanRTX-4090 (b)Subsequentcaptureillustratingtheinitialportionoftheload-downevent
running a LLaMA-3.1 8B model. The GPU current (black trace) rapidly (GPU returning to a lower-power state). Note the abrupt decline in GPU
increases,indicatingtheonsetofinferenceoperations. currentandthenear-sinusoidalPSUinputcurrent.
(d)Millisecond-scaleviewcapturingthefinalramptoidlepower.Thehigh-
(c)Moredetailedzoomofthenegativetransient,showingrepeateddownward frequency ripples on the GPU current trace illustrate rapid control-loop
spikesinGPUcurrentastheinferencerequestloaddiminishes. adjustmentsbeforesettling.
Fig. 5: Waveforms recorded during inference operations on an RTX-4090 running a LLaMA-3.1 8B model. (a) The GPU load-up event draws
substantial current as the inference request begins, while (b)–(d) document the load-down stages with progressively closer zoom, highlighting
the abrupt negative transients and the PSU’s response in stabilizing the supply voltage and current. Waveform from top to bottom: current of
| the GPU mother |     | board, PSU | current, PSU | voltage. |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
tiplerequestssimultaneously,butitcanalsoaltertheloadprofile to fault conditions to traditional protection systems, requiring
byconcentratingshort,high-powerbursts.Thistradeoffbetween more sophisticated detection and coordination approaches.
power efficiency and response time is central to practical Comment [G]: In multi-megawatt HPC or AI clusters, ag-
inference deployments. gregator effects can amplify transient peaks when dozens or
|                 |          |                 |        |         |             | hundreds             | of GPUs | checkpoint            | or load/unload | tasks       | nearly        | in    |
| --------------- | -------- | --------------- | ------ | ------- | ----------- | -------------------- | ------- | --------------------- | -------------- | ----------- | ------------- | ----- |
| E. System-Level |          | Impact          |        |         |             |                      |         |                       |                |             |               |       |
|                 |          |                 |        |         |             | unison. System-level |         | designs               | must consider  | phase-shift | or            | stag- |
|                 |          |                 |        |         |             | gered scheduling     |         | approaches—especially |                | when        | synchronizing |       |
| These           | workload | characteristics | create | several | fundamental |                      |         |                       |                |             |               |       |
challenges for power delivery system design. First, they re- gradientupdates—toavoidlarge-scalepowersurgesthatexceed
|              |         |         |          |         |                 | upstream | supply | capabilities. |     |     |     |     |
| ------------ | ------- | ------- | -------- | ------- | --------------- | -------- | ------ | ------------- | --- | --- | --- | --- |
| quire energy | storage | systems | that can | operate | across multiple |          |        |               |     |     |     |     |
timescales. Local capacitors must handle microsecond-level These characteristics fundamentally influence power delivery
transitions,whilelargerenergystorageelementsmanagelonger- system design decisions, from the selection of power converter
|                  |     |                  |         |        |                 | topologies | to the | implementation | of  | control and | protection |     |
| ---------------- | --- | ---------------- | ------- | ------ | --------------- | ---------- | ------ | -------------- | --- | ----------- | ---------- | --- |
| term variations. |     | The distribution | of this | energy | storage through |            |        |                |     |             |            |     |
the system becomes a critical design consideration. strategies. Successfully supporting AI workloads requires care-
|         |         |         |             |       |                 | ful consideration |     | of these patterns | and | their implications |     | across |
| ------- | ------- | ------- | ----------- | ----- | --------------- | ----------------- | --- | ----------------- | --- | ------------------ | --- | ------ |
| Second, | control | systems | must manage | power | delivery across |                   |     |                   |     |                    |     |        |
multipletimescaleswhilemaintainingstability.Traditionalcon- alloperationalmodes,aswillbefurtherexaminedinSectionV.
| trol approaches |     | designed | for slower-varying |     | loads may not |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
IV. POWERCHAINARCHITECTURE
| adequately | handle | the rapid | transitions | characteristic | of AI |     |     |     |     |     |     |     |
| ---------- | ------ | --------- | ----------- | -------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
workloads. This has driven the development of more sophisti- The power chain architecture of modern data center in-
cated control strategies that can anticipate and respond to rapid frastructures typically involves multiple cascaded conversion
power demand changes. stages, each optimized for dynamic response and tuned to
Third, protection systems must balance rapid response to achieve the necessary balance between efficiency, reliability,
potential faults with immunity to normal operation transients. and scalability. Such architectures carefully integrate converter
The fast power transitions in AI workloads can look similar topologies selected based on prevailing voltage levels, power
6

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
ratings, switching frequency constraints, desired availability, approachreducescablelossesbutintroducesdifferentprotection
andcompliancewithregionalstandards.Traditionalmulti-stage and compliance requirements [16].
implementations have long been established as reliable and Medium-Voltage AC (MVAC)-based power chain architec-
scalable solutions in a range of data center environments. tures represent a targeted evolutionary step that aims to reduce
Theseconventionalapproachesaregroundedinwell-understood the number of conversion stages and thereby improve overall
practicesanddemonstrateconsistentlyhighperformance.Mean- energy efficiency. They are often most effectively implemented
while, emerging power chain architectures, which often seek to in greenfield deployments, where the entire infrastructure can
streamlineconversionstepsandimprovesystem-wideefficiency, be designed holistically to accommodate higher distribution
are increasingly gaining attention. Yet, their broader adoption voltages. Nonetheless, regional standards play a significant role
remains subject to a variety of implementation constraints, ininfluencingthefeasibilityofthesesystems.Voltageregulation
operational complexities, and local regulatory considerations requirements, for instance, vary widely: in North America, a
that must be addressed to ensure dependable performance over ±5% tolerance is common, while some European jurisdictions
a data center’s lifespan. permit ±10% or other region-specific ranges. Similarly, the
|     |     |     |     |     |     |     |     | management | of fault | currents | becomes |     | more critical |     | at higher |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | ------- | --- | ------------- | --- | --------- |
A. AC-based Power Chain Architecture voltages,necessitatingcarefuldeviceselectionandcoordination
ofprotectionschemesthatalignwithlocalsafetyandreliability
AsdepictedinFig.6(a),anLVAC-baseddatacentertypically
standards.
| steps down   | from         | MVAC                   | (13.8kV,       | for example) |       | to 480V | or    |                |                 |          |          |              |           |             |        |
| ------------ | ------------ | ---------------------- | -------------- | ------------ | ----- | ------- | ----- | -------------- | --------------- | -------- | -------- | ------------ | --------- | ----------- | ------ |
|              |              |                        |                |              |       |         |       | Power          | quality metrics | must     | also     | be carefully |           | considered. | In     |
| 415V AC,     | then         | uses a Uninterruptible |                | Power        |       | Supply  | (UPS) |                |                 |          |          |              |           |             |        |
|              |              |                        |                |              |       |         |       | North America, | IEEE            | Standard | 519-2014 |              | generally | stipulates  | a      |
| stage before | distributing | to                     | the rack-level |              | PSUs. |         |       |                |                 |          |          |              |           |             |        |
|              |              |                        |                |              |       |         |       | Total Harmonic | Distortion      |          | (THD)    | limit        | of less   | than 5%     | at the |
The Low-Voltage AC (LVAC)-based architecture remains point of common coupling (PCC). European installations often
| the predominant |     | solution in | contemporary |     | data | center designs, |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------- | ------------ | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
refertoIEC61000-3-2orrelatedstandards,whichmayimpose
particularly in North American installations, due to historical stricter harmonic distortion limits, depending on equipment
| infrastructural | inertia       | and     | well-established |     | engineering |            | frame- |           |            |               |     |          |             |     |         |
| --------------- | ------------- | ------- | ---------------- | --- | ----------- | ---------- | ------ | --------- | ---------- | ------------- | --- | -------- | ----------- | --- | ------- |
|                 |               |         |                  |     |             |            |        | class and | load type. | Additionally, |     | regional | differences |     | in grid |
| works.          | This topology | employs | multiple         |     | cascaded    | conversion |        |           |            |               |     |          |             |     |         |
stability,powerfactorrequirements(ofteninthe0.95-0.98lead-
stages, each carefully tailored to address specific regional grid ing range), and local code compliance significantly influence
| characteristics | and | operational | demands. |     | Since | the efficiency |     |              |        |               |     |                |     |            |     |
| --------------- | --- | ----------- | -------- | --- | ----- | -------------- | --- | ------------ | ------ | ------------- | --- | -------------- | --- | ---------- | --- |
|                 |     |             |          |     |       |                |     | the ultimate | design | of MVAC-based |     | architectures. |     | Addressing |     |
of these conversion stages is closely tied to regional voltage these region-specific conditions is essential for ensuring that
standards and component design parameters, careful evaluation the chosen topology offers tangible reliability and efficiency
| of the entire | conversion | cascade | is  | necessary. | For | example, | the |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
improvements.
| initial transformation |     | from | medium-voltage |     | AC  | (MVAC) | down |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ---- | -------------- | --- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
to a 480VAC distribution level typically achieves efficiencies B. DC-based Power Chain Architecture
| between | approximately | 98.5% | and | 99.2%, | depending | on  | trans- |          |               |     |           |     |             |     |          |
| ------- | ------------- | ----- | --- | ------ | --------- | --- | ------ | -------- | ------------- | --- | --------- | --- | ----------- | --- | -------- |
|         |               |       |     |        |           |     |        | DC-based | architectures |     | introduce | the | possibility | of  | more di- |
former quality and loading conditions. rectandstreamlinedenergydeliverypathsbyeliminatingcertain
| In North | America, | the presence | of  | additional |     | transformation |     |       |           |            |        |       |        |             |     |
| -------- | -------- | ------------ | --- | ---------- | --- | -------------- | --- | ----- | --------- | ---------- | ------ | ----- | ------ | ----------- | --- |
|          |          |              |     |            |     |                |     | AC-DC | and DC-AC | conversion | stages | (Fig. | 6(b)). | Researchers |     |
stages(e.g.,from480Vto277V)canintroduceincrementaleffi- have evaluated 400V DC distribution in telco and data centers,
| ciency penalties | of  | roughly | 1-2% per | stage. | By  | contrast, | many |         |                    |     |              |     |       |       |          |
| ---------------- | --- | ------- | -------- | ------ | --- | --------- | ---- | ------- | ------------------ | --- | ------------ | --- | ----- | ----- | -------- |
|                  |     |         |          |        |     |           |      | finding | notable efficiency |     | improvements |     | [17], | [18]. | Google’s |
European implementations, which commonly use 400V/230V 400VDCrackproposallikewiseaddressesML/AIapplications
distributions, tend to have fewer intermediate steps, leading to [19], conceptually showing in Fig. 7. In practice, the realized
| slightly | higher end-to-end |     | efficiencies. | In  | Asian | deployments, |     |           |         |        |      |               |     |         |          |
| -------- | ----------------- | --- | ------------- | --- | ----- | ------------ | --- | --------- | ------- | ------ | ---- | ------------- | --- | ------- | -------- |
|          |                   |     |               |     |       |              |     | gains may | be more | modest | once | all practical |     | factors | are con- |
such as those in Japan where 200V/100V standards dominate, sidered, including the availability of DC-rated equipment, the
unique challenges arise from more frequent transformation complexity of grounding schemes, and the intricacies of safety
stages and from managing distribution losses effectively. These compliance across different markets.
regional variations demand meticulous engineering approaches Grounding requirements, for example, are highly region-
| to optimize | each | stage’s design | and | achieve | the | best | balance |     |     |     |     |     |     |     |     |
| ----------- | ---- | -------------- | --- | ------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
dependentandcanvaryfromredundantgroundpathsmandated
between efficiency, reliability, and compliance. in North America to more permissive floating DC system
Furtherdownstream,theUninterruptiblePowerSupply(UPS) configurations permitted under specific conditions in certain
stage incorporates multiple conversion processes. Modern European installations. Asian markets, with their diverse reg-
double-conversion UPS systems typically attain efficiencies ulatory landscapes, often adopt mixed approaches to grounding
| around 94-96% | at  | rated loads, | while | line-interactive |     | topologies |     |                 |         |       |           |      |      |      |         |
| ------------- | --- | ------------ | ----- | ---------------- | --- | ---------- | --- | --------------- | ------- | ----- | --------- | ---- | ---- | ---- | ------- |
|               |     |              |       |                  |     |            |     | and protection. | Voltage | level | selection | must | take | into | account |
mayreach97-98%atfullload,thoughatsomeexpenseinpower the required isolation margins—often in the range of 1.5 to 2.5
conditioning capability. In practice, data centers may operate at times the nominal voltage—as well as semiconductor device
only 30-50% of rated capacity, meaning the actual in-service ratings and the availability of DC-rated equipment that satisfies
efficiencyoftendeviatesfromtheseidealfigures.Hence,careful local regulatory frameworks.
| load profiling | and | region-specific | design | adjustments—such |     |     | as  |            |            |     |            |     |           |      |       |
| -------------- | --- | --------------- | ------ | ---------------- | --- | --- | --- | ---------- | ---------- | --- | ---------- | --- | --------- | ---- | ----- |
|                |     |                 |        |                  |     |     |     | Protection | strategies | for | DC systems |     | are often | more | chal- |
right-sizingequipmenttolocalstandards—arecriticaltoachieve lenging due to the lack of inherent zero-crossing in DC fault
intended performance targets. currents. Arc flash energy levels must be carefully managed,
In Fig. 6, one can also see the conceptual move to MVAC and the limited availability of high-current DC breakers in
distribution(middleblock)beforesteppingdowntoLVAC.This some markets can complicate device selection and compliance.
7

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
Fig.6:PowerchainofGPUclusters(coolingexcluded).Theillustrationshowsmultipleconversionstages(e.g.,MVACtoLVAC,LVACtoDC,
| and final | DC/DC | stages) | along with | potential | UPS | integration. |     |         |               |     |              |       |          |            |     |
| --------- | ----- | ------- | ---------- | --------- | --- | ------------ | --- | ------- | ------------- | --- | ------------ | ----- | -------- | ---------- | --- |
|           |       |         |            |           |     |              |     | follows | an industrial |     | perspective: | large | upstream | converters |     |
(e.g.,MVAC–LVACorUPSfront-ends)oftenhavelowercontrol
|     |     |     |     |     |     |     |     | bandwidths | and | higher            | power | ratings,   | making  | them a    | global |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------------- | ----- | ---------- | ------- | --------- | ------ |
|     |     |     |     |     |     |     |     | bottleneck | for | rapid transients. |       | Downstream | Voltage | Regulator |        |
Modules(VRMs)neartheGPUsmayswitchattensorhundreds
|     |     |     |     |     |     |     |     | of kHz,        | but their | fast                           | local loops | can only            | buffer      | small           | energy |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------------------------------ | ----------- | ------------------- | ----------- | --------------- | ------ |
|     |     |     |     |     |     |     |     | perturbations  |           | in the millisecond/microsecond |             |                     | range.      |                 |        |
|     |     |     |     |     |     |     |     | Furthermore,   |           | a load                         | jump        | is comparatively    |             | straightforward |        |
|     |     |     |     |     |     |     |     | to handle      | because   | a data                         | center      | can orchestrate     |             | a pre-charge    | or     |
|     |     |     |     |     |     |     |     | ramp-up        | sequence. | A                              | load drop,  | on the              | other hand, | can             | occur  |
|     |     |     |     |     |     |     |     | suddenly       | (e.g.,    | if a GPU                       | crash       | stops computation), |             | leaving         | the    |
|     |     |     |     |     |     |     |     | power chain    | with      | excess                         | energy      | that must           | be          | safely absorbed |        |
|     |     |     |     |     |     |     |     | or redirected. |           | Such negative                  |             | transients          | demand      | robust          | design |
considerationsintheupstream(final-stage)converter,including
|     |     |     |     |     |     |     |     | bi-directional |          | energy | paths or | advanced         | control | schemes.        | High- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ------ | -------- | ---------------- | ------- | --------------- | ----- |
|     |     |     |     |     |     |     |     | rate energy    | storage, |        | such as  | supercapacitors, |         | is particularly |       |
Fig. 7: Data center power delivery system with 400V DC bus. effective at absorbing sudden negative transients [20].
|     |     |     |     |     |     |     |     | A. Practical | PSU | Topologies |     | and Control |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ----------- | --- | --- | --- |
Groundfaultdetectionthresholdsalsovary,withacceptablesen-
| sitivities    | ranging     | from          | as low      | as 3mA        | up to      | 30mA,       | depending  |     |     |     |     |     |     |     |     |
| ------------- | ----------- | ------------- | ----------- | ------------- | ---------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| on local      | standards   | and           | operational | practice.     |            |             |            |     |     |     |     |     |     |     |     |
| Although      | a           | two-stage     | power       | chain         | (e.g.,     | direct      | 48V DC     |     |     |     |     |     |     |     |     |
| architecture) | can         | theoretically |             | reduce        | the number | of          | conversion |     |     |     |     |     |     |     |     |
| steps and     | improve     | efficiency,   |             | its practical |            | use in      | hyperscale |     |     |     |     |     |     |     |     |
| (100MW+)      | data        | centers       | remains     | to be         | verified.  | The         | high cur-  |     |     |     |     |     |     |     |     |
| rents and     | significant | distribution  |             | distances     | at         | such scales | create     |     |     |     |     |     |     |     |     |
challengesintermsofvoltagedrop,cablesizing,andequipment
| availability.  | Nevertheless, |            | smaller      | or  | specialized | deployments |           |     |     |     |     |     |     |     |     |
| -------------- | ------------- | ---------- | ------------ | --- | ----------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| (e.g., telecom |               | or edge    | sites)       | may | benefit     | from a      | two-stage |     |     |     |     |     |     |     |     |
| approach       | due           | to shorter | distribution |     | paths       | and lower   | overall   |     |     |     |     |     |     |     |     |
Fig.8:An8.5kWPSUarchitecturefromNavitas,illustratingaTotem-
| power demands. |     |     |     |     |     |     |     | Pole PFC | front-end | and | a DC/DC | stage. |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | ------- | ------ | --- | --- | --- |
V. POWERCHAINDYNAMICS
|     |     |     |     |     |     |     |     | a)  | Totem-Pole | Power | Factor | Correction | (PFC) | and | Inter- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------ | ---------- | ----- | --- | ------ |
In this paper, we define the “final stage” as the power interface leaved PFC Examples
to the utility or generator, while the “first stage” refers to Figure 8 illustrates an 8.5kW power supply that employs a
the rack-level or GPU-level power modules. This labeling totem-pole PFC topology on the AC front end, replacing the
8

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
b) Dual-Loop Control and Hold-Up Time
In a typical dual-loop control scheme for the PFC front end,
the Outer Voltage Loop maintains the desired DC bus voltage
(V ) by generating a reference current, i , proportional
BUS ref
to the load demand. In parallel, the Inner Current Loop
modulates the PWM duty cycle to shape the inductor current,
ensuring it follows i and remains sinusoidal while staying in
ref
phase with the AC input. Feedforward paths (e.g., measuring
v or predictive load monitoring) can be used to mitigate large
Fig. 9: A 12 kW PSU from Infineon, featuring advanced interleaved in
overshootsorundershootsbeforethefeedbackloopsfullyreact.
PFC and DC/DC topologies designed for high-density power conver-
sion. For example, in high-power GPU clusters, the controller may
incorporate predictions of upcoming load steps and adjust the
reference preemptively.
traditional diode bridge with a bidirectional switch leg (often Figure 10 shows the importance of hold-up time, where
using GaN or SiC devices) to reduce conduction losses [21]. a DC-link capacitor buffers the supply if there is an abrupt
Among its key design features is Reduced Bridge Losses, input failure. The capacitor keeps the Bus Voltage (V BUS )
achieved by using an active leg in place of a full diode-bridge near nominal until it discharges, and a Minimum Acceptable
rectifier. This minimizes the number of forward-voltage drops Voltage (V BUS,MIN ) ensures downstream regulators still oper-
and thereby boosts overall efficiency, which is especially vital ate. The margin between V NORM and V BUS,MIN determines
at multi-kilowatt scales. Another important aspect is the High how much energy is stored for bridging short outages (e.g.,
Switching Frequency made possible by fast-switching GaN t hold ≈ 20ms). Together, these control and design features
or SiC MOSFETs (often denoted S and S ). Operating at ensure rapid handling of load jumps and safer absorption of
1 2
higher frequencies decreases the size of magnetic components load drops, which is particularly vital in high-power data-
while still maintaining high efficiency. In addition, the totem- center applications where sudden GPU load changes occur on
pole stage provides Bidirectional Capability, allowing it to be millisecond or even microsecond timescales.
designed for partial energy return (limited by control) during
B. Small-Signal vs. Large-Signal Dynamics
negative transients such as load drops, so that some energy can
Traditionally, data center power designs rely on small-signal
flowbacktothesourceorbedissipatedinacontrolledmanner.
models linearized around a nominal operating point (e.g., 50–
Figure9highlightsa12kWPSUwithinterleavedPFCstages
80% load). For modest fluctuations, this approach suffices for
and a subsequent DC/DC converter [22]. By splitting the input
stability checks and controller tuning. However, AI workloads
current into multiple parallel phases, this interleaving scheme
can exhibit large load swings (20% → 100% → idle) on mil-
provides Current Sharing, which reduces the RMS current
lisecond timescales, making small-signal assumptions inaccu-
stressineachinductorandswitch,permittingtheuseofsmaller,
ratebecausetheoperatingpointisnolonger“close”tonominal.
more efficient components. Furthermore, phase interleaving
In industrial practice, Bode plots and phase-margin analyses
achieves Reduced Ripple on both the AC and DC sides,
remain useful for local-loop tuning, but they do not capture
leading to higher overall efficiency and lower Electromagnetic
the full nonlinear or large-signal behavior that arises during
Interference(EMI).ItalsoenablesScalability,acrucialconsid-
abruptGPUloadchanges.Consequently,systemarchitectshave
erationasdata-centerrackpowersriseintothetensofkilowatts
begun to incorporate time-domain or piecewise-linear analyses
per PSU. Interleaving is thus widely adopted in industry to
to better account for these rapid and sizable transients.
increase power density while maintaining manageable thermal
1) Representative Small-Signal Transfer Function
designs. Downstream of the PFC, the DC/DC stage often relies
Inthesmall-signaldomain,eachAC/DCorDC/DCstagecan
on resonant or soft-switching methods (e.g., LLC resonant
be approximated by:
or phase-shift full-bridge) to further improve efficiency under
moderate transients. V (s) k
G (s) ≈ o,i = i , (4)
i I (s) (cid:0) 1+ s (cid:1)(cid:0) 1+ s (cid:1)
o,i ωz,i ωp,i
where V and I are deviations around the operating point,
o,i o,i
andω andω arethezeroandpolefrequencies,respectively.
z,i p,i
Whenmultiplestagesarecascaded,theoveralltransferfunction
becomes
N
(cid:89)
G (s) = G (s), (5)
system i
i=1
thus combining the frequency responses of each power stage.
In many data center environments, the dominant (slowest) pole
is often located in an upstream converter, restricting the overall
Fig. 10: Hold-up time operation of PFCs, showing how DC-link bandwidth to only a few kilohertz—even if downstream VRMs
capacitors buffer short-term outages. can switch in the hundreds of kilohertz range or even higher.
As a result, large-signal performance often ends up limited by
9

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
the slower, high-power front-end units rather than by the fast DC-link capacitors or supercapacitors—and fast control action
local loops near the load. to maintain the DC voltage within safe limits.
During these large swings, the energy-balance perspective
C. Large-Signal Modeling and Controller Structures often proves more accurate than linear approximations. In
Modern data center power chains typically employ a hierar- particular, changes in the DC-link voltage can be expressed as
chical control strategy to handle both steady-state regulation dV (t)
and sudden transients. At the most granular level, an Inner C d d t c =i in (t)V in (t) − P load (t), (9)
Current Loop (ICL) ensures that the converter’s input or output
where C is the DC-link capacitance, i (t)V (t) is the input
currentaccuratelytracksareferencesignal,providingrapidfault in in
power, and P (t) is the instantaneous load power. If P
protection and power factor control when working with AC load load
falls drastically, e.g., due to a sudden GPU stop, the mismatch
sources. Above that, an Outer Voltage Loop (OVL) regulates
between input and load power causes V (t) to rise quickly.
theDC-linkorbusvoltagebyadjustingtheinnerloop’scurrent dc
Hence, the converter must either ramp down i or divert the
reference to match variations in load demand. Ultimately, a in
surplus energy into a resistor bank, battery, or supercapacitor—
higher-level Supervisory Control system ties together multi-
failure to do so can lead to excessive voltage spikes.
ple parallel modules, oversees battery or UPS operation, and
Nonlinear State-Space Representation.Large-signalevents
ensures compliance with grid or generator constraints. This
can be analyzed more precisely by casting the above dynamic
supervisorylayeroftencommunicateswithfacilitymanagement
equations into a general nonlinear state-space form. Let the
systems in real time, particularly in large-scale data centers.
state vector be
Before focusing on hierarchical loop structures, it is instruc-
(cid:20) (cid:21) (cid:20) (cid:21)
tive to present a comprehensive large-signal model of a final- x(t)= i L (t) , u(t)= d(t) . (10)
stage AC/DC converter rated at P rated . For simplicity, consider v dc (t) P load (t)
a single-phase AC input at voltage v (t), a rectifier stage, and
ac Then we can write x˙(t) = f(x(t),u(t)) and y(t) =
acontrolledswitch(orfull-bridge)withanoutputfilterinductor
g(x(t),u(t)),wherey(t)mightincludemeasurableoutputssuch
L feeding a DC-link capacitor C. Let
as v (t) or i (t). This nonlinear representation is particularly
dc L
• i L (t) be the inductor current, useful for analyzing operating points that deviate significantly
• v L (t) be the voltage across the inductor, from nominal conditions. It also provides the foundation for
• v dc (t) be the DC-link voltage, advancednonlinearcontrolapproaches(e.g.,sliding-modecon-
• d(t)∈[0,1] be the duty ratio, trol, feedback linearization, or Lyapunov-based methods) that
• P load (t) be the instantaneous load power (e.g., a GPU can robustly handle abrupt changes in P load (t).
load). To ensure safe and efficient operation under large-signal
A simplified set of large-signal dynamic equations for this disturbances, several control-theoretic investigations may be
power stage can be written as: employed:
L di d L t (t) =v ac,rect (t)− (cid:2) 1−d(t) (cid:3) v dc (t), (6) • P (i h L a , s v e d - c P ) la p n la e ne A , n o a n l e ys c is a : n B de y ter e m xa i m ne in h i o n w g q tr u a i j c e k c l t y or t i h e e s s i y n st t e h m e
recovers from transients. This is especially useful for
C dv dc (t) =d(t)i (t)v (t) − P (t), (7) identifying boundary conditions under extreme load steps.
dt L ac,rect load • Lyapunov Stability Criteria: Constructing a suitable Lya-
punov function can confirm global stability of the con-
where v (t) is the rectified AC input voltage. Note that
ac,rect
verter system under specific controller parameters. This is
this model assumes ideal switching and negligible losses for
valuable in data center environments where reliability is
brevity; more sophisticated versions include conduction losses,
paramount.
switching losses, and any EMI filter dynamics. These large-
signalequationshighlighthowrapidchangesind(t)orP (t) • Sliding-Mode Control: The discontinuous nature of large
load
loadstepscanbemitigatedbyforcingthesystemto“slide”
can directly impact both i (t) and v (t). Such a state-space
L dc
along a predefined manifold, offering robustness against
formulation is crucial for understanding transient phenomena
parameter variations and sudden transients.
that small-signal linearizations may overlook.
One way to formalize the hierarchical loops acting on this • Feedback Linearization: By algebraically transforming the
nonlinear system, feedback linearization methods can help
converter is to note that the outer voltage loop calculates an
achieve linear-like performance over a wide operating
error,
range. This approach is particularly powerful if precise
e (t)=V −V (t), (8)
v dc,ref dc knowledge of system parameters is available.
and transforms this into a reference current i (t) via a com- Extended Energy-Balance Control. Beyond simply regu-
ref
pensator K (s). In turn, an inner current loop compares i (t) lating voltage or current setpoints, an extended energy-balance
v in
withi (t),andacompensatorK (s)generatesthePWMduty controlframeworkincorporatesadditionalactionstomanagethe
ref i
ratio d(t). While small-signal models and frequency-domain flowofsurplusordeficitenergy.Forinstance,whenP drops
load
analysis provide a baseline for loop design and stability, large- sharply, an adaptive feedforward term can modulate K (s) or
i
signal events such as a GPU load swing from near-idle to full K (s) to quickly reduce the input current, thus minimizing
v
capacity can cause sudden changes in i . Addressing these overshoot in V (t). Conversely, when the load spikes rapidly,
ref dc
abrupt shifts demands robust energy buffering—through bulk the feedforward signal can preemptively boost the converter’s
10

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
current reference to mitigate under-voltage dips. This holistic ω , the slowest stage effectively sets the pace for system-level
c,i
viewpoint of energy transfer also allows for coordinated use of transients:
(cid:0) (cid:1)
local storage elements (e.g., supercapacitors) that can further ω ≈ min ω . (11)
cl c,i
1≤i≤N
buffer large power swings.
Predictive and Constraint-Based Strategies. When large If the final-stage converter’s control bandwidth is much lower
transients are frequent or have tight performance requirements, thanthatoftheVRM,theentiredatacenterpowerchainremains
model predictive control (MPC) offers a flexible solution. By bottleneckedbytheslowerunit.Inindustrialdatacenters,where
numerically optimizing a cost function over a finite horizon, multipleMWsofpowermightbesuppliedbyparalleledAC/DC
the controller can account for real-time system constraints modules, this constraint poses a practical limit on how quickly
(e.g., current and voltage limits) and compute the optimal large load swings can be supported without risking system
duty cycle d(t). This predictive method is particularly effective instability or voltage excursions.
at maintaining safe operating conditions under sudden GPU 1) Dominant Power Stage Dynamics
load ramps or drops, where classical linear compensators may While downstream loops might settle in just a few mi-
struggle with rapid nonlinear dynamics. In addition, constraint- croseconds, the outer voltage loop of the upstream converter or
handling ensures that key limits are never violated, which is UPS may require hundreds of microseconds—or even millisec-
critical for protecting both the power electronics and the load. onds—to react fully to a large load jump. For instance, when a
GPUloadrisesfrom20%to100%inafractionofamillisecond,
CoordinatedSupervisoryActions.Onahigherlevel,super-
local bus capacitors have to supply the initial current surge. If
visory controllers can integrate large-signal models into their
the surge endures, the final stage begins ramping its AC input
decision-making. By continuously monitoring predicted load
current. Conversely, if the load drops abruptly from 100% to
profiles, the supervisory layer can schedule power module
20% or even near-zero, the system faces a sudden surplus of
activation or coordinate energy storage dispatch (e.g., batteries,
energy in the DC link. Quickly redirecting or dissipating this
supercapacitors) to absorb or supply transient power. In cases
surplus is a major challenge: otherwise, the DC voltage can
where multiple parallel converter modules operate in tandem,
spike, triggering protective shutdowns or damaging hardware.
thecontrollercandynamicallyredistributeloadamongmodules
In particular, negative transients pose serious risks when bat-
tospreadoutthermalandelectricalstresses,enhancingbothsys-
teryorUPSsystemsaredesignedmainlyforoutageprotection,
tem resilience and efficiency. Moreover, advanced supervisory
i.e.,dischargingratherthanchargingathighrates.AGPUcrash
policies may anticipate large load steps by pre-charging energy
or job completion might halt a load consuming hundreds of
storage elements, thereby reducing the magnitude of transients
kilowatts, causing
seen by downstream converters.
dV
Overall, the large-signal model and the associated control C dc > 0, (12)
dt
strategies introduced above underscore the complexity of pow-
which leads to a voltage swell unless the incoming power is
ering modern data centers. While classic small-signal analy-
quickly curtailed. Active control can reduce i at the AC/DC
ses remain crucial for nominal design and linearized stability in
stage,whiledissipativeelementsorbi-directionalenergystorage
checks, the nonlinear nature of massive load swings requires
systems (BESS) can help safely absorb the excess. Failure to
complementary methods such as energy-balance principles,
handle these negative transients can produce nuisance tripping
phase-plane investigations, and predictive optimization. Future
of protective circuits or outright hardware failure.
work may focus on unifying these approaches into a cohesive
2) Transient Scenarios and Rapid Load Changes
framework that seamlessly handles both routine regulation and
Large load swings typically manifest as either positive tran-
worst-case fault scenarios.
sients (ramp-up) or negative transients (ramp-down). In a pos-
itive transient, such as a GPU jumping from idle to near-TDP,
D. Cascaded Power Stage Analysis and System Dominance local capacitors buffer the immediate surge, and the final stage
ramps up gradually to replenish the DC-link voltage. Often,
Data center power typically flows through multiple stages, techniques like pre-charging or staged enable sequences are
for instance: MVAC→LVAC→48V→12V→GPU. Each stage employed to limit inrush currents.
contains its own inductors, capacitors, and control loops, all Negativetransientsaregenerallymorecritical.Whentheload
of which influence how quickly or slowly power can ramp. dropsabruptly—whetherintentionally,throughnormaljobcom-
The final-stage AC/DC converter, or UPS, often incorporates pletion, or unexpectedly, via a GPU fault—P can plummet
load
large magnetics to handle high power levels and thus cannot from a high value to near-zero. In some industrial systems, a
change its current as fast as smaller downstream regulators. predictive controller might use GPU job-scheduling signals to
Meanwhile, local VRMs at the GPU boards can respond in anticipate an impending load reduction, issuing commands to
microseconds but have limited energy storage. Consequently, reduce i or route current into a fast-charging storage element.
in
when a GPU suddenly demands an enormous current jump, the Without these measures, the DC-link voltage can spike within
localcapacitorsabsorbtheimmediatesurge,whiletheupstream microseconds or milliseconds, potentially leading to equipment
source gradually ramps its input current within the confines of damage.
its bandwidth. Prolonged heavy load then propagates upstream Finally, the special case of a sudden load drop—where the
once the small buffers at the VRM stage are depleted. GPU instantly ceases consumption—represents the worst-case
The concept of overall bandwidth constraint emerges from scenario for many power designs. Unless the excess energy
thiscascade.Sinceeachstagehasacertaincrossoverfrequency is dumped or stored in a matter of microseconds, the rapid
11

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
rise of V (t) may exceed design tolerances. Therefore, ro- ii) AggregatedJouleDemand:WhileonePSUmighthandle
dc
bust negative-transient handling often includes resistor dump a 9J transient gracefully, a synchronized load transition
circuits, supercapacitor banks, or bi-directional batteries with across 10 PSUs would require 90J, and a larger row or
high charge acceptance capability. Such solutions improve the entire data hall might demand thousands of joules over
overall reliability and stability of AI-oriented data centers by the same short interval. If the sum of all PSU buffers
ensuring safe operation even under extreme load transitions. is insufficient, large upstream voltage swings or nuisance
|        |         |            |           |     |     |     |     |     | trips         | can result. |     |           |        |               |     |
| ------ | ------- | ---------- | --------- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | --------- | ------ | ------------- | --- |
|        |         | VI.        | CASESTUDY |     |     |     |     |     |               |             |     |           |        |               |     |
|        |         |            |           |     |     |     |     |     | iii) Dominant | Role        | of  | the Final | Stage: | As emphasized | in  |
| A. PSU | Inertia | Case Study |           |     |     |     |     |     |               |             |     |           |        |               |     |
SectionV,these“rack-level”PSUsorpowershelvesareef-
While the preceding sections have presented a theoretical fectivelythefinalpower-conversionstage,bridgingthedata
viewofdatacenterpowerdynamics,itisinstructivetoexamine center’s 208–480V supply (or MVAC in some topologies)
a concrete example of how a single power supply unit (PSU) and the GPUs. Their 30–50ms bandwidth thus bounds
buffers abrupt GPU load transitions in practice. Such “inertia,” the fastest net power swing the upstream infrastructure
on the order of a few tens of milliseconds, can be directly must handle. Consequently, multi-rack concurrency can
measured by comparing the GPU’s motherboard (DC) current still produce large sub-second transients that propagate
against the PSU’s single-phase AC input current. Figures 11b, back to the utility interface.
11a, and 11c showcase distinct operating points of the single- Need for Additional Buffers and Controls
phasePSUfeedingaGPUmotherboard.Theconsolidatedview Although tens-of-milliseconds smoothing is useful for indi-
in Figure 11 demonstrates the tens-of-milliseconds lag in the vidual GPU load steps, it may not suffice when large clusters
PSU’s AC input current whenever the GPU load steps rapidly createnear-simultaneouspowersurgesinthemulti-kWormulti-
on the 12V rail. The example provided here features a 1kW MWrange.Therefore,operatorstypicallydeployadditionalfast
Gold-rated PSU powering a single NVIDIA-class GPU, but the energy storage or advanced scheduling, including:
| same principles |     | hold for    | larger | AI compute   |     | nodes. |     |     |             |         |            |                 |          |                |     |
| --------------- | --- | ----------- | ------ | ------------ | --- | ------ | --- | --- | ----------- | ------- | ---------- | --------------- | -------- | -------------- | --- |
|                 |     |             |        |              |     |        |     |     | • High-Rate | Energy  | Storage:   | Supercapacitors |          | or specialized |     |
| Single-PSU      |     | Measurement |        | and Analysis |     |        |     |     |             |         |            |                 |          |                |     |
|                 |     |             |        |              |     |        |     |     | battery     | systems | can absorb | or deliver      | multiple | kilowatts      | (or |
a) Observed Load Step (GPU Rail). megawatts) for a few seconds, bridging any shortfall that the
| In Fig. | 11, | the GPU | rail current, |     | I   | , abruptly | increases |     |      |              |         |     |     |     |     |
| ------- | --- | ------- | ------------- | --- | --- | ---------- | --------- | --- | ---- | ------------ | ------- | --- | --- | --- | --- |
|         |     |         |               |     | GPU |            |           |     | PSUs | alone cannot | handle. |     |     |     |     |
from around 5A to nearly 20A. Assuming a 12V rail, this Staggered Workload Coordination: HPC or AI schedulers
•
| corresponds     | to  | a load-step | of       | roughly | 180W.   | The | GPU    | tran- |             |                      |     |              |            |                      |         |
| --------------- | --- | ----------- | -------- | ------- | ------- | --- | ------ | ----- | ----------- | -------------------- | --- | ------------ | ---------- | -------------------- | ------- |
|                 |     |             |          |         |         |     |        |       | may stagger | checkpoints          |     | or batch     | boundaries | so that              | not all |
| sitions between |     | partial     | idle and | active  | compute |     | within | a few |             |                      |     |              |            |                      |         |
|                 |     |             |          |         |         |     |        |       | GPUs        | ramp simultaneously, |     | distributing |            | the load transitions |         |
milliseconds. over a few hundred milliseconds to avoid huge instantaneous
| b)  | PSU “Lag” | on  | the AC | Input. |     |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
steps.
| The PSU’s | AC  | input | current, | I , | does not | mirror | this | abrupt |          |     |            |     |         |                     |     |
| --------- | --- | ----- | -------- | --- | -------- | ------ | ---- | ------ | -------- | --- | ---------- | --- | ------- | ------------------- | --- |
|           |     |       |          | in  |          |        |      |        | Enhanced | UPS | Solutions: | UPS | systems | with high slew-rate |     |
•
180Wriseinrealtime.Instead,itremainsnearitsoldamplitude designs and partial supercapacitor banks can further buffer
| for about | 1–2 | AC cycles | (20–40ms) |     | before | ramping | to  | match |                |     |          |             |            |         |     |
| --------- | --- | --------- | --------- | --- | ------ | ------- | --- | ----- | -------------- | --- | -------- | ----------- | ---------- | ------- | --- |
|           |     |           |           |     |        |         |     |       | large negative | or  | positive | transients, | minimizing | voltage | ex- |
thenewload.Insomecaptures,thislagmayextendto∼50ms, cursions on the facility bus.
| indicating | that      | the PSU’s | internal | bus    | capacitors |           | and | control |         |       |            |           |       |              |      |
| ---------- | --------- | --------- | -------- | ------ | ---------- | --------- | --- | ------- | ------- | ----- | ---------- | --------- | ----- | ------------ | ---- |
|            |           |           |          |        |            |           |     |         | Without | these | additional | measures, | large | data centers | risk |
| loops are  | providing | the       | extra    | energy | (or        | absorbing | it, | in the  |         |       |            |           |       |              |      |
transientovervoltages,under-voltages,orexcessiveflickeratthe
| case of | a negative | step). | This | timescale | effectively |     | defines | the |          |              |            |             |     |                    |     |
| ------- | ---------- | ------ | ---- | --------- | ----------- | --- | ------- | --- | -------- | ------------ | ---------- | ----------- | --- | ------------------ | --- |
|         |            |        |      |           |             |     |         |     | PCC with | the utility, | ultimately | threatening |     | system reliability |     |
PSU’s “inertia.”
|     |          |           |         |     |     |     |     |     | and potentially | violating |     | grid standards. | Thus, | while | a single |
| --- | -------- | --------- | ------- | --- | --- | --- | --- | --- | --------------- | --------- | --- | --------------- | ----- | ----- | -------- |
| c)  | Estimate | of Stored | Energy. |     |     |     |     |     |                 |           |     |                 |       |       |          |
PSU’s30–50msinertiaissufficienttosmoothoutmicrosecond-
| We can | approximate |     | how | many | joules | the PSU’s |     | internal |           |             |         |     |               |     |        |
| ------ | ----------- | --- | --- | ---- | ------ | --------- | --- | -------- | --------- | ----------- | ------- | --- | ------------- | --- | ------ |
|        |             |     |     |      |        |           |     |          | level GPU | transients, | scaling | up  | to multi-rack | or  | multi- |
capacitorsdeliverduringthat30–50msmismatchbycomputing
|     |     |     |     |     |     |     |     |     | megawatt | loads demands |     | supplementary | power-engineering |     | so- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ------------- | ----------------- | --- | --- |
∆E ≈ (∆P)×(∆t) = (180W) × (0.05s) = 9J. (13) lutions to maintain stable, compliant operation.
This estimate aligns well with typical bulk-capacitor values in B. Practical Considerations
1–2kW server or workstation PSUs, which often store on the 1) UPS Battery Limitations
| order of | 5–15J. | For sudden | load | drops, | this | same | buffer | must |      |             |     |          |               |      |          |
| -------- | ------ | ---------- | ---- | ------ | ---- | ---- | ------ | ---- | ---- | ----------- | --- | -------- | ------------- | ---- | -------- |
|          |        |            |      |        |      |      |        |      | Many | UPS systems | are | designed | for discharge | over | minutes, |
absorborshunttheexcessenergytopreventabus-voltagespike. rather than for rapid charging over a span of milliseconds.
Scaling to Rack-Level and Beyond Becausetheirchargecurrentistypicallylimited,alargenegative
| Although | this | measurement |     | involves | a single |     | GPU + | single |           |             |      |              |             |      |     |
| -------- | ---- | ----------- | --- | -------- | -------- | --- | ----- | ------ | --------- | ----------- | ---- | ------------ | ----------- | ---- | --- |
|          |      |             |     |          |          |     |       |        | transient | can quickly | lead | to a DC-link | overvoltage | when | the |
PSU, the fundamental notion of a ∼50ms buffering timescale load drops abruptly. To mitigate such scenarios, several high-
generalizes to larger AI systems: rateenergy-absorptionmethodscanbeemployed.Oneoptionis
i) Parallel Power Shelves:Inarackconsuming10–350kW, toincorporatesupercapacitors,whicharecapableofacceptinga
several PSUs or power shelves (often 5–15kW each) sudden influx of energy thanks to their high charge acceptance.
operate in parallel. Each still features tens of milliseconds Another possibility is to deploy dedicated dump resistors or
of “local inertia.” However, the aggregate load step from braking modules that can safely dissipate excess power when a
multiple GPUs can easily climb to tens or hundreds of load drop occurs. A further alternative is to use enhanced bi-
kilowatts if many GPUs initiate or end a compute phase directionalbatteriesthatcantolerateshortburstsofhigh-current
simultaneously. chargingwithoutcompromisingbatteryhealth.Inpractice,these
12

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
(a)Longertime-scalecaptureshowingrepeatedtransitions.
(b)ZoomedviewoftheGPUcurrentsteppingfrom∼5Ato20+A.
(c)Furtherzoomonthenegativetransientregion(3.5–3.75s).
Fig. 11: Empirical PSU inertia example from single-phase 120V supply to a 12V GPU rail. (a) A rapid load step on the GPU side, while
the PSU input current lags by tens of milliseconds. (b) An extended capture of multiple load surges. (c) Closer look at negative transients,
illustrating PSU hold-up capability.
strategies must be coordinated through a battery management fully coordinated. Supervisory control layers typically manage
system (BMS) that can handle rapid switching between dis- theseparallelmodulesbyadjustingreferencesignalstomaintain
charge and charge modes; however, thermal management and balanced bus voltages and avoid overstressing any single unit.
cycle-lifeconsiderationsoftencomplicatethedesignandcontrol In some cases, advanced scheduling or load shedding policies
of such BMS solutions. are employed to stagger large GPU load transitions, thereby
2) Coordination of Multiple Stages reducingthemagnitudeofsimultaneousramp-uporramp-down
Large-scale data centers commonly rely on multiple AC/DC events.Thisapproachhelpsmaintainmorestablepowerdelivery
modulesoperatinginparallel—oftenintherangeof50–100kW and alleviates sudden demand surges that could exceed the
each—to reach total capacities of several megawatts. Although module-level or facility-level bandwidth limits.
eachmodulehandlesonlyafractionofthetotalload,rapidload
changes can still cause localized voltage transients if not care-
13

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
3) Analytical Sizing and Stability element cannot supply (or absorb) power rapidly enough. In
Designingrobustenergystorageisacrucialaspectofprevent- such scenarios, data-center designers may need to rely on a
ing unwanted voltage excursions. For example, if a data center combination of storage technologies or fall back on alternative
requires a hold-up time t at a peak power draw P , the supplies to prevent large voltage dips or spikes. By analyzing
hold peak
necessary bus capacitance C can be estimated by ∆E (t) against the capabilities of capacitors, batteries,
mismatch
or other storage options, it becomes feasible to identify where
2P t
C ≥ peak hold . (14) a single ESS type falls short and where hybrid or tiered energy
V2 −(V −∆V )2
dc dc storage arrangements are necessary.
A larger capacitance can help manage voltage droop during
positiveloadsteps,butnegativetransientsalsobecomeafactor, B. Implications for Large-Scale GPU Deployments
sincetheallowablevoltagerise∆V up dictateshowmuchenergy In large data centers that house thousands of GPUs, the
storage or absorption capability is needed. Similar constraints load profile can feature a wide range of transient behaviors.
apply to supercapacitors or batteries, where the maximum Fast bursts on the order of microseconds to milliseconds often
charge rate determines how rapidly they can accept surplus reach tens of kilowatts or more per server rack; to buffer these
power during load drops. rapid events locally, operators rely on supercapacitors or low-
Control stability, on the other hand, hinges on maintaining inductancebusbarsthatsupplyorabsorbsuddencurrentsurges.
adequate phase margin in each power stage, particularly at Meanwhile, multi-second spikes in demand can occur during
high load levels. Although raising the crossover frequency can collective GPU tasks such as synchronized AI training steps
improve transient response, pushing it too high risks destabi- or HPC job orchestration, where rack-level power consumption
lizing the overall system—especially when multiple modules mayexceednominallevelsbyasubstantialmargin.Ifthegridor
are cascaded. Consequently, industry practice often sets con- front-end PFC stage cannot respond quickly enough, batteries
servative gain and phase margins (for example, ≥ 60◦) at or or large-scale flow batteries at the facility level are expected
near peak load to ensure that the power chain does not become to cover this mismatch. For even longer disruptions, typically
oscillatoryduringabruptGPUworkloadtransitions.Thistrade- lastingminutestohours,dieselorgasgeneratorscomeintoplay,
off between fast response and stable operation underscores the though these generators have comparatively slower response
significance of “final-stage” bandwidth: no matter how rapidly times and may not address sudden load transients on very
downstream VRMs can respond, the slower dynamics of large short timescales. By carefully computing ∆E (t) based
mismatch
upstream converters will ultimately bound the speed at which ontypicalworkloadandrampprofiles,data-centerdesignerscan
load variations can be accommodated safely. pinpoint how much of the load must be supported by different
energy-storage tiers.
VII. DISCUSSIONSANDOUTLOOKS
A. Quantifying the Mismatch Between Load Dynamics and C. Recommendations for Design and Integration
Energy Storage System (ESS) Capabilities Hybrid energy storage architectures are emerging as a robust
It is important to note how different energy storage tech- solution to the time-scale mismatch problem. One effective
nologies, such as capacitors, supercapacitors, lithium-ion bat- strategy combines supercapacitors, which excel at providing or
teries, flow batteries, and diesel generators, each operate most absorbing power surges that last only microseconds to a few
effectivelyoverparticulardischargedurationsandpower/energy seconds,withlargerbatterybanksthatcansustainmulti-second
levels. At one extreme, capacitors and supercapacitors deliver bridging. On-site diesel or gas generators then serve extended
high power in sub-second intervals, making them suitable for outages or peak-shaving operations. Dynamically allocating the
very rapid load changes on the order of microseconds to mil- portion of load each storage layer handles requires a fast
liseconds.Attheotherextreme,dieselgenerators(andsimilarly supervisory controller that engages supercapacitors for very
large engine-based systems) support moderate power for much short bursts and shifts responsibility to battery storage if the
longer durations, such as minutes to hours, thereby address- demand persists. At the same time, matching the slew rate of
ing extended outages or peak-shaving needs. AI accelerators the final-stage converter to these storage devices is essential.
like GPU-based clusters, however, often exhibit dynamic load Thisentailsusingtopologiessuchastotem-poleorbidirectional
patterns that include both rapid bursts of activity in the sub- PFC configurations and selecting semiconductor switches rated
millisecond range and multi-second surges for collective tasks. to handle large negative transients without damage.
Consequently,asingleenergystoragesolutiongenerallycannot Sizingeachenergystoragelayereffectivelyinvolvesapplying
optimize performance across all these time and power scales. themismatchanalysistoexpectedloadscenarios.Ifshortbursts
To quantify whether a particular ESS technology can ade- exceed the cumulative storage or discharge capability of local
quatelymeetaloadtransient,itishelpfultointegratethepower bus capacitors, then designers must ensure supercapacitors or
differenceovertherelevanttimeperiod.Specifically,themetric similarly high-rate solutions can capture that surge. Likewise,
if multi-second intervals surpass battery capacity, an additional
(cid:90) t
(cid:2) (cid:3)
∆E (t)= P (τ)−P (τ) dτ (15) layer of storage or on-site generation is needed. Finally, the
mismatch demand supply
0 ability to expand infrastructure incrementally is critical as
captures how much extra energy is required (when HPC and AI clusters grow in computational and power de-
∆E (t) > 0) beyond what the ESS can deliver. mands. By designing battery cabinets, supercapacitor modules,
mismatch
Fast load transients, such as those common in GPU workloads, and distribution buses in a modular fashion, data centers can
can lead to significant short-term mismatches if the storage adapt to increasing load envelopes with minimal disruption
14

This draft is under active development as followup of ongoing project: https://github.com/chennnnnyize/LLM Impact Energy Systems
to existing operations. In essence, carefully quantifying the [9] SchneiderElectricandNVIDIA,“AIReferenceDesignstoEnableAdop-
dynamic mismatch between load and supply (via Eq. 15) and tion,” Schneider Electric, Reference Design, 2024. [Online]. Available:
https://www.se.com/ww/en/download/document/AI Reference Designs/
distributing storage responsibilities among multiple ESS tiers
[10] Hewlett Packard Enterprise, HPE Cray Supercomputing EX, Hewlett
yields both improved resilience and greater efficiency, ensuring Packard Enterprise, 2024. [Online]. Available: https://www.hpe.com/us/
that sudden load ramps in GPU clusters do not compromise en/compute/hpc/supercomputing/cray-exascale-supercomputer.html
[11] Schneider Electric, “EcoStruxure Reference Design 109: 7392 kw, Tier
system performance or reliability.
III,NAM,ChilledWater,Liquid-CooledAIClusters,”SchneiderElectric,
Reference Design, 2024. [Online]. Available: https://www.se.com/id/en/
VIII. CONCLUSIONS
download/document/RD109DSR0 EN/
This paper has examined the critical interplay between AI [12] Vertiv,“360AIBrochure:AccelerateYourAIDeployment,”Vertiv,Prod-
uct Brochure, 2024. [Online]. Available: https://www.vertiv.com/4a51e3/
workload dynamics and power electronics in modern data
globalassets/documents/brochures/vertiv-360ai-brochure-sl-71291.pdf
centers, demonstrating that final-stage power conversion char- [13] ——, “Data Center 2025: Closer to the Edge,”
acteristicsoftenconstitutethefundamentalbottleneckinsystem Vertiv, Technical Report, 2019. [Online]. Avail-
able: https://www.vertiv.com/en-us/about/news-and-insights/articles/
response capabilities. Through empirical measurements and
pr-campaigns-reports/data-center-2025-closer-to-the-edge/
theoretical analysis, we have shown that typical PSU imple- [14] Hammerspace, “Accelerate Your AI Workflows with Hammerspace,”
mentations exhibit a built-in ”inertia” that limits power sys- Hammerspace, Technical Guide, 2024. [Online]. Available: https:
//hammerspace.com/accelerate-your-ai-workflows-with-hammerspace/
tem adaptability, regardless of downstream VRM performance.
[15] D. Gu, X. Xie, G. Huang, X. Jin, and X. Liu, “Energy-Efficient GPU
Our investigation reveals that GPU clusters create uniquely Clusters Scheduling for Deep Learning,” 2023. [Online]. Available:
challenging load patterns—from microsecond-level inference https://arxiv.org/abs/2304.06381
[16] HiPerGuard MV UPS User Manual, ABB, 2024. [Online]. Available:
transientstosustainedtraining-relatedpowerswings—thatpush
https://library.abb.com/r?cid=9AAC190686
conventional power architectures beyond their original design [17] A.Pratt,P.Kumar,andT.V.Aldridge,“Evaluationof400vDCdistribu-
parameters. While individual VRMs achieve microsecond re- tionintelcoanddatacenterstoimproveenergyefficiency,”inINTELEC
07-29thInternationalTelecommunicationsEnergyConference,2007,pp.
sponses, the cascade of conversion stages in data center power
32–39.
chains remains constrained by upstream converter bandwidth, [18] N. Rasmussen and J. Spitaels, “A Quantitative Comparison of
typicallyinthekilohertzrange.Thislimitationbecomesparticu- High Efficiency AC vs. DC Power Distribution for Data Centers,”
Schneider Electric, White Paper, 2024. [Online]. Available: https:
larlyacuteinlarge-scaledeploymentswheresynchronizedGPU
//www.se.com/us/en/download/document/SPD NRAN-76TTJY EN/
operations can create facility-wide power transients. Looking [19] X. Li and K. Ravikumar, “400v DC Rack Power System for ML/AI
ahead, emerging solutions incorporating wide-bandgap devices, Application,” in 2024 Open Compute Project (OCP) Global Summit.
Open Compute Project, 2024, google’s proposed 400V DC distribution
advanced control schemes, and hybrid energy storage systems
andracksolutionaimstoenhancedatacenterdensityandefficiency.
showpromiseinbridgingthegrowinggapbetweenAIworkload [20] J. Lee, “Ultracapacitor Applications for Uninterruptible Power
dynamics and power delivery capabilities—a critical consider- Supplies (UPS),” Maxwell Technologies, White Paper, 2021. [Online].
Available: https://maxwell.com/wp-content/uploads/2021/08/whitepaper
ation as data centers continue scaling to meet unprecedented
application for ups.pdf
computational demands. [21] NavitasSemiconductor,8.5kWAIPSU2-Pager,NavitasSemiconductor,
November 2024, datasheet. [Online]. Available: https://navitassemi.com/
REFERENCES
wp-content/uploads/2024/11/8.5-kW-AI-PSU-2-Pager-1.pdf
[22] Infineon Technologies, “OktoberTech 2024 Silicon Valley -
[1] U.S. Department of Energy, “Recommendations on Powering Artificial
Demos,” Infineon Technologies, Technical Report, 2024. [Online].
Intelligence and Data Center Infrastructure,” U.S. Department of
Available: https://tradeshows.infineon.com/oktobertech24 siliconvalley/
Energy, Technical Report, July 2024, presented to the Secretary of
demos/0657b274-f15a-4533-832d-01e5034ab6a0
Energy on July 30, 2024. [Online]. Available: https://www.energy.gov/
sites/default/files/2024-08/Powering%20AI%20and%20Data%20Center%
20Infrastructure%20Recommendations%20July%202024.pdf
[2] ABB. (2024, May) AI-Driven Data Center
Boom Triggers Unprecedented Demand for Power.
[Online]. Available: https://new.abb.com/news/detail/115913/
ai-driven-data-center-boom-triggers-unprecedented-demand-for-power
[3] Y.Li,M.Mughees,Y.Chen,andY.R.Li,“TheUnseenAIDisruptions
for Power Grids: LLM-Induced Transients,” 2024. [Online]. Available:
https://arxiv.org/abs/2409.11416
[4] Goldman Sachs & Co. LLC, “AI, Data Centers and the
Coming US Power Demand Surge,” Goldman Sachs &
Co. LLC, Research Report, April 2024. [Online]. Available:
https://www.goldmansachs.com/insights/goldman-sachs-research/
generational-growth-ai-data-centers-and-the-coming-us-power-demand-surge
[5] ElectricPowerResearchInstitute,“PoweringIntelligence:AnalyzingAr-
tificialIntelligenceandDataCenterEnergyConsumption,”ElectricPower
ResearchInstitute,TechnicalReport,May2024.[Online].Available:https:
//restservice.epri.com/publicdownload/000000003002028905/0/Product
[6] R. Caspart, S. Ziegler, A. Weyrauch, H. Obermaier, S. Raffeiner, L. P.
Schuhmacher, J. Scholtyssek, D. Trofimova, M. Nolden, I. Reinartz,
F. Isensee, M. Go¨tz, and C. Debus, “Precise Energy Consumption
MeasurementsofHeterogeneousArtificialIntelligenceWorkloads,”2022.
[Online].Available:https://arxiv.org/abs/2212.01698
[7] S. Balaban, “How to Build a GPU Cluster from Scratch for Your
ML Team,” Lambda, Technical Guide, June 2020. [Online]. Avail-
able: https://files.lambdalabs.com/How%20to%20build%20a%20GPU%
20cluster%20from%20scratch%20for%20your%20ML%20team.pdf
[8] DriveNets, “Guide for Building an 8k GPU Cluster with Network
Cloud-AI,”DriveNets,TechnicalGuide,2024.[Online].Available:https:
//www.drivenets.com/resources/white-papers/ai-cluster-reference-design/
15