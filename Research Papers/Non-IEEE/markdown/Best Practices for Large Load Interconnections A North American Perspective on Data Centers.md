21, rue d’Artois, F-75008 PARIS  CIGRE US National Committee
http://www.cigre.org

2025 Grid of the Future Symposium

Best Practices for Large Load Interconnections: A North American Perspective
on Data Centers

Rafi Zahedi, Amin Zamani, Rahul Anilkumar
Quanta Technology, LLC

SUMMARY
Large loads are expanding rapidly across North America, led by data centers, cryptocurrency mining,
hydrogen production facilities, and heavy-duty charging stations. Each class presents distinct electrical
characteristics, but data centers are drawing particular attention as AI deployment drives unprecedented
capacity growth. Their scale, duty cycles, and converter-dominated interfaces introduce new challenges
for transmission interconnections, especially regarding disturbance behavior, steady-state performance,
and operational visibility.
This paper reviews best practices for large-load interconnections across North America, synthesizing
utility  and  system  operator  guidelines  into  a  coherent  set  of  technical  requirements.  The  approach
combines handbook and manual analysis with cross-utility comparisons and an outlook on European
directions. The review highlights requirements on power quality, telemetry, commissioning tests, and
protection coordination, while noting gaps in ride-through specifications, load-variation management,
and post-disturbance recovery targets. Building on these findings, the paper proposes practical guidance
for developers and utilities.

KEYWORDS
Artificial intelligence, data center, grid interconnection, large loads, interconnection requirements

1.  INTRODUCTION

With the rapid transformation of the North American electric grid, emerging large loads, such as data
centers,  cryptocurrency  mining,  hydrogen  production,  and  heavy-duty  EV  charging,  are  requesting
interconnections at unprecedented scale and speed, often exceeding today’s largest operating facilities.
Early events associated with these types of loads already highlight reliability risks: in July 2024, a 230
kV fault in the Eastern Interconnection tripped 1,500 MW of  large data center loads, briefly raising
frequency  and  voltage  [1]–[2],  [3].  Between  late  2023  and  early  2025,  ERCOT  and  the  Eastern
Interconnection recorded 25 crypto-mining load losses of 100–400 MW each [2].
Artificial intelligence (AI),  cloud services, and high-performance computing are  among the  primary
drivers of rapid data center expansion. In 2024, global data generation exceeded 149 zettabytes, fueled
by AI-enabled applications, widespread digitalization, and the proliferation of connected devices [4].
The U.S. leads with 40% of global capacity, as electricity demand from data centers rose from 58 TWh
in 2014 to 176 TWh in 2023, with the US Department of Energy projecting 325–580 TWh by 2028 [5].
During this period, workloads shift toward inference (80% to 85%) and diversify geographically, with
edge computing projected to handle half of AI processing by 2028 [7].
Data centers are a distinct class of large electrical load. Unlike crypto mining or traditional industrial
processes, their demand is computationally driven with a constant baseline but sudden spikes from AI
training and real-time inference [6]. These bursty patterns make data centers uniquely challenging for
maintaining power quality and ensuring grid stability and integration.

Interconnection requests are now  outpacing legacy processes, creating reliability, study, and process
challenges for utilities and Independent System Operators (ISOs). From a performance standpoint, fast
ramps  and  step  changes  can  trigger  large-scale  disconnections  if  ride-through  and  reclosing
requirements are not properly defined [7]. Without adequate filtering, power-electronic interfaces can
introduce harmonic distortion, phase imbalance, and broader power quality concerns. These pressures
underscore the need for harmonized technical requirements at the point of interconnection (POI).
This  paper  provides  a  comparative  analysis  of  large-load  interconnection  requirements  across  U.S.
power entities, with emphasis on  technical  requirements. By  extracting explicit numeric  limits from
utility and ISO guidance, the study highlights areas of convergence and divergence in current practice.
The work contributes a framework and visual benchmarks designed to support both policy development
and practical planning for integrating data center loads.

2.  USA LARGE LOAD TECHNICAL INTERCONNECTION REQUIREMENTS

The operational concerns of large loads are distinct from traditional motor-dominated load. To ground
the  discussion  in  practice,  this  section  collates  utility  and  ISO  requirements  into  discipline-specific
primers, followed by comparative tables that report the most prescriptive, numeric obligations where
they exist.

