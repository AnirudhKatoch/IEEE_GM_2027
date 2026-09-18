arXiv is now an independent nonprofit! Learn more (https://info.arxiv.org/about)  ×

Why HTML?
(https://info.arx
iv.org/about/ac
cessible_HTM
L.html)

Report
Report
Issue
Issue

Back to
Back to
Abstract
Abstract

Download
Download
PDFPDF

License: CC BY-NC-ND 4.0 (https://info.arxiv.org/help/license/index.html#licenses-available)
arXiv:2606.00941v1 [eess.SY] 31 May 2026

Power Grid Infrastructure for AI Data Centers†

Amir Sajadi

Muhy E. Za’ter

Maria Vabson

Kyri Baker, , and Bri-Mathias Hodge,

Abstract

This article addresses recent advances in artificial intelligence, which have set off

an astounding race among technology frontiers to build large data centers. It pro-

vides insights into impacts of large data centers on the planning and operation of

the power grid.

Index Terms: : AI data centers, large language models, power system planning,
power system operation

I

Introduction

The field of artificial intelligence (AI), particularly large language models (LLMs),



has  taken  the  world  by  storm  in  recent  years.  Fueled  by  recent  advances  in
deep learning and massive datasets, these models have demonstrated remark-

able  abilities  across  a  broad  range  of  applications  and  a  strong  potential  for
positive contributions in many economic sectors. Consequently, a fierce compe-
tition  has  been  sparked  among  technology  leaders,  and  even  nations,  in  the

development  of  large-scale  data  centers,  creating  a  global  surge  in  electricity





demand.





Data centers and chip foundries are projected to grow exponentially in the com-

ing years. Meeting their rising electricity demand will require substantial invest-

ment  to  expand  and  reinforce  power  grid  infrastructure.  However,  upgrading

this  infrastructure  is  a  lengthy  process  that  can  take  several  years  and  often

leads  to  long  interconnection  and  commissioning  timelines  for  data  centers,

particularly for large data centers, mainly due to constrained power availability [

1]. As an emergency remedy, many utilities are taking near-term action to allevi-

ate the strain on their assets. For example, some utilities reversed previous po-

sitions  on  the  retirement  of  some  coal  units  to  operate  beyond  their  originally
planned  lifetimes  and  proposed  the  construction  of  new  fossil  fuel  units.

Similarly,  some  nuclear  plants  are  being  brought  out  of  retirement,  and  more

broadly, data centers are single-handedly driving a lot of new nuclear develop-



ment  that  was  not  seen  before.  The  mounting  pressure  from  the  widespread

construction  of  large  data  centers  leaves  many  power  utilities  at  the  perils  of

aging infrastructure and rising complexity of grid operation, in addition to chal-

lenges  around  system  planning  and  upgrade  needs  to  meet  the  reliability  and

affordability standards.

Furthermore, the inherent electric characteristics of these data centers and their



unconventional load shape and size for both training and inference in LLMs in-

troduce complexity to the power grid planning and operation. For instance, dur-

ing training, tens of thousands of processors can instantaneously spike power

consumption up or down due to factors such as waiting for checkpointing or col-

lective communication to complete or the startup and shutdown of entire train-

ing jobs. This stands in contrast with the conventional moderate ramp load pro-

files that power grids are designed to routinely manage. Such events can intro-

duce  power  quality  challenges  [2]  and  can  cause  sudden  fluctuations  in  data
center  power  usage,  sometimes  reaching  hundreds  of  kilowatts  (kW)  to


megawatts  (MW)  [3]. These  extreme  power  ramp  rates  are  unprecedented  in
large industrial loads, especially since they occur within millisecond timescales.
In  contrast,  inference  is  heavily  influenced  by  user  demand  for  a  given  LLM,

leading to potential surges at peak times.





Many of the grid critical challenges and complexities with regards to large data

centers  have  been  documented  in  the  literature  with  technical  analysis,  use
cases, and case studies [4] – [6]. This article examines the risks and opportuni-
ties  that  large AI  data  centers  present,  given  contemporary  electric  power  in-

dustry  processes  and  practices.  The  topics  discussed  are  organized  into  two

main categories:



1.

Grid Expansion and Market Strategy


2.

Grid Performance and Reliability


























First, we introduce the key components inside AI data centers and their power

consumption profiles. Subsequently, we discuss the integration of data centers

into the power grid and explore the associated challenges. For each topic, we



highlight the emerging trends and issues on the horizon, along with recommen-

dations  as  appropriate,  intended  for  policy  makers,  electric  utilities,  and  data

center developers and operators.

II Overview of Large Data Centers

II-A Data Center Components

A  typical  data  center  consists  of  many  servers,  ranging  from  500  to  2,000  for

small  data  centers  to  2,000  to  10,000  servers  for  medium  data  centers  and


numbering above 10,000 servers for hyperscale data centers  [7]. Each server

consists of computation units, which are the primary consumers of power in a

data  center.  These  can  be  either  AI-accelerated  graphics  processing  units

(GPUs) and tensor processing units (TPUs) or non AI-accelerated central pro-
cessing unit (CPUs). The CPU has been the standard technology of computa-
tion and is widely used in personal computers and professional servers. On the

other  hand,  GPUs  and  TPUs  are  emerging  processing  technologies  that  con-
sume more power than CPUs, but their higher processing speeds are valuable

for AI  applications  in  large  data  centers. Additionally,  each  server  consists  of
storage  and  network  units  for  data  storage  and  communication  whose  energy
consumption relative to that of the processors is much lower. Processing units,

when stacked up in a large data center and operating at full load, can sum to
large quantities of electric power, on the order of MW and expected to rise to gi-

gawatts  (GW). The  energy  demand  from  the  IT  components  in AI-accelerated
servers  alone,  accounting  for  all  processing,  storage,  and  communication  and

network  equipment,  is  estimated  to  contribute  between  50%  and  70%  of  total
data center energy consumption  [8].





The second most energy consuming element of a data center is its cooling sys-

tem.  Its  electricity  consumption  is  determined  based  on  the  scale  of  the  data

center, the type of cooling system, and the efficiency of the technology used, as

well as the data center location due to additional ambient cooling needs, espe-

cially in hotter or more humid climates. Cooling typically accounts for up to 40%
of the total electricity consumption of a data center [9].















The  third  energy  consuming  element  is  the  lighting  system.  This  energy  con-



sumption can be readily calculated based on power usage of the lighting tech-

nology used (commonly LED) and the number of lights used in a facility. The fi-

nal major energy consuming component is the electric losses in the electricity

distribution network of the facility, which can account for 10%–12% of the total

power [10]. This can be reduced by utilizing direct current (DC) technology and

operating at higher voltage levels.









Power usage effectiveness (PUE) is the most common metric used to quantify

the  amount  of  electric  energy  a  data  center  consumes  for  both  IT  and  non-IT

components.  It  is  the  ratio  of  the  total  power  consumed  by  a  data  center  (in-

cluding IT load, cooling system, lights, and electricity losses) to the power con-

sumed by the computer systems (which is the total aggregate of all power read-

ings  from  each  server  rack).  In  most  modern  efficient  data  centers,  especially

hyperscale  and AI  data  centers,  the  PUE  is  around  1.05–1.15  (the  lower  and
closer to 1.0, the better) [11], whereas in conventional data centers, this num-

ber can rise to 1.6.







II-B Data Centers Scale in Numbers

In 2023, data centers in the United States consumed approximately 4.4% of the



country’s  total  energy  consumption.  This  demand  is  projected  to  rise  signifi-
cantly  in  the  near  future,  reaching  6.7%  to  12%  of  nationwide  electricity  con-

sumption by 2028 [9]. A major driver of this growing energy demand is the in-
creasing  deployment  of  AI-accelerated  computing,  particularly  GPU-based
servers, which are significantly increasing in both power consumption and vol-

ume.  In  2023,  the  average  power  rating  per AI  server  instance  (typically  con-
sisting of eight GPUs) was approximately 8.5 kW, with operational power aver-

aging  around  6  kW.  By  2028,  these  values  are  expected  to  increase,  with
power ratings reaching 11 kW and operational power ranging between 6.5 and

8.5  kW  [8].  Even  when  idle,  servers  consume  about  20%–25%  of  their  peak

power, contributing to overall energy inefficiency  [12].





As AI usage continues to scale up, the number of installed servers in the United
States  is  projected  to  reach  37  million  by  2028,  with  AI-specific  servers  ac-

counting for 8 to 12 million of them [8]. This growth is driven by the surge in use





of AI products, which increases utilization rates. Training instances currently op-



erate at around 80% utilization and are projected to rise to 90% by 2028  [13],

while  inference  instances,  which  currently  utilize  about  40%  of  their  capacity,

are  expected  to  reach  60%  [14].  In  addition  to  the  energy-intensive  nature  of

the processing units, other components, such as storage and networking also

contribute to power consumption. Also, AI-focused data centers utilize efficient

cooling  technologies  that  typically  have  a  lower  PUE,  indicating  relatively  effi-

cient power management, although sustainability concerns persist.

II-C AI Load Profile and Characteristics

A key contributor to this surge in electricity demand is the training of large-scale



AI  models,  and  more  specifically  LLMs,  which  require  vast  computational  re-

sources.  For  instance,  the  training  of  Meta’s  LLaMA-3  405B  model  was  con-

ducted on 16,000 H100 GPUs, distributed across instances of eight GPUs per

server [3]. Similarly, Google’s PaLM model and DeepSeek’s latest model are on

the order of thousands of processing units.





Power  consumption  associated  with AI  workloads  can  be  broadly  categorized

into two primary types: 1) training and 2) inference. Training includes both the
pretraining  and  fine-tuning  stages  of  model  development,  each  of  which  de-
mands substantial computational resources. The power requirements for train-

