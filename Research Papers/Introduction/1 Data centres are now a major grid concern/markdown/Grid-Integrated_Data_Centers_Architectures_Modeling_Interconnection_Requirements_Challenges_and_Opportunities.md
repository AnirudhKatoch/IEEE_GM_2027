Received1June2026;accepted17June2026.Dateofpublication24June2026;
dateofcurrentversion15July2026.ThereviewofthisarticlewasarrangedbyAssociateEditorT.I.Strasser.
DigitalObjectIdentifier10.1109/OJIES.2026.3706771
| Grid-Integrated |             | Data            | Centers:      | Architectures, |
| --------------- | ----------- | --------------- | ------------- | -------------- |
| Modeling,       |             | Interconnection |               | Requirements,  |
|                 | Challenges, | and             | Opportunities |                |
PAMPAULGYANG 1,2 (StudentMember,IEEE),PRATYUSHCHAKRABORTY 1 (SeniorMember,IEEE),
2 2
LASANTHAMEEGAHAPOLA (SeniorMember,IEEE),ANDXINGHUOYU (Fellow,IEEE)
1DepartmentofElectricalandElectronicsEngineering,BITSPilani,Hyderabad500078,India
2DepartmentofElectricalandElectronicEngineering,SchoolofEngineering,RMITUniversity,Melbourne,VIC3000,Australia
CORRESPONDINGAUTHOR:LASANTHAMEEGAHAPOLA(lasantha.meegahapola@rmit.edu.au).
ABSTRACT Datacentersareemergingasoneofthefastest-growingelectricityconsumersworldwidedue
tothe rapid expansion of cloud computing, artificial intelligence (AI),and digitalservices. The large-scale
integrationofAIdatacentersintoelectricpowersystemsintroducessignificantchallengesforgridplanning,
operation, stability, power quality, and compliance with evolving grid codes. Modern data centers are
characterized by power-electronic-dominated infrastructures, including high-density computing platforms,
advanced cooling systems, on-site renewable energy, and energy storage resources, all of which exhibit
dynamic behaviors distinct from conventional passive loads. Consequently, their increasing integration
necessitatesthedevelopmentandapplicationofappropriatemodelingframeworkstoaccuratelyassessgrid
impacts and enable effective control and coordination strategies. This article covers grid-integrated data
centers, with a focus on their electrical and cooling architectures, and associated modeling approaches. In
addition, modeling of critical data center components, interconnection requirements, and key integration
challenges is examined. Finally, emerging opportunities for data centers to provide frequency regulation
and flexibility services are discussed, outlining future research directions toward reliable, efficient, and
grid-interactivedatacenterintegration.
INDEX TERMS Artificial intelligence (AI) data center, data center modeling, fault ride-through (FRT),
graphicsprocessingunit(GPU),hybridcooling,powerquality,powersystem,uninterruptiblepowersupply
(UPS).
| NOMENCLATURE |                                |     | FRT | Faultride-through.      |
| ------------ | ------------------------------ | --- | --- | ----------------------- |
| AESO         | AlbertaElectricSystemOperator. |     | GFM | Grid-forming.           |
| AI           | Artificialintelligence.        |     | GPU | Graphicsprocessingunit. |
| BESS         | Batteryenergystoragesystem.    |     | HIL | Hardwareintheloop.      |
CDU Coolantdistributionunit. HVAC Heating,ventilation,andairconditioning.
| CPU  | Centralprocessingunit.              |     | ICS  | Industrialcontrolsystems. |
| ---- | ----------------------------------- | --- | ---- | ------------------------- |
| CRAC | Computerroomairconditioner.         |     | LV   | Lowvoltage.               |
| CRAH | Computerroomairhandler.             |     | LVRT | Low-voltageride-through.  |
| CRU  | Commissionforregulationofutilities. |     | MV   | Mediumvoltage.            |
EMT Electromagnetictransient. NERC NorthAmericanelectricreliability
| ERCOT | ElectricReliabilityCouncilofTexas. |     |     | corporation.           |
| ----- | ---------------------------------- | --- | --- | ---------------------- |
| ESS   | Energystoragesystem.               |     | PCC | Pointofcommoncoupling. |
E-STATCOM Energystoragestaticsynchronous PDU Powerdistributionunit.
|     | compensator. |     | PFC | Powerfactorcorrection. |
| --- | ------------ | --- | --- | ---------------------- |
©2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/
1080 VOLUME7,2026

| PEM   | Protonexchangemembrane.                |     |     |
| ----- | -------------------------------------- | --- | --- |
| POI   | Pointofinterconnection.                |     |     |
| PSU   | Powersupplyunit.                       |     |     |
| PUE   | Powerusageeffectiveness.               |     |     |
| SCADA | Supervisorycontrolanddataacquisition.  |     |     |
| SLA   | Service-levelagreement.                |     |     |
| TPU   | Tensorprocessingunit.                  |     |     |
| UPS   | Uninterruptiblepowersupply.            |     |     |
| VASP  | ViennaAbinitiosimulationpackage.       |     |     |
| VRM   | Voltageregulatormodule.                |     |     |
| WECC  | Westernelectricitycoordinatingcouncil. |     |     |
I. INTRODUCTION FIGURE1. Globaldatacenterelectricityconsumption,byequipment,Base
Case,2020–2030.
Theunprecedentedexpansionofdigitaleconomyhasacceler-
| ated the adoption | of AI across | a wide range | of applications, |
| ----------------- | ------------ | ------------ | ---------------- |
including computer vision, recommendation systems, scien- trendsarebeingobservedglobally,incountriessuchasChina,
tific computing, optimization, and natural language process- Singapore, Ireland, and the United Kingdom [8]. This trend
ing. Many of these applications rely on large-scale neural- has intensified interest in the concept of grid-integrated data
network-baseddeeplearningalgorithmsthatrequireextensive centers and the manner in which their electrical and ther-
trainingandinferenceworkloads.GenerativeAImodels,such mal infrastructures are analyzed within the context of power
as large language models, including GPT (OpenAI), Gem- system operation, planning, and energy management. Fig. 2
ini (Google DeepMind), and LLaMA (Meta) [1], which are illustrates the evolution of these infrastructures from legacy
designed to generate human-like text and power advanced facilities of the early 2000s to traditional large-scale AI data
conversational agents, drive this growth [2]. The growing centers, characterized by significant increase in facility size,
reliance on deep learning workloads, characterized by long rack power density, cooling complexity, and electrical archi-
trainingcyclesandmassiveparallelprocessingrequirements, tectureadvancement.
isdrivingrapidexpansionofhyperscalecomputinginfrastruc- As the scale and energy intensity of these facilities
ture. As a result of this, data centers are scaling in both size continued to grow, concerns about their impact on the
and density, leading to a significant and sustained increase utility grid prompted system operators to introduce new
in their electricity demand. This surge is placing significant regulatory and policy measures to maintain grid reliability
stressonelectricalgrids,makingtheintegrationandsustain- and resilience. In 2022, data centers significantly increased
ableoperationofdatacentersacriticalchallengeformodern Ireland’snationalelectricitydemand,leadingtheCommission
energyinfrastructure[1],[3],especiallyasthepowerindustry forRegulationofUtilities(CRU)torestrictnewconnections
simultaneously undergoes large-scale system modernization, in Dublin due to grid capacity limitations [9]. Similarly, the
decarbonization,anddigitalizationofitsassets[4].Basedon Netherlandssuspendednewdatacenterpermitsduetoenergy
equipment-specificstatisticsshowninFig.1,theInternational use concerns and infrastructure impacts, while Singapore
Energy Agency reported that global data centers consumed introducedstricterapprovalframeworkstoensurethatfuture
approximately 415TWhofelectricityin2024[5],withcon- developments align with sustainability goals [10], [11], [12].
ventional servers accounting for the largest share at 46.3%. Recently, in Canada, the AESO published new guidelines
Cooling systems contributed 18.1%, followed by accelerated for grid-integrated data centers. These guidelines aim to
serversat14.5%,withother infrastructureandITequipment ensure that data centers are designed, modeled, integrated,
accounting for 10.8% and 10.3%, respectively. This energy and operated, in a manner that maintains grid reliability,
consumptionisprojectedtoincreasesignificantly,potentially stability,andpowerqualitywhilealsoaddressingoperational
doubling to around 945 TWh by 2030, mainly driven by the andplanningchallenges[13].Inthesameway,theAustralian
expandingcomputationaldemandsofAIdatacenters. Energy Market Commission has also proposed technical
Overthepastdecade,countrieswithlow-carbonelectricity standards for large-scale data centers connecting to the
have struggled to meet the growing electricity demands of NationalElectricityMarket[14].
data centers. For instance, in the United States, data centers These measures reflect a growing recognition that data
consumed approximately 183 TWh of electricity in 2024, centerexpansioncanposesignificantriskstogridreliability.
representing more than 4% of the country’s total electricity Moreover, asregulatory frameworks and gridsupport expec-
usage,comparabletoPakistan’sannualelectricitydemand[6]. tations continue to evolve, modern data centers are increas-
Thisconsumptionisprojectedtoincreasetoaround260TWh ingly transitioning from passive energy consumers to grid-
by 2026, which would represent approximately 6% of the interactiveinfrastructures.Inthiscontext,grid-interactivedata
total electricity demand [7]. In Australia, data centers are centers actively respond to grid conditions through coordi-
estimated to have consumed 3.9 TWh in 2025 and is pro- nated mechanisms such as demand response, computational
jected to increase to about 12.0 TWh by 2030. Comparable workload shifting, renewable energy integration, battery
VOLUME7,2026 1081

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
FIGURE2. Evolutionofdatacentercharacteristicsacrossfourgenerations.
TABLE1. ComparisonofExistingLiteratureandScopeCoverageofThisWork
energy storage dispatch, backup generation scheduling, and works concentrating on specific aspects such as electrical
participationinancillaryservicemarkets.Thistransformation architectures, cooling systems, modeling approaches, or the
positionsdatacentersnotonlyasmajorelectricityconsumers associatedchallengesandopportunities,ratherthanproviding
but also as flexible strategic assets capable of supporting a comprehensive coverage of all these dimensions simulta-
powersystemstability,resilience,anddecarbonizationgoals. neously. A review by Oró et al. [15] provided an overview
This transitioning toward grid-interactive operation cre- of existing data center infrastructures, energy efficiency
ates an urgent need for a comprehensive understanding of measures, and renewable energy integration approaches,
data center architectures, modeling approaches, intercon- whileemphasizingtheneedfordynamicmodelsandmetrics
nection requirements, and grid integration challenges and for evaluating energy consumption and emerging efficiency
opportunities. In particular, the increasing coupling between strategies. With the growing interest in grid-integrated and
computational workloads, electrical infrastructures, cooling AI-driven data centers, subsequent review studies expanded
systems, energy storage, and power system dynamics neces- the discussion toward smart grid integration, distributed en-
sitates more advanced and integrated modeling frameworks ergy systems, and advanced cooling technologies [16] [17].
capableofaccuratelyrepresentingdatacenterbehaviorunder More recent high-quality reviews have further examined the
diverseoperatingconditions.Suchunderstandingisessential rapidly increasing electricity demand of AI data centers and
not only for researchers and system operators, but also for its implications for modern power systems. In particular, the
informingfutureregulatoryandplanningframeworkscapable authors of [1] and [18] comprehensively discussed evolving
of balancing continued digital innovation with power system loadcharacteristics,gridimpacts,sustainabilityconcerns,op-
reliability,resilience,andsustainability. erational challenges, and emerging technological solutions,
while Ginzburg-Ganz et al. [19] highlighted the unique grid
A. LITERATURELIMITATIONS integration challenges associated with hyperscale AI-driven
As illustrated in Table 1, a considerable number of review facilities, including their impacts on system planning, stabil-
papershaveexaminedgrid-integrateddatacenters,withmost ity,andenergyinfrastructure.
1082 VOLUME7,2026

FIGURE3. Articleframework.
Despite the valuable contributions of these studies, lim- provides a perspective on converter-driven phenom-
ited attention has been given to the combined analysis of ena, including harmonics, resonance, and stability in
electrical and cooling architectures, modeling approaches, weak grids. In addition, it presents a structured model
interconnectionrequirements,aswellasgridintegrationchal- selectionframeworkthatconnectsstudyobjectivesand
lenges and emerging opportunities. This highlights the need timescalestotherequiredmodelingparameters.
for a more comprehensive review framework that systemati- 3) It clarifies the interconnection requirements for large-
callyexaminesthesecloselyrelatedaspectswithinthecontext scale grid-integrated data center loads by distinguish-
ofmoderngrid-integratedandgrid-interactivedatacenters. ing between mandatory industry practices and recom-
mendedones.
4) Newinsightsintomodelingcriticaldatacentercompo-
B. CONTRIBUTIONS nents are provided, focusing on their dynamic interac-
This article presents a comprehensive and structured re- tions and applicability for grid integration and power
viewofgrid-integrateddatacenters,withparticularfocus on systemstabilitystudies.
theirarchitectures,modelingapproaches,andinteractionwith 5) This article examines the challenges and opportunities
modern power systems. In contrast to existing review stud- ofintegratingmoderndatacenterswiththegrid.
ies, this article examines the evolution of data centers from
legacy infrastructures to traditional facilities and, ultimately, C. ARTICLEFRAMEWORKANDORGANIZATION
to AI data centers, while highlighting the operational transi- The framework illustrated in Fig. 3 clearly connects data
tion from grid-integrated to grid-interactive paradigms. The center architecture, modeling approaches, and grid integra-
maincontributionsofthisarticlearesummarizedasfollows. tionconsiderations.Thephysicalarchitectureofadatacenter
1) This article presents a critical analysis of data cen- forms the structural foundation for developing both device-
ter architectures, discussing the evolution of AC, DC, oriented and system-level models. These models facilitate
andhybridelectricaldistributionsystemsalongsideair- the analysis of dynamic behaviors, control interactions, and
based,liquid-based,andhybridcoolingstrategies,with performance characteristics that directly affect grid-related
emphasis on their efficiency and suitability for high- issues. The framework provides a cross-layer perspective
densitycomputingworkloads. by linking architectural elements with relevant modeling
2) Itexamines12modelingapproachesforgrid-integrated paradigmsandinterconnectionrequirements,challenges,and
data centers, detailing their underlying assumptions, opportunities. This perspective is intended to support re-
scope, applicability, advantages, and limitations, and searchersinthecoordinateddesign,analysis,andoperationof
VOLUME7,2026 1083

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
TABLE2. KeywordCategoriesUsedforLiteratureSearch
datacenters,positioningthemasactiveparticipantsinfuture excluded, while eligible studies proceeded to a full-text
powersystems. assessment to evaluate their relevance and suitability for in-
The rest of this article is organized as follows. Section II clusion. Following the full-text screening stage, the final set
provides the review methodology. Section III presents an of articles was selected for detailed analysis and catego-
overview of data center architectures. Section IV reviews rized according to the key themes of architectures, modeling
modelingapproachesandconverter-drivenphenomenaappli- approaches, interconnection requirements, challenges, and
cable to data center for grid studies. Section V then focuses opportunities. In addition, manual reference searching was
on the modeling of critical components within data center performedbyexaminingthereferencelistsofhighlyrelevant
electricalandcoolinginfrastructures.SectionVIdiscussesin- papers,particularlyreviewarticles,toidentifyfurtherstudies
terconnectionrequirementsrelevanttodatacenterintegration, that may not have been captured during the initial database
| whileSectionVIIexamineskeyintegrationchallengesonthe |     |     |     |     |     |     | search. |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
grid.SectionVIIIhighlightstheopportunitiesfordatacenters
| to provide | flexibility | services. |     | Finally, | Section | IX concludes |                              |     |     |     |     |     |     |
| ---------- | ----------- | --------- | --- | -------- | ------- | ------------ | ---------------------------- | --- | --- | --- | --- | --- | --- |
|            |             |           |     |          |         |              | III. DATACENTERARCHITECTURES |     |     |     |     |     |     |
thisarticleandoffersfutureneeds.
|     |     |     |     |     |     |     | The architecture |           | of a data   | center | is fundamentally |               | composed   |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | ----------- | ------ | ---------------- | ------------- | ---------- |
|     |     |     |     |     |     |     | of integrated    | power     | network,    |        | cooling,         | and IT        | subsystems |
|     |     |     |     |     |     |     | designed         | to ensure | continuous, |        | reliable,        | and efficient | opera-     |
II. REVIEWMETHODOLOGY
|     |     |     |     |     |     |     | tion [20]. | Power | is supplied | from | the utility |     | grid through a |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | ---- | ----------- | --- | -------------- |
Theliteraturesurveyisconductedtoidentifyexistingstudies
|               |            |         |            |           |           |          | power management |            | and | distribution | system       | that       | coordinates |
| ------------- | ---------- | ------- | ---------- | --------- | --------- | -------- | ---------------- | ---------- | --- | ------------ | ------------ | ---------- | ----------- |
| using several | scientific |         | databases, | including | Google    | Scholar, |                  |            |     |              |              |            |             |
|               |            |         |            |           |           |          | with back-up     | generation |     | units        | to guarantee | redundancy | and         |
| IEEE Xplore,  | IET        | Digital | Library,   | Scopus,   | Springer, |          | Wiley,           |            |     |              |              |            |             |
resilience.TheUPSservesasabufferagainstpowerinterrup-
andTaylor&Francis.Thesedatabaseswerechosentoensure
|                   |          |          |             |              |                  |           | tions and      | grid disturbances, |            | ensuring           | continuous |                 | and stable   |
| ----------------- | -------- | -------- | ----------- | ------------ | ---------------- | --------- | -------------- | ------------------ | ---------- | ------------------ | ---------- | --------------- | ------------ |
| comprehensive     | coverage |          | of journal  |              | and conference   |           | papers,        |                    |            |                    |            |                 |              |
|                   |          |          |             |              |                  |           | power delivery |                    | to servers | and                | network    | infrastructures | [21].        |
| technical         | reports, | industry | guidelines, |              | and relevant     | standards |                |                    |            |                    |            |                 |              |
|                   |          |          |             |              |                  |           | Within         | the data           | center,    | the infrastructure |            | can be          | broadly cat- |
| related to        | power    | systems  | and         | data center  | infrastructures. |           | To             |                    |            |                    |            |                 |              |
|                   |          |          |             |              |                  |           | egorized       | into two           | domains:   | 1)                 | facility   | infrastructure, | which        |
| ensure systematic |          | coverage | of          | the research | domain,          |           | a struc-       |                    |            |                    |            |                 |              |
|                   |          |          |             |              |                  |           | includes       | cooling            | systems    | and                | auxiliary  | support         | equipment    |
turedkeyword-basedsearchstrategywasadopted.Thesearch
termsaregroupedintosixthematiccategories,asdetailedin and2)serverandnetworkinfrastructure,whichcomprisesof
|          |           |         |          |     |             |       | conventional | servers | (e.g., | CPUs), | accelerated |     | servers (e.g., |
| -------- | --------- | ------- | -------- | --- | ----------- | ----- | ------------ | ------- | ------ | ------ | ----------- | --- | -------------- |
| Table 2. | The first | keyword | category |     | defines the | scope | of the       |         |        |        |             |     |                |
GPU-basedsystems),andotherITcomponents.
| target infrastructure, |     | followed |     | by the | second category, |     | which |     |     |     |     |     |     |
| ---------------------- | --- | -------- | --- | ------ | ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
focusesontheoperationalandarchitecturalcharacteristicsof
datacenters.Thethirdcategoryaddressesmodelingandana- A. DATACENTERELECTRICALARCHITECTURES
lyticalapproachesrelevanttogridinteractionstudies,andthe Adatacenter’selectricalarchitecturedefinestheoutcomeof
fourth emphasizes interconnection and compliance require- itsefficiency,reliability,andoverallcost[22].Fig.5illustrates
ments.Thefifthcategorycapturesgridintegrationchallenges the advancement of data center electrical architectures from
and their associated operational impacts, whereas the sixth the 208-V AC distribution system toward advanced 800-V
highlights grid support services and flexibility opportunities. DC configurations developed to support the increasing com-
ThekeywordgroupswerecombinedusingBooleanoperators putationalandpowerdensityrequirementsofAIdatacenters.
suchas“AND”and“OR”toretrievestudiessatisfyingmultiple TheevolutionhighlightsagradualtransitionfromlegacyAC-
searchcriteriasimultaneously. based topologies with multiple power conversion stages to
To ensure relevance to contemporary developments, only modernhybridAC/DCandfullyDC-distributedarchitectures,
studies published between 2015 and 2026 were considered. aimed at reducing conversion losses, improving efficiency,
Records that did not align with the review objectives were enhancing scalability, and supporting high-performance
| 1084 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

TABLE3. ComparisonofACandDCPowerArchitecturesinDataCenters
| computing | infrastructures. | The | architecture |     | includes | the full |     |     |     |
| --------- | ---------------- | --- | ------------ | --- | -------- | -------- | --- | --- | --- |
arrangementofACpowerdeliveryelementsandhowtheyare
| connected     | from the utility | to            | the UPSs,       |            | backup generators, |          |     |     |     |
| ------------- | ---------------- | ------------- | --------------- | ---------- | ------------------ | -------- | --- | --- | --- |
| ESSs, PDUs,   | and down         | to the        | power           | supply     | unit (PSU).        | In       |     |     |     |
| this setup,   | the UPS serves   | as            | a protection    |            | scheme             | for sen- |     |     |     |
| sitive loads, | ensuring         | continuous    | operation       |            | by conditioning    |          |     |     |     |
| the incoming  | supply           | and providing |                 | short-term | backup             | dur-     |     |     |     |
| ing outages   | [23]. The        | PDUs          | then distribute |            | and monitor        | this     |     |     |     |
conditionedpowerthroughoutthefacility,steppingitdownor
transformingitasneededtomatchtherequirementsofdiffer-
entequipmentzones[24].Atthefinalstage,thePSUswithin
eachserverconverttheincomingACpowertoanLVDClevel
| required | by the electronic | components, |     | while | also managing |     |     |     |     |
| -------- | ----------------- | ----------- | --- | ----- | ------------- | --- | --- | --- | --- |
powerqualityandsupportingenergy-efficientoperation. FIGURE4. ACversusDCpowercablecomparison;dataextracted
from[27].
| Over           | time, the rise | in energy | costs      | and       | the push | toward   |     |     |     |
| -------------- | -------------- | --------- | ---------- | --------- | -------- | -------- | --- | --- | --- |
| sustainability | led data       | center    | electrical | designers | to       | investi- |     |     |     |
gatealternativepowerdistributionarchitectures[25].Among andcablepowerdensityofdatacenterpowersystems.Com-
these, DC distribution gained significant attention due to its pared with the conventional 415-V AC architecture, higher
successful deployment in data centers over the past decade, voltage AC and especially DC distribution systems can de-
offering notable advantages such as improved energy effi- liver substantially more power through the same conductor
ciency, reduced conversion losses, enhanced power quality, size, with 800- and 1500-V DC architectures providing ma-
jorimprovementsintransferablepowerandcableutilization.
| and increased | system | reliability | [26]. | Despite | these | benefits, |     |     |     |
| ------------- | ------ | ----------- | ----- | ------- | ----- | --------- | --- | --- | --- |
the widespread adoption of DC architectures remained lim- This shows that higher voltage DC architectures can better
ited because of the lack of universally accepted standards, supportthegrowingrack-levelpowerdemandsoflarge-scale
as well as the challenges associated with specialized protec- AI data centers. Thus, this subsection reviews and compares
tion requirements and complex fault-coordination strategies conventional AC and emerging DC-based power distribution
approaches,whichdiffersignificantlyintermsofpowerdistri-
inDC-basedsystems[22].
In response, more advanced and efficient power conver- butiontopology,conversionstages,andoverallinfrastructure
| siontechnologiesweredevelopedtominimizelosses,forming |                |            |     |     |             |        | demands. |     |     |
| ----------------------------------------------------- | -------------- | ---------- | --- | --- | ----------- | ------ | -------- | --- | --- |
| the basis                                             | of what is now | considered |     | the | traditional | AC ar- |          |     |     |
chitecture widely deployed in traditional data centers. This 1) CONVENTIONALCPUDATACENTERS
approach has remained adequate for legacy and traditional DatacenterelectricalarchitecturesmainlyuseACdistribution
facilitieswithmoderaterack-levelpowerdensities.However, systems.ThesesystemsweredesignedtosupportgeneralIT,
therapidgrowthofAIworkloadshasledtoanunprecedented enterprise computing, and cloud workloads, with rack-level
increaseincomputer-rackpowerdensity,promptingdesigners powerdensitiestypicallyrangingfrom3to10kW[28].
to reevaluate the suitability of existing architectures and to Fig. 5(a) and (b) illustrates the AC distribution electrical
reconsider DC-based systems. Recently, NVIDIA [27] has architecturethathasbeenwidelyadoptedinlegacyandtradi-
released a technical report proposing an 800-V DC architec- tionaldatacenters,respectively.AsshowninFig.5(a),utility
turetailoredfornext-generationAIinfrastructure,illustrating power enters through the MV bus and is stepped down to
howhigh-voltageDCdistributioncanbeintegratedwithESSs the LV distribution level, where it supplies both the IT load
to meet the demands of AI data centers. Table 3 provides a andthefacilityinfrastructure,includingchillers,CRAHunits,
comparisonofACandDCpowerarchitecturesindatacenters,
|     |     |     |     |     |     |     | pumps, and lighting. | A double-conversion | LVAC UPS forms |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ------------------- | -------------- |
which highlights their respective advantages, disadvantages, the core of the critical power path, providing voltage condi-
and suitability for large-scale AI data centers. Furthermore, tioning and ride-through capability through an AC–DC–AC
Fig.4demonstratesthatincreasingtheoperatingdistribution conversion chain and an integrated battery system. At the
voltage significantly enhances the power transfer capability downstream side of the UPS, power is further transformed
VOLUME7,2026 1085

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
(a)
(b)
(c)
(d)
(e)
FIGURE5. Advancementofdatacenterelectricalarchitectures.(a)Legacy,(b)traditional,(c)moderndatacenterdistributionwithwhite-spaceretrofit,
(d)moderndatacenterhybridpowerdistribution,and(e)future-readypowerdistributionarchitecture[27],[33].
1086 VOLUME7,2026

