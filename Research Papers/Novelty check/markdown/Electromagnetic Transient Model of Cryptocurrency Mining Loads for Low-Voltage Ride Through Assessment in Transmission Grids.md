1
Electromagnetic Transient Model of Cryptocurrency
Mining Loads for Low-Voltage Ride Through
Assessment in Transmission Grids
Anindita Samanta, Subir Majumder, Member, IEEE, Hasan Ibrahim, Student Member, IEEE, Prasad
Enjeti, Fellow, IEEE, Le Xie, Fellow, IEEE
Abstract—In this paper, we developed an Electromagnetic
Transient(EMT)modeltailoredforlargecryptocurrencymining
loads to understand the cross-interaction of these loads with
the electric grid. The load model has been built using Electro-
magnetic Transients Program (EMTP) software. We have cross-
validated the tripping characteristics of the EMT model of this
loadwithcommercialapplication-specificintegratedcircuitmin-
ers, typically used by large-scale mining facilities, by comparing
the low-voltage ride-through (LVRT) capabilities. Subsequently,
LVRT capabilities of the large-scale miners have been tested
against various fault scenarios both within the miner’s remote
facilityaswellasatoneofthedistantbusesoftheinterconnected
grid. The significance of this model lies in its scalability to Figure1:MiningfirmRiotPlatforms,Inc.withownsubstation
accommodate larger blocks of mining loads and its seamless of 750MW located in Rockdale, Texas [7].
integration into a larger electric grid.
Index Terms—Cryptocurrency mining loads, Electromagnetic
model, EMTP, Low Voltage Ride Through, Transient studies
during this episode plummeted to 0.36pu. With a surge in
requests for interconnection from these cryptocurrency loads
I. INTRODUCTION [9], ERCOT has been scrambling to conduct power grid
dynamic performance analysis for developing newer LVRT
Overthepastdecade,blessedwithabundantwindandsolar
standards for these loads. Recent large penetration of these
resources, the Texas power grid has witnessed a significant
loads is also partially responsible for the lack of availability
increase in renewable energy penetration, accounting for al-
of suitable models for dynamic performance analysis.
most 40% of the state’s total generation capacity [1]. This
In regards to the modeling efforts for crypto-mining fa-
waspartlythereasonthatdrewattentionfrommanyemerging
cilities, efforts have been made toward the use of power
electric loads, such as large cryptocurrency mining operators
quality analyzers within a farm. In this context, Wheeler et
[2]. These crypto-mining industrial facilities with their large
al. have conducted power factor and harmonic analysis for
sitewide energy demand (see Fig. 1), integrated with power-
a physical site with S9 AntMiners as processing units [10].
electronic converters, play a crucial role in the system-wide
As demonstrated in [10], which is also corroborated by our
frequency response. These resources are similar to wind and
lab tests (see Fig. 2) available in [11], the voltage waveform solar resources, and operate on converter-based systems, akin
does not suffer from distortions owing to being connected
to inverter-based resources (IBR), with distinct dynamics in
to an ideal power source, but, the current waveform shows
contrast with conventional synchronous generators and loads.
distortion during startup. In [11], we also conducted power
However, depending upon the topology of the converter used,
quality analysis at two industrial facilities where we observed the transient response of these mining facilities can signifi-
similarperformance. Duringthesteadystate,thepowerfactor
cantly differ compared to solar or photovoltaic (PV) inverters
remains between 0.994 and 0.995 leading. However, these
[3]. Recent outage events of the IBR-interfaced resources
loads show non-linear characteristics during power system in the Panhandle and Odessa regions of Texas have raised
transients. The need for accurate modeling of crypto-mining
significant concerns [4], [5] on what if these large mining
facilities through dynamic load modeling, frequency scan,
facilities suffer from outages, or, how do these large loads
and eigenvalue analysis has already been discussed in the contributetosystemdynamics.IBR-resourcesoutageincidents
existing literature [12]. However, as discussed in [12], the
were considered to be associated with a lack of proper
electromagnetic transient (EMT) model of these loads for
electromagnetic transient responses from these resources [6],
their transient performance analysis is largely missing. To set
which would likely exacerbate with increasing penetration of
standardsforgridinterconnectioninTexas,thedevelopmentof
crypto-mining loads.
an EMT model for these power supplies, appropriate analysis
Owing to ERCOT’s (major power grid operator operating
oftheirtransientperformance,andtheirinteractionwithother
withinthestateofTexas,USA)interconnectionguidelines[8],
resources in the power grid are extremely important.
IBR-based generating resources should maintain connectivity
even during periods of low grid voltage – a requirement Thecontributionofthisproposedworkisthereforetwofold:
known as Low Voltage Ride Through (LVRT) capability. i. ThispaperaimstodevelopanEMTmodelofacryptocur-
While ERCOT’s existing framework does not impose specific rencyminingfacility.Weidentifythattheminingconvert-
mandatesontheseconverter-basedlargeloads,recentincidents ersprimarilyutilizeactivepowerfactorcorrection(PFC)-
in West Texas on October 12, 2022 [5] vividly demonstrated boostconverters.BeingIBR-interfacedimpliesthatthese
the repercussions of a low voltage event, triggering four devicescansufferfromthecurrentoverloadlimits.There-
cascadingfaultsandultimatelyleadingtoanoutageexceeding fore,theseresourcescontributetosystemtransientintwo
400MW, which included converter-based large loads, such differentways:(a)byactingasaconstantpowerload,and
as crypto-mining facilities. The recorded minimum voltage (b) through responses from the rest of the system due to
theoutageofsuchalargeload.Weuseaswitchingmodel
AninditaSamanta,SubirMajumder,HasanIbrahim,PrasadEnjeti,andLe to represent constant power load. To properly estimate
XiearewiththeDepartmentofElectricalEngineeringandComputerSciences, the outage of large loads, the voltage sag magnitude-
TexasA&MUniversity,USA.(Correspondingauthor:le.xie@tamu.edu)
durationcapabilitycharacteristicsofthedevelopedmodel
ThisworkissupportedinpartbyTexasA&MEnergyInstituteandinpart
bytheBlockchainandEnergyResearchConsortium. have been validated against a laboratory-scale crypto-
42298601.4202.49915MGSEP/9011.01
:IOD
|
EEEI
4202©
00.13$/42/2-3818-3053-8-979
| )MGSEP(
gniteeM
lareneG
yteicoS
ygrenE
&
rewoP
EEEI
4202
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:29:49 UTC from IEEE Xplore. Restrictions apply.

2
Active Boost PFC
Mining
Protection Load
Module iL
vrec vdc
PWM
vrec PWM iL vdc
PPWWMM
GGeenneerraattoorr
_ _
PPII (cid:1)(cid:1) + (cid:1)(cid:1) PPII (cid:1)(cid:1) + VVDDCC
RReeff
Figure 3: Block diagram of active PFC-Boost converter rep-
resenting mining power supply.
Figure2:IVCharacteristicsofminingpowersupply:(a)Based
onpowersupplyavailablein our lab,(b)Startuptime-domain
voltage and current waveforms reproduced from [10].
mining load. The EMT model has been developed in the
ElectromagneticTransientsProgram(EMTP)software.It
Figure4:Start-upwaveformfortheEMTmodelofcryptocur-
has been made open source1. rency miner power supply.
ii. The performance of the developed EMT model has been
demonstratedutilizinga120kV6-bustestsystemconsid-
ering faults at two different locations: (a) at the crypto-
miner’s premises, and (b) at bus 3 of the test system. power system. Here, we have developed switching-based
The rest of the paper is organized as follows. The detailed models of an active PFC-boost converter in the EMTP to
model of a cryptocurrency mining facility and its validation model the crypto-mining facility. A block diagram of this
against laboratory test results are provided in Section II. The converter is provided in Fig. 3. The converter consists of a
integration of the developed EMT model with a small-scale bridge rectifier at the input side and a boost circuit aiming
power grid from EPRI is provided in Section III. The LVRT to maintain a constant DC-bus voltage v dc. As shown in the
capability of these mining facilities for various fault scenarios figure,theprofileofrectifiedloadsandthedeviationinDC-bus
is also presented in this section. Section IV concludes this voltagepassedthroughthePIcontrollerprovidethereferences
paper and provides future scope of research. for the inductor current in the boost converter. The second
PI controller with a limiter generates PWM signals for the
insulated-gate bipolar transistor (IGBT)-based switch within
II. DEVELOPMENTOFEMTMODELOFA
theconvertertotracktheinductorcurrentwiththedetermined
CRYPTOCURRENCYMININGLOAD
reference.Theinductorandcapacitorsaredesignedtoallowa
Contrary to general-purpose computing resources, an certainamountofripplesinthevoltageandcurrentwaveform.
industrial-scale cryptocurrency mining facility utilizes ThegainsofthePIcontrollerscouldbetunedfordesiredfast-
application-specific integrated circuit (ASIC) chips embedded nessinresponsefromtheconverters.Asdescribedin(1),these
in a hashing board. These hash boards are powered by the miningloadsbehaveasconstantpowerloads(CPLs)duetothe
mining power supply. Typically these mining power supplies fact the ac to dc boost stage of the power supply regulates the
are driven by single-phase 240V source, however, in recent dc-link voltage against input supply variations. Here, V (t),
rms
times, the use of three-phase power supplies are also notable. I (t) are the rms voltage and current magnitudes and P is
In this analysis, we will focus on the widely-used S19 rms av
the average power drawn by the crypto-mining power supply.
Antminer with a 240V single-phase power supply. Based on
Fig. 2, and the power supply repair guide for the Antminer
∂V ∂I
[13], we model the crypto-mining power supply as active V (t)I (t)=P =⇒ rmsI +V rms =0 (1)
PFC-boost converters. Although diverse PFC converters, each rms rms av ∂t rms rms ∂t
with their unique dynamic performances, exist [14], we have
optedforconventionalboostPFCconvertersfortheirversatile Being operated as a CPL implies that during the transients
uses. the product of the rms voltage and the current remains
Electromagnetic Transient Program (EMTP) software is constant. The implications of this behavior can be observed
widely used for transient performance analysis [15] of the during all operating conditions. During start-up, depending
upon the DC-bus voltage, the converter would show inrush,
1Repository is available at: https://github.com/SuM-EM/EMT-Model- which can be found in both Figs. 2(b) and 4. Both of these
Crypto.git figuresalsoshowthataftertheinitialtransient,thevoltageand
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:29:49 UTC from IEEE Xplore. Restrictions apply.

3
current become in phase. During sags, the converter current
drops suddenly but grows as time progresses, as shown in
Fig. 5. As the voltage recovers, the inrush kicks in as shown
in Figs. 2(a), and 5, which may lead to tripping of mining
powersupply.Fromtheblock-diagraminFig.3,itisimminent
that during the zero-voltage condition, the current reference
wouldbezero,andtherefore,asshowninFig.2(a),thecurrent
drawn by the mining power supply would also be zero. The
diode as a part of the boost stage of the converter implies
that the energy from the DC bus cannot flow in the reverse
direction. Therefore, the miners never feed the faults. This
(a)Simulatedfaultof50%pre-faultvoltagefor45msduration.
alsoimpliesthatminerswillhavelimitedabilitytoparticipate
in the frequency response. However, miners can go into idle
mode or entirely shut off to provide ancillary support to the
powersystem.Howminersprovideancillarysupportisbeyond
the scope of this paper. Ideal voltage and current waveforms
of the crypto-mining power supply could be given as follows:
P
i(t)= av v(t) (2)
V (t)2+(cid:3)
rms
(cid:3) is a small positive real number prohibiting division by
zero.v(t)andi(t)areinstantaneousvoltageandcurrentdrawn
by the power supply. Here, miners have the capability to set (b)Simulatedfaultof50%pre-faultvoltagefor16msduration.
P av . Figure 5: Time-domain response of the EMT model of the
Theconvertersaredesignedtooperatebelowcertainloading
crypto-mining power supply.
capabilities,determiningtheirovercurrentlimits.Theyarealso
equippedwithbothover-andunder-voltageprotection.During
theinrushcondition,iftheovercurrentcircuitrygetstriggered,
or the DC-bus voltage drops significantly, it may eventually
cause the mining loads to trip. Therefore, we observe that
there are two major contributors to the transient behavior of
the system: (i) transient resulting because of being operated
as a constant power load, and (ii) transient response from the
system resources following the outage of mining loads. In
regards to the protection circuitry of the model, we have used
a simplified overcurrent protection, where, the crypto-mining
power supply trips if the rms value of the current through
the inductor exceeds a certain threshold. We have performed
extensive tests with the developed model by connecting the
developedmodeltoanidealpowersupplyandsubjectingitto
voltage sags of various magnitudes and durations. For further Figure 6: Validation with laboratory crypto-mining power
model validation, we compared this sag magnitude-duration supply. The solid black line corresponds to the laboratory
capability characteristics to a S19 ASIC miner available in results from the mining power supply. show experiments
our lab. The results are presented in Fig. 6. Individual mea- where the power supply was tripped. show experiments
surements obtained out of the laboratory testing are provided where the power supply did not trip.
in [11], and for representational simplicity, we have denoted
it by a continuous line. Given the non-linearity of the LVRT
characteristics, we have considered only a few typical voltage carrierfrequencyfortheswitchingconverter.I ispeakcurrent
levels with different durations that are very close to the capability of the protection block. kV, kI ar P e gains the PI-
trippingpointofthereal-worldS19ASICminers.Inthiswork, i p
we have limited ourselves to full load operating conditions controller to control voltage, and k p I and k i I are PI-controller
of the mining power supplies to understand their worst-case gains to generate current set-point.
performance. Understanding the behavior of the EMT model
of the mining load under different operating conditions will TABLEI:MODELPARAMETERS
be taken up as a part of future work. Nevertheless, based on
our experience, miners rarely operate each of load at partial R L =0.45Ω L=0.0848mH C =1F ωc =25kHz
loading conditions. v R D e C f =400V I P =2.2kA
Duringmodeltestingandsimulation,itbecameevidentthat k p V =0.25 k i V =35 k p I =2000 k i I =0.25
theseverityofvoltagesagsandthecurrentdrawnduringthese
events are influenced not only by the magnitude and duration
ofthesagbutalsobythespecificpointonthewave[16],(see
casestudysection,wheretrippingofapartialsetofconverters III. CASESTUDIES
is notable). Nevertheless, this additional information is absent
The performance of the developed EMT model has been
in the voltage sag magnitude-duration characteristics. Hence,
testedina120kV,60Hz,6-bustransmissionnetworkinEMTP.
modeling the converter to align exclusively with magnitude-
A detailed description of the test system containing the solar
durationcharacteristics,whileneglectingthebroaderconverter
PVparkisprovidedin[17].Amoderatelysizedcrypto-mining
protection system could lead to deviations from laboratory facility of ∼1MW with loads equally distributed across all
experiments (see one of the test results deviate from the ideal
three phases was considered. As shown in Fig. 7, the mining
scenario).
facility is connected with the rest of the transmission network
Parameters of the developed model are provided in Table I. through a Δ-Yg 25kV/415V transformer with a percentage
Given we aim to control the DC-bus voltage, v R D e C f , under the impedance of 6% at bus 6. Therefore, the mining power
constant power load paradigm, the load could be represented supplies are supplied with an input voltage at 240V with the
by resistance, R L. It could be calculated as V P D a C v 2 . ω c is the DC-bus voltage to be maintained at 400V.
Ref
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:29:49 UTC from IEEE Xplore. Restrictions apply.

4
|     |     |     |     |     |     |     |     |        | (a) Current | Waveforms   | of      | Miners     | (Aggregated) | Facility. |            |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----------- | ------- | ---------- | ------------ | --------- | ---------- |
|     |     |     |     |     |     |     |     |        |             | (b) Fault   | Voltage | at Miner   | Premises.    |           |            |
|     |     |     |     |     |     |     |     | Figure | 8:          | Voltage and | current | at miner’s | premises     | with      | a 3-φ      |
|     |     |     |     |     |     |     |     | fault  | of 50%      | pre-fault   | voltage | of 15      | ms duration  |           | applied at |
load end.
Figure7:Cryptocurrencyfarminterconnectedwith120kVTest
System.Theperformanceofminingconvertersiscomparedfor
| two distinct | scenarios  |           | considering |          | three-phase      | line-to-ground     |           |     |     |     |     |     |     |     |     |
| ------------ | ---------- | --------- | ----------- | -------- | ---------------- | ------------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| (LLLG)       | faults:    | (i) FAULT |             | 1: fault | within           | the cryptocurrency |           |     |     |     |     |     |     |     |     |
| miner’s      | premises,  | and       | (ii) FAULT  | 2:       | fault            | at bus             | 3.        |     |     |     |     |     |     |     |     |
| The          | non-mining |           | loads       | in the   | test system      | are                | modeled   |     |     |     |     |     |     |     |     |
| as constant  | impedance  |           | loads       | and      | the transmission |                    | lines     | are |     |     |     |     |     |     |     |
| modeled      | using      | constant  | parameter   |          | models.          | Both               | loads are | 30  |     |     |     |     |     |     |     |
MWeachandthesolarPVparkhasacapacityof75MVA.We
| consider | the constant |     | power | output | from the | solar | park across |     |             |           |     |        |              |           |     |
| -------- | ------------ | --- | ----- | ------ | -------- | ----- | ----------- | --- | ----------- | --------- | --- | ------ | ------------ | --------- | --- |
|          |              |     |       |        |          |       |             |     | (a) Current | Waveforms | of  | Miners | (Aggregated) | Facility. |     |
allscenariosandconstantloaddemandfromthecrypto-mining
facilityattheirrespectiveratedcapacity.Suchasettingwould
| facilitate    | testing | the transient |          | behavior    | of the   | power              | system      | in    |     |     |     |     |     |     |     |
| ------------- | ------- | ------------- | -------- | ----------- | -------- | ------------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| the presence  | of      | a mining      | facility | during      | peak     | load               | conditions. |       |     |     |     |     |     |     |     |
| The projected |         | sites         | in Fig.  | 7 represent |          | the scalability    |             | of    |     |     |     |     |     |     |     |
| our model.    | The     | faults        | were     | initiated   | after    | the cryptocurrency |             |       |     |     |     |     |     |     |     |
| miners        | reached | a steady      | state.   | We          | explored | multiple           |             | cases |     |     |     |     |     |     |     |
undereachofthesescenariosbasedonfaultdurationandfault
| impedance | dictating |         | the sag  | voltage       | magnitude. |             |     |       |     |           |         |          |           |     |     |
| --------- | --------- | ------- | -------- | ------------- | ---------- | ----------- | --- | ----- | --- | --------- | ------- | -------- | --------- | --- | --- |
| A. Fault  | applied   | at Load | End      |               |            |             |     |       |     |           |         |          |           |     |     |
|           |           |         |          |               |            |             |     |       |     | (b) Fault | Voltage | at Miner | Premises. |     |     |
| Compared  | to        | Fig.    | 5, which | was generated |            | considering |     | ideal |     |           |         |          |           |     |     |
voltagesource,limitedshort-circuitcapabilityimpliesthatthe Figure9:Voltageandcurrentatminer’spremiseswithabolted
post-fault network voltage may not remain as ideal sinusoid 3-φ fault of 15 ms duration applied at load end.
| as depicted | in  | Figs. | 8(b) and | 9(b). | Here, | we have | compared |     |     |     |     |     |     |     |     |
| ----------- | --- | ----- | -------- | ----- | ----- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
the LVRT capability of the crypto-miners’ power supply with TABLE II: LVRT CAPABILITY WITH FAULT WITHIN MINER’S
| a3-φboltedfaultandafaultwith50%pre-faultvoltage,each |     |     |     |     |     |     |     |          |     | (∗ → |        |                     |     |     |        |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ------ | ------------------- | --- | --- | ------ |
|                                                      |     |     |     |     |     |     |     | PREMISES |     | ALL  | MINERS | IN ONE-OUT-OF-THREE |     |     | PHASES |
TRIP)
| for a duration |     | of 15 | ms. | While the | mining | power | supplies |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | --- | --------- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
in all three phases were able to ride through with a fault of SagVoltage Durationoffault
50%pre-faultvoltage,noneoftheminingpowersupplieswere
|     |     |     |     |     |     |     |     |     | (%ofPrefault) | 09ms | 1cycle(15ms) |     | 3cycles(45ms) |     | 100ms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | ------------ | --- | ------------- | --- | ----- |
abletoridethroughwiththeboltedfault,whichisinlinewith 75% NO NO NO NO
1/3TRIP∗
the ride-through characteristics shown in Fig. 6. Also, it can 50% NO NO YES
|              |           |              |        |             |          |         |          |       | 25% | YES |     | YES |     | YES | YES |
| ------------ | --------- | ------------ | ------ | ----------- | -------- | ------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| be seen      | that      | after the    | mining | power       | supplies | were    | tripped, |       |     |     |     |     |     |     |     |
|              |           |              |        |             |          |         |          |       | 0%  | YES |     | YES |     | YES | YES |
| in Fig.      | 9(b), the | voltage      | at     | the miners’ | premises |         | contains | a     |     |     |     |     |     |     |     |
| large amount |           | of harmonics |        | that tend   | to       | die out | with     | time. |     |     |     |     |     |     |     |
| Harmonics    | could     | safely       | be     | attributed  | to       | the PV  | farm,    | and   |     |     |     |     |     |     |     |
additional experiments without mining power supply validate within the miner’s premises, and the results are tabulated in
this (not shown for brevity). Fig 9(a) shows that during zero Table II. As highlighted in Fig. 6, demonstrating the LVRT
voltage, mining power supplies draw no current compared to capabilityofcryptominer’spowersupply,withsagvoltageof
8(a).Also,wecanobservethatminingpowersuppliesarenot 75% pre-fault voltage magnitude none of the miners should
feeding the fault. trip, and it has been validated in Table II. As with 50% pre-
We have conducted additional experiments to understand fault voltage and fault duration of 45 ms, all the miners in
the LVRT capability of the mining facility if the faults are one of the phases out of all the three phases trips. This can
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:29:49 UTC from IEEE Xplore.  Restrictions apply.

5
TABLE III: MINER’S LVRT CAPABILITY WITH FAULT AT BUS 3
(∗ → ALL MINERS IN ONE-OUT-OF-THREE PHASES TRIP, † →
ALLMINERSINTWO-OUT-OF-THREEPHASESTRIP)
SagVoltage Timedurationoffault
(%of 09ms 1cycle 3cycles 100ms
Prefault) (15ms) (45ms)
75% 1/3TRIP∗ 1/3TRIP∗ 1/3TRIP∗ 1/3TRIP∗
50% 1/3TRIP∗ 2/3TRIP† 2/3TRIP† YES
25% 1/3TRIP∗ YES YES YES
0% 2/3TRIP† YES YES YES
(a) Current Waveforms of Miners (Aggregated) Facility.
in terms of its LVRT capability was compared considering
two fault scenarios: (i) fault within the miner’s premises, and
(ii) fault near the PV farm. The resulting harmonics from
the PV farm in the aftermath of the fault can interact with
the controllers of the cryptocurrency miner’s power supply
resulting in an outage of these cryptominers, which would
be challenging, especially in a network with a low short
circuitratio.Whilethedevelopedmodelofthecryptocurrency
miners is highly scalable, the use of a detailed switching
model hinders large-scale performance analysis of multiple
cryptocurrency mining facilities in a larger system. Therefore,
(b) Voltage Waveforms at Miner Premises. inthefuture,wewouldliketodevelopanaveragevaluemodel
and utilize it for larger-scale performance analysis.
REFERENCES
[1] P. Vegas, “ERCOT Public Presentation : CEO Update - Revised,”
Publishedin31,August2023, [Online].Available: https://www.ercot.
com/files/docs/2023/08/28/5%20CEO%20Update%20REVISED.pdf.
[2] J. Brett, “Texas Poised To Be A World Leader In Bitcoin And
Blockchain,” Published in Forbes 02, October 2021, [Online].
Available: https://www.forbes.com/sites/jasonbrett/2021/10/02/
texas-poised-to-be-a-world-leader-in-bitcoin-and-blockchain/?sh=
6e2db00a715b.
[3] B. Shakerighadi, N. Johansson, R. Eriksson, P. Mitra, A. Bolzoni,
A.Clark,andH.-P.Nee,“Anoverviewofstabilitychallengesforpower-
(c) Fault Voltage at Bus 3. electronic-dominated power systems: The grid-forming approach,” IET
Generation, Transmission & Distribution, vol. 17, no. 2, pp. 284–306,
Figure10:Voltageandcurrentatminer’spremisesandvoltage 2023.
at the faulted bus with a 3-φ fault of 75% pre-fault voltage [4] D. Woodfin, “Ercot public presentation: Item 7.2.1: Inverter based
resourceandlargeloadridethroughevents:Backgroundandmitigation,”
for a period of 100 ms duration applied at bus 3. Publishedin19,June2023,[Online].:www.ercot.com.
[5] A.Springer,E.Rowe,andE.Neel,“Ercotpublicpresentation:Ibrtf-lfl
interconnection&resourceadequacy,”Publishedin05,April2023,Texas
A&MUniversity.
be attributed to the large post-fault inrush current drawn from [6] ERCOT IBRTF Meeting - NERC, “Reliability guidelines: Electro-
magnetic transient (emt) modeling for bps-connected inverter-based
bus 6 which is a function of the point-on-wave. For a fault resources – requirements and verification practices & emt task
duration of less than 100 ms and with a sag voltage of less force,” [Online] Available : https://www.ercot.com/files/docs/2023/01/
than25%pre-faultvoltage,noneoftheminingpowersupplies 20/RG-EMTModelingandSimulation-EMTTF-ERCOTIBRTF2023.pdf.
[7] “North america’s largest bitcoin mining facility by developed capac-
can ride through. ity,”[Online]Available:https://www.riotplatforms.com/bitcoin-mining/
whinstone-u-s.
[8] S. Solis, “ERCOT Public Presentation: IBRTF - NOGRR245 -
B. Fault at bus 3 Inverter-Based Resource (IBR) Ride-Through Requirements,”
Published in 20, January 2023, [Online]. Available : https:
Owingtothetransmissionline’simpedance,thesagvoltage //www.ercot.com/files/docs/2023/01/20/NOGRR245%20IRR%20Ride%
observedatthecrypto-miners’spremiseswouldbelesssevere 20Through%20Requirements IBRTF 01202023.pptx.
[9] “ERCOT Public Presentation: Large Load Interconnection
than in the previous scenario (comparing Figs. 10(b) and
Status,” Published in 17, February 2023, [Online]. Available
10(c)). However, the occurrence of faults near the PV park : https://www.ercot.com/files/docs/2023/02/17/LLI%20Queue%
appears to inject a significant amount of harmonics. This 20Status%20Update%20-%202023-02-17.pdf.
interacts with the controller of the mining power supply, and [10] K.A.Wheeler,A.W.Bowers,C.H.Wong,J.Y.Palmer,andX.Wang,
“Apowerqualityandloadanalysisofacryptocurrencymine,”in2018
depending upon the phase it may lead to an outage of all IEEEElectricalPowerandEnergyConference(EPEC). IEEE,2018.
the mining power supplies. We have further conducted an [11] S. Almubarak, H. Ibrahim, D. Singhania, and P. Enjeti, “Energy con-
extensive number of experiments to understand the mining sumption&powerqualityinbitcoinminingfacilitiesintexas,”in2023
IEEEEnergyConversionConferenceandExpo,2023.
power supplies’ LVRT capability, which is demonstrated in [12] S.Mohan,S.Maleki,M.Shirinzad,B.Yancey,H.Trahan,andR.Ayass,
Table III. It can be seen that even with 75% pre-fault voltage “Loadmodelingimpactonsystemstabilityandguidelinesforstability
at the faulted node, or, a better voltage within the miner’s studiesonanislandedsystemwithgrid-forminginverters,”in2023IEEE
PowerandEnergySocietyGeneralMeeting(IEEE-PESGM),2023.
premises, all the miners are not able to ride through. While
[13] “Zeus Mining Crypto Mining Pro: Antminer APW8
not shown for brevity, it has also been observed that for a Power Supply Repair Guide [EN],” Published in 27, July
larger sag duration, more and more miners are unable to ride 2010, [Online]. Available: https://www.zeusbtc.com/manuals/
through even with 75% pre-fault voltage. Antminer-APW8-Power-Supply-Repair-Guide.asp.
[14] J.PrakashandI.Sarkar,“ComparisonofPFCConverterTopologyfor
Electric Vehicle Battery Charger Application,” in 2022 IEEE Students
ConferenceonEngineeringandSystems(SCES),2022.
IV. CONCLUSION
[15] P. M. Anderson, B. L. Agrawal, and J. E. Van-Ness, Subsynchronous
Thispaperprovidesadetailedswitching-basedEMTmodel ResonanceinPowerSystems. IEEEPowerEngineeringSociety,1989.
[16] M.H.J.Bollen,UnderstandingPowerQualityProblems:VoltageSags
of a typical cryptocurrency mining facility based on an active
andInterruptions,ser.IEEEPressSeriesonPowerEngineering. New
power factor correction (PFC) boost converter first by validat- York:IEEEPress,2000.
ing with a laboratory-based crypto-mining power supply, and [17] U.Karaagac,H.Ashourian,I.Kocar,A.Stepanov,H.Gras,andJ.Mah-
seredjian, “PV Park Models in EMTP,” Published in 10, June 2021,
then by integrating and testing it with a small-scale transmis-
Available: https://emtp.com/documents/EMTP%20Documentation/doc/
sionsystemwithaPVfarm.Theefficacyoftheminingfacility devices-2022/Renewables/PV Park Models.pdf,Tech.Rep.,2021.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloaded on September 10,2026 at 10:29:49 UTC from IEEE Xplore. Restrictions apply.