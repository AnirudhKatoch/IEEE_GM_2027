Received9July2025,accepted18August2025,dateofpublication26August2025,dateofcurrentversion4September2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3603095
Mission Profile-Based Reliability Assessment for
Modular MVAC-LVDC Solid-State Transformers
AHMEDMELIGY 1,2,RAFAELCOELHO-MEDEIROS1,
ILKNURCOLAK 1,(SeniorMember,IEEE),ANDSEDDIKBACHA 2,(SeniorMember,IEEE)
1SchneiderElectric,38000Grenoble,France
2Univ.GrenobleAlpes,CNRS,GrenobleINP,G2ELab,38000Grenoble,France
Correspondingauthor:AhmedMeligy(ahmed.meligy@se.com)
ABSTRACT This paper introduces a comprehensive framework for evaluating the reliability of modular
MVAC-LVDC Solid-State Transformers (SSTs) based on their mission profiles. The proposed approach
emphasizes the importance of accurately assessing the reliability of Medium-Frequency Transformers
(MFT), which play a critical role in SST performance. The study presents: 1) a mission profile-based
methodologyforanalyzingMFTreliability;2)adetailedprocessforestimatingSSTlifetimethataccounts
forbothrandomandwear-outfailuremechanisms;and3)anexplorationofhowMFTreliabilityinfluences
overallSSTlifespan.Additionally,thepaperoutlinesthedesignmethodologyforMVAC-LVDCSSTsand
detailsthecomponentselectionprocessusedinthereliabilityassessment.Twocasestudies—oneinvolving
anelectricvehicleloadandtheotheradatacenterload—areappliedtoa6.32MVA,11kVAC/1kVDC
SSTdesign.ResultsindicatethatincorporatingMFTreliabilityintotheanalysismayreducetheestimated
SSTlifespanbyover15%,highlightingthevalueofintegratedreliabilityassessmentsinSSTdesign.This
assessment identifies components prone to failure, allowing for redesigns that improve resilience against
missionprofilestressesandextendtheoverallconverterlifetime.
INDEXTERMS Electro-thermalmodeling,medium-frequencytransformers,rainflowcounting,reliability,
solid-statetransformer,wearout.
I. INTRODUCTION Their development focuses on enhancing power density,
TheSolid-StateTransformer(SST)isarelativelyhigh-power controllability, flexibility, and efficiency in electrical sys-
density conversion solution designed to interconnect elec- tems,makingthemsuitableacrossdiversedomains:railway
trical systems operating at different voltage levels—High traction,transmissionanddistributiongrids,microgrids,solar
Voltage (HV), Medium Voltage (MV), and Low Voltage andwindpowergenerationnetworks,electricvehiclecharg-
(LV)—and of different nature, whether Direct Current ing, data center power provisioning, shipboard electrical
(DC) or Alternating Current (AC). Driven by the growing networks,andenergystoragesystems[1].
demand for LVDC interconnections to distributed sources The SST comprises multiple fundamental conversion
and dense loads, SSTs have emerged as a viable alternative units tailored to the interconnected systems, with each
for conventional Low-Frequency Transformers (LFTs) and additional conversion stage offering an extra degree of
power factor correctors. SSTs integrate electrical isolation, freedomforenhancedcontrolcapabilities[1].TheSSTsare
voltagetransformation,andreactivecompensationfunctions therefore categorized based on their conversion stages and
through power electronic circuitry alongside one or more modularity,whereeachtopologypresentsdistinctadvantages
Medium Frequency Transformers (MFTs), while ensuring and trade-offs. In AC-DC applications, including MVAC-
backward compatibility with existing grid infrastructure. LVDC, SSTs have been validated as economically viable
alternatives to conventional systems [2]. These can employ
The associate editor coordinating the review of this manuscript and eithersingle-stageortwo-stageconfigurations,withthelatter
approvingitforpublicationwasTruong-DuyDuong . enabling input-output decoupling through DC links at both
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
151736 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
MV and LV levels [3]. To effectively meet the voltage handbooksthatprovideconstantfailureratestoestimatethe
and power requirements of MV applications, a modular MFTlifespan[26],[27],[28],[29],[30].
Input Series Output Parallel (ISOP) arrangement of con- Prior research has made strides in understanding SST
verter modules is often employed. This approach facilitates reliability; however, a research gap remains in adequately
voltage and current sharing among cascaded cells, thereby addressing the lifetime of MFTs and their impact on the
enhancingscalabilityandimprovingfault-resiliencethrough overall reliability of SSTs. When the SST is connected to
redundancy.However,thelargenumberofpowerelectronic medium-voltage (MV) mains, it is essential for the MFT to
devices in modular designs introduce reliability concerns. provide,ataminimum,medium-voltagefunctionalisolation
As all components are required to operate simultaneously, in accordance with the environmental pollution degree
the likelihood of failure increases, creating key technical outlined in IEC 60664-1 [31] to ensure operational safety.
bottlenecks that limit SST deployments. Although adding In addition to complying with MV insulation standards,
redundantmodulescanenhancereliability,itmayalsoresult MFTs must withstand electric field stresses caused by
in considerably higher costs. Therefore, finding the right pulse-widthmodulation(PWM)voltageduringbothnormal
balance between modularity and reliability is vital in SST and transient conditions. The combination of high voltage
design. To be a viable alternative to conventional systems, and high-frequency waveforms, along with the thermal
the longevity of SSTs should meet or surpass the already challenges stemming from the compact design of MFTs,
high standards set by their competition, while ensuring can lead to increased Partial Discharge (PD) activity within
comparableorimprovedefficiency. the insulation. This rise in PD activity increases the risk
While reliability studies on switching devices and capac- of dielectric material breakdown within the MFT and
itors are well-established [4], [5], [6], [7], [8], [9], [10], accelerates aging [32], [33], [34], [35], potentially reducing
[11],[12],researchonthereliabilityandlifespanassessment thelifetimeoftheSST.
of MFT remains largely underexplored in the literature. Given these challenges, an SST reliability study consid-
Previous works on SST reliability often overlook the ering the lifetime of MFTs is crucial for understanding the
influence of MFT lifespan on overall system reliability. remaining lifespan of the entire system. Future research
For example, in [13], the authors examine the cost and should aim to create comprehensive reliability models that
reliability of different SST module topologies, but their takeintoaccounttheuniquecharacteristicsandfailuremodes
assessmentreliesonconstantfailureratesandfocusessolely ofMFTs.Therefore,thispapercontributestothreekeyareas:
on semiconductor devices. In [14] and [15], the authors firstly,itproposesamissionprofilebasedtheoreticalframe-
combine reliability evaluation with redundancy designfor a work for estimating MFT reliability within MVAC/LVDC
modularDC/DCSSTfocusingonwear-outfailureanalysis, SSTs; secondly, it provides the complete methodology for
yettheyomitMFTsfromtheirevaluation.Similarly,in[16], lifetimeestimationoftheSSTthatincorporatesbothrandom
a mission profile-based reliability assessment for SSTs in failures derived from reliability handbooks and wear-out
railwayapplicationsispresented,butitalsoexcludesMFTs. failures assessed through a cycle-counting approach; and
In[3]and[17],theauthorsproposeapowerroutingmethod thirdly, it demonstrates the effects of MFT reliability when
betweenSSTmodulestoenhancethesystem’slifespan,but factoredintheSSTlifetimeestimation.Assystemreliability
their analysis estimates the remaining useful lifetime of the is integral to the design process, this paper also briefly
modules solely through power semiconductors. Likewise, outlines the design methodology for an MVAC-LVDC
in [18], a power routing control method based on virtual SST and details the component selection for which the
resistance is presented. While both power switches and mission-basedreliabilityassessmentisperformed.
capacitorsareinvestigatedinthiswork,theMFTreliabilityis The remainder of this paper is structured as follows.
yetomittedfromtheanalysis.Conversely,theauthorsin[19] Section II provides a brief overview of reliability metrics.
introduce a reliability-oriented SST design that employs a Section III describes the SST design and components
secondharmoniccurrentroutingmethod,incorporatingMFT selectionusedinthiswork.SectionIVillustratesthepower
reliabilityintotheirassessment,howevertheyuseempirical losses within the SST components and their translation to
lifetime equations for LFTs to estimate MFT lifespan. electro-thermal models. Section V describes each of the
In [20] and [21], the authors conducted a comparative components reliability estimation procedure. Section VI
analysisofvarioustopologyvariationsforcascadedmodular providesresultsofdifferenttestcasesfortheSSTreliability
MVAC-LVDC SSTs, evaluating multiple criteria, including model.SectionVIIsummarizesthefindingsofthisstudy.
reliability. The findings indicate that the front-end half-
bridge matrix-based dual active bridge module offers the II. RELIABILITYMETRICS:ABRIEFOVERVIEW
best compromise among the criteria studied. However, the Reliability is defined as the probability that a device will
reliabilityassessmentwasbasedsolelyontherandomfailure not fail for a specified duration under nominal operating
analysis of the semiconductors and capacitors. Moreover, conditions. In modern power electronics based systems,
reliability assessments of single-stage isolated converters understandingtheexpectedlifespanofconvertersisessential
similarly either overlook MFT reliability altogether [22], for making informed decisions regarding facility planning,
[23],[24],[25]orrelyonempiricalequationsfromreliability cost-effectivedesign,andreplacementscheduling[36].
VOLUME13,2025 151737

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
There are five critical reliability metrics that are used to a system of multiple components, if the failure of any
assess the lifetime of a device [37], [38], [39]. Firstly, the individualcomponentleadstothefailureoftheentiresystem,
failure probability density function (pdf) denoted by f(t) a series reliability network is utilized were the system’s
which indicates the failure distribution over a device’s failure rate is the sum of all individual components failure
| entire lifetime. | Secondly, |     | the failure | cumulative |     | distribution | rates. |     |     |     |     |     |     |     |
| ---------------- | --------- | --- | ----------- | ---------- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
function (cdf), also called the unreliability function and is X X
|     |     |     |     |     |     |     |     | h   | (t)= | h   | (t)+ |     | h   | (t) (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | ------- |
denotedF(t),whichdescribestheprobabilityoffailurebya sys,tot comp,r comp,wo
specifiedtimet.Thirdly,thereliabilityfunctionR(t),which Conversely,systemswithredundantstructuresandstandby
isthecomplementofF(t),andrepresentstheprobabilityof components utilize a combination of parallel and series
thedeviceoperatingwithoutfailurebetweentime0andtime reliability networks, for which reliability techniques like
| t,withR(0)=1andR(∞)=0. |                |     |     |     |        |     | Markovmodelsareused[38],[39]. |     |     |     |     |     |     |     |
| ---------------------- | -------------- | --- | --- | --- | ------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                        |                |     |     | Z   | ∞      |     |                               |     |     |     |     |     |     |     |
|                        | R(t)=1−F(t)=1− |     |     |     | f(x)dx | (1) |                               |     |     |     |     |     |     |     |
A. RANDOMFAILURE
t Predicting the failure rate during the useful lifetime of a
| The fourth | metric | is  | the hazard/failure |     | rate | h(t) which |        |           |          |     |           |            |     |              |
| ---------- | ------ | --- | ------------------ | --- | ---- | ---------- | ------ | --------- | -------- | --- | --------- | ---------- | --- | ------------ |
|            |        |     |                    |     |      |            | device | primarily | involves |     | analyzing | historical |     | failure data |
representsthelikelihoodofadevicefailingintheupcoming
|     |     |     |     |     |     |     | from | previous | operations, |     | with | more accurate | data | obtained |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ----------- | --- | ---- | ------------- | ---- | -------- |
timeinterval,providedthatithasbeenfunctioningcorrectly from long-term use under consistent operating conditions.
| up to time | t, essentially |     | indicating | the | instantaneous | risk of |             |          |            |               |     |            |            |            |
| ---------- | -------------- | --- | ---------- | --- | ------------- | ------- | ----------- | -------- | ---------- | ------------- | --- | ---------- | ---------- | ---------- |
|            |                |     |            |     |               |         | Reliability |          | handbooks, | such          | as  | the widely | recognized | Mil-       |
| failure.   |                |     |            |     |               |         | itary       | Handbook | 217        | (MIL-HDBK217) |     |            | [41],      | along with |
f(t)
|     |     |     | h(t)= |     |     |     | otherslikeTelcordiaSR-322,SiemensSN29500,RDF-2000, |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
(2)
|     |     |     |     | R(t) |     |     | IEC-TR-62380, |     | IEC-61709, |       | and         | FIDES,     | provide | generic    |
| --- | --- | --- | --- | ---- | --- | --- | ------------- | --- | ---------- | ----- | ----------- | ---------- | ------- | ---------- |
|     |     |     |     |      |     |     | estimates     |     | of failure | rates | for various | electronic |         | components |
Finally,theMeanTimeToFailure(MTTF)whichsignifies
theequivalentlifetimeinoperationandiscalculatedas based on available operational data. These handbooks offer
|     |     |     |     |     |     |     | a base | failure | rate | (λ ) for | each | component | and | incorporate |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---- | -------- | ---- | --------- | --- | ----------- |
|     |     |     | Z   | ∞   |     |     |        |         |      | b        |      |           |     |             |
π
MTTF = R(t)dt (3) various stress factors (e.g., electric factor - S , temperature
|     |     |     |     | 0   |     |     | stress-π |     | ,qualityfactor-π |     | ,environmentalfactor-π |     |     | ,..., |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------------- | --- | ---------------------- | --- | --- | ----- |
|     |     |     |     |     |     |     |          | T   |                  |     | Q                      |     |     | E     |
Fig. 1 depicts the standard hazard function for a device etc.)toaccountfortheireffectsonthecomponent’sreliability.
over its lifecycle, highlighting three distinct phases: early Furthermore,onecanutilizedatasuppliedbymanufacturers
failures, useful life, and wear-out failures [36], [37], [38], orusersasthefoundationalfailureratetoestimatethefailure
[39], [40]. Early failures are often overlooked in reliability rateforspecificoperatingconditions.
studies, as they generally arise from manufacturing defects Random failure is often modeled using the exponential
ordebuggingissues,whicharetypicallyresolvedpriortothe distribution function, as presented in (5) [38], [39]. The
randomfailurerate(λ
device being put into operation. During the useful lifetime r ),whichfortheexponentialreliability
thedevicemayexperiencerandomfailuresduetounexpected functionisequivalenttoh comp,r (t),representsthemeanofthe
instantaneousfailureratecalculatedateachoperatingpointi
internalfaultsorexternalenvironmentalfactors.Ontheother
hand, as materials age, the device may enter the wear-out acrossntotalpoints.
| phase, | where failure | rates | increase |     | due to the | effects of |     |     |        |     |     |     |     |     |
| ------ | ------------- | ----- | -------- | --- | ---------- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- |
|        |               |       |          |     |            |            |     |     | R(t)=e | −λ  | rt  |     |     |     |
(5)
materialdegradationandthecumulativestressesexperienced
|                  |     |     |     |     |     |     |     |     |     |     |     | S,T ,Q,E,... |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
| duringoperation. |     |     |     |     |     |     |     |     |     | 1   | N   |              |     |     |
|                  |     |     |     |     |     |     |     |     | λ   | =   | X λ | Y            | π   |     |
|                  |     |     |     |     |     |     |     |     | r   |     | b   |              | k   | (6) |
N
i=1
k
|     |     |     |     |     |     |     | Although     |         | these    | handbooks |         | are still  | used        | for lifetime |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | -------- | --------- | ------- | ---------- | ----------- | ------------ |
|     |     |     |     |     |     |     | estimations, |         | some     | of them   | have    | several    | notable     | concerns,    |
|     |     |     |     |     |     |     | including    |         | outdated | data,     | unclear | failure    | mechanisms, | and          |
|     |     |     |     |     |     |     | some         | exclude | various  | operating |         | conditions | [36].       | Therefore,   |
theassumptionofaconstantfailurerateinthesehandbooks
canresultinunrealisticprojections,especiallyincaseswhere
componentsenterthedegradationphaseduringtheirmission
profile,inwhichcasewear-outfailuremustbeconsidered.
FIGURE1. Failureratebathtubcurve.
B. WEAR-OUTFAILURE
In general, a component or system fails when a specific Wear out failure analysis is based on a Physics-of-Failure
failure mechanism is triggered, either by random chance or (PoF) approach, which emphasizes the investigation of
by wear-out processes. The total failure rate of the device, root-cause failure mechanisms and how materials, defects,
denoted as h (t), is the sum of the random failure rate and stresses affect product reliability. This method dis-
tot
(h r (t))andthewear-outfailurerate(h wo (t)).Whenassessing tinguishes between overstress failures, which result from
| 151738 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
a single event, and wear-out failures, which arise from emissions. Semi-modular configurations adopt a hybrid
cumulative damage due to the mission profile. Unlike approach,oftencombiningamodularMV-sideconverterwith
empiricalfailureanalysis,whichreliesonhistoricaldata,the asingleLV-sideconverterviaanMFT.Thisapproachreduces
PoFapproachisrootedindeterministicscience,necessitating the component count while retaining some advantages of
an understanding of component material properties, failure modularity.
mechanisms,andmissionprofiles[40].Asaresult,degrada- A wide variety of SST topologies have been proposed
tion cannot be generalized across different mission profiles by both academia and industry for which [20], [21], [43],
without conducting extensive tests on multiple devices to [44], [45], [46] provide a comprehensive summary. These
establish a failure probability density function. Therefore, generally comprise three fundamental conversion units—
lifetimeestimatesaregeneratedfromacceleratedagingtests, AC/DC, AC/AC, and DC/AC—with an MFT providing
enablingfailureratepredictionsforsimilardevicesthatshare galvanic isolation. These building blocks allow SST archi-
technologyandoperatingconditions[42]. tectures to be categorized based on the number and role
Astatisticalmethodcanbeemployedtoaccountforpoten- of DC links. Single-stage and quasi-single-stage topologies
tialvariationsinthecalculatedmeasurementsandparameters typically include a single DC link at the LV output,
ofthelifetimeequationusingMonteCarlosimulations[40]. implemented through direct and indirect matrix converters,
The lifetime data derived from the Monte Carlo analysis respectively,atthefrontendoftheSST.Incontrast,two-stage
is then commonly fitted to a Weibull probability density converterarchitecturesemploytwodecoupledDClinks:one
function (pdf), as described in (7), where α and β indicate at the MV side and one at the LV output. This decoupling
thescaleandshapeparameters,respectively. enablesindependentcontroloftheupstreamanddownstream
converters,providingmorecontrolflexibility.
f(t)=
β (cid:18) t (cid:19)β−1
e
−(
α
t)β
(7)
It is important to recognize that every aspect of the
α α SSTdesignprocessinfluencestheoverallconverterlifetime.
Amajorsourceofreliabilityvariationstemsfromthechosen
III. SSTDESIGN architecture,whethersingle-stage,quasi-single-stage,ortwo-
WhiletheconceptoftheSSTpresentsmanifoldadvantages, stage,aswellasthespecificconvertertopologyemployedat
its design and realization present significant technical eachstage.Theseconfigurationsdifferincomponentcount,
challenges, particularly in topology selection and reliability operating principles, modulation strategies, use of resonant
optimization. SSTs can be broadly classified based on circuitry, and switching frequencies, all of which affect
theirmodularityintomonolithic,modular,andsemi-modular stress distribution and lifetime estimation. Furthermore,
architectures [1], [43], [44], [45], [46]. Monolithic config- the mission profile and the stress tolerance of individual
urations use a single power converter rated for full power, components significantly impact system longevity. Lower
requiring HV power switches or a series association of LV overall efficiency can also lead to increased thermal losses,
power switches to scale up for the MV applications. While exposing components to elevated temperatures, thereby
thisreducesthenumberofcomponentsandsimplifiescontrol acceleratingagingmechanisms.
strategies,itmaycompromisefaulttoleranceandscalability. Among the various SST topologies reported in the
Modulardesignsconsistofmultipleconvertermodules,with literature, one of the most widely adopted configurations is
theISOPconfigurationbeingthemostcommonforMV/LV themodulartwo-stageconversionarchitecture,inwhicheach
conversions. This approach offers voltage/current scalabil- SSTmoduleemploysaFull-BridgeVoltageSourceConverter
ity, redundancy, and reduced electromagnetic interference (FB-VSC) at both the MV and LV stages, as illustrated in
FIGURE2. MVAC-LVDCISOPSST.
VOLUME13,2025 151739

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
Fig. 2. This topology was selected for the present study range [47]. The equal turns on the primary and secondary
due to its relative simplicity and reduced component count windings simplify the design, enhance magnetic coupling,
comparedtomorecomplexalternatives.Whilethereliability and reduce leakage inductance, which minimizes core and
assessmentframeworkdevelopedinthisworkisapplicableto copperlossestherebyincreasingtheefficiencyoftheMFT.
any SST topology or architecture, this particular configura- With 1 kV DC-links as per the system requirements
tionwaschosenasarepresentativebaselinetoestablishand and utilizing a FB-VSC, the maximum modulated Root
demonstrate the methodology. It serves as a foundation for Mean Square (RMS) voltage (V m (k , ) rms ) for a single module
futureinvestigationsintothereliabilityperformanceofmore iscalculatedtobe0.7071kV.Whereas,theRMSmaximum
(cid:54)
advancedsolid-statetransformerdesigns. modulatedACgridvoltagerequirementV m,rms iscalculated
as
A. REFERENCECASE q
Inthisstudyweconsidera6.32MVA,11kVAC/1kVDC V m (cid:54) ,rms = Re(v (cid:54) m,rms )2+Im(v (cid:54) m,rms )2 (8)
SST which schematic is illustrated in Fig. 2, and has
where,
the fixed parameters presented in Table 1 for which the
c
T
o
h
m
e
p
M
on
V
e
A
n
C
tss
g
e
r
l
i
e
d
ct
i
i
s
on
m
i
o
s
d
d
e
e
l
t
l
a
e
i
d
led
by
in
a
t
n
he
e
f
q
o
u
ll
i
o
v
w
al
i
e
n
n
g
t
s
t
u
h
b
re
s
e
ec
p
ti
h
o
a
n
s
s
e
. v (cid:54) m,rms = v g√ll ·
3
k g +(R tot +jX tot )i g (9)
source v in series with its equivalent impedance L ,
ga,b,c g whereas,R =R +R ,X =2πf (L +L ),k denotesthe
R . In the remainder of this article, the phase indices (a, tot g f tot 0 g f g
g maximumgridovervoltagelimit,v isthecomplexline-to-
b, and c) are omitted from the variables for simplicity. The gll
line grid RMS voltage, and i represents the complex RMS
ISOP SST is connected to the grid through a line inductor g
grid current at rated power. The real and imaginary part of
a
w
n
i
d
th
m
i
o
n
d
d
u
u
l
c
a
t
t
a
e
n
d
ce
vo
L
lt
f
ag
a
e
n
a
d
re
re
d
s
e
i
n
st
o
a
t
n
e
c
d
e
i
R
a
f
n
.
d
T
v
h (cid:54) e
,
g
re
r
s
id
pec
c
t
u
iv
rr
e
e
l
n
y
t
.
v (cid:54) m,rms canbederivedas
g m
WhereasthecurrentandvoltageattheLVDCsidearedenoted Re(v )·k
i and v , respectively. The Active Front End Converter Re(v (cid:54) m,rms )= √gll g +R tot ·Re(i g )−X tot ·Im(i g )
L L 3
(AFEC) connects the AC grid to the primary-side DC bus Im(v )·k
v ( C k , ) p oftheIsolatedDC/DCconverter.Inaddition,itemploys Im(v (cid:54) m,rms )= √gll 3 g +R tot ·Im(i g )+X tot ·Re(i g )
Phase-Shifted PWM (PS-PWM) to generate the modulated
voltagev (k) ,wherek ∈ [1,...,Nmod],andNmod represents (10)
m
thetotalnumberofmodulesperphase.TheisolatedDC/DC The minimum number of modules required per phase can
converteroperatesasaDual-ActiveBridge(DAB),utilizing thenbecomputedasfollowsandusedtodeterminetheopti-
trapezoidal modulation and featuring a medium frequency malblockingvoltageofthedeployedsemiconductors[48],
linkthatconsistssolelyoftheMFTtomaintainlowleakage
(cid:54) !
inductanceforhighefficiencyconversions[47]. Nmod =ceil V m,rms (11)
min V m (k , ) rms ·M max
B. COMPONENTSSELECTION
To attain high conversion efficiency in the DAB stage, where, M max is the maximum modulation index of the
the primary DC-link voltage is configured to match the converter. For this analysis, we have assumed an upper
secondaryDC-linkvoltage,ensuringaprimary-to-secondary grid overvoltage limit of 1.15 p.u. and set M rms to 0.95.
DC voltage ratio (N t V dc,s /V dc,p ) of 1 with a 1:1 turns This results in Nmod=12 modules per phase, each rated at
ratio in the MFT. This DC voltage ratio is established to 175.7kVAforan11kVline-to-linegrid.Theswitchingfre-
enabletrapezoidalmodulationthroughoutthefulloperational quencyfortheAFEC(f sw,
AFE
)usingPS-PWM,isestablished
at250Hztominimizemodulationharmonicswithinthe50th-
order window, ensuring that the first sideband harmonics
TABLE1. SSTmainsystemparameters. occur at the 2Nmod f sw,
AFE
order. Consequently, 1.7 kV
Si-IGBTswitchesareutilized,giventheircompatibilitywith
thelowswitchingfrequencyandthedefinedDCbusvoltage.
TheDABconverteroperatesatahigherswitchingfrequency
(f sw,
DC
= 15 kHz) to reduce the weight and volume of the
MFT. In this scenario, 2 kV SiC MOSFETs are considered
owing to their low switching losses at high frequencies and
reduced heat generation. The specifications of the selected
switchesforthisstudyareprovidedinTable2.
The primary DC-bus capacitor must filter the current
harmonics generated by the AFEC and the primary side
of the DC/DC converter. The DC/DC converter produces
high-frequency harmonics at multiples of its switching
151740 VOLUME13,2025

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
TABLE2. Modulecomponents&properties[49],[50],[51].
frequency of 15 kHz, while the AFEC generates har-
monics starting from double the fundamental frequency.
Lower-frequency harmonics encounter significantly higher
impedance than higher-frequency ones, which leads to
increased losses and voltage ripple thereby increasing
the capacitor filter requirements on the primary DC-bus.
While the low-order current harmonics, at integer multiples
of the grid frequency, are transferred from the primary
FIGURE3. MFTdesignalgorithm.
to the secondary side, they are, however, attenuated by the
MFTinductance.Consequently,thecurrentinthesecondary
DC-link is characterized by even multiples of the DC/DC material,andk isanadditionalsafetymarginthataccounts
saf
converter’s switching frequency, along with sidebands at fortransientovervoltage,andissetto0.3inthisstudy.
integermultiplesofthefundamentalfrequency.
The minimum required capacitance for each of the d iso =
V di-ins
(12)
k saf E di-ins
DC-links is calculated based on the maximum charge
variationcorrespondingtothemostdemandinggridoperating To determine the different V di−ins within the MFT, the
point,whileensuringamaximumvoltagerippleof5%.This potential of each wire turn in the MFT to ground must be
pointcorrespondstotheloweroperationalboundofthegrid calculated.Thisisdonebyfirstcomputingthevoltageatthe
voltage at rated apparent power transfer. The specifications inputandoutputterminalsofboththeprimaryandsecondary
fortheselectedcapacitorsarepresentedinTable2. windings, these reference points are marked by crosses in
Fig. 2. By tracing the path from each of these reference
points to ground, a generalized equation can be derived for
C. MFTDESIGN
the potential difference of each of the four MFT terminals
While switches and capacitors are off-the-shelf products,
to ground. These equations are formulated in the frequency
high-power MFTs are custom-made based on the system’s
domain as presented in (13)-(16), where V u,(1...6) denotes
ratings. In this study, we follow a design procedure similar
the voltage across the upper switches of the corresponding
to those presented in [52], [53], and [54] to design a
switchingcellcontrolledbytheswitchingsignalsu through
1
15 kHz, 170 kW MFT. The flowchart of the MFT design
u .Thetime-domainwaveformsforModule1,corresponding
6
procedureispresentedinFig.3.
to these equations, are shown in Fig. 4. Once the terminal
The design follows an iterative process in which the
voltages are known, the voltage on each individual wire
algorithm loops through a database of different cores,
turn within the MFT can be determined by assuming a
along with their corresponding material properties and wire
constantvoltagedropbetweenadjacentconductors,ensuring
types. It takes as input the electrical system parameters
auniformvoltagegradientthroughoutthewindingstructure,
(P nom , V dc,(p,s) , f sw , N t ) as well as the insulation material basedonthespatialpositioningofeachconductor.
propertiesofthewindingsandwires.AninitialMFTsizing
is determined from these input parameters and checked k:Nmod
for feasibility in terms of geometry. If the design is V m (k ft ) p,i = X V m (n)+V u ( , n 1 )−V u ( , n 3 )+V diff (13)
dimensionallyfeasible,theinsulationdistancesarecalculated n
and compared to the minimum requirements specified by k:Nmod
theBasicInsulationLevel(BIL)standards.Accordingtothe V m (k ft ) p,o = X V m (n)+V u ( , n 1 )−V u ( , n 4 )+V diff (14)
IEC60664-1standards,amedium-voltagesystemoperating n
at 11 kV must typically have a standard BIL rating of V (k) =V −V (k) (15)
mfts,i L u,6
60 kV [31]. The insulation distances based on the material V (k) =V −V (k) (16)
arecalculatedby(12),whereV di-ins representsthemaximum mfts,o L u,5
potential difference the insulation must withstand, E di-ins is The MFT electrical parameters (L p ,R p ,L s ,R s ,L m ) are
thefrequency-dependentdielectricstrengthoftheinsulating determined through open circuit tests using a magnetostatic
VOLUME13,2025 151741

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
FIGURE5. 2Dcross-sectionofreferenceMFTdesign.
FIGURE4. Module1MFTwindingsinputandoutputvoltagepotentials.
TABLE3. ReferenceMFTparameters.
FIGURE6. ModulatedvoltagesandcurrentsofreferenceMFTdesignat
nominalpower.
calculated,takingintoaccountthespecificisolatedconverter
operation, to determine the MFT losses and the expected
hotspot temperature. The criterion for a valid design in
this work is set at 150 ◦C at rated power. The hotspot
estimation and power loss methodology are explained in
more detail in the following section. In this study, the
chosen transformer from the iterations is one characterized
by relatively small leakage inductance and relatively high
magnetizing inductance to achieve the highest efficiency
using trapezoidal DAB modulation, as illustrated in [47].
In addition, the MFT design considers two aluminum
heatsinksmountedonthetopandbottomsurfaceofthecore
area. The designed MFT parameters used in this study are
presented in Table 3, and a 2D cross-section of the MFT is
showninFig.5.Additionally,thedesignedMFTwaveforms
atnominalpowerarepresentedinFig.6andareutilizedfor
theMFTlossescalculationinthesubsequentsection.
IV. LOSSCALCULATIONANDTHERMALANALYSIS
Power electronic converters face two main stress factors
throughout operation: electrical loading and temperature
cycling [56]. These factors induce thermal stresses, neces-
sitating careful design to ensure component durability.
To evaluate the lifespan of each component under their
model with open boundary conditions, deployed in Finite experienced thermal conditions, precise temperature pre-
Element Method Magnetics (FEMM) software [55]. The dictions are essential. In this study, owing to their low
MFT waveforms (v m,(p,s) ,i (p,s) ,) at rated power are then computationaldemands,electrothermalmodelsaredeployed
151742 VOLUME13,2025

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
toestimatethehotspottemperaturesoftheSSTcomponents. transistor, the current flows in both positive and negative
In these models, the temperatures at the nodes are assumed direction through the transistor. In which case, the current
homogeneous, with the temperature drops between them separationcanbeformulatedasfollows.
modeledviathermalresistances.
|     |     |     |     |     |     |     |     |     | mosfet | (t)=−u |     | (t)·i |       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ----- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     | i tru  |        |     | sw    | m (t) |     |     |
mosfet
| A. SEMICONDUCTORSLOSSESANDTHERMAL |     |     |     |     |     |     |     |     | i   | (t)=0 |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
Du
| MODELLING     |        |     |             |     |                 |     |     |     | i mosfet | (t)=(cid:0) | 1−u | (t) | (cid:1)·i (t) |     |     |
| ------------- | ------ | --- | ----------- | --- | --------------- | --- | --- | --- | -------- | ----------- | --- | --- | ------------- | --- | --- |
|               |        |     |             |     |                 |     |     |     | trl      |             |     | sw  | m             |     |     |
| Semiconductor | losses | are | categorized |     | into conduction | and |     |     |          |             |     |     |               |     |     |
|               |        |     |             |     |                 |     |     |     | m        | o sfet      |     |     |               |     |     |
switchinglosses,calculatedinthisworkasdetailedin[47]. i (t)=0 (18)
D l
| Fig. 7 illustrates         | the           | current                         | division     | within                 | a conventional   |     |                                           |         |            |      |       |        |               |           |     |
| -------------------------- | ------------- | ------------------------------- | ------------ | ---------------------- | ---------------- | --- | ----------------------------------------- | ------- | ---------- | ---- | ----- | ------ | ------------- | --------- | --- |
|                            |               |                                 |              |                        |                  |     | The                                       | average | conduction |      | power | losses | for           | the upper | and |
| power module               | configuration |                                 | representing |                        | either a Si-IGBT |     |                                           |         |            |      |       |        |               |           |     |
|                            |               |                                 |              |                        |                  |     | lowerswitchesoverafundamentalperiodT      |         |            |      |       |        | canbecomputed |           |     |
| oraSiCMOSFET.Inthefigure,i |               |                                 |              | representsthemodulated |                  |     |                                           |         |            |      |       |        | 0             |           |     |
|                            |               |                                 |              | m                      |                  |     | aspresentedin(19),forbothIGBTsandMOSFETs. |         |            |      |       |        |               |           |     |
| current,whilei             | andi          | denotecurrentpassingthrougheach |              |                        |                  |     |                                           |         |            |      |       |        |               |           |     |
|                            | tr            | D                               |              |                        |                  |     |                                           |         |            | Z T0 |       |        |               |           |     |
o f t h e t r a n s i st or ( e i th e r a n I G B T o r M O S F E T ) a nd t h e d i o d e , 1 (cid:0) (cid:1)
|     |     |     |     |     |     |     | P   | (t)=    |     | i       | (t)v | i          | (t),T     | (t) | dt  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | ---- | ---------- | --------- | --- | --- |
|     |     |     |     |     |     |     |     | tr(u,l) |     | tr(u,l) |      | on tr(u,l) | j,tr(u,l) |     |     |
re s p e c t iv e l y . W h e r e as , t h e s ub s cr ip ts u a n d l re fe r to t h e u p p e r T 0 0
a n d lo w e r s w i tc h e s , r e s p e c t iv e ly . T he g a ti ng s i g n al a p p l i ed t o 1 Z T0
|     |     |     |     |     |     |     |     | (t)= |     |     |     | (cid:0) | (t),T | (cid:1) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------- | ----- | ------- | --- |
th e p o w e r m o d u l e i s r e p r e s e n te d b y u . A dd i t io n al l y , i n th i s P D(u,l) i D(u,l) (t)v f i D(u,l) j,D(u,l) (t) dt (19)
|     |     |     |     | s w |     |     |     |     | T   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | 0   | 0   |     |     |     |     |     |
study,weconsiderzerodead-timeforsimplification.
|     |     |     |     |     |     |     | For | switching  |     | losses, | the | exact   | switching |     | instances |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --- | ------- | --------- | --- | --------- |
|     |     |     |     |     |     |     | are | determined | as  | follows | for | each of | the upper | and | lower     |
Si-IGBTs.
|     |     |     |     |     |     |     |     |     | igbt =t  |       | (cid:49)u | )>0&i |      | )<0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --------- | ----- | ---- | --- | --- |
|     |     |     |     |     |     |     |     |     | t tru,ON | s ,if | sw        | (t s  | m (t | s   |     |
igbt
|     |     |     |     |     |     |     |     |     | t =t    | ,if   | (cid:49)u | (t )<0&i | (t   | )<0 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | -------- | ---- | --- | --- |
|     |     |     |     |     |     |     |     |     | tru,OFF | s     | sw        | s        | m    | s   |     |
|     |     |     |     |     |     |     |     |     | igbt =t |       | (cid:49)u | )<0&i    |      | )>0 |     |
|     |     |     |     |     |     |     |     | t   |         | s ,if | sw        | (t s     | m (t | s   |     |
Du,OFF
|     |     |     |     |     |     |     |       |              | t igbt =t | ,if | (cid:49)u | (t )<0&i | (t      | )>0            |      |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --------- | --- | --------- | -------- | ------- | -------------- | ---- |
|     |     |     |     |     |     |     |       |              | trl,ON    | s   | sw        | s        | m       | s              |      |
|     |     |     |     |     |     |     |       |              | igbt      |     | (cid:49)u | )>0&i    |         | )>0            |      |
|     |     |     |     |     |     |     |       |              | t =t      | ,if |           | (t       | (t      |                |      |
|     |     |     |     |     |     |     |       |              | trl,OFF   | s   | sw        | s        | m       | s              |      |
|     |     |     |     |     |     |     |       |              | t igbt =t | ,if | (cid:49)u | (t )>0&i | (t      | )<0            | (20) |
|     |     |     |     |     |     |     |       |              | Dl,OFF    | s   | sw        | s        | m       | s              |      |
|     |     |     |     |     |     |     | Here, | t represents |           | the | specific  | time     | step of | the simulation |      |
s
|                                                      |                                  |               |         |                 |                  |         | and        | (cid:49)u  | is the     | difference | in        | the gating |             | signal        | from the |
| ---------------------------------------------------- | -------------------------------- | ------------- | ------- | --------------- | ---------------- | ------- | ---------- | ---------- | ---------- | ---------- | --------- | ---------- | ----------- | ------------- | -------- |
| FIGURE7.                                             | Singlepowermodulerepresentation. |               |         |                 |                  |         |            | sw         |            |            |           |            |             |               |          |
|                                                      |                                  |               |         |                 |                  |         | previous   |            | time step. | On         | the other | hand,      | for         | SiC MOSFETs,  |          |
| To determine                                         | conduction                       |               | losses, | 2-D             | linear scattered |         |            |            |            |            |           |            |             |               |          |
|                                                      |                                  |               |         |                 |                  |         | as         | conduction | occurs     | only       | through   | the        | transistor, | switching     |          |
| interpolatorsareemployedtoobtaintheon-statevoltagesv |                                  |               |         |                 |                  | on      |            |            |            |            |           |            |             |               |          |
|                                                      |                                  |               |         |                 |                  |         | losses     | are        | incurred   | only       | by the    | MOSFET     | at          | the following |          |
| and the forward                                      | voltages                         |               | v for   | the transistors | and              | diodes, |            |            |            |            |           |            |             |               |          |
|                                                      |                                  |               | f       |                 |                  |         | instances, |            | while      | the body   | diode     | does       | not         | contribute    | to       |
| respectively.                                        | These                            | interpolation |         | functions       | are established  |         |            |            |            |            |           |            |             |               |          |
switchinglosses.
fromthepowermodule’sdatasheetandareafunctionofthe
|     |     |     |     |     |     |     |     |     |     | m o sf et |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
respectivecomponent’scurrenti andjunctiontempera- t =t ,if (cid:49)u (t )>0
|     |     |     | (tr,D) |     |     |     |     |     | t   | ru ,O N | s   | sw  | s   |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
tureT j,(sw,D) .Theconductioncurrentisfirstcalculatedbased mosfet =t (cid:49)u )<0
|                                                     |     |     |     |     |     |     |     |     | t       |     | s ,if | sw (t | s   |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- | ----- | --- | --- | --- |
| ontheswitchtechnology.ForanIGBT,thecurrentisdivided |     |     |     |     |     |     |     |     | tru,OFF |     |       |       |     |     |     |
acrosseachoftheupperandlowertransistorsanddiodesas t mosfet =0
Du,OFF
| follows.    |     |       |      |            |     |     |     |     |         | mosfet    |     | (cid:49)u    | )<0 |     |      |
| ----------- | --- | ----- | ---- | ---------- | --- | --- | --- | --- | ------- | --------- | --- | ------------ | --- | --- | ---- |
|             |     |       |      |            |     |     |     |     | t       | =t        | ,if | (t           |     |     |      |
|             | (   |       |      |            |     |     |     |     | trl,ON  |           | s   | sw           | s   |     |      |
|             | −u  | (t)·i | (t), | if i       | <0  |     |     |     |         |           |     |              |     |     |      |
| i igbt (t)= |     | sw    | m    | m          |     |     |     |     | t       | mosfet =t | ,if | (cid:49)u (t | )>0 |     |      |
| tru         |     |       |      |            |     |     |     |     | trl,OFF |           | s   | sw           | s   |     |      |
|             | 0,  |       |      | otherwise. |     |     |     |     |         |           |     |              |     |     |      |
|             |     |       |      |            |     |     |     |     | m       | o sf e t  |     |              |     |     |      |
|             | (   |       |      |            |     |     |     |     | t       | =0        |     |              |     |     | (21) |
|             | −u  | (t)·i | (t), |            | >0  |     |     |     | D       | l ,O F F  |     |              |     |     |      |
| i g bt      |     | sw    | m    | if i m     |     |     |     |     |         |           |     |              |     |     |      |
i (t)=
D u 0, The switching energies (E trON , E trOFF , and E DOFF ) are
othe rwise.
determinedattheswitchinginstancesusing2-Dlinearscat-
|     | ((cid:0) |     | (cid:1)·i |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1−u (t) (t), if i >0 tered interpolators, which are functions of the commutated
| igbt (t)= |     | sw  | m   |     | m   |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i trl
0, otherwise. currentsandthejunctiontemperature.Theswitchingpower
|      |          |     |           |     |     |     | losses | are | then calculated |     | from | the interpolated |     | energies | as  |
| ---- | -------- | --- | --------- | --- | --- | --- | ------ | --- | --------------- | --- | ---- | ---------------- | --- | -------- | --- |
|      | ((cid:0) |     | (cid:1)·i |     | <0  |     |        |     |                 |     |      |                  |     |          |     |
| igbt | 1−u      | sw  | (t) m (t) | ,if | i m |     |        |     |                 |     |      |                  |     |          |     |
i (t)= (17) follows,wheret step denotesthesimulationtimestep.
| Dl  | 0,  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
otherwise.
|     |     |     |     |     |     |     | P   |           | (t         | )=E |             |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     | tr(u,l)ON | tr(u,l),ON |     | tr (u , l)O |     |     |     |     |
w h e r e a sf or a Si C M OS FE T p o w er m o d u l e ,c o n s i d e r ing ze ro N
|     |     |     |     |     |     |     |     |     |     |     | (cid:16) |     |         |     | (cid:17)(cid:14) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | --- | ---------------- |
|     |     |     |     |     |     |     |     |     |     | ×   | i (t     | ),T | j,tr (t |     | ) t              |
de a d - t im e an d o w ing to th e th i rd q ua d r a n t o p e r a ti o n of th e m tr(u,l),ON tr(u,l),ON step
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 151743 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
| P          | (t          | )=E |            |     |     |     |                  |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| tr(u,l)OFF | tr(u,l),OFF |     | tr(u,l)OFF |     |     |     |                  |     |     |     |     |     |     |     |     |
|            |             |     | (cid:16)   |     |     |     | (cid:17)(cid:14) |     |     |     |     |     |     |     |     |
),T
|           |            |     | × i (t    |             | j,tr | (t          | ) t              |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------- | ----------- | ---- | ----------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|           |            |     | m         | tr(u,l),OFF |      | tr(u,l),OFF | step             |     |     |     |     |     |     |     |     |
| P         | (t         | )=E |           |             |      |             |                  |     |     |     |     |     |     |     |     |
| D(u,l)OFF | D(u,l),OFF |     | D(u,l)OFF |             |      |             |                  |     |     |     |     |     |     |     |     |
|           |            |     | (cid:16)  |             |      |             | (cid:17)(cid:14) |     |     |     |     |     |     |     |     |
|           |            |     | × i (t    |             | ),T  | (t          | ) t              |     |     |     |     |     |     |     |     |
|           |            |     | D         | D(u,l),OFF  | j,D  | D(u,l),OFF  | step             |     |     |     |     |     |     |     |     |
(22)
Theelectrothermalmodelofapowermoduleispresented
inFig.8,whichparametersareextractedfromthesemicon-
ductor’sdatasheet.ThecircuitnetworkutilizesaCauermodel
| that reflects |              | the physical | structure |              | of the | semiconductor, |           |     |     |     |     |     |     |     |     |
| ------------- | ------------ | ------------ | --------- | ------------ | ------ | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| thereby       | illustrating | the          | internal  | temperatures |        | of             | the layer |     |     |     |     |     |     |     |     |
sequence [57]. Since the loss calculations and the thermal FIGURE9. Magneticfluxdensityandelectricfielddistributionwith
model are interdependent, an initial junction temperature is fundamentalharmonicvoltageexcitationatPnom.
assumedtocalculatethelossesandtheresultingtemperature
fromtheselosses.Thistemperatureisthenfedbackintothe
|                                                         |     |     |     |     |     |     |     | resistance(R |     | )isextractedfromthecapacitor’sdatasheet. |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
| losscalculationuntilasteady-statetemperatureisachieved. |     |     |     |     |     |     |     |              |     | thC                                      |     |     |     |     |     |
In this study, we consider three vacuum-brazed cold plates T =T +R ·P (25)
|         |        |          |     |       |          |       |         |     |     | C   | amb | thC | Closs |     |     |
| ------- | ------ | -------- | --- | ----- | -------- | ----- | ------- | --- | --- | --- | --- | --- | ----- | --- | --- |
| per SST | module | provided | by  | [58], | with the | power | modules |     |     |     |     |     |       |     |     |
ofeachFB-VSCmountedonaseparateplate.Additionally, C. MFTLOSSESANDTHERMALMODEL
| for simplicity, |     | we assume | a constant |     | flow | rate of | 3.5 l/min, |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ---------- | --- | ---- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
MFTlossesareclassifiedintothreemaintypes:corelosses,
withasetpointof50◦C.
|     |     |     |     |     |     |     |     | winding | losses,   | and    | dielectric      | losses,       | with       | the           | core and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | --------------- | ------------- | ---------- | ------------- | -------- |
|     |     |     |     |     |     |     |     | winding | losses    | making | up              | the majority. | In         | this section, | the      |
|     |     |     |     |     |     |     |     | MFT     | of Module | 1      | is investigated |               | at nominal | power         | as a     |
referenceforthelossesassessment.
|     |     |     |     |     |     |     |     | Core | losses | are determined |     | using | Improved | Generalized |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | -------------- | --- | ----- | -------- | ----------- | --- |
Steinmetzequation[59],givenby
|     |     |     |     |     |     |     |     |     |     | Ns  | 1 Z T | (cid:12) dB   | (t) (cid:12) α     |      |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | ------------------ | ---- | ---- |
|     |     |     |     |     |     |     |     |     |     | X   |       | (cid:12) s    | (cid:12) (cid:49)B | β −α |      |
|     |     |     |     |     |     |     |     |     | P c | =   |       | kk i (cid:12) | (cid:12)           | dt   | (26) |
|     |     |     |     |     |     |     |     |     |     |     | T     | (cid:12) d t  | (cid:12)           | s    |      |
|     |     |     |     |     |     |     |     |     |     | s=1 | 0     |               |                    |      |      |
where,
FIGURE8. Powersemiconductorelectrothermalmodel.
1
|                                        |     |     |     |     |     |     |     |     | k   | =         |     |           |        |     | (27) |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------ | --- | ---- |
|                                        |     |     |     |     |     |     |     |     |     | i (2π)α−1 | R2π | |cos(θ)|α | 2β−αdθ |     |      |
| B. CAPACITORSLOSSESANDTHERMALMODELLING |     |     |     |     |     |     |     |     |     |           |     | 0         |        |     |      |
Thepowerlossesincapacitorscanbecalculatedasthesumof TheSteinmetzparametersk,α,andβ areusedalongwith
theproductsofthecapacitor’sRMScurrentanditsEquivalent
|     |     |     |     |     |     |     |     | the instantaneous |     | and | peak-to-peak |     | magnetic | flux | density, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------------ | --- | -------- | ---- | -------- |
SeriesResistance(ESR)ateachharmonicfrequency. B (t) and (cid:49)B , for each finite element s out of a total N .
|     |     |     |     |     |     |     |     | s               |     | s     |      |                  |     |             | s   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----- | ---- | ---------------- | --- | ----------- | --- |
|     |     | Nh  |     |     |     |     |     | A magnetostatic |     | model | with | open boundaries, |     | implemented |     |
X
= ω )·(|Irms(k ω )|)2 in FEMM, calculates the magnetic flux density amplitude
|     | P Closs |     | ESR(k | 0   |     | 0   | (23) |     |     |     |     |     |     |     |     |
| --- | ------- | --- | ----- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
cap B ˆ (hω ) for each harmonic h of the fundamental frequency
|     |     | k=1 |     |     |     |     |     | s   | 0   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ω
.Thisharmonicdatareconstructsthetime-domainwave-
| In (23), | N   | is the maximum |     | considered |     | harmonic | order, | 0    |         |       |        |          |             |     |          |
| -------- | --- | -------------- | --- | ---------- | --- | -------- | ------ | ---- | ------- | ----- | ------ | -------- | ----------- | --- | -------- |
|          | h   |                |     |            |     |          |        | form | used in | (26). | Fig. 9 | presents | the maximum |     | absolute |
ω
| 0 represents |     | the fundamental |     | angular | frequency, |     | whereas |       |        |          |      |         |      |                 |     |
| ------------ | --- | --------------- | --- | ------- | ---------- | --- | ------- | ----- | ------ | -------- | ---- | ------- | ---- | --------------- | --- |
|              |     |                 |     |         |            |     |         | value | of the | magnetic | flux | density | over | one fundamental |     |
ESRisdeterminedasfollows
periodforthewaveformsshowninFig.6.
tan(δC) The winding losses are computed by summing the losses
|     |     | ESR(ω)=R |     | +   | 0   |     | (24) |                                    |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | ---- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |          |     | s   | ωC  |     |      | foreachindividualharmonicasfollows |     |     |     |     |     |     |     |
Nh
w h e r e R s i s t h e s u m o f O h m i c re s is t a n c e s in si d e t h e c a pa c it o r , X
|     |     |     |     |     |     |     |     |     | P   | =   | R   | F   | (hω )I | (h ) 2 | (28) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ---- |
ta n (δ C )s i g n i fi e s t he d i el e ct r ic d is s i p a ti o n fa c to r , a n d ω i s t h e w(p,s) dc,w(p,s) r 0 w ,s)
| 0                              |     |     |     |     |     |     |     |     |     |     |     |     |     | (p  |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| operatingangularfrequency[51]. |     |     |     |     |     |     |     |     |     |     | h=1 |     |     |     |     |
Toestimatethehotspottemperatureofthecapacitor(T C ), where R w(p,s) represents the DC resistance of the winding,
thepowerlossesareusedinconjunctionwithasteady-state F is the resistance factor for round litz wires from the
r
electrothermal model, expressed in (25), where the thermal modifiedDowell’sequation,linkingDCtoACresistanceat
| 151744 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
(h)
eachharmonic[59],whileI denotestheRMSamplitude TABLE4. DABtestbenchparameters.
w(p,s)
ofsingle-sidedcurrentharmonics.
|                                                    | Dielectric | losses | depend | on the | frequency, |     | the RMS |     |     |     |     |     |     |
| -------------------------------------------------- | ---------- | ------ | ------ | ------ | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| amplitudeofthesingle-sidedelectricfieldharmonics(E |            |        |        |        |            |     | (h) ),  |     |     |     |     |     |     |
ins
| the                    | volume | of the    | dielectric | region                             | (Vol),       | and | the material |     |     |     |     |     |     |
| ---------------------- | ------ | --------- | ---------- | ---------------------------------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- |
| properties             |        | that vary | with       | frequency,                         | specifically |     | absolute     |     |     |     |     |     |     |
| electricpermittivity(ε |        |           |            | )andthelosscoefficient(tan(δins)). |              |     |              |     |     |     |     |     |     |
ins
Thisrelationshipisillustratedin(29)[60].
Nh
|     | X     | ZZZ |     |               |     |             |      |     |     |     |     |     |     |
| --- | ----- | --- | --- | ------------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
|     | =     |     | ε   | ·tan(δins)·hω |     | ·E (h)2dVol |      |     |     |     |     |     |     |
|     | P ins |     | ins |               | 0   |             | (29) |     |     |     |     |     |     |
ins
|     | h=1     |       | Vol            |        |     |          |         |     |     |     |     |     |     |
| --- | ------- | ----- | -------------- | ------ | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
|     | In this | work, | the dielectric | losses | are | assessed | using a |     |     |     |     |     |     |
currentflowmodelwithopenboundaryconditionsinFEMM, V. COMPONENTSLIFETIMEEVALUATION
withthecoreatgroundpotential(0V).Themodelisexcited Toassesstheimpactofdifferentstresscyclesoneachcom-
withfixedvoltageconditionsateachconductorcontour.The
|     |     |     |     |     |     |     |     | ponent within |     | the SST, | accelerated | life tests | should ideally |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ----------- | ---------- | -------------- |
resulting electric field distribution, as depicted in Fig. 9 for be performed on multiple samples of these components to
the reference MFT at the fundamental harmonic excitation estimate the time or cycles to failure under said stress.
(f
0 component of the waveforms presented in Fig. 4), along However,duetominormanufacturingvariations,accurately
withthecurrentdensityareextractedfromtheFEMMmodel predictingtheprecisefailuretimeofanindividualdeviceis
| and | are used | to  | calculate | the power | loss | density | in the |              |            |     |            |            |              |
| --- | -------- | --- | --------- | --------- | ---- | ------- | ------ | ------------ | ---------- | --- | ---------- | ---------- | ------------ |
|     |          |     |           |           |      |         |        | impractical. | Therefore, |     | it is more | meaningful | to determine |
insulatingmaterial,representingthedielectriclosses. the failure probability of each device. Consequently, for
The steady-state thermal model utilized in this study is the wear-out failure in this study we employ Monte Carlo
basedontheadaptiveMFTthermalmodelpresentedin[61],
|     |     |     |     |     |     |     |     | analysis | to account | for | uncertainties | in  | both the lifetime |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------------- | --- | ----------------- |
whichisdevisedincludingconduction,convection,andradi- equation parameters as well as the system measurements.
| ation | mechanisms. |     | This | thermal model, |     | depicted | in Fig. 10, |                  |     |     |          |                    |            |
| ----- | ----------- | --- | ---- | -------------- | --- | -------- | ----------- | ---------------- | --- | --- | -------- | ------------------ | ---------- |
|       |             |     |      |                |     |          |             | This methodology |     | is  | detailed | in the reliability | estimation |
was bench-marked against a heat run test applied to a DAB studies described in [36], [42], and [62]. The total damage
converter test bench in [61], operating with conventional experiencedbythedeviceduetovariousstressesthroughout
| rectangular |                  | modulation |          | with the      | parameters     |            | described in |     |     |     |     |     |     |
| ----------- | ---------------- | ---------- | -------- | ------------- | -------------- | ---------- | ------------ | --- | --- | --- | --- | --- | --- |
| Table       | 4.The            | schematic  |          | of the tested | DAB            | converter, | along        |     |     |     |     |     |     |
| with        | the experimental |            |          | setup and     | the associated |            | MFT, are     |     |     |     |     |     |     |
| presented   |                  | in Fig.    | 11. This | test serves   | to             | validate   | the MFT      |     |     |     |     |     |     |
lossescalculationswhicharetranslatedintoheatinjectionsto
theircorrespondingnodesemulatedbycurrentsources.The
resultsoftheheat-runshowedamaximumerroraround16%
atalltestedoperatingconditions[61].
FIGURE10. Steadystatethermalnetworkofshell-typeMFT. FIGURE11. MFTheatruntestexperimentalsetup.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 151745 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
FIGURE12. SSTmissionprofilebasedlifetimeestimationalgorithm.
the load profile is first calculated. These different stresses atthisstage,thisstudyassumesaconstantinputvoltagetothe
are then converted into an equivalent single stress that SSTandasteadyambienttemperatureof27°Cforsimplicity.
would produce the same calculated total damage. Next, Once the temperature profile for each component is
uncertainties in the lifetime equation parameters are taken established, the subsequent steps for calculating component
intoaccount,consideringtheequivalentsinglestressvalues, reliability are detailed in the following subsections. The
throughtheMonteCarloanalysis.Theresultsofthisanalysis reliabilityoftheSSTdependsoneachindividualcomponent;
are subsequently used to fit the pdf of the Weibull function any failure (eg. switch, capacitor, or MFT) can lead to
presentedin(7).WhileacasestudyofaPVinverterin[63] complete converter failure in the absence of redundant
demonstratedthatMonteCarloreliabilityassessmentresults modules. Therefore, the total SST reliability, accounting
generallyconvergewhenthenumberofsimulationsreaches for both wear-out and random failures, is expressed as the
1000,thisworksetsthesamplesizeto10000.Thisnumber, product of each component’s reliability, as illustrated in
initially introduced in a degradation assessment of IGBTs Fig.12.
by[7],isconsideredsufficientlylargetoensureconvergence
regardlessoftheparametervariationrange.Thesimulations A. SEMICONDUCTORSRELIABILITYESTIMATION
in this study were conducted on a Windows 10 Pro system The number of cycles to failure (N ) of semiconductors are
f
withan11thGenIntel(R)Core(TM)i7-11850H@2.50GHz influenced by the specific lifetime model applied. Whereas
processor,witheachMonteCarlorunofthespecifiedsample the lifetime model and its parameters are specific to the
sizetakingnomorethan3seconds. powermodulespackagingtechnology.Whileanidealmodel
Thecompleteprocedureforcalculatingthemissionprofile would reflect the actual testing conditions encountered in
based SST reliability, as illustrated in Fig. 12, involves thefield,thisisoftenimpracticalduetothesignificanttime
evaluating system behavior at various operating points up required for such testing. Therefore, as this study employs
to P rated and determining the losses and temperatures of thestandardmulti-layerstructurepowermodules,weutilize
eachdeviceatthesecorrespondingpoints.This‘‘temperature thewidelyacceptedCIPSmodel[8],detailedin(30),which
mapping’’methodsimplifiestheanalysisbydirectlylinking is devised through accelerated lifetime testing of multiple
the thermal response of components to a specific mission IGBTs,constitutingsevendifferentbondingtechnologiesand
profile. While seasonal ambient temperature variations and sevendifferentpackaging.Thisempiricalequationaddresses
different AC input voltage distortions (such as voltage thekeyfailuremechanismsinIGBTs:bond-wirelift-offand
unbalance,harmonics,andDCoffsets,etc.)canbeconsidered solderjointfatigue[7],[42].A5%to20%increaseinforward
151746 VOLUME13,2025

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
voltage drop typically signals bond-wire lift-off, whereas a
20%to50%riseinthermalresistancebetweenthechipand
heatsink indicates solder fatigue. The latter is characterized
by crack propagation within the solder layers [64]. Short
temperature cycles (t ) occurring over just seconds or
on
less mainly contribute to bond wire degradation [65], [66].
Incontrast,longert contributemoretothebaseplatesolder
on
degradation.Thus,itisnecessarytoincludetheeffectsofthe
temperature cycle length on the number of cycles to failure FIGURE13. AveragedFITratesofsemiconductorswitchesnormalizedto
chiparea[71],[72],[73],[74],[75].
which is modelled as presented in (31) [65], [66]. As the
sampledloaddatainthisstudycontributetolongtemperature
cycles,solderjointfatigueareconsideredthemoreprominent as well as variations in each of T j,min and (cid:49)T j resulting
failuremechanism.
fromdeviationsoftheon-statevoltageofthesemiconductor
N =A·((cid:49)T) −β 1exp (cid:18) β 2 (cid:19) ·t β 3 (30) calculatedsimilarlyaspresentedin[7].
f j T j,min +273 on Tocalculatetherandomfailurerateofthesemiconductors,
 (6) is employed. However, base failure rates, also known as
2.25, t ≤0.1s
N f (t on ) =
(cid:18)
t on (cid:19)−0.3 , 0
o
.
n
1s≤t ≤60s (31)
F
in
ai
t
l
h
u
e
re
da
in
ta
T
sh
im
ee
e
ts
(
.
F
T
I
h
T
e
)
re
ra
fo
te
r
s
e
,
,
a
a
r
n
e
a
o
v
f
e
te
ra
n
g
n
e
o
o
t
f
re
th
a
e
di
f
l
a
y
il
a
u
v
re
ail
r
a
a
b
te
le
s
N f (1.5) 0.3 1
3
.5 , t on ≥60
o
s
n r
s
e
u
p
p
o
p
r
l
t
i
e
e
d
rs
i
a
n
cr
t
o
h
s
e
s v
li
a
te
ri
r
o
a
u
tu
s
re
rat
a
e
n
d
d
vo
b
l
y
tag
d
e
if
s
fe
w
re
a
n
s
t
c
s
a
e
lc
m
u
i
l
c
a
o
te
n
d
du
[7
ct
1
o
]
r
,
In (30), (cid:49)T is the fluctuation in junction temperature, [72],[73],[74],[75].TheseaverageFITratesarepresented
j
T j,min is the minimum junction temperature, whereas A, β 1 , in Fig. 13, serving as the base failure rate which already
β ,andβ arethelifetimeequationcoefficients[8]. accounts for the effects of electric stress. Additionally,
2 3
to incorporate the impact of thermal stress on the random
Although initially developed for Si-IGBTs, the CIPS
failurerate,thefollowingequationisutilized,sourcedfrom
model has also been evaluated for SiC-MOSFETs [9],
MIL-HDBK 217 [41], where, B represents a constant
[10], given the similarities in their failure modes. In SiC- T
that corresponds to the activation energy divided by the
MOSFETs,thechipdieissolderedtothecopperbase,with
Boltzmannconstant.
common failure location in standard packaging involving
(cid:18) (cid:18) (cid:19)(cid:19)
1 1
wire bonding solder and die attach. These components π =exp −B − (33)
T T
experience degradation as a result of temperature cycling T j 298
and mechanical stress [11], [12], [67]. The CIPS model
in this paper is selected for SiC MOSFETS based on
B. CAPACITORRELIABILITYESTIMATION
the selected power modules and their dominant failure
The wear out failure mode of film capacitors is determined
mechanisms. Notably, with the development of advanced
whenoneofitselectricparameters,namelyCapacitance(C),
packaging technologies, such as sintered chip modules like
Equivalent Series Resistance (ESR), dielectric loss factor
the SKiM [68], traditional soldering techniques have been (tan(δC)),leakagecurrent,orinsulationresistance,driftsover
0
replacedbynewermethods,suchassilverdiffusionbonding.
a specific threshold from its initial value [4]. These drifts
These modules failure modes primarily exhibit bond wire
are mainly triggered through breakdowns of the dielectric
lift-off and heel cracking. For such cases, the Semikron
material from continuous electrical and thermal stresses.
lifetime model proposed in [69] offers a more accurate
The state-of-the-art lifetime equation for film capacitors
degradationassessment.
accountingforthesefailuremechanismsandrelatinglifetime
To analyze the Accumulated Damage (AD) of the semi-
inhourstoappliedvoltageandhotspottemperatureisgiven
conductors, this paper applies Miner’s rule based on the
by
assumption of linear cumulative damage and the indepen-
denceofsemiconductor’sdamagefromtheorderofthestress L =L 0
(cid:18) V (cid:19)−n1
2
T0
n
−
2
T
(34)
cycles[70].TheADiscalculatedasthesumoftheratiosof V 0
thenumberofcyclesexperiencedbythesemiconductorunder where n and n are the voltage stress exponent and
1 2
eachspecificstresstype(n k )tothecorrespondingnumberof the temperature stress constant, respectively. L, V, and
cycles to failure for that stress type (N f,k ), where k denotes T are the lifetime, voltage, and temperature in Kelvin
differentstresscycletypes. under the use condition, respectively; whereas, L , V , and
0 0
AD= X n k (32) T 0 are the lifetime, voltage, and temperature in Kelvin at
N f,k the test condition, respectively. Following the ‘‘10-Kelvin-
k rule’’ of the Arrhenius law, n equals 10 for the analyzed
2
The uncertainties in the semiconductors lifetime model capacitors[62].Typically,forfilmcapacitorsn issetto9[4],
1
include, the lifetime equation parameters A, β , β , and β , [5],however,itisessentialtonotethatn isdependentonthe
1 2 3 1
VOLUME13,2025 151747

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
| voltagestresslevel[4],[6].Incaseoflowvoltagestress,n |     |     |     |     |     |     | is  |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
adjustedto1,suchthatthevoltagestressisdirectlyexpressed
astheratioofusevoltagetotestedvoltage.
| The | consumed | lifetime |     | of a capacitor | can | be calculated |     |     |     |     |     |     |     |     |
| --- | -------- | -------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
using
|     |     | N   |     | N         |             |         |      |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | ----------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     |     | X   | t i | X         | t i         |         |      |     |     |     |     |     |     |     |
|     | CL  | =   | =   |           |             |         | (35) |     |     |     |     |     |     |     |
|     |     |     | L   | (cid:16)  | (cid:17)−n1 | T0 − Ti |      |     |     |     |     |     |     |     |
|     |     |     | i   | V         |             |         |      |     |     |     |     |     |     |     |
|     |     | i=1 |     | i=1 L 0 i | 2           | n 2     |      |     |     |     |     |     |     |     |
V 0
| where | t is | the duration |     | of operation | with | temperature |     |     |     |     |     |     |     |     |
| ----- | ---- | ------------ | --- | ------------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
i
| T i and       | voltage | V,             | i at stress | point        | i. The         | lifetime | of      |     |     |     |     |     |     |     |
| ------------- | ------- | -------------- | ----------- | ------------ | -------------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| the capacitor |         | can be         | calculated  | by           | the reciprocal |          | of CL.  |     |     |     |     |     |     |     |
| The failure   |         | distribution   | function    | is           | obtained       | in a     | similar |     |     |     |     |     |     |     |
| manner        | to the  | semiconductors |             | by deploying |                | Monte    | Carlo   |     |     |     |     |     |     |     |
analysis.Followingtheapproachpresentedin[5],twotypes
|                  |     |     |             |     |          |               |     | FIGURE14. | MFTinsulationdivisionintomultipledielectricregions |     |     |     |     |     |
| ---------------- | --- | --- | ----------- | --- | -------- | ------------- | --- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- |
| of uncertainties |     | are | considered: | 1)  | lifetime | model-related |     |           |                                                    |     |     |     |     |     |
(adaptedfrom[33]).
| parameter,n |     | andn | ,and2)variationsduetomanufacturing |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 2
| processes,L |     | andT |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|             | 0   |      | 0 . |     |     |     |     |     |     |     |     |     |     |     |
(λ
For random failures, the base failure rates ) of the associated with PD issues, analyzed through exponential
b
| capacitors | and | the | corresponding | effects |     | of the | hotspot |            |       |            |       |                    |     |        |
| ---------- | --- | --- | ------------- | ------- | --- | ------ | ------- | ---------- | ----- | ---------- | ----- | ------------------ | --- | ------ |
|            |     |     |               |         |     |        |         | or inverse | power | law models | [78]. | In solid-insulated |     | trans- |
temperature and the operating voltage are obtained directly formers, PD is amplified by voids in the insulation that
from the capacitors’ respective datasheets. The random can provide discharge pathways, increasing failure risk.
failurerateiscalculatedastheaverageofthevariousFITrates
Inaddition,variationsinthethermalexpansioncoefficientsof
correspondingtoeachloadpoint. adjacentmaterialscancausecracksordelamination,further
|     |     |     |     |     |     |     |     | elevating | PD activity | [79]. | Thus, | the characteristics |     | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ----- | ----- | ------------------- | --- | ------ |
C. MFTRELIABILITYESTIMATION voids within the insulation significantly affect PD activity,
Specific failure data on MFTs is limited, however, research as it determines the Partial Discharge Inception Voltage
ondistributiontransformerscanbeusedtohighlightsimilar (PDIV),thethresholdforPDinitiation.FrequentPDevents
stress factors. Common points of failure in distribution reduceinsulationlongevity,withthePDIVmarkingacritical
transformers include bushings, internal connections, and stressthresholdthattriggerselectricalaging.
inter-turn and winding insulation breakdown [76]. The The reliability model for MFTs is designed as a series
structural similarities between distribution transformers and network that combines the reliabilities of all the dielectric
MFTs, coupled with the adverse effects of high frequencies regions,illustratedasparasiticcapacitorsintheMTLmodel.
on insulation degradation [32], [33], [34], [35], suggest The lifetime model for each region, presented in (36), was
that insulation failures are a predominant concern for devisedforinsulatingmaterialsin[80]andfurthervalidated
MFTs. As insulation is subjected to thermal, electrical, in [81] and forms the basis of the capacitor lifetime model,
and mechanical stresses, failures may arise from material which is simplified in (34) [4]. In (36), E represents the
a
| degradation |     | over time | or through | faults | such | as overvoltage |     |            |        |       |            |           |           |     |
| ----------- | --- | --------- | ---------- | ------ | ---- | -------------- | --- | ---------- | ------ | ----- | ---------- | --------- | --------- | --- |
|             |     |           |            |        |      |                |     | activation | energy | while | K b is the | Boltzmann | constant. | The |
orshortcircuits[76].High-frequencystressescanexacerbate consumedlifetimeforeachdielectricregioncanbecalculated
dielectricheatingandPartialDischarge(PD),increasingthe similarlytotheapproachusedin(35).
risk of insulation breakdown [32], [33], [60]. Therefore, (cid:18) (cid:19)−n (cid:20)(cid:18) (cid:19)(cid:18) (cid:19)(cid:21)
|     |     |     |     |     |     |     |     |     |     | V   | E   | a 1 | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a thorough examination of these failure mechanisms is L =L exp − (36)
0
essentialforaccuratelyestimatingthelifespanofMFTs. V 0 K B T T 0
The MFT reliability model in this study is based on Thermal stresses on the MFT insulating material are
the Multiconductor Transmission Line (MTL) principles derived from the nodes of the electrothermal model repre-
|           |     |           |        |            |     |                 |     | senting the | stressed | regions. | Whereas | regarding |     | the electric |
| --------- | --- | --------- | ------ | ---------- | --- | --------------- | --- | ----------- | -------- | -------- | ------- | --------- | --- | ------------ |
| presented | in  | [33]. MTL | models | discretize |     | electromagnetic |     |             |          |          |         |           |     |              |
equations of a coupled network that captures mutual stress, the voltage potentials of each winding turn are first
conductor interactions. Within MFTs, MTL capacitors rep- calculatedwithreferencetoground.InanISOPconfiguration
resentenergystoredininsulations,influencingperformance of modules, the first module of each phase experiences the
through high-frequency losses, PD, and insulation issues. highest voltage stresses. As one moves down the module,
eachsubsequentmodulehasitsinputvoltagepotentialwith
| An example |     | of the | MTL | parasitic capacitance |     | model | for a |     |     |     |     |     |     |     |
| ---------- | --- | ------ | --- | --------------------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
(k)
3:3turnratioMFTisshowninFig.14. respect to ground reduced by v . Regarding the MFT
m
Capacitor and insulation lifetime models share similar insulation,theMVsidewindingterminals(v (k) andv (k) ,
|     |     |     |     |     |     |     |     |     |     |     |     |     | mftp,i | mftp,o |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
dependencies on electrical and thermal stresses, primarily asdenotedinFig.2aredeterminedbythedifferencebetween
due to dielectric degradation, which leads to punctures the module’s AC input voltage referenced to ground and
and increased losses [4], [77]. Insulation failure is often the voltage drops across the switches along the path to the
| 151748 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
| FIGURE15. | Time-domainwaveformsofMFTprimarywindinginput |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
voltagepotentialstogroundformodules1,6,and12. FIGURE16. Paschen’scurveatambientpressureandtemperature(Vb,v
ispeakvoltage).
| MFT as | described | in 13 | and 14.   | Fig.    | 15 shows | the time  |     |     |     |     |
| ------ | --------- | ----- | --------- | ------- | -------- | --------- | --- | --- | --- | --- |
| domain | waveforms | of    | v (k) for | modules | 1, 6,    | and 12 of |     |     |     |     |
mftp,i
| a single     | phase for | the studied | SST. | The   | voltage   | harmonics |     |     |     |     |
| ------------ | --------- | ----------- | ---- | ----- | --------- | --------- | --- | --- | --- | --- |
| of the first | module    | display     | the  | 50 Hz | component | of the    |     |     |     |     |
gridvoltagealongwithhigh-frequencyharmonicsassociated
| with the           | converter’s | switching | frequency.    |       | Moving    | down the    |     |     |     |     |
| ------------------ | ----------- | --------- | ------------- | ----- | --------- | ----------- | --- | --- | --- | --- |
| modules            | of the      | phase,    | the dominance |       | of the    | first-order |     |     |     |     |
| harmonic           | (i.e.,      | 50 Hz)    | diminishes,   | while | the       | amplitudes  |     |     |     |     |
| of the converter’s |             | switching | frequency     |       | harmonics | become      |     |     |     |     |
relativelymorepronounced.Hence,inordertofacilitatethe
| manufacturing   | and | maintenance |               | of the MFT, | the   | MFTs in |           |                                                 |     |     |
| --------------- | --- | ----------- | ------------- | ----------- | ----- | ------- | --------- | ----------------------------------------------- | --- | --- |
|                 |     |             |               |             |       |         | FIGURE17. | Illustrationofthepossiblevoidscompositioninside |     |     |
| ISOP-configured |     | SSTs        | are typically | designed    | based | on the  |           |                                                 |     |     |
solid-insulatedMFT(nottoscale).
| module | experiencing | highest | insulation |     | stress (module | 1). |     |     |     |     |
| ------ | ------------ | ------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- |
Withknownterminalvoltages,individualwireturnvoltages
areestimatedassumingauniformvoltagegradientacrossthe Fig.16showsPaschen’scurveforanairgapatatmospheric
adjacentconductorsasdescribedinSectionIII-C. pressure and room temperature, indicating three conditions:
In(36),V representstheelectricstressthresholdvoltage, 1) No PD activity below the curve (e.g., k ), 2) PD activity
|     | 0   |     |     |     |     |     |     |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
indicatingthePDIVoftheinsulatingmaterial.ThePDIVesti- withintheshadedregion(e.g.,k 2 ),and3)Pointsonthecurve
mationutilizesthemodifiedPaschen’slaw,presentedin(37), (e.g.,k )representingthePDIV.Breakdownvoltagesharply
3
whichincorporatesatemperaturecorrectionfactor[82].This increases at relatively very small void lengths (d ) due to
v
law describes the breakdown voltage (V b,v ) as a function of insufficientgasmolecules,whileitriseslinearlyathigherd v
temperature(T)forspecificgasandelectrodematerialsunder duetoweakerelectricfields[85].
uniformelectricfieldconditions,anditisdependentongas Identifying potential air gap locations within the
property-specific parameters (A, B), gas pressure (P), and solid-insulated MFT is crucial; these can form both within
voidlength(d ),asfollows theinsulatingmaterialandbetweenadjacentwires,asshown
v
(cid:16) (cid:17) in Fig. 17. As high temperature is usually correlated to
|     |     |     | B·P· | 273+25    |     |      |                                                  |     |     |     |
| --- | --- | --- | ---- | --------- | --- | ---- | ------------------------------------------------ | --- | --- | --- |
|     |     |     |      | 273+T     |     |      | lowerPDIVs,wecanusethePaschen’scurveatthehighest |     |     |     |
|     |     | =   |      |           | ·d  |      |                                                  |     |     |     |
|     | V   | b,v |      | (cid:17)! | v   | (37) |                                                  |     |     |     |
(cid:16) 2 7 3 + 2 5 e x p e ct e d te m p e r at ur e t o e st im a te t h e m in i m a l ga p ( d v ,m i n )
|     |     |     | A·P·dv · | +   |     |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
ln 2 7 3 T li k e ly t o in i tia t e P D a c t ivi ty , as p re s e nt ed i n F i g. 1 6. O n t h e
k
|     |     |     |     |     |     |     | other hand, | following | the approach presented | in [86], the |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---------------------- | ------------ |
wherek isaconstantcalculatedas maximum length of a possible air gap (d v,max ) in this work
|     |     |     |          |            |     |     | is defined | as twice the | wire radius, applicable | to both void |
| --- | --- | --- | -------- | ---------- | --- | --- | ---------- | ------------ | ----------------------- | ------------ |
|     |     |     | (cid:18) | 1 (cid:19) |     |     |            |              |                         |              |
=ln 1+
|     |     | k   |     |     |     | (38) | types. |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------ | --- | --- | --- |
γ
Oncetherangeofpossiblevoidlengthsisidentified,and
Thecoefficientγ representsTownsend’ssecondaryemission knowingtheinsulatinglayerlengththroughwhichtheelectric
| coefficient, | indicating |         | the average | number   | of       | electrons |     |     |     |     |
| ------------ | ---------- | ------- | ----------- | -------- | -------- | --------- | --- | --- | --- | --- |
| released     | from the   | cathode | per         | incident | positive | ion [82], |     |     |     |     |
TABLE5. Voltageexponentialtermgatheredfromtheliterature.
γ
| [83], [84]. | The | temperature | variation | of  | for | the trans- |     |     |     |     |
| ----------- | --- | ----------- | --------- | --- | --- | ---------- | --- | --- | --- | --- |
former’sinsulatingmaterialsissourcedfrom[82]forepoxy
| and [83] | for polyimide |       | (PI). In addition, |               | this study  | assumes |     |     |     |     |
| -------- | ------------- | ----- | ------------------ | ------------- | ----------- | ------- | --- | --- | --- | --- |
| the gas  | in the        | voids | is air             | at a standard | atmospheric |         |     |     |     |     |
| pressure | (P=101,325    | Pa),  | with               | A = 11.25     | Pa          | m−1 and |     |     |     |     |
B=273.75VPa−1m−1[84].
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     | 151749 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
fieldlinespass,weapplythedielectricboundaryconditionto Hence,therandomfailurerate(λ )whichrepresentsthemean
r
calculatethemaximumvoltageacrossthevoidsofdifferent oftheinstantaneousfailureratecalculatedateachoperating
lengthsasfollows point i across n total steps in the simulation, is determined
using(40)forthestudiedinsulationclass[41].
|     |     |      | (cid:18) d (cid:19) | (cid:18) d | d     | (cid:19) |     |     |     |     |     |     |     |     |
| --- | --- | ---- | ------------------- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | =V · | v /                 | v          | + ins | ,        |     |     |     |     |     |     |     |     |
V void o p
|     |     |      | ε r,      | ε ,v  | ε ,        |     |      |     |     |     | N   | (cid:18) | (cid:19)10 |      |
| --- | --- | ---- | --------- | ----- | ---------- | --- | ---- | --- | --- | --- | --- | -------- | ---------- | ---- |
|     |     |      | v         | r     | r i n s    |     |      |     |     | 1   | X   | T hsi    | + 273      |      |
|     |     | ∈R   |           |       |            |     |      |     | λ   | =   | λ   | exp      |            | (40) |
|     |     | {d v | | d v,min | ≤ d v | ≤d v , m a | x } | (39) |     | r   |     | b   |          |            |      |
|     |     |      |           |       |            |     |      |     |     | N   |     |          | 4 09       |      |
i=1
| where d | ins is the | length | of the | electric | field | path between |     |     |     |     |     |     |     |     |
| ------- | ---------- | ------ | ------ | -------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
the active electrodes, ε r,v and ε r,ins are the permittivities of VI. SSTCONSUMEDLIFETIME:CASESTUDIES
the inner gas and the surrounding insulation, respectively, The distribution of losses within the system is critical
and V op denotes the maximum operating voltage applied to understanding its overall performance and reliability.
by the electrodes. By comparing the calculated voltages The overall theoretical efficiency curve of the designed
|           |           |        |     |            |     |           |     | SST, considering |     | the | investigated | system | parameters | and |
| --------- | --------- | ------ | --- | ---------- | --- | --------- | --- | ---------------- | --- | --- | ------------ | ------ | ---------- | --- |
| of d v to | Paschen’s | curve, | we  | can assess | the | potential | for |                  |     |     |              |        |            |     |
PD activity. If the voltages do not intersect the Paschen components as described in Section IV, is presented in
curve,itindicatesnoelectricstressundernormaloperation. Fig. 18 and the combined losses of each conversion stage
|             |     |              |           |     |         |          |     | per module | are | presented |     | in Table | 6. It is important | to  |
| ----------- | --- | ------------ | --------- | --- | ------- | -------- | --- | ---------- | --- | --------- | --- | -------- | ------------------ | --- |
| Conversely, | an  | intersection | signifies |     | that PD | activity | is  |            |     |           |     |          |                    |     |
possible, in which case the d representing the highest ratio note that the losses and efficiencies reported are derived
v
ofV /PDIVisconsidered,asitrepresentstheworst-case from suppliers data and have not been validated through
void
scenariocorrespondingtothelowestPDIV.Whenthevoltage laboratory testing. Additionally, the losses do not account
stressisbelowthePDIV,theexponentialcomponentnin(36) for cooling equipment, power supplies, or other auxiliary
|           |         |         |              |     |                 |     |        | components | required |     | for the | SST operation. | Furthermore, |     |
| --------- | ------- | ------- | ------------ | --- | --------------- | --- | ------ | ---------- | -------- | --- | ------- | -------------- | ------------ | --- |
| is set to | zero to | neglect | the electric |     | stress effects. |     | If the |            |          |     |         |                |              |     |
voltage exceeds the PDIV, n is assigned a value of 2.55, it is assumed that every instance of Zero Voltage Switching
representingtheaveragefromTable5whichpresentsvoltage (ZVS)andZeroCurrentSwitching(ZCS)ofthetrapezoidal
exponent stress factors based on voltage-lifetime data from operation of the DAB converter incurs zero power losses.
existing literature. A higher n reflects a greater impact of However,thisassumptionisasimplification,asitiscommon
|     |     |     |     |     |     |     |     | to observe | low | (but | non-zero) | turn-on | losses that | increase |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | --------- | ------- | ----------- | -------- |
electricstressoninsulationdegradation.However,insulation
inMFTsistypicallydesignedwithgeneroussafetymargins, at higher frequencies during ZVS operation. Whereas ZCS
ensuringoperationalvoltagesstaywellbelowthematerial’s lossesdependonthetransformermagnetizingcurrent,which
breakdown strength. This justifies using a low n, consistent mayalsoresultinhard-switchingconditions.
with standard capacitor lifetime models under low electric Thepowerlossresultsindicatethattheefficiencydropis
primarilyduetotheAFEC,followedbytheDABconverter,
stress[4].
To estimate the MFT wear-out pdf, two types of uncer- the MFT, and finally the capacitors. The zero power losses
taintiesareaddressedintheMonteCarloanalysis.Thefirst of the SiC diodes in the DAB converter are attributed to
involvesparametersrelatedtothelifetimemodel:nvariesby
22%,withitslowerboundmatchingtheminimumvaluefrom
| Table 5,      | while E | a and          | L 0 both | vary by     | 5%. The | second       | are |     |     |     |     |     |     |     |
| ------------- | ------- | -------------- | -------- | ----------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| uncertainties | in      | estimated      | values,  | including   | the     | temperature  |     |     |     |     |     |     |     |     |
| which varies  | by      | 16% reflecting |          | the maximum |         | error margin |     |     |     |     |     |     |     |     |
oftheelectrothermalmodel,Townsend’ssecondaryemission
| coefficient | (γ) | varying | by 5%, | and | the void | length | (d ) |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ------ | --- | -------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
v
whichvariesbetweenthepredefinedminimumandmaximum
values.
| For the | MFT | random | failure | computation, |     | the | base |     |     |     |     |     |     |     |
| ------- | --- | ------ | ------- | ------------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
(λ
| failure rate      | b   | ) is typically  |     | sourced | from         | the manufac- |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------- | --- | ------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| turer’s datasheet |     | or approximated |     | from    | MIL-HDBK-217 |              |     |     |     |     |     |     |     |     |
handbook[41].Theprimarystressfactor,asoutlinedinMIL-
DesignedSSTefficiency(η)vs.power.
| HDBK-217, | is  | the hotspot | temperature |     | (T hs ) | of the | MFT. | FIGURE18. |     |     |     |     |     |     |
| --------- | --- | ----------- | ----------- | --- | ------- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- |
TABLE6. SSTmoduleslossesdistributionatratedpower.
| 151750 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
TABLE7. Lifetimemodelsparametersandvariations[4],[5],[7],[8],[9],
[35],[51],[94],[95].
| FIGURE19.         | Investigatedloadprofilessampledhourly. |                 |          |               |           |             |     |     |     |     |
| ----------------- | -------------------------------------- | --------------- | -------- | ------------- | --------- | ----------- | --- | --- | --- | --- |
| reverse current   | flow                                   | through         | the      | MOSFET        | channel,  | along       |     |     |     |     |
| with the          | assumption                             | of              | lossless | ZVS and       | ZCS       | conditions. |     |     |     |     |
| This is justified |                                        | as no dead-time |          | is considered | for       | the sake    |     |     |     |     |
| of simplicity.    | While                                  | the             | losses   | of each       | converter | remain      |     |     |     |     |
consistentacrossthemodules,theeffectsofdielectriclosses
ontheMFTvaryduetothedifferentvoltagepotentialsacross
| each module’s | insulation, |     | as previously |     | discussed. | Notably, |     |     |     |     |
| ------------- | ----------- | --- | ------------- | --- | ---------- | -------- | --- | --- | --- | --- |
thedifferenceinMFTlossesbetweenModules1and12is≈
2.3W,whichisinsignificantcomparedtothecombinedcore
| and winding       | losses,   | which | are        | orders of     | magnitude  | higher |     |     |     |     |
| ----------------- | --------- | ----- | ---------- | ------------- | ---------- | ------ | --- | --- | --- | --- |
| for the presented |           | MFT   | design.    | Nevertheless, | these      | losses |     |     |     |     |
| contribute        | to direct | heat  | generation | in the        | insulating | mate-  |     |     |     |     |
rials, potentially influencing aging. Therefore, this section Forthecomponentswear-outinvestigation,theparameters
investigatestheimpactoftheselossesonthereliabilityofthe associated with the lifetime equations and the variations
MFT, alongside a comprehensive reliability analysis of the applied in the Monte Carlo analysis are detailed in Table 7.
SST,bothwithandwithoutconsideringtheMFT.
|     |     |     |     |     |     |     | All parameters | subjected | to variation | are represented using |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | ------------ | --------------------- |
Two test cases, each associated with a distinct mission normaldistributionfunctionswitha95%confidenceinterval,
profile, are used to assess the SST lifetime. The first with the exception of d . As the average expected value
v
load profile in Fig. 19 represents an Electric Vehicle (EV) for d v is not specified in this research, its variation is
station charging load sourced from [92], while the second insteadmodeledusingauniformdistributionthatspansfrom
profile depicts a data center load reported in [93], both of d to d . Additionally, the deviations in the MFTs’
|     |     |     |     |     |     |     | v,min v,max |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
whicharesampledhourly.Toaccommodateloadfluctuations V parameter representing the PDIV are taken into account
0
throughouttheyear,seasonalvariationsareappliedaswellas throughthevariationsofd andγ.Consequently,adifferent
v
±
up to 20% of the maximum load is randomly assignedat PDIVisestimatedforeachsampleofdielectricregionwithin
differentinstances.Thechoiceofthesetwoloadsisbasedon eachMFTintheMonteCarloanalysis.
theirdifferingannualanddailypeakloadsaswellastheirload The results of the Monte Carlo analysis yield the failure
durations. Moreover, reliability is significantly prioritized probability density function f(t) for each component, from
for data centers in comparison to EV charging loads due which the cumulative probability of failure over time, F(t),
to the common high availability requirements, therefore is derived. Fig. 20 illustrates the aggregated reliability
assessing different reliability demands. It’s important to (1−F(t)) of the various component technologies within
highlight that the sampling rate is low enough to ignore the Module 1, analyzed under the two load profiles. AFE
tr
transientbehaviorbetweensteady-statepointsoftheMFT’s represents the combined reliability of all the Si-transistors
temperature, thereby confirming the appropriateness of the in the AFEC, while AFE denotes the combined reliability
D
electrothermalmodelfortheloadprofilebeinganalyzed. of the Si-diodes. Similarly, DC p and DC s correspond to the
VOLUME13,2025 151751

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
| FIGURE20. | Module1componentsReliabilityforeachmissionprofiles. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
primaryandsecondarysideFB-VSCsoftheisolatedDC-DC
| converter, | respectively,                                   |     | utilizing | SiC technologies. |     | Whereas |     |     |     |     |     |     |     |     |
| ---------- | ----------------------------------------------- | --- | --------- | ----------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| C andC     | indicatethecombinedreliabilitiesofthecapacitors |     |           |                   |     |         |     |     |     |     |     |     |     |     |
p s
formingtheprimaryandsecondaryDClinks,respectively.
| It is anticipated |                 | that       | the devices | within | the        | data    | center |     |     |     |     |     |     |     |
| ----------------- | --------------- | ---------- | ----------- | ------ | ---------- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| module            | will experience |            | greater     | wear   | than those | under   | the    |     |     |     |     |     |     |     |
| EV load           | due to          | the higher | continuous  |        | power      | demand. | The    |     |     |     |     |     |     |     |
identifiedhighpowerlosscomponentsinTable6,particularly
| the AFEC       | transistors | and     | diodes, | the SiC  | transistors |      | of the  |     |     |     |     |     |     |     |
| -------------- | ----------- | ------- | ------- | -------- | ----------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
| DAB converter, |             | and the | MFT,    | indicate | that        | they | operate |     |     |     |     |     |     |     |
underincreasedstressonaveragewhensubjectedtothedata
centerloadcomparedtotheEVload.Thisisreflectedinthe
|     |     |     |     |     |     |     |     | FIGURE22. | MFTreliabilityofdifferentmoduleswithinonephase. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
reliabilitycurvesinFig.20astheirlifetimeisrelativelymore
affectedbythechangeinloaddemandcomparedtotheother
components. However, the analysis shows that compared that this variation can cause a deviation of approximately
to the MFT, other devices exhibit only minor reliability ±2.5 years in the B lifetime of the AFEC transistors. The
1
variationsduetosafetymarginsincomponentselection.The B lifetimeindicates1%populationfailuretranslatingto1%
1
MFT’sunreliabilityrelativelyincreasesasaresultofconstant probability of device failure occurring at a set operational
high-temperature operation exhibited with the data center period. This finding underscores the significant impact that
load. With constant SST input voltage in the two scenarios, each design aspect can have on the overall reliability of the
| thermalstressisthemainfactorimpactingthedesignedMFT |     |     |     |     |     |     |     | system. |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
reliability,underscoringthemissionprofile’sinfluenceonits TheSSTcontrolstrategydistributespowerequallyamong
lifetime. themodules,resultinginuniformstressontransistors,diodes,
Furthermore, to evaluate the sensitivity of the lifetime andcapacitorsacrossthemodules.However,thedifferencein
|          |         |             |     | ±5  | ◦C        |     |        | theMFTdielectriclossesincurdifferentstressesontheMFTs |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | --- | --------- | --- | ------ | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| model to | thermal | conditions, |     | a   | variation |     | in the |                                                       |     |     |     |     |     |     |
coolingfluidset-pointoftheAFECcoolingplateisassessed insidethetopology.Fig.22showstheMFTreliabilityunder
considering the EV load. The results of this sensitivity thedifferentmissionprofiles,emphasizingtheimpactofhigh
assessment are provided in Fig. 21. The results indicate voltageinsulationonitslifetime.Whilethedielectriclosses
|     |     |     |     |     |     |     |     | are only | a small portion | of  | the MFT | losses, | as presented | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ------- | ------- | ------------ | --- |
Table6,thecombinationofthedielectriclosseswiththecore
andwindinglossesathighpowerleadtoamoresignificant
differenceinreliabilityasdepictedwiththedatacenterload.
Fig.23illustratestheimpactofMFTreliabilityonmodule
|     |     |     |     |     |     |     |     | performance.      | Under     | EV          | load, the    | MFT | has          | the lowest |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --------- | ----------- | ------------ | --- | ------------ | ---------- |
|     |     |     |     |     |     |     |     | failure risk,     | minimally | affecting   | module       |     | reliability, | with the   |
|     |     |     |     |     |     |     |     | transformers      | in each   | module      | experiencing |     | similar      | energy     |
|     |     |     |     |     |     |     |     | losses throughout |           | the applied | profile      | and | therefore    | similar    |
Effectof±5◦Cvariationincoolingfluidset-point(Tsp)on failureprobabilities.ThisisreflectedintheB 10 lifetimedata
FIGURE21.
theB1lifetimeofAFECtransistors. in Table 8. In contrast, under data center load, the MFT
| 151752 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
|           |                                            |     |     |     |     |     |     | FIGURE24. | SSTreliabilityw/andw/oMFTconsideration. |     |      |             |     |              |
| --------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------- | --- | ---- | ----------- | --- | ------------ |
| FIGURE23. | Modulereliabilityw/andw/oMFTconsideration. |     |     |     |     |     |     |           |                                         |     |      |             |     |              |
|           |                                            |     |     |     |     |     |     | profiles. | Additionally,                           | the | PDIV | calculation |     | in this work |
TABLE8. ModuleB10lifetimew/andw/oMFTconsideration.
assumesthatameanvoidsizeisundefined;therefore,arange
ofpotentialvoidsizesisestablishedtoevaluatethelikelihood
ofPD.IfPDisdeemedpossible,thevoidlengthissettothe
|     |     |     |     |     |     |     |     | one achieving | the | highest | V   | /PDIV, | thereby | accounting |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | --- | ------ | ------- | ---------- |
void
|     |     |     |     |     |     |     |     | for the worst-case |             | scenario. | Based    | on      | the proposed | MFT        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------- | --------- | -------- | ------- | ------------ | ---------- |
|     |     |     |     |     |     |     |     | reliability        | framework,  | the       | effects  | of the  | electrical   | stress on  |
|     |     |     |     |     |     |     |     | the insulation     | lifetime    | model     | can      | be      | mitigated    | during the |
|     |     |     |     |     |     |     |     | design phase       | by ensuring |           | that the | voltage | potential    | across     |
significantly increases the failure risk for each module. The voids within the expected length range does not exceed the
results indicate that Module 1 reaches a 10% probability breakdown voltage of the void gas. On the other hand, this
| of failure | ≈ 4.4 | years | earlier | than | Module | 12. When | the |          |              |     |             |     |              |         |
| ---------- | ----- | ----- | ------- | ---- | ------ | -------- | --- | -------- | ------------ | --- | ----------- | --- | ------------ | ------- |
|            |       |       |         |      |        |          |     | can also | be addressed | by  | determining |     | the expected | average |
MFTisnotconsidered,theresultsindicatethatitwouldtake void size from the encapsulation process and ensuring that
≈1.6timeslongerforthemoduletoreachthesamelevelof
theoperatingvoltageremainsbelowthebreakdownvoltage,
unreliabilityasModule1withMFT. inwhichcasedeviationsinvoidsizewouldbemodeledusing
Following the assessment of the individual components anormaldistributionintheMonteCarloanalysis.
andmodules,theoverallreliabilityoftheSST,whichconsists
Furthermore,thedifferenceintheSSTMTTFbetweenthe
of 36 modules, is evaluated. Fig. 24 displays the SST two mission profiles, in the absence of MFT consideration,
reliabilitycurvefortwoloadprofiles,bothwithandwithout
|     |     |     |     |     |     |     |     | is only about | one | year. This | similarity |     | is attributed | to the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | ---------- | --- | ------------- | ------ |
considering the MFT reliability. Each module contains componentsalloperatingwellbelowtheirmaximumdesign
35 components, resulting in a total of 1,260 components limits, which minimizes degradation over time. As a result,
| within the | SST. | This aggregation |     | significantly |     | increases | the |               |         |           |     |        |         |             |
| ---------- | ---- | ---------------- | --- | ------------- | --- | --------- | --- | ------------- | ------- | --------- | --- | ------ | ------- | ----------- |
|            |      |                  |     |               |     |           |     | the lifetimes | in both | scenarios |     | remain | closely | aligned and |
risk of failure, as illustrated by the B 10 and B 50 lifetimes decreaseduetothemultiplecomponentswithinthesystem.
shown in Fig. 24. These metrics indicate the probability of TheMTTFfortheevaluatedSSTscenariosdoesnotaccount
a single failure event among the 1,260 components, arising for redundancy or scheduled maintenance, both of which
fromacombinationofrandomandwear-outfailures. could significantly improve system reliability and extend
Using(3),theMTTFofthefourSSTreliabilitycurvesare
|     |     |     |     |     |     |     |     | expected | lifetime. | Incorporating |     | these | factors | suggests that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | --- | ----- | ------- | ------------- |
plottedinFig.25,highlightingthedifferenceintheEV-load the SST system has considerable potential to match the
lifetime compared to that of data center load. This study lifetimesofconventionalarchitectureswhilebenefitingfrom
| identifies | the components |     | most | likely | to  | fail, specifically |     |     |     |     |     |     |     |     |
| ---------- | -------------- | --- | ---- | ------ | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
theaddedfunctionalitiesinherentinSSTs.
highlightingthedesignedMFTasthecomponentmostprone
tofailureinthecontextoftheinvestigateddatacenterload.
IncludingtheMFTinthereliabilityanalysisresultsinamore
| than 15%  | reduction | in   | MTTF          | for the | data           | center load. | It is |     |     |     |     |     |     |     |
| --------- | --------- | ---- | ------------- | ------- | -------------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| important | to note   | that | these results |         | are contingent | upon         | the   |     |     |     |     |     |     |     |
specificMFTdesignandmayvarywithminormodifications.
| For example, | altering  |       | the wire | insulation |     | material      | or the |     |     |     |     |     |     |     |
| ------------ | --------- | ----- | -------- | ---------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| cooling      | mechanism | could | improve  |            | the | MFT’s ability | to     |     |     |     |     |     |     |     |
withstandhighoperatingtemperaturesandultimatelyreduce
itsimpactonsystemlifetime.
WhilethereferenceMFTisdesignedaccordingtorequired
systemspecificationsandinsulationdistances,itstillshows
potential for degradation based on the utilized mission FIGURE25. SSTMTTFw/andw/oMFTconsideration.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 151753 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
VII. CONCLUSION [9] P.SalmenandP.Friedrichs,‘‘Qualifyingasiliconcarbidepowermodule:
Thisarticlepresentsacomprehensiveframeworkfordesign- Reliability testing beyond the standards of silicon devices,’’ in Proc.
|     |     |     |     |     |     |     |     | 12th | Int. Conf. | Integr. | Power Electron. | Syst. | (CIPS), | Berlin, | Germany, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ------- | --------------- | ----- | ------- | ------- | -------- |
ingandestimatingthereliabilityofsolid-statetransformers.
Mar.2022,pp.1–9.
| It integrates | a   | proposed | approach |     | for medium |     | frequency |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | -------- | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[10] F.Hoffmann,N.Kaminski,andS.Schmitt,‘‘Comparisonofthepower
transformerreliabilitywithestablishedassessmentsinpower cyclingperformanceofsiliconandsiliconcarbidepowerdevicesinabase-
platelessmodulepackageatdifferenttemperatureswings,’’inProc.33rd
| electronics. | The | framework |     | addresses | both | random | failures |      |             |               |     |         |              |         |        |
| ------------ | --- | --------- | --- | --------- | ---- | ------ | -------- | ---- | ----------- | ------------- | --- | ------- | ------------ | ------- | ------ |
|              |     |           |     |           |      |        |          | Int. | Symp. Power | Semiconductor |     | Devices | ICs (ISPSD), | Nagoya, | Japan, |
andwear-outmodestoevaluatesystemlifetime,highlighting
May2021,pp.175–178,doi:10.23919/ISPSD50666.2021.9452242.
howoperationalconditionsandmissionprofilessignificantly [11] UnderstandingandUsingPowerMOSFETReliabilityData,International
impact overall reliability. The reliability calculation is RectifierCorporation,ElSegundo,CA,USA,1987.
|     |     |     |     |     |     |     |     | [12] A. Testa, | S.  | De Caro, | and S. | Russo, ‘‘A | reliability | model | for power |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------ | ---------- | ----------- | ----- | --------- |
demonstrated through two test cases: an electric vehicle MOSFETs working in avalanche mode based on an experimental
charging load and a data center load. These scenarios temperaturedistributionanalysis,’’IEEETrans.PowerElectron.,vol.27,
show how carefully including reliability factors in the no.6,pp.3093–3100,Jun.2012,doi:10.1109/TPEL.2011.2177279.
|             |             |     |                   |             |     |                   |           | [13] S. E.      | Ogan,         | S. Chakraborty, |            | T. Geury, | and O.             | Hegazy, | ‘‘Lifetime |
| ----------- | ----------- | --- | ----------------- | ----------- | --- | ----------------- | --------- | --------------- | ------------- | --------------- | ---------- | --------- | ------------------ | ------- | ---------- |
| design      | can enhance |     | the understanding |             |     | of SST            | longevity |                 |               |                 |            |           |                    |         |            |
|             |             |     |                   |             |     |                   |           | and             | cost analysis | of              | DC–DC      | solid     | state transformers |         | for wind   |
| and support | effective   |     | risk              | management. |     | The investigation |           |                 |               |                 |            |           |                    |         |            |
|             |             |     |                   |             |     |                   |           | applications,’’ |               | in Proc.        | Int. Symp. | Power     | Electron.,         | Electr. | Drives,    |
Autom.Motion(SPEEDAM),Napoli,Italy,Jun.2024,pp.611–618,doi:
| into MFT | reliability |     | reveals | its critical |     | influence | on SST |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | ------- | ------------ | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
10.1109/speedam61530.2024.10609168.
| lifetime,   | a factor | often | overlooked |     | in         | existing | literature. |              |            |           |                |             |         |          |             |
| ----------- | -------- | ----- | ---------- | --- | ---------- | -------- | ----------- | ------------ | ---------- | --------- | -------------- | ----------- | ------- | -------- | ----------- |
|             |          |       |            |     |            |          |             | [14] R. Cao, | Y.         | Zhang, Y. | Li, X.         | Liu, C.     | Lv, and | D. Liu,  | ‘‘Redundant |
| The results | show     | that  | factoring  | in  | the medium |          | frequency   |              |            |           |                |             |         |          |             |
|             |          |       |            |     |            |          |             | design       | of modular |           | DC solid-state | transformer |         | based on | the long    |
transformerinreliabilityevaluationsmayleadtoasignificant term reliability evaluation,’’ in Proc. 4th Int. Conf. (HVDC),
reductionintheestimatedlifespanofsolid-statetransformers, China, Nov. 2020, pp.730–735, doi: 10.1109/HVDC50696.2020.
9292725.
| emphasizing |     | the necessity |     | of incorporating |     |     | it into the |             |           |     |         |             |        |                   |     |
| ----------- | --- | ------------- | --- | ---------------- | --- | --- | ----------- | ----------- | --------- | --- | ------- | ----------- | ------ | ----------------- | --- |
|             |     |               |     |                  |     |     |             | [15] Y. Li, | Y. Zhang, | R.  | Cao, X. | Liu, C. Lv, | and J. | Liu, ‘‘Redundancy |     |
overall reliability analysis. This framework helps confirm design of modular DC solid-state transformer based on reliabil-
designrobustness,preventsunnecessaryover-designofsafety ity and efficiency evaluation,’’ CPSS Trans. Power Electron. Appl.,
|          |     |            |           |     |            |        |        | vol.   | 6, no. 2, | pp.115–126, | Jun. | 2021, doi: | 10.24295/CPSSTPEA.2021. |     |     |
| -------- | --- | ---------- | --------- | --- | ---------- | ------ | ------ | ------ | --------- | ----------- | ---- | ---------- | ----------------------- | --- | --- |
| margins, | and | ultimately | regulates |     | additional | costs. | Future | 00010. |           |             |      |            |                         |     |     |
work should focus on refining lifetime models, especially [16] U.-M.ChoiandJ.-H.Park,‘‘Developmentandreliabilityassessmentof
regarding MFT reliability, due to the limited data in the SIandSiCpowerdevices-basedsolid-statetransformerforurbanrailway
vehicle,’’IEEETrans.Transport.Electrific.,vol.9,no.2,pp.2744–2753,
| magnetic | components |     | domain. | Additionally, |     | exploring | the |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Jun.2023,doi:10.1109/TTE.2022.3216581.
| variations | of  | the components’ |     | electric | parameters |     | due to |                     |     |              |     |        |          |             |         |
| ---------- | --- | --------------- | --- | -------- | ---------- | --- | ------ | ------------------- | --- | ------------ | --- | ------ | -------- | ----------- | ------- |
|            |     |                 |     |          |            |     |        | [17] V. Raveendran, |     | M. Andresen, |     | and M. | Liserre, | ‘‘Improving | onboard |
converterreliabilityformoreelectricaircraftwithlifetime-basedcontrol,’’
| degradation | over | time | will | further | improve | the | accuracy of |     |     |     |     |     |     |     |     |
| ----------- | ---- | ---- | ---- | ------- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEETrans.Ind.Electron.,vol.66,no.7,pp.5787–5796,Jul.2019,doi:
SSTlifetimeestimation.
10.1109/TIE.2018.2889626.
|     |     |     |     |     |     |     |     | [18] D. Yang, | Y.  | Zhang, | Y. Li, X. | Liu, Z. | Li, J. | Liu, and | X. Jiang, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | --------- | ------- | ------ | -------- | --------- |
REFERENCES ‘‘Power routing method based on optimization problem to improve
[1] R. Medeiros and I. Colak, ‘‘Solid-state transformers: How far have CHB-DAB lifetime,’’ IEEE J. Emerg. Sel. Topics Power Electron.,
|     |         |          |      |           |        |             |            | vol. | 11, no. | 5, pp.5354–5363, |     | Oct. 2023, | doi: 10.1109/JESTPE.2023. |     |     |
| --- | ------- | -------- | ---- | --------- | ------ | ----------- | ---------- | ---- | ------- | ---------------- | --- | ---------- | ------------------------- | --- | --- |
| we  | come?’’ | in Proc. | PCIM | Eur. Int. | Exhib. | Conf. Power | Electron., |      |         |                  |     |            |                           |     |     |
3306156.
| Intell. | Motion, | Renew. | Energy | Energy | Manage., | Nuremberg, | Germany, |                    |     |        |          |                        |     |        |            |
| ------- | ------- | ------ | ------ | ------ | -------- | ---------- | -------- | ------------------ | --- | ------ | -------- | ---------------------- | --- | ------ | ---------- |
|         |         |        |        |        |          |            |          | [19] C. University |     | and W. | Jinxiao, | ‘‘Reliability-oriented |     | design | of DC-link |
May2023,pp.1–12,doi:10.30420/566091329.
consideringthesecond-orderharmoniccurrentroutinginanSSTcell,’’
| [2] J. E. | Huber | and J. | W. Kolar, | ‘‘Applicability |     | of solid-state | trans- |     |     |     |     |     |     |     |     |
| --------- | ----- | ------ | --------- | --------------- | --- | -------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
IEEE Trans. Smart CPSSTrans.PowerElectron.Appl.,vol.8,no.3,pp.290–299,Sep.2023,
formers in today’s and future distribution grids,’’ doi:10.24295/cpsstpea.2023.00025.
| Grid, | vol. 10, | no. 1, | pp.317–326, | Jan. | 2019, | doi: 10.1109/TSG.2017. |     |     |     |     |     |     |     |     |     |
| ----- | -------- | ------ | ----------- | ---- | ----- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[20] J.SahaandS.K.Panda,‘‘Overviewandcomparativeanalysisofbidi-
2738610.
rectionalcascadedmodularisolatedmedium-voltageAC–low-voltageDC
| [3] M. Andresen, |     | V. Raveendran, |     | G. Buticchi, | and | M. Liserre, | ‘‘Lifetime- |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | ------------ | --- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
(MVAC-LVDC)powerconversionforrenewableenergyrichmicrogrids,’’
basedpowerroutinginparallelconvertersforsmarttransformerapplica-
tion,’’IEEETrans.Ind.Electron.,vol.65,no.2,pp.1675–1684,Feb.2018, Renew.Sustain.EnergyRev.,vol.174,Mar.2023,Art.no.113118.
doi:10.1109/TIE.2017.2733426. [21] J. Saha, ‘‘Selection of submodule topology in MVAC-LVDC modular
SST,’’inAnalysis,OptimizationandControlofGrid-InterfacedMatrix
| [4] H. Wang | and | F. Blaabjerg, |     | ‘‘Reliability | of  | capacitors | for DC-link |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | ------------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
BasedIsolatedAC-DCConverters.Singapore:Springer,2022,pp.35–71.
| applications |      | in power    | electronic | converters—An |               | overview,’’ | IEEE       |                   |     |                   |     |            |     |                   |     |
| ------------ | ---- | ----------- | ---------- | ------------- | ------------- | ----------- | ---------- | ----------------- | --- | ----------------- | --- | ---------- | --- | ----------------- | --- |
|              |      |             |            |               |               |             |            | [22] H. Tarzamni, |     | F. P. Esmaeelnia, |     | F. Tahami, | M.  | Fotuhi-Firuzabad, | P.  |
| Trans.       | Ind. | Appl., vol. | 50,        | no. 5,        | pp.3569–3578, | Sep.        | 2014, doi: |                   |     |                   |     |            |     |                   |     |
10.1109/TIA.2014.2308357. Dehghanian, M. Lehtonen, and F. Blaabjerg, ‘‘Reliability assessment
[5] H. Wang, P. Davari, H. Wang, D. Kumar, F. Zare, and F. Blaab- of conventional isolated PWM DC–DC converters,’’ IEEE Access,
jerg, ‘‘Lifetime estimation of DC-link capacitors in adjustable speed vol. 9, pp.46191–46200, 2021, doi: 10.1109/ACCESS.2021.
3067935.
| drives | under | grid voltage | unbalances,’’ |     | IEEE | Trans. Power | Electron., |     |     |     |     |     |     |     |     |
| ------ | ----- | ------------ | ------------- | --- | ---- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[23] H.Tarzamni,F.Tahami,M.Fotuhi-Firuzabad,andF.Blaabjerg,‘‘Improved
| vol. | 34, no. | 5, pp.4064–4078, |     | May | 2019, doi: | 10.1109/TPEL.2018. |     |     |     |     |     |     |     |     |     |
| ---- | ------- | ---------------- | --- | --- | ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2863701. Markovmodelforreliabilityassessmentofisolatedmultiple-switchPWM
[6] D. Zhou, Y. Song, Y. Liu, and F. Blaabjerg, ‘‘Mission profile based DC–DCconverters,’’IEEEAccess,vol.9,pp.33666–33674,2021,doi:
reliabilityevaluationofcapacitorbanksinwindpowerconverters,’’IEEE 10.1109/ACCESS.2021.3060950.
Trans.PowerElectron.,vol.34,no.5,pp.4665–4677,May2019,doi: [24] S. S. Shah and S. Bhattacharya, ‘‘Reliability oriented design of dual
|     |     |     |     |     |     |     |     | active | bridge | converter | for power | supply | on  | heavy-vehicles,’’ | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --------- | --------- | ------ | --- | ----------------- | --- |
10.1109/TPEL.2018.2865710.
[7] P.D.Reigosa,H.Wang,Y.Yang,andF.Blaabjerg,‘‘Predictionofbond Proc. IEEE Energy Convers. Congr. Exposit. (ECCE), Portland,
wirefatigueofIGBTsinaPVinverterunderalong-termoperation,’’IEEE OR, USA, Sep. 2018, pp.4102–4109, doi: 10.1109/ECCE.2018.
| Trans.PowerElectron.,vol.31,no.10,pp.7171–7182,Oct.2016,doi: |     |     |     |     |     |     |     | 8558046. |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
10.1109/TPEL.2015.2509643. [25] S.Acharya,A.Anurag,G.Gohil,S.Hazra,andS.Bhattacharya,‘‘Mission
[8] R.Bayerer,T.Herrmann,T.Licht,J.Lutz,andM.Feller,‘‘Modelforpower profilebasedreliabilityanalysisofamediumvoltagepowerconversion
cyclinglifetimeofIGBTmodules–variousfactorsinfluencinglifetime,’’ architectureforPMSGbasedwindenergyconversionsystem,’’inProc.
inProc.5thInt.Conf.Integr.PowerElectron.Syst.,Nuremberg,Germany, IEEEInd.Appl.Soc.Annu.Meeting(IAS),Portland,OR,USA,Sep.2018,
| Mar.2008,pp.1–6. |     |     |     |     |     |     |     | pp.1–6,doi:10.1109/IAS.2018.8544579. |     |     |     |     |     |               |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | ------------- | --- |
| 151754           |     |     |     |     |     |     |     |                                      |     |     |     |     |     | VOLUME13,2025 |     |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
[26] J. Liu, Y. Fan, J. Hou, and X. Bai, ‘‘Reliability evaluation of DC/DC [46] J. E. Huber and J. W. Kolar, ‘‘Solid-state transformers: On the origins
converter in direct current collection system of wind farm considering andevolutionofkeyconcepts,’’IEEEInd.Electron.Mag.,vol.10,no.3,
the influence of control strategy,’’ Processes, vol. 11, no. 10, p.2825, pp.19–28,Sep.2016,doi:10.1109/MIE.2016.2588878.
Sep.2023,doi:10.3390/pr11102825. [47] A. Meligy, R. Coelho-Medeiros, I. Colak, and S. Bacha,
[27] Y.He,H.Zhang,P.Wang,Y.Huang,Z.Chen,andY.Zhang,‘‘Engineering ‘‘Efficiency-driven parameter selection for dual active bridge
application research on reliability prediction of the combined DC–DC converters,’’ in Proc. 25th Eur. Conf. Power Electron. Appl. (EPE
powersupply,’’Microelectron.Rel.,vol.118,Mar.2021,Art.no.114059, ECCE Europe), Aalborg, Denmark, Sep. 2023, pp.1–8, doi:
doi:10.1016/j.microrel.2021.114059. 10.23919/epe23ecceeurope58414.2023.10264507.
[28] A.Bakeer,A.Chub,andY.Shen,‘‘Reliabilityevaluationofisolatedbuck- [48] J. E. Huber and J. W. Kolar, ‘‘Optimum number of cascaded cells for
boostDC–DCseriesresonantconverter,’’IEEEOpenJ.PowerElectron., high-power medium-voltage AC–DC converters,’’ IEEE J. Emerg. Sel.
vol.3,pp.131–141,2022,doi:10.1109/OJPEL.2022.3157200. Topics Power Electron., vol. 5, no. 1, pp.213–232, Mar. 2017, doi:
[29] K. R. de Faria, T. Phulpin, D. Sadarnac, C. Karimi, and L. Bendani, 10.1109/JESTPE.2016.2605702.
‘‘Reliability, power losses and volume comparison for isolated DC/DC [49] Infineon Technologies AG. (2024). FF450R17ME4_B11—
converters using Si and GaN devices,’’ in Proc. 3ème Symp. de Génie EconoDUALT3 Module. Accessed: Jan. 2025. [Online]. Available:
Electrique(SGE),Jul.2018. https://www.infineon.com/dgdl/Infineon-FF450R17ME4_B11-
[30] M. Mahmoudi, A. Ajami, and E. Babaei, ‘‘Comprehensive reliability DataSheet-v01_10-EN.pdf?fileId=db3a30432fbc32ee012fc06716403a90
evaluation of three types of connection of DC–DC converters: Single- [50] Infineon Technologies AG. (2022). FF3MR20KM1H—62 Mm C-
phase,two-phase,andparallelinput-seriesoutput,’’IETPowerElectron., SeriesT Trench MOSFET. Accessed: Jan. 2025. [Online]. Available:
vol.16,no.12,pp.2065–2075,Sep.2023,doi:10.1049/pel2.12528. https://www.infineon.com/dgdl/Infineon-FF3MR20KM1H-DataSheet-
[31] Insulation Coordination for Equipment Within Low-Voltage Supply v01_00-EN.pdf?fileId=8ac78c8c8afe5bd0018b18a8bcde381a
Systems—Part 1: Principles, Requirements and Tests, document IEC [51] TDKElectronicsAG.(2022).FilmCapacitors—PowerElectronicCapac-
60664-1,2020. itors, MKP DC—B2562. Accessed: Jan. 2025. [Online]. Available:
[32] W. Wang, X. Wang, J. He, Y. Liu, S. Li, and Y. Nie, ‘‘Electric https://www.tdk-electronics.tdk.com/inf/20/50/ds/B2562_.pdf
stress and dielectric breakdown characteristics under high-frequency [52] M.MogorovicandD.Dujic,‘‘Mediumfrequencytransformerdesignand
voltages with multi-harmonics in a solid-state transformer,’’ Int. J. optimization,’’ in Proc. Eur. Int. Exhib. Conf. Power Electron., Intell.
Electr. Power Energy Syst., vol. 129, Jul. 2021, Art.no.106861, doi: Motion,Renew.EnergyEnergyManage.(PCIM),Nuremberg,Germany,
10.1016/j.ijepes.2021.106861. May2017,pp.1–8.
[33] A. Cremasco, D. Rothmund, M. Curti, and E. A. Lomonova, ‘‘Volt-
[53] M. A. Bahmani, T. Thiringer, and M. Kharezy, ‘‘Optimization and
age distribution in the windings of medium-frequency transformers
experimentalvalidationofmedium-frequencyhighpowertransformersin
operated with wide bandgap devices,’’ IEEE J. Emerg. Sel. Topics
solid-statetransformerapplications,’’inProc.IEEEAppl.PowerElectron.
Power Electron., vol. 10, no. 4, pp.3587–3602, Aug. 2022, doi:
Conf.Exposit.(APEC),LongBeach,CA,USA,Mar.2016,pp.3043–3050,
10.1109/JESTPE.2021.3064702.
doi:10.1109/APEC.2016.7468297.
[34] Y.Zhao,G.Zhang,D.Han,K.Li,Z.Qiu,andF.Yang,‘‘Experimental
[54] N.DjekanovicandD.Dujic,‘‘DesignoptimizationofaMW-levelmedium
study on insulation properties of epoxy casting resins using high-
frequencytransformer,’’inProc.Eur.Int.Exhib.Conf.PowerElectron.,
frequency square waveforms,’’ CSEE J. Power Energy Syst., vol. 7,
Intell. Motion, Renew. Energy Energy Manage., Nuremberg, Germany,
no. 6, pp.1227–1237, Nov. 2021, doi: 10.17775/CSEEJPES.2019.
May2022,pp.1–10.
02110.
[55] (2020).FiniteElementMethodMagnetics(FEMM)[ComputerSoftware].
[35] Q.Zhuang,P.H.F.Morshuis,X.Chen,S.Meijer,J.J.Smit,andZ.Xu,
[Online].Available:https://www.femm.info/wiki/HomePage
‘‘Lifepredictionforepoxyresininsulatedtransformerwindingsthrough
[56] J. Falck, C. Felgemacher, A. Rojko, M. Liserre, and P. Zacharias,
acceleratedagingtests,’’inProc.10thIEEEInt.Conf.SolidDielectrics,
‘‘Reliability of power electronic systems: An industry perspective,’’
Potsdam, Germany, Jul. 2010, pp.1–4, doi: 10.1109/ICSD.2010.
IEEE Ind. Electron. Mag., vol. 12, no. 2, pp.24–35, Jun. 2018, doi:
5567921.
10.1109/MIE.2018.2825481.
[36] S. Peyghami, Z. Wang, and F. Blaabjerg, ‘‘A guideline for reliability
predictioninpowerelectronicconverters,’’IEEETrans.PowerElectron., [57] Infineon Technologies AG, ‘‘Transient thermal measurements and
thermal equivalent circuit models,’’ Appl. Note AN2015-10, V
vol.35,no.10,pp.10958–10968,Oct.2020,doi:10.1109/TPEL.2020.
1.2, 2020. Available: https://www.infineon.com/dgdl/Infineon-
2981933.
Thermal_equivalent_circuit_models-ApplicationNotes-v01_02-
[37] F.RichardeauandT.T.L.Pham,‘‘Reliabilitycalculationofmultilevel
EN.pdf?fileId=db3a30431a5c32f2011aa65358394dd2
converters:Theoryandapplications,’’IEEETrans.Ind.Electron.,vol.60,
no.10,pp.4225–4233,Oct.2013,doi:10.1109/TIE.2012.2211315. [58] Mersen Electrical Power. (2022). IsoMAXX: Enhanced
[38] G.Yang,LifeCycleReliabilityEngineering.Hoboken,NJ,USA:Wiley, Cooling. Accessed: Jan. 2025. [Online]. Available:
2007,doi:10.1002/9780470117880. https://ep-cn.mersen.com/en/products/engineering/isomaxx-enhanced-
[39] W. Kuo and M. J. Zuo, Optimal Reliability Modeling: Principles and cooling?level1#paragraph-309701
Applications.Hoboken,NJ,USA:Wiley,2003. [59] I. Villar, ‘‘Multiphysical characterization of medium-frequency power
[40] H. Wang, K. Ma, and F. Blaabjerg, ‘‘Design for reliability of electronictransformers,’’Ph.D.dissertation,Ècolepolytechniquefédérale
power electronic systems,’’ in Proc. 38th Annu. Conf. IEEE Ind. deLausanne,Lausanne,Switzerland,2010.
Electron. Soc., Montreal, QC, Canada, Oct. 2012, pp.33–44, doi: [60] T.Guillod,‘‘Modelinganddesignofmedium-frequencytransformersfor
10.1109/IECON.2012.6388833. futuremedium-voltagepowerelectronicsinterfaces,’’Ph.D.dissertation,
[41] MIL-HDBK-217: Reliability Prediction of Electronic Equipment, U.S. ETH,Zurich,Switzerland,2018.
Dept.Defense,Washington,DC,USA,1995. [61] A.Meligy,J.Twizeyimana,R.Coelho-Medeiros,C.Stackler,I.Colak,
[42] S. Peyghami, H. Wang, P. Davari, and F. Blaabjerg, ‘‘Mission- andS.Bacha,‘‘New2Dthermalmodelforshell-typemediumfrequency
profile-basedsystem-levelreliabilityanalysisinDCmicrogrids,’’IEEE transformersandexperimentalvalidationthereof,’’inProc.IEEEDesign
Trans. Ind. Appl., vol. 55, no. 5, pp.5055–5067, Sep. 2019, doi: MethodologiesConf.(DMC),Grenoble,France,Nov.2024,pp.1–8.
10.1109/TIA.2019.2920470. [62] D.Zhou,H.Wang,andF.Blaabjerg,‘‘Missionprofilebasedsystem-level
[43] X.She,A.Q.Huang,andR.Burgos,‘‘Reviewofsolid-statetransformer reliabilityanalysisofDC/DCconvertersforabackuppowerapplication,’’
technologiesandtheirapplicationinpowerdistributionsystems,’’IEEEJ. IEEETrans.PowerElectron.,vol.33,no.9,pp.8030–8039,Sep.2018,
Emerg.Sel.TopicsPowerElectron.,vol.1,no.3,pp.186–198,Sep.2013, doi:10.1109/TPEL.2017.2769161.
doi:10.1109/JESTPE.2013.2277917. [63] M.Novak,A.Sangwongwanich,andF.Blaabjerg,‘‘MonteCarlo-based
[44] J.W.KolarandG.Ortiz,‘‘Solid-state-transformers:Keycomponentsof reliability estimation methods for power devices in power electronics
futuretractionandsmartgridsystems,’’inProc.Int.PowerElectron.Conf. systems,’’IEEEOpenJ.PowerElectron.,vol.2,pp.523–534,2021,doi:
ECCEAsia(IPEC),Hiroshima,Japan,2014. 10.1109/OJPEL.2021.3116070.
[45] R.Peña-Alzola,G.Gohil,L.Mathe,M.Liserre,andF.Blaabjerg,‘‘Review [64] I.F.Kovacevic-Badstuebner,J.W.Kolar,andU.Schilling,‘‘Modellingfor
ofmodularpowerconverterssolutionsforsmarttransformerindistribution thelifetimepredictionofpowersemiconductormodules,’’inReliability
system,’’inProc.IEEEEnergyConvers.Congr.Exposit.,Denver,CO, ofPowerElectronicConverterSystems.London,U.K.:IET,2015,ch.5,
USA,Sep.2013,pp.380–387,doi:10.1109/ECCE.2013.6646726. pp.103–140,doi:10.1049/PBPO080E_ch5.
VOLUME13,2025 151755

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
[65] Infineon, ‘‘Technical information IGBT modules use of power cycling [85] R. Szilágyi, P. Molinié, M. J. Kirkpatrick, E. Odic, G. Galli, and P.
curves for IGBT 4,’’ Appl. Note AN2010-02, Infineon, Neubiberg, Dessante, ‘‘Role of temperature in partial discharge inception voltage
Germany,2012. attriplejunctions,’’IEEETrans.Dielectr.Electr.Insul.,vol.30,no.6,
[66] PC and TC Diagrams, Infineon Technologies AG, Munich, Germany, pp.2809–2818,Dec.2023,doi:10.1109/TDEI.2023.3315686.
InfineonAN2019-05,2019. [86] A.Meligy,R.Coelho-Medeiros,I.Colak,andS.Bacha,‘‘Mission-profile
basedreliabilityframeworkformedium-frequencytransformers,’’inProc.
| [67] M. Farhadi, |     | B. T. Vankayalapati, |     | and | B. Akin, | ‘‘Reliability | evalu- |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------- | --- | --- | -------- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ation of SiC MOSFETs under realistic power cycling tests,’’ IEEE 26thEur.Conf.PowerElectron.Appl.(EPE),Paris,France,Mar.2025,
Power Electron. Mag., vol. 10, no. 2, pp.49–56, Jun. 2023, doi: doi:10.34746/epe2025-0095.
10.1109/MPEL.2023.3271621. [87] T.Liu,Q.Li,G.Dong,M.Asif,X.Huang,andZ.Wang,‘‘Multi-factor
[68] U.ScheuermannandP.Beckedahl,‘‘Theroadtothenextgenerationpower modelforlifetimepredictionofpolymersusedasinsulationmaterialin
highfrequencyelectricalequipment,’’Polym.Test.,vol.73,pp.193–199,
module–100%solderfreedesign,’’inProc.5thInt.Conf.Integr.Power
| Electron.Syst.,Nuremberg,Germany,Mar.2008,pp.1–10. |     |     |     |     |     |     |     | Feb.2019. |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[69] U.ScheuermannandR.Schmidt,‘‘Anewlifetimemodelforadvanced [88] Z. Wang, X. Wei, F. F. da Silva, H. Sørensen, Z. Shen, and C.
powermoduleswithsinteredchipsandoptimizedAlwirebonds,’’inProc. L. Bak, ‘‘Interactions analysis and life modeling for high-frequency
Int.Exhib.Conf.PowerElectron.,Intell.Motion,Renew.EnergyEnergy transformersinsulationundermultistress,’’IEEETrans.PowerElectron.,
|     |     |     |     |     |     |     |     | vol. | 40, no. | 4, pp.5646–5660, |     | Apr. 2025, | doi: | 10.1109/TPEL.2024. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ---------------- | --- | ---------- | ---- | ------------------ | --- |
Manag.(PCIM,2013,pp.810–817.
3520336.
[70] M.A.Miner,‘‘Cumulativedamageinfatigue,’’J.Appl.Mech.,vol.12,
|     |     |     |     |     |     |     |     | [89] X. Shang, | L.  | Pang, Q. | Bu, and | Q. Zhang, | ‘‘Partial | discharge | aging |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------- | --------- | --------- | --------- | ----- |
no.3,pp.A159–A164,Sep.1945,doi:10.1115/1.4009458.
[71] D. J. Lichtenwalner, A. Akturk, J. McGarrity, J. Richmond, T. Bar- of epoxy insulation at different high-frequency pulse parameters
bieri, B. Hull, D. Grider, S. Allen, and J. W. Palmour, ‘‘Reliabil- and environmental stresses,’’ IEEE Trans. Dielectr. Electr. Insul.,
|        |     |               |         |        |     |         |              | vol. | 32, no. | 1, pp.45–54, |     | Feb. 2025, | doi: | 10.1109/TDEI.2024. |     |
| ------ | --- | ------------- | ------- | ------ | --- | ------- | ------------ | ---- | ------- | ------------ | --- | ---------- | ---- | ------------------ | --- |
| ity of | SiC | power devices | against | cosmic | ray | neutron | single-event |      |         |              |     |            |      |                    |     |
3502581.
| burnout,’’ | Mater. | Sci. | Forum, | vol. 924, | pp.559–562, |     | Jun. 2018, doi: |                 |     |            |        |       |              |       |            |
| ---------- | ------ | ---- | ------ | --------- | ----------- | --- | --------------- | --------------- | --- | ---------- | ------ | ----- | ------------ | ----- | ---------- |
|            |        |      |        |           |             |     |                 | [90] W. Haiyan, |     | G. Yunjie, | and C. | Xian, | ‘‘Electrical | aging | experiment |
10.4028/www.scientific.net/msf.924.559.
|     |     |     |     |     |     |     |     | of  | epoxy | resin insulation |     | equipment | and | research | on the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | --------- | --- | -------- | ------ |
[72] F.Principato,S.Altieri,L.Abbene,andF.Pintacuda,‘‘Acceleratedtests
onSIandSiCpowertransistorswiththermal,fastandultra-fastneutrons,’’ influence of electrical field uniformity,’’ in Proc. 4th Int.
|     |     |     |     |     |     |     |     | Conf. | Electric | Power | Equip. | Switching | Technol. |     | (ICEPE-ST), |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----- | ------ | --------- | -------- | --- | ----------- |
Sensors,vol.20,no.11,p.3021,May2020,doi:10.3390/s20113021.
|                      |     |          |     |          |     |                         |     | China, | Oct. | 2017, | pp.565–568, |     | doi: 10.1109/ICEPE-ST.2017. |     |     |
| -------------------- | --- | -------- | --- | -------- | --- | ----------------------- | --- | ------ | ---- | ----- | ----------- | --- | --------------------------- | --- | --- |
| [73] J. Lappalainen, |     | ‘‘Cosmic | ray | failures | in  | power semiconductors,’’ |     |        |      |       |             |     |                             |     |     |
8188911.
| Master’s | thesis, | Dept.    | Faculty  | Inf. | Technol. | Commun.   | Sci.,      |                |     |           |          |       |           |       |               |
| -------- | ------- | -------- | -------- | ---- | -------- | --------- | ---------- | -------------- | --- | --------- | -------- | ----- | --------- | ----- | ------------- |
|          |         |          |          |      |          |           |            | [91] C. Zhang, | J.  | Xiang, Z. | Chen, Z. | Wang, | Y. Su, S. | Wang, | J. Li, and S. |
| Tampere  | Univ.,  | Tampere, | Finland, | Dec. | 2022.    | [Online]. | Available: |                |     |           |          |       |           |       |               |
https://trepo.tuni.fi/handle/10024/143997 Li, ‘‘Surface degradation of epoxy resin exposed to corona discharge
|                      |     |       |         |               |     |              |        | under | bipolar | square wave | field: | From | phenomenon | to the | insights,’’ |
| -------------------- | --- | ----- | ------- | ------------- | --- | ------------ | ------ | ----- | ------- | ----------- | ------ | ---- | ---------- | ------ | ----------- |
| [74] C. Felgemacher, |     | S. V. | Araújo, | P. Zacharias, |     | K. Nesemann, | and A. |       |         |             |        |      |            |        |             |
Polym.DegradationStability,vol.228,Oct.2024,Art.no.110922,doi:
| Gruber, | ‘‘Cosmic | radiation | ruggedness |     | of SI | and SiC | power semi- |     |     |     |     |     |     |     |     |
| ------- | -------- | --------- | ---------- | --- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
10.1016/j.polymdegradstab.2024.110922.
| conductors,’’ |          | in Proc. | 28th Int. | Symp.     | Power | Semiconductor | Devices        |                |          |              |           |          |          |            |            |
| ------------- | -------- | -------- | --------- | --------- | ----- | ------------- | -------------- | -------------- | -------- | ------------ | --------- | -------- | -------- | ---------- | ---------- |
|               |          |          |           |           |       |               |                | [92] C. Hecht, | J.       | Figgener,    | X. Li, L. | Zhang,   | and D.   | U. Sauer,  | ‘‘Standard |
| ICs           | (ISPSD), | Prague,  | Czech     | Republic, | Jun.  | 2016,         | pp.51–54, doi: |                |          |              |           |          |          |            |            |
|               |          |          |           |           |       |               |                | load           | profiles | for electric | vehicle   | charging | stations | in Germany | based      |
10.1109/ISPSD.2016.7520775. on representative, empirical data,’’ Energies, vol. 16, no. 6, p.2619,
[75] N.KaminskiandA.Kopta,‘‘FailureratesofHiPakmodulesduetocosmic
Mar.2023.
rays,’’ABBSwitzerlandLtd,Zurich,Switzerland,ABBAppl.Note5SYA
[93] R.Rahmani,I.Moser,andM.Seyedmahmoudian,‘‘Acompletemodelfor
2042-04,2011.
modularsimulationofdatacentrepowerload,’’2018,arXiv:1804.00703.
| [76] M. Chafai, | L.  | Refoufi, | and | H. Bentarzi, | ‘‘Large | power | transformer |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | --- | ------------ | ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
[94] InsulationSystemThermalLifeExpectancyVsTotalOperatingTempera-
reliabilitymodeling,’’Int.J.Syst.AssuranceEng.Manage.,vol.7,no.S1, ture,MarathonGenerators,USA,2015.
pp.9–17,Dec.2016,doi:10.1007/s13198-014-0261-2.
[95] J.Ma,Y.Yang,Q.Wang,Y.Deng,M.Yap,W.K.Chern,J.T.Oh,andZ.
| [77] P. Maussion, |     | A. Picot, | M.  | Chabert, | and D. | Malec, | ‘‘Lifespan and |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | -------- | ------ | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen,‘‘Degradationandlifetimepredictionofepoxycompositeinsulation
| aging | modeling | methods | for insulation |     | systems | in electrical | machines: |     |     |     |     |     |     |     |     |
| ----- | -------- | ------- | -------------- | --- | ------- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
materialsunderhighrelativehumidity,’’Polymers,vol.15,no.12,p.2666,
| A survey,’’ | in  | Proc. | IEEE Workshop |     | Electr. | Mach. Design, | Control |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | ------------- | --- | ------- | ------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Jun.2023.
| Diagnosis | (WEMDCD), |     | Turin, | Italy, | Mar. 2015, | pp.279–288, | doi: |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | ------ | ------ | ---------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
10.1109/WEMDCD.2015.7194541.
| [78] X. Zhou, | P.  | Giangrande, | Y.          | Ji, W.     | Zhao, | S. Ijaz,  | and M. Galea, |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | ----------- | ---------- | ----- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ‘‘Insulation  | for | rotating    | low-voltage | electrical |       | machines: | Degradation,  |     |     |     |     |     |     |     |     |
lifetimemodeling,andacceleratedagingtests,’’Energies,vol.17,no.9,
p.1987,Apr.2024,doi:10.3390/en17091987.
[79] M.ErdoganandM.K.Eker,‘‘Acomparativeanalysisofpartialdischarge
| in 13 | combined | insulation | structures | of  | 11 materials | used | in cast-resin |     |     |     |     |     |     |     |     |
| ----- | -------- | ---------- | ---------- | --- | ------------ | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
dry-typetransformers,’’IEEETrans.Dielectr.Electr.Insul.,vol.29,no.6,
pp.2330–2339,Dec.2022,doi:10.1109/TDEI.2022.3205285.
[80] L.Simoni,‘‘Ageneralapproachtotheenduranceofelectricalinsulation
undertemperatureandvoltage,’’IEEETrans.Electr.Insul.,vol.EI-16,
no.4,pp.277–289,Aug.1981,doi:10.1109/TEI.1981.298361.
[81] L.Simoni,‘‘Generalequationofthedeclineintheelectricstrengthfor
| combined | thermal | and | electrical | stresses,’’ | IEEE | Trans. | Electr. Insul., |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | ---------- | ----------- | ---- | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.EI-19,no.1,pp.45–52,Feb.1984,doi:10.1109/TEI.1984.298732.
|     |     |     |     |     |     |     |     |     |     | AHMED | MELIGY |     | received | the B.Sc. | degree in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | --- | -------- | --------- | --------- |
[82] M.G.DeLaCalle,J.M.Martínez-Tarifa,Á.M.GómezSolanilla,and
|     |     |     |     |     |     |     |     |     |     | electrical | engineering |     | from American |     | University |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ------------- | --- | ---------- |
G.Robles,‘‘Uncertaintysourcesintheestimationofthepartialdischarge
|     |     |     |     |     |     |     |     |     |     | of  | Sharjah, | in 2018, | and | the M.Sc. | degree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | --------- | ------ |
inceptionvoltageinturn-to-turninsulationsystems,’’IEEEAccess,vol.8,
|     |     |     |     |     |     |     |     |     |     | in  | renewable | energy | engineering | and | manage- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----------- | --- | ------- |
pp.157510–157519,2020,doi:10.1109/ACCESS.2020.3018870.
[83] Y.Kemari,C.V.d.Steen,G.Belijar,L.Laudebat,S.Diaham,Z.Valdez- ment from Albert-Ludwigs-Universität Freiburg,
|     |     |     |     |     |     |     |     |     |     | in  | 2022. He | is currently | pursuing | the | Industrial |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | -------- | --- | ---------- |
Nava,andC.Abadie,‘‘ATownsend’ssecondaryionizationcoefficientesti-
Ph.D.degreeinelectricalengineeringwithGreno-
mationmethodforpartialdischargeinceptionvoltagepredictionforinsu-
|     |     |     |     |     |     |     |     |     |     | ble | Electrical | Engineering | Laboratory |     | (G2Elab), |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---------- | --- | --------- |
latingpolymers,’’inProc.IEEE4thInt.Conf.Dielectr.(ICD),Palermo,
|     |     |     |     |     |     |     |     |     |     | Grenoble |     | INP, France, | in  | collaboration | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | --- | ------------- | ---- |
Italy,Jul.2022,pp.226–229,doi:10.1109/ICD53806.2022.9863604.
|     |     |     |     |     |     |     |     |     |     | Schneider |     | Electric, | France. | He is also | a Power |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------- | ---------- | ------- |
[84] L.ElorzaAzpiazu,G.Almandoz,A.Egea,G.Ugalde,andX.Badiola,
‘‘Studyofpartialdischargeinceptionvoltageininverterfedelectricmotor Electronics Research Engineer with Schneider Electric. His research
insulationsystems,’’Appl.Sci.,vol.13,no.4,p.2417,Feb.2023,doi: interestsincludesolid-statetransformers,multi-levelconverters,reliability,
| 10.3390/app13042417. |     |     |     |     |     |     |     | andoptimization. |     |     |     |     |     |               |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | ------------- | --- |
| 151756               |     |     |     |     |     |     |     |                  |     |     |     |     |     | VOLUME13,2025 |     |

A.Meligyetal.:MissionProfile-BasedReliabilityAssessmentforModularMVAC-LVDCSolid-StateTransformers
RAFAEL COELHO-MEDEIROS received the SEDDIK BACHA (Senior Member, IEEE) was
M.Sc. degree in electrical engineering from borninIghram(Béjaïa-Bgayet),Algeria,in1958.
the National Polytechnic Institute of Toulouse, HereceivedtheEngineeringandmaster’sdegrees
in2018,andthePh.D.degreefromParis-Saclay fromtheNationalPolytechnicSchoolofAlgiers
University,in2022,France.Heiscurrentlywith (ENPAlger), in 1982 and 1990, respectively,
Schneider Electric, as a Lead Power Electron- the Ph.D. and Habilitation to Direct Research
ics Research and Development Engineer, with degreesfromtheNationalPolytechnicInstituteof
research interests in grid-connected power elec- Grenoble,in1993and1998,respectively,andthe
tronics converters, multiphysics modeling, real- AlgerianStateDoctoratedegree.
timesimulation,andpower-hardwareintheloop Hehaspreviouslyheldmanyscientificrespon-
testing. sibilities,bothlocallyastheHeadofaresearchgrouponelectricalsystems
|     |     |     |     | and networks | (80 people) and | at the national level, | where he served | as  |
| --- | --- | --- | --- | ------------ | --------------- | ---------------------- | --------------- | --- |
theDeputyDirectorofaCNRSResearchGroupgathering400researchers
|     |     |     |     | in electrical | engineering in France. | He is currently          | a Professor with  | the |
| --- | --- | --- | --- | ------------- | ---------------------- | ------------------------ | ----------------- | --- |
|     |     |     |     | University of | Grenoble Alpes.        | He is also the President | of the Scientific |     |
ILKNUR COLAK (Senior Member, IEEE) CounciloftheSuperGridEnergyTransitionInstituteandleadsoneofits
receivedtheM.Sc.andPh.D.degreesinelectrical scientific programs. In parallel, he is also a Researcher with the G2Elab
engineering from Istanbul Technical Univer- Laboratory,Grenoble.Hisscientificinterestsincludeoptimalmanagement
sity, Istanbul, Türkiye. In last 23 years, she ofenergyflowsandmodelingandcontrolofelectricalsystems.Hisresearch
worked in industry and research centers, such applicationscoverrenewableenergyintegration,electricmobility,HVDC
as ABB, Ansaldo Richerhe, TÜBITAK, CERN, networks, and microgrids. In these fields, he has supervised more than
and Maschinenfabrik Reinhausen. Since January 60doctoralthesesandco-authoredover500contributions,includingtwo
2022, she has been with Schneider Electric educationalbooksonelectricvehiclesandoneonthemodelingandcontrol
|     | and leading | the Medium Voltage | Converter | ofEPconverters. |     |     |     |     |
| --- | ----------- | ------------------ | --------- | --------------- | --- | --- | --- | --- |
activities.Herresearchinterestsincludemultilevel
convertertopologies,modulationschemes,transformerlessconcepts,high
| power resonant | converters, insulation-coordination, | EMC | and grounding, |     |     |     |     |     |
| -------------- | ------------------------------------ | --- | -------------- | --- | --- | --- | --- | --- |
reliability,andwaveenergyconversionsystems.
| VOLUME13,2025 |     |     |     |     |     |     |     | 151757 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ------ |