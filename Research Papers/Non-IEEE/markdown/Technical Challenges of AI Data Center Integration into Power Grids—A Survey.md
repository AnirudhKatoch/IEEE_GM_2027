Article
Technical Challenges of AI Data Center Integration into Power
Grids—A Survey
ElinorGinzburg-Ganz1,* ,PavelLifshits1 ,RamMachlev1,* ,JuriBelikov2 ,ZivKrieger1
andYoashLevron1
1 TheAndrewandErnaViterbiFacultyofElectricalandComputerEngineering,Technion—IsraelInstituteof
Technology,Haifa3200003,Israel;pavell@technion.ac.il(P.L.);ziv.krieger@campus.technion.ac.il(Z.K.);
yoashl@ee.technion.ac.il(Y.L.)
2 TheDepartmentofSoftwareScience,TallinnUniversityofTechnology,12618Tallinn,Estonia;
juri.belikov@taltech.ee
* Correspondence:elinor.g12@gmail.com(E.G.-G.);ramm@technion.ac.il(R.M.)
Abstract
The rapid expansion of Artificial Intelligence is fueling the growth of hyperscale data
centers,whichintroducessignificantchallengestoexistingpowersystems. Thispaperaims
toprovideacomprehensivesurveyoftheseintegrationchallenges,specificallyfromthe
perspectiveofpowergridutility. WefindthatAIdatacentersfunctionasadistinctload
category,characterizedbyhighpowerdensity,rapidandlarge-scalepowertransients,and
specificpowerqualityprofiles. Theseattributescreatedifficultiesforlong-termresource
adequacyandtransmissionplanningduetomismatcheddevelopmenttimelines. Theyalso
strainreal-timegridbalancingandintroduceriskstosystemstability,suchasvoltageand
frequencydeviationsandconverter-driveninstabilities. Theanalysisfurthercoverstheeco-
nomicandenvironmentalfootprintsassociatedwiththisnewtypeofconsumer. Thepaper
concludesthatsafelyintegratingtheseloadsrequiresacoordinatedstrategy,encompassing
datacenter-sidetechnologies,grid-enhancingsolutions,andnewpolicyframeworks.
Keywords: AIdatacenters;powersystems;loadmodeling;gridstability;energydemand
1. Introduction
TheriseoffoundationalAImodels,particularlyLargeLanguageModels(LLMs),is
fuelingsignificantgrowthinthesizeandscaleofdatacentersworldwide. Thisexpansion
isnecessarytohousethespecializedcomputinginfrastructurerequiredforAIworkloads.
Inrecentyears,thenumberofoperationalhyperscalefacilities,whicharecentraltothis
trend,hasnearlytripledtoover1100[1,2].
TrainingfoundationalAImodelsincursanexceptionallyhighcomputationalcost[3].
AcademicEditor:MarcinKaminski Theprocessinvolvesintensivepre-trainingonvastdatasets,oftenspanningseveralmonths
andrequiringthesynchronizedoperationofhundredsofthousandsofprocessors[4–6].
Received:17November2025
Revised:11December2025 This computationally intensive process is required due to the large scale of these new
Accepted:24December2025 model architectures, now containing hundreds of billions or even trillions of parame-
Published:26December2025 ters, asdetailedinTable1basedon[4,7], withnotableexamplesincludingmodelslike
Copyright:©2025bytheauthors. GPT-3,with175billionparameters,andsubsequentmodelssuchasGrok-1,with314bil-
LicenseeMDPI,Basel,Switzerland.
lionparameters.
Thisarticleisanopenaccessarticle
Theunprecedentedsizeandcomplexityofthesemodelshavebeenpreviouslycon-
distributedunderthetermsand
sidered infeasible [5]. This rapid scaling was allowed due to recent technological ad-
conditionsoftheCreativeCommons
Attribution(CCBY)license. vancements,bothonthesoftwareandonthehardwarelevels,allowinghighparallelism
Energies2026,19,137 https://doi.org/10.3390/en19010137

Energies2026,19,137
2of35
duringcomputationalphasesofthetrainingprocess. Specifically,themaindriverswere
advancedparallelcomputinghardwaresuchasGraphicsProcessingUnits(GPUs)and
TensorProcessingUnits(TPUs).
Table1.LLMworkloadscharacterizedforinferenceanalysis,basedon[4,7].
| Model                  | Parameters | ReleaseDate  |
| ---------------------- | ---------- | ------------ |
| RoBERTa[8]             | 355M       | July2019     |
| Grok-1[9]              | 314B       | March2024    |
| Llama-3.1[10]          | 70B        | July2024     |
| Llama-3.1[10]          | 405B       | July2024     |
| Llama2[11]             | 13B        | July2023     |
| Llama2[11]             | 70B        | July2023     |
| GPT-3[12]              | 175B       | June2020     |
| GPT-4o[13]             | 200B       | May2024      |
| GPT-NeoX[14]           | 20B        | February2022 |
| OPT[15]                | 30B        | May2022      |
| BLOOM[16]              | 176B       | July2022     |
| Flan-T5XXL[17]         | 11B        | December2022 |
| WuDao1.0[18]           | –          | January2021  |
| WuDao2.0[19]           | 1.75T      | June2021     |
| Megatron-TuringNLG[20] | 530B       | October2021  |
Thistechnologicalshifttowardslarge-scale,general-purposeAIintroducesacorre-
spondingchallengerelatedtoitssubstantialenergyfootprint. Thetotalpowerdemand
fromdatacenters,worldwide,isforecastedtoincreasefromroughly55GWtoover122GW
by2030, representingmorethanatwofoldincrease[21]. Thisprocessisdrivenbynew
capacity,withanestimated10GWexpectedtobreakgroundin2025alone. Thescaleof
individual projects highlights this trend: for example, the “Stargate” supercomputer is
planned to consume 5 GW of power, while Meta is developing its 1 GW “Prometheus”
clusterandafuture5GW“Hyperion”facility[22]. Thisconcentrationofdemandisalready
impactingregionalsystems. Virginia,oneoftheworld’slargestdatacenterhubs,servesas
aclearexample,wherefacilitieswerealreadydrawingover3GWofpowerin2024[23].
TherapidexpansionofAIisthereforeestablishingitasasubstantialandrapidlygrowing
consumerofenergy.
This,inturn,createsunprecedentedchallengesforthedesignandoperationofpower
grids,assummarizedinseveralrecentreports[5,24–26]. Aprimaryissueisthesheerscale
andspeedofdevelopmentofdatacenters,whichfaroutpacegridplanning. InERCOT,
forexample,theinfluxoflargeloadsisprojectedtoincreasepeakdemandfrom85GWto
150GWby2030,creatingsignificantuncertaintyforlong-termforecasting[27]. Moreover,
therapidandextremepoweroscillationsfromdatacenters,whicharedominatedbypower
electronics equipment, introduce dynamic stability problems for the electric grid [25].
Theseoscillationscancausevoltageflickerandexciteharmfulfrequencyandpowerangle
instabilitiesthatcanaffecttheentirepowersystem. Furthermore, thetendencyofdata
centerequipmenttotripofflinesimultaneouslyduringgridfaultscreatesariskofsudden,
large-scaleloadlossevents,suchasarecent1.5GWtripacross60datacentersinDominion
Energy’sterritory[25]. Suchanabruptdisconnectioncancausenearbygeneratorstolose
synchronism,threateningtheoverallstabilityandintegrityofthepowergrid[25,26].
The rapid integration of these large-scale data centers introduces unprecedented
challenges for power grid design and operation, as highlighted in several recent re-
ports [5,24–26]. One major challenge is that the scale and speed of this development
faroutpacetraditionalgridplanning,amismatchthatcreatessignificantlong-termforecast-
inguncertainty. AnotableexamplemaybeseeninERCOT,wheretheinfluxoflargeloads
https://doi.org/10.3390/en19010137

Energies2026,19,137 3of35
isprojectedtoincreasepeakdemandfrom85GWto150GWby2030[27]. Thechallenges
posedbythesefacilitiesextendbeyondlong-termplanning,andincludedynamicstability
problemsfortheelectricgrid. Thesedynamicproblemsarisemainlyduetotheextensive
use of power electronics equipment for the operation of data center facilities [25]. This
equipmentmaycauserapidandextremepoweroscillations,whichinturn,resultinlocal
disturbancessuchasvoltageflickerandharmfulfrequencyorpowerangleinstabilities
thatmaycascadegloballyacrossthepowersystem. Furthermore,datacenteroperators
usuallyuseprotectiveequipmenttoensurethecontinuousoperationoftheworkloads.
Asthisequipmentsensesanyslightdisturbanceonthepowerline,itmaydisconnectthe
wholefacility,makingittripofflineduringgridfaults,creatingariskofsudden,large-scale
loadloss. ArecenteventinDominionEnergy’sterritory,where60datacenterstripped
andcauseda1.5GWloadloss,illustratesthisvulnerability[25]. Moreover,nearbygenera-
torsmaylosesynchronismduetosuchsuddendisconnectionofthismagnitude,which
jeopardizesthecontinuousandsafeoperationofthepowergrid[25,26].
Given the profound and rapidly evolving challenges at the intersection of AI data
centersandpowergrids,acomprehensivesurveyisneeded,representingtheutilitygrid
perspective. Existingliteratureoftenaddressesaspectsofdatacenterenergyefficiencyor
thebroaderimplicationsofAIonenergyconsumption,asmaybeseenin[28–31].
Table 2 delineates the scope of this survey in relation to these prior works. While
previousstudiesprovidevaluableinsightsintointernalenergyoptimization,sustainability
metrics,andcomponent-levelreliabilitymodeling,theypredominantlyanalyzethedata
center as a static facility or focus on software-level efficiency. This survey extends this
line of works by characterizing AI training and inference as distinct, highly dynamic
electricalloads. Itshiftstheanalyticalperspectivefromthefacility’sinteriortotheutility
connectionpoint,specificallyaddressingthegridstabilityrisks,powerqualitydisturbances,
andtransmissionplanningconstraintsintroducedbytherapiddeploymentofhyperscale
AIinfrastructure.
Table2.Comparisonwithrelatedworks.
Energy Load AIWorkload GridStability Utility
Work Sustainability
Efficiency Modeling Specifics Risks Perspective
[28] ✓ ✓ ✓ ✗ ✗ ✗
[30] ✓ ✓ ✗ ✗ ✗ ✗
[29] ✓ ✗ ✗ ✗ ✗ ✗
[31] ✓ ✗ ✓ ✗ ✗ ✗
ThisWork ✓ ✓ ✓ ✓ ✓ ✓
Indeed,inlightofpreviousliterature,itisclearthatthereremainsagapinabroadview
ofthetechnicalchallengesexperiencedbytheutilitygrid,drivenbythisunprecedented
demand,fromoperational,economic,andpolicystandpoints. Thissurvey,assummarized
inFigure1,aimstosynthesizethelatestresearchinacademiaandindustryinsightsto:
1. CharacterizetheuniquepowerdemandsofAIworkloads: Movingbeyondaggregate
consumptionfigurestodetailthetransient,volatilenatureoftheseloadsandtheir
specificimpactongridstability.
2. Systematically analyze grid-side challenges: Providing a detailed breakdown of
capacityconstraints,interconnectionbottlenecks,powerqualitydegradation(voltage,
frequency,harmonics),andreliabilityrisks,withreal-worldexamples.
3. Explore the economic and environmental ramifications: Presenting economic con-
siderationsimposedonutilitiesandratepayers,andassessingtheimplicationsfor
decarbonizationeffortsandclimategoals.
https://doi.org/10.3390/en19010137

Energies2026,19,137 4of35
4. Identifyandevaluatestrategicsolutions: Presentinganoverviewofapproachesrang-
ingfrominternaldatacenterefficiencyimprovementsanddemand-sidemanagement
toon-sitegeneration(renewables,nuclear)andadvancedenergystoragesystems.
5. Examine the evolving regulatory landscape: Analyzing federal and state-level
policy responses and proposing recommendations for effective industry-utility-
policymakercollaboration.
Byfocusingspecificallyontheutilitygrid’sperspective,thisreviewoffersauniqueand
timelycontributiontothediscourse,providingcriticalinsightsforgridoperators,energy
policymakers,datacenterdevelopers,andtechnologycompanies. Itseekstobridgethe
understandinggapbetweentherapidlyadvancingdigitaleconomyandthefoundational
energyinfrastructure,fosteringamoreinformedandcollaborativeapproachtoensureboth
digitalcontinuityandgridresilienceinanAI-drivenfuture.
Powering the
AI Revolution:
Contributions
HolisticChallengesSurvey IntegratedSolutions
Grid-CentricPerspective
•Technical&Operational •Solutionsonthedatacenterside
•Firstreviewfromutility’sview
•Economic&Policy •Solutionsontheutilitygridside
•Focusongridstabilityimpacts
•Environmental&Life-Cycle •Collaborativesolutions
Fostering Sustainable & Resilient
AI-Grid Integration
Figure1. Overviewofthepaper’scontributions, emphasizingtheintroductionofagrid-centric
perspective alongside a consolidated survey of technical, operational, environmental, and eco-
nomicchallenges.
2. Background: TheAIDataCenterasaDynamicPowerLoad
Tofullyunderstandthegrid-sidechallengesoutlinedintheintroduction,itisessential
tofirstunderstandwhyAIdatacentersbehaveassuchuniqueanddynamicloads. Unlike
traditional data centers with relatively stable and predictable power consumption, AI
facilitiesexhibithighlyvariableandrapidpowerfluctuations. Thisvolatilitystemsfrom
twoprimaryfactors: thecomplex,multi-stageinternalpowerarchitecturerequiredtofeed
power-hungryprocessors,andthedistinctoperationalprofilesofAIworkloads,particularly
theintensive,burstynatureoftrainingandthefluctuatingdemandsoflarge-scaleinference.
Thissectiondelvesintothesetwoaspects,characterizingtheinternalpowerdeliverychain
andthespecificpowersignaturesofAItrainingandinferencetasks,whichtogetherdefine
theAIdatacenterasaninfluentialdynamicloadonthepowergrid.
2.1. InternalPowerArchitecture
The power distribution system within a data center, from external sources to the
individual GPUs, is characterized by an engineered hierarchy designed for continuous
operation,reliability,andefficiency. AsseeninFigure2,theflowofpowertotheGPUs
https://doi.org/10.3390/en19010137

Energies2026,19,137
5of35
beginswiththeutilityfeed. Forenhancedreliability,datacentersoftenreceivemultiple
redundantfeedsfromdifferentsectionsofthelocalpowergridtopreventasinglepointof
failure. Thisincominghigh-voltagepowerfirstpassesthroughmaintransformers,which
stepitdowntoalower,moremanageablevoltagesuitableforthedatacenter’sinternal
infrastructure. Concurrently,thelocalgeneratorsstandreadyasasecondary,long-term,
high-capacitypowersource,typicallydieselornaturalgas-powered,toprovideelectricity
duringextendedutilityoutages. Thispowerismanagedbyswitchgear,whichactsasthe
initialpointofcontactfortheutilitypower. Thissystemdistributestheincomingpower
andincludesAutomaticTransferSwitches(ATS)thatseamlesslyswitchthedatacenter’s
loadbetweentheutilitygridandthebackupgeneratorsintheeventofagriddisturbance.
Fromtheswitchgear,powerflowstoUninterruptiblePowerSupply(UPS)systems. These
arecriticalcomponentsthatprovideimmediate,short-termbackuppower, alsoknown
as“ride-through”capability, forbriefgridfluctuationsoruntilthegeneratorscanfully
startup,whichtypicallytakesabout10–15s. UPSsystemsalsoplayavitalroleinpower
conditioning, protectingsensitiveITequipmentfromvoltagefluctuations, sags, swells,
andotherpowerqualityissuesthatcanleadtoequipmentmalfunctionordatacorruption.
After conditioning at the UPS level, power is distributed throughout the facility
viaPowerDistributionUnits(PDUs). TheselargeunitsreceivepowerfromtheUPSor
directlyfromthemainswitchgear,anddistributeittovarioussectionsofthedatacenter,
often breaking it down into smaller circuits for more granular management. From the
PDUs,powerisfurtherdistributedtoRemotePowerPanels(RPPs),whichactaslocalized
distributionpointswithinthedatacenter. TheseRPPsthenfeedpowertorack-mounted
PDUs(rPDUs),whichareessentiallypowerstripslocatedwithineachserverrack. Finally,
withineachserver,PowerSupplyUnits(PSUs)converttheACpowerfromtherPDUinto
thelow-voltageDCpowerrequiredbytheserver’sinternalcomponents,includingthe
CPUs,memory,storagedevices,andultimately,theGPUs. TheGPUsthenconsumethis
powerfortheirintensivecomputationaltasks,particularlyforthetrainingandinference
tasksoflargefoundationalmodels. Toperformthistask,theGPUsdemandhighpower
densities,oftenexceedingdozensofkWperrackandsometimesreaching100kWperrack.
Theentiresystemisdesignedwithmultiplelayersofredundancytoensurecontinuous
operationandminimizedowntime.
Monitoring
Transfertime
Coolingsystem
inseconds
|     |     |     | Network | Generator   | MainAutomatic  |
| --- | --- | --- | ------- | ----------- | -------------- |
|     |     |     |         | Utilitygrid | TransferSwitch |
server1→PSU
VM1
|       |       | .   | .           |       |      |
| ----- | ----- | --- | ----------- | ----- | ---- |
|       | APPa1 | .   | .           | rPDUA | UPSA |
|       |       | .   | .           |       |      |
|       |       | VMv | servers→PSU |       |      |
|       | .     |     |             | rPDUB | RPPA |
| User1 | . .   |     |             | .     | PDUA |
.
|     |     | VM1 |     | .   | RPPB |
| --- | --- | --- | --- | --- | ---- |
.
|     |       | . . | . . |     | . PD UB |
| --- | ----- | --- | --- | --- | ------- |
|     | APPam | .   | .   |     | . .     |
.
.
VMv
server1→PSU
.
|     |       | . . | .   | rPDUA |     |
| --- | ----- | --- | --- | ----- | --- |
|     | APPa1 | .   | .   |       |     |
servers→PSU
|       | .   |     |     | rPDUB |     |
| ----- | --- | --- | --- | ----- | --- |
| Userk | .   |     |     | .     |     |
|       | .   |     |     | . .   |     |
VM1
Transfertimein
|     |       | .   | scaleofmilliseconds |     |     |
| --- | ----- | --- | ------------------- | --- | --- |
|     | APPam | . . |                     |     |     |
VMv
Figure2.Illustrationofthedatacenterpowerdistributionarchitecture.
https://doi.org/10.3390/en19010137

