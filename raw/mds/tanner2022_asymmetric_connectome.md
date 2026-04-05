bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## **Redefining the connectome: A multi-modal, asymmetric, weighted, and signed description of anatomical connectivity** 

Jacob Tanner[1] _[,]_[2] , Joshua Faskowitz[3] , Andreia Sofia Teixeira[4] , Caio Seguin[5] , Ludovico Coletta[6] , Alessandro Gozzi[7] , Bratislav Miˇsi´c[8] , and Richard F. Betzel[1] _[,]_[2] _[,]_[5] _[,]_[9] _[,]_[10] _[∗]_ 

> 1 _Cognitive Science Program,_ 2 _School of Informatics, Computing, and Engineering, Indiana University, Bloomington, IN 47405_[3] _National Institute of Health, Bethesda, MD,_ 

> 4 _LASIGE and Faculty of Sciences, University of Lisbon, Lisboa, Portugal,_[5] _Program in Neuroscience, Indiana University, Bloomington, IN 47405_[6] _Fondazione Bruno Kessler, Trento, Trento,_ 

> 7 _Functional Neuroimaging Lab, Istituto Italiano di Tecnologia, Center for Neuroscience and Cognitive Systems, Rovereto, Italy,_ 

> 8 _McConnell Brain Imaging Centre, Montr´eal Neurological Institute, McGill University, Montr´eal, Canada,_[9] _Department of Psychological and Brain Sciences,_ 

> 10 _Network Science Institute, Indiana University, Bloomington, IN 47405_ 

(Dated: December 20, 2022) 

The macroscale connectome is the network of physical, white-matter tracts between brain areas. The connections are generally weighted and their values interpreted as measures of communication efficacy. In most applications, weights are either assigned based on imaging features–e.g. diffusion parameters–or inferred using statistical models. In reality, the ground-truth weights are unknown, motivating the exploration of alternative edge weighting schemes. Here, we explore a multi-modal (combining diffusion and functional MRI data) regression-based, explanatory model that endows reconstructed fiber tracts with directed and signed weights. Benchmarking this method on Human Connectome Project data, we find that the model fits observed data well, outperforming a suite of null models. The estimated weights are subject-specific and highly reliable, even when fit using relatively few training samples. Next, we analyze the resulting network using graph-theoretic tools from network neuroscience, revealing bilaterally symmetric communities that span cerebral hemispheres. These communities exhibit a clear mapping onto known functional systems. We also study the shortest paths structure of this network, discovering that almost every edge participates in at least one shortest path. We also find evidence of robust asymmetries in edge weights, that the network reconfigures in response to naturalistic stimuli, and that estimated edge weights differ with age. In summary, we offer a simple framework for weighting connectome data, demonstrating both its ease of implementation while benchmarking its utility for typical connectome analyses, including graph theoretic modeling and brain-behavior associations. 

## **INTRODUCTION** 

The human connectome refers to the complete set of fiber tracts that link brain regions to one another [1]. It can be reconstructed non-invasively from diffusion weighted images using tractography algorithms [2, 3]. 

The connectome is of great interest to a number of scientific communities. Cognitive processes are supported by distributed, brain-wide networks [4, 5] and many neuropsychiatric disorders are thought to be disorders of dysconnectivity [6, 7]. Mapping connectomes and understanding their organizing and operational principles [3, 8–11] is also a key aim of network neuroscience [12] – the nascent discipline that focuses on modeling and analyzing brain data (micrographs, MR images, electrophysiological recordings) as networks. 

The connectome is an example of an “anatomical” or “structural” network, in that the edges all represent physical, material pathways [13–16]. In anatomical networks, connections are usually associated with weights. 

In human tractography data, these weights are frequently assigned based on diffusion parameters – e.g. fractional anisotropy, mean diffusivity, or streamline counts – and are interpreted as measures of white-matter fiber integrity. 

A related but distinct approach involves mapping “effective connectivity” [17, 18]. This approach uses recordings of brain activity – usually functional MRI data – to model the directed influence exerted by one gray matter region on another. Effective connectivity can be estimated using measures of temporal precedence, such as Granger causality [19–21] or transfer entropy [22, 23], which assess whether errors/uncertainty in the predicted activity of one region can be improved by including information about the history of another. This class also includes dynamic causal models [24–30], which seek the underlying circuit that, given a generative model, can best explain observed brain activity. 

These approaches for mapping anatomical and effective connections have pronounced limitations and trade off their utility with one another. For instance, diffusion/tractography-based measures are incapable of resolving directionality – i.e. the weight of the tract from re- 

> _∗_ rbetzel @ indiana.edu 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

2 

**==> picture [509 x 309] intentionally omitted <==**

FIG. 1. **Fitting and characterizing weighted, signed, and asymmetric structural connectivity.** ( _a_ ) Here, we used linear model to estimate regression (edge) weights. For a given region _i_ , we identified its structurally connected neighbors and used their past activity to predict node _i_ ’s future activity. This procedure results in a series of regression weights; one weight is associated with each neighbor. ( _b_ ) Those weights were then entered into the binary structural connectivity “mask”. When this procedure was repeated for all _i ∈_ [1 _, . . . ,_ 400] it generates a weighted, signed, and asymmetric matrix whose nonzero entries are masked by structural connections (see panel _c_ ). This matrix also has dynamic interpretations; a vector of brain-wide activity can be multiplied into the matrix to make a prediction of the activity at the subsequent time point. ( _d_ ) Two-dimensional histogram showing observed and predicted activity, pooled across all participants and scans. The colors indicate number of samples in any bin. ( _e_ ) Examples of observed and predicted activity for five select regions in a single subject and scan. ( _f_ ) Similarity of regression weights (edge weights) as a function of amount of data. Note that units on _x_ -axis are expressed as fraction of time points in scan, where the total number of frames was 1099. ( _g_ ) Weights fit using scans from subject _s_ are better at predicting activity in held-out scans from _s_ than other subjects, _s[′]_ . In this figure, the blocks along the diagonal are 4 _×_ 4 and represent the four resting-state HCP scans. ( _h_ ) Distributions of errors in model fit, grouped by whether the model is being used to predict activity in a scan of a different subject, the held-out scan from the same subject, or one of the scans used in fitting the weights. ( _i_ ) Comparison of model errors using the observed network with a minimally wired network, one in which rows/columns were randomly reordered, and another in which time series were circularly shifted (independently across regions, scans, and subjects). ( _j_ ) Relationship of regression weights and Euclidean distance. We also identified edges whose regression weights were much stronger than expected (those above the dashed line). ( _k_ ) Distribution of regression weights across canonical brain systems. ( _l_ ) Comparison of within- and between-system regression weights. ( _m_ ): Comparison of positive and negative weights. 

gion _i_ to _j_ is identical to that of _j_ to _i_ . Also, these same measures are indirect assessments of myelination status (those note [31–34]) and not necessarily informative about synaptic efficacy or influence. 

Measures of effective connectivity also have limitations. Precedence-based measures are typically estimated between all pairs of brain regions and not restricted to those for which a structural connection exists. This is a limitation shared by causal models, as well. In the case of causal models, the space of possible network parameters 

is huge, even for very small networks. This makes fitting causal models computationally costly [35]. Although recent approaches have helped reduce this burden, making it possible to fit cortex-wide networks, scaling beyond approximately 10[2] nodes is uncommon. Even for these small networks, the computational cost remains demanding enough that investigating individual differences–i.e. fitting subject-specific models–is prohibitive [36, 37]. 

Here, we present a multi-modal, explanatory model for estimating the weights of structural connections. In the 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

3 

spirit of diffusion-/tractography-based models, ours preserves the brain’s sparse white-matter architecture. However, rather than assign structural weights based on diffusion/imaging parameters, we assign weights based on the parameters of multi-linear regression models. These models are fit independently for each region, _i_ , and predict that region’s future activity based on the weighted histories of its connected neighbors. This allows us to fit asymmetric and signed edge weights for networks of hundreds of nodes in a matter of seconds. 

Our manuscript aims to explore this model and its network properties, positioning it as an intermediate method, situated between tractography-based weighting schemes and computationally expensive inferential techniques. To this end, we find that the model predicts fMRI BOLD activity at a rate greater than chance even when using a relatively small amount of data (approximately 1% of samples). We show that the inferred edge weights exhibit subject specificity and are aligned, broadly, with known functional systems, despite the fact that edge weights exhibit imperfect alignments with interregional correlations (see Fig. S1). Further, we show that this network exhibits bilaterally symmetric, hemisphere-spanning communities and a shortest path structure that involves most edges (in contrast with streamline-weighted networks that use only 15% edges in its shortest paths backbone). Taking advantage of the directed nature of links, we find evidence of robust asymmetries in connection weights and regions’ connectivity profiles (incoming _versus_ outgoing connections). Finally, in two applications we show that the inferred edge weights systematically reconfigure during movie-watching and across the human lifespan. Collectively, these observations suggest that this model is a practical alternative to existing edge-weighting schemes, and effectively endows anatomical connections with functional properties, thereby opening up avenues for future exploration and applications. 

## **FITTING AND BENCHMARKING ASYMMETRIC, WEIGHTED, AND SIGNED STRUCTURAL CONNECTIVITY** 

Brain regions are linked to one another _via_ whitematter fiber tracts. The topology and edge weights of this network constrains interareal communication and shape patterns of spontaneous activity. Most studies set the weights of structural connections equal to microstructural properties estimated from diffusion weighted images and tractography, e.g. fractional anisotropy or streamline derivatives, or infer them using computationally demanding generative models. However, the ground truth connection weights are unknown, motivating the exploration and benchmarking of alternative weighting schemes. 

Here, we use a model-based framework for assigning weights to existing structural connections. Briefly, we follow existing modeling work [38–41] and assume that at 

time _t_ the state of region _i_ (level of fMRI BOLD activity) is a function of its neighbors’ states at time _t −_ 1 plus an offset (bias). That is: 

**==> picture [196 x 24] intentionally omitted <==**

Where Γ _i_ is region _i_ ’s connected neighbors. We use linear regression and ordinary least squares to estimate the parameters _Wji_ and _ci_ separately for each node _i_ (Fig. 1a + b). Thus, the resulting matrix _W ∈_ R _[n][×][n]_ , is sparse and preserves _exactly_ the binary structure of white-matter connectivity (Fig. 1c). However, the weights, which are obtained from regression, can take on either positive or negative valence, whereas weights are typically positive only for connectomes inferred from dMRI and tractography. We note also that this network is directed–i.e. in general, _Wij_ = _Wji_ . 

In this section, we report the results of the fitted model. That is, we describe basic features of the asymmetric, weighted, and signed connectome and contrast them with a connectome in which weights are defined using a commonly used metric–i.e. streamline density (streamline count divided by geometric mean of regional volumes) [3, 42]. 

We fit the model at the group level using pooled time series data from 95 participants from the Human Connectome Project [43] (HCP100UR, five subjects excluded due to incomplete data or quality issues) and a group-averaged binary SC matrix [44]. We found that, at the group level, the model performed well (correlation between observed and predicted activity from individual scans, _r_ = 0 _._ 76 _±_ 0 _._ 03; mean squared error, _MSE_ = 0 _._ 43 _±_ 0 _._ 05; Fig. 1d + e). We also found that the model weights stabilize with relatively few samples. Specifically, we randomly sub-sampled an equal number of frames from each participant and scan and used those frames to estimate the connection (regression) weights. We repeated this process 100 times while varying the number of samples from 2, 4, 8, 16, 32, 64, 128, 256, 512, to 1099. We found that even with approximately 6% of the total number of samples (64 samples per scan), the estimated weights achieved a correlation with the fullsample weights of _r_ = 0 _._ 993; Fig. 1f). 

Brain activity dynamics and its correlation structure are deeply individualized [45, 46]. A good model of brain activity, therefore, must also exhibit subject specificity. To assess whether model performance was, indeed, subject specific, we estimated weights using three of every subject’s four resting state scans, and used those weights to predict the activity of the held-out scan (as well as the activity of all other scans and subjects; Fig. 1g). We found that the error (mean squared error) was lower for the held-out scans than for the scans of any other subjects (two-sample _t_ -test; _p <_ 10 _[−]_[15] ; Fig. 1h). Note that here, and in all subsequent single-subject/-scan analyses, we fit edge weights using the same group-representative connectivity mask. This ensures that any differences be- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

4 

tween individuals are not driven by differences in the underlying anatomical connectivity, but driven jointly by differences in edge weights and resting brain dynamics. 

Next, we assessed whether the observed results, namely the model error, was consistent with chance. Accordingly, we compared the observed model fitness against null distributions obtained under five distinct null models [47]: 1) a _minimally wired null model_ in which only the shortest (least-costly) connections are preserved (while preserving an equal number of connections), 2) a _reordered null model_ in which nodes’ orders were randomly permuted, 3) a _“spin” model_ in which nodes’ orders were randomly permuted but geometry preserved, 4) a _topological null model_ in which nodes’ degrees (number of connections and predictors) were preserved, but edge placement randomized, and 5) a _temporal_ null model in which regional fMRI BOLD time series were circularly shifted independently for each region and scan (see **Materials and Methods** for details related to these null models). In general, we found that the error (MSE) was significantly lower using the intact data than in any of the null models (two-sample _t_ -test, _p <_ 10 _[−]_[15] ; Fig. 1i). 

Finally, we examined some of the basic properties of the weights fit at the group level. We found that both positive and negative connection weights decay monotonically with distance (Fig. 1j). However, for any given distance bin there was a range of edge weight values. Examining the most extreme (z-scored weight of _z >_ 3 relative to the other edges in the same bin), we find they are dominated by intra-hemispheric connections ( _≈_ 71). Although fewer in number, the remaining 29% of connections still exceeds the baseline rate of inter-hemispheric connections (19.5%). Next, we tested how positive and negative connections were distributed with respect to canonical brain systems [48]. We found that, within systems, connections tended to be strong and positive whereas negatively-weighted connections showed no clear preference for falling either within or between systems. Indeed, when we examine the weights of individual connections, rather than system averages, we still find that within-system weights tend to be stronger and more positive compared to between-system weights (two-sample t-test, _p <_ 10 _[−]_[15] ; Fig. 1l) and that, in general, the mean positive connection is greater than the absolute mean negative (two-sample t-test, _p <_ 10 _[−]_[15] ; Fig. 1m). 

In the supplementary material we perform several additional tests. These include assessing model performance at different lags (Fig. S2), assessing the relative contributions of long _versus_ short connections (Fig. S3), comparing the estimated edge weights with other measures of functional and structural connectivity (Fig. S1), assessing regional fitness (Fig. S4), assessing the impact of global signal regression on results (Fig. S5), confirming that the distance dependence of edge weights is preserved when we use curvilinear fiber length rather than Euclidean distance (Fig. S6), fitting edge weights with regularization (Fig. S7), and comparing the relative performance of the asymmetric, weighted, and signed ma- 

trix _versus_ the fiber density matrix in as structural constraints for dynamic, neural mass models (Fig. S8). 

In summary, we show that this simple regression framework reliably estimates structural connection weights and requires relatively few observations to do so. The inferred weights are subject-specific and result in model fitness that exceeds chance. The strongest weights are positive and concentrated within putative brain systems. Collectively, these results set the stage for further explorations of the asymmetric, weighted, and signed network and the implications of the newly defined edge weights for network analyses. 

## **MODULAR ORGANIZATION OF THE ASYMMETRIC, WEIGHTED, AND SIGNED CONNECTOME** 

One of the hallmarks of biological neural networks is that they are organized into densely connected sub-networks called “modules” or “communities” [10]. Although there is a shared correspondence between anatomical modules–defined from streamlinederived structural connectivity–and functional modules, the alignment has, historically, been inexact [49, 50]. Here, we examine the modular structure of anatomical connectivity with the newly-derived asymmetric, weighted, and signed connectome and compare its organization with the modular structure derived from a connectome in which edges are weighted based on streamline density. 

To detect communities we optimized a signed variant of the modularity quality function [51] using the Louvain algorithm [52]. The output of the algorithm is sensitive to initial conditions and was optimized 1000 times for each of the two weighting schemes. In both cases we fixed the structural resolution parameter to _γ_ = 1. We aggregated and compared these results by computing coassignment matrices for each connectome, tallying the frequency with which node pairs were assigned to the same module across all 1000 repetitions (Fig. 2a,b). For the sake of visualization, we also calculated consensus communities for each matrix (Fig. 2c,d). We then calculated the difference between the two co-assignment matrices (Fig. 2e). We found that communities in the asymmetric, weighted, and signed matrix exhibited reduced laterality [53], tending to span the cerebral hemispheres whereas communities detected using the fiber density matrix tended to be more lateralized (t-test _p <_ 10 _[−]_[15] ; Fig. 2g). We note that these observations were anticipated, given that fMRI BOLD activity was involved in the estimation of structural connection weights. 

