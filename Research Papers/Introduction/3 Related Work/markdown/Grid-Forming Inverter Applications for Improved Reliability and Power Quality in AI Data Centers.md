| Grid-Forming |     |     | Inverter |       | Applications |     |     |     | for  | Improved |         |     |
| ------------ | --- | --- | -------- | ----- | ------------ | --- | --- | --- | ---- | -------- | ------- | --- |
| Reliability  |     | and |          | Power | Quality      |     | in  | AI  | Data |          | Centers |     |
Ali Azizi , Anuoluwapo Aluko, Sam Maleki, Reza Salehi, and Hasan Bayat
|     |             |                   |     |     | RMS Energy,  | ON, Canada  |                            |     |     |     |     |     |
| --- | ----------- | ----------------- | --- | --- | ------------ | ----------- | -------------------------- | --- | --- | --- | --- | --- |
|     | {ali.azizi, |                   |     |     |              |             | hasan.bayat}@rmsenergy.com |     |     |     |     |     |
|     |             | anuoluwapo.aluko, |     |     | reza.salehi, | sam.maleki, |                            |     |     |     |     |     |
Abstract—Based on the rapid growth in internet-based tech- Supplies (UPS) and specialized filtering techniques, are es-
nology and the prominence of artificial intelligence (AI), data sential, ensuring consistent power delivery and minimizing
centers are becoming a critical energy infrastructure in today’s operational risks [4].
| power system. | Their continuous,       |              | short-term, | and             | intermittent |                    |                 |              |             |                  |     |              |
| ------------- | ----------------------- | ------------ | ----------- | --------------- | ------------ | ------------------ | --------------- | ------------ | ----------- | ---------------- | --- | ------------ |
|               |                         |              |             |                 |              | Conventional       |                 | power        | quality     | improvement      |     | methods fre- |
| load profiles | lead to power           | quality      | issues      | that            | can degrade  |                    |                 |              |             |                  |     |              |
|               |                         |              |             |                 |              | quently            | rely on devices |              | like Static | Var Compensators |     | (SVCs),      |
| the network’s | reliability.            | Grid-forming |             | (GFM) inverters | have         |                    |                 |              |             |                  |     |              |
|               |                         |              |             |                 |              | Static Synchronous |                 | Compensators |             | (STATCOMs),      |     | and Dy-      |
| emerged       | as a promising solution | to           | various     | challenges      | posed by     |                    |                 |              |             |                  |     |              |
the growing integration of inverter-based resources with grid- namic Voltage Restorers (DVRs) to address issues such as
following characteristics. In this paper, we examine the impacts voltage sags, swells, and harmonic distortion. SVCs, which
ofvoltagesagandflickeronpowersystemswithAIdatacenters
|                |                     |         |          |        |           | use thyristor-controlled |           |       | reactors     | and capacitors, |              | are widely |
| -------------- | ------------------- | ------- | -------- | ------ | --------- | ------------------------ | --------- | ----- | ------------ | --------------- | ------------ | ---------- |
| as significant | loads and propose   | the     | adoption | of GFM | inverters |                          |           |       |              |                 |              |            |
|                |                     |         |          |        |           | used for                 | reactive  | power | compensation |                 | and voltage  | stabiliza- |
| to address     | these power quality | issues. |          |        |           |                          |           |       |              |                 |              |            |
|                |                     |         |          |        |           | tion, but                | they come | with  | a high       | cost            | due to their | need for   |
IndexTerms—Datacenter,flicker,grid-forminginverter,power
quality, voltage ride-through constant maintenance, high-voltage switching technology, and
|     |     |     |     |     |     | additional | harmonic | filters. | STATCOMs, |     | which | are voltage- |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | --------- | --- | ----- | ------------ |
I. INTRODUCTION source converter-based systems, offer improved dynamic per-
|     |     |     |     |     |     | formance | and faster | response | times | than | SVCs, | making them |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | ----- | ---- | ----- | ----------- |
Emerging power systems are evolving quickly, driven by highly effective for voltage support; however, their advanced
environmental goals and advances in renewable technologies, technology and power electronics components lead to high
particularly the increased integration of renewable energy installation and operational costs [5]. DVRs, on the other
| sources | and power electronics. | The | integration |     | of renewable |               |       |         |             |        |      |            |
| ------- | ---------------------- | --- | ----------- | --- | ------------ | ------------- | ----- | ------- | ----------- | ------ | ---- | ---------- |
|         |                        |     |             |     |              | hand, provide | rapid | voltage | restoration | during | sags | and swells |
resources, such as solar and wind, introduces variability and by injecting compensating voltage into the system, which
uncertainty,underminingthepredictabilityoffossil-fuel-based protectssensitiveloads.However,likeSVCsandSTATCOMs,
generation [1]. High penetration of power electronics, in- DVRs are also costly, requiring sophisticated control systems,
cluding devices like converters for wind and solar, HVDC large transformers, and regular upkeep to ensure reliable
| transmission, | and electric | vehicle | chargers, | offers | greater con- |              |       |       |           |             |         |       |
| ------------- | ------------ | ------- | --------- | ------ | ------------ | ------------ | ----- | ----- | --------- | ----------- | ------- | ----- |
|               |              |         |           |        |              | performance. | While | these | solutions | effectively | enhance | power |
trol over power flow, enhancing efficiency but also creating quality, the high initial and maintenance expenses associated
unique challenges in system stability and reliability. These witheachdeviceoftenposefinancialchallenges,especiallyfor
converter-dominatedgridsintroducelowinertia,complexelec- applications demanding large-scale or continuous compensa-
| tromagneticdynamics,andmulti-timescalecontrolinteractions |     |     |     |     |     | tion. |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
that complicate conventional stability models, which were The concept of grid-forming inverters (GFM inverters) has
designedfortraditionalsynchronousgenerators.Consequently, emerged as a powerful tool for stabilizing modern power
addressing these challenges necessitates innovative control systems, especially under high renewable penetration. Unlike
| strategies, | robust fault management, |     | and | adaptable | stability |             |                |     |       |            |       |             |
| ----------- | ------------------------ | --- | --- | --------- | --------- | ----------- | -------------- | --- | ----- | ---------- | ----- | ----------- |
|             |                          |     |     |           |           | traditional | grid-following |     | (GFL) | inverters, | which | synchronize |
frameworks to maintain reliable operation amidst an increas- to the grid’s voltage and frequency and operate as current
ingly decentralized and renewable-heavy power system [2]. sources, GFM inverters function as voltage sources with the
The rapid expansion of data centers to meet increasing capabilitytosetandmaintaintheirownvoltageandfrequency
digitaldemandshascreatedseveralchallengesrelatedtopower parameters. This voltage-source characteristic allows GFM
system integration, especially concerning power quality and inverters to operate independently of grid conditions and
energy efficiency. Data centers require stable, high-quality providecriticalsupportinscenariossuchasislandedoperation
power to support their sensitive electronic equipment, yet or weak grid conditions [6].
their high energy consumption introduces issues like voltage One of the main advantages of GFM inverters over GFL
sags, harmonic distortion, and frequent power transients [3]. inverters is their ability to offer inertia-like behavior, which
Even minor fluctuations in voltage or frequency can disrupt supports grid frequency stability and enhances voltage control
operations, causing data loss, equipment malfunction, and during disturbances, providing a level of robustness typi-
significant financial impact. To counteract these disturbances, cally associated with synchronous generators. GFM inverters,
power conditioning solutions, such as Uninterruptible Power through advanced control strategies like virtual synchronous
979-8-3315-0995-8/25/$31.00 ©2025 IEEE

