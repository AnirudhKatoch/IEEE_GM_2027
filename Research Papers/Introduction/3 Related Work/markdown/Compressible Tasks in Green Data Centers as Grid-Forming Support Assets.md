Compressible Tasks in Green Data Centers
as Grid-Forming Support Assets
Anna Vandi Ramon Aparicio-Pardo Guillaume Urvoy-Keller
Universite´ Coˆte d’Azur, CNRS, I3S Universite´ Coˆte d’Azur, CNRS, I3S Universite´ Coˆte d’Azur, CNRS, I3S
Sophia-Antipolis, France Sophia-Antipolis, France Sophia-Antipolis, France
Abstract—Renewable microgrids can help data centers cope inverter-based resources (IBRs), lacking the inertia of con-
withtheincreasingdemandforcloud-basedservices,buttheypay ventional rotating machines operating at 50 Hz, can cause
the price of the double uncertainty of workload and renewable
frequencydeviationsthatthreatengridstabilityandpotentially
resourceavailability.Themismatchbetweendemandandrenew-
trigger cascading failures and blackouts [4].
ablesupplypreventsmicrogrid-baseddatacentersfromachieving
full autonomy, requiring connection to the main grid. However, To mitigate these effects, modern power systems increas-
while imports from the main grid could increase environmental ingly rely on grid-forming control, which refers to the ca-
impact, the massive export of excess renewables, when injected pability of enforcing voltage and frequency in the main
into the grid, can cause serious instability in the system. This
grid [5]. However, frequency stability remains challenging in
work addresses both issues using compressible tasks, whose
renewable-richgridsduetofastandunpredictablepowervari-
concaveutilityfunctionsallowfortheadaptationtotheavailable
resources, reducing or increasing the task size with negligible ations[6].Inthiscontext,itbecomesnecessarytoenhancethe
impactonthequalityprovidedtotheuser.Byabsorbingsurplus autonomy of data centers from the main grid by minimizing
renewable energy, they help maintain frequency stability in the energy imports and exports. Two metrics are generally used
main grid, thereby supporting grid-forming operations. We cast
to capture the two aspects: (i) the Self-Sufficiency Rate (SSR),
thisproblemasanoptimizationproblemthatdynamicallyadapts
thetasksizebasedonrenewableavailability.WedevisedOnline- whichmeasurestheshareofdemandcoveredbyrenewableen-
REATA, an online heuristic able to manage tasks arrivals on the ergy,indicatingthesystem’scapacitytooperateindependently,
fly. Tested in a live video transcoding case study and compared and (ii) the Self-Consumption Rate (SCR), which measures
to a solution without task compression, Online-REATA achieves the share of renewables absorbed locally, showing how much
the same average QoE and self-sufficiency, as well as higher
renewable energy the system can use. We consider SSR and
self-consumption, while reducing storage requirements by up to
SCR as defined in reference [7], which counts the energy
35.3%.
Index Terms—green data center; sustainability; grid-forming. stored in the battery as part of the renewable supply.
Inthiswork,weproposetosupportgrid-formingcontrol
by adapting workloads to renewable availability through
I. INTRODUCTION
compressible tasks, whose size can be flexibly adjusted to
In recent years, increasing attention is devoted to the absorb renewable fluctuations. Compressible tasks [8], [9]
substantial rise in Data Centers (DCs) energy consumption are computational jobs where the utility function is concave:
resultingfromtheexpandingdemandforcloud-basedservices compressing them (i.e., reducing their length, and resource
[1]. This expansion is expected to continue in the coming usage) slightly degrades their utility, while increasing them
years,amplifyingtheurgencyofidentifyingsustainableenergy enables absorbing surplus energy that would otherwise desta-
solutions[2],[3].GreenDataCenters(GDCs)withmicrogrids bilize the grid. Then, our main contributions can be listed as:
for on-site renewable production are an effective response,
1) We model compressible task allocation within green
aiming for self-sufficiency and reduced dependence on the
data centers as an offline optimization problem. We
main grid. However, they need to address the mismatch
then develop an online heuristic algorithm that jointly
between energy demand and production, due to the inherent
addresses renewable surplus and shortage by leveraging
intermittency of renewable energy.
compressible tasks as grid-forming-supportive loads,
On one hand, GDCs often have to import energy from
capable of enhancing frequency stability.
the main grid (semi-autonomous green data centers), typically
2) We conduct a case study on live video streaming,
with a carbon intensity that is country-dependent and rarely
adjusting the transcoding task size to reduce interac-
fully renewable. On the other hand, in case of renewable
tion between the microgrid and the main grid. Our
energy surplus, data centers connected to the main grid often
results demonstrate that our proposal can increase self-
send extra renewable energy back to the grid, affecting its
consumption and self-sufficiency while reducing battery
stability. This is because variable renewable generation from
size.
ThisworkhasbeensupportedbytheUCAJEDI(ANR-15-IDEX-01)and
The paper is organized as follows. Section II reviews the
EURDS4H(ANR-17-EURE-004)projects,andbytheFrance2030program
undergrantagreementsNo.ANR-23-PECL-0003. related work, Section III presents the model, Section IV
979-8-3195-4209-0/26/$31.00 ©2026 IEEE
58478511.6202.16495CCI/9011.01
:IOD
|
EEEI
6202©
00.13$/62/0-9024-5913-8-979
|
snoitacinummoC
no
ecnerefnoC
lanoitanretnI
EEEI
-
6202
CCI
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore. Restrictions apply.