ing  are  exceptionally  high,  often  involving  thousands  of  high-performance

GPUs operating near full capacity over extended periods, sometimes spanning
days  or  even  months. Although  training  is  not  entirely  dispatchable,  it  demon-
strates a degree of flexibility in scheduling. Specifically, training processes can

be paused and resumed later without significant issues as they are neither real
time nor highly latency sensitive. However, instantaneous stopping is not feasi-

ble without the risk of losing unsaved progress. A characteristic of LLM training

is the abrupt power load variation that occurs during checkpoint saving, where

the load can rapidly drop from full utilization to near idle within seconds.





On  the  other  hand,  inference,  while  requiring  considerably  lower  power  than
training  due  to  reduced  computational  intensity,  presents  different  operational

challenges. Unlike training, inference workloads are primarily driven by user de-

mand, making them less predictable and less flexible. Furthermore, inference is












a  real-time,  latency-sensitive  process,  meaning  that  it  must  respond  instanta-



neously  to  input  requests  without  significant  delays.  Consequently,  it  is  a

nondispatchable  load  if  served  synchronously  as  its  execution  cannot  be  de-

ferred or paused without degrading the quality of service. The unpredictability of

inference demand, coupled with its real-time nature, may pose significant chal-

lenges for the management of the host power grid. As a potential remedial solu-

