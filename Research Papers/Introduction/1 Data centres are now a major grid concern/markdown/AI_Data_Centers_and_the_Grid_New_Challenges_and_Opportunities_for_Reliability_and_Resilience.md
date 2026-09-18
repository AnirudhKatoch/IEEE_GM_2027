©SHUTTERSTOCK.COM/CREATIVA IMAGES
AI Data Centers
and the Grid
New Challenges and Opportunities
for Reliability and Resilience
By Mahsa Omri , Ryan Quint , Ryan Elliott ,
Pramod Khargonekar , Mohammad Amin Mirzaei ,
Kyle Thomas , and Masood Parvania
Mahsa Omri is with the University of Utah, Salt Lake City, UT 84112 USA. Ryan Quint is with Elevate Energy Consulting,
Spokane, WA 99208 USA. Ryan Elliott is with Sandia National Laboratories, Albuquerque, NM 87123 USA. Pramod
Khargonekar is with the University of California, Irvine, Irvine, CA 92697 USA. Mohammad Amin Mirzaei is with the
University of Utah, Salt Lake City, UT 84112 USA. Kyle Thomas is with Elevate Energy Consulting, Spokane, WA 99208
USA. Masood Parvania is with the University of Utah, Salt Lake City, UT 84112 USA.
Digital Object Identifier 10.1109/ESM.2026.3677225
Date of current version: 29 July 2026
2998-3991 © 2026 IEEE. All rights reserved, i ncluding rights for text and
28 IEEE Energy Sustainability Magazine data mining, and training of artificial intelligence and similar technologies. August 2026
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.

TTHE RAPID PROLIFERATION OF ARTIFICIAL reliable, resilient, and affordable electricity while
intelligence (AI) applications and societal reli- simultaneously supporting the advancement of
ance on computing is driving an unprecedented modern society.
surge in electricity demand, with AI data cen- The U.S. National AI Action Plan outlines an
ters emerging as one of the fastest-growing and urgent strategy to align the nation’s electric grid
most energy-intensive load categories. These fa- with the growing energy requirements of AI
cilities often draw hundreds or even thousands of technologies.1 It emphasizes that the grid must
megawatts (MW) of power and exhibit demand keep pace with rising demand from AI data cen-
characteristics that differ markedly from tradi- ters, which are central to sustaining innovation
tional large loads such as aluminum smelters. and U.S. leadership in the field. To achieve this,
the plan prioritizes upgrading transmission in-
Introduction frastructure, enhancing grid resilience, and de-
Unlike traditional industrial facilities, AI data cen- ploying advanced dispatchable generation, such
ters concentrate synchronized power demands as small modular reactors. Translating these
over relatively short time frames, often in regions priorities into action will hinge on targeted in-
with constrained transmission capacity or lim- vestment and workforce development. Without
ited generation headroom. Their unprecedented enough skilled power system engineers, even
scale and variability are forcing a reexamination well-planned upgrades to transmission, genera-
of long-standing approaches to system plan- tion, and grid resilience cannot be implemented
ning, operation, and regulatory oversight. at the scale required.
Compounding the challenges introduced by Accommodating the rapid growth of AI loads
AI data centers, the grid itself is facing concur- requires balancing two critical objectives: sup-
rent transformative pressures, including the inte- porting the expansion of the AI economy while
gration of power electronically coupled resources ensuring grid reliability and resilience. Devel-
to complement conventional synchronous gen- oping strategies that incorporate advanced
eration, the deployment of flexible grid assets, planning, flexible operations, and coordinated
such as battery energy storage (BES), to manage stakeholder engagement will be essential to
variability and provide ancillary services, and the maintaining this balance. The success of these
expansion of grid measurement and monitoring strategies will determine the grid’s ability to sup-
systems to improve situational awareness, opera- port a future increasingly shaped by AI.
tional decision making, and control.
The combined effect of these pressures is re- AI Data Centers Driving Electricity
shaping the bulk power system (BPS), creating Demand Growth
conditions in which large concentrated loads For nearly two decades, electricity demand in
exert an outsized influence. The introduction the United States remained relatively flat. From
of AI data centers acts as a catalyst for these the early 2000s through the mid-2010s, national
trends, accelerating demand growth across consumption growth slowed to near-zero levels.
communities and regions. These trends also in- This plateau reflected energy efficiency improve-
tersect with growing planning and operational ments, structural economic changes, and the
challenges, including widespread replacement of inefficient technolo-
➤ addressing bottlenecks in expanding gies. Advances in data center power utilization
large-scale transmission infrastructure, largely offset rising demand for computation,
such as supply chain constraints, land thanks to more efficient server hardware, system
availability, and regulatory hurdles, that architectures, and cooling technologies. During
limit the ability to meet growing demand this period, the data center landscape included a
➤ managing resource adequacy risks from mix of cloud computing, enterprise, and emerg-
uncertainty in generation and load across ing blockchain/crypto operations, each with
multiple timescales distinct load profiles that collectively shaped elec-
➤ mitigating evolving cyber and physical se- tricity demand. Between 2014 and 2016, U.S. data
curity threats that require ongoing oversight center electricity use hovered around 60 TWh
➤ adapting to extreme weather events, includ- annually, despite rapid digital transformation.
ing wildfires, hurricanes, and flooding, that In response to this stagnation, utilities adopted
are increasing in frequency and severity. more conservative planning practices, regulators
But the imperative remains: the electric-
ity sector must supply end-use customers with 1 https://www.ai.gov/action-plan.
August 2026 IEEE Energy Sustainability Magazine 29
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.

 recalibrated standards, and investment remained  AI data centers, with peak loads of 100 MW or