Energies2026,19,137 6of35
2.2. PowerProfilesofAITrainingandInferenceWorkloads
The power consumption of an AI data center is primarily determined by its com-
putational function: model training or model inference. These two workloads present
fundamentallydifferentenergyprofiles. AItrainingischaracterizedbyasustained,high-
utilizationpowerdrawoverlongdurations. Incontrast,AIinferenceisdefinedbyhigh-
volume,latency-sensitivetransactionsthatresultinamorevolatileloadprofile,inasense,
sincethetaskarrivaltimeisunknown. Whilethispaperfocusesonthestabilitychallenges
posedbyAItraining,understandingthisdichotomyprovidesessentialcontext.
ThedistinctpowerprofileofAItrainingoriginatesfromitscomputationalstructure.
Trainingisanofflineprocessthatrefinesamodel’sparametersbyprocessingverylarge
datasets. Thisinvolvesaniterativeoptimizationprocess,centeredonthebackpropagation
algorithm,whichrequiresbothaforwardandasubsequentbackwardpassofdatathrough
theneuralnetwork. Thiscycleisrepeatedmillionsoftimes,creatingacomputationally
intensive load that persists for the duration of the training job, which can span from
daystoweeks. Theresultisasustainedhigh-powerdemandthat,whilepersistentover
the job’s duration, is not monolithic. Instead, the profile exhibits significant volatility,
withitsunpredictabilitystemmingfromtheworkload’sconstantcyclingbetweencompute-
intensive phases, where power draw is near its maximum, and communication-heavy
phases,whereconsumptiondropssharply.Inthiscontext,theprimaryoperationalobjective
is to maximize throughput to achieve model accuracy, with real-time latency being a
secondaryconcern.
To demonstrate these ideas, a training simulation is designed to profile the power
characteristicsofacompletedeeplearningtrainingworkloadontheTeslaT4GPU,thecode
maybeviewedhere[32]. ItutilizesaResNet50modelandasyntheticdatasettocreatea
consistentandreproduciblecomputationalload. Theprocessexecutesforapredefined
numberofepochs,processingafixedquantityofbatcheswithineachepoch. Toenable
granular analysis, the monitoring system precisely captures the constituent phases of
eachtrainingstep. Thesystemlogsdistinctstatesforforwardpassandbackwardpass
operations. Furthermore,acommunicationstateisexplicitlysimulatedaftereachoptimizer
stepbysynchronizingtheCUDAdeviceandintroducingabrief,fixeddelay. Thissmall
pauserepresentstheoverheadthatmightbeincurredduringgradientsynchronizationina
distributedtrainingsetup,thusprovidingamorecompleteprofileofthetrainingcycle.
Conversely,theinferenceworkloadisanonline,operationalphasewhereatrained
modelmakespredictionsonnewdata. Computationally,thisprocessislighter,requiring
only a forward pass through the network for each query. However, inference is highly
time-sensitive,aslowlatencyisarequirementforuser-facingapplications. Thisresultsina
volatileandunpredictablepowerconsumptionpattern,withsharppeakscorresponding
tofluctuatinguserrequests[4]. Whiletheenergyconsumedperqueryissmall,thecumu-
lativeenergyfootprintofinferenceoveramodel’slifecycleissubstantial. Thiscontrast
underscoreswhythesustained,high-powernatureofthetrainingworkloadpresentsa
uniqueandconcentratedchallengetothestabilityofitsdedicatedpowersupplysystem.
Tohighlightthediscussedbehavior,aninferencesimulationisdesigned,emulatinga
service-orientedenvironment,suchasamodelendpoint,whichrespondstoasynchronous
userrequests. Thisworkloadprocessesaspecifiednumberofinferencequeries, where
theinter-arrivaltimebetweeneachqueryismodeledstatistically. WeselectedaGamma
distributiontogovernthetimebetweensequentialrequests,whichintroducesarealistic,
stochastic pattern of query arrivals instead of a uniform or Poisson back-to-back work-
load[33]. Consequently,thesystemalternatesbetweentwodefinedstates: processinga
batch,whentheGPUisactivelyexecutingtheinference,and“waitingforqueries”during
theidleperiods.
https://doi.org/10.3390/en19010137

Energies2026,19,137 7of35
Figures 3 and 4 present the results of the integrated analysis of power consump-
tion,thatrevealsafundamentaldichotomybetweenAItrainingandinferencebehaviors.
Asillustratedinthepowerprofilecomparison,thetrainingworkloadexhibitsasustained,
high-powerdemandprofile,characterizedbyameanconsumptionof61.2Wandconsis-
tentpeaksreaching87.0W.Thisbehaviorreflectsthecontinuous,batch-processingnature
of training algorithms (backpropagation), effectively presenting to the grid as a heavy,
block-loadstepchange. Incontrast,theinferenceworkloaddemonstratesahighlyvolatile,
stochasticprofile. Whileitsmeanpowerconsumptionislower(51.5W),itexhibitsaggres-
sivetransientbehaviorwithsharp,sub-secondrampsfromanidlestateof25.7Wtoapeak
of91.0W,notablyhigherthanthetrainingpeak. Thisburstysignaturecorrespondstothe
randomarrivalofuserqueries,creatingrapidloadoscillationsthatposedistinctchallenges
forpowerqualityregulationcomparedtothesteadycapacitydemandoftraining.
Theunderlyingdriverforthesepowervariancesisevidentintheresourceutilization
andmemorymetrics.Thetrainingphasemaintainsnear-saturationlevelsofGPUutilization
(often hitting 100%) and a static, elevated memory footprint (approximately 30–40%)
requiredtostoremodelparameters,gradients,andbatchdata. Thisconsistentresource
engagementresultsinasteadythermalramp-up,asseeninthetemperatureprofilewhich
climbs from 35 ◦C to over 45 ◦C without significant fluctuation. Conversely, inference
utilizationoscillatesrapidlybetween0%and80%,causingimmediatethermalripplesrather
thanasmoothascent. Thememoryusageforinferenceremainslowandconstant,reflecting
thelightercomputationaloverheadofprocessingsinglequeries.Thesecomparativemetrics
underscorethatwhiletrainingstressesthegrid’senergycapacityandthermalmanagement
systemsthroughsustainedload,inferencestressesthegrid’stransientstabilitythrough
rapid,high-magnitudepowerswitchingevents.
80
60
40
20
0
0 2 4 6 8 10 12 14 16
100
50
0
0 1 2 3 4 5 6 7 8 9
Figure3. Comparisonoftherhythmic,high-meanpowerprofileofthetrainingphaseagainstthe
highlyvolatile,stochasticloadprofileoftheinferencephaseduetosporadicarrivals,highlighting
thedistincttransientbehaviorsandpeak-to-idletransitionsimposedonthepowersupplyforthe
TeslaT4GPU.
Furthermore,Figure5,whichplotsthetrainingandinferencepowerprofileovertime,
visuallycapturesthetransitionbetweendifferentstatesineachtypeofworkload. Forthe
trainingsimulation,thepowerprofileischaracterizedbyasustained,high-powerdraw.
Thissignaturereflectstherapidandcontinuouscyclingthroughthedefinedoperational
states. Thesystemtransitionsimmediatelyfromforwardpasstobackwardpass,andthen
toabriefcommunicationphaseforeachbatch. Becausethesetransitionsaresequential
withalmostnoidleperiod,theGPUremainsunderaconstant,heavycomputationalload,
resultingintheobservedrapidpowerconsumptiontransients. Notethatsometimesthe
https://doi.org/10.3390/en19010137

Energies2026,19,137
8of35
computationalphaseswerefasterthanthesamplingfrequency,thus,partoftheforward
andbackwardpasswasnotrecorded.
50
45
40
35
| 0 1 | 2 3 | 4 5 | 6   | 7 8 9 |
| --- | --- | --- | --- | ----- |
100
50
0
| 0 1 | 2 3 | 4 5 | 6   | 7 8 9 |
| --- | --- | --- | --- | ----- |
100
50
0
| 0 1 | 2 3 | 4 5 | 6   | 7 8 9 |
| --- | --- | --- | --- | ----- |
Figure4. ComparisonofGPUtemperature,utilization,andmemoryusagebetweentrainingand
inferenceprocessesfortheTeslaT4GPU.
Incontrast,theinferencesimulationplotdisplaysahighlyintermittentandbursty
pattern. Here, the transitions between states are visually pronounced. The plot shows
sharpascentstoahigh-powerpeak,whichcorrespondstotheactivebatchprocessingstate.
Thisisfollowedbyanabruptdescenttoalow,baselinepowerlevel. Thislow-powerstate,
labeled“waitingforqueries”,representstheidletimebetweenstochasticqueryarrivals
andpersistsuntilthesystemtransitionsbacktotheactiveprocessingstateuponreceiving
thenextrequest.
| 90  |       | 100  |     |        |
| --- | ----- | ---- | --- | ------ |
| 80  |       | 90   |     |        |
| 70  |       | 80   |     |        |
| 60  |       | 70   |     |        |
| 50  |       | 60   |     |        |
| 40  |       | 50   |     |        |
| 30  |       | 40   |     |        |
| 20  |       | 30   |     |        |
| 0 5 | 10 15 | 20 0 | 2 4 | 6 8 10 |
Figure5.TeslaT4GPUstatetransitionsintimeduringanAItrainingandinferencesimulation.Note:
Thegrayplussignsdenoteinitiationandcompletionofthetrainingprocess.
To validate these power consumption characteristics on additional AI accelerator
hardware,acomprehensivemonitoringexperimentisconductedusingGoogle’sTPUv5e-1.
TheexperimentalsetupemploysagainaResNet50modelimplementedinPyTorch2.9.1
withXLAbackendforTPUcompatibility,utilizingsyntheticdatasetstoensurereproducible
workloadpatterns. ThemonitoringsystemcapturesTPUmetricsat50-msintervals,track-
ingpowerconsumption,temperature,coreutilization,memoryusage,andTPU-specific
MatrixUnit(MXU)utilization.Fortrainingworkloads,theexperimentprocesses14batches
perepochacross2epochswithabatchsizeof48,whileinferenceworkloadshandle20query
batchesofsize64withstochasticinter-arrivaltimesfollowingaGammadistribution(shape
https://doi.org/10.3390/en19010137

Energies2026,19,137 9of35
α =2,scaleβ =0.1s). TheTPUmonitoringframeworkleverageshardwareperformance
counterswhenavailableandemploysstate-basedpowerestimationmodelscalibratedto
thev5e-1’s75Wthermaldesignpowerspecification.
Theexperimentalresults,presentedinFigures6–8demonstratedistinctpowercon-
sumptionpatternsanddivergentoperationalmetricsbetweentrainingandinferencephases
ontheTPUv5e-1architecture. Duringtraining,theTPUmaintainsasustainedmeanpower
consumptionof58.3Wwithconsistentpeaksreaching71.2W,reflectingthecontinuous
computationaldemandofforwardandbackwardpropagationpasses. TheMXUutilization
exhibitscorrespondingstability,averaging68.4%duringtrainingphaseswithpeaksreach-
ing89.2%,indicatingefficienttensoroperationscheduling. Temperaturemeasurements
showagradualthermalrampfrom42◦Cto57◦Coverthetrainingduration,stabilizingat
theelevatedlevelduetoconsistentworkloadintensity. Memoryutilizationremainsrela-
tivelyconstantat41.3%oftheavailable16GBHBM,storingmodelparameters,gradients,
andbatchdatathroughoutthetrainingprocess.
60
40
20
0
0 500 1000 1500
60
40
20
0
0 5 10 15 20 25
Figure6. Comparisonoftherhythmic,high-meanpowerprofileofthetrainingphaseagainstthe
highlyvolatile,stochasticloadprofileoftheinferencephaseduetosporadicarrivals,highlightingthe
distincttransientbehaviorsandpeak-to-idletransitionsimposedonthepowersupplyforGoogle’s
TPUv5e-1.
80
70
60
50
0 5 10 15 20 25
100
50
0
0 5 10 15 20 25
100
50
0
0 5 10 15 20 25
Figure7. ComparisonofTPUtemperature,utilization,andmemoryusagebetweentrainingand
inferenceprocessesforGoogle’sTPUv5e-1.
https://doi.org/10.3390/en19010137

Energies2026,19,137 10of35
90
80
70
60
50
40
30
20
10
0
0 5 10 15 20 25
Figure 8. Temporal analysis of MXU utilization for Training vs. Inference phases for Google’s
TPUv5e-1.
Theinferencephaserevealsmarkedlydifferentbehavior,withpowerconsumption
oscillatingbetweenanidlebaselineof22.4Wandpeaksof68.7W,drivenbythestochastic
queryarrivalpattern. Theserapidtransitionsoccurwithinsub-secondintervals,creating
powertransientsofupto46.3Wthatstressthepowerdeliverysystem. MXUutilization
duringinferencedemonstratessimilarvolatility,droppingtonear-zeroduringidleperiods
andspikingto74.8%duringqueryprocessing. Thetemperatureprofilerespondstothese
fluctuationswithripplesof±3◦Caroundameanof48◦C,neverreachingthethermalsatu-
rationobservedduringtraining. ThisexperimentalvalidationonTPUhardwarereinforces
thefundamentaldichotomybetweenAIworkloadtypes,wheretrainingpresentsasasus-
tainedhigh-powerblockloadwhileinferencemanifestsasahighlydynamic,transientload
withrapidpowerstatetransitionsthatchallengetraditionalgridintegrationassumptions.
3. Grid-SideTechnicalChallengesandReliabilityRisks
Theintegrationofmulti-gigawattAIdatacenters,characterizedbytheirvolatileand
power-electronic-denseloadprofiles, presentsaspectrumofunprecedentedchallenges
tothepowergrid. Thesechallengesextendfromthedecades-longtimescalesofsystem
planningdowntothesub-seconddynamicsofsystemstability.Thisrapidescalationingrid-
relatedconcernsisreflectedintherecentacademicandtechnicalliterature,withasignificant
concentrationofreportsandpapersemergingin2025. Thissurveysystematicallyexamines
thesegrid-sidetechnicalchallengesandtheirassociatedreliabilityrisks,withahigh-level
overview of the section’s structure provided in Figure 9. To further contextualize the
currentresearchlandscape,Figure10providesastatisticalanalysisofrecentpublications,
illustrating the research focus across the subsections of this survey (The reference list
includes only those sources cited in the Section 3, rather than an exhaustive list of all
publicationsreferencedinthiswork.). Interestingly,manyofthesepublicationsarefrom
recent years, indicating the growing interest in this sector. We then move to real-time
operationalhurdlesinbalancingsupplyanddemand,followedbyanin-depthanalysis
ofcriticalpowersystemstabilityrisksandpowerqualitydegradation. Finally,weassess
the cascading economic impacts on utilities and ratepayers, and conclude with a life-
cycle perspective on the broader environmental and resource intensity of this rapidly
growingconsumer.
https://doi.org/10.3390/en19010137

