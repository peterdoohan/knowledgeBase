S
A Network Model of Catecholamiine Effects: Gain,
Signal-to-Noise Ratio, and Behavior
DAVID SERVAN-SCHREIBER, HAARRY PRINTZ, JONATHAN D. COHEN
At the level of individual neurons, catecholamine release increases the responsivity of
cells to excitatory and inhibitory inputs. A model ofcatecholamine effects in a network
ofneural-like elements is presented, which shows that (i) changes in the responsivity of
individual elements do not affect their ability to detect a signal and ignore noise but (ii)
the same changes in cell responsivity in a network of such elements do improve the
signal detection performance ofthe network as a whole. The second result is used in a
computer simulation based on principles of parallel distributed processing to account
for the effect of central nervous system stimulants on the signal detection performance
of human subjects.
T
HE CATECHOLAMINES NOREPINEPH-
rine and dopamine are neuroactive
substances
that
are presumed
to
modulate
information
processing
in the
brain rather than to convey discrete sensory
or motor signals. Release of norepinephrine
and dopamine occurs over wide areas of the
central nervous system (CNS), and the post-
synaptic effects of the release of these cate-
cholamines are long-lasting (1). One impor-
tant effect consists of an enhancement of the
response of target cells to other afferent
inputs, inhibitory as well as excitatory [(2);
reviewed in (3)].
Increases or decreases in catecholaminer-
gic
tone
have many
behavioral
conse-
quences, including effects on motivated be-
haviors, attention, learning, memory, and
motor behavior. At the information process-
ing level, catecholamines appear to affect the
ability to detect a signal when it is embed-
ded in noise [reviewed in (4)]. However,
there is no adequate account of how these
changes at the system level relate to the
effect of catecholamines on individual cells.
Several investigators (5-8) have suggested
that catecholamine-mediated increases in a
cell's responsivity can be interpreted as a
change
in the
cell's signal-to-noise
ratio
(SNR). By analogy, they proposed that this
D. Servan-Schreiber, School of Computer Science, Car-
negie Mellon University, Pittsburgh, PA 15213 and
Department ofPsychiatry, School ofMedicine, Universi-
ty of Pittsburgh, Pittsburgh, PA 15213.
H. Printz, School ofComputer Science, Carnegie Mellon
University, Pittsburgh, PA 15213 and Digital Equip-
ment Corporation, Paris Research Laboratory, 85 Ave-
nue Victor Hugo,
92563
Rueil-Malmaison
Cedex,
France.
J. D. Cohen, Departnent of Psychology, Carnegie Mel-
lon University, Pittsburgh, PA 15213, Department of
Psychiatry, School of Medicine, University of Pitts-
burgh, Pittsburgh, PA 15213, and Department of Psy-
chiatry and Behavioral Sciences, School of Medicine,
Stanford University, Stanford, CA 94305.
892
change at the unit level may account for
changes in signal detection performance at
the behavioral level. We explore here the
relation between these two
levels, using
mathematical and computational models of
individual neurons and networks of neu-
rons.
We assume that the response of a typical
neuron can be described by a strictly increas-
ing function fG(x) from real-valued inputs
to the interval (0, 1). This function relates
the strength of a neuron's net afferent input
x to its probability of firing or activation.
We do not require that fG be differentiable
or even continuous. We call fG the activa-
tion function.
For instance, the family of logistics, given
by
fG(X) -1 + e(GX+B)
(1)
has been proposed as a model of neural
response functions (9). The logistics are all
strictly increasing, for all values of G > 0
and all values of B.
The potentiating effect of catecholamines
on responsivity can be modeled as a change
in the shape of the activation function. In
the case of the logistic, this is achieved by
increasing the value of the gain parameter
G, as illustrated in Fig. 1B. As G increases,
the valuefG(x) comes arbitrarily close to 1 if
x > 0 and arbitrarily close to 0 ifx < 0 (10).
Consider the signal detection perform-
ance of a network in which the response of a
single unit is compared with a threshold to
determine the presence or absence of a
signal. We assume that in the presence ofthe
signal this unit receives a positive (excitato-
ry) net afferent input x, and in the absence
of the signal it receives a null or negative
(inhibitory)
input XA. When
zero-mean
noise is added to this quantity, in the pres-
ence as well as in the absence of the signal,
the unit's net input in each case is distribut-
ed around x, or XA, respectively (Fig. LA).
Therefore, its response is distributed around
fG(Xs) orfG(xA), respectively.
In other words, the input in the case
where the signal
is present is a random
variable Xs, with probability density func-
tion (PDF) pxs, and in the absence of the
signal it is the random variable XA, with
PDF PXA. These inputs then determine the
random
variables
YGS = fG(Xs)
and
YGA =fG(XA), with PDFs pYyG
and PyGA,
which represent the response in the presence
or absence of the signal for a given value of
G (Fig. 1C).
Ifthe input PDFs px, and PXA overlap, the
output PDFs PYGs and PYGA will also overlap.
Thus, for any given threshold 0 on the y axis
z._
D
D
O
_
0
-60
A
PXA
Pxs
-4.0
-2.0
0.0
2.0
x (Net input)
4.0
6.0
1'0r B
-
co
:il
-6
._
co
G=2.0,'
Il
G=1.0
0
.0
-4.0
-2.0
0.0
2.0
x (Net input)
4.0
6.0
"C
PY
- =1.0
L
GA----
v
%,
Y~~~GS
0.0
0.5
y (Activation)
1.0
Fig. 1. (A) Example of the probability density
function (PDF) of the net input in the cases of
signal absent (PxA) and signal present (pxs). (B)
The logistic function at two values ofgain G. This
function has been proposed as a model of neural
responsivity. The unit's activation at zero net
input corresponds to a neuron's baseline firing
rate. Positive net inputs correspond to excitatory
stimuli, negative net inputs correspond to inhibi-
tory stimuli. For the graphs drawn here, we set
the bias B to -1. The negative bias renders the
function asymmetric around a net input of 0. This
asymmetry is often found in the response function
of actual neurons (22). Increasing G drives up a
unit's response to a positive input and drives
down its response to a negative input. (C) Exam-
ples of the PDFs of the activation value of a unit
in the presence (PYGS) and in the absence (PYGA) of
the signal. These are the PDFs ofthe transformed
RVs, YGS = fG(Xs), and YGA = fG(XA). Each
PDF is drawn for two different values of G, in the
case where fG is the logistic.
SCIENCE, VOL. 249
Downloaded from https://www.science.org at University of Newcastle on April 03, 2026