subdued. Consequently, transmission expansion  more, can be built and commissioned within
slowed, and modest growth in generation capac- one to two years. But the transmission, gen-
ity caused reserve margins to tighten. eration, and substation infrastructure needed to
This equilibrium is unraveling. Since 2021, utili- support them often lags behind. New intercon-
ties and grid operators have sharply revised load  nection requests routinely span 100–1,000 MW,
forecasts upward, signaling a new era of electric- roughly equivalent to the power needs of a small
ity demand growth. While electrification in in- city.  These  requests  are  often  concentrated  in
dustry, transportation, and hydrogen production  specific regions and appear with limited notice.
contributes to this shift, the most immediate  Unlike gradual residential or commercial growth,
driver is the expansion of data centers. The num- these surges stress the grid and complicate re-
ber of operational data center facilities worldwide  source adequacy. More importantly, the techni-
rose from approximately 8,000 in 2021 to nearly  cal characteristics of AI loads—power density,
12,000 by early 2025. The United States hosts the  variability, synchronization, and potential reso-
largest share, with more than 5,400 sites. nance  effects—pose  system  reliability  chal-
Data center electricity consumption in the  lenges distinct from conventional computing
United States tripled from 60 TWh in 2017 to 176  infrastructure.  These  challenges  are  forcing
TWh in 2023, accounting for roughly 4.4% of to- utilities, regulators, and system operators to re-
tal usage, as shown in Figure 1. According to the  consider long-standing planning and operational
| Lawrence  | Berkeley  | National  | Laboratory,  |     | fore- | practices. |     |     |
| --------- | --------- | --------- | ------------ | --- | ----- | ---------- | --- | --- |
casts suggest that this level could more than
triple again by 2028, reaching 580 TWh, or about  AI Infrastructure Load Characteristics
12% of total U.S. electricity consumption. AI, with  Specialized computing units, known as AI accel-
its GPU-accelerated training and inference, im- erators, lie at the heart of AI data centers. Most of
poses far greater demands for power, cooling,  these accelerators are based on graphics process-
and throughput than conventional IT, making it  ing units (GPUs), purpose-built for the massively
the primary driver of this growth. For context, a  parallel computations that AI workloads require.
single generative-AI query can consume nearly  Racks of GPU-powered accelerators are support-
10 times the electricity of a standard web search. ed by extensive cooling infrastructure and robust
The rapid pace of data center deployment  power delivery systems, including uninterruptible
creates acute planning challenges. Hyperscale  power supplies (UPSs). Networking, lighting, and
|     |     |     |     |     |     |     | site  management     | systems     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- |
|     |     |     |     |     |     |     | are  also  present,  | but  their  |
electricity demand is gen-
erally small compared with
|     | 600 |     |     |     |     |     | compute and cooling. Cool- |              |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | ------------ |
|     |     |     |     |     |     |     | ing  equipment,            | including    |
|     | 500 |     |     |     |     |     | chillers,  liquid          | loops,  and  |
)hWT( noitpmusnoC ygrenE
air-handling units, also con-
sumes substantial amounts
400
of power, highlighting why
these facilities are such large
300
and dynamic electricity con-
sumers.
|     | 200 |     |     |     |     |     | Modern      | AI  accelerators    |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------- |
|     |     |     |     |     |     |     | can  spike  | their  electricity  |
use almost instantaneously.
|     | 100 |     |     |     |     | Actual |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | --- |
At scale, this creates signifi-
Projected
cant challenges for the grid;
0
|     | 4 5     | 6 7         | 8 9 0   | 1 2     | 3 4       | 5 6 7 8       | repeated  surges           | can  strain  |
| --- | ------- | ----------- | ------- | ------- | --------- | ------------- | -------------------------- | ------------ |
|     | 0 1 0 1 | 0 1 0 1 0 1 | 0 1 0 2 | 0 2 0 2 | 0 2 0 2 0 | 2 0 2 0 2 0 2 |                            |              |
|     | 2 2 2   | 2 2         | 2 2     | 2 2 2   | 2 2       | 2 2 2         | equipment, complicate bal- |              |
ancing, and even risk trigger-
Year
ing system-wide oscillations.
In AI data centers, accelera-
figure 1. The actual and forecasted growth in U.S. data center electricity
| consumption, 2014–2028.                  |     |     |     |     |     |     | tors account for most of the  |             |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------------- | ----------- |
| 30  IEEE Energy Sustainability Magazine  |     |     |     |     |     |     |                               | August 2026 |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore.  Restrictions apply.

electricity  use,  running  training  jobs  that  cycle  grid stability. Harnessing this potential would al-
between intense bursts of computation and brief  low the grid to accommodate rapid AI growth
pauses for synchronization. while enhancing overall system reliability, a crucial
During computation, AI accelerators draw power  consideration as these facilities expand worldwide.
near their maximum thermal limits, with demand
dropping sharply during the synchronization pauses.  Regional Load Growth Patterns From
These cycles occur over intervals ranging from frac- AI Data Center Deployment
tions of a second to tens of seconds. They produce  Although AI loads are driving national electric-
large and highly periodic power swings that can  ity demand, that growth is unevenly distributed.
reach tens or even hundreds of megawatts per facil- Figure 3 illustrates data center operating ca-
ity. Critically, these power swings fall in the 0.2–3-Hz  pacity by state, organized according to E  lectric
| range,             | overlapping  | with  the  |     |     |     |     |
| ------------------ | ------------ | ---------- | --- | --- | --- | --- |
| grid’s  natural    | oscillation  | fre-       |     |     |     |     |
| quencies,          | arising      | from  the  |     |     |     |     |
| electromechanical  |              | dynamics   |     |     |     |     |
| of  synchronous    | generators.  |            |     |     |     |     |
60
| This  means  | that  large  | peri- )W( rewoP |     |     |     |     |
| ------------ | ------------ | --------------- | --- | --- | --- | --- |
odic data center loads could
unintentionally excite system-
40
wide oscillations, putting grid
| reliability  | at  risk.  Figure  | 2(a)  |     |     |     |     |
| ------------ | ------------------ | ----- | --- | --- | --- | --- |
illustrates a typical AI power  19:00 19:15 19:30 19:45 20:00 20:15 20:30 20:45
| demand  | profile  in  | the  time  |     |     |     |     |
| ------- | ------------ | ---------- | --- | --- | --- | --- |
domain, which is markedly dif-
ferent from conventional infor-
60
| mation technology workloads,  |              | )W( rewoP |     |     |     |     |
| ----------------------------- | ------------ | --------- | --- | --- | --- | --- |
| where                         | consumption  | is  rela- |     |     |     |     |
tively steady. Figure 2(b) shows
40
the frequency-domain repre-
sentation of GPU power con-
sumption during AI training,  19:24 19:25 19:26 19:27 19:28 19:29 19:30 19:31 19:32 19:33 19:34
| illustrating spectral content in  |                        |          |     | Time |     |     |
| --------------------------------- | ---------------------- | -------- | --- | ---- | --- | --- |
| the relevant frequency range.     |                        |          |     | (a)  |     |     |
| Hence,                            | AI  data               | centers  |     |      |     |     |
| aren’t                            | just  big  consumers;  |          |     |      |     |     |
| they  can                         | introduce              | unex-    |     |      |     |     |
edutingaM latoT fo noitcarF 0.02
pected stresses to the grid,
requiring operators to man-
0.015
age their fluctuations in real
| time.  Left               | unchecked,  | their  |      |     |     |     |
| ------------------------- | ----------- | ------ | ---- | --- | --- | --- |
| dynamic demand character- |             |        | 0.01 |     |     |     |
istics pose risks to BPS reli-
| ability and quality of service.  |              |            | 0.005 |     |     |     |
| -------------------------------- | ------------ | ---------- | ----- | --- | --- | --- |
| However,                         | careful      | manage-    |       |     |     |     |
| ment                             | of  on-site  | resources  | 0     |     |     |     |
within these facilities, such as
|             |                |      | 0 1 | 2 3 | 45  |     |
| ----------- | -------------- | ---- | --- | --- | --- | --- |
| batteries,  | could  create  | new  |     |     |     |     |
Frequency (Hz)
opportunities for supporting
(b)
grid operations and control.
There is growing interest in
figure 2. (a) An example GPU power consumption profile during an AI
| the  idea  | that  data  | centers  |     |     |     |     |
| ---------- | ----------- | -------- | --- | --- | --- | --- |
training workload. The top panel shows a 2-h segment of GPU power
could act as flexible power
draw, while the bottom panel zooms in on a 10-minute interval to provide
system resources, adjusting  a fine-grained view of the characteristic cyclical fluctuations between
their load in real time to help  compute-intensive and synchronization phases. (b) A frequency-domain
balance supply and maintain  representation (FFT) of the GPU power consumption during AI training.
| August 2026  |     |     |     | IEEE Energy Sustainability Magazine   |     | 31  |
| ------------ | --- | --- | --- | ------------------------------------- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore.  Restrictions apply.

Reliability  Organization  (ERO)  regions,  with  and serve these loads. Engineers and planners,
Table  1  summarizing  regional  totals.  Most  of  for example, often have little guidance on how
the new load is concentrated within existing  to model and study these facilities accurately
clusters, particularly in Northern Virginia, which  across the range of timescales required. Togeth-
hosts the world’s largest concentration of data  er, these factors are reshaping system planning,
centers, and in Texas, where recently approved  operations, and oversight, and they require in-
and queued projects represent tens of gigawatts  novative approaches to ensure grid reliability
| of additional demand. |     |     | and resilience moving forward. |     |     |     |     |
| --------------------- | --- | --- | ------------------------------ | --- | --- | --- | --- |
The expansion of AI data centers across vari-
Reliability Risks of AI Data Centers and
ous regions is creating new and complex chal-
lenges for long-term electricity planning. Unlike  How to Mitigate Them
other load categories, AI data centers are de- Continuous  and  reliable  flow  of  electricity  to
ployed  rapidly,  often  clustered  in  specific  end consumers is foundational to modern soci-
areas, and have a limited operational track  ety. Sustaining this foundation requires under-
record. Their technology evolves quickly, and  standing the grid’s performance across multiple
future demand patterns are unclear, leaving  dimensions. Power system reliability can be de-
grid stakeholders unsure how best to integrate  scribed in terms of
➤  adequacy: the availability
|     |     |     |      |             | of  sufficient            | generation,    |         |
| --- | --- | --- | ---- | ----------- | ------------------------- | -------------- | ------- |
|     |     |     |      |             | transmission,             | and            | distri- |
|     |     |     |      | >5,000      | bution resources to meet  |                |         |
|     |     |     |      |             | demand                    | under  steady- |         |
|     |     |     |      | 2,500–5,000 | state conditions          |                |         |
|     |     |     | NPCC |             | ➤  security               | (operating     | re-     |
)WM( yticapaC gnitarepO
|     |      |     |     | 1,000–2,500 | liability):                | the  ability  | to  |
| --- | ---- | --- | --- | ----------- | -------------------------- | ------------- | --- |
|     | WECC | MRO | RF  |             | maintain stability and op- |               |     |
erate within limits during
500–1,000
normal operating condi-
|     |     | SERC |     |     | tions and during defined  |     |     |
| --- | --- | ---- | --- | --- | ------------------------- | --- | --- |
200–500
|     |     |          |     |        | system                        | disturbances              |     |
| --- | --- | -------- | --- | ------ | ----------------------------- | ------------------------- | --- |
|     |     | Texas RE |     |        | such as faults or loss of     |                           |     |
|     |     |          |     | 50–200 | generation or load.           |                           |     |
|     |     |          |     |        | Both                          | pillars  of  reliability  |     |
|     |     |          |     | 0–50   | are increasingly stressed by  |                           |     |
|     |     |          |     |        | extreme                       | weather,  genera-         |     |
tion capacity shortfalls, and
figure 3. Contiguous U.S. data center operating capacity by state with
the variability of renewables.
ERO region boundaries. WECC: Western Electricity Coordinating Council;
MRO: Midwest Reliability Organization; Texas RE: Texas Reliability Entity; RF:  The  integration  of  large
reliability first; NPCC:  Northeast Power Coordinating Council amounts  of  inverter-based
SERC: SERC Reliability Corporation. generation  and  loads  is
table 1 Data center capacity by ERO region.
| ERO Region        |     | Operating (MW) | In Construction (MW) |     | Planned (MW)* |     |     |
| ----------------- | --- | -------------- | -------------------- | --- | ------------- | --- | --- |
| SERC (Southeast)  |     | 14,259         | 6,881                |     | 53,173        |     |     |
| WECC (West)       |     | 10,915         | 3,964                |     | 17,233        |     |     |
| Texas RE (Texas)  |     | 8,904          | 6,237                |     | 24,703        |     |     |
| RF (Mid-Atlantic) |     | 5,106          | 4,251                |     | 28,754        |     |     |
| MRO (Midwest)     |     | 3,544          | 1,752                |     | 7,695         |     |     |
| NPCC (Northeast)  |     | 1,016          | 199                  |     | 962           |     |     |
*Planned capacity reflects data center projects listed in regional interconnection queues and publicly reported planning
datasets. These values represent interconnection requests rather than committed or fully approved builds and are subject
to uncertainty as many planned projects may be delayed, downsized, or not ultimately realized.
| 32  IEEE Energy Sustainability Magazine  |     |     |     |     |     | August 2026 |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore.  Restrictions apply.

changing the fundamental nature of power sys- ness to market signals. These characteristics
tem design and control, while aging transmission complicate short-term demand forecasting and
and distribution infrastructure limits system flex- impair the grid’s ability to maintain balancing re-
ibility. The expansion of large loads such as AI data serves. AI data centers are often price insensitive
centers adds another layer of complexity atop and inflexible, operating around the clock to meet
these enduring stressors. performance targets. This limits their participation
in traditional demand-response programs and
How AI Data Centers Impact Grid creates challenges for grid operators tasked with
Reliability maintaining real-time equilibrium. Moreover, high
To examine how AI data centers affect the BPS, uptime requirements reduce operational flexibil-
we organize their impacts around the two pil- ity and compress the limited windows when grid
lars of reliability. Long-term planning and load maintenance can be safely scheduled. Combined
forecasting primarily influence adequacy, while with limited visibility into operational profiles, this
operational and real-time challenges are most hinders outage coordination and planned mainte-
closely linked to security. Grid stability and power nance.
quality concerns affect both pillars.
Adequacy and Security: Grid Stability, Power
Adequacy: Long-Term Planning Quality, and Resonance Concerns
and Load Forecasting The concentration of data centers at single inter-
Forecasting subregional electricity demand over connection points or within local pockets creates
multiyear horizons is complicated by the need to a new reliability concern: the potential for sud-
capture and differentiate large loads from gen- den large-scale loss of load if one or more facili-
eral demand growth, introducing substantial un- ties disconnect unexpectedly. Dense demands
certainty into planning. AI data center projects within these pockets may challenge voltage sta-
often enter transmission interconnection queues bility during severe contingencies, impose net-
in large numbers, with new proposals appearing work constraints driven by stability limits, and
faster than infrastructure can be planned or built. create common-mode failure events. These risks
Due to the low barrier to entry, combined with the are no longer hypothetical—clusters of nearly 60
speculative and highly competitive nature of ac- data centers totaling more than 1,000 MW have
cess to transmission service, transmission provid- disconnected simultaneously in Northern Virgin-
ers and market operators struggle to distinguish ia on more than one occasion, creating reliability
viable projects from placeholders. These uncer- incidents that could have triggered widespread
tainties flow directly into long-term planning. outages. Without fault ride-through c apabilities,
Integrated planning is constrained by a lead- ramp rate limits, and oscillation protections at
time mismatch where data centers can ma- data centers, the grid faces growing stability
terialize within months, whereas expanding risks. If unaddressed, such risks could propagate
transmission and generation capacity can take systemically, potentially resulting in widespread
years or even decades, creating a persistent gap reliability impacts that remain latent until trig-
in local adequacy. This creates uncertainty in ca- gered by a disturbance.
pacity expansion planning, necessitating repeat- In summary, the reliability challenges of AI data
ed upward revisions in utility load forecasts. The centers stem from the unprecedented scale of
result is a planning environment where genera- interconnection combined with the unique op-
tion and transmission adequacy are constantly erational characteristics of these loads. These chal-
strained. Transmission systems are particularly lenges not only span the entire spectrum of grid
exposed as a single facility or cluster can add hun- planning, operations, engineering, and restoration
dreds of megawatts of demand at one intercon- but also extend to policy and regulatory oversight.
nection point, overwhelming local infrastructure.
Traditional assumptions about diversified and Mitigating Grid Reliability Risks
gradually increasing loads are no longer viable in The challenges introduced by large AI data cen-
regions targeted for hyperscale AI deployment. ters have prompted early regulatory responses in
several jurisdictions. Policies such as Texas SB6
Security: Operations Planning and reflect a growing recognition that traditional
Real-Time Operations planning and interconnection frameworks are
AI workloads exhibit sharp ramping behavior, not well suited to manage the speed, scale, and
batch-driven variability, and limited responsive- operational complexity of emerging large loads.
August 2026 IEEE Energy Sustainability Magazine 33
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.

The electricity sector is addressing these risks accompanying generation resources, built on
through enforceable planning, interconnection, several mechanisms: 1) the ability to bring gen-
and operating measures to reposition these fa- eration to offset grid impacts, 2) flexible load
cilities from static and inflexible loads to control- management that allows curtailment, and 3) a
lable and grid-supportive assets. shorter interim option for faster connection, in
conjunction with an option to acquire firm rights
Interconnection Process Reforms in the longer term. The key elements of this evolv-
The rapid growth of large electricity loads has ing process are summarized in “Key Elements of
prompted federal and regional efforts to reform the SPP Accelerated Interconnection Process for
interconnection processes that were histori- Large Loads.”
cally designed for smaller loads. In response, the These types of new approaches are likely to
Secretary of Energy formally asked the Federal establish a precedent for other markets and
Energy Regulatory Commission (FERC) to estab- transmission providers to enable fast-tracked in-
lish a new standardized process for connecting terconnection for large customers as they seek
large load customers (i.e., greater than 20 MW) to align with federal regulatory actions. Ensur-
to the transmission grid. The aim is to make in- ing that new loads and paired generation assets
terconnections faster and more predictable by have a clear pathway with regulatory certainty
studying large loads together with on-site gen- and efficient processes is a key focus for the
eration, requiring upfront financial deposits and electricity sector in the years ahead. Regulatory
readiness milestones to ensure project viability as bodies must remain cognizant of the significant
well as offering expedited paths when custom- impact that these loads can have on BPS reliabil-
ers can be curtailed or dispatched as needed. It ity. Thus, load-specific requirements, ramp rate
also clarifies that projects prompting transmis- limits, metering equipment, power quality, ride-
sion upgrades will cover the costs and gives large through performance, oscillation mitigation, and
customers the “option to build” those upgrades voltage and frequency support requirements are
under standard utility oversight. This federal critical to harmonize nationally.
framing complements regional initiatives and is
intended to create a predictable national path- Financial Safeguards and Cost Allocation for
way for large customers. Reliability Upgrades
At the regional level, transmission providers Cost allocation is in the spotlight nationally to
are also rethinking standard interconnection ensure regulatory gaps do not result in unfair
processes to better accommodate large, high- allocation of network upgrade costs to existing
impact customers. For example, the Southwest ratepayers. Without clear rules, network upgrade
Power Pool (SPP) is working on a new acceler- costs associated with transmission infrastruc-
ated interconnection process for large loads and ture buildout to predominantly serve large load
Key Elements of the SPP Accelerated Interconnection Process
for Large Loads
• Verified requests: This requires state oversight on load ects that include on-site generation or paired gen-
or generation interconnection, including a state certi- eration support in a coordinated way.
fication process to ensure only credible projects submit • Conditional access: This allows customers to ener-
requests and provide high study deposits to show finan- gize facilities sooner, though subject to curtailment
cial readiness. if the grid is under stress.
• Certified high-load interconnection level studies: • Integrated coordination: This involves bundling
This establishes standardized study processes to design, registration, operations, and technical
certify whether a load can connect and under studies into a single coordinated pathway to inter-
what conditions, allowing loads to bring genera- connection, resulting in efficient system planning
tion to offset transmission congestion and gen- instead of siloed planning studies.
eration deficiency impacts.
• High-impact large load generation assessment:
This provides a parallel process for evaluating proj-
34 IEEE Energy Sustainability Magazine August 2026
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.