tion,  some  commercial  LLM  providers  such  as  OpenAI  and  Google  have  re-

cently begun developing mitigation solutions to reduce stress on the grid by of-

fering asynchronous inference for load flexibility. However, the underlying chal-

lenge remains unresolved and continues to represent a critical source of uncer-

tainty to the grid planners and operators.







Fig. 1: Data  centers  as  part  of  the  power  grid  ecosystem.  EMS:  energy  management

system; UPS: uninterruptible power supply.

II-D Interconnection to Power Grid

The interconnection of AI data centers to the electric power grid creates tight in-



teractions and potentially symbiotic relationships between their respective sys-

tems and subsystems, as conceptualized in Figure 1. As a result, close coordi-

nation is essential to prevent adverse impacts on grid components and to en-

sure safe integration of these data centers. The remainder of this article exam-

ines key issues related to their interconnection, associated implications, and im-

portant planning and operational considerations.







III Grid Expansion and Market Strategy

III-A Load Growth Forecast

A core challenge with grid planning for data center interconnection is accurately



forecasting load growth driven by expected data center additions. The intercon-

nection of large loads on its own has a long precedent in the power system in-

dustry. However, two barriers distinguish the data centers from the existing con-

vention of forecasting large loads: 1) the lack of easily accessible data regard-

ing  power  consumption  in  data  centers  and  their  specific  patterns  and  2)  the

lack of easily accessible development plans that are often treated as trade se-

crets. A solution to remove the former barrier would be to make electric power

consumption data of these facilities available to the grid planners. This type of

data with hourly resolution (to represent daily, seasonal, and annual variations

and  to  capture  variations  throughout  the  day,  including  ramps,  peaks,  and

unique shapes) for multiple years would be sufficient to inform the power sys-
tem planners. Additionally, data on daily peak and average power consumption

would  be  helpful  to  determine  power  generation  and  transfer  capacity  needs
and  the  cost  of  energy,  respectively.  Such  data  could  be  either  provided  from

historical  measurements  or  synthesized.  The  use  of  historical  measurement
would  be  beneficial  to  extrapolate  future  scenarios  with  a  more  limited  uncer-

tainty and obtain accurate hourly profiles. On the other hand, the development
and  use  of  synthetic  data  would  require  detailed  information  about  the  design

and topology of the data center and the technology planned to be employed. As
such, it might need a wider range of future scenarios to be investigated to ac-

count for a greater uncertainty which is embedded in the synthetic data.









The latter barrier could be lowered by putting in place a framework where the
data center developers have a statutory timeline to publicly disclose their con-

struction  or  expansion  intent  and  plans.  This  timeline  and  the  notice  periods

can  be  determined  by  the  regulators  and  subject  to  the  needs  of  the  hosting

electric utility. It would give the planners sufficient time to prepare the grid to re-

liably serve the data center without compromising the reliability of energy deliv-

ery to its ratepayers. Other efforts such as putting in place financial incentives

like better electricity rates or tax breaks could encourage the data center devel-

opers to disclose their plans reasonably in advance







III-B Resource Adequacy and Capacity Expansion

The  rapid  growth  of  large  data  centers  challenges  the  availability  of  sufficient



generation  capacity  with  adequate  ramping  rates  on  three  fronts. They  are  1)

the time for permitting and constructing new generation facilities, 2) the possi-

bility  of  introducing  acute  power  demand  fluctuations,  and  3)  the  interconnec-

tion  timelines.  First,  constructing  new  generation  units  can  be  a  lengthy

process, depending on the type of generation facility. In the United States, the

average  time  for  building  most  types  of  new  generation  facilities  is  more  than

two years, whereas a data center can be built and commissioned in less than

two  years.  For  example,  while  solar  has  the  shortest  time  for  implementation,

