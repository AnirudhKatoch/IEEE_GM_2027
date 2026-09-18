Improving Efficiency, Reliability and Life-time Cost of
Data Centers Using DC Technology
Abdullah AL-Harbi Farooq Al-Jwesm Yasser Al-Howeish
Saudi Aramco Saudi Aramco Saudi Aramco
Dhahran, Saudi Arabia Dhahran, Saudi Arabia Dhahran, Saudi Arabia
Abdullah.Harbi.47@Aramco.com Farooq.Jwesm@aramco.com Yasser.Howeish@aramco.com
Abstract— With the expansion of today’s digital era, the use of for better efficiency, more balanced between reliability and
electronic equipment is increasing exponentially at home, office, cost effectiveness and more intelligence in power
and plants. The common denominator of these electronic distribution.
equipment is that they all use Direct current (DC) power
internally by converting Alternating Current (AC) power to DC
This paper will examine the current data centers AC power
power using local converters. All these converters produce
architecture and compare it with DC power architecture as a
losses, heat, and are prone to failures which in turn impact the
viable alternative to analyze the merit of such architecture
equipment efficiency, life span, and reliability. In addition, these
converters increase the cost of equipment they are powering and deployment in facing the current industry growth and
their required footprint. The issue of reliability and cost overcome its challenges. The paper will compare both
reduction is more stressing for data centers where servers, architectures against reliability, efficiency, power quality,
Uninterruptable Power Supply (UPS) systems, and IT safety and footprint aspects. After that, a cost analysis is
equipment constituting the majority of the load can be powered performed to evaluate which architecture has lower Total
directly through a DC grid. This paper presents a case study
Cost of Ownership (TCO) to achieve the right balance
that compares AC and DC technologies for powering a typical
between cost effectiveness and all other aspects.
data center and outlines the main advantages and limitations of
each technology.
II. DRIVERS OF DC POWER IN DATA CENTERS
This study will present a comparative analysis of a DC power
The current dramatic increase in data center industry and the
system against a typical AC distribution for critical datacenter
loads. It also presents a real case study of existing AC powered high demand of energy consumption created both financial
data center and compare the benefits of powering the center via and environmental challenges. Also, the integration with
DC instead of AC. Analytical reliability, safety and efficiency renewable sources together with the need of maximizing data
models are developed, and quantitative results are obtained centers power efficiency, to deliver more densities and meet
based on a set of real data. The study indicates that the DC the computing demand, put more emphasis on the
system would be more reliable, efficient and will achieve less development of a modern data centers from design and
Capex and Opex values than the AC.
operation aspects.
Keywords—AC Architectures, Reliability, Efficiency and Total
Although all data centers IT loads such as CPUs and drives
Cost of Ownership
consume DC power, such facilities are powered by AC due to
I. INTRODUCTION its simplicity of converting and transmitting power to the IT
loads. Modern power electronics devices have the same AC
The current industrial revolution and the rapid increase of the
power capability with higher efficiency and compatibility
digital economy is driving fast development in data center
with DC generated power through renewable sources.
industry as one of the cornerstones of the world economy.
This growth in data centers is putting some stresses on
DC power becomes viable option in powering data center as
several aspects of this industry. These stresses vary from
it offers many features compare to the AC such as suffers
meeting the industry energy demand, reducing environmental
lower electrical losses (inductive & capacitive currents),
impact, securing lands and services, raising the need for
allows 29% more effective voltage than AC cable of equal
cybersecurity and others.
rating, no reactive power losses, no need for reactive power
compensation, reduced number of conductors, reduced RI2
The above stressing factors create more concerns on the way
losses, reduced transmission corridors, no synchronization
that current data centers are built with. Hence, more emphasis
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:39 UTC from IEEE Xplore. Restrictions apply.

