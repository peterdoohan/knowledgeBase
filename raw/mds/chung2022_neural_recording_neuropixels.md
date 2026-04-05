NeuroResource 

## High-density single-unit human cortical recordings using the Neuropixels probe 

## Graphical abstract 

**==> picture [286 x 287] intentionally omitted <==**

## Authors 

Jason E. Chung, Kristin K. Sellers, Matthew K. Leonard, ..., Marleen Welkenhuysen, Barundeb Dutta, Edward F. Chang 

## Correspondence 

edward.chang@ucsf.edu 

## In brief 

Recent technologies have enabled simultaneous recording from large numbers of individual neurons in animal models. Here, Chung, Sellers, et al. translate this technology to record from tens to hundreds of individual neurons in humans undergoing neurosurgical procedures. They provide quantitative unit metrics to serve as a benchmark for recording quality. 

## Highlights 

- d Single-unit recordings in 8 patients, yielding 596 putative single units across 11 recordings 

- d Units take longer to fire first spike in anesthetized versus awake participants 

- d Negative correlation between the motion of the electrode array and single-unit yield 

**==> picture [17 x 17] intentionally omitted <==**

Chung et al., 2022, Neuron 110, 2409–2421 August 3, 2022 ª 2022 Elsevier Inc. https://doi.org/10.1016/j.neuron.2022.05.007 

**ll** 

**ll** 

**==> picture [46 x 35] intentionally omitted <==**

## NeuroResource 

## High-density single-unit human cortical recordings using the Neuropixels probe 

Jason E. Chung,[1][,][5] Kristin K. Sellers,[1][,][2][,][5] Matthew K. Leonard,[1][,][2] Laura Gwilliams,[1][,][2] Duo Xu,[1][,][2] Maximilian E. Dougherty,[1][,][2] Viktor Kharazia,[1] Sean L. Metzger,[1][,][2][,][3] Marleen Welkenhuysen,[4] Barundeb Dutta,[4] and Edward F. Chang[1][,][2][,][6][,] * 

1Department of Neurological Surgery, University of California, San Francisco, San Francisco, CA 94143, USA 

2Weill Institute for Neuroscience, University of California, San Francisco, San Francisco, CA 94158, USA 

3University of California Berkeley, University of California, San Francisco Graduate Program in Bioengineering, Berkeley, CA 94720, USA 4IMEC, Leuven, Belgium 

5These authors contributed equally 

6Lead contact 

*Correspondence: edward.chang@ucsf.edu https://doi.org/10.1016/j.neuron.2022.05.007 

## SUMMARY 

The action potential is a fundamental unit of neural computation. Even though significant advances have been made in recording large numbers of individual neurons in animal models, translation of these methodologies to humans has been limited because of clinical constraints and electrode reliability. Here, we present a reliable method for intraoperative recording of dozens of neurons in humans using the Neuropixels probe, yielding up to �100 simultaneously recorded single units. Most single units were active within 1 min of reaching target depth. The motion of the electrode array had a strong inverse correlation with yield, identifying a major challenge and opportunity to further increase the probe utility. Cell pairs active close in time were spatially closer in most recordings, demonstrating the power to resolve complex cortical dynamics. Altogether, this approach provides access to population single-unit activity across the depth of human neocortex at scales previously only accessible in animal models. 

## INTRODUCTION 

The study of human mental processing would greatly benefit from our ability to observe the dynamics of action potentials of single neurons and the networks they form. For now, this requires electrodes to be implanted directly into the brain (Cash and Hochberg, 2015; Hong and Lieber, 2019). Single-unit recordings have been a critical tool for mapping circuits in neurosurgical procedures for decades. For example, microelectrode recordings during movement disorder surgery are used to define the functional properties of cell types and structures in the human basal ganglia and thalamus to guide accurate placement of deep brain stimulation electrode leads to small anatomical targets. This precision is essential to the success of the treatment, as even small deviations of 1–2 mm can reduce efficacy and cause unwanted side effects. 

Current technologies for cellular neurophysiology in humans are severely limited in the number of single neurons that can be simultaneously recorded. The most often utilized sharp metal microelectrodes typically yield one single neuron at a time (Benazzouz et al., 2002; Guridi et al., 2000; Hutchison et al., 1998). Microwire-based research-focused intraoperative technologies such as the Behnke-Fried electrode can yield up to 2.7 neurons per 8-microwire depth array on average, with 1–2 neurons being the most common yield (Misra et al., 2014). For semi-chronic or chronic studies, the Utah electrode array, a 96-channel ‘‘bed-of- 

nails’’ array (Maynard et al., 1997; Nordhausen et al., 1994), has been utilized for brain machine interface (Ajiboye et al., 2017; Collinger et al., 2013; Gilja et al., 2015; Hochberg et al., 2012) or memory studies (Vaz et al., 2020), but it lacks the ability to sample across the cortical depth and does not yield good recordings until hours after the insertion, thereby limiting its application to a tiny population of experimental settings with chronic or semi-chronic recordings. 

The past decade has seen the development of an impressive armament of new tools for neuroscientists to understand the structure and function of the brain in animal models, many of which are designed specifically for simultaneous recording from large numbers of single neurons (Chen and Pesaran, 2021). Many of these advances have been driven by high-density microfabricated electrode arrays and associated developments in integration (Bere´ nyi et al., 2014; Chung et al., 2019; Jun et al., 2017; Musk and Neuralink, 2019; Shobe et al., 2015; Steinmetz et al., 2021), thereby providing access to spatial and temporal scales required to understanding information processing across the cortical microcircuit (Larkum, 2013). However, translation of methods for recording fundamental computational units (e.g., single neurons and ensembles) has proven extremely difficult. This has led to an increasing gap between what can be learned in animal models and how these detailed principles apply to the human brain. 

**==> picture [17 x 17] intentionally omitted <==**

Neuron 110, 2409–2421, August 3, 2022 ª 2022 Elsevier Inc. 2409 

**ll** 

NeuroResource 

Table 1. Participant information 

|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|Table 1. Participant information|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|ID<br>Spikes<br>Isolable<br>units<br>Sex<br>Age<br>State<br>Hemisphere<br>Region and<br>procedure<br>Pathology<br>Failure reason|||||||||||||||||||
|NP01<br>no<br>no<br>M<br>31<br>awake<br>left<br>anterior temporal<br>resection<br>tumor<br>shank broke upon<br>insertion|||||||||||||||||||
|NP02<br>no<br>no<br>F<br>25<br>anesthetized<br>right<br>resection, frontal<br>lobe<br>epileptic foci<br>(focal cortical dysplasia)<br>noise issues|||||||||||||||||||
|NP03<br>yes<br>yes<br>M<br>49<br>asleep<br>right<br>resection, frontal<br>lobe<br>tumor<br>–|||||||||||||||||||
|NP04<br>yes<br>yes<br>F<br>33<br>awake<br>left<br>anterior temporal<br>lobectomy (ATL)<br>temporal epilepsy<br>noise issues|||||||||||||||||||
|NP05<br>no<br>no<br>F<br>22<br>awake<br>left<br>ATL<br>temporal epilepsy<br>probe broke soon<br>after insertion|||||||||||||||||||
|NP06<br>yes<br>no<br>F<br>32<br>awake<br>left<br>resection, motor<br>cortex<br>epileptic foci<br>(focal cortical dysplasia)<br>probe broke soon<br>after insertion|||||||||||||||||||
|NP07<br>no<br>no<br>F<br>54<br>awake<br>left<br>ATL<br>temporal epilepsy<br>noise issues|||||||||||||||||||
|NP08<br>no<br>no<br>M<br>38<br>awake<br>left<br>resection, post-<br>centralgyrus<br>epileptic foci<br>(focal cortical dysplasia)<br>no spikes|||||||||||||||||||
|NP09<br>no<br>no<br>F<br>57<br>awake<br>left<br>anterior temporal<br>resection<br>tumor<br>–|||||||||||||||||||
|NP10<br>yes<br>yes<br>F<br>36<br>anesthetized<br>right<br>ATL<br>temporal epilepsy<br>–|||||||||||||||||||
|NP11<br>yes<br>yes<br>M<br>49<br>awake<br>right<br>resection, motor<br>cortex<br>cavernoma<br>–|||||||||||||||||||
|NP12<br>yes<br>yes<br>F<br>46<br>anesthetized<br>right<br>ATL<br>temporal epilepsy<br>–|||||||||||||||||||
|NP13<br>yes<br>yes<br>M<br>25<br>awake<br>left<br>ATL<br>temporal epilepsy<br>–|||||||||||||||||||
|NP14<br>yes<br>yes<br>M<br>35<br>awake<br>left<br>ATL<br>temporal epilepsy<br>–|||||||||||||||||||
|NP15<br>yes<br>yes<br>M<br>27<br>awake<br>left<br>resection, angular<br>gyrus<br>cavernoma<br>–|||||||||||||||||||
||||||||||||||||||||



Participants are listed in chronological order. The majority had surgery for medically refractory epilepsy. Note that participant NP03 was asleep but not anesthetized during recording. 

Here, we present a methodology that utilizes the Neuropixels probe (Dutta et al., 2019; Jun et al., 2017; Steinmetz et al., 2018) to record across the cortical depth in a much broader patient population than previously available for single-unit recordings. The Neuropixels probe combines advanced complementary metaloxide semiconductor (CMOS) technology with integrated amplification, digitization, and multiplexing circuits on the same device for large-scale, high-density recordings with streamlined data transfer without bulky cabling or connectorization. This innovative probe contains 960 12 3 12 mm contacts with 384 selectable recording channels, arranged along a 10-mm-long shank in a 4-column checkerboard pattern, with a 16-mm pitch across columns and 20-mm pitch across rows. The Neuropixels probe has seen rapid adoption across multiple animal models in the neuroscience community (van Daal et al., 2021; Gaucher et al., 2020; Juavinett et al., 2019; Jun et al., 2017; Trautmann et al., 2019). 

Here,andinasimultaneousstudy(Paulketal.,2022),theNeuropixels probe shows the potential to access dozens of simultaneously recorded single neurons in human participants after addressing translational issues, including safety and sterilization, and electrical noise mitigation in the intraoperative setting. In this work, we report on 596 putative single units with cluster quality metrics from 11 recordings across 8 of our first 15 consecutively tested human participants, all of whom underwent craniotomy 

for a variety of clinical indications. Here, we demonstrate the method’s potential for access to dozens of simultaneously recorded single neurons, feasibility for intraoperative use, and accesstoavarietyoftargetlocations,andwealsoidentifytherelative motion of electrode array to brain as the next challenge in further improvement of cell yield. Neuropixels probes have tremendous promise for rapid and robust single-cell recordings at large scale in humans, with deep research and clinical potential. 

## RESULTS 

Intraoperative recordings utilizing the Neuropixels probe were attempted in 15 participants (Table 1). A Greenberg C-clamp, an articulating bar, 3 ball-joint arms, and a micromanipulator were attached to the Mayfield head clamp in series, allowing for gross targeting of the insertion location. The probe was then removed from custom-designed holders used during sterilization and transport and mounted to the micromanipulator (Figures 1A and 1B). The insertion locations were at the center of a gyrus, away from surface vasculature, that was going to be resected in the same surgical procedure (Figure 1B). In some cases, a piotomy was performed to allow for easier probe penetration. The probe was then inserted to a targeted depth of 7 mm (to span the full depth of the cortex and also record 

2410 Neuron 110, 2409–2421, August 3, 2022 

## **ll** 

## NeuroResource 

Figure 1. Intraoperative human recording with Neuropixels high-density silicon electrode arrays 

**==> picture [317 x 277] intentionally omitted <==**

(A) Neuropixels probe with ground and reference needle electrodes attached, as prepared for sterilization in custom-designed holder. 

(B) Representative intraoperative photo after Neuropixels probe has been inserted in cortex (participant NP10). Inset scale bars represent 10 mm. 

(C) Representative histology of insertion tract lesion and neocortical cytoarchitecture, stained with luxol fast blue and neutral red. Inset with area of higher magnification. Scale bars below represent 1 mm (left) and 0.5 mm (right). 

- (D) Insertion locations of Neuropixel probes with colors corresponding to participants, for all datasets with isolable single units. 

participants were awake. As more datasets were collected, issues related to probe fracture or noise were mitigated (see STAR Methods), with all 6 of the most recent recordings yielding spikes (Table 1). For the remainder of this paper, the 7 participants without isolable single units are excluded from further analyses. 

While at least some identifiable spiking was present immediately after insertion, total spiking activity increased for several minutes after insertion. The data were clustered and curated resulting in putative single units that generally aligned well to the action potentials seen in the band-pass-filtered data (Figures 2A and 2B). Across all 11 insertions over 8 participants, half of the recorded units became active within seconds after reaching target depth (8.8 ± 9.2 s, mean ± SD), and 75% of the recorded units were active within 2 min (33 ± 37 s). The recordings done in anesthetized patients took significantly longer for units to be active after reaching target depth (50% of units at least one spike, anesthetized 18.4 ± 8.9 s, non-anesthetized 3.3 ± 2.6 s, Wilcoxon rank-sum p = 0.014; 75% of units at least one spike, anesthetized 67.3 ± 39.8 s, non-anesthetized 13.5 ± 12.8 s, Wilcoxon rank-sum p = 0.038; Figure 2C). Note that participant NP03 was asleep but not anesthetized during recording and exhibits an empirical cumulative distribution function more similar to that of anesthetized patients (Figure 2C). These timescales are compatible with meaningful recordings done within the time constraints of the intraoperative environment. 

channels at the brain/air boundary for movement tracking) (Video S1). In some cases, the insertion sites were far enough away from local vasculature to allow for safe en bloc resection and subsequent histology (Figure 1C). Targeted regions were in the right or left superior temporal gyrus in 5 of 8 participants with putative single units, the right middle frontal gyrus in 1 participant (Figures 1D and S1), the right ventral motor cortex in 1 participant, and the left angular gyrus in 1 participant, dependent solely on the resection plan for tissue destined for removal (Table 1). We found that reducing AC noise was key for achieving the required signal-to-noise ratio in the intraoperative environment. Furthermore, reducing positive end-expiratory pressure for intubated participants helped reduce the amplitude of brain pulsation reflected in recordings caused by both cardiac and respiratory cycles. 

In cases where spiking was recorded, action potentials were apparent in the online filtered data (high-pass, 300 Hz) within seconds of insertion (all 13 insertions with visible action potentials within 30 s of insertion upon post-hoc review of 300 Hz highpass filtered data across all 9 participants with spikes). In one case with visible spiking (NP06), the probe shank broke less than 1 min after insertion, and no putative single units were isolated from this brief recording. In one other insertion there was too much motion of the probe, relative to the brain, to isolate units (NP11, second insertion). In the 6 of 15 participants where no spiking was seen, 2 probes broke upon insertion, 3 had electrical noise that precluded successful recording (2 participants were awake, and 1 was anesthetized), and in 1 participant no spiking was seen despite low noise and successful insertion (NP09). In all cases where the probe broke during or soon after insertion, 

There were 11 insertions that yielded putative single units. These recordings were 10 to 23 min in length (15 min 11 s ± 3 min 47 s, mean ± SD). A total of 596 putative single units were identified, with 11 to 94 units per insertion and 34 to 94 simultaneously recorded putative single units being isolated in each participant (best insertion per participant; 54.2 ± 27.2 putative single units, mean ± SD across all recordings). There was no significant relationship between length of recording and putative single-unit yield (Figure 2D, Spearman correlation = 0.44, p = 0.17). There was no difference in putative single-unit yield between anesthetized and non-anesthetized states (Wilcoxon 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, 2409–2421, August 3, 2022 2411 

## **ll** 

## NeuroResource 

**==> picture [318 x 311] intentionally omitted <==**

Figure 2. The majority of putative units are active within minutes 

(A) Left: schematic of electrode array. Horizontal red line represents estimated brain surface depth. Total length of the probe shown corresponds to 8 mm, with 6.8 mm below the brain surface. Right: spike rasters for 94 putative units following spike sorting and manual curation in 1 s of data from NP03. Each row is a raster from a putative single unit. Note that not all 94 units are active in this 1 s of data. 

(B) Representative recording snippets from NP03, filtered from 300 to 6,000 Hz, corresponding to colorcorresponding boxed segments of (A). Recording excerpts, boxed, from channels at the color-corresponding depths, with rasters for the 1 to 3 units represented in the excerpt. Inset scale bars in bottom left represent 200 mV and 5 ms. 

(C) Empirical cumulative distribution functions of time of first spike for all putative single units shown for all insertions. x axis, time in seconds. Time zero is after the probe is lowered to target recording depth. y axis, proportion of units that have at least 1 spike. Colors correspond to inset legend. Dashed lines represent recordings done in anesthetized participants. Note that NP03 was asleep but not anesthetized during recording. 

(D) Recording length (x axis, minutes) and number of putative single units recorded (y axis). Colors correspond to legend inset in (C). 

rank-sum p = 0.78), and as expected, no difference was detected between hemisphere (Wilcoxon rank-sum p = 0.47) or participant’s sex (Wilcoxon rank-sum p = 0.65). There was no difference seen in single-unit yield by recording location (superior temporal gyrus versus non-superior temporal gyrus; Wilcoxon rank-sum p = 0.92). 

Clusters that passed manual curation, following automated spike sorting, spanned a range of quality across individual recordings (Figure S2) as quantified by cluster metrics (see STAR Methods for more details; all metrics reported as median and interquartile range; spike amplitude: 136, 108 to 189 mV; estimated proportion of amplitude histogram truncation: 0.0019, 0.0005 to 0.0266; signal-to-noise ratio: 4.2, 2.7 to 6.8; RMS noise in action potential band (300 Hz to 6 kHz): 6.81, 6.14 to 10.08; proportion of events violating 1-ms inter-spike interval: 0.0006, 0 to 0.0028; isolation: 0.993, 0.984 to 0.997; D-prime: 3.24, 2.77 to 3.86; firing rate: 0.91, 0.50 to 1.69 Hz; spike half-width: 0.33, 0.23 to 0.40 ms; spread: 120, 80 to 160 mm; amplitude decay: 0.67, 0.41 to 1.3 per mm; active channels: 11, 8 to 14 channels; Figures 3 and S3). 

Stability of the Neuropixels probe, relative to brain tissue during recording, is ideal to avoid movement artifacts and facilitate clean spike sorting. However, there are multiple factors acting on the probe that lead to small movements. Despite skull fixation, awake participants can cause slight shifting of the probe. We quantified and corrected for motion in our data using several methods. First, we used the motion stabilization algorithm implemented in the spike-sorting software Kilosort 2.5 (Pachitariu 

et al., 2021; Steinmetz et al., 2021). Because of the high-density spacing of electrodes along the Neuropixels 1.0 probes, the waveform of a spike is captured over multiple adjacent channels—its ‘‘spike spatial footprint.’’ The algorithm tracks the footprint of each spike template as it moves over time and uses its vertical offset to stabilize the center location of the spike on the probe. These spatially re-registered data are then submitted to spike sorting and manual curation. This algorithm can detect and correct for movement on relatively slow timescales (2 s). 