byrack-levelorfloor-levelPDUs(e.g.,415/208VAC),after notprovideafullyoptimizedend-to-endsolution,asitintro-
whichserverPSUsperformanadditionalAC–DCconversion ducesadditionalconversionstages[27].Nevertheless,itoffers
to deliver 12 V DC to individual VRMs that feed the CPU, a practical upgrade pathway from traditional AC infrastruc-
storage,andnetworkingmodules. turetowardahigh-voltageDCarchitecturewithoutrequiring
The proliferation of virtualization and hyperscale comput- immediatelarge-scaleelectricalroomreplacements.
ing brought about the adoption of modular and redundant A related approach, as illustrated in Fig. 5(d), involves
architecture. Fig. 5(b) illustrates the existing traditional ar- a facility-level hybrid AC–DC power architecture designed
chitecture, which represents an improvement over legacy to support high-density computing environments, including
systems. This architecture incorporates optional generators racks for AI accelerators. The architecture starts at the MV
for redundancy and supports limited grid-interactive opera- interface, where utility power, optionally supplemented by
tions.Inaddition,externalenergystorageunitsareintegrated an on-site generator, is stepped down through MV/LV trans-
to help smooth the fast power dynamics caused by GPU formers to create a 480-V AC LV bus. A key feature of this
workloads [27]. It is worth noting that the voltage supplied architecture is the implementation of a facility-level AC/DC
totherackis415VAC,whilethePSUvoltageisincreasedto rectificationstage.Multiplerectifierstringscanoperateinpar-
54VDC.Thisincrementalimprovementreducesconversion allel, allowing for modular expansion and providing a stable
losses and increases the rack power density. One of the key DC bus that can support multimegawatt IT loads (approx-
advantages of this architecture is the improvement in PUE imately 1.5 MVA) [27]. The architecture enables seamless
values,whichhavedecreased. integration of energy storage units on the DC side. These
Conventional AC-based architectures remain robust, ma- storage systems, connected directly to the DC bus, offer
ture,andwidelycompatiblewithgridinfrastructure.Nonethe- rapid buffering for voltage support, transient suppression,
less, their multiple conversion stages inherently limit effi- andride-throughcapability.Importantly,theirdirectDCcon-
ciency and scalability, making them less suitable for modern nection avoids additional conversion losses and ensures a
high-densityAIworkloads. subsecond response to the fast load fluctuations typical of
GPUworkloads.Overall,thisarchitectureprovidesaflexible
foundation for integrating fast-acting energy storage particu-
larly suited for emerging AI data center deployments, where
2) ACCELERATEDGPUDATACENTERS highpowerdensities,rapidtransients,andstringentefficiency
TheemergenceofAItechnologiesandGPU-acceleratedcom- requirements exceed the capabilities of traditional AC-only
puting has fundamentally altered the power delivery require- architectures.
mentsofmoderndatacenters.ContemporaryAItrainingclus- Tosupportthelong-termgrowthandrisingpowerdemand
ters exhibit rack-level power densities exceeding 10–30 kW of AI data centers, Huntington and Tu [27] evaluate the use
[28], with next-generation GPU superpods trending toward of MV rectifiers for converting MV AC input to an 800-V
80–120 kW per rack [29], which is far beyond the capacity DC power feed. The study also examines solid state trans-
designforconventionalACarchitectures.Thesehigh-density former technology as a potential future option for enhancing
systems exhibit rapid and unpredictable load transients dur- resilienceanddistributionefficiencyinnext-generationfacili-
ing training cycles, placing significant stress on distribution ties.AsshowninFig.5(e),thepowerconversionsectiontakes
equipment, power conversion stages, and thermal infrastruc- MV AC (up to 35 kV) and directly converts it into 800 V
ture [30]. As a result of these challenges, new transitional DC using a solid state transformer conversion chain. This
architecturesarebeingdesignedtobridgethegapbetweenthe chain integrates AC-to-DC rectification, large-scale DC–DC
conventionalACpowerdistributionarchitectureandthelong- voltageregulation,andhigh-capacityDCdistributionspecifi-
established±400VDCarchitecturewidelyusedintelecom- callydesignedfordenseAIcomputeracks.Byeliminatingthe
munication and data centers [31], as well as the emerging intermediate480-VACdistributionlayer,thisdesignshortens
800-VDCdatacenterarchitectureshowninFig.5(c)[27].Al- the power path and simplifies infrastructure, reducing com-
though±400VbipolarDCarchitecturestheoreticallyprovide plexity.
inherentadvantagesingroundingandfaultisolation[27],their
deployment is constrained by the lack of protection devices. B. COOLINGSYSTEMARCHITECTURES
However, to relieve the growing imbalance between infras- Effective thermal management is fundamental to ensuring
tructure and compute space caused by AC power’s multiple that equipment in modern data centers operates reliably and
conversion stages [32], transitional 800-V DC side-power efficiently. As rack power densities continue to increase and
racks housing localized rectifiers and distribution equipment heat loads intensify,the efficiency ofheat rejectionand ther-
can be introduced to shift conversion out of the compute mal control mechanisms has become a defining factor in
rack and enable higher density AI deployments. Therefore, the overall performance [34]. The effectiveness of a cool-
in this architecture, the facility-level AC–DC conversion is ing system, whether implemented at a rack, row, or facility
centralized,andthe±400/800VDCbusreplacestheACdis- scale, is influenced by multiple factors, including airflow
tributionstage,withracksreceivinghigh-voltageDCdirectly distribution, heat transfer efficiency, coolant type and flow
andperformingonlyDC–DCconversion.Thisapproachdoes characteristics,systemintegrationwithITloaddynamics,and
VOLUME7,2026 1087

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
FIGURE6. Schematicdiagramofdirectandindirectfreecoolingarchitectures.(a)Directair-sidecooling.(b)Indirectair-sidecooling.(c)Direct
water-sidecooling.(d)Indirectwater-sidecooling[35].
the resilience of components under varying environmental architectural level, air cooling is commonly implemented at
conditions[35].Toadvancesystemefficiency,awiderangeof theroom,row,andracklevels,withthechoicelargelydeter-
coolingarchitectureshavebeendeveloped,focusingprimarily mined by the heat density of the IT equipment. Room-level
onadvancementsincoolingsystem,thermalinterfacedesign, systems rely on CRAC or CRAH units that deliver cold air
and control strategies. These innovations directly influence throughraised-floorplenumstocoldaisles,enablinga“face-
heat dissipation efficiency, PUE, and long-term operational to-face, back-to-back” rack configuration that separates cold
reliability. and hot airflow streams. While this architecture is simple
Amongthevariouscoolingconfigurationsdeployedindata andwidelydeployed,itslongairflowpathsandlargethermal
centers,systemarchitecturescanbebroadlycategorized into management domain make it susceptible to mixing losses
air-based,liquid-based, and hybrid cooling frameworks [35], and nonuniform cooling [35]. To address these limitations,
[36]. As implied by the term, air-based cooling relies on row-level cooling positions dedicated CRAH units directly
conditioned airflow to dissipate heat, though numerous de- alongsidespecificrackrowstoshorteningtheairflowdistance
signoptimizationssuchashot/coldaislecontainment,in-row and improving the targeting of cold air. At the most targeted
cooling,andraised-floorplenumsystemshavebeenexplored level, rack-level cooling integrates the cooling unit directly
to enhance thermal performance. In contrast, liquid-based within the rack, enabling heated air to return directly to the
cooling solutions are distinguished by their direct or indirect cooling module rather than recirculating into the room. This
contact mechanisms, ranging from liquid immersion cooling configuration supports much higher heat densities, typically
tocold-plateandrear-doorheatexchangersystems,whilehy- above50kWperrack,whiledeliveringmorepreciseairflow
brid cooling approaches combine both air and liquid cooling controlandgreatercoolingcapacityutilization.
techniques to improve thermal efficiency, operational flex- Free cooling is an advanced and well-established outdoor
ibility, and energy effectiveness. The following subsection cooling strategy used in conventional and large-scale data
provides a detailed analysis of these cooling architectures, centers and is particularly effective in reducing mechanical
examining their structural configurations, operational advan- coolingenergydemand[17].Theeffectivenessofthiscooling
tages, and limitations in modern and next-generation data architecturehasbeenvalidatedacrossawiderangeofclimatic
centerenvironments. and operational studies. For instance, analyses have shown
thatthetechniqueperformsoptimallyinregionswithambient
1) AIRCOOLINGSYSTEMS temperatures below 20 ◦ C and relative humidity above 60%
Air-based cooling remains the most widely adopted thermal [37]. Thus, seasonal benefits of optimal control frameworks
management approach in conventional data centers due to canreducethetotalenergyofthefacilityenergyduringwin-
its mechanical simplicity, ease of deployment, and compat- ter. Performance potential also exhibits strong geographical
ibility with existing IT hardware layouts. In typical config- variability; some temperate and coastal cities are capable of
urations, heat generated by IT equipment is transferred to operating in free cooling mode for more than 3000 hours
the surrounding air and transported out of the white space annually, whereas colder regions increasingly rely on flexi-
through controlled airflow pathways. The performance of bledecisionthresholdstoaccommodatewiderenvironmental
such systems is determined by the efficiency of air distri- operatingranges[38].
bution, pressure management, and the ability to minimize This approach is commonly implemented through air-side
thermal mixing between hot and cold air streams. Based on and water-side cooling strategies, which can be classified
1088 VOLUME7,2026

FIGURE7. Schematicdiagramofliquidcoolingarchitectures.(a)Single-phaseimmersionliquidcooling.(b)Two-phaseimmersionliquidcooling.
(c)Coldplateliquidcooling.(d)Sprayliquidcooling[39].
as direct or indirect free cooling. Direct air-side cooling, Recent research consistently highlights the performance
shown in Fig. 6(a) introduces filtered outside air directly andefficiencyadvantagesofliquidcoolinginAIdatacenters.
into the server room to remove heat, offering high efficiency Ramakrishnanetal.[40]reportthatdirectliquidcoolingcan
but relying heavily on ambient weather conditions. Indirect improveGPUperformanceefficiencyby2.7%,cutpowercon-
air-side cooling, shown in Fig. 6(b), keeps outdoor air sep- sumption by 12%, and reduce chip temperatures by roughly
◦
arate from indoor air by using heat exchangers, improving 20 C. These results are reinforced by Latif et al. [41], who
control and minimizing contamination risks. For water-side show that liquid-cooled GPUs operate at significantly lower
◦
strategy, direct cooling (water-side) circulates chilled water temperatures (41°C–50 C) than air-cooled counterparts
◦
or coolant directly through cooling coils inside the server (54°C–72 C), enabling up to 17% higher performance. As
room to absorb heat from the recirculating air, as shown in processorthermaldesignpowertrendstoward700W,Azari-
Fig. 6(c). Indirect water-side cooling, shown in Fig. 6(d), far et al. [42] argue that liquid cooling is becoming essential
transfersheatthroughintermediateloopssuchascoolingtow- for sustaining performance and energy efficiency in modern
ers,chillers,orheatexchangerswithoutbringingfacilitywater AI-drivendatacenters.MajorenergycompaniessuchasShell,
into direct contact with IT equipment environments, allow- ExxonMobil,andBPareincreasinglysupportingtheadoption
ing safer operation and easier integration with free cooling ofliquidcoolingindatacenters,backedbyseveralpilotinitia-
methods. tivesandstrongprojectedmarketgrowth[43].Liquidcooling
Overall, free cooling remains a climate-dependent op- technologies for servers generally fall into three categories:
timization method, with real-world energy benefits tightly immersion cooling (single- and two-phase), cold-plate cool-
coupledtolocalizedatmosphericconditionsandsite-specific ing, and spray-based cooling [39]. Among these, cold-plate
inlet-air constraints. However, conventional air cooling ap- cooling has become the most widely adopted approach. As
proachesarephysicallyinsufficienttohandletheextremeheat noted by Zhang et al. [44], it is the earliest established and
densitiesofAIdatacenters. most commonly used liquid cooling method, and it delivers
significantly better thermal performance than conventional
aircooling.
2) LIQUID-BASEDCOOLINGSYSTEMS Fig. 7(a) shows a single phase immersion cooling, where
Modernprocessorscanexceed100W/cm2,whileaircooling servers are fully submerged in a liquid coolant that always
typicallydissipatesonlyaround37W/cm2,creatingawiden- remains in the liquid state, absorbing heat through sensi-
ing thermal gap that leads to inefficiency, rising energy use, ble heat transfer before being pumped to a heat exchanger.
and thermal instability in data centers [17]. This challenge This approach uses a simple control design, limits coolant
is intensified by the rise in rack power density, with next- loss through effective sealing, and requires little to no fluid
generation deployments expected to exceed 30 kW per rack, replacement. In contrast, as shown in Fig. 7(b), two-phase
comparedwithmuchlowerdensitiesintraditionalsystems.To immersion cooling submerges servers in a low-boiling-point
tackle these escalating demands, liquid cooling has emerged dielectric fluid that vaporizes when the server components
as a leading solution and a key direction for next-generation heat up, with the vapor then condensed and returned to the
datacenterinfrastructure. tank. By using latent heat during this phase change, this
VOLUME7,2026 1089

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
FIGURE8. SystemconfigurationofahybridcoolingarchitectureforfutureAI-drivendatacenters[36].
approach can be used to reject heat efficiently. In cold-plate used to avoid the significant cost and complexity associated
liquidcooling,thecoolingtargetshigh-heatcomponentslike withfullyliquid-cooledAIdatacenterdesigns.
CPUsandGPUsbytransferringheattoacirculatingcoolant
| through | attached cold | plates, as shown | in Fig. 7(c). The |     |     |     |     |
| ------- | ------------- | ---------------- | ----------------- | --- | --- | --- | --- |
IV. MODELINGOFGRID-INTEGRATEDDATACENTERS
| coolant flows | through a | manifold to each | server and then | to  |     |     |     |
| ------------- | --------- | ---------------- | --------------- | --- | --- | --- | --- |
a CDU, which rejects heat to an external cooling system. Modelingisessentialforunderstandingthedynamicinterac-
tionsbetweengrid-integrateddatacentersandmodernpower
| Finally, | spray liquid cooling | delivers coolant | directly onto |     |     |     |     |
| -------- | -------------------- | ---------------- | ------------- | --- | --- | --- | --- |
systems.Differentmodelingapproachesarerequireddepend-
| heat-producing | components | through precision | nozzles, using |     |     |     |     |
| -------------- | ---------- | ----------------- | -------------- | --- | --- | --- | --- |
ingontheintendedstudyobjective,rangingfromsteady-state
lessfluidthanimmersionsystems,asshowninFig.7(d).The
|     |     |     |     | power flow | analysis to fastEMT | and stability | investigations. |
| --- | --- | --- | --- | ---------- | ------------------- | ------------- | --------------- |
warmedcoolantiscollected,cooled,andrecirculatedthrough
|          |                 |                       |              | In addition, | converter-driven | phenomena      | such as harmonics, |
| -------- | --------------- | --------------------- | ------------ | ------------ | ---------------- | -------------- | ------------------ |
| a system | that includes a | pump, heat exchanger, | and external |              |                  |                |                    |
|          |                 |                       |              | resonance,   | and interaction  | with weak-grid | introduce further  |
coolingunit.
challengesthatnecessitatedetailedrepresentationofconverter
|     |     |     |     | dynamics | and network behavior. | This section | discusses the |
| --- | --- | --- | --- | -------- | --------------------- | ------------ | ------------- |
3) HYBRIDCOOLINGSYSTEMS
|     |     |     |     | major modeling | approaches | for grid-integrated | data centers |
| --- | --- | --- | --- | -------------- | ---------- | ------------------- | ------------ |
Thehybridcoolingarchitectureintegratesbothair-basedand
andexaminesthekeyconverter-drivenphenomenathatinflu-
liquid-basedcoolingtosupportthehighheatdensitiestypical
encesystemperformanceandstability.
| of AI data | centers [1]. As | illustrated in Fig.  | 8, the approach |     |     |     |     |
| ---------- | --------------- | -------------------- | --------------- | --- | --- | --- | --- |
| proposed   | by Chen et al.  | [36] can be adopted, | where spray-    |     |     |     |     |
cooled cold plates are used for high-density compute racks. A. MODELINGAPPROACHES
Inthissetup,liquidcoolantremovesheatdirectlyatthechip Modelingapproachesarefundamentaltotheanalysisofgrid-
levelandtransfersittoacoolingwatertankandsubsequently integrated data centers, as they provide mathematical and
to the cooling tower. Air conditioning systems can be used computationalrepresentationsofelectricalcomponents,con-
for lower heat density racks, which circulate conditioned air trol systems, and their interactions to analyze, predict, and
throughtheservers.Achilled-waterstoragesystem,powered optimize system behavior under a wide range of operating
by an absorption cycle comprising of an absorber, generator, and disturbance conditions [45]. In this context, modeling
evaporator,andcondenser,furtherenhancescoolingflexibility enablesthesystematicstudyofthetightlycoupleddynamics
and stabilizes thermal performance during fluctuating work- betweendatacenterserverworkloads,powersupplydistribu-
loads.Coordinatedoperationofthesesubsystemscanenable tion infrastructures, cooling systems, energy storage, on-site
efficient heat rejection and maintains reliable temperature generation, and the external power grid. By capturing essen-
control under varying computational conditions. This can be tialelectricalandoperationalcharacteristicswhilesimplifying
| 1090 |     |     |     |     |     |     | VOLUME7,2026 |
| ---- | --- | --- | --- | --- | --- | --- | ------------ |

