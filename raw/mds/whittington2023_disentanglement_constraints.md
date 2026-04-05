Published as a conference paper at ICLR 2023 

# - DISENTANGLEMENT WITH BIOLOGICAL CON STRAINTS: A THEORY OF FUNCTIONAL CELL TYPES 

**James C.R. Whittington** _[∗]_ **William Dorrell Surya Ganguli Timothy E.J. Behrens** Stanford & Oxford UCL Stanford UCL & Oxford 

## ABSTRACT 

Neurons in the brain are often finely tuned for specific task variables. Moreover, such disentangled representations are highly sought after in machine learning. Here we mathematically prove that simple biological constraints on neurons, namely nonnegativity and energy efficiency in both activity and weights, promote such sought after disentangled representations by enforcing neurons to become selective for single factors of task variation. We demonstrate these constraints lead to disentanglement in a variety of tasks and architectures, including variational autoencoders. We also use this theory to explain why the brain partitions its cells into distinct cell types such as grid and object-vector cells, and also explain when the brain instead entangles representations in response to entangled task factors. Overall, this work provides a mathematical understanding of why single neurons in the brain often represent single human-interpretable factors, and steps towards an understanding task structure shapes the structure of brain representation. 

## 1 INTRODUCTION 

Understanding why and how neurons behave is now foundational for both machine learning and neuroscience. Such understanding can lead to better, more interpretable artificial neural networks, as well as provide insights into how biological networks mediate cognition. A key to both these pursuits lies in understanding how neurons can best structure their firing patterns to solve tasks. 

Neuroscientists have some understanding of how task demands affect both early single neuron responses (Olshausen & Field, 1996; Yamins et al., 2014; Ocko et al., 2018; McIntosh et al., 2016) and population level measures such as dimensionality (Gao et al., 2017; Stringer et al., 2019). However, there is little understanding of neural population structure in higher brain areas. As an example, we do not even understand why many different bespoke cellular responses exist for physical space, such as grid cells (Hafting et al., 2005), object-vector cells (Høydal et al., 2019), border vector cells (Solstad et al., 2008; Lever et al., 2009), band cells (Krupic et al., 2012), or many other cells (O’Keefe & Dostrovsky, 1971; Gauthier & Tank, 2018; Sarel et al., 2017; Deshmukh & Knierim, 2013). Each cell has a well defined, specific cellular response pattern to space, objects, _or_ borders, as opposed to a mixed response to space, objects, _and_ borders. Similarly, we don’t understand why neurons in inferior temporal cortex are aligned to axes of data generative factors (Chang & Tsao, 2017; Bao et al., 2020; Higgins et al., 2021), why visual cortical neurons are de-correlated (Ecker et al., 2010), why neurons in parietal cortex are selective only for specific tasks (Lee et al., 2022), why prefrontal neurons are apparently mixed-selective (Rigotti et al., 2013), and why grid cells sometimes warp towards rewarded locations (Boccara et al., 2019) and sometimes don’t (Butler et al., 2019). In essence, why are some neural representations entangled and others not? 

Machine learning has long endeavoured to build models that disentangle factors of variation (Hinton et al., 2011; Higgins et al., 2017a; Locatello et al., 2019; Bengio et al., 2012). We define disentanglement as single neurons responding to single factors of variation (see Appendix A.1 for further details). Such disentangled factors can facilitate compositional generalisation and reasoning (Higgins et al., 2018; 2017b; Whittington et al., 2021a) (though some work has challenged the idea that disentangled representations generalise better (Schott et al., 2022), as well as lead to more interpretable outcomes in which individual neurons represent meaningful quantities. Unfortunately, building models that disentangle is challenging (Locatello et al., 2019). 

> _∗_ Correspondence to: jcrwhittington@gmail.com 

1 

Published as a conference paper at ICLR 2023 

**==> picture [397 x 201] intentionally omitted <==**

**----- Start of picture text -----**<br>
z =  e 1 00 .. 86� +  e 2  − 00 . 8 . 6� + 00� z =  e 1 00 .. 86� +  e 2  − 00 . 8 . 6� +  a 11 .. 44� z =  e 1 10� +  e 2 01� +  a 11�<br>X V ar ( zj ) = 2 σ [2] X V ar ( zj ) = 2 σ [2] X V ar ( zj ) = 2 σ [2]<br>j j j<br>E || z || [2] = 2 σ [2] E || z || [2] = 2 σ [2] + 2 a [2] 1 . 4 [2] E || z || [2] = 2 σ [2] + 2 a [2]<br>Neuron 2 Neuron 2 Neuron 2<br>Make non-negative Minimise activity energy<br>Neuron 1 Neuron 1 Neuron 1<br>Figure 1: Proof intuition. Two uniformly distributed independent factors represented with two<br>entangled neurons (left). The representation can be made nonnegative at the expense of activity<br>energy (middle). Activity energy is minimised under a nonnegativity (and variance) constraint when<br>the neurons are axis aligned to task factors (i.e. disentangled, right). Grey boxes denote uniform<br>distributions over neural activity induced by uniform distributions over task factors. Note our proof<br>does not require uniformity.<br>**----- End of picture text -----**<br>


In this work we 1) prove simple biological constraints of **nonnegativity** and **minimising activity energy** lead to factorised representations in linear networks; 2) empirically show these constraints lead to disentangled representations in both linear and nonlinear networks; 3) obtain competitive disentanglement scores on a standard disentanglement benchmark; 4) provide an understanding why neurons in the brain are characterised into specific cell types due to these same biological constraints; 5) empirically show these constraints lead to specific cell types; 6) suggest when and why neurons in the brain exhibit disentanglement versus mixed-selectivity. 

Please see appendix A.2 for a comprehensive discussion relating our work to existing literature. 

## 2 LINEAR DISENTANGLEMENT WITH BIOLOGICAL CONSTRAINTS 

We first provide a theorem that suggests why the combined biological constraints of nonnegativity and energy efficiency lead to neural disentanglement (proofs of all theorems are in App. A.3): 

**Theorem 1** . Let _**e** ∈_ R _[k]_ be a random vector whose _k_ independent components denote _k_ task factors. We assume each independent task factor _ei_ is drawn from a distribution[1] that has mean 0, variance _σ_[2] , and maximum and minimum values of min( _ei_ ) = _−a_ and max( _ei_ ) = _a_ . Also let _**z** ∈_ R _[n]_ be a linear neural representation of the task factors given by 

**==> picture [230 x 10] intentionally omitted <==**

where _**M** ∈_ R _[n][×][k]_ are mixing weights and _**b** z ∈_ R _[n]_ is a bias. We further assume two constraints: (1) the neural representation is _nonnegative_ with _zi ≥_ 0 for all _i_ = 1 _, . . . , n_ , and (2) the neural population variance is a nonzero constant,[�] _j[V ar]_[(] _[z][j]_[)][=] _[C]_[,][so][that][the][neural][representation] retains some information about the task variables. Under these two constraints we show that in the space of all possible neural representations (parameterised by _**M**_ and _**b** z_ ), the representations that achieve minimal activity energy E _||_ _**z** ||_[2] also exhibit disentanglement, by which we mean every neuron _zj_ is selective for at most one task parameter: i.e. _|Mjk||Mjl|_ = 0 for _k_ = _l_ , a.k.a. each row of _**M**_ has at most 1 non-zero entry. (Proof in App. A.3.1). 

**Intuition.** The intuition underlying the proof of the theorem is shown in Fig.1, where the key idea can be seen with two neurons encoding two factors. In particular, the bias must make every _zi_ nonnegative for all values of _e_ 1 and _e_ 2. But since _e_ 1 and _e_ 2 are independent, the minimum firing of neuron 1 for example obeys min( _z_ 1) = min(0 _._ 8 _e_ 1 _−_ 0 _._ 6 _e_ 2) = min(0 _._ 8 _e_ 1) + min( _−_ 0 _._ 6 _e_ 2) = _−a_ (0 _._ 8 + 0 _._ 6). Thus for neurons that mix factors, a larger bias term must be used to ensure nonnegativity, which leads to increased expected energy. Minimising this energy (subject to a constant variance) requires the smallest possible bias for each neuron, which occurs when each neuron is selective for a single task factor. We note that this is consistent with neurons having a baseline firing 

> 1We understand that task factors, or indeed neurons in the brain, are generally not i.i.d., but we have made this assumption for mathematical convenience. 

2 

Published as a conference paper at ICLR 2023 

rate where now activity below baseline corresponds to negative/positive values in the distribution, and activity above baseline corresponds to positive/negative values in the distribution. 

The above theorem, while simple, is restricted in two ways: (1) the independent task factors _ei_ are _directly_ available to the network; (2) representational collapse (i.e. setting _**z**_ = 0) under energy minimisation is prevented solely by a variance constraint. We thus consider a more general setting where a neural circuit receives not the independent task factor vector _**e**_ , but instead receives the mixed combination _**x**_ = _**De**_ , where _**x** ∈_ R _[m]_ , _**D** ∈_ R _[m][×][k]_ and _m ≥ n ≥ k_ . We further model the neural representation _**z**_ as a linear generative model that can predict observed data _**x**_ via _**x**_ = _**W z**_ + _**b** x._ Thus prediction, not variance constraint, now prevents collapsing neural representations (proof in Appendix A.3.2). Furthermore in Appendix A.3.3 we prove the following: 

**Theorem 2.** Let _**x**_ = _**De**_ be observed entangled data, where the independent task factor vector _**e**_ obeys the same distributional assumptions as in Theorem 1. Let a neural representation _**z**_ exactly predict observed data via _**x**_ = _**W z**_ + _**b** x_ with zero error. Then for all such data generation models (with parameters _**D**_ ) and all such neural representations (with parameters _**W**_ and _**b** x_ ), as long as: (1) the columns of _**D**_ are (scaled) orthonormal; (2) the norm of the read-out weights _||_ _**W** ||_[2] _F_[is finite;] (3) the neural representation is nonnegative (i.e. _**z** >_ 0), then out of all such neural representations, the minimum energy representations are also disentangled ones. By this we mean that each neuron _zi_ will be selective for at most one hidden task factor _ej_ . 

We note that _**D**_ having (scaled) orthonormal columns may seem like a strong constraint, but it holds approximately for any random matrix _**D**_ with many observations (dimensionality of _**x**_ ) and few independent task factors (dimensionality of _**e**_ ) (proof in Appendix A.3.4). Appendix A.3.5 discusses and provides intuition for when disentanglement occurs as _**D**_ takes more general forms. 

Strikingly, the essential content of Theorem 2 is that any linear, nonnegative, optimally energetically efficient, generative neural representation that accurately predicts entangled observations that are linear mixtures of hidden task factors, will possess single neurons that are selective for individual task factors, despite _never_ having _direct_ access to them. In terms of applications, this theorem could apply in supervised or self-supervised machine learning settings in any neural network layer _**z**_ that is linearly read-out from, or in neuroscience settings where _**z**_ reflects a neural population from which one attempts to linearly decode task factors. While Theorem 2 holds in a simple setting, we will show through simulations that its essential content, namely that nonnegativity and energy efficiency together promote disentanglement, holds in practice in much more complex multilayer neural networks. 

## 3 DISENTANGLEMENT IN MACHINES 

We now present simulation results demonstrating that nonnegativity and energy efficiency (minimising either activity or weight energy) lead to single neuron selectivity for single task factors. We show this for supervised and unsupervised learning, both for linear and nonlinear tasks and networks (details of datasets, models, and simulations in Appendix A.4 & A.5). 

**A measure for disentangled subspaces.** While our theory describes when single neurons become selective for single independent task factors, it does not limit the number of neurons selective for any given factor. For example in Theorem 2, four copies of the same neuron in _**z**_ , each with half the activity, along with four copies of projecting weights each with half the values, predicts _**x**_ just as well and has exactly the same energy in both _**z**_ and _**W**_[2] . More interestingly, an underlying task factor may not be one-dimensional, e.g. spatial location, in which case the subspace that codes for this factor have at least the same dimension. This phenomena cannot be captured by many metrics of disentanglement (e.g. the popular mutual information gap; MIG; Chen et al. (2018)) since they score highly if each factor is represented in just _one_ neuron. Thus we define a new metric (mutual information ratio; MIR) that instead scores highly if each neuron only cares about one factor (see Appendix A.1 for details). 

**Regularizers as constraints.** We impose nonnegativity via a ReLU activation function, or softly via explicit regularization _L_ nonneg = _β_ nonneg � _i_[max(] _[−][a][i][,]_[ 0)][ where] _[ i]_[ indexes a neuron in the network,] and _βnonneg_ determines the regularization strength. Similarly, we apply regularization to the activity 

> 2Learning dynamics may favour fewer neurons per factor as there are fewer weights to align. 

3 

Published as a conference paper at ICLR 2023 

**==> picture [393 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
A Training data B Without biological constraints C With biological constraints D<br>x y x a 1 ˆy x a 1 ˆy<br>W true W 1 W 2 W 1 W 2<br>Mixed Mixed Mixed Mixed Mixed Mixed Disentangled Mixed<br>… …<br>… …<br>**----- End of picture text -----**<br>


Figure 2: **Shallow linear networks disentangle.** We train 1-hidden layer linear networks on linear data. **A)** Cartoon schematic showing both input and output are entangled linear mixtures of factors (colours). Neurons colours schematically denote which of the factors it codes for. _**W** true_ is the true mapping between _**x**_ and _**y**_ . **B)** A model without biological constraints learns entangled internal representations. Mutual information matrix (scale 0 to 0.6) shown on left, cartoon schematic on right. _**W**_ 1 and _**W**_ 2 are the learnable weights projecting to and from the hidden layer. **C)** A model with our constraints learns disentangled representations (MI matrix scale 0 to 2.25). **D)** Several model variants, in which only those with all our constraints learn disentangled representations (definition of metric MIR in Appendix A.1). Average and standard error shown for 5 random seeds. 

energy and weight energy; _L_ activity = _β_ activity � _l[||]_ _**[a]**[l][||]_[2][and] _[ L]_[weight][=] _[β]_[weight] � _l[||]_ _**[W]**[l][||]_[2][.][The role] of _L_ weight is to promote activity (variance) in the network, otherwise activity could be reduced via _L_ activity, and such reduced activity could be compensated for with arbitrarily large weights. The total loss we optimise is 

**==> picture [302 x 26] intentionally omitted <==**

Here ‘functional constraints’, are any prediction losses the network has i.e. error in predicting target labels in supervised learning, or reconstruction error in autoencoders. 

