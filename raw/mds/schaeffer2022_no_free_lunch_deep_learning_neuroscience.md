bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1 No Free Lunch from Deep Learning in Neuroscience: 2 A Case Study through Models of the Entorhinal-Hippocampal 3 Circuit 

4 

5 6 7 8 

Rylan Schaeffer[1,2] , Mikail Khona[2] , and Ila Rani Fiete[2,3] 

> 1Computer Science, Stanford University 

> 2Brain and Cognitive Sciences, Massachusetts Institute of Technology 

> 3Physics, Massachusetts Institute of Technology 

> 4McGovern Institute for Brain Research 

9 

August 7, 2022 

10 

## **Abstract** 

11 Research in Neuroscience, as in many scientific disciplines, is undergoing a renaissance based on deep 12 learning. Unique to Neuroscience, deep learning models can be used not only as a tool but interpreted as 13 models of the brain. The central claims of recent deep learning-based models of brain circuits are that 14 they make novel predictions about neural phenomena or shed light on the fundamental functions being 15 optimized. We show, through the case-study of grid cells in the entorhinal-hippocampal circuit, that 16 one may get neither. We begin by reviewing the principles of grid cell mechanism and function obtained 17 from first-principles modeling efforts, then rigorously examine the claims of deep learning models of grid 18 cells. Using large-scale hyperparameter sweeps and theory-driven experimentation, we demonstrate that 19 the results of such models may be more strongly driven by particular, non-fundamental, and post-hoc 20 implementation choices than fundamental truths about neural circuits or the loss function(s) they might 21 optimize. We discuss why these models cannot be expected to produce accurate models of the brain 22 without the addition of substantial amounts of inductive bias, an informal No Free Lunch result for 23 Neuroscience. Based on first principles work, we provide hypotheses for what additional loss functions 24 will produce grid cells more robustly. In conclusion, caution and consideration, together with biological 25 knowledge, are warranted in building and interpreting deep learning models in Neuroscience. 

## 26 

## **Introduction** 

27 Over the past decade, deep learning (DL) has underpinned nearly every success story in machine learning, 28 e.g., [43, 4] and increasingly many advances in fundamental science research, e.g., [26]. In neuroscience, deep 29 learning is similarly gaining widespread adoption as a useful method for behavioral and neural data analysis 30 [40, 38, 21, 32, 30, 35]. 

31 But DL offers a unique contribution to neuroscience that goes beyond its role in other fields, in that 32 deep networks can be viewed as models of the brain. The success of DL in matching or surpassing human 33 performance means it is now possible to construct models of circuits that may underlie human intelligence. As 34 a recent review wrote, “researchers are excited by the possibility that deep neural networks may offer theories 35 of perception, cognition and action for biological brains. This approach has the potential to radically reshape 36 our approach to understanding neural systems" [41]. Further, DL is a democratizing force for building neural 37 circuit models of complex function. 

38 The essential claims (and promises) of DL-based models of the brain are that 1) Because the models are 39 trained on a specific optimization problem, if the resulting representations match what has been observed in 40 the brain, then they reveal which optimization problem(s) the brain is solving, or 2) These models, when 41 trained on sensible optimization problems, should generate novel predictions about the brain’s representations 42 and behavior. 

43 However, given the nascent nature of such approaches and the excitement accompanying some claims, 44 we should examine them carefully. In DL and deep reinforcement learning, some successes attributed to 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [463 x 88] intentionally omitted <==**

**----- Start of picture text -----**<br>
a   spatial readout  b start decoded pathtrue path c Path integrationGrid cells d Place cell targetsPath Integration<br>velocity  encoding Place cells with single fields<br> inputs supervised       & homogenous scale<br>Difference of Gaussian<br>v   learning       tuning curves<br>v Narrow range of<br>  scale values<br>end<br>2.2 m<br>**----- End of picture text -----**<br>


Figure 1: (a-b) Schematic of approach of training recurrent networks to predict (different possible encodings of) 2D position from 2D velocity, in a supervised manner. (b-c) Grid cells are shown to emerge in recent DL papers as a consequence of optimizing a path integration objective [12, 2, 45, 53, 36], with the suggestion that path integration implies grid cells. (d) In the current work, we show how most ANNs trained to path integrate can do so, but only a very small set of output encoding functions (vanishingly small in the function space) and very small fraction of hyperparameter space yields grid cells, leading to the conclusion that grid cell emergence results in ANNs are post hoc: they result from tuning hyperparameters to bake grid cells into networks. 

45 novel algorithms have been shown to instead stem from seemingly minor or unstated implementation choices 46 [51, 15, 25]. In this paper, we ask whether Neuroscientists should similarly be cautious that DL-based models 47 of neural circuits that make specific claims about revealing the brain’s optimizaton functions or that predict 48 specific neural tuning curves may tell us less about fundamental scientific truths and more about programmers’ 49 particular implementation choices, and might as a result be more post hoc than predictive. 

- 49 

50 To explore these questions and point toward a systematic and circumspect use of DL for Neuroscience, we 51 evaluate recent DL-based models of grid cells in the entorhinal-hippocampal circuit. The medial entorhinal 52 cortex (MEC) and hippocampus (HPC) are part of the hippocampal formation, a critical brain structure for 53 learning and memory. In a pair of Nobel-prize winning discoveries, HPC was shown to contain **place cells** [37] 54 and MEC, its cortical input, was shown to contain **grid cells** [22]. Place cells fire at one or several seemingly 55 random locations in small and large environments [39], respectively, while grid cells fire in a spatially periodic 56 pattern in all two-dimensional environments, whenever the animal is at the vertices of a hexagonal lattice [22]. 57 Over five decades, the hippocampal formation has been central to understanding how the brain organizes 58 spatial and episodic memory, for experimentalists and theorists alike, with many mysteries remaining. A 59 recent series of DL-based models of the circuit [12, 2, 45, 53, 36]) present a story that training neural circuits 60 on **path integration (PI)** (i.e., the task of estimating one’s spatial position in an environment by integrating 61 velocity estimates) results in the emergence of grid cells. 

61 

62 We use public code from prior publications to demonstrate these results are due to implementation details 63 that tell us more about those choices than they do about MEC. By leveraging theoretically-guided large-scale 64 hyperparameter exploration and hypothesis-driven experimentation, we show: 

- 64 

- 65 1. Networks trained on path integration tasks almost always learn to optimally encode position, but almost 66 never learn grid-like representations to do so. 

66 

- 67 2. The emergence of grid-like representations depends wholly on a specifically chosen encoding of the 68 supervised target, not on the task itself, and these choices may be unrealistic. 

68 

- 69 3. The chosen encoding requires many other sensitive hyperparameter choices, such that small alterations 70 result in loss of grid-like representations. 

70 

4. Grid periods and period ratios depend on hyperparameter choices and are not set by the task. 

71 

5. Multiple grid modules, a fundamental characteristic of the grid cell system, do not emerge. 

72 

73 DL produces grid cells and some attendant properties only after making many specific design choices 74 and searching hyperparameter space to obtain such representations, effectively baking grid cells into the 75 task-trained networks. **It is highly improbable that DL models of path integration would have** 76 **produced grid cells as a novel prediction from task-training, had grid cells not already been** 77 **known to exist.** Moreover, it is unclear what interpretability or understanding these models contribute, 78 beyond or even up to what has already been shown for these particular circuits. These results challenge the 79 notion that deep networks offer a free lunch for Neuroscience in terms of discovering the brain’s optimization 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

80 problems or generating novel a priori predictions about single-neuron representations, and warn that caution 81 is needed when building and interpreting such models. 

82 Our work benefited greatly from previous publications that published their code, for which the authors 83 should be commended. By building on their code, we have been able to present novel insights that we hope 84 will contribute to a clearer understanding of the potential risks and rewards of using and interpreting DL 85 models in Neuroscience. To facilitate further research, we similarly release code[1] . 

## 86 

## **Background: grid cells** 

87 Grid cells [22] are found in the medial entorhinal cortex of mammals and are tuned to represent the spatial 88 location of the animal as it traverses 2D space. Each cell fires at every vertex of a triangular lattice that tiles 89 the explored space, regardless of the speed and direction of movement through the space. As a population, grid 90 cells exhibit several striking properties that provide support for a specialized and modular circuit. Grid cells 91 form discrete modules (clusters), such that all cells within a module share a common period and orientation, 92 while different modules express discretly different spatial periods [48]. The period ratios of successive modules 93 have values in the range of 1.2-1.5. 

94 The mechanism underlying grid cells is widely supported to be through attractor dynamics: Translation95 invariant lateral connectivity within the grid cell network results in a linear Turing instability and pattern 96 formation [7, 17, 5]. These models explain how grid cells can convert velocity inputs into updated spatial 97 estimates, and make several predictions that have been confirmed in experiments, including most centrally 98 the stability of low-dimensional cell-cell relationships regardless of environment and behavioral state, that 99 define a toroidal attractor dynamics [18, 54, 50, 20, 19]. 

## 100 

## **Experimental approach** 