SG-2 B2 T2 B7 B8 B9 T1 B1 SG-1 Grid Vault 1 Vault 1
P3 GFM-IBR
B5 B6 Vault M Vault M
P2
P1
B4 Rack 1 Rack N
GFM
T3 P, Q,V Data Center
DATA
SG-3 B3 CENTER
Fig.2. Grid-connecteddatacenterwithgrid-forminginverter
GFM-IBR
Fig. 1. IEEE 9-bus system with a grid-connected data center and a GFM
inverter. Each vault is a complex system comprising several power
converters, as shown in Fig. 2 [10]. The rectifier converts the
input AC voltage to DC; the DC-DC converter is an interface
machine (VSM) and droop control, can help mitigate fre-
between the DC bus and the battery. The inverter transforms
quency and voltage instabilities, especially in grids with low
the DC power into AC to serve the IT and mechanical loads.
inertiawhereconventionalinvertersfallshort[7].Furthermore,
The function of the battery interface is to maintain the DC
by stabilizing the voltage, GFM inverters mitigate risks asso-
link voltage within specified limits to sustain power transfer
ciated with power quality issues and protecting sensitive data
to the load for a certain period.
center equipment from outages or malfunctions [8].
When a voltage disturbance event occurs in the system and
This paper models a data center integrated with a GFM
the point of interconnection (POI) voltage is out of specified
in a 9-bus IEEE system to demonstrate its effectiveness in
limits,theloadsaredisconnectedfromthesystem.Thissudden
maintaining grid stability and power quality during faults or
disconnectionoflargeAIdatacenterloadsfurtherexacerbates
islanding. GFM inverters’ unique voltage-forming capability
the system’s reliability.
allows them to remain operational during low-voltage con-
Additionally, modern data centers have base loads (usually
ditions, providing essential support for voltage stability and
35% of the peak load) and AI loads that behave differently
reactive power, crucial for sensitive systems like data centers.
and can impact the system’s reliability. The load profile of a
Additionally, the study investigates GFM inverters’ role in
typical data center, shown in Fig. 3, can be written as:
mitigating voltage flicker and improving frequency regulation
during islanding, showcasing their advanced control strategies 
L for 0≤t<t
and inertia-like behavior. These contributions highlight the L b
+ Lpk−Lb ·(t−t ) for t ≤t<t
a
GFM’s potential to address key challenges in modern power L(t)= b tb−ta a a b (1)
sys
T
te
h
m
e
s
re
w
st
ith
of
hi
t
g
h
h
is
r
p
e
a
n
p
ew
er
ab
is
le
o
i
r
n
g
t
a
e
n
g
i
r
z
a
e
t
d
ion
a
.
s follows. Section II
 L
