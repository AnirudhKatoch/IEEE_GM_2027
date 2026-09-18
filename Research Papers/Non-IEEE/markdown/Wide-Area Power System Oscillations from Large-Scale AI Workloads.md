arXiv is now an independent nonprofit! Learn more (https://info.arxiv.org/about)  ×
Why HTML?
(https://info.arx
iv.org/about/ac
|              | RReeppoorrtt | BBaacckk  ttoo   | DDoowwnnllooaadd |
| ------------ | ------------ | ---------------- | ---------------- |
| cessible_HTM | IIssssuuee   | AAbbssttrraacctt | PPDDFF           |
L.html)
License: CC BY 4.0 (https://info.arxiv.org/help/license/index.html#licenses-available)
arXiv:2508.16457v2 [eess.SY] 20 Apr 2026

Wide-Area Power System Oscillations
from Large-Scale AI Workloads
Hao Zhu
†
[†This work has been supported by NSF grants
2130706 and 2150571 (Corresponding Author: Hao
Zhu.)]
Min-Seung Ko
†
[†M.-S. Ko and H. Zhu are with the Chandra Family
Department of ECE, The University of Texas at
Austin, Austin, TX 78712, USA. (e-mail:
kms4634500@utexas.edu, haozhu@utexas.edu)]
Abstract
This paper develops a new dynamic power profiling approach for modeling AI-
centric datacenter loads and analyzing their impact on grid operations, particu-
larly their potential to induce wide-area grid oscillations. We characterize the peri-
odic stochastic power fluctuations inherent to large-scale AI workloads during
both the training and fine-tuning stages, driven by the state-of-the-art graphics
processing unit (GPU) computing architecture design. These sustained, large
power fluctuations, unlike conventional load ramping, act as persistent forcing in-
puts capable of interacting with and amplifying local and inter-area oscillation
modes. Using the WECC 179-bus system and the NPCC 140-bus system, we
have numerically studied the amplitude and variability of oscillatory responses un-
der different factors. These factors include system strength, penetration level,
fluctuation frequency range, individual datacenter size, geographical deployment,
fluctuation suppression level, and workload ratio. Simulation results show that,
notably, narrower fluctuation bands, larger single-site capacities, or dispersed sit-
ing can intensify oscillations across multiple modes. Our models and numerical
studies provide a quantitative basis for integrating AI-dominant electricity demand
into grid oscillation studies and further support the development of new planning
and operational measures to power the growth of AI/computing load demands.
Index Terms: : AI workload, datacenter, forced oscillation, load fluctuation,
stochastic modeling, wide-area oscillation.

I Introduction
The rapid growth of large electrical loads, such as datacenters, cryptomining fa-
cilities, and transportation electrification, is fundamentally shifting the composi-
tion and characteristics of electricity demand. In particular, datacenters have
emerged as a primary driver of large-load growth, due to the explosion of AI ap-
plications and large language models (LLMs) [1, 2]. By the end of 2030, data-
center electricity demand is projected to account for up to 12% of total US elec-
tricity consumption [3, 4]. Unlike conventional industrial loads, datacenter
power profiles typically exhibit fast, sustained fluctuations with multi‑timescale
variability driven by workload orchestration and scheduling changes [5]. These
unique patterns significantly challenge the grid operational paradigm in power
balancing and dynamic control, and introduce new grid reliability considera-
tions. Hence, there is an urgent need to develop a comprehensive framework
for modeling datacenter electricity demand and assessing its potential impact
on grid dynamic performance [1, 2].

 
Along these lines, the majority of current research and industry assessments
focus on large ramping behaviors and transient stability analysis. Abrupt work-
load initiation, shutdown, and inter-site transfers result in stepwise power
changes that can significantly affect grid stability, especially with very high data-
center penetration [6]. This issue has been already observed in major US inter-
connections such as electric reliability council of Texas (ERCOT), western elec-
tricity coordinating council (WECC), and Pennsylvania-New Jersey-Maryland
(PJM) interconnection, where datacenter-initiated load shifts have caused mea-
surable frequency and voltage disturbances [7, 8]. For example, graphics pro-
cessing unit (GPU)-level power dynamics from AI workloads have been ana-
lyzed in [1], which points out the potential stress on local grids. A combined
modeling approach that incorporates both batch load patterns and AI-induced
fluctuating demand is presented in [6], showing that sudden demand variations
can be mitigated by adjusting the speed of frequency changes. To the best of
our knowledge, most existing work on datacenter variability has focused solely
on the effects of ramp power changes on power system transient responses.

 
Notably, the grid dynamics arising from the rapid increase in datacenter de-
mand and growing variability go far beyond ramping transients. With the latest
explosions in large generative AI (GenAI) models and LLMs, next-generation

super datacenters are increasingly being deployed and connected to power
systems [9]. Their GW-level power capacity not only significantly strains re-
source adequacy but also critically affects grid operations, leading to a vast in-
crease in datacenter-induced power fluctuations that have not been seen in
power systems thus far [10]. More recent technical assessments [11, 2] have
started to recognize this urgent concern and pointed out that GenAI-centric dat-
acenters can introduce periodic, sustained, and structured power fluctuations at
the second level. This is because these next-generation datacenters are
equipped with mega-scale GPU clusters and advanced computing architec-
tures. They can, on a fast timescale, perform synchronized mini-batch process-
ing cycles, job-level scheduling, and repetitive compute-to-communication
phases [12]. If not managed, these resulting power fluctuations can act as ex-
ternal forcing signals to the grid, potentially triggering severe wide-area oscilla-
tions in future power systems with very high datacenter penetration.
Unfortunately, quantitative models and systematic grid-level analyses of these
fluctuations are largely absent from the literature. In particular, the frequency-
selective and persistent nature of these GenAI-induced power fluctuations, as a
forcing mechanism, is fundamentally different from ramp-induced transients,
calling for a new modeling and analysis framework for the second-level oscilla-
tions. To this end, a rigorous quantitative evaluation of these fluctuations is es-
sential to improve future datacenter-dominated grid operations and to power
the integration of large-scale AI workloads.
To address this critical gap, this paper puts forth a comprehensive modeling ap-
proach to characterize the power fluctuations of large-scale AI workloads. Our

goal is to enable an effective assessment of their potential to induce wide-area
oscillations as the deployment of next-generation datacenters increases. We
represent AI workloads with stochastic, periodic power consumption profiles, by
considering the compute- and communication-dominated phase division within
each cycle. Cycle durations can vary around a dominant time period, and
phase power levels include both baseline shifts and fine-scale random devia-
tions, with parameters tailored for training and fine-tuning workloads, respec-
tively. More importantly, we leverage the proposed models to perform a large-
scale, grid-level analysis to identify a few deciding factors that can collectively
shape the severity and variability of grid oscillations. By studying the oscillatory
potentials in GenAI-dominant datacenter workloads, our work highlights an ur-
gent need to enhance grid operations and stability amid the explosive growth in
AI-driven demand. The main contributions of this work are summarized as
follows:

• Establishing AI datacenter workloads as continuous, structured forcing 
sources beyond the existing ramping-centric models, to allow the
analysis of their potential to induce inter‑area and local oscillations.

 
• Developing a stochastic AI workload model that captures both periodic
patterns and fine-scale randomness, to produce realistic, time‑varying
load profiles for grid studies.

 
• Systematically assessing the grid oscillation effects induced by large-
scale AI workloads, revealing the aggregated resonance phenomena
in a realistic power system.

 
• Identifying critical deployment factors and operational conditions, rang-
ing from the system inertia, datacenter penetration level, fluctuation
frequency characteristics, size of datacenters, geographical disper-
sion, fluctuation suppression, to workload ratio, in order to inform fu-
ture grid planning strategies for AI-dominant grids.

 
The remainder of this paper is organized as follows. Section II discusses the
characteristics and composition of AI workloads in new-generation datacenters.
Section III proposes a stochastic modeling approach to capture the periodic,
variable power consumption patterns of AI workloads. Section IV details our
case studies on the WECC 179-bus and NPCC 140-bus systems to assess os-
cillatory intensity and damping variability under various conditions, and the pa-
per is wrapped up in Section V.

 
II Characteristics of AI Workloads
and Datacenter Electricity Demand
Large-scale and generative AI models, particularly LLMs, are rapidly emerging

as dominant contributors to datacenter electricity demand, significantly reshap-
 
ing both regional and interconnection-wide consumption patterns. Fig. 1 illus-
trates current and projected composition of datacenter electricity use and AI
workloads. Recent studies [13, 3, 8] report that datacenters accounted for ap-
proximately 4% of total US electricity demand in 2024, with this share expected

to approach nearly 10% by 2030. What is worse, certain North American re-
gions have witnessed a concentrated datacenter development with potentially
GW-level facilities, such as Texas, Virginia, and California. Consequently, the
local penetration of datacenters in these regions will far exceed the average.
Thus, there is an urgent need to improve the modeling of large-scale AI work-
load power profiles for grid-level studies.
Datacenter electricity consumption is primarily divided between non-computa-
tional infrastructure and server operations. Non-computational components,
such as cooling, networking, and storage, typically account for 40–50% of total
consumption [13]. The remainder is consumed by server-side computational
workloads. Conventional CPU-based server applications, such as web hosting,

search indexing, and transactional processing, impose relatively small and sta-
ble demands. In contrast, GPU-accelerated AI workloads incur substantially
higher power consumption due to the large-scale parallelism. Current estimates
indicate that AI workloads contribute roughly 10–20% of total datacenter elec-
tricity use [13, 14]. In AI-centric facilities, this fraction is expected to be consid-
erably higher, potentially reaching 50% in the future [15].

 
From an operational standpoint, AI workloads are generally categorized into
three stages: training, fine-tuning, and inference [1]. Training is the most com-
pute-intensive stage, during which model parameters are optimized offline us-
ing comprehensive datasets for a pre-designed architecture. These jobs typi-
cally run continuously for days or weeks, resulting in sustained demands at
peak loading. The fine-tuning stage follows training and adapts pre-trained
models to task-specific applications using smaller datasets. Although fine-tun-
ing has lower resource requirements and shorter compute time than training,
particularly for GenAI models, it is often performed more frequently. As a result,
it leads to lower but more sustained power consumption [16]. Finally, the infer-
ence stage deploys fine-tuned models to perform real-time prediction tasks.
Unlike the continuous, large-scale nature of training/fine-tuning, inference jobs
are typically intermittent and event-driven in response to user queries, and their
computational demands are much lower.

 

Figure 1:Example of a hierarchical AI workload composition.
Given the operational characteristics of AI workloads, the training and fine-tun-
ing stages together constitute the majority of power consumption in AI-centric
datacenters. Large-scale training tasks are typically executed as a single re-
source-intensive job distributed across hundreds or thousands of GPUs [17].
Recent forecasts project that the peak power consumption of a single frontier AI
training run could even reach 4-16 GW by 2030, a scale that would dominate
the total electricity consumption of the hosted AI-centric facilities [18]. The re-
mainder of active compute demand is primarily driven by smaller-scale training
and fine-tuning tasks, which collectively sustain a high baseline load throughout
operational cycles. This concentration is reinforced by an architectural split,
with centralized GPU clusters for training and fine-tuning, and inference han-
dled in lower-power zones or edge facilities [19, 20].

 
III Stochastic Power Profiling for AI Workloads
We develop a stochastic modeling framework to characterize the power con-
sumption of training-centric AI datacenters. As established in Section II, infer-
ence workloads are intermittent, small‑scale, and hosted on separate
low‑power infrastructure, limiting their impact on grid loading. Thus, the frame-
work focuses on training and fine‑tuning, which together constitute the domi-
nant and sustained component of demand. Both workloads are modeled within
a unified stochastic framework while accounting for their distinct operational
profiles. Although real measurement data for next-generation datacenters are
not yet publicly available, our modeling choices are informed by the latest re-

search on characterizing their electricity demand [12, 1, 21, 22, 23] and publicly
available HPC power consumption datasets [24, 25].
III-A Training Workload Modeling

 
(a) (b)
Figure 2:Example power consumption profiles for (a) training and (b) fine-tuning
stages.
AI training workloads in large-scale datacenters exhibit inherently periodic
power consumption patterns due to the repetitive nature of mini-batch process-
ing. Each iteration alternates between the compute-intensive, high-power up
phases and the low-power down phases, driven by communication and syn-
chronization needs. During the up phases, forward propagation, backward
propagation, and gradient computation place heavy demands due to the inher-
ent matrix/tensor operations and GPU kernel executions. In contrast, synchro-
nization operations, memory transfers, and communication overhead result in
lower power consumption during down phases [12, 26, 21]. Beyond this period-
icity, stochastic variations arise at two distinct time scales. Inter-iteration vari-
ability is driven by changes in cycle durations and phase power levels across it-
erations, resulting from GPU runtime jitter, operating-state changes, and kernel-
scheduling delays [27, 28]. Intra-iteration variability arises within each phase it-
self, as various computational and communication tasks are sequentially exe-

cuted, naturally inducing short-timescale deviations around the nominal power
level [17, 21].
To precisely characterize this behavior, we represent the power consumption
for training as a stochastic signal fluctuating around a dominant frequency, de-
noted by 𝑓 . Fig. 2(a) illustrates an example of such a stochastic power profile
0
with the associated time duration and power variables. To model the variability,
we express the time durations for the training cycle and the up/down phases
per iteration 𝑖 as
𝑇tr 1
𝑖 =
𝑓 (1+𝜉 ) (1)
0 𝑖
𝑇 up = 𝑟tr 𝑇tr,
𝑖 𝑖 𝑖 (2)
𝑇down = (1−𝑟tr) 𝑇tr
(3)
𝑖 𝑖 𝑖
where 𝑓 is the baseline fluctuation frequency that is perturbed by 𝜉 in iteration
0 𝑖

𝑖. Moreover, 𝑟tr represents the duration ratio for the up phase within iteration 𝑖.
 𝑖 
To capture bounded variability across workloads, we model the baseline fre-
quency to be uniformly distributed 𝑓 ∼ 𝒰 (𝑓 ,𝑓¯ ), which is fixed for each work-
0 ¯0 0
load depending on, e.g., model architecture and batch sizes, as reported in [12,
29]. Following these studies, for each iteration 𝑖, its duration randomly deviates
from the baseline assuming 𝜉 ∼ 𝒩 (0,𝜎2). The phase ratio 𝑟tr ∼ 𝒰 (𝑟tr,𝑟¯tr) is
𝑖 𝜉 𝑖 ¯
specified based on the empirically observed ranges reported in [22, 23].

 
In addition, the electricity demands of the two phases are defined as: 
𝑃 𝑖 up (𝑡) = 𝑃 ^tr (1+Δ up +𝜂up (𝑡)) (4)
𝑖
𝑃 𝑖 down (𝑡) = 𝑃 ^tr (1−Δ 𝑖 down +𝜂down (𝑡)) (5)
^tr
where 𝑃 denotes the nominal up-phase power consumption. Additionally, for it-
eration 𝑖, Δup and Δdown denote the baseline power deviations, while 𝜂up (𝑡) and
𝑖 𝑖
𝜂down (𝑡) the intra-phase stochastic deviations. Slow variations in baseline de-
mand, caused by GPU state changes and runtime effects, have been shown to
follow an approximately symmetric distribution around the mean, namely 𝑓 [12,
0
22]. Therefore, we assume a Gaussian distribution for Δup ∼ 𝒩 (0,𝜎2) and
𝑖 Δ
Δdown ∼ 𝒩 (𝜇 ,𝜎2), where 𝜇 is the nominal power difference between the two
𝑖 Δ Δ Δ
phases. There also exist fine-grained power variations at sub-milliseconds

within each phase, due to heterogeneous GPU kernels and communication op-
erations [12, 30]. Consequently, we represent them as Gaussian random pro-
cesses,  with  instantaneous  distributions  such  as  𝜂up(𝑡) ∼ 𝒩(0,𝜎2 )  and
𝜂,up
| 𝜂down(𝑡) | ∼ 𝒩(0,𝜎2 | ).  |     |     |     |
| -------- | -------- | --- | --- | --- | --- |
𝜂,down
We further discuss the parameter choices for these probability models, which
are summarized in Table I. For the nominal frequency, recent grid disturbance
monitoring reports have linked AI datacenter operations to oscillations near 1
Hz [12, 31, 11]. Thus, in our tests, we will set the baseline range to be [0.5, 1.5]
Hz. The coefficient of variation in GPU resource utilization reported in [27] moti-
vates 𝜎 = 0.1. GPU profiling studies indicate that compute-heavy phases typi-
𝜉
cally occupy 55% to 80% of each cycle, leading to 𝑟 = 0.55 and 𝑟¯ = 0.8 [32,
¯tr tr
21]. For power-related parameters, 𝜎 = 0.05 and 𝜇 = 0.3 reflect an average
|     |     |     | Δ   | Δ   |     |
| --- | --- | --- | --- | --- | --- |
30% reduction in demand during the synchronization phases [12]. Finally, the
intra-phase  variability  parameters  are  set  to  𝜎 ∈ [0.02,0.05]  and
𝜂,up
| 𝜎   | ∈ [0.01,0.03],  |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- |
𝜂,down under  the  assumption  that  the  compute-intensive  up
phase  exhibits  greater  short-timescale  variability  than  the  down  phase.

Although these parameter values are selected based on reported measure-
 
ments and profiling studies, the proposed modeling framework is not restricted
to these choices and can accommodate different parameter ranges to repre-
sent diverse AI workload characteristics.

 
Table I:Example of AI workload model parameters
|     |          | Training |           | Fine-tuning |          |
| --- | -------- | -------- | --------- | ----------- | -------- |
|     |          | 𝑓 ,𝑓¯    |           | 𝑓 ,𝑓¯       |          |
|     |          | ¯0 0     | 0.5, 1.5  | ¯1 1        | 0.3, 0.7 |
|     | Duration | 𝜎        | 0.1       | 𝜎           | 0.1      |
|     |          | 𝜉        |           | 𝜁           |          |
|     |          | 𝑟tr,𝑟¯tr |           | 𝑟ft,𝑟¯ft    |          |
|     |          |          | 0.55, 0.8 |             | 0.7, 0.9 |
|     |          | ¯        |           | ¯           |          |
|     |          | 𝜎        |           | 𝜎           |          |
|     |          |          | 0.05      |             | 0.03     |
|     |          | Δ        |           | 𝛿           |          |
|     |          | 𝜇        | 0.3       | 𝜇           | 0.8      |
Power
|     |        | Δ      |              | 𝛿      |               |
| --- | ------ | ------ | ------------ | ------ | ------------- |
|     | demand | 𝜎      | [0.02, 0.05] | 𝜎      | [0.01, 0.03]  |
|     |        | 𝜂,up   |              | 𝜂,tail |               |
|     |        | 𝜎      |              | 𝜎      |               |
|     |        | 𝜂,down | [0.01, 0.03] | 𝜂,idle | [0.005, 0.02] |

III-B Fine-tuning Workload Modeling
Fine-tuning workloads also exhibit phase-based periodic power consumption
patterns, but their characteristics differ from training workloads. The fine-tuning
process typically consists of initialization, early training, late training, and shut-
down phases [1]. Among these, only early and late training phases contribute
meaningfully to overall power consumption. In the early training stage, alternat-
ing high-power tail phases and low-power idle phases form a periodic profile
similar to training workloads. In contrast, the late training stage exhibits sus-
tained high power consumption with minimal fluctuations, due to reduced learn-
ing rates. Given the limited durations of the other phases and the reduced vari-
ability in the late training, this study focuses on modeling the early training
stage, which dominates the demand for fine-tuning workloads.

|    |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- |
The early training process can be represented with the same underlying struc-
ture as large-scale training, as shown in Fig. 2(b). The cycle structure of the 𝑖-th
iteration is defined as:
1
𝑇ft
|     |     |     | 𝑖 = | ,   |     |
| --- | --- | --- | --- | --- | --- |
(6)
|     |     |       | 𝑓  (1+𝜁  | )   |     |
| --- | --- | ----- | -------- | --- | --- |
|     |     |       | 1        | 𝑖   |     |
|     |     | 𝑇tail | 𝑟ft 𝑇ft, |     |     |
=
|     |     | 𝑖     | 𝑖           | 𝑖   | (7) |
| --- | --- | ----- | ----------- | --- | --- |
|     |     | 𝑇idle | (1−𝑟ft) 𝑇ft |     |     |
|     |     |       | =           |     | (8) |
|     |     | 𝑖     |             | 𝑖 𝑖 |     |
where 𝑓  is the baseline fluctuation frequency with an iteration-based deviation
1
of 𝜁, and 𝑟ft
 is the ratio of the tail phase. Similarly to modeling large-scale train-
𝑖 𝑖
,𝑓¯
ing, empirical studies suggest the frequency variables to follow 𝑓 ∼ 𝒰 (𝑓 )
1 ¯1 1
and 𝜁 ∼ 𝒩 (0,𝜎2). The phase ratio 𝑟ft ∼ 𝒰 (𝑟ft,𝑟¯ft) is also used to capture the vari-
| 𝑖   | 𝜁   |     | 𝑖   | ¯   |     |
| --- | --- | --- | --- | --- | --- |
ation in the compute-to-communication ratio. Power consumption during tail
and idle phases can be defined similarly as:
|     |     | 𝑃 tail (𝑡) | ^ ft        |              |      |
| --- | --- | ---------- | ----------- | ------------ | ---- |
|     |     | =          | 𝑃  (1+𝛿tail | +𝜂tail (𝑡))  |      |
|     |     | 𝑖          |             | 𝑖            | (9)  |
|     |     | 𝑃 idle (𝑡) | ^ ft        |              |      |
|     |     | =          | 𝑃  (1−𝛿idle | +𝜂idle (𝑡)). | (10) |
|     |     | 𝑖          |             | 𝑖            |      |
^ft
Here, 𝑃  is the nominal demand for the tail-phase with similar power deviation
terms as in (4)-(5). In addition, probabilistic modeling for the deviation terms
| also follows with 𝛿tail |     | 𝒩 (0,𝜎2) and 𝛿idle |     |                                           |     |
| ----------------------- | --- | ------------------ | --- | ----------------------------------------- | --- |
|                         |     | ∼                  |     | ∼ 𝒩 (𝜇 ,𝜎2) for slow variations. Fast in- |     |
|                         | 𝑖   | 𝛿                  | 𝑖   | 𝛿                                         |     |
𝛿
tra-phase  variations  are  modeled  by  Gaussian  random  processes  as

𝜂tail(𝑡) ∼ 𝒩(0,𝜎2 ) and 𝜂idle(𝑡) ∼ 𝒩(0,𝜎2 ). These components are attributed
𝜂,tail 𝜂,idle
to the same reasons as those studied for large-scale training.
The parameter choices for the fine-tuning workload model are also shown in
Table I. The dominant fluctuation frequency is set to 𝑓 ∼ 𝒰(0.3,0.7) based on
1
reported measurements of server-level behavior during fine-tuning workloads,
where shorter iteration cycles yield higher intrinsic frequencies, but multi-GPU
aggregation suppresses high-frequency components [12]. Inter-iteration dura-
tion variability is modeled as 𝜁 ∼ 𝒩(0,0.12), following the assumption that vari-
𝑖
ability magnitude is comparable to the training workloads. The compute phase
fraction is selected as 𝑟 = 0.7 and 𝑟¯ = 0.9, reflecting the consistently higher
¯ft ft
proportion of computation relative to communication due to the reduced num-
ber of GPUs [1]. The nominal tail-phase demand, 𝑃 , is chosen to be lower
ft,0
than the training nominal 𝑃 to account for smaller datasets and reduced
tr,0
batch sizes. Intra-phase fluctuations are specified as 𝜎 ∈ [0.01,0.03] and
𝜂,tail
𝜎 ∈ [0.005,0.02]. At the same time, iteration-level baseline shifts are set to
𝜂,idle
𝜎 = 0.03 and 𝜇 = 0.8 to reflect shorter and less frequent communication
𝛿 𝛿
phases with consistently low power consumption. Similar to training workloads,
these parameters can be adjusted to represent different workload configura-
tions and hardware settings.

 
III-C Aggregated AI Workloads for Datacenter Power Profiling
To perform power system dynamic studies, we need to model the total datacen-
ter load to explicitly capture stochastic power fluctuations from AI workloads.
Since non-server and non-AI loads have relatively stable power consumption
 
profiles [33], these components are represented as quasi-constant loads
throughout the interval of oscillation studies. Thus, this work attributes the time-
varying component of datacenter load solely to AI computational workloads, fo-
cusing on high-penetration scenarios in next-generation facilities without active
power-fluctuation management.

 

Figure 3:Example of AI workload modeling process.
As discussed in Section II, these datacenters are typically dominated by a sin-
gle large-scale training workload, supplemented by smaller-scale training and
fine-tuning workloads. Each workload is assumed to operate independently,
and the total datacenter load results from the superposition of these stochastic
power profiles. Hence, we express the total fluctuating load demand from the
datacenter by
𝑁tr 𝑁ft
𝑃AI (𝑡) = 𝑃tr (𝑡)+ ∑ 𝑃tr (𝑡)+ ∑ 𝑃ft (𝑡) (11)
0 𝑗 𝑘
𝑗=1 𝑘=1
where 𝑃tr (𝑡) denotes the power profile of the dominant and largest training
0
workload. In addition, 𝑃tr (𝑡) corresponds to the 𝑗-th, small-scale training work-
𝑗
load, with a total 𝑁tr of them; and similarly for 𝑃ft (𝑡) and 𝑁ft representing the
𝑘
fine-tuning workloads. Note that the subscript here stands for the workload in-
dex, which is different from the cycle iteration 𝑖 in (4)-(5). Each workload’s
power profile is represented by an iteration-based function of time per the
aforementioned periodic structure. For example, 𝑃tr (𝑡) can be expressed using
0
(1)-(5) as:

𝑃up (𝑡), 𝑡 ∈ [𝑡, 𝑡 +𝑇up) 
𝑃tr (𝑡) = { 𝑖 𝑖 𝑖 𝑖
0 𝑃down (𝑡), 𝑡 ∈ [𝑡 +𝑇up, 𝑡 +𝑇tr) (12)
𝑖 𝑖 𝑖 𝑖 𝑖
where 𝑡 is the start time of the 𝑖-th iteration. The other two types of workloads
𝑖
follow the same structure, yet at a much smaller nominal power level. Note that
transitions between different phases are assumed to occur instantaneously, as
they typically occur at a very fast timescale [5].
The relative power contribution of different types of workloads is determined by
^tr ^ft
their nominal electricity demands, namely 𝑃 and 𝑃 . Based on general AI data-
center resource allocation patterns and future trends [12, 34], we assume
^tr ^tr ^ft
𝑃 0 : (∑𝑃 𝑗 ) : (∑𝑃 𝑘 ) = 9 : 0.5 : 0.5 1 [1 This ratio has been chosen based on the reported growth of
LLM scale and also discussions with hyperscale datacenter developers. Latest reports [18] suggest large-scale
LLM training requires several hundred MWs of power, which will grow with the model size in future. Thus, it is ex-
pected emerging GW-level datacenter would allocate the majority of its capacity to large training workloads. Of
course, as rapid advancements continue in both LLM architectures and GPU hardware, such proportions may
evolve over time. To account for this variability, we further examine the sensitivity of our results to changes in this
assumed ratio in Section IV-D.] . These values have not been directly measured but rep-
resent an educated estimate based on the dominance trend of frontier-scale
training workloads, such as ChatGPT version updates. Actual values may vary
across datacenters, depending on their architectures and operational strate-
gies, and can be readily updated for future studies. Fig. 3 shows an example of
the aggregated AI workload power profile based on our models and assump-
tions. The large power fluctuation patterns at the second level can be clearly
observed, which serve as a forcing source for grid-level oscillation studies.

 

Remark 1 (Model stochasticity). The proposed model represents a substation-
level workload profile corresponding to an entire hyperscale datacenter. In typical
LLM training and fine-tuning, the majority GPUs operate in a largely synchronized
manner, implying that the aggregated load can be interpreted as a scaled-up ver-
sion of individual GPU workloads. However, random variability inevitably arises
across devices due to differences such as operating conditions and thermal
states, as captured by the stochastic elements embedded in our modeling frame-
work. Although the underlying power-electronic mechanisms within a datacenter
are not explicitly modeled, the resulting aggregate power profile remains suffi-
ciently representative for assessing system-level interactions with the grid.
Hence, we believe our stochastic modeling captures a broad range of workload
behaviors, both within a single facility and across heterogeneous datacenters.
Remark 2 (Model validation). A direct comparison between our model results in
Fig. 3 and proprietary real-world measurements is inherently challenging due to
lack of data access. Nevertheless, the generated profiles exhibit strong qualitative
consistency with publicly available traces reported in the Google Cloud blog [10],
as well as with realistic GPU power measurements in [1, 22]. In addition, the tem-
poral features are well aligned with the rack-level power measurements pre-
sented in [35]. While dominant fluctuation frequencies differ, they depend on
GPU specifications and LLM size which can be adjusted by the parameters in our
model. Furthermore, our modeling results have been independently reviewed by
researchers from AWS and Meta, who confirmed that the observed behaviors are
highly consistent with their practical experience in characterizing real-world data-
center workloads. Collectively, the validity and practical relevance of the proposed
modeling framework are well supported.

IV Case Studies
Table II:Baseline Simulation Settings
| Simulation Parameters |     | WECC    | NPCC    |
| --------------------- | --- | ------- | ------- |
| Base load             |     | 60.8 GW | 27.7 GW |
| System inertia (𝐻     | )   | 2.7     | 0.60    |
sys
| Datacenter penetration         |     | 11.5 % | 10.8 % |
| ------------------------------ | --- | ------ | ------ |
| Number of datacenters          |     | 7      | 3      |
| Individual datacenter size     |     | 1 GW   |        |
| Fluctuation frequency range (𝑓 | -𝑓¯ |        |        |
0 ) 0.5–1.5 Hz
¯0
tr
| ^  ratio, 𝑁tr , 𝑁ft |     |             |     |
| ------------------- | --- | ----------- | --- |
| {𝑃                  | }   | {90%, 2, 2} |     |
0
tr
^
𝑃0 ratio represents the ratio between nominal demands of large training workload and total AI
workload.
IV-A Simulation Settings
To investigate the impact of AI workloads on power system oscillations, we con-
duct case studies using the WECC 179-bus system and the NPCC 140-bus
system. Both systems are constructed based on the ANDES configuration [36]
with base loads of 60.8 GW and 27.7 GW, respectively. As represented in Table
II, datacenters are implemented with the penetration level of around 10% in the
baseline case. Each datacenter is assumed to have a nominal capacity of 1
GW, consistent with recent forecasts that a single AI facility could reach this
scale [37]. Of this capacity, 80% is modeled as a steady-state component that
replaces an equivalent portion of the original aggregated load on the host bus.
The remaining 20% represents the fluctuating AI workload component and is
superimposed on the replaced steady-state demand. Accordingly, the datacen-
ter load is represented as a conventional PQ load whose active power varies
over time according to the proposed model outputs. The load varies at the sim-
ulation timestep of 0.01 s, and the model parameters follow the example values
listed in Table I. This modeling approach preserves the total steady-state load
of the original case, ensuring that the base-case power flow solution and the
initial  operating  point  for  time-domain  simulations  remain  unchanged.  The

WECC system tests show how system-level and datacenter-level factors gov-
ern oscillatory behaviors, while the NPCC system tests verify the persistence of
these oscillations and assess mitigation effectiveness in different
configurations.

 
Figure 4:Topology of the modified WECC 179-bus system with datacenters.

Figure 5:Eigen-analysis results of the WECC 179-bus system under different
system inertia levels.
When implementing datacenters, we consider the locations of unstable modes
2
identified through eigen-analysis [2 The eigenvalue analysis is performed by linearizing the differ-
ential-algebraic equations of the system around the initial operating point. It relies on the initial system configura-
tion, while the Prony analysis results are derived from the measurements obtained from the dynamic simulation.
In Fig. 5, a positive real eigenvalue indicates the unstable mode.] using the ANDES tool. In the
WECC system, unstable modes at 0.852 Hz, 1.06 Hz, and 1.44 Hz are identi-
fied. The locations of these modes are illustrated in Fig. 4 with the eigen-analy-
sis results in Fig. 5. Accordingly, in the baseline scenario, all datacenters are
placed within zone 1-A, which avoids buses with strong participation in these
unstable modes, and are randomly assigned within this zone. A distributed de-
ployment scenario is also considered, where datacenters are located on the
buses marked by red triangles in Fig. 4. In the NPCC system, unstable modes
exist mostly below 0.5 Hz, which will be further discussed in Section IV-D.
Therefore, only the distributed configuration is examined for this system.

 

Table III:Scenarios for Comparison in the WECC 179-bus System
Factors Scenario & Parameters
System-level factors
|     | Baseline (𝐻 = 2.7) |     |
| --- | ------------------ | --- |
sys
System inertia
Reduced SGs’ inertia constant (𝐻 = 1.36)
#1 sys
& intrinsic mode
|     | Replaced SGs by RES (𝐻 | = 0.79) |
| --- | ---------------------- | ------- |
sys
Baseline (11.5%)
Datacenter
| #2  | High penetration level (23%) |     |
| --- | ---------------------------- | --- |
penetration
Extra-high penetration level (34.5%)
Datacenter-level factors
|            | Baseline (1 GW×7 = |       |
| ---------- | ------------------ | ----- |
| Datacenter |                    | 7 GW) |
#3
| sizing & number | Larger size (2.3 GW×3 | = 7 GW) |
| --------------- | --------------------- | ------- |
Baseline (0.5–1.5 Hz)
Fluctuation
| #4  | Narrower frequency range (0.95–1.05 Hz) |     |
| --- | --------------------------------------- | --- |
frequency
Wider frequency range (0.1–2 Hz)
| Geographical | Centralized (circle in Fig. 4) |     |
| ------------ | ------------------------------ | --- |
#5
| location | Distributed (triangle in Fig. 4) |     |
| -------- | -------------------------------- | --- |
Table IV:Scenarios for Comparison in the NPCC 140-bus System
Factors Scenario & Parameters
Without mitigation
Mitigation
| #6  | Fluctuation suppression (50–90%) |     |
| --- | -------------------------------- | --- |
strategy
Improved system damping (20–80%)
| ^tr                     | Baseline ({90%, 2, 2}) |     |
| ----------------------- | ---------------------- | --- |
| #7 {𝑃  ratio, 𝑁tr , 𝑁ft |                        |     |
}
| 0   | Reduced ({60–80%, 4–8, 4–8}) |     |
| --- | ---------------------------- | --- |
Simulation  scenarios  are  designed  to  examine  how  AI-induced  oscillations
evolve under various factors. In WECC system, system-wide factors, such as
system inertia and datacenter penetration level, are evaluated. As the datacen-
ter-level factors, individual datacenter load sizes, load fluctuation frequency,
and datacenter geographical placement are compromised. The corresponding
scenarios and parameter settings are summarized in Table III. In the NPCC
system, we focus on oscillation-mitigation approaches and workload composi-

tion. Specifically, two mitigation approaches are examined, including enhanced
systematic damping and fluctuation magnitude suppression, as shown in Table
IV. Detailed explanations of each scenario are provided in corresponding sub-
sections. All time-domain simulations are performed using the ANDES tool [36].
Resulting frequency trajectories are analyzed using FFT, Prony analysis, and
pseudo energy. By representing the measurement signals as a linear combina-
tion of modal components, Prony analysis enables accurate identification of
small-signal eigenvalues. As discussed in [38], it generally has a higher recon-
struction ability than matrix pencil and eigen-system realization algorithms. The
pseudo energy, detailed in [39], serves as an effective metric for characterizing
the visibility and impact of specific oscillation modes within the system
response.
IV-B WECC 179-bus System: Impact of System-level Factors
To assess the impact of datacenter operations on oscillation behavior, we ana-
lyze the effects of two key system-level factors: system inertia and datacenter
penetration level. The baseline system exhibits a system inertia value of 2.7,
and two lower inertial grids are further simulated. The first case proportionally
reduces the inertia constants 𝐻 of all synchronous generators (SGs) by 50%, 
 
yielding a system inertia 𝐻 of 1.36 [40]. The other case replaces 7 SGs by re-
sys
newable energy sources (RES), resulting in a system inertia of 0.79. The re-
placed generators are marked in orange in Fig. 4, and the RES is modeled us-
ing the WECC renewable plant model [41]. As for the datacenter penetration
level, we consider a baseline scenario of seven datacenters collectively con-
suming approximately 7 GW of demand, accounting for 11.5% of the total sys-
tem load at 60.8 GW. We further define two higher-penetration scenarios by
uniformly increasing the size of each datacenter, keeping the number/location
fixed. In the high penetration scenario, each datacenter is doubled in size, re-
sulting in a total penetration level of 23%. In the extra-high penetration sce-
nario, datacenter sizes are tripled, corresponding to a penetration level of
34.5%.

 

(a)
(b)
(c)
Figure 6:Frequency trajectory and Prony analysis results according to the system
inertia: (a) baseline, (b) reduced generator inertia, and (c) RES replacement
cases.
Factor #1. System inertia & intrinsic mode: Simulation results under different
inertia conditions are represented in Fig. 6. The left figures show the generator
bus frequencies for each case. The black trace marks the bus with the largest
peak-to-peak oscillation. Even in the baseline scenario, sustained oscillation is
observed, exhibiting oscillation magnitudes up to approximately 0.2 Hz peak-to-
peak. With lower generator inertia in Fig. 6(b), oscillatory behavior intensifies
across all generator buses, reaching larger than 0.4 Hz peak-to-peak magni-
tude. Notably, under the baseline scenario, generator bus frequencies reflect
the characteristic shape of the datacenter electricity demand, particularly its

higher-frequency components. In contrast, under lower inertia conditions, these
features largely disappear from the frequency response. This indicates that as
inertia decreases, stronger interactions between datacenter load fluctuations
and the power system lead to resonance-like oscillations that dominate system
behavior. Surprisingly, although the RES replacement case shows the lowest
inertial level, the oscillation magnitudes in Fig. 6(c) are smaller than those of
the baseline case. This behavior is explained by the eigen-analysis in Fig. 5,
which shows that the RES case lacks an unstable mode around 1 Hz. In con-
trast, the other cases contain a 1.06 Hz unstable mode associated with Bus
116, located close to the datacenters, enabling resonance with the dominant 1
Hz fluctuation in datacenter demand. The absence of this resonance in the
RES case leads to significantly reduced oscillation magnitudes. These results
indicate that unstable-mode excitation primarily governs oscillation severity,
while lower inertia further aggravates this effect when resonance conditions
exist.
Further insights are obtained from Prony analysis results, as shown in the right
figures of Fig. 6. The axes represent the modal frequency and damping ratio of
oscillatory modes identified from generator bus frequency signals, with the size
of each circle indicating its magnitude. In the baseline scenario, oscillation
modes are concentrated in the 0.5–1.3 Hz range, with a prominent mode near
1.1 Hz exhibiting the largest amplitude. In the reduced generator inertia case,
we can confirm that the oscillation magnitudes are larger than in the baseline

case, with similar frequency and damping ratio. This is because the original
 
1.06 Hz mode, as well as the other unstable modes, shift slightly to the right
and become more unstable in the reduced generator inertia case, as shown in
Fig. 5. Additionally, a new unstable mode emerges at approximately 0.757 Hz,
further degrading system stability. Another notable observation from the eigen-
value analysis is the emergence of numerous unstable modes below 0.5 Hz in
the lower inertia case. While these modes exhibit higher damping ratios, they
still contribute to overall oscillation amplification, reflected in the enlarged oscil-
lation magnitudes in the Prony analysis results. Finally, the Prony analysis re-
sults of the RES case shows reduced modal magnitudes above 0.7 Hz com-
pared to the baseline, consistent with the absence of the unstable mode near 1
Hz. In contrast, modal magnitudes below 0.5 Hz remain comparable to, or even
larger than, those of the baseline, reflecting the presence of unstable modes in
this low-frequency range. These findings collectively demonstrate that prevent-
ing external forcing components that coincide with the system’s unstable
modes must be a primary consideration for mitigating severe oscillations. In ad-

dition, maintaining an adequate system inertia level also plays a key role in
keeping oscillation magnitudes within acceptable limits.
Figure 7:PSD analysis and coherence of the datacenter demand and system
frequency trajectory.

 

(a)
(b) (c) (d)
Figure 8:Simulation results according to the datacenter penetration level: (a)
electric frequency trajectories, (b) FFT results, (c) Prony analysis results, and (d)
pseudo energy.
We further perform the power spectral density (PSD) analysis on the datacenter
demand and the system frequency trajectory for the baseline case in Fig. 6(a)
to distinguish the effects of modal instability and forcing input. As illustrated in
Fig. 7, the PSD of the datacenter demand exhibits a dominant peak near 1 Hz
with smaller harmonic components, consistent with the FFT results in Fig. 3.
The PSD of the frequency trajectory also shows its largest value around 1 Hz
but differs significantly in other frequency ranges. Compared to the datacenter
demand, the frequency trajectory shows significantly larger PSD at low frequen-
cies and lower PSD at high frequencies. The elevated PSD value below 1 Hz
suggests that weak forcing components are strongly amplified by unstable
modes, which is further supported by the low coherence in this region.
Meanwhile, the coherence around 1 Hz exceeds 0.6, indicating strong similarity
between the forcing signal and the frequency response. This confirms that the 1
Hz oscillation is primarily driven by the datacenter demand and further rein-
forced by unstable system modes. Above 1 Hz, the low frequency PSD sug-
gests the absence of unstable modes in that region.

 
Factor #2. Datacenter penetration: Simulation results under varying datacen-
ter penetration levels are presented in Fig. 8, where all cases are evaluated un-

der the lower inertia level. As shown in Fig. 8(a), higher penetration consistently
amplifies oscillation magnitudes across the system. In particular, under the ex-
tra-high penetration, the maximum peak-to-peak oscillation magnitude reaches
approximately 0.5 Hz. Among various contributing factors, datacenter penetra-
tion level emerges as the primary driver of growth in oscillation magnitude.
Unlike the system inertia reduction, higher penetration mainly scales the oscilla-
tion amplitude without significantly altering the waveform shape. This distinction
is evident in both the FFT results in Fig. 8(b) and the Prony analysis results in
Fig. 8(c), obtained from the generator bus exhibiting the most significant oscilla-
tion. The dominant oscillation frequency remains approximately 1.2 Hz, and the
damping ratio is largely unaffected by penetration level. In contrast, both the
FFT amplitude and modal magnitude increase proportionally with penetration
level. These trends are further confirmed by the normalized pseudo-energy re-
sults, which quantify the mode’s observability in the measurement signal.
Results indicate that higher datacenter penetration directly enhances the
pseudo energy of the critical mode, reinforcing its dominant influence on overall
system oscillatory behavior.

 

(a)
(b)
Figure 9:Inter-area oscillation between GENROU 9, 12 and GENROU 10, 11: (a)
frequency deviation and (b) mode shape phase angles.
Another notable characteristic of datacenter-induced oscillations is that, al-
though the system modes near 1.2 Hz are generally classified as local modes,
an inter-area oscillation pattern is observed. As shown in Fig. 9(a), generators
GENROU 9 and GENROU 12 exhibit nearly identical phase responses, while
GENROU 10 and GENROU 11 oscillate in anti-phase relative to GENROU 9
and 12. To quantify this behavior, mode shape analysis was performed using
Prony analysis applied to the generator frequency deviation signals, focusing
on the mode near 1.2 Hz. The phase angles of the resulting mode shape, pre-
sented in Fig. 9(b), show that GENROU 9 and GENROU 12 swing at approxi-
mately +𝜋 radians, whereas GENROU 10 and GENROU 11 swing at approxi-
mately −𝜋 radians. This intense phase separation is a clear indicator of oscilla-
tory separation, consistent with inter-area oscillation behavior. It is further noted
that, as depicted in Fig. 4(a), GENROU 9 and GENROU 12 are geographically
clustered, as are GENROU 10 and GENROU 11, but the two groups are lo-
cated in distinct network zones. While the frequency response alone does not

fully reveal the separation typically associated with classical inter-area modes,
the phase-based mode shape analysis confirms the emergence of a zonal in-
ter-area oscillation between these generator groups.
IV-C WECC 179-bus System:
Impact of Datacenter-Level Factors
We further investigate the impact of key datacenter-level factors on power sys-
tem oscillations, including datacenter sizing, load fluctuation frequency, and the
geographical distribution of datacenters. First, regarding individual datacenter
size, the baseline scenario comprises seven datacenters, each rated at 1 GW,
collectively consuming a total demand of 7 GW. In contrast, the higher datacen-
ter-size case reconfigures this demand across three larger datacenters, each
approximately 3.3 GW, maintaining the same total demand of 7 GW. Second,
the frequency of load fluctuation is diversified by adjusting the range of 𝑓 for
0
the dominant training workload. While the baseline case uses a range of 0.5–
1.5 Hz, two alternative cases are considered: a narrower range of 0.95–1.05 Hz
and a wider range of 0.1–2 Hz. Finally, for the geographical location, we com-

pare a geographically distributed datacenter configuration, as illustrated in Fig.
4, against the baseline scenario in which datacenters are concentrated near
each other.

 

(a)
(b)
Figure 10:Simulation results according to the individual datacenter size: (a)
frequency trajectories and (b) Prony analysis results.
Factor #3. Datacenter sizing: The experimental results for the datacenter siz-
ing factor are presented in Fig. 10. Despite the identical total datacenter load-
ing, deploying larger datacenters has resulted in significantly amplified oscilla-
tions, as shown in Fig. 10(a). This amplification effect is particularly evident at
buses that do not experience the maximum oscillation in the baseline case.
Another important observation is the qualitative change in frequency signals at
the bus with the maximum oscillations. While the baseline scenario exhibits
conventional oscillatory waveforms, larger datacenter sizing shows more com-
ponents with frequencies above 1 Hz. This phenomenon indicates that larger
individual datacenters exert a stronger influence on the grid, allowing the peri-
odic fluctuations inherent in the datacenter output to manifest more prominently
in the system frequency. The Prony analysis results further confirm this behav-
ior in Fig. 10(b), which reveals an amplification of modes above 2 Hz in the
larger datacenter size scenario. However, around the dominant oscillation fre-
quency region near 1 Hz, differences between the baseline and the larger siz-
ing scenario are less pronounced, apart from a moderate increase in mode am-
plitudes across multiple buses. Although the dominant oscillation shifted from

approximately 1.2 Hz in the baseline to 0.8–1 Hz in the larger-size case, this
variation is primarily due to stochastic differences in the generated signals.

 

(a)
(b)
(c)
(d) (e)
Figure 11:Impact of datacenter fluctuation frequency range on system
oscillations: frequency trajectories and Prony analysis results under (a) baseline,
(b) narrower, and (c) wider ranges. (d) FFT results and (e) pseudo energy.

Factor #4. Frequency of load fluctuations: The simulation results under
three different fluctuation frequency ranges are presented in Fig. 11. Based on
the peak-to-peak oscillation magnitude, it is observed that oscillations intensify
as the frequency range becomes narrower. This trend can be attributed to the
concentration of fluctuations around the 1–1.2 Hz region in the narrower range
case, which interacts more strongly with the mode of Bus 116, thereby amplify-
ing the oscillatory response. The Prony analysis results further support this ob-
servation. As the frequency range shifts from narrower to baseline, then to
wider, the identified modes progressively spread over a broader frequency
band, with the mode magnitudes being largest in the narrower-range case.
These findings are consistent with the FFT results shown in Fig. 11(d), where
the narrower range scenario exhibits the highest spectral amplitude near the
dominant oscillation frequency. Meanwhile, the wider-range scenario shows a
notable distinction from the other cases. Specifically, an additional oscillation
component near 0.2 Hz is observed, which is visually apparent in Fig. 11(c).
Although this oscillation does not appear as a dominant mode in the Prony
analysis results or the FFT spectra, it emerges clearly in the pseudo energy dis-
tribution shown in Fig. 11(e), where it contributes the highest energy content
among all frequency bands. This result is partly due to the inherent nature of
the pseudo-energy, in which lower-frequency components tend to accumulate
larger energy values even when their amplitudes are relatively small. From a
power system stability perspective, such wide-area oscillations can be critical.
Although their magnitude may appear modest, their prolonged presence can
lead to sustained system stress and potential control challenges, making them
problematic despite their lower frequency-domain prominence.

 
Factor #5. Geographical distribution: As the final factor, we conduct a case
study examining the potential impact of datacenters’ geographical distribution.
We initially expected that concentrating datacenters in a single area could am-
plify oscillations due to the aggregated effects of power fluctuations.
Surprisingly, as shown in Fig. 12, the results revealed the opposite trend. Both
the frequency trajectories and the Prony analysis results indicate that, for the
geographically distributed datacenter case, oscillations in the 1.2 Hz region be-
come more pronounced than in the concentrated baseline case. An additional
noteworthy observation is that the distributed configuration amplifies not only
the oscillations around 1.2 Hz but also the oscillations near 0.5 Hz and 0.8 Hz.
This can be attributed to interactions between distributed datacenters and mul-
tiple local modes within the system. As illustrated in Fig. 4(b), the spatially dis-
tributed datacenters can interact with the 0.852 Hz mode associated with Bus

4, in addition to the dominant 1.2 Hz mode, likely leading to increased oscilla-
tory responses in both regions. Furthermore, the appearance of a signal com-
ponent around 0.5 Hz in the Prony analysis can be interpreted as the result of
the nonlinear interaction between the two excited modes, generating a differ-
ence-frequency oscillation. These findings highlight the complex, aggregated
role of datacenter location in shaping multi-mode interactions and amplifying
oscillatory levels across multiple frequency bands.
(a)

 
(b)
Figure 12:Simulation results according to the geographical location of
datacenters: (a) frequency trajectories and (b) Prony analysis results.

(a) (b) (c)
Figure 13:Stochastic variation of frequency trajectories and FFT results for the
maximum oscillation bus under (a) baseline, (b) narrower, and (c) wider
fluctuation frequency ranges considering different geographical locations.
To further investigate the potential for diverse mode excitation under geographi-
cally distributed datacenter deployments, comparative analyses are conducted
across different fluctuation frequency ranges under both concentrated and dis-
tributed configurations. Recognizing that stochasticity can result in varying os-
cillatory outcomes, multiple simulations are performed for each case, and the
frequency trajectory and FFT spectrum of the bus exhibiting maximum oscilla-
tion amplitude are compared, as illustrated in Fig. 13. In the geographically
concentrated scenario, consistent with previous discussions, a narrower fluctu-
ation frequency range yields larger oscillation magnitudes, whereas a wider
range yields smaller, more dispersed oscillatory responses. In contrast, the dis-
tributed deployment scenario exhibits more diverse FFT patterns due to greater
stochasticity. Notably, in the narrower-range case, the 0.85 Hz unstable mode
remains unexcited. In contrast, in the baseline-range case, interaction with this
mode results in larger oscillation magnitudes than in the narrower-range case.
In the wider-range scenario, the distributed case exhibits the highest variability
across simulation runs, yet consistently shows oscillations in the 0.1–0.3 Hz
range, highlighting the sustained presence of low-frequency components under
distributed deployments.

 

Figure 14:Example of simulation failure by the low voltage issue.
Based on our studies, geographical location is an important decisive factor that
affects oscillation behavior. Concentrated datacenter deployments tend to limit
the excitation of unstable modes, as their aggregated fluctuations are spatially
isolated from critical mode locations. In contrast, distributed deployments in-
crease the likelihood of multiple-mode excitations and broader spectral interac-
tions, particularly under wider fluctuation frequency ranges. Additionally, distrib-
uted deployments exhibit stronger stochastic effects, leading to greater variabil-
ity in oscillation severity and more diverse mode excitation patterns across sim-
ulation runs. These spatial coupling and stochastic amplification effects high-
light that distributed siting not only exacerbates oscillatory risks but also intro-
duces greater uncertainty in system response. Although concentrated deploy-
ments may mitigate oscillatory instability, they raise concerns about voltage sta-
bility, as shown in Fig. 14. The observed simulation termination arises from a
low-voltage condition that violates the convergence requirements of the
ANDES. Once the voltage on Bus 73 falls to 0.837 p.u., the solver encounters
an ill-conditioned Jacobian and cannot proceed, resulting in an automatic simu-
lation shutdown. In conclusion, determining the grid-friendly location for AI data-
centers requires a holistic approach that considers both their oscillation impact
and voltage stability.

 
IV-D Simulation Results on the NPCC 140-Bus System
To verify the generality of the observed forced oscillations, the baseline sce-
nario is tested on the NPCC 140-bus system, which represents a portion of the
eastern interconnection. As shown in Fig. 15, the dominant oscillation fre-

quency remains near 1 Hz, as also confirmed by the Prony analysis. When
comparing the Prony and matrix pencil methods, their extracted frequencies
and damping ratios closely match, validating the reliability of the Prony method.
The eigen-analysis results in Fig. 16 reveal that, unlike the WECC system, the
NPCC system contains several unstable modes below 0.25 Hz and none above
0.5 Hz. Consequently, compared to the WECC scenario, the NPCC system ex-
hibits significantly smaller oscillation magnitudes, with the largest peak-to-peak
value around 0.1 Hz. These results further demonstrate that forced-oscillation
severity is primarily governed by the frequency overlap between the forcing sig-
nal and unstable system modes.

 
(a) (b)
(c) (d)
Figure 15:Simulation results according to the fluctuation suppression: (a) demand
profiles, (b) Prony and matrix pencil analysis results of the baseline case, and
FFT results of (c) demand profiles and (d) frequency trajectories.

Figure 16:Eigen-analysis results of the NPCC 140-bus system.
(a) (b)
Figure 17:Comparison of the maximum peak-to-peak oscillation magnitude and
relative pseudo energy according to (a) fluctuation suppression and (b) effective
damping.
Factor #6. Mitigation strategy: We examine the impact of mitigation ap-
proaches to reduce datacenter-induced fluctuations, focusing on two represen-
tative strategies: i) smoothing the workload-induced power variations and ii) in-
creasing the system’s effective damping. For the former, we assume that the AI
workload’s maximum fluctuation amplitude is reduced by 50% to 90%. The ex-
ample of suppressed demand profiles is illustrated in Fig. 15(a) and their FFT

