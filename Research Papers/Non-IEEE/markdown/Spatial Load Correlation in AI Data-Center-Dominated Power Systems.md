|     |                       |     | Spatial |     | Load |     | Correlation |     |       |     | in      | AI  |     |     |     |
| --- | --------------------- | --- | ------- | --- | ---- | --- | ----------- | --- | ----- | --- | ------- | --- | --- | --- | --- |
|     | Data-Center-Dominated |     |         |     |      |     |             |     | Power |     | Systems |     |     |     |     |
Chandan Chaudhary, Student Member, IEEE, Alaaeldein Abdelkader, Student Member, IEEE,
Yansong Pei, Member, IEEE, Mohammed Benidris, Senior Member, IEEE, and Joydeep Mitra, Fellow, IEEE
Electrical and Computer Engineering, Michigan State University, East Lansing, MI 48824, USA
Emails: chaud152@msu.edu, abdelk15@msu.edu, peiyanso@msu.edu, benidris@msu.edu, and mitraj@msu.edu
Abstract—The proliferation of large-scale data centers intro- tromechanicalloads.Fieldmeasurementsreveallow-frequency
| duces spatially | correlated |      | demand         | profiles     | that | challenge | the      |            |              |         |           |                |              |        |          |
| --------------- | ---------- | ---- | -------------- | ------------ | ---- | --------- | -------- | ---------- | ------------ | ------- | --------- | -------------- | ------------ | ------ | -------- |
|                 |            |      |                |              |      |           |          | resonances |              | near 11 | Hz and    | high-frequency | oscillations |        | in the   |
| long-standing   | assumption |      | of statistical | independence |      | of        | loads in |            |              |         |           |                |              |        |          |
|                 |            |      |                |              |      |           |          | 5–10       | kHz          | range   | at rack,  | triggered      | by control   | delays | and      |
| power system    | analysis.  | This | paper          | examines     | the  | emergence | of       |            |              |         |           |                |              |        |          |
|                 |            |      |                |              |      |           |          | DC         | bus dynamics |         | [8], [9]. | Real-world     | events,      | such   | as 14.7– |
suchloadcorrelationsandevaluatestheirimpactondata-center-
6202 nuJ 11  ]YS.ssee[  1v35831.6062:viXra
dominated grids. Analytical derivations reveal that correlated 14.8HzoscillationsinDominionEnergy,showthatunplanned
load fluctuations amplify aggregate stochastic disturbances, re- excitations from data center operations destabilize hidden
duce voltage stability margins through weakened reactive power dynamic modes in weak grids [10].
| stiffness, | and degrade | frequency |     | stability | margin | by  | erosion |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --------- | --- | --------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
AIandHPCloadprofilesdemonstratethattheseloadsgen-
| of natural      | load diversity |          | effects. | Real-time   | digital | simulation     |     |       |                |     |       |        |         |        |          |
| --------------- | -------------- | -------- | -------- | ----------- | ------- | -------------- | --- | ----- | -------------- | --- | ----- | ------ | ------- | ------ | -------- |
|                 |                |          |          |             |         |                |     | erate | megawatt-scale |     | ramps | within | seconds | during | synchro- |
| studies confirm | that           | moderate | spatial  | correlation |         | in distributed |     |       |                |     |       |        |         |        |          |
data centers produces simultaneous frequency deviations and nizedcompute-communicationcycles,withfluctuationspectra
voltage fluctuations across multiple buses. The findings offer capable of exciting inter-area electromechanical modes when
transmission system operators a physics-based perspective to aligned with weakly damped grid resonances [3], [6], [11].
| interpret    | emerging | oscillatory | phenomena |            | and | establish        | stabil- |          |      |         |           |       |        |               |     |
| ------------ | -------- | ----------- | --------- | ---------- | --- | ---------------- | ------- | -------- | ---- | ------- | --------- | ----- | ------ | ------------- | --- |
|              |          |             |           |            |     |                  |         | Multiple | data | centers | operating | under | shared | orchestration |     |
| ity planning | criteria | grounded    | in        | measurable |     | load-correlation |         |          |      |         |           |       |        |               |     |
platforms,thermalconstraints,orworkloadschedulingexhibit
| structures | rather than | traditional |     | diversity | assumptions. |     |     |     |     |     |     |     |     |     |     |
| ---------- | ----------- | ----------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IndexTerms—AIdatacenter,correlatedload,inter-areaoscil- correlated power variations across distinct network buses.
lations, load correlation, power system dynamics, RTDS These loads induce voltage-sensitive reductions, trigger fre-
|     |     |                 |     |     |     |     |     | quency | excursions, |           | and exacerbate |     | stability risks | in converter- |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | ------ | ----------- | --------- | -------------- | --- | --------------- | ------------- | --- |
|     |     | I. INTRODUCTION |     |     |     |     |     |        |             |           |                |     |                 |               |     |
|     |     |                 |     |     |     |     |     | rich   | grids       | [2], [6]. |                |     |                 |               |     |
TherapidexpansionofAIandhigh-performancecomputing Although existing studies provide insight into single-site
(HPC) has fundamentally reshaped electricity demand across data-center dynamics, analytical tools that capture correla-
major interconnections. Data centers have emerged as one of tion across geographically dispersed facilities and translate
the most consequential load classes directly interfacing with thoseeffectstosystem-levelbehaviorremainscarce.Planning
bulk power system. Recent projections reveal that global data criteria assume load independence and overlook impacts of
centers could demand up to 945 TWh annually by 2030, correlated load variations in stability thresholds or reserve
with AI-driven workloads accounting for up to 12% of U.S. requirements. This paper addresses these gaps in three ways:
electricity consumption by 2028 [1], [2]. Modern hyperscale (1) defining spatial load correlation mathematically and iden-
facilities operate at extreme power densities, often exceeding tifying the physical mechanisms that create it; (2) deriving
100 MW per site [2], [3], and some campuses are now analytical relationships that link load correlation to voltage
planned at the gigawatt scale. Such facilities exhibit sharp stability, frequency response, and oscillation amplification;
power fluctuations arising from synchronized compute and and(3)validatingthetheoreticalframeworkthroughreal-time
communication phases in large-scale training jobs [3], [4]. digital simulations that show even moderate correlation can
A defining characteristic of this evolution is geographic produce simultaneous disturbances across multiple buses.
|                |          |            |     |       |        |        |     | The | remainder |     | of this paper | is organized |     | as follows. | Sec- |
| -------------- | -------- | ---------- | --- | ----- | ------ | ------ | --- | --- | --------- | --- | ------------- | ------------ | --- | ----------- | ---- |
| concentration. | Northern | Virginia’s |     | “Data | Center | Alley” | now |     |           |     |               |              |     |             |      |
exceeds2.5GWofactivedemand,andtheadditionofnewAI- tion II introduces the concept of correlated load. The physical
data-center campuses produces highly localized, synchronized mechanismsgivingrisetoloadcorrelationaredetailedinSec-
load patterns that intensify transmission stress [2], [3]. This tionIII.SectionIVquantifiestheimpactsofcorrelatedloadon
clustering forms demand hubs that impose intense stress on voltage stability, frequency dynamics, inter-area oscillations,
|          |              |                |     |     |            |     |      | and | reserve | planning | requirements. |     | Section | V presents | real- |
| -------- | ------------ | -------------- | --- | --- | ---------- | --- | ---- | --- | ------- | -------- | ------------- | --- | ------- | ---------- | ----- |
| regional | transmission | infrastructure |     | and | invalidate | the | load |     |         |          |               |     |         |            |       |
diversityassumptionsofpowersystemplanningandoperation. time digital simulation studies on the IEEE 39-bus system.
Data centers interface with the grid primarily through Finally,SectionVIconcludesthepaperandprovidesdirection
voltage-source converters, which include double-conversion for future research in this sector.
UPS systems, rack-level rectifiers, and high-density server II. CORRELATEDLOAD
power supplies [5]–[7]. This converter-dominated architec- Powersystemanalysishasreliedonthepremisethatelectri-
ture creates loads with ultra-low inertia, weak damping, and calloadsatdifferentnetworklocationsfluctuateindependently.
negative impedance across multiple frequency bands, which This consideration, valid for dispersed and uncoordinated
decouple demand from inertial buffering and differ from elec- residential or industrial demand, offers analytical simplicity

TransmissionLevel
and justifies the use of diversity factors in planning and 230kV 230kV
Bus1 Bus2 Bus3
stability studies. Each bus-level demand is modeled as an
uncorrelated stochastic process {P (t)}N , which ensures 1 C12 C13 0
aggregate variance grows linearly w
i
ith th
i=
e
1
number of loads. Subtransmission
C=

C
C
1
1
2
3 C
1
23
C
1
23 0
0


Level 0 0 0 1
This naturally mitigates system-wide fluctuations. 69–138kV 69–138kV
Sub.1 Sub.2 Sub.3 Sub.4
This independence simplifies forecasting, modal analysis,
and infrastructure planning as each load acts as an isolated
P1 P2 P4 P3 InternalSync
stochastic source. This allows linearized small-signal models
andprobabilisticmethodstotreatbusesseparately.Mathemat- Dat 1 a 50 C M en W ter1 Dat 1 a 80 C M en W ter2 Independent Dat 1 a 20 C M en W ter3 R R 1 2 HVAC
ically, independence requires that for i̸=j, AITraining AITraining Load50MW AIInference · R · n · R=Rack
Nospatialcorrelation
E[P i (t)P j (t′)]=E[P i (t)]E[P j (t′)],Corr(P i (t),P j (t′))=0 Sync’dWorkload,Weather Correlated
(1)
↓P1(t)=P¯+
↓
A
P
c
2
o
(
s
t
(
)
ω
=
ct
P
)
¯+Acos(ωct+ϕ12)
↓P3(t)=P¯+Acos(ωct+ϕ13)
a condition increasingly violated by the rise of synchronized Fig. 1. Representation of multi-site correlated data-center loads with rack-
and digitally managed facilities. levelandHVACsynchronization.
III. PHYSICALMECHANISMSOFLOADCORRELATION
A. Spatially Correlated Load Behavior
Correlatedloadinmodernpowersystemsstemsfromphys-
Moderngridsarecomprisedofconverter-dominatedentities
ical, operational, and environmental couplings among large
such as data centers, EV fleets, and smart campuses, that
digitallymanagedfacilities.Thissectionexaminesthephysical
operate under centralized control or shared environmental
mechanisms that induce such correlations across grid buses.
stimuli. Their coordinated behavior induces temporal correla-
In data-center-dominated networks, these mechanisms fall
tion among power injections at geographically distinct buses,
into three categories: operational synchronization, converter-
which gives rise to spatially correlated load. From a system
mediated electrical coupling, and environmental forcing.
perspective, such correlation emerges only when fluctuations
A. Cross-Facility Workload Orchestration
at multiple nodes evolve coherently in time.
Hyperscale cloud and AI operators routinely distribute
A single, time-varying load at one bus, regardless of the
computationalworkloadsacrossmultiplesitesforredundancy,
internal synchronization among its subsystems, does not con-
throughput, and latency optimization. Centralized orchestra-
stitute spatial correlation because the grid perceives only one
tion frameworks (e.g., DeepSpeed, Kubernetes, or internal
aggregated injection. A facility may be composed of multiple
schedulers) synchronize training phases, checkpoint updates,
subsystems that operate in synchrony. If the facility connects
and communication cycles across data centers connected to
to the transmission network through a single node i, the grid
different transmission nodes [12]–[14].
observes only the total power injection as a single stochastic
When compute clusters at buses i and j initiate or pause
process. Internal synchronization among subsystems, such as
tasksnearlysimultaneously,theiractivepowerdemandfollows
GPU racks or HVAC controls, remains electrically invisible,
aphase-alignedtemporalpattern,thatcanbeapproximatedby:
thus yields Corr(P (t),P (t′))=0 for all j ̸=i.
i j
Spatial correlation instead occurs when loads at distinct P (t)=P +A cos(ω t+ϕ ), (4)
i i,0 i c i
buses i and j (with Z ij ̸= 0, Z is the network impedance P j (t)=P j,0 +A j cos(ω c t+ϕ j ), (5)
matrix) fluctuate coherently. The correlation strength is cap-
whereω isthecharacteristicfrequencyoftheworkloadcycle.
tured by the cross-correlation function, c
When |ϕ −ϕ |≪1, the cross correlation
i j
ρ ij (τ)= E[(P i (t)−P¯ i ) σ (P σ j (t+τ)−P¯ j )] , (2) E[∆P i (t)∆P j (t)]= A i 2 A j cos(ϕ i −ϕ j )≈ A i 2 A j (6)
i j
is positive, which implies spatial correlation. This effect is
andasignificantcorrelationexistswhen|ρ (τ)|>ϵforsome
ij particularly plausible in regions such as Northern Virginia,
τ ∈[−τ ,τ ]. The resulting correlation matrix
max max where a dense concentration of hyperscale data centers shares
C ij = max |ρ ij (τ)| (3) common transmission corridors with large commercial and
τ∈[−τmax,τmax]
residential loads. In such clusters, synchronized AI training
is symmetric with C = 1 and C ∈ [0,1]. Strong off- schedules can create temporally correlated power fluctuations
ii ij
diagonal terms indicate synchronized fluctuations among dis- observable across multiple substations.
tinct buses, a phenomenon increasingly observed in data- B. Grid-Mediated Electromagnetic Coupling
center-dominated grids. As illustrated in Fig. 1, synchronized
Modern AI data centers are converter-dominated loads that
facilities connected to distinct buses can generate strong off-
interfacewiththegridthroughhigh-capacityAC/DCrectifiers,
diagonal correlation terms C , even when neighboring loads
ij UPS systems, and DC–DC converters [7]. These converters
remain independent. This spatial structure, characterized by
exhibit fast voltage–current dynamics, low effective inertia,
selective non-zero off-diagonal elements in C, fundamentally
and nonlinear impedance characteristics [5]. As a result,
differentiatescorrelatedloadphenomenafromsingle-sitetem-
local power disturbances can travel through the network as
poral variability and necessitates analytical frameworks that
electromagnetic effects that couple nearby substations [15].
extend beyond conventional power flow formulations.

Under small-signal conditions, the relation between nodal A. Voltage Stability Margin Degradation
voltage and power perturbations can be approximated by
Voltage variability near an operating point is governed by
∆P
∆V=Z∆I, ∆I k ≈ V∗ k. (7) the linearized power–flow sensitivities:
k
Thevoltagedeviationatbusjduetoactive-powervariations (cid:20)∆P(cid:21) (cid:20)J J (cid:21)(cid:20)∆θ(cid:21)
across all buses is ∆V = (cid:88) N Z ∆P k. (8) ∆Q = J Q PP P J Q PV V ∆V , ∆V ≈−J Q − V 1 ∆Q, (12)
j jk V∗
k=1 k sothesmallestsingularvalueσ (J )quantifiestheweak-
When a local power perturbation ∆P occurs at bus i, min QV
i
est voltage–restoring stiffness. The coupling between active-
converters at adjacent buses respond through grid-mediated
and reactive-power variations can be expressed through a
coupling. The induced active-power response at bus j is
local small-signal transfer function H (jω) that captures
E′V cosθ ∆P QP,i
∆Presp =− · i, (9) converter admittance and network voltage sensitivity after the
j X S b elimination of voltage perturbations [8], [9]. At each bus i,
where E′ and V are the internal and terminal voltages, θ is
the power angle, X is the line reactance, and S b is the system ∆Q i (jω)=H QP,i (jω)∆P i (jω). (13)
base power [15]. The disturbance travels through the network Expanding H around the steady-state set point at (ω=0):
QP,i
as an electromechanical wave with approximate speed
(cid:114) E′V cosθω H QP,i (jω)=H QP,i (0)+jωH Q ′ P,i (0)+O(ω2). (14)
c≈ s, (10)
2HS X Neglecting higher-order terms and defining
b
where H is the system inertia. This links the fast voltage and
α =H (0), β =H′ (0), (15)
currentdynamicsofspatiallyseparatedconverterstations[15]. i QP,i i QP,i
Inregionswithhighdata-centerdensity,suchasAIclusters
thefirst-orderapproximationfrom(13),(14)and(15)becomes
sharing 230–500 kV corridors, this propagation mechanism
synchronizes converter responses across substations. The re-
∆Q (jω)≈(α +jωβ )∆P (jω). (16)
i i i i
sultant voltage–current alignment reinforces correlated load
oscillations generated by synchronized computational work- Transforming to the time domain yields
loads and reduces voltage stability margins.
d∆P (t)
C. Thermal and Environmental Coupling ∆Q i (t)≈α i ∆P i (t)+β i dt i . (17)
Beyond fast electrical interactions, slower environmental
The coefficient α represents the quasi-static dependence of
processes also generate correlated load patterns. Data centers i
reactive power on active power at the converter node, deter-
located in the same geographical area experience similar
mined primarily by the DC-link and PLL control gains, while
weather conditions. Thus, their HVAC systems follow compa-
β quantifies the dynamic phase shift introduced by control
rable heating and cooling patterns. The thermal dynamics of i
and network time constants [8], [9], [15].
each facility is defined by a lumped-capacitance model [16].
Let the active-power fluctuations be spectrally correlated
dT T −T
C th dt i =P I ( T i)(t)− i R amb −Q( co i) ol (t), (11) over a dominant frequency band Ω c , with correlation strength
th λ and total spectral power S at frequency ω . The corre-
where Q( co i) ol is the HVAC cooling rate. When data centers sp 1 onding voltage spectrum (for c the most sensitiv c e mode) can
experience similar ambient temperatures T amb , their cooling be approximated as
controllers respond in a comparable manner. This leads to
correlated cooling demand and electrical load patterns. Such |∆V(jω)|≈ |∆Q(jω)| ≈ |α+jω c β|S c λ 1. (18)
effectismostpronouncedingeographicallyclusteredfacilities σ (J ) σ (J )
min QV min QV
butcanalsoariseinlargecommercialorinstitutionalbuildings
Voltage instability occurs when the correlated disturbance
with similar HVAC control strategies.
energyinthemostsensitivemodeequalsthevoltage-restoring
The mechanisms above act on distinct timescales. GPU
capability, i.e.,|∆V(jω )| ≳ 1. Rearranging (18) yields the
training induces high-frequency power fluctuations [4], con- c
critical correlation threshold,
verter interactions cause mid-frequency dynamics [5], and
HVAC systems add low-frequency modulation [4]. When data σ (J )
λcrit = min QV . (19)
centers are electrically and geographically proximate, these 1 (cid:112) α2+ω2β2S
c c
mechanisms may combine to form correlated load patterns.
Voltage instability is expected when λ >λcrit. Equation (19)
IV. IMPACTSOFCORRELATEDLOADONPOWERSYSTEMS 1 1
expresses an energy balance between correlated stochastic
Spatial and temporal correlations among large electrical
excitation and voltage-restoring stiffness. Higher load cor-
loads reshape system dynamics and reliability margins. When
relation (λ ), dominant low-frequency content (ω ), strong
load variations align across locations, aggregate disturbances 1 c
active–reactive coupling (α,β), or greater spectral power (S )
rise, and system modes show stronger oscillations that reduce c
all lower λcrit, thereby reducing the voltage stability margin.
voltage stability, frequency balance, and available reserves. 1

B. Frequency Deviation Amplification For illustration, with N=10 and a moderate correlation level
ρ =0.3(30%correlation),theaggregatevarianceis37×larger
Correlated load ramps reduce the effectiveness of inertial 0
than that of a single bus and 3.7× larger relative to the
buffering[17].Whendatacentersimposesynchronizedactive- √
independent-load baseline Nσ2, corresponding to a 3.7 ≈
power changes, the aggregate disturbance amplifies the initial
1.9× increase in aggregate standard deviation. This enlarged
frequency deviation.
Let L denote zero-mean load fluctuations at bus i with variability necessitates proportionally higher operating and
i
varianceσ2.Foranalyticaltractability,theN loadfluctuations contingencyreservestomaintainequivalentreliabilitymargins
L areassumedtohaveidenticalvariancesVar(L )=σ2.The under correlated demand fluctuations [17].
i i
uniform pairwise correlation is
V. REAL-TIMEDIGITALSIMULATIONSTUDIES
ρ = Cov(L i ,L j ) , (20) Real-time simulations were conducted on the IEEE 39-bus
so Cov(L ,L ) = σ2 0 if i = σ j 2 , and ρ σ2 otherwise. The test system using the RTDS platform to assess the dynamic
i j 0
(cid:80) impact of spatially correlated data center loads. RTDS was
aggregate load L = L then has variance
agg i
selected because it maintains real-time execution and syn-
(cid:32) N (cid:33) N
(cid:88) (cid:88) (cid:88) chronous phase relationships across loads (which offline tools
σ2 =Var L = Var(L )+2 Cov(L ,L )
agg i i i j cannotguarantee)andprovidessub-microsecondtimestepres-
i=1 i=1 i<j
olutiontocaptureconverterdynamics.ThreerepresentativeAI
=Nσ2+N(N−1)ρ σ2=Nσ2[1+(N−1)ρ ] (21) datacenterswereplacedatbuses4,12,and15,eachsupported
0 0
by dedicated battery energy storage systems (BESS), with
(cid:112)
For a step ∆P agg = 1+(N −1)ρ 0 ∆P 0 , the swing ratings summarized in Table I. Dynamic load models with
equation gives average-value converter representations were employed for
∆f ≈− ∆P 0 (cid:112) 1+(N −1)ρ . (22) the data centers following [6], rather than detailed switching
0 2H f 0 models, as switching frequencies (5–20 kHz) are far above
sys 0
the correlation time scales of interest. The active and reactive
where f is the nominal system frequency and H is
0 sys powerdemandsevolvedaccordingtomulti-cycleAIworkload
the system inertia constant. For N = 5, ρ = 0.8, the
0 patterns, with a correlation coefficient of ρ ≈ 0.4 imposed
factor ∆f ≈ 2.05, doubling the expected dip. This reduces
0 across the three sites to model partial synchronization driven
frequency margins under low-inertia conditions, where fast
bysharedcomputationalscheduling.Thismoderatecorrelation
converter control contains electromechanical waves [15] but
represents a conservative middle ground between statistical
synchronized action worsens RoCoF and nadir.
independence (ρ = 0) and perfect synchronization (ρ = 1).
C. Inter-Area Oscillation Amplification
Spatially correlated load variations can couple into elec- TABLEI
AIDATACENTERLOADSANDBESSRATING
tromechanicaloscillationsoftheinterconnectedsystem.When
thespatialcorrelationmodeofloadfluctuations,sayu ,aligns Bus P [MW] Q [MVAr] P [MW] E [MWh]
1 BESS BESS
with a poorly damped inter-area mode shape ϕ , the modal 4 200 40.6 200 50.0
k
12 225 45.7 225 56.3
excitation strength is proportional to the participation factor
15 250 50.8 250 62.5
|u⊤ϕ |2.Highvaluesindicateconstructivealignmentbetween
1 k
the correlated disturbance pattern and the oscillatory mode.
Figure2ashowstheactiveandreactivepowertrajectoriesat
Correlated activity from large-scale data centers or synchro-
thedatacenterbuses.Thetracesrevealsynchronizedramp-up
nized computing clusters, often concentrated around ∼1 Hz,
and ramp-down sequences, with active power peaks occurring
may interact with inter-area modes typically occurring in the
nearly concurrently across all sites. Reactive power exhibits
0.2–0.8 Hz range, potentially amplifying tie-line oscillations
analogously but with minor phase shifts from independent
anddegradingdamping[11],[17].Spectraloverlapcaninduce
converter voltage regulation. This temporal coherence in load
beat phenomena linking data center power electronics and
evolution generates amplified aggregate power swings relative
AI workloads to wide-area oscillatory behavior [10], [11].
to uncorrelated scenarios, consistent with theoretical expec-
These effects are pronounced when the spectral content of the
tations. The system frequency response, shown in Fig. 2b,
correlated load fluctuations overlaps the dominant electrome-
displays clear sensitivity to the correlated load ramps. During
chanical mode frequencies.
coincident demand surges, frequency deviates downward by
D. Planning and Operating Reserve Implications
up to 0.15 Hz from the 60 Hz nominal. Recovery occurs
Traditional diversity factors assume that individual load promptly as load decreases, supported by generator droop
fluctuations are statistically independent, which yields an action and BESS discharge. The distributed BESS units limit
aggregate variance that scales linearly with the number of the total frequency excursion to within 0.3 Hz peak-to-peak.
buses.Spatiallydistributeddatacenterloads,ontheotherhand This further signifies the need for dedicated ESS for effective
exhibit correlated behavior. Using the covariance structure suppressionoffrequencydeviationsinducedbycorrelatedload
derived in (21), positive correlation (ρ > 0) increases ag- fluctuations. Figure 2c illustrates the RMS voltage response
0
gregate variability relative to the independent-load aggregate. at buses 4, 12, and 15. Voltage magnitudes remain within

300
250
200
150
100
50
0 100 200 300 400 500 600 700
Time (s)
)rAVM
/ WM(
rewoP
Active and Reactive Power at Buses 4, 12, and 15
60.3
Real Power
60.2
60.1
60.0 Reactive Power
59.9
59.8
100 200 300 400 500 600 700
P Bus 4 P Bus 15 Q Bus 12 Time (s)
P Bus 12 Q Bus 4 Q Bus 15
(a)Activeandreactivepowervariations
)zH(
ycneuqerF
System Frequency Response
212
210
208
206
204
100 200 300 400 500 600 700
Time (s)
Frequency
(b)Systemfrequencyresponse
)SMR
V( egatloV
RMS Voltages at Buses 4, 12, and 15
Bus 4 Bus 12 Bus 15
(c)RMSvoltagefluctuations
Fig.2. DynamicresponsesoftheIEEE39-bussystemundercorrelateddata-centerloadprofiles
±2% of the nominal value but show distinct fluctuations REFERENCES
during the correlated load ramps. The nearly simultaneous
[1] A. Shehabi, A. Newkirk, S. J. Smith, A. Hubbard, N. Lei, M. A. B.
voltage dips observed across all three buses reveal a shared Siddik, B. Holecek, J. Koomey, E. Masanet, and D. Sartor, “2024
electromechanical mode driven by spatially correlated load United States Data Center Energy Usage Report,” Tech. Rep. LBNL-
2001637,LawrenceBerkeleyNationalLaboratory,Berkeley,CA,Dec.
variations. This behavior demonstrates inter-bus coupling in
2024. EnergyAnalysisandEnvironmentalImpactsDivision.
the voltage domain and underscores the influence of coherent [2] NERC, “Characteristics and risks of emerging large loads,” task force
load fluctuations on network-wide voltage stability. whitepaper,NorthAmericanElectricReliabilityCorporation,2025.
[3] R. Quint, K. Thomas, J. Zhao, A. Isaacs, and C. Baker, “Practical
Real-time simulations confirm that moderate load corre-
Guidance and Considerations for Large Load Interconnections,” tech.
lation (ρ ≈ 0.4) markedly diminishes the natural diversity rep.,ElevateEnergyConsultingandGridLab,May2025.
effectthatunderpinsclassicalloadindependenceassumptions. [4] S. Go, J. Park, S. More, H. Wu, I. Wang, A. Jezghani, T. Krishna,
andD.Mahajan,“CharacterizingtheEfficiencyofDistributedTraining:
Incorporating spatial load correlation into transient analysis
A Power, Performance, and Thermal Perspective,” in Proceedings of
becomes essential to capture realistic grid behavior. Coordi- the 58th IEEE/ACM International Symposium on Microarchitecture®,
nated BESS operation proves vital to maintain frequency and pp.626–642,2025.
[5] L. Xiong, X. Liu, Y. Liu, and F. Zhuo, “Modeling and stability issues
voltage stability in data-center-dominated networks.
ofvoltage-sourceconverter-dominatedpowersystems:Areview,”CSEE
Journal of Power and Energy Systems, vol. 8, no. 6, pp. 1530–1549,
VI. CONCLUSION
2020.
This paper provides a scientific rationale for characteriz- [6] C. Chaudhary, A. Abdelkader, M. Egan, E. Udren, M. Benidris, and
J. Mitra, “Impact of data center load modeling on power system
ing and analyzing spatially correlated loads in data-center-
stability,” in Grid of the Future Symposium, CIGRE US, (Denver,
dominatedpowersystems.Analyticalderivationsquantifyhow Colorado,USA),Nov.2025.
load correlation amplifies aggregate disturbances, weakens [7] J. Sun, S. Wang, J. Wang, and L. M. Tolbert, “Development of a
converter-based data center power emulator,” in 2021 IEEE Applied
voltage stability margins, degrades frequency response, and
Power Electronics Conference and Exposition (APEC), pp. 126–133,
excites inter-area oscillation modes. Real-time digital simula- IEEE,2021.
tions on the IEEE 39-bus system validate theoretical predic- [8] J. Sun, M. Xu, M. Cespedes, and M. Kauffman, “Data center power
system stability—Part I: Power supply impedance modeling,” CSEE
tions and demonstrate that moderate spatial correlation pro-
JournalofPowerandEnergySystems,vol.8,no.2,pp.403–419,2022.
duces simultaneous frequency and voltage deviations across [9] J. Sun, M. Mihret, M. Cespedes, D. Wong, and M. Kauffman, “Data
multiple buses. The results confirm that traditional diversity centerpowersystemstability—PartII:Systemmodelingandanalysis,”
CSEEJournalofPowerandEnergySystems,vol.8,no.2,pp.420–438,
assumptionsno longerhold inconverter-dominated gridswith
2022.
synchronized computational workloads. [10] C. Mishra, L. Vanfretti, J. Delaree Jr, T. Purcell, and K. D. Jones,
Future research will focus on empirical validation with “Understanding the inception of 14.7 Hz oscillations emerging from a
datacenter,”SustainableEnergy,GridsandNetworks,p.101735,2025.
datafromdata-center-intensiveregionstocalibratecorrelation
[11] M.-S. Ko and H. Zhu, “Wide-Area Power System Oscillations from
models and refine stability thresholds. The development of Large-ScaleAIWorkloads,”ArXiv,vol.abs/2508.16457,2025.
real-time load correlation estimation algorithms for system [12] T. V. Kumar, “Scalable Kubernetes Workload Orchestration for Multi-
CloudEnvironments,”TRJ,vol.11,Jan-March2025.
operators represents a operational need. Investigation of co-
[13] H. B. Patel and N. Kansara, “Dynamic Orchestration of Multi-Cloud
ordinated control strategies for distributed energy storage ResourcesforScalableandResilientAI/MLWorkloads:Strategiesand
systems to mitigate correlation-induced oscillations offers an Frameworks,”Journal,2024.
[14] S. Sharma, N. Kumar, Y. Dash, A. Dubey, and K. Devi, “Intelligent
important direction for grid management. Finally, integration
multi-cloudorchestrationforAIworkloads:enhancingperformanceand
of load correlation metrics into long-term transmission plan- reliability,” in 2024 7th International Conference on Contemporary
ning tools will support infrastructure investment decisions in ComputingandInformatics(IC3I),vol.7,pp.1421–1426,IEEE,2024.
[15] H.Cui,S.Konstantinopoulos,D.Osipov,J.Wang,F.Li,K.L.Tomsovic,
the evolution of AI-driven power systems.
and J. H. Chow, “Disturbance propagation in power grids with high
converter penetration,” Proceedings of the IEEE, vol. 111, no. 7,
ACKNOWLEDGMENT pp.873–890,2022.
[16] H.S.Erden,Experimentalandanalyticalinvestigationofthetransient
The research is supported in part by Sandia National Lab,
thermal response of air cooled data centers. PhD thesis, Syracuse
in part by MSU Research Foundation and in part by the U.S. University,2013.
National Science Foundation under grant 2408615. [17] P. Kundur et al., “Power system stability,” Power system stability and
control,vol.10,no.1,pp.7–1,2007.