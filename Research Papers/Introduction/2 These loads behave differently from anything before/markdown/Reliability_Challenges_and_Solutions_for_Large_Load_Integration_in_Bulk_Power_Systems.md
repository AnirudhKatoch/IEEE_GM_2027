| Reliability |     |             | Challenges |      |       |     | and  | Solutions |     |         | for        | Large |     | Load |     |
| ----------- | --- | ----------- | ---------- | ---- | ----- | --- | ---- | --------- | --- | ------- | ---------- | ----- | --- | ---- | --- |
|             |     | Integration |            |      |       | in  | Bulk | Power     |     | Systems |            |       |     |      |     |
|             |     |             |            | Eric | Meier |     |      |           |     | Sagnik  | Basumallik |       |     |      |     |
61026511.6202.22084DT/9011.01 :IOD | EEEI 6202© 00.13$/62/6-9655-5133-8-979 | )D&T( noitisopxE dna ecnerefnoC noitubirtsiD dna noissimsnarT SEP/EEEI 6202
Electric Reliability Council of Texas New York Power Authority
|     |     |     |                      | Taylor, | TX  |     |     |     |                            | Albany, | NY  |     |     |     |     |
| --- | --- | --- | -------------------- | ------- | --- | --- | --- | --- | -------------------------- | ------- | --- | --- | --- | --- | --- |
|     |     |     | eric.meier@ercot.com |         |     |     |     |     | sagnik.basumallik@nypa.gov |         |     |     |     |     |     |
Abstract—The increasing number of Large Loads, such as Large Loads is presented. These include (a) impacts on Large
| data centers | and        | cryptocurrency     |       | miners, | is         | introducing | new           |                  |              |            |        |        |            |            |         |
| ------------ | ---------- | ------------------ | ----- | ------- | ---------- | ----------- | ------------- | ---------------- | ------------ | ---------- | ------ | ------ | ---------- | ---------- | ------- |
|              |            |                    |       |         |            |             |               | Loads due        | to incidents |            | in BPS | and    | (b) impact | on         | the BPS |
| reliability  | challenges | for                | Bulk  | Power   | Systems    | (BPS).      | As seen       |                  |              |            |        |        |            |            |         |
|              |            |                    |       |         |            |             |               | due to incidents |              | involving  | Large  | Loads. | Further,   | a taxonomy |         |
| in recent    | industry   | events,            | these | loads   | have       | become      | significant   |                  |              |            |        |        |            |            |         |
|              |            |                    |       |         |            |             |               | is introduced    | that         | classifies | Large  | Load   | risks      | by root    | causes  |
| contributors | to         | customer-initiated |       | load    | reduction, |             | oscillations, |                  |              |            |        |        |            |            |         |
andfrequencytransients.WhiletheseLargeLoadsformthebasis such as equipment design, control strategies, and operational
forourdigitaleconomyandsupportmoderninfrastructure,itis characteristics. Finally, mitigation and design solutions for
| important | that | they do | not adversely |     | impact | the BPS | reliability. |                |     |       |                  |     |      |          |          |
| --------- | ---- | ------- | ------------- | --- | ------ | ------- | ------------ | -------------- | --- | ----- | ---------------- | --- | ---- | -------- | -------- |
|           |      |         |               |     |        |         |              | issues related | to  | Large | Load integration |     | from | both (a) | facility |
ThispaperinvestigatesvariousBPSeventsthatprimarilyinvolve
and(b)gridsidearesystematicallyclassifiedaccordingtotheir
| Large Loads | and     | develops | a taxonomy |     | of root-causes |          | related   | to        |                |     |     |     |     |     |     |
| ----------- | ------- | -------- | ---------- | --- | -------------- | -------- | --------- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
|             |         |          |            |     |                |          |           | scope and | applicability. |     |     |     |     |     |     |
| equipment   | design, | control  | systems,   | and | the            | software | operating |           |                |     |     |     |     |     |     |
these loads. This taxonomy is utilized to guide further research The rest of the paper is organized as follows: Section II
into solutions for these issues, and the paper proposes both provides a background of important characteristics for Large
| facility-level | and | grid-level | mitigation |     | techniques | to  | address the |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ---------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
LoadsrelevanttotheBPSrisks.SectionIIIcoversthegeneral
identified challenges.
|              |            |             |          |       |        |              |            | risks Large  | Loads   | pose | to the BPS | and   | disturbances |               | involving |
| ------------ | ---------- | ----------- | -------- | ----- | ------ | ------------ | ---------- | ------------ | ------- | ---- | ---------- | ----- | ------------ | ------------- | --------- |
| Index        | Terms—Data |             | centers, | Data  | center | power,       | Cryptocur- |              |         |      |            |       |              |               |           |
|              |            |             |          |       |        |              |            | Large Loads. | Section |      | IV covers  | Large | Load         | facility-side |           |
| rency, Power | system     | protection, |          | Power | system | reliability, | Power      |              |         |      |            |       |              |               |           |
system stability mitigation and solutions to these risks, followed by grid-side
mitigationsandsolutionsinSectionV.Finally,theconclusions
|     |     |     |              |     |     |     |     | are presented | in  | Section | VI. |     |     |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- |
|     |     | I.  | INTRODUCTION |     |     |     |     |               |     |         |     |     |     |     |     |
Theelectricpowerindustryisseeinganincreaseindemand, II. BACKGROUNDONLARGELOADS
withdatacentersandcryptocurrencyminersbeingkeydrivers The NERC Large Load Task Force [2] cites data cen-
in load growth [1]. These loads are primarily classified as ters, cryptocurrency mining facilities, hydrogen electrolyzers,
“LargeLoads”,i.e.,loadsthatarelargerthanloadshistorically manufacturing plants, and arc furnaces as examples of Large
connected and can threaten the security of the bulk power Loads. In this paper, we focus on data centers and cryptocur-
system(BPS).TheNERCLargeLoadTaskForcedefinesthese rencyminingfacilities.Datacenterssupportmuchofourmod-
loads as “any commercial or industrial individual load facility ern digital infrastructure, providing compute and storage for
or aggregation of load facilities at a single site behind one or end-users. In recent years, data centers focusing on artificial
more point(s) of interconnection that can pose reliability risks intelligence(AI)modeltrainingandinferenceareincreasingly
to the BPS due to its demand, operational characteristics, or being built. Compared to traditional data centers, these AI
other factors” [2]. There have been numerous reported events data centers generally have a much higher load demand and
where grid disturbances, such as transmission faults, led to a highly variable load pattern [3], [8]. Critically, data centers
customer-initiatedloadreduction[3]–[5].Duringtheseevents, have (a) a power distribution system including power supplies
thevoltagesensitivityofthecomputingandpowerdistribution to convert AC power to DC, and (b) uninterruptible power
equipment played a key role in the initiation of customer load supply (UPS) units that provide short-term battery backup
reduction. These Large Loads have also been the source of capabilities. The power supplies and UPS units are typically
oscillationsthatweredetectedfromtheBPS[6],[7].Toensure
|     |     |     |     |     |     |     |     | designed | to conform | to  | the Information |     | Technology |     | Industry |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------------- | --- | ---------- | --- | -------- |
BPSreliability,itisextremelyimportantthatsystemoperators Council (ITIC) curve or a ride-through curve, which specifies
understand the reliability risks that Large Loads pose so they the voltage limits of computer equipment across time.
can be effectively mitigated. In addition to data centers, cryptocurrency miners are also
The challenges and risks posed by Large Loads to the BPS driving load growth. Cryptocurrencies such as Bitcoin are
are not sufficiently documented and discussed in the existing decentralized currencies on a blockchain where a peer-to-peer
literature. This paper fills the gap by identifying and charac- network maintains a record of transactions, and new coins
terizing these risks and challenges in detail. A comprehensive canbeunlockedthroughcryptocurrencymining.Theseminers
evaluation of various real-life industry incidents involving use specialized computing equipment made with application
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:21 UTC from IEEE Xplore.  Restrictions apply.

TABLEI
IMPACTONLARGE-LOADSDUETOPOWERSYSTEMFAULTS
ID Entity FaultDescription ImpactonLargeLoad MWLoadAffected Remarks
OneDataCenterridesthrough1pfault,1st,2nd,and3rd
Normallycleared138kV
1 AEP phase-to-groundfaults recloseattempt.AnotherDataCentertripsafter2ndrecloseattempt. 68MW Protectionlogicsettotripafter
|     |     |     |     |     | Otherdatacentersridethrough.Crypto-mineridesthrough.      |     |     |     |     |     |     |     | 3voltagedipsoccurringwithin |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
|     |     |     |     |     | OneDataCenterridesthroughinitial1pfault,1strecloseattempt |     |     |     |     |     |     |     | 1minute.Bothdatacenters     |     |     |
Normallycleared138kV
phase-to-groundfaults buttripsafter2ndrecloseattempt.Otherdatacentersridethrough. 80MW andcrypto-minesareconstant
|     |                    |     |     |     |     |     | Crypto-minerodethrough. |     |     |     |     |     | powerloadsduring |                 |     |
| --- | ------------------ | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | ---------------- | --------------- | --- |
|     | 230kVLinelockedout |     |     |     |     |     |                         |     |     |     |     |     |                  | thevoltagedips. |     |
duringastormevent.A Initialloadreductionafterfirstandsecondreclosingshots. 1470MW Protectionlogicsettotripwhenacertain
| 2 Dominion | totalof6reclosingattempts |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with3ateachsubstation Mostloadreductionwasafterthirdreclosingshot. numberofvoltagedisturbancesare
Somedatacentersrodethroughalbeitwithabriefchangeinload. seenwithinacertaintime.Need
|     | 230kVtransmissionlinefault |     |     |     |     |     |     |     |     |     |        |     | high-resolutionmonitoringdata  |     |     |
| --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------------------------ | --- | --- |
|     | threeauto-recloseattempts  |     |     |     |     |     |     |     |     |     | 1800MW |     |                                |     |     |
|     | ateachendoftheline         |     |     |     |     |     |     |     |     |     |        |     | toreviewfacilitiesperformance. |     |     |
Phase-phasefaulton
|     | 220kVline-tripped |     |     |     |     |     |     |     |     |     | 80MW |     | UPSvoltageprotectionsettings |     |     |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---------------------------- | --- | --- |
3 EirGrid Datacentersdisconnectedfromthegrid setto10%fromnominal-data
|     |     | 220kVlinetripped, |     |     |     |     |     |     |     |     |     |     | centersdisconnectwithinmsoffaults. |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- |
reclosedandtripped
|     |     | forasinglephase |     |     |     |     |     |     |     |     | 204MW |     | Faultswereclearedin61ms,then |     |     |
| --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ---------------------------- | --- | --- |
80ms/90ms(reclosetrip)respectively.
togroundfault
|     |     | 220kVreactorfault |     |     |     |     |     |     |     |     | 321MW |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
multipleevents LargeLoadreductionassinglephasevoltagedippedbelow0.7p.u. Needforvalidateddynamicmodelsand
| 4 ERCOT |     |     |     |     |     |     |     |     |     | 107MW-432MW |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
singlephaseand3phasefaults LargeLoadsreductionbelowavoltageof0.75p.u.fora3LGfaulton345kV highresolutionmonitoring.
TABLEII
IMPACTONPOWERSYSTEMDUETOLARGE-LOADS
| ID  | Entity |     |     |     | Event/Issue |     |     |     |     | ImpactonPowerSystem |     |     |     |     |     |
| --- | ------ | --- | --- | --- | ----------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
∼25MWpeaktopeakandwith∼23Hzoscillations
| 1   | ERCOT |     |     | Olderfirmwareissues |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∼10mHz-50mHzfrequencytransients;
dropof5-15%ofnominalsteady-statesystemfrequency;
| 2   | EirGrid | Regular,cyclicalfluctuationsindatacenterdemand |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
systemoscillations;
interactionwithgovernorsandactivepowercontrolfromwind/solar
2 Dominion UnstableUPSinthedatacenter 14.7-14.8Hzoscillations
specific integrated circuits to mine Bitcoins. Miners typically multiple voltage disturbances in rapid succession, or (b) the
display a constant load pattern running at full consumption equipment trips following voltages outside of its ride-through
unless triggered to reduce demand from external factors. capabilities. Some recent examples include:
| Experimental | testing | of  | cryptocurrency |     | miners | such | as S19 |             |     |         |     |         |       |     |             |
| ------------ | ------- | --- | -------------- | --- | ------ | ---- | ------ | ----------- | --- | ------- | --- | ------- | ----- | --- | ----------- |
|              |         |     |                |     |        |      |        | 1) Dominion |     | Energy: | In  | 2024, a | storm | led | to a 230-kV |
Pros has validated that their ride-through curves are similar to transmission permanent line fault that was caused due to the
| the ITIC | curve [9], | [10]. |     |     |     |     |     |            |             |     |           |       |            |     |            |
| -------- | ---------- | ----- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------- | ----- | ---------- | --- | ---------- |
|          |            |       |     |     |     |     |     | failure of | a lightning |     | arrestor, | which | ultimately |     | locked out |
Fromapowersystemreliabilityperspective,itistheinterac-
|             |         |            |        |                 |      |           |          | the line. | There    | were     | three | auto-reclosing |        | actions | performed   |
| ----------- | ------- | ---------- | ------ | --------------- | ---- | --------- | -------- | --------- | -------- | -------- | ----- | -------------- | ------ | ------- | ----------- |
| tion of the | power   | conversion |        | infrastructure, |      | including | power    |           |          |          |       |                |        |         |             |
|             |         |            |        |                 |      |           |          | at each   | end of   | the line | over  | 85 seconds.    | After  | three   | reclosing   |
| supplies    | and UPS | units      | at the | Large           | Load | facility, | with the |           |          |          |       |                |        |         |             |
|             |         |            |        |                 |      |           |          | attempts, | the load | began    | to    | reduce         | demand | and     | transfer to |
BPS that poses one of the most urgent concerns, which we backup generation. It was found that numerous data centers
| seek to investigate |     | in this | paper. |     |     |     |     |                  |            |               |       |                |      |          |           |
| ------------------- | --- | ------- | ------ | --- | --- | --- | --- | ---------------- | ---------- | ------------- | ----- | -------------- | ---- | -------- | --------- |
|                     |     |         |        |     |     |     |     | had a “3-strike” |            | rule          | where | the protection |      | schemes  | count the |
|                     |     |         |        |     |     |     |     | number           | of voltage | disturbances, |       | and            | upon | reaching | three or  |
III. LARGELOADTHREATSTOBULKPOWERSYSTEM
|                  |               |           |              |           |                 |             |            | more strikes,     | they           | switch   | to        | backup        | generation | or        | trip. A total |
| ---------------- | ------------- | --------- | ------------ | --------- | --------------- | ----------- | ---------- | ----------------- | -------------- | -------- | --------- | ------------- | ---------- | --------- | ------------- |
| The rapid        | growth        | and       | operations   |           | of Large        | Load        | facilities |                   |                |          |           |               |            |           |               |
|                  |               |           |              |           |                 |             |            | of 32 substations |                | were     | impacted, | and           | the        | area      | control error |
| pose significant |               | threats   | to the       | BPS,      | especially      | when        | there      | is                |                |          |           |               |            |           |               |
|                  |               |           |              |           |                 |             |            | (ACE) was         | increased      |          | by 1470   | MW            | [3]. In    | a similar | incident      |
| unplanned        | load          | reduction | in           | response  | to transmission |             | faults     |                   |                |          |           |               |            |           |               |
|                  |               |           |              |           |                 |             |            | that occurred     | in             | 2025,    | loads     | from multiple |            | data      | centers were  |
| or voltage       | disturbances. |           | Sudden       | load      | reduction       | from        | the BPS    |                   |                |          |           |               |            |           |               |
|                  |               |           |              |           |                 |             |            | transferred       | off            | the grid | during    | a protection  |            | reclosing | event,        |
| perspective      | can lead      | to        | frequency    | overshoot |                 | and trigger | over-      |                   |                |          |           |               |            |           |               |
|                  |               |           |              |           |                 |             |            | leading           | to an increase |          | in ACE    | by 1800       | MW         | [12].     |               |
| frequency        | protection    | [11].     | Oscillations |           | arising         | from        | the oper-  |                   |                |          |           |               |            |           |               |
ations of these Large Loads and their associated controls can 2) ERCOT: IntheERCOTInterconnection,therehavebeen
numerouseventsoverthepasttwoyearswhereatransmission
| also have | widespread | impacts |     | on power | system | stability. | This |     |     |     |     |     |     |     |     |
| --------- | ---------- | ------- | --- | -------- | ------ | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
section provides an overview of recent large-load events and fault caused reductions in power electronic load demand as
their root causes. the Large Loads did not ride through the resulting voltage
|     |     |     |     |     |     |     |     | disturbance. | It  | was noted | that | the single | line | to ground | faults |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ---- | ---------- | ---- | --------- | ------ |
A. Fault-InducedCustomerInitiatedLoadReduction/Tripping
|     |     |     |     |     |     |     |     | caused | significant | reductions |     | for shallow |     | positive | sequence |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ---------- | --- | ----------- | --- | -------- | -------- |
Customer-initiated load reductions have been observed at voltage dips. In these cases, when the faulted phase was
Large Loads, including data centers and cryptocurrency fa- reduced to below 0.7 p.u., load reduction was seen, and most
cilities, following various normally cleared single-phase or loadreductionwasonlyinthefaultedphase.Someloadswere
phase-to-phase transmission fault events. In these facilities, notedtobemoresensitivetothevoltagedisturbances,asthere
protectionschemesareconfiguredto(a)tripafterexperiencing was a large variance in the load behavior in response to the
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:21 UTC from IEEE Xplore.  Restrictions apply.