used to categorize the output
as "signal
present" or "signal absent," there will be
some misses and some false alarms. The best
the system can do is to select a threshold that
optimizes performance. More precisely, the
expected payoffor performance ofthe unit is
given by
E(o) = X + a Pr(YGS.
0)
-w
* Pr(YGA- 0)
(2)
where A, a, and w are constants that togeth-
er reflect the prior probability of the signal
and the payoffs associated with correct de-
tections (also called hits), correct ignores,
false
alarms,
and
misses.
Note
that
Pr(YGs
:
0) and Pr(YGA
- 0) are the prob-
abilities of a hit and a false alarm, respective-
ly. By solving the equation dEldO = 0, we
can determine a threshold, 0*, that maxi-
mizes E. We call 0* the optimal threshold.
From examination of Fig. 1, it might be
supposed that, by changing the activation
function, one can improve signal detection
performance. But this is not so. For any
activation function f that satisfies our
as-
sumptions and any fixed input PDFs pxs and
PXA,
the
unit's
performance
at
optimal
threshold is the same. This is our constant
optimal performance theorem (COPT); it is
stated and proved in (11). In particular, for
the logistic, increasing the gain G does not
induce better performance. It may change
the value ofthe threshold that yields optimal
performance, but it does not change the
actual performance at optimum. This is be-
cause a strictly increasing activation function
gives a one-to-one mapping from input to
output values. This makes
it possible to
express Eq. 2 exclusively in terms of the
input PDFs px, and PXA, and a,
w, and X.
Because it is the overlap between pxs and
PXA that limits performance, and because
this overlap does not vary with the gain, the
performance
at optimal threshold
is con-
stant.
We now examine the effect of changing
the gain on the SNR of the output of a
single unit. In electrical
engineering, the
SNR measures the difficulty of extracting a
continuous-time signal
s(t) from
a noisy
background n(t). The SNR compares the
average power input to the receiver in the
presence of the signal,
9' = ([s(t) + n(t)]2),
with the average power input in the absence
of the signal, X = (n(t)2) (12). If s(t) is a
small
perturbation
added
to
n(t),
then
9' J-f,
and
the signal
will
be
difficult
to
detect. On the other hand, if the signal
amplitude is high and the noise amplitude is
low, then
9 >»
X. Thus, the ratio
9/X
measures how difficult it is to distinguish
signal from noise.
In the case of a single unit, if the unit's
input is x, its output is y = fG(x). Because
24 AUGUST 1990
Input unit
Response unit
Fig. 2. A chain of units. The output of the unit
receiving the signal is combined with noise to
provide input to a second unit called the response
unit. The activation of the response unit is com-
pared with a threshold to determine the presence
or absence of the signal.
this quantity represents the firing rate of the
neuron for a given stimulus presentation, if
each neural spike contains the same amount
of energy, the power the neuron delivers
will be proportional to y. Thus, over many
stimulus presentations, the average power
delivered in the presence of signal is propor-
tional to tL(YGS), the mean of YGS, and in
the absence of signal
is proportional
to
[t(YGA). Hence, the ratio of the average
power delivered in the presence ofthe signal
to the average power delivered in the ab-
sence of the signal, that is, the SNR, is
II( YGS)/ XL(YGA) -
In general, raising G will drive up R(YGS)
and drive down
,L(YGA),
increasing the
SNR of a single unit. Yet by the COPT, the
performance ofthe unit at optimal threshold
remains the same, because the effect of an
increase of G on PYS and pYA is not captured
by the mean alone. Increases in G will in
general
alter the shapes of these PDFs,
possibly driving apart the main concentra-
tions of probability mass but simultaneously
extending their tails (Fig. IC). The errone-
ous intuition that separating the means will
improve performance arises from the
as-
sumption that the effect of an increase in G
is to translate the output PDFs rigidly away
from one another. For this
reason,
it
is
misleading to explain the performance ef-
fects of catecholamines solely in terms ofthe
SNR.
Although increasing G does not affect the
signal detection performance of a single
element, it does improve the performance of
a chain of such elements. By a chain, we
mean an arrangement in which the output of
the first unit provides the input to another
unit. Let us call this second element the
response unit. We monitor the output of
this second unit to determine the presence
or absence of a signal (Fig. 2).
As
in the previous
discussion,
noise
is
added to the net input of each unit in the
chain in the
presence
as well
as in the
absence of a signal (13). We represent noise
as a random variable (RV) V, with PDF Pv
that we assume to be independent of gain.
Let the RVs Xs, XA, YGS, YGA, and their
PDFs all be defined as in the single-unit
case. Now, because noise is added to the net
input of the response unit as well, the input
ofthe response unit is the RV ZGS = YGS +
V or ZGA = YGA + V, again depending on
whether the signal is present or absent. We
write PZGS and PZGA for the PDFs of these
RVs. Then PzGS is the convolution of PYGS
and Pv, and PZGA is the convolution of PYGA
and Pv- Convolving the output PDFs of the
input unit with the noise distribution in-
creases the overlap between the resulting
distributions (PzGS and PzGA) and therefore
decreases the discriminability ofthe input to
the response unit.
How are these distributions affected by an
increase in G on the input unit? By the
COPT, we already know that the discrimi-
nability of YGS and YGA
is unchanged.
Furthermore, we have assumed that the
noise distribution is independent of G. It
would therefore seem that a change in G
should not affect the discriminability of ZGS
and ZGA. However, under very general con-
ditions, the overlap between PZGS and PZGA
decreases when the G of the input unit
increases, thereby improving performance
of the two-layered system. We call this the
chain effect.
The chain effect arises because the noise
added to the net input ofthe response unit is
not affected by variations in G. Increasing G
separates the means of the output PDFs of
the input unit, V1(YGs) and ,(YGA), even
though this does not affect the performance
ofthis unit. Suppose all the probability mass
were concentrated at these means. Then PZGS
would be a copy of Pv centered at pL(YGS),
and PZGA would be a copy of Pv centered at
pi(YGS). Thus, in this case, increasing G
would rigidly translate PZGS and PZGA apart,
thereby reducing their overlap and improv-
ing performance. A similar effect arises in
more general circumstances, when YGS and
YGA are not concentrated at their means.
The chain performance theorem, stated and
proved in (11), gives sufficient conditions
for the appearance of this effect.
The above analysis has shown that in-
creasing the G of the activation function of
individual units in a very simple network can
improve signal detection performance. We
now present computer simulation results
showing that this phenomenon can account
for catecholamine-induced performance im-
provements in a common behavioral test of
signal detection.
The continuous performance test (CPT)
(14) has been used extensively to study
attention and vigilance in behavioral and
clinical research. In this task, individual let-
ters are displayed tachystoscopically in a
sequence on a computer monitor. In one
common version ofthe task, a target event is
to be reported when two consecutive letters
are identical. Performance on this task has
been shown to be sensitive to drugs or
REPORTS
893
Downloaded from https://www.science.org at University of Newcastle on April 03, 2026

pathological conditions affecting catechol-
amine systems (15-17). During baseline per-
formance, subjects typically fail to report 10
to 20% of targets ("misses") and inappropri-
ately report a target during 0.5 to 1% of the
remaining events ("false alarms"). After the
administration of agents that directly release
catecholamines from synaptic terminals and
block
re-uptake from
the
synaptic
cleft
(CNS stimulants such as amphetamines or
methylphenidate), the number of misses de-
creases while the number of false alarms
remains
approximately
the
same.
Using
standard measures of signal detection the-
ory, investigators have shown that this pat-
tem of results reflects an improvement in the
discrimination between signal and nonsignal
events (d'), whereas the response criterion
(p) does not vary significantly (16, 17).
We used the backpropagation learning
algorithm (18) to train a recurrent network
of three layers (input layer, intermediate or
hidden layer, and output layer) to perform
the CPT (see Fig. 3A). In this model, several
simplifying assumptions made in the preced-
ing section are removed. First, the network
contains
recurrent
connections.
Second,
connection weights are developed entirely
by the training procedure; as a result, the
activation pattems on the intermediate layer
that are evoked by the presence or absence
of a signal are also determined solely by the
training procedure. Finally, the representa-
tion of the signal
is distributed over an
ensemble of units rather than determined by
a single unit.
After training, Gaussian noise with zero
mean was added to the net input of each
unit in the intermediate and output layers as
each letter was presented. The overall stan-
dard deviation of the noise distribution and
the threshold of the response unit were
adjusted to approximate the performance of
human subjects under baseline conditions
[human subjects: 11.7% misses and 0.6%
false alarms (16); simulation: 13.0% misses
and 0.75% false alarms]. We then increased
the G of all the intermediate and output
units from 1.0 to 1.1 to simulate the effect of
catecholamine release in the network. This
manipulation
resulted
in
rates of 6.6%
misses and 0.78% false alarms [human sub-
jects: 5.5% misses and 0.5% false alarms
with methylphenidate (16); see Fig. 3B].
The enhancement of signal detection per-
formance in the simulation is a robust effect.
It appears when G is increased in the inter-
mediate layer only, in the letter units only,
or in both. Because of the recurrent connec-
tions between the letter units and the inter-
mediate layer, the chain effect appears when
G is increased over either or both of them.
The impact of the chain effect is to reduce
the distortion, due to internal noise, of the
distributed representation on the layer re-
ceiving inputs from the layer where G is
increased. The improvement
takes
place
even when there is no noise added to the
Fig. 3. Simulation of the continuous performance
A
task. (A) Diagram of recurrent three-layer net-
0
work (12 input units, 30 intermediate units, 10
Response unit
Output layer
Letter units
output units, and 1 response unit). Each unit
0
0
projects to all units in the subsequent layer. In
addition, each output unit also projects to each
'.
unit in the intermediate layer. Letters are present-
0
i
ed to the network as patterns of activation over
O 0
Intermediate layer
the input units, which act as feature detectors.
During training, the network learns to activate
the output unit corresponding to the letter being
0
presented on the input. In addition, the recurrent
connections provide the network with the pattern
OFeature units
Input layer
of activation evoked on the output layer by the
0
(D
presentation of the previous letter. The network
learns to activate the response unit when two
consecutive letters are identical and to turn it off
B
in all other cases. The activation of a unit in the
15
intermediate or output layer depends on the
activations of all units in the layers providing
input to it. Each input is weighted by the corre-
sponding connection strength, which can be posi-
@
10
tive or negative. The sum of the weighted inputs
\
is then passed through the logistic function to
\
determine the unit's activation. The gain parame-
,
ter G is the same for all intermediate and output
5
units. In the simulation of the placebo condition,
G = 1.0; in the simulation ofthe drug condition,
G = 1.1. Bias B is -1 in both conditions. (B)
._
_
_
Performance ofhuman subjects and ofthe simula-
Placebo
CNS stimulant
tion on the CPT. Filled markers indicate the
performance of human subjects with placebo and methyphenidate (16). Empty markers indicate the
results of the simulation.
input of the response unit. The response
unit in this network acts only as an Tndi-
cator of the strength of the signal in the
intermediate layer. Finally, as the COPT
predicts, increasing G only on the response
unit does not affect the performance of the
network.
In this simulation, as well as in the preced-
ing discussion, increasing G appears to have
only the beneficial effect of making it easier
to distinguish between the presence and
absence of a signal. Nevertheless, it is possi-
ble to speculate about drawbacks of higher
G values in a biological system. First, at
lower G, the presence of noise guarantees
some variability in response selection. High-
er G may induce stereotyped responses.
Variability of responses may be a necessary
and adaptive feature of biological systems,
particularly in the context of new environ-
ments and during learning.
Second, we have seen that increasing G
reduces the effect of noise in a multilayer
network. However, under some circum-
stances, what we have regarded as noise may
be the expression of a weak signal that is
competing with a stronger signal for trans-
mission. In some situations, this weak signal
may undergo progressive enhancement in
subsequent layers of the network and ulti-
mately be an important determinant of the
system's response. With high values of G,
the representation of this weaker signal
would be eliminated early in processing, in
favor of the stronger signal.
Finally, although operating at a high G
improves signal detection performance,
it
may be energetically draining. Cortical neu-
rons appear to operate at high G in states of
wakefulness and arousal and at low G dur-
ing sleep (19), and autoradiography studies
suggest a correlation between catecholamine
release and increased deoxyglucose metabo-
lism (20). These observations are not sur-
prising. The communication channels in the
brain,
like
all communication pathways,
have finite bandwidths, determined by their
physical characteristics. The information ca-
pacity of such channels, operating in the
presence of noise, is a function of the power
emitted into them to transmit a signal (21).
Hence,
sending
information
over
these
channels at the rates associated with wakeful
or alert behavior (that
is,
at higher G)
requires higher power consumption or an
increased rate of energy expenditure.
REFERENCES AND NOTES
1. S. E. Loughlin, S. L. Foote, J. H. Fallon, Brain Res.
Bull. 9, 287 (1982); 0. Lindvall and A. Bjorklund,
Neurol. Neurobiol. N.Y. 10, 9 (1984).
2. The effect of catecholamines on target cells is gener-
ally characterized as an enhancement of stimulus-
elicited responses with respect to background firing
SCIENCE, VOL. 249
894-
Downloaded from https://www.science.org at University of Newcastle on April 03, 2026