Next, we asked whether the community structure of the asymmetric, weighted, and signed matrix was better aligned with functional connectivity (correlation structure of resting fMRI BOLD data) than the fiber density matrix and its system-level architecture. To address this question, we imposed canonical brain systems (coarse- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

5 

**==> picture [509 x 191] intentionally omitted <==**

FIG. 2. **Comparing modular structure of structural networks.** Modules are cohesive subnetworks – nodes that make more connections to other members of the same module than to other modules. Here, we compare the modular structure of network with original weights and the same network with weighted, directed, and signed edges. Here, we examine modules estimated with a fixed resolution parameter ( _γ_ = 1) but explore the multiscale modular structure in the supplement. Coassignment probability matrices for the inferred edge weight ( _a_ ) and the fiber density matrices ( _b_ ). ( _c_ and _d_ ) Consensus communities for both versions of weights. ( _e_ ) Element-wise difference in module co-assignment. ( _f_ ) System co-assignment matrix for reference. Black entries refer to pairs of brain regions that are assigned to the same system in both coarse and finescale system divisions. Gray entries are co-assigned to the same system for the coarse division, only. Comparison of laterality ( _g_ ) and modularity ( _h_ ) of detected modules. ( _i_ ) Alignment of modules with respect to coarse and fine-scale system partitions. Each point in panels _g_ - _i_ represents a partition from one of 1000 runs of the Louvain algorithm for optimizing modularity. 

and fine-scale intrinsic connectivity networks defined in [48]; Fig. 2f) on each matrix and calculated the induced modularity ( _Q[∗]_ ). We found that the asymmetric matrix exhibited greater modularity than the fiber density matrix ( _t_ -test, _p <_ 10 _[−]_[15] ; Fig. 2h). We also calculated the adjusted Rand index (ARI) between detected partitions and fine- and coarse-scale systems. ARI is a measure of partition similarity; larger values indicate that two partitions are more similar. For both the fine and coarse system partitions, we found that the ARI was greater when compared to partitions detected using the asymmetric and signed matrices than partitions detected using the fiber density matrices (two-sample _t_ -tests; maximum _p <_ 10 _[−]_[15] ; Fig. 2i). 

For completeness, we also examined the multi-scale and hierarchical organization of communities, allowing for the resolution _γ_ to vary [54] (Fig. S9). These results suggest that the asymmetric, signed, and weighted network exhibits community structure not limited to a single topological scale [55]. 

Notably, the results reported here were obtained using modularity maximization and a well-established null model [51]. We also explored an alternative “geographic” null model that has been used in network analysis of physical systems, e.g. granular materials [56–59] (details of this model are described in **Materials and Methods** ; Fig. S10). Briefly, this null model preserves the binary network architecture exactly – the same presence/absence of links as in the observed network – but as- 

signs a uniform weight across those edges. In general, we find that this null model generates results consistent with those described above, but also yields consensus communities that exhibit a striking correspondence to canonical brain systems (Fig. S11). 

Additionally, we compared the detected modules to a recently aggregated set of “brain maps” [60] – annotations of brain regions that describe properties ranging from density of receptors to the relative expansion of brain areas across development and evolution. In general, we found evidence that the modules detected using the asymmetric, weighted, and signed network were more strongly enriched for these annotations compared to modules detected in the fiber density matrix (Fig. S12). This observation was true both at the level of the entire partition, but also at the level of individual modules. 

Finally, we also repeated several of the analyses from this and the previous section using mouse anatomical connectivity data made available by the Allen Brain Institute [13] that was reprocessed and parcellated into _N_ = 182 regions of interest (see **Materials and Methods** for processing details). Unlike dMRI and tractography, these connectivity data were acquired invasively using tract-tracing and are considered the “gold standard” for mapping of anatomical connectivity. The resulting networks have some shared features in common with networks reconstructed from dMRI [11], but are also directed and hyper-dense (of the possible 32942 connections, 32936 exist; 99.98% density). In parallel, we also 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

6 

analyzed fMRI data acquired from a cohort of _N_ = 18 anaesthetized mice, with data parcellated into the same _N_ = 182 regions of interest (see **Materials and Methods** for details regarding acquisition, processing, and parcellation). In general, the results obtained using the mouse data were consistent with those reported using the human imaging data (see Fig. S13), including greater similarity between the community structure of the newly defined connectome weights and anatomically defined regions of mouse cortex. 

## **GRAPH THEORETIC PROPERTIES OF THE ASYMMETRIC, WEIGHTED, AND SIGNED CONNECTOME** 

In the previous section, we explored the modular architecture of the newly-derived asymmetric, weighted, and signed matrix, comparing it with analogous measures made on the fiber density matrix. Modular structure, however, is but one example of a network metric – it assesses a network’s organization at the “meso-scale”. However, other measures can be meaningfully applied to probe global (whole-network) and local (regional) properties. In this section, we investigate a subset of those measures. 

First, we compared shortest-paths structure. Shortest paths in weighted networks refer to the least-costly route from a source node, _s_ , to a target node, _t_ . Typically, the length or cost of a shortest path is interpreted as a measure of communication capacity [61]; networks where the average shortest path is low (or the average reciprocal shortest path is large) are considered better-suited for communication. 

To detect shortest paths we first mapped weights to costs. In the fiber density matrix, this mapping was accomplished by taking the reciprocal of an edge’s weight ( _cost_ = _weight_ 1[)][before][applying][a][shortest][paths][algo-] rithm. In the directed and signed network, however, we performed an additional step to rectify edge weights as the shortest paths algorithm is not compliant with negative edges. Briefly, we subtracted _min_ ( _βij_ ) and added _ε_ to every edge, where _min_ ( _βij_ ) = _−_ 0 _._ 43 is the smallest (most negative) weight among all edges weights and _ε_ = 0 _._ 0027 was the weight of the weakest edge in the fiber density network. This transformation ensures that all existing white-matter edges have weights that are nonzero and positive. Following this transformation, we used the reciprocal transform to map weights to cost. 

The shortest paths matrices for both networks are shown in Fig. 3a,b. Strikingly, the number of steps in the least-costly paths was much greater for the fiber density matrix than for the asymmetric, weighted, and signed network (Fig. 3e,f). This likely is a consequence of the heavy-tailed fiber density distribution; because a small number of connections exhibit orders of magnitude stronger weights than the others, the cost of including those edges in shortest path is exceptionally small. 

From the perspective of the shortest paths algorithm, it is optimal to direct paths through these ultra low-cost edges, possibly even at the expense of direct connections [11, 62]. Further evidence for this claim comes from the shortest paths usage; in the fiber density matrix, the fraction of edges that are used in at least one shortest path is only 14.2% (Fig. 3c,d), whereas in the asymmetric, weighted, and signed networks, 97.5% of all edges get used at least once (Fig. 3). 

The signed nature of the network means that we can also examine and compare properties of positive and negative edges to one another. That is, we can construct two versions of the same network: one in which nodes are linked _via_ positive connections only and another with negative connections. Interestingly, we find that the positive network exhibits greater local clustering (paired sample _t_ -test, _p <_ 10 _[−]_[15] ; Fig. 3i). That is, positive connections tend to form dense triangles and cliques around nodes at a greater rate than negative connections. Additionally, we find that nodes’ positive weighted degrees (total weight of all incident positive connections) exceeds that of their negative strength (Fig. 3j). 

In summary, we calculate a series of network statistics and show that their values differ, sometimes dramatically, depending on whether we weight edges using our regression-based framework or using more traditional diffusion/imaging parameters. In some specific cases, we find that statistics calculated on the asymmetric, weighted, and signed network are better aligned with our intuition about network function than statistics calculated based on fiber density. Collectively, these results underscore the impact of user decisions on network properties and our interpretation of network organization and function. 

## **ASYMMETRIES IN CONNECTION WEIGHTS** 

Due to technological limitations, structural connection weights estimated _in vivo_ using diffusion imaging and tractography methods lack directionality–i.e. _Wij_ = _Wji_ . Here, however, the regression framework we use allows for asymmetries, such that the weights of incoming and outgoing connections can deviate from one another. In this section, we describe a select set of asymmetries in greater detail. 

We measured asymmetry using a simple statistical test. Specifically, we identified pairs of regions whose weights were consistently asymmetric across 95 Human Connectome Project participants. This involved fitting weights independently for each subject and edge, and for every pair of nodes _i_ and _j_ , identifying connections where the distribution of asymmetry values, _Wij − Wji_ , excluded zero (false discovery rate fixed at _q_ = 0 _._ 05 resulting in _padj_ = 0 _._ 015; Fig. 4a,b) [63]. We found that, of 29024 possible connections, 8850 (approximately 30%) exhibited significant asymmetries. 

Next, we asked whether edges whose weights were sig- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

7 

**==> picture [509 x 183] intentionally omitted <==**

FIG. 3. **Network statistics for signed, weighted, and asymmetric matrix.** ( _a_ ) Path length (number of steps) between all pairs of nodes derived from the fiber density matrix ( _Cij_ = _W_ 1 _ij_[).][(] _[b]_[)][Path][length][for][new][matrix][(] _[C][ij]_[=] _Wij_ +1+1 _ε_[).][(] _[c]_[)] Edge usage matrix for fiber density network. ( _d_ ) Edge usage matrix for new matrix. Panels _e_ , _f_ , and _g_ compare percentage of edges used in shortest paths, characteristic path length, and network efficiency between matrices. Panels _h_ and _i_ compare local clustering and strength (weighted degree) between the two matrices. We grouped edges into percentiles (deciles; lowest deciles include negative weights) based on their weights and calculated how frequently edges in each decile are involved in shortest paths. Panel _j_ depicts the breakdown of edge usage by decile–e.g. top decile accounts for 33% of edges used on shortest paths. 

**==> picture [509 x 190] intentionally omitted <==**

FIG. 4. **Asymmetries of influence between brain regions as assessed by inferred structural weights.** ( _a_ ) Significant asymmetries, and ( _b_ ) absolute value of significant asymmetries were reorganized into system by system matrices ( _c_ ) and ( _d_ ) respectively. Note the increased absolute asymmetries within functionally defined systems in panel ( _d_ ). As illustrated in the schematic in panel ( _e_ ) next we measured in/out similarity as the correlation between incoming and outgoing weights per region. ( _f_ ) Here we show an example of in/out similarity plotted to the brains surface. ( _g_ ) Finally, we plot the per-system distribution of in/out similarity values across subjects. Boxplots on the right divide these systems into unimodal and heteromodal regions to show that there is more in/out similarity in unimodal systems. 

nificantly asymmetric were preferentially concentrated within or between specific brain systems (Fig. 4c,d). To assess whether this was the case, we created a “mask” of edges that exhibited statistically significant asymmetries and aggregated (summed) these connections within and between every pair of systems. We performed this procedure first using the signed difference in edge weights 

and again using the absolute difference. These summed values were compared against a null distribution generated _via_ a geometry-preserving null model [64]. We found that a number of system pairs exhibited greater than expected asymmetries, including connections that fall within control, default, and visual networks (ContC, DMNa, DMNc, central visual), as well as connections 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

8 

that fall between systems (ContC-DMNa, DMNa-DMNb, temporo-parietal and both ContC and DMNa, central visual and SMNb, and peripheral visual with DANb). 

As a second measure of asymmetry, we compared the weights of nodes’ incoming and outgoing connection profiles – the extent to which its activity is predicted by _versus_ predicts the activity of its neighbors. To do this, we calculated the linear product-moment correlation between vectors associated with row and column _i_ in the asymmetric, weighted, and signed connectivity matrix (Fig. 4e). This procedure resulted in a single similarity score (correlation) for each brain region. In general, we found that in-out similarity was region-specific and varied between putative brain systems (Fig. 4f), with regions in sensorimotor systems exhibiting greater in/out similarity (Fig. 4g). Indeed, when we grouped systems based on unimodal (visual + somatomotor) and heteromodal (all other systems) labels, we found that unimodal systems exhibited greater similarity (two-sample _t_ -test, _p <_ 10 _[−]_[15] ; Fig. 4h). 

As a final test, we also identified node pairs, _i_ and _j_ , where sign( _Wij_ ) = sign( _Wji_ ) (Fig. S14). We performed this analysis at the level of individual subjects and calculated the proportion of edges with an asymmetry of sign that fall either within or between brain systems (Fig. S14a). We repeated this analysis for every individual and found that between-system edges were more likely to exhibit an asymmetry of sign than within-system edges (two-sample _t_ -test, _p <_ 10 _[−]_[15] ; Fig. S14b). 

Collectively, these results suggest that local asymmetries are well circumscribed by canonically defined brain systems. Additionally, our results suggest that asymmetry in regional incoming and outgoing connection weights run along a unimodal-heteromodal axis. 

## **WEIGHTS ARE MODULATED BY STATE** 

In the previous sections we validated and characterized structural networks whose edge weights were fit using a regression-based procedure. In those sections, all weights were fit to maximize the correspondence of predicted and observed activity during the resting-state. Here, we assess whether weights estimated at rest are dissociable from those estimated during movie-watching. 

To address this question, we used resting-state and movie-watching data from the Human Connectome Project’s 7T dataset, focusing on a subset of 117 participants whose data passed quality checks and for whom all four scans were available. Using the same SC binary mask, we fit edge weights at the group level, pooling data across all subjects and scans to generate two asymmetric, weighted, and signed matrices: one based on resting-state and the other based on movie-watching data (Fig. 5a,b). In parallel, we also fit models at the level of individual subjects, pooling scans from the same subject to generate estimates of resting-state and moviewatching edges weights. In both cases, we found com- 

parable performance (mean squared error) between both rest and movie data, with movies exhibiting slightly better performance than resting state (paired sample _t_ -test; subject-level, _p <_ 10 _[−]_[15] ; group-level _p_ = 1 _._ 2 _×_ 10 _[−]_[12] ; Fig. 5f-h). 