Figure 1 groups the interconnection requirements into eight broad categories: load management, power
quality,  voltage  ride-through  (VRT),  frequency  ride-through  (FRT),  post-disturbance  recovery,
protection  requirements,  operational  communications  and  control  with  compliance,  and  study  and
modeling requirements. Table 1 compiles guidance from AEP, Dominion, ERCOT, Ameren (MISO),
PG&E, Southern Company, and SPP, using a POI-based frame that emphasizes explicit numerical limits
and restoration targets. This structure allows direct comparison while retaining each entity’s terminology
and scope.

Figure 1. Technical Requirements Categories Investigated in This Paper

                       oad  anagement  si e  smoothing  and ramping   oltage Ride through Po er  ualit   Po er  actor   armonics  Flic er R C   n alance  Transient   perational Communications  Control   Compliance Post  istur ance  oad Recover   tud   odeling Requirements Protection  Frequenc  Ride through

2.1.

Load Management (size, smoothing, and ramping)

As noted earlier, AI training facilities create rapid swings in demand, underscoring the need for clear
POI envelopes and staged restoration profiles. Interconnection requirements should therefore link step
and ramp limits with  reconnection staging, supported by  high-resolution telemetry and validation to
align operational control with the documented risks of large loads [1]. Further, smoothing strategies are
required to dampen fluctuations and stabilize load curves [8].

Entities differ considerably in how  they define “large load,” as shown in  Figure 2. Dominion sets a
threshold for power-electronic interface large loads at ≥50 MW, while ERCOT classifies ≥75 MW at a
single site as large and applies a 25 MW visibility threshold at substations. This means that if multiple
facilities behind the same transmission substation together exceed 25 MW, ERCOT requires enhanced
observability (e.g.,  telemetry,  status,  coordination)  even  if  each  facility is  below  75  MW.  Southern
Company defines transmission-connected (>40 kV) large loads as ≥50 MW, and SPP designates high-
impact large loads as >10 MW at 69 kV or >50 MW at higher voltages. By contrast, AEP, Ameren
(MISO), and PG&E do not set a fixed MW threshold.

As  shown in  Table  1, Southern Company is the only company that enforces a  numeric cap  of ≤  20
MW/min for load ramping under normal operation. AEP requires submission of a Load Ramp Schedule,
ERCOT mandates a Load Commissioning Plan consistent with Large Load Interconnection Study limits,
Dominion specifies a site-specific staged reconnection plan, and SPP calls for constant-current (rather
than constant-power) control during disturbances. Other entities focus more on planning data, control-
center coordination, and forecasting rather than prescribing explicit caps.

Figure 2.  arge  oad  e inition     i  erent Entities

2.2.

Power quality

Interconnection  requirements  generally  pair  explicit  power  quality  (PQ)  limits  at  the  POI  with
monitoring  provisions  so  disturbances  can  be  detected  before  affecting  other  customers  or  system
performance [9]. Table 1  shows that Dominion requires ≤3% instantaneous voltage fluctuation at the
POI  along  with  permanent metering that  records  time-stamped, high-resolution logs  for  compliance
audits. Ameren adopts IEEE 519 for harmonics mitigation and IEEE 1453 for flicker and rapid voltage
change (RVC).  PG&E  enforces Rule  2  limits (THD  ≤5%, ~10% imbalance), CAISO  applies power
factor  limits  at  POI,  and  Southern  Company  requires  harmonic  spectrum  out  to  the  50th  order,
permanent monitors, and enforceable mitigation. AEP references a designated measurement point with
IEEE 1453 for flicker/RVC.

Among these, only Dominion and Southern Company explicitly require permanent PQ monitoring at
the POI. Ameren may install monitors but does not mandate permanent recorders, PG&E enforces PQ
limits  without  specifying  devices,  and  AEP  identifies  a  measurement  point  without  prescribing  a
permanent meter. ERCOT and SPP, based on the publicly available materials, do not require load-side
PQ monitoring.

Ta le 1.  ummar  o  comparative anal sis o  load management and po er qualit   or large load interconnection

Categor

Entit

AEP [10]

 ominion
[11]

ERC T [12],
[13], [14], [15]

 I
Ameren [16]

PG E [17],
[18], [19],
[20], [21]

 outhern
Compan [22],
[23]

 PP [24]

 oad  anagement  si e  smoothing  and
ramping
• Definition: AEP treats projects on a case-by-case
basis.
• Customer submits a Load Ramp Schedule
describing step magnitudes, cadence,
reconnect/dropout thresholds, and delays; AEP
checks steps/ramps against flicker and RVC
planning limits and may require mitigation.
• Definition: ≥50 MW but may designate <50 MW
based on characteristics or location.
• Customer should provide site-specific data (load
type and transfers) and a staged reconnection plan.
• Definition: ≥75 MW at a single site; visibility
threshold ≥25 MW at a common substation.
• Behavior governed by the commissioning plan,
set by the transmission service provider based on
study limits; no explicit step/ramp is defined.
• Definition: not a fixed MW threshold; procedures
apply to any transmission-connected end user.
• Application includes MW/MVAr/PF, max
demand, actual peak (if applicable), 10-year
forecast, and unique operating characteristics.

