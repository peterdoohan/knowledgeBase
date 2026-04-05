Published as a conference paper at ICLR 2023 

## ACTIONABLE NEURAL REPRESENTATIONS: GRID CELLS FROM MINIMAL CONSTRAINTS 

**William Dorrell, Peter Latham** Gatsby Unit, UCL dorrellwec@gmail.com 

**Timothy E.J. Behrens James C.R. Whittington** UCL & Oxford Oxford & Stanford jcrwhittington@gmail.com 

## ABSTRACT 

To afford flexible behaviour, the brain must build internal representations that mirror the structure of variables in the external world. For example, 2D space obeys rules: the same set of actions combine in the same way everywhere (step north, then south, and you won’t have moved, wherever you start). We suggest the brain must represent this consistent meaning of actions across space, as it allows you to find new short-cuts and navigate in unfamiliar settings. We term this representation an ‘actionable representation’. We formulate actionable representations using group and representation theory, and show that, when combined with biological and functional constraints - non-negative firing, bounded neural activity, and precise coding - multiple modules of hexagonal grid cells are the optimal representation of 2D space. We support this claim with intuition, analytic justification, and simulations. Our analytic results normatively explain a set of surprising grid cell phenomena, and make testable predictions for future experiments. Lastly, we highlight the generality of our approach beyond just understanding 2D space. Our work characterises a new principle for understanding and designing flexible internal representations: they should be actionable, allowing animals and machines to predict the consequences of their actions, rather than just encode. 

## 1 INTRODUCTION 

Animals should build representations that afford flexible behaviours. However, different representation make some tasks easy and others hard; representing red versus white is good for understanding wines but less good for opening screw-top versus corked bottles. A central mystery in neuroscience is the relationship between tasks and their optimal representations. Resolving this requires understanding the representational principles that permit flexible behaviours such as zero-shot inference. 

Here, we introduce **actionable representations** , a representation that permits flexible behaviours. Being actionable means encoding not only variables of interest, but also how the variable transforms. Actions cause many variables to transform in predictable ways. For example, actions in 2D space obey rules; north, east, south, and west, have a universal meaning, and combine in the same way everywhere. Embedding these rules into a representation of self-position permits deep inferences: having stepped north, then east, then south, an agent can infer that stepping west will lead home, having never taken that path - a zero-shot inference (Figure 1A). 

**==> picture [397 x 75] intentionally omitted <==**

Figure 1: **A** 2D space is defined by rules, e.g. at all positions north = _−_ south. **B** Left: Entorhinal grid cells are hexagonally tuned cells (orange). Different cells within a module are translated copies (orange/blue/green). Right: Different modules have different lattice scale (pink/blue/green). 

1 

Published as a conference paper at ICLR 2023 

Indeed biology represents 2D space in a structured manner. Grid cells in medial entorhinal cortex represent an abstracted ‘cognitive map’ of 2D space (Tolman, 1948). These cells fire in a hexagonal lattice of positions (Hafting et al., 2005), (Figure 1B), and are organised in modules; cells within one module have receptive fields that are translated versions of one another, and different modules have firing lattices of different scales and orientations (Figure 1B), (Stensola et al., 2012). 

Biological representations must be more than just actionable - they must be **functional** , encoding the world efficiently, and obey **biological** constraints. We formalise these three ideas - actionable, functional, and biological - and analyse the resulting optimal representations. We define _actionability_ using group and representation theory, as the requirement that each action has a corresponding matrix that linearly updates the representation; for example, the ‘step north’ matrix updates the representation to its value one step north. _Functionally_ , we want different points in space to be represented maximally differently, allowing inputs to be distinguished from one another. _Biologically_ , we ensure all neurons have non-negative and bounded activity. From this constrained optimisation problem we derive optimal representations that resemble multiple modules of grid cells. 

Our problem formulation allows analytic explanations for grid cell phenomena, matches experimental findings, such as the alignment of grids cells to room geometry (Stensola et al., 2015), and predicts some underappreciated aspects, such as the relative angle between modules. In sum, we 1) propose actionable neural representations to support flexible behaviours; 2) formalise the actionable constraint with group and representation theory; 3) mix actionability with biological and functional constraints to create a constrained optimisation problem; 4) analyse this problem and show that in 2D the optimal representation is a good model of grid cells, thus offering a mathematical understanding of why grid cells look the way they do; 5) provide several neural predictions; 6) highlight the generality of this normative method beyond 2D space. 

## 1.1 RELATED WORK 

Neuroscientists have long explained representations with normative principles like information maximisation (Attneave, 1954; Barlow et al., 1961), sparse (Olshausen & Field, 1996) or independent (Hyv¨arinen, 2010) latent encodings, often mixed with biological constraints such as non-negativity (Sengupta et al., 2018), energy budgets (Niven et al., 2007), or wiring minimisation (Hyv¨arinen et al., 2001). On the other hand, deep learning learns task optimised representations. A host of representation-learning principles have been considered (Bengio et al., 2013); but our work is most related to geometric deep learning (Bronstein et al., 2021) which emphasises input transformations, and building neural networks which respect (equivariant) or ignore (invariant) them. This is similar in spirit but not in detail to our approach, since equivariant networks do not build representations in which all transformations of the input are implementable through matrices. Most related are Paccanaro & Hinton (2001), who built representations in which relations (e.g. _**x**_ is the father of _**y**_ ) are enacted by a corresponding linear transform, exactly like our actionable! 

There is much previous theory on grid cells, which can be categorised as relating to our actionable, functional, and biological constraints. **Functional:** Many works argue that grid cells provide an efficient representation of position, that hexagons are optimal (Mathis et al., 2012a;b; Sreenivasan & Fiete, 2011; Wei et al., 2015) and make predictions for relative module lengthscales (Wei et al., 2015). Since we use similar functional principles, we suspect that some of our novel results, such as grid-to-room alignment, could have been derived by these authors. However, in contrast to our work, these authors assume a grid-like tuning curve. Instead we give a normative explanation of why be grid-like at all, explaining features like the alignment of grid axes within a module, which are detrimental from a pure decoding view (Stemmler et al., 2015). **Actionability:** Grid cells are thought to a basis for predicting future outcomes (Stachenfeld et al., 2017; Yu et al., 2020), and have been classically understood as affording path-integration (integrating velocity to predict position) with units from both hand-tuned Burak & Fiete (2009) and trained recurrent neural network resembling grid cells (Cueva & Wei, 2018; Banino et al., 2018; Sorscher et al., 2019). Recently, these recurrent network approaches have been questioned for their parameter dependence (Schaeffer et al., 2022), or relying on decoding place cells with bespoke shapes that are not observed experimentally (Sorscher et al., 2019; Dordek et al., 2016). Our mathematical formalisation of path-integration, combined with biological and functional constraints, provides clarity on this issue. Our approach is linear, in that actions update the representation linearly, which has previously been explored theoretically (Issa & Zhang, 2012), and numerically, in two works that learnt grid cells (Whittington et al., 2020; Gao 

2 

Published as a conference paper at ICLR 2023 

et al., 2021). Our work could be seen as extracting and simplifying the key ideas from these papers that make hexagonal grids optimal (see Appendix H), and extending them to multiple modules, something both papers had to hard code. **Biological:** Lastly, both theoretically (Sorscher et al., 2019) and computationally (Dordek et al., 2016; Whittington et al., 2021), non-negativity has played a key role in normative derivations of hexagonal grid cells, as it will here. 

## 2 ACTIONABLE NEURAL REPRESENTATIONS: AN OBJECTIVE 

We seek a representation _**g**_ ( _**x**_ ) _∈_ R _[N]_ of 2D position _**x** ∈_ T[2] , where _N_ is the number of neurons. Our representation is built using three ideas: functional, biological, and actionable; whose combination will lead to multiple modules of grid cells, and which we’ll now formalise. 

**Functional:** To be useful, the representation must encode different positions differently. However, it is more important to distinguish positions 1km apart than 1mm, and frequently visited positions should be separated the most. To account for these, we ask our representation to minimise 

**==> picture [300 x 23] intentionally omitted <==**

The red term measures the representational similarity of _**x**_ and _**x**[′]_ ; it is large if their representations are nearer than some distance _σ_ in neural space and small otherwise. By integrating over all pairs _**x**_ and _**x**[′]_ , _L_ measures the total representational similarity, which we seek to minimise. The green term is the agent’s position occupancy distribution, which ensures only visited points contribute to the loss, for now simply a Gaussian of lengthscale _L_ . Finally, the blue term weights the importance of separating each pair, encouraging separation of points more distant than a lengthscale, _l_ . 

**==> picture [292 x 17] intentionally omitted <==**

**Biological:** Neurons have non-negative firing rates, so we constrain _**g** i_ ( _**x**_ ) _≥_ 0. Further, neurons can’t fire arbitrarily fast, and firing is energetically costly, so we constrain each neuron’s response _gn_ ( _**x**_ ) via � _gn_[2][(] _**[x]**_[)] _[p]_[(] _**[x]**_[)] _[d]_ _**[x]**_[ = 1] 

**Actionable:** Our final constraint requires that the representation is actionable. This means each transformations of the input must have its own transformation in neural space, independent of position. For mathematical convenience we enact the neural transformation using a matrix. Labelling this matrix _**T**_ (∆ _**x**_ ) _∈_ R _[N][×][N]_ , for transformation ∆ _**x**_ , this means that for all positions _**x**_ , 

**==> picture [255 x 11] intentionally omitted <==**

For intuition into how this constrains the neural code _**g**_ ( _**x**_ ), we consider a simple example of two neurons representing an angle _θ ∈_ [0 _,_ 2 _π_ ). Replacing _**x**_ with _θ_ in equation 3 we get the equivalent constraint: _**g**_ ( _θ_ + ∆ _θ_ ) = _**T**_ (∆ _θ_ ) _**g**_ ( _θ_ ). Here the matrix _**T**_ performs a rotation, and the solution (up to a linear transform) is for _**T**_ to be the standard 2 _×_ 2 rotation matrix, with frequency _n_ . 

**==> picture [391 x 25] intentionally omitted <==**

Thus as _θ_ rotates by 2 _π_ the neural representation traces out a circle an integer number, _n_ , times. Thanks to the problem’s linearity, extending to more neurons is easy. Adding two more neurons lets the population contain another sine and cosine at some frequency, just like the two neurons in equation 4. Extrapolating this we get our actionability constraint: the neural response must be constructed from some invertible linear mixing of the sines and cosines of _D <[N]_ 2[frequencies,] 

**==> picture [328 x 31] intentionally omitted <==**

The vectors _{_ _**a** d,_ _**b** d}[D] d_ =1 _[∈]_[R] _[N]_[are][coefficient][vectors][that][mix][together][the][sines][and][cosines,][of] which there are _D_ . _**a**_ 0 is the coefficient vector for a frequency that cycles 0 times. 

This argument comes from an area of maths called Representation Theory (a different meaning of representation!) that places constraints on the matrices _**T**_ for variables whose transformations form a mathematical object called a group. This includes many of interest, such as position on a circle, 

3 

Published as a conference paper at ICLR 2023 

torus, or sphere. These constraints on matrices can be translated into constraints on an actionable neural code just like we did for _**g**_ ( _θ_ ) (see Appendix A). When generalising the above example to 2D space (a torus), we must consider a few things: First, the space is two-dimensional, so compared to our previous equation 5, the frequencies, denoted _**k** d_ , are now two dimensional. Second, to approximate a finite region of flat 2D space, we consider a similarly sized region of a torus. As the radius of the torus grows this approximation becomes arbitrarily good (see Appendix A.4 for discussion). Periodicity constrains the frequencies in equation 5 to be _R[n]_[for integer] _[ n]_[ and ring radius] _R_ . As the loop (torus in 2D) becomes very large these permitted frequencies become arbitrarily close, so we drop the integer constraint, 

**==> picture [299 x 30] intentionally omitted <==**

Our constrained optimisation problem is complete. Equation 6 specifies the set of actionable representations. Without additional constraints these codes are meaningless: random combinations of sines and cosines produce random neural responses (Figure 2A). We will choose from amongst the set of actionable codes by optimising the parameters _**a**_ 0 _, {_ _**a** d,_ _**b** d,_ _**k** d}[D] d_ =1[to minimise] _[ L]_[, subject to] biological (non-negative and bounded firing rates) constraints. 

## 3 OPTIMAL REPRESENTATIONS 

Optimising over the set of actionable codes to minimise _L_ with biological constraints gives multiple modules of grid cells (Figure 2B). This section will, using intuition and analytics, explain why. 

**==> picture [396 x 147] intentionally omitted <==**

Figure 2: **A** Random actionable representations (equation 6) are meaningless combinations of sines and cosines. ( _gn_ ( _**x**_ ) plotted for different neurons, _n_ ) **B** Optimising among actionable codes to achieve functional and biological constraints produces multiple modules of _∼_ hexagonal grid cells. (Figure 6 shows that all the neurons in the population belong to one of these three modules) 

## 3.1 NON-NEGATIVITY LEADS TO A MODULE OF LATTICE CELLS 

To understand how non-negativity produces modules of lattice responses we will study the following simplified loss, which maximises the _Euclidean distance_ between representations of angle, _**g**_ ( _θ_ ), 

**==> picture [283 x 25] intentionally omitted <==**

This is equivalent to the full loss (equation 1) for uniform _p_ ( _θ_ ), _χ_ ( _θ, θ[′]_ ) = 1, and _σ_ very large. Make no mistake, this is a bad loss. For contrast, the full loss encouraged the representations of different positions to be separated by more than _σ_ , enabling discrimination[1] . Therefore, sensibly, the representation is most rewarded for separating nearby (closer than _σ_ ) points. _L_ 0 does the opposite! It grows quadratically with separation, so _**g**_ ( _θ_ ) is most rewarded for pushing apart already wellseparated points, a terrible representational principle! Nonetheless, _L_ 0 will give us key insights. 

> 1 _σ_ could be interpreted as a noise level, or a minimum discriminable distance, then points should be far enough away for a downstream decoder to distinguish them. 

4 

Published as a conference paper at ICLR 2023 

Since actionability gives us a parameterised form of the representations (equation 5), we can compute the integrals to obtain the following constrained optimisation problem (details: Appendix C) 

**==> picture [401 x 49] intentionally omitted <==**

(8) 

Where _N_ is the number of neurons. This is now something we can understand. First, reminding ourselves that the neural code, _**g**_ ( _θ_ ), is made from a constant vector, _**a**_ 0, and _θ−_ dependent parts (equation 5; Figure 3A), we can see that _L_ 0 separates representations by encouraging the size of each varying part, _∥_ _**a** d∥_[2] + _∥_ _**b** d∥_[2] , to be maximised. This effect is limited by the firing rate bound, _∥_ _**a**_ 0 _∥_[2] _−_[1] 2 _[L]_[0][=] _[N]_[.][Thus, to minimise] _[ L]_[0][we must minimise the constant vector,] _**[ a]**_[0][.][This would] be easy without non-negativity (when any code with _∥_ _**a**_ 0 _∥_ = 0 is optimal), but no sum of sines and cosines can be non-negative for all _θ_ without an offset. Thus the game is simple; choose frequencies and coefficients so the firing rates are non-negative, but using the smallest possible constant vector. 

**==> picture [314 x 225] intentionally omitted <==**

Figure 3: **A** The neural activity consists of a constant vector, _**a**_ 0, and _θ−_ dependent loops. **B** Progressively adding harmonic frequencies increases the code’s minima, allowing the code to be made non-negative using the smallest possible _**a**_ 0. This give a grid-like tuning curve. Simulations results confirm this heuristic in **C** 1D and **D** 2D, right: frequency spectrum, 2D dot size is frequency power. 

