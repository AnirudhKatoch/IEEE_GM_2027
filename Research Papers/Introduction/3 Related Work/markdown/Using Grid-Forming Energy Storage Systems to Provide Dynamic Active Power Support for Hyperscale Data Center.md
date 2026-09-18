IEEEPOWER&ENERGYSOCIETYSECTION
Received28January2026,accepted16February2026,dateofpublication23February2026,dateofcurrentversion26February2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3666746
| Using                  | Grid-Forming |                       |                      | Energy          | Storage         |     | Systems |     |     |     |
| ---------------------- | ------------ | --------------------- | -------------------- | --------------- | --------------- | --- | ------- | --- | --- | --- |
| to Provide             |              | Dynamic               |                      | Active          | Power           |     | Support |     |     |     |
| for Hyperscale         |              |                       | Data                 | Center          |                 |     |         |     |     |     |
| BRETTA.ROSS            |              | ,(Member,IEEE),XUELYU |                      |                 | ,(Member,IEEE), |     |         |     |     |     |
| UDOKAC.NWANETO         |              | ,(SeniorMember,IEEE), |                      |                 |                 |     |         |     |     |     |
| SHEIKMOHAMMADMOHIUDDIN |              |                       |                      | ,(Member,IEEE), |                 |     |         |     |     |     |
| ANDALEXANDREB.NASSIF   |              |                       | ,(SeniorMember,IEEE) |                 |                 |     |         |     |     |     |
PacificNorthwestNationalLaboratory,Richland,WA99354,USA
Correspondingauthor:BrettA.Ross(brett.ross@pnnl.gov)
ThisworkwassupportedbythePacificNorthwestNationalLaboratory(PNNL)operatedbyBattelleforU.S.DepartmentofEnergyunder
ContractDE-AC05-76RL01830.
ABSTRACT Large artificial intelligence (AI) training data centers are emerging as significant, highly
dynamicdigitalloadsthatposenumerouschallengestopowersystemstability.Methodstostudyandassess
theirimpactarestillbeingdevelopedandhavebeenthefocusofnumerousindustryinterestgroups.Intended
to contribute to bridging this gap, this paper develops a credible impact study for data centers, presenting
a dynamic data-center model that includes an uninterruptible power supply (UPS), co-generator, cooling
system, and a grid-forming (GFM) controlled energy storage system (ESS), with explicit converter and
controldynamics.Usingelectromagnetictransientsimulations,twostressscenariosarestudied:low-voltage
faultsandfastloadfluctuationscharacteristicofAItraining.Theresultsshowthatanadequatelytunedand
controlled GFM ESS can significantly improve the large load response by reducing frequency overshoot,
raising the nadir, shortening settling time, and enhancing post-fault recovery. Under fast fluctuation AI
training load profiles, the ESS also damps active-power oscillations and reduces torsional shaft-torque
oscillations in the generator train to safe levels. These findings support ESS-based control as an effective
toolforintegratinglargeAIdatacenterswithoutcompromisinggridstability.
INDEXTERMS Datacenterpower,energystorage,gridforming,powersmoothing,powersystemfaults.
I. INTRODUCTION in the transmission system. These variations can exceed
To accommodate society’s rapidly increasing broadband the response capabilities of traditional technologies such as
usage and facilitate development of larger artificial intel- electromechanical generation, leading to adverse impacts to
ligence (AI) models, particularly large language models, transmission system reliability [3]. Energy storage systems
hyperscaledatacenterswithconsumptionsexceeding1GW (ESS),duetotheirpowerelectronicgridinterfaceandflexible
are rapidly connecting to the grid [1], [2]. Being pre- dispatch, are well suited to provide dynamic active and
dominantly electronic loads, hyperscale data centers are reactivepowersupportnecessarytomaintainareliablegrid
both sensitive to grid disturbances and capable of rapidly while integrating hyperscale data centers [4]. Grid-forming
varying their power consumption, especially when they (GFM) control is especially applicable to ESS because the
are used for large-scale parallel computing tasks (e.g., DC link inherently supplies the necessary energy buffer,
training large language models). Due to the data centers’ enablingGFMfunctionalitytoberealizedprimarilythrough
| size and | tendency | to concentrate | geographically, |     | these | software[5]. |     |     |     |     |
| -------- | -------- | -------------- | --------------- | --- | ----- | ------------ | --- | --- | --- | --- |
characteristicsleadtorapidvariationsinactivepowerflows
A. LITERATUREREVIEWANDMOTIVATION
|               |        |              |            |                    |     | While | hyperscale | data centers | with power | consumptions |
| ------------- | ------ | ------------ | ---------- | ------------------ | --- | ----- | ---------- | ------------ | ---------- | ------------ |
| The associate | editor | coordinating | the review | of this manuscript | and |       |            |              |            |              |
approvingitforpublicationwasEmilioBarocio. exceeding 1 GW are rapidly being connected to bulk

2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
29250 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME14,2026

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
powersystems,accuratedynamicmodelsthatsimultaneously but detailed transmission system equivalent and a detailed
capture the interactions among information technology data center model. Two specific use cases are considered:
equipment (ITE), cooling systems, uninterruptible power post-fault frequency regulation and oscillation suppression.
supplies (UPS), ESS, and co-located generation remain Forpost-faultfrequencyregulation,thetransmissionsystem
scarce. Existing studies typically represent data centers as equivalent provides an aggregate representation of the
aggregate static or quasi-static loads [6], [7], [8], which is transmission system’s fault and frequency response. For
usefulforflexibleloadmanagementbutdoesnotresolvefast oscillation suppression, a steam turbine with a detailed
electromechanicalandcontroldrivendynamics.Otherworks multi-massturbinemodelisplacedatthedatacenterforthe
examine specific aspects of data center power systems— purposesofgeneration.Whilemodeledinthesamefacility,
for example, energy consumption and power electronics our findings also apply to any synchronous generator that
challenges from building distribution through DC architec- couldbenearby,e.g.,thermalbasegeneration.Thisenables
tures down to the board level [9], an all-in-one load data analysis of the internal stresses placed on the turbine shaft,
centerpoweremulatoronareconfigurablepower-electronics whichareoneoftheprimaryreliabilityconcernsassociated
hardware testbed [10], or an isolated parallel-ring bus with rapidly varying data center loads. For both cases,
datacenter microgrid with multiple UPSs [11]. However, we demonstrate GFM ESS control strategies are capable of
a high-fidelity dynamic model that integrates ITE, cooling, mitigatingthereliabilityissuesandcharacterizetheeffectsof
UPS, ESS, and co-located generation in a system-level majorsystemanddesignvariablessuchassysteminertiaand
contextisstilllacking.Toaddressthisgap,wedevelopsuch ESSsize.TheseresultsillustratethepotentialefficacyofESS
anintegrateddynamicmodelinthiswork. for augmenting bulk system reliability and provide insights
|             |           |             |            |     |      |           |     | into the | credible | application |     | and performance |     | expectations |     |
| ----------- | --------- | ----------- | ---------- | --- | ---- | --------- | --- | -------- | -------- | ----------- | --- | --------------- | --- | ------------ | --- |
| As AI       | workloads | scale,      | hyperscale |     | data | centers   | are |          |          |             |     |                 |     |              |     |
| introducing | new       | operational | challenges |     | that | can delay | or  | forESS.  |          |             |     |                 |     |              |     |
constrain their interconnection to the bulk power system. Thecontributionsofthisworkare:
| In 2024,        | a 230 | kV transmission |                       | line | fault in | the          | Eastern |               |     |      |                 |             |         |         |      |
| --------------- | ----- | --------------- | --------------------- | ---- | -------- | ------------ | ------- | ------------- | --- | ---- | --------------- | ----------- | ------- | ------- | ---- |
|                 |       |                 |                       |      |          |              |         | • development |     | of   | a high-fidelity |             | dynamic | model   | of a |
| Interconnection |       | led to          | a customer-initiated, |      |          | simultaneous |         |               |     |      |                 |             |         |         |      |
|                 |       |                 |                       |      |          |              |         | hyperscale    |     | data | center,         | integrating | ITE,    | cooling | sys- |
loss of approximately 1,500 MW of voltage sensitive load tems, UPS, ESS, and a co-located generator within a
| that operators | had | not | anticipated | [12], | [13]. | Many | large |       |            |     |           |     |               |          |     |
| -------------- | --- | --- | ----------- | ----- | ----- | ---- | ----- | ----- | ---------- | --- | --------- | --- | ------------- | -------- | --- |
|                |     |     |             |       |       |      |       | PSCAD | framework, |     | capturing |     | their control | dynamics |     |
loadsincludeprotectionandcontrolfunctionsthatdisconnect
andinteractions;
| during disturbances; |     | the | resulting | tripping | and | reconnection |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• system-levelassessmentoflargedatacenterintegration,
| can cause | significant | frequency |     | excursions |     | and increase |     |           |     |             |     |          |      |          |     |
| --------- | ----------- | --------- | --- | ---------- | --- | ------------ | --- | --------- | --- | ----------- | --- | -------- | ---- | -------- | --- |
|           |             |           |     |            |     |              |     | including |     | the impacts |     | of large | load | tripping | and |
the risk of generator tripping, thereby threatening overall re-connection on bulk system frequency and volt-
| grid stability | and      | integrity.  | In    | addition, | rapid  | load | ramps  |         |                |     |          |                |         |               |     |
| -------------- | -------- | ----------- | ----- | --------- | ------ | ---- | ------ | ------- | -------------- | --- | -------- | -------------- | ------- | ------------- | --- |
|                |          |             |       |           |        |      |        | age,    | and evaluation |     | of       | a grid-forming |         | ESS providing |     |
| (up or         | down) of | data center | loads | can       | stress | the  | system |         |                |     |          |                |         |               |     |
|                |          |             |       |           |        |      |        | dynamic | active         | and | reactive | power          | support | following     |     |
because generation must be quickly loaded or unloaded in faults, demonstrating improved post-fault frequency
response.Largeloadscanalsoactassourcesofoscillations,
nadir/overshootandvoltageregulation;
introducing reliability risks [14]. Against this backdrop, • analysis of high-frequency load-induced oscillations,
| there is | growing | industry | interest | in using | GFM | ESS | as a |     |     |     |     |     |     |     |     |
| -------- | ------- | -------- | -------- | -------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
showinghowfastAI/data-center-typeloadfluctuations
mitigationmeasureforAI-drivendatacenterloadvariability
|     |     |     |     |     |     |     |     | can | stress | the co-located |     | generator | (e.g., | increased |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | --------- | ------ | --------- | --- |
andassociatedpoweroscillations.Forexample,EPCPower torqueoscillations),andevaluationoftheeffectiveness
| is positioning | GFM | ESS | solutions |     | for load | variability |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheESSinsuppressingtheseoscillations.
smoothingandforreducingtheriskofloadsheddingduring
Theremainderofthispaperisorganizedasfollows.Sec-
| grid disturbances |     | [15]. | Tesla has | similarly | highlighted |     | the |     |     |     |     |     |     |     |     |
| ----------------- | --- | ----- | --------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
useofgrid-formingESSforAItrainingloadsmoothingand tion II describes the test system model. Section III presents
|     |     |     |     |     |     |     |     | case studies | in  | which | the ESS | provides | dynamic |     | support |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ------- | -------- | ------- | --- | ------- |
improvedlow-voltageride-throughcapability[16].
followingafaultandunderfastfrequencyfluctuationscaused
Motivatedbythisresearchgapandreal-worldapplications,
byAItrainingloads.SectionIVconcludesthepaper.
ourworkfocusesonhowaGFMESScanbeusedtomitigate
| the adverse | dynamic | impacts | of  | large | AI data | centers. | The |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | --- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
main objectives are to: (i) develop a high-fidelity dynamic II. DESCRIPTIONOFTHESYSTEMUNDERSTUDY
|     |     |     |     |     |     |     |     | In this section, |     | we present |     | the test | system | model, | which |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --- | -------- | ------ | ------ | ----- |
modelofahyperscaleAIdatacenteranditsinteractionwith
thebulkgrid;(ii)quantifytheimpactsoflargeloadtripping consists of: a synchronous machine (SM) connected to the
and reconnection events on system frequency and voltage; transmissiongrid,ahyperscaledatacenterwithacentralized
and(iii)assesstheeffectoffastAI-drivenloadvariabilityon UPS,asynchronousgenerationplantcollocatedwiththedata
torquefatigueintheco-locatedgeneratoratthedatacenter. center,andanESSlocatedatthedatacenter.
|     |     |     |     |     |     |     |     | Fig. 1 | illustrates | the | test | system used | in  | this study. | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ---- | ----------- | --- | ----------- | --- |
B. CONTRIBUTIONS system equivalent is modeled using a detailed synchronous
In this work, case studies are performed using electromag- generator equipped with a GOV2 governor [17], a steam
netic transient (EMT) analysis with a topologically small turbine, and an AC1A exciter model [17]. Impedances
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 29251 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
|     |     |     |     |     |     |     | ence is     | controlled | by a | proportional–integral |          | (PI)    | based     | DC  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---- | --------------------- | -------- | ------- | --------- | --- |
|     |     |     |     |     |     |     | bus voltage | regulator, |      | and the               | reactive | current | reference | is  |
controlledbyareactivepowerregulatorwithapowerrefer-
enceof0MVar,givingunitypowerfactoroperation.Rectifier
currentislimitedto1.25puusingadq-domaincurrentlimiter
|     |     |     |     |     |     |     | with active | power      | prioritization. |     | The output | inverter |           | control |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --------------- | --- | ---------- | -------- | --------- | ------- |
|     |     |     |     |     |     |     | is GFM      | with droop | control;        | the | active     | power    | reference | is      |
FIGURE1. Single-linediagramoftransmissionsystemmodel. setequalto0,andthereactivepowerreferenceiscontrolled
|     |     |     |     |     |     |     | by a PI | based | AC voltage | regulator. | The | inverter |     | current |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------- | ---------- | --- | -------- | --- | ------- |
magnitudeislimitedto1.5puusinghysteresis-basedcurrent
| Z andZ | representtwotransmissionsystempathstothedata |     |     |     |     |     | clipping[18]. |     |     |     |     |     |     |     |
| ------ | -------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
1 2
center. For a given study, the magnitudes of Z and Z are TheUPSbatteryisrepresentedasaDCvoltagesourcewith
|     |     |     |     |     | 1   | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
amagnitudeof800Vandaninternalresistanceof5m(cid:127).The
| selected to | obtain | a desired | short-circuit |     | ratio (SCR), | both |     |     |     |     |     |     |     |     |
| ----------- | ------ | --------- | ------------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
closed(SCR)andwiththemopen(SCR′).
withCB andCB batteryconverterisabidirectionalbuck-boostconverter.The
| 1   |     | 2   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
modulationindexoftheconverteriscontrolledusingbothan
A. HYPERSCALEDATACENTERMODEL activepowerregulator(tomanagecharginganddischarging)
andaDCvoltageregulator.CoordinationbetweenthetwoDC
| In this work, | we  | consider | a data | center | architecture | with |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------ | ------ | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
a centralized UPS, which is one of the most common link voltage regulators is achieved by operating the battery
configurations in large facilities. The overall data center converterataslightlylowerDCvoltagereference(0.99pu)
model is intentionally generic (i.e., not vendor-specific) and limiting the DC voltage regulator to contribute only
and was developed based on feedback from a broad group to the boost operating mode. With this arrangement, the
of industry experts, whose input helped ensure that the DC voltage regulator of the battery converter participates
architecture, load composition, and control assumptions are activelyinDCvoltageregulationwhentheDClinkvoltage
consistent with current industry practice. The model we is below 0.99 pu. This allows the UPS to maintain tight
|           |         |      |        |          |       |          | DC voltage | regulation |     | even when | the rectifier |     | is operating |     |
| --------- | ------- | ---- | ------ | -------- | ----- | -------- | ---------- | ---------- | --- | --------- | ------------- | --- | ------------ | --- |
| developed | in this | work | is not | intended | to be | an exact |            |            |     |           |               |     |              |     |
representation of any specific data center; rather, it is at its current limits, thereby minimizing the effect of deep
designed as a reasonable and transparent starting point for voltage sags in the rectifier AC voltage on the inverter AC
| thedevelopmentofsite-specificmodelssuitableforgrid-level |     |     |     |     |     |     | voltage. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
studies.
| Fig. 2 | illustrates | the | component | level | models | within |     |     |     |     |     |     |     |     |
| ------ | ----------- | --- | --------- | ----- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
the data center. This arrangement is intended to be an B. COGENERATION(SYNCHRONOUSGENERATION)
| aggregate | representation |     | of a cluster | of  | large data | centers | MODEL         |     |            |      |          |            |      |     |
| --------- | -------------- | --- | ------------ | --- | ---------- | ------- | ------------- | --- | ---------- | ---- | -------- | ---------- | ---- | --- |
|           |                |     |              |     |            |         | A synchronous |     | generation | (SG) | plant is | collocated | with | the |
builttoprovideconcurrentmaintainability.Single-phaseand
three-phase rectifiers represent to represent representative data center to illustrate both cases of a cogeneration plant
|           |           |       |        |         |               |      | or a nearby | base | generator, | such | as a | thermal | plant. | The |
| --------- | --------- | ----- | ------ | ------- | ------------- | ---- | ----------- | ---- | ---------- | ---- | ---- | ------- | ------ | --- |
| motor and | auxiliary | loads | on the | cooling | and auxiliary | sys- |             |      |            |      |      |         |        |     |
tems,andITEisconnectedtothegridviaadouble-conversion cogenerationplantismodeledasalargehigh-speedturbine,
| UPS. |     |     |     |     |     |     | suchasmightbeusedfornuclearornaturalgasgeneration. |             |                  |               |            |                     |               |        |
| ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | ----------- | ---------------- | ------------- | ---------- | ------------------- | ------------- | ------ |
|      |     |     |     |     |     |     | The inclusion                                      | of          | grid-connected   |               | generation | with                | hyperscale    |        |
|      |     |     |     |     |     |     | data centers                                       | is          | becoming         | increasingly  |            | common              | as            | it can |
|      |     |     |     |     |     |     | reduce                                             | the need    | for transmission |               | system     | upgrades            |               | which  |
|      |     |     |     |     |     |     | would otherwise                                    |             | significantly    |               | extend     | the interconnection |               |        |
|      |     |     |     |     |     |     | timeline                                           | (e.g., from | 2                | years to      | 5 to 10    | years).             | Additionally, |        |
|      |     |     |     |     |     |     | generation-rich                                    |             | areas            | are naturally | attractive |                     | options       | for    |
|      |     |     |     |     |     |     | the connection                                     |             | of hyperscale    | data          | centers,   | meaning             |               | that a |
hyperscalerislikelytobelocatedclosetoturbinegeneration
evenifthedatacenteritselfdoesnothostanyco-generation.
Thiscasestudyservesasareasonableapproximationofboth
cases.
Asix-massturbinemodelisused,providingarepresenta-
FIGURE2. Single-linediagramofdatacentermodel. tionofthemajoroscillatorymodeswithintheturbineshaft.
|     |     |     |     |     |     |     | Turbine | parameters | are | from a | real steam | turbine | [19]. | The |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------ | ---------- | ------- | ----- | --- |
Fig. 3 illustrates the control diagram for the UPS turbinegovernorandexcitercontrolsystemsarenotmodeled;
power converters. Both the UPS rectifier and inverter are while they are indeed of import in practical studies, as they
voltage-source converters represented by an average value can either improve or worsen torsional interactions [20].
models (AVM). The input rectifier control is grid-following Designing and tuning control systems for the considered
(GFL) with current vector control; the active current refer- turbineisbeyondthescopeofthestudy.
| 29252 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
| FIGURE3. | Uninterruptiblepowersupplycontroloverview. |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The aging of the steam turbine in response to cyclical C. BATTERYENERGYSTORAGESYSTEMMODEL
loads, such as those imposed by AI training loads, may AnaggregatedbatteryESSislocatedwiththedatacenter.For
be quantified using an stress/life-cycle (SN) Curve, which theESSinverter,weemployavirtualsynchronousmachine
provides the number of cycles that a given component can (VSM)–based grid-forming control. The implementation
withstandbeforeexperiencingmechanicalfailure.Inturbine corresponds to the WECC-approved generic REGFM_B1
| generators, | this failure | is usually | manifest | as  | a crack |        |       |     |         |           |            |           |     |
| ----------- | ------------ | ---------- | -------- | --- | ------- | ------ | ----- | --- | ------- | --------- | ---------- | --------- | --- |
|             |              |            |          |     |         | model, | which | was | jointly | developed | by Pacific | Northwest |     |
in the turbine shaft and effectively marks the end of NationalLaboratory(PNNL)andseveralGFMcontrolmanu-
the turbine’s useful life. Fig. 4 illustrates the exemplar facturers.Thismodelisdesignedtocapturethecharacteristic
SN curve used to perform fatigue assessments in this dynamic behavior of VSM-type GFM ESS installations.
study; this is intended to be a reasonable generic SN The detailed model specification and parameter ranges are
| curve for | a steam | turbine—specific | SN  | curves | differ |            |     |          |     |                |     |              |     |
| --------- | ------- | ---------------- | --- | ------ | ------ | ---------- | --- | -------- | --- | -------------- | --- | ------------ | --- |
|           |         |                  |     |        |        | documented |     | in [21]. | The | VSM controller |     | incorporates | the |
depending on the turbine and shaft section in question power–frequency droop characteristic as well as inertia and
and are protected propriety information held by turbine damping response functions. The control block diagram is
dδ
| manufacturers. | When | designing | a solution | to  | suppress |       |     |             |          |       |           |     | vsm = |
| -------------- | ---- | --------- | ---------- | --- | -------- | ----- | --- | ----------- | -------- | ----- | --------- | --- | ----- |
|                |      |           |            |     |          | shown | in  | Fig. 5. The | inverter | angle | expressed | as  |       |
dt
ω ,andtheinternalangularfrequencydynamicsaregiven
vsm
by,
dω
vsm
|     |     |     |     |     |     | 2H  |     | =P  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | vsm |     | ref |     |     |     |     |
dt
sD
|     |     |     |     |     |     |     |     |      | 1   |     | 2   | )(ω −ω | ),  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ------ | --- |
|     |     |     |     |     |     |     |     | −P−( |     | +D  | +   |        |     |
|     |     |     |     |     |     |     |     |      | m   | 1   | s+ω | vsm    | 0   |
|     |     |     |     |     |     |     |     |      |     | p   |     | D      |     |
(1)
|     |     |     |     |     |     |     |     | ,m ,D | ,D ,ω | ,ω  | ,ω ,P | ,Pdenoteinverter |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | ----- | ---------------- | --- |
FIGURE4. SNcurveusedtoevaluateturbineshaftfatiguefromcyclicalAI whereH p D
|     |     |     |     |     |     |     | vsm |     | 1 2 | vsm | 0 ref |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
trainingload. inertiaconstant,P−ωdroopcoefficient,dampingconstant,
transientdampingconstant,angularfrequencyofthewashout
oscillations that might cause torsional interactions, the goal filter, angular frequency, nominal angular frequency, active
istoensurethatthetorqueswithinthegeneratorsofconcern powerreference,andmeasuredactivepower.
haveamplitudesbelowtheblackdashedlineinFig.4,which
|     |     |     |     |     |     | TheterminalvoltageoftheESSinverterE |     |     |     |     |     | iscapturedby |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
indicatesthehighcyclefatiguelimit(HFCL).Torqueripple
| belowthisthresholdhasnomeasurableeffectonturbineshaft |     |     |     |     |     |     |     | dE  |     |     |         |     |       |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----- |
|                                                       |     |     |     |     |     |     |     | k   | =V  | +m  | (Q −Q), |     | (2)   |
|                                                       |     |     |     |     |     |     |     | iv  | ref | q   | ref     |     |       |
| life.                                                 |     |     |     |     |     |     |     |     | dt  |     |         |     |       |
| VOLUME14,2026                                         |     |     |     |     |     |     |     |     |     |     |         |     | 29253 |

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
| FIGURE5.      | Phaseanglegenerationofthevirtualsynchronousmachinecontrol[21]. |                                          |           |     |          |       |         |     |     |     |     |
| ------------- | -------------------------------------------------------------- | ---------------------------------------- | --------- | --- | -------- | ----- | ------- | --- | --- | --- | --- |
| where k       | ,V ,m                                                          | ,Q                                       | ,Q denote | the | integral | gain, | voltage |     |     |     |     |
| iv            | ref                                                            | q ref                                    |           |     |          |       |         |     |     |     |     |
| reference,Q−V |                                                                | droopcoefficient,reactivepowerreference, |           |     |          |       |         |     |     |     |     |
andmeasuredreactivepower.
Tolimitsteady-stateactiveandreactivepower,thevoltage
| magnitude | variation | is  | constrained | by  | the steady-state |     | reac- |     |     |     |     |
| --------- | --------- | --- | ----------- | --- | ---------------- | --- | ----- | --- | --- | --- | --- |
tivecurrentlimit,andthephase-anglevariationisconstrained
| by the steady-state |     | active | current        | limit. | A       | selectable  | PQ  |     |     |     |     |
| ------------------- | --- | ------ | -------------- | ------ | ------- | ----------- | --- | --- | --- | --- | --- |
| priority algorithm  |     | (P-    | or Q-priority) |        | is used | to allocate | the |     |     |     |     |
steadystatecurrentbetweenactiveandreactivecomponents.
| The PWM | layer | applies | current | clipping |     | to cap | transient |     |     |     |     |
| ------- | ----- | ------- | ------- | -------- | --- | ------ | --------- | --- | --- | --- | --- |
over-currentduringfaults.Additionally,toensuretheinverter
| remains     | synchronized |              | after fault | clearing, |             | a phase-locked |         |     |     |     |     |
| ----------- | ------------ | ------------ | ----------- | --------- | ----------- | -------------- | ------- | --- | --- | --- | --- |
| loop (PLL)  | is used      | to           | lock the    | inverter  | internal    | phase          | angle   |     |     |     |     |
| to prevent  | loss of      | synchronism. |             | This      | is achieved | by             | feeding |     |     |     |     |
| forward the | grid         | voltage      | angle       | measured  | by          | the PLL        | (δ )    |     |     |     |     |
PLL
asshowninFig.5.
III. CASESTUDIES
| In this section, |     | two main | applications |     | of dynamic |     | support |     |     |     |     |
| ---------------- | --- | -------- | ------------ | --- | ---------- | --- | ------- | --- | --- | --- | --- |
fordatacentersareconsidered:fastfrequencyresponseand
|     |     |     |     |     |     |     |     | FIGURE6. EffectsofSGinertiaon,(a)frequency,(b)POCvoltage. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
oscillationsuppression.Inbothscenarios,thekeycapability
inresponsetofault-induceddatacentertripping.
providedbytheESSisfastresponseandtheabilitytosupply
significantactivepower.
thiscaserepresentsdelayedclearingasmightbecausedbya
A. POST-FAULTFREQUENCYREGULATION failedcircuitbreakerorcommunicationslink.Therectifiers
In this case study, we evaluate the ability of the ESS to for the cooling loads and the UPS use undervoltage relays
stabilize the bulk system frequency following the tripping thatdisconnectifthePOCvoltageremainsbelow0.8p.u.for
|             |        |      |     |          |     |                |     | more than | 50 ms. We consider | scenarios with | and without |
| ----------- | ------ | ---- | --- | -------- | --- | -------------- | --- | --------- | ------------------ | -------------- | ----------- |
| of the data | center | load | in  | response | to  | a transmission |     |           |                    |                |             |
systemfault.Thisisasimilarscenariotothegigawatt-scale automatic reconnection of the UPS rectifier; when enabled,
load drops experienced in both the Texas and Eastern itreclosesoncethePOCvoltagehasrecoveredto1.0p.u.for
atleast1s.
| Interconnections |         | [12],  | [13]. In    | the following |            | studies, | SCR       |     |     |     |     |
| ---------------- | ------- | ------ | ----------- | ------------- | ---------- | -------- | --------- | --- | --- | --- | --- |
| is 6 and         | SCR′ is | 3. The | synchronous |               | generators |          | in Fig. 1 |     |     |     |     |
have a total nominal power of 8 GW with a 5% governor 1) WITHOUTAUTOMATICUPSRE-CONNECTIONAFTER
| droop. A | 2.5 GW | constant-power |     | load | is connected |     | on the | FAULT |     |     |     |
| -------- | ------ | -------------- | --- | ---- | ------------ | --- | ------ | ----- | --- | --- | --- |
SG side. The data center includes 140 MW of cooling load The system inertia constant is varied to emulate grids with
and 1.1 GW of ITE load. Assume a three-phase voltage differentinertialevels.WhenanESSisincluded,itssettings
faultoccursonthetransmissionlineandlasts320ms.Most are:m =0.01,H = 10,D = 20,D = 200,ω = 50.
|     |     |     |     |     |     |     |     | p   | vsm | 1 2 | D   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
transmission faults are cleared in less than 100 ms and so Figure 6 shows the post-fault frequency and the data center
| 29254 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
POC voltage across inertia levels, with and without a ESS.
Lowerinertiayieldslargerfrequencyexcursionsandslower
recovery:thefrequencypeakreaches61.22HzatH =2s,
sg
compared with 60.75 Hz at H = 4 s. An inertia value of
sg
H = 4 s approximates a system dominated by traditional
sg
synchronousgeneration.AvalueofH = 2sapproximates
sg
a system with roughly 50% penetration of inverter-based
resources,withtheassumptionthattheassumptionthatthese
resourcesdo notparticipate ininertial response.In thelow-
inertiacaseH =2s,addinganESSreducesthefrequency
sg
peak to 60.86 Hz with a 400 MW rating and to 60.55 Hz FIGURE7. Relationoffrequencyrisefromfault-inducedtrippingofdata
centerloadtoNERCPRC-024overfrequencyride-throughrequirements.
withan800MWratingandshortensthesettlingtime.Inthe
no-ESScase,thepost-faultdata-centerPOCvoltagesettlesat
1.07puratherthan1.0pubecausea350MVAshuntcapacitor
is installed at the POC for steady-state voltage support.
Whenthedatacenterloadtripsafterthefault,thecapacitor
overcompensatesandthebusvoltagerisesto1.07p.u.Witha
ESS,thecapacitorisunnecessary;theESSprovidesreactive
powersupport,maintainingbothpre-andpost-faultvoltages
at1.0p.u.
We study a low-reserve scenario with 4 GW online
generation (inertia H = 4 s). A 1.5 GW load is connected
upstream, and the data center parameters are unchanged.
FIGURE8. EffectsofESSinertiaonfrequencyinresponseto
Fig. 7 illustrates the effect of ESS capacity on grid
fault-induceddatacentertripping.
frequency rise following fault-induced tripping of the data
center load. Figure 7 shows the grid-frequency rise after
fault-induced tripping of the data-center load for different
ESS power ratings. Without ESS, the frequency peaks at
61.98 Hz and settles at 61.00 Hz. Adding ESS reduces the
overfrequency: with a 400 MW ESS, the peak drops to
61.62 Hz and the steady-state frequency to 60.73 Hz; with
an 800 MW ESS, the peak further drops to 61.25 Hz and
the steady-state frequency to 60.46 Hz. Fig. 7 illustrates
how the overfrequency conditions compare to the over
frequencyride-through(FRT)limitsdefinedinNERCPRC-
024 [22]. The limits vary by interconnection; values for
FIGURE9. EffectsofESSdroopcoefficientonfrequencyinresponseto
the Western Interconnection (WI) are chosen here simply fault-induceddatacentertripping.
for illustration. Observe that, without a ESS (0 MW of
capacity), the overfrequency condition exceeds the limits
that generators are required to ride through. This indicates
a serious reliability risk—such a condition could cause
widespread tripping of generation units and subsequent
cascadingoutages.A400MWESSisjustsufficienttobring
the excursion within the tolerable limits, while an 800 MW
ESS provides a more robust margin, including against
potential future reductions in system inertia and unforeseen
contingencies.
Under the same base case with a 4 GW synchronous
machine, a 1.5 GW constant-power load, and an 800 MW
FIGURE10. EffectsofESSω Donfrequencyinresponsetofault-induced
ESS, we adjust the ESS control parameters to study their datacentertripping.
impactonthefrequencyresponsetofault-induceddatacenter
tripping. Fig. 8 shows the results of varying the ESS inertia
constantHwithm = 1%,ω = 50.Itcanbeobservedthat it is 1 or 5. With H = 1,ω = 50, we vary the active
p D D
changingtheinertiaconstantdoesnotsignificantlyaffectthe power-frequency droop coefficient of the ESS m , and the
p
frequencybehavior.Thesecondaryfrequencyriseisslightly correspondingfrequencyresponseisshowninFig.9.Itcan
improvedwhentheinertiaconstantis10comparedtowhen be observed that changing the m significantly affects the
p
VOLUME14,2026 29255

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
| FIGURE11. | EffectofSGinertiaon,(a)frequency,(b)POCvoltage. |     |     |     |     |
| --------- | ----------------------------------------------- | --- | --- | --- | --- |
FIGURE12. ResponsetofastAI-trainingloadfluctuations(16Hz),
(a)data-centerPCCactivepower,(b)co-generatorelectricaltorque,
(c)torsionalshafttorque(masses3–4).
frequencyrecovery:thesteadystatefrequencyis60.73Hzfor
| m = 5%,60.67Hzform |             | = 3%,60.46Hzform |             |     | =         |
| ------------------ | ----------- | ---------------- | ----------- | --- | --------- |
| p                  |             | p                |             |     | p 1%.     |
| In addition,       | the smaller | the m is,        | the shorter | the | frequency |
p
| recovery | time becomes. | With m | = 1%,H | = 10, | we vary |
| -------- | ------------- | ------ | ------ | ----- | ------- |
p
ω
| the angular | frequency | on the washout | block |     | D , and the |
| ----------- | --------- | -------------- | ----- | --- | ----------- |
correspondingfrequencyresponseisshowninFig.9.Itcan
| beobservedthatchangingω |     | doesnotsignificantlyaffectthe |     |     |     |
| ----------------------- | --- | ----------------------------- | --- | --- | --- |
D
frequencybehavior.Thefrequencyrecoveryisslightlybetter
| dampedforlargervaluesofω |     | .   |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- |
D
2) WITHAUTOMATICUPSRE-CONNECTIONAFTERFAULT
WiththeUPSre-connectionfunctionenabled,Fig.11shows
FIGURE13. EffectsofESSonturbineagingintroducedby90to100%AI
thepost-faultSGfrequencyandthedata-centerPOCvoltage trainingloadwithfastfrequencyof16Hz.
| across inertia | levels, | with and without | an  | ESS. | Without an |
| -------------- | ------- | ---------------- | --- | ---- | ---------- |
ESS,thedatacenterloaddropfollowingthefaultproducesa
frequencyovershoot:thepeakreaches61.033HzatH =2s B. OSCILLATIONSUPPRESSIONFORCOGENERATION
sg
| and 60.737 | Hz at H | = 4 s. | In the | low-inertia | case |
| ---------- | ------- | ------ | ------ | ----------- | ---- |
sg OPERATION
(H sg = 2s),a400MWESSreducesthepeakto60.554Hz, Available AI training load data indicate that typical hyper-
and an 800 MW ESS further reduces it to 60.500 Hz, scale AI workloads exhibit two dominant time scales: (i) a
demonstratingfastfrequencyresponseandthevalueofESS ‘‘slow’’ component on the order of seconds, corresponding
inlowinertiasystems.ReconnectingtheUPSafterthefault to aggregate job/mini-batch dynamics, with characteristic
produces a frequency dip: the frequency nadir is 54.33 Hz frequenciesroughlyinthe0.1–1Hzrange,and(ii)a‘‘fast’’
at H sg = 2 and the frequency nadir is 59.03 Hz at H sg = component on the order of milliseconds, associated with
4. This suggests that, in a low inertia system, the simple accelerator/cluster-levelactivity,withdominantcomponents
approachofquicklyreconnectingtheloadpostfaultmaybe broadlyinthe5–30Hzrange.Inthisapplication,weevaluate
insufficient to avoid significant frequency fluctuations. The the effects of rapid, periodic variations in data center active
low-inertia case H = 2 violates the frequency capability power consumption on the co-generator. The concern is
sg
curve specified by NERC PRC-024. A ESS addresses this that these variations will cause torques in the turbine that
issue by raising the post-fault frequency nadir to 58.16 Hz exceed its mechanical limits, resulting in severe damage
with a 400 MW rating and to 59.77 Hz with an 800 MW to a generation asset that is critical to transmission system
rating.Meanwhile,thesettlingtimeisreducedwiththeESS reliability. Consideration is given to recent advances in
allocation. ITE-level controls, such as software-level mitigations and
29256 VOLUME14,2026

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
| FIGURE14. | ResponsetofastAI-trainingloadfluctuations(25.6Hz), |     |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(a)data-centerPCCactivepower,(b)co-generatorelectricaltorque,
(c)torsionalshafttorque(masses2–3).
| graphics    | processing  | unit         | (GPU)     | smoothing, |              | which         | can   |     |     |     |     |
| ----------- | ----------- | ------------ | --------- | ---------- | ------------ | ------------- | ----- | --- | --- | --- | --- |
| somewhat    | reduce      | the          | amplitude | of these   | fluctuations |               | [23]. |     |     |     |     |
| Our results | indicate    | that,        | even      | with       | these        | improvements, |       |     |     |     |     |
| additional  | oscillation | suppression, |           | such       | as that      | provided      | by    |     |     |     |     |
theESS,isnecessarytoavoidturbinedamage.
The co-generator is rated at 372 MVA. The AI training FIGURE15. ResponsetoanexampleAIdatacenterloadprofilefrom[3],
loadhasanominalpowerof1.1GW,withafastcomponent (a)AItrainingloadprofile,(b)activepoweratPCC,(c)frequency,
(d)torsionalshafttorque(masses3-4).
| at 16 Hz | and a | slow component |     | at 0.5333 |     | Hz; the | resting |     |     |     |     |
| -------- | ----- | -------------- | --- | --------- | --- | ------- | ------- | --- | --- | --- | --- |
loadis0.99GW.Afrequencyof16Hzisselectedtoprovide
| conservative | results | as  | it coincides | with | a   | lightly | damped |     |     |     |     |
| ------------ | ------- | --- | ------------ | ---- | --- | ------- | ------ | --- | --- | --- | --- |
• EachcycleofthefastfrequencyintheAItrainingload
| shaft mode. | The | slow | component | is selected |     | to be | roughly |     |     |     |     |
| ----------- | --- | ---- | --------- | ----------- | --- | ----- | ------- | --- | --- | --- | --- |
istreatedasonecycleintermsoftheSNcurve.
anorderofmagnitudelowerandanintegerdivisorofthefast
• Thepeaksteadystatetorquerippleisthevalueevaluated
frequency.Fig.12showsthedata-centerPCCactivepower,
againsttheSNcurve
| the co-generator                                    |     | electrical | torque, | and | the | torsional | shaft |              |                     |          |             |
| --------------------------------------------------- | --- | ---------- | ------- | --- | --- | --------- | ----- | ------------ | ------------------- | -------- | ----------- |
|                                                     |     |            |         |     |     |           |       | The SN curve | is derated linearly | based on | the average |
| torquebetweenmasses3and4.Althoughothershaftsections |     |            |         |     |     |           |       | •            |                     |          |             |
torqueloading.Inotherwords,iftheaveragetorqueon
alsoexperiencesignificanttorque,the3–4sectionisthemost
thegeneratoris0.5pu,theSNcurveintroducedinFig.4
| severe; | for brevity, | only | this | torque | is plotted. | Physically, |     |     |     |     |     |
| ------- | ------------ | ---- | ---- | ------ | ----------- | ----------- | --- | --- | --- | --- | --- |
it corresponds to the torque between the two low-pressure isshifteddownwardsby0.5pu
turbine stages. Fig. 12 shows that adding an 800 MW ESS Employingtheseassumptions,Fig.13illustratestheeffects
at the data center significantly reduces oscillations in PCC of the torques imposed by various AI training loads on
activepower,co-generatorelectricaltorque,andthetorsional the turbine life, both with and without the ESS included.
torquebetweenmasses3and4. Observe that the reduction in torque provided by the ESS
The torque waveforms illustrated in Fig. 12 can be used is sufficient to achieve a value below the endurance limit,
to perform an initial assessment of the turbine’s ability minimizing the risk that the AI training load profile will
to withstand the torque oscillations without experiencing meaningfully affect turbine life. Additionally, observe that,
shaft damage. That said, SN curves are intended to capture with the relatively high frequency of the AI loading, the
the fatigue induced by a simple periodic load and do not region where the torque ripple ages the shaft but does not
fully capture how the turbine will wear when responding resultinanear-termfailureissmall(torquerippleshereareall
to waveforms with broadband subsynchronous frequency near1p.u.).Theshorttimetofailureassociatedwithtorque
contentsuchasAItrainingwaveforms.Thus,wemustmake ripples in the range of 1 to 1.5 pu suggests that all that is
someconservativeassumptions:
|               |     |     |     |     |     |     |     | needed to determine | whether an oscillation | is acceptable | is    |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ---------------------- | ------------- | ----- |
| VOLUME14,2026 |     |     |     |     |     |     |     |                     |                        |               | 29257 |

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
theHFCLthreshold—loadingsthatareevenslightlyoverthe this article. The authors would like to especially thank
HFCLtranslatetoturbinelifetimesofmereminutesorhours. Siva Prakash of Amazon Web Services, Katelynn Vance of
Thiscontrastswithsomehistoricalsourcesofturbinefatigue, DominionEnergyVirginia,KeithWatsonofEaton,Andrew
suchaslineswitching[24]. IsaacsofElectranix,ParagMitraandLakshmiSundareshof
UnderanITloadprofilewithfast(25.6Hz,thefrequency the Electric Power Research Institute, Prashant Kansal of
ofanotherlightlydampedshaftmode)andslow(0.5115Hz) the Electric Reliability Council of Texas, Paul Ortmann
variation components, Fig. 14 shows the simulated data of Idaho Power, Scot Heath of Microsoft, Sumek Elimban
center PCC active power, cogenerator electrical torque, and ofReal-TimeDigitalSimulators,SaiGopalVennelagantiof
the torsional response of shaft sections II–III, with and Tesla,PrasadN.EnjetiandXiaoyangWangofTexasA&M
withoutESSdeployment.TheresultsindicatethattheBESS University, and Greg Ratcliffe of Vertiv. Inputs from these
mitigatesoscillationsunderthesefastfrequencyfluctuations. individuals helped assure the relevance of their research to
Inadditiontotheperiodicvariationsindatacenteractive currentindustrypractices.
| power consumption, |     | we  | also | verify the ESS’s | effectiveness |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ---- | ---------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
insmoothinganapproximationofarealAIdatacenterload
REFERENCES
| profile [3]. | Figure | 15(a)    | shows  | the AI training |       | load profile, |                |              |             |        |               |         |               |
| ------------ | ------ | -------- | ------ | --------------- | ----- | ------------- | -------------- | ------------ | ----------- | ------ | ------------- | ------- | ------------- |
|              |        |          |        |                 |       |               | [1] O. Isakov, | A.           | Frishman,   | and D. | Malka, ‘‘Data | center  | four-channel  |
| which has    | been   | linearly | scaled | to a peak       | value | of 1.1 GW.    |                |              |             |        |               |         |               |
|              |        |          |        |                 |       |               | multimode      | interference | multiplexer |        | using silicon | nitride | technology,’’ |
Note that, in practice, fluctuations from individual feeds Nanomaterials,vol.14,no.6,p.486,Mar.2024.
|                     |      |       |                |               |     |          | [2] E. Ioudashkin |              | and D. Malka, | ‘‘High-performance |         | O-band  | angled mul-   |
| ------------------- | ---- | ----- | -------------- | ------------- | --- | -------- | ----------------- | ------------ | ------------- | ------------------ | ------- | ------- | ------------- |
| will exhibit        | some | level | of destructive | interference, |     | making   |                   |              |               |                    |         |         |               |
|                     |      |       |                |               |     |          | timode            | interference | splitter      | with buried        | silicon | nitride | waveguide for |
| this a conservative |      | test. | Using          | this profile, | we  | simulate |                   |              |               |                    |         |         |               |
advanceddatacenteropticalnetworks,’’Photonics,vol.12,no.4,p.322,
| the following |     | quantities | at  | the data center | PCC | and the | Mar.2025. |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | --------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- |
co-locatedgenerator:(b)activepoweratthePCC,(c)system [3] LargeLoadsTaskForce.(2025).CharacteristicsandRisksofEmerging
frequency, and (d) torsional shaft torque (between masses LargeLoads.[Online].Available:https://www.nerc.com/comm/RSTCRe
viewItems/3DocWhite%20Paper%20Characteristics%20and%20Risks%
3–4 of the generator shaft) both without ESS and with 20of%20Emerging%20Large%20Loads.pdf
an800MWESSprovidinggrid-formingsupport.Theresults [4] S.JonesandS.Vennelaganti.(2025).BatteryStorageApplicationsAtData
in Figs.15(b–d) demonstrate that: Without ESS, the PCC Centers.[Online].Available:https://www.nerc.com/comm/RSTC/LLTF/
LLTFAprilMeeting&TechnicalWorkshopPresentations.pdf
experiencesrapid,irregularpowerfluctuationsdrivenbythe
[5] NERC.(2023).WhitePaper:GridFormingFunctionalSpecificationsfor
| AI training | load, | which | translate | into noticeable |     | frequency |     |     |     |     |     |     |     |
| ----------- | ----- | ----- | --------- | --------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
BPS-ConnectedBatteryEnergyStorageSystems.[Online].Available:http
variationsandelevatedtorsionaltorqueoscillations.Withthe s://www.nerc.com/comm/RSTCReliabilityGuidelines/WhitePaperGFMF
unctionalSpecification.pdf
ESSinservice,thefastpowerfluctuationsatthedatacenter
[6] M.Chen,C.Gao,M.Shahidehpour,Z.Li,S.Chen,andD.Li,‘‘Internet
| PCC are | substantially |     | mitigated. | As a result, | the | frequency |     |     |     |     |     |     |     |
| ------- | ------------- | --- | ---------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
datacenterloadmodelingfordemandresponseconsideringthecoupling
variations induced by the AI training load are reduced, and ofmultipleregulationmethods,’’IEEETrans.SmartGrid,vol.12,no.3,
the torsional torque oscillations in the co-generator are also pp.2060–2076,May2021.
|     |     |     |     |     |     |     | [7] A. Radovanovic, |     | B. Chen, | S. Talukdar, |     | B. Roy, A. | Duarte, and |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | -------- | ------------ | --- | ---------- | ----------- |
significantlydamped.
|     |     |     |     |     |     |     | M. Shahbazi, |               | ‘‘Power modeling | for         | effective | datacenter | planning and |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ---------------- | ----------- | --------- | ---------- | ------------ |
|     |     |     |     |     |     |     | compute      | management,’’ |                  | IEEE Trans. | Smart     | Grid, vol. | 13, no. 2,   |
pp.1611–1621,Mar.2022.
IV. CONCLUSION
|     |     |     |     |     |     |     | [8] P. Ren, | W. Sun, | Y. Wang, | and G. | Harrison, | ‘‘Grid frequency | stability |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------- | ------ | --------- | ---------------- | --------- |
AnEMTdata-centermodel—includingaUPS,cogenerator,
supportpotentialofdatacenter:Aquantitativeassessmentofflexibility,’’
| cooling | system, | and ESS—that |     | explicitly | represents | power |     |     |     |     |     |     |     |
| ------- | ------- | ------------ | --- | ---------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
2025,arXiv:2510.01050.
convertersandtheircontroldynamicswasdevelopedinthis [9] P.T.Krein,‘‘Datacenterchallengesandtheirpowerelectronics,’’CPSS
work.Usingthismodel,weassesstheimpactofdatacenter Trans.PowerElectron.Appl.,vol.2,no.1,pp.39–46,2017.
low-voltage ride-through and examine how fast-varying [10] L. L. Qi, H. Suryanarayana, Y. Zhang, T. Jiang, and S. Colombi,
‘‘Modeling,simulation,andprotectionofgridforminginverter-basedring
data-center AI training loads stress the cogenerator. Under configurationdatacenter,’’inProc.IEEEInd.Appl.Soc.Annu.Meeting
low-voltage fault conditions, EMT simulations show that (IAS),Oct.2022,pp.1–7.
protection-driventrippingofdata-centerloadscancausefre- [11] J. Sun, S. Wang, J. Wang, and L. M. Tolbert, ‘‘Dynamic model and
|     |     |     |     |     |     |     | converter-based |     | emulator | of a data | center power | distribution | system,’’ |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --------- | ------------ | ------------ | --------- |
quencyexcursionsthatviolatetheNERCPRC-024frequency
IEEETrans.PowerElectron.,vol.37,no.7,pp.8420–8432,Jul.2022.
| capability | curve, | risking | generator | trips. | Deploying | an ESS |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | --------- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
[12] NorthAmericanElectricReliabilityCorporation.(2025).IncidentReview:
substantiallymitigatestheseimpacts—raisingthefrequency ConsideringSimultaneousVoltage-SensitiveLoadReductions.[Online].
peak/nadirandshorteningthesettlingtime—therebyimprov- Available:https://www.nerc.com/pa/rrm/ea/Documents/IncidentRevie
wLargeLoadLoss.pdf
| ing post-fault |     | frequency | recovery | and preventing |     | potential |                  |             |         |           |         |       |            |
| -------------- | --- | --------- | -------- | -------------- | --- | --------- | ---------------- | ----------- | ------- | --------- | ------- | ----- | ---------- |
|                |     |           |          |                |     |           | [13] Electricity | Reliability | Council | of Texas. | (2025). | ERCOT | Large Load |
widespreadoutages.TheESSalsosuppresseshigh-frequency Loss/ReductionEvents2020–2024.[Online].Available:https://www.er
AI-trainingloadfluctuations,whichinturnreducestorsional cot.com/files/docs/2025/02/28/ERCOT-Large-Load-EventsLFLTFMarc
h2025.pptx
| shaft-torque | oscillations |     | in nearby | generators | to  | below the |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | --------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[14] EnergySystemsIntegrationGroup.(Aug.2024).ESIGOscillationsGuide.
HFCLandavoidssignificantreductionsinturbineshaftlife.
[Online].Available:https://www.esig.energy/wp-content/uploads/2024/
08/ESIG-Oscillations-Guide-2024.pdf
ACKNOWLEDGMENT [15] EPCPower.SolvingAIDataCenterChallengesWithAgileGrid-Forming
Bess.Accessed:Dec.31,2025.[Online].Available:https://www.epcpow
| A diverse | set | of industry | experts | graciously |     | gave input |     |     |     |     |     |     |     |
| --------- | --- | ----------- | ------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
er.com/insights/solving-ai-data-center-challenges-with-agile-grid-formi
| on the | development |     | of the | data center | models | used in | ng-bess |     |     |     |     |               |     |
| ------ | ----------- | --- | ------ | ----------- | ------ | ------- | ------- | --- | --- | --- | --- | ------------- | --- |
| 29258  |             |     |        |             |        |         |         |     |     |     |     | VOLUME14,2026 |     |

