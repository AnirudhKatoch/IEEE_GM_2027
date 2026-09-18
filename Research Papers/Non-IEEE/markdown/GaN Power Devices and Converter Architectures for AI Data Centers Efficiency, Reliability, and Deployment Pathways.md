GaN Power Devices and Converter Architectures for
AI Data Centers: Efficiency, Reliability, and
Deployment Pathways
Donald Intal, Abasifreke Ebong
Department of Electrical and Computer Engineering
University of North Carolina at Charlotte
Charlotte, North Carolina 28223
Email: dintal@charlotte.edu, aebong1@charlotte.edu
Abstract—The rapid growth of artificial-intelligence workloads reliability,transient-response,anduptimerequirements[2].This
is increasing the electrical and thermal demands placed on growth creates a critical power-electronics bottleneck upstream
data-center power-delivery systems, making conversion efficiency, of the computing hardware: the efficiency, power density, and
power density, and reliability critical infrastructure-level consid-
thermal behavior of the conversion and distribution chain that
erations. This review examines how gallium-nitride (GaN) power
devices can be matched to specific stages of the grid-to-load transfers energy from the utility interface to the processor
conversion chain, including front-end power-factor correction, point of load [2]. As illustrated in Fig. 2, this chain commonly
isolatedDC/DCconversion,48-Vintermediate-busconversion,and includesAC/DCrectificationandpower-factorcorrection,high-
point-of-load regulation. The material and device characteristics
voltage bus regulation, isolated intermediate-bus conversion,
of Si, SiC, and GaN are first compared using converter-
and point-of-load regulation. Losses introduced at each stage
relevant metrics, after which lateral, vertical, and specialized
GaN architectures are evaluated in terms of voltage scalability, appearprimarilyaswasteheat,increasingboththeinputpower
switching behavior, reverse conduction, thermal pathways, gate required to support a given computational load and the cooling
control, and technology maturity. The analysis shows that GaN demand imposed on the facility [3]. The resulting interaction
provides a stage-dependent rather than universal advantage.
among conversion loss, waste-heat generation, and cooling
Commercially mature lateral GaN HEMTs are particularly
overhead is conceptually summarized in Fig. 1.
effective in high-frequency, low-to-mid-voltage stages where
switching and commutation losses strongly influence efficiency
and passive-component volume. Specialized and hybrid devices
extend this capability to bidirectional operation, normally-off
control, extreme conversion ratios, and functional integration,
whileverticalGaNremainsanemergingoptionforhigher-voltage
and higher-power conversion. A quantitative framework is also
presented to connect cascaded converter efficiency with electrical-
loss reduction, cooling demand, annual facility energy use, and
operational carbon emissions. The resulting benefits depend on
the fraction of load processed, operating profile, cooling-system
performance,andgridcarbonintensity.Broaddeploymentfurther
requires low-parasitic packaging, disciplined gate-drive and Fig.1. Conceptualrelationshipbetweenconversionlosses,wasteheat,and
EMI co-design, mission-profile reliability qualification, scalable coolingoverhead.
manufacturing, and supply-chain resilience. GaN is therefore
best treated as a stage-specific system lever whose value emerges In this context, advances in power electronics are not
through coordinated device–topology–package–thermal co-design.
merely incremental component-level improvements; they can
act as first-order levers on facility energy consumption and
Index Terms—AI data centers, data-center power delivery,
operationalemissions[2].Higherconversionefficiencydirectly
gallium nitride, GaN power devices, high-frequency power
conversion, intermediate-bus converters, lateral GaN HEMTs, reduces electrical loss, while lower dissipated power reduces
point-of-loadconverters,powerconversionefficiency,powerfactor the thermal load that must be removed by cooling systems.
correction, thermal management, vertical GaN devices, wide- Together, these effects can improve power usage effectiveness
bandgap semiconductors.
(PUE) and reduce the electricity required per unit of delivered
computational work [1]. For AI-oriented facilities operating
I. INTRODUCTION
continuously at high utilization, even sub-percentage-point
Artificial intelligence (AI) is rapidly reshaping the energy improvements in stages that process the full rack or facility
footprint of digital infrastructure [1]. As training and inference power can therefore translate into meaningful reductions in
workloads scale, data centers must deliver increasing electrical energy use, operating cost, and carbon intensity, particularly
power to processors and accelerators while maintaining strict where the electricity supply remains partially fossil based.
6202
nuJ
42
]hp-ppa.scisyhp[
1v18252.6062:viXra

Fig.2. PowerconversionanddistributionchaininanAI/data-centerenvironment.
Silicon power devices have benefited from decades of switchingfrequencies,conversionratios,andthermalconditions.
technological optimization, but their performance becomes A portfolio of GaN architectures therefore provides a broader
increasingly constrained as converter designs move toward design space for matching device characteristics to stage-
higher switching frequency, higher volumetric power density, specificrequirementswhilebalancingefficiency,powerdensity,
andtighterthermalmargins[4].Increasingswitchingfrequency controllability, and reliability [6, 7].
can reduce the volume of magnetic and capacitive components, Lateral GaN/AlGaN high-electron-mobility transistors
but it also raises switching loss, electromagnetic-interference (HEMTs) are currently the most mature GaN devices for
(EMI)sensitivity,andstressassociatedwithparasiticinductance high-frequency, low-to-mid-voltage power conversion. Their
and capacitance. These challenges are intensified by sustained operationisbasedonthepolarization-inducedtwo-dimensional
24/7operationandtherapidloadtransientscharacteristicofpro- electrongas(2DEG)formedattheAlGaN/GaNheterointerface,
cessor and accelerator platforms. Consequently, wide-bandgap which provides a high-mobility conduction channel with low
semiconductors are receiving increased attention because they channel resistance [6]. In data-center converters, lateral GaN
can support higher electric fields and faster switching while HEMTs are attractive because their low switching charge and
maintaining competitive conduction loss and thermal stability absence of a conventional silicon MOSFET body diode can
[4]. The qualitative relationship among switching frequency, substantially reduce switching and reverse-recovery-related
achievable power density, and semiconductor technology is losses [8, 7]. These characteristics are particularly valuable in
illustrated in Fig. 3. high-frequency PFC, resonant DC/DC, intermediate-bus, and
Gallium nitride (GaN) has emerged as a particularly com- point-of-load stages, where converter efficiency and volumetric
pelling wide-bandgap platform for next-generation power power density are both critical [7].
conversion[5,4].GaNhasabandgapofapproximately3.4eV, Vertical GaN devices provide a complementary pathway for
acriticalbreakdownfieldontheorderof3.0–3.5MV/cm,and voltage and current ranges in which lateral drift-region scaling
high electron transport capability, including a higher saturated becomesincreasinglyrestrictive.Byconductingcurrentthrough
electron velocity than silicon. These properties enable devices thesemiconductorbulkratherthanparalleltothewafersurface,
that sustain high electric fields using compact active regions vertical architectures can scale blocking voltage through the
and that operate with reduced charge-related switching loss. drift-layer thickness while supporting higher current density
At the converter level, GaN can reduce switching loss through and potentially more direct heat-extraction paths [9, 10]. These
low device capacitances, limited stored charge, and rapid characteristicsarerelevanttohigher-powerstagessuchaspower
voltageandcurrenttransitions, whilelow on-resistancedesigns distribution units, uninterruptible power supplies, high-voltage
can limit conduction loss. These attributes support increased DC/DC converters, and emerging high-voltage DC distribution
switching frequency, reduced passive-component volume, and architectures,whereconductionloss,breakdowncapability,and
higherconverterpowerdensity,consistentwiththetrendshown thermal stability must be maintained under sustained loading
in Fig. 3. [9,10].ThedistinctionbetweenlateralandverticalGaNshould
The relevance of GaN to data-center power delivery is therefore not be treated as a simple replacement hierarchy.
determined not only by its intrinsic material properties but also Instead, the two architectures occupy complementary regions
by the structural diversity of the available device technologies. of the voltage–frequency–power design space and should be
GaN power devices span lateral and vertical conduction matched to the switching regime, thermal boundary conditions,
architectures, together with specialized structures designed and reliability requirements of the corresponding conversion
to address threshold-voltage control, electric-field management, stage [6, 9, 10] shown in Fig. 2.
thermal resistance, bidirectional power flow, and system SpecializedGaNstructuresfurtherbroadenthisdesignspace.
integration [6, 7]. This diversity is important because the Trench-gate GaN MOSFET concepts can improve electric-field
conversionstagesinFig.2donotimposeuniformrequirements. control and reduce specific on-resistance while supporting
Front-end power-factor-correction stages, isolated intermediate- high breakdown voltage, providing a potential route toward
bus converters, 48-V conversion stages, and processor-level compact, high-power-density conversion [11]. Bidirectional
regulators operate at different voltage classes, current levels, GaN HEMTs can reduce device count and conduction-path

Fig.3. Illustrativecomparisonofswitching-frequencyandpower-densityenvelopesforSi,SiC,andGaNdevices.
complexity in systems requiring bidirectional energy transfer, demonstrations, and data-center studies typically evaluate facil-
storage integration, AC switching, or advanced rack-level ity energy use, PUE, and cooling. A stage-resolved synthesis
power management [12]. However, device-level switching is therefore needed to connect GaN device architecture and
capability does not automatically translate into converter-level switching behavior to converter topology, operating domain,
performance. Metallization, package architecture, gate-loop packaging requirements, and facility-level consequences.
| design,     | commutation-loop |       | inductance, |            | thermal | interfaces,   | and       |                |          |               |           |                |     |                |          |
| ----------- | ---------------- | ----- | ----------- | ---------- | ------- | ------------- | --------- | -------------- | -------- | ------------- | --------- | -------------- | --- | -------------- | -------- |
|             |                  |       |             |            |         |               |           | Accordingly,   |          | this review   |           | examines       | how | GaN            | material |
| EMI control | strongly         |       | determine   | whether    |         | the intrinsic | speed     |                |          |               |           |                |     |                |          |
|             |                  |       |             |            |         |               |           | properties     | and      | architectural | diversity |                | can | be translated  | into     |
| of GaN      | produces         | lower | loss        | or instead |         | produces      | excessive |                |          |               |           |                |     |                |          |
|             |                  |       |             |            |         |               |           | stage-specific | benefits | across        | the       | AI data-center |     | power-delivery |          |
| overshoot,  | ringing,         | and   | electrical  | stress.    | In      | high-density  | power     |                |          |               |           |                |     |                |          |
chain.Theprincipalcontributionsarefourfold.First,thereview
| modules,           | reduced      | parasitic   |                 | inductance | can                | limit          | switching |                     |                      |                   |         |                |          |             |              |
| ------------------ | ------------ | ----------- | --------------- | ---------- | ------------------ | -------------- | --------- | ------------------- | -------------------- | ----------------- | ------- | -------------- | -------- | ----------- | ------------ |
|                    |              |             |                 |            |                    |                |           | develops            | a converter-oriented |                   |         | classification |          | of lateral, | vertical,    |
| overshoot          | and          | loss, while | improved        |            | thermal            | paths          | can lower |                     |                      |                   |         |                |          |             |              |
|                    |              |             |                 |            |                    |                |           | and specialized     |                      | GaN               | devices | based          | on       | voltage     | scalability, |
| junction           | temperature  |             | and support     | reliable   |                    | 24/7 operation | [13].     |                     |                      |                   |         |                |          |             |              |
|                    |              |             |                 |            |                    |                |           | switching           | behavior,            | conduction        |         | loss,          | thermal  | pathways,   | and          |
| These interactions |              | directly    |                 | affect     | the facility-level |                | loss and  |                     |                      |                   |         |                |          |             |              |
|                    |              |             |                 |            |                    |                |           | reliability         | limitations.         |                   | Second, | it maps        | these    | device      | classes      |
| cooling            | relationship | illustrated |                 | in Fig.    | 1.                 |                |           |                     |                      |                   |         |                |          |             |              |
|                    |              |             |                 |            |                    |                |           | onto representative |                      | front-end         |         | PFC,           | isolated | DC/DC,      | 48-V         |
| Manufacturability  |              |             | and scalability |            | are                | similarly      | important |                     |                      |                   |         |                |          |             |              |
|                    |              |             |                 |            |                    |                |           | intermediate-bus,   |                      | and point-of-load |         | conversion     |          | stages.     | Third, it    |
| for large-scale    |              | data-center | deployment.     |            | GaN                | devices        | can be    |                     |                      |                   |         |                |          |             |              |
evaluatesthepackage,gate-drive,EMI,thermal,manufacturing,
| fabricated        | on silicon,   |            | silicon           | carbide,     | or native     | GaN             | substrates,  |                   |               |               |              |                         |              |               |              |
| ----------------- | ------------- | ---------- | ----------------- | ------------ | ------------- | --------------- | ------------ | ----------------- | ------------- | ------------- | ------------ | ----------------------- | ------------ | ------------- | ------------ |
|                   |               |            |                   |              |               |                 |              | and qualification |               | constraints   |              | that determine          |              | whether       | device-      |
| with each         | platform      | providing  |                   | different    | trade-offs    |                 | among wafer  |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | level advantages  |               | are preserved |              | at the                  | converter    |               | and system   |
| cost, defect      | density,      |            | thermal           | performance, |               | voltage         | capability,  |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | levels. Fourth,   |               | it introduces |              | a quantitative          |              | framework     | that         |
| and manufacturing |               |            | maturity          | [7].         | The ability   |                 | to fabricate |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | connects          | cascaded      | conversion    |              | efficiency              |              | to electrical | loss,        |
| lateral GaN       | devices       |            | on large-diameter |              | silicon       | substrates      | can          |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | waste-heat        | generation,   |               | cooling      | demand,                 | and          | operational   | carbon       |
| improve           | manufacturing |            | scalability       | and          | reduce        | barriers        | relative     |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | impact.           | The objective |               | is not       | to present              | GaN          | as            | a universal  |
| to approaches     |               | that rely  | exclusively       |              | on bulk       | GaN             | substrates.  |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | replacement       | for           | silicon       | or silicon   | carbide,                |              | but to        | identify the |
| Nevertheless,     |               | total cost | of ownership      |              | is determined |                 | not only     |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | operating         | conditions    | under         | which        | device–topology–package |              |               |              |
| by transistor     | price,        | but        | also              | by converter |               | efficiency,     | package      |                   |               |               |              |                         |              |               |              |
|                   |               |            |                   |              |               |                 |              | co-optimization   |               | provides      | a defensible |                         | system-level |               | advantage.   |
| complexity,       | qualification |            | requirements,     |              | cooling       | infrastructure, |              |                   |               |               |              |                         |              |               |              |
reliability, and replacement frequency [7]. The material basis for the device-level comparisons used
Although GaN device physics, device reliability, converter throughout the review is summarized in Fig. 4. The remainder
implementation, and data-center energy efficiency have each of the paper progresses from material properties and device
receivedsubstantialattention,thesetopicsareoftentreatedsep- architecturestoconverter-stagedeployment,manufacturingand
arately. Device-oriented reviews generally emphasize material reliability constraints, quantitative facility-level implications,
properties, gate structures, trapping, and breakdown behavior, and future research priorities for GaN-enabled AI power
| whereas | converter | studies | focus | on  | individual |     | topologies | or infrastructure. |     |     |     |     |     |     |     |
| ------- | --------- | ------- | ----- | --- | ---------- | --- | ---------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |

Fig.4. Materialperformancecomparison:(A)Fundamentalrelationshipbetweenbreakdownfield(Ecrit)andbandgap(Eg);(B)Conceptualdrift-region
limitsshowingspecificon-resistance(Ron,sp)versusbreakdownvoltage(VBR);and(C)SummaryofkeymaterialpropertiesforSi,4H-SiC,andGaN(data
compiledfrom[14,15,16,17,18,19]).
II. CONVERTER-RELEVANTMATERIALBACKGROUND: resistance, while its high electron mobility and saturation
|     |     | GAN,SI,ANDSIC |     |     |     |     |     | velocity support |       | rapid carrier | transport |           | [22].     |     |          |
| --- | --- | ------------- | --- | --- | --- | --- | --- | ---------------- | ----- | ------------- | --------- | --------- | --------- | --- | -------- |
|     |     |               |     |     |     |     |     | The limits       | shown | in            | Fig. 4(b) | represent | idealized |     | unipolar |
The performance potential of a power semiconductor is drift-region behavior rather than the total on-resistance of a
| governed | by how | its intrinsic | material | properties |     | translate | into |           |         |        |            |      |          |               |     |
| -------- | ------ | ------------- | -------- | ---------- | --- | --------- | ---- | --------- | ------- | ------ | ---------- | ---- | -------- | ------------- | --- |
|          |        |               |          |            |     |           |      | practical | device. | Actual | resistance | also | includes | contributions |     |
voltage-blocking capability, conduction loss, switching behav- from the channel, access regions, contacts, substrate, current
| ior, and | thermal | management. | Compared |     | with | conventional |     |            |                |     |     |         |                |     |        |
| -------- | ------- | ----------- | -------- | --- | ---- | ------------ | --- | ---------- | -------------- | --- | --- | ------- | -------------- | --- | ------ |
|          |         |             |          |     |      |              |     | spreading, | metallization, |     | and | package | interconnects. |     | In GaN |
silicon(Si),galliumnitride(GaN)supportshigherelectricfields,
|     |     |     |     |     |     |     |     | HEMTs, | trapping | and | self-heating | can | further | increase | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ------------ | --- | ------- | -------- | --- |
faster carrier transport, and reduced theoretical drift-region effective on-resistance under dynamic switching conditions.
| resistance, | enabling | high-efficiency |     | and | high-power-density |     |     |               |     |             |     |          |       |        |           |
| ----------- | -------- | --------------- | --- | --- | ------------------ | --- | --- | ------------- | --- | ----------- | --- | -------- | ----- | ------ | --------- |
|             |          |                 |     |     |                    |     |     | Consequently, | the | theoretical |     | material | limit | should | be inter- |
conversion when these material advantages are preserved at preted as a comparison of intrinsic voltage-blocking potential
the device, package, and converter levels [20]. As illustrated rather than as a direct prediction of converter efficiency.
| in Fig.  | 4(a), the   | wide | bandgap  | and   | high critical | electric |     |              |     |                    |     |     |          |     |     |
| -------- | ----------- | ---- | -------- | ----- | ------------- | -------- | --- | ------------ | --- | ------------------ | --- | --- | -------- | --- | --- |
|          |             |      |          |       |               |          |     | B. Switching | and | Reverse-Conduction |     |     | Behavior |     |     |
| field of | GaN provide | the  | physical | basis | for compact   | voltage- |     |              |     |                    |     |     |          |     |     |
blocking regions [7]. Together with its high carrier-transport GaN’s converter-level advantage is strongly associated with
|             |       |            |      |                  |     |          |     | switching-related |     | device | metrics | rather | than | with breakdown |     |
| ----------- | ----- | ---------- | ---- | ---------------- | --- | -------- | --- | ----------------- | --- | ------ | ------- | ------ | ---- | -------------- | --- |
| capability, | these | properties | make | GaN particularly |     | relevant | to  |                   |     |        |         |        |      |                |     |
high-frequency power conversion in data-center and energy- field alone. High carrier velocity, compact device geometry,
system applications [20, 7]. and low charge storage can reduce gate-drive demand and
|              |            |     |                  |     |            |     |     | voltage–current |             | overlap | during   | switching | transitions.   |           | These    |
| ------------ | ---------- | --- | ---------------- | --- | ---------- | --- | --- | --------------- | ----------- | ------- | -------- | --------- | -------------- | --------- | -------- |
|              |            |     |                  |     |            |     |     | characteristics | can         | support | higher   | switching |                | frequency | and      |
| A. Breakdown | Capability |     | and Drift-Region |     | Resistance |     |     |                 |             |         |          |           |                |           |          |
|              |            |     |                  |     |            |     |     | smaller passive | components, |         | provided |           | that increased |           | magnetic |
As summarized in Fig. 4(c), GaN and 4H-SiC have substan- loss, output-capacitance loss, package parasitics, and electro-
tially wider bandgaps and higher critical electric fields than magnetic interference do not offset the semiconductor-level
| Si [20, | 21]. A higher | critical | field | allows | a power | device | to  | gain. |     |     |     |     |     |     |     |
| ------- | ------------- | -------- | ----- | ------ | ------- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
support a specified blocking voltage using a thinner and more Lateral GaN high-electron-mobility transistors use a
heavily doped drift region. This reduces the theoretical specific polarization-induced two-dimensional electron gas at the Al-
on-resistance associated with voltage blocking, as illustrated GaN/GaN heterointerface to obtain a high-mobility conduction
conceptually in Fig. 4(b). GaN’s critical electric field, which channel with low channel resistance [22, 23]. Unlike a conven-
exceeds approximately 3 MV/cm, therefore provides a strong tional Si MOSFET, a lateral GaN HEMT does not contain an
theoretical basis for compact devices with low drift-region intrinsic body diode with stored minority-carrier charge. It can

therefore avoid conventional body-diode reverse-recovery loss, important than maximum switching frequency [24]. SiC MOS-
althoughreverseconductionstillproduceslossandthecharging FETs and Schottky diodes are consequently widely used in
and discharging of output capacitance remain important during electric-vehicle traction inverters, charging systems, renewable-
commutation. These characteristics are especially valuable in energy converters, and grid-scale power electronics.
high-frequency PFC, resonant DC/DC, intermediate-bus, and Emerging vertical GaN devices exploit the high critical
point-of-load converters. GaN devices are also used in RF field of GaN while conducting through the semiconductor
systems, although RF operation is outside the principal power- thickness, providing a potential route toward higher blocking
conversion scope of this review. voltage, increased current capability, and improved voltage-
Commercial lateral GaN is particularly well established in area scaling [9]. Vertical GaN may therefore extend the useful
approximately 100–650 V high-frequency conversion, with range of GaN beyond the operating domains currently dom-
devices and converter demonstrations extending beyond this inated by lateral HEMTs. However, its practical deployment
range. Its compatibility with silicon substrates can support remains constrained by native-substrate cost, epitaxial defect
large-diameter wafer processing and scalable manufacturing, control, edge termination, processing maturity, packaging, and
although substrate choice, epitaxial buffer design, and defect high-voltage qualification. Specialized architectures, including
management influence dynamic performance, thermal behavior, trench-gate GaN MOSFETs and bidirectional HEMTs, further
and reliability. tailor electric-field control, normally-off operation, and current-
flow capability for specific converter requirements.
C. Thermal Behavior and Practical Power Density
Taken together, GaN and SiC both offer substantial ad-
Silicon carbide is particularly well suited to high-voltage, vantages over Si, but they occupy overlapping rather than
high-temperature, and high-power operating environments strictly separated design spaces [20]. GaN is strongest where
[24]. The thermal conductivity of 4H-SiC can approach high-frequency switching, compact passive components, and
400 W/(m·K), providing a strong material-level heat- high converter density are primary objectives, while SiC
spreading advantage over both Si and GaN. This contributes to is particularly competitive where high voltage, high power,
the use of SiC devices in converters that require high blocking thermalrobustness,andfaulttolerancedominate.Thepreferred
voltage, substantial current capability, elevated junction temper- technology must therefore be selected using converter-level
ature, and robust operation under severe electrical and thermal requirements, including voltage and current stress, switching
stress. mode, operating frequency, thermal boundary, reliability target,
Bulk GaN has a lower thermal conductivity than 4H-SiC, as and cost. These material-level trade-offs provide the basis for
indicated in Fig. 4(c). Therefore, GaN’s high achievable power thedevice-architecturediscussionthatfollows,inwhichlateral,
density does not imply that heat removal is inherently easier. vertical,andspecializedGaNstructuresareevaluatedaccording
Faster switching and smaller die or package dimensions may to how effectively they convert intrinsic material capability
reducetotallosswhilesimultaneouslyincreasinglocalheatflux. into practical power-electronics performance.
The realized junction temperature depends on the complete
thermal path, including the epitaxial structure, substrate, die at-
III. GANPOWER-DEVICEARCHITECTURESAND
tach, package, printed-circuit board, heat spreader, and cooling
CONVERTER-LEVELTRADE-OFFS
system.Powerdensitymustthereforebeevaluatedtogetherwith GaN power devices translate the intrinsic material properties
thermal resistance and allowable junction temperature rather discussed in Section II into practical voltage-blocking, conduc-
than inferred solely from semiconductor switching speed. tion,switching,andthermalcharacteristics.Theirimportanceto
powerelectronicsarisesfromthepossibilityofcombininghigh
D. Stage-Specific Positioning of GaN, SiC, and Si
conversion efficiency, elevated switching frequency, and high
The relative suitability of Si, SiC, and GaN cannot be volumetricpowerdensity[25].Theseattributesareincreasingly
defined by a single voltage threshold. Silicon remains highly relevantasAIworkloadsanddata-centerelectrificationincrease
competitive in cost-sensitive and mature converter platforms, rack power, tighten thermal constraints, and place greater
particularly where switching frequency and power density are emphasis on converter efficiency and compact power delivery
moderate. Lateral GaN is especially attractive in low-to-mid- [26, 27, 28, 1]. However, GaN’s converter-level performance
voltage stages where switching loss, passive-component size, is determined not by material capability alone, but by the
transient response, and volumetric density dominate the design device architecture used to control the channel, sustain electric
objective. Figure 4(b) therefore highlights a conceptual GaN field, conduct reverse current, extract heat, and interface with
advantageinmid-voltageoperation,butthisadvantagedepends the gate driver and package. Its high critical electric field
on topology, switching mode, package parasitics, cooling, and and carrier-transport capability provide the basis for low-loss,
operating frequency rather than on voltage alone. high-frequency operation, particularly in low-to-mid-voltage
SiC is commercially mature across multiple voltage classes, conversion [20].
including 650-V devices as well as 1.2-kV and higher-voltage A defining feature of the GaN platform is therefore its archi-
platforms. It is particularly advantageous when blocking- tectural diversity. Contemporary GaN power devices include:
voltage margin, thermal conductivity, surge capability, high- (i) lateral GaN/AlGaN HEMTs, which currently provide the
temperature operation, and high-power robustness are more most mature commercial route to high-frequency conversion;

Fig. 5. Overview of GaN power-device architectures and their converter-level positioning. (A) Lateral GaN/AlGaN HEMT structure and representative
normally-offimplementations,includingp-GaNgate,recessed-gate,andfluorine-implantapproaches,withpolarization-induced2DEGformation.(B)Vertical
GaNdeviceconcepts,includingp–ndiodesandtrench-MOSFETstructureswithcurrentflowthroughthebulkdriftregion.(C)Specializedarchitectures,
includingcascodeconfigurations,bidirectionalswitches,andGIT/p-GaNgateconcepts.(D)Conceptualdevice-classselectionmapillustratingvoltage–frequency
trade-offs,converter-levelstrengths,andarchitecturalpositioning.Themaprepresentstechnologicalcapabilityratherthanequalcommercialmaturityamongthe
deviceclasses.
(ii) vertical GaN devices, which use bulk current flow to threshold voltage. Their practical differences involve threshold-
improve voltage-area scaling at higher blocking voltages; voltage magnitude and stability, gate leakage, allowable gate-
and (iii) specialized architectures that address normally-off voltage range, process complexity, and sensitivity to charge
operation, bidirectional conduction, field management, driver trapping.
compatibility, and monolithic integration. Fig. 5 summarizes Lateral GaN devices are commercially established in high-
these device classes and their principal converter-level trade- frequency power conversion because of mature GaN-on-Si and
offs. GaN-on-SiCprocessing,availableenhancement-modeproducts,
and favorable switching-related figures of merit. Their low
A. Lateral GaN/AlGaN HEMTs and Normally-Off Implemen-
switchingchargeandabsenceofaconventionalminority-carrier
tations
body diode reduce commutation loss relative to many silicon
As illustrated in Fig. 5(A), lateral GaN/AlGaN HEMTs use implementations. However, reverse conduction still incurs a
polarization-induced charge at the AlGaN/GaN heterointerface voltage-dependent loss, and output-capacitance charging and
to form a high-mobility two-dimensional electron gas (2DEG) discharging remain important during hard switching. The
[29]. The 2DEG provides a low-resistance lateral conduction realized converter advantage therefore depends on dead-time
channel without intentional channel doping and supports rapid control, switching-node capacitance, package inductance, and
modulation of drain current during switching [29]. The source, the extent to which the topology provides soft switching.
gate, and drain are arranged on the same surface, while the As the required blocking voltage increases, the lateral
lateral access and drift regions determine the conduction path drift region must generally be extended, increasing die area
and contribute to the device voltage-blocking capability. and exposing a greater surface region to high electric field.
For practical power conversion, normally-off operation is Surfaceandbuffertrappingcanproducedynamicon-resistance,
required so that the device remains nonconducting at zero current collapse, and time-dependent changes in conduction
gate bias. Representative enhancement-mode implementations loss following high-voltage switching events [32]. Thus, lateral
shown in Fig. 5(A) include p-GaN gate structures, recessed- GaN is particularly attractive where switching-related loss and
gate geometries, and fluorine implantation beneath the gate passive-component volume dominate, but its operation must be
[30, 31, 32]. Each approach modifies the electrostatics beneath constrained by gate reliability, dynamic R , electric-field
DS(on)
thegatetodepletethe2DEGatzerobiasandproduceapositive management, and package-level parasitics.

B. Vertical GaN Devices posite normally-off behavior [26]. The low-voltage MOSFET
VerticalGaNdevicesroutecurrentperpendiculartothewafer controls the source potential of the depletion-mode GaN
|                 |        |         |               |       |                |          |         | device, | allowing        | the composite |              | switch | to be driven | using       | gate- |
| --------------- | ------ | ------- | ------------- | ----- | -------------- | -------- | ------- | ------- | --------------- | ------------- | ------------ | ------ | ------------ | ----------- | ----- |
| surface through |        | a bulk  | drift region, |       | as illustrated |          | in Fig. | 5(B)    |                 |               |              |        |              |             |       |
|                 |        |         |               |       |                |          |         | voltage | levels familiar |               | from silicon |        | power        | converters. | This  |
| [9, 33].        | Unlike | lateral | HEMTs,        | whose |                | blocking | voltage | is      |                 |               |              |        |              |             |       |
strongly influenced by lateral drift length and surface-field can simplify adoption in existing converter platforms, but
|             |     |          |            |     |     |            |        | the two-device | structure |     | introduces | additional |     | capacitances, |     |
| ----------- | --- | -------- | ---------- | --- | --- | ---------- | ------ | -------------- | --------- | --- | ---------- | ---------- | --- | ------------- | --- |
| management, | the | blocking | capability |     | of  | a vertical | device | is             |           |     |            |            |     |               |     |
governed primarily by drift-layer thickness, doping, junction internal interconnect parasitics, reverse-conduction behavior,
|             |      |             |     |          |      |          |          | and transient | interactions |     | that must | be  | considered | during | fast |
| ----------- | ---- | ----------- | --- | -------- | ---- | -------- | -------- | ------------- | ------------ | --- | --------- | --- | ---------- | ------ | ---- |
| design, and | edge | termination |     | [9, 34]. | This | geometry | provides |               |              |     |           |     |            |        |      |
switching.
| a potential | route | to blocking |     | voltages | exceeding |     | 1 kV | while |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | --- | -------- | --------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
maintaining competitive specific on-resistance and limiting the Bidirectional GaN switches are intended to control current
|          |            |     |          |          |     |     |     | and block | voltage | in both | directions, | making |     | them relevant | to  |
| -------- | ---------- | --- | -------- | -------- | --- | --- | --- | --------- | ------- | ------- | ----------- | ------ | --- | ------------- | --- |
| increase | in lateral | die | area [9, | 33, 34]. |     |     |     |           |         |         |             |        |     |               |     |
Representativeverticalstructuresincludep–ndiodes,current- AC switching, matrix converters, solid-state circuit breakers,
|          |          |             |              |     |     |          |        | energy-storage | interfaces, |     | and bidirectional |     | power | routing | [12]. |
| -------- | -------- | ----------- | ------------ | --- | --- | -------- | ------ | -------------- | ----------- | --- | ----------------- | --- | ----- | ------- | ----- |
| aperture | devices, | trench-gate | transistors, |     | and | vertical | MOSFET |                |             |     |                   |     |       |         |       |
Amonolithicbidirectionalstructurecanpotentiallyreplacetwo
| concepts. | The structures |     | depicted | in  | Fig. 5(B) | illustrate |     | how a |     |     |     |     |     |     |     |
| --------- | -------------- | --- | -------- | --- | --------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
bulk drift region and trench-based field control can combine anti-series unidirectional transistors, reducing device count and
|          |            |      |              |     |          |     |         | current-path | resistance. | However, |     | gate | control, | common-source |     |
| -------- | ---------- | ---- | ------------ | --- | -------- | --- | ------- | ------------ | ----------- | -------- | --- | ---- | -------- | ------------- | --- |
| vertical | conduction | with | high-voltage |     | blocking |     | [9, 35, | 34].         |             |          |     |      |          |               |     |
Vertical current flow can reduce dependence on long surface behavior, protection, and independent voltage blocking in both
drift regions, mitigate lateral current crowding, and distribute polarities increase the complexity of the device and converter
implementation.
| electric-field | stress | through | the | device | thickness |     | [9, 35]. |     |     |     |     |     |     |     |     |
| -------------- | ------ | ------- | --- | ------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
The vertical geometry can also provide a more direct Gate-injection transistors use hole injection from a p-type
|                   |             |           |           |       |          |              |     | gate region | to achieve     | normally-off |       | operation |            | and high | current |
| ----------------- | ----------- | --------- | --------- | ----- | -------- | ------------ | --- | ----------- | -------------- | ------------ | ----- | --------- | ---------- | -------- | ------- |
| thermal           | path toward | the       | substrate | and   | die      | attach,      | but | it does     |                |              |       |           |            |          |         |
|                   |             |           |           |       |          |              |     | capability  | [37]. Advanced |              | p-GaN | and       | gate-stack | concepts | sim-    |
| not automatically |             | guarantee |           | lower | junction | temperature. |     | The         |                |              |       |           |            |          |         |
realized thermal resistance depends on the conductivity and ilarly seek to improve threshold control, gate-current behavior,
andconductionperformance.Theirpracticalsuitabilitydepends
| thickness | of the | substrate, | active-region |     | placement, |     | backside |     |     |     |     |     |     |     |     |
| --------- | ------ | ---------- | ------------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
contact, die attach, package architecture, and external cooling onmaintainingastablethresholdvoltageandgatecharacteristic
|           |               |         |           |     |         |          |         | throughout | repetitive   | switching, |     | high | temperature, | and | long- |
| --------- | ------------- | ------- | --------- | --- | ------- | -------- | ------- | ---------- | ------------ | ---------- | --- | ---- | ------------ | --- | ----- |
| boundary. | Vertical      | current | alignment |     | may     | improve  | current |            |              |            |     |      |              |     |       |
|           |               |         |           |     |         |          |         | duration   | bias stress. |            |     |      |              |     |       |
| spreading | and heat-flow |         | geometry, |     | but the | complete | thermal |            |              |            |     |      |              |     |       |
stack still determines performance under sustained power Specialization also occurs through process and layout en-
|             |      |     |     |     |     |     |     | gineering. | Metallization |     | design, | surface | passivation, |     | buffer |
| ----------- | ---- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | ------- | ------- | ------------ | --- | ------ |
| density [9, | 35]. |     |     |     |     |     |     |            |               |     |         |         |              |     |        |
Vertical GaN remains less mature than commercial lateral engineering, field plates, edge termination, and trench ge-
|               |           |     |             |        |                     |        |     | ometries | can shape | the | electric    | field,  | suppress | trapping, | and   |
| ------------- | --------- | --- | ----------- | ------ | ------------------- | ------ | --- | -------- | --------- | --- | ----------- | ------- | -------- | --------- | ----- |
| GaN. Its      | adoption  | is  | constrained |        | by native-substrate |        |     | cost,    |           |     |             |         |          |           |       |
|               |           |     |             |        |                     |        |     | improve  | breakdown | and | reliability | margins |          | [38, 22]. | These |
| limited wafer | diameter, |     | epitaxial   | defect | density,            | p-type |     | doping   |           |     |             |         |          |           |       |
and activation, trench-interface quality, edge termination, and features can improve one performance dimension while adding
|         |                 |     |         |      |        |     |            | capacitance, | process | steps, | or  | field concentration |     | elsewhere. |     |
| ------- | --------------- | --- | ------- | ---- | ------ | --- | ---------- | ------------ | ------- | ------ | --- | ------------------- | --- | ---------- | --- |
| process | reproducibility |     | [9, 35, | 36]. | Native | GaN | substrates |              |         |        |     |                     |     |            |     |
can reduce dislocation density and support high-field vertical Device optimization must therefore account for the intended
structures, but their availability and cost currently limit high- switching topology and mission profile rather than treating
|     |     |     |     |     |     |     |     | breakdown | voltage, | static | R   | , or | threshold | voltage | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | --- | ---- | --------- | ------- | --- |
volume deployment [9, 35]. Vertical GaN should therefore be DS(on)
regarded as an emerging high-voltage platform rather than a isolated objectives [38].
| direct near-term  |     | replacement   |     | for established |     | lateral | GaN           | or              |     |           |     |            |          |     |     |
| ----------------- | --- | ------------- | --- | --------------- | --- | ------- | ------------- | --------------- | --- | --------- | --- | ---------- | -------- | --- | --- |
|                   |     |               |     |                 |     |         |               | D. Architecture |     | Selection | and | Technology | Maturity |     |     |
| SiC technologies. |     | Its strongest |     | prospective     |     | role    | is in voltage |                 |     |           |     |            |          |     |     |
and power ranges where lateral drift-region scaling becomes The conceptual voltage–frequency positioning of the main
|             |     |       |            |       |        |     |         | GaN device | classes | is  | summarized |     | in Fig. | 5(D). | Lateral |
| ----------- | --- | ----- | ---------- | ----- | ------ | --- | ------- | ---------- | ------- | --- | ---------- | --- | ------- | ----- | ------- |
| inefficient | and | where | sufficient | value | exists | to  | justify | the        |         |     |            |     |         |       |         |
additional substrate and qualification complexity [9, 36]. GaN HEMTs are strongest in high-frequency, low-to-mid-
voltageconversion,whereswitchingcharge,outputcapacitance,
C. Specialized, Cascode, and Bidirectional Architectures and compact passive components strongly influence converter
Specialized GaN structures address converter requirements performance[26].VerticalGaNbecomesincreasinglyattractive
that cannot be represented solely by breakdown voltage or as voltage, current, and die-area scaling place greater emphasis
static on-resistance. These requirements include normally-off on drift-region resistance, bulk field management, and high-
behavior, conventional gate-drive compatibility, bidirectional power thermal pathways [26]. Cascode, bidirectional, and
currentblocking,stablethresholdvoltage,electric-fieldshaping, other specialized devices occupy system-driven positions in
and functional integration [26]. Representative architectures which normally-off behavior, conventional drive compatibility,
showninFig.5(C)includecascodeconfigurations,bidirectional bidirectionalpowerflow,integration,orprotectionfunctionality
| GaN switches, | and | gate-injection |     | transistor |     | or advanced |     | p-GaN is decisive | [26]. |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | ---------- | --- | ----------- | --- | ----------------- | ----- | --- | --- | --- | --- | --- | --- |
gate concepts [22, 37]. From a converter-loss perspective, lateral GaN is advanta-
A cascode combines a normally-on, high-voltage GaN geous when transition loss, gate charge, commutation behavior,
HEMT with a low-voltage silicon MOSFET to produce com- and device capacitances represent a significant fraction of total

loss. Vertical GaN has the potential to become advantageous A. Stage Requirements and Device-Class Selection
when high-voltage drift-region resistance, current spreading, AdatacenterconvertsincomingACpowerintooneormore
| and die-area | scaling become     | limiting | factors | [18].  | Specialized |       |           |       |                 |            |         |              |            |            |
| ------------ | ------------------ | -------- | ------- | ------ | ----------- | ----- | --------- | ----- | --------------- | ---------- | ------- | ------------ | ---------- | ---------- |
|              |                    |          |         |        |             |       | regulated | DC    | buses and       | ultimately |         | into tightly | controlled | point-     |
| structures   | do not necessarily | provide  | the     | lowest | intrinsic   | loss; |           |       |                 |            |         |              |            |            |
|              |                    |          |         |        |             |       | of-load   | rails | for processors, |            | memory, | storage,     | and        | networking |
instead, they may offer system-level value by reducing device hardware [50, 23]. The conversion stages differ substantially
| count, simplifying | the driver, | enabling | bidirectional |     | operation, |     |             |          |     |       |             |           |     |            |
| ------------------ | ----------- | -------- | ------------- | --- | ---------- | --- | ----------- | -------- | --- | ----- | ----------- | --------- | --- | ---------- |
|                    |             |          |               |     |            |     | in voltage, | current, |     | power | throughput, | switching |     | frequency, |
improving normally-off control, or integrating functions that isolation requirement, conversion ratio, transient response, and
| would otherwise | require | discrete | components | [26]. |     |     |           |         |            |     |               |     |        |           |
| --------------- | ------- | -------- | ---------- | ----- | --- | --- | --------- | ------- | ---------- | --- | ------------- | --- | ------ | --------- |
|                 |         |          |            |       |     |     | allowable | thermal | impedance. |     | Consequently, |     | device | selection |
These classes also differ substantially in readiness. cannot be based on a single semiconductor figure of merit.
Enhancement-mode lateral GaN HEMTs are commercially Figure 6 provides an at-a-glance mapping of representative
matureandalreadyusedinPFC,isolatedDC/DC,intermediate-
|     |     |     |     |     |     |     | stages | and | operating | regimes, | while | Table | I   | summarizes |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | -------- | ----- | ----- | --- | ---------- |
bus, and compact power-supply applications. Cascode GaN is the corresponding voltage domains, power scales, switching
| also commercially | available, | although | its | hybrid | structure | pro- |          |          |               |     |     |                |     |          |
| ----------------- | ---------- | -------- | --- | ------ | --------- | ---- | -------- | -------- | ------------- | --- | --- | -------------- | --- | -------- |
|                   |            |          |     |        |           |      | regimes, | reported | efficiencies, |     | and | implementation |     | maturity |
ducesdifferentswitchingandreverse-conductionbehaviorfrom
|     |     |     |     |     |     |     | [50, 23]. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
a single-chip enhancement-mode HEMT. Monolithic bidirec- For a representative stage, the total converter loss may be
| tional devices,   | advanced | power integrated |                            | circuits, | and     | vertical |           |              |     |     |     |     |     |          |
| ----------------- | -------- | ---------------- | -------------------------- | --------- | ------- | -------- | --------- | ------------ | --- | --- | --- | --- | --- | -------- |
|                   |          |                  |                            |           |         |          | expressed | conceptually |     | as  |     |     |     |          |
| GaN transistors   | occupy   | emerging         | or early-commercialization |           |         |          |           |              |     |     |     |     |     |          |
| stages, depending | on the   | specific         | structure                  | and       | voltage | class.   |           |              |     |     |     |     |     |          |
|                   |          |                  |                            |           |         |          |           | P            | =P  | +P  | +P  |     | +P  | +P , (1) |
For continuously operated AI data centers, device selection loss,stage semi mag cap int aux
| must therefore | balance efficiency, |     | switching | frequency, |     | voltage |       |        |     |               |     |       |       |              |
| -------------- | ------------------- | --- | --------- | ---------- | --- | ------- | ----- | ------ | --- | ------------- | --- | ----- | ----- | ------------ |
|                |                     |     |           |            |     |         | where | P semi | is  | semiconductor |     | loss, | P mag | is magnetic- |
capability,packageparasitics,thermalresistance,faultbehavior,
|     |     |     |     |     |     |     | component |     | loss, P | is capacitor |     | and | charge-transfer | loss, |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ------------ | --- | --- | --------------- | ----- |
cap
manufacturability, and long-term stability [5]. A heterogeneous P is package, connector, busbar, and PCB interconnect loss,
int
| device landscape | is the | most credible |     | deployment | pathway: |     |       |          |             |     |          |          |     |                |
| ---------------- | ------ | ------------- | --- | ---------- | -------- | --- | ----- | -------- | ----------- | --- | -------- | -------- | --- | -------------- |
|                  |        |               |     |            |          |     | and P | includes | gate-drive, |     | control, | sensing, |     | and auxiliary- |
aux
commercially mature lateral GaN for prevalent high-frequency supply consumption. The semiconductor contribution can be
| 400–650-V       | stages, specialized | or        | hybrid | devices      | where | control |         |           |     |     |     |     |     |     |
| --------------- | ------------------- | --------- | ------ | ------------ | ----- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
|                 |                     |           |        |              |       |         | further | separated | as  |     |     |     |     |     |
| and integration | requirements        | dominate, |        | and vertical |       | GaN as  |         |           |     |     |     |     |     |     |
a longer-term option for higher-voltage and higher-power P =P +P +P +P +P , (2)
|            |                              |     |               |     |          |     |       | semi | cond       |     | tr Coss |     | gate               | rev |
| ---------- | ---------------------------- | --- | ------------- | --- | -------- | --- | ----- | ---- | ---------- | --- | ------- | --- | ------------------ | --- |
| conversion | after manufacturing          | and | qualification |     | barriers | are |       |      |            |     |         |     |                    |     |
|            |                              |     |               |     |          |     | where | P    | represents |     | channel | and | reverse-conduction |     |
| resolved   | [5]. This architecture-based |     | framework     |     | provides | the |       | cond |            |     |         |     |                    |     |
basis for the stage-specific data-center power-chain mapping loss, P tr represents voltage-current overlap during switching
developed in the following section. transitions, P represents output-capacitance charging and
Coss
|     |     |     |     |     |     |     | discharginglossnotrecoveredbythetopology,P |     |     |     |     |     |     | represents |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- |
gate
IV. SYSTEM-LEVELMAPPINGOFGANDEVICESTO gate-driveloss,andP rev representslossassociatedwithreverse
|     |     |     |     |     |     |     | conduction | and | commutation. |     | The | relative | importance | of these |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | --- | --- | -------- | ---------- | -------- |
DATA-CENTERPOWERCONVERSION
|     |     |     |     |     |     |     | terms | changes | with | topology | and | operating | point. | Therefore, |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ---- | -------- | --- | --------- | ------ | ---------- |
The device-level advantages of GaN become most con- increasing switching frequency does not automatically improve
sequential when evaluated across the complete data-center efficiency: reductions in passive-component volume can be
power-delivery chain, in which multiple conversion stages offset by increased semiconductor switching loss, magnetic
are cascaded across distinct voltage domains and their losses core and winding loss, common-mode current, EMI-filter
combine to determine the end-to-end efficiency [39]. GaN’s requirements, and local heat flux.
wide bandgap and high critical electric field reduce the drift- Lateral GaN/AlGaN HEMTs are best aligned with low-to-
region penalty associated with voltage blocking, while its high mid-voltage stages in which switching charge, transition loss,
electron transport capability supports rapid switching with and commutation behavior strongly influence total loss. Their
reduced charge-related loss [6]. However, favorable material polarization-induced two-dimensional electron gas supports
properties or device figures of merit do not independently high mobility and low channel resistance while enabling rapid
guarantee converter-level improvement. System benefit is switching [7, 51]. These characteristics make lateral devices
realized only when the GaN architecture, voltage rating, attractive for PFC, isolated DC/DC, intermediate-bus, and
package, gate drive, commutation loop, switching strategy, near-load conversion operating from tens of kilohertz into
and thermal path are matched to the operating requirements the megahertz regime [50, 23, 52, 53]. Within this class,
of a specific conversion stage. These requirements must also the choice among enhancement-mode, depletion-mode, and
be satisfied under the continuous loading, fast transients, and cascode implementations affects fail-safe behavior, gate-drive
high availability expected in 24/7 data-center operation [13]. compatibility, reverse conduction, parasitic interaction, and
Figure 6 maps representative GaN device classes onto the data- response under abnormal conditions [7, 54].
center power chain, while Table I summarizes representative Vertical GaN devices become increasingly relevant when
operating domains, reported performance, dominant design breakdown-voltagescaling,currentdensity,andconductionloss
constraints, and technology maturity. make lateral drift-region extension inefficient [9, 54]. Because

TABLEI
REPRESENTATIVEOPERATINGDOMAINSANDDEMONSTRATEDPERFORMANCEMETRICSACROSSTHEDATA-CENTERPOWERCHAIN,WITHIMPLICATIONS
FORGANDEVICE-CLASSSELECTION.VALUESAREREPRESENTATIVEEXAMPLESFROMRECENTREFERENCEDESIGNSANDSTANDARDS(DATACOMPILED
FROM[40,41,42,43,44,45,46,47,48,49]).
Power-chainstage Voltagedomain Powerscale Switchingregime Representative performance Dominantconverter-level GaNimplication
|     | andstatus |     |     | constraints |     |     |     |     |
| --- | --------- | --- | --- | ----------- | --- | --- | --- | --- |
Rack distribution 46–52VDCdistribu- Rack-andshelf- N/A; passive distri- OCP ORV3 specifies a 46.0– Busbarandconnectorresis- The 48-V bus reduces
I2R
(ORV348-Vbus) tion levelcurrentdis- bution 52.0 VDC IT-gear interface tance,currentsharing,pro- distribution loss
tribution rated at 100 A continuous. tection coordination, cop- relativetolower-voltage
|     | Ecosystem                  | documentation | de-        | per loss, | and conversion | buses                 | and moves  | high-  |
| --- | -------------------------- | ------------- | ---------- | --------- | -------------- | --------------------- | ---------- | ------ |
|     | scribes distribution       |               | capability | placement |                | ratio                 | conversion | closer |
|     | approaching                | ∼1000         | A at the   |           |                | totheload,creatingde- |            |        |
|     | output-connector           | level.        | Status:    |           |                | mandforcompact48-V-   |            |        |
|     | deployedstandardandecosys- |               |            |           |                | to-PoLconverters.     |            |        |
temarchitecture.
AC/DCfrontendand 90–264 VAC → ap- 3–3.2 kW mod- Approximately 65 A3-kWbridgelesstotem-pole Hard commutation, Coss LateralGaNisstrongly
PFC proximately400VDC uleclass kHz to 500 kHz PFC reference design reports energy,reverseconduction, positionedbecausefast
| in representative | 99% peak                        | efficiency  | with a  | common-mode              | EMI,           | cur- switching          | and             | the ab-   |
| ----------------- | ------------------------------- | ----------- | ------- | ------------------------ | -------------- | ----------------------- | --------------- | --------- |
| designs           | listedmaximumswitchingfre-      |             |         | rentsensing,gate-loopin- |                | sence                   | of conventional |           |
|                   | quency of                       | 65 kHz. A   | 3.2-kW  | ductance,                | and line-cycle | body-diode              | reverse         | re-       |
|                   | interleavedcritical-conduction- |             |         | thermalvariation         |                | covery                  | support         | high-     |
|                   | mode GaN                        | totem-pole  | design  |                          |                | efficiencytotem-poleop- |                 |           |
|                   | reports500-kHzoperationand      |             |         |                          |                | eration.                | Package         | para-     |
|                   | 99.3% peak                      | efficiency. | Status: |                          |                | sitics,                 | EMI,            | and gate- |
|                   | reference designs               | and         | demon-  |                          |                | voltage                 | margin          | remain    |
|                   | stratedprototypes.              |             |         |                          |                | decisive.               |                 |           |
IsolatedDC/DCcon- 400VDC→50VDC Up to 5.5 kW Resonant operation An input-series-output-parallel Circulating current, trans- High-frequency lateral
versionafterPFC (48-V-classbus) demonstrated near1MHz LLCconverterhasbeendemon- former and resonant-tank GaN supports compact
|     | stratedatupto5.5kWbetween     |           |        | loss, dead-time            | control, | magneticsandmodular     |     |          |
| --- | ----------------------------- | --------- | ------ | -------------------------- | -------- | ----------------------- | --- | -------- |
|     | a 400-VDC                     | input and | a 50-V | soft-switchingrange,isola- |          | isolation,              | but | the sys- |
|     | bus,witharesonantfrequency    |           |        | tioncapacitance,package    |          | tembenefitdependson     |     |          |
|     | near1MHz,98.5%peakeffi-       |           |        | parasitics,andheatextrac-  |          | maintainingsoftswitch-  |     |          |
|     | ciency,andapproximately97.5–  |           |        | tion                       |          | ingandcontrollingmag-   |     |          |
|     | 98%full-loadefficiencydepend- |           |        |                            |          | netic,capacitive,andin- |     |          |
|     | ingontheimplementation.Sta-   |           |        |                            |          | terconnectlosses.       |     |          |
tus:laboratoryprototype.
48-VVRMfirststage 48V→intermediate Approximately Approximately 1 AnunregulatedLLC-DCXwith Transformer integration, Lateral GaN enables
(fixed-ratioDCX) bususingfixedratios 900 W MHzandabove integratedmagneticshasdemon- winding and termination MHz-class switching
suchas4:1or8:1 continuous strated4:1and8:1conversion loss, current sharing, and magnetic
|     | ratiosat900Wcontinuousout-     |        |         | resonant-tank | tolerance,  | integration,         | supporting       |           |
| --- | ------------------------------ | ------ | ------- | ------------- | ----------- | -------------------- | ---------------- | --------- |
|     | put,withmaximumefficiencies    |        |         | board-level   | thermal     | conversionontheboard |                  |           |
|     | of 98.4% and                   | 98.0%, | respec- | spreading,    | and package | or                   | near accelerator |           |
|     | tively.Status:demonstratedcon- |        |         | footprint     |             | packages             |                  | where     |
|     | verterprototype.               |        |         |               |             | footprint            | and              | transient |
performancearecritical.
48 V → processor- 48 V → approxi- 300 A demon- Switched-capacitor The LEGO-PoL architecture Extreme conversion ratio, Specialized and hybrid
core PoL regulation mately1.5Vatvery strated stagenear100kHz combinesaswitched-capacitor conductionloss,capacitor architecturesdividethe
(hybrid or highcurrent andmultiphasebuck stage operating near 100 kHz charge-transferloss,multi- conversion ratio across
multiphase) stagenear1MHz with a multiphase buck stage phasecurrentsharing,fast stages. GaN is most
|     | near 1 MHz.                 | A representa-  |         | load transients, | intercon- | valuable               | where | MHz     |
| --- | --------------------------- | -------------- | ------- | ---------------- | --------- | ---------------------- | ----- | ------- |
|     | tiveimplementationusesthree |                |         | nect resistance, | and local | switching,             | low   | charge, |
|     | stacked 16-V,               | 100-A          | submod- | heatflux         |           | compactintegration,and |       |         |
|     | ules to provide             | 48-V-to-1.5-V, |         |                  |           | rapidtransientresponse |       |         |
|     | 300-A conversion.           | Status:        | re-     |                  |           | outweightheassociated  |       |         |
|     | searchprototype.            |                |         |                  |           | gate-drive             | and   | layout  |
complexity.
EmergingHVDCdis- ±400 V or 800-V- Facility- and Topologydependent; AIpower-architectureroadmaps DC fault interruption, in- Higher-voltagedistribu-
tributionforAIracks classDCdistribution rack-level includesHVDCbus include ±400-V and 800-V- sulationcoordination,pro- tion may increase the
→localconversion architectural conversion,isolation, class DC buses. Modular iso- tection selectivity, isola- long-term relevance of
trend intermediate-bus latedstagescanbeextendedto tion,high-voltagepackag- vertical GaN, but near-
| conversion,andPoL | thesebusesthroughadditional   |        |          | ing,qualification,andcon- |     | term                    | adoption          | depends |
| ----------------- | ----------------------------- | ------ | -------- | ------------------------- | --- | ----------------------- | ----------------- | ------- |
| regulation        | series-connectedinputmodules. |        |          | vertermodularity          |     | ondevicematurity,edge   |                   |         |
|                   | Status: emerging              | or     | prospec- |                           |     | termination,packageiso- |                   |         |
|                   | tive architecture             | rather | than     |                           |     | lation,                 | fault robustness, |         |
|                   | widespreaddeployment.         |        |          |                           |     | andsystem-levelqualifi- |                   |         |
cation.
current flows through the semiconductor thickness, the voltage- higher-voltage DC distribution architectures develop, vertical
blocking region can be scaled predominantly through epitaxial GaN may become relevant to high-voltage bus conversion and
thickness rather than lateral die dimension, offering a potential protection. However, this remains a prospective application
route to higher blocking voltage with reduced area penalty [9]. subject to high-voltage edge termination, defect control, native-
Verticalcurrentflowmayalsoprovideamoredirectpathtoward substratecost,packageinsulation,surgecapability,andmission-
the substrate, although the realized thermal advantage depends profile qualification [9, 54].
on the substrate, die attach, package, and cooling boundary. As Specialized GaN devices address system constraints that

Fig.6. MappingofGaNdeviceclassesontoarepresentativedata-centerpower-deliverychainusingstage-leveloperatingdomainsandreportedperformance
metrics.Eachblockidentifiesthevoltagedomain,powerscale,switchingregime,andarepresentativeefficiencyfromthefacilityACinputtopoint-of-load
regulation.ThelowerbandidentifiesstagesinwhichlateralGaNisfavoredforhigh-frequency,low-lossconversionandstagesinwhichspecializedorhybrid
architecturesaddressextremeconversionratiosandfasttransientrequirementsnearCPUsandGPUs.Theinsetsummarizesthefacilitycontext,includingPUE,
coolingdemand,andemerginghigh-voltageDCdistributionthatmayincreasefuturehigh-voltagedevicerequirements.
cannot be resolved through voltage rating or on-resistance gate-loop ringing, and common-mode EMI can become domi-
alone. Trench structures and field-management features can nant as the switching edges are accelerated. The representative
reduce electric-field crowding in high-voltage devices [54]. PFC systems in Table I therefore illustrate two different design
Bidirectional GaN devices can provide controlled current flow directions: moderate-frequency operation optimized for high
in both directions and may reduce the number of series efficiency and lower EMI burden, and substantially higher-
devices required in AC switching, storage interfaces, and frequency operation intended to increase power density and
bidirectional bus converters [52]. Advanced gate structures reduce passive-component size. In both cases, the useful GaN
target positive and stable threshold voltage, low leakage, and operating point is determined by a converter-level optimum
improved gate reliability during sustained operation [7, 54]. rather than by the maximum switching speed of the transistor.
Such architectures are most valuable when they resolve a
C. Isolated High-Voltage-to-48-V Conversion
specific converter bottleneck, including bidirectional operation,
extreme conversion ratio, normally-off safety, switching-node The isolated DC/DC stage converts the regulated high-
integration, or fast transient response [52, 53, 54]. voltage bus into a 48-V-class distribution rail and must
simultaneouslysatisfyefficiency,galvanicisolation,transformer
B. Front-EndAC/DCConversionandPower-FactorCorrection
utilization, thermal density, and hold-up or ride-through re-
The front-end AC/DC stage processes essentially the full quirements. Resonant topologies such as LLC converters are
electrical power delivered to the downstream rack or power attractivebecausezero-voltageswitchingcanreducetheturn-on
shelf. Consequently, even a small reduction in its loss can loss associated with transistor output capacitance. GaN enables
produce a meaningful absolute decrease in converter heat operation at hundreds of kilohertz or into the megahertz range,
generation. Totem-pole and bridgeless PFC topologies are allowing reductions in transformer and resonant-component
particularly relevant because they reduce the number of volume.
semiconductordropsintheprimarycurrentpath.However,their Atthesefrequencies,thesemiconductormaynolongerbethe
high-frequencyswitchinglegsimposedemandingcommutation onlyoreventhedominantsourceofloss.Transformercoreloss,
conditions, particularly near portions of the AC line cycle proximity and skin effects in windings, termination resistance,
where current is low or changes direction. circulatingresonantcurrent,isolationcapacitance,synchronous-
Lateral GaN is well suited to these stages because it avoids rectifiertiming,andPCBinterconnectlossbecomeincreasingly
the conventional body-diode reverse-recovery behavior of important. The 5.5-kW example in Table I demonstrates the
silicon superjunction MOSFETs and can reduce transition loss feasibility of megahertz-class isolated conversion, but it also
through low switching charge. The resulting benefit is not illustrates why high switching frequency must be accompanied
unconditional. Output-capacitance energy, reverse-conduction by integrated magnetics, low-inductance packaging, controlled
voltage drop during dead time, common-source inductance, resonant operation, and an effective thermal path. The value

of GaN in this stage is therefore its ability to expand the as a driver of heat generation and facility overhead [4, 55].
feasibledesignspaceforsoft-switched,high-densityconversion Higher conversion efficiency reduces the electrical power
rather than to eliminate the underlying magnetic and thermal dissipatedinsemiconductordevices,magnetics,capacitors,and
constraints. interconnects. A portion of this reduction can also decrease the
cooling power required to maintain acceptable component and
D. 48-V Intermediate-Bus and Point-of-Load Conversion
air temperatures. The magnitude of the facility-level benefit
The final stages of the data-center power chain must convert
depends on the stage power throughput, load profile, cooling-
a 48-V distribution bus into processor rails that can be
systemcoefficientofperformance,climate,airflowarchitecture,
near or below 1 V while supplying currents of hundreds
and interaction with other facility loads.
of amperes. This extreme conversion ratio cannot generally
GaN can reduce switching and conduction loss when it is
be addressed efficiently by increasing switching frequency
deployedwithinanappropriatevoltage,frequency,andtopology
in a conventional single-stage buck converter. Instead, fixed-
domain [51, 56]. In lateral GaN converters, low switching
ratio DC transformers, switched-capacitor stages, multiphase
chargeandrapidtransitionscanimprovestageefficiencyanden-
buck converters, and hybrid architectures divide the voltage
able smaller passive components. These benefits are preserved
transformation and regulation functions across multiple sub-
only when the package, gate driver, layout, magnetic design,
stages.
and control strategy prevent parasitic loss and excessive EMI.
GaN can improve these converters through low switching
Under these conditions, lower semiconductor and converter
charge,lowpackageinductance,high-frequencycapability,and
loss can reduce local component temperature and thermal-
the potential for close integration with magnetic and capacitive
management demand [57], particularly in front-end PFC and
components. However, near-load conversion is frequently
isolated conversion stages that process large portions of the
dominated by conduction and interconnect loss because the
rack power.
output current is extremely high. Package resistance, PCB
The efficiency of a cascaded power chain is multiplicative.
copper, vias, connectors, inductors, current-sharing imbalance,
Improving any individual stage increases the end-to-end chain
and the physical distance between the regulator and accelerator
efficiency, but the physical propagation of the benefit depends
package can therefore limit the total benefit. The DCX and
on the stage location. An improvement in a downstream stage
LEGO-PoL examples in Table I show how fixed-ratio and
reduces the power demanded from every upstream stage for a
hybrid approaches can reduce the burden placed on the final
fixed delivered load, whereas an improvement in an upstream
regulating stage. In these architectures, GaN is most valuable
stage primarily reduces the input power and heat generated
when it enables a reduction in conversion-stage count, passive
locally at that stage. Stages that process the full rack power
volume, or transient-response penalty without introducing
generally provide greater absolute leverage than converters
excessive charge-transfer, gate-drive, or thermal loss.
serving only a small load branch. Thus, the benefit should be
E. Emerging High-Voltage DC Distribution evaluated from the complete chain rather than inferred from
Higher-voltage DC distribution is being considered as a peak device or single-stage efficiency alone [4].
means to reduce current and conductor loss as rack power The cooling consequence is similarly site dependent. A
increases.Architecturesbasedon±400Vor800-V-classbuses reduction in converter heat does not produce a universal or
can reduce distribution current for a given power level but fixed reduction in PUE because PUE includes cooling, power
transfer greater responsibility to insulation coordination, DC distribution, lighting, controls, and other facility overheads.
fault interruption, isolation, protection selectivity, and local GaN should therefore be positioned as an enabling technology
high-ratio conversion. These systems should be distinguished that can reduce conversion loss and local thermal density,
from currently deployed 48-V rack architectures because supporting improved facility efficiency under appropriate
their protection and qualification ecosystems remain under operating conditions [57], rather than as a device substitution
development. that guarantees a predetermined reduction in PUE or carbon
Lateral GaN may remain applicable in modular or series- emissions. The quantitative relationship among cascaded effi-
connected converter cells, while vertical GaN could eventu- ciency, electrical loss, cooling demand, and carbon intensity is
ally provide a more direct device pathway for high-voltage developed separately in the facility-level analysis.
conversion. Nevertheless, the adoption of vertical GaN in
this domain is not determined by breakdown voltage alone. G. Practical Adoption Constraints in 24/7 Data-Center Oper-
High-voltage package insulation, edge termination, surge ation
robustness, short-circuit behavior, thermal extraction, defect
Despite its favorable device characteristics, GaN deploy-
density, manufacturing yield, and qualification maturity must
ment in mission-critical infrastructure remains constrained by
all be addressed before device-level capability can translate
gate-drive compatibility, dv/dt management, EMI, package
into mission-critical deployment.
parasitics, protection behavior, and long-term qualification
F. Efficiency, Waste Heat, Cooling Load, and PUE
under continuous operation [38]. These factors should be
Within the carbon-neutral data-center framework, converter evaluated using application-relevant electrical and thermal
efficiency is relevant not only as an electrical metric but also mission profiles rather than only static device ratings.

Gate-drive margin is a central concern. Enhancement-mode summarizes representative quantitative anchors related to sub-
GaN provides normally-off behavior at zero gate bias, but its strate scalability, packaging, qualification, yield, and embodied
| relatively | narrow     | allowable    | gate-voltage |               | range     | and            | sensitivity | impact.      |           |     |                   |     |     |             |     |
| ---------- | ---------- | ------------ | ------------ | ------------- | --------- | -------------- | ----------- | ------------ | --------- | --- | ----------------- | --- | --- | ----------- | --- |
| to loop    | inductance | require      | careful      | selection     |           | of the driver, | turn-       |              |           |     |                   |     |     |             |     |
| on and     | turn-off   | impedances,  |              | negative-bias | strategy, |                | and local   |              |           |     |                   |     |     |             |     |
|            |            |              |              |               |           |                |             | A. Substrate | Platforms |     | and Manufacturing |     |     | Scalability |     |
| decoupling | [58,       | 59]. Cascode |              | GaN can       | improve   | compatibility  |             |              |           |     |                   |     |     |             |     |
withconventionalgate-drivelevels,butthedynamicinteraction
|            |                 |          |           |        |           |                |           | Commercial   |            | GaN technologies |             | use     | three      | principal | substrate   |
| ---------- | --------------- | -------- | --------- | ------ | --------- | -------------- | --------- | ------------ | ---------- | ---------------- | ----------- | ------- | ---------- | --------- | ----------- |
| between    | the low-voltage |          | silicon   | MOSFET | and       | depletion-mode |           |              |            |                  |             |         |            |           |             |
|            |                 |          |           |        |           |                |           | pathways:    | GaN-on-Si, |                  | GaN-on-SiC, |         | and native | GaN       | [97, 98].   |
| GaN device | must            | be       | validated | during | switching | transitions,   |           |              |            |                  |             |         |            |           |             |
|            |                 |          |           |        |           |                |           | Each pathway |            | produces         | a different | balance |            | among     | wafer cost, |
| reverse    | conduction,     | startup, | and       | fault  | events.   | High           | dv/dt can |              |            |                  |             |         |            |           |             |
defectdensity,thermalperformance,voltagescalability,process
| produce       | Miller-induced |                   | false | turn-on,  | gate | ringing, | common-   |                |     |                   |     |         |     |     |     |
| ------------- | -------------- | ----------------- | ----- | --------- | ---- | -------- | --------- | -------------- | --- | ----------------- | --- | ------- | --- | --- | --- |
|               |                |                   |       |           |      |          |           | compatibility, |     | and manufacturing |     | volume. |     |     |     |
| mode current, |                | and drain-voltage |       | overshoot |      | when     | gate-loop |                |     |                   |     |         |     |     |     |
GaN-on-Sicurrentlyofferstheclearestpathwaytowardhigh-
| and commutation-loop |             |                 | inductances |                    | are not    | tightly      | controlled. |                |                      |                 |               |                           |                  |                   |              |
| -------------------- | ----------- | --------------- | ----------- | ------------------ | ---------- | ------------ | ----------- | -------------- | -------------------- | --------------- | ------------- | ------------------------- | ---------------- | ----------------- | ------------ |
|                      |             |                 |             |                    |            |              |             | volume         | manufacturing        |                 | because       | it can                    | leverage         | large-diameter    |              |
| Low-inductance       |             | packaging       |             | and co-located     |            | gate drivers | are         |                |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | silicon wafers |                      | and established |               | semiconductor-fabrication |                  |                   | in-          |
| therefore            | central     | to realizing    |             | the high-frequency |            | advantage    |             | of             |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | frastructure   | [99,                 | 97].            | This platform |                           | is particularly  |                   | relevant     |
| GaN [13,             | 60].        |                 |             |                    |            |              |             |                |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | to lateral     | devices              | in the          | voltage       | classes                   | used             | by                | many data-   |
| Packaging            | is          | not a           | secondary   | implementation     |            |              | detail;     | it             |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | center PFC,    | isolated-conversion, |                 |               | and                       | intermediate-bus |                   | stages.      |
| determines           | whether     | the             | intrinsic   | device             | capability | is           | preserved   |                |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | However,       | the economic         |                 | advantage     | of                        | the Si           | substrate         | does not     |
| in the converter     |             | [13]. Parasitic |             | inductance         | influences |              | voltage     |                |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | eliminate      | epitaxial            | complexity.     |               | Lattice                   | and              | thermal-expansion |              |
| overshoot,           | current     | ringing,        | switching   |                    | loss,      | and EMI,     | while       |                |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | mismatch       | require              | engineered      |               | nucleation,               | transition,      |                   | and buffer   |
| parasitic            | capacitance |                 | controls    | common-mode        |            | displacement |             |                |                      |                 |               |                           |                  |                   |              |
|                      |             |                 |             |                    |            |              |             | layers to      | control              | cracking,       | residual      | stress,                   | vertical         |                   | leakage, and |
currentandmayincreaseisolationorfilterrequirements.Atthe
|     |     |     |     |     |     |     |     | wafer bow | [100]. | These | effects | influence |     | process | uniformity, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | ------- | --------- | --- | ------- | ----------- |
sametime,thepackagemustprovideasufficientlylowthermal
|     |     |     |     |     |     |     |     | usable wafer | area, | trapping |     | behavior, | dynamic | R   | , and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | -------- | --- | --------- | ------- | --- | ----- |
impedance while maintaining dielectric isolation, mechanical DS(on)
|     |     |     |     |     |     |     |     | final device | yield. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
integrity,manufacturability,andcompatibilitywithhigh-volume
|           |       |              |     |                |     |           |          | GaN-on-SiC |     | prioritizes | thermal | performance |     |     | and material |
| --------- | ----- | ------------ | --- | -------------- | --- | --------- | -------- | ---------- | --- | ----------- | ------- | ----------- | --- | --- | ------------ |
| assembly. | These | requirements |     | are especially |     | stringent | in high- |            |     |             |         |             |     |     |              |
density power shelves and near-processor converters, where compatibility relative to GaN-on-Si, supported by the high
|         |        |            |     |            |      |          |     | thermal | conductivity |     | of SiC | and its | more | favorable | lattice |
| ------- | ------ | ---------- | --- | ---------- | ---- | -------- | --- | ------- | ------------ | --- | ------ | ------- | ---- | --------- | ------- |
| airflow | can be | restricted | and | local heat | flux | is high. |     |         |              |     |        |         |      |           |         |
Reliabilityundercontinuousloadremainsaprimaryadoption relationship with GaN [101, 98]. This can be advantageous
|            |            |               |       |              |        |           |         | in applications |              | where | localized   | heat     | flux | or sustained | power |
| ---------- | ---------- | ------------- | ----- | ------------ | ------ | --------- | ------- | --------------- | ------------ | ----- | ----------- | -------- | ---- | ------------ | ----- |
| criterion. | Dynamic    | on-resistance |       | and          | charge | trapping  | can     |                 |              |       |             |          |      |              |       |
|            |            |               |       |              |        |           |         | density         | is a primary |       | constraint. | However, |      | GaN-on-SiC   | also  |
| increase   | conduction | loss          | after | high-voltage |        | switching | events, |                 |              |       |             |          |      |              |       |
while threshold-voltage drift, gate degradation, and package inherits exposure to SiC substrate price, wafer-capacity limita-
|          |           |           |          |     |           |       |         | tions, and        | competing |     | demand          | from | electric-vehicle, |     | charging,    |
| -------- | --------- | --------- | -------- | --- | --------- | ----- | ------- | ----------------- | --------- | --- | --------------- | ---- | ----------------- | --- | ------------ |
| wear-out | can alter | converter | behavior |     | over time | [38]. | Thermal |                   |           |     |                 |      |                   |     |              |
|          |           |           |          |     |           |       |         | renewable-energy, |           | and | grid-conversion |      | markets.          | It  | is therefore |
cyclingcanfatiguedie-attachlayers,metallization,solderjoints,
|               |         |            |           |                |              |               |           | most appropriate |           | where      | the        | additional | thermal    |     | or electrical |
| ------------- | ------- | ---------- | --------- | -------------- | ------------ | ------------- | --------- | ---------------- | --------- | ---------- | ---------- | ---------- | ---------- | --- | ------------- |
| and substrate |         | interfaces | even      | when           | the average  |               | operating |                  |           |            |            |            |            |     |               |
|               |         |            |           |                |              |               |           | performance      | justifies |            | the higher | substrate  |            | and | supply-chain  |
| temperature   | remains | within     |           | specification. |              | Qualification | for       |                  |           |            |            |            |            |     |               |
| data-center   | use     | should     | therefore | combine        | conventional |               | static    | burden.          |           |            |            |            |            |     |               |
|               |         |            |           |                |              |               |           | Native-GaN       |           | substrates | provide    | the        | low-defect |     | foundation    |
stresstestingwithsystem-representativeevaluationofrepetitive
switching, line and load transients, startup and shutdown, required by many vertical-GaN device concepts, particularly
|           |         |          |         |          |     |                 |     | those using | thick | drift | regions | and | high | blocking | voltage |
| --------- | ------- | -------- | ------- | -------- | --- | --------------- | --- | ----------- | ----- | ----- | ------- | --- | ---- | -------- | ------- |
| overload, | thermal | cycling, | current | sharing, |     | EMI compliance, |     |             |       |       |         |     |      |          |         |
andfaultrecovery.Therequiredtestenvelopeshouldbederived [102].Theiradvantagesincludereducedlatticemismatch,lower
from the voltage, current, switching, and thermal domains dislocation density, and the ability to form vertical current
|            |     |         |            |     |             |      |          | paths without | the | highly | mismatched |     | buffer | structures | required |
| ---------- | --- | ------- | ---------- | --- | ----------- | ---- | -------- | ------------- | --- | ------ | ---------- | --- | ------ | ---------- | -------- |
| summarized | in  | Table I | and Figure | 6,  | rather than | from | a single |               |     |        |            |     |        |            |          |
nominal operating point. on foreign substrates. Nevertheless, bulk-GaN wafer diameter,
|     |     |     |     |     |     |     |     | availability, | cost, | and | supplier | diversity | remain | comparatively |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | -------- | --------- | ------ | ------------- | --- |
V. MANUFACTURING,PACKAGING,RELIABILITY,AND limited [103]. Native GaN is consequently better positioned
SUPPLY-CHAINCONSTRAINTS
|     |            |     |         |     |                  |     |      | as an enabling |             | platform    | for | specialized | high-voltage     |     | devices |
| --- | ---------- | --- | ------- | --- | ---------------- | --- | ---- | -------------- | ----------- | ----------- | --- | ----------- | ---------------- | --- | ------- |
|     |            |     |         |     |                  |     |      | than as        | a near-term | replacement |     | for         | the large-volume |     | lateral |
| GaN | deployment | in  | energy- | and | carbon-conscious |     | data |                |             |             |     |             |                  |     |         |
centersultimatelydependsonwhetherdevice-levelperformance GaN-on-Si ecosystem.
can be reproduced at high manufacturing volume, integrated Substrate selection therefore cannot be reduced to material
into low-parasitic and thermally robust packages, and qualified performance alone. GaN-on-Si provides manufacturing scale,
for continuous mission-critical operation. Substrate availability, GaN-on-SiC provides additional thermal headroom, and native
epitaxial yield, metallization compatibility, package assembly, GaN supports high-quality vertical structures. The appropriate
and supplier concentration therefore influence not only device choice depends on device voltage, current density, thermal
cost but also converter efficiency, reliability, replacement boundary, manufacturing volume, qualification requirements,
frequency, and total cost of ownership [55, 61]. Table II and acceptable cost per converter function.

TABLEII
REPRESENTATIVEMANUFACTURING,PACKAGING,RELIABILITY,ANDSUPPLY-CHAINCONSIDERATIONSRELEVANTTOGANDEPLOYMENTINDATA-CENTER
POWERCONVERSION.QUANTITATIVEVALUESARESCREENING-LEVELANCHORSFROMPUBLICLYAVAILABLETECHNICALREFERENCES,DATASHEETS,
MARKETREPORTS,ANDRELIABILITYDOCUMENTATIONRATHERTHANUNIVERSALVALUESFORALLGANPROCESSESORPRODUCTS.
Manufacturinglever Representativequantitativeanchor Implicationforconverterdeployment Ref.
Substrateplatformsandupstreamsupply
GaN-on-Si Publiclydescribedmanufacturing ProvidesthestrongestleveragefromexistingSi-fabricationinfrastructure.Scaling [62,63,64,65,
platformsinclude200-mmwafers,with challengesshifttowardepitaxialstress,waferbow,crackcontrol,defectmanagement, 66,67,68,69]
300-mmGaN-on-Similestonesalso andprocessuniformity,allofwhichinfluenceyieldanddynamicreliability.
reported.
GaN-on-SiC SiCsubstratesarecommerciallyoffered Providesgreatersubstrate-levelthermalheadroomandafavorablelatticerelationship,but [70,71,72,73]
at150and200mm.Onesupplierreports increasesexposuretoSiCwafercost,capacityconstraints,andcompetingdemandfrom
|     | thermalconductivitynear370W/(m·K). |     | automotiveandgrid-powermarkets. |     |     |     |     |
| --- | ---------------------------------- | --- | ------------------------------- | --- | --- | --- | --- |
NativeGaN Bulk-GaNofferingsarecommonly Supportslow-defectvertical-GaNstructuresandthickhigh-voltagedriftregions,but [74,75,76,77,
reportedinapproximately2–4-in. limitedwaferdiameter,substratecost,andsupplierconcentrationconstrainnear-term 78]
|     | formats,withhistoricallylimitedsupplier |     | volumedeployment. |     |     |     |     |
| --- | --------------------------------------- | --- | ----------------- | --- | --- | --- | --- |
diversity.
Upstreamgalliumsupply RecentUSGSreportingattributes Geographicconcentrationintroducesprocurement,geopolitical,andprice-volatilityrisks. [79,80,81]
approximately99%ofworldwideprimary Data-centerdeploymentthereforebenefitsfrommultiplequalifiedsuppliers,foundries,
|     | low-puritygalliumproductiontoChina. |     | andsubstratepathways. |     |     |     |     |
| --- | ----------------------------------- | --- | --------------------- | --- | --- | --- | --- |
Metallization,packaging,andthermalintegration
GoldcompatibilityinSi Shared-toolcontamination-controlrules Au-freeprocessflowsimprovecompatibilitywithestablishedSi-fabricationinfrastructure [82,83,84]
fabs mayrestrictAu-containingmaterialsand andreducetheneedforisolatedprocessequipment.
processes.
Au-to-Cuwiretransition Oneindustrycasestudyreports Canreduceinterconnectcostanddependenceonpreciousmetals,althoughCu-wire [83,85,86]
material-costreductionofupto90% reliability,bond-padcompatibility,andassemblyconditionsmustbequalifiedforthe
|     | whenreplacingAubondingwirewithCu |     | selectedpackage. |     |     |     |     |
| --- | -------------------------------- | --- | ---------------- | --- | --- | --- | --- |
wire.
Packageinductance Representativeestimatesincludelessthan Nanohenry-scaleparasiticsinfluencedrainovershoot,ringing,switchingloss,false [86,69]
0.2nHforanLGA-classpackage, turn-on,andEMIunderhighdv/dtanddi/dt.Packagearchitecturecantherefore
|     | approximately0.5nHforaQFNCu-clip |     | determinewhethertheintrinsicswitchingcapabilityofGaNisusable. |     |     |     |     |
| --- | -------------------------------- | --- | ------------------------------------------------------------- | --- | --- | --- | --- |
package,andapproximately1.5nHfor
anSO-8-classpackage.
Packagethermal Representativedatasheetsreporttop-side Thepackage,dieattach,PCB,andcold-plateinterfacefrequentlydominatetheeffective [87,88,89,90]
resistance junction-to-casethermalresistanceof thermalpath.Advancedcoolingpackagesimproveheatextractionbutmayincrease
|     | approximately0.28◦C/Wanda |     | assemblycomplexityandyieldsensitivity. |     |     |     |     |
| --- | ------------------------- | --- | -------------------------------------- | --- | --- | --- | --- |
bottom-cooledexamplenear0.5◦C/W.
Qualification,yield,andlifecycleimpact
HTOLqualification Acommonlycitedqualificationreference Providesacommonreliabilityframework,butlifetimeextrapolationisvalidonlywhen [91,92,93]
baseline pointis1000hofhigh-temperature theaccelerationmodelcorrespondstotherelevantgate,trapping,interconnect,or
|     | operatinglifeatajunctiontemperatureof |     | packagefailuremechanism. |     |     |     |     |
| --- | ------------------------------------- | --- | ------------------------ | --- | --- | --- | --- |
125◦Corhigher,dependingonthe
deviceandapplicablestandard.
Manufacturingyield Onepublicreportcitesa97%yield Yieldaffectsdevicecostandthemanufacturingburdenperfunctionaldie.Thevalue [91,94,95]
exampleina200-mmGaN shouldbetreatedasaprocess-specificexampleratherthanauniversalGaNyield
|     | manufacturingcontext. |     | benchmark. |     |     |     |     |
| --- | --------------------- | --- | ---------- | --- | --- | --- | --- |
Embodied-emissions Apublishedwafer-levellifecycle Providesascreening-levelbasisforexamininghowdieyield,packageburden,equipment [96]
anchor assessmentreportsdirectpost-abatement lifetime,andreplacementfrequencyaffectembodiedemissionsperdeliveredconverter
|     | emissionsontheorderoftensof |     | service. |     |     |     |     |
| --- | --------------------------- | --- | -------- | --- | --- | --- | --- |
kilogramsofCO2eper300-mmwafer,
withrepresentativecasesof
approximately65–88kgCO2e/wafer.a
aThewafer-levelvalueisageneralsemiconductor-manufacturingproxyandshouldnotbeinterpretedasaGaN-specificlifecycleinventorywithoutprocess-
specificvalidation.
B. Metallization, Packaging, and Thermal-Electrical Co- and thermal conduction, but their benefits depend on bond-pad
Design metallurgy, intermetallic formation, oxidation control, mechan-
|     |     |     |     | ical stress, | and thermal-cycling | reliability. | Their presence in |
| --- | --- | --- | --- | ------------ | ------------------- | ------------ | ----------------- |
Metallization and packaging determine whether the semi- established recycling streams is a lifecycle advantage, but end-
conductor die can be manufactured using high-volume infras- of-life recovery remains dependent on package construction
tructure and whether its switching capability is preserved in and disassembly economics [106]. Metallization choice should
the converter. The transition from Au toward Cu- and Al- thereforebetreatedprimarilyasamanufacturingandreliability
based interconnects can reduce material cost and improve decision, with sustainability benefits evaluated as a secondary
| compatibility | with Si-fabrication   | environments   | in which Au     | consequence. |                 |               |                      |
| ------------- | --------------------- | -------------- | --------------- | ------------ | --------------- | ------------- | -------------------- |
| contamination | is tightly controlled | [104,          | 105]. Gold-free |              |                 |               |                      |
|               |                       |                |                 | Packaging    | is particularly | consequential | for GaN because      |
| processing    | can therefore broaden | foundry access | and reduce      |              |                 |               |                      |
|               |                       |                |                 | fast voltage | and current     | transitions   | make small parasitic |
theneedfordedicatedcontamination-controlledmodules[104]. elements electrically significant [107, 108]. Common-source
CuandAlinterconnectsmayalsoprovidefavorableelectrical inductance and power-loop inductance increase gate ringing,

drain overshoot, switching energy, and EMI. Parasitic ca- metallization,andpackagingthereforestrengthentheeconomic
pacitance can increase common-mode displacement current and lifecycle case simultaneously [6].
and isolation stress. Low-inductance package formats, Kelvin-
source connections, Cu clips, embedded dies, and co-packaged D. Supply-Chain and Data-Center Deployment Implications
gate drivers can preserve fast-switching performance, but they
GaN supply-chain risk extends beyond the availability of
also increase assembly and qualification complexity.
elemental gallium. Commercial deployment also depends on
The thermal path must be co-designed with the electrical
epitaxial reactors, qualified wafer suppliers, foundry capacity,
package. Advanced substrates, sintered interfaces, top-side
package assembly, test infrastructure, and access to second-
cooling,double-sidedcooling,andhigh-conductivitybaseplates
source devices with sufficiently comparable switching and
can reduce junction-to-coolant thermal resistance [108]. How-
reliability characteristics [55, 61]. A nominally equivalent
ever, increasing package complexity can introduce additional
transistor from another supplier may require changes in gate
interfaces, coefficient-of-thermal-expansion mismatch, void
drive,deadtime,protectionthresholds,layout,thermalinterface,
sensitivity, and assembly-yield loss. A more complex module
or EMI filtering.
is advantageous only when its lower loss or longer service
For mission-critical data-center infrastructure, second-source
life offsets the added material and manufacturing burden.
qualification must therefore occur at both the component and
Long-lived, highly integrated modules may therefore provide
converterlevels.Deviceprocurementstrategiesshouldconsider
better lifecycle performance than frequently replaced lower-
package compatibility, dynamic R , gate-voltage limits,
DS(on)
cost packages, provided that reliability and repairability are
reverse-conduction behavior, thermal impedance, reliability
considered during design [109].
data, and long-term product availability. Multi-source wafer
and foundry strategies can reduce geographic and supplier
C. Qualification, Yield, and Lifetime concentration, but only when the resulting process variants
maintain consistent electrical and reliability behavior.
Reliability and manufacturing yield link semiconductor
The practical adoption criterion is ultimately total cost of
technologydirectlytoconvertereconomicsandlifecycleimpact
ownership rather than device price alone. A higher-cost GaN
[38]. A device that offers lower switching loss but exhibits
deviceorpackagemaybejustifiedifitreducesconverterlosses,
poor yield, unstable dynamic behavior, or shortened package
passive-component volume, cooling demand, rack footprint, or
lifetime may increase cost, spare inventory, maintenance
maintenance frequency. Conversely, a device with excellent
requirements, and replacement frequency. These concerns are
laboratoryperformancemayprovidelimitedinfrastructurevalue
especially important in data centers, where power systems
if it requires a single-source substrate, unusually complex as-
operate continuously and component failure can compromise
sembly, or insufficiently demonstrated lifetime. Manufacturing
service availability.
scale, package performance, qualification maturity, and supply
Conventionalqualificationtestsprovideanecessarybaseline,
continuity must therefore be evaluated together with efficiency
buttheydonotbythemselvesreproducethecompleteconverter
and power density when selecting GaN for data-center power
mission profile. GaN devices may experience repetitive high-
conversion.
voltage off-state stress, rapid hard or soft commutation, reverse
conduction, load transients, startup and shutdown events, and
VI. QUANTITATIVEENERGYANDOPERATIONALCARBON
elevated local heat flux. Relevant degradation mechanisms
include charge trapping, dynamic R , gate leakage,
IMPACT
DS(on)
threshold-voltage shift, dielectric degradation, metallization While GaN is often justified by device-level efficiency and
fatigue, die-attach degradation, and solder- or interconnect- power-densityadvantages,alower-carbondata-centerargument
related thermal cycling [110, 38]. requiresanexplicitlinkbetweenconverterperformance,facility
High-temperature operating life must therefore be supple- electricityconsumption,andCO emissions[111].Thissection
2
mented by dynamic and system-representative testing. Qualifi- introducesacompactquantitativeframeworkconnecting(i)the
cation should include repetitive switching stress, temperature multiplicative efficiency of cascaded power-conversion stages,
cycling, power cycling, surge and fault events, current sharing, (ii) the incremental cooling demand associated with converter
EMI-related overstress, and operation across the expected losses, and (iii) embodied impacts associated with manufac-
partial-load range. Acceleration factors should be linked to turing yield and replacement cycles [112]. The framework
a physically relevant failure mechanism rather than applied providesorder-of-magnitudesensitivityestimatesforhowstage-
generically. level efficiency improvements, such as sub-percentage-point
Yield improvements reduce the number of wafers, epitaxial gains enabled by GaN in front-end PFC or high-frequency
runs,packages,andassemblyoperationsrequiredperfunctional isolated conversion, affect annual facility energy consumption
device. Lifetime improvements reduce the number of replace- and operational emissions [3]. The objective is not to predict a
ment devices and modules required over the service life of the universal change in PUE or CO emissions, but to establish a
2
facility [6]. Both mechanisms lower cost and embodied burden transparent, parameterized model that can be populated using
per unit of delivered power-conversion service. Improvements site-specific values for load, utilization, cooling performance,
in epitaxy, passivation, gate-stack design, field management, grid carbon intensity, and equipment lifetime [113].

Fig.7. (a)Incrementalenergy-flowmodelforarepresentativecascadeddata-centerpower-deliverychain.ForafixeddeliveredITload,thestageefficiencies
determinetherequiredchaininputpowerandtotalconversionloss.Anefficiencyimprovementreducesconverterlossby∆P loss andproducesanassociated
cooling-powerreductionofapproximatelyα ∆P /COPsys.(b)IllustrativeannualoperationalCO2reductionasafunctionofabsolutestage-efficiency
|     |     |     |     | cool | loss |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
improvementfora1-MWcontinuouslydeliveredITload.Differencesamongthecurvesarisefromtheassumedbaselinestageefficienciesandloadprocessed;stage
positionalonedoesnotdeterminethesystem-levelbenefit.Thecalculationassumesu=1,COPsys=4,αcool=1,andCI =0.367kgCO2/kWh.
grid
| A. System      | Boundary     | and           | Metrics   |           |          |              |          |     |     |            |     |        |     |     |
| -------------- | ------------ | ------------- | --------- | --------- | -------- | ------------ | -------- | --- | --- | ---------- | --- | ------ | --- | --- |
| The electrical | boundary     |               | used here | separates |          | the power    | deliv-   |     |     |            |     |        |     |     |
|                |              |               |           |           |          |              |          |     |     | CUE≈PUE,CI |     | grid . |     | (5) |
| ered to the    | IT equipment |               | from the  | power     | entering | the          | selected |     |     |            |     |        |     |     |
| conversion     | chain.       | The delivered |           | IT load,  | P        | , represents | the      |     |     |            |     |        |     |     |
IT
regulatedelectricalpowersuppliedattheoutputofthemodeled For avoided-emissions calculations, a marginal grid emis-
chain. Facility power additionally includes conversion losses, sions factor is preferable when available because it represents
cooling energy, and other overhead loads. Carbon-reduction the generation displaced by the reduction in electricity demand.
progress is considered through both (i) use-phase emissions An average grid factor may instead be used as a transparent
associated with IT and facility electricity consumption and screening-level approximation.
(ii) embodied emissions associated with manufacturing and Embodiedemissionsperfunctionaldiearerepresentedusing
| replacement | of power            | devices | and | modules | [114].   |     |     | the proxy |     |     |     |     |     |     |
| ----------- | ------------------- | ------- | --- | ------- | -------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
| Power       | usage effectiveness |         | is  | defined | as [115] |     |     |           |     |     |     |     |     |     |
E
|                  |          |        |                | facility, |        |                |        |       |         |         | M wafer     |          |                |     |
| ---------------- | -------- | ------ | -------------- | --------- | ------ | -------------- | ------ | ----- | ------- | ------- | ----------- | -------- | -------------- | --- |
|                  |          | PUE=   |                |           |        |                | (3)    |       | M       | ≈       |             | +M       | +M ,           | (6) |
|                  |          |        |                | E         |        |                |        |       |         | emb,die | N Y         | pkg      | assy           |     |
|                  |          |        |                | IT        |        |                |        |       |         |         | die die     |          |                |     |
| where            | E        | is the | total facility |           | energy | and E          | is the |       |         |         |             |          |                |     |
|                  | facility |        |                |           |        | IT             |        |       |         |         |             |          |                |     |
| energy delivered |          | to IT  | equipment      | over      | the    | same reporting |        |       |         |         |             |          |                |     |
|                  |          |        |                |           |        |                |        | where | M wafer | is the  | wafer-level | embodied | greenhouse-gas |     |
interval. Carbon usage effectiveness is defined as [116] burden, N is the number of gross dies per wafer, Y
|     |     |     |     |     |     |     |     |        | die        |            |     |       |             | die |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ---------- | --- | ----- | ----------- | --- |
|     |     |     |     |     |     |     |     | is the | functional | die yield, | and | M and | M represent |     |
|     |     |     |     |     |     |     |     |        |            |            |     | pkg   | assy        |     |
M CO2,facility,
CUE= (4) packaging and assembly contributions, respectively. Wafer-
E
IT level greenhouse-gas data can therefore be propagated through
where M CO2,facility is the operational mass of CO∗2 as- yield, device count, service life, and replacement assumptions
sociated with facility electricity consumption. For a fully [117]. The numerical example below evaluates operational
grid-supplied facility using a consistent grid emissions factor, effects only; embodied impacts should be added separately
CI∗grid, the reporting relationship may be approximated as when sufficiently resolved lifecycle data are available.

B. Cascaded Efficiency and Incremental Cooling Demand assuming that all other facility overheads remain unchanged
For a power-conversion chain containing n series-connected [121]. Because Eq. (13) already accounts explicitly for the
|             |              |     |           |            |     |            |           | direct electrical-loss |     | reduction |     | and its      | cooling | consequence, |            |
| ----------- | ------------ | --- | --------- | ---------- | --- | ---------- | --------- | ---------------------- | --- | --------- | --- | ------------ | ------- | ------------ | ---------- |
| stages with | efficiencies |     | η i , the | end-to-end |     | efficiency | is multi- |                        |     |           |     |              |         |              |            |
|             |              |     |           |            |     |            |           | multiplying            | the | result by | PUE | would double | count   | at           | least part |
plicative [118]:
|     |     |     |     |     |     |     |     | of the same | power | and | cooling | overhead. | PUE | is  | therefore |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | ------- | --------- | --- | --- | --------- |
n retained as a facility-reporting metric and contextual parameter,
(cid:89)
|     |     |     | η   | =   | η . |     | (7) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
chain i but it is not used as an additional multiplier in the incremental
|     |         |           |     | i=1  |         |            |       | calculation | below. |     |     |     |     |     |     |
| --- | ------- | --------- | --- | ---- | ------- | ---------- | ----- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
| For | a fixed | delivered | IT  | load | P , the | electrical | power |             |        |     |     |     |     |     |     |
IT
|          |             |            |     |       |     |       |     | C. Illustrative | Full-Utilization |          |            | Sensitivity | Case    |                 |     |
| -------- | ----------- | ---------- | --- | ----- | --- | ----- | --- | --------------- | ---------------- | -------- | ---------- | ----------- | ------- | --------------- | --- |
| entering | the modeled | conversion |     | chain | is  | [119] |     |                 |                  |          |            |             |         |                 |     |
|          |             |            |     |       |     |       |     | Representative  |                  | baseline | parameters |             | used in | the sensitivity |     |
P IT calculation are summarized in Table III. These values are
|     |     |     | P = |     | ,   |     | (8) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | in  | η   |     |     |     |     |     |     |     |     |     |     |     |
chain illustrative anchors rather than universal data-center operating
|         |       |                  |      |      |     |     |     | conditions    | and should  |     | be replaced | with | site-specific | parameters |     |
| ------- | ----- | ---------------- | ---- | ---- | --- | --- | --- | ------------- | ----------- | --- | ----------- | ---- | ------------- | ---------- | --- |
| and the | total | power-conversion |      | loss | is  |     |     |               |             |     |             |      |               |            |     |
|         |       |                  |      |      |     |     |     | in a detailed | assessment. |     |             |      |               |            |     |
|         |       | P                | =P   | −P   | .   |     | (9) |               |             |     |             |      |               |            |     |
|         |       |                  | loss | in   | IT  |     |     |               |             |     |             |      |               |            |     |
TABLEIII
For a change in the efficiency of stage j, the sensitivity of BASELINEASSUMPTIONSFORTHECOMPACTSENSITIVITYCALCULATION
[122,123,124,125,126,127,128,129].
| the chain | input | power | is  |       |     |     |      |                         |     |     |     |              |     |     |     |
| --------- | ----- | ----- | --- | ----- | --- | --- | ---- | ----------------------- | --- | --- | --- | ------------ | --- | --- | --- |
|           |       |       |     |       |     |     |      | Parameter               |     |     |     | Assumedvalue |     |     |     |
|           |       | ∂P    | in  | P     | IT  |     |      |                         |     |     |     |              |     |     |     |
|           |       |       | =−  |       | .   |     | (10) |                         |     |     |     |              |     |     |     |
|           |       | ∂η    |     | η     | η   |     |      | DeliveredITload,PIT     |     |     |     | 1MW          |     |     |     |
|           |       |       | j   | chain | j   |     |      |                         |     |     |     |              |     |     |     |
|           |       |       |     |       |     |     |      | Annualoperatingtime,hyr |     |     |     | 8760h/year   |     |     |     |
Equation (10) shows that, for a purely series-connected Utilizationfactor,u 1.0
chain serving the same load, the impact of a stage-efficiency Gridemissionsfactor,CI 0.81lbCO2/kWh(0.367kg
grid
CO2/kWh)
improvementdependsonthestageefficiencyandthemagnitude
|               |          |             |                |              |        |          |           | Cooling-systemCOP,COPsys     |     |     |      | 4                           |     |     |     |
| ------------- | -------- | ----------- | -------------- | ------------ | ------ | -------- | --------- | ---------------------------- | --- | --- | ---- | --------------------------- | --- | --- | --- |
| of its change |          | rather than | on             | its physical |        | position | alone. In |                              |     |     |      |                             |     |     |     |
|               |          |             |                |              |        |          |           | Activelycooledlossfraction,α |     |     | cool | 1.0                         |     |     |     |
| practical     | branched | power       | architectures, |              | stages | that     | process   | a                            |     |     |      |                             |     |     |     |
|               |          |             |                |              |        |          |           | PFCefficiency,ηPFC           |     |     |      | 0.990baseline;0.993improved |     |     |     |
larger fraction of the total IT load provide greater absolute Isolated-stageefficiency,ηiso 0.985
leverage than converters serving only an individual board, 48-Vfront-stageefficiency, 0.984
η
| processor, | or load | branch. |           |     |       |                    |     | 48V,front |     |     |     |     |     |     |     |
| ---------- | ------- | ------- | --------- | --- | ----- | ------------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
| Although   | both    | the     | delivered | IT  | power | and the conversion |     |           |     |     |     |     |     |     |     |
losses ultimately appear primarily as heat within the facility The calculation assumes a constant 1-MW delivered IT
|            |           |        |              |           |              |         |             | load operating | continuously       |     |     | throughout  | the year. | Thus,  | u=1    |
| ---------- | --------- | ------ | ------------ | --------- | ------------ | ------- | ----------- | -------------- | ------------------ | --- | --- | ----------- | --------- | ------ | ------ |
| thermal    | boundary  | [120], | the          | delivered | IT           | load is | held con-   |                |                    |     |     |             |           |        |        |
|            |           |        |              |           |              |         |             | represents     | a full-utilization |     |     | sensitivity | case      | rather | than a |
| stant when | comparing |        | the baseline |           | and improved |         | converters. |                |                    |     |     |             |           |        |        |
Therefore, the incremental cooling benefit is governed by the universal data-center operating profile. The assumed cooling-
|           |               |     |      |        |         |           |         | system coefficient |     | of  | performance | is  | COPsys | =   | 4, and |
| --------- | ------------- | --- | ---- | ------ | ------- | --------- | ------- | ------------------ | --- | --- | ----------- | --- | ------ | --- | ------ |
| reduction | in conversion |     | loss | rather | than by | the total | IT heat |                    |     |     |             |     |        |     |        |
load. Defining the positive loss reduction as αcool = 1 assumes that all avoided converter heat would
|     |     |     |     |     |     |     |     | otherwise   | be removed |            | by the     | active cooling |         | system.         | PUE is |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | ---------- | ---------- | -------------- | ------- | --------------- | ------ |
|     |     |     |     |     |     |     |     | not applied | as an      | additional | multiplier |                | because | the incremental |        |
| ∆P  | =P  |     | −P  | =P  |     | −P  | ,   |             |            |            |            |                |         |                 |        |
loss loss,base loss,new in,base in,new (11) cooling contribution is calculated explicitly through COP ;
sys
|     |     |     |     |     |     |     |     | applying | both | factors | would | risk double | counting |     | facility |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------- | ----- | ----------- | -------- | --- | -------- |
thecorrespondingreductionincoolingpowercanbeapprox-
overhead.
imated as
|     |     |     |      |             |       |     |      | Using        | the three-stage    |     | representative |     | chain,    |     |      |
| --- | --- | --- | ---- | ----------- | ----- | --- | ---- | ------------ | ------------------ | --- | -------------- | --- | --------- | --- | ---- |
|     |     |     |      | α c oo l ∆P | loss, |     |      |              |                    |     |                |     |           |     |      |
|     |     | ∆P  | ≈    |             |       |     | (12) | η chain,base | =0.990×0.985×0.984 |     |                |     | =0.95955. |     | (14) |
|     |     |     | cool | C O         | P     |     |      |              |                    |     |                |     |           |     |      |
sys
|                |         |                |               |     |                |     |             | This multiplicative   |        |               | structure    | represents | a      | cascaded     | data-   |
| -------------- | ------- | -------------- | ------------- | --- | -------------- | --- | ----------- | --------------------- | ------ | ------------- | ------------ | ---------- | ------ | ------------ | ------- |
| where          | COP∗sys | is             | the effective |     | cooling-system |     | coefficient |                       |        |               |              |            |        |              |         |
|                |         |                |               |     |                |     |             | center power-delivery |        |               | architecture | in which   |        | the selected | con-    |
| of performance |         | and 0≤α∗cool≤1 |               |     | represents     | the | fraction    | of                    |        |               |              |            |        |              |         |
|                |         |                |               |     |                |     |             | version               | stages | are connected |              | in series  | [129]. | If           | the PFC |
avoidedconverterheatthatwouldotherwiseberemovedbythe
|                |             |         |           |             |     |         |          | efficiency             | increases | from | 0.990       | to 0.993,  | corresponding |      | to       |
| -------------- | ----------- | ------- | --------- | ----------- | --- | ------- | -------- | ---------------------- | --------- | ---- | ----------- | ---------- | ------------- | ---- | -------- |
| active cooling |             | system. | For power | electronics |     | located | entirely |                        |           |      |             |            |               |      |          |
|                |             |         |           |             |     |         |          | a 0.3-percentage-point |           |      | improvement | consistent |               | with | reported |
| within the     | conditioned |         | thermal   | boundary,   | α   | ≈1      | provides | a                      |           |      |             |            |               |      |          |
cool high-performance GaN PFC demonstrations [50, 123], the new
usefulscreening-levelcase.Ifaportionofthelossisdissipated
|         |              |        |        |     |     |        |          | chain efficiency |     | is  |     |     |     |     |     |
| ------- | ------------ | ------ | ------ | --- | --- | ------ | -------- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| outside | the actively | cooled | space, | α   | <1  | should | be used. |                  |     |     |     |     |     |     |     |
cool
The resulting reduction in facility electrical power is η chain,new =0.993×0.985×0.984 =0.96246. (15)
(cid:18) (cid:19) Although the absolute PFC efficiency improvement is only
α cool
|     | ∆P  |     | ≈∆P | 1+  |     | ,   | (13) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
facility loss COP 0.3 percentage points, the nominal PFC loss fraction decreases
sys

| from 1.0% | to 0.7%, corresponding |     | to a | 30% reduction |     | in that |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------- | --- | ---- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
stage’s fractional loss under the assumed operating condition. ∆E annual = ∆P facility,k ∆t k , (23)
| For P | =1 MW, | the reduction | in  | input power | is  |     |     |     |     |     | k   |     |     |     |     |
| ----- | ------ | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IT
(cid:18) (cid:19) or an equivalent integral over the annual load profile.
|     |     |     | 1   | 1   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
∆P =P − Similarly, the stage providing the largest benefit is not
in IT
|     |     | η chain,base |     | η chain,new |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
necessarilytheearlieststageinthechain.Inaseries-connected
|     |     | (cid:18) | 1       | 1       | (cid:19) | (16) |              |                  |     |               |     |                 |                  |         |     |
| --- | --- | -------- | ------- | ------- | -------- | ---- | ------------ | ---------------- | --- | ------------- | --- | --------------- | ---------------- | ------- | --- |
|     |     |          |         |         |          |      | model,       | all efficiencies |     | multiply,     | and | the sensitivity |                  | depends | on  |
|     | =1  | MW       | −       |         |          |      |              |                  |     |               |     |                 |                  |         |     |
|     |     |          | 0.95955 | 0.96246 |          |      |              |                  |     |               |     |                 |                  |         |     |
|     |     |          |         |         |          |      | the baseline | efficiency       |     | and magnitude |     | of              | the improvement. |         | In  |
≈3.15 kW. an actual data center, absolute leverage also depends on the
|         |               |     |                    |     |     |      | fraction | of facility | power | processed |       | by that | converter. | A        | front- |
| ------- | ------------- | --- | ------------------ | --- | --- | ---- | -------- | ----------- | ----- | --------- | ----- | ------- | ---------- | -------- | ------ |
| Because | the delivered | IT  | load is unchanged, |     |     |      |          |             |       |           |       |         |            |          |        |
|         |               |     |                    |     |     |      | end PFC  | stage       | may   | therefore | have  | high    | aggregate  | leverage |        |
|         |               |     |                    |     |     |      | because  | it serves   | an    | entire    | power | shelf   | or rack,   | whereas  | a      |
|         | ∆P            | =∆P | ≈3.15              | kW. |     | (17) |          |             |       |           |       |         |            |          |        |
|         | loss          |     | in                 |     |     |      |          |             |       |           |       |         |            |          |        |
point-of-loadconverterservesonlyaparticularloadbranch,not
ForCOP∗sys=4andα∗cool=1,thefacility-levelpower simply because the PFC stage appears earlier in the conversion
| reduction | becomes |     |     |     |     |     | chain [129]. |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:18) (cid:19) Finally, the operational result does not by itself establish
1
∆P =3.15 1+ ≈3.94 kW. (18) carbonneutrality.Acompletelifecycleassessmentmustalsoac-
facility
4 count for embodied emissions, manufacturing yield, equipment
This result includes both the direct reduction in converter lifetime, replacement frequency, refrigerants, onsite generation,
electricity consumption and the incremental reduction in storage, electricity procurement, and end-of-life treatment. The
coolingpowerassociatedwiththeavoidedheatload[130,131].
|     |     |     |     |     |     |     | framework | instead | provides |     | a traceable | method | for | translating |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | -------- | --- | ----------- | ------ | --- | ----------- | --- |
For an annual utilization factor u, the corresponding energy a measured stage-efficiency improvement into an incremental
reduction is facility-energy and operational-emissions consequence without
|           |        |          |          |     |     |      | conflating                                 | PUE, | cooling | COP, | and | converter | loss. |     |     |
| --------- | ------ | -------- | -------- | --- | --- | ---- | ------------------------------------------ | ---- | ------- | ---- | --- | --------- | ----- | --- | --- |
|           | ∆E     | =∆P      | ,u,h     | .   |     | (19) |                                            |      |         |      |     |           |       |     |     |
|           | annual |          | facility | yr  |     |      |                                            |      |         |      |     |           |       |     |     |
|           |        |          |          |     |     |      | VII. DEPLOYMENTPATHWAYSANDDESIGNGUIDELINES |      |         |      |     |           |       |     |     |
| Using u=1 | and h  | yr =8760 | h/year,  |     |     |      |                                            |      |         |      |     |           |       |     |     |
GaNadoptionindata-centerpowersystemsshouldbetreated
|           |               |     |        |       |           |      | as a staged                                         | system-integration |     |           | problem    | rather | than    | as a    | direct |
| --------- | ------------- | --- | ------ | ----- | --------- | ---- | --------------------------------------------------- | ------------------ | --- | --------- | ---------- | ------ | ------- | ------- | ------ |
|           |               |     |        |       |           |      | transistor                                          | substitution       |     | [23]. The | attainable |        | benefit | depends | on     |
| ∆E annual | =3.94 kW×8760 |     | h/year | ≈34.5 | MWh/year. |      |                                                     |                    |     |           |            |        |         |         |        |
|           |               |     |        |       |           | (20) | placingGaNinconversionstageswhereswitchingandcommu- |                    |     |           |            |        |         |         |        |
The associated operational emissions reduction is tation losses represent a meaningful fraction of total loss and
|     |     |     |     |     |     |     | where increased |     | switching | frequency |     | can reduce |     | magnetic | and |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | --------- | --- | ---------- | --- | -------- | --- |
∆M =∆E ,CI . (21) capacitive volume without creating excessive electromagnetic-
|          | CO2    |     | annual  | grid  |     |     |              |        |          |     |                |     |           |       |       |
| -------- | ------ | --- | ------- | ----- | --- | --- | ------------ | ------ | -------- | --- | -------------- | --- | --------- | ----- | ----- |
|          |        |     |         |       |     |     | interference | (EMI), | thermal, |     | or reliability |     | penalties | [132, | 133]. |
| Using CI | =0.367 | kg  | CO /kWh | gives |     |     |              |        |          |     |                |     |           |       |       |
grid 2 Device selection must therefore be coordinated with converter
|     |        |       |       |       |     |      | topology,    | package, | gate | drive, | layout, | protection, |     | magnetics, |     |
| --- | ------ | ----- | ----- | ----- | --- | ---- | ------------ | -------- | ---- | ------ | ------- | ----------- | --- | ---------- | --- |
|     | ∆M CO2 | ≈12.7 | tCO 2 | /year |     | (22) |              |          |      |        |         |             |     |            |     |
|     |        |       |       |       |     |      | and cooling. |          |      |        |         |             |     |            |     |
per1MWofcontinuouslydeliveredITloadunderthestated This section organizes the deployment pathway by tech-
|     |     |     |     |     |     |     | nology | maturity | and | power-chain |     | function. | Fig. | 8   | identi- |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ----------- | --- | --------- | ---- | --- | ------- |
assumptions.
|                   |        |       |                    |     |                  |     | fies representative            |             | near-, | mid-, | and           | long-term |        | opportunities |      |
| ----------------- | ------ | ----- | ------------------ | --- | ---------------- | --- | ------------------------------ | ----------- | ------ | ----- | ------------- | --------- | ------ | ------------- | ---- |
| D. Interpretation | and    | Model | Limitations        |     |                  |     |                                |             |        |       |               |           |        |               |      |
|                   |        |       |                    |     |                  |     | across power-factor-correction |             |        |       | (PFC),        | isolated  | DC/DC, |               | 48-V |
| The result        | in Eq. | (22)  | is an illustrative |     | full-utilization |     |                                |             |        |       |               |           |        |               |      |
|                   |        |       |                    |     |                  |     | intermediate                   | conversion, |        | and   | point-of-load |           | (PoL)  | regulation.   |      |
sensitivity case rather than a universal annual savings esti- Fig. 9 complements this roadmap by illustrating the coupled
mate. Actual facility performance depends on the converter design variables that determine whether GaN’s intrinsic device
| efficiency | curves over    | the operating | range,        | server | utilization, |         |            |          |     |            |                 |     |     |          |     |
| ---------- | -------------- | ------------- | ------------- | ------ | ------------ | ------- | ---------- | -------- | --- | ---------- | --------------- | --- | --- | -------- | --- |
|            |                |               |               |        |              |         | capability | produces | a   | repeatable | converter-level |     |     | benefit. |     |
| redundancy | configuration, | cooling       | architecture, |        | climate,     | airflow |            |          |     |            |                 |     |     |          |     |
management, location of the power electronics relative to the A. Near-Term Deployment in Mature Converter Stages
conditioned thermal boundary, and temporal variation in grid Near-term adoption should prioritize converter stages for
carbon intensity. which lateral GaN devices, suitable topologies, and supporting
Inparticular,peakconverterefficiencyshouldnotbeassumed package technologies are already commercially available or
to represent annual average efficiency. AI training, inference, extensively demonstrated. These stages include front-end PFC,
networking, and storage workloads can produce time-varying resonant isolated conversion from a high-voltage DC link to
electrical demand, and redundant power systems may operate a 48-V-class bus, and selected fixed-ratio intermediate-bus
individual modules below their rated load. A more detailed converters [50]. These applications process a large fraction of
model should therefore use time-indexed load and efficiency rack or power-shelf throughput and operate under switching
data, conditions in which commutation behavior, output capacitance,