Energies2026,19,137
11of35
Grid-SideTechnicalChallenges
|     | Long-Term |     | Real-Time  |     |     | Stability |
| --- | --------- | --- | ---------- | --- | --- | --------- |
|     | Planning  |     | Operations |     |     | Risks     |
• Datacenterdeployment • RapidAIworkloadrampsare • Massdatacenter
outpacesgridexpansion, hardtopredictanddraingrid disconnectionsduringgrid
straininglong-termcapacity reserves faultsriskcascadingsystem
failure
| •   | Poorforecastingandlong | • Abruptloadchangesthreaten |     |     |     |     |
| --- | ---------------------- | --------------------------- | --- | --- | --- | --- |
interconnectionqueuescreate real-timegridbalancewith • Powerelectronicsconcentration
majorintegrationbottlenecks voltageandfrequencyswings createsnewrisksofharmonic
resonanceandinstability
|     | PowerQuality |     | Economic   |     |     | Environmental |
| --- | ------------ | --- | ---------- | --- | --- | ------------- |
|     | Risks        |     | Challenges |     |     | Challenges    |
• Datacenters’non-linearloads • Broadgridupgradecostsspark • Anenvironmentalassessment
createharmonicdistortion, conflictoverwhopays: data mustincludeoperational
degradingpowerquality centersorallratepayers energy,embodiedcarbon,
| •   | Fastpowerchangescause | • Localtaxbenefitsareweighed |     |     | andwateruse |     |
| --- | --------------------- | ---------------------------- | --- | --- | ----------- | --- |
voltageflickerforothergrid againstcommunityopposition • Serverhardware’sembodied
|     | customers | torisingbillsandnoise |     |     | carbonisasignificant,upfront |     |
| --- | --------- | --------------------- | --- | --- | ---------------------------- | --- |
impact,separatefrom
operationalemissions
Figure9.Grid-sidetechnicalchallengessummary (organizedfromtop-lefttobottom-right).
16
15
|                      |     | Economicchallenges     |                | Real-time&Balancing |     |     |
| -------------------- | --- | ---------------------- | -------------- | ------------------- | --- | --- |
|                      |     | Environmentalfootprint |                | Long-termplanning   |     |     |
| snoitacilbupforebmuN |     |                        | Stabilityrisks | Powerquality        |     |     |
10
8
7
|     |     |     | 5 5 | 5   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
5
0
Figure10.Distributionofpapersacrossdifferentcategories.
3.1. Long-TermPlanningandInterconnectionChallenges
TheintegrationofAIdatacentersintothepowergridintroducessignificantlong-term
planningandinterconnectionchallenges. Thesechallengesoriginatefromafundamental
temporalmismatchbetweentherapiddeploymentcyclesofdatacenterinfrastructureand
themuchlongertimehorizonsrequiredforpowersystemexpansion. Thisdisparityaffects
boththeabilitytoensuresufficientgenerationcapacityandthedevelopmentofadequate
transmissioninfrastructure,creatingriskstothegrid’slong-termreliability.
Resourceadequacy,whichistheabilityofthepowersystemtomeettheaggregate
electricaldemand,isstrainedbythistimelineimbalance. Datacenterfacilitiescanoften
beconstructedandbroughtonlinewithin12to24months[25]. Incontrast,theplanning,
approval,andconstructionofnewlarge-scalegenerationresourcestypicallyspanfiveyears
ormore[25]. Consequently,aregioncanexperiencearapidincreaseinelectricitydemand
thattheexistinggenerationfleetandplannedadditionsarenotequippedtohandle,leading
topotentialshortfallsinsupply.
https://doi.org/10.3390/en19010137

Energies2026,19,137 12of35
A similar and often more pronounced challenge exists for transmission adequacy.
The development of new high-voltage transmission lines is a complex process involv-
ing lengthy regulatory approvals, permitting, and construction phases. These projects
frequently require five to ten years for completion [25]. This extended timeline creates
significantinterconnectionbottlenecksfordatacenters, leadingtolongqueuesfornew
largeloads.Asaresult,datacenterdevelopersmayprioritizelocationsbasedonimmediate
poweravailability,whichcanconcentratenewloadinareaswherethetransmissionsystem
isalreadyconstrained.
Beyondthephysicalinfrastructuredelays,long-termplanningisfurthercomplicated
bysignificantgapsinloadforecastingandmodeling. Gridplannersandoperatorsoften
lackaccurateandvalidateddynamicmodelsthatcanproperlycharacterizethebehavior
oftheselarge,power-electronic-basedloads[25]. Unliketraditionalaggregateddemand,
whichbenefitsfromthestatisticalsmoothingeffectofmillionsofuncorrelatedconsumers,
AI data centers represent large, single-point loads with highly correlated internal oper-
ations [34–37]. This characteristic diminishes the predictability that is foundational to
conventionalloadforecastingmodels.Theuncertaintyisamplifiedbycommercialpractices
wherecompaniessubmitinterconnectionrequestsinmultipleregionstoevaluatethemost
favorableconditions[25]. Thismakesitdifficultforplannerstodeterminewhichproposed
projectsarefirmcommitments,therebycomplicatingeffortstoproducereliablelong-term
demandforecasts.
3.2. Real-TimeOperationsandBalancingChallenges
ThevolatileandmassivepowerconsumptionprofilepresentedbyAIdatacenters
introducesdistinctchallengesforthereal-timemanagementofthepowergrid. Thehighly
variable and rapid changes in their power demand complicate short-term forecasting,
andplacesignificantstrainonthesystem’sabilitytobalancethegenerationandload.
Short-term demand forecasting is made more difficult by the stochastic nature of
AItrainingworkloads. Unliketraditionalloads,thepowerconsumptionofalarge-scale
trainingclusterdoesnotfollowpredictabledailyorweeklypatterns. Instead,itisdictated
bytheinitiation,execution,andcompletionoftrainingjobs,whichcancauselarge,abrupt
changesinpowerdemand[5]. Thepowerprofilewithinasingletrainingiterationconsists
of compute-heavy phases, where power draw is near maximum, and communication-
heavyphases,wherepowerconsumptiondropssignificantly[4]. Theserapidfluctuations,
whichcanoccuronasub-secondtimescale,arechallengingforgridoperatorstopredict
accuratelyusingconventionalforecastingmodelsthatrelyonhistoricaltrendsandslower-
movingvariables.
Thisvolatilitydirectlyimpactsthegrid’sbalancingandreservemanagement. Acore
principleofreliablegridoperationismaintainingacontinuousbalancebetweenelectricity
generationanddemand,sinceimbalanceinactiveorreactivepowersignificantlyimpacts
thevoltagemagnitudeatabus. ThisrelationshipcanbeexpressedusingVoltageSensi-
tivityFactors(VSF)[38]: ∆V = S ∆P +S ∆Q,where∆V isthechangeinvoltage
i VP,i i VQ,i i i
magnitudeatbusi,and∆P,∆Q arecolumnvectorsrepresentingthechangesinactive
i i
andreactivepoweratthearbitrarybuseswherethesechangesoccur. ThematricesS
VP,i
andS arethevoltagesensitivityfactors,specificallydenotingthevoltagesensitivityto
VQ,i
activepowerandreactivepowerrespectively. Datacenters,withtheirrapidactivepower
ramps,anddynamicreactivepowerdemands,causehigh∆Pand∆Qvalues. Theserapid
changescanleadtosignificantvoltagedeviationsthatconventionalgriddevicesaretoo
slowtocompensate[39,40].
Theconsumedpowerofthedatacenterdirectlyaffectsthevoltageattheconnection
point (PCC). For a simplified radial connection from a source, such as an infinite bus,
https://doi.org/10.3390/en19010137

Energies2026,19,137 13of35
throughalineimpedance Z = R +jX tothedatacenterload,theapproximate
line line line
voltage drop, ∆V, across the line is given by ∆V ≈ (R P +X Q )/|V |,
line L,DC line L,DC PCC
where P and Q arethe activeandreactivepowerconsumed bythedatacenter,
L,DC L,DC
and |V | is the voltage magnitude at the PCC. The voltage at the PCC can then be
PCC
approximated,|V | ≈ |V |−∆V = |V |−(R P +X Q )/|V |,where|V |
PCC g g line L,DC line L,DC PCC g
isthevoltagemagnitudeofthesource. Thisanalysis,althoughrelyingonapproximated
quasi-staticmodels,explainshowchangesintheactiveandreactivepowerconsumedby
thedatacenterinverselyinfluencethevoltagemagnitudeatthePCC.Thisisafundamental
challenge, ashyperscaledatacentersdemandexceptionallyhighactivepower, leading
to significant voltage drops, especially in weak grids or at the end of long distribution
lines[41].
Tomanagesuchunexpecteddeviations,systemoperatorsmaintainvarioustypesof
operating reserves. However, the ramp rates of AI data centers, which can change by
hundredsofmegawattsinseconds,areoftenmuchfasterthantheresponsecapabilitiesof
conventionalgenerators,whicharetypicallymeasuredinmegawattsperminute[25,42].
AsshownintheNERCreport,adatacenter’sloadcanrampdownbyover400MWin
just36s[25]. Suchrapidloadchangescanquicklyexhaustthegrid’sprimaryfrequency
controlandbalancingreserves. Tomanagethesefastramps,systemoperatorsmayneed
to procure larger amounts of more expensive and faster-acting ancillary services, such
as Fast-Frequency Response, which increases operational costs [25]. Without sufficient
fast-actingreserves,thesesuddenloadchangescanleadtosignificantfrequencydeviations,
posingarisktogridstability.
3.3. PowerSystemStabilityRisks
ThedynamicandunpredictablebehaviorofAIdatacenterloadsposesdirectrisks
topowersystemstability. Themostsignificantoftheserisksstemsfromtheprotective
mechanismswithindatacentersthemselves,whichcantriggercascadingeventsacrossthe
widergrid.
Aprimarystabilityconcernisthevoltageandfrequencyride-throughbehaviorofdata
centers. ToprotectsensitiveITequipmentandensureserviceuptime,datacentersarede-
signedwithinternalprotectionsystemsthatdisconnectthemfromthegridduringvoltage
orfrequencydisturbances[25]. Whilethisactionpreservestheindividualfacility,thesi-
multaneousdisconnectionofmultiplelargedatacenterscancreateaseveresystem-wide
disturbance. Thisphenomenon,whereindividualreliabilitymeasurescreateacollective
vulnerability,canbedescribedasaself-preservationparadox. Anotableexampleofthis
occurredinJuly2024,whenatransmissionlinefaultintheEasternInterconnectioncaused
avoltagedisturbancethattriggeredthesimultaneouslossofapproximately1500MWof
load,primarilyfromdatacenterstransferringtobackuppowersystems[25,43].
Suchlarge-scale,near-instantaneousloadsheddingeventshavedirectconsequences
forfrequencystability. Whenalargeamountofloadissuddenlyremovedfromthesystem,
thegenerationimmediatelyexceedstheremainingdemand. Thispowersurpluscausesthe
rotationalspeedofsynchronousgeneratorsacrosstheinterconnectiontoincrease,leading
toasystem-wideover-frequencyevent[25]. IntheJuly2024incident,thelossof1500MW
ofloadcausedthegridfrequencytoriseto60.053Hzbeforecontrolactionscouldrestore
thebalance[25]. Conversely,thesuddenstartofalargeAItrainingjobcancreateanunder-
frequencyeventiftheadditionalloadisnotanticipatedandmatchedbyanequivalent
increaseingeneration.
To demonstrate this concept, we perform a simulation to investigate the system’s
dynamic response to a realistic AI workload. The system model formulation includes
apowerarchitecturethatincludesthedatacenterload,adedicatedlocalpowersource,
https://doi.org/10.3390/en19010137

Energies2026,19,137
14of35
andaconnectiontotheexternalutilitygrid. Thedatacenter’stotalpowerconsumptionis
(t).
denotedbyP L,DC Itismetbythesumofpowerfromitslocalsynchronousgenerator,
|     | P(t),andpowerdrawnfromthegrid,P |     | (t). |     |     |
| --- | ------------------------------- | --- | ---- | --- | --- |
g Theutilitygridistreatedasaninfinitebus.
The behavior of the synchronous generator is governed by the swing equation, which
incorporatesastandarddroopcontrolmechanismtomanagethegenerator’sfrequency
deviation∆ω
androtorangleδ. Byapplyingtheprincipleofpowerconservationatthe
pointofcommoncoupling,thegenerator’sswingequationiscombinedwiththeACpower
flowequationdescribingthegridconnection.Thisprocessyieldsacoupledsetoffirst-order
differentialequationsthatdefinethesystem’sdynamicsintermsofthestatevariablesδ
and∆ωasfollows
d
δ = ∆ω,
dt
(cid:18) ||E|(cid:19) (1)
|     |     | d    |                | 3K|E      | K   |
| --- | --- | ---- | -------------- | --------- | --- |
|     |     | (∆ω) | = K(P −P (t))+ | g sin(δ)− | ∆ω. |
ref L,DC
|     |     | dt  |     | X   | D   |
| --- | --- | --- | --- | --- | --- |
Todemonstratethesystem’sdynamicbehaviorunderrapidloadchanges,simulations
areperformedusingMATLABR2024bandSimulink.Theanalysismodelsthecharacteristic
AIloadbasedondatacollectedduringaResNet50trainingprocessonaTeslaT4GPU,
whichisthenscaledtorepresenta100×103
GPUcluster, simulatingalarge-scaledata
centeroperation. Thisloadismanagedbyasystemwithbaselineparametersrepresenting
aplausibledatacenterscenario,includinga17.41MWratedgeneratoranda17.41MW
gridconnection. Thisconfigurationprovidesapowertransfercapabilitytwicethatofthe
loadstep. Thenominalsystemfrequencyis60Hz,andthegenerator’sreferencepowerP
ref
isinitiallysetto3.058MW,whichishalfoftheappliedloadincrease.
A comprehensive parametric study is then conducted to investigate the system’s
sensitivitytokeydesignchoices. Thedampingcharacteristicαisvariedacrossfivevalues
from0.01to100s−1. Thesimulationsarerunfor17.7s,employingnumericaltoleranceand
stepsizesettingsdesignedtoensureaccuracy. TheparametersaresummarizedinTable3.
Table3.SummaryofSimulationParameters.
| Variable | Value  | Units | Explanation                         |     |     |
| -------- | ------ | ----- | ----------------------------------- | --- | --- |
| P        | 50×106 | [W]   | Themaximalpowerdrawnbythedatacenter |     |     |
L,DC
|     | 75–200×106 |            | Theexpression(3|Eg||E|)/X   |     |     |
| --- | ---------- | ---------- | --------------------------- | --- | --- |
| Px  |            | [W]        |                             |     |     |
| Prt | 100×106    | [W]        | Theratedpowerofthegenerator |     |     |
| fs  | 60         | [Hz]       | Nominalelectricalfrequency  |     |     |
| ws  | 2π·60      | [rad/s]    | Nominalelectricalfrequency  |     |     |
| K   | 0.5–4×K    | [1/(W·s2)] | Generator’sinertiaconstant  |     |     |
base
12.5–50×106
| Pref |     | [W] | 3phasegenerator’sreferencepower |     |     |
| ---- | --- | --- | ------------------------------- | --- | --- |
α 0.01–100 [1/s] ThefractionK/D,whereDisthegenerator’sdroopconstant
| SimTime | 10  | [s] | Simulationtime |     |     |
| ------- | --- | --- | -------------- | --- | --- |
1×10−4
| RelTol* |        | -   | Simulationaccuracy    |     |     |
| ------- | ------ | --- | --------------------- | --- | --- |
| MaxStep | 1×10−3 | [s] | Simulationmaxstepsize |     |     |
*Thissolverparameterensurestheerrorscalesinproportiontothecalculatedvalue.
Thesimulationresults,presentedinFigure11,demonstrateafundamentaltrade-off
betweensystemstabilityandcomponentstresswhenageneratorrespondstoasudden
loadincrease. Ahighdampingfactor(α)effectivelysuppressesfrequencyandangleoscilla-
tions,allowingthesystemtostabilizequickly. However,thisrapidstabilizationdemands
largerpowerpeaksfromthegenerator,placingsignificanttransientstressonitshardware.
Conversely,alowerdampingfactorreducesthesepowerovershootsandcomponentstress
butallowsthesystemtooscillateforalonger,potentiallydestabilizing,period.
https://doi.org/10.3390/en19010137