results in Fig. 15(c). The suppressed datacenter fluctuation exhibits substan-
tially smaller FFT magnitudes in the 1-Hz band, which naturally reduces the
magnitude of the resulting oscillations, as represented in Fig. 15(d). Moreover,
this reduction does not vary linearly with the suppression level. Instead, once
exceeding a certain threshold, the effectiveness of mitigation increases
marginally. This nonlinear trend is consistently reflected in the maximum peak-
to-peak oscillation magnitudes and pseudo-energy values in Fig. 17(a).
Meanwhile, Fig. 15(d) shows relatively higher energy content below approxi-
mately 0.5 Hz compared than in the demand spectrum. This can be attributed
to the unstable low-frequency modes observed in Fig. 16.
To examine the influence of effective damping, we increase the SG damping
parameters from 20% to 80% and evaluate the resulting system response. As
illustrated in Fig. 17(b), the oscillation magnitude decreases as the damping in-
creases; however, its mitigation effect is considerably weaker than that

achieved through fluctuation suppression. This is mainly because the added
 
damping is distributed among geographically dispersed generators, limiting its
localized influence. Although co-locating damping resources near datacenters
could enhance effectiveness, the results clearly demonstrate that directly atten-
uating the forcing signal is a more efficient and robust strategy for oscillation
mitigation.

 