Fig.1. TaxonomyoftheRootCausesofLargeLoadInducedBulkPowerSystemRisks
fault [5]. prior to the load consumption decrease; however, there was
3) EirGrid: OntheEirGridtransmissionsystem,therewere an oscillation prior to the decrease. The oscillation magnitude
three normally cleared 220 kV transmission system faults was ≈ 25 MW peak to peak, and the oscillation mode was
(phase-phase fault, single phase to ground fault and reactor ≈ 23 Hz. Another oscillation was also detected with 20
fault) in 2022. These faults led to a transient voltage dip that samples/cycle DFR data showing a ≈ 23 Hz oscillation with
resultedinareductionofdatacenterdemandbetween80MW, ≈ 50 MW peak to peak magnitude on October 28, 2025. At
204MWand321MW.Duetostrictvoltageprotectionsettings consumption below 300 MW, DFR data (at 20 samples/cycle)
(suchasa10%deviationfromnominal),thedatacenterloads showedsignificantharmonicdistortionatthe3rdharmonicbut
were moved to UPS within milliseconds of the faults. The not a 23 Hz oscillation. Following a root cause investigation
powersystemsawafrequencyriseandpositiverateofchange and testing, the cause was determined to be older firmware
offrequency(ROCOF)asaresultofthesignificantimbalance versions on certain equipment. The firmware was updated,
triggered by the demand reduction [4]. which resolved the oscillation and improved the harmonic
4) AEP: OntheAEPtransmissionsystem,therehavebeen distortion, but was still not in compliance with IEEE 519 [7].
| two normally | cleared        | 138 kV  | phase-to-ground    | faults   | in 2025 |                |                 |                       |         |
| ------------ | -------------- | ------- | ------------------ | -------- | ------- | -------------- | --------------- | --------------------- | ------- |
|              |                |         |                    |          |         | D. Transients  | due to Regular, | Cyclical Fluctuations | in Data |
| within the   | area of data   | centers | and cryptocurrency |          | mining  |                |                 |                       |         |
|              |                |         |                    |          |         | Center Digital | Processes       |                       |         |
| facilities.  | These resulted | in      | several facilities | tripping | after   |                |                 |                       |         |
multiplereclosingattempts.Somedatacenterswereidentified EirGrid has reported consistent and sustained frequency
as having a protection scheme that is set to trip after three transients resulting from regular, cyclical fluctuations in data
voltage disturbances occur within one minute. These data center digital processes. These fluctuations cause frequency
jumpsbetween0.01−0.05Hz,withminortransientsoccurring
| centers rode | through | the first | two reclosing | attempts | and |     |     |     |     |
| ------------ | ------- | --------- | ------------- | -------- | --- | --- | --- | --- | --- |
tripped on the third attempt [13]. between 10 mHz and 50 mHz at regular intervals have also
|     |     |     |     |     |     | been observed. | These contribute | to a significant | 5−15% drop |
| --- | --- | --- | --- | --- | --- | -------------- | ---------------- | ---------------- | ---------- |
B. Oscillations due to Instability in Electronic Controllers insteady-statefrequency,andinteractwithfrequencyresponse
Dominion has seen oscillations due to possible interaction mechanisms including governors and active power controls
between an unstable UPS controller and a limiter [6]. While from renewable energy sources [4].
|          |                |     |             |          |     | E. Coordinated | Customer | Initiated Load Reduction |     |
| -------- | -------------- | --- | ----------- | -------- | --- | -------------- | -------- | ------------------------ | --- |
| the site | owner provided | the | information | that the | UPS | is             |          |                          |     |
unstable, no information on what is connected to the site and In AI model training, training jobs can be spread among
the possible reasons were shared. The authors in [6] indicated data centers to distribute the compute load. This is known
thatinstabilitystemmingfromcontrollersforpowerelectronic- as distributed model training. If one data center experiences
| based devices | was responsible |     | for creating | oscillations | in the |               |                   |            |                 |
| ------------- | --------------- | --- | ------------ | ------------ | ------ | ------------- | ----------------- | ---------- | --------------- |
|               |                 |     |              |              |        | a disruption, | then the training | is stopped | at all the data |
range of 14.7−14.8Hz. It was observed that the inclusion of centers. This could lead to a coordinated customer-initiated
hard limiters in controllers, such as under and over excitation load reduction across wide geographic areas. The system
constraints in voltage controllers for equipment protection, operator would have no visibility into this load behavior,
may result in chopped state-space once the system trajectory thus creating the risk of unplanned load reduction leading to
becomesunstable.Thisresultsinlimitcycleswithsignificantly frequency overshoot and overvoltage situations.
| high oscillation | amplitudes. |          |          |          |     |               |                       |                        |           |
| ---------------- | ----------- | -------- | -------- | -------- | --- | ------------- | --------------------- | ---------------------- | --------- |
|                  |             |          |          |          |     | F. Root Cause | Taxonomy              | for Large Load–induced | BPS Risks |
| C. Oscillations  | due to      | Outdated | Firmware | Settings |     |               |                       |                        |           |
|                  |             |          |          |          |     | Based on      | the various real-life | events described,      | a mapping |
ERCOT has seen oscillations related to large power elec- oftherootcausesofLargeLoad-inducedBPSrisksisderived
tronic loads. On October 25, 2024, a Large Load decreased as in Fig. 1. The taxonomy reveals that the root causes are
consumption by 300 MW in 24 seconds. There was no fault found in both the design of equipment and its controls, along
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:21 UTC from IEEE Xplore.  Restrictions apply.

