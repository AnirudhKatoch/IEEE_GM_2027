A Review of Power System Challenges Stemming
from Large AI Data Center Loads
44241311.5202.73756TSAEELDDIMTGSI/9011.01 :IOD | EEEI 5202© 00.13$/52/5-9373-5133-8-979 | )tsaE elddiM TGSI( tsaE elddiM - seigolonhceT dirG tramS evitavonnI no ecnerefnoC SEP EEEI 5202 Haris M. Khalid,
Venkateswara R. Seshmasetti,
|     |     |     |     |     | Abdulla Ismail  |     |     |     | College of Engineering & IT   |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ----------------------------- | --- |
Department of Electrical Engineering
|     |     |     |     | Department of Electrical Engineering  |     |     |     | University of Dubai, Dubai, UAE  |     |     |
| --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | -------------------------------- | --- | --- |
& Computing Sciences
|     |     |     |     |     | & Computing Sciences  |     |     |     | Department of Electrical and  |     |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | ----------------------------- | --- |
Rochester Institute of Technology
|     |     |     |     | Rochester Institute of Technology  |     |     |     | Electronic Engineering Science  |     |     |
| --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ------------------------------- | --- | --- |
Dubai, United Arab Emirates (UAE)
|     |     |     |     |     | Dubai, UAE  |     |     |     | University of Johannesburg,   |     |
| --- | --- | --- | --- | --- | ----------- | --- | --- | --- | ----------------------------- | --- |
vrs6329@rit.edu
|     |     |     |     |     | axicad@rit.edu  |     |     |     | Auckland Park, South Africa  |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ---------------------------- | --- |
mkhalid@ud.ac.ae
This review faced challenges due to the novelty of the
| Abstract—The deployment of  |     |     | Artificial  | Intelligence  | (AI)  |     |     |     |     |     |
| --------------------------- | --- | --- | ----------- | ------------- | ----- | --- | --- | --- | --- | --- |
data centers presents significant challenges for electrical power
topic, with significant research emerging only since 2023 [1].
systems. This proposed paper reviews the impacts of AI data
Comprehensive references were scarce, and currently, only
| center  loads  | on  | power  system  | operation  | by  systematically  |     |     |     |     |     |     |
| -------------- | --- | -------------- | ---------- | ------------------- | --- | --- | --- | --- | --- | --- |
the Alberta Electric System Operator (AESO) has published
analyzing technical documents, utility reports, and regulatory
|     |     |     |     |     |     | interconnection  |     | guidelines  [8].  | The  Electric  | Reliability  |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------- | -------------- | ------------ |
frameworks. Unlike traditional loads, AI data centers exhibit
Council of Texas (ERCOT) has shared valuable operational
distinct power dynamics, independent protection philosophies,
|     |     |     |     |     |     | data,  while  | the  | North  American  | Electric  | Reliability  |
| --- | --- | --- | --- | --- | --- | ------------- | ---- | ---------------- | --------- | ------------ |
and geographic concentration, which can destabilize both local
Corporation (NERC) is actively addressing these challenges
and system levels. Notable incidents, such as sharp power
with utilities and researchers. This synthesis offers insights
| fluctuations  | and  | load  disconnections,  | raise  | concerns  | about  |     |     |     |     |     |
| ------------- | ---- | ---------------------- | ------ | --------- | ------ | --- | --- | --- | --- | --- |
that validate theoretical predictions through field events.
| system  stability.  |     | This  proposed  | review  | aims  to  | synthesize  |     |     |     |     |     |
| ------------------- | --- | --------------- | ------- | --------- | ----------- | --- | --- | --- | --- | --- |
knowledge  on  this  emerging  topic  by  developing  a  multi- A. Motivation of the Proposed Work
| timescale  | framework,  | validating  | theoretical  | predictions,  |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- |
The rapid growth of AI data centers since the November 2022
classifying AI-induced oscillatory modes (0.5-23 Hz), examining
|     |     |     |     |     |     | rollout  of  | ChatGPT  | is  expected  | to  introduce  | significant  |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | ------------- | -------------- | ------------ |
stability effects in Inverter-Based Resources (IBR) systems, and
challenges for existing power system infrastructure. Recent
| proposing  | hierarchical  | mitigation  | strategies.  | These  | insights  |     |     |     |     |     |
| ---------- | ------------- | ----------- | ------------ | ------ | --------- | --- | --- | --- | --- | --- |
incidents, such as a simultaneous disconnection of 1,500 MW
provide vital guidance for operators and researchers on the
in the Eastern Interconnection in July 2024 and extended 14.7
impacts of AI data centers on the grid.
Hz oscillations in the Dominion Energy system, highlight
Index Terms—AI data centers, inverter-based resources,  these issues. These events indicate a shift from traditional
large loads, multi-timescale dynamics, oscillatory phenomena.  power  system  behavior,  with  increasing  IBR  penetration
exacerbating stability risks. Limited technical understanding
I.  INTRODUCTION
in existing literature, combined with the urgency of these
The  transformation  of  utility  power  systems  due  to  challenges, drives the need for a comprehensive review.
increased AI data center loads marks a significant shift in
power system evolution. Since the November 2022 public  B. Scope and Potential of the Work
deployment of ChatGPT, the infrastructure supporting these  The proposed paper examines the impacts of AI data
centers across temporal scales, ranging from microsecond
AI computations has expanded rapidly. The existing literature
|     |     |     |     |     |     | power  electronics  |     | interactions  | to  hourly  thermal  | cycling  |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------- | -------------------- | -------- |
indicates that AI data centers are distinct from traditional
patterns. The analysis encompasses 1) technical phenomena
| computing  | loads,  | referred  | to  as  “Large  | Loads,”  | [1]  |     |     |     |     |     |
| ---------- | ------- | --------- | --------------- | -------- | ---- | --- | --- | --- | --- | --- |
“programmable loads,” [2] or “negative generators,” [3] and  and  their  interconnections,  synthesis  of  real  operational
introduce unpredictable load variations. Data from Google's  incidents from multiple utilities, 2) evaluation of emerging
AI data center shows that these fluctuations can reach tens of  mitigation technologies, and 3) assessment of developing
| megawatts within sub-second intervals [4][5], while affecting  |     |     |     |     |     | regulatory frameworks.  |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
critical system oscillation modes.
This comprehensive review is expected to provide essential
This  proposed  review  highlights  the  concerning  guidance for power system planners, operators, regulatory
convergence of growing AI data center loads, which are  bodies, and researchers who must manage the challenges
primarily  power  electronic  loads,  with  inverter-based  arising  from  exponentially  growing  AI  computational
| resources (IBR) dominating power generation. This pairing  |     |     |     |     |     | demands.  |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
reduces system synchronous inertia and negatively impacts
C. Preceding Affined Reviews and Main Contribution of the
damping capability [3]. The July 2024 incident in the Eastern
| Interconnection,  |     | where  1,500  | MW  of  | data  center  | load  | Proposed Work  |     |     |     |     |
| ----------------- | --- | ------------- | ------- | ------------- | ----- | -------------- | --- | --- | --- | --- |
disconnected simultaneously, exemplifies the vulnerability to  This proposed paper advances the current understanding
through the following contributions that address critical gaps
cascading failures [6]. The incident revealed oscillations at
in existing literature (See Fig. I for the graphical abstract):
14.7 Hz for 2 hours, indicating a new phenomenon outside
traditional frequency ranges [7].
|     |     |     |     |     |     |   Multi-timescale  |     | Framework:  | Development  | of  a  |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------- | ------------ | ------ |
Technical analysis shows distinct differences between AI  comprehensive analysis demonstrating the cascade from
data centers and traditional computing loads, underscoring the  microsecond switching transients through millisecond
need for a deeper examination of their effects on power  protection operations and second-scale ramping to hourly
systems.  Operational  data  from  Google  indicates  power  thermal  patterns,  revealing  critical  interdependencies
fluctuations  reaching  tens  of  megawatts  in  sub-second  absent from single-scale studies.
intervals,  a  behavior  unseen  in  conventional  loads.  The    Operational Validation: Integration of field incidents
Eastern Interconnection incident exposes the limitations of  from Eastern Interconnection, Dominion Energy, and
existing analytical frameworks in addressing cascade failures.

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:56 UTC from IEEE Xplore.  Restrictions apply.
979-8-3315-3739-5/25/$31.00 ©2025 IEEE