• Definition: not specified; no step/ramp caps are
published.
• All connections/separations are coordinated with
the PG&E control center; remedial action schemes
may be required if studies identify them.
• Definition: ≥50 MW at >40 kV; SCT (Southern
Company Transmission) may designate smaller
facilities based on characteristics or location.
• Maximum active-power ramp ≤ 20 MW/min
under normal operation; settings are reviewed and
demonstrated; energization inrush and steps must
respect RVC limits.
• Definition: >10 MW at 69 kV or >50 MW at
higher voltages.
• For electronic loads, operate in constant-current
mode during disturbances and avoid constant-
power mode; no steady-state step/ramp defined.

2.3.

Voltage ride-through

Po er  ualit

• PQ is assessed at an AEP-designated point of
measurement (often the POI).
• Flicker/RVC must meet IEEE 1453; harmonic
expectations are reviewed for modern electronic
equipment.

• Instantaneous voltage fluctuation at the POI ≤ 3%.
• Permanent POI PQ metering with time-stamped logs (P,
Q, PF, harmonics to 50th, Pst/Plt, RVC, unbalance,
transients, frequency) and ≥90-day retention.
NA

• Harmonics must meet IEEE 519; Ameren may install
POI meter; customer must mitigate if limits are violated.
• Flicker/RVC assessed to IEEE 1453; e.g., 2.0% critical-
bus dip is marginal and may require mitigation.
• PF outside 95% lag–95% lead requires customer-side
correction. Persistent PQ non-compliance can lead to
disconnection.
• Enforces Electric Rule 2 at the POI; total voltage THD
≤ 5% and the customer funds mitigation.
• Phase balance: difference between any two phases at
peak load should not exceed ~10%.
• CAISO PF band is 97% lag–99% lead.
• Comply with SCT’s PQ policy; stricter limits may be
imposed from study results.
• Provide expected harmonic spectrum to the 50th order;
SCT may require mitigation and can temporarily reduce
or disconnect the load.
• SCT installs permanent POI PQ monitoring; PF must
remain within coordinated limits.
NA

VRT  is  the  capability and  obligation of  a  facility to  remain connected at  the  POI  through specified
combinations  of  voltage  magnitude  and  duration  that  occur  during  faults,  using  POI-referenced
envelopes  and  verified  by  standardized  test  methods  [25].  For  data  centers,  front-end  rectifiers  and
limited  dc-link  energy  make  constant-power  behavior  prone  to  tripping  on  deep,  short  sags  unless
buffered by an Uninterruptible Power Supply (UPS) systems or coordinated controls; this is why power
entities are moving to explicit load VRT expectations [26].
As illustrated in Table 2, SPP has published a time-voltage curve (0.90–1.10 pu continuous, with short-
duration tolerances down to ~0.50 pu for ~0.15 s) and transient overvoltage withstand aligned with IEEE
2800.  Dominion  emphasizes  reclosing  tolerance  instead,  requiring  ride-through  of  several  reclosing
shots  (each  ~50–70  ms)  with  undervoltage  pickup  near  85%.  ERCOT’s  proposed  large-load  VRT
requires continuous operation between 0.90–1.10 pu, with staged ride-through outside that range based
on the ITIC curve, global experience, and existing IBR requirements (see Section 3).

2.4.

Frequency ride-through

FRT requires facilities to remain connected through defined combinations of frequency deviation and
duration, typically expressed as frequency–time curves with “must-run” and “must-trip” regions [27].
For converter-dominated data centers, simultaneous tripping or transfer to UPS can remove hundreds of
megawatts at once, motivating explicit FRT requirements beyond system-wide under-frequency load
shedding (UFLS) schemes [26]. Most generator codes already require continuous operation near 59.4–
60.6 Hz, while the emerging practice is to apply analogous POI-referenced windows coordinated with
UFLS.  In  data  center  applications,  FRT  should  also  include  staged  recovery  and  high-resolution
telemetry to verify compliance [27].
As shown in Table 2, SPP publishes a detailed profile (continuous 58.8–61.2 Hz, extended to 299 s,
permissive trip beyond 61.8/<57.0 Hz). By  contrast, most other entities embed load behavior within
UFLS  frameworks: AEP  aligns with regional UFLS,  Dominion requires participation in  UFLS  with
necessary relays, Ameren defines staged UFLS blocks (59.3/59.0/58.7 Hz), PG&E applies UF relaying
as  directed  by  CAISO,  and  Southern  requires  verification  of  customer  settings  without  publishing
numeric bands.

