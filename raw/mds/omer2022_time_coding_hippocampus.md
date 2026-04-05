## **nature neuroscience** 

## **Article** 

https://doi.org/10.1038/s41593-022-01212-4 

## **Hippocampal spatial representations exhibit a hyperbolic geometry that expands with experience** 

Received: 21 April 2021 **Huanqiu Zhang[1,2] , P. Dylan Rich[3] , Albert K. Lee[4] & Tatyana O. Sharpee[1,2]** Accepted: 24 October 2022 Published online: 29 December 2022 Daily experience suggests that we perceive distances near us linearly. However, the actual geometry of spatial representation in the brain is Check for updates unknown. Here we report that neurons in the CA1 region of rat hippocampus that mediate spatial perception represent space according to a non-linear hyperbolic geometry. This geometry uses an exponential scale and yields greater positional information than a linear scale. We found that the size of the representation matches the optimal predictions for the number of CA1 neurons. The representations also dynamically expanded proportional to the logarithm of time that the animal spent exploring the environment, in correspondence with the maximal mutual information that can be received. The dynamic changes tracked even small variations due to changes in the running speed of the animal. These results demonstrate how neural circuits achieve efficient representations using dynamic hyperbolic geometry. 

Many aspects of our daily lives can be described using hierarchical systems. As we decide how to spend an afternoon, we may choose to read a book in a coffee shop or go to a shopping mall, which gives rise to a set of new questions: what coffee, which store and so forth, instantiating a decision tree[1][,][2] . Spatial navigation provides an example of decision-making in which hierarchical planning is useful[3] . Hierarchical organization in networks can provide several advantages, including achieving maximally informative representation of input signals[4] and efficient routing of signals in cases where network links are subject to change[5] . The latter property is especially useful for neural networks where connections between neurons change over time. However, to realize these advantages, the networks should be organized hierarchically in such a way as to follow a hidden hyperbolic geometry[5] . Unlike Euclidean geometry, hyperbolic geometry is negatively curved. This results in an exponential expansion of volume with the distance from the center, perceptual compression of large distances and distortions in the shortest distance paths between points, which now curve toward the representation center (Fig. 1a)[6] . Thus, hyperbolic organization would go against the everyday intuition that the brain represents distances around us linearly. 

We investigated whether hyperbolic geometry underlies neural networks by analyzing responses of sets of neurons from the dorsal CA1 region of the hippocampus. This region is considered essential for spatial representation[7][–][9] and trajectory planning[10] . CA1 neurons respond at specific spatial locations, termed place fields[11] . We will first illustrate the main idea by describing how neurons can be organized into a hierarchical tree-like network using a simplified picture where each neuron has only one place field in an environment. We will then follow up with analyses that take into account the presence of multiple place fields per neuron[12] . 

## **Results** 

## **Geometry of neural representation in CA1** 

The idea that hyperbolic geometry potentially underlies the neural representation of space follows from the construction illustrated in Fig. 1b. Each point in the two-dimensional (2D) plane represents an abstract neural response property, and a disk represents the collection of all the properties for one neuron in CA1. The more two disks overlap, the more similar the response properties of the corresponding two neurons are and, thus, the higher their response correlation. 

