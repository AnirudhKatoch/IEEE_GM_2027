| DeepEn2023: |     | Energy | Datasets |     |     | for Edge | Artificial |
| ----------- | --- | ------ | -------- | --- | --- | -------- | ---------- |
Intelligence
| XiaolongTu |     |     |     |     |     | AnikMallik |     |
| ---------- | --- | --- | --- | --- | --- | ---------- | --- |
DepartmentofComputerScience DepartmentofElectricalandComputerEngineering
| GeorgiaStateUniversity |     |     | TheUniversityofNorthCarolinaatCharlotte |     |     |     |     |
| ---------------------- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
3202 voN 03  ]GL.sc[  1v30100.2132:viXra Atlanta,GA30302 Charlotte,NC28223
| xtu1@student.gsu.edu |     |     |     |     | amallik@uncc.edu |          |     |
| -------------------- | --- | --- | --- | --- | ---------------- | -------- | --- |
| HaoxinWang           |     |     |     |     |                  | JiangXie |     |
DepartmentofComputerScience DepartmentofElectricalandComputerEngineering
| GeorgiaStateUniversity |     |     | TheUniversityofNorthCarolinaatCharlotte |     |                    |     |     |
| ---------------------- | --- | --- | --------------------------------------- | --- | ------------------ | --- | --- |
| Atlanta,GA30302        |     |     |                                         |     | Charlotte,NC28223  |     |     |
| haoxinwang@gsu.edu     |     |     |                                         |     | linda.xie@uncc.edu |     |     |
Abstract
| Climatechangeposesoneofthemostsignificantchallengestohumanity. |          |          |               |             |     |          | Asaresult         |
| -------------------------------------------------------------- | -------- | -------- | ------------- | ----------- | --- | -------- | ----------------- |
| of these                                                       | climatic | changes, | the frequency | of weather, |     | climate, | and water-related |
disastershasmultipliedfivefoldoverthepast50years,resultinginover2million
deathsandlossesexceeding$3.64trillionUSD.LeveragingAI-poweredtechnolo-
| gies for sustainable                                                  |     | development | and | combating | climate | change | is a promising |
| --------------------------------------------------------------------- | --- | ----------- | --- | --------- | ------- | ------ | -------------- |
| avenue. NumeroussignificantpublicationsarededicatedtousingAItoimprove |     |             |     |           |         |        |                |
renewableenergyforecasting,enhancewastemanagement,andmonitorenviron-
| mentalchangesinrealtime.            |     |             | However,veryfewresearchstudiesfocusonmaking |                                         |           |     |                    |
| ----------------------------------- | --- | ----------- | ------------------------------------------- | --------------------------------------- | --------- | --- | ------------------ |
| AIitselfenvironmentallysustainable. |     |             |                                             | Thisoversightregardingthesustainability |           |     |                    |
| of AI within                        | the | field might | be attributed                               | to                                      | a mindset | gap | and the absence of |
| comprehensiveenergydatasets.        |     |             | Inaddition,withtheubiquityofedgeAIsystems   |                                         |           |     |                    |
andapplications,especiallyon-devicelearning,thereisapressingneedtomeasure,
analyze,andoptimizetheirenvironmentalsustainability,suchasenergyefficiency.
Tothisend,inthispaper,weproposelarge-scaleenergydatasetsforedgeAI,named
DeepEn2023,coveringawiderangeofkernels,state-of-the-artdeepneuralnetwork
| models,andpopularedgeAIapplications. |     |     |     | WeanticipatethatDeepEn2023will |     |     |     |
| ------------------------------------ | --- | --- | --- | ------------------------------ | --- | --- | --- |
improvetransparencyinsustainabilityinon-devicedeeplearningacrossarangeof
| edgeAIsystemsandapplications. |     |     | Formoreinformation,includingaccesstothe |     |     |     |     |
| ----------------------------- | --- | --- | --------------------------------------- | --- | --- | --- | --- |
datasetandcode,pleasevisithttps://amai-gsu.github.io/DeepEn2023.
1 Introduction
Environmentally-sustainableAIreferstothedesignanduseofartificialintelligence(AI)andmachine
learning(ML)technologiestotackleenvironmentalissuesandadvancesustainability[1],whichisa
two-sidedresearcharea: AIforsustainabilityandsustainabilityofAI[2,3]. Whilethereisgrowing
interestinusingAItoachievetheSustainableDevelopmentGoals(SDGs)[4]relatedtoclimate
change,researchaddressingtheenvironmentalimpactofAIitselfremainslimited[5][6][7][8]. For
instance,asophisticatedAI-empoweredInternetofThings(IoT)systemcanbedeployedtomonitor
andpredictthetotalcarbonemissionsofabuildingorfactory,aligningwiththeobjectiveofAIfor
sustainability. However,thisraisesnewquestions: HowmuchcarbondoesthisAIsystememit? How
sustainableistheAIsystemitself?
TacklingClimateChangewithMachineLearning:workshopatNeurIPS2023.

On-device learning on edge devices, such as smartphones, IoT devices, and connected vehicles,
is increasingly prevalent for model personalization and enhanced data privacy, yet its impact in
termsofcarbonemissionisoftenoverlooked[1,9,10]. Thisoversightmightbeattributedtothe
typicallymodestpowerconsumptionandcarbonfootprintofindividualedgedevices. However,when
consideringtheimmenseproliferationoftheseAI-empowereddevicesworldwide,theircumulative
carbonfootprintwouldbesubstantialandcannotbeoverlooked. Forinstance,considerascenario
whereanindividualusesAI-poweredapplicationsontheirsmartphoneforonehoureveryday. The
averagepowerconsumptionofasmartphoneis3W[11]. With6.4billionsmartphoneconnections
reportedin2022[12],thecumulativeenergyconsumptionofthesesmartphonesamountsto19,200
MWhperday. BasedontheU.S.electricitygenerationcarbonintensityof371.2kgofcarbonperMWh
[13],theestimateddailycarbonemissionsfromthesesmartphoneswouldbe7127.04metrictons. For
comparison,thisisequivalenttotheannualcarbonfootprintof1,848gasoline-poweredpassenger
vehicles. [14]. Therefore,tounderstandandevaluatethesustainabilityofAIsystems,especially
edgeAIsystems,wehavedevelopedthreelarge-scaleenergyconsumptiondatasets: kernel-level,
model-level,andapplication-level. Wehopeourenergydatasets,namedDeepEn2023,willencourage
boththeresearchcommunityandend-userstoprioritizesustainabilityinon-devicelearningandedge
AI,aprinciplethatdrivesourresearch.
2 EnergyMeasurementPlatform
WedevelopedanenergymeasurementplatformemployingtheMonsoonPowerMonitortocapture
powerconsumptiondataduringmodelexecution. Thispowerdata,combinedwithinferencelatency,is
usedtogenerateenergydatasets. TheMonsoonPowerMonitorisselectedforitsmillisecond-leveldata
granularity. SincemostDNNmodellatencies,typicallybetween10to200msonmobileCPUs,can
besignificantlydecreasedto1to50msonmobileGPUs. Comparedtobuilt-insmartphonesensors,
theMonsoonprovidesmoreaccurateanddetailedpowerconsumptiondata,especiallyformodels
runningonedgedevices. Fig.1illustratesthepowermeasurementplatformwehaveimplemented.
Weconnectedbattery-removedsmartphonestothepowermonitorusingpowercables. Thenuse
Monsoonpowermonitortopoweronthedevicesandmeasurepowerconsumptionduringmodel
executionwithagranularityofupto0.2ms. WegeneratedthousandsofTensorFlowLitemodels
acrossvariouslevelsandexecutedthemondifferenthardwareplatformstocreateacomprehensive
dataset.
Forourstudy,weselectedeightmodernedgedevicesfeaturingeightdifferentmobileSoCs,including
at least one high-end and one mid-range SoC from leading chipset vendors such as Qualcomm,
HiSilicon, and MediaTek. These SoCs have been chosen for their status as representative and
advancedmobileAIsiliconwidelyusedinthelasttwoyears.
3 DeepEn2023: EnergyConsumptionDataset
Inthissection,weprovidedetailsofourdatasetsandhowitcontributestounderstandingtheenergy
consumptionandcarbonemissionsofedgeAIsystems. Wehavegeneratedcomprehensivedatasets
fortypicalkernels,modelsandapplicationsacrossvariousconfigurations. Wealsodiscusshoweach
datasetcanfacilitateresearcheffortsaimedataccessingtheadverseimpactofAIcarbonemissions
onglobalclimatechange.
3.1 Kernel-levelEnergyConsumptionDataset
Kernelsconstitutethefundamentalunitsofexecutionindeeplearningframeworks,withtheirtypes
andconfigurationparameterssignificantlyinfluencingtheenergyconsumptionduringDNNmodel
executions. InTable1welistninetypicalkernelsthatarepresentinalmostallCNNmodels,with
theenergyconsumptionandthecarbonemissionrangefordifferentconfigurations. Theprimary
configurations include input height and width (𝐻𝑊)1, input channel number (𝐶 ), output chan-
𝑖𝑛
nel number (𝐶 ), kernel size (𝐾𝑆), and stride (𝑆). Here are the key observations : 1) Energy
𝑜𝑢𝑡
consumptionvariessignificantlyforsamekernelwithdifferentconfigurationsonCPUandGPU.
2)Differentconfigurationparametershavevaryingimpactsforthekernelsenergyconsumption3)
conv⧺bn⧺relukernelstypicallyconsumemoreenergythanotherkerneltypes. 4)Acrossalmostall
1InCNNmodels,inputheightusuallyisequaltoinputwidth.
2

