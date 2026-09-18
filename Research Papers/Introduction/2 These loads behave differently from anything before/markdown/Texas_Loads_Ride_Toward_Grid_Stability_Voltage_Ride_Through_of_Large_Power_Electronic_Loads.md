Introduction electronic loads (PELs) bring and the possible solu-
IMAGINE SEEING AN EMPTY FIELD DE- tions to better integrate these large loads into the
void of any infrastructure. Now imagine returning electricity grid.
one year later and, instead of an empty field, there ERCOT is one of several independent system
are five incredibly large warehouses. Each is filled operators (ISOs) in the United States (Figure 1). As
floor to ceiling with thousands of computers, all the ISO for the region, ERCOT manages the flow of
humming together in a loud cacophony, busy solv- electric power to more than 27 million Texas cus-
ing cryptocurrency or maybe artificial intelligence tomers, representing about 90% of the state’s elec-
(AI) calculations. This structure maybe consumes a tric load. ERCOT’s mission is to serve the public by
massive 300 MW; many larger ones are under con- ensuring a reliable grid, efficient electricity markets,
struction. Told from the perspective of the Electric open access, and retail choice. Thus, ERCOT needs
Reliability Council of Texas (ERCOT), this article to determine the best way to manage new challenges,
explores the unique set of challenges large power whether past-to-date integration of more than 64 GW
of renewables or the ongoing integration of incred-
ibly large, rapidly developing PELs.
56 1540-7977 © 2025 IEEE. All rights reserved, including rights for text and IEEE POWER & ENERGY MAGAZINE
data mining, and training of artificial intelligence and similar technologies.
AIDEM.REBIERHCSRETEP/MOC.KCOTSRETTUHS©
FEATURE
TEXAS LOADS RIDE TOWARD
GRID STABILITY
Voltage Ride Through of Large Power Electronic Loads
José Conto , Yunzhi Cheng , Jonathan Rose , and John Schmall
Digital Object Identifier 10.1109/MPE.2025.3564963
Date of current version: 21 August 2025
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restrictions apply.

Currently, there are 57 GW of large loads, each mission studies are more likely to identify a need for
more than 75 MW, requesting interconnection to ER- transmission upgrades.
COT (Figure 2). Roughly three fourths are either data
centers or otherwise computer based. This is an almost What Are Large PELs?
unimaginably large addition to the bulk electric sys- PELs utilize switching semiconductors to process
tem, which currently has a peak load of approximately and convert electricity. Many modern loads utilize
85 GW. While it is assumed that not all will be built, power electronics for efficiency or flexibility. Be-
the rapid growth of these loads has spurred significant cause many types of loads natively require dc to
changes in the way that ERCOT plans and operates the operate, the power electronics will often include a
electric system. rectifier to convert ac power to regulated dc power.
Traditionally, the impact of load growth is as- Typical large loads, such as computer data centers,
sessed in annual and/or ad hoc studies that strictly hydrogen electrolyzers, and industrial motor drive
adhere to North American
Electric Reliability Corpora-
About ERCOT
tion (NERC) reliability stan-
dards and ERCOT transmis-
The ERCOT Interconnection is an electrical
sion planning criteria. The
island serving 85% of the Texas load.
rapid growth in large loads has More than Because it has only small ties back to the
rest of the United States and Mexico, load
led to a push for faster inter- 27 Million and generation must be kept in precise
connection timelines. ERCOT Customers in the balance within the interconnection.
ERCOT Region Sufficient reserves are necessary for
established the Large Flexible unexpected events, such as a power plant
trip, wind and solar ramps, and large load
Load Task Force to identify the
ramps or trips.
measures needed to address
the operational, planning, and
(a)
market impacts of intercon-
nected large loads in the ER-
COT region.
In March 2022, through this
task force, ERCOT implement-
ed an interim process to ensure
compliance with ERCOT and
NERC requirements for large
loads wishing to interconnect
to the ERCOT system on an
accelerated timeline.
ERCOT considers any large
load as subject to the interim
U.S.
process. A 75-MW threshold is
Interconnections
used to classify whether a load
Western Interconnection ERCOT Interconnection Eastern Interconnection
is “large.” This does not corre-
Includes EI Paso and Far West Texas Includes Portions of East Texas and
Panhandle Region
spond to another requirement;
(b)
rather it is the level at which ER-
COT considers it prudent for a Figure 1. The ERCOT grid is one of three interconnections in the United States.
The ERCOT corporation functions as an ISO to manage the ERCOT grid, serving as
load to undergo a formal review
a balancing authority, planning authority, and reliability coordinator. ERCOT is one
and the threshold at which trans- of several ISOs in the United States.
AuthorSizEePdT liEcMensBeEdR u/sOe ClimTOiteBd EtoR: T2e0c2h5n ische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restric5tio7ns apply.