ERCOT with theoretical analysis, providing empirical
|     |     |     |     |     |     |     | Wide area  |     | Examines a single  |     |     | Comprehensive  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------------ | --- | --- | -------------- |
validation of previously theoretical phenomena.  [4]  oscillation taxonomy
|     |     |     |     |     |     |     | oscillations  |     | phenomenon  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | --- | --- |
with interaction effects
  Oscillation Taxonomy: Systematic classification of AI-
Review documented
induced  oscillatory  phenomena  spanning  0.5-23  Hz,  [5]  Data center  No operational  system operational
|     |     |     |     |     |     |     | modeling  |     | validation  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | --- | --- | --- |
including  detection  methodologies  and  mitigation  incidents
| approaches.  |     |     |     |     |     | 1. AI is the acronym of artificial intelligence.   |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
  IBR-AI Data Center Interaction Analysis: Review
|            |           |            |             |     |          |     | II.  AI DATA CENTER DEMAND GROWTH AND  |     |     |     |     |     |
| ---------- | --------- | ---------- | ----------- | --- | -------- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
| revealing  | compound  | stability  | challenges  |     | in  IBR- |     |                                        |     |     |     |     |     |
CHARACTERISTICS
dominated grids, synthesizing findings that demonstrate
fundamental behavioral changes at high IBR penetration      This section comprises 1) quantitative growth trajectories
levels, particularly the critical 70% threshold identified in  and  uncertainty,  2)  geographic  concentration  and
recent studies where traditional mitigation approaches  consequences, and AI workload power signatures.
fail.
A. Quantitative Growth Trajectories and Uncertainty
  Hierarchical Mitigation: Formulation of time-matched
   The projection reports indicate significant uncertainty in AI