L
pk
+ Lb−Lpk ·(T −t )
f
f
o
o
r
r
t
t
b
≤
≤
t
t
<
<
T
t c
describes the model of elements of the system architecture
pk T−tc c c
andflickermeasurementmethodology.SectionIIIpresentsthe where L is the base load, L is the peak load, t is
b pk a
simulation setup and discusses the results. Section IV con- durationoftherisingedge,t isthetimetoreachpeakload,t
b c
cludes the findings, highlighting the role of GFM-controlled is time for the falling edge, and T is the period of the signal.
battery energy storage systems (BESSs) in enhancing power Thisperiodicbehaviorofthedatacenteratvaryingfrequencies
quality and system reliability in AI-driven data centers. can lead to another power quality issue known as flicker in
the system, thereby compromising the system’s reliability. It
II. SYSTEMARCHITECTUREANDFLICKER
becomes imperative that modern data centers comply with
MEASUREMENTMETHODOLOGY
IEEE 1453-2022.
Appropriate models need to be developed to investigate the
impacts of voltage disturbances on data centers. In this sec-
tion, the system architecture used for simulation is presented.
L(t)
The schematic is shown in Fig. 1. It depicts the IEEE 9- 32 ms 32 ms
L
bus system [9], representing a typical interconnected power pk
network,adatacenter,andaGFM-basedBESS.Thefollowing
subsections provide a detailed description of the data center
and GFM inverter modeling.
L
b
A. Data Center Modeling 100 ms 736 ms
A typical grid-connected data center exhibits GFL char- t a t b t c T 2T t
acteristics, consisting of multiple racks ranging from tens
to hundreds, and each rack has multiple vaults (hundreds). Fig.3. PeriodicloadprofileofatypicalAI-baseddatacenter
979-8-3315-0995-8/25/$31.00 ©2025 IEEE