TABLEIII
POTENTIALSOLUTIONSTOVARIOUSLARGELOADISSUES
Solution Fault-InducedLoadReduction Oscillations PowerQuality FrequencyTransients VoltageStability
✓
UPS/PowerSupplyControlSystemsDesign
| ServerSideLoadShaping            |     |     |     |     |     |     | ✓   |     | ✓   |     | ✓   |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UPSandPowerSupplyITICCurveChange |     |     |     |     |     | ✓   |     |     |     |     |     |     | ✓   |
| ProtectionCoordination           |     |     |     |     |     | ✓   |     |     |     |     |     |     |     |
|                                  |     |     |     |     |     | ✓   |     |     |     |     |     |     | ✓   |
Grid-FormingLoads
| AccurateDynamicModels        |     |     |     |     |     | ✓   | ✓   |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ImprovedMonitoring           |     |     |     |     |     |     | ✓   |     | ✓   |     |     |     |     |
| FastResponseAncillaryService |     |     |     |     |     | ✓   |     |     |     |     |     |     |     |
|                              |     |     |     |     |     | ✓   | ✓   |     | ✓   |     | ✓   |     | ✓   |
E-STATCOM
| BESS |     |     |     |     |     | ✓   | ✓   |     | ✓   |     | ✓   |     | ✓   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with the underlying software that the Large Load is operating 2) Coordination between Transmission Protection and Fa-
on. This taxonomy is used to explore both facility-level and cilityProtectionSchemes: AsdocumentedinSectionII,some
grid-level mitigation techniques for the issues identified in ofthecustomer-initiatedloadreductionoccurredduetofacility
the reviewed events. Table III maps the various mitigation protectionschemestransferringtheloadtobackuppowerafter
techniques to address issues due to Large Load integration, countingthreevoltagedisturbancesinaminute.Thesevoltage
which are discussed in the next two sections. disturbances originated from normal transmission re-closing
|     |     |     |     |     |     |     | practices. | Large         | Load | protection | schemes |              | may be updated |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ---- | ---------- | ------- | ------------ | -------------- |
|     |     |     |     |     |     |     | with a     | timing buffer |      | to account | for     | transmission | re-closing     |
IV. FACILITYMITIGATIONANDDESIGNSOLUTIONS
|                  |     |                |     |            |     |     | practices.   | Circuit   | breakers | need  | 40−70  | ms    | to operate, and |
| ---------------- | --- | -------------- | --- | ---------- | --- | --- | ------------ | --------- | -------- | ----- | ------ | ----- | --------------- |
| A. Oscillations, |     | Power Quality, |     | Transients |     |     |              |           |          |       |        |       |                 |
|                  |     |                |     |            |     |     | if the event | detection |          | timer | in the | Large | Load protection |
1) UPS and Power Supply Control System Design: Of the scheme does not account for a breaker timing tolerance, then
known oscillations originating from data centers, all were it may misoperate. If the scheme is set to count a voltage
|           |               |         |     |                |         |        | depression | at 80 | ms with | a ±20 | ms  | tolerance, | then it would |
| --------- | ------------- | ------- | --- | -------------- | ------- | ------ | ---------- | ----- | ------- | ----- | --- | ---------- | ------------- |
| mitigated | with software | updates |     | to the control | systems | of the |            |       |         |       |     |            |               |
UPS units/power supply rectifiers, or by changing the code operate if the voltage depression lasts for 60 ms, which is
of the underlying software that the Large Load is operating within the time frame of the breaker operation. Therefore, the
on. Some of the steps include (a) changing the UPS unit protection schemes should be updated to at least 80−120 ms
inputstagecontrolparameters,(b)modifyingthepowersupply toaccountforbreakeroperationtimingtoreducemisoperation
|                     |     |         |          |          |      |            | rates [12]. | This | change | could | potentially | prevent | data centers |
| ------------------- | --- | ------- | -------- | -------- | ---- | ---------- | ----------- | ---- | ------ | ----- | ----------- | ------- | ------------ |
| rectifier controls, |     | and (c) | reducing | the loop | gain | of the UPS |             |      |        |       |             |         |              |
rectifier power factor correction circuit. from transferring to backup power during events.
|                           |     |     |     |                             |     |     | To reduce | the | total count | of  | normal | events | that can poten- |
| ------------------------- | --- | --- | --- | --------------------------- | --- | --- | --------- | --- | ----------- | --- | ------ | ------ | --------------- |
| 2) ServerSideLoadShaping: |     |     |     | Othersourcesofoscillations, |     |     |           |     |             |     |        |        |                 |
power quality issues, and transients can result in varying tially trigger the Large Load transfer to a backup generation,
demand from Large Loads. To mitigate this, software-based the under-voltage pickup relay settings may be adjusted to
|           |              |               |     |          |      |         | ride through | system | faults. | For | example, | a threshold | currently |
| --------- | ------------ | ------------- | --- | -------- | ---- | ------- | ------------ | ------ | ------- | --- | -------- | ----------- | --------- |
| solutions | that balance | computational |     | programs | with | compute |              |        |         |     |          |             |           |
blocks can be implemented. These solutions can monitor the set at 90% of nominal voltage could potentially be relaxed to
|           |         |     |           |             |     |            | 85% of | nominal | voltage | while | ensuring | no  | damage is caused |
| --------- | ------- | --- | --------- | ----------- | --- | ---------- | ------ | ------- | ------- | ----- | -------- | --- | ---------------- |
| execution | of code | and | the power | consumption |     | of servers |        |         |         |       |          |     |                  |
to optimally schedule jobs executing code in a manner that to low-voltage equipment.
smoothsvariationsintheserverpowerconsumption[8].Power 3) Grid-Forming Loads: Many Large Loads are inverter-
|     |     |     |     |     |     |     | based loads, | which | can | offer | additional | control | capabilities |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | --- | ----- | ---------- | ------- | ------------ |
supply-basedsolutionstoloadsmoothingcouldinvolveadding
energy storage to the power supply, software controls to cap over the load. During a fault, the voltage drops, and the load
the power draw during ramp-ups, and systems to engage transferstobackuppowerandbehavesasapassiveelement.In
processing units with compute jobs to keep the processing contrast, Grid-Forming Loads with a voltage source converter
unit running to perform a controlled down-ramp. interface could be potentially used to regulate and stabilize
|            |              |     |     |     |     |     | the voltage | at the | load | following | a   | disturbance | in an active |
| ---------- | ------------ | --- | --- | --- | --- | --- | ----------- | ------ | ---- | --------- | --- | ----------- | ------------ |
| B. Voltage | Ride-Through |     |     |     |     |     | manner      | [14].  |      |           |     |             |              |
1) UPS and Power Supply Changes: To improve the low- V. GRIDSIDEMITIGATIONANDSOLUTIONS
| voltage ride-through |           | capabilities |     | of Large         | Load | facilities, the |                |     |              |     |            |     |     |
| -------------------- | --------- | ------------ | --- | ---------------- | ---- | --------------- | -------------- | --- | ------------ | --- | ---------- | --- | --- |
|                      |           |              |     |                  |      |                 | A. Oscillation | and | Ride-Through |     | Mitigation |     |     |
| UPS units            | and power | supplies     |     | can be modified. |      | This can be     |                |     |              |     |            |     |     |
done by modifying the ITIC curve to require equipment to Equipment can be deployed on the grid at the point of
withstand even longer faults and lower voltage depressions. interconnection or behind the meter to address Large load-
|         |                |     |      |               |           |     | induced | oscillations, | load | variations, |     | and support | ride-through |
| ------- | -------------- | --- | ---- | ------------- | --------- | --- | ------- | ------------- | ---- | ----------- | --- | ----------- | ------------ |
| To meet | more stringent |     | ITIC | requirements, | equipment | can |         |               |      |             |     |             |              |
be upgraded by changing power supply designs to increase capabilities. These include:
the on-board capacitor sizing, or by installing rack-mounted 1) E-STATCOM: These are static compensation devices
capacitor banks or energy storage. installedinparallelwiththeLargeLoadatorbehindthepoint
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:21 UTC from IEEE Xplore.  Restrictions apply.

of common coupling. They typically have modular multilevel riskstotheBPS,asdocumentedinrecenttransmissionsystem
converters that have integrated energy storage systems such events. This paper categorized the root causes of these risks,
as supercapacitors. These supercapacitors have parallel plates which include fault-induced customer load tripping from in-
with an electrolyte layer in between, and they are designed sufficient Large Load ride-through capabilities and protection
to charge and discharge in milliseconds. The E-STATCOMs system mis-coordination, oscillations from power supply and
are designed to cycle both active and reactive power (for UPS unit controls and old computing firmware, transients
example ±75 MW/MVAR for up to several seconds during from fluctuations in load demand, and coordinated customer-
fault events [15]. This provides a continuous active power initiated load reduction from distributed AI model training.
supply during the transition of the Large Load to the UPS. To address these risks, this paper provides several mitigation
Further, reactive power injection during events also helps approaches that can be implemented both at the Large Load
stabilize system voltage levels. The E-STATCOMS also help facility and on the grid side. These include changes to UPS
smooth alternating load cycles in data centers by injecting or unit and power supply designs, protection coordination, new
absorbing power into the energy storage unit. equipment, grid-forming loads, load shaping, improved moni-
2) Battery Energy Storage Systems (BESS): Similar to su- toring capabilities, and better dynamic models. To this end,
percapacitors,on-sitelargeBESSinparalleltotheLargeLoad further work is needed to address the voltage ride-through
canprovidequickenergyinjectionandwithdrawalcapabilities capabilities of Large Loads, improve dynamic load models,
|     |     |     |     |     |     |     |     | and to characterize |     | how | Large | Loads | operate | to inform | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ----- | ----- | ------- | --------- | --- |
tobalanceloads.BESScanenableloadsmoothingduringdata
center training periods where shifts of several tens of MWs possible risks they pose to the BPS.
| can occur | several | times | in a second. |     | While | such fluctuations |     |     |     |     |     |     |     |     |     |
| --------- | ------- | ----- | ------------ | --- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES
| can cause | local | generation | oscillations, |     | generator-generator |     |     |     |     |     |     |     |     |     |     |
| --------- | ----- | ---------- | ------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
interaction, inter-area oscillations, and voltage flicker, BESS [1] J. D. Wilson, Z. Zimmerman, and R. Gramlich, “Strategic industries
can reduce load variability up to 70% [16]. BESS can also surging: Driving us power demand,” tech. rep., Grid Strategies LLC,
|     |     |     |     |     |     |     |     | December2024. |     | TechnicalReport. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------- | --- | --- | --- | --- | --- |
supportlowvoltageride-throughbymimickingloadsjustafter [2] NERC,“Characteristicsandrisksofemerginglargeloads,”July2025.
voltage recovery, drawing power from the grid for charging Accessed:2025-07-24.
|            |            |              |            |     |       |        |       | [3] North                                                     | American            | Electric | Reliability       | Corporation, | “Incident         |         | review:   |
| ---------- | ---------- | ------------ | ---------- | --- | ----- | ------ | ----- | ------------------------------------------------------------- | ------------------- | -------- | ----------------- | ------------ | ----------------- | ------- | --------- |
| during the | transition | of           | loads from | UPS | units | to the | grid. |                                                               |                     |          |                   |              |                   |         |           |
|            |            |              |            |     |       |        |       | Considering                                                   | simultaneous        |          | voltage-sensitive |              | load reductions,” |         | technical |
|            |            |              |            |     |       |        |       | report,                                                       | North               | American | Electric          | Reliability  | Corporation       | (NERC), | Jan.      |
| B. Dynamic | Model      | Improvements |            |     |       |        |       | 2025.                                                         | AccessedAugust2025. |          |                   |              |                   |         |           |
|            |            |              |            |     |       |        |       | [4] T.Kerci,C.Duggan,U.Farooq,S.Tweed,andM.V.Escudero,“Impact |                     |          |                   |              |                   |         |           |
Withoutaccuratedynamicmodels,manyofthedocumented
|          |           |              |     |        |               |     |           | of converter-based |         | demand | on frequency |       | quality in   | the ireland | and |
| -------- | --------- | ------------ | --- | ------ | ------------- | --- | --------- | ------------------ | ------- | ------ | ------------ | ----- | ------------ | ----------- | --- |
| facility | trips and | oscillations |     | cannot | be replicated |     | [3], [5], |                    |         |        |              |       |              |             |     |
|          |           |              |     |        |               |     |           | northern           | ireland | power  | systems,”    | CIGRE | Session 2024 | Papers      | and |
Proceedings,2024.
| [7]. To perform |     | power | system | planning, | dynamic | models | that |                 |        |       |                     |     |                    |     |       |
| --------------- | --- | ----- | ------ | --------- | ------- | ------ | ---- | --------------- | ------ | ----- | ------------------- | --- | ------------------ | --- | ----- |
|                 |     |       |        |           |         |        |      | [5] P. Gravois, | “Ercot | large | load loss/reduction |     | events 2020-2024,” |     | March |
accuratelyrepresenttheloadfacilitiesareneeded.LargeLoad
2025. Accessed:2025-08-09.
| developers | need | to invest | in creating | dynamic |     | models | of their |                |     |            |            |        |              |     |           |
| ---------- | ---- | --------- | ----------- | ------- | --- | ------ | -------- | -------------- | --- | ---------- | ---------- | ------ | ------------ | --- | --------- |
|            |      |           |             |         |     |        |          | [6] C. Mishra, | L.  | Vanfretti, | J. Delaree | Jr, T. | Purcell, and | K.  | D. Jones, |
facilities, and the industry should create better load models. “Understanding the inception of 14.7 hz oscillations emerging from a
datacenter,”SustainableEnergy,GridsandNetworks,p.101735,2025.
|             |            |     |              |     |     |     |     | [7] P.Gravois,“Largeloadoscillationevent,”March2025.Accessed:2025- |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ------------ | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| C. Improved | Monitoring |     | Capabilities |     |     |     |     |                                                                    |     |     |     |     |     |     |     |
08-09.
Both Dominion and ERCOT noted that detecting oscilla- [8] H.GanandP.Ranganathan,“Balanceofpower:Afull-stackapproachto
powerandthermalfluctuationsinmlinfrastructure,”inSystems,Google
tionsandconductingeventanalysiswaschallengingduetothe
|     |     |     |     |     |     |     |     | Cloud,2025. |     | Accessed:2025-07-01. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------------- | --- | --- | --- | --- | --- |
lack of high-resolution data [3], [5], [7]. For greater visibility, [9] S. Almubarak, H, Ibrahim, D. Singhania, and P. Enjeti, “Energy con-
LargeLoaddevelopersandtransmissionownersshoulddeploy sumption amp; power quality in bitcoin mining facilities in texas,” in
high-resolution sensors such as phasor measurement units, 2023IEEEEnergyConversionConferenceandExpo,2023.
|     |     |     |     |     |     |     |     | [10] A. Samanta, | S.  | Majumder, | H. Ibrahim, | P.  | Enjeti, and | L. Xie, | “Elec- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | ----------- | --- | ----------- | ------- | ------ |
digitalfaultrecorders,andpowerqualitymonitorsattheLarge tromagnetic transient model of cryptocurrency mining loads for low-
Load point of interconnection. Additionally, this data would voltage ride through assessment in transmission grids,” in 2024 IEEE
Poweramp;energySocietyGeneralMeeting,july2024.
| help validate | dynamic |     | models. |     |     |     |     |                     |     |      |              |           |          |          |        |
| ------------- | ------- | --- | ------- | --- | --- | --- | --- | ------------------- | --- | ---- | ------------ | --------- | -------- | -------- | ------ |
|               |         |     |         |     |     |     |     | [11] “Announcement: |     | Grid | reliable and | resilient | in 2024; | however, | emerg- |
ingriskscreatenewchallenges.”https://www.nerc.com/news/Headlines
D. Fast Responding Load Ramping Ancillary Service [Accessed06-07-2025].
|              |        |          |                |            |     |        |           | [12] M. Parker                                            | and | B. Starling, | “Dominion | energy               | unplanned | data | center    |
| ------------ | ------ | -------- | -------------- | ---------- | --- | ------ | --------- | --------------------------------------------------------- | --- | ------------ | --------- | -------------------- | --------- | ---- | --------- |
| In ERCOT     | and    | EirGrid, | the            | reduction  | of  | load   | following |                                                           |     |              |           |                      |           |      |           |
|              |        |          |                |            |     |        |           | loadtransferupdate,”June2025.                             |     |              |           | Accessed:2025-08-09. |           |      |           |
| disturbances | caused | a        | rise in system | frequency. |     | If the | system    |                                                           |     |              |           |                      |           |      |           |
|              |        |          |                |            |     |        |           | [13] R.J.O’Keefe,“Datacenterfaulteventrecords,”April2025. |     |              |           |                      |           |      | Accessed: |
2025-08-09.
| frequency      | goes too | high, | generator | over-frequency |            |     | protection |                                                                    |     |     |     |     |     |     |     |
| -------------- | -------- | ----- | --------- | -------------- | ---------- | --- | ---------- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                |          |       |           |                |            |     |            | [14] O.Gomis-Bellmunt,S.D.Tavakoli,V.A.Lacerda,andE.Prieto-Araujo, |     |     |     |     |     |     |     |
| will activate, | which    | could | worsen    | system         | stability. |     | To arrest  |                                                                    |     |     |     |     |     |     |     |
“Grid-formingloads:Cantheloadsbeinchargeofformingthegridin
thefrequencyrise,afastrespondingancillaryservicethatpro-
|     |     |     |     |     |     |     |     | modern | power | systems?,” | IEEE Transactions |     | on Smart | Grid, | vol. 14, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---------- | ----------------- | --- | -------- | ----- | -------- |
vides immediate load ramp-up from energy storage resource no.2,pp.1042–1055,2023.
|          |                   |     |                 |     |     |     |     | [15] Siemens | Energy, | “SVC | PLUS frequency |     | stabilizer,” | 2025. | Accessed: |
| -------- | ----------------- | --- | --------------- | --- | --- | --- | --- | ------------ | ------- | ---- | -------------- | --- | ------------ | ----- | --------- |
| charging | could potentially |     | be implemented. |     |     |     |     |              |         |      |                |     |              |       |           |
Aug.12,2025.
|     |     |     |            |     |     |     |     | [16] Tesla,“Batterystorageapplicationsatdatacenters.”NERCLargeLoads |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | VI. | CONCLUSION |     |     |     |     |                                                                     |     |     |     |     |     |     |     |
TaskForce,NERCLLTFMeetingandWorkshop,Apr.2025.Accessed:
| The increasing |     | deployment |     | of Large | Loads, | such | as data | Aug.12,2025. |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | -------- | ------ | ---- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
centersandcrypto-miningfacilities,posesnumerousreliability
979-8-3315-5569-6/26/$31.00 ©2026 IEEE
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:21 UTC from IEEE Xplore.  Restrictions apply.