| solutions  | ranging     | from     | microsecond  |             | supercapacitor  |       |         |          |                     |     |         |         |
| ---------- | ----------- | -------- | ------------ | ----------- | --------------- | ----- | ------- | -------- | ------------------- | --- | ------- | ------- |
|            |             |          |              |             |                 | data  | center  | growth.  | The  International  |     | Energy  | Agency  |
| response   | to  hourly  | thermal  | storage,     | integrated  | with            |       |         |          |                     |     |         |         |
estimates global data center consumption will rise from 460
regulatory frameworks.
TWh in 2022 to over 1000 TWh by 2026 [9]. In the U.S.,
projections vary widely; IEEE PES anticipates 6.7-12% of
total electricity usage by 2028 [35], while the Lawrence
Berkeley National Laboratory forecasts 325 to 580 TWh [10].
A review by Kamiya and Coroam˘a suggests global energy
use at 300-380 TWh in 2023, with AI-specific consumption
potentially reaching 35-50% by 2030 [32]. EPRI estimates
range from 196 to 404 TWh by 2030 [11]. The variation in
|     |     |     |     |     |     | projections  | stems from AI  |     |     | efficiency improvements and  |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | ---------------------------- | --- | --- |
infrastructure limitations [31]. For instance, training GPT-4
consumed 62,318 MWh over 100 days [11], while inference
operations show a significant increase in energy use per query
compared to traditional searches [12][13]. Given billions of
queries daily, this leads to a substantial increase in power grid
demand.
B. Geographic Concentration and Consequences
|     |     |     |     |     |     |    The  | geographic  | distribution  |     | of  AI         | data  | centers  shows  |
| --- | --- | --- | --- | --- | --- | ------- | ----------- | ------------- | --- | -------------- | ----- | --------------- |
|     |     |     |     |     |     | unique  | patterns,   | influenced    |     | significantly  | by    | transmission    |
capacity and cooling resource availability. These factors may
lead to extreme concentration, creating vulnerabilities that
extend beyond mere capacity issues. Research highlights the
|     |     |     |     |     |     | risk  of  | cascade  | failures  | when  | clustered  |     | facilities  react  |
| --- | --- | --- | --- | --- | --- | --------- | -------- | --------- | ----- | ---------- | --- | ------------------ |
simultaneously to grid disturbances [5][14]. The July 2024
Eastern Interconnection event clearly demonstrated this, as
multiple substations disconnected within seconds [6].
C. AI Workload Power Signatures
Technical analysis reveals distinct power consumption
patterns in AI workloads, which impact the grid differently.
AI Training Workloads exhibit sustained high power with

fluctuations, modeled as pulse trains with 60-80% duty cycles
Figure 1. Graphical abstract of the proposed scheme.
[4][15]. Google's operational data reveals significant power
Table I represents the preceding affined reviews in this area,  swings due to alternating computer and networking phases,
the key  limitations,  and  possible  contributions  addressed  with forcing frequencies of 0.5-1.5 Hz overlapping with
through the proposed work.   traditional power system oscillation modes, posing potential
risks [5]. Fine-tuning AI operations exhibit higher-frequency
TABLE I. PRECEDING AFFINED REVIEWS AND CONTRIBUTIONS OF THIS
WORK1  variation (0.3-0.7 Hz) and lower-amplitude power variations.
Ref.  Focus Area  Key Limitations  Addressed Work  Inference  workloads  generate  burst  patterns  with  lower
Large load  No multi-timescale  Multi-timescale  average power but higher instantaneous ramp rates. Overall,
[1]
characteristics  technical analysis  framework  computational  resources  scale  dynamically  with  demand
Single-timescale  [15][16]. Measurements by Latif et al. on 8-GPU H100 nodes
Validates with real
[2]  Programmable  focus, lacks  incidents, covers all  show 8.4 kW max power draw versus a manufacturer rating
| load flexibility  |     | operational  |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
timescales
validation  of 10.2 kW, indicating capacity planning discrepancies [33].
|                  |     |                |     |                        | Review stability  | III. POWER SYSTEM CHALLENGES: AN INTEGRATED ANALYSIS  |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | ---------------------- | ----------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| AI load ramping  |     | Restricted to  |     | assessment, including  |                   |                                                       |     |     |     |     |     |     |
[3]
effects  frequency stability  voltage and oscillatory      This  section  comprises  1)  multi-time  scale  channel
|     |     |     |     |     | phenomena  | propagation,  |     | 2)  oscillatory  |          | phenomenon   |      | and  resonance  |
| --- | --- | --- | --- | --- | ---------- | ------------- | --- | ---------------- | -------- | ------------ | ---- | --------------- |
|     |     |     |     |     |            | mechanisms,   |     | 3)               | voltage  | sensitivity  | and  | protection      |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:56 UTC from IEEE Xplore.  Restrictions apply.

