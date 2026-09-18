arXiv is now an independent nonprofit! Learn more (https://info.arxiv.org/about)  ×
Why HTML?
(https://info.arx
iv.org/about/ac
|              | RReeppoorrtt | BBaacckk  ttoo   | DDoowwnnllooaadd |
| ------------ | ------------ | ---------------- | ---------------- |
| cessible_HTM | IIssssuuee   | AAbbssttrraacctt | PPDDFF           |
L.html)
License: CC BY 4.0 (https://info.arxiv.org/help/license/index.html#licenses-available)
arXiv:2603.00415v1 [eess.SY] 28 Feb 2026

Grid Integration of AI Data Centers: A
Critical Review of Energy Storage Solutions
†
Sina Mohammadi Wayne Wang
Marcus Chen I Wada Rouzbeh Haghighi
Ali Hassan
Hualong Liu, Archit Bhatnagar, Ang Chen, Wencong Su
Abstract
Artificial intelligence (AI) is driving a rapid expansion of data centers (DCs). These
facilities consume large amounts of electricity and introduce new challenges for
power systems. AI workloads cause rapid power changes and high peak demand.
These behaviors are different from traditional data centers (TDCs) and can affect
grid stability and reliability. This paper reviews how energy storage systems
(ESSs) can help integrate AI data DCs with the electric grid. We examine storage
solutions at multiple levels, including grid-scale batteries, UPS systems, rack-
level storage, and chip-level buffering. Each layer operates at a different time
scale and serves a different purpose. Grid-interactive UPS (GiUPS) systems can
respond quickly to disturbances and assist with frequency regulation or voltage
ride through. Large battery energy storage systems (BESSs) can smooth power
demand, support renewable on-site generation, and provide grid services. Rack-
level and server-level storage help manage fast power fluctuations close to com-
puting hardware. We also discuss other technologies such as fuel cells (FCs) and
thermal energy storage (TE) that can support co-generation and reduce emis-
sions. In addition, second-life battery energy storage (SLBESS) are reviewed as
a lower-cost option for large installations whether supporting UPS battery or as a
backup generation. The paper compares the benefits, challenges, and coordina-
tion requirements of these solutions. Overall, the study provides a structured view
of how energy storage can improve reliability, flexibility, and sustainability when
connecting future AI data centers to the power grid.
Index Terms: : AI data center, battery backup unit (BBU), battery energy storage
systems (BESS), fuel cell (FC), GPU, second-life battery energy storage systems
(SLBESS), thermal energy storage (TES), UPS

Abbreviations
AI Artificial Intelligence 
AWS Amazon Web Services
BBU Battery Backup Unit
BESS Battery Energy Storage System
BMS Battery Management System
BTM Behind-the-Meter
CapEx Capital expenditures
CPU Central Processing Unit
DC Data Center
DMA Direct Memory Access
DoD Depth of Discharge
DVFS Dynamic Voltage and Frequency Scaling

 

| EMS    | Energy Management System                      |    |
| ------ | --------------------------------------------- | --- |
| ESS    | Energy Storage System                         |     |
| EV     | Electric Vehicle                              |     |
| FC     | Fuel Cell                                     |     |
| FFR    | Fast Frequency Response                       |     |
| FTM    | Front-the-Meter                               |     |
| GFL    | Grid-Following                                |     |
| GFM    | Grid-Forming                                  |     |
| GiUPS  | Grid-interactive Uninterruptible Power Supply |     |
| GPU    | Graphics Processing Unit                      |     |
| HBM    | High Bandwidth Memory                         |     |
| HDD    | Hard Disk Drive                               |     |
| HPC    | High Performance Computing                    |     |
| HVRT   | High Voltage Ride Through                     |     |
| IEC    | International Electrotechnical Commission     |     |
| LFP    | Lithium Iron Phosphate                        |     |
| LLM    | Large Language Model                          |     |
| LV     | Low Voltage                                   |     |
| LDESSs | Long Duration Energy Storage Systems          |     |
| LVRT   | Low Voltage Ride Through                      |     |
| MV     | Medium Voltage                                |     |
| MVDC   | Medium Voltage Direct Current                 |     |
| OCP    | Open Compute Project                          |     |
| ORV3   | Open Rack V3                                  |     |
| PCC    | Point of Common Coupling                      |     |
| PDU    | Power Distribution Unit                       |     |
| PEMFCs | Polymer Electrolyte Membrane Fuel Cells       |     |
| PLL    | Phase Locked Loop                             |     |
| PPA    | Power Purchase Agreement                      |     |
| PSA    | Power Sharing Unit                            |     |
| RDMA   | Remote Direct Memory Access                   |     |
| RES    | Renewable Energy Sources                      |     |
| SLB    | Second Life Battery                           |     |
| SLBESS | Second-Life Energy Storage System             |     |
| SoC    | State of Charge                               |     |
| SOFCs  | Solid Oxide Fuel Cells                        |     |

SoH State of Health
SSD Solid State Disk
SST Solid State Transformer
TDCs Traditional Data Centers
TPU Tensor Processing Unit
TUPS Traditional UPS
VRT Voltage Ride Through

 
I Introduction
Artificial Intelligence (AI) has fundamentally altered society’s relationship with
technology; spanning applications from simple search tasks to advanced scien-
tific discovery. Large language models (LLMs) have been at the forefront of
these high-complexity AI systems, with models such as ChatGPT and Claude,
increasingly embedded in everyday use across the United States. These large-
scale models are trained on trillions of text tokens collected from online sources
and are deployed through web-based platforms that can attract millions over
short periods of time. The surge in demand has prompted AI industry stake-
holders to consider contemporary data center (DC) designs capable of support-
ing the high-computational tasks required for training, inference, and fine-tuning
of increasingly more complex models. Energy requirements for AI queries are
now nearly an order of magnitude greater than those of Google search, while AI
training workloads have been observed to double approximately every 3.4
months [1]. Collectively, these trends highlight the necessity for rethinking data
center architectures to sustainably support the rapid scaling of AI workloads.

 
DCs are dedicated facilities, or collections of facilities, designed to house com-
putational systems, telecommunications equipment, and data storage infra-
structure. Energy demand within a DC is unevenly distributed: IT equipment
and cooling systems account for the majority of electricity consumption, while
auxiliary loads such as lighting and security represent a comparatively small
fraction [2]. Traditional data centers (TDCs) have historically operated at total
power levels typically below 30 MW [2], with individual electrical distribution
branches commonly limited to a few tens of kilowatts. These facilities are pre-
dominantly connected to power distribution networks in densely populated ar-
eas and operate under an architectural paradigm that emphasizes redundancy
and exceptionally high uptime, making uninterrupted power delivery from the

utility grid essential. TDCs are often sited near population centers to minimize
latency for end users.
In contrast, AI DCs are driven by compute-intensive workloads, the widespread
deployment of power-hungry GPUs, and the use of high-efficiency cooling tech-
nologies, all of which significantly increase power requirements. Thus, large-
scale AI training facilities are increasingly located in remote or semi-rural re-
gions where land, power, and cooling resources are more accessible and cost-
effective. Rack-level power demand in AI DCs can exceed 100 kW, while ag-
gregate facility consumption may scale to hundreds of megawatts or even gi-
gawatt levels [3]. As a result, large-scale AI training facilities often require direct
interconnection with transmission networks and face more strict reliability, sit-
ing, and environmental constraints than traditional facilities [4]. Inference-ori-

ented facilities, while potentially smaller in individual footprint, may connect at
either distribution or transmission level depending on aggregate scale and
siting.

 
Beyond the differences in scale and infrastructure, AI DCs exhibit two distinct
load profiles (training and inference) that differ fundamentally from those of
TDCs. AI training workloads are characterized by rapid power fluctuations aris-
ing from idle periods, peak utilization events, and checkpointing operations,

with significant load variations occurring on sub-second timescales. In addition,
training jobs often produce high-frequency, jitter-like power spikes. In contrast,
inference workloads generally lack such rapid transients and exhibit compara-
tively smoother demand profiles. TDC loads, by comparison, behave more like
conventional grid loads and are typically predictable using historical data and
standard forecasting methods.
AI DCs are connected to the power grid through high-density power converters,
which lead to higher power distortion at the utility level. Besides, jittery spikes in
training jobs may cause sub-frequency mechanical oscillations in synchronous

generators, which increase mechanical stress and accelerate corrosion. As a
 
result, harmonic compensation and load smoothing become a critical require-
ment for AI DC operation, both to improve load predictability and to mitigate ad-
verse power-quality impacts on the power system.

 
Large-scale AI DCs enforce the power grid to accommodate higher reserve
margins and proactive resource planning. This is because forecasting their load
dynamics is more challenging than for traditional loads, and the uncertainty as-
sociated with these types of loads is significantly higher. Therefore, additional
reserve capacity is necessary to maintain normal grid operation and to support
grid expansion when integrating AI DCs.

 
Connecting or disconnecting large-scale AI DCs may jeopardize system stabil-
ity due to high-range frequency fluctuations. These facilities are designed to
rapidly transfer to backup power in response to even minor grid disturbances,
which can trigger large, sudden load drops at the transmission level. Such dis-
turbances may activate load-frequency relays or enforce grid operators to im-
plement load-shedding scenarios. A recent transmission fault in Virginia trig-
gered an abrupt 1,500 MW reduction in system load as multiple DCs transi-
tioned to backup power, leading to significant frequency and voltage deviations
that required operator intervention [5]. Events such as this illustrate the limita-
tions of conventional grid planning and operational strategies when accommo-
dating large AI DC loads.

 

Considering the above-mentioned challenges, we investigate on the role and
impact of energy storage systems (ESSs) in enabling the smooth integration of
future large-scale AI DCs into the power system. To the best of our knowledge,
there is no comprehensive document specifically focusing on the potential sup-
port roles of ESSs in the reliable integration of AI DCs with the power grid. In
this paper, we address this gap and investigate the role of ESS in AI DCs.
ESSs can act not only as backup units with limited uptime but also support
cooling through thermal storage units. They can be deployed as battery backup
units (BBUs) inside IT racks, GPU-level batteries for chip-level load smoothing,
and battery energy storage systems (BESSs) for DC-level load smoothing or
co-generation support. ESSs within UPS systems can also interact with the util-
ity grid to provide services such as frequency regulation and peak shaving.
Fuel cells (FCs) are also have the potential to replace diesel back-up genera-
tion with technology advancements.

 
In contrast to [6, 7], this paper is highly focused on the role of ESSs in enabling
reliable grid integration of AI DCs, rather than only characterizing the grid im-
pacts of these large loads. Moreover, our work does not focus on ESS chem-
istry technologies [8, 9], but instead attempts to reveal design architectures for
the optimal application of ESSs in AI DCs grid integration. Therefore, this study
serves as an appropriate source for both academic and industry partners seek-
ing the required knowledge to explore new avenues for the role of ESSs in fu-
ture AI DCs.

 
The remainder of the paper is organized as follows. Section II provides an over-
view of the AI DC architecture, where IT equipment, power delivery systems,
cooling systems, and miscellaneous units are examined, along with the re-
quired upgrades compared to TDCs. Section III investigates the role and opera-
tion of UPS systems, with particular emphasis on the grid-interactive UPS
(GiUPS) systems, which has recently been studied as a key component of fu-
ture AI DCs. Section IV discusses the integration of BESSs with AI DCs and
their role in power smoothing and reliable grid integration, with a special focus
on large-scale units. Sections V and VI address FCs and thermal energy stor-
age (TES) systems, respectively, as non-battery-based energy storage solu-
tions, highlighting their contributions to low-carbon on-site generation and more
efficient cooling systems while maximizing the utilization of renewable energy
sources (RESs). The role of rack-level and server-level ESSs is also examined

as primary components for mitigating chip- and server-level power fluctuations,
and their coordination requirements are emphasized in section VII. Section VIII
investigates the role of second-life BESSs (SLBESSs) as cost-effective ESSs
within the AI-DC architecture, and presents evidence demonstrating their capa-
bility to support centralized BESSs in AI DCs. Finally, Section X discusses the
challenges associated with integrating multi-layer ESSs and outlines potential
future research directions.
II AI DC Power Architecture
The AI DC infrastructure comprises different sections, including IT equipment,
power distribution networks, cooling systems, and miscellaneous units such as
lighting and security. In this section, we provide a brief introduction to the AI DC
components and the ESS units in its structure. The overall structure of the AI
DC with all ESSs is provided in Fig. I.

 
II-A IT equipment
The IT equipment itself comprises high-performance computational electronic
 
chips such as GPUs, TPUs, and CPUs. It also includes advanced storage ar-
chitectures, such as solid-state storage units, for storing required information
with very high speed and efficiency. In addition, it considers resilient and secure
networking among all processing units in AI DCs. High-speed, low-latency com-
munication among AI accelerators is primarily achieved through Remote Direct
Memory Access (RDMA) fabrics allowing direct memory-to-memory data trans-
fers between nodes without CPU involvement. Dominant implementations in-
clude RoCEv2/InfiniBand across racks in training clusters [10] and direct GPU-
to-GPU communication within racks via NVLink [11].

 
II-A1 Computing Units
The computing unit consumes half of the required electricity of an AI DC [12].
NVIDIA GPUs such as H100, B200, or Blackwell Ultra have been used for train-
ing jobs in hyperscale AI DCs. For instance, the B200 utilizes 208 billion tran-
sistors that can be parallelized through very fast communication settings such
as NVLink [13]. In addition, new GPU designs such as the GB300 NVL72 en-

able chip-level power smoothing using ESS [14]. Beyond NVIDIA, major cloud
providers have developed custom AI accelerators optimized for their infrastruc-
ture: Google’s Tensor Processing Units (TPUs) [15] are used to train and serve
models such as Gemini, while AWS Trainium and Inferentia chips provide train-
ing and inference acceleration, respectively, enabling cloud-scale AI services.
AMD has also entered the AI accelerator market with its Instinct GPU series
(e.g., MI300X), which offers competitive performance-per-watt for LLM training
and inference workloads. These GPUs integrate CPU and GPU compute with
high-bandwidth memory (HBM) in a unified package, positioning it as a direct

competitor in hyperscale AI DCs. In section VII, the role of ESSs for power
 
smoothing will be discussed in more detail.

 
II-A2 Data Storage Units
AI training workloads place extreme demands on storage infrastructure, requir-
ing high-throughput, low-latency access to datasets that can reach petabyte
scale. NVMe SSDs have become the dominant storage medium in modern AI
DCs, replacing both HDDs and legacy SATA SSDs due to their superior band-
width and latency characteristics. HDDs, while still present in archival or cold-
storage tiers of some traditional facilities, are largely absent from the hot data
path in AI training environments, where even brief I/O stalls can idle expensive
GPU clusters [16].

 
The prevailing architectural trend in hyperscale AI DCs is disaggregated stor-
age, in which compute (GPU servers) and storage are decoupled into indepen-
dent resource pools interconnected via high-speed RDMA fabrics. Unlike tradi-
tional server-attached storage, disaggregation allows compute and storage ca-
pacity to scale independently, improves overall resource utilization, and enables
storage to be shared across multiple training jobs simultaneously [10]. In prac-
tice, GPU servers access remote NVMe devices over RDMA-capable networks
using protocols such as NVMe over Fabrics (NVMe-oF), achieving latencies
that approach those of locally-attached storage. NVIDIA’s GPUDirect Storage
extends this further by enabling direct DMA transfers between NVMe storage

devices and GPU memory, bypassing the CPU and host memory entirely and
reducing both latency and CPU overhead for I/O-bound training workloads [17].
II-A3 Networking
AI DCs aggregate thousands of GPU accelerators into tightly coupled parallel
training clusters, placing extraordinary demands on the underlying network fab-
ric. Unlike TDCs, where network traffic patterns are largely client-server in na-
ture, AI training workloads generate dense all-to-all communication patterns
during gradient synchronization across distributed model replicas. This requires
network fabrics that deliver high bandwidth, ultra-low latency, and minimal con-
gestion at scale [10].

 
The foundational transport mechanism in modern AI DC networks is RDMA,

 
which enables direct memory-to-memory transfers between nodes without CPU
involvement, reducing both latency and CPU overhead. While InfiniBand has
historically been used in HPC settings and remains present in some training
clusters, the industry has broadly converged on RoCEv2 (RDMA over
Converged Ethernet) [18] as the fabric of choice at hyperscale, offering compa-
rable performance over commodity Ethernet switching infrastructure at lower
cost and with greater operational flexibility [10, 19]. NVIDIA’s Spectrum-X plat-
form is specifically engineered to optimize RoCEv2 performance for AI work-
loads, addressing congestion control and load balancing challenges that arise
in large-scale training deployments [19].

 
Within a single node or rack, inter-GPU communication bypasses the network
fabric entirely through NVIDIA NVLink, a high-bandwidth direct interconnect that
enables GPU-to-GPU data transfers at bandwidths far exceeding those achiev-
able over any network interface [11]. Beyond a single rack, scale-out communi-
cation relies on the RDMA fabric described above.

 
II-B Power Delivery Systems
The power delivery systems in an AI DC contain the external utility grid, internal
power distribution, UPS, on-site backup generation, and the associated control

systems. 
II-B1 External Utility Grid

TDCs, with power consumption on the order of a few megawatts, can typically
be directly connected to distribution grids at voltage levels such as 34.5 kV or
13.2 kV. However, hyperscale AI DCs, requiring more than 100 MW of power,
should be connected to transmission grids to ensure reliable and stable grid op-
eration [2]. However, there is no standardized voltage level across utilities for
integrating large loads such as AI DCs. The utility power is then transformed to
a lower voltage level through a medium-voltage to low-voltage distribution
transformer, typically 480 V, to feed the internal power distribution within the
DC. This transformer also electrically isolates the AI DC from the grid. The 480
V AC is then distributed among the various components of the AI DC, including
the UPS system, power distribution units (PDUs), cooling system, and IT
equipment.

 
II-B2 UPS system
The UPS system is comprised of an AC-to-DC power converter, a battery stor-
age unit, and a DC-to-AC power converter. Power is stored in the storage unit
under normal conditions, and the stored energy is used during emergency con-
ditions when there is a loss of utility power or rapid fluctuations that jeopardize
the normal operation of IT loads. In TDCs, UPS operation is typically limited to
a few seconds, after which on-site generation units take responsibility for pow-
ering the DC in the absence of utility power for several hours.

 
The UPS requirements for AI DCs differ significantly from those of TDCs. The
UPS system for AI DCs should operate over different ranges, including short-,
medium-, and long-duration operation. Medium- and long-duration operation
provides more time for on-site generation activation or, in some cases, can
eliminate the need for separate backup units. GiUPS systems with high power
density and large storage capacity can also be implemented to enable grid-sup-
port functions, including peak shaving or frequency regulation scenarios. The
UPS systems in modern AI DCs will be discussed in detail later in Section III.

 

II-B3 Backup On-Site Generation
Backup generation units are utilized in DCs to provide electrical power under
emergency conditions when utility power is unavailable. Backup generation is
activated a few seconds after a utility power interruption, following the UPS re-
sponse. Diesel backup generators are used in TDCs because they are combus-
tion-based units that can provide a fast response; however, they are not envi-
ronmentally friendly. RESs with appropriate BESSs can also be utilized for
backup generation, as discussed in more detail in Section IV. However, power
density, implementation cost, and the required space for installing PV panels or
wind turbines are challenging issues in this context [20]. Modular nuclear reac-
tors have also recently been introduced for AI DCs, offering MW-level power
generation [21]. The technology for this type of equipment is still immature, im-
plementation costs are high, and spent nuclear fuel must be stored properly. In
addition, FCs may be better options for backup generation, as they can provide
high power with fast response. Moreover, the development of hydrogen-based
FCs can enable clean generation units within AI DCs [22]. The role of FCs in
backup generation for future AI DCs will be discussed thoroughly in Section V.

 
II-C Cooling Systems
The IT equipment inside a DC produces heat as a result of electrical losses
within electronic chips. As the computational power and power density of com-
puting units increase, the associated losses and heat generation also increase.
In AI DCs, due to the presence of high-intensity AI accelerators, advanced cool-
ing systems are required to enhance IT load performance and optimize power
consumption. In TDCs, air is used as the primary medium for cooling IT equip-
ment. Chilled air is injected into server rooms, and the temperature is main-
tained at a certain level using a central cooling controller. Air-cooling systems
are cost-efficient, reliable, and agile. They can be easily extended to larger fa-
cilities, and the required hardware can be modified quickly. However, the effi-
ciency of air-cooling systems is low for effectively cooling power-hungry AI
accelerators.

 
Liquid cooling is a more advanced cooling system developed for AI DCs. By uti-
lizing liquid cooling systems, cooling can be provided at the rack level or even
at the chip level. Liquid cooling offers better heat transfer, requires less energy
and space, and is more efficient compared to air-cooling systems. It also elimi-

nates the need for large mechanical fans, which are less reliable. Direct-to-chip
cooling circulates a dielectric liquid through cold plates into chips and process-
ing units and can efficiently dissipate heat [23]. Hybrid cooling systems com-
bine the agility of air cooling with the efficiency of liquid cooling, making them a
suitable  option  for  hyperscale AI  DCs  where  redundancy  can  be  achieved
through hybrid solutions.

|    | TABLE I:Overview of GiUPS Operating Modes |     |     |     |    |
| --- | ----------------------------------------- | --- | --- | --- | --- |
Battery
| Mode | Grid Input |     | Trigger Condition | Key Feature |     |
| ---- | ---------- | --- | ----------------- | ----------- | --- |
Output
Standard double-
| Standard Operation | 100% | 0%  | Normal operation |     |     |
| ------------------ | ---- | --- | ---------------- | --- | --- |
conversion UPS
Discharge-Full
|     | 0%  | 100% | External command | Fully battery-powered load |     |
| --- | --- | ---- | ---------------- | -------------------------- | --- |
Disconnection
| Discharge-Partial |     | Partial (e.g., |     | Mixed grid and battery |     |
| ----------------- | --- | -------------- | --- | ---------------------- | --- |
<100%
External command
| Disconnection |          | 25%)    |                   | supply                   |     |
| ------------- | -------- | ------- | ----------------- | ------------------------ | --- |
|               | Supply > | Battery | SOC < 100%, over- | Power limited (20–25% of |     |
Recharge
|               | Load       | charging     | frequency           | UPS capacity)        |     |
| ------------- | ---------- | ------------ | ------------------- | -------------------- | --- |
|               |            | Discharge to |                     | Bi-directional power |     |
| Energy Export | Adjustable |              | Regulatory approval |                      |     |
|               |            | grid         |                     | conversion           |     |
TE units can also be utilized in parallel with different types of cooling systems [
24]. The TEs absorb chilled air or water and inject it into the IT equipment at
specific times. Utilizing TEs can effectively increase efficiency in AI DCs. TEs
cool the air or liquid by accessing extra energy from on-site generation units
during normal DC operation. The role of TEs as cooling system accelerators in
future AI DCs will be discussed thoroughly in Section VI.

|    |     |     |     |     |    |
| --- | --- | --- | --- | --- | --- |
II-D Miscellaneous Units
Apart from IT equipment, power delivery, and cooling systems, there are other
units required for the normal operation of AI DCs. These include the physical in-
frastructure for housing servers, racks, and wiring systems, as well as the light-
ing system within the AI DCs. In addition, security and control rooms are also

integral units of a AI DC. Miscellaneous units in an AI DC consume significantly
less electricity than the other sections.

 
Fig. 1:UPS and GiUPS operation modes
III UPS Systems in AI DCs
III-A Traditional UPS (TUPS) Operation and Limitations
UPS systems are fundamental components in AI DCs, ensuring continuous op-
eration of critical loads during grid disturbances or outages. Conventional UPS
systems [25, 26, 27] typically operate in standby or online modes. In standby
mode, the UPS remains bypassed during normal operation and transfers to bat-
tery-supported inverter operation only when a disturbance is detected. In online
mode, the rectifier and inverter continuously process power, providing isolation
from grid disturbances and maintaining tight voltage and frequency regulation
at the critical bus (see Fig. 1). In both modes, the UPS interacts with the grid
only through battery charging and synchronization. The UPS is therefore
treated as a passive protective device.

 
III-B GiUPS systems in AI DCs
TUPS architectures were designed primarily for load protection with minimal in-
teraction with the utility grid. This paradigm is increasingly insufficient for AI

DCs. First, AI workloads introduce rapid load variations that propagate up-
stream and cause voltage flicker, transformer thermal stress, and feeder
congestion [28]. These effects are amplified when multiple AI racks operate in
synchrony, which is common in distributed training. Second, the growing pene-
tration of renewable energy reduces system inertia and increases the rate of
change of frequency. TUPS systems do not contribute to frequency support be-
yond simple ride-through, which leaves a large amount of inverter capacity un-
used during normal operation [29]. Third, the energy stored in UPS batteries
remains idle for more than 99 percent of their lifetime, representing a significant
opportunity cost. These limitations motivate the development of UPS architec-
tures capable of dynamic grid interaction.
GiUPS systems enhance TUPS designs by incorporating bidirectional power

converters, advanced digital controllers, and communication interfaces that al-
low coordination with the utility grid or market operator. These systems can
modulate active power in response to grid frequency deviations or dispatch sig-
nals, enabling participation in services such as primary frequency regulation,
fast frequency response, synthetic inertia, and peak load management [30, 31,
32]. Unlike TUPS systems, which operate independently of grid conditions ex-
cept during outages, GiUPS systems continuously monitor grid conditions and
adjust their output accordingly.

 
GiUPS can provide fast frequency response (FFR) within 0.5 to 10 seconds af-
ter a grid event. It can operate in a dynamic frequency response mode. In this
mode, the injected battery power is adjusted in real time based on frequency
regulation needs. The UPS can also operate in a static frequency response
mode. In this case, a fixed amount of power is injected after a grid event such
as a fault or large load switching [33].

 
III-B1 Operational Modes of GiUPS
GiUPS can operate in several modes depending on the grid conditions and ex-
ternal control signals, including standard operation, discharge modes (full and
partial disconnection), recharge mode, and energy export (bi-directional)
mode [30, 34]. When a frequency variation is detected by an external controller,
the GiUPS adjusts its operation to provide both positive and negative regulation

by charging or discharging its batteries within operational limits. Table I, shows
an overview of GiUPS operation modes.
Under normal conditions, the GiUPS receives 100% of the input power from the
utility grid through the rectifier, delivering it to the load (see S1 in Fig. 1). In this
mode, the GiUPS functions as a standard double-conversion system, with the
batteries maintained in standby and not actively supplying power. This opera-
tion is referred to as the standard UPS operation. 
 

 
Discharge modes are employed to meet external control requests, supplying
energy to the load or the grid. In the full disconnection mode, the GiUPS is
completely disconnected from the utility, and 100% of the load power is sup-
plied by the batteries (see S2 in Fig. 1). In the partial disconnection mode, the
input power from the grid is reduced according to external commands, with the
remaining load power supplied by the batteries (see S3 in Fig. 1). For example,
the batteries may provide 25% of the total load power while the grid supplies
the remainder.

 
When the battery state of charge (SOC) is below 100% (e.g., 80%) and an
over-frequency event is detected, the GiUPS draws power from the grid to
recharge the batteries. This operation is referred to as recharge mode. The
maximum recharge power is typically limited to 20–25% of the GiUPS nominal
capacity, constrained by battery recharge characteristics and the maximum in-
put current.

 
The GiUPS can also operate as a bi-directional power converter to inject en-
ergy back into the grid (see S4 in Fig. 1). This energy export mode is subject to
local regulatory and grid requirements and allows the GiUPS to discharge bat-
teries upstream.

 

III-B2 GiUPS Reactive Power Support and
Voltage Ride-Through (VRT) Capability
In addition to active power modulation, advanced GiUPS systems can provide
reactive power injection and VRT capabilities, which are increasingly required
by modern grid codes and interconnection standards [35, 36]. Reactive power
support is enabled by the bidirectional inverter stage, which can independently
regulate active and reactive current components under a synchronous refer-
ence frame control strategy. GiUPS units typically provide reactive power capa-
bility in the range of 20–40% of their rated kVA. For example, a 1 MW/1.1 MVA
GiUPS can supply approximately ±250–300 kVAr of dynamic reactive support.
GiUPS can inject or absorb reactive power without significantly affecting active
power delivery to the critical load. This capability allows the DC to contribute to
feeder voltage regulation, mitigate voltage fluctuations caused by rapid AI load
variations (often inducing 5–10% voltage swings within milliseconds), and im-
prove local power factor at the point of common coupling (PCC) from typical
values of 0.92–0.95 to above 0.99 [37, 35].

 
VRT capability ensures that the GiUPS remains connected and operational dur-
ing short-duration voltage sags or swells [38]. TUPS systems typically transfer
to battery mode during severe disturbances, effectively isolating the load from
the grid. In contrast, GiUPS systems are designed to comply with low-voltage
ride-through (LVRT) and high-voltage ride-through (HVRT) requirements, simi-
lar to grid-scale inverter-based resources. Typical LVRT profiles require the in-
verter to remain connected down to 0.2 pu for 100–150 ms, and down to 0.5 pu
for up to 500 ms. During a voltage sag, the GiUPS can increase reactive cur-
rent injection proportionally to the voltage deviation, often delivering 2–3 pu re-
active current within 2–5 ms, thereby supporting grid voltage recovery while
maintaining uninterrupted supply to the critical load.

 
The coordination between active power support, reactive power regulation, and
VRT functionality requires a hierarchical control framework [39, 40, 41]. In grid-
following (GFL) mode, the GiUPS synchronizes to the grid using a phase-
locked loop (PLL) and provides reactive current according to predefined droop
characteristics (typically 3–5% voltage droop) or grid operator commands. In
grid-forming (GFM) mode, the inverter can regulate terminal voltage magnitude
and frequency directly, enabling seamless transition to islanded operation if grid
conditions deteriorate beyond acceptable thresholds. Protection logic ensures

that grid support functions never compromise critical load reliability, maintaining
load voltage within ±1–2% even during external disturbances.
III-B3 GiUPS Topologies
For GiUPS applications, topologies that support bidirectional power flow and
high-speed digital control are preferred. Double-conversion and delta conver-
sion architectures with bidirectional converters can rapidly transition between
load-following, grid-support, and islanded operation. Modular architectures are
particularly attractive in AI DCs because they allow some modules to participate
in grid services while others remain dedicated to critical load protection. This
 
partitioning reduces operational risk and improves economic performance [30].
Emerging DC-coupled architectures further reduce conversion stages and im-
prove round-trip efficiency. These architectures also enable direct coupling with
on-site renewable generation or FCs, which enhances the ability of the AI DCs
to operate as controllable grid resource.

 
III-C BESS Sizing in GiUPS Systems
The sizing of the BESS in GiUPS applications must simultaneously satisfy
backup reliability requirements and grid-service performance objectives [7, 8].
GiUPS participation in services such as FFR, primary regulation, and peak
shaving introduces additional sizing considerations. Frequency regulation is pri-
marily power-intensive rather than energy-intensive, requiring high ramp rates
and short-duration injections. Consequently, the inverter power rating may ap-
proach the full UPS capacity even if incremental energy capacity beyond
backup requirements remains moderate. Cycle life and cumulative energy
throughput are critical determinants of economic sizing. Grid-service participa-
tion may introduce hundreds of shallow cycles annually [42, 43, 44, 45].
Battery degradation correlates strongly with equivalent full cycles, temperature,
and average state of charge [46, 47, 48, 49]. Moderate oversizing of the BESS
can reduce effective depth of discharge (DOD) per cycle, extending service life
and lowering long-term replacement cost. However, excessive oversizing in-
creases capital expenditure, footprint, and thermal management complexity
without proportionate revenue gains.

 

An optimal sizing methodology therefore integrates (i) backup energy con-
straints, (ii) committed grid-service power capacity, and (iii) degradation-aware
lifecycle cost modeling. Optimization frameworks typically minimize total cost of
ownership while ensuring reliability margins and projected ancillary service rev-
enues. For AI DCs with highly dynamic loads, an additional allocation of BESS
capacity may be reserved for short-term load smoothing to mitigate upstream
ramp rates and transformer stress. This buffering function must be explicitly in-
cluded in sizing calculations to prevent erosion of guaranteed backup auton-
omy. This further highlights the role of long-duration ESSs (LDESSs) in modern
UPS systems, which are currently under investigation for grid use cases.

 
IV BESS in AI DCs
BESS integrated with DCs represent a practical and scalable solution to ad-
dress the challenges imposed by large and highly dynamic loads on the power
system [50]. When appropriately designed and controlled, BESS can play a
critical role in mitigating large load fluctuations, enhancing local power quality,
and supporting overall grid stability [12]. To establish a clear understanding of
the underlying mechanisms and achievable benefits, this section reviews the
fundamental BESS control paradigms, with emphasis on grid-forming and grid-
following modes of operation. The discussion then extends to key grid-support
functions enabled by AI DC–connected BESS, including co-generation, power
smoothing and frequency regulation. Finally, the cost and sizing implications of
BESS deployment are examined.

 
IV-A BESS Control Modes
From an operational perspective, AI DCs can be configured for grid-tied or is-
landed operation, depending on the BESS inverter control mode and the facil-
ity-level coordination architecture. GFM control enables the BESS to establish
the voltage and frequency reference required for islanded operation. In grid-tied
mode, the BESS can charge or discharge to support peak shaving and in-
crease renewable self-consumption, whereas in islanded mode it serves as the
anchor resource to supply the AI DCs and potentially reduce reliance on con-
ventional generation or support renewable co-generation [51, 52].

 

IV-A1 GFM Control Model
In grid-forming operation, the BESS behaves as a controlled voltage source
and establishes its own internal frequency and phase without relying on an ex-
ternal phase-locked loop (PLL) [53]. The controller emulates the swing dynam-
ics of a synchronous generator by incorporating virtual inertia, damping, and
active power–frequency droop characteristics.

 
The inverter angle dynamics are given by 
𝑑 𝛿
vsm
|     |     |     | = 𝜔 | ,   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     |     |     | vsm |     |     | (1) |
𝑑 𝑡
while the internal frequency dynamics are described by
|        | 𝑑 𝜔vsm |         | 1    | 𝑠 𝐷2       |     |     |
| ------ | ------ | ------- | ---- | ---------- | --- | --- |
| 2 𝐻vsm |        | =𝑃 −𝑃−( | +𝐷1+ | ) (𝜔vsm−𝜔0 | ).  |     |
|        |        | ref     |      |            |     | (2) |
|        | 𝑑 𝑡    |         | 𝑚𝑝   | 𝑠+𝜔𝐷       |     |     |

 
Here, 𝐻  is the virtual inertia constant, 𝑚  is the active power–frequency
| vsm |     |     |     | 𝑝   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
droop coefficient, 𝐷  represents steady-state damping, 𝐷
|     | 1   |     |     | 2  is a transient damp- |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- |
ing term shaped by a washout filter with corner frequency 𝜔 , 𝜔  is the in-
𝐷 vsm
verter angular frequency, 𝜔  is the nominal angular frequency, 𝑃
 is the active
|     |     | 0   |     |     | ref |     |
| --- | --- | --- | --- | --- | --- | --- |
power reference, and 𝑃 is the measured inverter output power. This formulation
enables autonomous frequency regulation and inertial response, making GFM
BESSs suitable for islanded operation [54].

 
IV-A2 GFL Control Model
In contrast, GFL BESS operate as controlled current sources that synchronize
to an externally imposed grid voltage using a PLL [55]. The inverter frequency
and phase are therefore dictated by the grid rather than internally generated.

 
A conventional synchronous-reference-frame PLL can be expressed as 
|     |     | 𝜔 = 𝜔 | +𝐾 𝑣 +𝐾 ∫𝑣 |  𝑑𝑡, |     |     |
| --- | --- | ----- | ---------- | ---- | --- | --- |
|     |     | pll 0 | 𝑝 𝑞        | 𝑖 𝑞  |     | (3) |

𝑑 𝛿 
pll
= 𝜔 , (4)
pll
𝑑 𝑡
where 𝑣 is the quadrature-axis component of the measured grid voltage in the
𝑞
PLL reference frame, 𝐾 and 𝐾 are the proportional and integral gains of the
𝑝 𝑖
PLL, and 𝛿 and 𝜔 denote the estimated grid angle and frequency,
pll pll
respectively.
Because GFL inverters depend on a strong external voltage reference, their
performance degrades under weak-grid conditions, motivating the adoption of
GFM control strategies in inverter-dominated systems [54].


 
 
The BESS terminal-voltage dynamics 𝐸 are modeled as 
𝑑 𝐸
𝑘 = 𝑉 +𝑚 (𝑄 −𝑄),
(5)
𝑖 𝑣 𝑑 𝑡 ref 𝑞 ref
where 𝑘 is the integral gain, 𝑉 is the voltage reference, 𝑚 is the 𝑄–𝑉 droop
𝑖 𝑣 ref 𝑞
coefficient, 𝑄 is the reactive power reference, and 𝑄 is the measured reactive
ref
power. This formulation regulates the inverter voltage magnitude through a re-
active-power droop relationship.

 

TABLE II:Summary of power-smoothing architectures for AI data centers: benefits and challenges [56]
| Architecture       | Benefits          |      | Challenges                 |     |
| ------------------ | ----------------- | ---- | -------------------------- | --- |
|                    | •                 |      | • Complex control strategy |     |
| Advanced GFM + GFL |                   | Load |                            |     |
| BESS Solution      | smoothing/shaping |      |                            |     |
|                    |                   |      | •  Fast  measurement       | and |
• Demand flexibility
communication
|     | • Grid services |     | •  Advanced  | plant-level |
| --- | --------------- | --- | ------------ | ----------- |
control
•
|     | Lower  | cost  and |     |     |
| --- | ------ | --------- | --- | --- |
footprint
|                    | •              |           | • Higher cost |     |
| ------------------ | -------------- | --------- | ------------- | --- |
| Hybrid E-STATCOM + | Load           | smoothing |               |     |
| BESS Solution      | and/or shaping |           |               |     |
• Increased footprint
• Demand flexibility
• Control interaction
• Grid services
• Lower flicker
|                   | •   |      | • May require a line reactor |     |
| ----------------- | --- | ---- | ---------------------------- | --- |
| Grid-Forming BESS |     | Load |                              |     |
smoothing/shaping
• Higher flicker
• Demand flexibility
• Plant-level control
•
|     |     | Support  grid |     |     |
| --- | --- | ------------- | --- | --- |
services/stability
|                           | •                 |            | •                |            |
| ------------------------- | ----------------- | ---------- | ---------------- | ---------- |
| Supercapacitors (e.g., E- |                   | High-speed | POI              | demand     |
| STATCOM)                  | response          |            | management       |            |
|                           | •                 |            | •                |            |
|                           | Effective         | load       | Not  supporting  | grid       |
|                           | smoothing/shaping |            | services         |            |
|                           | • Reduced flicker |            | •                |            |
|                           |                   |            | Does  not        | offer  GFM |
support

IV-B Grid Support Roles of BESS in AI DCs
IV-B1 On-Site Clean Power Integration
BESS play a critical role in enabling RESs integration at AI DCs. Given the en-
ergy-intensive nature of AI DCs, on-site renewable generation and off-site pro-
curement mechanisms such as power purchase agreements (PPAs) are in-
creasingly adopted to reduce operating costs and meet sustainability objec-
tives. However, the inherent intermittency of renewable resources complicates
reliable power supply. BESS mitigate these challenges by storing excess en-
ergy during periods of high generation and supplying it during low availability,
while also providing backup power, and improved renewable utilization [57]. AI
DC–integrated BESS can be architected either as large, multi-megawatt GFM
resources capable of replacing conventional backup generators, or as large-ca-
pacity batteries integrated within static UPS systems [58]. In this context,
GiUPS systems, traditionally designed for short-duration ride-through, are in-
creasingly complemented by dedicated BESS that are optimized for extended
energy management and grid-interactive operation rather than transient backup
alone [52]. At the converter-control level, BESS can be configured for GFM,
GFL, or hybrid GFM and GFL operation to balance fast dynamic response,
voltage/frequency support, and grid-service capability, although with added
control and sensing complexity.

 

Fig. 2:GFM BESS as a power smoothing unit [56]
IV-B2 Power Smoothing
BESS can inject or absorb power at the facility interface to attenuate rapid AI
DC demand variations and present a smoother power profile to the grid. A
BESS co-located with an AI DC can provide grid-level power smoothing while
supplying sufficient energy capacity to support sustained mitigation actions.
This architecture improves operational reliability by enabling load shaping, de-
mand flexibility, and extended ride-through for AI workloads.

 
As shown in Fig. 2, the GFM BESS effectively smooths the power fluctuations
of the AI DCs resulting from training and inference jobs. An alternative ap-
proach is a hybrid E-STATCOM and BESS configuration, which combines the
fast, high-speed charge/discharge response of supercapacitors with the higher
energy capacity of BESS to achieve effective smoothing and sustained load
support. This hybrid architecture can enhance resilience by improving demand
flexibility, reducing flicker, and enabling broader grid-service capability. The pri-

mary trade-off is increased cost and footprint compared with standalone solu-
tions. In addition, standalone supercapacitor-based E-STATCOM solutions can
mitigate high-frequency AI load fluctuations and improve power quality for sen-
sitive IT equipment by reducing flicker, although they provide limited long-dura-
tion energy support [56]. Table II compares the benefits and challenges of rep-
resentative BESS-based and hybrid strategies for enabling grid support from AI
DCs.

 
Fig. 3:UPS-Integrated BESS operation modes
IV-B3 UPS-Integrated BESS
UPS-integrated BESS are motivated by a simple premise: AI DCs already de-
ploy UPS systems with fast power-electronic interfaces, and augmenting this
mandatory infrastructure with BESS enables grid-interactive capability with lim-
ited additional integration complexity. In practice, grid-interactive deployments
also show that battery technology selection depends on the targeted services
and operating constraints. For example, UPS-integrated BESS have been used

to provide FFR by leveraging the rapid controllability of UPS power converters [
58, 59].
The UPS-integrated BESS, labeled as power smoothing units in Fig. I, extend
this concept by supporting long-duration outage operation and enabling partici-
pation in demand response programs, while the UPS maintains continuity of
critical loads when neither the grid nor the BESS can fully supply demand.

Although this architecture increases installation cost, it can significantly improve
 
overall system reliability [31].

 
As summarized in Fig. 3, a GiUPS-integrated BESS can operate in (i) standard
mode, (ii) discharge mode under full or partial disconnection, (iii) grid-services
mode, and (iv) recharge mode for SoC recovery [30]. This architecture can re-
duce the need for bidirectional power flow across the MV/LV distribution trans-
former by localizing fast power exchanges, allowing the transformer to operate
primarily under its normal unidirectional loading conditions [60]. These operat-
ing modes within the UPS–BESS subsystem enable long-duration BESS to en-
hance DC resilience through extended backup, reduce or eliminate reliance on
diesel generation, participate in ancillary and reserve markets, manage de-
mand charges and time-of-use tariffs, and increase RESs utilization [52].

 
S1) Normal operation: The AI DC load is supplied entirely from the utility grid,
and the system delivers 100% of the input power to the AI DC.

 
S2) Full disconnection with sufficient BESS reserve: The site is fully isolated
from the utility, and upon command from an external controller, the BESS sup-
plies 100% of the AI DC load power. In this case, long-duration, large-scale
BESS becomes essential; salt-cavern redox flow batteries are a promising due
to their high safety, large storage capacity, stable temperature, and low cost [61
].

 
During the transition from Scenario S1 to S2, the UPS initially supports the load
because its response time is on the order of milliseconds, while the BESS typi-
cally requires a few seconds to assume full load supply. Once engaged, the