**Disentanglement in supervised shallow neural networks** . First we consider a dataset _D_ = _{_ _**x** ,_ _**y** }_ , where _**x**_ is a orthogonal mixture of six i.i.d. random variables (hidden independent task factors; uniform distribution), and _**y**_ is a linear transform of _**x**_ (dimension 6; Fig. 2A). First we train shallow linear networks to read-out _**y**_ from _**x**_ . Networks without biological constraints exhibit mixed internal representations (Fig. 2B). However, with our constraints, networks learn distinct sub-networks for each task factor (Fig. 2C). Removing any one of our constraints leads to entangled representations (Fig. 2D). Lastly we note sparsity constraints do not induce disentanglement (Appendix A.6). Thus the disentanglement effect of ReLUs is not from sparsity, but instead from nonnegativity. 

**Disentanglement in supervised deep neural networks** . Training deep nonlinear (ReLU) networks on this data also leads to distinct sub-networks, with all layers learning disentangled representations (Fig. 3A). However with nonlinear data ( _**x** ←_ _**x**_[3] , _**y**_ remaining the same), the early layers are mixed-selective, whereas the later layers are disentangled (Fig. 3B-C). Understanding why the final hidden layer disentangles is easy, since it linearly projects to the target and so our theory directly applies. By extrapolating our theory, we conjecture that our biological constraints encourage any layer to be as linearly related to task factors and as disentangled as possible. However, early layers cannot be linear in hidden task factors since they are required to perform nonlinear computations on the nonlinear data, and thus only once activity becomes linearly related to independent task factors in later layers does disentanglement set in (as predicted by our linear theory). 

**Disentanglement in unsupervised neural networks** . We now consider unsupervised learning, i.e. _D_ = _{_ _**x** }_ , where _**x**_ is a linear mixture of multiple independent task factors as in Theorem 2. Training 0-hidden layer autoencoders on this data, with our biological constraints, recovers the independent task factors in individual neural subspaces (Fig. 4A/B). Moreover, this only occurs when all constraints are present (Fig. 4A). Again, even though our theory applies to the linear setting, the same phenomena occur when training deep nonlinear autoencoders on nonlinear data; i.e. when _**x**_ is a _nonlinear_ mixture of multiple i.i.d. random variables, i.e. _D_ = _{f_ ( _**x**_ ) _}_ (Fig. 4C-D). 

**Disentanglement on a standard benchmark with VAEs** . We now consider a standard disentanglement dataset (Fig. 5A; Kim & Mnih (2018). To be consistent with, and to compare to, the disentanglement literature we use a VAE and measure disentanglement with the familiar mutual-information gap (MIG) metric (Chen et al., 2018). For nonnegativity we ask the mean of the posterior to be 

4 

Published as a conference paper at ICLR 2023 

**==> picture [286 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>**----- End of picture text -----**<br>


Figure 3: **Deep nonlinear networks disentangle.** We train 5-hidden layer nonlinear networks with our constraints on linear and nonlinear data. **A)** For _linear_ data, all layers in the network learn a disentangled representation. **B)** For _nonlinear_ data, only later layers learn a disentangled representations. **C)** Example mutual information matrix from the penultimate hidden layer. 

**==> picture [318 x 84] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>**----- End of picture text -----**<br>


Figure 4: **Learning data generative factors with autoencoders. A)** Training linear autoencoders on linear data. Only models with our constraints learn disentangled representations. **B)** Example mutual information matrix from a high MIR model. **C)** Nonlinear autoencoders trained on nonlinear data. Only models with our constraints learn disentangled representations. **D)** Example mutual information matrix from a high MIR model. All learning curves show mean and standard error from 4 mean from 5 random seeds. 

nonnegative (via a ReLU)[3] , but we _do not_ add a norm constraint as the VAE loss already includes one in its KL term between the Gaussian posterior and the Gaussian prior. 

While state-of-the-art results are not our aim (instead we wish to elucidate that simple biological constraints lead to disentanglement), our disentanglement results (Fig. 5B) are competitive and often better than those in the literature (comparing to results of many models shown in Locatello et al. (2019)) even though those models explicitly ask for a factorised aggregate posterior. The particular baseline model we show here is _β_ -VAE (Fig. 5D). We see that (1) our constraints lead to disentanglement (Fig. 5B-C); (2) including a ReLU improves _β_ -VAE disentanglement (as predicted by nonnegativity arguments above, Fig. 5D); and (3) our constraints give results in the Goldilocks region of high disentanglement and high reconstruction accuracy (Fig. 5E). 

## 4 DISENTANGLEMENT IN BRAINS: A THEORY OF CELL TYPES 

We next turn our attention to neuroscience, which is indeed the inspiration for our biological constraints. While we hope our general theory of neural representations will be useful for explaining representations across tasks and brain areas, for reasons stated below, we choose our first example from spatial processing in the hippocampal formation. We show our biological constraints lead to separate neural populations (modules) coding for separate task variables, but **only** when task variables correspond to independent factors of variation. Importantly, the modules consist of distinct functional cell types with similar firing properties, resembling grid (Hafting et al., 2005) and objectvector cells (Høydal et al., 2019) (GCs and OVCs). 

We choose to focus on spatial representations for two reasons. Firstly, there is a significant puzzle about why neurons deep in the brain, synaptically far from the sensorimotor periphery, almost miraculously develop single cell representations for human-interpretable factors (e.g. GCs for location in space; Fig. 6A, and OVCs for relative location to objects Fig. 6B). Such observations are not easily accounted for by standard neural network accounts that argue that representations are unlikely to be human-interpretable (Richards et al., 2019). Secondly, whilst these bespoke spatial 

> 3Using a nonnegative posterior mean is odd when the prior is Gaussian, but it allows for easier comparison. 

5 

Published as a conference paper at ICLR 2023 

**==> picture [394 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>**----- End of picture text -----**<br>


Figure 5: **Learning data generative factors with variational autoencoders. A)** We train on the Shapes3D dataset, with two example images shown. These images have 6 underlying factors. **B)** MIG scores are higher with higher weight regularization, and generally higher than any _β_ -VAE (panel D). _β_ weight is the regularisation strength of the weight regularisation . **C)** Mutual information matrix for a high scoring model. **D)** _β_ -VAE MIG scores. Adding a ReLU improves MIG scores. **E)** MIG score against _R_[2] shows models with our constraints lie in the Goldilocks region of high disentanglement and high reconstruction. All learning curves show mean and standard error from 5 random seeds. Results from an additional dataset in Fig. 13 

representations are commonly observed to factorise into single cells, there are situations in which selectivity spans across multiple task variables (Boccara et al., 2019; Hardcastle et al., 2017). For example, sometimes spatial firing patterns of GCs are warped by reward (Boccara et al., 2019) and sometimes they are not (Butler et al., 2019). There is no theory for explaining why and when this happens. 

**A factorised task for rodents.** We consider a task in which rodents must know where they are in space, but must also approach one of multiple objects. If objects appear in different places in different contexts, the task is factorised into independent factors (Fig. 6C): ‘Where am I in allocentric spatial coordinates?’ and ‘Where am I in object-centric coordinates?’. By contrast, if objects always appear in the same locations, the task is not factorised (as spatial location can predict object location). Formally, our task requires predicting spatial location, _**x**_ , whether an object is observed, _**o**_ , and the optimal action, _**a**_ . If objects move between tasks, then _p_ ( _**x** ,_ _**a** ,_ _**o**_ ) = _p_ ( _**x**_ ) _p_ ( _**a** ,_ _**o**_ ), where _**o**_ and _**a**_ are not factored since optimal actions are dependent on objects (see Appendix A.9 for details). Our theory says the representation will have two subspaces - one for allocentric location (for predicting _**x**_ ) and one for location relative to objects (for predicting _**o**_ and _**a**_ ) - and that these sub-spaces should be represented in separate neural populations when biological constraints are present. 

The representation in rodent brains indeed has two distinct modules of non-overlapping cell populations: (1) GCs (Hafting et al., 2005) which represent allocentric space via hexagonal firing patterns (Fig. 6A); and (2) OVCs (Høydal et al., 2019) which represent relative location to objects through firing fields at specific relative distances and orientations (Fig. 6B). 

**Model with additional structural constraint.** Predicting allocentric spatial locations from egocentric self-motion cues is known as path integration (Burak & Fiete, 2009), and is believed to be a fundamental function of entorhinal cortex (where GCs and OVCs are found). GCs naturally emerge from training RNNs to path integrate under several additional biological constraints (Sorscher et al., 2019; 2020; Banino et al., 2018; Cueva & Wei, 2018). Hence to model this task (with locations _and_ objects) we could train an RNN, _**z**_ , that predicts (1) what the spatial location, _**x**_ , will be and (2) whether we will encounter an object, after an action, _**a**_ , from the current location, and (3) what the expected action, _**a**_ , will be. However, here we adopt a far more general framework that does not limit future applications of our approach simply to sequential integration problems. 

In particular, it was recently shown (Gao et al., 2021) that path integration constraints can be applied directly on the representation by adding a new constraint in the loss imposing 

**==> picture [252 x 11] intentionally omitted <==**

Here _f_ ( _·_ ) is an activation function and _**Wa**_ is a weight matrix that depends on the action _**a**_ . This surrogate constraint imposes potential path integration by ensuring that a motion _**a**_ in space _**x**_ imposes a lawful change in neural representation _**z**_ , thereby transforming the sequential path integration problem into the problem of directly estimating neural representations of space (see Appendix A.9 for more details). Thus we minimise: 

_L_ = _L_ nonneg + _L_ activity + _L_ weight + _L_ location + _L_ actions + _L_ objects + _L_ path integration (4) � ~~�~~ � ~~� � �� � � �� �~~ Biological constraints Functional constraints Structural constraints 

6 

Published as a conference paper at ICLR 2023 

**==> picture [393 x 161] intentionally omitted <==**

Figure 6: **Modules of distinct cell types form with nonnegativity and factorised tasks. A)** When rodents navigate environments with objects, GCs encode location in physical space with firing fields lying on a hexagonal lattice, while **B)** OVCs encode relative location to objects with firing fields at specific distances and orientations from (white) objects. These plots are ratemaps; the average firing of a given cell at every location. **C)** Top: To model these cells we use a task environment where objects move location in different contexts - space and objects are factorised. Bottom: We train a representation to predict 1) spatial location, 2) object location, and 3) correct action at every location. **D-E)** Model ratemaps when trained _with_ a ReLU activation function. Task 1 contains no objects, while task 2 has several objects (white dots). We see two types of cell representation: **D)** GCs that do not change across tasks and **E)** OVCs that only appear in the presence of objects. **F)** Model ratemaps when trained _without_ ReLu activation. All representations are multi-peaked but amorphous. Further cells representations shown in Fig. 14. **G)** To quantify modules in the ReLu model, we compute the distribution of individual cell spatial correlations across different tasks. **H)** The mode with high spatial correlation are cells that have high grid-score (Barry et al., 2012) and are grid cells (GCs), the mode with low spatial correlation are cells that respond similarly around objects (OVCs). **I)** Only one mode of cells is seen without a ReLu activation. **J)** To quantify module-ness over many random seeds, we compute the cosine distance between the population’s contribution to _**x**_ and _**o**_ . This is done by taking the absolute value of weights projecting from _**z**_ to _**x**_ and _**o**_ , then summing over the space/object dimension (to obtain a vector the same dimension as _**z**_ ), then computing the cosine distance. We see low cosine distance for the ReLu indicating different cells code for space vs objects - i.e. modules. 

These are the same biological constraints as above, but now the functional constraints involve predicting location, object, and action, and an additional structural constraint imposes equation 3. Interestingly, the structural constraint leads to a pattern forming optimisation dynamics (see Appendix A.9 for mathematical details). 

**Modules of distinct cell types when tasks are factorised and representations are nonnegative.** Just as our theory predicts, when training on tasks where objects and space are factorised (i.e. objects can be anywhere in space), under our biological constraints of nonnegativity and energy efficiency, distinct neural modules emerge, each selective for a single task factor (Fig. 6D-E). We see GC-like neurons that consistently represent space independent of object locations, and OVC-like neurons that recenter their representations around the moving objects or are inactive if no objects are present (further cells are shown in Fig. 14). Whereas without the nonnegativity constraint, all cells look qualitatively similar - a single module of multi-peaked amorphous cells (Fig. 6F). To quantify whether a population really has two distinct cell types (two modules) we analyse the consistency of a cell’s representation by taking its average spatial correlation between many different object configurations (Fig. 6G-I). In the ReLu case, there are two modes (Fig. 6G-I) showing a double dissociation: the mode containing cells that don’t change have high grid-score (Barry et al., 2012) and do not have consistent activity around objects. These are GCs. Whereas the mode containing cells that change between tasks have low grid-score and respond consistently around objects (Fig. 6H). These cells respond to objects and are comparable to OVCs. 

7 

Published as a conference paper at ICLR 2023 

**==> picture [393 x 111] intentionally omitted <==**

Figure 7: **Entangled tasks lead to entangled representations and grid cell warping.** We show a representative selection of cells from a model with **A)** a factorised task (as in Fig. 6) and **B)** an entangled task. The phases of the firing fields in the entangled task are locked to object location - they have warped their firing fields. This is not the case for the factorised task (asides from object specific cells). **C)** To quantify phase locking for each of the task/model variant, we compute the average spatial correlation of patches around objects. Only the entangled task shows high correlation, i.e. the cell representations have warped around objects. Each point is a model trained from a random seed. 

**Grid cell warping and mixed-selectivity when tasks are entangled.** Experimental results show GCs sometimes warp their firing fields towards rewarded locations (Boccara et al., 2019) and sometimes don’t (Butler et al., 2019). Intriguingly, in the warping situation, the rodents exhibited stereotyped behaviour; sequentially running between rewards using the same spatial trajectories rather than freely exploring the space (i.e. behaviour is entangled with space). We now explain these neuroscience observations as a consequence of space becoming entangled with objects/rewards. 

Modelling factorised versus entangled tasks (objects changing locations versus always staying in the same locations), produces very different GC behaviours. In the factorised case, grid fields are unrelated to objects (Fig. 7A), whereas in the entangled task grid fields warp to objects (Fig. 7B). We quantify this by measuring the average spatial correlation of patches around each object. Only when the task is entangled are fields consistently warped towards objects (Fig. 7C). Thus we have an explanation for GC warping; they warp when space can no longer be disentangled from other factors (e.g. objects or behaviour) in behavioural tasks. 

## 5 DISCUSSION 