|     |     |     |     |     |     |     |     | Similarly, | reactive   |          | power   | droop   | control   | operates | based on   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------- | ------- | ------- | --------- | -------- | ---------- |
|     |     |     |     |     |     |     | the | linear     | dependency |          | between | voltage | magnitude |          | (V) at the |
|     |     |     |     |     |     |     | POI | and        | the        | reactive | power   | (Q)     | managed   | by the   | inverter,  |
LPF
|     |     |     |     |     |     |     | illustrated |     | in Fig. | 4(b). | The | reactive | power | droop equation | is: |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ----- | --- | -------- | ----- | -------------- | --- |
|     |     |     | (a) |     |     |     |             |     |         | V =V  | −k  | ·(Q      | −Q    | )              | (4) |
|     |     |     |     |     |     |     |             |     |         |       | 0   | Q mes    | ref   |                |     |
LPF whereV 0 isthenominalvoltage,Q ref isthereferencereactive
|     |     |     |     |     |     |     | power, |     | and k | is the | droop | coefficient | for | reactive | power, |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----- | ------ | ----- | ----------- | --- | -------- | ------ |
Q
|     |     |     |     |     |     |     | adjusted |     | to balance | reactive |     | power among | parallel | inverters | in  |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | -------- | --- | ----------- | -------- | --------- | --- |
(b)
|     |     |     |                    |     |     |     | the     | system. | The          | LPF       | applied | in the | reactive | power | controller |
| --- | --- | --- | ------------------ | --- | --- | --- | ------- | ------- | ------------ | --------- | ------- | ------ | -------- | ----- | ---------- |
|     |     |     |                    |     |     |     | follows |         | the transfer | function: |         |        |          |       |            |
|     | PI  |     |                    |     | PI  |     |         |         |              |           |         |        | ω        |       |            |
|     |     |     | noitatimiL tnerruC |     |     |     |         |         |              |           | G (s)=k |        | c        |       | (5)        |
|     |     |     |                    |     |     |     |         |         |              |           | Q       | Qs+ω   |          |       |            |
c
|     |     |     |     |     |     |     |         | In addition |             | to the | droop     | control | loops,     | inner voltage | and   |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ----------- | ------ | --------- | ------- | ---------- | ------------- | ----- |
|     |     |     |     |     |     |     | current |             | controllers | are    | essential | for     | stable GFM | inverter      | oper- |
PI PI ation, as shown in Fig. 4(c). These inner control loops can be
describedusingtheproportional-integral(PI)controlstructure
(c) [13]. The PI controllers for the voltage and current loops are
defined by:
Fig.4. GFMcontrol(a)Activepowerdroopcontrol(b)Reactivepowerdroop
1
controller(c)Innervoltageandcurrentcontrollers[12]. G (s)=K + (6)
|     |     |     |     |     |     |     |     |     |     | v   |     | p−v |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
T i−v s
1
| B. Grid-forming | Inverter | Modeling |     |     |     |     |     |     |     |     |       |     |     |     |     |
| --------------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|                 |          |          |     |     |     |     |     |     |     | G   | (s)=K | +   |     |     | (7) |
|                 |          |          |     |     |     |     |     |     |     |     | i     | p−i | T s |     |     |
i−i
| In contrast | to GFL | inverters, |     | a GFM | inverter | control |     |     |     |     |     |     |     |     |     |
| ----------- | ------ | ---------- | --- | ----- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
topology actively manages both voltage and frequency at the where K p−v and T i−v represent the proportional gain and
POI, causing the inverter to emulate a voltage source. This integral time constant of the PI controller for the voltage
|     |     |     |     |     |     |     |     |     |     |     |     | K   |     | T   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
designenablestheGFMinvertertoseamlesslyoperateinboth control loop, respectively, and p−i and i−i represent the
grid-connected and islanded modes, providing the necessary proportional gain and integral time constant for the current
flexibility to handle fluctuations in load independently when control loop [12]. These parameters are critical for ensuring
in islanded mode [11]. stablecontrolandeffectiveresponseunderdynamicconditions
In this paper, a droop-based control approach is imple- in the GFM inverter.
mented for the GFM inverter to balance load sharing between The current saturation scheme is applied to ensure that the
the GFM and a synchronous generator. The droop-based con- currentreferencevaluesdonotexceedthemaximumallowable
|                  |         |     |            |           |     |             | current,I |     | ,thuspreventingpotentialovercurrentissues[14], |     |     |     |     |     |     |
| ---------------- | ------- | --- | ---------- | --------- | --- | ----------- | --------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
| trol methodology | adjusts | the | inverter’s | frequency |     | and voltage |           |     | max                                            |     |     |     |     |     |     |
in response to active and reactive power, respectively. This [15]. This limitation is achieved by defining the saturated
strategy allows the GFM inverter to adapt its power output current reference, isat , as:
dq-ref
| based on | system demands, |     | contributing |     | to stable | operation |     |     |     |    |     |     |     |     |     |
| -------- | --------------- | --- | ------------ | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:113)
a l o ng s i d e t h e s y n c h r o n ou s ge n e r a tor in b ot h g r id -c o n n e c te d i if i2 +i2 ≤I
|     |     |     |     |     |     |     |     | is  | a t | dq-ref |     | d-ref     |     | q-ref | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | --- | ----- | --- |
|     |     |     |     |     |     |     |     |     | =   |        |     | (cid:113) |     |       | (8) |
a n d is l a n d e d s c e n a ri o s . T he a c t iv e po we r d ro o p c o n tr o l , a s d q -ref i2 +i2
|     |     |     |     |     |     |     |     |     |     | ρi | dq-ref | if  |     | >I  | max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
shown in Fig. 4(a), adjusts the frequency (ω) according to d-ref q-ref
| the active | power (P) | output | of the | inverter, | defined | by the |       |     |     |        |         |           |        |           |       |
| ---------- | --------- | ------ | ------ | --------- | ------- | ------ | ----- | --- | --- | ------ | ------- | --------- | ------ | --------- | ----- |
|            |           |        |        |           |         |        | where | i   |     | is the | current | reference | in the | dq-frame, | and ρ |
dq-ref
relationship: is a scaling factor applied to limit the current to I when
max
thecombineddq-axiscurrentreferenceexceedsthisthreshold.
|     | ω =ω | −k  | ·(P | −P  | )   | (2) |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0 P mes ref This ensures that the current remains within safe operating
| whereω | isthenominalfrequency,P |       |             | isthereferenceactive |                 |     | limits. |      |                  |          |         |               |           |         |         |
| ------ | ----------------------- | ----- | ----------- | -------------------- | --------------- | --- | ------- | ---- | ---------------- | -------- | ------- | ------------- | --------- | ------- | ------- |
|        | 0                       |       |             | ref                  |                 |     |         |      |                  |          |         |               |           |         |         |
|        |                         |       |             |                      |                 |     |         | With | this droop-based |          | control | architecture, |           | the     | GFM in- |
| power, | and k P is the          | droop | coefficient |                      | that determines | the |         |      |                  |          |         |               |           |         |         |
|        |                         |       |             |                      |                 |     | verter  | not  | only             | provides | voltage | and           | frequency | support | at the  |
sensitivityoffrequencytochangesinactivepower.Toenhance
stability and mitigate high-frequency oscillations, a low-pass interconnection point but also dynamically adapts to changes
|              |                  |           |     |        |           |          | in  | active | and reactive |       | power, | crucial | for effective | load | sharing |
| ------------ | ---------------- | --------- | --- | ------ | --------- | -------- | --- | ------ | ------------ | ----- | ------ | ------- | ------------- | ---- | ------- |
| filter (LPF) | is incorporated, | resulting |     | in the | following | transfer |     |        |              |       |        |         |               |      |         |
| function     | for active power | control:  |     |        |           |          | and | grid   | stability    | [16]. |        |         |               |      |         |
ω
|     |     |       |     | c   |     |     | C.  | Flicker | Measurement |     | Methodology |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ----------- | --- | --- | --- | --- |
|     | G   | (s)=k |     |     |     | (3) |     |         |             |     |             |     |     |     |     |
P Ps+ω
|     |     |     |     | c   |     |     |     | In compliance |     | with | IEEE | 1453-2022, | flicker | severity | was |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ---- | ---------- | ------- | -------- | --- |
where ω c represents the cut-off frequency of the LPF. measured using a flicker meter that models human sensitivity
979-8-3315-0995-8/25/$31.00 ©2025 IEEE