> 1Neurosciences Graduate Program, University of California, San Diego, La Jolla, CA, USA. 2Computational Neurobiology Laboratory, Salk Institute for Biological Studies, La Jolla, CA, USA.[3] Princeton Neuroscience Institute, Princeton University, Princeton, NJ, USA.[4] Howard Hughes Medical Institute, Janelia Research Campus, Ashburn, VA, USA. e-mail: sharpee@salk.edu 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**131** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [396 x 292] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>c d<br>3 40<br>Exponential fit 4<br>3 log( N<br>2 2<br>1<br>20<br>0<br>1 –1<br>–2<br>0 1 2<br>0 0<br>0 10 20 30 40 50 0 1 2 3<br>Position on the linear track (m) Field size (m)<br>N fields<br>Field size (m) ln (N fields)<br>**----- End of picture text -----**<br>


**==> picture [193 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
d<br>40<br>Exponential fit 4<br>3 log( N ) = –1.98 × +  c<br>2<br>1<br>20<br>0<br>–1<br>–2<br>0 1 2 3<br>0<br>50 0 1 2 3<br>Field size (m)<br>N fields<br>ln (N fields)<br>**----- End of picture text -----**<br>


**Fig. 1 | Construction of hierarchical organization of place cell responses that reflects underlying hyperbolic geometry. a** , A Poincaré disk model of 2D hyperbolic geometry is shown for visualization of its similarity to a tree structure. Each curve represents the geodesic between the two connected points, and all triangles have the same size. **b** , Illustration of the construction of hierarchical representation from neuronal response properties. The tree structure does not have to be perfect to allow for mapping onto a hyperbolic geometry[14] . Some loops can be present (dashed lines) due to partial overlap between 

disks of neurons from different orders in the hierarchy. **c** , Place field size versus location of 264 place fields from 63 putative pyramidal cells from dorsal CA1 of a rat running on a 48-m-long linear track (Fig. 3b and Supplementary Fig. 1)[20] . **d** , Histogram of place field sizes shown in **c** . Gray line shows the maximum likelihood exponential fit. _P_ value of χ[2] GOF test is 0.851 (χ[2] = 5.56 and d.f. = 10). Inset shows the same plot with log-scale on the _y_ axis. The straight line shows the least-squares linear regression with slope forced to be the exponent of the exponential fit. 

We now assign neurons that have larger disks in the plane to higher positions within the hierarchy (quantified by the _z_ coordinate in the three-dimensional (3D) space) compared to neurons with smaller disks. The _x,y_ coordinates are taken directly as the center positions of their disks. A link from a higher-to-lower-tier neuron is made if the larger disk contains (at least partially) the smaller disk. The resulting construction generates an approximate tree-like structure. The tree-like structure can, in turn, be viewed as a discrete mesh over the underlying hyperbolic geometry[13][,][14] . The leaves of the tree correspond to peripheral points, whereas roots of the tree correspond to positions closer to the origin of the hyperbolic geometry (Fig. 1a). We note that, in general, the plane can be of any dimension and is drawn here as 2D mainly for illustrative purposes. In the simplified case of each neuron having only one place field, the plane can be interpreted as physical space and the disks as being the place fields of the neurons. In this setting, the distribution of one-dimensional (1D) place field sizes should follow approximately an exponential distribution: 

**==> picture [187 x 21] intentionally omitted <==**

where _p_ ( _s_ ) is the probability density of place field sizes, and _s_ max is the maximal place field size. The exponent in this distribution is the curvature _ζ_ of the representation (or, equivalently, the size of the hyperbolic geometry with unit curvature). In Fig. 1c,d, we indeed find that an exponential distribution fits the distribution of place field sizes well 

( _P_ = 0.851, χ[2] goodness-of-fit (GOF) test). A caveat with this analysis, however, is that, strictly speaking, it applies to the case where each neuron has one place field, whereas multiple place fields are observed per neuron in moderately large environments[12] . 

To quantitatively test whether hyperbolic geometry underlies neural representation in CA1, we employed a statistical tool from topology that does not directly rely on the computation of place fields. Instead, the method defines distances between neurons based on the pairwise correlations between their activities. This pairwise correlation is intuitively reflective of the degree of place field overlap between two neurons[15] and is capable of accounting for neurons with multiple fields. These distances are then analyzed to determine if they produce the same topological signatures as points sampled from different geometries[16][,][17] . The topological signatures used by the methods are the so-called Betti curves[16] . These are obtained by varying the threshold for what constitutes a significant connection between neurons and counting cycles in the thereby generated graph (Fig. 2a–c). One of the advantages of this method is that, because it considers all possible values of the threshold, it is invariant under any non-linear monotonic transformations of the correlation values. Similar topological methods based on persistent homology have been used to study manifold structures of population responses in the head direction and grid cell systems[18][,][19] . 

We first applied this method to recordings of putative active pyramidal (average firing rate between 0.1 Hz and 7 Hz) cells ( _n_ = 113, average firing rate ± s.d. = 0.42 ± 0.35 Hz) from dorsal CA1 of three rats 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**132** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [440 x 368] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b Thre1 Thre2 c<br>10 1 1 Edge density = 0.33 Edge density = 0.40<br>1 2  (0,0,0)  (1,0,0)<br>3 1 1<br>2 4 6 2 6 2<br>3 thre2thre3thre4thre1 65 0 5 3 5 3<br>Thre3 Thre4<br>4 1 4 4<br>2<br>5 3 Edge density = 0.47 Edge density = 0.53<br>4  (1,0,0)  (0,0,0)<br>6 5 1 1<br>0 6 6 2 6 2<br>1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6<br>Neuron index 5 3 5 3<br>4 4<br>d Hyperbolic geometry e Euclidean geometry f Shuffled<br>40 4 40 4 100 10<br>6 6 4<br>30 42 2 30 42 2 80 5 2<br>0 0 0 0 0 0<br>β 1 β 2 β 3 β 1 β 2 β 3 β 1 β 2 β 3 β 1 β 2 β 3 60 β 1 β 2 β 3 β 1 β 2 β 3<br>20 20<br>40<br>10 10<br>20<br>0 0 0<br>0 0.2 0.4 0.6 0 0.2 0.4 0.6 0 0.2 0.4 0.6<br>Edge density Edge density Edge density<br>g h i<br>Hyperbolic geometry Euclidean geometry  Shuffled<br>40 4 40 4 10<br>6 6 15<br>4 2 4 2 150 10 5<br>30 2 30 2 5<br>0 0 0 0 0 0<br>β 1 β 2 β 3 β 1 β 2 β 3 β 1 β 2 β 3 β 1 β 2 β 3 100 β 1 β 2 β 3 β 1 β 2 β 3<br>20 20<br>10 10 50<br>0 0 0<br>0 0.2 0.4 0.6 0 0.2 0.4 0.6 0 0.2 0.4 0.6<br>Edge density Edge density Edge density<br>Thresholded<br>Neuron index cross corr.<br>L1 distances L1 distances L1 distances<br>Int betti values Int betti values Int betti values<br># cycles # cycles # cycles<br>Linear track<br>Int betti values L1 distances Int betti values L1 distances Int betti values L1  distances<br>Square box # cycles # cycles # cycles<br>**----- End of picture text -----**<br>


**Fig. 2 | Neuronal activity in CA1 is topologically consistent with a 3D hyperbolic but not a Euclidean geometry. a** – **c** , Illustration of the topological algorithm on an example correlation matrix. **a** , Example pairwise correlation matrix for six neurons. **b** , Correlation matrices after various thresholding. The threshold gradually decreases from top-left to bottom-right such that correlation between more pairs of neurons becomes significant. **c** , An edge connecting two nodes is formed when the corresponding entry in **b** is non-zero. Edge density measures the fraction of edges connected out of the total number possible. The numbers in each set of parentheses represent the number of 1D, 2D and 3D cycles (or holes) in the corresponding graph, respectively (note that the dimensionality of the cycles is not directly related to the dimensionality of the underlying geometry). This example demonstrates how a 1D cycle appears due to new edges being formed and then disappears because of formation of cliques. The number of such cycles across the entire range of edge densities 

(or thresholds) gives the Betti curves. **d** , **g** , Experimental Betti curves (dashed) for 1D (red), 2D (green) and 3D (blue) cycles are statistically indistinguishable from those generated by sampling ( _n_ = 300 replicates) from 3D hyperbolic geometry (solid line and shading indicate mean ± s.d.) for linear track exploration with radius = 15.5 ( **d** ) and square box exploration with radius = 11.5 ( **g** ). Insets show comparison of the curve integrals and the L1 distances from model Betti curves against those of the experimental Betti curves. Boxes show the model interquartile range. Upper and lower whiskers encompass 95% of the model range. Black lines indicate experimental values. **e** , **h** , Betti curves generated from 3D Euclidean geometry are statistically different from the experimental Betti curves in both linear ( **e** ) and square ( **h** ) environments. **f** , **i** , After shuffling spike trains, Betti curves generated from 3D hyperbolic geometry are no longer consistent with the experimental Betti curves in both linear ( **f** ) and square ( **i** ) environments. Session ID for square box: ec014.215. 

(one session per animal) running on a novel 48-m-long linear track[20] . We found that experimental Betti curves were not consistent with samples from a Euclidean geometry but were consistent with a 3D hyperbolic geometry (Fig. 2d,e). Statistical analyses showed that 3D hyperbolic geometry provided the overall best fit compared to other dimensionalities of the hyperbolic geometry (Extended Data Fig. 1; two-way ANOVA across sessions: _F_ = 7,924.61, _P_ < 10[−8] ; Tukey’s post hoc test: _P_ < 10[−8] for all pairwise comparisons between 3D fits and fits from other dimensions). Similar low dimensionality of population activity in dorsal hippocampus has been reported with other manifold inference methods[21][,][22] . We note that three dimensions is also the expected dimensionality for a hierarchical set of 2D place fields according to the construction illustrated in Fig. 1b. The pairwise correlations were computed separately for each experimental 

session. Different sessions yielded latent 3D hyperbolic geometries of different radii (15.5, 15 and 13; see Methods and Extended Data Fig. 2a on how hyperbolic radius is estimated for each session). The same conclusions held for datasets of dorsal CA1 neurons recorded when rats explored 2.5-m linear tracks and 1.8 × 1.8-m square boxes for longer durations. We tested two (total number of putative active pyramidal neurons is 77, average firing rate ± s.d. = 0.92 ± 0.75 Hz) and seven ( _n_ = 274, average firing rate ± s.d. = 0.68 ± 0.61 Hz) publicly available datasets, respectively, for the above two environments, selecting recording sessions that had more than 50 neurons (not necessarily active) recorded simultaneously[23][,][24] . In each case, a 3D hyperbolic geometry produced Betti curves that matched those computed from data. In Fig. 2, we show one example analysis for each environment type (linear or square), and the rest of the datasets are 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**133** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

## **a** 

**==> picture [434 x 502] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 20<br>16 16<br>12 12<br>8 8<br>0 80 160 240 320 400 480 560 640 40 80 160 320 640<br>Exploration time (min) log-scale<br>b c<br>1 Section1 Section2 Section3 Section4<br>2 Epoch1<br>Epoch2<br>4 Epoch3<br>3<br>Epoch4<br>d e<br>4 4<br>3<br>3<br>3<br>2<br>2<br>2<br>1<br>1<br>1<br>0 0<br>0 1 2 3 4 1.5 2 2.5 3 –3 –2 –1 0 1 2<br>Temporal familiarity (s) log-scale In(first-pass speed (m/s))<br>f g h<br>0.8 3.5<br>0.7 3 40<br>2.5<br>0.6<br>20<br>2<br>0.5<br>1.5<br>0<br>0.4<br>1<br>0.3 0.5 –20<br>–0.5 0 0.5 1 1.5 2 –0.5 0 0.5 1 1.5 2 20 40 80 160<br>∆Entropy ∆Entropy Exploration time (s)<br>with unit curvature<br>Radius of the hyperbolic geometry<br>Field size (m)<br>Hyperbolic radius Hyperbolic radius<br>Speed (m/s)<br>Hyperbolic radius<br>% increase of hyperbolic radius<br>**----- End of picture text -----**<br>


**Fig. 3 | Hyperbolic geometry of neural representation expands with the logarithm of exploration time. a** , Radius of the hyperbolic representation of square box is estimated using topological analysis. Dots represent median estimates, and lines represent 95% confidence interval. Dashed black line is the least-squares regression of data with log-scale on the _x_ axis ( _r_ = 0.85, _P_ = 3 × 10[−6] ). Dashed gray line shows the least-squares fit of Eq. (2). **b** , Scale drawing of the 48-m linear track. The start of each track section is marked by numbers. **c** , Schematic of the experimental paradigm. During the first epoch, only the first section of the track is available to an animal. The linear track is progressively extended after each epoch. Total track length in the four epochs was 3, 10, 22 and 48 m. Black lines indicate periods when the animal is exposed to the corresponding section for the first time. Red lines indicate non-first exposures. 

**d** , Hyperbolic radius grows with temporal familiarity with the segments. Dashed black lines show the least-squares regression of data with log-scale on the _x_ axis ( _r_ = 0.50, _P_ = 0.0003), and dashed gray lines show the least-squares fit of Eq. (2). **e** , Field sizes increase with the animal’s first-pass speed through the field ( _r_ = 0.35, _P_ = 9 × 10[−21] ). Different symbols indicate fields of different animals. **f** , Animals run slower in segments of higher entropy ( _r_ = −0.56, _P_ = 4 × 10[−5] ). **g** , Radius of representation increases with entropy of the track ( _r_ = 0.42, _P_ = 0.004). **h** , During subsequent exposures (red lines in **c** ), hyperbolic radius increases with familiarity ( _r_ = 0.62, _P_ = 0.0057). Symbols represent different animals, whose least familiar points are used as normalization. Each data point is an animal in one epoch-section period. 

shown in Extended Data Figs. 2, 3 and 4. The fitting statistics and the hyperbolic radii estimated for all sessions are summarized in Supplementary Table 1. 

As a control, we verified that shuffled spike trains (spike times of individual neurons were shifted by the same amount to preserve firing statistics) produced correlation matrices that were not consistent with 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**134** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [521 x 307] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>d<br>0.4<br>Data<br>32 y = be [-cx]  fit 0.3<br>0.3<br>28<br>0.2<br>0.2<br>24<br>0.1 0.1<br>20<br>6 7 8 0 100 200 300 400 500 600 10 12 14 16 s  = ( x,y ) σ2 σ1<br>Average # spikes used Time (min) Hyperbolic radius<br>e f N  = 51,200<br>Poisson<br>Exponential 400 25,600 ( r1,...,rN ) exp(– ζσ )<br>7 Uniform<br>10<br>Lognormal 12,800 σ<br>6,400<br>g 17<br>106 300 3,200<br>1,600<br>13<br>800 Data<br>105 200<br>400<br>9<br>200<br>104 100 100<br>N  = 50 5<br>100 400 1,600 6,400 25,600 1 2 4 8 16 32 100 400 1,600 6,400 25,600 102,400<br>N  neurons simulated Hyperbolic radius N  neurons simulated<br>Simulations<br>Estimate of c Estimate of c<br>Median decoding error (cm)<br>)( pσ<br>Magnitude of Fisher info<br>Optimal radius<br>Magnitude of Fisher info per neuron<br>**----- End of picture text -----**<br>


**Fig. 4 | Increase in size of the hyperbolic representation results in higher accuracy in spatial localization. a** , A Bayesian decoder with integration time window of _δt_ = 500 ms is used for different number of subsampled neurons for each session (Methods). An example relationship is shown here, which is fitted with an exponential function of the form indicated to determine the value of _c_ for each session. **b** , Estimates of _c_ increase over time. Error bar represents the standard error of the estimate. Dashed gray line shows the least-squares fit with log-scale on the _x_ axis ( _r_ = 0.86, _P_ = 10[−6] ). **c** , Estimates of _c_ correlate significantly with hyperbolic radius ( _r_ = 0.70, _P_ = 0.0007). Black line shows the least-squares fit. Jitter has been added to _x_ values to improve visualization. **d** , Schematic of the modeling framework for computing Fisher information for how accurately an animal’s position can be decoded from neural responses: place fields are modeled as 2D Gaussian functions[47] , and neural response has Poisson variability[48] . **e** , Networks with exponentially distributed place field size 

provide more information about the animal’s position than networks where place field size is uniformly distributed (with the same mean size as the exponential distribution) or log-normally distributed (with the same mean and variance as the exponential distribution). _P_ < 0.001 for equal means between information from exponential and uniform distributions, or exponential and log-normal distributions, at all number of neurons, using an unpaired two-sample _t_ -test. **f** , Fisher information per neuron for networks of different sizes and of hyperbolic representations of different radii. **g** , Optimal hyperbolic radius depends logarithmically on the number of neurons in a network (with dashed portion showing extrapolation of the relationship). The extrapolated value for the full CA1 circuit agrees with median values (upper and lower endpoints of the cross) of hyperbolic radius determined in the last exposure of the square box in Fig. 3a. Left and right endpoints indicate range of experimental values 320,000 × 30% and 490,000 × 40%, respectively, for the number of active CA1 neurons. 

a 3D hyperbolic geometry (Fig. 2f,i). Also, restricting our analyses to subsets of neurons with high spatial information yields the same results that 3D hyperbolic geometry, but not Euclidean geometry, underlies the neural representation (Extended Data Fig. 5). We note that the hierarchical organization we study works in addition to those observed across larger extents of the hippocampus and the entorhinal cortex[25][–][27] . This is because the variation of place field sizes determined from our data was not significantly correlated with the anatomical positions of the neurons recorded within the hippocampus (Extended Data Fig. 6), which, in our experiments, are largely confined to dorsal CA1, comprising only a fraction of the span of dorsal–ventral axis that was recorded in the above references[25][,][27] . These analyses demonstrate that neural activity in CA1 consistently conforms to a 3D hyperbolic geometry, with variations in the size of the hyperbolic geometry across environments, with values that range within 10.5−15.5 (in units of inverse curvature). 

## **Hyperbolic representation expands with experience and information acquired** 

The environments in which these hyperbolic representations were observed differed in shape (linear versus square), size and also in 

the amount of time that the animals spent exploring them. First, we verified that the size of the hyperbolic representation was similar for data collected from linear and square environments, as long as the animals initially spent similar amounts of time in them (Extended Data Fig. 7a). Next, we investigated the effect of exploration time on the size of the resulting hyperbolic representation of the same environment that was initially novel to the animal. We found that the size of the hyperbolic representation was larger when the animal was more familiar with the environment, using the above topological method. The size increased with the logarithm of time that the animal had to explore it (Fig. 3a and Extended Data Fig. 7b,c). This is interesting because the logarithm of time is approximately proportional to the maximal amount of information the animal can acquire from the novel environment (considering an animal receiving a distinct combination of stimuli at each time step)[28] , with the exact relationship given by: 

**==> picture [187 x 19] intentionally omitted <==**

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**135** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [181 x 337] intentionally omitted <==**

**----- Start of picture text -----**<br>
a<br>120<br>N  = 51,200<br>25,600<br>80<br>12,800<br>6,400<br>3,200<br>40 1,600<br>800<br>400<br>200<br>100<br>0 50<br>1 2 4 8 16 32 64<br>Hyperbolic radius<br>b<br>17<br>13<br>Data<br>9<br>5<br>100 1,600 25,600 409,600<br>N  neurons simulated<br>Simulations<br>Magnitude of Fisher info per neuron<br>Optimal radius<br>**----- End of picture text -----**<br>


**Fig. 5 | Theoretically optimal representation radius is consistent with the experimental value when each cell can have potentially multiple place fields.** In this simulation, the statistics of number of place fields per cell are matched to the experimental values of sessions shown in Fig. 3 (mean = 0.98 and s.d. = 1.10, which determines the gamma distribution that, in general, describes number of place fields per cell[20] ), and the size of the environment is matched to the experimental value of 1.8 × 1.8 m. **a** , Fisher information per neuron for networks of different sizes and of hyperbolic representations of different radii. **b** , The extrapolated value for the full CA1 circuit agrees with median values of radius determined in the last exposure of Fig. 3. Same notation as in Fig. 4g, except left and right endpoints of the cross indicate range of experimental values 320,000 and 490,000, respectively, for the number of all CA1 neurons, as the gamma distribution is used to capture number of place fields for all neurons as opposed to only active neurons. 

where _t_ 0 is a constant that represents the product of sampling interval and the ratio between the effective signal _Sn_ and noise _Nn_ variances. In Fig. 3a, we show that this relationship accounts well for the expansion of the CA1 hyperbolic representations as the animal is exploring the environment. For these analyses, we sorted the datasets according to the number of times the animal had a chance to explore the square box; we also analyzed separately data from individual exposures (indicated by different colors in Fig. 3a) to the box in 20-min sections for their hyperbolic radii. We note that, although CA1 neural representations undergo substantial dynamic changes over these hour-long time scales of exposures across days[29][,][30] , the neural responses continued to be described by a 3D hyperbolic geometry with a systematic increase in its size. We verified that this was not due to changes in the animal’s locomotion and behavioral states; no significant correlation between representation size and parameters, such as the average running speed and active exploration time, was observed (Extended Data Fig. 8a). Excluding time periods with speed <5 cm s[−1] also do not change the 

results (Extended Data Fig. 8b). We also verified that time elapsed without exploration (that is, outside the environment) cannot account for the expansion of representation observed (Extended Data Fig. 8c). 

The same relationship between the size of the hyperbolic representation and exploration time was observed on shorter time scales, including the first seconds during initial exploration of a novel environment. For these analyses, we used the dataset from the 48-m-long linear track (Fig. 3b). The track was initially novel to the animals. In each epoch, an animal traversed the current total length of the available track 3–5 times. Between epochs, it was confined to the original start location while the track was extended (Fig. 3c). We first tested the relationship during initial formation of place fields by considering only periods when the animal explored the additional novel sections of the track introduced in each epoch (Fig. 3c, black lines). We estimated hyperbolic radii for each 1-m segment of the track by examining the distribution of place field sizes within it. In this situation, we are close to the one-field-per-neuron case for each 1-m segment (93.4% ± 6.6% place fields are from different neurons) and, thus, estimated the hyperbolic radii by examining the exponent of place field size distribution in Eq. (1) (Fig. 1d, arrow). We did not use the topological analysis here, because, with short recording duration, the method produces biased estimates of the radius, with larger bias for shorter recordings (Extended Data Fig. 9). We found that the hyperbolic radius increased with temporal familiarity with the environment (Fig. 3d). The temporal familiarity was calculated as the inverse of the mean speed (Methods). The same results were obtained when speed was computed for the initial traversal or across multiple traversals or when using a different segment length (Extended Data Fig. 10). Also, a significant positive correlation between field size and its first-pass speed was observed (Fig. 3e). Therefore, higher speed and, thus, less familiarity with the nearby environment produced larger place fields. This, in turn, led to a smaller hyperbolic radius or the exponent in Eq. (1). 

We also tested the relationship among the radius of the representation, the speed of the animal and the information content of the environment. The shape of the environment is a key aspect of spatial information that can be perceived by the animal. For a linear track, the shape is determined by its angles. In our experiment, some 1-m segments had more turns, whereas others were mostly straight (Fig. 3b). One can quantify the additional information provided by the changes in trajectory of the track by computing the probability distribution of the change in angle _δθ_ between segments and using the standard formula for entropy[31] . With this definition, straight segments have zero additional entropy, with larger values for more curved and varied segments. We found that animal speed was inversely related to the additional information (Fig. 3f), with lower speed in more informative segments. The more informative segments also generated representations with larger hyperbolic radius (Fig. 3g). However, the differences in the hyperbolic radius can be fully explained by differences in the time that the animal spent in a given segment. This is because, once controled for speed, representation size was no longer significantly correlated with additional information (linear partial correlation coefficient = 0.18, _P_ = 0.236). We then focused on subsequent exposures to sections of the track (Fig. 3c, red lines). Similarly to the above observations, we found that the radius of the representation continued to increase with additional familiarity using the same measure of hyperbolic radius (Fig. 3h). These analyses indicate that the neural representation maintains hyperbolic organization after experience-induced re-organization with systematic increases in the size of the hyperbolic geometry. 

## **Observed hyperbolic representation maximizes spatial information given the number of CA1 neurons** 

To quantify how well the CA1 neurons could support spatial localization, we computed Bayesian maximum likelihood decoder for the animal’s location based on neural responses from the square box datasets. To avoid the potential confound associated with differences in spike rates across sessions, we subsampled, for each session, subsets of neurons 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**136** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [440 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 3 4 Theorectical pdf 2.5 2.5<br>1 Fitted log-normal pdf<br>2.5 2<br>3 2<br>3<br>2 1.5<br>2 1.5<br>1<br>2 1.5<br>0 0 0.1 0.2 0.3 1 1 0.5<br>1 1 curve 1 010 [–2] 10 [–1] 10 [0] 8 curves 010 [–2] 10 [–1] 10 [0]<br>0.5<br>0.5<br>0 0 0<br>0 1 2 3 0 1 2 3 0 1 2 3<br>Place field size (m) Place field size (m) Place field size (m)<br>Prob. of<br>observation<br>Probability density Probability density Probability density<br>**----- End of picture text -----**<br>


**Fig. 6 | Illustration of observation of a log-normal distribution of place field sizes.** Random samples from each of eight different sinh distributions (left) are drawn. Suppressing the probability of observing small place fields according to a sigmoidal function (left inset) leads to a distribution that approximates log-normal (middle). The middle panel shows the resulting observed histogram for one sinh distribution. Inset shows log-scale on the _x_ axis. When sample size is not too large ( _n_ = 800 in this simulation), the histogram can be fitted by a 

log-normal distribution with _P_ = 0.07 (χ[2] GOF test, χ[2] = 11.66 and d.f. = 6). Black curve represents the theoretical density function, and gray line represents the fitted log-normal distribution. The right panel shows the results after pooling from eight distributions where an even better fit with log-normal can be obtained ( _P_ = 0.43, χ[2] GOF test, χ[2] = 4.87 and d.f. = 5) at a moderate sample size ( _n_ = 800 in this simulation). pdf, probability density function. 

**==> picture [105 x 19] intentionally omitted <==**

**----- Start of picture text -----**<br>
Radius increases with log( T )<br>log( T ) ∝ bits of info received<br>**----- End of picture text -----**<br>


**Fig. 7 | Schematic illustration of how increased hyperbolic radius affects neural representation of space.** As radius grows over time, exponential distribution of place field sizes shifts toward smaller place fields (Extended Data Fig. 7d) or larger depth in a discrete tree structure (Eq. 1), to improve spatial localization. 

resulting in different overall spike rates and estimated how much the median decoding error decreases with increasing the number of spikes used for decoding. The decoding error decreased exponentially with the number of spikes (Fig. 4a). The exponent _c_ in this case indicates how efficient an extra spike is in reducing decoding error. Similarly to the radius of hyperbolic representation, we found that _c_ increased consistently over time (Fig. 4b). Figure 4c shows that exponent _c_ also correlated significantly with hyperbolic radius. To establish a causal relationship between representation radius and accuracy of spatial localization, we computed the Fisher information, a measure of read-out accuracy[32][,][33] , for populations of model neurons with place field sizes distributed according to different distributions (Fig. 4d). In the one-field-per-neuron case, we found that populations of neurons whose place field sizes were exponentially distributed, as expected for a hidden hyperbolic geometry, provided more accurate spatial decoding compared to the cases of uniformly or log-normally distributed place field sizes (Fig. 4e and Supplementary Fig. 2). Furthermore, for a given network size, there was an optimal size of the hyperbolic representation that maximizes Fisher information (Fig. 4f). The optimal value is determined as a tradeoff between two factors. On the one hand, larger representations include exponentially more small place fields and have higher capacity to represent space. However, they also require more neurons for their sampling and can become undersampled if the number of neurons is limited. The interplay between these two factors determines the optimal size of the representation for a given number of neurons. The simulations indicate that the optimal representation size increases with the logarithm of the number of neurons (Fig. 4g). This theoretical prediction can be tested against data on the number of active neurons in the CA1 region. The CA1 region of rat hippocampus contains roughly 320,000–490,000 pyramidal neurons[34][,][35] with about 30–40% of neurons being active in any given environment[29][,][36][,][37] 

(Extended Data Fig. 7e). Extrapolating the theoretical curve in Fig. 4g to this number of neurons, we found a close match to the representation size extracted from the analysis of correlation in neural responses in square box (Fig. 3a). In any moderately large environment, however, individual CA1 neurons can have multiple place fields[12][,][20][,][38][,][39] . Therefore, we also simulated the case where each cell can have multiple place fields according to a gamma-Poisson model[20] with statistics matched to the experimental data, and we found that the same conclusions hold (Fig. 5). This match indicates that the hierarchical arrangement of neural responses is well-matched to the overall number of neurons and their propensities for forming fields. 

## **Exponential distribution of place field sizes** 

So far, we focused on using an exponential function to analyze the distribution of neural place fields, because this distribution connects with hyperbolic representations and makes it possible to infer its curvature. However, other skewed distributions, in particular the log-normal distributions, have similar properties at large values and have been shown to match neural data[40] . Therefore, it is worthwhile to discuss factors that distinguish and relate both model distributions to each other. First, it is important to note that these two distributions differ most for small place field sizes, and these are the place field sizes that are most affected by biases in the current experimental recording and place field determination methods. Very small place fields are often discarded by smoothing procedures used to estimate neural place fields or even by default (note their absence in Fig. 1c)[40] . Figure 6 presents simulations showing that this sampling bias alone can transform an exponential distribution of place field sizes into an almost log-normal one. Therefore, previous demonstrations of log-normal distributions of place field sizes do not necessarily argue against the presence of exponential distributions. Second, as we have observed, the curvature 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**137** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

of hyperbolic representations (or, equivalently, their radius relative to unit curvature) varies across environments depending on the animal exploration time (Fig. 3). Averaging of exponential distributions of place field sizes with different exponents will further bring the resultant distribution closer to the log-normal family of curves (Fig. 6, right panel). This effect will be even stronger when data collected from different animals and environments are pooled together as more different distributions are summed together. 

## **Discussion** 

Several previous studies described how place fields re-organize with experience[29][,][30][,][41][,][42] . Here we describe that these changes not only include the emergence of fine-grained place fields but also result in coordinated changes across the network. It turns out that the logarithmic growth of the hyperbolic radius _R_ ~ log( _T_ ) that we observe here can be explained by a simple mechanistic model where place fields of a small size appear as soon as the animal spends a certain minimal required time _t_ 0 within the field (Fig. 7). Because small place fields map to the edge of the hyperbolic geometry, their number _N_ increases exponentially with the radius _R_ . Thus, the hyperbolic representation will approximately reach radius _R_ once the total exploration time _T_ reaches _T_ = _Nt_ 0 ~ exp( _R_ ) _t_ 0, or: 

**==> picture [151 x 9] intentionally omitted <==**

as observed experimentally (Fig. 3). The logarithmic growth of _R_ with time in turn matches the entropy that can be acquired from the environment (Eq. (2)). These arguments demonstrate that it is possible to achieve efficient representations from the information theory point of view using simple mechanistic rules for the addition of small place fields (Eq. (3)). The constant _t_ 0 now acquires multiple interpretations. In the mechanistic model of place field addition and expansion of hyperbolic representation (Eq. (3)), _t_ 0 represents the minimal time required to form a place field. In the information acquisition formula, Eq. (2), _t_ 0 represents the temporal sampling interval. Being the only parameter in the information acquisition equation, _t_ 0 also determines the transition when the initially novel environment becomes familiar: during the initial exploration, the information and the hyperbolic radius both increase approximately linearly with time. For times much longer than _t_ 0, the linear increase changes over to a logarithmic one. The increase in the relative proportion of small place fields over time (Fig. 7 and Extended Data Fig. 7d) may also be achieved as a result of the overall decrease of firing rate in CA1 with familiarity[41][,][43] . 

The hyperbolic representation was recently demonstrated for the olfactory system[17][,][44] . However, those studies analyzed only natural olfactory stimuli[17][,][44] or human perceptual responses[17] . This left open the question of whether neural responses also have hyperbolic representation. We address this question here, not in the same sensory modality but for the more general hippocampal representation that interacts with many sensory modalities. 

Hyperbolic representation describes a specific instantiation of hierarchical organization that offers many functional advantages[45] . One particularly important advantage for neural circuits is that it allows effective communication within the network using only local knowledge of the network and in situations where network links are changing in time[5] . We show here that hyperbolic representations also support more accurate spatial localization (Figs. 4 and 5). Related to this, recent literature indicates the presence of multi-scale place fields within dorsal CA1, which could improve spatial decoding especially in large environments[38][,][39] . The presence of hyperbolic geometry could be further supported by hierarchical representation across broader scales in hippocampus and entorhinal cortex[25][–][27] . 

In addition to predictions for the spatial distribution of place field sizes, the hyperbolic representation also makes predictions for the temporal aspects of the neural code. The reason for this is that, within hyperbolic representations, addition is not commutative, meaning 

that the order in which vectors are added matters. For neural systems, this implies that the order in which spikes are received from different neurons should matter. A detailed investigation of these results comprises a promising direction for future research. 

To summarize, we have shown that organizing neural circuits to follow latent hyperbolic geometry makes it possible to implement coherent large-scale reorganization. For example, this could be achieved by adjusting neuronal thresholds to control place field sizes (Fig. 7 and Extended Data Fig. 7d). These changes allow a continuous increase in representational capacity (Figs. 4 and 5). As such, this type of organization might provide a general principle underlying large structural changes of neural representations to benefit communication between brain areas, as has been observed, for example, in the parietal cortex[46] . 

## **Online content** 

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41593-022-01212-4. 

## **References** 

1. Newell, A. _Unified Theories of Cognition_ (Harvard University Press, 1990). 

2. Sutton, R. S. & Barto, A. G. _Reinforcement Learning: An Introduction_ (MIT Press, 1998). 

3. Balaguer, J., Spiers, H., Hassabis, D. & Summerfield, C. Neural mechanisms of hierarchical planning in a virtual subway network. _Neuron_ **90** , 893–903 (2016). 

4. Cubero, R. J., Jo, J., Marsili, M., Roudi, Y. & Song, J. Statistical criticality arises in most informative representations. _J. Stat. Mech._ **2019** , 063402 (2019). 

5. Boguna, M., Papadopoulos, F. & Krioukov, D. Sustaining the internet with hyperbolic mapping. _Nat. Commun._ **1** , 62 (2010). 

6. Urdapilleta, E., Troiani, F., Stella, F. & Treves, A. Can rodents conceive hyperbolic spaces? _J. R. Soc. Interface_ **12** , 20141214 (2015). 

7. Scoville, W. B. & Milner, B. Loss of recent memory after bilateral hippocampal lesions. _J. Neurol. Neurosurg. Psychiatry_ **20** , 11–21 (1957). 

8. O’Keefe, J. & Nadel, L. _The Hippocampus as a Cognitive Map_ (Clarendon Press, 1978). 

9. O’Keefe, J., Burgess, N., Donnett, J. G., Jeffery, K. J. & Maguire, E. A. Place cells, navigational accuracy, and the human hippocampus. _Philos. Trans. R. Soc. Lond. Ser. B_ **353** , 1333–1340 (1998). 

10. Pfeiffer, B. E. & Foster, D. J. Hippocampal place-cell sequences depict future paths to remembered goals. _Nature_ **497** , 74–79 (2013). 

11. O’Keefe, J. & Dostrovsky, J. The hippocampus as a spatial map: preliminary evidence from unit activity in the freely-moving rat. _Brain Res._ **34** , 171–175 (1971). 

12. Fenton, A. A. et al. Unmasking the CA1 ensemble place code by exposures to small and large environments: more place cells and multiple, irregularly arranged, and expanded place fields in the larger space. _J. Neurosci._ **28** , 11250–11262 (2008). 

13. Krioukov, D., Papadopoulos, F., Kitsak, M., Vahdat, A. & Boguna, M. Hyperbolic geometry of complex networks. _Phys. Rev. E_ **82** , 036106 (2010). 

14. Gromov, M. _Metric Structures for Riemannian and Non-Riemannian Spaces_ (Birkhauser, 2007). 

15. Hampson, R. E., Byrd, D. R., Konstantopoulos, J. K., Bunn, T. & Deadwyler, S. A. Hippocampal place fields: relationship between degree of field overlap and cross-correlations within ensembles of hippocampal neurons. _Hippocampus_ **6** , 281–293 (1996). 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**138** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

16. Giusti, C., Pastalkova, E., Curto, C. & Itskov, V. Clique topology reveals intrinsic geometric structure in neural correlations. _Proc. Natl Acad. Sci. USA_ **112** , 13455–13460 (2015). 

17. Zhou, Y., Smith, B. H. & Sharpee, T. O. Hyperbolic geometry of the olfactory space. _Sci. Adv._ **4** , eaaq1458 (2018). 

18. Chaudhuri, R., Gerc¸ek, B., Pandey, B., Peyrache, A. & Fiete, I. The intrinsic attractor manifold and population dynamics of a canonical cognitive circuit across waking and sleep. _Nat. Neurosci._ **22** , 1512–1520 (2019). 

19. Gardner, R. J. et al. Toroidal topology of population activity in grid cells. _Nature_ **602** , 123–128 (2022). 

20. Rich, P. D., Liaw, H.-P. & Lee, A. K. Large environments reveal the statistical structure governing hippocampal representations. _Science_ **345** , 814–817 (2014). 

21. Low, R. J., Lewallen, S., Aronov, D., Nevers, R. & Tank, D. W. Probing variability in a cognitive map using manifold inference from neural dynamics. Preprint at https://www.biorxiv.org/ content/10.1101/418939v2 (2018). 

22. Nieh, E. H. et al. Geometry of abstract learned knowledge in the hippocampus. _Nature_ **595** , 80–84 (2021). 

23. Mizuseki, K., Sirota, A., Pastalkova, E., Diba, K. & Buzsáki, G. Multiple single unit recordings from different rat hippocampal and entorhinal regions while the animals were performing multiple behavioral tasks. CRCNS.org. https://doi.org/10.6080/ K09G5JRZ (2013). 

24. Mizuseki, K. et al. Neurosharing: large-scale data sets (spike, LFP) recorded from the hippocampal-entorhinal system in behaving rats. _F1000Res._ **3** , 98 (2014). 

25. Jung, M. W., Wiener, S. I. & McNaughton, B. L. Comparison of spatial firing characteristics of units in dorsal and ventral hippocampus of the rat. _J. Neurosci._ **14** , 7347–7356 (1994). 

26. Hafting, T., Fyhn, M., Molden, S., Moser, M.-B. & Moser, E. I. Microstructure of a spatial map in the entorhinal cortex. _Nature_ **436** , 801–806 (2005). 

27. Kjelstrup, K. B. et al. Finite scale of spatial representation in the hippocampus. _Science_ **321** , 140–143 (2008). 

28. Bialek, W. _Biophysics: Searching for Principles_ (Princeton University Press, 2012). 

29. Wilson, M. A. & McNaughton, B. L. Dynamics of the hippocampal ensemble code for space. _Science_ **261** , 1055–1058 (1993). 

30. Ziv, Y. et al. Long-term dynamics of CA1 hippocampal place codes. _Nat. Neurosci._ **16** , 264–266 (2013). 

31. Cover, T. M. & Thomas, J. A. _Elements of Information Theory_ (John Wiley & Sons, 2012). 

32. Brunel, N. & Nadal, J.-P. Mutual information, Fisher information, and population coding. _Neural Comput._ **10** , 1731–1757 (1998). 

33. Kloosterman, F., Layton, S. P., Chen, Z. & Wilson, M. A. Bayesian decoding using unsorted spikes in the rat hippocampus. _J. Neurophysiol._ **111** , 217–227 (2014). 

34. Boss, B. D., Turlejski, K., Stanfield, B. B. & Cowan, W. M. On the numbers of neurons on fields CA1 and CA3 of the hippocampus of Sprague-Dawley and Wistar rats. _Brain Res._ **406** , 280–287 (1987). 

35. West, M., Slomianka, L. & Gundersen, H. J. G. Unbiased stereological estimation of the total number of neurons in the subdivisions of the rat hippocampus using the optical fractionator. _Anat. Rec._ **231** , 482–497 (1991). 

36. Thompson, L. & Best, P. Place cells and silent cells in the hippocampus of freely-behaving rats. _J. Neurosci._ **9** , 2382–2390 (1989). 

37. Lee, I., Yoganarasimha, D., Rao, G. & Knierim, J. J. Comparison of population coherence of place cells in hippocampal subfields CA1 and CA3. _Nature_ **430** , 456–459 (2004). 

38. Eliav, T. et al. Multiscale representation of very large environments in the hippocampus of flying bats. _Science_ **372** , eabg4020 (2021). 

39. Harland, B., Contreras, M., Souder, M. & Fellous, J.-M. Dorsal CA1 hippocampal place cells form a multi-scale representation of megaspace. _Curr. Biol._ **31** , 2178–2190 (2021). 

40. Buzsáki, G. & Mizuseki, K. The log-dynamic brain: how skewed distributions affect network operations. _Nat. Rev. Neurosci._ **15** , 264–278 (2014). 

41. Karlsson, M. P. & Frank, L. M. Network dynamics underlying the formation of sparse, informative representations in the hippocampus. _J. Neurosci._ **28** , 14271–14281 (2008). 

42. Bittner, K. C., Milstein, A. D., Grienberger, C., Romani, S. & Magee, J. C. Behavioral time scale synaptic plasticity underlies CA1 place fields. _Science_ **357** , 1033–1036 (2017). 

43. Nitz, D. & McNaughton, B. Differential modulation of CA1 and dentate gyrus interneurons during exploration of novel environments. _J. Neurophysiol._ **91** , 863–872 (2004). 

44. Ghaninia, M. et al. Hyperbolic odorant mixtures as a basis for more efficient signaling between flowering plants and bees. _PLoS ONE_ **17** , e0270358 (2022). 

45. Sharpee, T. O. An argument for hyperbolic geometry in neural circuits. _Curr. Opin. Neurobiol._ **58** , 101–104 (2019). 

46. Driscoll, L. N., Pettit, N. L., Minderer, M., Chettih, S. N. & Harvey, C. D. Dynamic reorganization of neuronal activity patterns in parietal cortex. _Cell_ **170** , 986–999 (2017). 

47. O’Keefe, J. & Burgess, N. Geometric determinants of the place fields of hippocampal neurons. _Nature_ **381** , 425–428 (1996). 

48. Tolhurst, D. J., Movshon, J. A. & Dean, A. F. The statistical reliability of signals in single neurons in cat and monkey visual cortex. _Vis. Res._ **23** , 775–785 (1983). 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons. org/licenses/by/4.0/. 

© The Author(s) 2022 

Nature Neuroscience | Volume 26 | January 2023 | 131–139 

**139** 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

## **Methods** 

## **Data and processing** 

The dataset in which the rat was exposed to a 48-m linear track was recorded from five different animals along the entire track (see original paper[20] for detailed procedure of surgery, training, recording, etc.). All procedures were performed according to the Janelia Research Campus Institutional Animal Care and Use Committee guidelines on animal welfare (protocol 11–73). In brief, the subjects were five adult male Long-Evans rats, 400–500 g at the time of surgery. Two rats had fewer than 30 active neurons (overall average firing rate within the range 0.1–7 Hz) recorded, and they were excluded from further analyses. The track and room were both entirely novel to the animals. Animals made 3–5 traversals of the full extent of the track during each epoch (Fig. 3b,c) while their neural activity was recorded using a 64-channel system. Spikes were detected by a 60–70-µV negative threshold on a 600–6,000-Hz filtered signal, and waveforms (32 samples at 32 kHz) were captured around each threshold crossing. Local field potential (LFP) (0.1–9,000 Hz) was recorded continuously at 32 kHz. The position of the animals was reconstructed from video taken by three wide-angle overhead cameras synchronized to the time stamp clock from the acquisition system using a time stamp video titler. Exponential fitting of place field size distribution is done with a maximum likelihood estimate. To take into account that small place fields tend to be undersampled, we explicitly excluded the smallest place fields (<25 cm, first column of histogram in Fig. 1d) and modified the prior accordingly. In this way, the presence or absence of these fields does not affect the estimation of curvature. For computation of the entropy of each segment of the linear track, turn angles were considered in each segment (with angles = 0 for straight segments). All turn angles were discretized into 15 bins, and the entropy for each segment was calculated as ∑ _i pi_ log2 _p_ 1 _i_[, where ] _[i]_[ indexes bins of the ] turning angles. 

The first-pass speed for each place field was computed by dividing the field size by the first-time pass duration of the animal through the place field with the cell firing at least one spike (this ≥1-spike requirement is assumed for all of the following description of first-pass duration). The average speed in each 40-inch (~1-m) segment during place field formation was calculated as follows: average segment speed = (∑ili)/(∑i first-pass duration), where _i_ is the index of place fields that were centered within the segment, and _li_ is the size of each place field. We can then compute the temporal familiarity of the rat with the segment during place field formation as the time spent per unit length: temporal familiarity (s) = 1 m/average segment speed, which are used in Fig. 3d as the _x_ coordinates. When segment length is not unit (as in Extended Data Fig. 10a), a normalization of segment length is applied to make the familiarity measures comparable. 

For locating the neurons recorded in CA1, either immediately after the experiment or within a few days of it, 3–4 tetrodes were electrolytically lesioned (20 µA for 10 seconds) as fiducials, and animals were transcardially perfused with PBS, followed by a 4% paraformaldehyde solution. Brains were cut in 50-µm sections and stained with cresyl violet. Fiducial lesions, electrode tracks and - the relative locations of the tetrode guide cannulas in each micro drive, as well as allowance for brain shrinkage, were used to estimate the AP and ML coordinates of each tetrode with respect to a rat brain atlas[49] . Only tetrodes localized to the CA1 region were used in analysis. The atlas was used to construct a 3D model of the CA1 pyramidal cell layer, allowing an estimate of the tetrode locations with respect to the septotemporal and proximodistal axes of CA1. 

All the other datasets were obtained from http://crcns.org/ data-sets/hc/hc-3, contributed by the Buzsáki laboratory at New York University[23][,][24] . Neural activity in these datasets was recorded using either four or eight shank probes at 20 kHz. Each shank has eight 

recording sites, making 32 or 64 possible recording sites (channels). Spike detection was performed on the output from raw data with an 800–5,000-Hz bandpass filtering. See http://crcns.org/files/data/hc3/ crcns-hc3-processing-flowchart.pdf for more details about recording and experiments. 

For rats exploring a 180 × 180-cm box, all sessions that have more than 50 simultaneously recorded CA1 neurons were included for analysis. We also excluded neurons that are marked as inhibitory or not identified and those that have average firing rates outside the range 0.1–7 Hz during the entire recording session. We also excluded neurons that have average firing rates between 0.1 Hz and 7 Hz but remain silent (fire zero spikes) for more than 30 min for potential death of the cell or movement of electrodes. Details of sessions used are summarized in Supplementary Table 2. 

## **Place field determination and spatial information calculation** 

For place field determination on the linear track, animals were allowed to make 3–5 traversals of the full extent of the track in four epochs[20] . Rate maps were constructed by taking the number of spikes in each 1-cm spatial bin of the track divided by the occupancy in that bin, for each of the two directions of movement. Both were smoothed with a Gaussian kernel with an s.d. of 10 cm. Only periods when the animal’s velocity was greater than 5 cm s[−1] were included in the spatial firing rate maps. A place field was defined as at least 15 contiguous centimeters of the rate map in which the firing rate exceeded 2 Hz. Because, in linear tracks, place fields may be directional, place fields were detected independently for each directional firing rate map, outbound and inbound, and then fields in different directions were merged if either field showed at least 50% overlap with the other (for more details on experimental procedure, see ref.[20] ). For place field determination in Fig. 3h, we did not impose the 15-cm length requirement and did not merge place fields with different directions to have numerically more place fields and small place fields for estimating hyperbolic radius. 

For place field determination in the square box of size 180 × 180 cm, rate maps were constructed by taking the number of spikes in each 2 × 2-cm spatial bin of the box divided by the occupancy in that bin. The rate map is then smoothed with a 2D Gaussian kernel with an s.d. of 10 cm. Again, only periods when the animal’s velocity was greater than 5 cm s[−1] were included in the spatial firing rate maps. We then detected potential place fields as all contiguous regions in the rate map in which the firing rate exceeded 2 Hz, followed by a manual breakdown of some of these place fields into smaller ones when they have more than one peak in the firing rate map. 

For spatial information calculation, the following formula was used[50] : 

**==> picture [199 x 53] intentionally omitted <==**

where _i_ = 1, · · ·; _N_ are pixel indices in the rate map; _pi_ is the probability of occupancy of pixel _i_ ; _λi_ is the mean firing rate of pixel _i_ ; and _λ_ is the overall mean firing rate of the cell on the whole track or box. 

## **Position decoding with a maximum likelihood decoder** 

The spatial firing rate maps are computed with the procedure described above except that we now use a 5 × 5-cm spatial bin instead of 2 × 2 cm. The time window we use is _δt_ = 500 ms. Windows with mean speed less than 5 cm s[−1] were not used for decoding. For each time window, we _N_ compute the log-likelihood of observing the spike count vector { _nj_ } _j_ =1 at each pixel _i_ assuming conditional independence among neural responses: 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [207 x 52] intentionally omitted <==**

where _λij_ is the mean firing rate of the _j_ th neuron in pixel _i_ . The decoded _N_ location is then taken as the pixel that maximizes log _p_ ({ _nj_ } _j_ =1[|] _[i]_[)][. To take ] into account the dependence of the decoding error on the overall firing rate of the population, which differs across sessions, we subsampled between 17 and 25 neurons from all the active pyramidal cells for each time window in a 20-min session and computed the decoding error for each number of subsampled neurons. The dependence of the median decoding error as a function of the total number of spikes is shown in Fig. 4a. This dependence is exponential, with exponent that characterizes the decoding accuracy per spike. 

## **Computation of the pairwise correlation matrices** 

The cross-correlogram of spike trains of two neurons at time delay τ is 1 _T_ computed as _ccgij_ ( _τ_ ) = _T_[∫] 0 _[f][i]_[ (] _[t]_[)] _[ f][j]_[ (] _[t]_[ +] _[ τ]_[)] _[ dt]_[, where ] _[f][i]_[(] _[t]_[) is the spike train ] of the _i_ th neuron, and _T_ is the total duration of the recording considered. Then, the correlation of firing of two neurons on a time scale of _τmax_ is computed as: _Cij_ = _τmax_ 1 _rirj_[max][ (∫] _τ_ 0 _max ccgij_ ( _τ_ ) _dτ_ , ∫0 _τmax ccgji_ ( _τ_ ) _dτ_ , where ) _ri_ is the average firing rate of the _i_ th neuron during the recording time considered. Notice that the resulting correlation value is always non-negative. This computation replicates Giusti et al.[16] , which developed the clique topology method to be used for analyzing the pairwise correlation matrix. For all figures shown, we used _τmax_ = 1 second. For all datasets, only neurons with average firing rates in the range 0.1–7 Hz were included in the pairwise correlation computation. For datasets obtained from CRCNS, we used spike times from only the last two-thirds of the total duration of each session. Changing _τmax_ to 500 ms does not change our conclusions: (1) Betti curves of all the displayed datasets can be fitted with a 3D hyperbolic geometry ( _P_ > 0.05 for both curve integral and L1 distance for all three Betti curves); (2) low-dimensional (≤10D) Euclidean geometry still cannot explain the Betti curves that are used to falsify Euclidean geometry in Fig. 2e,h and Extended Data Figs. 3 and 4; and (3) hyperbolic radius increases proportionally to the logarithm of time that the animal had to explore it. 

For time shifting the spike trains as controls for Betti curves, a random time lag is added to each neuron’s spike train with periodic boundary condition applied so that the firing statistics of single neurons are preserved. The time lags are different across neurons to destroy the pairwise correlation statistics. 

## **Clique topology method for finding underlying hidden geometry in neural population responses** 

A useful technique to determine the geometry in which neuronal responses reside is clique topology. This method detects structures in a pairwise similarity matrix (or negative distance matrix) of points that are (1) invariant to any monotonic linear or non-linear transformations of the entries of the similarity matrix, making it ideal to use for neuronal responses that are known to be distorted by various monotonic functions and (2) characteristic of the underlying geometry. Here, we use pairwise correlation between CA1 neuronal responses (see above) for the similarity matrix as _Sij_ = _Cij_ , where _Sij_ is the similarity between responses of cells _i_ and _j_ , and _Cij_ is the correlation between two cells’ responses. This metric intuitively is reflective of degree of place field overlap between two neurons[15] . Provided with the symmetric pairwise correlation matrix, the algorithm passes the matrix through a step function of different thresholds to only keep those entries in the matrix above the threshold (Fig. 2b). Based on these values, a topological graph is created (Fig. 2c). This graph can then be characterized by its numbers of cycles (holes) in one, two or higher dimensions (called 

one cycle, two cycles, etc.), excluding those that arise from boundaries of higher-dimensional cliques. With high thresholds of the step function, the number of cycles will, in general, be low, as most nodes are not interconnected. With low thresholds, the number of cycles will also, in general, be low, as nodes form fully connected networks. These numbers of cycles in one, two or higher dimensions at a set threshold are called the 1st Betti number, 2nd Betti number and so on. Plotting them as a function over the entire density range _ρ_ of links (from highest threshold to lowest threshold) gives the so-called 1st Betti curve _β_ 1 ( _ρ_ ), 2nd Betti curve _β_ 2 ( _ρ_ ) and so on. These Betti curves are very sensitive to similarity matrices produced from different geometries and, hence, can be used for identifying the underlying geometric structure of CA1 neural representation. For our datasets, we use the first three Betti curves to search for the underlying geometries of the data. The CliqueTop MATLAB package was obtained online from the original authors[16] . 

The pairwise correlation matrices of CA1 neuronal responses that we used for Betti curve generations are computed as described above. From a correlation matrix, we can also define the distance matrix between neuronal responses as _Dij_ = − _Cij_ , where _Dij_ is the distance between neurons _i_ and _j_ , and _Cij_ is the correlation between two neurons as defined above. This definition makes neurons that are more correlated with each other to have shorter distance between them, consistent with intuition. We note that, with the algorithm being invariant under any non-linear monotonic transformations, it can be easily shown that this definition of distance can be monotonically transformed to become a true distance metric. Notably, the relative ordering of all the entries of a certain distance matrix may not be realizable in some geometries no matter how the points are configured, but, in other geometries, it becomes possible. Thus, the tool can be used to test geometries for their ability to support a found correlation matrix by inspecting those invariant features, namely the Betti curves, _βm_ ( _ρ_ ), where _ρ_ is the edge density from 0 to 1. 

To determine the geometry of the neuronal responses, we screened two kinds of geometries: Euclidean geometry of different dimensionality and hyperbolic geometry (native model) with different dimensionality and radii. In each geometry, we sampled points (same number as number of used CA1 neurons) uniformly according to the geometric properties. In d-dimensional Euclidean geometry, the points were sampled uniformly in the d-dimensional unit cube. In d-dimensional hyperbolic model, _ζ_ is set as 1 while the maximal radius _R_ max of the geometry was adjusted to different values (this is equivalent to fixed maximal radius _R_ max with changing curvature _ζ_ ). The points are then sampled uniformly to have uniformly distributed angles and their radii _r_ ∈ [0, _R_ max] following the distribution _ρ_ ( _r_ ) ~ sinh[(] _[d]_[−1)] ( _r_ ), which is approximately proportional to _e_[(] _[d]_[−1)] _[r]_ when _r_ ≫ 1. With points sampled, we then compute their pairwise distance matrices with their respective distance metric: Euclidean distance for points sampled from Euclidean geometry and hyperbolic distance for points sampled from hyperbolic geometry. The distance metric between two points in a hyperbolic geometry of constant curvature K = − _ζ_[2] < 0, _ζ_ > 0, is given by the hyperbolic law of cosines: 

cosh ( _ζx_ ) = cosh ( _ζr_ ) cosh ( _ζr_ ′) − sinh ( _ζr_ ) sinh ( _ζr_ ′) cos Δ _θ_ 

where _x_ is the hyperbolic distance; _ζ_ is set as 1 in our model; _r_ and _r_ ′ are the radial distances of the two points from the origin; and ∆θ is the angle between them. 

Considering that a small amount of noise may exist in the correlation between firing of two CA1 neurons due to the different trajectories taken by the animal, the stochastic nature of neuronal firing and other high-order cognitive processes, we also added i.i.d. multiplicative Gaussian noise to each entry of the pairwise distance matrices obtained for both Euclidean model and hyperbolic model before generating the Betti curves from them (no noise added to the experimental pairwise correlation matrices). Thus, the final distance matrices to be used for 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

Betti curve analyses have entries _Dij_ = _D[geo] ij_[⋅][ (1 + ] _[ϵ]_[·] _[N]_[(0,1)), where ] _[D][geo] ij_[ is ] the geometric distance computed based on the coordinates of the sampled points _i_ and _j_ , and _ϵ_ is the noise level set to be 0.05 for all the analyses in this paper. To summarize, sampled points from different geometries give different Betti curves through (1) different distribution of points in these geometries and (2) different distance metrics used to compute the pairwise distances. 

To determine whether a geometry underlies the correlation among CA1 neuronal responses, we compare the Betti curves generated from that geometry (by sampling points as described above) to the Betti curves generated from the pairwise correlation matrices of CA1 neurons (experimental Betti curves). Specifically, we uniformly sample points (same number as number of CA1 neurons) from the geometry, compute the pairwise distance matrix, use clique topology on the negative pairwise distance matrix (to correspond to correlation matrix) to generate the Betti curves and repeat 300 times. As a result, we have 300 × 3 Betti curves, as for each sampling we obtain the first three Betti curves ( _β_ 1 ( _ρ_ ), _β_ 2 ( _ρ_ ) and _β_ 3 ( _ρ_ )), counting number of cycles in one, two and three dimensions, respectively. For each Betti curve _βm_ ( _ρ_ ), we compute its integrated Betti value, defined as _βm_ = ∫10 _[β][m]_[ (] _[ρ]_[)] _[ dρ]_[, where ] _ρ_ is the edge density, and _βm_ ( _ρ_ ) denotes the m-th Betti curve. The integrated Betti values computed from the experimental Betti curves can then be compared to those generated from sampling in the given geometry (model Betti curves). We report the _P_ values of integrated Betti values as the two-tailed percentiles for where the experimental integrated Betti values fall within the sampling-generated distributions (of 300 samples), separately for _β_ 1 ( _ρ_ ), _β_ 2 ( _ρ_ ) and _β_ 3 ( _ρ_ ). Besides integrated Betti values, we also tested for L1 distances. Specifically, for each geometry, we calculate the average model Betti curves _β_[ave] 1 ( _ρ_ ), _β_[ave] 2 ( _ρ_ ) and _β_[ave] 3 ( _ρ_ ) by averaging over all 300 sampling-generated model Betti curves. Then, we compute the L1 distance between the experimental Betti curves ( _βm_ ( _ρ_ ), m = 1, 2, 3) and the averages: _lm_ = ∫10[||] _[β][m]_[ (] _[ρ]_[) −] _[β] m[ave]_[(] _[ρ]_[)||] _[dρ]_[. The ] _[P]_[ value of this L1 distance is the one-tailed ] percentile of itself in the distribution of L1 distances computed from each sampling-generated Betti curve and the average (% sampling that resulted in a larger or equal L1 distance to average than the experimental L1 distance). For visualization purposes only, the experimental Betti curves were smoothed with a kernel size of 1/50 total number of edge densities of each Betti curve (no smoothing was used for computing integrated Betti values and L1 distances). 

If a geometry gives statistically similar Betti curves compared to the experimental Betti curves, then the geometry is viable in explaining the neural representation. On the contrary, if the model Betti curves are dissimilar to the experimental Betti curves, then the geometry under testing is not viable. 

## **Determination of optimal** _**R**_ **max or dimension of hyperbolic geometry with Betti curves** 

To determine the optimal _R_ max of the hyperbolic geometry that captures a correlation matrix in Figs. 2 and 3, we searched over _R_ max in {5:0.5:24}. For each _R_ max, we calculate the _P_ values for integrated Betti values and L1 distances of the first two Betti curves (the 3rd Betti curve was excluded as its integrated Betti value becomes unstable when number of neurons is small). Multiplying the four _P_ values, we obtain the _P_ value product of them. The optimal _R_ max is defined as the _R_ max that results in the maximum _P_ value product out of all the _R_ max values that have been tested. For a recording session, we randomly sample 75% of active CA1 neurons, compute their pairwise correlation matrix, determine the optimal _R_ max as above and repeat 100 times to obtain a distribution of _R_ max for the recording session. 

To quantify how well the experimental Betti curves are fitted by model Betti curves from hyperbolic geometry of different dimensions, we used χ[2] statistics. Specifically, we first binned the Betti curves ( _nbins_ = 10 for each curve) and then computed the square of the difference between the experimental Betti curves after binning and the mean 

of the model Betti curves (estimated with bootstrap of 500 repetitions) after binning, denoted _Dexpm_ . We also computed the square of the difference between model curves from each sampling of points and the mean of the model curves and took their average, denoted _Dmodel_ . The χ[2] statistic is defined as _χ_[2] = _nbins_ 1[∑] _[bins] DDmodelexpm_[, where the division is ] bin-wise. Note that, when this χ[2] statistic is small, it means that the deviation of model curves from the experimental curves is small, which indicates that the experimental curves are well-explained by the model and vice versa. We also tested whether the dimension of hyperbolic geometry has an effect on this χ[2] statistic with two-way ANOVA, which also controls for the effect of different animals and sessions. 

## **Bayesian estimator of curvature/hyperbolic radius from place field sizes** 

We used a Bayesian estimator on place field sizes, taking into account that we can only observe place fields within a range of sizes [ _sl_ , _su_ ] due to the size of the entire experimental environment, the threshold for determination of place fields and grid sizes for computing rate maps. The probability to observe one place field size _s_ given curvature _ζ_ of the representation is given by: 

**==> picture [157 x 18] intentionally omitted <==**

when _sl_ < _s_ < _su_ and 0 otherwise, and 

**==> picture [156 x 22] intentionally omitted <==**

Then, by Bayes’ theorem, 

**==> picture [185 x 22] intentionally omitted <==**

where _P_ ( _ζ_ ) is the prior on _ζ_ which we used uniform distribution. Then, the estimate of _ζ_ is the _ζ_ that maximizes _P_ ( _ζ_ | _s_ 1,⋯, _sN_ ). 

## **Simulation on the effect of undersampling on estimated** _**R**_ **max** 

For this simulation, we fix the radius of the hyperbolic geometry to be 10 and randomly draw 41 points from it (same as the number of neurons in Fig. 2d–f). Then, at each time step of 1 second (same time scale as _τ_ max in the correlation calculation), we observe a noise-corrupted version of the pairwise distances (or negative pairwise correlations) among their responses. Specifically, we apply multiplicative Gaussian noise to the true pairwise distance matrix entrywise with _ϵ_ = 0.5 in the formula above. At each readout time, we average all the observations so far to obtain one pairwise distance matrix to be used for Betti curve analysis on estimating the underlying _R_ max, using the method just described above. 

## **Fisher information of model neurons** 

We modeled the neurons to have Gaussian tuning: _fi_ ( _s_ ) = _Aiexp_ (− 21[(] _[s]_[ −] _[μ][i]_[)] _T_ ∑− _i_ 1 ( _s_ − _μi_ )) , with stimulus _s_ = [ _x_ , _y_ ] as a 2D random variable taking values uniformly from [0, 1] × [0, 1]. For each neuron, we sample _Ai_ ∼ _unif_ [5,25], _μi_ ∼ _unif_ ([0, 1] × [0, 1]) and Σ _i_ = R( _θi_ ) diag( _σ_[2] _i_ 1[,] _[ σ]_[2] _i_ 2[)R(] _[θ][i]_[)][T][, where R(] _[θ][i]_[) is the rotation matrix ][(][ cos] sin _θ[ θ] i[i]_[−] cos[sin] _θ[ θ] i[i]_[)][ with ] _θi_ ∼ _unif_ [0, 2 _π_ ], and _σi_ 1 and _σi_ 2 are i.i.d. ∼ exp(− _ζσ_ ), with _ζ_ denoting the curvature of the representation geometry, which dictates the decay rate of the exponential distribution, and _ζ_[−1] is the mean of the distribution. For uniform distribution of place field sizes, _σi_ 1 and _σi_ 2 are i.i.d. ∼ _unif_ [0, 2 _ζ_[−1] ] to keep the same mean as in the exponential case. 

We also assume the neurons to have independent Poisson variability[48] . Thus, given a stimulus _s_ , the number of spikes fired by a neuron is _ri_ | _s_ ∼ _Poisson_ ( _fi_ ( _s_ )). These neurons’ responses then encode a posterior 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

distribution on _s_ : _p_ ( _s_ | _r_ 1,⋯, _rN_ ). For each of 10,000 iterations, a stimulus _s_ is randomly generated ∼ _unif_ ([0, 1] × [0, 1]) with _Ai_ , _μi_ and Σ _i_ all randomly generated again with the above distributions. The Fisher information matrix _I_ ( _s_ ) is computed by definition: 

**==> picture [232 x 21] intentionally omitted <==**

which, for the independent neuron model as we assume here, simplifies to: 

**==> picture [188 x 21] intentionally omitted <==**

So, with Fisher information matrix _I_ ( _s_ ) computed each time, we can compute the average magnitude of the 10,000 Fisher information matrices, defined as det( _I_ ( _s_ ))[0.5] . Second-order polynomial is used for fittings, and the optimal size of the hyperbolic representation is determined as the _R_ max under the peak of the fitting polynomial. 

For the case of each cell having potentially multiple place fields, we extracted the number of place fields from three 20-min sections in Fig. 3. Dividing them by the number of all cells gives mean number of place fields per cell. Similarly, we can compute standard deviations of the number of place fields across cells. The number of place fields per cell is experimentally described by a gamma distribution[20] , whose scale and shape parameters can now be determined by the average values of means and standard deviations computed from the three sessions. After drawing the number of place fields for each of _N_ cells, the number is rounded to the closest integer. Then, for each place field, _Ai_ and Σ _i_ are randomly generated as above, and the Fisher information matrix can be computed for a random _s_ . To also match the size of the environment to the experiment (1.8 × 1.8 m), _μi_ is now drawn from _unif_ ([0, 1.8] × [0, 1.8]) and so is _s_ for each of 10,000 iterations. 

## **Statistics and reproducibility** 

No statistical method was used to predetermine sample size, but our sample sizes are similar to those reported in previous publications[12][,][16][,][30][,][41] . We analyzed data from previous publications[20][,][23][,][24] . For rats exploring the 48-m linear track, two rats had fewer than 30 active neurons (overall average firing rate within the range 0.1–7 Hz) recorded, and they were excluded from further analyses. For rats exploring a 180 × 180-cm box, all sessions that have more than 50 simultaneously recorded CA1 neurons were included for analysis. We also excluded neurons that are marked as inhibitory or not identified and those that have average firing rates outside the range 0.1–7 Hz during the entire recording session. We also excluded neurons that have average firing rates between 0.1 Hz and 7 Hz but remain silent (fire zero spikes) for more than 30 min for potential death of the cell or movement of electrodes. Details of sessions used are summarized in Supplementary Table 2. There was no randomization or division into experimental groups. Analyses were not performed blinded to the conditions of the experiments. Throughout the study, we employed non-parametric statistical methods. For comparisons between two groups, we used unpaired two-sample _t_ -tests. Data distribution was assumed to be normal, but this was not formally tested. For comparisons among more than two groups, ANOVA with Tukey’s post hoc test was used. For checking whether samples are likely coming from a specific theoretical distribution, χ[2] GOF test was used. Correlations are reported using Pearson’s correlation coefficient. More information can be found in the Nature Research Reporting Summary. 

## **Data availability** 

All datasets used in this study, except rats running on the 48-m linear track, were generously contributed by György Buzsáki at http://crcns. org/data-sets/hc/hc-3 (refs.[23][,][24] ). See Supplementary Table 2 for the sessions used. The datasets in which rats ran on the 48-m linear track are made available on https://crcns.org/data-sets/hc/hc-31/. Source data are provided with this paper. 

## **Code availability** 

Code written in MATLAB 2018b to simulate Fisher information models is publicly accessible on GitHub at https://github.com/HuanqiuZhang/ Fisher_info_codes. The CliqueTop MATLAB package (2015 version) used for computing Betti curves is obtained from the original authors[16] at https://github.com/nebneuron/clique-top. Other codes are available upon reasonable request. 

## **References** 

49. Paxinos, G. & Watson, C. _The Rat Brain in Stereotaxic Coordinates_ (Elsevier Academic Press, 2005). 

50. Skaggs, W. E., McNaughton, B. L. & Gothard, K. M. An information-theoretic approach to deciphering the hippocampal code. in: _Advances in Neural Information Processing Systems_ 1030–1037 (1993). 

## **Acknowledgements** 

We are grateful to Y. Zhou and W. Hsu for helpful discussions and feedback on the manuscript. This research was supported by an AHA-Allen Initiative in Brain Health and Cognitive Impairment award made jointly through the American Heart Association and the Paul G. Allen Frontiers Group (19PABH134610000); the Janelia Visiting Scientist Program; the Dorsett Brown Foundation; the Mary K. Chapman Foundation; the Aginsky Fellowship; National Science Foundation (NSF) grant IIS-1724421; the NSF Next Generation Networks for Neuroscience Program (award 2014217); National Institutes of Health grants U19NS112959 and P30AG068635 (to T.O.S.); and the Howard Hughes Medical Institute (to P.D.R. and A.K.L.). The funders had no role in study design, data collection and analysis, decision to publish or preparation of the manuscript. 

## **Author contributions** 

H.Z. and T.S. designed the study and wrote the manuscript. P.D.R. and A.K.L. designed the experiments. P.D.R. performed the experiments. H.Z. performed the analyses and simulations. All authors discussed the results and contributed to writing the final manuscript. 

## **Competing interests** 

The authors declare no competing interests. 

## **Additional information** 

**Extended data** is available for this paper at https://doi.org/10.1038/ s41593-022-01212-4. 

**Supplementary information** The online version contains supplementary material available at https://doi.org/10.1038/s41593022-01212-4. 

**Correspondence and requests for materials** should be addressed to Tatyana O. Sharpee. 

**Peer review information** _Nature Neuroscience_ thanks Dori Derdikman and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. 

## **Reporting summary** 

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [504 x 535] intentionally omitted <==**

**Extended Data Fig. 1 | Betti curves generated from hyperbolic geometry of low dimensions (with optimized radius) are statistically indistinguishable from the experimental Betti curves for both 48m-linear track (a) and square box (b) environments with 3D being the optimal dimension in** 

**general.** For each environment type, three sessions with the most number of neurons recorded are shown. Session IDs are shown on the left. The Betti curves are statistically similar both in terms of the area under the curve (measured by integrated Betti value) and the curve shape (measured by L1 distances between curves). Boxes show model interquartile range (n = 300 independent replicates). Center line indicates model median and upper and lower whiskers extend to the most extreme data points excluding outliers. Black lines indicate 

experimental values. (c) χ[2] statistics (see Methods) are used to quantify how well the experimental Betti curves are fitted by model Betti curves from different dimensions. Results from two example sessions are shown, one for each environmental type (linear vs. square). Boxes show interquartile range (n = 500 bootstraps). Center line indicates median. Upper and lower whiskers encompass 95% of data. One-way ANOVA for each session: _p_ < 10[−8] across all dimensions (linear: F = 11239.87, square: F = 13613.23). Tukey’s post hoc test indicates that 3D fits are significantly better than fits from other dimensions ( _p_ < 10[−8] for all 3 pairwise comparisons). Same conclusions hold for two-way ANOVA across all sessions in (a) and (b). 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 506] intentionally omitted <==**

**Extended Data Fig. 2 | Betti curves generated from 3D hyperbolic geometry are statistically indistinguishable from the experimental Betti curves for both linear track and square box environments. (a** ) Illustration on how the hyperbolic radius is estimated for each session. 3D hyperbolic geometries of different radii are used to generate model Betti curves (solid lines and shading in the insets indicate mean ± std), which are then compared against the experimental Betti curves (dashed lines in the insets) of the session for _p_ -values of integrated Betti values and L1 distances. The product of _p_ -values versus radii are plotted and the radius of the session is estimated to be the radius that gives 

the largest product. ( **b** ) Linear track datasets. Notations are as in Fig. 2. Boxes show model interquartile range (n = 300 independent replicates). Center line indicates model median and upper and lower whiskers encompass 95% of model range. Black lines indicate experimental values. 48-m linear track datasets are from Rich, 2014. The rest are publicly available datasets collected by Dr. Buzsaki’s group including the two 2.5-m linear track datasets (2nd row in **b** ) and the square box datasets ( **c** ). Session IDs are shown at the upper-left corner of each panel. See Supplementary Table 1 for all the radii used and the fitting statistics. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 558] intentionally omitted <==**

**Extended Data Fig. 3 | Betti curves generated from low-dimensional Euclidean geometries are statistically different from the experimental Betti curves in 48-m linear track exploration.** Top to bottom rows represent different animals with N = 41, 38 and 34, respectively. ( **a,d,g** ) Distribution of experimental integrated Betti values (black lines) versus model statistics (boxplots). ( **b,e,h** ) Distribution of experimental L1 distances (black lines) versus 

model statistics (boxplots). Boxes show model interquartile range (n = 300 independent replicates). Center line indicates model median and upper and lower whiskers encompass 95% of model range. Black lines indicate experimental values. ( **c,f,i** ) Experimental Betti curves (dashed lines) and model Betti curves (solid lines and shading indicate mean ± std) from Euclidean geometry of dimension shown on the top. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 568] intentionally omitted <==**