BESS can sustain operation for extended durations (e.g., on the order of 1–4
hours, depending on sizing and operating conditions) [52].
S3) Full disconnection with insufficient BESS reserve: If the outage duration is

long and the BESS does not have sufficient available capacity to supply the full
 
AI DC load, the UPS assumes responsibility for supporting the critical load.

 
S4) Partial disconnection: The external controller reduces the grid input power,
and the remaining portion of the AI DC demand is supplied by the BESS. This
operating mode enables the BESS to support grid frequency regulation and to
present a smoother power profile at the grid interface.

 
S5) Coordinated UPS–BESS power smoothing: The grid, BESS, and UPS
jointly supply the AI DC load, with the UPS helping the BESS by providing fast
support during critical transient conditions to assist power smoothing and fre-
quency response. This case can be interpreted as an extension of S4 in which
the UPS contributes rapid, short-duration buffering when required.

 
S6) Recharge mode: When the SOC drops below full charge, the utility initiates
battery recharging (e.g., following an over-frequency detection). Under this con-
dition, the UPS is prioritized for recharging first, after which the BESS can be
recharged from the grid or from on-site renewable generation.

 
IV-C BESS Cost and Sizing Considerations
The cost of BESS per kilowatt-hour has declined dramatically, dropping from
approximately $7,500 in 1991 to $133 in 2024, with projections indicating a fur-
ther reduction to around $80 by 2030 [52]. This downward cost trajectory is ex-
pected to continue with further scale-up in manufacturing capacity and ad-
vances in both manufacturing and battery recycling processes.

 