First, we calculated the difference between edge weights for each subject and averaged the differences across subjects (Fig. 5c,d). At each edge, we performed a paired-sample _t_ -test on the differenced edge weight distributions. We found that, out of _m_ = 29204 total edges, 2463 exhibited significant state-dependent differences (multiple comparisons controlled for by fixing false discovery rate at _q_ = 0 _._ 01 and adjusting the critical _p_ - value, _padj_ = 8 _._ 5 _×_ 10 _[−]_[4] ). Although these edges were distributed across the entire brain, they were significantly concentrated within a small subset of systems (Fig. 5e; dashed black borders around system blocks). Specifically, we found significant system-level effects within central and peripheral visual networks, from edges in the central visual network to the peripheral visual network (but not _vice versa_ , and from the dorsal attention network (DANa) to the central visual network (spin test, false discovery rate fixed at _q_ = 0 _._ 01, _padj_ = 1 _._ 6 _×_ 10 _[−]_[4] ). 

Projected into anatomical space, we find that, as expected, the connections that differ from rest to moviewatching tend to involve regions in visual networks (Fig. 5i). Interestingly, there are approximately as many connections whose weights increase from rest to movies as there are those that decrease, an effect that holds both within the visual networks (241 increases _versus_ 218 decreases) but also across the entire brain (1292 increases _versus_ 1171 decreases). 

## **DIFFERENCES IN THE WEIGHTED, SIGNED, AND DIRECTED CONNECTOME ACROSS THE HUMAN LIFESPAN** 

To this point, we have estimated the weights of asymmetric, weighted, and signed structural connections, described properties of the resulting network, exposed asymmetries in connections’ weights, and demonstrated that the weights are systematically modulated by task (rest _versus_ movie). In this section, we investigate individual differences in connections’ weights and associate them with differences across the human lifespan (7-85 years). 

To do so, we used data from the Nathan Kline Institute’s enhanced Rockland Sample [65], which included both diffusion weighted and functional MRI data for _N_ = 542 participants. In-scanner head movement is known to vary systematically with age. To address motion-related concerns, we adopted the same conservative procedure as reported in Esfahlani _et al._ [66] for motion censoring. Specifically, for each of the remaining subjects, we dropped frames in which motion exceeded a pre-defined threshold ( _FD >_ 0 _._ 15 mm). We also dropped time points that were within two frames 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

9 

**==> picture [509 x 217] intentionally omitted <==**

FIG. 5. **Comparing matrices fit to resting-state and movie-watching data.** We analyzed 7T data from 117 participants in the Human Connectome Project. Using the same binary mask as in the previous sections, we fit edge weights for both conditions at the group level (pooling time series data across all subjects/scans) and individual level (pooling data from the same subjects). Weights for ( _a_ ) group-level movie-watching state matrix and ( _b_ ) group-level resting-state matrix. Panels _c_ and _d_ show the difference in edge weights (movie minus rest); rows and columns in panel _c_ are ordered identically to panels _a_ and _b_ , whereas in panel _d_ rows and columns are reordered by brain systems. ( _e_ ) The average weight across existing connections between every pair of systems. Here, weights were squared prior to averaging. Panels _f_ and _g_ depict two-dimensional histograms of observed and predicted activity. ( _h_ ) Model fitness when fit to pooled, group-level data ( _left_ ) and individual data ( _right_ ). ( _i_ ) Edges whose difference between movie and rest are significantly greater or less than zero plotted in anatomical space. ( _j_ ) Differences in functional connectivity (FC) between movie and rest for both the observed data ( _left_ ) and the predicted ( _right_ ). 

of any supra-threshold frame or failed for form a contiguous sequence of five frames or more. Following this procedure, we excluded any participant for whom the fraction of retained frames was fewer than 50% of their total number of frames. Collectively, these procedures left _N_ = 474 participants with high-quality (low-motion) data for further analysis. 

For each subject, we used the regression-based framework to fit weights to every structural connection, generating subject-specific asymmetric, weighted, and signed matrices. Note that, here, we restricted every subject to have the same binary set of consensus edges estimated from subjects aged 18-35 years; only edges’ weights varied across individuals. Prior to calculating age-related differences, we regressed out of each edge the following variables: sex (binary variable), gray matter volume, mean framewise displacement of all “low-motion” frames, and number of frames dropped due to motion contamination. Finally, using the residuals from this procedure, we calculated their linear product-moment correlation with subjects’ biological ages resulting in a (sparse) matrix of age-related correlations (Fig. 6a). For the sake of visualization, we show subsets of edges that pass uncorrected statistical tests (Fig. 6g-i). 

Previous studies have found that age-related differences in functional connectivity respect putative system boundaries [67–69]. Accordingly, we performed statis- 

tical tests at the level of systems [48]. Specifically, we calculated the mean correlation of all edges that fell between/within every pair of systems. We then compared these observed values with null distributions generated using “spin tests” (1000 repetitions). System pairs for whom the observed correlation exceeded that of the null were considered statistically significant (false discovery rate fixed at _q_ = 0 _._ 05; _padj_ = 0 _._ 0088). In line with previous work, we found that age-related decreases in connection weight tended to concentrate within brain systems, whereas between-system weights were, generally, centered around a value of zero (two-sample _t_ -test, _p_ = 7 _._ 65 _×_ 10 _[−]_[13] ; Fig. 6b-f). More specifically, at the coarse level, we found that connections within the somatomotor network significantly decreased their weight with age while connections from the default mode to the control network increased (Fig. 6b). The finer scale allowed us to better localize those effects while also discover new age-related differences. In particular, we found significant increases in connection weight from default mode B to control B, as well as an increase in connection weights from dorsal attention network A to the central visual module – an effect that had been previously obscured at the coarse scale. We also detected significant decreases in connection weight with age, concentrated within somatomotor network B, as well as previously undetected decreases within dorsal attention net- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

10 

**==> picture [509 x 181] intentionally omitted <==**

FIG. 6. **Age-related differences in inferred structural weights are more common within functional brain systems.** ( _a_ ) Edge level correlations with age. ( _b_ and _c_ ) Matrices of significant results for the coarse- and fine-scale system spin tests, respectively.( _d_ and _e_ ) Boxplots comparing the z-scores from the spin-test null model with the real values. One boxplot displays within system z-score values, and the other displays between system z-score values. ( _f_ ) Within-system z-scores from the finescale system spin test mapped onto cortical parcels. Panels _g_ - _i_ show individual edges that exhibit age-related correlations ( _p <_ 0 _._ 05; uncorrected). Blue and red edges correspond to edges whose weights decrease or increase with age, respectively. Panels _g_ - _i_ are presented for the sake of visualization only. 

work A, salience/ventral attention network A, and from the temporo-parietal network to default mode C. 

Altogether, these findings recapitulate well-known age effects that had been previously reported using functional connectivity data. However, our approach grounds these effects in anatomical connectivity, forming a multi-modal bridge between studies of anatomical and functional agerelated differences and opening up avenues for future applied studies. 

## **DISCUSSION** 

The “correct” weighting of structural connections is not known. Most strategies for assigning edge weights do so based on microstructural or tractographic parameters. Though commonly used, the values of these parameters are, in general, misaligned with the interpretation that weights reflect the efficacy of inter-regional communication. Alternatively, a number of groups have proposed using measures of “effective” or “directed” connectivity, in which edge weights correspond to the magnitude of directed influence in a (biophysical) generative model of brain activity. However, due to computational complexity this approach is limited to applications involving small networks. Additionally, although fitting effective connections can be restricted to only those edges for which white-matter tracts were traced, most models are generally unconstrained and can place effective connections between disconnected brain regions. In short, there exists a plurality of methods for determining the weights of structural connections and the dominant methods each have specific strengths and weaknesses. 

Here, we explored a simple regression-based model for endowing reconstructed fiber tracts with directionality and a signed weight. Benchmarking this method on Human Connectome Project data, we found that the model fit observed data well, outperforming a suite of null models. The estimated weights were highly reliable even when fit using relatively few training samples and exhibited marked subject specificity. We next analyzed the resulting network using tools from network neuroscience. These analyses revealed communities that spanned cerebral hemispheres and mapped clearly onto known functional systems. Almost every edge in this network was involved in at least one shortest path. We also found evidence of asymmetric weights, network reconfiguration during naturalistic movie watching, and age-related differences. We note that unlike biophysical and dynamic causal models, our weighting scheme is not generative– i.e. it cannot be used to generate new synthetic data. It is, however, explanatory and represents a means of weighting fiber tracts that is distinct from those most frequently used in network neuroscience. Collectively, the proposed framework presents opportunities for multiple follow-up studies and applications in other neuroscience disciplines. 

## **A new weighting scheme yields unique insights into brain network function** 

Over the past two decades, network neuroscience has led to a number of discoveries about the organization of brain networks. These include small-worlds [8], hubs [3] and rich clubs [9], modules and communities [10], and 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

11 

cost-efficient wiring [70]. These “canonical” findings have been observed not only in human brain networks reconstructed at the macroscale, but have been reported across phylogeny and at all spatial scales [71]. 

Despite this preponderance of converging evidence, the specifics of these findings often depend critically on whether or not to weight edges and the precise measure used. Consider the prototypical “small world” model of the brain, where long-distance edges are thought to represent shortcuts that allow signals to propagate long distances in relatively few hops. Although both weighted and binary networks exhibit small-world properties– relatively short path length and strong local clustering– when edges are weighted based on streamline density, the strong distance-dependence of streamlines ensures that virtually no long-distance connections are included in the network’s shortest path structure [11]. 

The example cited above represents just one instance where a processing decision (whether and how to weight structural connections) leads to different interpretations of brain network function, _vis a vis_ role of long-distance connections in interareal communication. Interestingly, we make a similar observation here; when edges are weighted with regression coefficients and their signs rectified, we recover a shortest path structure in which most edges contribute to at least one shortest path and modules that are now better aligned with functional brain systems[72]. Our work even presents challenges for how we define connectomes [73]. When we refer to the connectome, we often imagine an enumerable and finite set of neural elements and connections [1, 74]. Here, however, edge weights are context dependent, impermanent, and vary with task/cognitive state. Essentially, the structural edges inherit features usually reserved for functional connections, placing our approach slightly at odds with the perspective that structural connections are fixed over short timescales (duration of typical scan session). 

More importantly, the secrets of the connectome are far from unlocked. Existing data and methods have not unambiguously mapped structure to function, for example whether graph-theoretic measures can unveil functional properties of a brain (and which properties, specifically) is not clearly elucidated, and, although many studies have identified statistical associations between network properties and clinical, cognitive, behavioral, and developmental markers, the mechanisms that underlie those associations are largely unknown. Collectively, this motivates further neuroscientific exploration, both of new data/connectivity modalities [75] and experimental paradigms, as well as methodological frameworks. 

## **A network bridge between anatomical and functional connectivity** 

The edge-weighting scheme that we explore here can be used to help understand one of the central questions of network neuroscience: how does the brain’s anatomi- 

cal connectivity constrain its function? Past studies have established a link between structural and functional connectivity [49]. Empirical findings have shown that insults to structural connections cause acute loss or reorganization of functional connectivity [76]. Even in intact brains, structural connection weights are correlated with their functional analogs and pairs of brain regions that are connected directly or _via_ few processing steps have proportionally stronger FC [3]. In parallel, _in silico_ dynamical systems models have used anatomical connectivity to constrain simulated brain activity [77, 78], generating synthetic fMRI data whose correlation structure can be compared with empirical FC or analytic estimates of interregional communication capacity [61, 79]. 

Here, rather than compare SC to FC, we incorporate functional information directly into the estimates of edge weights [80]. This process generates a singular network object whose fitness (a metric that, itself, can be interpreted as a measure of structure-function coupling) can be estimated globally as the total error between observed and predicted activity [81] or parsed into local (regional) error terms, analogous to recent approaches for linking anatomical and functional connectivity weights [66, 82]. We note however, that this approach is also distinct from most studies that report structure-function correspondence, in that we seek a set of parameters that maximizes that correspondence, whereas most studies report a correlation between functional data (FC or activity) and structural networks and their derivatives [83]. 

Here, we explore this alternative approach for tracking changes in structure-function correspondence in two contexts: comparing edge weights between rest and moviewatching conditions and identifying differences in edge weight across the human lifespan. 

We find robust reconfiguration of edge weights during movie-watching. This observation is not new–a seemingly limitless number of studies have reported task- or state-induced changes in connection weights [84–87]. In these studies, however, it is the functional connections whose weights change, making it difficult to assess which structural connection facilitate those changes. Our approach addresses this issue directly; changes in regression weights at each structural edge allow for the formulation of targeted hypotheses about the roles of specific fiber tracts in a given task. 

## **Possible advantages of an asymmetric, weighted, and signed connectome** 

Throughout the study, we compare properties of the asymmetric, weighted, and signed network with a network in which edge weights represent fiber densities – a more traditional measure of structural connectivity. In general (and unsurprisingly), the properties of these networks are often dissimilar. That is, how we choose to weight a network’s edges can change its graph-theoretic profile and impact how we might interpret its func- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

12 

tion. Although we remain agnostic as to which weighting scheme is “superior”, we note that the asymmetric network both outperforms the fiber density network on a number of applications, and has properties that are better aligned with intuition. 

For instance, we find that the modular structure of the asymmetric network tends to be less lateralized– i.e. modules are more likely to contain nodes from both hemispheres–than the fiber density network. This observation suggests that the reweighting of the network helps circumvent one of the peculiarities (or limitations) of community-detection methods applied to structural brain networks. Namely, because fiber densities and weights derived from tract-tracing experiments tend to be heavy-tailed and distance-dependent [11, 42] and because long-distance interhemispheric tracts are notoriously challenging to reconstruct from diffusion imaging data [88, 89], communities tend to be spatially contiguous and exhibit poor correspondence with systems/communities derived from functional recordings [49]. 

Additionally, we take advantage of recent advances in neuroinformatics to compare communities with brain maps–i.e. the regional or vertex-wide expression of genetic, transcriptomic, evolutionary, and developmental markers. We find that communities obtained from the asymmetric network tend to be significantly enriched for many of these markers to an extent above and beyond the communities obtained from the fiber density matrix. These observations suggest that the multi-modal network generated by endowing structural connections with functionally-relevant information tightens the link between network organization and brain-based markers. 

## **Interpreting signed edges in macroscale connectome** 

One of the unique features of the networks we construct here is that, unlike connectomes whose weights are determined based on microstructural/diffusion/tractography parameters, we obtain weights that are signed (can take on positive or negative values). How do we interpret this feature? What are possible underlying neurophysiogical mechanisms that explain the emergence of signed edges in large-scale networks? 

At its core, the edge weights estimated here are statistical constructs; a negative weight from node _i_ to _j_ indicates that when the activity of _i_ increases, the activity of _j_ tends to decrease proportionally at the next time point. This statistical interpretation is in line with other frameworks for estimating effective connections [90]. Although it is tempting to ascribe “excitatory” and “inhibitory” labels to positive and negative edge weights, this terminology is typically reserved for cell-to-cell projections and, more specifically, pyramidal cells and interneurons, respectively. In general, the neurochemical (e.g. glutamate/excitatory and GABA/inhibitory) contributions to the diffusion MRI and fMRI BOLD signal are not easily 

## parsed. 

However, we can speculate about possible underlying mechanisms that support signed edges in large-scale networks. One possible explanation involves feed-forward or feedback inhibition [91], whereby excitatory interregional connections cause inhibition in their target region either by directly exciting local inhibitory interneurons, or by exciting local interneurons indirectly through connecting pyramidal cells. Indeed, recent studies have suggested that the balance of glutamate/GABA underlies the antagonistic (anti-correlated) activity of large-scale brain systems [92]. 

Irrespective of the underlying cause, the signed edges in the networks constructed here exhibit nonrandom organization in terms of their distribution across canonical brain systems and relationship to other network/geometric measures–e.g. clustering coefficient and fiber length. These features, of course, have implications for traditional network analyses and may require new methodologies in some cases. For instance, interregional communication models rely on shortest paths and diffusion dynamics to estimate communication efficacy [61]. However, these dynamics are not well-defined for networks with signed edges. Here, we circumvent this issue by offsetting edge weights, forcing negative connections to have small (but positive) values. However, there are likely many alternative strategies that embrace the signed and asymmetric nature of edges that could be explored in future studies [93]. 

## **Limitations** 

This study has a number of limitations. Most notably, the primary results rely on the use of diffusion weighted MRI and tractography for reconstructing white-matter tracts. Although these methods are still used widely, they have well-documented drawbacks and biases that call into questions the verisimilitude of structural connectivity networks [94, 95]. We partially mitigate these concerns by replicating our findings using tract-tracing data made available through the Allen Brain Institute [13]. Unlike tractography, in which anatomical connections are inferred non-invasively, antero-/retrograde tract-tracing is considered the gold standard mapping large-scale connectivity [96]. We expect that advances in imaging, tractography algorithms [97, 98], and better alignment of multi-scale datasets will narrow the gap between tracttracing and tractography in future studies [99]. 

Another possible limitation of the current study is its focus on neocortex only. Doing so necessarily ignores contributions from subcortical and cerebellar regions when modeling node-level time series. Adding additional regions is not computationally prohibitive and in principle could be addressed easily. However, new connections mean including additional explanatory terms in each regional multi-linear model and will, in general, lead to new estimates of edges’ weights. That is, the regression 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

13 

coefficients will vary with additional observations (new data) or new nodes. Future studies should investigate this explicitly. 

## **Future directions** 

Our study presents a number of opportunities for future studies. Among the most obvious and tantalizing opportunities is the empirical validation of edge weights estimated here. Datasets in which stimulation is paired with brain-wide recordings make it feasible to estimate directed influence between brain stimulus-target pairs of regions [100, 101]. These estimates could be compared directly to the connection weights inferred here. Relatedly, modeling studies have reported whole-brain effective connectivity [36] and asymmetries in communication patterns [63]. Here, we focused on characterizing properties of the network generated using our regression-based framework and contrasting it with a network of edges weighted based on fiber density; careful comparisons of this technique to extant, already-established methods should be carried out in the future. 

Our preliminary findings using movie-watching data suggest that our weighting scheme may be suitable for detecting state-specific changes in structural connection weights. Future studies should explore the sensitivity of this approach for other state-based comparisons. We note that, unlike unthresholded functional connectivity, which, when used in a brain-wide association or casecontrol study results in _N_ ( _N −_ 1) _/_ 2 comparisons, our approach results in much fewer connections [102]. Statistical tests only need to be performed for existing structural connections, possibly increasing the statistical power of these types of studies [103]. Additionally, while the edges we weight are structurally-defined and reflect best estimates of white-matter topology, we endow them with functionally relevant edge weights (derived from fMRI BOLD data). The multi-modal nature of this edgeweighting scheme may, in actuality, situate our approach somewhere between functional and anatomical connectivity. That is, it achieves what resting-state FC sometimes is assumed to be; namely, a functionally informative measure of anatomically connectivity [104]. 

Brain-wide association studies are familiar analyses in network neuroscience. In these studies, inter-individual variation in demographic, phenotypic, clinical, or behavioral data is associated with neural elements – usually node- or edge-level properties. In general, these types of studies are underpowered to detect small effect [102, 103]. This issue is especially problematic when tests are performed at the level of edges – for a network of _N_ nodes, this means performing _N_ ( _N −_ 1) _/_ 2 tests – which requires stringent corrections to control for multiple comparisons. Our approach may partly circumvent this issue (or at least reduce its severity); because anatomical connectivity is, in general, sparse, even if a statistical test is carried out at every edge, the total number of tests is far smaller 

than the upper limit. With fewer tests, the correction for multiple comparisons is less severe, potentially making it possible to resolve smaller effects. 

## **MATERIALS AND METHODS** 

In this section, we describe all four datasets that we analyzed. Briefly, they include three human MRI datasets: two from the Human Connectome Project and another from the Nathan Kline Institute. In addition, we also analyzed tract-tracing and functional MRI data from mice. 

## **Datasets: Human Connectome Project 3T resting-state and diffusion weighted MRI** 

The Human Connectome Project (HCP) 3T dataset [43] consists of structural magnetic resonance imaging (T1w), functional magnetic resonance imaging (fMRI), and diffusion magnetic resonance imaging (dMRI) young adult subjects, some of which are twins. Here we use a subset of the available subjects. These subjects were selected as they comprise the “100 Unrelated Subjects” released by the Connectome Coordination Facility. After excluding data based on completeness and quality control (4 exclusions based on excessive framewise displacement during scanning; 1 exclusion due to software failure), the final subset included 95 subjects (56% female, mean age = 29.29 _±_ 3.66, age range = 22-36). The study was approved by the Washington University Institutional Review Board and informed consent was obtained from all subjects. 

A comprehensive description of the imaging parameters and image prepocessing can be found in [105]. Images were collected on a 3T Siemens Connectome Skyra with a 32-channel head coil. Subjects underwent two T1weighted structural scans, which were averaged for each subject (TR = 2400 ms, TE = 2.14 ms, flip angle = 8 _[◦]_ , 0.7 mm isotropic voxel resolution). Subjects underwent four resting state fMRI scans over a two-day span. The fMRI data was acquired with a gradient-echo planar imaging sequence (TR = 720 ms, TE = 33.1 ms, flip angle = 52 _[◦]_ , 2 mm isotropic voxel resolution, multiband factor = 8). Each resting state run duration was 14:33 min, with eyes open and instructions to fixate on a cross. Subjects underwent 14 task fMRI scans over a two-day span. The fMRI data was collected with the same sequence parameters as the resting state fMRI. The fMRI runs consisted of working memory (5:01 min, 405 frames), gambling (3:12, 253), motor (3:34, 284), language (3:57, 316), social cognition (3:27, 274), relational processing (2:56, 232), and emotional processing (2:16, 176) tasks. Finally, subjects underwent two diffusion MRI scans, which were acquired with a spin-echo planar imaging sequence (TR = 5520 ms, TE = 89.5 ms, flip angle = 78 _[◦]_ , 1.25 mm isotropic voxel resolution, b-vales = 1000, 2000, 3000 s/mm[2] , 90 diffusion weighed volumes for each shell, 18 b = 0 vol- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

14 

umes). These two scans were taken with opposite phase encoding directions and averaged. 

Structural, functional, and diffusion images were minimally preprocessed according to the description provided in [105], as implemented and shared by the Connectome Coordination Facility. Briefly, T1w images were aligned to MNI space before undergoing FreeSurfer’s (version 5.3) cortical reconstruction workflow, as part of the HCP Pipeline’s PreFreeSurfer, FreeSurfer, and PostFreeSurfer steps. Functional images were corrected for gradient distortion, susceptibility distortion, and motion, and then aligned to the corresponding T1w with one spline interpolation step. This volume was further corrected for intensity bias and normalized to a mean of 10000. This volume was then projected to the 2mm _32k_ ~~_f_~~ _s_ ~~_L_~~ _R_ mesh, excluding outliers, and aligned to a common space using a multi-modal surface registration [106]. The resultant cifti file for each HCP subject used in this study followed the file naming pattern: `*` ~~`A`~~ `tlas MSMAll hp2000` ~~`c`~~ `lean.dtseries.nii` . These steps are performed as part of the HCP Pipeline’s fMRIVolume and fMRISurface steps. Each minimally preprocessed fMRI was linearly detrended, band-pass filtered (0.008-0.008 Hz), confound regressed and standardized using Nilearn’s `signal.clean` function, which removes confounds orthogonally to the temporal filters. The confound regression strategy included six motion estimates, mean signal from a white matter, cerebrospinal fluid, and whole brain mask, derivatives of these previous nine regressors, and squares of these 18 terms. Spike regressors were not applied. Following these preprocessing operations, the mean signal was taken at each time frame for each node, as defined by the Schaefer 200 parcellation [48] in _32k_ ~~_f_~~ _s_ ~~_L_~~ _R_ space. Diffusion images were normalized to the mean b0 image, corrected for EPI, eddy current, and gradient non-linearity distortions, and motion, and aligned to subject anatomical space using a boundary-based registration as part of the HCP pipeline’s Diffusion Preprocessing step. In addition to HCP’s minimal preprocessing, diffusion images were corrected for intensity non-uniformity with `N4BiasFieldCorrection` [107]. The Dipy toolbox (version 1.1) [108] was used to fit a multi-shell multi-tissue constrained spherical deconvolution [109] to the data with a spherical harmonics order of 8, using tissue maps estimated with FSL’s `fast` [110]. Tractography was performed using Dipy’s `Local Tracking` module [108]. Multiple instances of probabilistic tractography were run per subject [111], varying the step size and maximum turning angle of the algorithm. Tractography was run at step sizes of 0.25 mm, 0.4 mm, 0.5 mm, 0.6 mm, and 0.75 mm with the maximum turning angle set to 20 _[◦]_ . Additionally, tractography was run at maximum turning angles of 10 _[◦]_ , 16 _[◦]_ , 24 _[◦]_ , and 30 _[◦]_ with the step size set to 0.5 mm. For each instance of tractography, streamlines were randomly seeded three times within each voxel of a white matter mask, retained if longer than 10 mm and with valid endpoints, following Dipy’s implementation of 

anatomically constrained tractography [112], and errant streamlines were filtered based on the cluster confidence index [113]. For each tractography instance, streamline count between regions-of-interest were normalized by dividing the count between regions by the geometric average volume of the regions. Since tractography was run nine times per subject, edge values were collapsed across runs. To do this, the weighted mean was taken with weights based on the proportion of total streamlines at that edge. This operation biases edge weights towards larger values, which reflect tractography instances better parameterized to estimate the geometry of each connection. 

## **Datasets: Human Connectome Project 7T resting-state and movie-watching data** 

The Human Connectome Project (HCP) 7T dataset [43] consists of structural magnetic resonance imaging (T1w), resting state functional magnetic resonance imaging (rsfMRI) data, movie watching functional magnetic resonance imaging (mwfMRI) from 184 adult subjects. These subjects are a subset of a larger cohort of approximately 1200 subjects additionally scanned at 3T. Subjects’ 7T fMRI data were collected during four scan sessions over the course of two or three days at the Center for Magnetic Resonance Research at the University of Minnesota. Subjects’ 3T T1w data collected at Washington University in St. Louis. The study was approved by the Washington University Institutional Review Board and informed consent was obtained from all subjects. 

We analyzed MRI data collected from _Ns_ = 129 subjects (77 female, 52 male), after excluding subjects with poor quality data. Our exclusion criteria was as follows: where each spike is defined as relative framewise displacement of at least 0.25 mm, we excluded subjects who fulfill at least 1 of the following criteria: greater than 15% of time points spike, average framewise displacement greater than 0.2 mm; contains any spikes larger than 5mm. Following this filter, subjects who contained all four scans were retained. At the time of their first scan, the average subject age was 29 _._ 36 _±_ 3 _._ 36 years, with a range from 22 _−_ 36. 70 of these subjects were monozygotic twins, 57 where non-monozygotic twins, and 2 were not twins. 

A comprehensive description of the imaging parameters and image preprocessing can be found in [105] and in HCP’s online documentation ( `https:// www.humanconnectome.org/study/hcp-young-adult/ document/1200-subjects-data-release` ). T1w were collected on a 3T Siemens Connectome Skyra scanner with a 32-channel head coil. Subjects underwent two T1-weighted structural scans, which were averaged for each subject (TR = 2400 ms, TE = 2.14 ms, flip angle = 8 _[◦]_ , 0.7 mm isotropic voxel resolution). fMRI were collected on a 7T Siemens Magnetom scanner with a 32channel head coil. All 7T fMRI data was acquired with a 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

15 

gradient-echo planar imaging sequence (TR = 1000 ms, TE = 22.2 ms, flip angle = 45 _[◦]_ , 1.6 mm isotropic voxel resolution, multi-band factor = 5, image acceleration factor = 2, partial Fourier sample = 7/8, echo spacing = 0.64 ms, bandwidth = 1924 Hz/Px). Four resting state data runs were collected, each lasting 15 minutes (frames = 900), with eyes open and instructions to fixate on a cross. Four movie watching data runs were collected, each lasting approximately 15 minutes (frames = 921, 918, 915, 901), with subjects passively viewing visual and audio presentations of movie scenes. Movies consisted of both freely available independent films covered by Creative Commons licensing and Hollywood movies prepared for analysis [114]. For both resting state and movie watching data, two runs were acquired with posterior-to-anterior phase encoding direction and two runs were acquired with anterior-to-posterior phase encoding direction. 

Structural and functional images were minimally preprocessed according to the description provided in [105], as implemented and shared by the Connectome Coordination Facility. Briefly, T1w images were aligned to MNI space before undergoing FreeSurfer’s (version 5.3) cortical reconstruction workflow, as part of the HCP Pipeline’s PreFreeSurfer, FreeSurfer, and PostFreeSurfer steps. 7T fMRI images were downloaded after correction and reprocessing announced by the HCP consortium in April, 2018. fMRI images were corrected for gradient distortion, susceptibility distortion, and motion, and then aligned to the corresponding T1w with one spline interpolation step. This volume was further corrected for intensity bias and normalized to a mean of 10000. This volume was then projected to the 2mm _32k_ ~~_f_~~ _s_ ~~_L_~~ _R_ mesh, excluding outliers, and aligned to a common space using a multi-modal surface registration [106]. The resultant cifti file for each HCP subject used in this study followed the file naming pattern: `*` ~~`A`~~ `tlas MSMAll hp2000` ~~`c`~~ `lean.dtseries.nii` . These steps are performed as part of the HCP Pipeline’s fMRIVolume and fMRISurface steps. Resting state and moving watching fMRI images were nuisance regressed in the same manner. Each minimally preprocessed fMRI was linearly detrended, band-pass filtered (0.008-0.25 Hz), confound regressed and standardized using Nilearn’s `signal.clean` function, which removes confounds orthogonally to the temporal filters. The confound regression strategy included six motion estimates, mean signal from a white matter, cerebrospinal fluid, and whole brain mask, derivatives of these previous nine regressors, and squares of these 18 terms. Spike regressors were not applied. Following these preprocessing operations, the mean signal was taken at each time frame for each node, as defined by the Schaefer 400 parcellation [48] in _32k_ ~~_f_~~ _s_ ~~_L_~~ _R_ space. 

## **Datasets: Nathan Kline Institute, Enhanced Rockland Sample 3T resting-state and diffusion weighted MRI** 

The Nathan Kline Institute Rockland Sample (NKI) dataset consisted of structural magnetic resonance imaging, resting state functional magnetic resonance imaging data, as well as diffusion magnetic resonance imaging data from 811 subjects (downloaded December 2016 from the INDI S3 Bucket) of a community sample of participants across the lifespan [65]. After excluding subjects based on data and metadata completeness and quality control, the final subset utilized included 542 subjects (56% female, age range = 7-84). The study was approved by the Nathan Kline Institute Institutional Review Board and Montclair State University Institutional Review Board and informed consent was obtained from all subjects. A comprehensive description of the imaging parameters can be found online at the NKI website. 

Briefly, images were collected on a Siemens Magneton Trio with a 12-channel head coil. Subjects underwent one T1-weighted structural scan (TR = 1900 ms, TE = 2.52 ms, flip angle = 9 _[◦]_ , 1 mm isotropic voxel resolution). Subjects underwent three differently parameterized resting state scans, but only one acquisition is used in the present study. The fMRI data was acquired with a gradient-echo planar imaging sequence (TR = 645 ms, TE = 30 ms, flip angle = 60 _[◦]_ , 3 mm isotropic voxel resolution, multiband factor = 4). This resting state run lasted approximately 9:41 seconds, with eyes open and instructions to fixate on a cross. Subjects underwent one diffusion MRI scan (TR = 2400 ms, TE = 85 ms, flip angle = 90 _[◦]_ , 2 mm isotropic voxel resolution, 128 diffusion weighted volumes, b-value = 1500 s/mm[2] , 9 b = 0 volumes). 

The NKI was downloaded in December of 2016 from the INDI S3 Bucket. At the time of download, the dataset consisted of 957 T1w (811 subjects), 914 DWI (771 subjects), and 718 fMRI (“acquisition645”; 634 subjects) images. T1w and DWI images, and tractography results were first filtered based on visual inspection. T1w images were filtered based on artifact, such as ringing or ghosting (43 images) and for FreeSurfer reconstruction failure (105 images) as assesses with the ENIGMA QC tools, leaving 809 T1w images (699 subjects). DWI images were filtered based on corrupt data (13 images) and artifact on fitted fractional anisotropy maps (18 images), leaving 883 images (747 subjects). Tractography was run on 781 images (677 subjects) that had both quality controlled T1w and DWI images. Tractography results were filtered based on artifact, which include failure to resolve callosal, cingulum, and/or corticospinal streamlines or errors resulting in visually sparse streamline densities, resulting in 764 tractography runs (661 subjects). T1w, DWI, and fMRI images were then filtered using computed image quality metrics [115–117]. T1w images were excluded if the scan was marked as an outlier (1.5x the inter-quartile range in the adverse direction) in three or 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

16 

more of following quality metric distributions: coefficient of joint variation, contrast-to-noise ratio, signal-to-noise ratio, Dietrich’s SNR, FBER, and EFC. DWI images were excluded if the percent of signal outliers, determined by eddy ~~q~~ c, was greater than 15%. Furthermore, DWI were excluded if the scan was marked as an outlier (1.5x the inter-quartile range in the adverse direction) in two or more of following quality metric distributions: temporal signal-to-noise ratio, mean voxel intensity outlier count, or max voxel intensity outlier count. fMRI images were excluded if greater than 15% of time frames exceeded 0.5mm framewise displacement. Furthermore, fMRI images were excluded the scan was marked as an outlier (1.5x the inter-quartile range in the adverse direction) in 3 or more of the following quality metric distributions: DVARS standard deviation, DVARS voxelwise standard deviation, temporal signal-to-noise ratio, framewise displacement mean, AFNI’s outlier ratio, and AFNI’s quality index. This image quality metric filtering excluded zero T1w images, 16 DWI images, and 21 fMRI images. Following this visual and image quality metric filtering, 809 T1w images (699 subjects), 728 DWI images (619 subjects), and 697 fMRI images (633 subjects). The intersection of subjects with at least one valid T1w, DWI, and fMRI images totaled 567 subjects. Finally, age metadata was available for 542 of these subjects. 

T1-weighted images were submitted to FreeSurfer’s cortical reconstruction workflow (version 6.0). The FreeSurfer results were used to skull strip the T1w, which was subsequently aligned to MNI space with 6 degrees of freedom. fMRI preprocessing was performed using the fMRIPrep version 1.1.8 [118]. The following description of fMRI preprocessing is based on fMRIPrep’s documentation. This workflow utilizes ANTs (2.1.0), FSL (5.0.9), AFNI (16.2.07), FreeSurfer (6.0.1), nipype [119], and nilearn [120]. Each T1w was corrected using `N4BiasFieldCorrection` [107] and skull-stripped using `antsBrainExtraction.sh` (using the OASIS template). The ANTs derived brain mask was refined with a custom variation of the method to reconcile ANTs-derived and FreeSurfer-derived segmentations of the cortical graymatter of Mindboggle [121]. Brain tissue segmentation of cerebrospinal fluid (CSF), white-matter (WM) and gray-matter (GM) was performed on the brain-extracted T1w using `fast` [110]. Functional data was slice time corrected using `3dTshift` from AFNI and motion corrected using FSL’s `mcflirt` . “Fieldmap-less” distortion correction was performed by co-registering the functional image to the same-subject T1w with intensity inverted [122] constrained with an average fieldmap template [123], implemented with `antsRegistration` . This was followed by co-registration to the corresponding T1w using boundary-based registration [124] with 9 degrees of freedom, using `bbregister` . Motion correcting transformations, field distortion correcting warp, and BOLD-toT1w transformation warp were concatenated and applied in a single step using `antsApplyTransforms` using Lanczos interpolation. Frame-wise displacement [125] was cal- 

culated for each functional run using the implementation of Nipype. The first four frames of the BOLD data in the T1w space were discarded. Diffusion images were preprocessed following the “DESIGNER” pipeline using MRTrix (3.0) [126, 127], which includes denoising, Gibbs ringing and Rician bias correction, distortion and eddy current correction [128] and B1 field correction. DWI were then aligned to their corresponding T1w and the MNI space in one interpolation step with B-vectors rotated accordingly. Local models of white matter orientation were estimated in a recursive manner [129] using constrained spherical deconvolution [109] with a spherical harmonics order of 8. Tractography was performed using Dipy’s `Local Tracking` module [108]. Probabilistic streamline tractography was seeded five times in each white matter voxel. Streamlines were propagated with a 0.5 mm step size and a maximum turning angle set to 20 _[◦]_ . Streamlines were retained if longer than 10 mm and with valid endpoints, following Dipy’s implementation of anatomically constrained tractography [112]. Streamline count between regions-of-interest were normalized by dividing the count between regions by the geometric average volume of the regions. 

## _Estimating group-representative structural connectivity network_ 

The output of the tractography algorithm generated subject-level estimates of streamlines for both the NKI and HCP datasets. In general, subjects’ connectomes are variable. A fraction of this variability reflects true individual differences, while another fraction reflects unwanted noise, e.g. random variation. One strategy for reducing noise is to aggregate data from many individuals to construct a group-representative consensus connectome. Here, we follow [44] and generate distant-dependent connectomes for both the NKI and HCP datasets. Briefly, this procedure bins edges by their length and, within each distance bin, identifies the edges that are most consistently present across the full set of subjects. Compared to standard approaches, which retains the most consistent edges irrespective of their length, consensus networks generated using this procedure are more representative of singlesubject connectomes–i.e. has more properties in common. Note that this distance-preserving consensus procedure is applied separately to within- and betweenhemisphere edges. Note also that for the NKI dataset, the consensus connectome was constructed using data from subjects aged 18-35 years. Finally, we made the decision to use the same (but dataset-specific) grouprepresentative for all HCP and NKI subjects. The rationale behind this decision was that it allowed us to discount the possibility that differences in model performance–e.g. fitness or edge weights–was driven by differences in the structural connectivity. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

17 

## **Dataset: Mouse anatomical and functional connectivity** 

## _Mouse resting state fMRI data_ 

All in vivo experiments were conducted in accordance with the Italian law (DL 2006/2014, EU 63/2010, Ministero della Sanit´a, Roma) and the recommendations in the Guide for the Care and Use of Laboratory Animals of the National Institutes of Health. Animal research protocols were reviewed and consented by the animal care committee of the Italian Institute of Technology and Italian Ministry of Health. The rsfMRI dataset used in this work consists of n = 19 scans in adult male C57BL/6J mice that are publicly available [130, 131]. Animal preparation, image data acquisition, and image data preprocessing for rsfMRI data have been described in greater detail elsewhere [131]. Briefly, rsfMRI data were acquired on a 7.0-T scanner (Bruker BioSpin, Ettlingen) equipped with BGA-9 gradient set, using a 72-mm birdcage transmit coil, and a four-channel solenoid coil for signal reception. Single-shot BOLD echo planar imaging time series were acquired using an echo planar imaging sequence with the following parameters: repetition time/echo time, 1000/15 ms; flip angle, 30 _[◦]_ ; matrix, 100 ×100; field of view, 2 × 2 cm2; 18 coronal slices; slice thickness, 0.50 mm; 500 (n = 21) or 1500 (n = 19) volumes; and a total rsfMRI acquisition time of 30 min. 

Image preprocessing has been previously described in greater detail elsewhere [131]. Briefly, timeseries were despiked, motion corrected, skull stripped and spatially registered to an in-house EPI-based mouse brain template. Denoising and motion correction strategies involved the regression of mean ventricular signal plus 6 motion parameters. The resulting time series were band-pass filtered (0.01-0.1 Hz band) and then spatially smoothed with a Gaussian kernel of 0.5 mm full width at half maximum. After preprocessing, mean regional time-series were extracted for 182 regions of interest (ROIs) derived from a predefined anatomical parcellation of the Allen Brain Institute (ABI, [13, 132]). 

## _Mouse Anatomical Connectivity Data_ 

The mouse anatomical connectivity data used in this work were derived from a voxel-scale model of the mouse connectome made available by the Allen Brain Institute [133, 134] ( `https://data.mendeley. com/datasets/dxtzpvv83k/2` ). 

Briefly, the mouse structural connectome was obtained from imaging enhanced green fluorescent protein (eGFP)–labeled axonal projections derived 428 viral microinjection experiments, and registered to a common coordinate space [13]. Under the assumption that structural connectivity varies smoothly across major brain divisions, the connectivity at each voxel was modeled as a radial basis kernel-weighted average of the projection 

patterns of nearby injections [134]. Following the procedure outlined in [133], we re-parcellated the voxel scale model in the same 182 nodes used for the resting state fMRI data, and we adopted normalized connection density (NCD) for defining connectome edges, as this normalization has been shown to be less affected by regional volume than other absolute and/or relative measure of interregional connectivity [135]. 

## **Fitting edge weights** 

Here, we use a regression-based framework for assigning weights to existing structural connections. Our approach is simple; we assume that at time _t_ the state of region _i_ (level of fMRI BOLD activity) is a function of its neighbors’ states at time _t −_ 1 plus an offset (bias). That is: 

**==> picture [196 x 24] intentionally omitted <==**

Here, _yi_ ( _t_ ) refers to the level of activity in region _i_ at time _t_ , Γ _i_ is the set of _i_ ’s connected neighbors (their indices). We use linear regression and ordinary least squares to estimate the parameters _Wji_ and _ci_ separately for each node _i_ . Thus, the resulting matrix _W ∈_ R _[n][×][n]_ , is sparse and preserves _exactly_ the binary structure of the whitematter connectivity. However, the weights can take on both positive and negative valence. The resulting network is also asymmetric–i.e. in general, the _Wij_ = _Wji_ . 

## **Null models** 

We fit the linear model using data pooled from all participants and scans. The model fitness was quantified as the mean squared error (MSE) of the observed activity time series and the time series predicted by the model. We compared the empirical MSE against five null models. 

- _Minimally wired null model_ : Generates a synthetic structural network comprised of the _m_ least costly connections, where _m_ is the same number of connections as the observed network. Because this network contains only short-range (low cost) connections, this null model assesses how long-distance connections contribute to model fitness. 

- _Re-ordered null model:_ Randomly permutes node order, effectively endowing nodes with a different number and set of neighbors than they have in the original network. This model assesses the contributions of specific neighbors to model fitness. 

- _“Spin” null model:_ Randomly permutes node order while approximately preserving inter-regional Euclidean distances. This model can be viewed as 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

18 

a constrained versions of the _re-ordered null model_ , in that it only allows particular subset of permutations. 

- _Topological null model:_ In this model, each node makes the same number of connections as in the original network. However, those connections, which define nodes’ neighborhoods, are formed at random. This model assesses whether networks with identical degree distribution yield similar fitness values as the original network. 

- _Temporal null model:_ For each scan, parcel time series are circularly shifted by some random integer. This procedure preserves temporally invariant properties of each time series, like their mean and standard deviation, and approximately preserves other properties, e.g. power spectrum. However, it destroys interregional correlations. In effect, this model tests whether time series with similar statistical properties but no correlation structure could yield comparable fitness values as the original time series. 

## **Modularity maximization** 

Here, we used modularity maximization to detect clusters (modules) in brain network data [136, 137]. Generically, modularity maximization works by assigning nodes to non-overlapping clusters so that the within-cluster weight of connections maximally exceeds that of a null model. This intuition is formalized by the modularity quality function: 

**==> picture [193 x 24] intentionally omitted <==**

In this equation, _Wij_ and _Pij_ are the observed and expected weight of the connection between nodes _i_ and _j_ , _zi ∈{_ 1 _, . . . , K}_ is a categorical variable that indicates the community to which node _i_ was assigned, _γ_ is the structural resolution parameter, and _δ_ ( _zi, zj_ ) is the Kronecker delta function, which evaluates to 1 when _zi_ = _zj_ and 0 otherwise. In short, modularity maximization seeks to optimize the quantity _Q_ ( _γ_ ) by selecting the values of _zi_ . 

The modularity maximization framework is general and can test different null hypotheses (null connectivity models) by varying the entries of _P_ , the matrix of expected connections and their weights. Here, we test two different null models. The first was proposed in [51] and is designed, specifically, to work with signed connectivity matrices. Under this model, the modularity equation is: 

**==> picture [207 x 59] intentionally omitted <==**

Here, the modularity equation includes separate terms for the positive and negative connections. The positive term is weighted more than the negative term (note the scale factors before the summation). This allows modules to be detected in networks with signed connections. However, if this same version of modularity maximization is applied to a network with positive links only, the second term in the equation evaluates to zero and returns the standard modularity equation. Note that in this equation, _Pij[±]_[=] _k_ 2 _i[±] m[k][±] j[±]_[.] 

Here, we use this quality function in two ways. In the main text, we optimize _Q[∗]_ 1000 times for both the asymmetric, weighted, and signed network as well as the fiber density network. These results are shown in Fig. 2. In the supplement, we combine this quality function with a hierarchical consensus algorithm [54], in which we first vary the values of _γ_ over all possible ranges to obtain a representative sample of communities (1,000,000 repetitions in total), and second, use these samples to construct a hierarchical dendrogram that organizes the noisy individual samples into hierarchically related consensus communities. The results of this analysis are shown in Fig. S9. 

We also used a second version of the modularity equation that was originally proposed for analysis of physical systems [59]. Briefly, the equation reads: 

**==> picture [194 x 24] intentionally omitted <==**

Here, the matrix _A_ is the binary matrix of connections that exist in the empirical and weighted connectivity matrix. _⟨W ⟩_ is the mean weight of existing connections. In other words, this modularity equation preserves the topology of the network, but assumes that edge weights are assigned randomly and uniformly. The results of this analysis are presented in Fig. S11. We note that, in principle, a resolution parameter could be incorporated into this formulation of the modularity quality function as well by replacing _⟨W ⟩_ with a tunable _γ_ parameter. 

## **Network statistics** 

In addition to modularity, we calculated several other network metrics. These include efficiency, characteristic path length, signed strength, and signed clustering coefficient. In this section we define those measures in detail. 

- **Shortest paths.** Both efficiency and characteristic path length are defined based on a network’s shortest path structure. Consider source and target nodes, _s_ and _t_ . The shortest path from the _s_ to _t_ can be estimated easily using the FloydWarshall algorithm. In weighted networks where edge weights as interpreted as measures of affinities it requires that the user first map those weights to 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

19 

measures of cost. For networks with positive connections only, a straightforward way to do this is to transform _Cij_ = _Wij[−][γ]_[,][where][the][most][common] value for the parameter is _γ_ = 1. For signed networks, like the ones used here, we use the same transformation, but only after we add an offset to each edge so that all weights are greater than zero. Our strategy for doing so involved first subtract the smallest (most negative) edge weight from the network. This ensures that all edges have a weight greater than zero, except for the single edge corresponding to the most negative weight, which has a cost of 0. We then add to every edge an even smaller offset–in this case the weakest edge weight in the fiber density matrix. This guarantees that all pairs of nodes connected by a fiber tract have nonzero weights. 

Once a network’s affinity-based weights have been transformed to costs, algorithms like the FloydWarshall algorithm find the shortest–i.e. least costly–path between all pairs of nodes. This algorithm returns two outputs: 1) the total cost incurred by following said path and 2) the number of steps (hops) along said path. Here, we use the hop data but not that, in principle, one could repeat all subsequent analyses using the cost data, instead. Let _Hst_ be the number of hops on the shortest path from the source _s_ to the target _t_ . 

- **Characteristic path length.** The characteristic path length of this network is calculated as: 

**==> picture [176 x 27] intentionally omitted <==**

- **Efficiency.** The efficiency of this network is calculated as: 

**==> picture [178 x 28] intentionally omitted <==**

- **Clustering coefficient.** The local clustering coefficient is calculated for each node _i_ . Intuitively, it measures the extent to which node _i_ ’s neighbors are also connected to one another. It can be calculated easily for each node as the density of the subgraph composed of those neighbors. Here, we calculate clustering coefficients for each node in the network based on their positive connections and negative connections, separately. The values reported in the main text ignore the actual weight but preserve sign. 

- **Strength.** Node strength – or weighted degree – the total weight of connections incident upon node _i_ . For an undirected network, it is calculated as: 

_si_ =[�] _j[W][ij]_[.][For][a][directed][network,][we][calculate] strength as the average of a nodes’ incoming and outgoing connections, i.e. _si_ = � _j[W][ij]_[+] 2[�] _j[W][ji]_ . 

Here, we also differentiate between a node’s positive and negative strength. Let _W_[+] and _W[−]_ be the networks of positive and negative connections only. For the network of negative connections, we conveniently flip the sign of each connection. Then we calculate each nodes’ signed strength as � _j[W][ ±] ij_[+][�] _j[W][ ±] ji s[±] i_[=] 2 . 

- **Partition laterality.** We calculated partition laterality following Lohse _et al._ [53]. For a given community _c_ , we calculate its uncorrected laterality as andΛ _c_ = _N[|] r[N]_ and _[r] N[−] c[N] N[l][|]_ . _l_ are the number of those nodes in theHere, _Nc_ is the number of nodes in _c_ right and left hemispheres, respectively. When the community has a balanced number of nodes from both hemispheres its laterality is close to zero; if it is left- or right-dominant, then the value is close to 1. 

For a partition comprised of communities _c_ 1 _, . . . , cK_ , we calculate the partition laterality as Λ = _N_ 1[(][�] _c[N][c]_[Λ] _[c][−⟨]_[�] _c[N][c]_[Λ] _[c][⟩]_[).][Here,][the] term _⟨_[�] _c[N][c]_[Λ] _[c][⟩]_[indicates][the][expected][laterality] under a null model in which nodes get randomly assigned to one hemisphere or another. Note that here we cannot use spin tests for the permutation; the spin tests preserves hemisphere labels and a “spun” partition would have laterality exactly equal to that of the original, unpermuted partition. 

## **Neural mass models** 

Many studies have tried to link brain structure and function [49]. One popular strategy for doing so is to use an estimate of anatomical connectivity to generate synthetic covariance matrices (either directly or by first generating synthetic neural time series and calculating their covariance empirically). The synthetic covariance matrices can then be compared to the empirical FC, usually as a correlation of their edge weights. The resulting coefficient serves as a measure of structure-function coupling. Here, we analyzed two models for generating synthetic covariance matrices or time series based on populationlevel “neural mass” models (NMMs). 

- **Gal´an model.** We follow work by Honey _et al._ [77] for estimating the inter-areal covariance matrix, **C** , based on a linearization of Wilson-Cowan dynamics for neuronal populations [138]. The element _Cij ∈_ **C** denotes the covariance of activity in area _i_ with that of area _j_ . In more detail, we let **u** ( _t_ ) = _{u_ 1( _t_ ) _, . . . , uN_ ( _t_ ) _}_ be the vector of brain areas’ states (activity levels) at time _t_ . Under these dynamics, brain areas’ states evolve as: 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

20 

The spiking network model evolves according to the following differential equations: 

**==> picture [180 x 11] intentionally omitted <==**

where _ξ_ ( _t_ ) is uncorrelated Gaussian noise and ∆ _t_ is a single time step. Here, the generalized coupling matrix, **A** , is based on the structural connectivity matrix, **W** , and was defined as: 

**==> picture [203 x 78] intentionally omitted <==**

**==> picture [178 x 11] intentionally omitted <==**

where _α_ is a leak variable within each brain area and **I** is the identity matrix. As in Honey _et al._ [77], we fixed _α_ = 2. 

Conveniently, Gal´an [138] showed that brain areas’ pairwise covariances (summarized by the matrix **C** _∈_ R _[N][×][N]_ ) can be estimated directly from the spectral properties of **A** and the covariance of the noise terms _ξ_ ( _t_ ). As with covariance matrices estimated from recorded time series of brain activity, we interpret **C** as an estimate of functional connectivity. See Gal´an [138] for more details. 

- **Reduced Wong-Wang mean field model.** We also studied a second biophysical model for fMRI BOLD data. Unlike the Gal´an model, which calculates the covariance structure analytically given a structural connectivity matrix, this model generates simulated time series, first by using a reduced spiking neural network to generate population-level time courses, and second by convolving these data with a hemodynamic model. 

- [1] Olaf Sporns, Giulio Tononi, and Rolf K¨otter, “The human connectome: a structural description of the human brain,” PLoS Comput Biol **1** , e42 (2005). 

- [2] Chun-Hung Yeh, Derek K Jones, Xiaoyun Liang, Maxime Descoteaux, and Alan Connelly, “Mapping structural connectivity using diffusion mri: Challenges and opportunities,” Journal of Magnetic Resonance Imaging **53** , 1666–1682 (2021). 

- [3] Patric Hagmann, Leila Cammoun, Xavier Gigandet, Reto Meuli, Christopher J Honey, Van J Wedeen, and Olaf Sporns, “Mapping the structural core of human cerebral cortex,” PLoS Biol **6** , e159 (2008). 

- [4] Bo-yong Park, Reinder Vos de Wael, Casey Paquola, Sara Larivi`ere, Oualid Benkarim, Jessica Royer, Shahin Tavakol, Raul R Cruces, Qiongling Li, Sofie L Valk, _et al._ , “Signal diffusion along connectome gradients and inter-hub routing differentially contribute to dynamic human brain function,” Neuroimage **224** , 117429 (2021). 

- [5] Hae-Jeong Park and Karl Friston, “Structural and functional brain networks: from connections to cognition,” Science **342** (2013). 

In this equation, _xi_ , _H_ ( _xi_ ), and _Si_ are the total input current, population firing rate, and synaptic gating for region _i_ . The input current, _xi_ depends on recurrent connection strength, _w_ , excitatory input, _I_ , and inter-regional information “flow”, which is calculated as the sum of region _i_ ’s connected neighbors’ synaptic gating, weighted by the global coupling constant, _G_ , and synaptic coupling constant, _J_ . Following Wang _et al._ [139], we set the parameters of the input-output function, _H_ ( _xi_ ) to _a_ = 270 n/C, _b_ = 108 Hz, and _d_ = 0 _._ 154 s. Kinetic parameters for synaptic activity were fixed at _r_ = 0 _._ 641 and _τs_ = 0 _._ 1 s. The variable _vi_ ( _t_ ) is uncorrelated Gaussian-distributed noise whose variance is scaled by _σ_ . 

This model generates neural activity at submillisecond timescales. Again, following Wang _et al._ [139], population level activity is input to the Balloon-Windkessel hemodynamic model [28], which yields simulated fMRI BOLD time courses for every brain region. 

- [6] Jyothika Kumar, Sarina Iwabuchi, Shamuz Oowise, Vijender Balain, Lena Palaniyappan, and Peter F Liddle, “Shared white-matter dysconnectivity in schizophrenia and bipolar disorder with psychosis,” Psychological medicine **45** , 759–770 (2015). 

- [7] Alex Fornito, Andrew Zalesky, and Michael Breakspear, “The connectomics of brain disorders,” Nature Reviews Neuroscience **16** , 159–172 (2015). 

- [8] Olaf Sporns and Jonathan D Zwi, “The small world of the cerebral cortex,” Neuroinformatics **2** , 145–162 (2004). 

- [9] Martijn P Van Den Heuvel and Olaf Sporns, “Richclub organization of the human connectome,” Journal of Neuroscience **31** , 15775–15786 (2011). 

- [10] Olaf Sporns and Richard F Betzel, “Modular brain networks,” Annual review of psychology **67** , 613–640 (2016). 

- [11] Richard F Betzel and Danielle S Bassett, “Specificity and robustness of long-distance connections in weighted, interareal connectomes,” Proceedings of the National Academy of Sciences **115** , E4880–E4889 (2018). 

- [12] Danielle S Bassett and Olaf Sporns, “Network neuro- 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

21 

   - science,” Nature neuroscience **20** , 353–364 (2017). 

- [13] Seung Wook Oh, Julie A Harris, Lydia Ng, Brent Winslow, Nicholas Cain, Stefan Mihalas, Quanxin Wang, Chris Lau, Leonard Kuan, Alex M Henry, _et al._ , “A mesoscale connectome of the mouse brain,” Nature **508** , 207–214 (2014). 

- [14] Chi-Tin Shih, Olaf Sporns, Shou-Li Yuan, Ta-Shun Su, Yen-Jen Lin, Chao-Chun Chuang, Ting-Yuan Wang, Chung-Chuang Lo, Ralph J Greenspan, and Ann-Shyn Chiang, “Connectomics-based analysis of information flow in the drosophila brain,” Current Biology **25** , 1249– 1258 (2015). 

- [15] Lav R Varshney, Beth L Chen, Eric Paniagua, David H Hall, and Dmitri B Chklovskii, “Structural properties of the caenorhabditis elegans neuronal network,” PLoS computational biology **7** , e1001066 (2011). 

- [16] Nikola T Markov, MM Ercsey-Ravasz, AR Ribeiro Gomes, Camille Lamy, Loic Magrou, Julien Vezoli, P Misery, A Falchier, R Quilodran, MA Gariel, _et al._ , “A weighted and directed interareal connectivity matrix for macaque cerebral cortex,” Cerebral cortex **24** , 17–36 (2014). 

- [17] Anil K Seth and Gerald M Edelman, “Distinguishing causal interactions in neural populations,” Neural computation **19** , 910–933 (2007). 

- [18] Winrich A Freiwald, Pedro Valdes, Jorge Bosch, Rolando Biscay, Juan Carlos Jimenez, Luis Manuel Rodriguez, Valia Rodriguez, Andreas K Kreiter, and Wolf Singer, “Testing non-linearity and directedness of interactions between neural groups in the macaque inferotemporal cortex,” Journal of neuroscience methods **94** , 105–119 (1999). 

- [19] Clive WJ Granger, “Investigating causal relations by econometric models and cross-spectral methods,” Econometrica: journal of the Econometric Society , 424–438 (1969). 

- [20] Corrado Bernasconi and Peter KoEnig,[`] “On the directionality of cortical interactions studied by structural analysis of electrophysiological recordings,” Biological cybernetics **81** , 199–210 (1999). 

- [21] Alard Roebroeck, Elia Formisano, and Rainer Goebel, “Mapping directed influence over the brain using granger causality and fmri,” Neuroimage **25** , 230–242 (2005). 

- [22] Thomas Schreiber, “Measuring information transfer,” Physical review letters **85** , 461 (2000). 

- [23] Leonardo Novelli, Patricia Wollstadt, Pedro Mediano, Michael Wibral, and Joseph T Lizier, “Large-scale directed network inference with multivariate transfer entropy and hierarchical statistical testing,” Network Neuroscience **3** , 827–847 (2019). 

- [24] Karl J Friston, “Functional and effective connectivity: a review,” Brain connectivity **1** , 13–36 (2011). 

- [25] Karl Friston, Rosalyn Moran, and Anil K Seth, “Analysing connectivity with granger causality and dynamic causal modelling,” Current opinion in neurobiology **23** , 172–178 (2013). 

- [26] Pedro A Valdes-Sosa, Alard Roebroeck, Jean Daunizeau, and Karl Friston, “Effective connectivity: influence, causality and biophysical modeling,” Neuroimage **58** , 339–361 (2011). 

- [27] Matthieu Gilson, Ruben Moreno-Bote, Adri´an PonceAlvarez, Petra Ritter, and Gustavo Deco, “Estima- 

tion of directed effective connectivity from fmri functional connectivity hints at asymmetries of cortical connectome,” PLoS computational biology **12** , e1004762 (2016). 

- [28] Karl J Friston, Lee Harrison, and Will Penny, “Dynamic causal modelling,” Neuroimage **19** , 1273–1302 (2003). 

- [29] Jean Daunizeau, Olivier David, and Klaas E Stephan, “Dynamic causal modelling: a critical review of the biophysical and statistical foundations,” Neuroimage **58** , 312–322 (2011). 

- [30] Stefan Fr¨assle, Ekaterina I Lomakina, Adeel Razi, Karl J Friston, Joachim M Buhmann, and Klaas E Stephan, “Regression dcm for fmri,” Neuroimage **155** , 406–421 (2017). 

- [31] Matteo Mancini, Giovanni Giulietti, Nicholas Dowell, Barbara Span`o, Neil Harrison, Marco Bozzali, and Mara Cercignani, “Introducing axonal myelination in connectomics: A preliminary analysis of g-ratio distribution in healthy subjects,” NeuroImage **182** , 351–359 (2018). 

- [32] Tommy Boshkovski, Ljupco Kocarev, Julien CohenAdad, Bratislav Miˇsi´c, St´ephane Leh´ericy, Nikola Stikov, and Matteo Mancini, “The r1-weighted connectome: complementing brain networks with a myelinsensitive measure,” Network Neuroscience **5** , 358–372 (2021). 

- [33] Tommy Boshkovski, Julien Cohen-Adad, Bratislav Misic, Isabelle Arnulf, Jean-Christophe Corvol, Marie Vidailhet, St´ephane Leh´ericy, Nikola Stikov, and Matteo Mancini, “The myelin-weighted connectome in parkinson’s disease,” Movement Disorders **37** , 724–733 (2022). 

- [34] Yaniv Assaf, Tamar Blumenfeld-Katzir, Yossi Yovel, and Peter J Basser, “Axcaliber: a method for measuring axon diameter distribution from diffusion mri,” Magnetic Resonance in Medicine: An Official Journal of the International Society for Magnetic Resonance in Medicine **59** , 1347–1354 (2008). 

- [35] Adeel Razi, Mohamed L Seghier, Yuan Zhou, Peter McColgan, Peter Zeidman, Hae-Jeong Park, Olaf Sporns, Geraint Rees, and Karl J Friston, “Large-scale dcms for resting-state fmri,” Network Neuroscience **1** , 222– 241 (2017). 

- [36] Stefan Fr¨assle, Ekaterina I Lomakina, Lars Kasper, Zina M Manjaly, Alex Leff, Klaas P Pruessmann, Joachim M Buhmann, and Klaas E Stephan, “A generative model of whole-brain effective connectivity,” Neuroimage **179** , 505–529 (2018). 

- [37] Gerald Hahn, Michael A Skeide, Dante Mantini, Marco Ganzetti, Alain Destexhe, Angela D Friederici, and Gustavo Deco, “A new computational approach to estimate whole-brain effective connectivity from functional and structural mri, applied to language development,” Scientific reports **9** , 1–13 (2019). 

- [38] Shi Gu, Fabio Pasqualetti, Matthew Cieslak, Qawi K Telesford, B Yu Alfred, Ari E Kahn, John D Medaglia, Jean M Vettel, Michael B Miller, Scott T Grafton, _et al._ , “Controllability of structural brain networks,” Nature communications **6** , 1–10 (2015). 

- [39] Farras Abdelnour, Henning U Voss, and Ashish Raj, “Network diffusion accurately models the relationship between structural and functional brain connectivity networks,” Neuroimage **90** , 335–347 (2014). 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

22 

- [40] Richard F Betzel, Shi Gu, John D Medaglia, Fabio Pasqualetti, and Danielle S Bassett, “Optimally controlling the human connectome: the role of network topology,” Scientific reports **6** , 30770 (2016). 

- [41] Sarah Feldt Muldoon, Fabio Pasqualetti, Shi Gu, Matthew Cieslak, Scott T Grafton, Jean M Vettel, and Danielle S Bassett, “Stimulation-based control of dynamic brain networks,” PLoS computational biology **12** , e1005076 (2016). 

- [42] Richard F Betzel, John D Medaglia, Lia Papadopoulos, Graham L Baum, Ruben Gur, Raquel Gur, David Roalf, Theodore D Satterthwaite, and Danielle S Bassett, “The modular organization of human anatomical brain networks: Accounting for the cost of wiring,” Network Neuroscience **1** , 42–68 (2017). 

- [43] David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, _et al._ , “The wu-minn human connectome project: an overview,” Neuroimage **80** , 62–79 (2013). 

- [44] Richard F Betzel, Alessandra Griffa, Patric Hagmann, and Bratislav Miˇsi´c, “Distance-dependent consensus thresholds for generating group-representative structural brain networks,” Network neuroscience **3** , 475–496 (2019). 

- [45] Emily S Finn, Xilin Shen, Dustin Scheinost, Monica D Rosenberg, Jessica Huang, Marvin M Chun, Xenophon Papademetris, and R Todd Constable, “Functional connectome fingerprinting: identifying individuals using patterns of brain connectivity,” Nature neuroscience **18** , 1664–1671 (2015). 

- [46] Caterina Gratton, Timothy O Laumann, Ashley N Nielsen, Deanna J Greene, Evan M Gordon, Adrian W Gilmore, Steven M Nelson, Rebecca S Coalson, Abraham Z Snyder, Bradley L Schlaggar, _et al._ , “Functional brain networks are dominated by stable group and individual factors, not cognitive or daily variation,” Neuron **98** , 439–452 (2018). 

- [47] Frantiˇsek V´aˇsa and Bratislav Miˇsi´c, “Null models in network neuroscience,” Nature Reviews Neuroscience , 1– 12 (2022). 

- [48] Alexander Schaefer, Ru Kong, Evan M Gordon, Timothy O Laumann, Xi-Nian Zuo, Avram J Holmes, Simon B Eickhoff, and BT Thomas Yeo, “Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity mri,” Cerebral cortex **28** , 3095– 3114 (2018). 

- [49] Laura E Su´arez, Ross D Markello, Richard F Betzel, and Bratislav Misic, “Linking structure and function in macroscale brain networks,” Trends in Cognitive Sciences (2020). 

- [50] Caio Seguin, Olaf Sporns, Andrew Zalesky, Fernando Calamante, _et al._ , “Network communication models narrow the gap between the modular organization of structural and functional brain networks,” bioRxiv (2022). 

- [51] Mikail Rubinov and Olaf Sporns, “Weight-conserving characterization of complex functional brain networks,” Neuroimage **56** , 2068–2079 (2011). 

- [52] Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre, “Fast unfolding of communities in large networks,” Journal of statistical mechanics: theory and experiment **2008** , P10008 (2008). 

- [53] Christian Lohse, Danielle S Bassett, Kelvin O Lim, and Jean M Carlson, “Resolving anatomical and functional structure in human brain organization: identifying mesoscale organization in weighted network representations,” PLoS computational biology **10** , e1003712 (2014). 

- [54] Lucas GS Jeub, Olaf Sporns, and Santo Fortunato, “Multiresolution consensus clustering in networks,” Scientific reports **8** , 1–16 (2018). 

- [55] Richard F Betzel and Danielle S Bassett, “Multi-scale brain networks,” Neuroimage **160** , 73–83 (2017). 

- [56] Lia Papadopoulos, James G Puckett, Karen E Daniels, and Danielle S Bassett, “Evolution of network architecture in a granular material under compression,” Physical Review E **94** , 032908 (2016). 

- [57] Lia Papadopoulos, Mason A Porter, Karen E Daniels, and Danielle S Bassett, “Network analysis of particles and grains,” Journal of Complex Networks **6** , 485–565 (2018). 

- [58] Danielle S Bassett, Eli T Owens, Karen E Daniels, and Mason A Porter, “Influence of network topology on sound propagation in granular materials,” Physical Review E **86** , 041306 (2012). 

- [59] Danielle S Bassett, Eli T Owens, Mason A Porter, M Lisa Manning, and Karen E Daniels, “Extraction of force-chain network architecture in granular materials using community detection,” Soft Matter **11** , 2731–2744 (2015). 

- [60] Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Yanjun Wu, Jean-Dominique Gallezot, Etienne[´] Aumont, Stijn Servaes, Stephanie G Scala, _et al._ , “Mapping neurotransmitter systems to the structural and functional organization of the human neocortex,” Biorxiv (2021). 

- [61] Andrea Avena-Koenigsberger, Bratislav Misic, and Olaf Sporns, “Communication dynamics in complex brain networks,” Nature Reviews Neuroscience **19** , 17 (2018). 

- [62] Caio Seguin, Martijn P Van Den Heuvel, and Andrew Zalesky, “Navigation of brain networks,” Proceedings of the National Academy of Sciences **115** , 6297–6302 (2018). 

- [63] Caio Seguin, Adeel Razi, and Andrew Zalesky, “Inferring neural signalling directionality from undirected structural connectomes,” Nature communications **10** , 1–13 (2019). 

- [64] Ross D Markello and Bratislav Misic, “Comparing spatial null models for brain maps,” NeuroImage , 118052 (2021). 

- [65] Kate Brody Nooner, Stanley Colcombe, Russell Tobe, Maarten Mennes, Melissa Benedict, Alexis Moreno, Laura Panek, Shaquanna Brown, Stephen Zavitz, Qingyang Li, _et al._ , “The nki-rockland sample: a model for accelerating the pace of discovery science in psychiatry,” Frontiers in neuroscience **6** , 152 (2012). 

- [66] Farnaz Zamani Esfahlani, Joshua Faskowitz, Jonah Slack, Bratislav Miˇsi´c, and Richard F Betzel, “Local structure-function relationships in human brain networks across the human lifespan,” bioRxiv (2021). 

- [67] Linda Geerligs, Natasha M Maurits, Remco J Renken, and Monicque M Lorist, “Reduced specificity of functional connectivity in the aging brain during task performance,” Human brain mapping **35** , 319–330 (2014). 

- [68] Richard F Betzel, Lisa Byrge, Ye He, Joaqu´ın Go˜ni, 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

23 

Xi-Nian Zuo, and Olaf Sporns, “Changes in structural and functional connectivity among resting-state networks across the human lifespan,” Neuroimage **102** , 345–357 (2014). 

- [69] Micaela Y Chan, Denise C Park, Neil K Savalia, Steven E Petersen, and Gagan S Wig, “Decreased segregation of brain systems across the healthy adult lifespan,” Proceedings of the National Academy of Sciences **111** , E4997–E5006 (2014). 

- [70] Jennifer Stiso and Danielle S Bassett, “Spatial embedding imposes constraints on neuronal network architectures,” Trends in cognitive sciences **22** , 1127–1142 (2018). 

- [71] Martijn P Van den Heuvel, Edward T Bullmore, and Olaf Sporns, “Comparative connectomics,” Trends in cognitive sciences **20** , 345–361 (2016). 

- [72] Maria Grazia Puxeddu, Joshua Faskowitz, Olaf Sporns, Laura Astolfi, and Richard F Betzel, “Multi-modal and multi-subject modular organization of human brain networks,” bioRxiv (2022). 

- [73] Joshua Faskowitz, Richard F Betzel, and Olaf Sporns, “Edges in brain networks: Contributions to models of structure and function,” Network Neuroscience **6** , 1–28 (2022). 

- [74] Olaf Sporns, “The human connectome: a complex network,” Annals of the New York Academy of Sciences **1224** , 109–125 (2011). 

- [75] Ruben Sanchez-Romero and Michael W Cole, “Combining multiple functional connectivity methods to improve causal inferences,” Journal of cognitive neuroscience **33** , 180–194 (2021). 

- [76] Jill X O’Reilly, Paula L Croxson, Saad Jbabdi, Jerome Sallet, MaryAnn P Noonan, Rogier B Mars, Philip GF Browning, Charles RE Wilson, Anna S Mitchell, Karla L Miller, _et al._ , “Causal effect of disconnection lesions on interhemispheric functional connectivity in rhesus monkeys,” Proceedings of the National Academy of Sciences **110** , 13982–13987 (2013). 

- [77] Christopher J Honey, Olaf Sporns, Leila Cammoun, Xavier Gigandet, Jean-Philippe Thiran, Reto Meuli, and Patric Hagmann, “Predicting human resting-state functional connectivity from structural connectivity,” Proceedings of the National Academy of Sciences **106** , 2035–2040 (2009). 

- [78] Gustavo Deco, Viktor K Jirsa, and Anthony R McIntosh, “Emerging concepts for the dynamical organization of resting-state activity in the brain,” Nature Reviews Neuroscience **12** , 43–56 (2011). 

- [79] Inhan Kang, Matthew Galdo, and Brandon M Turner, “Constraining functional coactivation with a clusterbased structural connectivity network,” Network Neuroscience , 1–55 (2022). 

- [80] Anirudh Wodeyar and Ramesh Srinivasan, “Structural connectome constrained graphical lasso for meg partial coherence,” Network Neuroscience **6** , 1219–1242 (2022). 

- [81] Joaqu´ın Go˜ni, Martijn P Van Den Heuvel, Andrea Avena-Koenigsberger, Nieves Velez De Mendizabal, Richard F Betzel, Alessandra Griffa, Patric Hagmann, Bernat Corominas-Murtra, Jean-Philippe Thiran, and Olaf Sporns, “Resting-brain functional connectivity predicted by analytic measures of network communication,” Proceedings of the National Academy of Sciences **111** , 833–838 (2014). 

- [82] Bertha V´azquez-Rodr´ıguez, Laura E Su´arez, Ross D 

   - Markello, Golia Shafiei, Casey Paquola, Patric Hagmann, Martijn P Van Den Heuvel, Boris C Bernhardt, R Nathan Spreng, and Bratislav Misic, “Gradients of structure–function tethering across neocortex,” Proceedings of the National Academy of Sciences **116** , 21219–21227 (2019). 

- [83] Jessica S Damoiseaux and Michael D Greicius, “Greater than the sum of its parts: a review of studies combining structural connectivity and resting-state functional connectivity,” Brain structure and function **213** , 525– 533 (2009). 

- [84] Michael W Cole, Danielle S Bassett, Jonathan D Power, Todd S Braver, and Steven E Petersen, “Intrinsic and task-evoked network architectures of the human brain,” Neuron **83** , 238–251 (2014). 

- [85] Ann M Hermundstad, Danielle S Bassett, Kevin S Brown, Elissa M Aminoff, David Clewett, Scott Freeman, Amy Frithsen, Arianne Johnson, Christine M Tipper, Michael B Miller, _et al._ , “Structural foundations of resting-state and task-based functional connectivity in the human brain,” Proceedings of the National Academy of Sciences **110** , 6169–6174 (2013). 

- [86] Richard F Betzel, Lisa Byrge, Farnaz Zamani Esfahlani, and Daniel P Kennedy, “Temporal fluctuations in the brain’s modular architecture during movie-watching,” NeuroImage , 116687 (2020). 

- [87] Takuya Ito, Scott L Brincat, Markus Siegel, Ravi D Mill, Biyu J He, Earl K Miller, Horacio G Rotstein, and Michael W Cole, “Task-evoked activity quenches neural correlations and variability across cortical areas,” PLoS computational biology **16** , e1007983 (2020). 

- [88] Francois Rheault, Philippe Poulin, Alex Valcourt Caron, Etienne St-Onge, and Maxime Descoteaux, “Common misconceptions, hidden biases and modern challenges of dmri tractography,” Journal of neural engineering **17** , 011001 (2020). 

- [89] Kurt G Schilling, Vishwesh Nath, Colin Hansen, Prasanna Parvathaneni, Justin Blaber, Yurui Gao, Peter Neher, Dogu Baran Aydogan, Yonggang Shi, Mario Ocampo-Pineda, _et al._ , “Limits to anatomical accuracy of diffusion tractography using modern approaches,” NeuroImage **185** , 1–11 (2019). 

- [90] Karl J Friston, “Functional and effective connectivity in neuroimaging: a synthesis,” Human brain mapping **2** , 56–78 (1994). 

- [91] Gy¨orgy Buzs´aki, “Feed-forward inhibition in the hippocampal formation,” Progress in neurobiology **22** , 131–153 (1984). 

- [92] Hong Gu, Yuzheng Hu, Xi Chen, Yong He, and Yihong Yang, “Regional excitation-inhibition balance predicts default-mode network deactivation via functional connectivity,” Neuroimage **185** , 388–397 (2019). 

- [93] Alex Fornito, Andrew Zalesky, and Edward Bullmore, _Fundamentals of brain network analysis_ (Academic Press, 2016). 

- [94] Colin Reveley, Anil K Seth, Carlo Pierpaoli, Afonso C Silva, David Yu, Richard C Saunders, David A Leopold, and Q Ye Frank, “Superficial white matter fiber systems impede detection of long-range cortical connections in diffusion mr tractography,” Proceedings of the National Academy of Sciences **112** , E2820–E2828 (2015). 

- [95] Klaus H Maier-Hein, Peter F Neher, Jean-Christophe Houde, Marc-Alexandre Cˆot´e, Eleftherios Garyfallidis, Jidan Zhong, Maxime Chamberland, Fang-Cheng Yeh, 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

24 

Ying-Chia Lin, Qing Ji, _et al._ , “The challenge of mapping the human connectome based on diffusion tractography,” Nature communications **8** , 1–13 (2017). 

- [96] Larry W Swanson, Joel D Hahn, and Olaf Sporns, “Organizing principles for the cerebral cortex network of commissural and association connections,” Proceedings of the National Academy of Sciences **114** , E9692–E9701 (2017). 

- [97] Simona Schiavi, Mario Ocampo-Pineda, Muhamed Barakovic, Laurent Petit, Maxime Descoteaux, JeanPhilippe Thiran, and Alessandro Daducci, “A new method for accurate in vivo mapping of human brain connections using microstructural and anatomical information,” Science advances **6** , eaba8245 (2020). 

- [98] Matthew Cieslak, Philip A Cook, Xiaosong He, FangCheng Yeh, Thijs Dhollander, Azeez Adebimpe, Geoffrey K Aguirre, Danielle S Bassett, Richard F Betzel, Josiane Bourque, _et al._ , “Qsiprep: an integrative platform for preprocessing and reconstructing diffusion mri data,” Nature methods **18** , 775–778 (2021). 

- [99] Evan Calabrese, Alexandra Badea, Gary Cofer, Yi Qi, and G Allan Johnson, “A diffusion mri tractography connectome of the mouse brain and comparison with neuronal tracer data,” Cerebral cortex **25** , 4628–4637 (2015). 

- [100] Caio Seguin, Maciej Jedynak, Olivier David, Olaf Sporns, Andrew Zalesky, _et al._ , “Communication dynamics in the human connectome shape the cortex-wide propagation of direct electrical stimulation,” bioRxiv (2022). 

- [101] Mike J Veit, Aaron Kucyi, Wenhan Hu, Chao Zhang, Baotian Zhao, Zhihao Guo, Bowen Yang, Clara SavaSegal, Claire Perry, Jianguo Zhang, _et al._ , “Temporal order of signal propagation within and across intrinsic brain networks,” Proceedings of the National Academy of Sciences **118** , e2105031118 (2021). 

- [102] Scott Marek, Brenden Tervo-Clemmens, Finnegan J Calabro, David F Montez, Benjamin P Kay, Alexander S Hatoum, Meghan Rose Donohue, William Foran, Ryland L Miller, Eric Feczko, _et al._ , “Towards reproducible brain-wide association studies,” BioRxiv (2020). 

- [103] Stephanie Noble, Amanda F Mejia, Andrew Zalesky, and Dustin Scheinost, “Improving power in functional magnetic resonance imaging by moving beyond clusterlevel inference,” Proceedings of the National Academy of Sciences **119** , e2203020119 (2022). 

- [104] Timothy O Laumann and Abraham Z Snyder, “Brain activity is not only for thinking,” Current Opinion in Behavioral Sciences **40** , 130–136 (2021). 

- [105] Matthew F Glasser, Stamatios N Sotiropoulos, J Anthony Wilson, Timothy S Coalson, Bruce Fischl, Jesper L Andersson, Junqian Xu, Saad Jbabdi, Matthew Webster, Jonathan R Polimeni, _et al._ , “The minimal preprocessing pipelines for the human connectome project,” Neuroimage **80** , 105–124 (2013). 

- [106] Emma C Robinson, Saad Jbabdi, Matthew F Glasser, Jesper Andersson, Gregory C Burgess, Michael P Harms, Stephen M Smith, David C Van Essen, and Mark Jenkinson, “Msm: a new flexible framework for multimodal surface matching,” Neuroimage **100** , 414– 426 (2014). 

- [107] Nicholas J Tustison, Brian B Avants, Philip A Cook, Yuanjie Zheng, Alexander Egan, Paul A Yushkevich, 

   - and James C Gee, “N4itk: improved n3 bias correction,” IEEE transactions on medical imaging **29** , 1310–1320 (2010). 

- [108] Eleftherios Garyfallidis, Matthew Brett, Bagrat Amirbekian, Ariel Rokem, Stefan Van Der Walt, Maxime Descoteaux, and Ian Nimmo-Smith, “Dipy, a library for the analysis of diffusion mri data,” Frontiers in neuroinformatics **8** , 8 (2014). 

- [109] J-Donald Tournier, Fernando Calamante, and Alan Connelly, “Robust determination of the fibre orientation distribution in diffusion mri: non-negativity constrained super-resolved spherical deconvolution,” Neuroimage **35** , 1459–1472 (2007). 

- [110] Yongyue Zhang, Michael Brady, and Stephen Smith, “Segmentation of brain mr images through a hidden markov random field model and the expectationmaximization algorithm,” IEEE transactions on medical imaging **20** , 45–57 (2001). 

- [111] Hiromasa Takemura, Cesar F Caiafa, Brian A Wandell, and Franco Pestilli, “Ensemble tractography,” PLoS computational biology **12** , e1004692 (2016). 

- [112] Robert E Smith, Jacques-Donald Tournier, Fernando Calamante, and Alan Connelly, “Anatomicallyconstrained tractography: improved diffusion mri streamlines tractography through effective use of anatomical information,” Neuroimage **62** , 1924–1938 (2012). 

- [113] Kesshi M Jordan, Bagrat Amirbekian, Anisha Keshavan, and Roland G Henry, “Cluster confidence index: a streamline-wise pathway reproducibility metric for diffusion-weighted mri tractography,” Journal of Neuroimaging **28** , 64–69 (2018). 

- [114] James E Cutting, Kaitlin L Brunick, and Ayse Candan, “Perceiving event dynamics and parsing hollywood films.” Journal of experimental psychology: human perception and performance **38** , 1476 (2012). 

- [115] Oscar Esteban, Daniel Birman, Marie Schaer, Oluwasanmi O Koyejo, Russell A Poldrack, and Krzysztof J Gorgolewski, “Mriqc: Advancing the automatic prediction of image quality in mri from unseen sites,” PloS one **12** , e0184661 (2017). 

- [116] David R Roalf, Megan Quarmley, Mark A Elliott, Theodore D Satterthwaite, Simon N Vandekar, Kosha Ruparel, Efstathios D Gennatas, Monica E Calkins, Tyler M Moore, Ryan Hopson, _et al._ , “The impact of quality assurance assessment on diffusion tensor imaging outcomes in a large-scale population-based cohort,” Neuroimage **125** , 903–919 (2016). 

- [117] Matteo Bastiani, Michiel Cottaar, Sean P Fitzgibbon, Sana Suri, Fidel Alfaro-Almagro, Stamatios N Sotiropoulos, Saad Jbabdi, and Jesper LR Andersson, “Automated quality control for within and between studies diffusion mri data using a non-parametric framework for movement and distortion correction,” Neuroimage **184** , 801–812 (2019). 

- [118] Oscar Esteban, Christopher J Markiewicz, Ross W Blair, Craig A Moodie, A Ilkay Isik, Asier Erramuzpe, James D Kent, Mathias Goncalves, Elizabeth DuPre, Madeleine Snyder, _et al._ , “fmriprep: a robust preprocessing pipeline for functional mri,” Nature methods **16** , 111–116 (2019). 

- [119] Krzysztof Gorgolewski, Christopher D Burns, Cindee Madison, Dav Clark, Yaroslav O Halchenko, Michael L Waskom, and Satrajit S Ghosh, “Nipype: a flexible, 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

25 

lightweight and extensible neuroimaging data processing framework in python,” Frontiers in neuroinformatics **5** , 13 (2011). 

- [120] Alexandre Abraham, Fabian Pedregosa, Michael Eickenberg, Philippe Gervais, Andreas Mueller, Jean Kossaifi, Alexandre Gramfort, Bertrand Thirion, and Ga¨el Varoquaux, “Machine learning for neuroimaging with scikit-learn,” Frontiers in neuroinformatics **8** , 14 (2014). 

- [121] Arno Klein, Satrajit S Ghosh, Forrest S Bao, Joachim Giard, Yrj¨o H¨ame, Eliezer Stavsky, Noah Lee, Brian Rossa, Martin Reuter, Elias Chaibub Neto, _et al._ , “Mindboggling morphometry of human brains,” PLoS computational biology **13** , e1005350 (2017). 

- [122] Sijia Wang, Daniel J Peterson, J Christopher Gatenby, Wenbin Li, Thomas J Grabowski, and Tara M Madhyastha, “Evaluation of field map and nonlinear registration methods for correction of susceptibility artifacts in diffusion mri,” Frontiers in neuroinformatics **11** , 17 (2017). 

- [123] Jeffrey Mark Treiber, Nathan S White, Tyler Christian Steed, Hauke Bartsch, Dominic Holland, Nikdokht Farid, Carrie R McDonald, Bob S Carter, Anders Martin Dale, and Clark C Chen, “Characterization and correction of geometric distortions in 814 diffusion weighted images,” PloS one **11** , e0152472 (2016). 

- [124] Douglas N Greve and Bruce Fischl, “Accurate and robust brain image alignment using boundary-based registration,” Neuroimage **48** , 63–72 (2009). 

- [125] Jonathan D Power, Anish Mitra, Timothy O Laumann, Abraham Z Snyder, Bradley L Schlaggar, and Steven E Petersen, “Methods to detect, characterize, and remove motion artifact in resting state fmri,” Neuroimage **84** , 320–341 (2014). 

- [126] Benjamin Ades-Aron, Jelle Veraart, Peter Kochunov, Stephen McGuire, Paul Sherman, Elias Kellner, Dmitry S Novikov, and Els Fieremans, “Evaluation of the accuracy and precision of the diffusion parameter estimation with gibbs and noise removal pipeline,” NeuroImage **183** , 532–543 (2018). 

   - [132] Quanxin Wang, Song-Lin Ding, Yang Li, Josh Royall, David Feng, Phil Lesnar, Nile Graddis, Maitham Naeemi, Benjamin Facer, Anh Ho, _et al._ , “The allen mouse brain common coordinate framework: a 3d reference atlas,” Cell **181** , 936–953 (2020). 

   - [133] Ludovico Coletta, Marco Pagani, Jennifer D Whitesell, Julie A Harris, Boris Bernhardt, and Alessandro Gozzi, “Network structure of the mouse brain connectome with voxel resolution,” Science Advances **6** , eabb7187 (2020). 

   - [134] Joseph E Knox, Kameron Decker Harris, Nile Graddis, Jennifer D Whitesell, Hongkui Zeng, Julie A Harris, Eric Shea-Brown, and Stefan Mihalas, “High-resolution data-driven model of the mouse connectome,” Network Neuroscience **3** , 217–236 (2018). 

   - [135] Mikail Rubinov, Rolf JF Ypma, Charles Watson, and Edward T Bullmore, “Wiring cost and topological participation of the mouse brain connectome,” Proceedings of the National Academy of Sciences **112** , 10032–10037 (2015). 

   - [136] Mark EJ Newman and Michelle Girvan, “Finding and evaluating community structure in networks,” Physical review E **69** , 026113 (2004). 

   - [137] Farnaz Zamani Esfahlani, Youngheun Jo, Maria Grazia Puxeddu, Haily Merritt, Jacob C Tanner, Sarah Greenwell, Riya Patel, Joshua Faskowitz, and Richard F Betzel, “Modularity maximization as a flexible and generic framework for brain network exploratory analysis,” arXiv preprint arXiv:2106.15428 (2021). 

   - [138] Roberto F Gal´an, “On how network architecture determines the dominant patterns of spontaneous neural activity,” PloS one **3** , e2148 (2008). 

   - [139] Peng Wang, Ru Kong, Xiaolu Kong, Rapha¨el Li´egeois, Csaba Orban, Gustavo Deco, Martijn P Van Den Heuvel, and BT Thomas Yeo, “Inversion of a large-scale circuit model reveals a cortical hierarchy in the dynamic resting human brain,” Science advances **5** , eaat7854 (2019). 

- [127] J-Donald Tournier, Robert Smith, David Raffelt, Rami Tabbara, Thijs Dhollander, Maximilian Pietsch, Daan Christiaens, Ben Jeurissen, Chun-Hung Yeh, and Alan Connelly, “Mrtrix3: A fast, flexible and open software framework for medical image processing and visualisation,” NeuroImage **202** , 116137 (2019). 

- [128] Jesper LR Andersson and Stamatios N Sotiropoulos, “An integrated approach to correction for off-resonance effects and subject movement in diffusion mr imaging,” Neuroimage **125** , 1063–1078 (2016). 

- [129] Chantal MW Tax, Ben Jeurissen, Sjoerd B Vos, Max A Viergever, and Alexander Leemans, “Recursive calibration of the fiber response function for spherical deconvolution of diffusion mri data,” Neuroimage **86** , 67–80 (2014). 

- [130] Joanes Grandjean, Carola Canella, Cynthia Anckaerts, G¨ulebru Ayrancı, Salma Bougacha, Thomas Bienert, David Buehlmann, Ludovico Coletta, Daniel Gallino, Natalia Gass, _et al._ , “Common functional networks in the mouse brain revealed by multi-centre resting-state fmri analysis,” Neuroimage **205** , 116278 (2020). 

- [131] Daniel Gutierrez-Barragan, M Albert Basson, Stefano Panzeri, and Alessandro Gozzi, “Infraslow state fluctuations govern spontaneous fmri network dynamics,” Current Biology **29** , 2295–2306 (2019). 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

26 

**==> picture [509 x 116] intentionally omitted <==**

FIG. S1. **Similarity of edge weights.** In the main text we use linear models to fit edge weights to structural connections. Here, we different edge weighting schemes. We consider: the logarithm of fiber densities (log10SC), estimated edge weights using all data (NoDiag), estimated edge weights using only low-motion data (NoDiagLoMo), estimated edge weights with the inclusion of an autoregressive diagonal term (Diag), functional connectivity estimated using a full correlation (FC), and partial correlations (ParCorr). In all cases, similarity was calculated as the Spearman correlation using only edges for which a structural connection was observed. 

**==> picture [509 x 128] intentionally omitted <==**

FIG. S2. **Effect of lag on estimated edge weights.** In the main text we use linear models to fit edge weights by predicting activity at time _t_ + 1 using activity at time _t_ (one frame of lag = 0.720 seconds). Here, we investigate the effect of longer lags on the estimated weights, increasing the lag to _≈_ 15 seconds. ( _a_ ) Model error at different lags. ( _b_ ) Spatial similarity of weights estimated at each lab. ( _c_ ) Example weight matrices at different lags. 

**==> picture [509 x 143] intentionally omitted <==**

FIG. S3. **Effects of connection length on model performance.** We divided connections into 20 percentile bins based on their length. Next, we created structural network backbone comprising the 5% shortest (or longest) connections, gradually adding back the progressively longer (or shorter) connection 19 bins, until all connections were added. This allowed us to assess the relative contributions of short _versus_ long connections. In panel _a_ , we plot the model error as a function across all percentiles. We also grouped connections by percentiles (from 2 to 20) and fit the model using each percentile independently rather cumulatively. The results in panel _b_ suggest that short connections are more informative and lead to reduced model error. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

27 

**==> picture [509 x 99] intentionally omitted <==**

FIG. S4. **Model errors at the regional level.** Regional mean squared error (MSE) for model fit using observed and intact network ( _a_ ) _versus_ the mean MSE across 100 models fit using a degree-preserving rewiring model. ( _c_ ) Scatterplot comparing regional error. Points above the diagonal are regions fit better using the observed network compared to the rewired. Panels _d_ and _e_ compare regional MSE with the logarithm of nodes’ degree and weighted degree. That is, nodes with fewer connections exhibited worse fits (greater MSE). 

**==> picture [509 x 101] intentionally omitted <==**

FIG. S5. **Effect of global signal regression on results.** The human data analyzed in the main text was processed using a procedure that included global signal regression (GSR). Here, we compare select results using data processed without GSR. ( _a_ ) Mean FC for GSR and non-GSR data; each point is a scan (4 scans _×_ 95 participants yields 380 points). ( _b_ ) Two-dimensional histogram of group-level edge weights estimated using GSR and non-GSR data. ( _c_ ) Subject-level model error. ( _d_ ) Comparison of regional model errors. The red line is identity (equal performance with both models). Points below the line have time series better predicted with non-GSR data; points above the line have activity time series better predicted by GSR data. ( _e_ ) Model error as a function of lag. 

**==> picture [509 x 163] intentionally omitted <==**

FIG. S6. **Dependence of distance effects on Euclidean distance** _**versus**_ **fiber length.** ( _a_ ) Euclidean distance _versus_ fiber length. Panels _b_ and _c_ depict edges weighted by fiber fiber length and Euclidean distance. ( _d_ ) Difference in fiber length and Euclidean distance. Panels _e_ and _f_ show connection weight versus distance. Panels _g_ - _i_ show connections that are stronger than expected but unique to Euclidean distance, fiber length, or are shared between both. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

28 

**==> picture [509 x 199] intentionally omitted <==**

FIG. S7. **Comparing connectivity weights estimated with an without regularization.** In the main text we used linear regression optimized with ordinary least squares to fit weights to edges. Here, we compare those results to weights fit using lasso regularization (implemented in MATLAB with the function `lasso.m` ). For each node, we fits its edge weights independently. We logarithmically sampled 10 values of the regularization parameter, _λ_ , over the interval [10 _[−]_[3] _,_ 0 _._ 5]. For each value of _λ_ , we generate a new estimate of connection weights, with sparsity increasing monotonically. ( _a_ ) Correlation of edge weight values with the edge weights reported in the main text (no regularization). ( _b_ ) Similarity of regularized connection weights to one another. ( _c_ ) Connectivity matrices. 

**==> picture [509 x 189] intentionally omitted <==**

FIG. S8. **Simulated FC using linearized neural mass model.** We used a linearization of a neural mass model [138] to generate simulated covariance matrices (which are then scaled to correlation matrices; FC). We performed this procedure using both the asymmetric, weighted, and signed version of SC as well as the traditional fiber density matrix. Panels _a_ and _b_ show the resulting correlation matrices. We then compared these matrices to an empirical estimate of FC. We found that the correlation matrix generated using asymmetric, weighted, and signed matrix was more similar to FC than the matrix generated using the fiber density weights. Panel _c_ shows the results of this analysis using both product-moment correlation and rank correlations to assess similarity. We also analyzed a simplified neural mass model (reduced Wong-Wang model with implementation made available from [139]). This procedure generates synthetic fMRI BOLD time series that can be treated identically to an empirical time series. The correlation structure of the synthetic data can then be compared to the empirical correlation structure, i.e. FC. Panels _d_ - _f_ depict correlation matrices for asymmetric, weighted, and signed structural connectivity, the fiber density matrix, and their correlations with respect to the empirical FC matrix. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

29 

**==> picture [509 x 202] intentionally omitted <==**

FIG. S9. **Comparing modular structure of structural networks.** Modules are cohesive subnetworks – nodes that make more connections to other members of the same module than to other modules. Here, we compare the modular structure of network with weights defined by fiber density and the same network with asymmetric, weighted, and signed edges. Here, we examine modules estimated with a fixed resolution parameter ( _γ_ = 1) but explore the multiscale modular structure in the supplement. Co-assignment probability matrices for the inferred edge weight ( _a_ ) and the fiber density matrices ( _b_ ). ( _c_ ) Element-wise difference in module co-assignment. ( _d_ ) System co-assignment matrix for reference. Comparison of modularity ( _e_ ) and laterality ( _f_ ) of detected modules. ( _g_ ) Alignment of modules with respect to coarse- and fine-system partitions. ( _h_ and _i_ ) Consensus communities for both versions of weights. 

**==> picture [509 x 140] intentionally omitted <==**

FIG. S10. **Modularity maximization with alternative, “geographic” null model.** In the main text, we described the results of detecting modules using modularity maximization with an “standard” internal null model that preserved nodes’ (signed) degrees. Here, we report results using an alternative null model. Briefly, this null model preserves the same binary “backbone” of the original network, but assigns an expected weight to each connection equal to the mean weight of all existing connections. Modules therefore reflect groups of brain regions whose observed connections’ weights are greater than the mean weight. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

30 

**==> picture [509 x 329] intentionally omitted <==**

FIG. S11. **Modularity results using alternative null model.** Module coassignment matrices for the signed, weighted, and directed SC ( _a_ ) and fiber density ( _b_ ). ( _c_ ) Difference in coassignment probability. Panels _d_ - _f_ show the same matrices, but ordered by brain system. ( _g_ ) Laterality of detected communities. Bilateral communities have values close to zero. ( _h_ ) Adjusted Rand index of detected partitions with respect to coarse and fine-scale system labels. ( _i_ ) Consensus communities detected in signed, weighted, and directed SC. The panel next to each surface plot depicts each community’s composition in terms of canonical brain systems. ( _j_ ) Canonical brain systems. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

31 

**==> picture [509 x 394] intentionally omitted <==**

FIG. S12. **Enriching modules using brain maps.** In the main text we performed community detection on the asymmetric, weighted, and signed network ( `AWS` ) and fiber density network ( `Fiber` ) using two versions of modularity maximization: one that uses a signed internal null model ( `RS` ; [51])and another that we termed a “geometric” null model, in which topology is preserved but weights are not ( `geometric` ; [59]). Here, we further explore, validate, and compare the modules by aligning them with respect to whole-brain maps made available as part of [60]. In total, we considered 45 maps that included receptor densities, gene expression, myelination status, evolutionary and developmental expansion, and synaptic density (among others). Here, we assess whether modules are “enriched” for these maps. That is, whether the module boundaries delineate spatial boundaries in each map. The procedure for doing so is illustrated using the serotonin receptor 5HTA as an example (see panel _a_ for spatial distribution on cortical surface0. This map vectorized ( _b_ ), and transformed into a matrix by calculating its outer product ( _c_ ). We then compare the matrix to module co-assignment matrices (and example is shown in _d_ ). Specifically, we calculate the mean values of all within- and between-module elements ( _e_ and _f_ ) and subsequently calculate the difference in these means ( _g_ ). In parallel, we repeat this procedure for 1000 spatially constrained permutations of the map (spin test). The spin tests generate a null distribution against which we compare the empirical (observed) difference in means _via_ the z-score. Larger _z_ values indicate greater modular “enrichment”. We perform this entire procedure for four sets of modules – signed and geometric model for both the asymmetric, weighted, and signed matrix as well as the fiber density matrix. Panel _i_ shows the distribution of _z_ -scores. In general, we find that the AWS model always outperforms the fiber density matrix–i.e. leads to greater _z_ scores (paired sample _t_ -test; maximum _p_ = 0 _._ 0017). We also tested enrichment at the level of individual models ( _j_ ). Briefly, the mean within-module value for each brain map vector was calculated and compared to a null distribution (spin tests after excluding modules of fewer than ten nodes). The _z_ values were transformed into _p_ values and _p <_ 0 _._ 05 applied to determine statistical significance. In the margins of _j_ , we show the number of maps that were significantly enriched for each module. 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.19.519033; this version posted December 19, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

32 

**==> picture [509 x 195] intentionally omitted <==**

FIG. S13. **Replication of main effects using hyper-dense tract-tracing data from mice.** ( _a_ ) Logarithm of anatomical connection weights. ( _b_ ) Estimated weights using linear model. ( _c_ ) Functional connectivity (correlation). ( _d_ ) Two-dimensional histogram of predicted and observed activity across all regions and mice. ( _e_ ) Scatterplot of estimated edge weights versus Euclidean distance. ( _f_ ) Communities estimated by applying modularity maximization to the estimated edge weight matrix. ( _g_ ) Communities estimated by applying modularity maximization to the anatomical connectivity matrix. Panels _h_ and _i_ show module coassignment matrices for the two versions of edge weights. Panel _j_ shows the difference in edge weights. ( _k_ ) Areal coassignment matrix. Panels _l_ - _n_ show laterality of detected communities, similarity of detected partitions with respect to areal labels (adjusted Rand index), and the modularity of the detected partitions. 

**==> picture [509 x 129] intentionally omitted <==**

FIG. S14. **Signed asymmetry between incoming and outgoing edges is most common between functional brain systems.** ( _a_ ) The number of sign asymmetric edges across 95 subjects organized by system. ( _b_ ) Proportion of existing edges that exhibit sign asymmetry within systems _versus_ between systems. 

**==> picture [509 x 91] intentionally omitted <==**

FIG. S15. **Relationship between fitness of the linear model and modularity of the functional connnectivity matrix.** ( _a_ ) Relationship between modularity (Q) and mean square error (MSE). ( _b_ ) Relationship between modularity (Q) and the correlation between predicted and observed time series. 

