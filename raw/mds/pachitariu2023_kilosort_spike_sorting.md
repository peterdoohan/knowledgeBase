bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **Solving the spike sorting problem with Kilosort** 

## **Marius Pachitariu**[1†] **, Shashwat Sridhar**[2] **, Carsen Stringer**[1] 

1HHMI Janelia Research Campus, 

> 2Department of Ophthalmology, University Medical Center G¨ottingen. G¨ottingen 

> † correspondence to pachitarium@hhmi.org 

**Spike sorting is the computational process of extracting the firing times of single neurons from recordings of local electrical fields. This is an important but hard problem in neuroscience, complicated by the nonstationarity of the recordings and the dense overlap in electrical fields between nearby neurons. To solve the spike sorting problem, we have continuously developed over the past eight years a framework known as Kilosort. This paper describes the various algorithmic steps introduced in different versions of Kilosort. We also report the development of Kilosort4, a new version with substantially improved performance due to new clustering algorithms inspired by graph-based approaches. To test the performance of Kilosort, we developed a realistic simulation framework which uses densely sampled electrical fields from real experiments to generate non-stationary spike waveforms and realistic noise. We find that nearly all versions of Kilosort outperform other algorithms on a variety of simulated conditions, and Kilosort4 performs best in all cases, correctly identifying even neurons with low amplitudes and small spatial extents in high drift conditions.** 

## 1 **Introduction** 

- 2 Classical spike sorting frameworks require a sequence 3 of operations, which can be categorized into prepro4 cessing, spike detection, clustering and postprocess5 ing. Modern approaches have improved on these 6 steps by introducing new algorithms. Some frame7 works [1–3] took advantage of new clustering algo8 rithms such as density-based approaches [4] or ag9 glomerative approaches using bimodality criteria [5]. 

- 10 In contrast, the original Kilosort [6] used a simple clus11 tering approach (scaled K-means), but combined two 12 steps of the pipeline into one (spike detection + cluster13 ing = template learning) and added an extra matching 14 pursuit step for detecting overlapping spikes, some15 times referred to as solving the “collision problem” [7]. 

- 15 16 An important consideration for these early modern 17 algorithms was the requirement for additional human 18 curation, as the clustering results were imperfect in 19 many applications. Thus, algorithms like Kilosort bi20 ased the clustering process towards “over-splitting”, 21 producing more clusters than the number of real units 22 in the data, so that human curation would consist pri23 marily of merges, which are substantially easier to per24 form than splits. To facilitate human curation of the 25 automated results, a modern graphical user interface 26 called Phy was developed, which is now used for vi27 sualization by several of the most popular frameworks 28 including all versions of Kilosort [8]. 

- 29 Why was human curation still necessary for these 30 early modern methods? One of the main reasons 31 was the non-stationary nature of data from real ex32 periments. The electrical field of a unit sampled by 33 a probe, called a spike waveform, should be fixed and 

- 34 reproducible across long time periods. Yet in many 35 experiments, the shape of the waveform appeared to 36 change over the course of hours, and sometimes much 37 faster. The main reason for these changes was identi38 fied as vertical probe movement or “drift”, using high39 density electrodes [9]. Drift is primarily caused by fac40 tors such as tissue relaxation after probe insertion and 41 animal movements during behavior. Correcting for this 42 drift resulted in substantial improvements in spike sort43 ing performance. Kilosort2 used a “drift tracking” ap44 proach for this, while Kilosort2.5 developed a stan45 dalone drift correction method that directly modified 46 the voltage data to shift certain channels up or down 47 by appropriate distances (see Methods for drift track48 ing, and Methods in [9] for drift correction). The drift 49 correction step has been inherited by all Kilosort ver50 sions since 2.5. 

- 51 The main goal of this paper is to describe the devel52 opment of Kilosort4 and demonstrate its performance. 53 Some of the algorithmic steps in Kilosort4 are inherited 54 from previous versions (i.e. drift correction), while oth55 ers build on top of previous versions (i.e. template de56 convolution), while others are completely new (i.e. the 57 graph-based clustering approach). Except for drift cor58 rection, which was previously described in detail [9], 59 the other algorithmic steps are not described in the lit60 erature, and we add detailed descriptions in the Meth61 ods (see Table 1 for an overview). We also developed 62 a new simulation-based framework for benchmarking 63 spike sorting algorithms, which uses several realistic 64 drift patterns and dense electrical fields inferred from 65 real experiments. We show using the benchmarks that 66 Kilosort4 performs very well and outperforms all other 67 algorithms across a range of conditions. 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