| tolightfluctuations.Short-termflickerseverity,P |     |     |     |     |     | ,calculated |     |                 |     |     |                 |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | --- | --------------- | --- | --- |
|                                                 |     |     |     |     |     | st          |     | Fault inception |     |     | Fault clearance |     |     |
(ii)
| over 10 | minutes, | is given | by: |     |     |     |     |     |     |            |     |     |       |
| ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | ----- |
|         |          |          |     |     |     |     |     |     |     | V= 0.97 pu |     |     | (iii) |
(cid:115)
(cid:18)
(i)
| P = | 0.0314P |     | +0.0525P |     |     |     |     |     |            |     |     |            |     |
| --- | ------- | --- | -------- | --- | --- | --- | --- | --- | ---------- | --- | --- | ---------- | --- |
| st  |         | 0.1 |          | 1   |     |     |     |     | V= 0.90 pu |     |     | V= 0.87 pu |     |
(cid:19)
|     |     | +0.0657P |     | 3 +0.28P | 10 +0.08P | 50  | (9) |     |     |     | (a) |     |     |
| --- | --- | -------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Data center switches
where P ,P ,P ,P , and P represent flicker levels ex- to local supply.
|               | 0.1 1 | 3 10      |                   | 50       |          |                   |         |     |     |     |     |     |     |
| ------------- | ----- | --------- | ----------------- | -------- | -------- | ----------------- | ------- | --- | --- | --- | --- | --- | --- |
| ceeded for    | 0.1%, | 1%, 3%,   | 10%,              | and 50%  | of       | the time, respec- |         |     |     |     |     |     |     |
| tively. Per   | the   | IECEC     | TR 61000-3-7:2008 |          |          | standard,         | flicker |     |     |     |     |     |     |
| limits are    | Pst   | ≤ 0.9,Plt | ≤                 | 0.7 for  | medium   | voltage           | and     |     |     |     |     |     |     |
| Pst ≤ 0.8,Plt |       | ≤ 0.6 for | high              | voltage, | ensuring | compliance        |         |     |     |     |     |     |     |
(b)
| with electromagnetic |                                | compatibility |             | standards. |           |            |        |     |     |     |     |     |     |
| -------------------- | ------------------------------ | ------------- | ----------- | ---------- | --------- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
| III.                 | SIMULATIONRESULTSANDDISCUSSION |               |             |            |           |            |        |     |     |     |     |     |     |
| This section         |                                | outlines      | the results | of         | the PSCAD | simulation |        |     |     |     |     |     |     |
| of the study         | system                         | presented     |             | in Fig     | 1, where  | the data   | center |     |     |     |     |     |     |
hasapeakloadof500MW,andthedroop-basedBESS-GFM
(c)
isratedat200MW.Thefollowingelaboratesontwoscenarios
|            |         |        |     |     |     |     | Fig.5. | MeasurementsatthePOIoftheAIdatacenter,(a)voltagemagnitude, |     |     |     |     |     |
| ---------- | ------- | ------ | --- | --- | --- | --- | ------ | ---------------------------------------------------------- | --- | --- | --- | --- | --- |
| considered | in this | study. |     |     |     |     |        |                                                            |     |     |     |     |     |
(b)currentwithoutBESS-GFM,(c)currentwithBESS-GFM.
| A. Voltage | Sag       | Mitigation | with   | Grid-Forming   |     | Inverter |        |     |     |     |     |     |     |
| ---------- | --------- | ---------- | ------ | -------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
| In this    | scenario, | the        | impact | of low-voltage |     | events   | on the |     |     |     |     |     |     |
system’sreliabilityisinvestigatedwithandwithouttheBESS-
| GFM system. | With | the | increasing | penetration |     | of large | loads |     |     |     |     |     |     |
| ----------- | ---- | --- | ---------- | ----------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
AI Data Center without BESS-GFM
such as data centers, any disconnection in the load due to AI Data Center with BESS-GFM
| voltage | events       | will significantly |                | impact | the   | load-generation |     |     |     |     |     |     |     |
| ------- | ------------ | ------------------ | -------------- | ------ | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| balance | in the grid. | A single           | line-to-ground |        | fault | is applied      | at  |     |     |     |     |     |     |
BusB8att=4s,andclearedafter6cycles.Thecomparative
Fig.6. SystemfrequencywithandwithoutBESS-GFM
| voltage | and current | profiles | of  | this | scenario | are shown | in  |     |     |     |     |     |     |
| ------- | ----------- | -------- | --- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Fig.5.The“Faultinception”isexpectedtocauseavoltagesag
(below 0.9 pu) in the system as shown in Fig. 5(a)(i)–purple results in notable voltage flicker. These flicker values pose
plot.TocircumventfurthercomplicationsintheAIdatacenter a risk to system stability and could affect the reliability of
connected to the grid and ensure compliance with operational sensitive equipment connected to the grid.
standards,whenthevoltagedropsbelow0.9pu,thedatacenter To address this issue, a solution was implemented by
trips as shown in Fig. 5(b). The disconnection of the data integratingaBESS-GFMatthesamebus(BusB6)intheIEEE
centercausesavoltageriseatthePOI,keepingthedatacenter 9-bus system. The BESS-GFM, operating as a voltage source
within the operating limits, as shown in Fig. 5(a)(ii)–green with robust control capabilities, effectively compensates for
plot.
|     |     |     |     |     |     |     | the voltage | fluctuations |     | induced | by  | the data center’s | variable |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------- | --- | ----------------- | -------- |
When the BESS-GFM is connected to the system, it is load.ThisconfigurationstabilizesthepowerqualityatBusB6
observed that the voltage profile at the POI is above the 0.9- by dynamically adjusting voltage and frequency in response
| puthresholdandwithinnominaloperatinglimits,asshownin |     |     |     |     |     |     | to load | changes. |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- |
Fig. 5(a)(iii)–blue plot. This ride-through capability ensures AsillustratedinFig.7(b),afterconnectingtheBESS-GFM,
that the AI data center remains connected to the system as there is a significant reduction in flicker level compared to
depicted Fig. 5(c). Additionally, Fig. 6 shows the frequency the initial scenario. As shown by Fig. 8, the probability and
of the system with and without BESS-GFM. It is seen that cumulativedensityfunctionsoftheinstantaneousflickerlevels
the frequency of the system is within steady-state operating shift towards lower values, indicating that the magnitude and
conditionswhentheBESS-GFMisconnected,maintainingthe frequency of flicker have been mitigated.
load-generation balance in the system. Quantitatively, the short-term flicker severity (P ) for both
st
|            |            |      |              |     |          |     | scenarios  | was | evaluated, | with   | and without | the BESS-GFM, | as            |
| ---------- | ---------- | ---- | ------------ | --- | -------- | --- | ---------- | --- | ---------- | ------ | ----------- | ------------- | ------------- |
| B. Flicker | Mitigation | with | Grid-Forming |     | Inverter |     |            |     |            |        |             |               |               |
|            |            |      |              |     |          |     | summarized |     | in Table   | I. The | comparison  | shows         | a substantial |
AI data centers present unique challenges to power quality, differenceinflickerseverity,witha98.93%reductionachieved
especially in terms of flicker, due to their nonlinear load char- by integrating the BESS-GFM.
acteristics and rapidly fluctuating load profiles. As illustrated Fig. 7 illustrates the improvement in flicker mitigation at
by Fig. 7(a), the high variability of the data center’s load the POI with the addition of the BESS-GFM. Fig. 7 (a),
979-8-3315-0995-8/25/$31.00 ©2025 IEEE