Fig.8. StageddeploymentroadmapforGaNdevicesacrossrepresentativedata-centerPFC,isolatedDC/DC,48-Vfront-stage,andPoLconversionfunctions.
Near-termopportunitiesemphasizecommerciallymaturelateralGaNanddemonstratedconvertertopologies;mid-termopportunitiesrequiretighterdevice–
package–driver–thermalco-design;andlong-termopportunitiesincludeemerginghigh-voltage,bidirectional,andhighlyintegratedarchitectures.Theroadmap
indicatesexpecteddeploymentreadinessratherthanafixedimplementationschedule.
reverse conduction, and magnetic-component size strongly the expected GaN performance.
affect converter performance. Third,qualificationshouldincludeapplication-relevantrepet-
|     |     |     |     |     |     | itive switching |     | and | transient | conditions | in addition | to  | con- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------- | ---------- | ----------- | --- | ---- |
OpenComputeProjectOpenRackV3specifiesanominal48-
V distribution architecture with an IT-equipment input range of ventional static-bias tests. The test envelope should reproduce
|     |     |     |     |     |     | representative |     | dv/dt, | di/dt, | reverse-conduction |     | intervals, | line |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------ | ------------------ | --- | ---------- | ---- |
46–52V.Centralizedrack-orshelf-levelconversionfollowedby
48-V distribution reduces conductor current and corresponding and load transients, startup, shutdown, and thermal cycling.
I2Rlossrelativetolower-voltagerackbuses.Italsomovesthe These operating conditions can govern field reliability even
|     |     |     |     |     |     | when the | nominal | voltage, | current, | and | junction-temperature |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | -------- | --- | -------------------- | --- | --- |
finalhigh-ratioconversionclosertotheprocessororaccelerator
load. In the front-end and isolated stages, lateral GaN can ratings are not exceeded.
reduce switching and commutation losses while supporting B. Mid-Term Device–Package–Driver Co-Design
| higher operating |       | frequency,     | smaller magnetics, | and | increased |          |            |           |                  |     |               |             |      |
| ---------------- | ----- | -------------- | ------------------ | --- | --------- | -------- | ---------- | --------- | ---------------- | --- | ------------- | ----------- | ---- |
|                  |       |                |                    |     |           | Mid-term | deployment |           | is characterized |     | by increasing |             | rack |
| volumetric       | power | density [125]. |                    |     |           |          |            |           |                  |     |               |             |      |
|                  |       |                |                    |     |           | power,   | higher     | converter | density,         | and | closer        | integration | of   |
Near-term deployment should follow three priorities. First, power conversion with server boards and accelerator packages.
| enhancement-mode |     | lateral           | GaN should be | applied    | in totem- |             |             |            |              |            |               |             |       |
| ---------------- | --- | ----------------- | ------------- | ---------- | --------- | ----------- | ----------- | ---------- | ------------ | ---------- | ------------- | ----------- | ----- |
|                  |     |                   |               |            |           | Under these | conditions, |            | the limiting | factors    | progressively |             | shift |
| pole PFC         | and | resonant isolated | DC/DC         | topologies | where     |             |             |            |              |            |               |             |       |
|                  |     |                   |               |            |           | from the    | intrinsic   | transistor |              | die toward | package       | parasitics, |       |
its low switching charge and absence of conventional body- driverplacement,currentsharing,thermalinterfaces,integrated
| diode reverse | recovery | provide | a direct system | advantage | [50]. |            |     |     |            |       |              |     |         |
| ------------- | -------- | ------- | --------------- | --------- | ----- | ---------- | --- | --- | ---------- | ----- | ------------ | --- | ------- |
|               |          |         |                 |           |       | magnetics, | and | EMI | compliance | [13]. | As indicated | in  | Fig. 8, |
The switching frequency should be selected from a total-loss this phase requires coordinated design of the semiconductor,
optimumratherthanfromthemaximumcapabilityofthedevice,
package,driver,PCB,magneticcomponents,protectionsystem,
| because increased |     | frequency | also raises magnetic, |     | gate-drive, |             |            |     |     |     |     |     |     |
| ----------------- | --- | --------- | --------------------- | --- | ----------- | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
|                   |     |           |                       |     |             | and cooling | interface. |     |     |     |     |     |     |
capacitive, and EMI-related losses. Gate-drive practices should be standardized around the
Second, package and PCB layout should be treated as first- selected GaN architecture rather than transferred directly from
order electrical design variables. Commutation-loop and gate- silicon MOSFET platforms. Important design variables include
loop inductances should be estimated before hardware fabri- turn-on and turn-off resistance, gate-voltage margin, source
cation and verified through impedance extraction, switching- inductance, local driver decoupling, negative turn-off bias
waveform measurements, or both. Device replacement without where permitted, and active control of abnormal switching
corresponding loop and driver redesign is unlikely to realize events.Miller-clamporequivalentfalse-turn-onmitigation,fast

