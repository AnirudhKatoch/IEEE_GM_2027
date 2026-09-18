| Page 1 of 7 |     |     |     |     |     | 2025-ICPSD25-0029 |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Challenges with Modern Data Centers, Design
Considerations and Recommended Power System
56303011.5202.45246SPCI/9011.01 :IOD | EEEI 5202© 00.13$/52/1-8080-5133-8-979 | )SPC&I( ecnerefnoC lacinhceT smetsyS rewoP laicremmoC dna lairtsudnI ts16 SAI/EEEI 5202
Studies
Guruprasad Ramani         Zahid Hussain William Brown                            Qais Alsafasfeh
Senior Member, IEEE Senior Member, IEEE Senior Member, IEEE Senior Member, IEEE
Schneider Electric Schneider Electric Schneider Electric Schneider Electric
6700 Tower Circle  7500 N Dobson Road,  6700 Tower Circle, 1975 Technology Park,
Nashville, TN, 37067 Scottsdale, AZ, 85256 Nashville, TN, 37067                       Troy, MI 48098
Abstract — Data Center power systems today face unique
serving as critical infrastructure for managing and processing
power demand challenges due to the proliferation of cloud  large amounts of data. They serve as critical infrastructure in
computing,  Artificial  Intelligence  (AI),  Internet  of  Things  the digital landscape, enabling organizations and individuals to
(IOT), as well as the intensifying demand for high bandwidth  access online services and applications efficiently. [4] defines
applications  which  cause  instantaneous  spikes  in  load  data centers as entities that include physical servers, virtual
fluctuations. In addition, resonance incidents observed recently  servers,  operating  systems,  applications,  middleware,  and
in new data centers are leading to power quality concerns.  application  services.  They  can  be  virtual  or  physical  and
Motivated by such challenges, this paper discusses the design  represent the highest level of resources offered by a cloud
considerations for modern data centers and suggests various  service provider. While the definition of a data center may
power system studies during engineering design to overcome  somewhat vary across literature, this paper adopts the definition
such challenges. This paper presents a literature review that  provided in [5] which describes a data center as a facility that
suggests  the  essential  power  system  studies  that  can  help  constitutes  a  specialized  infrastructure  that  centralizes  IT
identify the root cause of the power quality concerns, identify  operations  and  apparatus  for  data  and  application  storage,
potential points of failure during operations of an existing data  processing,  and  management.  A  modern  data  center  may
center power system, and allow designers and engineers to  consume over 100 MW electric power and uses an advanced
overcoming  such  challenges  when  designing  modern  data  power  distribution  system  to  ensure  reliability  and  power
center power systems and developing and refining equipment  quality [6]. The main components of a data center include the
specifications.  electrical  distribution  equipment,  cooling  systems,  servers,
storage devices, networking and communication equipment,
| Keywords—  | Artificial  |     | Intelligence,  |     | Coefficient  | of  |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | -------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
software, security systems and data center staff [7] [8].  Data
| Grounding,  | Data  | Center  | power  |     | system,  | Graphics  |     |     |     |     |     |     |     |
| ----------- | ----- | ------- | ------ | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Centers are categorized by the Uptime Institute on a scale from
| Processing  | Unit,  | Internet  | of           | Things,  | Information  |        |                  |                 |              |     |                 |     |       |
| ----------- | ------ | --------- | ------------ | -------- | ------------ | ------ | ---------------- | --------------- | ------------ | --- | --------------- | --- | ----- |
|             |        |           |              |          |              |        | tier  1  (least  | sophisticated,  | fundamental  |     | infrastructure  |     | with  |
| Technology  | Load,  | Power     | Electronics  |          | Non-linear   | Load,  |                  |                 |              |     |                 |     |       |
minimal redundancy) to tier 4 (most sophisticated, exhibiting
Point of Common Coupling, Sub-resonance, Power System
complete fault tolerance with redundancy integrated across all
Studies, Power Transients, Transient Stability.
components), where each tier delineates progressive levels of
reliability and operational continuity predicated upon power
|     |     | I   | INTRODUCTION  |     |     |     |               |            |              |     |                |     |      |
| --- | --- | --- | ------------- | --- | --- | --- | ------------- | ---------- | ------------ | --- | -------------- | --- | ---- |
|     |     |     |               |     |     |     | and  cooling  | pathways,  | maintenance  |     | capabilities,  |     | and  |
A. Background
redundancy attributes [10].
| Fundamental  | drivers    | of   | modern         | data  centers  | include             | the  |                |               |           |       |                    |     |        |
| ------------ | ---------- | ---- | -------------- | -------------- | ------------------- | ---- | -------------- | ------------- | --------- | ----- | ------------------ | --- | ------ |
|              |            |      |                |                |                     |      | By  2030,      | global  data  | traffic   | is    | forecasted         | to  | reach  |
| increasing   | necessity  | for  | data  storage  |                | and  computational  |      |                |               |           |       |                    |     |        |
|              |            |      |                |                |                     |      | approximately  | 5016          | exabytes  | (EB)  | or  approximately  |     | 5      |
capability, predominantly driven by the proliferation of cloud
zettabytes (ZB), with an annual increase of 55% from 2020
computing, AI, IoT, as well as the intensifying demand for
[11]. This growth reflects the rising demand for data transfer
| high-bandwidth  |     | applications,  | necessitating  |     | a   | resilient  |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
and digital services in future wireless networks. Globally data
infrastructure to effectively manage the substantial quantities of
centers are growing rapidly and significantly to handle the
| data  produced  | by  | users  | and  businesses.  |     | Historically,  | data  |     |     |     |     |     |     |     |
| --------------- | --- | ------ | ----------------- | --- | -------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
rapidly growing data traffic, while the energy demand of the
| centers  | were  physical  |     | spaces  engineered  |     | to  support  | an  |                |           |              |     |                |         |     |
| -------- | --------------- | --- | ------------------- | --- | ------------ | --- | -------------- | --------- | ------------ | --- | -------------- | ------- | --- |
|          |                 |     |                     |     |              |     | data  centers  | is  also  | increasing.  |     | The  expected  | energy  |     |
organization’s requirements; however, they have evolved into
consumption of data centers by 2030 is projected to exceed 1
| essential  | frameworks  | that  | support  | the  | digital  | economy,  |     |     |     |     |     |     |     |
| ---------- | ----------- | ----- | -------- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Peta-Watt hour (PWh) annually, driven by the exponential
especially in relation to AI and cloud computing. [1] defines
growth of data traffic and cloud computing technologies [12].
data centers as facilities that host server systems, computer
Data centers are anticipated to account for 4.5% of global
systems, and associated components such as cooling units,
energy consumption by 2025, with further increases expected
| redundancy  | power  | supplies,  | and  | power  | storage  | systems,  |           |                  |        |           |            |         |     |
| ----------- | ------ | ---------- | ---- | ------ | -------- | --------- | --------- | ---------------- | ------ | --------- | ---------- | ------- | --- |
|             |        |            |      |        |          |           | by  2030  | [13].  Electric  | Power  | Research  | Institute  | (EPRI)  |     |
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore.  Restrictions apply.

2025-ICPSD25-0029 Page 2 of 7
estimates that data centers in the USA could grow to consume regulatory standards; all of which necessitate meticulous
up to 9% of its electricity generation annually by 2030, up from evaluation and optimization to guarantee dependable data
4% of the total load in 2023. processing and storage functionalities. Once the maximum
design IT load capacity is determined after taking into
B. Challenges
consideration the future expansion, load calculations should
In a data center, more so in a co-location setting where the data consider adding the total mechanical cooling load and any
center infrastructure is shared by several users, users auxiliary load to support the IT infrastructure and to meet the
continuously adjust their demands on a shared system, with redundancy requirements required by the tier rating
little insight into the IT infrastructure installed due to which the classification. When designing the mechanical cooling system,
power demands of IT loads can exhibit considerable variability maximizing Power Usage Efficiency (PUE) should be
throughout the day since they are driven by diverse prioritized to improve the overall system efficiency, given the
requirements. Emerging workloads from Graphics Processing inefficiencies in a data center power system due to multiple
Units (GPU) display unique power consumption patterns, power conversions and losses.
frequently leading to significant and nearly instantaneous
Special considerations must be given to network symmetry,
spikes in power demand. With nearly every watt of electrical
load calculations, and load balancing across all three phases to
energy being processed by power conversion devices multiple
create a balanced system as evenly loaded across all three
times, data centers exhibit a very high density of power
phases as practical to improve system stability at low frequency
electronics, exceeding that of substantial wind and PV
to overcome low frequency resonance issues [14] [15]. Also,
installations and nearing the levels found in HVDC converter
special attention may need to be given to designing the
stations [14] [15]. Consequently, data centers are similarly
distribution network to reduce or minimize the zero-sequence
susceptible to the types of instability and resonance challenges
impedance of the power system in steady state -for example
that have recently beset the renewable energy and HVDC
wye connected loads like Power Supply Units (PSU), to
sectors in recent years [16], [17].
improve overall power system stability [15].
Considering the substantial and unavoidable expansion of
B. Technical Challenges with Modern Data Centers
modern data centers which highlights their critical significance;
and acknowledging their progressively vital function in the Modern data centers frequently experience load fluctuations
present-day global landscape, it is essential to confront the and instantaneous spikes which pose significant challenges to
advancing power demand challenges related to data centers data center power systems. Such rapid changes in power flow,
while addressing issues related to their power quality. frequency, or voltage can lead to system instability and cause
equipment failures unless the power system design is sound and
C. Approach
robust from a power system stability perspective. Instantaneous
Motivated by the above challenges, this paper discusses the spikes in load fluctuations may require early detection for
technical considerations to help define and refine equipment timely resource and capacity allocation to prevent impacts on
specifications and sizing for modern data center designs and system performance or cause equipment degradation and
recommends different power system studies to help overcome failures.
these challenges. The structure of this paper is as follows:
In addition to the high load variability, the modern data center
Section II discusses the technical considerations for designing
designers are also challenged with the problem of resonance.
modern data centers, followed by the technical concerns and
This phenomenon in power systems was recently observed in
challenges discussed above in greater detail. Section III briefly
new data centers at both low and high frequencies. Figures 1(a)
reviews the basic compliance studies for data centers. In
and 1(b) show one such example, discussed in [14]. Low
addition, it discusses the power system studies suggested for
frequency resonances in Figure 1(a) were at less than the second
overcoming the challenges discussed in section II and advanced
harmonic frequency, with an oscillation at 11 Hz seen in the
modeling considerations for power system stability analysis.
amplitude of both the current and voltage measured at the tap
Lastly, section IV presents the conclusions.
box to a server rack [14]. High frequency resonances in Figure
1(b) in the 5-10 kHz range were observed in some other data
II.DESIGN CONSIDERATIONS AND TECHNICAL CONCERNS centers [14]. Such resonance phenomenon may create
WITH MODERN DATA CENTERS instability in data center power systems during perturbations
which may be caused by frequent load variations and
A. Design Considerations
instantaneous spikes, eventually causing equipment failures or
General design considerations for data centers include system outages.
geographical positioning (availability of power, network
To overcome the complex challenges discussed above and to
connectivity, environmental conditions), electrical distribution
analyze the different power quality and power system
and cooling infrastructure, IT apparatus (servers, storage
parameters for modern data centers, different power system
solutions, networking equipment), security protocols,
studies are recommended as outlined in Section III.
redundancy measures, scalability considerations, energy
efficiency, financial implications, and compliance with
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore. Restrictions apply.

Page 3 of 7 2025-ICPSD25-0029
strength of the utility source, which typically provides higher
fault contributions compared to paralleled standby backup
generators necessary to support the data center power
systemin off-grid mode. In general, under any mode of
operation, contributions from all the paralleled sources
should be considered for a fault at any distribution bus for
worst-case scenario, depending on the power system
architecture adopted for the data center tier rating. For the
TCC analysis, once selectivity is achieved in grid connected
mode, the goal is to maximize selectivity and coordination in
off-grid mode, given that the fault contributions from
generators are still significant, although not as high as utility.
Figure 2 below illustrates a short circuit analysis for a power
system where renewable energy sources operate in parallel
with the utility, and a three-phase short circuit fault occurs on
the main bus. As highlighted in yellow below, all the sources
operating in parallel contribute to the total short circuit
Figure 1a. Low frequency resonance measured in data center power
current during the fault condition.
systems [14]
Figure 1b High frequency resonance measured in data center power
systems [14] Figure 2 - Example of a partial power system SLD depicting fault
contributions from all the sources operating in parallel contributing
III. RECOMMENDED POWER SYSTEM STUDIES AND ADVANCED to the fault during a three-phase short circuit fault on the main bus.
MODELLING CONSIDERATIONS FOR POWER SYSTEM STABILITY
B. Harmonics Analysis
ANALYSIS
Basic compliance studies for power systems comprise of Harmonic distortion is a subject of great interest in modern
short circuit(SC), time-current coordination(TCC), and arc power systems. Harmonic distortion results from non-
flash(AF) analyses. These studies enable the engineer of sinusoidal load currents that result of non-linear loads, such as
record to establish system reliability, selectivity, and safety drives, which employ power electronic devices to rectify the
during the design phases. However, for the modern data AC waveform. These devices draw non-sinusoidal currents
center facilities faced with challenges discussed in Section II, which, in turn, cause non-linear voltages to develop and
it is essential to consider studies such as harmonics analysis, propagate in the system. Power disturbances can greatly affect
Time Domain Load Flow (TDLF), and transient studies. The
utilization equipment, for example servers and computers with
relevance of each of these studies is discussed below.
PSUs and GPUs, adjustable speed motor drives etc. With the
A. SC, TCC and AF Analyses high-reliability requirements from data centers to maintain
Service Level Agreement (SLA), it is imperative that power
Data centers are typically powered from more than one
system disturbances, or potential disturbances, be mitigated to
resource. The primary resource is the electric utility while the
avoid downtime, equipment loss, and/or risk to human life.
backup sources are typically standby generators. For SC and
Therefore, for data centers which typically include non-linear
AF analysis, grid-connected mode generally represents the
loads, such as rectifiers, power electronic loads (PELs),
worst-case scenario compared to off-grid mode owing to the
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore. Restrictions apply.

2025-ICPSD25-0029 Page 4 of 7
variable frequency drives (VFDs), etc., a power quality and
harmonics analysis is recommended to mitigate the harmonics
and comply with the IEEE-519 standard. The IEEE-519
standard gives recommended limits for current distortion due to
consumer loads and voltage distortion in the utility supply
voltage, both referenced at the point of common
coupling(PCC). Figure 3 shows an example of a power system
one-line diagram depicting the current THD (%) and PF at
different branches and voltage THD (%) at different buses. The
results from the harmonics analysis can be utilized to include
any active or passive filters in the design and avoid any
harmonics related issues during the operation of the data center.
Figure 4 - Example of a partial power system SLD setup for TDLF
Analysis.
Figure 3 - An Example of a power system SLD depicting the current
THD (%) and PF at different branches and voltage THD (%) at
different buses
C. Time Domain Load Flow Analysis
Figure 5 – Plot of total power losses vs time for a given IEEE-34 bus
distribution power system test bed.
A TDLF analysis has diverse applications. It can be used to
identify potential points of failure during operations in an
existing data center power system, develop and refine
equipment specifications, and analyze load, source and system
behavior. It can offer a granular and detailed assessment of
power quality and power system parameters such as power
factor, active and reactive power, active and reactive power
losses as a function of time. Additionally, this analysis can help
the design engineers analyze and review the annual energy
consumption trends, daily power consumption trends, current
and voltage waveforms, harmonic distortions etc. at any node
of choice. This will facilitate root cause analysis of loading,
power factor and voltage issues and develop solutions to
overcome these issues. Figure 4 below shows an example of a
power system setup for performing a TDLF analysis. Figure 5
shows the plot of total system losses versus time, Figure 6
shows the plot of power factor at the source bus versus time,
Figure 6 – Plot of power factor at the source bus at the substation vs
and Figure 7 depicts the plot of phase-A voltage at a distribution
time for a given IEEE-34 bus distribution power system test bed.
bus versus time, for a given IEEE-34 bus distribution power
system test bed.
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore. Restrictions apply.

Page 5 of 7 2025-ICPSD25-0029
Figure 8 Current and voltage waveforms captured during a transient
analysis of an off-grid sudden switching-in event of an MV
transformer onto a power system in steady state.
E. System Grounding Study
Figure 7 – Plot of phase-A voltage at a load bus vs time for a given
A system grounding analysis is typically required for complex
IEEE-34 bus distribution power system.
power systems such as data centers since it affects the system's
D. Power System Transients Studies susceptibility to voltage transients and helps in defining the
system protection requirements. The system grounding
Rapid changes in power flow, frequency, or voltage can lead to arrangement is determined by the grounding of the power
system instability, which may potentially cause system source. For commercial and industrial systems, the types of
blackouts and/or equipment failures. Transient stability power sources generally fall into four broad categories, namely
analysis can be used to evaluate a power system’s dynamic the utility service, generator, transformer, and static power
response to perturbations and assess its steady state stability. It converters. The system grounding on the system fed by the
can also be used to assess various power system and power utility service or a customer-owned transformer is determined
quality parameters in data centers during instantaneous spikes by the transformer secondary winding configuration. In grid-
in load fluctuations to help develop equipment specifications connected mode, the utility typically serves as the system
and improve overall power system design. Advanced grounding reference for the power system. Since the loss of
impedance modeling of data center equipment for modern data utility causes the loss of the system grounding reference, a
centers may sometimes be necessary for performing system system grounding reference is required for the data center
stability analysis [14] [15]. Advanced modeling considerations power system to operate in off-grid mode. For generators, the
may include building an impedance model for PSUs, system grounding is determined by stator winding
developing building distribution network model by impedance configuration; for static power converter devices such as
scaling, system modeling, and model reduction based on rectifiers and inverters, the system grounding is determined by
equivalent source impedance and system stability analysis [15]. the output stage of the converter.
The analysis from such studies will help the engineers
understand the root cause of system issues like resonance at low There are three different types of system grounding, solidly
and high frequencies, and develop the overall data center power grounded systems, impedance grounded systems (including
system design and equipment specifications after taking low and high impedance grounded), and ungrounded systems.
advanced technical considerations and design aspects into Solidly grounded systems have no intentional impedances to
account that impact power system stability like network ground to limit fault currents, thus allowing higher fault current
symmetry, load calculations and balancing and minimizing magnitudes, facilitating protection operation and system device
zero sequence impedance of the overall network. Figure 8 coordination. Impedance-grounded systems allow control of
shows current and voltage waveforms captured during transient ground fault currents by introducing an intentional impedance
analysis of an off-grid sudden switching-in event of a MV in the ground fault current path. An ungrounded system is a
transformer onto a power system in steady state. system where there is no intentional connection of the system
to ground.
A system grounding analysis can be performed in ETAP or a
similar software if the impedances of the source and the
system are known. This study is used to establish a power
system’s grounding performance. The Coefficient of Ground
(COG) is defined below per IEEE C62.92.1-6 standard:
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore. Restrictions apply.

2025-ICPSD25-0029 Page 6 of 7
𝐶𝑜𝑒𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑡𝑜𝑓𝐺𝑟𝑜𝑢𝑛𝑑𝑖𝑛𝑔(𝐶𝑂𝐺) This paper discussed various power system studies
𝐻𝑖𝑔ℎ𝑒𝑠𝑡𝑈𝑛𝑓𝑎𝑢𝑙𝑡𝑒𝑑𝑃ℎ𝑎𝑠𝑒−𝑡𝑜−𝐺𝑟𝑜𝑢𝑛𝑑𝑉𝑜𝑙𝑡𝑎𝑔𝑒𝐷𝑢𝑟𝑖𝑛𝑔𝑎𝐺𝑟𝑜𝑢𝑛𝑑𝐹𝑎𝑢𝑙𝑡
= recommended for designing modern data center power systems
𝑃ℎ𝑎𝑠𝑒−𝑡𝑜−𝑃ℎ𝑎𝑠𝑒𝑉𝑜𝑙𝑡𝑎𝑔𝑒𝑤𝑖𝑡ℎ𝐺𝑟𝑜𝑢𝑛𝑑𝐹𝑎𝑢𝑙𝑡𝑅𝑒𝑚𝑜𝑣𝑒𝑑
in addition to general design considerations. In addition, special
Figure 9 Coefficient of Grounding formula as defined by IEEE considerations for modern data center power systems were
C62.91.1-6 standards. discussed, which may necessitate advanced modeling and
power system analysis to design data center power systems and
Effective grounding of power systems is characterized by a
develop equipment specifications.
COG<0.8. A COG lower than 0.8 is recommended to limit the
transient over voltages (TOVs) within the power system and
REFERENCES
can be achieved through proper system grounding design. [1] Ramamoorthy, Sethuramalingam., Abhishek, Asthana., S., Xygkaki., K.,
Lowering the COG results in lower TOVs, leading to an Liu., Jorge, Eduardo., Stephanie, R., Wilson., C., Bater. (2022). Energy
Demand Reduction in Data Centres Using Computational Fluid Dynamics.
improved overall system grounding performance. Figure 10
Springer proceedings in energy, 275-284.
shows an example of a system grounding analysis performed
for an off-grid power system supported by two generators in [2] Wenhong, Tian., Yong, Zhao. (2014). Resource Modeling and Definitions
parallel and renewable sources offline. A single-line-to-ground for Cloud Data Centers. 51-77.
(SLG) fault occurs on phase A of the 13.2 kV medium [3] C., DeCusatis. (2016). Data center architectures. 3-41.
voltage(MV) switchgear bus, leading to temporary over-
[4] Madhurima, Pore., Zahra, Abbasi., Sandeep, K., S., Gupta., Georgios,
voltages(TOVs) on phases B and C of the switchgear bus. The
Varsamopoulos. (2014). Techniques to Achieve Energy Proportionality in Data
MV switchgear is grounded using a zig-zag transformer
Centers: A Survey. 109-162.
through a neutral grounding resistor(NGR). Since the MV
[5] Yu-Chu, Tian., Jing, Gao. (2023). Data Centers. Signals and communication
switchgear being grounded through an NGR, the resulting
technology, 405-445.
TOVs across the line-neutral voltages on phases B and C due
phase-A ground fault are limited to 10.18kV and 12.75kV [6] J. Park. Data Center – Mechanical Specifications v1.0. [Online]. Available:
https://www.opencompute.org/wiki/Data Center/Specs And Designs
respectively, compared to 13.2 kV line-neutral voltages that
would have otherwise developed across phases B and C on an [7] Sahana, Shetty., H., K., Shashikala. (2023). An Innovation Development of
ungrounded power system. New Perspective of Efficient Approaches, Techniques and Challenges for Data
Centers. 1-6.
[8] Data Centre Infrastructure: Design and Performance.
[9] Ni, Made., Vifiana, Anggi, Suryanti., I., N., Suweden., I., Wayan., Arta,
Wijaya. (2023). Rancangan sistem kelistrikan data center berstandar tier 3 pada
perbankan. Jurnal Spektrum
[10] R., Arno., A., Friedl., P., Gross., Robert, Schuerger. (2012). Reliability of
Data Centers by Tier Classification. IEEE Transactions on Industry
Applications, 48(2):777-783.
[11] (2022). Reconfigurable Intelligent Surfaces [Scanning the Issue].
Proceedings of the IEEE, 110(9):1159-1163.
[12] Norbert, Schmitt., Richard, Vobl., Andreas, Brunnert., Samuel, Kounev.
(2021). Towards a Benchmark for Software Resource Efficiency. 179-182.
[13] Yanan, Liu., Xiaoxia, Wei., Jinyu, Xiao., Zhijie, Liu., Yang, Xu., Yun,
Tian. (2020). Energy consumption and emission mitigation prediction based on
Figure 10 System Grounding Analysis model Example – Transient
data center traffic and PUE for global data centers. 3(3):272-282.
over voltages observed on B & C Phases B & C of a 13.2kV MV
Switchgear Bus grounded using a zig-zag transformer through an [14] J. Sun, M. Xu, M. Cespedes and M. Kauffman, "Data Center Power System
NGR during an SLG fault on A phase for an off-grid power system Stability — Part I: Power Supply Impedance Modeling," in CSEE Journal of
Power and Energy Systems, vol. 8, no. 2, pp. 403-419, March 2022
islanded on paralleled generators.
[15] J. Sun, M. Mihret, M. Cespedes, D. Wong and M. Kauffman, "Data Center
IV. CONCLUSIONS
Power System Stability — Part II: System Modeling and Analysis," in CSEE
Globally data centers are growing rapidly as a result of Journal of Power and Energy Systems, vol. 8, no. 2, pp. 420-438, March 2022
exponential growth in cloud computing, AI, IoT, as well as the
[16] C. Buchhagen, M. Greve, A. Menze, and J. Jung, “Harmonic stability
intensifying demand for high-bandwidth applications. The
practical experience of a TSO,” in Proceedings of the 2016 Wind Integration
energy demand of the data centers is becoming a significant Workshop, Vienna, 2016, pp. 1–6.
share of the total global energy demand, requiring special
attention of the design engineers during the early design phases [17] J. Sun, M. J. Li, Z. G. Zhang, T. Xu, J. B. He, H. J. Wang, and G. H. Li,
“Renewable energy transmission by HVDC across the continent: system
to address the issues that were historically not of significant
concern, but are concerns with modern data centers. .
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore. Restrictions apply.

Page 7 of 7 2025-ICPSD25-0029
challenges and opportunities,” CSEE Journal of Power and Energy Systems,
vol. 3, no. 4, pp. 353–364, Dec. 2017.
[18] Dmitry, Duplyakin., Alexandru, Uta., Aleksander, Maricq., Robert, Ricci.
(2020). In Datacenter Performance, The Only Constant Is Change. 370-379.
[19] A., Faulkner., Sarath, B., Tennakoon., Moofik, Al-Tai., S., Mackay.
(2018). Load flow, short circuit analysis and load point reliability for Data
Centre power distribution networks. 1-8.
[20] Jian, Sun., Mingchun, Xu., Mauricio, Cespedes., David, Wong., Mike,
Kauffman. (2019). Modeling and Analysis of Data Center Power System
Stability by Impedance Methods.
[21] Karl, A., Homburg. (2008). Short-Circuit, Coordination, and Arc-Flash
Studies for Data Centers: Best Practices and Pitfalls.
[22] Christopher, Lee, Brooks. (2014). Integrating Arc-Flash Analysis: A Look
at Protective Device Coordination. IEEE Industry Applications Magazine,
20(3):14-23.
[23] Rehan, Arif., Muhammad, Usama., Farhan, Mahmood. (2017). Mitigating
arc flash hazard based on protective devices re-coordination in smart
distribution networks. JOURNAL OF FACULTY OF ENGINEERING &
TECHNOLOGY, 24(1):21-30.
[24] Robert, D., Giese., Erling, Hesla. (2020). Power Management For Data
Centers Challenges And Opportunities.
[25] S., Arivazhagan., P., Sivaraman. (2020). Investigation on power quality
assessment in data centre. International Journal of Advance Research, Ideas and
Innovations in Technology, 6(2):144-148.
[26] Alexandre, B., Nassif., Yang, Wang., Iraj, Rahimi, Pordanjani. (2018).
Power Quality Characteristics and Electromagnetic Compatibility of Modern
Data Centres. 1-4.
[27] Arash, Mousavi., Alireza, Yavarian., Valeriy, Vyatkin., Xiaojing, Zhang.
(2017). Power quality assessment of energy efficient cooling systems in data
centers. 7191-7196.
[28] P., Harinath., K., Kamaleswaran., M., Venkateshwaran., C., Sreenath., S.,
Prabhakaran., V., Kirubakaran. (2015). A critical analysis of Power Quality
issues in Data Center. 1-6.
[29] Bill, Brown. (2005). System Grounding and Ground-Fault Protection
Methods for UPS-Supplied Power Systems.
[30] Kazi, Sharif, Uddin, Ahmed., Math, Bollen., Manuel, Alvarez., Shimi,
Sudha, Letha. (2022). The Impacts of Voltage Disturbances Due to Faults In
the Power Supply System of A Data Center. 1-6.
[31] Rohit, Narayan. (2024). Indoor Grounding of Data Centers to IEC30129
and TIA607-E Standards. 1-5.
/20/$31.00 © IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:45 UTC from IEEE Xplore. Restrictions apply.