We have proven that simple biological constraints like nonnegativity and energy efficiency lead to disentanglement, and empirically verified this in machine learning and neuroscience tasks, leading to a new understanding of functional cell types. We now consider some more neuroscience implications. 

**Representing categories.** Our theory additionally says that representations of individual categories should be encoded in separate neural populations (disentangled; see Appendix A.7[4] .). This provides a potential explanation for ”grandmother cells” that selectively represent specific concepts or categories (Quiroga et al., 2005), and have long puzzled proponents of distributed representations It further potentially explains situations where animals have been trained on multiple tasks, and different neurons are found to engage in each task (Rainer et al., 1998; Roy et al., 2010; Asaad et al., 2000; Lee et al., 2022; Flesch et al., 2022). We note that while our theory says you need at least one neuron per concept that is read-out (true even without disentanglement), it does not say you need a neuron for every possible concept - only for ones that are explicitly read-out. 

**When to disentangle?** Our theory speaks to situations in which brains or networks must generalise to new combinations of learnt factors. In this situation, if the input-output (or input-latent-output) transformations are linear, biological constraints will cause complete disentanglement of the networks. When the mappings are nonlinear, we show empirically that mixed-selectivity exists, but gradually de-mixes as layers approach the output (in supervised), or latent (in unsupervised), layers. 

> 4 . 

> 4We note this phenomena could also be accounted for with a sparsity constraint. 

8 

Published as a conference paper at ICLR 2023 

Optimising for low firing contrasts with previous ideas which instead optimise for linear read-out. This latter situation is akin to kernel regression, where mixed-selectivity through random expansion increases the dimensionality of neural representations, allowing simple linear read-outs in the high dimensional space to perform arbitrary nonlinear operations on the original low dimensional space. 

**Mixed-selectivity.** Mixed-selectivity exists in the brain. For example, Kenyon cells in the Drosophila mushroom body increase the dimensionality of their inputs by an order of magnitude by close to random projections (Aso et al., 2014). This may allow linear read-out to behaviour via simple dopamine gating. Similarly rodent hippocampal cells encode conjunctions of spatial and sensory variables to allow rapid formation of new memories (Komorowski et al., 2009)]. More recently it has been suggested that PFC neurons have this same property, for the same reason (Rigotti et al., 2013). However, it is less clear that this is a general property of representations in associative cortex (including PFC), which can separate into different neuronal representations of different interpretable factors (Hirokawa et al., 2019; Bernardi et al., 2020) or tasks (Lee et al., 2022; Flesch et al., 2022). 

One possibility is that in overtrained situations with only a relatively small number of categories or trial-types (where mixed-selectivity has been observed), the task can effectively be solved by categorising the current trial into one of a few previous experiences. By contrast in tasks where combinatorial generalisation is required, the factored solution may be preferred. 

**A program to understand how brain representations structure themselves.** This work is one piece of the puzzle. It tells us when neural circuits systems should represent different factors in different neurons. It does not tell us, however, how each factor itself should be represented. For example it does not tell us why GCs and OVCs look the ways they do. We believe that the same principles of nonnegativity, minimising neural activity, and representing structure, will be essential components obtaining this more general understanding. Indeed in a companion paper, we use the same constraints, along with formalising structure/path-integration using group and representations theory, to mathematically understand why grid cells look like grid cells (Dorrell et al., 2023). Similarly, our current understanding is limited to the optimal solution for factorised representations, but we anticipate similar ideas will be applicable to neural dynamics (Driscoll et al., 2022). 

## 6 CONCLUSION 

We introduced constraints inspired by biological neurons - nonnegativity and energy efficiency (w.r.t. either activity or weights) - and proved these constraints lead to linear factorised codes being disentangled. We empirically verified this in simulation, and showed the same constraints lead to disentanglement with both nonlinear data and nonlinear networks. We even achieve competitive disentanglement scores on a baseline disentanglement task, even though this was not our specific aim. We showed these biological constraints explain why neuroscientists observe bespoke cell types, e.g. GCs (Hafting et al., 2005), OVCs (Høydal et al., 2019), border vector cells (Solstad et al., 2008; Lever et al., 2009), since space, boundaries, and objects appear in a factorised form (i.e. occur in any independent combination), and so are optimally represented by different neural populations for each factor. These same principles explain why neurons in inferior temporal cortex are axis aligned to underlying factors of variation that generate the data they represent (Chang & Tsao, 2017; Bao et al., 2020; Higgins et al., 2021), why visual cortex neurons are decorrelated (Ecker et al., 2010), or why neurons in parietal cortex only selective for specific tasks (Lee et al., 2022). Lastly, we also explained the confusing finding of grid fields warping towards rewards (Boccara et al., 2019) as the space and rewards becoming entangled. 

This work bridges the gap between single neuron and population responses, and offers an understanding of properties of neural representations in terms of task structure above and beyond just dimensionality. Additionally it demonstrates the utility of neurobiological considerations in designing machine learning algorithms. Overall, we hope this work demonstrates the promise of a unified research program that more deeply connects the neuroscience and machine learning communities to help in their combined quest to both understand and learn neural representations. Such a unified approach spanning brains and machines could help both sides, offering neuroscientists a deeper understanding of how cortical representations structure themselves, and offering machine learners novel ways to control and understand the representations their machines learn. 

9 

Published as a conference paper at ICLR 2023 

## ACKNOWLEDGEMENTS 

We thank Emile Mathieu and Andrew Saxe for helpful comments and advice on our manuscript. We thank the following funding sources: Sir Henry Wellcome Post-doctoral Fellowship (222817/Z/21/Z) to J.C.R.W.; the Gatsby Charitable Foundation to W.D.; the James S. McDonnell, Simons Foundations, NTT Research, and an NSF CAREER Award to S.G.; Wellcome Principal Research Fellowship (219525/Z/19/Z), Wellcome Collaborator award (214314/Z/18/Z), and JeanFranc¸ois and Marie-Laure de Clermont-Tonnerre Foundation award (JSMF220020372) to T.E.J.B.; the Wellcome Centre for Integrative Neuroimaging and Wellcome Centre for Human Neuroimaging are each supported by core funding from the Wellcome Trust (203139/Z/16/Z, 203147/Z/16/Z). 

10 

Published as a conference paper at ICLR 2023 

## REFERENCES 

- Wael F. Asaad, Gregor Rainer, and Earl K. Miller. Task-Specific Neural Activity in the Primate Prefrontal Cortex. _Journal of Neurophysiology_ , 84(1):451–459, July 2000. doi: 10.1152/jn. 2000.84.1.451. URL https://journals.physiology.org/doi/full/10.1152/ jn.2000.84.1.451. 

- Yoshinori Aso, Daisuke Hattori, Yang Yu, Rebecca M Johnston, Nirmala A Iyer, Teri-TB Ngo, Heather Dionne, LF Abbott, Richard Axel, Hiromu Tanimoto, and Gerald M Rubin. The neuronal architecture of the mushroom body provides a logic for associative learning. _eLife_ , 3:e04577, December 2014. doi: 10.7554/eLife.04577. URL https://doi.org/10.7554/eLife. 04577. 

- Andrea Banino, Caswell Barry, Benigno Uria, Charles Blundell, Timothy Lillicrap, Piotr Mirowski, Alexander Pritzel, Martin J Chadwick, Thomas Degris, Joseph Modayil, Greg Wayne, Hubert Soyer, Fabio Viola, Brian Zhang, Ross Goroshin, Neil Rabinowitz, Razvan Pascanu, Charlie Beattie, Stig Petersen, Amir Sadik, Stephen Gaffney, Helen King, Koray Kavukcuoglu, Demis Hassabis, Raia Hadsell, and Dharshan Kumaran. Vector-based navigation using grid-like representations in artificial agents. _Nature_ , 557(7705):429–433, May 2018. doi: 10.1038/s41586-018-0102-6. URL http://www.nature.com/articles/ s41586-018-0102-6. 

- Pinglei Bao, Liang She, Mason McGill, and Doris Y. Tsao. A map of object space in primate inferotemporal cortex. _Nature_ , 583(7814):103–108, July 2020. doi: 10.1038/s41586-020-2350-5. URL https://doi.org/10.1038/s41586-020-2350-5. 

- David L. Barack and John W. Krakauer. Two views on the cognitive brain. _Nature Reviews Neuroscience_ , 22(6):359–371, June 2021. doi: 10.1038/s41583-021-00448-6. URL https: //www.nature.com/articles/s41583-021-00448-6. 

- Adrien Bardes, Jean Ponce, and Yann LeCun. VICReg: Variance-Invariance-Covariance Regularization for Self-Supervised Learning. _arXiv preprint_ , January 2022. URL http://arxiv. org/abs/2105.04906. 

- H. B. Barlow. Possible Principles Underlying the Transformations of Sensory Messages. In Walter A. Rosenblith (ed.), _Sensory Communication_ , pp. 216–234. The MIT Press, 1961. doi: 10.7551/mitpress/9780262518420.003.0013. URL https://academic.oup.com/ mit-press-scholarship-online/book/20714/chapter/180090664. 

- H B Barlow. Single Units and Sensation: A Neuron Doctrine for Perceptual Psychology? _Perception_ , 1(4):371–394, December 1972. doi: 10.1068/p010371. URL https://doi.org/10. 1068/p010371. 

- C. Barry, L. L. Ginzberg, J. O’Keefe, and N. Burgess. Grid cell firing patterns signal environmental novelty by expansion. _Proceedings of the National Academy of Sciences_ , 109(43):17687– 17692, 2012. doi: 10.1073/pnas.1209918109. URL http://www.pnas.org/cgi/doi/ 10.1073/pnas.1209918109. 

- David Bau, Bolei Zhou, Aditya Khosla, Aude Oliva, and Antonio Torralba. Network Dissection: Quantifying Interpretability of Deep Visual Representations, April 2017. URL http: //arxiv.org/abs/1704.05796. 

- Timothy E J Behrens, Timothy H Muller, James C. R. Whittington, Shirley Mark, Alon B Baram, Kimberly L Stachenfeld, and Zeb Kurth-nelson. What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior. _Neuron_ , 100(2):490–509, 2018. doi: 10.1016/j.neuron.2018.10.002. URL https://www.cell.com/neuron/fulltext/S0896-6273(18)30856-0. 

- Yoshua Bengio, Aaron Courville, and Pascal Vincent. Representation learning: A review and new perspectives. _arXiv preprint_ , (1993):1–34, 2012. doi: 3C2DBCEE-8A96-493B-B88B-36B1F52ECA58. URL http://arxiv.org/abs/1206. 5538{%}5Cnhttps://s3-us-west-2.amazonaws.com/mlsurveys/110.pdf. 

11 

Published as a conference paper at ICLR 2023 

- Silvia Bernardi, Marcus K. Benna, Mattia Rigotti, J´erˆome Munuera, Stefano Fusi, and C. Daniel Salzman. The Geometry of Abstraction in the Hippocampus and Prefrontal Cortex. _Cell_ , 183(4):954–967.e21, November 2020. doi: 10.1016/j.cell.2020.09.031. URL https:// linkinghub.elsevier.com/retrieve/pii/S0092867420312289. 

- Charlotte N. Boccara, Michele Nardin, Federico Stella, Joseph O’Neill, and Jozsef Csicsvari. The entorhinal cognitive map is attracted to goals. _Science_ , 363(6434):1443–1447, March 2019. doi: 10.1126/science.aav4837. URL http://www.sciencemag.org/lookup/doi/10. 1126/science.aav4837. 

- Blake Bordelon and Cengiz Pehlevan. Population codes enable learning from few examples by shaping inductive bias, March 2022. URL https://www.biorxiv.org/content/10. 1101/2021.03.30.437743v3. 

- Bariscan Bozkurt, Cengiz Pehlevan, and Alper T. Erdogan. Biologically-Plausible Determinant Maximization Neural Networks for Blind Separation of Correlated Sources, September 2022. URL http://arxiv.org/abs/2209.12894. 

- Yoram Burak and Ila R. Fiete. Accurate path integration in continuous attractor network models of grid cells. _PLoS Computational Biology_ , 5(2):e1000291, February 2009. doi: 10.1371/journal. pcbi.1000291. URL https://dx.plos.org/10.1371/journal.pcbi.1000291. 

- Christopher P. Burgess, Irina Higgins, Arka Pal, Loic Matthey, Nick Watters, Guillaume Desjardins, and Alexander Lerchner. Understanding disentangling in $ _\_ beta$-VAE. _arXiv preprint_ , April 2018. doi: 10.48550/arXiv.1804.03599. URL http://arxiv.org/abs/1804.03599. 

- William N. Butler, Kiah Hardcastle, and Lisa M. Giocomo. Remembered reward locations restructure entorhinal spatial maps. _Science_ , 363(6434):1447–1452, March 2019. doi: 10.1126/science. aav5297. URL http://www.sciencemag.org/lookup/doi/10.1126/science. aav5297. 

- Stephen Casper, Shlomi Hod, Daniel Filan, Cody Wild, Andrew Critch, and Stuart Russell. Graphical Clusterability and Local Specialization in Deep Neural Networks. April 2022. URL https://openreview.net/forum?id=HreeeJvkue9. 

- Le Chang and Doris Y. Tsao. The Code for Facial Identity in the Primate Brain. _Cell_ , 169(6): 1013–1028.e14, June 2017. doi: 10.1016/j.cell.2017.05.011. URL http://dx.doi.org/ 10.1016/j.cell.2017.05.011. 

- Ricky T. Q. Chen, Xuechen Li, Roger B Grosse, and David K Duvenaud. Isolating Sources of Disentanglement in Variational Autoencoders. _Advances in Neural Information Processing Systems_ , 31, 2018. URL https://proceedings.neurips.cc/paper/2018/hash/ 1ee3dfcd8a0645a25a35977997223d22-Abstract.html. 

- Chaitanya Chintaluri and Tim P. Vogels. Metabolically driven action potentials serve neuronal energy homeostasis and protect from reactive oxygen species, October 2022. URL https: //www.biorxiv.org/content/10.1101/2022.10.16.512428v1. 

- Pierre Comon. Independent component analysis, A new concept? _Signal Processing_ , 36 (3):287–314, April 1994. doi: 10.1016/0165-1684(94)90029-9. URL https://www. sciencedirect.com/science/article/pii/0165168494900299. 

- Christopher J. Cueva and Xue-Xin Wei. Emergence of grid-like representations by training recurrent neural networks to perform spatial localization. _International Conference on Learning Representations_ , 0:1–19, March 2018. URL http://arxiv.org/abs/1803.07770. 