introduces the case study, Section V reports the evaluation for longer periods [12]. In this work, rather than shifting
and results. Section VI summarizes our conclusion. demand in time or space, our approach adjusts the
duration (size) of workloads to better match available
II. RELATEDWORK
generation from the local microgrid.
The uncertain nature of renewable energy production can The closest related study is [10], which explores quality
result in deficits and surpluses [7], which can be compensated degradation to reduce grid imports in distributed DCs (some
for by importing and exporting energy to and from the main are grid-connected, other are autonomous and equipped with
grid, respectively. Imports occur in data centers equipped Photovoltaic (PV) and/or batteries). It proposes load nego-
with renewable energy systems but also connected to the tiation, consolidation, and resolution switching to a lower
main grid, importing energy whenever renewable production video quality under resource scarcity. These three strategies
is insufficient. Scientific literature largely focuses on reducing combined yield a +7.83% SCR increase and 35.7% footprint
grid imports to lower carbon emissions [10], while the issue reduction. In contrast to our work, authors in [10] do
of exports remains less explored. When there is a surplus of not provide a quantification of the degradation, neither
renewable energy generated, this energy needs to be exported theyenvisagequalityenhancementstomanagethesurplus.
to the main grid. However, the exported energy derived from Finally, the authors of [10] address excess generation in
inverter-based resources (IBRs) including renewable energy reference[12],bymodelinginterconnectedDCsthatexchange
generators(wind,solar)andbatteries,candestabilizethegrid. surplus energy through the main grid (imports from one can
Unlikeconventionalsynchronousgenerators,IBRslackinertia be offset by simultaneous exports from another). In contrast
andprovidelimitedshort-circuitcurrent,makingfrequencyde- to us, this mitigates the issue only economically, without
viations more likely and potentially leading to cascading out- resolving the physical limitations of large renewable injec-
ages[4].Reference[7]proposedfocusingonself-consumption tions into the grid.
and peak shaving to reduce energy exports and imports, yet Summing up, existing approaches mainly address imports
presenting these two objectives as mutually exclusive. In our or exports separately, without exploring the potential of lever-
proposal, we argue that the real objective should be to aging compressible tasks to jointly mitigate both issues.
reduce overall interaction with the main grid, reducing
dependence during imports and alleviating stability issues III. RENEWABLEENERGYAWARETASKALLOCATION
during exports. Let a compressible task j be characterized by a concave
An approach that can jointly mitigate both shortages and utility function U j (x j ), which mirrors the Chebyshev approx-
surpluses is the usage of an Energy Storage System (ESS). In
imation error model and its saturation behavior [13]. It is
[3], the authors compare a grid-dependent system with differ-
defined as:
ent autonomous DC configurations, showing that combining
a Battery Energy Storage System (BESS) with a Hydrogen U j (f j =F ·x j )=1−τ j ·exp(−θ j ·F ·x j ) j ∈J (1)
Energy Storage System (HESS) offers the best performance
toward full autonomy. Full autonomy remains cost-prohibitive The utility depends on the CPU usage x j allocated to the
compared to European energy prices. The leap from 95% to task j (x j can be larger than one, if more than a CPU core
100% renewable coverage requires a disproportionate infras- is used). Considering F the core frequency, the number of
tructureincrease(fivetimesthe0-95%requirement),makingit cycles per second used by each task j is f j = F ·x j. The
economically and environmentally unsustainable [11]. More- coefficients θ j and τ j are task-specific parameters and capture
over, the environmental impact of battery production reduces task efficiency. Notations in this section are summarized in
the benefits, suggesting hybrid solutions as a more realistic Table I. Time is modeled at two granularities: at the coarse
alternative. In this work, we show that compressible tasks scale, discrete time slots t ∈ T represent the periods over
canlowertherequiredbatterysize,whilesupportinggrid- which the renewable energy input R t may vary. At the fine
forming by reducing grid interactions. scale, intervals i ∈ I are defined between consecutive task
Previous studies have proposed shifting the execution of arrivals or completions, during which the active task set is
tasks over time or space to match renewable availabil- constant.
ity—either delaying tasks or migrating them across data For each task j, Eq. (2) defines X j min as the minimum
centers [10]–[12]. However, both approaches present major number of cores required to ensure its baseline utility Umin.
drawbacks. Spatial shifting increases the carbon footprint due
(cid:4) (cid:5)
toVMmigrationenergycosts,especiallywhennetworkpower
(cid:2) (cid:3) ln 1−Umin
isn’t green, and its efficacy is limited by latency constraints, Xmin =U−1 Umin =− τj (2)
bandwidth, and destination resource availability [12]. More- j (cid:6) j θ j ·F
over, spatial distribution causes loss of global system knowl- P t m i in = P ·X j min t∈T,i∈I t (3)
edge and communication overhead [10]. Temporal shifting
j∈Ji
requires extra server capacity, leading to higher embedded
carbon [11]. Finally, combining both strategies may increase Given J t,i the set of active tasks in (t,i) and Pmax the
total energy use, because more servers must stay powered on power consumed by a single core at full utilization, Eq. (3)
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore. Restrictions apply.