At the regional level, transmission providers are also
rethinking standard interconnection processes to better
accommodate large, high-impact customers.
customers may be shifted to broader ratepayers. may offer some operational network congestion
Grid operator market monitors have raised con- relief while long-lead reinforcements are built.
cerns about double-digit bill increases, predomi- Large AI data centers should also be incorporat-
nantly driven by upgrade costs to serve data ed directly into reliability and resource adequa-
center customers. Revised policies should define cy planning, providing ongoing load forecasts,
payment obligations, default penalties, and fi- availability profiles, and contingency character-
nancial commitment thresholds that reflect the istics into planning models; participating in new
actual impact and uncertainty of large load ad- ancillary services markets structured for non-
ditions. Provisions that reward demand flexibility, traditional assets; and, under defined operating
such as prioritized queue placement or intercon- frameworks, integrating into demand-response
nection cost discounts, can further align incen- and system restoration efforts so that they func-
tives while supporting grid reliability. tion as reliability assets rather than stressors.
Additional safeguards are also being consid- Together, these measures can improve visibility
ered and deployed to protect existing ratepayers into future load growth, reduce planning uncer-
to ensure fair costs and electricity affordability. tainty, and align infrastructure timelines with
Examples include customer-paid interconnec- the actual emergence of demand.
tion and grid upgrade costs, financial guarantees,
contractual commitments and exit penalties, Operational Controls and Load Behavior
minimum demand charges, demand ratchets, Management
minimum load factor obligations, and other pro- Real-time impacts are reduced by enforcing
tections. In parallel, new siting obligations could site-level caps and ramp rate limits on large
encourage load distribution and reduce bottle- load customers, which can be accomplished
necks. Early disclosure of data center siting plans through workload scheduling and supplemental
and regional capacity thresholds could identify devices such as BES systems (BESSs). Mandat-
early discrepancies between demand and local ing disturbance ride-through will result in more
hosting capacity. robust installations, settings, and commission-
ing of grid-interfacing equipment such as UPSs
Planning and Forecasting Enhancements and server-level power conversion settings. Load
Load forecast uncertainty is at least partly ad- flexibility, particularly for large load customers
dressed by raising the barrier to entry across all with backup or colocated resources that may
fronts for the load interconnection queue. Inter- not be fully utilized, can also drastically improve
connection studies should proceed only for proj- resource adequacy conditions, particularly dur-
ects that pass queue-maturity screening, such ing extreme events and energy shortfalls. Small-
as demonstrating site control, financial security, scale remedial action schemes (RASs) may also
technical completeness, accurate models, etc., be effective to avoid post-contingency network
thereby reducing placeholders and providing overloads that may occur within local large load
decision-grade data for planning studies. New pockets. Demand-side and grid-side solutions
load is energized in phases under flexible agree- may be able to turn inflexible loads into flexible
ments explicitly tied to deliverability milestones, assets from an operational perspective.
so additions occur only as N-1/N-1-1 capability be-
comes available. Conversely, colocated or other Grid Interface and Stability Support
“bring your own generation” constructs may also Advanced grid-stabilizing solutions are actively
enable faster interconnection while also provid- being deployed to handle the variability and
ing energy assets to support adequacy. Forecast oscillatory behavior of AI workloads. While so-
fidelity is improved with validated models and lutions are being explored at the chip and rack
standardized load ramp profiles. Grid-enhanc- levels, grid-side solutions may be required to cre-
ing technologies such as dynamic line ratings ate adequate layers of protection for grid stability
August 2026 IEEE Energy Sustainability Magazine 35
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.