In addition to capital cost, effective sizing must account for operational objec-
tives. Co-generation, power smoothing, and assisting GiUPS each require inde-
pendent studies to determine the optimal BESS size. Sizing also affects the
number of BESS units required for AI DCs. The sizing study will provide precise
information on whether a single hyperscale BESS is more optimal than multiple
grid-scale BESS units. Recent studies have applied advanced methods to de-
termine the optimal BESS capacity while ensuring the required capacity and
satisfying dispatch constraints [62, 63, 64]. Reference [65] shows that a 560
kWh Lithium-ion BESS, along with a 960 kWh lead-acid BESS, can provide
FFR and backup power generation for TDCs. This study can be further ex-
tended to AI DCs as well, in which the cooperation between UPS and BESS is
also considered.

 
In [62], an evolutionary algorithm is used to generate a Pareto front across dif-
ferent battery capacities, enabling selection of an appropriate size based on the
desired balance between operational benefits and battery degradation impacts.
In [63], the BESS capacity is determined using a bi-level optimization frame-
work in which the upper layer searches for the optimal storage size that mini-
mizes the total system cost. For each candidate size, the lower layer performs
optimal microgrid operation, including data center, and the BESS capacity that
yields the lowest combined investment and operational cost is selected. On the
other hand, [64] has investigated the BESS sizing for a data center based on
reliability requirements rather than cost optimization. The required storage ca-
pacity is obtained by estimating the minimum battery backup time needed to
maintain uninterrupted operation under stochastic grid outages and generator
failures.

 
V Fuel Cells (FCs) in AI DCs
FCs convert chemical energy directly into electrical energy through electro-
chemical oxidation reactions. Because this conversion is not combustion-
based, FCs can achieve electrical efficiencies exceeding 60%, which is signifi-
cantly higher than many conventional generators [66]. FC systems offer high
operational reliability due to their modular design and minimal use of mechani-
cal components, resulting in reduced maintenance requirements and high avail-

ability. When supplied with hydrogen, FCs produce no carbon dioxide or con-
ventional air pollutants during operation [67].

 
Fig. 4:FC integration with AI DC.
Among the several established FC chemistries, Solid Oxide Fuel Cells
(SOFCs), in context of AI DCs, are often highlighted for their high steady-state
efficiency and suitability for long-duration on-site power generation [68].
Polymer Electrolyte Membrane Fuel Cells (PEMFCs) exhibit faster electro-
chemical response and greater compatibility with power-electronic interfacing,
making them promising candidates for coordinated power smoothing [69]. As il-
lustrated in in Fig. 4, both SOFC and PEMFC systems rely on a shared up-
stream fuel supply while serving distinct operational roles: SOFCs assist with
base-load power to the AI DC, whereas PEMFCs, co-located with BESS, oper-
ate at faster timescales to mitigate short-term power fluctuations. With a consis-
tent and reliable fuel supply, this architecture enables hierarchical coordination
between the fuel infrastructure, on-site generation, and the utility grid.

 
V-A Role of FC in AI DCs
Commercial deployments, such as Bloom Energy’s SOFC systems, despite
their relatively high capital cost, have demonstrated the feasibility of FC installa-
tions capable of supplying primary or supplemental power to TDCs. These sys-

tems are typically configured to provide continuous or long-duration power,
serving as low-emission and more energy-efficient alternatives to diesel
generators [70]. In emerging AI DCs, whose power profiles are characterized by
large, rapid, and highly synchronized load variations, FC-based technologies
must be integrated within a broader energy architecture and operated as slow-
following or baseload resources in order to preserve efficiency and lifetime.
Accordingly, two complementary roles are considered:
V-A1 FC On-Site Generation
SOFC-based systems are primarily suited for on-site generation in AI DC envi-
 
ronments due to their high steady-state electrical efficiency, fuel flexibility, and
scalability to megawatt-class power levels [68]. When supplied by pipeline natu-
ral gas or on-site hydrogen storage, SOFC systems can provide sustained
power delivery over extended durations, making them alternatives to diesel
generators for backup and resilience applications. Unlike battery-based sys-
tems, whose backup duration is limited by stored energy capacity, FC-based
backup duration is primarily constrained by fuel availability, enabling outage
coverage ranging from hours to multiple days depending on infrastructure con-
figuration. However, due to their high operating temperatures and slow thermal
dynamics, SOFC systems are not designed for rapid power modulation and are
therefore best operated as baseload or slow-following generators within a coor-
dinated energy management framework.

 
V-A2 FC-Assisted Power Smoothing
PEMFCs operate at significantly lower temperatures than SOFCs and exhibit
faster electrochemical response, enabling limited power modulation relative to
high-temperature FC technologies. Experimental studies at the tens-of-kilowatt
scale have demonstrated that PEMFC systems can achieve sub-second power
ramping under carefully controlled conditions [71]. However, these studies also
show that stack power extraction must be constrained by maximum allowable
ramp rates to prevent fuel starvation, voltage collapse, and accelerated degra-
dation. Repeated exposure to aggressive load transients has been associated
with catalyst deterioration, membrane stress, and performance loss.
Consequently, while PEMFCs may contribute to low-frequency power balancing