101 **Path integration (PI)** is the task of using self-velocity estimates to track one’s spatial position, a crucial 102 component of spatial navigation. The central message of existing DL models of grid cells is that training 103 ANNs to path integrate causes the networks to learn grid cells [12, 2, 45, 53, 36]. 104 We follow the setup used by many previous papers: a 2.2m x 2.2m arena is created, then, spatial trajectories 105 (i.e. sequences of positions and velocities) are sampled. Networks receive as inputs the initial position and 106 velocities, and are trained to output (a possible encoding of) the positions (Fig. 1ab) in a supervised manner. 107 There are multiple possible encodings of position, and as we will show, this choice is critical. Two simple 108 encodings are Cartesian [12] or polar [1]. Another encoding scheme is via bump functions in 2D space, 109 with each output assigned a single different position that tiles the space and all outputs assigned identical 110 tuning curves [2, 45, 45, 36]. This encoding has been equated with place cells, even though place fields 111 tend to be heterogeneous in size and shape [39, 13], as well as in number [39], and unlike the choice of a 112 difference-of-Gaussians (DoG) readout tuning in ANN models, do not exhibit any inhibitory surround. See 113 Appendix 1 for position encoding details. For all encodings, supervised learning is used to train the network 114 via backpropagation through time. 

115 **Spatial tuning assessments** The spatial tuning of hidden units in the networks, visualized as ratemaps, 116 is the primary method for comparison with the brain’s grid cells. To compute ratemaps, a trained network 117 is evaluated on long trajectories that cover the 2D environment, then each hidden unit’s activity is binned 118 against the true position in the environment, and counts per bin are normalized by the number of visits to 119 that bin. Ratemaps of units are compared with grid cells through the gridness score. **We are extremely** 120 **lenient with classifying a training run with particular hyperparameters a success: if even a** 121 ***single* hidden unit has a grid score above a certain threshold, we say the model possesses grid** 122 **cells.** The grid score is not perfect since cells classified by grid scores represent only an upper bound on the 123 total number of grid cells; for details, see Appendices 1 and 1. 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [423 x 238] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>c<br>Difference of Softmaxes<br>Cartesian Polar Gaussian<br>(DoS)<br>**----- End of picture text -----**<br>


Figure 2: (a) Top: Across readout encodings, almost all networks learn to optimally encode position. Bottom: Few networks display possible grid-like representations (grid score threshold = 0.8). (b) Kernel density estimates of grid scores per readout encoding. (c) Rate maps of high grid-scoring units in deep networks trained on i) Cartesian, ii) Polar, iii) Gaussian, iv) specifically selected (tuned) Difference-of-Softmaxes (DoS) readouts. i)-iii) do not learn any grid cells. (b) Only networks trained on DoS readouts display grid-like cells. Numbers above rate maps are grid scores. 

## 124 **Networks trained on path integration tasks learn to estimate position,** 125 **but rarely learn grid cells** 

## 125 

126 As [45] wrote in their section titled “Optimally encoding position yields diverse grid-like patterns,” “Why 127 do these diverse architectures, across diverse tasks (both navigation and autoencoding), all converge to a 128 grid-like solution, and what governs the lattice structure of this solution?” We demonstrate, in contrast, 129 that most networks do not converge to a grid-like solution, instead requiring very specific readout tuning 130 functions and hyperparameter choices. Grid-like representation emergence is determined by choices made by 131 the programmer that, rather than relating to the path integration objective or biologically realistic place cells, 132 is designed post hoc to produce grid cells. 

132 

133 We ran large-scale hyperparameter sweeps across common implementation choices: 1) Architectures: RNN 134 [14]; LSTM [24]; GRU [10]; UGRNN [11]; 2) Activation: Sigmoid; Tanh; ReLU; Linear; 3) Optimizers: SGD, 135 Adam [31]; RMSProp [23] 4) Supervised Targets: Cartesian; Polar; high-dimensional bump-like readout 136 population code with Gaussian [2], **Difference-of-Softmaxes (DoS)** [45, 46, 36] or Difference-of-Gaussians 137 (DoG) tuning curves. 5) Loss: mean squared error on the agent’s Cartesian position [27, 12]; geodesic distance 138 on the agent’s polar position [1]; cross entropy on a high-dimensional population of bump-like readout units 139 [2, 45, 36] 6) Miscellaneous: recurrent & readout dropout, initialization, regularization, seed. 

139 140 For networks with bump-like population readouts, we additionally swept: 1) Field width _σ_ i.e. standard def 141 deviation of the Gaussian tuning curve (often denoted _σE_ = _σ_ in the literature); 2) Whether the bump-like 142 readouts have homogeneous or heterogeneous field widths; 3) In the case of readouts with DoG or DoS 143 tuning curves, the surround scale _s_ i.e. the ratio between the inhibitory and excitatory Gaussian’s standard def 144 deviations ( _s_ = _σI /σE_ ); 4) Number of fields per readout unit. Evaluating the entire hyperparameter volume 145 is computationally prohibitive, so we evaluated a subvolume most consistent with previous papers, focusing 146 on perturbations from hyperparameters that did produce grid cells. In this sense, **our search was biased** 147 **toward configurations shown to produce grid cell emergence and thus our findings about the** 148 **fragility of these solutions conservatively favored these solutions as much as possible.** All sweeps 

> 1 `https://github.com/RylanSchaeffer/MEC-HPC-Models-Investigation` 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [448 x 111] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>**----- End of picture text -----**<br>


Figure 3: **Grid periods are hyperparameter-dependent and multiple modules do not emerge.** (a) Over a wide sweep of DoS (the most likely to produce grid cells, Fig. 2a bottom) target field widths _σE_ , the distribution of grid periods is unimodal (each color is distribution of periods obtained from 3 runs with a _σE_ value; different periods are only obtained by varying _σE_ ), meaning multiple grid modules do not emerge, in contrast to real grid cells. (b) The chosen target field width _σE_ determines the grid period mode, meaning that hand-designed hyperparameter choices, not an intrinsic emergent property, sets the grid period. (c) If we use grid periods obtained from smoothly sweeping _σE_ as a proxy for different modules, the period ratios are closer to 1 than the experimental ratios of _∼_ 1 _._ 4. 

## 149 

## are provided in Appendix 1. 

150 To evaluate whether a network learns to optimally encode its position, we measured its position decoding 151 error using previous papers’ method [2, 45, 36]: we computed position decoding error using the network’s 152 output Cartesian positions (if trained on Cartesian targets) or by decoding position from the network’s 153 outputs. Any network with error _<_ 10 cm was considered to have achieved optimal position encoding; this 154 threshold was chosen based on noise inherent in the decoding algorithm. 

155 In total, we trained _>_ 5500 networks and found that most hyperparameter configurations succeed in 156 learning to path integrate (Fig. 2a, Top), but few learn grid cell representations (Fig. 2a, Bottom). This is 157 consistent with earlier work [27, 1] demonstrating that networks can learn to path integrate and solve other 158 navigational problems (e.g. estimating which of several environments correspond to the current location) 159 without lattice cells emerging as a solution. 

## **Lattice cell emergence requires a highly specific choice of supervised target encoding** 

160 

## 161 

162 We next sought to characterize when grid cells are learnt under different encodings of the supervised target 163 i.e., 2D position. We tested multiple encodings: i) Cartesian, ii) Polar, iii) Gaussian, iv) a very specifically 164 selected, Difference-of-Gaussian (DoG/DoS) readout and more. We found that grid cells do not emerge from 165 Cartesian, Polar or Gaussian encodings (Fig. 2abc), consistent with earlier work [27]. Only by choosing a 166 DoG readout tuning curve did grid cells sometimes emerge. 

166 

**Grid periods are parameter-dependent and multiple modules do not emerge** 

167 

168 Next, a prominent feature of grid cells that is critical for their unambiguous encoding of position over 169 large scales is the existence of a discrete set of grid periodicities, which tend to scale by a rough factor of 1 _._ 4 170 between adjacent scales [48]. We asked whether ANN models generate multiple periods and when they did so, 171 what hyperparameters and other choices the formed periods depended on. 

172 To ensure we would obtain at least some grid cells, we fixed the readouts to be DoSs, and swept over 173 different scales of the DoS. We found that almost all runs had a unimodal distribution of grid periods (Fig. 174 3a), meaning the networks learnt only one module of grid cells. 

