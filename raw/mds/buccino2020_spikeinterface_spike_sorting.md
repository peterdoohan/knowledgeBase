TOOLS AND RESOURCES 

**==> picture [104 x 36] intentionally omitted <==**

## Figures and figure supplements 

SpikeInterface, a unified framework for spike sorting 

## Alessio P Buccino et al 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

1 of 14 

Tools and resources 

Neuroscience 

**==> picture [493 x 46] intentionally omitted <==**

**==> picture [180 x 162] intentionally omitted <==**

**==> picture [56 x 71] intentionally omitted <==**

Figure 1. Comparison of spike sorters on a real Neuropixels dataset. (A) A visualization of the activity on the Neuropixels array (top, color indicates spike rate estimated on each channel evaluated with threshold detection) and of traces from the Neuropixels recording (below). (B) The number of detected units for each of the six spike sorters (HS = HerdingSpikes2, KS = Kilosort2, IC = IronClust, TDC = Tridesclous, SC = SpyKING Circus, HDS = HDSort). (C) The total number of units for which k sorters agree (unit agreement is defined as 50% spike match). (D) The number of units (per sorter) for which k sorters agree; most sorters find many units that other sorters do not. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

2 of 14 

Tools and resources 

Neuroscience 

**==> picture [478 x 64] intentionally omitted <==**

**==> picture [61 x 64] intentionally omitted <==**

**==> picture [39 x 57] intentionally omitted <==**

Figure 1—figure supplement 1. Examples of matched units in a Neuropixels recording. The illustration shows units from six spike sorters that were matched by spike train comparison. Panel (A) shows a unit with high agreement score (0.97), and panel (B) a lower agreement score (0.69). In both panels, the top plot shows the spike trains (the first 20 s of the recording) found by each sorter, and below unit templates (estimated from waveforms of 100 spikes randomly sampled from each unit) are shown. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

3 of 14 

Tools and resources 

Neuroscience 

**==> picture [262 x 197] intentionally omitted <==**

Figure 1—figure supplement 2. Cumulative histogram of agreement scores (above threshold of .5 that defines a match) for the ensemble sorting of the simulated ground-truth dataset. This analysis was performed with the six chosen sorters and highlights how over 80% of the matched units had an agreement score greater than 0.8. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

4 of 14 

Tools and resources 

Neuroscience 

**==> picture [492 x 45] intentionally omitted <==**

**==> picture [159 x 172] intentionally omitted <==**

**==> picture [65 x 69] intentionally omitted <==**

**==> picture [56 x 43] intentionally omitted <==**

Figure 1—figure supplement 3. Comparison of spike sorters on a Neuropixels recording. This dataset contains spontaneous neural activity from the rat cortex (motor and somatosensory areas) by Marques-Smith et al., 2018a; Marques-Smith et al., 2018b (dataset spe-c1). The dataset is also available at https://gui.dandiarchive.org/#/dandiset/000034/draft. (A) A visualization of the activity on the Neuropixels array (top, color indicates spike rate estimated on each channel evaluated with threshold detection) and of traces from the Neuropixels recording (below). (B) The number of detected units for each of the six spike sorters (HS = HerdingSpikes2, KS = Kilosort2, IC = IronClust, TDC = Tridesclous, SC = SpyKING Circus, HDS = HDSort). (C) The total number of units for which k sorters agree (unit agreement is defined as 50% spike match). (D) The number of units (per sorter) for which k sorters agree; Most sorters find many units that other sorters do not. The analysis notebook for this analysis can be found at https://spikeinterface. github.io/blog/ensemble-sorting-of-a-neuropixels-recording-2/. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

5 of 14 

Tools and resources 

Neuroscience 

**==> picture [38 x 87] intentionally omitted <==**

**==> picture [127 x 127] intentionally omitted <==**

**==> picture [148 x 238] intentionally omitted <==**

Figure 1—figure supplement 4. Comparison of spike sorters on a Biocam recording from a mouse retina. This retina recording (Hilgen et al., 2017) has 1’024 channels in a square configuration, and a sampling frequency of 23199 Hz. The dataset can be found at https://gui.dandiarchive.org/#/ dandiset/000034/draft. Only four spike sorters were capable of processing this data set (HS = HerdingSpikes2, KS = Kilosort2, IC = IronClust, HDS = HDSort). (A) A visualization of the activity on the Biocam array (top, color indicates spike rate estimated on each channel evaluated with threshold detection) and of traces from the recording (below). (B) The number of detected units for each of the four spike sorters. (C) The total number of units for which k sorters agree (unit agreement is defined as 50% spike match). (D) The number of units (per sorter) for which k sorters agree; most sorters find many units that other sorters do not. The analysis notebook for this analysis can be found at https://spikeinterface.github.io/blog/ensemblesorting-of-a-3brain-biocam-recording-from-a-retina/. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

6 of 14 

Tools and resources 

Neuroscience 

**==> picture [506 x 337] intentionally omitted <==**

**==> picture [136 x 126] intentionally omitted <==**

**==> picture [332 x 124] intentionally omitted <==**

Figure 2. Evaluation of spike sorters on a simulated Neuropixels dataset. (A) A visualization of the activity on and traces from the simulated Neuropixels recording. (B) The signal-to-noise ratios (SNR) for the ground-truth units. (C) The number of detected units for each of the six spike sorters (HS = HerdingSpikes2, KS = Kilosort2, IC = IronClust, TDC = Tridesclous, SC = SpyKING Circus, HDS = HDSort). (D) The accuracy, precision, and recall of each sorter on the ground-truth units. (E) A breakdown of the detected units for each sorter (precise definitions of each unit type can be found in the SpikeComparison Section of the Methods). The horizontal dashed line indicates the number of ground-truth units (250). 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

7 of 14 

Tools and resources 

Neuroscience 

**==> picture [514 x 235] intentionally omitted <==**

Figure 2—figure supplement 1. Evaluation of spike sorters performance metrics. (A) Precision versus recall for the ground-truth comparison the simulated dataset. Some sorters seem to favor precision (HerdingSpikes, SpyKING Circus, HDSort), others instead have higher recall (Ironclust) or score well on both measures (Kilosort2). Tridesclous does not show a bias towards precision or recall. (B) Accuracy versus SNR. All the spike sorters (except Kilosort2) show a strong dependence of performance with respect to the SNR of the ground-truth units. Kilosort2, remarkably, is capable of achieving a high accuracy also for low-SNR units. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

8 of 14 

Tools and resources 

Neuroscience 

**==> picture [506 x 413] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>Units agreed upon HS KS IC<br>by k sorters 222 68 168 30 21 6<br>20<br>13 50<br>659 k= 27 37<br>1<br>30<br>2<br>3 38<br>139 139 139<br>4<br>5<br>TDC SC HDS<br>6<br>28 129 226<br>2 5<br>139 2 7<br>18 28<br>8<br>35 24<br>18 27 [30 38] 28<br>139 32 139<br>139<br>C<br>HS KS IC TDC SC HDS<br>false positive<br>200<br>matched<br>100<br>0<br>D 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6<br>20<br>10<br>1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6 1 2 3 4 5 6<br>Found by # sorters<br>Number of units<br>Ground truth SNR<br>**----- End of picture text -----**<br>


Figure 3. Comparison of spike sorters on a simulated Neuropixels dataset. (A) The total number of units for which k sorters agree (unit agreement is defined as 50% spike match). (B) The number of units (per sorter) for which k sorters agree; Most sorters find many units that other sorters do not. (HS = HerdingSpikes2, KS = Kilosort2, IC = IronClust, TDC = Tridesclous, SC = SpyKING Circus, HDS = HDSort) (C) Number of matched ground-truth units (blue) and false positive units (red) found by each sorter on which k sorters agree upon. Most of the false positive units are only found by a single sorter. Number of false positive units found by k � `2` sorters: HS = 4, KS = 4, IC = 4, SC = 2, TDC = 1, HDS = 2. (D) Signal-to-noise ratio (SNR) of ground-truth unit with respect to the number of k sorters agreement. Results are split by sorter. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

9 of 14 

Tools and resources 

Neuroscience 

**==> picture [321 x 194] intentionally omitted <==**

Figure 3—figure supplement 1. The fractions of predicted false and true positive units from ensembles using different numbers of sorters. All possible subsets of two to five of the six sorters were tested by removing corresponding units from the full sorting comparison. Each dot corresponds to one unique combination of sorters. This analysis shows that false positive units are well-identified using pairs of sorters (almost all false positive units are only found by one sorter), indicating that the sorters are biased in different ways. However, the fraction of true positives in the ensemble (at least two sorters agree) can be significantly lower when only pairs of sorters are used. This is explained by the fact that, for this dataset, a fraction of true positive units are only found by one sorter (as expected since the quality of detection and isolation of the units varies among sorters). In contrast, using four or more sorters reliably identifies most true positive units. For two sorters, the most reliable identification of true positives was achieved by combining two of Kilosort2, Ironclust, and HDSort. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

10 of 14 

Tools and resources 

Neuroscience 

**==> picture [259 x 194] intentionally omitted <==**

Figure 3—figure supplement 2. The SNR of all units found by Kilosort2 in the ground-truth data separated into those with and without matches in the ground-truth spike trains. Many detected false positive units have an SNR above the mode of the ground-truth SNR, indicating that SNR is not a good measure to separate false and true positives in this case. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

11 of 14 

Tools and resources 

Neuroscience 

**==> picture [13 x 15] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


**==> picture [413 x 198] intentionally omitted <==**

**----- Start of picture text -----**<br>
B Percent all units<br>with match in curated sets<br>Curated 1<br>HS Curated 2<br>Curated 1 Curated 2 100<br>19<br>10 48<br>HDS 60 KS<br>20<br>207<br>22<br>45<br>174 SC IC<br>Kilosort2<br>TDC<br>**----- End of picture text -----**<br>


**==> picture [426 x 26] intentionally omitted <==**

**----- Start of picture text -----**<br>
C Percent consensus units D Percent non-consensus units<br>with match in curated sets with match in curated sets<br>**----- End of picture text -----**<br>


**==> picture [367 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
HS HS<br>100<br>20<br>HDS 60 KS HDS KS<br>10<br>20<br>SC IC SC IC<br>TDC TDC<br>**----- End of picture text -----**<br>


Figure 4. Comparison between consensus and manually curated outputs. (A) Venn diagram showing the agreement between Curator 1 and 2. 174 units are discarded by both curators from the Kilsort2 output. (B) Percent of matched units between the output of each sorter and C1 (red) and C2 (blue). Ironclust has the highest match with both curated datasets. (C) Similar to C, but using the consensus units (units agreed upon by at least two sorters - k � `2` ). The percent of matching with curated datasets is now above 70% for all sorters, with Kilosort2 having the highest match (KSc TC1 = 84.55%, KScTC2 = 89.55%), slightly higher than Ironclust (ICc T C1 = 82.63%, ICc T C2 = 83.83%). (D) Percent of non-consensus units (k ¼ `1` ) matched to curated datasets. The only significant overlap is between Curator one and Kilosort2, with a percent around 18% (KSnc T C1 = 18.58%, KSnc T C2 = 24.34%). 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

12 of 14 

Tools and resources 

Neuroscience 

**==> picture [512 x 126] intentionally omitted <==**

**----- Start of picture text -----**<br>
spikeinterface<br>.extractors .toolkit .sorters .comparison .widgets<br>spikeextractors spiketoolkit spikesorters spikecomparison spikewidgets<br>Recorded Data File IO Preprocessing Spike Sorting Sorter Comparison Visualization Widgets<br>Sorted Data File IO Postprocessing Job Launching Ground Truth Comparison<br>Probe File IO Validation Ground Truth Studies<br>Curation<br>**----- End of picture text -----**<br>


Figure 5. Overview of SpikeInterface’s Python packages, their different functionalities, and how they can be accessed by our meta-package, spikeinterface. 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

13 of 14 

Tools and resources 

Neuroscience 

**==> picture [514 x 264] intentionally omitted <==**

Figure 6. Sample spike sorting pipeline using SpikeInterface. (A) A diagram of a sample spike sorting pipeline. Each processing step is colored to represent the SpikeInterface package in which it is implemented and the dashed, colored arrows demonstrate how the Extractors are used in each processing step. (B) How to use the Python API to build the pipeline shown in (A). (C) How to use the GUI to build the pipeline shown in (A). 

Buccino, Hurwitz, et al. eLife 2020;9:e61834. DOI: https://doi.org/10.7554/eLife.61834 

14 of 14 