components and operations, fewer components, lower
conversion stages and less footprint required.
III. AC & DC DISTRIBUTION ARCHITECTURES
There are many AC and DC architectures in data center
industry. In this paper, the widely used AC architecture which
is illustrated in Fig. 1 will be analyzed and compared to other
DC architectures in terms of reliability, power quality, energy
efficiency, safety and footprint. In this paper’s case study,
this AC architecture will be compared to the DC one showed
in Fig.2. This is to compare in-kind architectures in order to
properly identify which architecture has an edge over the
other. Figure 3. Different Types of DC Distribution Architecture
The below AC architecture in Fig.1 is a widely used one
IV. CLOSER LOOK INTO AC & DC SYSTEM PROS AND
which has an AC UPS at 480V (or other standard distribution
CONS
voltage level) where the power will be converted twice to
In the below sections, AC & DC architectures will be
charge the battery system via DC power and supply the AC
evaluated and compared from different aspects which are
Power Distribution Units (PDU). After which the AC power
reliability, power quality, energy efficiency, safety and
will be step down to the rack level voltage. The server Power
footprint.
Supply Unit (PSU) will again lower the input voltage and
converted to DC to the IT components.
A. Reliability
The reliability of a system is its ability to perform required
function. The higher the number of series components in a
distribution path, the less the reliability in other words an
existence of single point of failure in the system will reduce
the system reliability. Also, the fewer the components needed
to perform the required function, the higher the reliability.
Figure 1. AC Distribution Architecture
These are some of the general rules of IEEE 493 [1].
Similarly, the below DC architecture in Fig.2 performs
The basic Reliability method is the reliability block diagram
exactly what mentioned above but with lower conversion and
(RBD) which looks after the series and parallel components
transforming stages and will require the server to accept DC
in the system such as UPS, battery, generator and others. The
at its input.
calculated reliability through RBD is 37.2% for AC
architecture compare to 81.5% for DC architecture [8]. This
is to get a basic idea about system reliability. However, in
data center -where there are large number of components,
different sequence of operation, existence of standby
equipment and others- a more comprehensive analysis shall
be performed such as the Monte Carlo simulation. The result
Figure 2. DC Distribution Architecture
of different studied AC and DC architectures showed that the
DC power can be delivered to the IT load via several failure rate per year in DC architecture is ranged from 20-
architectures. One of which is the High Voltage DC (HVDC) 40% less than the AC architecture [2]. Hence, this simulation
where DC power will be distributed at higher voltage level. results proved that the DC architectures -in general- have
Another architecture is to run AC all the way toward the higher reliability level than AC. It is worth mentioning that
white space and make the conversion either at the white space the reliability level gap between DC & AC will be disappear
level or at the rack level. Other architectures such as LVDC at higher redundancy level of AC architectures.
48V or 12V are also widely used in telecom industry. Fig.3
has some of the above stated DC architectures. B. Power Quality
The power quality level is of a paramount impact on data
center operations. So, power quality disturbances and system
performance shall always be studied and mitigated. There are
some common power quality disturbances that occur in AC
and DC which will not be discussed here as their impact and
mitigation are similar. So, the focus will be on what power
quality merits and issues that DC architecture has.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:39 UTC from IEEE Xplore. Restrictions apply.