175 Further, we found that the period of the formed grid-like representation is completely determined by the 176 scale _σE_ of the externally imposed readout DoG (Fig. 3). The period of the grid-like responses in every 177 run increased monotonically with the width of the DoG readout (Fig. 3b). Since the models did not result 178 in multiple modules in a single network, we used the somewhat discrete distribution of peaks of the single 179 module formed when sweeping the DoG parameter more continuously to compute grid period ratios. These 180 period ratios from adjacent peaks led to non-biological values (Fig. 3c). 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [225 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>c<br>**----- End of picture text -----**<br>


**==> picture [188 x 91] intentionally omitted <==**

**==> picture [95 x 57] intentionally omitted <==**

**==> picture [100 x 57] intentionally omitted <==**

**==> picture [101 x 58] intentionally omitted <==**

**==> picture [100 x 57] intentionally omitted <==**

Figure 4: **Other changes to Difference-of-Softmaxes (DoS) affect the formation of grid cells:** (a) The existence of grid solutions even with DoG readout encodings is highly sensitive to parameters such as the target function receptive field width _σE_ , and small alterations result in the disappearance of grid cells regardless of grid score threshold. (b) (left) Comparison of grid scores of trained networks with DoG shows that the Difference-of-Softmaxes (DoS), as used by [45, 36, 46], is critical for high grid scores, (right) Rate maps of highest scoring units from DoG networks achieving low position decoding error. (c) Computing the Fourier transform (right of each pair) of the readout second-moment matrix (left of each pair) explains that DoS places Fourier power on an annulus with sufficiently large radius to produce grid cells, showing why the particular DoS choice is critical. 

181 **Fourier analysis of Turing instability explains the preceding empirical results** Why do only 182 Difference-of-Softmaxes (DoS) readouts produce grid cells? We restate the essence of previous analyses of 183 first-principles models [7, 29] here, and explain why they might explain our empirical findings. 

183 

184 In a recurrent network with dynamics _r_ ˙( _x_ ) = _−r_ ( _x_ ) + _g_ ( _W ⋆r_ ), where _x_ designates the neural index (in a 185 continuum approximation for neurons), _W ⋆r_ designates the total (integrated) inputs from the network to the 186 neuron at index _x_ , and _g_ is the non-linearity, if the recurrent weight interaction is translationally invariant, 187 then _W_ ( _x, x[′]_ ) = _W_ ( _x − x[′]_ ) = _W_ (∆ _x_ ). Under DoG interactions: 

187 

**==> picture [369 x 26] intentionally omitted <==**

188 where ∆ _x_ refers to the difference of indices between the neural pair linked by the weights. The evolution 189 of activity can be decomposed into the growth and decay of Fourier components of the rate vector, which is 190 fully determined by the Fourier transform of _W_ , which is given by: 

**==> picture [400 x 26] intentionally omitted <==**

191 Here _αE_ ( _αI_ ) denotes the strength and _σE_ ( _σI_ ) denotes the scale of excitation (inhibition). For linearized ˙ 192 dynamics that approximate _r_ ( _x_ ) _∼−r_ ( _x_ ) + _f_ (∆ _x_ ) _⋆r_ (i.e. _g_ has been linearized), the solution will be periodic 193 if the maxima of _f_[˜] ( _k_ ), given by [ _k[∗]_ ][2] = _σE_[2] _[−]_ 2 _[σ] I_[2][log] � _αEσE_[3] _[/α][I][σ] I_[3] �, contains sufficient power and if _k[∗]_ = 0. 194 Specifically, the condition for pattern formation is _f_[˜] ( _k[∗]_ ) _>_ 1 [8, 29]. In particular, the inhibitory surround 195 contained in _f_ (∆ _x_ ), with strength _σI_ , is key to pattern formation; if _σI →∞_ or _αI →_ 0, the maximum is at 196 the origin ( _k[∗]_ = 0), causing no pattern formation. Therefore, a Gaussian interaction cannot produce periodic 197 patterns. 

198 The connection of this theory to ANNs trained with supervised readout target _P_ was made in [45] through ˙ 199 the observation that dynamics with an MSE loss _||P − W_ readout _r||_[2] can be approximated as _r_ = _−λr_ + Σ _r_ , 200 where Σ = _PP[T]_ is the readout correlation matrix and _λ_ is a regularization parameter. This dynamics 201 now looks identical to the first dynamics with recurrent interaction matrix _W_ ( _x, x[′]_ ) = Σ _xx′_ . For identical, 202 unimodal target readout functions with DoG tuning curves, this readout correlation matrix is also a difference 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [378 x 116] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>**----- End of picture text -----**<br>


**==> picture [90 x 106] intentionally omitted <==**

Figure 5: **Adding place cell-like heterogeneity to the readouts prevents the formation of grid cells.** To maximally favor the emergence of grid representations, we selected DoS encodings with the best hyperparameters for grid cell emergence (RNN or UGRNN, ReLU, _σE_ = 0 _._ 12 cm, _s_ = 2 _._ 0, 3 seeds), then tested the effect of multiple fields per place cell ( _∼_ 1 + Pois(3 _._ 0)) and multiple scales (receptive field width _σE ∼_ Unif(0 _._ 06 _,_ 1 _._ 0) m and surround scale _s ∼_ Unif(1 _._ 25 _,_ 4 _._ 5)). (a) Networks trained on single-field single-scale DoS and multi-scale multi-field DoS (more similar to biological place cells) readouts all obtain low position decoding error. (b) Multi-scale multi-field DoS readouts do not learn grid cells. (c) Highest-scoring rate maps from multi-field multi-scale networks. 

203 of Gaussians (Appendix 1). By the same theory outlined above, Gaussian tuning curves should not produce 204 periodic patterns. 

205 **Unmentioned implementation details matter** We discovered a seemingly minor implementation detail 206 in several preceding papers [45, 46, 36] that proved important for the emergence of grid cells, that (to the 207 best of our knowledge) is unmentioned in the main texts and supplements. While these papers nominally 208 refer to a Difference-of-Gaussian (DoG) readout target function (Eqn. 1), their code instead uses a Difference209 of-Softmaxes (DoS) target function. When we trained ideal grid-forming ReLU networks on place-cell-like 210 target encodings with DoG tuning curves, sweeping the receptive field _σ_ and surround scale _s_ , DoG readouts 211 did not result in grid cells (Fig. 4b), while DoS readouts did. The preceding Fourier analysis shows why DoS 212 tuning, though still more unrealistic as a place cell model than DoG, matters (Fig. 4c). 

## 213 

## **Grid cells disappear with more biologically-realistic readout functions** 

214 Place cells, to which grid cells project, differ significantly from the highly simplified single-scale, single-field 215 ANN readouts. Place cells have heterogeneously distributed field widths, many with multiple fields [39, 13] 216 (and are not DoS-like functions). This naturally leads to the question: Will readouts targets with multiple 217 scales and multiple fields per place cell still produce grid cells? 

218 We found that networks trained with multiple-field multiple-scale bump encodings per readout unit achieve 219 comparably low position decoding error as good single-field single-scale encodings (Fig. 5a), but do not learn 220 grid cells (Fig. 5bc). This further demonstrates that accurate position encoding and integration does not 221 require grid representations. 

## 222 

## **Discussion** 

223 For research that uses deep networks as models of the brain, there is a fundamental obstacle to making the 224 claim that a given optimization problem is what the brain is solving: If we know the responses of a significant 225 fraction of units from biological networks performing a certain task, we cannot infer the loss function that the 226 brain is optimizing since in principle, numerous different loss functions can have the same/similar minima 227 (Fig. 6 top). In other words, there is typically a many-to-one mapping between loss functions and some point 228 in state space where the functions have a minimum. Some of the different grid models from deep learning 229 and first principles show that this is possible [12, 2, 45, 53, 7]. Conversely, given a reasonable optimization 230 problem that we select based on an organism’s ecological niche, we cannot infer a single solution (and thus 231 build truly predictive single-cell tuning models), since there exist several minima to that optimization problem 232 (Fig. 6 bottom). In other words, there is typically a one-to-many mapping from a loss function to its set of 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

233 solutions. To break this degeneracy of multiple minima and arrive at truly predictive models or a better 234 understanding of the brain’s optimization problems, we must acknowledge, understand, and model the specific 235 inductive biases and constraints present in the biological system we are trying to model. It is untenable to 236 expect success without doing so. This is what we refer to as an informal neural ’no-free-lunch’. In these cases, 237 these constraints and biases are as informative as other design principles, such as the loss function. 238 What can we learn from DL models about brain 239 circuits without considering and studying biological 240 inductive biases? Population-wide low-dimensional 241 latent representations and dynamics that arise as 242 necessary for solving difficult problems are possibly 243 sufficiently robust and abstracted to be predictive 244 of population dynamics in a neural circuit without 245 addition of detailed biological constraints. This can 246 explain successes of the population-level analyses of 247 the visual pathway [28, 3], as well as the population248 level low-dimensional dynamics of circuits solving 249 inference tasks [49, 42, 1, 52]. In these cases, the Figure 6: **Challenges in achieving the two central** 250 emergent solutions are fundamental features of any **claims of recent DL models of neuroscience** : Top: 251 systems that solve the task, and by construction need Building a model that replicates observed neural re252 not be specific to brains. sponses does not guarantee that the loss function used 253 Returning to grid cells, we have conclusively is the brain’s objective, as multiple objectives can share 254 shown that they do not generically arise in networks a solution. Bottom: Training a network on a plausible 255 trained to path-integrate. This raises the question loss function or even the correct loss function need not 256 of what different additional architectural, hyperpayield the solution the brain has selected because the 257 rameter, and constraint choices had to be made in loss function may have multiple minima, of which the 258 previous papers [2, 45, 46] to obtain grid-like tuning, brain selects one based on its constraints, while an ANN 259 given that they used a path integration objective selects another, based on the optimization technique 260 with Gaussian place cell targets, requirements that used. 261 are reasonable but not sufficient to obtain grid-like 262 tuning. 263 Theoretical work on grid cell representations [16, 47, 34] suggests that the following two factors are important 264 features of the grid cell code: a very large coding range and the related property of robustness/intrinsic error 265 correcting coding. Adding these properties to the loss are likely to be a more principled way to obtain grid-like 266 fields rather than by hand-designing a biologically unrealistic DoG or DoS readout. Consistent with this, 267 the very large amount of dropout or other noise required in [2, 12] suggests that the coding-theoretic insight 268 on intrinsic error-correction properties of grid cells and their related large capacity may indeed be central 269 ingredients to produce grid cells. 

Figure 6: **Challenges in achieving the two central claims of recent DL models of neuroscience** : Top: Building a model that replicates observed neural responses does not guarantee that the loss function used is the brain’s objective, as multiple objectives can share a solution. Bottom: Training a network on a plausible loss function or even the correct loss function need not yield the solution the brain has selected because the loss function may have multiple minima, of which the brain selects one based on its constraints, while an ANN selects another, based on the optimization technique used. 

270 In fact, there are a number of key properties of the grid cell code elucidated earlier by theoretical arguments, 271 including but not limited to path integration, that we hypothesize may form a sufficient and biologically 272 relevant set for the emergence of grid cells: 1) non-negative activations; 2) equivariant population responses 273 (i.e., the population response always lies on a hypersphere); 3) a path integrating (PI) code or in other 274 words, translation invariant representations [17, 7]; 4) high representational capacity [6, 47, 33]; 5) intrinsic 275 error-correcting capabilities [6, 47]; and finally, 6) uniformly distributed (whitened) and low spatial information 276 per cell, such that the total spatial information of the grid code should be equally distributed across all cells. 