**One lattice cell** . We now heuristically argue, and confirm in simulation, that the optimal solution for a single neuron is a lattice tuning curve (see Appendix G for why this problem is non-convex). Starting with a single frequency component, e.g. sin( _θ_ ), achieving non-negativity requires adding a constant offset, sin( _θ_ ) + 1 (Figure 3B). However, we could also have just added another frequency. In particular adding harmonics of the base frequency (with appropriate phase shifts) pushes up the minima (Figure 3B). Extending this argument, we suggest non-negativity, for a single cell, can be achieved by including a grid of frequencies. This gives a lattice tuning curve (Figure 3B right). 

**Module of lattice cells** . Achieving non-negativity for this cell used up many frequencies. But as discussed (Section 2), actionability only allows a limited number frequencies in the population ( _<[N]_ 2 since each frequency uses 2 neurons (sine and cosine)), thus how can we make lots of neurons nonnegative with limited frequencies? Fortunately, we can do so by making all neuron’s tuning curves translated versions of each other, as translated curves contain the same frequencies but with different phases. This is a module of lattice cells. We validate our arguments by numerically optimising the coefficients _**a**_ 0 _, {_ _**a** d,_ _**b** d}[D] d_ =1[and][frequencies] _[{][n][d][}][D] d_ =1[to][minimise] _[L]_[0][subject][to][constraints,] producing a module of lattices (Figure 3C; details in Appendix B). These arguments equally apply to representations of a periodic 2D space (a torus; Figure 3D). 

5 

Published as a conference paper at ICLR 2023 

Studying _L_ 0 has told us why lattice response curves are good. But surprisingly, all lattices are equally good, even at infinitely high frequency. Returning to the full loss will break this degeneracy. 

## 3.2 PRIORITISING IMPORTANT PAIRS OF POSITIONS PRODUCES HEXAGONAL GRID CELLS 

Now we return to the full loss and understand its impact in two steps, beginning with the reintroduction of _χ_ and _p_ , which break the lattice degeneracy, forming hexagonal grid cells. 

**==> picture [305 x 25] intentionally omitted <==**

_χ_ **prefers low frequencies:** recall that _χ_ = 1 _− e[−][∥]_ _**[x]**[−]_ 2 _l_ _**[x]**_[2] _[′][∥]_[2] ensures very distant inputs have different representations, while allowing similar inputs to have similar representations, up to a resolution, _l_ . This encourages low frequencies ( _∥_ _**k** d∥ <_[1] _l_[), which separate distant points but produce similar rep-] resentations for pairs closer than _l_ (Analytics: Appendix D.1). At this stage, for periodic 2D space, the lowest frequency lattices, place cells, are optimal (see Appendix F; Sengupta et al. (2018)). 

_p_ ( _**x**_ ) **prefers high frequencies:** However, the occupancy distribution of the animal, _p_ ( _**x**_ ), counters _χ_ . On an infinite 2D plane animals must focus on representing a limited area, of lengthscale _L_ . This encourages high frequencies ( _∥_ _**k** d∥ > L_ 1[),][whose][response][varies][among][the][visited][points] (Analytics: Appendix D.2). More complex _p_ ( _x_ ) induce more complex frequency biases, but, to first order, the effect is always a high frequency bias (Figure 5F-G, Appendix L). 

**==> picture [342 x 193] intentionally omitted <==**

Figure 4: **A** _χ_ and _p_ ( _**x**_ ) induce a bias towards frequencies with magnitudes between _L_ 1[and][1] _l_[.] Since, of all lattices, hexagons fit the most frequencies within the annulus, they are preferred, and hexagonal frequency lattices lead to hexagonal grid cells. **B** Simulations confirm. **C** Harmonically related frequencies co-repeat more often than non-harmonic, meaning that, as a pair, harmonically related frequencies are worse at encoding, since they encode many points in the same way. 

**Combination** _→_ **Hexagons:** Satisfying non-negativity and functionality required a lattice of many frequencies, but now _p_ and _χ_ bias our frequency choice, preferring those beyond _L_[1][(to][separate] points the animal visits) but smaller than[1] _l_[(to separate distant visited points).][Thus to get as many] of these preferred frequencies as possible, we want the lattice with the densest packing within a Goldilocks annulus in frequency space (Figure 4A). This is a hexagonal lattice in frequency space which leads to a hexagonal grid cell. Simulations with few neurons agree, giving a module of hexagonal grid cells (Figure 4B). 

## 3.3 A HARMONIC TUSSLE PRODUCES MULTIPLE MODULES 

Finally, we will study the neural lengthscale _σ_ , and understand how it produces multiple modules. 

**==> picture [304 x 25] intentionally omitted <==**

6 

Published as a conference paper at ICLR 2023 

As discussed, _L_ prioritises the separation of poorly distinguished points, those whose representations are closer than _σ_ . This causes certain frequencies to be desired _in the overall population_ , in particular those unrelated to existing frequencies by simple harmonic ratios, i.e. not _ω_ 1 =[3] 2 _[ω]_[2][(Figure][4C;] see Appendix E for a perturbative derivation of this effect). This is because pairs of harmonically related frequencies represent more positions identically than a non-harmonically related pair, so are worse for separation (similar to arguments made in Wei et al. (2015)). 

This, however, sets up a ‘harmonic tussle’ between what the population wants - non-harmonically related frequencies for _L_ - and what single neurons want - harmonically related frequency lattices for non-negativity (Section 3.1). Modules of grid cells resolve this tension: harmonic frequencies exist within modules to give non-negativity, and non-harmonically related modules allow for separation, explaining the earlier simulation results (Figure 2B; further details in Appendix E.3). 

This concludes our main result. We have shown three constraints on neural populations - actionable, functional, and biological - lead to multiple modules of hexagonal grid cells, and we have understood why. We posit this is the minimal set of requirements for grid cells (see Appendix I for ablations simulations and discussion). 

## 4 PREDICTIONS 

Our theory makes testable predictions about the structure of optimal actionable codes for 2D space. We describe three here: tuning curve sharpness scales with the number of neurons in a module; the optimal angle between modules; and the optimal grid alignment to room geometry. 

## 4.1 LATTICE SIZE:FIELD WIDTH RATIO SCALES WITH NUMBER OF NEURONS IN MODULE 

In our framework the number of neurons controls the number of frequencies in the representation (equation 6). A neuron within a module only contains frequencies from that module’s frequency lattice, since other modules have non-harmonically related frequencies. More neurons in a module, means more and higher frequencies in the lattice, which sharpen grid peaks (Figure 5A). We formalise this (Appendix J) and predict that the number of neurons within a module scales with the square of the lattice lengthscale, _ν_ , to field width, _µ_ , ratio, _N ∝_ � _µν_ �2. This matches the intuition that the sharper a module’s peak, the more neurons you need to tile the entire space. In a rudimentary analysis, our predictions compare favourably to data from Stensola et al. (2012) assuming uniform sampling of grid cells across modules (Figure 5B). We are eager to test these claims quantitatively. 

## 4.2 MODULES ARE OPTIMALLY ORIENTED AT SMALL OFFSETS ( _∼_ 4 _[◦]_ ) 

In section 3.3 we saw how frequencies of different modules are maximally non-harmonically related in order to separate the representation of as many points as possible. To maximise non-harmonicity between two modules, the second module’s frequency lattice can be both stretched _and_ rotated relative to the first. 0 or 30 _[◦]_ relative orientations are particularly bad coding choices as they align the high density axes of the two lattices (Figure 5C). The optimal angular offset of two modules, calculated via a frequency overlap metric (Appendix K), is small (Figure 5D); the value depends on the grid peak and lattice lengthscales, _µ_ and _ν_ , but varies between 3 _[◦]_ and 8 _[◦]_ degrees. Multiple modules should orient at a sequence of small angles (Appendix K). In a rudimentary analysis, our predictions compare favourably to the observations of Stensola et al. (2012) (Figure 5E). 

## 4.3 OPTIMAL GRIDS MORPH TO ROOM GEOMETRY 

In Section 3.2 (and Appendix D) we showed that _p_ ( _x_ ), the animal’s occupancy distribution, introduced a high frequency bias - grid cells must peak often enough to encode visited points. However, changing _p_ ( _x_ ) changes the shape of this high frequency bias (Appendix L). In particular, we examine an animal’s encoding of square, circular, or rectangular environments, Appendix L, with the assumption that _p_ ( _x_ ) is uniform over that space. In each case the bias is coarsely towards high frequencies, but has additional intricacies: in square and rectangular rooms optimal frequencies lie on a lattice, with peaks at integer multiples of[2] _L[π]_[along one of the cardinal axes, for room width/height] _L_ (Figure 5F); whereas in circular rooms optima are at the zeros of a Bessel function (Figure 5G). 

7 

Published as a conference paper at ICLR 2023 

**==> picture [394 x 499] intentionally omitted <==**

Figure 5: **A** Adding neurons to a module sharpens the grid peaks. **B** In data from Stensola et al. (2012) the most sharply peaked grids were recorded most often (2nd from left), and the broadest the least (rightmost). **C** Aligning the high-density axes of two lattices creates high overlap, while small offsets minimise it. **D** We quantified the overlap as a function of offset angle (Appendix K) and found the minima occured at _∼_ 4 _[◦]_ from aligned (aligned = 6 maxima, 4 _[◦]_ offsets are the 12 minima). **E** The orientation and spacing of all grids in animals with multiple modules recorded by Stensola et al. (2012). Many modules are misaligned by small offsets, matching our prediction. **F** Square or **G** circular rooms create complex frequency biases, _L_ ( _**k**_ ) is the loss for a one frequency code of fixed amplitude. **H** The optimal frequencies along one axis of a box occur at[2] _[πn] L_[for integer] _[ n]_[:][Squishing] a room makes the optimal frequencies expand. Grids should change to fit the optimal patterns in the recorded environment, unless they happen to be optimal for both, as[6] _L[π]_[is.] **[I]**[ Most grid cells scale] with the room, but, when one side is squashed by a factor of 2/3, those at[6] _L[π]_[are stable.] 

8 

Published as a conference paper at ICLR 2023 

These ideas make several predictions. For example, grid modules in circular rooms should have lengthscales set by the optimal radii in Figure 5G, but they should still remain hexagonal since the Bessel function is circularly symmetric. However, the optimal representation in square rooms should not be perfectly hexagonal since _p_ ( _x_ ) induces a bias inconsistent with a hexagonal lattice (this effect is negligible for high frequency grids). Intriguingly, shearing towards squarer lattices is observed in square rooms (Stensola et al., 2015), and it would be interesting to test its grid-size dependence. 

Lastly, these effects make predictions about how grid cells morph when the environment geometry changes. A grid cell that is optimal in both geometries can remain the same, however sub-optimal grid cells should change. For example turning a square into a squashed square (i.e. a rectangle), stretches the optimal frequencies along the squashed dimension. Thus, some cells are optimal in both rooms and should stay stable, will others will change, presumably to nearby optimal frequencies (Figure 5H). Indeed Stensola et al. (2012) recorded the same grid cells in a square and rectangular environment (Figure 5I), and observed exactly these phenomena. 

## 5 DISCUSSION & CONCLUSIONS 

We have proposed actionability as a fundamental representational principle to afford flexible behaviours. We have shown in simulation and with analytic justification that the optimal actionable representations of 2D space are, when constrained to be both biological and functional, multiple modules of hexagonal grid cells, thus offering a mathematical understanding of grid cells. We then used this theory to make three novel grid cell predictions that match data on early inspection. 

While this is promising for our theory, there remain some grid cell phenomena that, as it stands, it will never predict. For example, grid cell peaks vary in intensity (Dunn et al., 2017), and grid lattices bend in trapezoidal environments (Krupic et al., 2015). These effects may be due to incorporation of sensory information or uncertainty - things we have not included - to better infer position. Including these may recapitulate these findings, similar to Ocko et al. (2018) and Kang et al. (2023). 

Our theory is normative and abstracted from implementation. However, both modelling (Burak & Fiete, 2009) and experimental (Gardner et al., 2022; Kim et al., 2017) work suggests that continuous attractor networks (CANs) implement path integrating circuits. Actionability and CANs imply seemingly different representation update equations; future work could usefully compare the two. 

While we focused on understanding the optimal representations of 2D space and their relationship to grid cells, our theory is more general. Most simply, it can be applied to behaviour in other, non 2D, spaces. In fact many variables whose transformations form a group are relatively easily analysed. The brain represents many such variables, e.g. heading directions, (Finkelstein et al., 2015), object orientations, (Logothetis et al., 1995), the‘4-loop task’ of Sun et al. (2020) or 3-dimensional space (Grieves et al., 2021; Ginosar et al., 2021). Interestingly, our theory predicts 3D representations with regular order (Figure 19E in Appendix M), unlike those found in the brain (Grieves et al., 2021; Ginosar et al., 2021) suggesting the animal’s 3D navigation is sub-optimal. 

Further, the brain represents these differently-structured variables not one at a time, but simultaneously; at times mixing these variables into a common representation (Hardcastle et al., 2017), at others giving each variable its own set of neurons (e.g. grid cells, object-vector cells Høydal et al. (2019)). Thus, one potential concern about our work is that it assumes a separate neural population represents each variable. However, in a companion paper, we show that our same biological and functional constraints encourage any neural representation to encode independent variables in separate sub-populations (Whittington et al., 2023), to which our theory can then be cleanly applied. 

But, most expansively, these principles express a view that representations must be more than just passive encodings of the world; they must embed the consequences of predictable actions, allowing planning and inferences in never-before-seen situations. We codified these ideas using Group and Representation theory, and demonstrated their utility in understanding grid cells. However, the underlying principle is broader than the crystalline nature of group structures: the world and your actions within it have endlessly repeating structures whose understanding permits creative analogising and flexible behaviours. A well-designed representation should reflect this. 

9 

Published as a conference paper at ICLR 2023 

## ACKNOWLEDGEMENTS 

We thank Cengiz Pehlevan for insightful discussions, the Parietal Team at INRIA for helpful comments on an earlier version of this work, Changmin Yu for reading a draft of this work, the Mathematics Stack Exchange user Roger Bernstein for pointing us to equation 69, and Pierre Glaser for teaching the ways of numpy array broadcasting. We thank the following funding sources: the Gatsby Charitable Foundation to W.D.; the Gatsby Charitable Foundation and Wellcome Trust (110114/Z/15/Z) to P.E.L.; Wellcome Principal Research Fellowship (219525/Z/19/Z), Wellcome Collaborator award (214314/Z/18/Z), and Jean-Franc¸ois and Marie-Laure de Clermont-Tonnerre Foundation award (JSMF220020372) to T.E.J.B.; Sir Henry Wellcome Post-doctoral Fellowship (222817/Z/21/Z) to J.C.R.W.; the Wellcome Centre for Integrative Neuroimaging and Wellcome Centre for Human Neuroimaging are each supported by core funding from the Wellcome Trust (203139/Z/16/Z, 203147/Z/16/Z). 

## REFERENCES 

- Fred Attneave. Some informational aspects of visual perception. _Psychological review_ , 61(3):183, 1954. 

- Andrea Banino, Caswell Barry, Benigno Uria, Charles Blundell, Timothy Lillicrap, Piotr Mirowski, Alexander Pritzel, Martin J Chadwick, Thomas Degris, Joseph Modayil, et al. Vector-based navigation using grid-like representations in artificial agents. _Nature_ , 557(7705):429–433, 2018. 