• Thousands of kernel models
• Hundreds of CNN models
• 6 different state-of-the-art AI applications
Monsoon Power Monitor
(with 0.2ms time-granularity)
• 8 different commercial smartphones with advanced AI
chipsets from Qualcomm, HiSilicon, and MediaTek
Energy consumption Carbon emission
Carbon intensity
Figure1: PowerMeasurementPlatformutilizingtheMonsoonPowerMonitortocaptureenergy
consumptiondata. Then,carbonintensityareusedtoconvertthisenergydataintocarbonemission
estimates.
Table1: Measuredkernelsperdeviceinourkernel-leveldataset.
EnergyConsumption(mJ) CarbonEmission(gCO2eq/kWh)2 #Measuredkernels
Kernels CPU GPU CPU GPU Configurations
CPU GPU
min-max min-max min-max min-max
conv⧺bn⧺relu 0.002-1200.083 0.002-120.152 1.762×10−10-1.057×10−4 1.762×10−10-1.058×10−5 1032 1032 (𝐻𝑊,𝐶𝑖𝑛,𝐶𝑜𝑢𝑡,𝐾𝑆,𝑆)
dwconv⧺bn⧺relu 0.022-222.609 0.016-0.658 1.938×10−9-1.961×10−5 1.409×10−9-5.797×10−8 349 349 (𝐻𝑊,𝐶𝑖𝑛,𝐾𝑆,𝑆)
bn⧺relu 0.002-161.334 0.001-14.594 1.762×10−10-1.421×10−5 8.811×10−11-1.285×10−6 100 100 (𝐻𝑊,𝐶𝑖𝑛 )
relu 0.001-141.029 0.003-6.86 8.811×10−11-1.242×10−5 2.643×10−10-6.044×10−7 46 46 (𝐻𝑊,𝐶𝑖𝑛 )
avgpool 0.066-7.711 0.034-1.142 5.815×10−9-6.794×10−7 2.995×10−9-1.006×10−7 28 28 (𝐻𝑊,𝐶𝑖𝑛,𝐾𝑆,𝑆)
maxpool 0.054-7.779 0.032-1.214 4.758×10−9-6.854×10−7 2.819×10−9-1.069×10−7 28 28 (𝐻𝑊,𝐶𝑖𝑛,𝐾𝑆,𝑆)
fc 0.038-94.639 - 3.348×10−9-8.338×10−7 - 24 - (𝐶𝑖𝑛,𝐶𝑜𝑢𝑡 )
c o o t n h c e a r t s 0 0 . . 0 0 0 0 1 1 - - 4 1 2 3 . 2 8 . 2 8 6 61 0 0 . . 0 0 6 0 6 3 - - 3 1 . 0 4 . 2 1 8 63 8 8 . . 8 8 1 1 1 1 × × 1 1 0 0 − − 1 1 1 1 - - 3 1 . . 7 1 7 7 3 0 × × 1 1 0 0 − − 6 5 5 2 . . 8 6 1 4 5 3 × × 1 1 0 0 − − 9 10 - - 3 8 .0 .9 2 5 0 4 × × 1 1 0 0 − − 7 7 1 9 4 8 2 1 7 4 2 2 ( ( 𝐻 𝐻 𝑊 𝑊 , , 𝐶 𝐶 𝑖 𝑖 𝑛 𝑛 1) ,𝐶𝑖𝑛2,𝐶𝑖𝑛3,𝐶𝑖𝑛4 )
thekernels,GPUexhibitbetterenergyefficiencyundersameconfigurations. Studyingtheimpactof
kernelconfigurationsonenergyconsumptionlaysthefoundationforacomprehensiveunderstanding
ofenergyusageduringDNNmodelexecutionsonedgedevices. Thisemphasizestheimportanceof
adaptiveconfigurationselecting,inenhancingtheenergyefficiencyofDNNmodelsandhowitcan
benefitresearchersworkingtowardcarbonneturalgoal.
Tobuildthedataset,weinitiallygeneratealargenumberofkernelswithavarietyoftypes(16types
forCPUand10typesforGPU)featuringarangeofconfigurationsinthetfliteformat(e.g.,1032
conv⧺bn⧺relu and 349 dwconv⧺bn⧺relu kernels). These kernel configurations are randomly
sampled. Thenumberofsampledconfigurationsforeachkerneltypehingesontwomainfactors: its
configurationdimensionanditsimpactontheoverallenergyconsumptionduringDNNexecutions.
Thisdatasetprovidesresearcherswithdetailedinsightsintohowenergyisconsumedwithinmodels
andwhichconfigurationsorparametersaffectkernelenergyefficiency. Researcherscanusethis
datasettoadaptconfigurationswithbesterergyefficiencyonedgedevices,consequentlyreducing
carbonemissions.
3.2 Model-levelEnergyConsumptionDataset
Wealsointroduceourmodel-levelenergydataset,whichcollectsninestate-of-the-artDNNmodels.
These models represent a mix of both manually-designed and NAS-derived models, each with
distinctkerneltypesandconfigurations. Foreachmodel,wegenerate50variantsforconducting
powerandenergymeasurementsbyre-samplingthe𝐶 and𝐾𝑆 foreachlayer. Specifically,we
𝑜𝑢𝑡
randomlysamplethenewoutputchannelnumberfromarangeof20%to180%oftheoriginal𝐶 ,
𝑜𝑢𝑡
2TheunitofmeasurementtypicallyusedforquantifyingandcomparingcarbonemissionsisCO2equivalents.
3