Early disclosure of data center siting plans and regional
capacity thresholds could identify early discrepancies
between demand and local hosting capacity.
and equipment integrity. For example, enhanced that enhance overall reliability and stability. Le-
static synchronous compensators (E-STATCOMs) veraging their inherent infrastructure—such
and grid-forming BESSs are being explored for as UPS systems and colocated BESSs—enables
grid-connected and islanded modes of opera- them to deliver fast frequency response, reac-
tion due to their fast response times and ability tive power support, and other ancillary services.
to stabilize load spikes across a wide range of Advanced inverter-based solutions can further
network conditions. Colocated BESSs may also strengthen small-signal stability, voltage regu-
be able to provide fast frequency response and lation, weak grid stability challenges, ramp rate
dynamic reactive power support and handle fast smoothing, etc. These benefits also reduce the
ramping and variability—introducing significant reliance on conventional reserves. In addition,
opportunities for grid flexibility and reliability en- the computational flexibility of AI data centers
hancements while supporting the energy needs enables both temporal and spatial load shifting,
of the data center customers. Regardless, with improving key grid performance metrics.
the advent of complex systems consisting of lay-
ered controls and inverter-based technologies, Turning Challenges Into Strengths: AI
advanced electromagnetic transient studies Data Centers as Grid Assets
may be required to ensure reliability for both the Power system resilience focuses on the grid’s ca-
grid and the load customer. pability to withstand and reduce the magnitude
and duration of high-impact, low-probability
Monitoring, Compliance, and Market Integration events (e.g., extreme weather, cyberattacks, and
Visibility and compliance are supported by high- large-scale equipment failures) by anticipating,
rate telemetry that enables real-time m onitoring, absorbing, adapting to, and rapidly recovering
short-term forecasting, and enforcement of from such events. In the context of AI infrastruc-
ramp rate and availability limits. Instrumenta- ture, resilience frameworks should consider both
tion at the point of interconnection, including direct grid vulnerabilities and cascading impacts
phasor measurement units (PMUs), disturbance on other critical services, spanning operational
recorders, and power quality monitors, provides resilience (e.g., updated protection philosophies,
time-synchronized data to verify ride-through RAS designs, and restoration procedures) and
performance, recovery behavior, harmonic com- infrastructural resilience (e.g., grid hardening,
pliance, and model accuracy. Compliance is transmission expansion, and revised planning/
maintained through defined test procedures and design standards for large loads).
periodic audits linked to interconnection require- Resilience in power systems is not a fixed
ments, with corrective actions triggered by mea- attribute but a dynamic process that evolves
sured deviations. Market mechanisms support through continuous cycles of planning, opera-
reliability by enabling dispatchable load reduc- tions, and post-event learning (see Figure 4). This
tions from noncritical AI workloads and com- framework is increasingly critical for managing
pensating fast frequency support from UPS and new challenges and uncertainties introduced by
battery systems through performance-based large AI data centers, and it involves
settlement. These measures collectively sup- 1) anticipation: proactively planning for dis-
port proactive reliability management, verifiable ruptions by integrating AI load characteris-
operational performance, and grid-compatible tics into system design and risk analysis
behavior from AI data centers. Table 2 maps the 2) response: quickly and effectively assess-
mitigation techniques discussed in this section to ing events, deploying emergency controls,
the specific reliability challenges introduced by and coordinating restoration
the rapid expansion of large AI data centers. 3) learning: translating post-event findings
With reliability risks properly managed, large into refined models, standards, and play-
AI data centers can serve as valuable grid assets books that inform future planning.
36 IEEE Energy Sustainability Magazine August 2026
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.