overcurrent detection, and coordinated soft shutdown may be edge termination, package isolation, surge capability, short-
requireddependingonthedeviceandtopology[59].Protection circuit behavior, and high-voltage qualification must reach
response must be sufficiently fast for the limited fault-energy infrastructure-grade maturity [6]. Until then, lateral GaN may
tolerance of high-power-density GaN devices, while avoiding remain applicable through modular converter cells, while SiC
nuisance triggering during normal high-di/dt operation. continues to provide an established alternative in high-voltage
EMI becomes a primary deployment constraint as edge and high-power stages.
rates and switching frequencies increase into the hundreds-of- Highlyintegratedlong-termarchitecturesmaycombineGaN
kilohertz and megahertz ranges [134]. An explicit dv/dt and switches,drivers,protection,sensing,andcontrolwithinacom-
| di/dt strategy |     | is therefore | required | to  | balance | switching | loss, |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | -------- | --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
monpackageorpowerintegratedcircuit.Integrationcanreduce
overshoot, common-mode current, and conducted and radiated gate-loop inductance and improve switching reproducibility,
emissions.Relevantmeasuresincludeminimizingcommutation- butitcanalsoincreaselocalheatflux,common-modecoupling,
loop area, separating power and gate return paths, using repair difficulty, and dependence on a single package platform.
Kelvin-source connections where available, controlling switch- The resulting value must therefore be assessed at the converter
node copper area, optimizing common-mode capacitance, and and rack levels rather than from component count alone.
selecting packages with low parasitic inductance. Long-term adoption also requires manufacturing and qualifi-
EMI pre-compliance measurements should begin with early cationmilestones.Multi-sourcesubstrate,foundry,andpackage
converter prototypes rather than after efficiency and den- strategies are needed to limit supply-chain concentration.
sity targets have been finalized. Otherwise, additional filters, Reliability reporting should include switching-relevant stress
| shielding, | slower | gate drive, | or  | layout | changes | may eliminate |     |             |          |     |                 |             |     |       |
| ---------- | ------ | ----------- | --- | ------ | ------- | ------------- | --- | ----------- | -------- | --- | --------------- | ----------- | --- | ----- |
|            |        |             |     |        |         |               |     | and package | wear-out |     | under realistic | temperature | and | power |
the expected power-density advantage. The coupling among cycling. More transparent cradle-to-gate lifecycle data are also
parasitics, switching waveforms, emissions, and converter required to determine whether increased package complexity
| performance | is  | summarized | in  | Fig. 9. |     |     |     |                   |     |        |            |           |         |       |
| ----------- | --- | ---------- | --- | ------- | --- | --- | --- | ----------------- | --- | ------ | ---------- | --------- | ------- | ----- |
|             |     |            |     |         |     |     |     | and manufacturing |     | burden | are offset | by longer | service | life, |
Thermal and mechanical reliability also become more reduced operational loss, and lower replacement frequency
| restrictive | as the | converter | footprint |     | decreases. | Lower | total |     |     |     |     |     |     |     |
| ----------- | ------ | --------- | --------- | --- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
[111].
| loss does | not necessarily |         | imply        | a lower    | junction | temperature |         |                   |     |        |            |     |     |     |
| --------- | --------------- | ------- | ------------ | ---------- | -------- | ----------- | ------- | ----------------- | --- | ------ | ---------- | --- | --- | --- |
| when the  | same            | loss is | concentrated |            | into a   | smaller     | package |                   |     |        |            |     |     |     |
|           |                 |         |              |            |          |             |         | D. Stage-Specific |     | Design | Guidelines |     |     |     |
| area. The | thermal         | path    | from         | the active | region   | through     | the     |                   |     |        |            |     |     |     |
Independentofdeploymenthorizon,thefollowingguidelines
| package, | PCB | or substrate, | interface |     | material, | heat | spreader, |     |     |     |     |     |     |     |
| -------- | --- | ------------- | --------- | --- | --------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
and cooling system must therefore be evaluated using realistic increase the probability that GaN integration produces a
|              |       |              |             |             |               |                |        | repeatable   | system-level |         | advantage. | They reflect     | the  | coupled |
| ------------ | ----- | ------------ | ----------- | ----------- | ------------- | -------------- | ------ | ------------ | ------------ | ------- | ---------- | ---------------- | ---- | ------- |
| spatial heat | flux  | and boundary |             | conditions. | Qualification |                | should |              |              |         |            |                  |      |         |
|              |       |              |             |             |               |                |        | dependencies | in           | Fig. 9, | where the  | device, package, | gate | drive,  |
| include      | power | cycling      | and thermal | cycling     |               | representative | of     |              |              |         |            |                  |      |         |
data-center load changes, redundancy operation, maintenance layout, magnetics, EMI control, protection, and thermal path
|             |               |     |            |     |       |     |     | jointly determine |        | converter | performance | [13, 136].        |     |     |
| ----------- | ------------- | --- | ---------- | --- | ----- | --- | --- | ----------------- | ------ | --------- | ----------- | ----------------- | --- | --- |
| events, and | environmental |     | excursions |     | [38]. |     |     |                   |        |           |             |                   |     |     |
|             |               |     |            |     |       |     |     | 1) Select         | stages |           | according   | to loss mechanism |     | and |
C. Long-Term High-Voltage and Integrated Architectures processed power. GaN should be prioritized where switching,
Long-term deployment is associated with more substantial output-capacitance, reverse-conduction, or commutation losses
changes in data-center power architecture, including higher- constituteameaningfulpartoftotalconverterloss.Theabsolute
|         |                  |     |         |           |             |     |          | infrastructure | benefit |     | also depends | on the fraction | of  | rack or |
| ------- | ---------------- | --- | ------- | --------- | ----------- | --- | -------- | -------------- | ------- | --- | ------------ | --------------- | --- | ------- |
| voltage | DC distribution, |     | greater | converter | modularity, |     | bidirec- |                |         |     |              |                 |     |         |
tional energy interfaces, solid-state protection, and increased facilityloadservedbythestage.Afront-endstagemayprovide
integration of power stages with rack- and board-level loads high aggregate leverage because it processes an entire power
[135]. These architectures may alter both the voltage class and shelf or rack, not simply because it appears earlier in the
| functional           | requirements |     | imposed   | on GaN    | devices. |     |          | conversion  | chain. |           |           |                  |     |        |
| -------------------- | ------------ | --- | --------- | --------- | -------- | --- | -------- | ----------- | ------ | --------- | --------- | ---------------- | --- | ------ |
|                      |              |     |           |           |          |     |          | 2) Optimize |        | switching | frequency | at the converter |     | level. |
| Several-hundred-volt |              |     | DC buses, | including | ±400-V   |     | and 800- |             |        |           |           |                  |     |        |
V-class concepts, are being considered as possible methods The switching frequency should minimize total system loss
for reducing distribution current, conductor mass, and busbar and volume rather than semiconductor switching loss alone.
loss as rack power increases. Such architectures also create Device loss, magnetic core and winding loss, capacitor loss,
additional requirements for insulation coordination, DC fault gate-drive power, EMI-filter volume, and cooling requirements
|               |            |     |              |          |            |     |           | should be | evaluated | together. |     |     |     |     |
| ------------- | ---------- | --- | ------------ | -------- | ---------- | --- | --------- | --------- | --------- | --------- | --- | --- | --- | --- |
| interruption, | protection |     | selectivity, | galvanic | isolation, |     | and local |           |           |           |     |     |     |     |
high-ratio conversion. Their deployment should therefore be 3) Specify package and layout limits quantitatively.
treatedasprospectiveratherthanasanestablishedreplacement Targetsshouldbeestablishedforcommutation-loopinductance,
for 48-V rack distribution. gate-loop inductance, common-source inductance, switch-node
Higher distribution voltages may increase the relevance capacitance, and thermal impedance. These quantities should
of vertical GaN devices, advanced edge termination, mono- be verified using extraction, impedance measurement, double-
lithic bidirectional switches, and series-connected modular pulse testing, or converter-level waveform analysis [137]. The
conversion. However, blocking voltage alone is not sufficient package must be treated as part of the electrical and thermal
to justify adoption. Native-substrate quality, defect density, circuit rather than as a mechanical enclosure.

