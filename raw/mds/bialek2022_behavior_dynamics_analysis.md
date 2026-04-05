PHYSICS **RESEARCH ARTICLE** NEUROSCIENCE 

**OPEN ACCESS** 

**==> picture [30 x 30] intentionally omitted <==**

## **On the dimensionality of behavior** 

William Bialek[a,b,c,1] 

Contributed by William Bialek; received October 19, 2020; accepted March 4, 2022; reviewed by Andr´e Brown, Sandeep Robert Datta, and Samuel Sober 

**There is a growing effort in the “physics of behavior” that aims at complete quantitative characterization of animal movements under more complex, naturalistic conditions. One reaction to the resulting explosion of high-dimensional data is the search for low-dimensional structure. Here I try to define more clearly what we mean by the dimensionality of behavior, where observable behavior may consist of either continuous trajectories or sequences of discrete states. This discussion also serves to isolate situations in which the dimensionality of behavior is effectively infinite.** 

## information _|_ prediction _|_ complexity 

Observations on behavior provide a window into the dynamics of the brain and mind. This is an ancient idea, now receiving renewed attention because of the explosive growth of methods for quantitative measurements of behavior (1–8). These methods produce enormous quantities of raw data, such as high-resolution videos, so there is an obvious practical interest in data compression. This often involves searching for a low-dimensional description of the animal’s configuration or posture at each moment in time. This search is grounded both by the observation that even large and complex animals have relatively small numbers of muscles or joints and by direct evidence that motor behaviors are described by low-dimensional models in organisms from the worm _Caenorhabditis elegans_ to humans and nonhuman primates (1, 9–14). 

Reducing great volumes of video data to time series for just a few degrees of freedom is a triumph. The fact that this now can be done more or less automatically with machine learning methods means that exhaustive and quantitative characterization of behavior is possible in a much wider range of organisms, under a wider range of conditions. But the classical literature on dynamical systems reminds us that the time series of even a single variable could encode a higher-dimensional structure (15, 16). Indeed, this seems natural: The brain that generates behavior has many degrees of freedom, and observations of behavior should be sensitive to these potentially high-dimensional dynamics. On the other hand, the dynamics of large neural networks might be confined to low-dimensional manifolds, perhaps to match the dimensionality of motor behaviors (17–20). 

All of these developments point to the problem of defining the dimensionality of behavior. In the extreme, we can imagine that the observable behavior reduces to a single function of time, as with the opening angle of a clamshell. Can we analyze this time series to identify a well-defined dimensionality for the underlying dynamics? Is it possible that this dimensionality is effectively infinite? 

## **Significance** 

How do we characterize animal behavior? Psychophysics started with human behavior in the laboratory, and focused on simple contexts, such as the decision among just a few alternative actions in response to sensory inputs. In contrast, ethology focused on animal behavior in the natural environment, emphasizing that evolution selects potentially complex behaviors that are useful in specific contexts. New experimental methods now make it possible to monitor animal and human behaviors in vastly greater detail. This “physics of behavior” holds the promise of combining the psychophysicist’s quantitative approach with the ethologist’s appreciation of natural context. One question surrounding this growing body of data concerns the dimensionality of behavior. Here I try to give this concept a precise definition. 

## **A Context for Phenomenology** 

The quantitative analysis of behavior, including what follows here, is unapologetically phenomenological. The question is not “How does the brain generate behavior?” but rather “What is it about behavior that we would like to explain?” In an era of highly mechanistic biology, this emphasis on phenomenological description may seem odd. So, at the risk of repeating things that are well known, it is useful to remind ourselves of the long historical context for this approach. 

If we want to explain why we look like our parents, a qualitative answer is that we carry copies of their DNA. But, if we want to understand the reliability with which traits pass from generation to generation, then DNA structure is not enough—the free energy differences between correct and incorrect base pairing are not sufficient to explain the reliability of molecular copying if the reactions are allowed to come to thermal equilibrium, and this problem arises not just in DNA replication but in every step of molecular information transmission. Cells achieve their observed reliability by holding these reactions away from equilibrium, allowing for proofreading or error correction (21, 22). In the absence of proofreading, the majority of proteins would contain at least one incorrect amino acid, and _∼_ 10% of our genes would be different from those carried by either parent; these error rates are orders of magnitude larger than observed. 

Author affiliations:[a] Joseph Henry Laboratories of Physics, Princeton University, Princeton, NJ 08544; bLewis-Sigler Institute for Integrative Genomics, Princeton University, Princeton, NJ 08544; and cInitiative for the Theoretical Sciences, The Graduate Center, City University of New York, New York, NY 10016 

Author contributions: W.B. designed research, performed research, and wrote the paper. 

Reviewers: A.B., MRC London Institute of Medical Sciences; S.R.D., Harvard Medical School; and S.S., Emory University. 

The author declares no competing interest. 

Copyright © 2022 the Author(s). Published by PNAS. This open access article is distributed under Creative Commons Attribution License 4.0 (CC BY). 

See online for related content such as Commentaries. 1Email: wbialek@princeton.edu. Published April 29, 2022. 

https://doi.org/10.1073/pnas.2021860119 **1 of 8** 

**PNAS** 2022 Vol. 119 No. 18 e2021860119 

These quantitative differences are so large that life without proofreading would be qualitatively different.[*] 

The example of proofreading highlights the importance of starting with a quantitative characterization of the phenomena we are trying to explain. For brains and behavior, this is an old idea. In the late nineteenth century, many people were trying to turn observations on seeing and hearing into quantitative experiments, creating a subject that would come to be called psychophysics (23). By _∼_ 1910, these experiments were sufficiently well developed that Lorentz could look at data on the “minimum visible” and suggest that the retina is capable of counting single photons (24), and Rayleigh could identify the conflict between our ability to localize low-frequency sounds and the conventional wisdom that we are “phase deaf” (25). Both of these essentially theoretical observations, grounded in quantitative descriptions of human behavior, drove experimental efforts that unfolded over more than half a century. 

Also _∼_ 1910, von Frisch (26) was doing psychophysics experiments to demonstrate bees could, in fact, discriminate among the beautiful colors of the flowers that they pollinate.[†] But he took these experiments in a very different direction, focusing not on the discrete choices made by individual bees but on how these individuals communicated their sensory experiences to other residents of the hive, leading to the discovery of the “dance language” of bees. What grew out of the work by von Frisch and others was ethology (28), which emphasizes the richness of behavior in its natural context, the context in which it was selected for by evolution. Because ethologists wrestle with complex behaviors, they often resort to verbal description. In contrast, psychophysicists focus on situations in which subjects are constrained to a small number of discrete alternative behaviors, so it is natural to give a quantitative description by estimating the probabilities of different choices under various conditions. 

The emergence of a quantitative language for the analysis of psychophysical experiments was aided by the focus on constrained behaviors, but was not an automatic consequence of this focus. For photon counting in vision, the underlying physics suggests how the probability of seeing vs. not seeing will depend on light intensity (29), but the observation that human observers behave as predicted points to profound facts about the underlying mechanisms (30). Attempts to formalize the problems of detection led to a more general view of the choices among discrete alternative behaviors being discriminations among signals in a background of noise (31), and, in the 1950s and 1960s, this view was exported to experimental psychology (23). Much of this now seems like an exercise in probability and statistics, something obviously correct, but the early literature records considerable skepticism about whether this (or perhaps any) mathematization of human behavior would succeed. 

More generally, quantitative phenomenology has been foundational, certainly in physics and also in the mainstream of biology. Mendel’s genetics was a phenomenological description of the patterns of inheritance, and the realization that genes are arranged linearly along chromosomes came from a more refined quantitative analysis of these same patterns (32). The work of Hodgkin and Huxley (33) led to our modern understanding of electrical activity in terms of ion channel dynamics, but explicitly eschewed mechanistic claims in favor of phenomenology. The 

> *In retroviruses, including HIV, reproduction occurs without proofreading. The dramatically accelerated pace of evolution in these viruses gives a glimpse of how different life would be if the transmission of genetic information depended on base pairing alone. 

> †See also the remarkable early work from Turner, who studied both insect behavior and neuroanatomy in the decades straddling 1900 (27). 

idea that transmission across a synapse depends on transmitter molecules packaged into vesicles emerged from the quantitative analysis of voltage fluctuations at the neuromuscular junction (34). 

Even when we are searching for microscopic mechanisms, it is not anachronistic to explore macroscopic descriptions. Time and again, the scientific community has leaned on phenomenology to imagine the underlying mechanisms, often taking literally the individual terms in a mathematical description as representing the actual microscopic elements for which we should be searching, whether these are genes, ion channels, synaptic vesicles, or quarks (35–37). What is anachronistic, in the literal sense of the word, is to believe that microscopic mechanisms were discovered by direct microscopic observations without guidance from phenomenology on a larger scale. 

In this broad context, how can we construct a quantitative phenomenology of complex, naturalistic behaviors? When we do psychophysics, we characterize behaviors with numbers that are meaningfully comparable across situations and across species. To give but one example, we can discuss the accumulation of evidence for decisions that humans and nonhuman primates make based on visual inputs, but we can use the same mathematical language to discuss decisions made by rodents based on auditory inputs (38). A quantitative characterization of naturalistic behaviors requires, similarly, that we attach comparable numbers to very different kinds of time series. The dimensionality of behavior is a candidate for this sort of unifying mathematical language. 

## **Two Examples** 

To work toward a sharper definition, consider the case in which the behavior we observe is just a single function of time, _x_ ( _t_ ). Two examples of such trajectories are shown in Fig. 1, _Left_ , and we will see that these correspond to one-dimensional (blue) and twodimensional (red) systems. Qualitatively, the blue trajectory varies on one characteristic time scale, while the red trajectory involves rough movements on a short time scale superposed on smoother movements over a longer time scale. Our task is to make these observations precise. 

**==> picture [240 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>1<br>3<br>2 0.8<br>1<br>0.6<br>0<br>0.4<br>-1<br>-2 0.2<br>-3<br>0<br>-4<br>5000 5005 5010 -20 0 20<br>t/ /<br>c c<br>x(t) C()<br>**----- End of picture text -----**<br>


**Fig. 1.** Two examples of behavioral trajectories ( _Left_ ) and their correlation functions ( _Right_ ). One-dimensional example, from Eq. **1** , is shown in blue. Two-dimensional example, from Eq. **4** , is shown in red. Behavioral trajectories are offset for clarity, and time is measured in units of the correlation time _τc_ . 

**2 of 8** https://doi.org/10.1073/pnas.2021860119 

pnas.org 

Let’s work backward and start with a model for the behavior, a model in which it seems clear that the behavior really is one dimensional: The observed behavioral trajectory _x_ ( _t_ ) is described completely by 

**==> picture [178 x 22] intentionally omitted <==**

where _η_ ( _t_ ) is white noise, 

**==> picture [190 x 12] intentionally omitted <==**

It is important that the noise source is white; nonwhite noise sources, which themselves are correlated over time, are equivalent to having hidden degrees of freedom that carry these correlations. The blue trajectory in Fig. 1, _Left_ is drawn from a simulation of Eq. **1** with _⟨x_[2] _⟩_ = 1. 

The observable consequences of the dynamics in Eqs. **1** and **2** . are well known: _x_ ( _t_ ) will be a Gaussian stochastic process, with the two-point correlation function 

**==> picture [208 x 13] intentionally omitted <==**

shown in Fig. 1, _Right_ . We recall that, for a Gaussian process, once we specify the two-point function, there is nothing else to say about the system. Importantly, we can turn this around: If the observed behavior is a Gaussian stochastic process, and the correlations decay exponentially as in Eq. **3** , then Eqs. **1** and **2** are a complete description of the dynamics. 

An example of a clearly two-dimensional system involves not only the observable _x_ ( _t_ ) but also an internal variable _y_ ( _t_ ), 

**==> picture [217 x 25] intentionally omitted <==**

To keep things simple, we can assume that the driving noises are independent of one another, and, again, they should be white so that we are not hiding additional variables that carry correlations. Since _y_ is hidden, its units are arbitrary, which allows us to have the strength of the noise driving each variable be the same without loss of generality, so that 

**==> picture [214 x 13] intentionally omitted <==**

The choice to give each variable the same correlation time is just for illustration, as is the symmetry of the dynamical matrix; the red trajectory in Fig. 1, _Left_ is drawn from a simulation of Eq. **4** with _⟨x_[2] _⟩_ = 1 and _a_ = 0.75. Again, _x_ ( _t_ ) is Gaussian, but now the correlation function has two exponential decays, 

**==> picture [218 x 39] intentionally omitted <==**

shown in Fig. 1, _Right_ . The short time scale _τc/_ (1 + _a_ ) corresponds to the rough movements seen in the trajectory, while _τc/_ (1 _− a_ ) corresponds to the smoother movements. 

We see that a one-dimensional system generates behavior with a correlation function that has one exponential decay, while a two-dimensional system generates a correlation function with two exponential decays. We would like to turn this around, and say that, if we observe a certain structure in the behavioral correlations, then we can infer the underlying dimensionality. 

## **Gaussian Processes More Generally** 

Analyzing behavioral trajectories by constructing explicit dynamical equations, as in Eq. **1** or **4** , may not be the best approach. In particular, if there are hidden dimensions, then there is no preferred coordinate system in the space of unmeasured variables, and hence no unique form for the dynamical equations. Let us think, instead, about the probability distribution of the observed trajectories _x_ ( _t_ ). For Gaussian processes, this has the form 

**==> picture [217 x 47] intentionally omitted <==**

where the integrals run over the interval of our observations, which should be long. The kernel _K_ ( _τ_ ) is inverse to the correlation function, 

**==> picture [212 x 23] intentionally omitted <==**

We can divide the full trajectory _x_ ( _t_ ) into the past, **x** p, with _t ≤_ 0, and the future, **x** f, with _t >_ 0. Schematically, 

**==> picture [207 x 36] intentionally omitted <==**

where _K_ pf couples the past and future. More explicitly, 

**==> picture [241 x 24] intentionally omitted <==**

If _K_ pf is of finite rank, so that 

**==> picture [192 x 31] intentionally omitted <==**

then everything that we can predict about future behavior given knowledge of past behavior is captured by _D_ features, 

**==> picture [191 x 40] intentionally omitted <==**

Eq. **14** is telling us that the features _{Fμ}_ provide “sufficient statistics” for making predictions. We recall that, in a dynamical system with _D_ variables, 

**==> picture [211 x 21] intentionally omitted <==**

predicting the future ( _t >_ 0) requires specifying _D_ initial conditions (at _t_ = 0). In this precise sense, the number of variables that we need to achieve maximum predictive power is the dimensionality of the dynamical system. To complete the argument, we need to show that _K_ pf has finite rank when correlations decay as a finite combination of exponentials; see _Appendix A_ . 

In the case of Gaussian stochastic processes, we thus arrive at a recipe for defining the dimensionality of the underlying dynamics. We estimate the correlation function, take its inverse to find the kernel, and isolate the part of this kernel which couples past and future. If this past–future kernel is of finite rank, then we can identify this rank with the dimensionality of the system. In Fig. 2, _Top_ we see a sample trajectory (in red) from a system that is, by 

https://doi.org/10.1073/pnas.2021860119 **3 of 8** 

**PNAS** 2022 Vol. 119 No. 18 e2021860119 

**==> picture [240 x 208] intentionally omitted <==**

**----- Start of picture text -----**<br>
5<br>0<br>-5<br>0 100 200 300 400<br>t/ t<br>10 [0]<br>10 [-5]<br>10 [-10]<br>10 [0] 10 [1]<br>rank<br>x(t)<br>eigenvalue<br>**----- End of picture text -----**<br>


**Fig. 2.** Sample trajectories ( _Top_ ) and spectra of the matrix _K_ pf ( _Bottom_ ). In red is an example in which the underlying dynamics is three dimensional. In blue is an example with power law correlations, as in Eq. **17** with _α_ = 1 _/_ 2, which is effectively infinite dimensional. Time is measured in discrete steps Δ _t_ , and spectra are computed in windows of duration _T_ = 100Δ _t_ ( _×_ ) or _T_ = 1000Δ _t_ ( _◦_ ). Details are provided in _Appendix B_ . 

construction, three dimensional, with correlation times 4 _×_ , 32 _×_ , and 256 _×_ the discrete time step (Δ _t_ ) of our observations. As explained in _Appendix B_ , the coefficients _aμ_ in Eq. **13** can be found as the eigenvalues of a symmetric matrix, and these eigenvalues are plotted in Fig. 2, _Bottom_ in rank order (in red). This numerical analysis yields three clearly nonzero eigenvalues, with other eigenvalues below 10 _[−]_[10] . Importantly, we find essentially the same three eigenvalues when the analysis is done in time windows of very different sizes—here _T_ = 100Δ _t_ and _T_ = 1, 000Δ _t_ , smaller and larger, respectively, than the longest correlation time. 

The past–future coupling is not guaranteed to be of finite rank. More generally, if we analyze signals in a window of size _T_ , then the rank can grow with _T_ . This happens, for example, if behavioral correlations decay as a power of time, 

**==> picture [195 x 24] intentionally omitted <==**

Fig. 2, _Top_ shows a sample trajectory from a Gaussian process with this correlation function (in blue), and Fig. 2, _Bottom_ shows the associated spectrum of coefficients _aμ_ for _α_ = 1 _/_ 2 (in blue). This illustrates both that there is no obvious cutoff to the spectrum and that the spectrum extends farther when the analysis is done in longer time windows [ _T_ = 100Δ _t_ ( _×_ ) vs. _T_ = 1000Δ _t_ ( _◦_ )]. Indeed, the larger the window, the farther the spectrum extends, with no bound. Under these conditions, the dimensionality is effectively infinite. 

The possibility that behavioral correlations decay as a power of time has a long and sometimes contentious history. It thus is worth noting that scaling of the correlation function implies an effectively infinite dimensionality, but it is not required. We can imagine situations in which the kernel _K_ pf has an arbitrarily large number of nonzero eigenvalues in the limit of long observation times even if the correlation is not precisely a power law. 

While the relation of dimensionality to the spectrum of _K_ pf is attractive, estimating this spectrum from finite data can be challenging. Even if the true spectrum has only a finite number of nonzero eigenvalues, in matrices built from finite samples of 

data, the zero eigenvalues will be replaced by a continuous spectrum, and this could make it difficult, in practice, to distinguish finite from infinite dimensional processes. At the same time, it is important to emphasize that difficulty in resolving eigenvalues against a continuum generated by finite sample size is not evidence for low dimensionality, nor should a continuum be assigned as noise without further analysis. Random matrix theory provides quantitative predictions for spectral broadening in closely related contexts, including the dependence of spectra on sample size and matrix dimensionality, and these should provide a basis for identifying the contributions of noise to the observed eigenvalue spectra (39). 

## **Discrete States** 

In many cases, it is natural to describe animal behavior as moving through a sequence of discrete states. We do this, for example, when we transcribe human speech to text, and when we describe a bacterium as running or tumbling (40). This identification of discrete states is not just an arbitrary quantization of continuous motor outputs, nor should it be a qualitative judgment by human observers. Discrete states should correspond to distinguishable clusters, or resolvable peaks in the distribution over the natural continuous variables, and the dynamics should consist of movements in the neighborhood of one peak that are punctuated by relatively rapid jumps to another peak (e.g., ref. 3). A “mechanism” for such discreteness is the existence of multiple dynamical attractors, with jumps driven by noise (e.g., refs. 1 and 13). 

When behavioral states are discrete, how do we define dimensionality? Once again, it is useful to think about the simplest case, where there are just two behavioral states—perhaps “doing something” and “doing nothing”—and time is marked by discrete ticks of a clock. We can represent the two states at each time _t_ by an Ising variable _σt_ = _±_ 1. If the sequence of behavioral states were Markovian, then _σt_ depends only on _σt−_ 1, and, because _σ_[2] = 1, the only possible stationary probability distribution for the sequences _σ_ 1, _σ_ 2, _· · ·_ , _σT_ is 

**==> picture [230 x 31] intentionally omitted <==**

which is the one-dimensional Ising model with nearest-neighbor interactions. Importantly, if we measure the correlations of the fluctuations in behavioral state around its mean, 

**==> picture [203 x 11] intentionally omitted <==**

we find that these correlations decay exponentially, 

**==> picture [186 x 14] intentionally omitted <==**

where we can express _τc_ in terms of _h_ and _J_ (41). This reminds us of the exponential decays in the continuous case with Gaussian fluctuations. 

Suppose that we have only two states, but observe correlations that do not decay as a single exponential. Then the probability distribution _P_ ( _{σt }_ ) must have terms that describe explicit dependences of _σt_ on _σt[′]_ with _t − t[′] >_ 1. This can be true only if there are some hidden states or variables that carry memory across the temporal gap _t − t[′]_ . A sensible definition for the dimensionality of behavior then refers to these internal variables. 

Imagine that we observe the mean of the behavioral variable, _⟨σ⟩_ , and the correlation function _C_ ( _t − t[′]_ ). What can we say about the probability distribution _P_ ( _{σt }_ )? There are infinitely many models that are consistent with measurements of just these 

**4 of 8** https://doi.org/10.1073/pnas.2021860119 

pnas.org 

(two-point) correlations, but there is one that stands out as having the minimal structure required to match these observations (42). Said another way, there is a unique model that predicts the observed correlations but otherwise generates behavioral sequences that are as random as possible. This minimally structured model is the one that has the largest possible entropy, and it has the form 

**==> picture [238 x 46] intentionally omitted <==**

where the parameter _h_ must be adjusted so that the model predicts the observed mean behavior _⟨σ⟩_ , and the function _J_ ( _t − t[′]_ ) must be adjusted so that the model predicts the observed correlation function _C_ ( _t − t[′]_ ). 

Maximum entropy models have a long history, and a deep connection to statistical mechanics (42). As applied to temporal sequences, the maximum entropy models sometimes are referred to as maximum caliber (43). For biological systems, there has been interest in the use of maximum entropy methods to describe amino acid sequence variation in protein families (44–46), patterns of electrical activity in populations of neurons (47–51), velocity fluctuations in flocks of birds (52, 53), and more. There have been more limited attempts to use these ideas in describing temporal sequences, in neural populations (54) and in flocks (55–57). 

To connect with the previous discussion, for continuous variables, a Gaussian process is the maximum entropy model consistent with the measured (two-point) correlations. In particular, if correlations decay as a combination of exponentials, then, in discrete time, the relevant Gaussian model has maximum entropy consistent with correlations among a finite number of neighboring time points. These models can also be written as autoregressive processes (58). 

The maximum entropy model in Eq. **21** can be rewritten exactly as a model in which the behavioral state at time _t_ depends only on some internal variable _x_ ( _t_ ). As explained in _Appendix C_ , _x_ ( _t_ ) is not Gaussian, but the only coupling of past and future, again, is through a kernel _K_ ( _t_ ). This kernel is not the inverse of the observed behavioral correlations but of the effective interactions between states at different times, _J_ ( _τ_ ). But, importantly, we are considering quantities that are determined by the correlation function, and hence the problem is conceptually similar to the Gaussian case: We analyze the correlations to derive a kernel, and the dimensionality of behavior is the rank of this kernel. The maximum entropy model plays a useful role because it is the least structured model consistent with the observed correlations. 

If _x_ ( _t_ ) is one dimensional in the sense defined above, then the interactions decay over some fixed time scale, _J_ ( _t_ ) _∼ J_ 0 _e[−|][t][|][/τ]_ , and, at long times, the correlations also will decay exponentially. At the opposite extreme, if _x_ ( _t_ ) has effectively infinite dimensionality, then we can have _J_ ( _t_ ) _≈ J_ 0 _|t|[−][α]_ . Ising models with such power-law interactions are the subject of a large literature in statistical physics; the richest behaviors are at _α_ = 2, where results presaged major developments in the renormalization group and topological phase transitions (59–62). It would be fascinating if these models emerged as effective descriptions of strongly nonMarkovian sequences in animal behavior, as suggested recently (63). 

## **Generalization** 

In both the continuous Gaussian case and the discrete case, dimensionality can be measured through the problem of prediction. 

To make this more general, consider observations of behavior in a time window _−T < t < T_ ; for simplicity, I will keep the notation _x_ ( _t_ ) for the behavioral trajectory. Within each window, the trajectory _x_ ( _t <_ 0) defines the past **x** p, _x_ ( _t >_ 0) defines the future **x** f, and these are drawn from the joint probability distribution _PT_ ( **x** p, **x** f). To characterize the possibility of making predictions, we can measure the mutual information between past and future, 

**==> picture [244 x 30] intentionally omitted <==**

This “predictive information” _I_ pred( _T_ ) can have very different qualitative behaviors as _T_ becomes large (64). 

For a time series that can be captured by a finite-state Markov process, or more generally described by a finite correlation time, then _I_ pred( _T_ ) is finite as _T →∞_ . On the other hand, for Gaussian processes with correlation functions that decay as a power, as in Eq. **17** , the predictive information diverges logarithmically, _I_ pred( _T →∞_ ) _∝_ log _T_ , and similarly for discrete time series with power-law correlations.[‡] 

In the example of a dynamical system with _D_ variables, as in Eq. **16** , all the predictive power available will be realized if we can specify _D_ numbers, which are the initial conditions for integrating the differential equations. Thus we consider smooth mappings of the past into _d_ features, 

**==> picture [205 x 11] intentionally omitted <==**

For any choice of features, we can compute how much predictive information has been captured, and then we can maximize over the mapping, resulting in 

**==> picture [191 x 17] intentionally omitted <==**

which is the maximum predictive information we can capture with _d_ features in windows of duration _T_ . 

If the system truly is _D_ dimensional, then _D_ features of the past are sufficient to capture all of the available predictive information. This means that a plot of _I_ pred( _T_ ; _d_ ) vs. _d_ will saturate. To be precise, we are interested in what happens at large _T_ , so we can define 

**==> picture [177 x 26] intentionally omitted <==**

**==> picture [223 x 11] intentionally omitted <==**

**==> picture [174 x 12] intentionally omitted <==**

where the features _Fμ_ now are more complex functions of the past. But there are only _D_ of these features needed to make Eq. **26** true ( _μ_ = 1, 2, _· · ·_ , _D_ ), and so we conclude that the behavior has dimensionality _D_ . 

The equivalence of Eq. **26** to Eq. **14** immediately tells us that the general information theoretic definition of dimensionality agrees with the definition for Gaussian processes based on the spectrum of _K_ pf. In the Gaussian case, we see that the features _Fμ_ are just linearly filtered versions of the past, as in Eq. **15** . The connection to the discussion of two-state variables is a bit more complicated, and exploits the equivalence to an internal or latent variable as described in _Appendix C_ . 

> ‡If we observe a continuous variable in continuous time, then smoothness generates a formal divergence in the mutual information between past and future. Modern analyses of behavior typically begin with video data, with time in discrete frames, evading this problem. Alternatively, if measurements include a small amount of white noise, then the predictive information becomes finite even without discrete time steps. Thanks go to A. Frishman for emphasizing the need for care here. 

https://doi.org/10.1073/pnas.2021860119 **5 of 8** 

**PNAS** 2022 Vol. 119 No. 18 e2021860119 

## **Conclusion** 

The arguments here define the dimensionality of behavior as the minimum number of features of the past needed to make the maximally informative predictions about the future. As we consider pasts of longer duration, the dimensionality can grow, potentially without bound. The connection between dimensionality and prediction is familiar from the now classical literature on dynamical systems, which also reminds us that, in its most general form, any such definition runs into all the well-known difficulties of estimating dimensions from finite data (65). More useful is the result that, in some cases, estimating this predictive dimensionality reduces to analyzing the spectrum of a matrix. 

## **Data Availability.** There are no data underlying this work. 

## **Appendix** 

**A. Past–Future Kernels, Explicitly.** We are interested in the behavior of the kernel _K_ when the correlation function _C_ is a sum of exponentials. As noted above, we need to be a little careful to make this problem well posed. If we monitor a continuous variable in continuous time, then continuity leads to infinite mutual information between _x_ ( _t[−]_ ) and _x_ ( _t_[+] ). We can solve this either by assuming that observations are made at discrete ticks of a clock (as in video recordings) or by assuming that observations are made in a background of white noise. Here I will take the second approach. 

The statement that the correlation function is a sum of exponentials, but measurements are in a background of white noise, means that the observed correlation function 

**==> picture [231 x 31] intentionally omitted <==**

where _N_ is the strength of the noise. We want to construct the kernel _K_ ( _t_ ) that is the operator inverse to _C_ , as in Eq. **10** . We recall that this can be done by passing to Fourier space, 

**==> picture [183 x 51] intentionally omitted <==**

From Eq. **27** , we can see that 

**==> picture [232 x 67] intentionally omitted <==**

Then, to find _K_ ( _t_ ), we invert and transform back, being careful to isolate the contribution of the white noise term, 

**==> picture [232 x 63] intentionally omitted <==**

where 

**==> picture [210 x 32] intentionally omitted <==**

is a _M −_ 1 st-order polynomial in _ω_[2] , and 

**==> picture [239 x 31] intentionally omitted <==**

is a _M_ th-order polynomial in _ω_[2] . Note that both polynomials have all real and positive coefficients. 

We notice that _PM −_ 1( _ω_[2] ) _/PM_ ( _ω_[2] ) vanishes at large _|ω|_ , and _e[−][i][ω][t]_ vanishes for values of _ω_ with a large negative (positive) imaginary part if _t >_ 0 ( _t <_ 0). This means that we can do the integral over _ω_ in Eq. **33** by closing a contour in the complex plane. Then we can use the fact that 

**==> picture [184 x 30] intentionally omitted <==**

where _B_ is a constant and _{ω_ n[2] _[}]_[ are the roots of the polynomial.] The simplest case is where all _ω_ n[2][are real, in which case they must] be negative, and we can write _ω_ n = _−i λ_ n, with _λ_ n _>_ 0. Then, for _t >_ 0, we close the contour in the lower half plane, picking out the poles at _ω_ = _ω_ n, while, for _t <_ 0, we close the contour in the upper half plane, picking out the poles at _ω_ = _−ω_ n. The result is that 

**==> picture [244 x 55] intentionally omitted <==**

If we look back at the derivation of Eq. **12** , we can see that a delta function term in _K_ ( _t_ ) does not contribute to coupling past and future. Thus _K_ ( _t >_ 0) collapses into the form of Eq. **13** , 

**==> picture [201 x 77] intentionally omitted <==**

and the dimensionality _D_ = _M_ , as we hoped: If the observed behavioral variable is Gaussian, and the correlation function can be written as the sum of _M_ exponentials, then the system has underlying dimensionality _D_ = _M_ . It is useful to work out the case _M_ = 1. Then we have 

**==> picture [211 x 13] intentionally omitted <==**

And, after some algebra, we find 

**==> picture [181 x 39] intentionally omitted <==**

It is useful to think more explicitly about the fact that we have embedded a correlated signal in the background of white noise, so we can write 

**==> picture [181 x 43] intentionally omitted <==**

**6 of 8** https://doi.org/10.1073/pnas.2021860119 

pnas.org 

Only _y_ ( _t_ ) is predictable; the best predictions would be based on knowledge of _y_ ( _t_ = 0). One can then show that the best estimate of this quantity, given observations on the noisy _x_ ( _t_ ), is 

**==> picture [185 x 24] intentionally omitted <==**

with the same _K_ ( _t_ ) as in Eq. **43** . Thus, asking for the optimal prediction is the same as asking for the optimal separation of the predictable signal from the unpredictable noise (66). 

**B. Details for Fig. 2.** To generate Fig. 2, I start with some assumed correlation function _C_ ( _τ_ ) _≡⟨x_ ( _t_ ) _x_ ( _t_ + _τ_ ) _⟩_ , sampled at discrete times _t_ n = nΔ _t_ . This defines a correlation matrix _C_ nm = _C_ ( _t_ n _− t_ m), and then the kernel is the inverse of this matrix. One row of the matrix _K_ nm = ( _C[−]_[1] )nm provides a sampled version of the function _K_ ( _t − t[′]_ ), from which we can construct _K_ pf = _K_ ( _t_ + _t[′]_ ) from Eq. **12** . Note that _K_[˜] nm = _K_ ( _t_ n + _t_ m) is a symmetric matrix, and, if we normalize the functions _φn_ ( _t_ ), then the coefficients _a_ n in Eq. **13** are the eigenvalues of this matrix; these eigenvalues are plotted in Fig. 2. 

As an example that should illustrate a finite dimensionality, consider 

**==> picture [233 x 21] intentionally omitted <==**

**==> picture [18 x 9] intentionally omitted <==**

To be a bit more realistic, I add measurement noise with an amplitude of 10%, independent in each time bin, so that _C_ nm _→_ (1 _/_ 1.01) _C_ nm + (0.01 _/_ 1.01) _δ_ nm. Then the matrix _Knm_ is computed by inverting _C_ nm in a window of _T_ = 4, 000Δ _t_ . The symmetric _K_[˜] nm is constructed in windows of _T_ = 100Δ _t_ or _T_ = 1000Δ _t_ , and then diagonalized to find the eigenvalues. As an example that could illustrate infinite dimensionality, I consider the power-law correlation function in Eq. **17** , with _t_ 0 = Δ _t_ and _α_ = 1 _/_ 2, then follow the same procedure as with _C_ 3. 

**C. Interactions vs Latent Variables.** Models where the observed degrees of freedom depend on hidden or latent variables, but 

1. G. J. Stephens, B. Johnson-Kerner, W. Bialek, W. S. Ryu, Dimensionality and dynamics in the behavior of _C. elegans. PLOS Comput. Biol._ **4** , e1000028 (2008). 

2. K. Branson, A. A. Robie, J. Bender, P. Perona, M. H. Dickinson, High-throughput ethomics in large groups of _Drosophila. Nat. Methods_ **6** , 451–457 (2009). 

3. G. J. Berman, D. M. Choi, W. Bialek, J. W. Shaevitz, Mapping the stereotyped behaviour of freely moving fruit flies. _J. R. Soc. Interface_ **11** , 20146072 (2014). 

4. A. B. Wiltschko _et al._ , Mapping sub–second structure in mouse behavior. _Neuron_ **88** , 1121–1135 (2015). 

5. A. Mathis _et al._ , DeepLabCut: Markerless pose estimation of user-defined body parts with deep learning. _Nat. Neurosci._ **21** , 1281–1289 (2018). 

6. T. D. Pereira _et al._ , Fast animal pose estimation using deep neural networks. _Nat. Methods_ **16** , 117–125 (2019). 

7. S. R. Datta, D. J. Anderson, K. Branson, P. Perona, A. Leifer, Computational neuroethology: A call to action. _Neuron_ **104** , 11–24 (2019). 

8. M. W. Mathis, A. Mathis, Deep learning tools for the measurement of animal behavior in neuroscience. _Curr. Opin. Neurobiol._ **60** , 1–11 (2020). 

9. A. d’Avella, E. Bizzi, Low dimensionality of supraspinally induced force fields. _Proc. Natl. Acad. Sci. U.S.A._ **95** , 7711–7714 (1998). 

10. M. Santello, M. Flanders, J. F. Soechting, Postural hand synergies for tool use. _J. Neurosci._ **18** , 10105–10115 (1998). 

11. T. D. Sanger, Human arm movements described by a low-dimensional superposition of principal components. _J. Neurosci._ **20** , 1066–1072 (2000). 

12. L. C. Osborne, S. G. Lisberger, W. Bialek, A sensory source for motor variation. _Nature_ **437** , 412–416 (2005). 

13. G. J. Stephens, M. Bueno de Mesquita, W. S. Ryu, W. Bialek, Emergence of long timescales and stereotyped behaviors in _Caenorhabditis elegans. Proc. Natl. Acad. Sci. U.S.A._ **108** , 7286–7289 (2011). 

14. T. Ahamed, A. C. Costa, G. J. Stephens, Capturing the continuous complexity of behavior in _C elegans. Nat. Phys._ **17** , 275–283 (2021). 

15. N. H. Packard, J. P. Crutchfield, J. D. Farmer, R. S. Shaw, Geometry from a time series. _Phys. Rev. Lett._ **45** , 712–716 (1980). 

16. H. D. I. Abarbanel, R. Brown, J. J. Sidorowich, L. S. Tsimring, The analysis of observed chaotic data in physical systems. _Rev. Mod. Phys._ **65** , 1331–1392 (1993). 

17. S.Kato _et al._ ,Global brain dynamics embed the motor command sequence of _Caenorhabditis elegans. Cell_ **163** , 656–669 (2015). 

not directly on one another, are sometimes set in opposition to statistical physics models, where it is more natural to think about direct interactions. But, as explained also in the supplementary material of ref. 67, this dichotomy is incorrect. In fact, interacting models can be rewritten as models where individual element responds independently to some hidden or latent variables. As an example, the maximum entropy model in Eq. **21** can be rewritten exactly as a model in which the behavioral state at time _t_ depends only on some internal variable _x_ ( _t_ ), 

**==> picture [235 x 55] intentionally omitted <==**

and the distribution of the internal variable is 

**==> picture [255 x 51] intentionally omitted <==**

where _K_ ( _t_ ) is the matrix inverse of the function _J_ ( _t_ ), 

**==> picture [191 x 23] intentionally omitted <==**

**ACKNOWLEDGMENTS.** This paper is based, in part, on a presentation at the Physics of Behavior Virtual Workshop (30 April 2020), organized by G. J. Berman and G. J. Stephens. Videos are available at https://www.youtube. com/watch?v=xSwWAgp2VdU. My sincere thanks go to Gordon, Greg, and all my fellow panelists for this wonderful event, especially in such difficult times. Thanks go to V. Alba, G. J. Berman, X. Chen, A. Frishman, K. Krishnamurthy, A. M. Leifer, C. W. Lynn, S. E. Palmer, J. W. Shaevitz, and G. J. Stephens for many helpful discussions. This work was supported, in part, by the NSF through the Center for the Physics of Biological Function (Award PHY-1734030) and Grant PHY-1607612, and by the NIH (Grant NS104889). 

18. A. L. A. Nichols, T. Eichler, R. Latham, M. Zimmer, A global brain state underlies _C. elegans_ sleep behavior. _Science_ **356** , eaam6851 (2017). 

19. B. M. Yu _et al._ , Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity. _J. Neurophysiol._ **102** , 614–635 (2009). 

20. J. A. Gallego, M. G. Perich, L. E. Miller, S. A. Solla, Neural manifolds for the control of movement. _Neuron_ **94** , 978–984 (2017). 

21. J. J. Hopfield, Kinetic proofreading: A new mechanism for reducing errors in biosynthetic processes requiring high specificity. _Proc. Natl. Acad. Sci. U.S.A._ **71** , 4135–4139 (1974). 

22. J. Ninio, Kinetic amplification of enzyme discrimination. _Biochimie_ **57** , 587–595 (1975). 

23. D. M. Green, J. A. Swets, _Signal Detection Theory and Psychophysics_ (Wiley, New York, 1966). 

24. M. A. Bouman, “History and present status of quantum theory in vision” in _Sensory Communication_ , W. Rosenblith, Ed. (MIT Press, Cambridge, MA, 1961), pp. 377–401. 

25. X. I. I. Lord Rayleigh, On our perception of sound direction. _Philos. Mag. Series 6_ **13** , 214–232 (1907). 

26. K. von Frisch, Decoding the language of the bee. _Science_ **185** , 663–668 (1974). 

27. M.Giurfa,M.G.de Brito Sanchez,Black lives matter: Revisiting Charles Henry Turner’s experiments on honey bee color vision. _Curr. Biol._ **30** , R1235–R1239 (2020). 

28. J. L. Gould, _Ethology: The Mechanisms and Evolution of Behavior_ (W. W. Norton, New York, 1982). 

29. S. Hecht, S. Shlaer, M. H. Pirenne, Energy, quanta and vision. _J. Gen. Physiol._ **25** , 819–840 (1942). 

30. W. Bialek, _Biophysics: Searching for Principles_ (Princeton University Press, Princeton, NJ, 2012). 

31. J. L. Lawson, G. E. Uhlenbeck, _Threshold Signals_ (MIT Radiation Laboratory Series, McGraw–Hill, New York, 1950), vol. 24. 

32. A. H. Sturtevant, The linear arrangement of six sex–linked factors in _Drosophila_ , as shown by their mode of association. _J. Exp. Zool._ **14** , 43–59 (1913). 

33. A. L. Hodgkin, A. F. Huxley, A quantitative description of membrane current and its application to conduction and excitation in nerve. _J. Physiol._ **117** , 500–544 (1952). 

34. P. Fatt, B. Katz, Spontaneous subthreshold activity at motor nerve endings. _J. Physiol._ **117** , 109–128 (1952). 

35. G. Zweig, “Origins of the quark model” in _Proceedings of the Fourth International Conference on Baryon Resonances_ , N. Isgur, Ed. (University of Toronto, 1980), pp. 439–479. 

36. G. Zweig, Memories of Murray and the quark model. _Int. J. Mod. Phys. A_ **25** , 3863–3877 (2010). 

37. G. Zweig, Concrete quarks: The beginning of the end. _EPJ Web Conf._ **71** , 00146 (2014). 

38. B. W. Brunton, M. M. Botvinick, C. D. Brody, Rats and humans can optimally accumulate evidence for decision-making. _Science_ **340** , 95–98 (2013). 

https://doi.org/10.1073/pnas.2021860119 **7 of 8** 

**PNAS** 2022 Vol. 119 No. 18 e2021860119 

39. M. Potters, J.-P. Bouchaid, _A First Course in Random Matrix Theory for Physicists, Engineers and Data Scientists_ (Cambridge University Press, Cambridge, 2020). 

40. H. C. Berg, D. A. Brown, Chemotaxis in _Escherichia coli_ analysed by three-dimensional tracking. _Nature_ **239** , 500–504 (1972). 

41. C. J. Thompson, _Mathematical Statistical Mechanics_ (Princeton University Press, Princeton, NJ, 1972). 

42. E. T. Jaynes, Information theory and statistical mechanics. _Phys. Rev._ **106** , 620–630 (1957). 

43. P.D.Dixit _et al._ ,Perspective: Maximum caliber is a general variational principle for dynamical systems. _J. Chem. Phys._ **148** , 010901 (2018). 

44. W. Bialek, R. Ranganathan, Rediscovering the power of pairwise interactions. _arXiv_ [Preprint] (2007). https://doi.org/10.48550/arXiv.0712.4397. 

45. M. Weigt, R. A. White, H. Szurmant, J. A. Hoch, T. Hwa, Identification of direct residue contacts in protein–protein interaction by message passing. _Proc. Natl. Acad. Sci. U.S.A._ **106** , 67–72 (2009). 

46. D. S. Marks _et al._ , Protein 3D structure computed from evolutionary sequence variation. _PLoS One_ **6** , e28766 (2011). 

47. E. Schneidman, M. J. Berry 2nd, R. Segev, W. Bialek, Weak pairwise correlations imply strongly correlated network states in a neural population. _Nature_ **440** , 1007–1012 (2006). 

48. J. Shlens _et al._ , The structure of large-scale synchronized firing in primate retina. _J. Neurosci._ **29** , 5022–5031 (2009). 

49. E. Granot-Atedgi, G. Tkaˇcik, R. Segev, E. Schneidman, Stimulus-dependent maximum entropy models of neural population codes. _PLOS Comput. Biol._ **9** , e1002922 (2013). 

50. G. Tkaˇcik _et al._ , Searching for collective behavior in a large network of sensory neurons. _PLOS Comput. Biol._ **10** , e1003408 (2014). 

51. L. Meshulam, J. L. Gauthier, C. D. Brody, D. W. Tank, W. Bialek, Collective behavior of place and non-place neurons in the hippocampal network. _Neuron_ **96** , 1178–1191.e4 (2017). 

52. W. Bialek _et al._ , Statistical mechanics for natural flocks of birds. _Proc. Natl. Acad. Sci. U.S.A._ **109** , 4786–4791 (2012). 

53. W. Bialek _et al._ , Social interactions dominate speed control in poising natural flocks near criticality. _Proc. Natl. Acad. Sci. U.S.A._ **111** , 7212–7217 (2014). 

54. T. Mora, S. Deny, O. Marre, Dynamical criticality in the collective activity of a population of retinal neurons. _Phys. Rev. Lett._ **114** , 078105 (2015). 

55. A. Cavagna _et al._ , Dynamical maximum entropy approach to flocking. _Phys. Rev. E Stat. Nonlin. Soft Matter Phys._ **89** , 042707 (2014). 

56. T. Mora _et al._ , Local equilibrium in bird flocks. _Nat. Phys._ **12** , 1153–1157 (2016). 

57. F. Ferretti, V. Chardes, T. Mora, A. M. Walczak, I. Giardina, Building general Langevin models from discrete data sets. _Phys. Rev. X_ **10** , 031018 (2020). 

58. J. Burg, “ _Maximum entropy spectral analysis_ ,” PhD dissertation, Stanford University, Stanford, CA (1975). 

59. D. Ruelle, Statistical mechanics of a one-dimensional lattice gas. _Commun. Math. Phys._ **9** , 267–278 (1968). 

60. F. J. Dyson, Existence of a phase-transition in a one-dimensional Ising ferromagnet. _Commun. Math. Phys._ **12** , 91–107 (1969). 

61. G. Yuval, P. W. Anderson, Exact results for the Kondo problem: One-body theory and extension to finite temperature. _Phys Rev B_ **1** , 1522–1528 (1970). 

62. G. Yuval, P. W. Anderson, D. R. Hamman, Exact results for the Kondo problem. II. Scaling theory, qualitatively correct solution, and some new results on one-dimensional classical statistical models. _Phys Rev B_ **1** , 4464–4473 (1970). 

63. V. Alba, G. J. Berman, W. Bialek, J. W. Shaevitz, Exploring a strongly non-Markovian animal behavior. _arXiv_ [Preprint] (2020). 

64. W. Bialek, I. Nemenman, N. Tishby, Predictability, complexity, and learning. _Neural Comput._ **13** , 2409–2463 (2001). 

65. D. Ruelle, Deterministic chaos: The science and the fiction. _Proc. R. Soc. Lond. A Math. Phys. Sci._ **427** , 241–248 (1990). 

66. W. Bialek, R. R. de Ruyter van Steveninck, N. Tishby, Efficient representation as a design principle for neural coding and computation. _arXiv_ [Preprint] (2007). https://doi.org/10.48550/arXiv.2012.15681. 

67. G. Tkaˇcik _et al._ , Thermodynamics and signatures of criticality in a network of neurons. _Proc. Natl. Acad. Sci. U.S.A._ **112** , 11508–11513 (2015). 

**8 of 8** https://doi.org/10.1073/pnas.2021860119 

pnas.org 

