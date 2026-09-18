IEEETRANSACTIONSON[JOURNALNAME] 1
Source Side Mitigation of AI Datacenter Power
Fluctuations with a Hybrid Energy Storage System
and Residual Differentiable Predictive Control
Haiyang You, Chengwei Lou, and Jin Yang
Abstract—The rapid growth of hyperscale AI datacenters A key source of these variations is the workload execution
introducesstructured,workload-drivenactivepowerfluctuations dynamics of power-intensive AI computing. During large-
at the point of interconnection. These fluctuations appear to scale training jobs, many GPUs repeatedly alternate between
the grid as time-varying disturbance injections that cannot be computation-heavy phases and lower-utilization communica-
captured by conventional peak or average load representations. tion or synchronization phases [4]. Fine-tuning tasks and
To reduce the residual power disturbance before it propagates smaller concurrent jobs introduce additional variations at dif-
into the power system, this paper proposes a hybrid energy ferent power levels and timescales [5], [6]. When workload
storagesystemwithdifferentiablepredictivecontrol(HESS-DPC) phasesstart,end,ortransition,thenumberofdevicesoperating
framework for datacenter-side power smoothing. A workload- athighutilizationchangesaccordingly,producingactivepower
fluctuations at the facility level [7]. These fluctuations can
driven disturbance model is first established, representing the
create ramping stress and persistent disturbances at the point
point of interconnection load deviation as the superposition of
of interconnection, increasing the dynamic stress associated
training and fine-tuning workloads to capture the structured
with large-load integration [8], [9].
forcing inputs that can excite frequency dynamics. A frequency
decomposition rule-based controller then allocates this devia- Prior studies have examined datacenter power variability at
tion between a battery energy storage system (BESS) and a both the facility and grid levels. Measurement-based studies
supercapacitor (SC), assigning the energy-dominant component have characterized it at the facility level by using GPU-level
to the BESS and the fast-varying component to the SC. To power traces to construct aggregate demand profiles [10]–
overcome the anticipation and constraint limitations of fixed [13]. Beyond facility-scale characterization, recent reliability-
oriented studies indicate that the tightly synchronized, peri-
frequencydecomposition,aresidualdifferentiablepredictivecon-
odic compute cycles of AI training datacenters can induce
trol policy is trained offline to compute finite-horizon command
sustained load oscillations that propagate into the bulk power
correctionsaroundtherule-basedbaselinewhileenforcingaone-
system across a wide frequency range [14]. Because such
step safeguard. Simulations on the NPCC 140-bus system show
fast, structured variations are not captured by conventional
that HESS-DPC reduces grid-side residual deviations during
peak or average load descriptors, dedicated fast-timescale
workload transitions, improves SC state of charge sustainability
and electromagnetic-transient modeling of datacenter loads
over extended operation, and reduces generator peak-to-peak
has been advocated for grid-level studies [2], [15]. From a
frequency deviations by more than 80% across all monitored
modeling perspective, recent works represent AI datacenter
generators, with the worst affected generator response falling
loads as structured forcing inputs in power-system dynamic
from 15.1 mHz to 1.3 mHz. These results confirm that local
studies and show that these variations can sustain oscilla-
activepowersmoothingatthedatacenterpointofinterconnection
tory responses rather than only produce isolated transient
can substantially mitigate frequency disturbances caused by AI
events [16]. Ko et al. [17] further investigate the use of
workloads.
hybrid energy storage to reduce datacenter-induced ramping
and fluctuation stresses under prolonged stochastic training
Index Terms—AI datacenter, hybrid energy storage system,
cycles.Thesestudiesconfirmthatdatacenterpowervariability
differentiable predictive control, power smoothing, frequency
can have direct dynamic impacts on the bulk power system.
stability, large dynamic load
However,theyprimarilycharacterizeormodelthedisturbance,
and even where hybrid storage is considered for ramping and
fluctuation reduction [17], source-side suppression of residual
I. INTRODUCTION
active-power disturbances at the datacenter point of inter-
The rapid expansion of hyperscale AI datacenters is in- connection explicitly addressed under time-varying workload
troducing new grid-integration challenges for large loads in conditions remains insufficiently studied.
powersystems.Inconventionalplanningandadequacystudies, The practical importance of this source-side mitigation gap
a large customer is often characterized by aggregate demand is reinforced by recent reliability guidance from the North
descriptors, such as peak demand or representative load pro- American Electric Reliability Corporation (NERC) on emerg-
files. These abstractions are useful for steady-state capacity ing large loads. NERC notes that some large loads, including
assessment, but they may fail to capture short-term active computationalloads,canexhibitsecond-to-secondandminute-
power variations and fast ramping behaviors that enter the to-minute power oscillations together with fast ramping ca-
grid as dynamic disturbances [1]–[3]. For AI datacenters, pability, which complicates short-term operational forecasting
the grid impact is therefore determined not only by the for system operators. Such fast load variations can produce
connected power level, but also by the magnitude, ramp rate, demandswingswithinsecondsorminutesthatstressbalancing
and timescale of the resulting power variations. reserves and frequency-control resources, while abrupt load
changes or disconnections may cause system imbalance and
frequency instability. To address these risks, NERC recom-
H. You and J. Yang are with the James Watt School of Engineering,
UniversityofGlasgow,GlasgowG128QQ,UK.C.LouiswiththeCollegeof mends incorporating large-load variability into balancing as-
InformationandElectricalEngineering,ChinaAgriculturalUniversity,Beijing sessmentssothatsufficientregulatingcapabilityandcoordina-
100083,China. tioncanbemaintainedunderexistingcontrol-performanceand
6202
nuJ
03
]YS.ssee[
2v96840.6062:viXra

IEEETRANSACTIONSON[JOURNALNAME] 2
allocation does not explicitly anticipate future disturbances or
jointlyoptimizeresidualpowerreductionanddeviceoperating
constraints over a prediction horizon.
These limitations motivate the incorporation of a predictive
refinement layer. DPC offers such a mechanism without re-
quiring an online optimization problem to be solved at every
sampling instant [25]. It combines a known prediction model
withanofflinetrainingprocedurebasedonamodel-predictive-
control (MPC)-inspired finite-horizon objective [26]. In this
work,DPCisadoptedinresidualform:ratherthangenerating
the complete BESS and SC commands directly, it computes
finite-horizon corrections around the rule-based HESS com-
mands. This design preserves the physical BESS/SC alloca-
tion structure, limits the scope of the correction task, and
improves performance in operating regions where the fixed
baseline is most limited [27], [28]. The training objective
penalizes grid-side residual power, command variation, and
violationsofpower,ramp-rate,andstate-of-chargelimits[29],
[30]. The proposed HESS-DPC framework first extracts the
workload-driven active power deviation, applies frequency-
based BESS/SC allocation, and then uses residual DPC to
reduce the grid-side residual. The resulting disturbance is in-
jectedintotheNortheastPowerCoordinatingCouncil(NPCC)
140-bus system to quantify the reduction in workload-driven
generator frequency deviations. The overall source-side miti-
gation pathway is illustrated in Fig. 1. The main contributions
Fig. 1: Source-side active power smoothing framework for AI
of this paper are summarized as follows.
datacenter fluctuations.
• A source-side disturbance model is developed to
characterize the active power forcing input imposed
by AI datacenter workloads. The datacenter active
ACE-limitrequirements.ForAItrainingdatacenters,itfurther power deviation from its mean value is modeled as the
identifiesmitigationoptionssuchassoftwaremitigation,GPU disturbanceinputandconstructedfromdominanttraining,
power smoothing, and rack-level energy storage, and points smaller training, and fine-tuning workloads, retaining the
to interconnection requirements based on oscillation attenu- structured fluctuation components relevant to generator
ation metrics, real-power amplitude variation thresholds, and frequency dynamics.
amplitude-frequencylimitsforoscillatorydemand[18].These • A frequency-decomposition HESS interface is es-
recommendationsdirectlymotivateapoint-of-interconnection- tablished for point-of-interconnection smoothing. The
level smoothing mechanism that suppresses residual active- workload-driven disturbance is separated into energy-
powerdisturbancesatthedatacenter-side,therebyreducingthe dominant and fast-varying components and allocated to
burden imposed on grid-side balancing and frequency-control the BESS and SC, respectively, under power, ramp-rate,
functions. and state-of-charge constraints.
While NERC identifies device-level options such as GPU • A residual DPC strategy is proposed to compen-
power smoothing and rack-level storage, this work focuses on sate for the limitations of fixed rule-based HESS
a hybrid energy storage system (HESS) installed at the data- allocation. The policy learns finite-horizon corrections
centerboundary.Thisboundary-levelinterfacecanoperateau- around the rule-based BESS/SC commands through a
tonomouslyatthefacilitylevelwithoutrequiringtransmission- differentiable HESS rollout with an MPC-inspired loss,
level coordination or upstream control modifications [2]. The improvingsmoothingduringworkloadtransitionintervals
hybrid form is motivated by the spectral characteristics of while preserving the physical baseline allocation.
the datacenter power disturbance. Because the disturbance • The grid-level impact of source-side smoothing is
contains both a slow, energy-dominant component and a fast, evaluated in the NPCC 140-bus system. The residual
power-dominant component [19], a single storage technology disturbance after HESS-DPC compensation is injected
is not well suited to handle both within practical operating into the bulk-system model to quantify the attenuation
limits [4]. Battery energy storage systems (BESSs) provide a of workload-driven generator frequency deviations.
larger energy buffer but are less suitable for sustained high- The remainder of this paper is organized as follows. Sec-
frequency tracking [20], whereas supercapacitors (SCs) can tion II presents the datacenter load model and the HESS
respond quickly to transient deviations but cannot sustain model. Section III develops the rule-based baseline controller
long-durationcompensationduetotheirlimitedenergycapac- and the residual DPC method. Section IV presents the NPCC
ity [21]. A HESS combines these complementary properties 140-bussimulationstudies,andSectionVconcludesthepaper.
and provides a structured local interface for reducing AI
datacenter power fluctuations at the source. II. DATACENTERLEVELLOADAGGREGATION
Rule-based HESS controllers provide a natural first step Theactivepowerdemandatthedatacenterpointofintercon-
for this smoothing problem [22]. A frequency-decomposition nectionisdrivenbytheaggregateofconcurrentlyexecutingAI
controller can assign the fast component of the datacenter workloads. These workloads exhibit periodic phase structures
disturbance to the SC and the remaining component to the whose superposition produces sustained fluctuations at the
BESS[23].Suchastructureisphysicallymeaningfulandeasy facilitylevel.Followingthestochasticworkloadmodelin[19],
to implement, but its filter settings and allocation parameters which characterizes the power level statistics of training and
are typically selected for a prescribed operating condition. fine-tuning workloads from GPU profiling measurements, the
When the workload profile changes in amplitude, frequency consideredoperatingconditionconsistsofonedominantlarge-
content, or ramping pattern, the same fixed controller may scale training workload, one smaller training workload, and
leave non-negligible residual deviations, especially during one fine-tuning workload. The aggregate computational load
workload transition intervals [24]. Moreover, fixed rule-based profile is written as

IEEETRANSACTIONSON[JOURNALNAME] 3
discharging power delivered to compensate an above-baseline
P (t)=Ptr(t)+Ptr(t)+Pft(t), (1) demand deviation, while negative storage power denotes
Σ L S
charging associated with a below-baseline deviation. Perfect
whereP
L
tr,P
S
tr,andPft denotethedominanttraining,smaller compensationcorrespondstoP
B
(t)+P
SC
(t)=∆(t),inwhich
training, and fine-tuning profiles, respectively. The smaller case the grid-side residual in (7) vanishes; the smoothing
workloads are scaled as P S tr 0 = κ S P L tr 0 and P 0 ft = κ F P L tr 0 . objective is to bring the realized output pair as close to this
The aggregate is then scaled to the target datacenter operating ideal as the device constraints permit.
level: Each storage unit is represented by a first-order power
P DC (t)=γ DC P Σ (t), (2) response model. For d ∈ {B,SC}, the transfer function from
the control input U (s) to the actual output power P (s) is
where γ > 0 is a case study scaling factor fixed before d d
DC
control design. This factor uniformly scales the aggregate
P (s) 1
workload profile to the target datacenter operating level while G (s)= d = , (8)
preserving the relative temporal structure of the underlying d U (s) τ s+1
d d
training and fine-tuning fluctuations. Thus, P (t) represents
DC
the equivalent active power demand of the datacenter as seen where τ is the response time constant. The complementary
d
from the grid side. This profile is used as the load input for characteristics of the two devices are summarized by
the subsequent HESS smoothing control.
The HESS is designed to compensate the fluctuation com- Ecap ≫Ecap, Rmax <Rmax, τ ≫τ . (9)
B SC B SC B SC
ponent of the datacenter load rather than its average demand.
In the simulation study, the baseline datacenter power is The storage units are required to operate within prescribed
computed offline over the evaluation horizon as power, ramp rate, and state of charge limits:
P D 0 C = T 1 (cid:90) 0 T P DC (t)dt, (3) (cid:12) (cid:12) (cid:12) d | P P d d ( ( t t ) ) (cid:12) (cid:12) (cid:12) | ≤ ≤P R d m m a a x x , , ( ( 1 1 0 1 ) )
where T is the simulation horizon. For a discrete time profile, (cid:12) dt (cid:12) d
this quantity is computed as
1 N (cid:88) −1 SoCm d in ≤SoC d (t)≤SoCm d ax, d∈{B,SC}. (12)
P0 = P [n], (4)
DC N DC TheserelationsdefinetheoperatingrequirementsoftheHESS
n=0
smoothing problem. Their specific treatment within the dis-
where N is the number of samples. In practical online oper- crete time predictive control formulation is introduced in
ation, this baseline may be replaced by a scheduled operating Section III.
reference or a slowly updated moving average estimate, while The reference powers are generated from ∆(t) through a
the controller continues to act on the corresponding deviation frequency-decomposition allocation.
signal.
A first-order low-pass filter extracts the slow component:
The datacenter power deviation is then defined by
∆(t)=P (t)−P0 , (5) ∆ LPF (s)=G LPF (s)∆(s), (13)
DC DC
or, in discrete time, where
2πf
∆[n]=P [n]−P0 . (6) G (s)= split . (14)
DC DC LPF s+2πf
split
A positive deviation ∆(t) > 0 indicates that the datacenter
demand exceeds its baseline level, whereas a negative devia- The complementary fast component is
tion ∆(t)<0 indicates that the demand is below the baseline
level. By construction, both ∆(t) and ∆[n] have zero mean ∆ (s)=∆(s)−∆ (s). (15)
HPF LPF
over the evaluation horizon, so the HESS is not required to
supply net energy. They are used as the disturbance inputs for Before being assigned to the SC, the fast component is
the HESS smoothing problem. further conditioned by a first-order shaping filter:
∆ (s)=G (s)∆ (s), (16)
A. HESS Modeling and Reference Power Allocation SC shape HPF
To mitigate the datacenter power deviation seen from the with
grid side, a hybrid energy storage system is installed at the 2πf
point of interconnection. The HESS consists of a battery G (s)= shape . (17)
energystoragesystem(BESS)andasupercapacitor(SC).The shape s+2πf shape
two devices have complementary characteristics: the BESS
offers a larger energy buffer suited to slower variations, while This shaping stage limits excessively sharp high-frequency
theSCprovidesafastertransientresponseforrapidlyvarying contentintheSCchannelwhilepreservingitsroleincompen-
components. sating fast disturbance variations. In the time domain, the SC
Throughout the mathematical formulation, the subscript B is assigned ∆ SC (t) and the BESS compensates the remainder
denotes the BESS branch, while the subscript SC denotes the ∆(t)−∆ SC (t),sothattheirsumequals∆(t)beforeprojection
supercapacitor branch. and device dynamics. Note that ∆(t) − ∆ SC (t) retains a
Following the discharged power positive convention, the residual fast component because G shape (s) provides approxi-
remaining power deviation supplied by the grid is expressed mate rather than perfect frequency separation; in practice, this
as residual has limited influence on the realized BESS output
P g d r e i v d (t)=∆(t)−P B (t)−P SC (t), (7) because the larger time constant τ B attenuates high-frequency
contentinP (t).Thediscrete-timerealization,includingZOH
B
where P (t) and P (t) are the actual output powers of the discretization and operating-limit treatment, is presented in
B SC
BESS and SC, respectively. Positive storage power denotes Section III.

IEEETRANSACTIONSON[JOURNALNAME] 4
III. POWERSMOOTHINGVIADIFFERENTIABLE To obtain an explicit and easily previewed baseline com-
PREDICTIVECONTROL mand sequence fully aligned with the predictive rollout, the
local command mapping is defined as
The discrete-time grid-side residual is
P g d r e i v d [k]=∆[k]−P B [k]−P SC [k], (18) U d 0[k]=P d ref,0[k], d∈{B,SC}. (27)
where P [k] and P [k] are the actual BESS and SC powers. By propagating the LPF (19) and shaping filter (22) over
Reducing B |Pdev[k]| SC means that a larger portion of the data- the previewed disturbance ∆ k:k+Np−1 from the current filter
grid state, the baseline controller generates the command sequence
center fluctuation is compensated locally by the HESS.
A two layer control structure is developed. The first layer T0 = (cid:8) U0 , U0 (cid:9) , (28)
is a rule-based HESS baseline controller that allocates the k B,0:Np−1 SC,0:Np−1
disturbance according to the complementary response char-
where the subscripts 0 : N − 1 denote local prediction
acteristicsoftheBESSandSC.Thesecondlayerisaresidual p
step indices within the window initialized at control instant
differentiable predictive control (DPC) policy that generates
k (globally k : k+N −1). This command sequence serves
finite-horizon command corrections around the baseline tra- p
as the reference around which the residual DPC correction is
jectory.Theresultingdesigncombinesphysicallyinterpretable
constructed.
frequency-based allocation with predictive refinement over a
short look ahead window.
B. Residual DPC Policy
A. Rule-Based HESS Baseline DPCusesadifferentiablefinite-horizonpredictionmodelto
optimize a closed-loop policy offline. The policy is written in
The baseline controller allocates ∆[k] between the BESS
residual form: instead of generating complete BESS and SC
andSCviafrequencydecomposition.Adiscrete-timelow-pass
commands directly, it outputs bounded command corrections
filter, obtained by ZOH discretization of (14) with sampling
that refine the rule-based baseline.
period T , extracts the slow component:
s At time step k, the policy maps a feature vector ξ to a
k
∆ [k]=α ∆ [k−1]+(1−α )∆[k], (19) sequence of residual corrections over the prediction horizon
LPF LPF LPF LPF
N :
p
with δU =π (ξ ), (29)
α
LPF
=e−2πfsplitTs. (20) 0:Np−1 Θ k
where Θ denotes the policy parameters. For prediction step j,
The corresponding fast component is
(cid:104)δU (cid:105)
∆ HPF [k]=∆[k]−∆ LPF [k]. (21) δU j = δU B,j , j =0,...,N p −1. (30)
SC,j
Before becoming the SC reference, the fast component is
The command used in the prediction rollout is
shaped by another first-order filter:
U =Π (cid:0) U0 +δU (cid:1) , d∈{B,SC}, (31)
∆ SC [k]=α shape ∆ SC [k−1]+(1−α shape )∆ HPF [k], (22) d,j d d,j d,j
where whereU0 isthebaselinecommandatpredictionstepj within
d,j
α
shape
=e−2πfshapeTs. (23) the current window.
Each residual component is bounded by
The cutoff frequency f determines the bandwidth of the
shape
shaped SC reference. Throughout this section, Π (·) denotes δU =δUmaxtanh(uˆ ), d∈{B,SC}, (32)
d d,j d d,j
scalar projection onto the instantaneous power command in-
terval defined by the device power rating: with uˆ d,j the raw network output and δU d max the prescribed
correction limit.
Π d (z)=min{P d max, max{−P d max, z}}, d∈{B,SC}. The feature vector includes the recent disturbance history,
(24) a short horizon disturbance preview, the current HESS state,
and the baseline command preview:
This projection enforces the instantaneous command mag-
nitude bounds, while realized power output, ramp rate, and (cid:20) ∆ ∆
SoCrequirementsareincorporatedintothepredictiveobjective ξ = k−Nh+1:k, k+1:k+Np, xn,
through dedicated penalty terms. k σ ∆ σ ∆ k
The baseline SC reference is obtained by projecting the U0 U0 (cid:21)
shaped fast component: B,k:k+Np−1 , SC,k:k+Np−1 . (33)
Pmax Pmax
Pref,0[k]=Π (cid:0) ∆ [k] (cid:1) . (25) B SC
SC SC SC Here, N is the history length, N is the prediction horizon,
h p
The remaining disturbance is assigned to the BESS and andσ isthestandarddeviationofthedisturbancesignalused
∆
projected onto its instantaneous admissible range: to normalize its magnitude. The disturbance history covers
stepsk−N +1throughk,andthepreviewcoversstepsk+1
(cid:16) (cid:17) h
P B ref,0[k]=Π B ∆[k]−P S r C ef,0[k] . (26) t t h h r e ou cu g r h re k nt + c N on p t ; ro b l o i t n h st w an in t. do T w h s e a b r a e se a l l i i n g e ne c d om so m t a h n a d t s p t r e e p vi k ew is s
When neither projection is active, the baseline references U B 0 ,k:k+Np−1 and U S 0 C,k:k+Np−1 cover the same future steps
preserve the exact balance relation inherited from the un- k through k+N −1 as the rollout commands in (31). The
p
constrained allocation. When projection becomes active, the short horizon preview ∆ is assumed to be available
k+1:k+Np
reference pair remains bounded within the prescribed instan- from a short term workload schedule over the prediction
taneouscommandlimits,whiletheunallocatedportionappears window.Inthecasestudies,thispreviewistakendirectlyfrom
naturally in the residual deviation in (18). This treatment the generated disturbance trajectory. Therefore, the present
keeps the baseline allocation consistent with the constrained studyisolatesthecontrolbenefitofdeterministicshorthorizon
smoothing objective. disturbance preview; forecasting errors are not considered.

IEEETRANSACTIONSON[JOURNALNAME] 5
The normalized HESS state is defined as finite-horizon objective to be back-propagated to the policy
parameters.
 P [k]/Pmax 
B B Within a prediction window initialized at control instant k,
 P SC [k]/P S m C ax  theprevieweddisturbanceatpredictionstepj+1corresponds


(cid:0)
SoC
[k]−SoCref(cid:1)
/∆SoC


to ∆[k+j+1]. Because U
j
influences the device powers at
xn = B B B ∈R6. (34) step j+1, the predicted grid-side residual associated with the
k   (cid:0) SoC SC [k]−SoCr S e C f(cid:1) /∆SoC SC   j-th control decision is
 
 U B [k−1]/P B max  e g,j+1 =∆[k+j+1]−P B,j+1 −P SC,j+1 . (41)
U [k−1]/Pmax
SC SC
Here, ∆SoC and ∆SoC denote the normalization spans D. Policy Training and Receding Horizon Deployment
B SC
used for the BESS and SC SoC deviations, respectively. The The DPC policy is trained offline using disturbance win-
statevectorcollectsthecurrentdevicepowers,SoCdeviations dows sampled from the datacenter load trajectory. For each
from their operating references, and the commands applied at window,thepolicygeneratesaresidualsequence,thedifferen-
the previous sampling instant. Together with the disturbance tiableHESSmodelpredictstheclosed-loopevolution,andthe
history, preview, and baseline command preview, it provides lossfunctionpenalizesgrid-sideresiduals,commandvariation,
the policy with the operating context required for residual excessive residual action, and operating limit violations.
command refinement. The policy parameters are obtained from
Theresidualpolicyπ isimplementedasafullyconnected
Θ
feedforward neural network with three hidden layers. In the
1 (cid:88)
n N
(cid:88)
p−1
case studies, N = 64 and N = 64. From (33), the input Θ⋆ =argmin ℓi (Θ), (42)
dimension is h p Θ nN p j+1
i=1 j=0
N h +N p +6+N p +N p =262, (35) where n is the batch size. The stage loss is
and the output dimension is 2N p =128, corresponding to the ℓi =Q (cid:0) ei (cid:1)2 +Q ·1[j =N −1]· (cid:0) ei (cid:1)2
two residual command sequences. GELU activation functions j+1 g g,j+1 t p g,j+1
a z r e e ro u w se e d ig in ht t s h a e n h d id z d e e ro n b la ia y s er s s o .T th h a e tt fi h n e a u l n la tr y a e i r ne is d i p n o it l i i a c l y iz i e n d it w ia i l t l h y +Q ∆U (cid:13) (cid:13)U j i−U j i −1 (cid:13) (cid:13) 2 2 +Q soc ℓi soc,j+1 +Q p ℓi p,j+1
reproduces the rule-based baseline. +Q ramp ℓi ramp,j+1 +Q v ℓi viol,j+1 +Q res (cid:13) (cid:13)δU j i(cid:13) (cid:13) 2 2 .
(43)
C. Differentiable HESS Prediction Model
Forj =0,Ui denotesthecommandappliedimmediatelybe-
−1
The finite-horizon rollout uses the same storage dynamics forethei-thtrainingwindow;itisretainedtoensurecontinuity
as the HESS model. For d ∈ {B,SC}, the device power of the command variation penalty at the window boundary
followsthefirst-orderdiscrete-timeresponseobtainedbyZOH and is included in the normalized HESS state (34). The
discretization of (8): first term penalizes the predicted grid-side residual at every
step throughout the horizon. The second term is a terminal
P =a P +b U , (36)
d,j+1 d d,j d d,j penalty active only at the final step j = N −1, where 1[·]
p
with denotes the indicator function. The command variation term
a
d
=e−Ts/τd, b
d
=1−a
d
. (37) encourages smooth control, and the residual regularization
limits unnecessary deviations from the rule-based baseline.
Here, j = 0 corresponds to the current control instant k, so The SoC displacement penalty is
P =P [k] and U determines the predicted power at the
d,0 d d,0 (cid:16) (cid:17)2 (cid:16) (cid:17)2
next sampling instant. ℓi = SoCi −SoCref + SoCi −SoCref .
The SoC update uses the device power at the beginning of soc,j+1 B,j+1 B SC,j+1 SC
the sampling interval as a causal left endpoint approximation: (44)
The power limit penalty is
P
SoC d,j+1 =SoC d,j − 3600 T E s cap ·  η d d d i , s j, P d,j ≥0, ℓi p,j+1 = (cid:88) (cid:2) max (cid:0) |P d i ,j+1 |−P d max, 0 (cid:1)(cid:3)2 . (45)
d P ηch, P <0, d∈{B,SC}
d,j d d,j
(38)
The ramp rate penalty is
where Ecap is expressed in MWh, P is expressed in MW,
d d,j
a sa n m d p T l s in i g s i e n x t p e r r e v s a s l ed fro in m se se c c o o n n d d s. s T to he h f o a u c r t s o . r T 3 h 6 e 00 ch co ar n g v i e n r g ts a t n h d e ℓi = (cid:88) (cid:34) max (cid:32)(cid:12) (cid:12) (cid:12) P d i ,j+1 −P d i ,j (cid:12) (cid:12) (cid:12)−Rmax, 0 (cid:33)(cid:35)2 .
discharging efficiencies are denoted by η d ch and η d dis, respec- ramp,j+1 d∈{B,SC} (cid:12) (cid:12) T s (cid:12) (cid:12) d
tively. The piecewise efficiency model in (38) is differentiable
(46)
almost everywhere.
The SoC bound penalty is
Collecting the device power and SoC into the state vector
(cid:40)
 P B,j  ℓi = (cid:88) (cid:2) max (cid:0) SoCmin−SoCi , 0 (cid:1)(cid:3)2
P viol,j+1 d d,j+1
x
j
=So S
C
C,j , (39)
d∈{B,SC}
B,j
SoC (cid:41)
SC,j
+ (cid:2) max (cid:0) SoCi −SoCmax, 0 (cid:1)(cid:3)2 .
the prediction rollout is written compactly as d,j+1 d
x =f (x ,U ), j =0,...,N −1, (40) (47)
j+1 HESS j j p
During offline training, the command sequence is projected
where f stacks the power dynamics (36) and the SoC through (31), while power output, ramp rate, and SoC operat-
HESS
update (38). The rollout is implemented with automatic dif- ing requirements are incorporated through soft penalty terms.
ferentiation compatible operations, allowing gradients of the Thisstructureallowstheresidualpolicytoimprovesmoothing

IEEETRANSACTIONSON[JOURNALNAME] 6
performance without replacing the physically interpretable
baseline allocation.
After training, the policy is deployed in a receding horizon
fashion. At each time step k, the feature vector ξ is assem-
k
bled, the policy outputs a residual sequence, and only the first
correction is applied:
(cid:104)δU (cid:105)
δU = B,0 . (48)
k δU
SC,0
The candidate DPC command is
UDPC[k]=Π (cid:0) U0[k]+δU [k] (cid:1) , d∈{B,SC}. (49)
d d d d
A one-step safeguard uses the known disturbance preview
∆[k +1] to compare the predicted immediate residuals. Let
eDPC[k + 1] and e0[k + 1] denote the one-step predicted
g g
residuals under the candidate DPC command and the baseline
command, respectively. Define Fig. 2: NPCC 140-bus topology with datacenter disturbance
injection buses and monitored generators highlighted.
(cid:20) (cid:21) (cid:20) (cid:21)
U [k] UDPC[k]
U[k]= B , UDPC[k]= B ,
U SC [k] U S D C PC[k] TABLE I: Datacenter Disturbance Injection Buses in the
(cid:20) (cid:21) NPCC 140-Bus System
U0[k]
U0[k]= B . (50)
U S 0 C [k] Datacenter Bus BaseLoad[MW] PeakDeviation[MW]
The applied command is DC1 78 2000 17.1
DC2 91 1650 18.5
(cid:40) UDPC[k], (cid:12) (cid:12)eD
g
PC[k+1] (cid:12) (cid:12)≤ (cid:12) (cid:12)e0
g
[k+1] (cid:12) (cid:12)+ε
s
, D
D
C
C
3
4
1
1
3
2
1
8
1
9
1
7
6
0
0 1
1
6
7
.
.
5
0
U[k]=
DC5 120 946 18.4
U0[k], otherwise. DC6 55 939 18.0
(51) DC7 53 923 16.6
The safeguard is used as a conservative deployment time
acceptance check for the first receding horizon correction. It
does not replace the finite-horizon training objective and is
disturbance smoothing performance is therefore evaluated at
not intended to provide a complete hard feasibility guarantee
the single datacenter level, while the system level frequency
for power output, ramp rate, or SoC limits. Instead, it rejects
impact is assessed by injecting the compensated and uncom-
candidate corrections that are predicted to produce a clearly
pensated disturbance profiles from seven datacenters into the
inferior immediate residual relative to the baseline command.
NPCC system. Each profile is applied at a separate load
The tolerance ε prevents the screening rule from discarding
s bus as a time-varying active power deviation, following the
corrections whose one-step effect is nearly neutral. Thus, the
played in large load disturbance setup used in recent AI
rule-based baseline remains available as a reliable fallback
datacenter dynamic studies [16], [32], [33]. The injection
command, whereas the residual DPC correction is applied
buses are selected as the largest load buses in the system,
whenever its immediate predicted effect is acceptable under
and the corresponding bus assignments are listed in Table I.
the prescribed safeguard criterion.
Differentstarttimesareusedforthesevendisturbanceprofiles
to represent asynchronous workload operation, producing a
IV. SIMULATIONSTUDIES peak aggregate disturbance of approximately 140 MW. The
A. Simulation Setup simulation horizon is 700 s with a sampling period of 0.01 s.
The HESS device parameters and DPC training settings are
The simulation studies are designed to assess both the
listed in Table II.
localdisturbancesmoothingcapabilityoftheproposedHESS-
Inbothtrainingandclosed-loopevaluation,theDPCpolicy
DPC framework and its resulting impact on system frequency
usesashort-horizondisturbancepreviewoverN T =0.64s,
dynamics. The NPCC 140-bus system is simulated using the p s
consistentwiththeformulationinSectionIII-B.Inthepresent
benchmark case distributed with the ANDES power system
casestudies,thispreviewistakenfromthegeneratedworkload
simulator [31]. Synchronous generators are represented by
trajectory so that the effect of predictive command refinement
the classical second-order GENCLS model in the NPCC
can be evaluated independently of disturbance-forecasting
benchmark. The analysis focuses on the resulting generator
accuracy.
frequency responses to datacenter active power disturbances.
Fig. 3 shows the individual and aggregate disturbance
Explicit excitation system and turbine governor dynamics are
profiles over a representative interval. Although the individual
not included in this study. Therefore, the reported responses
profiles have comparable magnitudes, their superposition pro-
should be interpreted as forced frequency oscillations of
duces a much larger aggregate deviation with both sustained
the classical machine NPCC benchmark under the imposed
plateaus and sharp transitions, ranging from approximately
datacenter disturbances. To introduce generator to generator
+50 MW to near −90 MW. This aggregate profile charac-
diversity in the frequency response, the inertia coefficient
terizes the uncompensated system level disturbance used to
of each GENCLS unit is scaled by a fixed random factor
assess the frequency impact in the NPCC system.
uniformlysampledfrom[0.7,1.3],usingthesamerandomseed
for all compared cases.
At the datacenter level, each datacenter is modeled as a 50-
B. HESS Power Smoothing
MW synthetic AI datacenter load following the aggregation
model in Section II. The load comprises three workload Fourconfigurationsarecompared:(A)noHESS,(B)BESS
components, including one dominant training workload, one only, (C) rule-based HESS, and (D) the proposed HESS-
smaller training workload, and one fine-tuning workload. DPC.Thegrid-sideresidualpowerdeviationPdev underthese
grid
HESS-DPC is implemented locally at each datacenter. Its four configurations is shown in Fig. 4. Without HESS, the

| IEEETRANSACTIONSON[JOURNALNAME] |                |     |            |     |              |     |      |     |     |     |     |     | 7   |
| ------------------------------- | -------------- | --- | ---------- | --- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |
| TABLE                           | II: Simulation |     | Parameters | for | the HESS-DPC |     | Case |     |     |     |     |     |     |
Studies
| Parameter |     |     |     |     | BESS | SC  | Unit |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
Datacenterloadparameters
Nominalpowerofdominanttrainingworkload,Ptr
|                       |     |     |     |     | L0  | 50    | MW  |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Smalltrainingratio,κS |     |     |     |     |     | 0.056 | –   |     |     |     |     |     |     |
| Fine-tuningratio,κF   |     |     |     |     |     | 0.056 | –   |     |     |     |     |     |     |
HESSdeviceparameters
| Powerrating,Pmax |     |     |     |     | 30  |     | 15 MW |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
d ,Ecap
| Energycapacity         |     |      |     |     |      | 7 0.05 | MWh  |     |     |     |     |     |     |
| ---------------------- | --- | ---- | --- | --- | ---- | ------ | ---- | --- | --- | --- | --- | --- | --- |
| Rampratelimit,R        |     | dmax |     |     |      |        |      |     |     |     |     |     |     |
|                        |     | d    |     |     | 50   | 100    | MW/s |     |     |     |     |     |     |
| Responsetimeconstant,τ |     |      |     |     | 0.25 | 0.015  | s    |     |     |     |     |     |     |
d
| Initialstateofcharge,SoC |     |     | d,0 |     | 0.60 | 0.60 | –   |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
SoClowerbound,SoCmin
dm 0.05 0.05 – Fig. 4: Grid side residual power deviation under the four
| SoCupperbound,SoC |     | ax  |     |     | 0.95 | 0.95 | –         |                 |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | ---- | ---- | --------- | --------------- | --- | --- | --- | --- | --- |
|                   |     | d   |     |     |      |      | smoothing | configurations. |     |     |     |     |     |
Baselinecontrollerparameters
| Frequencysplitcutoff,f |     | split |     |     |     | 0.5 | Hz  |     |     |     |     |     |     |
| ---------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCshapingcutoff,f      |     |       |     |     |     | 8.0 | Hz  |     |     |     |     |     |     |
shape
DPCpolicyparameters
| Predictionhorizon,Np |     |     |     |     |     | 64  | steps |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| Historywindow,N      |     |     |     |     |     | 64  | steps |     |     |     |     |     |     |
h
| Safetytolerance,εs       |     |     |     |     |     | 0.05  | MW              |          |          |              |       |          |            |
| ------------------------ | --- | --- | --- | --- | --- | ----- | --------------- | -------- | -------- | ------------ | ----- | -------- | ---------- |
| Trainingepochs           |     |     |     |     |     | 800   | –               |          |          |              |       |          |            |
| Training/validationsplit |     |     |     |     |     | 85/15 | %               |          |          |              |       |          |            |
|                          |     |     |     |     |     |       | Fig. 5:         | BESS and | SC power | outputs      | under | the      | rule-based |
|                          |     |     |     |     |     |       | HESS and        | proposed | HESS-DPC | controllers, |       | together | with       |
|                          |     |     |     |     |     |       | their reference | signals. |          |              |       |          |            |
Fig.3:Individualdisturbanceprofilesofthesevendatacenters
| and the | corresponding |     | aggregate | deviation | injected | into | the |     |     |     |     |     |     |
| ------- | ------------- | --- | --------- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
NPCC system.
|     |     |     |     |     |     |     | while the    | SC responds | to fast           | transitions | and      | high-frequency  |         |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ----------------- | ----------- | -------- | --------------- | ------- |
|     |     |     |     |     |     |     | variations.  | Under       | both controllers, | the         | device   | outputs         | closely |
|     |     |     |     |     |     |     | follow their | references, | confirming        |             | that the | frequency-based |         |
residual closely follows the workload-induced fluctuation of allocation is consistent with the physical characteristics of the
| the datacenter | load. | The | BESS-only | configuration |     | reduces | the two devices. |     |     |     |     |     |     |
| -------------- | ----- | --- | --------- | ------------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
slowly varying component, but large residual spikes remain Under HESS-DPC, the residual corrections are modest in
around the major workload transition intervals because the magnitude but concentrated at workload transition intervals.
BESS ramp rate limit and response time constant prevent it The SC correction supplements the rule-based shaping near
from tracking rapid power changes. workload transition intervals, while the BESS correction re-
The rule-based HESS substantially reduces these transient duces slower tracking errors. The resulting power trajectories
|            |              |     |          |             |           |     | remain within | the | rated ranges | in  | Table | II throughout | the |
| ---------- | ------------ | --- | -------- | ----------- | --------- | --- | ------------- | --- | ------------ | --- | ----- | ------------- | --- |
| deviations | by assigning |     | the fast | disturbance | component |     | to the        |     |              |     |       |               |     |
simulation.
| SC and the | remaining | component |     | to the | BESS. | Nevertheless, |     |     |     |     |     |     |     |
| ---------- | --------- | --------- | --- | ------ | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- |
TheSoCtrajectoriesoverthefull700shorizonareshownin
| residual deviations |           | persist | near          | workload | transition | intervals,  |                                      |     |     |     |     |               |     |
| ------------------- | --------- | ------- | ------------- | -------- | ---------- | ----------- | ------------------------------------ | --- | --- | --- | --- | ------------- | --- |
|                     |           |         |               |          |            |             | Fig.6.BothdevicesareinitializedatSoC |     |     |     |     | =0.60.TheBESS |     |
| as the fixed        | frequency |         | decomposition |          | does not   | incorporate |                                      |     |     |     | 0   |               |     |
preview information about the upcoming disturbance profile. SoC remains close to its initial value under both controllers,
The proposed HESS-DPC achieves the smallest residual consistent with the zero-mean property of ∆[n] established in
among all four cases. The residual remains within a small Section II. A more pronounced difference is observed in the
band around zero during steady fluctuation intervals and is SC SoC. Under the rule-based controller, the SC SoC drifts
strongly attenuated at workload transition intervals—precisely progressively downward during the second half of the simula-
the operating condition where fixed frequency decomposition tion,indicatingthatthefixedrule-basedallocationaccumulates
is most limited due to the absence of disturbance preview. a net energy imbalance over an extended operating horizon.
Theseresultsconfirmthatapredictiveresidualcorrectionover Under HESS-DPC, the SC SoC remains substantially closer
a short horizon of N T =0.64 s substantially reduces the to its initial level throughout the simulation, confirming that
|     |     | p   | s   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tracking errors at workload transitions while preserving the the finite-horizon policy improves SC energy sustainability
structured BESS/SC allocation. overtheextendedhorizonwithoutadedicatedSoCrestoration
| Fig. 5 | shows | the BESS | and | SC power | outputs | under | the scheme. |     |     |     |     |     |     |
| ------ | ----- | -------- | --- | -------- | ------- | ----- | ----------- | --- | --- | --- | --- | --- | --- |
rule-basedHESSandHESS-DPCconfigurations,togetherwith The one-step safeguard in (51) governs which DPC cor-
their reference signals. The BESS primarily tracks the low rections are applied at each time step. A smaller tolerance
frequency energy-dominant component of the disturbance, ε s makes the safeguard more conservative, accepting the

IEEETRANSACTIONSON[JOURNALNAME] 8
| Fig. 6:          | SoC trajectories |             | of the      | BESS | and SC      | under | the rule- |     |     |     |     |
| ---------------- | ---------------- | ----------- | ----------- | ---- | ----------- | ----- | --------- | --- | --- | --- | --- |
| based HESS       | and              | proposed    | HESS-DPC    |      | controllers |       | over the  |     |     |     |     |
| 700 s simulation |                  | horizon.    |             |      |             |       |           |     |     |     |     |
| TABLE            | III:             | Sensitivity | of HESS-DPC |      | Performance |       | to ε      |     |     |     |     |
s
| εs             | Accept. |              | RMS   | RMS          |          | Peak-to-peak | MinSC    |       |     |     |     |
| -------------- | ------- | ------------ | ----- | ------------ | -------- | ------------ | -------- | ----- | --- | --- | --- |
| [MW]           | rate[%] | residual[MW] |       | reduction[%] |          | residual[MW] | SoC[%]   |       |     |     |     |
| Rulebased      | –       |              | 1.36  |              | –        | 11.45        |          | –     |     |     |     |
| 0.00           | 45.8    |              | 0.300 |              | 77.9     | 4.91         |          | 50.91 |     |     |     |
| 0.01           | 46.9    |              | 0.303 |              | 77.7     | 5.00         |          | 51.06 |     |     |     |
| 0.05           | 50.7    |              | 0.316 |              | 76.8     | 5.05         |          | 51.52 |     |     |     |
| 0.10           | 54.6    |              | 0.336 |              | 75.3     | 5.32         |          | 52.03 |     |     |     |
| 0.20           | 60.6    |              | 0.373 |              | 72.6     | 5.71         |          | 53.11 |     |     |     |
| DPC correction |         | only when    | its   | predicted    | one-step |              | residual | is    |     |     |     |
no larger than the baseline residual within the prescribed Fig.7:DatacenterdisturbancesmoothingimpactontheNPCC
tolerance.Alargerε s admitsmorecorrections,includingsteps 140-bus system: aggregate disturbance, generator frequency
forwhichthepredictedimmediateadvantageoverthebaseline response, and frequency spectrum.
is smaller.
| Table        | III reports | the       | DPC         | acceptance     | rate,          | RMS  | grid-side |     |     |     |     |
| ------------ | ----------- | --------- | ----------- | -------------- | -------------- | ---- | --------- | --- | --- | --- | --- |
| residual,    | RMS         | reduction | relative    | to             | the rule-based |      | baseline, |     |     |     |     |
| peak-to-peak | residual,   |           | and minimum |                | SC SoC         | over | the 700   | s   |     |     |     |
| horizon      | for five    | values    | of ε .      | The rule-based |                | HESS | baseline  |     |     |     |     |
s
| achieves | an RMS   | residual | of   | 1.36 | MW and        | a peak-to-peak |         |     |     |     |     |
| -------- | -------- | -------- | ---- | ---- | ------------- | -------------- | ------- | --- | --- | --- | --- |
| residual | of 11.45 | MW.      | At ε | = 0, | the safeguard |                | accepts |     |     |     |     |
s
| 45.8% of | DPC | corrections | and | reduces | the | RMS residual |     | to  |     |     |     |
| -------- | --- | ----------- | --- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
0.300MW,correspondingtoa77.9%reductionrelativetothe
| rule-based | baseline. | As  | ε increases |     | from 0 | to 0.20 | MW, the |     |     |     |     |
| ---------- | --------- | --- | ----------- | --- | ------ | ------- | ------- | --- | --- | --- | --- |
s
| acceptance | rate | rises from | 45.8% | to  | 60.6%, | while | the RMS |     |     |     |     |
| ---------- | ---- | ---------- | ----- | --- | ------ | ----- | ------- | --- | --- | --- | --- |
reductiondecreasesfrom77.9%to72.6%.Thistrendindicates
| that the   | additional | corrections |           | admitted | under       | more | relaxed  |     |     |     |     |
| ---------- | ---------- | ----------- | --------- | -------- | ----------- | ---- | -------- | --- | --- | --- | --- |
| thresholds | provide    | weaker      | immediate |          | improvement |      | on aver- |     |     |     |     |
age, leading to moderately degraded residual power metrics. Fig. 8: Zoomed view of the G9/bus 97 frequency deviation.
Across the tested range, the RMS reduction remains above HESS-DPC reduces the peak-to-peak value from 15.1 mHz to
| 72% and       | the minimum |           | SC SoC       | stays   | above     | 50%,        | showing   |          |     |     |     |
| ------------- | ----------- | --------- | ------------ | ------- | --------- | ----------- | --------- | -------- | --- | --- | --- |
|               |             |           |              |         |           |             |           | 1.3 mHz. |     |     |     |
| that the      | safeguard   | maintains |              | strong  | smoothing | performance |           |          |     |     |     |
| over a        | practical   | range     | of tolerance |         | values.   | In the      | remaining |          |     |     |     |
| case studies, | ε           | = 0.05    | MW           | is used | as a      | balanced    | setting   |          |     |     |     |
s
between correction acceptance and residual quality. consistent with the structured and periodic nature of the
|     |     |     |     |     |     |     |     | aggregate datacenter | disturbance. | This behavior | indicates that     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ------------ | ------------- | ------------------ |
|     |     |     |     |     |     |     |     | the uncompensated    | disturbance  | acts as a     | persistent forcing |
C. Frequency Impact on the NPCC 140-Bus System input to the bulk system. With the proposed HESS-DPC, the
frequencydeviationisstronglyattenuatedandremainscloseto
| Fig. | 7(a) shows | the | aggregate | power | deviation |     | from the |     |     |     |     |
| ---- | ---------- | --- | --------- | ----- | --------- | --- | -------- | --- | --- | --- | --- |
seven datacenters over the full simulation horizon. Without zero,substantiallyreducingthesustainedoscillatoryexcitation
HESS, the aggregate disturbance exhibits sustained large- in the bulk system.
amplitude fluctuations whose cycle to cycle amplitudes vary The frequency spectrum of the G9 deviation is shown in
due to the stochastic workload profiles and asynchronous Fig.7(c).WithoutHESS,thespectrumexhibitsadominantlow
timing offsets among the facilities. With the proposed HESS- frequency peak at the fundamental workload cycle frequency
DPC applied at each datacenter, the aggregate residual is andseveralharmoniccomponents,eachofwhichmayinteract
suppressed to a narrow band around zero, showing that local with electromechanical modes of the power system. With
compensation at each datacenter remains effective once the HESS-DPC compensation, the spectral amplitude is reduced
seven profiles are combined. to near the noise floor across the range below 2 Hz.
Fig. 7(b) shows the frequency deviation of generator G9 at To quantify the mitigation effect, Fig. 8 provides a zoomed
bus 97, identified as the most affected generator under this view of the G9 frequency deviation over a representative 25
disturbance scenario. Without HESS, G9 exhibits sustained s interval. Without HESS, the peak-to-peak deviation reaches
oscillations throughout the simulation horizon with peak-to- 15.1 mHz. With the proposed HESS-DPC, this value is re-
peak deviations reaching 15.1 mHz. These oscillations are ducedto1.3mHz,correspondingtoa91.4%reduction.Fig.9

IEEETRANSACTIONSON[JOURNALNAME] 9
(a) Without HESS-DPC.
Fig. 9: Frequency deviations of the four most affected gen- (b) With HESS-DPC.
erators under uncompensated and HESS-DPC-compensated
Fig. 10: Effect of generator dynamic representation on the
datacenter disturbances.
G9/bus 97 frequency response: (a) without HESS-DPC and
(b) with HESS-DPC.
TABLE IV: Peak-to-Peak Frequency Deviation Reduction of
Monitored Generators
Generator WithoutHESS[mHz] HESS-DPC[mHz] Reduction[%W]ith HESS-DPC, the corresponding values are reduced to
2.3 mHz and 1.3 mHz, respectively. The same trend is
G9/bus97 15.1 1.3 91.4
observed at the system level. Based on the worst generator
G16/bus130 14.7 2.9 80.3
G8/bus92 14.7 1.2 91.8 response in each case, HESS-DPC reduces the peak-to-peak
G14/bus122 13.7 0.5 96.4 deviation from 28.80 mHz to 3.07 mHz in the classical ma-
chineNPCCbenchmark,correspondingtoan89.3%reduction.
In the full dynamic model, the worst generator deviation
decreases from 15.83 mHz to 2.94 mHz, corresponding to
extends this comparison to the four most affected generators,
an 81.4% reduction. Thus, the full dynamic model confirms
with the corresponding peak-to-peak values summarized in
that HESS-DPC strongly suppresses the frequency response
Table IV. Without HESS, all four generators exhibit sustained
causedbydatacenterpowerfluctuations.Atthesametime,the
oscillatoryresponseswithpeak-to-peakdeviationsintherange
classicalmachineNPCCbenchmarkoverestimatestherelative
of13–16mHz,sharingtheperiodicityoftheaggregateforcing
mitigation benefit by 7.9 percentage points.
disturbance but differing in phase and waveform shape due to
The case studies verify the proposed source-side mitigation
their distinct modal participation and network coupling. With
path: HESS-DPC suppresses the active-power disturbance at
the proposed HESS-DPC, the peak-to-peak deviation of each
the datacenter point of interconnection under time-varying
generator is reduced by more than 80%. A small residual
workload conditions, with the residual DPC correction con-
oscillation remains at G16, which is more strongly coupled
tributing most at workload transitions where fixed frequency
to the dominant system mode excited by the disturbance, but
decomposition falls short. The reduced disturbance injected
its compensated deviation remains at the mHz level and is
into the NPCC 140-bus system results in substantially lower
much smaller than the uncompensated response. These results
generator frequency deviations and spectral excitation across
demonstratethatlocalpowersmoothingatthedatacenterlevel
the system. The full dynamic model comparison shows that
effectivelyreducesfrequencydeviationsacrosstheNPCC140-
this mitigation benefit persists when governor and excitation
bus system.
dynamicsarerepresented,sotheresultisnotanartifactofthe
The classical GENCLS benchmark excludes governor and
simplified GENCLS benchmark.
excitation dynamics, which provide additional frequency
damping in practice. To examine whether this simplification
affects the estimated mitigation benefit, the same datacenter V. CONCLUSION
disturbance setting is repeated using the full dynamic NPCC This paper presented a source-side active power smoothing
model. The full dynamic model retains 21 GENCLS units frameworkinwhichafrequency-decompositionhybridenergy
and additionally includes 27 GENROU machines, 29 TGOV1 storage system provides a structured rule-based baseline and
turbine governors, and 24 IEEEX1 excitation systems from a residual differentiable predictive control policy refines the
the original NPCC dynamic data; the smaller frequency re- baselinecommandsusingashort-horizondisturbancepreview.
sponse it produces relative to the classical benchmark reflects InNPCC140-bussimulationswithseven50MWAIdatacen-
this additional damping. Cases without HESS-DPC and with ters, HESS-DPC reduced grid-side residual power deviations
HESS-DPC are evaluated for both model representations. at the point of interconnection and maintained SC state-of-
Figure 10 compares the frequency response of the common charge balance over extended operation; generator peak-to-
reference generator G9 at bus 97. Without HESS-DPC, the peak frequency deviations were reduced by more than 80%
peak-to-peak deviation is 28.8 mHz in the classical machine across all monitored generators, with the worst-case generator
NPCC benchmark and 15.8 mHz in the full dynamic model. (G9 at bus 97) reduced from 15.1 mHz to 1.3 mHz. This

IEEETRANSACTIONSON[JOURNALNAME] 10
gain stems from the complementary roles of the two layers: [22] J. W. Shim et al., “Virtual capacity of hybrid energy storage systems
the rule-based frequency decomposition handles steady-state using adaptive state of charge range control for smoothing renewable
intermittency,”IEEEAccess,vol.8,pp.126951–126964,2020.
allocation, while the residual DPC correction applies most
[23] T. Chmielewski, W. Jarzyna, D. Zielin´ski, K. Gopakumar, and
of its action at workload transition intervals, where the fixed M. Chmielewska, “Modified repetitive control based on comb filters
baselinecannotanticipatetheapproachingdisturbancechange. for harmonics control in grid-connected applications,” Electric Power
SystemsResearch,vol.200,p.107412,2021.
Repeating the evaluation with a full dynamic NPCC model
[24] J. Cao and A. Emadi, “A new battery/ultracapacitor hybrid energy
that includes governor and excitation systems yields the same storagesystemforelectric,hybrid,andplug-inhybridelectricvehicles,”
more-than-80% reduction, showing that the result does not IEEE Transactions on power electronics, vol. 27, no. 1, pp. 122–132,
2011.
depend on the simplified GENCLS representation. These re-
[25] B. Amos, I. Jimenez, J. Sacks, B. Boots, and J. Z. Kolter, “Differen-
sults demonstrate that source-side smoothing at the datacenter tiable mpc for end-to-end planning and control,” Advances in neural
pointofinterconnection,reinforcedbyashort-horizonlearned informationprocessingsystems,vol.31,2018.
[26] J.Drgonˇa,K.Kisˇ,A.Tuor,D.Vrabie,andM.Klaucˇo,“Differentiable
correction, can substantially limit the impact of AI workload
predictivecontrol:Deeplearningalternativetoexplicitmodelpredictive
fluctuations on bulk system frequency. control for unknown nonlinear systems,” Journal of Process Control,
vol.116,pp.80–92,2022.
[27] T. Silver, K. Allen, J. Tenenbaum, and L. Kaelbling, “Residual policy
REFERENCES learning,”arXivpreprintarXiv:1812.06298,2018.
[28] T.Johannink,S.Bahl,A.Nair,J.Luo,A.Kumar,M.Loskyll,J.A.Ojea,
[1] North American Electric Reliability Corporation, “Characteristics and E.Solowjow,andS.Levine,“Residualreinforcementlearningforrobot
risksofemerginglargeloads,”2025. control,” in 2019 international conference on robotics and automation
[2] B. A. Ross and J. Follum, “Electromagnetic transient modeling (ICRA). IEEE,2019,pp.6023–6029.
of large data centers for grid-level studies,” [Online]. Available: [29] S. Chen, K. Saulnier, N. Atanasov, D. D. Lee, V. Kumar, G. J. Pap-
https://www.pnnl.gov/publications/ electromagnetic-transient-modeling- pas, and M. Morari, “Approximating explicit model predictive control
large-data-centers-grid-level-studies,PacificNorthwestNationalLabora- using constrained neural networks,” in 2018 Annual American control
tory(PNNL),Tech.Rep.PNNL-38817,December2025,alphaRelease. conference(ACC). IEEE,2018,pp.1520–1527.
PreparedfortheU.S.DepartmentofEnergyunderContractDE-AC05- [30] D. Q. Mayne, J. B. Rawlings, C. V. Rao, and P. O. Scokaert, “Con-
76RL01830. strainedmodelpredictivecontrol:Stabilityandoptimality,”Automatica,
[3] A. Shehabi, S. J. Smith, A. Hubbard, A. Newkirk, N. Lei, M. A. B. vol.36,no.6,pp.789–814,2000.
Siddik, B. Holecek, J. G. Koomey, E. R. Masanet, and D. A. Sartor, [31] H.Cui,F.Li,andK.Tomsovic,“Hybridsymbolic-numericframework
“2024unitedstatesdatacenterenergyusagereport,”2024. forpowersystemmodelingandanalysis,”IEEETransactionsonPower
[4] E. Choukse, B. Warrier, S. Heath, L. Belmont, A. Zhao, H. A. Khan, Systems,vol.36,no.2,pp.1373–1384,2021.
B.Harry,M.Kappel,R.J.Hewett,K.Dattaetal.,“Powerstabilization [32] S. Biswas, A. C. Varghese, K. Chatterjee, S. Nekkalapu, B. Ross, and
foraitrainingdatacenters,”arXivpreprintarXiv:2508.14318,2025. J. Follum, “Evaluating the risk to bulk power system reliability from
[5] Z.Ye,W.Gao,Q.Hu,P.Sun,X.Wang,Y.Luo,T.Zhang,andY.Wen, largeloadinducedoscillations,”AuthoreaPreprints,2025.
“Deeplearningworkloadschedulingingpudatacenters:Asurvey,”ACM [33] Energy Systems Integration Group (ESIG), “Large load disturbance
ComputingSurveys,vol.56,no.6,pp.1–38,2024. events,” Energy Systems Integration Group, Tech. Rep. ESIG-LLTF-
[6] P.Patel,E.Choukse,C.Zhang,´I.Goiri,B.Warrier,N.Mahalingam,and 2026-01,Mar.2026.
R.Bianchini,“Characterizingpowermanagementopportunitiesforllms
inthecloud,”inProceedingsofthe29thACMInternationalConference
on Architectural Support for Programming Languages and Operating
Systems,Volume3,2024,pp.207–222.
[7] G. Wilkins, F. Kazhamiaka, and R. Rajagopal, “From servers to sites:
Compositionalpowertracegenerationofllminferenceforinfrastructure
planning,”arXivpreprintarXiv:2603.18383,2026.
[8] R. O’Keefe, “Event records showing data center response to faults,”
Presentation, NERC LLTF April Meeting and Technical Workshop,
2025.
[9] M.ParkerandB.Sterling,“Unplanneddatacenterloadtransferupdate,”
Presentation,NERCLLTFJuneWorkshop,2025.
[10] Y.Li,M.Mughees,Y.Chen,andY.R.Li,“Theunseenaidisruptionsfor
powergrids:Llm-inducedtransients,”arXivpreprintarXiv:2409.11416,
2024.
[11] A.Jimenez-RuizandF.Milano,“Datacentermodelfortransientstability
analysisofpowersystems,”arXivpreprintarXiv:2505.16575,2025.
[12] A. Borghesi, C. Di Santi, M. Molan, M. S. Ardebili, A. Mauri,
M.Guarrasi,D.Galetti,M.Cestari,F.Barchi,L.Beninietal.,“M100
exadata: a data collection campaign on the cineca’s marconi100 tier-0
supercomputer,”ScientificData,vol.10,no.1,p.288,2023.
[13] A.Radovanovic,B.Chen,S.Talukdar,B.Roy,A.Duarte,andM.Shah-
bazi, “Power modeling for effective datacenter planning and compute
management,” IEEE Transactions on Smart Grid, vol. 13, no. 2, pp.
1611–1621,2021.
[14] K.Chatterjee,J.D.Follum,A.Varghese,S.Biswas,E.Farantatos,and
L.Zhu,“Measurementadequacyformonitoringdatacenteroscillations,”
PacificNorthwestNationalLaboratory,Richland,WA,USA,Technical
Report,2026.
[15] S. Talukdar, S. Marti, K. Prabakar, and D. Vaidhynathan, “Modeling
framework for data center,” National Renewable Energy Laboratory,
Golden,CO,USA,TechnicalReportNREL/TP-2C00-97716,2026.
[16] M.-S.KoandH.Zhu,“Wide-areapowersystemoscillationsfromlarge-
scaleaiworkloads,”IEEETransactionsonPowerSystems,2026.
[17] M.-S. Ko et al., “Mitigation of datacenter demand ramping and fluc-
tuation using hybrid ESS and supercapacitor,” arXiv preprint, vol.
arXiv:2512.08076,2025.
[18] North American Electric Reliability Corporation, “Relia-
bility Guideline: Risk Mitigation for Emerging Large
Loads,” North American Electric Reliability Corpora-
tion, Reliability Guideline, May 2026. [Online]. Avail-
able: https://www.nerc.com/globalassets/our-work/guidelines/reliability/
RG Risk-Mitigation-For-Emerging-Large-Loads.pdf
[19] M.-S.KoandH.Zhu,“Wide-areapowersystemoscillationsfromlarge-
scale ai workloads,” IEEE Transactions on Power Systems, pp. 1–14,
2026.
[20] North American Electric Reliability Corporation, “White
paper: Grid forming functional specifications for bps-
connected battery energy storage systems,” [Online]. Available:
https://www.nerc.com/globalassets/our-work/reports/white-
papers/white paper gfm functional specification.pdf,2023.
[21] J.Xiao,P.Wang,andL.Setyawan,“Hierarchicalcontrolofhybriden-
ergystoragesystemindcmicrogrids,”IEEETransactionsonIndustrial
Electronics,vol.62,no.8,pp.4915–4924,2015.