Fig.9. System-levelGaNconverterdesignworkflowshowingthecouplingamongdeviceselection,packageandinterconnectparasitics,PCBlayout,gatedrive
andprotection,EMImanagement,magneticdesign,andthermalpathways.Converterefficiency,powerdensity,waveformquality,compliance,andreliability
emergefromthecombineddesignratherthanfromthesemiconductordevicealone.
4) Maintain gate-drive and protection margins. Gate E. Deployment Decision Framework
| voltage,           | drain-voltage |            | overshoot,           | reverse-conduction |                | interval,       |             |                 |                |                  |              |                         |            |              |
| ------------------ | ------------- | ---------- | -------------------- | ------------------ | -------------- | --------------- | ----------- | --------------- | -------------- | ---------------- | ------------ | ----------------------- | ---------- | ------------ |
|                    |               |            |                      |                    |                |                 |             | A practical     | deployment     | decision         |              | should                  | compare    | the mea-     |
| and peak           | current       | should     | be verified          |                    | over device    | tolerance,      |             |                 |                |                  |              |                         |            |              |
|                    |               |            |                      |                    |                |                 | surable     | system          | benefit        | against          | the          | implementation          |            | penalties    |
| temperature,       | load,         | and        | parasitic            | variation.         | Protection     | thresholds      |             |                 |                |                  |              |                         |            |              |
|                    |               |            |                      |                    |                |                 | introduced  |                 | by the         | new technology.  |              | GaN adoption            |            | is justified |
| and response       | times         | should     | be selected          |                    | for the        | fault withstand |             |                 |                |                  |              |                         |            |              |
|                    |               |            |                      |                    |                |                 | when        | reductions      |                | in semiconductor |              | loss, passive-component |            |              |
| capability         | of the        | specific   | GaN architecture     |                    | [59].          |                 |             |                 |                |                  |              |                         |            |              |
|                    |               |            |                      |                    |                |                 | volume,     | distribution    |                | loss,            | and cooling  | burden                  | outweigh   | the          |
|                    |               |            |                      |                    |                |                 | additional  |                 | requirements   | for              | packaging,   | gate                    | drive, EMI | control,     |
| 5) Co-design       |               | EMI        | and efficiency.      |                    | Switching-edge | control         |             |                 |                |                  |              |                         |            |              |
|                    |               |            |                      |                    |                |                 | protection, |                 | qualification, | and              | supply-chain | management.             |            |              |
| should balance     |               | transition | loss against         |                    | common-mode    | current,        |             |                 |                |                  |              |                         |            |              |
|                    |               |            |                      |                    |                |                 |             | This comparison |                | can be           | expressed    | conceptually            |            | as           |
| ringing,           | overshoot,    | and        | filter requirements. |                    | EMI            | testing should  |             |                 |                |                  |              |                         |            |              |
| use representative |               | magnetics, |                      | cables,            | grounding,     | enclosure       |             |                 |                |                  |              |                         |            |              |
geometry,andcoolinghardwarebecauselaboratoryopen-bench ∆B =∆B +∆B +∆B
|           |     |               |     |       |           |             |     | system |     | efficiency       |     | density       | thermal | (24) |
| --------- | --- | ------------- | --- | ----- | --------- | ----------- | --- | ------ | --- | ---------------- | --- | ------------- | ------- | ---- |
| waveforms | may | not reproduce | the | final | emissions | environment |     |        |     |                  |     |               |         |      |
|           |     |               |     |       |           |             |     |        |     | − ∆C integration | −∆C | qualification |         | ,    |
[138].
|     |     |     |     |     |     |     |     | where the | benefit | terms represent |     | improvements |     | in conver- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | --------------- | --- | ------------ | --- | ---------- |
6) Evaluate partial-load and transient performance. sion efficiency, power density, and thermal burden, while the
|                 |     |          |              |     |              |          | cost | terms | represent | additional | integration |     | and qualification |     |
| --------------- | --- | -------- | ------------ | --- | ------------ | -------- | ---- | ----- | --------- | ---------- | ----------- | --- | ----------------- | --- |
| Peak efficiency |     | alone is | insufficient | for | continuously | operated |      |       |           |            |             |     |                   |     |
data-center infrastructure. Converter efficiency, temperature, requirements.Thequantitiesneednotshareacommonphysical
regulation, and current sharing should be characterized across unit at the initial screening stage, but a final deployment
theexpectedloaddistribution,redundancystate,andaccelerator decision should translate them into total cost of ownership,
transient profile. energy consumption, rack capacity, failure risk, or another
|     |     |     |     |     |     |     | system-level |     | objective. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
7) Qualify the complete mission profile. Static-bias Accordingly, the recommended pathway is heterogeneous
life testing should be supplemented by repetitive switching, rather than universal: mature lateral GaN in near-term high-
reverse conduction, thermal cycling, power cycling, surge, frequency stages, tighter device–package–driver integration in
startup,shutdown,overload,andfault-recoverytests.Switching- mid-term high-density conversion, and vertical, bidirectional,
reliability guidance for GaN power devices should be applied or highly integrated GaN only where their manufacturing
together with converter-specific stress analysis [138]. and qualification maturity supports the required infrastructure