(a) (b)
(c) (d)
Figure 18:Simulation results according to the workload ratio: FFT results of (a)
workload and (b) frequency trajectories. (c) Prony analysis results and (d) pseudo
energy.
Factor #7. Workload ratio: We analyze the impact of large training workload
^tr
ratio, 𝑃 , on oscillatory behavior. This ratio is reduced from the baseline 90% to
0
60%, with the remaining portion reallocated to small training and fine-tuning
workloads. For every 10% reduction in 𝑃
^tr
, the numbers of these workloads, 𝑁tr
0
and 𝑁ft , are each increased by 2. As shown in Fig. 18(a), decreasing 𝑃
^tr
re-
0
duces the magnitude around the 1-Hz band, while amplifying components near
0.5 Hz and 1.8 Hz. The amplification around 1.8 Hz can be attributed to the su-
perposition of multiple smaller workloads, which collectively introduce high-fre-
quency components. Frequency trajectory, Prony, and pseudo-energy analyses
consistently confirm that the dominant oscillation shifts from the 1-Hz band to-
ward higher-frequency regions as the large-workload proportion decreases. At
lower ratios, the 1.8-Hz component exceeds the 1-Hz component in both modal
magnitude and energy, indicating constructive accumulation of fine-grained
workload variations rather than mutual cancellation.

 