facilities, all utilize dc power. The first two utilize  misbehave in unexpected ways. The lack of com-
dc power directly, while the third usually incorpo- plicated feedback controls on the grid side possibly
rates dc as an intermediate stage before variable  means that rectifier-based loads can be represented
frequency inversion. In addition to rectification, a  by relatively simple, approximately algebraic models
power factor correction (PFC) circuit is also nor- in most time-domain power system stability stud-
mally needed to reduce harmonics and reactive  ies. The word “possibly” is used because this alge-
power strains and increase efficiency.  braic hypothesis has not been fully proven; additional
There are generally two broad categories of recti- laboratory testing and system event benchmarking is
fiers (Figure 3). Rectifiers have relatively simple con- necessary. (To learn more about complicated power
trols, or, in the case of the inexpensive passive diode  electronics behaving in unexpected ways on the pow-
rectifier, they may have no controls at all. This is in  er system, refer to the “Odessa Disturbance” listed in
contrast to the dc-to-ac inverters used in wind tur- the section “For Further Reading.”)
bines, solar photovoltaic, and energy storage systems,  Note that the power conversion equipment can be
which  have  complicated  phase-synchronizing  and  incorporated into a larger control system, for exam-
voltage-feedback controls that can, on rare occasions,  ple, an industrial load governed by product orders
or a cryptocurrency data cen-
57,236 ter load governed by the real-
56,736
time market price of electricity
| 50,000 | Project Status |     |     |     | relative to the monetary reward  |     |
| ------ | -------------- | --- | --- | --- | -------------------------------- | --- |
No Studies Submitted
|     |     |     | 43,820 |     | for  mathematically  | validating  |
| --- | --- | --- | ------ | --- | -------------------- | ----------- |
Under ERCOT Review
blockchain transactions.
40,000
Planning Studies Approved
|     |     |     | 36,090 |     | The dc bus ripple-smooth- |     |
| --- | --- | --- | ------ | --- | ------------------------- | --- |
Approved to Energize
| )WM( daoL |     |     |     |     | ing capacitor in Figure 3 plays  |     |
| --------- | --- | --- | --- | --- | -------------------------------- | --- |
30,000
|     |     | 26,755 |     |     | an important role in the voltage  |     |
| --- | --- | ------ | --- | --- | --------------------------------- | --- |
ride-through capability of the
| 20,000 |     |     |     |     | device, particularly in the case  |     |
| ------ | --- | --- | --- | --- | --------------------------------- | --- |
16,758
|     |     |     |     |     | of  computer  power  | supplies.  |
| --- | --- | --- | --- | --- | -------------------- | ---------- |
For economic reasons, this ca-
10,000
|     | 4,479 |     |     |     | pacitor is typically quite small,  |     |
| --- | ----- | --- | --- | --- | ---------------------------------- | --- |
2,523
only sized so that the converter
0
2022 2023 2024 2025 2026 2027 2028 2029 can ride through a momentary
In-Service Date (Cumulative)
drop in voltage (such as one
Figure 2. Actual and projected large load growth for 2022–2029 as of August 2024.   cycle, or 1/60th of a second in
Passive Diode Rectifier Active Switching Rectifier The active switching rectifier
offers improved efficiencies,
P F C  a n d
|       |               |        |       | Optional DC Out | harmonic reduction, and PFC. |     |
| ----- | ------------- | ------ | ----- | --------------- | ---------------------------- | --- |
|       | O p tio n a l | DC Out |       |                 |                              |     |
|       |               |        | AC In | Voltage         | Transistors are switched     |     |
|       | Voltage       |        |       | Regulator       |                              |     |
| AC In | Regulator     |        |       |                 | with pulse width modulation  |     |
so that sinusoidal current
PFC Smoothing Transistor Voltage Smoothing flows in phase with voltage.
| Diode Bridge | and |           |        |                     |     |     |
| ------------ | --- | --------- | ------ | ------------------- | --- | --- |
|              |     | Capacitor | Bridge | Reduction Capacitor |     |     |
Voltage Reduction
Figure 3. Two types of rectifiers commonly used in modern PELs. Both types efficiently convert ac to dc power. A detailed
understanding is not necessary for grid studies but helps justify modeling assumptions.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore.  Restrictions apply.
| 58  |     |     |     |     | IEEE POWER & ENERGY MAGAZINE |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- |

North America) without interrupting the dc output The frequency could be
and causing the computer to reboot. This is not well
affected, export stability limits
aligned with the four-to-seven cycles typically re-
could be exceeded, and a
quired for protective elements to clear a fault on
the electric grid. As a result, nearby fully loaded sudden change in flows could
data centers will likely reboot if they do not have
cause overloads or voltage
backup uninterruptible power supplies (UPSs) on
violations.
site. Many cryptocurrency data centers do not have
such UPS devices, as their work is tolerant of inter-
ruptions, while many AI and cloud computing data lightning, animal intrusion, or equipment failure,
centers do include UPS devices. for example. Time-domain simulations are per-
A typical computer power supply, such as the kind formed to simulate such disturbances and ensure
used in data centers, has additional components to that the power system returns to a stable operating
step down and regulate the final output voltage (Fig- point within acceptable tolerances.
ure 4) in addition to protection logic to shut down The integration of PELs into the electric power
should the dc output voltage exceed strict tolerances. system introduces several stability challenges that
Many other dc loads, including hydrogen electrolyzer must be studied.
facilities, may have a subset of similar components. ✔ Voltage stability: The substantial and vari-
The possibility that several massive data centers able demand from PELs can cause voltage
could reboot or switch over to UPSs at the same instability. Effective voltage regulation and
time for the same nearby grid fault, causing thou- sufficient reactive power reserves are neces-
sands of megawatts of load to momentarily disap- sary to prevent disruptions.
pear for a few minutes, has numerous reliability ✔ Frequency stability: Maintaining the grid
implications and concerns. frequency within acceptable limits is critical.
The addition of large PELs can complicate
Power System Stability frequency management, requiring advanced
control strategies and sufficient reserves.
Introduction to Power System ✔ Loss of load events: Operational processes,
Stability Studies such as procedures for the procurement of ad-
A variety of disturbances can impact the perfor- ditional reserves or postdisturbance operating
mance of a power system. Large voltage distur- plans, must be in place to cope with potential
bances, called faults, involve electricity being tem- overvoltage and/or overfrequency when PELs
porarily shorted to ground and may be caused by are suddenly removed from the grid.
Mains Transistor Regulated
Supply Input Rectifier Bridge Switch High-Frequency Output Rectifier dc Output
(Refer to Figure 3) (dc) (dc to (ac) Transformer (ac) and Filter
High-Frequency ac)
(ac) (dc)
(Actual topology may vary.) Controller Voltage Measurement
(Voltage Regulation and
Protection)
Figure 4. Topology of a typical ac-to-dc converter, such as those used in computer power supplies. The size of the
capacitors within the rectifiers generally determines the voltage disturbance ride-through capability.
AuthorSizEePdT liEcMensBeEdR u/sOe ClimTOiteBd EtoR: T2e0c2h5n ische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restric5tio9ns apply.

tions are based on ERCOT’s understanding of the
load functioning rather than on information di-
rectly relayed by load customers. Direct informa-
tion would be superior, but ERCOT has observed
PEL customers having substantial difficulty ob-
taining useful information from their equipment
suppliers—perhaps because the large PEL indus-
try is still relatively new, and only recently were
these devices installed in such large quantities
The accuracy of power system studies depends that one needed to be concerned about possible
heavily on the collective accuracy of the input mod- grid impacts.
els. Unfortunately, the precise characteristics of
large loads are often not well known when facilities A PEL Model for Power System Studies
are in the planning phase. Of special importance It is common to model electronic loads—particu-
is whether the load under study, along with nearby larly data centers—as constant-power loads down
loads, will trip for a given event. To address the to the voltage trip point. Computer power supplies
tripping uncertainty, ERCOT requires running load and similar voltage-regulated ac-to-dc converters
trip sensitivities when they are perceived to have an contain fast regulation circuits that will compen-
impact on stability. For the load modeling issue, re- sate for grid disturbances, allowing the dc load to
search groups have provided broad starting points be unaffected by moderate grid events. This effec-
for certain categories of load, which can be modi- tively decouples the computer from many grid dy-
fied by the load customer based on available data to namics and reinforces constant-power operation. In
conservatively account for unknowns. While these the event of more severe dips, the device will shut
measures provide a workable stopgap, a better un- down to avoid damage. Computers generally ad-
derstanding of site-specific load characteristics is here to the Information Technology Industry Coun-
very much needed. cil (ITIC) curve (Figure 5) for uninterrupted op-
The next several paragraphs discuss possible eration. Most faults on the electric grid are cleared
modeling assumptions for PELs. These assump- when protection elements detect and remove faulted
equipment, typically in four to
seven cycles (1 cycle = 1/60th
Voltage Ride-Through Region of a second). This means that
the ITIC curve specifies unin-
terrupted operation only if the
supply voltage remains above
70%. The voltage could be
much lower near the fault as
power is temporarily sourced
to ground. This could poten-
tially lead to interruption at
nearby PELs and even PELs
more than 100 miles away.
Data centers are made up of
thousands of such computers.
For the most part, the single-
load model can be scaled up.
60 IEEE POWER & ENERGY MAGAZINE
egatloV
lanimoN
fo
tnecreP
If many large loads in an
area were to behave similarly,
their tripping could cause
voltage excursions and power
imbalance between generation
and load.
140
120
110
100
90
80
70
No-Damage Region
40
0
0.001 c 0.01 c 1 c 10 c 100 c Steady
1 us 1 ms3 ms 20 ms 0.5 s 10 s
State
Duration in Cycles (c) and Seconds (s)
Figure 5. The ITIC curve for computers and other IT equipment. Although tech-
nically not a ride-through requirement, computer power supplies are generally
designed to successfully ride through the low-voltage portion without interrup-
tion. A compliant computer running at full load will generally survive one cycle
at 0 V without rebooting. For a typical transmission fault cleared in four to
seven cycles, the voltage at the computer’s electrical outlet must be above 70%
to avoid a reboot.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restrictions apply.

 However, the trip threshold will be higher because  a rural part of the ERCOT system, including one
of the voltage drop in the facility power distribution  three-phase fault due to a circuit breaker failure.
wiring. The voltage drop tends to increase under  The event induced a 1,600-MW load reduction.
low voltages because of the increased current flow  Loads that tripped during this event included data
necessary to serve a constant-power load. Thus, a  centers, oil/gas pumping facilities, and other in-
70% voltage trip threshold at the computers may  dustrial facilities that were unable to ride through
correspond to a 75% or higher voltage at the point  the  extended  low-voltage  period.  Additionally,
of grid interconnection. some generation was lost, including two thermal
Figure 6 is a suggested data center load model  generators totaling 112 MW. As a result of the loss
adapted from the Electric Power Research Institute  of load, the system frequency spiked to 60.235 Hz
electronic load model. The percentages of each  and returned to 60 Hz in 12 min, 30 s. Figure 7
type of load can be customized by input from the  shows the system frequency spike response, and
facility owner. Figure 8 shows the voltage d ropping to almost half
Further work is still needed to improve load mod- of its nominal value at a nearby 345-kV station for
| els. The constant-power model does not consider  |     |     |     | this event. |     |     |     |
| ------------------------------------------------ | --- | --- | --- | ----------- | --- | --- | --- |
electromagnetic effects like harmonic and subsyn-
chronous interaction. Power losses and the effect of
voltage drop within the facility are not well quanti-
At <75% voltage,
| fied. Some facilities will consume additional power  |     |     |     | the breaker |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- |
opens.
|     |     |     |     |     |     | ~   | ~   |
| --- | --- | --- | --- | --- | --- | --- | --- |
once the voltage recovers as motors speed back up
and dc capacitors and batteries recharge. Some non-
|     |     |     |     |     | Three-Phase Fan | Air-Conditioning  |     |
| --- | --- | --- | --- | --- | --------------- | ----------------- | --- |
|     |     |     |     |     | Motors          | Load (If Present) |     |
computer PEL loads may not exhibit constant-power  Constant-Power
|                 |               |                        |     | Electronic      | (Many cryptocurrency facilities           |     |     |
| --------------- | ------------- | ---------------------- | --- | --------------- | ----------------------------------------- | --- | --- |
| behavior.  UPS  | systems  may  | introduce  additional  |     |                 |                                           |     |     |
|                 |               |                        |     | (Computer) Load | are air cooled without air-conditioning.) |     |     |
characteristics, altering the dynamic performance.
Figure 6. Example equivalent stability model for a
The Voltage Ride-Through Problem typical data center in grid stability studies.
Self-disconnection of a single
load may not have much im-
pact on the system; however,  High-Speed Frequency Recorder Data
60.3
| the  simultaneous  | disconnec- |     |     |     |     |     |     |
| ------------------ | ---------- | --- | --- | --- | --- | --- | --- |
tion of hundreds or even thou-
60.25
sands of megawatts of large
| loads in an area could pose a  |     | 60.2 |     |     |     |     |     |
| ------------------------------ | --- | ---- | --- | --- | --- | --- | --- |
risk to reliability. The frequen-
)zH( ycneuqerF
60.15
cy could be affected, export
stability limits could be ex-
60.1
ceeded, and a sudden change
in flows could cause overloads
60.05
or voltage violations.
60
An Actual Loss of
| Load Event |     | 59.95           |                 |                 |                 |                 |         |
| ---------- | --- | --------------- | --------------- | --------------- | --------------- | --------------- | ------- |
|            |     | 3:49:24 3:49:32 | 3:49:41 3:49:49 | 3:49:58 3:50:07 | 3:50:15 3:50:24 | 3:50:33 3:50:41 | 3:50:50 |
At 3:50 a.m. on 7 December  Date and Time (mm/dd/yy hh:mm:ss)
2022, multiple related faults
occurred on 138-kV lines in  Figure 7. System frequency: loss of load event on 7 December 2022.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore.  Restrictions apply.
| SEPTEMBER/OCTOBER 2025  |     |     |     |     |     |     | 61  |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- |

While the event did not result in any substan- a known specific limit, called the generic trans-
tially negative impacts, the sensitivity of large mission limit. Integrating PELs behind a GTC can
loads to voltage disturbances raised concerns. If significantly impact the generic transmission limit.
many large loads in an area were to behave simi- The addition of large loads without an adequate
larly, their tripping could cause voltage excursions voltage ride-through capability presents significant
and power imbalance between generation and challenges in managing this constraint. For exam-
load, and lead to frequency excursions and other ple, large loads have expressed interest in locating
operational problems. behind such stability constraints where electricity
prices may be lower. Adding a load here permits
Case Study: Impact of Large PELs on the dispatch of additional generation because some
Grid Stability generation will be absorbed locally, and the stabil-
Increased renewable development has caused ity limit will be preserved. This works until a trans-
stability constraints to appear in ERCOT’s rich mission fault causes a line to trip and the large load
renewable resource areas. Because electrical in- trips as well due to the brief voltage drop. In this
stability can evolve very quickly, operators must case, the stability limit could be e xceeded, sending
take action ahead of time, meaning that system the area into oscillations or other instability.
operators will constrain operating conditions in This challenging situation is illustrated in Fig-
preparation for the next unplanned contingency. ure 9. The simplest management approach currently
To manage this situation and other similar ones on being implemented will reduce the stability limit by
the ERCOT grid, ERCOT uses generic transmis- an amount needed to preserve stability whenever a
sion constraints (GTCs) to manage stability, volt- load without assured ride-through capability is add-
age, and other constraints that cannot be directly ed behind a generation export GTC. This is not the
modeled in ERCOT’s online steady-state power most efficient outcome as adding a 500-MW load
flow and contingency analysis applications. A without ride-through capability could result in re-
GTC is a tool that ERCOT operators use to geo- ducing up to 500 MW of generation on the system
graphically constrain the transmission flow on under certain scenarios.
one or more defined interfaces (selected trans-
mission elements determined by a study) to avoid Improving the Ride Through of PELs
unstable operating conditions. Stability is main- ERCOT implemented a low-voltage ride-through
tained by limiting the GTC interface flow below standard for renewable generation in 2009. Imple-
menting a similar standard for
load remains challenging be-
cause most load equipment and
facilities were not designed
considering their impacts on
the grid. Just as the renewable
ride-through standard required
some innovation to design
wind turbines and solar invert-
ers, a similar innovation will
be required for large loads.
While efforts to implement
ride-through standards for load
has been met with hesitancy
from industry, ERCOT has
62 IEEE POWER & ENERGY MAGAZINE
0
1.2
1.1
1
0.9
0.8
0.7
0.6
0.5
0.4
72.0 35.0 8.0 70.1 33.1 6.1 78.1 31.2 4.2 76.2 39.2 2.3 74.3 37.3
Time (s; . Offset From 3:49 a.m.)
).u.p(
cV
4 72.4 35.4 8.4 70.5 33.5 6.5 78.5 31.6 4.6 76.6 39.6
Figure 8. Voltage at nearby 345-kV station: fault and loss of load event on 7
December 2022.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restrictions apply.

been making progress engaging research and indus- Operators must take action
try partners. Additionally, ERCOT has proposed a
ahead of time, meaning
standard that limits the maximum amount of load
that system operators will
that can be lost for a single credible planning event
to maintain frequency stability (refer to the ERCOT constrain operating conditions
Reliability Performance Criteria for Loss of Load
in preparation for the next
in the section “For Further Reading”).
unplanned contingency.
One significant challenge to overcome when
considering how to improve the ride through of
large loads—particularly large PELs—is the down- modulating the load power proportional to volt-
stream process that the PEL is driving. Consider a age, the load changes from a constant-power load
motor driving an industrial process or a computer to more like a constant impedance. As the grid
running important software code. If the power is voltage drops, power reduces, and voltage recov-
interrupted, a lengthy restart process may be need- ery becomes much easier. A new IEEE standard,
ed. It may be several minutes before the load ramps “Recommended Practice for System Stability of
back to the predisturbance value. Thus, the best as- AC Power Converters in Data Centers” (IEEE
surance seems to involve a method that avoids pro- Standard P3380), appears to be working on a
cess interruption to begin with. But how can this be similar goal.
accomplished for a load of several hundred mega-
watts in size? Figure 10 illustrates some options the Impact of Load Ramp Rates
authors have gathered from research institutions; PELs can exhibit very high ramp rates, from 0%
however, we are not experts in this field, and further to 100% consumption power in less than a second.
collaboration is needed. Too high a ramping rate could create problems
Critical loads often employ a UPS—essentially, with overloads, voltages, and frequency stability.
a battery backup inverter system that picks up the This may especially be a concern when a large
load when the power fails. While this keeps the pro- number of PELs ramp according to a common sig-
cess running, it does not necessarily keep the load nal, such as the price of electricity. It may become
on the grid as many UPS systems are programmed necessary to implement ramp rate restrictions for
to delay switching back until
a period of observation deter-
Stability Interface
mines acceptable grid integrity.
Generation Export Rest of ERCOT
While the period of observation Region Flow
is typically tens of seconds, the
Large Load A contingency (fault on the transmission line causing it to trip),
good news is that UPS systems could have a compounding impact on the remaining line if the
load simultaneously trips causing increased exports.
are very programmable, per-
haps providing a unique op- The voltage sensitivity of this load may cause it to trip for the nearby
transmission fault. Losing load with the tie line would further strain the
portunity for the facility owner weakened interface.
to coordinate with the utility
Figure 9. Example of a counterintuitive situation in which loss of a new large load
operator.
can negatively impact and worsen an existing stability constraint. Here, two trans-
Idea 2 of Figure 10 is appeal- mission lines connect a generation export region to demand in the rest of ERCOT.
To avoid instability, the flow through the interface must be constrained below a
ing in that the technology exists
predetermined level to avoid instability. Because generation redispatch takes time to
today and is in widespread use. implement and instability can happen very quickly, flow must be constrained precon-
Idea 3 is especially ap- tingency. In this example, adding a large load inside the export region could worsen
the stability constraint if it does not ride through. The stability interface limit may
pealing because it makes
need to be lowered as a result of the load addition because the load may trip and
PELs more grid friendly—by send an excess of generation to flow down the already-strained transmission path.
AuthorSizEePdT liEcMensBeEdR u/sOe ClimTOiteBd EtoR: T2e0c2h5n ische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restric6tio3ns apply.

very large loads. Until then, the worst-case impact Unplanned fluctuations in large PELs can com-
of load ramping can be studied by either tripping plicate the ability of transmission operators to meet
or by reconnecting large loads in planning stabil- underfrequency load-shedding obligations. For ex-
ity simulations. ample, a single PEL may represent half of the load
served by a small transmission operator. In such a
Impact on Traditional Grid Operation case, the underfrequency load-shedding obligation
and Planning for the transmission operator may double or be cut
Incorporating large PELs into the traditional grid in half as the demand from the PEL fluctuates. Ad-
introduces several challenges and necessitates ad- ditionally, the unpredictable nature of PEL demand,
justments in planning and operational strategies. particularly when aggregated, can result in sudden
The following ERCOT concerns are based on past drops or spikes in load, making it difficult to main-
experiences or those potentially occurring in the tain grid stability without rapid response mecha-
near term. nisms in place.
If several large loads fail to ride through a nearby transmission fault, the simultaneous loss of
hundreds to thousands of megawatts of load could occur. Below are some ideas for improving the
ride-through capability of PELs.
1. Add a UPS 2. Add Energy Storage
This is the most common solution for critical loads. The capacitor within the ac–dc power supply typically
However, a UPS may not transfer the load back to provides about one cycle of ride-through capability.
the grid as soon as the fault clears; many require an Adding 10 times more for fault ride through, although
observation time during which the load is theoretically possible, might be impractical. A more
incrementally switched back to utility power. elegant solution would be to add local bulk energy
However, many large UPS systems are highly storage. Large grid-scale batteries are already
programmable, perhaps pointing to further economically justified in many regions for their ability
collaboration opportunities between the utility and to provide timed energy and ancillary services
the load customer. to the grid.
3. Add Fast, Dynamic Power Management Controls 4. Bias the Facility Voltage High
If the downstream processes must run at full power Many ac–dc converters are capable of operating over a
during the fault, lots of energy storage would be wide voltage range. Perhaps the power distribution
required to prevent interruption. What if the processes network could serve power at 277 V or 480 V
were slowed down during the voltage dip? In the case instead of the typical 240 V which would provide an
of a data center, a software driver could be written additional margin for low voltages. The converter could
to throttle the computer processor in proportion to also be designed to continue operating for lower
grid voltage during the brief ~200 ms it takes voltages. Note that while this may help reduce tripping,
for the fault to clear. This would greatly reduce the it could potentially cause voltage collapse on the grid
additional dc bus storage needed to ensure ride from the increased currents required to sustain the
through, potentially making an elegant solution. load under reduced voltage.
Figure 10. Potential solutions for improving the ability of PELs to ride through low voltages and transmission faults
(further collaboration with industry is needed). Concepts originate from ERCOT discussions with large load industry
partners, the Electric Power Research Institute, and other research institutions, such as Texas A&M University.
Authorize6d 4lic ensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:I4E7E:1E3 PUOTCW fEroRm & IE EENE EXRpGlorYe .M RAesGtrAictZioInNsE apply.

Large PELs can constitute a significant portion estimate load behavior based upon surveys and sta-
of the load in certain areas. This concentration of tistical analyses of mixed and diffuse loads. These
demand can stress the local transmission infrastruc- numbers would then get plugged into standard load
ture and require substantial upgrades to accommo- models adjusted for the specific types of industry
date the load without compromising reliability. and the regional climate. While this routine works
PELs often exhibit demand profiles that differ for diffuse loads where any unique behaviors aver-
from those of traditional loads. For instance, they age out, it does not appear adequate for large loads,
may operate continuously at high power levels or which individually and collectively can have a sig-
have significant loading flexibility depending on nificant stability impact.
operational cycles and market conditions (e.g., Despite many being advertised as flexible and
cryptocurrency prices or electric market prices). price responsive, most large loads currently do not
This variability challenges traditional load forecast- register as a controllable load resource in the ER-
ing and requires more dynamic and responsive grid COT market; thus, they are treated as nondispatch-
management strategies. able in real time and likewise “firm” in planning
ERCOT has identified several key milestones for studies. This “firm” designation makes it possible
incorporating large PELs into planning cases, in- to use reliability as a justification to build transmis-
cluding the following: sion upgrades, but it also means that ERCOT may
✔ Initial interconnection request: This is used need to limit the size of the load interconnection if
to evaluate the feasibility and impact of the upgrades cannot be built in time. The Large Flex-
proposed load. ible Load Task Force has been considering potential
✔ Detailed impact studies: Thorough analyses modifications to the market rules with the intent to
are conducted to assess the effects on local encourage more large loads to register as a control-
and regional grid stability. lable load resource dispatchable resource. This could
✔ Integration planning: Strategies can be de- provide a faster path for interconnection, especially
veloped to manage and mitigate identified if the constraint is expected to occur less frequently.
impacts before the load is energized. Once a study is completed, it may determine a
A summary of ERCOT’s current guideline for need for upgrades. For example, in the case of volt-
large load studies is presented in Figure 11. age violations, it may be necessary to add dynamic
Large Load Assumptions
for Planning Studies
ERCOT’s Large Load Studies Guideline
The 75% voltage trip threshold
1.Studies should follow all applicable NERC requirements including TPL-001 and FAC-002
is being used as a placeholder as well as the ERCOT Planning Guide requirements.
until more accurate estimates 2.Large loads are generally treated as “firm,” meaning that the system must be designed or
upgraded to accommodate them. ERCOT may restrict the interconnection size of a large load
or measurements can be ob- as necessary to preserve reliability until upgrades can be completed.
3.A contingency must be run, tripping the large load under study.
tained from PEL owners. Get-
4.A load reconnection study may be required.
ting large load customers to 5.The most critical contingency(-ies) should be run with nearby PELs modeled with a high trip
threshold, such as 75% voltage, if the trip threshold was not already included in their models.
provide validated models suit-
6.If the load is inside an area with a known stability constraint, contingencies and transfers
able for transmission studies related to that stability constraint should be rerun to check whether the load has an impact.
7.Additional studies should be conducted as required (short circuit, subsynchronous oscillation
is a significant challenge that
including ferroresonance, etc.).
requires greater industry col- 8.The load model should be justified. In general, ERCOT has found customer-provided
information to be somewhat sparse, and there are still gaps in understanding. This forces
laboration. Historically, load conservative assumptions in studies.
customers have not needed
to provide such models, and
Figure 11. ERCOT’s Large Load Studies Guideline for steady-state and dynamic
transmission companies would stability studies.
AuthorSizEePdT liEcMensBeEdR u/sOe ClimTOiteBd EtoR: T2e0c2h5n ische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restric6tio5ns apply.

ERCOT collaborates extensively especially during grid disturbances, that they can
share with grid planners and operators to ensure ac-
with various stakeholders and
curate and proper modeling for system studies. PELs
research institutions to enhance
may be adaptable to utilize advanced controls that
grid reliability and address the provide a more grid-friendly performance charac-
teristic. ERCOT has started several “grid modern-
challenges posed by PELs.
ization and enhancement” initiatives for continued
research, development, collaboration, and innova-
r eactive transmission support for voltage control, such tion to address such evolving challenges and ensure
as adding static var compensators and STATCOMs. grid reliability and resilience (Figure 12).
Grid Modernization Initiatives Collaboration With Stakeholders and
The old paradigm of loads being served by large, Research Institutions
central generating stations through transmission net- ERCOT collaborates extensively with various stake-
works and distribution systems is not sustainable in holders and research institutions to enhance grid re-
the future. PELs, such as data centers and cryptomin- liability and address the challenges posed by PELs:
ing sites, can be developed much faster than the infra- ✔ Stakeholder engagement: ERCOT engages
structure that is needed to serve them. Whereas elec- with market participants, utility companies,
tric systems have typically been developed to simply and regulatory bodies to gather input and align
serve loads in the past, loads in the future will gener- on strategies for grid reliability. This includes
ally need to be more integrated into system planning regular meetings of working groups, public
and operation practices. For example, mechanisms consultations, and collaborative focused plan-
for leveraging load flexibility may be able to replace a ning sessions.
need for additional infrastructure investment. ✔ Research partnerships: ERCOT has partnered
In the future, loads may incorporate battery-stor- with academic institutions to develop better
age devices (or electric vehicle charging) that may models of data center load and to research
offer opportunities to inject power into the grid. As ways to improve ride through.
a result, it will be important for load owners to have ✔ Pilot projects: ERCOT conducts pilot projects
a better understanding of their load characteristics, to test new technologies and methodologies in
real-world scenarios. These proj-
ects provide valuable insights
Managing the Grid With and data that inform broader
Uncertainty and Large Penetrations of
Variability Management Energy Storage implementation strategies across
Resources
the grid. One successful pilot
project let energy storage re-
sources participate in a fast fre-
Evolving Grid Identify and Evaluate
Ancillary Modernization Use Cases for AI and quency response program. This
Services and Machine Learning
raised the level of comfort in
Enhancement
dealing with large power unbal-
ance disturbances, for example,
Alternative Techniques when a large load trips.
for Dynamic Security
Control Capability for
Assessment and
DERs and Smart Loads Awareness
Conclusion
The integration of large loads
Figure 12. ERCOT grid modernization and enhancement initiatives. DER: distrib-
uted energy resource. into the ERCOT grid brings
Authorize6d 6lic ensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:I4E7E:1E3 PUOTCW fEroRm & IE EENE EXRpGlorYe .M RAesGtrAictZioInNsE apply.

amplified risks to reliability, resiliency, and operat- in bitcoin mining facilities in Texas,” in Proc. IEEE
ing margins. The testing of the grid performance Energy Convers. Congr. Expo. (ECCE), 2023, pp.
under multiple scenarios and contingencies be- 742–749, doi: 10.1109/ECCE53617.2023.10362562
comes a necessity when the number of large PELs P. Mitra, “Transmission planning and large
keeps increasing. This article highlights pressing datacenters [Viewpoint],” IEEE Electrific. Mag.,
problems that ERCOT faces when planning to in- vol. 11, no. 3, pp. 90–92, Sep. 2023, doi: 10.1109/
terconnect multiple large loads, particularly PELs, MELE.2023.3291509.
in a relatively short period. We list some interim “Technical reference on the composite load
processes ERCOT has implemented to handle new model,” Electric Power Res. Inst., Palo Alto, CA,
large load interconnections, some of the challenges, USA, Sep. 2020. [Online]. Available: https://
like voltage ride through and effects on existing sta- www.epri.com/research/programs/027570/results/
bility constraints, and also potential solutions, such 3002019209
as working with industry to obtain better models “Large Load Working Group,” Electric Rel.
and improve voltage ride through and dynamic volt- Council of Texas, Austin, TX, USA, 2025. [On-
age characteristics. line]. Available: https://www.ercot.com/committees/
ERCOT is committed to plan and maintain a re- tac/llwg
liable and stable grid, to provide an interconnection “LFLTF event details,” Electric Rel. Council of
process of large loads that is fair, and to apply best Texas, Austin, TX, USA, 2022. [Online]. Available:
practices and sound engineering when assessing the https://www.ercot.com/calendar/04142022-large
impact of large loads on the Texas grid. ERCOT is -flexible-load-task
working with industry and research institutions to bet- “Odessa disturbance,” NERC, Atlanta, GA, USA,
ter understand the characteristics and hence the chal- Sep. 2021. [Online]. Available: https://www.nerc.
lenges of these very large additions to the system and com/pa/rrm/ea/Documents/Odessa_Disturbance
is seeking collaboration to continue successful inter- _Report.pdf
connections while ensuring reliability. Better model- “Trending topic: Generic transmission con-
ing, improved load ride through, and better visibility straints (GTCs),” Electric Rel. Council of Texas,
in studies and operations are our continued goals. Austin, TX, USA, 2024. [Online]. Available: https://
www.ercot.com/files/docs/2024/08/09/ERCOT
Acknowledgment _Trending_Topic_GTCs.pdf
The authors would like to thank Manuel Navarro “Planning guide revision request 122, reliability
Catalan, Chris Cosway, Julie Snitman, and Agee performance criteria for loss of load,” Electric Rel.
Springer with the ERCOT Grid Interconnections Council of Texas, Austin, TX, USA, 2024. [Online].
for providing review and feedback, and they also Available: https://www.ercot.com/mktrules/issues/
thank Patrick Gravois with the Operations Analysis PGRR122#keydocs
team at ERCOT for gathering information about the
load loss event. Biographies
José Conto is with the Electric Reliability Council of
Further Reading Texas, Taylor, TX 76574 USA.
M. Bossart, R. W. Kenyon, D. Maksimovic, and Yunzhi Cheng is with the Electric Reliability
B. -M. Hodge, “The effect of power electronic loads Council of Texas, Taylor, TX 76574 USA.
on western interconnection stability,” in Proc. IEEE Jonathan Rose is with the Electric Reliability
Power Energy Soc. General Meeting (PESGM), 2020, Council of Texas, Taylor, TX 76574 USA.
pp. 1–5, doi: 10.1109/PESGM41954.2020.9281863. John Schmall is with the Electric Reliability
S. Almubarak, H. Ibrahim, D. Singhania, and Council of Texas, Taylor, TX 76574 USA.
P. Enjeti, “Energy consumption and power quality
p&e
AuthorSizEePdT liEcMensBeEdR u/sOe ClimTOiteBd EtoR: T2e0c2h5n ische Universitaet Muenchen. Downloaded on September 10,2026 at 10:47:13 UTC from IEEE Xplore. Restric6tio7ns apply.