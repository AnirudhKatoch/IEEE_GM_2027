IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023 2441
Data Center Power Supply Systems:
From Grid Edge to Point-of-Load
Yenan Chen , Member, IEEE, Keyan Shi, Min Chen , Senior Member, IEEE, and Dehong Xu , Fellow, IEEE
Abstract—Data centers consume about 2% of the world’s Electricity usually accounts for 40%–80%of the long-term
electricity with continuing growth. The power supply system operating expenditures of a data center [6]. Improving the
playsasignificantroleintheenergy savinganddecarbonization
energyefficiencyofdatacenterscandirectlyleadtosignificant
of data centers. The development of power electronics brings
economic benefits. Data center owners/operators care about
opportunities for more efficient and reliable data centers. This
article presents an overview of the data center power supply one metric called power usage effectiveness (PUE), which
system covering the power delivery path from the grid edge to is the ratio of a data center’s total electricity usage to the
onboardpoint-of-load(PoL)conversion.Thesystemarchitectures electricity used by IT equipment. The average annual PUE
are introduced at first with the discussion on efficiency and
for a large-scale data center was 1.57 in 2021 [7] and the
reliably.Thepowerconversionstagesofdatacenterpowersupply
best-in-class PUE has dropped to 1.1 [8] by optimizing
systemarediscussedasac–dcconversionsanddc–dcconversions.
The state-of-the-art techniques in topology, control, and device the power distribution path and improving the efficiency of
areinvestigated.Thisarticleisanattempttoprovideanoverview the uninterruptible power supply (UPS) and cooling system.
for high-performance data center power supply system design. Besides PUE, the power supply units (PSUs) and point-of-
Index Terms—ac–dc, data center, dc–dc, efficiency, reliability, load (PoL) converters, which deliver power from the rack
soft-switching, solid state transformer (SST), switched-capacitor to end loads such as central processing unit (CPU), graphic
(SC), uninterruptiblepower supply (UPS). processing unit (GPU) and storage, are also critical to the
overallenergyefficiencyof data centers. Therefore,the entire
I. INTRODUCTION power conversion path should be investigated to drive the
THE explosive demand for data and computing and the efficiencyimprovementofthe entiredatacenterpowersupply
system.
development of 5G technology have driven the rapid
The data center industry is considered to have high carbon
growthofdatacenters.Itisreportedthattheglobaldatacenter
emission. Following the global trend toward net-zero carbon,
market has exceeded 200 billion U.S. dollars in 2021 [1],
the data center industry is also striving to achieve the goal of
and is expected to increase with a compound annual growth
zero carbon emissions by employing clean energies such as
rate around 5%–10% in the next decade [2], [3]. As a result,
solar, wind, and hydrogenfuel. Google, Apple, and Facebook
the energy consumption of data centers also continues to
have announced that their operational energy usage, includ-
grow. The annual energy consumption of global data center
ing the data centers, is fully supplied by renewable energy.
(including data computing and transmission) in 2021 is esti-
To replace diesel generators, Microsoft has tested hydrogen
mated about 480–660 TWh [4], accounting for 1.7%–2.2%
fuelcellsasbackuppowerindatacenters[9].Asaresult,data
of the world’s electricity generation [5]. Such high-energy
center power supplysystems need to be upgradedto interface
consumption of data centers has raised public concerns about
with renewable energy.
their economic and environmentalimpact.
The power supply system is also critical to the reliability
Manuscript received 14 July 2022; revised 26 September 2022 of a data center. An industry survey shows that power is the
and 17 November 2022; accepted 6 December 2022. Date of publication leading cause of data center outage (43%) [7]. The reliability
14 December 2022; date of current version 13 June 2023. This work was
can be enhanced at all levels of the power supply system:
supportedinpartbytheNationalNaturalScienceFoundationofChinaunder
Grant52037010andinpartbytheZhejiangProvincialNaturalScienceFoun- newsystemarchitecturestoreducetheconversionstages,new
dation of China under Grant LQ23E070004. Recommended for publication circuit topologies and control strategies to reduce electrical
byAssociateEditorJosephO.Ojo.(Correspondingauthor:DehongXu.)
and thermal stress, and new devices with better performance.
Yenan Chen is with the College of Electrical Engineering and
the ZJU-Hangzhou Global Scientific and Technological Innovation Cen- Power electronics for data centers continues to evolve to
ter, Zhejiang University, Hangzhou, Zhejiang 311200, China (e-mail: address these challenges. In [10], the data center challenges
yenanc@zju.edu.cn).
andtherelatedpowerelectronicsarereviewedfromtheutility
Keyan Shi was with the College of Electrical Engineering, Zhe-
jiang University, Hangzhou, Zhejiang 310027, China. He is now with level to the internal-chip level. This article focuses on the
HoymilesPowerElectronicsInc.,Hangzhou,Zhejiang310015,China(e-mail: emerging technologies of data center power supply system
skyshi@zju.edu.cn).
in recent years, covering the ac interface at the grid edge to
Min Chen and Dehong Xu are with the College of Electrical Engi-
neering, Zhejiang University, Hangzhou, Zhejiang 310027, China (e-mail: PoLconverters.Thearchitecturesofdata centerpowersupply
heaven@zju.edu.cn; xdh@zju.edu.cn). systems are introduced in Section II. The power conversion
Color versions of one or more figures in this article are available at
stages in data center power supply systems are divided into
https://doi.org/10.1109/JESTPE.2022.3229063.
Digital ObjectIdentifier 10.1109/JESTPE.2022.3229063 ac–dc conversions and dc–dc conversions. Section III intro-
2168-6777©2022IEEE.Personaluseispermitted, butrepublication/redistribution requires IEEEpermission.
Seehttps://www.ieee.org/publications/rights/index.html formoreinformation.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore. Restrictions apply.