- Sachin S Deshmukh and James J Knierim. Influence of local objects on hippocampal representations: Landmark vectors and memory. _Hippocampus_ , 23(4):253–67, April 2013. doi: 10.1002/hipo.22101. URL http://www.ncbi.nlm.nih.gov/pubmed/23447419. 

- Yedidyah Dordek, Daniel Soudry, Ron Meir, and Dori Derdikman. Extracting grid cell characteristics from place cell inputs using non-negative principal component analysis. _eLife_ , 5 (MARCH2016):1–36, 2016. doi: 10.7554/eLife.10094. 

12 

Published as a conference paper at ICLR 2023 

- Will Dorrell, Peter E. Latham, Timothy E. J. Behrens, and James C. R. Whittington. Actionable Neural Representations: Grid Cells from Minimal Constraints. In _International Conference on Learning Representations_ , 2023. URL https://openreview.net/forum?id= xfqDe72zh41. 

- Laura Driscoll, Krishna Shenoy, and David Sussillo. Flexible multitask computation in recurrent networks utilizes shared dynamical motifs. preprint, Neuroscience, August 2022. URL http: //biorxiv.org/lookup/doi/10.1101/2022.08.15.503870. 

- Alexander S. Ecker, Philipp Berens, Georgios A. Keliris, Matthias Bethge, Nikos K. Logothetis, and Andreas S. Tolias. Decorrelated Neuronal Firing in Cortical Microcircuits. _Science_ , 327(5965): 584–587, January 2010. doi: 10.1126/science.1179867. URL https://www.science. org/doi/abs/10.1126/science.1179867. 

- Nelson Elhage, Tristan Hume, Catherine Olsson, Nicholas Schiefer, Tom Henighan, Shauna Kravec, Zac Hatfield-Dodds, Robert Lasenby, Dawn Drain, Carol Chen, Roger Grosse, Sam McCandlish, Jared Kaplan, Dario Amodei, Martin Wattenberg, and Christopher Olah. Toy Models of Superposition, September 2022. URL http://arxiv.org/abs/2209.10652. 

- Yuguang Fang, K.A. Loparo, and Xiangbo Feng. Inequalities for the trace of matrix product. _IEEE Transactions on Automatic Control_ , 39(12):2489–2490, December 1994. doi: 10.1109/9.362841. URL https://ieeexplore.ieee.org/document/362841/. 

- Timo Flesch, Keno Juechems, Tsvetomira Dumbalska, Andrew Saxe, and Christopher Summerfield. Orthogonal representations for robust context-dependent task performance in brains and neural networks. _Neuron_ , 110(7):1258–1270.e11, 2022. doi: 10.1016/j.neuron.2022.01.005. URL https://doi.org/10.1016/j.neuron.2022.01.005. 

- Peiran Gao, Eric Trautmann, Byron M. Yu, Gopal Santhanam, Stephen I. Ryu, Krishna V. Shenoy, and Surya Ganguli. A theory of multineuronal dimensionality, dynamics and measurement. _bioRxiv preprint_ , 0:214262, 2017. doi: 10.1101/214262. URL https://www.biorxiv. org/content/early/2017/11/05/214262. 

- Ruiqi Gao, Jianwen Xie, Xue-Xin Wei, Song-Chun Zhu, and Ying Nian Wu. On Path Integration of Grid Cells: Group Representation and Isotropic Scaling. _Advances in Neural Information Processing Systems 35_ , 0(NeurIPS):1–28, June 2021. URL http://arxiv.org/abs/2006. 10259. 

- Jeffrey L. Gauthier and David W. Tank. A Dedicated Population for Reward Coding in the Hippocampus. _Neuron_ , 99(1):179–193.e7, 2018. doi: 10.1016/j.neuron.2018.06.008. URL https://doi.org/10.1016/j.neuron.2018.06.008. 

- Gabriel Goh, Nick Cammarata †, Chelsea Voss †, Shan Carter, Michael Petrov, Ludwig Schubert, Alec Radford, and Chris Olah. Multimodal Neurons in Artificial Neural Networks. _Distill_ , 2021. doi: 10.23915/distill.00030. 

- Merse E G´asp´ar, Pierre-Olivier Polack, Peyman Golshani, M´at´e Lengyel, and Gerg˝o Orb´an. Representational untangling by the firing rate nonlinearity in V1 simple cells. _eLife_ , 8:e43625, September 2019. doi: 10.7554/eLife.43625. URL https://elifesciences.org/articles/ 43625. 

- Torkel Hafting, Marianne Fyhn, Sturla Molden, May-britt Britt Moser, and Edvard I. Moser. Microstructure of a spatial map in the entorhinal cortex. _Nature_ , 436(7052):801–806, 2005. doi: 10.1038/nature03721. 

- Kiah Hardcastle, Niru Maheswaranathan, Surya Ganguli, and Lisa M. Giocomo. A Multiplexed, Heterogeneous, and Adaptive Code for Navigation in Medial Entorhinal Cortex. _Neuron_ , 94 (2):375–387.e7, 2017. doi: 10.1016/j.neuron.2017.03.025. URL http://dx.doi.org/10. 1016/j.neuron.2017.03.025. 

- Irina Higgins, Loic Matthey, Arka Pal, Christopher Burgess, Xavier Glorot, Matthew Botvinick, Shakir Mohamed, and Alexander Lerchner. beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. _International Conference on Learning Representations_ , 0, July 2017a. URL https://openreview.net/forum?id=Sy2fzU9gl. 

13 

Published as a conference paper at ICLR 2023 

- Irina Higgins, Arka Pal, Andrei A. Rusu, Loic Matthey, Christopher P Burgess, Alexander Pritzel, Matthew Botvinick, Charles Blundell, and Alexander Lerchner. DARLA: Improving Zero-Shot Transfer in Reinforcement Learning. _arXiv preprint_ , 2017b. doi: 10.3109/17482620903223036. URL http://arxiv.org/abs/1707.08475. 

- Irina Higgins, Nicolas Sonnerat, Loic Matthey, Arka Pal, Christopher P Burgess, Matko Bosnjak, Murray Shanahan, Matthew Botvinick, Demis Hassabis, and Alexander Lerchner. SCAN: Learning Hierarchical Compositional Visual Concepts. _arXiv preprint_ , pp. 1–24, 2018. doi: 10.1186/s12884-017-1520-4. URL http://arxiv.org/abs/1707.03389. 

- Irina Higgins, Le Chang, Victoria Langston, Demis Hassabis, Christopher Summerfield, Doris Tsao, and Matthew Botvinick. Unsupervised deep learning identifies semantic disentanglement in single inferotemporal face patch neurons. _Nature Communications_ , 12(1):1–14, 2021. doi: 10.1038/ s41467-021-26751-5. 

- Geoffrey E. Hinton, Alex Krizhevsky, and Sida D. Wang. Transforming Auto-Encoders. _International Conference on Artificial Neural Networks_ , 6791:44–51, 2011. doi: 10.1007/978-3-642-21735-7 ~~6~~ . URL http://link.springer.com/10.1007/ 978-3-642-21735-7_6. 

- Junya Hirokawa, Alexander Vaughan, Paul Masset, Torben Ott, and Adam Kepecs. Frontal cortex neuron types categorically encode single decision variables. _Nature_ , 576(7787):446–451, December 2019. doi: 10.1038/s41586-019-1816-9. URL https://www.nature.com/ articles/s41586-019-1816-9. 

- Daniella Horan, Eitan Richardson, and Yair Weiss. When Is Unsupervised Disentanglement Possible? _Advances in Neural Information Processing Systems_ , 34:5150– 5161, 2021. URL https://proceedings.neurips.cc/paper/2021/hash/ 29586cb449c90e249f1f09a0a4ee245a-Abstract.html. 

- A. Hyv¨arinen and E. Oja. Independent component analysis: algorithms and applications. _Neural Networks_ , 13(4):411–430, June 2000. doi: 10.1016/S0893-6080(00)00026-5. URL https: //www.sciencedirect.com/science/article/pii/S0893608000000265. 

- A Hyv¨arinen, Erkki Oja, Aapo Hyv, Erkki Oja, A Hyv¨arinen, and Erkki Oja. Independent component analysis: A tutorial. _Notes for International Joint Conference on Neural Networks (IJCNN’99), Washington DC_ , 1:1–30, 1999. doi: 10.1093/mnras/stv2744. URL http://scholar.google.com/scholar?q=related:qM2Iwk0laFQJ: scholar.google.com/{&}hl=en{&}num=20{&}as{_}sdt=0,5{%}5Cnfile: ///Users/tsmoon/Documents/PapersBak/Articles/1999/Hyv?rinen/ NotesforInternationalJointConferenceonNeuralNetworks(IJCNN?99) WashingtonDC1. 

- Øyvind Arne Høydal, Emilie Ranheim Skytøen, Sebastian Ola Andersson, May-Britt Moser, and Edvard Ingjald Moser. Object-vector coding in the medial entorhinal cortex. _Nature_ , 568(7752): 400–404, April 2019. doi: 10.1038/s41586-019-1077-7. URL http://www.nature.com/ articles/s41586-019-1077-7. 

- Ilyes Khemakhem, Diederik Kingma, Ricardo Monti, and Aapo Hyvarinen. Variational Autoencoders and Nonlinear ICA: A Unifying Framework. _Proceedings of the Twenty Third International Conference on Artificial Intelligence and Statistics_ , pp. 2207–2217, June 2020. URL https://proceedings.mlr.press/v108/khemakhem20a.html. 

- Hyunjik Kim and Andriy Mnih. Disentangling by Factorising. _Proceedings of the 35th International Conference on Machine Learning_ , pp. 2649–2658, July 2018. URL https://proceedings. mlr.press/v80/kim18b.html. 

- Diederik P. Kingma and Jimmy Lei Ba. Adam: A Method for Stochastic Optimization. _arXiv preprint_ , 0, 2014. doi: http://doi.acm.org.ezproxy.lib.ucf.edu/10.1145/1830483.1830503. URL http://arxiv.org/abs/1412.6980. 

14 

Published as a conference paper at ICLR 2023 

- Diederik P. Kingma and Max Welling. Auto-Encoding Variational Bayes. _arXiv preprint_ , 0(Ml): 1–14, 2013. doi: 10.1051/0004-6361/201527329. URL http://arxiv.org/abs/1312. 6114. 

- Robert W. Komorowski, Joseph R. Manns, and Howard Eichenbaum. Robust Conjunctive ItemPlace Coding by Hippocampal Neurons Parallels Learning What Happens Where. _Journal of Neuroscience_ , 29(31):9918–9929, August 2009. doi: 10.1523/JNEUROSCI.1378-09. 2009. URL https://www.jneurosci.org/lookup/doi/10.1523/JNEUROSCI. 1378-09.2009. 

- Julia Julija Krupic, Neil Burgess, John O’Keefe, and John O’Keefe. Neural Representations of Location Composed of Spatially Periodic Bands. _Science_ , 337(6096):853–857, August 2012. doi: 10. 1126/science.1222403. URL https://www.science.org/doi/10.1126/science. 1222403. 

- Abhishek Kumar, Prasanna Sattigeri, and Avinash Balakrishnan. Variational Inference of Disentangled Latent Concepts from Unlabeled Observations. _International Conference on Learning Representations_ , pp. 16, 2018. 

- Daniel Kunin, Jonathan M. Bloom, Aleksandrina Goeva, and Cotton Seed. Loss Landscapes of Regularized Linear Autoencoders. _arXiv preprint_ , 2019. URL http://arxiv.org/abs/ 1901.08168. 

- Daniel D Lee and H Sebastian Seung. Algorithms for Non-negative Matrix Factorization. _Advances in Neural Information Processing Systems_ , 0(1), 2000. 

- Julie J. Lee, Michael Krumin, Kenneth D. Harris, and Matteo Carandini. Task specificity in mouse parietal cortex. _Neuron_ , August 2022. doi: 10.1016/j.neuron.2022.07.017. URL https:// www.sciencedirect.com/science/article/pii/S0896627322006626. 

- Colin Lever, Stephen Burton, Ali Jeewajee, John O’Keefe, and Neil Burgess. Boundary vector cells in the subiculum of the hippocampal formation. _Journal of Neuroscience_ , 29(31):9771–9777, 2009. doi: 10.1523/JNEUROSCI.1319-09.2009. 

- David Lipshutz, Cengiz Pehlevan, and Dmitri B. Chklovskii. Biologically plausible single-layer networks for nonnegative independent component analysis, March 2022. URL http://arxiv. org/abs/2010.12632. 

- Francesco Locatello, Stefan Bauer, Mario Lucic, Gunnar R¨atsch, Sylvain Gelly, Bernhard Sch¨olkopf, and Olivier Bachem. Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations, June 2019. URL http://arxiv.org/abs/1811. 12359. 

- Lane McIntosh, Niru Maheswaranathan, Aran Nayebi, Surya Ganguli, and Stephen Baccus. Deep Learning Models of the Retinal Response to Natural Scenes. In _Advances in Neural Information Processing Systems_ , volume 29. Curran Associates, Inc., 2016. URL https://proceedings.neurips.cc/paper/2016/hash/ a1d33d0dfec820b41b54430b50e96b5c-Abstract.html. 

- Samuel Ocko, Jack Lindsey, Surya Ganguli, and Stephane Deny. The emergence of multiple retinal cell types through efficient coding of natural movies. In _Advances in Neural Information Processing Systems_ , volume 31. Curran Associates, Inc., 2018. doi: 10.1101/458737. URL https://papers.nips.cc/paper/2018/hash/ d94fd74dcde1aa553be72c1006578b23-Abstract.html. 

- Erkki Oja. Simplified neuron model as a principal component analyzer. _Journal of mathematical biology_ , 15(3):267–273, November 1982. doi: 10.1007/BF00275687. 

- John O’Keefe and J. Dostrovsky. The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. _Brain Research_ , 34(1):171–175, November 1971. doi: 10.1016/ 0006-8993(71)90358-1. URL http://linkinghub.elsevier.com/retrieve/pii/ 0006899371903581. 

15 

Published as a conference paper at ICLR 2023 

Bruno A. Olshausen and David J. Field. Emergence of simple-cell receptive field properties by learning a sparse code for natural images, 1996. 

- Cengiz Pehlevan, Tao Hu, and Dmitri B. Chklovskii. A Hebbian/Anti-Hebbian Neural Network for Linear Subspace Learning: A Derivation from Multidimensional Scaling of Streaming Data. _Neural Computation_ , 27(7):1461–1495, July 2015. doi: 10.1162/NECO ~~a 0~~ 0745. URL http: //arxiv.org/abs/1503.00669. 