**Extended Data Fig. 4 | Betti curves generated from low-dimensional Euclidean geometries are statistically different from the experimental Betti curves in square box exploration.** Top to bottom rows represent different datasets (session IDs shown on the left) with N = 56, 48 and 42, respectively. ( **a,d,g** ) Distribution of experimental integrated Betti values (black lines) versus model statistics (boxplots). ( **b,e,h** ) Distribution of experimental L1 distances 

(black lines) versus model statistics (boxplots). Boxes show model interquartile range (n = 300 independent replicates). Center line indicates model median and upper and lower whiskers encompass 95% of model range. Black lines indicate experimental values. ( **c,f,i** ) Experimental Betti curves (dashed lines) and model Betti curves (solid lines and shading indicate mean ± std) from Euclidean geometry of dimension shown on the top. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [451 x 490] intentionally omitted <==**

**Extended Data Fig. 5 | Betti curves generated from neurons with high spatial information are statistically indistinguishable from those of 3D hyperbolic geometry.** ( **a** ) Distribution of information of each neuron’s response about the animal’s location per second. Black line indicates 25 percentile cutoff of the distribution. Those above the cutoff are used for Betti curve analyses in **b,c** . ( **b,c** ) Same notations as in Fig. 2. ( **d** ) Distribution of information of each neuron’s response about the animal’s location per spike. Black line indicates 25 percentile cutoff of the distribution. Those above the cutoff are used for Betti curve analyses 