The Power quality disturbance in DC architecture is the magnitude of safe operating current of DC is always
significantly less than AC as there are less harmonics, no higher than AC which makes DC safer.
unbalance loads issue, no power factor correction circuits
required and no need for synchronization circuits [3]. In E. Footprint
contrast, continuous change and switching in IT loads will
Since DC architectures have fewer components than AC, a
create ripples in the DC bus. This can be easily mitigated by
smaller physical footprint is required. This will result not
the battery system via suppling the needed current to stabilize
only in delivering more power capacity as a result of reduced
the bus voltage. Furthermore, voltage sags and DC bus
losses but also will reduce the cost of data center building and
voltage can be managed by the rectifier.
land which represent an advantage of lower TCO in DC data
centers.
C. Energy Efficiency
V. CASE STUDY. TOTAL COST OF OWNERSHIP
Efficiency and energy delivery to the IT loads are crucial
(TCO) COMPARISION FOR DC AND AC
aspects to all data centers owners. AC equipment is currently
ARCHITECTURES
achieving the highest efficiency level and can run on different
The study presents an energy efficiency analysis which has
operational mode to become even more efficient.
been conducted for an existing AC powered data center and
Nevertheless, the lower conversion stages and components in
compared against a similar-in-kind modeled DC powered
DC architectures will always be a positive aspect of DC
data center via utilizing Etap simulation software.
architectures.
The cost analysis in this paper is focused on the total cost of
Several recent industry studies that compare AC to DC
ownership which covers both the Operational Expenses
efficiency concluded that DC is more efficient than AC.
(Opex) and the Capital Expenses of the equipment (Capx).
Some indicated that DC is 10% more efficient that AC [3].
The Opex analysis has been simplified to cover only the
Other concluded that DC achieves 17% Energy Reduction
power losses as a result of the conversion stages in both AC
compared to AC and power loss is reduced by 36% in DC
and DC systems. Although cables’ losses and number of
compared to AC [7]. On the other hand, this paper indicates
conductors in DC system are less compared to AC, these
different figure, too, as detailed in the case study section. The
losses have been excluded from the study and considered
take away here is that DC is always more efficient than AC
alike due to the fact that different DC distribution
and the data center architecture and eco-system what
architectures will result in different analysis results. Also, and
basically determine by how much.
for the same reason maintenance costs were exempted. On
It’s worth mentioning that efficiency has a cascaded impact the other hand, the capex analysis covers the conversion
since it is all about the whole ecosystem not only the equipment costs and disregards the building and land cost
individual equipment. For instance, DC suffers less conductor while of course the footprint in DC is smaller than the AC.
losses than AC. This results in 1-2% higher efficiency in DC The objective of this analysis is to set a baseline mature AC
architecture [5]. Also, the higher the efficiency, the lower architecture and compare it with similar DC architecture via
heat dissipated and the resulted cooling power. Some studies eliminating the AC converters. Thus, the selected DC
concluded that about 11% efficiency gain will result in a cost architecture was the exact AC one without some conversions.
saving of about $740,000 in three years period [6].
The study analyzes the above stated AC distribution
architecture in Fig.1 as a baseline and compares it to the DC
D. Safety
distribution architecture in Fig.2. The single line diagram of
The topic of DC voltage is not new to the industry as it is
AC architecture is shown in Fig.4. It represents a tier VI data
already being used in many industries such as microgrids and
center with a redundancy level of 2(N+1). Hence, the Site
smart cities, HVDC system that interconnect different grids
electrical system consists of 13.8 kV double ended switchgear
together, telecom, railways [4], renewable, etc. Thus,
with double tie breakers, two redundant UPS sub-systems,
experience has been gained in dealing with DC systems. The
each of which contains 5 UPSS rated 0.48 kV, 750 KVA.
concern of safely interrupting DC current is presently
Each UPS sub-system deliver the load to 12 PDUs (24 PDUs
vanished by the development of power electronic devices that
in total). The studied data center has three UPS systems with
has fast interrupting capability, DC breakers technology and
total UPS number of 30 units.
Residual Circuits Breakers (RCB). However, safety concerns
are of an equal criticality for AC & DC that is why NFPA and
other industry standards classify the arcing levels and their
mitigation such as remote racking, switching and other.
In regard to personnel protection, it is important to know that
the impact of electric shock depends on current magnitude,
duration, current path and type of voltage AC or DC. Thus,
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:39 UTC from IEEE Xplore. Restrictions apply.

|     |     |     |     |     |                                                        |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------ | --- | --- |
|     |     |     |     |     | TABLE II.  SAMPLE OF LOAD FLOW ON THE SYSTEM INCOMERS  |     |     |

|             |                                                 |                     |              |                 | #   | Item                           | Value  Unit   |
| ----------- | ----------------------------------------------- | ------------------- | ------------ | --------------- | --- | ------------------------------ | ------------- |
|             |                                                 |                     |              |                 | 1   | Operation Per Day              | 24.00  hours  |
|             |                                                 |                     |              |                 | 2   | Operation Per Year             | 365.00  days  |
|             |                                                 |                     |              |                 | 3   | Lifetime of The System         | 25.00  years  |
|             | Figure 4.  AC Architecture Single Line Diagram  |                     |              |                 |     |                                |               |
|             |                                                 |                     |              |                 | 4   | Input Power                    | 2,656.00  kW  |
| The  above  | redundancy                                      | level  will result  | in           | a  single  UPS  |     |                                |               |
|             |                                                 |                     |              |                 | 5   | Cost of KWH (Average Tariffs)  | 0.13  $/kWh   |
| maximum     | loading                                         | of  25%  which      | equivalents  | to  energy      |     |                                |               |
COOLING RATIO
efficiency  of  89%  as  per  the  equipment  manufacturer  6  VI.  60  %
efficiency curve which is illustrated in Fig. 5 and validated by
the site data. Normally, the UPS will be loaded to less than  7  750KVA UPS Cost (Estimated)  600,000.00  USD
15%. However, the study has taken the efficiency of the UPS  300 kVA PDU’s Transformer Cost
|     |     |     |     |     | 8   |     | 7,500.00  USD  |
| --- | --- | --- | --- | --- | --- | --- | -------------- |
as 91% considering efficient utilization of the UPS in its eco  (Estimated)
mode and not the status quo of 2 (N+1) configuration.   9  UPS Footprint  15.21  m^2
|     |     |     |     |     | 10  | PDU Transformer Footprint  | 7.29  m^2  |
| --- | --- | --- | --- | --- | --- | -------------------------- | ---------- |