Energies2026,19,137 15of35
ThisbalanceiscriticalforAIdatacenters,whichproducecontinuous,high-frequency
loadfluctuations. Inthisenvironment,ahighdampingsettingthatseemsbeneficialfora
singleeventcouldbedetrimental. Itmightcausethegeneratortoconstantlyreacttothe
volatile load, leading to excessive mechanical wear and a reduced operational lifespan.
Therefore,thedampingcharacteristicmustbeselectedwithcaretobalancetheneedfor
a fast transient response with the long-term reliability required to handle the unique,
persistentlyfluctuatingloadprofileofAItraining.
Figure11.Impactofvaryingdroopconstantsonthepower(P),frequency(f),androtorangle(δ)ofa
synchronousgeneratorandgridsystemduringafluctuatingAItrainingworkload.
Toquantifythesystemperformanceunderthesevaryingdampingconditions,Table4
presentstheRootMeanSquareErrorandMeanAbsoluteErrorforbothfrequencyand
rotor angle deviations. A clear inverse relationship exists between the damping coeffi-
cient α and the frequency error metrics. Specifically, as α increases from 0.01 to 100.00,
theFrequencyRMSEdecreasesfrom0.2090Hzto0.0073Hz. Similarly,theMeanAbsolute
Errorforfrequencydropsfrom0.1727Hzatthelowestdampingsettingto0.0064Hzatthe
highestsetting. Thesevaluesindicatethathigherdampingcoefficientseffectivelyconstrain
frequencyexcursionstoanarrowbandaroundthenominal60Hzvalue.
The rotor angle stability exhibits a corresponding trend where increased damping
significantlyreducesangulardeviationsfromtheequilibriumpoint. TheRMSEforthe
relativeanglediminishesfrom17.9674degreesatαequals0.01to6.9838degreesatαequals
100.00. WeobserveasimilarreductionintheMAEmetric,whichfallsfrom14.1121degrees
to 6.3865 degrees across the same range. The intermediate damping value of α equals
1.00 yields an angle RMSE of 11.3524 degrees and represents a transitional state where
thesystemmaintainsstabilitywithoutimposingtheextremerigidityassociatedwiththe
highestdampingvalues. Thisquantitativereductioninerrormetricsathigherdamping
levelsconfirmsthatthesystemcreatesastifferresponsetotheloadfluctuations.
Table4.ErrorMetrics:RMSEandMAEAnalysis.
RMSE MAE
Metric α= 0.01 α= 0.10 α= 1.00 α=10.00 α=100.00 α= 0.01 α= 0.10 α= 1.00 α=10.00 α=100.00
Frequency(f [Hz]) 0.2090 0.1777 0.0735 0.0248 0.0073 0.1727 0.1486 0.0602 0.0190 0.0064
Rel.Angle(δ[deg]) 17.9674 16.1249 11.3524 10.1607 6.9838 14.1121 12.8820 10.1580 9.3312 6.3865
Referencevalues: fs =60Hz(nominalfrequency),δn =0deg.
https://doi.org/10.3390/en19010137

Energies2026,19,137 16of35
To further visualize these stability margins, we analyze the phase plane portraits
shown in Figure 12. This plot illustrates the trajectory of the system state, defined by
the frequency deviation ∆ω and the relative rotor angle δ−δ∗, as it converges toward
the equilibrium point. The trajectories for low damping values, specifically α = 0.01
and α = 0.10, exhibit wide, spiraling orbits that span a large area of the state space.
These extensive excursions indicate a highly oscillatory response where the generator
rotorundergoessignificantangularswingsandfrequencydeviationsbeforesettling. Such
behaviorsuggestsasystemwithlowstabilitymargins,whereasubsequentloadspikefrom
anAItrainingbatchcouldeasilypushtherotoranglebeyonditscriticallimit,resultingin
alossofsynchronism.
In contrast, the trajectories for higher damping values, such as α = 10.00 and
α = 100.00, demonstrate a tightly constrained response where the system state moves
rapidlyanddirectlytowardtheequilibrium. Whilethisconfinementeffectivelyminimizes
theriskofangularinstability,itphysicallyrepresentsascenariowherethegeneratorgover-
noraggressivelycounteractseverydeviation. InthecontextofAIworkloads,whichare
characterizedbystochasticandrapidpowerpulses,thisaggressivecontrollogicforcesthe
mechanicalcomponentstoendurehigh-frequencystresscycles. Consequently,thephase
planeanalysisreinforcestheconclusionthatoptimalparameterselectionliesintheinter-
mediaterange,suchasα =1.00,whichcreatesabalancebyrestrictinghazardousangular
excursionswithoutimposingtheexcessiverigiditythatacceleratesequipmentdegradation.
Figure12. Phaseplaneportraitshowingsystemsstabilitytrajectoriesoftherotoranglerelative
to its equilibrium point (δ−δ∗ in [deg]) of a synchronous generator as a function of the grid’s
frequencyrelativetothenominalfrequency(∆ωin[rad/s]),forafluctuatingAItrainingworkload
consumptionprofile.
Voltage stability is also compromised by mass load-tripping events. The sudden
disconnection of large loads, which consume both active and reactive power, can lead
to a surplus of reactive power on the local transmission system. This excess reactive
powercancausearapidandsignificantvoltagerise,orovervoltage,thatcandamageother
connectedequipmentandpotentiallyinitiatefurtherprotectivetripping,increasingthe
riskofcascadingoutages[25].
Furthermore,thehighconcentrationofpowerelectronicconverterswithinAIdata
centersintroducesrisksofconverter-driveninstabilityandresonance. Theseelectronicde-
viceslackthephysicalinertiaoftraditionalelectromechanicalequipmentandaregoverned
byfast-actingcontrolsystems. Thesecontrolscaninteractnegativelywiththeelectrical
characteristicsofthegrid,potentiallyreducingthedampingofnaturalsystemoscillations
orcreatingnew,unstableoscillations[25]. Forexample,aneventin2023demonstratedthat
powerelectronicsatalargedatacenterinadvertentlyperturbedthelocalsystemata1Hz
https://doi.org/10.3390/en19010137

Energies2026,19,137 17of35
frequency. Thisactionrepeatedlyexcitedanatural11Hzresonantfrequencyinthegrid,
producingapersistentforcedoscillationthatposedarisktosystemreliability[25].
To better understand the source of this behavior, we can examine the system in
thephasordomain. Naturally, datacenters, asnon-linearloads, aresignificantsources
of harmonic distortion. The non-sinusoidal current drawn by the data center contains
harmoniccomponents. Theseharmonicsaregeneratedbytheswitchingactionsofpower
electronicconverterswithinUPSsystems,ITpowersupplies,andvariablefrequencydrives
forcooling. ThelevelofcurrentdistortionisquantifiedbytheTotalHarmonicDistortion
(THD)ofthecurrent,withhighTHD indicatingsignificantcurrentdistortion. Whenthese
I
harmoniccurrentsflowthroughtheimpedanceofthegrid, Z ,theygenerateharmonic
h
voltages,V ,acrossthesystem. Foraspecificharmonicfrequencyω = nω,theharmonic
h h
voltageisV = I ·Z (ω ),whereZ (ω )isthegrid’simpedanceatthen-thharmonic
h DC,h h h h h
frequency, meaning that even if the source voltage is perfectly sinusoidal, the voltage
atthepointofcommoncouplingwiththedatacenterwillbecomedistortedduetothe
harmoniccurrents.
Acriticalissueariseswhenloadswithcapacitiveprofile,C ,areconnectedtooneof
p
thebuses. Indeed,moderndatacenterITloads,governedbypowerelectronics,typically
present a capacitive load profile. This stems from the fact that the IT equipment itself,
namely,theservers,storage,andnetworkingdevices,usesswitch-modepowersupplies
thatarerequiredtohavePowerFactorCorrection(PFC)circuits. ThesePFCcircuitsalmost
universallyusefiltercapacitorsattheirinputstage,resultinginthecapacitivenatureof
the data center. While the overall data center’s power factor is a complex mix of these
capacitiveITloadsandtheinductivecoolingloads[44],thepowerelectronicsattheserver
levelaretheprimarysourceofthecapacitivenature,notaninductiveone. Thisleading
powerfactorfromITloadsisaknownchallenge,asitcaninteractpoorlywiththeinductive
componentsofthegridandthedatacenter’sownbackupUPSsystems[45,46].
In this scenario, these capacitors may create a parallel resonance with the grid’s
inductivecomponents,L ,ataharmonicfrequencyω . Theimpedanceofsuchaparallel
s h
combinationisgivenbyZ = jωhLs . If1−ω2L C ≈0,theimpedanceZ approaches
infinity,leadingtoanampl h ifica 1 ti − o ω n h 2 o Ls f C h p armonicv h ol s tag p es,meaningV → ∞,e h venforsmall
h
harmoniccurrents. Althoughtheseoscillationsmayremainwithinsafetymargins,they
cancauseoverheatingandequipmentdamage.
3.4. PowerQuality
Powerqualityisameasureofthedegreetowhichvoltageandcurrentwaveforms
complywithestablishedspecifications[47]. Recentresearchworks,including[25,48],high-
lightthatlargedatacenters,oftenreachinghundredsofmegawattsandrelyingonpower
electronicsequipment,introducenewpowerqualityconcerns. Akeychallengeistherapid
fluctuationinpowerdemand,whichcanproducesuddenloadrampswithinmilliseconds
andmakeitdifficulttomaintainpowerqualitywithinspecifiedlimits. Furthermore,inre-
gionswhereseveralcentersoperatefromthesamegridnode,simultaneousfluctuations
cancreatesubstantialpowerqualitydisturbances.
More specifically, the power electronics systems common in data centers, such as
UPS units (Illustrated in Figure 2), and variable-speed drives for cooling, operate with
high-frequency switching. This process generates non-linear currents that distort the
grid’s voltage waveform. These harmonic distortions, illustrated in Figure 13a, are a
primarydisturbance. Forinstance,arecentreport[25]documentsadatacenterfacilitythat
producedexcessivevoltageharmonicdistortion,whichwassignificantenoughtorequire
theinstallationofadedicatedharmonicmitigationsolution. Withoutsuchfiltering,these
non-linear currents can interact with grid components. This interaction poses a risk of
https://doi.org/10.3390/en19010137

Energies2026,19,137 18of35
parallelresonance, whichcanamplifyharmonicvoltagesandleadtoproblemssuchas
transformeroverheating,increasedequipmentlosses,andgeneralcomponentstress.
Voltagesags,swells,andshortinterruptionsalsoposesignificantrisks(Figure13b).
Datacentersarehighlysensitivetobriefvoltagedipsthatcaninterruptserversorcooling
systems. Whenfacilitiestransfertobackupgenerators,thesuddendisconnectionoflarge
loadscanproducesharpchangesinvoltageandfrequency,similarinimpacttoamajor
generationtrip.
Thesepowerqualityissuesarefurthercompoundedbythelimitedvisibilitythatgrid
operatorshaveintodatacenterloads. Thislackofdatahinderstheabilityofsystemopera-
torstoaccuratelyforecastloadbehaviorunderbothnormalanddisturbanceconditions.
Manydatacenteroperatorsmanagetheiron-sitesystemsprivately,meaningtheirinternal
switchingprotocolsandloadrampingactionsarenotfullytransparenttoutilities.
Toconclude,powerqualityproblemsindatacentersarisefromrapidloadvariations,
non-linearcurrentprofiles,voltagesensitivity,andunstablereactivepowerbehavior,all
of which may degrade overall power quality. Addressing these issues requires coordi-
natedplanningbetweenutilitiesandoperators,improvedharmonicfiltering,andclear
interconnectionstandards.
1
0
−1
0 50 100 150 200 250
Time (ms)
(a)
).u.p(
egatloV
(b)
Figure13. Examplesofgrid-sidevoltagedisturbancesobservedatthepointofcommoncoupling
(PCC)ofadatacenter:(a)harmonicdistortionfrompower-electronicloads(THD≈8–10%)suchas
UPSrectifiers,powersupplies,andcoolingdrives;and(b)voltagesag(0.8p.u.,3cycles)andswell
(1.1p.u.,2cycles)causedbyfastloadstepssuchasGPU-clusteractivationorcoolingramp-up.
3.5. EconomicChallenges
The costs of training frontier AI models have grown dramatically in recent years,
reachingbillionsofdollars[3]. Thissectionanalyzesthefinancialdimensionsoftherapid
increaseinenergydemanddrivenbyAI,includingthecostsofnecessarygridmodern-
ization, thecontentiousdebateoverwhobearsthesecosts, thedisruptionofwholesale
electricitymarkets,andthecomplex,oftencontradictory,socio-economicimpactsonlo-
calcommunities.
ThescaleofinvestmentrequiredtobuildthephysicalinfrastructurefortheAIrevolu-
tionisimmense. Arecentanalysis[49]projectsaglobalneedfor$6.7trillionindatacenter
capitalexpendituresby2030,with$5.2trillionofthatdedicatedspecificallytoAI-ready
facilities. Thisfigureencompasseslandacquisition, construction, andtheprocurement
ofserversandnetworkinghardware[26]. Theupfrontcapitalrequiredtoequipasingle
frontiertrainingclusterisasignificantbarriertoentry;thehardwareacquisitioncostfor
thesystemusedtotrainGPT-4,forinstance,isestimatedat$800million[49].
Thisdatacenterbuildoutnecessitatesaparallelandequallymassiveinvestmentinthe
powergrid. Theprojectedloadgrowthfarexceedsthecapacityofexistinginfrastructurein
manyregions. Theresearchpresentedin[50]estimatesthatapproximately$720billionin
U.S.gridspendingwillberequiredthrough2030tosupportthisnewdemand,covering
newpowerplants,high-voltagetransmissionlines,andlocalsubstationupgrades.
https://doi.org/10.3390/en19010137

Energies2026,19,137 19of35
Acentraleconomicandpoliticalconflicthasemergedoverasimplequestion: who
paysforthesegridupgrades? Historically,thecostsofnewtransmissioninfrastructure
weresocialized,orspreadacrossallcustomerswithinautility’sservicearea. However,
thismodelisbeingchallengedbytheuniquenatureofdatacenterload,whereasingle
customercannecessitatebillionsofdollarsindedicatedupgrades.
A recent report [51] has identified a structural issue within the existing regulatory
frameworkofthePJMInterconnection,thelargestgridoperatorintheU.S.Theiranalysis
foundthatin2024alone,anestimated$4.4billionintransmissionupgradecosts,directly
attributabletonewdatacenterconnections,werepassedontoallresidentialandcommer-
cialcustomersinsevenstates. Inanotherresearchanalysis,forecastsofanationalaverage
increaseof8%by2030werepresented,duetoincreasingdatacenterpowerdemand[52].
Thissituationhastriggeredareal-timeregulatoryscrambleacrossthenation,asstates
independentlyattempttoreformtheapplicationofcostcausationprincipleswithincentury-
old utility frameworks. For instance, in Ohio, the Public Utilities Commission (PUCO)
ordered AEP Ohio to create a distinct tariff classification for data centers. This move,
supportedbytheOhioConsumers’Counsel,isdesignedtoensuredatacentersbearthe
fullcostofserviceandtoprotectothercustomersfromtherisksofstrandedassets,which
areunderusedinvestmentsmadespecificallyforthedatacenterindustry[53]. InOregon,
the legislature passed HB 3546, which mandates that data centers enter into long-term
contracts(10yearsormore)andthatthefullcosttoservetheirloadisallocateddirectlyto
them,explicitlypreventingthesocializationofthesecosts[54]. WhileinMichigan,atariff
case involving Consumers Energy is exploring similar protective measures, including
15-yearminimumcontractsandexitfees,tomitigatethefinancialrisktothepublicifadata
centerprojectiscanceledordecommissionedprematurely[55,56]. Thesestate-levelactions
represent a fundamental re-evaluation of utility ratemaking principles, setting critical
precedents for how the substantial cost of the AI energy transition will be distributed
betweencorporationsandthepublic.
3.6. TheEnvironmentalFootprint: ALife-CyclePerspectiveonAI’sResourceIntensity
AcomprehensiveevaluationoftheenvironmentalimpactofAIdatacentersrequiresa
perspectivethatextendsbeyondoperationalelectricityusetoincludetheembodiedcarbon
ofhardwareandtheconsumptionofwaterforcooling[7,57]. Whileefficiencygainsare
beingmade,thesheerscaleoftheindustry’sgrowth,withglobaldatacenterpowerdemand
forecasttomorethandoubleby2030,presentsaformidableenvironmentalchallenge[2].
To accurately assess energy use, a “full-stack” measurement approach is essential.
ThismethodologyaccountsfornotonlytheenergyconsumedbyactiveAIaccelerators
butalsothepowerdrawnbyhostsystems(CPUs,DRAM),theenergyusedbyidlema-
chinesprovisionedforreliability,andtheoverheadofthedatacenter’spowerandcooling
infrastructure,capturedbythePowerUsageEffectiveness(PUE)metric. Asdemonstrated
inadetailedanalysisbyGoogle,narrowerapproachesthatfocussolelyontheaccelerator
chipcansignificantlyunderestimatethetrueenergyfootprint,withtheircomprehensive
measurementbeing2.4timesgreaterthananarrower,existingapproach[7].
Applyingthiscomprehensivemethod,astudybyGooglefoundthatamediantext
prompt for its Gemini model consumes 0.24 Wh [7]. This figure is notably lower than
manypublicestimates,whichhaverangedfrom0.3WhforaChatGPT-4oquerytoashigh
as3.0Whforoldermodels,demonstratingthesignificantimpactofhardware-software
co-designandcontinuousoptimization[7]. Theenergyconsumedduringmodeltrainingis
ordersofmagnitudegreaterduetotheimmensecomputationalrequirementsoftraining
jobsthatcanspantensofthousandsofGPUs[3,57]. Forinstance,theamortizedhardware
andenergycostfortrainingafrontiermodellikeGPT-4isestimatedat$40million. While
https://doi.org/10.3390/en19010137

Energies2026,19,137 20of35
energyrepresentsarelativelysmallfractionofthistotaltrainingcost(2–6%),theabsolute
expenditureforasinglefrontiermodelstillamountstomillionsofdollars[3].
ThecarbonfootprintofanAIdatacenteriscomposedoftwoprimarycomponents:
operational emissions from electricity consumption and embodied emissions from the
manufacturinganddeploymentofitsphysicalinfrastructure.
Operationalemissionsarethegreenhousegasesreleasedfromthepowerplantsthat
generatetheelectricityconsumedbythedatacenter. Thisfootprintishighlydependenton
thecarbonintensityofthelocalgrid. Majortechnologycompaniesareamongthelargest
corporatepurchasersofrenewableenergy,oftenusingPowerPurchaseAgreements(PPAs)
andmarket-basedaccountingmechanismstoreducetheirreportedcarbonfootprint[58].
However,the24/7operationalrequirementofdatacentersmeansthattheyinevitablydraw
powerfromfossilfuel-basedgenerationwhenrenewablesourceslikewindandsolarare
notavailable[59].
Embodiedemissionsrepresentthecarbonassociatedwiththeentiresupplychainof
a data center’s physical assets, including emissions from raw material extraction, man-
ufacturing, transportation, and end-of-life disposal of hardware [57]. This category is
distinctfromoperationalcarbon,whicharisesfromenergyconsumptionduringuse.ForAI
inference systems, while GPUs are the primary source of operational carbon, the host
systems—including CPUs, memory, and storage—dominate the embodied carbon, ac-
countingforaround75%ofthetotal[57]. Thequantificationoftheseemissionsrelieson
methodologiessuchasLifeCycleAssessments(LCAs)anddatafromproductenviron-
mentalreports[57,60]. Recognizingtheimportanceofthisimpact,leadingresearchnow
incorporatesembodiedemissionsintoaholisticcarbonfootprintmetric,accountingfor
boththeoperationalandembodiedimpactsperuserprompt[7].
AIdatacentersconsumewaterprimarilyforcoolingthehigh-densityserverracks
andassociatedinfrastructurerequiredtomanagetheheatgeneratedbyITequipment[7].
TheefficiencyofthiswateruseisbenchmarkedusingtheWaterUsageEffectiveness(WUE)
metric,whichmeasuresthelitersofwaterconsumedperkilowatt-hourofITenergy. While
efficiencyvaries,GooglereportsafleetwideaverageWUEof1.15L/kWh. Basedondirect
instrumentationofitsproductionenvironment,amedianGeminiAppstextpromptwas
foundtoconsume0.26mLofwater[7]. Tomitigatetheimpactonlocalwatersupplies,
particularlyinhigh-stresslocations, strategiesincludedeployingair-cooledtechnology
duringnormaloperations[7].
Toconclude,thispartofthesurveysystematicallydetailsthetechnical,operational,
andfinancialchallengesofAIdatacentergridintegration. Weanalyzethefullspectrumof
issues,fromlong-termplanningmismatchesandreal-timebalancingstrainstosub-second
stabilityrisksandpowerqualitydegradation. Theanalysisalsoextendstothesignificant
economicandlife-cycleenvironmentalimpacts. Ahigh-leveloverviewofthesecritical
challengesandtheirkeyfindingsispresentedinTable5.
Table5.Summaryofsurveyedgridintegrationchallenges.
SurveyDomain SpecificChallenge SummaryofFindingsfromLiterature KeyRefs.
AItrainingloadsareadistinctcategory,
characterizedbyhighpowerdensity,sustained
LoadCharacterization AIWorkloadProfiles [4,5]
highutilization,andrapidpowerfluctuations
(ramprates)thatdifferfromtraditionalITloads.
Afundamentaltemporalmismatchexists.
Datacenterdeployment(1–2years)issignificantly
Long-TermPlanning Resource&TransmissionAdequacy fasterthangridinfrastructureplanningand [25,26]
construction(5–10years),
strainingresourceadequacy.
https://doi.org/10.3390/en19010137

Energies2026,19,137 21of35
Table5.Cont.
SurveyDomain SpecificChallenge SummaryofFindingsfromLiterature KeyRefs.
Rapidandlarge-scaleloadramps(e.g.,400MWin
36s)arefasterthanconventionalgeneration
Real-TimeOperations Balancing&VoltageControl [25,39,40]
reserves,strainingbalancingservicesandcausing
localvoltagedeviations.
Protectivesettingsondatacenterscantriggera
simultaneousdisconnectionoflargeloads
PowerSystemStability CoordinatedLoadTripping [25,43]
(e.g.,1.5GWeventin2024)duringagridfault,
causingsystem-wideover-frequencyevents.
PowerelectronicconvertersinUPSandserver
PSUsintroduceharmonicdistortion.These
PowerSystemStability Harmonics&Resonance [25,45,46]
harmonicscaninteractwithgridimpedance
anddatacentercapacitors,creatingresonance.
Substantialgridupgradecostsraiseapolicy
debateovercostallocation,witharegulatory
Economic&Policy CostAllocation [51,53,61]
trendmovingawayfromsocializingcosts
andtowards“causationpays”models.
On-siteBatteryEnergyStorage(BESS),
hardware-levelpowersmoothing,
MitigationStrategies Load-Side&CollaborativeSolutions andcollaborativeloadcurtailmentprogramsare [5,26,42,62]
identifiedaskeystrategiestomanagevolatility
andsupportthegrid.
4. MitigationStrategiesandSolutions
The formidable technical, economic, and environmental challenges detailed in the
previoussectionnecessitateamulti-facetedapproachtomitigation. Asustainableintegra-
tionofAIdatacenterscannotbeachievedthroughisolatedefforts,butratheritrequiresa
concertedstrategyinvolvinginnovationwithinthedatacenter,collaborativeframeworks
betweenutilitiesandoperators,andproactivegrid-sideenhancementscoupledwithsup-
portivepolicy. Thissectionsurveysthelandscapeofpotentialsolutions,categorizingthem
intothreeprimarydomains: advancementsonthedatacenterside,collaborativemodels
forloadmanagement,andbroadergrid-levelandpolicy-driveninterventions.
4.1. DataCenter-SideSolutions
Mitigation strategies implemented within the data center itself offer direct control
overtheload’sinteractionwiththepowergrid. Thesesolutions,summarizedinFigure14,
rangefromaddingsupplementaryhardwaretorefiningoperationalsoftwareandhardware
designprinciples.
Aprimarystrategyinvolvesthedeploymentofon-siteBESS.Thesecaneffectively
addressseveralchallengesposedbyAIdatacenters. Byabsorbingandreleasingenergy,
BESScansmooththerapidpowerfluctuationsinherentinAItrainingworkloads,presenting
amorestableloadprofiletotheutilitygrid[5,26]. Thissmoothingcapabilityhelpsmitigate
issuesrelatedtovoltageflickerandfrequencydeviations. Furthermore,BESScanprovide
LowVoltageRide-Throughsupport. Duringgridvoltagesagsthatmightotherwisecause
datacenterUPSsystemstodisconnectITload,strategicallycontrolledBESScaninjectpower
orrapidlyincreasechargingtomimicthedisconnectedloadfromthegrid’sperspective,
therebypreventinglarge,abruptloaddropsseenbytheutility. BESSalsofacilitatesbackup
powerduringoutagesandcanenableloadshaping,allowingdatacenterstomanagetheir
consumptionpatternstoalignwithgridconstraintsorparticipateinflexibleinterconnection
programs. Whileeffective, implementingBESSincursadditionalcapitalcosts, requires
https://doi.org/10.3390/en19010137

Energies2026,19,137 22of35
physicalspace, andnecessitatescarefulconsiderationofbatterycapacityandchargeor
dischargeratestomeetthespecificneedsofAIworkloads.
Complementaryoralternativeapproachesfocusonactivelymanagingthepowercon-
sumptionprofileofthecomputationalhardwareitself. Software-basedpowersmoothing
techniques involve monitoring GPU power draw or activity in real-time and dynami-
callyinjectingsecondarycomputationalworkloads(eitherartificialorlow-prioritytasks)
whentheprimaryworkload’spowerconsumptiondrops,suchasduringcommunication
phases[5]. Thismethodaimstomaintainahigher, moreconsistentpowerfloor, reduc-
ingthemagnitudeofpowerswings. However,challengesincludepotentialperformance
overheadfortheprimaryworkload, theneedforfine-grained, low-latencymonitoring,
ensuringreliabilityatscale,andtheenergypotentiallywastedonartificialworkloads[5].
Asanalternativeintegratedsolution,GPUhardwarevendorsareintroducingpower
smoothing features directly into firmware. These features allow operators to program
specificpowerramp-upandramp-downrates,establishaminimumpowerfloorduring
operation, and define a stop delay before ramping down after workload inactivity [5].
Thishardware-levelcontroloffersamorereliableandpotentiallylower-overheadmethod
comparedtopurelysoftware-basedapproaches,directlyaddressingutilityspecifications
inthetimedomain. Nonetheless,similartosoftwaresmoothing,maintaininganelevated
powerfloorinevitablyleadstoincreasedenergyconsumptioncomparedtoallowingthe
hardwaretooperateatlowerpowerlevelsduringidleorcommunicationperiods. Ahybrid
approach combining BESS with GPU-level smoothing may offer an optimized balance,
using smoothing to handle ramps and BESS to manage fluctuations without excessive
energywaste[5].
Furtheradvancementsinpowerelectronicsofferadditionalsolutions. Theadoptionof
grid-forminginverters,potentiallyintegratedwithon-siteresourceslikeBESS,represents
a more sophisticated approach. Grid-forming inverters can actively contribute to grid
stabilitybyprovidingvoltageandfrequencysupport,mimickingthebehavioroftraditional
synchronousgenerators[26,63]. Deployingsuchtechnologieswithindatacenterscould
transformthemfrompassiveloadsintoactivegrid-supportiveassets.
Beyonddirectpowermanagement,aholisticviewencompassingtheentirelifecycle
and resource utilization offers further mitigation pathways through environmentally-
consciousdesignprinciples. Suchstrategiesincludereusingtypicallyunderutilizedhost
CPUresourceswithinAIserversforlesstime-sensitivetasks,therebyincreasingoverall
computecapacitywithoutaddinghardware. Anotherapproachinvolvesrightsizingby
provisioning a heterogeneous mix of GPUs and tailoring their allocation based on the
specific compute, memory, and energy characteristics of different AI workload phases
andservicelevelobjectives. Additionally, reducingtheenvironmentalimpactinvolves
optimizing host system configurations by minimizing overprovisioned resources like
DRAM and SSD storage, which contribute significantly to embodied carbon. Finally,
recyclingprinciplescanbeappliedthroughasymmetrichardwarerefreshcycles,extending
thelifetimeofhostsystems(whichhaveslowerefficiencygainsandhighembodiedcarbon)
whilepotentiallyupgradingacceleratorsmorefrequentlytocaptureoperationalenergy
efficiencyimprovements. Thesedesignphilosophiesaimtominimizebothoperationaland
embodiedenvironmentalimpacts[57].
Additional data center-centric strategies focus on optimizing energy sourcing and
utilizationwithinthefacilityitself. Integratingon-siterenewableenergygeneration,such
as rooftop solar panels, allows data centers to directly consume clean energy, reducing
relianceongridpower,particularlyduringpeakgenerationtimes. Intelligentworkload
scheduling can further enhance this synergy by temporally shifting deferrable compu-
tationaltasks, likeAImodeltrainingorbatchprocessing, toalignwithperiodsofhigh
https://doi.org/10.3390/en19010137

Energies2026,19,137
23of35
on-siterenewablegenerationorlowgridcarbonintensity. Spatiallyshiftingworkloads
betweengeographicallydistributeddatacentersbasedonreal-timegridcarbonintensityor
renewableavailabilityrepresentsanotheravenueforoptimization. Furthermore,exploring
thepotentialforwasteheatrecoveryandutilization,forexample,fordistrictheatingor
other industrial processes, can improve the overall energy efficiency and sustainability
profileofthedatacenteroperation[64].
Finally,continuousimprovementsintheinternalenergyefficiencyofthedatacenter
remaincrucial. Thisincludesoptimizingcoolingsystems,whichcanaccountforasubstan-
tialportionoftotalenergyuse,throughtechniqueslikeadvancedthermalmanagement,
automation,andadjustmentsbasedonworkloadintensity. Enhancingserverutilization
andemployingpowermanagementtechniquessuchasDynamicVoltageandFrequency
ScalingforbothCPUsandGPUscanalsocontributetoreducingtheoverallenergydemand
and associated grid impact [65]. The internal strategies explored in this subsection are
summarizedinFigure14.
DataCenter-SideSolutions
|     |     | Software-Based |     | Hardware-Based |     | ImproveInternal |
| --- | --- | -------------- | --- | -------------- | --- | --------------- |
BESS
|     |     | PowerSmoothing |     | PowerSmoothing |     | EnergyEfficiency |
| --- | --- | -------------- | --- | -------------- | --- | ---------------- |
• Smoothrapidpower • Usereal-time • Programpowerramp • Optimize
thermal
|     | fluctuations       | monitoringfor        |                  | rates                 |                    |                 |
| --- | ------------------ | -------------------- | ---------------- | --------------------- | ------------------ | --------------- |
|     |                    | workloadinjection    |                  |                       |                    | management      |
| •   | ProvideLVRTsupport |                      |                  | • ConfigureGPU        |                    |                 |
|     |                    |                      |                  | firmwarepowerfloor    |                    | • Enhanceserver |
| •   | Backuppower&load   | • Maintainconsistent |                  |                       |                    |                 |
|     |                    | powerduring          |                  |                       |                    | utilization     |
|     | shaping            |                      |                  | • Providemorereliable |                    |                 |
|     |                    | communication        |                  | control               |                    | • UseDV&FS      |
|     | Grid-Forming       |                      | Environmentally- |                       | EnergySourcing&    |                 |
|     | Inverters          |                      | ConsciousDesign  |                       | WorkloadScheduling |                 |
• IntegratewithBESS • ReuseunderutilizedCPU • Integrateon-siterenewable
| •   | Activelysupportgridvoltage |     | resources            |     | energy             |     |
| --- | -------------------------- | --- | -------------------- | --- | ------------------ | --- |
|     | andfrequency               |     | • RightsizeGPUmixfor |     | • Temporalshifting |     |
workloadneeds
| •   | Functionliketraditional |     |     |     | • Spatialshifting |     |
| --- | ----------------------- | --- | --- | --- | ----------------- | --- |
• Minimizeoverprovisioning
|     | generators |     |     |     | • Utilizewasteheat |     |
| --- | ---------- | --- | --- | --- | ------------------ | --- |
• Useasymmetricrefreshcycles
Figure14.Datacenter-sidesolutionsforAIworkloadpowermanagementandsustainability.
4.2. CollaborativeSolutions
Whenitcomestopowerconsumption,AIworkloadsaremoreflexiblethanmostother
datacentertasks.Operatorscanpauseandresume,ormovethetrainingandinferenceofAI
models,whichallowsthemtoparticipateincurtailmentprograms. Theseprogramsenable
datacenterstooperateatfullcapacityformostoftheyear,thenreducetheirpowerusage
for short periods when the electrical grid is under stress, such as during peak summer
demand events. This flexibility is a significant advantage because the grid is built to
handlepeakdemand,notaveragedemand. Asaresult,asubstantialamountofpower
generationandtransmissioncapacitysitsidleformostoftheyear. Byparticipatinginthese
programs,techcompaniescanaccesslargeamountsofavailablepowerwithoutbuilding
newinfrastructure.
Foryears,thedesignofdatacentersfocusedonmaximizinguptime—thepercentage
oftimeafacilityisfullyoperational. Thisfocusonreliabilityhasbeenthebedrockofthe
industry, asitallowsproviderstoguaranteeconsistentserviceandchargehigherrates.
Based on their uptime, data centers are categorized into tiers based on their reliability,
https://doi.org/10.3390/en19010137

Energies2026,19,137 24of35
withhighertiersbeingmoreexpensivetobuildandoperate. Forexample,acommonTier
3datacenteroffers99.982%uptime,whichtranslatestoabout1.6hofdowntimeperyear.
TheemphasisoncontinuousuptimeisbestexemplifiedbyTier4datacenters. These
facilities boast an impressive 99.995% uptime, with only 26 min of downtime annually.
However,achievingthislast0.013%ofperformancecostsnearlytwiceasmuch. Eventhe
lowest-gradeTier1datacentersarebuilttomaintainarobust99.671%annualuptime. This
relentlesspursuitofreliabilityshowsthatcustomershavealwaysdemanded—andpaida
premiumfor—uninterruptedservice[66,67].
Unliketraditionalcloudcomputing,thenewpriorityforAIcompaniesisspeedto
marketandscale, notultra-highuptime. Thisfocusonspeedcreatesastrongflywheel
effect: thefasteracompanycansecurepower,thefasteritcanbuildinfrastructure,train
anddeploynewAImodels,andgatherthedataneededtodevelopthenextgeneration
ofAI.
Thisvirtuouscyclemakesspeedamajorcompetitiveadvantagethatfocusesnoton
reliabilitybutratheronscaleandspeedofdeployment. Infact,manycurrentAIservices
are already running at uptime levels similar to the lowest-tier traditional data centers,
whichshowstheshiftintheindustry’spriorities[68,69].
Asmentioned,TheflexibilityofAIcomesfromtwomainprocesses,thefirstbeingthe
trainingprocess. Thisprocesscanbepausedandresumedusingcheckpoints,meaning
trainingcanstopduringapowershortageandeitherrestartlaterorberedirectedtoanother
datacenter.
Theotheroneistheinferencestage. Unliketraditionalwebsites,whichrequirenear-
instant loading times, AI responses can take several seconds to generate. This makes
network latency, even across continents, irrelevant. As a result, companies can move
inferencetaskstodatacenterswithcheaperormoreavailablepowerwithoutaffectingthe
userexperience.
Thisisasignificantshiftfromthemillisecondresponsetimeoftheearlyinternet. Tra-
ditionalwebapplicationstaughtustoexpectinstantresponses,asevenatenthofasecond
delaycouldimpactsales. AIchangesthisentirely. AChatGPTresponse,forexample,can
take20stogenerate. Adelay,evenofhundredsofmilliseconds,iscompletelyunnoticeable
whenconsideringAIinference,comparedwithtraditionalwebapplications. Thistolerance
isevenmorepronouncedwithagenticAI,whichperformscomplex,multi-steptasksthat
can run for tens of minutes. The rise of these agents is shifting user expectations from
constant,real-timeattentiontoadifferent,morelatency-tolerantmodel.
Astudypresentedin[62]quantifiesthispotential,findingthatcurtailmentcouldadd
76GWofnewloadcapacitywithjusta0.25%reductioninuptime. Thiscouldbeashigh
as 126 GW with a 1% reduction, effectively adding 10% to the nation’s power capacity
withoutanynewconstruction. Thesecurtailmenteventsaretypicallyshort—around1.7to
2.5h—andstillmaintainatleast50%ofnormalcapacity. Ultimately,thisapproachmeans
AIcompanieswillnothavetowaitfornewenergyinfrastructuretocomeonlinetomeet
everynewdemand. Thisabilitytousecurtailmentoffersasignificantadvantageinaworld
wherebacklogsforgridinterconnectionhavesurgedtooveradecade. Buildingnewpower
plantstopowerdatacentersisnolongeraquickfix,asmajorturbinemanufacturershave
backlogsstretchingto2029orbeyond. Curtailmentoffersafarfasterpathtoaccesspower.
Thefinancialupsideisequallycompelling. TheDukeUniversitystudy,whichpro-
jectedthepotentialtounlock100GWofcapacity, suggeststhatthisrepresentsroughly
$150billioninusablepowerinfrastructurethatiscurrentlysittingidle. Thismeansthat
withcurtailmentprograms,AIcompaniesdonotneedtowaitfornewenergyprojectstobe
built. Fromawiderperspective,theUSpowergridcurrentlyoperatesatabout53%ofits
capacity,withbillionsinassetssittingidle. ByusingflexibleAIworkloadstoincreasegrid
https://doi.org/10.3390/en19010137

Energies2026,19,137 25of35
utilization,utilitiescanspreadtheirfixedcostsoveralargerload. Thisreducesper-unit
costsforallratepayersandincreasesrevenueforinvestorswithoutaddingstrainduring
peaktimes. Ultimately,curtailmentpresentsanewvisionforAI’srelationshipwiththe
grid: insteadofbeingasourceofcrisis,AIbecomesashockabsorberthathelpsthesystem
runmoreefficiently[42]. Thesecollaborativestrategiesdiscussedinthissubsectionare
summarizedinFigure15.
CollaborativeSolutions
ParticipateinCurtailmentPrograms LeverageTemporalFlexibility(Pausing)
• PauseAItrainingworkloads
• Temporarilyreducepowerconsumption
usingcheckpoints
• Lose0.25%–1%oftotaluptime
• Resumelaterwhengridcapacityavailable
• Supportgridduringpeakstressperiods
• Minimizeimpactonoperations
LeverageSpatialFlexibility(Moving) ActasaGrid“ShockAbsorber”
• ShiftAIinferencetasksgeographically • Utilizegrid’sexistingslackcapacity
• Movetoregionswithavailable,cheaper, • Unlock76–126GWwithoutnewpowerplants
orcleanerpower • Save$150Bininfrastructurecosts
• Leveragetolerancetonetworklatency • Reducebillsforallratepayers
Figure15.Collaborativesolutionsbetweendatacentersandgridoperatorsforpowermanagement.
4.3. Grid-SideandPolicySolutions
AddressingthegridintegrationchallengesofAIdatacentersnecessitatessolutions
thatextendbeyondthefacilityboundary,involvinggridoperators,utilities,policymak-
ers,andregulators. Thesesolutionsfocusonimprovinggridinfrastructure,operational
practices,marketmechanisms,andregulatoryframeworks.
Enhanced coordination and data sharing between data center operators and grid
entitiesarefundamental. Gridplannersandoperatorsrequiretimelyandaccurateinforma-
tionregardingprojectedloadgrowth,expectedoperationalprofiles(includingpotential
rampratesandvariability),andthevoltageorfrequencyride-throughcapabilitiesofdata
centerequipment. Lackofvisibilityintothesecharacteristicshindersaccurateforecasting,
operationalplanning,andstabilityanalysis[25]. Establishingstandardizeddatareporting
requirementsandsecurecommunicationchannelscanimprovesituationalawarenessand
enablemoreeffectivegridmanagement.
Thesignificanttemporalmismatchbetweenrapiddatacenterdeploymentandlengthy
gridinfrastructuredevelopmentnecessitatesreformsinpermittingandinterconnection
processes[25,26]. Currentproceduresoftencreatebottlenecks,delayingtheconnectionof
newloadsandpotentiallyexacerbatinggridconstraints[26]. Streamliningsiting,permit-
ting,andgridinterconnectionstudies,whileensuringnecessaryreliabilityassessmentsare
performed,iscrucial. Thiscouldinvolveexpeditedreviewsforprojectsmeetingcertain
criteria,bettercoordinationbetweeninvolvedagencies,andincorporatingmoreflexible
interconnectionoptions.
Policyandregulatoryleversplayanimportantroleinguidingsustainableintegration.
Akeyareaismodernizingratedesignandcostallocationprinciples.Thetraditionalpractice
https://doi.org/10.3390/en19010137

Energies2026,19,137 26of35
ofsocializingthecostsofgridupgradesacrossallratepayersisincreasinglycontentious
when substantial investments are driven by a single large load, potentially leading to
significantincreasesinelectricitybillsforresidentialandcommercialcustomers[25,61].
Transitioning towards “causation pays” models, where the entity directly causing the
needforupgradesbearsalarger,proportionateshareofthecosts,isgainingtractionin
severaljurisdictions[61]. Designingappropriatetariffscanalsoincentivizegrid-friendly
behavior. For instance, dynamic pricing mechanisms, such as time-of-use (TOU) rates
orreal-timepricingexposure, canencouragedatacenterstoshiftflexibleworkloadsto
off-peak hours or periods of high renewable generation. Interruptible service tariffs,
potentiallycombinedwithflexibleconnectionagreements,offerreducedelectricityrates
in exchange for the data center agreeing to curtail load during grid stress events [26].
Inaddition,financialincentives,suchastaxcreditsorgrantsforinvestinginon-siteBESS
or energy efficiency measures, can further steer data center development. Establishing
environmentalstandards,potentiallythroughcarbonpricingmechanisms,emissionslimits,
orcertificationsforgreendatacenters,canpromotetheadoptionofcleanerenergysources
andmoreefficientoperations[64].
Decentralizingpowersupplythroughon-sitegenerationandmicrogridsoffersanother
pathway,asillustratedinFigure16. Integratingsignificantrenewableresourcesdirectlyat
thedatacentersitereducesdependenceonthemaingrid[64]. Thepotentialuseofsmall
modularreactors(SMRs)isalsobeingexploredbysomedevelopersfordedicated,reliable,
carbon-freepower[70]. Microgrids,combininglocalgeneration(renewables,potentially
backupgenerators)andenergystorage,canallowdatacenterstooperateindependently
duringgridoutages,enhancingresilienceandpotentiallyprovidinggridsupportservices
wheninterconnected.
Figure16.Illustrationofthedatacenter’sintegratedecosystem,interactingwiththeelectricalgrid,
localpowerplants,andrenewableenergysources.Thedatacenteralsoreliesonancillarysystems,
suchasenergystoragedevices,andimplicitlyinteractswithotherloadunits.
Maximizing the efficiency of the existing transmission network through Grid-
EnhancingTechnologies(GETs)canhelpaccommodatenewloadsmorequicklyandcost-
effectively. DynamicLineRatingsallowtransmissionlinestooperateclosertotheirtrue
thermallimitsbasedonreal-timeweatherconditions,oftenunlockingsignificantlatent
capacitycomparedtoconservativestaticratings. Advancedpowerflowcontroldevices
canactivelymanagepowerflowsacrosstransmissionlines,redirectingpowerfromcon-
gestedlinestounderutilizedones,therebyincreasingoverallgridtransfercapability[71].
Topologyoptimizationinvolvesstrategicallyreconfiguringthegridnetworkbyopeningor
closingcircuitbreakerstooptimizepowerflowsandalleviatecongestion[71]. Deploying
GETs can often defer or avoid the need for expensive and time-consuming traditional
transmissionupgrades.
Finally,integratingthesesolutionsrequiresashifttowardsmoreproactivegridplan-
ning and potential market reforms. Planning processes need to better account for the
uncertaintyandspeedassociatedwithlargeloadgrowth,potentiallyemployingscenario-
basedanalysisandadaptiveplanningframeworks[25]. Crucially,effectivelyanalyzingthe
https://doi.org/10.3390/en19010137

Energies2026,19,137
27of35
gridimpactofthesefacilitiesrequiresevolvinghowtheyarerepresentedinpowersystem
models. AIdatacentersrepresentahistoricallydistinctcategoryofload,characterizedby
highconcentrationsofpowerelectronicinterfaces,highlycorrelatedinternaloperations
thatdiminishstatisticalsmoothingeffects,andthepotentialforextremelyrapidpower
fluctuations[25,72]. Thesecharacteristicschallengetheassumptionsunderlyingtraditional
load models, which often represent aggregate demand as relatively slow-varying and
predictablebasedontheLawofLargeNumbers. Consequently,standardanalyticalmodels
mayfailtocapturethefasttransientbehaviorsandpotentialinstabilitiesintroducedby
theselargecomputationalloads.Solutionsinvolvedevelopingandvalidatingnewdynamic
load models. For instance, limitations have been identified in the standard Composite
LoadModel(CMLD)parameterstoaccuratelyrepresentdatacenterdisconnectionbehav-
ior,particularlyregardingdelayedtrippingorrampedreconnectionlogic[26]. Emerging
approachesadaptmodelsoriginallydevelopedforotherpowerelectronicloads,suchas
ElectricVehicle(EV)chargers,whichoffermoregranularparameterstorepresentvoltage
orfrequencyride-throughcharacteristics,tripdelays,andcontrolledreconnectionramps,
providingapotentialpathwayformoreaccuratestabilityassessments[26]. Adoptingand
standardizingsuchadvancedmodelsisessentialforreliablegridplanningandoperationin
aneraincreasinglyshapedbylarge,dynamiccomputationalloads. Theproposedsolutions
inthissubsectionareoutlinedinFigure17.
Grid-SideandPolicySolutions
| Coordination& |     | ReformPermitting |     |     | RateDesign |     |     | Policy& |
| ------------- | --- | ---------------- | --- | --- | ---------- | --- | --- | ------- |
DataSharing &Interconnection &CostAllocation FinancialIncentives
• Establishsecure • Streamlinesiting • Implement“causation • TaxcreditsforBESS
| communication |     | processes |     |     | pays”models |     |     | andefficiency |
| ------------- | --- | --------- | --- | --- | ----------- | --- | --- | ------------- |
channels
|                   |     | • Expeditegrid  |     |     | • Usedynamicpricing  |     | •   | Carbonpricing |
| ----------------- | --- | --------------- | --- | --- | -------------------- | --- | --- | ------------- |
| • Shareloadgrowth |     | interconnection |     |     |                      |     |     | mechanisms    |
|                   |     |                 |     |     | • Offerinterruptible |     |     |               |
projections • Reducedeployment servicetariffs • Greendatacenter
| • Standardizedata |     | bottlenecks |     |     |     |     |     | certifications |
| ----------------- | --- | ----------- | --- | --- | --- | --- | --- | -------------- |
reporting
|     | Decentralize |     |     | Grid-Enhancing |     |     | GridPlanning |     |
| --- | ------------ | --- | --- | -------------- | --- | --- | ------------ | --- |
|     | PowerSupply  |     |     | Technologies   |     |     | &Modeling    |     |
• Integrateon-siterenewables • DynamicLineRatings • Proactivescenario-based
| •   | DeploySmallModular   |     | •   | AdvancedPowerFlow    |     |     | planning            |     |
| --- | -------------------- | --- | --- | -------------------- | --- | --- | ------------------- | --- |
|     | Reactors             |     |     | Control              |     | •   | Developdynamicload  |     |
| •   | Developmicrogridsfor |     | •   | TopologyOptimization |     |     | models              |     |
|     | resilience           |     |     |                      |     | •   | CaptureAIdatacenter |     |
behavior
Figure17.Grid-sideandpolicysolutionsforintegratingAIdatacenterswithpowergrids.
Insummary,thissectionexploresathree-prongedapproachtomitigation,spanning
datacenterinternalhardwareandsoftware,collaborativeloadflexibilitymodels,andsys-
temic grid and policy reforms. A high-level overview of these interconnected solution
categoriesisprovidedinTable6.
https://doi.org/10.3390/en19010137

Energies2026,19,137 28of35
Table6.Summaryofmitigationstrategiesandsolutions.
StrategyCategory SpecificSolution Mechanism/Description KeyRefs.
On-sitebatteriesabsorbandreleaseenergytosmoothrapidpower
DataCenter-Side BatteryEnergyStorage [5,26]
fluctuationsandprovideride-throughsupportduringgridsags.
Softwareinjectssecondarytasksorhardwarefirmwarecontrolsramprates
DataCenter-Side PowerSmoothing(HW/SW) [5]
toestablishamoreconsistentpowerfloor,reducingvolatility.
Advancedpowerelectronicsthatcanactivelyprovidevoltageand
DataCenter-Side Grid-FormingInverters [26,63]
frequencysupporttothegrid,mimickingsynchronousgenerators.
LeveragestheflexibilityofAItraining,whichcanbepausedandresumed,
Collaborative LoadCurtailmentPrograms [42,68]
toreducedemandduringperiodsofgridstress.
Moveslatency-tolerantworkloads(e.g.,inference)betweengeographically
Collaborative GeographicalLoadShifting [N/A]
distributeddatacenterstoutilizeavailablepower.
Regulatoryshifttowards“causationpays”models,requiringdatacentersto
Grid-Side&Policy CostAllocationReform [25,51,53,61]
bearthecostsofthegridupgradestheynecessitate.
DeployingDynamicLineRatings(DLR)andpowerflowcontrollersto
Grid-Side&Policy Grid-EnhancingTech.(GETs) [71]
maximizethecapacityofexistingtransmissioninfrastructure.
Developingandstandardizingnewdynamicmodelsthataccuratelycapture
Grid-Side&Policy AdvancedLoadModeling [25,26,72]
thefasttransientbehaviorofpower-electronic-basedloads.
5. FutureWork
Lookingahead,focusedresearcheffortscancontributetoaddressingthegridintegra-
tionchallengesofAIdatacenters. Keyareasofferingpromisingavenuesforinvestigation
includeadvancingloadmodelingtechniques,assessingmitigationstrategiesthroughsim-
ulation,anddevelopingframeworksformarketandpolicyanalysis,asdiscussedinthe
followingsubsections.
5.1. AdvancingLoadModelingandSimulationFrameworks
Amajorstepisthedevelopment,validation,andstandardizationofaccuratedynamic
modelsspecificallyforAIdatacenters.Currentmodels,suchasthestandardCMLD,often
failtocapturethenuancedbehavior,particularlythefasttransientsandspecificride-through
logic,exhibitedbythesepower-electronic-intensiveloads[26].Futureresearchcanfocuson
comparativestudiesevaluatingthefidelityofexistingmodelsagainstreal-worldmeasurement
data(whereavailable)ordetailedcomponent-levelsimulations.Apracticalavenueinvolves
adaptingandrefiningmodelsinitiallydevelopedforotherpowerelectronicloads,suchas
EVchargers,whichincludeparametersfortripdelaysandrampedreconnections,tobetter
representAIdatacenterresponses[25,26].Furthermore,researchcomparingthetrade-offs
betweendetailedcomponent-levelmodels(representingUPS,PDUs,PSUsindividually)and
computationally efficient aggregated models under various grid conditions (for instance,
weakandstronggrid,anddifferentfaulttypes)wouldprovidevaluableguidanceforindustry
practitioners. Developingopen-sourcebenchmarkmodelsandvalidationdatasetswould
significantlyaccelerateprogressinthisarea.Investigatingcomplexelectromagnetictransient
(EMT)interactions,suchassub-synchronousresonanceandharmonicpropagation,through
detailedEMTsimulationsisanotherimportantresearchdirection[5].
5.2. Simulation-BasedAssessmentofMitigationStrategies
Quantitativeassessmentofvariousmitigationstrategiescanbeeffectivelyconducted
usingpowersystemsimulationtools,offeringvaluableinsightswithoutrequiringlarge-
scalehardwaredeployment.Futureresearchcanfocusonparametricstudiestooptimizethe
sizing,placement,andcontrolalgorithmsforon-siteBESSspecificallytailoredtosmooth
AI workload fluctuations and enhance ride-through performance under different grid
scenarios. Comparativeanalysesevaluatingthegrid-wideimpact,costs,andbenefitsof
deployingGETssuchasDynamicLineRatingsoradvancedpowerflowcontrollersversus
https://doi.org/10.3390/en19010137

Energies2026,19,137 29of35
conventionaltransmissionupgradestoaccommodatedatacenterclustersrepresentanother
importantarea. Furthermore,simulationcanbeusedtorigorouslyevaluatetheenergy
consumptionimplicationsandgridstabilityeffectsofdifferentsoftwareandhardware-
basedpowersmoothingtechniques,quantifyingthetrade-offsbetweenmitigatingpower
swingsandincreasingoperationalenergyuse. Thesesimulation-basedstudiescanprovide
essential data to inform investment decisions and operational guidelines for both data
centeroperatorsandutilities.
5.3. DevelopingFrameworksforMarketIntegrationandPolicyAnalysis
Researchisneededtoexploreanddevelopframeworksthatfacilitatetheintegration
ofAIdatacentersintoelectricitymarketsandinformeffectivepolicydesign. Thisincludes
creatingsimulationplatformstotestinnovativemarketmechanismsandtariffstructures
(forexample,dynamicpricing,interruptiblerates,ancillaryserviceproducts)designedto
incentivizeandeffectivelyharnessthepotentialloadflexibilityofAIdatacenters.Economic
modelingstudiescanquantifythegrid-widebenefitsofutilizingthisflexibilityandcompare
different approaches for compensating data centers for providing grid services. Policy
analysisresearchcanfocusondevelopingandevaluatingframeworksforequitablecost
allocationofgridupgrades,balancingthe“causationpays”principlewithbroadersystem
benefits. Furthermore, future research can contribute by developing methodologies to
analyzethepotentialcontributionofdatacenters,especiallythosewithon-siteresources
likeBESSormicrogrids,tooverallgridresilience,includingtheirpotentialrolesduring
systemrestorationevents. Suchanalyticalandsimulation-basedframeworkscanprovide
valuable,evidence-basedinsightsforregulatorsandpolicymakersnavigatingthecomplex
economic and regulatory landscape surrounding AI data center integration. Refining
lifecycleassessmentmethodologiestobetterquantifytheembodiedenvironmentalimpacts
ofAIhardwarealsoremainsanimportant,data-drivenresearchtask.
Inconclusion,thissectionoutlineskeyresearchdirections,fromfoundationalload
modelingandsimulation-basedassessmentstothedevelopmentofnewmarketandpolicy
frameworks, as summarized in Table 7. Addressing these research questions through
rigorousanalysisandsimulation,leveragingcollaborationbetweenindustry,academia,
andpolicymakers,willbecrucialforensuringthatthepowergridcanreliably,affordably,
andsustainablysupporttheongoingAIadvancements.
Table7.Summaryoffutureworkandresearchdirections.
ProposedResearch
ResearchArea IdentifiedGap/Objective KeyRefs.
Action/Methodology
Currentmodels(e.g.,CMLD)donot Develop,validate,andstandardize
accuratelycapturethefasttransient newdynamicmodels.Adaptmodels
LoadModeling&Simulation [26]
behaviorandride-throughlogicofAI fromotherpowerelectronicloads
datacenters. (e.g.,EVchargers).
Usepowersystemsimulation
Needforquantitativeassessmentof
(e.g.,parametricstudies)tooptimize
MitigationStrategyAssessment mitigationstrategiesbeforecostly, [N/A]
BESSsizing,control,andtocompare
large-scalehardwaredeployment.
GETsvs.traditionalupgrades.
Developsimulationplatformstotest
Lackofframeworkstoincentivizeload
newmarketmechanisms(e.g.,dynamic
MarketIntegration&Policy flexibilityanddetermineequitablecost [N/A]
pricing,ancillaryservices)andpolicy
allocationforgridupgrades.
frameworks.
https://doi.org/10.3390/en19010137

Energies2026,19,137 30of35
6. Conclusions
The rapid proliferation and increasing scale of large AI data centers introduce sig-
nificantchallengestopowersystemsglobally,demandingurgentattentionfromutilities,
regulators,andtechnologydevelopers. Thissurveydetailstheuniqueelectricalcharac-
teristics intrinsic to these facilities. Their high power density concentrates substantial
demandgeographically,whilerapidloadvariability,drivenbythecomputationalpatterns
of AI workloads, introduces fast power swings that deviate from the more predictable,
statisticallysmoothedbehavioroftraditionalaggregatedloads. Furthermore,theinherent
voltage sensitivity of their power electronic-intensive equipment adds another layer of
complexity,asthefacility’sdefensesystemmayoftencausesubstantialloadtrippingoffline.
Thesedistinguishingcharacteristicscollectivelycreatesubstantialhurdlesforconventional
gridplanningandoperation.
Difficultiesariseinensuringlong-termresourceandtransmissionadequacy,asthe
swiftdeploymentcyclesofdatacentersoftenoutpacethemulti-yeartimelinesrequired
forgridinfrastructureupgrades. Real-timegridbalancingandreservemanagementface
increasedstrainduetothemagnitudeandspeedofloadfluctuations,potentiallyrequiring
more costly, faster-responding grid services. Concurrently, these operational dynamics
heightenriskstopowersystemstability,encompassingpotentialdeviationsinfrequency
followinglargeloadchanges,localizedvoltageissuesstemmingfromreactivepowerdy-
namics,andcomplexinstabilitiesdrivenbytheinteractionofnumerouspowerelectronic
converterswiththegridnetwork. Beyondthesecoreoperationalandstabilityconcerns,
thesuccessfulintegrationofAIdatacentersnecessitatescarefulconsiderationofpower
qualityimpactssuchasharmonicsandvoltageflicker,theresolutionofcomplexeconomic
questionsregardingequitableallocationofgridupgradecosts,anddiligentmanagement
ofthesignificantenvironmentalfootprint,whichstemsnotonlyfromsubstantialopera-
tionalenergyconsumptionbutalsofromtheembodiedcarbonembeddedinthehardware
lifecycleandconsiderablewaterusageforcooling.
Addressingtheseinterconnectedandmultifacetedchallengeseffectivelynecessitatesa
coordinated,multi-prongedstrategythatspanstechnologicalinnovation,operationaladap-
tation,andforward-thinkingpolicydevelopment. Solutionscannotresidesolelywithin
onedomain;rather,theyrequireparalleleffortsinvolvingactionsimplementeddirectly
withindatacenters,correspondingadaptationsonthegridside,andtheestablishmentof
supportive,guidingpolicyframeworks. Withinthedatacenteritself,proactivemeasures
suchasthedeploymentofBESStobufferpowerfluctuationsandenhanceride-through
capabilities,theimplementationofadvancedsoftwareorhardware-basedpowersmooth-
ingandramp-ratecontrolstomanagedemandprofiles,theadoptionofgrid-supportive
powerelectronicinterfacessuchasgrid-forminginverterscapableofcontributingtosystem
stability,andtheapplicationofcomprehensivelifecycle-awaredesignprinciplesfocusing
onbothoperationalefficiencyandembodiedenvironmentalimpacts,allofferdirectmeans
tomitigateadversegridinteractionsatthesource.
Concurrently,essentialgrid-sideandpolicyinitiativesmustfocusonimprovingcom-
municationandcoordinationbetweenloadoperatorsandgridmanagers,reformingoften
lengthyinterconnectionprocesseswhilemaintainingreliabilitystandards,modernizing
ratestructuresandcostallocationmechanismstoaccuratelyreflectsystemimpactsand
incentivizebeneficialloadbehaviors,acceleratingthedeploymentofGETstomaximize
existinginfrastructurecapacity,andinstitutingproactive,adaptiveplanningprocessesca-
pableofhandlingtheuniqueuncertaintiespresentedbythisrapidlyevolvingloadcategory.
Furthermore, collaborative models that recognize and leverage the potential flexibility
inherentincertainAIworkloads,suchasdeferrabletrainingtasks,throughwell-designed
https://doi.org/10.3390/en19010137

Energies2026,19,137 31of35
demandresponseorcurtailmentprogramspresentsignificantopportunitiestooptimize
overallgridresourceutilizationanddefercostlyinfrastructureinvestments.
Ultimately,thechallengeposedbyintegratingAIdatacentersextendsbeyondsimply
accommodating an incremental increase in electricity demand. It signifies a potential
fundamentalshifttowardsapowergridincreasinglyinfluencedbylarge,geographically
concentrated,andhighlydynamicloads. Thistransformationdisruptslong-heldassump-
tionsaboutloadpredictabilityandbehavior,demandingaholisticevolutionacrossmulti-
pledimensionsofthepowersystem-encompassingnotjusttechnologicalupgradesbut
alsofundamentaladjustmentsingridarchitecture,marketdesign,operationalprotocols,
andregulatoryapproaches. Successfullynavigatingthiscomplextransitionistherefore
essential. Itrequiresaforward-lookingperspectivethatbalancestheneedtoreliablyand
sustainablypowertheongoingAIrevolutionwiththeimperativetomaintaingridstability,
ensureequitablecostdistribution,andupholdenvironmentalresponsibilityforthebroader
energysystem.
AuthorContributions:Conceptualization,Y.L.andE.G.-G.;methodology,E.G.-G.;software,E.G.-G.
andZ.K.;validation,P.L.andR.M.;formalanalysis,E.G.-G.andZ.K.;investigation,E.G.-G.,P.L.,R.M.
andZ.K.;datacuration,Z.K.andP.L.;writing—originaldraftpreparation,E.G.-G.andR.M.;writing—
reviewandediting,Y.L.,E.G.-G.,J.B.andR.M.;visualization,E.G.-G.,R.M.andJ.B.;supervision,
Y.L.;projectadministrationY.L.;fundingacquisition,Y.L.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Thedatapresentedinthisstudyareopenlyavailablein[DataCenter-
Survey]at[https://github.com/ElinorG11/DataCenterSurvey].
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
AI ArtificialIntelligence
ATS AutomaticTransferSwitch
BESS BatteryEnergyStorageSystem
CMLD CompositeLoadModel
CPU CentralProcessingUnit
DV DynamicVoltage
EV ElectricVehicle
FS FrequencyScaling
GET Grid-EnhancingTechnology
GPU GraphicsProcessingUnit
LLM Largelanguagemodels
LVRT LowVoltageRide-Through
MAE MeanAbsoluteError
MXU MatrixUnit
PDU PowerDistributionUnits
PFC PowerFactorCorrection
PSU PowerSupplyUnit
PUE PowerUsageEffectiveness
RMSE RootMeanSquareError
rPDU rack-mountedPowerDistributionUnits
https://doi.org/10.3390/en19010137

Energies2026,19,137 32of35
RPP RemotePowerPanels
SMR SmallModularReactor
THD TotalHarmonicDistortion
TOU Time-of-Use
TPU TensorProcessingUnit
UPS UninterruptiblePowerSupply
VM VirtualMachine
WUE WaterUsageEffectiveness
References
1. SynergyResearchGroup. HyperscaleDataCenterCountJumpsto43;Another132inthePipeline. 2019. Availableonline:
https://www.globenewswire.com/news-release/2019/01/10/1686004/0/en/Hyperscale-Data-Center-Count-Jumps-to-43-
Another-132-in-the-Pipeline.html(accessedon14September2025).
2. SynergyResearchGroup. HyperscaleDataCenterCountHits1136;AverageSizeIncreases;USAccountsfor54. Availableonline:
https://www.srgresearch.com/articles/hyperscale-data-center-count-hits-1136-average-size-increases-us-accounts-for-54-of
-total-capacity(accessedon14September2025).
3. Cottier,B.;Rahman,R.;Fattorini,L.;Maslej,N.;Besiroglu,T.;Owen,D. TherisingcostsoftrainingfrontierAImodels.arXiv2025,
arXiv:2405.21015.
4. Patel,P.;Choukse,E.;Zhang,C.;Goiri,I.n.;Warrier,B.;Mahalingam,N.;Bianchini,R. CharacterizingPowerManagement
Opportunities for LLMs in the Cloud. In Proceedings of the ACM International Conference on Architectural Support for
ProgrammingLanguagesandOperatingSystems,LaJolla,CA,USA,27April–1May2024;Volume3,pp.207–222.[CrossRef]
5. Choukse,E.;Warrier,B.;Heath,S.;Belmont,L.;Zhao,A.;Khan,H.A.;Harry,B.;Kappel,M.;Hewett,R.J.;Datta,K.;etal. Power
StabilizationforAITrainingDatacenters. arXiv2025,arXiv:2508.14318.[CrossRef]
6. Lu,J.;Liu,A.;Dong,F.;Gu,F.;Gama,J.;Zhang,G. LearningunderConceptDrift:AReview. IEEETrans.Knowl.DataEng.2019,
31,2346–2363.[CrossRef]
7. Elsworth, C.; Huang, K.; Patterson, D.; Schneider, I.; Sedivy, R.; Goodman, S.; Townsend, B.; Ranganathan, P.; Dean, J.;
Vahdat, A.; et al. Measuring the Environmental Impact of Delivering AI at Google Scale. 2025. Available online: https:
//services.google.com/fh/files/misc/measuring_the_environmental_impact_of_delivering_ai_at_google_scale.pdf(accessed
on21October2025).
8. Liu,Y.;Ott,M.;Goyal,N.;Du,J.;Joshi,M.;Chen,D.;Levy,O.;Lewis,M.;Zettlemoyer,L.;Stoyanov,V. RoBERTa:ARobustly
OptimizedBERTPretrainingApproach.arXiv2019,arXiv:1907.11692.
9. xAI. AnnouncingGrok.2023. Availableonline:https://x.ai/(accessedon27October2025).
10. MetaAI. TheLlama3HerdofModels. 2024. Availableonline:https://ai.meta.com/blog/meta-llama-3-1/(accessedon27
October2025).
11. Touvron,H.;Martin,L.;Stone,K.;Albert,P.;Almahairi,A.;Babaei,Y.;Bashlykov,N.;Batra,S.;Bhargava,P.;Bhosale,S.;etal.
Llama2:OpenFoundationandFine-TunedChatModels.arXiv2023,arXiv:2307.09288.[CrossRef]
12. OpenAI. OpenAIAPI.2020. Availableonline:https://openai.com/blog/openai-api(accessedon27October2025).
13. OpenAI. HelloGPT-4o.2024. Availableonline:https://openai.com/index/hello-gpt-4o/(accessedon27October2025).
14. Black, S.; Biderman, S.; Hallahan, E.; Anthony, Q.; Gao, L.; Golding, L.; He, H.; Leahy, C.; McDonell, K.; Phang, J.; et al.
GPT-NeoX-20B:AnOpen-SourceAutoregressiveLanguageModel.arXiv2022,arXiv:2204.06745.
15. Zhang,S.;Roller,S.;Goyal,N.;Artetxe,M.;Chen,M.;Chen,S.;Dewan,C.;Diab,M.;Li,X.;Lin,X.V.;etal. OPT:OpenPre-trained
TransformerLanguageModels.arXiv2022,arXiv:2205.01068.[CrossRef]
16. Scao,T.L.;Fan,A.;Akiki,C.;Pavlick,E.;Ilic´,S.;Hesslow,D.;Castagné,R.;Luccioni,A.S.;Yvon,F.;Gallé,M.;etal. BLOOM:A
176B-ParameterOpen-AccessMultilingualLanguageModel.arXiv2023,arXiv:2211.05100.
17. Chung, H.W.; Hou, L.; Longpre, S.; Zoph, B.; Tay, Y.; Fedus, W.; Li, Y.; Wang, X.; Dehghani, M.; Brahma, S.; etal. Scaling
Instruction-FinetunedLanguageModels.arXiv2022,arXiv:2210.11416.[CrossRef]
18. WikipediaContributors. WuDao.2021. Availableonline:https://en.wikipedia.org/wiki/Wu_Dao(accessedon27October2025).
19. BeijingAcademyofArtificialIntelligence(BAAI). WuDao2.0: China’sLargestPre-TrainedModel. 2021. Availableonline:
http://www.china.org.cn/business/2021-06/03/content_77546375.htm(accessedon27October2025).
20. NVIDIA;Microsoft. UsingDeepSpeedandMegatrontoTrainMegatron-TuringNLG530B,theWorld’sLargestandMost
PowerfulGenerativeLanguageModel.2021. Availableonline:https://developer.nvidia.com/blog/using-deepspeed-and-mega
tron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/(accessedon27
October2025).
https://doi.org/10.3390/en19010137