/ytilibixelfnI
snoitatimiL
 esnopseR
-dnameD
 tekraM
|     | ✓ ✓ |     |     | ✓   |     |
| --- | --- | --- | --- | --- | --- |
noitanidrooC
 noitcetorP
|     | ✓   |     | ✓   |     |     |
| --- | --- | --- | --- | --- | --- |
 cinomraH /noitrotsiD ecnanoseR
|     |     |     | ✓   | ✓   |     |
| --- | --- | --- | --- | --- | --- |
/ytivitisneS
ycneicifeD
 egatloV  hguorhT
-ediR
|     | ✓ ✓ | ✓   |     | ✓   |     |
| --- | --- | --- | --- | --- | --- |
 ytilibatS
seussI
 dirG
|     | ✓ ✓ | ✓   | ✓   | ✓ ✓ |     |
| --- | --- | --- | --- | --- | --- |
snoitatimiL
 emiT-laeR
 lortnoC
|     | ✓ ✓ |     | ✓   | ✓   |     |
| --- | --- | --- | --- | --- | --- |
 noissimsnarT
.segnellahc ytilibailer retnec atad lA ot snoitulos laitnetoP 2 elbat
stniartsnoC
|     | ✓   | ✓ ✓ | ✓   |     |     |
| --- | --- | --- | --- | --- | --- |
tnemngilasiM
 ycauqedA
 ecruoseR