|pre-processing<br>template deconvolution<br>clustering & post-processing|pre-processing<br>template deconvolution<br>clustering & post-processing|pre-processing<br>template deconvolution<br>clustering & post-processing|pre-processing<br>template deconvolution<br>clustering & post-processing|pre-processing<br>template deconvolution<br>clustering & post-processing|
|---|---|---|---|---|
|algorithms|language|fltering &<br>whitening<br>drift<br>correction|template<br>deconv-<br>olution<br>template<br>learning<br>deconv.<br>during<br>learning<br>new<br>templates<br>from residual|clustering<br>splits<br>merges|
|Kilosort 1<br>(2016)<br>Kilosort 2<br>(2018)<br>Kilosort 2.5<br>(2020)<br>Kilosort 3<br>(2021)<br>Kilosort 4<br>(2023)|matlab<br>+CUDA<br>matlab<br>+CUDA<br>matlab<br>/**python**<br>+CUDA<br>matlab<br>+CUDA<br>python<br>+**pytorch**|yes 1<br>_−_<br>yes<br>_−_<br>(only**tracking***)<br>yes<br>**yes** 2<br>yes<br>yes<br>yes<br>yes|yes1<br>scaled<br>k-means1<br>_−_<br>_−_<br>yes<br>scaled<br>k-means<br>**yes***<br>**threshold**<br>**crossing***<br>yes<br>scaled<br>k-means<br>yes<br>threshold<br>crossing<br>yes<br>**recursive**<br>**pursuit***<br>_−_<br>_−_<br>yes<br>**graph**<br>**clustering***<br>_−_<br>_−_|_−_<br>_−_<br>_−_<br>_−_<br>**bimodality**<br>**pursuit***<br>**yes***<br>_−_<br>bimodality<br>pursuit<br>yes<br>**recursive**<br>**pursuit***<br>yes<br>yes<br>**graph**<br>**clustering***<br>**merging**<br>**tree***<br>yes|



**Table 1: The evolution of kilosort.** New features added after Kilosort 1 are bolded in the version they were first introduced.[1] described in Pachitariu et al, 2016 _bioRxiv_ ,[2] described in Steinmetz et al, 2021 _Science_ , _[∗]_ described in this paper. 

## **Results** 

## 68 

- 69 To be able to process the large amounts of data from 70 modern electrophysiology, all versions of Kilosort are 71 implemented on the GPU. Kilosort4 is the first ver72 sion fully implemented in python and using the pytorch 73 package for all its functionality, thus making the old 74 CUDA functions obsolete [10, 11]. Pytorch allows the 75 user to switch to a CPU backend which may be suf76 ficiently fast for testing on small amounts of data but 77 is not recommended for large-scale data. All versions 78 of Kilosort take as input a binary data file, and out79 put a set of “.npy” files that can be used for visualiza80 tion in Phy [8]. To set up a Kilosort4 run, we built a 81 pyqtgraph GUI which replicates the functionality of the 82 Matlab GUI, and can assist users in debugging due 83 to several diagnostic plots and summary statistics that 84 are displayed [12] (Figure S1). 

- 85 The preprocessing step in all versions of Kilo86 sort includes temporal filtering and channel whiten87 ing (see Methods). These linear operations reduce 88 the strong spatiotemporal correlations of the electrical 89 background in the brain, which is mainly formed by the 90 electrical discharge of units that are too far from the 91 probe to be identified as single units. This step is ac92 celerated in Kilosort4 through the use of explicit convo93 lutions in place of a Butterworth filter. Drift correction is 94 an additional preprocessing step that was introduced 95 in Kilosort2.5 and maintained in all subsequent ver96 sions (see Methods of [9]). Unlike previous versions, 97 Kilosort4 no longer needs to generate an intermediate 98 file of processed data, as all preprocessing operations 99 are fast enough to be performed on-demand. 

## **Template deconvolution** 

## 100 

101 We refer to the spike detection and feature extraction 102 steps jointly as “template deconvolution”. This mod103 ule requires a set of templates which correspond to 104 the average spatiotemporal waveforms of neurons in 105 the recording. The templates are used in the match106 ing pursuit step for detecting overlapping spikes [6]. A 107 template deconvolution step has been used in all ver108 sions of Kilosort, but the details of the template learn109 ing have changed (see Methods). In Kilosort 3 and 4, 110 the template deconvolution serves an extra role as a 111 feature extraction method with background correction. 112 The template deconvolution pipeline has the same 113 format for both Kilosort 3 and 4 (Figure 1a). A set 114 of initial spike waveforms are extracted from prepro115 cessed data using a set of universal templates (Fig116 ure 1b,c). The features of these spikes are then clus117 tered, using either the recursive pursuit algorithm from 118 Kilosort3 (see Methods), or the graph-based algorithm 119 from Kilosort4 (described in Figure 2). The centroids 120 of the clusters are the “learned templates”, which are 121 then aligned temporally (Figure 1d). The templates 122 are compared to each other by cross-correlation and 123 similar templates are merged together to remove du124 plicates. The learned templates are then used in the 125 matching pursuit step, which iteratively finds the best 126 matching templates to the preprocessed data and sub127 tracts off their contribution. The subtraction is a critical 128 part of all matching pursuit algorithms and allows the 129 algorithm to detect spikes that were overlapped by the 130 subtracted ones. The final reconstruction of the data 131 with the templates is shown in Figure 1e. The residual 132 is the difference between data and reconstruction, and 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [500 x 291] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Feature extraction pipeline<br>b Data (preprocessed) e Reconstruction f Residual (final model)<br>0 0 0<br>20 20 20<br>40 40 40<br>60 60 60<br>5 ms<br>c Universal templates (30 / 45,960) 2 0 2 g Features from universal templates h Features from learned templates i Features with background subtracted<br>d Learned templates (30 / 669)<br>t-SNE 1<br>j Spike distributions (75,546 out of 3,777,346 spikes)<br>template norm<br>15 21 30<br>40<br>20<br>800 900 1000 1100 1200 1300 1400<br>depth (um)<br>channel<br>t-SNE 2<br>lateral (um)<br>**----- End of picture text -----**<br>


**Figure 1: Spike detection and feature extraction. a,** Schematic of the pipeline for detecting spikes and extracting spikes features. **b,** Short segment of preprocessed data over 70 channels and 1,000 timepoints (data from [13]). **c,** Example universal templates centered at a single position on the probe. Templates are repeated at 1536 positions for a Neuropixels probe. **d,** Example learned templates centered at different positions on the probe. **e,** Reconstruction of the data in **b** based on the inferred templates and spike times. **f,** Residual after subtracting the reconstruction from the data. **g-i,** t-SNE visualization of spike features from a 40µm segment of the probe. Spike features were extracted using either universal templates ( **g** ) or learned templates without ( **h** ) or with ( **i** ) background subtraction. **j,** Spatial distribution of a subset of the final extracted spikes colored by their template norm. 

133 can be informative if the algorithm fails to find some 134 units (Figure 1f). 

- 135 This template learning step from Kilosort 3/4 is dif136 ferent from the one in Kilosort1 (see [6]), and both 137 are different from the equivalent step in Kilosort 2/2.5 138 (see Methods). Furthermore, the templates of Kilo139 sort1 are in one-to-one correspondence with the final 140 inferred units which are exported for manual curation. 141 This correspondence is weaker in Kilosort 2/2.5, be142 cause a post-processing step is used to perform splits 143 and merges on these templates (see Methods). Fi144 nally, in Kilosort 3/4 these templates are completely 145 discarded after being used to extract spikes. This is 146 because more powerful clustering algorithms can be 147 applied to the spike features once they have been ex148 tracted with template deconvolution. The “corrected” 149 or deconvolved features have three additional proper150 ties compared to the features detected with universal 151 templates or more generally detected with any clas152 sical threshold crossing method: 1) they contain all, 153 or a majority of spikes from the clustered units, even 

- 154 the ones that are overlapped by larger, bigger spikes; 155 2) they group spikes together by templates, which can 156 be used to more precisely assign spikes to their best 157 channels for batched clustering across channels; 3) 158 they can be computed after subtraction of the back159 ground produced by all other spikes (Figure 1e). 

- 160 These properties have a substantial effect on the 161 features, allowing for better clustering. Figure 1g-i 162 show the t-SNE embeddings of three different sets of 163 features from spikes detected over a 40um stretch of a 164 Neuropixels probe. The features computed with the 165 learned templates with background subtraction (Fig166 ure 1i) are embedded as more uniform, Gaussian-like 167 clusters. Without background subtraction, each cluster 168 is surrounded by a patterned envelope of points due to 169 the contribution of overlapping spikes, and these pat170 terns can be easily mistaken for other clusters (Fig171 ure 1g,h). The visualization in Figure 1i can be used to 172 get an impression of a small section of the data with173 out performing any clustering at all. To visualize the 174 distribution of spikes over a larger portion of a probe, 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [500 x 348] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Neighbor clustering b Initial clustering (27 clusters) c Merging tree g Waveforms of refractory units<br>cluster 3<br>cluster 1 cluster 2<br>#AP=  3901 65372 14696 925<br>t-SNE 1 36023 2532 51841 39792 1509<br>d No merge  Merge  Merge  e After merges (13 clusters) h Auto- and cross- correlograms and regression axes<br>f<br>Only refractory units (9 clusters)<br>regression axis regression axis regression axis<br>50 auto- cross-<br>correlogram correlogram<br>0<br>20 0 20<br>samplestime  auto-correlogram<br>i Refractory units on the probe<br>40<br>20<br>400 500 600 700 800 900 1000<br>depth (um)<br>modularity index<br>t-SNE 2<br>PC of residual<br>counts<br># pairs<br>lateral (um)<br>**----- End of picture text -----**<br>


**Figure 2: Clustering spike with graph-based methods. a,** Illustration of the iterative re-assignment process. At each iteration, a node is assigned to the cluster which has most of its neighbors. A penalty is used to compensate for larger clusters having more neighbors. This process is initialized with 200 clusters obtained from K-means++ [14] and converges to a smaller set of clusters in tens of iterations. **b,** Example clustering produced by this process overlaid on a t-SNE visualization (data from [15]). **c,** Merging tree formed by merging clusters according to the modularity cost function. Colored branches correspond to merges that were accepted. The tree is traversed from top to bottom to make split/merge decisions. **d,** Criteria for performing a merge/split decision in the merging tree: (top) projection across the regression axis has to be bimodal, (bottom) cross-correlogram of spike times cannot be refractory (dashed line indicates approximate refractory criterion). **e,** Final result of the clustering algorithm after merges. **f,** Same as **e** with non-refractory units grayed out. **g,** Average waveforms of units with refractory periods and the total number of spikes in each cluster. **h,** (diagonal) Auto-correlograms; (below diagonal) projection on regression axes; (above diagonal) cross-correlograms. **i,** Subset of spikes colored by their final assigned clusters. Non-refractory units shown in gray. 

- 175 we plot a subset of spikes at their inferred XY positions 176 (Figure 1j). The spikes are colored according to ampli177 tudes, which tends to be uniform for spikes from the 178 same unit. 

## **Graph-based clustering with merging trees** 

179 

- 180 We developed two new clustering algorithms for spike 181 features extracted by template deconvolution. In Kilo182 sort3, we developed an algorithm that uses a recursive 183 application of the bimodality pursuit algorithm from 184 Kilosort2, which in turn had been developed to auto185 matically find potential splits within clusters (see Meth186 ods). In Kilosort4 we developed a graph-based clus187 tering method. This approach first constructs a graph 188 of points connected to their nearest neighbors in Eu- 

- 189 clidean space, then constructs a cost function from 190 the graph properties to encourage the clustering of 191 nodes. A popular cost function is “modularity”, which 192 counts the number of graph edges inside a cluster 193 and compares them to the expected number of edges 194 from a disorganized, unclustered null model [16]. Well195 known implementations of modularity optimization are 196 the Leiden and Louvain algorithms [17, 18]. Applied 197 directly to spike features, these established algorithms 198 fail in a few different ways: 1) difficulty partitioning clus199 ters with very different number of points; 2) very slow 200 processing speed for hundreds of thousands of points; 201 3) cannot use domain knowledge to make merge/split 202 decisions. 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

203 To remedy these problems, we developed a new 204 graph-based algorithm, in which the clusters are de205 fined as the stationary points of an iterative neighbor 206 reassignment algorithm based on the modularity cost 207 function (Figure 2a and see Methods). This method 208 allowed us to find more of the small clusters com209 pared to a straightforward application of the Leiden al210 gorithm (Figure 2b). To improve the processing speed, 211 which typically grows quadratically in the number of 212 data points, we developed a landmark-based version 213 of the algorithm which uses nearest neighbors within a 214 subset of all data points. The application of this algo215 rithm resulted in oversplit clusters, which required ad216 ditional merges using domain knowledge. To find the 217 best merges efficiently, we used the modularity cost 218 function to construct a “merging tree” (Figure 2c). Po219 tential splits in this tree were tested using two crite220 ria: 1) a bimodal distribution of spike projections along 221 the regression axis between the two sub-clusters (Fig222 ure 2d, top), and 2) whether the cross-correlogram 223 was refractory or not (Figure 2d, bottom). 224 This clustering algorithm was applied to groups of 225 spikes originating from the same 40 µm vertical sec226 tion of the probe. After all sections were clustered, an 227 additional merging step was performed which tested 228 the refractoriness of the cross-correlogram for all pairs 229 of templates with a correlation above 0.5, similar to the 230 global merging step from previous versions (2/2.5/3). 231 The final results are shown in (Figure 2e). Units that 232 did not have a refractory period are shown grayed 233 out in (Figure 2f); they likely correspond to neurons 234 that were not well isolated. A quick overview of the 235 units identified on this section of the probe shows that 236 all units had refractory auto-correlograms, all pairs 237 of clusters had bimodal projections on their respec238 tive regression axes, and all pairs of clusters had flat, 239 non-refractory cross-correlograms (Figure 2h). These 240 properties together indicate that these nine units cor241 respond to nine distinct, well-isolated neurons. These 242 clusters can also be visualized on the probe, in their 243 local contexts (Figure 2i). 

## 244 **Electrical simulations with realistic drift** 

245 To test the performance of Kilosort4 and previous ver246 sions, we next developed a set of realistic simulations 247 with different drift patterns. Constructing such a sim248 ulation requires knowledge of the dense electric fields 249 of a neuron, because different drift levels sample the 250 electric field at different positions. We obtained this 251 knowledge by sampling neurons from recordings with 252 large drift (Figure 3a) from a public repository of more 253 than 500 Neuropixels recordings from the IBL con254 sortium (Figure 3b). In this repository, we found 11 255 recordings with large, continuous drift that spanned 

256 over at least 40 µm, which is the spatial repetition 257 period of a Neuropixels probe. We separately built 258 two pools of units: one from neurons that were well259 isolated and had refractory periods, and one from 260 multi-unit activity which had refractory period contam261 inations. Drift levels were discretized in 2 µm inter262 vals, and only units with enough spikes in each drift 263 interval were considered. The average waveforms at 264 five positions is shown for a few examples (Figure 3c 265 and Figure S2a,b). To simulate drift, we generated 266 a single average drift trace and additional deviations 267 for each channel to account for heterogeneous drift. 268 Spike trains were generated using shuffled inter-spike 269 intervals from real units. For each simulation, a set of 270 600 ground-truth neurons were generated in this fash271 ion, with amplitudes drawn from a truncated exponen272 tial distribution which matched the amplitudes in real 273 datasets. Another 600 “multi-units” were added with 274 lower amplitudes (Figure 3d). Additional independent 275 noise was added on each channel. The resulting sim276 ulation was “un-whitened” across channels using a ro277 tation matrix from real experiments (Figure S2c). 

278 This simulation framework allowed us to test many 279 algorithms across many simulated experimental con280 ditions [2, 3, 6, 19–23]. All algorithms other than Kilo281 sort4 were run through their respective SpikeInterface 282 wrappers to ensure consistent processing, and param283 eter adjustments were made in some cases to improve 284 results (see Methods) [24]. The latest algorithm ver285 sions as of December 2022 were used in all cases, 286 which are often substantially different from the initial 287 published versions [2, 3]. Results for all conditions are 288 shown in (Figure 3e-j) and quantified in Table 2. All 289 the algorithms had reasonable run times (within 2x the 290 duration of the simulations). The drift conditions we 291 chose were based on patterns of drift identified in the 292 IBL dataset (Figure S3): no drift, medium drift, high 293 drift, fast drift and step drift. The medium drift condi294 tion was matched to the median recording from the IBL 295 dataset. The high drift condition had a drift range span296 ning the entire 40 µm spatial period of the probe, thus 297 sampling all potential shapes of each waveform. The 298 fast drift condition uses drift on the timescale of sec299 onds and sub-seconds, to simulate fast head move300 ments such as during a behavioral task. The step 301 drift condition simulates abrupt changes during an ex302 periment, which are common in the IBL dataset and 303 likely caused by excessive animal movements. This 304 condition also simulates chronic recordings made on 305 different days, where the probe is stationary on each 306 day, but moves in-between days. Since this condition 307 was the most difficult for all algorithms, we also tested 308 whether an aligned sites probe configuration (such as 309 in Neuropixels 2) improves the results. 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [504 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
a 50 drift of recording used for simulation c example unit 1 d 0 example simulation, before indep. high-freq. noise added<br>0 1140 m380 m 10<br>1900 m<br>50 2680 m3440 m -20 m -10 m 0 m 10 m 20 m 20<br>0 30 60 30<br>b distribution of drift across IBL recordingstime (min) example unit 2 40<br>100 median = 9.5 m<br>50<br>60<br>0 1 10 100 -20 m -10 m 0 m 10 m 20 m 5 ms 2 0 2<br>e 20 no drift drift range ( m)1.0 kilosort2.5 kilosort3 h 20 fast drift 1.0<br>kilosort2 kilosort4<br>10 spykingcircus2 mountainsort4 spykingcircus 10<br>0 0.5 ironclust 0 0.5<br>10 probe herdingspikes hdsortkilosort 10<br>tridesclous2<br>20 0.0 20 0.0<br>0 15 30 45 0 100 200 300 400 500 600 0 5 10 0 100 200 300 400 500 600<br>time (min) sorted units<br>f 20 medium drift 1.0 i 20 step drift 1.0<br>10 10<br>0 0.5 0 0.5<br>10 10<br>20 0.0 20 0.0<br>0 15 30 45 0 100 200 300 400 500 600 0 15 30 45 0 100 200 300 400 500 600<br>g 20 high drift 1.0 j 20 step drift, aligned 1.0<br>10 10<br>0 0.5 0 0.5<br>10 10<br>20 0.0 20 0.0<br>0 15 30 45 0 100 200 300 400 500 600 0 15 30 45 0 100 200 300 400 500 600<br>m)<br>est depth (<br>channel<br>count<br>m)<br>sim depth ( score<br>**----- End of picture text -----**<br>


**Figure 3: Spike sorting simulations and benchmarks. a,** Example drift traces at different depths for a recording with large drift from the IBL dataset. **b,** Distribution of drift ranges across all IBL recordings. Drift range was defined as the difference between the 5[th] and 95[th] percentile of the median drift across channels. **c,** Waveforms of example units at multiple drift positions. **d,** Segment of a simulated recording with drift over 70 channels and 1,000 timepoints. **e-j,** Accuracy of spike-sorting algorithms on simulations with various drift profiles. Left: simulated drift traces. Right: sorted accuracies for 600 ground truth units from each simulation matched to the results of each algorithm. The accuracy score is defined as 1 - FP - FN, where FP is the false positive rate and FN is the false negative rate (see Methods). **e,** No drift. **f,** Medium drift. **g,** High drift. **h,** Fast drift (10 minutes out of 45 minutes plotted for visibility). **i,** Step drift. **j,** Step drift for a probe with aligned sites. 

|algorithms|no drift|medium drift|high drift|fast drift|step|drift<br>step drift<br>aligned|runtime<br>(minutes|
|---|---|---|---|---|---|---|---|
|Kilosort4|**526**|**534**|**477**|**506**|**43**|**6**<br>**512**|25.4_±_0|
|Kilosort3|495|454|283|446|25|3<br>415|69.0_±_2|
|Kilosort2.5|479|456|321|460|27|4<br>433|24.0_±_0|
|Kilosort2|469|454|408|444|11|0<br>71|23.6_±_0|
|Kilosort[6]|163|147|54|111|7|4|51.8_±_0|
|IronClust[1,1|9]<br>331|301|239|254|1|1|34.9_±_0|
|MountainSort|4[3]<br>316|283|124|262|2|1|82.8_±_4|
|SpyKING CIR|CUS[2]<br>348|301|135|285|6|4|65.6_±_2|
|SpyKING CIR|CUS 2[20]<br>123|131|62|93|7|1|32.9_±_2|
|HDSort[21]|159|5|19|10|1|1|42.5_±_1|
|HerdingSpike|s[22]<br>25|21|6|13|0|0|24.7_±_0|
|Tridesclous2[|23]<br>7|12|3|2|0|1|7.8_±_0.|



**Table 2: Number of correctly identified units in simulations.** Number of detected units that matched ground truth units with a 1 - FP - FN score greater than 0.8, for each simulation. Runtime averaged over the 6 simulations of 45 minutes each _±_ s.e.m. (RTX 3090 + 2x Intel Xeon Gold 6348 + SSD). 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **Benchmarks** 

## 310 

311 Kilosort 2, 2.5, 3 and 4 outperformed all other algo312 rithms in all cases. Kilosort 1 performed poorly, due 313 to the lack of drift correction and its bias towards over314 split units. The nearest competing algorithm in per315 formance was IronClust developed by the Flatiron In316 stitute, which accounts for drift in a different way from 317 Kilosort [19]. IronClust generally found _∼_ 50% of all 318 units, compared to the 80-90% found by Kilosort4 (Ta319 ble 2). Many of the algorithms tested did not have ex320 plicit drift correction. Some of these (SpyKING CIR321 CUS, MountainSort4) matched the IronClust perfor322 mance at no drift, medium and fast drift, but their 323 performance deteriorated drastically with higher drift 324 [2, 3]. Among all algorithms with explicit drift correc325 tion (Kilosort 2.5, 3 and 4), Kilosort4 consistently per326 formed better due to its improved clustering algorithm, 327 and in some cases performed much better (on the step 328 drift conditions). As we suspected, the aligned sites 329 condition recovered the full performance of Kilosort4 330 on the step drift simulations, likely because it reduces 331 the vertical sampling from 40 µm to 20 µm. 

332 We also tested how well the drift amplitudes were 333 identified by the drift detection algorithm from Kilo334 sort2.5 (in the Kilosort4 implementation) and found 335 good performance in all cases, except for the fast drift 336 condition where the timescale of drift was faster than 337 the 2 sec bin size used for drift correction (Figure S4). 338 Much smaller bin sizes cannot be used for drift esti339 mation, since a minimum number of spike samples is 340 required. Nonetheless, the results show that Kilosort 341 still performed well in this case, likely due to the ro342 bustness of the clustering algorithms. Finally, we cal343 culated the performance of the algorithms as a func344 tion of the ground truth firing rates, amplitudes and 345 spatial extents (Figure S5). The dependence of Kilo346 sort4 on these variables was minimal. However, some 347 of the other algorithms had a strong dependence on 348 amplitude, which could not be improved by lowering 349 spike detection thresholds. Also, many algorithms per350 formed more poorly when the waveforms had a large 351 spatial extent as opposed to having their electrical 352 fields concentrated on just a few channels. 

## **Discussion** 

## 353 

354 Here we described Kilosort, a computational frame355 work for spike sorting electrophysiological data. The 356 latest version, Kilosort4, represents our cumulative de357 velopment efforts over the past eight years, contain358 ing algorithms like template deconvolution (from Kilo359 sort1), drift correction (from Kilosort2.5), as well as 360 completely new clustering algorithms based on graph 361 methods. Furthermore, Kilosort4 was re-written from 362 the ground up in Python, an open-source programming 

- 363 language, using the pytorch package for GPU acceler364 ation. The popularity of pytorch/python should ensure 365 that Kilosort continues to be further improved and de366 veloped. We have also developed a new simulation 367 framework to improve the benchmarking of spike sort368 ing algorithms. Our simulations contain realistic back369 ground noise and realistic drift with diverse properties, 370 and they are qualitatively similar to real recordings with 371 Neuropixels probes. Kilosort4 outperformed all other 372 algorithms on all simulation conditions, in some cases 373 by a large margin. 

374 All versions of Kilosort have been developed pri375 marily on Neuropixels data. However, since Kilosort 376 adapts to the data statistics, it has been used widely 377 on other types of probes and other recording methods. 378 Some types of data do require special consideration. 379 For example, some data cannot be drift corrected ef380 fectively due to either lacking a well-defined geometry 381 (tetrodes), or due to the vertical spacing between elec382 trodes being too high (more than 40 µm). This con383 sideration also applies to data from single electrodes 384 such as in a Utah array. Kilosort2 might be a bet385 ter algorithm for such data, because it performs drift 386 tracking without requiring an explicit channel geometry. 387 Based on our benchmarks, Kilosort2 with drift tracking 388 performs similarly to Kilosort2.5 with drift correction, 389 except for the cases where step drift is present. Data 390 from retinal arrays does not require drift correction and 391 may be processed through Kilosort4, but it may require 392 large amounts of GPU RAM for arrays with thousands 393 of electrodes and thus would be better split into multi394 ple sections and processed separately. Another spe395 cial type of data are cerebellar neurons with complex 396 spikes, which can have variable, complex shapes that 397 are not well matched by a single template, and spe398 cialized algorithms for detection may be required [25]. 399 Another special type of recording comes from chronic 400 experiments over multiple days, potentially separated 401 by long intervals. While we have not explicitly tested 402 such recordings here, the benchmark results for the 403 step drift simulation are encouraging because this sim404 ulation qualitatively matches changes we have seen 405 chronically with implanted Neuropixels 2 electrodes 406 [9]. 

407 The problem of identifying neurons from extracellu408 lar recordings has a long history in neuroscience. The 409 substantial progress seen in the past several years 410 stems from multiple simultaneous developments: en411 gineering of better devices (Neuropixels and others), 412 better algorithms (Kilosort and others), improved vi413 sualizations of spike sorting results (Phy) and multi414 ple rounds of user feedback provided by a quickly415 expanding community. Computational requirements 416 have sometimes influenced the design of new probes, 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

417 such as the aligned sites and reduced vertical spacing 418 of Neuropixels 2 which were motivated by the need 419 for better drift correction. Such computational consid420 erations will hopefully continue to influence the devel421 opment of future devices to increase the quality and 422 quantity of neurons recovered by spike sorting. 

## **Acknowledgments** 

## 423 

424 This research was funded by the Howard Hughes 425 Medical Institute at the Janelia Research Campus. 

## **Author contributions** 

## 426 

427 M.P. designed and built all versions of Kilosort. S.S. 428 wrote the python GUI and C.S. developed the drifting 429 simulations. C.S. and M.P. performed data analysis, 430 coordinated the project and wrote the paper. 

## **Code availability** 

## 431 

432 Kilosort4 will be available upon publication at https: 433 //www.github.com/mouseland/kilosort. Version 434 2, 2.5 and 3 are currently available at the same link. 

## **Data availability** 

## 435 

436 We used datasets shared by Nick Stein437 metz and the International Brain Laboratory 438 [13, 15]. The datasets are available at at http: 439 //data.cortexlab.net/singlePhase3/ and 440 https://ibl.flatironinstitute.org/public/. 

## **Methods** 

## 441 

442 The Kilosort4 code library is implemented in Python 3 443 [10] using pytorch, numpy, scipy, scikit-learn, faiss-cpu 444 , numba and tqdm [11, 26–32]. The graphical user in445 terface additionally uses PyQt and pyqtgraph [12, 33]. 446 The figures were made using matplotlib and jupyter447 notebook [34, 35]. Kilosort 2, 2.5 and 3 were imple448 mented in MATLAB. 

449 We demonstrate the Kilosort4 method step450 by-step in Figure 1 and Figure 2. In Fig451 ure 1 an electrophysiological recording from Nick 452 Steinmetz was used (”Single Phase 3”; [13] 453 and https://figshare.com/articles/_Single_ 454 Phase3_Neuropixels_Dataset/7666892). In Fig455 ure 2 an electrophysiological recording from the In456 ternational Brain Laboratory was used (id: 6f6d2c8e457 28be-49f4-ae4d-06be2d3148c1; [15]). Both record458 ings were performed with a Neuropixels 1.0 probe, 459 which has 384 sites organized in rows of two with a 460 vertical spacing of 20 µm, a horizontal spacing of 32 461 µm. Due to the staggered design (16 µm horizontal 462 offset between consecutive rows), the spatial repeti463 tion period of this probe is 40 µm. 

## **Graphical user interface (GUI)** 

## 464 

- 465 We developed a graphical user interface to facilitate 466 the user interaction with Kilosort4. This interface was 467 built using pyqtgraph which itself uses PyQt [12, 33], 468 and it replicates the Matlab GUI which was originally 469 built for Kilosort2 by Nick Steinmetz. The GUI allows 470 the user to select a data file, a configuration file for the 471 probe, and set the most important parameters manu472 ally. In addition, a probe file can be constructed directly 473 in the GUI. After loading the data and configuration file, 474 the GUI displays a short segment of the data, which 475 can be used to determine if the configuration was cor476 rect. Typical mistakes are easy to identify. For example 477 if the total number of channels is incorrect, then the 478 data will appear to be diagonally “streaked” because 479 multi-channel patterns will be offset by 1 or 2 extra 480 samples on each consecutive channel. Another typ481 ical problem is having an incorrect order of channels, 482 in which case the user will see clear single-channel but 483 no multi-channel waveforms. Finally, the GUI can pro484 duce several plots during runs which can be used to 485 diagnose drift correction and the overall spike rates of 486 the recording. 

## 487 **Algorithms for Kilosort4** 

- 488 In the next several sections we describe the algorith489 mic steps in Kilosort4. Some of these steps are inher490 ited or evolved from previous versions. For clarity, we 491 describe each of the steps exactly as they are currently 492 used in Kilosort4. If a previous version of Kilosort is dif493 ferent, we clearly indicate the difference. We dedicate 494 a completely separate section below for algorithms not 495 used in Kilosort4 but used in previous versions. 

496 Many of the processing operations are performed 497 on a per-batch basis. The default batch size is _NT_ = 498 60 _,_ 000, and it was _NT_ = 65 _,_ 536 in versions 2/2.5/3 499 and _NT_ = 32 _,_ 768 in version 1. The increase in batch 500 size in Kilosort2 was designed to allow better per501 batch estimation of drift properties. Due to the per502 batch application of temporal operations, we require 503 special considerations at batch boundaries. Every 504 batch of data is loaded with left and right padding of 505 _nt_ additional timepoints on each side ( _nt_ = 61 by de506 fault). On the first batch, the left pad consists of the 507 first data sample repeated _nt_ times. The last batch is 508 typically less than a full batch size of _NT_ . For consis509 tency, we pad this batch to the full _NT_ size using the 510 repeated last value in the data. 

511 The clustering in Kilosort 3/4 is done in small 40 µm 512 sections of the probe, but including information from 513 nearby channels and including spikes extracted at all 514 timepoints. 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 515 **Preprocessing** 

516 Our standard preprocessing pipeline includes a se517 quence of operations: common average referencing 518 (CAR), temporal filtering, channel whitening and drift 519 correction. In Kilosort4, all these steps are performed 520 on demand whenever a batch of data is needed. In 521 all previous versions, the preprocessing of the entire 522 data was done first and the preprocessed data was 523 stored in a separate binary file. Drift correction was 524 introduced in Kilosort 2.5. 

## 525 _Common average referencing_ 

526 The first operations applied to data are to remove the 527 mean across time for each batch, followed by removing 528 the median across channels (common average refer529 encing or CAR). The CAR can substantially reduce the 530 impact of artifacts coming from remote sources such 531 as room noise or optogenetics. The CAR must be 532 applied before the other filtering and whitening oper533 ations, so that large artifacts do not ”leak” into other 534 data samples. 

## 535 _Temporal filtering_ 

536 This is a per-channel filtering operation which defaults 537 to a high-pass filter at 300Hz. Bandpass filtering is 538 typically done using IIR filters for example with Butter539 worth coefficients. Butterworth filters have some de540 sirable properties in the frequency space, but their im541 plementation on the GPU is slow. To accelerate it, we 542 switch to using an FIR filter that simulates the Butter543 worth filter and we perform the FIR operation in FFT 544 space taking advantage of the convolution theorem. 545 To get the impulse response of a Butterworth filter, we 546 simply filter a vector of size _NT_ with all zeros and a 547 single 1 value at position floor( _NT /_ 2) (0-indexed). 

## _Channel whitening_ 

## 548 

549 While temporal filtering reduces time-lagged corre550 lations coming from background electrical activity, it 551 does not reduce across-channel correlations. To re552 duce the impact of local sources, such as spikes from 553 100-1000µ _m_ away from the probe, we perform chan554 nel whitening in local neighborhoods of channels. A 555 separate whitening vector is estimated for each chan556 nel based on its nearest 32 channels using the so557 called ZCA transform, which stands for Zero Phase 558 Component Analysis [36]. ZCA is the data whitening 559 transformation which is closest in Euclidean norm to 560 the original data. For an _N_ by _T_ matrix _A_ , the ZCA 561 transform matrix _W_ is found by inverting the covari562 ance matrix, using epsilon-smoothing of the singular 563 values: 

**==> picture [112 x 49] intentionally omitted <==**

564 The local whitening matrix _W_ is calculated sepa565 rately for each channel and its neighborhood of 32 566 channels, and only the whitening vector correspond567 ing to that channel is kept and embedded into a full568 size _Nchan_ by _Nchan_ matrix. This is preferable to di569 rectly calculating a grand _Nchan_ by _Nchan_ whitening ma570 trix because it reduces the number of whitening coef571 ficients to 32 _· Nchan_ instead of _Nchan · Nchan_ which pre572 vents overfitting in the limit of a large _Nchan_ . 

## _Drift correction_ 

- 573 

574 Drift correction is a complex preprocessing step which 575 was described in detail in [9]. Here we only described 576 a few small modifications in Kilosort4. The drift correc577 tion process can be separated into drift estimation and 578 data alignment. In Kilosort4, drift estimation is per579 formed in advance, while data alignment is performed 580 on-demand along with the other preprocessing opera581 tions. Drift estimation includes a step of spike detec582 tion, which uses a set of predefined, “universal” tem583 plates to detect multi-channel spikes. In Kilosort 2.5 584 and 3, these predefined templates were constrained 585 to be negative-going spikes, while in Kilosort4 we con586 sider both positive and negative going spikes using 587 pairs of inverted templates (for fast computation). An588 other modification in Kilosort4 is the use of linear inter589 polation for sampling the drift traces at every channel, 590 in place of the “Makima” method used in previous ver591 sions. 

592 Since data alignment is a linear operation performed 593 with a Gaussian kriging kernel, it can be combined with 594 channel whitening which is also a linear operation. In 595 practical terms, the two _Nchan_ by _Nchan_ matrix multipli596 cations are combined into one, thus further accelerat597 ing the computation. 

## 598 **Template deconvolution** 

599 Template deconvolution is the process of using a set 600 of waveform templates matched to the data in order 601 to detect spikes and extract their features, even when 602 they overlap other spikes on the same channels and at 603 the same timepoints. Template deconvolution can be 604 seen as replacing the spike detection step in a classi605 cal spike sorting pipeline. The goal in Kilosort4 is to 606 extract all the spikes above a certain waveform norm, 607 and calculate their spike features in a way that discards 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

623 3) The features extracted for each spike can be de624 contaminated from other overlapping spikes, due to 625 the use of a generative or reconstructive model. As 626 described below, these features are robust to imper627 fectly chosen templates. 

608 the contribution of nearby overlapping spikes. Tem609 plate deconvolution improves on classical spike detec610 tion in several ways: 

611 1) The detection of the spikes is performed by tem612 plate matching, which is a more effective way of detect613 ing spikes compared to threshold crossings, because it 614 uses templates that represent the multi-channel spikes 615 of the neurons being matched. 

616 2) Spikes that overlap in time and channels can 617 be detected and extracted as separate events due to 618 the use of iterative matching pursuit. Classical meth619 ods require an ”interdiction” area in time and channels 620 around each detected spike where a second spike de621 tection is disallowed, in order to prevent double detec622 tions of the same spike. 

## _Template learning_ 

628 

629 To perform template deconvolution, a set of templates 630 must be learned that can match all the detectable 631 spikes on the probe. In previous Kilosort versions (1 / 2 632 / 2.5), special care was taken to ensure that these tem633 plates match neural waveforms on a one-to-one basis. 634 This was necessary because relatively few additional 635 merges and splits were performed after template de636 convolution. In Kilosort 3 and 4, the templates do not 637 need to match single neurons because the features ex638 tracted by template deconvolution are clustered again 639 using more refined clustering algorithms. However, it 640 is important that every spike in the raw data has _some_ 641 template to match to. 

642 To build a set of templates, we perform clustering 643 on a set of spikes identified by template matching with 644 a set of universal spike templates. This initial spike 645 detection step is equivalent to the spike detection per646 formed in Kilosort 2.5 for drift correction. The universal 647 templates are defined by all possible combinations of 648 1) a spatial position in 2D; 2) a single-channel wave649 form shape; 3) a spatial size. The spatial positions 650 need not be coincident with actual probe channels, 651 and we choose them to upsample the channel densi652 ties by a factor of 2 in each dimension. For a Neuropix653 els 1 probe, this corresponds to 1536 positions. The 654 single-channel waveform shapes are obtained by k- 655 means clustering of single channel spikes, either from 656 a pre-existing dataset (IBL dataset) or from spikes de657 tected by threshold crossings in the data, and we de658 fault to 6 such waveforms. Finally, the spatial sizes 659 (five by default) define the envelope of an isotropic 660 Gaussian centered on the spatial position of the tem- 

661 plate, which is used as per-channel amplitudes. In to662 tal, a set of 46,080 universal templates are used for 663 a Neuropixels 1 probe; for more details see [9]. The 664 spatial footprints are explicitly precomputed for all po665 sitions and all spatial sizes. The templates are effec666 tively normalized to unit norm by separately normaliz667 ing the per-channel waveform templates and the spa668 tial footprints. Since the universal templates are unit 669 norm, their variance explained at each timepoint can 670 be easily calculated as the dot product with the data, 671 squared: 

**==> picture [163 x 49] intentionally omitted <==**

672 where _W_ is the unit-norm universal template, _D_ is 673 the data over a particular set of channels and time674 points, and _x_ is the best matching amplitude that the 675 template needs to be multiplied by to match the data. 

676 The dot products between each of these templates 677 and the data at each timepoint can be performed effi678 ciently in the following order: 1) temporal convolution 679 of each data channel with each of the 6 single-channel 680 waveforms; 2) per timepoint matrix multiplication with 681 a set of weights corresponding to all positions and all 682 spatial sizes. Once the dot products are calculated 683 in this manner, the largest variance explained value is 684 kept at each spatial position of each template. For a 685 Neuropixels probe, this is a matrix of size 1536 by _NT_ 686 (batch size). The goal of this spike detection step is 687 to find localized peaks in this matrix, which must be 688 local maxima in a neighborhood of timepoints ( _±_ 20) 689 and spatial positions (100 nearest positions). The rela690 tively large neighborhood size ensures that no spike is 691 detected twice, but prevents many overlapping spikes 692 from being detected (typically about 50% of spikes go 693 undetected). However, the missing spikes are not a 694 concern for the purpose of template learning, since it 695 is extremely unlikely that all the spikes from a neuron 696 will be consistently missed by this procedure. 

697 Once the spikes are detected, we extract PC fea698 tures in the 10 nearest channels to each detection. We 699 use a set of six PCs which are found either from a pre700 existing dataset (IBL dataset) or from spikes detected 701 by threshold crossings. For each spike, an XY position 702 on the probe is computed based on the center-of-mass 703 across channels of the spike’s projection on the best704 matching single channel template (same as in Kilosort 705 2.5). We assign all spikes in 40 µm bins according to 706 their vertical position, and embed all spikes detected 707 in the same bin to the same set of channels (which is 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 708 usually more than 10 channels due to differences be709 tween spike positions). Finally, the embedded PC fea710 tures are clustered according to the same graph-based 711 clustering algorithm we describe below, using only the 712 merging criterion of the bimodal regression-axis and 713 not using the cross-correlation based criterion. In Kilo714 sort3, the same procedure is applied but the clustering 715 algorithm is recursive pursuit. After clustering each 40 716 µm section of the probe, the centroids are multiplied 717 back from PC space into spatio-temporal waveforms, 718 and pooled together across the probe. 719 Templates from the same neuron may be detected 720 multiple times, either on the same 40 µm section or 721 in nearby sections. This is not inherently a problem 722 because each neuron can have multiple templates. 723 However, it can become a problem if these multiple 724 templates are not aligned to each other, because then 725 spikes from the same neuron will be detected at differ726 ent temporal positions, which changes their PC feature 727 distribution. In addition, having many templates makes 728 the spike detection step memory and compute ineffi729 cient. A solution to both these problems is to merge 730 together templates which have a high correlation with 731 each other and similar means, where the correlation 732 is maximized across possible timelags. In addition, 733 we temporally align all templates based on their maxi734 mal correlation with the same six prototypical single735 channel waveforms describe above. Note that this 736 merging step may result in the opposite scenario of 737 having one template for multiple neurons. This is also 738 not a problem, because templates are only merged 739 when they have a high correlation, and thus the same 740 average template can successfully match the shape of 741 multiple neurons. 

## 742 _Spike detection with learned templates and matching_ 743 _pursuit_ 

- 744 Once a set of templates is learned, they can be used 745 for template matching similar to the universal tem746 plates described above. The main difference is that 747 instead of allowing for an arbitrary scaling factor _x_ , we 748 require that matches use the average amplitude of the 749 template it was found with. The variance explained of 750 learned template _W_ of some data _D_ thus becomes: 

**==> picture [163 x 31] intentionally omitted <==**

751 Like before, this quantity only requires the calcula752 tion of _W[T] D_ , which can be done convolutionally for 753 each template. In practice, we represent templates us- 

754 ing a three-rank approximation, factorized over chan755 nels and time, which speeds up the convolutions dra756 matically [6]. We first multiply the data with the chan757 nel weights for each rank, and convolve the result758 ing traces with the temporal components. The three759 rank approximation captures nearly the entire wave760 form variance in all cases ([6]), and also helps to de761 noise templates calculated from relatively few spikes. 762 To extract overlapping spikes, we must detect spikes 763 iteratively over the same portion of data, and subtract 764 off from the data those parts attributed to spike de765 tections. This subtraction allows for another pass of 766 detections to be performed, which can detect other 767 spikes left over and yet un-subtracted. This proce768 dure is called matching pursuit ([37]) and is fundamen769 tally a sequential process: to detect another spike, one 770 must first subtract off the contributions of spikes de771 tected before. However, we can parallelize this step 772 thus making it suitable for GPU processing by observ773 ing that the subtraction of a single spike results in 774 highly-localized changes to the data, which cannot af775 fect the calculated amplitudes far from the position of 776 that subtracted spike. Thus, we can detect and sub777 tract multiple spikes in one round as long as they are 778 far enough from each other. Upon calculating a ma779 trix of variance explained for each template at each 780 timepoint, we detect peaks in this matrix which are lo781 cal maxima over local neighborhoods in time _±nt_ time 782 samples, and across all channels. After detection, the 783 optimal amplitude for each spike is calculated and its 784 contribution from the data is subtracted off. To avoid 785 recalculating the dot products of templates at all time786 points, the contribution of the subtracted spikes to the 787 dot-products is directly updated locally using a set of 788 precomputed dot-products between templates, at all 789 possible timelags. This detection and subtraction pro790 cess is repeated for 50 rounds, with later rounds being 791 much faster due to the increasingly smaller number of 792 spikes left to extract. 

- 793 _Extracting PC features with background subtraction_ 

794 The final step in template deconvolution is to extract 795 features from the data to be used by the clustering al796 gorithm. One possibility would be to directly extract PC 797 features from the preprocessed data, at the spike de798 tection times (Figure 1h), however this results in con799 tamination with background spikes. A better option 800 is to first subtract the effect of other spikes, since we 801 know from the matching pursuit step how much these 802 other spikes contribute (Figure 1e). To do this compu803 tation efficiently, we first extract PC features from the 804 residual (Figure 1f), and then add back to these fea805 tures the contribution of the template which was used 806 to extract the spike. The contribution of each template 

11 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## 807 in PC space is precomputed for faster processing. 

## **Graph-based clustering** 

## 808 

809 The new clustering algorithm in Kilosort4 uses graph810 based algorithms. This class of algorithms relies en811 tirely on the graph constructed by finding the nearest 812 neighbors to each data point. There are several steps: 

813 1) Neighbor finding with subsampling 

814 2) Iterative neighbor reassignment 

- 815 3) Hierarchical linkage tree 

- 816 _Neighbor finding with subsampling_ 

817 Many frameworks for fast neighbor finding exist and we 818 tested a lot of them for spike sorting data. In the end, 819 the brute force implementation from the faiss frame820 work [38] outperformed other approaches in speed on 821 modern multi-core computers for the range of data 822 points we need to search over (10,000-100,000) and 823 the number of data points we need to find neighbors 824 for (100,000-1,000,000). 

## _Iterative neighbor assignment_ 

825 

826 Clustering algorithms based on graphs typically opti827 mize a cost function such as the modularity cost func828 tion. We review this approach first, before describing 829 our new approach. Following [17], the modularity cost 830 function is defined by 

**==> picture [112 x 28] intentionally omitted <==**

831 where _m_ is the total number of edges in the graph, _ec_ 832 is the number of edges in community _c_ , _Kc_ is the sum 833 of degrees in community _c_ and γ is a “resolution” pa- _c_ 834 rameter that controls the number of clusters. The _[K]_[2] 2 _m_ 835 can be interpreted as the expected number of edges 836 in community _c_ from a null model with the same node 837 degrees as the data but otherwise random graph con838 nections. 

839 Specialized optimization algorithms exist to maxi840 mize the modularity cost function by moving nodes be841 tween communities and performing merges when the 842 node re-assignment converges [18]. Additionally, split843 ting steps and other optimizations were recently intro844 duced which improve the results of the algorithm and 845 its speed [17]. These algorithms are effective for many 846 types of data, yet have a substantial failure mode for 847 spike sorting data: they have difficulty clustering data 848 with very different number of points per cluster. In 849 practice, for our clustering problems, there are often 850 very large clusters of up to 100,000 points together 851 with clusters with many fewer ( _<_ 1,000) points. A low 852 resolution parameter γ can keep the large cluster in 

- 853 one piece, but also merges the small clusters into 854 larger clusters. Conversely, high resolution parame855 ters may return the small clusters as individual clus856 ters, but can split the large cluster into very many (hun857 dreds) of pieces. The oversplitting is not inherently a 858 bad property, since we will perform merges on these 859 clusters anyway, but the very large number of pieces 860 returned for the large clusters means that very many 861 correct merging decisions must be made, which is in 862 itself a very difficult optimization problem. In addition, 863 running the Louvain/Leiden algorithms with large reso864 lution parameters may somewhat reduce the effective- _c_ 

- 865 ness of the algorithm since the community penalty γ 2 _[K] m_[2] 866 only has a null model interpretation for λ = 1. 

- 866 

867 To improve on these algorithms, we started from 868 the observation that local minima of the neighbor 869 re-assignment step have some desirable properties. 870 These local minima arise because the neighbor re871 assignment step monotonically improves the modular872 ity cost function by greedily moving nodes to new clus873 ters if that improves the modularity score. This step 874 converges after a while, because no more clusters can 875 be moved. This is however a local minimum of the 876 optimization, and the modularity can often be further 877 increased by making merges between clusters. Un878 like the node re-assignment, which consists of small 879 local moves, the merging between clusters is a global 880 move in the cost function and can thus escape the lo881 cal minimum. Algorithms like Leiden/Louvain take ad882 vantage of such global merges by applying the node 883 re-assignment step again on a new graph made by 884 aggregating all the points into their clusters when the 885 local minimum is reached. 

886 Our observation was that the local minima them887 selves can consist of good clustering, if the neighbor 888 re-assignment step is initialized appropriately. Our ini889 tialization uses the K-means++ algorithm to partition 890 the data initially into 200 clusters [14]. The node re891 assignment algorithm for the modularity cost function 892 with γ = 1 is run for a fixed number of iterations (typi893 cally sufficient for convergence). The converged parti894 tioning of the data is then used as a clustering result. 895 Especially relevant to the next step, the algorithm al896 most never made incorrect merges, and instead output 897 some clusters oversplit. This bias towards oversplit898 ting is important, because it allows us to correct the 899 mistakes of the algorithm by making correct merge de900 cisions, which is much easier than finding the correct 901 split in a cluster. 

902 We also found that clusters which were oversplit 903 generally had a reason to be oversplit: the separate 904 pieces identified by the algorithm were in fact suffi905 ciently different to create a local minimum in the clus- 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

906 ter assignments. This is a common problem in spike 907 sorting data, where nonlinear changes in the waveform 908 can result in clusters that appear bimodal in Euclidian 909 space. An extreme example of this effect is due to 910 abrupt drifts of the probe changing the sampling of the 911 waveforms by a non-integer multiple of the probe pe912 riod. Even after drift correction, waveforms sampled 913 at the two different positions will be much more similar 914 to other waveforms from the same position, than they 915 are to waveforms sampled at the other position (Fig916 ure S2b). As a consequence, many algorithms return 917 such units oversplit into two halves, as can be clearly 918 seen in the benchmark results for the step drift condi919 tion, where many units are identified with exactly a 0.5 920 score, which corresponds to 50% of the spikes identi921 fied. 

## 922 _Hierarchical merging tree_ 

923 To perform merges, we could take two strategies: 1) 924 a brute-force approach in which we check all pairs 925 of clusters for merges, or at least the ones with high 926 waveform correlation; 2) a directed approach where 927 we use the structure of the data to tell us which merges 928 to check. We use both, starting with the second one 929 to reduce the number of clusters and thus reduce the 930 number of brute-force checks we need to make later. 

931 For the directed approach, we construct a hierarchi932 cal merging tree based on the modularity cost function. 933 The leaves of this tree consist of the clusters identi934 fied at the previous step. For each pair of clusters 935 _i, j_ , we aggregate the neighbors and node degrees, 936 similar to the Leiden/Louvain algorithms, thus result937 ing in a full matrix _K_ of size _nk_ by _nk_ where _nk_ is the 938 number of clusters, and where _Kij_ is the number of 939 edges between clusters _i, j_ , while _Kii_ is the number 940 of internal edges. Additionally, a variable _ki_ holds the 941 aggregated degree of each cluster _i_ . The linkage tree 942 is constructed by varying the resolution parameter γ 943 in the modularity cost function from ∞ down to 0. As 944 γ decreases, merges of two clusters start to increase 945 the modularity cost function. Specifically, a pair of clus946 ters gets merged when the modularity _H_ 2 after merg947 ing equals the modularity _H_ 1 before merging, where: 

**==> picture [243 x 95] intentionally omitted <==**

**==> picture [124 x 53] intentionally omitted <==**

949 In other words, a pair of clusters _i, j_ should be 950 merged when γ reaches a value of 2 _mKij/_ ( _kik j_ ). After 951 merging, the matrix _K_ and vector _k_ can be recomputed 952 with the two clusters _i, j_ becoming aggregated into 953 one. Note that a merging decision does not change 954 the γˆ for other pairs of clusters, and it cannot result in ˆ ˆ 955 a higher γ than the current γ _ij_ . This can be shown by 956 reductio ad absurdum: if the merged _i, j_ cluster had a 957 higher γˆ with another cluster _l_ , it would imply that one 958 of the original clusters _i_ or _j_ had a higher ˆγ _il_ or ˆγ _jl_ , and 959 thus it should have been merged a priori. The monoˆ 960 tonic property of γ _ij_ ensures that a well-defined merg961 ing tree exists, with a strictly decreasing sequence of ˆγ 962 for increasingly higher merges in the tree. Empirically, 963 we have found that the resulting merging tree is very 964 useful for making merge/split decisions. 

965 **Split/merge criteria** 

966 With the tree constructed, we next move down the tree 967 starting from the top and make individual merge/split 968 decisions at every node. If a node is not being split, 969 then the splits below that node are no longer checked. 970 We use two splitting criteria: 1) the bimodality of the 971 data projection along the regression axis between the 972 two clusters and 2) the degree of refractoriness of the 973 cross-correlogram. If the pair of units has a refractory 974 cross-correlogram, then the split is always performed. 975 If the cross-correlogram is not refractory, then the split 976 is performed if and only if the projection along the re977 gression axis is bimodal. 

978 _Bimodality of regression axis_ 

979 Consider a set of spike features **x** _k_ with associated la980 bels _yk ∈{−_ 1 _,_ 1 _}_ , where _−_ 1 indicates the first cluster 981 and 1 indicates the second cluster. A regression axis ˆ 982 **u** can be obtained by minimizing: 

**==> picture [125 x 25] intentionally omitted <==**

983 This regression problem becomes highly unbal984 anced when one of the clusters has many more points 985 than the other. We therefore add a set of weights 986 _w−_ 1 = _n_ 2 _/_ ( _n_ 1 + _n_ 2) _, w_ +1 = _n_ 1 _/_ ( _n_ 1 + _n_ 2), where _n_ 1, 987 _n_ 2 are the number of spikes in the first and second 988 cluster. 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [140 x 25] intentionally omitted <==**

989 This weighted regression problem can be solved in ˆ 990 the usual fashion. Finally, we use the **u** axis to esti991 mate how well separated the clusters are by projecting ˆ 992 _xproj_ = **u** _[T]_ **x** _k_ . The projections are binned in 400 bins 993 linearly-spaced between -2 and 2, and the histogram 994 is gaussian smoothed with a standard deviation of 4 995 bins. To score the degree of bimodality, we find three 996 important values in the histogram: the peak of the neg997 ative portion, the trough around 0, and the peak of the 998 positive portion. First we find the trough _xmin_ at posi999 tion _imin_ in the bin range of 175 to 225. Then we find 1000 the peaks _x_ 1, _x_ 2 in the bin ranges from 0 to _imin_ and 1001 from _imin_ to 400. The bimodality score is defined by 

1001 

**==> picture [154 x 11] intentionally omitted <==**

1002 In other words, we compare the density of the _xproj_ 1003 distribution at its trough to the peak densities for both 1004 clusters. If the density at the trough is similar in value 1005 to the density of either the left or right peak, that indi1006 cates a non-bimodal distribution. 

## _Refractory auto- and cross-correlograms_ 

1007 

1008 There are many cases where the regression axis has 1009 a bimodal distribution, yet the clusters are part of the 1010 same neuron. This is due to the non-stationarity of 1011 the waveforms from the same neuron, either due to 1012 drift or due to other factors. In such cases, we need 1013 to use extra information such as the statistics of the 1014 spike trains. Fortunately, all neurons have a refractory 1015 period, which is a short duration (1-5ms) after they fire 1016 an action potential when they cannot fire again. The 1017 refractory period is heavily used by human curators to 1018 decide whether: 1) a cluster is well isolated and not 1019 contaminated with spikes from other neurons; 2) a pair 1020 of clusters are distinct neurons or pieces of the same 1021 neuron. These two decisions can be made based on 1022 the auto- and cross- correlograms (ACG and CCG) re1023 spectively: 

**==> picture [104 x 53] intentionally omitted <==**

1024 where _sk, r j_ represent the spikes times of the two 1025 neurons. In practice, we bin the auto- and cross1026 correlograms in 1ms bins from δ _t_ = _−_ 0 _._ 5 sec to δ _t_ = 

1027 0 _._ 5 sec. We consider the central bins of the cross1028 correlograms, and calculate how likely it is to see 1029 a very small number of coincidences in that bin, if 1030 the two clusters are from neurons firing independently 1031 from each other. We define _nk_ as the number of coin1032 cidences in the central _−k_ to + _k_ bin range, _R_ as the 1033 baseline rate of coincidences calculated from the other 1034 bins of the cross-correlogram. Cross-correlograms 1035 may be assymetric, and to account for that we esti1036 mate _R_ as the maximum rate from either the left or 1037 right shoulder of the cross-correlogram. We use two 1038 criteria to determine refractoriness. The first criterion 1039 is simply based on the ratio of refractory coincidences 1040 versus coincidences in other bins which works well in 1041 most cases, except when one of the units has very few 1042 spikes, in which case very few refractory coicindences 1043 may be observed just by chance. For the first criterion, 1044 we use the ratio _R_ 12 of _nk_ to its expected value from a 1045 rate _R_ , where _R_ 12 takes the minimum value of this ratio 1046 across _k_ . We set a threshold of 0.25 on _R_ 12 to consider 1047 a CCG refractory, and 0 _._ 1 to consider an ACG refrac1048 tory. For the second criterion, we use the probability 1049 _pk_ that _nk_ spikes or less would be observed from a 1050 Poisson process with rate λ _k_ = (2 _k_ + 1) _R_ , which we 1051 approximate using a Gaussian with the same mean 1052 and standard deviation as the Poisson process as 

**==> picture [137 x 27] intentionally omitted <==**

1053 where ε = 10 _[−]_[10] is a small constant to prevent tak1054 ing the square root of 0. If _Q_ 12 = min( _pk_ ) is large, it im1055 plies that the number of refractory spikes have a high 1056 chance of being observed from a Poisson distribution 1057 with the baseline rate, and thus the CCG is not refrac1058 tory. We set a threshold on _Q_ 12 of 0.05 to consider a 1059 CCG refractory, and 0 _._ 2 to consider an ACG refractory. 1060 Both criteria have to be satisfied for a CCG to be re1061 fractory: _R_ 12 _<_ 0 _._ 25 and _Q_ 12 _<_ 0 _._ 05 for the CCG and 1062 _R_ 12 _<_ 0 _._ 1 and _Q_ 12 _<_ 0 _._ 2 for the CCG. The different 1063 thresholds for ACG and CCG has to do with the func1064 tion of these decisions: for the ACG, we want small 1065 contamination rates _R_ 12 because it indicates a well1066 isolated neuron, while for the CCG we want to prevent 1067 clusters from being split if their contamination rate _R_ 12 1068 is indicative of a relation between these two clusters. 1069 Similarly for _Q_ 12. 

1070 _Global merges_ 

Global merges are performed after all sections of the probe have been clustered. As a similarity metric, we use the maximum correlation of pairs of waveforms over all timelags. To test for merges, we sort all units 

1071 

1072 

1073 

1074 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1075 by their number of spikes, and start testing in order 1076 from the units with the most spikes. For each unit, we 1077 find all other units with a similarity above 0 _._ 5 and start 1078 testing for merges starting from high to low similarity. A 1079 merge is performed if the cross-correlogram is refrac1080 tory. After a merge is performed, the merged unit is re1081 tested again versus all other units with similarity above 1082 0.5 with it. After no more merges can be performed, 1083 a unit is considered “complete”, and is removed from 1084 potential merges with subsequent tested units. 

1128 nodes, as opposed to the ”left” nodes which consist of 1129 all datapoints. Note that this is purely a mathematical 1130 construction, in which we duplicated the subsampled 1131 nodes so they exist both among the left and the right 1132 nodes. The reason for making the graph bipartite is 1133 to allow the cluster identities for left nodes to be op1134 timized independently, given the identities of the right 1135 nodes, and viceversa. However, making the graph bi1136 partite is not sufficient, we must also modify the mod1137 ularity cost function from: 

## 1085 **Scaling up the graph-based clustering** 

1086 Graph-based clustering algorithms do not scale well 1087 with the number of data points, and we had to de1088 velop new formulations and optimization strategies. 1089 The poor scalability is due to several problems: 1) find1090 ing the neighbors of all points scales quadratically with 1091 the number of points; 2) the _K_ nearest neighbors in 1092 a small dataset are relatively further away from the 1093 _K_ nearest neighbors in a larger dataset; 3) existing 1094 optimization algorithms like Leiden/Louvain are inher1095 ently sequential and thus hard or impossible to paral1096 lelize on GPUs. The first problem could be reduced 1097 by using some of the neighbor finding algorithms that 1098 have sublinear time for finding neighbors [27]. How1099 ever, for the particular type of data we consider, we 1100 find these algorithms to be slower, not faster than the 1101 brute force approach, at least when a multi-core CPU 1102 is used. The second problem is an issue because the 1103 effective neighborhood size around a point influences 1104 its clustering properties. If the neighborhood sizes are 1105 very small, clusters may split up into multiple pieces 1106 more easily. If it is too large, it may include points from 1107 other clusters. As a recording grows in duration, the 1108 number of spikes grows linearly with it. Thus, some 1109 normalization step must be introduced to ensure that 1110 neighborhood sizes are comparable for short and long 1111 recordings. To solve the third problem, a redesign of 1112 the cost function is necessary, so as to make multiple 1113 optimization steps in parallel. 1114 Our approach for improving scalability relies on a 1115 subsampled data approach, where we only search 1116 for neighbors in a smaller subset of all points. In 1117 other words, instead of constructing an _N_ by _N_ ad1118 jacency matrix, where _N_ is the number of points, we 1119 construct an _N_ by _nsub_ adjacency matrix, where _nsub_ 1120 is a fixed number of spikes independent of recording 1121 length, which is determined by the size of the sec1122 tion of the probe being clustered (40 µm typically, for 1123 which we use _nsub_ = 25,000). This solves the first 1124 two problems, but not the third. To solve the third 1125 problem, we treat the adjacency graph as a bipartite 1126 graph, by designating the subsampled datapoints as 1127 a different set of nodes, which we will call the ”right” 

**==> picture [170 x 116] intentionally omitted <==**

into: 

1138 

1139 where _Kc[left]_ is the sum of degrees of left nodes in the 1140 cluster _c_ , _Kc[right]_ is the sum of degrees of right nodes, 1141 and _ec_ are the number of edges between left and right 1142 nodes. If the cluster identities for all right nodes are 1143 fixed, a short calculation shows that every left node _t_ 1144 can be assigned independently to a cluster σ _t_ to max1145 imize their contribution to the modularity cost function: 

**==> picture [142 x 33] intentionally omitted <==**

1146 where _ntc_ are the number of right node neighbors of 1147 left node _t_ in cluster _c_ , and _kt_ is the degree of node 1148 _t_ like before. Similarly, every right node can be as1149 signed independently given fixed assignments for all 1150 left nodes. Thus, we can iterate between assigning 1151 cluster identities to all right nodes given all the left 1152 nodes, followed by assigning all the left nodes given 1153 all the right nodes. Note that a left node which repre1154 sents the same point as a right node may in fact be 1155 assigned to a different cluster than its corresponding 1156 right node. This new iterative optimization has massive 1157 parallelism, and thus is suitable for GPU acceleration. 

This optimization is initialized with 200 clusters identified by K-means++, which we implemented in pytorch for GPU-based scalability [14]. 

1158 1159 

1160 

15 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## **Algorithms for Kilosort 2/2.5/3** 

## 1161 

1162 The previous section completes the description of Kilo1163 sort4. In the next sections, we decribe algorithms from 1164 previous versions of Kilosort which have not been pre1165 viously described. These are divided into drift tracking 1166 (Kilosort2), global optimization (Kilosort2/2.5) and re1167 cursive pursuit (Kilosort3). 

## 1168 **Drift tracking (Kilosort 2)** 

1169 Drift tracking was an alternative strategy of accounting 1170 for drift. Unlike the drift correction algorithms from Kilo1171 sort2.5 and onwards, drift tracking does not require a 1172 geometrical model of the recording channels and thus 1173 it can be used for recordings with tetrodes, single elec1174 trodes etc. Drift tracking works well when drift changes 1175 are continuous, or at least the drift positions overall 1176 span a continuous range. Drift tracking does not work 1177 well when the recording consists mainly of two drift po1178 sitions, with little sampling of the positions in-between 1179 (see step drift benchmarks in Figure 3). Drift tracking 1180 requires two algorithmic steps, described below: on1181 line template learning and fast drift tracking. 

## _Online template learning and tracking_ 

## 1182 

1183 In the simplest case, imagine that the drift of the probe 1184 is very slow. A possible spike sorting strategy in that 1185 case could be to start by spike sorting a subsection 1186 of the data, say 5 minutes, over which the probe is at 1187 an almost fixed position, since drift is slow. With the 1188 templates learned from 5 minutes of data, one could 1189 then use the templates to extract and assign spikes on 1190 the next 5 minutes of data, and update the templates 1191 based on the spikes that were found. If the drift is slow, 1192 the distribution of waveforms from single templates will 1193 have only shifted slightly, so that spike assignments to 1194 clusters are still correct. The update of the templates 1195 would then track the mean of the shifted distribution 1196 for each cluster. This is, in a broad sense, the drift 1197 tracking strategy from Kilosort2, and it was a natural 1198 extension of the online template learning of Kilosort1. 1199 In the rest of this section, we describe the exact math1200 ematical form of online template learning. 

1201 The generative model of Kilosort is given by the re1202 construction cost function: 

**==> picture [78 x 12] intentionally omitted <==**

**==> picture [186 x 36] intentionally omitted <==**

1203 where _V_ ( _c,t_ ) is the recorded voltage at channel _c_ 1204 and timepoint _t_ , σ( _k_ ) is the template index for spike _k_ 1205 at time _s_ ( _k_ ), _Wi_ is the multi-channel template for cluster 

1206 _i_ and _x_ ( _k_ ) is the amplitude of spike _k_ . For mathemat1207 ical simplicity, we assume “infinite” temporal windows 1208 for each template _Wi_ and we also assume that they 1209 span all channels of the probe, but in practice we re1210 strict each template to a width of _nt_ = 61 samples and 1211 to a small number of channels (typically 32). Learning 1212 and inference in this model proceeds via the standard 1213 “EM-style” algorithm. For inference, we assume the 1214 templates _W_ are fixed, and we simultaneously infer 1215 _s_ ( _k_ ) _,_ σ( _k_ ) _, x_ ( _k_ ) for all _k_ via the parallelized matching 1216 pursuit algorithm described above. Learning proceeds 1217 iteratively by inferring **s** _,_ σ _,_ **x** from a single batch with 1218 the current _W_ , and computing an improved _W_ for this 1219 batch: 

**==> picture [165 x 53] intentionally omitted <==**

1220 where we omit the dependence on amplitudes _x_ ( _k_ ) 1221 for robustness, since outlier artifacts may have very 1222 large _xk_ that could dominate the templates. To con1223 vert this EM-style algorithm into an online algorithm, 1224 we perform the inference at a single batch level ( _≈_ 2 1225 sec), and update the templates with an exponential fil1226 ter which depends on the number of spikes inferred for 1227 each template: 

**==> picture [141 x 31] intentionally omitted <==**

1228 where τ is typically set to 400 spikes. In other words, 1229 it takes approximately 400 new inferred spikes for _Wi_ 1230 to “forget” its previous value. For learning to be ef1231 fective, the batches from one recording are processed 1232 in pseudorandom order in Kilosort1. For tracking in 1233 Kilosort2, we fix the order of the batches. For ex1234 ample, if the batches were processed in consecutive 1235 order 1, 2, 3, etc, then online learning of the tem1236 plates would ensure tracking of the slow changes in 1237 templates over long timescales, similar to the simple 1238 scenario describe at the beginning of this section. In 1239 practice however, drift often contains fast components 1240 in addition to slow components. Since the τ scale is 1241 set to 400 spikes, fast drift cannot be tracked well with 1242 this approach. Reducing τ would improve tracking, at 1243 least for neurons with high firing rates, but many neu1244 rons fire at _∼_ 1Hz and/or in bursty sequeces. For such 1245 neurons, drift movements _<_ 1 min would be quite diffi1246 cult to track, since very few spike samples of the neu1247 rons are seen in that time. 

16 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

## _Tracking fast drift_ 

## 1248 

1249 To track fast drift, we make another modification to the 1250 online template learning algorithm. Instead of process1251 ing the batches in random order (like in Kilosort1), or in 1252 consecutive order (like for slow drift), we use a special 1253 re-ordering of the batches which puts similar batches 1254 next to each other. We define and estimate a drift dis1255 similarity metric between batches, based on the distri1256 butions of spike shapes in each batch. 

1257 To construct the drift similarity metric, the first step 1258 is to extract a set of templates **W** _[k]_ for each batch _k_ . 1259 These templates are obtained by first detecting spikes 1260 via threshold crossing of PC-projected data. The PC 1261 projection is performed by convolving the data with the 1262 top three PCs, squaring and adding together the pro1263 jections. Local maxima in this projection are found in a 1264 neighborhood of the nearest 17 channels and 61 time1265 points. The features are extracted at the local maxima 1266 via PC projection for a subset of neighboring channels. 1267 Scaled k-means clustering is then performed, which is 1268 initialized with a random subset of the spikes and im1269 plemented on the GPU for speed, since it needs to be 1270 performed once for each 2 sec batch. A fixed number 1271 of clusters is used, equal to half the total number of 1272 channels. The centroids of the clustering are used as 1273 templates. 

1274 Once the templates **W** _[k]_ are obtained for each batch, 1275 we calculate a dissimilarity matrix _Aij_ between each 1276 pair of batches, each with their own template sets _W[i]_ , 1277 _W[j]_ : 

**==> picture [112 x 23] intentionally omitted <==**

1278 In other words, _Aij_ is a metric which is small when 1279 every template _k_ in a set of templates _W[i]_ has a close 1280 match in another set of templates _W[j]_ . Pairs of batches 1281 _i, j_ from similar drift levels will therefore have a small 1282 dissimilarity, while batches taken at very drift levels will 1283 have high dissimilarity because the templates won’t be 1284 very well matched. 

1285 Once we compute the matrix **A** , all that is left 1286 is to find a permutation ρ of the batches in which 1287 small dissimilarity values _A_ ρ( _i_ )ρ( _j_ ) are near the diag1288 onal. The algorithm we use for this is a version of 1289 “rastermap”, a framework algorithm we have been 1290 developing for sorting high-dimensional data along a 1291 one-dimensional continuum. This particular version of 1292 rastermap matches the similarity matrix **A** to the matrix 1293 of distances in a one-dimensional space, where _xk_ is 1294 a scalar value assigned to each batch _k_ and optimized 

by the algorithm: 

1295 

**==> picture [121 x 60] intentionally omitted <==**

1296 where the _< · >_ operation signifies averaging. This 1297 cost function is initialized with _xk_ based on the largest 1298 left singular vectors of **A** and minimized by gradient 1299 descent. We preprocess **A** by z-scoring each row sep1300 arately and symmetrize it by adding its transpose to it. 1301 In the optimization we ignore the mean of _dij_ over all 1302 _i, j_ , to avoid having to fit a constant offset term. Once 1303 the gradient descent optimization converges, we ob1304 tain a sorting of the batches by ρ = argsort( **x** ), where 1305 the argsort operation returns the index order of a vec1306 tor. 

1307 This ordering ρ is used to perform online template 1308 learning and tracking. The template learning is per1309 formed by running the algorithm over one half of the 1310 data (typically the first half after reordering, from the 1311 middle of the ρ range to the first batch and then back 1312 to the middle of the range). During this stage, the 1313 templates are being learnt: new templates can be in1314 troduced from the residuals of the reconstruction pro1315 cess, templates which are not used above a baseline 1316 spike rate are discarded, and merges and splits are 1317 also performed. See the next section for this template 1318 learning step. Once the template set is learned, the 1319 tracking is performed from the middle of the ρ range 1320 to the first batch, and then from the middle of the ρ 1321 range to the last batch. During the tracking phase, no 1322 new templates can be created or destroyed with any 1323 of the operations performed in the template learning 1324 phase. However, the template waveform itself contin1325 ues to change in an online fashion as described above 1326 in the online template learning section. 

## 1327 **Global optimization algorithms for clustering** 1328 **(Kilosort 2 / 2.5)** 

1329 Drift tracking was not the only new algorithm intro1330 duced in Kilosort2. We also added algorithmic steps 1331 designed to perform global optimization moves, in or1332 der to escape local minima which are very common 1333 in clustering algorithms. These global optimization 1334 moves were of three types: initialization, splitting a 1335 cluster and merging two clusters. We describe these 1336 in separate sections below. Some global optimiza1337 tion moves were also performed in Kilosort1 (simple 1338 splits and merges), but they were not as important 1339 there because the automated results of Kilosort1 un1340 derwent manual curation in Phy, and thus an oversplit 1341 cluster distribution was preferred because merges are 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1342 much easier than splits. For Kilosort2 however, the 1343 automated results of the algorithm became sufficiently 1344 good to be used in an automated manner, and thus it 1345 was important to avoid oversplit or overmerged clus1346 ters. 

1395 merged together if they have a high correlation ( _>_ 0.9) 1396 and if their means are similar ( _<_ 4 ~~_√_~~ 10 difference). If 1397 a merge is performed. the template with the smaller 1398 firing rate is simply dropped out of the active set. 

1399 _Bimodality splits_ 

## 1347 _Template initialization from residual_ 

1348 Initialization is one of the most important steps in a 1349 clustering algorithm. A common initialization for k- 1350 means style algorithms is k-means++, which sequen1351 tially adds data points as cluster centroids if they are 1352 far enough away from centroids already chosen. We 1353 use a similar strategy in Kilosort2, with the added com1354 plication that spikes which are far from existing cen1355 troids would not even be detected by the online tem1356 plate matching step. In this case, such spikes must 1357 be detected in the residual of the model after recon1358 structing the data with the spikes found by template 1359 matching. 

1360 To perform these detections, we run a spike detec1361 tor on the residual and pick a subset of those spikes 1362 as new templates to be introduced in the optimiza1363 tion. The spike detector was designed primarily to 1364 be fast, and to ensure that large amplitude spikes 1365 are not missed. It uses six single-channel prototype 1366 waveforms _wk, k_ = 1 _,_ 2 _,...,_ 6. For each channel, we 1367 check the variance explained of all templates that ex1368 tend over the nearest _n_ channels with _n ≤_ 7 and have 1369 the same single-channel waveform on each channel, 1370 chosen from one of the six single-channel prototypes 1371 _wk_ . This is a much simplified version of the spike de1372 tector introduced in Kilosort2.5, but a very fast version 1373 nonetheless. Similar to the Kilosort2.5 spike detec1374 tor, this detector computes the maximum variance ex1375 plained at each channel and each timepoint, that can 1376 be obtained using one of the 42 template combina1377 tions described above. Using this maximum variance 1378 matrix, we find peaks that are maxima across chan1379 nels for each timepoint, and then we find the subset 1380 of those which are also maxima across time, and in a 1381 neighborhood of _±_ 4 channels in a single batch. The 1382 reason for taking the maxima across time is to ensure 1383 that no spike from the same neuron is detected twice, 1384 because these spike detections are introduced as new 1385 putative templates. 

1386 New templates are introduced on every batch. The 1387 raw data snippets at the detected spikes are first 1388 smoothed with three principal components before be1389 ing added to the set of active templates. The num1390 ber of spikes detected by each template is monitored 1391 using an exponential filter with a decay scale of _∼_ 20 1392 batches. Every five batches, templates are triaged and 1393 removed from the active set if their firing rate is be1394 low 0.02 spikes/s. During this step, templates are also 

1400 Merges are relatively easy to perform, for example by 1401 checking all pairs of correlated templates and comput1402 ing their cross-correlograms to find whether it is refrac1403 tory (as described above for Kilosort4). Splits however 1404 are much more difficult, because finding a good split of 1405 a cluster in high-dimensional space is in itself a com1406 binatorially difficult problem. In fact, the problem of 1407 finding good splits is not so different from the original 1408 problem of clustering the data, with the distinction that 1409 a split is a separation into only two, rather than many, 1410 clusters. Since we only need to divide the data into two 1411 clusters, we can take advantage of a common intuition 1412 that human operators have when performing splits: if a 1413 projection axis in the data exists which has a bimodal 1414 distribution, that is strong evidence that a split should 1415 be performed along that axis. This split can also be 1416 tested with respect to refractoriness of the CCG (like 1417 we check merges), and if the CCG is not refractory, 1418 then the split is typically performed. 1419 How could we find such splits automatically? Hu1420 man curators typically find the splits in a GUI like Phy, 1421 by investigating multiple scatter plots of pairs of prin1422 cipal components from a few neighboring channels. 1423 Clearly this can be improved on, since the optimal split 1424 should include information from all channels and all 1425 principal components. In Kilosort2, we designed an 1426 algorithm called bimodal pursuit to find projection axes 1427 that are highly bimodal. The “pursuit” part is a refer1428 ence to other pursuit-type algorithms like ICA (kurto1429 sis/skewness pursuit), and refers to the iterative nature 1430 of the algorithm which sequentially increases the bi1431 modality of a projection _w[T]_ **x** , where _w_ is the unit-norm 1432 projection vector, and **x** is the data to be split into two 1433 clusters. 

1434 Specifically, we find the projection _w_ which maxi1435 mizes the following log-likelihood function: 

**==> picture [226 x 90] intentionally omitted <==**

1436 where _xk_ are the features of the _k_ -th spike, _µ j,_ σ _j_ 1437 are the scalar mean and variances of one cluster _j_ 

18 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

of the two total, _p j_ is the prior probability of draw1464 compute a measure of the certainty in assigning _yk_ as: a spike from that cluster with _p_ 1 + + _p_ 2 = 1. 1.. This 1465 _q j_ = _< r jk >yk_ = _j_ . If _q j_ is very close to 1, it means function can be optimized via an EM-style algorithm 1466 all spikes in cluster _j_ are assigned with nearly maxfor mixtures of Gaussians, where we first infer the pos1467 imum confidence. If it is close to its lower boundary terior distribution over cluster assignments, and then 1468 of 0 _._ 5, it means there is almost no difference between optimize the free energy function with respect to 1469 the means and variances _µ j,_ σ _j_ of the two Gaussians _j,, µ j, j,,_ σ _j_ given _w_ and viceversa. The posterior dis1470 in the mixture. To perform a split, we require that tribution over cluster assignments is given by the “re1471 min( _q_ 1 _, q_ 2) _>_ 0 _._ 9. In addition, we require that the responsibilities” _rk jk j_ = Prob(( _ykk_ = _j||_ θ),),, where _ykk_ is the 1472 sulting clusters have templates that are sufficiently distrue hidden label of data point _k_ and θ θ is the set of all 1473 tinct (correlation _<_ 0.9 or norms _n_ 1 _, n_ 2 that are suffiparameters. 1474 ciently different: _∥n_ 1 _− n_ 2 _∥/_ ( _n_ 1 + _n_ 2) _>_ 0 _._ 1). We also 1475 require that the smallest cluster in the split should have 1476 at least 300 spikes, and that the cross-correlogram be- _rk j_ = _p jN_ ( _w[t] xk_ ; _µ j,_ σ _j_ ) _/p_ ( _xk_ ) 1477 tween resulting clusters is not refractory, using similar 1478 criteria to those described above for Kilosort4. and the free energy function takes the form 1479 Splits are performed by traversing the list of clus1480 ters in consecutive order across channels. Once a _F_ ( **r** _,_ θ) = ∑ _k_[∑] _j rk j_ log _N_ ( _w[t] xk_ ; _µ j,_ σ _j_ ) 14811482 splittentialistentialisis splits.found,found, Wewewe alsododo thischeckbycheckbyby appendingthethe subclustersthethe smallestforfor po1483 sub-cluster to the end of the list, and testing the large = ∑ _rk j_ log( _p j_ ) _−_[(] _[w][T][x]_ 2 _[k]_ σ _[ −]_[2] _[µ][j]_[)][2] _−_[1] 2[πσ][2] _j_ 14841485 clusternono moreforgoodsplitssplitsagain.areforgoodsplitssplitsagain.aregoodsplitssplitsagain.aresplitssplitsagain.aresplitsagain.areagain.areare Thisfound,processandfound,processandprocessandand thencontinuesthecontinuesthethe processuntiluntil _k, j_ � _j_ � 

1438 out of the two total, _p j_ is the prior probability of draw1439 ing a spike from that cluster with _p_ 1 + + _p_ 2 = 1. 1.. This 1440 function can be optimized via an EM-style algorithm 1441 for mixtures of Gaussians, where we first infer the pos1442 terior distribution over cluster assignments, and then 1443 we optimize the free energy function with respect to 1444 _p j,, µ j, j,,_ σ _j_ given _w_ and viceversa. The posterior dis1445 tribution over cluster assignments is given by the “re1446 sponsibilities” _rk jk j_ = Prob(( _ykk_ = _j||_ θ),),, where _ykk_ is the 1447 true hidden label of data point _k_ and θ θ is the set of all 1448 parameters. 

1449 

Splits are performed by traversing the list of clusters in consecutive order across channels. Once a splittentialistentialisis splits.found,found, Wewewe alsododo thischeckbycheckbyby appendingthethe subclustersthethe smallestforfor posub-cluster to the end of the list, and testing the large clusternono moreforgoodsplitssplitsagain.areforgoodsplitssplitsagain.aregoodsplitssplitsagain.aresplitssplitsagain.aresplitsagain.areagain.areare Thisfound,processandfound,processandprocessandand thencontinuesthecontinuesthethe processuntiluntil moves to the next cluster in the list. 

1486 

Merges are also performed at the end in all versions of Kilosort starting with Kilosort2, and they take the some form as the global merges described above in the Kilosort4 section. 

1450 Holding _w_ fixed, we can maximize with respect to 1451 _p j, µ j,_ σ _j_ : 

1487 1488 1489 1490 

**==> picture [374 x 84] intentionally omitted <==**

In Kilosort3, we realized that the cost function above has some major weaknesses, such as the lack of scale invariance which means that projections with small amounts of variance have undesirably large values of log _L_ ( _w_ ). Nonetheless, in practice the maximization of log _L_ ( _w_ ) does indeed find projections with substantial bimodality, which is perhaps a consequence of good initialization and local minima. In Kilosort3, we made some appropriate modifications to the cost function as well as to the initialization to further improve its performance. The improved bimodal pursuit algorithm was able to find surprisingly good splits, even when given a mixture of more than two clusters. We took advantage of its performance and designed a new clustering algorithm in Kilosort3 which performs clustering by recursively splitting off clusters from the main distribution using the bimodal pursuit algorithm. 

1452 Holding _p j, µ j,_ σ _j_ fixed for all _j_ , we can maximize 1453 with respect to _w_ : 

1497 1498 1499 

**==> picture [211 x 77] intentionally omitted <==**

1454 _w_ is re-normalized to unit norm on every iteration. 1455 The algorithm is initialized with _w_ being either the top 1456 principal component of **x** , or its normalized mean. In 1457 Kilosort 2 and 2.5, we run the algorithm twice, first ini1458 tialized with the top principal component, and then ini1459 tialized with the mean. The EM algorithm is run for 1460 50 iterations, but _w_ is only updated after iteration 10, 1461 and on odd iterations only, in order to make the opti1462 mization faster. We assign each spike _k_ to the clus1463 ter _yk_ with highest posterior probability _rykk_ . We also 

1507 1508 

## _Improved bimodal pursuit_ 

1509 

The idea of “projection pursuit” comes from the field of independent components analysis (ICA) and similar algorithms, and it was perhaps popularized the most by the fast ICA algorithm from Hyvarinnen and colleagues [39]. Like our cost function, projection pursuit maximizes some criterion computed over the distribu- 

1510 

1511 

1512 

1513 

1514 

1515 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1516 tion of projections _w[T] x_ . Unlike our function, this cri1517 terion is usually scale-invariant, such as the kurtosis 1518 or skewness criteria which are normalized by the vari1519 ance of the data. A simple way to make our criterion 1520 scale-invariant is whitening or “sphering”, which is also 1521 a very common preprocessing step for ICA. Whitening 1522 normalizes a multi-dimensional dataset **x** into **x** ˜ = _A_ **x** , 1523 where _A_ is an appropriate whitening matrix, so that the 1524 mean of each dimension is 0, and the covariance of 1525 the normalized data is the identity. As a consequence, 1526 any projection _w[T]_ **x** ˜ is standardized, in other words it 1527 has mean 0 and variance 1. A common choice of 1528 whitening is PCA / SVD, and this is also our approach. 1529 In Kilosort3, we perform whitening on every matrix 1530 **x** before running the bimodal pursuit algorithm. In this 1531 case, the log-likelihood criterion can be interpreted as 1532 searching for the projection _w_ which can be best mod1533 elled by a mixture of Gaussians after z-scoring. Of all 1534 distributions with mean 0 and variance 1, the criterion 1535 _L_ ( _w_ ) is now maximized by the sum of discrete distri1536 butions centered on _−_ 1 and +1. In addition, we con1537 strain σ1 = σ2 = σ, which allows to perform the matrix 1538 inversion _C[−]_[1] only once, because 

## _Recursive pursuit_ 

1560 

1561 The bimodal pursuit algorithm described above takes 1562 as input a set of spike features, and outputs a parti1563 tion into two clusters. Applied recursively, the algo1564 rithm can find a subset of a dataset that is well iso1565 lated from other clusters and cannot be split further 1566 into more clusters. We start will all spikes detected on 1567 a set of channels, and find the first split. Of the two 1568 pieces, we take the piece with higher average wave1569 form amplitude, and we split it again. This process 1570 continues until no more splits can be found. Splits can 1571 be veto-ed in similar ways to Kilosort 2/2.5, except that 1572 the index of bimodality is used instead of the “mea1573 sure of certainty” described above. A split requires 1574 all three criteria to be satisfied: high bimodality index, 1575 low waveform correlation and non-refractory CCG. In 1576 Kilosort4, we use the same criteria minus the criterion 1577 for low waveform correlation which is somewhat redun1578 dant with the bimodality index criterion. 

1579 Once a cluster is found out of the dataset, the 1580 spikes corresponding to that cluster are removed, and 1581 the cluster finding process is applied to the remain1582 ing spikes. This process continued until the remaining 1583 spikes can no longer be split, and thus they constitute 1584 the final cluster. Note that the complete algorithm con1585 tains two recursive loops: one loop for finding a single 1586 cluster out of the dataset, and another loop for finding 1587 all clusters in the dataset. This clustering operation is 1588 applied to spikes detected in 40 µm segments of the 1589 probe, similar to the process described for Kilosort4. 

**==> picture [189 x 87] intentionally omitted <==**

## **Benchmarking** 

1590 

1591 To determine the performance of various spike-sorting 1592 algorithms, we created realistic simulations using the 1593 properties of 512 electrophysiological recordings from 1594 the International Brain Laboratory (IBL) performed us1595 ing Neuropixels 1.0 probes [15, 40]. These recordings 1596 were processed by the IBL using pyKilosort. The sim1597 ulation generation was over two times faster than real1598 time (e.g. a 45 minute simulation took around 20 min1599 utes to generate), which enabled us to create several 1600 simulations for benchmarking. The simulations, other 1601 than “step drift, aligned”, used the site configuration 1602 of the Neuropixels 1.0 probes, which have a vertical 1603 spacing of 20 µm, a horizontal spacing of 32 µm and 1604 a horizontal offset across rows of 16 µm. 

1539 because ∑ _j rk j_ = 1 by construction and ∑ _k xkxk[T]_[due to] 1540 whitening, where _N_ is the total number of spikes. 1541 We also introduce a new form of initialization. Since 1542 the algorithm is highly sensitive to initialization, we run 1543 a brute force search for a good initialization vector _w_ . 1544 Remembering that we are in normalized PCA space, 1545 the brute force approach checks all vectors _w_ with 1546 _wd ∈{−_ 1 _/n,_ 1 _/n}_ for _d_ = 1 _,...,_ 6 and _wd_ = 0 _, d >_ 6, 1547 with _n_ being a normalization constant, in this case ~~_√_~~ 6. 1548 For each of the resulting 64 combinations, we check 1549 the bimodality of the projection _w[T]_ **x** by performing a 1550 histogram and using similar criteria to those described 1551 above for Kilosort4. This histogram based algorithm is 1552 also used in the first 25 iterations of bimodal pursuit as 1553 a replacement for the EM assignments for µ _,_ σ _, p_ . This 1554 is done by computing the mean, variance and fraction 1555 of all points _w[T] xk_ smaller/bigger than the trough of the 1556 distribution respectively. We found this initial approxi1557 mation of the EM assignments to be more robust, es1558 pecially in cases where one cluster has substantially 1559 more spikes than the other. 

## _Drift simulation_ 

1605 

pyKilosort, like other Kilosort versions, returns the estimated depth for each processing batch at nine equallyspaced positions along the 3.84 mm probe. The processing batch size for all IBL recordings was 65,536 timepoints. We quantified the drift range for each recording by first taking the median of the depth across 

1606 1607 

1608 

1609 

1610 1611 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1612 the nine positions, then computing difference between 1613 the 5[th] and 95[th] percentile of the drift. We used the 1614 properties of the drift across these recordings to cre1615 ate simulated drift (see drift examples in Figure S3). 1616 For the simulations, we generated a drift trace of 1617 length 45 minutes at each of the positions, then up1618 sampled the drift to all 384 channels using linear in1619 terpolation. The drift was the same across a period of 1620 2 seconds for all simulations, other than the fast drift 1621 simulation which varied in periods of 200 ms. Here are 1622 the details of the generation of each drift simulation: 

- 1623 • _no drift_ : Zero drift at all nine positions. 

1624 • _medium drift_ : The overall drift was generated as ran1625 dom gaussian noise smoothed in time with a gaus1626 sian filter of σ=100 sec. Drift at each of the nine 1627 positions was generated as random gaussian noise 1628 smoothed in time with a gaussian filter of standard 1629 deviation 100 seconds and smoothed across the po1630 sitions with a gaussian filter with σ=2. This per1631 position drift was rescaled by a factor of 0.4 and 1632 added to the overall drift, then the drift across posi1633 tions and time was rescaled such that the minimum 1634 and maximum values were -7 µm and 7 µm. This 1635 resulted in a simulation with a drift range of 9.4 µ. 

1636 • _high drift_ : The overall drift and per-position drift were 1637 generated in the same way as the medium drift. The 1638 per-position drift was next rescaled by a factor of 1639 0.26 and added to the overall drift, then the drift 1640 across positions and time was rescaled such that 1641 the minimum and maximum values were -18.5 µm 1642 and 18.5 µm. This resulted in a simulation with a 1643 drift range of 27.9 µm. 

1644 • _fast drift_ : A medium drift simulation was used for the 1645 slow drift across positions and time (generated in 1646 bins of two seconds, then upsampled to 200 ms bins 1647 with nearest neighbor interpolation). Then fast drift 1648 events were generated with an amplitude of 10 µm 1649 and a difference of exponentials kernel with a rise 1650 time of 80 ms and a decay time of 200 ms. 300 of 1651 these fast drift events were added to the upsampled 1652 medium drift simulation at random times. 1653 • _step drift_ : The overall drift and per-position drift were 1654 generated in the same way as the medium drift. The 1655 per-position drift was next rescaled by a factor of 1656 0.58 and added to the overall drift, then the drift 1657 across positions and time was rescaled such that 1658 the minimum and maximum values were -4 µm and 1659 4 µm. Halfway through the recording 30 µm was 1660 added to all the drifts across positions. 

1661 • _step drift, aligned_ : Same exact drift as step drift, 1662 but waveforms were upsampled using aligned probe 1663 sites with a vertical separation of 20µm and a hori1664 zontal separation of 32µm. 

## _Extraction of waveforms at multiple depths_ 

1665 

1666 Obtaining waveforms across many depths requires 1667 recordings with substantial drift. In the IBL dataset 1668 we found 11 such recordings with high drift that well1669 sampled a range of 40 µm in depth. We used the es1670 timated spike times from pyKilosort for each detected 1671 unit in these recordings, and the estimated depth of the 1672 probe to compute the average waveform for the unit at 1673 specified depth positions. We used 20 depth bins each 1674 of size 2µm, resulting in average waveforms across 40 1675 µm. To ensure the quality of the waveforms, we did not 1676 use any units which had fewer than 50 spikes at each 1677 depth. 1678 The waveforms were denoised by reconstructing 1679 each waveform across depths with only its top three 1680 principal components. The waveforms were then nor1681 malized by the average norm of the waveform across 1682 depths. We then threw out waveforms which varied 1683 substantially from -20 µm to 20 µm in depth, since 1684 these waveforms’ shape changes are likely caused by 1685 other processes besides drift. To quantify the varia1686 tion across depth we computed the Euclidean distance 1687 across channels and timepoints between the wave1688 form at -20µm and the waveform at 20µm shifted up 1689 by 4 channels (a distance of 40 µm). We removed 1690 units with variation greater than 0.25 ( _∼_ 25% of units), 1691 resulting in a waveform bank of 597 units from the 11 1692 recordings. 

Next we needed the waveform shapes at a finer scale than 2µm. For this, we upsampled the waveforms by a factor of 100 using kriging interpolation [9] with a regularization coefficient of 0.01 and a gaussian of standard deviation 20µm. For the step drift with aligned site simulation, the upsampled waveforms were interpolated using a probe with sites aligned vertically. Then the waveforms were again normalized by the average norm of the waveform across depths. We next divided these waveforms into two groups according to the contamination rates from their units’ estimated spike trains [41]: a contamination rate less than 0.1 were used to generate “single-units”, while those with a contamination rate greater than 0.1 were used to generate “multi-units”. 

1693 1694 1695 1696 1697 1698 1699 1700 1701 1702 1703 1704 1705 1706 

1707 

The units from these recordings exhibited waveform changes across depth, see example waveforms in Figure 3c and Figure S2a. All waveforms moved down the probe as the depth changes, but some waveforms also changed their shape (example units 2 and 4, which had smaller spatial footprints). This shape change could not be inferred by other channels. We demonstrated this by using the same Kriging interpolation procedure as above in order to estimate the 0 µm depth waveform from the waveforms at other depths (Figure S2b). The waveform at 0 µm depth was well- 

1708 

1709 1710 1711 1712 1713 1714 1715 

1716 1717 1718 

21 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1719 estimated for units 1 and 3 but not for 2 and 4. This 1720 exemplifies the need for real recordings to create ac1721 curate simulations of waveform shapes. 1722 We quantified the performance of the spike-sorting 1723 algorithms as a function of the spatial extent of the 1724 waveforms of the ground truth unit (Figure S5c,f). We 1725 defined the spatial extent of the waveform as the spa1726 tial scale across channels over which the waveform 1727 shape is maintained (using the 0 µm depth waveform). 1728 To compute this we first matched the waveform with 1729 its most similar waveform from the universal templates 1730 as defined by cosine similarity. We then projected 1731 the waveform onto this best template waveform and 1732 thresholded it, to obtain a template weight for each 1733 channel. We next computed the weighted mean of the 1734 distance from each channel to the center-of-mass of 1735 the waveform as defined by the template weights, and 1736 termed this the spatial extent. 

## 1737 _Simulation of spikes_ 

1738 We simulated 600 “single-units” and 600 “multi-units” 1739 by randomly drawing waveforms from these two 1740 classes. These waveforms were randomly placed on 1741 the probe at positions from site 4 to site 380. To cre1742 ate the correct waveform shapes, the waveform’s best 1743 channel modulo 4 was computed and maintained in 1744 the simulation (because the probe site arrangement 1745 repeats every 4 sites). 1746 We used the inter-spike intervals from detected units 1747 in the 11 recordings which had a contamination rate of 1748 less than 0.1, this was 1497 units in total. The av1749 erage firing rate of these units was 12.6 Hz. Each 1750 simulated spike train for a “single-unit” was then gen1751 erated by randomly shuffling the inter-spike intervals 1752 of one of the detected units. For the spike trains of 1753 “multi-units” we generated Poisson spike trains with fir1754 ing rates drawn randomly from these units’ firing rates. 1755 The amplitudes for the “single-units” were generated 1756 by adding a constant, 10, to a random exponential 1757 with a mean of 7, which approximated the distribution 1758 from units detected in the data. The amplitudes for 1759 the “multi-units” were generated from a uniform ran1760 dom distribution with a range from 4 to 10. The wave1761 form across depth for each unit was then multiplied by 1762 its amplitude. We quantified the performance of the 1763 spike-sorting algorithms as a function of the amplitude 1764 (norm) of the ground truth unit (Figure S5b,e). 1765 We then added one-by-one the spike train of each 1766 simulated unit to the simulation, using the simulated 1767 drift at each timepoint to determine which depth of the 1768 waveform to add for each spike. Collisions could occur 1769 in the spike trains, so we added the spike train in 3 in1770 terleaved parts to ensure correct reconstruction while 1771 still maintaining the speed of simulation generation. 

1772 All simulations used different waveforms, spike 1773 trains, and amplitudes, except for the two step drift 1774 simulations, in which all parameters were kept fixed to 1775 determine the effect of probe site configuration. These 1776 two step drift simulations therefore only differed in their 1777 exact waveform shapes across depths due to the dif1778 ference in the probe site positions. 

## _Simulation noise and “unwhitening”_ 

1779 

1780 To each channel in the simulation we added random 1781 noise with a flat frequency spectrum in time, up to 300 1782 Hz. This noise was scaled to have a standard devia1783 tion of 0.76. Next the simulation was “unwhitened”: the 1784 simulation was multiplied by the inverse of a whiten1785 ing matrix estimated from one of the 11 recordings 1786 used. Different whitening matrices were used for each 1787 simulation, except for the two step drift simulations, 1788 where it was the same matrix for both. Finally, to 1789 save the simulation as int16, the simulation was mul1790 tiplied by 200, cut-off at _±_ 32767 and converted to 1791 int16. For each simulation we saved a correspond1792 ing “.meta” file, which SpikeInterface expects for pro1793 cessing IMEC Neuopixels probe recordings. For the 1794 aligned site probe, we added a probe type to the spike 1795 GLX loader in SpikeInterface. 

1796 _Performance metrics_ 

1797 Each ground truth unit was compared to the 20 clos1798 est detected units from the algorithm, where close1799 ness was defined by the distance between the ground 1800 truth and detected units best channels. If an estimated 1801 spike from a detected unit was less than or equal to 0.1 1802 ms from a ground truth spike, it was counted as a pos1803 itive match. The false positive rate (FP) was defined 1804 as the number of estimated spikes without a positive 1805 match divided by the total number of estimated spikes, 1806 which is equivalent to 1 _− precision_ . The false nega1807 tive rate (FN) was defined as the number of missed 1808 ground truth spikes divided by the total number of 1809 ground truth spikes, which is equivalent to 1 _− recall_ . 1810 We matched the ground truth unit with the detected 1811 unit that maximized the _score_ , defined as 1 _−FP−FN_ 1812 [6]. The upper bound of the score is 1. In Figure 3e-j, 1813 the ground truth units were sorted by their score from 1814 each algorithm separately. We defined ground truth 1815 units as being correctly identified in Table 2 if the score 1816 was higher than 0.8. 

## _Spike-sorting algorithm parameters_ 

1817 

1818 We ran Kilosort 1, 2, 2.5 & 3, IronClust, Mountain1819 Sort4, SpyKING CIRCUS, SpyKING CIRCUS 2, HD1820 Sort, Herding Spikes, and Tridesclous2 on all sim1821 ulations using the SpikeInterface platform to ensure 1822 that all spike-sorting algorithms were run in the same 

22 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

1845 All other parameters were set to their default values. 

1846 

1823 way. For Kilosort 1, 2, 2.5 and 3, we set the detection 1824 thresholds to [9, 8] instead of their defaults which var1825 ied across verrsions. Also, to speed up Kilosort 1, we 1826 set the number of passes through the data to 2 instead 1827 of 6 (this did not reduce performance). 1828 For the other top performing algorithms (IronClust, 1829 MountainSort4, and SpyKING CIRCUS), we ran a pa1830 rameter sweep over the detection threshold and used 1831 the detection threshold which maximized the number 1832 of correctly identified units on the medium drift simu1833 lation. For MountainSort4 and IronClust, the best de1834 tection threshold was the default detection threshold; 1835 for SpyKING CIRCUS, this was a detection threshold 1836 of 4.5. For SpyKING CIRCUS 2, we noticed poor de1837 tection of low amplitude units (Figure S5b,e) and thus 1838 also swept over the detection threshold for this algo1839 rithm, but did not achieve an improvement in perfor1840 mance. For IronClust the default adjacency radius is 1841 50, while for MountainSort4 the default is set to all 1842 channels. This large radius led to an incredibly long 1843 run time (10s of hours), and thus we set the Mountain1844 Sort4 adjacency radius to 50 as well. 

## _Comparison to other benchmarking approaches_ 

1847 Here we compare our approach to previous spike1848 sorting benchmarking performed in the literature. The 1849 first approach is to use datasets where the ground1850 truth spiking of a single unit is known. These datasets 1851 are acquired by performing cell-attached recordings 1852 while simultaneously recording with a probe. Then 1853 spike-sorting is performed on the probe and compared 1854 to the ground-truth spiking to determine spike-sorting 1855 performance. Since these are very difficult experi1856 ments, existing ground-truth datasets were acquired 1857 in anesthetized animals and are very short [2, 42–48]. 1858 This makes these datasets much easier to spike sort 1859 compared to long, realistic awake recordings with drift 1860 and with relatively more neuronal firing. Further, such 1861 cell-attached recordings are biased towards larger 1862 and higher firing units, and less likely to be successful 1863 on smaller amplitude units. When SpikeForest used 1864 these ground-truth datasets to compare various spike1865 sorting algorithms (”PAIRED” recordings, https: 1866 //spikeforest.flatironinstitute.org/) [49], 1867 they found that IronClust, Kilosort2 and SpyKING 1868 CIRCUS performed similarly on these recordings. 1869 This is consistent with our own benchmarking results 1870 on the ”no drift” recordings, where many of the 1871 spike-sorting algorithms recovered units with high 1872 amplitudes equally well (Figure S5b,e). However, 1873 most recordings in awake animals have drift and 1874 contain many low amplitude units that can be isolated 1875 by Kilosort. 

1876 Another approach is to create so-called “hybrid 1877 ground-truth datasets”. Either ground-truth units, as 1878 acquired above, or manually curated units are used 1879 [6, 8, 49]. These units can be inserted into other real 1880 recordings, or the same recording in a different posi1881 tion after being subtracted off, to ensure appropriate 1882 background noise. Multiple ground truth units can be 1883 inserted in a dataset in this fashion. However, these 1884 hybrid datasets depend on finding the neurons in the 1885 first place and they also depend on correcting for the 1886 initial drift of the dataset. Alternatively, these ground1887 truth units can be used to create simulations with drift, 1888 in which the units are moved up and down the probe at 1889 some rate over time, then background noise is added 1890 [46, 50]. These simulations do have drift but they have 1891 drawbacks: 1) waveform changes across depths can1892 not occur, but they do in the real data, as demonstrated 1893 in Figure S2a,b, and 2) the background noise is only 1894 simple gaussian noise with the same frequency spec1895 trum as the real data. To remedy (1), we obtained 1896 waveforms at various drift positions from real record1897 ings, as outlined above, to simulate the waveforms 1898 at various depth positions. To remedy (2), we added 1899 600 “multi-units” with low amplitudes to the simulation 1900 to create more realistic background, on top of adding 1901 gaussian noise with a matched frequency spectrum 1902 (Figure S2c). 

1903 The final approach is to instead simulate waveforms, 1904 either using some specified properties [3], or using 1905 the electrical field of a biophysically simulated neuron 1906 [51–54]. These simulators do not produce waveforms 1907 as diverse as real neurons from recordings, likely be1908 cause we lack a full understanding of how the tissue 1909 geometry interacts with action potentials and the probe 1910 to create all the diverse spike shapes that can be ob1911 served. Various types of noise and background can 1912 be added to these neurons. For example these simu1913 lated neurons can be added to background signal from 1914 other recordings [3]. Alternatively noise can be added 1915 by simulating neurons further away from the probe 1916 [53]. Other simulators use spatially correlated noise 1917 with parameters extracted from the data [51, 54]. The 1918 MEAREC simulator includes the option for probe drift; 1919 however it is unclear how much the waveform shape 1920 changes over drift positions in their simulations, as this 1921 depends on the geometry of the electrical fields. 

## **References** 

1922 

- 1923 [1] James J Jun, Catalin Mitelut, Chongxi Lai, 1924 Sergey L Gratiy, Costas A Anastassiou, and Tim1925 othy D Harris. Real-time spike sorting platform 1926 for high-density extracellular probes with ground1927 truth validation and drift correction. _BioRxiv_ , page 1928 101030, 2017. 

23 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 1929 [2] Pierre Yger, Giulia LB Spampinato, Elric Es1930 posito, Baptiste Lefebvre, St´ephane Deny, 1931 Christophe Gardella, Marcel Stimberg, Florian 1932 Jetter, Guenther Zeck, Serge Picaud, et al. A 1933 spike sorting toolbox for up to thousands of elec1934 trodes validated with ground truth recordings in 1935 vitro and in vivo. _Elife_ , 7:e34518, 2018. 

- 1936 [3] Jason E Chung, Jeremy F Magland, Alex H Bar1937 nett, Vanessa M Tolosa, Angela C Tooker, Kye Y 1938 Lee, Kedar G Shah, Sarah H Felix, Loren M 1939 Frank, and Leslie F Greengard. A fully automated 1940 approach to spike sorting. _Neuron_ , 95(6):1381– 1941 1394, 2017. 

- 1942 [4] Alex Rodriguez and Alessandro Laio. Clustering 1943 by fast search and find of density peaks. _science_ , 1944 344(6191):1492–1496, 2014. 

- 1945 [5] Jeremy F Magland and Alex H Barnett. Uni1946 modal clustering using isotonic regression: Iso1947 split. _arXiv preprint arXiv:1508.04841_ , 2015. 

- 1948 [6] Marius Pachitariu, Nicholas Steinmetz, Shabnam 1949 Kadir, Matteo Carandini, and Kenneth D. Har1950 ris. Kilosort: realtime spike-sorting for extracellu1951 lar electrophysiology with hundreds of channels. 1952 _bioRxiv_ , 2016. 

- 1953 [7] Samuel Garcia, Alessio P. Buccino, and Pierre 1954 Yger. How do spike collisions affect spike sort1955 ing performance? _eNeuro_ , 9(5), 2022. 

- 1956 [8] Cyrille Rossant, Shabnam N Kadir, Dan FM 1957 Goodman, John Schulman, Maximilian LD 1958 Hunter, Aman B Saleem, Andres Grosmark, Mar1959 iano Belluscio, George H Denfield, Alexander S 1960 Ecker, et al. Spike sorting for large, dense elec1961 trode arrays. _Nature neuroscience_ , 19(4):634– 1962 641, 2016. 

- 1963 [9] Nicholas A Steinmetz, Cagatay Aydin, Anna 1964 Lebedeva, Michael Okun, Marius Pachitariu, Mar1965 ius Bauza, Maxime Beau, Jai Bhagat, Clau1966 dia B¨ohm, Martijn Broux, et al. Neuropix1967 els 2.0: A miniaturized high-density probe for 1968 stable, long-term brain recordings. _Science_ , 1969 372(6539):eabf4588, 2021. 

- 1970 [10] Guido Van Rossum and Fred L Drake Jr. _Python_ 1971 _reference manual_ . Centrum voor Wiskunde en 1972 Informatica Amsterdam, 1995. 

- 1973 [11] Adam Paszke, Sam Gross, Francisco Massa, 1974 Adam Lerer, James Bradbury, Gregory Chanan, 1975 Trevor Killeen, Zeming Lin, Natalia Gimelshein, 1976 Luca Antiga, Alban Desmaison, Andreas Kopf, 1977 Edward Yang, Zachary DeVito, Martin Raison, 1978 Alykhan Tejani, Sasank Chilamkurthy, Benoit 1979 Steiner, Lu Fang, Junjie Bai, and Soumith 1980 Chintala. Pytorch: An imperative style, high1981 performance deep learning library. In _Advances_ 

- 1982 _in Neural Information Processing Systems 32_ , 1983 pages 8024–8035. Curran Associates, Inc., 2019. 

- 1984 [12] Luke Campagnola. Scientific graphics and 1985 gui library for python. https://github.com/ 1986 pyqtgraph/pyqtgraph, 2020. 

- 1987 [13] Nick Steinmetz, Matteo Carandini, and Ken1988 neth D. Harris. ”Single Phase3” and ”Dual 1989 Phase3” Neuropixels Datasets. 3 2019. 

- 1990 [14] David Arthur and Sergei Vassilvitskii. k-means++: 1991 The advantages of careful seeding. Technical re1992 port, Stanford, 2006. 

- 1993 [15] International Brain Laboratory , Kush Banga, 1994 Julius Benson, Niccol`o Bonacchi, Sebastian A 1995 Bruijns, Rob Campbell, Ga¨elle A Chapuis, 1996 Anne K Churchland, M Felicia Davatolhagh, 1997 Hyun Dong Lee, Mayo Faulkner, Fei Hu, Julia 1998 Hunterberg, Anup Khanal, Christopher Krasniak, 1999 Guido T Meijer, Nathaniel J Miska, Zeinab Mo2000 hammadi, Jean-Paul Noel, Liam Paninski, Alejan2001 dro Pan-Vazquez, Noam Roth, Michael Schart2002 ner, Karolina Socha, Nicholas A Steinmetz, Karel 2003 Svoboda, Marsa Taheri, Anne E Urai, Miles Wells, 2004 Steven J West, Matthew R Whiteway, Olivier Win2005 ter, and Ilana B Witten. Reproducibility of in2006 vivo electrophysiological measurements in mice. 2007 _bioRxiv_ , 2022. 

- 2008 [16] Mark EJ Newman and Michelle Girvan. Finding 2009 and evaluating community structure in networks. 2010 _Physical review E_ , 69(2):026113, 2004. 

- 2011 [17] Vincent A Traag, Ludo Waltman, and Nees Jan 2012 Van Eck. From louvain to leiden: guaranteeing 2013 well-connected communities. _Scientific reports_ , 2014 9(1):1–12, 2019. 

- 2015 [18] Vincent D Blondel, Jean-Loup Guillaume, Re2016 naud Lambiotte, and Etienne Lefebvre. Fast un2017 folding of communities in large networks. _Journal_ 2018 _of statistical mechanics: theory and experiment_ , 2019 2008(10):P10008, 2008. 

- 2020 [19] Jeremy F Magland and James J Jun. Iron2021 clust: Spike sorting software being devel2022 oped at flatiron institute, based on jrclust 2023 (janelia rocket cluster). https://github.com/ 2024 flatironinstitute/ironclust, 2021. 2025 [20] Pierre Yger, Samuel Garcia, and Alessio Paolo 2026 Buccino. spykingcircus2. https://github. 2027 com/SpikeInterface/spikeinterface/ 2028 blob/master/spikeinterface/sorters/si_ 2029 based_sorters/spyking_circus2.py, 2022. 

2026 

2027 

2028 

2029 

- 2030 [21] Roland Diggelmann, Michele Fiscella, Andreas 2031 Hierlemann, and Felix Franke. Automatic spike 2032 sorting for high-density microelectrode arrays. 2033 _Journal of neurophysiology_ , 120(6):3155–3171, 2034 2018. 

24 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 2035 [22] Gerrit Hilgen, Martino Sorbaro, Sahar Pir2036 moradian, Jens-Oliver Muthmann, Ibolya Edit 2037 Kepiro, Simona Ullo, Cesar Juarez Ramirez, Al2038 bert Puente Encinas, Alessandro Maccione, Luca 2039 Berdondini, et al. Unsupervised spike sorting for 2040 large-scale, high-density multielectrode arrays. 2041 _Cell reports_ , 18(10):2521–2532, 2017. 

- 2042 [23] Samuel Garcia and Alessio Paolo Buc2043 cino. tridesclous2. https://github.com/ 2044 SpikeInterface/spikeinterface/blob/ 2045 master/spikeinterface/sorters/si_ 2046 based_sorters/tridesclous2.py, 2022. 

- 2047 [24] Alessio Paolo Buccino, Cole Lincoln Hurwitz, 2048 Samuel Garcia, Jeremy Magland, Joshua H 2049 Siegle, Roger Hurwitz, and Matthias H Hennig. 2050 Spikeinterface, a unified framework for spike sort2051 ing. _Elife_ , 9:e61834, 2020. 

- 2052 [25] Akshay Markanday, Joachim Bellet, Marie E Bel2053 let, Junya Inoue, Ziad M Hafed, and Peter Thier. 2054 Using deep neural networks to detect complex 2055 spikes of cerebellar purkinje cells. _Journal of neu-_ 2056 _rophysiology_ , 123(6):2217–2234, 2020. 

- 2057 [26] Fabian Pedregosa, Ga¨el Varoquaux, Alexan2058 dre Gramfort, Vincent Michel, Bertrand Thirion, 2059 Olivier Grisel, Mathieu Blondel, Peter Pretten2060 hofer, Ron Weiss, Vincent Dubourg, et al. Scikit2061 learn: Machine learning in python. _Journal of_ 2062 _machine learning research_ , 12(Oct):2825–2830, 2063 2011. 

- 2064 [27] Jeff Johnson, Matthijs Douze, and Herv´e J´egou. 2065 Billion-scale similarity search with GPUs. _IEEE_ 2066 _Transactions on Big Data_ , 7(3):535–547, 2019. 

- 2067 [28] Charles R. Harris, K. Jarrod Millman, St´efan J. 2068 van der Walt, Ralf Gommers, Pauli Virtanen, 2069 David Cournapeau, Eric Wieser, Julian Tay2070 lor, Sebastian Berg, Nathaniel J. Smith, Robert 2071 Kern, Matti Picus, Stephan Hoyer, Marten H. 2072 van Kerkwijk, Matthew Brett, Allan Haldane, 2073 Jaime Fern´andez del R´ıo, Mark Wiebe, Pearu 2074 Peterson, Pierre G´erard-Marchant, Kevin Shep2075 pard, Tyler Reddy, Warren Weckesser, Hameer 2076 Abbasi, Christoph Gohlke, and Travis E. Oliphant. 2077 Array programming with NumPy. _Nature_ , 2078 585(7825):357–362, September 2020. 

- 2079 [29] Pauli Virtanen, Ralf Gommers, Travis E. Oliphant, 2080 Matt Haberland, Tyler Reddy, David Courna2081 peau, Evgeni Burovski, Pearu Peterson, Warren 2082 Weckesser, Jonathan Bright, St´efan J. van der 2083 Walt, Matthew Brett, Joshua Wilson, K. Jarrod 2084 Millman, Nikolay Mayorov, Andrew R. J. Nelson, 2085 Eric Jones, Robert Kern, Eric Larson, C J Carey, 2086 ˙Ilhan Polat, Yu Feng, Eric W. Moore, Jake Vander2087 Plas, Denis Laxalde, Josef Perktold, Robert Cim- 

2088 rman, Ian Henriksen, E. A. Quintero, Charles R. 2089 Harris, Anne M. Archibald, Antˆonio H. Ribeiro, 2090 Fabian Pedregosa, Paul van Mulbregt, and SciPy 2091 1.0 Contributors. SciPy 1.0: Fundamental Algo2092 rithms for Scientific Computing in Python. _Nature_ 2093 _Methods_ , 17:261–272, 2020. 

- 2094 [30] Siu Kwan Lam, Antoine Pitrou, and Stanley Seib2095 ert. Numba: A llvm-based python jit compiler. 2096 In _Proceedings of the Second Workshop on the_ 2097 _LLVM Compiler Infrastructure in HPC_ , pages 1– 2098 6, 2015. 

- 2099 [31] Casper da Costa-Luis, Stephen Karl Larroque, 2100 Kyle Altendorf, Hadrien Mary, richardsheridan, 2101 Mikhail Korobov, Noam Raphael, Ivan Ivanov, 2102 Marcel Bargull, Nishant Rodrigues, and et al. 2103 tqdm: A fast, extensible progress bar for python 2104 and cli. Apr 2022. 

- 2105 [32] G. Bradski. The OpenCV Library. _Dr. Dobb’s Jour-_ 2106 _nal of Software Tools_ , 2000. 

   - [33] PyQT. Pyqt reference guide. 2012. 

2107 

- 2108 [34] John D Hunter. Matplotlib: A 2d graphics envi2109 ronment. _Computing in science & engineering_ , 2110 9(3):90, 2007. 

- 2111 [35] Thomas Kluyver, Benjamin Ragan-Kelley, Fer2112 nando P´erez, Brian E Granger, Matthias Bus2113 sonnier, Jonathan Frederic, Kyle Kelley, Jes2114 sica B Hamrick, Jason Grout, Sylvain Corlay, 2115 et al. Jupyter notebooks-a publishing format for 2116 reproducible computational workflows. In _ELPUB_ , 2117 pages 87–90, 2016. 

- 2118 [36] Agnan Kessy, Alex Lewin, and Korbinian Strim2119 mer. Optimal whitening and decorrelation. _The_ 2120 _American Statistician_ , 72(4):309–314, 2018. 

- 2121 [37] St´ephane G Mallat and Zhifeng Zhang. Matching 2122 pursuits with time-frequency dictionaries. _IEEE_ 2123 _Transactions on signal processing_ , 41(12):3397– 2124 3415, 1993. 

2122 

2123 

2124 

- 2125 [38] Jeff Johnson, Matthijs Douze, and Herv´e J´egou. 2126 Billion-scale similarity search with GPUs. _IEEE_ 2127 _Transactions on Big Data_ , 7(3):535–547, 2019. 

2126 

2127 

- 2128 [39] Aapo Hyvarinen. Fast ica for noisy data using 2129 gaussian moments. In _1999 IEEE international_ 2130 _symposium on circuits and systems (ISCAS)_ , vol2131 ume 5, pages 57–61. IEEE, 1999. 

- 2132 [40] James J Jun, Nicholas A Steinmetz, Joshua H 2133 Siegle, Daniel J Denman, Marius Bauza, Brian 2134 Barbarits, Albert K Lee, Costas A Anastassiou, 2135 Alexandru Andrei, C¸ a˘gatay Aydın, et al. Fully 2136 integrated silicon probes for high-density record2137 ing of neural activity. _Nature_ , 551(7679):232–236, 2138 2017. 

25 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

- 2139 [41] Jonathan W Pillow, Jonathon Shlens, 2140 EJ Chichilnisky, and Eero P Simoncelli. A 2141 model-based spike sorting algorithm for re2142 moving correlation artifacts in multi-neuron 2143 recordings. _PloS one_ , 8(5):e62123, 2013. 

- 2144 [42] Darrell A Henze, Zsolt Borhegyi, Jozsef Csicsvari, 2145 Akira Mamiya, Kenneth D Harris, and Gyorgy 2146 Buzsaki. Intracellular features predicted by 2147 extracellular recordings in the hippocampus in 2148 vivo. _Journal of neurophysiology_ , 84(1):390–400, 2149 2000. 

- 2150 [43] Kenneth D Harris, Darrell A Henze, Jozsef 2151 Csicsvari, Hajime Hirase, and Gyorgy Buzsaki. 2152 Accuracy of tetrode spike separation as deter2153 mined by simultaneous intracellular and extracel2154 lular measurements. _Journal of neurophysiology_ , 2155 84(1):401–414, 2000. 

- 2156 [44] DA Henze, KD Harris, Z Borhegyi, J Csicsvari, 2157 A Mamiya, H Hirase, A Sirota, and G Buzs´aki. Si2158 multaneous intracellular and extracellular record2159 ings from hippocampus region ca1 of anes2160 thetized rats. _CRCNS. org_ , 2009. 

- 2161 [45] Joana P Neto, Gonc¸alo Lopes, Jo˜ao Fraz˜ao, 2162 Joana Nogueira, Pedro Lacerda, Pedro Bai˜ao, 2163 Arno Aarts, Alexandru Andrei, Silke Musa, Elvira 2164 Fortunato, et al. Validating silicon polytrodes 2165 with paired juxtacellular recordings: method and 2166 dataset. _Journal of neurophysiology_ , 116(2):892– 2167 903, 2016. 

   - 2191 facing ground-truth validation of automated neu2192 ral spike sorters. _Elife_ , 9:e55167, 2020. 

   - 2193 [50] M Pachitariu, NA Steinmetz, and J Colonell. Kilo2194 sort2. github, 2019. 

   - 2195 [51] Espen Hagen, Torbjørn V Ness, Amir Khos2196 rowshahi, Christina Sørensen, Marianne Fyhn, 2197 Torkel Hafting, Felix Franke, and Gaute T 2198 Einevoll. Visapy: a python tool for biophysics2199 based generation of virtual spiking activity for 2200 evaluation of spike-sorting algorithms. _Journal of_ 2201 _neuroscience methods_ , 245:182–204, 2015. 

   - 2202 [52] Sergey L Gratiy, Yazan N Billeh, Kael Dai, 2203 Catalin Mitelut, David Feng, Nathan W Gouwens, 2204 Nicholas Cain, Christof Koch, Costas A Anastas2205 siou, and Anton Arkhipov. Bionet: A python inter2206 face to neuron for modeling large-scale networks. 2207 _PLoS One_ , 13(8):e0201630, 2018. 

   - 2208 [53] Luis A Camu˜nas-Mesa and Rodrigo Quian 2209 Quiroga. A detailed and fast model of extracellu2210 lar recordings. _Neural computation_ , 25(5):1191– 2211 1212, 2013. 

   - 2212 [54] Alessio Paolo Buccino and Gaute Tomas Einevoll. 2213 Mearec: a fast and customizable testbench simu2214 lator for ground-truth extracellular spiking activity. 2215 _Neuroinformatics_ , 19(1):185–204, 2021. 

- 2168 [46] Andr´e Marques-Smith, Joana P. Neto, Gonc¸alo 2169 Lopes, Joana Nogueira, Lorenza Calcaterra, 2170 Jo˜ao Fraz˜ao, Danbee Kim, Matthew G. Phillips, 2171 George Dimitriadis, and Adam R. Kampff. 2172 Recording from the same neuron with high2173 density cmos probes and patch-clamp: a ground2174 truth dataset and an experiment in collaboration. 2175 _bioRxiv_ , 2020. 

- 2176 [47] A Marques-Smith, JP Neto, G Lopes, J Nogueira, 2177 L Calcaterra, J Fraz˜ao, D Kim, MG Phillips, 2178 G Dimitriadis, and A Kampff. Simultaneous 2179 patch-clamp and dense cmos probe extracellu2180 lar recordings from the same cortical neuron in 2181 anaesthetized rats. _CRCNS. org_ , 10:K0J67F4T, 2182 2018. 

- 2183 [48] Giulia LB Spampinato, Elric Esposito, Pierre 2184 Yger, Jens Duebel, Serge Picaud, and Olivier 2185 Marre. Ground truth recordings for validation of 2186 spike sorting algorithms. March 2018. 

- 2187 [49] Jeremy Magland, James J Jun, Elizabeth 2188 Lovero, Alexander J Morley, Cole Lincoln Hur2189 witz, Alessio Paolo Buccino, Samuel Garcia, and 2190 Alex H Barnett. Spikeforest, reproducible web- 

26 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [480 x 302] intentionally omitted <==**

**S1: Kilosort4 graphical user interface.** The GUI for Kilosort4 enables the user to load in and view the binary file both raw and whitened. Next the user runs the spike-sorting pipeline. The message log box allows the user to monitor the progress of the spike-sorting algorithm. 

**==> picture [434 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
drift-corrected<br>a example unit 1 b example unit 1 example unit 2 c example simulation<br>0<br>10<br>-20 m -10 m 0 m 10 m 20 m<br>example unit 2 20<br>30<br>40<br>example unit 3 example unit 3 example unit 4 50<br>60<br>5 ms<br>example unit 4 10000 1000<br>channel<br>**----- End of picture text -----**<br>


**S2: Simulation features. a,** Four additional example units like in Figure 3c. **b,** The units in **a** after drift correction with the interpolation method from Kilosort 2.5/3/4. Units 1 and 3 interpolate well, while units 2 and 4 do not, due to having features with small spatial footprints. **c,** Example section of the simulation in Figure 3d, but after independent noise was added and the data was un-whitened. 

27 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [288 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
a no drift b medium drift c high drift d fast drift e step drift<br>20 20 40 40 40<br>20 20 20<br>380 m<br>0 1140 m 0 0 0 0<br>1900 m2680 m 20 20 20<br>20 3440 m 20 40 40 40<br>0 30 60 90 0 30 60 90 0 30 60 90 0 5 10 15 0 30 60 90<br>time (min)<br>20 20 40 40 40<br>20 20 20<br>0 0 0 0 0<br>20 20 20<br>20 20 40 40 40<br>0 30 60 90 0 30 60 90 0 30 60 90 0 5 10 15 0 30 60 90<br>20 20 40 40 40<br>20 20 20<br>0 0 0 0 0<br>20 20 20<br>20 20 40 40 40<br>0 30 60 90 0 30 60 90 0 30 60 90 0 5 10 15 0 30 60 90<br>20 20 40 40 40<br>20 20 20<br>0 0 0 0 0<br>20 20 20<br>20 20 40 40 40<br>0 30 60 90 0 30 60 90 0 30 60 90 0 5 10 15 0 30 60 90<br>m)<br>est. depth (<br>**----- End of picture text -----**<br>


**S3: Real drift examples.** These are inferred drift traces from the IBL dataset grouped into: **a,** no/small drift **b,** medium drift, **c,** high drift, **d,** fast drift and **e,** step drift. Note that in many cases different types of drift are combined. 

**==> picture [379 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
a no drift MSE = 0.04 m d fast drift MSE = 5.29 m<br>20 20 20 20<br>ground truth<br>estimated<br>200 380 m1900 m3440 m 200 380 m1140 m1900 m2680 m3440 m 200 200<br>0 15 30 45 20 0 20 0 2 4 6 8 10 20 0 20<br>time (min) ground truth ( m)<br>b medium drift MSE = 0.19 m e step drift MSE = 0.93 m<br>20 20 20 20<br>0 0 0 0<br>20 20 20 20<br>0 15 30 45 20 0 20 0 15 30 45 20 0 20<br>c high drift MSE = 3.21 m f step drift, aligned MSE = 0.60 m<br>20 20 20 20<br>0 0 0 0<br>20 20 20 20<br>0 15 30 45 20 0 20 0 15 30 45 20 0 20<br>m) m)<br>sim depth ( estimated (<br>**----- End of picture text -----**<br>


**S4: Recovered drift traces from simulations. a-f,** Ground truth simulated drift + the drift identified by Kilosort4. (Left) Estimated and true drift traces. (Right) Scatter plot of estimated and true drift traces. 

28 

bioRxiv preprint doi: https://doi.org/10.1101/2023.01.07.523036; this version posted January 7, 2023. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC 4.0 International license. 

**==> picture [504 x 505] intentionally omitted <==**

**----- Start of picture text -----**<br>
a [no drift simulation units] mountain spyking spyking herding<br>1.0 kilosort4 1.0 kilosort3 1.0 kilosort2.5 1.0 kilosort2 1.0 kilosort 1.0 ironclust 1.0 sort4 1.0 circus 1.0 circus2 1.0 hdsort 1.0 spikes 1.0 tridesclous2<br>0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5<br>0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10 1 10<br>firing rate (Hz)<br>b<br>1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0<br>0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5<br>0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50<br>norm<br>c<br>1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0<br>0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5 0.5<br>0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50 10 20 50<br>spatial extent ( m)<br>d no drift medium drift high drift fast drift step drift step drift, aligned<br>1.0 1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4 0.4<br>0.2 0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0 0.0<br>1 10 1 10 1 10 1 10 1 10 1 10<br>firing rate (Hz)<br>e<br>1.0 1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4 0.4<br>0.2 0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0 0.0<br>10 20 10 20 10 20 10 20 10 20 10 20<br>norm<br>f<br>1.0 1.0 1.0 1.0 1.0 1.0<br>0.8 0.8 0.8 0.8 0.8 0.8<br>0.6 0.6 0.6 0.6 0.6 0.6<br>0.4 0.4 0.4 0.4 0.4 0.4<br>0.2 0.2 0.2 0.2 0.2 0.2<br>0.0 0.0 0.0 0.0 0.0 0.0<br>20 50 20 50 20 50 20 50 20 50 20 50<br>spatial extent ( m)<br>score<br>score<br>score<br>score<br>score<br>score<br>**----- End of picture text -----**<br>


**S5: Accuracy as a function of firing rate, amplitude/norm and spatial extent. a-c,** Scatter plots of unit properties (firing rate, norm, spatial extent respectively) versus accuracy, for the no drift simulation. Lines show the average accuracy in bins of wqual numbers of points. **d-f,** Average accuracy curves for all types of simulations and all unit properties (firing rate, norm, spatial extent respectively). 

29 