one to two years, it is highly location dependent due to the amount of solar en-

ergy varying locations receive and the space requirements needed for sufficient

capacity, which is a concern for scalability of large data center sites. Similarly,

there are additional considerations for the other power plants in terms of where

they  can  be  both  better  placed  for  new  construction  and  relicensed  for  pro-
longed use.









Second,  large  data  centers  can  introduce  significantly  acute  power  demand

fluctuations throughout the day in the form of high-power pulsated ramp up and
down as their power consumption varies by their computation queries. Two ap-
proaches exist to address this issue. The first approach is to equip the grid with

more fast-ramping backup units, which presents the risk of suboptimal planning

or overbuilt. Such support was traditionally provided using fast ramping gas tur-
bines  and  coal  units,  which  are  not  the  most  environmentally  friendly  options.
Also, conventionally, hydropower plants have been used for fast-regulation pur-

poses,  which  could  still  be  viewed  as  a  more  environmentally  friendly  option.
While construction of new hydropower plants remains restricted to specific geo-
graphical  locations  and  water  availability,  there  could  be  more  focus  on  reli-

censing  existing  facilities.  It  should  be  noted  that  the  ramp  rate  of  all  conven-

tional  resources,  even  those  that  are  traditionally  recognized  as  fast-ramping

units,  is  much  slower  than  that  of  data  centers.  More  recently,  inverter-based
resources, which consist of utility-scale batteries and variable renewable units

(when available and operating with a headroom), offer a greener and ubiquitous
solution with capabilities to more closely match the ramp rates of data centers.

Regardless of the generation technology, the addition of more generation units
always hinges on the availability of transmission capability, which adds a layer

of interdependency to the feasibility of this approach. The second approach is
to equip the data center facility with resources to smoothen its fluctuations and

limit its ramps. The latter approach could transform the data center into a self-



regulating  load  and  could  be  achieved  via  options  such  as  on-site  diesel,  gas

generators,  batteries,  or  other  energy  storage  systems,  subject  to  the

local/regional  environmental  restrictions  and  air  quality  requirements  and  de-

pending on the developer’s appetite for reducing the carbon footprint of their fa-

cilities  considering  the  higher  cost  of  most  storage  units.  The  choice  of  using

battery  storage  as  a  backup  resource,  however,  adds  an  extra  layer  of  com-

plexity to system planning as a new question arises about the optimal sizing for

battery  storage  units,  including  both  short-term  battery  and  long-duration  stor-

age systems. This question could be multifaceted to understand the adequate

size  of  the  battery  to  1)  minimize  (ideally  eliminate)  the  fluctuations  that  the

data  center  introduces  to  grid  and  2)  maximize  the  value  of  power  generation

from solar and wind units. We note that the small modular reactors and fuel cell

industries have gained substantial interest in this space. Despite not yet having

reached commercial maturity, both technologies could play a major role in the

future. To address this problem, in the long term, we suggest that energy regu-
lators  may  consider  mandating  data  centers  to  self-regulate  their  fluctuations

and be allowed on the network only if they satisfy certain ramp limits.

Third, the interconnection of new generation is a lengthy process and can take



years. New generation to supply a modern AI data center will likely be a project
greater than 20 MW and will take more than two years[15]. Between 2015 and

2020,  the  average  timeline  for  the  construction  and  commissioning  of  large
data centers was reported to be around three years, with as little construction
time as a year  [1]. However, in recent years, this timeline has increased to up

to six years, mainly due to the lack of power infrastructure  [1]. Moving forward,

the timeline gap between power plants and data center constructions needs to
be eliminated to achieve sustainable growth.





A common practice for data centers to avoid delays caused by the generation

interconnection  process  is  to  develop  or  utilize  a  generation  facility  near  the

data center and directly connect the two facilities, therefore bypassing the grid.

Nevertheless, a colocated generation facility could be still physically connected

to the main utility grid with limited power exchanges and certain obligations and

regulations,  which  are  not  clearly  defined.  This  is  an  area  where  regulators
need to pay closer attention and ease the path for developers.

















III-C Transmission System Upgrades

Large data centers are emerging all across the United States, and it is safe to



suggest  that  they  are  pushing  transmission  systems  to  their  limits.  Therefore,

increasing the transmission capacity across the country is the key to ensuring

the reliability of the grid with adequate redundancy in the years to come.

















Similar to the process for generation capacity expansion, the transmission sys-

tem  and  associated  substation  construction  and  upgrades  can  be  a  lengthy

process and takes several years, whereas a large data center, as noted earlier,

can  be  constructed  and  commissioned  in  less  than  two  years.  This  timescale

discrepancy  between  the  demand  growth  and  network  upgrade  can  delay  the

interconnection  of  data  centers  and,  thus,  result  in  a  loss  of  revenue  for  the

utilities.





Of the available options to increase the ampacity of a transmission line, recon-

ductoring using advanced conductors presents a viable option to increasing its
carry  capacity  (double  to  triple)  with  minimal  modification  to  the  transmission