The opex which focuses only on the losses costs has been
illustrated in the below Fig. 6 and concluded that the DC
architecture is 95.22% efficient compare to 88.92 % for AC
architecture.  The losses are driven by the conversion stages
  in AC such as the inverters and PDUs transformers which are
not parts of the DC architecture. Also, this lower losses in the
|     | Figure 5.  | UPS Efficiency Curve  |     |     |     |     |     |
| --- | ---------- | --------------------- | --- | --- | --- | --- | --- |
DC architecture leads to a reduced heat dissipation and in
deed cooling requirements.
Etap software has been utilized for the load flow analysis
where the data center has been modeled in the software. The

total power consumption per single UPS system is 2.656 MW
distributed between the sub-systems as illustrated in Table I.

TABLE I. SAMPLE OF LOAD FLOW ON THE SYSTEM INCOMERS

|            | MW       | Mvar     |               | S      |     |     |     |
| ---------- | -------- | -------- | ------------- | ------ | --- | --- | --- |
| Bus ID     |          |          | P+jQ          |        |     |     |     |
|            | Loading  | Loading  |               | (MVA)  |     |     |     |
| INCOMER_A  | 1.327    | 0.683    | 1.327+0.683i  | 1.492  |     |     |     |
| INCOMER_B  | 1.329    | 0.683    | 1.329+0.683i  | 1.494  |     |     |     |

|     |     |     |     |     | Figure 6.  | AC & DC Systems Losses Comparison  |     |
| --- | --- | --- | --- | --- | ---------- | ---------------------------------- | --- |
The study parameters are described in the below Table II. It’s
worth mentioning that the $/KWH cost as based on average  By converting these losses figures to $ value, the total cost of
tariff in the region, cooling ratio represents the cooling power  losses of AC and DC architectures are listed in Fig.7. Thus,
|     |     |     |     |     | total cost saving in  | DC due to better efficiency and less  |     |
| --- | --- | --- | --- | --- | --------------------- | ------------------------------------- | --- |
requirements to remove the heat, UPS and PDU Transformer
costs are comprehensive estimated cost based on combined  conversions is $7,586,421. For comprehensive and specific
suppliers’ and data centers owners’ inputs.  DC architecture, the saving will be much higher due to lower
cabling losses and maintenance costs.

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:39 UTC from IEEE Xplore.  Restrictions apply.

  One  of  the  challenges  is  the  high  maturity  level  and
significant gained experience of data centers personnel in
  dealing  with  AC  architectures.  This  helps  achieve  high
|     |     |     |     |     |     |     | availability  | and reliability levels in which all data center  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------------------ | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     | owners  | strive      | to  sustain.  | All   | directives  | toward  | achieving     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------------- | ----- | ----------- | ------- | ------------- |
|     |     |     |     |     |     |     | higher  | efficiency  | levels        | were  | focused     | on      | data  center  |

components where several advancements to the AC electrical
|     |     |     |     |     |     |     | and mechanical equipment accomplished and indeed resulted  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
in higher efficiencies of the whole ecosystem. However, the
  calls for reducing energy consumption and the limitation in
energy delivery are more stressing these days due to the

previously stated drivers toward DC power.
|     | Figure 7.  | AC & DC Systems Opex Comparison  |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
On the other hand, there are several barriers that delay DC
The capex cost analysis is illustrated in the below Fig. 8. The  architectures deployments such as lack of such DC inclusion
costs are associated with the UPSs and PDUs transformers for  in  data  center  standards,  Lack  of  DC  ecosystems
classifications and redundancy level and the majority of IT
the AC and the Rectifiers in DC. Thus, the total cost saving in
DC due to less capex is $4,134,000. The capex in DC is  load accepts only AC power and convert it to DC.
expected to be lower due to the elimination of the inverters
Challenges are always there and a collaboration between data
and PDUs’ Transformers. In other DC configurations the
center industry owners, manufacturers, designers, consultants
| saving  | will  be  | even  | more.  | The  more  | elimination  |     | of  |     |     |     |     |     |     |
| ------- | --------- | ----- | ------ | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
and governors is a must to overcome all challenges toward
components the higher the saving.
such transformation and help data center industry meeting the
|     |     |     |     |     |     |     | future demands.   |              |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |   VIII.           | CONCLUSION   |     |     |     |     |     |
The DC architectures in data center is emerging with several