2442 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
| Fig. 1. Typical | data | center | power supply | system | from | the MV | grid to the |     |     |     |     |     |     |     |     |
| --------------- | ---- | ------ | ------------ | ------ | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
serverPSU.
|     |     |     |     |     |     |     |     | Fig. 3. | Three dc | power supply | architectures. |     | (a) Conventional |     | HVDC |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------------ | -------------- | --- | ---------------- | --- | ---- |
Fig. 2. Data center power supply system with ac online UPS (ac UPS architecture. (b) HVDC architecture with dc PSU. (c) Simplified LVDC
architecture.
system).
|     |     |     |     |     |     |     |     | shown in | Fig. 2. | The double-conversion(ac–dc–ac)efficiency |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----------------------------------------- | --- | --- | --- | --- | --- |
duces advances in ac–dc converters for the data center grid of commercial high-power ac online UPS is usually around
|                                           |     |     |     |     |     |              |     | 96%–97% | [13], | [14]. With | silicon | carbide | (SiC) | and | three- |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ----- | ---------- | ------- | ------- | ----- | --- | ------ |
| interface,UPS,andPSUwithinservers.Section |     |     |     |     |     | IVintroduces |     |         |       |            |         |         |       |     |        |
thedc–dcconvertersforserverpowersupplyandPoLconver- level technologies, the double-conversion efficiency is higher
sions. Section V summarizes this article and gives an outlook than 98% at 50% load [15], [16], and the efficiency of each
|                      |     |     |       |        |           |      |          | stage can  | reach    | 99% [17],  | [18].          |     |            |         |          |
| -------------------- | --- | --- | ----- | ------ | --------- | ---- | -------- | ---------- | -------- | ---------- | -------------- | --- | ---------- | ------- | -------- |
| on the developmentof |     |     | power | supply | system of | data | centers. |            |          |            |                |     |            |         |          |
|                      |     |     |       |        |           |      |          | The        | PSU also | has        | two conversion |     | stages:    | usually | a        |
|                      |     |     |       |        |           |      |          | boost-type | PFC      | stage with | a 400-V        |     | output and | an      | isolated |
II. SYSTEMARCHITECTURE
|              |     |          |                       |     |     |        |         | dc–dc stage | converting      |     | the 400-V | bus     | to a        | 12-V     | or 48-V |
| ------------ | --- | -------- | --------------------- | --- | --- | ------ | ------- | ----------- | --------------- | --- | --------- | ------- | ----------- | -------- | ------- |
| This section |     | provides | an architecture-level |     |     | review | of data |             |                 |     |           |         |             |          |         |
|              |     |          |                       |     |     |        |         | bus for     | the motherboard |     | power     | supply. | The 80-Plus | Titanium |         |
centerpowersupplysystems.Fig.1showsatypicaldatacenter certification requires a 96% half-load efficiency and a 91%
| power supply | system | from | the | medium | voltage | (MV) | grid | to  |     |     |     |     |     |     |     |
| ------------ | ------ | ---- | --- | ------ | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
full-loadefficiencyforaPSUwiththe230-Vacinput[19].The
| theserverPSU |     | [10].Theutilitygridis |     |     | themainpowersource |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
latestOCPopenrackstandardalreadypushesthesemetricsto
| of the data  | center. | Besides, | diesel | generators  |         | are the | backup   |           |         |           |          |       |        |         |     |
| ------------ | ------- | -------- | ------ | ----------- | ------- | ------- | -------- | --------- | ------- | --------- | -------- | ----- | ------ | ------- | --- |
|              |         |          |        |             |         |         |          | 97.5% and | 96.5%   | [20].     | The last | stage | is the | onboard | PoL |
| power source | for     | servers  | and    | the cooling | system. |         | They are |           |         |           |          |       |        |         |     |
|              |         |          |        |             |         |         |          | converter | for the | CPU power | supply.  |       |        |         |     |
interconnected by the automatic transfer switch (ATS). Then Intheacpowerarchitecture,therearesixconversionstages
| the power           | is delivered |     | to the       | server | by UPS | and PSU | with    |                 |          |         |       |             |        |         |       |
| ------------------- | ------------ | --- | ------------ | ------ | ------ | ------- | ------- | --------------- | -------- | ------- | ----- | ----------- | ------ | ------- | ----- |
|                     |              |     |              |        |        |         |         | in total        | from the | grid to | CPUs. | The battery | power  | also    | needs |
| parallel redundancy |              | for | reliability. | The    | power  | supply  | systems |                 |          |         |       |             |        |         |       |
|                     |              |     |              |        |        |         |         | to be converted |          | by the  | dc–ac | stage       | in the | ac UPS. | Such  |
arecategorizedasacarchitectures,dcarchitectures,andhybrid
|                |     |             |     |               |     |            |      | long conversion |        | path may     | decrease | the | overall | efficiency     | and |
| -------------- | --- | ----------- | --- | ------------- | --- | ---------- | ---- | --------------- | ------ | ------------ | -------- | --- | ------- | -------------- | --- |
| architectures. | For | simplicity, |     | the following |     | discussion | only |                 |        |              |          |     |         |                |     |
|                |     |             |     |               |     |            |      | reliability     | of the | power supply | system.  |     | On the  | other hand,the |     |
focuses on the power electronics converters of data center ac power distribution is mature and inexpensive.
powersupplysystems.Thedieselgenerator,powerdistribution
| units (PDUs), | protection,  |     | and | redundancy | are | not included. |     |             |              |                 |     |            |           |      |           |
| ------------- | ------------ | --- | --- | ---------- | --- | ------------- | --- | ----------- | ------------ | --------------- | --- | ---------- | --------- | ---- | --------- |
|               |              |     |     |            |     |               |     | B. DC Power | Architecture |                 |     |            |           |      |           |
|               |              |     |     |            |     |               |     | Comparing   | to           | ac, paralleling |     | in dc      | is simple | and  | reliable, |
| A. AC Power   | Architecture |     |     |            |     |               |     |             |              |                 |     |            |           |      |           |
|               |              |     |     |            |     |               |     | making      | dc power     | architectures   |     | attractive | for       | data | centers.  |
The ac power architecture has existed in data centers over Fig. 3(a)showsthe powersupplysystem with dc onlineUPS,
decades.AsshowninFig.2,theacpowerarchitectureconsists which is also called the high voltage direct current (HVDC)
ofUPS,PSU,andPOLconvertertoCPU.Powerisdistributed system. In the HVDC system, ac power is distributed at
in ac at both building-level and rack-level. UPS is critical building-levelanddcpowerisdistributedatrack-level.Theac
to the reliability, power quality, and stability of the entire online UPS is replaced by the dc online UPS. The first stage
system. The classification, topology, and control of UPS are of the dc online UPS is the same as the three-phase PFC
comprehensively reviewed in [11] and [12]. Among them, converter in ac online UPS. A second isolated dc–dc stage
the online UPS has better tolerance to the grid variation, which typically employs LLC topology is needed to provide
precise output regulation, and seamless transition to backup, the 240-V or 336-V output voltage (nominal value, voltage
andhasbeenwidelyusedindatacenterpowersupplysystems. range is 204–288 V and 300–400 V). High-voltage battery
Considering the power level of typical data center racks, the strings are directly connected to the HVDC bus. Except the
ac online UPS in data centers employs a three-phase ac–dc UPS, other conversion stages are the same as the ac UPS
stage for power factor correction (PFC) and a three-phase architecture. ac PSUs are compatible with the HVDC system
dc–ac stage as a three-phase back-to-back (BTB) converter. without modification.
The backup batteries are deployed on the dc bus of the BTB Above two solutions are the mainstream data center power
converter. The bypass switch of the ac online UPS is not supply systems, both with online UPS and six conversion
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2443
Fig.4. 48-Vrackpowersupplysystemwith48-VBBU[21].
|     |     |     |     | Fig.6. Datacenter | powersupplysystemwithSST. |     |     |     |     |
| --- | --- | --- | --- | ----------------- | ------------------------- | --- | --- | --- | --- |
ac+dchybridsystemwithdirect
|     |     |     |     | Fig.7.      |                |             | utility supplyanddcUPS. |            |     |
| --- | --- | --- | --- | ----------- | -------------- | ----------- | ----------------------- | ---------- | --- |
|     |     |     |     | traditional | line-frequency | transformer | (LFT)-based             | rectifiers |     |
Fig.5. Panamapowersupplysystem[23]. and solid-state transformer (SST) [25]. The result shows the
|     |     |     |     | 12-pulse rectifier | solution | has the | highest efficiency. | Besides |     |
| --- | --- | --- | --- | ------------------ | -------- | ------- | ------------------- | ------- | --- |
stages. In fact, the ac–dc stage of PSU is not necessary for the efficiency, the Panama architecture also has high-power
the HVDC architecture and it can be removed as shown in density and low cost because the circuit topology of the
Fig. 3(b). Fig. 3(c) shows a further simplified dc architecture, rectifier is greatly simplified.
in which the batteries are deployed at the HVDC bus of the The SST has raised the interest from the academia and
ac PSU and the power is distributed at low voltage (48 V or industry [26], [27], [28], [29], [30], [31], [32], [33], recently.
12 V) among servers. Generally, dc architectures with fewer Fig. 6showsthe data centerpowersupplywith SST. Modular
conversionstagescanachievehigherefficiency.Thedc power SSTcellsareconfiguredasinput-seriesoutput-parallel(ISOP)
|              |                   |                    |            | for interfacing | the MV | grid and the | dc bus. In | SST, energy | is  |
| ------------ | ----------------- | ------------------ | ---------- | --------------- | ------ | ------------ | ---------- | ----------- | --- |
| distribution | also has flexible | battery deployment | with fewer |                 |        |              |            |             |     |
conversion stages to the load, so that the efficiency of the dc processed by semiconductor devices at high frequency rather
systemishigherinthebackupmodeandtherelatedreliability than by transformer at line frequency. Thereby, the power
is also higher. However, the dc breaker and protection for densityofthepowersupplysystemisincreased.Thefull-load
HVDC system are difficult and costly. efficiency of a 3.8-kVac to 400-Vdc/25-kW laboratory proto-
|        |                   |                   |              | typewith 10-kVSiC | deviceachieves98.1%[29],[30].Anda |     |     |     |     |
| ------ | ----------------- | ----------------- | ------------ | ----------------- | --------------------------------- | --- | --- | --- | --- |
| Google | proposed the 48-V | rack power supply | system [21]. |                   |                                   |     |     |     |     |
As shown in Fig. 4, both the PSU and the battery backup 13.2-kVacto 1.05-kVdc/400-kWdemonstrationfrom industry
unit (BBU) are deployed on the rack shelf. The bidirectional shows a 98.5% efficiency around half-load [32]. The major
dc–dc converter in the BBU is a four-switch buck-boost advantageof SST is the high-powerdensity. Furthermore,the
converter whose peak efficiency is above 98% [22]. Power HVDC output of SST is directly fed to server racks and
|                |            |                       |              | the PSU | only performs | single-stage | conversion. | That | also |
| -------------- | ---------- | --------------------- | ------------ | ------- | ------------- | ------------ | ----------- | ---- | ---- |
| is distributed | at 48 V to | servers with 16 times | reduction of |         |               |              |             |      |      |
cable loss comparing to the conventional 12-V system. The improves the overall efficiency.
| overall    | efficiency is also improved | with the reduction | of total       |           |                    |     |     |     |     |
| ---------- | --------------------------- | ------------------ | -------------- | --------- | ------------------ | --- | --- | --- | --- |
|            |                             |                    |                | C. Hybrid | Power Architecture |     |     |     |     |
| conversion | stages. The challenges      | are that the       | PoL converters |           |                    |     |     |     |     |
haveto operateat higherinputvoltageandthe backupbattery Most top-tier data centers require dual power feeds for
capacity is limited by the volume of the rack shelf. better redundancy. That is, there are two independent power
Recently, power electronics manufacturers together with distribution paths from the utility grid to servers. The most
data center owners have also focused on innovations in the typical way is duplicating the power supply system in Figs. 2
gridinterfacestageuptoMVlevel.Fig.5showsadatacenter and3.Butthepainisthecostofinfrastructureandequipment.
power supply system called the Panama power supply [23]. Fig.7showsanhybridpowersupplysystemwithdirectutility
The 36-pulse phase shift transformer connects the 10-kV supply and dc UPS. Power is equally shared during normal
grid and the multipulse ac–dc rectification system [24]. Each operation and the efficiency is improved owing to removing
rectifier includesa diode rectifier bridge and a buck converter the online UPS in the ac path. The investment in UPS is
toregulatethe outputdcvoltage.The240-Vor336-VHVDC also reduced. However, the ac path is not protected by UPS.
bus is also compatible with the universal ac PSUs. The case Thereby,the reliability ofthis ac + dc hybridsystem is lower
study in [23] shows the efficiency of the 36-pulse phase shift than both the dual feeds systems.
transformer is 99% and the peak efficiency of the rectifier Moredatacentersarealsousingrenewableenergytoreduce
is 98.5% with Silicon devices, resulting a 97.5% efficiency the carbon emission. A super-UPS concept [34] is illustrated
from the MV grid to the HVDC bus of a 2.5-MW data enter. in Fig. 8, which is the evolution of UPS by adding natural
Anotherrecentstudycomparesasimilar12-pulserectifierwith gas, PV and Hydrogen fuel cell to the dc bus. The utility
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2444 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
TABLEI
COMPARISONOFDATACENTERPOWERSUPPLYARCHITECTURES
|     |     |     |     |     |     |     | stages is  | counted    | from    | the        | MV grid | to the         | CPU.   | The        | ac and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------- | ---------- | ------- | -------------- | ------ | ---------- | ------ |
|     |     |     |     |     |     |     | dc online  | UPS,       | ac PSU, | and        | SST     | are considered |        | to have    | two    |
|     |     |     |     |     |     |     | conversion | stages.    | For     | efficiency |         | comparison,    |        | we choose  | the    |
|     |     |     |     |     |     |     | overall    | efficiency | from    | MV         | grid    | and the        | backup | efficiency |        |
measuredfromthebackupbatteries.Theefficiencycalculation
|     |     |     |     |     |     |     | ends at          | the input | of  | the POL    | converter. |         | The   | input      | voltage |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --------- | --- | ---------- | ---------- | ------- | ----- | ---------- | ------- |
|     |     |     |     |     |     |     | of the PoL       | converter |     | is assumed |            | to be   | 48 V  | in each    | case    |
|     |     |     |     |     |     |     | for consistency. |           | The | losses     | from       | PDU and | other | mechanical |         |
Fig.8. Concept ofSuper-UPS[34]. parts are not included. The efficiency data of each conversion
|          |                        |         |        |        |             |       | stage at  | 50% load | are     | used       | considering | the        | derating | of          | power |
| -------- | ---------------------- | ------- | ------ | ------ | ----------- | ----- | --------- | -------- | ------- | ---------- | ----------- | ---------- | -------- | ----------- | ----- |
| grid and | the natural            | gas are | two    | major  | independent | power |           |          |         |            |             |            |          |             |       |
|          |                        |         |        |        |             |       | supplies. | The      | overall | efficiency | is          | calculated | by       | multiplying |       |
| sources  | for the infrastructure |         | of the | modern | society,    | which |           |          |         |            |             |            |          |             |       |
are competing and naturally backing up each other. Fuel cell the efficiency of each stage.
|           |                    |     |        |       |        |           | Detailed | converter |     | specifications |     | and | efficiency | calculation |     |
| --------- | ------------------ | --- | ------ | ----- | ------ | --------- | -------- | --------- | --- | -------------- | --- | --- | ---------- | ----------- | --- |
| and Li-on | battery supportthe |     | backup | power | to the | load when |          |           |     |                |     |     |            |             |     |
aregivenintheAppendix.Theefficiencyevaluationshowsthe
| both the | utility grid and  | gas | pipelines | fail. | This           | architecture |              |     |                   |     |       |                  |     |     |      |
| -------- | ----------------- | --- | --------- | ----- | -------------- | ------------ | ------------ | --- | ----------------- | --- | ----- | ---------------- | --- | --- | ---- |
|          |                   |     |           |       |                |              | power supply |     | architectureswith |     | fewer | conversionstages |     |     | have |
| not only | reduce the carbon |     | emission  | but   | also increases | the          |              |     |                   |     |       |                  |     |     |      |
higherefficiencyinnormaloperationmodeandbackupmode.
| system reliabilitysignificantly.Its |              |        |             | meantime | betweenfailures |           |             |               |     |      |      |            |     |        |      |
| ----------------------------------- | ------------ | ------ | ----------- | -------- | --------------- | --------- | ----------- | ------------- | --- | ---- | ---- | ---------- | --- | ------ | ---- |
|                                     |              |        |             |          |                 |           | Traditional | architectures |     | with | more | conversion |     | stages | have |
| (MTBF)                              | is 2.5 times | of the | traditional | UPS      | [34].           | The power |             |               |     |      |      |            |     |        |      |
relativelylowefficiency.Theperformanceevaluationdoesnot
managementandfaultprotectionarechallengingwithmultiple
|           |                    |         |        |            |              |         | cover the       | power | density   | of     | all architectures |     | due   | to     | the lack |
| --------- | ------------------ | ------- | ------ | ---------- | ------------ | ------- | --------------- | ----- | --------- | ------ | ----------------- | --- | ----- | ------ | -------- |
| sources.  | The Super-UPS      | system  | is     | originally | proposed     | for ac  |                 |       |           |        |                   |     |       |        |          |
|           |                    |         |        |            |              |         | of dimension    |       | data. The | volume | estimation        |     | at    | 2.5-MW | level    |
| loads. It | is also applicable |         | for dc | power      | distribution | so that |                 |       |           |        |                   |     |       |        |          |
|           |                    |         |        |            |              |         | in the Appendix |       | shows     | that   | the Panama        |     | power | supply | offers   |
| the PFC   | stage of the       | PSU can | be     | removed.   |              |         |                 |       |           |        |                   |     |       |        |          |
about30%spacesavingcomparedtotheconventionalacUPS
systemwithLFT.AnSSTprototypepresentedin[29]and[30]
| D. Evaluation | and Discussion |     |     |     |     |     |                   |     |              |     |       |       |      |       |     |
| ------------- | -------------- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | --- | ----- | ----- | ---- | ----- | --- |
|               |                |     |     |     |     |     | also demonstrates |     | high-density |     | power | stage | with | 10-kV | SiC |
Nine data center power supply architectures from Figs. 2 device. Whereas, the overall power density of the current
to 8 are compared in Table I. The number of the conversion cascadedSSTprototypesmaybelowerthantheLFTsolutions
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2445
| due to the        | complex | assembly |     | structure, | isolation   |     | distance | for   |     |     |     |     |
| ----------------- | ------- | -------- | --- | ---------- | ----------- | --- | -------- | ----- | --- | --- | --- | --- |
| the semiconductor |         | devices  | and | circuit    | components, |     | and      | extra |     |     |     |     |
protectioncircuitryforthecascadedmodules.Furtherstudyis
| needed       | to increase     | the | power        | density      | of         | SST.       |          |       |     |     |     |     |
| ------------ | --------------- | --- | ------------ | ------------ | ---------- | ---------- | -------- | ----- | --- | --- | --- | --- |
| Furthermore, |                 | the | cable losses |              | are also   | evaluated, |          | which |     |     |     |     |
| in fact,     | is important    |     | to the       | system       | efficiency | and        | cost.    | Two   |     |     |     |     |
| scenarios    | are considered: |     | power        | distribution |            | at         | building | level |     |     |     |     |
andpowerdistributionamongserverswithinarack.Inthefirst
| scenario, | the ac         | and | dc online | UPS,        | Panama |       | power  | supply, |     |     |     |     |
| --------- | -------------- | --- | --------- | ----------- | ------ | ----- | ------ | ------- | --- | --- | --- | --- |
| and SST   | are considered |     | to        | be deployed |        | close | to the | utility |     |     |     |     |
infrastructure.Thecorrespondingdistributionvoltagesofeach
| architecture      | are              | listed            | in Table    | I.                | Using     | the              | same        | wiring                                                 |     |     |     |     |
| ----------------- | ---------------- | ----------------- | ----------- | ----------------- | --------- | ---------------- | ----------- | ------------------------------------------------------ | --- | --- | --- | --- |
| configuration     | of               | [25]              | with        | Delta             | BL busbar | (one             | conductor   |                                                        |     |     |     |     |
| for each          | phase            | line              | and neutral | line              | in        | ac distribution, |             | two                                                    |     |     |     |     |
| conductors        | for              | each              | rail in     | dc distribution), |           | the              | cable       | loss                                                   |     |     |     |     |
|                   |                  |                   |             |                   |           |                  |             | Fig.9. ConceptofTCMandCRM.(a)ZVS-ONofS1.(b)ZVS-ONofS2. |     |     |     |     |
| ratio of          | the 220/380-Vac, |                   | 240-Vdc,    |                   | 336-Vdc,  |                  | and 400-Vdc |                                                        |     |     |     |     |
| distribution      | is               | 1:2.52:1.29:0.91. |             | The               | boundary  |                  | is 380      | Vdc                                                    |     |     |     |     |
| that the          | dc distribution  |                   | is          | more              | efficient | than             | the         | three-                                                 |     |     |     |     |
| phase 220/380-Vac |                  | distribution.     |             | The               | cable     | loss             | at rack     | level                                                  |     |     |     |     |
| with 240/336      |                  | and 400-Vdc       |             | is clearly        | lower     | than             | the         | single-                                                |     |     |     |     |
phase220-Vacdistributionandthe48-Vdcdistribution.Higher
| distribution    | voltage        |          | can significantly |             | reduce       | the       | cable        | loss  |     |     |     |     |
| --------------- | -------------- | -------- | ----------------- | ----------- | ------------ | --------- | ------------ | ----- | --- | --- | --- | --- |
| as the power    |                | of racks | and               | servers     | increases.   |           | On the       | other |     |     |     |     |
| hand, isolation |                | and      | protection        | for         | high-voltage |           | distribution |       |     |     |     |     |
| require         | more attention |          | and               | investment. | In           | addition, | SST          | can   |     |     |     |     |
| be deployed     | at             | each     | server            | room        | without      | the       | bulky        | MV to |     |     |     |     |
LV distribution transformer. Thereby the power is distributed Fig. 10. Inductor current and MOSFET voltage under TCM and CRM
| at MV-level     | to       | each | server   | room   | and the | cable  | loss   | can be operation. |              |                  |               |     |
| --------------- | -------- | ---- | -------- | ------ | ------- | ------ | ------ | ----------------- | ------------ | ---------------- | ------------- | --- |
| significantly   | reduced. |      |          |        |         |        |        |                   |              |                  |               |     |
| The reliability |          | of   | the data | center | power   | supply | system | is                |              |                  |               |     |
|                 |          |      |          |        |         |        |        | power supply      | system. This | section presents | three updates | to  |
highlyrelatedtothenumberofconversionstages,thelocation
|     |     |     |     |     |     |     |     | ac–dc converters | in data | centers. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | -------- | --- | --- |
ofbackupbattery,andthesystem-levelredundancy.Similarly,
| fewer conversion |              | stages | in  | the power | delivery |         | path   | lead to    |               |     |     |     |
| ---------------- | ------------ | ------ | --- | --------- | -------- | ------- | ------ | ---------- | ------------- | --- | --- | --- |
|                  |              |        |     |           |          |         |        | A. TCM and | CRM Converter |     |     |     |
| higher           | reliability. | The    | low | voltage   | direct   | current | (LVDC) |            |               |     |     |     |
system and the 48-V system have the distributed battery Triangle current mode (TCM) [36], [37], [38], [39] and
deployment because there are no centralized UPS or power criticalconductionmode(CRM)[40],[41],[42],[43],[44]are
supplies. Their reliability is consideredto be better than other two zero-voltage switching (ZVS) operation modes for ac–dc
backup structure because the shelf-assembled batteries are anddc–acconverters.Onechallengetotheconventionalac–dc
physically closer to the load. On the other hand, the capacity converter is the switching loss especially from the reverse
and backup time of the LVDC system and the 48-V system recovery of diodes. Wide bandgap (WBG) semiconductor
are limited by the shelf space. Distribution of backup battery devices like SiC and GaN device have excellent switch-
also requires more efforts on management and maintenance. ing performance with almost zero reverse recovery current.
The LVDC system also requiresdeeply customized PSU with Whereas,theirturn-onlossisstillmuchlargerthantheturn-off
build-in batteries. loss [45], [46], [47]. Besides, the fast-switching transition of
The ac power distribution is mature and low cost. On the WBGdevicesalsocausesEMIissues.Thereby,soft-switching,
contrary, dc power distribution, especially at HVDC, has the especially ZVS, is of great significance to WBG devices.
issue of dc breaker, arc extinction, and protection. dc archi- Figs. 9 and 10 show the concept of TCM and CRM
tecturesaremoresuitableforwell-designedandoperateddata operationinonephaselegandtherelatedinductorcurrentand
centers. As the demand for decarbonization of Data centers metal oxide silicon field effect transistor (MOSFET) voltage.
increases, more renewable energy will be integrated into the The key idea is to avoid the diode freewheeling by changing
power supply system. The concept of super-UPS will be the inductor current direction when the switch is turned off.
gradually implemented in the data center. With TCM operation, S 1 in Fig. 9(b) is turned off when the
inductorcurrentdecreasestoanegativeboundary.Thecurrent
III. AC–DCCONVERSION directionof S isfromdraintosourcesothatthereisnodiode
1
The ac–dc conversions are needed in UPS, PSU, and SST. freewheeling. The output capacitance of S and S is charged
1 2
In most cases, ac–dc conversion is the first power conversion and discharged by i . Then the body-diode of S conducts
|     |     |     |     |     |     |     |     |     | L   |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stageanddeliversallpowertoservers.Theefficiencyandreli- afteritsoutputcapacitanceisdischargedtozero.Thenegative
abilityofac–dcconversionarecriticaltotheentiredatacenter currentof inductor is necessary for ZVS even the grid instant
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2446 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
Giventhefactthattheac–dcstageandthedc–acstageofthe
aconlineUPSshareacommondcbus,theresonancebetween
theauxiliarycircuitandthedclinkpotentiallycancreateZVS
for both stages. A three-phase four-wire ZVS BTB converter
is proposed in [56] and the topology is shown in Fig. 11.
The auxiliary circuit is inserted between the bus capacitors
and the dc link of two three-phaseconverters.Duringmost of
the switching cycle, the auxiliary switch S is conductingand
Fig.11. Topologyofthree-phase four-wireZVSBTBconverter [56]. 7
the dc link voltage V is the summation of the bus voltage
link
V and the clamping voltage V . Prior to any high loss
BUS Cc
current is zero. With CRM operation, S is turned off when commutation (from the diode or body-diode of a switch to
1
the inductorcurrentdecreasesto zero. Theoutputcapacitance its complement switch in the same phase leg) of three-phase
of switch starts to resonate with the filter inductor. The ZVS converters, S 7 is turned off to initiate the resonance between
condition of CRM is that the dc bus voltage is higher than the resonant inductor L r and the equivalent capacitance (the
twice of the instantaneous grid voltage. output capacitance of the semiconductor power device and
The TCM and CRM both introduce high current ripple to optional external capacitors) of the dc link. The targeting
semiconductor devices and filter inductors, leading to a 15% switch can achieve ZVS-ON after the entire dc link voltage
increment on root-mean-square (RMS) current compared to decreases to zero.
the continuous conduction mode (CCM) converter. Another The switching action of S 7 mustbe timed at everycommu-
challenge for TCM and CRM operation is the variation of tation with higher switching loss (Type-2 commutation [55],
switching frequency, which may be complicated for control [57]) in two three-phase converters. As shown in Fig. 12(a),
and filter design. Modifications of TCM and CRM have S 7 needs to switch six times in each switching cycle with
been proposed to narrow the switching frequency range conventional sine pulse width modulation (SPWM), resulting
including adjusting the current boundary [37] and combining incomplicatedcontrolandextracirculationlossinthecircuit.
CRM,TCMwithdiscontinuousconductionmode(DCM)[44]. Anedge-alignedPWM (EA-PWM)[57]hasbeenproposedto
Despite the challenges, TCM and CRM converters are still synchronize all commutations with higher switching loss and
attracting research interest for their effectiveness on ZVS reducetheswitchingfrequencyof S 7 .AsshowninFig.12(b),
and excellent efficiency and power density. TCM and CRM the switching frequency of S 7 is the same as the switching
technology for the single-phase PFC rectifier in server PSU frequency of all other six switches. The ZVS topology and
havebeeninvestigatedin[36],[38],[39],[40],[41],and[42]. EA-PWM are further extended to more complex system with
With ZVS and WBG device, the switching frequency of the bothacanddcconversions[58].Thefundamentalanddetailed
TCM and CRM PFC converters is pushed to MHz range implementation of the ZVS technology is comprehensively
with a peak efficiency around 99%. A single-stage TCM introducedin[59].Itispotentiallyapplicablefortherenewable
PFC converter with 10-kV SiC device is proposed for the integration of data center power supply systems.
MV grid interface [30]. The switching frequency is between
35 and 75 kHz with direct conversion from 3.8 kVac to
C. Three-Level BTB Converter With Hybrid Module
7 kVdc and the full-load efficiency reaches 99.1% at 25 kW,
proving the effectiveness of the TCM technology. The TCM Three-leveltopologieshave beenwidely used in PV invert-
and CRM operation with nonlinear load, which is typical in ers, high-power UPS, motors drives, and so on. Compared to
UPS applications, still requires investigation. two-leveltopologies,three-leveltopologieshavelowervoltage
stress on semiconductor devices, smaller dv/dt and lower
switchingharmonics[60],[61].Fig.13showsthetopologyof
B. ZVS BTB Converter
a T-type three-level BTB converter. All the vertical switches
Another soft-switching approach is to use the auxiliary needto blockthe entiredc busvoltageV , while thevoltage
bus
circuit to resonate the entire dc link voltage to zero before stress of horizontal switch is only V /2. Compared to the
bus
the switching commutation. This soft-switching concept is neutral point clamped (NPC) three-level converter, the T-type
used in resonant dc-link (RDCL) inverter [48], [49], which converterhaslowerconductionlossandhigherswitchingloss.
is the pioneer and has a significant impact on this area. Thereby it is suitable for low-voltage high-power application
It originally uses discrete pulse modulation (DPM) with such as UPS.
variable switching frequency, resulting in sub-harmonics in The reverse recovery loss of the anti-parallel Silicon diode
the grid-side current. pulsewidth modulation (PWM) controls of insulated gate bipolar transistor (IGBT) has significant
for the resonant dc link concept also have been investigated impact on the system efficiency. Replacing the anti-parallel
andappliedtosingle/three-phaseac–dc/dc–acconverters[50], Silicon diode by SiC Schottky barrier diode (SBD) becomes
[51], [52], [53], [54], [55]. In these topologies, one auxiliary attractive because: 1) SiC diodes have almost zero reverse
circuit covers the ZVS for one converter. A major feature of recoveryloss;2)the maincircuitandgatedriversdonotneed
thisZVStechnologyisthatthefilter inductorisin continuous to be changed; and 3) the cost is lower than all SiC solu-
conduction mode and the conduction loss of device is not tion. Device manufacturers have released hybrid half-bridge
increased. module [62] and hybrid three-level NPC module [63].
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore. Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2447
|     |     |     |     |     | Fig.13. | T-typethree-level |     | BTBconverter | withIGBT. |     |     |     |
| --- | --- | --- | --- | --- | ------- | ----------------- | --- | ------------ | --------- | --- | --- | --- |
Fig.14. HybridmoduleconfigurationofaT-typethree-levelBTBconverter.
|     |     |     |     |     | SiC SBDs | are marked | in  | red [65]. | (a) One rectifier | phase. | (b) One | inverter |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ----------------- | ------ | ------- | -------- |
phase.
moduleconfigurationisshowninFig.14.Ahybridhalf-bridge
modulewithSiliconIGBTandSiCSBDisusedasthevertical
|     |     |     |     |     | switches | in the | rectifier | phase. | The | bidirectional | horizontal |     |
| --- | --- | --- | --- | --- | -------- | ------ | --------- | ------ | --- | ------------- | ---------- | --- |
switchisimplementedbytwohalf-bridgeIGBTmodules.Two
|                     |                 |                      |              |               | hybrid half-bridge |                   | modules     |               | form the    | bidirectional     | horizontal       |      |
| ------------------- | --------------- | -------------------- | ------------ | ------------- | ------------------ | ----------------- | ----------- | ------------- | ----------- | ----------------- | ---------------- | ---- |
|                     |                 |                      |              |               | switch of          | the inverterphase |             |               | and a 1200V | half-bridgemodule |                  |      |
|                     |                 |                      |              |               | is used as         | the               | vertical    | switches.     | This        | configuration     | is suitable      |      |
|                     |                 |                      |              |               | for unity          | PF operation.     |             | The           | full load   | efficiency        | at 45            | kW   |
|                     |                 |                      |              |               | is 97.0%           | at 7.2            | kHz,        | and 96.6%     | at          | 15 kHz,           | which is         | 0.3% |
|                     |                 |                      |              |               | and 0.6%           | higher            | than        | the converter |             | with all          | Silicon devices. |      |
| Fig. 12. Modulation | waves, carrier  | waves, and           | gate signals | of the con-   |                    |                   |             |               |             |                   |                  |      |
|                     |                 |                      |              |               | The efficiency     |                   | improvement |               | also shows  | the               | effectiveness    | of   |
| ventional SPWM      | and the EA-PWM. | The commutations     | with         | diode reverse |                    |                   |             |               |             |                   |                  |      |
|                     |                 |                      |              |               | the hybrid         | module            | solution    |               | for higher  | switching         | frequency.       |      |
| recovery are        | marked by red   | rectangles [58]. (a) | Conventional | SPWM.         |                    |                   |             |               |             |                   |                  |      |
(b)EA-PWM. Furthermore, the efficiency will be higher If the vertical
|                      |              |                 |          |          | modules       | of the | inverter | are        | 600-V devices. |     |     |     |
| -------------------- | ------------ | --------------- | -------- | -------- | ------------- | ------ | -------- | ---------- | -------------- | --- | --- | --- |
| In the T-type        | three-level  | BTB converter,  | reverse  | recovery |               |        |          |            |                |     |     |     |
|                      |              |                 |          |          | D. Comparison |        | of BTB   | Converters |                |     |     |     |
| of the anti-parallel | diode exists | in the vertical | switches | of the   |               |        |          |            |                |     |     |     |
rectifier and in the horizontal switches of the inverter with Table II lists the key specifications of the ZVS BTB
unity power factor (PF) operation. Fuji Electric released a converter prototypes and the three-level BTB converter with
225–333-kVA T-type three-level UPS with hybrid SiC hybridmodulethatalldevelopedbytheauthorsofthisarticle.
half-bridgemoduleastheverticalswitchesintherectifier[64]. The detailed design and test results are presented in [65]
Due to the unavailability of the hybrid SiC module with and [56]. The ZVS two-level BTB prototype and the hard-
bidirectional configuration, the inverter still uses all Silicon switching two-level BTB prototype have the same operation
devices. The efficiency is 96% at 25% load and 97.3% at full condition, same SiC MOSFET, and the same circuit layout
load. except the auxiliary circuit. The efficiency of the ZVS BTB
A T-type three-levelBTB converterwith hybridmodulesin converter is 3% higher at both half-load and full-load. The
both the rectifier and the inverter is researched in [65]. The efficiencyabove97%at150kHzalsoindicatesthehigh power
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2448 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
TABLEII
COMPARISONOFBTBCONVERTERSINACONLINEUPS
|     |     |     |     |     |     | efficiency     | than               | the commercial |                     | products    |                | with            | similar    | power   |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------ | -------------- | ------------------- | ----------- | -------------- | --------------- | ---------- | ------- |
|     |     |     |     |     |     | level [66],    | [67].              |                |                     |             |                |                 |            |         |
|     |     |     |     |     |     | Fig. 15        | compares           |                | the efficiency      |             | of the         | two-level       | SiC        | BTB     |
|     |     |     |     |     |     | converter      | with               | ZVS            | and hard-switching. |             |                | The             | efficiency | with    |
|     |     |     |     |     |     | ZVS drops      | slightly           |                | as the              | switching   |                | frequency       | increases  |         |
|     |     |     |     |     |     | from 20        | to 200             | kHz.           | Thereby             | the         | ZVS            | BTB             | topology   | is      |
|     |     |     |     |     |     | suitable       | for high-frequency |                |                     | operation   | up             | to hundreds     |            | of kHz  |
|     |     |     |     |     |     | with WBG       | devices.           |                | The hybrid          |             | SiC +          | Si solution     |            | is more |
|     |     |     |     |     |     | cost effective | than               | the            | full-SiC            | solution.   |                | Its performance |            | can     |
|     |     |     |     |     |     | be further     | improved           |                | if SiC              | and Si      | devices        | are             | packed     | in the  |
|     |     |     |     |     |     | same module    | according          |                | to                  | the circuit | configuration. |                 |            |         |
IV. DC–DCCONVERSION
|           |                        |         |           |               |              | The dc–dc  | conversions |        | in            | data | centers        | include         | the           | isolated |
| --------- | ---------------------- | ------- | --------- | ------------- | ------------ | ---------- | ----------- | ------ | ------------- | ---- | -------------- | --------------- | ------------- | -------- |
|           |                        |         |           |               |              | second     | stage of    | dc     | online        | UPS  | and PSU,       | the             | bidirectional |          |
|           |                        |         |           |               |              | converters | for         | backup | batteries     | and  | the            | PoL converters. |               | LLC      |
| Fig. 15.  | Efficiency comparison  | between | the 10-kW | ZVS2-level    | SiC BTB      |            |             |        |               |      |                |                 |               |          |
|           |                        |         |           |               |              | Resonant   | topologies  |        | with inherent |      | soft-switching |                 | have          | been     |
| converter | and the hard-switching | 2-level | SiC       | BTB converter | at different |            |             |        |               |      |                |                 |               |          |
switching frequencies [65]. widely applied to the isolated dc–dc conversion from the
|     |     |     |     |     |     | HVDC              | bus to     | the low-voltage |       | output      | at       | 12 V            | or 48         | V [68], |
| --- | --- | --- | --- | --- | --- | ----------------- | ---------- | --------------- | ----- | ----------- | -------- | --------------- | ------------- | ------- |
|     |     |     |     |     |     | [69], [70],       | [71],      | [72],           | [73]. | WBG         | devices, | soft-switching, |               | and     |
|     |     |     |     |     |     | novel transformer |            | design          |       | [70], [71], | [72],    | [73],           | [74],         | [75]    |
|     |     |     |     |     |     | enable high       | efficiency |                 | and   | power       | density  | with            | the switching |         |
frequencyuptoMHzrange.Recentpublicationsalsoshowthe
|         |                                         |     |     |     |       | effectivenessof   |                | modular          | topologieswith |                    |            | series-inputparallel- |              |         |
| ------- | --------------------------------------- | --- | --- | --- | ----- | ----------------- | -------------- | ---------------- | -------------- | ------------------ | ---------- | --------------------- | ------------ | ------- |
|         |                                         |     |     |     |       | output            | structure      | for              | the HVDC       |                    | to 12      | V or                  | 48 V         | conver- |
|         |                                         |     |     |     |       | sion [76],[77],in |                | which            | the            | high-voltagestress |            |                       | canbe        | shared  |
|         |                                         |     |     |     |       | by modular        | cells          | with             | low-voltage    |                    | device     | and                   | the          | voltage |
|         |                                         |     |     |     |       | second            | of transformer |                  | is             | also reduced.      |            | The                   | reported     | peak    |
|         |                                         |     |     |     |       | efficiency        | is 98.6%–99%   |                  | with           | a 48-V             | output     | [70],                 | [71],        | [72]    |
|         |                                         |     |     |     |       | and this          | number         | has              | reached        | 98.4%              | with       | a 12-V                | output       | [76].   |
|         |                                         |     |     |     |       | This              | section        | will             | introduce      | an                 | efficient  | power                 | conversion   |         |
|         |                                         |     |     |     |       | concept           | called         | the differential |                | power              | processing |                       | (DPP),       | and     |
|         |                                         |     |     |     |       | explore           | its potential  |                  | applications   |                    | in data    | centers.              | In addition, |         |
| Fig.16. | DPPpowersupplyforfour12-Vstackedservers |     |     |     | [83]. |                   |                |                  |                |                    |            |                       |              |         |
recentdevelopmentsonthehighconversionratioPoLconvert-
|         |                |            |         |         |           | ers are | also included. |     |     |     |     |     |     |     |
| ------- | -------------- | ---------- | ------- | ------- | --------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
| density | of the ZVS BTB | converter. | Similar | results | are found |         |                |     |     |     |     |     |     |     |
inahigh-powerZVSBTBprototypewithIGBTmodule.Both A. Differential Power Processing in Data Centers
the ZVS two-level BTB converter and the T-type three-level The concept of differential power processing was initially
BTB converterwith hybrid SiC + Si device [65] have higher applied to battery systems [78], [79], in which the power
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2449
|     |     |     |     | One limitation           |                  | of the      | above            | DPP           | systems         | is that           | the bus |
| --- | --- | --- | --- | ------------------------ | ---------------- | ----------- | ---------------- | ------------- | --------------- | ----------------- | ------- |
|     |     |     |     | voltage                  | is only          | determined  | by               | the           | PSU.            | That means        | any     |
|     |     |     |     | voltage                  | fluctuationon    |             | the bus          | will directly | changethe       |                   | voltage |
|     |     |     |     | of each                  | load. To         | address     | this issue,      | a             | buck-typeseries |                   | voltage |
|     |     |     |     | compensator              | [88]             | is employed |                  | between       | the             | ten-port          | MAB     |
|     |     |     |     | DPP converter            |                  | and the     | 50-V             | bus to        | absorb          | the bus           | voltage |
|     |     |     |     | variation.               | Whereas          | the         | overall          | efficiency    | drops           | by                | 1%–3%   |
|     |     |     |     | with a 5-Vdifference.The |                  |             | floatinggroundin |               |                 | the DPP           | system  |
|     |     |     |     | also requires            | differential     |             | signal           | transmission  |                 | or even           | optical |
|     |     |     |     | communication.           |                  | Another     | concern          | is            | that the        | output            | of DPP  |
|     |     |     |     | system is                | not galvanically |             | isolated         | from          | its             | input, which      | can     |
|     |     |     |     | cause potential          |                  | common-mode |                  | and           | safety          | issues especially |         |
|     |     |     |     | at high-voltage          |                  | application | such             | as            | 400–48-V        | conversion.       |         |
Intheauthors’opinion,theapplicableapplicationsoftheDPP
|     |     |     |     | architecture | are           | battery | equalizer  | of      | BBU    | and the interface |     |
| --- | --- | --- | --- | ------------ | ------------- | ------- | ---------- | ------- | ------ | ----------------- | --- |
|     |     |     |     | between      | the new       | 48-V    | system     | and the | legacy | 12-V servers.     |     |
|     |     |     |     | B. 48-V      | Point-of-Load |         | Converters |         |        |                   |     |
AsthelaststagetopowertheCPU,PoLconvertersfacethe
| Fig.17. MABDPPpowersupplyforstorage |     | server[84]. |     |            |         |            |     |        |             |          |     |
| ----------------------------------- | --- | ----------- | --- | ---------- | ------- | ---------- | --- | ------ | ----------- | -------- | --- |
|                                     |     |             |     | challenges | of high | conversion |     | ratio, | high output | current, | and |
highloadtransient.Inthe12-Vsystems,typicalPoLsolutions
converters only process the charge difference among series utilizethesingle-stagemultiphasebucktopologyasthevoltage
battery cells for equalization. Similar DPP idea is later used regulatormodule(VRM)[89].Duetothehighoutputcurrent,
to deal with the power mismatch from partial shading of extreme duty ratio at 1 V output and the hard-switching of
PV strings [80], [81], [82]. Recently, the DPP architecture is buckconverter,thepeakefficiencyof12–1V conversionwith
also extendedto data center applicationsto power the stacked DrMOS just reaches 90%, making it the bottleneck of the
servers[83],stackedharddiskdrives(HDD)[84],andstacked overallefficiencyofthedatacenterpowersupplysystem.Now
processors [85]. The nature of DPP enables high efficiency thedatacenterindustryisundergoingthetransitiontothe48-V
and high power density in these particular systems. Detailed system for lower power distribution loss. 48-V PoL solutions
review and classification of DPP architectures can be reached usually cascade two conversion stages with an intermediate
in [86] and [87]. bus to extend the conversion ratio [90]. The intermediate bus
Fig.16illustratestheDPPpowersupplyforstackedservers architectures (IBAs) with regulated bus and unregulated bus
proposed in [83]. Four 12-V servers are connected in series are systematically reviewed and compared in [91]. Besides,
and powered by the 48-V bus from the PSU. For the stacked two stages can be stacked as ISOP. Based on how two stages
servers,unequalpowerconsumptionleadstounbalancedinput are connected,we classify them into four architecturesshown
| voltage of each | server. Then | the DPP converter | is needed | to in Fig. 18. |     |     |     |     |     |     |     |
| --------------- | ------------ | ----------------- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
draw energy from the port with less server power consump- Fig. 18(a) shows the two-stage IBA that adds an inter-
tion and compensate energy to the port with higher power mediate bus converter in front of the VRM. dc transformer
consumption. The DPP converter is made up by four dual- (DCX)topologies[92],[93],[94],[95]andswitched-capacitor
active-bridge(DAB)cellsandabuffercapacitor,in whichthe (SC)-based topologies [96], [97], [98], [99], [100], [101],
differentialpowerisexchangedthroughtwoDABcells.Itcan [102],[103],[104],[105],[106]areusedforthebusconverter
achievea peakefficiencyof98.7%owingtothesmallportion because voltage regulation is not required in this stage. The
ofdifferentialpower.Furthermore,theDPPconverterdoesnot mature control of VRMs can be directly applied, enabling
needtobedesignedforthetotalpoweroffourservers,sothat the fast migration to the 48-V system. Since both DCX
the cost and size of DPP converter are also reduced. and SC topologies can achieve high efficiency up to 99%,
A ten-port muli-active-bridge(MAB) converter is designed the efficiency of the VRM is still the bottleneck of the
as the DPP converter for storage servers [84]. The system overall efficiency of two-stage IBA. Reducing the IB voltage
schematic is shown in Fig. 17. The 5-V HDDs in the storage becomesattractivebecauseitcanreducetheVRM’sswitching
server are groupedin series and powered by a 50-V bus. The loss and improve the dynamic performance at higher switch-
MAB converterwith ten half-bridgecells and one multiwind- ing frequency [104], [105], [106]. Intel has demonstrated a
ing single-core transformer interconnects all the ten groups. 5-V VRM with low-voltage GaN nMOS transistors [107].
TheoperationconceptissimilartotheDPPsysteminFig.16. The reported full load efficiency is 88.8% at 1 V/32 A and
| Thedifferentialpowerbetweentwo |     | arbitraryportsonlyneeds |     | 3.1 MHz. |     |     |     |     |     |     |     |
| ------------------------------ | --- | ----------------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
to be processed by two half-bridgecells with less power loss. The two-stage IBA with preregulation shown in Fig. 18(b)
The single core design further improves the power density. is patented by Vicor [108], [109], in which the first stage is a
Thereportedsystemefficiencyis99.77%withapowerdensity buck-boostconverterandthesecondstageisaLLC-DCX.The
of 700 W/in3. intermediatebusvoltageis48V or32V with the48-Vinput.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2450 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
|     |     |     |     |     |     |     |     | Fig.19. | Four-phasebuckconverterandthefour-phaseseries-capacitorbuck |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
converter.
|                       |           |                          |                |               |     |                    |     | the regulation |               | stage with | high           | efficiency |     | and power  | density |
| --------------------- | --------- | ------------------------ | -------------- | ------------- | --- | ------------------ | --- | -------------- | ------------- | ---------- | -------------- | ---------- | --- | ---------- | ------- |
|                       |           |                          |                |               |     |                    |     | [127], [128].  |               |            |                |            |     |            |         |
|                       |           |                          |                |               |     |                    |     | C. Comparison  |               | of 48-V    | PoL Converters |            |     |            |         |
| Fig. 18.              | Four 48-V | PoL                      | architectures. | (a) Two-stage |     | IBA. (b) Two-stage |     |                |               |            |                |            |     |            |         |
|                       |           |                          |                |               |     |                    |     | Table          | III comparesa |            | few key        | metrics    | of  | the recent | 48-V to |
| IBAwithPreregulation. |           | (c)ISOP.(d)Single-stage. |                |               |     |                    |     |                |               |            |                |            |     |            |         |
point-of-loadvoltageregulatordesigns.The48-VPoLtopolo-
|     |     |     |     |     |     |     |     | gies are       | categorized | as        | four groups:two-stage |     |     | IBA,       | two-stage |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | --------- | --------------------- | --- | --- | ---------- | --------- |
|     |     |     |     |     |     |     |     | preregulation, |             | ISOP, and | single-stage.         |     | The | comparison | shows     |
Therefore,theinductorofthebuck-booststagehasbothlowdc
|                |          |             |              |                           |       |            |     | the single-stage |        | solutions | including  |           | the             | transformer-based |              |
| -------------- | -------- | ----------- | ------------ | ------------------------- | ----- | ---------- | --- | ---------------- | ------ | --------- | ---------- | --------- | --------------- | ----------------- | ------------ |
| bias andripple |          | current,and |              | significantlyreducedsize. |       | Vicor’s    |     |                  |        |           |            |           |                 |                   |              |
|                |          |             |              |                           |       |            |     | topologies       | and    | SC-based  | topologies |           | have relatively |                   | high effi-   |
| 48-V PoL       | solution | has         | the industry | leading                   | power | density.   | Its |                  |        |           |            |           |                 |                   |              |
|                |          |             |              |                           |       |            |     | ciency.          | In the | authors’  | opinion,   | two-stage |                 | and               | single-stage |
| dynamic        | response | may         | be           | slow due to               | long  | power path | and |                  |        |           |            |           |                 |                   |              |
solutionsarebothneededinthefuture.Two-stageIBAismore
| the inherentnonlinearresonantbehavior.Fig. |           |        |           |           |       | 18(c)showsthe |        |          |                  |             |     |         |        |         |             |
| ------------------------------------------ | --------- | ------ | --------- | --------- | ----- | ------------- | ------ | -------- | ---------------- | ----------- | --- | ------- | ------ | ------- | ----------- |
|                                            |           |        |           |           |       |               |        | suitable | if multiple      | low-voltage |     | rails   | (e.g., | 1, 1.8, | 3.3 V) are  |
| ISOP architecture                          |           | [110], | in        | which the | input | terminals     | of the |          |                  |             |     |         |        |         |             |
|                                            |           |        |           |           |       |               |        | needed.  | The intermediate |             | bus | voltage | design | to      | balance the |
| DCX and                                    | regulator | are    | connected | in series | and   | their outputs |        |          |                  |             |     |         |        |         |             |
overallefficiency,powerdensity,andthedynamicperformance
| are connected |          | parallel. | The | power rating   | of  | the regulator    | is  |           |            |      |              |     |           |      |            |
| ------------- | -------- | --------- | --- | -------------- | --- | ---------------- | --- | --------- | ---------- | ---- | ------------ | --- | --------- | ---- | ---------- |
|               |          |           |     |                |     |                  |     | will be   | one focus. | The  | single-stage |     | solutions | can  | be applied |
| only part     | of total | power     | and | the conversion |     | loss is reduced. |     |           |            |      |              |     |           |      |            |
|               |          |           |     |                |     |                  |     | to system | with       | less | complexity   | but | requires  | high | current.   |
Ontheotherhand,itsregulationabilitymaybelimitedbythe
Meanwhilethedynamicperformanceandthetransientcontrol
| power rating | of  | the regulator. |     |     |     |     |     |                     |     |           |         |     |      |                |     |
| ------------ | --- | -------------- | --- | --- | --- | --- | --- | ------------------- | --- | --------- | ------- | --- | ---- | -------------- | --- |
|              |     |                |     |     |     |     |     | of the single-stage |     | solutions | require |     | more | investigation. |     |
Infact,single-stageisolatedtopologieswithcurrentdoubler
| are the earliest |     | work | on 48-V | PoL applications |     | [111], | [112], |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | ------- | ---------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
V. SUMMARY
[113],[114].Recentlytheyhaveraisedresearchinterestagain
because of the simple circuit topology [115], [116], [117], This article presents an architecture-level review of data
[118], [119]. Another single-stage approach combines the SC center power supply systems first, including the ac archi-
concept with inductor to provide both output regulation and tecture, dc architectures, and hybrid architectures. There is
high step-down conversion [120], [121], [122], [123], [124]. a trend to reduce the power conversion stages to improve
The dynamic performance of the single-stage isolated/SC the overall efficiency and reliability. Therefore, dc architec-
solutionsrequiresfurtherinvestigationbecausetheirmaximum tures are promising because the dc–ac stage in UPS and
duty ratio is limited below 50%. Similar SC-based regulation the ac–dc stage in PSU can be eliminated. Recent develop-
topologies are also applied to two-stage architectures. Fig. 19 ments on SST also enable the direct interface to the MV
shows a four-phase buck converter and a four-phase series- grid without the bulky LFT. Renewable integration is a new
capacitor buck (SCB) converter [125], [126]. Four high-side demand, that requires the innovationson circuit topology and
| switches | of the | series-capacitor |     | buck converter |     | are connected |     | control. |     |     |     |     |     |     |     |
| -------- | ------ | ---------------- | --- | -------------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
inseriesandtheintermediatebusvoltageV isequallyshared The recent developments on the converter-level in data
IB
by four switching cells. Thereby, the effective input voltage centerpowersupplysystemsarealsointroducedinthisarticle,
of each phase is only V /4, which significantly reduces including the ZVS technologies with WBG devices and a
IB
the voltage stress and switching loss. The series-capacitor low-cost alternative with hybrid SiC SBD and IGBT module
buck topology is also applied to the two-stage solutions as for ac–dc/dc–ac conversions in data centers, the server dc
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2451
TABLEIII
PERFORMANCECOMPARISONOF48-VPOINT-OF-LOADVOLTAGEREGULATORDESIGNS
power supply with DPP concept and 48-V PoL converters. UPSwithleadingperformance.Wechoosethenumberof97%
Theseemergingtechnologiesalltargetlowerdevicestressand forthegeneralcasewithSilicondevice.Theefficienciesofthe
faster operating frequency to improve the efficiency, power three-phase rectifier and three-phase inverter in the ac online
density, and dynamic performance of converters. UPSarebothsetto98.5%withthesymmetricalstructure.The
Giventhefactthatthepowerconsumptionofdatacentersis efficiency of the two-stage 220-Vac to 48-Vdc PSU is set to
huge and continues to grow. The importance of the efficiency be 97% at the power level of 3 kW [129], [130]. The normal
of data center powersupply system is obvious.Energysaving operation efficiency and the backup efficiency of the power
and decarbonization in data centers requires efforts on both architecture with ac online UPS are
| system architecture |     | and | every power | conversion |     | stage | from |     |     |     |                      |     |     |     |     |
| ------------------- | --- | --- | ----------- | ---------- | --- | ----- | ---- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
|                     |     |     |             |            |     |       |      |     | η   |     | = 99%×97%×97%=93.15% |     |     |     |     |
ac_normal
| the grid edge | to onboard |     | processors. |     |     |     |     |     |     |         |                     |     |     |     |     |
| ------------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | ------- | ------------------- | --- | --- | --- | --- |
|               |            |     |             |     |     |     |     |     |     | η       | = 98.5%×97%=95.55%. |     |     |     |     |
|               |            |     |             |     |     |     |     |     |     | ac_back |                     |     |     |     | (1) |
APPENDIX
|                |     |     |             |     |              |     |     | We     | assume    | the  | dc online | UPS          | has the  | same   | efficiency |
| -------------- | --- | --- | ----------- | --- | ------------ | --- | --- | ------ | --------- | ---- | --------- | ------------ | -------- | ------ | ---------- |
| SPECIFICATIONS |     | AND | PERFORMANCE |     | EVALUATIONOF |     |     |        |           |      |           |              |          |        |            |
|                |     |     |             |     |              |     |     | as the | ac online | UPS. | The       | single-stage | isolated | dc PSU | faces      |
DATA CENTERPOWERARCHITECTURE
|                  |         |             |            |                   |          |        |     | the       | input        | voltages | of 240,   | 336, and | 400 Vdc.       | Considering |           |
| ---------------- | ------- | ----------- | ---------- | ----------------- | -------- | ------ | --- | --------- | ------------ | -------- | --------- | -------- | -------------- | ----------- | --------- |
| One fact         | is that | the power   | conversion | in                | the data | center | is  |           |              |          |           |          |                |             |           |
|                  |         |             |            |                   |          |        |     | the       | distribution | of       | switching | loss     | and conduction |             | loss with |
| more centralized |         | at the grid | edge       | (e.g., high-power |          | LFT    | and |           |              |          |           |          |                |             |           |
|                  |         |             |            |                   |          |        |     | different | voltages,    |          | we assume | a 98%    | efficiency     | for         | all three |
UPS)andmoredistributedattheloadside.Ateachconversion
|           |          |       |              |         |     |              |     | cases. | The   | efficiency   | data | of first two | HVDC | architectures | in  |
| --------- | -------- | ----- | ------------ | ------- | --- | ------------ | --- | ------ | ----- | ------------ | ---- | ------------ | ---- | ------------- | --- |
| stage, we | consider | there | are multiple | modules |     | in parallel. |     |        |       |              |      |              |      |               |     |
|           |          |       |              |         |     |              |     | Fig.   | 3 can | be obtained. |      |              |      |               |     |
e.g., one LFT, several UPS, hundreds, or thousands of PSU. The conventionalHVDC architecture
Thereby,theoverallefficiencyofthedatacenterpowersupply
system can be evaluatedby multiplyingthe efficiency of each η = 99%×97%×97%=93.15%
HVDC1_normal
converter and the difference of the converter’s power rating η = 97%. (2)
HVDC1_back
| does not affect  | the         | calculation. | The | efficiency       | data | with | 50%    |     |      |              |     |         |     |     |     |
| ---------------- | ----------- | ------------ | --- | ---------------- | ---- | ---- | ------ | --- | ---- | ------------ | --- | ------- | --- | --- | --- |
|                  |             |              |     |                  |      |      |        | The | HVDC | architecture |     | with dc | PSU |     |     |
| load is selected | considering |              | the | load utilization |      | and  | design |     |      |              |     |         |     |     |     |
overhead.
|       |            |     |            |         |          |     |      |     | η            |     | = 99%×97%×98%=94.11% |     |     |     |     |
| ----- | ---------- | --- | ---------- | ------- | -------- | --- | ---- | --- | ------------ | --- | -------------------- | --- | --- | --- | --- |
| A 99% | efficiency | is  | reasonable | for the | MW-level |     | LFT. |     | HVDC2_normal |     |                      |     |     |     |     |
|       |            |     |            |         |          |     |      |     | η            |     | = 98%.               |     |     |     | (3) |
Table IV lists the specifications of four high-power ac online HVDC2_back
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2452 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
TABLEIV
SPECIFICATIONSOFACONLINEUPS
TABLEV
SPECIFICATIONSOFPANAMAPOWERSUPPLYANDTWOSSTPROTOTYPES
| The      | efficiencycalculationof |      |                 | the simplified |     | LVDC | architec- | to 400-Vdc |     | SST        |     |                  |     |     |     |
| -------- | ----------------------- | ---- | --------------- | -------------- | --- | ---- | --------- | ---------- | --- | ---------- | --- | ---------------- | --- | --- | --- |
| ture can | use the                 | data | of ac PSU       | and dc         | PSU |      |           |            |     |            |     |                  |     |     |     |
|          |                         |      |                 |                |     |      |           |            |     | η          | =   | 97.5%×98%=95.55% |     |     |     |
|          | η                       |      | =99%×97%=96.03% |                |     |      |           |            |     | SST_normal |     |                  |     |     |     |
LVDC_normal
|     |     |     |       |     |     |     | (4) |     |     | η        | =   | 98%. |     |     | (7) |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --- | --- | --- |
|     | η   |     | =98%. |     |     |     |     |     |     | SST_back |     |      |     |     |     |
LVDC_back
Theefficiencycalculationofthe48-Vracksystemissimilar. The power density of SST is not compared due to the lack
|          |     |            |                  |        |      |     |     | of fully  | commercializedproducts. |           |           | [33]       | shows      | the    | 1-MW SST    |
| -------- | --- | ---------- | ---------------- | ------ | ---- | --- | --- | --------- | ----------------------- | --------- | --------- | ---------- | ---------- | ------ | ----------- |
| The 48-V | BBU | efficiency | is set           | to 98% | [22] |     |     |           |                         |           |           |            |            |        |             |
|          |     |            |                  |        |      |     |     | prototype | is                      | assembled | in        | a standard | container. |        | The volume  |
|          | η   |            | = 99%×97%=96.03% |        |      |     |     |           |                         |           |           |            |            |        |             |
|          |     |            |                  |        |      |     |     | of the    | container               | is        | typically | around     | 25         | m3 and | larger than |
48V_normal
η = 98%. the Panama power supply and the mature online UPS system.
(5)
48V_back
|     |     |     |     |     |     |     |     | Further | study | is needed | to  | improvethe | power | density | of SST. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | --- | ---------- | ----- | ------- | ------- |
The specifications of a 2.5-MW Panama power supply are In the ac + dc hybrid system we assume the input power
| listed | in Table | V. The | data | source | of the | Panama | power |            |        |     |         |         |            |        |          |
| ------ | -------- | ------ | ---- | ------ | ------ | ------ | ----- | ---------- | ------ | --- | ------- | ------- | ---------- | ------ | -------- |
|        |          |        |      |        |        |        |       | is equally | shared |     | and the | overall | efficiency | is the | weighted |
supply [23] does not give the exact dimension but mentions average efficiency of two paths
| that a | standard | rectifier | rack | and a | PDU rack | can | support |     |     |     |     |     |     |     |     |
| ------ | -------- | --------- | ---- | ----- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
the power up to 720 kW, the phase shift transformer together η = 99%×(0.5×97%+0.5×97%×98%)
Hybrid_normal
with the input power distribution circuit occupy the space of = 95.07%
| 4 standard   | racks. | The      | overall | volume  | of the | 2.5-MW | system   |     |             |        |     |     |     |     |     |
| ------------ | ------ | -------- | ------- | ------- | ------ | ------ | -------- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
|              |        |          |         |         |        |        |          | η   |             | = 98%. |     |     |     |     | (8) |
|              |        |          | m3      |         |        |        |          |     | Hybrid_back |        |     |     |     |     |     |
| is estimated |        | as 15.36 | (12     | racks). | If we  | use    | the same |     |             |        |     |     |     |     |     |
transformerspacewithtwo1.25-MWMegaFlexandfourmore
|            |          |          |             |         |                |             |        | The            | super-UPS |       | system       | is implemented |       | by             | 100-kW     |
| ---------- | -------- | -------- | ----------- | ------- | -------------- | ----------- | ------ | -------------- | --------- | ----- | ------------ | -------------- | ----- | -------------- | ---------- |
| additional | PDU      | racks,   | the overall | volume  | of             | this 2.5-MW | ac     |                |           |       |              |                |       |                |            |
|            |          |          |             |         |                |             |        | bi-directional |           | dc–ac | modules      | and 30-kW      |       | bi-directional | dc–dc      |
| system     | is 22.42 | m3. This | comparison  |         | shows          | the high    | power  |                |           |       |              |                |       |                |            |
|            |          |          |             |         |                |             |        | modules,       | both      | are   | non-isolated | [35].          | The   | dc bus         | voltage is |
| density    | of the   | Panama   | power       | supply. | The efficiency |             | of the |                |           |       |              |                |       |                |            |
|            |          |          |             |         |                |             |        | ±375           | V and     | the   | input range  | of the         | dc–dc | module         | is 200–    |
Panama power supply is considered to be 97.5%, and the 400V.Wealsoassumethedc–acmodulesanddc–dcmodules
| overall | system | efficiency | and                | backup efficiency |     | are |     |        |              |     |        |          |         |            |            |
| ------- | ------ | ---------- | ------------------ | ----------------- | --- | --- | --- | ------ | ------------ | --- | ------ | -------- | ------- | ---------- | ---------- |
|         |        |            |                    |                   |     |     |     | in the | super-UPS    |     | system | all have | a 98.5% | efficiency | so that    |
|         |        |            |                    |                   |     |     |     | power  | distribution |     | in the | backup   | mode    | does not   | affect the |
|         | η      |            | = 97.5%×98%=95.55% |                   |     |     |     |        |              |     |        |          |         |            |            |
Panama_normal
|       |        |             |                    |     |     |       |          | efficiency. | The | efficiency |                      | of the | super-UPS | system | can be |
| ----- | ------ | ----------- | ------------------ | --- | --- | ----- | -------- | ----------- | --- | ---------- | -------------------- | ------ | --------- | ------ | ------ |
|       | η      |             | = 98%.             |     |     |       | (6)      |             |     |            |                      |        |           |        |        |
|       |        | Panama_back |                    |     |     |       |          | calculated  | by  |            |                      |        |           |        |        |
| Table | V also | shows       | the specifications |     | of  | three | SST pro- |             |     |            |                      |        |           |        |        |
|       |        |             |                    |     |     |       |          |             | η   |            | = 99%×97%×97%=93.15% |        |           |        |        |
Super_normal
| totypes. | Considering |     | the different | input–output |     | voltages, |     | a   |     |     |                     |     |     |     |     |
| -------- | ----------- | --- | ------------- | ------------ | --- | --------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
|          |             |     |               |              |     |           |     |     | η   |     | = 98.5%×97%=95.55%. |     |     |     | (9) |
97.5%efficiencyisusedforthecalculationwithfora10-kVac Super_back
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2453
REFERENCES [24] B. Singh, S. Gairola, B. N. Singh, A. Chandra, and K. Al-Haddad,
|     |     |     |     |     |     |     |     | “Multipulse |     | AC–DC | converters | for improving |     | power quality: | A   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ---------- | ------------- | --- | -------------- | --- |
[1] StatistaResearchDepartment(2022).DataCentersStatistics&Facts.
|           |            |     |                                                    |     |     |     |     | review,”  | IEEE | Trans. | Power Electron., |     | vol. 23, | no. 1, pp.260–281, |     |
| --------- | ---------- | --- | -------------------------------------------------- | --- | --- | --- | --- | --------- | ---- | ------ | ---------------- | --- | -------- | ------------------ | --- |
| [Online]. | Available: |     | https://www.statista.com/topics/6165/data-centers/ |     |     |     |     | Jan.2008. |      |        |                  |     |          |                    |     |
[2] P&SIntelligence. (2022). DataCenter Market Report:ByInfrastruc- [25] J. Huber, P. Wallmeier, R. Pieper, F. Schafmeister, and J. W. Kolar,
| ture | Type, End | User | Global | Industry | Size and | Demand | Forecast to |     |     |     |     |     |     |     |     |
| ---- | --------- | ---- | ------ | -------- | -------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
“ComparativeevaluationofMVAC-LVDCSSTandhybridtransformer
| 2030. | [Online]. | Available: | https://www.psmarketresearch.com/market- |     |     |     |     |          |     |                      |     |          |            |           |        |
| ----- | --------- | ---------- | ---------------------------------------- | --- | --- | --- | --- | -------- | --- | -------------------- | --- | -------- | ---------- | --------- | ------ |
|       |           |            |                                          |     |     |     |     | concepts | for | future datacenters,” |     | in Proc. | Int. Power | Electron. | Conf., |
analysis/data-center-market
May2022,pp.2027–2034.
[3] Allied Market Research. (2021). Data Center Market by Component, [26] X.She,A.Q.Huang,andR.Burgos,“Reviewofsolid-statetransformer
Type, Enterprise Size, and End User: Global Opportunity Analy- technologiesandtheirapplicationinpowerdistributionsystems,”IEEE
| sis and | Industry | Forecast, | 2021–2030. |     | [Online]. | Available: | https:// |           |      |        |       |            |         |                    |     |
| ------- | -------- | --------- | ---------- | --- | --------- | ---------- | -------- | --------- | ---- | ------ | ----- | ---------- | ------- | ------------------ | --- |
|         |          |           |            |     |           |            |          | J. Emerg. | Sel. | Topics | Power | Electron., | vol. 1, | no. 3, pp.186–198, |     |
www.alliedmarketresearch.com/data-center-market-A13117
Sep.2013.
[4] InternationalEnergyAgency.(2021).DataCentresandDataTransmis-
|      |           |           |            |                                   |     |     |     | [27] M. | Leibl, G. | Ortiz, | and J. | W. Kolar, | “Design | and experimental |     |
| ---- | --------- | --------- | ---------- | --------------------------------- | --- | --- | --- | ------- | --------- | ------ | ------ | --------- | ------- | ---------------- | --- |
| sion | Networks. | [Online]. | Available: | https://www.iea.org/reports/data- |     |     |     |         |           |        |        |           |         |                  |     |
analysisofamedium-frequencytransformerforsolid-statetransformer
centres-and-data-transmission-networks applications,”IEEEJ.Emerg.Sel.TopicsPowerElectron.,vol.5,no.1,
| [5] BP | P.L.C. | (2022). | Bp Statistical | Review | of  | World Energy | 2022. |     |     |     |     |     |     |     |     |
| ------ | ------ | ------- | -------------- | ------ | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
pp.110–123,Mar.2017.
| [Online]. | Available: |     | https://www.bp.com/content/dam/bp/business- |     |     |     |     |               |     |           |          |        |                 |             |     |
| --------- | ---------- | --- | ------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --------- | -------- | ------ | --------------- | ----------- | --- |
|           |            |     |                                             |     |     |     |     | [28] S. Zhao, | Q.  | Li, F. C. | Lee, and | B. Li, | “High-frequency | transformer |     |
sites/en/global/corporate/pdfs/energy-economics/statistical-review/bp-
designformodularpowerconversionfrommedium-voltageACto400
stats-review-2022-full-report.pdf
|                 |          |            |                                            |     |                |         |             | VDC,”             | IEEE | Trans. Power | Electron., | vol.        | 33, no. | 9, pp.7545–7557, |           |
| --------------- | -------- | ---------- | ------------------------------------------ | --- | -------------- | ------- | ----------- | ----------------- | ---- | ------------ | ---------- | ----------- | ------- | ---------------- | --------- |
| [6] U.S.Chamber |          | ofCommerce | Technology                                 |     | Engagement     | Center. | (2017).     | Sep.2018.         |      |              |            |             |         |                  |           |
| Data            | Centers: | Jobs       | and Opportunities                          |     | in Communities |         | Nationwide. |                   |      |              |            |             |         |                  |           |
|                 |          |            |                                            |     |                |         |             | [29] D. Rothmund, |      | T. Guillod,  | D.         | Bortis, and | J. W.   | Kolar, “99%      | efficient |
| [Online].       |          | Available: | https://www.uschamber.com/technology/data- |     |                |         |             |                   |      |              |            |             |         |                  |           |
10kVSiC-based7kV/400VDCtransformerforfuturedatacenters,”
centers-jobs-opportunities-communities-nationwide
IEEEJ.Emerg.Sel.TopicsPowerElectron.,vol.7,no.2,pp.753–767,
| [7] Uptime | Institute. |     | (2021). | 2021 Data | Center | Industry | Survey |           |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ------- | --------- | ------ | -------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| Results.   |            |     |         |           |        |          |        | Jun.2019. |     |     |     |     |     |     |     |
[Online]. Available: https://uptimeinstitute.com/2021-data- [30] D.Rothmund,T.Guillod,D.Bortis,andJ.W.Kolar,“99.1%efficient
center-industry-survey-results
10kVSiC-basedmedium-voltageZVSbidirectionalsingle-phasePFC
| [8] Google | (2022). | Data | Center | Efficiency. | https://www.google.com/ |     |     |       |         |      |           |             |       |            |         |
| ---------- | ------- | ---- | ------ | ----------- | ----------------------- | --- | --- | ----- | ------- | ---- | --------- | ----------- | ----- | ---------- | ------- |
|            |         |      |        |             |                         |     |     | AC/DC | stage,” | IEEE | J. Emerg. | Sel. Topics | Power | Electron., | vol. 7, |
about/datacenters/efficiency
no.2,pp.779–797,Jun.2019.
| [9] J. Roach. | (2020). | Microsoft |     | Tests Hydrogen | Fuel | Cells | for Backup |     |     |     |     |     |     |     |     |
| ------------- | ------- | --------- | --- | -------------- | ---- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
PoweratDatacenters.[Online].Available:https://news.microsoft.com/ [31] H. Weng, J. Li, K. Shi, M. Chen, P. T. Krein, and D. Xu, “A DC
innovation-stories/hydrogen-datacenters/ solid-state transformer with DC fault ride-through capability,” IEEE
|     |     |     |     |     |     |     |     | J.Emerg.Sel.Topics |     |     | PowerElectron., | vol.10,no.4,pp.3617–3630, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --------------- | ------------------------- | --- | --- | --- |
[10] P.T.Krein,“Datacenterchallengesandtheirpowerelectronics,”CPSS
Aug.2022.
| Trans.PowerElectron. |     |     | Appl.,vol.2,no.1,pp.39–46,2017. |     |     |     |     |         |              |                  |     |                |     |        |        |
| -------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | ------- | ------------ | ---------------- | --- | -------------- | --- | ------ | ------ |
|                      |     |     |                                 |     |     |     |     | [32] C. | Zhu. (2021). | High-Efficiency, |     | Medium-Voltage |     | Input, | Solid- |
[11] S.B.BekiarovandA.Emadi,“Uninterruptiblepowersupplies:Classi-
fication,operation,dynamics,andcontrol,”inProc.IEEEAppl.Power State, Transformer Based 400-kW/1000-V/400-A Extreme Fast
Electron. Conf.Expo.,Mar.2002,pp.597–604. Charger for Electric Vehicles. DOE Vehicle Technologies Office
|                |     |            |     |              |          |                 |     | Annual | Merit | Review | about | Electrification. |     | [Online]. | Available: |
| -------------- | --- | ---------- | --- | ------------ | -------- | --------------- | --- | ------ | ----- | ------ | ----- | ---------------- | --- | --------- | ---------- |
| [12] M. Aamir, | K.  | A. Kalwar, | and | S. Mekhilef, | “Review: | Uninterruptible |     |        |       |        |       |                  |     |           |            |
https://www.energy.gov/sites/default/files/2021-06/elt241_zhu_
| power | supply | (UPS) | system,” | Renew. | Sustain. | Energy Rev., | vol. 58, |     |     |     |     |     |     |     |     |
| ----- | ------ | ----- | -------- | ------ | -------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
2021_o_5-24_126pm_LR_TM.pdf
pp.1395–1410,May2016.
[13] ABB.UninterruptiblePowerSupplySystemsStandaloneandModular [33] T. Liu et al., “Design and implementation of high efficiency control
Portfolio1kVAto6MVA.Accessed:Sep.12,2022.[Online].Available: schemeofdualactivebridgebased10kV/1MWsolidstatetransformer
|     |     |     |     |     |     |     |     | for | PV application,” |     | IEEE Trans. | Power | Electron., | vol. 34, | no. 5, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ----- | ---------- | -------- | ------ |
https://search.abb.com/library/Download.aspx?DocumentID=
pp.4223–4238,May2019.
04-2782_PO_EN&DocumentPartId=
|               |       |        |              |     |           |      |           | [34] D. Xu, | H. Li, | Y. Zhu, | K. Shi, | and C. | Hu, “High-surety |     | microgrid: |
| ------------- | ----- | ------ | ------------ | --- | --------- | ---- | --------- | ----------- | ------ | ------- | ------- | ------ | ---------------- | --- | ---------- |
| [14] Toshiba. | G9000 | Series | 100-2000kVA. |     | Accessed: | Sep. | 12, 2022. |             |        |         |         |        |                  |     |            |
[Online]. Available: https://www.toshiba.com/tic/power-electronics/ Super uninterruptable power supply with multiple renewable energy
uninterruptible-power-systems/three-phase/g9000-series-100-to-2000- sources,”Electr.PowerCompon.Syst.,vol.43,nos.8–10,pp.839–853,
May2015.
kva
|               |            |        |                                                |      |           |      |           | [35] H.Li,M.Chen,B.Yang,F.Blaabjerg,andD.Xu,“Fastfaultprotection |              |     |               |     |                 |              |     |
| ------------- | ---------- | ------ | ---------------------------------------------- | ---- | --------- | ---- | --------- | ---------------------------------------------------------------- | ------------ | --- | ------------- | --- | --------------- | ------------ | --- |
| [15] Toshiba. | G2020      | Series | SiC 500–750                                    | kVA. | Accessed: | Sep. | 12, 2022. |                                                                  |              |     |               |     |                 |              |     |
|               |            |        |                                                |      |           |      |           | based                                                            | on direction | of  | fault current | for | the high-surety | power-supply |     |
| [Online].     | Available: |        | https://www.toshiba.com/tic/power-electronics/ |      |           |      |           |                                                                  |              |     |               |     |                 |              |     |
uninterruptible-power-systems/three-phase/g2020-series-sic-500-to- system,”IEEETrans.PowerElectron.,vol.34,no.6,pp.5787–5802,
| 750-kva |     |     |     |     |     |     |     | Jun.2019. |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[16] MitsubishiElectricPowerProductsInc.SummitSeriesDataSheet500 [36] C. Marxgut, F. Krismer, D. Bortis, and J. W. Kolar, “Ultraflat
|     |     |     |     |     |     |     |     | interleaved | triangular |     | current | mode (TCM) | single-phase |     | PFC rec- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------- | ---------- | ------------ | --- | -------- |
&750kVA.Accessed:Sep.12,2022.[Online].Available:https://www.
|     |     |     |     |     |     |     |     | tifier,” | IEEE | Trans. Power | Electron., |     | vol. 29, | no. 2, pp.873–882, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------------ | ---------- | --- | -------- | ------------------ | --- |
mitsubishicritical.com/media/6317/sa-enl0048-summit-series-data-
| sheet.pdf |     |     |     |     |     |     |     | Feb.2014. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[17] L. Schrittwieser, M. Leibl, M. Haider, F. Thöny, J. W. Kolar, and [37] M. Haider et al., “Novel ZVS S-TCM modulation of three-
T.B.Soeiro, “99.3% efficient three-phase buck-type all-SiC SWISS phase AC/DC converters,” IEEE Open J. Power Electron., vol. 1,
pp.529–543,2020.
| rectifier | for | DC distribution | systems,” |     | IEEE Trans. | Power | Electron., |         |           |                  |     |             |        |              |        |
| --------- | --- | --------------- | --------- | --- | ----------- | ----- | ---------- | ------- | --------- | ---------------- | --- | ----------- | ------ | ------------ | ------ |
|           |     |                 |           |     |             |       |            | [38] M. | Haider et | al., “Analytical |     | calculation | of the | residual ZVS | losses |
vol.34,no.1,pp.126–140,Jan.2019.
[18] Z. Wang, Y. Wu, M. H. Mahmud, Z. Zhao, Y. Zhao, and of TCM-operated single-phase PFC rectifiers,” IEEE Open J. Power
H.A.Mantooth, “Design and validation of a 250-kW all-silicon car- Electron.,vol.2,pp.250–264,2021.
bide high-density three-level T-type inverter,” IEEE J. Emerg. Sel. [39] Q. Huang, R. Yu, Q. Ma, and A. Q. Huang, “Predictive ZVS con-
Topics PowerElectron.,vol.8,no.1,pp.578–588,Mar.2020. trol with improved ZVS time margin and limited variable frequency
|                  |     |      |            |            |           |      |           | range | for a | 99% Efficient, | 130-W/in3 |     | MHz GaN | totem-pole | PFC |
| ---------------- | --- | ---- | ---------- | ---------- | --------- | ---- | --------- | ----- | ----- | -------------- | --------- | --- | ------- | ---------- | --- |
| [19] CLEAResult. |     | What | is 80 PLUS | Certified. | Accessed: | Sep. | 12, 2022. |       |       |                |           |     |         |            |     |
[Online].Available:https://www.clearesult.com/80plus/program-details rectifier,”IEEETrans.PowerElectron.,vol.34,no.7,pp.7079–7091,
| [20] Open | Compute | Project. | (2022). |     | Open Rack | V3  | 48V PSU | Jul.2019. |     |     |     |     |     |     |     |
| --------- | ------- | -------- | ------- | --- | --------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Specification. [Online]. Available: https://www.opencompute.org/wiki/ [40] Z. Liu, F. C. Lee, Q. Li, and Y. Yang, “Design of
Open_Rack/SpecsAndDesigns GaN-based MHz totem-pole PFC rectifier,” IEEE Trans. Emerg.
|     |     |     |     |     |     |     |     | Sel. | Topics | Power | Electron., | vol. | 4, no. | 3, pp.799–807, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ----- | ---------- | ---- | ------ | -------------- | --- |
[21] X.LiandS.Jiang,Google48VRackAdaptationandOnboardPower
| Technology |     | Update.SanJose,CA,USA:OCPGlobalSummit,2019. |     |     |     |     |     | Sep.2016. |     |     |     |     |     |     |     |
| ---------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[22] L.Tian,X.Wu,C.Jiang,andJ.Yang,“Asimplifiedreal-time digital [41] B. Li, Q. Li, F. C. Lee, Z. Liu, and Y. Yang, “High-efficiency high-
control scheme for ZVS four-switch buck–boost with low inductor densitycriticalmoderectifier/inverterforWBG-device-basedon-board
current,” IEEE Trans. Ind. Electron., vol. 69, no. 8, pp.7920–7929, charger,” IEEETrans.Ind. Electron., vol. 64, no. 11, pp.9114–9123,
Nov.2017.
Aug.2022.
[23] Open Data Center Committee. (2020). Panama Power Supply Tech- [42] J. Sun et al., “Mitigation of current distortion for GaN-based CRM
nology White Paper. [Online]. Available: http://www.odcc.org.cn/ totem-pole PFC rectifier with ZVS control,” IEEE Open J. Power
download/p-1248609053405745154.html Electron.,vol.2,pp.290–303,2021.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2454 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
[43] Z. Huang, Z. Liu, F. C. Lee, and Q. Li, “Critical-mode-based soft- [65] K.Shi,“Researchontopologyandcontrolofhighefficiency back-to-
switching modulation for high-frequency three-phase bidirectional backconversion,”Ph.D.dissertation,Dept.Elect.Eng.,ZhejiangUniv.,
AC–DC converters,” IEEE Trans. Power Electron., vol. 34, no. 4, Hangzhou, Zhejiang, China,2019.
pp.3888–3898,Apr.2019. [66] ABB. PowerScale Technical Specifications. Accessed: Sep. 12, 2022.
[44] G. Son, Z. Huang, Q. Li, and F. C. Lee, “Analysis and control [Online]. Available: https://new.abb.com/ups/systems/three-phase-ups/
of critical conduction mode high-frequency single-phase transformer- powerscale/technical-data
less PV inverter,” IEEE Trans. Power Electron., vol. 36, no. 11, [67] DeltaPowerSolutions.DeltaUPSUltronFamily.[Online].Available:
pp.13188–13199,Nov.2021. https://www.deltapowersolutions.com/media/download/Leaflet-UPS-
[45] G. Deboy and O.Häberlen, and M.Treu, “Perspective of loss mech- HPH-G2-20-40-kVA-en-us.pdf
anisms for silicon and wide band-gap power devices,” CPSS Trans. [68] C.Fei,R.Gadelrab,Q.Li,andF.C.Lee,“High-frequencythree-phase
PowerElectron.Appl.,vol.2,no.2,pp.89–100,2017. interleaved LLC resonant converter with GaN devices and integrated
[46] H. Gui et al., “SiC MOSFET versus Si super junction MOSFET- planarmagnetics,”IEEEJ.Emerg.Sel.TopicsPowerElectron.,vol.7,
switching loss comparison in different switching cell configurations,” no.2,pp.653–663,Jun.2019.
| in Proc. | IEEE Energy | Convers. | Congr. | Expo. (ECCE), | Sep. 2018, |            |          |             |       |                   |               |
| -------- | ----------- | -------- | ------ | ------------- | ---------- | ---------- | -------- | ----------- | ----- | ----------------- | ------------- |
|          |             |          |        |               |            | [69] G. C. | Knabben, | J. Scähfer, | J. W. | Kolar, G. Zulauf, | M. J. Kasper, |
pp.6146–6151. and G.Deboy, “Wide-input-voltage-range 3 kW DC-DC converter
[47] A.Agarwal,A.Kanale,andB.J.Baliga,“Advanced650VSiCpower with hybrid LLC & boundary/ discontinuous mode control,” in
MOSFETs with 10 V gate drive compatible with Si superjunction Proc. IEEE Appl. Power Electron. Conf. Expo. (APEC), Mar. 2020,
| devices,”IEEETrans.PowerElectron.,vol.36,no.3,pp.3335–3345, |     |     |     |     |     | pp.1359–1366. |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
Mar.2021. [70] R.Yu,T.Chen,P.Liu,andA.Q.Huang,“A3-Dwindingstructurefor
[48] D.M.Divan,“TheresonantDClinkconverter—Anewconceptinstatic planar transformers and its applications to LLCresonant converters,”
powerconversion,”IEEETrans.Ind.Appl.,vol.25,no.2,pp.317–325, IEEEJ.Emerg.Sel.Top.PowerElectron.,vol.9,no.5,pp.6232–6247,
| Apr.1989. |     |     |     |     |     | Oct.2021. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
[49] G. Venkataramanan, D. M. Divan, and T. M. Jahns, “Discrete pulse [71] R. Gadelrab, A. Nabih, F. C. Lee, and Q. Li, “LLC resonant
modulation strategies for high-frequency inverter systems,” IEEE converter with 99% efficiency for data center server,” in Proc.
Trans.PowerElectron.,vol.8,no.3,pp.279–287,Jul.1993. IEEE Appl. Power Electron. Conf. Expo. (APEC), Jun. 2021,
| [50] D.XuandB.Feng,“NovelZVSthree-phasePFCconvertersandzero- |     |     |     |     |     | pp.310–319. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
voltage-switching space vector modulation (ZVS-SVM) control,” in [72] A. Nabih and Q. Li, “Low-profile and high-efficiency 3 kW
Proc.Int.Conf.PowerElectron. Syst.Appl.,Nov.2004,pp.30–37. 400 V-48 V LLC converter with a matrix of four transformers
[51] Y.Chenetal.,“AZVSgrid-connectedfull-bridgeinverterwithanovel and inductors for 48 V power architecture for data centers,” in
|                       |          |      |              |            |                 | Proc.         | IEEE Energy | Convers. | Congr. | Expo. (ECCE), | Oct. 2021, |
| --------------------- | -------- | ---- | ------------ | ---------- | --------------- | ------------- | ----------- | -------- | ------ | ------------- | ---------- |
| ZVS SPWM              | scheme,” | IEEE | Trans. Power | Electron., | vol. 31, no. 5, |               |             |          |        |               |            |
| pp.3626–3638,May2016. |          |      |              |            |                 | pp.1813–1819. |             |          |        |               |            |
[52] N. He, Y. Zhu, A. Zhao, and D. Xu, “Zero-voltage-switching [73] M. K. Ranjram and D. J. Perreault, “A 380-12 V, 1-kW, 1-MHz
sinusoidal pulsewidth modulation method for three-phase four-wire converterusingaminiaturizedsplit-phase,fractional-turnplanartrans-
inverter,”IEEETrans.PowerElectron.,vol.34,no.8,pp.7192–7205, former,”IEEETrans.PowerElectron.,vol.37,no.2,pp.1666–1681,
| Aug.2019. |     |     |     |     |     | Feb.2022. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
[53] N. He, M. Chen, J. Wu, N. Zhu, and D. Xu, “20-kW zero-voltage- [74] G.C. Knabben, J.Schäfer, L.Peluso, J.W.Kolar, M.J.Kasper, and
switching SiC-MOSFET grid inverter with 300 kHz switching fre- G.Deboy, “New PCB winding ‘snake-core’ matrix transformer for
quency,”IEEETrans.PowerElectron.,vol.34,no.6,pp.5175–5190, ultra-compact wide DC input voltage range hybrid B+DCM resonant
Jun.2019. server powersupply,”inProc.IEEEInt.Power Electron. Appl.Conf.
[54] Y.Chen,M.Chen,andD.Xu,“A3-kWtwo-stagetransformerlessPV Expo.,Nov.2018,pp.1–6.
inverterwithresonantDClinkandZVS-PWMoperation,”IEEETrans. [75] F. C. Lee, Q. Li, and A. Nabih, “High frequency resonant con-
Ind.Appl.,vol.57,no.2,pp.1495–1506,Apr.2021. verters: An overview on the magnetic design and control methods,”
[55] Y. Wu, N. He, M. Chen, and D. Xu, “Generalized space-vector- IEEE J. Emerg. Sel. Top. Power Electron., vol. 9, no. 1, pp.11–23,
| modulation | method | for soft-switching |     | three-phase | inverters,” IEEE | Feb.2021. |     |     |     |     |     |
| ---------- | ------ | ------------------ | --- | ----------- | ---------------- | --------- | --- | --- | --- | --- | --- |
Trans.PowerElectron.,vol.36,no.5,pp.6030–6045,May2021. [76] G. Li and X. Wu, “A 98.4% efficiency 380 V-12 V DCX with
|              |          |          |        |                             |     | 1.3 kW/in3 | power | density | using | low NFoM devices | and resonant |
| ------------ | -------- | -------- | ------ | --------------------------- | --- | ---------- | ----- | ------- | ----- | ---------------- | ------------ |
| [56] K. Shi, | A. Zhao, | J. Deng, | and D. | Xu, “Zero-voltage-switching |     |            |       |         |       |                  |              |
SiC-MOSFET three-phase four-wire back-to-back converter,” IEEE drive transformer,” IEEE Trans. Power Electron., vol. 37, no. 10,
J. Emerg. Sel. Topics Power Electron., vol. 7, no. 2, pp.722–735, pp.12346–12356,Oct.2022.
Jun.2019. [77] B. Majmunovic and D. Maksimovic, “400-48-V stacked active
[57] K. Shi, J. Deng, and D. Xu, “A general pulse width modulation bridge converter,” IEEE Trans. Power Electron., vol. 37, no. 10,
method forzero-voltage-switching active-clamping three-phase power pp.12017–12029,Oct.2022.
converters: Edge aligned pulse width modulation (EA-PWM),” IEEE [78] S.T.Hung,D.C.Hopkins,andC.R.Mosling, “Extensionofbattery
OpenJ.PowerElectron.,vol.1,pp.250–259,2020. life via charge equalization control,” IEEE Trans. Ind. Electron.,
[58] J. Deng, K. Shi, M. Chen, and D.Xu, “Analysis and design of zero- vol.40,no.1,pp.96–104,Feb.1993.
voltage-switching multiphaseAC/DCconverters,”IEEEJ.Emerg.Sel. [79] N.H.Kutkut,D.M.Divan,andD.W.Novotny,“Chargeequalization
TopicsPowerElectron.,vol.10,no.6,pp.6495–6510,Dec.2022,doi: forseries connected battery strings,” IEEETrans. Ind.Appl., vol. 31,
| 10.1109/JESTPE.2021.3129322. |     |     |     |     |     | no.3,pp.562–568,May1995. |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
[59] D. Xu,R. Li,N.He, J.Deng, andY. Wu,Soft-Switching Technology [80] T.Shimizu,M.Hirakata,T.Kamezawa,andH.Watanabe,“Generation
for Three-Phase Power Electronics Converters. Hoboken, NJ, USA: controlcircuitforphotovoltaicmodules,”IEEETrans.PowerElectron.,
| Wiley, 2022. |     |     |     |     |     | vol.16,no.3,pp.293–300,May2001. |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
[60] A. Nabae, I.Takahashi, and H.Akagi, “A new neutral-point-clamped [81] P.S.Shenoy,K.A.Kim,B.B.Johnson,andP.T.Krein,“Differential
PWMinverter,”IEEETrans.Ind.Appl.,vol.IA-17,no.5,pp.518–523, power processing for increased energy production and reliability of
Sep.1981. photovoltaic systems,” IEEE Trans. Power Electron., vol. 28, no. 6,
[61] M.SchweizerandJ.W.Kolar,“Designandimplementationofahighly pp.2968–2979,Jun.2013.
efficient three-level T-type converter for low-voltage applications,” [82] Y. Jeon, H. Lee, K. A. Kim, and J. Park, “Least power point
IEEETrans.PowerElectron.,vol.28,no.2,pp.899–907,Feb.2013. tracking method for photovoltaic differential power processing sys-
[62] Fuji Electric Co., Ltd. Hybrid SiC Modules. [Online]. Avail- tems,” IEEE Trans. Power Electron., vol. 32, no. 3, pp.1941–1951,
| able: https://www.fujielectric.com/products/semiconductor/model/sic/ |     |     |     |     |     | Mar.2017. |     |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
hybrid.html [83] E. Candan, P. S. Shenoy, and R. C. N. Pilawa-Podgurski, “A series
[63] Infineon Technologies AG. (Jun. 29, 2020). EasyPAC 650 V, 200 stacked power delivery architecture with isolated differential power
A 3-Level IGBT Module With TRENCHSTOP 5, CoolSiC Schottky conversion for data centers,” IEEE Trans. Power Electron., vol. 31,
Diode. [Online]. Available: https://www.infineon.com/cms/en/product/ no.5,pp.3690–3703,May2016.
power/igbt/igbt-modules/f3l200r07w2s5f_b11
|     |     |     |     |     |     | [84] P. Wang, | Y.  | Chen, J. Yuan, | R.  | C. N. Pilawa-Podgurski, | and M. |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ----------------------- | ------ |
[64] Fuji Electric Co., Ltd. Uninterruptible Power Supply Systems Chen, “Differential power processing for ultra-efficient data stor-
UPS7300WX-T3U. Accessed: Jun. 15, 2022. [Online]. Available: age,” IEEE Trans. Power Electron., vol. 36, no. 4, pp.4269–4286,
| https://americas.fujielectric.com/products/ups/ups7300wx-t3u/ |     |     |     |     |     | Apr.2021. |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