towers. Nonetheless, their deployment is costly and needs to be carefully stud-
ied to ensure it is economically justified.





At  the  heart  of  transmission  system  planning  is  cost  allocation,  which  deter-

mines  the  mechanism  for  investment  recovery  and  return  on  equity.  One  may
rely on intuition to suggest that if the line upgrade is required because of inter-

connection of a large data center as the main beneficiary, then the “beneficiary
pays.” But defining beneficiaries for cost allocation purposes is often murky and
not  straightforward.  Notwithstanding  that  each  regional  transmission  organiza-

tion has an established set of regional and interregional transmission planning

rules,  cost  allocation  often  serves  as  a  source  of  dispute  among  stakeholders

and remains a complicated topic, especially if it involves other loads or multiple
data centers.







III-D Integrated Resource Planning

The  rapid  pace  at  which  data  centers  are  coming  online  has  compelled  many



utilities to take swift action to address their near-term risks. However, these fa-

cilities  have  long-term  broader  impacts  well  beyond  the  power  grid  as  they

could  alter  their  local  and  larger  communities,  ranging  from  climate,  environ-

ment, and individual health to socioeconomic consequences. Therefore, the de-

velopment of these facilities needs holistic examination of all relevant parame-

ters. This could be achieved through integrated resource planning (IRP), which

aims to optimize the whole system in the long term and shed light on all direct

and indirect costs of the data centers.









An  effective  IRP  could  be  achieved  through  direct  engagement  of  the  local

community in all stages of planning, construction, and operation to directly hear

from them. Their engagement also helps address their concerns early on and to
ensure  the  developments  and  their  operation  align  with  the  community,  local,

and  regional  interests  and  standards. Their  concerns  may  include  carbon  and

water footprint, air and water pollution and mitigation efforts, electricity and wa-
ter  availability  and  prices,  job  creation  and  the  local  economy,  and  the  impact
on the housing market. Ongoing dialogue and iterative processes that include

meaningful  debates  and  open  communication  with  the  residents  and  commu-
nity  leaders  are  the  key  to  continuously  keeping  the  locals  informed  and

engaged.







III-E Risk Management and Market Strategy

All data center development projects are subject to risks of delays or failure due
to a range of issues such as supply chain challenges, technical flaws, financial



security,  permitting,  land  acquisition,  changes  in  the  political  or  social  land-

scape, and legal challenges. In the power industry, the rules of wholesale en-

ergy  markets  are  well  established  for  delays  or  withdrawal  of  generation  or

transmission  projects.  However,  these  rules  need  to  be  expanded  to  include

risk  management  for  large  data  centers.  Rules  should  also  be  established  to

discourage and prevent data center withdrawal and define mechanisms for re-

covery  of  all  network  upgrade  studies  and  asset  costs  incurred.  Such  expan-
sions will hedge the reliability risks for system planners, the investment risks for

developers, and the risks for public ratepayers.







Large data centers are relatively new in the power industry, and therefore, there



is  a  lack  of  adequate  data  and  sufficient  knowledge  about  their  behavior  and

performance. From the operations perspective, accessing data centers’ behav-

ior and profile data can help the host utility with its multiday ahead and the day

ahead load forecasts and improve its market strategy. This is a critical function

of operational planning and determines the energy (electricity and/or fuel) pro-

curement  and  bidding  strategy

in

the  market,  directly

impacting

revenues/losses  and  the  settlements.  From  the  planning  perspective,  the  cre-

ation  of  a  reporting  system  for  large  data  centers  can  help  the  grid  planners

better  learn  about  these  new  assets  and  improve  their  processes  and  proce-

dures. This reporting can contain information about the availability and perfor-

mance  of  these  facilities,  efficiency  performance,  their  involuntary  disconnec-

tion from the grid, duration, cause, and values like PUE and water usage effec-

tiveness. These reports can be collected and processed by the existing bodies,

for  example,  the  North American  Electric  Reliability  Corporation  or  the  Energy

Information  Administration,  as  a  new  reporting  requirement,  for  example,  the
large-load availability data system.









Lastly,  the  on-site  resources  of  large  data  centers,  generators  or  battery  stor-

age units, can offer them some operational flexibility, particularly during the grid
constraint  periods.  Such  capability  may  help  them  expedite  their  interconnec-
tion  to  the  grid,  subject  to  the  flexibility  parameters. Additionally,  we  envision

that in the future, the data center operator could use these resources to offer a

range of services to support their host grid, either as a participant in the whole-
sale  energy  market,  a  direct  service  agreement,  or  a  combination  of  both.
These services will be discussed later in this article. From the market strategy

perspective, the key enabler for their engagement in wholesale energy markets
is having market rules and tariffs that provide financial incentives to data cen-
ters  to  participate. Achieving  this  regulatory  milestone  requires  direct  engage-

ment of electric power utilities, energy commissions, and data center develop-

ers and operators.







IV Grid Performance and Reliability

IV-A System Stability and Power Quality