Alexnet DenseNet GoogleNet MobileNetv1 MobileNetv2 ProxylessNAS ResNet18 ShuffleNetv2 SqueezeNet
)%(
egatnecrep
noitpmusnoc
ygrenE
conv dwconv fc concat others
Alexnet DenseNet GoogleNet MobileNetv1 MobileNetv2 ProxylessNAS ResNet18 ShuffleNetv2 SqueezeNet
(a) MobileCPU
)%(
egatnecrep
noitpmusnoc
ygrenE
conv dwconv fc concat others
(b) MobileGPU
Figure 2: DNN model energy consumption percentage breakdown. The top four most energy-
consumingkerneltypesareconv⧺bn⧺relu(conv),dwconv⧺bn⧺relu(dwconv),fc,andconcat.
whilethe𝐾𝑆 issampledfromthesetofvalues: {1,3,5,7,9}. Generally,runningthesemodelson
mobileGPUsresultsinanenergyconsumptionreductionofapproximately49%to79%,compared
totheexecutiononmobileCPUs. Fig. 2presentstheenergyconsumptionbreakdownofindividual
modelsbykerneltypes. Thefourkerneltypesthatconsumethemostenergyareconv⧺bn⧺relu,
dwconv⧺bn⧺relu,fc,andconcat. Theyaccountfor79.27%,14.79%,2.03%,and1.5%ofthetotal
model energy consumption on the mobile CPU, respectively. On the mobile GPU, these kernels
represent78.17%,10.91%,4.01%,and4.28%ofthetotalmodelenergyconsumption. Furthermore,in
mostmodels,conv⧺bn⧺reluanddwconv⧺bn⧺reluaccountforthemainenergypercentages. On
average,conv⧺bn⧺reluanddwconv⧺bn⧺relutake93.97%and87.74%ofthetotalmodelenergy
consumptiononthemobileCPUandGPU,respectively. Withthismodel-levelenergyconsumption
dataset,researcherscanvisuallyseetheenergyconsumptionofdifferentmodelsonvariousplatforms,
helpingthemchoosehemostenergy-efficientmodelsaccordingtotheirneeds.
3.3 Application-levelEnergyConsumptionDataset
Thekernel-andmodel-leveldatasetscanbebeneficialforresearchersanddevelopersinunderstanding,
modelling,andoptimizingpowerandenergyefficiencyofDNNexecutions. However,theenergy
efficiencyofapplicationsonedgedeviceshasamoredirectimpactoncarbonemissions. Toadress
this,wecreateanapplication-leveldataset,whichuncoverstheend-to-endenergyconsumptionofsix
popularedgeAIapplications,coveringthreemaincategories: vision-based(objectdetection,image
classification, super resolution, and image segmentation), NLP-based (natural language question
answering),andvoice-basedapplications(speechrecognition). AsshowninTable2,wemeasure
thepowerandenergyconsumptionofeachapplicationwithmultiplereferenceDNNmodelsthat
operateunderfourdistinctcomputationalsettings,includingCPUwithasinglethread,CPUwithfour
threads,GPUdelegate,andtheNNAPIdelegate. Thedatasetcanserveasaresourceforexploring
theenergyconsumptiondistributionthroughouttheend-to-endprocessingpipelineofanedgeAI
application. Forexample,wecanusethedatasettoexaminetheenergyconsumedingeneratingimage
frames,convertingtheseframesfromYUVtoRGB,andconductingDNNinferencewithinanobject
detectionapplication. Itdemonstratesthatourapplication-leveldatasetcanprovideinterpretable
observations for comprehending who is the primary energy consumer in the end-to-end edge AI
application. Fig. 3depictstheenergyconsumptionbreakdownbasedontheprocessingphasesin
the object detection. It demonstrates that our application-level dataset can provide interpretable
observations for comprehending who is the primary energy consumer in the end-to-end edge AI
application.
3.4 BeneficialForGlobalClimateChange
Thesethreedatasetscancontributetoaddressingglobalclimatechangefromdifferentperspectives.
Forexample,thekernel-leveldatasetcanassistresearchersinidentifyingthemostenergy-efficient
4

|     |     |     |     |     |     |     | Image generation | Image conversion |     | Inference |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------------- | --- | --------- |
O b j e c t
| sneL aremaC | Image   langis egamI | Preview      |                  | Detection results |                | det ec t i o n |     |                                   |     |        |
| ----------- | -------------------- | ------------ | ---------------- | ----------------- | -------------- | -------------- | --- | --------------------------------- | --- | ------ |
|             | sensor gnissecorp    |              |                  |                   |                |                |     |                                   |     |        |
|             |                      | Scale & crop |                  | YUV  to  R GB &   |                |                |     |                                   |     |        |
|             |                      |              |                  | c ro p            | classification | Image          |     |                                   |     |        |
|             | Bayer  filter        | Image buffer | Image reader     |                   | DNN            |                |     |                                   |     |        |
|             |                      |              |                  |                   |                | 0              | 20  | 40                                | 60  | 80 100 |
|             | Image Generation     |              | Image conversion |                   | Inference      |                |     | Energy consumption percentage (%) |     |        |
(a) End-to-endprocessingpipelineforobjectdetection (b) Energyconsumptionpercentagebreakdown
andimageclassification
Figure3: End-to-endenergyconsumptionbreakdownforobjectdetectionandimageclassification
basedonourapplication-leveldataset.
|          | Table2:        | MeasurededgeAIapplicationsperdeviceinourapplication-leveldataset. |     |                                 |                    |     |      |          |       |           |
| -------- | -------------- | ----------------------------------------------------------------- | --- | ------------------------------- | ------------------ | --- | ---- | -------- | ----- | --------- |
|          |                |                                                                   |     |                                 |                    |     |      | Delegate |       | Modelsize |
| Category |                | Application                                                       |     |                                 | ReferenceDNNmodels |     |      |          |       |           |
|          |                |                                                                   |     |                                 |                    |     | CPU1 | CPU4 GPU | NNAPI | (MB)      |
|          |                |                                                                   |     | MobileNetv2,FP32,300×300pixels  |                    |     |      |          |       | 24.2      |
|          |                |                                                                   |     |                                 |                    |     | ✓    | ✓        | ✓     |           |
|          | Imagedetection |                                                                   |     | MobileNetv2,INT8,300×300pixels  |                    |     | ✓    | ✓        | ✓     | 6.9       |
|          |                |                                                                   |     | MobileNetv2,FP32,640×640pixels  |                    |     | ✓    | ✓        | ✓     | 12.3      |
|          |                |                                                                   |     | MobileNetv2,INT8,640×640pixels  |                    |     | ✓    | ✓        | ✓     | 4.5       |
|          |                |                                                                   |     | EfficientNet,FP32,224×224pixels |                    |     | ✓    | ✓ ✓      | ✓     | 18.6      |
Vision-based
|     | Imageclassification |     |     | EfficientNet,INT8,224×224pixels |     |     | ✓   | ✓   | ✓   | 5.4  |
| --- | ------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | ---- |
|     |                     |     |     | MobileNetv1,FP32,224×224pixels  |     |     | ✓   | ✓ ✓ | ✓   | 4.3  |
|     |                     |     |     | MobileNetv1,INT8,224×224pixels  |     |     |     |     |     | 16.9 |
|     |                     |     |     |                                 |     |     | ✓   | ✓   | ✓   |      |
|     | Superresolution     |     |     | ESRGAN,FP32,50×50pixels         |     |     | ✓   | ✓   |     | 5    |
|     | Imagesegmentation   |     |     | DeepLabv3,FP32,257×257pixels    |     |     |     |     |     | 2.8  |
✓
NLP-based Naturallanguagequestionanswering MobileBERT,FP32 ✓ ✓ ✓ 100.7
| Voice-based | Speechrecognition |     |     | Conv-Actions-Frozen,FP32 |     |     |     |     |     | 3.8 |
| ----------- | ----------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
|             |                   |     |     |                          |     |     | ✓   | ✓   | ✓   |     |
kernelconfigurationsandparameters,findingthebalancebetweencomputingperformanceandcarbon
emissions. Wehaveusedourdatasettotrainarandomforestmodeltopredicttheenergyconsumption
andcarbonemissionsofunseenmodels,andtheaccuracyisquitepromising[15]. Themodel-level
datasetaidsresearchersindiscoveringthemostenergy-efficientmodelsbasedonvariousdeployment
requirements. Forinstance,ModelAdeployedonaCPUmayexhibitbetterenergyefficiencythan
ModelBwiththesameaccuracyforimageclassification. Theapplication-leveldatasetprovides
researcherswithinsightsintotheend-to-endenergyconsumptionofanapplicationonedgedevices,
enablingthemtoimplementmorecomprehensivemeasurestoreduceenergyconsumption.
4 Conclusion
Inthispaper,wepresentourenergyconsumptiondatasets,DeepEn2023,fromkernel-level,model-
level,andapplication-leveltofacilitateresearchanddevelopmentaimedatimprovingtheenergy
efficiency and reducing the carbon emissions of AI applications on diverse edge devices. These
datasetsarevaluableresourcesandtoolsforresearchersandcommunitytodesignenergy-efficiency
AI systems with fewer greenhouse gas emissions, thus contributing to the global climate change
mitigation. We hope DeepEn2023 can help shift the mindset of both end-users and the research
communitytowardssustainableedgeAI,aprinciplethatdrivesourresearch.
AcknowledgmentsandDisclosureofFunding
ThisworkwassupportedbytheUSNationalScienceFoundation(NSF)underGrantNo. 1910667,
1910891,and2025284.
5

References
[1] Carole-JeanWu,RamyaRaghavendra,UditGupta,BilgeAcun,NewshaArdalani,KiwanMaeng,
GloriaChang, FionaAga, JinshiHuang, CharlesBai, etal. SustainableAI:Environmental
implications,challengesandopportunities. InProceedingsofMachineLearningandSystems
(MLSys22),volume4,pages795–813,2022.
[2] AimeeVanWynsberghe. SustainableAI:AIforsustainabilityandthesustainabilityofAI. AI
andEthics,1(3):213–218,2021.
[3] RicardoVinuesa,HosseinAzizpour,IolandaLeite,MadelineBalaam,VirginiaDignum,Sami
Domisch,AnnaFelländer,SimoneDanielaLanghans,MaxTegmark,andFrancescoFusoNerini.
The role of artificial intelligence in achieving the sustainable development goals. Nature
communications,11(1):1–10,2020.
[4] Sustainbale Development Goal. https://sdgs.un.org/goals/goal13. Accessed on
September2023.
[5] Jie You, Jae-Won Chung, and Mosharaf Chowdhury. Zeus: Understanding and optimizing
GPUenergyconsumptionofDNNtraining. InProceedingsofthe20thUSENIXSymposiumon
NetworkedSystemsDesignandImplementation(NSDI23),pages119–139,2023.
[6] ManniWang,ShaohuaDing,TingCao,YunxinLiu,andFengyuanXu. Asymo: scalableand
efficient deep-learning inference on asymmetric mobile CPUs. In Proceedings of the 27th
AnnualInternationalConferenceonMobileComputingandNetworking,pages215–228,2021.
[7] SiminChen,MirazulHaque,CongLiu,andWeiYang. Deepperform: Anefficientapproach
forperformancetestingofresource-constrainedneuralnetworks. InProceedingsofthe37th
IEEE/ACMInternationalConferenceonAutomatedSoftwareEngineering,pages1–13,2022.
[8] Dongqi Cai, Qipeng Wang, Yuanqiang Liu, Yunxin Liu, Shangguang Wang, and Mengwei
Xu. Towardsubiquitouslearning: Afirstmeasurementofon-devicetrainingperformance. In
Proceedingsofthe5thInternationalWorkshoponEmbeddedandMobileDeepLearning,pages
31–36,2021.
[9] Carole-JeanWu,DavidBrooks,KevinChen,DouglasChen,SyChoudhury,MaratDukhan,
Kim Hazelwood, Eldad Isaac, Yangqing Jia, Bill Jia, et al. Machine learning at facebook:
Understandinginferenceattheedge. InProceedingsof2019IEEEInternationalSymposiumon
HighPerformanceComputerArchitecture(HPCA),pages331–344,2019.
[10] StefanoSavazzi,SanazKianoush,VittorioRampa,andMehdiBennis. Aframeworkforenergy
andcarbonfootprintanalysisofdistributedandfederatededgelearning. InProceedingsof
2021 IEEE 32nd Annual International Symposium on Personal, Indoor and Mobile Radio
Communications(PIMRC),pages1564–1569,2021.
[11] HaoxinWang,BaekGyuKim,JiangXie,andZhuHan. Energydrainoftheobjectdetection
processingpipelineformobiledevices: Analysisandimplications. IEEETransactionsonGreen
CommunicationsandNetworking,5(1):41–60,2020.
[12] The Mobile Economy 2023. https://www.gsma.com/mobileeconomy/wp-content/
uploads/2023/03/270223-The-Mobile-Economy-2023.pdf. Accessed on September
2023.
[13] HowmuchcarbondioxideisproducedperkilowatthourofU.S.electricitygeneration? https:
//www.eia.gov/tools/faqs/faq.php?id=74&t=11. AccessedonSeptember2023.
[14] Greenhouse Gas Equivalencies Calculator. https://www.epa.gov/energy/
greenhouse-gas-equivalencies-calculator#results. Accessed on September
2023.
[15] XiaolongTu,AnikMallik,DaweiChen,KyungtaeHan,OnurAltintas,HaoxinWang,andJiang
Xie. Unveilingenergyefficiencyindeeplearning: Measurement,prediction,andscoringacross
edgedevices. InProceedingsoftheEighthACM/IEEESymposiumonEdgeComputing(SEC),
pages1–14,2023.
6