Fig. 10. Qualitative matrix of deployment-limiting challenges for GaN data-center power conversion. Rows identify device, packaging, qualification,
benchmarking,andsupply-chainconstraints,whilecolumnsrepresentrepresentativestagesofthedata-centerpowerchain.Thefirstletterineachcelldenotes
estimatedseverity(H:high,M:medium,L:low),andtheseconddenotesmitigationmaturity(T:availabletoday,N:requiringnear-termdevelopment,L:
requiringlonger-termresearch).Cellshadingrepresentsseverityonly.Theclassificationsindicaterelativeresearchpriorityandshouldnotbeinterpretedas
quantitativefailureprobabilities.
reliability. These guidelines translate the material and device under realistic switching conditions [38, 6]. Trapped charge in
advantages developed in Sections II and III into a practical surface,barrier,buffer,orinterfacestatescanincreasedynamic
deployment framework for next-generation AI data centers. on-resistance, produce current collapse, and alter threshold
|     |     |     |     | voltage after | high-voltage | off-state stress. | The resulting | loss |
| --- | --- | --- | --- | ------------- | ------------ | ----------------- | ------------- | ---- |
VIII. OPENCHALLENGESANDRESEARCHGAPS
increasemaynotbeapparentfromstaticdatasheetvalues,yetit
Despite substantial progress in GaN materials, device ar- can raise junction temperature and change converter efficiency
|                         |               |                 |         | during repetitive | operation | [38]. |     |     |
| ----------------------- | ------------- | --------------- | ------- | ----------------- | --------- | ----- | --- | --- |
| chitectures, packaging, | and converter | demonstrations, | several |                   |           |       |     |     |
coupled barriers continue to limit fleet-scale deployment in A central interpretation challenge is that reversible trapping
mission-critical data centers [22, 139]. These barriers extend andpermanentdegradationcanoccursimultaneously.Dynamic
beyond intrinsic device physics and arise from interactions R DS(on) may partially recover after the stress is removed,
among switching stress, package parasitics, electrothermal while defect generation, gate degradation, or package aging
|                         |              |                     |          | may produce | cumulative | changes. Measurements |     | taken after |
| ----------------------- | ------------ | ------------------- | -------- | ----------- | ---------- | --------------------- | --- | ----------- |
| behavior, manufacturing | variability, | and the reliability | require- |             |            |                       |     |             |
ments of continuous operation [140, 37]. Resolving them different recovery delays can therefore yield substantially
requiresmeasurementandqualificationmethodsthatreproduce different results even for the same device and stress condition.
converter mission profiles rather than relying only on static Comparisons among published studies are further complicated
device ratings or best-case laboratory operating points. by differences in drain-voltage stress, switching waveform,
|                       |            |               |            | temperature, | duty cycle, | current level, | measurement | aperture, |
| --------------------- | ---------- | ------------- | ---------- | ------------ | ----------- | -------------- | ----------- | --------- |
| Fig. 10 qualitatively | summarizes | the principal | deployment |              |             |                |             |           |
constraintsacrossrepresentativestagesofthedata-centerpower and preconditioning.
chain. The matrix distinguishes the estimated severity of each Normally-off devices introduce additional stability concerns.
barrier from the maturity of available mitigation approaches. Inp-GaNgateHEMTs,carrierinjectionanddefectdynamicsin
It should be interpreted as a research-priority map rather than the gate region can modify gate current and threshold voltage
as a quantitative failure-risk assessment. during positive gate-bias stress [22]. Extracted V th values can
|     |     |     |     | also depend | on the measurement | method, | sweep | direction, |
| --- | --- | --- | --- | ----------- | ------------------ | ------- | ----- | ---------- |
A. Switching-Stress Reliability: Dynamic On-Resistance, Trap- delay time, and prior bias history. A reported threshold shift
| ping, and Gate Stability |     |     |     |                |                  |        |                     |     |
| ------------------------ | --- | --- | --- | -------------- | ---------------- | ------ | ------------------- | --- |
|                          |     |     |     | must therefore | be distinguished | from a | measurement-induced |     |
Charge trapping and field-driven degradation remain central transient or reversible charge redistribution.
reliability concerns for lateral GaN power HEMTs operated Three research priorities follow from these limitations. First,