CHENetal.: DATACENTERPOWERSUPPLYSYSTEMS:FROMGRIDEDGETOPOINT-OF-LOAD 2455
[85] S.K.Lee,T.Tong,X.Zhang,D.Brooks,andG.-Y.Wei,“A16-core [107] N. Desai et al., “A 32-A, 5-V-input, 94.2% peak efficiency high-
voltage-stacked system with adaptive clocking and an integrated frequency power converter module featuring package-integrated low-
switched-capacitor DC–DCconverter,” IEEETrans.VeryLargeScale voltage GaN nMOS power transistors,” IEEE J. Solid-State Circuits,
Integr. (VLSI)Syst.,vol.25,no.4,pp.1271–1284,Apr.2017. vol.57,no.4,pp.1090–1099,Apr.2022.
[86] H. Jeong, H. Lee, Y. Liu, and K. A. Kim, “Review of differential [108] P. Vinciarelli, “Factorized power architecture with point of load sine
power processing converter techniques for photovoltaic applications,” amplitude converters,” U.S.Patent6984965B2,Jan.10,2006.
IEEETrans,EnergyConvers.,vol.34,no.1,pp.351–360,Mar.2019. [109] Vicor.PRMPRM48BH480T250A00andVTMVTM48MP010x107AA1.
Accessed:May20,2022.[Online].Available:https://www.vicorpower.
| [87] C.LiandJ.A.Cobos,“Classificationofdifferential |     |     |     |     |     | powerprocessing |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
architectures based on VA area modeling,” IEEE J. Emerg. Sel. Top. com/dc-dc/isolated-regulated/buck-boost-current-multipliers
Power Electron., vol. 10, no. 6, pp.7849–7866, Dec. 2022, doi: [110] M. H. Ahmed, C. Fei, F. C. Lee, and Q. Li, “Single-stage high-
10.1109/JESTPE.2021.3093654. efficiency 48/1 V sigma converter with integrated magnetics,” IEEE
Trans.Ind.Electron.,vol.67,no.1,pp.192–202,Jan.2020.
| [88] P. Wang | and | M. Chen, | “Analysis | and | design | of series | voltage com- |     |     |     |     |     |     |     |     |
| ------------ | --- | -------- | --------- | --- | ------ | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
pensator for differential power processing,” IEEE J. Emerg. Sel. Top. [111] X.Peng,Y.Ren,Y.Mao,andF.C.Lee,“Afamilyofnovelinterleaved
Power Electron., vol. 10, no. 6, pp.7890–7903, Dec. 2022, doi: DC/DCconvertersforlow-voltagehigh-currentvoltageregulatormod-
10.1109/JESTPE.2021.3116091. uleapplications,”inProc.IEEEPowerElectron.Spec.Conf.,Jun.2001,
| [89] X.Zhou,P.-L.Wong,P.Xu,F.C.Lee,andA.Q.Huang,“Investigation |     |     |     |     |     |     |     | pp.1507–1511. |        |              |     |       |                     |     |             |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ------------ | --- | ----- | ------------------- | --- | ----------- |
|                                                                |     |     |     |     |     |     |     | [112] M.      | Ye, P. | Xu, B. Yang, | and | F. C. | Lee, “Investigation |     | of topology |
ofcandidateVRMtopologiesforfuturemicroprocessors,”IEEETrans.
PowerElectron.,vol.15,no.6,pp.1172–1182,Nov.2000. candidatesfor48VVRM,”inProc.IEEEAppl.PowerElectron.Conf.
[90] Y.Ren,M.Xu,J.Sun,andF.C.Lee,“Afamilyofhighpowerdensity Expo.,Mar.2002,pp.699–705.
unregulated bus converters,” IEEE Trans. Power Electron., vol. 20, [113] P. Xu, M. Ye, P.-L. Wong, and F. C. Lee, “Design of 48 V Voltage
|     |     |     |     |     |     |     |     | regulator | modules | with | a novel | integrated | magnetics,” |     | IEEE Trans. |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---- | ------- | ---------- | ----------- | --- | ----------- |
no.5,pp.1045–1054,Sep.2005.
|            |         |           |     |           |     |               |          | PowerElectron., |     | vol.17,no.6,pp.990–998,Nov.2002. |     |     |     |     |     |
| ---------- | ------- | --------- | --- | --------- | --- | ------------- | -------- | --------------- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| [91] D. F. | D. Tan, | “A review | of  | immediate | bus | architecture: | A system |                 |     |                                  |     |     |     |     |     |
perspective,”IEEEJ.Emerg.Sel.TopicsPowerElectron.,vol.2,no.3, [114] Y.Zhang,D.Xu,M.Chen,Y.Han,andZ.Du,“LLCresonantconverter
pp.363–373,Sep.2014. for48Vto0.9VVRM,”inProc.IEEEPowerElectron.Spec.Conf.,
Jun.2004,pp.1848–1854.
| [92] M. H. | Ahmed,     | C. Fei,  | F. C.           | Lee, and | Q. Li,      | “48-V             | voltage regu- |                                                 |              |                  |           |            |                          |            |            |
| ---------- | ---------- | -------- | --------------- | -------- | ----------- | ----------------- | ------------- | ----------------------------------------------- | ------------ | ---------------- | --------- | ---------- | ------------------------ | ---------- | ---------- |
|            |            |          |                 |          |             |                   |               | [115] Using                                     | the          | LMG5200POLEVM-10 |           |            | 48V to Point             | of         | Load EVM,  |
| lator      | module     | with PCB | winding         | matrix   | transformer | for               | future data   |                                                 |              |                  |           |            |                          |            |            |
|            |            |          |                 |          |             |                   |               | Texas                                           | Instruments, |                  | Dallas,   | TX, USA,   | 2017.                    | [Online].  | Available: |
| centers,”  | IEEETrans. |          | Ind. Electron., | vol.     | 64, no.     | 12, pp.9302–9310, |               |                                                 |              |                  |           |            |                          |            |            |
| Dec.2017.  |            |          |                 |          |             |                   |               | https://www.ti.com/lit/ug/snvu520b/snvu520b.pdf |              |                  |           |            |                          |            |            |
|            |            |          |                 |          |             |                   |               | [116] Bel.                                      | (2020).      | Main &           | Satellite | Power      | Stamp                    | 48V-to-PoL | Isolated   |
| [93] M. H. | Ahmed,     | F. C.    | Lee, and        | Q. Li,   | “Two-stage  | 48-V              | VRM with      |                                                 |              |                  |           |            |                          |            |            |
|            |            |          |                 |          |             |                   |               | DC-DC                                           | Converters.  |                  | [Online]. | Available: | https://www.belfuse.com/ |            |            |
intermediatebusvoltageoptimizationfordatacenters,”IEEEJ.Emerg.
resources/datasheets/powersolutions/ds-bps-48-v-to-pol-power-
| Sel.Topics | PowerElectron.,vol.9,no.1,pp.702–715,Feb.2021. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stamp.pdf
[94] G.LiandX.Wu,“Highpowerdensity48–12VDCXwith3-DPCB
winding transformer,” IEEE Trans. Power Electron., vol. 35, no. 2, [117] S. Saggini, O. Zambetti, R. Rizzolatti, M. Picca, and P. Mattavelli,
“Anisolatedquasi-resonantmultiphasesingle-stagetopologyfor48V
pp.1189–1193,Feb.2020.
|          |      |        |            |            |     |       |          | VRM | applications,” |     | IEEE Trans. | Power | Electron., | vol. | 33, no. 7, |
| -------- | ---- | ------ | ---------- | ---------- | --- | ----- | -------- | --- | -------------- | --- | ----------- | ----- | ---------- | ---- | ---------- |
| [95] 48V | Data | Center | Solutions. | Monolithic |     | Power | Systems. |     |                |     |             |       |            |      |            |
pp.6224–6237,Jul.2018.
| Accessed: | May | 20, 2022. | [Online]. | Available: |     | https://www.monolit- |     |          |              |     |           |       |            |        |               |
| --------- | --- | --------- | --------- | ---------- | --- | -------------------- | --- | -------- | ------------ | --- | --------- | ----- | ---------- | ------ | ------------- |
|           |     |           |           |            |     |                      |     | [118] F. | Li, L. Wang, | and | L. Yu, “A | novel | integrated | matrix | magnetics for |
hicpower.com/en/products/power-management/48v-data-center.html isolatedsingle-stageDC-DCconverter,” IEEETrans.PowerElectron.,
| [96] S. Jiang, | S.  | Saggini, | C. Nan, | X. Li, | C. Chung, | and | M. Yazdani, |     |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ------- | ------ | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.37,no.10,pp.12380–12390,Oct.2022.
| “Switched | tank | converters,” | IEEE | Trans. | Power | Electron., | vol. 34, |     |     |     |     |     |     |     |     |
| --------- | ---- | ------------ | ---- | ------ | ----- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[119] X.LouandQ.Li,“300Asingle-stage48Vvoltageregulatorwithmul-
no.6,pp.5048–5062,Jun.2019.
|              |        |         |           |     |         |                |       | tiphase | current | doubler | rectifier | and | integrated | transformer,” | in Proc. |
| ------------ | ------ | ------- | --------- | --- | ------- | -------------- | ----- | ------- | ------- | ------- | --------- | --- | ---------- | ------------- | -------- |
| [97] X. Lyu, | Y. Li, | N. Ren, | S. Jiang, | and | D. Cao, | “A comparative | study |         |         |         |           |     |            |               |          |
ofswitched-tankconverterandcascadedvoltagedividerfor48-Vdata IEEEAppl.PowerElectron. Conf.Expo.,Mar.2022,pp.1004–1010.
|        |               |        |            |     |                     |     |        | [120] M.  | Halamicek, | T. McRae, |     | and A. | Prodic, “Cross-coupled |          | series-    |
| ------ | ------------- | ------ | ---------- | --- | ------------------- | --- | ------ | --------- | ---------- | --------- | --- | ------ | ---------------------- | -------- | ---------- |
| center | application,” | IEEEJ. | Emerg.Sel. |     | Top.PowerElectron., |     | vol.8, |           |            |           |     |        |                        |          |            |
|        |               |        |            |     |                     |     |        | capacitor | quadruple  | step-down |     | buck   | converter,”            | in Proc. | IEEE Appl. |
no.2,pp.1547–1559,Jun.2020.
|     |     |     |     |     |     |     |     | Power | Electron. | Conf. | Expo., | New | Orleans, LA, | USA, | Mar. 2020, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ----- | ------ | --- | ------------ | ---- | ---------- |
[98] Z.Ye,Y.Lei,andR.C.N.Pilawa-Podgurski,“Thecascadedresonant
pp.1–6.
converter: A hybrid switched-capacitor topology with high power [121] G.Seo,R.Das,andH.Le,“Dualinductorhybridconverterforpoint-
| density | and efficiency,” |     | IEEE | Trans. Power | Electron., |     | vol. 35, no. | 5,      |         |           |           |      |        |             |          |
| ------- | ---------------- | --- | ---- | ------------ | ---------- | --- | ------------ | ------- | ------- | --------- | --------- | ---- | ------ | ----------- | -------- |
|         |                  |     |      |              |            |     |              | of-load | voltage | regulator | modules,” | IEEE | Trans. | Ind. Appl., | vol. 56, |
pp.4946–4958,May2020.
no.1,pp.367–377,Jan./Feb.2020.
| [99] R. Rizzolatti, |     | C. Rainer, | S.  | Saggini, | and M. | Ursino, | “High den- |          |        |                  |                  |     |      |         |           |
| ------------------- | --- | ---------- | --- | -------- | ------ | ------- | ---------- | -------- | ------ | ---------------- | ---------------- | --- | ---- | ------- | --------- |
|                     |     |            |     |          |        |         |            | [122] H. | Cao et | al., “A 12-level | series-capacitor |     | 48-1 | V DC-DC | converter |
sity hybrid switched capacitor converter for data-center applica- withon-chipswitchandGaNhybridpowerconversion,”IEEEJ.Solid-
tion,” in Proc. IEEE Appl. Power Electron. Conf. Expo., Jun. 2021, StateCircuits.,vol.56,no.12,pp.3628–3638,Dec.2021.
pp.1288–1293.
|              |           |             |             |                  |             |         |               | [123] Y. | Zhu, T. | Ge, Z. Ye,         | and R. | C. N.     | Pilawa-Podgurski, |     | “A Dickson- |
| ------------ | --------- | ----------- | ----------- | ---------------- | ----------- | ------- | ------------- | -------- | ------- | ------------------ | ------ | --------- | ----------------- | --- | ----------- |
| [100] J. Zhu | and D.    | Maksimovic, |             | “Transformerless |             | stacked | active bridge |          |         |                    |        |           |                   |     |             |
|              |           |             |             |                  |             |         |               | squared  | hybrid  | switched-capacitor |        | converter | fordirect         | 48  | V topoint-  |
| converters:  | Analysis, |             | properties, | and              | synthesis,” | IEEE    | Trans. Power  |          |         |                    |        |           |                   |     |             |
of-loadconversion,”inProc.IEEEAppl.PowerElectron.Conf.Expo.,
Electron., vol.36,no.7,pp.7914–7926,Jul.2021. Mar.2022,pp.1272–1278.
[101] C. Li and J. A. Cobos, “A switched capacitor and autotransformer [124] N.M.EllisandR.C.N.Pilawa-Podgurski,“Asymmetricdual-inductor
hybridconverterwithDCcurrentinthewindings,”IEEETrans.Power
hybridDicksonconverterfordirect48V-to-PoLconversion,”inProc.
| Electron., | vol.37,no.2,pp.1870–1884,Feb.2022. |     |     |     |     |     |     |                         |     |     |     |                                   |     |     |     |
| ---------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --------------------------------- | --- | --- | --- |
|            |                                    |     |     |     |     |     |     | IEEEAppl.PowerElectron. |     |     |     | Conf.Expo.,Mar.2022,pp.1267–1271. |     |     |     |
[102] Hybrid Switched-Capacitor (HSC) Intermediate Bus Converter. Infi- [125] K. Nishijima, K. Harada, T. Nakano, T. Nabeshima, and T. Sato,
neonTechnologies AG.Accessed:May20,2022.[Online].Available: “Analysis of double step-down two-phase buck converter for VRM,”
https://www.infineon.com/cms/en/applications/communication/48v- inProc.IEEETelecommun. EnergyConf.,Sep.2005,pp.497–502.
power-distribution/hsc-topology/
|     |     |     |     |     |     |     |     | [126] Y.Jang,M.M.Jovanovic, |     |     | andY.Panov,“Multiphase |     |     | buckconverters |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ---------------------- | --- | --- | -------------- | --- |
[103] LTM4664-54VIN Dual 25A, Single 50A μModule Regulator With withextendeddutycycle,”inProc.IEEEAppl.PowerElectron.Conf.
Digital Power System Management, Analog Devices, Norwood, MA, Expo.,Mar.2006,pp.38–44.
USA, 2021. Accessed: May 20, 2022. [Online]. Available: https:// [127] Y. Chen, D. M. Giuliano, and M. Chen, “Two-stage 48V-1 V hybrid
www.analog.com/en/products/ltm4664.html switched-capacitorpoint-of-loadconverterwith24Vintermediatebus,”
| [104] W. C. | Liu, Z. | Ye, and | R. C. | N. Pilawa-Podgurski, |     |     | “A 97% peak |                                    |     |     |     |     |                         |     |     |
| ----------- | ------- | ------- | ----- | -------------------- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- |
|             |         |         |       |                      |     |     |             | inProc.IEEEWorkshopControlModeling |     |     |     |     | PowerElectron.,Aalborg, |     |     |
efficiency and 308 A/in3 current density 48-to-4 V two-stage res- Denmark,Nov.2020,pp.1–8.
onant switched-capacitor converter for data center applications,” in [128] Y.Chenetal.,“VirtualintermediatebusCPUvoltageregulator,”IEEE
Proc. IEEE Appl. Power Electron. Conf. Expo. (APEC), Mar. 2020, Trans.PowerElectron.,vol.37,no.6,pp.6883–6898,Jun.2022.
pp.468–474. [129] Murata Manufacturing Co., Ltd. 68mm 1U 3600W Front End Power
[105] J. Baek et al., “Vertical stacked LEGO-PoL CPU voltage regulator,” Supply Module. Accessed: Nov. 10, 2022. [Online]. Available:
IEEETrans.PowerElectron.,vol.37,no.6,pp.6305–6322,Jun.2022. https://www.murata.com/en-us/products/power/open-compute/
[106] Z.Ye,R.A.Abramson,T.Ge,andR.C.N.Pilawa-Podgurski,“Multi- overview/lineup/psu
resonantswitched-capacitorconverter:Achievinghighconversionratio [130] Artesyn. ARTESYN 50V 3kW OPEN RACK V3 PSU.
with reduced component number,” IEEE Open J. Power Electron., Accessed: Nov. 10, 2022. [Online]. Available: https://www.artesyn.
| vol.3,pp.492–507,2022. |     |     |     |     |     |     |     | com/documents/644 |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.