service provision, they are not well suited to serve as primary resources for
high-frequency load smoothing in AI DCs [72].
In practical deployments, PEMFC operation must, therefore, be coordinated
with on-site BESSs and GiUPS systems. In such hierarchical architectures,
BESSs and UPS systems regulate fast load transients and maintain AI DC-bus
stability on millisecond-to-second timescales, while PEMFCs are dispatched
through filtered power references that limit ramp rates and confine operation to
degradation-aware regimes. Continuous monitoring of PEMFC operating condi-
tions is essential both for degradation analysis and for coordinated control with
fast-acting storage systems. When integrated in this manner, PEMFCs can
complement BESS-dominated load smoothing strategies by supplying average
power and extending overall system endurance without being subjected to
damaging high-frequency load variations [69].


 
 
V-B Sizing Considerations
Scaling FC technologies to AI DC capacities introduces constraints related to
physical aggregation, hydrogen logistics, and balance-of-plant complexity.

 
GFM control strategies for PEMFC systems have primarily been validated at
the tens-of-kilowatt scale. Scaling such architectures to the multi-megawatt
level requires parallel stack aggregation, coordinated hydrogen distribution
manifolds, auxiliary subsystem synchronization, and high-capacity DC/DC and
DC/AC conversion stages [73].

 
SOFC systems exhibit a distinct scaling trajectory. Hybridized configurations
that integrate bottoming cycles for thermal energy recovery have demonstrated
stable operation at multi-megawatt and hundred-megawatt scales [68]. In these
installations, performance gains arise primarily from thermodynamic integration.
As capacity grows, system complexity (increases) toward thermal management
and mechanical integration.

 

Accordingly, sizing decisions for AI DC deployments should not be based solely
on nominal power ratings, but on the interaction between electrochemical con-
straints, infrastructure requirements, and load temporal characteristics. PEMFC
capacity, if deployed, should be bounded by hydrogen logistics and ramp-rate
considerations, while SOFC capacity may be aligned with the steady baseload
fraction of demand.

 
VI Thermal Energy Storage (TES) in AI DCs
TES refers to technologies that store energy in the form of heat or cold by rais-
ing or lowering the temperature of a storage medium relative to ambient condi-
tions [74]. Unlike electrochemical and mechanical energy storage, TES does
not directly support the electrical power, instead it reshapes the energy demand
by decoupling thermal energy production from its consumption. This makes
TES relevant in systems where thermal load are tightly coupled with perfor-
mance and electrical demand, such as DCs [75].

 
In AI DCs, cooling constitutes 30-40% of total facility energy consumption [76]
due to the high power density of accelerator-based computing. Nearly all elec-
trical energy consumed by GPUs and associated IT equipment is ultimately
converted into low-grade heat, with studies estimating that around 90 % of in-
put electrical power manifests as waste heat within the DC environment [76].
Cooling demand, as a result, scales with computational load. While training DC
power exhibits high-frequency power swings, thermal load evolves on slower
timescales. This creates favorable conditions for the use of thermal energy stor-
age to store cooling capacity and supply it during periods of high electrical de-
mand or grid stress.

 
VI-A Characteristics and Timescale of TES Operation
TES exhibits operational characteristics that differ fundamentally from electrical
ESSs. Due to thermal inertia and heat transfer dynamics, these systems re-
spond on slower timescales, typically ranging from several minutes to hours. As
a result, TES is not suited for fast grid services such as frequency regulation or
power quality support [77].

 

Instead, the storage units are well matched to applications involving load shift-
ing, peak demand reduction, and ramp-rate mitigation of cooling-related electri-
cal loads. Thermal standby losses and insulation constraints further limit the
suitability of TES for long-term or seasonal storage in most data center applica-
tions. Consequently, TES is most effective when operated on diurnal
timescales, complementing faster electrical storage technologies within a hier-
archical energy storage framework [75].

 
VI-B TES Technologies and Integration Architectures
VI-B1 Sensible TES
Sensible TES stores cooling capacity through temperature changes in a stor-
age medium, most commonly water. Chilled water storage tanks are a mature
and widely deployed form of the technology due to their simplicity, low cost, and
ease of integration with conventional chilled-water systems [78]. However, be-
cause energy is stored through temperature differential rather than phase
change, sensible TES exhibits comparatively lower volumetric energy density
than alternative technologies. As a result, achieving equivalent storage capacity
requires significantly larger physical volume and installation area.

 
Despite this footprint requirement, sensible water-based systems remain the
least expensive option per unit of stored thermal energy and demonstrate pre-
dictable thermal behavior with minimal operational complexity [77]. For AI DC
campuses where land availability permits, sensible TES provides a cost-effec-
tive and technically robust solution for short-term load shifting and peak chiller
reduction.

 
VI-B2 Latent TES (PCM-Based)
Latent TES exploits the phase change of materials to store thermal energy at
nearly constant temperature. Compared to sensible storage, phase change ma-
terials (PCMs) provide higher volumetric energy density, allowing equivalent
cooling capacity to be achieved with substantially reduced installation volume.
This characteristic is particularly advantageous in space-constrained AI DC fa-
cilities [78].

 

The most widespread latent storage medium in cooling networks is ice, owing
to its high latent heat and relatively low material cost. Ice-based TES has been
successfully deployed in large-scale district cooling systems worldwide, demon-
strating technical feasibility at substantial capacity [78]. However, latent sys-
tems introduce additional engineering complexity, particularly in heat exchanger
integration, phase stability, and long-term cycling reliability. Although more com-
pact than sensible storage, latent TES generally entails higher capital cost per
unit of stored energy. Consequently, while ice-based TES offers clear volumet-
ric advantages for cooling applications, its deployment in AI DC environments
must balance footprint reduction against increased system complexity and eco-
nomic uncertainty.

 
VI-B3 Thermochemichal TES
Thermochemical TES stores energy through reversible chemical or sorption
processes, allowing thermal energy to be stored as chemical potential rather
than as temperature change. Such systems can achieve high energy density
and the lowest standby losses, making them attractive for long-duration storage
[78].

 
Despite these advantages, thermochemical TES systems are generally com-
plex, expensive, and less mature than sensible or latent storage technologies.
Their application in DCs is currently limited to research and demonstration
projects, though they represent a potential future option as cooling demands
continue to increase.

 
VI-C TES for RESs Integration
TES can support the integration of RESs in AI DCs by enabling power-to-cool-
ing strategies. During periods of surplus RESs generation or low electricity
prices, chillers can be operated to charge TES systems, storing cooling capac-
ity for later use [79]. This approach improves the utilization of RESs and re-
duces reliance on grid power during peak or high-emission periods.

 
By shifting cooling-related electrical demand in time, TES enhances the flexibil-
ity of AI DCs as large grid-connected loads and supports broader decarboniza-

tion objectives. 

 
VII Rack- and Server-Level ESSs roles in AI DCs
Fig. 5:Rack-level BBUs and server-level capacitors
Rack- and server-level ESSs exist to handle two constraints that centralized
UPS/BESS alone cannot satisfy: (i) local buffering (GPU-/server-scale tran-
sients that require local energy buffering), and (ii) fault domain (limiting the blast
radius of power disturbances and energy storage failures). In modern DC-archi-
tecture AI facilities, upstream layers (SST/MVDC front-ends and facility
UPS/BESS) primarily set facility envelopes and ride-through at longer
timescales, while downstream layers move buffering closer to the load to
smoothen fast dynamics and localize contingencies under faults[80, 81]. This
section focuses on rack-level BBUs as distributed ride-through and backup re-

sources, and on server/GPU-level capacitive storage as power profile
smoothening for the highest-frequency behaviors[82, 83, 84].
TABLE III:High-level comparison of rack-level BBUs and centralized UPS systems.
Aspect Rack BBUs Central UPS
Rack ride-through; local fault containment [ Facility ride-through; centralized
Primary purpose
83] management [34]
Minutes+ (backup) and grid services
Timescales Seconds–minutes (backup, recovery) [85]
where allowed [86]
Sub-second Not ideal; GPU transients are localized rail
Not ideal; accelerates battery aging [87, 72] 
 smoothing events [72] 
Coordination High; fleet SoC, recharge scheduling,
Lower; centralized components
burden priority handling [88]
Often involves AC–DC–AC in classic
Efficiency Avoids some double conversion [89]
designs
VII-A Rack-Level ESS: Role, Benefits, and Constraints
The rack represents a natural operational and electrical boundary for AI infra-
structure, with dense DC-architecture racks alone reaching MW-scale power
demands [80]. Deploying energy storage at the rack level offers several advan-
tages. First, the storage is electrically close to the load, enabling local buffering
before propagating upstream to the facility distribution system. Second, failures
in battery, converters, or wiring can be contained to individual racks, limiting the
blast radius of faults. Third, storage capacity budgets and ride-through priorities
can be configured on a per-rack basis, allowing workload-specific policies that
reflect criticality differences across the DC.

 
Despite these benefits, rack-level deployment introduces operational chal-
lenges. Coordination becomes necessary, as many independent storage units
must be managed for state-of-charge tracking, recharge scheduling, and avail-
ability monitoring. Safety and compliance requirements increase, since coloca-
tion of lithium-ion energy storage with IT equipment raises fire and thermal-run-
away mitigation concerns. Finally, maintenance overhead grows substantially,

as consistent monitoring, battery replacement, and preventive maintenance
must be performed across racks. Fig. 5 shows the implementation of rack-level
BBUs and server-level capacitors in the IT equipment.
VII-B Battery Backup Units (BBUs) as Distributed UPS
In OCP Open Rack designs, BBUs are integrated into the rack as distributed
DC ride-through modules that supply the rack DC bus during upstream AC dis-
turbances [82]. In Open Rack V3 (ORV3) architecture, a BBU shelf typically
 
hosts multiple BBU modules with 5+1 redundancy and supports both charge
mode and discharge mode operations with monitoring of SoC/SoH and mainte-
nance tests [83]. Public reference designs summarize the intended operating
point (e.g., per-module backup power on the order of kW for minutes, and
lower-power charging over hours), reflecting a design goal of short ride-through
and fast recovery rather than continuous power profile smoothening [85]. Meta
reports ORV3 BBU shelves designed for minutes of backup, and notes that
paired shelves can be used for higher rack power configurations [90].

 
VII-B1 BBU vs centralized UPS
BBUs and centralized UPS systems can both respond quickly in principle to
supply the gap between grid power disturbance or outage and longer-term en-
ergy storage systems coming online (e.g., gensets / BESS), but they differ in
where energy is buffered and what the buffer is optimized for. Centralized UPS
concentrates energy and power conversion at room/facility scale, simplifying
management and enabling grid-interactive use cases when permitted [34, 86].
Rack BBUs push storage behind fewer conversion stages in DC racks and re-
duce some double-conversion penalties compared to traditional centralized
UPS architectures [89]. Practically, BBUs are best viewed as a distributed en-
ergy availability layer for the rack (seconds–minutes), not as the primary solu-
tion for sub-second smoothing which is handled more effectively by server/GPU
capacitive buffers. Table III summarizes the high level comparison of rack-level
BBUs and centralized UPS systems.

 

VII-B2 BBUs as power absorbers
BBU shelves inherently include charging control; in normal operation they re-
main in charge mode and can modulate charging current/power within design
limits [82]. At hyperscale, uncontrolled simultaneous recharge can create step
increases in aggregate load that trip upstream protection. Production case
studies show that coordinated and priority-aware charging of distributed batter-
ies can dramatically reduce recharge power (reported reductions up to ∼80%)
while meeting recharge constraints [88].

 
However, using BBUs as a frequent, high-rate smoothing solution can acceler-
ate degradation depending on cycling throughput, C-rate, SoC range, and tem-
perature [87, 91]. Practically, server/GPU capacitors and software solution are
better suited to handle high-frequency power fluctuation, and BBUs are better
suited for ride-through, controlled recovery, and low-frequency shaping with
budgeted cycling.

 
VII-B3 Safety and deployment considerations
Rack BBUs introduce Li-ion safety considerations near IT equipment. OCP
BBU specifications explicitly reference safety and propagation constraints and
relevant certification/testing practices [82, 92]. This strongly motivates designs
that (i) enforce conservative SoC windows and thermal monitoring, and (ii) re-
duce unnecessary cycling.

 
If the design intent is “UPS-like” ride-through for all computing devices, deploy-
ment of BBU on every rack is the straightforward approach used in OCP-style
architectures [82, 83, 90]. Selective deployment (e.g., BBUs only on the high-
est-power or highest-priority racks) can reduce capex and coordination over-
head, but it changes the availability model: unprotected racks become depen-
dent on workload-level fault tolerance, or upstream ESS (BESS/gensets) with-
out transient protection.

 

VII-C Server- and GPU-Level Storage
VII-C1 Capacitors instead of batteries
The highest-frequency components of AI load power dynamics are at server-
level: rapid power consumption swings on the GPUs. These events are handled
by local decoupling and bulk capacitance [50]. Buffering at this layer prevents
microsecond-to-millisecond disturbances from propagating to the power sharing
unit (PSU) and rack bus, reducing upstream stress and allowing higher utiliza-
tion at the rack power infrastructure [72].

 
Compared with batteries, supercapacitors tolerate extremely frequent charge–
discharge cycles with minimal degradation, making them attractive for sub-sec-
ond smoothing [93, 94]. Industry offerings and proposals include compact su-
percapacitor banks intended to suppress short spikes that would otherwise re-
quire overbuilding upstream power infrastructure. The main constraint is energy
density and physical volume: supercapacitors can buffer transients and short
bursts, but they cannot provide minutes of ride-through and therefore comple-
ment (not replace) rack BBUs and other upstream ESSs [94].

 
VII-C2 Firmware/software shaping as energy “storage”
A key trend is co-design of electrical buffering with firmware-level power shap-
ing. Vendors explicitly target smoother power draw by controlling ramp rates
and limiting transient excursions. For example, NVIDIA describes firmware-con-
trolled ramp-up behavior and a “power burner” mode to manage ramp-down
and stabilize facility-level power dynamics during AI job transitions [14]. At the
platform level, software interfaces such as NVIDIA’s NVML expose enforced
GPU power limits and real-time power telemetry, enabling operators and
higher-level controllers to constrain GPU power draw and coordinate device-
level consumption with rack- or facility-level power envelopes [95]. It is framed
as an industry direction to approach power stabilization as a cross-stack prob-
lem that couples hardware energy storage and software control to prevent large
excursions and meet grid/facility ramp constraints [50].

 

VII-D Sizing Considerations for Rack- and Server-Level ESSs
Sizing at the rack and server layers is driven by different objectives than grid-
scale or UPS-level storage. Rather than energy capacity for extended outages
or grid-service participation, the dominant constraints are rack power consump-
tion, backup duration target, and redundancy requirements.

 
The fundamental BBU shelf sizing requirement is that the shelf must supply the
full rack power demand for the target ride-through duration under a single mod-
ule failure. For AI racks, where power demands can exceed 100 kW and reach
MW-scale in dense configurations [80], this places a substantially larger energy
requirement on the shelf than in traditional deployments. In ORV3 architec-
tures, the 5+1 redundancy model requires each active module to be sized for
its proportional share of the full rack load plus margin [83]. For target backup
duration, OCP reference designs reflect a goal of minutes of ride-through [85,
90]. The specific duration that rack-level storage supports should be designed
in sync with upstream ESSs, namely BESS or gensets, since its task is to
bridge outage onset with extended ESS being online. Extending this window in-
creases energy capacity but consumes already limited rack space, as well as
amplifying thermal risks for Li-ion cells colocated with IT equipment [87, 82].

 
Supercapacitors at the server level are sized to absorb the transient energy of
rapid GPU power swings [72]. For sub-second transients, while power swings
could be large, the energy required is limited, which makes supercapacitors vi-
able at this layer despite their low energy density [50, 93]. The binding con-
straint is therefore capacity with regard to the GPU power swing rather than cy-
cle life, since supercapacitors tolerate very high cycle counts with minimal
degradation [94, 14].

 
VII-E Coordination Across Rack and Server Layers
Coordination should be explicit about objectives and timescales: GPU/server
controllers shape fast dynamics under performance constraints; rack BBU con-
trollers manage SoC availability and recovery without creating recharge spikes
at facility level; facility controllers enforce facility envelopes and power-quality
limits [88, 96]. OCP rack ecosystems already expose the necessary hooks
(telemetry, shelf controllers, parallel shelf operation) to implement multi-layer