- Cengiz Pehlevan, Sreyas Mohan, and Dmitri B. Chklovskii. Blind nonnegative source separation using biological neural networks. _Neural Computation_ , 29(11):2925–2954, November 2017. doi: 10.1162/neco ~~a 0~~ 1007. URL http://arxiv.org/abs/1706.00382. 

- M. Plumbley. Conditions for nonnegative independent component analysis. _IEEE Signal Processing Letters_ , 9(6):177–180, June 2002. doi: 10.1109/LSP.2002.800502. 

- M.D. Plumbley. Algorithms for nonnegative independent component analysis. _IEEE Transactions on Neural Networks_ , 14(3):534–543, May 2003. doi: 10.1109/TNN.2003.810616. 

- R. Quian Quiroga, L. Reddy, G. Kreiman, C. Koch, and I. Fried. Invariant visual representation by single neurons in the human brain. _Nature_ , 435(7045):1102–1107, June 2005. doi: 10.1038/ nature03687. URL https://www.nature.com/articles/nature03687. 

- Gregor Rainer, Wael F. Asaad, and Earl K. Miller. Selective representation of relevant information by neurons in the primate prefrontal cortex. _Nature_ , 393(6685):577–579, June 1998. doi: 10. 1038/31235. URL https://www.nature.com/articles/31235. 

- Blake A. Richards, Timothy P. Lillicrap, Philippe Beaudoin, Yoshua Bengio, Rafal Bogacz, Amelia Christensen, Claudia Clopath, Rui Ponte Costa, Archy de Berker, Surya Ganguli, Colleen J. Gillon, Danijar Hafner, Adam Kepecs, Nikolaus Kriegeskorte, Peter Latham, Grace W. Lindsay, Kenneth D. Miller, Richard Naud, Christopher C. Pack, Panayiota Poirazi, Pieter Roelfsema, Jo˜ao Sacramento, Andrew Saxe, Benjamin Scellier, Anna C. Schapiro, Walter Senn, Greg Wayne, Daniel Yamins, Friedemann Zenke, Joel Zylberberg, Denis Therien, and Konrad P. Kording. A deep learning framework for neuroscience. _Nature Neuroscience_ , 22(11):1761–1770, November 2019. doi: 10.1038/s41593-019-0520-2. URL https://www.nature.com/articles/ s41593-019-0520-2. 

- Karl Ridgeway and Michael C Mozer. Learning Deep Disentangled Embeddings With the F-Statistic Loss. _Advances in Neural Information Processing Systems_ , 31, 2018. URL https://proceedings.neurips.cc/paper/2018/hash/ 2b24d495052a8ce66358eb576b8912c8-Abstract.html. 

- Mattia Rigotti, Omri Barak, Melissa R Warden, Xiao-Jing Wang, Nathaniel D Daw, Earl K Miller, and Stefano Fusi. The importance of mixed selectivity in complex cognitive tasks. _Nature_ , 497(7451):1–6, 2013. doi: 10.1038/nature12160. URL http://dx.doi.org/10.1038/ nature12160. 

- Michal Rolinek, Dominik Zietlow, and Georg Martius. Variational Autoencoders Pursue PCA Directions (by Accident), April 2019. URL http://arxiv.org/abs/1812.06775. 

- Jefferson E. Roy, Maximilian Riesenhuber, Tomaso Poggio, and Earl K. Miller. Prefrontal Cortex Activity during Flexible Categorization. _Journal of Neuroscience_ , 30(25):8519–8528, June 2010. doi: 10.1523/JNEUROSCI.4837-09.2010. URL https://www.jneurosci.org/ content/30/25/8519. 

- Ayelet Sarel, Arseny Finkelstein, Liora Las, and Nachum Ulanovsky. Vectorial representation of spatial goals in the hippocampus of bats. _Science_ , 355(6321):176–180, 2017. doi: 10.1126/ science.aak9589. 

- Lukas Schott, Julius von K¨ugelgen, Frederik Tr¨auble, Peter Gehler, Chris Russell, Matthias Bethge, Bernhard Sch¨olkopf, Francesco Locatello, and Wieland Brendel. Visual Representation Learning Does Not Generalize Strongly Within the Same Domain, February 2022. URL http: //arxiv.org/abs/2107.08221. 

16 

Published as a conference paper at ICLR 2023 

- Trygve Solstad, Charlotte N Boccara, Emilio Kropff, May-Britt Moser, and Edvard I Moser. Representation of Geometric Borders in the Entorhinal Cortex. _Science_ , 322(5909):1865–1868, December 2008. doi: 10.1126/science.1166466. URL https://www.sciencemag.org/ lookup/doi/10.1126/science.1166466. 

- Ben Sorscher, Gabriel C Mel, Surya Ganguli, and Samuel A Ocko. A unified theory for the origin of grid cells through the lens of pattern formation. _Advances in Neural Information Processing Systems 32_ , 32(NeurIPS):10003–10013, 2019. 

- Ben Sorscher, Gabriel C Mel, Samuel A Ocko, Lisa Giocomo, and Surya Ganguli. A unified theory for the computational and mechanistic origins of grid cells. _bioRxiv preprint_ , pp. 2020.12.29.424583, 2020. URL https://doi.org/10.1101/2020.12.29.424583. 

- Carsen Stringer, Marius Pachitariu, Nicholas Steinmetz, Matteo Carandini, and Kenneth D. Harris. High-dimensional geometry of population responses in visual cortex. _Nature_ , 2019. doi: 10.1038/ s41586-019-1346-5. URL http://dx.doi.org/10.1038/s41586-019-1346-5. 

- James C. R. Whittington, Rishabh Kabra, Loic Matthey, Christopher P. Burgess, and Alexander Lerchner. Constellation: Learning relational abstractions over objects for compositional imagination. _arXiv preprint_ , 2021a. URL http://arxiv.org/abs/2107.11153. 

- James C. R. Whittington, Joseph Warren, and Tim E. J. Behrens. Relating transformers to models and neural representations of the hippocampal formation. _International Conference on Learning Representations_ , September 2021b. URL https://openreview.net/pdf?id= B8DVo9B1YE0. 

- Daniel L K Yamins, Ha Hong, Charles F. Cadieu, Ethan A. Solomon, Darren Seibert, and James J. DiCarlo. Performance-optimized hierarchical models predict neural responses in higher visual cortex. _Proceedings of the National Academy of Sciences of the United States of America_ , 111 (23):8619–8624, 2014. doi: 10.1073/pnas.1403112111. 

- Guangyu Robert Yang, Madhura R. Joglekar, H. Francis Song, William T. Newsome, and XiaoJing Wang. Task representations in neural networks trained to perform many cognitive tasks. _Nature Neuroscience_ , 22(2):297–306, February 2019. doi: 10.1038/s41593-018-0310-2. URL https://www.nature.com/articles/s41593-018-0310-2. 

- Ilker Yildirim, Mario Belledonne, Winrich Freiwald, and Josh Tenenbaum. Efficient inverse graphics in biological face processing. _Science Advances_ , 6(10):eaax5979, March 2020. doi: 10.1126/sciadv.aax5979. URL https://www.science.org/doi/10.1126/sciadv. aax5979. 

- Dominik Zietlow, Michal Rolinek, and Georg Martius. Demystifying Inductive Biases for (Beta)VAE Based Architectures. In _Proceedings of the 38th International Conference on Machine Learning_ , pp. 12945–12954. PMLR, July 2021. URL https://proceedings.mlr. press/v139/zietlow21a.html. 

17 

Published as a conference paper at ICLR 2023 

## A APPENDIX 

## A.1 DEFINITIONS 

**Disentanglement definition** . We define disentanglement as when single _model_ neurons care about single ground truth factors. We do not mind if more than one model neuron cares about the same factor. We note that other definitions of disentanglement are when _single_ ground truth factors of variation are encoded in at most a _single_ model neuron - we do not ask for this level of parsimony. 

**Disentanglement metric** . Our metric (mutual information ratio; MIR) measures the mutual information between neurons and factors, I _n,f_ , then calculates each neuron’s preference (we exclude inactive neurons) for one factor over the rest via 

**==> picture [236 x 26] intentionally omitted <==**

We then divide by the number of (active) neurons, _nn_ , and normalise for the number of factors, _nf_ , i.e. 

**==> picture [244 x 34] intentionally omitted <==**

High MIR means single neurons show high preference for a single ground truth factor. 

We do not propose this metric as a gold-standard metric for disentanglement, indeed in some situations such as spiral shaped functions, it could exhibit pathological properties. Furthermore since our metric is normalised by the sum mutual information of all factors, rather than the just the gap between the factors with 1[st] and 2[nd] highest MI (like the MIG metric), it appears lower even when with near perfect disentanglement. However in our situations it works just fine. Again, we use it over other metrics since other metrics penalise situations where more than one neuron codes for a ground-truth factor. 

18 

Published as a conference paper at ICLR 2023 

## A.2 RELATED WORK 

Here we review the literature on disentanglement and the use of biological constraints, in both machines and in the brain, and where possible relate back to the work presented in this paper. 

While there are many technique for learning linear features of data, by far the most relevant to this work is independent component analysis (ICA), though we briefly mention principal component analysis (PCA) here too. ICA seeks to learn source signals in data that are maximally independent (Comon, 1994), and there exist algorithms (Hyv¨arinen & Oja, 2000) that provably extract these components when the underlying sources are linearly mixed in the observed data (provided the sources are non-gaussian). PCA, on the other hand, aims to find the minimally correlated components of the signal that explain the most variance, and simple algorithms exist for PCA too. 

## A.2.1 LINEAR DISENTANGLEMENT 

PCA can be done in neural hardware too. Oja’s rule (Oja, 1982)) is a simple learning rule that learns principle components sequentially. More recently, neural algorithms for learning the principal components non-sequentially have been developed, either using Hebbian/anti-Hebbian learning rules in biological networks (Pehlevan et al., 2015) or specific weight regularization in linear autoencoders (Kunin et al., 2019). 

Neural algorithms for ICA also exist. These draw on ideas from nonnegative ICA (Plumbley, 2002; 2003) - where the sources are assumed to be nonnegative - and use a similarity matching objective to derive biologically plausible networks for ICA (Lipshutz et al., 2022; Pehlevan et al., 2017), with this extendable to correlated sources (Bozkurt et al., 2022). These works relate to ours as they consider nonnegativity, however their focus is on biological neural networks implementing _linear_ ICA, whereas we mathematically prove biological constraints including nonnegativity lead to source separation in linear ICA, and empirically show that the same is true from _nonlinear_ ICA. 

## A.2.2 NONLINEAR DISENTANGLEMENT 

There exist no known algorithm for _exact_ source recovery (‘identifying’ the sources) when the factors are nonlinearly mixed. Indeed it is provably the case that nonlinear ICA is not identifiable (Hyv¨arinen et al., 1999). 

Nevertheless, there have many methods for disentanglement in _nonlinear_ models, with most modern methods use variational autoencoders (VAE; Kingma & Welling (2013)), with various choices that promote explicit factorisation of the learned latent space. For example _β_ -VAEs (Higgins et al., 2017a) up-weight (by _β_ ) the term in the VAE loss that encourages the posterior to be a factorised distribution. Other variations of disentanglement VAEs (Burgess et al., 2018; Kim & Mnih, 2018; Ridgeway & Mozer, 2018; Kumar et al., 2018; Chen et al., 2018) similarly try to explicitly enforce a factorised aggregate posterior. 

Importantly, analogously to the nonlinear ICA case, it has been shown that disentanglement is not possible without inductive bias in the data or model (Locatello et al., 2019), and it has been shown that generic VAEs are only able to disentangle when there is a particular bias in the data (Rolinek et al., 2019; Zietlow et al., 2021). However, it has also been shown that numerous inductive biases are sufficient for disentanglement (i.e. conditioning the prior on a third variable Khemakhem et al. (2020); or local isometry and non-Gaussianity Horan et al. (2021)). 

Though, in our work, we show disentanglement in VAEs with biological constraints, we also show disentanglement in supervised DeepNets and linear and non-linear autoencoders. Empirically, it seems out constraints are not limited to the VAE case, though further and more intensive empirical investigation are needed to confirm this. 

Our work also relates to modern self-supervised learning (Bardes et al., 2022) which seeks decorrelated representations with non-zero variance. Similar to many of the VAEs that disentangle, they introduce loss terms specifically to force decorrelation. Here instead, we show that simple biological constraints of nonnegativity and energy efficiency lead to emergent disentanglement without an explicit decorrelation term in the objective. 

19 

Published as a conference paper at ICLR 2023 

There is already evidence of disentanglement in machines as an emergent phenomenon as opposed to being baked in, for example interpretable neurons in vision model (Bau et al., 2017), multi-modal neurons in CLIP (Goh et al., 2021), and other work by on superposition/ privileged axes (Elhage et al., 2022) that also discusses the role of nonnegativity constraints. Similarly, other work is on understanding specialization in DeepNets (Casper et al., 2022). 

## A.2.3 DISENTANGLEMENT IN BRAINS 

Barlow first hypothesised that neurons represent independent components via redundancy reduction - minimising mutual information between their representation (Barlow, 1961; 1972)[5] . Since Barlow there have been numerous experimental results suggesting that brain neurons are disentangled: in inferior temporal cortex (Chang & Tsao, 2017; Bao et al., 2020; Higgins et al., 2021; Yildirim et al., 2020), visual cortex (Ecker et al., 2010; G´asp´ar et al., 2019), parietal cortex (Lee et al., 2022), and entorhinal cortex (Hafting et al., 2005; Solstad et al., 2008; Høydal et al., 2019). Similarly, however, there have been many reported neurons in various brain regions that are apparently mixed-selective (Rigotti et al., 2013; Boccara et al., 2019; Butler et al., 2019; Komorowski et al., 2009). 

There is no formal understanding of when and why neurons in the brain factorise across task parameters. Nevertheless, single latent dimensions from disentanglement models do predict single neuron activity, implying biological neurons are disentangled (Higgins et al., 2021). One conjecture in neuroscience is that while representing task factors is important for generalisation, mixed-selectivity is important for efficient read-out (Behrens et al., 2018; Rigotti et al., 2013; Bernardi et al., 2020). Here we show disentangled brain representations are preferred if the task is factorised into independent factors. This work bridges the gap between a single neuron understanding (i.e. like Sherrington) and a population based understanding (i.e. like Hopfield) (Barack & Krakauer, 2021). 