To further evaluate the impact of stochastic variability in the proposed datacen-
ter model, we run 20 simulations under both normal and narrow workload fre-
quency ranges, as shown in Fig. 19. Despite the inherent randomness in indi-
vidual workload realizations, the resulting system response consistently exhibits
a dominant oscillation around 1 Hz, accompanied by smaller oscillatory compo-
nents near 0.5 Hz and 2 Hz. This persistent pattern indicates that stochastic
variations in AI workloads do not diminish the system’s susceptibility to data-
center-induced oscillation. The effect becomes even more pronounced in the
narrower frequency range case in Fig. 19(b), where more coherent forcing
leads to stronger and more repeatable oscillatory responses. Notably, these re-
sults account not only for randomness within each workload profile but also for
inter-workload and inter-datacenter timing differences. The consistent oscilla-
tion patterns across all trials suggest that the oscillation risk driven by large-
scale AI workloads remains systematically significant even under substantial
stochasticity.

 
(a) (b)
Figure 19:Prony analysis results for multiple simulations with (a) normal and (b)
narrow frequency ranges.
IV-E Oscillation Implications of AI Datacenter Deployment
Our case studies demonstrate that AI datacenters can act as persistent and in-
tense sources of forced oscillations in power systems when their power fluctua-
tions are not adequately suppressed. Although total datacenter penetration lev-
els are set based on the projection of future deployments, the proportion of AI