Energies2026,19,137 33of35
21. InternationalEnergyAgency(IEA). Electricity2024. Availableonline:https://www.iea.org/reports/electricity-2024(accessed
on12September2025).
22. DataCenterDynamics. MetaPlans5GW‘Hyperion’AIDataCenterCluster.2024. Availableonline:https://www.datacenterdy
namics.com/en/news/meta-to-invest-hundreds-of-billions-of-dollars-into-compute-to-build-superintelligence-with-several
-multi-gw-data-center-clusters/(accessedon12September2025).
23. DominionEnergy. DominionEnergyVirginiaIRPFiling.2024. Availableonline:https://www.dominionenergy.com/about/our
-company/irp(accessedon12September2025).
24. Gan,H.;Ranganathan,P. BalanceofPower:AFull-StackApproachtoPowerandThermalFluctuationsinMLInfrastructure.
2025. Availableonline:https://cloud.google.com/blog/topics/systems/mitigating-power-and-thermal-fluctuations-in-ml-infr
astructure(accessedon27October2025).
25. NERC. CharacteristicsandRisksofEmergingLargeLoads.2025. Availableonline:https://tinyurl.com/3jw5xyyh(accessedon
12September2025).
26. NERCLargeLoadsTaskForce. LLTFAprilMeeting&TechnicalWorkshopPresentations. 2025. Availableonline: https:
//www.nerc.com/comm/RSTC/LLTF/LLTF_April_Meeting_&_Technical_Workshop_Presentations_.pdf(accessedon12
September2025).
27. Potomac Economics. 2023 State of the Market Report for the ERCOT Electricity Markets. 2024. Available online: https:
//tinyurl.com/ye22wmdw(accessedon12September2025).
28. Khosravi,A.;Sandoval,O.R.;Taslimi,M.S.;Sahrakorpi,T.;Amorim,G.;GarciaPabon,J.J. Reviewofenergyefficiencyand
technologicaladvancementsindatacenterpowersystems. EnergyBuild.2024,323,114834.[CrossRef]
29. Mytton,D.;Ashtine,M. Sourcesofdatacenterenergyestimates:Acomprehensivereview. Joule2022,6,2032–2056.[CrossRef]
30. Bharany,S.;Sharma,S.;Khalaf,O.I.;Abdulsahib,G.M.;AlHumaimeedy,A.S.;Aldhyani,T.H.H.;Maashi,M.;Alkahtani,H. A
SystematicSurveyonEnergy-EfficientTechniquesinSustainableCloudComputing. Sustainability2022,14,6256.[CrossRef]
31. Ahmed,K.M.U.;Bollen,M.H.J.;Alvarez,M. AReviewofDataCentersEnergyConsumptionandReliabilityModeling. IEEE
Access2021,9,152536–152563.[CrossRef]
32. ElinorGinzburg-Ganz. GitAIDataCenterPowerGridIntegrationAnalysis.2025. Availableonline:https://github.com/Elino
rG11/DataCenterSurvey/tree/main(accessedon29October2025).
33. Xiang,Y.;Li,X.;Qian,K.;Yu,W.;Zhai,E.;Jin,X. ServeGen:WorkloadCharacterizationandGenerationofLargeLanguageModel
ServinginProduction.arXiv2025,arXiv:2505.09999.[CrossRef]
34. Ye,Z.;Gao,W.;Hu,Q.;Sun,P.;Wang,X.;Luo,Y.;Zhang,T.;Wen,Y. DeepLearningWorkloadSchedulinginGPUDatacenters:A
Survey.ACMComput.Surv.2024, 56,146.[CrossRef]
35. Wesolowski, L.; Acun, B.; Andrei, V.; Aziz, A.; Dankel, G.; Gregg, C.; Meng, X.; Meurillon, C.; Sheahan, D.; Tian, L.; etal.
Datacenter-ScaleAnalysisandOptimizationofGPUMachineLearningWorkloads. IEEEMicro2021,41,101–112.[CrossRef]
36. Wang,X.;Wang,X.;Zheng,K.;Yao,Y.;Cao,Q. Correlation-AwareTrafficConsolidationforPowerOptimizationofDataCenter
Networks. IEEETrans.ParallelDistrib.Syst.2016,27,992–1006.[CrossRef]
37. Zheng,K.;Wang,X.;Li,L.;Wang,X. Jointpoweroptimizationofdatacenternetworkandserverswithcorrelationanalysis. In
ProceedingsoftheIEEEINFOCOM2014—IEEEConferenceonComputerCommunications,Toronto,ON,Canada,27April–2
May2014;pp.2598–2606.[CrossRef]
38. Trinh,P.H.;Chung,I.Y. IntegratedActiveandReactivePowerControlMethodsforDistributedEnergyResourcesinDistribution
SystemsforEnhancingHostingCapacity. Energies2024,17,1642.[CrossRef]
39. JeremieEliahouOntiveros,A.P.;Patel,D. AITrainingLoadFluctuationsatGigawatt-Scale-RiskofPowerGridBlackout?2025.
Availableonline:https://semianalysis.com/2025/06/25/ai-training-load-fluctuations-at-gigawatt-scale-risk-of-power-grid
-blackout/(accessedon23July2025).
40. Chen,Y.;Zhang,B. VoltageIssuesCausedbyVolatileDataCenterPowerDemand. arXiv2025,arXiv:2507.06416.
41. Özcan,M.;Wiesner,P.;Weiß,P.;Kao,O. QuantifyingtheEnergyConsumptionandCarbonEmissionsofLLMInferencevia
Simulations.2025. Availableonline:https://arxiv.org/html/2507.11417v1(accessedon23July2025).
42. Long,F.;Lee,G. BridgingtheGap:HowSmartDemandManagementCanForestalltheAIEnergyCrisis.2025. Availableonline:
https://www.goldmansachs.com/what-we-do/goldman-sachs-global-institute/articles/smart-demand-management-can-fo
restall-the-ai-energy-crisis(accessedon16August2025).
43. NERC. Incident Review—Considering Simultaneous Voltage-Sensitive Load Reductions. 2025. Available online: https:
//www.nerc.com/pa/rrm/ea/Documents/Incident_Review_Large_Load_Loss.pdf(accessedon18October2025).
44. ABB. WhyPUETellsOnlyPartoftheDataCenterEnergyEfficiencyStory.2023. Availableonline:https://new.abb.com/drives
/highlights-and-references/why-pue-tells-only-part-of-the-data-center-energy-efficiency-story(accessedon19October2025).
45. Sun,J.;Xu,M.;Cespedes,M.;Kauffman,M. DataCenterPowerSystemStability—PartI:PowerSupplyImpedanceModeling.
CSEEJ.PowerEnergySyst.2022,8,403–419.[CrossRef]
https://doi.org/10.3390/en19010137