Ta le 2.  ummar  o  comparative anal sis o   RT and FRT requirements  or large load interconnection

Entit

 RT

AEP [10]

 ominion
[11], [28]

ERC T [12],
[13], [14], [15]

 I
Ameren [16]

PG E [17],
[18], [19],
[20], [21]
 outhern
Compan [22],
[23]
 PP [24]

• No POI time–voltage envelope for loads is
published; voltage performance is managed via PQ
limits and settings review during studies.
• Remain connected through several automatic
reclosing shots (50-70 ms); recommend
undervoltage pickup ≤85% with short timers to
avoid nuisance transfers.
• ERCOT follows ITIC Curve and IEEE 1668 for
undervoltage, and NOGRR245 for overvoltage.
• Proposal applies prospectively.
• No load ride-through curve; undervoltage load
shedding is not standard and may be applied on a
case-by-case basis as an interim measure.
• No load time-voltage curve; unexpected
separations are reported with causes and event
files; settings should be coordinated with PG&E.
• Submit voltage ride-through settings for SCT
review and adjust as directed or per standards;
settings to be verified through testing/monitoring.
• Follows ITIC curve and IEEE 1668-2017, IEEE
standard 2800-2022 (Clause 7 adopted by SPP),
and NERC standard PRC-029-1.

2.5.

Post-disturbance load recovery

Categor

FRT

• Coordination with regional UFLS (under-frequency
load shedding); no separate numeric frequency-time
envelope is prescribed.
• Participation in system-wide UFLS with appropriate
relays and communications.

• Numeric load frequency settings are “to be developed”;
any adopted settings are to be set to maximum feasible
capability.
• UFLS stages near 59.3, 59.0, and 58.7 Hz (~10% each).
• New connections may initially be allowed without
UFLS, but Ameren can require UFLS at a later retrofit.
• No explicit load frequency window; under-frequency
relaying is applied where applicable, with telemetry;
PG&E interfaces under ISO direction in emergencies.
• Submit frequency ride-through settings for SCT review
and adjust as directed or per standards; settings to be
verified through testing/monitoring.
• Example withstand: continuous 58.8–61.2 Hz; extended
tolerance for 299 s outside that band; trip permissible
above ~61.8 Hz or below ~57.0 Hz.

In this paper, post-disturbance load recovery refers to the requirements for reconnecting data center load
to the grid following a fault or power quality event. This requirement is critical to preserve grid integrity,
since large portions of data center load may temporarily shift to backup power during a disturbance.
Table 3 shows that ERCOT is the only entity specifying a numeric target: ≥90% of pre-disturbance load
restored within 1 second once 𝑉𝑃𝑂𝐼 ≥ 0.9𝑝𝑢. AEP and Dominion require customer-specific restoration
plans  (thresholds,  delays,  block  sizes,  ramps),  but  no  uniform  limits.  Ameren  coordinates  recovery
through switching and reactive support. PG&E requires control-center approval before reconnection,
including  safeguards  against  unattended  remote  restore.  Southern  Company  enforces  approved
procedures  and  validated  ramp  limits,  with  curtailment  capability,  while  SPP  expects  recovery
consistent with its VRT/FRT boundaries and operating guidance.

2.6.

System protection

Table  3  summarizes  practices:  AEP  requires  complete  protection  data  and  clearing  verification;
Dominion specifies delta high-side intertie transformers and may reduce service if harmful interactions
occur;  ERCOT  requires  remotely  operable  interrupters  and  includes  system  oscillation  analysis  in

interconnection  study;  Ameren  specifies  redundant  schemes  and  breaker-failure  coverage;  PG&E
mandates communication-aided schemes, periodic testing, and prohibits ≥100 kV taps; while Southern
Company  adds  instrument  transformer  accuracy,  breaker  ratings,  and  potential  inclusion  in  load
shedding schemes. SPP does not provide detailed load-side protection rules. Nearly all entities mandate
utility review and approval of the protection system before energization.

Ta le 3.  ummar  o  post distur ance load recover  and protection requirements  or large load interconnection

Entit

AEP [10]

 ominion
[11], [28]

Post  istur ance  oad Recover

Protection

Categor