workloads within these datacenters has been conservatively underestimated. In
practical systems, where AI-driven workloads may account for a higher share,
the associated risk of oscillation could be significantly higher.
Similar to conventional electromechanical oscillations, the severity of datacen-
ter-induced oscillations is governed by several key system and load character-
istics. Lower system inertia, higher datacenter penetration, and larger individual

datacenter sizes intensify oscillation severity. Most critically, the impact of these
 
oscillations is dictated by the degree of frequency alignment between datacen-
ter load fluctuations and the system’s unstable modes. When the forcing signal
resonates with an existing unstable mode, the oscillation magnitudes are dra-
matically amplified, posing serious risks to system reliability. Geographical sit-
ing, fluctuation frequency range, and workload composition influence this align-
ment either directly or indirectly. From a mitigation perspective, increasing sys-
tem inertia or damping can alleviate oscillations by limiting their amplitudes
once excited. However, our study shows that suppressing load fluctuations at
their source is a more effective and robust strategy for preventing forced
oscillations.

 
V Conclusion
This paper has presented a stochastic power profiling framework that explicitly
captures the periodic and high-magnitude fluctuations introduced by large-scale
AI workloads in next-generation datacenters. By incorporating workload-specific
characteristics, the proposed method models AI-centric datacenters as continu-
ous, frequency-selective forcing sources distinct from conventional ramping
loads. Using the WECC 179-bus system and NPCC 140-bus system, we have
systematically evaluated forced oscillations induced by datacenters under vari-
ous factors. Our results show that severe oscillations can emerge when data-
center-induced fluctuations excite intrinsic unstable modes of the grid. The
severity of these oscillations is strongly influenced by the fluctuation’s fre-
quency content and geographical location, as well as by broader system factors
such as workload composition and datacenter deployment configuration. Direct
suppression of the datacenter load fluctuation is demonstrated to be substan-
tially more effective than indirect system-level measures, highlighting the impor-
tance of understanding the characteristics of workload-driven variability when
assessing oscillatory risk. These findings emphasize the need to incorporate