## A.2.4 BIOLOGICAL CONSTRAINTS 

While these constraints of nonnegativity and energy efficiency are not new to the machine learning or neuroscience literature, we package them together to learn new insights into how biological constraints shape the space of neural representation. 

**Nonnegativity.** Recent work on multitask learning in recurrent neural networks (RNNs) (Yang et al., 2019; Driscoll et al., 2022) demonstrated that neural populations, with a nonnegative activation function, partition themselves into task specific modules (Driscoll et al., 2022). Nonnegativity is also important in obtaining hexagonal, not square, grid cells (Dordek et al., 2016; Whittington et al., 2021b; Sorscher et al., 2019; 2020). Also, nonnegative matrix factorisation empirically yields spatially localised factors for images (Lee & Seung, 2000). Other work discusses potential algorithmic functions of nonnegativity in again Hebbian/anti-Hebbian networks, relating it to clustering, sparse feature discovery and again ICA (Pehlevan et al., 2015). Our work demonstrates theoretically and empirically _why_ nonnegativity leads to single neurons becoming selective for single factors. 

**Energy efficiency.** Using regularisation is common in machine learning, with l2 or l1 losses on weights primarily used. Less commonly do machine learners ask for energy efficiency on activations, though the VAE loss does include energy efficiency latent activations, and additionally some activation functions can be see as energy minimising, e.g. ReLus are sparsity inducing. In neuroscience, there is much work considering energy efficiency (see Chintaluri & Vogels (2022) for a fun recent example). There are also results more relevant to us, for example work that test whether orientation of neural manifolds from mouse V1 minimise energy efficiency (spike count) by randomly rotating and optimally shifting them to fit into nonnegative orthants (Bordelon & Pehlevan, 2022). 

> 5We note that Barlow also considered parsimony as a representational pressure too. While we do not consider it in this paper, we believe it is an important constraint. 

20 

Published as a conference paper at ICLR 2023 

## A.3 DETAILS OF DERIVATIONS 

- A.3.1 PROOF OF CONSTRAINTS LEADING TO DISENTANGLEMENT FOR A GIVEN POPULATION VARIANCE. 

**Theorem** . Let _**e** ∈_ R _[k]_ be a random vector whose _k_ independent components denote _k_ task factors. We assume each independent task factor _ei_ is drawn from a distribution that has mean 0, variance _σ_[2] , and maximum and minimum values of min( _ei_ ) = _−a_ and max( _ei_ ) = _a_ . Also let _**z** ∈_ R _[n]_ be a linear neural representation of the task factors given by 

**==> picture [230 x 9] intentionally omitted <==**

where _**M** ∈_ R _[n][×][k]_ are mixing weights and _**b** z ∈_ R _[n]_ is a bias. We further assume two constraints: (1) the neural representation is _nonnegative_ with _zi ≥_ 0 for all _i_ = 1 _, . . . , n_ , and (2) the neural population variance is a nonzero constant,[�] _j[V ar]_[(] _[z][j]_[)][=] _[C]_[,][so][that][the][neural][representation] retains some information about the task variables. Under these two constraints we show that in the space of all possible neural representations (parameterised by _**M**_ and _**b** z_ ), the representations that achieve minimal activity energy E _||_ _**z** ||_[2] also exhibit disentanglement, by which we mean every neuron _zj_ is selective for at most one task parameter: i.e. _|Mjk||Mjl|_ = 0 for _k_ = _l_ . 

**Proof.** We aim to find a representation, _**z**_ , that minimises activity energy (the expected norm of _**z**_ ), is nonnegative, all for a fixed population variance, _C_ . This is a constrained optimisation problem, and equates to understanding what _**M**_ and _**b** z_ must look like in order to satisfy our constraints, and minimise E _||_ _**z** ||_[2] . 

**==> picture [300 x 24] intentionally omitted <==**

The total activity energy, i.e. the expected norm of _**z**_ , is 

**==> picture [313 x 53] intentionally omitted <==**

We want to minimise this, under the constraint _zj ≥_ 0. To satisfy this constraint, ( _**b** z_ ) _j_ must account for any negativity. This means that 

**==> picture [273 x 22] intentionally omitted <==**

Where the last equality is because all _**e** k_ are i.i.d. and so the minimum of a sum of random variables is the sum of their minima. The modulus sign is since _Mjk_ can be positive or negative, so we need to consider the maximum and minimum of _**e** k_ , and an assumption of ours was that the maximum and minimum had the same value _a_ . Thus 

**==> picture [249 x 23] intentionally omitted <==**

Where _pj ≥_ 0. Intuitively, _pj_ = 0 since anything else would increase activity energy. Formally, 

**==> picture [332 x 82] intentionally omitted <==**

Since both[�] _k[|][M][jk][|][a]_[ and] _[ p][j]_[are greater than zero,] _[ p][j]_[always increases activity energy, no matter] what _Mjk_ is. Thus we set it to zero, i.e. _pj_ = 0. Hence we can simplify the expected activity as 

21 

Published as a conference paper at ICLR 2023 

follows 

**==> picture [313 x 147] intentionally omitted <==**

Now all the constraints have been incorporated, our only job is to minimise E _||_ _**z** ||_[2] . This is done when[�] _j,k,l_ = _k[|][M][jk][||][M][jl][|]_[=][0][,][and][that][only][happens][when] _[|][M][jk][||][M][jl][|]_[=][0][for][all] _[j]_[and] _[l]_[=] _[k]_[.] In words, this means that neuron _j_ in only receives information from one element of _**e**_ . This is disentanglement. 

## A.3.2 PROOF THAT POPULATION VARIANCE IS BOUNDED BY READ-OUT WEIGHTS NORM 

**Theorem.** Let _**x**_ = _**De**_ be observed entangled data, where _**x** ∈_ R _[m]_ , _**D** ∈_ R _[m][×][k]_ , and _**e** ∈_ R _[k]_ is a random vector whose _k_ independent components denote _k_ task factors. We assume each independent task factor _ei_ is drawn from a distribution that has mean 0, variance _σ_[2] , and maximum and minimum values of min( _ei_ ) = _−a_ and max( _ei_ ) = _a_ . Let a neural representation _**z** ∈_ R _[n]_ exactly predict observed data via _**x**_ = _**W z**_ + _**b** x_ with zero error, i.e. _**x**_ = _**De**_ = _**W z**_ + _**b** x_ . Where _**W** ∈_ R _[m][×][n] m ≥ n ≥ k_ , are read-out weights and _**b** x ∈_ R _[m]_ is an offset. 

Then for all such data generation models (with parameters _**D**_ ) and all such neural representations (with parameters _**W**_ and _**b** x_ ), as long as: (1) the smallest singular value of _**D**_ is non-zero, _σmin_ ( _**D**_ ) _>_ 0; (2) the norm of the read-out weights _||_ _**W** ||_[2] _F_[is finite;][then the population variance] of _**z**_ is bounded from below by the norm of the read-out weights. 

**==> picture [256 x 29] intentionally omitted <==**

**Proof** . Since _**x**_ = _**W z**_ + _**b** x_ , we have 

**==> picture [246 x 26] intentionally omitted <==**

Where _**W**_[+] is the Moore-Penrose pseudoinverse. Additionally since the read-out error is zero, _**W**_ must contain all the same information as _**D**_ , and so must be _**W**_ = _**DF**_[+] , where _**F**_[+] _∈_ R _[k][×][n]_ is a matrix with rank _k_ ( _n ≥ k_ ). The pseudoinverse of _**W**_ is thus _**W**_[+] = _**F D**_[+] . The population variance becomes 

**==> picture [291 x 102] intentionally omitted <==**

Using the fact that the norm of a matrix’s pseudoinverse is bounded by the norm of the matrix 

**==> picture [273 x 25] intentionally omitted <==**

22 

Published as a conference paper at ICLR 2023 

Along with using the following trace identity (Fang et al., 1994) 

**==> picture [326 x 13] intentionally omitted <==**

Where _σmin_ ( _**D**_ ) and _σmax_ ( _**D**_ ) are the smallest and largest singular values of _**D**_ . Thus 

**==> picture [242 x 26] intentionally omitted <==**

Combining it all together 

**==> picture [261 x 82] intentionally omitted <==**

We note that the first inequality becomes an equality if and only if _**F**_[+] has (scaled) orthonormal _rows_ , and the second inequality becomes and equality if and only if _**D**_ has (scaled) orthonormal _columns_ . 

## A.3.3 PROOF OF DISENTANGLEMENT WHEN DATA GENERATIVE MATRIX HAS (SCALED) ORTHONORMAL COLUMNS 

**Theorem** . Let _**x**_ = _**De**_ be observed entangled data, where _**D** ∈_ R _[m][×][k]_ , and _**e** ∈_ R _[k]_ is a random vector whose _k_ independent components denote _k_ task factors. We assume each independent task factor _ei_ is drawn from a distribution that has mean 0, variance _σ_[2] , and maximum and minimum values of min( _ei_ ) = _−a_ and max( _ei_ ) = _a_ . Let a neural representation _**z** ∈_ R _[n]_ exactly predict observed data via _**x**_ = _**W z**_ + _**b** x_ with zero error, i.e. _**x**_ = _**De**_ = _**W z**_ + _**b** x_ . Where _**W** ∈_ R _[m][×][n] m ≥ n ≥ k_ , are read-out weights and _**b** x ∈_ R _[m]_ is an offset. 

Then for all such data generation models (with parameters _**D**_ ) and all such neural representations (with parameters _**W**_ and _**b** x_ ), as long as: (1) the columns of _**D**_ are (scaled) orthonormal; (2) the norm of the read-out weights _||_ _**W** ||_[2] _F_[is][finite;][(3)][the][neural][representation][is][nonnegative][(i.e.] _**z** >_ 0), then out of all such neural representations, the minimum energy representations are also disentangled ones. By this we mean that each neuron _zi_ will be selective for at most one hidden task factor _ej_ . 

**Proof.** We aim to find a representation, _**z**_ , that minimises activity energy (the expected norm of _**z**_ ), is nonnegative, and predicts data _**x**_ = _**De**_ via _**x**_ = _**W z**_ + _**b** x_ with zero error ( _**De**_ = _**W z**_ + _**b** x_ ). This is a constrained optimisation problem, and equates to understanding what _**W**_ and _**b** x_ (and therefore _**z**_ ) must look like in order to satisfy our constraints, and minimise E _||_ _**z** ||_[2] . 

**==> picture [333 x 17] intentionally omitted <==**

We note that this is the classic matrix factorisation setting. The difference here is that we ask the representation _**z**_ to be nonnegative. 

Firstly, we note that since the columns of _**D**_ are (scaled) orthonormal, then the singular values are all equal: _σmin_ ( _**D**_ ) = _σmax_ ( _**D**_ ) = _σ_ ( _**D**_ ). This result is useful as now the inequality in equation 19 becomes an equality 

**==> picture [238 x 26] intentionally omitted <==**

Now we prove disentanglement. Since the read-out error is zero, _**W**_ must contain all the same information as _**D**_ and so must be _**W**_ = _**DF**_[+] . Using this, and repeating a similar process to the 

23 

Published as a conference paper at ICLR 2023 

first proof (Appendix A.3.1), we get 

**==> picture [339 x 125] intentionally omitted <==**

Where the inequality is due to equation 17. This inequality becomes an equality if and only if _**F**_[+] has (scaled) orthonormal _rows_ (i.e. _**F**_ has (inverse scaled) orthonormal _columns_ ). This means that for a fixed _||_ _**W** ||_[2] _F_[,][the][first][term][in][equation][23][is][minimised][when] _**[F]**_[ +][has][(scaled)][orthonormal] rows, or equally when _**F**_ has (inverse scaled) orthonormal columns. This is interesting to us, as we can additionally make the second term in equation 23 go to zero when _**F**_ is a _particular_ type of matrix with (inverse scaled) orthonormal columns. Thus we will have fully optimised equation 23, and this will be our solution. First, rewriting _**F**_ as a matrix with (inverse scaled) orthonormal columns 

**==> picture [260 x 21] intentionally omitted <==**

Where _**O**_ is a matrix with orthonormal columns. The particular _**F**_ that minimises the second term in equation 23, is when _**O**_ only has, at most, a single non-zero element per row as this sets _|Fjk||Fjl|_ = 0. This is disentanglement and is easily seen by 

**==> picture [258 x 58] intentionally omitted <==**

Since _**O**_ only has a single non-zero element per row, then each _**z** i_ must only contain a single element (random variable) from _**e**_ . We note that nonnegativity is easily achieved by _**b** x_ learning to take a value that satisfies nonnegativity, i.e. _α_ _**O**[T]_ _**D**_[+] _**b** x_ = min _α_ _**O**[T]_ _**e**_ . Since _**O**_ and _**D**_ are full ( _k_ ) rank, this is always possible. 

We also offer an alternate proof in Appendix A.3.5 when analysing ‘Simplification 1’. 

## A.3.4 PROOF THAT A TALL RANDOM MATRIX WITH FINITE WIDTH HAS (SCALED) APPROXIMATELY ORTHONORMAL COLUMNS 

**Theorem.** Let _**D** ∈_ R _[m][×][k]_ be a random matrix with elements _Dij_ that are i.d.d. with expectation 0 and variance _κ_[2] _/m_[2] ). Then as _m →∞_ , with finite _k_ , _**D**[T]_ _**D** →_ _**I**_ . 

## **Proof.** 

**==> picture [274 x 70] intentionally omitted <==**

Thus _**D**_ has orthonormal columns, scaled by _κ_ , and so its singular values are all identical; _σmin_ ( _**D**_ ) = _σmax_ ( _**D**_ ) = _κ_[2] . 

- A.3.5 WHEN THE DATA GENERATIVE MATRIX **DOES NOT** HAVE (SCALED) ORTHONORMAL COLUMNS 

While we do not prove the general case, we offer some intuition here that suggest disentangled representations are favoured in many situations. Consider the general setting in which _**D** ∈_ R _[m][×][k]_ 

24 

Published as a conference paper at ICLR 2023 

has the following singular value decomposition (SVD): 

**==> picture [223 x 9] intentionally omitted <==**

Where Σ _∈_ R _[m][×][k]_ is a rectangular diagonal matrix with positive entries, and _**U** ∈_ R _[m][×][m]_ and _**V** ∈_ R _[k][×][k]_ are orthogonal matrices. As in the above proofs, since _**x**_ is predicted with zero error from _**z**_ , via 

**==> picture [243 x 9] intentionally omitted <==**