in **e,f** . For **a–f** , the animal with the most number of active neurons recorded on the 48-m linear track is used (same one as in Fig. 2d-f). ( **g–l** ) Same analyses for a session in square box. Again, the session with the most number of active neurons is used (same one as in Fig. 2g-i, session ID: ec014.215). For all boxplots, boxes show model interquartile range (n = 300 independent replicates). Center line indicates model median and upper and lower whiskers encompass 95% of model range. Black lines indicate experimental values. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [457 x 521] intentionally omitted <==**

**Extended Data Fig. 6 | Place field size on the linear track as a function of anatomical recording location.** ( **a** ) The location of each place fieldcorresponding cell viewed from above the septal half of CA1, with the field size denoted by the color scale at the right. ( **b** ) The same fields as in ( **a** ) but plotted in terms of the relative septal-temporal and proximal-distal coordinates of CA1. ( **c** ) 

As in ( **b** ) but separated by animal. ( **d** ) and ( **e** ) show the field sizes with respect to the two hippocampal axes, as well as the Pearson’s correlation coefficients and associated two-sided _p_ -values. Jitter has been added to all anatomical values to improve visualization. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 486] intentionally omitted <==**

**Extended Data Fig. 7 | The hyperbolic representation sizes are similar initially** 

**across environments and change over time.** ( **a** ) Estimated hyperbolic radii are similar for linear track and square box environments during the initial exposures. Dots represent median estimates (n = 100 independent sampling), lines represent 95% confidence interval. For linear track, same sessions used as in Fig. 2d and Extended Data Fig. 2b first row; square box session used: ec014.215. ( **b** ) Estimated radius increases for the same animal’s 1st and 8th exposure to a linear track environment. Session ID: ec014.468 and ec014.639. _p_ -value = 4·10[−15] using two-sample _t_ -test for same mean (two-sided). ( **c** ) Estimated radius increases for another animal’s 6th and 10th exposure to a square box environment. Session ID: ec016.397 and ec016.582. _p_ -value = 1.3·10[−5] using two-sample _t_ -test for same mean (two-sided). Hyperbolic radii are estimated using topological analyses for 

both **b** and **c** . For boxplots in **b** and **c** , boxes show interquartile range (n = 100 independent sampling). Center line indicates median and upper and lower whiskers encompass 95% of data. ( **d** ) Exponent of distribution of place field sizes increases over time ( _r_ = 0.85, _p_ = 2·10[−6] with x-axis has log-scale). Same square box sessions used as in Fig. 3a. Dots and error bars (n = 100 independent sampling) indicate medians and 95% confidence intervals. Distribution of 4 sample 20-min sections indicated in the left panel are shown on the right. Same notation as in Fig. 1d. ( **e** ) % active neurons (firing frequency between 0.1 and 7 Hz) decays with familiarity with the environment (number of times the animal has been exposed to the environment). Each data point is a session. Straight line shows the leastsquares fit. _r_ = −0.9174, with associated two-sided _p_ = 0.00361. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 469] intentionally omitted <==**

## **Extended Data Fig. 8 | The increase of hyperbolic radius over time is independent of behavior, network state and time elapsed without** 

**experience.** ( **a** ) No consistent change in the animal’s behavior is observed when the hyperbolic radius changes. Error bars represent standard deviations from jackknife resampling using 15 min out of 20 min (n = 4 jackknives). Same sessions used as in Fig. 3a. Gray lines show least-squares regression. Two-sided _p_ > 0.05 for all three panels. Total area covered is calculated by breaking the square box into 2 × 2 cm grids and counting how many of the grids are passed by the animal during 15 min out of each of the 20-min intervals. ( **b** ) Hyperbolic radius increases over exploration time when periods with running speed <5 cm/sec were excluded from Betti curve calculation. Dots and error bars (n = 100 independent sampling) indicate medians and 95% confidence intervals. Dashed black line is the leastsquares regression of data with log scale on the x-axis (r = 0.91, two-sided _p_ = 2·10[−8] ). Dashed gray line shows the least-squares fit of Eq. 2. ( **c** ) Two animals 

are identified (one for each panel) which explored section 4 of the linear track during epoch 4 (Fig. 3c) for more than 15 min. They were put back into the sleep box for at least 4 h (at most 5 h) and then returned to the long track where they ran an additional 4–5 laps. Hyperbolic radii are estimated using the topological method for epoch 4 and after-sleep exploration. The middle boxplots are obtained by extrapolating hyperbolic radius during epoch 4 to after 4-h sleep using Eq. 2. For both animals, the actual hyperbolic radii estimated during exploration after 4-h sleep are significantly lower than the extrapolated values (two-sided _p_ = 6·10[−8] , 1.5·10[−15] for two animals, respectively, using two-sample _t_ -test for same mean). Boxes show interquartile range (n = 100 independent sampling). Center line indicates median and upper and lower whiskers encompass 95% of data. Jitter has been added to the estimated hyperbolic radii to improve visualization. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 338] intentionally omitted <==**

**Extended Data Fig. 9 | Bias exist when hyperbolic radius is estimated using Betti curve analyses from short neural recordings.** ( **a** ) The estimated hyperbolic radius exhibits strong positive bias when the recording time is less than 1 min in a simulation (see Methods for the simulation details.). Black line at y = 10 represents the ground truth radius value used in the simulation. Boxes show interquartile range (n = 100 independent sampling). Center line indicates median. Upper and lower whiskers encompass 95% confidence interval of the 

radius estimate. ( **b** ) Hyperbolic radius is estimated from actual neural recordings of different length. Shown here are results for two example sessions (session IDs are given on the top left). Boxes show interquartile range (n = 100 independent sampling). Center line indicates median. Upper and lower whiskers encompass 95% of the radius estimate. An exponential function is then fitted to the medians with the time constant denoted on the plot. 

Nature Neuroscience 

**Article** 

https://doi.org/10.1038/s41593-022-01212-4 

**==> picture [519 x 121] intentionally omitted <==**

**Extended Data Fig. 10 | The radius of hyperbolic representation increases over timescale of seconds independent of segment length and exposures used in measure of familiarity.** ( **a** ) Hyperbolic radius increases over time 

when 2-m segments are used instead of 1-m segments ( _r_ = 0.48, _p_ = 0.02). ( **b** ) Hyperbolic radius increases over time when mean speed of all passes are used instead of first passes ( _r_ = 0.54, _p_ = 8·10[−5] ). 

Nature Neuroscience 

Corresponding author(s): Tatyana Sharpee Last updated by author(s): Oct 13, 2022 

**==> picture [227 x 37] intentionally omitted <==**

## Reporting Summary 

Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist. 

## Statistics 

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section. 

## n/a Confirmed 

The exact sample size ( _n_ ) for each experimental group/condition, given as a discrete number and unit of measurement 