Interconnecting  large  data  centers  to  a  power  grid  will  require  network  impact



studies  to  demonstrate  that  the  incoming  data  center  does  not  have  adverse

impacts on the extant network. These loads are driven by an opaque concen-

tration of electronic and digital control systems and can be pulsated, withdraw-

ing  large  quantities  of  power  from  the  network  instantaneously  without  any  or

with  a  negligible  amount  of  directly  coupled  mechanical  inertia.  Furthermore,

any electronic equipment could easily introduce a large degree of nonlinearity,

in  addition  to  power  pulses,  which  are  induced  by  data/computation  queries,

collectively contributing to stability and power quality concerns.





The  adverse  impacts  of  data  centers  on  the  grid  performance  can  manifest

themselves in steady-state, oscillations, or nonideal sinusoidal waveforms, im-
plicating  system  frequency,  nodal  voltages,  and  phase  angles.  Steady-state
stability concerns slower dynamics, in which gradually accumulating deviations

from scheduled values or standard limits can eventually render the system in-

feasible  or  inoperable. The  oscillations  are  faster  dynamics  and  can  be  either
sustained (forced oscillations) or temporary (for example, local or inter-area os-
cillations). These oscillations, if left unmitigated, can damage equipment and in-

cur maloperations and may lead to forced outages with the potential to cause
blackouts.  The  nonideal  waveforms,  on  the  other  hand,  contain  higherfre-

quency  components,  known  as  harmonics,  which  could  be  integer  multiples,
subharmonics, or interharmonics of the nominal frequency and could also dam-
age equipment, lower their life span, and force malfunctions. These behaviors

should  be  closely  studied  and  routinely  monitored  to  ensure  the  data  center’s
interactions  with  other  assets  are  safe  and  in  compliance  with  the  grid  codes

and  regional  regulation  on  harmonic  limits,  power  fluctuations,  and  response
obligations.





From the grid dynamics perspective, the large data centers could be the source

of  disturbances  to  the  grid.  On  that  note,  these  data  centers  can  introduce  a

new class of contingencies that involve a rapid, significant drop in the amount
of  power  consumption  by  load  at  a  specific  node  or  complete  disconnection

from the network (load tripping). The system planners should consider studying









this  class  of  contingencies  from  both  the  small-  and  large-signal  stability  per-



spectives, and operators should put in place appropriate remedial actions.

When  an  area  is  identified  to  suffer  from  an  adverse  impact  caused  by  a



planned  large  data  center,  then  it  is  inevitable  that  network  upgrades  or  rein-

forcement are needed as a mitigation plan. Traditionally, electromechanical so-

lutions,  such  as  synchronous  condensers,  and  power  electronics-based  solu-

tions,  such  as  the  static  synchronous  compensator  and  static  VAR  compen-


sator, have been successful in improving a system’s dynamics and power qual-

ity. More recently, grid-forming inverters have reached the maturity needed for

utility-scale  deployment,  and  solid-state  transformers  are  expected  to  reach  a

similar level within the next few years. Both technologies offer promising solu-

tions for data center applications.





An outstanding challenge in this domain is the lack of reliable, high-fidelity, in-

dustry-grade models to accurately represent their transients and power quality
issues  and  efficiently  allow  for  system-wide  phasor  and  electromagnetic  tran-
sient simulations. Access to such models and simulation capabilities are essen-

tial for the utility planners to adequately understand and describe all hardware

and  software  components  as  they  relate  to  grid  interactions.  To  address  this
challenge, data center developers and power system planners need to work to-
gether to create generic, open access, industry standard dynamic models and

practices for model verification and quality testing.













IV-B Fault Response and Fault Ride-Through

Short circuit fault response and ride-through capabilities are preventative mea-



sures against undesired frequency and voltage phenomena. The power indus-

try is realizing that these grid-supporting functions may not remain solely on the

generation side and could be enforced on the load side, especially for the large

data centers. This need came to light following a data center disconnection in

2024, where a fault on a 345-kV line resulted in near-instantaneous disconnec-

tion of 1.5 GW of data center load due to voltage sensitivity [16]. Load drop of

such  magnitude  following  a  high-voltage  fault  was  unprecedented  and

concerning.







The preventative measures could be the standardization of fault response from



large  data  centers  in  the  form  of  short  circuit  contribution  and  mandatory  en-

forcement of ride-through capability. For these measures, data centers may rely

on their onsite resources or other existing solutions. Most notably, synchronous

condensers are widely used for increasing fault current and system strength as

they produce short circuit current and prevent significant voltage depression.





The specific level of fault current contribution and requirements for ride-through

can be determined by either the host utility or the regional reliability entity and

included  in  the  interconnection  agreement  as  operational  requirements.

Mandating a contribution to short circuit fault current in the context of data cen-

ters not only helps with easier detection of fault conditions, but it serves to re-

quire data centers to stay online and not disconnect immediately.











IV-C Data Centers as Grid Flexibility Assets

AI data centers can range from tens of MW- to GW-scale loads; however, their