277 We suggest that several of these properties (e.g. excluding the more specific property 3)) are extremely 278 general features of neural codes, and incorporating them into ANN models of neural circuits could increase 279 their ability to make de novo rather than post hoc predictions, and remove the need to use synthetic and 280 unrealistic choices with fine hyperparameter tuning (such as DOG and DOS readouts). 

281 In sum, the findings here argue that the central contribution of scientific interest when building and 282 studying ANN models of the brain that reproduce specific tuning curves is not that the model produced the 283 curves (after all, given the expressive power of deep networks, it is no surprise that training them to effectively 284 generate a given tuning will in fact succeed), but rather to explore and carefully characterize conditions and 285 constraints under which the particular tuning does and does not emerge, to consider whether the constraints 286 align with biological constraints, and to consider what principles can be extracted from them. When not 287 predicting specific tuning curves, but rather population-level response dynamics, the results are expected to 288 be more robust to specific implementational choices and thus more durable. 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 289 

## **References** 

- 290 [1] Emergence of dynamically reconfigurable hippocampal responses by learning to perform probabilistic 291 spatial reasoning. _biorxiv_ . 

- 292 [2] Andrea Banino, Caswell Barry, Benigno Uria, Charles Blundell, Timothy Lillicrap, Piotr Mirowski, 293 Alexander Pritzel, Martin J. Chadwick, Thomas Degris, Joseph Modayil, Greg Wayne, Hubert Soyer, 294 Fabio Viola, Brian Zhang, Ross Goroshin, Neil Rabinowitz, Razvan Pascanu, Charlie Beattie, Stig 295 Petersen, Amir Sadik, Stephen Gaffney, Helen King, Koray Kavukcuoglu, Demis Hassabis, Raia Hadsell, 296 and Dharshan Kumaran. Vector-based navigation using grid-like representations in artificial agents. 297 _Nature_ , 557(7705):429–433, May 2018. 

- 298 [3] Pouya Bashivan, Kohitij Kar, and James J. DiCarlo. Neural population control via deep image synthesis. 299 _Science_ , 364(6439):eaav9436, May 2019. Publisher: American Association for the Advancement of Science. 

- 300 [4] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind 301 Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, 302 Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens 303 Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack 304 Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language 305 Models are Few-Shot Learners. _arXiv:2005.14165 [cs]_ , July 2020. arXiv: 2005.14165. 

- 306 [5] Yoram Burak and Ila Fiete. Do We Understand the Emergent Dynamics of Grid Cell Activity? _Journal_ 307 _of Neuroscience_ , 26(37):9352–9354, September 2006. Publisher: Society for Neuroscience Section: Journal 308 Club. 

309 

   - [6] Yoram Burak and Ila R Fiete. Unpublished observations. 2008. 

- 310 [7] Yoram Burak and Ila R. Fiete. Accurate Path Integration in Continuous Attractor Network Models of 311 Grid Cells. _PLOS Computational Biology_ , 5(2):e1000291, February 2009. Publisher: Public Library of 312 Science. 

- 313 [8] Yoram Burak and Ila R Fiete. Accurate path integration in continuous attractor network models of grid 314 cells. _PLoS Comput Biol_ , 5(2):e1000291, Feb 2009. 

- 315 [9] Malcolm G. Campbell, Samuel A. Ocko, Caitlin S. Mallory, Isabel I. C. Low, Surya Ganguli, and Lisa M. 316 Giocomo. Principles governing the integration of landmark and self-motion cues in entorhinal cortical 317 codes for navigation. _Nature Neuroscience_ , 21(8):1096–1106, August 2018. Number: 8 Publisher: Nature 318 Publishing Group. 

- 319 [10] Junyoung Chung, Caglar Gulcehre, KyungHyun Cho, and Yoshua Bengio. Empirical Evaluation of Gated 320 Recurrent Neural Networks on Sequence Modeling. _NIPS Workshop Deep Learning and Representation_ 321 _Learning_ , December 2014. Number: arXiv:1412.3555 arXiv:1412.3555 [cs]. 

321 

- 322 [11] Jasmine Collins, Jascha Sohl-Dickstein, and David Sussillo. Capacity and Trainability in Recurrent Neural 323 Networks. _International Conference on Learning Representations_ , March 2017. Number: arXiv:1611.09913 324 arXiv:1611.09913 [cs, stat]. 

- 325 [12] Christopher J Cueva and Xue-Xin Wei. Emergence of grid-like representations by training recurrent 326 neural networks to perform spatial localization. _International Conference on Learning Representations_ , 327 page 19, 2018. 

- 328 [13] Tamir Eliav, Shir R. Maimon, Johnatan Aljadeff, Misha Tsodyks, Gily Ginosar, Liora Las, and Nachum 329 Ulanovsky. Multiscale representation of very large environments in the hippocampus of flying bats. 330 _Science_ , 372(6545):eabg4020, May 2021. Publisher: American Association for the Advancement of Science. 

- 331 [14] Jeffrey L. Elman. Finding Structure in Time. _Cognitive Science_ , 14(2):179–211, 1990. _eprint: 332 https://onlinelibrary.wiley.com/doi/pdf/10.1207/s15516709cog1402_1. 

- 333 [15] Logan Engstrom, Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry Rudolph, 334 and Aleksander Madry. Implementation Matters in Deep Policy Gradients: A Case Study on PPO and 335 TRPO. _arXiv:2005.12729 [cs, stat]_ , May 2020. arXiv: 2005.12729. 

335 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 336 [16] Ila R Fiete, Yoram Burak, and Ted Brookings. What grid cells convey about rat location. _J Neurosci_ , 337 28(27):6858–71, Jul 2008. 

- 338 [17] Mark C Fuhs and David S Touretzky. A spin glass model of path integration in rat medial entorhinal 339 cortex. _J Neurosci_ , 26(16):4266–4276, 2006. 

- 340 [18] Marianne Fyhn, Torkel Hafting, Alessandro Treves, May-Britt Moser, and Edvard I Moser. Hippocampal 341 remapping and grid realignment in entorhinal cortex. _Nature_ , 446(7132):190–194, 2007. 

- 342 [19] Richard J. Gardner, Erik Hermansen, Marius Pachitariu, Yoram Burak, Nils A. Baas, Benjamin A. Dunn, 343 May-Britt Moser, and Edvard I. Moser. Toroidal topology of population activity in grid cells. _Nature_ , 344 602(7895):123–128, February 2022. Number: 7895 Publisher: Nature Publishing Group. 

- 345 [20] Richard J. Gardner, Li Lu, Tanja Wernle, May-Britt Moser, and Edvard I. Moser. Correlation structure 346 of grid cells is preserved during sleep. _Nature Neuroscience_ , 22(4):598–608, April 2019. Number: 4 347 Publisher: Nature Publishing Group. 

- 348 [21] Joshua I. Glaser, Ari S. Benjamin, Raeed H. Chowdhury, Matthew G. Perich, Lee E. Miller, and 349 Konrad P. Kording. Machine Learning for Neural Decoding. _eNeuro_ , 7(4), July 2020. Publisher: Society 350 for Neuroscience Section: Research Article: Methods/New Tools. 

- 351 [22] Torkel Hafting, Marianne Fyhn, Sturla Molden, May-Britt Moser, and Edvard I. Moser. Microstructure 352 of a spatial map in the entorhinal cortex. _Nature_ , 436(7052):801–806, August 2005. Number: 7052 353 Publisher: Nature Publishing Group. 

354 

   - [23] Geoffrey Hinton, Nitish Srivastava, and Kevin Swersky. Lecture 6e-RMSProp. 

- 355 [24] Sepp Hochreiter and Jürgen Schmidhuber. Long Short-Term Memory. _Neural Computation_ , 9(8):1735– 356 1780, November 1997. 

- 357 [25] Andrew Ilyas, Logan Engstrom, Shibani Santurkar, Dimitris Tsipras, Firdaus Janoos, Larry Rudolph, 358 and Aleksander Madry. A Closer Look at Deep Policy Gradients. _arXiv:1811.02553 [cs, stat]_ , May 2020. 359 arXiv: 1811.02553. 

- 360 [26] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ronneberger, 361 Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, Alex Bridgland, Clemens 362 Meyer, Simon A. A. Kohl, Andrew J. Ballard, Andrew Cowie, Bernardino Romera-Paredes, Stanislav 363 Nikolov, Rishub Jain, Jonas Adler, Trevor Back, Stig Petersen, David Reiman, Ellen Clancy, Michal 364 Zielinski, Martin Steinegger, Michalina Pacholska, Tamas Berghammer, Sebastian Bodenstein, David 365 Silver, Oriol Vinyals, Andrew W. Senior, Koray Kavukcuoglu, Pushmeet Kohli, and Demis Hassabis. 366 Highly accurate protein structure prediction with AlphaFold. _Nature_ , 596(7873):583–589, August 2021. 367 Number: 7873 Publisher: Nature Publishing Group. 