B.A.Rossetal.:UsingGFMESStoProvideDynamicActivePowerSupportforHyperscaleDataCenter
[16] TeslaMegapack.(2024).AIDataCenterLoadCharacteristics.Accessed: UDOKA C. NWANETO (SeniorMember,IEEE)
Jan.1,2025.[Online].Available:https://x.com/TeslaMegapack/status/1 received the B.Eng. degree (Hons.) in electri-
989073638273012133 cal engineering from the University of Nigeria,
[17] ManitobaHydroInternationalLtd.(2024).PSCADUser’sGuide.[Online]. Nsukka, in 2013, the M.Sc. degree (Hons.) in
Available:https://www.pscad.com/knowledge-base/article/160 new and renewable energy from the College
[18] W.Du,Q.Nguyen,Y.Liu,andS.M.Mohiuddin,‘‘Acurrentlimiting
|         |          |                 |                  |              |           |     |     | of      | St. Hild | and St. Bede,  | Durham | University,      |
| ------- | -------- | --------------- | ---------------- | ------------ | --------- | --- | --- | ------- | -------- | -------------- | ------ | ---------------- |
| control | strategy | for single-loop | droop-controlled | grid-forming | inverters |     |     |         |          |                |        |                  |
|         |          |                 |                  |              |           |     |     | Durham, |          | U.K., in 2018, | and    | the Ph.D. degree |
underbalancedandunbalancedfaults,’’inProc.IEEEEnergyConvers.
|     |     |     |     |     |     |     |     | in  | electrical | and computer | engineering | from the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ----------- | -------- |
Congr.Expo.(ECCE),Oct.2022,pp.1–7.
|              |           |           |                     |     |                   |     |     | University |     | of Calgary, | Calgary, | AB, Canada, |
| ------------ | --------- | --------- | ------------------- | --- | ----------------- | --- | --- | ---------- | --- | ----------- | -------- | ----------- |
| [19] ‘‘First | benchmark | model for | computer simulation |     | of subsynchronous |     |     |            |     |             |          |             |
resonance,’’ IEEE Trans. Power App. Syst., vol. PAS-96, no. 5, in2022.From2016to2018,hewasaGraduate
|     |     |     |     |     |     | Assistant | with the | Department | of  | Electrical Engineering, |     | University of |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | ----------------------- | --- | ------------- |
pp.1565–1572,May1977.
Nigeria.FromApril2020toNovember2020,hewasaMitacsAccelerate
| [20] P. Kundur, | Power | System Stability | and Control. | New | York, NY, USA: |     |     |     |     |     |     |     |
| --------------- | ----- | ---------------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
InternwithAudaciousEnergyInc.,Calgary,whereheconductedindustry-
McGraw-Hill,1994.
basedresearch,whichfocusedonthedevelopmentoftheInternet-of-Things-
[21] W.Duetal.,‘‘Virtualsynchronousmachinegrid-forminginvertermodel
specification (REGFM_B1),’’ Nat. Renew. Energy Lab., Golden, CO, based microgrid control products. Since 2018, he has been a Lecturer II
USA,Tech.Rep.UNIFI-2024-6-1,2024. withtheDepartmentofElectricalEngineering,UniversityofNigeria.Heis
[22] NorthAmericanElectricReliabilityCorporation,‘‘Generatorfrequency currentlyaResearchEngineerwiththeEnergySystemsResilienceGroup,
and voltage protective relay settings,’’ North Amer. Electr. Rel. Corp., Pacific Northwest National Laboratory, Richland, WA, USA, where he
Washington,DC,USA,Tech.Rep.PRC-024-2,2015. servesasaprincipalinvestigatorandtaskleadonmultipleU.S.Department
[23] E.Choukseetal.,‘‘PowerstabilizationforAItrainingdatacenters,’’2025, ofEnergy–fundedresearchprojects.Heistheauthorofsixjournalarticles
arXiv:2508.14318.
andtenconferencepapers.Heisacontributortothedevelopmentofthe
[24] ElectricPowerResearchInstitute.(2006).TorsionalInteractionBetween
WesternElectricityCoordinatingCouncil(WECC)-approvedREGFM_B1
ElectricalNetworkPhenomenaandTurbine-GeneratorShafts.[Online]. model that was recently implemented in major commercial simulation
Available:https://www.epri.com/research/products/1013460 softwaretools.HeisalsoamajorcontributortothedevelopmentofWECC-
|     |     |     |     |     |     | approved           | REGFM_C1 | and                     | REPCGFM_C1 | models,             | which   | were recently   |
| --- | --- | --- | --- | --- | --- | ------------------ | -------- | ----------------------- | ---------- | ------------------- | ------- | --------------- |
|     |     |     |     |     |     | implemented        | in major | commercial              |            | simulation software |         | tools. His main |
|     |     |     |     |     |     | research interests |          | include electromagnetic |            | transient,          | dynamic | phasor and      |
staticphasor-basedmodelingofpowersystems,co-simulationofelectrical
|     |     |     |     |     |     | distribution | and transmission |     | systems, | the control | of renewable | energy |
| --- | --- | --- | --- | --- | --- | ------------ | ---------------- | --- | -------- | ----------- | ------------ | ------ |
systems,modularmultilevelconverters,andtheInternet-of-Thingsenabled
|     |     |     |     |     |     | microgrids. | He has | been a | recipient | of numerous | awards, | including the |
| --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | --------- | ----------- | ------- | ------------- |
OutstandingPerformanceAward(OPA)fromthePacificNorthwestNational
Laboratory,theNSERCAlexanderGrahamBellDoctoralScholarship,the
|     |     |     |     |     |     | Commonwealth | Shared | Scholarship, |     | and the Alberta | Innovates | Graduate |
| --- | --- | --- | --- | --- | --- | ------------ | ------ | ------------ | --- | --------------- | --------- | -------- |
StudentDoctoralScholarship.
|     |     | BRETT    | A. ROSS (Member, | IEEE)          | received the     |     |     |     |     |     |     |     |
| --- | --- | -------- | ---------------- | -------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | B.S.E.E. | degree from      | the University | of Central       |     |     |     |     |     |     |     |
|     |     | Florida, | Orlando, FL,     | USA,           | in 2019, and the |     |     |     |     |     |     |     |
SHEIKMOHAMMADMOHIUDDIN(Member,
|     |     | M.S.E.E. | degree from | the University | of Idaho, |     |     |     |     |     |     |     |
| --- | --- | -------- | ----------- | -------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
IEEE)receivedtheB.Sc.degreeinelectricaland
Moscow,ID,in2025.HeiscurrentlyanElectrical
electronicengineeringfromRajshahiUniversityof
|     |     | Engineer | with the Pacific | Northwest | National |     |     |     |     |     |     |     |
| --- | --- | -------- | ---------------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Laboratory (PNNL). Prior to joining PNNL, Engineering&Technology,Bangladesh,in2013,
hewaswithDukeEnergy,LakeMary,FL,andas themaster’sdegreeinelectricalengineeringfrom
|     |     |     |     |     |     |     |     | the | University | of New | South | Wales (UNSW), |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ----- | ------------- |
aLeadResearchEngineerwithSchweitzerEngi-
|     |     |     |     |     |     |     |     | Australia, |     | in 2017, and | the | Ph.D. degree in |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | --------------- |
neeringLaboratoriesInc.,Pullman,WA,USA.His
electricalengineeringfromtheStevensInstituteof
researchinterestsincludepowersystemsapplicationsofpowerelectronics,
Technology,in2021.
powersystemprotection,andpowersystemtransients.
HeiscurrentlyaSeniorPowerSystemResearch
|     |     |     |     |     |     | Engineer          | with the      | Pacific     | Northwest | National        | Laboratory.   | His research     |
| --- | --- | --- | --- | --- | --- | ----------------- | ------------- | ----------- | --------- | --------------- | ------------- | ---------------- |
|     |     |     |     |     |     | interests include | fault-ride    |             | through   | control design  | for inverters | and grid-        |
|     |     |     |     |     |     | enhancing         | technologies, | control     | design    | for solid-state |               | transformers and |
|     |     |     |     |     |     | high-voltage      | multi-level   | converters, |           | and distributed | control       | for AC/DC        |
microgrids.
Dr.MohiuddinreceivedtheBestPaperAwardatthe2021IEEEPESISGT
AsiaConference.
ALEXANDREB.NASSIF(SeniorMember,IEEE)
XUE LYU (Member, IEEE) received the Ph.D. receivedthePh.D.degreefromtheUniversityof
degree in electrical engineering from The Hong Alberta,Canada.HejoinedthePacificNorthwest
Kong Polytechnic University, in 2019. She is NationalLaboratory,inJune2024,whereheleads
currently a Senior Research Engineer with the orsupportresilienceeffortsinjurisdictions,such
Pacific Northwest National Laboratory (PNNL). asPuertoRico,Hawaii,andinseveralcountries
PriortojoiningPNNL,shewasaResearchAsso- inCentralAmerica.Healsosupportsnationwide
ciatewiththeUniversityofWisconsin–Madison, DOE efforts related to grid modernization and
from2021to2022,andaPostdoctoralFellowwith transmission planning. Prior to joining PNNL,
TheUniversityofHongKong,from2019to2020. hebuiltacareerworkingforthreemajorutilities
Herresearchinterestsincludemodelingandcon- in North America and supporting system expansion. He was the General
trol for inverter-based resources integration in power systems, with a Chair of the 2023 PES ISGT-LA. He holds editorial positions in IEEE
particularemphasisonenhancinggridstabilityandresilience.Shereceived TRANSACTIONSONPOWERDELIVERYandIEEETRANSACTIONSONPOWERSYSTEMS.
theBestPaperAwardatthe2024IEEEPESGeneralMeeting.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     | 29259 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |