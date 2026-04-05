## **Neuroscience** 

## **Reviewed Preprint** 

**v2 •** March 14, 2025 Revised by authors 

## **Reviewed Preprint** 

**v1 •** October 31, 2024 

## **Reproducibility of** _**in vivo**_ **electrophysiological measurements in mice** 

**International Brain Laboratory, Kush Banga, Julius Benson, Jai Bhagat, Dan Biderman, Daniel Birman, Niccolò Bonacchi, Sebastian A Bruijns, Kelly Buchanan, Robert AA Campbell, Matteo Carandini, Gaëlle A Chapuis, Anne K Churchland , M Felicia Davatolhagh, Hyun Dong Lee, Mayo Faulkner, Berk Gerçek, Fei Hu, Julia Huntenburg, Cole Hurwitz, Anup Khanal, Christopher Krasniak, Christopher Langfield, Petrina Lau, Nancy Mackenzie, Guido T Meijer, Nathaniel J Miska, Zeinab Mohammadi, Jean-Paul Noel, Liam Paninski, Alejandro Pan-Vazquez, Cyrille Rossant, Noam Roth, Michael Schartner, Karolina Socha, Nicholas A Steinmetz, Karel Svoboda, Marsa Taheri, Anne E Urai, Shuqi Wang, Miles Wells, Steven J West, Matthew R Whiteway, Olivier Winter, Ilana B Witten, Yizi Zhang** 

Max-Planck-Institute, Tübingen, Germany • University College London, London, United Kingdom • New York University, New York, United States • Columbia University, New York, United States • Department of Neurobiology and Biophysics, University of Washington, Seattle, United States • William James Center for Research, ISPA - Instituto Universitário, Lisbon, Portugal • Sainsbury Wellcome Center, London, United Kingdom • University of Geneva, Geneva, Switzerland • University of California Los Angeles, Los Angeles, United States • University of California, Berkeley, Berkeley, United States • Champalimaud Foundation, Lisbon, Portugal • Cold Spring Harbor Laboratory, New York, United States • Princeton University, Princeton, United States • Allen Institute for Neural Dynamics, Seattle, United States • Leiden University, Leiden, Netherlands • School of Computer and Communication Sciences, EPFL, Lausanne, Switzerland 

https://en.wikipedia.org/wiki/Open_access 

Copyright information 

## **eLife Assessment** 

This paper represents an **important** contribution to the field. Summarizing results from neural recording experiments in mice across ten labs, the work provides **compelling** evidence that basic electrophysiology features, single-neuron functional properties, and population-level decoding are fairly reproducible across labs with proper preprocessing. The results and suggestions regarding preprocessing and quality metrics may be of significant interest to investigators carrying out such experiments in their own labs. 

https://doi.org/10.7554/eLife.100840.2.sa3 

## **Abstract** 

Understanding brain function relies on the collective work of many labs generating reproducible results. However, reproducibility has not been systematically assessed within the context of electrophysiological recordings during cognitive behaviors. To address this, we formed a multi-lab collaboration using a shared, open-source behavioral task and experimental apparatus. Experimenters in ten laboratories repeatedly targeted Neuropixels probes to the same location (spanning secondary visual areas, hippocampus, and thalamus) 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

1 of 89 

in mice making decisions; this generated a total of 121 experimental replicates, a unique dataset for evaluating reproducibility of electrophysiology experiments. Despite standardizing both behavioral and electrophysiological procedures, some experimental outcomes were highly variable. A closer analysis uncovered that variability in electrode targeting hindered reproducibility, as did the limited statistical power of some routinely used electrophysiological analyses, such as single-neuron tests of modulation by individual task parameters. Reproducibility was enhanced by histological and electrophysiological qualitycontrol criteria. Our observations suggest that data from systems neuroscience is vulnerable to a lack of reproducibility, but that across-lab standardization, including metrics we propose, can serve to mitigate this. 

## **Introduction** 

Reproducibility is a cornerstone of the scientific method: a given sequence of experimental methods should lead to comparable results if applied in different laboratories. In some areas of biological and psychological science, however, the reliable generation of reproducible results is a well-known challenge ( Crabbe et al., 1999 ; Sittig et al., 2016 ; Baker, 2016 ; Voelkl et al., 2020 ; Li et al., 2021 ; Errington et al., 2021 ). In systems neuroscience at the level of singlecell-resolution recordings, evaluating reproducibility is difficult: experimental methods are sufficiently complex that replicating experiments is technically challenging, and many experimenters feel little incentive to do such experiments since negative results can be difficult to publish. Unfortunately, variability in experimental outcomes has been well-documented on a number of occasions. These include the existence and nature of "preplay" ( Dragoi and Tonegawa, 2011 ; Silva et al., 2015 ; Ólafsdóttir et al., 2015 ; Grosmark and Buzsáki, 2016 ; Liu et al., 2019 ), the persistence of place fields in the absence of visual inputs ( Hafting et al., 2005 ; Barry et al., 2012 ; Chen et al., 2016 ; Waaga et al., 2022 ), and the existence of spike-timing dependent plasticity (STDP) in nematodes ( Zhang et al., 1998 ; Tsui et al., 2010 ). In the latter example, variability in experimental results arose from whether the nematode being studied was pigmented or albino, an experimental feature that was not originally known to be relevant to STDP. This highlights that understanding the source of experimental variability can facilitate efforts to improve reproducibility. 

For electrophysiological recordings, several efforts are currently underway to document this variability and reduce it through standardization of methods ( de Vries et al., 2020 ; Siegle et al., 2021 ). These efforts are promising, in that they suggest that when approaches are standardized and results undergo quality control, observations conducted within a single organization can be reassuringly reproducible. However, this leaves unanswered whether observations made in separate, individual laboratories are reproducible when they likewise use standardization and quality control. Answering this question is critical since most neuroscience data is collected within small, individual laboratories rather than large-scale organizations. A high level of reproducibility of results across laboratories when procedures are carefully matched is a prerequisite to reproducibility in the more common scenario in which two investigators approach the same highlevel question with slightly different experimental protocols. Therefore, establishing the extent to which observations are replicable even under carefully controlled conditions is critical to provide an upper bound on the expected level of reproducibility of findings in the literature more generally. 

We have previously addressed the issue of reproducibility in the context of mouse psychophysical behavior, by training 140 mice in 7 laboratories and comparing their learning rates, speed, and accuracy in a simple binary visually-driven decision task. We demonstrated that standardized protocols can lead to highly reproducible behavior ( The International Brain Laboratory et al., 2021 ). Here, we build on those results by measuring within- and across-lab variability in the context of intra-cerebral electrophysiological recordings. We repeatedly inserted Neuropixels 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

2 of 89 

multi-electrode probes ( Jun et al., 2017 ) targeting the same brain regions (including secondary visual areas, hippocampus, and thalamus) in mice performing an established decision-making task ( The International Brain Laboratory et al., 2021 ). We gathered data across ten different labs and developed a common histological and data processing pipeline to analyze the resulting large datasets. This pipeline included stringent new histological and electrophysiological quality-control criteria (the "Recording Inclusion Guidelines for Optimizing Reproducibility", or RIGOR) that are applicable to datasets beyond our own. 

We define reproducibility as a lack of systematic across-lab differences: that is, the distribution of within-lab observations is comparable to the distribution of across-lab observations, and thus a data analyst would be unable to determine in which lab a particular observation was measured. This definition takes into account the natural variability in electrophysiological results. After applying the RIGOR quality control measures, we found that features such as neuronal yield, firing rate, and LFP power were reproducible across laboratories according to this definition. However, the proportions of cells modulated and the precise degree of modulation by single decision-making variables, such as the sensory stimulus or the choice, while reproducible for many tests and brain regions, sometimes failed to reproduce in some regions (tests that considered the a neuron’s full response profile were more robust). To interpret potential lab-to-lab differences in reproducibility, we developed a multi-task neural network encoding model that allows nonlinear interactions between variables. We found that within-lab random effects captured by this model were comparable to between-lab random effects. Taken together, these results suggest that electrophysiology experiments are vulnerable to a lack of reproducibility, but that standardization of procedures and quality control metrics can help to mitigate this problem. 

## **Results** 

## **Neuropixels recordings during decisionmaking target the same brain location** 

To quantify reproducibility across electrophysiological recordings, we set out to establish standardized procedures across the International Brain Laboratory (IBL) and to test whether this standardization led to reproducible results. Ten IBL labs collected Neuropixels recordings from one repeated site, targeting the same stereotaxic coordinates, during a standardized decisionmaking task in which head-fixed mice reported the perceived position of a visual grating ( The International Brain Laboratory et al., 2021 ). The experimental pipeline was standardized across labs, including surgical methods, behavioral training, recording procedures, histology, and data processing ( **Figure 1a, b** , **Figure 1-supplemental 1** ); see Methods for full details. Neuropixels probes were selected as the recording device for this study due to their standardized industrial production, and their 384 dual-band, low-noise recording channels providing the ability to sample many neurons in each of multiple brain regions simultaneously. In each experiment, Neuropixels 1.0 probes were inserted, targeted at −2.0 mm AP, −2.24 mm ML, 4.0 mm DV relative to bregma; 15° angle ( **Figure 1c** ). This site was selected because it encompasses brain regions implicated in visual decision-making, including visual area a/am ( Najafi et al., 2020 ; Harvey et al., 2012 ), dentate gyrus, CA1, ( Turk-Browne, 2019 ), and lateral posterior (LP) and posterior (PO) thalamic nuclei ( Saalmann and Kastner, 2011 ; Roth et al., 2016 ). 

Once data were acquired and brains were processed, we visualized probe trajectories using the Allen Institute Common Coordinate Frame ( **Figure 1d** , more methodological information is below). This allowed us to associate each neuron with a particular region ( **Figure 1e** ). To evaluate whether our data were of comparable quality to previously published datasets ( Steinmetz et al., 2019 ; Siegle et al., 2021 ), we compared the neuron yield. The yield of an insertion, defined as the number of quality control (QC)-passing units recovered per electrode site, is informative about the quality of both the raw recording and the spike sorting pipeline. We 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

3 of 89 

**==> picture [398 x 402] intentionally omitted <==**

**Figure 1.** 

## **Standardized experimental pipeline and apparatus; location of the repeated site.** 

**(a)** , The pipeline for electrophysiology experiments. **(b)** , Drawing of the experimental apparatus. **(c)** , Location and brain regions of the repeated site. VISa: Visual Area A/AM; CA1: Hippocampal Field CA1; DG: Dentate Gyrus; LP: Lateral Posterior nucleus of the thalamus; PO: Posterior Nucleus of the Thalamus. Black lines: boundaries of sub regions within the five repeated site regions. **(d)** , Gray lines: Actual repeated site trajectories shown within a 3D brain schematic. Red line: planned trajectory **(e)** , Raster plot of all measured neurons (including some that ultimately failed quality control) from one example session. **(f)** , A comparison of neuron yield (neurons/channel of the Neuropixels probe) for this dataset (IBL), _Steinmetz et al_ . (2019) (STE) and _Siegle et al_ . (2021) (ALN) in 3 neural structures. Bars: standard error of the mean; the center of each bar corresponds to the mean neuron yield for the corresponding study. **Figure 1–Figure supplement 1** . Detailed experimental pipeline for the Neuropixels experiment. **Figure 1–Figure supplement 2** . Electrophysiology data quality examples. **Figure 1–Figure supplement 3** . Detailed comparison of yield between our dataset and published reference datasets. **Figure 1–Figure supplement 4** . Visual inspection of datasets by three observers blinded to data identity yielded similar metrics for all three studies. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**4 of 89** 

performed a comparative yield analysis of the repeated site insertions and the external electrophysiology datasets. Both external datasets were recorded from mice performing a visual task, and include insertions from diverse brain regions. 

Different spike sorting algorithms detect distinct units as well as varying numbers of units, and yield is sensitive to the inclusion criteria for putative neurons. We therefore re-analyzed the two comparison datasets using IBL’s spike sorting pipeline ( _The International Brain Laboratory et al., 2022a_ ). When filtered using identical quality control metrics and split by brain region, we found the yield was comparable across datasets within each region ( **Figure 1f** ). A two-way ANOVA on the yield per insertion with dataset (IBL, Steinmetz, or Allen/Siegle) and region (Cortex, Thalamus, or Hippocampus) as categorical variables showed no significant effect of dataset origin (p=0.31), but a significant effect of brain region ( _p <_ 10[−17] ). Systematic differences between our dataset and others were likewise absent for a number of other metrics ( **Figure 1-supplemental 3** ). 

Finally, in addition to the quantitative assessment of data quality, a qualitative assessment was performed. 100 total insertions were randomly selected from the three datasets and assigned random IDs to blind the raters during manual assessment. Three raters were asked to look at snippets of raw data traces with spikes overlaid and rate the overall quality of the recording and spike detection on a scale from 1-10, taking into account the apparent noise levels, drift, artifacts, and missed spikes. We found no evidence for systematic quality differences across the datasets ( **Figure 1-supplemental 4** ). 

## **Stereotaxic probe placement limits resolution of probe targeting** 

As a first test of experimental reproducibility, we assessed variability in Neuropixels probe placement around the planned repeated site location. Brains were perfusion-fixed, dissected, and imaged using serial section 2-photon microscopy for 3D reconstruction of probe trajectories ( **Figure 2a** ). Whole brain auto-fluorescence data was aligned to the Allen Common Coordinate Framework (CCF) ( Wang et al., 2020 ) using an elastix-based pipeline ( Klein et al., 2010 ) adapted for mouse brain registration ( West, 2021 ). cm-DiI labelled probe tracks were manually traced in the 3D volume ( **Figure 2b** ; **Figure 2, supp. 1** ). Trajectories obtained from our stereotaxic system and traced histology were then compared to the planned trajectory. To measure probe track variability, each traced probe track was linearly interpolated to produce a straight line insertion in CCF space ( **Figure 2c** ). 

We first compared the micro-manipulator brain surface coordinate to the planned trajectory to assess variance due to targeting strategies only (targeting variability, **Figure 2d** ). Targeting variability occurs when experimenters must move probes slightly from the planned location to avoid blood vessels or irregularities. These slight movements of the probes led to sizeable deviations from the planned insertion site ( **Figure 2d** and **g** , total mean displacement = 104 µm). 

Geometrical variability, obtained by calculating the difference between planned and final identified probe position acquired from the reconstructed histology, encompasses targeting variance, anatomical differences, and errors in defining the stereotaxic coordinate system. Geometrical variability was more extensive ( **Figure 2e** and **h** , total mean displacement = 356.0 µm). Assessing geometrical variability for all probes with permutation testing revealed a p- value of 0.19 across laboratories ( **Figure 2h** ), arguing that systematic lab-to-lab differences don’t account for the observed variability. 

To determine the extent that anatomical differences drive this geometrical variability, we regressed histology-to-planned probe insertion distance at the brain surface against estimates of animal brain size. Regression against both animal body weight and estimated brain volume from histological reconstructions showed no correlation to probe displacement (R[2] < 0.03), suggesting differences between CCF and mouse brain sizes are not the major cause of variance. An 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

5 of 89 

**==> picture [348 x 402] intentionally omitted <==**

**Figure 2.** 

## **Histological reconstruction reveals resolution limit of probe targeting.** 

**(a)** , Histology pipeline for electrode probe track reconstruction and assessment. Three separate trajectories are defined per probe: planned, micro-manipulator (based on the experimenter’s stereotaxic coordinates) and histology (interpolated from tracks traced in the histology data). **(b)** , Example tilted slices through the histology reconstructions showing the repeated site probe track. Plots show the green auto-fluorescence data used for CCF registration and red cm-DiI signal used to mark the probe track. White dots show the projections of channel positions onto each tilted slice. Scale bar: 1mm. **(c)** , Histology probe trajectories, interpolated from traced probe tracks, plotted as 2D projections in coronal and sagittal planes, tilted along the repeated site trajectory over the allen CCF, colors: laboratory. Scale bar: 1mm. **(d, e, f)** , Scatterplots showing variability of probe placement from planned to: micro-manipulator brain surface insertion coordinate (d, targeting variability, N=88), histology brain surface insertion coordinate (e, geometrical variability, N=98), and histology probe angle (f, angle variability, N=99). Each line and point indicates the displacement from the planned geometry for each insertion in anterior-posterior (AP) and mediolateral (ML) planes, color-coded by institution. **(g, h, i)** , Assessment of probe displacement by institution from planned to: micro-manipulator brain surface insertion coordinate (g, N=88), histology brain surface insertion coordinate (h, N=98), and histology probe angle (i, N=99). Kernel density estimate plots (top) are followed by boxplots (bottom) for probe displacement, ordered by descending median value. A minimum of four data points per institution led to their inclusion in the plot and subsequent analysis. Dashed vertical lines display the mean displacement across institutions, indicated in the respective scatterplot in (d, e, f). 

**Figure 2–Figure supplement 1** . Tilted slices of histology along the probe insertion for all insertions used in assessing probe placement. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**6 of 89** 

alternative explanation is that geometrical variance in probe placement at the brain surface is driven by inaccuracies in defining the stereotaxic coordinate system, including discrepancies between skull landmarks and the underlying brain structures. 

Accurate placement of probes in deeper brain regions is critically dependent on probe angle. We assessed probe angle variability by comparing the final histologically-reconstructed probe angle to the planned trajectory. We observed a consistent mean displacement from the planned angle in both medio-lateral (ML) and anterior-posterior (AP) angles ( **Figure 2f** and **i** , total mean difference in angle from planned: 7.5 degrees). Angle differences can be explained by the different orientations and geometries of the CCF and the stereotaxic coordinate systems, which we have recently resolved in a corrected atlas ( Birman et al., 2023 ). The difference in histology angle to planned probe placement was assessed with permutation testing across labs, and shows a p-value of 0.45 ( **Figure 2i** ). This suggests that systematic lab-to-lab differences were minimal. 

In conclusion, insertion variance, in particular geometrical variability, is sizeable enough to impact probe targeting to desired brain regions and poses a limit on the resolution of probe targeting. The histological reconstruction, fortunately, does provide an accurate reflection of the true probe trajectory ( Liu et al., 2021 ), which is essential for interpretation of the Neuropixels recording data. We were unable to identify a prescriptive analysis to account for probe placement variance, which may reflect that the major driver of probe placement variance derives from differences in skull landmarks used for establishing the coordinate system and the underlying brain structures. Our data suggest the resolution of probe insertion targeting on the brain surface to be approximately 360 µm (based on the mean across labs, see **Figure 2h** ), which must be taken into account when planning probe insertions. 

## **Reproducibility of electrophysiological features** 

Having established that targeting of Neuropixels probes to the desired target location was a source of substantial variability, we next measured the variability and reproducibility of electrophysiological features recorded by the probes. We implemented twelve exclusion criteria. Two of these were specific to our experiments: a behavior criterion where the mouse completed at least 400 trials of the behavioral task, and a session number criterion of at least 3 sessions per lab for analyses that directly compared across labs (permutation tests; **Figure 3d,e** , **Figure 4g** , **Figure 5** ). The remaining ten criteria, which we collectively refer to as the "Recording Inclusion Guidelines for Optimizing Reproducibility" (RIGOR; **Table 1** ), are more general and can be applied widely to electrophysiology experiments: a yield criterion, a noise criterion, LFP power criterion, qualitative criteria for visual assessment (lack of drift, epileptiform activity, noisy channels and artifacts, see **Figure 1-supplement 2** for examples), and single unit metrics (refractory period violation, amplitude cutoff, and median spike amplitude). These metrics could serve as a benchmark for other studies to use when reporting results, acknowledging that a subset of the metrics will be adjusted for measurements made in different animals, regions or behavioral contexts. The RIGOR metrics, along with additional analysis-specific constraints, determined the number of neurons, mice, and sessions included in subsequent analyses presented here (See spreadsheet). 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

7 of 89 

**==> picture [471 x 616] intentionally omitted <==**

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

8 of 89 

## **Figure 3.** 

## **Electrophysiological features are mostly reproducible across laboratories.** 

**(a)** , Number of experimental sessions recorded; number of sessions used in analysis due to exclusion criteria. Upper branches: exclusions based on RIGOR criteria ( **Table 1** ); lower branches: exclusions based on IBL-specific criteria. For the rest of this figure an additional targeting criterion was used in which an insertion had to hit 2 of the target regions to be included. **(b)** , Power spectral density between 20 and 80 Hz of each channel of each probe insertion (vertical columns) shows reproducible alignment of electrophysiological features to histology. Insertions are aligned to the boundary between the dentate gyrus and thalamus. Tildes indicate that the probe continued below -2.0mm. Location of channels reflect the data after the probes have been adjusted using electrophysiological features CSHL: Cold Spring Harbor Laboratory [(C): Churchland lab, (Z): Zador lab], NYU: New York University, SWC: Sainsbury Wellcome Centre, UCL: University College London, UCLA: University of California, Los Angeles, UW: University of Washington. **(c)** , Firing rates of individual neurons according to the depth at which they were recorded. Colored blocks indicate the target brain regions of the repeated site, grey blocks indicate a brain region that was not one of the target regions. If no block is plotted, that part of the brain was not recorded by the probe because it was inserted too deep or too shallow. Each dot is a neuron, colors indicate firing rate. Probes within each institute are sorted according to their distance from the planned repeated site location. **(d)** , P-values for five electrophysiological metrics, computed separately for all target regions, assessing the reproducibility of the distributions over these features across labs. P-values are plotted on a log-scale to visually emphasize values close to significance. **(e)** , A Random Forest classifier could successfully decode the brain region from five electrophysiological features (neuron yield, firing rate, LFP power, AP band RMS and spike amplitude), but could only decode lab identity from the dentate gyrus. The red line indicates the decoding accuracy and the grey violin plots indicate a null distribution obtained by shuffling the labels 500 times. The decoding of lab identity was performed per brain region. (* p < 0.05, *** p < 0.001) 

**Figure 3–Figure supplement 1** . Recordings that did not pass QC can be visually assessed as outliers. 

**Figure 3–Figure supplement 2** . High LFP power in dentate gyrus was used to align probe locations in the brain. 

**Figure 3–Figure supplement 3** . Bilateral recordings assess within- vs across-animal variance. 

**Figure 3–Figure supplement 4** . Values used in the decoding analysis, per metric and per brain region. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

9 of 89 

**==> picture [471 x 611] intentionally omitted <==**

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 10 of 89 

**Figure 4.** 

## **Neural activity is modulated during decision-making in five neural structures and is variable between laboratories.** 

**(a)** , Raster plot (top) and firing rate time course (bottom) of an example neuron in LP, aligned to movement onset, split for correct left and right choices. The firing rate is calculated using a causal sliding window; each time point includes a 60 ms window prior to the indicated point. **(b)** , Peri-event time histograms (PETHs) of all LP neurons from a single mouse, aligned to movement onset (only correct choices in response to right-side stimuli are shown). These PETHs are baseline-subtracted by a pre-stimulus baseline. Shaded areas show standard error of mean (and propagated error for the overall mean). The thicker line shows the average over this entire population, colored by the lab from which the recording originates. **(c,d)** , Average PETHs from all neurons of each lab for LP (c) and the remaining four repeated site brain regions (d). Shaded regions indicate one standard error of the mean. **(e)** , Schematic defining all six task-modulation tests ( _top_ ) and proportion of task-modulated neurons for each mouse in each brain region for an example test (movement initiation) ( _bottom_ ). Each row within a region correspond to a single lab (colors same as in (d), points are individual sessions). Horizontal lines around vertical marker: S.E.M. around mean across lab sessions **(f)** , Schematic to describe the power analysis. Two hypothetical distributions: first, when the test is sensitive, a small shift in the distribution is enough to make the test significant (non-significant shifts shown with broken line in grey, significant shift outlined in red). By contrast, when the test is less sensitive, the vertical line is large and a corresponding large range of possible shifts is present. The possible shifts we find usually cover only a small range. **(g)** Power analysis example for modulation by the stimulus in CA1. Violin plots: distributions of firing rate modulations for each lab; horizontal line: mean across lab; vertical line at right: how much the distribution can shift up- or downwards before the test becomes significant, while holding other labs constant. **(h)** Permutation test results for task-modulated activity and the Fano Factor. Top: tests based on proportion of modulated neurons (or in the case of Fano Factor, proportion of neurons with a value <1); Bottom: tests based on the distribution of firing rate modulations (or Fano Factor values). Comparisons performed for correct trials with nonzero contrast stimuli. (Figure analyses include collected data that pass our quality metrics and have at least 4 good units in the specified brain region and 3 recordings from the specified lab, to ensure that the data from a lab can be considered representative.) 

**Figure 4–Figure supplement 1** . Proportion of task-modulated neurons, defined by six statistical comparisons, across mice, labs, and brain regions. 

**Figure 4–Figure supplement 2** . Power analysis of permutation tests 

We recorded a total of 121 sessions targeted at our planned repeated site ( **Figure 3a** ). Of these, 18 sessions were excluded due to incomplete data acquisition caused by a hardware failure during the experiment (10) or because we were unable to complete histology on the subject (8). Next, we applied exclusion criteria to the remaining complete datasets. We first applied the RIGOR standards described in **Table 1** . Upon manual inspection, we observed 1 recording fail due to drift, 10 recordings fail due to a high and unrecoverable count of noisy channels, 2 recordings fail due to artefacts, and 1 recording fail due to epileptiform activity. 1 recording failed our criterion for low yield, and 1 recording failed our criterion for noise level (both automated quality control criteria). Next, we applied criteria specific to our behavioral experiments, and found that 5 recordings failed our behavior criterion by not meeting the minimum of 400 trials completed). Some of our analysis also required further (stricter) inclusion criteria (see Methods). 

When plotting all recordings, including those that failed to meet quality control criteria, one can observe that many discarded sessions were clear outliers ( **Figure 3-supplemental 1** ). In subsequent figures, only recordings that passed these quality control criteria were included. Overall, we analyzed data from the 82 remaining sessions recorded in ten labs to determine the 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

11 of 89 

**==> picture [444 x 345] intentionally omitted <==**

**Figure 5.** 

## **Principal component embedding of trial-averaged activity uncovers differences that are clear region-to-region and more modest lab-to-lab.** 

**(a)** PETHs from two example cells (black, fast reaction times only) and 2-PC-based reconstruction (red). Goodness of fit _r_[2] indicated on top with an example of a poor (top) and good (bottom) fit. **(b)** Histograms of reconstruction goodness of fit across all cells based on reconstruction by 1-3 PCs. Since PETHs are well approximated with just the first 2 PCs, subsequent analyses used the first 2 PCs only. **(c)** Two-dimensional embedding of PETHs of all cells colored by region (each dot corresponds to a single cell). **(d)** Mean firing rates of all cells per region, note visible pink/green divide in line with the scatter plot. Error bands are standard deviation across cells normalised by the square root of the number of cells in the region **(e)** Cumulative distribution of the first embedding dimension (PC1, as shown in **(c)** ) per region with inset of KS statistic, measuring the maximum absolute difference between the cumulative distribution of a region’s first PC values and that of the remaining cells; asterisks indicate significance at _p_ = 0.01. **(f)** same data as in (c) but colored by lab. Visual inspection does not show lab clusters. **(g)** Mean activity for each lab, using cells from all regions (color conventions the same as in (f)). Error bands are standard deviation across cells normalised by square root of number of cells in each lab. **(h)** same as (e) but grouping cells per lab. **(i)** p-values of all KS tests without sub-sampling; white squares indicate that there were too few cells for the corresponding region/lab pair. The statistic is the KS distance of the distribution of a target subset of cells’ first PCs to that of the remaining cells. Columns: the region to which the test was restricted and each row is the target lab of the test. Bottom row "all": p-values reflecting a region’s KS distance from all other cells. Rightmost column "all": p-values of testing a lab’s KS distance from all other cells. Small p-values indicate that the target subset of cells can be significantly distinguished from the remaining cells. Note that all region-targeting tests are significant while lab-targeting tests are less so. **(j)** Cellnumber-controlled test results; for the same tests as in **i** the the minimum cell number across compared classes was sampled from the others before the test was computed and p-values combined using Fisher’s method across samplings. Fewer tests are significant after this control. (Figure analyses include collected data that pass our quality metrics and have at least 4 good units in the specified brain region and 3 recordings from the specified lab, to ensure that the data from a lab can be considered representative.) 

**Figure 5–Figure supplement 1** . Lab-grouped average PETH, CDF of the first PC and 2-PC embedding, separate per brain region. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**12 of 89** 

**==> picture [444 x 411] intentionally omitted <==**

**Table 1.** 

Recording Inclusion Guidelines for Optimizing Reproducibility (RIGOR). These criteria could be applied to other electrophysiology experiments (including those using other probes) to enhance reproducibility. We provide code to apply these metrics to any dataset easily (see Code Availability). Note that whole recording metrics are most relevant to large scale (>20 channel) recordings. For those recordings, manual inspection of datasets passing these criteria will further enhance data quality. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**13 of 89** 

reproducibility of our electrophysiological recordings. The responses of 5312 single neurons (all passing the metrics defined in ( **Table 1** ) are analyzed below; this total reflects an average of 105 ± 53 [mean ± std] per insertion. 

We then evaluated whether electrophysiological features of these neurons, such as firing rates and LFP power, were reproducible across laboratories. In other words, is there consistent variation across laboratories in these features that is larger than expected by chance? We first visualized LFP power, a feature used by experimenters to guide the alignment of the probe position to brain regions, for all the repeated site recordings ( **Figure 3b** ). The dentate gyrus (DG) is characterized by high power spectral density of the LFP ( Penttonen et al., 1997 ; Bragin et al., 1995 ; Senzai and Buzsáki, 2017 ) and this feature was used to guide physiology-to-histology alignment of probe positions ( **Figure 3-supplementary 2** ). By plotting the LFP power of all feature aligned recordings along the length of the probe side-by-side, aligned to the boundary between the DG and thalamus, we confirmed that this band of elevated LFP power was visible in all recordings at the same depth. The variability in the extent of the band of elevated LFP power in DG was due to the fact that the DG has variable thickness and due to targeting variability, not every insertion passed through the DG at the same point in the sagittal plane ( **Figure 3-supplemental 2** ). 

The probe alignment allowed us to attribute the channels of each probe to their corresponding brain regions to investigate the reproducibility of electrophysiological features for each of the target regions of the repeated site. To visualize all the neuronal data, each neuron was plotted at the depth it was recorded overlaid with the position of the target brain region locations ( **Figure 3c** ). From these visualizations it is apparent that there is recording-to-recording variability. Several trajectories missed their targets in deeper brain regions (LP, PO), as indicated by gray blocks, despite the lack of significant lab-dependent effects in targeting as reported above. These off-target trajectories tended to have both a large displacement from the target insertion coordinates and a probe angle that unfavorably drew the insertions away from thalamic nuclei ( **Figure 2f** ). These observations raise two questions: (1) Is the recording-to-recording variability within an animal the same or different compared to across animals? (2) Is the recording-torecording variability lab dependent? 

To answer the first question we performed several bilateral recordings in which the same insertion was targeted in both hemispheres, as mirror images of one another. This allowed us to quantify the variability between insertions within the same animal and compare this variability to the across-animal variability ( **Figure 3-supplemental 3** ). We found that whether within- or across-animal variance was larger depended on the electrophysiological feature in question ( **Figure 3-supplemental 3f** ). For example, neuronal yield was highly variable across animals, and less so within animals. By contrast, noise (assessed as action-potential band root mean square, or AP band RMS) was more variable within the same animal than across animals, presumably because probes have noise levels which are relatively stable over time. 

To test whether recording-to-recording variability is lab dependent, we used a permutation testing approach (Methods). The tested features were neuronal yield, firing rate, spike amplitude, LFP power, and AP band RMS. These were calculated in each brain region ( **Figure 3-supplemental 4** ). As was the case when analysing probe placement variability, the permutation test assesses whether the distribution over features varies significantly across labs. When correcting for multiple tests, we were concerned that systematic corrections (such as a full Bonferroni correction over all tests and regions) might be too lenient and could lead us to overlook failures (or at least threats) to reproducibility. We therefore opted to use a more stringent _a_ of 0.01 when establishing significance, and refrained from applying any further corrections (this correction can be thought of as correcting only for the number of regions). The permutation test revealed a significant effect for the spike amplitude in VISa/am. Otherwise, we found that all electrophysiological features were reproducible across laboratories for all regions studied ( **Figure 3d** ). 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

14 of 89 

The permutation testing approach evaluated the reproducibility of each electrophysiological feature separately. It could be the case, however, that some combination of these features varied systematically across laboratories. To test whether this was the case, we trained a Random Forest classifier to predict in which lab a recording was made, based on the electrophysiological markers. The decoding was performed separately for each brain region because of their distinct physiological signatures. A null distribution was generated by shuffling the lab labels and decoding again using the shuffled labels (500 iterations). The significance of the classifier was defined as the fraction of times the accuracy of the decoding of the shuffled labels was higher than the original labels. For validation, we first verified that the decoder could successfully identify brain region (instead of lab identity) from the electrophysiological features; the decoder was able to identify brain region with high accuracy ( **Figure 3e** , left). When decoding lab identity, the classifier had above-chance performance only on the dentate gyrus and not from any of the other regions, indicating that most electrophysiological features were reproducible across laboratories for these regions ( **Figure 3e** , right). 

## **Reproducibility of functional activity depends on brain region and analysis method** 

Concerns about reproducibility extend not only to electrophysiological properties, but also functional properties. To address this, we analyzed the reproducibility of neural activity driven by perceptual decisions about the spatial location of a visual grating stimulus ( The International Brain Laboratory et al., 2021 ). In total, we compared the activity of 4400 neurons across all labs and regions. We focused on whether the targeted brain regions have comparable neural responses to stimuli, movements and rewards. An inspection of individual neurons revealed clear modulation by, for instance, the onset of movement to report a particular choice ( **Figure 4a** ). Despite considerable neuron-to-neuron variability ( **Figure 4b** ), the temporal dynamics of sessionaveraged neural activity were similar across labs in some regions (see VISa/am, CA1 and DG in **Figure 4d** ). Elsewhere, the session-averaged neural response was more variable (see LP and PO in **Figure 4c** and **d** ). 

Having observed that many individual neurons are modulated by task variables during decisionmaking, we examined the reproducibility of the proportion of modulated neurons. Within each brain region, we compared the proportion of neurons that were modulated by stimuli, movements or rewards ( **Figure 4e** ). We used six different comparisons of task-related time windows (using Wilcoxon signed-rank tests and Wilcoxon rank-sum tests, _Steinmetz et al._ ( _2019_ )) to identify neurons with significantly modulated firing rates to different task aspects ( **Figure 4e** , top and **Figure 4-supplemental 1** specify which time windows we compared for which test on each trial; for this, we use _a_ = 0.05; since leftwards versus rightwards choices are not paired we use Wilcoxon rank-sum tests to determine modulation for them). For most individual tests, the proportions of modulated neurons across sessions and across brain regions were quite variable ( **Figure 4e** , bottom and **Figure 4-supplemental 1** ). We also measured the neuronal Fano Factor, which enables the comparison of the fidelity of signals across neurons and regions despite differences in firing rates ( Tolhurst et al., 1983 ). Since the Fano Factor tends to be consistently low around movement time ( Churchland et al., 2010 , _2011_ ), we calculated the average Fano Factor per neuron during 40-200 ms after movement onset (for correct trials with full-contrast right-side stimuli) and quantified differences across labs. 

After determining that our measurements afforded sufficient power to detect differences across labs ( **Figure 4f,g** , **Figure 4-supplemental 2** , see Methods), we evaluated reproducibility of these proportions using permutation tests ( **Figure 4h** ). (Note that we report the reproducibility of the Fano Factor across labs with some caution due to our power analysis results in **Figure 4- supplemental 2** ). Our tests uncovered only one region and period for which there were significant differences across labs ( _a_ = 0.01, corresponding to a Bonferroni correction for the number of regions but not the number of tests, as described above): VISa/am during the stimulus 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

15 of 89 

onset period ( **Figure 4h** , top). In addition to examining the proportion of responsive neurons (a quantity often used to determine that a particular area subserves a particular function), we also compared the full distribution of firing rate modulations. Here, reproducibility was tenuous and failed in thalamic regions for some tests ( **Figure 4h** , bottom). Taken together, these tests uncover that some traditional metrics of neuron modulation are vulnerable to a lack of reproducibility. 

These failures in reproducibility were driven by outlier labs; for instance, for movement-driven activity in PO, UCLA reported an average change of 0 spikes/s, while CCU reported a large and consistent change ( **Figure 4d** , right most panel, compare orange vs. yellow traces). Similarly, the differences in modulation in VISa/am were driven by one lab, in which all four mice had a higher percentage of modulated neurons than mice in other labs ( **Figure 4-supplemental 1a** , purple dots at right). 

Looking closely at the individual sessions and neuronal responses, we were unable to find a simple explanation for these outliers: they were not driven by differences in mouse behavior, wheel kinematics when reporting choices, or spatial position of neurons (examined in detail in the next section). This high variability across individual neurons meant that differences that are clear in across-lab aggregate data can be unclear within a single lab. For instance, a difference between the proportion of neurons modulated by movement initiation vs. left/right choices is clear in the aggregate data (compare panels d and f in **Figure 4-supplemental 1** ), but much less clear in the data from any single lab (e.g., compare values for individual labs in panels d vs. f of **Figure 4- supplemental 1** ). This is an example of a finding that might fail to reproduce across individual labs, and underscores that single-neuron analyses are susceptible to lack of reproducibility, in part due to the high variability of single neuron responses. Very large sample sizes of neurons could serve to mitigate this problem. We anticipate that the feasibility of even larger scale recordings will make lab-to-lab comparisons easier in future experiments; multi-shank probes could be especially beneficial for cortical recordings, which tend to be the most vulnerable to low cell counts since the cortex is thin and is the most superficial structure in the brain and thus the most vulnerable to damage. Analyses that characterize responses to multiple parameters are another possible solution (See **Figure 7** ). 

Having discovered vulnerabilities in the reproducibility of standard single-neuron tests, we tested reproducibility using an alternative approach: comparing low-dimensional summaries of activity across labs and regions. To start, we summarized the response for each neuron by computing perievent time histograms (PETHs, **Figure 5a** ). Because temporal dynamics may depend on reaction time, we generated separate PETHs for fast ( _<_ 0.15 s) and slow ( _>_ 0.15 s) reaction times (0.15 s was the mean reaction time when considering the distribution of reaction times across all sessions). We concatenated the resulting vectors to obtain a more thorough summary of each cell’s average activity during decision-making. The results (below) did not depend strongly on the details of the trial-splitting; for example, splitting trials by “left" vs “right" behavioral choice led to similar results. We further tried a stimulus-aligned pre-movement window, which resulted in many fewer responding cells, although no substantially different test results, not shown here. 

Next, we projected these high-dimensional summary vectors into a low-dimensional “embedding" space using principal component analysis (PCA). This embedding captures the variability of the population while still allowing for easy visualization and further analysis. Specifically, we stack each cell’s summary double-PETH vector (described above) into a matrix (containing the summary vectors for all cells across all sessions) and run PCA to obtain a low-rank approximation of this matrix (see Methods). The accuracy of reconstructions from the top two principal components (PCs) varied across cells ( **Figure 5a** ); PETHs for the majority of cells could be well-reconstructed with just 2 PCs ( **Figure 5b** ). 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

16 of 89 

This simple embedding exposes differences in brain regions ( **Figure 5c** ; e.g., PO and DG are segregated in the embedding space), verifying that the approach is sufficiently powerful to detect expected regional differences in response dynamics. Region-to-region differences are also visible in the region-averaged PETHs and cumulative distributions of the first PCs ( **Figure 5d, e** ). By contrast, differences are less obvious when coloring the same embedded activity by labs ( **Figure 5f, g, h** ), however some labs, such as CCU and CSHL(Z) are somewhat segregated. In comparison to regions, the activity point clouds overlap somewhat more homogeneously across most labs ( **Figure 5-supplemental 1** for scatter plots, PETHs, cumulative distributions for each region separately, colored by lab). 

We quantified this observation via two tests. First, we applied a permutation test using the first 2 PCs of all cells, computing each region’s 2D distance between its mean embedded activity and the mean across all remaining regions, then comparing these values to the null distribution of values obtained in an identical manner after shuffling the region labels. Second, we directly compared the distributions of the first PCs, applying the Kolmorogov-Smirnov (KS) test to determine whether the distribution of a subset of cells was different from that of all remaining cells, targeting either labs or regions. The KS test results were nearly identical to the 2D distance permutation test results, hence we report only the KS test results below. 

This analysis confirmed that the neural activity in each region differs significantly (as defined above, _a_ = 0.01, Bonferroni correction for the number of regions but not the number of tests) from the neural activity measured in the other regions ( **Figure 5i** , bottom row), demonstrating that neural dynamics differ from region-to-region, as expected and as suggested by **Figure 5c-e** . We also found that the neural activity from 7/10 labs differed significantly from the neural activity of all remaining labs when considering all neurons ( **Figure 5i** , right column). When restricting this test to single regions, significant differences were observed for 6/40 lab-region pairs ( **Figure 5i** , purple squares in the left columns). Note that in panels i,j of **Figure 5** , the row "all" indicates that all cells were used when testing if a region had a different distribution of first PCs than the remaining regions and analogously the column "all" for lab-targeted tests. We further repeated these tests after controlling for varying cell numbers, by sampling the minimum cell number across compared classes and combining p-values across these samplings using Fisher’s method, which resulted in overall fewer significant differences ( **Figure 5j** ). Overall, these observations are in keeping with **Figure 4** and suggest, as above, that outlier responses during decisionmaking can be present despite careful standardization ( **Figure 5i** ). 

## **The spatial position within regions and spike waveforms of neurons explain minimal firing rate vari-ability** 

In addition to lab-to-lab variability, which was low for electrophysiological features and higher for functional modulation during decision-making ( **Figures 4** , **5** ), we observed considerable variability between recording sessions and mice. Here, we examined whether this variability could be explained by either the within-region location of the Neuropixels probe or the single-unit spike waveform characteristics of the sampled neurons. 

To investigate variability in session-averaged firing rates, we identified neurons that had firing rates different from the majority of neurons within each region (absolute deviation from the median firing rate being >15% of the firing rate range). These outlier neurons, which all turned out to be high-firing, were compared against the general population of neurons in terms of five features: spatial position (x, y, z, computed as the center-of-mass of each unit’s spike template on the probe, localized to CCF coordinates in the histology pipeline) and spike waveform characteristics (amplitude, peak-to-trough duration). We observed that recordings in all areas, such as LP ( **Figure 6a** ), indeed spanned a wide space within those areas. Interestingly, in areas other than DG, the highest firing neurons were not entirely uniformly distributed in space. For instance, in LP, high firing neurons tended to be positioned more laterally and centered on the 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

17 of 89 

anterior-posterior axis ( **Figure 6b** ). In VISa/am and CA1, only the spatial position of neurons, but not differences in spike characteristics, contributed to differences in session-averaged firing rates ( **Figure 6-supplemental 1b** and **2b** ). In contrast, high-firing neurons in LP, PO, and DG had different spike characteristics compared to other neurons in their respective regions ( **Figures 6b** and **6-supplemental 3a,c** ). It does not appear that high-firing neurons in any brain region belong clearly to a specific neuronal subtype (see **Figure 6-supplemental 5** ). 

To quantify variability in session-averaged firing rates of individual neurons that can be explained by spatial position or spike characteristics, we fit a linear regression model with these five features (x, y, z, spike amplitude, and duration of each neuron) as the inputs. For each brain region, features that had significant weights were mostly consistent with the results reported above: In VISa/am and CA1, spatial position explained part of the variance; in DG, the variance could not be explained by either spatial position or spike characteristics; in LP and PO, both spatial position and spike amplitudes explained some of the variance. In LP and PO, where the most amount of variability could be explained by this regression model (having higher _R_[2] values), these five ∼ features still only accounted for a total of 5% of the firing rate variability. In VISa/am, CA1, and DG, they accounted for approximately 2%, 4%, and 2% of the variability, respectively. 

Next, we examined whether neuronal spatial position and spike features contributed to variability in task-modulated activity. We found that brain regions other than DG had minor, yet significant, differences in spatial positions of task-modulated and non-modulated neurons (using the definition of at least of one of the six time-period comparisons in **Figure 4e** and **Figure 4- supplemental 1** ). For instance, LP neurons modulated according to the movement initiation test and the left versus right movement test tended to be more ventral ( **Figure 6c-d** ). Other brain regions had weaker spatial differences than LP ( **Figure 6-supplemental 1** , **2** , **3** ). Spike characteristics were significantly different between task-modulated and non-modulated neurons only for one modulation test in LP ( **Figure 6d** ) and two tests in DG, but not in other brain regions. On the other hand, the task-aligned Fano Factors of neurons did not have any differences in spatial position except for in VISa/am, where lower Fano Factors (<1) tended to be located ventrally ( **Figure 6-supplemental 4** ). Spike characteristics of neurons with lower vs. higher Fano Factors were only slightly different in VISa/am, CA1, and PO. Lastly, we trained a linear regression model to predict the 2D embedding of PETHs of each cell shown in **Figure 5c** from the x, y, z coordinates and found that spatial position contains little information ( _R_[2] ∼ 5%) about the embedded PETHs of cells. 

In summary, our results suggest that neither spatial position within a region nor waveform characteristics account for very much variability in neural activity. We examine other sources of variability below (see section, A multi-task neural network accurately predicts activity and quantifies sources of neural variability). 

## **Single neuron coefficients from a regression-** 

## **based analysis are reproducible across labs** 

Neural encoding models provide a natural way to quantify the impact of many variables on single neuron activity, and to test whether the resulting profiles are reproducible across labs or brain regions. We first estimated single-neuron response profiles using standard linear regression models. Second, we evaluated reproducibility by decoding either lab identity or brain region from the response profiles of each neuron 

We used a Reduced-Rank Regression (RRR) encoding model to predict the single neuron activity as a function of the experimental conditions and the subject’s behavior. Our approach follows a previous application of the RRR model to cortical neurons in the IBL Brainwide Map dataset ( Posani et al., 2024 ). Specifically, the input variables we used for fitting the model range from cognitive (left vs. right block), sensory (stimulus side, contrast), motor (wheel velocity, whisker 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

18 of 89 

**==> picture [350 x 345] intentionally omitted <==**

**Figure 6.** 

## **High-firing and task-modulated LP neurons have slightly different spatial positions and spike waveform features than other LP neurons, possibly contributing only marginally to variability between sessions.** 

**(a)** Spatial positions of recorded neurons in LP. Colors: session-averaged firing rates on a log scale. To enable visualization of overlapping data points, small jitter was added to the unit locations. **(b)** Spatial positions of LP neurons plotted as distance from the planned target center of mass, indicated with the black x. Colors: session-averaged firing rates on a log scale. Larger circles: outlier neurons (above the firing rate threshold of 13.5 sp/s shown on the colorbar). In LP, 114 out of 1337 neurons were outliers. Only histograms of the spatial positions and spike waveform features that were significantly different between the outlier neurons (yellow) and the general population of neurons (blue) are shown (two-sample Kolmogorov-Smirnov test with Bonferroni correction for multiple comparisons; * and ** indicate corrected p-values of <0.05 and <0.01). Shaded areas: the area between 20th and 80th percentiles of the neurons’ locations. **(c)** (Left) Histogram of firing rate changes during movement initiation ( **Figure 4e** , **Figure 4-supplemental 1d** ) for task-modulated (orange) and non-modulated (gray) neurons. 697 out of 1337 LP neurons were modulated during movement initiation. (Right) Spatial positions of task-modulated and non-modulated LP neurons, with histograms of significant features (here, z position) shown. **(d)** Same as (c) but using the left vs. right movement test ( **Figure 4e** and **Figure 4-supplemental 1f** ) to identify task-modulated units; histogram is bimodal because both left- and right-preferring neurons are included.292 out of 1337 LP neurons were modulated differently for leftward vs. rightward movements. (Figure analyses include all collected data that pass our quality metrics, regardless of the number of recordings per lab or number of repeated site brain areas that the probes pass through.) **Figure 6–Figure supplement 1** . High-firing and task-modulated VISa/am neurons. **Figure 6–Figure supplement 2** . High-firing and task-modulated CA1 neurons. **Figure 6–Figure supplement 3** . High-firing and task-modulated DG and PO neurons. **Figure 6–Figure supplement 4** . Time-course and spatial position of neuronal Fano Factors. **Figure 6–Figure supplement 5** . Neuronal subtypes and firing rates. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**19 of 89** 

motion energy, lick), to decision-related (choice, outcome). The goal of the model is to relate these variables to the measured neural activity (aligned to stimulus onset, smoothed, and normalized). After fitting the RRR model to predict trial-by-trial activity, each neuron is summarized by a single 32-dimensional coefficient vector. 

Using these 32-dimensional vectors, we then attempted to decode the region or lab identity associated with the neurons. We used 69 sessions from the dataset presented here. Neurons from the regions VISa, DG, PO, CA1, LP, passing the quality control (RIGOR), and with sufficient goodness-of-fit (cross-validated _R_[2] ≥ 0.03) were included in the decoding analysis. There were 1767 responsive neurons in total. We used the support vector classification (SVC) for the multi-class classification and the macro-averaged F1 score to assess the goodness of decoding. Additionally, we conducted a permutation test (Methods and Materials, N_permute = 1000) to determine whether the macro-averaged F1 score obtained from the data was significantly higher than chance level. 

We found that the region identity was more decodable than the lab identity. The macro-averaged F1 score for the region decoding was 0.35 (p<0.0001, **Figure 7a** ), while for lab decoding, it was only 0.14 (p=0.325, **Figure 7b** ). To ensure that the unequal distribution of recorded regions did not cause us to mis-estimate the lab decoding performance, we applied the same lab decoding analysis to each region separately. The results are close to chance level for all the regions (p=0.166, 0.048, 0.147, 0.124 0.599 for VISa, CA1, DG, LP, and PO respectively, **Figure 7c** ). The results align with our visual inspection using linear discriminant analysis ( **Figure 7** , bottom row), where region-to-region differences are more visible than lab-to-lab differences. In summary, the identity of the brain region is significantly decodable from the single-neuron response profiles, while the identity of the laboratory is not. This speaks to the reproducibility of single neuron metrics across labs, and provides reassurance that when a neuron’s full response profile is considered (instead of its selectivity for just one variable as in **Figure 4** ), results are more robust. 

## **A multi-task neural network accurately predicts activity and quantifies sources of neural variability** 

As discussed above, variability in neural activity between labs or between sessions can be due to many factors. These include differences in behavior between animals, differences in probe placement between sessions, and uncontrolled differences in experimental setups between labs. Simple linear regression models or generalized linear models (GLMs) may be too inflexible to capture the nonlinear contributions that many of these variables, including lab identity and spatial positions of neurons, might make to neural activity. On the other hand, fitting a different nonlinear regression model (involving many covariates) individually to each recorded neuron would be computationally expensive and could lead to poor predictive performance due to overfitting. 

To estimate a flexible nonlinear model given constraints on available data and computation time, we adapt an approach that has proven useful in the context of sensory neuroscience ( McIntosh et al., 2016 ; Batty et al., 2016 ; Cadena et al., 2019 ). We use a “multi-task" neural network (MTNN; **Figure 8a** ) that takes as input a set of covariates (including the lab ID, the neuron’s 3D spatial position in standardized CCF coordinates, the animal’s estimated pose extracted from behavioral video monitoring, feedback times, and others; see **Table 2** for a full list). The model learns a set of nonlinear features (shared over all recorded neurons) and fits a Poisson regression model on this shared feature space for each neuron. With this approach we effectively solve multiple nonlinear regression tasks simultaneously; hence the “multi-task" nomenclature. The model extends simpler regression approaches by allowing nonlinear interactions between covariates. In particular, previous reduced-rank regression approaches ( Izenman, 1975 ; Kobak 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

20 of 89 

**==> picture [444 x 194] intentionally omitted <==**

## **Figure 7.** 

## **Brain region, but not lab identity is decodable from single-neuron response profiles.** 

Results of decoding analysis for different scenarios: (a) brain region decoding using all neurons, (b) lab decoding using all neurons, and (c) lab decoding using neurons from specific brain regions. The histogram shows the distribution of macroaveraged F1 for perturbed null datasets. The null distribution is compared to the macro-averaged F1 of the original dataset (indicated by the dashed red line). The scatter plot shows the cross-validated 2-dimensional linear discriminant analysis (LDA) projection. Neurons are randomly and evenly split into two groups: one for training the LDA model and the other for testing. The plots are generated exclusively using the test set. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**21 of 89** 

et al., 2016 ; Steinmetz et al., 2019 ; Posani et al., 2024 ), including the analysis presented here 

( **Figure 7** ), can be seen as a special case of the multi-task neural network, with a single hidden layer and no nonlinearity between layers. 

**==> picture [471 x 576] intentionally omitted <==**

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

22 of 89 

## **Figure 8.** 

## **Single-covariate, leave-one-out, and leave-group-out analyses show the contribution of each (group of) covariate(s) to the MTNN model. Lab and session IDs have low contributions to the model.** 

**(a)** We adapt a MTNN approach for neuron-specific firing rate prediction. The model takes in a set of covariates and outputs time-varying firing rates for each neuron for each trial. See **Table 2** for a full list of covariates. **(b)** MTNN model estimates of firing rates (50 ms bin size) of a neuron in VISa/am from an example subject during held-out test trials. The trials with stimulus on the left are shown and are aligned to the first movement onset time (vertical dashed lines). We plot the observed and predicted PETHs and raster plots. The blue ticks in the raster plots indicate stimulus onset, and the green ticks indicate feedback times. The trials above (below) the black horizontal dashed line are incorrect (correct) trials, and the trials are ordered by reaction time. The trained model does well in predicting the (normalized) firing rates. The MTNN prediction quality measured in _R_[2] is 0.45 on held-out test trials and 0.94 on PETHs of held-out test trials. **(c)** We plot the MTNN firing rate predictions along with the raster plots of behavioral covariates, ordering the trials in the same manner as in (b). We see that the MTNN firing rate predictions are modulated synchronously with several behavioral covariates, such as wheel velocity and paw speed. **(d)** Singlecovariate analysis, colored by the brain region. Each dot corresponds to a single neuron in each plot. **(e)** Leave-oneout and leave-group-out analyses, colored by the brain region. The analyses are run on 1133 responsive neurons across 32 sessions. The leave-one-out analysis shows that lab/session IDs have low effect sizes on average, indicating that within and between-lab random effects are small and comparable. The “noise" covariate is a dynamic covariate (white noise randomly sampled from a Gaussian distribution) and is included as a negative control: the model correctly assigns zero effect size to this covariate. Covariates that are constant across trials (e.g., lab and session IDs, neuron’s 3D spatial location) are left out from the single-covariate analysis. 

**Figure 8–Figure supplement 1** . MTNN prediction quality; MTNN slightly outperforms GLMs on predicting the firing rates of held-out test trials; PETHs and MTNN predictions for held-out test trials 

**Figure 8–Figure supplement 2** . MTNN prediction quality on the data simulated from GLMs is comparable to the GLMs’ prediction quality. The effect sizes computed by the MTNN leave-one-out analysis are similar to the effect sizes computed by the GLMs’ leave-one-out analysis 

**Figure 8–Figure supplement 3** . Lab IDs have a negligible effect on the MTNN prediction. MTNN leave-one-out analysis captures artificially inflated lab ID effects. 

**Figure 8–Figure supplement 4** . MTNN single-covariate effect sizes are highly correlated across sessions and labs. 

**Figure 8b** shows model predictions on held-out trials for a single neuron in VISa/am. We plot the observed and predicted peri-event time histograms and raster plots for left trials. As a visual overview of which behavioral covariates are correlated with the MTNN prediction of this neuron’s activity on each trial, the predicted raster plot and various behavioral covariates that are input into the MTNN are shown in **Figure 8c** . Overall, the MTNN approach accurately predicts the observed firing rates. When the MTNN and GLMs are trained on movement, task-related, and prior covariates, the MTNN slightly outperforms the GLMs on predicting the firing rate of held-out test trials (See **Figure 8-supplemental 1b** ). On the other hand, as shown in _Posani et al._ ( _2024_ ), reduced-rank regression models can achieve similar predictive performance as the MTNN. 

Next we use the predictive model performance to quantify the contribution of each covariate to the fraction of variance explained by the model. Following _Musall et al._ ( _2019_ ) , we run two complementary analyses to quantify these effect sizes: _single-covariate fits_ , in which we fit the model using just one of the covariates, and _leave-one-out fits_ , in which we train the model with one of the covariates left out and compare the predictive explained to that of the full model. As an 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

23 of 89 

**==> picture [398 x 340] intentionally omitted <==**

**Table 2.** 

## **List of covariates input to the multi-task neural network.** 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**24 of 89** 

extension of the leave-one-out analysis, we run the _leave-group-out analysis_ , in which we quantify the contribution of each group of covariates (electrophysiological, task-related, and movement) to the model performance. Using data simulated from GLMs, we first validate that the MTNN leaveone-out analysis is able to partition and explain different sources of neural variability (See **Figure 8-supplemental 2** ). 

We then run single-covariate, leave-one-out, and leave-group-out analyses to quantify the contributions of the covariates listed in **Table 2** to the predictive performance of the model on held-out test trials. The results are summarized in **Figure 8d** and **8e** , with a simulated positive control analysis in **Figure 8-supplemental 3** . According to the single-covariate analysis ( **Figure 8d** ), face motion energy (derived from behavioral video), paw speed, wheel velocity, and first movement onset timing can individually explain about 5% of variance of the neurons on average, and these single-covariate effect sizes are highly correlated ( **Figure 8-supplemental 4** ). The leave-one-out analysis ( **Figure 8e** left) shows that most covariates have low unique contribution to the predictive power. This is because many covariates are correlated and are capable of capturing variance in the neural activity even if one of the covariates is dropped (See behavioral raster plots in **Figure 8c** ). According to the leave-group-out analysis ( **Figure 8e** right), the “movement" covariates as a group have the highest unique contribution to the model’s performance while the task-related and electrophysiological variables have close-to-zero unique contribution. Most importantly, the leave-one-out analysis shows that lab and session IDs, conditioning on the covariates listed in **Table 2** , have close to zero effect sizes, indicating that within-lab and between-lab random effects are small and comparable. 

## **Decodability of task variables is consistent across labs, but varies by brain region** 

The previous sections addressed whether task modulation of neural activity is consistent across labs from an encoding perspective. In this section, we explored the consistency in population-level representation of task variables across labs from a decoding perspective. The analysis consists of two parts: first, we decoded selected task variables—choice, stimulus side, reward, and wheel speed—using population activity from five brain regions (PO, LP, DG, CA1, and VISa/am) across individual probe insertions. Second, we conducted statistical tests to determine whether the decodability of task variables is comparable across labs. 

We used the multi-animal, across-region reduced-rank decoder introduced in _Zhang et al._ ( _2024_ ) . We performed 5-fold cross-validation and adjusted for chance-level decoding scores for each task variable. For choice, stimulus side, and reward, we calculated chance-level accuracy by decoding based on the majority class in the training data and then subtracting this from the observed accuracy. For wheel speed, we report the single-trial _R_[2] , which measures prediction quality by first calculating the trial-average behavior across choice, stimulus side, and reward conditions, and then subtracting these averages from the observed behavior. This approach adjusts for chancelevel decoding by implicitly assuming that the condition-specific trial averages can serve as the chance-level prediction. 

Given the decoding scores over chance level, we performed statistical tests to assess the consistency of task variable decodability across labs and regions. To assess whether there are significant differences in mean decoding scores across different labs, we performed a one-way ANOVA test ( **Figure 9a** ); the adjusted significance level is 0.01 after multiple-comparison correction. No statistically significant differences in decoding scores were apparent for any region or variable. This suggests that the decodability of task variables from populations is generally comparable across different labs. We then evaluated task-specific decoding performance categorized by region and lab, accounting for the number of neurons ( **Figure 9b** ). No clustering of decoding scores based on lab identities was apparent. We then performed a quantitative test by decoding lab and region identity using both decoding scores and the number of units as 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

25 of 89 

covariates. We conducted a permutation test with 5000 permutations and used a support vector classifier (again with an adjusted significance level of 0.01 after multiple-comparison correction). We could accurately determine region identity based on decoding scores and unit counts, as evidenced by macro F1 scores that exceed chance levels and significant p-values. In contrast, lab identity is less decodable than region identity, with F1 scores near chance. This implies that, after accounting for the number of neurons, the decodability of task variables from populations remains comparable across different labs. 

## **Discussion** 

We set out to test whether the results from an electrophysiology experiment could be reproduced across 10 geographically separated laboratories. We observed notable variability in the position of the electrodes in the brain despite efforts to target the same location ( **Figure 2** ). Fortunately, after applying stringent quality-control criteria (including the RIGOR standards, **Table 1** ), we found that electrophysiological features such as neuronal yield, firing rate, and LFP power were reproducible across laboratories ( **Figure 3d** ). The proportion of neurons with responses that were modulated, and the ways in which they were modulated by individual, behaviorally-relevant task events was more variable: lab-to-lab differences were evident in some regions ( **Figures 4** , **5** ) and these were not explainable by, for instance, systematic variation in the subregions that were targeted ( **Figure 6** ). Reassuringly, analyses that summarized each neuron’s activity by a compact vector of features were more robust ( **Figure 7** ). Further, when we trained a multi-task neural network to predict neural activity, lab identity accounted for little neural variance ( **Figure 8** ), arguing that the lab-to-lab differences we observed are driven by outlier neurons/sessions and nonlinear interactions between variables, rather than, for instance, systematic biases. This is reassuring, but points to the need for appropriate analytical choices to ensure reproducibility. Altogether, our results suggest that standardization and quality control metrics can enhance reproducibility, and that caution should be taken with regard to electrode placement and the interpretation of some standard single-neuron metrics. 

The absence of systematic differences across labs for some metrics argues that standardization of procedures is a helpful step in generating reproducible results. Our experimental design precludes an analysis of whether the reproducibility we observed was driven by person-to-person standardization or lab-to-lab standardization. Most likely, both factors contributed: all lab personnel received standardized instructions for how to implant head bars and train animals, which likely reduced personnel-driven differences. In addition, our use of standardized instrumentation and software minimized lab-to-lab differences that might normally be present. Another significant limitation of the analysis presented here is that we have not been able to assess the extent to which other choices of quality metrics and inclusion criteria might have led to greater or lesser reproducibility. 

Reproducibility in our electrophysiology studies was further enhanced by rigorous quality control metrics that ultimately led us to exclude a significant fraction of datasets (retaining 82 / 121 experimental sessions). Quality control was enforced for diverse aspects of the experiments, including histology, behavior, targeting, neuronal yield, and the total number of completed sessions. A number of recordings with high noise and/or low neuronal yield were excluded. Exclusions were driven by artifacts present in the recordings, inadequate grounding, and a decline in craniotomy health; all of these can potentially be improved with experimenter experience (a metric that could be systematically examined in future work). A few quality control metrics were specific to our experiments (and thus not listed in **Table 1** ). For instance, we excluded sessions with fewer than 400 trials, which could be too stringent (or not stringent enough) for other experiments. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

26 of 89 

**==> picture [398 x 416] intentionally omitted <==**

**Figure 9.** 

## **The decodability of task variables from the population is consistent across labs, but varies by brain region.** 

**(a)** Task-specific decoding performance per region with per session results. The decoding scores over chance level for choice, stimulus side, and reward represent decoding accuracy, while the score for wheel speed is measured in _R_[2] units. Each dot indicates the decoding performance for a single insertion, color-coded by lab identity. A one-way ANOVA is conducted to determine if there are significant differences in mean decoding scores across labs. The F-statistic and p-value are reported. After multi-comparison correction, the reported p-values reveal no statistically significant differences in decoding scores across labs. **(b)** The scatter plot shows the decoding score over chance level plotted against the number of neurons used. Each dot represents a single insertion, color-coded by the region (top) and lab (bottom) identity. The scores for choice, stimulus side, and reward represent decoding accuracy, while the score for wheel speed is measured in _R_[2] units. We conduct a quantitative test of the decodability of lab and region identity using decoding scores and the number of units as covariates. A support vector classifier is used, and a permutation test with 5000 permutations is applied. We report the macro F1 scores and p-values from the permutation test. After multiple-comparison correction, lab identity is less decodable than region identity, and its observed decodability may occur by chance. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**27 of 89** 

These observations suggest that future experiments would be more consistently reproducible if researchers followed, or at least reported, a number of agreed upon criteria, such as the RIGOR standards we define in **Table 1** . This approach has been successful in other fields: for instance, the neuroimaging field has agreed upon a set of guidelines for “best practices", and has identified factors that can impede those practices ( Nichols et al., 2017 ). The genomics field likewise adopted the Minimum Information about a Microarray Experiment (MIAME) standard, designed to ensure that data from microarrays could be meaningfully interpreted and experimentally verified ( Brazma et al., 2001 ). The autophagy community has a similar set of guidelines for experiments ( Klionsky, 2016 ). Our work here suggests the creation of a similar set of standards for electrophysiology and behavioral experiments would be beneficial, at least on an “opt in" basis: for instance, manuscript authors, especially those new to electrophysiology, could state which of the metrics were adhered to, and which were not needed. The metrics might also serve as the starting point for training students how to impose inclusion criteria for electrophysiological studies. Importantly, the use of RIGOR need not prevent flexibility: studies focusing on multi-unit activity would naturally omit single unit metrics, and studies on other animals or contexts would understandably need to adjust some metrics. We provide code to easily run RIGOR metrics on users’ external datasets, which we hope will encourage this practice. 

Establishment of such standards has the potential to enhance lab-to-lab reproducibility, but experiment-to-experiment variability may not be entirely eliminated. A large-scale effort to enhance reproducibility in _C. elegans_ aging studies successfully replicated average lifespan curves across 3 labs by standardizing experimental methods such as handling of organisms and notation of age (e.g. when egg is hatched vs laid) ( Lithgow et al., 2017 ; Lucanic et al., 2017 ). Still, variability in the lifespan curves of individual worms nevertheless persisted, warranting further studies to understand what molecular differences might explain this. Similarly, we observed no systematic difference across labs in some electrophysiological measures such as LFP power ( **Fig 3d** ) or functional responses in some regions but found considerable variability across experiments in other regions ( **Figure 4h** , **Figure 5i** ). 

We found probe targeting to be a large source of variability. Our ability to detect targeting error benefited from an automated histological pipeline combined with alignment and tracing that required agreement between multiple users, an approach that greatly exceeds the histological analyses done by most individual labs. Our approach, which enables scalability and standardization across labs while minimizing subjective variability, revealed that much of the variance in targeting was due to the probe entry positions at the brain surface, which were randomly displaced across the dataset. The source of this variance could be due to a discrepancy in skull landmarks compared to the underlying brain anatomy. Accuracy in placing probes along a planned trajectory is therefore limited by this variability (about 400µm). Probe angle also showed a small degree of variance and a bias in both anterior-posterior and medio-lateral direction, indicating that the Allen Common Coordinate Framework (CCF) ( Wang et al., 2020 ) and stereotaxic coordinate systems are slightly offset. Detecting this offset relied on a large cohort size and an automated histological pipeline, but now that we have identified the offset, it can be easily accounted for by any lab. Specifically, probe angles must be carefully computed from the CCF, as the CCF and stereotaxic coordinate systems do not define the same coronal plane angle. Minimizing variance in probe targeting is another important element in increasing reproducibility, as slight deviations in probe entry position and angle can lead to samples from different populations of neurons. Collecting structural MRI data in advance of implantation ( Browning et al., 2023 ) could reduce targeting error, although this is infeasible for most labs. A more feasible solution is to rely on stereotaxic coordinates but account for the inevitable off-target measurements by increasing cohort sizes and adjusting probe angles when blood vessels obscure the desired location. This is essential because small differences in probe location may be responsible for other studies arriving at different conclusions, highlighting the need for agreed upon methods for targeting specific areas ( Rajasethupathy et al., 2015 ; Andrianova et al., 2022 ). 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

28 of 89 

Our results also highlight the critical importance of reproducible histological processing and subsequent probe alignment. Specifically, we used a centralized histology and registration pipeline to assign each recording site on each probe to a particular anatomical location, based on registration of the histological probe trajectories to the CCF and the electrophysiological features recorded at each site. This differs from previous approaches, in which stereotaxic coordinates alone were used to target an area of interest and exclusion criteria were not specified; see e.g. ( Harvey et al., 2012 ; Raposo et al., 2014 ; Erlich et al., 2015 ; Goard et al., 2016 ; Najafi et al., 2020 ). The reliance on stereotaxic coordinates for localization, instead of standardized histological registration, is a possible explanation for conflicting results across laboratories in previous literature. Our results speak to the importance of adopting standardized procedures more broadly across laboratories. Notably, centralizing the histology pipeline likely reduces variance, but the extent of additional variability introduced by individual lab implementations remains unclear. 

A major contribution of our work is open-source data and code: we share our full dataset (see Data Availability) and suite of analysis tools for quantifying reproducibility (see Code Availability) and computing the RIGOR standards. The analyses here required significant improvements in data architecture, visualization, spike sorting, histology image analysis, and video analysis. Our analyses uncovered major gaps and issues in the existing toolsets that required improvements (see Methods and _The International Brain Laboratory et al._ ( _2022b_ ,a) for full details). For example, we improved existing spike sorting pipelines with regard to scalability, reproducibility, and stability. These improvements contribute towards advancing automated spike sorting, and move beyond subjective manual curation, which scales poorly and limits reproducibility. We anticipate that our open-source dataset will play an important role in further improvements to these pipelines and also the development of further methods for modeling the spike trains of many simultaneously recorded neurons across multiple brain areas and experimental sessions. 

Scientific advances rely on the reproducibility of experimental findings. The current study demonstrates that reproducibility is attainable for many features measured during a standardized perceptual decision task. We offer several recommendations to enhance reproducibility, including (1) standardized protocols for data collection and processing, (2) methods to account for variability in electrode targeting and (3) rigorous data quality metrics, such as RIGOR. These recommendations are urgently needed as neuroscience continues to move towards increasingly large and complex datasets. 

## **Resources** 

## **Data availability** 

All data are freely available. Please visit _https://int-brain-lab.github.io/iblenv/notebooks_external/data _release_repro_ephys_ . html to access the data used in this article. Please visit the visualisation website _https://viz.internationalbrainlab.org/app_ to view the data (use the tab _Repeated sites_ ). 

## **Code availability** 

All code is freely available. Please visit _https://github.com/int-brain-lab/paper-reproducible-ephys/_ to access the code used to produce the results and figures presented in this article. The RIGOR metrics can be computed on external datasets by following the tutorial at _https://github.com/intbrain-lab/paper-reproducible-ephys/blob/master/RIGOR_script.ipynb_ . 

## **Protocols and pipelines** 

Please visit _https://figshare.com/projects/Reproducible_Electrophysiology/138367_ to access the protocols and pipelines used in this article. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

29 of 89 

## **Quality control and data inclusion** 

Please see this spreadsheet for a comprehensive overview of which recordings and the number of cells, mice and sessions that are used in each figure panel, as well as the reasons for inclusion or exclusion. 

## **Methods and Materials** 

All procedures and experiments were carried out in accordance with local laws and following approval by the relevant institutions: the Animal Welfare Ethical Review Body of University College London; the Institutional Animal Care and Use Committees of Cold Spring Harbor Laboratory, Princeton University, University of California at Los Angeles, and University of California at Berkeley; the University Animal Welfare Committee of New York University; and the Portuguese Veterinary General Board. 

## **Animals** 

Mice were housed under a 12/12 h light/dark cycle (normal or inverted depending on the laboratory) with food and water available ad libitum, except during behavioural training days. Electrophysiological recordings and behavioural training were performed during either the dark or light phase of the cycle depending on the laboratory. N=78 adult mice (C57BL/6, male and female, obtained from either Jackson Laboratory or Charles River) were used in this study. Mice were aged 111 - 442 days and weighed 16.4-34.5 g on the day of their first electrophysiology recording session in the repeated site. 

## **Materials and apparatus** 

Briefly, each lab installed a standardized electrophysiological rig (named ‘ephys rig’ throughout this text), which differed slightly from the apparatus used during behavioral training ( The International Brain Laboratory et al., 2021 ). The general structure of the rig was constructed from Thorlabs parts and was placed inside a custom acoustical cabinet clamped on an air table (Newport, M-VIS3036-SG2-325A). A static head bar fixation clamp and a 3D-printed mouse holder were used to hold a mouse such that its forepaws rest on the steering wheel (86652 and 32019, LEGO) ( The International Brain Laboratory et al., 2021 ). Silicone tubing controlled by a pinch valve (225P011-21, NResearch) was used to deliver water rewards to the mouse. The display of the visual stimuli occurred on a LCD screen (LP097Q × 1, LG). To measure the precise times of changes in the visual stimulus, a patch of pixels on the LCD screen flipped between white and black at every stimulus change, and this flip was captured with a photodiode (Bpod Frame2TTL, Sanworks). Ambient temperature, humidity, and barometric air pressure were measured with the Bpod Ambient module (Sanworks), wheel position was monitored with a rotary encoder (05.2400.1122.1024, Kubler). 

Videos of the mouse were recorded from 3 angles (left, right and body) with USB cameras (CM3U3-13Y3M-CS, Point Grey). The left camera acquires at 60Hz; full resolution (1280 x1024), right camera at 150Hz; half resolution (640x512), and body camera at 30Hz; half resolution (640Hzx512). A custom speaker (Hardware Team of the Champalimaud Foundation for the Unknown, V1.1) was used to play task-related sounds, and an ultrasonic microphone (Ultramic UM200K, Dodotronic) was used to record ambient noise from the rig. All task-related data was coordinated by a Bpod State Machine (Sanworks). The task logic was programmed in Python and the visual stimulus presentation and video capture were handled by Bonsai ( Lopes et al., 2015 ) utilizing the Bonsai package BonVision ( Lopes et al., 2021 ). 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

30 of 89 

All recordings were made using Neuropixels probes (Imec, 3A and 3B models), advanced in the brain using a micromanipulator (Sensapex, uMp-4) tilted by a 15 degree angle from the vertical line. The aimed electrode penetration depth was 4.0 mm. Data were acquired via an FPGA (for 3A probes) or PXI (for 3B probes, National Instrument) system and stored on a PC. 

## **Headbar implant surgery** 

Mice were placed in an induction box with 3-4% isoflurane and maintained at 1.5-2% isoflurane. Saline 10mg/kg subcutaneously is given each hour. The mouse is placed in the stereotaxic frame using ear bars placed in the ridge posterior to the ear canal. The mouse is then prepped for surgery, removing hair from the scalp using epilation creme. Much of the underlying periosteum was removed and bregma and lambda were marked. Then the head was positioned such that there was a 0 degree angle between bregma and lambda in all directions. Lateral and middle tendons are removed using fine forceps. The head bar was then placed in one of three stereotactically defined locations and cemented in place These locations are: AP -6.90, ML +/1.25(curved headbar placed caudally onto cerebellum), AP +1.36, ML +/- 1.25 (curved headbar placed rostrally onto frontal zones), and AP -2.95, ML +/-1.25 (straight headbar placed centrally). The location of planned future craniotomies were measured using a pipette referenced to bregma, and marked on the skull using either a surgical blade or pen. A small amount of vetbond was applied to the edges of the skin wound to seal it off and create more surface area. The exposed skull was then covered with cement and clear UV curing glue, ensuring that the remaining scalp was unable to retract from the implant. 

## **Behavioral training and habituation to the ephys rig** 

All recordings performed in this study were done in expert mice. To reach this status, animals were habituated for three days and trained for several days in the equal probability task version where the Gabor patch appears on the right or left side of the screen with equal probability. Animals are trained to move the visual stimulus controlled by a wheel toward the center of the screen. Animals must reach a ‘trained 1b’ status wherein each of the three consecutive sessions, the mouse completed over 400 trials and performed over 90% on the easy (contrast >= 50%) trials. Additionally, the median reaction time across these sessions must be below 2 seconds for the 0% contrast. Lastly, a psychometric curve is fitted with four parameters bias, lapse right, lapse left and threshold, must meet the following criteria: the absolute bias must be below 10, the threshold below 20, and each lapse below 0.1. Once these conditions are met, animals progress to ‘biasedChoiceWorld’ in which they are first presented with an unbiased block of trials and subsequently blocks are from either of two biased blocks: Gabor patch is presented on the left and right with probabilities of 0.2 and 0.8 (20:80) respectively, and in the other block type the Gabor patch is presented on the left and right with probabilities of 0.8 and 0.2 (80:20) respectively. In summary, once mice learned the biasedChoiceWorld task (criteria ‘ready4ephysRig’ reached), they were habituated to the electrophysiology rig. Briefly, this criterion is met by performing three consecutive sessions that meet ‘trained 1b’ status. Additionally, psychometric curves (separately fit for each block type) must have bias shifts < 5%, and lapse rates measured on asymmetric blocks must be below 0.1. Their first requirement was to perform one session of biasedChoiceWorld on the electrophysiology rig, with at least 400 trials and 90% correct on easy contrasts (collapsing across block types). Once this criterion was reached, time delays were introduced at the beginning of the session; these delays served to mimic the time it would take to insert electrodes in the brain. To be included in subsequent sessions, mice were required to maintain performance for 3 subsequent sessions (same criterion as ‘ready4ephysRig’), with a minimum of one session with a 15-minute pre-session delay. For the analyses in this study, only electrophysiology sessions where the mouse completed at least 400 trials were used. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

31 of 89 

## **Electrophysiological recording using Neuropixels probes** 

## **Data acquisition** 

Briefly, upon the day of electrophysiological recording, the animal was anaesthetised using isoflurane and surgically prepared. The UV glue was removed using ethanol and a biopsy punch or a scalpel blade. The exposed skull was then checked for infection. A test was made to check whether the implant could hold liquid without leaking to ensure that the brain did not dry during the recording. Subsequently, a grounding pin was cemented to the skull using Metabond. 1-2 craniotomies (1 × 1 mm) were made over the marked locations using a biopsy punch or drill. The dura was left intact, and the brain was lubricated with ACSF. DuraGel was applied over the dura as a moisturising sealant, and covered with a layer of Kwikcast. The mouse was administered analgesics subcutaneously, and left to recover in a heating chamber until locomotor and grooming activity were fully recovered. 

Once the animal was recovered from the craniotomy, it was relocated to the apparatus. Once a craniotomy was made, up to 4 subsequent recording sessions were made in that same craniotomy. Up to two probes were implanted in the brain on a given session. 

## **Probe track labeling** 

CM-Dil (V22888, Thermofisher) was used to label probes for subsequent histology. CM-Dil was strored in the freezer -at 20C until ready for use. On the day of recording, we thawed CM-Dil at room temperature, protecting it from light. Labeling took place under a microscope while the Neuropixels probe was secured onto a micromanipulator, electrode sites facing up. 1uL of CM-Dil was placed onto either a coverslip or parafilm. Using the micromanipulator, the probe tip was inserted into the drop of dye with care taken to not get dye onto the electrode sites. For Neuropixels probes, the tip extends about 150um from the first electrode site. The tip is kept in the dye until the drop dries out completely (approximately 30 seconds) and then the micromanipulator is slowly retracted to remove the probe). 

## **Spike sorting** 

Raw electrophysiological recordings were initially saved in a flat uncompressed binary format, representing a storage of 1.3GB per minute. To save disk space and achieve better transfer speeds we utilized simple lossless compression to achieve a compression ratio between 2x and 3x. In many cases, we encounter line noise due to voltage leakage on the probe. This translates into large "stripes" of noise spanning the whole probe. To reduce the impact of these noise "stripes" we perform three main pre-processing steps including: (1) correction for "sample shift" along the length of the probe by aligning the samples with a frequency domain approach; (2) automatic detection, rejection and interpolation of failing channels; (3) application of a spatial “de-striping" filter. After these preprocessing steps, spike sorting was performed using ibl-sorter, a Python port of the Kilosort 2.5 algorithm that includes modifications to preprocessing ( Steinmetz et al., 2021 ). At this step, we apply registration, clustering, and spike deconvolution. We found it necessary to improve the original code in several aspects (e.g., improved modularity and documentation, and better memory handling for datasets with many spikes) and developed an open-source Python port; the code repository is here: ( _The International Brain Laboratory et al., 2024_ ). See _The International Brain Laboratory et al._ ( _2022a_ ) for full details. 

## **Single cluster quality metrics** 

To determine whether a single cluster will be used in downstream analysis, we used three metrics (listed as part of RIGOR in **Table 1** ): the refractory period, an amplitude cut-off estimate, and the median of the amplitudes. First, we developed a metric which estimates whether a neuron is 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

32 of 89 

contaminated by refractory period violations (indicating potential overmerge problems in the clustering step) without assuming the length of the refractory period. For each of the many refractory period lengths, we compute the number of spikes (refractory period violations) that would correspond to some maximum acceptable amount of contamination (chosen as 10%). We then compute the likelihood of observing fewer than this number of spikes in that refractory period under the assumption of Poisson spiking. For a neuron to pass this metric, this likelihood that our neuron is less than 10% contaminated, must be larger than 90% for any one of the possible refractory period lengths. 

Next, we compute an amplitude cut-off estimate. This metric estimates whether an amplitude distribution is cut off by thresholding in the deconvolution step (thus leading to a large fraction of missed spikes). To do so, we compare the lowest bin of the histogram (the number of neurons with the lowest amplitudes), to the bins in the highest quantile of the distribution (defined as the top 1/4 of bins higher than the peak of the distribution.) Specifically, we compute how many standard deviations the height of the low bin falls outside of the mean of the height of the bins in the high quantile. For a neuron to pass this metric, this value must be less than 5 standard deviations, and the height of the lowest bin must be less than 10% of the height of the peak histogram bin. See for further details. 

Finally, we compute the median of the amplitudes. For a neuron to pass this metric, the median of the amplitudes must be larger than 50 uV. 

## **Local field potential (LFP)** 

Concurrently with the action potential band, each channel of the Neuropixel probe recorded a low-pass filtered trace at a sampling rate of 2500 Hz. A denoising was applied to the raw data, comprising four steps. First a Butterworth low-cut filter is applied on the time traces, with 2Hz corner frequency and order 3. Then a subsample shift was applied to rephase each channel according to the time-sampling difference due to sequential sampling of the hardware. Then faulty bad channels were automatically identified, removed and interpolated. Finally, the median reference is subtracted at each time sample. See _The International Brain Laboratory et al._ ( _2022a_ ) for full details. After this processing, the power spectral density at different frequencies was estimated per channel using the Welch’s method with partly overlapping Hanning windows of 1024 samples. Power spectral density (PSD) was converted into dB as follows: 

**==> picture [321 x 11] intentionally omitted <==**

## **Serial section two-photon imaging** 

Mice were given a terminal dose of pentobarbital intraperitoneally. The toe-pinch test was performed as confirmation that the mouse was deeply anesthetized before proceeding with the surgical procedure. Thoracic cavity was opened, the atrium was cut, and PBS followed by 4% formaldehyde solution (Thermofisher 28908) in 0.1M PB pH 7.4 were perfused through the left ventricle. The whole mouse brain was dissected and post-fixed in the same fixative for a minimum of 24 hours at room temperature. Tissues were washed and stored for up to 2-3 weeks in PBS at 4C, prior to shipment to the Sainsbury Wellcome Centre for image acquisition. 

The brains were embedded in agarose and imaged in a water bath filled with 50 mM PB using a 4 kHz resonant scanning serial section two-photon microscopy ( Ragan et al., 2012 ; Economo et al., 2016 ). The microscope was controlled with ScanImage Basic (Vidrio Technologies, USA), and BakingTray, a custom software wrapper for setting up the imaging parameters ( Campbell, 2020 ). Image tiles were assembled into 2D planes using StitchIt ( Campbell, 2021 ). Whole brain coronal image stacks were acquired at a resolution of 4.4 x 4.4 x 25.0 µm in XYZ (Nikon 16x NA 0.8), with a two-photon laser wavelength of 920 nm, and approximately 150 mW at the sample. The microscope cut 50 µm sections using a vibratome (Leica VT1000) but imaged two optical planes 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

33 of 89 

within each slice at depths of about 30 µm and 55 µm from the tissue surface using a PIFOC. Two channels of image data were acquired simultaneously using Hamamatsu R10699 multialkali PMTs: ‘Green’ at 525 nm ±25 nm (Crhoma ET525/50m); ‘Red’ at 570 nm low pass (Chroma ET570lp). 

Whole brain images were downsampled to 25 µm isotropic voxels and registered to the adult mouse Allen common coordinate framework ( Wang et al., 2020 ) using BrainRegister ( West, 2021 ), an elastix-based ( Klein et al., 2010 ) registration pipeline with optimised parameters for mouse brain registration. Two independent registrations were performed, samples were registered to the CCF template image and the CCF template was registered to the sample. 

## **Probe track tracing and alignment** 

Tracing of Neuropixels electrode tracks was performed on registered image stacks. Neuropixels probe tracks were manually traced to yield a probe trajectory using Lasagna ( Campbell et al., 2020 ), a Python-based image viewer equipped with a plugin tailored for this task. Tracing was performed on the merged images on the green (auto-fluorescence) and red (CM-Dil labeling) channels, using both coronal and sagittal views. Traced probe track data was uploaded to an Alyx server ( Rossant et al., 2021 ); a database designed for experimental neuroscience laboratories. Neuropixels channels were then manually aligned to anatomical features along the trajectory using electrophysiological landmarks with a custom electrophysiology alignment tool ( Faulkner, 2020 ) ( Liu et al., 2021 ). This alignment process was performed by the experimenter and an additional member to ensure agreement on the assigned channel locations. 

## **Permutation tests and power analysis** 

We use permutation tests to study the reproducibility of neural features across laboratories. To this end, we first defined a test statistic that is sensitive to systematic deviations in the distributions of features between laboratories: the maximum absolute difference between the cumulative distribution function (CDF) of a neural feature within one lab and the CDF across all other labs (similar to the test statistic used for a Kolmogorov–Smirnov test). For the CDF, each mouse might contribute just a single value (e.g. in the case of the deviations from the target region), or a number for every neuron in that mouse (e.g. in the case of comparing firing rate differences during specific time-periods). The deviations between CDFs from all the individual labs are then reduced into one number by considering only the deviation of the lab with the strongest such deviation, giving us a metric that quantifies the difference between lab distributions. The null hypothesis is that there is no difference between the different laboratory distributions, i.e. the assignment of mice to laboratories is completely random. We sampled from the corresponding null distribution by permuting the assignments between laboratories and mice randomly 50,000 times (leaving the relative numbers of mice in laboratories intact) and computing the test statistic on these randomised samples. Given this sampled null distribution, the p-value of the permutation test is the proportion of the null distribution that has more extreme values than the test statistic that was computed on the real data. 

For the power analysis ( **Figure 4, Supp. Fig 2** ), the goal was to find how much each value (firing rate modulations or Fano factors) would need to shift within the individual labs to create a significant p-value for any given test. This grants us a better understanding of the workings and limits of our test. As we chose an _a_ level of 0.01 (implementing a Bonferroni correction for the number of regions, but not the number of tests, so as to not have too lenient a criterion), we needed to find the perturbations that gave a p-value _<_ 0.01. To achieve this for a given test and a given lab, we took the values of every neuron within that lab, and shifted them all up or down by a certain amount. We used binary search to find the exact points at which such an up- or down-shift caused the test to become significant. This analysis tells us exactly at which points our test becomes significant, and importantly, ensures that our permutation test is sensitive enough to detect deviations of a given magnitudes. It may seem counter intuitive that some tests allow for larger deviations than others, or that even within the same test some labs have a different range of 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

34 of 89 

possible perturbations than others. This is because the test considers the entire distribution of values, resulting in possibly complex interactions between the labs. Precisely because of these interactions of the data with the test, we performed a thorough power analysis to ensure that our procedure is sufficiently sensitive to across-lab variations. The bottom row of **Figure 4, Supp. Fig 2** shows the overall distribution of permissible shifts, the large majority of which is below one standard deviation of the corresponding lab distribution. 

## **Dimensionality reduction of PETHs** 

## **via principal component analysis** 

The analyses in **Figure 5** rely on principal component analysis (PCA) to embed PETHs into a two-dimensional feature space. Our overall approach is to compute PETHs, split into fast-reactiontime and slow-reaction-time trials, then concatenate these PETH vectors for each cell to obtain a summary of each cell’s activity. Next we stack these double PETHs from all labs into a single matrix. Finally, we used PCA to obtain a low-rank approximation of this PETH matrix. 

In detail, the two PETHs consist of one averaging fast reaction time ( _<_ 0.15 _sec_ , 0.15 _sec_ being the mean reaction time when considering the distribution of reaction times across all sessions) trials and the other slow reaction time ( _>_ 0.15 _sec_ ) trials, each of length _T_ time steps. We used 20 ms bins, from −0.5 sec to 1.5 sec relative to motion onset, so _T_ = 100. We also performed a simple normalization on each PETH, subtracting baseline activity and then dividing the firing rates by the baseline firing rate (prior to motion onset) of each cell plus a small positive offset term (to avoid amplifying noise in very low-firing cells), following _Steinmetz et al._ ( _2019_ ). 

Let the stack of these double PETH vectors be _Y_ , being a _N_ × 2 _T_ matrix, where _N_ is the total number of neurons recorded across 5 brain regions and labs. Running principal components analysis (PCA) on _Y_ (singular value decomposition) is used to obtain the low-rank approximation _UV_ ≈ _Y_ . This provides a simple low-d embedding of each cell: _U_ is _N_ × _k_ , with each row of _U_ representing a _k_ -dimensional embedding of a cell that can be visualized easily across labs and brain regions. _V_ is _k_ × 2 _T_ and corresponds to the _k_ temporal basis functions that PCA learns to best approximate _Y_ . **Figure 5a** shows the responses of two cells of _Y_ (black traces) and the corresponding PCA approximation from _UV_ (red traces). 

The scatter plots in **Figure 5c,f** show the embedding _U_ across labs and brain regions, with the embedding dimension _k_ = 2. Each _k_ × 1 vector in _U_ , corresponding to a single cell, is assigned to a single dot in **Figure 5c,f** . 

## **Linear regression model to quantify the contribution** 

## **of spatial and spike features to variability** 

To fit a linear regression model to the session-averaged firing rate of neurons, for each brain region, we used a Nx5 predictor matrix where N is the number of recorded neurons within the region. The five columns contain the following five covariates for each neuron: x, y, z position, spike amplitude, and spike peak-to-trough duration. The Nx1 observation matrix consisted of the average firing rate for each neuron throughout the entire recording period. The linear model was fit using ordinary least-squares without regularization. The unadjusted coefficient of determination ( _R_[2] ) was used to report the level of variability in neuronal firing rates explained by the model. 

## **Video analysis** 

In the recording rigs, we used three cameras, one called ‘left’ at full resolution (1280x1024) and 60 Hz filming the mouse from one side, one called ‘right’ at half resolution (640x512) and 150 Hz, filming the mouse symmetrically from the other side, and one called ‘body’ filming the trunk of 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

35 of 89 

the mouse from above. Several quality control metrics were developed to detect video issues such as poor illumination or accidental misplacement of the cameras. 

We used DeepLabCut ( Mathis et al., 2018 ) to track various body parts such as the paws, nose, tongue, and pupil. The pipeline first detects 4 regions of interest (ROI) in each frame, crops these ROIs using ffmpeg ( Tomar, 2006 ) and applies a separate network for each ROI to track features. For each side video we track the following points: 

ROI eye: 

- 'pupil_top_r', 'pupil_right_r', 'pupil_bottom_r', 'pupil_left_r' ROI mouth: 

- 'tounge_end_r', 'tounge_end_l' ROI nose: 

- 'nose_tip' ROI paws: 'paw_r', 'paw_l' 

The right side video was flipped and spatially up-sampled to look like the left side video, such that we could apply the same DeepLabCut networks. The code is available here: ( The International Brain Laboratory, 2021 ). 

Extensive curating of the training set of images for each network was required to obtain reliable tracking across animals and laboratories. We annotated in total more than 10K frames, across several iterations, using a semi-automated tracking failure detection approach, which found frames with temporal jumps, three-dimensional re-projection errors when combining both side views, and heuristic measures of spatial violations. These selected ‘bad’ frames were then annotated and the network re-trained. To find further raw video and DeepLabCut issues, we inspected trial-averaged behaviors obtained from the tracked features, such as licking aligned to feedback time, paw speed aligned to stimulus onset and scatter plots of animal body parts across a session superimposed onto example video frames. See _The International Brain Laboratory_ ( _2021_ ) for full details. 

Despite the large labeled dataset and multiple network retraining iterations described above, DeepLabCut was not able to achieve sufficiently reliable tracking of the paws or pupils. Therefore we used an improved tracking method, Lightning Pose, for these body parts ( Biderman et al., 2023 ). Lightning Pose models were trained on the same final labeled dataset used to train DeepLabCut. We then applied the Ensemble Kalman Smoother (EKS) post-processor introduced in _Biderman et al._ ( _2023_ ), which incorporates information across multiple networks trained on different train/validation splits of the data. For the paw data, we used a version of EKS that further incorporates information across the left and right camera views in order to resolve occlusions. See _Biderman et al._ ( _2023_ ) for full details. 

## **Multi-task neural network model to quantify sources of variability** 

## **Data preprocessing** 

For the multi-task neural network (MTNN) analysis, we used data from 32 sessions recorded in SWC, CCU, CSHL (C), UCL, Berkeley, NYU, UCLA, and UW. We filtered out the sessions with unreliable behavioral traces from video analysis and selected labs with at least 4 sessions for the MTNN analysis. For the labs with more than 4 sessions, we selected sessions with more recorded neurons across all repeated sites. We included various covariates in our feature set (e.g. go-cue signals, stimulus/reward type, DeepLabCut/Lightning Pose behavioral outputs). For the “decision strategy" covariate, we used the posterior estimated state probabilities of the 4-state GLM-HMMs 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

36 of 89 

trained on the sessions used for the MTNN analysis ( Ashwood et al., 2021 ). Both biased and unbiased data were used when training the 4-state model. For each session, we first filtered out the trials where no choice is made. We then selected the trials whose stimulus onset time is no more than 0.4 seconds before the first movement onset time and feedback time is no more than 0.9 seconds after the first movement onset time. Finally, we selected responsive neurons whose mean firing rate is greater than 5 spikes/second for further analyses, to make model training more efficient; using a lower threshold of 1 Hz did not substantially change the results. 

The lab IDs and session IDs were each encoded in a “one-hot” format (i.e., each lab is encoded as a length 8 one-hot vector). For the leave-one-out effect size of the session IDs, we compared the model trained with all of the covariates in **Table 2** against the model trained without the session IDs. For the leave-one-out effect size of the lab IDs, we compared the model trained without the lab IDs against the model trained without both the lab and session IDs. We prevented the lab and session IDs from containing overlapping information with this encoding scheme, where the lab IDs cannot be predicted from the session IDs, and vice versa, during the leave-one-out analysis. 

## **Model Architecture** 

Given a set of covariates in **Table 2** , the MTNN predicts the target sequence of firing rates from 0.5 seconds before first movement onset to 1 second after, with bin width set to 50 ms (30 time bins). More specifically, a sequence of feature vectors _x_ dynamic ∈ ℝ _[D]_[dynamic][×] _[T]_ that include dynamic covariates, such as Deep Lab Cut (DLC) outputs, and wheel velocity, and a feature vector _x_ static ∈ ℝ _[D]_[static] that includes static covariates, such as the lab ID, neuron’s 3-D location, are input to the MTNN to compute the prediction _y[pred]_ ∈ ℝ _[T]_ , where _D_ static is the number of static features, _D_ dynamic is the number of dynamic features, and _T_ is the number of time bins. The MTNN has initial layers that are shared by all neurons, and each neuron has its designated final fullyconnected layer. 

Given the feature vectors _x_ dynamic and _x_ static for session _s_ and neuron _u_ , the model predicts the firing rates _y[pred]_ by: 

**==> picture [337 x 12] intentionally omitted <==**

**==> picture [291 x 12] intentionally omitted <==**

**==> picture [299 x 12] intentionally omitted <==**

**==> picture [291 x 12] intentionally omitted <==**

**==> picture [285 x 12] intentionally omitted <==**

where _f_ is the activation function. **Eqn. (2)** and **Eqn. (3)** are the shared fully-connected layers for static and dynamic covariates, respectively. **Eqn. (4)** and **Eqn. (5)** are the shared one-layer bidirectional recurrent neural networks (RNNs) for dynamic covariates, and **Eqn. (6)** is the neuron-specific fully-connected layer, indexed by ( _s, u_ ). Each part of the MTNN architecture can have an arbitrary number of layers. For our analysis, we used two fully-connected shared layers for static covariates ( **Eqn. (2)** ) and four-layer bidirectional RNNs for dynamic covariates, with the embedding size set to 128. 

## **Model training** 

The model was implemented in PyTorch and trained on a single GPU. The training was performed using Stochastic Gradient Descent on the Poisson negative loglikelihood (Poisson NLL) loss with learning rate set to 0.1, momentum set to 0.9, and weight decay set to 10[−15] . We used a learning 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

37 of 89 

rate scheduler such that the learning rate for the _i_ -th epoch is 0.1 × 0.95 _[i]_ , and the dropout rate was set to 0.15. We also experimented with mean squared error (MSE) loss instead of Poisson NLL loss, and the results were similar. The batch size was set to 1024. 

The dataset consists of 32 sessions, 1133 neurons and 11490 active trials in total. For each session, 20% of the trials are used as the test data and the remaining trials are split 20:80 for the validation and training sets. During training, the performance on the held-out validation set is checked after every 3 passes through the training data. The model is trained for 100 epochs, and the model parameters with the best performance on the held-out validation set are saved and used for predictions on the test data. 

## **Simulated experiments** 

For the simulated experiment in **Figure 8-supplemental 2** , we first trained GLMs on the same set of 1133 responsive neurons from 32 sessions used for the analysis in **Figure 8d** and **8e** , with a reduced set of covariates consisting of stimulus timing, stimulus side and contrast, first movement onset timing, feedback type and timing, wheel velocity, and mouse’s priors for the current and previous trials. The kernels of the trained GLMs show the contribution of each of the covariates to the firing rates of each neuron. For each simulated neuron, we used these kernels of the trained GLM to simulate its firing rates for 500 randomly initialized trials. The random trials were 1.5 seconds long with 50 ms bin width. For all trials, the first movement onset timing was set to 0.5 second after the start of the trial, and the stimulus contrast, side, onset timing and feedback type, timing were randomly sampled. We used wheel velocity traces and mouse’s priors from real data for simulation. We finally ran the leave-one-out analyses with GLMs/MTNN on the simulated data and compared the effect sizes estimated by GLMs and MTNN. 

## **Supplementary figures** 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

38 of 89 

**==> picture [444 x 468] intentionally omitted <==**

**Figure 1–Figure supplement 1.** 

## **Detailed experimental pipeline for the Neuropixels experiment.** 

The experiment follows the main steps indicated in the colored squares at left in chronological order from top to bottom. Within each main step, actions are undertaken from left to right; diamond markers indicate points of quality control. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**39 of 89** 

**==> picture [398 x 355] intentionally omitted <==**

**Figure 1–Figure supplement 2.** 

## **Electrophysiology data quality examples.** 

**(a)** Example raster (left) and raw electrophysiology data snippet (right) for a recording that passes quality control. The black vertical line on the raster indicates the completion of the behavioral task and transition to spontaneous and passive stimulus periods. Red dots on the raw data snippets indicate detected spikes from multi-unit activity; green dots indicate spikes from "good" units. Colored columns to the right of each plot indicate the brain regions at each depth as in **Fig 1c** and **e** . **(b)** Example raster and raw data snippets for four recordings that fail quality control; either because of the presence of epileptiform activity (top-left), pronounced drift (top-right), artifacts (bottom-left), or large number of noisy channels (bottom-right). 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**40 of 89** 

**==> picture [398 x 466] intentionally omitted <==**

**Figure 1–Figure supplement 3.** 

## **Detailed comparison of yield between our dataset and published reference datasets.** 

Detailed comparison between the current dataset (IBL, left), Steinmetz et al. 2019 (STE, middle), and Siegle et al. 2021 (ALN, right) for measurements within cortex (Top; blue graphs), hippocampus (Middle; green graphs), and thalamus (Bottom; pink graphs). The plots show, in order: the number of insertions included in each dataset; the number of sites in the brain region per insertion; the number of "neurons" produced by the spike sorting algorithm without any quality metric filters, per insertion; the number of neurons (no QC filters) per site; the fraction of neurons passing the refractory period metric; the fraction of neurons passing the noise cutoff metric; the fraction of neurons passing the minimum amplitude metric; and, the number of neurons passing all three QC metrics, per site (as shown in **Fig. 1f** ). In all cases, error bars show mean ± std. err. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**41 of 89** 

**==> picture [444 x 181] intentionally omitted <==**

**Figure 1–Figure supplement 4.** 

## **Visual inspection of datasets by three observers blinded to data identity yielded similar metrics for all three studies.** 

Each plot reflects manually-determined scores from a single observer (letters at top indicate their initials), who was blinded to the origin of the dataset at the time of scoring. Labels on the horizontal axis indicate the dataset: the current dataset (IBL, left), Steinmetz et al., 2019 (STE, middle), and Siegle et al. 2021 (ALN, right). Each point is the score assigned to a single snippet. Error bars represent mean ± std. err. A two way ANOVA was performed with rater identity and source dataset as categorical variables. A two way ANOVA was performed with rater identity and source dataset as categorical variables. We found a significant effect of rater ID ( _p <_ 10[−6] ), and a significant interaction between rater ID and dataset ( _p <_ 0.05), reflecting statistically reliable differences between datasets that were inconsistent from rater to rater. There was no significant effect of dataset ( _p_ = 0.08) overall. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**42 of 89** 

**==> picture [444 x 444] intentionally omitted <==**

**Figure 2–Figure supplement 1.** 

## **Tilted slices of histology along the probe insertion for all insertions used in assessing probe placement.** 

Histology slices were tilted to be off-coronal along the linearly interpolated best-fit to the probe insertion vector (green: autofluorescence data for image registration; red: CM-DiI fluorescence signal marking probe tracks). Traced probe tracks are highlighted in white. Note that tissue damage at the brain surface visible in many sections generally occurs at the time of perfusion and brain removal, as scar tissue related to the craniotomy is detached from the brain. Scale bar: 1mm. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**43 of 89** 

**==> picture [398 x 461] intentionally omitted <==**

**Figure 3–Figure supplement 1.** 

## **Recordings that did not pass QC can be visually assessed as outliers.** 

**(a, b)** Probe plots as in **Figure 3b,c** . The mouse name (top) is colored according to whether the recording passed QC (green) or failed (red). The probes are ordered according to the distance from the planned repeated site from left to right. **(c)** Probe plots showing the power spectrum of the LFP prior to using electrophysiological features to align the location of the recording channels. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**44 of 89** 

**==> picture [398 x 343] intentionally omitted <==**

## **Figure 3–Figure supplement 2.** 

## **High LFP power in dentate gyrus was used to align probe locations in the brain.** 

Power spectral density between 20 and 80 Hz recorded along each probe shown in **Fig. 3** overlaid on a coronal atlas slice (from the Allen Common Coordinate Framework template volume). Each coronal slice has been rotated so that the probe lies along the vertical axis. Colors correspond to probe insertions belonging to a single lab (color legend at bottom). Scale bar (red) is 1 mm. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**45 of 89** 

**==> picture [444 x 434] intentionally omitted <==**

**Figure 3–Figure supplement 3.** 

## **Bilateral recordings assess within- vs across-animal variance.** 

Bilateral recordings of the repeated site in both hemispheres show within-animal variance is often smaller than across-animal variance. **(a, b)** , Power spectral density and neural activity of all bilateral recordings. L and R indicate the left and right probe of each bilateral recording. Each L/R pair is recorded simultaneously. The color indicates the lab (lab-color assignment as in **Fig. 3** ). **(c)** Comparison of within-animal variance to across-animal variance for LFP power in CA1. The across-animal variance is depicted as the distribution of all pair-wise absolute differences in LFP power between any two recordings in the entire dataset (blue shaded violin plot). The black horizontal ticks indicate where the bilateral recordings (within-animal differences) fall in this distribution. **(d, e)** Violin plots for firing rate and spike amplitude in VISa/am, similar analysis as in (c). **(f)** Whether within or across animal variance is larger is dependent on the metric and brain region; red colors indicate that within < across and green colors within > across. Variance is quantified here as the interquartile distance of the distributions in c-e. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**46 of 89** 

**==> picture [444 x 378] intentionally omitted <==**

**Figure 3–Figure supplement 4.** 

## **Values used in the decoding analysis, per metric and per brain region.** 

All electrophysio-logical features (rows) per brain region (columns) that were used in the permutation test and decoding analysis of **Figure 3** . Each dot is a recording, colors indicate the laboratory. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**47 of 89** 

**==> picture [398 x 517] intentionally omitted <==**

**Figure 4–Figure supplement 1.** 

## **Proportion of task-modulated neurons, defined by six statistical comparisons, across mice, labs, and brain regions.** 

**(a)** - **(f)** , Schematics of six statistical comparisons in specific task-related time windows to quantify neuronal task modulation. Each panel includes a schematic depiction of the time windows analyzed in the comparison, where the example trials show potential caveats of each method. For instance, in (a) the stimulus period may or may not include movement, depending on the reaction time of the animal. In (c), to avoid any overlap between pre-stimulus and reaction periods, we calculated the reaction period only in trials with >50 ms between the stimulus and movement onset. We also limited the reaction period to a maximum of 200 ms before movement onset. Below each test schematic, the corresponding proportion of task-modulated neurons across brain regions is shown, colored by lab ID (points are individual sessions; horizontal lines around vertical marker are mean ± s.e.m. across sessions). 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**48 of 89** 

**==> picture [398 x 463] intentionally omitted <==**

**Figure 4–Figure supplement 2.** 

## **Power analysis of permutation tests.** 

**(a)** For every test and every lab, we performed a power analysis to test how far the values of that lab would have to be shifted upwards or downwards to cause a significant permutation test (tests that were already significant in the absence of such shifts are crossed out). The p-values shown indicate the p-value of the unperturbed test. Horizontal lines indicate the means of the lab distributions and vertical bars indicate the range over which up- and downwards perturbations do not result in a significant test (p-value _<_ 0.01). These typically show a rather small range of permissible values, which means that our permutation testing procedure is sensitive to detecting small differences in the measured quantities in individual labs. The most notable exception is the Fano Factor, meaning our ability to detect systematic differences in Fano Factor across labs is limited. **(b)** The correlation between the within-lab standard error of the mean of the measured quantity and the minimal shift size required to yield a significant test, showing that, as expected, measured modulations that are precisely distributed (small standard error) are very sensitive to small shifts. **(c)** Histogram of the magnitude of minimal shifts in units of the standard deviation of the corresponding distribution. Most shifts are below 1 standard deviation of the corresponding lab distribution. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**49 of 89** 

**==> picture [398 x 399] intentionally omitted <==**

**Figure 5–Figure supplement 1.** 

## **Lab-grouped average PETH, CDF of the first PC and 2-PC embedding, separate per brain region.** 

Mean firing rates across all labs per region including VISa/am, CA1, DG, LP, and PO (panels a, d, g, j, m). In addition, the second column of panels (panels b, e, h, k, n) shows for each region the cumulative distribution function (CDF) of the first embedding dimension (PC1) per lab. The insets show the Kolmogorov-Smirnov distance (KS) per lab from the distribution of all remaining labs pooled, annotated with an asterisk if _p <_ 0.01 for the KS test. The third column of panels (c, f, i, l, o) displays the embedded activity of neurons from VISa/am, CA1, DG, LP, and PO. For 6 region/lab pairs, dynamics were significantly different from the mean of all remaining labs using the KS test. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**50 of 89** 

**==> picture [398 x 396] intentionally omitted <==**

**Figure 6–Figure supplement 1.** 

## **High-firing and task-modulated VISa/am neurons.** 

**(a-d)** Similar to **Figure 6** but for VISa/am. High-firing and some task-modulated VISa/am neurons had slightly different spatial positions than other VISa/am neurons, as shown, but had similar spike waveform features. Out of 877 VISa/am neurons, 550 were modulated during movement initiation (in (c)) and 170 were modulated differently for leftward vs. rightward movements (in (d)). 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**51 of 89** 

**==> picture [398 x 391] intentionally omitted <==**

**Figure 6–Figure supplement 2.** 

## **High-firing and task-modulated CA1 neurons.** 

**(a-d)** Similar to **Figure 6** but for CA1. High-firing and some task-modulated CA1 neurons had slightly different spatial positions than other CA1 neurons, as shown, but had similar spike waveform features. Out of 548 CA1 neurons, 366 were modulated during movement initiation (in (c)) and 109 were modulated differently for leftward vs. rightward movements (in (d)). 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**52 of 89** 

**==> picture [444 x 378] intentionally omitted <==**

**Figure 6–Figure supplement 3.** 

## **High-firing and task-modulated DG and PO neurons.** 

Spatial positions of high-firing and some task-modulated neurons in PO, but not DG, were different from other neurons. **(ab)** , Spatial positions of DG neurons plotted as distance from the planned target center of mass, indicated with the black x. Spatial positions were not significantly different between high-firing neurons (yellow) and the general population of neurons (blue hues) in (a), nor between task-modulated (orange) and non-modulated (gray) neurons in (b). High-firing neurons and task-modulated neurons (for only some tests) tended to have lower spike durations, possibly related to cell subtype differences. 262 out of 448 DG neurons were modulated during movement initiation (in (b)). **(c-d)** , Same as (a-b) but for PO neurons. Spatial positions and spike waveform features were significantly different between outliers and the general population of neurons (in (c)). Task-modulated and non-modulated PO neurons had small differences in spatial position for only some tests (not the test shown in (d)) and no difference in spike waveform features. 833 out of 1529 PO neurons were modulated during movement initiation (in (d)). 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**53 of 89** 

**==> picture [354 x 473] intentionally omitted <==**

**Figure 6–Figure supplement 4.** 

## **Time-course and spatial position of neuronal Fano Factors.** 

**(a)** _Left column_ : Firing rate (top) and Fano Factor (bottom) averaged over all VISa/am neurons when aligned to movement onset after presentation of left or right full-contrast stimuli (correct trials only; Fano Factor calculation limited to neurons with a session-averaged firing rate >1 sp/sec). Error bars: standard error means between neurons. _Right column_ : Neuronal Fano Factors (averaged over 40-200 ms post movement onset after right-side full-contrast stimuli, i.e. shaded green section from the left column) and their spatial positions. Larger circles indicate neurons with Fano Factor <1. **(b-e)** Same as (a) for CA1, DG, LP, and PO. Spatial position between high vs. low Fano Factor neurons was only significantly different in VISa/am (deeper neurons had lower Fano Factors). In VISa/am, spike duration between high and low Fano Factor neurons was also significantly different, possibly due to cell subtype differences (neurons with shorter spike durations tended to have higher Fano Factors; histograms not shown). Lastly, in CA1 and PO, neurons with larger spike amplitudes had slightly higher Fano Factors. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**54 of 89** 

**==> picture [398 x 411] intentionally omitted <==**

**Figure 6–Figure supplement 5.** 

## **Neuronal subtypes and firing rates.** 

High-firing neurons do not belong to a specific cell subtype. To identify putative Fast-Spiking (FS) and Regular-Spiking (RS) neuronal populations, we examined spike peak-to-trough durations (Jia et al., 2019 ). This distribution was bimodal in Visa/am, CA1, and DG, but not LP and PO (as expected from _Jia et al._ ( _2019_ )). This bimodality (indicated with the black and blue boxes) suggests distinct populations of FS and RS neurons only in cortical and hippocampal regions, which should have narrow (black) and wide (blue) spike widths, respectively. To confirm the distinct populations of FS and RS neurons, we next plotted the cumulative probability of firing rate for these two putative neuronal categories. Indeed, in cortex and hippocampus, neurons with narrow spikes tend to have higher firing rates (in black) while neurons with wider spikes have lower firing rates (in blue). In contrast, in LP and PO, we did not identify specific populations of neuronal subtypes using the spike waveform (to our knowledge, this has not been done in previous work either). Importantly, even in cortex/hippocampus where putative RS and FS neurons are distinguishable, there is still a large firing rate overlap between these two groups, especially for firing rates above 11-19 sp/s (the firing rate thresholds from **Figure 6** and supplemental figures). Hence, high-firing neurons do not seem to belong to only a specific neuronal subtype. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**55 of 89** 

**==> picture [398 x 390] intentionally omitted <==**

**Figure 8–Figure supplement 1.** 

## **MTNN prediction quality** 

**(a)** For each neuron in each session, we plot the MTNN prediction quality on held-out test trials against the firing rate of the neuron averaged over the test trials. Each lab/session is colored/shaped differently. _R_[2] values on concatenations of the heldout test trials are shown on the left, and those on PETHs of the held-out test trials on the right. **(b)** MTNN slightly outperforms GLMs on predicting the firing rates of held-out trials when trained on movement/task-related/prior covariates. **(c)** The left half shows for each neuron the trial averaged activity for left choice trials and next to it right choice trials. The vertical green lines show the first movement onset. The horizontal red lines separate recording sessions while the blue lines separate labs. The right half of each of these images shows the MTNN prediction of the left half. The trial-averaged MTNN predictions for held-out test trials capture visible modulations in the PETHs. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**56 of 89** 

**==> picture [398 x 404] intentionally omitted <==**

**Figure 8–Figure supplement 2.** 

## **MTNN prediction quality on the data simulated from GLMs is comparable to the GLMs’ prediction quality.** 

To verify that the MTNN leave-one-out analysis is sensitive enough to capture effect sizes, we simulate data from GLMs and compare the effect sizes estimated by the MTNN and GLM leave-one-out analyses. We first fit GLMs to the same set of sessions that are used for the MTNN effect size analysis and then use the inferred GLM kernels to simulate data. **(a)** We show the scatterplot of the GLM and MTNN predictive performance on held-out test data, where each dot represents the predictive performance for one neuron. The MTNN prediction quality is comparable to that of GLMs. **(b)** We run GLM and MTNN leaveone-out analyses and compare the estimated effect sizes for eight covariates. The effect sizes estimated by the MTNN and GLM leave-one-out analyses are comparable. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**57 of 89** 

**==> picture [444 x 444] intentionally omitted <==**

**Figure 8–Figure supplement 3.** 

## **Lab IDs have a negligible effect on the MTNN prediction. MTNN leave-one-out analysis captures artificially inflated lab ID effects.** 

**(a)** (Left) Observed per-lab PETH of held-out test trials for PO. (Center) Per-lab PETH of held-out test trials with MTNN predictions for PO. (Right) Per-lab PETH of held-out test trials with MTNN predictions for PO, after fixing the lab IDs of the input to CCU. **(b)** Here we verify that the MTNN leave-one-out analysis is sensitive enough to capture variability induced by lab IDs. First, given an MTNN model trained with the full set of covariates listed in **Table 2** , we created four different MTNN models by perturbing the weights for the lab IDs. One is a model with the originally learned weights for the lab IDs ("Original lab weights"). The other three models have (randomly sampled) orthogonal weights for the lab IDs, where the l2 norms of the weights for the first and last labs (i.e., the labs with lab IDs 1 and 8) are set to _a_ and _b_ , respectively ("Perturbed lab weights, Varying l2 norm: _a_ - _b_ "). The l2 norms of the weights for the labs in between (i.e., the labs with lab IDs from 2 to 7) are set to values equally spaced between _a_ and _b_ . We then generated four different sets of datasets by running the models forward with the original features that are used to train, validate and test the model. Finally, we reran the MTNN leave-oneout analysis for the lab IDs with each simulated dataset. Each dot in each column represents the change in prediction quality (measured by _R_[2] ) for each neuron in the dataset, when the lab IDs are left out from the set of covariates. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**58 of 89** 

**==> picture [444 x 427] intentionally omitted <==**

**Figure 8–Figure supplement 4.** 

We plot pairwise scatterplots of MTNN single-covariate effect sizes. Each dot represents the effect sizes of one neuron and is colored by lab. Many of the effect sizes are highly correlated across sessions and labs. 

**International Brain Laboratory** _**et al.**_ **, 2025 eLife. https://doi.org/10.7554/eLife.100840.2** 

**59 of 89** 

## **Acknowledgements** 

This work was supported by grants from the Wellcome Trust (209558 and 216324), National Institutes of Health (1F32MH123010, 1U19NS123716, including a Diversity Supplement) and the Simons Collaboration on the Global Brain. We thank R. Poldrack, T. Zador, P. Dayan, S. Hofer, N. Ghani, and C. Hurwitz for helpful comments on the manuscript. We thank Anna li for graphical contributions to **Figures 1** and **3** . 

The production of all IBL Platform Papers is led by a Task Force, which defines the scope and composition of the paper, assigns and/or performs the required work for the paper, and ensures that the paper is completed in a timely fashion. The Task Force members for this platform paper include authors SAB, GC, AKC, MFD, CL, HDL, MF, GM, LP, NR, MS, NAS, MT, and SJW. 

## **Additional information** 

## **Diversity Statement** 

We support inclusive, diverse and equitable conduct of research. One or more of the authors of this paper self-identifies as a member of an underrepresented ethnic minority in science. One or more of the authors self-identifies as a member of the LGBTQIA+ community. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

60 of 89 

## **References** 

Andrianova L, Yanakieva S, Margetts-Smith G, Kohli S, Brady ES, Aggleton JP, Craig MT 2022) **No evidence from complementary data sources of a direct projection from the mouse anterior cingulate cortex to the hippocampal formation** _bioRxiv_ 

Ashwood ZC, Roy NA, Stone IR, Churchland AK, Pouget A, Pillow JW, et al. 2021) **Mice alternate between discrete strategies during perceptual decision-making** _bioRxiv_ :2020–10 

Baker M 2016) **1,500 scientists lift the lid on reproducibility** _Nature_ **533** https://doi.org/10 .1038/533452a 

Barry C, Ginzberg LL, O’Keefe J, Burgess N 2012) **Grid cell firing patterns signal environmental novelty by expansion** _Proceedings of the National Academy of Sciences_ **109** :17687–17692 

Batty E, Merel J, Brackbill N, Heitman A, Sher A, Litke A, Chichilnisky E, Paninski L 2016) **Multilayer recurrent network models of primate retinal ganglion cell responses** _Iclr_ 

Biderman D, Whiteway MR, Hurwitz C, Greenspan N, Lee RS, Vishnubhotla A, Warren R, Pedraja F, Noone D, Schartner M, Huntenburg JM, Khanal A, Meijer GT, Noel JP, Pan-Vazquez A, Socha KZ, Urai AE, Cunningham JP, Sawtell NB, Paninski L 2023) **Lightning Pose: improved animal pose estimation via semi-supervised learning, Bayesian ensembling, and cloud-native open-source tools** _bioRxiv_ 

Birman D, Yang KJ, West SJ, Karsh B, Browning Y, Siegle JH, Steinmetz NA 2023) **Pinpoint: trajectory planning for multi-probe electrophysiology and injections in an interactive web-based 3D environment** _eLife_ **12** :1 https://doi.org/10.1101/2023.07.14.548952 

Bragin A, Jando G, Nadasdy Z, van Landeghem M, Buzsáki G 1995) **Dentate EEG spikes and associated interneuronal population bursts in the hippocampal hilar region of the rat** _Journal of Neurophysiology_ **73** :1691–1705 https://doi.org/10.1152/jn.1995.73.4.1691 

Brazma A, Hingamp P, Quackenbush J, Sherlock G, Spellman P, Stoeckert C, Aach J, Ansorge W, Ball CA, Causton HC, et al. 2001) **Minimum information about a microarray experiment (MIAME)—toward standards for microarray data** _Nature genetics_ **29** :365–371 

Browning Y, Lynch GF, Totten S, Lee D, Svoboda K, Siegle JH 2023) **Brain-wide, MRI-guided electrophysiology** _Society for Neuroscience Abstracts_ :117.25 

Cadena SA, Denfield GH, Walker EY, Gatys LA, Tolias AS, Bethge M, Ecker AS 2019) **Deep convolutional models improve predictions of macaque V1 responses to natural images** _PLOS Computational Biology_ **15** :1–27 https://doi.org/10.1371/journal.pcbi.1006897 

Campbell R 2020) **BakingTray** _GitHub_ 

Campbell R 2021) **StitchIt** _GitHub_ 

Campbell R, Blot A, Rousseau C, Winter O 2020) **Lasagna** _GitHub_ 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

61 of 89 

Chen G, Manson D, Cacucci F, Wills TJ 2016) **Absence of visual input results in the disruption of grid cell firing in the mouse** _Current Biology_ **26** :2335–2342 

Churchland AK, Kiani R, Chaudhuri R, Wang XJ, Pouget A, Shadlen MN 2011) **Variance as a signature of neural computations during decision making** _Neuron_ **69** :818–31 https://doi .org/10.1016/j.neuron.2010.12.037 

Churchland MM, Yu BM, Cunningham JP, Sugrue LP, Cohen MR, Corrado GS, Newsome WT, Clark AM, Hosseini P, Scott BB, Bradley DC, Smith MA, Kohn A, Movshon JA, Armstrong KM, Moore T, Chang SW, Snyder LH, Lisberger SG, Priebe NJ, et al. 2010) **Stimulus onset quenches neural variability: a widespread cortical phenomenon** _Nat Neurosci_ **13** :369–78 https://doi .org/10.1038/nn.2501 

Crabbe JC, Wahlsten D, Dudek BC 1999) **Genetics of mouse behavior: interactions with laboratory environment** _Science_ **284** :1670–1672 

Dragoi G, Tonegawa S 2011) **Preplay of future place cell sequences by hippocampal cellular assemblies** _Nature_ **469** :397–401 

Economo MN, Clack NG, Lavis LD, Gerfen CR, Svoboda K, Myers EW, Chandrashekar J 2016) **A platform for brain-wide imaging and reconstruction of individual neurons** _eLife_ **5** https:// doi.org/10.7554/eLife.10566 

Erlich JC, Brunton BW, Duan CA, Hanks TD, Brody CD 2015) **Distinct effects of prefrontal and parietal cortex inactivations on an accumulation of evidence task in the rat** _eLife_ **4** :e05457 

Errington TM, Mathur M, Soderberg CK, Denis A, Perfito N, Iorns E, Nosek BA 2021) **Investigating the replicability of preclinical cancer biology** _eLife_ **10** :e71601 https://doi.org /10.7554/eLife.71601 

Faulkner M 2020) **Ephys Atlas GUI** _GitHub_ 

Goard MJ, Pho GN, Woodson J 2016) **Sur M. Distinct roles of visual, parietal, and frontal motor cortices in memory-guided sensorimotor decisions** _eLife_ **5** :e13764 

Grosmark AD, Buzsáki G 2016) **Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences** _Science_ **351** :1440–1443 

Hafting T, Fyhn M, Molden S, Moser MB, Moser EI 2005) **Microstructure of a spatial map in the entorhinal cortex** _Nature_ **436** :801–806 

Harvey CD, Coen P, Tank DW 2012) **Choice-specific sequences in parietal cortex during a virtual-navigation decision task** _Nature_ **484** :62–68 

Izenman AJ 1975) **Reduced-rank regression for the multivariate linear model** _Journal of multivariate analysis_ **5** :248–264 

Jia X, Siegle JH, Bennett C, Gale SD, Denman DJ, Koch C, Olsen SR 2019) **High-density extracellular probes reveal dendritic backpropagation and facilitate neuron classification** _Journal of Neurophysiology_ **121** :1831–1847 https://doi.org/10.1152/jn.00680.2018 

Jun JJ, Steinmetz NA, Siegle JH, Denman DJ, Bauza M, Barbarits B, Lee AK, Anastassiou CA, Andrei A, Aydın Ç, et al. 2017) **Fully integrated silicon probes for high-density recording of neural activity** _Nature_ **551** :232–236 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

62 of 89 

Klein S, Staring M, Murphy K, Viergever MA 2010) **Pluim JPW. elastix: a toolbox for intensity based medical image registration** _IEEE Transactions on Medical Imaging_ **29** :196–205 https:// doi.org/10.1109/TMI.2009.2035616 

Klionsky DJ 2016) **Developing a set of guidelines for your research field: a practical approach** _Mol Biol Cell_ **27** :733–8 https://doi.org/10.1091/mbc.E15-09-0618 

Kobak D, Brendel W, Constantinidis C, Feierstein CE, Kepecs A, Mainen ZF, Qi XL, Romo R, Uchida N, Machens CK 2016) **Demixed principal component analysis of neural population data** _eLife_ **5** :e10989 

Li X, Ai L, Giavasis S, Jin H, Feczko E, Xu T, Clucas J, Franco A, Sólon Heinsfeld A, Adebimpe A, Vogelstein JT, Yan CG, Esteban O, Poldrack RA, Craddock C, Fair D, Satterthwaite T, Kiar G, Milham MP 2021) **Moving Beyond Processing and Analysis-Related Variation in Neuroscience** _bioRxiv_ https://doi.org/10.1101/2021.12.01.470790 

Lithgow GJ, Driscoll M, Phillips P 2017) **A long journey to reproducible results** _Nature_ **548** :387– 388 https://doi.org/10.1038/548387a 

Liu LD, Chen S, Hou H, West SJ, Faulkner M, Economo MN, Li N 2021) **Svoboda K, the International Brain Laboratory. Accurate localization of linear probe electrode arrays across multiple brains** _eNeuro_ **8** https://doi.org/10.1523/ENEURO.0241-21.2021 

Liu Y, Dolan RJ, Kurth-Nelson Z, Behrens TE 2019) **Human replay spontaneously reorganizes experience** _Cell_ **178** :640–652 

Lopes G, Bonacchi N, Frazão J, Neto JP, Atallah BV, Soares S, Moreira L, Matias S, Itskov PM, Correia PA, et al. 2015) **Bonsai: an event-based framework for processing and controlling data streams** _Frontiers in neuroinformatics_ **9** :7 

Lopes G, Farrell K, Horrocks EA, Lee CY, Morimoto MM, Muzzu T, Papanikolaou A, Rodrigues FR, Wheatcroft T, Zucca S, et al. 2021) **Creating and controlling visual environments using BonVision** _eLife_ **10** :e65541 

Lucanic M, Plummer WT, Chen E, Harke J, Foulger AC, Onken B, Coleman-Hulbert AL, Dumas KJ, Guo S, Johnson E, et al. 2017) **Impact of genetic background and experimental reproducibility on identifying chemical compounds with robust longevity effects** _Nature communications_ **8** :1–13 

Mathis A, Mamidanna P, Cury KM, Abe T, Murthy VN, Mathis MW, Bethge M 2018) **DeepLabCut: markerless pose estimation of user-defined body parts with deep learning** _Nature neuroscience_ **21** :1281–1289 

McIntosh LT, Maheswaranathan N, Nayebi A, Ganguli S, Baccus SA 2016) **Deep learning models of the retinal response to natural scenes** _Advances in neural information processing systems_ **29** :1369 

Musall S, Kaufman MT, Juavinett AL, Gluf S, Churchland AK 2019) **Single-trial neural dynamics are dominated by richly varied movements** _Nature neuroscience_ **22** :1677–1686 

Najafi F, Elsayed GF, Cao R, Pnevmatikakis E, Latham PE, Cunningham JP, Churchland AK 2020) **Excitatory and inhibitory subnetworks are equally selective during decision-making and emerge simultaneously during learning** _Neuron_ **105** :165–179 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

63 of 89 

Nichols TE, Das S, Eickhoff SB, Evans AC, Glatard T, Hanke M, Kriegeskorte N, Milham MP, Poldrack RA, Poline JB, et al. 2017) **Best practices in data analysis and sharing in neuroimaging using MRI** _Nature neuroscience_ **20** :299–303 

Ólafsdóttir HF, Barry C, Saleem AB, Hassabis D, Spiers HJ 2015) **Hippocampal place cells construct reward related sequences through unexplored space** _eLife_ **4** :e06063 

Penttonen M, Kamondi A, Sik A, Acsády L, Buzsáki G 1997) **Feed-forward and feed-back activation of the dentate gyrus in vivo during dentate spikes and sharp wave bursts** _Hippocampus_ **7** :437–450 

Posani L, Wang S, Muscinelli S, Paninski L, Fusi S 2024) **Rarely categorical, always highdimensional: how the neural code changes along the cortical hierarchy** _bioRxiv_ 

Ragan T, Kadiri LR, Venkataraju KU, Bahlmann K, Sutin J, Taranda J, Arganda-Carreras I, Kim Y, Seung HS, Osten P 2012) **Serial two-photon tomography for automated ex vivo mouse brain imaging** _Nat Methods_ **9** :255–8 https://doi.org/10.1038/nmeth.1854 

Rajasethupathy P, Sankaran S, Marshel JH, Kim CK, Ferenczi E, Lee SY, Berndt A, Ramakrishnan C, Jaffe A, Lo M, Liston C, Deisseroth K 2015) **Projections from neocortex mediate top-down control of memory retrieval** _Nature_ **526** :653–659 

Raposo D, Kaufman MT, Churchland AK 2014) **A category-free neural population supports evolving demands during decision-making** _Nature neuroscience_ **17** :1784–1792 

Rossant C, Winter O, Hunter M, Huntenburg J, Faulkner M, Wells M, Steinmetz N, Harris K, Bonacchi N 2021) **Alyx** _GitHub_ 

Roth MM, Dahmen JC, Muir DR, Imhof F, Martini FJ, Hofer SB 2016) **Thalamic nuclei convey diverse contextual information to layer 1 of visual cortex** _Nat Neurosci_ **19** :299–307 

Saalmann YB, Kastner S 2011) **Cognitive and perceptual functions of the visual thalamus** _Neuron_ **71** :209–223 

Senzai Y, Buzsáki G 2017) **Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells** _Neuron_ **93** :691–704 https://doi.org/10.1016/j .neuron.2016.12.011 

Siegle JH, Jia X, Durand S, Gale S, Bennett C, Graddis N, Heller G, Ramirez TK, Choi H, Luviano JA, Groblewski PA, Ahmed R, Arkhipov A, Bernard A, Billeh YN, Brown D, Buice MA, Cain N, Caldejon S, Casal L, et al. 2021) **Survey of spiking in the mouse visual system reveals functional hierarchy** _Nature_ **592** :86–92 

Silva D, Feng T, Foster DJ 2015) **Trajectory events across hippocampal place cells require previous experience** _Nature neuroscience_ **18** :1772–1779 

Sittig LJ, Carbonetto P, Engel KA, Krauss KS, Barrios-Camacho CM, Palmer AA 2016) **Genetic background limits generalizability of genotype-phenotype relationships** _Neuron_ **91** :1253– 1259 

Steinmetz NA, Aydin C, Lebedeva A, Okun M, Pachitariu M, Bauza M, Beau M, Bhagat J, Böhm C, Broux M, Chen S, Colonell J, Gardner RJ, Karsh B, Kloosterman F, Kostadinov D, Mora-Lopez C, O’Callaghan J, Park J, Putzeys J, et al. 2021) **Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings** _Science_ **372** :eabf4588 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

64 of 89 

Steinmetz NA, Zatka-Haas P, Carandini M, Harris KD 2019) **Distributed coding of choice, action and engagement across the mouse brain** _Nature_ **576** :266–273 

The International Brain Laboratory 2021) **iblvideo** _GitHub_ 

The International Brain Laboratory, Aguillon-Rodriguez V, Angelaki D, Bayer H, Bonacchi N, Carandini M, Cazettes F, Chapuis G, Churchland AK, Dan Y, Dewitt E, Faulkner M, Forrest H, Haetzel L, Hausser M, Hofer SB, Hu F, Khanal A, Krasniak C, Laranjeira I, et al. 2021) **Standardized and reproducible measurement of decision-making in mice** _eLife_ **10** :e63711 https://doi.org/10.7554/eLife.63711 

The International Brain Laboratory, Banga K, Boussard J, Chapuis G, Faulkner M, Harris K, Huntenburg J, Hurwitz C, Lee HD, Paninski L, Rossant C, Roth N, Steinmetz N, Windolf C, Winter O 2022) **Spike sorting pipeline for the International Brain Laboratory** _figshare_ https://doi .org/10.6084/m9.figshare.19705522.v3 

The International Brain Laboratory, Banga K, Faulkner M, Langfield C, Rossant C, Winter O 2024) **ibl-sorter** 

The International Brain Laboratory, Birman D, Bonacchi N, Buchanan K, Chapuis G, Huntenburg J, Meijer G, Paninski L, Schartner M, Svoboda K, Whiteway M, Wells M, Winter O 2022) **Video hardware and software for the International Brain Laboratory** _figshare_ https: //doi.org/10.6084/m9.figshare.19694452 

Tolhurst DJ, Movshon JA, Dean AF 1983) **The statistical reliability of signals in single neurons in cat and monkey visual cortex** _Vision Res_ **23** :775–85 http://www.ncbi.nlm.nih.gov/entrez /query.fcgi?cmd=Retrieve&db=PubMed&dopt=Citation&list_uids=6623937 

Tomar S 2006) **Converting video formats with FFmpeg** _Linux Journal_ **2006** :10 

Tsui J, Schwartz N, Ruthazer ES 2010) **A developmental sensitive period for spike timingdependent plasticity in the retinotectal projection** _Frontiers in synaptic neuroscience_ **2** :13 

Turk-Browne NB 2019) **The hippocampus as a visual area organized by space and time: A spatiotemporal similarity hypothesis** _Vision research_ **165** :123–130 

Voelkl B, Altman NS, Forsman A, Forstmeier W, Gurevitch J, Jaric I, Karp NA, Kas MJ, Schielzeth H, Van de Casteele T, Würbel H 2020) **Reproducibility of animal research in light of biological variation** _Nature Reviews Neuroscience_ **21** :384–393 https://doi.org/10.1038/s41583 -020-0313-3 

de Vries SEJ, Lecoq JA, Buice MA, Groblewski PA, Ocker GK, Oliver M, Feng D, Cain N, Ledochowitsch P, Millman D, Roll K, Garrett M, Keenan T, Kuan L, Mihalas S, Olsen S, Thompson C, Wakeman W, Waters J, Williams D, et al. 2020) **A large-scale standardized physiological survey reveals functional organization of the mouse visual cortex** _Nature Neuroscience_ **23** :138–151 https://doi.org/10.1038/s41593-019-0550-9 

Waaga T, Agmon H, Normand VA, Nagelhus A, Gardner RJ, Moser MB, Moser EI, Burak Y 2022) **Grid-cell modules remain coordinated when neural activity is dissociated from external sensory cues** _Neuron_ 

Wang Q, Ding SL, Li Y, Royall J, Feng D, Lesnar P, Graddis N, Naeemi M, Facer B, Ho A, Dolbeare T, Blanchard B, Dee N, Wakeman W, Hirokawa KE, Szafer A, Sunkin SM, Oh SW, Bernard A, 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

65 of 89 

Phillips JW, et al. 2020) **The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas** _Cell_ **181** :936–953 https://doi.org/10.1016/j.cell.2020.04.007 

West SJ 2021) **BrainRegister** _GitHub_ 

Zhang LI, Tao HW, Holt CE, Harris WA, Mm Poo 1998) **A critical window for cooperation and competition among developing retinotectal synapses** _Nature_ **395** :37–44 

Zhang Y, Lyu H, Hurwitz C, Wang S, Findling C, Hubert F, Pouget A, Laboratory IB, Varol E, Paninski L 2024) **Exploiting correlations across trials and behavioral sessions to improve neural decoding** _bioRxiv_ 

## **Author information** 

## **International Brain Laboratory** 

Max-Planck-Institute, Tübingen, Germany 

## **Kush Banga** 

University College London, London, United Kingdom 

## **Julius Benson** 

New York University, New York, United States 

## **Jai Bhagat** 

University College London, London, United Kingdom 

## **Dan Biderman** 

Columbia University, New York, United States 

## **Daniel Birman** 

Department of Neurobiology and Biophysics, University of Washington, Seattle, United States 

## **Niccolò Bonacchi** 

William James Center for Research, ISPA - Instituto Universitário, Lisbon, Portugal 

## **Sebastian A Bruijns** 

Max-Planck-Institute, Tübingen, Germany 

## **Kelly Buchanan** 

Columbia University, New York, United States 

## **Robert AA Campbell** 

Sainsbury Wellcome Center, London, United Kingdom 

## **Matteo Carandini** 

University College London, London, United Kingdom 

## **Gaëlle A Chapuis** 

University of Geneva, Geneva, Switzerland 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

66 of 89 

## **Anne K Churchland** 

University of California Los Angeles, Los Angeles, United States ORCID iD: 0000-0002-3205-3794 

**For correspondence:** anne.churchland@internationalbrainlab.org 

## **M Felicia Davatolhagh** 

University of California Los Angeles, Los Angeles, United States ORCID iD: 0000-0002-0607-5164 

## **Hyun Dong Lee** 

Columbia University, New York, United States 

## **Mayo Faulkner** 

University College London, London, United Kingdom 

## **Berk Gerçek** 

University of Geneva, Geneva, Switzerland 

## **Fei Hu** 

University of California, Berkeley, Berkeley, United States 

## **Julia Huntenburg** 

Champalimaud Foundation, Lisbon, Portugal 

## **Cole Hurwitz** 

Columbia University, New York, United States 

## **Anup Khanal** 

University of California Los Angeles, Los Angeles, United States ORCID iD: 0000-0002-8929-7984 

## **Christopher Krasniak** 

Cold Spring Harbor Laboratory, New York, United States 

## **Christopher Langfield** 

Columbia University, New York, United States 

## **Petrina Lau** 

University College London, London, United Kingdom 

## **Nancy Mackenzie** 

Department of Neurobiology and Biophysics, University of Washington, Seattle, United States 

## **Guido T Meijer** 

Champalimaud Foundation, Lisbon, Portugal ORCID iD: 0000-0002-7473-0482 

## **Nathaniel J Miska** 

University College London, London, United Kingdom 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

67 of 89 

## **Zeinab Mohammadi** 

Princeton University, Princeton, United States 

## **Jean-Paul Noel** 

New York University, New York, United States 

## **Liam Paninski** 

Columbia University, New York, United States 

## **Alejandro Pan-Vazquez** 

Princeton University, Princeton, United States 

## **Cyrille Rossant** 

University College London, London, United Kingdom ORCID iD: 0000-0003-2069-9093 

## **Noam Roth** 

Department of Neurobiology and Biophysics, University of Washington, Seattle, United States ORCID iD: 0000-0002-0168-0103 

## **Michael Schartner** 

Champalimaud Foundation, Lisbon, Portugal 

## **Karolina Socha** 

University College London, London, United Kingdom 

## **Nicholas A Steinmetz** 

Department of Neurobiology and Biophysics, University of Washington, Seattle, United States 

## **Karel Svoboda** 

Allen Institute for Neural Dynamics, Seattle, United States 

## **Marsa Taheri** 

University of California Los Angeles, Los Angeles, United States ORCID iD: 0000-0003-2917-9692 

## **Anne E Urai** 

Leiden University, Leiden, Netherlands ORCID iD: 0000-0001-5270-6513 

## **Shuqi Wang** 

School of Computer and Communication Sciences, EPFL, Lausanne, Switzerland 

## **Miles Wells** 

University College London, London, United Kingdom 

## **Steven J West** 

University College London, London, United Kingdom 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

68 of 89 

## **Matthew R Whiteway** 

Columbia University, New York, United States 

## **Olivier Winter** 

Champalimaud Foundation, Lisbon, Portugal 

## **Ilana B Witten** 

Princeton University, Princeton, United States 

## **Yizi Zhang** 

Columbia University, New York, United States 

## **Editors** 

Reviewing Editor 

## **Caleb Kemere** 

Rice University, Houston, United States of America 

Senior Editor 

## **Michael Frank** 

Brown University, Providence, United States of America 

## **Reviewer #1 (Public review):** 

The IBL here presents an important paper that aims to assess potential reproducibility issues in rodent electrophysiological recordings across labs and suggests solutions to these. The authors carried out a series of analyses on data collected across 10 laboratories while mice performed the same decision-making task, and provided convincing evidence that basic electrophysiology features, single-neuron functional properties, and population-level decoding were fairly reproducible across labs with proper preprocessing. This well-motivated large-scale collaboration allowed systematic assessment of lab-to-lab reproducibility of electrophysiological data, and the suggestions outlined in the paper for streamlining preprocessing pipelines and quality metrics will provide general guidance for the field, especially with continued effort to benchmark against standard practices (such as manual curation). 

The authors have carefully incorporated our suggestions. As a result, the paper now better reflects where reproducibility is affected when using common, simple, and more complex analyses and preprocessing methods, and it is more informative-and more reflective of the field overall. We thank the reviewers for this thorough revision. We have 2 remaining suggestions on text clarification: 

(1) Regarding benchmarking the automated metrics to manual curation of units: although we appreciate that a proper comparison may require a lot of effort potentially beyond the scope of the current paper; we do think that explicit discussion regarding this point is needed in the text, to remind the readers (and indeed future generations of electrophysiologists) the pros and cons of different approaches. 

In addition to what the authors have currently stated (line 469-470): "Another significant limitation of the analysis presented here is that we have not been able to assess the extent to which other choices of quality metrics and inclusion criteria might have led to greater or lesser reproducibility." 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

69 of 89 

## Maybe also add: 

"In particular, a thorough comparison of automated metrics against a careful, large, manually-curated dataset, is an important benchmarking step for future studies. 

(2) The authors now include in Figure 3-Figure Supplement 1 that highlight how much probe depth is adjusted by using electrophysiological features such as LFP power to estimate probe and channel depth. This plot is immensely informative for the field, as it implies that there can be substantial variability-sometimes up to 1 mm discrepancy between insertions-in depth estimation based on anatomical DiI track tips alone. Using electrophysiological features in this way for probe depth estimation is currently not standard in the field and has only been made possible with Neuropixels, which span several millimeters. These figures highlight that this should be a critical step in preprocessing pipelines, and the paper provides solid evidence for this. 

Currently, this part of the figure is only subtly referenced to in the text. We think it would be helpful to explicitly reference this particular panel with discussions of its implication in the text. 

https://doi.org/10.7554/eLife.100840.2.sa2 

## **Reviewer #2 (Public review):** 

## Summary: 

The authors sought to evaluate whether analyses of large-scale electrophysiology data obtained from 10 different individual laboratories are reproducible when they use standardized procedures and quality control measures. They were able to reproduce most of their experimental findings across all labs. Despite attempting to target the same brain areas in each recording, variability in electrode targeting was a source of some differences between datasets. 

## Strengths: 

This paper gathered a standardized dataset across 10 labs and performed a host of state-ofthe-art analyses on it. Their ability to assess the reproducibility of each analysis across this kind of data is an important contribution to the field. 

## Comments on revisions: 

The authors have addressed almost all of the concerns that I raised in this revised version. The new RIGOR notebook is helpful, as are the new analyses. 

This paper attributes much error in probe insertion trajectory planning to the fact that the Allen CCF and standard stereotaxic coordinate systems are not aligned. Consequently, it would be very helpful for the community if this paper could recommend software tools, procedures, or code to do trajectory planning that accounts for this. 

I think it would still be helpful for the paper to have some discussion comparing/contrasting the use of the RIGOR framework with existing spike sorting statistics. They mention in their response to reviewers that this is indeed a large space of existing approaches. Most labs performing Neuropixels recordings already do some type of quality control, but these approaches are not standardized. This work is well-positioned to discuss the advantages and disadvantages of these alternative approaches (even briefly) but does not currently do so-it does not need to run any of these competing approaches to helpfully mention ideas for what a reader of the paper should do for quality control with their own data. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

70 of 89 

https://doi.org/10.7554/eLife.100840.2.sa1 

## **Author response:** 

The following is the authors’ response to the original reviews. 

We thank the reviewers and editors for their careful read of our paper, and appreciate the thoughtful comments. 

Both reviewers agreed that our work had several major strengths: the large dataset collected in collaboration across ten labs, the streamlined processing pipelines, the release of code repositories, the multi-task neural network, and that we definitively determined that electrode placement is an important source of variability between datasets. 

However, a number of key potential improvements were noted: the reviewers felt that a more standard model-based characterization of single neuron responses would benefit our reproducibility analysis, that more detail was needed about the number of cells, sessions, and animals, and that more information was needed to allow users to deploy the RIGOR standards and to understand their relationship to other metrics in the field. 

We agree with these suggestions and have implemented many major updates in our revised manuscript. Some highlights include: 

(1) A new regression analysis that specifies the response profile of each neuron, allowing a comparison of how similar these are across labs and areas (See Figure 7 in the new section, “Single neuron coefficients from a regression-based analysis are rep oducible across labs”); 

(2) A new decoding analysis (See Figure 9 in the section, “Decodability of task variables is consistent across labs, but varies by brain region”); 

(3) A new RIGOR notebook to ease useability; 

(4) A wealth of additional information about the cells, animals and sessions in each figure; 

(5) Many new additional figure panels in the main text and supplementary material to clarify the specific points raised by the reviewers. 

Again, we are grateful to the reviewers and editors for their helpful comments, which have significantly improved the work. We are hopeful that the many revisions we have implemented will be sufficient to change the “incomplete” designation that was originally assigned to the manuscript. 

## _**Reviewer #1 (Public review):**_ 

_Summary:_ 

_The authors explore a large-scale electrophysiological dataset collected in 10 labs while mice performed the same behavioral task, and aim to establish guidelines to aid reproducibility of results collected across labs. They introduce a series of metrics for quality control of electrophysiological data and show that histological verification of recording sites is important for interpreting findings across labs and should be reported in addition to planned coordinates. Furthermore, the authors suggest that although basic electrophysiology features were comparable across labs, task modulation of single neurons can be variable, particularly for some brain regions. The authors then use a multi-task neural network model to examine how neural dynamics relate to multiple interacting task- and experimenter-related variables, and find that lab-specific differences contribute little to the variance observed. Therefore, analysis approaches that_ 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

71 of 89 

_account for correlated behavioral variables are important for establishing reproducible results when working with electrophysiological data from animals performing decisionmaking tasks. This paper is very well-motivated and needed. However, what is missing is a direct comparison of task modulation of neurons across labs using standard analysis practice in the fields, such as generalized linear model (GLM). This can potentially clarify how much behavioral variance contributes to the neural variance across labs; and more accurately estimate the scale of the issues of reproducibility in behavioral systems neuroscience, where conclusions often depend on these standard analysis methods._ 

We fully agree that a comparison of task-modulation across labs is essential. To address this, we have performed two new analyses and added new corresponding figures to the main text (Figures 7 and 9). As the reviewer hoped, this analysis did indeed clarify how much behavioral variance contributes to the variance across labs. Critically, these analyses suggested that our results were more robust to reproducibility than the more traditional analyses would indicate. 

Additional details are provided below (See detailed response to R1P1b). 

## _Strengths:_ 

_(1) This is a well-motivated paper that addresses the critical question of reproducibility in behavioural systems neuroscience. The authors should be commended for their efforts._ 

_(2) A key strength of this study comes from the large dataset collected in collaboration across ten labs. This allows the authors to assess lab-to-lab reproducibility of electrophysiological data in mice performing the same decision-making task._ 

_(3) The authors' attempt to streamline preprocessing pipelines and quality metrics is highly relevant in a field that is collecting increasingly large-scale datasets where automation of these steps is increasingly needed._ 

_(4) Another major strength is the release of code repositories to streamline preprocessing pipelines across labs collecting electrophysiological data._ 

_(5) Finally, the application of MTNN for characterizing functional modulation of neurons, although not yet widely used in systems neuroscience, seems to have several advantages over traditional methods._ 

Thanks very much for noting these strengths of our work. 

## _Weaknesses:_ 

_(1) In several places the assumptions about standard practices in the field, including preprocessing and analyses of electrophysiology data, seem to be inaccurately presented:_ 

_a) The estimation of how much the histologically verified recording location differs from the intended recording location is valuable information. Importantly, this paper provides citable evidence for why that is important. However, histological verification of recording sites is standard practice in the field, even if not all studies report them. Although we appreciate the authors' effort to further motivate this practice, the current description in the paper may give readers outside the field a false impression of the level of rigor in the field._ 

We agree that labs typically do perform histological verification. Still, our methods offer a substantial improvement over standard practice, and this was critical in allowing us to identify errors in targeting. For instance, we used new software, LASAGNA, which is an 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

72 of 89 

innovation over the traditional, more informal approach to localizing recording sites. Second, the requirement that two independent reviewers concur on each proposed location for a recording site is also an improvement over standard practice. Importantly, these reviewers use electrophysiological features to more precisely localize electrodes, when needed, which is an improvement over many labs. Finally, most labs use standard 2D atlases to identify recording location (a traditional approach); our use of a 3D atlas and a modern image registration pipeline has improved the accuracy of identifying the true placement of probes in 3D space. 

Importantly, we don’t necessarily advocate that all labs adopt our pipeline; indeed, this would be infeasible for many labs. Instead, our hope is that the variability in probe trajectory that we uncovered will be taken into account in future studies. Here are 3 example ways in which that could happen. First, groups hoping to target a small area for an experiment might elect to use a larger cohort than previously planned, knowing that some insertions will miss their target. Second, our observation that some targeting error arose because experimenters had to move probes due to blood vessels will impact future surgeries: when an experimenter realizes that a blood vessel is in the way, they might still re-position the probe, but they can also adjust its trajectory (e.g., changing the angle) knowing that even little nudges to avoid blood vessels can have a large impact on the resulting insertion trajectory. Third, our observation of a 7 degree deviation between stereotaxic coordinates and Allen Institute coordinates can be used for future trajectory planning steps to improve accuracy of placement. Uncovering this deviation required many insertions and our standardized pipeline, but now that it is known, it can be easily corrected without needing such a pipeline. 

We thank the reviewer for bringing up this issue and have added new text (and modified existing text) in the Discussion to highlight the innovations we introduced that allowed us to carefully quantify probe trajectory across labs (lines 500 - 515): 

“Our ability to detect targeting error benefited from an automated histological pipeline combined with alignment and tracing that required agreement between multiple users, an approach that greatly exceeds the histological analyses done by most individual labs. Our approach, which enables scalability and standardization across labs while minimizing subjective variability, revealed that much of the variance in targeting was due to the probe entry positions at the brain surface, which were randomly displaced across the dataset. … Detecting this offset relied on a large cohort size and an automated histological pipeline, but now that we have identified the offset, it can be easily accounted for by any lab. Specifically, probe angles must be carefully computed from the CCF, as the CCF and stereotaxic coordinate systems do not define the same coronal plane angle. Minimizing variance in probe targeting is another important element in increasing reproducibility, as slight deviations in probe entry position and angle can lead to samples from different populations of neurons. Collecting structural MRI data in advance of implantation could reduce targeting error, although this is infeasible for most labs. A more feasible solution is to rely on stereotaxic coordinates but account for the inevitable off-target measurements by increasing cohort sizes and adjusting probe angles when blood vessels obscure the desired location.” 

_b) When identifying which and how neurons encode particular aspects of stimuli or behaviour in behaving animals (when variables are correlated by the nature of the animals behaviour), it has become the standard in behavioral systems neuroscience to use GLMs - indeed many labs participating in the IBL also has a long history of doing this (e.g., Steinmetz et al., 2019; Musall et al., 2023; Orsolic et al., 2021; Park et al., 2014). The reproducibility of results when using GLMs is never explicitly shown, but the supplementary figures to Figure 7 indicate that results may be reproducible across labs when using GLMs (as it has similar prediction performance to the MTNN). This should be introduced as the first analysis method used in a new dedicated figure (i.e., following Figure 3 and showing results of analyses similar to what was shown for the MTNN in_ 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

73 of 89 

_Figure 7). This will help put into perspective the degree of reproducibility issues the field is facing when analyzing with appropriate and common methods. The authors can then go on to show how simpler approaches (currently in Figures 4 and 5) - not accounting for a lot of uncontrolled variabilities when working with behaving animals - may cause reproducibility issues._ 

We fully agree with the reviewer's suggestion. We have addressed their concern by implementing a Reduced-Rank Regression (RRR) model, which builds upon and extends the principles of Generalized Linear Models (GLMs). The RRR model retains the core regression framework of GLMs while introducing shared, _trainable_ temporal bases across neurons, enhancing the model’s capacity to capture the structure in neural activity (Posani, Wang, et al., bioRxiv, 2024). Importantly, Posani, Wang et al compared the predictive performance of GLMs vs the RRR model, and found that the RRR model provided (slightly) improved performance, so we chose the RRR approach here. 

We highlight this analysis in a new section (lines 350-377) titled, “Single neuron coefficients from a regression-based analysis are reproducible across labs”. This section includes an entirely new Figure (Fig. 7), where this new analysis felt most appropriate, since it is closer in spirit to the MTNN analysis that follows (rather than as a new Figure 3, as the reviewer suggested). As the reviewer hoped, this analysis provides some reassurance that including many variables when characterizing neural activity furnishes results with improved reproducibility. We now state this in the Results and the Discussion (line 456-457), highlighting that these analyses complement the more traditional selectivity analyses, and that using both methods together can be informative. 

_When the authors introduce a neural network approach (i.e. MTNN) as an alternative to the analyses in Figures 4 and 5, they suggest: 'generalized linear models (GLMs) are likely too inflexible to capture the nonlinear contributions that many of these variables, including lab identity and spatial positions of neurons, might make to neural activity'). This is despite the comparison between MTNN and GLM prediction performance (Supplement 1 to Figure 7) showing that the MTNN is only slightly better at predicting neural activity compared to standard GLMs. The introduction of new models to capture neural variability is always welcome, but the conclusion that standard analyses in the field are not reproducible can be unfair unless directly compared to GLMs._ 

_In essence, it is really useful to demonstrate how different analysis methods and preprocessing approaches affect reproducibility. But the authors should highlight what is actually standard in the field, and then provide suggestions to improve from there._ 

Thanks again for these comments. We have also edited the MTNN section slightly to accommodate the addition of the previous new RRR section (line 401-402). 

_(2) The authors attempt to establish a series of new quality control metrics for the inclusion of recordings and single units. This is much needed, with the goal to standardize unit inclusion across labs that bypasses the manual process while keeping the nuances from manual curation. However, the authors should benchmark these metrics to other automated metrics and to manual curation, which is still a gold standard in the field. The authors did this for whole-session assessment but not for individual clusters. If the authors can find metrics that capture agreed-upon manual cluster labels, without the need for manual intervention, that would be extremely helpful for the field._ 

We thank the reviewer for their insightful suggestions regarding benchmarking our quality control metrics against manual curation and other automated methods at the level of individual clusters. We are indeed, as the reviewer notes, publishing results from spike 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

74 of 89 

sorting outputs that have been automatically but not manually verified on a neuron-byneuron basis. To get to the point where we trust these results to be of publishable quality, we manually reviewed hundreds of recordings and thousands of neurons, refining both the preprocessing pipeline and the single-unit quality metrics along the way. All clusters, both those passing QCs and those not passing QCs, are available to review with detailed plots and quantifications at https://viz.internationalbrainlab.org/app (turn on “show advanced metrics” in the upper right, and navigate to the plots furthest down the page, which are at the individual unit level). We would emphasize that these metrics are definitely imperfect (and fully-automated spike sorting remains a work in progress), but so is manual clustering. Our fully automated approach has the advantage of being fully reproducible, which is absolutely critical for the analyses in the present paper. Indeed, if we had actually done manual clustering or curation, one would wonder whether our results were actually reproducible independently. Nevertheless, it is not part of the present manuscript’s objectives to validate or defend these specific choices for automated metrics, which have been described in detail elsewhere (see our Spike Sorting whitepaper, https://figshare.com/articles/online_resource /Spike_sorting_pipeline_for_the_International_Brain_La boratory/19705522?file=49783080). It would be a valuable exercise to thoroughly compare these metrics against a careful, large, manually-curated set, but doing this properly would be a paper in itself and is beyond the scope of the current paper. We also acknowledge that our analyses studying reproducibility across labs could, in principle, result in more or less reproducibility under a different choice of metrics, which we now describe in the Discussion (line 469-470)”: 

“Another significant limitation of the analysis presented here is that we have not been able to assess the extent to which other choices of quality metrics and inclusion criteria might have led to greater or lesser reproducibility.” 

_(3) With the goal of improving reproducibility and providing new guidelines for standard practice for data analysis, the authors should report of n of cells, sessions, and animals used in plots and analyses throughout the paper to aid both understanding of the variability in the plots - but also to set a good example._ 

We wholeheartedly agree and have added the number of cells, mice and sessions for each figure. This information is included as new tabs in our quality control spreadsheet (https:// docs.google.com/spreadsheets/d/1_bJLDG0HNLFx3SOb4GxLxL52H4R2uPRcpUlIw6n4 n-E/). This is referred to in line 158-159 (as well as its original location on line 554 in the section, “Quality control and data inclusion”). 

_Other general comments:_ 

_(1) In the discussion (line 383) the authors conclude: 'This is reassuring, but points to the need for large sample sizes of neurons to overcome the inherent variability of single neuron recording'. - Based on what is presented in this paper we would rather say that their results suggest that appropriate analytical choices are needed to ensure reproducibility, rather than large datasets - and they need to show whether using standard GLMs actually allows for reproducible results._ 

Thanks. The new GLM-style RRR analysis in Figure 7, following the reviewer’s suggestion, does indeed indicate improved reproducibility across labs. As described above, we see this new analysis as complementary to more traditional analyses of neural selectivity and argue that the two can be used together. The new text (line 461) states: 

“This is reassuring, and points to the need for appropriate analytical choices to ensure reproducibility.” 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

75 of 89 

_(2) A general assumption in the across-lab reproducibility questions in the paper relies on intralab variability vs across-lab variability. An alternative measure that may better reflect experimental noise is across-researcher variability, as well as the amount of experimenter experience (if the latter is a factor, it could suggest researchers may need more training before collecting data for publication). The authors state in the discussion that this is not possible. But maybe certain measures can be used to assess this (e.g. years of conducting surgeries/ephys recordings etc)?_ 

We agree that understanding experimenter-to-experimenter variability would be very interesting and indeed we had hoped to do this analysis for some time. The problem is that typically, each lab employed one trainee to conduct all the data collection. This prevents us from comparing outcomes from two different experimenters in the same lab. There are exceptions to this, such as the Churchland lab in which 3 personnel (two postdocs and a technician) collected the data. However, even this fortuitous situation did not lend itself well to assessing experimenter-to-experimenter variation: the Churchland lab moved from Cold Spring Harbor to UCLA during the data collection period, which might have caused variability that is totally independent of experimenter (e.g., different animal facilities). Further, once at UCLA, the postdoc and technician worked closely together- alternating roles in animal training, surgery and electrophysiology. We believe that the text in our current Discussion (line 465-468) accurately characterizes the situation: 

“Our experimental design precludes an analysis of whether the reproducibility we observed was driven by person-to-person standardization or lab-to-lab standardization. Most likely, both factors contributed: all lab personnel received standardized instructions for how to implant head bars and train animals, which likely reduced personnel-driven differences.” 

Quantifying the level of experience of each experimenter is an appealing idea and we share the reviewer’s curiosity about its impact on data quality. Unfortunately, quantifying experience is tricky. For instance, years of conducting surgeries is not an unambiguously determinable number. Would we count an experimenter who did surgery every day for a year as having the same experience as an experimenter who did surgery once/month for a year? Would we count a surgeon with expertise in other areas (e.g., windows for imaging) in the same way as surgeons with expertise in ephys-specific surgeries? Because of the ambiguities, we leave this analysis to be the subject of future work; this is now stated in the Discussion (line 476). 

_(3) Figure 3b and c: Are these plots before or after the probe depth has been adjusted based on physiological features such as the LFP power? In other words, is the IBL electrophysiological alignment toolbox used here and is the reliability of location before using physiological criteria or after? Beyond clarification, showing both before and after would help the readers to understand how much the additional alignment based on electrophysiological features adjusts probe location. It would also be informative if they sorted these penetrations by which penetrations were closest to the planned trajectory after histological verification._ 

The plots in Figure 3b and 3c reflect data _after_ the probe depth has been adjusted based on electrophysiological features. This adjustment incorporates criteria such as LFP power and spiking activity to refine the trajectory and ensure precise alignment with anatomical landmarks. The trajectories have also been reviewed and confirmed by two independent reviewers. We have clarified this in line 180 and in the caption of Figure 3. 

To address this concern, we have added a new panel c in Figure 3 supplementary 1 (also shown below) that shows the LFP features along the probes prior to using the IBL alignment 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

76 of 89 

toolbox. We hope the reviewer agrees that a comparison of panels (a) and (c) below make clear the improvement afforded by our alignment tools. 

In Figure 3 and Figure 3 supplementary 1, as suggested, we have also now sorted the probes by those that were closest to the planned trajectory. This way of visualizing the data makes it clear that as the distance from the planned trajectory increases, the power spectral density in the hippocampal regions becomes less pronounced and the number of probes that have a large portion of the channels localized to VISa/am, LP and PO decreases. We have added text to the caption to describe this. We thank the reviewer for this suggestion and agree that it will help readers to understand how much the additional alignment (based on electrophysiological features) adjusts probe location. 

_(4) In Figures 4 and 6: If the authors use a 0.05 threshold (alpha) and a cell simply has to be significant on 1/6 tests to be considered task modulated, that means that they have a false positive rate of ~30% (0.05*6=0.3). We ran a simple simulation looking for significant units (from random null distribution) from these criteria which shows that out of 100.000 units, 26500 units would come out significant (false error rate: 26.5%). That is very high (and unlikely to be accepted in most papers), and therefore not surprising that the fraction of task-modulated units across labs is highly variable. This high false error rate may also have implications for the investigation of the spatial position of taskmodulated units (as effects of the spatial position may drown in falsely labelled 'taskmodulated' cells)._ 

Thank you for this concern. The different tests were kept separate, so we did not consider a neuron modulated if it was significant in only one out of six tests, but instead we asked whether a neuron was modulated according to test one, whether it was modulated according to test two, etc., and performed further analyses separately for each test. Thus, we are only vulnerable to the ‘typical’ false positive rate of 0.05 for any given test. We made this clearer in the text (lines 232-236) and hope that the 5% false positive rate seems more acceptable. 

_(5) The authors state from Figure 5b that the majority of cells could be well described by 2 PCs. The distribution of R2 across neurons is almost uniform, so depending on what R2 value one considers a 'good' description, that is the fraction of 'good' cells. Furthermore, movement onset has now been well-established to be affecting cells widely and in large fractions, so while this analysis may work for something with global influence - like movement - more sparsely encoded variables (as many are in the brain) may not be well approximated with this suggestion. The authors could expand this analysis into other epochs like activity around stimulus presentation, to better understand how this type of analysis reproduces across labs for features that have a less global influence._ 

We thank the reviewer for the suggestion and fully agree that the window used in our original analysis would tend to favor movement-driven neurons. To address this, we repeated the analysis, this time using a window centered around stimulus onset (from -0.5 s prior to stimulus onset until 0.1 s after stimulus onset). As the reviewer suspected, far fewer neurons were active in this window and consequently far fewer were modelled well by the first two PCs, as shown in Author response image 1b (below). Similar to our original analysis using the post-movement window, we found mixed results for the stimulus-centered window across labs. Interestingly, regional differences were weaker in this new analysis compared to the original analysis of the post-movement window. We have added a sentence to the results describing this. Because the results are similar to the post-movement window main figure, we would prefer to restrict the new analysis only to this point-by-point response, in the hopes of streamlining the paper. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

77 of 89 

## **Author response image 1.** 

PCA analysis applied to a stimulus-aligned window ([-0.5, 0.1] sec relative to stim onset). Figure conventions as in main text Fig 5. Results are comparable to the post-movement window analysis, however regional differences are weaker here, possibly because fewer cells were active in the pre-movement window. We added panel j here and in the main figure, showing cell-number-controlled results. I.e. for each test, the minimum neuron number of the compared classes was sampled from all classes (say labs in a region), this sampling was repeated 1000 times and p-values combined via Fisher’s method, overall resulting in much fewer significant differences across laboratories and, independently, regions. 

**==> picture [403 x 362] intentionally omitted <==**

_(6) Additionally, in Figure 5i: could the finding that one can only distinguish labs when taking cells from all regions, simply be a result of a different number of cells recorded in each region for each lab? It makes more sense to focus on the lab/area pairing as the authors also do, but not to make their main conclusion from it. If the authors wish to do the comparison across regions, they will need to correct for the number of cells recorded in each region for each lab. In general, it was a struggle to fully understand the purpose of Figure 5. While population analysis and dimensionality reduction are commonplace, this seems to be a very unusual use of it._ 

We agree that controlling for varying cell numbers is a valuable addition to this analysis. We added panel j in Fig. 5 showing cell-number-controlled test results of panel i. I.e. for a given statistical comparison, we sample the lowest number of cells of compared classes from the 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

78 of 89 

others, do the test, and repeat this sampling 1000 times, before combining the p-values using Fisher’s method. This cell-number controlled version of the tests resulted in clearly fewer significant differences across distributions - seen similarly for the pre-movement window shown in j in Author response image 1. We hope this clarified our aim to illustrate that lowdimensional embedding of cells’ trial-averaged activity can show how regional differences compare with laboratory differences. 

As a complementary statistical analysis to the shown KS tests, we fitted a linear-mixed-effects model (statsmodels.formula.api mixedlm), to the first and second PC for both activity windows (“Move”: [-0.5,1] first movement aligned; “Stim”: [-0.5,0.1] stimulus onset aligned), independently. Author response image 2 (in this rebuttal only) is broadly in line with the KS results, showing more regional than lab influences on the distributions of first PCs for the post-movement window. 

## **Author response image 2:** 

Linear mixed effects model results for two PCs and two activity windows. For the postmovement window (“Move”), regional influences are significant (red color in plots) for all but one region while only one lab has a significant model coefficient for PC1. For PC2 more labs and three regions have significant coefficients. For the pre-movement window (“Stim”) one region for PC1 or PC2 has significant coefficients. The variance due to session id was smaller than all other effects (“eids Var”). “Intercept” shows the expected value of the response variable (PC1, PC2) before accounting for any fixed or random effects. All p-values were grouped as one hypothesis family and corrected for multiple comparisons via BenjaminiHochberg. 

**==> picture [136 x 57] intentionally omitted <==**

_(7) In the discussion the authors state: " Indeed this approach is a more effective and streamlined way of doing it, but it is questionable whether it 'exceeds' what is done in many labs._ 

_Classically, scientists trace each probe manually with light microscopy and designate each area based on anatomical landmarks identified with nissl or dapi stains together with gross landmarks. When not automated with 2-PI serial tomography and anatomically aligned to a standard atlas, this is a less effective process, but it is not clear that it is less precise, especially in studies before neuropixels where active electrodes were located in a much smaller area. While more effective, transforming into a common atlas does make additional assumptions about warping the brain into the standard atlas - especially in cases where the brain has been damaged/lesioned. Readers can appreciate the effectiveness and streamlining provided by these new tools without the need to invalidate previous approaches._ 

We thank the reviewer for highlighting the effectiveness of manual tracing methods used traditionally. Our intention in the statement was not to invalidate the precision or value of these classical methods but rather to emphasize the scalability and streamlining offered by our pipeline. We have revised the language to more accurately reflect this (line 500-504): 

“Our ability to detect targeting error benefited from an automated histological pipeline combined with alignment and tracing that required agreement between multiple users, an approach that greatly exceeds the histological analyses done by most individual labs. Our 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

79 of 89 

approach, which enables scalability and standardization across labs while minimizing subjective variability, revealed that much of the variance in targeting was due to the probe entry positions at the brain surface, which were randomly displaced across the dataset.” 

_(8) What about across-lab population-level representation of task variables, such as in the coding direction for stimulus or choice? Is the general decodability of task variables from the population comparable across labs?_ 

Excellent question, thanks! We have added the new section “Decodability of task variables is consistent across labs, but varies by brain region” (line 423-448) and Figure 9 in the revised manuscript to address this question. In short, yes, the general decodability of task variables from the population is comparable across labs, providing additional reassurance of reproducibility. 

## _**Reviewer #2 (Public review):**_ 

_Summary:_ 

_The authors sought to evaluate whether observations made in separate individual laboratories are reproducible when they use standardized procedures and quality control measures. This is a key question for the field. If ten systems neuroscience labs try very hard to do the exact same experiment and analyses, do they get the same core results? If the answer is no, this is very bad news for everyone else! Fortunately, they were able to reproduce most of their experimental findings across all labs. Despite attempting to target the same brain areas in each recording, variability in electrode targeting was a source of some differences between datasets._ 

_Major Comments:_ 

_The paper had two principal goals:_ 

_(1) to assess reproducibility between labs on a carefully coordinated experiment_ 

_(2) distill the knowledge learned into a set of standards that can be applied across the field._ 

_The manuscript made progress towards both of these goals but leaves room for improvement._ 

_(1) The first goal of the study was to perform exactly the same experiment and analyses across 10 different labs and see if you got the same results. The rationale for doing this was to test how reproducible large-scale rodent systems neuroscience experiments really are. In this, the study did a great job showing that when a consortium of labs went to great lengths to do everything the same, even decoding algorithms could not discern laboratory identity was not clearly from looking at the raw data. However, the amount of coordination between the labs was so great that these findings are hard to generalize to the situation where similar (or conflicting!) results are generated by two labs working independently._ 

_Importantly, the study found that electrode placement (and thus likely also errors inherent to the electrode placement reconstruction pipeline) was a key source of variability between datasets. To remedy this, they implemented a very sophisticated electrode reconstruction pipeline (involving two-photon tomography and multiple blinded data validators) in just one lab-and all brains were sliced and reconstructed in this one location. This is a fantastic approach for ensuring similar results within the IBL collaboration, but makes it unclear how much variance would have been observed if each lab had attempted to reconstruct their probe trajectories themselves using a mix of_ 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

80 of 89 

_histology techniques from conventional brain slicing, to light sheet microscopy, to MRI imaging._ 

_This approach also raises a few questions. The use of standard procedures, pipelines, etc. is a great goal, but most labs are trying to do something unique with their setup. Bigger picture, shouldn't highly "significant" biological findings akin to the discovery of place cells or grid cells, be so clear and robust that they can be identified with different recording modalities and analysis pipelines?_ 

We agree, and hope that this work may help readers understand what effect sizes may be considered “clear and robust” from datasets like these. We certainly support the reviewer’s point that multiple approaches and modalities can help to confirm any biological findings, but we would contend that a clear understanding of the capabilities and limitations of each approach is valuable, and we hope that our paper helps to achieve this. 

_Related to this, how many labs outside of the IBL collaboration have implemented the IBL pipeline for their own purposes? In what aspects do these other labs find it challenging to reproduce the approaches presented in the paper? If labs were supposed to perform this same experiment, but without coordinating directly, how much more variance between labs would have been seen? Obviously investigating these topics is beyond the scope of this paper. The current manuscript is well-written and clear as is, and I think it is a valuable contribution to the field. However, some additional discussion of these issues would be helpful._ 

We thank the reviewer for raising this important issue. We know of at least 13 labs that have implemented the behavioral task software and hardware that we published in eLife in 2021, and we expect that over the next several years labs will also implement these analysis pipelines (note that it is considerably cheaper and faster to implement software pipelines than hardware). In particular, a major goal of the staff in the coming years is to continue and improve the support for pipeline deployment and use. However, our goal in this work, which we have aimed to state more clearly in the revised manuscript, was not so much to advocate that others adopt our pipeline, but instead to use our standardized approach as a means of assessing reproducibility under the best of circumstances (see lines 48-52): “A high level of reproducibility of results across laboratories when procedures are carefully matched is a prerequisite to reproducibility in the more common scenario in which two investigators approach the same high-level question with slightly different experimental protocols.” 

Further, a number of our findings are relevant to other labs regardless of whether they implement our exact pipeline, a modified version of our pipeline, or something else entirely. For example, we found probe targeting to be a large source of variability. Our ability to detect targeting error benefited from an automated histological pipeline combined with alignment and tracing that required agreement between multiple users, but now that we have identified the offset, it can be easily accounted for by any lab. Specifically, probe angles must be carefully computed from the CCF, as the CCF and stereotaxic coordinate systems do not define the same coronal plane angle. Relatedly, we found that slight deviations in probe entry position can lead to samples from different populations of neurons. Although this took large cohort sizes to discover, knowledge of this discovery means that future experiments can plan for larger cohort sizes to allow for off-target trajectories, and can re-compute probe angle when the presence of blood vessels necessitates moving probes slightly. These points are now highlighted in the Discussion (lines 500-515). 

Second, the proportion of responsive neurons (a quantity often used to determine that a particular area subserves a particular function), sometimes failed to reproduce across labs. For example, for movement-driven activity in PO, UCLA reported an average change of 0 spikes/s, while CCU reported a large and consistent change (Figure 4d, right most panel, 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

81 of 89 

compare orange vs. yellow traces). This argues that neuron-to-neuron variability means that comparisons across labs require large cohort sizes. A small number of outlier neurons in a session can heavily bias responses. We anticipate that this problem will be remedied as tools for large scale neural recordings become more widely used. Indeed, the use of 4-shank instead of single-shank Neuropixels (as we used here) would have greatly enhanced the number of PO neurons we measured in each session. We have added new text to Results explaining this (lines 264-268): 

“We anticipate that the feasibility of even larger scale recordings will make lab-to-lab comparisons easier in future experiments; multi-shank probes could be especially beneficial for cortical recordings, which tend to be the most vulnerable to low cell counts since the cortex is thin and is the most superficial structure in the brain and thus the most vulnerable to damage. Analyses that characterize responses to multiple parameters are another possible solution (See Figure 7).” 

_(2) The second goal of the study was to present a set of data curation standards (RIGOR) that could be applied widely across the field. This is a great idea, but its implementation needs to be improved if adoption outside of the IBL is to be expected. Here are three issues:_ 

_(a) The GitHub repo for this project (https://github.com/int-brain-lab/paper-reproducibleephys/) is nicely documented if the reader's goal is to reproduce the figures in the manuscript. Consequently, the code for producing the RIGOR statistics seems mostly designed for re-computing statistics on the existing IBL-formatted datasets. There doesn't appear to be any clear documentation about how to run it on arbitrary outputs from a spike sorter (i.e. the inputs to Phy)._ 

We agree that clear documentation is key for others to adopt our standards. To address this, we have added a section at the end of the README of the repository that links to a jupyter notebook (https://github.com/int-brain-lab/paper-reproducible-ephys/blob/master/RIGOR _script.ipynb) that runs the RIGOR metrics on a user’s own spike sorted dataset. The notebook also contains a tutorial that walks through how to visually assess the quality of the raw and spike sorted data, and computes the noise level metrics on the raw data as well as the single cell metrics on the spike sorted data. 

_(b) Other sets of spike sorting metrics that are more easily computed for labs that are not using the IBL pipeline already exist (e.g. "quality_metrics" from the Allen Institute ecephys pipeline [https://github.com/AllenInstitute/ecephys_spike_sorting/blob/main/ecephys _spike_sorting/m odules/quality_metrics/README.md] and the similar module in the Spike Interface package [https://spikeinterface.readthedocs.io/en/latest/modules /qualitymetrics.html]). The manuscript does not compare these approaches to those proposed here, but some of the same statistics already exist (amplitude cutoff, median spike amplitude, refractory period violation)._ 

There is a long history of researchers providing analysis algorithms and code for spike sorting quality metrics, and we agree that the Allen Institute’s ecephys code and the Spike Interface package are the current options most widely used (but see also, for example, Fabre et al. https://github.com/Julie-Fabre/bombcell). Our primary goal in the present work is not to advocate for a particular implementation of any quality metrics (or any spike sorting algorithm, for that matter), but instead to assess reproducibility of results, given one specific choice of spike sorting algorithm and quality metrics. That is why, in our comparison of yield across datasets (Fig 1F), we downloaded the raw data from those comparison datasets and reran them under our single fixed pipeline, to establish a fair standard of comparison. A full comparison of the analyses presented here under different choices of quality metrics and spike sorting algorithms would undoubtedly be interesting and useful for the field - however, 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

82 of 89 

we consider it to be beyond the scope of the present work. It is therefore an important assumption of our work that the result would not differ materially under a different choice of sorting algorithm and quality metrics. We have added text to the Discussion to clarify this limitation: 

“Another significant limitation of the analysis presented here is that we have not been able to assess the extent to which other choices of quality metrics and inclusion criteria might have led to greater or lesser reproducibility.” 

That said, we still intend for external users to be able to easily run our pipelines and quality metrics. 

_(c) Some of the RIGOR criteria are qualitative and must be visually assessed manually. Conceptually, these features make sense to include as metrics to examine, but would ideally be applied in a standardized way across the field. The manuscript doesn't appear to contain a detailed protocol for how to assess these features. A procedure for how to apply these criteria for curating non-IBL data (or for implementing an automated classifier) would be helpful._ 

We agree. To address this, we have provided a notebook that runs the RIGOR metrics on a user’s own dataset, and contains a tutorial on how to interpret the resulting plots and metrics (https://github.com/int-brain-lab/paper-reproducible-ephys/blob/master/RIGOR_script.ipynb). 

Within this notebook there is a section focused on visually assessing the quality of both the raw data and the spike sorted data. The code in this section can be used to generate plots, such as raw data snippets or the raster map of the spiking activity, which are typically used to visually assess the quality of the data. In Figure 1 Supplement 2 we have provided examples of such plots that show different types of artifactual activity that should be inspected. 

_Other Comments:_ 

_(1) How did the authors select the metrics they would use to evaluate reproducibility? Was this selection made before doing the study?_ 

Our metrics were selected on the basis of our experience and expertise with extracellular electrophysiology. For example: some of us previously published on epileptiform activity and its characteristics in some mice (Steinmetz et al. 2017), so we included detection of that type of artifact here; and, some of us previously published detailed investigations of instability in extracellular electrophysiological recordings and methods for correcting them (Steinmetz et al. 2021, Windolf et al. 2024), so we included assessment of that property here. These metrics therefore represent our best expert knowledge about the kinds of quality issues that can affect this type of dataset, but it is certainly possible that future investigators will discover and characterize other quality issues. 

The selection of metrics was primarily performed before the study (we used these assessments internally before embarking on the extensive quantifications reported here), and in cases where we refined them further during the course of preparing this work, it was done without reference to statistical results on reproducibility but instead on the basis of manual inspection of data quality and metric performance. 

_(2) Was reproducibility within-lab dependent on experimenter identity?_ 

We thank the reviewer for this question. We have addressed it in our response to R1 General comment 2, as follows: 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

83 of 89 

We agree that understanding experimenter-to-experimenter variability would be very interesting and indeed we had hoped to do this analysis for some time. The problem is that typically, each lab employed one trainee to conduct all the data collection. This prevents us from comparing outcomes from two different experimenters in the same lab. There are exceptions to this, such as the Churchland lab in which 3 personnel (two postdocs and a technician) collected the data. However, even this fortuitous situation did not lend itself well to assessing experimenter-to-experimenter variation: the Churchland lab moved from Cold Spring Harbor to UCLA during the data collection period, which might have caused variability that is totally independent of experimenter (e.g., different animal facilities). Further, once at UCLA, the postdoc and technician worked closely together- alternating roles in animal training, surgery and electrophysiology. We believe that the text in our current Discussion (line 465-468) accurately characterizes the situation: 

_“Our experimental design precludes an analysis of whether the reproducibility we observed was driven by person-to-person standardization or lab-to-lab standardization. Most likely, both factors contributed: all lab personnel received standardized instructions for how to implant head bars and train animals, which likely reduced personnel-driven differences.”_ 

Quantifying the level of experience of each experimenter is an appealing idea and we share the reviewer’s curiosity about its impact on data quality. Unfortunately, quantifying experience is tricky. For instance, years of conducting surgeries is not an unambiguously determinable number. Would we count an experimenter who did surgery every day for a year as having the same experience as an experimenter who did surgery once/month for a year? Would we count a surgeon with expertise in other areas (e.g., windows for imaging) in the same way as surgeons with expertise in ephys-specific surgeries? Because of the ambiguities, we leave this analysis to be the subject of future work; this is now stated in the Discussion (line 476). 

_(3) They note that UCLA and UW datasets tended to miss deeper brain region targets (lines 185-188) - they do not speculate why these labs show systematic differences. Were they not following standardized procedures?_ 

Thank you for raising this point. All researchers across labs were indeed following standardised procedures. We note that our statistical analysis of probe targeting coordinates and angles did not reveal a significant effect of lab identity on targeting error, even though we noted the large number of mis-targeted recordings in UCLA and UW to help draw attention to the appropriate feature in the figure. Given that these differences were not statistically significant, we can see how it was misleading to call out these two labs specifically. While the overall probe placement surface error and angle error both show no such systematic difference, the magnitude of surface error showed a non-significant tendency to be higher for samples in UCLA & UW, which, compounded with the direction of probe angle error, caused these probe insertions to land in a final location outside LP & PO. 

This shows how subtle differences in probe placement & angle accuracy can lead to compounded inaccuracies at the probe tip, especially when targeting deep brain regions, even when following standard procedures. We believe this is driven partly by the accuracy limit or resolution of the stereotaxic system, along with slight deviations in probe angle, occurring during the setup of the stereotaxic coordinate system during these recordings. 

We have updated the relevant text in lines 187-190 as follows, to clarify: 

“Several trajectories missed their targets in deeper brain regions (LP, PO), as indicated by gray blocks, despite the lack of significant lab-dependent effects in targeting as reported above. These off-target trajectories tended to have both a large displacement from the target 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

84 of 89 

insertion coordinates and a probe angle that unfavorably drew the insertions away from thalamic nuclei (Figure 2f).” 

_(4) The authors suggest that geometrical variance (difference between planned and final identified probe position acquired from reconstructed histology) in probe placement at the brain surface is driven by inaccuracies in defining the stereotaxic coordinate system, including discrepancies between skull landmarks and the underlying brain structures. In this case, the use of skull landmarks (e.g. bregma) to determine locations of brain structures might be unreliable and provide an error of ~360 microns. While it is known that there is indeed variance in the position between skull landmarks and brain areas in different animals, the quantification of this error is a useful value for the field._ 

We thank the reviewer for their thoughtful comment and are glad that they found the quantification of variance useful for the field. 

_(5) Why are the thalamic recording results particularly hard to reproduce? Does the anatomy of the thalamus simply make it more sensitive to small errors in probe positioning relative to the other recorded areas?_ 

We thank the reviewer for raising this interesting question. We believe that they are referring to Figure 4: indeed when we analyzed the distribution of firing rate modulations, we saw some failures of reproducibility in area PO (bottom panel, Figure 4h). However, the thalamic nuclei were not, in other analyses, more vulnerable to failures in reproducibility. For example, in the top panel of Figure 4h, VisAM shows failures of reproducibility for modulation by the visual stimulus. In Fig. 5i, area CA1 showed a failure of reproducibility. We fear that the figure legend title in the previous version (which referred to the thalamus specifically) was misleading, and we have revised this. The new title is, “Neural activity is modulated during decision-making in five neural structures and is variable between laboratories.” This new text more accurately reflects that there were a number of small, idiosyncratic failures of reproducibility, but that these were not restricted to a specific structure. The new analysis requested by R1 (now in Figure 7) provides further reassurance of overall reproducibility, including in the thalamus (see Fig. 7a, right panels; lab identity could not be decoded from single neuron metrics, even in the thalamus). 

## _**Reviewer #1 (Recommendations for the authors):**_ 

_(1) Figure font sizes and formatting are variable across panels and figures. Please streamline the presentation of results._ 

Thank you for your feedback. We have remade all figures with the same standardized font sizes and formatting. 

_(2) Please correct the noncontinuous color scales in Figures 3b and 3d._ 

Thank you for pointing this out, we fixed the color bar. 

_(3) In Figures 5d and g, the error bars are described as: 'Error bands are standard deviation across cells normalised by the square root of the number of sessions in the region'. How does one interpret this error? It seems to be related to the standard error of the mean (std/sqrt(n)) but instead of using the n from which the standard deviation is calculated (in this case across cells), the authors use the number of sessions as n. If they took the standard deviation across sessions this would be the sem across sessions, and interpretable (as sem*1.96 is the 95% parametric confidence interval of the mean)._ 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

85 of 89 

_Please justify why these error bands are used here and how they can be interpreted - it also seems like it is the only time these types of error bands are used._ 

We agree and for clarity use standard error across cells now, as the error bars do not change dramatically either way. 

_(4) It is difficult to understand what is plotted in Figures 5e,h, please unpack this further and clarify._ 

Thank you for pointing this out. We have added additional explanation in the figure caption (See caption for Figure 5c) to explain the KS test. 

_(5) In lines 198-201 the authors state that they were worried that Bonferroni correction with 5 criteria would be too lenient, and therefore used 0.01 as alpha. I am unsure whether the authors mean that they are correcting for multiple comparisons across features or areas. Either way, 0.01 alpha is exactly what a Bonferroni corrected alpha would be when correcting for either 5 features or 5 areas: 0.05/5=0.01. Or do they mean they apply the Bonferroni correction to the new 0.01 alpha: i.e., 0.01/5=0.002? Please clarify._ 

Thank you, that was indeed written confusingly. We considered all tests and regions as whole, so 7 tests * 5 regions = 35 tests, which would result in a very strong Bonferroni correction. Indeed, if one considers the different tests individually, the correction we apply from 0.05 to 0.01 can be considered as correcting for the number of regions, which we now highlight better. We apply no further corrections of any kind to our alpha=0.01. We clarified this in the manuscript in all relevant places (lines 205-208, 246, 297-298, and 726-727). 

_(6) Did the authors take into account how many times a probe was used/how clean the probe was before each recording. Was this streamlined between labs? This can have an effect on yield and quality of recording._ 

We appreciate the reviewer highlighting the potential impact of probe use and cleanliness on recording quality and yield. While we did not track the number of times each probe was used, we ensured that all probes were cleaned thoroughly after each use using a standardized cleaning protocol (Section 16: Cleaning the electrode after data acquisition in Appendix 2: IBL protocol for electrophysiology recording using Neuropixels probe). We acknowledge that tracking the specific usage history of each probe could provide additional insights, but unfortunately we did not track this information for this project. In prior work the re-usability of probes has been quantified, showing insignificant degradation with use (e.g. Extended Data Fig 7d from Jun et al. 2017). 

_(7) Figure 3, Supplement1: DY_013 missed DG entirely? Was this included in the analysis?_ 

Thank you for this question. We believe the reviewer is referring to the lack of a prominent high-amplitude LFP band in this mouse, and lack of high-quality sorted units in that region. Despite this, our histology did localize the recording trajectory to DG. This recording did pass our quality control criteria overall, as indicated by the green label, and was used in relevant analyses. 

The lack of normal LFP features and neuron yield might reflect the range of biological variability (several other sessions also have relatively weak DG LFP and yield, though DY_013 is the weakest), or could reflect some damage to the tissue, for example as caused by local bleeding. Because we could not conclusively identify the source of this observation, we did not exclude it. 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

86 of 89 

_(8) Given that the authors argue for using the MTNN over GLMs, it would be useful to know exactly how much better the MTNN is at predicting activity in the held-out dataset (shown in Figure 7, Supplement 1). It looks like a very small increase in prediction performance between MTNN and GLMs, is it significantly different?_ 

The average variance explained on the held-out dataset, as shown in Figure 8–Figure Supplement 1 Panel B, is 0.065 for the GLMs and 0.071 for the MTNN. As the reviewer correctly noted, this difference is not significant. However, one of the key advantages of the MTNN over GLMs lies in its flexibility to easily incorporate covariates, such as electrophysiological characteristics or session/lab IDs, directly into the analysis. This feature is particularly valuable for assessing effect sizes and understanding the contributions of various factors. 

_(9) In line 723: why is the threshold for mean firing rate for a unit to be included in the MTNN results so high (>5Hz), and how does it perform on units with lower firing rates?_ 

We thank the reviewer for pointing this out. The threshold for including units with a mean firing rate above 5 Hz was set because most units with firing rates below this threshold were silent in many trials, and reducing the number of units helped keep the MTNN training time reasonable. Based on this comment, we ran the MTNN experiments including all units with firing rates above 1 Hz, and the results remained consistent with our previous conclusions (Figure 8). Crucially, the leave-one-out analysis consistently showed that lab and session IDs had effect sizes close to zero, indicating that both within-lab and between-lab random effects are small and comparable. 

## _**Reviewer #2 (Recommendations for the authors):**_ 

_(1) Most of the more major issues were already listed in the above comments. The strongest recommendation for additional work would be to improve the description and implementation of the RIGOR statistics such that non-IBL labs that might use Neuropixels probes but not use the entire IBL pipeline might be able to apply the RIGOR framework to their own data._ 

We thank the reviewer for highlighting the importance of making the RIGOR statistics more accessible to a broader audience. We agree that improving the description and implementation of the RIGOR framework is essential for facilitation of non-IBL labs using Neuropixels probes. To address this we created a jupyter notebook with step-by-step guidance that is not dependent on the IBL pipeline. This tool (https://github.com/int-brain-lab/paperreproducible-ephys/blob/develop/RIGOR_script.ipynb) is publicly available through the repository, accompanied by example datasets and usage tutorials. 

_(2) Table 1: How are qualitative features like "drift" defined? Some quantitative statistics like "presence ratio" (the fraction of the dataset where spikes are present) already exist in packages like ecephys_spike_sorting. Who measured these qualitative features? What are the best practices for doing these qualitative analyses?_ 

At the probe level, we compute the estimate of the relative motion of the electrodes to the brain tissue at multiple depths along the electrode. We overlay the drift estimation over a raster plot to detect sharp displacements as a function of time. Quantitatively, the drift is the cumulative absolute electrode motion estimated during spike sorting (µm). We clarified the corresponding text in Table 1. 

The qualitative assessments were carried out by IBL staff and experimentalists. We have now provided code to run the RIGOR metrics along with an embedded tutorial, to complement the 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

87 of 89 

supplemental figures we have shown about qualitative metric interpretation. 

- _(3) Table 1: What are the units for the LFP derivative?_ 

We thank the reviewer for noting that the unit was missing. The unit (decibel per unit of space) is now in the table. 

- _(4) Table 1: For "amplitude cutoff", the table says that "each neuron must pass a metric". What is the metric?_ 

We have revised the table to include this information. This metric was designed to detect potential issues in amplitude distributions caused by thresholding during deconvolution, which could result in missed spikes. There are quantitative thresholds on the distribution of the low tail of the amplitude histogram relative to the high tail, and on the relative magnitude of the bins in the low tail. We now reference the methods text from the table, which includes a more extended description and gives the specific threshold numbers. Also, the metric and thresholds are more easily understood with graphical assistance; see the IBL Spike Sorting Whitepaper for this (Fig. 17 in that document and nearby text; https://doi.org/10.6084/m9 .figshare.19705522.v4). This reference is now also cited in the text. 

- _(5) Figure 2: In panel A, the brain images look corrupted._ 

Thanks; in the revised version we have changed the filetype to improve the quality of the panel image. 

- _(6) Figure 7: In panel D, make R2 into R^2 (with a superscript)_ 

Panel D y-axis label has been revised to include superscript (note that this figure is now Figure 8). 

Works Cited 

Julie M.J. Fabre, Enny H. van Beest, Andrew J. Peters, Matteo Carandini, and Kenneth D. Harris. Bombcell: automated curation and cell classification of spike-sorted electrophysiology data, July 2023. URL https://doi.org/10.5281/zenodo.8172822. 

James J. Jun, Nicholas A. Steinmetz, Joshua H. Siegle, Daniel J. Denman, Marius Bauza, Brian Barbarits, Albert K. Lee, Costas A. Anastassiou, Alexandru Andrei, C¸ a˘gatayAydın, Mladen Barbic, Timothy J. Blanche, Vincent Bonin, Jo˜ao Couto, Barundeb Dutta, Sergey L. Gratiy, Diego A. Gutnisky, Michael H¨ausser, Bill Karsh, Peter Ledochowitsch, Carolina Mora Lopez, Catalin Mitelut, Silke Musa, Michael Okun, Marius Pachitariu, Jan Putzeys, P. Dylan Rich, Cyrille Rossant, Wei-lung Sun, Karel Svoboda, Matteo Carandini, Kenneth D. Harris, Christof Koch, John O’Keefe, and Timothy D.Harris. Fully integrated silicon probes for high-density recording of neural activity.Nature, 551(7679):232–236, Nov 2017. ISSN 1476-4687. doi: 10.1038/nature24636. URL https://doi.org/10.1038/nature24636. 

Simon Musall, Xiaonan R. Sun, Hemanth Mohan, Xu An, Steven Gluf, Shu-Jing Li, Rhonda Drewes, Emma Cravo, Irene Lenzi, Chaoqun Yin, Bj¨orn M. Kampa, and Anne K. Churchland. Pyramidal cell types drive functionally distinct cortical activity patterns during decisionmaking. Nature Neuroscience, 26(3):495– 505, Mar 2023. ISSN 1546-1726. doi: 10.1038/s41593022-01245-9. URL https://doi.org/10.1038/s41593-022-01245-9. 

Ivana Orsolic, Maxime Rio, Thomas D Mrsic-Flogel, and Petr Znamenskiy. Mesoscale cortical dynamics reflect the interaction of sensory evidence and temporal expectation during perceptual decision-making. Neuron, 109(11):1861–1875.e10, April 2021. Hyeong-Dong Park, St´ephanie Correia, Antoine Ducorps, and Catherine Tallon-Baudry.Spontaneous fluctuations 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

88 of 89 

in neural responses to heartbeats predict visual detection.Nature Neuroscience, 17(4):612– 618, Apr 2014. ISSN 1546-1726. doi: 10.1038/nn.3671. URL https://doi.org/10.1038/nn.3671. 

Lorenzo Posani, Shuqi Wang, Samuel Muscinelli, Liam Paninski, and Stefano Fusi. Rarely categorical, always high-dimensional: how the neural code changes along the cortical hierarchy. bioRxiv, 2024. doi: 10.1101/2024.11.15.623878. URL https://www.biorxiv.org/content /early/2024/12/09/2024.11.15.623878. 

Nicholas A. Steinmetz, Christina Buetfering, Jerome Lecoq, Christian R. Lee, Andrew J. Peters, Elina A. K. Jacobs, Philip Coen, Douglas R. Ollerenshaw, Matthew T. Valley, Saskia E. J. de Vries, Marina Garrett, Jun Zhuang, Peter A. Groblewski, Sahar Manavi, Jesse Miles, Casey White, Eric Lee, Fiona Griffin, Joshua D. Larkin, Kate Roll, Sissy Cross, Thuyanh V. Nguyen, Rachael Larsen, Julie Pendergraft, Tanya Daigle, Bosiljka Tasic, Carol L. Thompson, Jack Waters, Shawn Olsen, David J. Margolis, Hongkui Zeng, Michael Hausser, Matteo Carandini, and Kenneth D. Harris. Aberrant cortical activity in multiple gcamp6-expressing transgenic mouse lines. eNeuro, 4(5), 2017. doi: 10.1523/ENEURO.0207-17.2017. URL https://www.eneuro.org /content/4/5/ENEURO.0207-17.2017. 

Nicholas A. Steinmetz, Peter Zatka-Haas, Matteo Carandini, and Kenneth D. Harris. Distributed coding of choice, action and engagement across the mouse brain. Nature, 576(7786):266–273, Dec 2019. ISSN 1476-4687. doi: 10.1038/s41586-019-1787-x. URL https://doi .org/10.1038/s41586-019-1787-x. 

Nicholas A. Steinmetz, Cagatay Aydin, Anna Lebedeva, Michael Okun, Marius Pachitariu, Marius Bauza, Maxime Beau, Jai Bhagat, Claudia B¨ohm, Martijn Broux, Susu Chen, Jennifer Colonell, Richard J. Gardner, Bill Karsh, Fabian Kloosterman, Dimitar Kostadinov, Carolina Mora-Lopez, John O’Callaghan, Junchol Park, Jan Putzeys, Britton Sauerbrei, Rik J. J. van Daal, Abraham Z. Vollan, Shiwei Wang, Marleen Welkenhuysen, Zhiwen Ye, Joshua T. Dudman, Barundeb Dutta, Adam W. Hantman,Kenneth D. Harris, Albert K. Lee, Edvard I. Moser, John O’Keefe, Alfonso Renart, Karel Svoboda, Michael H¨ausser, Sebastian Haesler, Matteo Carandini, and Timothy D. Harris. Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. Science, 372(6539):eabf4588, 2021. doi: 10.1126/science.abf4588.URL https://www.science.org/doi/abs/10.1126/science.abf4588. 

Charlie Windolf, Han Yu, Angelique C. Paulk, Domokos Mesz´ena, William Mu˜noz, Julien Boussard, Richard Hardstone, Irene Caprara, Mohsen Jamali, Yoav Kfir, Duo Xu, Jason E. Chung, Kristin K. Sellers, Zhiwen Ye, Jordan Shaker, Anna Lebedeva, Manu Raghavan, Eric Trautmann, Max Melin, Jo˜ao Couto, Samuel Garcia, Brian Coughlin, Csaba Horv´ath, Rich´ard Fi´ath, Istv´an Ulbert, J. Anthony Movshon, Michael N. Shadlen, Mark M. Churchland, Anne K. Churchland, Nicholas A. Steinmetz, Edward F. Chang, Jeffrey S. Schweitzer, Ziv M. Williams, Sydney S. Cash, Liam Paninski, and Erdem Varol. Dredge: robust motion correction for highdensity extracellular recordings across species. bioRxiv, 2023. doi: 10.1101/2023.10.24.563768. URL https://www.biorxiv.org/content/early/2023/10/29/2023.10.24.563768. 

https://doi.org/10.7554/eLife.100840.2.sa0 

International Brain Laboratory _et al._ , 2025 eLife. https://doi.org/10.7554/eLife.100840.2 

89 of 89 