- 368 [27] I. Kanitscheider and I. R. Fiete. Training recurrent networks to generate hypotheses about how the brain 369 solves hard navigation problems. _Advances in Neural Information Processing Systems (NeurIPS)_ , 2017. 

- 370 [28] Alexander J. E. Kell, Daniel L. K. Yamins, Erica N. Shook, Sam V. Norman-Haignere, and Josh H. 371 McDermott. A Task-Optimized Neural Network Replicates Human Auditory Behavior, Predicts Brain 372 Responses, and Reveals a Cortical Processing Hierarchy. _Neuron_ , 98(3):630–644.e16, May 2018. 

- 373 [29] Mikail Khona, Sarthak Chandra, and Ila R. Fiete. From smooth cortical gradients to discrete mod374 ules: spontaneous and topologically robust emergence of modularity in grid cells. _bioRxiv_ , page 375 2021.10.28.466284, January 2022. 

- 376 [30] Timothy D. Kim, Thomas Z. Luo, Jonathan W. Pillow, and Carlos D. Brody. Inferring Latent Dynamics 377 Underlying Neural Population Activity via Neural Differential Equations. In _Proceedings of the 38th_ 378 _International Conference on Machine Learning_ , pages 5551–5561. PMLR, July 2021. ISSN: 2640-3498. 

- 379 [31] Diederik P. Kingma and Jimmy Ba. Adam: A Method for Stochastic Optimization. _International_ 380 _Conference on Learning Representations_ , January 2017. Number: arXiv:1412.6980 arXiv:1412.6980 [cs]. 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 381 [32] Jesse A. Livezey, Kristofer E. Bouchard, and Edward F. Chang. Deep learning as a tool for neural 382 data analysis: Speech classification and cross-frequency coupling in human sensorimotor cortex. _PLOS_ 383 _Computational Biology_ , 15(9):e1007091, September 2019. Publisher: Public Library of Science. 

- 384 [33] A. Mathis, A. Herz, and M. Stemmler. Optimal population codes for space: grid cells outperform place 385 cells. _Neural Comp._ , 24:2280–2317, 2012. 

- 386 [34] Alexander Mathis, Andreas V. M. Herz, and Martin Stemmler. Optimal Population Codes for Space: 387 Grid Cells Outperform Place Cells. _Neural Computation_ , 24(9):2280–2317, September 2012. 

- 388 [35] Alexander Mathis, Pranav Mamidanna, Kevin M. Cury, Taiga Abe, Venkatesh N. Murthy, Macken389 zie Weygandt Mathis, and Matthias Bethge. DeepLabCut: markerless pose estimation of user-defined 390 body parts with deep learning. _Nature Neuroscience_ , 21(9):1281–1289, September 2018. Number: 9 391 Publisher: Nature Publishing Group. 

- 392 [36] Aran Nayebi, Alexander Attinger, Malcolm Campbell, Kiah Hardcastle, Isabel Low, Caitlin S Mallory, 393 Gabriel Mel, Ben Sorscher, Alex H Williams, Surya Ganguli, Lisa Giocomo, and Dan Yamins. Explaining 394 heterogeneity in medial entorhinal cortex with task-driven neural networks. In _Advances in Neural_ 395 _Information Processing Systems_ , volume 34, pages 12167–12179. Curran Associates, Inc., 2021. 

- 396 [37] J. O’Keefe and J. Dostrovsky. The hippocampus as a spatial map: Preliminary evidence from unit activity 397 in the freely-moving rat. _Brain Research_ , 34:171–175, 1971. Place: Netherlands Publisher: Elsevier 398 Science. 

- 399 [38] Talmo D. Pereira, Diego E. Aldarondo, Lindsay Willmore, Mikhail Kislin, Samuel S.-H. Wang, Mala 400 Murthy, and Joshua W. Shaevitz. Fast animal pose estimation using deep neural networks. _Nature_ 401 _Methods_ , 16(1):117–125, January 2019. Number: 1 Publisher: Nature Publishing Group. 

- 402 [39] P. D. Rich, H.-P. Liaw, and A. K. Lee. Large environments reveal the statistical structure governing 403 hippocampal representations. _Science_ , 345(6198):814–817, August 2014. 

- 404 [40] Muhammad Saif-ur Rehman, Robin Lienkämper, Yaroslav Parpaley, Jörg Wellmer, Charles Liu, Brian 405 Lee, Spencer Kellis, Richard Andersen, Ioannis Iossifidis, Tobias Glasmachers, and Christian Klaes. 406 SpikeDeeptector: a deep-learning based method for detection of neural spiking activity. _Journal of Neural_ 407 _Engineering_ , 16(5):056003, July 2019. Publisher: IOP Publishing. 

- 408 [41] Andrew Saxe, Stephanie Nelli, and Christopher Summerfield. If deep learning is the answer, what is 409 the question? _Nature Reviews Neuroscience_ , 22(1):55–67, January 2021. Number: 1 Publisher: Nature 410 Publishing Group. 

- 411 [42] Rylan Schaeffer, Mikail Khona, Leenoy Meshulam, Brain Laboratory International, and Ila Fiete. Reverse412 engineering recurrent neural network solutions to a hierarchical inference task for mice. _Advances in_ 413 _Neural Information Processing Systems_ , 33:4584–4596, 2020. 

- 414 [43] David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den Driessche, Julian 415 Schrittwieser, Ioannis Antonoglou, Veda Panneershelvam, Marc Lanctot, Sander Dieleman, Dominik 416 Grewe, John Nham, Nal Kalchbrenner, Ilya Sutskever, Timothy Lillicrap, Madeleine Leach, Koray 417 Kavukcuoglu, Thore Graepel, and Demis Hassabis. Mastering the game of Go with deep neural networks 418 and tree search. _Nature_ , 529(7587):484–489, January 2016. Number: 7587 Publisher: Nature Publishing 419 Group. 

- 420 [44] Trygve Solstad, Charlotte N. Boccara, Emilio Kropff, May-Britt Moser, and Edvard I. Moser. Represen421 tation of Geometric Borders in the Entorhinal Cortex. _Science_ , 322(5909):1865–1868, December 2008. 422 Publisher: American Association for the Advancement of Science. 

- 423 [45] Ben Sorscher, Gabriel C Mel, Surya Ganguli, and Samuel A Ocko. A unified theory for the origin of grid 424 cells through the lens of pattern formation. _Advances in Neural Information Processing Systems_ , page 18, 425 2019. 

- 426 [46] Ben Sorscher, Gabriel C. Mel, Samuel A. Ocko, Lisa Giocomo, and Surya Ganguli. A unified theory 427 for the computational and mechanistic origins of grid cells. Technical report, bioRxiv, December 2020. 428 Section: New Results Type: article. 

11 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 429 [47] Sameet Sreenivasan and Ila Fiete. Grid cells generate an analog error-correcting code for singularly 430 precise neural computation. _Nat Neurosci_ , 14(10):1330–7, Sep 2011. 

430 

- 431 [48] Hanne Stensola, Tor Stensola, Trygve Solstad, Kristian Frøland, May-Britt Moser, and Edvard I. Moser. 432 The entorhinal grid map is discretized. _Nature_ , 492(7427):72–78, December 2012. Number: 7427 Publisher: 433 Nature Publishing Group. 

- 434 [49] David Sussillo and Omri Barak. Opening the Black Box: Low-Dimensional Dynamics in High-Dimensional 435 Recurrent Neural Networks. _Neural Computation_ , 25(3):626–649, March 2013. 

- 436 [50] S.G. Trettel, J.B. Trimper, E. Hwaun, I.R. Fiete, and L.L. Colgin. Grid cell co-activity patterns during 437 sleep reflect spatial overlap of grid fields during active behaviors. _Nat Neurosci_ , 22(4):609–617, 04 2019. 

- 438 [51] George Tucker, Surya Bhupatiraju, Shixiang Gu, Richard E. Turner, Zoubin Ghahramani, and Sergey 439 Levine. The Mirage of Action-Dependent Baselines in Reinforcement Learning. _arXiv:1802.10031 [cs,_ 440 _stat]_ , November 2018. arXiv: 1802.10031. 

440 

- 441 [52] Jakob Voigts, Ingmar Kanitscheider, Nicholas J. Miller, Enrique H. S. Toloza, Jonathan P. Newman, 442 Ila R. Fiete, and Mark T. Harnett. Spatial reasoning via recurrent neural dynamics in mouse retrosplenial 443 cortex. _biorxiv_ , April 2022. 

- 444 [53] James C. R. Whittington, Timothy H. Muller, Shirley Mark, Guifen Chen, Caswell Barry, Neil Burgess, 445 and Timothy E. J. Behrens. The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory 446 through Generalization in the Hippocampal Formation. _Cell_ , 183(5):1249–1263.e23, November 2020. 

- 447 [54] K.J. Yoon, M.A. Buice, R. Barry, C.and Hayman, N. Burgess, and I.R. Fiete. Specific evidence of 448 low-dimensional continuous attractor dynamics in grid cells. _Nat Neurosci_ , 16(8):1077–84, Aug 2013. 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

449 

## **1 Checklist** 

450 

   1. For all authors... 

- 451 (a) Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions 452 and scope? 

- 453 (b) Did you describe the limitations of your work? 

- 454 (c) Did you discuss any potential negative societal impacts of your work? We do not feel our paper 455 has potential negative societal impacts. 

- 456 (d) Have you read the ethics review guidelines and ensured that your paper conforms to them? 

- 457 2. If you are including theoretical results... 

- 458 (a) Did you state the full set of assumptions of all theoretical results? 