Thus _**W**_ must be of the form _**W**_ = _**DF**_[+] , where _**F**_[+] _∈_ R _[k][×][n]_ is a rank _k_ matrix, since _**z** ∈_ R _[n]_ , _**x** ∈_ R _[m]_ , and _**e** ∈_ R _[k]_ , _m ≥ n ≥ k_ . We define the SVD of _**F**_ as 

**==> picture [271 x 11] intentionally omitted <==**

Where Λ _∈_ R _[k][×][n]_ is a rectangular diagonal matrix with positive entries, _λi_ , Λ _[−]_[1] _∈_ R _[n][×][k]_ is a rectangular diagonal matrix with positive entries, _λ_ 1 _i_[,][and][where] _**[O]**[∈]_[R] _[n][×][n]_[and] _**[R]**[∈]_[R] _[k][×][k]_[are] orthogonal matrices. From equation 16 the population variance is 

**==> picture [250 x 51] intentionally omitted <==**

Where _σ_ is the variance of the random variables _ei_ . The norm of the weights _||_ _**W** ||_[2] _F_[is] 

**==> picture [280 x 77] intentionally omitted <==**

While we have been previously interested in finding the minimal activity energy with fixed _||_ _**W** ||_[2] _F_[,] we instead allow _||_ _**W** ||_[2] _F_[to change and instead minimise] _[ ||]_ _**[W]**[ ||]_[2] _F_[:] _[L]_[ =][ E] _[||]_ _**[z]**[||]_[2][ +] _[ β][w][||]_ _**[W]**[ ||]_[2] _F_[, where] _βw_ is the strength of regularization on the weights. Thus using equation 23, we have 

**==> picture [360 x 30] intentionally omitted <==**

This is the overall thing we want to optimise. However, for now we do not consider the the middle term - the interaction induced by the nonnegativity constraint - and instead consider the following optimisation problem 

**==> picture [337 x 29] intentionally omitted <==**

Under the constraints that _**V**_ and _**R**_ remain orthogonal and Λ remains rectangular diagonal with positive entries. This is difficult in general, but we can simplify to gain intuition and insights. 

**Simplification 1** . The first simplification is when Σ is a scaled identity matrix. This is the same simplification we used in Proof 3 (Appendix A.3.3), i.e. the singular values of _**D**_ are all equal, _σi_[2][(] _[D]_[) =] _[ σ]_[2][(] _[D]_[)][.] 

**Simplification 2** . The second simplification is that _**V**_ is the identify matrix. This corresponds to data being generated via _**D**_ = _**U**_ Σ, i.e. the random variables are scaled and then orthogonally projected. 

25 

Published as a conference paper at ICLR 2023 

Analysing **simplification 1** first, to build up intuition (and offer an alternative proof of Theorem 3), _L[′]_ becomes 

**==> picture [330 x 123] intentionally omitted <==**

Where we exploited the fact that _**R**_ and _**V**_ are orthogonal matrices. Optimising this is easy to do, we can simply take derivatives to get 

**==> picture [231 x 24] intentionally omitted <==**

This result is independent of _**R**_ and _**O**_ , and so we are free to choose whatever orthogonal matrices we like. This is good news for us as the real game we are in is minimising _L_ (equation 32) which contains an additional term involving _**R**_ and _**O**_ : _a_[2][ �] _j,k,l_ = _k[|][F][jk][||][F][jl][|]_[=] _a_[2][ �] _j,k,l_ = _k[|]_[(] _**[O]**_[Λ] _**[R]**[T]_[ )] _[jk][||]_[(] _**[O]**_[Λ] _**[R]**[T]_[ )] _[jl][|]_[.][Thus][if][we][can][set] _[|]_[(] _**[O]**_[Λ] _**[R]**[T]_[ )] _[jk][||]_[(] _**[O]**_[Λ] _**[R]**[T]_[ )] _[jl][|]_[=][0][,][then] we will have fully minimised _L_ . This is easy enough to do (keeping _**R**_ and _**O**_ orthogonal) and is achieved when _**R**_ is a permutation matrix, and _**O**_ has at most one non-zero element per row (or equally _**O**_ has at most one non-zero element per column). This corresponds to disentangled representations. 

Returning to **simplification 2** , where _**V**_ is the identify matrix, now _L[′]_ becomes: 

**==> picture [316 x 62] intentionally omitted <==**

Thus we have the following constrained optimisation problem 

**==> picture [332 x 30] intentionally omitted <==**

Here we let intuition take over. Taking inspiration from the simplification 1, our ansatz is that _**R**_ is a permutation matrix and _λ_[4] _i_[=] _βσw_[2] _σ_ + _j_[2][(] _a[D]_[2][)] (where _i_ and _j_ are related by the permutation). To justify that _**R**_ should be a permutation matrix in this case, we note that as _λ_[2] _i_[gets][smaller][to] keep _||_ _**W** ||_[2] _F_[=][�] _ij[σ] i_[2][(] _[D]_[)] _[V][ij] λ_[1][2] _j_[as small as possible,][the] _[ R][ij]_[must ensure the low valued] _[ λ]_[2] _j_[are] matched with the low valued _σi_[2][(] _[D]_[)][.][Intuitively this is done when] _**[ V]**_[is a permutation matrix.][Once] _**R**_ is chosen as a permutation matrix, showing that _λ_[4] _i_[=] _βσw_[2] _σ_ + _j_[2][(] _a[D]_[2][)] is simple - just take derivatives and set to zero. While this is not a full proof, if one derives the KKT conditions, this solution is at least a consistent solution, i.e. it is a minima but may not be the global minima. We note that for specific (small) values of _βw_ it will be the global minima. 

As before, our actual aim is to minimise _L_ . Since we are free to choose _**O**_ , and we choose it to make the cross terms in equation 32 go to zero, which is when _**O**_ has at most one non-zero element per column. This corresponds to disentangled representations. 

**No simplifications.** Reminding ourselves of the full objective 

**==> picture [360 x 29] intentionally omitted <==**

26 

Published as a conference paper at ICLR 2023 

In this case _**V**_ is an arbitrary orthogonal matrix, and _σi_[2][(] _[D]_[)][ are the (not necessarily equal) singular] values of _**D**_ . One potential ansatz is to assume _**R**_ is a permutation matrix once again, which then reduces the problem to simplification 2. Again this offers a minima, but not necessarily the global minima. 

In sum, we can see that there is always a pressure to disentangle due to the middle term in the loss. However it will have to trade-off against the weight regularization term (last term). Thus we posit that for small values of _βw_ disentanglement is preferred, even for arbitrary _**D**_ . 

27 

Published as a conference paper at ICLR 2023 

## A.4 DETAILS OF GENERATED DATASETS 

We note that no domain knowledge, like the exact number of factors, is provided too our models at any point. However the dimensionality of the network layer must be at least this number to disentangle all factors. 

## **Disentanglement in supervised shallow neural networks** . 

Starting with 6 independent variables, each sampled from a standard uniform distribution, i.e. _**e** ∈_ [0 _,_ 1][6] . We construct a dataset with _**x**_ = _**Oe**_ , where _**O**_ is a random orthogonal matrix (random for each model/seed). The target _**y** ∈_ R[6] is a generated from _**y**_ = _**W e**_ where _**W** ∈_ R[6] _[×]_[6] has elements drawn independently from a standard normal distribution ( _**W**_ different from each model/seed). We generate 200000 data points. 

## **Disentanglement in supervised deep neural networks** . 

This is generated in the same way as above but we additionally set _**x** ←_ _**x**_[3] , where the cubing is done element-wise. 

## **Disentanglement in unsupervised shallow neural networks** . 

Starting with 6 independent variables, each sampled from a standard uniform distribution, i.e. _**e** ∈_ [0 _,_ 1][6] . We construct a dataset _**y** ∈_ R[50] , with _**y**_ = _**W e**_ , where _**W** ∈_ R[50] _[×]_[6] has elements drawn independently from a standard normal distribution ( _**W**_ different from each model/seed). We generate 200000 data points. 

## **Disentanglement in unsupervised deep neural networks** . 

Starting with 6 independent variables, each sampled from a standard uniform distribution, i.e. _**e** ∈_ [0 _,_ 1][6] . We construct a dataset _**y** ∈_ R[50] , with _**y**_ = _MLP_ ( _**e**_ ), where the MLP is a 1-hidden layer network with relu activation function on the hidden layer. The hidden later has dimension 28, and all weights of the network are drawn independently from a standard normal distribution (redrawn from each model/seed). We generate 200000 data points. 

28 

Published as a conference paper at ICLR 2023 

## A.5 NETWORK ARCHITECTURES AND OPTIMISATION DETAILS 

All code will be released on publication. All hyper-parameters are shown in Table 1. We describe any additional details here. We use the Adam optimiser (Kingma & Ba, 2014). Supervised nets use square error loss. Unsupervised nets use sigmoid cross entropy loss. 

**Supervised networks.** _L_ nonneg, _L_ activity and _L_ weight are applied to all layers. The shallow Network is a 1-layer MLP with hidden dimensions of [188]. The deep networks are 5-layer MLP with hidden dimensions of [188,186,184,182,180]. We use a squared error loss for _L_ prediction. 

**Autoencoders.** We apply _L_ nonneg and _L_ activity to the latent layer only. We apply _L_ weight to all layers. The shallow autoencoder has no hidden layers in the encoder or decoder. The deep autoencoder has and encoder with hidden dimensions of [500,300,100] and a decoder with hidden dimensions of [100,300,500]. The output has a sigmoid and we use a sigmoid cross entropy loss for _L_ prediction. 

**Variational Autoencoder.** We use an architecture described in Higgins et al. (2017a) (Table 2). We use the standard _β_ -VAEs loss with the following additions. We apply _L_ nonneg to the latent layer only. We apply _L_ weight to the dense layers in the decoder only. We _do not_ apply _L_ activity as an effective norm constrain term already exists in the _β_ -VAEs loss. 

||**Supervised Net**|**Supervised Net**|**Supervised Net**|**Autoencoder**|**Autoencoder**|**VAE**|
|---|---|---|---|---|---|---|
||_Shallow_|_Deep_||_Shallow_|_Deep_|_Deep_|
|input dimension<br>output dimension<br>#parameters|6<br>6<br>2450|6<br>6<br>138574||50<br>n/a<br>1570|50<br>n/a<br>414870|(64, 64, 3)<br>n/a<br>766295|
|# (hidden) layers|1|5||enc: 0<br>dec: 0|enc: 3<br>dec 3|enc: 6<br>dec 6|
|latent dimension<br>learning rate<br>batch size<br>#gradient updates|n/a<br>3e-3<br>128<br>300000|||10<br>1e-4<br>64<br>300000||10<br>1e-4<br>64<br>500000|
|_βactivity_<br>_βweight_<br>_βnonneg_<br>_βV AE_|1e-3<br>1e-4<br>2.0<br>n/a|||5e-3<br>1e-3<br>0.5<br>n/a||n/a<br>0.01→1.0<br>100.0<br>1.0|
|Table 1: The values of various hyper-parameters. enc/dec: encoder/decoder. n/a: not applicable.<br>**Encoder**<br>**Decoder**<br>Input: 64 × 64 × number of channels<br>Input: 10<br>4 × 4 conv, 32 ReLU, stride 2<br>FC, 256 ReLU<br>4 × 4 conv, 32 ReLU, stride 2<br>FC, 4×4×64 ReLU<br>4 × 4 conv, 64 ReLU, stride 2<br>4 × 4 upconv, 64 ReLU, stride 2<br>4 × 4 conv, 64 ReLU, stride 2<br>4 × 4 upconv, 32 ReLU, stride 2<br>FC 256<br>4 × 4 upconv, 32 ReLU, stride 2<br>F2 2 × 10<br>4 × 4 upconv,number of channels,stride 2|||||||
|**Encoder**|||**Decoder**||||
|Input: 64 × 64 × number of channels<br>4 × 4 conv, 32 ReLU, stride 2<br>4 × 4 conv, 32 ReLU, stride 2<br>4 × 4 conv, 64 ReLU, stride 2<br>4 × 4 conv, 64 ReLU, stride 2<br>FC 256<br>F2 2 × 10|||Input: 10<br>FC, 256 ReLU<br>FC, 4×4×64 ReLU<br>4 × 4 upconv, 64 ReLU, stride 2<br>4 × 4 upconv, 32 ReLU, stride 2<br>4 × 4 upconv, 32 ReLU, stride 2<br>4 × 4 upconv,number of channels,stride 2||||



Table 2: Encoder and decoder architecture for the variational autoencoder experiments. 

29 

Published as a conference paper at ICLR 2023 

## A.6 SPARSITY DOES NOT PROMOTE DISENTANGLEMENT 

Readers may wonder if imposing a sparsity constraint would encourage disentanglement, as ReLUs promote sparsity as well as enforcing nonnegativity. This is not the case, and can be understood intuitively, and also with numerical simulation. For intuition, a sparsity constraint creates a diamond shaped iso-contour in neural space (Fig. 8) left, and so encourages the firing rate distribution to fall inside that diamond, which in the case our our random variables, means maximal entangling. We confirm this intuition in simulation (data and setup the same as Fig. 2) with a variety of sparsity regularization strengths (Fig. 8 right). Thus the reason ReLUs promote nonnegativity is not because they induce sparsity (which they do), but because they enforce nonnegativity. 

