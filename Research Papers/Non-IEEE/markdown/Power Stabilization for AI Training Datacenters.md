|     |     | Power |     | Stabilization |     |     | for | AI Training |     | Datacenters |     |     |     |     |     |
| --- | --- | ----- | --- | ------------- | --- | --- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- |
Esha Choukse, Brijesh Warrier, Scot Heath, Luz Belmont, April Zhao, Hassan Ali Khan, Brian Harry1,
Matthew Kappel, Russell J. Hewett1, Kushal Datta, Yu Pei, Caroline Lichtenberger, John Siegler,
|     |     | Lukofsky1, |     |     | Kahn1, |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
David Zaid Gurpreet Sahota, Andy Sullivan, Charles Frederick, Hien Thai,
Rebecca Naughton1, Daniel Jurnove, Justin Harp1, Reid Carper, Nithish Mahalingam,
Srini Varkala, Alok Gautam Kumbhare, Satyajit Desai, Venkatesh Ramamurthy,
Praneeth Gottumukkala, Girish Bhatia, Kelsey Wildstone, Laurentiu Olariu,
|                                          |     |     | Ileana | Incorvaia, |     | Alex  | Wetmore,  | Prabhat Ram,      | Melur |           | Raghuraman |     |     |     |     |
| ---------------------------------------- | --- | --- | ------ | ---------- | --- | ----- | --------- | ----------------- | ----- | --------- | ---------- | --- | --- | --- | --- |
|                                          |     |     |        | Mohammed   |     | Ayna, | Mike      | Kendrick, Ricardo |       | Bianchini |            |     |     |     |     |
| 5202 guA 12  ]RA.sc[  2v81341.8052:viXra |     |     |        |            |     |       | Microsoft |                   |       |           |            |     |     |     |     |
Aaron Hurst, Reza Zamani, Xin Li, Michael Petrov, Gene Oden, Rory Carmichael
OpenAI
Tom Li, Apoorv Gupta, Pratikkumar Patel, Nilesh Dattani, Lawrence Marwong, Rob Nertney,
Hirofumi Kobayashi, Jeff Liott, Miro Enev, Divya Ramakrishnan, Ian Buck, Jonah Alben
NVIDIA
Abstract—Large Artificial Intelligence (AI) training work- communicate,ordoothertasks.Thiscouldbeduringtheall-
loads spanning several tens of thousands of GPUs present reduce communication collective in an iteration [16], where
| unique power     | management  |          | challenges. |          | These  | arise  | due to    | the               |         |         |      |                |     |          |           |
| ---------------- | ----------- | -------- | ----------- | -------- | ------ | ------ | --------- | ----------------- | ------- | ------- | ---- | -------------- | --- | -------- | --------- |
|                  |             |          |             |          |        |        |           | the participating |         | GPUs    | need | to synchronize |     | on the   | model-    |
| high variability |             | in power | consumption |          | during | the    | training. |                   |         |         |      |                |     |          |           |
|                  |             |          |             |          |        |        |           | weight            | update, | or when | a    | checkpoint     |     | is being | recorded. |
| Given the        | synchronous |          | nature      | of these | jobs,  | during | every     |                   |         |         |      |                |     |          |           |
iteration there is a computation-heavy phase, where each GPU While the power utilized in a computationally heavy phase
works on the local data, and a communication-heavy phase in a GPU can be close to its TDP (Thermal Design Power),
wherealltheGPUssynchronizeonthedata.Becausecompute- the power utilized during the communication phase can be
| heavy phases | require     | much            | more   | power | than          | communication |             |          |                 |        |          |      |      |           |        |
| ------------ | ----------- | --------------- | ------ | ----- | ------------- | ------------- | ----------- | -------- | --------------- | ------ | -------- | ---- | ---- | --------- | ------ |
|              |             |                 |        |       |               |               |             | close to | the idle        | power. |          |      |      |           |        |
| phases,      | large power | swings          | occur. |       | The amplitude |               | of these    |          |                 |        |          |      |      |           |        |
|              |             |                 |        |       |               |               |             | Such     | huge variations |        | in power | draw | lead | to swings | at the |
| power swings | is          | ever increasing |        | with  | the increase  |               | in the size |          |                 |        |          |      |      |           |        |
of training jobs. An even bigger challenge arises from the node level (Figure 1). Furthermore, due to the large and
frequencyspectrumofthesepowerswingswhich,ifharmonized synchronous nature of the job, participating nodes are co-
withcriticalfrequenciesofutilities,cancausephysicaldamage located to form a majority of a datacenter, or even multiple
tothepowergridinfrastructure.Therefore,tocontinuescaling
|             |            |              |         |            |              |               |           | datacenters  | in     | the same | grid,       | making |         | the power   | swings     |
| ----------- | ---------- | ------------ | ------- | ---------- | ------------ | ------------- | --------- | ------------ | ------ | -------- | ----------- | ------ | ------- | ----------- | ---------- |
| AI training | workloads  |              | safely, | we need    | to stabilize |               | the power |              |        |          |             |        |         |             |            |
|             |            |              |         |            |              |               |           | visible      | at the | rack,    | datacenter, | and    | power   | grid        | levels. At |
| of such     | workloads. | This         | paper   | introduces |              | the challenge | with      |              |        |          |             |        |         |             |            |
|             |            |              |         |            |              |               |           | scale, these | swings |          | can amount  |        | to tens | or hundreds | of         |
| production  | data       | and explores |         | innovative | solutions    |               | across    | the          |        |          |             |        |         |             |            |
stack:software,GPUhardware,anddatacenterinfrastructure. megawatts, occurring at frequencies that, if poorly aligned
We present the pros and cons of each of these approaches with the resonant characteristics of power grid components
| and finally | present | a multi-pronged |     |     | approach | to  | solving | the            |            |     |     |                   |     |         |          |
| ----------- | ------- | --------------- | --- | --- | -------- | --- | ------- | -------------- | ---------- | --- | --- | ----------------- | --- | ------- | -------- |
|             |         |                 |     |     |          |     |         | (e.g., turbine | generators |     | or  | long transmission |     | lines), | can risk |
challenge.Theproposedsolutionsarerigorouslytestedusinga
|                  |     |               |          |                 |     |          |          | grid instability |     | and mechanical |         | failure.  | These | issues   | are not |
| ---------------- | --- | ------------- | -------- | --------------- | --- | -------- | -------- | ---------------- | --- | -------------- | ------- | --------- | ----- | -------- | ------- |
| combination      | of  | real hardware |          | and Microsoft’s |     | in-house | cloud    |                  |     |                |         |           |       |          |         |
|                  |     |               |          |                 |     |          |          | theoretical      | —   | multiple       | utility | providers |       | have now | docu-   |
| power simulator, |     | providing     | critical | insights        |     | into the | efficacy | of               |     |                |         |           |       |          |         |
these interventions under real-world conditions. mented the impact of harmonics induced by synchronized
|     |     |     |     |     |     |     |     | computing | loads | [11]. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ----- | --- | --- | --- | --- | --- |
I. INTRODUCTION
|     |     |     |     |     |     |     |     | This | paper | proposes | a   | multi-faceted |     | approach | to miti- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | -------- | --- | ------------- | --- | -------- | -------- |
Thepastfewyearshaveseenafastincreaseinthesizeand gate these risks, grounded in real-world production teleme-
|          |            |     |          |          |     |          |         | try. We | first characterize |     |     | the amplitude |     | and frequency | of  |
| -------- | ---------- | --- | -------- | -------- | --- | -------- | ------- | ------- | ------------------ | --- | --- | ------------- | --- | ------------- | --- |
| speed of | deployment | of  | training | clusters | for | frontier | founda- |         |                    |     |     |               |     |               |     |
tional large AI models [20], [18]. A single training job can power oscillations observed in hyperscale training clusters.
|                                   |     |     |     |     |     |                  |     | Then, we | evaluate | three | classes | of  | mitigation: | (1) | software- |
| --------------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | -------- | ----- | ------- | --- | ----------- | --- | --------- |
| spanmorethanahundredthousandGPUs, |     |     |     |     |     | [15],[23].During |     |          |          |       |         |     |             |     |           |
atrainingjob,theparticipatingGPUsworkinlockstepunder based approaches that inject controlled workloads to smooth
the bulk synchronous paradigm [16], [19]. Although most transitions, (2) GPU-level firmware features that enforce
|        |          |      |          |       |               |     |       | ramping | constraints |     | and power | floors, |     | and (3) | rack-level |
| ------ | -------- | ---- | -------- | ----- | ------------- | --- | ----- | ------- | ----------- | --- | --------- | ------- | --- | ------- | ---------- |
| of the | training | time | is spent | doing | computational |     | work, |         |             |     |           |         |     |         |            |
there are phases where all the participating GPUs need to energy storage to absorb and release power as needed. Each
|     |     |     |     |     |     |     |     | technique | is assessed |     | for its | effectiveness, |     | energy | efficiency, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------- | -------------- | --- | ------ | ----------- |
1WorkwasdonewhentheywereemployeesatMicrosoft. and deployability. Finally, we advocate for cross-industry

GPU Power Draw Time Series (Normalized)
1.0
GPU Power Draw (W) (Normalized)
0.9
dezilamroN )W( warD rewoP UPG 0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0.0
|     | 0   |     |     |     | 50  |     | 100 |     |     | 150 |     |     | 200 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (s)
|     |     |     |     | Fig.1. | Powerreadingsfromanat-scaletrainingjobonDGX-H100racks. |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
co-design across software, hardware, and infrastructure to Subsequently, during the backward pass, these devices com-
ensure that AI systems remain both scalable and power- pute local gradients of the loss function with respect to
| aware. |     |     |     |     |     |     |     | theirassignedsubsetofdata.BecauseallparticipatingGPUs |     |             |        |       |            |         |
| ------ | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | ----------- | ------ | ----- | ---------- | ------- |
|        |     |     |     |     |     |     |     | must converge                                         |     | to the same | global | model | state, the | locally |
II. BACKGROUNDANDMOTIVATION
computedgradientsmustbeaggregatedandsharedaftereach
| A. Rise | of large | training | jobs |     |     |     |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
iteration.
|      |          |         |        |           |     |            |          | This aggregation |     | is typically | performed |     | via an all-reduce |     |
| ---- | -------- | ------- | ------ | --------- | --- | ---------- | -------- | ---------------- | --- | ------------ | --------- | --- | ----------------- | --- |
| Over | the past | several | years, | the field | of  | artificial | intelli- |                  |     |              |           |     |                   |     |
gence has seen explosive growth in the size and complexity operation, most commonly implemented using optimized
of neural networks. Originally, popular models such as libraries(e.g.,NVIDIANCCL[14]).Throughtheall-reduce,
|     |     |     |     |     |     |     |     | partial gradients |     | are summed | or  | averaged | across all | GPUs, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | --- | -------- | ---------- | ----- |
AlexNet[7]containedontheorderof60millionparameters
and could be trained on a single GPU. However, in the ensuring that every model replica obtains an identical final
|     |     |     |     |     |     |     |     | gradient | vector. | After this | communication |     | step, model | pa- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ---------- | ------------- | --- | ----------- | --- |
timesince,thecommunityhasrapidlyembraced“foundation
models” with billions, and even hundreds of billions of rameters are synchronously updated on each GPU, thereby
parameters. The scaling of AI models has been driven by preserving consistency across the distributed system. This
iterationoflocalcomputationandall-reducecommunication
| reinforcing | trends | in: | (1) architectural |     | advances | such | as  |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ----------------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Transformers, (2) system design strategies like data, tensor, formsthecoreofbulk-synchronousparallelism[16],wherein
and pipeline parallelism that enable the distribution of com- trainingcannotadvancetothenextiterationuntilalldevices
putation,(3)hardwareevolution,includinghigherbandwidth complete the gradient synchronization phase.
interconnects and specialized datacenter GPU devices, and Less frequent communication phases occur during check-
|                |            |     |       |      |      |            |     | pointing, | when | model states | are | periodically | saved | to per- |
| -------------- | ---------- | --- | ----- | ---- | ---- | ---------- | --- | --------- | ---- | ------------ | --- | ------------ | ----- | ------- |
| (4) datacenter | deployment |     | sizes | that | have | grown from | <   |           |      |              |     |              |       |         |
10MW to >100MW. sistent storage. Checkpointing preserves the training state
In particular, the training of GPT-3 (175B parameters) [2] at regular intervals, safeguarding long-running jobs against
|                |     |            |       |             |     |       |      | common | hardware | or software | failures |     | [9]. By periodically |     |
| -------------- | --- | ---------- | ----- | ----------- | --- | ----- | ---- | ------ | -------- | ----------- | -------- | --- | -------------------- | --- |
| and successors |     | like Grok1 | (314B | parameters) |     | [23], | PaLM |        |          |             |          |     |                      |     |
(540B parameters) [3], Llama3.1 (405B parameters) [21], writing model parameters—and, in some cases, optimizer
|           |           |     |       |        |               |        |     | states—to | persistent | storage, | checkpointing |     | enables | a faster |
| --------- | --------- | --- | ----- | ------ | ------------- | ------ | --- | --------- | ---------- | -------- | ------------- | --- | ------- | -------- |
| etc., has | showcased | the | trend | toward | massive-scale | models |     |           |            |          |               |     |         |          |
thatdemandequallymassivecomputationalresources.While and more consistent recovery, allowing training to resume
domain-targeted training, model size efficiency, and the use without losing significant computational effort or compro-
|               |           |     |              |     |         |         |        | mising convergence |     | guarantees.Though |     |     | not as frequent | as  |
| ------------- | --------- | --- | ------------ | --- | ------- | ------- | ------ | ------------------ | --- | ----------------- | --- | --- | --------------- | --- |
| of pretrained | backbones |     | has recently |     | enabled | cheaper | train- |                    |     |                   |     |     |                 |     |
ing runs for model families like Phi [10] and DeepSeek [5], gradient synchronization, checkpointing can still introduce
|     |     |     |     |     |     |     |     | non-trivial | network | and | I/O overhead | across | the cluster. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | ------------ | ------ | ------------ | --- |
trendsshowthatthefoundationmodeltrainingwillstillspan
several tens-of-thousands of GPUs. Although techniques for overlapping communication and
|     |     |     |     |     |     |     |     | computation | (e.g., | dedicated | DMA | engines | or asynchronous |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --------- | --- | ------- | --------------- | --- |
B. Compute and communication phases kernel launches) can reduce idle time, most data-parallel
Large-scaletrainingofmodelsproceedsiniterations,each workloadsretainasignificantsynchronizationstepattheend
iteration going over a small batch of the training data, ofeachiteration [19],[5].Checkpointingand othertransient
encompassing distinct compute and communication phases. phases, such as failure recovery or dynamic load balancing,
The model and the data are distributed across the partici- can further exacerbate power variations by introducing addi-
pating GPUs using various parallelism techniques [19]. In tionalpatternsofactivityandinactivityacrosstheGPUfleet.
the forward pass of each iteration, each GPU processes its Asynchronous training methods with lazy weight updates
own portion of the mini-batch independently, calculating avoid this synchronicity challenge, but have been shown to
partial predictions based on the current model parameters. have accuracy and convergence trade-offs [8].

failure, particularly in large 2-pole and 4-pole turbine de-
signs.
E. Challenges at utility grid systems
AI workload frequencies fall into the sub-synchronous
regime. These can excite resonant modes in transmission
networks potentially leading to sub-synchronous resonance
(SSR) [22] or inter-area oscillations. Furthermore, rapid,
cyclical power swings can lead to voltage flicker visible on
Fig.2. GB200serverpowerbreakdown. lightingsystemsandfrequencymodulationthatimpactsgrid
frequency regulation, particularly in isolated or constrained
regions.
C. Power consumption during training
This is further complicated by the size of the training
The power draw of GPUs can rapidly swing as the clusters: as GPU counts grow, the aggregate load swing am-
application transitions between compute and communication plitudeatthesecriticalfrequenciesincreases(Figure3),mag-
phases (Figure 1). In the compute phase, the GPU tensor nifying the potential resonance effects in any interconnected
cores typically run at or near full utilization, drawing power turbine or generator. To eliminate the possibility that shaft
close to the TDP of the device [17]. By contrast, during damage or other less severe effects (e.g., breakers opening
the communication phase, in which the GPUs synchronize resulting in islands) occur, prevention of the excitation of
gradients via collective operations (e.g., all-reduce), or are these critical frequencies is required.
working on checkpointing the model, compute resources sit
III. SPECIFICATIONSANDREQUIREMENTS
idleorunderutilized.Asaresult,thesameGPUmayexhibit
We present the utility-level specifications and additional
a dramatic drop in power consumption over relatively short
recommended requirements for effective mitigation strate-
timescales — ranging from once per second or less, to once
gies.
every tens of seconds, depending on the scale of the job.
At the server-level, GPUs contribute more than 50% A. Utility-level specification
of the provisioned power, as shown in Figure 2. There-
The specification can vary from one utility to the other.
fore, these cyclical changes in utilization across thousands
Utility-level specification can be divided into time-domain
of tightly synchronized GPUs manifest as large-amplitude
spec and frequency-domain spec.
power swings at the rack, row, and potentially even the
1.Time-domainspec.Utilityoperatorsmayimposetime-
datacenter power feed levels. The amplitude of these swings
domain constraints on how quickly a load may change its
grows proportionally with the number of GPUs participat-
power draw. These constraints include:
ing in the job and their peak per-GPU power. In extreme
cases, aggregate power consumption can oscillate by tens • Ramp-Up Rate: The maximum permitted rate of
increase in power demand, typically expressed in
of megawatts within a single datacenter [20]. Such high-
megawatts per second (MW/s).
magnitude variability can strain power distribution units,
affect upstream transformers, and introduce harmonic fre- • Ramp-Down Rate: The maximum permitted decrease
in power consumption over time.
quencies that may interfere with the broader utility grid.
• Dynamic Power Range: The allowed short-term de-
In summary, while modern GPU clusters continue to
viation in power draw before ramp constraints are
deliver exceptional FLOPS (floating point operations per
triggered.
second) performance for large-scale AI training, the in-
Figure 4 illustrates the time-domain spec with a power
herent synchronicity of deep learning workloads leads to
waveform.
pronounced swings in power draw. These swings pose new
Time-domain constraints ensure the grid can respond
challenges in utility and grid-level stability, motivating the
effectively to load changes without triggering oscillations or
need for systemic solutions that address variability at the
frequencydisturbances.Inpractice,utilitiesmonitorplanned
software, hardware, and infrastructure layers.
versus actual power usage using 5- to 15-minute scheduling
intervals. Deviations beyond allowed margins may result in
D. Challenges to generation systems
financial penalties or curtailment notices. These planning
Thehigher-orderriskforthisemergeswhenthesecyclical constraints are vital for maintaining reliability in modern
load fluctuations align with or excite torsional resonances power systems, especially in real-time operations and day-
in upstream turbine-generator powertrains [4], [6]. As doc- ahead markets.
umented in analyses of large steam turbine rotors, torsional The dynamic power range specification is particularly
vibration occurs at particular natural frequencies, and an relevant for fast-changing workloads. It defines how much
external disturbance at or near these frequencies can induce instantaneous fluctuation in power draw is acceptable, usu-
high-amplitude oscillations in the rotor shafts. Prolonged ally over sub-second intervals. These tolerances are often
resonance, even if partial, risks mechanical fatigue or shaft informedbygridstandardssuchasIEC61000-3-3[1],which

FFT of GPU Power Draw
FFT Magnitude
0.025
0.020
edutingaM latot fo noitcarF
0.015
0.010
0.005
0.000
|     |     | DC 1 2 | 3 4 | 5 6 | 7 8 9 10 | 11 12 13 14 | 15 16 | 17  | 18 19 20 |     |     |     |
| --- | --- | ------ | --- | --- | -------- | ----------- | ----- | --- | -------- | --- | --- | --- |
Frequency (Hz)
|     |     |     | Fig.3. | FrequencycomponentsofthepowerwaveformshowninFigure1. |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.4. Specificationforpowerstabilizationintimedomain.PLdenotesthedeviceTDPhere,andfloordenotesMPF.Ramp-upandramp-downtimes
arecalculatedfromtheprogrammedramprates.PowerbetweenMPFandceilingisallowedasadynamicpowerrange.
sets thresholds for allowable voltage flicker and short-term AIworkloadpowertraceslikethoseinFigure1showFFT
harmonic disturbances. energy concentrated between 0.2–3Hz (Figure 3)—close
2. Frequency-domain spec. In addition to ramp lim- to known resonant modes of turbine-generator shafts and
|              |           |                       |     |     |                | long transmission |     | lines. | As workload | behavior | evolves, | the |
| ------------ | --------- | --------------------- | --- | --- | -------------- | ----------------- | --- | ------ | ----------- | -------- | -------- | --- |
| its, utility | providers | need frequency-domain |     |     | specifications |                   |     |        |             |          |          |     |
to prevent resonance with power system components. AI emitted frequency can shift, so specs must cover a dynamic
range.
| workloads, | due to       | their periodic, | synchronized |      | nature, can  |     |     |     |     |     |     |     |
| ---------- | ------------ | --------------- | ------------ | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| emit power | oscillations | that            | align with   | grid | or generator |     |     |     |     |     |     |     |
resonant frequencies, causing sub-synchronous resonance B. Understanding the frequency-domain spec
| (SSR), voltage | flicker,         | or equipment | stress.        |     |     |             |            |        |               |             |             |       |
| -------------- | ---------------- | ------------ | -------------- | --- | --- | ----------- | ---------- | ------ | ------------- | ----------- | ----------- | ----- |
|                |                  |              |                |     |     | The primary | issue      | unique | to a periodic | large       | synchronous |       |
| A typical      | frequency-domain |              | spec includes: |     |     |             |            |        |               |             |             |       |
|                |                  |              |                |     |     | load is the | excitation | of     | resonant      | frequencies | in the      | power |
• A critical frequency range, e.g., 0.1−20 Hz. generation and delivery network. Resonant frequencies exist
Amaximumallowedspectralmagnitude,e.g.capped from approximately 0.16Hz to greater than 60Hz in various
•
20%
at of total harmonic energy within that range. components of the system:

1. <1Hz – Resonance in this range is present due to increase in energy consumption, preserving both cost-
the naturally occurring characteristics of long transmission effectiveness and sustainability goals.
linesconnectingportionsofthegridwhichareindependently ControlEDP.DatacenterGPUsallowpowerovershoots
•
strong. A 2019 NERC study [12] of interconnection-wide at shorter time-scales (50ms), called electrical design
oscillatory behavior observed that most dominant modes are power (EDP) peaks (or, EDPp) [13], while still main-
highly damped, though damping varies based on system taining the TDP at a granularity of 1 second. These
topology and configuration. The damping ratio refers to the peaks can be seen in Figure 5 each time the workload
abilityofthesystemtostoposcillatingafterastepexcitation spikes up. Although usually the systems are designed
andvaluesmuchgreaterthan1aredesirableastheyindicate such that the EDP peaks should not be visible beyond
greater speed at which the resulting oscillations are reduced. the rack power supply units (PSUs), depending on the
In the case of periodic load variations, there is a danger system design, this may change. If the EDP peaks are
of instability despite the damping ratios being greater than visibleatthePDUandutilitylevel,theEDPmightneed
one. An incident in January 2019 caused by an unstable tobesettoalowervaluetoensurecompliancewiththe
| combinedcycleunitinFloridaquicklygrewinmagnitudeto |        |       |         |                |           |     | utility | spec. |     |     |     |     |     |
| -------------------------------------------------- | ------ | ----- | ------- | -------------- | --------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
| a somewhat                                         | stable | point | and not | until the unit | was taken | out |         |       |     |     |     |     |     |
of service did the oscillations cease [11]. The magnitude of IV. MITIGATIONSTRATEGIES
thedrivingsourcewasapproximately200MW.Thepotential Thecriticalfrequencies,andthemagnitudeacceptableata
magnitude of the synchronous portion of the load for large criticalfrequency,togetherrepresentaspecificationsfromthe
training jobs can be much greater. While the oscillations utility.Thespecificationcanvarybetweenutilities.Solutions
produced during the event in 2019 did not cause serious in this space should be able to meet even the most stringent
| disruptions,amuchlargerdistributedloadcouldhavegreater |     |     |     |     |     |     | specifications. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
consequences.
|        |     |         |         |                     |         |     | A. Software-only |     | mitigation |     |     |     |     |
| ------ | --- | ------- | ------- | ------------------- | ------- | --- | ---------------- | --- | ---------- | --- | --- | --- | --- |
| 2. 1Hz | to  | 2.5Hz – | In this | range, oscillations | between |     |                  |     |            |     |     |     |     |
closely coupled sources are possible, for instance, units in A purely software-based approach to mitigating power
the same plant or plant to plant in close proximity. swings from the primary workload focuses on dynami-
callyintroducingpower-hungrysecondaryworkloadssuchas
3. 7Hzto>100Hz–Thisistherangeoccupiedbyshaft
torsional critical frequencies as discussed earlier. These are GEMM kernels, whenever the GPU activity level or power
the result of one of more masses on a turbine-generator set falls below a designated threshold. By doing so, the system
|             |         |           |        |        |           |         | can sustain | a more | uniform | power | draw | across the | compute |
| ----------- | ------- | --------- | ------ | ------ | --------- | ------- | ----------- | ------ | ------- | ----- | ---- | ---------- | ------- |
| oscillating | against | the other | masses | on the | shaft. In | a large |             |        |         |       |      |            |         |
steamturbinegenerator,therearemanystages.Typically,the andcommunicationphasesofeachtrainingiteration,thereby
|               |     |            |         |                |     |         | reducing | the amplitude |     | of power | fluctuations | visible | to the |
| ------------- | --- | ---------- | ------- | -------------- | --- | ------- | -------- | ------------- | --- | -------- | ------------ | ------- | ------ |
| high-pressure |     | stage, the | re-heat | stage and then | one | or more |          |               |     |          |              |         |        |
low-pressure stages. Each of these stages is coupled by a datacenter and utility infrastructure.
lengthofshaftwiththefinalconnectionexistingbetweenthe Secondary workload. This power-hungry secondary
|                   |     |         |         |           |           |        | workload | could | either | be a lower-priority, |     | useful | job, or an |
| ----------------- | --- | ------- | ------- | --------- | --------- | ------ | -------- | ----- | ------ | -------------------- | --- | ------ | ---------- |
| last low-pressure |     | section | and the | generator | where the | torque |          |       |        |                      |     |        |            |
from the entire output of all turbine sections is transmitted. artificial workload. The challenge with a useful job is that
|     |     |     |     |     |     |     | the job’s | state would | need | to be | saved | and restored, | causing |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | ----- | ----- | ------------- | ------- |
C. Additional requirements additional delay in power smoothing, and performance im-
|     |     |     |     |     |     |     | pact to the | primary | workload. |     | An artificial | workload | would |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | --- | ------------- | -------- | ----- |
Successful mitigation of the large, synchronous power avoid such challenges, with the downside of wasted energy.
| swings | must satisfy | four | additional | requirements: |     |     |             |     |              |     |         |          |           |
| ------ | ------------ | ---- | ---------- | ------------- | --- | --- | ----------- | --- | ------------ | --- | ------- | -------- | --------- |
|        |              |      |            |               |     |     | Monitoring. |     | An important |     | note is | that the | secondary |
Ability to meet different utility specifications. Power workload cannot be deterministically called within a com-
•
regulations and reliability constraints vary across util- munication library. The core of the problem is that the GPU
ities and geographic regions. Therefore, any proposed power drop is the result of several compute kernels end-
intervention must be adaptable to diverse power quality ing, rather than a communication kernel starting. Therefore,
standards and address the range of critical frequencies instead of a compiler-based solution, we prefer a software
identified by different transmission and distribution op- mechanism that uses real-time, fine-grained power and ac-
erators. tivity monitoring of the GPUs. Today, NVIDIA datacenter
• Minimal performance loss. AI training jobs run for GPUs have capability to expose instantaneous or averaged
extended periods at substantial computational expense. in-band power and activity readings at a minimum of 1-
Any load-shaping or smoothing mechanism should in- 100ms latency, depending on the acceptable reliability of
troducenegligibledegradationtotrainingthroughputor the counters. The reliable 100ms counters are too slow for
convergencetimes.Solutionsthatimposeunduelatency a use-case where we would want to detect power swings at
orstallcriticaltrainingstepsriskdrivingupoperational 20Hzforinstance,needingustoinjectasecondaryworkload
costs, resources, and undermining the effectiveness of every 50 ms. Therefore, this solution will have to be built
large-scale model development. upon faster telemetry sources.
Minimal wasted energy. The ideal solution should Secondary workload start and stop conditions. The
•
reduceoreliminatepowervariabilitywithlittletononet secondary workload is started as soon as the block activity

(andthuspowerdraw)dropsbelowapresetlevel,preventing
adrasticpowerdip.Assoonastheutilizationfortheprimary
| workload | ramps         | up again, | the   | secondary | workload    | needs    |     |
| -------- | ------------- | --------- | ----- | --------- | ----------- | -------- | --- |
| to back  | off. However, | since     | there | are       | no activity | or power |     |
countersperprocesstoday,thesecondaryworkloadwillneed
| to periodically          | back        | off        | and read | the activity    | counters.      |          |     |
| ------------------------ | ----------- | ---------- | -------- | --------------- | -------------- | -------- | --- |
| The ramp-up              | and         | ramp-down  |          | requirement     | is easy        | to meet  |     |
| in a software-mitigation |             |            | by       | either stepping | up             | the load |     |
| synchronously,           | or          | staggering | the      | load            | ramp-up across | all the  |     |
| participating            | GPUs.       |            |          |                 |                |          |     |
| Firefly.                 | With these  | insights,  |          | we built        | a solution,    | named    |     |
| Firefly,                 | to mitigate | the        | power    | swings          | in software.   | We       |     |
Fig.5. GB200Powersmoothingresultswithasquare-wavemicrobench-
| used NVIDIA’s | Multi-Process |     |     | Service | (MPS), which | allows |     |
| ------------- | ------------- | --- | --- | ------- | ------------ | ------ | --- |
mark.
| multiple | CUDA processes |     | to    | share a      | single GPU | context, |     |
| -------- | -------------- | --- | ----- | ------------ | ---------- | -------- | --- |
| with the | provisioning   | to  | carve | up resources | as needed. | For      |     |
monitoring we used block activity counters from the GPU, could try predictive modeling of forthcoming communica-
and as a secondary workload, we used a series of matrix tion/computation phases. This could help reduce the perfor-
multiplicationsscaledasneeded.Fireflywasabletoincrease mance impact of this solution.
the power utilization all the way up to 100% of the TDP. 3. Priority scheduling: Faster, priority-based scheduling
Challenges. Although Firefly does not require any addi- mechanismsintheGPUcouldfurtheravoidtheneedtoself-
tional hardware features or infrastructure for mitigation, it preempt the secondary workload, reducing the interference
does present a few challenges. The first one is related to for the primary workload.
performanceoverheads.Thesecondaryworkloadneedssome 4.Softwaresolutioninthefirmware:Thehardwarevendor
memory and compute resources of its own. Additionally, could provide the software solution in a way that is tightly
the back-off based mechanism for stopping the secondary coupled with the scheduler and monitoring. This would re-
workload leads to performance loss for the primary work- ducetheoverheads,andthedependencyontheendcustomer.
load. With NVIDIA’s MPS, we were able to bring down Overall, software-based smoothing offers a flexible and
the performance overhead to the primary workload down to relatively quick-to-deploy solution, providing immediate re-
< 5%. However, there was a considerable amount of CPU lief from large power swings without hardware modifi-
cores and host-device bandwidth dedicated for processing cations. However, it requires a careful trade-off between
the GPU power data continuously at a 1 ms granularity. As limiting performance impact and minimizing wasted energy,
training jobs become more heterogeneous, requiring more thus underscoring the importance of precise telemetry, well-
CPU work, this can become a challenge too, making the designedfallbacklogic,andongoingcalibrationasthework-
| softwaresolutionveryexpensivefromaresourcestandpoint. |           |      |     |         |               |        | loads scale. |
| ----------------------------------------------------- | --------- | ---- | --- | ------- | ------------- | ------ | ------------ |
| Second,                                               | since the | GPUs | are | used in | direct-device | access |              |
B. GPU power smoothing
| mode by | most virtual | machine |     | offerings | from | large cloud |     |
| ------- | ------------ | ------- | --- | --------- | ---- | ----------- | --- |
providers today, this mitigation requires close collaboration Toavoidtheperformanceloss,secondaryworkloadtuning
between the end customer and the cloud provider, which with primary workload changes, and the close collaboration
might be difficult in certain settings. The solution may even requirementsincloudprovidersettings,wediscussapossible
need tuning as the primary workload changes, to ensure that GPU-level solution. The GPU power smoothing feature, as
the primary power patterns are well hidden. introduced in NVIDIA GB200, allows the developers in-
Third challenge is the reliability of this solution. In band, and the cloud provider out-of-band, to program a
particular, the MPS feature ties the failure domain of the presetprofiletoeachGPU.Theprofileincludesthefollowing
| primary | and secondary |     | workloads | at  | the GPU scale, | since | notable settings: |
| ------- | ------------- | --- | --------- | --- | -------------- | ----- | ----------------- |
they share the same GPU context. A fault in one workload 1. Ramp-up rate and ramp-down rate: These settings
can propagate to the other, making the setup more error- can be programmed to directly meet the requirements of
prone at scale. Improving reliability will require software utility’s time domain spec. These can be programmed in a
enhancements across multiple layers of the stack. watts per second format.
And finally, an artificial secondary workload, if not per- 2. Minimum Power Floor (MPF): This setting allows
forming real work, wastes energy. the user to set the floor for the power utilization by the
Potential optimizations. GPUduringstableperiodsofexecution.Incombinationwith
1.Separatefailuredomains:Iftheprimaryandsecondary the maximum allowed power (thermal design power) of the
jobs could be run in a way that the failure of secondary job GPU, this allows us to meet the dynamic power range of
doesnotleadtoacrashintheprimaryworkload,theat-scale the utility’s spec, ensuring that the power changes in short
reliability of this solution would benefit a lot. time-scales are within the spec.
2. Adaptive throttling of the secondary workload: Instead 3. Stop delay: This setting specifies how long the GPU
of being completely dependent on monitoring, the software should stay at the minimum power floor without any real

Normalized MPF Time Series
1.0
Original Power Draw (normalized)
| 0.9 |     |     |     |     |     |     |     |     |     | MPF Ceil (normalized) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
MPF Floor (normalized)
| 0.8 |     |     |     |     |     |     |     |     |     | Final GPU + MPF Power Draw (normalized) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- |
MPF Added Power (normalized)
warD rewoP dezilamroN 0.7
0.6
0.5
0.4
0.3
0.2
0.1
0.0
|     | 0   |     | 50  |     |     | 100 | 150 |     | 200 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (s)
Fig.6. Powersmoothingtotheminimumpowerfloor(MPF)simulatedonthetrainingwaveformfromFigure1.
workload activity before ramping down. This stop delay at the GPU level. This creates challenges in meeting tighter
presents a trade-off between performance impact and energy specs. Let us say for instance, the utility company requires
burn, while meeting the spec. us to meet a 10MW dynamic range, and we are running a
|       |      |                        |     |      |          |          | job using | 100MW | of power. | This requires | a   | dynamic power |
| ----- | ---- | ---------------------- | --- | ---- | -------- | -------- | --------- | ----- | --------- | ------------- | --- | ------------- |
| Since | this | feature implementation |     | uses | hardware | counters |           |       |           |               |     |               |
and the GPU’s power controller, the power floor engage and rangeof10%beingallowed,whichcannotbemetwithGPU
|               |           |           |         |               |          |            | power smoothing |     | today. |     |     |     |
| ------------- | --------- | --------- | ------- | ------------- | -------- | ---------- | --------------- | --- | ------ | --- | --- | --- |
| disengage     | latencies | can       | be very | small,        | allowing | us to meet |                 |     |        |     |     |     |
| the frequency |           | spec from | the     | utility. Note | that     | a high MPF |                 |     |        |     |     |     |
value will maximize the energy burn. On the other hand, the C. Energy-storage solution
dynamicpowerrangespecificationleadstoleastperformance The best-case solution to the training power-stabilization
| impact | at a | high MPF. |     |     |     |     |           |       |                |          |      |     |
| ------ | ---- | --------- | --- | --- | --- | --- | --------- | ----- | -------------- | -------- | ---- | --- |
|        |      |           |     |     |     |     | challenge | is an | energy-storage | solution | that |     |
Figure 5 shows this feature on a GB200 with a square- 1. Can directly measure the load,
| wave | power | micro-benchmark |     | with high | power | utilization |        |        |             |            |     |           |
| ---- | ----- | --------------- | --- | --------- | ----- | ----------- | ------ | ------ | ----------- | ---------- | --- | --------- |
|      |       |                 |     |           |       |             | 2. Has | enough | capacitance | to support | the | workload, |
across all the GPUs. The power floor was set to 65% of 3. Can meet the sudden rise/drop needs in power, and
| the TDP | of   | the GPU. The | figure    | shows  | the ramp-up, | steady        |        |        |               |          |     |                 |
| ------- | ---- | ------------ | --------- | ------ | ------------ | ------------- | ------ | ------ | ------------- | -------- | --- | --------------- |
|         |      |              |           |        |              |               | 4. Can | switch | modes between | charging |     | and discharging |
| phase,  | stop | delay, and   | ramp-down | phases | of           | the run. Note |        |        |               |          |     |                 |
quickly.
that the workload stays the same throughout, until the stop Anenergy-storagesolutiondoesnotwasteenergytosolve
| delay | phase, | where the | workload | has no | activity. |     |           |               |          |          |     |                 |
| ----- | ------ | --------- | -------- | ------ | --------- | --- | --------- | ------------- | -------- | -------- | --- | --------------- |
|       |        |           |          |        |           |     | the power | stabilization | problem. | Instead, | it  | can potentially |
Since the micro-benchmark shown in Figure 5 is not even reduce peak power needs in training, by using the low-
| representative |     | of the | true ups | and | downs | in the power |                     |     |        |            |     |                |
| -------------- | --- | ------ | -------- | --- | ----- | ------------ | ------------------- | --- | ------ | ---------- | --- | -------------- |
|                |     |        |          |     |       |              | power communication |     | phases | to charge, | and | release energy |
waveformduringatrainingworkload,weuseMicrosoft’sin- during high-power computation phases. Figure 7 shows a
house power simulator called StratoSim, to show the impact simulatedexampleofhowthissolutioncouldwork.Weshow
of power smoothing on the real waveform from Figure 1. the battery charge along with the final waveform.
Figure 6 shows the results. The floor was set to 90% of the Placement level. The main design question concerns the
TDPforthissimulation.Atsuchahighsetting,forthepower
|     |     |     |     |     |     |     | placement | of the | energy-storage | solution. | It  | could be added |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------------- | --------- | --- | -------------- |
waveform in Figure 1, we note a total energy overhead of at the server-level, rack-level, row-level, or colo/datacenter-
10.5% due to the power smoothing feature. level. The higher up in the hierarchy we add the energy
Challenges. Similar to the software solution, the addi- storage,moredeviceslikeUPSesandPDUsbecomeexposed
tional energy burned with the GPU power smoothing is the to the power and voltage perturbations. Although a higher
maindownsideofthissolution.TheGB200solutionincludes hierarchy level can theoretically offer more power demand
a built-in lifetime counter because its durability is limited. multiplexing from the servers, since we are concerned about
The actual lifetime depends on how frequently the feature is large synchronous training jobs that have identical power
used and the extra energy it consumes. While the expected demands across all participating servers, this is not a factor
lifespan is reasonable compared to the typical 5-year GPU thataffectsus.Amoredistributedenergy-storagealsoallows
lifetime, real usage in training jobs over the coming years foramorerelaxedreliabilitymetric,sincethefailuredomain
will provide a more accurate picture of its endurance. Fur- ofarack-levelshouldnothaveabigeffectonthedatacenter-
thermore, since the current solution in GB200 only allows wide power waveform. Furthermore, the AC-DC converters
a maximum MPF of 90% of TDP, and a minimum EDP of are present at the rack-level already, making that an optimal
1.1× of TDP, we are left with at least 20% of the TDP as place for a DC block energy storage. Therefore, a rack-level
the dynamic range (Section III-A) of the power fluctuations energy storage emerges as the best option.

Rack-Level Energy Storage Power Draw Time Series (Normalized)
1.0
Original Rack Power Draw (W)
| 0.9 |     |     |     |     |     |     |     |     |     |     |     | Moving Average Power Draw (W) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- |
Updated Rack Power Draw (W)
| 0.8 |     |     |     |     |     |     |     |     |     |     |     | Rack-Level Energy Storage Charge |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- |
Rack-Level Energy Storage Discharge
warD rewoP dezilamroN 0.7
0.6
0.5
0.4
0.3
0.2
0.1
0.0
Charge Over Time (Normalized)
Charge (%)
54
)%( egrahC
52
50
|     | 0   |     |     | 50  |     | 100 |     | 150 |     |     | 200 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time (s)
|     |     |     |     | Fig.7. | Energy-storagesolutionsimulatedonthepowerwaveformfromFigure1. |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Solution Reliability Performance Energy Cost Ability to meet Dependency on the Lifetime
|     |     |     |     |     |     |     |     |     | tightest | spec |     | developer |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | --------- | --- | --- | --- |
Software-only mitigation Medium Medium High Medium High High High
GPU power smoothing High Medium High Low Medium Medium Medium
| Rack-level |     | energy storage |     | High |     | High | Low | High |     | High |     | Low |     |     | High |
| ---------- | --- | -------------- | --- | ---- | --- | ---- | --- | ---- | --- | ---- | --- | --- | --- | --- | ---- |
TABLEI
SUMMARYOFVARIOUSPROPOSEDSOLUTIONS.FORENERGY,COST,ANDDEPENDENCYONTHEDEVELOPER,LOWERISBETTER.
Challenges.Giventherangeoffrequenciesthatneedtobe storage solution requires additional hardware deployment,
handled,oneofthemainchallengesthatemergesisanenergy leading to higher cost and embodied carbon in lieu of lower
storagesolutionthatcanmeetdemandsacrossthisspectrum. training energy. Using energy storage alone would require
Higher frequencies are easier to filter out, compared to the high capacitance to meet the ramp-up and ramp-down phase
| lower | frequencies. |             | Additionally, | ramp-up |           | and        | ramp-down  | specs. |     |     |     |     |     |     |     |
| ----- | ------------ | ----------- | ------------- | ------- | --------- | ---------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| can   | require      | very large  | capacitance   |         | from      | the energy | storage.   |        |     |     |     |     |     |     |     |
| Such  | large        | capacitance | would         | be very | expensive |            | from cost, |        |     |     |     |     |     |     |     |
rack-level space, and embodied carbon perspectives. Given Therefore, we propose a combination of the solutions:
|          |              |           |         |                 |     |          |             | GPU level | power | smoothing  | using  | software/hardware |     |           | so- |
| -------- | ------------ | --------- | ------- | --------------- | --- | -------- | ----------- | --------- | ----- | ---------- | ------ | ----------------- | --- | --------- | --- |
| that     | these events | happen    | rarely, | compared        |     | to the   | rest of the |           |       |            |        |                   |     |           |     |
|          |              |           |         |                 |     |          |             | lutions,  | and a | rack-level | energy | storage.          | The | GPU-level |     |
| workload | run,         | designing |         | enough capacity |     | for this | does not    |           |       |            |        |                   |     |           |     |
necessarily pay off. solutioncanbeusedtomeettheramp-up,ramp-downspecs,
|     |     |     |     |     |     |     |     | and any | corner | case scenarios | where | the | energy | storage | runs |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------------- | ----- | --- | ------ | ------- | ---- |
D. Putting a solution together. out of capacity. Such a combination of solutions is optimal
|     |     |     |     |     |     |     |     | from wasted | energy, | cost, | and space | perspectives. |     | However, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----- | --------- | ------------- | --- | -------- | --- |
The three solutions we discussed have various pros and it does require a co-design of the solutions, such that the
| cons.      | We summarize |              | these    | in Table  | I.      |         |             |             |           |         |           |            |        |     |         |
| ---------- | ------------ | ------------ | -------- | --------- | ------- | ------- | ----------- | ----------- | --------- | ------- | --------- | ---------- | ------ | --- | ------- |
|            |              |              |          |           |         |         |             | rack-level  | energy    | storage | and the   | GPU        | should | be  | able to |
| The        | software     | and          | hardware | solutions | are     | readily | available   |             |           |         |           |            |        |     |         |
|            |              |              |          |           |         |         |             | communicate | regarding |         | the state | of charge. |        |     |         |
| with       | the latest   | hardware,    |          | and both  | have    | similar | energy      |             |           |         |           |            |        |     |         |
| overheads. |              | The hardware |          | solution  | is much | more    | reliable at |             |           |         |           |            |        |     |         |
scale today, and does not lead to resource overheads unlike ForevenlargerAItrainingdeploymentsinthefuture,long
the software-solution. However, in regions where utilities storage BESS (battery energy storage system) should also
enforce stricter time-domain specifications (e.g., dynamic be considered. In general a combined approach of solutions
rangepower),hardwarealonemaynotbesufficientduetothe closer to the rack (the mitigation strategies we discussed in
90% limit on MPF; in such cases, a Firefly-like solution can detail), supplemented with battery storage systems at larger
beusedincombinationtomeettherequirements.Theenergy scale would help alleviate the power swing challenges.

E. Fast telemetry-based backstop venues such as the Open Compute Project (OCP) and be-
|                     |           |             |     |            |          |          |           | yond—to | drive             | forward | shared | standards, | validation |     | frame- |
| ------------------- | --------- | ----------- | --- | ---------- | -------- | -------- | --------- | ------- | ----------------- | ------- | ------ | ---------- | ---------- | --- | ------ |
| While               | proactive | smoothing   |     | strategies | can      | mitigate | most      |         |                   |         |        |            |            |     |        |
|                     |           |             |     |            |          |          |           | works,  | and architectural |         | best   | practices. | Together,  |     | we can |
| power fluctuations, |           | large-scale |     | AI         | training | jobs     | can still |         |                   |         |        |            |            |     |        |
occasionally excite critical sub-synchronous frequencies. To design for a future where AI training is not only powerful,
|                   |         |             |                      |              |          |          |       | but also | power-aware. |     |     |     |     |     |     |
| ----------------- | ------- | ----------- | -------------------- | ------------ | -------- | -------- | ----- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
| safeguard         | against | this, a     | fast telemetry-based |              |          | backstop | sys-  |          |              |     |     |     |     |     |     |
| tem is necessary. |         | This system |                      | continuously | monitors |          | power |          |              |     |     |     |     |     |     |
waveforms across the datacenter, looking for early signs of REFERENCES
| instability | or resonance |     | that may | not | be addressed |     | in time |     |     |     |     |     |     |     |     |
| ----------- | ------------ | --- | -------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
by primary mitigation techniques. [1] Iec 61000-3-3:2013 — electromagnetic compatibility (emc), 2013.
Standardforvoltageflickerandpowerswinglimitations.
Byleveragingfine-grained,low-latencytelemetryandreal-
|     |     |     |     |     |     |     |     | [2] Tom | B. Brown, | Benjamin | Mann, | Nick | Ryder, | Melanie | Subbiah, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | ----- | ---- | ------ | ------- | -------- |
timespectralanalysis(e.g.,FFTbinmonitoring),thesystem
JaredKaplan,PrafullaDhariwal,ArvindNeelakantan,PranavShyam,
GirishSastry,AmandaAskell,SandhiniAgarwal,ArielHerbert-Voss,
| can identify | the               | emergence | of      | problematic   | frequencies |       | and     |          |             |         |           |         |         |             |         |
| ------------ | ----------------- | --------- | ------- | ------------- | ----------- | ----- | ------- | -------- | ----------- | ------- | --------- | ------- | ------- | ----------- | ------- |
|              |                   |           |         |               |             |       |         | Gretchen | Krueger,    | Tom     | Henighan, | Rewon   | Child,  | Aditya      | Ramesh, |
| initiate     | tiered responses. |           | Initial | interventions |             | might | include |          |             |         |           |         |         |             |         |
|              |                   |           |         |               |             |       |         | Daniel   | M. Ziegler, | Jeffrey | Wu,       | Clemens | Winter, | Christopher | Hesse,  |
softthrottlingorloadshaping;ifineffective,moreaggressive
MarkChen,EricSigler,MateuszLitwin,ScottGray,BenjaminChess,
responses can follow—such as circuit-level power shedding JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,Ilya
Sutskever,andDarioAmodei.Languagemodelsarefew-shotlearners,
| or coordinated |     | disconnects—executed |     |     | in collaboration |     | with |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------------- | --- | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2020.
site-specific infrastructure logic. [3] Aakanksha Chowdhery, Sharan Narang, ..., Jason Wei, and [and
|     |     |                 |     |     |     |     |     | manyothers]...Petrafikowski. |     |      |          | Palm:Scalinglanguagemodelingwith |     |              |       |
| --- | --- | --------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | ---- | -------- | -------------------------------- | --- | ------------ | ----- |
|     |     | V. CALLTOACTION |     |     |     |     |     |                              |     |      |          |                                  |     |              |       |
|     |     |                 |     |     |     |     |     | pathways.                    | In  | JMLR | Workshop | and Conference                   |     | Proceedings, | 2023. |
540-billion-parametermodel.
| As the | scale | and complexity |     | of  | AI training | workloads |     |             |          |          |           |     |           |       |            |
| ------ | ----- | -------------- | --- | --- | ----------- | --------- | --- | ----------- | -------- | -------- | --------- | --- | --------- | ----- | ---------- |
|        |       |                |     |     |             |           |     | [4] General | Electric | Company. | Torsional |     | dynamics: | Large | 2-pole and |
continue to grow, power variability and grid impact will 4-pole steam turbine powertrains. Technical report (ger-4724), GE
onlybecomemoresevere.Addressingthischallengerequires Power & Water, 2013. Based on EPRI 1011679, Electric Power
ResearchInstitute,2005.
proactivecollaborationacrosssoftware,hardware,infrastruc-
|     |     |     |     |     |     |     |     | [5] DeepSeek-AI, |     | Aixin | Liu, Bei | Feng, Bing | Xue, | ..., and many | others. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | -------- | ---------- | ---- | ------------- | ------- |
ture, and utility domains. We outline three critical calls to Deepseek-v3technicalreport.Technicalreport,DeepSeek-AI/CoRR,
action: December 2024. Mixture-of-Experts language model with 671B
parameters(37Bactivatedpertoken).
| 1. AI        | Framework | and         | System | Designers: |            | Explore | less |              |         |           |            |                       |     |             |         |
| ------------ | --------- | ----------- | ------ | ---------- | ---------- | ------- | ---- | ------------ | ------- | --------- | ---------- | --------------------- | --- | ----------- | ------- |
|              |           |             |        |            |            |         |      | [6] Electric | Power   | Research  | Institute. | Torsional             |     | interaction | between |
| synchronous, | more      | power-aware |        | training   | algorithms |         | that |              |         |           |            |                       |     |             |         |
|              |           |             |        |            |            |         |      | electrical   | network | phenomena |            | and turbine-generator |     | shafts:     | Plant   |
reducelarge-scalepowerswingswithoutcompromisingcon- vulnerability. TechnicalReport1013460,EPRI,PaloAlto,CA,2006.
|           |      |          |              |     |          |             |     | [7] Alex | Krizhevsky, | Ilya | Sutskever, | and Geoffrey |     | E. Hinton. | Imagenet |
| --------- | ---- | -------- | ------------ | --- | -------- | ----------- | --- | -------- | ----------- | ---- | ---------- | ------------ | --- | ---------- | -------- |
| vergence. | This | includes | asynchronous |     | training | techniques, |     |          |             |      |            |              |     |            |          |
classificationwithdeepconvolutionalneuralnetworks.InAdvancesin
| staggered | scheduling, | and | overlap | of  | compute | and | commu- |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------- | --- | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
NeuralInformationProcessingSystems25,pages1097–1105.Curran
| nication. |     |     |     |     |     |     |     | Associates,Inc.,2012. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
2. Utility Providers and Grid Operators: Share resonance [8] Xiangru Lian, Wei Zhang, Ce Zhang, and Ji Liu. Asynchronous
and ramp specifications openly and establish standardized decentralized parallel stochastic gradient descent. In Jennifer G. Dy
|     |     |     |     |     |     |     |     | and | Andreas | Krause, | editors, | Proceedings | of the | 35th International |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------- | ----------- | ------ | ------------------ | --- |
communication pathways with datacenter operators. This ConferenceonMachineLearning(ICML),volume80ofProceedings
coordination is essential to ensure safe grid operation and ofMachineLearningResearch,pages3049–3058.PMLR,2018.
|                 |     |                |              |         |              |             |     | [9] Meta              | Engineering. | How | meta                 | keeps its | ai hardware | reliable. | Engi-    |
| --------------- | --- | -------------- | ------------ | ------- | ------------ | ----------- | --- | --------------------- | ------------ | --- | -------------------- | --------- | ----------- | --------- | -------- |
| avoid unplanned |     | outages        | or equipment |         | degradation. |             |     |                       |              |     |                      |           |             |           |          |
|                 |     |                |              |         |              |             |     | neeringblog,July2025. |              |     | Accessed:2025-08-06. |           |             |           |          |
| 3. Industry     |     | Collaboration: |              | Support | and          | participate | in  |                       |              |     |                      |           |             |           |          |
|                 |     |                |              |         |              |             |     | [10] Microsoft        | Azure        | AI  | Team. Phi-3:         | A highly  | capable     | small     | language |
pre-competitive, open forums—such as the Open Com- modellocallyonyourphone.Technicalreport,Microsoft,April2024.
IntroducedinMicrosoftAzureAIblog;technicalreportavailableon
| pute Project | (OCP)—to |     | establish | interoperable |     | standards | for |     |     |     |     |     |     |     |     |
| ------------ | -------- | --- | --------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arXiv.
| telemetry, | load | signaling, | and | sub-synchronous |     | oscillation |     |                                                                    |     |     |     |     |     |     |     |
| ---------- | ---- | ---------- | --- | --------------- | --- | ----------- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|            |      |            |     |                 |     |             |     | [11] NorthAmericanElectricReliabilityCorporation(NERC).Disturbance |     |     |     |     |     |     |     |
mitigation. It is extremely difficult for a single customer, monitoring and analysis of oscillatory events. https://www.
|         |                |     |            |              |     |               |     | nerc.com,2019. |             | [Online;accessed2025-08-06]. |             |              |            |            |           |
| ------- | -------------- | --- | ---------- | ------------ | --- | ------------- | --- | -------------- | ----------- | ---------------------------- | ----------- | ------------ | ---------- | ---------- | --------- |
| vendor, | or hyperscaler | to  | solve      | this problem |     | in isolation. |     |                |             |                              |             |              |            |            |           |
|         |                |     |            |              |     |               |     | [12] North     | American    | Electric                     | Reliability | Corporation  |            | (NERC).    | Intercon- |
|         |                |     |            |              |     |               |     | nection        | oscillation | analysis.                    | Reliability |              | assessment | technical  | report,   |
|         |                | VI. | CONCLUSION |              |     |               |     |                |             |                              |             |              |            |            |           |
|         |                |     |            |              |     |               |     | North          | American    | Electric                     | Reliability | Corporation, |            | July 2019. | Report    |
Power stabilization is emerging as a critical bottleneck in published July2019; includes analysis of inter-area oscillations, no-
|     |     |     |     |     |     |     |     | table | events | (e.g., Alberta | separation | 2000, | WECC | 2005, | EI 2016), |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | -------------- | ---------- | ----- | ---- | ----- | --------- |
thecontinuedscalingofAItrainingworkloads.Inthispaper,
andmodalcharacteristicsoftheEastern,Western,andERCOTinter-
| we detailed | the | impact | such | workloads | can | lead | to, and | connections. |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ---- | --------- | --- | ---- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
gave examples of the specifications needed for mitigation. [13] NVIDIA. NVIDIA GB200 NVL Multi-Node Tuning Guide — Power
We have presented a cross-stack approach that combines andThermals.NVIDIA,April2025.ProvidesGPUpowerandthermal
managementtuningfordatacentersystems.
software-based smoothing, GPU-level controls, and rack- [14] NVIDIA Corporation. Nvidia collective communications library
levelenergystorage,backedbyreal-worldmeasurementsand (nccl). https://developer.nvidia.com/nccl, 2025. Ac-
cessed:2025-08-06.
| simulation. | These   | techniques   | offer | practical      |     | and immediate |      |                                              |         |            |     |              |                 |     |      |
| ----------- | ------- | ------------ | ----- | -------------- | --- | ------------- | ---- | -------------------------------------------- | ------- | ---------- | --- | ------------ | --------------- | --- | ---- |
|             |         |              |       |                |     |               |      | [15] OpenAI.                                 | Scaling | kubernetes | to  | 7,500 nodes. | https://openai. |     |      |
| relief for  | today’s | deployments. |       |                |     |               |      |                                              |         |            |     |              |                 |     |      |
|             |         |              |       |                |     |               |      | com/index/scaling-kubernetes-to-7500-nodes/, |         |            |     |              |                 |     | Jan- |
| However,    | this    | work is      | just  | the beginning. |     | Ensuring      | that |                                              |         |            |     |              |                 |     |      |
uary2021.
|                   |     |         |      |            |     |           |      | [16] OpenAI. |           | Techniques |     | for                       | training | large | neu- |
| ----------------- | --- | ------- | ---- | ---------- | --- | --------- | ---- | ------------ | --------- | ---------- | --- | ------------------------- | -------- | ----- | ---- |
| AI infrastructure |     | remains | both | performant | and | grid-safe | will |              |           |            |     |                           |          |       |      |
|                   |     |         |      |            |     |           |      | ral          | networks. |            |     | https://openai.com/index/ |          |       |      |
requiresustainedcollaborationacrossresearch,industry,and
techniques-for-training-large-neural-networks/,
| utilities. | We urge | the community |     | to come | together—through |     |     | June2022. |     |     |     |     |     |     |     |
| ---------- | ------- | ------------- | --- | ------- | ---------------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |

| [17] Pratyush                                  | Patel, | Esha Choukse, | Chaojie | Zhang, | ´In˜igo Goiri, | Brijesh |
| ---------------------------------------------- | ------ | ------------- | ------- | ------ | -------------- | ------- |
| Warrier,NithishMahalingam,andRicardoBianchini. |        |               |         |        | Characterizing |         |
powermanagementopportunitiesforllmsinthecloud.InProceedings
| of the | 29th ACM | International | Conference | on  | Architectural | Support |
| ------ | -------- | ------------- | ---------- | --- | ------------- | ------- |
forProgrammingLanguagesandOperatingSystems(ASPLOS),vol-
| ume 3, | pages | 207–222, La | Jolla, CA, | USA, | 2024. Association | for |
| ------ | ----- | ----------- | ---------- | ---- | ----------------- | --- |
ComputingMachinery.
[18] KonstantinF.Pilz,JamesSanders,RobiRahman,andLennartHeim.
Trendsinaisupercomputers,2025.
| [19] Mohammad | Shoeybi,  | Mostofa           | Patwary,   | Raul              | Puri, Patrick | LeGres-      |
| ------------- | --------- | ----------------- | ---------- | ----------------- | ------------- | ------------ |
| ley, Jared    | Casper,   | and Bryan         | Catanzaro. |                   | Megatron-lm:  | Training     |
| multi-billion | parameter | language          | models     | using             | model         | parallelism. |
| arXiv         | preprint  | arXiv:1909.08053, | 2019.      | http://arxiv.org/ |               |              |
abs/1909.08053.
| [20] Super  | Micro                                   | Computer,  | Inc. Inside | the       | 100k gpu       | xai colos- |
| ----------- | --------------------------------------- | ---------- | ----------- | --------- | -------------- | ---------- |
| sus cluster | that                                    | supermicro | helped      | build     | for elon musk. | Case       |
| study       | / success                               | story,     | Super Micro | Computer, | Inc.,          | Decem-     |
| ber 2024.   | https://www.supermicro.com/CaseStudies/ |            |             |           |                |            |
Success_Story_xAI_Colossus_Cluster.pdf.
| [21] Hugo | Touvron,      | Thibaut Lavril, | ..., and | Guillaume | Lample. | Llama:   |
| --------- | ------------- | --------------- | -------- | --------- | ------- | -------- |
| Open      | and efficient | foundation      | language | models.   | arXiv   | preprint |
arXiv:2302.13971,2023.
| [22] L.Wang.                               | Reviewofemergingssr/ssoissuesandtheirclassifications. |            |                       |           |                    |     |
| ------------------------------------------ | ----------------------------------------------------- | ---------- | --------------------- | --------- | ------------------ | --- |
| JournalofOperationalEngineering(JOE),2017. |                                                       |            |                       |           | Online.            |     |
| [23] xAI. Open                             | release                                               | of grok-1: | A 314b                | parameter | mixture-of-experts |     |
| model.                                     | Webpage,2024.                                         |            | ReleasedMarch17,2024. |           |                    |     |