dynamic R protocols should specify the off-state stress evidence appropriate for mission-critical systems. Until those
DS(on)
voltage, switching waveform, junction temperature, stress requirements are met, vertical GaN should be treated as a
duration, recovery delay, and measurement aperture. Second, high-potential but emerging platform rather than as a mature
threshold-voltage and gate-current measurements should use replacement for established high-voltage technologies.
| controlled     | preconditioning    |        | and separate  | reversible |                | instability |                      |          |     |          |             |         |     |             |
| -------------- | ------------------ | ------ | ------------- | ---------- | -------------- | ----------- | -------------------- | -------- | --- | -------- | ----------- | ------- | --- | ----------- |
|                |                    |        |               |            |                |             | C. Packaging-Limited |          |     | Scaling: | Parasitics, | Thermal |     | Interfaces, |
| from permanent | aging.             | Third, | device-level  |            | stress results | should      |                      |          |     |          |             |         |     |             |
|                |                    |        |               |            |                |             | and Cycling          | Wear-Out |     |          |             |         |     |             |
| be connected   | to converter-level |        | consequences, |            | including      | addi-       |                      |          |     |          |             |         |     |             |
tional conduction loss, temperature rise, current-sharing error, Packaging often determines whether the intrinsic switching
and control-margin reduction. capability of GaN produces lower converter loss or instead
Structure-levelapproachesthatreducegateleakage,stabilize produces excessive overshoot, ringing, false turn-on, and EMI
the threshold voltage, and suppress trapping remain important [147, 148]. Common-source inductance, gate-loop inductance,
|                     |     |                         |     |     |             |           | power-loop | inductance, |     | and | package | capacitance |     | influence |
| ------------------- | --- | ----------------------- | --- | --- | ----------- | --------- | ---------- | ----------- | --- | --- | ------- | ----------- | --- | --------- |
| research directions |     | [6]. Switching-oriented |     |     | reliability | guidance, |            |             |     |     |         |             |     |           |
including JEDEC JEP180.01, also reinforces the need to switching energy and voltage stress. The resulting behavior
supplement conventional qualification with application-relevant depends on the complete commutation path, including the
dynamic testing [141, 142, 143]. The unresolved deployment transistor package, driver placement, PCB layout, decoupling
question is not simply whether a device passes a static network, and magnetic-component connections [147].
|                |     |         |               |     |            |        | Thermal | behavior |     | presents | a parallel |     | limitation. | High- |
| -------------- | --- | ------- | ------------- | --- | ---------- | ------ | ------- | -------- | --- | -------- | ---------- | --- | ----------- | ----- |
| lifetime test, | but | whether | its switching |     | parameters | remain |         |          |     |          |            |     |             |       |
sufficiently stable throughout the expected converter mission frequency GaN converters may reduce total loss while concen-
profile [142, 144, 143, 145]. tratingtheremainingdissipationintoasmallerdieandpackage
|     |     |     |     |     |     |     | area. Junction |     | temperature | is therefore |     | governed | by  | local heat |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | ------------ | --- | -------- | --- | ---------- |
B. High-VoltageandVerticalGaN:FieldManagement,Rugged-
|     |     |     |     |     |     |     | flux and | the stability |     | of the full | thermal | path | rather | than by |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | --- | ----------- | ------- | ---- | ------ | ------- |
ness, and Edge Termination efficiency alone. Die attach, substrate metallization, direct-
Vertical GaN offers a potential pathway toward higher bonded-copper structures, interface materials, PCB vias, heat
blocking voltage and improved voltage-area scaling, but spreaders, and cold plates can each become lifetime-limiting
| its deployment | introduces |     | additional | high-field |     | and process- | interfaces. |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | ---------- | ---------- | --- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
integration challenges [9, 146]. In trench-gate devices, electric- Thermal-cycling studies of low-inductance GaN modules
field crowding near dielectric corners can accelerate dielectric haveshownthatpackagedegradationcanappearasanincrease
degradation or cause premature breakdown during off-state in thermal resistance, including delamination and interface
operation [146]. Field plates, buried field shields, optimized deterioration that may not be detected through switching-
| trench geometry, | and | dielectric-stack |     | engineering |     | can reduce |          |            |     |              |      |         |     |          |
| ---------------- | --- | ---------------- | --- | ----------- | --- | ---------- | -------- | ---------- | --- | ------------ | ---- | ------- | --- | -------- |
|                  |     |                  |     |             |     |            | waveform | monitoring |     | alone [149]. | This | creates | a   | need for |
peak field, but their effectiveness depends strongly on dimen- coupled electrical, thermal, and mechanical diagnostics. Useful
sional tolerances, interface quality, charge distribution, and indicators include thermal-impedance evolution, structure-
process reproducibility. function analysis, transient thermal response, switching-energy
Edge termination is similarly critical in high-voltage vertical drift, and post-stress imaging or failure analysis.
| diodes and | transistors | [9]. | The active | region | may | support | a   |     |     |     |     |     |     |     |
| ---------- | ----------- | ---- | ---------- | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Futurepackageresearchshouldthereforetargetsimultaneous
high theoretical breakdown field, while the practical device reductions in electrical parasitics and thermal impedance while
fails at a substantially lower voltage because of field crowding preservingmanufacturabilityandcyclinglifetime.Qualification
at the die perimeter, implantation damage, surface charge, or should reproduce both rapid electrical transients and slower
crystallographic defects. Termination effectiveness must there- thermal-mechanical cycling. Package comparisons should also
| fore be evaluated | together |     | with leakage | stability, |     | temperature |            |         |     |           |           |           |     |          |
| ----------------- | -------- | --- | ------------ | ---------- | --- | ----------- | ---------- | ------- | --- | --------- | --------- | --------- | --- | -------- |
|                   |          |     |              |            |     |             | report the | cooling |     | boundary, | interface | material, |     | mounting |
dependence, process variability, and long-duration high-field pressure, substrate configuration, and measured parasitics so
stress [146]. that device-level advantages can be separated from package-
| Furtherresearchisrequiredinthreeareas.First,high-voltage |     |     |     |     |     |     | level effects. |     |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
structures need termination and dielectric-protection designs A further challenge is balancing integration with lifecycle
thatremaineffectiveacrossrealisticfabricationtolerancesrather performance. Advanced modules may reduce operating loss
than only at an optimized nominal geometry. Second, reported and cooling demand, but excessive material complexity, low
breakdown voltage should be accompanied by leakage-current assembly yield, difficult repair, or package-driven wear-out
behavior, temperature dependence, active area, termination can weaken the overall sustainability benefit [7]. Package
dimensions, and statistical device-to-device variation. Third, optimization must therefore include lifetime, repairability, and
ruggedness metrics—including surge response, repetitive over- manufacturing yield in addition to switching performance.
| voltage, fault | behavior, | and        | short-circuit | tolerance—must |              | be  |                  |     |             |     |                  |     |            |     |
| -------------- | --------- | ---------- | ------------- | -------------- | ------------ | --- | ---------------- | --- | ----------- | --- | ---------------- | --- | ---------- | --- |
|                |           |            |               |                |              |     | D. Manufacturing |     | Variability |     | and Supply-Chain |     | Resilience |     |
| characterized  | under     | conditions | relevant      | to             | high-voltage | DC  |                  |     |             |     |                  |     |            |     |
distribution and infrastructure converters. Large-scale GaN deployment depends on stable access to
The principal deployment gap is therefore the transition substrate materials, epitaxial capacity, foundry processes, pack-
from isolated high-voltage demonstrations to manufacturable, age assembly, and upstream critical materials. Public supply
yield-robust devices with package insulation and qualification assessments indicate substantial geographic concentration in