software  defined  workloads  and  the  redundancy  in  their  on-site  equipment
make  them  uniquely  capable  of  acting  as  potentially  controllable  grid  assets.

There are multiple sources of dispatchable flexibility that could be used to sup-
port the grid, including but not limited to the following:









•

Uninterruptible  power  supply  (UPS)  batteries:  UPSs  regulate  power



and provide clean AC waveform to the IT systems. They also provide
short-term  backup  power  during  grid  interruptions  before  the  backup
generators  take  over  for  long-term  outages.  These  systems  contain

batteries on their DC segment that have the potential to be utilized in

the  future  for  grid-supporting  services,  using  their  idle  capacity  that

can absorb or inject power.




•

Thermal  storage  and  thermal  inertia:  Chilled  water  tanks  and  the

facility’s own thermal mass could be utilized by the operators for pre-
cooling  or  changing  the  temperature  set  points,  therefore  allowing

peak  shaving  and  load  shifting  without  any  manipulation  to  the  IT





workload.






•

Dynamic IT workload management: Studies show that around 60% of





IT or server tasks [17] are tolerant of delays. This flexibility can be ex-

ploited  by  shifting  the  workload  temporally  or  spatially,  therefore  pro-

viding dynamic workload management  [18].




•

Backup generators: During a period when the grid is stressed, the data

center  site  can  island  itself  and  have  the  technical  capability  to  even

inject power back into the grid, especially during strenuous conditions





such as restoration and synchronization.






Considering these attributes, data centers can be converted from firm loads into



interruptible loads (fully or partially), enabling the electric utilities to tap into their

existing grid headroom capacity for serving flexible data centers. Consequently,

such flexibility help could accelerate the interconnection of AI data centers. For

the  flexible  data  centers  to  become  operational,  there  are  many  nuances  that

the host electric utility and the data center enterprise need to thoroughly evalu-
ate and mutually agree upon, including flexibility expectations, performance re-
quirements, contractual obligations, and incentives.





We envision that large data centers will potentially play a larger role in grid real-

time  operation  as  they  can  be  practically  treated  as  microgrids.  There  are  a
host of services that these facilities may provide to the grid and act as a cata-


lyst  for  decarbonization,  for  example,  acting  as  nonwire  alternative  assets  for
peak  shaving  and  load  shifting  (both  temporal  and  spatial),  congestion  relief,
short-term reserve for frequency and voltage response, helping with improved

damping  of  oscillations,  and  intentional  islanding  during  extreme  events  and
helping with restoration for resilience.





Most modern utility control rooms are equipped with the information and com-

munication  technologies  and  control  infrastructure  needed  to  implement  these

services. They are, namely, energy management systems for controlling trans-

mission-connected assets and advanced distribution management systems and
distributed  energy  resource  management  systems  for  managing  the  distribu-











tion-connected  assets  and  coordination  with  distributed  resources
lies
However,

[19].
terms  and  conditions  of

the  key  enabler

the

in

business/commercial agreements between data centers and utilities on the re-



sponse mechanism and specifications and the obligations from both sides, in-

cluding the technical details such as the measurement information that will be

used  for  determining  market  tariffs  and  payment  processes.  Furthermore,  be-

fore  data  centers  can  safely  become  grid  flexibility  assets,  there  remain  open

questions to clarify the coordination among balancing authority, market opera-

tor, transmission owner and operator, and load entities with regards to responsi-

bilities, data sharing, decision making, procedures, jurisdiction, and authorities

to prevent any missteps or noncompliance.

V Closing Remarks

Artificial intelligence is widely regarded as the cornerstone of the fourth indus-

trial  revolution,  with  large-scale  data  centers  as  the  backbone  driving  this
progress.  To  achieve  sustainable  growth  of  these  facilities,  data  center  enter-
prises, power utilities, and energy regulators need to come together and make







adjustments  to  their  processes,  regulations,  and  standards  to  streamline  their

expedited interconnection and secure operation. We are optimistic that this arti-
cle could serve as an informative basis for all parties involved and shed light on
the opportunities and challenges that large AI data centers present for reevalu-

ation and development of reliability standards, performance requirements, and
market  tariffs  to  prioritize  the  ratepayers  and  grid  security  and  simultaneously

paving the path for a sustainable AI boom.



Acknowledgment





We thank Ramanathan Thiagarajan for his insightful comments. This work was



in  part  funded  by  the  Climate  Innovation  Collaboratory  (CIC),  an  ongoing  al-

liance between Deloitte and University of Colorado Boulder.



References





[1]

S. Obando, “Data center building boom shows cracks,” 2023.
[Online]. Available:

https://www.constructiondive.com/news/psmj-survey-data-
center-construction/699469/

[2]

J. Sun, M. Xu, M. Cespedes, D. Wong, and M. Kauffman, “Modeling
and analysis of data center power system stability by impedance

methods,” in 2019 IEEE Energy Conversion Congress and Exposition
(ECCE). IEEE, 2019, pp. 107–116.

[3]

A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman,