**==> picture [394 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
Neuron 2 Neuron 2<br>Satisfy sparsity<br>Neuron 1 Neuron 1<br>**----- End of picture text -----**<br>


Figure 8: **Sparsity intuition and simulations.** Sparsity does not encourage disentanglement. Here the best situation is maximal entangling. Simulations verify that sparsity constraints do not induce disentanglement. 

Similarly, one may wonder if sparsity on weights may encourage disentanglement. We do not observe this empirically (Fig. 9) 

**==> picture [199 x 148] intentionally omitted <==**

Figure 9: **Sparsity on weights does not lead to disentanglement.** 

30 

Published as a conference paper at ICLR 2023 

## A.7 REPRESENTING CATEGORICAL DISTRIBUTIONS 

We note that this is a fundamentally different problem to representing factors, since only one category is active at any one time; categories are anti-correlated. This contrasts to factors as all factors can be active independently. So even though the proofs are similar, they are about different situations. 

**Theorem** . Given a nonnegative representation, _**z** ∈_ R _[n]_ , that linearly reads-out a population, _**x** ∈_ R _[m]_ which is itself a linear projection of a categorical variable (one-hot variable) 

_**x**_ = _**W z**_ and _**x**_ = _**Cc**_ (39) 

Where _**c** ∈_ R _[c]_ is a one-hot representation (with each one-hot vector having equal probability) with each element, _ci_ , representing category identity (1 when present, 0 otherwise, only one category active at once), _**W** ∈_ R _[m][×][n]_ are read-out weights with fixed norm, _||_ _**W** ||_[2] _F_[,][and] _**[C]**[∈]_[R] _[m][×][c]_[are] the data generative weights which is a rank _c_ matrix with all singular values equal and positive; _σmin_ ( _**C**_ ) = _σmax_ ( _**C**_ ) = _σ_ ( _**C**_ ) _>_ 0. Then in order to minimise the expected activity energy, E _||_ _**z** ||_[2] , _**z**_ must be structured so that each neuron only represents at most a single category. 

**Intuition.** In order to linearly read-out a categorical variable from a neural population, _**z**_ , then _**z**_ must take be a linear combination of a one-hot vector ( _**c**_ ; each element in the one-hot vector corresponding to each category. 

_**z**_ = _**Mc**_ (40) 

For this representation to be nonnegative, all entries of _**M**_ must be nonnegative. This means that the population response, _**z** i_ , for each category, _i_ , must be a vector in the positive orthant (Fig. 10). Assuming we keep the expected activity energy constant, i.e. 

**==> picture [296 x 26] intentionally omitted <==**

Then the easiest representation to read-out from is the one-hot representation, since in all other situations the vectors are closer together which require larger read-out weights to disambiguate. Alternatively, if there is noise on _**z**_ then the categories will be more often confused if the _**z** c_ vectors are closer to each other. A one-hot representation is the best, and it is a disentangled representation for each category. 

**Proof.** We aim to show when minimising E _||_ _**z** ||_[2] , when _**z**_ is nonnegative ( _zi ≥_ 0), and for a finite norm of the read-out weights, _||_ _**W** ||_[2] _F_[,][then][it][is][optimal][for][each][element,] _[z][i]_[in] _**[z]**_[to][represent][at] most a single category. This is a constrained optimisation problem 

**==> picture [291 x 16] intentionally omitted <==**

Since we read-out with zero error, _**Cc**_ = _**W z**_ , then _**W**_ must contain all the information of _**C**_ , i.e. _**W**_ = _**CF**_[+] , where _**F**_[+] _∈_ R _[c][×][n]_ is a rank _c_ matrix. Thus _**z**_ must be 

**==> picture [227 x 40] intentionally omitted <==**

**==> picture [342 x 114] intentionally omitted <==**

**----- Start of picture text -----**<br>
M<br>**----- End of picture text -----**<br>


Figure 10: Schematic for representing categories. Each axis is neural firing rate. Each colour is a population activity for a single category, i.e. _**z** c_ . 

31 

Published as a conference paper at ICLR 2023 

For this to be nonnegative, since _**c**_ is one-hot, then _Fij ≥_ 0. Additionally, the expected activity energy becomes 

**==> picture [242 x 94] intentionally omitted <==**

Where the final equality if from equation 22, and where the inequality is from equation 17. This inequality becomes an equality if and only if _**F**_[+] has (scaled) orthonormal rows (or _**F**_ has (scaled) orthonormal columns). Thus to minimise E _||_ _**z** ||_[2] we want _**F**_[+] to have (scaled) orthonormal rows or equally _**F**_ to have (scaled) orthonormal columns. To satisfy nonnegativity we wanted _Fij ≥_ 0. There is only one type of matrix with (scaled) orthonormal columns that has nonnegative entries, and that is when _**F**_ has rows that contain at most one non-zero element, and so each neuron only ‘attends’ to one category; categories are disentangled. 

## A.7.1 SIMULATION RESULTS 

We train an autoencoder on data from 6 categories. The data from each category is noiseless, so we essentially just have 6 data samples that we train on. Each category vector is sampled from a uniform distribution. We train an autoencoder with a deep encoder (hidden layers: [500,300,100]) and a shallow decoder (0-hidden layers), and with latent dimension of 10. 

Along with variants of our constraints, we also train a network with a sparsity inducing loss: _L_ sparsity = _βsparsity_ � _i[|][a][i][|]_[,][where] _[a][i]_[is][the][activity][of][a][neuron][in][the][latent][layer.][All][other] hyper-parameters are as described in the autoencoder section of Table 1, and we set _βsparsity_ to be the same as _βnonneg_ . 

We see that only our constraints, and the sparsity inducing loss, achieves disentanglement of categories (Fig. 11). 

**==> picture [394 x 221] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>**----- End of picture text -----**<br>


Figure 11: **Learning data generative factors with autoencoders. A)** Training linear autoencoders on linear data. Only models with our constraints, or with sparsity, learn disentangled representations. **B)** Example mutual information matrix from a high MIR model. All learning curves show mean and standard error from 4 mean from 5 random seeds. 

32 

Published as a conference paper at ICLR 2023 

## A.8 FURTHER VAE SIMULATIONS RESULTS 

**==> picture [394 x 247] intentionally omitted <==**

Figure 12: **Latent space traversals.** An image is encoded and then the value of a single latent dimensions is changed, and the resulting image is generated. Each row shows this image for when a single latent dimension is traversed. The histogram shows the marginal distribution of that latent variable. From the images, we can see that each latent dimension predominantly cares about a single ground truth factor. 

**==> picture [394 x 82] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>**----- End of picture text -----**<br>


Figure 13: **Same as Fig. 5, but for the dSprites dataset. A)** We train on the dSprites dataset, with two example images shown. These images have 5 underlying factors. **B)** MIG scores are higher with higher weight regularization, and generally higher than any _β_ -VAE (panel D). **C)** Mutual information matrix for a high scoring model. We note it has dropped a latent dimension. **D)** _β_ -VAE MIG scores. We note the high disentanglement _β_ -VAE models have bad reconstruction as they drop latent dimensions. **E)** MIG score against _R_[2] shows models with our constraints lie in the Goldilocks region of high disentanglement and high reconstruction. All learning curves show mean and standard error from 5 random seeds. 

33 

Published as a conference paper at ICLR 2023 

## A.9 PATTERN FORMING DETAILS 

## A.9.1 DETAILS ON TRAINING DATA 

**A factorised task for rodents.** We generate many 16x16 worlds (so 256 locations; _nl_ = 256) where objects can be at random locations. The number of objects in each world is chosen uniformly between 0 and 8. In practice it is not always possible to place every object as we do not permit objects to be closer than 8 units away. 

From each world we have the following data: _{_ _**x** ,_ _**o**_ ( _**x**_ ) _,_ _**a**_ ( _**x**_ ) _}_ for all 256 locations _**x**_ , where _**x**_ is a one-hot identifier of location, _**o**_ ( _**x**_ ) is a binary variable of whether there is an object or not at location _**x**_ , and _**a**_ ( _**x**_ ) is a 4-dimensional vector describing the optimal action - a one or zero in each entry corresponding to North/South/East/West (more than one action could be optimal at each location). Optimal actions are towards the closest object. 

We train on this data, with a batch size of 8, i.e. presenting 8 such worlds simultaneously. Each world in the batch is randomly sampled from the above process. 

**A entangled task for rodents.** This is the same as the above, except we sample only 1 world throughout training, i.e. every world in the 8 batches are identical and all batches are identical. 

## A.9.2 MODEL DETAILS 

We use a discrete 16x16 world (so 256 locations; _nl_ = 256) and optimise an independent representation, _**z**_ ( _**x**_ ) _∈_ R _[n][c]_ , at each location. We now detail each component of the following loss 

**==> picture [358 x 26] intentionally omitted <==**

**Biological losses.** These are exactly the same as in the main paper, but we must also average over all locations, _**x**_ 

**==> picture [283 x 87] intentionally omitted <==**

where _zi_ ( _**x**_ ) is a neuron in representation _**z**_ ( _**x**_ ), _t_ indexes the task (i.e. object, action, location prediction), and the _β_ values determines the regularization strength. 

**Location loss.** The representation predicts location (a one-hot encoding describing each of the 256 locations) via a linear transformation, which is then fed into a softmax cross-entropy loss. In particular, the logits for each location, _**x**_ , are _**W** l_ _**z**_ ( _**x**_ ), where _**W** l ∈_ R _[n][l][×][n][c]_ . If we denote each row of _**W** l_ as _**lx**_ , noting that this row that ‘corresponds’ to location _**x**_ in the one-hot encoding, then the loss is as follows 

**==> picture [282 x 28] intentionally omitted <==**

**Object loss.** An object is either present or not present at each location, so we use a sigmoid crossentropy loss. In particular, the logits for each location _**x**_ is _**W** o_ _**z**_ ( _**x**_ ), where _**W** o ∈_ R[1] _[×][n][c]_ . If 1 object at _**x**_ returns a 1 if an object is present at location, _**x**_ , and 0 otherwise, then the loss is as follows 

**==> picture [372 x 27] intentionally omitted <==**

**Action loss.** More than one action can be correct at a location, so we use a sigmoid cross-entropy loss for each of the 4 actions. In particular, the logits at location, _**x**_ , are _**W** t ·_ _**z**_ ( _**x**_ ), where _**W** t ∈_ R _[n][a][×][n][c]_ , where _na_ is the number of actions (4 in our case - North, South, East, West). We denote each row 

34 

Published as a conference paper at ICLR 2023 

of _**W** t_ as _**t** j_ , noting this row ‘corresponds’ to action _j_ in the action encoding. If 1 _a_ = _**a**_ ( _**x**_ ) returns a 1 if action, _a_ , is a correct action at location _**x**_ , and 0 otherwise, then the loss is as follows 

**==> picture [385 x 26] intentionally omitted <==**

**Structural loss.** We use a squared error loss for the structural constraint, which asks for neighbouring representations to be related to each other by an action matrix _**W** a_ for each action, _a_ . This is just like a path integration loss. This loss is done for every location, _**x**_ , and each of the 4 actions, _a_ . 

**==> picture [331 x 27] intentionally omitted <==**

Where _**W** a ∈_ R _[n][c][×][n][c]_ is a weight matrix that depends on action, _a_ , (i.e. there are 4 trainable weights matrices - one for each action). _**d** a_ means the displacement in the underlying space (the space of _**x**_ ), that the action _a_ corresponds to. 

This loss is effectively a path integration loss and can be understood by considering the path integration equation. While there are more than one potential forms for path integration we choose the form relating to Gao et al. (2021) which sequentially updates representations in time via: 

**==> picture [234 x 11] intentionally omitted <==**

If the representation at time-step _t −_ 1 corresponds to location _**x** −_ _**d** a_ , then for path integration to be successful, the representation at time _t_ must correspond to location _**x**_ . Then the equation becomes like equation 3. This is exactly what our loss asks for. We note, however, that this loss on its own could just make all representations at all locations the same constant (and learn all _**W** a_ to be the identity), in which case location isn’t represented at all. However the location loss ensures all locations are represented differently. So really it is the structural loss and the location loss together that are like path integration. Overall, this formulation translates sequential path integration in time into an optimisation over representation at locations without needing to incorporate time. This greatly reduces the difficulty of optimisation and makes the problem more general than just sequences in time. 

**Pattern forming dynamics.** The overall loss can be optimised with respect to the weights. However, it can also be optimised directly with respect to _**z**_ . This is particularly interesting for us, as it allows our representation to be dynamic and change rapidly for a single task, and not just slowly via learning over many tasks. This is a necessity for us as we need to represent objects which may move between tasks. To optimise both _**z**_ (task particularities) and weights (task generalities), we do so in two stages. First, we optimise with respect to _**z**_ to ‘infer’ a representation for the current task. Second, we optimise with respect to the weights to learn parameters that are general across tasks. 

When optimising with respect to _**z**_ we only optimise two terms in the loss: _L_ objects and _L_ path integration. We optimise the first term so the systems has the ability to know where the objects are. We optimise the second term so that information can be propagated around (effectively via path integration). 

The dynamics of the _L_ objects are: 

**==> picture [297 x 24] intentionally omitted <==**

This says if you get the object prediction wrong, then update _**z**_ to better predict the object. We restrict this update to only take place where the object is, so it is just an object signal. This update is equivalent to a rodent observing that it is at an object. 

The dynamics of the _L_ path integration are: 

**==> picture [337 x 42] intentionally omitted <==**

The two terms in the above equation can be easily understood. The first says that the representation at each location, _**z**_ ( _**x**_ ), should be updated according to what its neighbours think it should (this is 

35 

Published as a conference paper at ICLR 2023 

the same update rule as path integration!). The second term says the representation at each location, _**z**_ ( _**x**_ ), should be updated if did not predict its neighbours correctly. This equation tells representations to update based their neighbours. This is just like a **cellular automata** , but instead of a discrete value being updated on the basis of its neighbours, it is a whole population vector whose elements can are continuous. Indeed, just like cellular automata, it is also possible to initialise a single ‘cell’ (location) of the cellular automata, and have that representations propagate throughout the space. In this case, it’s just like path integration, but spreading through all space at once. We note, however, that in our simulations we initialise representations at all locations (for each task). 

We note that while we simulated this on a discrete grid, the same principles apply to continuous cases. In this case the sums over location/actions need to be replaces with integrals. 

This is a very general approach for understanding representations. The structural loss does not have to related to the rules of path integration. It can be anything. It could be the rules of a graph. It could be rules of topology. It could have one set of rules at some locations and another set of rules at other locations. The rules don’t have to be neighbouring representations telling each other what to be, it could also be long range rules too. If there are structure or rules in the world or behaviour, our constraints say that representations should understand that structure or rules. In mathematics this is known as a homeomorphism. In sum, understanding representations via constraints is very general. 

**Hyper-parameters.** _β_ nonneg, _β_ weight, _β_ activity, _β_ location, _β_ object, _β_ action, _β_ path integration are chosen as 1 _e−_ 2, 1 _e −_ 7, 1 _e −_ 3, 1 _e −_ 2,1 _e −_ 1, 1 _e −_ 2, 40. The learning rate is 12 _e −_ 4. In the Euler updates for pattern formation, the step size for path integration is 0.1, and the step size for objects is 1. We additionally clip the norm of the update in pattern formation for stability. The batch size is 8, i.e. we present 8 worlds simultaneously. 

36 

Published as a conference paper at ICLR 2023 

**==> picture [394 x 367] intentionally omitted <==**

Figure 14: All cells. A/B) Ratemaps from a ReLU model. A) A task with no objects. B) Task with objects. C/D) Ratemaps from a model with linear activation function. C) A task with no objects. D) Task with objects. 

37 