miscoordination, and 4) IBR integration compound effects,  milliseconds [19][25], aimed at protecting IT equipment, but
respectively.
implementation varies widely among facilities. ERCOT’s
data shows that identical voltage disturbances can lead to load
A. Multi-Time Scale Channel Propagation
reductions between 39% and 100% across different setups
The investigation highlights that AI data center challenges
[26]. Differences in UPS technology, such as automatic
span multiple time scales, with each influencing the others.
reconnection in static systems versus manual intervention in
This creates a cascade effect from microsecond-level power
Dynamic/Diesel Rotary UPS (DRUPS) systems, contribute to
| electronics  | switching  | to hour-scale   |     | thermal      | cycling.  | Key  |       |                |     |            |                |     |                 |
| ------------ | ---------- | --------------- | --- | ------------ | --------- | ---- | ----- | -------------- | --- | ---------- | -------------- | --- | --------------- |
|              |            |                 |     |              |           |      | this  | inconsistency  |     | [15][27].  | Additionally,  |     | variations  in  |
| phenomena,   | their      | grid  impacts,  |     | measurement  | needs,    | and  |       |                |     |            |                |     |                 |
protection philosophy and firmware configurations can lead
references are summarized in Table II. At the microsecond
to further discrepancies [18][24]. The interaction between
scale, power electronics in servers cause switching transients,
|           |      |                  |            |     |              |        | utility           | operations  |      | and  data  | center     | protections  | creates         |
| --------- | ---- | ---------------- | ---------- | --- | ------------ | ------ | ----------------- | ----------- | ---- | ---------- | ---------- | ------------ | --------------- |
| with  Li  | and  | Li  identifying  | bandwidth  |     | limitations  | [17].  |                   |             |      |            |            |              |                 |
|           |      |                  |            |     |              |        | vulnerabilities;  |             | for  | instance,  | utilities  | may          | attempt  three  |
Upstream AC/DC converters limit system response, resulting
automatic reclose operations for temporary faults. Some data
in a 30-50 millisecond lag between GPU load changes and
grid-visible power variations. These microsecond phenomena  centers count these as separate disturbances, resulting in
lead to millisecond-scale protection challenges, where voltage  disconnecting after the third attempt, even if disturbances are
disturbances lasting 42-66 milliseconds can trigger data center  within  tolerance  limits.  This  miscoordination  led  to  a
protection  [6].  The  interaction  between  utility  reclosing  significant 1500 MW disconnection event, highlighting the
schemes  and  the  "three  strikes"  disconnection  logic  systemic  risks  from  independently  developed  protection
| complicates these issues [18][19]. At the second-to-minute  |     |     |     |     |     |     | philosophies [6][19].  |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
scale, ramping poses significant operational challenges due to
software-driven load variations. NERC documents indicate  D. IBR Integration Compound Effects
ramp rates of 1.9 p.u. per second [1], with the xAI facility  The interaction between AI data centers and IBR-dominated
showing 10-20 MW variations multiple times per second [20],  power grids presents significant stability challenges. Al Kez
exceeding  traditional  generation  capabilities  and  posing  and Foley note that systems with approximately 70% IBR
serious frequency regulation issues [34].  penetration  can  experience  frequency  collapse  due  to
TABLE II. MULTI-TIMESCALE CHALLENGE2  unpredictable  AI  data  center  load  changes  [3],  whereas
synchronous systems manage these ramps effectively.
| Ref.  |     | Time Scale  |     | Primary Phenomenon  |     |     |     |     |     |     |     |     |     |
| ----- | --- | ----------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[17] [21]  µs  PE switching     The lack of inherent inertia in IBRs reduces synchronous
inertia, thereby decreasing the system's capacity to handle
| [6][7][8]  |     | ms  |     | Protection operations  |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
power imbalances caused by large AI loads. This results in
| [4][5][20][32]  |     | sec  |     | AI workload transitions  |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
higher rates of change of frequency (RoCoF) during load
| [16][22]  |     | min  |     | Thermal management cycling  |     |     |               |     |              |     |             |         |          |
| --------- | --- | ---- | --- | --------------------------- | --- | --- | ------------- | --- | ------------ | --- | ----------- | ------- | -------- |
|           |     |      |     |                             |     |     | transitions,  |     | approaching  |     | protection  | system  | limits.  |
| [15][23]  |     | H    |     | Training epoch patterns     |     |     |               |     |              |     |             |         |          |
Additionally, limited fault-current contributions from IBRs
|     | Grid Impact  |     |     | Measurement Challenge  |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
complicate protection coordination and heighten voltage-
| Harmonic generation  |     |     |     | Beyond SCADA capability  |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sensitivity issues [8], [28].
| Voltage-triggered disconnections  |     |     |     | Requires PMU/DFR equipment  |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Frequency deviations  Standard SCADA sufficient      Control  dynamics  between  remaining  synchronous
Reactive power variations  Correlation with temperature  generators and IBR controls can lead to complex interactions,
Sustained oscillations  Pattern recognition/source location  with  the potential  for undamped  oscillations  from grid-
2. DFR, PE, PMU, and SCADA are the acronyms of digital fault recorder, power electronics, phasor  following inverters [7], [17]. As IBR penetration increases
measurement unit, and supervisory control and data acquisition, respectively.
significantly, critical grid stability metrics for AI operations
B. Oscillatory Phenomenon and Resonance Mechanisms
degrade, with trends including a reduced frequency nadir,
| AI  data  | centers  | are  likely  | to  | introduce  | new  | oscillatory  |     |     |     |     |     |     |     |
| --------- | -------- | ------------ | --- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
extended voltage recovery times, and a shift in oscillation
phenomena in power systems, which will be a significant  damping from positive to negative at higher penetration
concern for future operations. Sub-synchronous oscillations,  levels. These factors raise concerns about system instability,
such as 14.7 Hz from UPS instability [7] and 23 Hz from large  particularly when combined with variable AI workloads
| loads [24], pose risks through torsional interactions that  |        |          |       |              |        |       | [5][21].  |     |     |     |     |     |     |
| ----------------------------------------------------------- | ------ | -------- | ----- | ------------ | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- |
| standard                                                    | SCADA  | systems  | fail  | to  detect.  | These  | high- |           |     |     |     |     |     |     |
TABLE III. OSCILLATORY PHENOMENON CLASSIFICATION3
frequency oscillations could challenge system-wide stability,
|                                                               |           |                |                |                   |                |              |       | Frequency   |     | Origin       |     | Detection   | Mitigation  |
| ------------------------------------------------------------- | --------- | -------------- | -------------- | ----------------- | -------------- | ------------ | ----- | ----------- | --- | ------------ | --- | ----------- | ----------- |
|                                                               |           |                |                |                   |                |              | Ref.  | Range       |     | Mechanism    |     | Method      | Approach    |
| requiring                                                     | advanced  |                | synchrophasor  |                   | measurements.  |              |       |             |     |              |     |             |             |
|                                                               |           |                |                |                   |                |              |       | 0.5 – 1.5   |     | AI training  |     | Standard    | Workload    |
| Additionally, forced oscillations from AI workloads, ranging  |           |                |                |                   |                |              | [5]   |             |     |              |     |             |             |
|                                                               |           |                |                |                   |                |              |       |             | Hz  | cycles       |     | PMU         | Scheduling  |
| from  0.5-1.5                                                 | Hz        | [5],  overlap  |                | with  inter-area  |                | oscillation  |       |             |     |              |     |             |             |
|                                                               |           |                |                |                   |                |              | [7]   | 10.0–11.0   |     | UPS control  |     | High rate   | Firmware    |
modes.  Research  indicates  that  distributed  data  center  Hz  instability  PMU  updates
deployments  amplify  these  oscillations  more  than  14.7–14.8  Limit cycle  Specialized  Controller
[7]
concentrated ones, contradicting conventional grid planning  Hz  from instability  monitoring  retuning
|     |     |     |     |     |     |     |       |        |     |                 |     | DFR   | Component  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | --------------- | --- | ----- | ---------- |
|     |     |     |     |     |     |     | [24]  | 23 Hz  |     | PE interaction  |     |       |            |
views. A comprehensive classification of these oscillatory  required  replacement
phenomena, including frequency ranges, origins, detection,  3. UPS is the acronym of uninterrupted power supply.
and mitigation methods, is provided in Table III.  IV. MITIGATION STRATEGIES: TECHNICAL AND
C. Voltage Sensitivity and Protection Miscoordination  INSTITUTIONAL DIMENSIONS
The voltage sensitivity of data centers presents a significant  This section comprises 1) hierarchical control and storage
vulnerability, influenced by various factors. The ITIC curve  architecture, 2) advanced grid codes and interconnection
indicates disconnection at 0.7-0.8 p.u. voltage for over 20  requirements, and 3) operational coordination paradigm.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:56 UTC from IEEE Xplore.  Restrictions apply.

A. Hierarchical Control and Storage Architecture  than treating data centers as passive loads, this framework
positions them as active grid participants. This setup could
| The  multi-timescale  |     | nature  | of  | challenges  | necessitates  |     |     |     |     |     |     |     |     |
| --------------------- | --- | ------- | --- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
further provide 1) ancillary services using backup generation
| hierarchical  | mitigation  |     | approaches.  | The  | investigation  |     |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | ------------ | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
revealed  successful  strategies  that  employ  different  and  storage  for  frequency  regulation  &  reactive  power
technologies, which are matched to specific timescales:  support,  2)  demand  response  leveraging  computational
|                     |     |     |            |                  |     |      | flexibility  | for  | load  | management,  | and  | 3)  | infrastructure  |
| ------------------- | --- | --- | ---------- | ---------------- | --- | ---- | ------------ | ---- | ----- | ------------ | ---- | --- | --------------- |
| Microsecond-Second  |     |     | Response:  | Supercapacitors  |     | and  |              |      |       |              |      |     |                 |
investment through co-funding transmission and generation
power electronics modifications address switching transients
|     |     |     |     |     |     |     | projects.  | Implementation  |     | faces  | both  | technical  | and  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------ | ----- | ---------- | ---- |
and brief power quality events. Google’s compiler-based  institutional barriers. Technical challenges include real-time
power  shaping  [4]  operates  at  this  scale,  redistributing  coordination  between computational scheduling and grid
computational  operations  to  smooth  power  profiles.  operations. This is not trivial. Institutional barriers involve
Additionally,  Google  found  that  simple  CPU  utilization  regulatory frameworks designed for unidirectional power
metrics can predict data center power consumption within 5%  flow and fixed load profiles.
accuracy for over 95% of their power distribution units,
TABLE IV. REGULATORY FRAMEWORK COMPARISON 4
despite complex AI hardware mixes [38]. It redistributes
|     |     |     |     |     |     |     |     |     |     | Key   | Enforcement  |     | Effectiveness  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | -------------- |
computational operations to smooth power profiles with less  Ref.  Utility  Requirements  Mechanism
than  1%  performance  impact.  This  approach  seems  Quantified  High specific
| promising.  |     |     |     |     |     |     |      |        |                | limits for  |            |     | thresholds  |
| ----------- | --- | --- | --- | --- | --- | --- | ---- | ------ | -------------- | ----------- | ---------- | --- | ----------- |
|             |     |     |     |     |     |     | [8]  | AESO   | oscillations,  |             | Mandatory  |     |             |
compliance
Second-Minute  Response:  Battery  energy  storage  ramping, and
systems appear to be effective here. Systems sized at 350-450  ride through
|     |     |     |     |     |     |     |     |     | Performance- |     |     |     | Medium  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | ------- |
MVA demonstrate effectiveness for frequency regulation  Economic
|     |     |     |     |     |     |     | [29]  | ERCOT   | based capacity  |     |     |     | voluntary  |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --------------- | --- | --- | --- | ---------- |
during AI load ramps [3]. Tesla’s Megapack deployments  allocation  incentives  participation
show a 70% reduction in power variability when properly  [1], [27],  Risk framework  Industry  developing
NERC
| controlled [20].  |     |     |     |     |     |     | [28]  |     | and guidelines  |     | collaboration  |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --------------- | --- | -------------- | --- | --- |
  4. AESO, ERCOT, and NERC are the acronyms of Alberta Electric System Operator, Electric
Reliability Council of Texas, and North American Electric Reliability Corporation, respectively.
| Minute-Hour  |     | Response:  | Thermal  |     | energy  | storage  |     |                                      |     |     |     |     |     |
| ------------ | --- | ---------- | -------- | --- | ------- | -------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|              |     |            |          |     |         |          |     | V.  SYNTHESIS AND FUTURE DIRECTIONS  |     |     |     |     |     |
leverages cooling system thermal mass for load shifting.
Zhang et al. [22] demonstrate that 600 m3 cold water storage  This section discusses the synthesis and future direction with
enables  energy  arbitrage  while  maintaining  temperature  1) an interconnected challenge framework, and 2) respective
| requirements. This is a clever use of existing infrastructure.   |     |     |     |     |     |     | research priorities.    |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
The  interaction  between  storage  layers  requires  A. Interconnected Challenge Framework
coordinated control, something often overlooked. Li and Li
The analysis highlighted that AI data center challenges are
| [17]  emphasize  | that  | bandwidth  |     | limitations  | of  upstream  |     |     |     |     |     |     |     |     |
| ---------------- | ----- | ---------- | --- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
interconnected across multiple time scales. Issues at the
converters constrain overall system response. Controlling
microsecond scale, such as power electronics constraints,
architecture must respect these fundamental limits.
affect millisecond protection system operations, which in
turn lead to second-scale ramping challenges and hour-scale
B. Advanced Grid Codes and Interconnection Requirements
thermal cycling. Solutions must be integrated across these
Regulatory frameworks are slowly evolving to address AI
scales; for example, compiler-based power shaping addresses
data center characteristics. Alberta’s AESO requirements [8]
|     |     |     |     |     |     |     | microsecond  | fluctuations  |     | but  | requires  | coordination  | with  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ---- | --------- | ------------- | ----- |
represent the first of their kind and the most comprehensive
|             |            |             |     |              |      |           | battery  | and  thermal  |     | storage  | systems  | [4].  | Regulatory  |
| ----------- | ---------- | ----------- | --- | ------------ | ---- | --------- | -------- | ------------- | --- | -------- | -------- | ----- | ----------- |
| regulatory  | framework  | available.  |     | It  clearly  | set  | out  the  |          |               |     |          |          |       |             |
frameworks need to account for these interactions while
Oscillation limits (<16 kW variation per 100 milliseconds),
| Ramping  | constraints  | (≤10  | MW/minute),  |     | Ride-through  |     | ensuring reliability.   |     |     |     |     |     |     |
| -------- | ------------ | ----- | ------------ | --- | ------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
obligations (0.15 seconds at <0.45 p.u. voltage), and the Most     Fig. 2 shows how microsecond power electronics switch
Severe Demand Contingency (MSDC) compliance for all  cascades  through  various  scales—from  millisecond
configurations.  ERCOT’s  Advanced  Remedial  Action  protection operations to hour-scale training patterns. This
Scheme  [29]  takes  a  different  approach.  It  introduces  cascading effect illustrates the need for coordinated multi-
performance-based  capacity  allocation.  Facilities  timescale approaches, as traditional single-scale solutions are
demonstrating  20-cycle  (333  millisecond)  response  inadequate. Furthermore, the spectrum of AI data center
capability gain access to full grid capacity. Slower responses  oscillations (0.1-23 Hz) overlaps with AI workload forcing
receive  proportionally  reduced  allocations.  This  creates  functions and traditional inter-area oscillations, emphasizing
economic incentives for flexibility investment, a market- the need for upgraded monitoring infrastructure and new
based solution that appears to be working. The analysis  frameworks for stability assessment.
| presented  | in  [37]  | indicates  | Virtual  | Power  | Plants  | could  |     |     |     |     |     |     |     |
| ---------- | --------- | ---------- | -------- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
B. Research Priorities
| provide  | 40-60%  | cost  savings  | compared  |     | to  conventional  |     |     |     |     |     |     |     |     |
| -------- | ------- | -------------- | --------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
alternatives. Table IV compares the regulatory frameworks  The analysis found critical knowledge gaps not covered in the
currently being developed by different utilities, highlighting  literature, particularly regarding the simultaneous operation
the variation in requirements, enforcement mechanisms, and  of multiple AI data centers on standard transmission systems
observed  effectiveness  in  addressing  AI  data  center  and their systemic effects. Koomey’s analysis revealed that
integration challenges.  national  projections  can  obscure  significant  regional
variations, with some utility forecasts regularly surpassing
C. Operational Coordination Paradigm  actual generation [36]. The potential for interference patterns
The U.S. Department of Energy’s “shared energy economy”
remains uncertain, and the scalability of potential mitigation
| concept  | [30]  represents  |     | something  | new,  | a  fundamental  |     |             |           |     |              |                |     |              |
| -------- | ----------------- | --- | ---------- | ----- | --------------- | --- | ----------- | --------- | --- | ------------ | -------------- | --- | ------------ |
|          |                   |     |            |       |                 |     | approaches  | requires  |     | validation,  | necessitating  |     | testing  of  |
reconceptualization of data center-grid relationships. Rather
solutions demonstrated at single facilities at the system scale.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:56 UTC from IEEE Xplore.  Restrictions apply.

[11] Electric Power Research Institute, “Powering intelligence: Analyzing
artificial intelligence and data center energy consumption,” EPRI Tech.
Rep. 3002028905, May 2024.
[12] M. Lauby,” Reliability Implications: Integrating Large Loads Into Bulk
Power [Hot Topic],” in IEEE Power and Energy Magazine, vol. 23, no.
5, pp. 24-26, Sept.-Oct. 2025.
[13] J. Smith, “GPU Data Centers Strain Power Grids: Balancing AI
Innovation and Energy Consumption,” Unite.AI, Oct. 15, 2024.
[Online]. Available: https://www.unite.ai/gpu-data-centers-strain-
powergrids-balancing-ai-innovation-and-energy-consumption/
[14] [NERC, “Large Loads Task Force materials,” Jun. 18, 2025. [Online].
Available: https://www.nerc.com/comm/RSTC/Pages/LLTF.aspx
[15] A. Jim´enez-Ruiz and F. Milano, “Data center model for transient
stability analysis of power systems,” arXiv preprint arXiv:2505.16575,
Figure 2. AI data centers multi-scale challenge cascade. May 2025.
[16] Q. Zhang et al., “Integration and interaction of next-generation AI-
VI. CONCLUSION focused data centers with smart grids and district energy systems,”
Appl—energy, vol. 375, p. 124511, Feb. 2025.
This proposed review highlights that AI data centers signify a [17] X. Li and Y. Li, “AI load dynamics–A power electronics perspective,”
significant shift in power system loads, going beyond mere arXiv preprint arXiv:2502.01647, Feb. 2025.
growth. Their unique characteristics and integration with [18] D. Bauer, “Data center event - Recent large load loss event,” NERC
Presentation, ERCOT LFLTF, Mar. 2025.
inverter-based resources (IBR) present challenges that current
[19] CIGRE/IEEE, “Large loads and their impact on the grid: An emerging
infrastructure and practices struggle to address. reliability risk,” Webinar Presentations, May 2025.
[20] NERC, “LLTF April meeting & technical workshop presentations,”
Key takeaways include the need for hierarchical solutions Apr. 10, 2025. https://www.nerc.com/comm/RSTC/Pages/LLTF.aspx
due to the multi-timescale nature of these challenges; no single [21] PSERC, G. E. C. Reyes, C. Tomlin, R. Dye, and D. Callaway, “Effects
technology can provide complete mitigation. The shift to IBR- of Dynamic Power Electronic Load Models on Power Systems
Analysis Using ZIP-E Loads,” 56th North American Power
dominated grids will require a fundamental reevaluation of
Symposium (NAPS), El Paso, TX, USA, 2024, pp. 1-6
solutions originally designed for synchronous systems. [22] Y. Zhang et al., “Unlocking the flexibilities of data centers for smart
grid services: Optimal dispatch and design of energy storage systems
To successfully integrate AI data centers as proactive grid under progressive loading,” Appl. Energy, vol. 364, p. 123156, 2025.
participants, technical innovations, regulatory changes, and [23] V. Govind et al., “Comparing power signatures of HPC workloads:
new market mechanisms are essential. Future power systems Machine learning vs simulation,” in Proc. SC23, Denver, CO, USA,
Nov. 2023, pp. 1–14.
must factor in AI workload characteristics and develop new
[24] ERCOT, “Large load oscillation event,” LFLTF Presentation, Mar.
modeling frameworks tailored to these demands, alongside 2025. https://www.ercot.com/calendar/03042025-LFLTF-Meeting
specific technical standards for computational loads. [25] CIGRE/IEEE, “NGN webinar presentations on large loads and grid
Collaboration among utilities, data center operators, and impact,” May 21, 2025.
[26] P. Gravois, “ERCOT large load loss/reduction events 2020-2024,”
researchers will be crucial in tackling these significant
ERCOT LFLTF Presentation, Mar. 2025.
challenges. https://www.ercot.com/calendar/03042025-LFLTF-Meeting
[27] NERC, “LLTF July meeting & technical workshop presentations,” Jul.
ACKNOWLEDGMENT 24, 2025. https://www.nerc.com/comm/RSTC/Pages/LLTF.aspx
[28] ERCOT, “Data center operations task force,” Large Flexible Load Task
The authors thank the NERC Large Load Task Force
Force Presentation, Mar. 2025.
members for their insights during the workshop discussions. https://www.ercot.com/calendar/03042025-LFLTF-Meeting
[29] ERCOT, “Planning guide revision request: Incorporating advanced
REFERENCES technology options for generator and large load interconnections,”
PGRR, 2024.
[1] North American Electric Reliability Corporation, “Characteristics and
[30] U.S. Department of Energy SEAB, “Recommendations on powering
risks of emerging large loads,” NERC White Paper, Jul. 2025.
artificial intelligence and data center infrastructure,” DOE Tech. Rep.,
[2] D. Al Kez and A. Foley, “Programmable load risks and system
Jul. 2024.
flexibility: Rethinking Data Center Participation in Modern Power
[31] J. Norris et al., “Rethinking load growth: Assessing the potential for
Systems,” SSRN, May 30, 2025. [Online]. Available:
integration of large flexible loads in US power systems,” Energy
https://ssrn.com/abstract=5395002
Institute at Haas, Working Paper, 2025.
[3] D. Al Kez and A. Foley, “Instability Risks from Programmable AI
[32] G. Kamiya and V. Coroam˘a, “Data center energy use: Critical review
Load Ramping in Low-Inertia Grids,” SSRN, July 29, 2025. [Online].
of models and results,” Energy Efficiency, vol. 18, no. 1, pp. 1–22,
Available: https://ssrn.com/abstract=5370875
2025.
[4] H. Gan and P. Ranganathan, “Mitigating power and thermal
[33] Latif I, Newkirk AC, Carbone MR, Munir A, Lin Y, Koomey J, Yu X,
fluctuations in ML infrastructure,” Google Cloud Blog, Feb. 12, 2025.
Dong Z. “Empirical Measurements of AI Training Power Demand on
[5] M.-S. Ko and H. Zhu, “Wide-area power system oscillations from
a GPU-Accelerated Node.”, arXiv preprint arXiv:2412.08602. Dec.
large-scale AI workloads,” arXiv preprint arXiv:2508.16457, Aug.
2024
2025.
[34] Z. Zhao, E. Rrapaj, S. Bhalachandra, B. Austin, H. A. Nam, and N.
[6] NERC, “Incident Review: Considering Simultaneous Voltage-
Wright, “Power analysis of NERSC production workloads,” in Proc.
Sensitive Load Reductions,” North American Electric Reliability
SC ’23 Workshops Int. Conf. High Performance Comput., Network,
Corporation, Incident Review Rep., Jan. 2025.
Storage, Anal., Denver, CO, USA, Nov. 2023, pp. 1279–1287.
[7] C. Mishra, L. Vanfretti, J. Delaree, T.J. Purcell, K. D. Jones,
[35] B. Chalamala et al., “Data Center Growth and Grid Readiness
“Understanding the inception of 14.7 Hz oscillations emerging from a
(TR131),” IEEE Power and Energy Society, Technical Report TR131,
data center,” Sustainable Energy, Grids and Networks, Vol 43, May
May 2025
2025.
[36] J. Koomey and Z. Schmidt, “Electricity Demand Growth and Data
[8] Alberta Electric System Operator (AESO), Connection Requirements
Centers: A Guide for the Perplexed, Bipartisan Policy Center”,
for Transmission-Connected Data Centers, Alberta Electric System
Washington, D.C., USA, Feb. 2025.
Operator, Alberta, Canada, Aug. 2025.
[37] S. Newell, R. Hledik, and J. Pfeifenberger, “Meeting Unprecedented
[9] International Energy Agency, “Energy and AI,” IEA Special Report,
Load Growth: Challenges & Opportunities”, The Brattle Group, Apr.
Apr. 2025. [Online]. Available: https://www.iea.org/reports/energy-
2025.
and-ai
[38] Google Research, “Power modeling for effective datacenter planning
[10] A. Shehabi et al., “2024 United States data center energy usage report,”
and compute management,” in Proc. ISCA, Orlando, FL, USA, Jun.
Lawrence Berkeley National Laboratory, Tech. Rep. LBNL-2024, Dec.
2024, pp. 1–12.
2024.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:56 UTC from IEEE Xplore. Restrictions apply.