(a)
(b)
98.93% Flicker reduction
| Fig.7. | POIvoltage(a)withoutBESS-GFM,(b)withBESS-GFM. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLEI
PstLEVELSWITHANDWITHOUTBESS-GFM
|     |     |     |     |     |     |     | Fig. 8. Probability |     | density | and cumulative |     | probability | of  | flicker values |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | -------------- | --- | ----------- | --- | -------------- |
SCR Pst levelwithoutBESS-GFM Pst levelwithBESS-GFM with and without BESS-GFM, plotted on a logarithmic x-axis for better
visualization.
| High | 0.2061 |     |     |     | 0.0212 |     |             |     |               |        |        |         |        |             |
| ---- | ------ | --- | --- | --- | ------ | --- | ----------- | --- | ------------- | ------ | ------ | ------- | ------ | ----------- |
| Low  | 0.947  |     |     |     | 0.278  |     |             |     |               |        |        |         |        |             |
|      |        |     |     |     |        |     | [3] M. Koot | and | F. Wijnhoven, | “Usage | impact | on data | center | electricity |
needs:Asystemdynamicforecastingmodel,”AppliedEnergy,vol.291,
p.116798,2021.
representing the scenario without the BESS-GFM, the voltage [4] C.Boonseng,R.Boonseng,andK.Kularbphettong,“The3rdharmonic
|          |                  |             |     |     |            |        | current | and power | quality | improvements       |     | of data    | centers | using hybrid  |
| -------- | ---------------- | ----------- | --- | --- | ---------- | ------ | ------- | --------- | ------- | ------------------ | --- | ---------- | ------- | ------------- |
| waveform | shows noticeable | oscillation |     | due | to flicker | caused |         |           |         |                    |     |            |         |               |
|          |                  |             |     |     |            |        | power   | filters,” | in 2019 | 22nd International |     | Conference |         | on Electrical |
by the rapidly fluctuating load of the AI-driven data center. MachinesandSystems(ICEMS),2019,pp.1–4.
These fluctuations contribute to a high flicker severity level, [5] S. G M et al., “Combination of APF and SVC for the Power Quality
impacting power quality. In contrast, Fig. 7 (b) shows the Improvement in Microgrid,” in 2022 IEEE 3rd Global Conference for
AdvancementinTechnology(GCAT),2022,pp.1–4.
scenario with the BESS-GFM connected, where the voltage [6] Y.ZhouandR.Yokoyama,“ModifiedDroopControlforSupportSystem
waveform is significantly smoother. This stability reflects the Voltage with PID and its Implementation to Multi-VSCs for GFM
|            |            |             |         |     |                 |     | Inverter,” | in  | 2023 Power | Electronics | and | Power | System | Conference |
| ---------- | ---------- | ----------- | ------- | --- | --------------- | --- | ---------- | --- | ---------- | ----------- | --- | ----- | ------ | ---------- |
| BESS-GFM’s | capability | to mitigate | flicker |     | by compensating |     |            |     |            |             |     |       |        |            |
(PEPSC),2023,pp.1–6.
for load-induced voltage oscillations, thus improving power [7] Y. Li, K. Meng, and Z. Y. Dong, “Frequency enhancement of grid-
qualityandreducingtheflickerseverityatthePOI.Itisworth forminginvertersunderlow-SCRweakgrid,”in8thRenewablePower
GenerationConference(RPG2019),2019,pp.1–7.
| mentioning | that factors        | like system | strength,    |     | magnitude | and      |                                                                     |        |                   |     |            |            |     |             |
| ---------- | ------------------- | ----------- | ------------ | --- | --------- | -------- | ------------------------------------------------------------------- | ------ | ----------------- | --- | ---------- | ---------- | --- | ----------- |
|            |                     |             |              |     |           |          | [8] Z.Zhangetal.,“Lowvoltageridethroughcharacteristicsofgridforming |        |                   |     |            |            |     |             |
| frequency  | of load variations, |             | and response |     | time of   | inverter |                                                                     |        |                   |     |            |            |     |             |
|            |                     |             |              |     |           |          | inverters,”                                                         | in2020 | 21stInternational |     | Scientific | Conference |     | on Electric |
PowerEngineering(EPE),2020,pp.1–6.
| controls | can impact the | BESS-GFM |     | requirements | for | flicker |                                                              |     |     |     |     |     |     |     |
| -------- | -------------- | -------- | --- | ------------ | --- | ------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|          |                |          |     |              |     |         | [9] S.Sharifetal.,“PerformanceAnalysisforLFCofanEnhancedIEEE |     |     |     |     |     |     |     |
mitigation.
|     |     |     |     |     |     |     | 9-Bus | Power             | System | with GFL   | and GFM        | Inverter | Control,” | in 2024    |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------------- | ------ | ---------- | -------------- | -------- | --------- | ---------- |
|     |     |     |     |     |     |     | IEEE  | 4th International |        | Conference | on Sustainable |          | Energy    | and Future |
ElectricTransportation(SEFET).
|     | IV. | CONCLUSION |     |     |     |     |            |            |            |             | IEEE,2024,pp.1–6. |            |     |              |
| --- | --- | ---------- | --- | --- | --- | --- | ---------- | ---------- | ---------- | ----------- | ----------------- | ---------- | --- | ------------ |
|     |     |            |     |     |     |     | [10] L. L. | Qi et al., | “Modeling, | simulation, | and               | protection | of  | grid forming |
This paper demonstrated that integrating BESS-GFM with inverter-basedringconfigurationdatacenter,”inIEEEIndustryApplica-
|           |              |             |          |     |       |         | tionsSocietyAnnualMeeting(IAS).                                     |     |     |     | IEEE,2022,pp.1–7. |     |     |     |
| --------- | ------------ | ----------- | -------- | --- | ----- | ------- | ------------------------------------------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- |
| AI-driven | data centers | effectively | enhances |     | power | quality |                                                                     |     |     |     |                   |     |     |     |
|           |              |             |          |     |       |         | [11] W.Duetal.,“Modelingofgrid-formingandgrid-followinginvertersfor |     |     |     |                   |     |     |     |
and system reliability. Simulations on a modified IEEE 9- dynamicsimulationoflarge-scaledistributionsystems,”IEEETransac-
bus system showed that BESS-GFM mitigates voltage sags tionsonPowerDelivery,vol.36,no.4,pp.2035–2045,2020.
|             |                |          |             |     |        |          | [12] A. Azizi | and | A. Hooshyar, | “Fault | current | limiting | and | grid code |
| ----------- | -------------- | -------- | ----------- | --- | ------ | -------- | ------------- | --- | ------------ | ------ | ------- | -------- | --- | --------- |
| and flicker | caused by data | centers’ | fluctuating |     | loads, | ensuring |               |     |              |        |         |          |     |           |
complianceforgrid-forminginverters—partI:Problemstatement,”IEEE
| stable voltage | and frequency | even | during | low-voltage |     | events. |     |     |     |     |     |     |     |     |
| -------------- | ------------- | ---- | ------ | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
TransactionsonSustainableEnergy,2024.
|                |            |     |          |         |       |         | [13] A. D.    | Paquette | and D.     | M. Divan, | “Virtual    | impedance    | current | limiting    |
| -------------- | ---------- | --- | -------- | ------- | ----- | ------- | ------------- | -------- | ---------- | --------- | ----------- | ------------ | ------- | ----------- |
| By maintaining | connection | and | reactive | support | under | distur- |               |          |            |           |             |              |         |             |
|                |            |     |          |         |       |         | for inverters | in       | microgrids | with      | synchronous | generators,” |         | IEEE Trans. |
bances,BESS-GFMpreventsloaddisconnectionsandsupports
IndAppl.,vol.51,no.2,pp.1630–1638,Mar./Apr.2015.
| IEEE power | quality standards, |     | making | them | a valuable | so- |                   |     |               |     |              |     |         |            |
| ---------- | ------------------ | --- | ------ | ---- | ---------- | --- | ----------------- | --- | ------------- | --- | ------------ | --- | ------- | ---------- |
|            |                    |     |        |      |            |     | [14] B. Mahamedi, |     | M. Eskandari, | J.  | E. Fletcher, | and | J. Zhu, | “Sequence- |
lution for stability in systems with high inverter-based and basedcontrolstrategywithcurrentlimitingforthefaultride-throughof
inverter-interfaceddistributedgenerators,”IEEETrans.Sustain.Energy,
| renewable | resources. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vol.11,no.1,pp.165–174,Jan.2020.
|     |     |     |     |     |     |     | [15] S.F.Zarei,H.Mokhtari,M.A.Ghasemi,andF.Blaabjerg,“Reinforcing |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES fault ride through capability of grid forming voltage source converters
|     |     |     |     |     |     |     | using | an enhanced | voltage | control | scheme,” | IEEE | Trans. | Power Del., |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----------- | ------- | ------- | -------- | ---- | ------ | ----------- |
vol.34,no.5,pp.1827–1842,Oct.2019.
[1] J.Shairetal.,“Powersystemstabilityissues,classificationsandresearch
|           |                |                     |     |               |     |           | [16] F. Sadeque, | M.  | Gursoy, | and B. | Mirafzal, | “Grid-forming |     | inverters in a |
| --------- | -------------- | ------------------- | --- | ------------- | --- | --------- | ---------------- | --- | ------- | ------ | --------- | ------------- | --- | -------------- |
| prospects | in the context | of high-penetration |     | of renewables |     | and power |                  |     |         |        |           |               |     |                |
electronics,”RenewableandSustainableEnergyReviews,vol.145,2021. microgrid:Maintainingpowerduringanoutageandrestoringconnection
[2] L. Xie et al., Emerging Technology for Distributed Energy Resources. to the utility grid without communication,” IEEE Transactions on
Cham:SpringerInternationalPublishing,2023,pp.17–44. IndustrialElectronics,2024.
979-8-3315-0995-8/25/$31.00 ©2025 IEEE