A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly 

The statistical test(s) used AND whether they are one- or two-sided 

_Only common tests should be described solely by name; describe more complex techniques in the Methods section._ 

A description of all covariates tested 

A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons 

A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient) AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals) 

For null hypothesis testing, the test statistic (e.g. _F_ , _t_ , _r_ ) with confidence intervals, effect sizes, degrees of freedom and _P_ value noted _Give P values as exact values whenever suitable._ 

For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings 

For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes 

Estimates of effect sizes (e.g. Cohen's _d_ , Pearson's _r_ ), indicating how they were calculated 

_Our web collection on statistics for biologists contains articles on many of the points above._ 

## Software and code 

## Policy information about availability of computer code 

Data collection No software was used for data collection as all the experimental data were obtained from published sources. Data analysis Code written in Matlab 2018b to simulate Fisher information models is publicly accessible on GitHub at https://github.com/HuanqiuZhang/ Fisher_info_codes. The CliqueTop Matlab package (2015 version) used for computing Betti curves is obtained from the original authors (ref. 16) at https://github.com/nebneuron/clique-top. Other codes are available upon request. 

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information. 

## Data 

Policy information about availability of data 

All manuscripts must include a data availability statement. This statement should provide the following information, where applicable: 

- Accession codes, unique identifiers, or web links for publicly available datasets 

- A description of any restrictions on data availability 

- For clinical datasets or third party data, please ensure that the statement adheres to our policy 

All datasets used in this study except rats running on the 48-meter linear track are generously contributed by Dr. Buzsaki at http://crcns.org/data-sets/hc/hc-3. See Table S2 for the sessions used. 

The datasets in which rats ran on the 48-meter linear track will be made available on crcns.org. 

## - Field specific reporting 

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection. Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences 

For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf 

## Life sciences study design 

All studies must disclose on these points even when the disclosure is negative. 

|Sample size<br>Data exclusions<br>Replication<br>Randomization<br>Blinding|No statistical method was used to predetermine sample size, but our sample sizes are similar to those reported in previous publications (refs.<br>12,16,30,41).<br>For rats exploring the 48-meter linear track, there were two rats with less than 30 active neurons (overall average firing rate within the range<br>0.1 - 7 Hz) recorded, which are excluded from further analyses. For rats exploring a 180 x 180 cm box, all sessions that have more than 50<br>simultaneously recorded CA1 neurons were included for analysis. We also excluded neurons that are marked as inhibitory or not identified,<br>and those that have average firing rates outside the range 0.1 - 7 Hz during the entire recording session. We also excluded neurons that have<br>average firing rates between 0.1 and 7 Hz, but remain silent (fire 0 spike) for more than 30 min for potential death of the cell or movement of<br>electrodes.<br>The main findings presented in this study were consistently replicated across 5 animals, environment types (5 linear sessions and 7 square<br>sessions), and environment sizes (3 sessions on 48-meter linear track and 2 sessions on 2.5-meter linear track).<br>There was no randomization or division into experimental groups.<br>Analyses were not performed blinded to the conditions of the experiments.|
|---|---|
||Analyses were not performed blinded to the conditions of the experiments.|



## Reporting for specific materials, systems and methods 

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material, system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response. 

Materials & experimental systems Methods n/a Involved in the study n/a Involved in the study Antibodies ChIP-seq Eukaryotic cell lines Flow cytometry Palaeontology and archaeology MRI-based neuroimaging Animals and other organisms Human research participants Clinical data Dual use research of concern 