• Customer provides staged reconnection and ramp
plans (thresholds, delays, block sizes, ramps); AEP
coordinates to avoid secondary dips and RVCs.
• Customer specifies reconnection method and
ramp process; numeric recovery level/time is not
prescribed.

ERC T [12],
[13], [14], [15]

• Proposed target (Area B): recover to ≥90% of
pre-disturbance consumption within 1 second once
VPOI ≥ 0.9pu; if disconnected (Area C), restoration
is staggered across multiple large loads.

 I
Ameren [16]

• No numeric minimum level/maximum time;
restoration should be coordinated with Ameren
using switching, reactive adjustments, and operator
direction.

PG E [17],
[18], [19],
[20], [21]

• After any separation, the operator notifies the
Control Center and obtains permission before
reconnecting; unattended remote restoration
requires verification that the circuit is energized
from a PG&E-approved source.

 outhern
Compan [22],
[23]

• No utility-wide numeric minimum level/max
time; restoration follows approved operating
procedures and validated ramp limits; curtailment
capability and ramp-rate performance are checked
before “Full Readiness.”

 PP [24]

• No numeric minimum level/max time;
expectation is to remain connected within V/F
boundaries and coordinate restoration per
operational guidance.

• Customer supplies full protection data; AEP confirms
interrupting duties, clearing times, and transformer/high-
side/low-side device adequacy.
• Intertie transformer high-side is normally delta;
configurations require review.
• Reduction/disconnection may be required if interactions
are harmful; inter-substation transfers need approval.
• Each POI includes remotely operable disconnect
devices able to interrupt fault current and isolate the load;
the study scope includes steady-state, stability, short-
circuit, and Subsynchronous Oscillation (SSO)
considerations.
• At minimum, a ring-bus is required; large hubs may use
a straight bus or breaker-and-a-half configuration.
• Breaker failure protection for customer interrupting
devices; visible isolation at the POI; redundant schemes
that detect faults on both sides.
• Utility-grade, PG&E-approved relays coordinated with
PG&E line protection; visible load-interrupting device at
the POI; fault-interrupting devices located close to POI.
• Communication-aided line schemes and transfer-trip
channels may be required; relay/breaker testing before
energization and every six years.
• New taps on ≥100 kV lines are not permitted;
interconnect at a substation.
• Utility-grade relays with coordinated settings; relaying-
accuracy CTs; SCT determines intertie breaker rating and
may require high-speed protection communications.
• High-side transformer normally delta; on-site
generation is interlocked to prevent parallel operation
unless allowed.
• Load may be included in load shedding schemes.
NA

2.7.

Control and communication requirements

For large loads, utilities are moving toward substation-grade communications and control to ensure fast,
deterministic signaling for operations and auditable data for compliance. As summarized in  Table 4,
visibility expectations are rising: Dominion mandates permanent POI PQ  meters with ≥90-day logs;
ERCOT  requires ≤10-s telemetry, continuous state reporting, and redundant ICCP;  Ameren requires
continuous  MW/MVAr/V/I  telemetry  over  Harris  5000  or  equivalent;  PG&E  specifies  24/7
communications with operator notification, cellular/Ethernet revenue meters, and dedicated protection
comms as needed; Southern Company requires company-owned RTUs with validated points and may
deploy Phasor Measurement Units (PMU) and/or advanced Digital Fault Recorders (DFR); AEP calls
for reliable telemetry but does not specify a protocol.

2.8.

Study modeling requirements

Data center loads behave as constant-power loads, drawing more current when the voltage decreases
and less when the voltage increases. This behavior produces negative incremental impedance, which
can amplify disturbances and compromise stability  during large transients. Therefore, planners have

begun  supplementing  positive-sequence  studies  with  Electromagnetic  Transient  (EMT)  analyses,
particularly when local short-circuit strength is low [29].
Table 4 shows that all entities require steady-state and short-circuit studies, with EMT analysis added
as needed. AEP accepts PSS/E and may request PSCAD/EMTDC models; Dominion requires PSS/E
with as-planned/as-built data and may also request PSCAD models; ERCOT defines scope and model
registration through interconnection studies; Ameren adds short-circuit, stability, switching, or EMT
studies under a study agreement; PG&E cites ASPEN, PSLF, PSCAD, and RTDS (at 500 kV) studies;
Southern Company requires as-planned/as-built/as-left datasets with simulation-based validation; and
SPP  emphasizes  dynamic  load-model  validation  through  modeling,  commissioning  tests,  and
operational monitoring.

Ta le 4.  ummar  o  communications  control  compliance  and stud  requirements  or large load interconnection