Energies2026,19,137 34of35
46. Zhu,T.;Wang,X.;Zhao,F.;Torrico-Bascopé,G.V.Impedance-BasedAggregationofParalleledPowerFactorCorrectionConverters
inDataCenters. IEEETrans.PowerElectron.2023,38,5254–5265.[CrossRef]
47. Bollen,M.H. UnderstandingPowerQualityProblems;IEEEPress:NewYork,NY,USA,2000;Volume3.
48. Ahrabi,R.R.;Mousavi,A.;Mohammadi,E.;Wu,R.;Chen,A.K. AI-DrivenDataCenterEnergyProfile,PowerQuality,Sustainable
Sitting,andEnergyManagement:AComprehensiveSurvey. InProceedingsofthe2025IEEEConferenceonTechnologiesfor
Sustainability(SusTech),LosAngeles,CA,USA,20–23April2025;pp.1–8.[CrossRef]
49. McKinsey Quarterly. The Cost of Compute: A $7 Trillion Race to Scale Data Centers. 2025. Available online: https:
//tinyurl.com/vw2hsue2(accessedon19October2025).
50. GoldmanSachs. AItoDrive165%IncreaseinDataCenterPowerDemandby2030.2025. Availableonline:https://www.gold
mansachs.com/insights/articles/ai-to-drive-165-increase-in-data-center-power-demand-by-2030(accessedon19October2025).
51. UnionofConcernedScientists(UCS). LoopholeCostsCustomersOver$4BilliontoConnectDataCenterstoPowerGrid.2025.
Availableonline:https://www.ucs.org/sites/default/files/2025-09/PJM%20Data%20Center%20Issue%20Brief%20-%20Sep
%202025.pdf(accessedon19October2025).
52. CarnegieMellonUniversity. DataCenterGrowthCouldIncreaseElectricityBills8%NationallyandasMuchas25%inSome
RegionalMarkets.2025. Availableonline:https://www.cmu.edu/work-that-matters/energy-innovation/data-center-growth-c
ould-increase-electricity-bills(accessedon19October2025).
53. Office of the Ohio Consumers’ Counsel. Data Center Costs–Who Should Pay the Costs of Serving These Power-Hungry
Consumers? 2025. Availableonline: https://www.occ.ohio.gov/content/data-center-costs-24-0508-el-ata(accessedon19
October2025).
54. PacificGas;ElectricCompany. OREGONHOUSEBILL3546.2025. Availableonline:https://docs.cpuc.ca.gov/PublishedDocs
/SupDoc/A2411007/8565/580323859.pdf(accessedon19October2025).
55. michigan EIBC. Newsletter: Data Center Tariff Case, More Conference Photos and More. 2025. Available online: https:
//www.mieibc.org/16914-2/(accessedon19October2025).
56. MichiganPublicServiceCommission. MPSCTakesActiontoStrengthenPowerGridandMaximizeCustomerValuefrom
DistributedEnergyResources.2025. Availableonline:https://www.michigan.gov/mpsc/commission/news-releases/2025/03
/13/mpsc-takes-action-to-strengthen-power-grid-and-maximize-customer-value(accessedon19October2025).
57. Li,Y.;Hu,Z.;Choukse,E.;Fonseca,R.;Suh,G.E.;Gupta,U. EcoServe:DesigningCarbon-AwareAIInferenceSystems.arXiv
2025,arXiv:2502.05043.
58. DataCentreDynamicsLtd.(DCD). AmazonSigns159MWOffshoreWindPPAwithIberdrolaintheUK.2024. Availableonline:
https://www.datacenterdynamics.com/en/news/amazon-signs-159mw-offshore-wind-ppa-with-iberdrola-in-the-uk/
(accessedon21October2025).
59. DataCentreDynamicsLtd.(DCD). MicrosoftGrantedPermissiontoRunItsDublinDataCenteronGas.2023. Availableonline:
https://tinyurl.com/n5n45csr(accessedon17October2025).
60. Shi,Y.;Cao,X.;Yang,X. Assessmentandreductionofembodiedcarbonemissionsinbuildings:Asystematicliteraturereviewof
recentadvances. EnergyBuild.2025,345,116058.[CrossRef]
61. Bloomberg. AIDataCentersAreSendingPowerBillsSoaring.2024. Availableonline:https://www.bloomberg.com/graphics/2
025-ai-data-centers-electricity-prices/?embedded-checkout=true(accessedon25October2025).
62. NicholasInstituteforEnergy,Environment&Sustainability. RethinkingLoadGrowth:AssessingthePotentialforIntegrationof
LargeFlexibleLoadsinUSPowerSystems,2025. Availableonline:https://nicholasinstitute.duke.edu/publications/rethinking-l
oad-growth(accessedon18August2025).
63. Unruh,P.;Nuschke,M.;Strauß,P.;Welck,F. OverviewonGrid-FormingInverterControlMethods. Energies2020,13,2589.
[CrossRef]
64. Han,T.;Wang,Y.;Mi,Z.;Han,K.;Tian,J.;Wei,Y.M. Designingandregulatingcleanenergydatacentres. Nat.Rev.CleanTechnol.
2025,1,373–374.[CrossRef]
65. Zidar,J.;Matic,T.;Aleksi,I.;Hocenski,Z.DynamicVoltageandFrequencyScalingasaMethodforReducingEnergyConsumption
inUltra-Low-PowerEmbeddedSystems. Electronics2024,13,826.[CrossRef]
66. HewlettPackardEnterprise. WhatIsDataCenterTiers.2025. Availableonline:https://www.hpe.com/us/en/what-is/data-cen
ter-tiers.html(accessedon18August2025).
67. GoogleCloud. SpannerInstanceConfigurations.2025. Availableonline:https://cloud.google.com/spanner/docs/instance-con
figurations(accessedon18August2025).
68. OpenAI. OpenAIStatusAPI.2025. Availableonline:https://status.openai.com/(accessedon18August2025).
69. Anthropic. ClaudeStatusAPI.2025. Availableonline:https://status.anthropic.com(accessedon18August2025).
70. WorldNuclearAssociation. SmallNuclearPowerReactors.2025. Availableonline:https://world-nuclear.org/information-libr
ary/nuclear-fuel-cycle/nuclear-power-reactors/small-nuclear-power-reactors(accessedon25October2025).
https://doi.org/10.3390/en19010137

Energies2026,19,137 35of35
71. GridStrategies. AdvancedTransmissionTechnologies: EntergyRegionalStateCommitteeWorkingGroup. 2021. Available
online:https://cdn.misoenergy.org/20240927%20ERSC%20Working%20Group%20Item%2004%20Advanced%20Transmissi
on%20Technologies650072.pdf(accessedon25October2025).
72. Belikov,J.;Levron,Y. UsesandMisusesofQuasi-StaticTime-VaryingPhasorModelsinPowerSystems. IEEETrans.PowerDeliv.
2018,33,3263–3266.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/en19010137