2026 IEEE Green Technologies Conference (GreenTech)
AI Data Centers and U.S. Grids: A 2026–2030
Regional Forecast
Chaitanya Chandran Melnatami
Vista Ridge HS
Cedar Park, TX, USA
chaitanyamelnatami@gmail.com
Abstract—The rapid expansion of AI-driven data centers is This paper examines how AI-centric data center growth
projected to dramatically increase U.S. electricity demand and (2026–2030) will impact the Eastern, Western, and Texas
challenge regional power grids. By 2030, data center energy could (ERCOT) grid regions. The Eastern Interconnection faces grid
reach ~600 TWh (10-12% of U.S. power). This growth will not
strain in areas like Virginia due to dense hyperscale clusters
impact all regions equally: the Eastern Interconnection e.g.
[7]. The Western region must balance slower AI data center
Northern Virginia’s massive “Data Center Alley” and Texas
growth with aggressive renewable goals and limited water
(ERCOT) face the greatest strains, while the Western
[6][11]. Texas’s ERCOT grid sees rapid expansion from data
Interconnection sees significant but comparatively smaller
impacts. Key factors such as grid infrastructure age, transmission centers and crypto mining, risking resource adequacy as
constraints, climate, state policy incentives, and local data center flexible loads could reach 60 GW by 2031 [9][10].
density create these regional differences. An empirical forecast
model (2026–2030) is developed to project data center energy use This work projects regional data center energy use (2026-
and peak loads for each interconnection, based on these drivers. 2030), identifies grid challenges, and proposes mitigation
The model indicates that without intervention, surging AI-related
strategies. [1][4]. Paper structure: Section II gives background
loads could stress legacy grid components and exacerbate peak
on U.S. grids and data center energy; Section III reviews recent
demand e.g. ERCOT’s summer peak might nearly double from
and projected regional trends; Section IV describes the
~85 GW in 2023 to ~145 GW by 2030 and complicate
empirical forecast model; Section V discusses challenges and
decarbonization efforts in some regions. Data centers already
account for ~26% of Virginia’s power use and that share may solutions by region; Section VI reviews prior research and
double by 2030. Major challenges for each grid are identified, and unique contributions; Section VII concludes with grid planning
mitigation strategies are proposed prioritizing renewable energy and policy recommendations. This work offers actionable
expansion, grid modernization, policy reforms, and demand-side insights for utilities, grid operators, and policymakers to
measures. Prior work (2017–2025) on data center energy is manage AI-driven demand while supporting reliability and
reviewed, and it is shown how this analysis extends beyond
sustainability [2][4].
existing literature by providing a region-specific, grid-focused
perspective. Results indicate that with proactive planning e.g. II. BACKGROUND
new high-efficiency capacity, transmission upgrades, flexible
U.S. Power Grids and Regional Context
operations, and clean energy integration, the U.S. grid can
accommodate the AI-driven surge in data center load while The United States is served by three primary synchronous
maintaining reliability and climate commitments. power grids (interconnections), each having distinct
characteristics:
Index Terms-- Artificial Intelligence, Data centers, Load
Eastern Interconnection: Covering about 39 states in the East
Forecasting, Power Grid, Power Usage Effectiveness.
and Midwest, the Eastern Interconnection is the nation’s
largest grid by load, operated by PJM, MISO, SERC and
I. INTRODUCTION
others. Much of its transmission and distribution infrastructure
The U.S. electric grid is confronting a major challenge from is outdated and was not built for today’s concentrated data
the rapid rise of energy-intensive AI data centers. While center demand [7][8]. Tax incentives and low electricity rates
efficiency advances kept data center energy use relatively have drawn dense clusters, especially in Northern Virginia’s
stable at ~1.8–2% of the nation’s electricity through the 2010s “Data Center Alley,” which accounted for roughly 25–26% of
[1], this changed around 2019 as compute-heavy AI workloads Virginia’s power use in 2023 [5][7]. Other major hubs are
drove demand higher. By 2023, U.S. data centers consumed found in Georgia, North Carolina, Ohio, and Illinois.
about 147 TWh (3.7% of national electricity), ending nearly a Supplying these loads strains infrastructure, as Dominion
decade of flat global data center usage [2][4]. Energy warns transmission into Loudoun County is near
/26/$31.00 ©2026 IEEE
14617411.6202.58286hceTneerG/9011.01
:IOD
|
EEEI
6202©
00.13$/62/6-4285-5133-8-979
|
)hceTneerG(
ecnerefnoC
seigolonhceT
neerG
EEEI
6202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:40 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
capacity [7]. Data center demand often overlaps with peak Energy use remains geographically concentrated: about 15
periods due to the region’s hot summers and cold winters. states account for ~80% of U.S. data center electricity, with
Ambitious clean energy targets, like Virginia’s 100% carbon- Virginia exceeding 10% by 2020 and Dominion Energy
free goal by 2045, risk being undermined if rising data center reporting ~2.6 GW load in 2022 (24% of peak demand), rising
demand is met with fossil generation [5][11]. to ~6 GW by 2035 [5][7][12]. Other major states are Texas,
California, Oregon, and Washington. Grid impacts are highly
Western Interconnection: Covering 11 states from the localized, making region-specific analysis essential.
Rockies to the Pacific, the Western Interconnection transmits Utilities and grid operators are adapting: PJM raised 2030
power over vast distances from remote sources (Wyoming forecasts after Virginia’s interconnection requests [7][8],
wind, Arizona solar, Pacific Northwest hydro) to coastal cities. ERCOT launched a “Large Flexible Load” category in 2023
The region leads in renewable integration, with California for data center and crypto loads with proposed new market
reaching 35% renewables in 2021 and retiring natural gas plants
mechanisms [9], and Oregon’s 2025 law requires large new
to achieve a 100% clean electricity target by 2045 [6]. Key data
loads to fund grid upgrades [8][13]. Hyperscalers like Google
center hubs include Silicon Valley, the Pacific Northwest, and
are shifting workloads to match renewables, aiming to lower
emerging Desert Southwest locations like Phoenix, Arizona.
emissions [6].
Challenges include aligning data center demand with variable
renewable supply, ensuring reliability during periods of low
In short, U.S. data center energy demand—driven by AI—
solar output, and managing cooling water requirements in arid
grows rapidly and unevenly, putting pressure on specific
regions. Large Western data centers rely on evaporative cooling
regional grids. The following sections will quantify this growth
towers, consuming 100–300 million gallons annually for a
single 30 MW facility, raising concerns in drought-prone states and address management strategies for each interconnection.
[6][11]. Wildfire risks and extreme heat waves prompt utilities III. ENERGY GROWTH TRENDS AND
to implement Public Safety Power Shutoffs, sometimes forcing ANALYSIS (2026–2030)
data centers onto backup generators for extended periods.
Several reports project that by 2030, data centers could
Growth must be managed in tandem with grid resilience and
account for ~10% of total U.S. power consumption, up from
decarbonization policies.
~3–4% today [2][4]. Table I summarizes a medium-case
Texas Interconnection (ERCOT): Covering most of projection for U.S. data center electricity usage in 2030, broken
Texas and operating independently, ERCOT runs an energy- down by interconnection (with 2023 values for reference).
only market and has historically maintained a reserve margin
Table I – Projected Data Center Electricity Use by 2030 (Medium
near 15% via scarcity pricing signals. Texas’s business-friendly
Scenario)
policies, ample land, and low electricity prices ($0.05–
$0.07/kWh for industrial users) have attracted data centers and
crypto miners, making Texas the second-largest data center
state with about 450 facilities as of 2023. AI-oriented data
center growth is booming, especially in the Austin–San
Antonio corridor and Dallas–Fort Worth area. ERCOT’s total
load was ~360 TWh in 2022 and could exceed 600 TWh by
2030, with data centers comprising 10–15% of consumption, up U.S. data center annual energy consumption is projected to
from ~2–3% in 2020 [9][10]. The combination of explosive quadruple from ~150 TWh in 2023 to ~600 TWh in 2030,
growth and limited power import capability poses a resource reaching approximately 10–12% of national demand [2][4].
adequacy challenge, as demonstrated during the February 2021 Eastern and ERCOT regions are expected to comprise ~75% of
winter storm when high outages led to widespread blackouts. the 2030 data center load. If AI adoption is slower and
Tens of GW of nearly continuous new load may double efficiency improves, data centers may use ~300–350 TWh in
ERCOT’s summer peak by 2031 if all proposed projects 2030 (~6% of U.S. load) [1]. Accelerated AI demand or
proceed [10]. ERCOT must build generation or manage stagnant efficiency could push usage above 700 TWh by 2030
demand response internally; however, Texas leads the nation in [4][11]. Despite uncertainty, the trend is clearly upward.
wind and solar capacity, offering an opportunity to power new
Regional Patterns: Growth remains concentrated in specific
data centers with clean energy if transmission and storage
regions:
infrastructure are expanded [9][10].
Eastern Interconnection: Anticipated to supply about half
Data Center Energy Use Patterns and Efficiency
of U.S. data center energy by 2030 (~300 TWh)—a 4x jump
Since 2019, surging AI and cloud workloads have outpaced from ~120 TWh in 2023. States such as Georgia, North
efficiency, causing U.S. data center energy to climb from Carolina, Ohio, and Illinois are adding hundreds of MW of new
~150 TWh in 2022 to a projected ~500–600 TWh by 2030 capacity. By 2030, Eastern data centers could increase by 10–
[2][4][14]. Modern AI data centers operate at much higher 15 GW of constant load, potentially comprising 20–30% of
utilization (60–80%) than traditional ones (historically <30%), peak demand for some utilities. Dominion Virginia’s peak
with PUE improving modestly from ~1.5 (2020) to ~1.3 (2030) could reach 35–40% data centers by 2030, up from ~24% in
2022 [5][7]. Substantial grid infrastructure upgrades will be
[1][8].
necessary.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:40 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
Western  Interconnection:  Data  center  consumption  is  •  U_peak,r(t) = Peak utilization: fraction of IT capacity
projected at ~120–140 TWh/year by 2030, up from ~30 TWh
in use at the time of the grid’s peak demand.
in 2020 (~4–5x growth). Growth is slower in California due to
costs and local moratoria [11], while Oregon, Arizona, and
Then the annual energy consumption E_r(t) and peak load
| Utah  are  | experiencing  | expansion,  | with  | some  | new  | sites  |     |     |     |     |     |     |
| ---------- | ------------- | ----------- | ----- | ----- | ---- | ------ | --- | --- | --- | --- | --- | --- |
L_peak,r(t) attributable to data centers in region r can be
| exceeding 200 MW. Even with improved efficiency, Western  |     |     |     |     |     | estimated by:  |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
data center load is likely to at least double by 2030, potentially
|     |     |     |     |     |     | Er(t)=I_r(t)×PUE_r(t)×U_r(t)×8760                   |     |     |     |     |     | (1)  |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | ---- |
making up ~10–15% of Western grid demand (from ~5% in
|     |     |     |     |     |     | L_peak,r(t)=I_r(t)×PUE_r(t)×U_peak,r(t)  |     |     |     |     |               (2)  |     |
| --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ------------------ | --- |
2020). Integration with a grid transitioning to renewables will
| be a key challenge.  |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Assumptions: The model is calibrated to 2022 data and then
Texas (ERCOT): The fastest growth is forecasted here,  projected through 2030 with region-specific assumptions:
with data centers expected to use ~150 TWh/year by 2030, up
Installed IT Capacity (I_r): Baseline 2022 industry values
from ~50 TWh in 2023 (~3x increase). ERCOT’s forecast
|            |         |                   |           |        |     | estimates  | (e.g.  ~8 GW  | Eastern,  | ~4 GW  | Western,  |     | ~3 GW  |
| ---------- | ------- | ----------------- | --------- | ------ | --- | ---------- | ------------- | --------- | ------ | --------- | --- | ------ |
| indicates  | “large  | flexible  loads”  | reaching  | 18 GW  | by  | 2030       |               |           |        |           |     |        |
ERCOT). Growth is added based on known expansion plans
[9][10]; if operated continuously, this equals ~158 TWh/year.
and trend extrapolation. In a medium scenario, I_r is assumed
By 2030, these loads could represent ~25% of ERCOT’s peak
to grow ~10–15%/year in Eastern, ~8–12%/year in Western,
demand and energy use (up from ~5% in 2020) [9][10]. This
and ~20%/year in ERCOT through 2030 (reflecting numerous
shift creates a 24/7 base load, potentially reducing ERCOT’s
large projects in Texas). This yields roughly a doubling of
planning reserve margin to near zero in extreme cases [10].
Market adjustments, new generation, and load flexibility will  Eastern capacity, ~2.5x in Western, and ~3x in ERCOT by
2030, in line with forecasts [2][10].
be required.

|     |     |     |     |     |     | Power  Usage  |     | Effectiveness  | (PUE_r):  |     | Gradual  | PUE  |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --------- | --- | -------- | ---- |
  improvement over time is assumed. Many new hyperscale data
|     |     |     |     |     |     | centers  achieve                                           |     | PUE  ~1.2–1.3,  | but  | the  fleet  | average  | is  |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --------------- | ---- | ----------- | -------- | --- |
|     |     |     |     |     |     | projected to improve from ~1.5 in 2022 to ~1.3 by 2030 as  |     |                 |      |             |          |     |
  older sites are upgraded and new efficient designs come online.
Hotter climates (Texas and Arizona) are expected to have

slightly higher PUE (~1.3–1.35) due to greater cooling needs,
|     |     |     |     |     |     | whereas cooler regions (Pacific Northwest) could average  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
~1.2. No major breakthroughs (like widespread liquid cooling

or server photonics) are assumed by 2030, consistent with
|     |     |     |     |     |     | industry outlooks [1][6].  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |

Fig 1: US Power Interconnections & Data Center Hubs
|     |     |     |     |     |     | Average  | utilization  | (U_r):  | Historically,  |     | average  | server  |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ------- | -------------- | --- | -------- | ------- |
All scenarios indicate a significant increase in data center  utilization was low (~20% for enterprise data centers). Cloud
energy use by 2030. Adaptation in generation, transmission,
|     |     |     |     |     |     | and  AI  | workloads  | are  assumed  |     | to  drive  | much  | higher  |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------- | --- | ---------- | ----- | ------- |
and operations will be required by grid operators. An empirical
utilization. U_r is projected to rise over time and is considered
| model  quantifying  |     | electricity  | demand  | and  | peak  | load  |     |     |     |     |     |     |
| ------------------- | --- | ------------ | ------- | ---- | ----- | ----- | --- | --- | --- | --- | --- | --- |
region-agnostic (since it depends more on workload type).
| contributions  | will  | be  presented  | in  the  | following  | section,  |     |     |     |     |     |     |     |
| -------------- | ----- | -------------- | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
forming the basis for impact analysis in Section V.  Baseline 2022 U ~0.5 (50%) for hyperscale operators [1],
reaching ~0.6–0.7 by 2030 as AI workloads (which often run
at 70–90% utilization around the clock) constitute a larger
| IV.  | FORECAST MODEL FOR DATA CENTER  |     |     |     |     |     |     |     |     |     |     |     |
| ---- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ENERGY LOAD  share. This aligns with reports that AI training clusters are kept
near fully busy to maximize expensive hardware use [4].
 A projection model links IT capacity, PUE, and utilization to

| energy  consumption  |     | and  peak  | load  including  |     | installed  | IT  |     |     |     |     |     |     |
| -------------------- | --- | ---------- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Peak utilization (U_peak,r): Data center loads tend to be flat
capacity, facility efficiency, utilization, etc. For a given region
or only moderately weather-sensitive. U_peak is assumed to be
r and year t, define:
~0.9 (90% of servers active) in Eastern and Western regions,
•  I_r(t) = Installed IT capacity (MW): the total power  reflecting some diversity or demand response, and U_peak
draw of all data center IT equipment if running at full  ~1.0 in ERCOT, reflecting that many Texas data centers are
expected to run continuously and ERCOT’s peak (summer late
load.
afternoon) does not significantly curtail their usage. If demand-
•  PUE_r(t) = Power Usage Effectiveness: ratio of total
response programs are effective, U_peak could be lower (as
facility power to IT power (dimensionless; lower is
|                   |     |     |     |     |     | data  centers              | temporarily  | shed  | loads  | at  peak),  |     | which  is  |
| ----------------- | --- | --- | --- | --- | --- | -------------------------- | ------------ | ----- | ------ | ----------- | --- | ---------- |
| more efficient).  |     |     |     |     |     | discussed in mitigations.  |              |       |        |             |     |            |

| •  U_r(t)  | =   | Average  | IT  utilization:  | fraction  |     | of  IT  |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
capacity actually used on average (0–1).  Sensitivity Analysis: Leading hyperscalers achieved PUE 1.1-
1.2 in 2025 (Google: 1.10, Meta: 1.15, Microsoft: 1.18), but
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:40 UTC from IEEE Xplore.  Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
fleet average remains ~1.4 due to legacy facilities. This model for large campuses (e.g., Georgia). Advanced technologies like
assumes air cooling with incremental efficiency gains. dynamic line ratings and power flow controls optimize
Widespread adoption of liquid cooling or server photonics capacity until new lines are ready. Demand response programs
could reduce PUE to ~1.05 by 2030, lowering projections by also help temporarily by shifting loads or using on-site
15-20%. However, liquid cooling faces infrastructure costs and generation during peak hours [7]. Substantial, timely
retrofit challenges, limiting near-term deployment. investment in grid infrastructure is essential to support AI-
driven load growth.
Table II – Parameter Sensitivity (2030 Projections)
Challenge E2: Aging Infrastructure & Reliability Risks. Much
of the Eastern interconnection’s infrastructure is decades old,
and large constant loads accelerate wear and reduce margins.
Transformers, underground cables, and switchgear in urban
and suburban tech hubs are handling higher continuous
currents than originally designed for, leading to overheating or
overloading during peaks. For instance, a 40-year-old 138 kV
cable serving a data center cluster may now operate near its
This model reproduces known 2022 values (e.g. ~150 TWh
thermal limit year-round, increasing risk of equipment failures
total U.S. data center energy [2]) and yields 2030 estimates
consistent with Table I earlier. It forms the basis for quantifying and outages that could impact both data centers and local
certain impacts: e.g. how much new peak capacity is needed in communities. These concentrated loads may also alter power
ERCOT (from Eq. 2), or how much energy could be saved by flow patterns, necessitating updates to protection settings and
efficiency (from Eq. 1). Using this model, the next section voltage control schemes. Without targeted upgrades, a single
explores, for each interconnection, the top challenges posed by utility equipment failure could disrupt significant loads,
data center growth and how they can be addressed. including critical IT services.
V. CHALLENGES & MITIGATION Mitigation: Prioritize modernizing grid infrastructure in data
STRATEGIES center hubs by replacing or upgrading transformers, cables,
Based on the above trends and model results, each major breakers, and protection systems [12]. Dominion’s 2023–2027
grid region faces specific challenges from AI data center plan commits significant funding to such reliability upgrades
expansion. We focus on two key challenges per region and in Northern Virginia [12]. Deploy advanced monitoring and
discuss potential mitigation strategies for each. Some automation (e.g., fiber-optic sensors, SCADA) to manage grid
challenges (e.g. infrastructure needs) are common across conditions and voltage. Data centers can enhance reliability by
regions, but the details and priorities differ. increasing redundancy (multiple feeds, on-site backup,
storage) and participating in fast frequency response programs
A. Eastern Interconnection (Eastern U.S.)
to stabilize the grid [14]. Incentivizing grid services and
Challenge E1: Transmission & Distribution Constraints in
updating T&D infrastructure are vital for maintaining
Data Center Hubs. The main bottleneck in the Eastern grid is
reliability amid rapid load growth.
delivering enough power to concentrated data center hubs,
especially in Northern Virginia. High-voltage transmission
B. Western Interconnection (Western U.S.)
lines and local substations in Loudoun and Prince William
Challenge W1: Generation-Load Mismatch & Renewable
counties are nearing capacity due to the surge of data center
Integration. Issue: The Western grid is adding substantial solar
connections. In 2022, Dominion Energy reported that several
and wind while retiring fossil plants, but data centers consume
500 kV transmission circuits into Loudoun County faced
power constantly and do not natively respond to supply
overload risks, potentially delaying new data center
variability. This mismatch can result in high data center
connections until upgrades were finished [7]. Similar
demand during low renewable output (e.g., at night or during
constraints exist around Atlanta, GA, and Columbus, OH,
wind lulls), requiring more gas generation or imports and
where numerous 100+ MW interconnection requests strain the
raising CO₂ emissions unless mitigated [6][11]. Conversely,
network. Without upgrades, these bottlenecks could hinder
abundant renewable generation may be curtailed if data center
data center expansion or cause local reliability issues such as
loads are not flexible. The California Energy Commission
voltage drops or thermal overloads during hot weather.
(2025) warned that data center growth could boost natural gas
use during peak net-load hours if demand is not shifted or
Mitigation: Accelerate grid upgrades and modernize delivery
paired with storage, hindering clean energy targets [11]. The
networks. Utilities and grid operators are fast-tracking
core issue is aligning flat data center consumption with
transmission and distribution improvements for data center
variable renewable production.
growth in the Eastern region—such as PJM’s $1 billion
package for new lines and substations in Northern Virginia [8],
Mitigation: Integrate data centers into the clean energy
with expedited permitting by Virginia regulators [7][12].
transition through storage and flexible operations. (1) Use
Distribution enhancements include high-capacity substations,
utility-scale and on-site batteries to shift renewables to cover
transformer and feeder upgrades, and dedicated 115 kV feeds
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:40 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
data center loads during low generation periods—California [9][10]. If resource additions lag, reserve margins may erode,
targets >10 GW of batteries by 2030 for evening discharge [6]. increasing the likelihood of reliability events such as
Some data centers cycle backup batteries daily for grid emergency load shedding during extreme weather.
support. (2) Employ demand response by scheduling non-
essential workloads when renewable output is high; cloud Mitigation: Generation and storage additions are being
providers like Google already shift computing to cleaner times, accelerated through market reforms and state initiatives. (1) In
and even 10–20% load flexibility flattens peaks. CAISO 2023, the Public Utility Commission of Texas approved the
incentivizes participation through flexible demand programs Performance Credit Mechanism (PCM), incentivizing new
[6]. (3) Pair data center growth with direct renewable dispatchable generation by rewarding availability during tight
procurement and smart siting, such as co-location near conditions [9]. PCM implementation by 2025, with sufficient
renewable-rich regions and on-site generation with storage for revenue for 10–20 GW of new gas peakers or demand response
grid reliability [5]. Policies like time-of-use rates, demand by 2030, is crucial. (2) The Texas Energy Fund (S.B. 2627)
response contracts, and clean energy standards for large users will provide up to $10 billion for backup generation and
are key to aligning data center demand with renewable reliability projects [9]. Rapid deployment of this fund to build
integration goals. or upgrade peaking plants is critical, with ERCOT projecting a
need for ~7–10 GW of new dispatchable capacity by 2030
Challenge W2: Long-Distance Transmission & Siting [10]. (3) ERCOT’s renewable and storage pipeline includes
Challenges. Issue: New or upgraded transmission is often over 20 GW of solar and 5 GW of batteries by 2025 [9].
required for Western data centers to access remote generation, Integration of these resources, supported by transmission
but projects face complex permitting, environmental reviews, expansions, is planned to meet new data center demand.
and local opposition. For example, the SunZia project took Battery storage, set to exceed 10 GW by 2030, will help
over a decade to permit due to route issues [15]. Local siting manage evening and winter peaks. (4) Demand response
challenges also arise, such as concerns over noise, water use, programs already enroll ~1.8 GW of “controllable load”
and infrastructure strain in communities like Silicon Valley, (mainly crypto mines) [10]. Expansion to data centers, with
central Washington, and Phoenix [11]. The main challenges backup generators and interruptible rate contracts, is
are to ensure timely construction of bulk transmission for data encouraged. Overall, Texas is reforming its market, funding
center hubs and to minimize local impacts through careful site reliable generation, and deploying renewables and storage to
selection and design. maintain ERCOT’s reliability amid AI-driven demand.
Mitigation: Streamline transmission development and adopt Challenge T2: Minimal Import/Export Capability (Isolated
strategic data center siting to minimize conflicts. (1) Grid). ERCOT’s limited interconnections (<1 GW DC ties)
Accelerate projects with federal and state policy support, mean it cannot rely on neighboring grids for support. As data
leveraging “National Interest Electric Transmission Corridors” center loads grow, this isolation heightens risk; ERCOT must
for faster approvals [15]. (2) Use existing corridors and manage large load swings and supply shortages alone. The
advanced technologies like HVDC and high-capacity 2021 winter crisis underscored the vulnerability, and rising
conductors to boost transmission with less land impact, as seen constant loads could increase the risk of emergency load
with underground HVDC along California’s I-5. (3) Site data shedding unless internal reserves are strengthened.
centers in industrial areas, near substations, or on former plant
sites to reduce community disruption; employ advanced Mitigation: ERCOT is enhancing reserves by considering
cooling, including water-free or recycled water systems, to new HVDC interconnections, expanded demand-side reserves,
address noise and water issues [6]. Engage communities and and backup generation. (1) New DC ties, such as a 1000 MW
offer local grid upgrades and economic benefits to secure link to Louisiana or Oklahoma, are being discussed to provide
support [5]. Overall, responsible grid expansion and smart emergency support; in 2022, a 2000 MW emergency-only tie to
the Eastern grid was proposed [9]. (2) Texas plans to maintain
siting will enable Western Interconnection to balance data
a larger internal reserve margin, with the Energy Fund investing
center growth with environmental and social objectives.
in grid-scale backup generators, aiming for a strategic reserve
of several GW by 2030. (3) Emergency interruptible programs
C. Texas (ERCOT)
for data centers, allowing rapid curtailment, and leveraging
Challenge T1: Rapid Demand Growth vs. Supply Expansion.
onsite generation to feed power back to the grid during
ERCOT faces unprecedented demand growth—about 5–6%
emergencies are being explored [14]. These measures
per year through 2030, far exceeding its historical ~2% rate
strengthen ERCOT’s self-reliance and, combined with
[10]. The main challenge is ensuring generation and grid
generation and transmission expansions, should enable the grid
capacity keep pace. ERCOT’s energy-only market relies on to handle growing AI loads while maintaining reliability
price signals to drive new capacity, but surging data center standards.
loads may cause signals to lag or spike excessively. In 2022–
2023, record summer peaks and conservation appeals VI. PRIOR WORK AND COMPARISON
highlighted the risk; by 2030, summer peaks could regularly
From 2017–2025, studies showed data center energy use
surpass the current firm generation capacity of ~90 GW
stayed flat with just a ~6% increase from 2010–2018 despite a
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:40 UTC from IEEE Xplore. Restrictions apply.

2026 IEEE Green Technologies Conference (GreenTech)
550% jump in compute instances [1]. This led to optimism that directly affect generation needs, transmission infrastructure, [15] U.S. Dept. of Energy, “Designation of National Interest Electric
ongoing efficiency could contain energy demand. However, and grid operations in key regions. Transmission Corridors,” Federal Register, vol. 88, no. 45, Mar. 20
since 2019–2022, efficiency gains have slowed and AI-driven
demand has surged, causing usage to rise. The IEA warned in Empirical modeling indicates that Eastern Interconnection
2023 that global data center energy could double by 2030 if AI faces challenges in upgrading transmission and distribution
growth continues rapidly, ending the previous plateau [4]. This systems to serve new load clusters, such as those in Virginia
analysis’s projections match IEA’s high scenario, indicating and Georgia, while meeting clean energy goals and ensuring
data center loads could be a major grid factor by 2030. equitable cost allocation. Utilities in the East and PJM have
initiated grid upgrade programs; the continuation of these
Recent national reports (McKinsey 2024, EPRI 2024, efforts and implementation of special tariffs for high-load
Lawrence Berkeley National Lab) forecast substantial users are essential. The Western Interconnection must
increases in data center loads and emissions unless the grid mix integrate large, constant data center loads amid rising
improves [2][3][11]. McKinsey (2024) estimates U.S. data renewable energy penetration, requiring expanded energy
centers may reach ~570 TWh by 2030 (~12% of total demand), storage, demand flexibility, and strategic siting to minimize
echoing this study’s medium scenario [2]. This analysis also water and local impacts. Ultimately, the intersection of digital
highlights grid reliability risks, noting ERCOT’s reserve and energy sectors via AI data centers presents both risks and
margin challenges and PJM’s transmission needs in Virginia opportunities. Success will depend on coordination among
topics rarely addressed in earlier literature that focused mainly data center operators, utilities, and regulators. Proactive
on energy and carbon metrics. Prior literature highlights management can drive grid modernization and accelerate clean
improving PUE and achieving “24/7 renewable energy” as key energy adoption, using data center demand to support
strategies [1][6]. Unlike previous national, global, or state- renewable investment and justify transmission upgrades.
focused work [1][4][11], this study provides a region-specific Neglect could increase grid stress and emissions. Early,
comparison: Texas prioritizes capacity, the West targets region-specific planning is crucial. Encouragingly, many
renewable integration and water impacts, and the East stakeholders are pursuing the right strategies. By continuing to
addresses infrastructure expansion and cost allocation. expand capacity, strengthen networks, improve efficiency, and
leverage flexibility, reliable support for AI growth and clean
Economic Impact Analysis energy progress can be achieved, turning potential strain into a
catalyst for a smarter, greener grid.
Table III – Regional mitigation Strategies Comparison Projected
REFERENCES
[1] E. Masanet et al.,“Recalibrating global data center energy-use
estimates,” Science, vol. 367, no. 6481, pp. 984–986, 2020.
[2] B. Atamturk et al.,“The coming wave of data center demand: How
AI and cloud are reshaping power needs,” McKinsey Energy
Insights, Sep.2024.
[3] Electric Power Research Institute (EPRI), U.S. Data Center Energy
Consumption Projections, Product ID: 3002031198, 2024.
[4] International Energy Agency, “Data Centres and Data
Transmission Networks – Analysis,” IEA, Oct. 2023.
[5] Pew Research Center, “What we know about energy use at U.S.
Note: Costs include both public and private investment. Industrial users in data data centers amid the AI boom,” Pew Research Center – Short
center zones may see 5-10% rate increases by 2030 without cost recovery Reads, Oct. 24, 2025.
mechanisms [6] Chen, X., Wang, X., Colacelli, A., Lee, M., & Xie, L., “Electricity
Demand and Grid Impacts of AI Data Centers: Challenges and
These estimates assume proactive infrastructure investment. Prospects,” arXiv preprint arXiv:2509.07218, 2025
Delayed action could increase costs 30-50% due to emergency [7] M. Turner, Loudoun County, Virginia: Data Center Capital of the
World — “A Strategy for a Changing Paradigm”, Loudoun County
construction premiums and reliability events. In summary, this
Board of Supervisors, Oct. 20, 2025.
work confirms the rise in data center energy use and the need [8] PJM Resource Adequacy Planning Department, 2025 Long-Term
for efficiency and clean energy, while expanding the scope to Load Forecast Report, PJM Interconnection, Jan. 24, 2025
grid infrastructure and tailored regional strategies—delivering [9] ERCOT, “Report on Capacity, Demand and Reserves (CDR),”
Dec. 2024.
a more holistic perspective than earlier research, which largely
[10] Z. Skidmore, “Texas power demand could reach 218 GW by 2031,
centered on IT efficiency or general energy/emissions analysis. fueled by data centers,” Data Center Dynamics, Apr. 2025.
[11] A. Cantú, “The insatiable energy demands of data centers could
increase fossil fuel emissions in California,” Capital & Main, Oct.
VII. CONCLUSION 1, 2025.
[12] Dominion Energy, 2023 Integrated Resource Plan, Richmond,
The rapid expansion of AI-focused data centers is set to
VA, May 2023 (Appendix 5: Data Center Load).
reshape U.S. power grids by 2030, potentially driving data
[13] Oregon HB 3546, 82nd Legislative Assembly – 2023, “Relating to
centers to consume around 10% of national electricity—up energy load; establishing large energy consumer rate classes,” Jul.
from about 3–4% in 2020—with highest concentrations in the 2025.
[14] Review of Challenges and Research Opportunities for Control of
Eastern and Texas interconnections [2][4]. This growth will
Transmission Grids,” IEEE Xplore, Document 10589406.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:44:40 UTC from IEEE Xplore. Restrictions apply.