- 459 (b) Did you include complete proofs of all theoretical results? 

- 460 3. If you ran experiments... 

- 461 (a) Did you include the code, data, and instructions needed to reproduce the main experimental results 462 (either in the supplemental material or as a URL)? 

- 463 (b) Did you specify all the training details (e.g., data splits, hyperparameters, how they were chosen)? 

- 464 (c) Did you report error bars (e.g., with respect to the random seed after running experiments multiple 465 times)? 

- 466 (d) Did you include the total amount of compute and the type of resources used (e.g., type of GPUs, 467 internal cluster, or cloud provider)? We haven’t yet had time to collect this information, but we 468 will add this information to the final version if accepted. 

- 469 4. If you are using existing assets (e.g., code, data, models) or curating/releasing new assets... 

- 470 (a) If your work uses existing assets, did you cite the creators? 

- 471 (b) Did you mention the license of the assets? 

- 472 (c) Did you include any new assets either in the supplemental material or as a URL? 

- 473 (d) Did you discuss whether and how consent was obtained from people whose data you’re using/cu474 rating? 

- 475 (e) Did you discuss whether the data you are using/curating contains personally identifiable information 476 or offensive content? 

- 477 5. If you used crowdsourcing or conducted research with human subjects... 

- 478 (a) Did you include the full text of instructions given to participants and screenshots, if applicable? 

- 479 (b) Did you describe any potential participant risks, with links to Institutional Review Board (IRB) 480 approvals, if applicable? 

- 481 (c) Did you include the estimated hourly wage paid to participants and the total amount spent on 482 participant compensation? 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

483 

## **Position Encodings** 

484 Suppose we sample a sequence of positions _x_ 0 _, ..., xT ∈_ R[2] and a sequence of velocities _v_ 1 _, ..., vT ∈_ R[2] , where 485 _xt_ = _xt−_ 1 + _vt_ . We want to train the networks in a supervised manner to predict (a possible encoding of) 486 their position. We used the below encodings as different regression targets. For some encodings that required 487 place cell populations, we denote the number of place cells _Np_ and denote their locations _{pi}[N] i_ =1 _[p]_[,][sampled] 488 uniformly at random within the 2.2 m _×_ 2.2 m arena. 

489 

- **“Low-dimensional" Cartesian:** _xt_ 

- **“High-dimensional" Cartesian:** Let _A ∈_ R _[N][p][×]_[2] _, b ∈_ R _[N][p]_ have entries sampled i.i.d. from _Uniform_ ( _−_ 1 _,_ 1). The target is a vector in R _[N][p]_ given by: 

   - _Axt_ + _b_ 

- **Polar:** Let ( _rt, θt_ ) denote the polar form of the agent’s position _xt_ . The target is a vector in R _[N][p]_ , half comprised of “distance" units and half comprised of “direction" units. Let _A ∈_ R[0] _[.]_[5] _[N][p][×]_[1] _, b ∈_ R[0] _[.]_[5] _[N][p]_ have entries sampled i.i.d. from _Uniform_ ( _−_ 1 _,_ 1); the distance cells have activites: 

**==> picture [33 x 10] intentionally omitted <==**

Let _µ ∈_ [ _−π, π_ ] _[N][p][/]_[2] have entries sampled i.i.d. uniformly at random. The direction cells have entries given by von-Mises-like bumps: 

**==> picture [83 x 18] intentionally omitted <==**

- **Gaussian:** A vector in R _[N][p]_ whose entries are given by: 

**==> picture [107 x 25] intentionally omitted <==**

- **Difference of Gaussians:** A vector in R _[N][p]_ whose entries are given by: 

**==> picture [223 x 24] intentionally omitted <==**

- **Difference of Softmaxes:** A vector in R _[N][p]_ whose entries are given by: 

**==> picture [271 x 24] intentionally omitted <==**

- **Softmax of Differences:** A vector in R _[N][p]_ whose entries are given by: 

**==> picture [207 x 24] intentionally omitted <==**

490 

## **Grid Scores and Grid Cell Thresholds** 

491 What qualifies as a grid cell? The most commonly used method of quantifying grid cells is via the “grid 492 score", which functions by binning neural activity into rate maps using spatial position, applying an adaptive 493 smoother, then taking a circular sample of the autocorrelation centered on the central peak and comparing it 494 to rotated versions of the same circular sample. The 60 _[◦]_ grid score is specifically given by: 

( _corr_ [60] + _corr_ [120]) _/_ 2 _−_ ( _corr_ [30] + _corr_ [90] + _corr_ [150]) _/_ 3 

