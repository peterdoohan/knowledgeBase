bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 1 A theory of multineuronal dimensionality, dynamics and 2 measurement 

3 Peiran Gao[1] , Eric Trautmann[2] , Byron Yu[3] , Gopal Santhanam[4] , Stephen Ryu[5,4] , Krishna 4 Shenoy[4,1,6,7,8,9] and Surya Ganguli _[∗]_[10,2,4,8,9] 

1 5 Department of Bioengineering, Stanford University, Stanford, CA 94305, USA 2 6 Neurosciences Program, School of Medicine, Stanford University, Stanford, CA 94305, 7 USA 

3 8 Department of Electrical Computer Engineering and Biomedical Engineering, Carnegie 9 Mellon University, Pittsburgh, PA 15213, USA 

4 10 Department of Electrical Engineering, Stanford University, Stanford, CA 94305, USA 

5 11 Department of Neurosurgery, Palo Alto Medical Foundation, Palo Alto, CA 94301, USA 

6 12 Department of Neurobiology, School of Medicine, Stanford University, Stanford, CA 13 94305, USA 

14 

15 

16 

17 

7Howard Hughes Medical Institute, Stanford University, Stanford, CA 94305, USA 

8Bio-X Programs, Stanford University, Stanford, CA, 94305, USA 

9Stanford Neurosciences Institute, Stanford University, Stanford, CA 94305, USA 

10Department of Applied Physics, Stanford University, Stanford, CA 94305, USA 

18 

## November 4, 2017 

19 **Abstract** 

- 20 In many experiments, neuroscientists tightly control behavior, record many trials, and obtain trial-averaged 21 firing rates from hundreds of neurons in circuits containing billions of behaviorally relevant neurons. Di22 mensionality reduction methods reveal a striking simplicity underlying such multi-neuronal data: they can 23 be reduced to a low-dimensional space, and the resulting neural trajectories in this space yield a remarkably 24 insightful dynamical portrait of circuit computation. This simplicity raises profound and timely conceptual 25 questions. What are its origins and its implications for the complexity of neural dynamics? How would the 26 situation change if we recorded more neurons? When, if at all, can we trust dynamical portraits obtained 27 from measuring an infinitesimal fraction of task relevant neurons? We present a theory that answers these 28 questions, and test it using physiological recordings from reaching monkeys. This theory reveals conceptual 29 insights into how task complexity governs both neural dimensionality and accurate recovery of dynamic 30 portraits, thereby providing quantitative guidelines for future large-scale experimental design. 

> _∗_ sganguli@stanford.edu 

1 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 31 **1 Introduction** 

- 32 In this work, we aim to address a major conceptual elephant residing within almost all studies in mod33 ern systems neurophysiology. Namely, how can we record on the order of hundreds of neurons in regions 34 deep within the brain, far from the sensory and motor peripheries, like mammalian hippocampus, or pre35 frontal, parietal, or motor cortices, and obtain scientifically interpretable results that relate neural activity 36 to behavior and cognition? Our apparent success at this endeavor seems absolutely remarkable, consid37 ering such circuits mediating complex sensory, motor and cognitive behaviors contain _O_ (10[6] ) to _O_ (10[9] ) 38 neurons [Shepherd, 2004] - 4 to 7 orders of magnitude more than we currently record. Or alternatively, we 39 could be completely misleading ourselves: perhaps we should not trust scientific conclusions drawn from 40 statistical analyses of so few neurons, as such conclusions might become qualitatively different as we record 41 more. Without an adequate theory of neural measurement, it is impossible to _quantitatively_ adjudicate where 42 systems neuroscience currently stands between these two extreme scenarios of success and failure. 43 One potential solution is an experimental one: simply wait until we can record more neurons. Indeed, 44 exciting advances in recording technology over the last several decades have lead to a type of Moore’s 45 law in neuroscience: an exponential growth in the number of neurons we can simultaneously record with a 46 doubling rate of 7.4 years since the 1960’s [Stevenson and Kording, 2011]. Important efforts like the BRAIN 47 Initiative promise to ensure such growth in the future. However, if we simply extrapolate the doubling rate 48 achieved over the last 50 years, we will require about 100 to 200 years to record 4 to 7 orders of magnitude 49 more neurons. Thus, for the near future, it is highly likely that measurements of neural dynamics at single 50 cell, single spike-time resolution in mammalian circuits controlling complex behaviors will remain in the 51 highly sub-sampled measurement regime. Therefore we need a theory of neural measurement that addresses 52 a fundamental question: how and when do statistical analyses applied to an infinitesimally small subset of 53 neurons reflect the collective dynamics of the much larger, unobserved circuit they are embedded in? 54 Here we provide the beginnings of such a theory, that is quantitatively powerful enough to (a) formu55 late this question with mathematical precision, (b) make well defined, testable predictions that guide the 56 interpretation of past experiments, and (c) provide a theoretical framework to guide the design of future 57 large scale recording experiments. We focus in this work on an extremely commonly used experimental 58 design in which neuroscientists repeat a given behavioral or cognitive task over many trials, and record 59 the trial averaged neural dynamics of many neurons. An advantage of this design, which has promoted 60 its widespread usage, is that the neurons need not be simultaneously recorded. This resulting trial average 61 firing rate dynamics can be thought of as a collection of neural trajectories exploring a high dimensional 62 neural space, with dimensionality equal to the number of recorded neurons (see e.g. Fig 1 below for a con63 ceptual overview). They reflect a fundamental description of the state space dynamics of the neural circuit 64 during cognition and behavior. Almost always, such trajectories are analyzed via dimensionality reduction 65 (see [Cunningham and Yu, 2014] for a review), and almost ubiquitously, a large fraction of variance in these 66 trajectories lives in a much lower dimensional space. 

- 67 The resulting neural trajectories in the low dimensional space often provide a remarkably insightful dy68 namical portrait of circuit computation during the task in a way that is inaccessible through the analysis 69 of individual neurons [Briggman et al., 2006]. For example, curvature in the geometry of these dynamical 70 portraits recovered from macaque prefrontal cortex by [Mante et al., 2013] revealed a novel computational 71 mechanism for contextually-dependent integration of sensory evidence. Similarly, dimensionality reduction 72 by [Machens et al., 2010] uncovered dynamical portraits which revealed that macaque somatosensory cor73 tices compute both stimulus frequency and time in a functionally but not anatomically separable manner 74 in a tactile discrimination task. Dynamical portraits obtained by [Mazor and Laurent, 2005] revealed that 75 neural transients in insect olfactory areas rapidly computed odor identity long before the circuit settled to 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 76 a steady state. And an analysis of neural dynamics in macaque parietal cortex showed that the dynamical 77 portraits were largely one-dimensional, revealing an emergent circuit mechanism for robust timing in atten78 tional switching and decision making [Ganguli et al., 2008a]. Also, the low-dimensional activity patterns 79 found in primary motor-cortex provide causal constraints learning itself [Sadtler et al., 2014] . 

- 80 Given the importance of these dynamical portraits as a first window into circuit computation, it is im81 portant to ask if we can trust them despite recording so few neurons? For example, would their geometry 82 change if we record more neurons? How about their dimensionality? The ubiquitous low dimensionality of 83 neural recordings suggests an underlying simplicity to neural dynamics; what is its origin? How does the 84 number of neurons we need to record to accurately recover dynamical portraits scale with the complexity of 85 the task, and properties of the neural dynamics? Indeed which minimal properties of neural dynamics are 86 important to know in order to formulate and answer this last question? 

- 87 Our theory provides a complete answer to these questions within the context of trial averaged experimen88 tal design. Central to our theory are two main conceptual advances. The first is the introduction of neural task 89 complexity (NTC), a mathematically well defined quantity that takes into account both the complexity of 90 the task, and the smoothness of neural trajectories across task parameters. Intuitively, the NTC measures the 91 volume of the manifold of task parameters, in units of the length scales over which neural trajectories vary 92 across task parameters, and it will be small if tasks are very simple and neural trajectories are very smooth. 93 We prove that this measure upper bounds the dimensionality of neural state space dynamics. This theorem 94 has important implications for systems neuroscience: it is likely that the ubiquitous low dimensionality of 95 measured neural state space dynamics is due to a small NTC. In any such scenario, simply recording many 96 more neurons than the NTC, while repeating the same simple task will not lead to richer, higher dimensional 97 datasets; indeed data dimensionality will become independent of the number of recorded neurons. One 98 would have to move to more complex tasks to obtain more complex, higher dimensional dynamical portraits 99 of circuit computation. 

- 100 The second conceptual advance is a novel theoretical link between the act of neural measurement and a 101 technique for dimensionality reduction known as random projections. This link allows us to prove that, as 102 long as neural trajectories are sufficiently randomly oriented in state space, we need only record a number 103 of neurons proportional to the product of the number of task parameters and the _logarithm_ of the NTC. This 104 theorem again has significant implications for systems neuroscience. Indeed, it quantitatively adjudicates 105 between the two extremes of success or failure raised above, fortunately, in the direction of success: it 106 is highly likely that low dimensional dynamical portraits recovered from past experiments are reasonably 107 accurate despite recording so few neurons, because those tasks were so simple, leading to a small NTC. 108 Moreover, as we begin to move to more complex tasks, this theorem provides rigorous guidance for how 109 many more neurons we will need to record in order to accurately recover the resulting more complex, higher 110 dimensional dynamical portraits of circuit computation. 

- 111 Below, we build up our theory step by step. We first review the process of recovering state space dy112 namical portraits through dimensionality reduction in neuroscience. We then introduce the notion of NTC, 113 and illustrate how it provides an upper bound on neural dimensionality. Then we review the notion of ran114 dom projections, and illustrate how the NTC of an experiment _also_ determines how many neurons we must 115 record to accurately obtain dynamical portraits. Along the way, we extract a series of experimentally testable 116 predictions, which we confirm in neural recordings from the motor and premotor cortices of monkeys per117 forming reaches to multiple directions. We end in the discussion with an intuitive summary of our theory 118 and its implications for the future of large scale recordings in systems neuroscience. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 119 

## **2 Recovery of neural state space dynamics through dimensionality reduction** 

120 Imagine an experiment in which a neuroscientist records trial averaged patterns of neural activity from a set 121 of _M_ neurons across time. We denote by **x** _i_ ( _t_ ) the trial averaged firing rate of neuron _i_ at time _t_ . These data 122 are often visualized by superimposing the firing rates of each neuron across time (Fig. 1A). Alternatively, 123 these data can be thought of as a neural trajectory in an _M_ dimensional space (Fig. 1B). At each time, the 124 measured state of the neural circuit consists of the instantaneous pattern of activity across _M_ neurons, which 125 corresponds to a point in _M_ dimensional space, where each dimension, or axis in the space corresponds to 126 the firing rate of one neuron. As time progresses, this point moves, tracing out the neural trajectory. 