TABLE I: Notation. xxx = x tj are the decision variables representing the CPU
allocation for task j at slot t, and S ti denotes the imported
Name Description
power required to meet the minimum allocation demand. The
T Setoftimeslots.Aslott∈T isaperiod
objective function (5a) maximizes the aggregate utility of
ofunchangingrenewablepowerlevels.
It Setofintervalsintimeslott.Aninterval active tasks, subject to the minimum utility requirement (5c)
i∈It isaperiodwithoutchangeinthe and the power budget constraint (5b).
J n T u o m tal be ta r s o k f s a s c e t t i . vetasks. Online-REATA. To tackle the online version of the REATA
J
i
Setofactivetasksatintervali. problem, where tasks are assigned as they arrive, we devise
H i Subsetofactivetaskswithutility a heuristic algorithm from applying the Karush-Kuhn-Tucker
largerthantheminimaloneatintervali.
L i Subsetofactivetasksatminimalutility (KKT) conditions [14] to the formulation (5). Unlike the
atintervali. offline case, tasks’ characteristics are not available in advance
l∈I
k
Themostloadedintervalduringtaskk.
butrevealedovertime,anddecisionsarebasedonlyoncurrent
A N l il ∈Z ≥0 T A h rt e ifi m ci a a x l im ta u sk m s l s o e a t: d ta d s u k r s in a g dd ta e s d k t k o . setJ i task states and predictions about future states. We decompose
togetthemaximalloadN l. theoracleformulationinto|J|subproblems,eachsolvedupon
x tj ∈R ≥0 NumberofCPUcores(CPUusage)used thearrivalofataskk ∈J.Here,thenotationrelatingtoslots
U j (x j )∈R ≥0 b U y til t i a t s y k o j ft a a t s s k lo j t a t t . CPUusagex j. t∈T will be omitted (R t →R, S ti →S i).
Umin∈R ≥0 Minimalutility. Assuming that tasks j ∈ J i \ k from other intervals are
X j min∈R ≥0 Valueforx j atminimalutility. optimally allocated, and that constraints (5b) can be replaced
F ∈R ≥0 CPUcorefrequency(inGHz). with the tightest one, i.e., the one corresponding to the most
f tj ∈R ≥0 t E a f s f k ec j tiv a e t C sl P ot U t f ( r i e n qu G e H nc z y )( u f s j ed = to F p · e x rf j o ) r . m loaded interval l during the task k, the problem reduces to
θ j ∈R ≥0 Decayrateconstantof1−U j (x j ). Eq. (6):
τ j ∈R ≥0 Valueof1−U j (x j )atzeroCPUusage (cid:6)
R S t t i ∈ ∈ R R ≥ ≥ 0 0 ( R P x o e j w ne = e w r a 0 ( b W ) l . e ) p im ow po e r r te ( d Wa a t t ts s ) lo a t t -i s n l t o e t rv t a . lpair(t,i). m {x a k x } U k (x k ) s.t j . ∈J l \k x∗ j +x k ≤ R+ P S l, x k ≥X k min (6)
P ∈R ≥0 Maxcorepowerconsumption(W). By convexity, KKT conditions yield the allocation rule:
λ μ P j t m ∈ i ∈ i R n R ≥ ∈ ≥ 0 0 R ≥0 P L L o a a w g g r r e a a r n n g g (W e e ) m m t u u o l l t t a i i p p s l l s i i u e e r r r e f f o o U r r m c c i o o n n n a s s t t t r r s a a l i i o n n t t t -i ( ( n 5 5 t b c e ) r ) . v . al(t,i). x∗ = (cid:7) X k min (cid:4) (cid:5) if λ>U k (cid:5)(X k min) (7)
k − 1 ln λ if λ≤U(cid:5)(Xmin)
θ F τ θ F k k
k k k
calculates the minimum power requirement at slot t and inter- wherethedualvariableλisobtainedfromtheconstraint(5b):
val i. The resource allocation problem is therefore to assign
{x j } j∈Jt,i such that x j ≥ X j min, ∀j ∈ J t,i, maximizing ⎛ (cid:11) (cid:12) (cid:13) (cid:12) ⎞
a se g t gr J e i ga i t s ed pa t r a t s i k tio u n t e il d ity i . nt A o t H ea i ch = in { t j er ∈ val J i i ∈ : U I t j , (x th t e j ) ac > tiv U e j m ta in s } k λ=exp ⎜ ⎜ ⎜ −F R+ P S l − j∈Li X (cid:12) j min + j∈Hi ln(τ θ j j θjF) ⎟ ⎟ ⎟
a re n q d ui L re i d = to {j sa ∈ tis J fy i a : l U l b j ( a x se tj li ) ne = a U ll j o m c i a n t } io . n T s h i e s: minimum import ⎜ ⎝ j∈Hi θ 1 j ⎟ ⎠
(cid:2) (cid:3)
S ti =max 0,P t m i in−R t , t∈T, i∈I t (4) The λ value computed as in Eq. (8) can be used in t ( h 8 e )
Allocations {x tj } are updated only at the coarse scale t∈T, allocation rule (7) to determine if the optimal allocation x∗ k
while within each interval i, variations in due to task arrivals of the task k is equal or larger than Xmin, by replacing λ
k
and departures are compensated by adjusting imports S ti. in (7) when x∗
k
> X
k
min. The full mathematical derivation is
Oracle solution. The allocation problem, which we refer to described in Section I of the supplementary material.1
as Renewable Energy Aware Task Allocation (REATA), can be The pseudocode of the heuristic is shown in Algorithm 1. At
decomposedinto|T|independentsubproblems.Eq.(5)defines the arrival of a new task k, it is estimated whether the current
the Oracle solution for each slot t ∈ T as an offline convex intervalicorrespondstothemostloadedintervallforthetime
optimization problem with full knowledge of the task set J, slot, based on the estimated maximal load Nˆ l. If not, artificial
including the arrivals and durations of all tasks. tasks A il are generated to emulate the expected future load,
ensuringthatthecomputationofthedualvariableλinEq.(8)
m {xxx a } x (cid:6) (1−τ j ·exp(−θ j ·F ·x tj )) (5a) r d e e fl te e r c m ts in th e e d m ac a c x o i r m di u n m gt l o oa th d e sc ru e l n e ar in io E . T q. h ( e 7) a : ll i o f c λ at > ion U x k (cid:5) k (X is k m t i h n e ) n ,
j∈ (cid:6) J the task is assigned its minimum allocation Xmin and added
k
s.t. P ·x tj ≤R t +S ti , i∈I t , (5b) to L i; otherwise, it receives a higher allocation x k > X k min
j∈Ji and is added to H i. The active set is updated accordingly as
x tj ≥X j min, j ∈J, (5c) J i =H i ∪L i.
x tj ∈R ≥0 , j ∈J (5d) 1Availableat:https://hal.science/hal-05326830
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore. Restrictions apply.

Algorithm 1: ONLINE-REATA: abstract task alloca- The data center receives video streams from live broadcast
tion channels and prepare them for the Content Distribution Net-
Data: J i−1, H i−1, L i−1, Nˆ l, S i−1, R work (CDN), which then delivers the transcoded streams to
k: arriving task at interval i (slot t). edge servers serving the end-users [15]. In accordance with
Result: Optimal allocation x k for task k guidelines [16], the broadcasting server originally encodes
1 for each arriving task k do video streams at 1080p and 8000 kbps. We will refer to
2 if |J i−1 |+1≥Nˆ l then this resolution-bitrate (1080p, 8000 kbps) pair as the original
3
Hˆ
i
←H
i−1
∪{k}; encoding profile. This profile may not be suitable for users
with low-resolution devices or slow connections; therefore,
4 else
5 Generate artificial tasks A il based on Nˆ l; videos are transcoded into 360p and 720p to ensure playback
6 Hˆ i ←H i−1 ∪{k}∪A il; o th n e t r h e e q s u e es d t e t v o ic li e v s e . -t I r n an t s h c i o s de ca a se ch s a tu n d n y e , l’s w v e id d e e o fi s n t e rea a m ta a s t k on a e s
7 Compute λ using (8) with (Hˆ i ,L i−1 ,R,S i−1 ); of these two resolutions. Since different transcoding profiles
8 if λ>U k (cid:5)(X k min) then (resolution-bitrate) require different CPU usage and energy
9
x
k
←X
k
min;
resources (higher bitrates require more resources), renewable
10
L
i
←L
i−1
∪{k};
availability must be considered when choosing a profile.
11 else (cid:4) (cid:5) CPU usage model. The computational effort for transcoding
12 x k ←− θ 1 F ln τ θ λ F ; operationsvarieswiththevideocontenttype(TableII)andthe
k k k
13
H
i
←H
i−1
∪{k}; selected target profile. We obtained these values by transcod-
14 J i ←H i ∪L i; ing, with ffmpeg [17], a video of fixed duration w for
each content type, converting from the original profile to both
target resolutions and sampled bitrates. For each operation,
we measured the transcoding time c and, then, estimated the
IV. CASESTUDY number of CPU cycles per second (i.e., frequency) required
to transcode w seconds as f = c·F , with F as the maximum
w
In this section we describe our case study, which corre- CPU frequency. Then, we fitted a linear relation between
spondstoagrid-connecteddatacenterequippedwithahybrid the sampled bitrates r and its corresponding frequency f,
energy system, including a microgrid with solar panels and obtaining coefficients m and n for each (content type, target
windturbines.Thedatacenterperformslivevideotranscoding resolution) pair, such that r(f)=mf +n.
operations, an example of compressible tasks. A Lithium- Energy consumption model. For each transcoding task with
Ion (LI) battery, well suited for cloud applications [3], is afrequencyf,thepowerconsumptionwasestimatedasx·P,
integrated into the system and charged exclusively when where P is the maximum power consumption of a core, and
excessrenewableenergyisavailable,untilitscapacityisfully x is the task core usage calculated as x= f .
F
reached. Consequently, power imports can be supplied either Utility model. The utility of a transcoding task is defined as
by the battery or by the main grid, with the battery being the Quality of Experience (QoE), which depends on video
prioritized for both import and export operations. A converter content, target resolution, and bitrate. Following [15], QoE is
regulates transfers between AC and DC components [2] (see modeled through the VQM metric as U(r)=1−aexp(−br),
Fig. 1). where r is the target bitrate. To relate this to the utility
function in (1), we express r as the function of the frequency
f derived above: considering τ = aexp(−bn), θ = bm, we
(cid:42)(cid:85)(cid:72)(cid:72)(cid:81)(cid:3)(cid:39)(cid:68)(cid:87)(cid:68)(cid:3)(cid:38)(cid:72)(cid:81)(cid:87)(cid:72)(cid:85) obtain U(r(f))=1−τexp(−θf). Table II reports the fitting
(cid:54)(cid:72)(cid:79)(cid:72)(cid:70)(cid:87) (cid:55)(cid:85)(cid:68)(cid:81)(cid:86)(cid:70)(cid:82)(cid:71)(cid:72)(cid:71)(cid:29) parameters θ and τ, and Fig. 2 shows the resulting curves.
(cid:69)(cid:72)(cid:86)(cid:87)(cid:3)(cid:69)(cid:76)(cid:87)(cid:85)(cid:68)(cid:87)(cid:72)
(cid:55)(cid:68)(cid:86)(cid:78)(cid:3)(cid:20)(cid:29)(cid:3)(cid:87)(cid:82)(cid:3)(cid:22)(cid:25)(cid:19)(cid:83) (cid:22)(cid:25)(cid:19)(cid:83) FurtherdetailsareprovidedinSectionIIofthesupplementary
(cid:69)(cid:76)(cid:87)(cid:85)(cid:68)(cid:87)(cid:72)
(cid:3)(cid:3)(cid:3)(cid:54)(cid:87)(cid:85)(cid:72)(cid:68)(cid:80) (cid:38)(cid:39)(cid:49) material.1
(cid:20)(cid:19)(cid:27)(cid:19)(cid:83)
(cid:55)(cid:68)(cid:86)(cid:78)(cid:3)(cid:21)(cid:29)(cid:3)(cid:87)(cid:82)(cid:3)(cid:26)(cid:21)(cid:19)(cid:83)
(cid:27)(cid:19)(cid:19)(cid:19)(cid:3)(cid:78)(cid:69)(cid:83)(cid:86) (cid:55)(cid:85)(cid:68)(cid:81)(cid:86)(cid:70)(cid:82)(cid:71)(cid:72)(cid:71)(cid:29) Real-time constraint. Upon the arrival of each task, Algo-
(cid:26)(cid:21)(cid:19)(cid:83)
rithm 1 simply applies Eq. (7), resulting in negligible latency.
(cid:69)(cid:76)(cid:87)(cid:85)(cid:68)(cid:87)(cid:72)
Frequency f ensures that transcoding is completed within the
(cid:50)(cid:81)(cid:16)(cid:86)(cid:76)(cid:87)(cid:72) (cid:48)(cid:68)(cid:76)(cid:81) playback time of each fragment, avoiding additional delay.
(cid:51)(cid:57)(cid:18)(cid:58)(cid:76)(cid:81)(cid:71) (cid:42)(cid:85)(cid:76)(cid:71)
(cid:40)(cid:54)(cid:54)
V. EVALUATION
Fig. 1: Case study description. The 1080p, 8000 kbps video A. Experimental Settings
stream must be transcoded to 720p and 360p. The stream
We evaluate Online-REATA over a three-day scenario
arrives at the data center, where the Online-REATA algorithm
(2021-06-15,2021-06-16,and2021-06-19),wherebothtraffic
is applied to find the optimal bitrate based on the renewable
intensity and renewable energy availability vary over time.
energy available. The transcoded video streams are then de-
All simulations were run on a 13th generation Intel Core i7-
livered to end users via CDN.
13850HX (2.2–5.3 GHz, 20 cores with 8 performance and 12
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore. Restrictions apply.

| TABLEII:Testvideosandtype,τ |            |             |     |     | andθparametersbycontent |     |     |                  |       |             |            |              |         |        |            |
| --------------------------- | ---------- | ----------- | --- | --- | ----------------------- | --- | --- | ---------------- | ----- | ----------- | ---------- | ------------ | ------- | ------ | ---------- |
|                             |            |             |     |     |                         |     |     | is theoretically |       | sufficient, | mismatches |              | between | demand | and        |
| type                        | and device | resolution. |     |     |                         |     |     |                  |       |             |            |              |         |        |            |
|                             |            |             |     |     |                         |     |     | supply occur     | since | the         | temporal   | distribution |         | does   | not follow |
|                             |            |             |     |     |                         |     |     | the workload’s   | trend | (see        | Fig.       | 3).          |         |        |            |
|                             |            |             |     |     | τ                       |     | θ   |                  |       |             |            |              |         |        |            |
ContentType Resolution Benchmarks. We compare Online-REATA against three ref-
Documentary 1.162×10−8 erence strategies: (1) Benchmark-0.99, which assigns each
|     |     |     | 360p | 4273873.86 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Aspen, task the number of cores needed to reach a target QoE of
|     | SnowMountain |     | 720p |     | 116.93 | 2.042×10−9 |     |               |     |       |           |        |      |            |     |
| --- | ------------ | --- | ---- | --- | ------ | ---------- | --- | ------------- | --- | ----- | --------- | ------ | ---- | ---------- | --- |
|     |              |     |      |     |        |            |     | 0.99 (maximum |     | QoE), | importing | energy | when | renewables | are |
5.776×10−9
Movie 360p 4951.70 insufficient. It provides the upper bound for QoE and import
OldTownCross 2.389×10−9 and a lower bound for export; (2) Benchmark-0.75, which
|     |       |     | 720p |     | 4234.21 |            |     |         |           |     |            |     |         |          |        |
| --- | ----- | --- | ---- | --- | ------- | ---------- | --- | ------- | --------- | --- | ---------- | --- | ------- | -------- | ------ |
|     |       |     |      |     |         |            |     | assigns | each task | the | allocation | to  | achieve | a target | QoE of |
|     | Sport |     | 360p |     | 560.79  | 3.400×10−9 |     |         |           |     |            |     |         |          |        |
0.75(minimumQoE),providingalowerboundforexportand
|     | TouchdownPass, |     |      |     |       | 1.046×10−9 |     |              |            |             |       |          |                 |         |          |
| --- | -------------- | --- | ---- | --- | ----- | ---------- | --- | ------------ | ---------- | ----------- | ----- | -------- | --------------- | ------- | -------- |
|     | RushFieldCuts  |     | 720p |     | 73.18 |            |     |              |            |             |       |          |                 |         |          |
|     |                |     |      |     |       |            |     | an upper     | bound      | for import; |       | and (3)  | Benchmark-0.89, |         | which    |
|     |                |     |      |     |       |            |     | satisfies    | every task | with        | a QoE | of 0.89, | the             | average | QoE that |
|     |                |     |      |     |       |            |     | Online-REATA | achieves.  |             |       |          |                 |         |          |
1.0
|     |     |     |     |     |     |     |     | Data center    | and          | energy  | system.  |      | Battery  | charging    | and dis- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------ | ------- | -------- | ---- | -------- | ----------- | -------- |
|     |     |     |     |     |     |     |     | charging       | efficiencies | are     | set      | to η | = η      | = 0.9,      | assuming |
|     |     |     |     |     |     |     |     |                |              |         |          | ch   | disch    |             |          |
| 0.8 |     |     |     |     |     |     |     |                |              |         |          | =    | 0.8      |             |          |
|     |     |     |     |     |     |     |     | a Depth        | of Discharge |         | (DoD)    |      | [3].     | DoD defines | the      |
|     |     |     |     |     |     |     |     | usable portion | of           | battery | capacity |      | [11] and | it is set   | to avoid |
0.6 premature degradation. The battery prioritizes renewable en-
| EoQ |     |     |     |     |     | documentary, 360p  |     |                                                       |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | documentary, 720p  |     | ergyexchangeoveranyinteractionwiththegrid.Forthetests |     |     |     |     |     |     |     |
0.4 movie, 360p  involving a battery, the system is initialized with the battery
movie, 720p
|     |     |     |     |     |     |     |     | initially | discharged, | and | charging |     | and discharging |     | processes |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | -------- | --- | --------------- | --- | --------- |
sport, 360p
|     |     |     |     |     |     | sport, 720p  |     | of the battery | are | simulated. |     | Converter | efficiency | is  | 1, battery |
| --- | --- | --- | --- | --- | --- | ------------ | --- | -------------- | --- | ---------- | --- | --------- | ---------- | --- | ---------- |
0.2
|     |     |     |     |     |     | QoE=0.75 |     | degradation | and | idle power |     | are neglected |     | (the latter | would |
| --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | ---------- | --- | ------------- | --- | ----------- | ----- |
QoE=0.99
|     |     |     |     |     |     |     |     | add constant | offset | to  | dynamic | consumption |     | and it | has been |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --- | ------- | ----------- | --- | ------ | -------- |
0.0
0.00 0.25 0.50 0.75 1.00 1.25 1.50 1.75 reduced by recent hardware efficiency improvements [1]). All
Number of Used Cores
|      |            |        |     |         |        |          |      | coresareassumedhomogeneous,withfrequencyF |     |     |     |     |     |     | andpower |
| ---- | ---------- | ------ | --- | ------- | ------ | -------- | ---- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | -------- |
| Fig. | 2: Fitting | curves | of  | QoE vs. | number | of cores | x (x | =                                         | P.  |     |     |     |     |     |          |
consumption
f
| F ).                                                      | Assuming | a maximum |     | per-core | frequency | of  | 5.1 GHz, |             |         |              |     |           |           |            |         |
| --------------------------------------------------------- | -------- | --------- | --- | -------- | --------- | --- | -------- | ----------- | ------- | ------------ | --- | --------- | --------- | ---------- | ------- |
| additionalcoresareallocatedwhenasinglecoreisinsufficient. |          |           |     |          |           |     |          | B. Results  |         |              |     |           |           |            |         |
|                                                           |          |           |     |          |           |     |          | We evaluate |         | Online-REATA |     | against   | different | benchmarks |         |
|                                                           |          |           |     |          |           |     |          | by varying  | battery | size         | and | analyzing | its       | impact     | on grid |
efficiencycores),with32GBRAM,underUbuntu22.04LTS.
|     |     |     |     |     |     |     |     | interactions, | QoE, | and | the effective |     | use of | storage. | First, we |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --- | ------------- | --- | ------ | -------- | --------- |
Traffic Intensity. We rely on the Twitch traffic dataset ran the tests without batteries. Fig. 4 reports, for each time
| published |     | in [18], | [19]. | From this | worldwide |     | dataset, we |         |          |       |     |           |     |               |      |
| --------- | --- | -------- | ----- | --------- | --------- | --- | ----------- | ------- | -------- | ----- | --- | --------- | --- | ------------- | ---- |
|           |     |          |       |           |           |     |             | slot of | June 17, | 2021, | the | reduction | in  | total imports | plus |
extract French-language live streams to align user demand exports(i.e.,interactionswiththemaingrid)togetherwiththe
with renewable energy sources from the French grid in terms averageQoEachieved.Overthethree-daysimulation,Online-
| of timezone. |     | Timestamps |     | are adapted | to UTC+2. |     | To capture |       |         |         |       |         |     |        |             |
| ------------ | --- | ---------- | --- | ----------- | --------- | --- | ---------- | ----- | ------- | ------- | ----- | ------- | --- | ------ | ----------- |
|              |     |            |     |             |           |     |            | REATA | reduces | average | daily | imports | by  | 52.76% | relative to |
content diversity, we identify the most popular Twitch cat- Benchmark-0.99 and cuts exports by 21.62% compared to
egories [20] (e.g., Just Chatting, Minecraft) and map them Benchmark-0.75, while ensuring an average QoE of 0.89.
to three representative video classes: documentary (25.4%), Secondly, experiments are conducted by introducing batter-
movie (45.8%), and sports (28.8%), based on visual and ies and varying their capacity in 500 Wh increments, ranging
| dynamic | similarity. |     | Traffic | intensity | is defined | as  | an estimate |           |         |     |         |     |                  |     |              |
| ------- | ----------- | --- | ------- | --------- | ---------- | --- | ----------- | --------- | ------- | --- | ------- | --- | ---------------- | --- | ------------ |
|         |             |     |         |           |            |     |             | from 0 Wh | to 5500 | Wh. | Figures | 5   | and 6 illustrate |     | the results, |
(Nˆ
of maximum number of concurrent tasks per slot l). In this where the performance of each algorithm is evaluated using
work, we assume that this estimate is highly accurate (we use the SSR and SCR metrics, as defined in [7]. SCR and SSR
actual values), since many reliable techniques are available computation for the considered case study is discussed in
to forecast seasonal streaming patterns, such as SARIMA, Section III of the supplementary material.1 We observed that
| Fourier | analysis | and | recurrent | neural | networks | (RNNs). |     |            |         |      |        |         |       |                    |     |
| ------- | -------- | --- | --------- | ------ | -------- | ------- | --- | ---------- | ------- | ---- | ------ | ------- | ----- | ------------------ | --- |
|         |          |     |           |        |          |         |     | increasing | battery | size | past a | certain | point | yields diminishing |     |
Renewable Availability. For the same three days, we ob- returnsforSCRandSSR.Thisoccursbecauselargerbatteries
tained hourly wind and solar production data from the French takelongertoreachtheminimumDoD,delayingthedischarge
grid[21].Thesevalueswereinterpolatedtocapturefinerfluc- phase. This reduced utilization of stored renewable energy
tuations(15-minutetimeslots).Toalignrenewablesupplywith leads to lower effective SCR and SSR values, since all the
the Twitch workload, we compute the daily renewable budget dischargedenergyfromthebatterycountsasrenewablesupply.
E 24h,i.e.,theenergyrequiredtoservealltasksatatargetQoE Figures 5 and 6 confirm that, among all benchmarks, Online-
of0.99.Thisbudgetisdistributedacrossslotsproportionallyto REATA achieves the best trade-off between SCR and SSR,
thegrid’srenewableprofile:evenifthedailyrenewablebudget without requiring large battery storage, while maintaining an
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore.  Restrictions apply.

00:00 03:10 00:30 03:40 00:60 03:70 00:90 03:01 00:21 03:31 00:51 03:61 00:81 03:91 00:12 03:22
620
376
187
Daily time
)hW(
ytilibaliava
elbaweneR
Renewable share High Criticality
Traffic intensity Low Criticality
146
60
20
sksat
tnerrucnoC
Fig. 3: Traffic and energy patterns at Day 3, 2021-06-17:
Load trend (blue line) and energy profile (black line) during
the simulated days. The heatmap indicates the criticality of
each slot: the criticality is higher when the mismatch between
resources and demand is accentuated.
00:00 03:10 00:30 03:40 00:60 03:70 00:90 03:01 00:21 03:31 00:51 03:61 00:81 03:91 00:12 03:22
200
175
150
125
100
75
50
25
0
Daily time
)hW(
ygrenE
1.0
0.8
0.6
0.4
0.2
0.0
EoQ
1.0
0.9
0.8
0.7
0.6
0.5
0 1000 2000 3000 4000 5000
Battery Capacity (Wh)
Import + Export - Online-REATA Exported energy reduction
Import + Export - Benchmark 0.99 QoE - Online-REATA
Import + Export - Benchmark 0.75 QoE - Benchmark 0.75
Imported energy reduction QoE - Benchmark 0.99
Fig.4:ThesumoftheenergyimportedandexportedatDay3,
2021-06-17,byBenchmark-0.99,Benchmark-0.75andOnline-
REATAandtheaverageQoEforeachtimeslotarerepresented.
average QoE that is only about 10% below the maximum
value. We also observe that Online-REATA, for an equivalent
averageQoE(0.89),isabletomatchthebestSSRperformance
of Benchmark-0.89 (≈ 0.97), while improving SCR by about
3.4% and doing so with a 35.3% smaller battery capacity
(from 5035 Wh to 3257 Wh). Additionally, for an equal
battery size (500 Wh), Online-REATA is able to deliver an
SCR improvement of +11.24% while maintaining an SSR
improvement of +7.57%. We underline that the high self-
consumptionobservedinBenchmark-0.99ismainlyduetothe
factthattherenewableavailabilitywasdimensionedaccording
to the energy required to achieve the maximum QoE of
0.99. Despite this, in the absence of a battery, Online-REATA
is able to almost match Benchmark-0.99 in terms of SCR
(only –0.62% difference), while significantly outperforming
it in SSR, with an improvement of +23.18%. Moreover, for
almost all battery sizes, Online-REATA maintains a higher
SSR level compared to Benchmark-0.75 (up to a battery size
)etaR
ycneiciffuS-fleS(
RSS Benchmark 0.99
Benchmark 0.89
Benchmark 0.75
Online-REATA - 35.3%
Fig. 5: SSR metric for each algorithm and battery capacity: it
indicates the share of total load supplied by renewables.
1.0
0.9
0.8
0.7
0.6
0.5
0 1000 2000 3000 4000 5000
Battery Capacity (Wh)
)etaR
noitpmusnoC-fleS(
RCS
Benchmark 0.99
Benchmark 0.89
Benchmark 0.75
Online-REATA
+ 3.4%
- 35.3%
Fig. 6: SCR metric for each algorithm and battery capacity:
it measures the share of renewable energy used over that
available.
of ≈ 4000 Wh), and substantially increases SCR, achieving
up to a +17.78% improvement with a 500 Wh battery while
maintaining a higher average QoE.
VI. CONCLUSION
This work proposes an approach based on compressible
tasks to reduce green data centers’ reliance on the main
grid while preserving QoE. The approach jointly addresses
imports reduction, final QoE, grid stability, and suitability
for delay-sensitive workloads. We also aimed to reduce the
reliance on storage systems. These aspects, to the best of our
knowledge, have not been addressed together in prior work.
We developed the Online-REATA heuristic, and we evaluated
it in the case study of live video transcoding: Online-REATA
achieved up to ≈ 11% higher SCR and ≈ 8% higher SSR
than constant allocation (Benchmark-0.89), while maintaining
the same average QoE without additional dependence on
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore. Restrictions apply.

| energy | storage. | The | gains came | from | adjusting |     | the bitrate, |     |     |     |     |     |     |     |     |
| ------ | -------- | --- | ---------- | ---- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
TaskswithLimitedEnergyBudget,”inICPP,2024.[Online].Available:
https://hal.science/hal-04676376
| reducing   | the import | from   | the | main      | grid but | also | absorbing |         |            |               |          |            |                    |               |     |
| ---------- | ---------- | ------ | --- | --------- | -------- | ---- | --------- | ------- | ---------- | ------------- | -------- | ---------- | ------------------ | ------------- | --- |
|            |            |        |     |           |          |      |           | [10] W. | E. Gnibga, | A. Blavette,  | and      | A.-C.      | Orgerie, “Latency, | energy        | and |
| the energy | surplus.   | Future |     | work will | extend   | the  | proposed  |         |            |               |          |            |                    |               |     |
|            |            |        |     |           |          |      |           | carbon  | aware      | collaborative | resource | allocation | with               | consolidation | and |
approachtoothercompressibletasks(e.g.,MLinference)and
|     |     |     |     |     |     |     |     | qos | degradation | strategies | in  | edge computing,” | in  | 2023 IEEE | 29th |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ---------------- | --- | --------- | ---- |
todistributedenvironments,includingspace-shiftingofdelay- InternationalConferenceonParallelandDistributedSystems(ICPADS),
2023.
| tolerant | compressible |     | tasks across | data | centers. |     |     |               |     |         |             |           |           |     |          |
| -------- | ------------ | --- | ------------ | ---- | -------- | --- | --- | ------------- | --- | ------- | ----------- | --------- | --------- | --- | -------- |
|          |              |     |              |      |          |     |     | [11] B. Acun, | B.  | Lee, F. | Kazhamiaka, | K. Maeng, | U. Gupta, | M.  | Chakkar- |
avarthy,D.Brooks,andC.-J.Wu,“Carbonexplorer:Aholisticframe-
REFERENCES
|        |          |           |             |     |          |         |           | work | for designing     |     | carbon aware | datacenters,” | in Proceedings |         | of the   |
| ------ | -------- | --------- | ----------- | --- | -------- | ------- | --------- | ---- | ----------------- | --- | ------------ | ------------- | -------------- | ------- | -------- |
|        |          |           |             |     |          |         |           | 28th | ACM International |     | Conference   | on            | Architectural  | Support | for Pro- |
| [1] A. | Shehabi, | S. Smith, | A. Hubbard, | A.  | Newkirk, | N. Lei, | M. Siddik |      |                   |     |              |               |                |         |          |
grammingLanguagesandOperatingSystems,Volume2,2023.
| et al.,  | “2024    | united states | data | center energy | usage              | report,” | Lawrence |            |         |              |     |                |                 |     |        |
| -------- | -------- | ------------- | ---- | ------------- | ------------------ | -------- | -------- | ---------- | ------- | ------------ | --- | -------------- | --------------- | --- | ------ |
|          |          |               |      |               |                    |          |          | [12] W. E. | Gnibga, | A. Blavette, | and | A.-C. Orgerie, | “Energy-related |     | impact |
| Berkeley | National | Laboratory,   |      | Tech.         | Rep. LBNL-2001637, |          | 2024.    |            |         |              |     |                |                 |     |        |
ofredefiningself-consumptionfordistributededgedatacenters,”in2024
[Online].Available:https://escholarship.org/uc/item/32d6m0d1
[2] C.Sahin,C.Andic,E.Aydin,andB.Turkay,“Integrationofsustainable IEEE15thInternationalGreenandSustainableComputingConference
(IGSC),2024.
| energy | sources | into | data centre | electrical | systems,” | in  | 2024 Global |                  |     |        |          |         |            |                   |     |
| ------ | ------- | ---- | ----------- | ---------- | --------- | --- | ----------- | ---------------- | --- | ------ | -------- | ------- | ---------- | ----------------- | --- |
|        |         |      |             |            |           |     |             | [13] S. Sachdeva |     | and N. | Vishnoi, | “Faster | algorithms | via approximation |     |
EnergyConference(GEC),122024,pp.264–269.
|        |            |              |     |                |     |            |        | theory,” | Foundations |     | and Trends | in Theoretical | Computer |     | Science, |
| ------ | ---------- | ------------ | --- | -------------- | --- | ---------- | ------ | -------- | ----------- | --- | ---------- | -------------- | -------- | --- | -------- |
| [3] W. | E. Gnibga, | A. Blavette, | and | A.-C. Orgerie, |     | “Renewable | energy | in       |             |     |            |                |          |     |          |
vol.9,2013.
datacenters:Thedilemmaofelectricalgriddependencyandautonomy
costs,”IEEETransactionsonSustainableComputing,2024. [14] S. Boyd and L. Vandenberghe, Convex Optimization. Cambridge
UniversityPress,2004.
| [4] F. Ahmed, |                 | D. Al Kez, | S. McLoone,    | R.  | J. Best,   | C. Cameron, | and     |               |     |                 |     |           |           |        |           |
| ------------- | --------------- | ---------- | -------------- | --- | ---------- | ----------- | ------- | ------------- | --- | --------------- | --- | --------- | --------- | ------ | --------- |
|               |                 |            |                |     |            |             |         | [15] L. Toni, | R.  | Aparicio-Pardo, |     | G. Simon, | A. Blanc, | and P. | Frossard, |
| A.            | Foley, “Dynamic |            | grid stability | in  | low carbon | power       | systems |               |     |                 |     |           |           |        |           |
“Optimalsetofvideorepresentationsinadaptivestreaming,”inMMSys,
| with | minimum | inertia,” | Renewable | Energy, | 2023. | [Online]. | Available: |     |     |     |     |     |     |     |     |
| ---- | ------- | --------- | --------- | ------- | ----- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
2014.
https://www.sciencedirect.com/science/article/pii/S0960148123003774
[5] M.Liu,Y.Li,N.Li,K.Li,Z.Hong,andW.Yang,“Adaptivefrequency [16] AT&T Business, “What internet speed, bitrate is best
|     |     |     |     |     |     |     |     | for | streaming |     | Twitch?” | accessed: | 2025-04-10. |     | [Online]. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --------- | ----------- | --- | --------- |
controlstrategyforthecoordinationofflexibleloadsandgrid-forming
|      |            |         |      |                   |     |            |          | Available: |     | https://www.business.att.com/resources/knowledge-center/ |     |     |     |     |     |
| ---- | ---------- | ------- | ---- | ----------------- | --- | ---------- | -------- | ---------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
| wind | turbines,” | in 2025 | IEEE | 3rd International |     | Conference | on Power |            |     |                                                          |     |     |     |     |     |
what-internet-speed-is-best-for-esport-streaming.html
ScienceandTechnology(ICPST),2025.
[6] P. Ren, W. Sun, Y. Wang, and G. Harrison, “Grid frequency stability [17] F.Developers,“Ffmpegdocumentation,”https://ffmpeg.org/ffmpeg.html,
supportpotentialofdatacenter:Aquantitativeassessmentofflexibility,” 2023,accessed:2025-04-30.
|     |     |     |     |     |     |     |     | [18] H. Le, | J. Wu, | L. Yu, | and M. | Lynn, “A | study on channel | popularity | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | ------ | -------- | ---------------- | ---------- | --- |
2025.[Online].Available:https://arxiv.org/abs/2510.01050
Twitch,”arXivpreprintarXiv:2111.05939,2021.
| [7] D.           | Kim, Y. | Jang, and | Y. Choi,         | “Improved | metrics           | for | evaluating |             |         |            |                                   |     |     |     |           |
| ---------------- | ------- | --------- | ---------------- | --------- | ----------------- | --- | ---------- | ----------- | ------- | ---------- | --------------------------------- | --- | --- | --- | --------- |
|                  |         |           |                  |           |                   |     |            | [19] H. Le, | “Twitch | crawling,” | https://github.com/hvrlxy/twitch\ |     |     |     | crawling/ |
| self-consumption |         | and       | self-sufficiency | rates     | in ess-integrated |     | renewable  |             |         |            |                                   |     |     |     |           |
energysystems,”RenewableEnergy,vol.247,p.123059,2025. tree/main,gitHubrepository,accessed:2025-05-19.
|            |             |         |             |                    |     |                    |     | [20] SullyGnome, |            | “2021 | june streamed                                   | games,” | accessed: | 2025-04-10. |     |
| ---------- | ----------- | ------- | ----------- | ------------------ | --- | ------------------ | --- | ---------------- | ---------- | ----- | ----------------------------------------------- | ------- | --------- | ----------- | --- |
| [8] T. da  | Silva       | Barros, | F. Giroire, | R. Aparicio-Pardo, |     | S. Perennes,       | and |                  |            |       |                                                 |         |           |             |     |
|            |             |         |             |                    |     |                    |     | [Online].        | Available: |       | https://sullygnome.com/games/2021june/streamed? |         |           |             |     |
| E. Natale, | “Scheduling |         | with        | fully compressible |     | tasks: Application |     | to               |            |       |                                                 |         |           |             |     |
language=fr
deeplearninginferencewithneuralnetworkcompression,”inCCGRID,
|     |     |     |     |     |     |     |     | [21] H.Upton,“Windandsolarelectricityproduction,”2023,accessed:2023- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
2024. 08-02.[Online].Available:https://www.kaggle.com/datasets/henriupton/
| [9] T. da | Silva | Barros, | D. Ferre, | F. Giroire, | R.  | Aparicio-Pardo, | and |     |     |     |     |     |     |     |     |
| --------- | ----- | ------- | --------- | ----------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wind-solar-electricity-production
| S. Perennes, |     | “Scheduling | Machine | Learning | Compressible |     | Inference |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | ------- | -------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:56:13 UTC from IEEE Xplore.  Restrictions apply.