|     | ✓   | ✓   | ✓   |     |     |
| --- | --- | --- | --- | --- | --- |
 gnitsaceroF
ytniatrecnU
 daoL
✓
gniretlif cinomraH
sloot gnirotinom  noitcennocretni
 elbahctapsid(
|     |     |  enil cimanyD | /egatlov dna |  smsinahcem -ecnamrofrep |     |
| --- | --- | ------------- | ------------ | ------------------------ | --- |
 dna sgnitar noitazimitpo )stnemelttes
|     |           |                   |  gniludehcs  ycneuqerf |  eueuq dna |     |
| --- | --------- | ----------------- | ---------------------- | ---------- | --- |
|     | snoituloS |                   |  daolkroW  dna sUMP    | gnineercs  |     |
|     |           | MOCTATS  ygolopot |                        |  ytirutam  |     |
|     |           |                   | gnilacs  degatS        |  tekraM    |     |
 desab
 ,daol
SPU SSEB
| August 2026  |     |     |     | IEEE Energy Sustainability Magazine   | 37  |
| ------------ | --- | --- | --- | ------------------------------------- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore.  Restrictions apply.

Data centers can contribute to grid resilience in
meaningful ways, provided that policy and regulatory
frameworks evolve to enable such opportunities.
Framing resilience as this closed loop builds  ration and that the data center industry will act
systematic learning into the grid’s architecture,  as a good steward of grid reliability. Thus, creative
ensuring that as large AI data centers reshape  pathways to integrate AI data center loads at
the load landscape, resilience evolves in paral- scale can be pursued by deploying technologies
lel, guided by real-world system behavior and  and strategies that make their demand grid-
emerging threats. compatible and supportive. Looking ahead, data
centers can contribute to grid resilience in mean-
Unlocking the Resilience Potential of AI  ingful ways, provided that policy and regulatory
| Data Centers |     | frameworks evolve to enable such opportunities. |     |     |     |
| ------------ | --- | ----------------------------------------------- | --- | --- | --- |
This section pivots away from the familiar narra-
tive that casts AI data centers as “power-hungry”  Temporal Flexibility for Peak Relief
sinks with predominantly negative grid impacts.  and Variability Reduction
Instead, it envisions a near-term future where  Data centers may provide significant levels of
roadblocks  are  overcome  and  these  facilities  flexibility to the grid if they are able to ramp their
operate as grid-supportive assets. This outlook  workloads and power demands to meet grid
envisions that innovation will solve many of the  operator needs. This may include curtailing or
grid reliability risks through cross-sector collabo- reducing power demand during resource ade-
quacy or energy adequacy
|     |     |     | shortfalls,            | extreme         | events,  |
| --- | --- | --- | ---------------------- | --------------- | -------- |
|     |     |     | and  other             | emergency       |          |
|     |     |     | operating              | conditions      | [see     |
|     |     |     | Figure                 | 5(a)].  Having  | spa-     |
|     |     |     | tially  c oncentrated  |                 | “mega    |
loads” across the grid that
demand firm service may
|     |     |     | create  | challenges  | for  grid  |
| --- | --- | --- | ------- | ----------- | ---------- |
Resilience
|     |       |     | operation                   | and  reliability  |       |
| --- | ----- | --- | --------------------------- | ----------------- | ----- |
|     | Cycle |     | and require significant in- |                   |       |
|     |       |     | frastructure                | investment.       |       |
|     |       |     | Turning                     | these  loads      | into  |
flexible and curtailable as-
sets for grid operators may
result in a future grid that is
able to handle higher levels
| 1   | 2   | 3   |     |     |     |
| --- | --- | --- | --- | --- | --- |
of variable and intermittent
resources moving forward.
| Anticipation | Response | Learning |     |     |     |
| ------------ | -------- | -------- | --- | --- | --- |
Spatial Flexibility for
•  Scenario Analysis and •Assess System Damage • Evaluate System Regional Stress Mitigation
| Risk Modeling | • Deploy Emergency | Performance |     |     |     |
| ------------- | ------------------ | ----------- | --- | --- | --- |
During Extreme Events
| •  Planning for AI Data | Controls | • Identify Modeling Gaps |          |              |       |
| ----------------------- | -------- | ------------------------ | -------- | ------------ | ----- |
|                         |          |                          | Extreme  | events  are  | also  |
| Center Impacts          |          | and Coordination         |          |              |       |
• Manage Repair and
|                           |                 | Issues | generally  | regionally  | con- |
| ------------------------- | --------------- | ------ | ---------- | ----------- | ---- |
| •  Implementing Proactive | Re-Energization |        |            |             |      |
Strategies • Integrate Insights into centrated,  and  data  cen-
|     |     | Future Planning | ters may play a key role in  |     |     |
| --- | --- | --------------- | ---------------------------- | --- | --- |
shifting workloads to other
|     |     |     | synchronized  | data  | cen- |
| --- | --- | --- | ------------- | ----- | ---- |
figure 4. The resilience cycle under AI data center growth. ters  in  other  parts  of  the
| 38  IEEE Energy Sustainability Magazine  |     |     |     | August 2026 |     |
| ---------------------------------------- | --- | --- | --- | ----------- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore.  Restrictions apply.