Categor

Entit

AEP [10]

 perational Communications  Control
Compliance
• Reliable operational telemetry is required for
real-time coordination and compliance; no specific
communication protocol is mandated.

 ominion
[11], [28]

ERC T [12],
[13], [14], [15]

• Permanent POI PQ meters; time-aligned, high-
resolution logging with ≥ 90-day retention.
• Facilities subject to UFLS must maintain
communications to coordinate actions.
• Operational telemetry to ERCOT at ≤10-s scan
rate with condition detection; continuous
breaker/switch state is needed.
• Fully redundant ICCP links with automatic
failover.

 I
Ameren [16]

PG E [17],
[18], [19],
[20], [21]

 outhern
Compan [22],
[23]

• Continuous telemetry (MW, MVAr, current,
voltage) using Harris 5000 protocol or agreed-
upon equivalent; 24-hour contacts; annual meter
testing; customer maintains telecom circuits.
• 24-hour comms with Control Center; telephone
service required; revenue meters use cellular
modem and, when possible, Ethernet with static IP.
• Dedicated comms for protection, such as transfer
trip as specified by PG&E.
• Data link from SCT-owned interconnection RTU,
typically serial over fiber; real-time telemetry
points exchanged and tested before energization;
SCT may deploy PQ meters, PMU, and advanced
DFR devices.

 PP [24]

• Compliance via modeling, commissioning tests,
and operational monitoring; the document does not
prescribe a specific communications protocol.

 tud   odeling Requirements

• Steady-state, short-circuit, and (as needed) stability
studies; inputs include step-change cadence, harmonic
spectra, VAR devices, and multi-year forecasts.
• Positive-sequence models in PSS/E are accepted; EMT
studies in PSCAD may be requested where needed.
• Provide CMLD/EV or user-defined models in PSS/E
with as-planned/as-built data; PSCAD may be requested
for interaction/stability studies.

• A large load must pass steady-state, stability, and short-
circuit studies (plus any other studies the TSP/ISO deems
necessary).
• Additional load at the same site is not included in
ERCOT’s planning/operational models until the current
request’s studies are finished, and agreement executed.
• No specific software is mandated in the materials
provided.
• Ameren begins with power flow studies; it adds short-
circuit, stability, switching, or EMT as needed under a
study agreement, consistent with NERC TPL-001; no
specific commercial tool is mandated.
• Modeling submittal is required; PG&E cites ASPEN,
PSLF, PSCAD models (and RTDS model for 500 kV).
• Pre-energization testing and PG&E witnessing are
mandatory with defined tolerances and report lead times.

• Provide site-specific data at “as-planned/as-built/as-left”
stages; SCT verifies via simulations before initial
energization and through a performance-validation period.
• The appendix lists modeling inputs (load composition,
PF, sag/swell and reconnection thresholds, frequency
trips, ramp rates, harmonic spectrum, load profiles).
• No specific commercial tool is mandated; EMT analysis
may be requested.
• Studies, commissioning tests, and monitoring emphasize
dynamic load-model validation and ride-through
demonstration; no specific commercial tool is mandated.

3.  EUROPEAN EXPERIENCE AND VISION

Across Europe, the  binding framework for  large-load connections is the  Network Code  on  Demand
Connection, which harmonizes rules for connecting demand facilities and distribution systems [30]. It
also  makes VRT  expectations explicit at  the  POI.  For  Continental Europe,  this means  a  continuous
operating window of 0.90–1.05 pu and a sustained band of 1.05–1.10 pu for 20–60 minutes, as set by
the transmission operator.

Figure 3 compares low-voltage ride-through envelopes applied by RTE (France), Energinet (Denmark),
and EirGrid (Ireland) [31] with numeric VRT curves from two U.S. entities, SPP and ERCOT. At the

system level, European studies show that congestion at legacy hubs can delay new connections by up to
13  years.  To  reduce  queues,  recommended  measures  include  strategic  siting,  phased  or  non-firm
connections,  and  smarter  connection  agreements,  which  could  cut  timelines  to  around  a  year.  The
analysis also highlights the need for pilots on data center flexibility and greater transparency, such as
capacity maps and visible queue data, to better coordinate siting and investment [32].

Figure 3.  RT Curves  or American and European Entities [13], [24].

4.  CONCLUSION

This review compared interconnection requirements for large loads across U.S. utilities and ISOs, with
a focus on data centers. Eight technical categories were examined: load management, power quality,
voltage  ride-through,  frequency  ride-through,  post-disturbance  recovery,  protection,  control  and
communications, and  modeling requirements. The  analysis shows  uneven  development across  these
areas.  Protection  requirements  are  relatively  mature,  with  most  entities  converging  on  utility-grade
relays, selective clearing, modeling workflows, and auditable POI isolation. Power quality expectations
are also broadly aligned, referencing IEEE 519 and IEEE 1453, with growing emphasis on permanent
PQ metering.
In contrast, ride-through, load recovery, and load modeling are all in progress. Only SPP and ERCOT
publish explicit POI-based VRT envelopes, while most others rely on qualitative guidance. Load FRT
is still tied primarily to UFLS, with limited use of numeric remain-connected windows. Post-disturbance
recovery is mainly procedural, with ERCOT proposing a quantitative target. Likewise, definitions of
“large load” and ramping limits vary widely across entities.
Overall, the trend points toward greater standardization of ride-through profiles, recovery targets, and
visibility requirements similar to European practice. Publishing harmonized VRT/FRT envelopes, class-
specific  recovery  benchmarks,  standard  telemetry  expectations,  and  defined  modeling  requirements
would accelerate convergence and reduce study burden. The harmonized framework and comparative
analysis (Table 1–Table 4 ) provide a practical reference for utilities, regulators, and developers working
to integrate large, fast-growing loads such as data centers reliably and efficiently.

REFERENCES

[1]

[2]

[3]

[4]

[5]

[6]

[7]

“Characteristics and Risks of Emerging Large Loads,” 2025. Accessed: Aug. 18, 2025. [Online].
Available:
https://www.nerc.com/comm/RSTCReviewItems/3_Doc_White%20Paper%20Characteristics%20and
%20Risks%20of%20Emerging%20Large%20Loads.pdf
“NERC Activities and Plans to Address Reliability Impacts from Large Load Integration.” Accessed:
Aug. 18, 2025. [Online]. Available: https://www.ferc.gov/news-events/news/presentation-nerc-seeks-
address-
R. Zahedi, R. Sheinberg, S. N. Gowda, K. SedghiSigarchi, and R. Gadh, “A Framework for Optimal
Sizing of Heavy-Duty Electric Vehicle Charging Stations Considering Uncertainty,” World Electric
Vehicle Journal 2025, Vol. 16, Page 318, vol. 16, no. 6, p. 318, Jun. 2025, doi:
10.3390/WEVJ16060318.
N. Lin, M. Arzumanyan, E. Arzumanyan, D. Foreman, and N. Schuba, “Data Center Growth in Texas:
Energy, Infrastructure, and Policy Pathways.”
“DOE Releases New Report Evaluating Increase in Electricity Demand from Data Centers |
Department of Energy.” Accessed: Aug. 18, 2025. [Online]. Available:
https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-
centers
A. Cowie-Haskell, “Large Computational Load Growth: A literature review and first-order assessment
of load characteristics and its impacts on emissions, costs, and decarbonization on CAISO,” Apr. 25,
2025. Accessed: Aug. 18, 2025. [Online]. Available: https://hdl.handle.net/10161/32282
“Practical Guidance and Considerations for Large Load Interconnections - GridLab.” Accessed: Aug.
18, 2025. [Online]. Available: https://gridlab.org/portfolio-item/practical-guidance-and-
considerations-for-large-load-interconnections/

[9]

[8]  M. Wang et al., “Load curve smoothing strategy based on unified state model of different demand side
resources,” Journal of Modern Power Systems and Clean Energy, vol. 6, no. 3, pp. 540–554, May
2018, doi: 10.1007/S40565-017-0358-0/FIGURES/18.
“IEEE Recommended Practice for Monitoring Electric Power Quality,” 2019, Accessed: Aug. 20,
2025. [Online]. Available: http://www.ieee.org/web/aboutus/whatis/policies/p9-26.html.
“Requirements for Connection of New Facilities or Changes to Existing Facilities Connected to the
AEP Transmission System,” Dec. 2024. Accessed: Aug. 18, 2025. [Online]. Available:
https://aeptransmission.com/dist/docs/power-ready-
grid/AEP_Interconnection_Requirements_Rev4.pdf

[10]

[11]  K. Vance, “Data Center Performance  at Dominion Energy Virginia,” 2025.
[12]
[13]  P. Gravois, “ERCOT Large Electronic Load  Voltage Ride-Through Performance Requirements

“Large Load Interconnection Status Update,” Aug. 2025.