Significant vertical motion was partially compensated for by using the motion correction in Kilosort 2.5 (Figure 4A). However, faster timescale motion remained in some recordings. We used a second approach to quantify this movement. We identified highrate, high-amplitude, and spatially isolated putative single units to serve as spatial markers (Figures 4B [green trace] and S4). These units were tracked with 20-ms resolution to quantify motion (see STAR Methods for more information). Using this method, we measured an overall mean amplitude of movement of 251 ± 112 mm (mean ± SD, n = 11 recordings). We found that the mean motion of a recording was negatively correlated with the single-unit yield for that same recording (Spearman R = � 0.62, p = 0.040, Figure 4D). 

Putative neurons may be intermittently detectable because of increased relative motion of electrode array and brain. To quantify the relative length of time a putative single unit had spiking activity in the recording, the presence ratio (Buccino et al., 2020) was calculated. Briefly, the presence ratio is the proportion of a 

2412 Neuron 110, 2409–2421, August 3, 2022 

## **ll** 

## NeuroResource 

Figure 3. Neuropixels probe reliably isolates putative single units in human cortex Cluster metrics plots for all 596 clusters from 11 datasets across 8 participants, legend inset. 

**==> picture [317 x 301] intentionally omitted <==**

- (A) Scatterplot of amplitude (x axis, mV) versus estimated proportion of amplitude histogram truncation (y axis). 

- (B) As in (A), but for signal-to-noise ratio (x axis) and proportion of events violating the refractory period (inter-spike-interval less than 1 ms, y axis). 

- (C) As in (A), but for isolation (x axis) and d-prime (y axis). 

- (D) As in (A), but for firing rate (x axis, Hz), and spike half-width (y axis, ms). 

computational processes underlying neuronal function (Buzsa´ ki, 2004). The ability to conduct these recordings in awake, behaving human participants paves the way for studying the millisecond-timescale computations that underlie these behaviors. Toward achieving this goal, we herein provide a methodology capable of yielding large-scale simultaneously recorded putative neurons within the constraints of the operative environment, using the Neuropixels probe. 

Here, we show 11 recordings that yielded a total of 596 putative single units in 8 of the initial 15 participants where Neuropixels recordings were attempted. Notably, failures related to intraoperative electrical noise and probe fracture were mitigated in later recordings. We noted the key general goal of eliminating any alternating current device attached to the participant. Importantly, the operative table, electrocautery, and electronics associated with intravenous lines should be on direct current, including syringe pumps and blood/fluid warmers. Probe shank fractures were mitigated by either seeking locations with relatively thin pia or by performing piotomy. 

recordingthataputativesingleunithasdetectedspikes(see STAR Methods for more information). There was no significant correlation between the mean motion and presence ratio of the putative single units (Spearman R = �0.19, p value = 0.57, Figure 4E). 

Access to tens of simultaneously recorded neurons across the depth of cortex allows analysis of the relative timings of the thousands of cell pairs relative to their locations. Single-unit pairs’ relative activity was stratified by cell-pair coordination index (CCI) (see STAR Methods). Briefly, cross-correlograms were calculated and the activity of cell pairs in close temporal proximity (within ± 50 ms) was compared with the next 100-ms period (from �100 to �50 ms and from 50 to 100 ms). Putative neuron pairs that fired more within ±50 ms than the next 100-ms period had positive CCI; putative neuron pairs that fired more within the �100 to �50 ms and 50 to 100 ms time period, combined, than the ± 50 ms time period had negative CCI. Datasets with more than 500 cell pairs were included in further analysis (Table 2). In all 4 of the datasets across 3 participants, cell pairs with positive CCI were significantly closer together than those with negative CCI (Figures 5 and S5; Table 2). The simultaneous recording of tens of single units and thousands of cell pairs across the depth of cortex allows for their relative spike timings and spatial locations to be studied at an unprecedented resolution in an awake human. 

Nearly all recordings that yielded putative single units had visible spiking activity within seconds of insertion, and the majority of isolated units were active within a couple of minutes of reaching target depth. In cases where the participant was anesthetized, there was a significantly longer latency before most putative single units became active, although this delay was still on the timescale of minutes. Given the short recording length, compared with animal experiments, this result may be heavily influenced by the firing rates of the isolated single units—there are likely insufficient spikes detected from low firing rate neurons to isolate them successfully, using traditional spike-sorting algorithms. 

Here, all spike sorting was done using Kilosort 2.5 with manual curation (Pachitariu et al., 2016, 2021; Steinmetz et al., 2021)— necessary in large part due to the pulsation-associated electrode drift described below. Whereas considerable variability is introduced from the operator biases inherent in manual curation in the spike-sorting pipeline (Wood et al., 2004), the application of metrics (Buccino et al., 2020; Magland et al., 2020) allows 

## DISCUSSION 

Large-scale recordings of single-unit action potential firing across cortical layers provide unprecedented insight into the 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, 2409–2421, August 3, 2022 2413 

**ll** 

NeuroResource 

**==> picture [414 x 599] intentionally omitted <==**

(legend on next page) 

2414 Neuron 110, 2409–2421, August 3, 2022 

**ll** 

## NeuroResource 

objective assessment of quality. In this work, and for the first time in human high-density silicon array recording, cluster metrics for all putative single units are reported, thereby establishing an objectivepointofcomparisonforqualityand yield forhuman application of the Neuropixels probe. 

Among the contributors to variability in recording quality and cell yield, the relative motion of electrode array and neural tissue from the pulsation of cardiac and respiratory cycles is the primary component affecting quality. In this work, we report a significant negative correlation between motion and putative single-unit yield. As for steps that can be taken to mitigate motion, we found that in intubated participants, reducing positive end-expiratory pressure helped reduce amplitude of both cardiac and respiratory cycles. There is a considerable amount of work necessary to counteract or compensate for brain movements both in physical and computational approaches. Notwithstanding that Neuropixels 2.0 and associated motion correction algorithms (Steinmetz et al., 2021) show promise to better mitigate electrode drift in animal models, further physical stabilization and computational work will be necessary for future human application. 

In this study, a craniotomy was required for a range of clinical indications. Craniotomies expose a relatively large surface area of the brain to the air, thereby allowing access to a multitude of regions, depending on the clinical indications. Because craniotomies can give access to nearly all surface brain structures and multiple structures simultaneously, this larger surgical exposure is associated with greater pulsation and brain movement relative to burr holes (which are typically 14 to 25 mm in diameter). The difference in exposure size is an important point of comparison with a recent study (Paulk et al., 2022), where the two cases done through burr holes over dorsolateral prefrontal cortex yielded successful recordings, but the open craniotomy was very limited with relatively few putative single units. Here, we show that the Neuropixels probe can yield far higher single units despite the technical challenges associated with larger surgical exposures to multiple brain areas. With the increased number of recordings and quantification of motion, we are also able to identify the significant negative correlation between the relative motion of the electrode array and neural tissue and putative single-unit yield. This work provides quantification not only of the recordings themselves, such as motion and cell yield, but also of cluster metrics, thereby acting as a point of comparison for future human recording studies. 

Finally, we demonstrate the unprecedented capability to measure the millisecond dynamics across the depth of cortex in an awake, behaving human. As predicted from work in non-human 

primates across multiple regions (Constantinidis and GoldmanRakic, 2002; Lee et al., 1998; Smith and Kohn, 2008), we report in all 4 of the datasets and all 3 of the participants who met the inclusion criterion (at least 500 eligible cell pairs) that cell pairs with a positive CCI (see STAR Methods) are significantly closer together than those with a negative CCI. Although considerable work remains to be done to investigate these spatiotemporal relationships across different subjects, conditions, and locations, the application of Neuropixels probes in human intraoperative experiments provides an unprecedented opportunity for detailed investigations of cellular neurophysiology at large scale with implications for clinical and research applications. 

## Single-unit recordings in humans 

Single-unit recordings in the human brain have paved the way for exceptional findings, including ‘‘concept cells’’ (Quiroga et al., 2005), tremor-related cells (Levy et al., 2000), place cells (Ekstrom et al., 2003), mechanisms underlying seizure generation (Wyler et al., 1982), and anatomical subdivisions of language and memory processing (Ojemann et al., 1988, 2002). The earliest single-unit recordings in human brain were conducted in the 1950s (Ward and Thomas, 1955). For decades, these recordings were conducted with a single microwire, tungsten electrode (Bertrand and Jasper, 1965), or a small bundle of microwires, typically in patients with seizures or for confirmation of anatomical targeting in movement disorders (Benazzouz et al., 2002; Hutchison et al., 1998). Although such data are valuable to inform neuronal processing, the unit yields were very low (e.g., 74 units across 9 patients [Fried et al., 1997]; 90 units across 17 patients [Wyler et al., 1982]), and localization of individual microwire placement was difficult or impossible. 

More recent advances in human single-unit recordings include the use of the Utah array. Spiking activity from the Utah array has successfully been used by a tetraplegic participant to control a cursor-based brain machine interface (BMI) (Hochberg et al., 2006) and a 17-degree-of-freedom robotic limb (Aflalo et al., 2015). Gradually degrading but viable signal has been recorded from Utah arrays for up to 1,500 days (Hughes et al., 2021); however, substantial immune responses and tissue reorganization at the implant site are also common (Szymanski et al., 2021). The Utah array samples units across an xy plane and is not able to record units across the depth. Another class of probes includes microelectrode arrays, such as the Michigan array. These arrays are silicon-based probes manufactured to use electron beam lithography techniques (Choi et al., 2018; Pochay et al., 1979); these arrays allow for recording across the depth, but their use has been mainly limited to animal models. 

**==> picture [46 x 35] intentionally omitted <==**

Figure 4. Electrode motion reduces putative single-unit yield 

(A) Top: representative recording segment from participant NP12. Each dot represents a detected spike where grayscale reflects amplitude of spikes in arbitrary units (darker is higher amplitude), whitened and rescaled amplitudes, as in Steinmetz et al. (2021). x axis corresponds to time in seconds; y axis corresponds to spike position along the shank (0 mm is the deepest recording site). Red traces represent the motion detected and corrected for by Kilosort. Below: as above, but after Kilosort motion correction. 

(B) As in (A), but showing a time segment with high-rate, high-amplitude, and spatially isolated putative single unit to serve as a spatial marker of fast timescale motion (green trace). 

(C) An example of a high-pass (>0.1 Hz) filtered motion trace used to quantify the faster timescale mean peak-to-peak motion amplitudes in (D) and (E). (D) Mean peak-to-peak motion (x axis, in mm) and putative single-unit yield (y axis) for all recordings, legend inset. 

(E) Mean peak-to-peak motion (x axis, in mm) and boxplot of presence ratio (y axis, notch and red horizontal line marks median, box representing interquartile range [IQR], whiskers 1.5 3 the IQR, and outliers with open circles). Fill color corresponding to legend inset as in (D). 

Neuron 110, 2409–2421, August 3, 2022 2415 

NeuroResource 

## **ll** 

Table 2. Cell-pair coordination index and distance 

|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|Table 2. Cell-pair coordination index and distance|
|---|---|---|---|---|---|---|---|---|---|---|
|ID<br>Number of<br>cell pairs<br>CCI and distance<br>relationship<br>Median distance<br>positive CCI (mm)<br>Median distance<br>negative CCI (mm)<br>Rank-sum p<br>value|||||||||||
|NP03<br>811<br>positive closer<br>1220.0<br>1820<br>5.8e�04|||||||||||
|NP04<br>734<br>positive closer<br>540<br>1240<br>7.4e�11|||||||||||
|NP10-1<br>752<br>positive closer<br>1040<br>1360<br>0.012|||||||||||
|NP10-2<br>568<br>positive closer<br>760<br>1950<br>9.8e�11|||||||||||
|NP10-3<br>16<br>excluded<br>–<br>–<br>–|||||||||||
|NP11<br>155<br>excluded<br>–<br>–<br>–|||||||||||
|NP12<br>207<br>excluded<br>–<br>–<br>–|||||||||||
|NP13<br>358<br>excluded<br>–<br>–<br>–|||||||||||
|NP14-1<br>473<br>excluded<br>–<br>–<br>–|||||||||||
|NP14-2<br>29<br>excluded<br>–<br>–<br>–|||||||||||
|NP15<br>456<br>excluded<br>–<br>–<br>–|||||||||||
||||||||||||



Participants and insertions listed in chronological order. Datasets with more than 500 cell pairs with significant CCI (falling within the top or bottom 5th percentile compared with their shuffled distributions, see STAR Methods) were included in further analysis. All distances in microns. p values for Wilcoxon rank-sum test. 

For the microwire and Utah array approaches discussed above, a given unit can only be detected on one recording channel, as the shanks/contacts are spaced at least 100 mm apart (Harris et al., 2016). Some microelectrode arrays have contacts less than 50 mm apart, allowing for a given unit to be detected on multiple channels. This increases not only the number of recording contacts but also the accuracy of spike sorting because the spatiotemporal profile of a given unit can be better differentiated from other units when acquired from multiple recording channels (Rossant et al., 2016). The Neuropixels probe extends this even further, with a larger number of densely spaced contacts. 

Ethical issues surrounding large-scale invasive neurophysiological recordings in humans must be conscientiously considered. See Chiong et al. (2018) and Feinsinger et al. (2022) for suggestions and discussions on practices and principles for the ethical implementation of this research. These principles should be adopted as applicable given the details of the experiment. We emphasize that clinical care and safety should never be compromised for the purpose of research. In the work shown here, an evaluation of the appropriateness of patients’ participation in the research occurred only after surgical plan and resection margins were established, thereby avoiding any bias in clinical decision-making driven by this research. Consent was obtained far in advance of the procedure. The team involved in these research studies included a combination of treating physicians and nontreating researchers. Immediately prior to starting the recordings in the operating room, these team members conferred to establish whether the patient is clinically stable and re-checked whether the patient is still amenable to carrying out the research recordings; it was not uncommon to skip experiments with a patient who had consented and later changed his/her mind or because of changed clinical circumstances. 

## Neuropixels probe 

The major advance demonstrated here is recording in human brain with densely spaced high channel count simultaneously acquired across the cortical thickness. This is directly enabled 

by the Neuropixels probe. The Neuropixels probe is one of a handful of advanced neural recording probes that have built on CMOS-based microelectrode silicon probes (Hong and Lieber, 2019). The Neuropixels probe contains 960 contacts arranged in a 4-column checkerboard pattern; select subsets of 384 contacts can be recorded from simultaneously (Jun et al., 2017). We recorded in a ‘‘long column’’ configuration, in which one contact was used at each depth, and adjacent contacts alternated between two columns. This geometry of contacts allowed for semi-automatic spike sorting. 

Kilosort is an automated spike-sorting algorithm that has been designed to directly leverage the geometry of Neuropixels probes (Pachitariu et al., 2016; Steinmetz et al., 2021). We used version 2.5 of the software (Pachitariu et al., 2021), which includes more advanced drift correction. Because contacts are arranged with 20-mm spacing, waveforms for one unit are typically detected on multiple adjacent contacts. Kilosort employs a clustering algorithm across channels in order to separate units from different putative neurons, using template waveforms. Although unsupervised performance of the algorithm exceeded that of prior spike-sorting methods, manual review and curation were conducted using the Phy graphical user interface (Rossant et al., 2016). 

## Procedural hurdles for Neuropixels in humans 

The translation of Neuropixels technology from animal models to human participants required several procedural and experimental hurdles to be overcome. First and foremost is the health and safety of human participants. Therefore, risks related to the insertion of the Neuropixels probe and any modifications to standard procedures in the operating room must remain at a minimum. Notwithstanding that the thicker shank of the Neuropixels 1.0 NHP-short probe was more robust against movement in the human brain, shank breakage did still occur in some experiments. In each instance, the broken shank was retrieved. Probes typically broke in two scenarios—while attempting insertion or following insertion when there was large lateral movement. In both of the breakage scenarios we encountered, the shank 

2416 Neuron 110, 2409–2421, August 3, 2022 

**ll** 

## NeuroResource 

**==> picture [46 x 35] intentionally omitted <==**

**==> picture [420 x 353] intentionally omitted <==**

Figure 5. Cell-pair spike timing differs by distance apart (A) Left: each row is a normalized cross-correlogram for all 811-cell pairs in participant NP03 with significant cell-pair coordination index (CCI, see STAR Methods), sorted by CCI. Normalized firing rate scale bars inset. Middle: CCI by cell-pair distance apart (y axis, in mm), with identification inset top left. Right: as in plot to left, but for y axis 0 to 1,000 mm. 

(B) As in (A), but for participant NP04. 734 cell pairs included. 

broke near the probe base in one intact piece. In cases where the probe broke while attempting insertion, the broken piece was removed from the surgical field using forceps. In cases where the probe broke following insertion, the broken shank protruded from brain tissue and could be retrieved using forceps. Additionally, careful and continuous visualization of the probe during attempted insertion allowed the experimenter to see if the probe began to bend (the probe has some bend tolerance before breakage). Particularly in awake participants, keeping all voluntary movement to a minimum, following the insertion of the probe, decreased the chance for breakage. Even in cases where the shank remains intact, microscopic tissue damage occurs along the insertion trajectory. For both these reasons, we only inserted the probe in tissue that was planned for resection in the same procedure. 

To minimize the risk of infection, all probes and accessories were sterilized using standard medical-grade processes. The sterile surgical field was maintained and extended to part way along the length of the cable connecting the headstage to the 

Neuropixels PXIe acquisition module. A gowned and gloved surgeon connected the headstage to the cable and probe and positioned the probe in the micromanipulator. No probes were reused across participants. 

## Experimental hurdles for Neuropixels in humans 

The intraoperative environment imposes limitations on experimental recordings. When the Neuropixels probe is used in animal models, the probe is typically inserted quite slowly (e.g., 2– 10 mm/s) (Bo¨ hm and Lee, 2020; Kostadinov et al., 2019; Park et al., 2022; Schro¨ der et al., 2020) to optimize recording quality (Fia´ th et al., 2019), and then it is allowed to sit for 5–60 min prior to starting experimental data acquisition. However, to minimize added time in the operating room and under anesthesia, we restricted recordings to �20 min. Therefore, we started acquiring data minutes after probe insertion. Future work (likely in animal models) will be required to understand how settling time and potential stunning effects from insertion alter spike rates or patterns. Our total recording duration was also shorter than may 

Neuron 110, 2409–2421, August 3, 2022 2417 

## **ll** 

## NeuroResource 

be optimal for spike sorting, possibly leading to higher error rates. Nevertheless, we were able to acquire tens of units within minutes of probe insertion and identify distinct clusters. 

The operating room is an electrically noisy environment. During recordings, we turned off and unplugged all non-essential powered equipment. Equipment that contributed the most noise included anesthesia equipment, neuromonitoring, and the IR sensor from neuronavigation. We found that using separate needles for ground and reference reduced noise rather than electrically shorting these together. Despite these de-noising steps, the noise levels remained higher than those can be achieved using a Faraday cage for animal experiments. 

A major challenge for recording single units in human cortex is the movement of the brain caused by cardiac and respiratory pulsations; any motion of electrodes relative to the neural tissue changes the recorded extracellular potential (Buzsa´ ki et al., 2012). In this work, the skull is secured in a clamp, and the micromanipulator apparatus holding the Neuropixels probe is secured relative to this clamp. Therefore, any brain movement relative to the skull is left largely unmitigated and thus present in the recordings. The primary axis of motion is along the length of the electrode array shank and can be observed as a given putative unit shifting up and down on the contacts. Both cardiac and respiratory cycles, beyond introduction of motion, are known to have complex relationships with cell types, excitability, and waveform morphologies (Kluger et al., 2021; Mosher et al., 2020). 

Future iterations of the recording procedure will benefit from both physical and computational means of compensating for this movement. For example, untethering the probe from the insertion micromanipulator apparatus, a ‘‘floating’’ electrode approach used in chronic implants, would allow the inserted probe to move with the brain surface. Our initial attempts to manually correct for movement based on video recordings or frequency of pulsation were not successful—while the heart rate was recorded, the brain movement was not always stereotyped based on the heart rate, and there were multiple axes of movement (primarily vertical relative to the probe, but also small amounts of lateral movement). Work with additional computational methods to model and compensate for the pulsation-associated electrode drift is ongoing but faces two key challenges in human intraoperative experiments. First, the amplitude of movement is far larger than in animals and at least an order of magnitude larger relative to rodents. Second, short recording times reduce the number of recorded spikes for every neuron. Together, this means that fewer spikes are spread across a larger region of the array, making it far more difficult to correct for the motion. Densely packed and linearly arranged (in the axis of the motion) columns of electrodes, such as in the Neuropixels 2.0 design (Steinmetz et al., 2021), may be much more capable to compensate for the motion seen in human participants. Despite these challenges, we conducted post-hoc algorithmic motion correction using Kilosort 2.5, as described above. 

As with any study, there are shortcomings and weaknesses in this method. Although the intraoperative environment provides access to recording single units in human cortex, the duration of the recordings and possible tasks and behaviors are limited (e.g., only non-ambulatory). Sub-chronic implant of 

a Neuropixels probe or other comparable technology would allow for a richer dataset to explore the longitudinal behavior of unit firing. However, this is accompanied by considerable barriers regarding material safety, stabilization, and signal integrity. The current geometry of Neuropixels probes also precludes recordings in deeper subcortical structures. Even if probes were made longer, there remains the risk of probe breakage and the need to retrieve the shank. Currently available Neuropixels probes do not include the capacity for electrical stimulation. Future iterations may add this feature, at which point a new set of experiments looking at activation of the microcircuit across cortical layers will be possible. Also, as with any study incorporating spike sorting, there are false-positive and false-negative errors in assigning spiking to individual units/clusters (Harris et al., 2016). Our single-unit yields varied across participants—additional work is underway to better understand and mitigate these sources of variability, including assessing for oxidation during sterilization of the ZIF metal contact pads and decreasing brain pulsation with additional mechanical stabilization. 

In summary, use of the Neuropixels probe in humans offers widespread access to large ensembles of cortical neurons across the depth of the neocortex. Even though there are practical and technical limitations to experiments that can be conducted in the intraoperative environment, there are still myriad insights into human behavior that can be gained using this approach. 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE d RESOURCE AVAILABILITY B Lead contact 

   - B Materials availability 

   - B Data and code availability 

- d EXPERIMENTAL MODEL AND SUBJECT DETAILS d METHOD DETAILS 

   - B Probe preoperative preparation and sterilization B Recording site selection B Probe positioning and insertion B Post-hoc insertion localization B Recording B Histology 

- d QUANTIFICATION AND STATISTICAL ANALYSIS B Spike sorting 

   - B Cluster metrics B Waveform template-based cluster metrics B Motion correction and characterization B Cell-pair coordination index 

## SUPPLEMENTAL INFORMATION 

Supplemental information can be found online at https://doi.org/10.1016/j. neuron.2022.05.007. 

2418 Neuron 110, 2409–2421, August 3, 2022 

**ll** 

## NeuroResource 

## ACKNOWLEDGMENTS 

We thank Nick Steinmetz for sharing his expertise and experience regarding Neuropixels recordings. Eric Trauttman was helpful in early troubleshooting. We thank members of the Chang Lab for their helpful discussion on this manuscript. This work was supported by Howard Hughes Medical Institute. 

## AUTHOR CONTRIBUTIONS 

J.E.C., K.K.S., M.K.L., and E.F.C. designed the experiments. B.D. and M.W. designed and manufactured the Neuropixels probes. J.E.C., K.K.S., M.K.L., L.G., D.X., S.L.M., and E.F.C. performed the experiments. J.E.C., K.K.S., M.K.L., L.G., D.X., M.E.D., and S.L.M. analyzed the data. K.K.S. performed manual curation following spike sorting. V.K. performed the histology. D.X. developed MTracer. All authors discussed the data. J.E.C., K.K.S., M.K.L., L.G., D.X., M.E.D., and S.L.M. wrote the paper with input from all authors. E.F.C. supervised the work. 

## DECLARATION OF INTERESTS 

B.D. and M.W. are employees of IMEC, a non-profit nano-electronics and digital technologies research and development organization that develops, manufactures, and distributes Neuropixels probes at cost to the research community. V.K. is employed by the Neuralink Corp. 

## INCLUSION AND DIVERSITY 

We worked to ensure that the study questionnaires were prepared in an inclusive way. One or more of the authors of this paper self-identifies as an underrepresented ethnic minority in science. One or more of the authors of this paper self-identifies as a member of the LGBTQ+ community. While citing references scientifically relevant for this work, we also actively worked to promote gender balance in our reference list. 

Received: January 7, 2022 Revised: April 10, 2022 Accepted: May 10, 2022 Published: June 8, 2022 

## REFERENCES 

Aflalo, T., Kellis, S., Klaes, C., Lee, B., Shi, Y., Pejsa, K., Shanfield, K., HayesJackson, S., Aisen, M., Heck, C., et al. (2015). Neurophysiology. Decoding motor imagery from the posterior parietal cortex of a tetraplegic human. Science 348, 906–910. https://doi.org/10.1126/science.aaa5417. 

Ajiboye, A.B., Willett, F.R., Young, D.R., Memberg, W.D., Murphy, B.A., Miller, J.P., Walter, B.L., Sweet, J.A., Hoyen, H.A., Keith, M.W., et al. (2017). Restoration of reaching and grasping movements through brain-controlled muscle stimulation in a person with tetraplegia: a proof-of-concept demonstration. Lancet 389, 1821–1830. https://doi.org/10.1016/S0140-6736(17)30601-3. 

Benazzouz, A., Breit, S., Koudsie, A., Pollak, P., Krack, P., and Benabid, A.L. (2002). Intraoperative microrecordings of the subthalamic nucleus in Parkinson’s disease. Mov. Disord. 17 (suppl 3), S145–S149. https://doi.org/ 10.1002/mds.10156. 

Bere´nyi, A., Somogyva´ri, Z., Nagy, A.J., Roux, L., Long, J.D., Fujisawa, S., Stark, E., Leonardo, A., Harris, T.D., and Buzsa´ki, G. (2014). Large-scale, high-density (up to 512 channels) recording of local circuits in behaving animals. J. Neurophysiol. 111, 1132–1149. https://doi.org/10.1152/jn.00785.2013. 

Bertrand, G., and Jasper, H. (1965). Microelectrode recording of unit activity in the human thalamus. Confin. Neurol. 26, 205–208. https://doi.org/10.1159/ 000104026. 

Bo¨ hm, C., and Lee, A.K. (2020). Canonical goal-selective representations are absent from prefrontal cortex in a spatial working memory task requiring behavioral flexibility. eLife 9, e63035. https://doi.org/10.7554/eLife.63035. 

Buccino, A.P., Hurwitz, C.L., Garcia, S., Magland, J., Siegle, J.H., Hurwitz, R., and Hennig, M.H. (2020). SpikeInterface, a unified framework for spike sorting. eLife 9, e61834. https://doi.org/10.7554/eLife.61834. 

Buzsa´ki, G. (2004). Large-scale recording of neuronal ensembles. Nat. Neurosci. 7, 446–451. https://doi.org/10.1038/nn1233. 

Buzsa´ ki, G., Anastassiou, C.A., and Koch, C. (2012). The origin of extracellular fields and currents — EEG, ECoG, LFP and spikes. Nat. Rev. Neurosci. 13, 407–420. https://doi.org/10.1038/nrn3241. 

Cash, S.S., and Hochberg, L.R. (2015). The emergence of single neurons in clinical neurology. Neuron 86, 79–91. https://doi.org/10.1016/j.neuron.2015. 03.058. 

Chen, Z.S., and Pesaran, B. (2021). Improving scalability in systems neuroscience. Neuron 109, 1776–1790. https://doi.org/10.1016/j.neuron.2021.03.025. 

Chiong, W., Leonard, M.K., and Chang, E.F. (2018). Neurosurgical patients as human research subjects: ethical considerations in intracranial electrophysiology research. Neurosurgery 83, 29–37. https://doi.org/10.1093/neuros/nyx 361. 

Choi, J.R., Kim, S.M., Ryu, R.H., Kim, S.P., and Sohn, J.W. (2018). Implantable neural probes for brain-machine interfaces – Current developments and future prospects. Exp. Neurobiol. 27, 453–471. https://doi.org/10.5607/en.2018.27. 6.453. 

Chung, J.E., Joo, H.R., Fan, J.L., Liu, D.F., Barnett, A.H., Chen, S., GeaghanBreiner, C., Karlsson, M.P., Karlsson, M., Lee, K.Y., et al. (2019). High-density, long-lasting, and multi-region electrophysiological recordings using polymer electrode arrays. Neuron 101, 21–31.e5. https://doi.org/10.1016/j.neuron. 2018.11.002. 

Chung, J.E., Magland, J.F., Barnett, A.H., Tolosa, V.M., Tooker, A.C., Lee, K.Y., Shah, K.G., Felix, S.H., Frank, L.M., and Greengard, L.F. (2017). A fully automated approach to spike sorting. Neuron 95, 1381–1394.e6. https://doi. org/10.1016/j.neuron.2017.08.030. 

Collinger, J.L., Wodlinger, B., Downey, J.E., Wang, W., Tyler-Kabara, E.C., Weber, D.J., McMorland, A.J.C., Velliste, M., Boninger, M.L., and Schwartz, A.B. (2013). High-performance neuroprosthetic control by an individual with tetraplegia. Lancet 381, 557–564. https://doi.org/10.1016/S0140-6736(12) 61816-9. 

Constantinidis, C., and Goldman-Rakic, P.S. (2002). Correlated discharges among putative pyramidal neurons and interneurons in the primate prefrontal cortex. J. Neurophysiol. 88, 3487–3497. https://doi.org/10.1152/jn.00188.2002. 

Dutta, B., Andrei, A., Harris, T.D., Lopez, C.M., O’Callahan, J., Putzeys, J., Raducanu, B.C., Severi, S., Stavisky, S.D., Trautmann, E.M., and Welkenhuysen, M. (2019). The Neuropixels probe: a CMOS based integrated microsystems platform for neuroscience and brain-computer interfaces. In IEEE international electron devices meeting (IEDM), 2019 (IEEE Publications), pp. 10.1.1–10.1.4. 

Ekstrom, A.D., Kahana, M.J., Caplan, J.B., Fields, T.A., Isham, E.A., Newman, E.L., and Fried, I. (2003). Cellular networks underlying human spatial navigation. Nature 425, 184–188. https://doi.org/10.1038/nature01964. 

Feinsinger, A., Pouratian, N., Ebadi, H., Adolphs, R., Andersen, R., Beauchamp, M.S., Chang, E.F., Crone, N.E., Collinger, J.L., Fried, I., et al. (2022). Ethical commitments, principles, and practices guiding intracranial neuroscientific research in humans. Neuron 110, 188–194. https://doi.org/ 10.1016/j.neuron.2021.11.011. 

Fia´ th, R., Ma´ rton, A.L., Ma´ tya´ s, F., Pinke, D., Ma´ rton, G., To´ th, K., and Ulbert, I. (2019). Slow insertion of silicon probes improves the quality of acute neuronal recordings. Sci. Rep. 9, 111. https://doi.org/10.1038/s41598-018-36816-z. 

Fried, I., MacDonald, K.A., and Wilson, C.L. (1997). Single neuron activity in human hippocampus and amygdala during recognition of faces and objects. Neuron 18, 753–765. https://doi.org/10.1016/s0896-6273(00)80315-3. 

Gaucher, Q., Panniello, M., Ivanov, A.Z., Dahmen, J.C., King, A.J., and Walker, K.M. (2020). Complexity of frequency receptive fields predicts tonotopic variability across species. eLife 9, e53462. https://doi.org/10.7554/eLife.53462. 

Gilja, V., Pandarinath, C., Blabe, C.H., Nuyujukian, P., Simeral, J.D., Sarma, A.A., Sorice, B.L., Perge, J.A., Jarosiewicz, B., Hochberg, L.R., et al. (2015). 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, 2409–2421, August 3, 2022 2419 

## **ll** 

## NeuroResource 

Clinical translation of a high-performance neural prosthesis. Nat. Med. 21, 1142–1145. https://doi.org/10.1038/nm.3953. 

Guridi, J., Rodriguez-Oroz, M.C., Lozano, A.M., Moro, E., Albanese, A., Nuttin, B., Gybels, J., Ramos, E., and Obeso, J.A. (2000). Targeting the basal ganglia for deep brain stimulation in Parkinson’s disease. Neurology 55 (Supplement 6 ), S21–S28. 

Harris, K.D., Quiroga, R.Q., Freeman, J., and Smith, S.L. (2016). Improving data quality in neuronal population recordings. Nat. Neurosci. 19, 1165– 1174. https://doi.org/10.1038/nn.4365. 

Hill, D.N., Mehta, S.B., and Kleinfeld, D. (2011). Quality metrics to accompany spike sorting of extracellular signals. J. Neurosci. 31, 8699–8705. https://doi. org/10.1523/JNEUROSCI.0971-11.2011. 

Hochberg, L.R., Bacher, D., Jarosiewicz, B., Masse, N.Y., Simeral, J.D., Vogel, J., Haddadin, S., Liu, J., Cash, S.S., van der Smagt, P., and Donoghue, J.P. (2012). Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. Nature 485, 372–375. https://doi.org/10.1038/nature11076. 

Hochberg, L.R., Serruya, M.D., Friehs, G.M., Mukand, J.A., Saleh, M., Caplan, A.H., Branner, A., Chen, D., Penn, R.D., and Donoghue, J.P. (2006). Neuronal ensemble control of prosthetic devices by a human with tetraplegia. Nature 442, 164–171. https://doi.org/10.1038/nature04970. 

Hong, G., and Lieber, C.M. (2019). Novel electrode technologies for neural recordings. Nat. Rev. Neurosci. 20, 330–345. https://doi.org/10.1038/s41583019-0140-6. 

Hughes, C.L., Flesher, S.N., Weiss, J.M., Downey, J.E., Boninger, M., Collinger, J.L., and Gaunt, R.A. (2021). Neural stimulation and recording performance in human sensorimotor cortex over 1500 days. J. Neural Eng. 18, 045012. https://doi.org/10.1088/1741-2552/ac18ad. 

Hutchison, W.D., Allan, R.J., Opitz, H., Levy, R., Dostrovsky, J.O., Lang, A.E., and Lozano, A.M. (1998). Neurophysiological identification of the subthalamic nucleus in surgery for Parkinson’s disease. Ann. Neurol. 44, 622–628. https:// doi.org/10.1002/ana.410440407. 

Juavinett, A.L., Bekheet, G., and Churchland, A.K. (2019). Chronically implanted Neuropixels probes enable high-yield recordings in freely moving mice. eLife 8, e47188. https://doi.org/10.7554/eLife.47188. 

Jun, J.J., Steinmetz, N.A., Siegle, J.H., Denman, D.J., Bauza, M., Barbarits, B., Lee, A.K., Anastassiou, C.A., Andrei, A., Aydın, C¸ ., et al. (2017). Fully integrated silicon probes for high-density recording of neural activity. Nature 551, 232–236. https://doi.org/10.1038/nature24636. 

Kluger, D.S., Balestrieri, E., Busch, N.A., and Gross, J. (2021). Respiration aligns perception with neural excitability. eLife 10, e70907. https://doi.org/ 10.7554/eLife.70907. 

Kostadinov, D., Beau, M., Blanco-Pozo, M., and Hausser, M. (2019). Predictive€ and reactive reward signals conveyed by climbing fiber inputs to cerebellar Purkinje cells. Nat. Neurosci. 22, 950–962. https://doi.org/10.1038/s41593019-0381-8. 

Larkum, M. (2013). A cellular mechanism for cortical associations: an organizing principle for the cerebral cortex. Trends Neurosci. 36, 141–151. https://doi.org/10.1016/j.tins.2012.11.006. 

Lee, D., Port, N.L., Kruse, W., and Georgopoulos, A.P. (1998). Variability and correlated noise in the discharge of neurons in motor and parietal areas of the primate cortex. J. Neurosci. 18, 1161–1170. 

Levy, R., Hutchison, W.D., Lozano, A.M., and Dostrovsky, J.O. (2000). Highfrequency synchronization of neuronal activity in the subthalamic nucleus of parkinsonian patients with limb tremor. J. Neurosci. 20, 7766–7775. 

Magland, J., Jun, J.J., Lovero, E., Morley, A.J., Hurwitz, C.L., Buccino, A.P., Garcia, S., and Barnett, A.H. (2020). SpikeForest, reproducible web-facing ground-truth validation of automated neural spike sorters. eLife 9, e55167. https://doi.org/10.7554/eLife.55167. 

Maynard, E.M., Nordhausen, C.T., and Normann, R.A. (1997). The Utah intracortical Electrode Array: a recording structure for potential brain-computer interfaces. Electroencephalogr. Clin. Neurophysiol. 102, 228–239. https://doi. org/10.1016/s0013-4694(96)95176-0. 

Misra, A., Burke, J.F., Ramayya, A.G., Jacobs, J., Sperling, M.R., Moxon, K.A., Kahana, M.J., Evans, J.J., and Sharan, A.D. (2014). Methods for implantation of micro-wire bundles and optimization of single/multi-unit recordings from human mesial temporal lobe. J. Neural Eng. 11, 026013. https://doi.org/10.1088/ 1741-2560/11/2/026013. 

Mongen, M.A., and Willems, P.W.A. (2019). Current accuracy of surface matching compared to adhesive markers in patient-to-image registration. Acta Neurochir. 161, 865–870. https://doi.org/10.1007/s00701-019-03867-8. 

Mosher, C.P., Wei, Y., Kaminski,� J., Nandi, A., Mamelak, A.N., Anastassiou, C.A., and Rutishauser, U. (2020). Cellular classes in the human brain revealed in vivo by heartbeat-related modulation of the extracellular action potential waveform. Cell Rep. 30, 3536–3551.e6. https://doi.org/10.1016/j.celrep. 2020.02.027. 

Musk, E., and Neuralink. (2019). An integrated brain-machine interface platform With thousands of channels. J. Med. Internet Res. 21, e16194. https:// doi.org/10.2196/16194. 

Nordhausen, C.T., Rousche, P.J., and Normann, R.A. (1994). Optimizing recording capabilities of the Utah intracortical Electrode Array. Brain Res. 637, 27–36. https://doi.org/10.1016/0006-8993(94)91213-0. 

Ojemann, G.A., Creutzfeldt, O., Lettich, E., and Haglund, M.M. (1988). Neuronal activity in human lateral temporal cortex related to short-term verbal memory, naming and reading. Brain 111, 1383–1403. https://doi.org/10.1093/ brain/111.6.1383. 

Ojemann, G.A., Schoenfield-McNeill, J., and Corina, D.P. (2002). Anatomic subdivisions in human temporal cortical neuronal activity related to recent verbal memory. Nat. Neurosci. 5, 64–71. https://doi.org/10.1038/nn785. 

Pachitariu, M., Rossant, C., Steinmetz, N., Colonell, J., Bondy, A.G., Winter, O., Kushbanga, B., J, Sosa, M., O’Shea, D., et al. (2021). MouseLand/ Kilosort: Kilosort 2.5. https://doi.org/10.5281/zenodo.4482749. 

Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M., Kenneth, D., and H. (2016). Kilosort: realtime spike-sorting for extracellular electrophysiology with hundreds of channels. bioRxiv. https://doi.org/10.1101/061481. 

Park, J., Phillips, J.W., Guo, J.Z., Martin, K.A., Hantman, A.W., and Dudman, J.T. (2022). Motor cortical output for skilled forelimb movement is selectively distributed across projection neuron classes. Sci. Adv. 8, eabj5167. https:// doi.org/10.1126/sciadv.abj5167. 

Paulk, A.C., Kfir, Y., Khanna, A.R., Mustroph, M.L., Trautmann, E.M., Soper, D.J., Stavisky, S.D., Welkenhuysen, M., Dutta, B., Shenoy, K.V., et al. (2022). Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex. Nat. Neurosci. 25, 252–263. https:// doi.org/10.1038/s41593-021-00997-0. 

Pochay, P., Wise, K.D., Allard, L.F., and Rutledge, L.T. (1979). A multichannel depth probe fabricated using electron-beam lithography. IEEE Trans. Biomed. Eng. 26, 199–206. https://doi.org/10.1109/TBME.1979.326558. 

Quiroga, R.Q., Reddy, L., Kreiman, G., Koch, C., and Fried, I. (2005). Invariant visual representation by single neurons in the human brain. Nature 435, 1102– 1107. https://doi.org/10.1038/nature03687. 

Rossant, C., Kadir, S.N., Goodman, D.F.M., Schulman, J., Hunter, M.L.D., Saleem, A.B., Grosmark, A., Belluscio, M., Denfield, G.H., Ecker, A.S., et al. (2016). Spike sorting for large, dense electrode arrays. Nat. Neurosci. 19, 634–641. https://doi.org/10.1038/nn.4268. 

Schro¨ der, S., Steinmetz, N.A., Krumin, M., Pachitariu, M., Rizzi, M., Lagnado, L., Harris, K.D., and Carandini, M. (2020). Arousal modulates retinal output. Neuron 107, 487–495.e9. https://doi.org/10.1016/j.neuron.2020.04.026. 

Shobe, J.L., Claar, L.D., Parhami, S., Bakhurin, K.I., and Masmanidis, S.C. (2015). Brain activity mapping at multiple scales with silicon microprobes containing 1,024 electrodes. J. Neurophysiol. 114, 2043–2052. https://doi.org/10. 1152/jn.00464.2015. 

Smith, M.A., and Kohn, A. (2008). Spatial and temporal scales of neuronal correlation in primary visual cortex. J. Neurosci. 28, 12591–12603. https://doi.org/ 10.1523/JNEUROSCI.2929-08.2008. 

Steinmetz, N.A., Aydin, C., Lebedeva, A., Okun, M., Pachitariu, M., Bauza, M., Beau, M., Bhagat, J., Bo¨ hm, C., Broux, M., et al. (2021). Neuropixels 2.0: A 

2420 Neuron 110, 2409–2421, August 3, 2022 

**ll** 

## NeuroResource 

miniaturized high-density probe for stable, long-term brain recordings. Science 372, eabf4588. https://doi.org/10.1126/science.abf4588. 

Steinmetz, N.A., Koch, C., Harris, K.D., and Carandini, M. (2018). Challenges and opportunities for large-scale electrophysiology with Neuropixels probes. Curr. Opin. Neurobiol. 50, 92–100. https://doi.org/10.1016/j.conb.2018. 01.009. 

Szymanski, L.J., Kellis, S., Liu, C.Y., Jones, K.T., Andersen, R.A., Commins, D., Lee, B., McCreery, D.B., and Miller, C.A. (2021). Neuropathological effects of chronically implanted, intracortical microelectrodes in a tetraplegic patient. J. Neural Eng. 18, 0460b9. https://doi.org/10.1088/1741-2552/ac127e. 

Trautmann, E.M., Stavisky, S.D., Lahiri, S., Ames, K.C., Kaufman, M.T., O’Shea, D.J., Vyas, S., Sun, X., Ryu, S.I., Ganguli, S., et al. (2019). Accurate estimation of neural population dynamics without spike sorting. Neuron 103, 292–308.e4. https://doi.org/10.1016/j.neuron.2019.05.003. 

van Daal, R.J.J., Aydin, C¸ ., Michon, F., Aarts, A.A.A., Kraft, M., Kloosterman, F., and Haesler, S. (2021). Implantation of Neuropixels probes for chronic 

recording of neuronal activity in freely behaving mice and rats. Nat. Protoc. 16, 3322–3347. https://doi.org/10.1038/s41596-021-00539-9. 

Vaz, A.P., Wittig, J.H., Inati, S.K., and Zaghloul, K.A. (2020). Replay of cortical spiking sequences during human memory retrieval. Science 367, 1131–1134. https://doi.org/10.1126/science.aba0672. 

Ward, A.A., and Thomas, L.B. (1955). The electrical activity of single units in the cerebral cortex of man. Electroencephalogr. Clin. Neurophysiol. 7, 135–136. https://doi.org/10.1016/0013-4694(55)90067-5. 

Wood, F., Black, M.J., Vargas-Irwin, C., Fellows, M., and Donoghue, J.P. (2004). On the variability of manual spike sorting. IEEE Trans. Biomed. Eng. 51, 912–918. https://doi.org/10.1109/TBME.2004.826677. 

Wyler, A.R., Ojemann, G.A., and Ward, A.A. (1982). Neurons in human epileptic cortex: correlation between unit and EEG activity. Ann. Neurol. 11, 301–308. https://doi.org/10.1002/ana.410110311. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 110, 2409–2421, August 3, 2022 2421 

**ll** 

NeuroResource 

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|REAGENT or RESOURCE<br>SOURCE<br>IDENTIFIER|
|---|---|---|
||||
|Deposited data|||
||||
|Raw and analyzed data<br>This paper|||
|Software and algorithms|||
|Kilosort 2.5<br>Steinmetz, 2021<br>https://zenodo.org/record/4482749#.YhVJHOjMKUk|||
|Phy<br>https://phy.readthedocs.io/en/latest/<br>https://github.com/cortex-lab/phy|||
|SpikeInterface<br>https://spikeinterface.readthedocs.io/en/latest/<br>v0.90.0, pypi|||
|MTracer<br>Thispaper<br>https://doi.org/10.5281/zenodo.6529091|||
|Cell-pair coordination index<br>This paper<br>https://doi.org/10.5281/zenodo.6528318|||



## RESOURCE AVAILABILITY 

## Lead contact 

Further information and requests should be directed to and will be fulfilled by the lead contact, Edward F. Chang (edward.chang@ ucsf.edu). 

## Materials availability 

This study did not generate new unique reagents. 

## Data and code availability 

All data and code reported in this paper will be shared by the lead contact upon request. DOIs and code repositories are listed in the key resources table. Any additional information required to reanalyze the data reported in this paper is available from the lead contact upon request. 

## EXPERIMENTAL MODEL AND SUBJECT DETAILS 

The experimental protocol was approved by the UCSF Institutional Review Board. Fifteen participants were included in the study (Table 1), and all provided written informed consent. Eleven participants had medically refractory seizures from temporal lobe epilepsy, requiring surgical management during which the anterior temporal lobe was resected from a lateral approach. Two participants had a tumor and two had a cavernous malformation with surrounding epileptogenic tissue that was resected. In some cases, clinical grid and strip ECoG arrays were used as part of routine clinical care for intraoperative monitoring. Participants were either under general anesthesia or under sedation (awake or asleep, Table 1) during the recordings according to clinical need (e.g. intraoperative stimulation mapping procedures). For all cases using general anesthesia, a combination of dexmedetomidine, propofol, and fentanyl or remifentanil were administered. In cases where recording was done in the awake or asleep state, a combination of dexmedetomidine and remifentanil was administered, with propofol sometimes being used during initial induction. 

## METHOD DETAILS 

## Probe preoperative preparation and sterilization 

Neuropixels 1.0 NHP-short probes, with 10mm long shanks and metal dovetail caps (IMEC, Leuven, Belgium), were used for all recordings. These probes are adapted and modified versions of the Neuropixels 1.0 rodent probes (Jun et al., 2017) that are electronically identical, with the notable difference of increased shank thickness from 24mm to 97mm (Paulk et al., 2022). This increased thickness allowed for tolerance of greater mechanical forces for larger brain recordings. Two 27G subdermal needle electrodes (Ambu, Columbia, MD) were soldered separately to the probe flex-interconnect to serve as ground and reference using lead-free solder and two strands of twisted 36 AWG copper wire. The connected needle electrodes were approximately 20cm long, to allow for insertion into the skin flap following probe insertion. No additional modifications were made to the Neuropixels probe. Probes with soldered needle electrodes were installed into custom CleanCut mounting cards (Oliver Healthcare Packaging, Grand Rapids, MI) for storage and transport. 

The Neuropixels probe was secured to the metal cap dovetail probe mount (IMEC, Leuven, Belgium). The probe mount was in turn attached to either a Elekta microdrive (Elekta, Stockholm, Sweden) or Narishige (Tokyo) micromanipulator (MM-3 or M-3333). The 

e1 Neuron 110, 2409–2421.e1–e3, August 3, 2022 

**ll** 

## NeuroResource 

**==> picture [46 x 35] intentionally omitted <==**

manipulator/microdrive was secured to the Mayfield skull clamp using an 3-joint mounting arm (Noga NF9038CA) and Nano clamp (Manfrotto 386BC-1, Cassola, Italy) assembly attached to the primary articulating arm and C-clamp of the Integra Brain Retractor System A2012 (Integra, Princeton, NJ). Probes, headstages, interface cables, Narishige micromanipulators, screwdrivers, and probe mount with metal cap dovetail were all separately sterilized according to standard protocols of ethylene oxide sterilization, while the Elekta micromanipulators were sterilized using Sterrad prior to use. Probes were not reused across participants. 

## Recording site selection 

In all cases, the insertion of Neuropixels probes was targeted to cortical tissue that was destined for resection in the same procedure based on clinical criteria. In cases where a tumor or cavernoma was resected, the recording was targeted to radiographically normal tissue (no T2 hyperintensity) which would require resection as part of the transcortical approach. In all cases the recorded tissue appeared normal intraoperatively. The specific sites were selected to be the crown of surface gyri which allowed for direct visualization and monitoring of the insertion and penetration through cortical layers. See below for post-hoc insertion localization. 

## Probe positioning and insertion 

Each participant was secured with a Mayfield skull clamp. A compatible C-clamp was then attached to the skull clamp, and in turn, a primary articulating bar was attached to the C-clamp (all items contained in Integra Brain Retractor System A2012). A clamp (Manfrotto 386BC-1) was used to attach a 3-joint mounting arm (Noga NF9038CA) to the articulating bar. The 3-joint mounting arm was connected to a micromanipulator (Elekta or Narishige MM-3 or M-3333) which held the Neuropixels assembly. All equipment was sterilized according to standard protocols using either Sterrad or ethylene oxide sterilization. The articulating arms were positioned to place the micromanipulator above the target insertion site, and the Neuropixels probe was lowered using the micromanipulator to a target depth of 6 to 8 mm from the brain surface, at a rate of 50–75 mm/sec. Insertion trajectory was approximately perpendicular to the surface. Insertion locations were estimated through a combination of intraoperative navigation, intraoperative photos taken during the surgery, and histology when available. In some cases, a piotomy was performed at the site of insertion, which also reduced the risk for probe fracture. We hypothesized this would also increase unit yield, although this did not appear to have an effect. Recordings were typically started to visualize probe insertion (Video S1). 

## Post-hoc insertion localization 

Localization of the probe insertion site was done using preoperative MRI with fiducial markers and intraoperative neuronavigation (Brainlab, Munich, Germany), which together have an average target error of 2.49 mm (Mongen and Willems, 2019). Beyond this localization, visible surface vasculature from intraoperative photos was used and matched with preoperative MRI. When available, resection boundaries from intraoperative photos were matched to postoperative MRI. In cases where grid and depth electrodes were implanted prior to recording, these images and combined reconstruction were also used to further supplement insertion localization. 

## Recording 

Data were collected using a custom-constructed rig including a Windows machine, PXI chassis (NI PXIe-1071), PXI Multifunction I/O Module (NI PXIe-6341), NI SHC68-68-EPM shielded cable, Neuropixels PXIe Acquisition Module, and NI BNC-2110 Connector Block with SpikeGLX 3.0 (http://billkarsh.github.io/SpikeGLX/) acquisition software. In some experiments, speakers were used to present auditory stimuli and a microphone was used for recording; these signals were also acquired as analog inputs synchronized with the neural data. The Neuropixels probe was configured to acquire from 384 channels in a ‘long column’ layout, providing the greatest possible depth span of recording while acquiring from a contact at each depth. Total recording span was 7.67mm. Ground and reference needle electrodes were inserted into the scalp adjacent to the craniotomy. AP gain was 500 and LF gain was 250. During data acquisition, all non-essential equipment in the operating room was unplugged or run using battery power in order to reduce electrical noise. By iterativelyturning off pieces ofequipment,whenpossible, and listening tothehigh-passfilteredsignalfroma recording channel,wefound the operative table, electrocautery, and electronics associated with intravenous lines should be on direct current, including syringe pumps and blood/fluid warmers. Other key environmentalsources of noise included neuromonitoring and the Brainlab neuronavigation system. 

## Histology 

All tissue that had a device inserted was previously determined to be bound for resection. Despite this, in some cases the tissue could not be safely resected en bloc due to proximity to critical vascular structures, and as such, histology was not performed on all insertion sites. In cases where en bloc resection of the insertion site was possible, the tissue was drop-fixed in ice-cold formalin before being cryoprotected and sectioned into 50-mm thick sections. Tissue was then stained with luxol fast blue and neutral red. 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

## Spike sorting 

Kilosort 2.5 (Pachitariu et al., 2016, 2021; Steinmetz et al., 2021) was used for spike sorting on a server with an NVIDIA GPU, CUDA, and Matlab installed. Sorting was conducted on data after final recording depth was achieved. Following automated spike sorting, Phy (Rossant et al., 2016) was used for manual curation of clusters by an experienced electrophysiologist (KKS). 

Neuron 110, 2409–2421.e1–e3, August 3, 2022 e2 

**ll** 

NeuroResource 

## Cluster metrics 

Amplitude histogram truncation was calculated using code based upon SpikeInterface (Buccino et al., 2020). This metric provides an estimate of the miss rate due to spike amplitude falling below the detection threshold, based upon the amplitude histogram. The empirical amplitude histogram is modeled using a gaussian, with the fraction of the estimated events below the detection amplitude of the modelbeingreported.Higherproportionofamplitudehistogramtruncationreflectsahigherestimatedfalsenegativerateandlowercluster quality. 

The proportion of events violating the refractory period (Hill et al., 2011) was calculated using code based upon SpikeInterface (Buccino et al., 2020). This metric reports the number of events in a cluster below an inter-spike-interval threshold of 1 ms. Higher proportion of events that violate the refractory period reflects a higher estimated false positive rate and lower cluster quality. 

Presence ratio is a metric that reports the fraction of time a unit is present within the recording epoch. If a unit is unstable, it would drop in and out of the recording, thereby being only in a fraction of the total recording epoch. Presence ratio was calculated using code based upon SpikeInterface (Buccino et al., 2020) as follows: First, the epoch is divided into 100 bins. If a unit has an event within a bin, it is considered present in that bin. The presence ratio is then the number of bins that the unit is present divided by the total number of bins from the recording. 

D-prime (Hill et al., 2011) is a linear discriminant analysis-based metric to quantify isolation distance from other clusters. Higher D-prime reflects higher cluster quality and lower estimated false positive rates. 

Isolation score (Chung et al., 2017) is a nearest-neighbor based metric which reports the proportion of spikes whose nearest neighbor in feature space comes from the same cluster. Higher isolation reflects higher cluster quality and lower estimated false positive rate. 

## Waveform template-based cluster metrics 

For every putative unit the template waveform is calculated by taking the mean of all events after Kilosort motion correction. The primary channel is then defined as the electrode with highest peak amplitude. For a channel to be considered involved or active in a given unit, the peak amplitude on that channel must be greater than or equal to 10% of the peak amplitude of the primary channel. 

Spread is defined as the distance between the primary channel and the most distant channel with template peak amplitude greater than or equal to 10% of the peak amplitude of the primary channel. 

Amplitude decay is calculated by taking the channels that have peak amplitude greater than or equal to 10% of peak amplitude and then using a linear regression to calculate the best-fit line of amplitude versus distance. The absolute value of the slope of this line is the amplitude decay, reported in mv decrease per mm. 

## Motion correction and characterization 

Motion correction was conducted using Kilosort 2.5 (Pachitariu et al., 2016, 2021; Steinmetz et al., 2021). Additional characterization of fast timescale motion was done with custom software (MTracer, https://github.com/yaxigeigei/MTracer). In spike maps, tissue movements are reflected in the shifting of spiking patterns across time. Within the patterns, we can identify and follow streaks of active, high-amplitude, and spatially isolated spikes that mark precise instantaneous tissue position (example shown in Figure 4B; green trace). One to five such streaks were manually traced (with makima interpolation at 50 samples/s) for each recording using MTracer. The traces were next highpass filtered at 0.1 Hz to isolate the respiration and heartbeat components (Figure 4C). Instantaneous peak-to-peak movement amplitudes were computed after Hilbert transform. Each movement trace has its mean amplitude, and the overall mean amplitude of a recording is the average across all trace means. 

## Cell-pair coordination index 

Cell-pair coordination index is a cell-pair metric to capture the relative coordinated activity (within 50ms) compared to activity seen at slightly longer timescales (50 to 100ms). Single-unit pair firing relationships were first quantified using cross-correlograms. For each cross correlogram that contained at least 100 events within a 1 second window (±0.5s), the sum of events was calculated in three different windows: from -50 to 50ms (s0), -100 to -50ms (s1), and 50 to 100ms (s2). 

The cell coordination inderx (CCI) was then defined as: 

**==> picture [82 x 21] intentionally omitted <==**

As such, a more positive CCI reflects higher cell-pair activity from -50 to 50 ms compared to -100 to -50 ms and 50 to 100 ms, while a negative CCI corresponds to higher cell pair activity seen combined in -100 to -50 ms and 50 to 100 ms compared to the -50 to 50 ms window. 

CCI was only calculated for cell pairs with cross-correlograms having a minimum of 50 events falling within the -100 to +100 ms window. To control for CCI relationships that could be a product of normal rate variations, a shuffled cross-correlogram was generated from circularly-shuffled spike times. This was repeated 10,000 times to generate a distribution of shuffled CCIs for every cellpair. The non-shuffled CCI was then compared against the shuffled distribution, and was deemed to be a significant relationship if the CCI was within the upper or lower 5th percentile of the shuffled distribution. Only these cell-pairs were included for further analyses. 

e3 Neuron 110, 2409–2421.e1–e3, August 3, 2022 