grid or even in different interconnections [see  rates, variability limits, oscillation mitigation, etc.,
Figure 5(b)]. In practice, spatial flexibility is pri- are not well established in the United States and
marily  applicable  to  inference  and  batch-pro- present significant uncertainties to grid planning,
cessing workloads, which can be shifted across  design, and operations. Shoring up these gaps
geographically distributed data centers without  could further result in data centers being a reliable
violating latency or data-locality constraints. In  and trustworthy load that supports broader resil-
| contrast, large-scale training remains geographi- |     |     |     | ience efforts. |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
cally constrained due to data gravity, high band-
width demands, and the need for tightly coupled  Dual Role of AI Data Centers in Grid Support
high-density GPU clusters. The ability to offload  Fully leveraging the unique operational capa-
regional grid stresses during wildfires, hurricanes,  bilities of data centers and maximizing the value
derechos, and other extreme hot and cold condi- that they can bring to grid operators can improve
tions could provide grid operators with additional  local, regional, and BPS-wide stability, reliability,
tools to manage emergency conditions. and resilience moving forward. Operationally, we
may be able to think about data centers as hybrid
Leveraging On-Site Resources for Faster  assets, simultaneously serving as a highly flex-
Restoration ible load that additionally includes dispatchable
Data centers are deployed with a tremendous  resources that support energy policy goals. This
amount of on-site backup generation. These gen- can enable improved grid support services such
erators often sit dormant until a grid event happens  as ramping, peak shaving, improved fault ride-
and the UPSs initiate a transfer over to these on- through and stability, quicker system r estoration,
site generators. Historically, these generators have
been diesel gensets that are
| limited  to    | a  small  | number   |     |     |     |     |     |     |     |
| -------------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| of  operating  | hours     | due  to  |     |     |     |     |     |     |     |
Load
| environmental  | restrictions.       |     |     |     |     |     |     |     |     |
| -------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| However,       | various  colocated  |     |     |     |     |     |     |     |     |
Temporal
| and backup generation solu- |     |     | Flexibility |     |     |     |     |     |     |
| --------------------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
tions, including natural gas,
Baseline
| renewables, and BESSs, are  |                 |     | Load Profile |     |     |     |     |     |     |
| --------------------------- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| emerging.                   | Under  extreme  |     |              |     |     |     |     |     |     |
Flexible
| events or during system res- |                       |     | Load Profile |     |     |     |     |     |     |
| ---------------------------- | --------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| toration                     | efforts,  leveraging  |     |              |     |     |     |     |     |     |
the full capability and capac-
|                               |               |      |     | 12 a.m. | 6 a.m | 12 p.m | 6 p.m | 12 a.m |     |
| ----------------------------- | ------------- | ---- | --- | ------- | ----- | ------ | ----- | ------ | --- |
| ity of these resources could  |               |      |     |         |       | (a)    |       |        |     |
| enable  quicker               | restoration   |      |     |         |       |        |       |        |     |
| and  higher                   | reliability.  | How- |     |         |       |        |       |        |     |
ever, policies need to evolve
| to consider these options. |     |     |     |     |     |     |     | Cloud |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
System
Provider
| Enabling Resilience Through  |     |     | Data   |     | Data   |     |     |     |     |
| ---------------------------- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- |
|                              |     |     | Center |     | Center |     |     |     |     |
Data Center Performance
|                               |                |      |          | Data   |     | Data          |     |     |     |
| ----------------------------- | -------------- | ---- | -------- | ------ | --- | ------------- | --- | --- | --- |
| Standards                     |                |      |          | Center |     | Center        |     |     |     |
| There  are                    | currently      | few  |          |        |     |               |     |     |     |
| technical                     | requirements—  |      |          |        |     |               |     |     |     |
|                               |                |      | Workload | Data   |     | Workload Data |     |     |     |
| capability, performance, and  |                |      |          | Center |     | Center        |     |     |     |
|                               |                |      | Baseline |        |     | Flexible      |     |     |     |
utilization—that define how
(b)
large loads such as data cen-
ters must operate when con-
figure 5. (a) A temporal flexibility pathway for AI data centers. Tempo-
nected to the grid. While power
ral flexibility is achieved by modulating or shifting compute over time,
quality and interconnecting
ramping workloads and power demand to align with grid conditions, to
protection system require-
flatten peaks, fill valleys, and reduce intraday load variability. (b) A spa-
ments  may  exist,  broader  tial flexibility pathway for AI data centers. Spatial flexibility is achieved by
requirements related to ride- dynamically routing workloads across geographically dispersed facilities,
through performance, ramp  optimizing resource utilization, and mitigating local grid stress.
| August 2026  |     |     |     |     |     | IEEE Energy Sustainability Magazine   |     |     | 39  |
| ------------ | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore.  Restrictions apply.