parts of the gallium and compound-semiconductor value chain efficiency was measured at nominal, peak, or thermally sta-
[150]. This concentration can expose converter programs to bilized operation and whether auxiliary, gate-drive, fan, and
price volatility, export controls, long qualification cycles, and control power were included.
limited second-source options. A standardized benchmark for data-center GaN converters
For mission-critical data centers, second sourcing cannot be should therefore include:
| based only     | on  | nominal voltage |     | and current | ratings.  | Devices  |     |        |          |            |          |       |           |        |
| -------------- | --- | --------------- | --- | ----------- | --------- | -------- | --- | ------ | -------- | ---------- | -------- | ----- | --------- | ------ |
|                |     |                 |     |             |           |          |     | 1) the | fraction | of rack or | facility | power | processed | by the |
| from different |     | suppliers       | may | differ in   | threshold | voltage, |     | stage; |          |            |          |       |           |        |
gate-voltage margin, output capacitance, reverse-conduction 2) complete efficiency curves over the expected load and
| behavior, | dynamic | R      | , package | inductance, |     | and thermal |     |             |        |     |     |     |     |     |
| --------- | ------- | ------ | --------- | ----------- | --- | ----------- | --- | ----------- | ------ | --- | --- | --- | --- | --- |
|           |         | DS(on) |           |             |     |             |     | temperature | range; |     |     |     |     |     |
impedance. Substituting a nominally equivalent device may 3) semiconductor, magnetic, interconnect, and auxiliary loss
| therefore | require | changes in | gate | drive, dead | time, | overcurrent |     |     |     |     |     |     |     |     |
| --------- | ------- | ---------- | ---- | ----------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
breakdowns;
protection, EMI filtering, and cooling. 4) extracted or measured package and commutation-loop
| Research    | and         | manufacturing | priorities     |         | include    | qualification |     | parasitics; |          |            |     |                |     |             |
| ----------- | ----------- | ------------- | -------------- | ------- | ---------- | ------------- | --- | ----------- | -------- | ---------- | --- | -------------- | --- | ----------- |
| of multiple | substrate   | and wafer     | sources,       | process |            | flows compat- |     |             |          |            |     |                |     |             |
|             |             |               |                |         |            |               |     | 5) thermal  | boundary | conditions |     | and stabilized |     | device tem- |
| ible with   | high-volume | Si            | manufacturing, |         | and device | designs       |     | peratures;  |          |            |     |                |     |             |
tolerant of substrate and epitaxial variability [105]. Statistical 6) conducted and radiated EMI results or defined pre-
reporting of wafer-level uniformity, dynamic behavior, yield, compliance conditions; and
and reliability distribution would also improve the ability to 7) mission-profile reliability testing under representative
| assess supply-chain |     | substitutability. |     |     |     |     |     |           |     |         |         |     |     |     |
| ------------------- | --- | ----------------- | --- | --- | --- | --- | --- | --------- | --- | ------- | ------- | --- | --- | --- |
|                     |     |                   |     |     |     |     |     | switching | and | cycling | stress. |     |     |     |
Lifecycle claims require similar transparency. Process- Such reporting would allow device, package, and topology
specificcradle-to-gateinventories,package-materialdata,equip-
|     |     |     |     |     |     |     |     | improvements | to  | be compared | on  | a common | converter-level |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | --- | -------- | --------------- | --- |
ment lifetime, and end-of-life recovery assumptions remain basis rather than through isolated best-case metrics.
| limited. | Better | data are required |     | to determine | whether |     | opera- |     |     |     |     |     |     |     |
| -------- | ------ | ----------------- | --- | ------------ | ------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
tional energy savings offset the embodied burden of advanced F. Priority Research Directions
substrates and packages [55]. The resulting research need is a Themostimportantresearchgapsclusteraroundfivecoupled
combined technical and supply-chain qualification framework objectives: switching-stress stability, high-field ruggedness of
| that evaluates |     | electrical equivalence, |     | reliability |     | equivalence, |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------------------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
verticaldevices,packageelectrothermallifetime,manufacturing
manufacturing continuity, and lifecycle burden. and supply-chain reproducibility, and standardized converter
|                 |     |               |     |      |     |     |     | benchmarking. | These      | categories | and      | their | stage-specific | impli- |
| --------------- | --- | ------------- | --- | ---- | --- | --- | --- | ------------- | ---------- | ---------- | -------- | ----- | -------------- | ------ |
| E. Benchmarking |     | and Reporting |     | Gaps |     |     |     |               |            |            |          |       |                |        |
|                 |     |               |     |      |     |     |     | cations are   | summarized | in         | Fig. 10. |       |                |        |
Published GaN results are difficult to compare when device Near-term research should prioritize standardized dynamic-
| and converter | metrics | are reported |     | under inconsistent |     | operating |     |           |              |                   |     |     |                   |     |
| ------------- | ------- | ------------ | --- | ------------------ | --- | --------- | --- | --------- | ------------ | ----------------- | --- | --- | ----------------- | --- |
|               |         |              |     |                    |     |           |     | parameter | measurement, | package-parasitic |     |     | characterization, |     |
conditions. Device studies may emphasize minimum static mission-profile qualification, and comparable converter report-
| R   | , low switching | energy, | or  | maximum | breakdown |     | volt- |     |     |     |     |     |     |     |
| --- | --------------- | ------- | --- | ------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
DS(on) ing. Mid-term research should target integrated electrothermal
age,whileinfrastructuredeploymentdependsonefficiencyand
|     |     |     |     |     |     |     |     | package | design, | stable normally-off |     | gate | structures, | multi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------------------- | --- | ---- | ----------- | ------ |
stabilityacrossload,temperature,switchingfrequency,cooling, source process qualification, and partial-load optimization.
| EMI, and | transient | conditions. | Review | literature |     | continues | to  |             |          |      |           |                |     |           |
| -------- | --------- | ----------- | ------ | ---------- | --- | --------- | --- | ----------- | -------- | ---- | --------- | -------------- | --- | --------- |
|          |           |             |        |            |     |           |     | Longer-term | research | must | establish | manufacturable |     | vertical- |
identifydynamicR DS(on) ,gatedegradation,andelectrothermal GaN structures, high-voltage package insulation, bidirectional
accumulationascentralbarriersrequiringimproveddefect-level and protection functionality, and process-specific lifecycle
| and system-level |     | understanding | [38]. |     |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inventories.
At the device level, useful reporting should include voltage Addressing these gaps is necessary to move GaN from
| and current | waveforms, | junction |     | or case | temperature, | gate | re- |            |           |               |     |                |     |            |
| ----------- | ---------- | -------- | --- | ------- | ------------ | ---- | --- | ---------- | --------- | ------------- | --- | -------------- | --- | ---------- |
|             |            |          |     |         |              |      |     | successful | component | and converter |     | demonstrations |     | to repeat- |
sistance, loop inductance, switching speed, reverse-conduction able deployment across large data-center fleets. The decisive
interval, dead time, and the timing used to extract dynamic criterion is not whether GaN can achieve a record efficiency
| parameters. | At  | the converter | level, | reports | should | specify |     |                  |     |            |         |     |          |         |
| ----------- | --- | ------------- | ------ | ------- | ------ | ------- | --- | ---------------- | --- | ---------- | ------- | --- | -------- | ------- |
|             |     |               |        |         |        |         |     | at one operating |     | point, but | whether | the | complete | device– |
topology, device part number and voltage class, switching package–converter system can sustain its electrical, thermal,
| mode, switching |     | frequency, | magnetic | design, |     | package | and |                 |            |            |     |               |     |           |
| --------------- | --- | ---------- | -------- | ------- | --- | ------- | --- | --------------- | ---------- | ---------- | --- | ------------- | --- | --------- |
|                 |     |            |          |         |     |         |     | and reliability | advantages | throughout |     | manufacturing |     | variation |
layout, cooling boundary, peak and full-load efficiency, partial- and the intended service life.
| load efficiency, |     | power density, | EMI | conditions, | and | protection |     |     |     |                |     |     |     |     |
| ---------------- | --- | -------------- | --- | ----------- | --- | ---------- | --- | --- | --- | -------------- | --- | --- | --- | --- |
| strategy.        |     |                |     |             |     |            |     |     |     | IX. CONCLUSION |     |     |     |     |
Reliability studies should report the complete stress wave- Gallium nitride provides a broad device and converter
form and distinguish among reversible trapping, parametric design space for addressing the increasing efficiency, power-
drift, catastrophic failure, and package degradation. Where density, and thermal demands of AI data-center power delivery.
accelerated lifetime models are used, the assumed failure Its value, however, is stage dependent rather than universal.
mechanism and acceleration law should be stated explicitly. CommerciallymaturelateralGaNHEMTsareparticularlywell
Converter studies should also identify whether demonstrated suited to high-frequency PFC, resonant isolated DC/DC, and

intermediate-busconversion,whereswitchingandcommutation [6] M. Meneghini, C. De Santi, I. Abid, M. Buffolo,
losses strongly influence converter performance. Specialized M. Cioni, R. A. Khadar, L. Nela, N. Zagni, A. Chini,
and hybrid architectures extend this capability to normally-off F. Medjdoub et al., “Gan-based power devices: Physics,
control, bidirectional power flow, extreme conversion ratios, reliability,andperspectives,”JournalofAppliedPhysics,
and functional integration. Vertical GaN offers a potential vol. 130, no. 18, 2021.
pathway toward higher-voltage and higher-power conversion, [7] R.T.Yadlapalli,A.Kotapati,R.Kandipati,S.R.Balusu,
but its deployment remains dependent on continued progress andC.S.Koritala,“Advancementsinenergyefficientgan
in substrate availability, edge termination, dielectric protection, power devices and power modules for electric vehicle
packaging, and infrastructure-grade qualification. applications: A review,” International Journal of Energy
At the system level, GaN performance cannot be inferred Research, vol. 45, no. 9, pp. 12638–12664, 2021.
from material properties or device figures of merit alone. [8] M. Meneghini, O. Hilt, J. Wuerfl, and G. Meneghesso,
Converter benefit emerges from coordinated selection of the “Technology and reliability of normally-off gan hemts
device architecture, topology, switching frequency, package, with p-type gate,” Energies, vol. 10, no. 2, p. 153, 2017.
gate drive, magnetics, layout, protection, EMI strategy, and [9] C. Langpoklakpam, A.-C. Liu, Y.-K. Hsiao, C.-H. Lin,
thermalboundary.Whentheseelementsareco-optimized,GaN and H.-C. Kuo, “Vertical gan mosfet power devices,”
can reduce conversion loss, increase volumetric power density, Micromachines, vol. 14, no. 10, p. 1937, 2023.
and lower the heat generated within the power-delivery chain. [10] C. Gupta and S. S. Pasayat, “Vertical gan and vertical
The associated facility-energy and operational-carbon benefit ga2o3 power transistors: status and challenges,” physica
depends on the magnitude of the efficiency improvement, the status solidi (a), vol. 219, no. 7, p. 2100659, 2022.
fraction of rack power processed by the affected stage, con- [11] N. K. Jaiswal and V. Ramakrishnan, “An optimized
verter utilization, cooling-system performance, and grid carbon vertical gan parallel split gate trench mosfet device
intensity. GaN should therefore be regarded as an enabling structure for improved switching performance,” IEEE
technology for lower-energy and lower-carbon operation rather access, vol. 11, pp. 46998–47006, 2023.
than as a device substitution that independently guarantees a [12] S.S.AlharbiandM.Matin,“Experimentalevaluationof
fixed reduction in PUE or emissions. medium-voltage cascode gallium nitride (gan) devices
The principal requirement for broader deployment is no for bidirectional dc-dc converters,” CES Transactions
longer the demonstration of isolated peak-efficiency records, on Electrical Machines and Systems, vol. 5, no. 3, pp.
but the achievement of repeatable device–package–converter 232–248, 2021.
performance under realistic mission profiles, manufacturing [13] P.J.ChrzanandP.B.Derkacz,“Ganpowertransistorsin
variation, and long service life. Progress is particularly needed converter design techniques,” Energies, vol. 18, no. 11,
in switching-stress stability, dynamic R characterization, p. 2890, 2025.
DS(on)
gate reliability, high-field ruggedness of vertical devices, [14] H.Matsunami,“Fundamentalresearchonsemiconductor
package electrothermal lifetime, multi-source manufacturing sic and its applications to power electronics,” Proceed-
qualification, and standardized converter benchmarking. Ad- ings of the Japan Academy, Series B, vol. 96, no. 7, pp.
dressing these challenges through coordinated device, packag- 235–254, 2020.
ing, converter, and infrastructure development will determine [15] T. Ayalew, “Sic semiconductor devices technology,
whether GaN becomes a foundational technology for efficient, modelingandsimulation,”Ph.D.dissertation,Technische
high-density, and reliable AI data-center power systems. Universität Wien, 2004.
[16] K. Matocha, “Challenges in sic power mosfet design,”
REFERENCES
Solid-State Electronics, vol. 52, no. 10, pp. 1631–1635,
[1] K. N. K. C. Sunkara, “Power consumption and heat 2008.
dissipation in ai data centers: A comparative analysis,” [17] H. Zhang, M. Nie, Q. Dong, H. Liu, P. Jia, Z. Li,
2025. and Y. Fang, “Applicability analysis of high-voltage
[2] Y. Li and Y. Li, “Ai load dynamics–a power electronics transmission and substation equipment based on silicon
perspective,” arXiv preprint arXiv:2502.01647, 2025. carbide devices,” Micromachines, vol. 16, no. 11, p.
[3] Y. Zhang and J. Liu, “Prediction of overall energy 1192, 2025.
consumption of data centers in different locations,” [18] D. Cittanti, E. Vico, and I. R. Bojoi, “New fom-
Sensors, vol. 22, no. 10, p. 3704, 2022. based performance evaluation of 600/650 v sic and gan
[4] O. S. Chaudhary, M. Denaï, S. S. Refaat, and G. Pis- semiconductors for next-generation ev drives,” IEEE
sanidis, “Technology and applications of wide bandgap Access, vol. 10, pp. 51693–51707, 2022.
semiconductormaterials:currentstateandfuturetrends,” [19] H. Dai, T. Song, and H. Du, “Study on the grinding
Energies, vol. 16, no. 18, p. 6689, 2023. mechanism of single-crystal gan based on atomic scale
[5] S. Musumeci and V. Barba, “Gallium nitride power and stress field modeling,” Materials Science in Semi-
devices in power electronics applications: State of art conductor Processing, vol. 204, p. 110313, 2026.
and perspectives,” Energies, vol. 16, no. 9, p. 3894, [20] S. S. H. Rafin, R. Ahmed, M. A. Haque, M. K. Hossain,
2023. M.A.Haque,andO.A.Mohammed,“Powerelectronics

revolutionized: A comprehensive analysis of emerging gan-based trench mosfets on 4-inch free standing gan
wide and ultrawide bandgap devices,” Micromachines, wafer,”NanoscaleResearchLetters,vol.17,no.1,p.14,
vol. 14, no. 11, p. 2045, 2023. 2022.
[21] M. Zhang and Y. Zhang, “Status and prospects of [34] Y. Duan, J. Wang, A. Xie, Z. Zhu, and P. Fay, “1.7-kv
wide bandgap semiconductor devices,” Applied and vertical gan pn diode with triple-zone graded junction
Computational Engineering, vol. 23, pp. 252–262, 2023. termination extension formed by ion-implantation,” e-
[22] N.Islam,M.F.P.Mohamed,M.F.A.J.Khan,S.Falina, Prime-Advances in Electrical Engineering, Electronics
H.Kawarada,andM.Syamsul,“Reliability,applications and Energy, vol. 6, p. 100330, 2023.
andchallengesofganhemttechnologyformodernpower [35] M. Kamin´ski, A. Taube, J. Tarenko, O. Sadowski,
devices: A review,” Crystals, vol. 12, no. 11, p. 1581, E. Brzozowski, J. Wierzbicka, M. Zadura, M. Ekielski,
2022. K. Kosiel, J. Jankowska-S´liwin´ska et al., “Vertical gan
[23] C.-T. Ma and Z.-H. Gu, “Review of gan hemt appli- trench-mosfets fabricated on ammonothermally grown
cations in power converters over 500 w,” Electronics, bulk gan substrates,” physica status solidi (a), vol. 221,
vol. 8, no. 12, p. 1401, 2019. no. 21, p. 2400077, 2024.
[24] J. Shi, “A deep dive into sic and gan power devices: [36] Y. Ma, H. Chen, S. Zhang, H. Duan, B. Hu, H. Ma,
Advances and prospects,” Appl. Comput. Eng, vol. 23, J.Rao,andC.Liu,“Lowleakagefully-verticalgan-on-si
no. 1, pp. 230–237, 2023. power mosfets,” Applied Physics Letters, vol. 127, no. 5,
[25] D. Kinzer, “Advancing gan power ics: Efficiency, relia- 2025.
bility & autonomy,” in 2022 24th European Conference [37] Z. Wang, J. Nan, Z. Tian, P. Liu, Y. Wu, and J. Zhang,
on Power Electronics and Applications (EPE’22 ECCE “Review on main gate characteristics of p-type gan
Europe). IEEE, 2022, pp. 1–2. gate high-electron-mobility transistors,” Micromachines,
[26] A. Udabe, I. Baraia-Etxaburu, and D. G. Diez, “Gallium vol. 15, no. 1, p. 80, 2023.
nitride power devices: a state of the art review,” IEEE [38] J. P. Kozak, R. Zhang, M. Porter, Q. Song, J. Liu,
Access, vol. 11, pp. 48628–48650, 2023. B. Wang, R. Wang, W. Saito, and Y. Zhang, “Stability,
[27] P. Boschee, “Comments: Grabbing the brass ring to reliability, and robustness of gan power devices: A re-
power the demand for data centers and generative ai,” view,” IEEE Transactions on Power Electronics, vol. 38,
Journal of Petroleum Technology, vol. 76, no. 05, pp. no. 7, pp. 8442–8471, 2023.
8–9, 2024. [39] S. Rahman, H. Shehada, and I. A. Khan, “Review of
[28] S. Shankar, “Enhancing energy efficiency in ai-powered isolated dc-dc converters for applications in data center
data centers: Challenges and solutions,” Marine Biology power delivery,” in 2023 IEEE Texas Power and Energy
Research at Bahamas, p. 93, 2024. Conference (TPEC). IEEE, 2023, pp. 1–6.
[29] H.-Q. Nguyen, T. Nguyen, P. Tanner, T.-K. Nguyen, [40] Open Compute Project, “Open rack v3 it gear
A. R. M. Foisal, J. Fastier-Wooller, T.-H. Nguyen, H.-P. 48v input connector, rev. 1.6,” Open Compute
Phan, N.-T. Nguyen, and D. V. Dao, “Piezotronic effect Project, Technical Specification Rev. 1.6, Sep. 2022,
in a normally off p-gan/algan/gan hemt toward highly published 29 September 2022. [Online]. Available:
sensitive pressure sensor,” Applied Physics Letters, vol. https://bit.ly/40N0xKk
118, no. 24, 2021. [41] TE Connectivity, “Ocp orv3 power solutions guide,”
[30] X. Ji, A. Fariza, J. Zhao, M. Wang, J. Wang, F. Yang, TE Connectivity, Technical Guide, May 2023, guide for
J. Li, and T. Wei, “Ridge-channel algan/gan normally- Open Compute Project Open Rack V3 power solutions
off high-electron mobility transistor based on epitaxial (10 pages). [Online]. Available: https://bit.ly/3MWUakE
lateral overgrowth,” Semiconductor Science and Tech- [42] W. Yu, X. Fan, T. Wei, and Y. Xu, “A novel digital
nology, vol. 36, no. 7, p. 075003, 2021. control strategy for gan-based interleaving crm totem-
[31] Z. Chen, L. Cai, K. Niu, C. Xu, H. Lin, P. Ren, D. Sun, pole pfc,” in 2024 IEEE Energy Conversion Congress
and H. Lin, “Research on a high-threshold-voltage and Exposition (ECCE). IEEE, 2024, pp. 2831–2836.
algan/gan hemt with p-gan cap and recessed gate in [43] Infineon Technologies AG, “Gs-evb-btp-3kw-gs
combination with graded algan barrier layer: Z. chen et evaluation board technical documentation,” Infineon
al.” Journal of Electronic Materials, vol. 53, no. 5, pp. Technologies AG, Evaluation Board / Technical
2533–2543, 2024. Manual, 2024, 3 kW High-Efficiency Bridgeless
[32] S. C. Kang, H.-W. Jung, S.-J. Chang, S. M. Kim, S. K. Totem Pole PFC evaluation board (CoolGaN
Lee,B.H.Lee,H.Kim,Y.-S.Noh,S.-H.Lee,S.-I.Kim family) and supporting technical manual. [Online].
et al., “Charging effect by fluorine-treatment and recess Available: https://www.infineon.com/evaluation-board/
gate for enhancement-mode on algan/gan high electron GS-EVB-BTP-3KW-GS
mobility transistors,” Nanomaterials, vol. 10, no. 11, p. [44] A. Pozo, M. de Rooij, and M. Palma, “Wide bandgap
2116, 2020. power conversion – part 3: Isop llc converter,” Efficient
[33] W. He, J. Li, Z. Liao, F. Lin, J. Wu, B. Wang, M. Wang, Power Conversion (EPC), Technical Article, Sep. 2025,
N. Liu, H.-C. Chiu, H.-C. Kuo et al., “1.3 kv vertical published 28 September 2025 as part of Bodo’s Power

Systems series. [Online]. Available: https://epc-co.com/ [55] L. A. Yeboah, A. Abdul Malik, P. A. Oppong,
epc/portals/0/epc/documents/articles/bp_092025.pdf P. S. Acheampong, J. A. Morgan, R. A. A. Addo,
[45] M. H. Ahmed, F. C. Lee, Q. Li, M. de Rooij, and B. Williams Henyo, S. T. Taylor, W. M. Zudor, and
D. Reusch, “Gan based high-density unregulated 48 v S. Osei-Amponsah, “Wide-bandgap semiconductors:
to x v llc converters with??? 98% efficiency for future a critical analysis of gan, sic, algan, diamond, and
datacenters,”inPCIMEurope2019;InternationalExhi- ga2o3 synthesis methods, challenges, and prospective
bition and Conference for Power Electronics, Intelligent technological innovations,” Intelligent and Sustainable
Motion, Renewable Energy and Energy Management. Manufacturing, vol. 2, no. 1, p. 10011, 2025.
VDE, 2019, pp. 1–8. [56] B. Zhang, M. Zhao, P. Huang, and Q. Wang, “Optimal
[46] J. Baek, P. Wang, Y. Elasser, Y. Chen, S. Jiang, and design of gan hemt based high efficiency llc converter,”
M.Chen,“Lego-pol:A48v-1.5v300amerged-two-stage Energy Reports, vol. 8, pp. 1181–1190, 2022.
hybrid converter for ultra-high-current microprocessors,” [57] G. Han, J. Kim, S. Park, and W. Bae, “Thermal
in 2020 IEEE Applied Power Electronics Conference management of wide-bandgap power semiconductors:
and Exposition (APEC). IEEE, 2020, pp. 490–497. Strategies and challenges in sic and gan power devices,”
[47] A.Shehabi,A.Newkirk,S.J.Smith,A.Hubbard,N.Lei, Electronics, vol. 14, no. 21, p. 4193, 2025.
M. A. B. Siddik, B. Holecek, J. Koomey, E. Masanet, [58] V. Heumesser, J.-S. Lai, H.-C. Hsieh, J. Hsu, C.-Y.
and D. Sartor, “2024 united states data center energy Yang, E. Y. Chang, C.-Y. Liu, W.-H. Chieng, and Y.-T.
usage report,” 2024. Hsieh, “Cascode gan hemt gate driving analysis,” in
[48] Uptime Institute, “Uptime institute global data 2023 IEEE Workshop on Wide Bandgap Power Devices
center survey 2024,” Uptime Institute, Technical and Applications in Asia (WiPDA Asia). IEEE, 2023,
Report UII Keynote Report 146M, Jul. 2024, pp. 1–6.
findings highlight resiliency, sustainability, efficiency, [59] P. Bau, M. Cousineau, B. Cougo, F. Richardeau, and
staffing, cloud, and AI trends among data N. Rouger, “Cmos active gate driver for closed-loop
center owners and operators. [Online]. Available: dv/dt control of gan transistors,” IEEE Transactions on
https://datacenter.uptimeinstitute.com/rs/711-RIA-145/ Power Electronics, vol. 35, no. 12, pp. 13322–13332,
images/2024.GlobalDataCenterSurvey.Report.pdf 2020.
[49] ASHRAE Technical Committee 9.9, “Data Center [60] H. Bu and Y. Cho, “Gan-based matrix converter design
Power Equipment Thermal Guidelines and Best with output filters for motor friendly drive system,”
Practices,” ASHRAE, White Paper, Jun. 2016, Energies, vol. 13, no. 4, p. 971, 2020.
revised 22 June 2016; thermal guidelines for [61] C.Lu,“Designandapplicationofhigh-efficiencygallium
data center power equipment. [Online]. Available: nitride (gan)-based power electronic devices,” Applied
https://www.ashrae.org/file%20library/technical% and Computational Engineering, vol. 153, no. 1, pp.
20resources/bookstore/ashrae_tc0909_power_white_ 90–95, 2025.
paper_22_june_2016_revised.pdf [62] UniversityWafer, Inc. (n.d.) Silicon wafers.
[50] J.-Y. Lee, J.-H. Chen, and K.-Y. Lo, “Design of a gan Accessed: 2026-03-03. [Online]. Available: https:
totem-pole pfc converter using dc-link voltage control //www.universitywafer.com/silicon_wafers.html
strategy for data center applications,” IEEE Access, [63] ——. (n.d.) Gallium nitride on silicon
vol. 10, pp. 50278–50287, 2022. epitaxial wafers. Accessed: 2026-03-03. [On-
[51] N. Keshmiri, D. Wang, B. Agrawal, R. Hou, and line]. Available: https://www.universitywafer.com/
A.Emadi,“Currentstatusandfuturetrendsofganhemts gallium-nitride-on-silicon-epitaxy-wafer.html
in electrified transportation,” IEEE access, vol. 8, pp. [64] Okmetic. (n.d.) Rf gan substrate wafers for
70553–70571, 2020. gan-on-si applications. Accessed: 2026-03-03.
[52] M. Frivaldsky, J. Morgos, and R. Zelnik, “Evaluation of [Online]. Available: https://www.okmetic.com/
gan power transistor switching performance on charac- silicon-wafers/rfsi-wafers-high-resistivity-line-for-rf/
teristics of bidirectional dc-dc converter,” Elektronika ir rf-gan-substrate-wafers/
elektrotechnika, vol. 26, no. 4, pp. 18–24, 2020. [65] Navitas Semiconductor. (2025, Jul.) Navitas announces
[53] M. Faizan, X. Wang, and M. Z. Yousaf, “Design and plans for 200mm gan production with psmc. Accessed:
comparativeanalysisofanultra-highlyefficient,compact 2026-03-03.[Online].Available:https://bit.ly/4bmGOHy
half-bridge llc resonant gan converter for low-power [66] X-FAB Silicon Foundries SE. (2025, Sep.) X-fab now
applications,”Electronics,vol.12,no.13,p.2850,2023. offersgan-on-sifoundryservices.Accessed:2026-03-03.
[54] M. Buffolo, D. Favero, A. Marcuzzi, C. De Santi, [Online]. Available: https://www.xfab.com/news/details/
G. Meneghesso, E. Zanoni, and M. Meneghini, “Review article/x-fab-now-offers-gan-on-si-foundry-services
and outlook on gan and sic power devices: Industrial [67] Infineon Technologies AG. (n.d.) Gallium nitride
state-of-the-art, applications, and perspectives,” IEEE (gan) technology. Accessed: 2026-03-03. [On-
Transactions on Electron Devices, vol. 71, no. 3, pp. line]. Available: https://www.infineon.com/technology/
1344–1355, 2024. gallium-nitride-gan