- Horace B Barlow et al. Possible principles underlying the transformation of sensory messages. _Sensory communication_ , 1(01), 1961. 

- Yoshua Bengio, Aaron Courville, and Pascal Vincent. Representation learning: A review and new perspectives. _IEEE transactions on pattern analysis and machine intelligence_ , 35(8):1798–1828, 2013. 

- Michael M Bronstein, Joan Bruna, Taco Cohen, and Petar Velickovic. Geometric deep learning: Grids, groups, graphs, geodesics, and gauges. _arXiv preprint arXiv:2104.13478_ , 2021. 

- Yoram Burak and Ila R Fiete. Accurate path integration in continuous attractor network models of grid cells. _PLoS computational biology_ , 5(2):e1000291, 2009. 

- Christopher J Cueva and Xue-Xin Wei. Emergence of grid-like representations by training recurrent neural networks to perform spatial localization. _arXiv preprint arXiv:1803.07770_ , 2018. 

- Yedidyah Dordek, Daniel Soudry, Ron Meir, and Dori Derdikman. Extracting grid cell characteristics from place cell inputs using non-negative principal component analysis. _Elife_ , 5:e10094, 2016. 

- Bogdan Dumitrescu. _Positive trigonometric polynomials and signal processing applications_ , volume 103. Springer, 2007. 

- Benjamin Dunn, Daniel Wennberg, Ziwei Huang, and Yasser Roudi. Grid cells show field-to-field variability and this explains the aperiodic response of inhibitory interneurons. _arXiv preprint arXiv:1701.04893_ , 2017. 

- Arseny Finkelstein, Dori Derdikman, Alon Rubin, Jakob N Foerster, Liora Las, and Nachum Ulanovsky. Three-dimensional head-direction coding in the bat brain. _Nature_ , 517(7533):159– 164, 2015. 

William Fulton and Joe Harris. _Representation Theory: A First Course_ . Springer-Verlag, 1991. 

- Ruiqi Gao, Jianwen Xie, Xue-Xin Wei, Song-Chun Zhu, and Ying Nian Wu. On path integration of grid cells: isotropic metric, conformal embedding and group representation. _Advances in neural information processing systems_ , 34, 2021. 

- Richard J Gardner, Erik Hermansen, Marius Pachitariu, Yoram Burak, Nils A Baas, Benjamin A Dunn, May-Britt Moser, and Edvard I Moser. Toroidal topology of population activity in grid cells. _Nature_ , 602(7895):123–128, 2022. 

10 

Published as a conference paper at ICLR 2023 

- Gily Ginosar, Johnatan Aljadeff, Yoram Burak, Haim Sompolinsky, Liora Las, and Nachum Ulanovsky. Locally ordered representation of 3d space in the entorhinal cortex. _Nature_ , 596 (7872):404–409, 2021. 

- Roddy M Grieves, Selim Jedidi-Ayoub, Karyna Mishchanchuk, Anyi Liu, Sophie Renaudineau, ´El´eonore Duvelle, and Kate J Jeffery. Irregular distribution of grid cell firing fields in rats exploring a 3d volumetric space. _Nature neuroscience_ , 24(11):1567–1573, 2021. 

- Torkel Hafting, Marianne Fyhn, Sturla Molden, May-Britt Moser, and Edvard I Moser. Microstructure of a spatial map in the entorhinal cortex. _Nature_ , 436(7052):801–806, 2005. 

- Kiah Hardcastle, Niru Maheswaranathan, Surya Ganguli, and Lisa M Giocomo. A multiplexed, heterogeneous, and adaptive code for navigation in medial entorhinal cortex. _Neuron_ , 94(2): 375–387, 2017. 

- Aapo Hyv¨arinen. Statistical models of natural images and cortical visual representation. _Topics in Cognitive Science_ , 2(2):251–264, 2010. 

- Aapo Hyv¨arinen, Patrik O Hoyer, and Mika Inki. Topographic independent component analysis. _Neural computation_ , 13(7):1527–1558, 2001. 

- Øyvind Arne Høydal, Emilie Ranheim Skytøen, Sebastian Ola Andersson, May-Britt Moser, and Edvard Ingjald Moser. Object-vector coding in the medial entorhinal cortex. _Nature_ , 568(7752): 400–404, 2019. 

- John B Issa and Kechen Zhang. Universal conditions for exact path integration in neural systems. _Proceedings of the National Academy of Sciences_ , 109(17):6716–6720, 2012. 

- Joseph Ivanic and Klaus Ruedenberg. Rotation matrices for real spherical harmonics. direct determination by recursion. _The Journal of Physical Chemistry_ , 100(15):6342–6347, 1996. 

- Joseph Ivanic and Klaus Ruedenberg. Rotation matrices for real spherical harmonics. direct determination by recursion. _The Journal of Physical Chemistry A_ , 102(45):9099–9100, 1998. 

- Yul HR Kang, Daniel M Wolpert, and M´at´e Lengyel. Spatial uncertainty and environmental geometry in navigation. _bioRxiv_ , pp. 2023–01, 2023. 

- Sung Soo Kim, Herv´e Rouault, Shaul Druckmann, and Vivek Jayaraman. Ring attractor dynamics in the drosophila central brain. _Science_ , 356(6340):849–853, 2017. 

- Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. _arXiv preprint arXiv:1412.6980_ , 2014. 

Anthony W. Knapp. _Lie Groups Beyond an Introduction_ . Springer, 2002. 

- Julija Krupic, Marius Bauza, Stephen Burton, Caswell Barry, and John O’Keefe. Grid cell symmetry is shaped by environmental geometry. _Nature_ , 518(7538):232–235, 2015. 

- Nikos K Logothetis, Jon Pauls, and Tomaso Poggio. Shape representation in the inferior temporal cortex of monkeys. _Current biology_ , 5(5):552–563, 1995. 

- Alexander Mathis, Andreas VM Herz, and Martin Stemmler. Optimal population codes for space: grid cells outperform place cells. _Neural computation_ , 24(9):2280–2317, 2012a. 

- Alexander Mathis, Andreas VM Herz, and Martin B Stemmler. Resolution of nested neuronal representations can be exponential in the number of neurons. _Physical review letters_ , 109(1): 018103, 2012b. 

- Jeremy E Niven, John C Anderson, and Simon B Laughlin. Fly photoreceptors demonstrate energyinformation trade-offs in neural coding. _PLoS biology_ , 5(4):e116, 2007. 

- Samuel A Ocko, Kiah Hardcastle, Lisa M Giocomo, and Surya Ganguli. Emergent elasticity in the neural code for space. _Proceedings of the National Academy of Sciences_ , 115(50):E11798– E11806, 2018. 

11 

Published as a conference paper at ICLR 2023 

Bruno A Olshausen and David J Field. Emergence of simple-cell receptive field properties by learning a sparse code for natural images. _Nature_ , 381(6583):607–609, 1996. 

- Alberto Paccanaro and Geoffrey E Hinton. Learning hierarchical structures with linear relational embedding. _Advances in neural information processing systems_ , 14, 2001. 

- Cengiz Pehlevan and Dmitri B Chklovskii. Neuroscience-inspired online unsupervised learning algorithms: Artificial neural networks. _IEEE Signal Processing Magazine_ , 36(6):88–96, 2019. 

Archontis Politis et al. Microphone array processing for parametric spatial audio techniques. 2016. 

Danilo Jimenez Rezende and Fabio Viola. Taming vaes. _arXiv preprint arXiv:1810.00597_ , 2018. 

- Rylan Schaeffer, Mikail Khona, and Ila Fiete. No free lunch from deep learning in neuroscience: A case study through models of the entorhinal-hippocampal circuit. _ICML 2022 Workshop AI4Science_ , 2022. 

- Anirvan Sengupta, Cengiz Pehlevan, Mariano Tepper, Alexander Genkin, and Dmitri Chklovskii. Manifold-tiling localized receptive fields are optimal in similarity-preserving neural networks. _Advances in neural information processing systems_ , 31, 2018. 

- Ben Sorscher, Gabriel Mel, Surya Ganguli, and Samuel Ocko. A unified theory for the origin of grid cells through the lens of pattern formation. _Advances in neural information processing systems_ , 32, 2019. 

- Ben Sorscher, Gabriel C Mel, Aran Nayebi, Lisa Giocomo, Daniel Yamins, and Surya Ganguli. When and why grid cells appear or not in trained path integrators. _bioRxiv_ , 2022. 

- Sameet Sreenivasan and Ila Fiete. Grid cells generate an analog error-correcting code for singularly precise neural computation. _Nature neuroscience_ , 14(10):1330–1337, 2011. 

- Kimberly L Stachenfeld, Matthew M Botvinick, and Samuel J Gershman. The hippocampus as a predictive map. _Nature neuroscience_ , 20(11):1643–1653, 2017. 

- Martin Stemmler, Alexander Mathis, and Andreas VM Herz. Connecting multiple spatial scales to decode the population activity of grid cells. _Science Advances_ , 1(11):e1500816, 2015. 

- Hanne Stensola, Tor Stensola, Trygve Solstad, Kristian Frøland, May-Britt Moser, and Edvard I Moser. The entorhinal grid map is discretized. _Nature_ , 492(7427):72–78, 2012. 

- Tor Stensola, Hanne Stensola, May-Britt Moser, and Edvard I Moser. Shearing-induced asymmetry in entorhinal grid cells. _Nature_ , 518(7538):207–212, 2015. 

- Chen Sun, Wannan Yang, Jared Martin, and Susumu Tonegawa. Hippocampal neurons represent events as transferable units of experience. _Nature neuroscience_ , 23(5):651–663, 2020. 

Edward C Tolman. Cognitive maps in rats and men. _Psychological review_ , 55(4), 1948. 

Xue-Xin Wei, Jason Prentice, and Vijay Balasubramanian. A principle of economy predicts the functional architecture of grid cells. _Elife_ , 4:e08362, 2015. 

- James C. R. Whittington, Will Dorrell, Surya Ganguli, and Timothy Behrens. Disentanglement with biological constraints: A theory of functional cell types. In _The Eleventh International Conference on Learning Representations_ , 2023. URL https://openreview.net/forum?id=9Z_ GfhZnGH. 

- James CR Whittington, Timothy H Muller, Shirley Mark, Guifen Chen, Caswell Barry, Neil Burgess, and Timothy EJ Behrens. The tolman-eichenbaum machine: unifying space and relational memory through generalization in the hippocampal formation. _Cell_ , 183(5):1249–1263, 2020. 

- James CR Whittington, Joseph Warren, and Timothy EJ Behrens. Relating transformers to models and neural representations of the hippocampal formation. _arXiv preprint arXiv:2112.04035_ , 2021. 

- Changmin Yu, Timothy EJ Behrens, and Neil Burgess. Prediction and generalisation over directed actions by grid cells. _arXiv preprint arXiv:2006.03355_ , 2020. 

12 

Published as a conference paper at ICLR 2023 

## A CONSTRAINING REPRESENTATIONS WITH REPRESENTATION THEORY 

Having an actionable code means the representational effect of every transformation of the variable, ∆ _**x**_ , can be implemented by a matrix: 

**==> picture [254 x 11] intentionally omitted <==**

In Section 2 we outlined a rough argument for how this equation leads to the following constraint on actionable representations of 2D position, that was vital for our work: 

**==> picture [298 x 31] intentionally omitted <==**

In this section, we’ll repeat this argument more robustly using Group and Representation Theory. In doing so, it’ll become clear how broadly our version of actionability can be used to derive clean analytic representational constraints; namely, the arguments presented here can be applied to the representation of any variable whose transformations form a group whose representations are well understood. 

Sections A.1 and A.2 contain a review of the Group and Representation theory used. Section A.3 applies it to our problem. 

## A.1 GROUP THEORY 

A mathematical group is a collection of things (like the set of integers), and a way to combine two members of the group that makes a third (like addition of two integers, that always creates another integer), in a way that satisfies a few rules: 

1. There is an identity element, which is a member of the group that when combined with any other element doesn’t change it. For adding integers the identity element is 0, since _a_ + 0 = _a_ for all _a_ . 

2. Every member of the group has an inverse, defined by its property that combining an element with its inverse produces the identity element. In our integer-addition example the inverse of any integer _a_ is _−a_ , since _−a_ + _a_ = 0, and 0 is the identity element. 

3. Associativity applies, which just means the order in which you perform operations doesn’t matter: ( _a_ + _b_ ) + _c_ = _a_ + ( _b_ + _c_ ) 

Groups are ubiquitous. We mention them here because they will be our route to understanding actionable representations - representations in which transformations are also encoded consistently. The set of transformations of many variables of interest are groups. For example, the set of transformations of 2D position, i.e. 2D translations - ∆ _**x**_ , is a group if you define the combination of two translations via simple vector addition, ∆ _**x**_ 1+2 = ∆ _**x**_ 1 + ∆ _**x**_ 2. We can easily check that they satisfy all three of the group rules: 

1. There is an identity translation: simply add **0** . 

2. Each 2D translation has its inverse: _−_ ∆ _**x**_ + ∆ _**x**_ = **0** 

3. Associativity: (∆ _**a**_ + ∆ _**b**_ ) + ∆ _**c**_ = ∆ _**a**_ + (∆ _**b**_ + ∆ _**c**_ ) 

The same applies for the transformations of an angle, _θ_ , or of positions on a torus or sphere, and much else besides. This is a nice observation, but in order to put it to work we need a second area of mathematics, Representation Theory. 

## A.2 REPRESENTATION THEORY 

Groups are abstract, in the sense that the behaviour of many different mathematical objects can embody the same group. For example, the integers modulo _P_ with an addition combination rule 

13 

Published as a conference paper at ICLR 2023 

2 _πn_ form a group, called _CP_ . But equally, the _P_ roots of unity ( _{e P }[P] n_ =0 _[ −]_[1][)][with][a][multiplication] combination rule obey all the same rules: you can create a 1-1 correspondence between the integers 0 through _P −_ 1 and the _P_ roots of unity by labelling all the roots with the integer _n_ that appears 2 _πn_ in the exponent _e P_ , and, under their respective combination rules, all additions of integers will 2 _πn_ 1 2 _πn_ 2 2 _π_ mod _P_ ( _n_ 1+ _n_ 2) exactly match onto multiplication of complex roots (i.e. _e P ∗ e P_ = _e P_ ) 

In this work we’ll be interested in a particular instantiation of our groups, defined by sets of matrices, _**T**_ (∆ _**x**_ ), combined using matrix multiplication. For example, a matrix version of the group _CP_ would be the set of 2-by-2 rotation matrices that rotate by[2] _P[π]_[increments:] 

**==> picture [386 x 25] intentionally omitted <==**

Combining these matrices using matrix multiplication follows all the same patterns that adding the integers modulo P, or multiplying the P roots of unity, followed; they all embody the same group. 

Representation theory is the branch of mathematics that specifies the structure of sets of matrices that, when combined using matrix multiplication, follow the rules of a particular group. Such sets of matrices are called a representation of the group; to avoid confusion arising from this unfortunate though understandable convergent terminology, we distinguish group representations from neural representations by henceforth denoting _representations_ of a group in italics. We will make use of one big result from _Representation_ Theory, hinted at in Section 2: the Peter-Weyl theorem (Knapp, 2002). For compact topological groups (which include transformations of a point on a circle, torus, and sphere) any matrix that is a _representation_ of a group can be composed from the direct product of a set of blocks, called irreducible _representations_ , or _irreps_ for short, up to a linear transformation. i.e. if _**T**_ (∆ _**a**_ ) is a _representation_ of the group of transformations of some variable _**a**_ : 

**==> picture [332 x 62] intentionally omitted <==**

where _Id_ (∆ _**a**_ ) are the _irreps_ of the group in question, which are square matrices not necessarily of the same size as _d_ varies, and _**S**_ is some invertible square matrix. 

To motivate our current rabbit hole further, this is exactly the result we hinted towards in Section 2. We discussed _**T**_ (∆ _θ_ ), and, in 2-dimensions, argued it was, up to a linear transform, the 2-dimensional rotation matrix. Further, we discussed how every extra two neurons allowed you to add another frequency, i.e. another rotation matrix. This was an attempt to motivate the plausibility of the Peter-Weyl theorem: the rotation matrices are the _irreps_ of the group of transformations of an angle, and adding two neurons allows you to create a larger _**T**_ (∆ _θ_ ) by stacking rotation matrices on top of one another. Now including the invertible linear transform, _**S**_ , we can state the 4-dimensional version of equation 4: 

**==> picture [356 x 44] intentionally omitted <==**

In performing this decomposition the role of the rotation matrices as _irreps_ is clear. There are infinitely many types, each specified by an integer frequency, _nd_ , and their direct product produces any _representation_ of the rotation group. 

We can now return to actionable neural representations of periodic 2D space, a torus, where this theorem comes in very useful. We sought codes, _**g**_ ( _**x**_ ), that could be manipulated via matrices: 

_**g**_ ( _**x**_ + ∆ _**x**_ ) = _**T**_ (∆ _**x**_ ) _**g**_ ( _**x**_ ) (16) 

14 

Published as a conference paper at ICLR 2023 

Now we recognise that we’re asking _**T**_ (∆ _**x**_ ) to be a _representation_ of the transformation group of _**x**_ , and we know the shape _**T**_ (∆ _**x**_ ) must take to fit this criteria. To specify _**T**_ (∆ _**x**_ ) from this constrained class we must simply choose a set of _irreps_ that fill up the dimensionality of the neural space, stack them one on top of each other, and rotate and scale them using the matrix _**S**_ . 

A final detail is that there is a trivial way to make a _representation_ of any group: choose _**T**_ ( _θ_ ) = I _N_ , the N-by-N identity matrix. This also fits our previous discussion, but corresponds to a representation made from the direct product of _N_ copies of something called the trivial _irrep_ , a 1-dimensional _irrep_ , _I_ trivial(∆ _**a**_ ) = 1. 

Armed with this knowledge, the following subsection will show how this theory can be used to constrain the neural code, _**g**_ ( _**x**_ ). To finish this review subsection, we list the non-trivial _irreps_ of the groups used in this work. To be specific, in all our work we use only the real-valued _irreps_ , i.e all elements of _**T**_ are real numbers, since firing rates are real numbers. These are less common than complex _irreps_ , which is often what is implied by the simple name _irreps_ . 

|Transformationgroupof which variable|Non-trivial Real_Irreps_|
|---|---|
|An angle on a unit circle,_θ_<br>Position on a very big circle_≈_a line,_x_<br>Angles on a unit torus,**_θ_**<br>Position on a very big torus_≈_plane,**_x_**<br>Position on a unit sphere, _φ_|�<br>cos(_n_∆_θ_)<br>_−_sin(_n_∆_θ_)<br>sin(_n_∆_θ_)<br>cos(_n_∆_θ_)<br>�<br>for_n ∈_Z<br>�<br>cos(_ω_∆_θ_)<br>_−_sin(_ω_∆_θ_)<br>sin(_ω_∆_θ_)<br>cos(_ω_∆_θ_)<br>�<br>for_ω ∈_R<br>�<br>cos(**_a_**_·_∆**_θ_**)<br>_−_sin(**_a_**_·_∆**_θ_**)<br>sin(**_a_**_·_∆**_θ_**)<br>cos(**_a_**_·_∆**_θ_**)<br>�<br>for**_a_**_∈_Z2<br>�<br>cos(**_k_**_·_∆**_x_**)<br>_−_sin(**_k_**_·_∆**_x_**)<br>sin(**_k_**_·_∆**_x_**)<br>cos(**_k_**_·_∆**_x_**)<br>�<br>for**_k_**_∈_R2<br>Real Wigner-D Matrices|



Proofs and discussions for deriving these _irreps_ of the circle, torus, and sphere transformation groups can be found in any textbook on the _representation_ theory of compact Lie Groups (e.g. Knapp (2002)). The step from complex to real _irreps_ can be done using the Frobenius-Schur indicator, which gives a recipe for mapping from the complex _irreps_ of a compact group to the real _irreps_ (Fulton & Harris, 1991). The real Wigner D-Matrices were calculated recursively as detailed in Ivanic & Ruedenberg (1996; 1998), by translating matlab code from Politis et al. (2016) into python. 

Our derivations of the _irreps_ on the very large circle and torus are simple. In 1D the constraint that the frequencies _n_ be integers is only because _θ_ lives on the unit circle. Then the frequencies are constrained such that after rotating by 2 _π_ the function is identical. If you change the radius of the circle to _R_ this constraint becomes _ωd_ = _[n] R[d]_[where] _[ n][d]_[is any integer.][As you take the circle’s] radius to infinity, in the process making finite sections of the circle a better and better approximation of finite patches of flat 1D space, the lattice of permitted frequencies _ωd_ becomes arbitrarily close together. Eventually they are separated by machine precision, and so we can simply implement the code as if they were continuous, hence _ωd ∈_ R. The same argument applies analogously for 2D frequencies on a very very large torus. 

## A.3 REPRESENTATIONAL CONSTRAINTS 

Finally, we will translate these constraints on transformation matrices into constraints on the neural code. This is, thankfully, not too difficult. Consider the representation of an angle for simplicity, and take some arbitrary origin in the input space, _θ_ 0 = 0. The representation of all other angles can be derived via: 

**==> picture [342 x 63] intentionally omitted <==**

15 

Published as a conference paper at ICLR 2023 

In the case of an angle, each _irrep_ , _Id_ ( _θ_ ), is just a 2-by-2 rotation matrix at frequency _d_ , table A.2, and for an _N_ -dimensional _**T**_ we can fit maximally _[N]_ 2[(for] _[ N]_[even) different frequencies, where] _[ N]_ is the number of neurons. Hence the representation, _**g**_ ( _θ_ ), is just a linear combination of the sine and cosine of these different frequencies, exactly as quoted previously: 

**==> picture [328 x 31] intentionally omitted <==**

_**a**_ 0 corresponds to the trivial _irrep_ , and we include it since we know it must be in the code to make the firing rates non-negative for all _θ_ . It also cleans up the constraint on the number of allowable frequencies, for even or odd _N_ we require _D < N_ 2[.][This][is][because][if] _[N]_[is][odd][one][dimension] is used for the trivial _irrep_ , the rest can be shared up amongst _[N]_ 2 _[−]_[1] frequencies, so _D_ must be an integer smaller than _[N]_ 2[.][If] _[ N]_[is even, one dimension must still be used by the trivial] _[ irrep]_[, so] _[ D]_[ can] still maximally be only the largest integer smaller than _[N]_ 2[.] 

Extending this to other groups is relatively simple, the representation is just a linear combination of the functions that appear in the _irrep_ of the group in question, see table A.2. For position on a circle, line (very large circle), torus, or plane (very large torus), they all take the relatively simple form as in equation 18, but requiring appropriate changes from 1 to 2 dimensions, or integer to real frequencies. Representations of position on a sphere are slightly more complex, instead being constructed from linear combinations of sets of spherical harmonics. 

## A.4 PERIODIC VS INFINITE SPACES 

We finally give further details about a key step in our argument for representations of flat 2D space. We approximate a finite region of the infinite 2D plane by a finite region of a very large periodic 2D space, the torus. We do this because the _representation_ theory of the group of 2D translations is not as well characterised (to the best our knowledge there is no equivalent of the Peter-Weyl theorem that could be used to provide a target for optimisation). Fortunately, any animal only cares about a finite region of 2D space (encoded in equation 2 via the lengthscale _L_ ). We therefore approximate this finite region of flat 2D space with an equivalently sized region of a torus. This enables us to use the fully characterised _representation_ theory of the set of translations of periodic space. 

Now, there are legitimate concerns over whether this is a reasonable approximation. Fortunately, we are free to choose the radii of the torus as we wish, and we make use of this freedom to make the approximation of the finite flat 2D space arbitrarily good. As the radii increase to infinity the small region of torus approximates the flat 2D space arbitrarily well. 

This use of periodic space does exclude some representations of the full set of 2D translations, for example: 

**==> picture [265 x 32] intentionally omitted <==**

There are two reasons not to be concerned by this. First, this solution would never have been allowed, as including it ensures that your representation, _**g**_ ( _**x**_ ), cannot have non-negative or bounded firing rates (we suspect this would be the case for all such additional representations of flat 2D translations). Second, any result which was dependent on these kind of boundary effects at _∞_ would be highly suspect. After all, animals are not truly representing flat 2D space, rather they are representing an approximately flat section of the surface of a sphere (the Earth). 

16 

Published as a conference paper at ICLR 2023 

## B NUMERICAL OPTIMISATION DETAILS 

In order to test our claims, we numerically optimise the parameters that define the representation to minimise the loss, subject to constraints. Despite sharing many commonalities, our optimisation procedures are different depending on whether the variable being represented lives in a very large periodic space (approximations to the line, plane, or volume) or finite (circle, torus, sphere). We describe each of these schemes in turn, beginning with the very large spaces. All code is available on github: https://github.com/WilburDoz/ICLR_Actionable_Reps. 

## B.1 NUMERICAL OPTIMISATION FOR VERY LARGE SPACES 

We will use the representation of a point on a line for explanation, planes or volumes are a simple extension. _**g**_ ( _x_ ) is parameterised as follows: 

**==> picture [363 x 30] intentionally omitted <==**

Our loss is made from three terms: the first is the functional objective, the last two enforce the non-negativity and boundedness constraint respectively: 

**==> picture [288 x 11] intentionally omitted <==**

To evaluate the functional component of our loss we sample a set of points _{xi}[M] i_ =1[from] _[ p]_[(] _[x]_[)][ and] calculate their representations _{_ _**g**_ ( _xi_ ) _}[M] i_ =1[.][To make the bounded constraint approximately satisfied] (there’s still some work to be done, taken care of by _L_ bounded) we calculate the following neuron-wise norm and use it to normalise each neuron’s firing: 

**==> picture [285 x 30] intentionally omitted <==**

The functional form of _L_ functional varies, as discussed in the main paper. For example, for the full loss we compute the following using the normalised firing, a discrete approximation to equation 1: 

**==> picture [313 x 30] intentionally omitted <==**

Now we come to our two constraints, which enforce that the representation is non-negative and bounded. We would like our representation to be reasonable (i.e. non-negative and bounded) for all values of _x_ . If we do not enforce this then the optimiser finds various trick solutions in which the representation is non-negative and bounded only in small region, but negative and growing explosively outside of this, which is completely unbiological, and uninteresting. Of course, _x_ is infinite, so we cannot numerically ensure these constraints are satisfied for all _x_ . However, ensuring they are true in a region local to the animal’s explorations (which are represented by _p_ ( _x_ )) suffices to remove most of these trick solutions. As such, we sample a second set of _MS_ ‘shift positions’, _{xm}[M] m_ =1 _[S]_[,] from a scaled up version of _p_ ( _x_ ), using a scale factor _S_ . We then create a much larger set of positions, by shifting the original set by each of the ‘shift positions’, creating a dataset of size _M ∗ MS_ , and use these to calculate our two constraint losses. 

Our non-negativity loss penalises negative firing rates: 

**==> picture [356 x 31] intentionally omitted <==**

Where I is the indicator function, 1 if the firing rate is negative, 0 else, i.e. we just average the magnitude of the negative portion of the firing rates. 

17 

Published as a conference paper at ICLR 2023 

The bounded loss penalises the deviation of each neuron’s norm from 1, in each of the shifted rooms: 

**==> picture [308 x 31] intentionally omitted <==**

That completes our specification of the losses. We minimise the full loss over the parameters ( _**a**_ 0 _, {_ _**a** d,_ _**b** d, ωd}[D] d_ =1[)][using][a][gradient-based][algorithm,][ADAM][(Kingma][&][Ba,][2014).][We][ini-] tialise these parameters by sampling from independent zero-mean gaussians, with variances as in table B.3. 

The final detail of our approach is the setting of _λp_ and _λb_ , which control the relative weight of the constraints vs. the functional objective. We don’t want the optimiser to strike a tradeoff between the objective and constraints, since the constraints must actually be satisfied. But we also don’t want to make _λp_ so large that the objective is badly minimised in the pursuit of only constraint satisfaction. To balance these demands we use GECO (Rezende & Viola, 2018), which specifies a set of stepwise updates for _λp_ and _λb_ . These ensure that if the constraint is not satisfied their coefficients increase, else they decrease allowing the optimiser to focus on the loss. The dynamics that implement this are as follows, for a timestep, _t_ . 

GECO defines a log-space measure of how well the constraint is being satisfied: 

**==> picture [235 x 11] intentionally omitted <==**

(or small variations on this), where _k_ is a log-threshold that sets the target log-size of the constraint loss in question, and _Lt_ is the value of the loss at timestep _t_ . _Lt_ is then smoothed: 

**==> picture [246 x 13] intentionally omitted <==**

And this smoothed measure of how well the constraint is being satisfied controls the behaviour of 

**==> picture [229 x 14] intentionally omitted <==**

This specifies the full optimisation, parameters are listed in table B.3. 

## B.2 NUMERICAL OPTIMISATION FOR FINITE SPACES 

Optimising the representation of finite variables has one added difficulty, and one simplification. Again, we have a parameterised form, e.g. for an angle _θ_ : 

**==> picture [361 x 31] intentionally omitted <==**

The key difficulty is that each frequency, _nd_ , has to be an integer, so we cannot optimise it by gradient descent. Similar problems arise for positions on a torus, or sphere. We shall spend the rest of this section outlining how we circumvent this problem. However, we do also have one major simplification. Because the variable is finite, we can easily ensure the representation is non-negative and bounded across the whole space, avoiding the need for an additional normalisation constraint. Further, for the uniform occupancy distributions we consider in finite spaces, we can analytically calculate the neuron norm, and scale the parameters appropriately to ensure it is always 1: 

**==> picture [326 x 31] intentionally omitted <==**

**==> picture [234 x 24] intentionally omitted <==**

18 

Published as a conference paper at ICLR 2023 

_{_ As _**g**_ ˜( _θ_ such, _m_ ) _}[M] m_ we=1[,][and] simply[compute] sample[the] a[appropriate] set of angles[functional] _{θm}[M] m_[and] =1[,][non-negativity][and][their][normalised][loss,][as][in][representations][equations][23] & 24. 

The final thing we must clear up is how to learn which frequencies, _nd_ , to include in the code. To do this, we make a code that contains many many frequencies, up to some cutoff _D_ max, where _D_ max is bigger than _N_ : 

**==> picture [340 x 30] intentionally omitted <==**

We then add a term to the loss that forces the code to choose only _D_ of these _D_ max frequencies, setting all other coefficient vectors to zero, and hence making the code actionable again but allowing the optimiser to do so in a way that minimises the functional loss. 

The term that we add to achieve this is inspired by the _representation_ theory we used to write these constraints, Section A.2. We create first a 2 _D_ max + 1-dimesional vector, **I** ( _θ_ ), that contains all the _irreps_ i.e. each of the _D_ max sines and cosines and a constant. We then create a (2 _D_ max + 1) _×_ (2 _D_ max + 1)-dimensional transition matrix, _**G** I_ (∆ _θ_ ) that is a _representation_ of the rotation group in this space: _**G** I_ (∆ _θ_ ) **I** ( _θ_ ) = **I** ( _θ_ + ∆ _θ_ ). _**G** I_ can be simply made by stacking 2-by-2 rotation matrices. Then we create the neural code by projecting the frequency basis through a rectangular weight matrix, _**W**_ : _**g**_ ( _θ_ ) = _**W**_ **I** ( _θ_ ). Finally, we create the best possible _representation_ of the group in the neural space: 

**==> picture [252 x 11] intentionally omitted <==**

Where _**W** ∗_ denotes the Moore-Penrose pseudoinverse. We then learn _**W**_ , which is equivalent to learning _**a**_ 0 and _{_ _**a** d,_ _**b** d}[D] d_ =1[max][.] 

_Representation_ theory tells us this will not do a perfect job at rotating the neural representation, unless the optimiser chooses _**W**_ to cut out all but _D_ of the frequencies. As such, we sample a set of shifts _{θms }[M] ms_ =1[, and measure the following discrepancy:] 

**==> picture [336 x 31] intentionally omitted <==**

Minimising it as we minimised the other constraint terms will force the code to choose _D_ frequencies and hence make the code actionable. 

Since calculating the pseudoinverse is expensive, we replace _**W**[∗]_ with a matrix _**B**_ that we also learn by gradient descent. _**B**_ quickly learns to approximate the pseudoinverse, speeding our computations. 

That wraps up our numerical description. We are again left with three loss terms, two of which enforce constraints. This can be applied to any group, even if you can’t do gradient descent through their _irreps_ , at the cost of limiting the optimisation to a subset of _irreps_ below a certain frequency, _D_ max. 

**==> picture [298 x 11] intentionally omitted <==**

B.3 PARAMETERS VALUES 

We list the parameter values used to generate the grid cells in Figure 2B, and show the full population of neurons in figure 6. 

19 

Published as a conference paper at ICLR 2023 

|Parameter|Meaning|Value|
|---|---|---|
|_σ_<br>_l_<br>_T_<br>_N_<br>_M_<br>_MS_<br>_S_<br>_n_resample<br>_λp_0<br>_kp_<br>_αp_<br>_γp_<br>_λn_0<br>_kn_<br>_αn_<br>_γn_<br>_ϵw_,<br>_ϵ_om<br>_β_1<br>_β_2<br>_η_|neural lengthscale<br>_χ_lengthscale<br>number of gradient steps<br>number of neurons<br>number of sampled points every_n_resamplesteps<br>number of room shifts sampled every_n_resamplesteps<br>standard deviation of normal for shift sampling<br>number of steps per resample of points<br>initial positivity weighting coeffcient<br>log positivity target<br>positivity target smoothing<br>positivity coeffcient dynamics coeffcient<br>same set of GECO parameters for norm constraint<br>ditto<br>ditto<br>ditto<br>coeffcient gradient step size<br>frequency gradient step size<br>exponential moving average of frst gradient moment<br>exponential moving average of second moment<br>ADAM non-explodingterm|0.2<br>0.5<br>150000<br>64<br>150<br>15<br>3<br>5<br>0.1<br>-9<br>0.9<br>0.0001<br>0.005<br>4<br>0.9<br>0.0001<br>0.1<br>0.1<br>0.9<br>0.9<br>1_×_10_−_8|



**==> picture [397 x 349] intentionally omitted <==**

Figure 6: All the neurons for the population in figure 2: all neurons fall into one of three modules. 

20 

Published as a conference paper at ICLR 2023 

## B.4 ROBUSTNESS TO PARAMETER VALUES 

In this section we explore the parameter-dependence of our numerical solutions. Most of the parameters in table B.3 control the behaviour of the optimisation scheme (for example controlling the behaviour of ADAM (Kingma & Ba, 2014) or GECO (Rezende & Viola, 2018)). These were tuned so that the optimiser found the best solutions possible; any parameter dependence in these does not seem deeply worrying, reflecting the optimisers used rather than the core problem we’re solving. 

We therefore focus our explorations on the parameters that define key parts of the loss function: the neural lengthscale, _σ_ , the two spatial lengthscales, _L_ and _l_ , and the number of neurons, _N_ . We choose the units of the input space such that _L_ = 1, leaving us with three parameters to explore. (The neural space units are not so arbitrary, due to the firing rate constraint) 

Our theory actually makes predictions for how these parameters should change the representation. As discussed in appendix E.3, if the ratio of _N_ and _σ_ is small there should be one module of neurons, and increasing it should increase the number of modules in the optimal solutions. _l_ enforces the push to hexagons, so, assuming there’s only one module for simplicity, if _l_ is sufficiently large the optimal solution should be hexagonal grid cells. If _l_ is very small then it will have no effect, so all sufficiently high frequency grids should be equal and their shape should matter less. 

We verify these claims in a series of numerical experiments, and we show that there are reasonably large parameter regimes in which our suggested qualitative solutions emerge (one module for high _σ_ , as in figure 4, multiple modules for low _σ_ , as in figure 2). In these experiments most other parameters are kept at the values in table B.3, barring the number of steps which was varied with the number of neurons, and _λp_ 0 and _λn_ 0 which should be scaled with the approximate size of the loss, that varies as _σ_ and _l_ vary. 

## B.4.1 EFFECT OF VARYING _l_ 

The top 6 panels of figure 8 show that for a fixed number of neurons one module of hexagonal grids is optimal for a range of _l_ . We start at _l_ = 1, as that corresponds to the rough lengthscale of the environment. Eventually for small _l_ the optimiser chooses other, non-hexagonal grids. While hexagons are optimal for a reasonable range of _l_ , we might wonder why our arguments do not hold for even smaller _l_ ? 

We believe this is due to the small number of neurons we are using. We argued hexagons were optimal because they packed the most frequencies into a Goldilocks annulus in frequency space, figure 4. As _l_ decreases the outer ring of this annulus moves further away, providing a larger Goldilocks region. When the number of neurons in a module, i.e. the number of frequencies, is small this permits many different lattices to pack frequencies within the Goldilocks annulus equally well, figure 7. So, for a given number of neurons, there is a _l_ -threshold, beyond which there is no longer a push towards hexagons, and this threshold can be decreased by increasing the number of neurons. 

We verify this in the last panel of figure 8, where we show that at _l_ = 0 _._ 1, where 64 neuron modules were not hexagonal, 100 neuron modules were. Therefore, we expect for modules containing many neurons (like those in the brain) hexagons are optimal for a much larger range of _l_ . 

**==> picture [238 x 124] intentionally omitted <==**

Figure 7: For small _l_ , relative to the number of frequencies, many different lattices pack frequencies into the Goldilocks annulus equally well, e.g. these square and hexagonal lattice. 

21 

Published as a conference paper at ICLR 2023 

**==> picture [397 x 559] intentionally omitted <==**

Figure 8: For 64 neurons with _σ_ = 0 _._ 4 one module of grids is consistently optimal, all representations contained one module with occasionally one stray neuron with a garbled response. At high _l_ the modules are all hexagonal, for low _l_ other grids start appearing, like band cells or square grids. This is likely due to the small number of neurons used, because when we increase the number of neurons to 100 as in the bottom plot the module remains hexagonal at lower values of _l_ . 

22 

Published as a conference paper at ICLR 2023 

## B.4.2 EFFECT OF VARYING _σ_ 

As discussed in Appendix E.3, varying _σ_ varies the push towards non-harmonicity, and hence how many modules we would expect in the optimal solution. We confirm this in Figure 9. For large _σ_ (up to _σ_ = 1) we get one hexagonal module, decreasing it leads to solutions with more modules. 

The more modules the less hexagonal they are. We suspect this is again partly a finite neuron effect, as in Appendix B.4.1. Future work could usefully explore whether more constraints are needed to robustly generate many hexagonal modules, or whether more neurons is enough as it was in figure 8. 

**==> picture [318 x 292] intentionally omitted <==**

Figure 9: For fixed _l_ = 0 _._ 2 and _N_ = 64 we vary _σ_ and count the number of modules. For large _σ_ (including up to _σ_ = 1) there is consistently one hexagonal module. As _σ_ decreases you get more modules. Error bars are standard deviation over multiple simulations. Inset are the module shapes in one simulation for each of three _σ_ values. 

## B.4.3 VARYING NUMBER OF NEURONS 

Figures 10 and 11 show that as we vary the number of neurons (with fixed _l_ ), we can find values of _σ_ for which the population produces either one module of hexagonal grids (Figure 10) or multiple modules (Figure 11). Hence, our qualitative solution types are found across a range of population sizes. 

23 

Published as a conference paper at ICLR 2023 

**==> picture [397 x 575] intentionally omitted <==**

Figure 10: Each row of this figure summarises one simulation, and each simulation has a different population size, _N_ . We fix _l_ = 0 _._ 5 and show a _σ_ value at which almost all neurons form one hexagonal module. 

24 

Published as a conference paper at ICLR 2023 

**==> picture [396 x 463] intentionally omitted <==**

Figure 11: Each row of this figure summarises one simulation, and each simulation has a different population size, _N_ . We fix _l_ = 0 _._ 5 and show a _σ_ value at which the population falls into multiple modules. 

25 

Published as a conference paper at ICLR 2023 

## C ANALYSIS OF SIMPLEST LOSS THAT LEADS TO ONE LATTICE MODULE 

In this section we analytically study the simplified loss suggested in section 3.1 and derive equation 8. The actionability constraint tells us that: 

**==> picture [313 x 30] intentionally omitted <==**

Where D is smaller than half the number of neurons (Appendix A). We ensure _nd_ = _nd′_ if _d_ = _d[′]_ by combining like terms. Our loss is: 

**==> picture [282 x 24] intentionally omitted <==**

Developing this and using trig identities for the sum of sines and cosines: 

**==> picture [378 x 26] intentionally omitted <==**

**==> picture [433 x 38] intentionally omitted <==**

We now change variables to _α_ = _[θ][−]_ 2 _[θ][′]_ and _β_ = _[θ]_[+] 2 _[θ][′]_[.][This][introduces][a][factor][of][two][from][the] Jacobian ( 2[1][), which we cancel by doubling the range of the integral while keeping the same limits,] despite the change of variable, Figure 12. This gives us: 

**==> picture [349 x 28] intentionally omitted <==**

**==> picture [359 x 87] intentionally omitted <==**

**==> picture [396 x 128] intentionally omitted <==**

Figure 12: The original integral is shown in orange. We rotate to the purple axes and, for convenience, use the same limits (i.e. _−π_ to _π_ ). This corresponds to adding the green area to the integral but, using the fact that these functions are unchanged by shifts of 2 _π_ in either _θ_ or _θ[′]_ we can see that the green region is equal to the original orange region. Therefore, performing the full purple integral just gets us twice our desired integral. 

26 

Published as a conference paper at ICLR 2023 

Performing these integrals is easy using the fourier orthogonality relations; the two cross terms with mixed sin and cos of _β_ are instantly zero, the other two terms are non-zero only if _nd_ = _nd′_ , i.e. _d_ = _d[′]_ . When _d_ = _d[′]_ these integrals evaluate to _π_[2] , giving: 

**==> picture [251 x 24] intentionally omitted <==**

Exactly as quoted in equation 7. We can do the same development for the firing rate constraint: 

**==> picture [332 x 30] intentionally omitted <==**

Again using the orthogonality relation. These are the constraints that must be enforced. For illustration it is useful to see one slice of the constraints made by summing over the neuron index: 

**==> picture [272 x 30] intentionally omitted <==**

This is the constraint shown in equation 8, and is strongly intuition guiding. But remember it is really a stand-in for the _N_ constraints, one per neuron, that must each be satisfied! 

This analysis can be generalised to derive exactly the same result in 2D by integrating over pairs of points on the torus. It yields no extra insight, and is no different, so we just quote the result: 

**==> picture [350 x 27] intentionally omitted <==**

## D ANALYSIS OF PARTIALLY SIMPLIFIED LOSS THAT LEADS TO A MODULE OF HEXAGONAL GRIDS 

In this section we will study an intermediate loss: it will compute the euclidean distance, like in Appendix C, but we’ll include _χ_ and _p_ . We’ll show that they induce a frequency bias, _χ_ for low frequencies, and _p_ for high, which together lead to hexagonal lattices. We’ll study _χ_ first for representations of a circular variable, then we’ll study _p_ for representations of a line, then we’ll combine them. At each stage generalising to 2-dimensions is a conceptually trivial but algebraically nasty operation with no utility, so we do not detail here. In Appendix L we will return to the differences between 1D and 2D, and show instances where they become important. 

## D.1 LOW FREQUENCY BIAS: PLACE CELLS ON THE CIRCLE 

We begin with the representation of an angle on a circle, introduce _χ_ , and show the analytic form of the low frequency bias it produces. Since we’re on a circle _χ_ must depend on distance on the circle, rather than on a line (i.e. not _χ_ = 1 _− e[−][∥][x][−]_ 2 _l[x]_[2] _[′][∥]_[2] ). We define the obvious generalisation of this to periodic spaces, Figure 13A, which is normalised to integrate to one under a uniform _p_ ( _θ_ ): 

**==> picture [255 x 27] intentionally omitted <==**

Where _I_ 0 is the zeroth-order modified Bessel function. Hence the loss is: 

**==> picture [316 x 26] intentionally omitted <==**

In this expression _k_ is a parameter that controls the generalisation width, playing the inverse role of _l_ in the main paper. Taking the same steps as in Appendix C we arrive at: 

**==> picture [388 x 28] intentionally omitted <==**

27 

Published as a conference paper at ICLR 2023 

The _β_ integral again kills the cross terms: 

**==> picture [314 x 29] intentionally omitted <==**

These integrals can be computed by relating them to modified Bessel functions of the first kind, which can be defined for integer _n_ as: 

**==> picture [271 x 24] intentionally omitted <==**

Hence the loss is: 

**==> picture [275 x 29] intentionally omitted <==**

This is basically the same result as before, equation 42, all the frequencies decouple and decrease the loss in proportion to their magnitude. However, we have added a weighting factor, that decreases with frequency, Figure 13B, i.e. a simple low frequency bias! 

This analysis agrees with that of Sengupta et al. (2018), who argued that the best representation of angles on a ring for a loss related to the one studied here should be place cells. We disentangle the relationship between our two works in Appendix F. Regardless, our optimisation problem now asks us to build a module of lattice neurons with as many low frequencies as possible. The optimal solution to this is the lowest frequency lattice, i.e. place cells! (we validate this numerically in Appendix M). Therefore, it is only additional developments of the loss, namely the introduction of an infinite space for which you prioritise the coding of visited regions, and the introduction of the neural lengthscale, _σ_ , that lead us to conclude that modules of grid cells are better than place cells. 

## D.2 HIGH FREQUENCY BIAS: OCCUPANCY DISTRIBUTION 

Now we’ll examine how a Gaussian _p_ ( _x_ ) affects the result, using a representation of _x_ , a 1- dimensional position: 

**==> picture [396 x 34] intentionally omitted <==**

Developing the argument as before: 

**==> picture [380 x 27] intentionally omitted <==**

The cross terms again are zero, due to the symmetry of the _β_ integral around 0. 

**==> picture [357 x 28] intentionally omitted <==**

Where we’ve wrapped up the details into the following integrals of trigonometric functions over a gaussian measure: 

**==> picture [443 x 164] intentionally omitted <==**

28 

Published as a conference paper at ICLR 2023 

**==> picture [358 x 498] intentionally omitted <==**

Figure 13: **A** The circular version of _χ_ (∆ _θ_ ), equation 46, weights the importance of separating different pairs on the circle. downweighting nearby points, closer than _k_[1][.] **[B]**[The][Low][Frequency] Bias of equation 51 **C** High Frequency Bias of equation 57 and 59. Left: bias for isolated frequency (e.g. all frequencies when space is encoded uniformly). Right: cosine and sine bias for a pair of frequencies _ω_ and _ω[′]_ . Diagonals of right = left. Right plots show both a high frequency bias and a smoothing over similar frequencies, where similar means within _L_[1][.][(Here] _[L]_[=][1][)] **[D]**[High] and Low Frequency Biases. Same as **C** for equation. 61. Notice peak around the inverse room size, _L_[1][=][1][.] **[E]**[ Optimising a neural code on equation 60 with constraints produces one module of] hexagons, as predicted. But, as shown in **F** , each neuron activates in the same way, hence this is a bad representation. 

29 

Published as a conference paper at ICLR 2023 

The downstream consequence of this loss is simple if a module encodes all areas of space evenly. Encoding evenly implies the phases of the neurons in the module are evenly distributed. The phase of a particular neuron is encoded in the coefficients of the sine and cosine of the base frequency, _an_ 1 and _bn_ 1. Even distribution implies that _an_ 1 oscillates from _Ad_ , where _Ad_ = max _n an_ 1, to _−Ad_ and back again as you sweep the neuron index. As you perform this sweep the subsidiary coefficients, such as _an_ 2, perform the same oscillation, but multiple times. _an_ 2 does it twice, since, by the arguments that led us to grids, the peaks of the two waves must align (Figure 3B), and that implies the peak of the wave at twice the frequency moves at the same speed as you sweep the neuron number. This implies its phase oscillates twice as fast, and hence that[�] _n[a][n]_[1] _[a][n]_[2][=][0][.][Arguments] like this imply the frequencies actually decouple for a uniform encoding of space, making the loss, 

**==> picture [311 x 32] intentionally omitted <==**

This is exactly a high frequency bias! (Fig 13C Left) 

However, uniform encoding of the space is actually not optimal for this loss, as can be seen either from the form of equation 57, and verified numerically using the loss in the next section, Figure 13EF. The weighting of the sine factor and the cosine factor differ, and in fact push toward sine, since it plateaus at lower frequencies. Combine that with a low frequency push, and you get an incentive to use only sines, which is allowed if you can encode only some areas of space, as the euclidean loss permits. 

A final interesting feature of this loss is the way the coupling between frequencies gracefully extends the decoupling between frequencies to the space of continuous (rather than integer) frequencies. In our most simplified loss, equation 42, each frequency contributed according to the square of its amplitude, _∥_ _**a** d∥_[2] + _∥_ _**b** d∥_[2] . How should this be extended to continuous frequencies? Certainly, if two frequencies were very far from one another we should retrieve the previous result, and their contributions would be expected to decouple, _∥_ _**a**_ 1 _∥_[2] + _∥_ _**b**_ 1 _∥_[2] + _∥_ _**a**_ 2 _∥_[2] + _∥_ _**b**_ 2 _∥_[2] . But if _**k**_ 2 = _**k**_ 1 + _δ_ _**k**_ , for a small _δ_ _**k**_ then the two frequencies are, for all intents and purposes, the same, so they should contribute an amplitude _∥_ _**a**_ 1 + _**a**_ 2 _∥_[2] + _∥_ _**b**_ 1 + _**b**_ 2 _∥_[2] = _∥_ _**a**_ 1 _∥_[2] + _∥_ _**b**_ 1 _∥_[2] + _∥_ _**a**_ 2 _∥_[2] + _∥_ _**b**_ 2 _∥_[2] . Equation 57, Figure 13C right, performs exactly this bit of intuition. It tells us that the key lengthscale in frequency space is _L_[1][. Two frequencies separated by more than this distance contribute] in a decoupled way, as in equation 37. Conversely, at very small distances, much smaller than _L_[1][the] contribution is exactly _∥_ _**a**_ 1 + _**a**_ 2 _∥_[2] + _∥_ _**b**_ 1 + _**b**_ 2 _∥_[2] , as it should be. But additionally, it tells us the functional form of the behaviour between these two limits: a Gaussian decay. 

## D.3 THE COMBINED EFFECT = HIGH AND LOW FREQUENCY BIAS 

In this section we show that the simple euclidean loss with both _χ_ and _p_ can be analysed, and it contains both the high and low frequency biases discussed previously in isolation. This is not very surprising, but we include it for completeness. 

**==> picture [341 x 47] intentionally omitted <==**

Following a very similar path to before we reach: 

**==> picture [397 x 28] intentionally omitted <==**

**==> picture [17 x 9] intentionally omitted <==**

**==> picture [304 x 11] intentionally omitted <==**

**==> picture [283 x 24] intentionally omitted <==**

This contains the low and high frequency penalisation, at lengthscales _L_[1][and][1] _l_[, respectively.][There] are 4 terms, 2 are identical to equation 57, and hence perform the same role. The additional two 

30 

Published as a conference paper at ICLR 2023 

terms are positive, so should be minimised, and they can be minimised by making the frequencies smaller than _∼_[1] _l_[, Figure 13D.] 

We verify this claim numerically by optimising a neural representation of 2D position, _**g**_ ( _**x**_ ), to minimise _L_ 1 subject to actionable and biological constraints. It forms a module of hexagonal cells, Figure 13E, but the representation is shoddy, because the cells only encode a small area of space well, as can be seen by zooming on the response, Figure 13. 

## E ANALYSIS OF FULL LOSS: MULTIPLE MODULES OF GRIDS 

In this Section we will perturbatively analyse the full loss function, which includes the neural lengthscale, _σ_ . The consequences of including this lengthscale will become most obvious for the simplest example, the representation of an angle on a ring, _**g**_ ( _θ_ ), with a uniform weighting of the importance of separating different points. We’ll use it to derive the push towards non-harmonically related modules. 

Hence, we study the following loss: 

**==> picture [272 x 24] intentionally omitted <==**

And examine how the effects of this loss differ from the euclidean verison studied in Appendix C. 

This loss is difficult to analyse, but insight can be gained by making an approximation. We assume that the distance in neural space between the representations of two inputs depends only on the difference between those two inputs, i.e.: 

**==> picture [257 x 12] intentionally omitted <==**

Looking at the constrained form of the representation, we can see this is satisfied if frequencies are orthogonal: 

**==> picture [361 x 30] intentionally omitted <==**

**==> picture [236 x 41] intentionally omitted <==**

Then: 

**==> picture [293 x 30] intentionally omitted <==**

Now we will combine this convenient form with the following expansion: 

**==> picture [291 x 28] intentionally omitted <==**

Developing equation 64 using eqns. 69 and 68: 

**==> picture [354 x 136] intentionally omitted <==**

31 

Published as a conference paper at ICLR 2023 

We will now look at each of these two terms separately and derive from each an intuitive conclusion. Term A will tell us that frequency amplitudes will tend to be capped at around the legnthscale _σ_ . Term B will tell us how well different frequencies combine, and as such, will exert the push towards non-harmonically related frequency combinations. 

## E.1 TERM A ENCOURAGES A DIVERSITY OF HIGH AMPLITUDE FREQUENCIES IN THE CODE 

Fig 14A shows a plot of _I_ 0( 4 _[A] σd_[2][2][)][.][As can be seen there are a couple of regimes, if] _[ A][d]_[, the amplitude] of frequency _nd_ , is smaller than _σ_ then _I_ 0( 4 _[A] σd_[2][2][)] _[ ≈]_[1][.][On the other hand, as] _[ A][d]_[ grows,] _[ I]_[0][ also grows.] Asymptotically: 

**==> picture [236 x 39] intentionally omitted <==**

Correspondingly Term A also behaves differently in the two regimes, when _Ad_ is smaller than _σ_ the loss decreases exponentially with the amplitude of frequency _d_ : 

**==> picture [295 x 23] intentionally omitted <==**

Alternatively: 

**==> picture [290 x 25] intentionally omitted <==**

So, up to a threshold region defined by the lengthscale _σ_ , there is an exponential improvement in the loss as you increase the amplitude. Beyond that the improvements drop to being polynomial. This makes a lot of sense, once you have used a frequency to separate a subset of points sufficiently well from one another you only get minimal gains for more increase in that frequency’s amplitude, Figure 14B. Since there are many frequencies, and the norm constraint ensures that few can have an amplitude of order _σ_ , it encourages the optimiser to put more power into the other frequencies. In other words, amplitudes are only usefully increased to a lengthscale _σ_ , encouraging a diversity in high amplitude frequencies. This is moderately interesting, but will be a useful piece of information for the next derivation. 

## E.2 TERM B ENCOURAGES THE CODE’S FREQUENCIES TO BE NON-HARMONICALLY RELATED 

Term B is an integral of the product of _D_ infinite sums, which seems very counter-productive to examine. We are fortunate, however. First, the coefficients in the infinite sum decay very rapidly with _m_ when the ratio of _[A] σ[d]_[is] _[ O]_[(1)][,][Figure 14C. The previous section’s arguments make it clear] that, in any optimal code, _Ad_ will be smaller or of the same order as _σ._ As such, the inifite sum is 

rapidly truncated. Additionally, all of the coefficient ratios, � _IIm_ 0((4 _A_ 4 _Aσσ_[2] _d_[2] _d_[2][2][)][)] �, are smaller than 1, as such we can understand the role of Term B by analysing just the first few terms in the following series expansion, 

**==> picture [417 x 97] intentionally omitted <==**

**==> picture [374 x 29] intentionally omitted <==**

32 

Published as a conference paper at ICLR 2023 

**==> picture [396 x 228] intentionally omitted <==**

Figure 14: **A** Modified Bessel Function. **B** Amplitude Usefully Increases to a limit _**σ**_ . When _Ad < σ_ then growing the amplitude pushes many points very usefully apart, hence the loss decreases quickly. However, once _Ad ∼ σ_ many points are already sufficiently separated. The only gains from growing the amplitude more are in the small region that remain neighbouring, hence the loss starts decreasing much more slowly, and precious amplitude is much better invested in other smaller amplitude frequencies. **C** Ratios of Modified Bessel Functions. The terms appearing in the series expansion are, first, smaller than 1, so each additional term is the series, which is multiplied by an additional ratio smaller than 1, decays rapidly. And, second, these ratios decay rapidly with _m_ , so the infinite sums within each term in the series expansion decay rapidly, containing roughly 3 or 4 nonzero terms for the largest amplitude frequencies in the code. **D** Pairwise Continuous Interactions. _p_ ( _x_ ) causes frequencies to be penalised for both being smaller than _∼ L_[1][, and, to a lesser extent, for] being harmonically related, up to a lengthscale _∼ L_[1][, equation 85.][This same interaction applies for] all pairs of frequencies, and all pairs of harmonics of frequencies, though the contribution is more downweighted the higher the harmonics in the pair. 

The 0[th] order term is a constant, and the 1[st] order term is zero when you integrate over _α_ . As such, the leading order effect of this loss on the optimal choice of frequencies arrives via the 2[nd] order term. The integral is easy, 

**==> picture [312 x 24] intentionally omitted <==**

We want to minimise the loss, and this contribution is positive, so any time the 2[nd] order term is non-zero it is a penalty. As such, we want as few frequencies to satisfy the condition in the delta function, _mnd_ = _m[′] nd[′]_ . Recall from equation 77 that these terms are weighted by coefficients that decay rapidly as _m_ grows. As such, the condition that the loss is penalising, _mnd_ = _m[′] nd[′]_ , is really saying: penalise all pairs of frequencies in the code, _nd_ , _nd′_ , that can be related by some simple harmonic ratio, _nd_ = _[m] m[′][n][d][′]_[, where] _[ m]_[ and] _[ m][′]_[are small integers, roughly less than 5, Figure 14C.] 

This may seem obtuse, but is very interpretable! Simply harmonically related frequencies are exactly those that encode many inputs with the same response! Hence, they should be penalised, Fig 4C. 

## E.3 A HARMONIC TUSSLE - NON-HARMONICS LEADS TO MULTIPLE MODULES 

As described in Section 3.3, we now arrive at a dilemma. The arguments of Sections 3.1 and C suggest that the optimal representation is comprised of lattice modules, i.e. the neurons must build a code from a lattice of frequencies. A lattice is exactly the arrangement that ensures all the frequencies are related to one another by simple harmonic ratios. Yet, the arguments of the previous section 

33 

Published as a conference paper at ICLR 2023 

suggest that frequencies with simple harmonic relations are a bad choice - i.e. a frequency lattice would be the worst option! How can this be resolved? 

The resolution will depend on the value of two parameters: the first, _σ_ , is the neural lengthscale; the second, _N_ , is the number of neurons, which, through the boundedness constraint, sets the scale of the amplitudes, _Ad_ . We can already see this key ratio, _[A] σ[d]_[,][appearing][in][the][preceding][arguments.] Its role is to choose the compromise point in this harmonic tussle, and in doing so it chooses the number of modules in the code. 

A simple Taylor expansion illustrates that as _σ_ tends towards _∞_ the full loss reverts to the euclidean approximation that was the focus of Sections C and D, in which the effect of the harmonic penalisation drops to zero. 

**==> picture [306 x 21] intentionally omitted <==**

Hence, as _σ →∞_ we recover our original optimal solution: all the neurons belong to one module, whose shape is determined by _χ_ and _p_ . This explains why, with few neurons (equivalent to _σ →∞_ ), the optimal solution is a single module of perfectly hexagonal grids, fig 4B. 

But as _σ_ decreases the effect of the harmonic penalisation becomes larger and larger. Eventually, one module is no longer optimal. Yet, all the previous arguments that modularised codes are easily made non-negative, and hence valuable, still apply. The obvious solution is to have two modules. Within each module all the neurons are easily made non-negative, but between modules you can have very non-harmonic relations, trading off both requirements. 

As such increasing the ratio _[A] σ[d]_[, either by increasing the number of neurons or decreasing] _[ σ]_[, creates] an optimisation problem for which the high quality representations are modules of grids with more modules as the ratio gets bigger. We observed exactly this effect numerically, and it explains the presence of multiple modules of grids in the full version of our problem for a range of values of _σ_ . Finally, we can extract from this analysis a guiding light: that the frequencies in different modules should be maximally non-harmonically related. This additional principle, beyond the simple low and high frequency biases of Section D, frames our normative arguments for the optimal arrangement of modules, that we explore Section 4.2 and Appendix K. 

## E.4 NON-HARMONICALLY RELATED CONTINUOUS FREQUENCIES - A SMOOTHING EFFECT 

We will address one final concern. When representing infinite variables the frequencies in the code become real numbers. For example, when representing a 1-dimensional continuous input, _x_ , the code, _**g**_ ( _x_ ), has the form, 

**==> picture [315 x 30] intentionally omitted <==**

And it seems like the equivalent penalisation as in equation 78, _δ_ ( _mωd − m[′] ωd′_ ), is very easy to avoid. If _mωd_ = _m[′] ωd′_ and the code is being penalised, just increase _ωd_ by an infinitely small amount, _δω_ , such that _mωd_ + _mδω_ = _m[′] ωd′_ , and suddenly this term does not contribute to the loss. 

This, however, is not how the loss manifests. Instead frequencies are penalised for being close to one another, where close is defined by the size of the region the animal encodes, set by lengthscale _L_ . This can be seen by analysing the following loss, 

**==> picture [296 x 53] intentionally omitted <==**

34 

Published as a conference paper at ICLR 2023 

Making the same assumption as in the previous Section, equation 67, and developing the loss identically, 

**==> picture [383 x 47] intentionally omitted <==**

We again analyse this through the series expansion in equation 77. The 0[th] order term is again constant. The 1[st] order term is proporational to, 

**==> picture [297 x 25] intentionally omitted <==**

i.e., as in Section D.2, _p_ ( _x_ ) implements a high frequency bias. In fact, the mathematical form of this penalty, a gaussian, is identical to that in diagonal terms of the previously derived sum, equation 57. The 2[nd] order term is where we find the answer to this Section’s original concern, 

**==> picture [372 x 49] intentionally omitted <==**

Which is similar to the cross terms in equation 57, but with the addition of harmonic interactions. This is the continuous equivalent to the penalty in equation 78. Frequencies and their low order harmonics are penalised for landing closer than _∼ L_[1][from one another, Fig 14D. In conclusion, the] logic gracefully transfers to continuous frequencies. 

## F LINKS TO SENGUPTA ET AL. 2018 

Sengupta et al. (2018) derive an optimal representation of structured variables, where their definition of structured exactly aligns with ours: the variable’s transformations form a group (though the term they use is symmetric manifolds). Further, there are analytic similarities between the loss they study and ours. However, their optimal representations are place cells, and ours are multiple modules of grid cells. In this section we will disentangle these two threads, explaining this difference, which arises from our actionability principle, the neural lengthscale _σ_ , and our use of infinite inputs. 

Sengupta et al. (2018) study the optimisation of a loss derived from a dot product similarity matching objective, an objective that has prompted numerous interesting discoveries (Pehlevan & Chklovskii, 2019). Input vectors, _**x**_ , stacked into the matrix _**X**_ , are represented by vectors of neural activity, _**y**_ , stacked into _**Y**_ , that have to be non-negative and bounded. The loss measures the similarity between pairs of inputs, _**x**[T]_ _**x**[′]_ , and pairs of outputs, _**y**[T]_ _**y**[′]_ , and tries to optimise the neural representation, _**y**_ , such that all input similarities above a threshold, _α_ , are faithfully reproduced in the similarity structure of the neural representation. 

**==> picture [281 x 27] intentionally omitted <==**

where _**E**_ is a matrix of ones, and diag( _**Y**[T]_ _**Y**_ ) _≤ β_ **1** enforces the neural activity’s norm constraint. 

Our loss is strikingly similar. Our inputs are variables, such as the angle, that play the role of _**x**_ . Sengupta et al.’s input dot product similarity, _**x**[T]_ _**x**[′] − α_ , plays the role of _χ_ ( _θ, θ[′]_ ), measuring similarity in input space. The neural activities, _**g**_ , must, like _**y**_ , be non-negative and bounded in L2 norm. And minimising the similarity matching loss is like minimising the simple euclidean form of the loss studied in Appendix D, with the integrals playing the role of the trace, 

**==> picture [299 x 25] intentionally omitted <==**

35 

Published as a conference paper at ICLR 2023 

The analogy then, is that minimising _L_ 1 is asking the most similar elements of the input to be represented most similarly, and dissimilar dissimilarly, as in the non-negative similarity matching objective; an orthogonal motivation for our loss! 

Sengupta et al. (2018) use beautiful convex optimisation techniques (that cannot, unfortunately, be applied directly to our problem, Appendix G) to show that the optimal representation of the finite spaces they consider (circles and spheres) are populations of place cells. What is it about our losses that leads us to different conclusions? 

Our problems differ in a few ways. First, since they use dot-product similarities, their loss is closest to our simplified losses, i.e. those without the presence of the neural lengthscale, _σ_ . So, due to this difference, we would expect them to produce a single module of responses, as observed. 

The second difference is the addition of actionability to our code which produces a harsh frequency content constraint, and is pivotal to our derivation (as can be seen from ablation studies, Appendix I). They, however, assume infinitely many neurons, at which point the frequency constraint becomes, especially when there is only one module, relatively vacuous. So we could still see their analysis as 

Third, we use a different measure of input similarity, though we do not believe this would have particularly strong effects on our conclusions. 

Finally, we consider infinite spaces, like position on a line, by introducing a probability distribution over inputs, _p_ ( _x_ ). 

As such, for representations of finite variables, like angle, the infinite neuron predictions of our simplified loss and Sengupta et al. should align. Thankfully, they do! As shown in Appendix M we predict place-cell like tuning for the representation of circular variables. This follows from our previous discussions, Appendix D.1: for finite spaces including a low frequency bias via the input similarity _χ_ was argued to make the optimal representation a module of the lowest frequency lattices, place cells! 

Hence, relative to Sengupta et al., by extending to the representation of infinite spaces with actionability we reach grids, rather than place cells. And by additionally including _σ_ , the neural lengthscale, we produce multiple modules. 

- G OPTIMAL NON-NEGATIVE ACTIONABLE CODE - A NON-CONVEX PROBLEM 

In this section we highlight that actionability is what makes our problem non-convex. Specifically, choosing the set of frequencies is difficult: for a fixed choice of frequencies the simplified loss (equation 7) and constraints are convex in the neural coefficients. We include it here to point towards tools that may be useful in proving grid’s optimality, rather than heuristically justifying them with numerically support, as we have done. 

Consider a representation _**g**_ ( _θ_ ). For a fixed set of frequencies _{nd}[D] d_ =1[,][we’ll][aim][to][optimise][the] coefficients _**a**_ 0 _, {_ _**a** d,_ _**b** d}[D] d_ =1[. The losses take simple forms, the functional objective to be minimised] is min _−_[�] _d[∥]_ _**[a]**[d][∥]_[2][ +] _[ ∥]_ _**[b]**[d][∥]_[2][.][The boundedness constraint is similarly quadratic in the coefficients,] equation 8. The only potential trouble is the non-negativity constraint. Sengupta et al. (2018) solve this problem by having no actionabtility and infintely many neurons, we can take a different approach. 

Our code is a Positive Trigonometric Polynomial, a function of the following form: 

**==> picture [250 x 32] intentionally omitted <==**

where _D_ max = max _d nd_ , a type of polynomial studied in engineering and optimisation settings Dumitrescu (2007). Due to actionability our code is a sparse positive trigonometric polynomial, only 2 _D_ + 1 of the _**rd**_ are non-zero. 

36 

Published as a conference paper at ICLR 2023 

While positivity is a hard constraint to enforce, Bochner’s theorem gives us hope. It tells us that for _gn_ ( _θ_ ) to be positive for all _θ_ , its fourier transform, _gn_ ( _ω_ ) must be positive-definite. This means that the following matrix, made from the fourier coefficients, must be positive-definite: 

**==> picture [300 x 69] intentionally omitted <==**

The set of positive-definite matrices forms a convex set. Even the set of matrices _**Q** n_ where fixed diagonals are zero is a convex set. Further, this matrix displays all the right tradeoffs for positivity: _rn_ 0 must be non-zero for the matrix to be positive-definite, i.e. there must be a constant offset to achieve non-negativity. Similarly, including harmonics makes achieving non-negativity easier than non-harmonics, just as in Figure 2A. 

But even having made this link we cannot make progress, since we had to choose which frequencies had non-zero amplitude. Hence, the choice of frequency sparsity implied by actionability stops our problem from being convex. A plausible solution might be to solve the convex optimisation problem for a given set of frequencies, then to take gradients through that solution to update the frequencies, but we have not implemented this. 

## H LINKS TO SOME OTHER PATH INTEGRATION MODELS 

Our theory is a theory of path-integrating representations. Actionability means you understand the rules of space (a representation should be unchanged after taking a step north then east then south then west), but it does not mean you understand where you are, or how fine-grained this understanding is (a representation that encodes all positions the same way satisfies the actionable rules for example). Our functional constraint rectifies this, as it requires all relevant locations to be represented differently, up to a certain spatial scale. Understanding rules, and representing locations differently is the same as path-integration - now a representation can be updated according to the rules, and the underlying spatial variables can be decoded. 

## H.1 LINEAR PATH INTEGRATION MODELS 

Linear path integration models of the entorhinal cortex, like ours, have, to the best of our knowledge, been suggested three times before (Issa & Zhang, 2012; Whittington et al., 2020; Gao et al., 2021). Whittington et al. and Gao et al. are both simulation based, optimising losses related to ours, and show the resulting optimisations look like grid cells, though both papers only obtain multiple modules of grids by manually enforcing block diagonal transformation matrices. In this section we will discuss the differences between these two losses and ours, to explain their results in our framework as much as possible. 

**Gao et al.** optimise a representation of position and a set of linear neural transition matrices to minimise a series of losses. One loss enforces path integration, like our actionability constraint. Another bounds the firing rate of vectors, similar to our boundedness constraint. A final similarity is their version of the functional objective, which enforces the ability to linearly readout place-cell-like activity from the grid code. 

However, additionally they enforce an ‘isotropic scaling term’. This term measures how much the neural activity vector moves when you take a small step in direction _ψ_ in the input space, and encourages all the steps to be the same size independent of _ψ_ . This can be understood through the strong force towards hexagonality it produces: if you know your representation is some type of grid then of all the two dimensional grid the one that is most symmetric is hexagons, with it’s _C_ 6 symmetry. Hence it will minimise this isotropic scaling. 

We have shown that it is not necessary to include this term in the loss to produce hexagonal grids. However, there will be differences in behaviour between a code minimising this constraint and a 

37 

Published as a conference paper at ICLR 2023 

code that doesn’t. The stronger push towards hexagonality that isotopy exerts will make deviations from perfect hexagonality, such as shearing Stensola et al. (2015) less optimal. A careful analysis of the behaviour of the two losses, both with functional, actionable, and biological constraints, but adding or removing isotropy, in different rooms could produce different predictions. Further, each module would be more robustly hexagonal with this term added, which might be necessary to make many many modules hexagonal. 

Finally, the relation between our non-negative firing rates, and the concept of non-negativity in Gao et al. is slightly murky. Gao et al. use non-negative grid-to-place-cell weights, but also show this non-negativity is not required to produce grids. How this meshes with our findings that nonnegativity is vital for grid formation remains unclear. This discrepancy could be caused by the isotropy constraint, but we remain unsure. 

Theoretically, Gao et al. develop a rich group theory view for studying grid cells. We add to this work using Representation theory to make clear what constraints linear actionability implies (equation 5). Given this starting point we are able to explain intuitively and with analytic insight why this loss leads to grid cells, extend to multiple modules, and make neural predictions. 

**Whittington et al.** train a recurrent neural network to path integrate, but also to separate the representation of different points in the input space by predicting different observations at different positions. Path integration is linear with action dependent matrices, exactly like our actionability, and the neural activities are bounded. In recent versions of the model, Whittington et al. (2021), nonnegative firing rates are used, which gave hexagonal grid cells. This can be understood as a direct application of our framework, though the pressures on the representation are naturally more blurry since it is optimised with behavioural trajectories using a recurrent neural network. In particular, the goldilocks frequency bounds (section 3.2) can be thought of as coming from the finite map the agent explores (high frequency bias) and the discrete step-size in the environment (low frequency bias). 

## H.2 SORSCHER, MEL, ET AL.’S NON-LINEAR PATH INTEGRATION MODEL 

Sorscher et al. (2019) provide a nice theoretical analysis of how non-negativity and linear reconstruction of place cells can lead to hexagonal grids, providing valuable insight into previous observations in the field such as that of Dordek et al. (2016). 

The key difference between our theoretical analysis and theirs, is that they rely on the covariance structure of place cell input to obtain a representation made from plane waves, whereas we show that actionability (path integration) alone demands a representation built from plane waves. The reliance on a particular place cell covariance structure makes a strict constraint on the form place cells take - whether this is compatible with observed place cells is a topic of much debate (Schaeffer et al., 2022; Sorscher et al., 2022). The subsequent arguments that lead to hexagonal grid cells bear some resemblance, but are different, as we outline here: 

Sorscher et al. (2019) discuss how finite room effects (i.e. the animal only exploring a limited region of space) lead to a discretisation of Fourier space onto a lattice. Their place cell covariance structure argument then says allowed frequencies should lie on a ring since the spectrum is peaked in a small band of frequencies. Lastly, including a 3rd order regularisation on the code (such as non-negativity) induces a triplet interaction between frequencies on the ring, meaning they should add to zero - this is satisfied by a hexagonal code. 

Our argument also leads to lattice frequencies, but this is due to actionability and non-negativity. Then, from the space of all lattices, a band-pass filter argument chooses hexagons: the high-pass arises because the animal only explores a limited region of space, and the low-pass because the animal only wants to encode space up to some useful resolution. This creates a preferred an annulus in frequency space, and leads to a preference for a hexagonal lattice, since it most densely packs frequencies into the annulus that is optimal for encoding space. 

So the arguments have similar components - lattice frequencies, non-negativity, band-pass filters - but they put these pieces together in different ways. 

These technical differences, among others, lead our two theories to make different predictions. For example, we provide a normative derivation of multiple modules, which we believe only arise in 

38 

Published as a conference paper at ICLR 2023 

Sorscher et al. (2019) due to a quantization effect. Finally, and crucially in our opinion, our predictions result from a normative framework for understanding generic representations. 

## I ABLATION STUDIES 

We have argued that three principles - biological, functional, and actionable - are necessary to produce grid cells. In this section we show that removing any of these three and numerically optimising produces fundamentally different patterns, and we explain these results with the theory we’ve developed in this work. 

We study the representation of a small torus, since for periodic spaces the three terms appear cleanly in the loss, so can be easily excised, Appendix B. Figure 15 shows that removing any term stops grid cells emerging. 

**==> picture [278 x 383] intentionally omitted <==**

Figure 15: **A** With no non-negativity the code is simply built from _D_ non-harmonically related frequencies. **B** Without the functional term an optimal code can be made by increasing the constant vector sufficiently, and containing few frequencies, leaving a random pattern of sines and cosines. **C** Without actionability there is no push towards sparsity in fourier space. Bumps are still easy to positivise, without frequency sparsity there’s no reason to arrange them into lattices. Hence, this response looks a bit like grid cells with the peak positions randomised. 

39 

Published as a conference paper at ICLR 2023 

**No Non-negativity** Without non-negativity the code wants to maximise the size of each of the limited number of frequencies in the code, ensuring that they are non-harmonically related. As such, it builds a wavey but fairly random looking code. 

**No Functional** Without a functional term the loss simply wants the code to contain few frequencies and be non-negative, so produces random looking responses with a sparse fourier spectrum and a large constant offset to ensure non-negativity. 

**No Actionability** Without actionability the code wants to be non-negative but separable. Bumps are easily positivised and encode the space well, but there is no reason to arrange them into lattices, and it would actually be detrimental to co-ordinate the placement across neurons so that any hypothetical lattice axes align. As such, it builds a random but bumpy looking pattern. This observation will be important for our discussion of the coding of 3-dimensional space, Appendix M. 

## J LATTICE SIZE:PEAK WIDTH RATIO SCALES WITH NUMBER OF NEURONS 

Thanks to the actionability constraint, the number of neurons in a module controls the number of frequencies available to build the module’s response pattern. In our scheme the frequencies within one module organise into a lattice, and the more frequencies in the module, the higher the top frequency, and the correspondingly sharper the grid peaks. This link allows us to extract the number of neurons from a single neuron’s tuning curve in the module. In this section we add slightly more justification to this link. 

We begin with a representation of 1D position, _**g**_ ( _x_ ). When there are enough neurons the griddy response can be approximated as, 

**==> picture [260 x 11] intentionally omitted <==**

where _DC_ ( _ν_ ) is a Dirac comb with lengthscale _ν_ , _∗_ is convolution, and _µ_ is the grid peak width, Fig 16. The fourier transform of this object is simple, Fig 16, 

**==> picture [270 x 24] intentionally omitted <==**

**==> picture [396 x 137] intentionally omitted <==**

Figure 16: Approximate Large Neuron Responses. With many neurons the grid response is approximately a dirac comb convolved with a Gaussian, and hence the frequency response is approximately a Gaussian multiplied by a Dirac Comb. Actionability implies sparsity in fourier space, which we approximate as a finite number of frequencies having power above some threshold _τ_ , i.e. a sufficiently fast decay in frequency space, which corresponds to a sufficiently broad grid peak width. 

We can now extract the tradeoff exactly. In this continuous approximation the equivalent of actionability’s sparsity in frequency space is that the frequency spectra must decay sufficiently fast i.e. the number of frequencies with power above some small threshold must be less than half the number of neurons. This number is controlled by the ratio of _µ_ and _ν_ . We’ll set some arbitrary low scaled threshold, _τ_ , which defines the power a frequency must have, relative to the constant component, to be considered as a member of the code. The actual value of _τ_ is inconsequential, as we just want 

40 

Published as a conference paper at ICLR 2023 

scaling rules. Then we’ll derive the scaling of the frequency at which the amplitude of the gaussian drops below threshold, _ω[∗]_ : 

**==> picture [264 x 59] intentionally omitted <==**

Now we can ask how many frequencies there are in the code, by counting the number of peaks of the Dirac comb that occur before this threshold. Counting from 0, because in 1D negative frequencies are just scaled versions of positive frequencies: 

**==> picture [249 x 26] intentionally omitted <==**

Therefore, in 1D, when there are enough neurons, the number of frequencies, and therefore the number of the neurons scales with the lattice to peak width ratio: 

**==> picture [214 x 21] intentionally omitted <==**

A completely analogous argument can be made in 2D, Again the cutoff frequency is _ω[∗] ∝ µ_ 1[.][A] different scaling emerges, however, because the number of frequencies in a dirac comb lower than some threshold scales with dimension. The frequency density of the dirac comb is proportional to _ν_ 1[2][peaks per unit area with the specifics depending on the shape of the frequency lattice, so we’re] asking how many peaks are there in a half circle of radius _ω[∗]_ . This is simple, 

**==> picture [261 x 71] intentionally omitted <==**

Hence we recover the stated scaling, 

## K OPTIMAL RELATIVE ANGLE BETWEEN MODULES 

Our analysis of the full loss, Appendix E, suggested that optimal representations should contain multiple modules, and each module should be chosen such that its frequencies are optimally nonharmonically related to the frequencies in other modules. This is a useful principle, but the full implications are hard to work through exactly. In this section we use rough approximations and coarse calculations to make estimates of one aspect of the relationships between modules: the optimal relative angle between lattice axes. Our scheme begins by calculating a smoothed frequency lattice density as a function of angle, _ρ_ ( _ψ_ ). It then aligns two of these smoothed densities, representing two modules, at different angular offsets, and finds the angle which minimises the overlap. This angle is the predicted optimal angle. We then extend this to multiple modules by searching over all doubles or triples of alignment angles for the minimal overlap of three or four densities. We will talk through the details of this method, and arrive at the results that are quoted in section 4.2. 

If you imagine standing at the origin in frequency space, corresponding to the constant component, and looking to infinity at an angle _ψ_ to the _kx_ axis, the density function, _ρ_ ( _ψ_ ), measures, as a function of _ψ_ , the number of smoothed frequencies that you see, fig 17A. We assume there are many neurons in this module, and hence many frequencies in the frequency lattice. Then we make the same approximation as in eqns. 91 and 92, that the frequency response is a hexagonal grid multiplied by a decaying Gaussian. The lengthscale of this Guassian is the first parameter that will effect our results, and it scales linearly with the number of neurons in the module. Then we try and capture the repulsive effects of the lattice. Each lattice point repels frequencies over a nearby region, as calculated in Section E.4. This region is of size _∼_ 21 _L_[,][where] _[L]_[is][the][exploration][lengthscale] of the animal. We therefore smooth the grid peaks in our density function by convolving the lattice with a Gaussian. We choose our units such that _L_ = 1, then the width of this smoothing Gaussian is also order 1. The second important parameter is then the grid lattice lengthscale. The larger the 

41 

Published as a conference paper at ICLR 2023 

grid cell lengthscale the more overlapping the repulsive effects of the frequencies will be, and the smoother the repulsive density, _ρ_ ( _ψ_ ). In maths, 

**==> picture [335 x 26] intentionally omitted <==**

where _kr_ is the radial part of the frequency. We calculate the obvious numerical approximation to this integral, Fig 17B, and in these calculations we ignore the effect of higher harmonics in equation E.4. This isn’t as bad as is sounds, since higher harmonics contribute density at the same angle, _ψ_ , part of the reason we chose to calculate this angular density. 

**==> picture [396 x 279] intentionally omitted <==**

Figure 17: **A: Smoothed Angular Density** We stand at the origin and look out at angle _ψ_ . We then count the density of smoothed grid frequency peaks along this line, where the smoothing occurs over lengthscale _L_[1][.] **[B: Smoothed Density Plot.][C: Overlap of Density Plots at Offsets][ ∆]** _**[ψ]**_[ This] curve shows a clear minima at 4 degrees from perfect alignment of grid axes. **D: Three Module Overlaps** The overlap (left) and the log of the overlap (right) show similar patterns as a function of the two angular offsets between modules, and the overlap is minimise for stepwise offsets of around 4 degrees. 

The next stage is finding the optimal angle between modules, starting with two identical modules. We do this by overlapping copies of _ρ_ ( _ψ∥µ, ν_ ). For simplicity, we start with two identical lattices and calculate the overlap as a function of angular offset: 

**==> picture [302 x 24] intentionally omitted <==**

Then the predicted angular offset is, 

**==> picture [258 x 18] intentionally omitted <==**

42 

Published as a conference paper at ICLR 2023 

Figure 17C shows this is a small angular offset around 4 degrees, though it can vary between 3 and 8 degrees depending on _µ_ and _ν_ . An identical procedure can be applied to multiple modules. For example, for the arrangement of three modules we define, 

**==> picture [373 x 24] intentionally omitted <==**

and find the pair of offsets that minimise the overlap. For identical modules this also predicts small offsets between modules, of around 4 degrees between each module, Figure 17D, and similarly three identical modules should be oriented at multiples of 4 degrees from a reference lattice (i.e. offsets of 4, 8, and 12). As shown in Figure 5E, these small offsets appear to be present in data, validating our prediction. 

There are many natural next steps for this kind of analysis. In future we will explore the effect of different lattice lengthscales and try to predict the optimal module arrangement. Another simple analysis you can do is explore how changing the grid lengthscale, _ν_ , effects the optimal relative angle. The larger the grid lattice lengthscale, the smaller its frequency lattice, and the more smooth the resulting repulsion density is. As a result, the optimal relative angle between large modules is larger than between small modules, a prediction we would like to test in data. It would be interesting to apply more careful numerical comparisons, for example matching the _ν_ and _µ_ to those measured in data, and comparing the real and optimal angular offsets. 

## L ROOM GEOMETRY ANALYSIS 

The functional objective depends on the points the animal wants to encode, which we assume are the points the animal visits. As such, the exploration pattern of the animal determines the optimal arrangement of grids, through the appearance of _p_ ( _x_ ) in the functional objective. Different constraints to the exploration of the animal, such as different sized environments, will lead to different optimal representations. In this section we analyse the functional objective for a series of room shapes, and show they lead to the intricate frequency biases suggested in Section 4.3. 

## L.1 1-DIMENSONAL BOX 

To begin and to set the pattern for this section, we will study the representation of 1-dimensional position in a finite box. Ignoring the effects of _χ_ for now, our loss is, 

**==> picture [272 x 30] intentionally omitted <==**

Making the symmetry assumption as in Section E our loss is, 

**==> picture [285 x 30] intentionally omitted <==**

Changing variables to _α_ = _x − x[′]_ , _β_ = _x_ + _x[′]_ , Figure 18A, 

**==> picture [385 x 60] intentionally omitted <==**

Performing the expansion as in Section E we reach: 

**==> picture [379 x 46] intentionally omitted <==**

43 

Published as a conference paper at ICLR 2023 

Term A behaves the same as before, so we again study the series expension of term B, the analogue of equation 77. The 0[th] order term is a constant with respect to the code, but the first order term provides the main frequency biasing effect, as in Section E.4. 

**==> picture [322 x 27] intentionally omitted <==**

Hence the 1-dimensional box coarsely creates a high frequency bias ( _> L_ 1[),][but][also][encourages] frequencies that fit whole numbers of wavelengths within the length of the box, Figure 18B. 

Before we move on we will study the second order term. We won’t repeat this for future finite rooms as it shows basically the same effect as in Section E.4: coarsly frequencies repel each other up to a lengthscale _L_[1][.][However,][as][for][the][first][order][term,][there][is][additional][structure,][i.e.][subsidiary] optimal zeros in the loss, that could be of interest: 

**==> picture [349 x 53] intentionally omitted <==**

This is fundamentally a repulsion between frequencies closer than _L_[1][from][one][another,][fig][18C.] Additionally, the repulsion is zero when the difference between frequencies is exactly[2] _L[π]_[times an] integer. 

**==> picture [396 x 207] intentionally omitted <==**

Figure 18: **A: Changing Integration Variables** The logic behind the integration change in 105. **B: 1D Box Frequency Bias** As in equation 108, shows both a high frequency bias and a preference for integer numbers of wavelengths in the box. **C: 1D Box Frequency Interaction** Plot of equation 109, shows both a high frequency bias, a repulsion between frequencies, and non-trivial optimal interaction differences. 

## L.2 2-DIMENSIONAL BOX 

A very similar analysis can be applied to the representation of a 2-dimensional box, and used to derive the frequency bias plotted in Figure 5F. We reach an exactly analogous point to equation 106, 

44 

Published as a conference paper at ICLR 2023 

**==> picture [330 x 65] intentionally omitted <==**

Again we’ll study the first order term of the series expansion, 

**==> picture [290 x 26] intentionally omitted <==**

This is exactly the bias plotted in Figure 5F. Changing to rectangles is easy, it is just a rescaling of one axis, which just inversely scales the corresponding frequency axis. 

## L.3 CIRCULAR ROOM 

The final analysis we do of this type is the hardest, a circular environment. It follows the same pattern, make the symmetry assumption, expand the series. Doing so we arrive at the following first order term: 

**==> picture [327 x 26] intentionally omitted <==**

where ( _r, ψ_ ) is a radial co-ordinate system, _**x**_ = � _rr_ cos sin _ψ ψ_ �. Using the double angle formula to spread the cosine, and rotating the 0 of each _ψ_ variable to align with _**k** d_ , we get: 

**==> picture [402 x 40] intentionally omitted <==**

The second integral is 0, because sine is odd and periodic. We can perform the first integral using the following Bessel function properties, 

**==> picture [272 x 26] intentionally omitted <==**

Hence, 

**==> picture [275 x 27] intentionally omitted <==**

Which can be solved using another Bessel function property, 

**==> picture [256 x 26] intentionally omitted <==**

Therefore, 

**==> picture [248 x 25] intentionally omitted <==**

This is exactly the circular bias plotted in Figure 5G. Placing the base frequencies of grid module on the zeros of this bessel function would be optimal, i.e. calling a zero _ξ_ , then the wavelengths of the grid modules should optimally align with, 

**==> picture [218 x 23] intentionally omitted <==**

45 

Published as a conference paper at ICLR 2023 

This corresponds to grids with wavelengths that are the following multiples of the circle diameter: 0 _._ 82 _,_ 0 _._ 45 _,_ 0 _._ 31 _,_ 0 _._ 24 _,_ 0 _._ 19 _, . . ._ . Though, as with the other predictions, the major effect is the polynomial decay with frequency, so these effects will all be of larger importance for the larger grid modules. As such, we might expect only the first two grid modules to fit this pattern, the others should, in our framework, focus on choosing their lattice parameters to be optimally non-harmonic. 

## M REPRESENTATIONS OF CIRCLES, SPHERES, AND 3-DIMENSIONS 

We believe our approach is relevant to the representation of many variables beyond 2-dimensional space. Most simply we can directly apply the tools we’ve developed to the representation of any variable whose transition structure is a group, Section A.1. This is actually true for both numerical and analytic approaches, but here we focus mainly on the numerical approach. We discuss the representation of an angle on a ring, a point on a sphere, and 3 dimensional space. Additional interesting variables might include a position in hyperbolic space (since tree-like category structures, such as the taxonomic hierarchy of species, are best described by hyperbolic spaces), or the full orientation of an object in 3-dimensional space. 

For starters, we have frequently referenced the representation of an angle, _**g**_ ( _θ_ ). This is also something measured in brain, in the famous head direction circuit, perhaps the most beautiful circuit in the brain (Kim et al., 2017). There, you measure neurons that have unimodal tuning to heading direction. We match this finding, Figure 19A. This is understandable since, as discussed, on a finite space you still want a lattice module, but _χ_ , encourages you to be low frequency and there is no high frequency bias, since the space is finite and _p_ ( _θ_ ) is uniform. Thus, place cells are optimal. If we included more neurons it would likely form multiple modules of cells with higher frequency response properties. 

We can also apply our work to the representation of a point on a sphere. Again, with the low frequency bias place cells are optimal, Figure 19B. Without it, or conceivably with enough neurons that multiple modules form, you can get many interesting patterns, Figure 19C-D. These could be relevant to the representation of object orientations, or in virtual reality experiments where animals must truly explore spherical spaces. 

Finally, we can equally apply our framework to the representation of a point in three dimensional space. Grid cells have been measured while an animal explores in 3D and shown to have irregular firing fields in both bats (Ginosar et al., 2021), and mice (Grieves et al., 2021). Analogously to the griddy modules in one and two dimensions, our framework predicts griddy three dimensional responses that are similarly densely packing, which is verified in 19E. However, in Appendix I we performed ablation studies and found that removing the actionable constraint led to multimodal tuning curves without structure, and we find the same for 3D, Figure 19F, perhaps matching the multimodal but unstructured representation found in the brain (e.g. Figure 19G from Ginosar et al. (2021)). As such, it seems that in three dimensions the animals are building a non-negative and discriminative representation without the constraint to path integrate. Therefore, we suggest that the animals have sacrificed the ability to manipulate their internal representations in 3D and instead focus on efficiently encoding the space. 

46 

Published as a conference paper at ICLR 2023 

**==> picture [318 x 481] intentionally omitted <==**

Figure 19: **A** Representation of an angle on the ring. With a low frequency bias the optimal one module response is a set of head-direction cells. **B** Representation of position on a sphere. With a low frequency response place cells are again optimal. **C-D** Allowing the optimiser to find other modules produces funky looking responses on the sphere, like grids ( **C** ) and ‘pole & orbit’ cells ( **D** .) **E** A module of densely packing grids in 3D space. **F** The same cells without the actionability constraint, as we did for 2D in Figure 15. **G** Recordings of multimodal cells from bat entorhinal cortex from Ginosar et al. (2021). 

47 