resource adequacy deficiencies, and other resil- the future will depend not only on technologi-
ience benefits. cal advances but on the technicians, engineers,
Realizing the resilience value of AI data centers planners, operators, and skilled tradespeople
requires clear operational roles and compatible who make those advances real. Anticipating the
interconnection arrangements for hybrid facilities pace of technological change and making stra-
that are both large loads and holders of dispatch- tegic investments in research and development
able storage/generation. Streamlined processes are equally critical, ensuring that new technolo-
that recognize this dual nature (e.g., coordinated gies are practical, implementable, and ready to
treatment of load and generation interconnec- meet evolving grid demands. Embedding re-
tions, defined emergency operating modes, and silience into every layer of planning and opera-
explicit compensation mechanisms for event- tions and equipping the power sector to adapt
time services) reduce procedural friction and are key to keeping the lights on and the infor-
align incentives. Policy adjustments should focus mation flowing. If utilities, regulators, and inno-
on specifying when and how these facilities sup- vators stay focused on these priorities, the grid
port the grid during emergencies, defining data will remain a reliable, resilient, and economic
and control interfaces to enable safe coordination, foundation upon which modern society is built.
and ensuring that cybersecurity and reliability re-
quirements are met for any grid-support function. Acknowledgment
Sandia National Laboratories is a multimission
Looking Forward laboratory managed and operated by National
The rise of AI and hyperscale data centers is reshap- Technology & Engineering Solutions of Sandia,
ing electricity demand in ways that have profound LLC, a wholly owned subsidiary of Honeywell In-
impacts on grid reliability and resilience. Meeting ternational Inc., for the U.S. Department of En-
these demands requires more than steel in the ergy’s National Nuclear Security Administration
ground and wires in the air. Looking ahead, the under Contract DE-NA0003525.
electricity sector needs to remain focused on inno-
vations in the following areas: For Further Reading
➤ improving power system modeling practic- A. Shehabi, “2024 United States data cen-
es for large loads across multiple simulation ter energy usage report,” Lawrence Berkeley
timescales and domains Nat. Lab. (LBNL), Berkeley, CA, USA, Tech. Rep.
➤ incorporating the performance characteris- LBNL2001637, Dec.2024. [Online]. Available:
tics of large loads into studies for grid inter- https://eta-publications.lbl.gov/sites/default/
connection, long-term planning, operation- files/2024-12/lbnl-2024-united-states-data-cen-
al planning, and real-time applications ter-energy-usage-report_1.pdf
➤ establishing streamlined and equita- “Characteristics and risks of emerging large
ble interconnection processes that facili- loads – Large loads task force white paper,” North
tate the connection of both new large loads Amer. Electric Rel. Corporation (NERC), Washing-
and resources to meet energy and capacity ton, DC, USA, Jul.2025. [Online]. Available: https://
demands www.nerc.com/globalassets/who-we-are/
➤ ensuring clear, transparent, and fair cost standing-committees/rstc/whitepaper-charac
allocation that protects existing ratepay- teristics-and-risks-of-emerging-large-loads.pdf
ers while facilitating economic growth and R. Quint, J. Zhao, and K. Thomas, “An assess-
development ment of large load interconnection risks in the
➤ advancing policies and operating prac- western interconnection,” Western Electric-
tices that fully leverage colocated genera- ity Coordinating Council (WECC), Salt Lake City,
tion and loads to maximize grid flexibility, UT, USA, Elevate Energy Consulting, Spokane,
particularly during generation shortfalls or WA, USA, Feb.2025. [Online]. Available: https://
grid congestion www.wecc.org/sites/default/files/documents/
➤ fostering market-driven innovation to products/2025/Report_WECC%20Large%20
bring value to customers and enable novel Loads%20Risk%20Assessment%204.pdf
approaches to connect large loads effec- M. A. Mirzaei and M. Parvania, “Spatio-tem-
tively and economically. poral energy flexibility of data centers: Model-
Achieving such a vast undertaking will re- ing the impact on the western interconnection,”
quire sustained investment in workforce devel- in Proc. 59th Hawaii Int. Conf. Syst. Sci. (HICSS),
opment. Building and maintaining the grid of 2026, pp. 3141–3150.
40 IEEE Energy Sustainability Magazine August 2026
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:43:53 UTC from IEEE Xplore. Restrictions apply.