FIGURE9. Modelingapproachesfordatacenters.
noncritical details, these models can support the investiga- Researchhighlightsthat,unlikestandardizedmodelingframe-
tionofkeyphenomenasuchaspowerflow,stability,control, works,thesemodelsexplicitlyenablegranularexplorationof
reliability, and flexibility across different time scales [46]. server behavior, power electronics, cooling strategies, or en-
Therefore,thelevelofmodelfidelityshouldbeselectedbased ergymanagementalgorithms,allowinginvestigationofnovel
ontheintendedapplication,strikingabalancebetweenaccu- datacentergridinteractionparadigms[52].Anotherresearch
racyandcomputationalefficiency[47],[48]. proposed a modular toolbox that allows building data cen-
This subsection reviews the main modeling approaches termodels ofanyscaleandconfiguration usingstandardized
showninFig.9forgrid-integrateddatacenters,rangingfrom buildingblocks[53].Thesemodelsofferdetailedrepresenta-
detailed device-level models for component and transient tions and are more precise than generic ones. However, they
analysis to simplified system-level and grid-interface models aremorecomplextotune,resultinginslowersimulationper-
usedforstabilityandlarge-scalepowersystemstudies. formance.Consequently,whileuser-definedmodelsarepow-
|     |     |     |     |     | erful tools | for innovation-driven | research, | their applicability |     |
| --- | --- | --- | --- | --- | ----------- | --------------------- | --------- | ------------------- | --- |
1) GENERICMODELS tobroadersystemstudiesrequirescarefuldocumentationand
Generic models are widely utilized for power system mod- validationagainstreal-worlddata.
| eling, particularly | as reduced-order      |             | models | in transmission |       |     |     |     |     |
| ------------------- | --------------------- | ----------- | ------ | --------------- | ----- | --- | --- | --- | --- |
| planning            | that involves dynamic | components. |        | These models    |       |     |     |     |     |
| are better          | suited for long-term  | planning    | and    | high-level      | flex- |     |     |     |     |
3) PERFORMANCEMODELS
ibility assessments than for detailed stability or protection Performance models aim to establish quantitative relation-
| analysis. | This approach | can also | effectively | represent | grid- |     |     |     |     |
| --------- | ------------- | -------- | ----------- | --------- | ----- | --- | --- | --- | --- |
shipsbetweenelectricaloperatingconditionsanddatacenter
integrated data centers by focusing on aggregated power service-levelmetrics,suchasthroughput,latency,orcompu-
demand, energy flows, and flexibility characteristics, while tational efficiency under different load characteristics [54].
oftenneglectingmodelfidelityandspecificmanufacturerde-
|     |     |     |     |     | Within this | context, Kühn [55] | developed | energy | efficiency |
| --- | --- | --- | --- | --- | ----------- | ------------------ | --------- | ------ | ---------- |
tails[49].Forexample,Ounifietal.[50]introduceageneric performance models that relate server operations to SLAs,
datacentermetamodelcapableofrepresentingheterogeneous while Schlitt and Nebel [56] proposed the load-dependent
infrastructure characteristics. Such an abstract model ap- energyefficiencymetric,integratingutilization,performance,
proach allows for scalable analysis of system-wide impacts, andpowermodelstoprovidedetailedefficiencycharacteriza-
| including | grid planning, | capacity adequacy, |     | and demand | re- |     |     |     |     |
| --------- | -------------- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- |
tion.Thesestudiesdemonstratethatsuchmodelscanfacilitate
sponse potential under varying operating conditions. While theintegrationofworkloadcharacterizationwithpowercon-
generic models provide computational efficiency and con- sumption,enablingtheevaluationofhowgrideventsorpower
ceptual clarity, their reliance on lumped parameters limits constraints affect computational performance. For grid inte-
theirabilitytocapturedetaileddynamicinteractionsbetween grationstudies,performancemodelsareusefulforevaluating
| internal subsystems, | especially | during | rapid | disturbances | or              |            |              |           |       |
| -------------------- | ---------- | ------ | ----- | ------------ | --------------- | ---------- | ------------ | --------- | ----- |
|                      |            |        |       |              | demand response | strategies | by balancing | temporary | power |
control-driventransients[51]. modulation with quality-of-service requirements [57]. Their
fastexecutionandlowdatarequirementsmakethemsuitable
2) USER-DEFINEDMODELS forearly-stageorhigh-levelanalyses.However,theirreliance
User-defined models provide researchers with the flexibility on empirical relationships limits accuracy under unforeseen
to tailor system representations according to specific archi- conditions, and they lack the fidelity needed to capture elec-
tectural choices, control strategies, or research objectives. tricaltransientsorconverter-levelinteractions.
| VOLUME7,2026 |     |     |     |     |     |     |     |     | 1091 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
| 4) COMPONENT-LEVELMODELS |     |     |     |     |     |     | 7) EMTMODELS |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Component-level models represent individual physical el- EMT models provide a detailed time-domain representation
ements within the data center, including servers, PDUs, of electrical systems, capturing fast dynamics, switching ac-
uninterruptible power supplies, converters, cooling equip- tions, and nonlinear control behavior [66]. Therefore, in the
ment,andESSs[54].Bymodelingtheelectricalandthermal context of grid-integrated data centers, EMT models are
characteristics of each component, these approaches enable essential for analyzing converter-dominated interfaces, pro-
detailedinvestigationofinternalpowerflowsandlossmecha- tection coordination, and system response to faults or abrupt
nisms[58].Thismodelingapproachisutilizedin[59]and[60] disturbances [67]. These models enable accurate assessment
for reliability studies, failure mode analysis, and detailed of high-frequency interactions between data center power
control design, where it is essential to understand the inter- electronics and the grid, which are increasingly important
actions between specific components. Although component- as data centers adopt advanced inverter-based architectures.
level modeling provides high fidelity and physical insight, Despitetheirhighfidelity,EMTsimulationsarecomputation-
its application to large-scale systems can be computationally ally demanding and typically limited to small subsystems or
intensive,oftennecessitatingmodelreductionoraggregation short simulation windows, restricting their use in large-scale
techniqueswhenstudyinginteractionswiththegrid. orlong-termstudies[68].
8) HILMODELS
5) PHASOR-DOMAINMODELS
|                       |              |           |          |          |            |          | HIL modeling   |           | integrates         | physical | hardware       |           | with | real-time  |
| --------------------- | ------------ | --------- | -------- | -------- | ---------- | -------- | -------------- | --------- | ------------------ | -------- | -------------- | --------- | ---- | ---------- |
| Phasor-domain         | models       | represent |          | voltages | and        | currents | using          |           |                    |          |                |           |      |            |
|                       |              |           |          |          |            |          | simulation     | platforms | to                 | assess   | system         | behavior  | in   | controlled |
| fundamental-frequency |              |           | phasors, | thereby  | capturing  | steady-  |                |           |                    |          |                |           |      |            |
|                       |              |           |          |          |            |          | and repeatable |           | test environments. |          | By             | operating | the  | hardware   |
| state and             | slow dynamic |           | behavior | while    | neglecting |          | high-          |           |                    |          |                |           |      |            |
|                       |              |           |          |          |            |          | and simulator  |           | in a closed-loop   |          | configuration, |           | this | approach   |
frequencyswitchingphenomena.Thesemodelsareacorner-
|          |              |       |        |          |     |          | enhances        | the | realism of | system       | evaluation |      | and | enables de-  |
| -------- | ------------ | ----- | ------ | -------- | --- | -------- | --------------- | --- | ---------- | ------------ | ---------- | ---- | --- | ------------ |
| stone of | conventional | power | system | analysis |     | and have | been            |     |            |              |            |      |     |              |
|          |              |       |        |          |     |          | tailed analysis |     | of complex | interactions |            | that | are | difficult to |
increasinglyappliedtostudythegridimpactoflargedatacen-
|                    |           |       |               |             |     |           | capture     | using  | purely software-based |          |     | simulations |     | [69]. Sun  |
| ------------------ | --------- | ----- | ------------- | ----------- | --- | --------- | ----------- | ------ | --------------------- | -------- | --- | ----------- | --- | ---------- |
| ters, particularly | in        | terms | of voltage    | regulation, |     | power     | flow,       |        |                       |          |     |             |     |            |
|                    |           |       |               |             |     |           | et al. [70] | employ | a HIL                 | approach | by  | integrating |     | a physical |
| and frequency      | stability |       | [61]. Several | studies,    |     | including | [59]        |        |                       |          |     |             |     |            |
converter-basedemulatorwithareal-timesimulatedmodelof
and[62],adoptphasor-domainmodelsforgrid-integrateddata
|     |     |     |     |     |     |     | the data | center | power distribution |     | system. |     | Given | the grow- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------------------ | --- | ------- | --- | ----- | --------- |
centerstudiestosupportefficientlarge-scalenetworksimula-
|               |           |          |     |              |     |            | ing need  | for dynamic    | data       | center     | models,          |                      | this | approach is |
| ------------- | --------- | -------- | --- | ------------ | --- | ---------- | --------- | -------------- | ---------- | ---------- | ---------------- | -------------------- | ---- | ----------- |
| tions, making | them      | suitable | for | contingency  |     | assessment | and       |                |            |            |                  |                      |      |             |
|               |           |          |     |              |     |            | essential | for validating |            | controller | implementations, |                      |      | inverter    |
| operational   | planning. | However, |     | the inherent |     | assumption | of        |                |            |            |                  |                      |      |             |
|               |           |          |     |              |     |            | hardware, | and            | protection | schemes    | under            | realisticgriddistur- |      |             |
sinusoidalsteady-stateoperationlimitstheirabilitytocapture
|              |               |            |            |      |           |            | bances.        | HIL modeling |            | bridges   | the   | gap between  |       | simulation  |
| ------------ | ------------- | ---------- | ---------- | ---- | --------- | ---------- | -------------- | ------------ | ---------- | --------- | ----- | ------------ | ----- | ----------- |
| fast control | interactions, |            | harmonics, |      | and EMTs  | associated |                |              |            |           |       |              |       |             |
|              |               |            |            |      |           |            | studies        | and field    | deployment |           | [71]. | However,     | their | reliance    |
| with power   | electronic    | interfaces |            | [63] | prevalent | in AI      | data           |              |            |           |       |              |       |             |
|              |               |            |            |      |           |            | on specialized |              | equipment, | real-time |       | constraints, |       | and limited |
centers.
|     |     |     |     |     |     |     | scalability | confines | their | useprimarilytovalidation |     |     |     | and pro- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ----- | ------------------------ | --- | --- | --- | -------- |
totypingratherthanlarge-systemanalysis.
6) POSITIVE-SEQUENCEMODELS
Positive-sequence models represent three-phase power sys- 9) SWITCHINGMODELS
tems using only the balanced fundamental-frequency com- Switchingmodelsrepresentthebehaviorofpowerelectronic
ponent, assuming symmetrical operating conditions and ne- switching devices, together with their associated pulsewidth
glecting unbalanced and harmonic effects. This modeling modulation (PWM) control schemes and gating circuits. By
approach is used for longer time scales, particularly for fre- modeling the generation of sinusoidal voltage and current
quency response, and system-level stability and load-flow waveforms through high-frequency switching and embedded
studies [64]. By significantly reducing model complexity, controlstructures,thesemodelscapturedetailedconverterdy-
positive-sequence representations enable efficient simulation namics,harmonicdistortion,andcomplexcontrolinteractions
ofextensivenetworkswithhighdatacenterpenetration,mak- withthesurroundingpowersystem[72].Withthechallenges,
ingthemsuitableforlong-durationandwide-areastudies,as such as frequency coupling and low-frequency oscillations,
used in [54] for studying UPS performance in a data center. posed by AI data centers, switching models are essential for
However, considering the underlying assumptions of bal- investigating issues such as harmonic distortion, converter-
ancedoperationlimittheirapplicabilityinscenariosinvolving inducedinstabilities,andhigh-frequencyinteractionswiththe
asymmetricalfaults,unbalancedloading,orpower-electronic- grid [73]. These models provide the highest level of electri-
induced harmonics. Consequently, positive-sequence models cal fidelity and are often used as reference benchmarks for
aregenerallyunsuitablefordetailedpowerquality,protection, validating reduced-order or average models. However, their
or electromagnetic interaction studies involving data center extreme computational complexity restricts their application
infrastructure[65]. tosmall-scalesystemsorshort-durationsimulations,making
| 1092 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

themimpracticalforlargenetworksorlong-termoperational the choice solely depends on the required fidelity, compu-
studies[72]. tational complexity, simulation time scale, and the intended
|     |     |     |     |     |     |     | grid integration |     | study. | High-fidelity |     | models | provide | detailed |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------------- | --- | ------ | ------- | -------- |
10) AVERAGEMODELS dynamicandtransientbehavioratthecomponentlevel,while
|         |        |          |                    |     |     |          | system-level | models |     | enable | efficient | large-scale |     | power sys- |
| ------- | ------ | -------- | ------------------ | --- | --- | -------- | ------------ | ------ | --- | ------ | --------- | ----------- | --- | ---------- |
| Average | models | simplify | the representation |     |     | of power | elec-        |        |     |        |           |             |     |            |
temanalysisandcontrolevaluation.Acomparativesummary
| tronic converters |     | by averaging |     | switching | behavior |     | over a   |          |             |     |           |       |          |        |
| ----------------- | --- | ------------ | --- | --------- | -------- | --- | -------- | -------- | ----------- | --- | --------- | ----- | -------- | ------ |
|                   |     |              |     |           |          |     | of these | modeling | approaches, |     | including | their | fidelity | level, |
switchingperiod,therebyretainingessentialdynamiccharac-
simulationtime-step,advantages,andlimitations,ispresented
teristicswhileeliminatinghigh-frequencycomponents.These
|        |              |          |     |            |           |     | in Table | 4. Furthermore, |       | Fig.  | 10          | presents   | a model-selection |             |
| ------ | ------------ | -------- | --- | ---------- | --------- | --- | -------- | --------------- | ----- | ----- | ----------- | ---------- | ----------------- | ----------- |
| models | are commonly | utilized |     | in dynamic | stability | and | con-     |                 |       |       |             |            |                   |             |
|        |              |          |     |            |           |     | workflow | that            | links | study | objectives, | simulation |                   | timescales, |
trolstudiesofgrid-connectedinverter-basedresources,where
requiredparameters,andvalidationrequirementstothemost
| switching-level |     | detail is | less [72], | which | now | includes | AI  |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ---------- | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
data centers. Average modeling significantly reduces com- appropriatemodelingapproach,therebyprovidingapractical
|            |        |          |     |     |              |         | guideline | for | selecting | suitable | models | for | planning, | opera- |
| ---------- | ------ | -------- | --- | --- | ------------ | ------- | --------- | --- | --------- | -------- | ------ | --- | --------- | ------ |
| putational | burden | compared | to  | EMT | or switching | models, |           |     |           |          |        |     |           |        |
tional,stability,andEMTstudiesoflarge-scaledatacenters.
enablinglongersimulationtimesandlargersystemrepresen-
| tations. | Nevertheless, | the | exclusion | of  | switching | harmonics |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
andfasttransientslimitstheirapplicabilityinstudiesinvolv- B. CONVERTER-DRIVENPHENOMENA
ing electromagnetic compatibility, protection, or harmonic Theinteractionbetweenconverter-basedloadsandthepower
|     |     |     |     |     |     |     | grid introduces |     | a range | of  | dynamic | phenomena |     | that can |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | --- | ------- | --------- | --- | -------- |
interactionanalysis[74].
|     |     |     |     |     |     |     | significantly   | influence |           | power | quality,   | system   | stability, | and |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | --------- | ----- | ---------- | -------- | ---------- | --- |
|     |     |     |     |     |     |     | electromagnetic |           | behavior. |       | Therefore, | accurate | modeling   | of  |
11) IMPEDANCE-BASEDMODELS
converter-driveninteractionsisessentialforanalyzingsystem
Theimpedance-basedmodelingapproachisgainingpopular-
|                  |                |            |             |           |            |              | stability, | assessing | grid | impacts, |     | and developing |           | mitigation |
| ---------------- | -------------- | ---------- | ----------- | --------- | ---------- | ------------ | ---------- | --------- | ---- | -------- | --- | -------------- | --------- | ---------- |
| ity for          | inverter-based | electrical |             | networks, | such       | as inverter- |            |           |      |          |     |                |           |            |
|                  |                |            |             |           |            |              | strategies | under     | both | normal   | and | weak-grid      | operating | condi-     |
| based resources, |                | dominant   | electricity |           | grids, and | microgrids.  |            |           |      |          |     |                |           |            |
tions.
Itisafrequency-domain-basedtechniqueusedtoanalyzeres-
| onance | stability | issues in | electrical | networks. |     | In impedance- |     |     |     |     |     |     |     |     |
| ------ | --------- | --------- | ---------- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1) HARMONICDISTORTION
| based modeling, |     | loads are | represented |     | by input | impedance, |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ----------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
while sources are represented by output impedance, and the The nonsinusoidal currents drawn by data center power
|     |     |     |     |     |     |     | electronics | constitute |     | one | of the | most dominant |     | forms of |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --- | ------ | ------------- | --- | -------- |
ratiobetweenthesourceandloadimpedancemustsatisfythe
converter-gridinteraction.ModernserverPSUstypicallyem-
Nyquiststabilitycriterion.Thistechniquehasbeenemployed
to analyze the resonance incident in a data center. The study ploy single-phase boost or dual-boost PFC converters at the
front-endstage,whoseswitching-cycleaveragedinductorcur-
| has developed |     | an impedance-based |     | model | for | the PSU | of a |     |     |     |     |     |     |     |
| ------------- | --- | ------------------ | --- | ----- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
serverandapplied theNyquiststabilitycriterionforstability rentdynamicscanbeexpressedasfollows:
analysis[75],[76].Thus,thismodelingapproach canbeuti- di v −(1−d (cid:3) )v
|     |     |     |     |     |     |     |     |     | L   | = a |     | DC  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lized to analyze the resonance-based stability issues in data (1)
|          |             |          |     |         |        |          |      |     | dt  |     | L   |         |     |     |
| -------- | ----------- | -------- | --- | ------- | ------ | -------- | ---- | --- | --- | --- | --- | ------- | --- | --- |
| centers, | as recently | employed |     | by Ruan | et al. | [77] for | data |     |     |     |     |         |     |     |
|          |             |          |     |         |        |          | v    |     |     |     |     | (cid:3) |     |     |
centercontrolagainstsubsynchronousresonance. where a is the AC input voltage, d is the off-time duty
|     |     |     |     |     |     |     | ratio,Lrepresentsinductance,andv |     |     |     |     | istheDC-linkvoltage. |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- |
DC
|                       |                |     |             |     |                |     | The bilinear | term      | (1−d     | (cid:3) )v | introduces | nonlinear |         | behavior |
| --------------------- | -------------- | --- | ----------- | --- | -------------- | --- | ------------ | --------- | -------- | ---------- | ---------- | --------- | ------- | -------- |
| 12) DATA-DRIVENMODELS |                |     |             |     |                |     |              |           |          |            | DC         |           |         |          |
|                       |                |     |             |     |                |     | into the     | converter | dynamics |            | [79].      | For this  | reason, | even un- |
| Data-driven           | modelsleverage |     | measurement |     | dataandmachine |     |              |           |          |            |            |           |         |          |
deridealsinusoidalsupplyconditions,switchingactionsand
| learning | techniques | to capture |     | the dynamic | behavior |     | of data |     |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --- | ----------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
centerswithoutrequiringdetailedphysicalrepresentationsof imperfect current tracking generate harmonic components at
|          |             |                     |          |              |     |               | odd multiples |            | of the | fundamental |              | frequency. | In   | large-scale |
| -------- | ----------- | ------------------- | -------- | ------------ | --- | ------------- | ------------- | ---------- | ------ | ----------- | ------------ | ---------- | ---- | ----------- |
| internal | components. | By                  | learning | input–output |     | relationships |               |            |        |             |              |            |      |             |
|          |             |                     |          |              |     |               | data centers  | containing |        | tens        | of thousands | of         | PSUs | operating   |
| directly | from        | data, a data-driven |          | approach     | is  | used          | in [78]       |            |        |             |              |            |      |             |
simultaneously,theseharmoniccurrentsaggregatethroughout
| to simulate | a   | data center | cooling | system | and | predict | its re- |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | ------- | ------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
theinternaldistributionhierarchyandpropagatebacktoward
sponseshoursintothefuture.Suchmodelsarebeneficialfor
thePCC.TheresultingharmonicvoltagedistortionatthePCC
real-timecontrol,forecasting,andsystem-levelstudieswhere
canbeapproximatedas
| detailed                                               | equipment | parameters |     | are unavailable. |     | Despite | their |     |     |     |        |     |     |     |
| ------------------------------------------------------ | --------- | ---------- | --- | ---------------- | --- | ------- | ----- | --- | --- | --- | ------ | --- | --- | --- |
| flexibilityandlowercomputationaldemand[72],data-driven |           |            |     |                  |     |         |       |     |     | =I  |        | (ω  |     |     |
|                                                        |           |            |     |                  |     |         |       |     |     | V   | DC,h Z | )   |     | (2) |
|                                                        |           |            |     |                  |     |         |       |     |     | h   |        | h h |     |     |
modelsoftensufferfromlimitedinterpretability,reducedgen-
eralizationoutsidetheoperatingconditionsrepresentedinthe whereI DC,h representstheaggregatedharmoniccurrentathar-
training data, and data scarcity due to confidentiality con- monicfrequencyω ,andZ (ω )denotesthegridimpedance
|     |     |     |     |     |     |     |     |     | h   |     | h h |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
straints. Moreover, their performance is highly dependent on at that frequency [19]. Although reactive power panels and
dataquality[72]. line inductors provide partial attenuation of high-frequency
The reviewed modeling approaches demonstrate that no distortion, these passive elements also contribute additional
single modeling approach is suitable for all applications, as inductive impedance capable of interacting with converter
| VOLUME7,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 1093 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
FIGURE10. Flowchartforselectingdatacentermodelsbasedonstudyobjectives,timescales,andparameters.
1094 VOLUME7,2026

TABLE4. SummaryofAdvantagesandLimitationsofDataCenterModelingApproaches
filter capacitance [76]. A more severe power quality is- the interacting network inductance and distributed converter
sue emerges when the equivalent distributed capacitance of capacitance. AI data centers further intensify power quality
large converter populations resonates with the inductive grid challenges through rapid and stochastic load variations asso-
impedance. Since server-level PFC filters exhibit a predom- ciated with AI intensive workloads. Fast transitions between
inantly capacitive characteristic, the combined impedance compute and communication phases can produce subsecond
betweenthedistributedcapacitanceC andinductivecompo- powerfluctuationsthataggregateintolargefacility-levelramp
p
nentsL becomes events, causing voltage flicker, voltage sags, and transient
s
harmonicamplificationatthePCC[19].
jω L
Z = h s . (3)
h 1−ω2LC
h s p
2) RESONANCE
Asthedenominatorapproacheszero,resonanceconditions Resonance-inducedoscillationsarisefrominteractionsamong
amplify even relatively small harmonic currents into signif- converter control systems, passive network elements, and
icant voltage distortion [19]. This phenomenon may result grid impedance. These interactions can produce instabil-
in transformer overheating, increased system losses, insula- ity in both low- and high-frequency regions, leading to
tion stress, and wideband oscillations spanning frequencies harmonic amplification, oscillatory behavior, and degraded
from several hertz to multiple kilohertz. Unlike conventional system performance. Such phenomena are commonly
integer-order harmonics, these distortions are determined by analyzed using impedance-based stability methods, which
VOLUME7,2026 1095

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
evaluate the dynamic relationship between source and load frameworkaggregatesimpedancecontributionsacrossthehi-
impedance across different frequency ranges. The medium- erarchicaldistributionstructure
⎡ ⎤
frequencyPFCimpedancemodelis
(cid:5)6 (cid:8)i
Z (s)= sL+V DC H c (s) (4) Z s (s)=Z 0 (s)+ ⎣ Z i (s) N j ⎦ (10)
am 1+GV H (s) i=1 j=1
DC c
where N is the number of sublines powered from the line
where H (s) denotes the current controller, G is the con- j
c designatedbyimpedanceZ , j =1,2,...,6.Theimpedance
verter forward gain, and V is the DC-bus voltage [75]. j
DC
accumulation extends from rack-level distribution through
Low-frequencyinstabilityhasbeenobservedinseveralMeta
reactive power panels, switchboards, transformers, and up-
datacenters,whereoscillationsnear11Hzwereaccompanied
stream substations. Stability assessment can then be per-
by strong sideband components at 49 and 71 Hz around the
formed using the Nyquist criterion applied to the loop gain
60-Hz fundamental frequency [75]. In this frequency range,
formedbytheconverteradmittanceandtheequivalentsource
(4) is unable to accurately reproduce this phenomenon be-
impedance.
cause it assumes a constant DC-link voltage and neglects
Theseequationsareimportantfortreatingconverter-driven
DC-bus dynamics. In practice, perturbations at the AC ter-
resonance phenomena for large-scale data centers because
minal interact with the DC-link control loop through the
their highly concentrated power electronic infrastructure
bilinearcouplingtermintroducedin(1),producingadditional
causes complex interactions between converters, network
frequency-coupled current components [79]. To capture this
impedance, and harmonic currents that can destabilize both
behavior,theconvertersmall-signalmodelmustincludethree
thefacilitydistributionsystemandtheutilitygrid.
coupledtransferadmittances
Y (s)= iˆ a (s) (5) 3) STABILITYINWEAKGRID
a vˆ (s) Data centers exhibit largely passive impedance characteris-
a
tics,dominatedbytightlyregulatedswitch-modePSUs,UPS
iˆ (s− j2ω ) converters, and battery interfaces whose control loops can
Y c−2 (s)= a
vˆ (s)
1 (6) introduce negative damping and fast electromagnetic inter-
a actions [75], [76]. As a result, voltage stability at the PCC
becomes highly sensitive to rapid active and reactive power
iˆ (s+ j2ω ) fluctuations associated with AI workloads. The voltage vari-
Y c+2 (s)= a
vˆ (s)
1 (7)
ationatthePCCcanberepresentedusingvoltagesensitivity
a
relationshipsas
whereiˆ isthecurrentresponse,Y (s)denotestheinputadmit-
a a
tanceofthePFCconverterunderidealAC-sourceconditions, (cid:4)V i =S VP,i (cid:4)P i +S VQ,i (cid:4)Q i (11)
andY c−2 (s) andY c+2 (s) represent the associated transfer ad- whereS VP,i andS VQ,i representthevoltagesensitivityfactors
mittances [75]. At higher frequencies, the converter digital associatedwithactiveandreactivepowervariations[81].For
control delays become a dominant source of instability. For a radial connection, the PCC voltage deviation is approxi-
converters employing trailing-edge modulation, the effective mately
controldelaycanbeapproximatedas
(cid:2) (cid:3) (cid:4) |V |≈|V |− R line P L,DC +X line Q L,DC (12)
T =2f 2
1
f1 T 1+
d(τ)
+n dτ (8)
PCC g |V
PCC
|
d 1 s
2 where the active and reactive power consumed by the data
0
whereT istheswitchingperiod,2f isthesecondharmonic center are represented as P L,DC and Q L,DC , respectively, and
s 1 |V |isthevoltagemagnitudeofthesource[19].Thisindicates
frequency, d is the duty ratio of the switch, and n represents g
that under weak-grid conditions, where network impedance
additional processing cycles [75]. Incorporating this delay
is high, significant voltage drops can occur during rapid
intotheconverterimpedancemodel(4)yields
loadchanges,leadingtovoltageinstability.Inaddition,these
Z (s)=
sL+V
DC
e −sTdH
c
(s)
. (9)
load transients can excite frequency and rotor-angle dynam-
ah 1+GV
DC
e−sTdH
c
(s) ics across the wider power system. When large-scale AI
workloadsstart,stop,ortransfertoUPSoperationduringdis-
These interactions can produce high-frequency resonance
turbances,theresultingpowerimbalancepropagatesthrough
andnegativedamping,particularlyinsystemswithtightlyreg-
nearby synchronous generators according to theswing equa-
ulatedparallelconverters[80].Inlargedatacenters,instability
tion
mechanisms are not confined to the PCC because the inter-
(cid:11) (cid:12)
d
nal facility impedance may substantially exceed the external ((cid:4)ω)= K P ref −P L,DC (t)
dt
utilityimpedance[76].Consequently,oscillatorybehaviorcan (cid:13) (cid:14)
originatewithintheinternalradialdistributionnetworkitself. + 3K|E g ||E| sin(δ)−α(cid:4)ω (13)
To represent this behavior, the equivalent source impedance X
1096 VOLUME7,2026

where K is the generator inertia constant, α is the damping Several studies have demonstrated that CPU power for
(cid:4)ω
coefficient, is the frequency deviation, P ref is the three- fixed-function accelerators can be modeled using a register
phase generator reference power, δ is the rotor angle, E is transfer level (RTL) regression-based approach [85], [86],
g
the internal generator voltage magnitude, E is the bus/grid [87]. This approach supports the development of higher res-
voltagemagnitude,andX representstheequivalentreactance olution power models. Recent advances in machine learning
between the generator and the grid. The term (3|E ||E|/X) have enabled more accurate power consumption modeling
g
represents the electrical power transfer interaction between techniques for CPU, with predictive modeling considered
the generator and the connected power system [19]. Accord- as an alternative to cycle-accurate simulation [88]. In [89],
ingly,ifthedatacenterloadchangesfasterthanconventional advanced machine learning methods utilizing deep neural
generatorscanrespond,frequencydeviationsandrotor-angle networks have shown the ability to achieve highly accurate
oscillations may become severe under weak-grid conditions RTL power estimation using large training datasets. More
withlowshort-circuitratio[82]. recently, Kumar et al. [90] proposed a machine-learning-
|     |     |     |     |     |     |     | based | microarchitecture-level |          |        | power | modeling | approach, | us-        |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------------------- | -------- | ------ | ----- | -------- | --------- | ---------- |
|     |     |     |     |     |     |     | ing   | high-level              | activity | traces | and a | small    | set of    | gate-level |
V. MODELINGOFCRITICALCOMPONENTSOFADATA
|     |     |     |     |     |     |     | simulations. |     | Cycle-accurate |     | subcomponent |     | models | are hier- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------- | --- | ------------ | --- | ------ | --------- |
CENTER
archicallycomposedinthestudytoestimatefull-CPUpower,
| Accurate | modeling | of  | critical | data | center components |     | is        |     |                |      |          |       |     |           |
| -------- | -------- | --- | -------- | ---- | ----------------- | --- | --------- | --- | -------------- | ---- | -------- | ----- | --- | --------- |
|          |          |     |          |      |                   |     | achieving |     | less than 3.6% | mean | absolute | error | for | cycle-by- |
essentialforanalyzingtheirpowerconsumptionbehavior,dy-
cyclepowerofreal-worldapplications.
namicresponse,andinteractionwiththeelectricalgrid.Data
GPUpowerconsumptionrequiresadifferentmodelingap-
| centers     | consist     | of interconnected |       | electrical, | computational, |     |        |          |        |     |          |        |               |     |
| ----------- | ----------- | ----------------- | ----- | ----------- | -------------- | --- | ------ | -------- | ------ | --- | -------- | ------ | ------------- | --- |
|             |             |                   |       |             |                |     | proach | compared | to CPU | due | to their | unique | architectural |     |
| and thermal | subsystems, |                   | whose | combined    | operation      |     | deter- |          |        |     |          |        |               |     |
andcomputationalcharacteristics[91].Multiplestudieshave
minesthefacility’sflexibilityandstabilitysupportcapability.
|            |                |     |          |     |                |     | been | published   | to support     | this | claim; | for      | instance, | a review   |
| ---------- | -------------- | --- | -------- | --- | -------------- | --- | ---- | ----------- | -------------- | ---- | ------ | -------- | --------- | ---------- |
| Therefore, | representative |     | modeling | of  | key components |     | such |             |                |      |        |          |           |            |
|            |                |     |          |     |                |     | on   | statistical | power modeling |      | by     | Chitkara | [92]      | highlights |
asCPU/GPUloads,UPS,coolingsystems,ESSs,andon-site
|           |            |     |           |     |                  |     | that | GPUs | have distinct | power | dynamics | due | heterogeneous |     |
| --------- | ---------- | --- | --------- | --- | ---------------- | --- | ---- | ---- | ------------- | ----- | -------- | --- | ------------- | --- |
| renewable | generation | is  | necessary | for | grid integration |     | and  |      |               |       |          |     |               |     |
computing.In2021,Kandiah[93]developedanAccelWattch
powersystemstabilitystudies.Thefollowingsectionreviews
|     |     |     |     |     |     |     | specialized |     | GPU power | model | that | resolves | long-standing |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ----- | ---- | -------- | ------------- | --- |
themodelingconsiderationsandcharacteristicsofthesecriti-
modelingchallenges,specificallyaddressingGPUs’staticand
calcomponents.
dynamicpowerconsumptionpatterns.Alavanietal.[94]fur-
|     |     |     |     |     |     |     | ther | validated | this by | developing | machine |     | learning | models |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ------- | ---------- | ------- | --- | -------- | ------ |
A. CENTRALPROCESSINGUNIT/GRAPHICSPROCESSING that capture GPU-specific power consumption relationships,
| UNIT |     |     |     |     |     |     | achievinganimpressiveR2valueof0.9646fortheVoltaarchi- |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
tecture.DuetotherapidlyevolvingnatureofAItechnologies,
Powerconsumptionmodelshavelongbeendevelopedtoeval-
uate energy management potential and predict power usage LiandLi[95]classifiedtwodifferentworkloads:trainingand
at both server and data center levels. In 2020, Jin et al. [83] inference. They then provided a formal mathematical model
presentedacomprehensivereviewof47modelsthatevaluate foreachoftheworkloadpowerconsumptionin(15)and(16)
| CPU power | consumption |     | in data | centers. | The | study catego- |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:5)N
rizes these models into three main types: additive models, (t)=P + α (t)+(cid:7)(t)
|     |     |     |     |     |     |     |     |     | P train | base |     | i f i |     | (15) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | --- | ----- | --- | ---- |
baseline-plus-active(BA)models,andvariousformula-based
i=1
| approaches. | The | BA models |     | are further | divided | into | four |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ----------- | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
categories:linear,powerfunction,nonlinear,andpolynomial
(cid:5)M
| forms, which | are         | represented | in  | (14),   | where P    | denotes | the    |     |         |      |     |       |     |      |
| ------------ | ----------- | ----------- | --- | ------- | ---------- | ------- | ------ | --- | ------- | ---- | --- | ----- | --- | ---- |
|              |             |             |     |         | s,t        |         |        |     | P (t)=P |      | + P | (t)·R | (t) | (16) |
|              |             |             |     |         |            |         |        |     | inf     | idle |     | k     | k   |      |
| server power | consumption |             | at  | time t, | P idle and | P max   | repre- |     |         |      |     |       |     |      |
k=1
| sent the | idle and | maximum | power | levels, | respectively, |     | u s,t is |     |     |     |     |     |     |     |
| -------- | -------- | ------- | ----- | ------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
the server utilization, and a , a , b , b , b , b , and m are where P denotes the baseline power consumption, typ-
|     |     |     | 1   | 2 1 | 2 3 | 4   |     | base |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
modelcoefficientsdefiningthepower–utilizationrelationship. ically in the range of 60%–70% of the peak load. The
Buildinguponthis,AnandMa[84]evaluatedtheaccuracyof summationtermα representsthecontributionofpowervari-
i
|     |     |     |     |     |     |     | ations | associated | with | different | training |     | phases, | with each |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ---- | --------- | -------- | --- | ------- | --------- |
BAmodelingapproachesandreportedthatpolynomial-based
models generally achieve better performance compared to coefficient reflecting the relative intensity of the correspond-
otherformulations ing phase. The function f (t) describes the temporal profile
i
ordurationofeachphase,whileε(t)isastochastictermthat
⎧
⎪⎪⎪⎨ P +(P −P )u s,t captures minor power fluctuations arising from microbatch-
|     | idle  |       | max   | idle     |     |          |       |               |                   |           |              |           |             |               |
| --- | ----- | ----- | ----- | -------- | --- | -------- | ----- | ------------- | ----------------- | --------- | ------------ | --------- | ----------- | ------------- |
|     |       |       |       |          |     |          | i n g | e f f e c t s | o r a s y n c h r | o n o u s | b ac k g r o | u n d t a | s k s . F o | r ( 1 6 ) , P |
|     | P     | + a   | u 2   |          |     |          |       |               |                   |           |              |           |             | i d l e       |
| P   | = i d | l e 1 | s , t | (cid:11) |     | (cid:12) | (14)  |               |                   |           |              |           |             | ·             |
s,t ⎪⎪⎪⎩ + −P −u m r ep r e s e n t s t h e i d l e p o w e r d r a w , a n d t h e p r o d u c t P k ( t ) R k ( t )
|     | P   | (P  | m a x | ) 2u | s,t ,t |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i d l e idle s m o d e l s t h e p ow e r d e m a n d a n d a r r i v a l p at t e r n a s s o c i a t e d w i t h
|              |     | +b      | +b  | 2 +b | 3 .    |     |                       |     |     |     |     |     |     |      |
| ------------ | --- | ------- | --- | ---- | ------ | --- | --------------------- | --- | --- | --- | --- | --- | --- | ---- |
|              | b 1 | 2 u s,t | 3   | u ,t | 4 u ,t |     |                       |     |     |     |     |     |     |      |
|              |     |         |     | s    | s      |     | aspecificrequesttype. |     |     |     |     |     |     |      |
| VOLUME7,2026 |     |         |     |      |        |     |                       |     |     |     |     |     |     | 1097 |

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
TABLE5. ComparativeSummaryofUPSTopologiesUsedinGrid-IntegratedDatacenters[101]
|     |     |     |     |     |     |     | disturbances.   | Beyond | the                | functional     | classification, |                    |                   | UPS sys- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ------------------ | -------------- | --------------- | ------------------ | ----------------- | -------- |
|     |     |     |     |     |     |     | tems can        | also   | be distinguished   |                | based           | on                 | their topologies. |          |
|     |     |     |     |     |     |     | According       | to     | [101], power       | converter      |                 | topologies         |                   | for UPS  |
|     |     |     |     |     |     |     | systems         | can be | classified         | into           | three           | categories         | based             | on       |
|     |     |     |     |     |     |     | their operating |        | principles:        | line-frequency |                 | transformer-based, |                   |          |
|     |     |     |     |     |     |     | high-frequency  |        | transformer-based, |                | and             | transformerless    |                   | con-     |
figurations.AssummarizedinTable5,eachtopologypresents
differenttradeoffsintermsofefficiency,powerdensity,relia-
bility,protectionrequirements,anddeploymentsuitabilityfor
moderndatacenters.
FIGURE11. IllustrativediagramofadatacenteronlineUPS. UPSconfigurations differintermsofthenumberofsemi-
|     |     |     |     |     |     |     | conductor | devices           | used, | and these      | differences |     | fundamentally |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | ----- | -------------- | ----------- | --- | ------------- | --- |
|     |     |     |     |     |     |     | influence | the corresponding |       | configuration. |             | For | instance,     | the |
Itisworthnotingthatdistributeddeeplearningrequiresac- VertivLiebertEXM2UPS[102]combinesathree-phasehigh-
curateGPUpowermodelingthataccountsfortheparallelism frequency rectifier with a three-level T-type insulated gate
strategies (e.g., data, model, pipeline or fully sharded data bipolar transistor inverter using space vector PWM control,
parallelism),synchronizationschemes(e.g.,bulksynchronous whereas EXL S1 UPS [103] employs a three-level neutral-
| parallel, stale-synchronous |     | parallel | asynchronous |     | stochastic |     |               |     |          |          |           |     |          |        |
| --------------------------- | --- | -------- | ------------ | --- | ---------- | --- | ------------- | --- | -------- | -------- | --------- | --- | -------- | ------ |
|                             |     |          |              |     |            |     | point-clamped |     | topology | for both | rectifier | and | inverter | stages |
gradientdescentparallelorlocalstochasticgradientdescent) inlarge-scaleapplicationssuchasAIdatacenters.Therefore,
and the communication topologies (e.g., parameter server, forEMTmodeling,itisessentialtoidentifythespecificUPS
all-reduce, and gossip) [96], [97], [98]. Thus, depending on converter configuration under study in order to accurately
theparallelismstrategy,synchronizationscheme,andcommu- capture its distinct dynamic behavior. Once the UPS con-
| nication topology, | the | relative | contributions | of  | computation, |     |            |             |          |     |                  |     |        |      |
| ------------------ | --- | -------- | ------------- | --- | ------------ | --- | ---------- | ----------- | -------- | --- | ---------------- | --- | ------ | ---- |
|                    |     |          |               |     |              |     | figuration | is defined, | detailed |     | control-oriented |     | models | must |
communication, andidleperiodscanvarysignificantly.Fail- be developed for each associated power electronic converter.
ure to accurately represent the idle behavior can negatively Numerous UPS control modeling approaches have been re-
impactpowermodelingaccuracy. ported in [100] and [101], exhibiting variations in control
|     |     |     |     |     |     |     | structure   | and complexity. |        | These           | models | typically  | include | in-  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ------ | --------------- | ------ | ---------- | ------- | ---- |
|     |     |     |     |     |     |     | ner current | control         | loops, | synchronization |        | mechanisms |         | such |
B. UNINTERRUPTIBLEPOWERSUPPLY
|             |         |         |        |           |       |      | as phase-locked |     | loops | (PLLs), | and | outer control |     | loops for |
| ----------- | ------- | ------- | ------ | --------- | ----- | ---- | --------------- | --- | ----- | ------- | --- | ------------- | --- | --------- |
| Modern data | centers | are now | viewed | as active | loads | that |                 |     |       |         |     |               |     |           |
voltage,power,orDC-linkregulation.Furthermore,practical
| function | similarly to | large inverter-based |     | systems, |     | making |     |     |     |     |     |     |     |     |
| -------- | ------------ | -------------------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
implementationaspectssuchascurrentsaturationandlimiting
detailedmodelingofUPSimperative[99].Thisisessentialfor
|     |     |     |     |     |     |     | strategies, | filter | dynamics, | energy | management |     | of  | the ESS, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --------- | ------ | ---------- | --- | --- | -------- |
assessingthedatacenter’sdynamicinteractionwiththegrid,
ride-throughcontrol,andprotectionfunctionsmustbeincor-
| including | power quality, | load | controllability, |     | fault response, |     |     |     |     |     |     |     |     |     |
| --------- | -------------- | ---- | ---------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
porated,astheyplayacriticalroleinaccuratelyanalyzingthe
| and ride-through | capability | under | both | normal | and disturbed |     |     |     |     |     |     |     |     |     |
| ---------------- | ---------- | ----- | ---- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dynamicbehaviorofUPSsystems.
operatingconditions,toensurereliableplanning,integration,
| and operation | of power | infrastructures. |     | UPS | systems | can |     |     |     |     |     |     |     |     |
| ------------- | -------- | ---------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
be classified into three main categories: standby (offline), C. COOLINGSYSTEMS
line-interactive, and online (double-conversion) UPS [21]. Modeling a data center cooling system is one of the most
Each type offers a distinct tradeoff when it comes to pro- challenging aspects when carrying out a facility-level anal-
tection level, efficiency, and transfer time [100]. The online ysis, whether it involves air-side or liquid-side cooling.
double-conversion UPS illustrated in Fig. 11 is widely used Generally, these systems have a significant impact on key
in data centers to provide the highest level of reliability, performance metrics, such as PUE and water usage effec-
fully isolating critical loads from grid voltage and frequency tiveness [104]. Hence, modeling their power consumption
| 1098 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

accurately is essential for effective energy management. A constraints, which makes them computationally efficient for
dynamic Modelica-based modeling framework is proposed large-scalesimulations.Suchapproachhasbeenusedin[112]
in[105]toanalyzetheperformanceofdatacentercoolingand and[113]toassesstheroleofESSsinprovidinggridsupport.
control systems under both normal and emergency operating For dynamic and control-oriented studies, equivalent circuit
conditions.Thismodelingapproachcapturesthemultidomain modelshavebeenextensivelyreportedin[114],[115],[116],
dynamicmodelingofcooling,electrical,andcontrolsystems. and [117]. These models typically employ first-order and
Furthermore,calibrationagainstrealmeasurementdatashows second-order Thevenin models, which are particularly pop-
that Modelica-based simulations can effectively identify op- ular due to their ability to capture battery voltage dynamics,
erationalinefficienciesandquantifysignificantenergy-saving internal losses, and transient behavior under rapidly varying
potentials through improved control strategies and system loads.Amoredetailedmodelwithahighdegreeofaccuracy
optimization [106]. Hence, it is particularly suitable for as- relies on electrochemical models, which describe ion trans-
sessing operational behavior, identifying inefficiencies, and port, diffusion, and reaction kinetics within the battery cells.
evaluatingenergy-savingpotentials. Acomprehensivedescriptionoftheunderlyingequationsand
The modeling of a cooling system in the thermal liquid the methodology associated with this modeling approach is
domain, with applications in power system studies, is pro- providedin[118],[119],and[120].Inaddition,theeffective
posedin[59].Theinterdependencebetweenserverworkload, useofthismodelingapproachrequiresaclearunderstanding
power consumption, and thermal behavior, which enables oftheESS’sarchitectureandoperatingbehavior[110].
more accurate and realistic modeling, is implemented using
MATLAB [59]. The same work further demonstrates that
E. OTHERSOURCES(WINDANDSOLARPLANTS)
environmental conditions have a significant impact on the
Wind and solar plants are increasingly integrated on-site or
resultingdatacenterpowerconsumption.Recently,anenergy-
locally with data centers to meet decarbonization and cost
performance modeling approach for direct liquid cooling is
objectives[121].Insuchconfigurations,localgenerationand
presentedin[107]toassesstheinfluenceofsupplywatertem-
storage must closely track highly dynamic data center loads,
perature on overall system efficiency. The developed model
fundamentally changing the power balance and operational
is validated using operational data from the HAWK super-
requirements.Unlikecentralizedrenewables,theseresources
computer, and the results show that increasing the supply
operate in a tightly coupled environment where inverter-
temperatureimprovesliquidcoolingenergyefficiency,while
basedgeneration,energystorage,andloaddynamicsinteract
also increasing heat transfer to the server room air and IT
over fast time scales, necessitating accurate converter-based
powerconsumption.Adifferentstudy[108]developsdetailed
modeling. Both phasor-domain and EMT models are used,
component-levelmathematicalmodelsforacold-plateliquid-
with EMT becoming critical under weak-grid and islanded
cooled data center, enabling the derivation of system power
conditions [72]. Review studies show that hybrid renewable
consumption and chip temperature characteristics. Experi-
architectures can enhance reliability and reduce dependence
mentalvalidationconfirmsthehighaccuracyoftheproposed
on diesel backup, but they also introduce protection chal-
method, supporting its applicability for optimizing opera-
lenges such as bidirectional power flows, low fault currents,
tionalparameters.
and complex coordination with UPS systems [122], [123].
Withregardtothis,robustmodelingmustaccountnotonlyfor
D. ENERGYSTORAGESYSTEMS
energyproductionbutalsoforcontroldynamicsandadaptive
ESSs in data center UPSs are gradually becoming grid-
inverter-aware protection schemes to ensure resilient opera-
interactive, supporting power system reliability rather than
tionofAIdatacenterloads.
operating solely as backup devices. For this reason, it is es-
sential to model these systems in a way that conforms with
the battery characteristics to effectively assess the dynamic VI. INTERCONNECTIONREQUIREMENTS
interactionsbetweendatacentersandthepowergrid[109].A Over the years, grid codes have primarily concentrated on
comprehensive study of various ESS modeling techniques is generation assets, requiring capabilities such as FRT, reac-
presentedin[110],wheretheapproachesdifferincomplexity tive power support, voltage control, and frequency regula-
depending on application requirements, computational effi- tion [125]. Large electrical loads, including traditional data
ciency,modelingfidelity,andefficiencyconsiderations.ESSs centers, were generally treated as passive consumers and,
can be broadly classified into electrochemical, electrostatic, therefore, subjected to comparatively limited operational re-
electromechanical, and electromagnetic technologies, which quirements. However, large-scale AI data centers operate as
are typically characterized based on their power and energy converter-dominated infrastructures with highly dynamic de-
density[111]. mand characteristics, capable of influencing both local and
Whenconsideringlong-termplanningandtechnoeconomic wide-areagridbehavior.Duetothisoutcome,severalsystem
analyses, bucket models [110] or energy-based and power operators and regulatory bodies are beginning to recognize
balancemodelsarecommonlyusedtorepresentthebehavior. that large-scale data centers should satisfy interconnection
These models typically describe the progress of the state of and operational requirements similar to those traditionally
charge (SoC) using straightforward efficiency and capacity imposedongenerationfacilities[125].
VOLUME7,2026 1099

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
TABLE6. ProposedGrid-CodeRequirementsforGrid-IntegratedDataCentersAcrossSelectedSystemOperators
Recent developments by the ERCOT, AESO, Fingrid Oyj, allowablecurrentandvoltagedistortionlevelsbasedonPCC
andtheCRUDublinreflectthistransitiontowardmorestruc- voltagelevelandtheratiobetweenavailableshort-circuitcur-
tured regulatory monitoring and enforcement for large-scale rent and facility load current [128]. Although IEEE 519 is
data center interconnections. Table 6 summarizes the emerg- formally published as a recommended practice, its harmonic
ing interconnection requirements, operational concerns, and limits are widely enforced through utility interconnection
evolving compliance expectations introduced by these sys- agreementsandtariffrequirements,makingcomplianceeffec-
temoperatorsforlarge-scalefacilities.Thissectiondiscusses tivelymandatoryforlarge-scaleAIdatacentersconnectedto
| fourkeyinterconnectionrequirementsidentifiedacrossthese |     |     |     | thegird. |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- |
regulatory frameworks, distinguishing between requirements A report by the Energy Systems Integration Group [129]
thatarecurrentlymandatory,thoseregardedasrecommended has identified that fast dynamic behavior of large loads
practices,andthosethatarestillevolvingtowardformalcom- can lead to subsynchronous interactions that conventional
plianceobligations. static load assumptions do not adequately represent. A sig-
|     |     |     |     | nificant | issue is that the | high-frequency | cycling | behavior |
| --- | --- | --- | --- | -------- | ----------------- | -------------- | ------- | -------- |
A. POWERQUALITYREQUIREMENTS associated with converter controls may contribute to sub-
|     |     |     |     | synchronous | control interactions, | subsynchronous |     | torsional |
| --- | --- | --- | --- | ----------- | --------------------- | -------------- | --- | --------- |
PowerqualitycomplianceatthePCChasbecomeoneofthe
|                |                 |                |                | interactions, | and resonance | phenomena, | particularly | under |
| -------------- | --------------- | -------------- | -------------- | ------------- | ------------- | ---------- | ------------ | ----- |
| most important | interconnection | considerations | for converter- |               |               |            |              |       |
dominated large-scale data centers. The use of UPS sys- weak-grid conditions. Consequently, utilities and system op-
|     |     |     |     | erators now | require large-scale | data centers | to  | comply with |
| --- | --- | --- | --- | ----------- | ------------------- | ------------ | --- | ----------- |
tems,switched-modepowersupplies,batteryconverters,and
variable-speedcoolingdrivesintroducesharmonicdistortion, harmonic emission standards such as IEEE 519 [130]. More
|                  |                      |             |           | specifically, | regional approaches        | vary | considerably | depend-       |
| ---------------- | -------------------- | ----------- | --------- | ------------- | -------------------------- | ---- | ------------ | ------------- |
| voltage flicker, | interharmonics,      | and current | imbalance | [127].        |                            |      |              |               |
|                  |                      |             |           | ing on        | local grid characteristics | and  | system       | strength. The |
| IEEE 519         | remains the dominant | framework   | governing | har-          |                            |      |              |               |
monic emission limits at the PCC. The standard defines AESO mandates on detailed harmonic and EMT studies for
| 1100 |     |     |     |     |     |     |     | VOLUME7,2026 |
| ---- | --- | --- | --- | --- | --- | --- | --- | ------------ |