2456 IEEEJOURNALOFEMERGINGANDSELECTEDTOPICSINPOWERELECTRONICS,VOL.11,NO.3,JUNE2023
Yenan Chen (Member, IEEE)received the Honors Min Chen (Senior Member, IEEE) received the
degreeinengineeringfromtheChuKochenCollege, bachelor’s and Ph.D. degrees in electrical engi-
ZhejiangUniversity,Hangzhou,China,in2010,and neering fromtheCollege ofElectrical Engineering,
the bachelor’s andPh.D.degrees inelectrical engi- ZhejiangUniversity, Hangzhou,China,in1998and
|     | neering | fromtheCollege | ofElectrical |     | Engineering, |     |     | 2004,respectively. |     |     |     |     |     |
| --- | ------- | -------------- | ------------ | --- | ------------ | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ZhejiangUniversity,in2010and2018,respectively. He is currently a Professor with Zhejiang Uni-
From 2018 to 2021, he was a Post-Doctoral versity. His research interests include power device
Research Associate with the Department of Elec- packaging, high-frequency high-power conversion,
trical Engineering, Princeton University, Princeton, andrenewable energypowerconversion systems.
NJ, USA. Since December 2021, he has been a Dr.ChenisanAssociateEditoroftheIEEEOPEN
Research Scientist andaPrincipal Investigator with JOURNALOFPOWERELECTRONICS.
| the ZJU-Hangzhou       | Global Scientific          | and      | Technological     | Innovation  | Center     |     |     |                                            |     |     |     |     |     |
| ---------------------- | -------------------------- | -------- | ----------------- | ----------- | ---------- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
| and the College        | of Electrical Engineering, |          | Zhejiang          | University. | He holds   |     |     |                                            |     |     |     |     |     |
| five issued            | Chinese patents. His       | research | interests include | power       | electronic |     |     |                                            |     |     |     |     |     |
| topology, architecture | and control                | for data | center,           | renewable   | energy and |     |     |                                            |     |     |     |     |     |
| transportation.        |                            |          |                   |             |            |     |     | DehongXu(Fellow,IEEE)receivedtheB.S.,M.S., |     |     |     |     |     |
Dr.Chenwasarecipient oftwoPrizePaperAwardsoftheIEEE TRANS- andPh.D.degreesinelectricalengineeringfromthe
ACTIONSONPOWERELECTRONICSin2021and2022, the IEEECOMPEL CollegeofElectrical Engineering, ZhejiangUniver-
BestPaperAwardin2020,theIEEEApplied PowerElectronics Conference sity, Hangzhou, China, in 1983, 1986, and 1989,
andExposition(APEC)OutstandingPresentationAwardin2019,andtheFirst respectively.
PlaceAwardfromtheInnovation ForumofPrinceton University in2019. Since 1996, he has been with the College of
ElectricalEngineering,ZhejiangUniversity,asaFull
|     |     |     |     |     |     |     |     | Professor. | From June | 1995     | to May     | 1996, | he was |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | -------- | ---------- | ----- | ------ |
|     |     |     |     |     |     |     |     | a Visiting | Scholar   | with The | University | of    | Tokyo, |
Tokyo,Japan.FromJunetoDecember2000,hewas
aVisitingProfessorwiththeCenterforPowerElec-
tronicsSystems,VirginiaTech,Blacksburg,VA,USA.FromFebruarytoApril
2006,hewasaVisitingProfessorwiththeETHZürich,Zürich,Switzerland.
|     |     |     |     |     |     | He is interested | in  | power electronics | topology, | control, | and | applications | to  |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------- | --------- | -------- | --- | ------------ | --- |
renewableenergyandenergyefficiency.Heauthoredorcoauthoredtenbooks
Keyan Shi received the bachelor’s degree in elec- andmorethan300IEEEjournalsandconferencepapers.Heholdsmorethan
|     | tronics | and information | engineering |     | and the Ph.D. | 50patents. |                    |     |            |     |            |             |     |
| --- | ------- | --------------- | ----------- | --- | ------------- | ---------- | ------------------ | --- | ---------- | --- | ---------- | ----------- | --- |
|     |         |                 |             |     |               | Dr. Xu is  | the Vice-President | for | Membership | of  | IEEE Power | Electronics |     |
|     | degree  | in electrical   | engineering |     | from the Col- |            |                    |     |            |     |            |             |     |
Societyfrom2022.HewastherecipientofsevenIEEEjournalandconference
|     | lege ofElectrical |     | Engineering, | Zhejiang | University, |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ------------ | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Hangzhou, China,in2010and2020,respectively. paperawards.HewasanIEEEPELSDistinguishLecturerfrom2015to2018.
HeiscurrentlyworkingasaSeniorSystemEngi- Hewasalsoarecipient oftheIEEEPELSR.D.Middlebrook Achievement
neeratHoymilesPowerElectronicsInc.,Hangzhou, Awardin2016.HewastheGeneralChairofIEEEInternational Symposium
|     |     |     |     |     |     | on Industrial | Electronics | (ISIE2012, | Hangzhou) | and | the IEEE | International |     |
| --- | --- | --- | --- | --- | --- | ------------- | ----------- | ---------- | --------- | --- | -------- | ------------- | --- |
China.Hisresearchinterestsincludehigh-efficiency
PowerElectronicsandApplicationsConference(PEAC2018,Shenzhen).Heis
|     | powerconversion |     | systemanditscontrolstrategy. |     |     |                        |     |         |                               |     |     |     |     |
| --- | --------------- | --- | ---------------------------- | --- | --- | ---------------------- | --- | ------- | ----------------------------- | --- | --- | --- | --- |
|     |                 |     |                              |     |     | the Co-editor-in-Chief |     | of IEEE | OPENJOURNALOFPOWERELECTRONICS |     |     |     |     |
andanAssociateEditorofIEEETRANSACTIONSONPOWERELECTRONICS.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:28:48 UTC from IEEE Xplore.  Restrictions apply.