workload-based electricity demand modeling and forced-oscillation risk assess-
ments into future grid planning and operational studies, particularly as AI-cen-
tric datacenters grow in scale and prevalence. Exciting future research direc-
tions open up including the mitigation of power fluctuations at both datacenter-
and grid-levels, as well as the extension to modeling a wider time-scale range
in the variability of datacenter power consumption.
References
[1] Y. Li, M. Mughees, Y. Chen, and Y. R. Li (2024)
The unseen AI disruptions for power grids: LLM-induced transients.
arXiv preprint arXiv:2409.11416.
Cited by: §I, §I, §II, §III-B, §III-B, §III, Remark 2.
[2] R. Quint et al. (2025)
Practical guidance and considerations for large load interconnections.
Technical report
Elevate Energy Consulting.
Cited by: §I, §I.
[3] A. Shehabi et al. (2024)
2024 United States data center energy usage report. 
 
Technical report
Lawrence Berkeley National Laboratory, Berkeley, CA.
Cited by: §I, §II.
[4] J. Aljbour, T. Wilson, and P. Patel (2024)
Powering intelligence: analyzing artificial intelligence and data center
energy consumption.
Technical report
EPRI White Paper no. 3002028905.
Cited by: §I.
[5] Y. Li and Y. Li (2025)
AI load dynamics–a power electronics perspective.
arXiv preprint arXiv:2502.01647.
Cited by: §I, §III-C.
[6] A. Jimenez-Ruiz and F. Milano (2025)
Data center model for transient stability analysis of power systems.

arXiv preprint arXiv:2505.16575.
Cited by: §I.
[7] R. O’Keefe (2025)
Event records showing data center response to faults.
External Links: Link (https://www.nerc.com/comm/RSTC/LLTF/LLTF_April_Me
eting_&_Technical_Workshop_Presentations_.pdf)
Cited by: §I.
[8] M. Parker and B. Sterling (2025)
Unplanned data center load transfer update.
External Links: Link (https://www.nerc.com/comm/RSTC/LLTF/LLTF_June_Wo
rkshop_Presentations.pdf)
Cited by: §I, §II.
[9] Y. Zhang, H. Tang, H. Li, and S. Wang (2025)
Integration and interaction of next-generation AI-focused data centers
with smart grids and district energy systems: the state-of-the-art,
opportunities and challenges.
Renewable and Sustainable Energy Reviews 224, pp. 116097.
Cited by: §I.
[10] H. Gan and P. Ranganathan (2025)
Balance of power: a full-stack approach to power and thermal
fluctuations in ml infrastructure.
External Links: Link (https://cloud.google.com/blog/topics/systems/mitigating-p
ower-and-thermal-fluctuations-in-ml-infrastructure?hl=en)
Cited by: §I, Remark 2.
[11] NERC Large Load Task Force (2025)
Characteristics and risks of emerging large loads.
Technical report
North American Electric Reliability Corporation (NERC).
Cited by: §I, §III-A.