large-scaleconverter-dominatedweakportionsoftheAlberta controllability,andreal-timevisibilityforlargetransmission-
network [13], while Nordic system operators emphasize on connectedloads[124].FingridfurtherrequirevalidatedEMT
harmonic monitoring and voltage quality assessment due to and phasor-domain models benchmarked against measured
growingconcentrationsofdigitallyintensiveloads[125]. operationaldataforcomplianceverification[125],
Operational visibility requirements are also expanding be-
B. LVRT/FRTANDGRIDSUPPORT yond SCADA monitoring. Advanced telemetry, high-speed
Ride-through capability represents one of the most rapidly measurements, real-time operational coordination, and de-
evolving areas of large-load interconnection requirements, mand forecasting are increasingly viewed as essential for
highlighting a significant gap between existing mandatory maintaining grid situational awareness under high penetra-
standards and the performance expectations emerging from tions of flexible and rapidly varying loads [133]. Most re-
gridoperators.Duringtransmissiondisturbances,severevolt- gionaltransmissionorganizationsrequirelargetransmission-
age depressions at the POI may trigger rapid disconnection connected customers, typically those exceeding 20 MW, to
of UPS systems, server power supplies, and converter-based supply SCADA-based telemetry data, including measure-
infrastructuredesignedtoprotectsensitiveITequipment[19]. mentsofactivepower,reactivepower,andvoltage,tosystem
The simultaneous loss of several large facilities can abruptly operators for real-time monitoring and operational coordi-
remove hundreds of megawatts of demand from the grid, nation [134]. While behind-the-meter visibility, such as the
resulting in frequency excursions, uneven voltage recovery, operating status of UPS, generator dispatch, and battery
transient power imbalance, and reduced operator visibility SoC, is not yet universally mandatory, organizations like the
formaintainingsystemstability.Thisrequiresgrid-integrated Department of Energy and the North American Electric Re-
data centers to remain connected during temporary voltage liability Corporation recommend enhanced monitoring and
and frequency disturbances through defined ride-through ca- telemetrytoimprovegridvisibility,reliability,andoperational
pabilities[129].Theserequirementsarebecomingmandatory awareness.Thesedevelopmentsindicatethatfutureintercon-
in weak grids and low-inertia systems, where sudden large- nection frameworks will likely require data centers not only
loadtrippingcansignificantlyamplifyinstabilityrisks[13]. to demonstrate compliance during planning studies but also
Several jurisdictions have now introduced detailed ride- to maintain continuous operational transparency throughout
through requirements for large transmission-connected loads theirlifecycle.
and data centers. The Southwest Power Pool, through its
high-impact large load framework, specifies mandatory volt- D. INTERCONNECTIONSTUDYPROCESS
ageride-throughenvelopes,controlledactivepowerrecovery Interconnection approval for large-scale grid-integrated data
requirements, and restrictions on constant-power converter centers typically requires comprehensive technical studies to
operation during voltage disturbances to prevent excessive assess potential impacts on transmission system reliability,
current amplification under LV conditions [131]. The AESO stability,protectioncoordination,andinfrastructureadequacy.
also proposed voltage tolerance, frequency withstand, and Unlike smaller commercial loads, these facilities can affect
phase-angledisturbancerequirementsforgrid-integrateddata regional load forecasting, transmission expansion planning,
centers to mitigate instability risks associated with sudden voltage stability margins, and operational reserve require-
loaddisconnection[13].Ireland’sincreasingdatacenterpen- ments.Accordingly,utilitiesandsystemoperatorscommonly
etration has prompted regulators to emphasize coordinated recommend staged interconnection assessments that may in-
reconnectionproceduresandoperationalflexibilityfollowing clude power flow analysis, short-circuit studies, harmonic
networkdisturbances[126]. analysis,transientstabilitysimulations,EMTstudies,andpro-
tectioncoordinationevaluations[13],[129],[131].Thescope
C. DYNAMICMODELINGANDOPERATIONALVISIBILITY ofrequiredstudiesgenerallydependsongrid-specificthresh-
Theincreasingcomplexityofdatacentershavecreatedgrow- olds such as connection capacity, voltage level, geographical
ing demand for accurate dynamic models capable of rep- location,andproximitytoconstrainednetworkregions[133].
resenting fast load transients, converter interactions, backup Fig. 12 illustrates the relationship between simulation do-
generation behavior, and coordinated control systems [59]. mains and the characteristic time scales associated with grid
WithAIdatacentersexhibitingextremelyfastdemandramps interconnectionstudies.Thefigurealsohighlightsthestudies
associated with computational workload scheduling, GPU required at different stages of the connection process. EMT
clusteractivation,andcoolingsystemresponses,high-fidelity studies are primarily required for fast electromagnetic phe-
modeling approaches are necessary for accurate representa- nomenaoccurringwithinmicrosecond-to-secondtimescales,
tionoftheirgridinteractions[132].Asaresult,severalsystem while phasor-domain simulations are generally applied to
operatorsandutilitiesnowrequire,andinsomejurisdictions slowerelectromechanicalphenomena[135].
mandate, the provision of real-time telemetry and accurate
dynamicmodelsaspartoflarge-loadinterconnectionrequire- VII. GRIDINTEGRATIONCHALLENGES
ments [13], [131]. In the ERCOT, growing concerns regard- As data centers continue to evolve into active participants
ing large coincident load ramps and operational uncertainty in modern power systems, grid integration challenges have
have motivated increased emphasis on operational telemetry, become a critical focus for ongoing research. The literature
VOLUME7,2026 1101

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
FIGURE12. Timescalesofpowersystemdynamics,controlactions,andrequiredstudiesduringdifferentstagesofdatacentergridconnection.
highlights a range of technical issues, including power sta- Peivandizadeh [136] proposed a new stability criteria for
bilization during high power ramps, harmonic interactions, gigawatt-scale ramps, where the critical clearing times for
system stability, voltage quality, and FRT capability. Further protectionsystemsshouldbereducedfrom150to83ms.
discussionsofthesechallengesareprovidedinthefollowing In2025,researchersfromMicrosoft,OpenAI,andNVIDIA
subsections. examinedthechallengesassociatedwithpowerswingscaused
bythehighvariabilityinpowerconsumptionduringtraining
A. POWERSTABILIZATIONANDHIGHPOWERRAMPS workloads [30]. They subsequently proposed three classes
|           |        |     |                |       |     | of power | stabilization | techniques |     | to mitigate | these | swings, |
| --------- | ------ | --- | -------------- | ----- | --- | -------- | ------------- | ---------- | --- | ----------- | ----- | ------- |
| Computing | demand | can | create extreme | power |     | dynam-   |               |            |     |             |       |         |
ics that can lead to undesirable high-magnitude transient including: 1) software-based approaches that inject con-
|                                |     |     |                 |     |          | trolled workloads |     | to smooth | power | transitions; | 2)  | GPU-level |
| ------------------------------ | --- | --- | --------------- | --- | -------- | ----------------- | --- | --------- | ----- | ------------ | --- | --------- |
| peaks inelectricityconsumption |     |     | withinsubsecond |     | tominute |                   |     |           |       |              |     |           |
timescales [1]. A study by Jimenez-Ruiz and Milano [62] firmware mechanisms that enforce ramping constraints and
on the all-island Irish transmission system reveals that un- power floors; and 3) rack-level energy storage solutions that
|            |             |              |        |     |      | absorb and | release | power as | needed. | In addition, |     | Huntington |
| ---------- | ----------- | ------------ | ------ | --- | ---- | ---------- | ------- | -------- | ------- | ------------ | --- | ---------- |
| controlled | data center | reconnection | timing | can | lead | to grid    |         |          |         |              |     |            |
instabilityduetoasuddensurgeinelectricalpowerdemand. and Tu [27] proposed the use of BESSs, and Siemens En-
ergy[137]introducedthedeploymentE-STATCOM,bothin-
| Motivated | by such risks, | the | AESO have | introduced |     | explicit |     |     |     |     |     |     |
| --------- | -------------- | --- | --------- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
ramping constraints to limit load ramping to a maximum stalledadjacenttothegridinterconnectiontosmoothtransient
rate of 10 MW/min [13]. Another study [95] shows that power swings. Meanwhile, Ko et al. [138] presents a hybrid
|             |              |        |        |        |     | coordinated | control | of colocated |     | BESS | and E-STATCOM. |     |
| ----------- | ------------ | ------ | ------ | ------ | --- | ----------- | ------- | ------------ | --- | ---- | -------------- | --- |
| large-scale | AI workloads | impose | unique | demand | on  | power       |         |              |     |      |                |     |
conversion chains and that synchronized GPU operations Collectively, these existing solutions can be categorized into
|            |               |           |            |         |          | software-defined |     | approaches      | operating |     | within the    | comput-      |
| ---------- | ------------- | --------- | ---------- | ------- | -------- | ---------------- | --- | --------------- | --------- | --- | ------------- | ------------ |
| can induce | facility-wide | power     | transients | that    | strongly | in-              |     |                 |           |     |               |              |
|            |               |           |            |         |          | ing stack        | and | grid-compatible | solutions |     | that leverage | power        |
| fluence    | the dynamic   | behavior. | Building   | on [62] | and      | [95],            |     |                 |           |     |               |              |
| 1102       |               |           |            |         |          |                  |     |                 |           |     |               | VOLUME7,2026 |

FIGURE13. Grid-integrateddatacentersupportarchitecturesforpowersystemstability.(a)GFM-BESS.(b)E-STATCOM.(c)Hybridapproach.
TABLE7. BenefitsandChallengesofStorageandControlSolutionsforAIDataCenters
electronicandenergystoragetechnologiesatthegridandload data centers in MW sizes can stimulate torsional modes in
interface.Fig.13illustratesrepresentativegridsupportarchi- nearby generating stations due to interharmonics, resulting
tectures for grid-integrated data centers aimed at improving in damage to turbine shafts. Zubi and Hfouda [140] investi-
powersystemstabilityandoperationalflexibility.Specifically, gatedthepowerqualityofatypicaldatacenter,revealingthat
theGFM-BESSconfigurationforvoltageandfrequencysup- heavy-loaded nonlinear loads leads to poor power quality at
port,isanE-STATCOM-basedarchitectureforreactivepower thePCC,withseveralscenariosapproachingorexceedingthe
compensation and voltage regulation and is a hybrid GFM- limits specified in IEEE 519 standard. That is, as more data
BESS with AI-ready UPS architecture that enhances system centers connect to the grid, harmonics will increase further,
resilience,controllability,anddisturbanceride-throughcapa- therebypushingthetotalharmonicdistortionbeyondaccept-
bility through coordinated converter-based support. Table 7 ablelimits[141].Thissituationposessignificantcompliance
furthersummarizesthecorrespondingadvantages,operational challengesforutilityoperators.
benefits,andimplementationchallengesassociatedwiththese
grid-compatiblesupportarchitectures. C. STABILITY
Severalstabilitychallengesareemergingonthegridduetothe
B. HARMONICS increasing integration of AI workload data centers. Stability
Large-scale data centers loads are typically characterized as is evaluated based on multiple criteria, including frequency,
nonlinearloadsthatintroducesignificantharmonicdistortion voltage, rotor angle, converter-driven, and resonance [142].
into the grid, resulting in power quality degradation. There- Highlydynamicdatacenteroperationsthatsupplylargenon-
fore, harmonic distortions can accumulate in large facilities linear loads can impact the aforementioned criteria, leading
housingthousandsofserverracks,spreadingthroughthelocal to grid instability [143]. Such stability issues can increase
distribution network and posing hazards to nearby industrial stress on grid assets, accelerate equipment degradation, and
and residential systems, including equipment malfunctions, ultimatelycompromiseoverallgridreliability.Apracticalex-
accelerateddegradation,overheating,andevenpotentialelec- ampleoffrequencystabilitychallengesoccurredinall-island
trical fires [1]. An analysis reported by Bloomberg in 2024 Irishtransmissionsystem[144].Whereafault-inducedevent
highlights that over three-quarters of highly distorted power ledtoasuddenreductionof204MWindatacenterdemand.
quality measurements in the United States occur within 50 This disturbance caused a rate of change of frequency (Ro-
milesofmajordatacenteractivity[139]. CoF)of0.12Hz/s,reachingapeakfrequencyof50.22Hz.
AnextensivestudyconductedbyNorthAmericanElectric Thesechallengesarefurthercomplicatedbythegeographic
Reliability Corporation [82] also points out that large-scale clustering of data centers, which creates large and highly
VOLUME7,2026 1103

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
dynamicpowerdemand[145].Subsynchronousresonancehas A practical example was recorded on 2024, when a perma-
emerged as a major challenge in situations like this [77]. A nent fault occurred on a 340-kV transmission line within
study, motivated by a real-world example [146], investigated the Eastern Interconnection in the United States [155]. The
the high-frequency undamped oscillations that appeared, ini- disturbance triggered a sequence of six short-duration volt-
tiatedbyaperiodicvoltagedisturbanceinadatacenter-dense age violations over an interval of approximately 82 s, with
regionwithinDominionEnergy’sgrid.TheERCOT,WECC, individualeventslastingbetween42and66msandreaching
andPJMInterconnectionalsoreportedsituationswherelarge magnitudesof0.24–0.40p.u.Theresultingundervoltagecon-
computing loads tripped and disconnected from the grid ditionsactivateddemand-sideprotectionmechanisms,leading
during transmission disturbance [1], [147], [148]. Kwon to the disconnection of nearly 1.5 GW of voltage-sensitive
et al. [149] investigate how large-scale data centers dynami- load[155].Posteventinvestigationsdeterminedthatthisentire
cally interact with the grid and have shown that sudden load curtailedloadoriginatedfromdatacenterfacilities.Following
surgescausesignificantfrequencydeviations,persistentoscil- the tripping events, the system voltage increased to approxi-
lations may lead to system collapse, and gradual load ramps mately1.07p.u.
tendtotriggersloweroscillatorybehaviors.Researchonwide In response to the issue highlighted above, system oper-
areapowersystemswithintegratedlarge-scaleAIworkloads ators, particularly those that have not previously imposed
indicatesthatoscillationmodesaresignificantlyinfluencedby ride-throughrequirementsonlarge-scaledatacenters,arenow
loadfluctuationfrequencyandthesizeofdatacenters[132]. activelyevaluatingtheintroductionofsuchrequirements.For
example,AESOtechnicalinterconnectionrequirementsstate
D. VOLTAGEFLICKER thattransmission-connecteddatacentersmustbedesignedto
Another power quality issue arising from the integration of withstand voltage disturbances [13]. In addition, NERC has
datacentersintothegridisvoltageflicker.Thisissueistypi- formed a dedicated task force to examine the system-level
callycausedbyvoltagefluctuationsthatresultfromdynamic impacts associated with large load interconnections [156].
changesinelectricalloadcurrentsinteractingwiththesystem Similarly, the ERCOT has established a large-load working
impedance [150]. A field measurement investigation con- group and is currently consulting on the implementation of
ductedatthePCCbetweenthegridandtwolargedatacenters FRT requirements for loads with capacities exceeding 75
(20and32MW)byNassifetal.[127]revealedthatmultiple MW [124]. In Europe, EirGrid and FinGrid have proposed
sources, including large HVAC systems, massive computer updated FRT standards for large energy users [125]. In Aus-
loads, sudden power demand changes, and nonlinear power tralia,theAustralianEnergyMarketOperatorproposedarule
electronic equipment, tend to generate voltage flickers. This changetobefinalizedin2026regardingtheaccessstandards
is further confirmed by Ahmed et al. [151], which adds that forlargeloads,suchaslargeinverter-basedloads[99].
internal power condition systems in data centers are prone
to faults that can create voltage flickers, which propagate F. CYBERSECURITYANDDATASECURITY
through the electrical system. The recent report from [82] Grid-integrated data centers concentrate vast quantities of
highlighted that large loads, such as cryptocurrency miners sensitive, proprietary, and regulated information while si-
and AI data centers, can cause voltage flickers in the grid. multaneously interacting with critical power system infras-
ThisoccursduetothevariableloadprofilesassociatedwithAI tructure, making data security and cybersecurity one of the
workloads,whichmayleadtovoltageflickerlevelsexceeding mostconsequentialoperationalandgrid-reliabilitychallenges
theacceptablelimitsoutlinedinIEC61000-3-3[152]. in modern digital energy systems. The progressive conver-
genceofITandoperationaltechnologywithinthesefacilities
E. FAULTRIDE-THROUGH/LOW-VOLTAGERIDE-THROUGH has substantially expanded the cyberattack surface. Systems
As power electronic converters increasingly dominate the thatweretraditionallyisolated,includingSCADAcontrollers,
power grid, FRT capability has become essential for main- buildingmanagementsystems,UPSmanagementbuses,cool-
taininggridstability.Thiscapabilityallowsgenerationassets ingcontrollers,energymanagementsystems,anddatacenter
and equipment to remain connected during faults, such as infrastructure management platforms, are now connected to
voltage sags [153]. When a system can sustain and support IP-basedandcloud-accessibleenvironments[157].Thiscon-
grid voltage during these fault induced voltage sags, it is vergenceexposesnotonlydigitalassetsbutalsoelectricaland
referredtoasLVRT[154].Traditionally,LVRTrequirements thermal control infrastructures to adversarial threats that can
havebeenassociatedwithgenerators,whileloadshavegener- affectbothfacilityoperationsandpowersystemstability.
allybeenconsideredpassive.However,withAIdatacenters’ A survey reported that nearly 90% of organizations oper-
powerdemandsreachinghundredsofmegawatts,theseloads ating connected IT infrastructures had experienced cyberse-
are now seen as active participants in the grid. Thus, FRT curitybreacheswithintheirICS/SCADAenvironments[158].
capabilitiesofsuchlargeloadspresentsignificantchallenges In grid-integrated data centers, such attacks may extend be-
for grid stability. These challenges are no longer theoretical, yond data compromise to directly influence grid operation
asrecentgriddisturbanceshavedemonstratedthatinadequate through manipulation of electrical demand, disruption of de-
FRT capability of large-scale AI data center loads can di- mand response participation, or destabilization of distributed
rectlytranslateintowidespreadsystem-levelstabilityimpacts. energyresources.Sincelarge-scaleAIfacilitiescanconsume
1104 VOLUME7,2026

TABLE8. SummaryofOpportunitiesforGridSupportFromAIDataCentersandTheirImpact
hundreds of megawatts, malicious alteration of cooling sys- electrical–thermal modeling study of a 10-MW data center
tems, workload scheduling, UPS dispatch, or battery coordi- showed that participation in demand response, via IT load
nationmaytriggerrapidloadfluctuations,voltageinstability, reduction and cooling setpoint adjustment, improved grid
frequency deviations, and local network congestion within frequencyfrom59.58to59.60Hzfollowinga25%loaddis-
transmissionanddistributionsystems. turbance on the grid [59]. By leveraging real-time workload
modulationandUPScoordination,anotherstudyreportedan
VIII. OPPORTUNITIES increase in frequency nadir from 59.66 to 59.85 Hz and a
Modern data centers are evolving into controllable grid- 34%reductioninrecoverytimeundera200-MWgeneration
loss[162].Acooperativecontrolofdelay-tolerantworkloads
| interactive | assets. Their | integrated | electrical, | thermal, | and |     |     |     |
| ----------- | ------------- | ---------- | ----------- | -------- | --- | --- | --- | --- |
computational systems enable coordinated multitimescale and backup power supplies across 350 MW of data center
flexibility,allowingeffectiveparticipationingridsupportser- capacity was shown to contain frequency deviation above
|              |           |                  |     |                    | 49.6 Hz | and limit RoCoF | to below | 730 mHz/s in ultra- |
| ------------ | --------- | ---------------- | --- | ------------------ | ------- | --------------- | -------- | ------------------- |
| vices. These | positions | them as enablers | of  | future low-inertia |         |                 |          |                     |
andrenewable-dominatedpowersystems.Thefollowingsec- low-inertiasystemsoperatingat75%systemnonsynchronous
|              |                   |          |              |           | penetration | [163]. In addition, | a data-driven | co-optimization |
| ------------ | ----------------- | -------- | ------------ | --------- | ----------- | ------------------- | ------------- | --------------- |
| tion discuss | these flexibility | services | and enabling | technolo- |             |                     |               |                 |
giesindetail,demonstratinghowAIdatacenterscanprovide framework demonstrated that higher penetration of flexible
fast,reliable,andscalablegridsupport. data center loads consistently improves system performance
andenhancesrenewableintegration[164].
A. FREQUENCYCONTROLSERVICES
B. FLEXIBILITYSERVICES
| Data centers | can provide | additional | services | to help | stabi- |     |     |     |
| ------------ | ----------- | ---------- | -------- | ------- | ------ | --- | --- | --- |
lize the grid, especially now that they are being redefined as They have various internal assets and operational control
|     |     |     |     |     | strategies | that can be utilized | to provide | support for the grid |
| --- | --- | --- | --- | --- | ---------- | -------------------- | ---------- | -------------------- |
grid-interactiveassets[125].Numerousstudiesandreal-world
applications have demonstrated that when data centers are whilestillmeetingSLAsforcorecomputationaltasks[165].
properlycoordinated,theycaneffectivelycontributetoancil- After reviewing the frequency control services offered by
|     |     |     |     |     | data centers, | it is important | to identify | the different sources |
| --- | --- | --- | --- | --- | ------------- | --------------- | ----------- | --------------------- |
laryservicesandsystembalancing[159],[160],[161].These
facilities are capable of adjusting active power consumption of flexibility for these services. Each source exhibits distinct
operationalcharacteristicsthatinfluenceitssuitabilityforde-
withinsubsecondtominutetimescales,duetotheirfast-acting
powerelectronicinterfaces,flexibleworkloadscheduling,and liveringancillaryservices.Thefollowingsubsectiondiscusses
integrated ESSs. This makes them well suited for frequency theflexibilityassets,responsetime,andtheirapplications.
controlservices.
| Recent | studies demonstrate |     | that data centers | can | effec- 1) UPS-BASED |     |     |     |
| ------ | ------------------- | --- | ----------------- | --- | ------------------- | --- | --- | --- |
tively support power system frequency regulation through A UPS is traditionally designed and viewed as a reliability
coordinated load and energy storage control. A coupled device,usedtosecurecriticalloadsinthedatacenter during
VOLUME7,2026 1105

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
powerinterruptions,withreal-worlddemonstrationsshowing
| that they | can respond |     | quickly | during | frequency-containment |     |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------- | ------ | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
disturbances[166].Today,AIdatacentersareequippedwith
| AI-ready | UPS | systems | [167]. | These | systems | are | large GPU |     |     |     |     |     |     |     |
| -------- | --- | ------- | ------ | ----- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
clustersthatexperiencerapidpowerfluctuationswhenaccel-
eratorssynchronizeduringtrainingorinference.Theseevents
| occur faster | than         | most       | control          | systems   | can          | respond, | making       |     |     |     |     |     |     |     |
| ------------ | ------------ | ---------- | ---------------- | --------- | ------------ | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| the UPS      | the          | first line | of stabilization |           | because      |          | it is always |     |     |     |     |     |     |     |
| online and   | electrically |            | connected        | to        | the internal |          | bus. In this |     |     |     |     |     |     |     |
| context,     | the UPS      | serves     | as a             | transient | shock        | absorber | rather       |     |     |     |     |     |     |     |
thanjustabackupenergysource.Itcaninjectorabsorbpower
withinmilliseconds,effectivelyprovidinginertialandprimary
frequency response for ancillary services markets. From the FIGURE14. Datacenterflexibilityoptionsacrosstimescales.
| grid’s perspective, |     | during | these | conditions, |     | the | data center |     |     |     |     |     |     |     |
| ------------------- | --- | ------ | ----- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
behaveslikeanactiveload.Thekeylimitationisavailability
Thiscapabilityhasbeendemonstratedinhyperscaledatacen-
ratherthanpowerrating.ThestoredenergyinaUPSprimarily
|     |     |     |     |     |     |     |     | ters, where | GFM | Tesla | Megapack | systems | help | stabilize AI |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | -------- | ------- | ---- | ------------ |
existsforride-throughcapability,whichmeansonlyafraction
|     |     |     |     |     |     |     |     | load variability |     | and improve |     | voltage resilience |     | during grid |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --- | ------------------ | --- | ----------- |
ofitscapacitycanbeusedforgridserviceswhilestillmain-
disturbances[171].Althoughenergy-limited,theseassetscan
| taining | contingency | reserves. |     | Thus, | the participation |     | of UPS |     |     |     |     |     |     |     |
| ------- | ----------- | --------- | --- | ----- | ----------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
providecontrollablerampratesandconfigurableparticipation
systemsasaflexibleresourceinthefuturemustbecarefully
forfastfrequencyresponse,makingthemtheprimaryelectri-
| managed | within | SoC | margins | and | closely | coordinated | with |     |     |     |     |     |     |     |
| ------- | ------ | --- | ------- | --- | ------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
calbufferinAIdatacenters.
thefacility’senergymanagementsystem[162].
4) ON-PREMGENERATOR
2) COOLINGCONTROL On-premise generators provide a fundamentally different
Coolingsystemsindatacentersaccountforasignificantpor- form of flexibility function compared to electronic or com-
| tion of | total electrical |     | demand, | following |     | IT load | demand, |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | ------- | --------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
putationalcontrols,mostcommonlyusingdiesel,naturalgas,
makingthemanimportantsourceofflexibility.UnlikecoreIT orhydrogen-basedtechnologies[172].Duetoenvironmental
loads,coolingdemandhasinherentthermalinertiathatcanbe
|     |     |     |     |     |     |     |     | concerns | associated | with | diesel | generators, | fuel | cells have |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ---- | ------ | ----------- | ---- | ---------- |
leveragedbytemporarilyadjustingtemperaturesetpoints[59]. emerged as a cleaner and reliable alternative for primary
Operational strategies include precooling before anticipated and backup power in data centers, a feasibility demonstrated
| peak periods |     | or temporarily |     | relaxing | cooling | requirements |     |           |     |      |                   |     |            |        |
| ------------ | --- | -------------- | --- | -------- | ------- | ------------ | --- | --------- | --- | ---- | ----------------- | --- | ---------- | ------ |
|              |     |                |     |          |         |              |     | by a 3-MW | PEM | fuel | cell installation |     | in Latham, | United |
when grid support is needed [168]. This approach can be States [173]. These assets can be viewed as deep-reserve
appliedinhigh-power-densitydatacenters,wherethethermal
|            |        |         |        |              |     |     |             | layer of     | data center | flexibility |              | significant | for grid | support,    |
| ---------- | ------ | ------- | ------ | ------------ | --- | --- | ----------- | ------------ | ----------- | ----------- | ------------ | ----------- | -------- | ----------- |
| inertia of | liquid | cooling | loops, | air volumes, |     | and | server room |              |             |             |              |             |          |             |
|            |        |         |        |              |     |     |             | particularly | by          | reducing    | the reliance | on          | the grid | during peak |
structuresactsasshort-termenergybuffers.Thesebufferscan demand times. However, their relatively slow ramp-up rates
| absorb and | release | energy | over | time, | helping | to  | smooth out |                |     |              |           |           |     |             |
| ---------- | ------- | ------ | ---- | ----- | ------- | --- | ---------- | -------------- | --- | ------------ | --------- | --------- | --- | ----------- |
|            |         |        |      |       |         |     |            | and regulatory |     | restrictions | regarding | emissions |     | and contin- |
cluster-level power ramps caused by GPU utilization. Cool- uous operation limit their effectiveness for rapid frequency
| ing adjustments  |     | respond | slowly         | due | to thermal |     | lags and the  |             |          |      |            |        |               |     |
| ---------------- | --- | ------- | -------------- | --- | ---------- | --- | ------------- | ----------- | -------- | ---- | ---------- | ------ | ------------- | --- |
|                  |     |         |                |     |            |     |               | regulation. | Instead, | they | are better | suited | for secondary | and |
| slow propagation |     | of      | heat. However, |     | they       | can | significantly |             |          |      |            |        |               |     |
tertiarysystemfrequencyregulation,wheredurationandpre-
contribute to secondary frequency regulation for events that dictabilityaremorecriticalthanresponsespeed[160].Rather
| last minutes. |     | Nevertheless, |     | thermal | margins | can | be limited |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | ------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
thanreshapingdemand,theytemporarilyreplacegridsupply.
| by the operational |     | envelopes |     | and standards |     | of the | hardware; |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ------------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
therefore,itisessentialtomanageflexibilitycarefullytopre-
5) E-STATCOM
ventaccelerateddegradationofcomponents.
|     |     |     |     |     |     |     |     | E-STATCOMs |     | are power | electronic | assets | that enhance | grid |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ---------- | ------ | ------------ | ---- |
flexibilitybyintegratingsupercapacitorsinparallelwithloads
3) GFM-BESS toprovidefastactivepowercompensationduringloadswings
As mentioned in Section III, modern data centers now de- and reactive power support for voltage stability[137], [174].
ploy dedicated BESS as grid-interactive assets located at the AIdatacentersexperiencerapidpowerfluctuationsandvolt-
PCC.ThisapproachisalreadyusedbyGoogleandMicrosoft, agedisturbancesduetothelargepowerelectronicconverters
where lithium-ion BESS are integrated into their data cen- utilized in GPU power supplies, especially during inference
terinfrastructures,primarilytoenhanceoperationalresilience and training of AI models. Unlike GFM-BESS, which ef-
andsupportrenewableenergyintegration[169],[170].When fectively manages energy imbalances over longer periods,
operated with GFM control, these BESS units emulate the E-STATCOMsofferafast-responsesolutiontomitigatethese
dynamicbehaviorofsynchronousgeneratorsbyactivelyreg- power and voltage transients and can be deployed at the
ulating terminal voltage and system frequency, while also PCC within the data center. However, this capability comes
delivering synthetic inertia during fast grid transients [143]. atthecostoflimitedenergycapacityinsupercapacitor-based
| 1106 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

| storage. | Their response |     | times | are typically |     | in the | subcycle |                        |     |     |     |     |     |     |
| -------- | -------------- | --- | ----- | ------------- | --- | ------ | -------- | ---------------------- | --- | --- | --- | --- | --- | --- |
|          |                |     |       |               |     |        |          | 8) CLOCKRATEMODULATION |     |     |     |     |     |     |
to millisecond range, making them particularly effective for Clock rate modulation, typically implemented through dy-
inertial response, fast frequency response, and voltage reg- namic voltage and frequency scaling (DVFS) at the server
ulation in weak or low-inertia grids [175]. Therefore, they or processor level, provides a fine-grained control lever for
occupy the fastest layer of the flexibility stack, enabling the adjusting the power draw of compute resources [181]. By
| facility | to host | extremely | dense | compute | hardware |     | without |     |     |     |     |     |     |     |
| -------- | ------- | --------- | ----- | ------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
leveragingthisapproachonCPUandGPUcores,datacenters
compromisinggridstability,whileallowingslowerflexibility can significantly reduce power consumption with minimal
mechanisms to respond subsequently in grid-interactive data impactoncomputationalperformance,enablingeffectiveand
centers.
responsivepowerflexibility.Forexample,duringAItraining,
|     |     |     |     |     |     |     |     | underclocking |     | an NVIDIA | A100 | GPU | running | a Vienna Ab |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ---- | --- | ------- | ----------- |
initiosimulationpackage(VASP)workloadachievedapprox-
6) WORKLOADSCHEDULING
|             |            |         |     |           |     |           |      | imately | 50% power | reduction |     | with only | 10% | performance |
| ----------- | ---------- | ------- | --- | --------- | --- | --------- | ---- | ------- | --------- | --------- | --- | --------- | --- | ----------- |
| Data center | operations | involve |     | a variety | of  | workloads | that |         |           |           |     |           |     |             |
loss[182].Themainadvantageofthisapproachisitspropor-
differintermsofurgencyandcomputationalflexibility[176].
tionalandreversiblebehavior,whichallowsdemandshaping
| These workloads |        | can be | broadly  | categorized |     | into urgent | and |          |             |     |                  |     |           |         |
| --------------- | ------ | ------ | -------- | ----------- | --- | ----------- | --- | -------- | ----------- | --- | ---------------- | --- | --------- | ------- |
|                 |        |        |          |             |     |             |     | in small | increments, |     | with performance |     | recovered | immedi- |
| nonurgent       | tasks, | based  | on their | sensitivity |     | to latency  | and |          |             |     |                  |     |           |         |
atelytheconstraintisreleased.Thisprovidessecondresponse
| execution           | requirements.   |           | Nonurgent  | tasks,   | such      | as           | data back- |               |          |           |               |               |                |           |
| ------------------- | --------------- | --------- | ---------- | -------- | --------- | ------------ | ---------- | ------------- | -------- | --------- | ------------- | ------------- | -------------- | --------- |
|                     |                 |           |            |          |           |              |            | capabilities, | making   | it        | suitable      | for primary   | frequency      | regu-     |
| ups, large          | file transfers, |           | and the    | training | of        | new AI       | models,    |               |          |           |               |               |                |           |
|                     |                 |           |            |          |           |              |            | lation[163].  | The      | response  | time,measured |               | in seconds,    | aligns    |
| do not require      |                 | immediate | execution. |          | Because   | of           | this, they |               |          |           |               |               |                |           |
|                     |                 |           |            |          |           |              |            | well with     | the time | constants | of            | grid control, | enabling       | DVFS      |
| can be              | scheduled       | flexibly  | to help    | support  |           | the system   | dur-       |               |          |           |               |               |                |           |
|                     |                 |           |            |          |           |              |            | to operate    | more     | like a    | controllable  | load          | than a delayed | com-      |
| ing periods         | of high         | demand.   | In         | 2023,    | Google    | demonstrated |            |               |          |           |               |               |                |           |
|                     |                 |           |            |          |           |              |            | putational    | task.    | However,  | it is         | essential     | to note        | that DVFS |
| a workload-shifting |                 | approach  | that       | delays   | nonurgent |              | tasks      | to            |          |           |               |               |                |           |
shouldnotbeseenasadeepflexibilityresource.Itseffective-
| support        | grid demand | response |             | [177].      | Studies      | indicate        | that      |                 |            |                       |              |              |               |             |
| -------------- | ----------- | -------- | ----------- | ----------- | ------------ | --------------- | --------- | --------------- | ---------- | --------------------- | ------------ | ------------ | ------------- | ----------- |
|                |             |          |             |             |              |                 |           | ness is limited |            | by performance        |              | guarantees   | and           | SLAs, which |
| 30%–50%        | of current  | data     | center      | workloads   |              | are deferrable, |           | a               |            |                       |              |              |               |             |
|                |             |          |             |             |              |                 |           | cap the         | achievable | curtailment.          |              | In practice, | DVFS          | provides    |
| share expected |             | to grow  | with the    | expansion   |              | of AI           | data cen- |                 |            |                       |              |              |               |             |
|                |             |          |             |             |              |                 |           | high-quality    | but        | low-volume            | flexibility. |              | Consequently, | it is       |
| ters [178].    | This        | strategy | offers      | flexibility | on           | minute-to-hour  |           |                 |            |                       |              |              |               |             |
|                |             |          |             |             |              |                 |           | best deployed   |            | as a regulation-layer |              | control,     | complementing |             |
| timescales.    | While       | SLAs     | and latency |             | requirements |                 | constrain |                 |            |                       |              |              |               |             |
slowerbutlargermechanismssuchasworkloadschedulingor
workloadscheduling,theflexibilityisstillsubstantialbecause
migration.
| modern | data centers | host | a heterogeneous |     | mix | of  | interactive |     |     |     |     |     |     |     |
| ------ | ------------ | ---- | --------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Table8summarizesthekeyopportunitiesingrid-integrated
andbatchprocesses.AsAIworkloadsexpand,theproportion
AIdatacenters,highlightingthechallengesaddressed,poten-
| of deadline-based |     | computation |     | is likely | to  | grow, | increasing |               |     |          |          |       |      |                |
| ----------------- | --- | ----------- | --- | --------- | --- | ----- | ---------- | ------------- | --- | -------- | -------- | ----- | ---- | -------------- |
|                   |     |             |     |           |     |       |            | tial impacts, | and | enabling | methods, | while | Fig. | 14 illustrates |
thetemporalbufferingcapabilityofdatacenters.Thus,work-
|                 |     |        |           |     |          |              |     | the available | data | center | flexibility | options | across | multiple |
| --------------- | --- | ------ | --------- | --- | -------- | ------------ | --- | ------------- | ---- | ------ | ----------- | ------- | ------ | -------- |
| load scheduling |     | should | be viewed | as  | the core | load-shaping |     |               |      |        |             |         |        |          |
timescales.
| resource, | forming | the middle | layer | between |     | fast but | shallow |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | ----- | ------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
clockratemodulationcontrolandslowerspatialmechanisms
suchasworkloadmigration.
|     |     |     |     |     |     |     |     | IX. CONCLUSIONANDFUTURENEEDS |         |          |           |         |     |              |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | ------- | -------- | --------- | ------- | --- | ------------ |
|     |     |     |     |     |     |     |     | Recent                       | reports | indicate | that data | centers | are | experiencing |
7) WORKLOADMIGRATION rapid growth and becoming increasingly integrated into the
Workload migration introduces spatial flexibility into data electrical grid, which presents new challenges. Choosing the
center operation by geographically relocating computation right modeling approach for data centers is imperative to
ratherthancurtailingload,therebyexploitingregionaldiffer- accuratelyrepresenttheirinteractionwiththegridundervar-
ences in electricity prices, policy incentives, and renewable ious operating conditions. This article presents a detailed
energy availability [179]. This capability has been shown to review of data center architectures, modeling techniques, in-
support grid balancing for both data centers and system op- terconnection requirements, as well as the challenges and
erators through cost-effective coordination strategies [180]. opportunities associated with grid integration. In addition,
AI workloads are becoming increasingly portable across ge- detailedmodelingconsiderationsforcriticalcomponentshave
ographically distributed data centers. Moving training tasks beendiscussedtosupportaccuraterepresentationofdynamic
between regions does not change how much energy is used, loadbehaviorandgridinteractionacrossmultipletimescales.
but determines where the grid must supply it. However, the Looking forward, future research must prioritize hybrid
flexibility is constrained by data gravity and communication and high-fidelity modeling frameworks that balance compu-
latency. Large datasets and network bandwidth can impose tational efficiency with dynamic accuracy, particularly for
practical limits on how frequently workloads can move and large-scale AI data centers. There is also a growing need for
how much load can be relocated. Consequently, migration standardized grid-code frameworks tailored to large flexible
operatesnaturallyonminute-to-hourhorizonsfastenoughto loads, enhancing coordination between data center energy
followrenewablerampsandmarketintervals,buttooslowfor management systems and system operators, as well as inte-
primarycontrolservices[172]. grating GFM assets and machine-learning-based predictive
| VOLUME7,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 1107 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
| control strategies | to effectively       |              | utilize multitimescale |              | flexi- |                        |            |              |             |           |             |           |
| ------------------ | -------------------- | ------------ | ---------------------- | ------------ | ------ | ---------------------- | ---------- | ------------ | ----------- | --------- | ----------- | --------- |
|                    |                      |              |                        |              |        | [19] E. Ginzburg-Ganz, |            | P. Lifshits, | R. Machlev, | J.        | Belikov, Z. | Krieger,  |
|                    |                      |              |                        |              |        | and Y.                 | Levron,    | “Technical   | challenges  | of AI     | data center | inte-     |
| bilityfor          | improved grid        | stabilityand | reliable participation |              | in     |                        |            |              |             |           |             |           |
|                    |                      |              |                        |              |        | gration                | into power | grids—A      | survey,”    | Energies, | vol.        | 19, 2025, |
| ancillary          | services. Addressing | these        | needs will             | be essential |        |                        |            |              |             |           |             |           |
Art.no.137.
for enabling AI data centers to operate not merely as large [20] K.M.U.Ahmed,M.Bollen,andM.Alvarez,“Areviewofdatacenters
consumersofelectricity,butasresilient,intelligent,andgrid- energyconsumptionandreliabilitymodeling,”IEEEAccess,vol.9,
pp.152536–152563,2021.
| supportive | assets in low-inertia | renewable-dominated |     |     | power |                                                               |     |     |     |     |     |     |
| ---------- | --------------------- | ------------------- | --- | --- | ----- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |                       |                     |     |     |       | [21] Y.S.Hussein,M.Alrashd,A.S.Alabed,andA.Zraiqat,DataCentre |     |     |     |     |     |     |
systems. Infrastructure:PowerEfficiencyandProtection.London,U.K.:Inte-
chOpen,2023.
|     |     |     |     |     |     | [22] A.Barthelme,X.Xu,andT.Zhao,“AhybridACandDCdistribution |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
architectureindatacenters,”inProc.IEEEEnergyConvers.Congr.
REFERENCES
Expo.,2017,pp.2017–2022.
[1] X. Chen, X. Wang, A. Colacelli, M. Lee, and L. Xie, “Electricity [23] M.A.MiladandM.Darwish,“UPSsystem:Howcurrentandfuture
demandandgridimpactsofaidatacenters:Challengesandprospects,” technologiescanimproveenergyefficiencyindatacentressubmitted
2025,arXiv:2509.07218.
inpartialfulfilmentoftherequirementsforthedegreeofdoctorofphi-
[2] A.Bozkurt,“Generativeartificialintelligence(AI)poweredconver- losophy,” 2017. [Online]. Available: http://bura.brunel.ac.uk/handle/
| sationaleducationalagents:Theinevitableparadigmshift,”AsianJ. |     |     |     |     |     | 2438/14664 |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
DistanceEduc.,vol.18,no.1,pp.198–204,Mar.2023. [24] M. Faisal, T. Walter, and S. Montenegro, “Power distribution unit
[3] H.WangandD.Tang,“Challengesandopportunitiesfortheenergy (PDU)foradistributedcomputingnetwork,”inProc.21stConf.Open
managementofsustainabledatacentersinsmartgrids,”inProc.IOP
Innov.Assoc.,2017,pp.108–113.
Conf.Ser.:EarthEnviron.Sci.,2022,vol.984,no.1,Art.no.012005. [25] A.Al-Harbi,F.Al-Jwesm,andY.Al-Howeish,“Improvingefficiency,
[4] “Data center sustainability,” Deloitte Insights. Accessed: Dec. reliabilityandlife-timecostofdatacentersusingDCtechnology,”in
29, 2025. [Online]. Available: https://www.deloitte.com/us/ Proc.IEEE3rdInt.Conf.DCMicrogrids,2019,pp.1–5.
en/insights/industry/technology/technology-media-and-telecom- [26] V. Vossos et al., “Adoption pathways for dc power distribution in
predictions/2025/genai-power-consumption-creates-need-for-more- buildings,”Energies,vol.15,no.3,2022,Art.no.786.
sustainable-data-centers.html [27] J.HuntingtonandM.Tu,“800VDCarchitecturefornext-generation
[5] “Global data centre electricity consumption, by equipment, AI infrastructure 800 VDC architecture for next-generation AI in-
base case, 2020-2030—Charts–data & statistics,” Int. Energy frastructure the architectural imperative of 800VDC and integrated
Agency, 2025. [Online]. Available: https://www.iea.org/data-and- energy storage,” NVIDIA, Santa Clara, CA, USA, Tech. Rep.,
| statistics/charts/global-data-centre-electricity-consumption-by- |     |     |     |     |     | 2025. |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
equipment-base-case-2020-2030 [28] NlyteSoftware,“Datacenterrackpowercosts:Acondensedanaly-
[6] “USdatacenters’energyuseamidtheartificialintelligenceboom,” sis,”2024.Accessed:Nov.19,2025.[Online].Available:https://www.
Pew Research Center. Accessed: Dec. 29, 2025. [Online]. Avail- nlyte.com/blog/data-center-rack-power-costs-acondensed-analysis/
able: https://www.pewresearch.org/short-reads/2025/10/24/what-we- [29] “AI-ready data center construction—Hyperscale & modern
know-about-energy-use-at-us-data-centers-amid-the-ai-boom/ infrastructure,”2024.Accessed:Nov.19,2025.[Online].Available:
[7] InternationalEnergyAgency,“Electricity2024—Analysisandfore- https://skillit.com/ai-ready-data-center-construction-hyperscale-
castto2026,”Int.EnergyAgency,2024.[Online].Available:www. modern-infrastructure
iea.org [30] E.Choukseetal.,“PowerstabilizationforAItrainingdatacenters,”
[8] InternationalEnergyAgency,“Worldenergyoutlookspecialreport:
2025,arXiv:2508.14318.
Energy and AI,” Int. Energy Agency, Tech. Rep., 2025. [Online]. [31] R. B. Darla and A. Chitra, “A comprehensive review of distributed
Available:https://www.iea.org/ power system architecture for telecom and datacenter applications,”
[9] “CRUduetosetoutnewrulesfordatacentre,”MasonHayesCur- Int.J.PowerElectron.DriveSyst.,vol.12,no.3,2021,Art.no.1535.
ran.Accessed:Mar.8,2026.[Online].Available:https://www.mhc.ie/ [32] ABB,“RedefiningpowerinfrastructureforAI:Theroleof800VDC
latest/insights/cru-sets-out-new-rules-for-data-centre-connections
indatacenters,”ABB,2025.[Online].Available:https://new.abb.com/
[10] “Netherlandsprohibitscreatinghyperscaledatacentresuntilnational [33] R. Taylor and S. Ashok, “Next-generation server power designs
guidelinesarepassed,”onlinenewsreport,2025. with integrated GAN technology,” Texas Instruments Presentation
[11] F.H.Liu,K.P.Lai,B.Seah,andW.T.Chow,“Decarbonisingdigital on Power Designs With Integrated GaN Technology, 2025. [On-
infrastructureandurbansustainabilityinthecaseofdatacentres,”npj line].Available:https://www.ti.com/jp/lit/ml/slypa77/slypa77.pdf?ts=
UrbanSustainability,vol.5,2025,Art.no.15.
1741767985265
[12] “Data centres: An international legal and regulatory perspective [34] A. Isazadeh, D. Ziviani, and D. E. Claridge, “Global trends,
spotlightonSingapore,”WatsonFarley&Williams.Accessed: Jan. performance metrics, and energy reduction measures in data-
12, 2026. [Online]. Available: https://www.wfw.com/articles/data- com facilities,” Renewable Sustain. Energy Rev., vol. 174, 2023,
| centres-an-international-legal-and-regulatory-perspective-spotlight- |     |     |     |     |     | Art.no.113149. |     |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
on-singapore/
|     |     |     |     |     |     | [35] X. Huang, | J.  | Yan, X. Zhou, | Y.  | Wu, and | S. Hu, | “Cooling |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ------- | ------ | -------- |
[13] AESO, “Connection requirements for transmission-connected data technologies for internet data center in China: Principle, energy
centres draft for stakeholder review,” Calgary, Alberta, Canada, efficiency, and applications,” Energies, vol. 16, no. 20, 2023,
| Aug.2025.[Online].Available:https://www.aeso.ca. |     |     |     |     |     | Art.no.7158. |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
[14] AustralianEnergyMarketCommission,“AEMCproposesnewgrid [36] H.Chen,Y.hangPeng,andY.lingWang,“Thermodynamicanalysis
standardsfordatacentreconnections,”2026.Accessed:May11,2026. ofhybridcoolingsystemintegratedwithwasteheatreusingandpeak
[Online]. Available: https://www.aemc.gov.au/news-centre/media- load shifting for data center,” Energy Convers. Manage., vol. 183,
releases/aemc-proposes-new-grid-standards-data-centre-connections 2019,pp.427–439.
[15] E.Oró,V.Depoorter,A.Garcia,andJ.Salom,“Energyefficiencyand [37] L.Silva-Llanca,C.V.Ponce,E.Bermúdez,D.Martínez,A.J.Díaz,
renewableenergyintegrationindatacentresstrategiesandmodelling andF.Aguirre,“Improvingenergyandwaterconsumptionofadata
review,”RenewableSustain.EnergyRev.,vol.42,pp.429–445,2015. centerviaairfree-coolingeconomization:Theeffectweatheronits
[16] Y.Zhang,H.Tang,H.Li,andS.Wang,“Integrationandinteractionof performance,” Energy Convers. Manage., vol. 292, 2023, Art. no.
| next-generationai-focuseddatacenterswithsmartgridsanddistrict |     |     |     |     |     | 117344. |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
energy systems: The state-of-the-art, opportunities and challenges,” [38] E.A.Amado,P.S.Schneider,andC.S.Bresolin,“Freecoolingpoten-
RenewableSustain.EnergyRev.,vol.224,2025,Art.no.116097.
tialforBraziliandatacentersbasedonapproachpointmethodology,”
[17] D.A.Kez,A.M.Foley,F.W.B.H.Wong,A.Dolfi,andG.Srinivasan, Int.J.Refrigeration,vol.122,pp.171–180,2021.
“AI-driven cooling technologies for high-performance data centres: [39] H.ChenandD.Li,“Currentstatusandchallengesforliquid-cooled
State-of-the-artreviewandfuturedirections,”Sustain.EnergyTechnol. datacenters,”Front.EnergyRes.,vol.10,2022,Art.no.952680.
Assessments,vol.82,2025,Art.no.104511. [40] B. Ramakrishnan et al., “Understanding the impact of data center
| [18] Y. Sheng | et al., “Power | for AI data | centers: Energy | demand, | grid |                |     |            |             |            |          |     |
| ------------- | -------------- | ----------- | --------------- | ------- | ---- | -------------- | --- | ---------- | ----------- | ---------- | -------- | --- |
|               |                |             |                 |         |      | liquid cooling | on  | energy and | performance | of machine | learning | and |
impacts,challengesandperspectives,”Energies,vol.19,no.3,2026, artificialintelligenceworkloads,”J.Electron.Packag.,vol.147,no.2,
| Art.no.722. |     |     |     |     |     | 2024,Art.no.021003. |     |     |     |     |              |     |
| ----------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | ------------ | --- |
| 1108        |     |     |     |     |     |                     |     |     |     |     | VOLUME7,2026 |     |