(Proposal),” Jul. 2025. Accessed: Aug. 18, 2025. [Online]. Available:
https://www.ercot.com/files/docs/2025/07/11/ERCOT-LEL-Ride-Through-Criteria_LLWG-final.pptx
“1234NPRR-01 Interconnection Requirements for Large Loads and Modeling Standards for Loads 25
MW or Greater 052824”, Accessed: Aug. 18, 2025. [Online]. Available:
https://www.ercot.com/files/docs/2024/05/28/1234NPRR-
01%20Interconnection%20Requirements%20for%20Large%20Loads%20and%20Modeling%20Stand
ards%20for%20Loads%2025%20MW%20or%20Greater%20052824.docx
“115PGRR-01 Related to NPRR1234, Interconnection Requirements for Large Loads and Modeling
Standards for Loads 25 MW or Greater 052824.” Accessed: Aug. 18, 2025. [Online]. Available:
https://www.ercot.com/files/docs/2024/05/28/115PGRR-
01%20Related%20to%20NPRR1234,%20Interconnection%20Requirements%20for%20Large%20Lo
ads%20and%20Modeling%20Standards%20for%20Loads%2025%20MW%20or%20Greater%200528
24.docx
“End User Connection Procedures Requirements for the Connection of Customer Load to the Ameren
Transmission System,” 2023.
“PG&E Transmission Interconnection Handbook - Section L1-T: Revenue-Metering Requirements
For Transmission-Only And Load-Only Entities,” 2024.

[14]

[15]

[16]

[17]

[18]

[19]

[20]

[21]

[22]
[23]

“PG&E Transmission Interconnection Handbook - Section L2: Protection And Control Requirements
For Load Entities And Transmission Entities,” 2024.
“PG&E Transmission Interconnection Handbook - Section L3: Substation Design For Load-Only
Entities And Transmission-Only Entities,” 2024.
“PG&E Transmission Interconnection Handbook - Section L4: Operating Procedures And
Requirements For Load-Only And Transmission-Only Entities,” 2023.
“PG&E Transmission Interconnection Handbook - Section L5: Pre-Energization Test Procedures For
Load-Only Entities And Transmission-Only Entities,” 2022.
“Integration Process for Transmission Connected Large Loads.”
“Technical Requirements for Transmission Connected Large Loads.” [Online]. Available:
http://www.oatioasis.com/SOCO/SOCOdocs/Southern-OATT_current.pdf

[24]  D. Baker and M. Sedighizadeh, “high impact large load ride through requirements.” Accessed: Aug.

18, 2025. [Online]. Available:
https://www.spp.org/Documents/74272/High%20Impact%20Large%20Load%20Ride%20Through%2
0Requirements.docx

[25]  W. Houk, “RIDING THROUGH VOLTAGE SAGS WITH THE IEEE 1668 STANDARD,” 2023,

[26]

Accessed: Aug. 20, 2025. [Online]. Available: https://library.powermonitors.com/riding-through-
voltage-sags-ieee-1668
J. Conto, Y. Cheng, J. Rose, and J. Schmall, “Texas Loads Ride Toward Grid Stability: Voltage Ride
Through of Large Power Electronic Loads,” IEEE Power and Energy Magazine, vol. 23, no. 5, pp.
56–67, Sep. 2025, doi: 10.1109/MPE.2025.3564963.

[27]  M. A. Zamani, N. Wrathall, and R. Beresh, “A review of the latest voltage and frequency ride-through
requirements in canadian jurisdictions,” Proceedings - 2014 Electrical Power and Energy Conference,
EPEC 2014, pp. 116–121, Feb. 2014, doi: 10.1109/EPEC.2014.10.
“Large Load Interconnections_FIR Rev 24,” Aug. 2025.

[28]
[29]  F. Chang, X. Cui, M. Wang, and W. Su, “Potential-Based Large-Signal Stability Analysis in DC

[30]
[31]

[32]

Power Grids with Multiple Constant Power Loads,” IEEE Open Access Journal of Power and Energy,
vol. 9, pp. 16–28, 2022, doi: 10.1109/OAJPE.2021.3132860.
“Network Code on Demand Connection,” Aug. 2016.
“Explanatory guide on how to connect a demand facility to the transmission grid ,” Jan. 2025.
Accessed: Aug. 21, 2025. [Online]. Available: https://en.energinet.dk/media/oh0oexqp/explanatory-
guide-on-how-to-connect-a-demand-facility-to-the-electricity-transmission-grid-january-2025.pdf
“Grids for data centres: ambitious grid planning can win Europe’s AI race.” Accessed: Aug. 20, 2025.
[Online]. Available: https://ember-energy.org/app/uploads/2025/06/Grids-for-data-centres-in-
Europe.pdf