demonstration sites and the deployments in other industry.
|     |     |     |     |     |     |     | The represented benefits and cost saving of DC over AC in  |     |     |     |                               |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
|     |     |     |     |     |     |     | this paper are key areas of                                |     |     |     | focus and such analysis will  |     |     |
continue to rationalize the transformation. As stated in this
     paper, many studies have listed some benefits and figures of
DC data center from all aspects such as safety, reliability,
|     | Figure 8.  | AC & DC Systems Capex Comparison  |     |     |     |     | efficiency and other.   |     |     |     |     |     |     |
| --- | ---------- | --------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |

| It’s  clearly  | observable  |     | that  the  | Total  | Cost  of  | Ownership  |     |     |     |     |     |     |     |
| -------------- | ----------- | --- | ---------- | ------ | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
The objective of this paper was to emphasize on the pros and
(TCO) in DC is less than the AC and the cost saving for the
cons of each architecture and most importantly to quantify the
life time of a single 2 (N+1) UPS system is $11,725,291.
|     |     |     |     |     |     |     | merits  and  | cost  | advantage  | of  | DC  architecture  |     | over  AC.  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ---------- | --- | ----------------- | --- | ---------- |
Finally, a collaboration between all data center industry chain
The cost analysis results show that DC architecture has 55%
will smooth such transformation and help boost the digital
lower TCO compared to AC architecture and this value could
economy and the industry revolution.
be higher with other hybrid or Open Compute Project (OCP)

architectures [8].
IX. REFERENCES
Another major cost saving factor is the footprint reduction in
[1]  IEEE 493-2007 - IEEE Recommended Practice for the Design of
DC architecture due to reduced conversion stages. For this
Reliable Industrial and Commercial Power Systems
| paper  study  | and  | since  | the  AC  | UPS  footprint  |     | is  15.2m2  |                                   |     |     |     |                                   |     |     |
| ------------- | ---- | ------ | -------- | --------------- | --- | ----------- | --------------------------------- | --- | --- | --- | --------------------------------- | --- | --- |
|               |      |        |          |                 |     |             | [2]  Bijen Raj Shrestha, Timothy  |     |     |     | M. Hansen and Reinaldo Tonkoski,  |     |     |
“Reliability Analysis of 380V DC Distribution in Data Centers”.
compare to DC UPS with 7.6m2 and the elimination of the
[3]  Satish Rajagopalan, Brian Fortenbery and Dennis Symanski, “Power
PDU transformer with footprint of 7.29m2. The total saving
Quality Disturbances Within DC Data Centers”.
in DC UPS footprint is about 76% of AC UPS plus the PDU.
[4]   Tilo Pueschel, “DC-Powered Office Buildings and Data Centres”.
[5]  Dustin J Becker and B.J. Sonnenberg, “DC Microgrids in Buildings and
| VII. DC ADAPTATION CHALLENGES  |     |     |     |     |     |     | Data Centers”.  |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
[6]
Subrata Mondal and Earl Keisling, “Efficient Data Center design using
Novel Modular DC UPS, Server Power supply with DC voltage and
| With  the  | current  | direction  | toward  | DC  | power  | in  | many  |     |     |     |     |     |     |
| ---------- | -------- | ---------- | ------- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
Modular CDU cooling”.
| industries,  | data  | center  | industry  | is  still  | facing  |     | several  |     |     |     |     |     |     |
| ------------ | ----- | ------- | --------- | ---------- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
[7]  Keiichi Hirose, “DC powered data center with 200 kW PV panels”
challenges to make this transformation despite all of the clear
[8]  Alexander Barthelme, Xiwen Xu and Tiefu Zhao, “A Hybrid AC and
advantages of DC architectures over AC.
DC Distribution architecture in Data Center”

Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 14,2026 at 08:52:39 UTC from IEEE Xplore.  Restrictions apply.