A. Mathur, A. Schelten, A. Yang, A. Fan et al., “The llama 3 herd of
models,” arXiv preprint arXiv:2407.21783, 2024.

[4]

Chen, Xin and et al., “Electricity demand and grid impacts of AI data

centers: Challenges and prospects,” arXiv preprint arXiv:2509.07218,
2025.

[5]

Lin, Liuzixuan and Wijayawardana, Rajini and Rao, Varsha and

Nguyen, Hai and GNIBGA, Emmanuel Wedan and Chien, Andrew A,
“Exploding ai power use: an opportunity to rethink grid planning and
management,” 15th ACM International Conference on Future and
Sustainable Energy Systems, pp. 434–441, 2024.

B. Chalamala and et al., “Data center growth and grid readiness”
(TR131),”, IEEE Power and Energy Society, Technical Report, 2025.

“Data Centers and the Power System: A Primer — NESCOE —
nescoe.com,” https://nescoe.com/resource-center/data-
centers-primer/, [Accessed 09-02-2025].

A. Shehabi, A. Hubbard, A. Newkirk, N. Lei, M. A. B. Siddik,
B. Holecek, J. Koomey, E. Masanet, D. Sartor et al., “2024 united
states data center energy usage report,” 2024. https://eta-
publications.lbl.gov/sites/default/files/2024-12/lbnl-
2024-unitedstates-data-center-energy-usage-report_1.pdf.

J. Aljbour, T. Wilson, and P. Patel, “Powering intelligence: Analyzing
artificial intelligence and data center energy consumption,” EPRI
White Paper no. 3002028905, 2024.

[6]

[7]

[8]

[9]

[10]

“Reduce Energy Losses from Power Distribution Units (PDUs)
energystar.gov,”

https://www.energystar.gov/products/data_center_equipmen
t/16-more-ways-cut-energy-waste-data-center/reduce-
energy-losses-power-distribution-units-pdus, [Accessed 09-
02-2025].

R. Verdecchia, J. Sallou, and L. Cruz, “A systematic review of green
ai,” Wiley Interdisciplinary Reviews: Data Mining and Knowledge
Discovery, vol. 13, no. 4, p. e1507, 2023.

Y.-C. Wang, J. Xue, C. Wei, and C.-C. J. Kuo, “An overview on
generative ai at scale with edge-cloud computing,” IEEE Open
Journal of the Communications Society, 2023.

J. Sevilla and E. Roldán, “Training compute of frontier ai models
grows by 4-5x per year,” 2024, accessed: 2025-02-10. [Online].
Available: https://epoch.ai/blog/training-compute-of-
frontier-ai-models-grows-by-4-5x-per-year

E. Erdil, “Optimally allocating compute between inference and
training,” 2024, accessed: 2025-02-10. [Online]. Available:

https://epoch.ai/blog/optimally-allocating-compute-
between-inference-and-training

[11]

[12]

[13]

[14]

[15]

J. Rand, N. Manderlink, W. Gorman, R. H. Wiser, J. Seel, J. M.

Kemp, S. Jeong, and F. Kahrl, “Queued up: 2024 edition,
characteristics of power plants seeking transmission interconnection
as of the end of 2023,” 2024.

[16]

[17]

[18]

North American Electric Reliability Corporation, “Incident review:
Considering simultaneous voltage-sensitive load reductions,” 2025,
[Accessed 09-02-2025].

Y. Cao, M. Cheng, S. Zhang, H. Mao, P. Wang, C. Li, Y. Feng, and
Z. Ding, “Data-driven flexibility assessment for internet data center
towards periodic batch workloads,” Applied Energy, vol. 324, p.
119665, 2022.

Colangelo, Philip and Coskun, Ayse K and Megrue, Jack and
Roberts, Ciaran and Sengupta, Shayan and Sivaram, Varun and
Tiao, Ethan and Vijaykar, Aroon and Williams, Chris and Wilson,
Daniel C and others, ”AI data centres as grid-interactive assets,”
Nature Energy, vol. 11, no. 2, p. 254–261, 2026

[19]

Bash, Cullen and Bian, Jessica and Milojicic, Dejan and Patel,
Chandrakant D and Strezoski, Luka and Terzija, Vladimir, “Energy
supplies for future data centers,” Computer, vol. 57, no. 7, p. 126–
134, 2024.

Experimental support, please view the build logs for errors. Generated by L  T   xml

 (http
s://math.nist.gov/~BMiller/LaTeXML/).

A E

Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance
accessibility and mobile support. To report errors in the HTML that will help us improve conversion
and rendering, choose any of the methods listed below:

Click the "Report Issue" (

) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues (https://github.com/arXiv/html_feedback/issues). We
appreciate your time reviewing and reporting rendering errors we may not have found yet. Your
efforts will help us improve the HTML versions for all readers, because disability should not be a
barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML
maintain a list of packages that need conversion (https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-
packages-for-LaTeXML), and welcome developer contributions (https://github.com/brucemiller/LaTeXML/issue
s).