coordination in practice [82, 83]. Under MVDC architectures, server/GPU ca-
pacitive buffering can reduce required BBU power bandwidth and cycling, but
does not eliminate the seconds–minutes energy role of BBUs for ride-through
and controlled recovery [81].

 
Fig. 6:SLBESS with heterogeneous composition for backup generation of UPS
for AI DC load.
VIII Second-Life Battery Energy
Storage Systems (SLBESS) in AI DCs
Having established the functional roles of ESSs across architectural layers, an
important practical question concerns cost scalability, motivating the use of sec-
ond-life batteries (SLBs).

 
Electric vehicle (EV) batteries are typically retired when they reach around 80%
of their initial capacity. Retired batteries can either be sent to recycling facilities

or repurposed for secondary applications, giving them a second life. One of the
most common second-life applications is stationary BESS for the electric power
grid [97]. Many U.S. and Canada based startups have raised funding to re-pur-
pose used batteries. For example, B2U Storage Solutions [98], Element
Energy [99], Moment Energy [100], Smartville [101], and Redwood Energy [
102] have each demonstrated the technical and economic viability of SLBs as
behind-the-meter (BTM) and front-of-the-meter (FTM) BESS. Beyond technical
feasibility and cost savings, the reuse of SLBs confers substantial environmen-
tal advantages by decreasing lifecycle emissions and supporting a circular
economy [103]. While the application of SLBESS for grid support is well docu-
mented, their deployment for AI DC loads is an emerging and promising oppor-
tunity, as highlighted in a recent project by Crusoe Energy, where the company
installed used batteries to power AI DC load [104]. SLBESS installations must
also adhere to battery repurposing standards such as UL 1974 [105].
Therefore, regulatory compliance is mandatory for building AI DC infrastructure
and battery reuse.
VIII-A SLBESS Assisting AI DC On-Site Generation 
 
For AI DC load, SLBESS can serve as BTM generation backup source, pro-
vided that the battery packs are rigorously tested and qualified via health met-
rics. This is a GFL mode of operation where hybrid configurations, combining
used and new battery packs, are technically feasible as shown in Fig. 6. The
battery management system (BMS) balances the varying capacities of different
packs. Additionally, a single SLB pack exhibits heterogeneity across cells and
modules, resulting in variable capacities, voltages, and current limits. E.g. a sin-
gle degraded cell may constrain the performance of an entire module or pack.
To solve this, passive and active balancing schemes have been explored to
mitigate these challenges. Advanced control architectures have been proposed
to actively balance heterogeneous cell capacities in SLBs [106].

 
VIII-B Hybrid GiUPS configuration for AI DCs using SLBESS
UPS systems in AI DCs provide instantaneous backup for critical IT loads. This
necessitates energy storage solutions capable of sustained discharge durations
exceeding 10 hours. SLBESS are generally not suitable for extended durations,
and operate within a narrow SoC window to avert deep discharge. This is be-
cause the over-discharge accelerates cell-level degradation and may push cells

to the non-linear “knee point” region in the degradation curve. Thus, unless
carefully derated and managed, SLBESS may offer limited suitability for long-
duration UPS applications.
In AI DC, using SLBESS for short-duration backups while avoiding rapid degra-
dation is technically feasible. Optimal dispatch strategies must be implemented
to achieve that. Traditionally, the fundamental approach of using BESS involves
energy arbitrage, where the BESS charging occurs when electricity prices are
 
low, and discharge occurs when the electricity prices are high. This economic
objective is balanced against the physical aging of the battery through a degra-
dation cost component, shown in Eq. 6.

 

max (𝐶 𝑃 −𝐶 𝑃 ) −𝐶 (cycles (𝑃 ,𝑃 ) )
𝑑 𝑖 𝑠,𝑡 𝑑 𝑖 𝑠,𝑡 𝑐 ℎ,𝑡 𝑐 ℎ,𝑡 𝑑 𝑒 𝑔 𝑑 𝑖 𝑠,𝑡 𝑐 ℎ,𝑡 (6)

 
subject to: 
• Battery Constraints that include limits on the SoC and maximum
charge/discharge rates to ensure operational safety.

 
• Grid Constraints that includes power exchange limits and local grid
regulations.

 

 
For ever time step, 𝑡 in hours, 𝐶 and 𝐶 are the market price ($/kWh) of elec-
𝑑 𝑖 𝑠 𝑐 ℎ
tricity during the discharge and charge phase. 𝑃 and 𝑃 are the power output
𝑑 𝑖 𝑠 𝑐 ℎ
(kW) discharged from and charged to the SLBESS. 𝐶 is the degradation cost
𝑑 𝑒 𝑔
coefficient, representing the cost of battery wear per cycle. The cycles of BESS
can be calculated as a function of aggregated energy throughput 𝑓 (𝑃 CLOSE ,
𝑑 𝑖 𝑠
OPEN𝑃 ). The sum of 𝑃 and 𝑃 represents the total power throughput,
𝑐ℎ 𝑐ℎ 𝑑 𝑖 𝑠
which serves as a proxy for the stress placed on the SLBESS. To find 𝐶 in
𝑑 𝑒 𝑔
$/cycle, the data from an accelerated life testing of SLB cells of corresponding
chemistry can be used.

 

For AI DCs, the primary objective of energy storage optimal dispatch shifts from
pure arbitrage to supply guarantee and reliability. In a hybrid GiUPS configura-
tion, the SLBESS must prioritize the load over economic gains. The optimality
equation can be modified to include a reliability term, which serves as a signifi-
cant penalty for unserved load, ensuring the AI DC remains operational.
Therefore, Eq. 6 can be modified as Eq. 7

 

𝐶 𝑃 −𝐶 𝑃
max ( dis,𝑡 dis,𝑡 ch,𝑡 ch,𝑡 )
(7)
−𝐶 (𝑃 +𝑃 ) −𝐶 𝐿
deg ch,𝑡 dis,𝑡 reliability unserved,𝑡

 
𝐶 is a high-value penalty factor associated with the loss of power to the
𝑟 𝑒 𝑙𝑖 𝑎 𝑏 𝑖 𝑙 𝑖 𝑡 𝑦
AI DC (interpreting the ”supply guarantee” requirement from the sources) and
𝐿 is the portion of the critical AI DC load not met by the grid or the
𝑢 𝑛 𝑠 𝑒 𝑟 𝑣 𝑒 𝑑
SLBESS while subjected to the BESS and UPS constraints.

 
Fig. 7:FFR by utilizing new BESS and SLBESS in GiUPS architecture

On the grid side, GiUPS can be a source of FFR. This is possible with bidirec-
tional rectifiers that can respond to changing grid frequency. FFR tends to use
the BESS frequently within a narrow SoC window. SLBESS alone is not suit-
able for this sort of grid service, leading to its rapid degradation [107]. However,
if used alongside a new BESS, the UPS controller can be programmed to lever-
age the SLBESS for charging the new BESS when its SoC falls below a certain
threshold. If optimized, this can reduce the energy import from the grid, saving
the cost of energy. Fig. 7 shows the possible scenarios, which are listed below.
(i) In case of grid frequency above the threshold, the UPS controller
charges the new BESS and SLBESS, providing stabilization of the
frequency.

 
(ii) In case of grid frequency below the threshold, 
a) The UPS controller can discharge new BESS and provide power
back to the grid while powering the IT load with SLBESS.
b)The UPS controller can meet a part of the IT load using the new
BESS, and use SLBESS to charge the new BESS and stop any
import/export to the grid.

 

 
VIII-C Grid-Scale SLBESS for AI DCs
The US national grid has a long queue for interconnection requests. This leads
to limited generation and difficulties in accommodating new AI DC load. In [108
], the authors concluded that 76 GW of new load can be integrated without sig-
nificant upgrades by curtailing 0.25% of new flexible load per year. This
amounts to a curtailment of 22 hours/year. FTM grid-scale SLBESS can
achieve this by shaving peaks of AI DC load, decreasing the stress on the grid
that is caused by erratic peaks of AI DC load. It can also acts as standby gener-
ation and partake in resource adequacy. Furthermore, as hyperscalers such as
Meta, Microsoft, and Apple Inc. increasingly engage in energy market opera-
tions [109], grid-scale FTM SLBESS can be utilized to manage surplus power
from renewable generation plants under PPAs enabling these hyperscalers to
hedge against increasing energy prices.

 
By implementing the optimal dispatch strategies previously discussed, these
systems can store excess renewable energy during periods of high production

or low market cost and sell it back to the wholesale market when prices are
high. This strategy is particularly effective when using lithium-ion batteries, such
as lithium iron phosphate (LFP), which have been proven to be a viable and
high-capacity option for DC loads.
However, to successfully integrate this FTM SLBESS approach into hyperscale
 
infrastructure, several factors must be carefully balanced:

 

• Reliability vs. Profit: While selling energy to the wholesale market
provides economic benefits, the dispatch logic must prioritize supply
guarantees and the reliability of the AI DC load over arbitrage profits.

 
• Degradation Management: Because these systems utilize second-
life battery cells, dispatch strategies must be carefully managed, and
aging of the SLBESS must be monitored more rigorously than conven-
tional BESS to prevent accelerated degradation during market
participation.

 
• System Optimization: Hyperscalers can leverage real-time SLBESS
status to optimize hybrid BESS/UPS system operation, enabling effec-
tive peak shaving and grid interaction while maintaining sufficient
power reserves for critical AI DC operations.

 

 
VIII-D Cost and Sizing Aspects of SLBESS for AI DCs
VIII-D1 Csot
SLBESS is typically more cost-effective than new BESS. However, cost is influ-
enced by supply, location, and market conditions. The cost of stationary storage
declined from $169/kWh in 2020 to about $108/kWh in 2025, amounting to 36%
reduction worldwide [110]. This decline trajectory may be a hindrance to
SLBESS usage in the future. Moreover, refurbishing, operation, and mainte-
nance can constitute a significant portion of CapEx. Market analysis suggests
LFP batteries are more economically advantageous for second-life use com-
pared to nickel-rich chemistries, primarily due to the NCX battery’s higher recy-

cling value posing a demand competition between SLB repurposers and
recyclers [111]. Since reliability can be a huge factor in AI DCs, the hyper-
scalers may prioritize new BESS over SLBESS. However, the retirement of EV
batteries is expected to coincide with rising DC energy demand and the poli-
cies, such as the One, Big, Beautiful Bill Act (OBBBA) bill, introduce investment
tax credits (ITC) for battery storage sourced within the country, enhancing the
attractiveness of domestically available SLBs for AI DC deployment [112].
VIII-D2 Sizing
Sizing SLBESS for AI DCs presents a distinct engineering challenge. SLBs, re-
purposed from EV applications, exhibit reduced usable capacity, increased in-
ternal resistance, and greater heterogeneity in state-of-health (SoH) compared
to new cells [113, 114]. To mitigate accelerated degradation and ensure opera-
tional reliability, SLBs are typically operated within narrower SoC windows and

under derated conditions [115]. Unlike new batteries that can safely utilize a
broad operational SoC range (e.g., 10–90%), second-life systems are often
constrained to tighter windows (e.g., 30–70%) to limit stress and extend re-
maining useful life. This restriction directly reduces the effective usable energy
fraction, thereby requiring oversizing in both energy (kWh) and power (kW) ca-
pacity relative to the predicted load demand of AI DCs. SLBESS must be sized
not only for operational objectives such as FFR, peak shaving, and short-dura-
tion backup, but also to satisfy redundancy and fault-tolerance criteria. The SoH
variability across SLBs introduces capacity dispersion and imbalance, which
must be explicitly accounted for in system-level sizing methodologies [113].

 
Thermal and cycling considerations further complicate the sizing process. For
SLBs with limited remaining useful life (RUL), constraining DoD and per-cycle
energy throughput becomes essential to mitigate capacity fade and impedance
growth. However, these operational safeguards further reduce usable capacity
and necessitate additional oversizing. Moreover, increased internal resistance
in aged lithium-ion cells leads to reduced power capability, particularly at lower
SoC levels [116]. This reinforces the requirement for power oversizing to en-
sure that transient load spikes can be supported without violating voltage, ther-
mal, or safety constraints.

 

IX Challenges and Future Directions
IX-A Challenges for Integrating ESSs in AI DCs
In the following section the main challenges and gaps are discussed consider-
ing multi-level ESSs in AI DCs. As discussed in previous sections, the ESSs not
only can support the reliable operation of AI DCs but also can smooth the AI
DC grid integration. In addition, it showed that integrating ESSs in different lev-
els in AI DC power infrastructure leads to a grid interactive AI DC that can sup-
port the grid in emergency cases like frequency regulation, reactive power com-
pensation or peak shaving scenarios. However, there are still challenges for im-
plementing hierarchical ESSs in AI DCs, which will be discussed in the follow-
ing sections.

 
IX-A1 Simulation and Experimental Validation
To validate the optimal operation of the energy management system (EMS) of
an AI DC, it is necessary to model its different components, including the ESSs.
To our best knowledge, there is no software specifically developed for simulat-
ing EMSs of AI DCs. While MATLAB/Simulink or GT-SUITE software can be
used to integrate mechanical and electrical parts in an AI DC, the integration of
multiple solvers, electrical units, and mechanical units is not properly sup-
ported. Specifically, the multiple power conversion stages inside an AI DC re-
quire transient analysis, whereas the thermal units do not have the same re-
quirement [117, 118]. Thus, accurate analysis of ESSs in AI DCs requires a
software package that can simultaneously integrate transient and steady-state
analyses [29]. On the other hand, the available real-time simulator devices are
also not suitable for real-time experimental analysis of AI DCs, since they are
primarily developed for analyzing electrical circuits rather than combined
systems.

 
IX-A2 GPU Scheduling
Current GPU-based AI workloads are predominantly executed at the highest
supported core frequency, prioritizing peak performance at the expense of en-
ergy efficiency. Unlike CPUs, where dynamic voltage and frequency scaling
(DVFS) is a mature and widely adopted mechanism, energy-aware frequency
regulation for GPUs remains at an early stage of development [119, 120].
Moreover, existing GPU scheduling policies largely optimize for throughput and

latency, without explicitly considering the energy consumption characteristics of
heterogeneous deep learning tasks [121, 122]. This limitation is further exacer-
bated by the fact that many deep learning developers possess limited insight
into the underlying hardware behavior of AI workloads. This can accelerate the
degradation of ESSs and reveals the lack of control over GPU power profiles,
which is essential for power smoothing scenarios.
IX-A3 Distribution Transformers and AI DCs
Traditional distribution transformers are primarily designed for unidirectional
power flow, supplying electricity from the medium-voltage grid to downstream
loads, and their deployment in grids with grid-interactive AI DCs introduces new

operational challenges. AI DCs equipped with large-scale ESSs and advanced
 
power electronics can dynamically shift between high consumption and active
power injection modes for grid services. Under such bidirectional power flow,
conventional transformers may experience accelerated thermal aging due to
loading patterns and reverse power conditions that deviate from standard de-
sign assumptions [60]. Moreover, voltage regulation mechanisms and tap set-
tings optimized for passive load behavior may become ineffective or unstable
when facing rapid transitions between load and injection states [123]. These
limitations reveal that conventional distribution transformers are not inherently
suited for highly dynamic, bidirectional operation driven by GiUPS or BESSs in
AI DCs, underscoring the need for enhanced transformer models, real-time
monitoring, and power-electronic-aware grid interfaces.

 
IX-A4 Load Forecasting in AI DCs
As discussed earlier, the AI DC power profile is hard for forecast. The traditional
loads in power grids have predictable trajectories that can be predicted consid-
ering the proper historical data. However, this is not applicable for AI DC load
profile. As a result, it can directly affected the sizing and ESS operation modes
in AI DCs. For instance, the rack-level BESS or chip-level batteries which are
designed for power smoothing applications need the accurate power consump-
tion to operate effectively. In addition, the grid-scale BESSs are also need the
accurate load profile of the DC to smooth the load and provide effective grid
support.

 

IX-A5 Advanced ESSs Degradation Modeling and Life Time Prediction
Due to high power variability in AI DCs, more frequent charging and discharging
scenarios for ESSs are inevitable. This require a precise degradation analysis
to maximize the life time and optimize the ESS operation. As discussed in sec-
tion VII, the ESS at chip or rack level experiences a very high frequency in dif-
ferent operating conditions to smooth the power profile. In this regard, the on-
line monitoring of the ESS could help for better life time prediction and proac-
tive maintenance operations. As Lithium-ion batteries are more desirable for fu-
ture AI DCs, the study of cyclic aging is important in both small scale ESSs or
large scale BESSs. In addition, the installed SLBESSs in AI DCs are more vul-
nerable in case of aging and they need more precise monitorization especially
for larger scale storage units.

 
IX-A6 Hierarchical ESSs Coordination
Multi-level ESS implementation in AI DCs requires a centralized EMS to moni-
tor the operating modes of different ESSs and ensure coordination among them
[124]. The on-site grid-scale BESS should operate properly with the GiUPS to
enable accurate power sharing, either to efficiently utilize RESs or to support
the grid in emergency cases. Moreover, the GiUPS battery size and its switch-
ing time are related to the size of the on-site grid-scale BESS. Reliability analy-
sis and cost-comparison analysis are required to determine the optimal combi-
nation of both for supplying the AI DC and supporting the power grid. The work
[125] demonstrates a novel control framework for utilizing supercapacitors and
grid-scale BESS for load smoothing, which shows the potential of hierarchical
coordination among ESS units.

 
TES is also required to operate coherently with the on-site BESS or FC. The
BESS absorbs excess power during off-peak periods, and this energy can be
utilized to support the TES, as stated in section VI. However, coordinating these
systems according to the BESS capacity and its key role in power smoothing or
grid support is challenging. In addition, the BBUs and chip-level ESSs should
operate together for power smoothing through multi-layer coordination. Thus,
ESSs have a direct impact on each other, or at least on their neighboring lay-
ers, in a multi-layer structure, which necessitates a centralized control and
management system with appropriate data acquisition units.

 

IX-A7 Long Duration ESSs (LDESSs)
On-site large scale BESSs or GiUPS systems require LDESSs to compensate
the intermittency of RESs or providing long lasting AI DC support in case of the
utility power failure [126]. The technology for LDESSs is still not mature and fur-
ther investigation are needed.

 
IX-A8 Optimal Sizing and Cost Considerations
There is little public research on the optimal sizing and cost analysis of ESSs
inside DCs. In AI DCs, due to the presence of multi-layer ESSs, sizing and cost
analysis are even more critical. For instance, is a grid-scale BESS more cost-
effective, or a GiUPS system with high power-density batteries? Alternatively, is
it more cost-effective to consider large-scale supercapacitors at the rack level,
or to use a combination of BBUs and supercapacitors in load-smoothing sce-
narios? To answer these questions, multiple analyses should be considered to
enable precise comparisons.

 
IX-B Possible Future Directions
IX-B1 Power-Aware GPU Scheduling
During the training of deep learning models for predicting responses under dif-
ferent configuration settings, it is essential to jointly learn and optimize both
throughput and energy consumption. This requires adaptive strategies for local
and global batch size scheduling to balance convergence speed with computa-
tional efficiency [127]. Some solutions are discussed in section VII. In addition,
GPU resources should be dynamically scheduled across training tasks by ac-
counting for time-varying electricity prices and the availability of renewable en-
ergy sources, enabling energy-aware model training [6, 128, 129, 130]. To sup-
port such flexibility, elastic resource allocation is a key requirement, allowing
the number of GPUs assigned to a training job to be adjusted dynamically dur-
ing execution without disrupting the learning process. This elasticity enables ef-
ficient utilization of heterogeneous compute resources and provides the control-
lability of GPU power consumption which is necessary for chip-level ESS or
BBU scheduling. Beyond this, dynamic batch size selection can be imple-
mented to regulate the utility grid voltage profile [131]. The work [131] demon-
strates the potential of chip-level utilization to enhance system-level objectives,

in which ESSs implementation can also be included in the optimization
problem.
IX-B2 AI DC Load Observability
High-resolution monitoring of DC load dynamics can be achieved by employing
waveform measurement units capable of capturing load profiles at very short
time intervals (below 10 ms) [1]. Such fine-grained measurements enable the
observation of fast transient behaviors and rapid load fluctuations that are oth-
erwise invisible to conventional metering infrastructure. Building on this high-fi-
delity data, machine learning techniques can be leveraged to accurately predict
short-term and long-term load patterns, supporting proactive control and opti-
mization strategies. Besides, advanced load modeling studies are further in-
crease the load observability of AI DCs not only for short term studies but also
for long term planning and operation tasks [132, 133, 134, 135]. Furthermore,
close collaboration between utilities and DC operators is essential to enable se-
cure access to real-time load profiles, ensuring data confidentiality while facili-
tating coordinated grid–DC operation and enhanced system reliability.

 

 
IX-B3 Advanced Degradation, State Estimation,
and RUL Prediction during operation
Lithium-ion batteries undergo both calendar degradation and cyclic aging [136].
Calendar degradation is time-dependent and occurs regardless of battery us-
age, while cyclic degradation results from charge-discharge cycles.
Degradation pathways, including solid electrolyte interphase (SEI) growth,
lithium plating, and particle fracture [97] lead to capacity fade and increased in-
ternal resistance. To avoid the SLBs from entering the non-linear region of the
degradation curve, a degradation-aware dispatch strategy needs to be devised.
Estimating the RUL of SLBs is essential for safe deployment. Approaches
range from data-driven techniques [137], neural network-based models, to en-
tropy-based algorithms [138]. Uniquely, aging curves of SLBs are shaped by
first-life usage patterns, making every battery distinct. European Union led
Initiative Battery Passport [139] tracks lifecycle data, empowering refurbishers
to select candidates for reuse.

 

IX-B4 FTM grid-scale BESS as A Reliable Reserve
By monitoring and communicating the grid-scale BESS status, located in AI DC
sites, with the grid operator, more optimized reserve planning can be achieved [
140, 141]. In this case, the total amount of unused energy of grid-scale BESS
can be considered a potential reserve that can be injected into the utility grid
during contingency events such as the tripping of synchronous generators. The
FTM grid-scale BESS can also play the role of an active reserve source in
emergency cases by locally feeding the AI DC load. In this case, the grid opera-
tor disconnects the AI DC from the grid and allows the AI DC to supply its load
using the available BESS co-generation resources. However, this requires pre-
cise coordination and control strategies between both the utility and AI DC
owners.

 
IX-B5 Revisiting SSTs for AI DCs
SSTs [142, 143, 144] are considered primarily for enabling medium-voltage AC
to high-voltage DC conversion (e.g., 800 V DC or higher) to improve rack-level
power density in AI DCs [80]. In SST-based architectures, traditional UPS func-
tionalities can be embedded within multi-stage power electronic converters.
Moreover, SSTs eliminate the distribution transformer in the AI DC power deliv-
ery system, thereby minimizing the side effects of bidirectional power flow.
However, SSTs face several challenges including lower reliability due to multi-
level, multi-stage power conversion, limited power rating (typically a few MVA)
and increased control complexity and cost. While SSTs are attractive for high-
density power delivery, they are not yet suitable replacements for UPS systems
at gigawatt-scale DCs. Multi-level modular SST architectures, as proposed in
recent industry studies, may improve scalability, but reliability and standardiza-
tion remain key challenges.

 
IX-B6 AI DC as a Microgrid
AI DC microgrids adopt hybrid power architectures [145, 146]. These architec-
tures integrate BESS, conventional generators, distributed generation units,
and utility grid connections (see Fig. 8). The objective is to achieve high reliabil-
ity and redundancy. The placement of BESS is a key design choice. Proper
placement allows BESS to damp fast load fluctuations. It also improves local
voltage and frequency stability. BESS enable coordinated operation among dif-
ferent power generation units. They support grid services such as demand re-

sponse and peak shaving. They also provide fast reserves. Optimal integration
of BESS with other units requires joint power flow and control design. This inte-
gration raises the question of BESS versus grid-interactive UPS systems. The
boundary between backup and active grid support becomes unclear. In this
context, BESS redefine power interface thresholds and reshape power quality
metrics. This enables data center microgrids to act as active and flexible grid
participants.

 
Fig. 8:AI DC microgrid.
X Conclusions
This paper provides a comprehensive review of multi-layer ESSs in future AI
DCs and their role in supporting both DCs and the utility grid. ESSs ranging
from chip-level units to large-scale BESSs are discussed, with particular em-

