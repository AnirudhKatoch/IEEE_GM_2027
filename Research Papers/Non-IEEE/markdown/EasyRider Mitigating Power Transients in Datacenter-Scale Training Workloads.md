|     |                       | EasyRider:       |     | Mitigating |                    | Power | Transients |                    | in  |     |
| --- | --------------------- | ---------------- | --- | ---------- | ------------------ | ----- | ---------- | ------------------ | --- | --- |
|     |                       | Datacenter-Scale |     |            | Training           |       | Workloads  |                    |     |     |
|     |                       | DillonJensen     |     |            | ObiNnoromJr.       |       |            | GrantWilkins       |     |     |
|     | dillonj0@stanford.edu |                  |     |            | obdk@stanford.edu  |       |            | gfw@stanford.edu   |     |     |
|     | StanfordUniversity    |                  |     |            | StanfordUniversity |       |            | StanfordUniversity |     |     |
Stanford,California,USA Stanford,California,USA Stanford,California,USA
|     |                       | HugoBudd |     |     | RamRajagopal       |     |     | JuanRivas-Davila     |     |     |
| --- | --------------------- | -------- | --- | --- | ------------------ | --- | --- | -------------------- | --- | --- |
|     | hugobudd@stanford.edu |          |     |     | ramr@stanford.edu  |     |     | jmrivas@stanford.edu |     |     |
|     | StanfordUniversity    |          |     |     | StanfordUniversity |     |     | StanfordUniversity   |     |     |
6202 rpA 61  ]RA.sc[  1v22551.4062:viXra Stanford,California,USA Stanford,California,USA Stanford,California,USA
PhilLevis
pal@cs.stanford.edu
StanfordUniversity
Stanford,California,USA
Abstract
|     |     |     |     |     |     | 1.00 |     |     | 40s fall-off |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------------ | --- |
Large-scaleAImodeltrainingworkloadsusethousandsof
95% decay
).u.p( rewoP 0.75
GPUsoperatingintightlysynchronizedloops.Duringsyn-
chronouscommunication,start-up,shut-down,andcheck-
0.50
pointing,GPUpowerconsumptioncanswingfrompeakto
idlewithinmilliseconds.Theselargeandrapidloadswings
0.25
| endanger                                             | grid | infrastructure | as they | induce steep | power |      |     |     |     |     |
| ---------------------------------------------------- | ---- | -------------- | ------- | ------------ | ----- | ---- | --- | --- | --- | --- |
| ramprates,voltageandfrequencyshifts,andreactivepower |      |                |         |              |       | 0.00 |     |     |     |     |
transients that can damage transformers, converters, and 20 40 60 80
| protectionequipment. |     |     |     |     |     |     |                     | Time (s) |     |           |
| -------------------- | --- | --- | --- | --- | --- | --- | ------------------- | -------- | --- | --------- |
|                      |     |     |     |     |     |     | Training Rack Power |          |     | EasyRider |
Tosolvethisproblem,weintroduceEasyRider,apower
architecturetomitigatepowerfluctuationsattheracklevel.
|     |     |     |     |     |     |     | The EasyRider | prototype | is able | to smooth the |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ------- | ------------- |
Figure 1.
EasyRiderusespassivecomponentsandactively-controlled
rackpowerdrawtowithingridrampratelimits.Whilerack
auxiliaryenergystoragetoattenuaterackpowerswings.A
|          |        |             |          |            |         | power | drops rapidly | by 80%, the grid | observes | a gradual |
| -------- | ------ | ----------- | -------- | ---------- | ------- | ----- | ------------- | ---------------- | -------- | --------- |
| software | system | continually | monitors | the energy | storage |       |               |                  |          |           |
powerdrawchangeovertensofseconds.
systemtomaximizeitslifetimeinthepresenceoffrequent
charge/dischargecycles.EasyRiderfiltersrackpowervaria-
near-instantaneous80%powerreduction,asshowninFig-
tionstobewithingridsafetyrequirementswithoutrequir-
ing software modifications to AI training frameworks or ure1[12,37].Atthescaleofmoderntrainingjobsindat-
wastingenergy.WeevaluateEasyRiderona400𝑉 -rated acenters,theseswingscreateamajorproblem.Amodern
𝐷𝐶
prototypesystemagainstpublishedworkloadtracesandour trainingjobthatuses50,000GPUs(e.g.Meta’sLlama-3[34])
own GPU testbed, demonstrating its effectiveness across draws35MWwhencomputinganddropsto7MWduring
communication.
heterogeneouspowerlevelsandworkloadpowerprofiles.
Thefundamentalchallengewithsuchswingsisthatthe
stabilityofthepowergridrequiresaconstantbalancebe-
1 Introduction
tweensupplyanddemand.Tomatchsupplytodemand,the
Pre-trainingfoundationmodelssuchasOpenAI’sGPTseries, gridreliesongeneratorsthatadjustoutputinresponseto
Anthropic’sClaude,orGoogle’sGeminirequiretensorhun- loadchanges.Generators,however,aremechanicalsystems
dredsofthousandsofGPUs/TPUs.Duringtraining,these withspinningturbines,inertia,andangularmomentum—
accelerators execute synchronous compute-communicate propertiesthatfundamentallylimithowquicklytheycan
iterations:innearlockstep,theyallcompute,pausetocom- adjusttheiroutput.Dependingonthegenerator,ramping
municate,thencomputeagain[32,33].Duringcommunica- timescanrangefromafewsecondstoseveralhours,and
tionevents,thepowerdrawofalloftheacceleratorsswings bringingnewgeneratorsonlinecantakeminutestodays
from maximum power to idle within milliseconds; for an [19, 48]. When power demand changes faster than gener-
NVIDIAH100,forexample,thisisa700Wto140Wswing,a atorscanrespond,thegrid’sfrequencyandvoltagemove

outsidetheirnarrowsaferanges,damagingthegenerators Software system: EasyRider uses an optimization-based
andotherconnectedequipment[25]. controlsystemtodynamicallytrackatargetstateofcharge
Becausesuchdamagecouldbecatastrophic,takingser- (SoC)forthebatterysystem.TrackingatargetSoCensures
viceofflineforweeksorlonger,thegridprotectsitselffrom EasyRiderwillhavesufficientstoredenergytosmoothfuture
damagebyautomaticallydisconnectingunstableloads[50]. transientsdespitecharginganddischarginginefficiencies.
However,whenthoseloadsaremulti-gigawattdatacenters, Furthermore,itmaintainsbatterylifebyavoidingdeepdis-
thesuddenlossofdemandisitselfadestabilizingevent.The chargesorover-charging.Italsoallowsthesystemtoadjust
ElectricReliabilityCouncilofTexas(ERCOT)hasidentified theSoCofthebatteryduringmaintenanceforsafestorage.
thatsimultaneousdisconnectionof2.0–2.6GWofdatacenter
EasyRiderisdesignedforcompatibilitywiththefuture
loadcoulddestabilizetheentireTexasgridandtriggercas-
high-voltage400𝑉 datacenterregime.Whencomparedto
𝐷𝐶
cadingblackouts[17].Thisscenarioisnottheoretical:inJuly
thecostofaGB200rack,theper-wattcapitalexpenditurefor
2024,atransmissionfaultcaused1.5GWofdatacentersin
thepowersupplyprototypediscussedinthispaperworks
NorthernVirginiatosimultaneouslydisconnect,requiring
out to less than 1.25% of the rack cost. Using EasyRider,
emergency grid management to prevent widespread out-
large power swings by a GPU server or rack appear as a
ages[35].
gradually changing power draw. When GPU power draw
Thepossibilityofgriddamageandblackoutsfromtrain-
suddenlydrops,thesystemcharges,storingpowerfromthe
ingloadshasbecomeamajorimpedimenttobuildingnew
grid.WhenGPUpowersuddenlyincreases,thesystemdis-
datacenters.Insomerecentcases,newdatacenterprojects
charges,allowingtimeforgridpowertorampup.EasyRider
havebeendeniedbecauseoftheinstabilitythattrainingcan
cansmoothmillisecond-scaletransientstoaslowchange
bringtothegrid[44].
over30secondsormore.
ThispaperproposesEasyRider,anovelrack-levelpower
supply architecture which automatically performs power
2 BackgroundandMotivation
smoothingasshowninFigure1.EasyRidercanbeconfig-
uredtosatisfyanygrid-imposedramp-raterestrictionswith- Thissectionprovidesbackgroundonthreetopicsthatmo-
outrequiringchangestoexistingsoftware,models,orGPU tivate EasyRider’s design. First, it describes how the grid
firmware.EasyRiderallowsaracktoeasily"ridethrough"a deliverspowertodatacentersandwhyitassumestheaggre-
trainingtransientwithoutrequiringcircuitsorsystemsatthe gateload(powerconsumption)changesslowly.Second,it
datacenterorgridscale.Smoothingtransientsinhardware explainswhymodernlarge-scaletrainingworkloadsbreak
hasnumerousotheradvantages:thesystemcanrespondef- thisassumption,introducinglargeandfasttransients.Third,
fectivelyinstantaneously,canbebuiltonphysicalprinciples itgoesintothepowerarchitectureofmoderndatacenters
thatdonotsufferfromsoftwarebugs,providesextremely aswellassomecurrentandproposedapproachestoprotect
highreliability,andcanbeengineeredtotolerateanarbitrary thegridfromtrainingtransients.
loaduptoagivenmaximumpowermagnitude.
Thispapermakesthreeresearchcontributions: 2.1 GridOperatingParameters
Atanygivenmomentintime,thesumofallpowersinks
Hardware/softwarearchitecture:EasyRiderintroduces
(loads)inthegridequalsthesumofallpowersources(gen-
anovelarchitectureanddivisionofresponsibilitiesforpro-
erators). Some generators, such as solar panels and wind
viding a stable power draw to the grid. Each rack-mount
turbines,producepoweraccordingtotheweather;others,
EasyRiderpowerdistributionunit(PDU)containsthecir-
suchasgas,coal,nuclear,andhydro,canbecontrolleddy-
cuitry and energy storage needed to power the rack and
namically. The rate at which a generator can increase or
smoothpowertransients.Ahigh-bandwidthanalogcontrol
systemregulatescharging/dischargingoftheenergystorage
decreaseitspoweroutputiscalledtheramprate[20].Two
physicalpropertiesgovernthemaximumramprate:therate
as needed to smooth transients over 30 seconds or more.
atwhichthegeneratorcanchangeitsfuelconsumptionand
Alight-weightonboardsoftwaresystemisresponsiblefor
themaximumacceleration/decelerationitcanapplytothe
monitoringandmanagingthestateoftheenergystorage
largephysicalturbinesthatgeneratetheelectricalpower.For
system,maximizingitslifetimeinthefaceofmanysmall
extremelyfastgeneratorssuchasgas,themaximumramp
chargeanddischargeevents.
rateisintherangeof10-20MW/min,evenwhentheunitis
Hardwaresystemdesign:EasyRidersimultaneouslypow-
designedforafewhundredMWmaximumoutput[2,15,20].
ersarackandremovestransientsthroughacombination
Theseramprateshavehistoricallybeensufficientbecause
ofpassiveandregulatedcomponents.Passivecomponents
theaggregateloadinthegridchangesslowly.
(capacitors and inductors) filter higher frequency events
Atthesametime,loadsmakeassumptionsaboutgener-
(≤10 ms, ≥100 Hz), and high-power batteries are used in
ators:intheUnitedStates,forexample,thegridprovides
closed-loopcontroltofilterlonger,low-frequency(≥0.016
residentialpowerat120𝑉 and60Hz,butthiscanvary,and
𝑅𝑀𝑆
Hz)powerfluctuations.
mustremainwithin114-126𝑉 and59.9–60.1Hz[3,15].
𝑅𝑀𝑆
2

Devicesattachedtothegridassumethisandcanbedamaged
Utility / Backup Gens
ifpowermovesoutsidetheseranges[20].
Ifaggregateloadchangesfasterthangeneratorscanadapt,
|     |     |     |     |     |     |     |     | ATS | ATS |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thegridviolatesvoltageandfrequencyranges,damaging
…
equipment.Powerinmustequalpowerout:ifdemandin-
|         |                 |      |            |      |           |     |     | UPS 1 | UPS 2 |     |     |     |
| ------- | --------------- | ---- | ---------- | ---- | --------- | --- | --- | ----- | ----- | --- | --- | --- |
| creases | faster than the | grid | can adapt, | then | loads end | up  |     |       |       |     |     |     |
receiving less power than they need. This manifests as a SWBD SWBD
Row
saginvoltageand/orfrequency.Ifdemanddecreasesfaster
Busbars
thanthegridcanadapt,thevoltageand/orfrequencyspikes PDU Easy
up. To protect against these violations, utilities and oper- IT Rack Rider
Power
| ators install | reactive equipment |     | that | disconnects | parts | of  |     |     |     |     |     |     |
| ------------- | ------------------ | --- | ---- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Power
GPUs
thenetworkbeforepowermovesoutsideofitssafeparam- Row Row Shelf
eters[20].Thedangeranddamageoflarge,fastswingsis
real:in2023,thetripofa1.5GWloadcausedsystem-wide
frequencydeviationsacrossTexas[17],andNERC’sanaly-
Figure2.Moderndatacenterpowerhierarchyandwhere
sisofa2019disturbanceshowedthataloadoscillatingat
EasyRiderfitsin.Thisparticulardesignshowsdisaggregated
0.25Hzpropagatedacrossinterconnectionsanddamaged
powerfromtherackwithaconnectiontobusbardistribution
generatorshundredsofmilesaway[10,14].
|     |     |     |     |     |     |     | per-row. | Design variations | may | include | in-rack UPSes | or  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | ------- | ------------- | --- |
otherpowerconversioncomponents.
2.2 AI/MLTrainingPowerDynamics
Historically,datacentershaveoperatedwithingridoperating
parameters:theirpowerdrawchangesslowly,overminutes deniedbecauseoftheinstabilitythattrainingcanbringto
orhours.Agivendatacenterrunstensorhundredsofmil-
thegrid[44].
lionsofdifferentjobs,eachofwhichisatinyload;control
planessuchasKubernetes[27]orBorg[46]staggerjobstarts 2.3 DatacenterPowerHierarchy
overseconds,astheyloadbinaries,images,andsupporting
|           |     |     |     |     |     |     | Figure 2                                           | shows how | modern | hyperscale | data centers | use |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --------- | ------ | ---------- | ------------ | --- |
| software. |     |     |     |     |     |     | multi-stagepower-deliverysystemsthattransformpower |           |        |            |              |     |
Large-scaledistributedtrainingbehavesdifferently.Dur-
fromhigh-voltage13.8kVutilityinterfaces1downtothe0.8-
| ing synchronous | data-parallel |     | training, | tens | or hundreds |     |     |     |     |     |     |     |
| --------------- | ------------- | --- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
1.2VlowvoltagerailsonCPUs,GPUs,andotheraccelerators.
| of thousands | of GPUs | execute | in lockstep: |     | they compute |     |     |     |     |     |     |     |
| ------------ | ------- | ------- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Utilitypowerentersthedatacenterandanon-sitesubstation
gradientslocally,thensynchronizeparametersthroughcol-
stepsitdowntomedium-andlow-voltageswitchgear.Power
lectivecommunicationprimitiveslikeexchangingtensors isthenroutedthroughuninterruptiblepowersupplies(UP-
orgradients.
Ses),floor-orrow-levelpowerdistributionunits(PDUs),and
Thislockstepexecutioncreateslarge,suddenpowertran-
branchcircuitstoindividualracks[5,21,22,39,55].
| sients. Modern | accelerators |     | show 5:1 | to 20:1 | peak-to-idle |     |     |     |     |     |     |     |
| -------------- | ------------ | --- | -------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
DatacenterracksarebuiltaroundDCpower,historically
| ratios: an | H100 drops    | from | 700 W to    | 140 W | during | com- |             |            |             |       |                |     |
| ---------- | ------------- | ---- | ----------- | ----- | ------ | ---- | ----------- | ---------- | ----------- | ----- | -------------- | --- |
|            |               |      |             |       |        |      | at 48V [5], | to support | CPU-centric | racks | with aggregate |     |
| munication | phases, while | a    | B200 swings | from  | 1000   | W to |             |            |             |       |                |     |
powerdrawsof30kW.CurrentAIacceleratorracks,however,
50W[1,33].When10,000GPUsundergoaneventtogether,
candraw>100kW[36]andthecurrentroadmapincludes
theclusterpowercandropby5–15MWwithinhundredsof
|     |     |     |     |     |     |     | 1 MW racks | (e.g., OCP’s | Mt. | Diablo [23]). | This enormous |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ------------- | ------------- | --- |
milliseconds[12,37].Thesearenotrareevents—theyoccur powerdensity—1,000homesinasingle8ft2rackfootprint—
everytrainingiteration(typically1–10Hz)andduringevery
|     |     |     |     |     |     |     | is driven | by networking | density; | bringing | 1,000 GPUs | to- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | -------- | ---------- | --- |
checkpoint,restart,orcollectivestall.
gethersotightlyinasinglerackallowsthemtocommuni-
Alldigitalcomputingequipmentcreatestransients:aCPU,
catewithhigherbandwidthandlowerlatency.Tosupply
forexample,canexecuteanenergy-expensivememoryload
thispower,datacentersaretransitioningfrom48Vto400V
| instructionthenpauseonawfi(waitforinterrupt)instruc- |     |     |     |     |     |     | DCpower[9,47]. |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
tion.Powerregulationcircuitsonmotherboards,GPUs,and
powersuppliessmoothoutthese<1ms(>1kHz)transients.
|     |     |     |     |     |     |     | 2.4 ExistingApproaches |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
Iteration-leveltrainingdynamics,synchronizedcollectives,
|     |     |     |     |     |     |     | A training | cluster is | grid-safe | only if | its load swings | are |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | ------- | --------------- | --- |
andjob-levelevents,however,createlonger,lowerfrequency
attenuatedbeforetheyreachtheupstreamelectricalplant.
| transients, | in the range | of 100 | ms–10 | s (0.1–10 | Hz). | This |     |     |     |     |     |     |
| ----------- | ------------ | ------ | ----- | --------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
Therelevantdynamicsspanbothslowereventssuchasjob
| matters | because this frequency |     | range | overlaps | with | bulk |     |     |     |     |     |     |
| ------- | ---------------------- | --- | ----- | -------- | ---- | ---- | --- | --- | --- | --- | --- | --- |
transitionsandcheckpointsandfastercontentthatoverlaps
powersystemoscillationmodes,wheregridinfrastructure
haslimiteddampingandprotectionequipmentismostsen- 1Utilitiesconsider13.8kVa“medium”voltage,with>100kV,e.g.,forlong-
sitive[14].Insomecases,newdatacenterprojectshavebeen
rangetransmissionlinesbeing“high’voltage.
3

Table1.Transientmitigationapproaches.Thekeydistinctioniswheremitigationisinsertedandwhetherthehighfrequency
transientsareelectricallyorsoftware-mediated.
Approach Placement Highfrequency Lowfrequency SW/FWdependence Mainlimitation
GPUburn[37] GPU None Workinjection Trainingstack Energywaste;nohardwareprotection
GB300support[1] Powershelf Capacitors Powercap/burn Platformfirmware Platform-specific
Software-controlledbatteries[12] Rack Battery,SW-triggered Battery+cap+burn Telemetry+software Fastpathlimitedbytelemetry
SiteBESS[24] Substation None Sitebattery Sitecontroller DoesnotprotectinternalDCdistribution
EasyRider(ours) RackPDU PassiveLC Localbattery Nonefortransientmitigation Rack-localonly
| with rack-level |     | electrical | dynamics | and | power-system |     | os- |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1.00
| cillation | bands. | Existing | mitigations |     | address | parts | of this |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ----------- | --- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
).u.p( rewoP
| problem,butatdifferentpointsinthehierarchyandwith      |     |     |     |     |     |     |     | 0.75 |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
| differentdependenciesonsoftware,firmware,orsiteinfras- |     |     |     |     |     |     |     | 0.50 |     |     |     |     |     |     |
allowed
tructure[1,12,14,24].Table1summarizesthisdesignspace. 0.25 ramp
SoftwareburnattheGPU.Oneapproachistoinjectsec-
|     |     |     |     |     |     |     |     | 0.00 |     |  22 sec. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------- | --- | --- | --- | --- |
ondarywork,suchasGEMMkernels,whenGPUactivity 0 20 40 60 80 100
Time (s)
orpowerfallsbelowatarget[12].Thiscansmoothsome
utilizationdrops,butonlybyspendingextraenergyandcou- (a)Time-domain.
plingprotectiontothetrainingstack.Ifdetectionorcontrol
fails,thetransientisexposedupstream.
|     |     |     |     |     |     |     |     |     | 1   |     |     | fc  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
).u.p( rewoP 10
| Platform-specific |     | electrical |     | support. | NVIDIA’s |     | GB300 |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | -------- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
NVL72addspower-shelfcapacitorstogetherwithstartup
10 3
powercappingandramp-downsupport[1].Thisprovides
grid limit
1/22 Hz
electricalmitigationforshort(≤60ms)transients,butitis
10 5
tiedtoaspecificplatformanddoesnotaddresslargerenergy 10 2 10 1 10 0 10 1
Frequency (Hz)
imbalancesoverlongerevents.
Software-coordinatedrackstorage.Anotherapproachis (b)Frequency-domain.
tocombinerack-levelbatteriesthatdispatchonsoftware-
|           |        |       |          |       |         |      |     |        | Time- | and frequency-domain |     | representation |     | of  |
| --------- | ------ | ----- | -------- | ----- | ------- | ---- | --- | ------ | ----- | -------------------- | --- | -------------- | --- | --- |
| triggered | events | along | with GPU | power | capping | like | the | Figure | 3.    |                      |     |                |     |     |
NVIDIAGB300[1,12].However,thisapproachhastwokey apowertrace basedonFig.1from [12],whichweuseas
limitations.First,conventionalbatterychemistriessuchas atestbenchforourEasyRiderprototype.Thelargestdips
lithium-ionarelimitedbythekineticsoftheirelectrochem- occur at approximately 22-second intervals, producing a
ical reactions, which cannot respond to transients faster prominentpeaknear1/22Hz.𝛽 istheallowedramprateby
|                                                     |     |     |     |     |     |     |     | thegridoperatorand𝑓 |     | isthecutofffrequencyforthegrid |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------------------------ | --- | --- | --- | --- |
| thantenstohundredsofmillisecondswithoutaccelerating |     |     |     |     |     |     |     |                     |     | 𝑐                              |     |     |     |     |
| degradation,makingthemfundamentallyunsuitedtoabsorb |     |     |     |     |     |     |     | limit𝛼.             |     |                                |     |     |     |     |
high-frequencyrack-leveltransients.Second,thedesignis
notfault-tolerant:becausebatterydischargeistriggeredby
softwaretelemetry,anyfaultordelayinthesoftwarestack
|     |     |     |     |     |     |     |     | 3 ProblemFormulation |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
wouldpreventthesystemfromrespondingtoatransient
ThegriddoesnotseeindividualGPUs,itonlyseestheag-
entirely.
gregatepowerdrawofadatacenterandrequiresthatthis
|     |     | Site | batteries | buffer | the aggregate |     | load |     |     |     |     |     |     |     |
| --- | --- | ---- | --------- | ------ | ------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Site-level BESS. composite signal be “well-behaved.” As discussed in Sec-
seenatthegridinterconnectionpoint[24].Thishelpswith
tion2.1,large-scaletrainingviolatesthisexpectationbycre-
slowersite-widevariation,butitsitsabovetheinternalrow
|     |     |     |     |     |     |     |     | ating | large changes | in power | draw | that occur | faster | than |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | -------- | ---- | ---------- | ------ | ---- |
andrackdistributionhierarchy.Itthereforedoesnotstop
|     |     |     |     |     |     |     |     | generators | and | protection equipment |     | can safely | respond. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------- | --- | ---------- | -------- | --- |
racktransientsfrompropagatingthroughtheinternalpower
|     |     |     |     |     |     |     |     | Grid operators |     | therefore impose | limits | on how | quickly | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | ------ | ------ | ------- | --- |
distributionbeforetheyareabsorbedatthesiteboundary.
|                  |     |            |     |                |     |     |       | datacenter | may | change its power | draw | over | time and | on  |
| ---------------- | --- | ---------- | --- | -------------- | --- | --- | ----- | ---------- | --- | ---------------- | ---- | ---- | -------- | --- |
| Scheduling-based |     | smoothing. |     | Bubble-filling |     | and | high- |            |     |                  |      |      |          |     |
howmuchvariationisallowedatfasttimescales.
| utilization | schedulers |     | reduce | some iteration-level |     |     | swings |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------ | -------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Tomaketheseconstraintseasytoreasonabout,weview
| by keeping | GPUs | more | uniformly | utilized |     | [4, 16, | 40, 52]. |     |     |     |     |     |     |     |
| ---------- | ---- | ---- | --------- | -------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
thedatacenterpowertracenotjustasatimeseriesbutasa
Thesemethodsarecomplementary,buttheydonotprovide
sumofsinusoidsatdifferentfrequencies,obtainedviaaDis-
| an electrical | guarantee |     | at the | rack boundary |     | and | remain |     |     |     |     |     |     |     |
| ------------- | --------- | --- | ------ | ------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
creteFourierTransform(DFT).Themagnitudeofthesignal
sensitivetoworkloadstructure,checkpointing,andrecovery
at0Hzisitsaveragevalue;lowfrequenciescorrespondto
events.
slowchanges,andhighfrequenciestorapidones.Intuitively,
4

havemagnitudeatmost𝛼:
|     | Model Training | EasyRider |               |              |     |                        |         |                           |         |     |
| --- | -------------- | --------- | ------------- | ------------ | --- | ---------------------- | ------- | ------------------------- | ------- | --- |
|     |                |           |               |              |     |                        | 𝑆(𝑓) ≤𝛼 | forall𝑓                   | ≥ 𝑓 𝑐 . |     |
|     | GPU            |           | DC/DC  Filter | Power        |     |                        |         |                           |         |     |
|     | Rack           | Converter |               | Distribution |     |                        |         |                           |         |     |
|     |                |           |               |              |     | Above𝑓 ,onlyafraction𝛼 |         | ofthecampuspowerispermit- |         |     |
𝑐
tedtoparticipateinfastoscillations.Figure3bshowsthis
Battery Bank
SoC/Voltage Corrective  constraint:thebluecurveis𝑆(𝑓)onalog–logscale,andany
current signal
|     |                 |                       |     |                 |     | portionabovethehorizontallineat𝛼 |            |            | for𝑓 ≥ 𝑓 violatesthe |     |
| --- | --------------- | --------------------- | --- | --------------- | --- | -------------------------------- | ---------- | ---------- | -------------------- | --- |
|     |                 | Battery Optimization  |     |                 |     |                                  |            |            | 𝑐                    |     |
|     |                 | and Control Loop      |     |                 |     | spec.                            |            |            |                      |     |
|     | As seen at rack |                       |     | As seen by grid |     |                                  |            |            |                      |     |
|     |                 |                       |     |                 |     | Maximum                          | ramp rate. | The second | limit bounds         | how |
Figure4.EasyRiderarchitecture.Softwarecomponentsare
quicklythedatacenterpowercanchangeintime:
showninwhite,hardwareingray.EasyRiderisagnosticto
(cid:12)𝑑𝑃(cid:12)
thetrainingworkloadandcanbeintegratedintoexisting (cid:12) (cid:12)
|     |     |     |     |     |     |     | (cid:12) (cid:12)≤𝛽 | forall𝑡, |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | -------- | --- | --- |
(cid:12)𝑑𝑡
datacenterpowerhierarchieswithappropriateconversions (cid:12)
andcomponentsizing. forsomeramp-ratelimit𝛽 expressedasafractionofrated
powerpersecond.Steeprampscorrespondtoexcesshigh-
|     |     |     |     |     |     | frequency | content: a spectrum | concentrated | at  | fast time |
| --- | --- | --- | --- | --- | --- | --------- | ------------------- | ------------ | --- | --------- |
scalesinevitablyproduceslargechangesin𝑃(𝑡)overshort
thehighestsignificantfrequencyinthespectrumdetermines intervals.Figure3aillustratesapowertracethatrepeatedly
exceedsthisslopebound.
howsteeplythesignalcanchangeintime.
Ifeachrack’spower-deliverysystemissizedsothatits
Fromthisperspective,trainingracksneedalow-passfilter:
acircuitand/orsoftwarestackthatremoveshigh-frequency 𝛼, 𝛽 limitssumtothecampus-levelbudget,thenahallof
|     |     |     |     |     |     | such racks | will satisfy | the same aggregate | constraints. | If  |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | ------------------ | ------------ | --- |
contentandpasseslow-frequencybehavior.Low-passfilters
areubiquitousinpowerelectronics—forexample,everycom- the power-delivery system for every rack satisfies these
puterpowersupplyusesthemsothataCPUseesastable, per-rack constraints, then the datacenter as a whole will
dosoinaggregate.Ratherthanreasonabouteverywork-
cleanvoltageeventhoughitsinstantaneousloadchanges
everycycle.Training,however,stressesfiltersintwoways. loadindividually,wespecifyEasyRider’sbehaviorinterms
|     |     |     |     |     |     | of the frequencies | it attenuates | or  | preserves. This | makes |
| --- | --- | --- | --- | --- | --- | ------------------ | ------------- | --- | --------------- | ----- |
First,itrequiressmoothingdowntounusuallylowfrequen-
cies, on the order of tens of seconds (≤ 0.1 Hz), whereas iteasytocheckwhetheragivenEasyRiderconfiguration
conventional filters target millisecond scales. Second, the satisfies both the frequency-content and ramp-rate limits
thegridimposes.EasyRideraddressesbothchallenges—very
| amount | of energy | involved | is enormous, | as smoothing | a   |     |     |     |     |     |
| ------ | --------- | -------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- |
transientmeanstemporarilystoringorsupplyingthediffer- loweffectivecutofffrequenciesandhighenergy—throughits
hardware/softwarearchitectureandsoftwarecontrolsystem,
encebetweentherack’sinstantaneousandaveragepower
| withoutexposingthatswingtothegrid. |     |     |     |     |     | describednext. |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
Theadvantageofviewingtrainingtransientsasfrequency
|     |     |     |     |     |     | 4 EasyRiderArchitecture |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
signalsisthatfiltersaregovernedbywell-understoodcircuit
theory:oncesizedcorrectly,theirbehavioroverfrequency EasyRiderisaPDUsystemthatsitsbetweenaGPUrackand
therowbus,reshapingtherack’spowerwaveformbeforeit
ispreciseandpredictable.Assumingcorrectimplementation
andnocomponentfailures,afilterwillshapethepowertrace reachestherestofthedatacenterpowersystem(Figure2).
exactlyasdesigned. Itissizedforfuturehigh-densityrackswith400𝑉 power
𝐷𝐶
Suppose𝑃(𝑡)isthenormalizedpowerdrawthegridsees andan80%idle-to-peakpowerswing.EasyRidersmooths
fromadatacenter.Itsfrequency-domainrepresentationde- transients(i.e.jobstart-up,shutdown,checkpointing)that
occurontimescalesfrommicrosecondsuptotensofseconds,
| scribes, | for each | frequency | 𝑓, how much | of the campus |     |     |     |     |     |     |
| -------- | -------- | --------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- |
power is concentrated at that rate—exactly what grid op- whicharetoofastforthegridtorespondtobuttoslowfor
eratorscareabout.Let𝑆(𝑓) denotethenormalizedmagni- traditionalGPUpowersuppliestohandle.Itsactionsarein-
tudeatfrequency 𝑓,scaledsoitcanbeinterpretedasthe visibletoupstreamdevices:UPSes,PDUs,andsubstationsall
fractionoftotalsignalpower.Forexample,Figure3bshows seeagrid-compliant,low-ramprackload.Becauseitoperates
𝑆(1/22𝐻𝑧) 0.1foraspecifictrainingtrace,so≈10%of upto400𝑉 anddependsonlyonlocalsensingandactua-
|     | ≈   |     |     |     |     |     | 𝐷𝐶  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thatrack’spoweruseisinthe1/22Hzfrequencybin. tion,EasyRidercanbeaddedtonext-generationrackswith
Gridoperatorsgenerallyimposetwokindsoflimitson powersidecars[9]orretrofittedintoexistingdatacenters
𝑃(𝑡)and𝑆(𝑓): within-rackPDUswithoutchangestotheclustersoftware
stack.
Thefirstlimitconstrainshowmuch AsillustratedinFigure4,EasyRidercomprisesthreephysi-
Frequencycontent.
variationisallowedathighfrequencies.Thegridoperator calelementspluscontrolsandasoftwaresystem,withaclean
specifiesacutofffrequency𝑓 ;allfrequenciesabove𝑓 must decomposition.Hardwaremanagespowerovertimescales
|     |     |     | 𝑐   | 𝑐   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5

𝐿 𝑅
𝐷𝑎 𝐷𝑎
𝐿
|     |      | 𝐹   | 𝑖   |     |     | 𝑖   |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |      |     | 𝐼𝑁  |     |     | 𝐵   |     |     |     |
|     | 𝑖 𝐷𝐶 |     | +   |     | +   | 𝑖 𝑅 |     |     |     |
(2)
|     |      |     |     | DC-DC   |     |      | (3)                    | +   |     |
| --- | ---- | --- | --- | ------- | --- | ---- | ---------------------- | --- | --- |
|     | + 𝑉  | 𝐶   | 𝑉   |         | 𝑉   |      | Bi d i re c t i o n al | 𝐵   |     |
|     | − 𝐷𝐶 | 𝐹   | 𝐼𝑁  | voltage | 𝑂𝑈𝑇 |      |                        | 𝐴𝑈𝑋 |     |
|     |      |     |     |         |     | 𝑅𝑎𝑐𝑘 | c o n v e r t e r      | −   |     |
regulator
|     |     |     | −   |     | −   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1)Inputfilter
Figure5.Thehardwaresystemarchitectureconsistsofthreemaincomponents:(1)aninputfiltertobufferthepowergrid
againsthigh-frequencypowerfluctuations„(2)aDC-DCconvertertomaintainconstantrackvoltage,and(3)anauxiliary
batterysystemtostoreordispatchenergyduringtransients.Thisconfigurationallowsthepowergridtograduallytransition
betweendifferentloadconditionswhiletherackseesimmediatepoweravailability.
fasterthanthegridcanrespond,smoothingandremoving dropinrackpowerforjustsixsecondswouldrequirestoring
transients. Software manages energy storage over longer 4.8MJ,whichismorethanwhatanaverageU.S.housedraws
| timescales, | to maximize system | lifetime without | disrupt- | inanhour[45]. |     |     |     |     |     |
| ----------- | ------------------ | ---------------- | -------- | ------------- | --- | --- | --- | --- | --- |
ing the hardware. The hardware consists of a passive in- Figure5showsasimplifiedcircuitschematicforthehard-
putfilterthatattenuateshigh-frequencytransients,aDC- waresystem.Assumingtherackisprovidedwithadequate
DCregulatorthatmanagesrack-sidevoltageandcurrent, energystoragecapacityandaproperinputfilter,thisdesign
and a rack-scale battery bank that absorbs or injects en- canbeadaptedtomeetanygridspecificationwhiletherack
ergy during lower-frequency swings. A controller moni- seesimmediatepoweravailability.
tors battery capacity and current and issues slow correc- WhereEasyRidersits.EasyRidermovesmitigationtothe
tivecharge/dischargeadjustmentssothatthebatterystays rack PDU, between the accelerator rack and the row bus,
withinitspreferredoperatingwindowwhileenforcingthe andsplitstheproblembytimescale.ApassiveLCstageat-
grid-facinglimitsonramprateandfrequencycontent. tenuatesfasttransientsdirectlyintheelectricalpath,while
Together,thesestagespresentasmoothedrackloadthat alocalbatterycompensatesforslowervariations.Thisre-
satisfiesthefrequencyandramp-ratespecificationsfromSec- movesthetransientfastpathfromthetrainingstackand
tion3whileleavingtheunderlyingtrainingjobunchanged. delayedtelemetrywithoutrequiringsite-levelbuffering.In
Section5detailsthefilter,converter,andbatterydesign;Sec- thiscomparison,EasyRideristheonlyapproachthatisboth
tion6describesthecontrolloopthatkeepsthebatteryina rack-localandsoftware-independentinthetransientpath.
narrowmid-SOCbandtoavoidlong-termdriftandaging.
| 5 HardwareDesign |     |     |     | 5.1 | InputFilter |     |     |     |     |
| ---------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
ThissectiondescribesEasyRider’sthreehardwareelements: ThefiltershowninFigure5isasecond-orderpassivefilter
aninputfilter,aDC-DCconverter,andanauxiliarybattery witharesistivedampingleg.Thecombinationofcapacitor
energystoragesystemstoragesystem.Thesecomponents 𝐶 andinductor𝐿 stabilizestheinputvoltage𝑉 andin-
|     |     |     |     |     | 𝐹   | 𝐹   |     |     | 𝐼𝑁  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
workinconcerttoremovetransientsfromarack’spower putcurrent𝑖 fromthedatacenterDCbusbaroversmall
𝐷𝐶
drawandensureitmeetsgridspecifications.Thisdecompo- timescales(<50ms).
sitionhandlesanypowersignalthatstayswithinthesys- Bythemselves,however,𝐿 and𝐶 arenotsufficientto
|     |     |     |     |     |     |     | 𝐹   | 𝐹   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tem’smaximumprovisionedpower:itrequiresnochanges satisfygridspecifications.Theyhavetwolimitations.First,
tosoftware,canbedeployedonexistingracks,andwilloper- every capacitor/inductor pair has a frequency, at
resonant
atecorrectlyevenifthesoftwaremanagementsystemfails, whichtheycaninteractandenteracycleofchargingand
althoughmulti-hoursoftwaredowntimesmightagethebat- dischargingeachother.Thedampingcircuitcomposedof
terysystemslightlyfasterastheymoveoutsidetheiroptimal 𝑅 and𝐿 isinactivewhentherackpowerissteady,butit
|     |     |     |     |     | 𝐷𝑎 𝐷𝑎 |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
operatingrange. suppressesthisresonanceduringtransients.Second,because
Therearetwomajorchallengestothehardwaredesign: theenergydensityofinductorsandcapacitorsislow,the
smoothinganextremelybroadrangeoffrequenciesandbe- input filter does not store very much energy—smoothing
ingabletostoreaswellasreleasethelargeamountsofenergy transientsthatlastmorethanafewmillisecondswouldre-
thatarackcanrequireatthosetimescales.A1MWrack,for quire a prohibitively large passive filter. It is only useful
example,drawstheequivalentpowerof≈800averageU.S. for smoothing high-frequency power fluctuations. It also
homes.Atsuchapowerlevel,tocompletelysmootha80% filtersoutthehigh-frequencynoiseintroducedtothesystem
6