[68] ——. (2024, Sep.) Infineon pioneers world’s first 300 VA, Tech. Rep. 2026, 2026, in: Mineral Commodity
mm power gallium nitride (gan) technology. Accessed: Summaries 2026. [Online]. Available: https://pubs.usgs.
2026-03-03. [Online]. Available: https://www.infineon. gov/periodicals/mcs2026/mcs2026-gallium.pdf
com/press-release/2024/infxx202409-142 [81] J. W. Moon, “The mineral industry of china,”
[69] GaNSystemsInc.,“Gs66508t:650venhancementmode U.S. Geological Survey, Reston, VA, Tech. Rep.
gan transistor datasheet, rev. 200402,” 2020, accessed: Area Reports—International, 2026, 2023 Minerals
2026-03-03. [Online]. Available: https://www.mouser. Yearbook, advance release. [Online]. Available: https:
com/datasheet/3/70/1/GS66508T-DS-Rev-200402.pdf //pubs.usgs.gov/myb/vol3/2023/myb3-2023-china.pdf
[70] Coherent Corp., “Silicon carbide (sic) materials,” [82] Cornell NanoScale Science & Technology Facility,
Coherent Corp., Datasheet, n.d., accessed: 2026-03- “Material compatibility,” https://www.cnf.cornell.edu/
03. [Online]. Available: https://www.coherent.com/ equipment/compatibility, n.d., accessed: 2026-03-03.
resources/datasheet/materials/sic-materials-ds.pdf [83] TANAKA Precious Metals, “High precision,
[71] TrendForce. (2025) Sic raw materials see a price high durability, low cost bead dishes,” https:
increase while 6-inch substrate kicks off a price war. //tanaka-preciousmetals.com/en/solution/case/case13/,
TrendForce. Accessed: 2026-03-03. [Online]. Available: n.d., accessed: 2026-03-03.
https://bit.ly/4aNZCzj [84] C. Breach, “The great debate: Copper vs.
[72] Navitas Semiconductor. (n.d.) Silicon carbide: The gold ball bonding,” Semiconductor Digest,
facts. Navitas Semiconductor. Accessed: 2026- October 2008, accessed: 2026-03-03. [Online].
03-03. [Online]. Available: https://navitassemi.com/ Available: https://sst.semiconductor-digest.com/2008/
silicon-carbide-the-facts/ 10/the-great-debate-copper-vs-gold-ball-bonding/
[73] Navistrat Analytics. (2025) Silicon carbide (sic) [85] J.Strydom,M.deRooij,andA.Lidow,“Galliumnitride
wafer market size, share and trend analysis, transistor packaging advances and thermal modeling,”
forecast 2025–2032. Navistrat Analytics. Report EDN China, pp. 1–13, 2012.
code: NA_01409. Accessed: 2026-03-03. [Online]. [86] D. Reusch and J. Strydom, “Effectively paralleling
Available: https://navistratanalytics.com/report_store/ enhancement mode gallium nitride transistors for
silicon-carbide-sic-wafer-market/ high current and high frequency applications,”
[74] H.Osada,Y.Yoshizumi,K.Uematsu,S.Minobe,F.Sato, Efficient Power Conversion Corporation (EPC),
F. Nakanisihi, Y. Yamamoto, Y. Hagi, and Y. Yabuhara, Application Note AN020, May 2013, accessed:
“Developmentofnon-core4-inchgansubstrate,”inProc. 2026-03-03. [Online]. Available: https://epc-co.com/epc/
Int. Conf. Compound Semiconductor Manufacturing portals/0/epc/documents/application-notes/AN020%
Technology, 2017, pp. 16–4. 20Effectively%20Paralleling%20Enhancement%
[75] UniversityWafer,Inc.,“Bulkgalliumnitride(gan)wafers 20Mode%20Gallium%20Nitride%20Transistors.pdf
forresearchandproduction,”n.d.,accessed:2026-03-03. [87] Texas Instruments, “Lmg3522r030-q1 650-v 30-mω gan
[Online]. Available: https://www.universitywafer.com/ fet with integrated driver, protection, and temperature
bulk-gan.html reporting,” 2024, rev. D datasheet. [Online]. Available:
[76] Sapphire-Substrate.com, “4 inch research grade 0.4 https://www.ti.com/lit/ds/symlink/lmg3522r030-q1.pdf
mm free standing gan wafer for semiconductors,” [88] Infineon Technologies AG, “Igt65r055d2 coolgan™
n.d., accessed: 2026-03-03. [Online]. Available: https: g5 650 v enhancement-mode power transistor,”
//bit.ly/4aQ1MOU 2024, datasheet, Revision 0.1. [Online]. Available:
[77] “Bulk gan substrate market growing at 10% https://www.infineon.com/assets/row/public/documents/
cagr to $100m in 2022, from 60,000 wafers 24/49/infineon-igt65r055d2-datasheet-en.pdf
in 2016,” semiconductorTODAY Compounds & [89] IDTechEx, “Die attach materials for power electronics
Advanced Silicon, vol. 12, no. 2, March/April in electric vehicles 2020–2030,” 2020, market research
2017, market focus: GaN materials. [Online]. Avail- report. [Online]. Available: https://bit.ly/4b4E3JC
able: https://www.semiconductor-today.com/features/ [90] TrendForce. (2026) Innoscience gan products break into
PDF/semiconductor-today-mar-apr-2017-bulk-gan.pdf google’s supply chain. News article. [Online]. Available:
[78] “Gallium nitride substrate costs to plummet by https://bit.ly/3OEa5F0
60 percent,” Compound Semiconductor, Nov. 2012, [91] TexasInstruments,“Achievingganproductswithlifetime
accessed: 2026-03-03. [Online]. Available: https: reliability,” Texas Instruments, White Paper SNOAA68,
//compoundsemiconductor.net/article/90117/Gallium_ Jun. 2021, accessed: 2026-03-03. [Online]. Available:
nitride_substrate_costs_to_plummet_by_60_percent https://www.ti.com/lit/wp/snoaa68/snoaa68.pdf
[79] U.S. Geological Survey, “Gallium,” U.S. Geological [92] D. Bizo, “Silicon heatwave: The looming change in
Survey, Tech. Rep., Jan. 2025, in: Mineral Commodity data center climates,” Uptime Institute Intelligence,
Summaries 2025. [Online]. Available: https://pubs.usgs. UI Intelligence Report 74, Aug. 2022, accessed:
gov/periodicals/mcs2025/mcs2025-gallium.pdf 2026-03-03. [Online]. Available: https://bit.ly/46YmzxB
[80] ——, “Gallium,” U.S. Geological Survey, Reston, [93] W. Runyon. (2023, Sep.) An industry’s journey to

system-level predictive analytics for the data center [105] Y. Zhong, J. Zhang, S. Wu, L. Jia, X. Yang, Y. Liu,
starts now. Schneider Electric. Schneider Electric Y.Zhang,andQ.Sun,“Areviewonthegan-on-sipower
Blog. Accessed: 2026-03-03. [Online]. Available: electronicdevices,”FundamentalResearch,vol.2,no.3,
https://bit.ly/4cmeWEw pp. 462–475, 2022.
[94] Y. Chen, “Statistical interpretation of life test: [106] Y. Lin, S. Chen, P. Lee, K. Lai, T. Huang, E. Y. Chang,
Comparison between mil and jedec requirements,” and H.-T. Hsu, “Gallium nitride (gan) high-electron-
Presentation, NASA Electronic Parts and Packaging mobility transistors with thick copper metallization
(NEPP) Electronics Technology Workshop (ETW), featuring a power density of 8.2 w/mm for ka-band
Jun. 2023, nASA Technical Reports Server applications,” Micromachines, vol. 11, no. 2, p. 222,
Document ID: 20230009005. Accessed: 2026-03- 2020.
03. [Online]. Available: https://nepp.nasa.gov/docs/etw/ [107] A. B. Jørgensen, S. Be˛czkowski, C. Uhrenfeldt, N. H.
2023/15-JUN-THU/1000_Chen_20230009005.pdf Petersen, S. Jørgensen, and S. Munk-Nielsen, “A fast-
[95] T. Eikenberg, “Automotive electronics reliability testing switching integrated full-bridge power module based
starts and ends with the mission profile,” Monolithic on gan ehemt devices,” IEEE Transactions on Power
PowerSystems,Tech.Rep.Article#0061,Rev.1.0,May Electronics, vol. 34, no. 3, pp. 2494–2504, 2018.
2022, accessed: 2026-03-03. [Online]. Available: https: [108] L. Wang, W. Wang, R. J. Hueting, G. Rietveld, and
//media.monolithicpower.com/mps_cms_document/2/0/ J. A. Ferreira, “Review of topside interconnections for
2020-aip-automotive-electronics-reliability-testing_r1. wide bandgap power semiconductor packaging,” IEEE
0.pdf Transactions on Power Electronics, vol. 38, no. 1, pp.
[96] M. T. N. P. de Vera, “Search for new particles at the 472–490, 2022.
ilc,” arXiv preprint arXiv:2311.00525, 2023. [109] D. Lumbreras, M. Vilella, J. Zaragoza, N. Berbel,
[97] L.-H. Hsu, Y.-Y. Lai, P.-T. Tu, C. Langpoklakpam, J. Jordà, and A. Collado, “Effect of the heat dissipation
Y.-T. Chang, Y.-W. Huang, W.-C. Lee, A.-J. Tzou, system on hard-switching gan-based power converters
Y.-J. Cheng, C.-H. Lin et al., “Development of gan for energy conversion,” Energies, vol. 14, no. 19, p.
hemts fabricated on silicon, silicon-on-insulator, and 6287, 2021.
engineeredsubstratesandtheheterogeneousintegration,” [110] A. Calzolaro, T. Mikolajick, and A. Wachowiak, “Sta-
Micromachines, vol. 12, no. 10, p. 1159, 2021. tus of aluminum oxide gate dielectric technology for
[98] N. Kaminski and O. Hilt, “Sic and gan devices–wide insulated-gate gan-based devices,” Materials, vol. 15,
bandgap is not all the same,” IET Circuits, Devices & no. 3, p. 791, 2022.
Systems, vol. 8, no. 3, pp. 227–236, 2014. [111] M. Manganelli, A. Soldati, L. Martirano, and S. Ra-
[99] A. Dadgar, “Sixteen years gan on si,” physica status makrishna, “Strategies for improving the sustainability
solidi (b), vol. 252, no. 5, pp. 1063–1068, 2015. ofdatacentersviaenergymix,energyconservation,and
[100] B. Spiridon, M. Toon, A. Hinz, S. Ghosh, S. Fairclough, circular energy,” Sustainability, vol. 13, no. 11, p. 6114,
B. Guilhabert, M. Strain, I. Watson, M. D. Dawson, 2021.
D. Wallis et al., “Method for inferring the mechanical [112] Z. Yang, J. Du, Y. Lin, Z. Du, L. Xia, Q. Zhao, and
strain of gan-on-si epitaxial layers using optical pro- X. Guan, “Increasing the energy efficiency of a data
filometry and finite element analysis,” Optical Materials center based on machine learning,” Journal of Industrial
Express, vol. 11, no. 6, pp. 1643–1655, 2021. Ecology, vol. 26, no. 1, pp. 323–335, 2022.
[101] A. Jarndal, M. A. Alim, A. Raffo, and G. Crupi, “2- [113] S. Mondal, F. B. Faruk, D. Rajbongshi, M. M. K.
mm-gate-periphery gan high electron mobility transistor Efaz, and M. M. Islam, “Geeco: Green data centers
s on sic and si substrates: A comparative analysis from for energy optimization and carbon footprint reduction,”
a small-signal standpoint,” International Journal of RF Sustainability, vol. 15, no. 21, p. 15249, 2023.
and Microwave Computer-Aided Engineering, vol. 31, [114] U. Gupta, Y. G. Kim, S. Lee, J. Tse, H.-H. S. Lee, G.-Y.
no. 6, p. e22642, 2021. Wei, D. Brooks, and C.-J. Wu, “Chasing carbon: The
[102] T. Paskova, D. A. Hanser, and K. R. Evans, “Gan elusive environmental footprint of computing,” in 2021
substrates for iii-nitride devices,” Proceedings of the IEEE International Symposium on High-Performance
IEEE, vol. 98, no. 7, pp. 1324–1338, 2009. Computer Architecture (HPCA). IEEE, 2021, pp. 854–
[103] C.-H. Huang, C.-Y. Wu, and Y.-C. Chou, “Direct 867.
growth of wafer-scale self-separated gan on reusable 2d [115] G.Fieni,R.Rouvoy,andL.Seinturier,“xpue:Extending
material substrates,” Advanced Science, vol. 11, no. 41, power usage effectiveness metrics for cloud infrastruc-
p. 2406126, 2024. tures,” IEEE Transactions on Sustainable Computing,
[104] A.-C. Liu, P.-T. Tu, C. Langpoklakpam, Y.-W. Huang, 2025.
Y.-T. Chang, A.-J. Tzou, L.-H. Hsu, C.-H. Lin, H.-C. [116] H. Liu and J. Zhai, “Carbon emission modeling for
Kuo, and E. Y. Chang, “The evolution of manufacturing high-performance computing-based ai in new power
technology for gan electronic devices,” Micromachines, systems with large-scale renewable energy integration,”
vol. 12, no. 7, p. 737, 2021. Processes, vol. 13, no. 2, p. 595, 2025.

[117] B. Li, R. Basu Roy, D. Wang, S. Samsi, V. Gadepally, [128] M. H. Ahmed, F. C. Lee, and Q. Li, “Two-stage 48-v
and D. Tiwari, “Toward sustainable hpc: Carbon foot- vrm with intermediate bus voltage optimization for data
print estimation and environmental implications of hpc centers,” IEEE Journal of Emerging and Selected Topics
systems,” in Proceedings of the international conference in Power Electronics, vol. 9, no. 1, pp. 702–715, 2020.
for high performance computing, networking, storage [129] R. Pilawa-Podgurski, “Extreme efficiency 240 vac to
and analysis, 2023, pp. 1–15. load data center power delivery topologies and control,”
[118] S. Mönch, R. Reiner, P. Waltereit, M. Basler, R. Quay, University of California, Berkeley, CA (United States),
S. Gebhardt, C. Molin, D. Bach, R. Binninger, and Tech. Rep., 2024.
K. Bartholomé, “How highly efficient power electronics [130] X. Huang, J. Yan, X. Zhou, Y. Wu, and S. Hu, “Cooling
transfershighelectrocaloricmaterialperformancetoheat technologies for internet data center in china: Principle,
pump systems: S. mönch et al.” MRS advances, vol. 8, energy efficiency, and applications,” Energies, vol. 16,
no. 15, pp. 787–796, 2023. no. 20, p. 7158, 2023.
[119] P. A. Sesotyo, T. D. Cahyono, E. Sadewa et al., “Eval- [131] Q.Chang,Y.Huang,K.Liu,X.Xu,Y.Zhao,andS.Pan,
uating of dc-dc buck-boost converter implementation “Optimizationcontrolstrategiesandevaluationmetricsof
for integrated solar photovoltaic and thermoelectric coolingsystemsindatacenters:areview,”Sustainability,
cooler system,” International Journal of Engineering vol. 16, no. 16, p. 7222, 2024.
Continuity, vol. 4, no. 1, pp. 140–172, 2025. [132] Z. Wang, F. Ye, S. Duan, X. Yuan, D. Zuo, Y. Zhang,
[120] L. Vikhor, “Modeling of thermoelectric converter char- K.Wang,andY.Li,“A3kwganhemtbasedthree-phase
acteristics: Lecture at the summer thermoelectric school, converter achieving a switching frequency of 300 khz
june 30, 2024, krakow, poland,” Journal of Thermoelec- and an efficiency of 97.06%,” IEEE Access, vol. 12, pp.
tricity, no. 3, pp. 5–22, 2024. 116442–116456, 2024.
[121] K. X. Le, M. J. Huang, N. N. Shah, C. Wilson, [133] C. Li, Q. Ma, Y. Tong, J. Wang, and P. Xu, “A survey
P. Mac Artain, R. Byrne, and N. J. Hewitt, “Techno- of conductive and radiated emi reduction techniques
economic assessment of cascade air-to-water heat pump in power electronics converters across wide-bandgap
retrofittedintoresidentialbuildingsusingexperimentally devices,” IET Power Electronics, vol. 16, no. 13, pp.
validated simulations,” Applied Energy, vol. 250, pp. 2121–2137, 2023.
633–652, 2019. [134] N. Jia, L. Xue, and H. Cui, “Mitigating emi noise in
[122] N. Ishraq and A. Mallik, “Design of a 2.5 kw four- propagation paths: Review of parasitic and coupling
level interleaved flying capacitor multilevel totem-pole effectsinpowerelectronicpackages,filters,andsystems,”
pfc converter with ac-side passive volume optimization,” IEEE Open Journal of Power Electronics, vol. 5, pp.
IEEE Open Journal of Power Electronics, vol. 5, pp. 352–368, 2024.
214–231, 2024. [135] D. Rothmund, T. Guillod, D. Bortis, and J. W. Kolar,
[123] J.Sun,H.Gui,J.Li,X.Huang,N.Strain,D.J.Costinett, “99%efficient10kvsic-based7kv/400vdctransformer
and L. M. Tolbert, “Mitigation of current distortion for for future data centers,” IEEE Journal of Emerging and
gan-based crm totem-pole pfc rectifier with zvs control,” Selected Topics in Power Electronics, vol. 7, no. 2, pp.
IEEE Open Journal of Power Electronics, vol. 2, pp. 753–767, 2018.
290–303, 2021. [136] P. Prajapati and S. Balamurugan, “Leveraging gan for
[124] A. H. Okilly and J. Baek, “Design and fabrication of an dc-dc power modules for efficient evs: A review,” IEEE
isolatedtwo-stageac–dcpowersupplywitha99.50%pf Access, vol. 11, pp. 95874–95888, 2023.
and zvs for high-power density industrial applications,” [137] B.Sun,Z.Zhang,andM.A.Andersen,“Researchofpcb
Electronics, vol. 11, no. 12, p. 1898, 2022. parasitic inductancein thegan transistor power loop,” in
[125] F. C. Lee, Q. Li, Z. Liu, Y. Yang, C. Fei, and M. Mu, 2019 IEEE Workshop on Wide Bandgap Power Devices
“Applicationofgandevicesfor1kwserverpowersupply and Applications in Asia (WiPDA Asia). IEEE, 2019,
withintegratedmagnetics,”CPSSTransactionsonpower pp. 1–5.
electronics and applications, vol. 1, no. 1, pp. 3–12, [138] P.B.Derkacz,J.-L.Schanen,P.-O.Jeannin,P.J.Chrzan,
2016. P. Musznicki, and M. Petit, “Emi mitigation of gan
[126] M. Chrysostomou, N. Christofides, S. Ioannou, and power inverter leg by local shielding techniques,” IEEE
A. Polycarpou, “Multicell power supplies for improved Transactions on Power Electronics, vol. 37, no. 10, pp.
energyefficiencyintheinformationandcommunications 11996–12004, 2022.
technology infrastructures,” Energies, vol. 14, no. 21, p. [139] H. Lavricˇ, P. Zajec, K. Drobnicˇ, A. Rihar, V. Ambrožicˇ,
7038, 2021. D. Voncˇina, and M. Nemec, “Challenges for large-scale
[127] D. Reusch, S. Biswas, and Y. Zhang, “System optimiza- deployment of wbg in power electronics,” Informacije
tion of a high power density non-isolated intermediate MIDEM, vol. 55, no. 1, pp. 3–24, 2025.
bus converter for 48 v server applications,” IEEE [140] Y. Qin, B. Albano, J. Spencer, J. S. Lundh, B. Wang,
Transactions on Industry Applications, vol. 55, no. 2, C. Buttay, M. Tadjer, C. DiMarino, and Y. Zhang,
pp. 1619–1627, 2018. “Thermal management and packaging of wide and ultra-

wide bandgap power devices: a review and perspective,”
Journal of physics D: applied physics, vol. 56, no. 9, p.
093001, 2023.
[141] JEDEC Solid State Technology Association, “Guide-
line for switching reliability evaluation procedures for
gallium nitride power conversion devices,” JEDEC
Solid State Technology Association, JEDEC Publication
JEP180.01, Jan. 2021.
[142] J. P. Kozak, R. Zhang, M. Porter, Q. Song, J. Liu,
B. Wang, R. Wang, W. Saito, and Y. Zhang, “Stability,
reliability, and robustness of GaN power devices: A re-
view,” IEEE Transactions on Power Electronics, vol. 38,
no. 7, pp. 8442–8471, Jul. 2023.
[143] M. F. Tayyab and T. Basler, “Dynamic high temperature
operating life test methodology for long-term switching
reliability of GaN power devices,” Microelectronics
Reliability, vol. 138, p. 114613, Nov. 2022.
[144] F. Rauf, M. F. Tayyab, S. Mouhoubi, M. L. Heldwein,
andG.Curatola,“Investigationofthelong-termdynamic
R variation and dynamic high temperature oper-
DS(on)
ating life test robustness of Schottky-gate and ohmic-
gate GaN HEMT with comparable stress conditions,”
Microelectronics Reliability, vol. 168, p. 115708, May
2025.
[145] C. Fan, H. Zhang, H. Liu, X. Pan, S. Yan, H. Chen,
W. Guo, L. Cai, and S. Wei, “A study on the dynamic
switching characteristics of p-GaN HEMT power de-
vices,” Micromachines, vol. 15, no. 8, p. 993, Jul. 2024.
[146] K. Mukherjee, C. De Santi, M. Borga, K. Geens,
S. You, B. Bakeroot, S. Decoutere, P. Diehle, S. Hübner,
F. Altmann et al., “Challenges and perspectives for
vertical gan-on-si trench mos reliability: From leakage
current analysis to gate stack optimization,” Materials,
vol. 14, no. 9, p. 2316, 2021.
[147] M. Wang, P. Gao, F. Shi, W. Hu, X. Wang, H. Yan, and
Y. Mei, “Advanced packaging technology of gan hemt
module for high-power and high-frequency applications:
areview,”IEEETransactionsonComponents,Packaging
andManufacturingTechnology,vol.14,no.9,pp.1537–
1550, 2024.
[148] D.Wöhrle,B.Burger,andO.Ambacher,“Powermodule
design for gan transistors enabling high switching
speedinmulti-kilowattapplications,”EnergyTechnology,
vol. 11, no. 12, p. 2300460, 2023.
[149] Z. Sun, M. Takahashi, W. Guo, S. Munk-Nielsen, and
A. B. Jørgensen, “Thermal cycling characterization of
an integrated low-inductance gan ehemt power module,”
Microelectronics Reliability, vol. 161, p. 115482, 2024.
[150] J. Wesselkaemper, A. C. Newkirk, T. P. Hendrickson,
N. Helal, P. Rao, S. J. Smith, and A. Z. Haddad,
“Enhancing supply resilience for critical materials: Case
study of gallium supply in the united states,” Resources,
Conservation and Recycling, vol. 222, p. 108436, 2025.