phasis on their contribution to grid support and ancillary services. Chip-level
ESSs act as the first layer for smoothing heterogeneous GPU power profiles,
while large-scale BESSs constitute the final layer in this hierarchical structure.
The concept of GiUPS is thoroughly examined, highlighting bidirectional power
flow capability as a key enabler of grid-aware UPS design. Moreover, the paper
extends beyond battery-based ESSs and investigates the roles of FCs and
TEs. FCs are considered a promising alternative to conventional gensets in fu-
ture AI DCs, offering a lower carbon footprint when using hydrogen. The role of
TEs in enabling advanced cooling systems and maximizing the utilization of
RESs as on-site generation units is also discussed. SLBESSs offer more cost-
efficient solutions for ESS integration but require additional monitorization due
to lifetime uncertainties. Furthermore, the main challenges associated with ESS
integration in AI DCs are outlined. Finally, as a future direction, the deployment
of multi-layer ESS architectures necessitates advanced monitoring systems
and EMSs to enable optimal coordination across different layers.
References

 
[1] B. Chalamala et al. (2025)
Data center growth and grid readiness (tr131).
Technical Report
Technical Report TR131, IEEE Power and Energy Society.
External Links: Document (https://dx.doi.org/10.17023/w4wy-s557)
Cited by: §I, §IX-B2.
[2] North American Electric Reliability Corporation (NERC) (2025)
Characteristics and risks of emerging large loads.
White Paper
NERC.
Note: Large Loads Task Force (LLTF)
External Links: Link (https://www.nerc.com/globalassets/who-we-are/standin
g-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.
pdf)
Cited by: §I, §II-B1.

[3] A. Jonker and A. Gomstyn (2025)
What is an ai data center?.
External Links: Link (https://www.ibm.com/think/topics/ai-data-center)
Cited by: §I.
[4] Stream Data Centers (2024)
Data center development in an ai-driven market.
Technical report
Stream Data Centers.
External Links: Link (https://www.streamdatacenters.com/wp-content/upload
s/2024/02/SDC-BTPS-Whitepaper-240222.pdf)
Cited by: §I.
[5] T. McLaughlin (2025)
Big tech’s data center boom poses new risk to us grid operators.
External Links: Link (https://www.reuters.com/technology/big-techs-data-cent
er-boom-poses-new-risk-us-grid-operators-2025-03-19/)
Cited by: §I.
[6] X. Chen, X. Wang, A. Colacelli, M. Lee, and L. Xie (2025)
Electricity demand and grid impacts of ai data centers: challenges
and prospects.
arXiv preprint arXiv:2509.07218.
Cited by: §I, §IX-B1.
[7] E. Ginzburg-Ganz, P. Lifshits, R. Machlev, J. Belikov, Z. Krieger, and
Y. Levron (2025)
Technical challenges of ai data center integration into power grids—
a survey.
Energies 19 (1), pp. 137.
Cited by: §I, §III-C.
[8] S. Rahman and T. A. Khan (2026)
Energy storage systems for ai data centers: a review of
technologies, characteristics, and applicability.
Energies 19 (3), pp. 634.
Cited by: §I, §III-C.
[9] A. Safari, F. Blaabjerg, and A. Oshnoei (2026)
A research-industry perspective of battery systems technology for
next-generation data centers.
Journal of Energy Storage 152, pp. 120386.

External Links: ISSN 2352-152X, Document (https://dx.doi.org/https%3
A//doi.org/10.1016/j.est.2026.120386), Link (https://www.sciencedirect.com/scie
nce/article/pii/S2352152X26000502)
Cited by: §I.
[10] K. Qian, Y. Xi, J. Cao, J. Gao, et al. (2024)
Alibaba hpn: a data center network for large language model
training.
In Proceedings of the ACM SIGCOMM 2024 Conference,
New York, NY, USA, pp. 691–706.
External Links: Document (https://dx.doi.org/10.1145/3651890.3672265),
Link (https://dl.acm.org/doi/10.1145/3651890.3672265)
Cited by: §II-A2, §II-A3, §II-A3, §II-A.
[11] N. V. Savant (2025)GPU-to-gpu communication: unlocking
parallelism beyond the core(Website)
Medium.
External Links: Link (https://medium.com/@nikheelvs/gpu-to-gpu-communica
tion-unlocking-parallelism-beyond-the-core-a80de2974078)
Cited by: §II-A3, §II-A.
[12] North American Electric Reliability Corporation (NERC) (2025)
Characteristics and risks of emerging large loads.
Technical report
North American Electric Reliability Corporation.
Note: Large Loads Task Force White Paper
Cited by: §II-A1, §IV.
[13] Atlantic.Net (2025)An overview of popular nvidia gpus(Website)
Atlantic.Net.
Note: Accessed: 2026-02-27
External Links: Link (https://www.atlantic.net/gpu-server-hosting/an-overview-
of-popular-nvidia-gpus/)
Cited by: §II-A1.
[14] N. S. Rouslan Dimitrov and M. Blake (2025)How new gb300 nvl72
features provide steady power for ai(Website)
NVIDIA Developer Blog.
External Links: Link (https://developer.nvidia.com/blog/how-new-gb300-nvl72
-features-provide-steady-power-for-ai/)
Cited by: §II-A1, §VII-C2, §VII-D.

[15] Google Cloud (2024)Accelerating ai inference with google cloud
tpus and gpus(Website)
Google Cloud Blog.
Note: Accessed: 2026-02-27
External Links: Link (https://cloud.google.com/blog/products/compute/acceler
ating-ai-inference-with-google-cloud-tpus-and-gpus)
Cited by: §II-A1.
[16] Micron Technology (2024)What changes in storage will ai drive?
(Website)
Micron Blog.
External Links: Link (https://www.micron.com/about/blog/storage/ai/what-cha
nges-in-storage-will-ai-drive)
Cited by: §II-A2.
[17] NVIDIA Corporation (2019)GPUDirect storage: a direct path
between storage and gpu memory(Website)
NVIDIA Developer Blog.
External Links: Link (https://developer.nvidia.com/blog/gpudirect-storage/)
Cited by: §II-A2.
[18] A. Gangidi, R. Miao, S. Zheng, S. J. Bondu, G. Goes, H. Morsy, R.
Puri, M. Riftadi, A. J. Shetty, J. Yang, S. Zhang, M. J. Fernandez, S.
Gandham, and H. Zeng (2024)
RDMA over ethernet for distributed training at meta scale.
In Proceedings of the ACM SIGCOMM 2024 Conference,
ACM SIGCOMM ’24, New York, NY, USA, pp. 57–70.
External Links: ISBN 9798400706141, Link (https://doi.org/10.1145/3651
890.3672233), Document (https://dx.doi.org/10.1145/3651890.3672233)
Cited by: §II-A3.
[19] NVIDIA Corporation (2023)Networking for data centers and the era
of ai(Website)
NVIDIA Developer Blog.
External Links: Link (https://developer.nvidia.com/blog/networking-for-data-ce
nters-and-the-era-of-ai/)
Cited by: §II-A3.
[20] S. Sheehan and A. Rakow (2023)
Evolving a data center into a microgrid: industry perspectives and
lessons learned.
IEEE Electrification Magazine 11 (3), pp. 16–25.

External Links: Document (https://dx.doi.org/10.1109/MELE.2023.3291193)
Cited by: §II-B3.
[21] U.S. Department of Energy (2025)Advantages and challenges of
nuclear-powered data centers(Website)
Office of Nuclear Energy.
Note: Accessed: 2026-02-27
External Links: Link (https://www.energy.gov/ne/articles/advantages-and-chal
lenges-nuclear-powered-data-centers)
Cited by: §II-B3.
[22] H. Nehrir and C. Wang (2025)
Hydrogen fuel and fuel cells: potential candidates for sustainable,
dispatchable, and environmentally friendly power generation and
transport technologies.
IEEE Energy Sustainability Magazine 1 (3), pp. 52–65.
External Links: Document (https://dx.doi.org/10.1109/ESM.2025.3606163)
Cited by: §II-B3.
[23] Vertiv (2024)Understanding direct-to-chip cooling in hpc
infrastructure: a deep dive into liquid cooling(Website)
Vertiv.
External Links: Link (https://www.vertiv.com/en-us/about/news-and-insights/a
rticles/educational-articles/understanding-direct-to-chip-cooling-in-hpc-infrastruct
ure-a-deep-dive-into-liquid-cooling/)
Cited by: §II-C.
[24] M. T. Takci, M. Qadrdan, J. Summers, and J. Gustafsson (2025)
Data centres as a source of flexibility for power systems.
Energy Reports 13, pp. 3661–3671.
Cited by: §II-C.
[25] A. Karpati, G. Zsigmond, M. Vörös, and M. Lendvay (2012)
Uninterruptible power supplies (ups) for data center.
In 2012 IEEE 10th Jubilee International Symposium on Intelligent
Systems and Informatics,
pp. 351–355.
Cited by: §III-A.
[26] A. Fawaz, J. Lorincz, and A. F. Mohammed (2019)
Minimizing data center uninterruptable power supply overload by
server power capping.
IEEE Communications Letters 23 (8), pp. 1342–1346.

Cited by: §III-A.
[27] Z. Wang, Z. Yin, J. Yang, and J. Wang (2025)
Coordinated optimization of distributed energy system and storage-
enhanced uninterruptible power supply in data center: a three-level
optimization framework with model predictive control.
Energy Conversion and Management 342, pp. 120137.
Cited by: §III-A.
[28] J. Paananen (2023)
Grid-interactive data centers enabling energy transition: data
center’s hidden potential to provide essential grid services of a
future power system.
IEEE Electrification Magazine 11 (3), pp. 26–34.
External Links: Document (https://dx.doi.org/10.1109/MELE.2023.3291195)
Cited by: §III-B.
[29] P. Colangelo, A. K. Coskun, J. Megrue, C. Roberts, S. Sengupta, V.
Sivaram, E. Tiao, A. Vijaykar, C. Williams, D. C. Wilson, et al. (2025)
AI data centres as grid-interactive assets.
Nature Energy, pp. 1–8.
Cited by: §III-B, §IX-A1.
[30] A. Di Filippi and L. Valentini (2025)
How to maximize revenues from your data center energy storage
system with grid interactive ups.
Technical report
Vertiv.
Note: Vertiv White Paper
Cited by: §III-B1, §III-B3, §III-B, §IV-B3.
[31] J. Paananen and E. Nasr (2021)
Grid-interactive data centers: enabling decarbonization and system
stability.
Dublin, Ireland.
Cited by: §III-B, §IV-B3.
[32] ON.energy (2025)
Hyperscale meets grid stability: on.energy launches medium-voltage
ups built for ai data centers.
External Links: Link (https://www.nacleanenergy.com/alternative-energies/hy
perscale-meets-grid-stability-on-energy-launches-medium-voltage-ups-built-for-a
i-data-centers)

Cited by: §III-B.
[33] A. Di Filippi and L. Valentini (2025)
How to maximize revenues from your data center energy storage
system with grid interactive ups.
External Links: Link (https://www.vertiv.com/4918e5/globalassets/documents/
white-papers/white-paper-maximize-revenues-data-center-energy-storage-grid-u
ps_329440_2.pdf)
Cited by: §III-B.
[34] Eaton
Eaton and microsoft’s energyaware ups technology pilot project.
External Links: Link (https://www.eaton.com/us/en-us/products/backup-power
-ups-surge-it-power-distribution/backup-power-ups/dual-purpose-ups-technolog
y.html)
Cited by: §III-B1, §VII-B1, TABLE III.
[35] Y. Xie, W. Cui, and A. Wierman (2025)
Enhancing data center low-voltage ride-through.
arXiv preprint arXiv:2510.03867.
Cited by: §III-B2.
[36] A. Azizi, S. Morovati, A. Zamani, J. Piruzza, D. Guo, Z. Liu, and P.
Taimela (2026)
Strengthening data center operations using grid-forming battery
energy storage as a line-interactive uninterruptible power supply.
International Journal of Electrical Power & Energy Systems 175,
pp. 111638.
Cited by: §III-B2.
[37] C. Tozzi (2026)
Voltage ride-through: a key ingredient in data center resilience.
External Links: Link (https://www.datacenterknowledge.com/uptime/voltage-ri
de-through-a-key-ingredient-in-data-center-resilience)
Cited by: §III-B2.
[38] J. Conto, Y. Cheng, J. Rose, and J. Schmall (2025)
Texas loads ride toward grid stability: voltage ride through of large
power electronic loads.
IEEE Power and Energy Magazine 23 (5), pp. 56–67.
Cited by: §III-B2.
[39] R. Zahedi, A. Zamani, and R. Anilkumar (2026)

Best practices for large load interconnections: a north american
perspective on data centers.
arXiv preprint arXiv:2601.12686.
Cited by: §III-B2.
[40] R. Li, H. Geng, and G. Yang (2016)
Fault ride-through of renewable energy conversion systems during
voltage recovery.
Journal of Modern Power Systems and Clean Energy 4 (1), pp. 28–
39.
Cited by: §III-B2.
[41] Y. Cheng, M. Sahni, J. Conto, S. Huang, and J. Schmall (2011)
Voltage-profile-based approach for developing collection system
aggregated models for wind generation resources for grid voltage
ride-through studies.
IET Renewable Power Generation 5 (5), pp. 332–346.
Cited by: §III-B2.
[42] D. Pant, A. Singh, G. Van Bogaert, Y. A. Gallego, L. Diels, and K.
Vanbroekhoven (2011)
An introduction to the life cycle assessment (lca) of
bioelectrochemical systems (bes) for sustainable energy and
product generation: relevance and key aspects.
Renewable and Sustainable Energy Reviews 15 (2), pp. 1305–
1313.
Cited by: §III-C.
[43] R. Kaiser (2007)
Optimized battery-management system to improve storage lifetime
in renewable energy systems.
Journal of Power Sources 168 (1), pp. 58–65.
Cited by: §III-C.
[44] Y. Zhang, Y. Xu, H. Yang, Z. Y. Dong, and R. Zhang (2019)
Optimal whole-life-cycle planning of battery energy storage for multi-
functional services in power systems.
IEEE Transactions on Sustainable Energy 11 (4), pp. 2077–2086.
Cited by: §III-C.
[45] J. Wang, S. Ye, B. Wu, and B. Liu (2026)
Life-cycle performance analysis of a building integrated energy
system considering equipment performance degradation.

Energy Conversion and Management 347, pp. 120593.
Cited by: §III-C.
[46] M. Kamali and K. Hewage (2016)
Life cycle performance of modular buildings: a critical review.
Renewable and sustainable energy reviews 62, pp. 1171–1183.
Cited by: §III-C.
[47] N. Omar, M. A. Monem, Y. Firouz, J. Salminen, J. Smekens, O.
Hegazy, H. Gaulous, G. Mulder, P. Van den Bossche, T.
Coosemans, et al. (2014)
Lithium iron phosphate based battery–assessment of the aging
parameters and development of cycle life model.
Applied Energy 113, pp. 1575–1585.
Cited by: §III-C.
[48] G. Majeau-Bettez, T. R. Hawkins, and A. H. Strømman (2011)
Life cycle environmental assessment of lithium-ion and nickel metal
hydride batteries for plug-in hybrid and battery electric vehicles.
Environmental science & technology 45 (10), pp. 4548–4554.
Cited by: §III-C.
[49] Y. Ding, Z. P. Cano, A. Yu, J. Lu, and Z. Chen (2019)
Automotive li-ion batteries: current status and future perspectives.
Electrochemical Energy Reviews 2 (1), pp. 1–28.
Cited by: §III-C.
[50] E. Choukse, B. Warrier, S. Heath, L. Belmont, A. Zhao, H. A. Khan,
B. Harry, M. Kappel, R. J. Hewett, K. Datta, et al. (2025)
Power stabilization for ai training datacenters.
arXiv preprint arXiv:2508.14318.
Cited by: §IV, §VII-C1, §VII-C2, §VII-D.
[51] North American Electric Reliability Corporation (NERC) (2023)
Grid forming functional specifications for bps-connected battery
energy storage systems.
White Paper
North American Electric Reliability Corporation.
External Links: Link (https://www.nerc.com/globalassets/our-work/reports/whi
te-papers/white_paper_gfm_functional_specification.pdf)
Cited by: §IV-A.
[52] P. Donovan (2025)

Understanding bess: battery energy storage systems for data
centers.
Technical report
Technical Report White Paper 185, Schneider Electric Energy
Management Research Center.
Cited by: §IV-A, §IV-B1, §IV-B3, §IV-B3, §IV-C.
[53] R. H. Lasseter, Z. Chen, and D. Pattabiraman (2020)
Grid-forming inverters: a critical asset for the power grid.
IEEE Journal of Emerging and Selected Topics in Power Electronics
8 (2), pp. 925–935.
External Links: Document (https://dx.doi.org/10.1109/JESTPE.2019.295927
1)
Cited by: §IV-A1.
[54] F. Milano, F. Dörfler, G. Hug, D. J. Hill, and G. Verbič (2018)
Foundations and challenges of low-inertia systems (invited paper).
In 2018 Power Systems Computation Conference (PSCC),
Vol. , pp. 1–25.
External Links: Document (https://dx.doi.org/10.23919/PSCC.2018.845088
0)
Cited by: §IV-A1, §IV-A2.
[55] F. Blaabjerg, R. Teodorescu, M. Liserre, and A.V. Timbus (2006)
Overview of control and grid synchronization for distributed power
generation systems.
IEEE Transactions on Industrial Electronics 53 (5), pp. 1398–1409.
External Links: Document (https://dx.doi.org/10.1109/TIE.2006.881997)
Cited by: §IV-A2.
[56] Quanta Tech LLC (2025)
Understanding ai load profiles and their impact on power systems.
Note: Online Seminar (Webinar)
Cited by: Fig. 2, §IV-B2, TABLE II.
[57] R. R. Ahrabi, A. Mousavi, E. Mohammadi, R. Wu, and A. K. Chen
(2025)
AI-driven data center energy profile, power quality, sustainable
sitting, and energy management: a comprehensive survey.
In 2025 IEEE Conference on Technologies for Sustainability
(SusTech),
pp. 1–8.

Cited by: §IV-B1.
[58] K. Watson (2025)
Data centers – a good grid citizen.
Eaton.
Note: PresentationSlide on grid support and batteries; Mission
Critical Solutions presentation
Cited by: §IV-B1, §IV-B3.
[59] X. Tao and R. Gadh (2025)
Coordinated fast frequency response from electric vehicles, data
centers, and battery energy storage systems.
arXiv preprint arXiv:2512.14136.
Cited by: §IV-B3.
[60] I. B. Majeed and N. I. Nwulu (2022)
Impact of reverse power flow on distributed transformers in a solar-
photovoltaic-integrated low-voltage network.
Energies 15 (23), pp. 9238.
Cited by: §IV-B3, §IX-A3.
[61] L. Pan, M. Song, N. Muzaffar, L. Chen, C. Ji, S. Yao, J. Xu, W. Wu,
Y. Li, J. Chen, et al. (2025)
Salt cavern redox flow battery: the next-generation long-duration,
large-scale energy storage system.
Current Opinion in Electrochemistry 49, pp. 101604.
Cited by: §IV-B3.
[62] A. Mamun, I. Narayanan, D. Wang, A. Sivasubramaniam, and H.
Fathy (2016)
Multi-objective optimization of demand response in a datacenter
with lithium-ion battery storage.
Journal of Energy Storage 7, pp. 258–269.
Cited by: §IV-C, §IV-C.
[63] G. Ye, J. Fang, N. Wang, Y. Gaogao, and K. Sun (2026)
A grid-forming energy storage system capacity planning method
considering device lifetime.
Energies.
Cited by: §IV-C, §IV-C.
[64] Y. Yu, K. Shan, H. Tang, and S. Wang (2025)
Reliability and economic impacts of utilizing battery energy storage
in data centers for energy flexibility services in smart grids.

Energy Conversion and Management 339, pp. 119951.
Cited by: §IV-C, §IV-C.
[65] L. Cupelli, N. Barve, and A. Monti (2017)
Optimal sizing of data center battery energy storage system for
provision of frequency containment reserve.
In IECON 2017 - 43rd Annual Conference of the IEEE Industrial
Electronics Society,
Vol. , pp. 7185–7190.
External Links: Document (https://dx.doi.org/10.1109/IECON.2017.8217257)
Cited by: §IV-C.
[66] L. Fan, Z. Tu, and S. H. Chan (2021)
Recent development of hydrogen and fuel cell technologies: a
review.
Energy Reports 7, pp. 8421–8446.
Cited by: §V.
[67] D. Manzo, R. Thai, H. T. Le, and G. K. Venayagamoorthy (2025)
Fuel cell technology review: types, economy, applications, and
vehicle-to-grid scheme.
Sustainable Energy Technologies and Assessments 75, pp. 104229.
Cited by: §V.
[68] I. Nikiforakis, S. Mamalis, and D. Assanis (2025)
Understanding solid oxide fuel cell hybridization: a critical review.
Applied Energy 377, pp. 124277.
Cited by: §V-A1, §V-B, §V.
[69] I. Kong, W. Kim, and S. Chae (2025)
A grid-forming control method for pemfc power conversion systems
with power ramp rate limitation to prevent fuel starvation.
IEEE Open Journal of Power Electronics.
Cited by: §V-A2, §V.
[70] F. Perez (2025)
Enabling net zero data centers: a techno-economic analysis of
bloom energy’s sofc systems.
Ph.D. Thesis, Politecnico di Torino.
Cited by: §V-A.
[71] K. Nikiforow, J. Pennanen, J. Ihonen, S. Uski, and P. Koski (2018)

Power ramp rate capabilities of a 5 kw proton exchange membrane
fuel cell system with discrete ejector control.
Journal of Power Sources 381, pp. 30–37.
Cited by: §V-A2.
[72] Y. Li and Y. Li (2025)
AI load dynamics–a power electronics perspective.
arXiv preprint arXiv:2502.01647.
Cited by: §V-A2, §VII-C1, §VII-D, TABLE III, TABLE III.
[73] P. Zheng, X. Xie, C. Zhang, S. Cai, J. Pan, H. Zhang, M. Yan, and
Q. Mu (2025)
Techno-economic assessment framework for 2.5 mw-scale grid-
connected proton exchange membrane fuel cell power systems: a
case study in china.
International Journal of Hydrogen Energy 167, pp. 150942.
Cited by: §V-B.
[74] G. Alva, Y. Lin, and G. Fang (2018)
An overview of thermal energy storage systems.
Energy 144, pp. 341–378.
Cited by: §VI.
[75] D. Enescu, G. Chicco, R. Porumb, and G. Seritan (2020)
Thermal energy storage for grid applications: current status and
emerging trends.
Energies 13 (2), pp. 340.
Cited by: §VI-A, §VI.
[76] M. Omrani and M. Ghassemi (2025)
AI-driven optimization of fan-wall cooling system in a medium-
density data center.
International Journal of Heat and Mass Transfer 247, pp. 127159.
Cited by: §VI.
[77] E. Guelpa and V. Verda (2019)
Thermal energy storage in district heating and cooling systems: a
review.
Applied Energy 252, pp. 113474.
Cited by: §VI-A, §VI-B1.
[78] I. Sarbu and C. Sebarchievici (2018)
A comprehensive review of thermal energy storage.
Sustainability 10 (1), pp. 191.

Cited by: §VI-B1, §VI-B2, §VI-B2, §VI-B3.
[79] C. Luerssen, O. Gandhi, T. Reindl, C. Sekhar, and D. Cheong
(2020)
Life cycle cost analysis (lcca) of pv-powered cooling systems with
thermal energy and battery storage for off-grid applications.
Applied Energy 273, pp. 115145.
Cited by: §VI-C.
[80] J. Huntington and M. Tu (2025)
800 vdc architecture for next-generation ai infrastructure.
External Links: Link (https://nvdam.nvidia.com/assets/share/asset/zlg5snufe
o)
Cited by: §VII-A, §VII-D, §VII, §IX-B5.
[81] IEC (2025)
Medium voltage dc (mvdc) grids for anall-electric society.
External Links: Link (https://www.iec.ch/basecamp/medium-voltage-dc-mvdc-
grids-all-electric-society)
Cited by: §VII-E, §VII.
[82] D. Sun, D. Shapiro, B. Kim, J. Athavale, and R. Mercado (2023)
Open compute project: open rack v3 48v bbu (rev 1.4).
External Links: Link (https://www.opencompute.org/documents/open-rack-v3-
bbu-module-spec-1-4-pdf)
Cited by: §VII-B2, §VII-B3, §VII-B3, §VII-B, §VII-D, §VII-E, §VII.
[83] D. .Sun, D. Shapiro, B. Kim, J. Athavale, and R. Mercado (2022)
Open compute project: open rack v3 bbu shelf (rev 1.1).
External Links: Link (https://www.opencompute.org/documents/open-rack-v3-
bbu-shelf-spec-rev1-1-pdf-1)
Cited by: §VII-B3, §VII-B, §VII-D, §VII-E, TABLE III, §VII.
[84] R. Dimitrov, H. Petty, N. Srivastava, and M. Blake (2025)
How new gb300 nvl72 features provide steady power for ai.
External Links: Link (https://developer.nvidia.com/blog/how-new-gb300-nvl72
-features-provide-steady-power-for-ai)
Cited by: §VII.
[85] Analog Devices (2024)
ADI ocp orv3 bbu reference design.
External Links: Link (https://wiki.analog.com/resources/eval/adi-ocp-orv3-bbu
-reference-design)

Cited by: §VII-B, §VII-D, TABLE III.
[86] Roach, John (2022)
Microsoft datacenter batteries to support growth of renewables on
the power grid.
External Links: Link (https://news.microsoft.com/source/features/sustainabilit
y/ireland-wind-farm-datacenter-ups)
Cited by: §VII-B1, TABLE III.
[87] N. Collath, B. Tepe, S. Englberger, A. Jossen, and H. Hesse (2022)
Aging aware operation of lithium-ion battery energy storage
systems: a review.
Journal of Energy Storage 55, pp. 105634.
External Links: ISSN 2352-152X, Document (https://dx.doi.org/https%3
A//doi.org/10.1016/j.est.2022.105634)
Cited by: §VII-B2, §VII-D, TABLE III.
[88] S. Malla, Q. Deng, Z. Ebrahimzadeh, J. Gasperetti, S. Jain, P.
Kondety, T. Ortiz, and D. Vieira (2020)
Coordinated priority-aware charging of distributed batteries in
oversubscribed data centers.
In 2020 53rd Annual IEEE/ACM International Symposium on
Microarchitecture (MICRO),
pp. 839–851.
External Links: Document (https://dx.doi.org/10.1109/MICRO50266.2020.00
073)
Cited by: §VII-B2, §VII-E, TABLE III.
[89] A. Safari, H. Sorouri, A. Rahimi, and A. Oshnoei (2025)
A systematic review of energy efficiency metrics for optimizing cloud
data center operations and management.
Electronics 14 (11), pp. 2214.
Cited by: §VII-B1, TABLE III.
[90] Bjorlin, Alexis (2022)
OCP summit 2022: open hardware for ai infrastructure (grand teton /
orv3 rack and power).
External Links: Link (https://engineering.fb.com/2022/10/18/open-source/ocp-
summit-2022-grand-teton)
Cited by: §VII-B3, §VII-B, §VII-D.
[91] A. J. Crawford, Q. Huang, M. C.W. Kintner-Meyer, J. Zhang, D. M.
Reed, V. L. Sprenkle, V. V. Viswanathan, and D. Choi (2018)

Lifecycle comparison of selected li-ion battery chemistries under grid
and electric vehicle duty cycle combinations.
Journal of Power Sources 380, pp. 185–193.
External Links: ISSN 0378-7753, Document (https://dx.doi.org/https%3
A//doi.org/10.1016/j.jpowsour.2018.01.080)
Cited by: §VII-B2.
[92] UL Solutions
UL 9540a test method for battery energy storage systems (bess).
External Links: Link (https://www.ul.com/services/ul-9540a-test-method)
Cited by: §VII-B3.
[93] D. Genkina (2025)
Will supercapacitors come to ai’s rescue? power bursts in large ai
workloads can threaten to overwhelm the grid.
External Links: Link (https://spectrum.ieee.org/supercapacitor-2671883490)
Cited by: §VII-C1, §VII-D.
[94] Eaton
Supercapacitors in ai data centers.
External Links: Link (https://www.eaton.com/us/en-us/products/electronic-co
mponents/infographics/supercaps-in-ai-datacenters.html)
Cited by: §VII-C1, §VII-D.
[95] NVIDIA (2025)
NVML api reference guide - gpu deployment and management
documentation.
External Links: Link (https://docs.nvidia.com/deploy/nvml-api/group__nvmlDe
viceQueries.html#group__nvmlDeviceQueries_1gf754f109beca3a4a8c8c1cd65
0d7d66c)
Cited by: §VII-C2.
[96] J. Kaur and S. K. Bath (2025)
Harmonic distortion in power systems due to electronic control and
renewable energy integration: a comprehensive review.
Discover Electronics 2 (1), pp. 67.
External Links: Document (https://dx.doi.org/10.1007/s44291-025-00111-9),
ISSN 2948-1600
Cited by: §VII-E.
[97] A. Hassan, S. A. Khan, R. Li, W. Su, X. Zhou, M. Wang, and B.
Wang (2023)

Second-life batteries: a review on power grid applications,
degradation mechanisms, and power electronics interface
architectures.
Batteries 9 (12), pp. 571.
Cited by: §VIII, §IX-B3.
[98] B2U Storage Solutions (2025)
B2U storage solutions.
External Links: Link (https://www.b2uco.com/)
Cited by: §VIII.
[99] Element Energy (2025)
Element energy.
External Links: Link (https://elementenergy.com/)
Cited by: §VIII.
[100] Moment Energy (2025)
Moment energy.
External Links: Link (https://www.momentenergy.com/)
Cited by: §VIII.
[101] Smartville (2025)
Smartville.
External Links: Link (https://smartville.io/)
Cited by: §VIII.
[102] Redwood Energy (2025)
Fast, low-cost storage to power the age of ai and a changing grid.
External Links: Link (https://www.redwoodmaterials.com/news/redwood-ener
gy-fast-low-cost-storage-to-power-the-age-of-ai-and-a-changing-grid/)
Cited by: §VIII.
[103] S. e. al. Bobba (2018)
Life cycle assessment of repurposed electric vehicle batteries:
environmental and climate benefits of second-life use.
Journal of Energy Storage 19, pp. 213–225.
Cited by: §VIII.
[104] Crusoe Energy and Redwood Materials (2025)
Crusoe and redwood materials power ai/data center infrastructure
using second-life ev battery microgrid.
External Links: Link (https://www.crusoe.ai/resources/newsroom/crusoe-and-
redwood-materials-power-the-future-of-ai)

Cited by: §VIII.
[105] UL (2024)
UL 1974: evaluation for repurposing batteries.
External Links: Link (https://www.ul.com/services/second-life-electric-vehicle-
battery-repurposing-facility-certification)
Cited by: §VIII.
[106] H. Wang, M. Rasheed, R. Hassan, M. Kamel, S. Tong, and R. Zane
(2023)
Life-extended active battery control for energy storage using electric
vehicle retired batteries.
IEEE Transactions on Power Electronics 38 (6), pp. 6801–6805.
Cited by: §VIII-A.
[107] C. White, B. Thompson, and L. G. Swan (2020)
Repurposed electric vehicle battery performance in second-life
electricity grid frequency regulation service.
Journal of Energy Storage 28, pp. 101278.
External Links: Document (https://dx.doi.org/10.1016/j.est.2020.101278)
Cited by: §VIII-B.
[108] T. H. Norris, T. H. Profeta, D. Patino-Echeverri, and A. Cowie-
Haskell (2025)
Rethinking load growth: assessing the potential for integration of
large flexible loads in us power systems.
Report
Nicholas Institute for Energy, Environment & Sustainability, Duke
University, Durham, NC.
Note: Report NI R 25-01
External Links: Link (https://hdl.handle.net/10161/32077)
Cited by: §VIII-C.
[109] B. Roy (2025)New power players: how big tech firms are disrupting
energy markets(Website)
University of Houston Energy.
Note: Accessed: 2026-01-24
External Links: Link (https://www.uh.edu/energy/news/stories/2025/ow_big_t
ech_firms_are_disrupting_energy_hmarkets.php)
Cited by: §VIII-C.
[110] BloombergNEF (2025)

Lithium-ion battery pack prices fall to $108 per kilowatt-hour despite
rising metal prices.
External Links: Link (https://about.bnef.com/insights/clean-transport/lithium-io
n-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-blo
ombergnef/)
Cited by: §VIII-D1.
[111] A. Bach, S. Onori, S. Reichelstein, and J. Zhuang (2025)
Fair market value of used capacity assets: forecasts for repurposed
electric vehicle batteries.
Technical report
Technical Report Discussion Paper No. 25-065, ZEW – Centre for
European Economic Research.
Cited by: §VIII-D1.
[112] Internal Revenue Service (IRS) (2025)
Domestic content bonus credit.
External Links: Link (https://www.irs.gov/credits-deductions/clean-electricity-p
roduction-credit)
Cited by: §VIII-D1.
[113] L. C. Casals, B. A. García, and C. Canal (2019)
Second life batteries lifespan: rest of useful life and environmental
analysis.
Journal of environmental management 232, pp. 354–363.
Cited by: §VIII-D2.
[114] E. Martinez-Laserna, I. Gandiaga, E. Sarasketa-Zabala, J. Badeda,
D. Stroe, M. Swierczynski, and A. Goikoetxea (2018)
Battery second life: hype, hope or reality? a critical review of the
state of the art.
Renewable and Sustainable Energy Reviews 93, pp. 701–718.
Cited by: §VIII-D2.
[115] J. Neubauer and A. Pesaran (2011)
The ability of battery second use strategies to impact plug-in electric
vehicle prices and serve utility energy storage applications.
Journal of Power Sources 196 (23), pp. 10351–10358.
Cited by: §VIII-D2.
[116] J. Vetter, P. Novák, M. R. Wagner, C. Veit, K. Möller, J. Besenhard,
M. Winter, M. Wohlfahrt-Mehrens, C. Vogler, and A. Hammouche
(2005)

Ageing mechanisms in lithium-ion batteries.
Journal of power sources 147 (1-2), pp. 269–281.
Cited by: §VIII-D2.
[117] Z. Cao, M. Li, F. Lin, J. Jia, Y. Wen, J. Yin, and S. See (2025)
Transforming future data center operations and management via
physical ai.
arXiv preprint arXiv:2504.04982.
Cited by: §IX-A1.
[118] M. Li, R. Wang, R. Tan, and Y. Wen (2025)
Phythesis: physics-guided evolutionary scene synthesis for energy-
efficient data center design via llms.
arXiv preprint arXiv:2512.10611.
Cited by: §IX-A1.
[119] J. Chung, R. Wu, J. J. Ma, and M. Chowdhury (2026)
Where do the joules go? diagnosing inference energy consumption.
arXiv preprint arXiv:2601.22076.
Cited by: §IX-A2.
[120] R. Wu, J. Chung, and M. Chowdhury (2026)
Kareus: joint reduction of dynamic and static energy in large model
training.
arXiv preprint arXiv:2601.17654.
Cited by: §IX-A2.
[121] J. Chung, Y. Gu, I. Jang, L. Meng, N. Bansal, and M. Chowdhury
(2024)
Reducing energy bloat in large model training.
In Proceedings of the ACM SIGOPS 30th Symposium on Operating
Systems Principles,
pp. 144–159.
Cited by: §IX-A2.
[122] J. Chung, J. J. Ma, R. Wu, J. Liu, O. J. Kweon, Y. Xia, Z. Wu, and M.
Chowdhury (2025)
The ml. energy benchmark: toward automated inference energy
measurement and optimization.
arXiv preprint arXiv:2505.06371.
Cited by: §IX-A2.
[123] R. Frotscher, M. Rave, E. teNyenhuis, and P. Upadhyay (2021)
Reverse power flow impact on transformers.

Note: IEEE PES Transformers Committee Spring 2021 Meeting –
Tutorial / Technical PresentationSlides
External Links: Link (https://grouper.ieee.org/groups/transformers/subcommit
tees/standardsc/C57.133/F24-C57.133-ReversePowerFlowTutorial-%20teNyenh
uis.pdf)
Cited by: §IX-A3.
[124] L. Li, P. Yang, Y. Ju, Z. Hu, and Z. Wang (2025)
Coordinating multiple ups batteries in datacenter for load flexibility
and cost reduction.
SSRN Electronic Journal.
External Links: Document (https://dx.doi.org/10.2139/ssrn.5647230), Link
(https://ssrn.com/abstract=5647230)
Cited by: §IX-A6.
[125] M. Ko, J. W. Shim, and H. Zhu (2025)
Mitigation of datacenter demand ramping and fluctuation using
hybrid ess and supercapacitor.
arXiv preprint arXiv:2512.08076.
Cited by: §IX-A6.
[126] F. Farzan, K. Mahani, F. Farzan, R. Masiello, and W. Brown (2025)
Long-duration energy storage: planning and operation to enhance
power grid sustainability.
IEEE Energy Sustainability Magazine 1 (3), pp. 41–51.
External Links: Document (https://dx.doi.org/10.1109/ESM.2025.3606162)
Cited by: §IX-A7.
[127] D. Gu, X. Xie, G. Huang, X. Jin, and X. Liu (2023)
Energy-efficient gpu clusters scheduling for deep learning.
arXiv preprint arXiv:2304.06381.
External Links: 2304.06381, Link (https://arxiv.org/abs/2304.06381)
Cited by: §IX-B1.
[128] Y. Wang, Q. Guo, and M. Chen (2025)
Providing load flexibility by reshaping power profiles of large
language model workloads.
Advances in Applied Energy, pp. 100232.
Cited by: §IX-B1.
[129] D. A. Kez and A. Foley (2025)
Instability risks from programmable ai load ramping in low-inertia
grids.

SSRN Electronic Journal.
External Links: Document (https://dx.doi.org/10.2139/ssrn.5370875), Link
(https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5370875)
Cited by: §IX-B1.
[130] C. Crozier and M. Liska (2025)
The potential of data center energy demand to provide grid flexibility.
Current Sustainable/Renewable Energy Reports 12 (1), pp. 12.
Cited by: §IX-B1.
[131] Z. Liang, J. Chung, M. Chowdhury, J. Chen, and V. Dvorkin (2026)
GPU-to-grid: voltage regulation via gpu utilization control.
arXiv preprint arXiv:2602.05116.
Cited by: §IX-B1.
[132] S. Lu, C. Xiao, and Y. Weng (2026)
Dynamic load model for data centers with pattern-consistent
calibration.
arXiv preprint arXiv:2602.07859.
Cited by: §IX-B2.
[133] M. Mughees, Y. Li, Y. Chen, and Y. R. Li (2025)
Short-term load forecasting for ai-data center.
In 2025 IEEE Power & Energy Society General Meeting (PESGM),
pp. 1–5.
Cited by: §IX-B2.
[134] H. Jiang, B. Qu, J. Zhu, F. Zeng, X. Lin, and W. Zhong (2025)
HyperLoad: a cross-modality enhanced large language model-
based framework for green data center cooling load prediction.
arXiv preprint arXiv:2512.19114.
Cited by: §IX-B2.
[135] R. Mo, W. Lin, G. Liu, H. Liu, and L. He (2025)
Learning from imbalance: cross-server power prediction in large
data centers via domain adaptation regression.
Expert Systems with Applications 287, pp. 127845.
Cited by: §IX-B2.
[136] G. P. Kostenko (2024)
Accounting calendar and cyclic ageing factors in diagnostic and
prognostic models of second-life ev batteries.
Cited by: §IX-B3.

[137] X. Cui, M. A. Khan, S. Singh, R. Sharma, and S. Onori (2025)
Toward a bms 2.0 design framework: adaptive data-driven state-of-
health estimation for second-life batteries with bibo stability
guarantees.
IEEE Transactions on Transportation Electrification.
Cited by: §IX-B3.
[138] B. Strugnell-Lees, E. Evdokimova, and T. Wik (2024)
An entropy-based, self-adaptive predictive algorithm for battery
degradation.
Cited by: §IX-B3.
[139] European Union (2023)
Regulation (eu) 2023/1542.
External Links: Link (https://eur-lex.europa.eu/eli/reg/2023/1542/oj)
Cited by: §IX-B3.
[140] B. Xu, Y. Wang, Y. Dvorkin, R. Fernández-Blanco, C. A. Silva-
Monroy, J. Watson, and D. S. Kirschen (2017)
Scalable planning for energy storage in energy and reserve
markets.
IEEE Transactions on Power Systems 32 (6), pp. 4515–4527.
External Links: Document (https://dx.doi.org/10.1109/TPWRS.2017.268279
0)
Cited by: §IX-B4.
[141] N. Padmanabhan, M. Ahmed, and K. Bhattacharya (2020)
Battery energy storage systems in energy and reserve markets.
IEEE Transactions on Power Systems 35 (1), pp. 215–226.
External Links: Document (https://dx.doi.org/10.1109/TPWRS.2019.293613
1)
Cited by: §IX-B4.
[142] D. Rothmund, T. Guillod, D. Bortis, and J. W. Kolar (2019)
99% efficient 10 kv sic-based 7 kv/400 v dc transformer for future
data centers.
IEEE Journal of Emerging and Selected Topics in Power Electronics
7 (2), pp. 753–767.
External Links: Document (https://dx.doi.org/10.1109/JESTPE.2018.288613
9)
Cited by: §IX-B5.
[143] A. Sidorov, G. Zinoviev, and J. Petzoldt (2021)

Solid state transformer as a part electrical circuit for data center
application.
In 2021 IEEE 22nd International Conference of Young Professionals
in Electron Devices and Materials (EDM),
pp. 354–359.
Cited by: §IX-B5.
[144] A. Q. Huang (2016)
Medium-voltage solid-state transformer: technology for a smarter
and resilient grid.
IEEE Industrial Electronics Magazine 10 (3), pp. 29–42.
Cited by: §IX-B5.
[145] J. Irion, P. Wiesner, J. Bader, and O. Kao (2025)
Optimizing microgrid composition for sustainable data centers.
In Proceedings of the SC’25 Workshops of the International
Conference for High Performance Computing, Networking, Storage
and Analysis,
pp. 1990–1996.
Cited by: §IX-B6.
[146] Y. Zhang, H. Tang, H. Li, and S. Wang (2025)
Unlocking the flexibilities of data centers for smart grid services:
optimal dispatch and design of energy storage systems under
progressive loading.
Energy 316, pp. 134511.
Cited by: §IX-B6.
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