1
0
1
0
1
10 20 30 40
Time (s)
).u.p(
rewoP
100
10 2
10 4
10 6
10 3 10 1 101 103 105
Frequency (Hz)
Rack EasyRider Auxiliary storage
Figure6.SmoothingshowninanEasyRiderprototypetest.
Gridpower(red)remainssmootheventhoughrackpower
(grey)fluctuates.Theauxiliaryenergysystem(orange)ab-
sorbsthedifference.
bytheswtichingcomponentsinthevoltageregulatorand
bidirectionalconverter.
5.2 DC-DCConverter
TheDC-DCconvertermaintainsaconstantoutputvoltage,
𝑉 whichpowerstherack.Thecontrolsforthevoltage
𝑂𝑈𝑇
regulatorinourdesignareimplementedfullyinhardware,
meaningthereisnoprocessingtimedelayasinasoftware-
basedsystem.Itrespondsandcorrectsforevensmallerrors
inoutputvoltageinlessthanamillisecond.Theconverter
regulates𝑉 towithin0.7%oftheratedrackvoltageeven
𝑂𝑈𝑇
iftherackpowerchangeswithrampratesashighas±200
kW/second.
5.3 AuxiliaryEnergyStorageSystem
Becausethepassivefiltercan’tstoreenoughenergytosmooth
outlongtransients,EasyRiderusesanactivelycontrolleden-
ergystoragesystemtobufferagainstchangesinrackpower
overlongertimescales.Whentherack’spowerdrops,the
storagesystemcharges,absorbingtheextrapowerfromthe
grid.Whentherack’spowerrises,thestoragesystemdis-
charges,temporarilyprovidingpowertotherackuntilthe
grid supply can catch up. High-bandwidth sensors detect
changesinrackpowerandautomaticallytriggertheflow
ofcurrentintooroutofthestoragesystemtomakeupthe
differencesuchthatthevalue𝑖
𝐼𝑁
≈𝑖
𝐷𝐶
+𝑖
𝐵
isstableover
longertimescales.Ourprototype,forexample,buffersrack
powerfluctuationssuchthattheDCsupplytakesabout30
secondsafterastepchangeinrackpowerbeforetaperingoff
tothenewsteadystate.Figure6demonstratesthesmoothing
effectofthebatterysystemduringapreliminarytestofthe
EasyRiderprototype.
Traditionalgridbatteriesaredesignedtoprovidepower
forhours,whileEasyRideronlyneedsafewminutesworth
of capacity. In our prototype, we use high-power lithium
ironphosphate(LiFePO )batteriesasenergystorage,due
4
edutingaM
evitaleR
Input Filter
Auxiliary
Energy System
fb ff EasyRider
Figure7.EasyRider’sfrequencyresponse,showingthecom-
binedeffectoftheinputfilterandcontrolledenergystor-
agesystem.Theinputfilterattenuatesfluctuationsabove
𝑓 ,whiletheauxiliaryenergycompensatesforfluctuations
𝑓
above 𝑓 .Together,theyensuretherackmeetsgridspeci-
𝑏
fications.“RelativeMagnitude”indicatesthemagnitudeof
fluctuationsseenbytheDCdistributiongridrelativetothose
drawnbytherack,
(cid:12)
(cid:12)
𝑖˜
𝑅
(cid:12)
(cid:12).
(cid:12)𝑖˜
𝐷𝐶
(cid:12)
totheirhighpower-to-capacityratioandlowcostperunit
energy.Supercapacitorsoracombinationofdifferentenergy
storage technologies could also meet EasyRider’s storage
needs.Thekeysizingrequirementsandcontroldynamics
forthissystemaredefinedinAppendixA.1.
5.4 FilterResponse
Theresponseofafilterdescribeshowitbehavesoverdiffer-
entfrequencies.EasyRider’shardwareessentiallyconsists
oftwofilters(thepassiveinputfilterandthecontrolledbat-
terysystem),anditsbehavioristhesimplemultiplication
oftheirresponses.Thecomponentsusedintheinputfilter
andenergystoragesystemmustbesizedappropriatelyto
complywiththegridspecificationsdiscussedinSection3.
AppendixA.1describeshowthecorrectsizesarederived
fromtherackpowerratingandgridspecifications.
Asecond-orderLCfilterliketheonepicturedinFigure5
has a cutoff frequency 𝑓 . At frequencies higher than 𝑓 ,
𝑓 𝑓
thefilterattenuatesrackpowerfluctuationsbyafactorof
as much as 100 for every 10x increase in frequency. Our
implementationofEasyRiderusesacutofffrequency 𝑓 𝑓 ≈
4Hz,andFigure7showsitsfrequencyresponseattenuating
fluctuationsabovethisfrequency.Withoutthecontrolled
auxiliaryenergysystem,asinusoidalchangeinrackpower
with𝑓 =1Hzwillnotbedampenedatallbytheinputfilter,
whileafluctuationat𝑓 =1000Hzwillbecutbyafactorof
≈1000,asobservedbythegrid.
Theauxiliaryenergysystemisalsoafilter.Itscutofffre-
quency,𝑓 ,islowerthan𝑓 ,butitssystemcontroldynamics
𝑏 𝑐
aresuchthatfrequenciesareattentuatedbyafactorofonly
10forevery10xinfrequencyabove𝑓 .
𝑏
Thesetwofilterscompound.Figure7showsthetotalfre-
quencyresponseoftheEasyRidersystemastheproductof
theinputfilterandauxiliarysystem’sresponses.
7

6 BatteryLifetimeManagement
EasyRider’s hardware path handles all fast transients au-
tonomously: the passive LC filter and controlled battery
systemabsorbandreleaseenergyatthespeedtherackde-
mands,withnosoftwareintheloop.Becausethebattery
chargeanddischargeefficiencies(𝜂 and𝜂 respectively)are
𝑐 𝑑
notperfect,aslowercontrolloopisrequiredtomanagethe
battery’sSoC.
Everycharge–dischargecycleincursround-triplosseson
the order of 1−𝜂
𝑐
𝜂
𝑑
of the energy exchanged, and these
lossesaccumulateoverhoursoftrainingintoamonotonic
SoC drift. This can be either upward when set-point bias
dominates, or downward when resistive losses dominate.
Leftuncorrected,thebatteryeventuallysaturatesagainstits
upperorlowersafebound,losingthesymmetricheadroom
itneedstosmooththenexttransient.DwellingatahighSoC
alsoacceleratesidle-timeaging.
The software controller’s purpose is to counteract this
Figure8.PhotoofthebuiltEasyRiderprototypesystem.
drift.Itperiodicallyreadsthebattery’sstateofchargefrom
thebatterymanagementsystemandissuesmilliamp-scale
thatwouldresultinsuddendropsorjumpsincurrenttothe
correctivecurrentstotheDC–DCstage.Becausethecorrec-
battery). The controller applies only the first action from
tivecurrentisordersofmagnitudebelowtherack’stransient
eachsolveandre-optimizesatthenextintervalwithafresh
current,thecontrollercannotinterferewiththehardware’s
SoCreadingfromtheBMS.Anarrowmarginoferroraround
filteringevenifitissuesanincorrectcommand.Ifthesoft-
thetargetbringsthecurrenttozerosothatthebatteryavoids
warecrashesorlosesconnectivity,thehardwarecontinues
unnecessarycurrentfluctuationsnear𝑆∗.TheresultingQP
tosmoothtransients,andtheonlyconsequenceisthatthe
issmallenoughtosolveinunder10msonaRaspberryPi
batterySoCbeginstodrift,whichcanbecorrectedonrestart
5,wellwithinthe5supdateinterval.Thefullformulation,
withnocold-startpenalty.Wedecomposethecontrollerinto
includingthestorage-targetcomputation,theQPobjective
twoloopsthatoperateondifferenttimescales:anouterloop
and constraints, and the normalization of tuning weights
thatselectstheSoCtargetandaninnerloopthatdrivesthe
appearsinAppendixB.
batterytowardthetarget.
The key property this decomposition provides is that,
OuterLoop:Aslowouterloop,updatedonregimechanges
givenanySoCwithinthehardwaresafebounds,theinner
andrefreshedeveryfewminutes,selectstheSoCtarget𝑆∗
loopisalwaysfeasibleandconvergesto𝑆∗withinafewcon-
thebatteryshouldtrackbasedonreducingbatteryaging[53].
trolintervalswithoutperturbingthegrid-facingpowerqual-
Duringactivetraining,thetargetisamid-bandvalue𝑆
mid ity.Thecontrollerdependsonthreegroupsofparameters:
chosentomaximizesymmetricchargeanddischargehead-
(1)batterypropertiessuchasmaxcharge/dischargecurrent
room.Duringprolongedidleperiods,suchasjobcompletion,
androundtripefficiency,(2)outer-looppolicysuchasthe
maintenancewindows,orinter-jobgapsexceedingaconfig-
mid-bandSoCandidle-timeSoC,and(3)inner-loopweights
urablethreshold𝑇 ,thetargetdropstoalowervalue𝑆
enter idle suchasthetrackingerror,maintenance-currentmagnitude,
thatreducesvoltage-dependentidle-timeaging[29,53].The
andcommandsmoothness.Theseareallsetonceatdeploy-
outerloopcomputesthisstoragetargetfromtheremaining
mentfromthebatterydatasheetandthedesiredcorrection
usableidlebudget:thetimeleftintheidlewindowminusthe
timescale,withnoper-workloadtuning.
timeneededtochargebackto𝑆 atthemaximumrate.As
mid
theidlewindowelapses,thebudgetshrinksandthetarget
7 Evaluation
risesbacktoward𝑆 automatically;whentheremaining
mid
Westructureourevaluationaroundfourquestions:(1)can
timecannolongercoverthereturncharge,thetargetreverts
EasyRiderkeeptrainingloadsgrid-compliantwithoutaffect-
to𝑆 withoutoperatorintervention.
mid
ingjobs,(2)howdoesitcomparetosoftware-basedsolutions,
InnerLoop:Afasterinnerloop,executedevery5s,drives
(3)isthedesignrobustacrossdifferentworkloads,and(4)
thebatterytowardthecurrenttargetbysolvingasmallcon-
whataretheoverheadsandlifetimetrade-offs?
vex program over a receding horizon of 𝐻 intervals. The
objectivebalancesthreeconcerns:trackingerror(distance
7.1 ExperimentalSetup
from𝑆∗),maintenance-currentmagnitude(tolimitunneces-
sarycycling),andcommandsmoothness(topreventchatter Prototyperating:Toevaluateoursystem,weconstructed
aprototypeofthehardwaredesignoutlinedinSections5
8

| and6.Thisprototype,picturedinFigure8,isratedtodeliver |     |     |     |     | 1.0 |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Rack
| 10kWofpowertoa400𝑉                      |     | load.2Itisequippedwitha74Ah |     |              | 0.8 |     |     |           |     |
| --------------------------------------- | --- | --------------------------- | --- | ------------ | --- | --- | --- | --------- | --- |
|                                         |     | 𝐷𝐶                          |     |              |     |     |     | EasyRider |     |
| batterybankwithamaxdischargerateof2.4C. |     |                             |     | ).u.p( rewoP |     |     |     |           |     |
0.6
Workloadsandtraces:Inourevaluationweareonlycon-
0.4
cernedwithtrainingjobsthatexhibitswingsbetweenpeak
| andidlepowerconsumption.Cluster-scaletracesoffrontier- |     |     |     |     | 0.2  |          |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | ---- | -------- | --- | --- | --- |
| modeltrainingjobsarenotpubliclyavailable,therefore,we  |     |     |     |     | 0.0  |          |     |     |     |
|                                                        |     |     |     |     | 0 50 | 100 150  | 200 | 250 |     |
| relyonanexistingnormalizedtraceofatrainingjobthat      |     |     |     |     |      | Time (s) |     |     |     |
existsfromChoukseetal.[12].Furtherfortestingsoftware (a)Powertrace.
| approachesandprototypeevaluation,wealsoprofiletrain- |     |     |     |     | 0.75 |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Rack
| ingaGPT-style125MparameterLLMona2-GPUNVIDIA |     |     |     | )s/.u.p( etaR pmaR | 0.50 |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | ------------------ | ---- | --- | --- | --- | --- |
EasyRider
| Titan-Xdecommissionedserverbladefromourlab. |     |     |     |     | 0.25 |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
0.00
0.25
7.2 RampRate&FrequencyContentCompliance
0.50
withoutTrainingChanges
| Benchmarkspecifications:AsdiscussedinSection3,the |     |     |     |     | 0.75 |         |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- |
|                                                   |     |     |     |     | 0 50 | 100 150 | 200 | 250 |     |
Time (s)
| maximumallowableramprate𝛽 |     | andparameters𝛼 | and 𝑓 |     |     |              |     |     |     |
| ------------------------- | --- | -------------- | ----- | --- | --- | ------------ | --- | --- | --- |
|                           |     |                | 𝑐     |     |     | (b)Ramprate. |     |     |     |
definingrestrictionsonthefrequencycontentofthegrid
| power trace | will be set | by local grid operators’ | require- |     |     |     |     |     |     |
| ----------- | ----------- | ------------------------ | -------- | --- | --- | --- | --- | --- | --- |
Figure9.(a)ConditionedpowertraceusingEasyRiderto
ments.Todemonstratethesmoothingeffect,wedesigned
|     |     |     |     | power | a DC load | with a jittery | training | power trace. | (b) |
| --- | --- | --- | --- | ----- | --------- | -------------- | -------- | ------------ | --- |
ourEasyRiderprototypeundertheassumptionthatthedat-
|                                   |     |     |           | Corresponding | ramp | rate of power | drawn | from the | grid |
| --------------------------------- | --- | --- | --------- | ------------- | ---- | ------------- | ----- | -------- | ---- |
| acenterisallowedtorampatamaximum𝛽 |     | =   | 0.1(10%of |               |      |               |       |          |      |
comparedtotheunconditionedramprateasafunctionof
ratedpowerpersecond)andthatthegridimposesalimit
time.TheEasyRiderprototypeisabletoconstraintherack’s
=10−4
| 𝑆(𝑓) <𝛼 | onthenormalizedmagnitudeoffrequen- |     |     |     |     |     |     |     |     |
| ------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
rampratetolessthan±10%ofitsratedpowerpersecond.
| cies 𝑓 above | 𝑓 =2Hz.Thisspecisinlinewiththeissues |     |     |     |     |     |     |     |     |
| ------------ | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
𝑐
describedbypreviouswork[12,33,37]andaddressesthe
| bandoffrequeciesfrom0.1-10Hzthatcandamagegenera- |     |     |     |     | 100 |     |     |       |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
| torsandturbinesasnotedbyNERC[14,15,20].          |     |     |     |     |     |     |     | PRack |     |
10 1
|     |     |     |     | ).u.p( rewoP |     |     |     | PEasyRider |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | ---------- | --- |
Rampratecompliance:Figure9ashowstheresultofusing
2
| ourEasyRiderprototypetodeliverpowertoaDCloadfol-    |     |     |     |     | 10  |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lowingthenormalizedtrainingpowertracefrom[12].While |     |     |     |     | 3   |     |     |     |     |
10
therackpowertraceexhibitssharppowerswingsateach 4 grid limit
10
communicationeventandanabruptdropatjobtermination,
10 5
theEasyRider-conditionedtracetransitionsmuchmoregrad- 10 2 10 1 100 101
uallyandexhibitsalowerpeakpowerdraw.Figure9bshows Frequency (Hz)
theramprateacrossthesametimeperiod,demonstrating
Figure10.ThefilteringeffectofEasyRiderkeepsharmonic
thatEasyRidersuccessfullysmoothstherackpowertraceto
|     |     |     |     | contentbelowagrid-imposedlimit𝛼 |     |     | forfrequenciesabove |     |     |
| --- | --- | --- | --- | ------------------------------- | --- | --- | ------------------- | --- | --- |
ensurethattheramprateneverexceeds10%oftherack’s
𝑓 =2Hz,eventhoughtherackpowertracecontainssignif-
| ratedpowerpersecond. |     |     |     | 𝑐   |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
icantenergyinthisband.
Thisbehaviorisindependentofthetrainingjob’spower
profile,thereforecomplyingwiththegridramp-ratespec-
ificationwithoutmodifyingtheworkload.Thisdecouples rackpresentsapowerwaveformwith|𝑑𝑃/𝑑𝑡 |≤𝛽,theag-
gridcompliancefromjobscheduling,asanytrainingwork- gregatedatacenterramprateislikewiseconstrained.3This
loadcanrununmodified,andEasyRiderwillensurethatits
allowsoperatorstoreasonaboutcampus-widelimitsinterms
worst-caseramprateneverexceeds𝛽,evenacrossstart-up ofper-rackdesignratherthanper-jobcoordination.
andshut-downphases.Importantly,theguaranteecomposes
Frequencycontentcompliance:Figure10showstherack
acrossracksandrows—becauseeachEasyRider-equipped andEasyRiderpowertracesfromFigure9abrokenintotheir
respectivefrequencycomponents.Thecombinedeffectof
|     |     |     |     | the input | filter and | battery system | is enough | to shift | the |
| --- | --- | --- | --- | --------- | ---------- | -------------- | --------- | -------- | --- |
entireEasyRiderpowerspectrumoutofrestrictedzone.
2Thethermaldesignoftheprototypedoesnotsupportaloadcurrentabove
3AppendixDprovidesadditionalexplanationonsmoothingeffectsata
25A.BecauseDCpoweristheproductofcurrentandvoltage,thesystem
| cannotdeliverthefull10kWwhenoperatedatlowervoltages. |     |     |     | clusterscale. |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
9

Thisfrequencyresponseshapinghastwopracticalimpli- 1.0
cations.First,becauseEasyRiderimplementsafixedtransfer
0.8 function(Figure7)attherack-to-power-distributionconnec-
tion, any training job whose raw power spectrum falls at 0.6
orbelowthegreycurvewill,afterconditioning,satisfythe
0.4
samegridconstraintwithoutchangingthemodel,scheduler,
orGPUfirmware.Thismeansthatoperatorscanfreelyvary 0.2
workloadsaslongastheystaywithintherack’sratedpower
envelope.Aswithrampratecompliance,theguaranteecom- 0.0
0 50 100 150 200 250
posesacrossracksandrows:eachEasyRider-equippedrack Time (s)
enforcesthesameper-rackboundon𝑆 (𝑓),soahallof
grid
racksbehaveslikeacollectionof“tamed”loadsthatcanbe
integratedunderacampus-levelinterconnectionagreement.
Ineffect,EasyRiderturnsarbitraryhigh-frequencypower
fluctuationsfromtrainingintoawaveformwhoseworst-case
harmoniccontentisknownandboundedbydesign.
7.3 EnergyEfficiencyAgainstSoftwareBurn-Based
Solutions
Otherapproachestoenforcingramp-ratelimits,asdiscussed
inSection2.4,eitherrelyoncluster-widecoordinationor
use proprietary hardware that we cannot reproduce. The
mostdirectlycomparable,software-onlymechanismisto
inject“burn”kernelsthatartificiallyraiseGPUutilizationto
atargetpowerlevel.WethereforecompareEasyRidertoa
softwareburn-basedsolutiononourdecommissioned2-GPU
TitanXblade.
Toimplementthesoftwareburn,weprofileGEMMker-
nelstoderiveamappingbetweendutycycleandGPUpower,
thenusethismappingtoscheduleadditionalmatrixmulti-
plicationsthatmaintainorramptoadesiredpowersetpoint.
FulldetailsofthisimplementationappearinAppendixC.1.
Figure11showstheresultingnormalizedpowertracesfor
therawTitanXworkload,EasyRider,andsoftwareburn.We
delaythestartoftheTitanXtracebyapproximately41sto
accountforthewarm-upperiodrequiredbysoftwareburn,
andnormalizealltracestotheTitanXblade’sTDP.
WhileobservingFigure11,wenoticethatEasyRiderre-
mainsatalowerpowerlevelthansoftwareburn.Thesoft-
wareburn-basedsolutionsucceedsinsmoothingthepower
tracewithintherequiredramp-rateenvelope,butonlyby
payingforanextendedstartupphaseandahighersteady-
statepowerlevel.Takingtheintegralofthepowertrace,we
findthatsoftwareburnconsumes19%moretotalenergythan
thecombinedrack+EasyRiderconfiguration.Asanadded
benefit,EasyRiderdoesnotrequireanyadditionalwarm-up
periodorchangestothetrainingcode.WhileEasyRiderdoes
incursomelossesinitsbatteryandpowerelectronics,these
manifest as a small additional energy sink over weeks of
training,whereassoftwareburnswasteenergythroughout
everysecondofthejob.
).u.p(
rewoP
EasyRider
GPU Burn
Rack
Figure11.NormalizedpoweroftheEasyRiderprototype
andaGPUburnsmoothingaTitanXtrace.
60
50
40
)%(
CoS
Target SoC
With control
Without control
1
0
1
0 5 10 15 20
Time (min)
)A(
tnerruC Corrective
charging current
Figure12.BatteryadjustmentforanSoCthatisoverthe
desiredsetpoint.Ourcontrolsystemupdatesthecorrective
currentevery5secondstoreturnto𝑆
mid
=0.5.Withoutthis
correction,thebatterywoulddriftslowlytowardstheupper
bound.
7.4 EnergyStorageStabilityandLifetime
AsdiscussedinSection6,overhoursoftraining,oursystem
produces a monotonic SoC drift. Our software controller
existstocounteractthisdriftwithoutinterferingwiththe
hardware’sfiltering.
Figure12demonstratesthismechanisminpractice.Aftera
fewhoursofoperationwithoutsoftwarecontrol,oursystem
driftstoapproximately62%SoC.Assoonaswebeginthis
experiment,oursoftwarecontrollerallowstheinner-loopQP
(AppendixB)toissuecorrectivecurrentswhiletherackruns
the training trace. The controller updates every 5s, reads
thecurrentSoCfromtheBMS,andsolvesforamilliamp-
scaledischargecurrentthatdrivesthebatterytoward𝑆∗.The
“withsoftware”traceconvergesto𝑆 withinapproximately
mid
20minutes.The“withoutsoftware”trace,showstheSoCifit
weretoreceivenocorrectivesignal,andhowitwoulddrift
intheoppositedirectionasthehardwarepath’sset-point
biaspushestheSoCtowardtheuppersafebound.
Twopropertiesarevisibleinthefigure.First,thecorrective
current is small and changes slowly relative to the rack’s
transientcurrents,confirmingthatthecontrollerdoesnot
disturbourexistinghardwarefiltering.Second,convergence
ismonotonic,asoncetheSoCentersthedeadband|𝑆−𝑆∗| ≤
10

𝜀,thecontrollerdampsthecurrentsothatthebatteryholds fitwithintherackorimmediatelyadjacenttoittopreserve
position. the electrical behavior characterized in this paper which
Thisexperimentvalidatestheinnerloopinisolation.The willdrivemechanicalandthermalco-designbutnotrequire
outerloop’sstorage-modepolicy,whichlowers𝑆∗ during changestoupstreamsubstations.
prolongedidleintervalstoreducecalendaraging,follows
thesamecorrectivemechanismwithadifferenttargetand
thereforedoesnotrequireseparatevalidation.Thepractical
implicationisthatthesoftwarestackaddsnoper-workload
tuning,since𝑆 ,𝜀,andtheQPweightsaresetoncefrom
mid
thebatterydatasheetandthedesiredcorrectiontimescale,
andthecontrollerkeepsthebatteryinitsoptimaloperating 9 RelatedWork
bandacrossarbitrarytrainingtraces. CharacterizationofAITrainingPowerDynamics.Large
swingsincomputeloadhavebeendocumentedinHPCsys-
temsforoveradecade[6,38,42,43].Thisliteraturestudies
8 Discussion howlargecomputeclustersinteractwiththegrid,quanti-
Incrementaldeploymentacrossrowsandhalls.Akey fiesproblematicrampratesandoscillations,andconsiders
advantage of EasyRider is that it sits between each rack scheduler-level mitigation. Our setting is different, since
and the upstream power distribution. While some hyper- recent work has shown that large AI training jobs create
scalers already use in-rack UPSes or other alternatives to tightlysynchronized,multi-megawattswingswithdistinct
Figure2,EasyRidercanbedroppedinincrementallyacross temporalstructure[32,33,37].EasyRiderbuildsonthatob-
rowsandhallswithoutsubstationormid-voltageretrofits. servation,buttargetsmitigatingthesetransientrisks,not
Because racks and pods arrive in a staggered fashion [7], justcharacterizingtheloads.
thisenablesadhoc,per-rackinstallationsthatstillmaintain DatacenterPowerManagement.Priordatacenterpower-
campusramp-rateandspectrallimits. managementsystemstreatpowerasasharedresourceto
Faulttolerance.EasyRider’shardwarecontinuestofunc- allocate, cap, or oversubscribe through cluster-level con-
tionsafelyevenifitssoftwarecontrollerisoffline.Aslong trol[18,22,28,30,31,39,51,55].Similarworkusesbatteries
asthebatterybankiswithinareasonablestateofcharge, and UPSes for peak shaving and other site-level services
thesystemwillstillsmooththerackpowertraceandkeep overlongertimescales[8,41,57].Thesesystemsdetermine
ramprateswithinspec.Whensoftwareisavailable,thecon- when,where,andhowmuchpowerworkloadsmayconsume.
trollersimplyre-optimizesassumingaconstantrackpower EasyRider addresses a different layer, as it conditions the
setpoint,sothereisnocold-startpenaltywhenajobbegins rack’selectricalloadbeforethatloadreachestheupstream
orwhenthecontrollerrestarts. powerhiearchy,andisthereforecomplementarytoexisting
Minimal and isolated software. The software stack is control-planemechanisms.
deliberatelysmallanddecoupledfromtrainingjobs.Itsonly AI/MLTrainingPowerManagement.RecentworkonAI
rolesaretomeasurebatterystate-of-chargeandcurrentand trainingpowerandenergymanagementreducesenergycon-
toissueslow,correctivecurrentadjustmentsthatkeepthe sumptionbychangingtrainingbehaviorthroughprofiling,
batteryinahealthySoCandvoltagerange.Inourprototype, scheduling,DVFS,orpowercapping[11,13,26,49,54,56].
aRaspberryPipollsthebatterymanagementsystemover The goal in this literature is to improve job-level energy
Modbusandgatesbalancingcurrenttothebatterypack;this efficiency or fit workloads within cluster power budgets.
implementationisidenticalacrossracksanddoesnotinteract EasyRiderdoesnotmodifythetrainingjob;instead,itleaves
with model code, frameworks, or schedulers, simplifying theworkloadunchangedandreshapestheresultingpower
replicationandscaling. drawintherackPDU.
Costanddeploymentcomplexity.Our10kWprototype Industrycharacterizationandproposals.Existingindus-
costapproximately$3,500tobuild.Alargefractionofthis tryproposalsmitigatetrainingtransientsatdifferentpoints
billofmaterialscomesfromthe74Ahbatterypack,whichis inthestack:someshapecomputationthroughburnorpower
intentionallyoversizedrelativetotherequirementsderived capping[1,37],whileothersbufferpowerattheplatform
inAppendixA.1.Costsarehigherthanaproductiondesign orsiteboundary[24].RelatedanalysesofAIloaddynamics
becausewerelyonindividuallypurchased,commoditymod- havealsoclarifiedthegrid-sideriskcreatedbysynchronized
ulesratherthanbatterypoolingandintegratedpowerstages. trainingloads[33,37].Otherproposalsconsiderrack-level
However, in our current deployment we achieve $0.35/W storagecoordinatedwithsoftwarecontrol[12].Acrossthese
whichforaGB200rackisapproximately$66,000perrack.At efforts,thehardwareandsoftwarerolesintransientmiti-
anestimatedrackcostof$3.7M,thisislessthan1.25%ofthe gationremainonlylooselyseparated.EasyRiderisableto
rackcost.Inadeploymentsetting,theprimaryadditional managetransientsinhardwarewhichisfastandpathinde-
constraintisphysicalaswell.Thefilterandconvertermust pendentfromthesoftwarestack.
11

10 Conclusion [9] Mathias Blake, Martin Hsu, Ivan Goldwasser, Harry Petty, and
InthispaperwepresentedEasyRider,aper-rackpowersys- JaredHuntington.2025. NVIDIA800VHVDCArchitectureWill
|                     |     |          |       |        |     |             | Power the  | Next Generation                                      | of AI Factories. | NVIDIA | Devel- |
| ------------------- | --- | -------- | ----- | ------ | --- | ----------- | ---------- | ---------------------------------------------------- | ---------------- | ------ | ------ |
| tem that conditions |     | training | power | before | it  | reaches up- |            |                                                      |                  |        |        |
|                     |     |          |       |        |     |             | oper Blog. | https://developer.nvidia.com/blog/nvidia-800-v-hvdc- |                  |        |        |
streamdistributionandthegrid.EasyRidercombinesapas-
architecture-will-power-the-next-generation-of-ai-factories/
sivefilter,anactivelycontrolledrack-scalebattery,andaDC [10] EricBuskirk.2013.TorsionalDynamics;Large2-poleand4-poleSteam
regulatortopowertherackandsmoothtransientsaslongas TurbinePowertrains(GER-4724). TechnicalReport.GeneralElectric
tensofsecondsandenforcegrid-facinglimitsonramprate Company. https://www.gevernova.com/content/dam/gepower-
new/global/en_US/downloads/gas-new-site/resources/reference/
andfrequencycontentwithoutmodifyingthetrainingstack.
ger-4724-torsional-dynamics-large-2-and-4-pole-steam-turbine-
Alightweightoptimizationcontrollermonitorsandmain-
powertrains.pdf
tainsbatteryhealthovertime.Usinga10kWprototypeon [11] Sangjin Choi, Inhoe Koo, Jeongseob Ahn, Myeongjae Jeon, and
normalizedclustertracesandrealGPUtrainingworkloads, YoungjinKwon.2023.EnvPipe:Performance-preservingDNNTrain-
weshowthatEasyRidermeetsthesegridconstraintswhile ingFrameworkforSavingEnergy.In2023USENIXAnnualTechnical
Conference(USENIXATC23).USENIXAssociation,Boston,MA,851–
incurringsubstantiallylowerenergyandruntimeoverheads
864. https://www.usenix.org/conference/atc23/presentation/choi
| than software | burn–based |     | approaches. |     | Because | it sits en- |     |     |     |     |     |
| ------------- | ---------- | --- | ----------- | --- | ------- | ----------- | --- | --- | --- | --- | --- |
[12] EshaChoukse,BrijeshWarrier,ScotHeath,LuzBelmont,AprilZhao,
tirelybehindtherackPDUandreliesonlyonlocalsensing
HassanAliKhan,BrianHarry,MatthewKappel,RussellJ.Hewett,
andcontrol,EasyRidercanbeincrementallydeployedacross KushalDatta,YuPei,CarolineLichtenberger,JohnSiegler,David
existingandfuturehigh-voltageDCracks,providingaprac- Lukofsky,ZaidKahn,GurpreetSahota,AndySullivan,CharlesFred-
erick,HienThai,RebeccaNaughton,DanielJurnove,JustinHarp,
ticalpathtogrid-safeAIclustersasmodelandrackpower
ReidCarper,NithishMahalingam,SriniVarkala,AlokGautamKumb-
continuetoscale.
hare,SatyajitDesai,VenkateshRamamurthy,PraneethGottumukkala,
GirishBhatia,KelseyWildstone,LaurentiuOlariu,IleanaIncorvaia,
References AlexWetmore,PrabhatRam,MelurRaghuramanMohammedAyna,
|     |     |     |     |     |     |     | MikeKendrick,andRicardoBianchini.2025. |     |     | PowerStabilization |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | ------------------ | --- |
[1] RouslanDimitrovandHarryPettyandNeerajSrivastavaandMathias
|     |     |     |     |     |     |     | for AI Training | Datacenters. | arXiv:2508.14318v2 | [cs.AR] | https: |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | ------------------ | ------- | ------ |
Blake.2025.HowNewGB300NVL72FeaturesProvideSteadyPower
//arxiv.org/pdf/2508.14318
| forAI. | https://developer.nvidia.com/blog/how-new-gb300-nvl72- |     |     |     |     |     |                     |               |             |              |         |
| ------ | ------------------------------------------------------ | --- | --- | --- | --- | --- | ------------------- | ------------- | ----------- | ------------ | ------- |
|        |                                                        |     |     |     |     |     | [13] Jae-Won Chung, | Yile Gu, Insu | Jang, Luoxi | Meng, Nikhil | Bansal, |
features-provide-steady-power-for-ai/
|           |        |           |               |            |     |             | andMosharafChowdhury.2024. |     | ReducingEnergyBloatinLarge |     |     |
| --------- | ------ | --------- | ------------- | ---------- | --- | ----------- | -------------------------- | --- | -------------------------- | --- | --- |
| [2] Kamal | Abudu, | Uyioghosa | Igie, Orlando | Minervino, |     | and Richard |                            |     |                            |     |     |
ModelTraining.InProceedingsoftheACMSIGOPS30thSymposium
| Hamilton.                          | 2021. | Gas | turbine efficiency | and                      | ramp | rate improve- |                              |     |                              |     |     |
| ---------------------------------- | ----- | --- | ------------------ | ------------------------ | ---- | ------------- | ---------------------------- | --- | ---------------------------- | --- | --- |
|                                    |       |     |                    |                          |      |               | onOperatingSystemsPrinciples |     | (Austin,TX,USA)(SOSP’24).As- |     |     |
| mentthroughcompressedairinjection. |       |     |                    | ProceedingsoftheInstitu- |      |               |                              |     |                              |     |     |
sociationforComputingMachinery,NewYork,NY,USA,144–159.
tionofMechanicalEngineers,PartA:JournalofPowerandEnergy235,
doi:10.1145/3694715.3695970
| 4(2021),866–884. |     | arXiv:https://doi.org/10.1177/0957650920932083 |     |     |     |     |                     |                      |              |     |            |
| ---------------- | --- | ---------------------------------------------- | --- | --- | --- | --- | ------------------- | -------------------- | ------------ | --- | ---------- |
|                  |     |                                                |     |     |     |     | [14] North American | Electric Reliability | Corporation. |     | 2019. Jan- |
doi:10.1177/0957650920932083
|     |     |     |     |     |     |     | uary 11, 2019 | Oscillation | Event Report. | Technical | Report. |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ------------- | --------- | ------- |
[3] AlbertaElectricSystemOperator(AESO).2025.ConnectionRequire-
|           |                        |     |     |               |       |            | NERC. https://www.nerc.com/globalassets/our-work/reports/event- |     |     |     |     |
| --------- | ---------------------- | --- | --- | ------------- | ----- | ---------- | --------------------------------------------------------------- | --- | --- | --- | --- |
| ments for | Transmission-Connected |     |     | Data Centres. | Draft | for Stake- |                                                                 |     |     |     |     |
reports/january_11_oscillation_event_report.pdf
holderReview.AlbertaElectricSystemOperator,Calgary,Alberta.
|     |     |     |     |     |     |     | [15] North American | Electric Reliability | Corporation. | 2025. | Charac- |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | -------------------- | ------------ | ----- | ------- |
https://www.aeso.ca/VersiondatedAugust22,2025.
|             |         |      |                 |      |         |             | teristics and                                                | Risks of Emerging | Large Loads. | Technical | Report. |
| ----------- | ------- | ---- | --------------- | ---- | ------- | ----------- | ------------------------------------------------------------ | ----------------- | ------------ | --------- | ------- |
| [4] Daiyaan | Arfeen, | Zhen | Zhang, Xinwei   | Fu,  | Gregory | Ganger, and |                                                              |                   |              |           |         |
|             |         |      |                 |      |         |             | NERC. https://www.nerc.com/globalassets/who-we-are/standing- |                   |              |           |         |
| Yida Wang.  | 2025.   |      | PipeFill: Using | GPUs | During  | Bubbles in  |                                                              |                   |              |           |         |
committees/rstc/whitepaper-characteristics-and-risks-of-emerging-
| Pipeline-parallel |     | LLM | Training. In | Proceedings | of Machine | Learn- |     |     |     |     |     |
| ----------------- | --- | --- | ------------ | ----------- | ---------- | ------ | --- | --- | --- | --- | --- |
large-loads.pdf
ing and Systems, M. Zaharia, G. Joshi, and Y. Lin (Eds.), Vol. 7. [16] DeepSeek-AI,AixinLiu,BeiFeng,BingXue,BingxuanWang,Bochao
MLSys. https://proceedings.mlsys.org/paper_files/paper/2025/file/ Wu,ChengdaLu,ChenggangZhao,ChengqiDeng,ChenyuZhang,
53d3f45797970d323bd8a0d379c525aa-Paper-Conference.pdf ChongRuan,DamaiDai,DayaGuo,DejianYang,DeliChen,DongjieJi,
[5] Luiz André Barroso, Jimmy Clidaras, and Urs Hölzle. 2013. The ErhangLi,FangyunLin,FucongDai,FuliLuo,GuangboHao,Guanting
Datacenter as a Computer: An Introduction to the Design of Chen,GuoweiLi,H.Zhang,HanBao,HanweiXu,HaochengWang,
Warehouse-ScaleMachines,SecondEdition. http://dx.doi.org/10.2200/ HaoweiZhang,HonghuiDing,HuajianXin,HuazuoGao,HuiLi,
S00516ED2V01Y201306CAC024 HuiQu,J.L.Cai,JianLiang,JianzhongGuo,JiaqiNi,JiashiLi,Jiawei
[6] NatalieBates,GirishGhatikar,GhalebAbdulla,GregoryA.Koenig, Wang,JinChen,JingchangChen,JingyangYuan,JunjieQiu,Junlong
SriduttBhalachandra,MehdiSheikhalishahi,TapasyaPatki,Barry Li,JunxiaoSong,KaiDong,KaiHu,KaigeGao,KangGuan,Kexin
Rountree,andStephenPoole.2015. ElectricalGridandSupercom- Huang,KuaiYu,LeanWang,LecongZhang,LeiXu,LeyiXia,Liang
puting Centers: An Investigative Analysis of Emerging Opportu- Zhao,LitongWang,LiyueZhang,MengLi,MiaojunWang,Mingchuan
nitiesandChallenges. Informatik-Spektrum38,2(2015),111–127. Zhang,MinghuaZhang,MinghuiTang,MingmingLi,NingTian,
doi:10.1007/s00287-014-0850-0 PanpanHuang,PeiyiWang,PengZhang,QianchengWang,Qihao
[7] SaumilBaxi,KaylaCummings,AlexandreJacquillat,SeanLo,Rob Zhu,QinyuChen,QiushiDu,R.J.Chen,R.L.Jin,RuiqiGe,Ruisong
McDonald,KonstantinaMellou,IshaiMenache,andMarcoMolinaro. Zhang,RuizhePan,RunjiWang,RunxinXu,RuoyuZhang,RuyiChen,
2025. OnlineRackPlacementinLarge-ScaleDataCenters:Online S.S.Li,ShanghaoLu,ShangyanZhou,ShanhuangChen,Shaoqing
SamplingOptimizationandDeployment.arXiv:2501.12725[math.OC] Wu,ShengfengYe,ShengfengYe,ShirongMa,ShiyuWang,Shuang
https://arxiv.org/abs/2501.12725 Zhou,ShuipingYu,ShunfengZhou,ShutingPan,T.Wang,TaoYun,
[8] RicardoBianchini,ChristianBelady,andAnandSivasubramaniam. TianPei,TianyuSun,W.L.Xiao,WangdingZeng,WanjiaZhao,Wei
2024.DataCenterPowerandEnergyManagement:Past,Present,and An,WenLiu,WenfengLiang,WenjunGao,WenqinYu,WentaoZhang,
Future. IEEEMicro44,5(Sept.2024),30–36. doi:10.1109/MM.2024. X.Q.Li,XiangyueJin,XianzuWang,XiaoBi,XiaodongLiu,Xiaohan
3426478
12

Wang,XiaojinShen,XiaokangChen,XiaokangZhang,XiaoshaChen, [28] AlokGautamKumbhare,RezaAzimi,IoannisManousakis,Anand
XiaotaoNie,XiaowenSun,XiaoxiangWang,XinCheng,XinLiu,Xin Bonde,FelipeFrujeri,NithishMahalingam,PulkitAMisra,SeyyedAh-
Xie,XingchaoLiu,XingkaiYu,XinnanSong,XinxiaShan,XinyiZhou, mad Javadi, Bianca Schroeder, Marcus Fontoura, et al. 2021.
XinyuYang,XinyuanLi,XuechengSu,XuhengLin,Y.K.Li,Y.Q. {Prediction-Based} poweroversubscriptionincloudplatforms.In
Wang,Y.X.Wei,Y.X.Zhu,YangZhang,YanhongXu,YanhongXu, 2021USENIXAnnualTechnicalConference(USENIXATC21).473–487.
YanpingHuang,YaoLi,YaoZhao,YaofengSun,YaohuiLi,Yaohui [29] VivekN.Lam,XiaofanCui,FlorianStroebl,MaitriUppaluri,Simona
Wang,YiYu,YiZheng,YichaoZhang,YifanShi,YiliangXiong,Ying Onori,andWilliamC.Chueh.2025. Adecadeofinsights:Delving
He,YingTang,YishiPiao,YisongWang,YixuanTan,YiyangMa, intocalendaragingtrendsandimplications.Joule9,1(2025),101796.
YiyuanLiu,YongqiangGuo,YuWu,YuanOu,YuchenZhu,Yuduan doi:10.1016/j.joule.2024.11.013
Wang,YueGong,YuhengZou,YujiaHe,YukunZha,YunfanXiong, [30] ShaohongLi,XiWang,XiaoZhang,VasileiosKontorinis,Sreeku-
YunxianMa,YutingYan,YuxiangLuo,YuxiangYou,YuxuanLiu, mar Kodakara, David Lo, and Parthasarathy Ranganathan. 2020.
YuyangZhou,Z.F.Wu,Z.Z.Ren,ZehuiRen,ZhangliSha,ZheFu, Thunderbolt:{Throughput-Optimized},{Quality-of-Service-Aware}
ZheanXu,ZhenHuang,ZhenZhang,ZhendaXie,ZhengyanZhang, powercappingatscale.In14thUSENIXSymposiumonOperating
ZhewenHao,ZhibinGou,ZhichengMa,ZhigangYan,ZhihongShao, SystemsDesignandImplementation(OSDI20).1241–1255.
ZhipengXu,ZhiyuWu,ZhongyuZhang,ZhuoshuLi,ZihuiGu,Zijia [31] YangLi,CharlesR.Lefurgy,KarthickRajamani,MalcolmS.Allen-
Zhu,ZijunLiu,ZilinLi,ZiweiXie,ZiyangSong,ZiyiGao,andZizheng Ware,GuillermoJ.Silva,DanielD.Heimsoth,SaugataGhose,and
Pan.2025.DeepSeek-V3TechnicalReport.arXiv:2412.19437[cs.CL] OnurMutlu.2019.AScalablePriority-AwareApproachtoManaging
https://arxiv.org/abs/2412.19437 DataCenterServerPower.In2019IEEEInternationalSymposiumon
[17] ElectricReliabilityCouncilofTexas.2025. GridandMarketCondi- HighPerformanceComputerArchitecture(HPCA).701–714. doi:10.
tions.TechnicalReport.ERCOT. https://www.ercot.com/gridmktinfo/ 1109/HPCA.2019.00067
dashboards [32] YuzhuoLiandYunweiLi.2025.AILoadDynamics–APowerElectron-
[18] DanielEllsworth,TapasyaPatki,SwannPerarnau,SangminSeo,Ab- icsPerspective.arXiv:2502.01647[cs.AR] https://arxiv.org/abs/2502.
delhalimAmer,JudicaelZounmevo,RinkuGupta,KazutomoYoshii, 01647
HenryHoffman,AllenMalony,MartinSchulz,andPeteBeckman. [33] YuzhuoLi,MariamMughees,YizeChen,andYunweiRyanLi.2024.
2016. SystemwidePowerManagementwithArgo.In2016IEEEIn- TheUnseenAIDisruptionsforPowerGrids:LLM-InducedTransients.
ternationalParallelandDistributedProcessingSymposiumWorkshops arXiv:2409.11416[cs.AR] https://arxiv.org/abs/2409.11416
(IPDPSW).1118–1121.doi:10.1109/IPDPSW.2016.81 [34] Meta,Inc.2024.TheLlama3HerdofModels.arXiv:2407.21783[cs.AI]
[19] Miguel Angel Gonzalez-Salazar, Trevor Kirsten, and Lubos Prch- https://arxiv.org/abs/2407.21783
lik. 2018. Review of the operational flexibility and emissions of [35] NorthAmericanElectricReliabilityCorporation.2024.2024Long-Term
gas-andcoal-firedpowerplantsinafuturewithgrowingrenew- ReliabilityAssessment.TechnicalReport.NERC.
ables.RenewableandSustainableEnergyReviews82(2018),1497–1513. [36] NVIDIACorporation.2024.NvidiaGB200NVL72:Specificationsand
doi:10.1016/j.rser.2017.05.278 DeploymentDetails. BlackwellNVL72systemdraws120kilowatts
[20] NorthAmericanElectricReliabilityCorporationSynchronizedMea- onFP4performance.
surementWorkingGroup.2021. RecommendedOscillationAnalysis [37] JeremieEliahouOntiveros,AjeyPandey,andDylanPatel.2025. AI
forMonitoringandMitigationReferenceDocument.TechnicalReport. TrainingLoadFluctuationsatGigawatt-scale–RiskofPowerGrid
NERC. Blackout? SemiAnalysis. https://semianalysis.com/2025/06/25/ai-
[21] JamesHamilton.2009.Internet-scaleserviceinfrastructureefficiency. training-load-fluctuations-at-gigawatt-scale-risk-of-power-grid-
SIGARCHComput.Archit.News37,3(June2009),232. doi:10.1145/ blackout/
1555815.1555756 [38] Tapasya Patki, Barry Rountree, Torsten Wilde, Andrea Bartolini,
[22] Chang-HongHsu,QingyuanDeng,JasonMars,andLingjiaTang. StephanieBrink,EsaHeiskanen,SachinIdgunji,MatthiasMaiterth,
2018.SmoothOperator:ReducingPowerFragmentationandImproving JamesRogers,ErmalRrapaj,RalfSchneider,WoongShin,Kathleen
PowerUtilizationinLarge-scaleDatacenters.InProceedingsofthe Shoga,ChristianSimmendinger,NicholasJ.Wright,andZhengjiZhao.
Twenty-ThirdInternationalConferenceonArchitecturalSupportfor 2025. AGlobalPerspectiveonSupercomputerPowerProvisioning:
ProgrammingLanguagesandOperatingSystems(Williamsburg,VA, CaseStudiesfromUnitedStatesandEurope.InProceedingsofthe
USA)(ASPLOS’18).AssociationforComputingMachinery,NewYork, 39thACMInternationalConferenceonSupercomputing(ICS’25).As-
NY,USA,535–548. doi:10.1145/3173162.3173190 sociationforComputingMachinery,NewYork,NY,USA,1034–1051.
[23] Jason Adrian, Laurentiu Olariu, Banhu Sok. 2024. Mt Diablo - doi:10.1145/3721145.3734532
Disaggregated Power Fueling the Next Wave of AI Platforms. [39] LeonardoPiga,IyswaryaNarayanan,AdityaSundarrajan,MattSkach,
https://techcommunity.microsoft.com/blog/azureinfrastructureblog/ Qingyuan Deng, Biswadip Maity, Manoj Chakkaravarthy, Alison
mt-diablo---disaggregated-power-fueling-the-next-wave-of-ai- Huang, Abhishek Dhanotia, and Parth Malani. 2024. Expanding
platforms/4268799 DatacenterCapacitywithDVFSBoosting:Asafeandscalablede-
[24] PatrickKennedy.2025.Insidethe100KGPUxAIColossusClusterthat ploymentexperience.InProceedingsofthe29thACMInternational
SupermicrohelpedbuildforElonMusk. https://www.supermicro. ConferenceonArchitecturalSupportforProgrammingLanguagesand
com/CaseStudies/Success_Story_xAI_Colossus_Cluster.pdf OperatingSystems,Volume1(LaJolla,CA,USA)(ASPLOS’24).As-
[25] BrendanJKirby.2003.FrequencycontrolconcernsintheNorthAmerican sociationforComputingMachinery,NewYork,NY,USA,150–165.
electricpowersystem.TechnicalReport.ORNL. doi:10.1145/3617232.3624853
[26] GrzegorzKoszczal,JanDobrosolski,MariuszMatuszek,andPawel [40] PenghuiQi,XinyiWan,GuangxingHuang,andMinLin.2024.Zero
Czarnul.2023. PerformanceandEnergyAwareTrainingofaDeep Bubble(Almost)PipelineParallelism.InTheTwelfthInternationalCon-
NeuralNetworkinaMulti-GPUEnvironmentwithPowerCapping. ferenceonLearningRepresentations. https://openreview.net/forum?
InEuro-Par2023:ParallelProcessingWorkshops:Euro-Par2023Inter- id=tuzTN0eIO5
nationalWorkshops,Limassol,Cyprus,August28–September1,2023, [41] ZhihuiShao,MohammadA.Islam,andShaoleiRen.2020.DeepPM:
RevisedSelectedPapers,PartII (Limassol,Cyprus).Springer-Verlag, EfficientPowerManagementinEdgeDataCentersusingEnergy
Berlin,Heidelberg,5–16. doi:10.1007/978-3-031-48803-0_1 Storage.In2020IEEE13thInternationalConferenceonCloudComputing
[27] Kubernetes.2014.Kubernetes. https://kubernetes.io/ (CLOUD).370–379.doi:10.1109/CLOUD49709.2020.00058
13

[42] WoongShin,VladyslavOles,AhmadMaroofKarimi,J.AustinEllis,and [55] ChaojieZhang,AlokKumbhare,IoannisManousakis,DeliZhang,
FeiyiWang.2021.Revealingpower,energyandthermaldynamicsofa PulkitMisra,RodAssis,KyleWoolcock,NithishMahalingam,Bri-
200PFpre-exascalesupercomputer.InProceedingsoftheInternational jesh Warrier, David Gauthier, Lalu Kunnath, Steve Solomon, Os-
ConferenceforHighPerformanceComputing,Networking,Storageand valdoMorales,MarcusFontoura,andRicardoBianchini.2021.Flex:
Analysis(St.Louis,Missouri)(SC’21).AssociationforComputing High-AvailabilityDatacentersWithZeroReservedPower.InPro-
Machinery,NewYork,NY,USA,Article12,14pages. doi:10.1145/ ceedingsoftheInternationalSymposiumonComputerArchitecture
3458817.3476188 (ISCA). https://www.microsoft.com/en-us/research/publication/flex-
[43] GrantL.Stewart,GregoryA.Koenig,JingjingLiu,AndersClausen, high-availability-datacenters-with-zero-reserved-power/
SonjaKlingert,andNatalieBates.2019.GridAccommodationofDy- [56] DanZhao,SiddharthSamsi,JosephMcDonald,BaolinLi,DavidBestor,
namicHPCDemand.InWorkshopProceedingsofthe48thInternational MichaelJones,DeveshTiwari,andVijayGadepally.2023. Sustain-
ConferenceonParallelProcessing(ICPPWorkshops’19).Association ableSupercomputingforAI:GPUPowerCappingatHPCScale.In
forComputingMachinery,NewYork,NY,USA,Article9,4pages. Proceedingsofthe2023ACMSymposiumonCloudComputing(Santa
doi:10.1145/3339186.3339214 Cruz,CA,USA)(SoCC’23).AssociationforComputingMachinery,
[44] Dan Swinhoe. 2025. Proposals for 100MW natural gas- NewYork,NY,USA,588–596. doi:10.1145/3620678.3624793
powered data center campus rejected in North Carolina. [57] WenliZheng,KaiMa,andXiaoruiWang.2015.TE-Shave:Reducing
https://www.datacenterdynamics.com/en/news/100mw-natural- DataCenterCapitalandOperatingExpenseswithThermalEnergy
gas-powered-data-center-campus-proposed-in-north-carolina/ Storage. IEEETrans.Comput.64,11(2015),3278–3292. doi:10.1109/
| [45] U.S. Energy              | Information                                        | Administration.      | 2024. | Electricity use | TC.2015.2394381 |
| ----------------------------- | -------------------------------------------------- | -------------------- | ----- | --------------- | --------------- |
| in homes.                     | https://www.eia.gov/energyexplained/use-of-energy/ |                      |       |                 |                 |
| electricity-use-in-homes.php. |                                                    | Accessed:2026-04-08. |       |                 |                 |
[46] AbhishekVerma,LuisPedrosa,MadhukarR.Korupolu,DavidOp-
| penheimer,EricTune,andJohnWilkes.2015. |     |     | Large-scalecluster |     |     |
| -------------------------------------- | --- | --- | ------------------ | --- | --- |
managementatGooglewithBorg.InProceedingsoftheEuropean
ConferenceonComputerSystems(EuroSys).Bordeaux,France.
| [47] Jarred  | Walton. 2025. | Nvidia Shows        | Off Rubin | Ultra with |     |
| ------------ | ------------- | ------------------- | --------- | ---------- | --- |
| 600,000-Watt | Kyber Racks   | and Infrastructure, | Coming    | in 2027.   |     |
https://www.tomshardware.com/pc-components/gpus/nvidia-
shows-off-rubin-ultra-with-600-000-watt-kyber-racks-and-
| infrastructure-coming-in-2027 |     | Kyber | rack architecture | targeting |     |
| ----------------------------- | --- | ----- | ----------------- | --------- | --- |
600kWperrackwithRubinUltraGPUs.
[48] C.WangandS.M.Shahidehpour.1993.Effectsoframp-ratelimitson
unitcommitmentandeconomicdispatch.IEEETransactionsonPower
Systems8,3(1993),1341–1350.doi:10.1109/59.260859
[49] FaruiWang,WeizheZhang,ShichaoLai,MengHao,andZhengWang.
| 2022. DynamicGPUEnergyOptimizationforMachineLearning |                                          |     |     |     |     |
| ---------------------------------------------------- | ---------------------------------------- | --- | --- | --- | --- |
| TrainingWorkloads.                                   | IEEETransactionsonParallelandDistributed |     |     |     |     |
Systems33,11(2022),2943–2954.doi:10.1109/TPDS.2021.3137867
| [50] Keith Watson. | 2025.                                                   | Data Centers | – A Good | Grid Citi- |     |
| ------------------ | ------------------------------------------------------- | ------------ | -------- | ---------- | --- |
| zen.               | https://www.ercot.com/files/docs/2025/07/10/Eaton-Data- |              |          |            |     |
center-A-Good-Grid-Citizen.pdf
[51] QiangWu,QingyuanDeng,LakshmiGanesh,Chang-HongHsu,Yun
Jin,SanjeevKumar,BinLi,JustinMeza,andYeeJiunSong.2016.Dy-
namo:facebook’sdatacenter-widepowermanagementsystem.In
Proceedingsofthe43rdInternationalSymposiumonComputerArchi-
tecture(Seoul,RepublicofKorea)(ISCA’16).IEEEPress,469–480.
doi:10.1109/ISCA.2016.48
[52] TianyuanWu,LunxiCao,HanfengLu,XiaoxiaoJiang,YinghaoYu,
SiranYang,GuodongYang,JiamangWang,LinQu,LipingZhang,and
WeiWang.2026.AttackoftheBubbles:Straggler-ResilientPipeline
ParallelismforLargeModelTraining.In23rdUSENIXSymposiumon
NetworkedSystemsDesignandImplementation(NSDI26),Vol.23.
https:
//www.usenix.org/conference/nsdi26/presentation/wu-tianyuan
[53] WanwanXu,HuiyingCao,XingyuLin,FuchunShu,JialuDu,Junzhou
| Wang,andJunjieTang.2023. |     | Data-DrivenSemi-EmpiricalModel |     |     |     |
| ------------------------ | --- | ------------------------------ | --- | --- | --- |
ApproximationMethodforCapacityDegradationofRetiredLithium-
| IonBatteryConsideringSOCRange. |     |     | AppliedSciences13,21(2023). |     |     |
| ------------------------------ | --- | --- | --------------------------- | --- | --- |
doi:10.3390/app132111943
[54] JieYou,Jae-WonChung,andMosharafChowdhury.2023.Zeus:Under-
standingandOptimizingGPUEnergyConsumptionofDNNTraining.
In20thUSENIXSymposiumonNetworkedSystemsDesignandIm-
plementation(NSDI23).USENIXAssociation,Boston,MA,119–139.
https://www.usenix.org/conference/nsdi23/presentation/you
14

Finally,ifyouarerestrictedtousingonlysomeproportion𝛾
A HardwareComponents:Valuesand
|     | Sizing |     |     |     |     |     | ofthetotalcapacityoftheenergystoragemechanism—asin |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
thecaseofbatteries,whichmayneedtobekeptina40-60%
A.1 ComponentSizing
stateofchargetopreventrapidaging—theminimumviable
Energystoragecapacity:SupposeweareusingEasyRider storagecapacity𝐸 injoulesis
𝐵
toridethroughthepowertransientsofarackwithathemal
𝜖
| designpower(TDP)of𝑃 |     |     |       | .Thedesigndependsonan |     |     |     |     | 𝐸 𝐵 | ≥ 𝑃 𝑅𝐴𝑇𝐸𝐷 |     |     | (8) |
| ------------------- | --- | --- | ----- | --------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- |
|                     |     |     | 𝑅𝐴𝑇𝐸𝐷 |                       |     |     |     |     |     | 𝛾𝛽        |     |     |     |
adequatelysizedenergystoragesystem,whetherusingbat-
teries,supercapacitors,oranyotherstoragemechanism.The The energy storage sys-
|     |     |     |     |     |     |     | Energy | storage | power | rating: |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----- | ------- | --- | --- | --- |
DC-DCregulatorstagemaintainsthevoltageattheinputof
temmustalsobecapableofsourcingorsinkingpowerata
| therackataconstant𝑉 |     |     |     | =𝑉 ,sopowerdivertedtothe |     |     |                                                    |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | ------------------------ | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                     |     |     | 𝑂𝑈𝑇 | 𝐷𝐶                       |     |     | sufficientratetomaintaincompliancewithgridramprate |     |     |     |     |     |     |
auxiliaryenergystoragebranchatanygiventime(𝑡)is
|     |     |     |     |     |     |     | specifications. |     | From equation | 2   | we can | see that | the maxi- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------- | --- | ------ | -------- | --------- |
𝑃 𝐵(𝑡) =𝑉 ·𝑖 𝐵(𝑡) (1) mumpowerthattheenergystoragesystemmustbecapable
𝐷𝐶
ofsourcingorsinkingoccurswhentherackpowerchanges
EasyRider‘senergystoragesystemiscontrolledinour
|                           |     |     |     |                          |     |     | instantaneously                                    |     | from its | maximum | to  | minimum | value or |
| ------------------------- | --- | --- | --- | ------------------------ | --- | --- | -------------------------------------------------- | --- | -------- | ------- | --- | ------- | -------- |
| designsuchthatthecurrent𝑖 |     |     |     | isfixedbythedifferential |     |     |                                                    |     |          |         |     |         |          |
|                           |     |     |     | 𝐵                        |     |     | viceversa.Itfollowsthattheenergystoragesystemneeds |     |          |         |     |         |          |
equation
toberatedtochargeordischargeatapowerlevelofatleast
|     |     | 𝑑   |      | 𝑑    |     |     |     |     |     |             |     |     |     |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
|     |     |     | 𝑖 +𝛽 | ·𝑖 𝑖 | =0  | (2) |     |     |     |             |     |     |     |
|     |     |     | 𝐵    | 𝐵 +  | 𝑅   |     |     |     |     |             |     |     |     |
|     |     | 𝑑𝑡  |      | 𝑑𝑡   |     |     |     |     | 𝑃   | 𝐵 ≥𝜖𝑃 𝑅𝐴𝑇𝐸𝐷 |     |     | (9) |
whichensuresthatthemaximumrampratethattheEasyRider
where𝜖 isasdefinedinequation5.
| systemimposesonthegridcanneverexceed𝛽·𝑃 |     |     |     |     |     | 𝑅𝐴𝑇𝐸𝐷 ,even |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
iftherackweretoturnoffaltogether.(𝛽ischosentomeetthe Inputfiltercomponents:Theinputfilter’sprimaryfunc-
systemrampraterestrictionasshowninFigure3a,discussed tion is to attenuate high-frequency power fluctuations in
inSection3.) order to comply with the frequency content specification
Ifweassumethatattime𝑡 =0,𝑖 hasbeenconstantat laidoutinSection3.Thecontroldynamicsoftheenergystor-
𝑅
some current𝐼 for some time, and then over a period of agesystemshowninequation2alreadyensurethatpower
1
sometimeittransitionstosomecurrent𝐼 andholdssteady, fluctuationswithharmoniccontentabove𝑓 𝛽 Hzareat-
|     |     |     |     |     | 2   |     |     |     |     |     |     | 𝑏 = 2 𝜋 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
thenetenergy(injoules)storedintheduringthetransient
tenuatedbyafactorof10forevery10xincreaseinfrequency.
underidealconditionsis Becausethismaynotbeadequateonitsown,theinputfilter
|     |       | ∫   | ∞    | ∫     | ∞    |             | providesadditionalattenuationofhigher-frequencypower |     |     |     |     |     |     |
| --- | ----- | --- | ---- | ----- | ---- | ----------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |       |     |      | 𝑉 𝐷 𝐶 | 𝑑    |             |                                                      |     |     |     |     |     |     |
|     | Δ𝐸 =𝑉 |     | 𝑖 𝑑𝑡 | =−    | (𝑖   | +𝑖 𝐵)𝑑𝑡 (3) |                                                      |     |     |     |     |     |     |
|     | 𝐵     | 𝐷𝐶  | 𝐵    | 𝛽     | 𝑑𝑡 𝑅 |             | fluctuations.                                        |     |     |     |     |     |     |
|     |       | 0   |      |       | 0    |             |                                                      |     |     |     |     |     |     |
Asecond-orderLCfilterliketheoneshowninFigure5
Fromequation2weknowthatthebatterycurrentdecaysto
attenuatesrackpowerfluctuationsbyafactorofasmuch
zerowhentherackcurrentisconstant.Then
as100forevery10xincreaseinfrequencyaboveitscutoff
𝑉 𝐷 𝐶 𝑉 𝐷 𝐶 f r e qu e n c y 𝑓 . D e pe n d in g o n t h e c h a r a c te r i s tic s o ft h e ra ck
|     | Δ𝐸 =− |     | [𝑖 𝑅(𝑡)+𝑖 | 𝐵(𝑡)]𝑡 = | ∞ = (𝐼 | 1−𝐼 2) (4) |           | 𝑓            |             |                 |             |              |               |
| --- | ----- | --- | --------- | -------- | ------ | ---------- | --------- | ------------ | ----------- | --------------- | ----------- | ------------ | ------------- |
|     | 𝐵     | 𝛽   |           | 𝑡 =      | 0 𝛽    |            |           |              |             |                 |             |              |               |
|     |       |     |           |          |        |            | p o w e r | p r ofi le , | th e c u to | ff f re q u e n | c y i s c h | o s e n s uc | h t h at th e |
Themaximumchangeinrackpowerasaproportionoftotal gridpowerharmoniccontentisacceptableunderthegrid
| TDPis |     |     |           |     |     |     | specifications.Because𝑓                  |           |            | 𝑓 isafunctionofthefiltercompo- |         |             |           |
| ----- | --- | --- | --------- | --- | --- | --- | ---------------------------------------- | --------- | ---------- | ------------------------------ | ------- | ----------- | --------- |
|       |     |     | 𝑃         | −𝑃  |     |     | nentvalues,theinductance𝐿andcapacitance𝐶 |           |            |                                |         | ofthefilter |           |
|       |     |     | 𝜖 = 𝑅𝐴𝑇𝐸𝐷 | 𝑀𝐼𝑁 |     | (5) |                                          |           |            |                                |         |             |           |
|       |     |     |           | 𝑃   |     |     | should                                   | be chosen | to achieve | the                            | desired | cutoff      | frequency |
𝑅𝐴𝑇𝐸𝐷
where𝑃 istheminimum(≥0)rackpowerinwatts.Be- usingthestandardformulaforasecond-orderLCfilter:
𝑀𝐼𝑁
causetheenergystoragesystemwon’teverchargeunlessthe
1
rackpowerhasgenerallydecreased,andthesystemwon’t 𝑓 𝑓 = √ (10)
|     |     |     |     |     |     |     |     |     |     | 2𝜋  | 𝐿𝐶  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
everdischargeunlesstherackpowerhasgenerallyincreased,
themaximummagnitudeof Δ𝐸 𝐵 inequation4occursfor ThetotalsystemfrequencyresponseisshowninFigure7.
| 𝐼                         | 𝑃𝑅 𝐴 𝑇 𝐸𝐷,𝐼 | 𝑃 𝑀   | 𝐼 𝑁,themaximumandminimumpossible |     |     |     |                         |     |     |     |     |     |     |
| ------------------------- | ----------- | ----- | -------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
| 1                         | = 𝑉         | 2 = 𝑉 |                                  |     |     |     |                         |     |     |     |     |     |     |
|                           | 𝐷 𝐶         | 𝐷     | 𝐶                                |     |     |     |                         |     |     |     |     |     |     |
| rackcurrents,repectively: |             |       |                                  |     |     |     | B ControllerFormulation |     |     |     |     |     |     |
|Δ𝐸 ≤Δ𝐸 (6) T h is a p p en d i x st at e st h e o u t e r - a nd i n n e r -l oo p o p ti m i za t i o n
|     |     | 𝐵|  |     | 𝐵| 𝑃𝑅 𝐴 𝑇 𝐸𝐷,𝐼2= | 𝑃 𝑀 𝐼 𝑁 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
𝐼1= 𝑉 𝑉 pr o bl e m s s o l ve d b y E a s y R i d e r ’s so f t w a r e co n t ro l le r ( S e c -
|                                                    |     |     |     | 𝐷 𝐶 | 𝐷 𝐶 |     |         |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
| Thereforewecanconcludethatthenetenergystoredduring |     |     |     |     |     |     | tion6). |     |     |     |     |     |     |
anyrackpowertraceisboundedby
|     |     |     |     | 𝜖       |     |     | B.1 OuterLoop:SoCTargetSelection          |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | Δ𝐸  | ≤ 𝑃     |     | (7) |                                           |     |     |     |     |     |     |
|     |     |     | 𝐵   | 𝛽 𝑅𝐴𝑇𝐸𝐷 |     |     | Theouterloopselectsatarget𝑆∗fromtwomodes: |     |     |     |     |     |     |
15

Activemode(𝑆∗ 𝑆 Duringtraining,thetargetis Algorithm1Calibrationofduty→powermapping
= mid).
| fixedat𝑆 |     | topreservesymmetricheadroom. |     |     |     |     |     |                      |     |     |      |               |     |     |
| -------- | --- | ---------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ---- | ------------- | --- | --- |
|          | mid |                              |     |     |     |     |     | 1: Measureidlepower𝑃 |     |     | idle | withGPUatrest |     |     |
Whenthepredictedidleintervalexceeds𝑇 2: for𝑁 ∈N do ⊲matrixsizes
| Storagemode.                                     |     |     |     |     |     |     | enter |     |             |     |       |       |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----- | --- | ----------- | --- | ----- | ----- | --- | --- |
|                                                  |     |     |     |     |     |     |       |     | Allocate𝐴,𝐵 |     | ∈R𝑁×𝑁 | onGPU |     |     |
| andthereachableSoCreductionexceedsaminimumuseful |     |     |     |     |     |     |       | 3:  |             |     |       |       |     |     |
shiftΔ𝑆 ,thetargetdropsto 4: Calibratematmultime𝜏(𝑁)usingCUDAevents
min
|     |     |              |     |            |     |          |               | 5:  | for𝑑 ∈                       | D   |     |     |     | ⊲dutycycles |
| --- | --- | ------------ | --- | ---------- | --- | -------- | ------------- | --- | ---------------------------- | --- | --- | --- | --- | ----------- |
|     | 𝑆 ∗ | =max(cid:0)𝑆 |     | , 𝑆 mid−Δ𝑆 |     | , 𝑆      | (cid:1), (11) |     |                              | do  |     |     |     |             |
|     | s   | torage       |     | idle       | max | safe,min |               |     | forwindowsoverfixedhorizondo |     |     |     |     |             |
6:
whereΔ𝑆 =𝑖max max(0,𝑇 remain−𝑇 ready(𝑆 idle)) / (𝜂 𝑄 max) 7: RunGEMMsfortime𝑑 ·𝑇 using𝜏(𝑁)
|     | max |     |     |     |     |     | 𝑑   |     |     |     |     |     | win |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and𝑇 ready(𝑆) =(𝑆 mid−𝑆)𝑄 max/(𝜂 𝑖max)isthetimerequired Sleepforremaining(1−𝑑)·𝑇
|     |     |     |     |     | 𝑐   |     |     | 8:  |     |     |     |     |     | win |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tochargefrom𝑆backto𝑆 mid .Because𝑇 remain decreasesasthe 9: SampleGPUpower𝑃 viaNVML
idlewindowelapses,𝑆 ∗ risestoward𝑆 automatically. Record(𝑁,𝑑,𝑃,𝑃 idle)toCSV
|     |     |     | s torage |     |     | mid |     | 10: |     |     |     | −𝑃  |     |     |
| --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
When𝑇 remain <𝑇 ready(𝑆 current),thetargetrevertsto𝑆 mid .In Selectfixed𝑁★andfitlinear𝑃(𝑑) ≈𝑎𝑑+𝑏 fromCSV
11:
| ourprototype,𝑇 |     |     | =4handΔ𝑆 |     | =0.02. |     |     |                              |     |     |     | =clip(cid:0) | −𝑏)/𝑎,0,1(cid:1) |     |
| -------------- | --- | --- | -------- | --- | ------ | --- | --- | ---------------------------- | --- | --- | --- | ------------ | ---------------- | --- |
|                |     |     | enter    |     | min    |     |     | 12: Defineinversemapping𝑑(𝑃) |     |     |     |              | (𝑃               |     |
B.2 InnerLoop:Receding-HorizonQP
| LetI | =(𝑖 | ,...,𝑖 | 𝐻−1)bethecorrectivecurrentsover𝐻 |     |     |     | inter- |     |     |     |     |     |     |     |
| ---- | --- | ------ | -------------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
0
| valsoflengthΔ𝑡,andletS                              |     |     |     | =(𝑆 | ,...,𝑆 | bethepredicted |     |         |       |       |              |        |             |             |
| --------------------------------------------------- | --- | --- | --- | --- | ------ | -------------- | --- | ------- | ----- | ----- | ------------ | ------ | ----------- | ----------- |
|                                                     |     |     |     |     | 0 𝐻)   |                |     |         |       |       |              |        |             |             |
|                                                     |     |     |     |     |        |                |     | (1−𝑑)   | ·𝑇 ), | which | smoothly     | scales | the average | power       |
| SoCtrajectoryinitializedatthemeasuredvalue𝑆ˆ.Define |     |     |     |     |        |                |     |         | win   |       |              |        |             |             |
|                                                     |     |     |     |     |        |                | 𝑡   | between | idle  | (𝑑 0) | and near-TDP |        | (𝑑 1).      | Concretely, |
| normalizedvariables                                 |     |     |     |     |        |                |     |         |       | ≈     |              |        | ≈           |             |
weruntwosmallcalibrationtoolsonasingleTitanX:one
|     |     |     | 𝑖   |     | 𝑆 −𝑆∗ |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑢 𝑘 , 𝑒 𝑘 , (12) sweepsovermatrixsizes𝑁 anddutycycles𝑑 [0,1] using
|         |     |          | 𝑘 =   | 𝑘   | =       |     |     |               |     |      |         |       |         | ∈            |
| ------- | --- | -------- | ----- | --- | ------- | --- | --- | ------------- | --- | ---- | ------- | ----- | ------- | ------------ |
|         |     |          | 𝑖m ax |     | Δ 𝑆 ref |     |     |               |     |      |         |       |         |              |
|         |     |          |       |     |         |     |     | a duty-cycled |     | GEMM | loop in | fixed | windows | and logs the |
| whereΔ𝑆 |     | =𝑆 mid−𝑆 |       | .   |         |     |     |               |     |      |         |       |         |              |
ref idle resulting average GPU power to CSV, and the other uses
Theinnerloopsolves the same GEMM burner to sweep only over𝑑 for a fixed
|     | 𝐻−1         |     |     |     |     |           |     | 𝑁.Wethenfitasimplelinearmodel𝑃(𝑑) |     |     |     |     | ≈𝑎𝑑 | +𝑏 onthe |
| --- | ----------- | --- | --- | --- | --- | --------- | --- | --------------------------------- | --- | --- | --- | --- | --- | -------- |
|     | ∑︁(cid:104) |     |     |     |     | (cid:105) |     |                                   |     |     |     |     |     |          |
min 𝑒 2 +𝜆 𝑢 2 +𝜆 Δ(𝑢 −𝑢 𝑘−1)2 +𝜆 𝑒 2 (13) stableregimeofthesweepandinvertittoobtain𝑑(𝑃) for
|     |     | 𝑘 +1 | 𝐼   | 𝑘   | 𝑘   |     | 𝑇 𝐻 |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I
|     |     | 𝑘=0 |     |          |       |             |     | ourruntimerampsandcheckpointcompensation.    |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | ----- | ----------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |     | Δ𝑡  |          |       |             |     | IntegrationinTrainingLoop.InAlgorithm2weshow |     |     |     |     |     |     |
|     |     |     |     | (cid:0)𝜂 | −1[−𝑖 | 𝑘]+(cid:1), |     |                                              |     |     |     |     |     |     |
s.t. 𝑆 =𝑆 + [𝑖 𝑘]+−𝜂 (14) howweimplementourGEMMburnsduringtraining.During
|     |     | 𝑘+1 | 𝑘 𝑄 | 𝑐   | 𝑑   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
max
warmup,beforethefirsttrainingstep,werepeatedlyrunthe
|     | 𝑆   | =𝑆ˆ , |       |     |     |     | (15) |                                                    |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | --- | ---- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | 0 𝑡   |       |     |     |     |      | kernelonbothGPUs,graduallyincreasingthetargetpower |     |     |     |     |     |     |
|     | 𝑆   |       | ≤𝑆 ≤𝑆 | ,   |     |     | (16) |                                                    |     |     |     |     |     |     |
safe,min 𝑘 safe,max fromalow“warmup”leveltothenormaltrainingpowerover
|𝑖 ≤𝑖max, (17) afixedtimewindow(e.g.,30s).Thiscreatesasmoothramp
𝑘|
fromidletofullloadinsteadofastepchange.Thetraining
| where𝑢 | −1  | isthepreviouslyappliednormalizedcurrentand |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
loopisotherwisestandard,exceptateachcheckpoint.Since
| [𝑥]+                    | =max(𝑥,0).Thecontrollerappliesonly𝑖 |     |     |                                  |     | andre-solves |     |          |     |           |     |         |       |               |
| ----------------------- | ----------------------------------- | --- | --- | -------------------------------- | --- | ------------ | --- | -------- | --- | --------- | --- | ------- | ----- | ------------- |
|                         |                                     |     |     |                                  |     | 0            |     | our GPUs | are | connected | by  | NVLink, | there | is no need to |
| atthenextinterval.If|𝑆ˆ |                                     |     |     | 𝑡−𝑆∗| ≤𝜀,itsetsthecurrenttozero. |     |              |     |          |     |           |     |         |       |               |
communicateoveranetworkandthereforetheonlydipswe
| Thethreeratios𝜆 |     |     | ,𝜆  | ,𝜆 tradeofftrackingspeedagainst |     |     |     |                                                  |     |     |     |     |     |     |
| --------------- | --- | --- | --- | ------------------------------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|                 |     |     | 𝐼 Δ | 𝑇                               |     |     |     | seearefromthecheckpointingitself.Whenrank0savesa |     |     |     |     |     |     |
currentmagnitudeandcommandsmoothness.Wesetthem
checkpointanditspowerdrops,theotherGPUstemporarily
fromtwodesigntargets:thedesiredcorrectiontimescalefor
runtheburnkernelatahighertargetpowerchosensothat
arepresentativeSoCdeviation,andthedesiredsmoothness
thesumofGPUpowerstaysclosetothenormaltraining
ofthemaintenance-currenttrajectory.Theproblemisasmall
|     |     |     |     |     |     |     |     | level. All | ranks | synchronize |     | at a barrier | before | resuming |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | --- | ------------ | ------ | -------- |
convexQP,feasiblewhenever𝑆ˆ
lieswithinhardwaresafe
|     |     |     |     | 𝑡   |     |     |     | training.Afterthelaststep,werunasymmetriccooldown: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
bounds.
|     |     |     |     |     |     |     |     | both GPUs | gradually |     | reduce | their target | power | from the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | ------------ | ----- | -------- |
trainingleveldowntoalower“cool”levelusingthesame
C SoftwareComponents
burnkernel,againoverafixedtimewindow.Thisproduces
C.1 GPUBurnAlgorithmforBaseline asmoothrampdowntonear-idleinsteadofasuddendrop.
Calibration.Wefirstcalibrateatinymatrix–multiplykernel Gloo and NCCL Barriers. To make sure we can run
tolearnalinearmappingbetweenitsdutycycleandGPU checkpointburncompensationwithoutsacrificingtraining
power,andtheninvertthismappingsowecaninterpolate performance, we use a dual process group approach. We
foratargetpowerandgetbackadutycyclethatachieves initializetwoseparatePyTorchdistributedprocessgroups:a
it.Herethedutycycle𝑑 [0,1] isthefractionofeachfixed primaryNCCLgroupforalltrainingcommunication(gradi-
∈
controlwindow𝑇 thattheGPUspendsactivelyrunning entsynchronization,modelupdates),andasecondaryGloo
win
theGEMMkernel(fortime𝑑·𝑇 )versussleeping(fortime group exclusively for checkpoint barriers. NCCL barriers
win
16

40
Unfiltered cluster IT power
)WM( rewoP
|     | 30  |     |     |     |     |     |     |     |     | Simulatedgridpowerwith |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- |
EasyRiderpowersmoothing:
|     | 20  |     |     |     |     |     |     |     |     | Power from grid with  |     | =12.5% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | ------ | --- |
|     |     |     |     |     |     |     |     |     |     | Power from grid with  |     | =5%    |     |
10
|     |     |       |     |     |     |         |         |     |     | Power from grid with  |     | =1% |     |
| --- | --- | ----- | --- | --- | --- | ------- | ------- | --- | --- | --------------------- | --- | --- | --- |
|     |     | 0 100 | 200 |     | 300 | 400 500 | 600 700 |     |     |                       |     |     |     |
Time (s)
Figure13.Expectedsmoothingbehaviorofa40MWtrainingclusterwhereeveryrackisequippedwithanEasyRiderpower
supply,vs.theunfilteredcase. 𝛽 representstheEasyRider-enforcedmaximumrackpowerramprate(seeSection3),asa
proportionofmaximumratedrackpowerpersecond.TheITtrace(red)isscaledfromactualmeasurementsfromrunninga
trainingjobonH100GPUs.Thehighestrampraterecordedinthistraceoccuredwhenthesystemexperiencedacomputation
faultobservedaround400s,causinganear-instantaneousdropinpower.Atthispoint,theredtracefallsatarateof193.7
MW/sec(11.6GW/min),whichisfaroutsidetherangeofwhatconventionalgeneratorscouldcompensatefor.Alsonotethat
suchacomputationfaultwouldbedifficulttopredictinordertosmoothusingascheduledpowerburn,buttheplotshows
thatEasyRiderstillprovidessmoothingbecauseitdoesnotdependonsoftwaretelemetrytodetectpowerfluctuations.
Algorithm2GPUBurnAugmentedTraining load𝑃 𝐼𝑇(𝑡)intothesumoftheinstantaneouspowerdemands
| Calibratelinearmap𝑃(𝑑)andinverse𝑑(𝑃)usingGEMM |     |     |     |     |     |     | ofeachrack: |     |         |     |           |     |      |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --- | --------- | --- | ---- |
| 1:                                            |     |     |     |     |     |     |             |     |         |     | 𝑁         |     |      |
| burns                                         |     |     |     |     |     |     |             |     | 𝑃 𝐼𝑇(𝑡) |     | ∑︁ 𝑃 𝑖(𝑡) |     | (18) |
=
| 2: for𝑡 | =0to𝑇     | stepΔ𝑡 |         |     | ⊲warmupramp |     |     |     |     |     |     |     |     |
| ------- | --------- | ------ | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
|         |           | warm   | do      |     |             |     |     |     |     |     | 𝑖=1 |     |     |
|         | 𝑃★←lerp(𝑃 |        | ,𝑃 ,𝑡/𝑇 |     |             |     |     |     |     |     |     |     |     |
3: warm train warm) In syncronous training, because all the individual power
| 4:      | Burn(𝑑(𝑃★),Δ𝑡) |     |     |     |                |     | tracesacrossaclusterareessentiallythesame, |     |         |     |         |     |      |
| ------- | -------------- | --- | --- | --- | -------------- | --- | ------------------------------------------ | --- | ------- | --- | ------- | --- | ---- |
| 5: for𝑠 | =1to𝑆          | do  |     |     | ⊲trainingsteps |     |                                            |     | 𝑃 𝐼𝑇(𝑡) | =𝑁  | ·𝑃 𝑖(𝑡) |     | (19) |
6: TrainStep(𝑠)
if𝑠 mod𝐾 =0then ⊲checkpointevery𝐾 steps andfurthermorebecausetheDFTisalinearfunction,italso
7:
allowsscalingbyalinearmultiplier—thepowerspectrum
| 8:  |     | if rank=0then |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fortheclusterisproportionaltothepowerspectrumofthe
SaveCheckpoint(𝑠)
9:
individualracksoperatinginsynchrony:
| 10: |     | else         |     |     |                |     |     |     |         |     |         |     |      |
| --- | --- | ------------ | --- | --- | -------------- | --- | --- | --- | ------- | --- | ------- | --- | ---- |
| 11: |     | Compensate(𝑃 |     | ,𝑃  | )⊲burnonrank>0 |     |     |     | 𝑆 𝐼𝑇(𝑓) | =𝑁  | ·𝑆 𝑖(𝑓) |     | (20) |
train ckpt
12: CUDA_Barrier() ⊲synchronizeallranks Althoughtheprototypedemonstratedinthispaperisonly
13: for𝑡 =0to𝑇 stepΔ𝑡 do ⊲cooldownramp ratedfor10kWasaproofofconceptanddoesnotsinglehand-
cool
𝑃★←lerp(𝑃 ,𝑃 ,𝑡/𝑇 edlyhandleenoughpowertosmoothgrid-scalefluctuations,
| 14: |     | train | cool | cool) |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thescalingrelationsinequations19and20assertthatthe
15: Burn(𝑑(𝑃★),Δ𝑡)
normalizedresultsweshowinthepaperforasinglerack
|     |     |     |     |     |     |     | would look | identical | at  | the cluster | scale, | were every | rack |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ----------- | ------ | ---------- | ---- |
equippedwithanEasyRiderpowersupply.
enqueueoperationsontheCUDAstream,whichblockssub-
Figure13showstheexpectedsmoothingbehaviorona40
sequentGPUkernelsandpreventsourGEMMburnfrom
MWtrainingclusterwereeveryrackequippedwithanindi-
executingconcurrently,somethingthatGloobarrierswhich
vidualEasyRiderpowersupply.BecauseEasyRidersmooths
| use CPU-based                                      |     | synchronization |     | primitives | do  | not do. By |                                           |     |     |     |     |     |        |
| -------------------------------------------------- | --- | --------------- | --- | ---------- | --- | ---------- | ----------------------------------------- | --- | --- | --- | --- | --- | ------ |
|                                                    |     |                 |     |            |     |            | eachrack’spower,theaggregateclusterpower𝑃 |     |     |     |     |     | isalso |
| routingonlycheckpointsynchronizationthroughtheGloo |     |                 |     |            |     |            |                                           |     |     |     |     | 𝐼𝑇  |        |
smoothed.
groupwhilemaintainingNCCLforalltrainingoperations,
| we can | achieve | full NCCL | training | performance |     | while al- |     |     |     |     |     |     |     |
| ------ | ------- | --------- | -------- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
lowingotherGPUstoruncompensationburnsconcurrently
duringcheckpointing.
D ExplanationofSmoothingatScale
ThesmoothingeffectofEasyRideratthecampus-widescale
followsfromthefactthatthetotaldatacenterpoweruseis
| a sum | of all | the individual | system | demands. |     | For a cluster |     |     |     |     |     |     |     |
| ----- | ------ | -------------- | ------ | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
spreadacrossNracks,wecanbreakdownthetotalclusterIT
17