[41] I. Latif, M. A. Shafique, H. Ullah, A. C. Newkirk, X. Yu, [62] A. Jimenez-Ruiz and F. Milano, “Data center model for transient
and A. Munir, “Cooling matters: Benchmarking large language stabilityanalysisofpowersystems,”2025.[Online].Available:http:
models and vision-language models on liquid-cooled versus air- //arxiv.org/abs/2505.16575
cooled h100 GPU systems,” IEEE Trans. Cloud Comput., 2026 [63] R.W.Kenyon,B.Wang,A.Hoke,J.Tan,andB.-M.Hodge,“Com-
(inpress). parisonofelectromagnetictransientandphasordynamicsimulations:
[42] M.Azarifar,M.Arik,andJ.-Y.Chang,“Liquidcoolingofdatacenters: Implications for inverter dominated systems,” in Proc. IEEE Power
Anecessityfacingchallenges,”Appl.ThermalEng.,vol.247,2024, EnergySoc.Innov.SmartGridTechnol.Conf.,2023,pp.1–5.
Art.no.123112. [64] K. Engineering, “Model accuracy and verification for EMT and
[43] P.Boschee,“Comments:Runninghotandcoolforapowerboost,”J. PSPDsimulationsofinverter-basedresources,”2026.Accessed:Jan.
PetroleumTechnol.,vol.76,pp.14–15,2024. 26,2026.[Online].Available:https://keentelengineering.com/model-
[44] Y.Zhang,C.Fan,andG.Li,“Discussionsofcoldplateliquidcooling accuracy-and-verification-for-emt-and-pspd-simulations-of-inverter-
technologyanditsapplicationsindatacenterthermalmanagement,” based-resources
Front.EnergyRes.,vol.10,2022,Art.no.954718. [65] North American Electric Reliability Corporation (NERC),
[45] T.Bambaravanage,A.S.Rodrigo,andS.Kumarawadu,“Modelling “Beyond positive sequence RMS simulations for high
thepowersystem,”inModeling,Simulation,andControlofaMedium- DER penetration conditions,” North American Electric
ScalePowerSystem.Singapore:Springer,2018. Reliability Corporation, Oct. 2022. [Online]. Available:
[46] F. Li, H. Wang, D. Liu, and K. Sun, “A review of multi- https://www.nerc.com/globalassets/who-we-are/standing-
temporal scale regulation requirements of power systems and di- committees/rstc/beyond_positive_sequence_technical_report.pdf
verseflexibleresourceapplications,”Energies,vol.18,no.3,2025, [66] Keentel Engineering, “Electromagnetic transient (EMT) analysis
Art.no.643. for modern power systems,” 2025. Accessed: Jan. 26, 2026. [On-
[47] K. Oikonomou, J. D. Kern, B. Tarroja, and N. Voisin, “Review of line]. Available: https://keentelengineering.com/emt-analysis-power-
coreprocessrepresentationinpowersystemoperationalmodels:Gaps, systems
challenges,andopportunitiesformultisectordynamicsresearch,”En- [67] K. Chen, “EPE perspective on modeling needs,” Large Loads
ergy,vol.238,2022,Art.no.122049. Workshop, Session 3: Modeling Needs, 2025 [Online]. Available:
[48] J. Priesmann, L. Nolting, and A. Praktiknjo, “Are complex energy https://www.esig.energy/wp-content/uploads/2025/03/EPE-
systemmodelsmoreaccurate?Anintra-modelcomparisonofpower Perspective-on-Modeling-Needs_Kevin-Chen.pdf
systemoptimizationmodels,”Appl.Energy,vol.255,2019,Art.no. [68] A.Allabadi,J.Mahseredjian,S.Dennetière,A.Abusalah,I.Kocar,
113783. andT.Ould-Bachir,“AccelerationstrategiesforEMTsimulationof
[49] Energy Systems Integration Group (ESIG), “Generic models HVDC systems,” Electr. Power Syst. Res., vol. 252, 2026, Art. no.
(WPPS),”2026.Accessed:Jan.22,2026.[Online].Available:https: 112399.
//www.esig.energy/wiki-main-page/generic-models-wpps/ [69] M.R.Nasab,R.Cometa,S.Bruno,G.Giannoccaro,andM.LaScala,
[50] H.-A. Ounifi, X. Liu, A. Gherbi, Y. Lemieux, and W. Li, “Model- “Powersystemssimulationandanalysis:Areviewoncurrentapplica-
based approach to data center design and power usage effective- tionsandfuturetrendsinDRTSofgrid-connectedtechnologies,”IEEE
ness assessment,” Procedia Comput. Sci., vol. 141, pp.143–150, Access,vol.12,pp.121320–121345,2024.
2018. [70] J.Sun,S.Wang,J.Wang,andL.M.Tolbert,“Dynamicmodeland
[51] Energy Systems Integration Group (ESIG), “GFM landscape— converter-based emulator of a data center power distribution sys-
Modeling and model verification efforts,” 2026. Accessed: Jan. tem,” IEEE Trans. Power Electron., vol. 37, no. 7, pp. 8420–8432,
22, 2026. [Online]. Available: https://www.esig.energy/working- Jul.2022.
users-groups/reliability/grid-forming/gfm-landscape/modeling/ [71] A. Arisoy and D. K. Sen, “A hardware-in-the-loop simulation case
[52] “PyDCM:Customdatacentermodelswithreinforcementlearningfor study of high-order sliding mode control for a flexible-link robotic
sustainability,” in Proc. 10th ACM Int. Conf. Syst. Energy-Efficient arm,”Appl.Sci.,vol.15,no.19,2025,Art.no.10484.
Buildings,Cities,Transp.,2023,pp.232–235. [72] C.Shahetal.,“Reviewofdynamicandtransientmodelingofpower
[53] Y. Berezovskaya, C.-W. Yang, A. Mousavi, V. Vyatkin, and T. B. electronicconvertersforconverterdominatedpowersystems,”IEEE
Minde,“Modularmodelofadatacentreasatoolforimprovingits Access,vol.9,pp.82094–82117,2021.
energyefficiency,”IEEEAccess,vol.8,pp.46559–46573,2020. [73] G.Gao,X.Wang,T.Zhu,Y.Liao,andJ.Tong,“HSSmodelingand
[54] E. Mickelson and J. Gibfried, “NERC large loads task force: stabilityanalysisofsingle-phasePFCconverters,”inProc.IEEEAppl.
LLTF meeting and technical workshop,” Accessed: Apr. 10, 2025. PowerElectron.Conf.Expo.,2022,pp.1812–1819.
[Online]. Available: https://www.nerc.com/globalassets/who-we- [74] S.Chakrabortyetal.,“Designofmultifunctionalelectromagnetictran-
are/standing-committees/rstc/lltf/lltf_april_meeting__technical_ sient model for grid-forming inverters,” in Proc. 50th Annu. Conf.
workshop_presentations_.pdf IEEEInd.Electron.Soc.,Chicago,IL,USA,Nov.2024,pp.1–6.
[55] P.J.Kühn,“Energyefficiencyandperformanceofclouddatacenters: [75] J.Sun,M.Xu,M.Cespedes,andM.Kauffman,“Datacenterpower
Whichrolecanmodelingplay?,”inProc.5thInt.WorkshopEnergy systemstability—PartI:Powersupplyimpedancemodeling,”CSEEJ.
EfficientDataCentres,2016,pp.1–6. PowerEnergySyst.,vol.8,no.2,pp.403–419,2022.
[56] D.SchlittandW.Nebel,“Datacenterperformancemodelforeval- [76] J.Sun,M.Mihret,M.Cespedes,D.Wong,andM.Kauffman,“Data
uatingloaddependentenergyefficiency,”2016.[Online].Available: center power system stability—Part II: System modeling and anal-
https://www.spec.org/power ysis,” CSEE J. Power Energy Syst., vol. 8, no. 2, pp. 420–438,
[57] Y.Zhang,I.C.Paschalidis,andA.K.Coskun,“Datacenterparticipa- 2022.
tionindemandresponseprogramswithquality-of-serviceguarantees,” [77] G. Ruan, M. D. Ilic, and L. Xie, “Data center control against
inProc.10thACMInt.Conf.FutureEnergySyst.,2019,pp.285–302. sub-synchronous resonance: A data-driven approach,” 2025,
[58] K. M. U. Ahmed, J. Sutaria, M. H. J. Bollen, andS. K. Rönnberg, arXiv:2511.14141.
“Electricalenergyconsumptionmodelofinternalcomponentsindata [78] M.Siltala,“Simulatingdatacentercoolingsystems:Data-drivenand
centers,”inProc.IEEEPESInnov.SmartGridTechnol.Eur.,2019, physicalmodelingmethods,”AaltoUniv.,2020.[Online].Available:
pp.1–5. https://www.aalto.fi
[59] P.P.Gyang,P.Chakraborty,L.Meegahapola,andX.Yu,“Dynamic [79] J.Sun,M.Xu,M.Cespedes,andM.Kauffman,“Low-frequencyinput
modelingofadatacenterforpowersystemstabilitystudies,”IEEE impedancemodelingofsingle-phasePFCconvertersfordatacenter
Trans.PowerSyst.,vol.41,no.3,pp.2317–2332,May2026. powersystemstabilitystudies,”inProc.IEEEEnergyConvers.Congr.
[60] H.Suryanarayana,L.Qi,Y.Zhang,T.Jiang,S.Colombi,andH.C. Expo.,2019,pp.97–106.
Handlin, “System modeling and fault studies in data center power [80] L. Kong, Y. Xue, L. Qiao, and F. Wang, “Review of small-signal
distribution,” in Proc. 26th Int. Conf. Exhib. Electr. Distrib., 2021, converter-drivenstabilityissuesinpowersystems,”IEEEOpenAccess
pp.1435–1439. J.PowerEnergy,vol.9,pp.29–41,2022.
[61] J.D.Lara,R.Henriquez-Auba,D.Ramasubramanian,S.Dhople,D. [81] P.-H.TrinhandI.-Y.Chung,“Integratedactiveandreactivepowercon-
S.Callaway,andS.Sanders,“Revisitingpowersystemstime-domain trolmethodsfordistributedenergyresourcesindistributionsystems
simulationmethodsandmodels,”IEEETrans.PowerSyst.,vol.39, forenhancinghostingcapacity,”Energies,vol.17,no.7,2024,Art.
no.2,pp.2421–2437,Mar.2024. no.1642.
VOLUME7,2026 1109

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
[82] NorthAmericanElectricReliabilityCorporation(NERC),“Character- [106] Y. Fu, W. Zuo, M. Wetter, J. W. VanGilder, X. Han, and D. Pla-
isticsandrisksofemerginglargeloads,”2025.Accessed:Jan.5,2026. mondon, “Equation-based object-oriented modeling and simulation
[Online].Available:https://tinyurl.com/3jw5xyyh for data center cooling: A case study,” Energy Buildings, vol. 186,
[83] C.Jin,X.Bai,C.Yang,W.Mao,andX.Xu,“Areviewofpowercon- pp.108–125,2019.
sumptionmodelsofserversindatacenters,”Appl.Energy,vol.265, [107] M.Gheni,H.Kerskes,andK.Stergiaropoulos,“Operationalanalysis
2020,Art.no.114806. ofthecoolingsysteminadirectliquid-cooleddatacenter:Ameasure-
[84] H.AnandX.Ma,“Dynamiccouplingreal-timeenergyconsumption mentandsimulationstudyontheimpactofsupplywatertemperature,”
modelingfordatacenters,”EnergyRep.,vol.8,pp.1184–1192,2022. Appl.Energy,vol.403,2026,Art.no.127061.
[85] Y.Nasser,J.Lorandel,J.-C.Prévotet,andM.Hélard,“RTLtotran- [108] S.Qu,K.Duan,Y.Guo,Y.Feng,C.Wang,andZ.Xing,“Real-time
sistorlevelpowermodelingandestimationtechniquesforFPGAand optimizationoftheliquid-cooleddatacenterbasedoncoldplatesun-
ASIC: A survey,” IEEE Trans. Comput.-Aided Des. Integr. Circuits derdifferentambienttemperaturesandthermalloads,”Appl.Energy,
Syst.,vol.40,no.3,pp.479–493,Mar.2021. vol.363,2024,Art.no.123101.
[86] J.Yang,L.Ma,K.Zhao,Y.Cai,andT.-F.Ngai,“Earlystagereal-time [109] J.Paananen,“Grid-interactivedatacentersenablingenergytransition:
SoCpowerestimationusingRTLinstrumentation,”inProc.20thAsia Datacenter’shiddenpotentialtoprovideessentialgridservicesofa
SouthPacificDesignAutom.Conf.,2015,pp.779–784. futurepowersystem,”IEEEElectrific.Mag.,vol.11,no.3,pp.26–34,
[87] Z.Xieetal.,“Apollo:Anautomatedpowermodelingframeworkfor Sep.2023.
runtimepowerintrospectioninhigh-volumecommercialmicroproces- [110] A. J. Hutchinson et al., “A comprehensive review of modeling ap-
sors,”inProc.54thAnnu.IEEE/ACMInt.Symp.Microarchitecture, proachesforgrid-connectedenergystoragetechnologies,”J.Energy
2021,pp.1–14. Storage,vol.109,2025,Art.no.115057.
[88] K. O’Neal and P. Brisk, “Predictive modeling for CPU, GPU, and [111] S. G. Jayasinghe, L. Meegahapola, N. Fernando, Z. Jin, and J. M.
FPGAperformanceandpowerconsumption:Asurvey,”inProc.IEEE Guerrero,“Reviewofshipmicrogrids:Systemarchitectures,storage
Comput.Soc.Annu.Symp.VLSI,2018,pp.763–768. technologiesandpowerqualityaspects,”Inventions,vol.2,2017,Art.
[89] Y.Zhou,H.Ren,Y.Zhang,B.Keller,B.Khailany,andZ.Zhang,“Pri- no.4.
mal:Powerinferenceusingmachinelearning,”inProc.Des.Automat. [112] A. J. Hutchinson and D. T. Gladwin, “Flywheel energy storage for
Conf.,2019,pp.1–6. ancillary services: A novel design and simulation of a continuous
[90] A. K. A. Kumar, S. Al-Salamin, H. Amrouch, and A. Gerst- frequency response service for energy limited assets,” IEEE Open
lauer, “Machine learning-based microarchitecture-level power mod- AccessJ.PowerEnergy,vol.11,pp.434–445,2024.
eling of CPUs,” IEEE Trans. Comput., vol. 72, no. 4, pp.941–956, [113] L. K. Gan, J. Reniers, and D. Howey, “A hybrid vanadium
Apr.2023. redox/lithium-ion energy storage system for off-grid renewable
[91] “CPUvsGPU:Howtheyworkandwhentousethem,”DataCamp. power,”inProc.IEEEEnergyConvers.Congr.Expo.,2017,pp.1016–
Accessed: Feb. 1, 2026. [Online]. Available: https://www.datacamp. 1023.
com/blog/cpu-vs-gpu [114] M.TekinandM.˙IhsanKaramangil,“Comparativeanalysisofequiv-
[92] Y.Chitkara,“Areviewonstatisticalpowermodellingforagraphics alentcircuitbatterymodelsforelectricvehiclebatterymanagement
processingunit(GPU),”inProc.6thInt.Conf.IoTSoc.,Mobile,Anal. systems,”J.EnergyStorage,vol.86,2024,Art.no.111327.
Cloud,2022,pp.327–330. [115] R. Xu, “Lithium-ion battery modeling and SoC estimation: Degree
[93] V. Kandiah et al., “AccelWattch: A power modeling framework for projectinelectricpowerengineering(TELPM),secondcycle,30cred-
modernGPUs,”inProc.54thAnnu.IEEE/ACMInt.Symp.Microar- its,”MasterThesis,SchoolElect.Eng.Comput.Sci.,KTHRoy.Inst.
chit.,2021,pp.738–753. Technol.,Stockholm,Sweden,Jun.2023.
[94] G.Alavani,J.Desai,S.Saha,andS.Sarkar,“Programanalysisand [116] A.BhattacharjeeandH.Saha,“Designandexperimentalvalidationof
machine learning–based approach to predict power consumption of ageneralisedelectricalequivalentmodelofvanadiumredoxflowbat-
CUDA kernel,” ACM Trans. Model. Perform. Eval. Comput. Syst., teryforinterfacingwithrenewableenergysources,”J.EnergyStorage,
vol.8,pp.1–24,2023. vol.13,pp.220–232,2017.
[95] Y.LiandY.Li,“AIloaddynamics—Apowerelectronicsperspective,” [117] S.Nejad,D.T.Gladwin,andD.A.Stone,“Asystematicreviewof
2025,arXiv:2502.01647. lumped-parameterequivalentcircuitmodelsforreal-timeestimation
[96] M. S. I. Ovi, “A study on distributed strategies for deep learning oflithium-ionbatterystates,”J.PowerSources,vol.316,pp.183–196,
applicationsinGPUclusters,”2025,arXiv:2505.12832. 2016.
[97] T.AvidorandN.Tal-Israel,“Locallyasynchronousstochasticgradient [118] M. T. Castro and J. D. Ocon, “Development of chemistry-specific
descentfordecentraliseddeeplearning,”2022,arXiv:2203.13085. battery energy storage system models using combined multiphysics
[98] S. Wang, J. Geng, and D. Li, “Impact of synchronization topol- andreducedordermodeling,”J.EnergyStorage,vol.54,2022,Art.
ogy on DML performance: Both logical topology and physical no.105305.
topology,” IEEE/ACM Trans. Netw., vol. 30, no. 2, pp. 572–585, [119] F.Bovera,M.Spiller,M.Zatti,G.Rancilio,andM.Merlo,“Devel-
Apr.2022. opment,validation,andtestingofadvancedmathematicalmodelsfor
[99] Australian Energy Market Operator (AEMO), “2025 transition the optimization of BESS operation,” Sustain. Energy, Grids Netw.,
plan for system security.” Accessed: Jan. 6, 2026. [Online]. vol.36,2023,Art.no.101152.
Available: https://www.aemo.com.au/-/media/files/major- [120] R.Nebulonietal.,“Ahierarchicaltwo-levelMILPoptimizationmodel
publications/tpss/2025-transition-plan-for-system-security.pdf?rev= for the management of grid-connected BESS considering accurate
0984b6183240456bbc85bfaaa12fec62&sc_lang=en physicalmodel,”Appl.Energy,vol.334,2023,Art.no.120697.
[100] A.Muhammad,A.Kalwar,andK.Mekhilef,“Review:Uninterruptible [121] P. A. Lombardi, K. R. Moreddy, A. Naumann, P. Komarnicki, C.
powersupply(UPS)system,”RenewableSustain.EnergyRev.,vol.58, Rodio, and S. Bruno, “Data centers as active multi-energy systems
pp.1395–1410,2016. forpowergriddecarbonization:Atechnicalandeconomicanalysis,”
[101] K. Shi and D. Xu, “Operation and control of uninterruptible power Energies,vol.12,2019,Art.no.4182.
supplysystem,”inControlofPowerElectronicConvertersandSys- [122] S.Ashraf,O.Hasan,I.Evkay,U.S.Selamogullari,andM.Baysal,
tems.NewYork,NY,USA:Elsevier,2024,pp.457–509. “Recenttrendsanddevelopmentsinprotectionsystemsformicrogrids
[102] LiebertEXM2UserManual:100kVAto250kVAUPS,VertivGroup incorporatingdistributedgeneration,”WileyInterdiscipl.Rev.:Energy
Corp.,Westerville,OH,USA,2024. Environ.,vol.13,no.4,2024,Art.no.e532.
[103] VertivTM Liebert EXL S1 UPS: 300–1200 kW, Vertiv Group Corp., [123] K.Kumar,P.Kumar,andS.Kar,“Areviewofmicrogridprotection
Westerville,OH,USA,2024. for addressing challenges and solutions,” Renewable Energy Focus,
[104] Y. Wang, “Data center integrated energy system for sustainability: vol.49,2024,Art.no.100572.
Generalization,approaches,methods,techniques,andfutureperspec- [124] ElectricReliabilityCouncilofTexas(ERCOT),“Largeloads—Impact
tives,”Innov.Energy,vol.1,no.1,2024,Art.no.100014. on grid reliability and overview of revision request package,”
[105] Y.Fu,W.Zuo,M.Wetter,J.W.VanGilder,andP.Yang,“Equation- Aug. 2023. Accessed: Jan. 6, 2026. [Online]. Available:
basedobject-orientedmodelingandsimulationofdatacentercooling https://www.ercot.com/files/docs/2023/11/08/PUBLIC-Overview-of-
systems,”EnergyBuildings,vol.198,pp.503–519,2019. Large-Load-Revision-Requests-for-8-16-23-Workshop.pptx
1110 VOLUME7,2026

[125] M. Kumar, “Data centres as “virtual power plants”: Emerging [146] C. Mishra, L. Vanfretti, J. Delaree Jr, T. Purcell, and K. D. Jones,
grid code requirements,” Smart Grid Analytics, Oct. 2025, Ac- “Understandingtheinceptionof14.7Hzoscillationsemergingfrom
cessed: Jan. 6,2026.[Online].Available:https://sgrids.com/images/ adatacenter,”Sustain.Energy,GridsNetw.,vol.43,2025,Art.no.
DataCentresasVPP.pdf 101735.
[126] CommissionforRegulationofUtilities(CRU),“Largeenergyusers [147] R. O’Keefe, “Event records showing data center response to
connectionpolicy,”CommissionforRegulationofUtilities,Dublin, faults,” 2025. Accessed: Jan. 3, 2026. [Online]. Available: https:
Ireland,Tech.Rep.CRU/2025236,2025. //www.nerc.com/comm/RSTC/LLTF/LLTF\%20April\%20Meeting\
[127] A.B.Nassif,Y.Wang,andI.R.Pordanjani,“Powerqualitycharac- %20&\%20Technical\%20Workshop\%20Presentations.pdf
teristicsandelectromagneticcompatibilityofmoderndatacentres,”in [148] M. Parker and B. Sterling, “Unplanned data center load transfer
Proc.IEEECan.Conf.Elect.Comput.Eng.,2018,pp.1–4. update,” 2025. Accessed: Jan. 3, 2026. [Online]. Available:
[128] M. Ingram, R. Mahmud, and D. Narang, “Background information https://www.nerc.com/comm/RSTC/LLTF/LLTF\%20June\
on the power quality requirements in IEEE Std 1547-2018,” Nat. %20Workshop\%20Presentations.pdf
Renewable Energy Lab., Golden, CO, USA, Tech. Rep. NREL/TP- [149] K.-B. Kwon, S. Mukherjee, and V. Adetola, “Operational risks in
5D00-78751,2021. grid integration of large data center loads: Characteristics, stability
[129] Energy Systems Integration Group, “Large load interconnection assessments,andsensitivitystudies,”2025,arXiv:2510.05437.
performance requirements,” 2026. Accessed: May 21, 2026. [On- [150] A.S.AkinyemiandI.E.Davidson,“Impactofrenewableenergygen-
line]. Available: https://www.esig.energy/reports-briefs/large-load- erationonvoltageflickerwithdynamicloadconnectedtodistribution
interconnection-performance-requirements/ network,”Int.J.Appl.Eng.Res.,vol.14,pp.3137–3145,2019.
[130] G.Wollam,A.Lewis,andF.Jahanbakhsh,“Guidelineforverifying [151] K.M.U.Ahmed,M.H.J.Bollen,M.Alvarez,andS.S.Letha,“The
IEEEharmoniccompliance,”inProc.IEEEPowerEnergySoc.Gen. impacts of voltage disturbances due to faults in the power supply
Meeting,2025,pp.1–5. systemofadatacenter,”inProc.20thInt.Conf.Harmon.Qual.Power,
[131] SouthwestPowerPool(SPP),“Highimpactlargeloadride-through 2022,pp.1–6.
requirements”SPPOperationsPlanning,PolicyRes.Team,Jul.2025. [152] T. Shioda, “Voltage fluctuation/flicker international standards and
[Online]. Available: https://www.spp.org/documents/74635/spp\ measurementtechniques,”YokogawaTest&MeasurementCorpora-
%20hill\%20fault\%20ride\%20through\%20requirements-v1.0-8- tion,IEC61000-3-3andIEC61000-3-11overview,2021.
19-2025\%20(updated\%20version).docx [153] Y.Xie,W.Cui,andA.Wierman,“Enhancingdatacenterlow-voltage
[132] M.-S. Ko and H. Zhu, “Wide-area power system oscillations from ride-through,”2025,arXiv:2510.03867.
large-scaleAIworkloads,”IEEETrans.PowerSyst.,2026(inpress). [154] M.Ahmed,L.Meegahapola,A.Vahidnia,andM.Datta,“Stabilityand
[133] R. Zahedi, A. Zamani, and R. Anilkumar, “Best practices for large controlaspectsofmicrogridarchitectures—Acomprehensivereview,”
loadinterconnections:ANorthAmericanperspectiveondatacenters,” IEEEAccess,vol.8,pp.144730–144766,2020.
2026,arXiv:2601.12686. [155] North American Electric Reliability Corporation (NERC), “NERC
[134] M.J.Culler,R.V.Stolworthy,A.Tylecote,J.Kmiec,T.Ponto,andL. incident review considering simultaneous voltage-sensitive load
Martin,“Digitalassuranceforgridreliabilityintheeraoflargeload reductions,”NorthAmericanElectricReliabilityCorporation,2025.
growth,”IdahoNat.Lab.,IdahoFalls,ID,USA,Tech.Rep.INL/RPT- [Online]. Available: https://www.nerc.com/pa/rrm/ea/Documents/
26-90975,2026. Incident_Review_Large_Load_Loss.pdf
[135] B.A.RossandJ.D.Follum,“Electromagnetictransientmodelingof [156] M. Lauby, “NERC activities and plans to address reliability
largedatacentersforgrid-levelstudies,”PacificNorthwestNat.Lab., impacts from large load integration,” presented at FERC Open
Richland,WA,USA,Tech.Rep.PNNL-38817,2026. Meeting,2025.Accessed:Apr.17,2025.[Online].Available:https:
[136] A.Peivandizadeh,“Atheoreticalframeworkforvirtualpowerplant //www.ferc.gov/sites/default/files/2025-04/Presentation\%20NERC\
integrationwithgigawatt-scaleaidatacenters:Multi-timescalecontrol %20Seeks\%20to\%20Address\%20Reliability\%20Impacts\
andstabilityanalysis,”2025,arXiv:2506.17284. %20from\%C2\%A0Large\%20Load\%20Integration_1.pdf
[137] Siemens Energy, “E-STATCOM—SVC plus frequency sta- [157] G.Murray,M.N.Johnstone,andC.Valli,“TheconvergenceofITand
bilizer,” 2026. Accessed: Jan. 2, 2026. [Online]. Available: OTincriticalinfrastructure,”inProc.15thAust.Inf.Secur.Manage.
https://www.siemens-energy.com/global/en/home/products- Conf.,2017,pp.149–155.
services/product/svcplus-frequency-stabilizer.html [158] I.Paredes,“IT/OTconvergence—Cybersecuritybeyondtechnology,”
[138] M.-S.Ko,J.W.Shim,andH.Zhu,“Mitigationofdatacenterdemand inProc.AbuDhabiInt.PetroleumExhib.Conf.,2020,Art.no.SPE-
rampingandfluctuationusinghybridESSandsupercapacitor,”2025, 203093-MS.
arXiv:2512.08076. [159] Y.Fu,X.Han,K.Baker,andW.Zuo,“Assessmentsofdatacentersfor
[139] Bloomberg News, “AI power needs threaten billions in damages provisionoffrequencyregulation,”Appl.Energy,vol.277,2020,Art.
for US households,” 2024. Accessed: Jan. 5, 2026. [Online]. no.115621.
Available: https://www.bloomberg.com/graphics/2024-ai-power- [160] E.Nasr,“Grid-interactivedatacenters:Enablingdecarbonizationand
home-appliances/ systemstability,”Eaton,Dublin,Ireland,Tech.Rep.,2021.
[140] H. Zubi and N. Hfouda, “Measurement-based data center complete [161] Sympower,“Seabirddataservices—Thedatacentrebecomingaflexi-
loadmodelconstruction&powerqualityassessment atdistribution bilitypowerhouse,”2026.Accessed:Jan.9,2026.[Online].Available:
level,” in Proc. IEEE 4th Int. Maghreb Meeting Conf. Sci. Techn. https://sympower.net/case-studies/seabird-data-services-sympower
Autom.ControlComput.Eng.,2024,pp.333–340. [162] X.TaoandR.Gadh,“Fastfrequencyresponsepotentialofdatacenters
[141] Dynamic Ratings, “Managing harmonic distortion from data throughworkloadmodulationandUPScoordination,”IEEEAccess,
centers,” 2026. Accessed: Jan. 6, 2026. [Online]. Available: vol.13,pp.214511–214519,2025.
https://www.dynamicratings.com/managing-harmonic-distortion- [163] D.AlKez,A.M.Foley,F.W.Ahmed,M.O’Malley,andS.Muyeen,
from-data-centers/ “Potentialofdatacentersforfastfrequencyresponseservicesinsyn-
[142] N.Hatziargyriouetal.,“Definitionandclassificationofpowersystem chronouslyisolatedpowersystems,”RenewableSustain.EnergyRev.,
stability—Revisited&extended,”IEEETrans.PowerSyst.,vol.36, vol.151,2021,Art.no.111547.
no.4,pp.3271–3281,Jul.2021. [164] P.Ren,W.Sun,Y.Wang,andG.Harrison,“Gridfrequencystability
[143] S.Morovatietal.,“Strengtheningdatacenteroperationsthroughbat- supportpotentialofdatacenter:Aquantitativeassessmentofflexibil-
teryenergystoragesystems,”2025.[Online].Available:https://ssrn. ity,”IEEETrans.Ind.Appl.,2026.
com/abstract=5583916 [165] S. M. Ali et al., “An ancillary services model for data centers and
[144] T. Kerçi, C. Duggan, U. Farooq, S. Tweed, and M. Val vEscudero, powersystems,”IEEETrans.CloudComput.,vol.8,no.4,pp.1176–
“Impactofconverter-baseddemandonfrequencyqualityintheIreland 1188,Oct.–Dec.2020.
andnorthernIrelandpowersystems,”inProc.CIGREParisSession, [166] Svenskakraftnät,“Finalreport:Pilotprojectindemandresponseand
Paris,France,Aug.2024,pp.213–247. energy storage,” Svenska Kraftnät, Stockholm, Sweden, Tech. Rep.
[145] S. Zhang et al., “Grid modernization in the age of artificial intel- SVK3551,2018.
ligence and cloud: Synergies between grid modernization, artificial [167] T. Raggi, “Understanding AI power demands: How standard Vertiv
intelligence, and cloud,” IEEE Power Energy Mag., vol. 23, no. 5, UPSsystemssupportAIfactoryloaddynamics,”Vertiv,Westerville,
pp.102–116,Sep./Oct.2025. OH,USA,Sep.2025.
VOLUME7,2026 1111

GYANGETAL.:GRID-INTEGRATEDDATACENTERS
[168] C.CrozierandM.Liska,“Thepotentialofdatacenterenergydemand PRATYUSH CHAKRABORTY (Senior Member,
to provide grid flexibility,” Curr. Sustain./Renewable Energy Rep., IEEE)receivedtheB.E.degreeinelectricalengi-
vol.12,no.1,pp.1–6,2025. neeringfromJadavpurUniversity,Kolkata,India,
[169] DatacenterDynamics,“Googlesignsfirstlongdurationenergystorage in 2006, the M.Tech. degree in electrical engi-
partnership,” 2026. Accessed: Jan. 12, 2026. [Online]. Available: neering from the Indian Institute of Technology
https://www.datacenterdynamics.com/en/news/google-signs-first- Bombay,Mumbai,India,in2011,andtheM.S.and
long-duration-energy-storage-partnership/ Ph.D.degreesinelectricalandcomputerengineer-
[170] DatacenterDynamics,“Microsoftreplacesdieselswithbatterysystem ingfromtheUniversityofFlorida,Gainesville,FL,
at swedish data center,” 2023. Accessed: Jan. 12, 2026. [Online]. USA,in2013and2016,respectively.
Available: https://www.datacenterdynamics.com/en/news/microsoft- From 2006to 2009, he worked in projects for
replaces-diesels-with-battery-system-at-swedish-data-center/ Siemens Limited, Mumbai, India. From 2017 to
[171] S. Kundu, K. Chatterjee, R. R. Hossain, S. P. Nandanoori, and V. 2020, he was a Postdoctoral Researcher with the University of California,
Adetola,“Managingrisksfromlargedigitalloadsusingcoordinated Berkeley,CA,USA;NorthwesternUniversity,Evanston,IL,USA;andthe
grid-forming storage network,” Proc. IEEE/PES Transmis. Distrib. UniversityofUtah,SaltLakeCity,UT,USA.HeiscurrentlyanAssociate
Conf.Exposit.,Chicago,IL,USA,2026,pp.1–5. Professor with the Department of Electrical and Electronics Engineering,
[172] D.AlKez,A.Foley,andF.Ahmed,“Datacenterpotentialflexibil- BITSPilani,Hyderabad,India.Hisresearchinterestsincludegametheory,
itiesandchallengesfordemandresponsetofacilitate100%variable optimization, control theory, and their applications to power systems with
renewable generation: A review,” 2024. [Online]. Available: https: deeprenewablepenetration.
//ssrn.com/abstract=5101561
| [173] J. Roach, | “Hydrogen |     | fuel cells | could | provide | emission | free backup |     |     |     |     |     |     |     |
| --------------- | --------- | --- | ---------- | ----- | ------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
poweratdatacenters,Microsoftsays,”2022.Accessed:Oct.13,2026. LASANTHA MEEGAHAPOLA (Senior Member,
| [Online]. | Available: |     | https://news.microsoft.com/innovationstories/ |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IEEE)receivedthePh.D.degreeinelectricalengi-
hydrogen-fuel-cells-could-provide-emission-free-backup-power-at-
neeringfromQueen’sUniversityBelfast,Belfast,
datacentersmicrosoft-says/
U.K.,in2010.
[174] Siemens Energy, “World’s first e-statcom,” 2026. Accessed: Jan. From2009to2010,hewasavisitingResearcher
13, 2026. [Online]. Available: https://www.sechsa.com/featured/ with the Electricity Research Centre, University
worlds-first-e-statcom/
|     |     |     |     |     |     |     |     |     |     | College | Dublin, Dublin, | Ireland. | From | 2011 to |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | -------- | ---- | ------- |
[175] S.Mohanty,A.Das,andB.Singh,“Fault-tolerantcascadedH-bridge
|     |     |     |     |     |     |     |     |     |     | 2014, | he was a Lecturer | with | the | University of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----------------- | ---- | --- | ------------- |
basedenhanced-STATCOMinapowerelectronicsdominatedgrid,”in Wollongong, Wollongong, NSW, Australia, and
Proc.IEEE11thPowerIndiaInt.Conf.,2024,pp.1–6. continuesasaSeniorHonoraryFellow.Heiscur-
[176] C.Jiangetal.,“Optimalpricingstrategyfordatacenterconsidering
rentlyaProfessorofElectricalPowerSystemswith
| demand | response | and | renewable | energy | source | accommodation,” |     | J.  |     |     |     |     |     |     |
| ------ | -------- | --- | --------- | ------ | ------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
RMITUniversity,Melbourne,VIC,Australia.Hehasmorethan18yearsof
ModernPowerSyst.CleanEnergy,vol.11,no.1,pp.345–354,2021.
researchexperienceinpowersystemdynamicsandstabilitywithrenewable
[177] GoogleCloud,“Usingdemandresponsetoreducedatacenterpower powergenerationandhasauthoredorcoauthoredmorethan230journaland
| consumption,” |     | 2026. | Accessed: | Jan. | 13, 2026. | [Online]. | Available: | conferencearticles. |     |     |     |     |     |     |
| ------------- | --- | ----- | --------- | ---- | --------- | --------- | ---------- | ------------------- | --- | --- | --- | --- | --- | --- |
https://cloud.google.com/blog/products/infrastructure/using-demand-
|     |     |     |     |     |     |     |     | Dr. Meegahapola |     | is an Associate | Editor | for IEEE | TRANSACTIONS | ON  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | ------ | -------- | ------------ | --- |
response-to-reduce-data-center-power-consumption
POWERSYSTEMS,IEEEPOWERENGINEERINGLETTERS,andIEEETRANS-
[178] BloombergNEF,“Datacentersanddecarbonization:Unlockingflex-
ACTIONSONINDUSTRYAPPLICATIONS.HeisaMemberoftheIEEEPower
ibility in Europe’s data centers,” Bloomberg New Energy Finance, EngineeringSociety(PES)andtheIEEEIndustrialElectronicsSociety.Heis
London,U.K.,Tech.Rep.,Oct.2021. alsoanactiveMemberoftheIEEEPESPowerSystemDynamicPerformance
[179] M.Chenetal.,“Aggregatedmodelofdatanetworkfortheprovisionof
|     |     |     |     |     |     |     |     | Committee | Task Forces | on“Microgrid | Stability | Definitions, |     | Analysis, and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------------ | --------- | ------------ | --- | ------------- |
demandresponseingenerationandtransmissionexpansionplanning,”
Modeling”and“MicrogridDynamicModeling.”
IEEETrans.SmartGrid,vol.12,no.1,pp.512–523,Jan.2021.
[180] J.Ahmadi,A.ToroghiHaghighat,A.M.Rahmani,andR.Ravanmehr,
“Aflexibleapproachforvirtualmachineselectioninclouddatacenters
withAHP,”Softw.:Pract.Exp.,vol.52,no.5,pp.1216–1241,2022. XINGHUOYU(Fellow,IEEE)receivedtheB.Eng.
[181] R. Awati, “What is dynamic voltage and frequency scaling and M.Eng. degrees in electrical and electronic
|     |     |     |     |     |     |     |     |     |     | engineering | from the | University | of  | Science and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ---------- | --- | ----------- |
(DVFs)?”TechTarget,2024.Accessed:Jan.14,2026.[Online].Avail-
|       |                                                               |     |     |     |     |     |     |     |     | Technology | of China, | Hefei, | China, | in 1982 and |
| ----- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------ | ------ | ----------- |
| able: | https://www.techtarget.com/whatis/definition/dynamic-voltage- |     |     |     |     |     |     |     |     |            |           |        |        |             |
1984,respectively,andthePh.D.degreeincontrol
and-frequency-scaling-DVFS
[182] Z.Zhao,B.Austin,E.Rrapaj,andN.J.Wright,“UnderstandingVASP science and engineering from Southeast Univer-
powerprofilesonNVIDIAA100GPUs,”inProc.SC24-W:Workshops sity,Nanjing,China,in1988.
|     |     |     |     |     |     |     |     |     |     | He  | is currently | a Distinguished | Professor | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------------- | --------- | --- |
Int.Conf.HighPerform.Comput.,Netw.,StorageAnal.,Atlanta,GA,
anAssociateDeputyVice-ChancellorwithRMIT
USA,2024,pp.1496–1505.
|     |     |     |     |     |     |     |     |     |     | University, | Melbourne, | VIC, | Australia. | His re- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---- | ---------- | ------- |
searchinterestsincludecontrolsystems,complex
|     |     | PAM | PAUL | GYANG | (Student | Member, | IEEE) |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | ----- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
andintelligentsystems,andpowerandenergysystems.
receivedtheB.Eng.degreeinelectricalandelec- Dr. Yu received a number of awards and honors for his contributions,
tronicsengineering(powersystems)fromtheFed- includingthe2013Dr.-Ing.EugeneMittelmannAchievementAwardofthe
|     |     | eral | University | of  | Technology, | Owerri, | Nigeria, |     |     |     |     |     |     |     |
| --- | --- | ---- | ---------- | --- | ----------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
IEEEIndustrialElectronicsSocietyandthe2018M.A.SargentMedalfrom
|     |     | in  | 2015, and | the | M.Sc. degree | in  | electrical and |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
EngineersAustralia.HewasanAssociateEditorforIEEETRANSACTIONS
electronicsengineering(electricalpower)fromthe ONAUTOMATICCONTROL,IEEETRANSACTIONSONCIRCUITSANDSYSTEMS
UniversityofLagos,Akoka,Nigeria,in2020.He I: REGULAR PAPERS, IEEE TRANSACTIONS INDUSTRIAL ELECTRONICS,
ON
is currently working toward the Cotutelle (joint- IEEETRANSACTIONSONINDUSTRIALINFORMATICS,andseveralotherjour-
supervision)Ph.D.degreeinelectricalengineering
nals.HewasthePresidentoftheIEEEIndustrialElectronicsSocietyin2018
|     |     | with | the | Birla Institute | of  | Technology | and Sci- |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --------------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
and2019.HeisaFellowoftheAustralianAcademyofScience,anHonorary
ence, Hyderabad, India, and RMIT University, FellowoftheInstitutionofEngineersAustralia,andaFellowofInternational
| Melbourne,VIC,Australia. |          |             |              |             |           |        |              | FederationofAutomaticControl. |     |     |     |     |     |     |
| ------------------------ | -------- | ----------- | ------------ | ----------- | --------- | ------ | ------------ | ----------------------------- | --- | --- | --- | --- | --- | --- |
| From 2018                | to 2023, | he          | was an       | Engineering | Standards |        | and Research |                               |     |     |     |     |     |     |
| Specialist               | with Eko | Electricity | Distribution |             | Company,  | Lagos, | Nigeria. His |                               |     |     |     |     |     |     |
researchinterestsincludepowersystemstabilityanddynamics,demandre-
sponseandflexibleloadcontrol,dynamicmodelingofgrid-interactivedata
centers,andstabilityassessmentofrenewableenergydominatedpowersys-
tems.
| 1112 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |