The 2014 International Power Electronics Conference
Adaptive Thermal Control for Power Fluctuation to
Improve Lifetime ofIGBTs in Multi-MW Medium
Voltage Wind Power Converter
|     |     |          |     | i                  |     |     |            |            |     | 2   |        | i   |     |     |
| --- | --- | -------- | --- | ------------------ | --- | --- | ---------- | ---------- | --- | --- | ------ | --- | --- | --- |
|     |     | Gen Chen |     | ,  Jianwen Zhang\  |     |     | Miao Zhu\  | Ningyi Dai |     | ,   | Xu Cai |     |     |     |
1 Wind Power Research Center, Department of Electrical Engineering,
|     |     |     |     |     | Shanghai Jiao Tong University,  |     |     | China  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
2 Department of Electrical and Computer Engineering,
University of Macau, China
Abstract-Multi-MW wind power converter's reliability is a  junction  temperature  variation,  affecting  its  reliability  and
key issue for the whole wind power generation system. Due to  lifetime. According to an industry-based survey of reliability
wind power  fluctuation,  IGBT's handling power is  fluctuating  in power electronic converters, power semiconductor devices
| largely  and  | rapidly,  | which  | will  | cause  a  | large  | junction  |     |     |     |     |     |     |     |     |
| ------------- | --------- | ------ | ----- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
are ranked as the most fragile components [4].
temperature variation of IGBT. Thermal stress is the main factor
The reliability and lifetime of power converter in research
| affecting IGBT's lifetime.  |     | In this paper,  |     | the adaptive thermal  |     |     |                   |     |      |      |          |       |            |             |
| --------------------------- | --- | --------------- | --- | --------------------- | --- | --- | ----------------- | --- | ---- | ---- | -------- | ----- | ---------- | ----------- |
|                             |     |                 |     |                       |     |     | and  application  |     | are  | one  | of  the  | most  | important  | things  to  |
control is proposed to improve IGBT's lifetime during power
consider due to its link with the overall system. In [7], the
| fluctuation.  | In  the  adaptive  |     | thermal  | control,  | different  | vector  |     |     |     |     |     |     |     |     |
| ------------- | ------------------ | --- | -------- | --------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
reliability calculation of multi-level converter is presented and
sequences are adopted adaptively to power fluctuation levels. The
the short-circuit fault tolerance capability of several topologies
| IGBT's  junction  | temperature  |     | variation  | can  | be  reduced  | in  |     |     |     |     |     |     |     |     |
| ----------------- | ------------ | --- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comparison with normal vector sequence.  According to power  are compared. A redundancy design is a good way to improve
fluctuation level and IGBT's junction temperature, the relevant  the  converter's  reliability.  In  [6],  a  lifetime  estimation
vector  sequence is adopted.  The adaptive thermal control can  technique for voltage source inverters is presented. Reliability
relieve  IGBT's thermal stress and improve its lifetime during  issues are more and more considered in all fields,  ranging
wind power fluctuation. The improvement of IGBT's lifetime can
from industry field to research institutes.
| also  improve  | wind  power        | converter  |             | and  system's  |              | reliability.  |            |     |         |            |     |          |         |                |
| -------------- | ------------------ | ---------- | ----------- | -------------- | ------------ | ------------- | ---------- | --- | ------- | ---------- | --- | -------- | ------- | -------------- |
| Finally,       | the  MATLAB/PLECS  |            | simulation  |                | is  carried  | out.          |            |     |         |            |     |          |         |                |
|                |                    |            |             |                |              |               | Regarding  |     | IGBT's  | lifetime,  |     | thermal  | stress  | is  the  main  |
Simulation results indicate the feasibility and advantages of the
proposed adaptive thermal control.  factor  affecting  it  [7-8].  Hence,  decreasing  and smoothing
IGBT's junction temperature is a good way to improve its
Keywords- adaptive  thermal  control,  power  fluctuation,  lifetime. IGBT's junction temperature is a reflection of its
lifetime improvement, wind power converter.  power losses. In [9], the reliability-cost model is established to
enable more accurate and effective design for the wind power
I.  INTRODUCTION  converter to reach the reliability requirements. In [10], the loss
Recently, with both land and offshore wind power rapid  and thermal redistributed modulation methods are introduced
|               |       |        |              |           |     |           | to  wind  | power  | converter  |     | which   | undergo    | low  | voltage  ride  |
| ------------- | ----- | ------ | ------------ | --------- | --- | --------- | --------- | ------ | ---------- | --- | ------- | ---------- | ---- | -------------- |
| development,  | wind  | power  | converters'  | capacity  |     | increase  |           |        |            |     |         |            |      |                |
|               |       |        |              |           |     |           | through.  | The    | different  |     | vector  | sequences  |      | have  good     |
rapidly. Nowadays, multi-megawatt (multi-MW) wind power
|     |     |     |     |     |     |     | performance  |     | on  | the  reduction  |     | of  junction  |     | temperature  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --------------- | --- | ------------- | --- | ------------ |
converters are commercialized [I]. In multi-MW level wind
variation, which can be promoted to other application fields.
power converter, both voltage and current level are high. At
So,  the adaptive thermal control of power fluctuation to
| the  same  | time,  the  power  |     | fluctuations  | of  | multi-MW  | wind  |     |     |     |     |     |     |     |     |
| ---------- | ------------------ | --- | ------------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
improve IGBT's lifetime and power handling ability in multi­
| power  converter  | are  | usually  | large,  | which  | will  cause  | high  |     |     |     |     |     |     |     |     |
| ----------------- | ---- | -------- | ------- | ------ | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
voltage and current fluctuations and significant power losses.  MW medium voltage wind power converter is proposed in this
|     |     |     |     |     |     |     | paper.  | In  the  | proposed  |     | adaptive  | thermal  | control,  | different  |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------- | --- | --------- | -------- | --------- | ---------- |
Large voltage or current fluctuations affect the reliability of
|     |     |     |     |     |     |     | vector  | sequences  |     | are  adopted  |     | adaptively  | to  | the  power  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ------------- | --- | ----------- | --- | ----------- |
IGBT and the power converter. The wind power converter is a
crucial part of the wind power generation system and it has a  fluctuation levels. The IGBT's junction temperature variation
can be reduced in comparison with normal vector sequence.
direct impact on the reliability of the whole system [2-3]. Due
|     |     |     |     |     |     |     | According  | to  | power  | fluctuation  |     | level  and IGBT's junction  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------------ | --- | --------------------------- | --- | --- |
to the wind power fluctuation, IGBT's power handling power
|     |     |     |     |     |     |     | temperature,  |     | the  relevant  |     | vector  | sequence  | is  | adopted.  The  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ------- | --------- | --- | -------------- |
ability is fluctuating largely and rapidly, which causes a high
adaptive thermal control can relieve IGBT's thermal stress and
This work was supported by the National High Technology Research and  improve  its  lifetime  during  wind  power  fluctuation.  The
Development of China 863 Program under Grant 20 I 2AA050203, Macau  improvement ofIGBT's lifetime can also improve wind power
Science and Technology Development Fund (FDCT) under Grant 072/20121
converter and the whole system's reliability. The proposed
A3, Shanghai Jiao Tong University and Fuji Electric Co. Ltd joint project.
Author9iz7e8d -li1ce-n4s7ed9 u9s-e2 li7m0ite5d- t0o/: 1Te4c/h$n3is1ch.e0 0Un ©ive2rs0it1ae4t  MIEueEncEhe n. Downloa1d4e9d6  on September 14,2026 at 08:55:23 UTC from IEEE Xplore.  Restrictions apply.

The 2014 International Power Electronics Conference
adaptive thermal control is of great significance in multi-MW  sector I.  Normal  modulation  method  work  well  when  the
| wind power converter.  |     |     |     |     |     | power level is relatively steady.  |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
In this paper, space vector sequences and thermal model are
d e s c r ib e d   i n   s e c t i o n   I I .   T h e   a d a p t i v e   t h e r m a l   c o n t r o l  i s   ···I
|     |     |     |     |     |     |     |     | • r    .. .... .... | .. .. .. ......I ,.      .. .. | ....  _  ........ �I | ..   .......... .. ........ ...  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ------------------------------ | -------------------- | -------------------------------- |
p r e s e n te d   i n   d e t a i l   i n   s e c t i o n   I I I .   T h e   s i m u l a ti o n   r e s u l t s   a r e   •···•       •   I,   ,   ,,..,   I
|     |     |     |     |     |     |     |     |     | .",, | , ' | .,,,      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --------- |
s h o w n   in   s e c t i o n   I V .  F i n a l l y ,  s o m e   o b t a i n e d   c o n c l u s i o n s   a r e   f ....  .. u  I ,
|     |     |     |     |     |     |     | A   | u u |  .. ..-  - u u | u  .. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | --- |
summarized in section V.
|     |     |     |     |     |     |     |     |     | T   | i   | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t ......................r  ................................ 1.. ........ 1.. ........ ..
II.  SPACE VECTOR SEQUENCES AND THERMAL MODEL  t----- ; ----------------i-----i------
___ MOO
| In multi-MW medium wind power converter the three-level  |     |     |     |     |     |     |     |           |                     |                             | i               |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | --------------------------- | --------------- |
|                                                          |     |     |     |     |     |     | B   | t - - - - | - r - - - - - � --- | - - - - - - - - - - - - - + | --- - --- - - - |
NPC  topology  is  widely  applied.  In  the  three-level  space  ,,•     "II   ,f,
  rI,
|     |     |     |     |     |     |     |     | I · · · · | ·� : : : : | : : : : : : : : : : : : : r | + · ··   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --------------------------- | -------- |
vector modulation, all the vectors can be divided into three
| categories:  | long  | (purple),  medium  | (blue)  | and  small  | (red)  |     |     |     |     |     |     |
| ------------ | ----- | ------------------ | ------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
vectors except for the zero vectors, as shown in Fig.l.
|     |     |     |     |     |     |     |     |                             | · ..t:  -..-..-.......... - | .. .... .... ....--t........  ........ �: -.......... ·  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --------------------------- | -------------------------------------------------------- | --- |
|     |     |     |     |     |     |     |     | :�  ....................... |                             | - - -                                                    |     |
c
|     |     |     |     |     |     |     |     |                              | ' l | I,, |           |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --------- |
|     |     |     |     |     |     |     |     | r ··   ....................  |     | :   |   ..:     |
FNNOO Foopoooo4oo�ONN
|     |     |     |     |     |     | Fig.3 Normal vector sequence in area A  |     |     |     |     | of sector I  |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | ------------ |
I
|     |     |     |     |     |     | In  wind                        | power  | field,  | power  | fluctuation  | is  one  of  the  |
| --- | --- | --- | --- | --- | --- | ------------------------------- | ------ | ------- | ------ | ------------ | ----------------- |
|     |     |     |     |     |     | characteristics of wind power.  |        |         |        | Large power  | fluctuations of   |
wind power will lead to the thermal stress sever. Therefore,
novel modulation method is of great importance. In [10], a
series of new modulation methods are presented to relocate the
thermal loading among power devices when the 3L-NPC wind
power inverter undergo low voltage ride through operation. In
this paper, one of the modulation methods [10] is adopted for
power fluctuation. FigA shows the optimized vectors sequence.
Fig.l Space vectors for three-level NPC topology
|     |     |     |     |     |     |     |     | •   | I   |     | •  I  I  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
According to the vectors shown in Fig.l, the small vectors
have redundant ones, that is, the P vectors and the N vectors.  (nmnttl  iii  I'- (tmn ( n.
Different vectors lead to different power devices turning on or  A  i  i 1 . ..  u-t-n-lun"1u"u .  1 i  i
off. Thus, the power devices' thermal stress can be relieved,  t----------t-t-------t---"i""--t-------j--; -----j-----.
which lay the fundamental of adaptive thermal control.
|             |      |                                             |     |     |     |     | t----------t-t-------.  |     |     | :  .--------j--j-----j-----.  |      |
| ----------- | ---- | ------------------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | ----------------------------- | ---- |
| Generally,  | the  | full vectors in Fig.l are divided into six  |     |     |     |     |                         |     |     |                               |      |
|             |      |                                             |     |     |     |     | t-----                  | ..  |     | .                             | ...  |
sectors. Take sector I as example, shown in Fig.2.
B
V;4PPN
c
....
D  :; _
_
|     |     | PPO V,  _____________ : | V7 PON    |     |     |     |     |     |     |     |     |
| --- | --- | ----------------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | OON ...                 | ..-.. '"  |     |     |     |     |     |     |     |     |
fNNOo�ptooo9ppo!ppoipooorOpO�ONN
|     |     | A, "'       | e " /"   .....  ..  |     |     |     |     |       |     |     |            |
| --- | --- | ----------- | ------------------- | --- | --- | --- | --- | ----- | --- | --- | ---------- |
|     |     | •••         |   ,                 |     |     |     |     |       |     |     |            |
|     |     | •••• A'   � | ��..  . / B  .. ..  |     |     |     | !   | .. !  |     | !   | ;l1li  ..  |
•
|     |     |     |      |     |     |     | :  III  | Ts/2  | :   | :   | :  Ts/2  |
| --- | --- | --- | ---- | --- | --- | --- | ------- | ----- | --- | --- | -------- |
|     |     | Vo  | V;3  |     |     |     |         |       |     |     |          |
v;
|     |     | PPP  | POO  PNN  |     |     |     | j�  |     | �   | �!�  | �  �  |
| --- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | ---- | ----- |
|     |     | 000  | ONN       |     |     |     |     |     |     |      |       |
NNN
Fig.2 Space vectors in sector I  FigA The optimized vectors sequence
Fig.S shows the thermal models for IGBT and diode. Fig.6
| In  the  | area  | A  of  sector I,  | the  reference  | vector  | Vrej  is  |     |     |     |     |     |     |
| -------- | ----- | ----------------- | --------------- | ------- | --------- | --- | --- | --- | --- | --- | --- |
I  is the thermal model of the impedance from junction to case,
| synthesized  | by  | vector  | And  the  | normal  | vector  |     |     |     |     |     |     |
| ------------ | --- | ------- | --------- | ------- | ------- | --- | --- | --- | --- | --- | --- |
|              |     | Va,     | VI,  V2.  |         |         |     |     |     |     |     |     |
sequence is  which is a detail description of  ZTIDO-c)'  It is a four-layer Foster
aNN � OON � 000 � POO � 000 � OON
RC network.
| � aNN.  | Fig.3 shows the normal vector sequence in area A  |     |     |     | of  |     |     |     |     |     |     |
| ------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
I
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloa1d4e9d7  on September 14,2026 at 08:55:23 UTC from IEEE Xplore.  Restrictions apply.

The 2014 International Power Electronics Conference
IGBT with Diode  Ao: failure rate reference at 1j=100 °C, depends on the
|     |     | �   |     |     | technological class of the device and package;  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
T
J
: for 1j different from 100°C with Arrhenius law[5];
7r/
|     | IGBT  | Diode  |     |     |     |     |     |     |     |     |
| --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     | ZTU-c)  | ZTU-c)  |     |     |     |     |              |     |     |
| --- | --- | ------- | ------- | --- | --- | --- | --- | ------------ | --- | --- |
|     |     |         |         |     |     |     |     | 4640( � ___  | )   |     |
373  Tj+373
|     |     | Tc  | Tc  |     |     |                  | 7r1 =e   |        |            |             |
| --- | --- | --- | --- | --- | --- | ---------------- | -------- | ------ | ---------- | ----------- |
|     |     |     |     |     |     | :  acceleration  | voltage  | break  | down  for  | the  drain­ |
7rs
|     |     | Z1'(c_")  | Z1'(c_")  |     |     |     |     |     |     |     |
| --- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
source by the empirical relation [5];
|     |     |     |     |     |     |     |     | 1.7( Vee off  | siale |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- |
)
Vce_raling
7rs = 0.22e
|     |     |     |     |     |     | and  7r q : the environmental and the quality factors of  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | --- |
7rE
the device.
Fig.5 The thermal models for IGBT and diode  According  to  equation  (1)-(5),  the  control  of  IGBT's
junction temperature is fundamental to improve its reliability
and lifetime.
|               |     |     |     |     |     | III.  ADAPTIVE THERMAL CONTROL FOR LIFETIME    |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- |
| [GBT / Diode  |     |     |     |     |     | IMPROVEMENT OF IGBTs DURING POWER FLUCTUATION  |     |     |     |     |
In multi-MW wind power converter, the three-level NPC
Fig.6 Thermal model of impedance from junction to case  topology is widely applied, as shown in Fig.7. In multi-MW
medium voltage wind power converter, the IGBT's handling
|                                                   |     |     |     |      | voltage  | and  current  | are  large,  | which  | make  | its  junction  |
| ------------------------------------------------- | --- | --- | --- | ---- | -------- | ------------- | ------------ | ------ | ----- | -------------- |
| The semiconductor's mean junction temperature Tj  |     |     |     | can  |          |               |              |        |       |                |
-IGBT
be estimated by equation (1 )-(2).  temperature increase rapidly. As the junction temperature and
|     |     |     |     |     | IGBT's lifetime are linked,  |     |     | the control of IGBT's junction  |     |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | --- | ------------------------------- | --- | --- |
temperature is of great importance in industry applications.
(1)
(2)
R,hJC, R,hCH, RlhHA
| Where,  |     | are the thermal resistance from  |     |     |     |     |     |     |     |     |
| ------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
junction to case, case to heater, heater to ambient, respectively
| and  TA  is the ambient temperature of converter.  |     |     |     | is the  |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
PIOI
power losses ofIGBT and Diode.
(3)
(4)
�Ol = PrGST + PDlOde
Usually, the power semiconductor device has a long useful
time. So, its failure rate during the constant failure stage can
| be denoted as  | and its general reliability function  |     |     | R(t)  can  |     |     |     |     |     |     |
| -------------- | ------------------------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
A
Fig.7 Three-level NPC topology
l [5].
be modeled as R(t) = e-.?t
The failure rate depends on the technological complexity of  According to the analysis in section II, in a given range, the
increase of junction temperature will directly act on IGBT's
the devices and the operation voltage, current and thermal
reliability which will be lower, so will its lifetime.
| condition.  | In  [5,  11-12],  | the  acceleration  | factors  | are  also  |     |     |     |     |     |     |
| ----------- | ----------------- | ------------------ | -------- | ---------- | --- | --- | --- | --- | --- | --- |
considered as equation (5), which can make the failure rate  In order to relieve IGBT's thermal stress, adaptive thermal
control is proposed. It behaves on the lifetime improvement of
more accurate.
IGBTs in multi-MW mediwn voltage wind power converter
|         |     |     |     | (5)  | during                      | power  fluctuation. The  |     | scheme  | of  adaptive  | thermal  |
| ------- | --- | --- | --- | ---- | --------------------------- | ------------------------ | --- | ------- | ------------- | -------- |
| Where,  |     |     |     |      | control is shown in Fig.8.  |                          |     |         |               |          |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloa1d4e9d8  on September 14,2026 at 08:55:23 UTC from IEEE Xplore.  Restrictions apply.

The 2014 International Power Electronics Conference
Adaplive Thermal Con/rol
|     |     |     |     |     |     |     |     |                | I,               | I,          | I,              | ,                 | •               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------------- | ----------- | --------------- | ----------------- | --------------- | --- |
|     |     |     |     |     |     |     |     | 180 •.••.••.•• | :.   ••.••.••. + |  .......... | : .  .........  | . +    .......... | . :    . ... .  |     |
|     |     |     |     |     |     |     |     |                |                  | ,II         | ,II             | ,I,               | .,•             |     |
Vector
Sequence
Selection
.. J
80 ••••.••. ..:-••.••.••. + ........ ..:-.......... : ......... , ...... .
|     |                                           |     |     |     |     |     |     |     | ,II,I                         | ,II,I         | ,II,I           | .I,           | .,•          |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | ------------- | --------------- | ------------- | ------------ | --- |
|     | Fig.8 Scheme of adaptive thermal control  |     |     |     |     |     |     |     |                               |               |                 | .I            | .,           |     |
|     |                                           |     |     |     |     |     |     |     | 60 .......... '.   .........  | '  .......... | '.   .........  | '  .........  | '  .......   |     |
|     |                                           |     |     |     |     |     |     |     | 0.8  0.85                     | 0.9           | 0.95            | 1             | 1.05         |     |
Time(s)
In the proposed adaptive thermal control, different vector
| sequences  | are  | adopted  | adaptively  | to  act  | against  | power  |     |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ----------- | -------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.10 Junction temperature of inner IGBT under
tluctuations. Thus, the junction temperature variation can be
conventional control
| reduced    | and  | smoothed  | in  comparison  | with        | normal  | vector  |     |     |     |     |     |     |     |     |
| ---------- | ---- | --------- | --------------- | ----------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| sequence.  | The  | power     | tluctuation     | level  and  | the     | IGBT's  |     |     |     |     |     |     |     |     |
junction temperature are estimated. Then accordingly vector
| sequence  | is  selected.  | Adaptive  |     | thermal  control  | can  | relieve  |     |     |     |     |     |     |     |     |
| --------- | -------------- | --------- | --- | ----------------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
IGBT's thermal stress and improve its lifetime during power
tl uctuati on.
The improvement of IGBT's lifetime can also improve the
wind power converter and the whole system's reliability. The
proposed adaptive thermal control is of great significance in
multi-MW wind power converter.
|     |     | IV.  | SIMULATION RESULTS  |     |     |     |     |     | I   | I   | I   | I   | I   |     |
| --- | --- | ---- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
70  ......... � ......... � ......... � ......... � ......... � ........ .
|     |     |     |     |     |     |     |     |     | I   | I,I    '-----� | I,I    ' | I,I'     | I,I    '----�  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | -------- | -------------- | --- |
According to the analysis in section III, the simulation is  ,I'
|     |     |     |     |     |     |     |     |     | 60�--� ----� |     | ---L | ---- | �   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ---- | --- | --- |
carried out in MAT  LAB/PLECS to validate the feasibility of  0.95  1.05  1.1  1.15  1.2
Time(s)
| the  proposed  |          | adaptive    | thermal  | control.  Fig.9  | shows       | the  |     |     |     |     |     |     |     |     |
| -------------- | -------- | ----------- | -------- | ---------------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| scheme         | of  the  | simulation  | circuit  | and  the         | parameters  | for  |     |     |     |     |     |     |     |     |
Fig.II Junction temperature of inner IGBT under
simulation are shown in Table 1.
adaptive thermal control
When the power tluctuation is at time t=Is, the adaptive
|     |     |     |     |     |     |     | thermal  | control  | can  | reduce  | the  | inner  | IGBT's  | junction  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ------- | ---- | ------ | ------- | --------- |
temperature maximum variation from 53°C to 37.5°C.
In [6], the IGBT's number of power cycles to failure,
Nf
can be estimated by equation (6) and the results are shown in
|     |     |     |     |     |     |     |     |     |     |     | (   | )-4.367  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
Table 2.
0 488�T;)'
|     |     |     |     |     |     |     |     |     | N    =0.5x |     | ·   |     |     | (6)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ---- |
f
606.1724
Fig.9 Scheme of simulation circuit  TABLE 2 NF UNDER DIFFERENT CONTROL
TABLE I PARAMETERS FOR SIMULATION
|     |             |     |     |        |     |     |     | Conventional control      |     |     | 53°C    |     | 4.8009*10 | 5   |
| --- | ----------- | --- | --- | ------ | --- | --- | --- | ------------------------- | --- | --- | ------- | --- | --------- | --- |
|     | Parameters  |     |     | Value  |     |     |     |                           |     |     |         |     |           |     |
|     |             |     |     |        |     |     |     | Adaptive thermal control  |     |     | 37.5°C  |     | 2.1749*10 | 6   |
|     | DC Voltage  |     |     | 5400V  |     |     |     |                           |     |     |         |     |           |     |
Rated grid voltage  From Table 2, it is obvious that the adaptive thermal can
3.3kV
(line to line)  improve the IGBTs' lifetime, the wind power converter and
|     | Filter inductance  |     |     | 3mH  |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the whole system's reliability greatly.
IGBT modules
I MBII 200UE-330
The  power  steps  up  at  the  time  Is,  and  the junction  V.  CONCLUSION
temperature of inner IGBT under conventional control and
|           |          |          |            |             |      |            |     | In  this  | paper,  the  | adaptive  | thermal  |     | control  | for  power  |
| --------- | -------- | -------- | ---------- | ----------- | ---- | ---------- | --- | --------- | ------------ | --------- | -------- | --- | -------- | ----------- |
| adaptive  | thermal  | control  | is  shown  | in  Fig.lO  | and  | Fig. 11 ,  |     |           |              |           |          |     |          |             |
tluctuation to improve IGBT's lifetime and power handling
respectively.
|     |     |     |     |     |     |     | capability  |     | in  multi-MW  |     | medium  | voltage  | wind  | power  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ------- | -------- | ----- | ------ |
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloa1d4e9d9  on September 14,2026 at 08:55:23 UTC from IEEE Xplore.  Restrictions apply.

The 2014 International Power Electronics Conference
converter is analyzed. In the proposed adaptive thermal
control, different vector sequences are adopted adaptively to
act against the power fluctuation. The IGBT's junction
temperature variation can be reduced in comparison with
normal vector sequences. According to power fluctuation level
and IGBT's junction temperature, the relevant vector sequence
is adopted. The adaptive thermal control can relieve IGBT's
thermal stress and improve its lifetime during wind power
fluctuation. The improvement of IGBT's lifetime can also
improve wind power converter, the whole system's reliability
and its effectiveness. The proposed adaptive thermal control is
of great significance in multi-MW wind power converter.
ACKNOWLEDGMENT
The authors gratefully acknowledge the contributions of
Fuji Electric Co. Ltd for the joint project support.
REFERENCES
[II M. Liserre, R. Cardenas, M. Molinas and J. Rodriguez,"Overview of
multi-MW wind turbines and wind parks," iEEE Trans. on industrial
Electronics, vol.58, no.4, pp. 1081-1095,2011.
[21 K. Xie, Z. Jiang and W. Li, "Effect of wind speed on wind turbine power
converter reliability," iEEE Trans. on Energy ConverSion, vol.27, no.l,
pp. 96-104,2012.
[31 F. Blaabjerg, M. Liserre and K. Ma, "Power Electronics Converters for
Wind Turbine Systems," iEEE Trans. on industry Applications, vol.48,
no.2, pp. 708-719,2012.
[41 S. Yang, A. Bryant, P. Mawby, D. Xiang, L. Ran and P. Tavner, "An
industry-based survey of reliability in power electronic converters,"
iEEE Trans. on industry App/ications, vol.47, no.3, pp. 1441-1451,2011.
[5] F. Richardeau and L. Pham, "Reliability Calculation of Multilevel
Converters - Theory and Applications," iEEE Trans. on industrial
Electronics, vol.60, no. 10, pp. 4225-4233, 2013.
[6] H. Huang and P. A. Mawby, "A Lifetime Estimation Technique for
Voltage Source Inverters," iEEE Trans. on Power Electronics, vol.28,
no.8, pp. 4113-4119, 2013.
[7] l. F. Kovacevic, U. Drofenik and J. W. Kolar, "New physical model for
lifetime estimation of power modules," in Proc. international Power
Electronics Conference (iPEC), 2010, pp. 2106-2114.
[8] C. Busca, "Modeling lifetime of high power IGBTs in wind power
applications -An overview," in Proc. iEEE international Symposium on
industrial Electronics (iSlE), 2011, pp. 1408-1413.
[9] K. Ma and F. Blaabjerg, "Reliability-cost models for the power
switching devices of wind power converters," in Proc. 3rd IEEE
International Symposium on Power Electronics for Distributed
Generation Systems (PEDG), 2012, pp. 820-827.
[10] K. Ma and F. Blaabjerg, "Loss and thermal redistributed modulation
methods for three-level neutral-point-c1amped wind power inverter
undergoing Low Voltage Ride Through" in Proc. iEEE international
Symposium on industrial Electronics (iSiE), 2012, pp. 1880-1887.
[11] F. Chan and H. Calleja, "Reliability Estimation of Three Single-Phase
Topologies in Grid-Connected PV Systems," iEEE Trans. on industrial
Electronics, vol.58, no. 7, pp. 2683-2689, 2011.
[12] Reliability Prediction of Electronic Equipment, Military Handbook 217-
F,Dept. Defense, Arlington, VA, 1991.
Authorized licensed use limited to: Technische Universitaet Muenchen. Downloa1d5e0d0 on September 14,2026 at 08:55:23 UTC from IEEE Xplore. Restrictions apply.