**==> picture [226 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Population Activities B Neural Space<br>time<br>C D Dim Reduced Projection<br>c1<br>×<br>+<br>×<br>c2 time c1<br>nrn2<br>c2<br>nrn1<br>c1<br>normalized rate nrn3<br>c2<br>neurons<br>**----- End of picture text -----**<br>


Figure 1: **Conceptual overview of state space dynamics through dimensionality reduction. (A)** The trial averaged firing rate dynamics of _M_ neurons. **(B)** This data can be equivalently thought of as tracing out a neural state space trajectory in an _M_ dimensional firing rate space with one axis per neuron. Here only three of the _M_ axes are shown, and as illustrated, sometimes such a trajectory can be largely confined to a lower dimensional subspace, here a two dimensional subspace. **(C)** A decomposition of the data in **(A)** into two static spatial patterns across neurons (red and blue patterns, left). The population activity pattern at each instant of time is a weighted sum of the two static _basis_ patterns, where the weighting coefficients (red and blue traces, right) depend on time. If all population patterns across time can largely be explained by linear combinations of these two patterns, then the neural trajectory corresponding to the data in **(A)** will be largely confined to explore a two dimensional subspace within _M_ dimensional firing rate space, shown for example in **B** . Two special points in the subspace correspond to the two basis patterns in **(C)** , i.e. the endpoints of the two red and blue vectors in **(B)** , and the subspace is spanned by all linear combinations of these two patterns. **(D)** . One can then accurately visualize the state space dynamics in pattern space, by plotting the time-dependent weighting coefficients in **(C)** against each other. Each axis in pattern space corresponds to how much each basis pattern is present in the neural population. 

127 It is difficult to directly understand or visualize this trajectory, as it evolves in such a high-dimensional 128 ambient space. Here dimensionality reduction is often used to simplify the picture. The main idea behind 129 many linear dimensionality reduction methods is to decompose the entire set of dynamic neural activity 130 patterns across neurons, unfolding over time, into a time dependent linear combination of a fixed set of 131 static patterns across neurons (Fig. 1C). The hope is that the data can be dramatically simplified if a linear 132 combination of a small number of static basis patterns are sufficient to account for a large fraction of variance 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

133 in the data across time. When this is the case, the neural state space dynamics can unfold over time in a much 134 lower dimensional pattern space, whose coordinates consist of how much each static pattern is present in the 135 neural population (Fig. 1D). 

136 Mathematically, the decomposition illustrated in Fig. 1C can be written as **x** _i_ ( _t_ ) =[�] _[D] α_ =1 **[u]** _i[α][c][α]_[(] _[t]_[)][,] 137 where each _M_ dimensional vector **u** _[α]_ is a static basis pattern across neurons, each _cα_ ( _t_ ) is the amplitude of 138 that pattern across time (Fig.1C), and _D_ denotes the number of patterns or dimensions retained. Principal 139 components analysis (PCA) is a simple way to obtain such a decomposition (see Supplementary Material for 140 a review). PCA yields a sequence of basis patterns **u** _[α]_ , _α_ = 1 _, . . . , M_ each accounting for a different amount 141 of variance _µ[α]_ in the neural population. The patterns can be ordered in decreasing amount of variance 142 explained, so that _µ_ 1 _≥ µ_ 2 _≥, . . . , ≥ µM_ . By retaining the top _D_ patterns, one achieves a fraction of 143 variance explained given by _χ_[2] = _µ_ 1[Tot] � _Dα_ =1 _[µ][α]_[, where] _[ µ]_[Tot][=][�] _[M] α_ =1 _[µ][α]_[is the total variance in the neural] 144 population. Dimensionality reduction is considered successful if a small number of patterns _D_ relative to 145 number of recorded neurons _M_ , accounts for a large fraction of variance explained in the neural state space 146 dynamics. 

147 How well does dimensionality reduction perform in practice in neurophysiology data? We have per148 formed a meta-analysis (Fig. 2) of a diverse set of 20 experiments spanning a variety of model organisms 149 (macaques, rodents, and insects), brain regions (hippocampal, prefrontal, parietal, somatosensory, motor, 150 premotor, visual, olfactory and brainstem areas), and tasks (memory, decision making, sensory detection 151 and motor control). This meta-analysis reveals that dimensionality reduction as a method for simplifying 152 neural population recordings performs exceedingly well. Indeed it reflects one of the most salient aspects of 153 systems neurophysiology to have emerged over the last couple of decades: namely that neuronal recordings 154 are often far lower dimensional than the number of recorded neurons. Moreover, in each of these works, the 155 associated low dimensional dynamical portraits provide insights into relations between neural population 156 activity and behavior. Despite this almost ubiquitous simplicity found in neural population recordings, prior 157 to this work, we are unaware of any simple, experimentally testable theory that can quantitatively explain 158 the dimensionality and accuracy of these recovered dynamical portraits. 

## 159 

## **3 Neural Task Complexity and Dimensionality** 

- 160 We now begin to describe such a theory. Central to our theory is the notion of neural task complexity 161 (NTC), which both upper bounds the dimensionality of state space dynamics and quantifies how many 162 neurons are required to accurately recover this dynamics. Here, we first consider the dimensionality of the 163 dynamics, and later we consider the accuracy of the dynamics. To introduce the NTC intuitively, imagine 164 how many dimensions a single neural trajectory could possibly explore. Consider for concreteness, the trial 165 averaged neural population activity while a monkey is performing a simple reach to a target (Fig. 3AB). This 166 average reach lasts a finite amount of time _T_ , which for example could be about 600ms. The corresponding 167 neural trajectory (Fig. 3C) can explore neural space for this much time, but it cannot change direction 168 infinitely fast. The population response is limited by an autocorrelation time _τ_ (see supplementary methods 169 for details). Roughly, one has to wait an amount of time _τ_ before the neural population’s activity pattern 170 changes appreciably (Fig. 3B) and therefore the neural trajectory can bend to explore another dimension 171 (Fig. 3C). This implies that the maximal number of dimensions the state space dynamics can possibly 172 explore is proportional to _T/τ_ . Of course the constant of proportionality is crucial, and our theory, applicable 2 

- 173 to reaching data described below, computes this constant to be ~~�~~ _π_[(see supplementary material for a proof] 174 and a definition of _τ_ ), yielding, for this experiment, an _NTC_ = � _π_ 2 _Tτ_[.] 175 Now most tasks have more than just time as a parameter. Consider a slightly more complex experiment in 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

**==> picture [196 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
Mante and Sussillo et al., 2013*<br>1 Churchland et al., 2012+<br>6/842 Bromberg−Martin et al., 2010<br>Haddad et al., 2010<br>0.8 3/143 8/125 Machens et al., 2010<br>3/45 Raman et al., 2010<br>3/65 8/88 Luo et al., 2010<br>0.6 3/300 10/1288/1106/74 Peyrache et al., 2009Narayanan and Laubach, 2009<br>2/72 Bathellier et al., 2008<br>3/100 6/55 Fantana et al., 2008<br>3/100 Assisi et al., 2007<br>0.4 1/20 Sasaki et al., 2007<br>2/6322/135 2/993/1103/53 Briggman et al., 2005Mazor and Laurent, 2005*<br>1/179 3/99 Paz et al., 2005<br>0.2 12/7271/23 Matsumoto et al., 2005<br>12/993 1/20 3/37 Hegde and Van Essen, 2004*Stopfer et al., 2003<br>Chapin and Nicolelis, 1999<br>0<br>0 0.2 0.4 0.6 0.8 1<br>dimensionality / # recorded units<br>fraction of variance explained<br>**----- End of picture text -----**<br>


Figure 2: **The ubiquity of low dimensionality relative to number of recorded neurons.** In many experiments (e.g. in insect [Stopfer et al., 2003, Mazor and Laurent, 2005, Assisi et al., 2007, Raman et al., 2010, Haddad et al., 2010] olfactory systems, mammalian olfactory [Bathellier et al., 2008, Haddad et al., 2010], prefrontal [Narayanan and Laubach, 2009, Peyrache et al., 2009, Machens et al., 2010, Warden and Miller, 2010, Mante et al., 2013], motor and premotor,[Paz et al., 2005, Churchland et al., 2012], somatosensory [Chapin and Nicolelis, 1999], visual [Hegd´e and Van Essen, 2004, Matsumoto et al., 2005], hippocampal [Sasaki et al., 2007], and brain stem [Bromberg-Martin et al., 2010] systems) a _much_ smaller number of dimensions than the number of recorded neurons captures a large amount of variance in neural firing rates. 

176 which a monkey reaches to 8 different targets (Fig. 3D). Now the manifold of trial averaged task parameters 177 is a cylinder, parameterized by time _t_ into the reach and reach angle _θ_ (Fig. 3E). Since for each time _t_ and 178 angle _θ_ , there is a corresponding trial averaged neural activity pattern across neurons **x** _i_ ( _θ, t_ ), the neural state 179 space dynamics is fundamentally an embedding of this task manifold into neural space, yielding a curved 180 intrinsically two dimensional neural manifold that could potentially explore many more than two dimensions 181 in firing rate space by curving in different ways (Fig. 3F). How many dimensions could it possibly explore? 182 Well the same argument that we made for time into a reach at fixed angle, also holds for reaching across 183 all angles at a fixed time into the reach. The total extent of angle is 2 _π_ . Moreover, the neural population 184 response cannot vary infinitely fast across angle; it has a spatial autocorrelation length ∆. Intuitively, this 185 means that the two patterns of activity **x** _i_ ( _θ_ 1 _, t_ ) and **x** _i_ ( _θ_ 2 _, t_ ) across neurons at two different reach angles _θ_ 1 186 and _θ_ 2 at the same time _t_ will not be appreciably different unless _|θi − θj| >_ ∆. Roughly, one can think of 187 ∆ as the average width of single neuron tuning curves across reach angle. 

187 188 Thus, just as in the argument for time, because the total angle to be explored is limited to 2 _π_ , and patterns 189 are largely similar across angular separations less than ∆, the maximal number of dimensions a single circle 190 around the neural manifold at any fixed time could explore, is proportional to[2] ∆ _[π]_[, where the proportionality] 

- 191 constant is again � _π_ 2[.][Now][intuitively,][the][number][of][dimensions][the][full][neural][manifold][could][explore] 192 across both time and angle would be maximized if these explorations were independent of each other. Then 193 the maximal dimensionality would be the product of � _π_ 2 _Tτ_[and] � _π_ 2 2∆ _π_[(see][supplementary][material][for][a] 194 proof), yielding an NTC = 4 _[T] τ_ ∆1[.] 195 More generally, consider a task that has _K_ task parameters indexed by _k_ = 1 _, . . . , K_ , each of which 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

**==> picture [352 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Reach to a Single Target B Population Firing Rates C Neural Trajectory<br>τ τ<br>τ<br>τ<br>0 300<br>time (ms)<br>D Reaches to All Directions E Task Parameter Manifold F Neural Data Manifold<br>reach reach<br>angles angles<br>neuron 2<br>neuron 2<br>neuron 1<br>neuron 1<br>time time<br>nrn3<br>normalized rate<br>neuron 3<br>**----- End of picture text -----**<br>


Figure 3: **Trial averaged neurophysiology as an embedding of a task manifold into a neural manifold. (A)** A monkey reaching to a single target. The task is parameterized simply by time _t_ . **(B)** Schematic of neuronal firing rate data during the reach, and **(C)** the associated neural trajectory. **(D)** A monkey reaching to several targets. **(E)** The associated task manifold is a cylinder parameterized by time into the reach and reach angle. **(F)** The neural state space dynamics is a smooth embedding of the task manifold into neural firing rate space. 

196 

vary over a range _Lk_ , and for which neural activity patterns have a correlation length _λk_ . Then the NTC is 

**==> picture [258 x 29] intentionally omitted <==**

197 For example, in the special case of reaches to all angles we have considered so far, we have _K_ = 2, _L_ 1 = _T_ , 198 _λ_ 1 = _τ_ , _L_ 2 = 2 _π_ , _λ_ 2 = ∆, and _C_ = _π_[2][.][In the general case, our theory (see supplementary material) pro-] 199 vides a precise method to define the autocorrelation lengths _λk_ , in a manner consistent with the intuition that 200 a correlation length measures how far one has to move in behavioral manifold, to obtain an appreciably dif201 ferent pattern of activity across neurons in the neural manifold (Fig. 3EF). Moreover, our theory determines 202 the constant of proportionality _C_ , as well as provides a proof that the neural dimensionality _D_ , measured 203 by the participation ratio of the PCA eigenvalue spectrum (see methods) is less than the minimum of the 204 number of recorded neurons _M_ and the _NTC_ : 

**==> picture [259 x 11] intentionally omitted <==**

205 Also, in the supplementary material, we consider a much simpler scenario in which there are a finite set of _P_ 206 neural activity patterns, for example in response to a finite set of _P_ stimuli. There, the NTC is simply _P_ , and 207 we compute analytically how measured dimensionality _D_ increases with number of recorded neurons _M_ , 208 and how it eventually asymptotes to the NTC if there are no further constraints on the neural representation. 209 In the following, however, we focus on the much more interesting case of neural manifolds in (1). 

210 We note that the NTC in (1) takes into account two very distinct pieces of information. First, the nu211 merator only knows about the task design; indeed it is simply the volume of the manifold of task parameters 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 212 (e.g. Fig. 3E). The denominator on the other hand requires knowledge of the smoothness of the neural 213 manifold; indeed it is the volume of an autocorrelation cell over which population neural activity does not 214 change appreciably across _all K_ task parameters. Thus the theorem (2) captures the simple intuition that 215 neural manifolds of limited volume and curvature (e.g. Fig. 3CF ) cannot explore that many dimensions 216 (though they could definitely explore fewer than the NTC). However, as we see below the precise theorem 217 goes far beyond this simple intuition, as it provides a quantitative framework to guide the interpretation of 218 past experiments and design future ones. 

## 219 

## **4 A Dimensionality Frontier in Motor Cortical Data** 

- 220 To illustrate the interpretative power of the NTC, we re-examined the measured dimensionality of neural 221 activity from the motor and premotor cortices of two monkeys, H and G, recorded in [Yu et al., 2007], 222 during an eight-direction center-out reach task, as in Fig. 3D (see also, Methods). The dimensionality of 223 the entire dataset, i.e. the number of dimensions explored by the neural manifold in Fig. 3F, was 7.1 for 224 monkey H and 4.6 for monkey G. This number is far less than the number of recorded single units, which 225 were 109 and 42 for monkeys H and G respectively. So a natural question is, how can we explain this order 226 of magnitude discrepancy between the number of recorded units and the neural dimensionality, and would 227 the dimensionality at least increase if we recorded more units? In essence, what is the origin of the simplicity 228 implied by the low dimensionality of the neural recordings? 

- 229 Here, our theorem (2) can provide conceptual guidance. As illustrated in Fig. 4A, our theorem in general 230 implies that experiments in systems neurophysiology can live within 3 qualitatively distinct experimental 231 regimes, each with its own unique predictions. First, the dimensionality _D_ could be close to the number of 232 recorded neurons _M_ but far less than the NTC. This scenario suggests one may not be recording enough 233 neurons, and that the dimensionality and accuracy of dynamic portraits may increase when recording more 234 neurons. Second, the dimensionality may be close to the NTC but far below the number of neurons. This 235 suggests that the task is very simple, and that the neural dynamics is very smooth. Recording more neurons 236 would not lead to richer, higher dimensional trial averaged dynamics; the only way to obtain richer dynamics, 237 at least as measured by dimensionality, is to move to a more complex task. Finally, and perhaps most 238 interestingly, in the third regime, dimensionality may be far less than both the NTC and the number of 239 recorded neurons. Then, and only then, can one say that the dimensionality of neural state space dynamics is 240 constrained by neural circuit properties above and beyond constraints imposed by the simplicity of the task 241 and the smoothness of the dynamics alone. 

242 Returning to the motor cortical data, it is clear that scenario (i) is ruled out in this experiment. But 243 without the definition and computation of the NTC, one cannot distinguish between scenarios (ii) and (iii). 244 We computed the spatial and temporal autocorrelation lengths of neural activity across reach angle and time, 245 and found them to be ∆= 1 _._ 82 radians and _τ_ = 126 ms in monkey H, and ∆= 1 _._ 91 radians and _τ_ = 146 246 ms in monkey G. Given that the average reach duration is _T_ = 600 ms in both monkeys, the NTC = 4 _[T] τ_ ∆1 247 is 10 _._ 5 for monkey H and 8 _._ 6 for monkey G. Comparing these NTCs to the dimensionalities _D_ = 7 _._ 1 for 248 monkey H and _D_ = 4 _._ 6 for monkey G, and the number of recorded neurons _M_ = 109 for monkey H and 249 _M_ = 42 for monkey G (see Fig. 4B), we see that this experiment is deep within experimental regime (ii) in 250 Fig. 4A. 

251 This deduction implies several striking predictions for motor cortical dynamics. First, assuming the rest 252 of the unrecorded neurons are statistically homogenous to the recorded neurons (implying that population 253 smoothness _τ_ and ∆ would not change much as we added more neurons to our measured population), 254 then if we were to record more neurons, even roughly all 500 million neurons in macaque motor cortex, 255 the dimensionality of the neural manifold in each monkey would not exceed 10.5 and 8.6 respectively. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

**==> picture [316 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Dimensionality Frontier C Fixed Angle D Fixed Time<br>4<br>109 4 109<br>72 72<br>36 36<br># neurons<br>i<br>ii iii<br>Monkey H 1 Monkey H<br>1<br>neural task complexity 1 T / τ 4 3 2π / ∆ 5<br>B Manifold Dimensionality 4<br>4<br># neurons 42 42<br>NTC 21 21<br>80 dim (PR)<br>40<br>Monkey G 1 Monkey G<br>0 1<br>Monkey H Monkey G 1 T / τ 4 3 2π / ∆ 5<br>NTC<br>dimensionality dimensionality dimensionality<br>dimensionality dimensionality<br>**----- End of picture text -----**<br>


Figure 4: **A Dimensionality frontier in motor cortical data** . **(A)** A schematic of the dimensionality frontier imposed by theorem (2). Allowed possibilities of dimensionality _D_ and neural task complexity, NTC, exhibit 3 distinct regimes: (i) the number of recorded neurons _M_ but not NTC restricts dimensionality, (ii) NTC but not _M_ restricts _D_ , and (iii) _D_ is far less than both _M_ and _NTC_ , reflecting an unexplained circuit constraint beyond smoothness and task simplicity. **(B)** The number of recorded neurons _M_ , neural task complexity, NTC and dimensionality _D_ are 109, 10.5, and 7.1 respectively for Monkey H, and 42, 8.6 and 4.6 for monkey G. **(C)** Dimensionality and NTC as we explore segments of neural trajectories of different durations at fixed angle, on the full neural manifold in Fig 3E. Temporal segments of different durations were chosen from a uniform distribution between 100ms and 600ms from all reach angles. For each segment we computed its dimensionality and plotted it against its own _[T] τ_[ratio to obtain the scatter plot.][The red curve] indicates the dimensionality frontier, predicted by theory to be proportional to _[T] τ_[.] **[(D)]**[ Dimensionality and NTC as we] explore along all angles on the neural manifold in 3E at fixed times. Relative to movement onset, at each 10ms interval we computed the number of dimensions explored across angles against[2] ∆ _[π]_[to obtain the scatter plot.][Due to the natural] variability in the time-dependent population tuning width, we were able to obtain ∆’s of different values. The red curve indicates the dimensionality frontier, predicted by theory to be proportional to[2] ∆ _[π]_[.][Moreover in][both] **[(C)]**[and] **[(D)]**[,][we] repeat the above analyses, while discarding a randomly chosen one third (red triangles) or two thirds (blue circles) of the recorded neurons for monkey H (top panels) and one half (red triangles) of the recorded neurons for monkey G (bottom panels). 

256 Equivalently, if we were to drop a significant fraction of neurons from the population, the dimensionality 257 would remain essentially the same. In essence, dimensionality would be largely _independent_ of the number 258 of recorded neurons. The second prediction is that if we were to vary the NTC, by varying the task, then this 259 would have a significant impact on dimensionality: it would be proportional to the NTC. 260 We confirm both of these predictions in Fig. 4CD. First, in the given dataset, we cannot increase the NTC 261 further, but we can reduce it by restricting our attention to subsets of reach extents and angles. In essence we 262 explore restricted one-dimensional slices of the full neural manifold in Fig. 3F as follows. First, in Fig. 4B, 263 we explore different random time intervals at different fixed angles, and we plot the dimensionality explored 264 by the segment of neural trajectory against the duration _T_ of the trajectory divided by its autocorrelation _τ_ . 265 Moreover, we vary the number of recorded neurons we keep in our analysis. Second, in Fig. 4C, we pick 266 different times and we plot the number of dimensions explored by the neural manifold (now a circle) across 267 all angles at each chosen time, against[2] ∆ _[π]_[, where][ ∆][is the smoothness parameter of the neural circle at that] 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

268 time, again also varying the number of neurons in our analysis. As can be clearly seen, in both monkeys 269 the predictions of the theory in experimental regime (ii) in Fig. 4A are confirmed: dimensionality is largely 270 independent of the number of recorded neurons, and it hugs closely the dimensionality frontier set by the 271 NTC. 

272 Overall, these results suggest a conceptual revision in the way we may wish to think about neural com273 plexity as measured by its dimensionality. Essentially, neural state space dynamics should not be thought 274 of as inherently simple just because its measured dimensionality is much less than the number of recorded 275 neurons. Instead, by properly comparing dimensionality to neural task complexity, we find neural state space 276 dynamics in motor cortex is as complex and as high-dimensional as possible given basic task constraints and 277 neural smoothness constraints. In essence, the neural state space dynamics represented in Fig. 3F is curving 278 as much as possible within its speed limits set by spatiotemporal autocorrelation lengths, in order to control 279 reaching movements. 

280 We note that theorem (2) is not circular; i.e. it is not tautologically true that every possible measured 281 neural state space dynamics, assuming enough neurons are recorded, will have dimensionality close to the 282 NTC. In the supplementary material, we exhibit an analytical example of a very fast neural circuit, with 283 a small temporal autocorrelation _τ_ , recorded for a long time _T_ , that nevertheless has dimensionality _D_ 284 much less that _[T] τ_[because the connectivity is designed to amplify activity in a small number of dimensions] 285 and attenuate activity in all others, similar to the way non-normal networks have been proposed to play a 286 functional role in sequence memory [Ganguli et al., 2008b]. Finally, what kind of neural dynamics would 287 have a maximal dimensionality, equal to its NTC? As we show in the Supplementary material, a random 288 smooth manifold, with no other structure beyond smoothness, has such maximal dimensionality. 

## 289 **5 Beyond dimensionality: accurate recovery of the geometry of dynamical portraits** 

290 The above theory reveals a simple sufficient condition under which the dimensionality of dynamical portraits 291 would remain unchanged if we recorded more neurons: namely if the number of recorded neurons exceeds 292 the NTC, and the unrecorded neurons are statistically similar to the recorded neurons so as not to change 293 population smoothness estimates. But importantly, even if we obtain the dimensionality of neural state space 294 dynamics correctly by simply recording more neurons than the NTC, our theory so far does not provide any 295 guarantee that we obtain their geometry correctly. Here we address the fundamental question of how many 296 recorded neurons are sufficient to obtain the correct dynamical portrait of circuit computation at a given level 297 of precision? By definition, the correct dynamical portrait is what we would obtain from dimensionality 298 reduction applied to recordings of all the neurons in the behaviorally relevant brain region in question. 299 Importantly, how does the sufficient number of recorded neurons scale with the complexity of the task, the 300 desired precision, the total number of neurons in the brain region, and other properties of neural dynamics? 301 And, interestingly, what minimal aspects of neural dynamics are important to know in order to compute this 302 number? 

303 To introduce our theory, it is useful to ask, when, intuitively, would recordings from a subset of neurons 304 yield the same dynamical portrait as recordings from all the neurons in a circuit? The simplest visualizable 305 example is a circuit of 3 neurons, where we can only measure 2 of them (Fig. 5A). Suppose the set of neural 306 activity patterns encountered throughout the experiment consists of a single neural trajectory, that does not 307 curve too much, and is somewhat randomly oriented relative to the single neuron axes (or equivalently, neural 308 activity patterns at all times are distributed across neurons). Then the act of subsampling 2 neurons out of 3 309 is like looking at the shadow, or projection of this neural trajectory onto a coordinate subspace. Intuitively, 310 it is clear that the geometry of the shadow will be similar to the geometry of the neural trajectory in the full 311 circuit, no matter which 2 neurons are recorded. On the other hand, if the manifold is not randomly oriented 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

312 with respect to single neuron axes, so that neural activity patterns may be sparse (Fig. 5B), then the shadow 313 of the full neural trajectory onto the subspace of recorded neurons will not preserve its geometry across all 314 subsets of recorded neurons. The challenge of course, is to make these intuitive arguments quantitatively 315 precise enough to guide experimental design. 

- 316 To develop our theory of neural measurement, lets first assume the optimistic scenario in Fig. 5A, and 317 pursue and test its consequences. If, in general, the neural data manifold (i.e. Fig. 3F) is randomly oriented 318 w.r.t. the single neuron axes, then a measurement we can currently do, namely record from _M_ randomly 319 chosen neurons (Fig. 5C, top), becomes equivalent to a measurement we do not yet do, namely record from 320 _M_ random linear combinations of all neurons in the circuit (Fig. 5C, bottom). The former corresponds to 321 projecting the neural manifold onto a coordinate subspace as in Fig. 5A, while the latter corresponds to 322 projecting it onto a randomly oriented _M_ dimensional subspace. If the neural manifold is randomly oriented 323 to begin with, the nature of the geometric distortion incurred by the shadow, relative to the full manifold, is 324 the same in either case. 

- 324 

- 325 This perspective allows us to then invoke a well-developed theory of how smooth manifolds in a high 326 dimensional ambient space become geometrically distorted under a random projection (RP) down to a lower 327 dimensional subspace [Baraniuk and Wakin, 2007, Clarkson, 2008]. The measure of geometric distortion _ϵ_ 328 is the worst case fractional error in euclidean distances between all pairs of points on the manifold, measured 329 in the subspace, relative to the full ambient space (see Methods). The theory states that, to achieve a desired 

- 330 fixed level of distortion, _ϵ_ , with high probability ( _>_ 0 _._ 95 in our analyses below) over the choice of random 331 projection, the number of projections _M_ should exceed a function of the distortion _ϵ_ , the manifold’s intrinsic 332 dimension _K_ (1 for trajectories, 2 for surfaces, etc..), volume _V_ , and curvature _C_ , and the number of 333 ambient dimensions _N_ . In particular the theory states that _M ≥ ϵ[K]_[2][(] _[c]_[1][ log] _[ CV]_[+] _[ c]_[2][ log] _[ N]_[+] _[ c]_[3][)][, where] _[ c]_[1][,] 334 _c_ 2, and _c_ 3 are fixed constants, is sufficient. Thus intuitively, manifolds with low intrinsic dimensionality 335 that do not curve much and have limited volume do not require that many measurements to preserve their 336 geometry. Intriguingly, the number of ambient dimensions has a very weak effect; the number of required 337 measurements grows only logarithmically with it. This is exceedingly fortunate, since in a neuroscience 338 context, the number of ambient dimensions _N_ is the total number of neurons in the relevant brain region, 339 which could be very large. The logarithm thus ensures that this large number alone does not impose a 340 requirement to make a prohibitively large number of measurements. Translating the rest of this formula to 341 a neuroscience context, _K_ is simply the number of task parameters, and _CV_ , or curvature times volume, is 342 qualitatively related to the NTC in (1); the numerator is the volume of the manifold in task space, and the 343 reciprocal of correlation length is like curvature (short correlation length implies high curvature). Making 344 this qualitative translation, the theory of neural measurement as a random projection suggests that as long as 345 the number of recorded neurons obeys 

**==> picture [296 x 22] intentionally omitted <==**

346 then we can obtain dynamical portraits with fractional error _ϵ_ , with high probability over the choice of a 347 random subset of recorded neurons. Remarkably, this predicts the number of recorded neurons need only 348 scale logarithmically with the NTC to maintain a fixed precision. 349 Thus this theory makes a striking prediction that we can test in neural data: for a fixed number of task 350 parameters _K_ , and a fixed number of total neurons _N_ , if we vary the number of recorded neurons _M_ and the 351 NTC, and compute the worst case fractional error _ϵ_ in the recovered dynamical portraits relative to what we 352 would get if we recorded all _N_ neurons, then the iso-contours of constant distortion will be straight lines in 

353 a plane formed by _M_ and the _logarithm_ of the NTC. Of course we cannot currently record all _N_ neurons in 

- 354 motor cortex, so we simply treat the dynamical portraits obtained in each monkey from all recorded neurons 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

**==> picture [430 x 291] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Distributed Activity B Sparse Activity C Recording as RP<br>random sampling<br>slightly slightly<br>distorted distorted<br>random projection<br>H RP and RS Comparison<br>slightly highly 0.1 0.3 0.01 ε = 0.2 ε = 0.3 ε = 0.4<br>distorted distorted 0.2<br>0.05 0.1<br>neuron 1 neuron 1 0.2 0.4 60<br>D Distorted Portrait F Distortion under RP G Distortion under RS<br>Example ε = 0.2 ε = 0.3 ε = 0.4<br>Monkey H ε ≥0.5 Monkey H ε ≥0.5 20 Monkey H<br>R [2]  = 0.93, 0.95, 0.96 R [2]  = 0.95, 0.96, 0.98<br>60 60 20 60<br>full random projection M<br>ε=0.2 0.3 0.3<br>ε=0.3<br>ε=0.4 20 20<br>30<br>PC1 (A.U.) ≤0.1 ≤0.1<br>10 100 600 10 100 600<br>E Variations of PCs<br>Monkey G ε Monkey G ε<br>ε ≥0.5 ≥0.5 10 Monkey G<br>R [2]  = 0.91, 0.93, 0.96 R [2]  = 0.92, 0.83, 0.93<br>0.4<br>30 30 10 30<br>0.3 0.3 random projection M<br>0.3<br>10 10<br>0.2<br>≤0.1 ≤0.1<br>-200 0 400 10 100 600 10 100 600<br>since movement onset (ms) time (msec, log scale) time (msec, log scale)<br>neuron 3 neuron 3<br>neuron 2 neuron 2<br>random sampling M<br>PC2 (A.U.) M M<br>random sampling M<br>PC1 (A.U.)<br>M M<br>PC2 (A.U.)<br>**----- End of picture text -----**<br>


Figure 5: **Conditions for accurate recovery of the geometry of dynamical portraits** . **A** . A simple example of a _K_ = 1 dimensional neural trajectory in _N_ = 3 ambient dimensions, that is not aligned with respect to single neuron axes, so that neural patterns at all times are distributed across neurons. Recording any subset of _M_ = 2 neurons induces only small geometric distortions in the neural trajectory relative to recording all _N_ = 3 neurons. **B** . A simple example of a neural trajectory that is largely aligned with respect to the axis of neuron 2. Measuring any subset of neurons that does not include neuron 2 incurs a large distortion in the trajectory. **C** . For neural manifolds that are randomly oriented with respect to the single neuron axes, recording a random sample (RS) of _M_ neurons (top) yields similar dynamical portraits as those obtained from recording a set of _M_ random linear combinations, or random projection (RP), of all _N_ neurons in the circuit. **D** . Example neural trajectories from two reach angles under different levels of distortion. The trajectories are projected into the top 2 PCSs, and only rotated for optimal alignment against fully observed trajectories. **E** . Variations (95% interval) of recovered PCs under different levels of distortion. **F** . For each monkey, the 95th percentile of the distortion distribution obtained after measuring _M_ random linear combinations of all _N_ recorded neurons ( _N_ = 109 for monkey H and _N_ = 42 for monkey G), for random neural trajectory intervals of varying duration _T_ . For each _M_ and _T_ we conducted 200 random trials and in 95% of trials the distortion _ϵ_ between the resulting dynamical portrait and that obtained from all _N_ recorded neurons for the same neural trajectory was less than the reported distortion. The iso-contrours of constant distortion are indeed straight lines in the _M_ -log _T_ plane, as predicted by Eq. (3). For the iso-contours _ϵ_ = 0 _._ 2 _,_ 0 _._ 3, and 0 _._ 4, linear regression of _M_ against log _T_ yields excellent fits ( _R_[2] ’s of 0.93, 0.95 and 0.96 respectively for monkey H; 0.91, 0.93 and 0.96 for monkey G). **G** . Exactly the same analysis as **F** except now the measurement process corresponds to random samples of _M_ neurons as opposed to _M_ random projections of all _N_ neurons. **H** . A quantitative comparison of panels _F_ and _G_ through a scatter plot of the number of randomly sampled neurons versus random projections required to obtain the same distortion on neural trajectories of varying duration. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

355 as the ground truth: i.e. we take _N_ = 109 in monkey H and _N_ = 42 in monkey G, as the total number 356 of neurons, and we subsample a smaller number of neurons _M_ from this pool. Also, we focus on the case 357 _K_ = 1, as the neural manifold in Fig. 3F is sampled smoothly only in time, and not angle; the reaches 358 were done at only 8 discrete angles. Therefore we vary the NTC exactly as in Fig. 4C, by choosing random 359 intervals of neural trajectories of varying durations _T_ at each angle. For each interval duration _T_ , which 360 in this restricted context we can think of as simply proportional to the NTC, we use data from a random 361 subset of _M_ neurons, and compute the distortion _ϵ_ ( _M, T_ ) in the resulting dynamical portraits relative to the 362 assumed ground-truth portrait obtained from all _N_ recorded neurons. The theory above in Eq. (3) predicts 363 exactly the same scaling in this scenario, with NTC replaced by time _T_ . 

- 364 Examples of the effects of different distortions _ϵ_ , obtained by by sampling different sets of _M_ neurons, 365 are shown in Fig. 5D for dynamic portraits and Fig. 5E for individual PC’s. More generally, for each _M_ and 366 _T_ , we conducted 200 trials and we plotted the 95’th percentile of resultant distribution of distortion _ϵ_ as a 367 heat map in Fig. 5FG. (i.e. 95% of trials had distortion less than what is reported). In panel F, we measured 368 _M_ random projections, or _M_ random linear combinations of all _N_ recorded neurons, for varying intervals of 369 duration _T_ , as the subsampled dataset, corresponding to the hypothetical experiment in Fig. 5C, bottom. It is 370 clear that the iso-contours of constant distortion _ϵ_ are well fit by straight lines in a plane formed by _M_ and the 371 logarithm of time _T_ . This is a completely expected result, as this analysis is simply a numerical verification 372 of an already proven theory. However, it forms a quantitative baseline for comparison in panel _G_ , where we 373 repeat the same analysis in panel _F_ , except we record random subsamples of _M_ neurons, as in experiment 374 5C, top. We obtain a qualitatively similar result as in panel _F_ , which is remarkable, since this analysis is 375 no longer a simple numerical verification of a mathematical theory. Rather, it is a stringent test of the very 376 assumption that the neural manifold in Fig. 3F is randomly oriented enough with respect to single neuron 377 axes so that random projections form a good theoretical model for the traditional measurement process of 378 randomly sampling a subset of neurons. In essence it is a test of the assumption that the neural manifold is 379 more like Fig. 5A than Fig. 5B, so that the two experiments in Fig. 5C yield similar geometric distortions 380 in dynamical portraits as a function of recorded neurons _M_ and neural task complexity NTC. In particular, 381 the striking scaling of recorded neurons _M_ with the logarithm of the NTC to maintain fixed precision in 382 recovered dynamical portraits, predicted by the random projection theory of neural measurement, is verified. 383 Moreover, we quantitatively compare the discrepancy between the two measurement scenarios in Fig. 5H, 384 by creating a scatter plot of how many randomly sampled neurons versus random projections it takes to 385 get the same distortion _ϵ_ across all possible neural trajectory durations _T_ , or equivalently, NTC’s. Even 386 at a quantitative level, the data points are close to the unity line, relative to the total number of recorded 387 neurons, suggesting that for this dataset, random projection theory is an impressively good model for the 388 neural measurement process. 389 In the Supplementary Material, we study how these results are modified as neural activity patterns be390 come more sparse and aligned with single neuron axes (i.e. less extreme versions of Fig. 5B). Remarkably, 391 the linear scaling of number of neurons with the logarithm of NTC at fixed error is preserved, albeit with 392 a higher slope and intercept. By comparing the neural data to simulated data with different levels of spar393 sity, we find that the neural data is indeed close to randomly aligned with respect to single neuron axes, as 394 suggested by the closeness of the points in 5H to the unity line. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 395 **6 Discussion** 

## 396 **6.1 An intuitive summary of our theory** 

397 Overall, we have generated a quantitative theory of trial averaged neural dimensionality, dynamics, and 398 measurement that can impact both the interpretation of past experiments, and the design of future ones. Our 399 theory provides both quantitative and conceptual insights into the underlying nature of two major order of 400 magnitude discrepancies dominating almost all experiments in systems neuroscience: (1) the dimensionality 401 of neural state space dynamics is often orders of magnitude smaller than the number of recorded neurons 402 (e.g. Fig. 2), and (2) the number of recorded neurons is orders of magnitude smaller than the total num403 ber of relevant neurons in a circuit, yet we nevertheless claim to make scientific conclusions from such 404 infinitesimally small numbers of recorded neurons. This latter discrepancy is indeed troubling, as it calls 405 into question whether or not systems neuroscience has been a success or a failure, even within the relatively 406 circumscribed goal of correctly recovering trial-averaged neural state space dynamics in such an undersam407 pled measurement regime. To address this fundamental ambiguity, our theory identifies and weaves together 408 diverse aspects of experimental design and neural dynamics, including the number of recorded neurons, the 409 total number of neurons in a relevant circuit, the number of task parameters, the volume of the manifold of 410 task parameters, and the smoothness of neural dynamics, into quantitative scaling laws determining bounds 411 on the dimensionality and accuracy of neural state space dynamics recovered from large scale recordings. 412 In particular, we address both order of magnitude discrepancies by taking a geometric viewpoint in 413 which trial-averaged neural data is fundamentally an embedding of a task manifold into neural firing rate 414 space (Fig 3EF), yielding a neural state space dynamical portrait of circuit computation during the task. We 415 explain the first order of magnitude discrepancy by carefully considering how the complexity of the task, 416 as measured by the volume of the task manifold, and the smoothness of neural dynamics, as measured by 417 a product of neural population correlation lengths across each task parameter, can conspire to constrain the 418 maximal number of linear dimensions the neural state space dynamics can possibly explore. We define a 419 mathematical measure, which we call neural task complexity (NTC), which, up to a constant, is simply the 420 ratio of the volume of the task manifold and the product of neural population correlation lengths (Eq. (1)) 421 and we prove (see Supplementary material) that this measure forms an upper bound on the dimensionality 422 of neural state space dynamics (Eq. (2)). We further show in neural data from the motor cortex of reaching 423 monkeys, that the NTC is much smaller than the number of recorded neurons, while the dimensionality 424 is only slightly smaller than the NTC (Fig. 4). Thus the simplicity of the center out reach task and the 425 smoothness of motor cortical activity, are by themselves sufficient to explain the low dimensionality of the 426 dynamics relative to the number of recorded neurons. A natural hypothesis is that for a wide variety of tasks, 427 neural dimensionality is much smaller than the number of recorded neurons because the task is simple and 428 the neural population dynamics is smooth, leading to a small NTC. In such scenarios (experimental regime 429 (ii) in Fig. 4A), only by moving to more complex tasks, not by recording more neurons, would we obtain 430 richer higher dimensional trial averaged state space dynamics. 

431 We address the second, more troubling, order of magnitude discrepancy by making a novel conceptual 432 link between the time-honored electrophysiology tradition of recording infinitesimally small subsets of neu433 rons in much larger circuits, and the theory of random projections, corresponding in this context to recording 434 small numbers of random linear combinations of _all_ neurons in the circuit. In scenarios where the neural 435 state space dynamics is sufficiently randomly oriented with respect to single neuron axes (e.g. Fig. 5A) these 436 two different measurement scenarios (Fig. 5C) yield similar predictions for the accuracy with which the dy437 namics are recovered as a function of the number of recorded neurons, the total number of neurons in the 438 circuit, the volume of the task manifold, and the smoothness of the neural dynamics. A major consequence 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 439 of the random projection theory of neural measurement is that the worst case fractional error in the geometry 440 of recovered neural state space dynamics increases only with the _logarithm_ of the total number of neurons in 441 the circuit (Eq. (3)). This remarkable property of random projections goes hand in hand with why systems 442 neuroscience need not be daunted by so many unrecorded neurons: we are protected from their potentially 443 detrimental effect on the error of state space dynamics recovery by a strongly compressive logarithm. More444 over, the error grows linearly with the number of task parameters, and only again _logarithmically_ with the 445 NTC, while it decreases linearly in the number of recorded neurons (Eq. (3)). Thus recording a modest 446 number of neurons can protect us against errors due to the complexity of the task, and lack of smoothness in 447 neural dynamics. 

- 448 This theory then resolves the ambiguity of whether systems neuroscience has achieved success or has 449 failed in correctly recovering neural state space dynamics. Indeed it may well be the case that in a wide 450 variety of experiments, we have indeed been successful, as we have been doing simple tasks with a small 451 number of task parameters and NTC, and recorded in circuits with distributed patterns of activity, making 452 random projections relevant as a model of the measurement process. Under these conditions, we have 453 shown there is a modest requirement on the number of recorded neurons to achieve success. Our work 454 thereby places many previous works on dimensionality reduction in neuroscience on much firmer theoretical 455 foundations. Having summarized our theory, below we discuss its implications and its relations to other 456 aspects of neuroscience. 

## 457 **6.2 Dimensionality is to neural task complexity as information is to entropy** 

- 458 To better understand the NTC, and its relation to dimensionality, it is useful to consider an analogy between 459 our results and applications of information theory in neuroscience [Reike et al., 1996]. Indeed, mutual in460 formation has often been used to characterize the fidelity with which sensory circuits represent the external 461 world. However, suppose that one reported that the mutual information rate _I_ ( _S, R_ ) between the sensory 462 signal _S_ and the neural response _R_ were 90 bits per second, as it is in the fly H1 neuron [Strong et al., 1998]. 463 This number by itself would be difficult to interpret. However, just as dimensionality is upper bounded by the 464 neural task complexity, mutual information _I_ is upper bounded by entropy _H_ , i.e. _I_ ( _S, R_ ) _≤ H_ ( _R_ ). Thus 465 if one measured the entropy rate of the response spike train to be 180 bits per second [Strong et al., 1998], 466 then by comparing the mutual information to the entropy one could make a remarkable conclusion, namely 467 that the neural code is highly efficient: the fidelity with which the response _R_ codes for the stimulus _S_ is 468 within a factor of 2 of the fundamental limit set by the entropy of the neural response _R_ . 

- 469 Similarly, the observation that the dimensionality of recordings of 109 neurons in Monkey H in Fig. 4 470 is 7.1, is by itself, difficult to interpret. However, if one computed the NTC to be 10.5, then by comparing 471 dimensionality to the NTC, one could make another remarkable conclusion, namely that motor cortex is 472 exploring almost as many dimensions as possible given the limited extent, or volume of behavioral states 473 allowed by the task, and the limited speeds with which neural population dynamics can co-vary across 474 behavioral states. Thus just as entropy, as an upper bound on mutual information, allows us to measure 475 the fidelity of the neural code on an absolute scale from 0 to 1 through the ratio of information to entropy, 476 the NTC, as an upper bound on dimensionality, allows us to measure the complexity of neural state space 477 dynamics on an absolute scale from 0 to 1, through the ratio of dimensionality to NTC. When this ratio is 1, 478 neural dynamics is as complex, or high dimensional, as possible, given task and smoothness constraints. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 479 **6.3 Towards a predictive theory of experimental design** 

- 480 It may seem that neural task complexity could not be useful for guiding the design of future experiments, 481 as its very computation requires knowing the smoothness of neural data, which would not have yet been 482 collected. However, this smoothness can be easily estimated based on knowledge of previous experiments. 483 As an illustration, consider how one might obtain an estimate of how many neurons one would need to 484 record in order to accurately recover neural state space dynamics during a more complex reaching task in 485 3 dimensions. For concreteness, suppose a monkey has to reach to all points on a sphere of fixed radius 486 centered at the shoulder of the reaching arm. The manifold of trial averaged task parameters is specified 487 by time _t_ into the reach, which varies from 0 to _T_ ms, and the azimuthal and altitudinal angles _φ_ and _θ_ , 488 each of which range from 0 to 2 _π_ . Now lets assume the smoothness of neural population dynamics across 489 time will be close to the average of what we observed for 2 dimensional reaches ( _τ_ = 126 and 146 ms 490 in monkeys H and G). Also lets assume reaches will take on average _T_ = 600 ms as it did in the case of 491 two dimensional reaches. Then the we obtain the estimate _[T]_[600][4] _[.]_[41][.][Now again,][lets assume that] _τ_[=] 136[=] 

- 492 both azimuthal (∆ _φ_ ) and altitudinal (∆ _θ_ ) neural correlation lengths would be the average of the angular 493 correlation length of two dimensional reaches (∆= 1 _._ 82 and 1 _._ 91 radians in monkeys H and G), yielding 494 ∆2 _πφ_[=] ∆2 _πθ_[=] 1 _._ 2865 _π_[=][3] _[.]_[37][.][Then][the][NTC,][according][to][Eq.][(1),][is][proportional][to][the][product][of][these] 495 3 numbers, where in 3 dimensions, the constant of proportionality could be taken to be _C_ = � _π_ 2 �3 _/_ 2. This 2 3 _/_ 2 

- 496 product yields an estimate of NTC = � _π_ � _×_ 4 _._ 41 _×_ 3 _._ 37 _×_ 3 _._ 37 = 25 _._ 4. 497 If we trust this estimate, then this simple computation, coupled with our theorems proven above, allows 498 us to make some predictions that can guide experimental design. For example, the theorem in Eq. (1) implies 499 that no matter how many neurons we record in monkey motor and premotor cortices, the dimensionality of 500 the trial averaged state space dynamics will not exceed 25. Moreover, the theorem in Eq. (3) tells us that 501 if we wish to recover this state space dynamics to within fractional error _ϵ_ = 0 _._ 2, relative to what we 502 would obtain if we recorded all task relevant neurons, then we should record at least _M_ = 300 neurons (see 503 Supplementary Material). Now of course, we may not wish to trust this estimate, because we may have mis504 estimated the neural correlation lengths. To be safer, we could easily underestimate the correlation lengths, 505 and thereby obtain a safe overestimate of the NTC and requisite number of neurons to record. But overall, in 506 this fashion, by combining an estimate of a likely NTC in future experiments with the new theorems in this 507 work, we can obtain back of the envelope estimates of the dimensionality and accuracy of recovered state 508 space dynamics, as neuroscience moves forward to unravel the neural basis for more complex behavioral 509 and cognitive acts. 

## 510 **6.4 Departures from our assumption of statistical homogeneity** 

- 511 A critical assumption in using our theory to guide future experiments is that the set of unrecorded neurons 512 is statistically similar to the set of recorded neurons, so that the denominator of the NTC in Eq. (1) will 513 not change much as we fix the task and record more neurons. There are several important ways that this 514 assumption could be violated. For example, there could be strong spatial topography in the neural code of 515 the relevant circuit, so that as we expand our electrode array to record more neurons, the new neurons might 516 have fundamentally different coding properties. Also, we may wish to record from multiple task relevant 517 brain regions simultaneously, in which case our theory would have to apply to each brain region individually. 518 Moreover, there may be multiple cell types in the relevant brain region. Unfortunately, most electrophysiol519 ogy recordings do not give us access to cell type information (though spike width can sometimes serve as a 520 proxy for the excitatory/inhibitory distinction). Thus the recovered neural state space dynamics reflects the 521 combined action of all cell types. However, if we had access to cell type information, me may wish to define 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

522 state space dynamical variables for each cell type. Then the theory would apply to each cell type alone. 523 However, if cells of different types are strongly coupled, it is not clear that the collective dynamics of the cir524 cuit should be well explained by reduced degrees of freedom, or state, that are in one-to-one correspondence 525 with cell types. This is an important empirical issue for further studies. 

- 526 In essence, our theory applies to a spatially well mixed, statistically homogenous, localized brain region 527 whose dynamics is relevant to the task. Fortunately, a wide variety of phylogenetically newer brain regions 528 that evolved to learn new connectivities to solve tasks that evolution itself could not anticipate, for example 529 prefrontal, parietal, pre-motor and motor cortices, and even older hippocampal circuits, exhibit precisely 530 these kinds of mixed representations, in which the coding properties of individual neurons exhibit no dis531 cernible spatial topography, and almost every neuron codes for a mixture of multiple task parameters (e.g. 532 [Machens et al., 2010, Mante et al., 2013, Rigotti et al., 2013, Raposo et al., 2014]). These are precisely the 533 properties that make the neural manifold randomly oriented with respect to single neuron axes, and there534 fore make our random projection theory of neural measurement relevant, and the recovery of state space 535 dynamics relatively easy despite subsampling. 

- 536 But ironically, these very same properties make the goal of understanding what each and every individual 537 neuron in the circuit does a seemingly difficult and questionable endeavor. While this endeavor has indeed 538 traditionally been the putative gold standard of understanding, perhaps instilled in systems neuroscience by 539 the tremendous success of Hubel and Wiesel in discovering single cell orientation tuning in primary visual 540 cortex [Hubel and Wiesel, 1959], it is unclear that it will continue to be a profitable path going forward, 541 especially in recently evolved brain regions where mixed representations dominate. But fortunately, the 542 path of moving away from understanding single neurons to recovering collective state space dynamics, is 543 a promising route forward, and indeed one that has firmer theoretical justification now, even in the face of 544 extreme neural subsampling. 

## 545 **6.5 A why question: the neuroscientist and the single neuron** 

- 546 We have shown that when neural representations are distributed, or randomly enough oriented with respect to 547 single neuron axes (Fig. 5A), so that random projections constitute a good model of the neural measurement 548 process (Fig. 5C), then the life of the neuroscientist studying neural circuits becomes much easier: he or she 549 can dramatically subsample neurons, yet still recover global neural state space dynamics with reasonable 550 accuracy. However, neural systems evolved on earth long before neuroscientists arrived to study them. Thus 551 no direct selection pressures could have possibly driven neural systems to self-organize in ways amenable 552 to easy understanding by neuroscientists. So one could then ask a teleological question: why did neural 553 systems organize themselves this way? 

- 554 One possible answer lies in an analogy between the neuroscientist and the single neuron, whose goals 555 may be inadvertently aligned. Just as a neuroscientist needs to read the state of a cortical neural circuit by 556 sampling _O_ (100) randomly chosen neurons, a downstream cortical neuron needs to compute a function of 557 the state of the upstream circuit while listening to _O_ (10 _,_ 000) neurons. Intuitively, if neural activity patterns 558 are low dimensional enough, and distributed enough across neurons, then the single neuron will be able 559 to do this. Indeed, a few works have studied constraints on neural representations in the face of limited 560 network connectivity. For example, [Valiant, 2005] showed that the sparser neural connectivity is, the more 561 distributed neural representations need to be, in order for neural systems to form arbitrary associations 562 between concepts. Also [Sussillo and Abbott, 2012] showed that if neural representations in a circuit are 563 low dimensional and randomly oriented with respect to single neuron axes, then a neuron that subsamples 564 that circuit can compute any function of the circuit’s state that is computable by a neuron that can listen 565 to all neurons in the circuit. And finally, [Kim et al., 2012] showed that the hippocampal system appears 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

566 to perform a random projection, transforming a sparse CA1 representation of space into a dense subicular 567 representation of space, yielding the ability to communicate the output of hippocampal computations to the 568 rest of the brain using very few efferent axons. 

569 These considerations point to an answer to our teleological question: in essence, our success as neuro570 scientists, in the accurate recovery of neural state space dynamics under extreme subsampling, may be an 571 exceedingly fortunate corollary of evolutionary pressures for single neurons to communicate and compute 572 accurately under the constraints of limited degree network connectivity. 

## 573 **6.6 Beyond the trial average: towards a theory of single trials** 

- 574 A natural question is how this theory would extend to the situation of single trial analyses. Several new 575 phenomena can arise in this situation. First, in any single trial, there will be trial to trial variability, so that 576 neural activity patterns may lie near, but not on, the trial averaged neural manifold, illustrated for example 577 in Fig. 3F. The strength of this trial to trial variability can be characterized by a single neuron SNR, and it 578 can impact the performance of various single trial analyses. Second, on each and every trial, there may be 579 fluctuations in internal states of the brain, reflecting potentially cognitive variables like attention, or other 580 cognitive phenomena, that are uncontrolled by the task. Such fluctuations would average out in the trial 581 averaged manifold, but across individual trials would manifest as structured variability around the manifold. 582 It would be essential to theoretically understand methods to extract these latent cognitive variables from the 583 statistics of structured variability. Third, the trial averaged neural manifold may have such a large volume, 584 especially in a complex task, so that in a finite number of trials _P_ we may not be able to sufficiently cover this 585 volume. One would like to know then, what is the minimum number of training trials _P_ one would require, 586 to successfully decode behavioral or cognitive variables on subsequent, held-out, single trials. Moreover, 587 how would this minimum number of trials scale with properties of the trial averaged manifold, obtained 588 only in the limit of very large numbers of trials? 

- 589 We have already begun to undertake a study of these and other questions. Our preliminary results, some 590 of which were stated in [Gao and Ganguli, 2015], suggest that the basic theory of trial averaged neural data 591 analysis forms an essential springboard for addressing theories of single-trial data analysis. For example, in 592 the case of the last question above, we find that the number of training trials _P_ must scale with the NTC of 593 the trial averaged neural manifold, in order for subsequent single trial decoding to be successful. Moreover, 594 we have analyzed theoretically the recovery of internal states reflected in the spontaneous activity of large 595 model neural circuits, while subsampling only _M_ neurons for a finite amount of time _[T] τ_[(a][dimensionless] 596 ratio of recording time to single neuron correlation time _τ_ ). We find that the dynamics of these internal 597 states can be accurately recovered as long as (a) both _M_ and _[T] τ_[exceed the intrinsic dimensionality explored] 598 by the manifold of latent circuit states, and (b) the square-root of the product of neurons _M_ and _[T] τ_[exceeds] 599 a threshold set by both this dimensionality and the single neuron SNR [Gao and Ganguli, 2015]. In turn 600 the dimensionality of the manifold of latent circuit states is upper bounded by its NTC, so the NTC of a 601 latent neural manifold determines the viability of single trial analyses, just as it does in the recovery of 602 neural manifolds explicitly associated with externally measured task parameters. And finally, one may be 603 tempted to conjecture that, due to finite SNR, single trial decoding performance may grow without bound 604 as the number of recorded neurons increase - a result that is qualitatively different from the trial averaged 605 theory, which suggests that only modest only numbers of neurons are required to accurately recover neural 606 state space dynamics. However, there are several reasons to believe that such a qualitative discrepancy may 607 not bear out. For example, neural noise may be embedded in the same direction as the signal, resulting in 608 information limiting correlations [Moreno-Bote et al., 2014]. Moreover, empirically, in single trial decoding 609 in the brain machine interface community, decoding performance already achieves a point of diminishing 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

610 returns at even modest numbers of recorded neurons. The precise theoretical reasons for this remain an 611 object of future study. 

- 612 But overall, our initial results in a theory of single-trial analyses, to be presented elsewhere, suggest 613 that the theory of trial-averaged neural dimensionality, dynamics and measurement, presented here, not only 614 provides interpretive power for past experiments, and guides the design of future trial averaged experiments, 615 but also provides a fundamental theoretical building block for expansion of the theory to single trial anal616 yses. In essence, this work provides the beginnings of a theoretical framework for thinking about how and 617 when statistical analyses applied to a subset of recorded neurons correctly reflect the dynamics of a much 618 larger, unobserved neural circuit, an absolutely fundamental question in modern systems neuroscience. A 619 proper, rigorous theoretical understanding of this question will be essential as neuroscience moves forward 620 to elucidate the neural circuit basis for even more complex behavioral and cognitive acts, using even larger 621 scale neural recordings. 

## 622 

## **7 Materials and Methods** 

623 

## **7.1 Dimensionality Measure** 

624 Our measure of dimensionality is derived from the eigen-spectrum of the neuronal covariance matrix. This 625 matrix underlies PCA, and indicates how pairs of neurons covary across time and task parameters (see 626 Supplementary material). The eigenvalues of this matrix, _µ_ 1 _≥ µ_ 2 _≥, . . . , ≥ µM_ , reflect neural population 627 variance in each eigen-direction in firing rate space. The participation ratio (PR), 

**==> picture [249 x 28] intentionally omitted <==**

628 is a natural continuous measure of dimensionality. Intuitively, if all variance is concentrated in one dimen629 sion, so that _µα_ = 0 for _α ≥_ 2, then PR=1. Alternatively, if the variance is evenly spread across all _M_ 630 dimensions, so that _µ_ 1 = _µ_ 2 = _. . . µM_ , then PR= _M_ . For other PCA eigenspectra, the PR sensibly interpo631 lates between these two regimes, and for a wide variety of uneven spectra, the PR corresponds to the number 632 of dimensions required to explain about 80% of the total population variance (see Supplementary material). 

## 633 **7.2 Preprocessing of the Motor Cortical Dataset** 

634 We use multi-electrode array recordings from two monkeys’ (H and G) PMd and M1 areas as they performed 635 an eight-direction center-out delayed reach task [Yu et al., 2007]. There are between 145 and 148 trials in 636 monkey H’s dataset and between 219 and 222 trials in monkey G’s dataset for each of the eight reach direc637 tions. Neural activities from each trial are time aligned to hand movement onset (time of 15% maximal hand 638 velocity), and restricted to the -250ms to 350ms range time window around movement onset. Each spike 639 train is smoothed with a 20ms gaussian kernel, and averaged with trials of the same reach angle to obtain the 640 averaged population firing rates for the eight conditions. To homogenize the activity levels between neurons 641 of different firing rates, and to highlight variability in the data resulting from task conditions, we further 642 applied the square-root transform to population firing rates [Thacker and Bromiley, 2001], and subtracted 643 their cross-condition average [Churchland et al., 2012]. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 644 **7.3 Distortion Measure** 

645 To quantify the geometric distortion of dynamic portraits incurred from projecting them down from the _N_ 646 dimensional space of all neurons to the _M_ dimensional subspace of recorded neurons (or _M_ dimensional 647 random subspace for a random projection), we adopt the pairwise distance distortion measure widely em648 ployed in the theory of random projections. Let **P** be the _M_ -by- _N_ linear projection operator that maps 649 points from the full _N_ -dimensional neural space into the _M_ -dimensional subspace. For any pair of neural 650 activity patterns **x** _[i]_ and **x** _[j]_ in the full _N_ -dimensional space, the pairwise distance distortion induced by **P** is 

650 651 

651 

**==> picture [288 x 27] intentionally omitted <==**

652 where the � _N/M_ ratio compensates for the global distortion introduced simply by the reduction in dimen653 sionality, and _||_ **v** _||_ denotes the Euclidean length of a vector **v** . A distortion of 0 indicates that the pairwise 654 distance is the same both before and after the projection (up to an overall scale). The worst case distortion 655 over all pairs of points ( _i, j_ ) on the neural manifold is given by, 

**==> picture [264 x 16] intentionally omitted <==**

656 Since under either random projection or random sampling, **P** is a random mapping, _d_[max] ( **P** ) is a random 

657 variable. We characterize the distortion by the 95th percentile of the distribution of this random variable, i.e. 658 that _ϵ_ for which 

**==> picture [114 x 10] intentionally omitted <==**

659 Thus with high probability (95%), over the random set of _M_ measurements, the worst case distortion over 660 all pairs of points on the neural manifold, will not exceed _ϵ_ . In Fig. 5, for each value of _M_ and _T_ , we 661 estimated _ϵ_ by computing _d_[max] ( **P** ) 200 times for different random choices of **P** , and set _ϵ_ to be the 95th 662 percentile of this empirical distribution of distortions. 

663 

## **8 Acknowledgements** 

664 We thank S. Lahiri for inputs on dimensionality upper bound proofs. This work was supported by the 665 Stanford Graduate Fellowship (P.G. and E.T.), the Mind, Brain and Computation Trainee Program (NSF 666 IGERT 0801700, P.G. and E.T.), the Ruth L. Kirschstein National Research Service Award Predoctoral 667 Fellowship (E.T.), NIH Director’s Pioneer Award (8DPIHD075623) and the Burroughs Wellcome, Simons, 668 McKnight, and James S. McDonell foundations. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

## 669 **Supplementary Materials:** 670 **A Theory of Multi-Neuronal Dimensionality,** 671 **Dynamics and Measurement** 

|672|**I**|**Introduction**|**21**|
|---|---|---|---|
|673|**II **|**The relation between neuronal and task dimensionality**|**22**|
|674||II.I<br>Review of principal components analysis as a dimensionality reduction method . . . . . . .|22|
|675||II.II Participation ratio as a measure of dimensionality . . . . . . . . . . . . . . . . . . . . . . .|24|
|676||II.III A duality between neuronal dimension and task dimension . . . . . . . . . . . . . . . . . .|24|
|677||II.IV Dimensionality of simple stationary tasks unfolding over time<br>. . . . . . . . . . . . . . . .|25|
|678||II.V Example stationary tasks: relation between participation ratio and fraction of variance ex-||
|679||plained . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|27|
|680|**III **|**Towards Neural Task Complexity: upper bounds on dimensionality through destruction of**||
|681||**structure**|**29**|
|682||III.I Increasing dimensionality by reducing long-range correlation . . . . . . . . . . . . . . . . .|29|
|683||III.II Increasing dimensionality by homogenizing dynamics . . . . . . . . . . . . . . . . . . . . .|30|
|684||III.IIIThe best stationary approximation to a task has higher dimensionality than the original task .|30|
|685||III.IVFor multiple task parameters, a factorized stationary approximation to a task has higher||
|686||dimensionality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|687||III.V Algorithmic computation of neural task complexity . . . . . . . . . . . . . . . . . . . . . .|34|
|688|**IV **|**Examples of the relationship between dimensionality and neural task complexity**|**35**|
|689||IV.I Dimensionality and neural task complexity for discrete stimuli or behavioral conditions . . .|35|
|690||IV.II Random smooth manifolds have dimensionality equal to neural task complexity . . . . . . .|36|
|691||IV.IIIIntrinsic constraints on neural dynamics can prevent dimensionality from approaching the||
|692||NTC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|38|
|693|**V **|**Neural task complexity and random projections as a theory of neural measurement**|**39**|
|694||V.I<br>Review of random projection theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|39|
|695||V.II Numerical analysis of scaling behavior a random projection theory of measurement . . . . .|41|
|696||V.III Scaling of distortion with neural sparsity . . . . . . . . . . . . . . . . . . . . . . . . . . . .|43|



## 697 **I Introduction** 

698 In this supplementary material, we fill in the technical details associated with the main manuscript, and 699 present proofs of the theorems stated there. The outline of the supplementary material is as follows. 700 In Sec. II, after reviewing principal components analysis, we justify the participation ratio as a reason701 able measure of neural dimensionality, and explain its relation to more traditional measures like fraction of 702 variance explained as a function of the number of principal components retained. We also explain rigorously 703 how neural dimensionality is intimately related to task dimensionality through simple properties of linear 704 algebra. Finally we compute the dimensionality of simple stationary tasks. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 705 In Sec. III we introduce the logic behind neural task complexity (NTC) and why it places an upper bound 706 on neural dimensionality. Along the way we prove a series of rigorous theorems in which we successively 707 destroy structure in neural data, and show that the resultant destroyed dataset has higher dimensionality 708 than the original dataset. The final outcome of this destruction of structure yields a simple dataset that is 709 characterized purely by the number and range of task parameters and the local smoothness of the original 710 dataset along each task parameter. The dimensionality of this simple dataset is by definition the NTC, and by 711 construction it forms an upper bound on the dimensionality of the original dataset. Along the way we prove 712 several intermediate results: (1) destroying long range correlations in a dataset increases its dimensionality; 713 (2) making a dataset more homogeneous increases its dimensionality; (3) the best stationary approximation 714 to a dataset has higher dimensionality than the original one; and (4) a particular factorization of a dataset 715 across multiple task parameters has higher dimensionality than the original. Overall, this section proves the 716 central results of Equations (1) and (2) in the main paper. 717 In Sec. IV we provide examples of the relationship between measured dimensionality, number of 718 recorded neurons, and neural task complexity for a diverse set of theoretical models for datasets. We begin 719 with a set of discrete stimuli, which we do not consider in the main paper, but include here for completeness. 720 We then consider the case of random smooth neural manifolds, as an example of a model dataset in which 721 actual dimensionality equals the neural task complexity. For both of these datasets, we show that the mea722 sured dimensionality initially grows with the number of recorded neurons, but then saturates to the value of 723 the actual dimensionality as soon as the number of recorded neurons exceeds the actual dimensionality by 724 a factor of about 10. This is consistent with the theory of random projections discussed later in which the 725 preservation of geometric structure in data (including its dimensionality) to within a fractional error, requires 726 a number of neurons that varies inversely with the error tolerance. Finally, at the end of Sec. IV we provide 727 a theoretical neural network model that generates a dataset that lies deep within the elusive experimental 728 regime (iii) in Figure 4A of the main paper. In this regime, the actual dimensionality is much less than the 729 NTC (as well as the number of measured neurons), indicating that some neural network property is constrain730 ing dimensionality to a smaller value than that predicted by limited recording time and neural smoothness 731 alone. In our example, this property is non-normal amplification which rapidly constraints network activity 732 to a small number of neural activity patterns. 

- 733 In Sec. V we begin with a self-contained review of seminal results in random projection theory. We 734 then explore random projections of smooth manifolds in detail using simulations to quantitatively determine 735 different constants of proportionality relating the number of required projections to the volume, smoothness, 736 and ambient dimension of the manifold. These numerical simulations demonstrate that the constants of 737 proportionality, which were not measured quantitatively in prior work, are not that large and are indeed 738 _O_ (1). Finally, we explore the effects of sparsity on neural activity, confirming that the essential theoretical 739 prediction verified in Fig. 5 in the main paper, namely that the number of recorded neurons _M_ need only 740 scale logarithmically with the NTC in order to achieve a constant level of distortion, holds even when the 741 data is quite sparse. 

## 742 

## **II The relation between neuronal and task dimensionality** 

## 743 **II.I Review of principal components analysis as a dimensionality reduction method** 

744 Trial averaged neural data is often described by an _M_ -by- _NT_ data matrix, **X** . The _M_ rows of **X** correspond 745 to _M_ recorded neurons, while the _NT_ columns of **X** correspond to all experimental task conditions - i.e. the 746 columns could range over all combinations of time points and task parameter values occurring throughout 747 the experiment. Each matrix element **X** _ia_ reflects the firing rate of neuron _i_ in task condition _a_ . For example, 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

748 for a simple task unfolding over time as shown in Fig. 1 of the main paper, each column of **X** represents a 749 pattern of firing rates across _M_ recorded neurons at some specified time, and _NT_ is equal to the total number 750 of sampled time points. 

751 Principal components analysis (PCA), as a method of dimensionality reduction, starts from the _M_ by _M_ 752 neuronal covariance matrix, 

**==> picture [259 x 22] intentionally omitted <==**

753 Here we have assumed that the data matrix **X** is centered, so that the sum of the columns is 0 (i.e.[�] _[N] a_ =1 _[T]_ **[X]** _[ia]_[=] 754 0 _∀ i_ ). Geometrically, this means the cloud of _NT_ neural activity patterns in _M_ dimensional firing rate space, 755 where each point in the cloud corresponds to a column of **X** , has its center of mass at the origin. Each matrix 756 element **C**[Neuron] _ij_ then reflects how strongly the firing rates of neurons _i_ and _j_ co-vary across task parameters. 757 PCA relies on the eigen-decomposition of **C**[Neuron] , given by 

757 

**==> picture [268 x 30] intentionally omitted <==**

758 where **u** _[α]_ ’s are the eigenvectors of **C**[Neuron] and the _µα_ ’s denote the associated ordered eigenvalues, so that 759 _µ_[1] _≥ µ_[2] _≥, . . . , ≥ µ[M]_ . Each eigenvector **u** _[α]_ can be thought of as a static, spatial basis pattern of firing rates 760 across neurons (i.e. the red and blue patterns in Fig. 1C of the main paper). Each eigenvalue _µα_ reflects the 761 amount of neural population variance along firing rate direction **u** _[α]_ . Also, if we project neural activity onto 762 pattern **u** _[α]_ , we obtain the amount of pattern _α_ in the neural population in task condition _a_ : 

**==> picture [251 x 30] intentionally omitted <==**

763 The variance of _c[α] a_[across][task][conditions] _[a]_[is][precisely][(up][to][a][normalization][by] _[N][T]_[)][the][variance][of] 764 the neural population in the direction **u** _[α]_ , i.e. the eigenvalue _µα_ . In the special case, where _a_ simply 765 indexes time, we can think _c[α] a_[as one component of a dynamical trajectory in pattern space (i.e.][the temporal] 766 components in Fig. 1C of the main paper). A low, _D_ dimensional dynamic portrait of the trial-averaged 767 data can then be obtained by plotting the top _c[α] a_[against][each][other,][for] _[α]_[=][1] _[, . . . , D]_[(i.e.][Fig.][1D][of] 768 the main paper). The fraction of variance explained by the top _D_ dimensions is _r_ = _µ_ 1Tot � _Dα_ =1 _[µ][α]_[, where] 769 _µ_ Tot =[�] _[M] α_ =1 _[µ][α]_[ is the total variance in the neural population.] 

770 Dimensionality reduction by PCA is considered successful if a small number of patterns _D_ relative to 771 number of recorded neurons _M_ , accounts for a large fraction of variance explained in the neural state space 772 dynamics. One possible measure of dimensionality is the minimal number of basis patterns in the projection 773 one must keep to achieve some pre-specified fraction, _r_ , of the neural population’s total variance: 

**==> picture [288 x 27] intentionally omitted <==**

- 774 Note, that like any sensible measure of dimensionality based on the neuronal covariance eigenspectrum, 775 this measure is invariant to an overall scaling of the eigenvalues. Fig. 2 of the main paper indicates that 776 many experiments yield exceedingly low dimensional neural state space dynamics, in that a small number of 777 dimensions relative to number of recorded neurons account for a large fraction of explained variance. Indeed, 778 in many experiments, there is an order of magnitude discrepancy between dimensionality and number of 

- 779 recorded neurons, and one of our goals below is to understand the origin of such a large discrepancy, as well 

780 as to understand the accuracy of the dynamical portraits given by _c[α] a_[in the face of extreme subsampling in] 781 the number of recorded neurons. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 782 **II.II Participation ratio as a measure of dimensionality** 

783 While commonly used, measures of dimensionality associated with a given fraction of variance explained 784 are not easily amenable to theoretical analysis. Here, we introduce a closely related measure, namely the 785 participation ratio (PR) of the neural covariance eigenvalue spectrum, that obeys many of the same properties 786 as more traditional measures, but is in contrast, much more amenable to theoretical analysis. The PR is 787 

787 

**==> picture [353 x 39] intentionally omitted <==**

788 Like the fraction of variance explained measure, the participation ratio is also invariant to an overall scaling 789 of eigenvalues. The PR is often used in statistical mechanics to quantify the number of active degrees of 790 freedom in a thermally fluctuating system. Here we are using it to measure how many dimensions of the 791 eigen-spectrum are active, relative to the total variance. 

792 To gain an intuitive understanding of the participation ratio, let us consider an exactly rank- _D_ neural 793 covariance matrix **C**[Neuron] with variance evenly spread across _D_ dimensions: i.e. _µα_ = _µ_ for _α ≤ D_ , 794 and _µα_ = 0 for _α > D_ . The PR is invariant to the overall scale _µ_ and evaluates exactly to _D_[2] _/D_ = _D_ 795 as expected. For a more complex example, consider the eigenvalue spectrum of a typical trial-averaged 796 dataset with full-rank but exponentially decaying eigenvalues: _µα_ = _µe[−] D[α]_ . The spectrum’s PR is again 797 independent of the overall scale _µ_ and evaluates to 2 _D_ in the limit that _D ≪ M_ , which is an intuitively 798 sensible answer, and this value of dimensionality explains roughly 86% of the total variance. As we will 799 further demonstrate below in more examples, the PR and the the measure of dimensionality _D_ ( _r_ ) based 800 on a fraction _r_ of variance explained, are often scaled versions of each other with the scaling constant 801 depending on the shape of the eigenvalue spectrum. Moreover, for several typical spectra, keeping a number 802 of dimensions equal to the PR leads to a fraction of variance explained between 80% to 90%. 

803 While closely related to fraction of variance explained, the considerable theoretical advantage of the 804 PR as a dimensionality measure is that it is an exceedingly simple function of the matrix elements of the 805 neural covariance **C**[Neuron] . In particular, the numerator and denominator in Eq. (11) are simple quadratic 806 functions of the matrix elements. In contrast the eigenvalues _µα_ are highly complex functions of the matrix 807 elements, as they are roots of the characteristic polynomial _P_ ( _µ_ ) = det � **C**[Neuron] _− µ_ **I** �, whose coefficients 808 themselves are polynomials in the matrix elements of **C**[Neuron] of all degrees ranging from 0 to _M_ . In turn, 809 _D_ ( _r_ ) defined in Eq. (10), as a nontrivial function of the eigenvalue spectrum, inherits this complexity as 810 a function of the matrix elements of **C**[Neuron] . Thus the PR is a singular measure in that it embodies many 811 of the intuitive properties we would associate with the notion of dimensionality, and is well correlated with 812 traditional measures of dimensionality, yet it retains considerable analytical simplicity as a direct function 813 of the matrix elements of **C**[Neuron] . 

813 

814 

**II.III A duality between neuronal dimension and task dimension** 

- 815 While the _M_ by _M_ neuronal covariance matrix **C**[Neuron] is widely used for dimensionality reduction, and 816 yields a set of neural basis patterns from which a dynamical portrait may be constructed, the overall structure 817 or pattern of its matrix elements, **C**[Neuron] _ij_ is usually nonintuitve and cannot be succinctly summarized. (See 818 Supplementary Fig. 6A). Alternatively, consider the closely related _NT_ by _NT_ task covariance matrix, 

**==> picture [253 x 22] intentionally omitted <==**

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 819 While the matrix elements **C**[Neuron] _ij_ reflect how the firing rates of neurons _i_ and _j_ co-vary across _NT_ task 820 parameters, the matrix elements **C**[Task] _ab_ reflect how similar (if positive) or different (if negative) the neural population activity patterns across _M_ neurons are for two different task conditions _a_ and _b_ . 

**==> picture [362 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Neuronal Covariance B Temporal Correlation C Auto-correlation Function<br>2 0.5<br>-2 -0.5<br>neuron index time -300 ∆ t -300<br>time<br>neuron index<br>**----- End of picture text -----**<br>


**Supplementary Figure** 6: Neuron-by-neuron covariance versus task-by-task correlation. **A** . The complex _M_ by _M_ neuron-by-neuron covariance matrix for reaches to a single direction in Monkey H ( _M_ = 109 recorded neurons. ) **C**[Neuron] , of the motor cortical data recorded from a monkey reaching to a single target; **B** . The corresponding _NT_ by _NT_ time-by-time task correlation matrix, **C**[Task] , where _NT_ = 600, corresponding to the _T_ = 600ms duration of a trial averaged reach with bin width 1ms. **C** . Example Gaussian auto-correlation function for a stationary task. Here the auto-correlation function is _f_ (∆ _t/τ_ ) where the time-scale _τ_ = 125ms and _f_ ( _x_ ) is a Gaussian profile of variance 1. 

821 

822 A well known property of linear algebra [Strang and Aarikka, 1986] is that the nonzero eigenvalues of 823 **C**[Task] are exactly the same as the nonzero eigenvalues of **C**[Neuron] (after a global rescaling of _[N] M[T]_[due to the] 824 specific normalizations chosen in Eq. (8) and (12)). This implies that any measure of dimensionality based 825 on a scale invariant function of eigenvalue spectra (this of course includes both _D_ ( _r_ ) and PR), will be exactly 826 the same, no matter whether it is computed with the spectrum of **C**[Neuron] or **C**[Task] . It is this precise sense in 827 which neural dimensionality and task dimensionality are inextricably linked. 828 The advantage of **C**[Task] is that the overall structure or pattern of its matrix elements are often much 829 easier to understand intuitively, and therefore to simplify. Compare for example Supplementary Fig. 6A to 830 Supplementary Fig. 6B, as an example of a dual pair of **C**[Neuron] and **C**[Task] in the case of a simple task in 831 which the only task parameter is time into a reach. While the former matrix elements are difficult to interpret, 832 the latter are simple. They reflect the simple fact that patterns of neural activity are more similar to each 833 other the more closely they occur in time relative to each other. When the neuronal dimensionality, measured 834 through the PR, is computed using **C**[Task] instead of **C**[Neuron] in (11), it is clear that neural dimensionality is 

- 835 a very simple function of the similarity of neural activity patterns across pairs of task parameters. This is a 836 key observation that will drive our theory below. 

837 

## **II.IV Dimensionality of simple stationary tasks unfolding over time** 

- 838 To gain further intuition behind the PR, and its relation to _D_ ( _r_ ), we consider the calculation of both in the 839 special case of a simple task indexed only by time, where the task covariance matrix is _stationary_ (up to 840 boundary effects due to finite time _T_ ), which means that the similarity of two neural population activity 841 patterns at two different times depends only on the relative time difference; i.e. **C**[Task] _t_ 1 _,t_ 2[=] _[f]_[(] _[|][t]_[1] _[−][t]_[2] _[|][/τ]_[)][,] 842 where _f_ ( _x_ ) is a smooth and symmetric auto-correlation function (Supplementary Fig. 6C). Here we have 843 separated our description of the autocorrelation function into an intrinsic time scale _τ_ , and an overall shape 844 _f_ ( _x_ ) which takes as its argument a dimensionless ratio of actual time separation to _τ_ . The width of _f_ ( _x_ ) as 845 a function of _x_ is chosen to be _O_ (1). 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

> 846 Now, while in any given experiment, **C**[Task] _t_ 1 _,t_ 2[will][never][exactly][be][of][this][stationary][form,][we][show] 847 below that we can always find a best stationary approximation to **C**[Task] _t_ 1 _,t_ 2[,][and][that][the][dimensionality][of] 848 this approximate stationary version of the task is higher than that of the original. Therefore, understanding 849 the dimensionality of idealized stationary tasks becomes important, and also relevant to understanding the 850 dimensionality of more general non-stationary tasks. 851 To begin, we first note that **C**[Task] _t_ 1 _,t_ 2[is][of][course][a][symmetric][matrix,][but][also][a][Toeplitz][matrix,][as][its] 

> 852 diagonal elements **C**[Task] _t,t_[and off diagonal elements] **[ C]**[Task] _t,t_ +∆ _t_[, are independent of time] _[ t]_[.][As the size of such] 853 a _T_ by _T_ matrix becomes large, summations of any continuous function, _F_ ( _·_ ), of the matrix’s eigenvalues, 854 like the numerator and denominator of the PR in Eq. (11), can be expressed using the Fourier transform of 855 its central row [Gray, 1972], which is a discretized version of the auto-correlation function, _f_ ( _t/τ_ ). If we 856 denote the Fourier transform of this autocorrelation by 

**==> picture [283 x 33] intentionally omitted <==**

857 

which exists as long as _f_ ( _x_ ) is absolutely summable, then we have 

**==> picture [303 x 32] intentionally omitted <==**

858 In practice, when the Toeplitz task-by-task correlation matrix is of a finite size _T_ , the above expression still 859 yields an accurate approximation under some restrictions: first, the stationary task needs to be in the regime 860 where the duration of the task is much longer than the neural activities’ characteristic time scale, i.e. _T ≫ τ_ . 861 Second, when the recorded firing rates are discretized, binned or smoothed before analysis, the bin size or 862 the smoothing kernel of the trial-averaged data needs to be much smaller than characteristic time scale. In 863 other words, if _dt_ is the temporal bin-width, then _τ ≫ dt_ is needed for the approximation to be accurate. 864 Since both assumptions hold to a reasonable approximation in most large scale recordings collected in 865 neuroscience today, we use Eq. (13) and Eq. (14) to compute the neural dimensionality of a stationary task. 866 First, we reformulate the participation ratio in terms of the Fourier transform of the auto-correlation function 867 governing the task-by-task correlation matrix, 

**==> picture [285 x 37] intentionally omitted <==**

We then approximate the numerator term, 

**==> picture [195 x 88] intentionally omitted <==**

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

and the denominator term, 

**==> picture [392 x 129] intentionally omitted <==**

868 

to obtain **C**[Task] ’s participation ratio in terms of the task’s stationary auto-correlation function, 

**==> picture [261 x 27] intentionally omitted <==**

869 Interestingly, the measured dimensionality of neural state space dynamics associated with a simple stationary 870 task scales linearly with the ratio of _T/τ_ , with the constant of proportionality depending only on the shape 871 of the auto-correlation function _f_ ( _x_ ). This result is the mathematical instantiation of the intuition embodied 872 in Fig. 3C of the main paper, namely that a neural trajectory of duration _T_ and autocorrelation with intrinsic 873 timescale _τ_ can explore at most order of magnitude _[T] τ_[dimensions, because one must wait an amount of time] 874 _τ_ before the neural trajectory can bend enough to explore another dimension. The constant of proportionality 875 in Eq. (16) is, for a wide variety of autocorrelation profiles _f_ ( _x_ ), typical of neural data, simply an _O_ (1) pre876 factor, which we explore next. 

## 877 **II.V Example stationary tasks: relation between participation ratio and fraction of variance ex-** 878 **plained** 

879 For concreteness, and further intuition, we compute the two measures of dimensionally, PR and _D_ ( _r_ ) 880 for some example stationary tasks, with their respective auto-correlation functions. For the exponential, 881 _f_ ( _t/τ_ ) = _e[−|][t][|][/τ]_ , the Gaussian, _f_ ( _t/τ_ ) = _e[−][t]_[2] _[/τ]_ and the power-law, _f_ ( _t/τ_ ) = ( _|t|/τ_ + _α_ ) _[−][β]_ , auto882 correlation functions, we tabulate the analytical expressions for their participation ratio in Supplementary 883 Table 1. In all three cases, their Fourier transforms are decreasing functions in frequency, which allows us 884 to compute the dimensionality _D_ ( _r_ ) associated with a given fraction _r_ of variance explained: 

**==> picture [304 x 37] intentionally omitted <==**

885 We obtain simple analytical expressions for _D_ ( _r_ ) in Supplementary Table 1 for the exponential and Gaussian 886 auto-correlation functions. In these cases, just like the PR, _D_ ( _r_ ) also scales linearly with _T/τ_ for any 887 given desired _r_ , indicating a semblance of universality in the conclusion that any reasonable measure of 888 dimensionality is proportional to _T/τ_ for a simple stationary task with intrinsic autocorrelation time scale 889 _τ_ . This holds true regardless of the particular fraction of variance _r_ desired in the measure _D_ ( _r_ ), or the 890 particular shape of the autocorrelations (exponential or Gaussian) we have examined. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

||_f_(_t/τ_) = exp (_−|t|/τ_)|_f_(_t/τ_) = exp<br>�<br>_−t_2_/τ_ 2�|_f_(_t/τ_) = (_|t|/τ_ +_α_)_−β_|_f_(_t/τ_) = (_|t|/τ_ +_α_)_−β_|
|---|---|---|---|---|
|PR<br>D(_r_)|_T_<br>_τ_<br>tan<br>�_πr_<br>2<br>�1<br>_π_<br>_T_<br>_τ_|~~�~~<br>2<br>_π_<br>_T_<br>_τ_<br>inverf(_r_) 2<br>_π_<br>_T_<br>_τ_||2_β −_1<br>2_α_<br>_T_<br>_τ_<br>-|



**Supplementary Table** 1: Analytical expressions for the participation ratio and the factional variance explained dimensionality measures for the Gaussian, exponential and power-law auto-correlation functions. 

891 However, more quantitatively, what fraction of variance is actually explained by keeping a number of 892 dimensions equal to the PR in these examples? This fraction _r_ of variance explained corresponds to the 893 solution to the equation _D_ ( _r_ ) = PR. For the exponential case, this equation reduces to tan � _πr_ 2 � = _π_ , which 894 has an approximate solution of _r_ = 0 _._ 8. For the Gaussian case, this equation reduces to inverf( _r_ ) = ~~[�]~~ _π_ 2[,] _π_ 895 or _r_ = erf = 0 _._ 92. � ~~�~~ 2 � 896 We verify the correctness of these analytical expressions by comparing them against measured dimen897 sionalities of numerically generated temporal correlation matrices under a variety of parameter combina898 tions (Supplementary Fig. 7A,B). Overall, for both PR and _D_ ( _r_ ) (with _r_ = 0 _._ 9), the numerical results show 899 excellent agreement with our analytical expressions throughout the range of simulated _T/τ_ values (Supple900 mentary Fig. 2A,B). For the the dimensionality measure _D_ ( _r_ ) applied to the power-law auto-correlation 901 function, the linear scaling with _T/τ_ is numerically evident, despite the lack of an analytical formula. 

**==> picture [465 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Participation Ratio B Fractional Var Exp C PR, Zoomed In D Frac Var Exp, Zoomed In<br>70 160 9 Gaussian 25 Gaussian<br>Gaussian Gaussian<br>Exponential Exponential<br>Exponential Exponential Power Law, Power Law,<br>Power Law, Power Law, α=1,β=2 α=1,β=2<br>α=1,β=2 α=1,β=2<br>00 T / τ 40 00 T / τ 40 00 T / τ 5 00 T / τ 5<br>Dimensionality Dimensionality Dimensionality Dimensionality<br>**----- End of picture text -----**<br>


**Supplementary Figure** 7: Numerical verifications of analytically computed participation ratios and fractional variance explained for the Gaussian, exponential and power-law auto-correlation functions. **A, B** . Analytical (lines) versus simulated (circles) participation ratio and fractional variance explained measured of dimensionality in the regime with large _T/τ_ . **C, D** . Same as **A, B** , except zoomed in to show the small _T/τ_ regime. 

902 For completeness, we also conducted a comparison between the analytic approximations for dimension903 ality and their direct numerical calculation when _T/τ_ is small, a regime in which the assumptions required 904 for the accuracy of the analytical approximation to the eigenspectra of Toeplitz matrices in Eq. (14) are vi905 olated. As shown in the zoomed-in views (Supplementary Fig. 7C,D), the main deviation, in this regime, of 906 the correct numerical result from its analytical approximation is a constant under-estimation by the analytical 907 approximation. This deviation is simple to understand: if we consider a dataset with just two data points (so 908 that the duration _T_ equals the bin-width _dt_ , which could be much less than the autocorrelation time _τ_ - i.e. 909 _T_ = _dt ≪ τ_ ), the measured dimensionality will always be one, corresponding to the line connecting them, 910 regardless of how close they are in time. The analytical expressions above for dimensionality are not valid in 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

911 this regime, which violates the condition _dt ≪ τ ≪ T_ necessary for accuracy of the analytic approximation 912 to the eigenspectra of Toeplitz matrices in Eq. (14). 

913 In summary, for a stationary task, characterized by an intrinsic autocorrelation time scale _τ_ and total 914 duration _T_ , and sampled in time using bin width _dt_ , both measures of dimensionality, _D_ ( _r_ ) for any _r_ 915 and PR, are proportional to _T/τ_ in the experimentally relevant regime _dt ≪ τ ≪ T_ , independent of the 916 particular shapes of the auto-correlation function we have considered (exponential, Gaussian, and power 917 law), and independent of the bin-width. Moreover, for a variety of typical auto-correlation functions, a 918 number of dimensions equal to the PR explains about 80% to 90% of neural population variance in the data. 919 Having now described the PR, and demonstrated its utility as a sensible measure of dimensionality, as well 920 as its similarity to the more traditional measure _D_ ( _r_ ), we focus on the PR in our subsequent theoretical 921 development, due to its theoretical simplicity. 

## 922 **III Towards Neural Task Complexity: upper bounds on dimensionality through** 923 **destruction of structure** 

924 We now aim to address the first order of magnitude discrepancy in systems neuroscience that we consider 925 in this work, namely that the dimensionality of neural state space dynamics is often far less than the number 926 of recorded neurons, as exemplified by the meta-analysis of 20 datasets in Fig. 2 of the main paper. We 927 seek to explain the origin of this underlying simplicity. Our approach is to ask how high dimensional trial 928 averaged neural state space dynamics could possibly be, given a limited extent of behavioral task parameters 929 visited throughout any given experiment, and the smoothness of neural activity patterns across these task 930 parameters. To address this, we describe a sequence of successive destructions of structure in neural state 931 space dynamics, and prove that each destruction of structure necessarily increases the dimensionality of the 932 dynamics. At the end point of this sequence of destruction, we are left with an exceedingly simple neural 933 state space dynamics that has no structure whatsoever, above and beyond a limited volume and smoothness. 934 The dimensionality of this resulting destroyed state space dynamics is by definition the neural task complex935 ity (NTC) of the original state space dynamics, and by construction, this NTC constitutes an upper bound on 936 the dimensionality of the original state space dynamics. 

937 As described in the previous section, the structure of neural state space dynamics is well characterized by 938 the _NT_ by _NT_ task correlation matrix **C**[Task] , and because of the duality between neural dimensionality and 939 task dimensionality described above, we can compute neural dimensionality, as measured by its participation 940 ratio, by replacing **C**[Neuron] with **C**[Task] in (11), obtaining, 

**==> picture [265 x 39] intentionally omitted <==**

941 Any destruction of structure in the neural state space dynamics corresponds to a manipulation of the matrix 942 elements **C**[Task] _ab_[, that essentially alters the correlation between the neural state, as a pattern of activity across] 943 _M_ neurons, at two different task parameter values _a_ and _b_ . 

## 944 **III.I Increasing dimensionality by reducing long-range correlation** 

945 The simplest destruction of structure in **C**[Task] is simply to reduce the magnitude of any off-diagonal element 946 **C**[Task] _ab_ for _a_ = _b_ . This decreases a single term in the denominator of (18) without changing the numerator, 947 which only depends on the diagonal elements **C**[Task] _aa_[, and therefore increases the dimensionality.][Intuitively,] 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

948 reducing the squared correlation between neural activity patterns at two different task parameters allows the 949 resulting dynamics to explore more dimensions. 

950 As specific example, consider a single periodic neural trajectory that is confined to oscillate with period 951 _τ_ . Then the task parameter _a_ indexes time _t_ , and the task correlation matrix **C**[Task] _t_ 1 _t_ 2[has peaks in off-diagonal] 952 bands whenever _t_ 1 _− t_ 2 is an integer multiple of _τ_ , reflecting the fact that after every time _τ_ , the neural 953 dynamics is forced to revisit the same neural activity pattern by virtue of the oscillation. Consider instead a 954 destroyed dynamics in which all off-diagonal elements **C**[Task] _t_ 1 _t_ 2[areset to][ 0][ for all] _[ |][t]_[2] _[−][t]_[1] _[| ≥][τ]_ 2[.][The resulting] 955 destroyed dynamics only has a central band of correlation for _|t_ 2 _− t_ 1 _| ≤[τ]_ 2[,][reflecting][the][smoothness][in] 956 time, but not the periodicity, of the original dynamics. The destroyed dynamics behaves more like a smooth 957 random walk with an approximate autocorrelation time _τ_ , that never revisits the same point in neural state 958 space over long times, and therefore can explore more dimensions than the original periodic dynamics. In 959 this sense, the destruction of long-range temporal correlations necessarily increases dimensionality. 

## 960 **III.II Increasing dimensionality by homogenizing dynamics** 

961 A second way to destroy structure in the task-by-task correlation matrix **C**[Task] _ab_[is][to][homogenize][it][by][re-] 962 placing each of a subset of the matrix’s off-diagonal entries with their average. This replacement increases 963 dimensionality by again reducing PR’s denominator, without affecting the numerator, which only depends 964 on diagonal elements. To see this, first consider Jensen’s inequality, which states that for any convex function 

965 _g_ , 

**==> picture [70 x 11] intentionally omitted <==**

966 where _x_ is any random variable drawn from a distribution _P_ ( _x_ ), and _⟨·⟩_ denotes an average with respect 967 to this distribution. To apply Jensen’s inequality, consider a specific subset of _K_ off diagonal elements 968 of **C**[Task] _ab_[,][indexed][by] _[γ]_[=][1] _[, . . . , K]_[,][taking][the][values] _[x][γ]_[.][Here][each] _[γ]_[indexes][a][particular][pair][of][task] 969 parameters ( _ab_ ) with _a_ = _b_ , and _xγ_ is the value **C**[Task] _ab_[.][Let][the][distribution] _[P]_[(] _[x]_[)][=] _K_ 1 � _Kγ_ =1 _[δ]_[(] _[x][ −][x][γ]_[)][.] 970 _P_ ( _x_ ) places equal probability mass on the chosen elements. Also let _g_ be the convex function _g_ ( _x_ ) = _x_[2] . 971 Then according to Jensen’s inequality, the average of the squares of _x_ 1 _, . . . , xK_ is greater than or equal to 972 their average squared, or 

**==> picture [119 x 35] intentionally omitted <==**

973 If we denote the average by _x_ ¯ = _K_ 1 � _Kγ_ =1 _[x][γ]_[,][this means that replacing each] _[ x][γ]_[with the average value] _[x]_[¯] 974 leads to a smaller denominator in Eq. (18), since the above inequality implies[�] _[K] γ_ =1 _[x]_[2] _γ[≥]_[�] _[K] γ_ =1 _[x]_[¯][2][=] _[ K][x]_[¯][2][.] 975 By reducing the denominator of the PR without changing the numerator, the dimensionality goes up. 976 Thus intuitively, any inhomogeneities in the off diagonal task-task correlation matrix **C**[Task] _ab_ reflect in977 herent structure in the neural state space dynamics, through different degrees of similarity between neural 978 activity patterns at different pairs of task parameters _a_ and _b_ . Destroying such structure by homogenizing it, 979 i.e. replacing a subset of off-diagonal elements by their average, necessarily increases the dimensionality of 980 the resulting destroyed dynamics. 

## 981 **III.III The best stationary approximation to a task has higher dimensionality than the original task** 

982 A simple, but important application of the above method for destroying structure is the result that the best 983 stationary approximation of the task-by-task correlation matrix associated with a single task parameter (Sup984 plementary Fig. 8A,B) has increased dimensionality. Consider a simple task where the task parameter _a_ 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

> 985 indexes time _t_ only. In general such a task will be non-stationary, so that the matrix elements **C**[Task] _t_ 1 _t_ 2[will not] 986 be a function of the time separation _|t_ 2 _− t_ 1 _|_ only. What is the best stationary approximation to this neural 987 dynamics, described by a corresponding stationary task-task covariance matrix **C**[Sta] _t_ 1 _t_ 2[=] _[ f]_[(] _[|][t]_[2] _[−][t]_[1] _[|]_[)][, where] 988 by definition, the best one minimizes the squared error 

**==> picture [116 x 25] intentionally omitted <==**

989 By the usual result that the single number _x_ ¯ that minimizes the squared distance to a fixed collection of 990 _K_ numbers _x_ 1 _, . . . , xK_ is the average of those numbers, _x_ ¯ = _K_ 1 � _Kγ_ =1 _[x][γ]_[,][it][is][easy][to][see][that][the][best] 991 stationary approximation is the one that averages the diagonals and off-diagonals of **C**[Task] : 

**==> picture [300 x 20] intentionally omitted <==**

992 When _t_ 2 = _t_ 1 the average corresponds to homogenizing in time an off-diagonal band of **C**[Task] , which by 993 the above section increases dimensionality by decreasing the denominator of the PR in (18). However, the 994 diagonal band is also averaged. Fortunately, this does not change the numerator of the PR, which is simply 995 the sum of the diagonals squared. Thus overall, the best stationary approximation to a task, by destroying 996 structure in the original task associated with temporal inhomogeneities, has increased dimensionality relative 997 to the original task. See Supp. Fig. 8AB for an example of a non-stationary task and its best stationary 998 approximation. In neural data analyzed in this work, this best stationary approximation is very well modeled by a Gaussian shaped autocorrelation profile (Supp. Fig. 8C). 

**==> picture [364 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Temporal Correlation B Stationary Approximation C Auto-correlation Function<br>-250 0.5 -250 0.5<br>350 -0.5 350 -0.5<br>-250 350 -250 350 -300 -300<br>time (ms) time (ms) ∆ t (ms)<br>time (ms) time (ms)<br>**----- End of picture text -----**<br>


**Supplementary Figure** 8: Example stationary approximation of a trial-averaged dataset. **A** . The task-by-task correlation matrix, **C**[Task] , of motor cortical state space dynamics while Monkey H is reaching to a single target. **B** . The best stationary approximation **C**[Sta] to **C**[Task] obtained by replacing the diagonal and the off-diagonals with their respective averages. **C** . A Gaussian fit (red) to the measured auto-correlation function of the best stationary approximation (blue). 

999 

1000 In general, once we have the best stationary approximation **C**[Sta] and its associated autocorrelation func1001 tion _F_ (∆ _t_ ), we can proceed in one of several ways to obtain an upper bound on the dimensionally of the 1002 original neural state space dynamics described by **C**[Task] . First, a natural further destruction of structure is to 1003 destroy long range correlations, as described above, by setting to 0 _F_ (∆ _t_ ) for _|_ ∆ _t|_ greater than some thresh1004 old, which is chosen to include the central peak of _F_ near the origin, but exclude other structure associated 1005 with peaks in _F_ away from the origin. This process is designed to obtain dimensionality upper bounds that 1006 incorporate local smoothness alone, and no other longer range structure. 

1007 With this modified _F_ one could write _F_ in the form _F_ (∆ _t_ ) = _f_ (∆ _t/τ_ ), thereby separating the width of 1008 the central peak of _F_ , as described by _τ_ , and the shape of the central peak of _F_ , as described by the function 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1009 _f_ ( _x_ ) which has width in its dimensionless argument _x_ of _O_ (1). Then the resulting dimensionality upper 1010 bound is given by Eq. (16). This dimensionality upper bound is proportional to _T/τ_ , up to a constant _O_ (1) 1011 factor that depends on the detailed shape of _f_ ( _x_ ). It turns out that in the neural data analyzed in this paper, 1012 the shape of _f_ ( _x_ ) was well approximated by a Gaussian profile, yielding the constant factor ~~�~~ _π_ 2[and][the] 1013 resulting NTC for a single task parameter of 

**==> picture [247 x 24] intentionally omitted <==**

1014 reported in the main paper. 

1015 Now this procedure for obtaining an NTC that upper-bounds neural dimensionality seems to depend on 1016 knowing many details of the neural data beforehand. However, it is exceedingly easy to estimate a likely 1017 NTC _before_ the neural data is collected. Basically, one simply needs to estimate _τ_ , the approximate width 1018 of the central peak of the temporal autocorrelation function of the neural trajectory, and know the total 1019 duration _T_ of the neural trajectory. One need not know in detail the exact shape of the central peak, as this 1020 only contributes an _O_ (1) constant of proportionality. For example, if it is Gaussian then this constant is 1021 2[Supp.][Table 1).][However, when one is attempting] ~~�~~ _π_[= 0] _[.]_[8][, while if it is exponential then it is][ 1][ (see e.g.] 1022 to explain 1 to 2 order of magnitude discrepancies between neural dimensionality and number of recorded 1023 neurons, then these _O_ (1) differences in NTC due to different shapes of the auto-correlation function are 1024 not that important. Similarly, when one is attempting to estimate a likely NTC in future recordings for the 1025 purposes of designing experiments, these _O_ (1) differences again are not as important - i.e. they may not be 1026 the dominant source of estimation error. 

1026 

1027 

1028 

## **III.IV For multiple task parameters, a factorized stationary approximation to a task has higher dimensionality** 

1029 For datasets with _K_ task parameters, the task-by-task correlation matrix has a block structure. For example, 1030 for the eight-direction center-out reach task in shown in Figure 3D of the main paper with _K_ = 2, the 1031 correlation matrix consists of eight-by-eight blocks of _T_ -by- _T_ temporal correlation or cross-correlation 1032 matrices (Supplementary Fig. 9A): entries of the (1 _,_ 1) block denote the correlations between neural activity 1033 patterns at different time points for reaches to the first target, whereas entries of the (1 _,_ 2) block denote the 1034 cross-correlations between neural activity patterns at some time during the reach to the first target and at a 1035 different time during the reach to the second target. 

1036 To upper bound the dimensionality of such compound correlation matrices, with multiple task param1037 eters, we destroy structure in a specific way that leads to a stationary and factored approximation to the 1038 original correlation matrix. The dimensionality of this stationary factored approximation is then defined 1039 to be the NTC, and by construction, it upper bounds the dimensionality of the original data. To arrive at 1040 the stationary factorized approximation, we follow a two-step procedure (Supplementary Fig. 9B). The first 1041 step is to obtain a stationary approximation to the original task covariance matrix, using an extension of the 1042 logic we used in the _K_ = 1 parameter case. With _K_ parameters, the task manifold in parameterized by a 1043 _K_ -tuplet of numbers ( _t_[1] _, . . . t[K]_ ). Let two _K_ -tuplets, ( _t_[1] 1 _[, . . . t]_ 1 _[K]_[)][ and][ (] _[t]_[1] 2 _[, . . . t][K]_ 2[)][ denote two points on the] 1044 task manifold, and let the task correlation matrix **C**[Task] ( _t_[1] 1 _[,t]_[1] 2[)] _[,...,]_[(] _[t][K]_ 1 _[,t][K]_ 2[)][denote the correlation between the two] 1045 neural activity patterns associated with two points on this task manifold. In general, this task correlation will 1046 not be stationary, in that it will not be a function of only differences between points, i.e. of ∆ _t[k]_ = _t[k]_ 2 _[−][t][k]_ 1[.] 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1047 

We can find the best stationary approximation by averaging along off-diagonals through 

**==> picture [382 x 20] intentionally omitted <==**

1048 Via arguments similar to those presented in the previous section, the resulting stationary, block Toeplitz 1049 approximation of the task correlation matrix has a higher dimensionality than the original task correlation 1050 matrix. Interestingly, this approximation is diagonalizable, since it is an example of a Hewitt block Toeplitz 1051 matrix, but its correlation structure is still too complex for the resulting dimensionality upper bound to be 1052 intuitive and interpretable. 

**==> picture [487 x 103] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Compound Correlation B Factored Approximation<br>1 0.5 -250 1 1<br>=<br>-1 -0.5 350 0 -1<br>time/angle angle -250 time (ms) 350 time/angle<br>time/angle reacn angle time (ms) time/angle<br>**----- End of picture text -----**<br>


**Supplementary Figure** 9: Example stationary and factor approximation of a trial-averaged dataset of a monkey doing the eight-direction center-out reach task. **A** . The compound task-by-task correlation matrix, **C**[Task] , of the motor cortical data during reaches to all possible directions. Inner indexes denote time during the reaches, while the outer blocks denote the different reach targets. **B** . The factored and stationary approximation to **A** as the Kronecker product of an angle-by-angle and a time-by-time stationary correlation matrices. 

1053 Instead, we apply a second approximation step to factorize the contributions of each task parameter. 1054 Formally, we decompose the approximate stationary compound correlation function, _f_[approx] (∆ _t_[1] _, . . . ,_ ∆ _t[K]_ ), 1055 into a product of individual task parameters’ auto-correlation functions, 

**==> picture [295 x 30] intentionally omitted <==**

1056 This factorization is the same as approximating the stationary compound correlation matrix with a Kronecker 1057 product, 

**==> picture [310 x 30] intentionally omitted <==**

where each of the component matrix is a task parameter’s stationary correlation matrix, whose NTC and dimensionality is given by the corresponding auto-correlation function, _g[k]_ ( _·_ ). Since the resulting eigenvalues of the Kronecker product are all possible outer products of the form of[�] _[K] k_ =1 _[µ][k,i][k]_[, with] _[ µ][k,i][k]_[denotes the] 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

_ik_ th eigenvalue of the **C** _[k]_ factor, the participation ratio of the factored and stationary approximation is, 

**==> picture [192 x 108] intentionally omitted <==**

- 1058 which is precisely the product of the NTCs for each of the task parameters. 

For this approximation to be an upper bound on the original correlation matrix’s dimensionality, we still need to prescribe a factorization procedure that yields a guaranteed increase in dimensionality. The factorization we choose is a recursive projection procedure, where we successively replace the off-diagonal blocks of the stationary approximation with their projections onto the diagonal blocks. In terms of the _·_ auto-correlation factors, _g[k]_ ( )s, the recursive projection procedure is given by, 

**==> picture [355 x 77] intentionally omitted <==**

... 

- 1059 To see that this procedure produces an approximation that upper bounds dimensionlality, we first note that the 1060 numerator of the resulting approximation’s participation ratio is unchanged from the stationary approxima1061 tion, since only the off-diagonal blocks are replaced by projections. Secondly, we note that the denominator 1062 of the participation ratio, which is the sum of squares of the off-diagonal blocks’ entries, can only be de1063 creased by the projections. Consequently, the dimensionality of the factored approximation upper bounds 1064 that of the stationary approximation which in turn upper bounds that of the original task correlation matrix. 1065 For example, one can compare the original task correlation matrix (Fig. 9A) to its stationary factorized 1066 approximation (Fig 9B) in the case of a center out reach task studied in the main paper. 

## 1067 **III.V Algorithmic computation of neural task complexity** 

1068 Here we summarize the algorithmic steps required to compute the NTC. 1069 To compute the NTC of a trial-averaged dataset with a single task parameter, _t_ , in practice, we have the 1070 following procedure: 

- 1071 _•_ Mean-subtract each neurons’ averaged activity across task parameters from each row of the neurons 1072 by task parameter data matrix **X** . 

- 1073 _•_ Compute data’s task-by-task correlation matrix **C**[Task] = **X** _[T]_ **X** . 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 1074 _•_ Find the best stationary approximation of **C**[Task] , and construct the corresponding auto-correlation 1075 function _f_[approx] (∆ _t_ ) = � **C**[Task] _t,t_ +∆ _t_ � _t_[.][If][necessary,][set][any][long-range][correlations][to][zero,][while] 1076 keeping the short-range correlations induced by smoothness alone. 

- 1077 _•_ If _f_[approx] ( _·_ ) can be fitted with a simple form, such as the Gaussian, exponential or power-law auto1078 correlation function whose participation ratio we’ve computed analytically (See Supplementary Table 1079 1), extract the relevant auto-correlation scale _τ_ and substitute it into the appropriate participation ratio 1080 expression to obtain the NTC. 

- 1081 _•_ If the stationary approximation has a non-classical functional form for the auto-correlation function, 1082 one can still compute an NTC that depends, up to an _O_ (1) factor, on the detailed shape of this auto1083 correlation function through the formula for the PR derived in (16). 

1084 To compute the NTC of a dataset with multiple task parameters, we have the following procedure: 

- 1085 _•_ Mean-subtract each neurons’ activity averaged over all task parameters for rows of the data matrix **X** . 

1086 

1087 

- Compute the compound task-by-task correlation matrix, **C**[Task] = **X** _[T]_ **X** . 

- Compute **C**[Task] ’s stationary approximation with the averaging procedure, 

**==> picture [248 x 21] intentionally omitted <==**

1088 

and its factorization with the prescribed recursive projection procedure (24), 

**==> picture [157 x 31] intentionally omitted <==**

- 1089 _•_ Compute the correlation lengths and the dimensionalities for the individual task parameter’s the sta1090 tionary approximation, **C** _[k]_ , as described for the single-parameter case. The resulting product of di1091 mensionalities is then the NTC for this dataset of multiple task parameters. 

## 1092 **IV Examples of the relationship between dimensionality and neural task complex-** 1093 **ity** 

## 1094 **IV.I Dimensionality and neural task complexity for discrete stimuli or behavioral conditions** 

1095 Thus far, we focused on continuous task parameters that evoke smoothly evolving neural activity patterns, 1096 and showed how to compute a simple NTC measure that upper bounds the dimensionality of the neural data 1097 by taking into account only the extent of each task parameter and the neural correlation length along each 1098 task parameter. Is there a similar concept of NTC for stimuli or behaviors that are discrete? With _P_ discrete 1099 stimuli, the resulting trial-averaged neural activity patterns can, of course, span a _P_ -dimensional subspace 1100 of the neural space as long as the number of recorded of neurons exceeds that of the number of trials, i.e. 1101 _M ≥ P_ . Thus _P_ is a natural, if trivial, measure of NTC in this case. 

1102 A more interesting quantity in this situation may be the dimensionality of a _random_ data set. Consider 1103 for example a situation in which _P_ stimuli or behavioral conditions, indexed by _a_ = 1 _, . . . , P_ , yield _P_ 1104 random (mean subtracted) activity patterns across all _N_ neurons in a circuit. By this we mean that the 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1105 mean subtracted activity **x** _ia_ of neuron _i_ in stimulus _a_ are uncorrelated across both neurons and stimuli, and 1106 drawn i.i.d from a Gaussian distribution of mean 0 and variance 1 (since our dimensionality measures are 1107 independent of overall scale, we simply normalize the variance to be 1). This means that for large _N ≫ P_ , 1108 the task correlation matrix of the full neural population, **C**[Task] = _N_ 1 **[X]** _[T]_ **[ X]**[,][where] **[X]**[is][the] _[N]_[by] _[P]_[data] 1109 matrix, converges to a _P_ by _P_ identity matrix, and therefore has a dimensionality, measured by its PR, to be 1110 _P_ . This is a reflection of the fact that in very high dimensions ( _N ≫ P_ ), all � _P_ 2 � pairs of random vectors in 1111 _N_ dimensional space are overwhelmingly likely to be close to right angles with respect to each other. Thus 1112 the _P_ neural patterns form an orthogonal basis and have dimensionality _P_ . 

1113 However, the situation is very different if we don’t record all _N_ neurons, but instead record only _M_ 1114 neurons, where _M_ may be the same order of magnitude as the number of stimuli/behaviors, _P_ . The data 1115 matrix **X** is then a smaller _M_ -by- _P_ dimensional random matrix, whose entries are generated i.i.d. with zero 1116 mean and unit variance. In the limit in which _M_ and _P_ are large, while the ratio is _O_ (1), the distribution of 1117 eigenvalues of **C**[Task] , converges to the Marchenko-Pastur law [Marchenko and Pastur, 1967], 

**==> picture [349 x 26] intentionally omitted <==**

1118 This law allows us to evaluate the numerator of the PR, which is the squared sum of the eigenvalues of 1119 **C**[Task] , as well as the denominator, which is the sum of squares of eigenvalues of **C**[Task] . The resulting 1120 dimensionality, or ratio of these two quantities, is simply, 

**==> picture [256 x 26] intentionally omitted <==**

1121 This of course reduces to the previous result of dimensionality _P_ when the number of recorded neurons _M_ 1122 is much larger than _P_ . For example, if _M_ = 10 _× P_ , then the measured dimensionality would be about 1123 0 _._ 9 _× P_ . However, the cloud of neural activity patterns becomes geometrically distorted as we subsample _P_ 1124 neurons down to the point where _M_ is not much larger than _P_ . In that case, all � 2 � pairs of neural activity 1125 patterns are no longer sufficiently orthogonal, leading to a proliferation of small, but non-negligible, off 1126 diagonal elements in the _P_ by _P_ matrix **C**[Task] that conspire to reduce the measured dimensionality of the 1127 random neural dataset, relative to what one would find if one recorded all _N_ neurons. 

> 1128 The dimensionality PR[rand] of a random dataset yields an interesting null model with which to compare 1129 dimensionality measured in actual experiments with _P_ discrete stimuli, especially after the neural activity 1130 patterns have been normalized to have the same length in firing rate space. Indeed, comparison of measured 1131 dimensionality to this null model dimensionality, as opposed to the NTC upper bound, which is simply _P_ , 1132 provides a powerful guideline for the interpretation of neural data. When the measured dimensionality is 1133 far below PR[rand] , the dataset is more correlated and lower-dimensional than what one would expect from 1134 random data, suggesting that circuit dynamics may be constraining neural activity patterns to live in a low 1135 dimensional space. On the other hand, when the measured dimensionality is higher than PR[rand] , the neural 1136 circuit may be actively de-correlating neuronal activity patterns to make them more orthogonal than one 1137 would expect by chance. 

## 1138 **IV.II Random smooth manifolds have dimensionality equal to neural task complexity** 

We return to the case of a smooth, trial averaged neural state space dynamics in a task with _K_ task parameters. What kind of state space dynamics would have a dimensionality that would necessarily saturate the upperbound set by the NTC, given we have recorded enough neurons _M_ ? Intuitively, the answer is a smooth 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

random manifold that has the same autocorrelation lengths across task parameters and moreover factorizes across task parameters, with no other structure to further constrain its dimensionality. Such a random neural manifold for the state space dynamics is generated randomly by drawing each neuron’s response given the task parameters independently from a stationary random gaussian process with covariances determined by the data’s factored correlations. Formally, the joint distribution of the neural activities is Gaussian, and obeys the following, 

**==> picture [240 x 47] intentionally omitted <==**

1139 where _xi_ ( _t_[1] _, . . . , t[K]_ ) denotes neuron _i_ ’s firing rate at the point in the task manifold given by the _K_ -tuplet 1140 ( _t_[1] _, . . . , t[K]_ ). Since the task-by-task correlation matrix of this generated manifold is exactly factored and 1141 stationary as specified, its measured dimensionality must saturate the NTC upper bound constrained by only 1142 smoothness, as long as we measure enough neurons _M_ , so that the empirically measured autocorrelation 1143 functions converge in limit to those that generated them. 1144 We simulate such a smooth random manifold with _K_ = 2 and gaussian auto-correlation functions with 1145 circular boundaries parameterized by lengths _L_[1] _[,]_[2] = 100 and autocorrelation lengths _λ_[1] _[,]_[2] = 12 _,_ 20 in 1146 arbitrary units. This yields an NTC of 26. With a large total population of _N_ = 1000, relative to the NTC, 1147 the measured participation ratio of the simulated manifold is 26, and indeed saturates the dimensionality 1148 upper bound set by the NTC as predicted. 

**==> picture [129 x 111] intentionally omitted <==**

**----- Start of picture text -----**<br>
30<br>NTC<br>20<br>10<br>0<br>0 400 800<br># recorded neurons (M)<br>measured dimensionality<br>**----- End of picture text -----**<br>


**Supplementary Figure** 10: Measured dimensionality of subsampled a random smooth manifold. A random smooth manifold with intrinsic dimensionality of 2 is generated with 1,000 simulated neurons as a Gaussian process with an NTC of 26 ( _L_[1] _[,]_[2] = 100 _, λ_[1] _[,]_[2] = 12 _,_ 20). For each value of _M_ , a random subset of the simulated neurons is kept to simulated recording. Measured participation ratios of the resulting subsampled data are plotted as function of _M_ , and compared against the NTC (horizontal line). 

1149 In practice, however, we never record from the entire population of _N_ neurons. Suppose we only record a 1150 subset of _M_ neurons. How would the measured dimensionality scale with _M_ , and how large would _M_ have 1151 to be before the measured dimensionality approached the true dimensionality of the random smooth mani1152 fold which is equal to the NTC? We answer these questions by subsampling the number of neurons in the 1153 generated random dataset. When plotted as a function of the number of recorded neurons, _M_ , (Supplemen1154 tary Fig. 10), the measured participation ratio of the subsampled data stayed close to the true dimensionality 1155 as long as the number of recorded neurons is much higher than the NTC. Only when the number of recorded 1156 neurons gets closer to the NTC, does the measured dimensionality start to decrease significantly due to the 1157 more stringent constraint of the limited number of recorded neurons. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1158 These results are completely parallel to the case of random clouds of _P_ points discussed in the previous 1159 section, as opposed to smooth manifolds discussed here. There we found that measured dimensionality 1160 monotonically increased with number of recorded neurons _M_ in an analytically controllable manner (See 1161 Eq. (26)) ultimately saturating as _M ≫ NTC_ = _P_ . In fact, the red curve in Fig. 10 reflecting the measured 1162 dimensionality as a function of number of recorded neurons, is the analog for smooth random manifolds of 1163 Eq. (26) for random point clouds. 

## 1164 **IV.III Intrinsic constraints on neural dynamics can prevent dimensionality from approaching the** 1165 **NTC** 

1166 In this section, we demonstrate an example simulated dataset that does not saturate the NTC dimensionality 1167 upper bound like the _random_ smooth manifold. The key idea is to generate neural firing rate patterns that are 1168 fundamentally constrained by neural network connectivity. In particular, we build an _N_ -dimensional linear 1169 dynamical system that evolves according the difference equation, 

**==> picture [140 x 12] intentionally omitted <==**

1170 where _**η**[t]_ is a time-dependent driving input. The length- _N_ vector **x** _[t]_ denotes the population activity pattern 1171 at time _t_ , and the _N_ -by- _N_ connectivity matrix **W** defines the connectivity of the network. For simplicity, 1172 we assume the inputs to be white noise. 

**==> picture [273 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
A. Dynamical System Architectures C. Dim of Subsampled Data<br>a a a 120<br>b b b<br>… NTC<br>a=0.3, b=0.7 80<br>B. Fitted Auto-correlation Function<br>1<br>τ=7.8 40<br>0<br>0 50 00 400<br>∆ t # recorded neurons (M)<br>measured dim<br>**----- End of picture text -----**<br>


**Supplementary Figure** 11: **A** . Architectures of a non-normal linear dynamical system with non-smooth trajectories but low dimensionality. **B** . Fitted auto-correlation function of the simulated data with an exponential function. The data is simulated with _a_ = 0 _._ 3 _, b_ = 0 _._ 7 _, N_ = 400 and a duration of 800. **C** . Measured dimensionality of subsampled simulated data compared against the NTC. 

1173 We construct a non-normal system with a distributed delay-line architecture (Supplementary Fig. 11A). 1174 Its connectivity has the general form, 

**==> picture [142 x 54] intentionally omitted <==**

**----- Start of picture text -----**<br>
 a ab b <br>T<br>W  =  U U  ,<br>... ...<br>a<br> <br>**----- End of picture text -----**<br>


1175 where _a_ and _b_ are the feedback and feedforward gains at each node; and **U** is an arbitrary orthogonal matrix 1176 that distributes the nodes across neurons. With a reasonably large feedforward gain, _b_ , input evoked network 1177 activity patterns propagate rapidly from one pattern to another associated with successive nodes, resulting 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1178 in fast-changing single-neuron time courses with a low smoothness value and a high NTC. Despite the non1179 smooth responses, the system, however, can still be low-dimensional. By the time an input signal propagates 1180 to the end of the delay line, it would have incorporated feedforward amplification from all preceding nodes 1181 so that the final variance of neural activity along the pattern associated with the last node dominates the total 1182 variance of the entire network, resulting in very low dimensionality of the recorded data. 

1183 To demonstrate a numerical example, we constructed such a non-normal system with _N_ = 400, _a_ = 0 _._ 3, 1184 _b_ = 0 _._ 7 and a random orthogonal matrix **U** , and simulated recordings of neural activity patterns over a 1185 duration of 800 time steps. By construction, the simulated neural activity patterns have a short characteristic 1186 time scale of _τ_ = 7 _._ 8 time-steps, obtained by fitting an exponential auto-correlation function to the stationary 1187 approximation of the temporal correlation matrix. The corresponding NTC of the simulated data is then 1188 800 _/_ 7 _._ 8 = 102, which is not saturated by the data’s dimensionality of 40, measured by the participation 1189 ratio (Supplementary Fig. 11C). 

1190 Overall, this model constitutes an example of the elusive experimental regime (iii) in Fig. 4A of the main 1191 paper. One need not record all _N_ = 800 neurons in the circuit for the dimensionality to stabilize. In fact the 1192 dimensionality stabilizes already at _M_ = 400 neurons, which is about 10 times the actual dimensionality 1193 of 40. So basically, the actual dimensionality is both much less than the number of recorded neurons _and_ 1194 much less than the NTC - the key signatures of experimental regime (iii). In this case, the gap between the 1195 actual dimensionality and the NTC reflects an additional circuit constraint that does not arise from temporal 1196 smoothness alone. This constraint corresponds to preferential amplification of a subset of activity patterns 1197 associated with the nodes near the end of the hidden delay line. 

## 1198 **V Neural task complexity and random projections as a theory of neural measure-** 1199 **ment** 

1200 

## **V.I Review of random projection theory** 

1201 Dimensionality reduction techniques such as principal component analysis attempt to reduce the dimen1202 sionality of neural data in a targeted way by computing some data-dependent statistics first, such as the 1203 covariance matrix. Alternatively, a dataset may also be dimensionally reduced by simply projecting full data 1204 points in a high _N_ -dimensional space (in our application with think of _N_ as the _total_ number of behaviorally 1205 relevant neurons in a circuit) into a randomly chosen _M_ -dimensional subspace ( _M_ will correspond to the 1206 number of recorded neurons and is much less than _N_ ). Despite its simplicity, random projections have 1207 been shown to nicely preserve the geometric structure of the original high-dimensional data. This structural 1208 preservation is measured through the fractional distortion in distance between pairs of data points before and 1209 after the projection. Formally, for a pair of _N_ -dimensional data points, **x** _t_ 1 and **x** _t_ 2 and an _M_ -by- _N_ random 1210 orthogonal projection operator **P** , the pairwise distance distortion is defined as, 

**==> picture [148 x 27] intentionally omitted <==**

1211 where the ratio ~~�~~ _N/M_ corrects for the expected shrinking of distances under a projection from _N_ to _M_ 1212 dimensions. If this distortion were equal to 0 for all possible pairs, the geometric structure of the dataset 1213 would be preserved, since all pairs of points would have the same distance (up to an overall scale) before 1214 and after the projection. However, when _M < N_ , this is impossible for all pairs of points. 1215 The Johnson-Lindenstrauss lemma [Johnson and Lindenstrauss, 1984, Dasgupta and Gupta, 2003], a fun1216 damental result in the theory of random projections, considers high-dimensional datasets with _P_ arbitrary 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1217 points in the high _N_ -dimensional space. The lemma states that, with a probability of at least 1 _− ρ_ , a random 1218 projection of the _P_ data points into a _M_ -dimensional subspace has bounded pairwise distance distortions 1219 for _all_ possible pairs, 

**==> picture [87 x 11] intentionally omitted <==**

1220 as long as the target subspace’s dimensionality, _M_ , is of the order, 

**==> picture [92 x 25] intentionally omitted <==**

1221 where _ϵ_ denotes the maximal, or worse case distortion in distances between all pairs of data points. In other 1222 words, the JL lemma tells us that, for random projections to preserve the geometry of a dataset up to some 1223 level of tolerance _ϵ_ in the fractional error of pairwise distances, it is sufficient to scale the dimensionality _M_ 1224 of the projected subspace as 1 _/ϵ_[2] and only as the _logarithm_ of the number of data points, _P_ . 1225 While proven initially for sets of arbitrary data points, the JL lemma has also been extended to datasets 1226 with known prior structures. One such extension considers points occupying a _D_ -dimensional linear sub1227 space of the full _N_ -dimensional space [Indyk and Motwani, 1998]. The corresponding condition to preserve 1228 the geometry of a dataset up to a maximal distortion level _ϵ_ requires the projected subspace dimension _M_ to 1229 scale as 

**==> picture [136 x 25] intentionally omitted <==**

1230 Note that a subspace of dimension _D_ is extremely “large”, in the sense that if one wishes to fill a ball 1231 of any given radius within the subspace with a cloud of points at a fixed density, the requisite number of 1232 points would have to scale _exponentially_ with _D_ . This phenomenon is one manifestation of the curse of 1233 dimensionality; adequate exploration through sampling of a space of dimension _D_ , without missing any 1234 regions, requires a number of samples that grows exponentially with _D_ . However, despite this curse of 1235 dimensionality, the number of random projections _M_ required to preserve the geometry of _all_ pairs of points 1236 within a subspace of dimension _D_ at some fixed distortion _ϵ_ , need only scale _linearly_ with _D_ . Roughly, 1237 the subspace JL lemma follows from the pointwise JL lemma by making the replacements _P → e[D]_ and 1238 log _P → D_ . In this sense they are consistent with each other. 

1239 A similar extension considers data points sampled from a low _K_ -dimensional non-linear manifold with 1240 a finite volume _V_ embedded in an _N_ -dimensional space [Baraniuk and Wakin, 2007]. The sufficient con1241 dition to preserve the geometric structure of the data to within fractional distortion _ϵ_ requires the subspace 1242 dimension _M_ to scale as, 

**==> picture [224 x 25] intentionally omitted <==**

1243 This scaling is similar to the linear subspace case, as it grows logarithmically with the volume of the man1244 ifold. Given that the volume of a manifold grows exponentially with the intrinsic dimension (log _V ∝ K_ ), 1245 the scaling of _M_ is, in fact, linear in the dataset’s intrinsic dimension _K_ . Different from the previous two 1246 cases, however, the random projection of manifolds includes an addition dependency on the embedding di1247 mensionality, _N_ , which we will check in the next section with simulations. The condition number _τ_ and 1248 geodesic covering regularity _R_ characterizes the curvature of the nonlinear manifold, which are properties 1249 of the manifold’s geometry. 

1250 These theoretical results all suggest that random projections yield extremely efficient representations of 1251 high-dimensional data, as long as the number of coefficients in the reduced representation grows logarithmi1252 cally with the amount of data. With different theorems, this amount of data is measured in different ways: by 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1253 the number of data points in the JL lemma, by the exponentiated subspace dimension for linear subspaces, 1254 and by the volume of a nonlinear manifold. 

1255 In the main paper, we argue that, in many scenarios, random projection theory constitutes a good model 1256 of the process of neural measurement of a random subset of _M_ neurons. Conceptually, the process of 1257 projecting high-dimensional data points into a randomly generated low-dimensional subspace in a random 1258 and data-blind way is similar to the random sampling of the high-dimensional patterns of neural activity 1259 across all _N_ neurons in a circuit, down to a random subset of _M_ neurons that happen to be measured in a 1260 single experiment. Indeed, when the full _N_ -dimensional neural activity patterns are randomly oriented with 1261 respect to the single neuron axes, the neuroscientists’ act of random sampling is exactly equivalent to the 1262 mathematical procedure of a random projection. 

- 1263 To see this equivalence, consider a full-dimensional dataset denoted as the _N_ -by- _N[T]_ data matrix **X** . 1264 If we force the data to be randomly oriented by applying a random orthogonal rotation to obtain a rotated 1265 dataset, **UX** , the random sampling of its rows is mathematically equivalent to the random projection of 1266 the original data with the sampled rows of **U** as the projection’s basis. Consequently, the attractive scaling 1267 laws governing the requisite number of random projections _M_ to achieve a desired distortion _ϵ_ can be 1268 directly translated into scaling laws governing the required number of neurons to record in order to achieve a 1269 given desired accuracy of the resultant dynamic portraits of circuit computation obtained via dimensionality 1270 reduction. Of course, this equivalence comes with the caveat that neural activity patterns should be randomly 1271 oriented with respect to the single neuron axes. In such a scenario, neural activity patterns are distributed, 1272 or exhibit mixed selectivity in which many neurons code for many task parameters. A major departure from 1273 this assumption is a high degree of sparsity, and we will investigate the effects of sparsity using simulations 1274 below. 

1275 

## **V.II Numerical analysis of scaling behavior a random projection theory of measurement** 

1276 Since, as nonlinear representations of stimulus or behaviorial variables, trial-averaged neural data can be 1277 best described as nonlinear manifolds embedded in the full _N_ -dimensional firing rate space of all neurons 1278 in the circuit, we verify the scaling laws of the random projection of smooth manifolds in this section using 1279 simulations. We further aim to make the proportionality constants concrete in the sufficient condition for 1280 accurate recovery, 

**==> picture [305 x 22] intentionally omitted <==**

1281 where we replaced the manifold volume, _V_ , with NTC, since they are scaled versions of each other. Because 

1282 NTC scales exponentially with the intrinsic dimensionality, _K_ , this sufficient target dimension _M_ is still 1283 linearly proportional to _K_ . 

- 1283 

1284 We first check the scaling against log NTC using simulated data from one- and two-dimensional smooth 1285 manifolds generated using Gaussian processes. With the kernel’s characteristic time scale fixed at, _τ_ = 12, 1286 the NTCs for the 1D and the 2D cases are simply ~~�~~ _π_ 2 _Tτ_[and] _π_[2] _Tτ_[2][2][(the 2D Gaussian process has a factored] 1287 kernel), where _T_ is the range of the task parameters. In both cases, we embedded the generated random 1288 manifold in a 1,000-dimensional space, and computed the maximal pairwise distortions, max _t_ 1 _,_ 2 _dt_ 1 _,_ 2, for 1289 all possible pairwise distances under random projections of different _M_ s and of different NTCs (by varying 1290 _T_ from 4 to 100). For each combinations of _M_ and NTC, we computed the maximal distortion over 100 1291 trials, and used the 95 percentile ( _ρ_ = 0 _._ 05) of all the maximal distortions as the value for _ϵ_ . 

1292 With the distortion, _ϵ_ , plotted in the _M_ -vs-log NTC plane, we highlighted values of _M_ for three different 1293 distortion levels, _ϵ_ = 0 _._ 2 _,_ 0 _._ 3 _,_ 0 _._ 4, at different NTCs, and obtained excellent linear fits of the corresponding 1294 constant-distortion contours as predicted (Supplementary Fig. 12A). Furthermore, with a renormalization of 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

**==> picture [318 x 205] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Scaling with NTC C Scaling with N<br>ε = 0.2 ε = 0.3 ε = 0.4<br>200 K=1 200 K=2 ≥0.5 0.4<br>0.3<br>100 100 0.3<br>0.2<br>M=50, 100, 150<br>0.1 K=1<br>K=2<br>4 4 ≤ 0.1<br>-0.2 0.8 -0.4 1.6 2 3 4 5<br>log10(NTC) log10(NTC) log10(N)<br>B Renormalization Fit D Renormalization at Large N<br>6 5<br>ԑ = 0.2<br>   K = 1 4<br>4    K = 2<br>ԑ = 0.3 3<br>   K = 1 K=1<br>   K = 2 2<br>2 ԑ = 0.4 K=2<br>   K = 1 1<br>   K = 2<br>0 0<br>0 1.4 40 80 120 160<br>log10(NTC) / K M<br>M<br>Distortion (ε)<br>2 / KM × ԑ 2 - log NTC) / K(M ɛ<br>**----- End of picture text -----**<br>


**Supplementary Figure** 12: Random projections of simulated smooth manifold. **A** . Simulated distortions, _ϵ_ with _ρ_ = 0 _._ 05, of smooth random manifolds generated using 1D and 2D (factored kernel) Gaussian processes. Distortions are plotted in the plane of the number of recorded neuron, _M_ , versus the logarithm of the NTC. Locations of exemplar distortions, _ϵ_ = 0 _._ 2 _,_ 0 _._ 3 _,_ 0 _._ 4 are highlighted and fitted with linear functions of log NTC. **B** . Fitted constant-distortion contours on rescaled x and y axes to extract the parameter _c_ 1. **C** . Distortion’s saturation as a function of the embedding dimension, _N_ , for 1D and 2D manifolds with _M_ = 50 _,_ 100 _,_ 150. **D** . Offset and rescaled distortions as a function of _M_ in the limit of large _N_ = 100 _,_ 000. 

1295 the highlighted _M_ values by _K/ϵ_[2] , the fitted linear functions of log NTC _/K_ under different parameter com1296 binations have similar slopes, or _c_ 1 (Supplementary Fig. 12B). Indeed, the slopes fitted using 1D manifolds 1297 have an average of 1 _._ 07 _±_ 0 _._ 07, which is within the region of uncertainty for the average slopes fitted using 1298 2D manifolds, 1 _._ 05 _±_ 0 _._ 11. 1299 Next, we check the scaling of _M_ with the dimension of the embedding space, _N_ . Since simulations be1300 come very expensive for high embedding dimensions, we compute the distortions under just three values of 1301 _M_ = 50 _,_ 100 _,_ 150 for embedding dimensions ranging logarithmically from 200 to 100,000 (Supplementary 1302 Fig. 12C). While the simulated distortions seem to increase linearly with log _N_ initially, as the embedding 1303 dimension becomes large ( _N ∼_ 10 _,_ 000), the distortion _ϵ_ derived from simulations saturate to a constant 1304 in each case. While seemingly contradictory, the theory isn’t falsified since it provides only a _sufficient_ 1305 condition on the scaling of _M_ , and would be consistent with any scaling that is better than log _N_ (Eq 27). 1306 So what happens at large _N_ ? Can we tighten the published sufficient condition to better describe our 1307 simulations of the random projection of smooth manifolds? Given our observation of the saturating behavior, 1308 a simple modification of the scaling law is to simple replace the log _N_ term with a constant, which we 1309 combine with _c_ 3 to obtain the following simplified scaling law, 

**==> picture [272 x 22] intentionally omitted <==**

1310 In this new formula, we have also replaced the _c_ 1 term with our fitted value of 1. Given this hypothetical 1311 relation, the constant _c_ 0 must then equal to _K_ 1 � _ϵ_[2] _M −_ log NTC� for large _N_ . To check its validity, we 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1312 simulated additional 1D and 2D manifolds in 100,000-dimensional embedding spaces with values of _M_ 1313 varies more densely from 10 to 150 (Supplementary Fig. 12D). Remarkably, for combinations of different 1314 _M_ and _K_ values, the resulting values of _c_ 0 remain extremely steady around a value of 3 _._ 5 _±_ 0 _._ 2, consistent 1315 with our simplified scaling law. 

## 1316 **V.III Scaling of distortion with neural sparsity** 

1317 While random projection and random sampling are mathematically equivalent when the neural activities are 1318 randomly oriented with respect to the neuronal axes, actual neural data may be more sparse and preferentially 1319 oriented along the neuronal axes. To quantify how distributed or sparse a set of _M_ -dimensional population 1320 activities are, we use a measure called data coherence, which, for the _M_ -by- _N[T]_ data matrix **X** , is defined 1321 as, 

**==> picture [250 x 25] intentionally omitted <==**

1322 where **X** _∗t_ denotes the _t_ th column vector of the data matrix. Algebraically, the data coherence measure 1323 averages the individual column vectors’ sparsity, which is defined as the ratio of the vector’s coordinate with 1324 the maximal magnitude to its norm. Conceptually, the data coherence measure quantifies a dataset’s sparsity 1325 by computing its mutual coherence–a concept widely utilized in the compressive sensing literature–with 1326 respect to the neuronal basis. Numerically, this measure of sparsity varies from 1 for a perfectly sparse 1327 dataset, where only a single neuron is active in any recorded population activity pattern, to 1 _/√M_ for a 1328 distributed dataset, where components of the population activity are evenly distributed across neurons. The 1329 chance level coherence of a zero mean unit variance random gaussian dataset is roughly _[√]_ 2 log _M_ , which 1330 is the expected maximum for the absolute values of _M_ zero mean unit-variance gaussian random variables. 1331 Note that for the same underlying network size, _N_ , the data coherence measure may change depending on 1332 the number of recorded neurons. 

1332 

1333 To investigate how sparsity affects the number of required neurons for the accurate recovery of dynami1334 cal portraits under subsampling, we use simulations of nonlinear neural networks whose activities patterns’ 1335 sparsity can be controlled. The simulated recurrent nonlinear neural networks evolve according to the fol1336 lowing differential equation, 

**==> picture [277 x 22] intentionally omitted <==**

1337 where the state of the _N_ neurons in the network at time _t_ is represented by the vector **x** _t_ . Neuronal dynamics 1338 is modeled using the soft-thresholding nonlinearity, 

**==> picture [98 x 13] intentionally omitted <==**

and produces outputs which are then fed through the connectivity matrix **W** with some gain factor _g_ into the rest of the network. The network is driven by random _N_ -dimensional pink noise, _**η** t_ , smoothed with a gaussian kernel of a width of 5ms. For the network dynamics to dominate the neuronal dynamics, we fix _g_ at 0.99 for our simulations. To control the sparsity of the simulated activities, we manipulate the sparsity of the connectivity matrix using the following formula, 

**==> picture [110 x 12] intentionally omitted <==**

1339 where the product of _V_ Λ _V[†]_ is the eigen-decomposition of a randomly generated orthogonal matrix obtained 

1340 from applying the Gram-Schmidt procedure to a random gaussian matrix. The parameter _α_ corresponds to 

1341 an element-wise exponentiation of the decomposition’s eigenvalues, which are pure imaginary numbers. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1342 As _α_ varies from 0 to 1, _W_ transitions smoothly from the sparse identity matrix to a distributed random 1343 orthogonal matrix, generating neural activity patterns of varying sparsity. 

**==> picture [122 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
N = 109<br>0.5 N = 738<br>N = 5000<br>chance<br>0.3<br>10 [-2] α 10 [0]<br>(M = 109)<br>Data Coherence<br>**----- End of picture text -----**<br>


**Supplementary Figure** 13: Relation between the parameter _α_ and the resulting data coherence measured with a subset of 109 neurons for different network sizes. 

1344 We empirically mapped the relation between the parameter _α_ to the simulated activities’ data coherence 1345 with networks of different sizes 109, 738, and 5000 run with values _α_ varied logarithmically from 0.01 1346 to 1 (Supplementary Fig. 13). When measured with a fixed 109 number of neurons (same as monkey H), 1347 the measured coherences of samples activities depended only on the parameter _α_ but not the network size, 1348 suggesting that modifying the value of _α_ is a controlled way of exploring data coherence without affecting 1349 other properties of the simulated neural activity patterns. For the rest of this section, we compare random 1350 samplings of simulated activities with coherences of either 0.27 or 0.55 inclusive of observed coherence in 1351 data (0.34 for monkey H and 0.43 for monkey G). 1352 Applying both random samplings and random projections to the simulated dataset, we explored their 1353 resulting distortions in the _M_ -by-log _T_ plane, and fitted to them constant distortion contours of the same 1354 three levels (Figure 4B,C). The excellent linear fits of _M_ against log _T_ across data coherences for both 1355 random projections and random sampling reaffirms that the logarithmic scaling of the requisite number of 1356 neurons is a robust phenomenon that persists across a large range of sparsity levels of neural activity patterns. 1357 Furthermore, comparing results in the case where simulated neural activity patterns are randomly dis1358 tributed (data coherence = 0.27, leftmost panels, Figure 4A,B,C,D), we see no difference between the req1359 uisite number of neurons for random sampling and the requisite subspace dimension for random projection, 1360 verifying the intuitive connection we’ve made between the two for randomly oriented activity patterns. The 1361 increase in the number of requisite neurons relative to the number of random projections only starts to ap1362 pear as simulated neural activity patterns become more sparse, in agreement with the small discrepancy 1363 observed in the motor cortical data (Figure 3H) where neural activities have less-than-random orientations 1364 with respect to the neuronal axes as reflected by their higher data coherence (0 _._ 32 _>_ 0 _._ 27). 1365 More quantitatively, we compared, for the distortion value of 0.3, the slopes (increase in the requisite 1366 number of neurons or random subspace dimension for every 10-fold increase in volume) and intercepts 1367 (the minimal number of neuron or subspace dimension) of the _M_ versus log _T_ fits as functions of data 1368 coherence for random sampling and random projection. We see that the slopes and intercepts in the case of 1369 random sampling increased systematically with data coherence, or sparsity, reflecting the increased chance 1370 of missing “important” neurons as trajectories become sparser (Figures 3A,B). However, at data coherence 1371 levels around the value observed in our motor cortical dataset, the increases in both the fitted slope and 1372 intercept are quite small, suggesting that the motor cortical data are not far from being randomly oriented. 1373 On the other hand, because random projection always results in subspaces that are, by definition, randomly 1374 oriented with respect to any chosen basis of the firing-rate space, neither the fitted slopes nor the intercepts 1375 have a dependency on the simulated activities’ data coherence. This behavior is consistent with the fact that 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

**==> picture [456 x 377] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Simulated Neural Activities<br>Distributed as random Increasing Sparsity<br>α: 0.65, coh: 0.27 α: 0.34, coh: 0.32 α: 0.17, coh: 0.40 α: 0.04, coh: 0.49<br>1<br>0<br>Time Time Time Time<br>B Distortion under Random Projections E Effects of Sparsity on<br>ε = 0.2 ε = 0.3 ε = 0.4 Distortion Scaling<br>≥0.5 rand proj<br>R [2]  = 0.98, 0.99, 0.98 R [2]  = 0.98, 0.95, 0.99 R [2]  = 0.98, 0.99, 0.99 R [2]  = 0.99, 0.99, 0.96 rand samp<br>80 80 80 80<br>30<br>0.3<br>20 20 20 20 20<br>≤ 0.1<br>10 100 10 100 10 100 10 100<br>T (log scale) T (log scale) T (log scale) T (log scale) 0.25 Data Coherence 0.50<br>C Distortion under Random Samplings<br>R [2]  = 0.99, 0.98, 0.99 R [2]  = 0.98, 0.98, 0.97 R [2]  = 0.97, 0.95, 0.95 R [2]  = 0.88, 0.95, 0.98 ≥0.5<br>30<br>80 80 80 80<br>0.3<br>10<br>20 20 20 20<br>≤ 0.1<br>10 100 10 100 10 100 10 100 0.25 0.50<br>T (log scale) T (log scale) T (log scale) T (log scale) Data Coherence<br>D RP and RS Comparison<br>80 80 80 80<br>20 20 20 20<br>20 80 20 80 20 80 20 80<br>Rand Proj M Rand Proj M Rand Proj M Rand Proj M<br>Neuron Index<br>M Slope<br>M<br>Intercept<br>Rand Samp M<br>**----- End of picture text -----**<br>


Figure 14: **Effect of sparsity A** . Example firing rates of simulated networks with different levels of sparsity; **B** . Constant distortion contours for the simulated activities under random projection; **C** . Constant distortion contours for simulated activities under random sampling; **D** . Comparisons of the requisite number of neurons under random projections and random samplings. **E** . Fitted slopes and intercepts of constant distortion contours as functions of data coherence. Error bars correspond to standard errors of the fitted parameters. 

1376 properties other than sparsity are well controlled in our simulations. 1377 Overall, analysis of simulated data suggests that the optimistic result that the number of recorded neu1378 rons need only scale logarthmically with the neural task complexity to achieve a fixed distortion in neural 1379 state space dynamics, holds true for a broad range of sparsities of neural activity patterns. The actual req1380 uisite number of neurons grows with increasing sparsity, but the linear relation between _M_ and log NTC 1381 is preserved. While we support this conclusion using simulation results, it is a highly plausible theoretical 1382 conjecture as well. In fact, recent theoretical progress has been made to extend the basic JL lemma beyond 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1383 random projections into cases where the projection vectors are sparse [Achlioptas, 2003, Li et al., 2006], 1384 including random sampling. 

## 1385 

## **References** 

- 1386 [Achlioptas, 2003] Achlioptas, D. (2003). Database-friendly random projections: Johnson-Lindenstrauss 1387 with binary coins. _Journal of Computer and System Sciences_ , 66(4). 

- 1388 [Assisi et al., 2007] Assisi, C., Stopfer, M., Laurent, G., and Bazhenov, M. (2007). Adaptive regulation of 1389 sparseness by feedforward inhibition. _Nature neuroscience_ , 10(9):1176–1184. 

- 1390 [Baraniuk and Wakin, 2007] Baraniuk, R. G. and Wakin, M. B. (2007). Random projections of smooth 1391 manifolds. _Foundations of Computational Mathematics_ , 9. 

- 1392 [Bathellier et al., 2008] Bathellier, B., Buhl, D. L., Accolla, R., and Carleton, A. (2008). Dynamic ensemble 1393 odor coding in the mammalian olfactory bulb: sensory information at different timescales. _Neuron_ , 1394 57(4):586–598. 

- 1395 [Briggman et al., 2006] Briggman, K. L., Abarbanel, H. D., and Kristan, W. B. (2006). From crawling 1396 to cognition: analyzing the dynamical interactions among populations of neurons. _Current opinion in_ 1397 _neurobiology_ , 16(2):135–144. 

- 1398 [Bromberg-Martin et al., 2010] Bromberg-Martin, E. S., Hikosaka, O., and Nakamura, K. (2010). Coding 1399 of task reward value in the dorsal raphe nucleus. _The Journal of neuroscience : the official journal of the_ 1400 _Society for Neuroscience_ , 30(18):6262–6272. 

- 1401 [Chapin and Nicolelis, 1999] Chapin, J. and Nicolelis, M. (1999). Principal component analysis of neu1402 ronal ensemble activity reveals multidimensional somatosensory representations. _Journal of neuroscience_ 1403 _methods_ , 94(1):121–140. 

- 1404 [Churchland et al., 2012] Churchland, M. M., Cunningham, J. P., Kaufman, M. T., Foster, J. D., Nuyu1405 jukian, P., Ryu, S. I., and Shenoy, K. V. (2012). Neural population dynamics during reaching. _Nature_ , 1406 487(7405):51–56. 

- 1407 [Clarkson, 2008] Clarkson, K. L. (2008). Tighter bounds for random projections of manifolds. In _Proceed-_ 1408 _ings of the Twenty-fourth Annual Symposium on Computational Geometry_ , SCG ’08, pages 39–48, New 1409 York, NY, USA. ACM. 

- 1410 [Cunningham and Yu, 2014] Cunningham, J. P. and Yu, B. M. (2014). Dimensionality reduction for large1411 scale neural recordings. _Nature neuroscience_ . 

- 1412 [Dasgupta and Gupta, 2003] Dasgupta, S. and Gupta, A. (2003). An elementary proof of a theorem of 1413 johnson and lindenstrauss. _Random Structures and Algorithms_ , 22. 

- 1414 [Ganguli et al., 2008a] Ganguli, S., Bisley, J., Roitman, J., Shadlen, M., Goldberg, M., and Miller, K. 1415 (2008a). One-dimensional dynamics of attention and decision making in lip. _Neuron_ , 58(1):15–25. 

- 1416 [Ganguli et al., 2008b] Ganguli, S., Huh, D., and Sompolinsky, H. (2008b). Memory traces in dynamical 1417 systems. _Proc. Natl. Acad. Sci._ , 105(48):18970. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

1418 [Gao and Ganguli, 2015] Gao, P. and Ganguli, S. (2015). On simplicity and complexity in the brave new 1419 world of large-scale neuroscience. _Current opinion in neurobiology_ , 32:148–155. 

- 1420 [Gray, 1972] Gray, R. (1972). On the asymptotic eigenvalue distribution of toeplitz matrices. _IEEE Trans-_ 1421 _actions on Information Theory_ , 18. 

- 1422 [Haddad et al., 2010] Haddad, R., Weiss, T., Khan, R., Nadler, B., Mandairon, N., Bensafi, M., Schneidman, 1423 E., and Sobel, N. (2010). Global features of neural activity in the olfactory system form a parallel code 1424 that predicts olfactory behavior and perception. _The Journal of neuroscience : the official journal of the_ 1425 _Society for Neuroscience_ , 30(27):9017–9026. 

- 1426 [Hegd´e and Van Essen, 2004] Hegd´e, J. and Van Essen, D. C. (2004). Temporal dynamics of shape analysis 1427 in macaque visual area v2. _Journal of neurophysiology_ , 92(5):3030–3042. 

- 1428 [Hubel and Wiesel, 1959] Hubel, D. H. and Wiesel, T. N. (1959). Receptive fields of single neurones in the 1429 cat’s striate cortex. _The Journal of physiology_ , 148(3):574–591. 

- 1430 [Indyk and Motwani, 1998] Indyk, P. and Motwani, R. (1998). Approximate nearest neighbors: towards 1431 removing the curse of dimensionality. 

- 1432 [Johnson and Lindenstrauss, 1984] Johnson, W. and Lindenstrauss, J. (1984). Extensions of lipschitz maps 1433 into a hilbert space. _Contemporary Mathematics_ , 26:189–206. 

- 1434 [Kim et al., 2012] Kim, S. M., Ganguli, S., and Frank, L. M. (2012). Spatial information outflow from the 1435 hippocampal circuit: distributed spatial coding and phase precession in the subiculum. _The Journal of_ 1436 _neuroscience_ , 32(34):11539–11558. 

- 1437 [Li et al., 2006] Li, P., Hastie, T. J., and Church, K. W. (2006). Very sparse random projections. In _Pro-_ 1438 _ceedings of the 12th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining_ , 1439 KDD ’06, pages 287–296, New York, NY, USA. ACM. 

- 1440 [Machens et al., 2010] Machens, C. K., Romo, R., and Brody, C. D. (2010). Functional, but not anatomical, 1441 separation of ”what” and ”when” in prefrontal cortex. _The Journal of neuroscience : the official journal_ 1442 _of the Society for Neuroscience_ , 30(1):350–360. 

- 1443 [Mante et al., 2013] Mante, V., Sussillo, D., Shenoy, K. V., and Newsome, W. T. (2013). Context-dependent 1444 computation by recurrent dynamics in prefrontal cortex. _Nature_ . 

- 1445 [Marchenko and Pastur, 1967] Marchenko, V. and Pastur, L. (1967). Distribution of eigenvalues for some 1446 sets of random matrices. _Matematicheskii Sbornik_ , 114(4):507–536. 

- 1447 [Matsumoto et al., 2005] Matsumoto, N., Okada, M., Yasuko, S., Yamane, S., and Kawano, K. (2005). 1448 Population dynamics of face-responsive neurons in the inferior temporal cortex. _Cerebral cortex (New_ 1449 _York, N.Y. : 1991)_ , 15(8):1103–1112. 

- 1450 [Mazor and Laurent, 2005] Mazor, O. and Laurent, G. (2005). Transient dynamics versus fixed points in 1451 odor representations by locust antennal lobe projection neurons. _Neuron_ , 48(4):661–673. 

- 1452 [Moreno-Bote et al., 2014] Moreno-Bote, R., Beck, J., Kanitscheider, I., Pitkow, X., Latham, P., and Pouget, 1453 A. (2014). Information-limiting correlations. _Nature neuroscience_ . 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 1454 [Narayanan and Laubach, 2009] Narayanan, N. S. and Laubach, M. (2009). Delay activity in rodent frontal 1455 cortex during a simple reaction time task. _Journal of neurophysiology_ , 101(6):2859–2871. 

- 1456 [Paz et al., 2005] Paz, R., Natan, C., Boraud, T., Bergman, H., and Vaadia, E. (2005). Emerging patterns 1457 of neuronal responses in supplementary and primary motor areas during sensorimotor adaptation. _The_ 1458 _Journal of neuroscience : the official journal of the Society for Neuroscience_ , 25(47):10941–10951. 

- 1459 [Peyrache et al., 2009] Peyrache, A., Khamassi, M., Benchenane, K., Wiener, S. I., and Battaglia, F. P. 1460 (2009). Replay of rule-learning related neural patterns in the prefrontal cortex during sleep. _Nature_ 1461 _neuroscience_ , 12(7):919–926. 

- 1462 [Raman et al., 2010] Raman, B., Joseph, J., Tang, J., and Stopfer, M. (2010). Temporally diverse firing 1463 patterns in olfactory receptor neurons underlie spatiotemporal neural codes for odors. _The Journal of_ 1464 _neuroscience : the official journal of the Society for Neuroscience_ , 30(6):1994–2006. 

- 1465 [Raposo et al., 2014] Raposo, D., Kaufman, M. T., and Churchland, A. K. (2014). A category-free neural 1466 population supports evolving demands during decision-making. _Nature neuroscience_ . 

- 1467 [Reike et al., 1996] Reike, F., Warland, D., van Steveninck, R., and Bialek, W. (1996). _Spikes: Exploring_ 1468 _the Neural Code_ . MIT Press. 

- 1469 [Rigotti et al., 2013] Rigotti, M., Barak, O., Warden, M. R., Wang, X. J., Daw, N. D., Miller, E. K., and Fusi, 1470 S. (2013). The importance of mixed selectivity in complex cognitive tasks. _Nature_ , 497(7451):585–590. 

- 1471 [Sadtler et al., 2014] Sadtler, P. T., Quick, K. M., Golub, M. D., Chase, S. M., Ryu, S. I., Tyler-Kabara, 1472 E. C., Byron, M. Y., and Batista, A. P. (2014). Neural constraints on learning. _Nature_ , 512(7515):423– 1473 426. 

- 1474 [Sasaki et al., 2007] Sasaki, T., Matsuki, N., and Ikegaya, Y. (2007). Metastability of active CA3 networks. 1475 _The Journal of neuroscience : the official journal of the Society for Neuroscience_ , 27(3):517–528. 

- 1476 [Shepherd, 2004] Shepherd, G. M. (2004). _The synaptic organization of the brain_ , volume 3. Oxford 1477 University Press New York. 

- 1478 [Stevenson and Kording, 2011] Stevenson, I. H. and Kording, K. P. (2011). How advances in neural record1479 ing affect data analysis. _Nature neuroscience_ , 14(2):139–142. 

- 1480 [Stopfer et al., 2003] Stopfer, M., Jayaraman, V., and Laurent, G. (2003). Intensity versus identity coding 1481 in an olfactory system. _Neuron_ , 39(6):991–991004. 

- 1482 [Strang and Aarikka, 1986] Strang, G. and Aarikka, K. (1986). _Introduction to applied mathematics_ , vol1483 ume 16. Wellesley-Cambridge Press Wellesley, MA. 

- 1484 [Strong et al., 1998] Strong, S. P., Koberle, R., van Steveninck, R. R. d. R., and Bialek, W. (1998). Entropy 1485 and information in neural spike trains. _Physical review letters_ , 80(1):197. 

- 1486 [Sussillo and Abbott, 2012] Sussillo, D. and Abbott, L. (2012). Transferring learning from external to in1487 ternal weights in echo-state networks with sparse connectivity. 

- 1488 [Thacker and Bromiley, 2001] Thacker, N. A. and Bromiley, P. A. (2001). The effects of a square root 1489 transform on a poisson distributed quantity. _Tina memo_ , 10. 

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

- 1490 [Valiant, 2005] Valiant, L. G. (2005). Memorization and association on a realistic neural model. _Neural_ 1491 _computation_ , 17(3):527–555. 

- 1492 [Warden and Miller, 2010] Warden, M. R. and Miller, E. K. (2010). Task-dependent changes in short-term 1493 memory in the prefrontal cortex. _The Journal of neuroscience : the official journal of the Society for_ 1494 _Neuroscience_ , 30(47):15801–15810. 

1495 [Yu et al., 2007] Yu, B. M., Kemere, C., Santhanam, G., Afshar, A., Ryu, S. I., Meng, T. H., Sahani, M., 1496 and Shenoy, K. V. (2007). Mixture of trajectory models for neural decoding of goal-directed movements. 1497 _Journal of neurophysiology_ , 97(5):3763–3780. 

## 1498 

## **Appendix** 

1499 

## **Analytical expressions for fraction of variance explained** 

For the exponential correlation function, _f_[ˆ] ( _ω_ ) evaluates to, 

**==> picture [139 x 62] intentionally omitted <==**

Taking advantage of _f_[ˆ] ( _ω_ )’s ordering, we evaluate the integral, 

**==> picture [176 x 26] intentionally omitted <==**

The minimum _ω[∗]_ given the fraction parameter _r_ is then, 

**==> picture [162 x 19] intentionally omitted <==**

With the _τ ≫_ 1, we ignore terms beyond _O_ (1 _/τ_ ) to obtain the clean, final expression, 

**==> picture [303 x 46] intentionally omitted <==**

For the gaussian temporal correlation function, we state without showing that the Fourier transform is in fact nicely ordered. To compute the fraction of variance explained, we switch the order of the summation over _t_ and the integration of _ω_ to obtain, 

**==> picture [350 x 79] intentionally omitted <==**

bioRxiv preprint first posted online Nov. 5, 2017; doi: http://dx.doi.org/10.1101/214262. The copyright holder for this preprint (which was not peer-reviewed) is the author/funder. It is made available under a CC-BY-NC-ND 4.0 International license. 

With the optimal _ω[∗] ≈_ 2 inverf( _r_ ) _/τ_ , we then have the final expression, 

_T D_ ( _r_ ) _≈_ inverf( _r_ )[2] _π τ_ 