495 We used the grid scorer implementation used by [2] (https://github.com/deepmind/grid-cells/blob/master/scores.py), 496 [45] (https://github.com/ganguli-lab/grid-pattern-formation/blob/master/scores.py) and [36]. 497 What score is sufficient to qualify as a grid score? Experimentalists have used thresholds of 0.3 [44] and 498 0.349 [9] on biological neurons, whereas computationalists have used 0.3 [36] and 0.37 [2, 45] on artificial 499 neurons. We found that for artificial neurons, these thresholds are far too low (Fig. 7); ANN units with grid 500 scores _>_ 0 _._ 4, and even as high as 1 _._ 3, often look nothing like grid cells. This is because the grid score looks 501 for 60 _[◦]_ rotational symmetry, and while grid cells are indeed symmetric, so are many other rate maps. Private 502 conversations with the authors of [2, 45, 36] showed everyone was in agreement that grid scores are a metric 503 in need of improvement. After internal disagreement, we compromised at a grid score threshold of 0.8. 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

504 

## **Number of Bins for Computing Rate Maps** 

505 The first step in computing grid scores is determining the number of bins to use to compute rate maps. 506 However, establishing the number of bins used by previous approaches proved baffling difficult. The original 507 experimental work used 5 cm by 5 cm bins [22]. Since the square arena used in these experiments is 2.2 m by 508 2.2 m (same as [2, 45, 36], the number of bins should be 44 x 44. However, we found discrepancies in previous 509 approaches’ text and code. 510 [2]’s text claims to use 32 x 32 bins of 6.875 cm x 6.875 cm (“Spatial (ratemaps) and directional activity 511 maps were calculated for individual units as follows. Each point in the trajectory was assigned to a specific 512 spatial and directional bin according to its location and the direction in which it faced. Spatial bins were 513 defined as a 32 × 32 square grid spanning each environment and directional bins as 20 equal width intervals.”), 514 but their code[2] used 20 x 20 bins of 11 cm x 11 cm. [45] claimed to use 2 cm x 2 cm bins (“"Grid score was 515 evaluated as in [2]]. A spatial ratemap was computed for each neuron by binning the agent’s position into 516 2cm x 2cm bins, and computing the average firing rate within each bin.”) but their code[3] similarly used 20 x 517 20 bins. [36] claimed to use 5 cm x 5 cm bins (“Nayebi: "We bin the positions in each environment using 5 cm 518 bins, following prior work [Hardcastle et al., 2017, Butler et al., 2019, Low et al., 2020]. Thus, the 100cm[2] 519 environment used 400 (20 × 20) bins, the 150cm[2] environment used 900 (30 × 30) bins, and the 400cm 1D 

> 2 `https://github.com/deepmind/grid-cells/blob/master/train.py#L201` 

> 3 `https://github.com/ganguli-lab/grid-pattern-formation/blob/master/visualize.py#L136` 

**==> picture [142 x 164] intentionally omitted <==**

**==> picture [142 x 164] intentionally omitted <==**

**==> picture [142 x 164] intentionally omitted <==**

**==> picture [142 x 168] intentionally omitted <==**

**==> picture [142 x 168] intentionally omitted <==**

**==> picture [142 x 168] intentionally omitted <==**

Figure 7: **Grid scoring is the dominant method to identify grid cells, but we found it performs extremely poorly at identifying grid cells.** Top: example rate maps from low position decoding error Difference-of-Softmaxes (DoS) networks three grid score ranges: [0 _._ 35 _,_ 0 _._ 45) _,_ [0 _._ 8 _,_ 0 _._ 9) _,_ [1 _._ 15 _, ∞_ ). Bottom: example rate maps from low position decoding error Difference-of-Gaussians (DoG) networks. We considered three grid score thresholds: 0.3 (used by some experimentalists), 0.8 (low probability of finding grid cells), 1.15 (decent probability of finding grid cells). 

15 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [90 x 75] intentionally omitted <==**

**==> picture [91 x 75] intentionally omitted <==**

**==> picture [90 x 75] intentionally omitted <==**

**==> picture [91 x 73] intentionally omitted <==**

**==> picture [90 x 73] intentionally omitted <==**

**==> picture [90 x 75] intentionally omitted <==**

**==> picture [91 x 73] intentionally omitted <==**

**==> picture [91 x 73] intentionally omitted <==**

**==> picture [91 x 72] intentionally omitted <==**

**==> picture [90 x 72] intentionally omitted <==**

**==> picture [91 x 73] intentionally omitted <==**

**==> picture [91 x 73] intentionally omitted <==**

**==> picture [90 x 72] intentionally omitted <==**

**==> picture [91 x 72] intentionally omitted <==**

**==> picture [90 x 72] intentionally omitted <==**

Figure 8: Grid score distributions do not differ as a function of number of bins: 400 (20 x 20; blue), 1024 (32 x 32; orange), 1936 (44 x 44; green). 

520 track used 80 bins.”) but their code similarly used 20 x 20 bins. The code suggests that [36] used the grid 521 scorer of [45], who in turn used the grid scorer of [2]. 

522 Consequently, we tested what effect the number of bins has on the distribution of grid scores. We found 523 that the number of bins appears to have little to no effect (Fig. 8), so we chose to use 44 x 44 bins since this 524 yields bins of size 5 cm x 5 cm. 

## 525 

## **Place cell autocorrelation** 

In this section, we will derive the form of the place cell correlation function, centered at _⃗µ_ . When the spatial tuning curve is a difference-of-Gaussians, the correlation function is *also* a Difference-of-Gaussians, albeit with different parameters. Consider the spatial tuning curve: 

**==> picture [246 x 26] intentionally omitted <==**

So the correlation between place cells centered at _⃗µ_ 1 and _⃗µ_ 2 with **r** = _⃗µ_ 1 _− ⃗µ_ 2 is given by 

**==> picture [236 x 23] intentionally omitted <==**

Simplifying the above expression, using the identity: � _dxN_ ( _x_ ; _µf , σf_ ) _N_ ( _r−x_ ; _µf , σf_ ) = _N_ ( _r_ ; _µf_ + _µg,_ ~~�~~ _σf_[2][+] _[ σ] g_[2][)][,] we get: 

**==> picture [300 x 26] intentionally omitted <==**

16 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 526 **Sweeps** 

527 **.1 Cartesian (Low Dimensional)** 

528 method : grid 529 metric : 530 goal : minimize 531 name : pos_decoding_err 532 parameters : 533 Ng: 534 values : 535 −1024 536 Np: 537 values : 538 −2 539 activation : 540 values : 541 −relu 542 −tanh 543 −sigmoid 544 −l i n e a r 545 batch_size : 546 values : 547 −200 548 bin_side_in_m : 549 values : 550 −0.05 551 box_height_in_m : 552 values : 553 −2.2 554 box_width_in_m : 555 values : 556 −2.2 557 i n i t i a l i z e r : 558 values : 559 −glorot_uniform 560 −glorot_normal 561 −orthogonal 562 is_periodic : 563 values : 564 −f a l s e 565 learning_rate : 566 values : 567 −0.0001 568 n_epochs : 569 values : 570 −20 571 n_grad_steps_per_epoch : 572 values : 573 −10000 574 n_place_fields_per_cell : 575 values : 576 −1 577 optimizer : 578 values : 579 −sgd 580 −adam 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

581 −rmsprop 582 place_cell_rf : 583 values : 584 −0 585 place_field_loss : 586 values : 587 −mse 588 place_field_normalization : 589 values : 590 −none 591 place_field_values : 592 values : 593 −c a rtes i an 594 readout_dropout : 595 values : 596 −0 597 −0.5 598 recurrent_dropout : 599 values : 600 −0 601 −0.5 602 rnn_type : 603 values : 604 −RNN 605 −LSTM 606 −UGRNN 607 −GRU 608 seed : 609 values : 610 −0 611 −1 612 −2 613 sequence_length : 614 values : 615 −20 616 surround_scale : 617 values : 618 −1 619 weight_decay : 620 values : 621 −0 622 −0.0001 

## 623 **.2 Cartesian (High Dimensional)** 

624 method : grid 625 metric : 626 goal : minimize 627 name : pos_decoding_err 628 parameters : 629 Ng: 630 values : 631 −1024 632 Np: 633 values : 634 −512 

18 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

635 activation : 636 values : 637 −relu 638 −tanh 639 −sigmoid 640 −l i n e a r 641 batch_size : 642 values : 643 −200 644 bin_side_in_m : 645 values : 646 −0.05 647 box_height_in_m : 648 values : 649 −2.2 650 box_width_in_m : 651 values : 652 −2.2 653 i n i t i a l i z e r : 654 values : 655 −glorot_uniform 656 −glorot_normal 657 −orthogonal 658 is_periodic : 659 values : 660 −f a l s e 661 learning_rate : 662 values : 663 −0.0001 664 n_epochs : 665 values : 666 −20 667 n_grad_steps_per_epoch : 668 values : 669 −1000 670 n_place_fields_per_cell : 671 values : 672 −1 673 optimizer : 674 values : 675 −adam 676 place_cell_rf : 677 values : 678 −0 679 place_field_loss : 680 values : 681 −mse 682 place_field_normalization : 683 values : 684 −none 685 place_field_values : 686 values : 687 −high_dim_cartesian 688 readout_dropout : 689 values : 690 −0 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

691 −0.5 692 recurrent_dropout : 693 values : 694 −0 695 −0.5 696 rnn_type : 697 values : 698 −RNN 699 −LSTM 700 −UGRNN 701 −GRU 702 seed : 703 values : 704 −0 705 −1 706 −2 707 sequence_length : 708 values : 709 −20 710 surround_scale : 711 values : 712 −0 713 weight_decay : 714 values : 715 −0 716 −0.0001 

## 717 **.3 Polar (High Dimensional)** 

718 method : grid 719 metric : 720 goal : minimize 721 name : pos_decoding_err 722 parameters : 723 Ng: 724 values : 725 −1024 726 Np: 727 values : 728 −512 729 activation : 730 values : 731 −relu 732 −tanh 733 −l i n e a r 734 −sigmoid 735 batch_size : 736 values : 737 −200 738 bin_side_in_m : 739 values : 740 −0.05 741 box_height_in_m : 742 values : 743 −2.2 744 box_width_in_m : 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

745 values : 746 −2.2 747 i n i t i a l i z e r : 748 values : 749 −glorot_uniform 750 −glorot_normal 751 −orthogonal 752 is_periodic : 753 values : 754 −f a l s e 755 learning_rate : 756 values : 757 −0.0001 758 n_epochs : 759 values : 760 −20 761 n_grad_steps_per_epoch : 762 values : 763 −1000 764 n_place_fields_per_cell : 765 values : 766 −1 767 optimizer : 768 values : 769 −adam 770 place_cell_rf : 771 values : 772 −0 773 place_field_loss : 774 values : 775 −mse 776 place_field_normalization : 777 values : 778 −none 779 place_field_values : 780 values : 781 −high_dim_polar 782 readout_dropout : 783 values : 784 −0 785 −0.5 786 recurrent_dropout : 787 values : 788 −0 789 −0.5 790 rnn_type : 791 values : 792 −RNN 793 −LSTM 794 −UGRNN 795 −GRU 796 seed : 797 values : 798 −0 799 −1 800 −2 

21 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

801 sequence_length : 802 values : 803 −20 804 surround_scale : 805 values : 806 −0 807 weight_decay : 808 values : 809 −0 810 −0.0001 

811 **.4 Gaussian Place Cells** 812 method : grid 813 metric : 814 goal : minimize 815 name : pos_decoding_err 816 parameters : 817 Ng: 818 values : 819 −1024 820 Np: 821 values : 822 −512 823 activation : 824 values : 825 −l i n e a r 826 −relu 827 −tanh 828 −sigmoid 829 batch_size : 830 values : 831 −200 832 bin_side_in_m : 833 values : 834 −0.05 835 box_height_in_m : 836 values : 837 −2.2 838 box_width_in_m : 839 values : 840 −2.2 841 i n i t i a l i z e r : 842 values : 843 −glorot_uniform 844 is_periodic : 845 values : 846 −f a l s e 847 learning_rate : 848 values : 849 −0.0001 850 n_epochs : 851 values : 852 −20 853 n_grad_steps_per_epoch : 854 values : 

22 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

855 −10000 856 n_place_fields_per_cell : 857 values : 858 −1 859 optimizer : 860 values : 861 −adam 862 place_cell_rf : 863 values : 864 −0.08 865 −0.1 866 −0.12 867 −0.14 868 −0.16 869 −0.2 870 −0.24 871 −0.28 872 place_field_loss : 873 values : 874 −crossentropy 875 place_field_normalization : 876 values : 877 − **global** 878 place_field_values : 879 values : 880 −gaussian 881 readout_dropout : 882 values : 883 −0 884 −0.5 885 recurrent_dropout : 886 values : 887 −0 888 −0.5 889 rnn_type : 890 values : 891 −RNN 892 −LSTM 893 −UGRNN 894 −GRU 895 seed : 896 values : 897 −0 898 −1 899 sequence_length : 900 values : 901 −20 902 surround_scale : 903 values : 904 −1 905 weight_decay : 906 values : 907 −0.0001 

908 **.5 Dfiference-of-Gaussians Place Cells** 

23 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

909 method : grid 910 metric : 911 goal : minimize 912 name : pos_decoding_err 913 parameters : 914 Ng: 915 values : 916 −1024 917 Np: 918 values : 919 −512 920 activation : 921 values : 922 −relu 923 batch_size : 924 values : 925 −200 926 bin_side_in_m : 927 values : 928 −0.05 929 box_height_in_m : 930 values : 931 −2.2 932 box_width_in_m : 933 values : 934 −2.2 935 i n i t i a l i z e r : 936 values : 937 −glorot_uniform 938 is_periodic : 939 values : 940 −f a l s e 941 learning_rate : 942 values : 943 −0.0001 944 n_epochs : 945 values : 946 −20 947 n_grad_steps_per_epoch : 948 values : 949 −10000 950 n_place_fields_per_cell : 951 values : 952 −1 953 optimizer : 954 values : 955 −adam 956 place_cell_rf : 957 values : 958 −0.05 959 −0.1 960 −0.15 961 −0.2 962 −0.3 963 −0.4 964 −0.5 

24 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

965 place_field_loss : 966 values : 967 −crossentropy 968 place_field_normalization : 969 values : 970 − **global** 971 place_field_values : 972 values : 973 −true_difference_of_gaussians 974 readout_dropout : 975 values : 976 −0 977 −0.5 978 recurrent_dropout : 979 values : 980 −0 981 −0.5 982 rnn_type : 983 values : 984 −RNN 985 −LSTM 986 −UGRNN 987 −GRU 988 seed : 989 values : 990 −0 991 −1 992 −2 993 sequence_length : 994 values : 995 −20 996 surround_scale : 997 values : 998 −1.5 999 −2 1000 −2.5 1001 −3 1002 −4 1003 −5 1004 −6 1005 weight_decay : 1006 values : 1007 −0.0001 

## 1008 **.6 Difference-of-Softmaxes Place Cells** 

1009 method : grid 1010 metric : 1011 goal : minimize 1012 name : pos_decoding_err 1013 parameters : 1014 Ng: 1015 values : 1016 −1024 1017 Np: 1018 values : 

25 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

|1019|−512|
|---|---|
|1020|activation :|
|1021|values :|
|1022|−relu|
|1023|−tanh|
|1024|batch_size :|
|1025|values :|
|1026|−200|
|1027|bin_side_in_m :|
|1028|values :|
|1029|−0.05|
|1030|box_height_in_m :|
|1031|values :|
|1032|−2.2|
|1033|box_width_in_m :|
|1034|values :|
|1035|−2.2|
|1036|i n i t i a l i z e r :|
|1037|values :|
|1038|−glorot_uniform|
|1039|is_periodic :|
|1040|values :|
|1041|−f a l s e|
|1042|learning_rate :|
|1043|values :|
|1044|−0.0001|
|1045|n_epochs :|
|1046|values :|
|1047|−20|
|1048|n_grad_steps_per_epoch :|
|1049|values :|
|1050|−10000|
|1051|n_place_fields_per_cell :|
|1052|values :|
|1053|−1|
|1054|optimizer :|
|1055|values :|
|1056|−adam|
|1057|place_cell_rf :|
|1058|values :|
|1059|−0.08|
|1060|−0.09|
|1061|−0.1|
|1062|−0.11|
|1063|−0.12|
|1064|−0.13|
|1065|−0.14|
|1066|−0.15|
|1067|−0.16|
|1068|−0.17|
|1069|−0.18|
|1070|−0.19|
|1071|−0.2|
|1072|−0.24|
|1073|−0.28|
|1074|−0.32|



26 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1075 place_field_loss : 1076 values : 1077 −crossentropy 1078 place_field_normalization : 1079 values : 1080 − **global** 1081 place_field_values : 1082 values : 1083 −difference_of_gaussians 1084 readout_dropout : 1085 values : 1086 −0 1087 −0.5 1088 recurrent_dropout : 1089 values : 1090 −0 1091 −0.5 1092 rnn_type : 1093 values : 1094 −RNN 1095 −LSTM 1096 −UGRNN 1097 −GRU 1098 seed : 1099 values : 1100 −0 1101 −1 1102 −2 1103 sequence_length : 1104 values : 1105 −20 1106 surround_scale : 1107 values : 1108 −1.5 1109 −2 1110 −2.5 1111 −3 1112 −4 1113 weight_decay : 1114 values : 1115 −0.0001 

1116 **.7 Softmax-of-Differences Place Cells** 

1117 method : grid 1118 metric : 1119 goal : minimize 1120 name : pos_decoding_err 1121 parameters : 1122 Ng: 1123 values : 1124 −1024 1125 Np: 1126 values : 1127 −512 1128 activation : 

27 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1129 values : 1130 −relu 1131 batch_size : 1132 values : 1133 −200 1134 bin_side_in_m : 1135 values : 1136 −0.05 1137 box_height_in_m : 1138 values : 1139 −2.2 1140 box_width_in_m : 1141 values : 1142 −2.2 1143 i n i t i a l i z e r : 1144 values : 1145 −glorot_uniform 1146 is_periodic : 1147 values : 1148 −f a l s e 1149 learning_rate : 1150 values : 1151 −0.0001 1152 n_epochs : 1153 values : 1154 −20 1155 n_grad_steps_per_epoch : 1156 values : 1157 −10000 1158 n_place_fields_per_cell : 1159 values : 1160 −1 1161 optimizer : 1162 values : 1163 −adam 1164 place_cell_rf : 1165 values : 1166 −0.09 1167 −0.12 1168 −0.15 1169 −0.18 1170 −0.21 1171 −0.24 1172 place_field_loss : 1173 values : 1174 −crossentropy 1175 place_field_normalization : 1176 values : 1177 − **global** 1178 place_field_values : 1179 values : 1180 −softmax_of_differences 1181 readout_dropout : 1182 values : 1183 −0 1184 recurrent_dropout : 

28 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1185 values : 1186 −0 1187 rnn_type : 1188 values : 1189 −RNN 1190 −LSTM 1191 −UGRNN 1192 −GRU 1193 seed : 1194 values : 1195 −0 1196 −1 1197 −2 1198 sequence_length : 1199 values : 1200 −20 1201 surround_scale : 1202 values : 1203 −1.5 1204 −2 1205 −2.5 1206 −3 1207 weight_decay : 1208 values : 1209 −0.0001 

1210 **.8 Multiple Scales and Multiple Fields Difference-of-Softmaxes Place Cells** 

1211 method : grid 1212 metric : 1213 goal : minimize 1214 name : pos_decoding_err 1215 parameters : 1216 Ng: 1217 values : 1218 −1024 1219 Np: 1220 values : 1221 −512 1222 activation : 1223 values : 1224 −relu 1225 batch_size : 1226 values : 1227 −200 1228 bin_side_in_m : 1229 values : 1230 −0.05 1231 box_height_in_m : 1232 values : 1233 −2.2 1234 box_width_in_m : 1235 values : 1236 −2.2 1237 i n i t i a l i z e r : 1238 values : 

29 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1239 −glorot_uniform 1240 is_periodic : 1241 values : 1242 −f a l s e 1243 learning_rate : 1244 values : 1245 −0.0001 1246 n_epochs : 1247 values : 1248 −20 1249 n_grad_steps_per_epoch : 1250 values : 1251 −10000 1252 n_place_fields_per_cell : 1253 values : 1254 −Poisson ( 2.0 ) 1255 −Poisson ( 3.0 ) 1256 optimizer : 1257 values : 1258 −adam 1259 place_cell_rf : 1260 values : 1261 −0.12 1262 −Uniform ( 0.06 , 0.24 ) 1263 −Uniform ( 0.06 , 1.0 ) 1264 place_field_loss : 1265 values : 1266 −crossentropy 1267 place_field_normalization : 1268 values : 1269 − **global** 1270 place_field_values : 1271 values : 1272 −difference_of_gaussians 1273 readout_dropout : 1274 values : 1275 −0 1276 recurrent_dropout : 1277 values : 1278 −0 1279 rnn_type : 1280 values : 1281 −RNN 1282 −UGRNN 1283 seed : 1284 values : 1285 −0 1286 −1 1287 −2 1288 sequence_length : 1289 values : 1290 −20 1291 surround_scale : 1292 values : 1293 −2 1294 −Uniform ( 1.50 , 2.50 ) 

30 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1295 −Uniform ( 1.25 , 4.50 ) 1296 weight_decay : 1297 values : 1298 −0.0001 

1299 **.9 Nayebi et al. 2021 [36] Replication** 1300 method : grid 1301 metric : 1302 goal : minimize 1303 name : pos_decoding_err 1304 parameters : 1305 Ng: 1306 values : 1307 −4096 1308 Np: 1309 values : 1310 −512 1311 activation : 1312 values : 1313 −relu 1314 batch_size : 1315 values : 1316 −200 1317 bin_side_in_m : 1318 values : 1319 −0.05 1320 box_height_in_m : 1321 values : 1322 −2.2 1323 box_width_in_m : 1324 values : 1325 −2.2 1326 i n i t i a l i z e r : 1327 values : 1328 −glorot_uniform 1329 is_periodic : 1330 values : 1331 −f a l s e 1332 learning_rate : 1333 values : 1334 −0.0001 1335 n_epochs : 1336 values : 1337 −20 1338 n_grad_steps_per_epoch : 1339 values : 1340 −10000 1341 n_place_fields_per_cell : 1342 values : 1343 −1 1344 optimizer : 1345 values : 1346 −adam 1347 place_cell_rf : 1348 values : 

31 

bioRxiv preprint doi: https://doi.org/10.1101/2022.08.07.503109; this version posted August 7, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

|1349|−0.12|
|---|---|
|1350|place_field_loss :|
|1351|values :|
|1352|−crossentropy|
|1353|place_field_normalization :|
|1354|values :|
|1355|−**global**|
|1356|place_field_values :|
|1357|values :|
|1358|−difference_of_gaussians|
|1359|readout_dropout :|
|1360|values :|
|1361|−0|
|1362|recurrent_dropout :|
|1363|values :|
|1364|−0|
|1365|rnn_type :|
|1366|values :|
|1367|−RNN|
|1368|−LSTM|
|1369|−UGRNN|
|1370|−GRU|
|1371|−SRNN|
|1372|seed :|
|1373|values :|
|1374|−0|
|1375|−1|
|1376|−2|
|1377|−3|
|1378|−4|
|1379|sequence_length :|
|1380|values :|
|1381|−20|
|1382|surround_scale :|
|1383|values :|
|1384|−2|
|1385|weight_decay :|
|1386|values :|
|1387|−0.0001|



32 