[12] P. Patel et al. (2024)
Characterizing power management opportunities for LLMs in the
cloud.
In Proceedings of the 29th ACM International Conference on
Architectural Support for Programming Languages and Operating
Systems, Volume 3,
pp. 207–222.
Cited by: §I, §III-A, §III-A, §III-A, §III-A, §III-B, §III-C, §III.
[13] D. D’Ambrosio et al. (2025)
Energy and AI.
Technical report
International Energy Agency (IEA).
Cited by: §II, §II.
[14] L. de Roucy-Rochegonde and A. Buffard (2025)
AI, data centers and energy demand: reassessing and exploring the
trends.
Ifri Papers.
Cited by: §II.
[15] A. de Vries-Gao (2025)
Artificial intelligence: supply chain constraints and energy
implications.
Joule 9 (6).
Cited by: §II.
[16] X. Wang, C. Na, E. Strubell, S. Friedler, and S. Luccioni (2023)
Energy and carbon considerations of fine-tuning BERT.
arXiv preprint arXiv:2311.10267.
Cited by: §II.
[17] Q. Hu, P. Sun, S. Yan, Y. Wen, and T. Zhang (2021)
Characterization and prediction of deep learning workloads in large-
scale GPU datacenters.
In Proceedings of the International Conference for High Performance
Computing, Networking, Storage and Analysis,
pp. 1–15.
Cited by: §II, §III-A.
[18] J. You et al. (2025)
Scaling intelligence: the exponential growth of AI’s power needs.
Technical report

EPRI White Paper no. 3002033669.
Cited by: §II, footnote 1.
[19] V. Avelar, P. Donovan, P. Lin, W. Torell, and M. A. T. Arango (2023)
The AI disruption: challenges and guidance for data center design.
Artificial Intelligence in Medicine 138.
Cited by: §II.
[20] B. Eichman (2024)
Inference zones: how data centers support real-time AI.
External Links: Link (https://www.coresite.com/blog/inference-zones-how-data-
centers-support-real-time-ai)
Cited by: §II.
[21] Q. Hu et al. (2024)
Characterization of large language model development in the
datacenter.
In 21st USENIX Symposium on Networked Systems Design and
Implementation (NSDI 24),
pp. 709–729.
Cited by: §III-A, §III-A, §III.
[22] I. Latif, A. C. Newkirk, M. R. Carbone, A. Munir, Y. Lin, J. Koomey, X.
Yu, and Z. Dong (2024)
Empirical measurements of AI training power demand on a GPU-
accelerated node.
arXiv preprint arXiv:2412.08602.
Cited by: §III-A, §III-A, §III, Remark 2.
[23] V. Singhania, S. Aga, and M. Assem Ibrahim (2024)
Methodology for fine-grain GPU power visibility and insights.
arXiv e-prints, pp. arXiv–2412.
Cited by: §III-A, §III.
[24] S. Samsi, M. L. Weiss, D. Bestor, B. Li, M. Jones, A. Reuther, D.
Edelman, W. Arcand, C. Byun, J. Holodnack, et al. (2021)
The MIT supercloud dataset.
In 2021 IEEE High Performance Extreme Computing Conference
(HPEC),
pp. 1–8.
Cited by: §III.
[25] A. Borghesi et al. (2023)

M100 exadata: a data collection campaign on the cineca’s
marconi100 tier-0 supercomputer.
Scientific Data 10 (1), pp. 288.
Cited by: §III.
[26] R. A. Bridges, N. Imam, and T. M. Mintz (2016)
Understanding GPU power: a survey of profiling, modeling, and
simulation methods.
ACM Computing Surveys (CSUR) 49 (3), pp. 1–27.
Cited by: §III-A.
[27] P. Sinha, A. Guliani, R. Jain, B. Tran, M. D. Sinclair, and S.
Venkataraman (2022)
Not all GPUs are created equal: characterizing variability in large-
scale, accelerator-rich systems.
In SC22: International Conference for High Performance Computing,
Networking, Storage and Analysis,
pp. 01–15.
Cited by: §III-A, §III-A.
[28] H. V. Pham et al. (2020)
Problems and opportunities in training deep learning software
systems: an analysis of variance.
In Proceedings of the 35th IEEE/ACM international conference on
automated software engineering,
pp. 771–783.
Cited by: §III-A.
[29] R. Jain, B. Tran, K. Chen, M. D. Sinclair, and S. Venkataraman (2024)
PAL: a variability-aware policy for scheduling ML workloads in GPU
clusters.
In SC24: International Conference for High Performance Computing,
Networking, Storage and Analysis,
pp. 1–18.
Cited by: §III-A.
[30] V. Singhania, S. Aga, and M. A. Ibrahim (2025)
FinGraV: methodology for fine-grain gpu power visibility and insights.
In 2025 IEEE International Symposium on Performance Analysis of
Systems and Software (ISPASS),
pp. 96–107.
Cited by: §III-A.

[31] S. G. Vennelaganti and S. Jones (2025)
Battery storage applications at data centers.
Tesla.
External Links: Link (https://www.nerc.com/comm/RSTC/LLTF/LLTF_April_Me
eting_&_Technical_Workshop_Presentations_.pdf)
Cited by: §III-A.
[32] B. Li, R. Arora, S. Samsi, T. Patel, W. Arcand, D. Bestor, C. Byun, R.
B. Roy, B. Bergeron, J. Holodnak, et al. (2022)
AI-enabling workloads on large-scale GPU-accelerated system:
characterization, opportunities, and implications.
In 2022 IEEE International Symposium on High-Performance
Computer Architecture (HPCA),
pp. 1224–1237.
Cited by: §III-A.
[33] A. Radovanovic, B. Chen, S. Talukdar, B. Roy, A. Duarte, and M.
Shahbazi (2021)
Power modeling for effective datacenter planning and compute
management.
IEEE Transactions on Smart Grid 13 (2), pp. 1611–1621.
Cited by: §III-C.
[34] D. N. D. Patel and J. E. Ontiveros (2024)
AI datacenter energy dilemma - race for AI datacenter space.
External Links: Link (https://semianalysis.com/2024/03/13/ai-datacenter-energ
y-dilemma-race)
Cited by: §III-C.
[35] E. Choukse et al. (2025)
Power stabilization for AI training datacenters.
arXiv preprint arXiv:2508.14318.
Cited by: Remark 2.
[36] H. Cui, F. Li, and K. Tomsovic (2020)
Hybrid symbolic-numeric framework for power system modeling and
analysis.
IEEE Transactions on Power Systems 36 (2), pp. 1373–1384.
Cited by: §IV-A, §IV-A.
[37] L. H. Konstantin F. Pilz (2025)
AI’s power requirements under exponential growth.
Technical report

RAND.
External Links: Link (https://www.rand.org/pubs/research_reports/RRA3572-1.
html)
Cited by: §IV-A.
[38] A. Almunif, L. Fan, and Z. Miao (2020)
A tutorial on data-driven eigenvalue identification: prony analysis,
matrix pencil, and eigensystem realization algorithm.
International Transactions on Electrical Energy Systems 30 (4),
pp. e12283.
Cited by: §IV-A.
[39] D. J. Trudnowski, J. W. Pierre, N. Zhou, J. F. Hauer, and M. Parashar
(2008)
Performance of three mode-meter block-processing algorithms for
automated dynamic stability assessment.
IEEE Transactions on Power Systems 23 (2), pp. 680–690.
Cited by: §IV-A.
[40] B. Hartmann, I. Vokony, and I. Táczi (2019)
Effects of decreasing synchronous inertia on power system dynamics
—overview of recent experiences and marketisation of services.
International Transactions on Electrical Energy Systems 29 (12),
pp. e12128.
Cited by: §IV-B.
[41] WECC Renewable Energy Modeling Task Force (2017)
Central station PV plant model validation guideline.
Technical report
Western Electricity Coordinating Council (WECC), Salt Lake City, UT
(United States).
Cited by: §IV-B.
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