Technical RepoRT 

**https://doi.org/10.1038/s41593-021-00997-0** 

**==> picture [149 x 49] intentionally omitted <==**

**==> picture [72 x 15] intentionally omitted <==**

## **Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex** 

**Angelique C. Paulk[1,2]**[ ✉] **, Yoav Kfir[3] , Arjun R. Khanna[3] , Martina L. Mustroph[4] , Eric M. Trautmann[5,6,7,8,9,10,11] , Dan J. Soper[1] , Sergey D. Stavisky[9,10,12,13] , Marleen Welkenhuysen[14] , Barundeb Dutta[14] , Krishna V. Shenoy[8,9,10,13,15,16] , Leigh R. Hochberg[1,2,17,18] , R. Mark Richardson[3] , Ziv M. Williams[3,19]**[ ✉] **and Sydney S. Cash[1,2,19]**[ ✉] 

**Recent advances in multi-electrode array technology have made it possible to monitor large neuronal ensembles at cellular resolution in animal models. In humans, however, current approaches restrict recordings to a few neurons per penetrating electrode or combine the signals of thousands of neurons in local field potential (LFP) recordings. Here we describe a new probe variant and set of techniques that enable simultaneous recording from over 200 well-isolated cortical single units in human participants during intraoperative neurosurgical procedures using silicon Neuropixels probes. We characterized a diversity of extracellular waveforms with eight separable single-unit classes, with differing firing rates, locations along the length of the electrode array, waveform spatial spread and modulation by LFP events such as inter-ictal discharges and burst suppression. Although some challenges remain in creating a turnkey recording system, high-density silicon arrays provide a path for studying human-specific cognitive processes and their dysfunction at unprecedented spatiotemporal resolution.** 

esearch programs now routinely rely on the analysis of action potentials (APs) from hundreds and even thousands of neuRrons owing to major technological advances, providing a rich understanding of the coordinated activity of large neuronal ensembles underlying sensory, motor and cognitive operations[1][–][4] . Although the advances have been most pronounced in animal models, there have been parallel, albeit slower, advances in the ability to record from single neurons in humans. Performed since the mid-1950s[5] , at least four high-resolution, single-neuron recording technologies can currently be used in human participants in acute, subacute and even chronic settings. These include microwire bundles[6] , laminar microelectrode arrays[7] , microelectrode contacts arranged on a grid for use above the pia or on the shaft of a depth electrode[8] and the ‘Utah’ planar array of penetrating microelectrodes[9] . Recent technological developments include thin-film-based systems with organic polymer electrodes (often referred to as micro-electrocorticography or ‘µECoG’), which provide access to cortical[10][,][11] and hippocampal recordings[12] . 

Although these approaches are nominally capable of recording APs, all are limited to capturing only 10–150 separable units (typically well below 150) per device. In addition, these approaches rarely 

allow for high-quality isolation of APs from more than one neuron on a single recording channel (and rarely a single neuron sampled on multiple channels). This constraint biases observations toward neurons with large and distinct waveforms with relatively high spike rates. Overall, human electrophysiology technical capabilities have substantially lagged what is possible in animals. 

Neural recording systems for animal models have advanced more rapidly, which has included a recent landmark technological advance, the Neuropixels probe, a fully integrated linear silicon array covered with microelectrode contacts at 20-µm spacing (Fig. 1a). The Neuropixels 1.0 probes can simultaneously record from 384 user-selectable channels distributed along a 24 µm × 70 µm × 10 mm shank. This system, introduced in 2017, has already enjoyed widespread adoption for recording in rodents[1][,][2] and non-human primates (NHPs)[3] , with continuing improvements[4] . 

Recording single-unit neural activity in humans is increasingly common in both research and clinical care[13][–][16] , including real-time neurophysiology, to guide deep brain stimulating electrodes for neurological disorders like Parkinson’s disease[17][,][18] . Utah arrays have proven instrumental in enabling both basic neuroscience and clinical studies at the level of single neurons and at the population 

1Center for Neurotechnology and Neurorecovery, Department of Neurology, Massachusetts General Hospital, Boston, MA, USA. 2Department of Neurology, Harvard Medical School, Boston, MA, USA.[3] Department of Neurosurgery, Harvard Medical School and Massachusetts General Hospital, Boston, MA, USA.[4] Department of Neurosurgery, Harvard Medical School and Brigham & Women’s Hospital, Boston, MA, USA.[5] Department of Neuroscience, Columbia University Medical Center, New York City, NY, USA.[6] Zuckerman Institute, Columbia University, New York City, NY, USA. 7Grossman Center for the Statistics of Mind, Columbia University Medical Center, New York City, NY, USA. 8Department of Electrical Engineering, Stanford University, Stanford, CA, USA.[9] Wu Tsai Neurosciences Institute and Bio-X Institute, Stanford University, Stanford, CA, USA.[10] Howard Hughes Medical Institute at Stanford University, Stanford, CA, USA.[11] Columbia University, New York City, NY, USA.[12] Department of Neurological Surgery, University of California at Davis, Davis, CA, USA.[13] Department of Neurosurgery, Stanford University, Stanford, CA, USA.[14] IMEC, Leuven, Belgium.[15] Department of Bioengineering, Stanford University, Stanford, CA, USA.[16] Department of Neurobiology, Stanford University, Stanford, CA, USA.[17] VA RR&D Center for Neurorestoration and Neurotechnology, Rehabilitation R&D Service, Providence VA Medical Center, Providence, RI, USA.[18] School of Engineering and Carney Institute for Brain Science, Brown University, Providence, RI, USA.[19] These authors contributed equally: Ziv M. Williams, Sydney S. Cash. ✉ e-mail: apaulk@mgh.harvard.edu; zwilliams@mgh.harvard.edu; scash@mgh.harvard.edu 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**252** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [419 x 540] intentionally omitted <==**

**----- Start of picture text -----**<br>
a c e f<br>g<br>d<br>b<br>h i k<br>Pt. 03<br>Temporal<br>lobe<br>Cortex<br>j Pt. 02<br>Neuropixels<br>Neuropixels White matter<br>dlPFC<br>200<br>0<br>l Pt. 01 m Pt. 02 –200<br>100 µV 100 µV<br>10 ms 10 ms<br>Headstage<br>Flex cable Ground contacts<br>External reference contacts<br>10 mm Shank<br>µ<br>V<br>**----- End of picture text -----**<br>


**Fig. 1 | Human neocortical neurons recorded using Neuropixels 1.0-S probes. a** – **d** , Diagram of the Neuropixels 1.0-S probe with a headstage and the ground and reference pads indicated (outlined in cyan, left) and preparation in a sterile field, with the probe outlined in cyan ( **a** ), set up before electrode insertion, including opening the sterile electrode in the packaging ( **b** ), handling and connecting to wires and visual inspection ( **c** ) and testing in saline ( **d** ). **e** , Electrode attached to three sterile stylets on the ROSA robot for insertion. **f** , Electrode inserted into the dlPFC through a burr hole using the ROSA robot. **g** , Electrode inserted into the lateral temporal cortex using a three-axis micromanipulator attached to a Greenberg retractor. **h** , 3D model of the DBS burr hole location with a model of the Neuropixels probe. **i** , Location zoomed-in view on the 3D view with the gray wire the reference and the black wire the ground. **j** , With the putative Neuropixels location overlaid on the preoperative MRI (top) during one DBS case, which was mapped based on the implanted location of the DBS electrode (and the burr hole) and the angles of the Neuropixels probe based on the dimensions of the holder and burr hole as well as the closest visible cortical gyrus. **k** , Putative location and likely depth of the electrode in an open craniotomy case for epilepsy surgery in the lateral temporal cortex (left two columns), with the depth informed by the electrophysiology, where the LFP shows a clear difference between superficial electrodes and deeper contacts, as highlighted here in a color scale indicating voltage. **l** , **m** , Example recording from Pt. 01 and Pt. 02 in the dlPFC across multiple channels, with APs shown extending across multiple channels. The light green filled-in box in the background traces are then expanded in the green-outlined voltage traces in the foreground. In **a** , **e** , **j** and **k** : cyan rectangles are highlighting the location of the Neuropixels probe. 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**253** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

level. Research to develop clinical brain–computer interfaces for individuals with severe speech and motor disorders involved Utah arrays recording small populations of single neurons. These studies range in application from decoding handwriting and controlling prosthetic limbs and reanimating upper extremities to providing sensory feedback (via intracortical microstimulation)[19][–][24] . Adapting the Neuropixels recording system for similar use in clinical research presents a viable approach for building on these prior demonstrations of the utility of cellular resolution neural recordings for clinical and neuroscientific applications. 

In this study, we sought to develop a suite of techniques for using Neuropixels probes to record brain activity acutely during clinically indicated neurosurgery. Scaling up the size and quality of neural population recordings is a crucial step to enable novel fundamental neurophysiological and clinical investigations in humans. For example, detailing the cellular scale mechanisms underlying epilepsy[13][,][15] , understanding changes in cellular interactions induced by the presence of tumor cells[25][,][26] or advancing brain–computer interfaces would be considerably accelerated via high-density recordings. Here we demonstrate a set of methods and a new, thicker variant of the Neuropixels probe in acute experiments in human patients. We describe solutions to challenges in sterilizing probes, electrical isolation in the operating room and brain pulsation after craniotomy. We used this approach to record from populations of neurons in dorsolateral prefrontal cortex (dlPFC) and temporal lobe during deep brain stimulator (DBS) placement and open craniotomies. We subsequently characterized the electrophysiological diversity of neurons in these regions of human cortex (assigning single units into different putative cell type groupings using three separate clustering techniques). We also found that single-cell activity covaried significantly with epileptiform activity as well as anesthesia-induced burst suppression. Taken together, this new version of the Neuropixels probe and the methods to use the probe in interoperative settings lays the foundation for expanding understanding of human cortical function in both health and pathology and in developing neurorestorative technologies. 

## **Results** 

Here we report successful recordings from the cortex of temporal and frontal lobes in patients undergoing brain tissue resection to treat epilepsy ( _n_ = 1, under general anesthesia, lateral temporal lobe) or during the implantation of DBS leads to treat movement disorders ( _n_ = 2, one awake and one under general anesthesia, dlPFC) using Neuropixels probes. We also report unsuccessful recordings—and lessons learned—from six cases performed while developing these approaches (Supplementary Table 1, Extended Data Fig. 1 and Methods). Unsuccessful recordings were due 

either to electrode fracture ( _n_ = 2, with the devices and pieces fully recovered; Supplementary Table 1) or excessive noise during the recordings ( _n_ = 4). Two different types of arrays were tested. In the first two attempts, we used the original Neuropixels 1.0 probe but found it to be too fragile. Instead, we developed a variant featuring a thicker shank (Neuropixels 1.0-ST: thickness: 100 µm, width: 70 µm, length: 10 mm). This version enabled considerably easier insertions and robust use during neurosurgical cases. This probe version, combined with an improved grounding and reference electrode configuration, enabled us to observe spiking activity from populations of isolatable single neurons in three participants ( _n_ = 3; Supplementary Table 1, Extended Data Figs. 1 and 2 and Methods). 

Because the Neuropixels probe was originally designed for small animal neurophysiology, five technical developments were needed to translate this device to intraoperative use in humans. These included (1) sterilization with ethylene oxide and maintaining sterile conditions in the operating room; (2) mounting the probe to a neurosurgical robot or sterile micromanipulator; and (3) stereotactically guided insertion through a burr hole or craniotomy window. These techniques, informed by our previous experience adapting Neuropixels to NHPs[3] , are described in further detail in the Methods. A fourth, and crucial, consideration was the identification and reduction of sources of noise in our recordings in the operating room, which are considerably larger and more difficult to control than in experimental laboratory settings. We performed tests both during the neurosurgical cases as well as in the operating room without a patient to identify the external sources of noise (for example, anesthesia intravenous pumps) as well as internal sources of noise (for example, we found that, in this environment, ground and reference should be separate and not tied together as is often done in mouse studies; Methods and Extended Data Fig. 1). Fifth, as it was not possible to suppress the brain owing to patient safety considerations and shear stress on the Neuropixels probe (Methods), a semi-automated post hoc registration method was developed to allow for single units to be stably isolated and tracked over time. 

Single-unit waveforms were observed both on individual Neuropixels probe channels and across multiple channels (Figs. 1 and 2). However, we also observed considerable modulation of the voltage recording related to motion of the brain. This motion primarily results from respiratory and cardiac rhythms, which cause the surface of the brain to move relative to the probe. We observed these movement-related changes in both the LFP and AP bands (Fig. 2a–d). To confirm that the movement present in the neural recordings was due to tissue movement, we matched the neural recording itself, specifically the LFP band, to the synchronized audio of the electrocardiogram (EKG) and video of the brain (Fig. 2b). 

**Fig. 2 | A variety of waveform types and shapes recorded in human neocortex with Neuropixels probes. a** , Illustration of evidence of tissue movement relative to the electrode recordings in the LFP (shown in red-blue color scale with the range in µV shown in **c** ). This is quantified by manually tracing these ‘band shifts’ using the Blender program, followed by detection of these movements in the LFP and tracking of these movements across channels (white line, second to rightmost plot). **b** , Validation of movement being reflected in the LFP channel shifts. Left: Video of the intraoperative recording, and the pumping evident in the cerebrospinal fluid surrounding the electrode was tracked through time. Right: simultaneous traces of the video-tracked movements and the LFP-tracked movements in the same patient (Pt. 03) at two different scales. Generally, the magnitude of the movement artifact was on the order of 80–100 µm. **c** , Series of steps taken for adjusting for movement and interpolating the data. **d** , High-frequency (AP) signal before (left) and after (right) adjusting for movement effects. **e** , Example unit waveforms (each color is a separate unit; * indicates the largest waveform per unit, and this was used for further waveform measurements). On the left, original waveforms are overlaid relative to the recorded channels, with the gray bars to the left indicating the location of the units along the probe. **f** , Example autocorrelograms and ISI distributions for three different units. **g** , Approach for cross-correlating the movement-corrected neural data and the raw signals by cross-correlating the 12 channels of the sorted spikes with the raw data (left). Top: tracked single unit across 12 channels identified in the realigned data (top row) as well as the raw data (second row; after cross-correlation), with waveforms from single spike times overlaid from different epochs of time (indicated by the brackets beneath the waveforms). Cyan traces: first third of the recording; purple traces: middle third of the recording; magenta traces: last third of the recording. Bottom: Cross-correlation values (shown in color map), which were paired with the LFP-tracked movement (white lines), allowed tracking of individual units along the raw channel data (bottom, right, purple dots). **h** , We could then correlate the 12 channels with the waveforms on a per-unit and per-channel level and overlay the unit waveforms for the raw data (black lines) and over the average units sorted from the realigned data (red lines). 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**254** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

Critically, the high spatial density of Neuropixels electrodes allows for post hoc motion correction and high-quality spike sorting. Estimating the timepoint-by-timepoint brain position relative 

to the probe was best achieved using the high-density sampling of LFP (Fig. 2a–c and Extended Data Fig. 3). We determined that the optimal approach was to use semi-automated tracking (after testing 

**==> picture [435 x 629] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>LFP signal Tracked movement  Video-tracked<br>movement<br>Video<br>tracking LFP-tracked<br>movement<br>334 340 334 340<br>Time (s) Time (s) 5 s<br>c d<br>Before alignment After alignment<br>Raw<br>data<br>75 µV<br>200 ms<br>e Pt. 02 Interpolated data-sorted spikes<br>*<br>* *<br>* * *<br>1 ms 1 ms<br>f Autocorrelation, ISI,  Autocorrelation, ISI,  Autocorrelation,  ISI,<br>unit example 1 unit example 1 unit example 2 unit example 2 unit example 3 unit example 3<br>30 60 100 400 40 100<br>0 0 0 0<br>0–0.1 0 0.1 00 2 –0.1 0 0.1 0 2 –0.1 0 0.1 0 2<br>Time (s) ISI (s) Time (s) ISI (s) Time (s) ISI (s)<br>g Re- Waveforms at different time ranges of the recording h Unit example a<br>aligned 2 × 10 [7] Realigned data<br>data Raw signal<br>Raw<br>0<br>1,000<br>2,000 Unit example b<br>2D cross- 3,000<br>X correlate 4,000<br>300 800<br>Single unit spike times and cross-correlated locations<br>LFP tracked movement<br>0<br>540 560<br>Time (s)<br>Time (s)<br>Interpolated data<br>Realigned data<br>Count<br>m)<br>µ<br>Realigned data<br>Depth (<br>2D cross-correlation<br>Raw signal<br>**----- End of picture text -----**<br>


**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**255** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [435 x 562] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c<br>Clinical  Neuropixels,<br>depth  20 µm Utah array<br>contact,  contact  400 µm<br>1.2–3 mm spacing contact spacing<br>contact<br>spacing<br>Contacts<br>Cortical<br>surface<br>White matter<br>Laminar array,<br>150 µm Cortical<br>contact spacing surface<br>Utah<br>array 500 µm Neuropixels<br>d Single-channel WaveMAP clusters<br>unit classification  PCA and  k -means  classification using 6 channels<br>based on waveform  clusters classification<br>Chan. 1 Chan. 2 Chan. 3<br>duration using 6 channels<br>n  = 117<br>Chan. 1  Chan. 2 Chan. 3 1<br>n  = 34<br>PS 1 n  = 85<br>Positive 2<br>spikes (PS),  PS 2 n  = 145<br>n  = 348<br>n  = 85<br>n  = 180 3<br>PS 3<br>Regular  n  = 92<br>spiking (RS)units,  RS n  = 76 4<br>n  = 82<br>n  = 127 n  = 61<br>Fast  FS 5<br>spiking (FS)<br>n  = 15<br>units,  Triphasic n  = 103<br>n  = 115 600 µs 6<br>n  = 25<br>Broad<br>spikes Triphasic n  = 34<br>spike 7<br>667  µs<br>n  = 25<br>8<br>e<br>*<br>*<br>6 *<br>10<br>10<br>8<br>4 8<br>6<br>6<br>4<br>2 4<br>2<br>2<br>0 0<br>0<br>PS RS FS 1 2 3 4 5 6 7 8<br>Positive spikes Negative spikes<br>PS 1 PS 2 PS 3 RS FSTriphasic BroadSpikes<br>matterWhite<br>Contacts<br>m<br>µ<br>250<br>Micro-contacts: contact spacing<br>Positive spikes<br>Negative spikes<br>Mean spike rate (Hz)<br>**----- End of picture text -----**<br>


**Fig. 3 | Classifying waveforms based on spatial and temporal features. a** , Illustration of different types of state-of-the-art intracranial microelectrodes implanted in cortex, with a zoomed-out view of the clinical depth lead and the electrodes in cortex in the inset box in the lower-right corner. **b** , Photograph of the Utah array side by side with the Neuropixels array, with the yellow (Utah array) and cyan (Neuropixels) insets at the same scale. **c** , Reconstructions of human pyramidal cells and inhibitory interneurons with cells from NeuroMorpho.Org[60][–][64] relative to the Neuropixels array and the 1.5-mm Utah array. **b** , **c** , Scale bar, 500 µm. **d** , Left, average waveforms of each unit using the single-channel classifications. Middle, average three channels per unit (each column is a channel); multi-channel classification based on the principal components and _k_ -means clustering across patients. Right, average three channels per unit (each column is a channel); multi-channel classification based on the WaveMAP approach across patients. Columns are the three channels with the largest amplitudes per detected unit. **e** , For the violin plots, the mean (black horizontal line) and median (red horizontal line) firing rate including the kernel density estimation distribution represented by the shaded outlined area (vertical extent of the distribution indicates the range of the data values) for the different waveform classifications. Asterisks indicate significant differences between putative cell or waveform types, Kruskal–Wallis multiple comparisons test, _P_ < 0.001, post hoc Tukey–Kramer test for multiple comparisons (left plot: _P_ = 1.07 × 10[−][18] ; middle plot: _P_ = 2.18 × 10[−][15] ; right plot: _P_ = 3.68 × 10[−][8] ). 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**256** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

multiple methods; Methods and Extended Data Figs. 3 and 4). The tracked motion contained multiple dynamics with one peak around 1.5 Hz, which shifted with time (possibly with heart rate), a variable slow oscillation (~0.15 Hz) that dampened over time (possibly as the electrode settles into the tissue) and slow drift (~0.01–0.02 Hz) that has different timing dynamics as shown in a spectrogram (Extended Data Fig. 4). This combination of movement frequencies proved challenging for fully automated approaches that rely on a more than 1-s time scale and spikes for motion correction[27] and were not compensated for by the drift correction offered by Kilosort 3.0 (refs.[4][,][28] ) (Extended Data Fig. 3). 

After this movement alignment, we sorted waveforms into clusters using Kilosort 3.0 software[4][,][28] and extracted an average of 201 ± 151.04 clusters from the recordings. Each cluster presumably represents APs generated from a single neuron or very small number of neurons with separable temporal (waveform shape) and spatial characteristics (the pattern of waveforms across multiple recording channels). Data from the two participants undergoing DBS implants contained similar numbers of clusters (with the Neuropixels recording from the dlPFC, participant (Pt.) 01, not awake: _n_ = 262; Pt. 02, awake: _n_ = 312), whereas the third participant undergoing an anterior temporal lobectomy yielded considerable fewer (Pt. 03, not awake: _n_ = 29). The waveform clusters were then classified as either multi-unit activity (MUA) clusters (Pt. 01: _n_ = 60; Pt. 02: _n_ = 134; Pt. 03: _n_ = 10) or single units (Pt. 01: _n_ = 202; Pt. 02: _n_ = 178; Pt. 03: _n_ = 19) (Extended Data Figs. 5 and 6 and Supplementary Table 1). 

As single units could be captured both vertically and laterally on a fine spatial scale, the advantage of the contact-to-contact 20-µm distance of the Neuropixels array relative to the known sizes of human cortical neurons (approximately 20 µm at the cell body; Figs. 2b and 3a–c and Extended Data Fig. 5) allowed a sub-sampling of the extracellular single-unit AP. As such, we could reliably trace the location and identity of single cells across the recording, an approach that would be limited if we could only access a single channel at the more than 150-µm resolution of other single-neuron recording devices (Fig. 2d and 3a–c[7][,][9][,][13] ). Specifically, we found that an average of 52% of units had significant (5 s.d. above baseline voltage) deflections across multiple channels (Pt. 01: 90 units out of 202 units; Pt. 02: 103 units out of 178 units; Pt. 03: ten units out of 19 units; Fig. 2 and Supplementary Video 1). To determine if the movement correction and interpolation could influence the detection and tracking of identifiable single units through time, we performed a two-dimensional cross-correlation between the sorted waveforms and the raw AP (high-frequency band) data (Extended Data Fig. 4). The process involved cross-correlating the 12 channels of the sorted spikes from the movement-corrected data, stepwise and channel set by channel set through the raw data (Extended Data Fig. 4). We found that we could track the spatial location of individually identifiable units (not simply the largest waveforms) through time and spatially in the raw data along the electrode as well as calculate the average movement found per patient (Fig. 2g and Extended Data Fig. 4). Subsequently, we found high correlations on the per-waveform and channel level across units and participants (mean Pearson’s correlation per waveform per channel: Pt. 01: 0.64 ± 0.197, maximum: 0.99; Pt. 02: 0.65 ± 0.254, maximum: 0.99; Pt. 03: 0.50 ± 0.125, maximum: 0.60) (Fig. 2h). Overall, the correlation between the raw data and the sorted spikes increased with increasing number of spikes (Pearson’s correlation between number of spikes and correlation values: Pt. 01: ρ = 0.27, _P_ = 0.0001; Pt. 02: ρ = 0.33, _P_ < 0.0001; Pt. 03: ρ = −0.35, _P_ = 0.137) (Extended Data Fig. 4). 

Finally, we found that most units could be detected throughout the recording in the raw data (mean range of time the units are detected: Pt. 01: 480.1 ± 129.70 s; Pt. 02: 438.8 ± 94.92 s; Pt. 03: 517.9 ± 165.90 s; proportion of the recorded time the units 

were detected: Pt. 01: 0.82 ± 0.221; Pt. 02: 0.77 ± 0.166; Pt. 03: 0.71 ± 0.229) (Fig. 2g, Extended Data Fig. 4 and Supplementary Video 1). Both with the cross-correlated tracking of the single units and the LFP movement detection, we found that the movement variance was higher for the awake case over the two not-awake cases (LFP variance in movement: Pt. 1: 2.31; Pt. 2 awake case: 26.15; Pt. 3: 4.47; cross-correlated unit maps: significant differences between = patients; Kruskal–Wallis multiple comparisons test; chi-square 399.39, _P_ < 0.00001; Fig. 2i and Extended Data Fig. 4). Last, the calculated mean velocity of the movement estimated from the LFP was 76.5 ± 27.30 µm s[−][1] (Extended Data Fig. 4). 

After confirming that identifiable single units could be tracked in both the movement-corrected and raw datasets, we observed a diverse set of spike waveforms within and across participants. A neuron’s waveform changes depending on the location of the recording electrode, not as an invariant property of the neuron but as a function of both the neuron and the recording geometry[29][,][30] . As would be expected from electrically observing a neuron from multiple vantages with high-density sampling[29] , some isolated units had more than one type of waveform across the different channels. For example, there were units with positive peaks on some channels and, simultaneously, negative peaks on other channels or double peaks on one channel and single peaks on other channels (Extended Data Fig. 5). Finally, different units were highly localized to 2–3 channels while others were widely dispersed across electrodes, with waveforms of various durations and amplitudes (Figs. 1e,f, 2c,g and Extended Data Fig. 5). 

With the ability to record simultaneously from multiple closely spaced 20-µm contact-to-contact spaced electrodes, unlike with other state-of-the-art microelectrode recording devices (Fig. 3a,b), we could spatially sub-sample and confirm that the voltage generated per single cell during the putative AP was detected as differently shaped waveforms (Fig. 2e,f, Extended Data Fig. 5 and Supplementary Video 1). These phenomena were previously reported in NHPs[3][,][31] and rodents[1][,][2][,][4] , but such a high-resolution view of electrophysiological waveform diversity has not been previously available in vivo in humans, particularly because the smallest contact-to-contact spacing regularly used in human studies is 150 µm (Fig. 3a,b). 

**Cell type classification based on extracellular waveforms.** Although waveform polarity and shape could be dependent on the location of the electrode relative to the cell body[29] , there is a growing set of studies in other species with Neuropixels recordings arguing that positive deflecting waveforms represent axonal APs[3][,][32][,][33] . In addition to investigating the frequency of waveform types in this dataset, we wanted to link the current Neuropixels spatially subsampled APs to past human single-unit studies using technologies with lower contact-to-contact spatial resolution (>150-µm spacing[7][,][13] ). We used three classification techniques to independently cluster waveforms: (1) a single-channel classification based on definitions employed in human single-unit studies[13] ; (2) a multi-channel classification using principal component analysis (PCA) followed by _k_ -means clustering; and (3) a unsupervised, multi-channel classification algorithm called WaveMAP[31] (Fig. 3d and Extended Data Fig. 6). Each classification improved the separability of the classes of units, with the different classes showing similar waveform and spike rate feature separation among single-channel, PCA and WaveMAP approaches (Fig. 3d and Extended Data Fig. 7). For instance, all three approaches classified negatively deflecting regular spiking (RS) and fast spiking (FS) units separate from other waveforms, with similar classifications for positively deflecting waveforms between the PCA/ _k_ -means approach and WaveMAP. 

**Single-channel duration and sign waveform classification.** Following previous studies, in which researchers routinely classified 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**257** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

putative inhibitory and excitatory neurons based on the polarity and half-peak waveform width of the largest waveform for each unit (that is, from the one channel with the largest waveform for that unit), we used single-channel metrics (waveform half-peak width and duration (valley–peak)) to separate units into three classes: positive spikes (PS, _n_ = 348) versus negative spikes, with the latter subdivided into negative FS ( _n_ = 115) or negative RS ( _n_ = 82) single units based on the peak–trough duration of the largest waveform across channels per unit (asterisks in Fig. 2e and Methods)[34][–][36] . As positive deflecting waveforms have been hypothesized to be the results of axonal APs, we separated positive and negative spikes[2][,][31][–][33] . We also included a fourth category of MUA where the waveforms were mixed across the single-unit cluster, and the autocorrelation and inter-spike-interval (ISI) distributions were more representative of MUA, with more uniform ISI distributions versus single-unit ISI distributions (Fig. 3d). The peak–trough duration cutoff for FS versus RS units was at 300 µs, which is similar to the cutoff reported previously[34][,][37] , near a boundary in a presumed bimodal distribution of peak–trough durations for negative polarity events (purple line; Extended Data Fig. 8). 

Each putative class of neuron displayed differences in waveform features and spike rates (Fig. 3d and Extended Data Figs. 8 and 9). First, positive spike (PS) units generally had wider waveforms than RS and FS units. The half-peak width was 167.3 ± 55.4 µs for PS and 133.8 ± 70.9 µs for FS + RS, and spike duration was 494.2 ± 175.1 µs for PS and 349.6 ± 222.2 µs for FS and RS (Fig. 3d and Extended Data Fig. 8). These unit types also showed significant differences in repolarization slope and recovery slope as well as the peak–trough ratio (Extended Data Fig. 8). Among these three categories of units (PS, RS and FS), the PS unit mean firing rates were significantly higher than those of RS and FS units ( _P_ < 0.001, Wilcoxon rank-sum test; RS: 0.3 ± 0.27; FS: 0.4 ± 0.59; PS: 1.1 ± 1.35 Hz mean firing rate). FS units trended, though non-significantly, toward slightly higher firing rates than RS units ( _P_ > 0.05, Kruskal–Wallis multiple comparisons test; Fig. 3e). Spike rates were higher in the awake case overall. However, no significant difference was observed in spike rates between the FS (narrow waveform) and RS (wide waveform) units in either the anesthetized cases ( _P_ = 0.0705, Wilcoxon rank-sum test) or the awake cases ( _P_ = 0.0901, Wilcoxon rank-sum test). The peak–trough ratio was significantly lower for the FS and RS units than the PS units (PS: 4.8 ± 2.0; RS: 3.9 ± 1.7; FS: 4.1 ± 1.8; _P_ < 0.001, Kruskal–Wallis multiple comparisons test), whereas the recovery slope was higher in absolute amplitude for the RS units than the FS and PS units. The repolarization slope was larger for the PS units than the RS or FS units (Extended Data Fig. 8). These differences in waveform characteristics resemble previous studies in mice, cats and macaques[2][,][32][,][34] . However, single-channel classification explicitly ignores the spatiotemporal features of extracellular waveforms afforded by high-resolution sampling in Neuropixels recordings (Fig. 3a–c). 

**Multi-channel PCA and** _**k**_ **-means clustering unit classification.** For multi-channel waveform classification, we applied PCA and _k_ -means clustering in an unbiased clustering approach (using a larger feature vector that includes data from multiple electrode sites; Fig. 3d and Extended Data Fig. 6). This analysis identified seven classes of units using the waveforms from the first six channels of each unit (with channels reordered from largest to smallest waveform per unit; Fig. 3d). The resultant classes subdivided the single-channel classification, which resulted in varying temporal and spatial distributions as well as triphasic waveforms, with two of the classes closely resembling the RS and FS single-unit classifications from the previous analysis (Fig. 3d), again showing increased average firing rates for two of the positive spikes (PS1 and PS2) relative to FS and RS units. We also found similar trends and differences between the PS and other waveforms with increased PS 

peak–trough ratios and varying repolarization and recovery slopes per waveform classification (Extended Data Fig. 8). 

**Multi-channel classification of units using WaveMAP.** Finally, we used an automated, non-linear method for classifying extracellular waveforms, with the goal of identifying additional classes based on smaller and more nuanced features of the waveforms using uniform manifold approximation and projection (UMAP) dimensionality reduction combined with Louvain clustering[31] . Using WaveMAP[31] , we found that specific waveform types were identifiable across and within participants. After performing WaveMAP on each dataset, the same WaveMAP classifications could be found with independent classifications per participant. Negative RS- and FS-like units were present in all three patients’ data, whereas the positive large waveforms (PS) appeared in two of the three cases (Fig. 3d and Extended Data Fig. 7). We, therefore, pooled the waveforms across patients and classified waveforms from across the six channels with the largest amplitude waveforms of each unit using WaveMAP, which revealed eight total classes, which include four PS classes and four mostly negatively deflecting neuron classes, which included FS-like, RS-like, triphasic and broad classes (Fig. 3d). As with PCA and _k_ -means classification, we found little difference in the number of classes when we included either six or 12 channels with the largest amplitude waveforms in the classification. In addition, we found similar differences in spike rates for different PS classes (including two of the three PS classes having higher spike rates than the RS, FS and triphasic neurons; Fig. 3e). 

**Spatial spread of single-channel and multi-channel waveform classes.** An important feature of the Neuropixels probe is the ability to obtain high local spatial sampling, which permits tracking of individual spike propagation and has been used to argue for extracellular identification of back-propagating APs (Fig. 3a–c)[1][,][2][,][4] . Using published metrics and code[2] , we calculated the spatial spread and velocity of the waveforms among the three identified categories of waveforms (Extended Data Fig. 9). In the single-channel classification, we found that the spatial spread for the FS and RS units was significantly lower than for the PS units ( _P_ < 0.001, Kruskal– Wallis multiple comparisons test). This trend held when using multi-channel classification (PCA/ _k_ -means and WaveMAP) with some PS units with higher spatial spread than RS, FS and triphasic units (Extended Data Fig. 9). 

Finally, mapping the different waveform classes to their location along the probes showed that PS units were observed at sites throughout the shank of the probe (and throughout the cortical layers), whereas the RS and FS type units appeared to be concentrated on probe sites located more distally along the probe. This spatial distribution of these cell categories likely reflects the inhomogeneous distribution of cell types and AP propagation patterns throughout cortical lamina, although a precise mapping of PS, RS and FS waveform groups to cell classes is impossible using extracellularly recorded waveforms alone (Extended Data Fig. 9). That said, we found subtle differences among the PS groups as well as the RS, FS and triphasic spike groups with the multi-channel classifications (PCA/ _k_ -means and WaveMAP) all along the Neuropixels probe. A subset of PS units was located more superficially relative to the negative spikes and even other PS units (Extended Data Fig. 9). However, none of the waveform classes (single-channel or multi-channel) had a significant difference in the velocity of the waves above or below the peak waveform, suggesting that the APs recorded here are localized and possibly generated at the soma (Extended Data Fig. 9)[2] . 

In summary, we found that there was strong agreement in the three different unit classifications between the single-channel and multi-channel classification approaches, although the multi-channel classifications (PCA/ _k_ -means and WaveMAP) revealed more putative cell subtypes among the units, which were supported by 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**258** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

significantly different firing rates, spatial distribution, depth and waveform features. 

**Timing and interactions among single units.** In the recording, we could observe units within seconds of insertion, although there was generally a ~2-min period of time when both single-unit and MUA spike rates would slowly increase in all three participants’ recordings before leveling off at a seemingly consistent rate (Extended Data Fig. 10). Mapping the WaveMAP-classified single units and MUA classes to the electrode depth for the duration of the recordings, we found the different WaveMAP classes to be observable throughout the recording and across the Neuropixels probe (Extended Data Fig. 10). 

To determine, as a proof of concept, whether there were interactions between units through time, we performed pairwise covariance analyses between the spike times of different pairs of units and found correlations between individual units in two datasets (Pt. 01 and Pt. 02; Extended Data Fig. 10)[38][,][39] , suggestive of inter-unit circuit activity. We found that some individual units covaried with each other in time (within a 0.1-s time window), even between different classes (Extended Data Fig. 10). Across the WaveMAP classes, we found that an average of 6.9 ± 2.58% of all pairs had a significant covarying relationship (at least one binned peak in the covariance calculations 8 s.d. above the baseline covariance levels across the recording). The average absolute lag between pairs with significant covariances was 13.9 ± 2.0 ms (Pt. 01: 14.1 ± 14.2 s; Pt. 02: 15.4 ± 14.9 s; Pt. 03: 12.7 ± 13.6 ms). Of these comparisons, we found that 58% of the pairs with significant covariances showed absolute spike lags of more than 5 ms, and 46% were even longer than 10 ms (Pt. 01: >5 ms, 60%, >10 ms, 46%; Pt. 02: >5 ms, 65%, >10 ms, 52%; Pt. 03: >5 ms, 49%, >10 ms, 42%). However, a challenge in interpreting these temporal lead/lag relationships is that epileptiform activity or general anesthesia-induced burst suppression could have induced correlated class activity in two of the three participants (Extended Data Fig. 10). We anticipate that more detailed pairwise relationships between units can be identified in future studies without these confounds[40][,][41] or using additional analytical techniques accounting for the specific effects of anesthesia[42][,][43] . 

**Neuropixels recordings reveal spike field relationships.** Many questions in clinical and cognitive neuroscience have been addressed by examining the relationships between LFPs and the timing of spikes[15] , even in the short period of time (15 min) of these recordings, using single-channel lowered electrodes[18][,][44] . To that end, we next sought to determine whether the single units and multi units detected using Neuropixels could also be used to extract spike field relationships (Fig. 4). We first movement-corrected the Neuropixels LFP recordings using the same manual approach as for correcting spiking activity, which revealed local field voltage reversals along with the Neuropixels depth (Fig. 4a). 

Even without interpolating and re-aligning the LFP, we could identify interictal epileptiform discharges (IIDs) in the recording from the lateral temporal lobe before tissue resection for epilepsy (Fig. 4b). After confirming the presence of the IIDs using both automatic approaches[45] and visual confirmation by a trained epileptologist (S.S.C.), we then aligned the single-unit and multi-unit activity to the peak of the IIDs ( _n_ = 57). Single units increased their firing rate around the peak of the IIDs, even in recordings with sparse firing (Fig. 4c). To verify this change, we jittered (centered on a normal distribution) the timing of the IID peak relative to the unit times and found that the increase in spike events was significant (Fig. 4d). Furthermore, we compared the average binned spike counts (across trials per time step) to a baseline −2 s to −0.5 s before the IID and found a significant increase in spikes in the half second after the IID peak ( _P_ < 0.005, Wilcoxon rank-sum test). As reported previously, some units increased at the IID onset or fired only during the IID peak, whereas other units decreased firing around or after an IID, although we did not find a correspondence between unit class and spike rate modulation[46] . 

In two cases, the participants were under general anesthesia, producing a typical burst suppression pattern in the average LFP[47] (Fig. 4e,f and Supplementary Table 1). Single-unit firing generally increased during the bursts and decreased during the suppression periods in the LFP. The firing rate from −1.5 s to −0.5 s before the onset of a detected burst relative to the −0.5 s to +1 s after the onset of the detected burst was significantly increased. The unit firing during the bursts was significantly higher than the burst-triggered unit firing calculated in a time-shuffled dataset, where the burst time onset was shuffled in time relative to the spike data (1,000 shuffled tests; Fig. 4g). This population change could also be observed at the level of individual units, where the firing rates of single units would increase before, during and after (depending on the unit) the burst onset time in both patients (Fig. 4h). Interestingly, between 25% and 55% of the individual units within different WaveMAP unit classifications showed significant spike rate modulation relative to the burst onset, whereas the other units did not vary significantly with the burst suppression. In addition, some units increased firing preceding the burst, whereas others increased firing later during the burst, indicating separable response profiles (Fig. 4h). Together, these recordings appeared to provide richly detailed information about the spike field relationship of neurons and their dynamics during physiologically relevant states. 

## **Discussion** 

Here we show that Neuropixels probes can be adapted for use in acute recordings of neuronal activity in the human cortex in an operating room environment. We found that, within minutes after inserting the Neuropixels probe into cortical tissue, we could observe up to 200 clear and stable units. Taking advantage of the spatiotemporal 

**Fig. 4 | Relationship of units to the LFP events and epileptiform discharges. a** , Example LFP averaged across the electrode (top) and along the depth of the Neuropixels probe after interpolating the LFP using manual registration. **b** , IID example (gray line) along with single-unit activity (colored dots represent spike times for different units) through time in Pt. 03 and binned spike times (below). **c** , Top, individual (black traces, _n_ = 57) and average IIDs (red line). Bottom, binned spike rates of individual units along the Neuropixels depth ( _y_ axis), with the brighter pixels indicating increased activity aligned to the peak of the IIDs. **d** , Individual unit example spike timing relative to the peak of the IIDs. **e** , LFP burst suppression in a participant under general anesthesia, as shown by the gray line (LFP) along with the detected single-unit activity (raster plot in the middle figure; each color represents a different unit) and binned into 50-ms windows (bottom). Red bars on top of the figure indicate automated burst detection algorithm[65] . **f** i, **f** ii, Detected burst onsets relative to binned single-unit activity along the Neuropixels probe in two different patients (Pt. 01 (i) and Pt. 03 (ii)). **g** , Binned spike rates relative to the burst onset (red) compared to time points where the burst onset was jittered randomly around a normal distribution of time ranges (black line). Green dots indicate spike rates (mean across units) that are significantly different compared to the −1.5 s to −0.5 s before burst onset. **h** i, Left, units separated into six classes for one patient (Pt. 01), color-coded per class. Middle, example unit activity relative to the 1 s before and 2 s after the burst. Some units increase spiking before, during or after the burst. Right, bar graph indicating the percentage of units per class with significant changes in firing rate relative to the burst onset. **h** ii, Units separated into two classes for one patient (upper right, Pt. 03), color-coded per class, and example unit activity with changes in spike rates relative to the 1 s before the burst onset, with some units increasing spiking before, during or after the burst. Below right, bar graph indicating the percentage of units per class with significant changes in spike rate relative to the burst onset. 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**259** 

**NAtuRE NEuRoScIENcE** 

## Technical RepoRT 

scales afforded by these probes, we could separate units based on waveform shapes (using duration and polarity), and we could also classify the waveforms using unbiased techniques via PCA with _k_ -means clustering and, separately, using a novel non-linear approach, WaveMAP[31] . Similar waveform classes were found across participants, indicating consistencies across individuals. 

This waveform diversity likely reflects both differences in cell type and in proximity of the contact to specific structures (for example, near soma versus axons)[31] . Historically, single-channel extracellular recordings have led to the primary categorization of neurons into inhibitory versus excitatory/pyramidal neuron classes with bimodal distributions of firing rate and spike width as primary 

**==> picture [510 x 602] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b c d<br>Average LFP  IID Detected IIDs,  n  = 57 Actual Jittered IID times<br>across channels 0.04<br>100<br>0.4<br>0<br>–0.4 100 µV 0<br>Interpolated LFP 2 –100<br>1,200<br>0<br>1,400 –5 Baseline0 5<br>1,600 0 Binned spike times 0.15 Unit example 1<br>1,800 0.05<br>2,000 0 1,000<br>2,2002,400 5 2,000 0.150 Unit example 2<br>2,600 3,000<br>2,800 –2 0 0<br>3.2 3.6 281.4 282 –3 0 3 0–5 0 5<br>Time (s) Time (s) Time relative to IID peak (s)<br>Time relative to IID peak (s)<br>e Relationship between units  f i Detected bursts,  n  = 207 ii Detected bursts,  n  = 130<br>and burst suppression<br>Pt. 01 Pt. 03<br>100<br>Burst<br>detection<br>0 Pt. 01 0<br>1,000 200 µV<br>LFP –100<br>2,000<br>Binned spike times  Binned spike times  0.05<br>0<br>3,000<br>1,000<br>2,000<br>15<br>10<br>3,000<br>5<br>0<br>456 457 458 459 460 461 –1 0 1 2 –1 0 1 2 0<br>Time (s) Time relative to detected burst onset (s)<br>g h i Example burst  ii Example burst<br>suppression responses Pt. 01 suppression responses Pt. 03<br>0.1 Unit 154 0.04 Unit 367<br>Actual burst Jittered burst<br>onset times onset times Classes  Classes<br>0 0<br>0.035 0.06 Unit 583 0.04 Unit 401 2<br>6 0 0<br>0.3 Unit 226 0.06 Unit 469 1<br>5<br>0 Unit 223 0 Unit 468<br>0.1 0.06<br>0 Pt. 01 4 0 Unit 447 60 0 Unit 342 60<br>0.0016 0.06 0.04<br>3<br>0 0<br>0.1 Unit 571 0.04 Unit 111<br>2<br>0.10 Unit 551 0 Unit 37<br>Pt. 03 1 0.06<br>0–1 0 1 2 0–1 0 1 2 0 1 2 3 4 5 6 0–1 0 1 2 0 1 2<br>Baseline Time relative to detected burst onset (s)<br>LFP  Vµ Mean<br>Normalized binned spikes 100-ms bins<br>m)<br>µ<br>Normalized LFP<br>Channel depth (µm)<br>100-ms bins Binned spikes<br>Cluster depth (<br>Binned spikes 50-ms windows Binned spikes 100-ms bins<br>V<br>µ<br>m)<br>µ<br>Cluster depth (<br>m)<br>µ<br>Cluster depth (<br>Binned spikes, 100-ms bins<br>50-ms bins<br>Binned spikes,<br>Mean binned spikes, 50-ms bins % responsive units per class % responsive units per class<br>**----- End of picture text -----**<br>


**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**260** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

categorization features[34][,][37][,][48][,][49] . Contrary to these expectations, we did not find strong differences in firing rate or spatial spread for the RS versus FS units. One possible explanation is that the higher density of Neuropixels allows more sensitive neuron detection, which leads to recording a wider range of neurons with less bias toward large-waveform APs. Nonetheless, we were able to segregate multiple neuron classes and also found a differential laminar distribution of distinct unit types. These results suggest that the ultra-high-density recording approach enabled by Neuropixels might enable an association of electrophysiologically identified units with specific neuronal subtypes[50][,][51] . Future work in both animal models and humans will be necessary to correlate functional differences in waveform morphology with essential cellular characteristics. 

In addition, we were able to find evidence of pairwise covariance between units. This suggests that the high spatial sampling of the Neuropixels probe, especially if coupled with current source density analysis of the LFP[52] and investigations of possible back-propagating APs[2] , could be used to provide detailed microcircuit maps of human cortex. This could be further augmented by precision ex vivo physiology[53] and super-high-resolution anatomy[54] . 

We also observed substantive relationships between LFP and unit activity during two clinically relevant events. During burst suppression, we found units with increased firing before the burst, with others firing during and after. Similarly, we found certain units firing at or after an IID. In both cases, the Neuropixels probe captured clinically relevant activity in the LFP while recording from a large number of single cells even acutely in the operating room. This demonstrates, in preliminary fashion, the power of the Neuropixels to examine mechanisms of anesthesia, pathology and more. 

An important component of human Neuropixels recordings, and a particular consideration when examining activity across cortical layers, is that the small form factor allows the probe to be inserted at a wide range of angles and locations relative to gyri and sulci, even with clinical constraints on approach trajectories. In most cases, we could approach the tissue only at a limited set of angles (for example, limited by the burr hole) or penetrate a curved surface (with gyri more complex in humans), such that we might not be as perpendicular to the cortical layers as in NHP or mouse studies[1][,][3] , although localization could be improved to identify insertion angles. 

For research with intraoperative time constraints, there is a high priority on being able to achieve high-fidelity, stable recordings quickly. Previous experiences suggest that this might be hampered by cortical ‘stunning’, which results in few units being recorded for minutes or even longer after electrode insertion[24] . With the Neuropixels probe, however, we were able to record large numbers of units within minutes of insertion. In two cases, we recorded more than 200 single units in a period of 5–10 min, whereas, in the third case, we recorded 29 units in a similar timespan (10 min). The possible difference in the third participant was that the electrode was placed in the lateral temporal lobe to be resected for epilepsy, and the patient was deeply anesthetized (indicated by the high level of suppression during the burst suppression waves). 

Although these human Neuropixels recordings are promising, it is crucial to recognize that there are inherent limitations of this recording system for human neuroscience. In the current configuration, we can use only a single, essentially linear electrode array. Unlike in rodent and NHP experiments, widespread sampling is not yet available; only a single cortical column can be accessed, and there is concern that this will not allow us to identify the underlying neural circuits of cognition or pathophysiology. However, considerable work using laminar electrodes[55] (Fig. 3a) and Utah arrays[22][,][23] , as well as single lowered electrodes as done during DBS surgeries[18][,][44] , have shown that we can parse and decode complex cognitive processes and motor control even from a small area of cortex. In addition, recent work using higher-resolution planar electrodes has revealed details previously inaccessible with current clinical technologies, 

including microscale spatiotemporal dynamics of epileptiform activity[11][,][56] and propagating wave dynamics across the hippocampus[12] . Combining such thin film electrodes with Neuropixels arrays could open up an entire field of human neuroscience discovery, linking inter-cortical columnar dynamics as well as inter-laminar interactions. 

Furthermore, in some situations, data are obtained under anesthesia. Although this does allow for focused study of anesthetic agent physiology, it also has an effect on the observed physiology, particularly as the spiking activity of individual neurons can stretch and shift due to anesthesia, as shown in rodent Neuropixels studies[42] . As expected, we encountered substantial challenges with the electrically noisy environment of the operating room. This required flexibility in the arrangement of the ground and reference electrodes for the recordings. 

Another major challenge is effect of brain movement on the recordings. Here, we were able to perform a post hoc manual analysis to mitigate this artifact. After correction, motion was reduced to smaller than the average size of a pyramidal neuron body—that is, 20–40 µm. Although this was sufficient to allow for accurate spike sorting for the units reported in this analysis, it is likely that isolatable units with smaller signals were rejected due to the challenge of clustering in the face of movement. We note that extracellular APs can vary considerably across this scale; one study[57] found that cardiac-related electrode motion of just 3–5 μm changed peak amplitude by ~20%. We also found that we could not rely on alignment approaches that used only spike rates, because the movement artifact was considerably faster than the 1–2 s needed for published stabilization approaches[4][,][27] . This is because the problem is not one of drift (that is, slow displacement of the electrode) but of blood-flow-related pulsation artifact. Our manual approach provided a reasonable fix but can certainly be improved. To this end, we have provided open-source de-identified data, which we hope will allow groups to develop and update automated alignment algorithms to work well with these new types of human electrophysiology data. Future work to automatically adjust for movement artifacts would ideally use the voltage fluctuations in the LFP, or a combination of LFP and spike rates, to align the channels and adjust for the movement. Alternative electrode configurations, such as the linear column configuration used in the Neuropixels 2.0 probe, specifically facilitate automated post hoc motion correction[4] . 

Other approaches could involve minimizing tissue motion itself through mechanically stabilizing the cortex around the probe, although clinical issues, such as damage to the surface, would need to be taken into account. Another approach would be to allow the recording electrodes to move with the brain—for example, as developed by Neuralink[58] —or with a flexible link isolating the probe from any positioning equipment or cables. We think that further development of motion stabilization techniques, in a manner that maximizes patient safety, is a top priority and will result in substantially more recorded neurons, each sampled and isolated more consistently. 

An additional challenge for this technology in intraoperative studies is the necessary time constraints on the recordings. The fact that we obtained single-unit-resolution recordings almost immediately upon insertion of the Neuropixels is encouraging, because it indicates that useful information can be obtained in a short period of time, but, for patient safety, it is inappropriate to extend their time in the operating room markedly. Our current study limited extra time conservatively to ~15 min. The brevity of these recordings might be a factor in the waveform shapes that we observed; for example, cell types that fire infrequently or only in certain contexts would be less likely to be observed, and studies in other species indicate that optimal recording stability is achieved at considerably longer recordings (45 min)[3] . Comparable studies in NHPs or other models in which single units from the first minutes after insertion 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**261** 

**NAtuRE NEuRoScIENcE** 

## Technical RepoRT 

would help better contextualize human Neuropixels recordings. In addition, the recording time in the operating room can be extended in different contexts. For example, extensive language mapping during an awake tumor resection might allow for a longer recording. 

Indeed, the power of these acute tests in the operating room using Neuropixels probes will be realized with experiments in which awake patients engage with a task during the recording period. We will also be able to approach fundamental questions surrounding neural dynamics, including the independence of single neurons relative to populations[40] or relative to broad LFP activity, such as traveling waves[41] , in the human brain. Perhaps most exciting is the potential for Neuropixels (or future variants) to accelerate clinical electrophysiology via substantially increased channel counts relative to single-channel or low-channel count probes. For example, these probes allow for a detailed exploration of neuronal activity underlying epileptiform activity, the effects of anesthetic agents and the pathophysiology of brain tumors. Understanding of these and other clinically relevant conditions would benefit from high-resolution, microscale, single-neuron information[15][,][16][,][25] . 

In summary, the Neuropixels approach suggests a pathway forward for increasingly sophisticated and detailed explorations of the cellular-scale code underlying higher-order cognitive function in multiple areas of the human brain as well as for generating a deeper understanding of the dynamics of clinically relevant neural activity. It is also a step toward developing high-channel-count chronic neural interfaces for human use, which might accelerate and expand the therapeutic possibilities of brain–computer interfaces[59] . 

## **online content** 

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/ s41593-021-00997-0. 

Received: 21 June 2021; Accepted: 7 December 2021; Published online: 31 January 2022 

## **References** 

1. Jun, J. J. et al. Fully integrated silicon probes for high-density recording of neural activity. _Nature_ **551** , 232–236 (2017). 

2. Jia, X. et al. High-density extracellular probes reveal dendritic backpropagation and facilitate neuron classification. _J. Neurophysiol._ **121** , 1831–1847 (2019). 

3. Trautmann, E. M. et al. Accurate estimation of neural population dynamics without spike sorting. _Neuron_ **103** , 292–308.e4 (2019). 

4. Steinmetz, N. A. et al. Neuropixels 2.0: a miniaturized high-density probe for stable, long-term brain recordings. _Science_ **372** , eabf4588 (2021). 

5. Ward, A. A. & Thomas, L. B. The electrical activity of single units in the cerebral cortex of man. _Electroencephalogr. Clin. Neurophysiol._ **7** , 135–136 (1955). 

6. Verzeano, M., Crandall, P. H. & Dymond, A. Neuronal activity of the amygdala in patients with psychomotor epilepsy. _Neuropsychologia_ **9** , 331–344 (1971). 

7. Ulbert, I., Halgren, E., Heit, G. & Karmos, G. Multiple microelectrode-recording system for human intracortical applications. _J. Neurosci. Methods_ **106** , 69–79 (2001). 

8. Worrell, G. A. et al. High-frequency oscillations in human temporal lobe: simultaneous microwire and clinical macroelectrode recordings. _Brain_ **131** , 928–937 (2008). 

9. Nordhausen, C. T., Rousche, P. J. & Normann, R. A. Optimizing recording capabilities of the Utah Intracortical Electrode Array. _Brain Res._ **637** , 27–36 (1994). 

10. Khodagholy, D. et al. NeuroGrid: recording action potentials from the surface of the brain. _Nat. Neurosci._ **18** , 310–315 (2015). 

11. Paulk, A. C. et al. Microscale physiological events on the human cortical surface. _Cereb. Cortex_ **8** , 3678–3700 (2021). 

12. Kleen, J. K. et al. Bidirectional propagation of low frequency oscillations over the human hippocampal surface. _Nat. Commun._ **12** , 2764 (2021). 

13. Truccolo, W. et al. Single-neuron dynamics in human focal epilepsy. _Nat. Neurosci._ **14** , 635–641 (2011). 

14. Mukamel, R. & Fried, I. Human intracranial recordings and cognitive neuroscience. _Annu. Rev. Psychol._ **63** , 511–537 (2012). 

15. Cash, S. S. & Hochberg, L. R. The emergence of single neurons in clinical neurology. _Neuron_ **86** , 79–91 (2015). 

16. Chari, A., Thornton, R. C., Tisdall, M. M. & Scott, R. C. Microelectrode recordings in human epilepsy: a case for clinical translation. _Brain Commun._ **2** , fcaa082 (2020). 

17. Amirnovin, R., Williams, Z. M., Cosgrove, G. R. & Eskandar, E. N. Experience with microelectrode guided subthalamic nucleus deep brain stimulation. _Neurosurgery_ **58** , ONS96-102 (2006). 

18. Jamali, M. et al. Dorsolateral prefrontal neurons mediate subjective decisions and their variation in humans. _Nat. Neurosci._ **22** , 1010–1020 (2019). 

19. Hochberg, L. R. et al. Neuronal ensemble control of prosthetic devices by a human with tetraplegia. _Nature_ **442** , 164–171 (2006). 

20. Hochberg, L. R. et al. Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. _Nature_ **485** , 372–375 (2012). 

21. Stavisky, S. D. et al. Neural ensemble dynamics in dorsal motor cortex during speech in people with paralysis. _eLife_ **8** , e46015 (2019). 

22. Stavisky, S. D. et al. Speech-related dorsal motor cortex activity does not interfere with iBCI cursor control. _J. Neural Eng._ **17** , 016049 (2020). 

23. Willett, F. R., Avansino, D. T., Hochberg, L. R., Henderson, J. M. & Shenoy, K. V. High-performance brain-to-text communication via handwriting. _Nature_ **593** , 249–254 (2021). 

24. Flesher, S. N. et al. Intracortical microstimulation of human somatosensory cortex. _Sci. Transl. Med_ . **8** , 361ra141 (2016). 

25. Venkataramani, V. et al. Glutamatergic synaptic input to glioma cells drives brain tumour progression. _Nature_ **573** , 532–538 (2019). 

26. Venkatesh, S. et al. Electrical and synaptic integration of glioma into neural circuits. _Nature_ **573** , 539–545 (2019). 

27. Varol, E. et al. Decentralized motion inference and registration of neuropixel data. In: 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 1085–1089 https://doi.org/10.1109/ ICASSP39728.2021.9414145 (2021). 

28. Pachitariu, M., Steinmetz, N., Kadir, S., Carandini, M. & Harris, K. Fast and accurate spike sorting of high-channel count probes with KiloSort. _Adv. Neural Inf. Process. Syst._ **2016** , 1–9 (2016). 

29. Buzsáki, G., Anastassiou, C. A. & Koch, C. The origin of extracellular fields and currents—EEG, ECoG, LFP and spikes. _Nat. Rev. Neurosci._ **13** , 407–420 (2012). 

30. Gold, C., Henze, D. A. & Koch, C. On the origin of the extracellular action potential waveform: a modeling study. _J. Neurophysiol._ **95** , 3113–3128 (2006). 

31. Lee, E. K. et al. Non-linear dimensionality reduction on extracellular waveforms reveals physiological, functional, and laminar diversity in premotor cortex. _eLife_ **10** , e67490 (2021). 

32. Sun, S. H. et al. Analysis of extracellular spike waveforms and associated receptive fields of neurons in cat primary visual cortex. _J. Physiol._ **8** , 2211–2238 (2021). 

33. Zhu, S., Xia, R., Chen, X. & Moore, T. Heterogeneity of neuronal populations within columns of primate V1 revealed by high-density recordings. Preprint at https://www.biorxiv.org/content/10.1101/2020.12.22.424048v1. abstract (2020). 

34. Mitchell, J. F., Sundberg, K. A. & Reynolds, J. H. Differential attention-dependent response modulation across cell classes in macaque visual area V4. _Neuron_ **55** , 131–141 (2007). 

35. McCormick, D. A., Connors, B. W., Lighthall, J. W. & Prince, D. A. Comparative electrophysiology of pyramidal and sparsely spiny stellate neurons of the neocortex. _J. Neurophysiol._ **54** , 782–806 (1985). 

36. Bartho, P. et al. Characterization of neocortical principal cells and interneurons by network interactions and extracellular features. _J. Neurophysiol._ **92** , 600–608 (2004). 

37. Kaufman, M. T. et al. Roles of monkey premotor neuron classes in movement preparation and execution. _J. Neurophysiol._ **104** , 799–810 (2010). 

38. Swadlow, H. A. Fast-spike interneurons and feedforward inhibition in awake sensory neocortex. _Cereb. Cortex_ **13** , 25–32 (2003). 

39. Swadlow, H. A. Efferent neurons and suspected interneurons in motor cortex of the awake rabbit: axonal properties, sensory receptive fields, and subthreshold synaptic inputs. _J. Neurophysiol._ **71** , 437–453 (2017). 

40. Okun, M. et al. Diverse coupling of neurons to populations in sensory cortex. _Nature_ **521** , 511–515 (2015). 

41. Sakata, S. & Harris, K. D. Laminar structure of spontaneous and sensory-evoked population activity in auditory cortex. _Neuron_ **64** , 404–418 (2009). 

42. Dearnley, B., Dervinis, M., Shaw, M. & Okun, M. Stretching and squeezing of neuronal log firing rate distribution by psychedelic and intrinsic brain state transitions. Preprint at https://www.researchgate.net/publication/354091542_ Stretching_and_squeezing_of_neuronal_log_firing_rate_distribution_by_ psychedelic_and_intrinsic_brain_state_transitions (2021). 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**262** 

## **NAtuRE NEuRoScIENcE** 

43. Ching, S., Purdon, P. L., Vijayan, S., Kopell, N. J. & Brown, E. N. A neurophysiological–metabolic model for burst suppression. _Proc. Natl Acad. Sci. USA_ **109** , 3095–3100 (2012). 

44. Sheth, S. A. et al. Human dorsal anterior cingulate cortex neurons mediate ongoing behavioural adaptation. _Nature_ **488** , 218–221 (2012). 

45. Janca, R. et al. Detection of interictal epileptiform discharges using signal envelope distribution modelling: application to epileptic and non-epileptic intracranial recordings. _Brain Topogr._ **28** , 172–183 (2015). 

46. Keller, C. J. et al. Heterogeneous neuronal firing patterns during interictal epileptiform discharges in the human cortex. _Brain_ **133** , 1668–1681 (2010). 

47. Lewis, L. D. et al. Local cortical dynamics of burst suppression in the anaesthetized brain. _Brain_ **136** , 2727–2737 (2013). 

48. Kaufman, M. T., Churchland, M. M. & Shenoy, K. V. The roles of monkey M1 neuron classes in movement preparation and execution. _J. Neurophysiol._ **110** , 817–825 (2013). 

49. Peyrache, A. et al. Spatiotemporal dynamics of neocortical excitation and inhibition during human sleep. _Proc. Natl Acad. Sci. USA_ **109** , 1731–1736 (2012). 

50. Hodge, R. D. et al. Transcriptomic evidence that von Economo neurons are regionally specialized extratelencephalic-projecting excitatory neurons. _Nat. Commun._ **11** , 1172 (2020). 

51. Boldog, E. et al. Transcriptomic and morphophysiological evidence for a specialized human cortical GABAergic cell type. _Nat. Neurosci._ **21** , 1185–1195 (2018). 

52. Halgren, M. et al. The generation and propagation of the human alpha rhythm. _Proc. Natl Acad. Sci. USA_ **116** , 23772–23782 (2019). 

53. Beaulieu-Laroche, L. et al. Enhanced dendritic compartmentalization in human cortical neurons. _Cell_ **175** , 643–651 (2018). 

54. Shapson-Coe, A. et al. A connectomic study of a petascale fragment of human cerebral cortex. Preprint at https://www.biorxiv.org/content/10.1101/2 021.05.29.446289v1 (2021). 

## Technical RepoRT 

55. Halgren, E. et al. Processing stages underlying word recognition in the anteroventral temporal lobe. _Neuroimage_ **30** , 1401–1413 (2006). 

56. Yang, J. C. et al. Microscale dynamics of electrophysiological markers of epilepsy. _Clin. Neurophysiol._ **132** , 2916–2931 (2021). 

57. Mosher, C. P. et al. Cellular classes in the human brain revealed in vivo by heartbeat-related modulation of the extracellular action potential waveform. _Cell Rep._ **30** , 3536–3551 (2020). 

58. Musk, E. & Neuralink. An integrated brain–machine interface platform with thousands of channels. Preprint at https://www.biorxiv.org/ content/10.1101/703801v4 (2019). 

59. Dutta, B. et al. The Neuropixels probe: a CMOS based integrated microsystems platform for neuroscience and brain–computer interfaces. 2019 IEEE International Electron Devices Meeting. 10.1.1–10.1.4 https://doi. org/10.1109/IEDM19573.2019.8993611 (2019). 

60. Koch, C. & Jones, A. Big science, team science, and open science for neuroscience. _Neuron_ **92** , 612–616 (2016). 

61. Ascoli, G. A. Mobilizing the base of neuroscience data: the case of neuronal morphologies. _Nat. Rev. Neurosci._ **7** , 318–324 (2006). 

62. Ascoli, G. A., Donohue, D. E. & Halavi, M. NeuroMorpho.Org: a central resource for neuronal morphologies. _J. Neurosci._ **27** , 9247–9251 (2007). 

63. Tóth, K. et al. Hyperexcitability of the network contributes to synchronization processes in the human epileptic neocortex. _J. Physiol._ **596** , 317–342 (2018). 

64. Varga, C., Tamas, G., Barzo, P., Olah, S. & Somogyi, P. Molecular and electrophysiological characterization of GABAergic interneurons expressing the transcription factor COUP-TFII in the adult human temporal cortex. _Cereb. Cortex_ **25** , 4430–4449 (2015). 

65. Westover, M. B. et al. Real-time segmentation of burst suppression patterns in critical care EEG monitoring. _J. Neurosci. Methods_ **219** , 131–141 (2013). 

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

© The Author(s), under exclusive licence to Springer Nature America, Inc. 2022 

**NATuRE NEuRoSCiENCE** | VOL 25 | FEBRUARY 2022 | 252–263 | www.nature.com/natureneuroscience 

**263** 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

## **Methods** 

**Patients and clinical/research electrode placement.** All patients voluntarily participated after informed consent according to guidelines as monitored by the Massachusetts General Brigham (previously Partners) institutional review board at Massachusetts General Hospital (MGH). Participants were informed that participation in the experiment would not alter their clinical treatment in any way and that they could withdraw at any time without jeopardizing their clinical care. Participants were not compensated monetarily for participating. Recordings in the operating room were acquired with nine participants (mean, 59 years old; range, 34–75 years; seven females; Supplementary Table 1) who were already scheduled for a craniotomy for concurrent clinical intraoperative neurophysiological monitoring or testing for mapping motor, language and sensory regions and removal of tissue as a result of tumor or epilepsy or who were already scheduled to undergo intraoperative neurophysiology as part of their planned DBS placement[11][,][17][,][18][,][56][,][66] . Before inserting the Neuropixels probe, a small superficial incision in the pia was done using an arachnoid surgical knife. The Neuropixels probe was inserted through this incision. Recordings were referenced to sterile ground and recording reference needle electrodes (Medtronic) placed in nearby muscle tissue (often scalp) as deemed safe by the neurosurgical team though a series of tests. Ground and reference tests were performed to identify the ideal combinations of ground and reference options, which are listed below (Supplementary Table 1). 

After the surgery, preoperative T1-weighted magnetic resonance imaging (MRI) was used to generate a three-dimensional (3D) surface brain map using FreeSurfer scripts[67][–][69] (http://surfer.nmr.mgh.harvard.edu). Images obtained during surgery, locations as indicated using the proprietary software Brainlab and photographs captured during surgery were aligned to the 3D reconstructions using Blender (version 2.92) software (https://www.blender.org/) and the Multi-Modal Neuroimaging Analysis and Visualization Tool (MMVT) (https://github.com/ pelednoam/mmvt)[69][–][71] (Extended Data Fig. 2). For the two DBS cases, there are physical limits imposed by the 3D shape and location of the burr hole as well as the size of the Neuropixels probe and the headstage. As such, we took postoperative computed tomography after the DBS leads were implanted (after the surgery) and overlaid it with the preoperative MRI using Mango (http://ric.uthscsa. edu/mango/)[72][–][74] . We then used these coordinates and sizes to reconstruct the to-scale burr hole and DBS lead trajectories and mapped them to the participants’ brains reconstructed using MMVT and FreeSurfer[67][–][70][,][75] , and we then placed the Neuropixels probe in Blender to the best approximation based on all this information. For the open craniotomy case, the reconstruction involved projecting the surgical image onto the patient’s reconstructed brain using Blender and then placing a 3D model of the Neuropixels probe on that location similar to other co-registration approaches[11][,][56][,][69][,][70][,][76] (Extended Data Fig. 2). Angles were calculated from photographs taken during surgery as well as trajectories limited by the location and angle of the burr hole for DBS surgery. 

Separately, we compared the relative sizes of the Neuropixels probe contacts relative to the reconstructed pyramidal neurons and inhibitory interneurons from NeuroMorpho.Org[60][–][62] . The process involved importing the .swc files from NeuroMorpho.Org into MATLAB (Mathworks), converting the data into a surface and then exporting the .stl files, which we then imported into Blender. Neural reconstructions were from NeuroMorpho.Org IDs NMO_86955, NMO_86997, NMO_109433, NMO_61420 and NMO_61421. After manual adjustments, the reconstructed neurons were then placed next to the to-scale 3D-reconstructed electrodes in Blender (Fig. 3a,c). 

**Neuropixels recordings, data collection and analysis.** Neuropixels probes (NP version 1.0-S, IMEC) sterilized with ethylene oxide (Bioseal) were connected to a 3B2 IMEC headstage wrapped in a sterile plastic bag and sealed using Tegaderm (3M) to keep the field sterile. Neuropixels probes (NP version 1.0-S, IMEC) include an electrode shank (width: 70 µm, length: 10 mm, thickness: 100 µm) of 960 total sites laid out in a checkerboard pattern with contacts at ~18-µm site-to-site distances (16 µm (column), 20 µm (row)[1][,][59] ). Handling of the electrodes and the headstage from outside of the sterile bag was all performed in sterile conditions in the operating room. The headstage was connected via a multiplexed cable to a PXIe acquisition module card (IMEC), installed into a PXIe chassis (PXIe-1071 chassis, National Instruments). For the Neuropixels 1.0 probes as used in this study, the linear dynamic range of the Neuropixels amplifier is 10 mVpp. This range is digitized using a 10-bit analog-to-digital conversion[77] . All Neuropixels recordings were performed using SpikeGLX release v20201103-phase30 (http://billkarsh. github.io/SpikeGLX/) on a computer connected to the PXIe acquisition module recording the AP band (band-pass filtered from 0.3 kHz to 10 kHz) sampled at 30 kHz and an LFP band (band-pass filtered from 0.5 Hz to 500 Hz) sampled at 2.5 kHz[1][–][3] . Because these Neuropixels probes enable 384 recording channels, which can then be used to address 960 electrodes across the probe shank, we tested different electrode maps, which allowed us to record different portions of the probe. One map allowed for recording the lower portion of the probe (the most distal channels). A second map allowed for recording two rows along the entire length of the electrode. This map was used to identify the depth of the electrode in the cortex, and we switched to the distal tip map (short map) for the main recording. A final map allowed for recording in a series of tetrode 

locations, skipping rows to distribute recordings along the entire length of the probe. 

As the Neuropixels probe is stably rigid with regard to the channels relative to one another, we could estimate depth of the sites in the tissue along the electrode using the LFP signal. When some channels are outside the tissue, we found that the LFP signal was relatively noisy and did not show differences between channels when outside of tissue. This electrophysiological marker, however, provided an upper boundary limit of how deep the electrode was in the tissue relative to the measurements on the electrode itself, resulting in a depth relative to this upper boundary. However, we did not identify the depth as cortical depth as the Neuropixels probe could be inserted at different angles relative to the sulci and gyri (Extended Data Fig. 2). 

Synchronization was performed through two different approaches. TTL triggers via a parallel port, produced during a task via MATLAB or with custom code from a separate computer, were sent to both the National Instruments and IMEC recording systems. In addition, we used the TTL output to send the synchronization trigger via the SMA input to the IMEC PXIe acquisition module card to allow for added synchronizing triggers, which were also recorded on an additional breakout analog and digital input/output board (BNC-2110, National Instruments) connected via a PXIe board (PXIe-6341 module, National Instruments). The TTL triggers were produced either during a task via MATLAB or with custom code on the task computer. 

Data collection and analysis were not performed blinded to the conditions of the experiments. 

**Recording challenges and lessons learned.** Five main challenges were faced when performing these recordings: (1) sterilization and maintaining a sterile field and conditions; (2) electrode fracture and disconnects; (3) decreasing noise in the recordings through referencing; (4) external sources of noise; and (5) mechanical stabilization (Fig. 1 and Extended Data Fig. 1). 

_Sterilization and maintaining a sterile field._ To ensure that we could use the Neuropixels probes in the operating room, we worked with Bioseal and sent them a sample of 25 Neuropixels probes. Bioseal took the samples through a validation process to determine that ethylene oxide could be used to sterilize the Neuropixels probes. We also tested whether working Neuropixels probes were operational before and after sterilization. An important part of the process was identifying safe sterile packaging for sterilization and transport. We found that we could place the probes sideways inside a slightly modified ethylene oxide safe sterile container (SteriBest Trays, sterilization instrument tray, instrument tray sizes (inches): base, lid, mat: 6 × 2.5 × .75, item A-CP614, Duraline BioSystems; Fig. 1a, Extended Data Fig. 1g and Supplementary Table 1). When we received the boxes, we clipped protruding silicone nubs in an area of 3 cm× 3 cm on one side of the box as well as a few silicone nubs on the other end of the box. We found that we could package and safely ship and handle the Neuropixels probe cross-country by weaving the Neuropixels ribbon cable around the vertical silicone nubs in the sterilization containers, with the Neuropixels probe and headstage perpendicular to the base of the box. We performed several tests to show that the probe consistently survived this shipment approach, including before and after sterilization. Before shipping for sterilization, we soldered on a 10-cm-long male touchproof cable (the white cable in Fig. 1a,b,d) to the reference side of the Neuropixels probe. In addition, we labeled the lid of the box to track individual probes. The validation of 25 probes performed by Bioseal was done with the Neuropixels probes in this configuration and with this specific SteriBest Tray packaging (including the added touchproof connection cable). Once shipped to Bioseal packed in bubble wrap, the company would return the probes in their sterilization boxes sealed in approved packaging. We found that this approach kept the electrodes intact and tracked throughout transport and sterilization. 

_Electrode fractures and disconnects._ We had instances of electrode fracture ( _n_ = 2), both of which were with the thinner Neuropixels 1.0 probes (thickness: 25 µm, width: 70 µm, length: 10 mm). We then switched to a thicker custom Neuropixels 1.0-S probe (thickness: 100 µm width: 70 µm, length: 10 mm) for the remaining recordings, and, of the seven uses of thick probes, we had only one instance of electrode fracture. In each instance, we documented whether the probes were intact afterward, both via the SpikeGLX software and through thorough photograph documentation. In the three probes that were fractured, we were able to photograph the pieces to reconstruct the entire probe to validate probe recovery. In the remaining probes, the photographs after the case confirmed that the electrodes were intact. In addition, in the intact probes after the case, the software check via SpikeGLX involved a hardware check, indicating that the probes were intact and fully functioning. 

We ensured that insertion of the electrodes was done under direct visual guidance for the entire process with loupe magnification, therefore allowing us to identify a mechanical break if it occurred. Throughout the entire process, the real-time recordings and impedance testing during placement and insertion provided real-time confirmation that the electrode had any stress or strain (which resulted in an error message in the software). If, at any point, a fracture or disconnection was noted, the electrode advancement was halted, and the 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

fractured electrode was removed. Importantly, though, and as communicated to the participants, only regions that were planned for resection or cortisectomy were implanted. These areas were, therefore, already planned for removal, meaning that, even in the event of a retained electrode, the tissue, together with electrode, can be safely and ethically removed. Finally, Neuropixels probes are radiopaque, meaning that they can be identified by imaging if needed. Importantly, all these considerations were always discussed with the participants before study consent. There were no instances of retained electrode components in our studies 

We previously investigated the use of a temporary stabilization using TISSEEL (Baxter) as has been used with single fine wire recordings[18] , but we found that, with the use of TISSEEL, we could not visualize where the Neuropixels probe was inserted, which was problematic as we were aiming for the small incision on the pial surface. In addition, we found that the sealant placed additional stress on the array shank, therefore increasing the risk of fracture. 

_Decreasing noise using referencing and grounding._ Even though we had tested the Neuropixels probe as well as had considerable experience in using Neuropixels in NHPs, which informed how we built our electrophysiological system[3] , we found that moving the Neuropixels recordings into the human operating room was made much more difficult with considerable added noise compared to any of the other testing settings. In the first four tests, we followed the original recommendations to tie the reference to the ground on the Neuropixels probe, which degraded the signal markedly in the operating room (Extended Data Fig. 1a). The signal was substantially improved by separating the ground and reference on the Neuropixels probe, with a single Medtronic sterile wire connected to the reference placed in the scalp and a separate wire attached to the ground and also placed in the scalp, as deemed safe by the neurosurgical team. Improving the signal in some cases involved tying the patient ground to the recording ground via a Bovie pad connected to the grounding BNC on the NI DAQ board used for the Neuropixels system. Placing the grounding lead into saline or cerebrospinal fluid degraded the signal by saturating the LFP and increasing noise in the system. 

_External sources of noise._ Changing the reference from the external reference in the software (using SpikeGLX) to the internal reference also increased noise substantially (Extended Data Fig. 1c). We also discovered that an external source of noise was the wall-powered anesthesia intravenous pump (as is commonly used during patient transport), which, when unplugged and operating on battery, would decrease the physiological noise. Finally, we did a series of tests to determine if other signals added sources of noise, and we did not find an effect of the Bovie cautery machine, the ROSA robot, the lights or other machines in the room. 

_Mechanical stabilization._ Two separate stabilization approaches were tested. One approach involved the patients receiving DBS implantations at MGH—patients who normally also undergo standardized microelectrode recording to optimize anatomical targeting[17][,][66] . In these patients, Neuropixels probes were inserted in the same locations as the microelectrodes that traverse the dorsal lateral surface of the prefrontal cortex on the way to the target nucleus, offering a brief chance to study neuronal dynamics in the dlPFC and not perturbing the planned operative approach nor altering clinical care[11][,][18][,][44][,][66][,][78] . Three cannulae were placed in a manipulator (Alpha Omega Engineering), and the Neuropixels probe was attached to the cannulae using Steri-Strips (3M Steri-Strip Reinforced Adhesive Skin Closures). The manipulator was attached to the ROSA ONE Brain (Zimmer Biomet) arm. The Neuropixels probe was put over the burr hole by the ROSA robot arm. ROSA was then used to insert the probe using fine millimeter steps, with some adjustment possible using the Alpha Omega micromanipulator. The second approach involved securing the Neuropixels probe to a sterile syringe, which was then held by a three-axis micromanipulator built for Utah array placement (Blackrock), which was attached to a Greenberg retractor. The Neuropixels probe was in place and lowered using the micromanipulator. 

**Compensation for tissue movement and electrode alignment through time.** We found clear evidence of vertical tissue movement relative to the Neuropixels probe in the LFP recordings (Extended Data Fig. 2). To confirm that this was due to movement of the tissue as well as the effects of heartbeat, we aligned the movement artifact to the heartbeat in time (this was possible thanks to audio tracking of the EKG in two participants’ cases). We found that the movement roughly matched this tracking. To confirm that the manual tracking could match the movement of the brain relative to the electrode, we performed tissue-level tracking of the video recordings of the case and found that we could align the filmed movement of the brain pumping relative to the electrode, which was well visualized in the LFP band across channels as tracked through time (Extended Data Fig. 2b). We tested several approaches to address this movement and correct for the alignment, including the Kilosort 3.0 drift adjustments and estimation (https://github.com/MouseLand/ Kilosort) and spike time-informed alignment approaches (https://github.com/ evarol/NeuropixelsRegistration). We chose to use the LFP-informed manual tracking as it was better resolved in the time domain because the dynamic range of LFP allowed for per time step (0.0004 s) alignment and interpolation. By contrast, the other automatic approach depended on firing rate and arrival of spikes, which were sparse (Fig. 1e,f). 

_Manual tracking of movement using LFP signals._ The signal was first extracted from the binary files into LFP (<500 Hz filtered data, sampled at 2,500 Hz) and AP (>500 Hz filtered data, sampled at 30,000 Hz) from SpikeGLX using MATLAB and available pre-processing code (https://billkarsh.github.io/SpikeGLX/). We inspected the data visually as well as examined the timeline of the recording to reject noisy time ranges (such as during insertion.) We then further examined the voltage deflections in the LFP for a prominent, bounded deflection in the voltage where we observed the voltage values shifting in unison (Extended Data Fig. 2), which was consistently present throughout the recording (blue or red bands in Extended Data Fig. 2). We attempted to use several algorithms to detect these shifts, but the multiple changes present (heart rate, slow and mid-range drifting and other shifts) were not effectively tracked by these algorithms. Instead, to capture the displacement in the movement bands, we imported the LFP voltage as an .stl file from MATLAB into Blender (https://www.blender.org/), a 3D animation program that allowed for easier manual tracing than MATLAB. Using the surface voltage and the Grease Pencil feature, we traced the shifting band of negatively deflecting LFP throughout the recording at a resolution of 500 Hz. The line produced was then exported as a .csv file and imported into MATLAB, where it was compared with the LFP at higher resolution to check whether the manual tracing matched the LFP displacement (Extended Data Fig. 2a). This traced line information was upsampled to 2,500 Hz to match the sampling frequency of the LFP channels (interp1, ‘makima’). 

_Pre-processing AP recordings._ Once we had the LFP baseline to track probe movement through time, we then applied analyses to the AP sampled band. To account for differences in the channels before aligning the data (as channels can have differences in impedance), we first de-trended data (which removes the best fitted line to each channel), calculated the median and subtracted it from all channels. We then normalized the voltage signal across channels by multiplying each channel’s voltage time series by a normalization factor, where normalized data = channel signal × (1/s.d.) × 600. In this case, the s.d. was the standard deviation of channel data without outliers, particularly epochs that were relatively quiet. We defined outliers as elements that were more than 1.5 interquartile ranges above the upper quartile or below the lower quartile of the distribution of voltage signals. Finally, we chose the value of 600 in the normalization to allow us to scale the data up to an int16 format for improved data resolution. 

_Alignment and interpolation of AP channels for manual registration._ To re-align the AP channel data so as to offset the movement artifact, we upsampled the traced line to 30 kHz to match the AP sampling rate (interp1, ‘makima’). We then, for each time bin, applied a spatial interpolation between channels vertically in two columns of the Neuropixels recording, resulting in a vertical spatial resolution of 1 µm (Extended Data Fig. 2). These steps resulted in a large, high-resolution interpolated matrix that we could then follow through time. This let us compensate for the movement effects by resampling the voltage in space (Extended Data Fig. 2) based on the manually registered movement trajectory described in the ‘Manual tracking of movement using LFP signals’ section. 

Specifically, for each time bin, we shifted the vertical channels vector up or down according the upsampled traced line, resulting in more than 450 ‘virtual channels’ that each contained voltage information putatively from a specific brain location. Finally, because the virtual channels on both ends (top and bottom of the shank) contained only partial data (due to brain movement relative to the electrode), we selected a subset of 384 virtual channels that contained the most continuous information throughout the recording (and did not shift channels into the edge), which could be inferred from the average channel offset. 

**Unit isolation and clustering.** Single-unit sorting was performed using Kilosort 3.0 (ref.[28] ) (https://github.com/MouseLand/Kilosort) as well as Phy (https://github. com/cortex-lab/phy) and then manually curated using in-house MATLAB code to visually inspect the template as well as the waveforms assigned to each cluster. The Kilosort 3.0 parameters included: Nblocks = 0, as no additional registration was needed according to spiking activity after the manual registration; and Threshold [10, 11] to be more strict in our detections (initial values were [9,9]), which resulted in ~800 units for Pt. 02. Clusters were merged in Phy if the templates were similar between clusters, if the spatial spread of waveforms was highly similar and if overlapping and cross-correlations of the event times indicated high levels of correlation. To further process and shift each individual waveform to correct for Kilosort3 misalignment, we also calculated the cross-correlation of individual waveforms with the cluster template and adjusted waveforms according to location of maximal voltage value per waveform in the sampled time. 

**Waveform feature analyses and classification.** Clusters were then separated into single units and MUA. Units were classified as MUA if there was a mixture of distinct waveforms (examined in Phy) as well as a complicated (and abnormal) autocorrelogram of spike times. For all units, we then measured the spike duration, half-width, peak–trough ratio, repolarization slope, recovery slope and amplitude measures (Fig. 2; code adapted from ref.[2] ; https://github.com/jiaxx/waveform_ classification). Furthermore, we applied the spatial spread and velocity measures to 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

**NAtuRE NEuRoScIENcE** 

## Technical RepoRT 

each cluster to identify whether we could observe evidence for back-propagating APs or other unique spatial dynamics (Fig. 2; code adapted from ref.[2] ). 

We used three different classification approaches to group the units. First, using a standard approach, units were grouped into RS, FS and PS classifications based on the spike waveform duration (valley-to-peak) of the largest peak across channels per unit[32][,][34][–][36][,][79][,][80] . The ranges for each classification were as follows: negative-going peaks, which included FS (duration <0.3 ms) and RS (duration >0.3 ms) and positive spikes (PS). Second, we applied PCA on the first six channels per unit and clustered these average waveforms using _k_ -means clustering (squared Euclidean distance, 1,000 replicates, 1,000 maximum iterations) into seven clusters based on the separability of the clusters (using silhouette) and how clean the resulting clusters were. Finally, we used a novel non-linear method, WaveMAP, which took into account the spatial and temporal waveform characteristics while separating out differences in the waveforms[44] . WaveMAP includes a combination of dimensionality reduction with UMAP combined with Louvain clustering to identify clusters in the dataset[33] . We then compared the waveform features across these different classifications. 

**LFP analyses.** For LFP analyses, we used custom MATLAB code (version R2020a) in combination with open-source code from the Fieldtrip toolbox (ref.[34] ; http:// www.fieldtriptoolbox.org/). 

**Burst suppression ratio measurement.** The burst suppression ratio was computed using an automated method[65][,][81] (https://github.com/drasros/bs_detector_icueeg). After averaging the LFP across all channels, this method then labels each time sample as either burst or suppression. In brief, the method uses the previous data with each channel and applies the following equations: 

**==> picture [121 x 22] intentionally omitted <==**

**==> picture [52 x 8] intentionally omitted <==**

where _xt_ is the value of the normalized signal of one channel at time _t_ , and _µt_ and _σt2_ are current values of the recursively estimated local mean and variance, respectively. Finally, _zt_ is an indicator function that labels each data point as either burst (0) or suppression (1). The value of _β_ determines the balance between the effect of recent and past datasets based on previously trained data[65] . The classification threshold _θ_ (that is, the value above which a data point should be classified as burst) was adjusted to evaluate our dataset visually with values of _θ_ = 50, 100, 150 and 200 and was informed by the input from two experts who reviewed selected intervals to identify burst and suppression using each possible _θ_ value. The value of _θ_ = 200 was selected to reliably identify burst and suppression induced by general anesthesia. The burst suppression ratio for each recording in an anesthetized patient ( _n_ = 2) was evaluated as the proportion of suppression-labeled samples in a moving window (1-s duration, no overlap). 

**IIDs.** In one case, the Neuropixels electrode was inserted into the lateral temporal lobe before tissue resection for epilepsy. As we could identify IIDs in the LFP, we applied both an automatic and a visual detection approach to verify the timing and location of the IIDs in the Neuropixels recording. For automatic detection, we averaged the LFP across channels and applied the algorithm of ref.[45] , version 21, with default settings except -h at 60 and -k1 at 7 to increase the threshold for detection (http://isarg.fel.cvut.cz), which adaptively models distributions of signal envelopes to discriminate IIDs from LFP[45] . In addition, a trained and experienced epileptologist (S.S.C.) examined the average LFPs and confirmed the timing of the detected IIDs. This two-step process was necessary as the burst suppression from the anesthesia produced waveforms that could obscure the IIDs. For several analyses, the single-unit spike times were then aligned relative to the peaks of the IIDs. 

**Statistics and reproducibility.** No statistical method was used to predetermine sample size. All statistical comparisons were performed using non-parametric measures, so we did not test for normality. Multiple comparisons tests were performed using the Kruskal–Wallis test for non-equivalence of multiple medians, followed by the post hoc Tukey–Kramer method to identify statistically separable groups. For comparisons between individual medians, we used the Wilcoxon rank-sum test (two sided). We corrected by adjusting the target _P_ value (0.05) with a Bonferroni correction for the number of comparisons being done. In addition, the investigators were not blinded to allocation during experiments and outcome assessment. The experiments were not randomized as this was an investigation into the feasibility and use of the Neuropixels probe to record neural activity in the human operating room. No statistical methods were used to predetermine sample sizes, but our sample sizes are similar to those reported in previous publications[10][,][82] . Randomization was not relevant to the study as this was a study performed in the human operating room and depended on patient consent and recording during different conditions, taking into account clinical considerations per participant. 

**Reporting Summary.** Further information on research design is available in the Nature Research Reporting Summary linked to this article. 

## **Data availability** 

The data is available for download at Dryad (https://doi.org/10.5061/dryad. d2547d840) upon publication. 

## **Code availability** 

Open-source acquisition software, SpikeGLX Release v20201103-phase30 (http://billkarsh.github.io/SpikeGLX/), was used to record the neural data. Single-unit sorting was performed using Kilosort 3.0 (ref.[28] ) (https://github. com/MouseLand/Kilosort) as well as Phy2 (https://github.com/cortex-lab/phy) custom MATLAB code (version R2020a), and Python code in combination with open-source code from the Fieldtrip toolbox (http://www.fieldtriptoolbox. org/) was used for most of the analyses, with some code involving manual alignment available on GitHub (https://github.com/Center-For-Neurotechnology/ CorticalNeuropixelProcessingPipeline). The burst suppression ratio was computed using an automated method[65][,][81] (https://github.com/drasros/bs_detector_icueeg). Reconstruction of electrode locations and the manual tracing was done using the open-source, free software Blender (https://www.blender.org/), Mango (http://ric. uthscsa.edu/mango/) and MMVT (https://github.com/pelednoam/mmvt). Violin plots showing the distribution of the data based on kernel density estimate using ksdensity in several figures were produced using code by the Holger Hoffmann (2021) violin plot (https://www.mathworks.com/matlabcentral/fileexchange/451 34-violin-plot) on the MATLAB Central File Exchange (retrieved 15 April 2021). 

## **References** 

66. Patel, S. R. et al. Studying task-related activity of individual neurons in the human brain. _Nat. Protoc._ **8** , 949–957 (2013). 

67. Reuter, M., Rosas, H. D. & Fischl, B. Highly accurate inverse consistent registration: a robust approach. _Neuroimage_ **53** , 1181–1196 (2010). 

68. Reuter, M., Schmansky, N. J., Rosas, H. D. & Fischl, B. Within-subject template estimation for unbiased longitudinal image analysis. _Neuroimage_ **61** , 1402–1418 (2012). 

69. Dykstra, A. R. et al. Individualized localization and cortical surface-based registration of intracranial electrodes. _Neuroimage_ **59** , 3563–3570 (2012). 

70. Holmes, C. J. et al. Enhancement of MR images using registration for signal averaging. _J. Comput. Assist. Tomogr._ **22** , 324–333 (1998). 

71. Felsenstein, O. et al. Multi-Modal Neuroimaging Analysis and Visualization Tool (MMVT). Preprint at https://arxiv.org/abs/1912.10079 (2019). 

72. Lancaster, J. L. et al. Automated regional behavioral analysis for human brain images. _Front. Neuroinform_ . **6** , 23 (2012). 

73. Lancaster, J. L. et al. Automated analysis of fundamental features of brain structures. _Neuroinformatics_ **9** , 371–380 (2011). 

74. Lancaster, J. L. et al. Anatomical global spatial normalization. _Neuroinformatics_ **8** , 171–182 (2010). 

75. Felsenstein, O. & Peled, N. Multi-Modality Visualization Tool (MMVT). https://doi.org/10.5281/zenodo.438343 (2017). 

76. Postelnicu, G., Zöllei, L. & Fischl, B. Combined volumetric and surface registration. _IEEE Trans. Med. Imaging_ **28** , 508–522 (2009). 

77. Mora Lopez, C. et al. A neural probe with up to 966 electrodes and up to 384 configurable channels in 0.13 μm SOI CMOS. _IEEE Trans. Biomed. Circuits Syst._ **11** , 510–522 (2017). 

78. Mian, M. K. et al. Encoding of rules by neurons in the human dorsolateral prefrontal cortex. _Cereb. Cortex_ **24** , 807–816 (2014). 

79. Dickey, C. W. et al. Travelling spindles create necessary conditions for spike-timing-dependent plasticity in humans. _Nat. Commun._ **12** , 1027 (2021). 

80. Snyder, A. C., Morais, M. J. & Smith, M. A. Dynamics of excitatory and inhibitory networks are differentially altered by selective attention. _J. Neurophysiol._ **116** , 1807–1820 (2016). 

81. Salami, P., Borzello, M., Kramer, M. A., Westover, M. B. & Cash, S. S. Quantification of seizure termination patterns reveals limited pathways to seizure end. Preprint at https://www.medrxiv.org/content/10.1101/2021.03.03. 21252789v1 (2021). 

82. Ganji, M. et al. Development and translation of PEDOT:PSS microelectrodes for intraoperative monitoring. _Adv. Funct. Mater._ **28** , 1700232 (2017). 

## **Acknowledgements** 

We would like to thank Y. Chou, A. Tripp, F. Minidio, A. Zhang and A. O’Donnell for help in data collection. We would like to especially thank the patients for their willingness to participate in this research. This research was supported by the ECOR and K24-NS088568 (to S.S.C.) and the Tiny Blue Dot Foundation (to S.S.C. and A.C.P.) and NIH grant U01NS121616 (to Z.M.W.). This research was also supported by NIH NINDS BRAIN R01NS11662301 (to K.V.S.), NIH NIDCD R01DC01403406 (to K.V.S.), the Simons Foundation (543045, to K.V.S.) and the Howard Hughes Medical Institute at Stanford University (to K.V.S., S.D.S. and E.M.T.). S.D.S. was supported by the A. P. Giannini Foundation and the Wu Tsai Neurosciences Institute Interdisciplinary Scholars 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

## **NAtuRE NEuRoScIENcE** 

Fellowship and holds a Career Award at the Scientific Interface from the Burroughs Wellcome Fund. E.M.T. is additionally funded by the Brain and Behavior Research Foundation and the Grossman Institute. The views and conclusions contained in this document are those of the authors and do not represent the official policies, either expressed or implied, of the funding sources. The funders had no role in study design, data collection and analysis, decision to publish or preparation of the manuscript. 

## **Author contributions** 

The experiment was conceived by S.S.C., Y.K., A.C.P., Z.W., K.V.S., L.R.H., E.M.T. and S.D.S. Z.W. and R.M.R. performed the surgeries and placed the arrays, and A.C.P., D.J.S., M.M., A.K. and Y.K. collected the data and did first-pass analysis. A.C.P., Y.K. and S.S.C. prepared the first manuscript draft. A.C.P. and Y.K. analyzed all the data for the final results, and A.C.P. prepared all the figures. All authors revised the manuscript. B.D., M.W. and E.M.T. conceived of and advanced the production of the thicker custom Neuropixels probes used in the study. All the authors edited the manuscript. 

## **Competing interests** 

K.V.S. is a consultant to Neuralink Corporation and CTRL-Labs, Inc. (now part of the Facebook Reality Labs division of Facebook) and is on the scientific advisory boards 

of Mind-X, Inc., Inscopix, Inc. and Heal, Inc. S.D.S. is a scientific advisor to Nēsos Corporation. The MGH Translational Research Center has clinical research support agreements with Neuralink, Paradromics and Synchron, for which S.S.C. and L.R.H. provide consultative input. None of these entities listed is involved with this research or the Neuropixels device. B.D. and M.W. are employees of IMEC, a non-profit semiconductor research and development organization that manufactures, sells and distributes the Neuropixels probes, at cost, to the research community. The remaining authors declare no competing interests. 

## **Additional information** 

**Extended data** is available for this paper at https://doi.org/10.1038/s41593-021-00997-0. **Supplementary information** The online version contains supplementary material available at https://doi.org/10.1038/s41593-021-00997-0. 

**Correspondence and requests for materials** should be addressed to Angelique C. Paulk, Ziv M. Williams or Sydney S. Cash. 

**Peer review information** _Nature Neuroscience_ thanks Ueli Rutishauser and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. 

**Reprints and permissions information** is available at www.nature.com/reprints. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [447 x 625] intentionally omitted <==**

**Extended Data Fig. 1 | See next page for caption.** 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

## **NAtuRE NEuRoScIENcE** 

**Extended Data Fig. 1 | Recording challenges and lessons learned.** Recording challenges and lessons learned. a. Diagram of the different combinations of ground and referencing and connections that improved the electrophysiological signal or degraded the signal with the indicated ground and reference contacts (including the external and internal reference). Each circled number indicates a combination tested. A major step in reducing noise levels was to separate the ground and reference, with a single separate wire going to the grounding pads on one side and another wire going to a grounding pad on the other side of the Neuropixels probe, pictured here. We used the external reference tied to a sterile MedTronic grounding wire with a needle which, when placed in the scalp or CSF, improved the signal and reduced 60 Hz noise. Common 60 Hz noise and other noise decreased considerably if the anesthesia IV pump was unplugged from the wall and was run on battery during the recordings. Otherwise, turning off lights or other sources of noise (BOVIE cautery machine, AlphaOmega recording system, etc.) had no noticeable effect on noise. b. Diagram of the connections relative to the participant including the BOVIE pad placed on the leg connected to the IMEC ground via a BNC cable to the NIDAQ PCI chassis BNC. c. Securing the wires and the probe to the cannulae attached to the AlphaOmega manipulator with Tegaderm and Steristrips improved the stability. d. Mechanical stabilization of the probe involved two options, one using the ROSA robot combined with an AlphaOmega manipulator with the Neuropixels probe secured to cannulae. e. The second option involved securing the Neuropixels probe to a sterile syringe using Steristrips. f. Then, the syringe is attached to a 3-axis manipulator mounted on a Greenberg retractor over the craniotomy. g. Every Neuropixels probe is documented and checked several times during and after the procedure both via software (in the OpenEphys or SpikeGLX software) and a quick saline test is done in the side sterile table. h. Each probe is photographed before, during, and afterward in the OR to determine if they are intact. Regular checks of the connections are done as the electrode is being moved into place in the sterile field. The electrode is also checked and photographed afterward for whether it is intact and connected. i. In two cases, 60 Hz noise was reduced by tying a ground to a spare BOVIE pad placed on the thigh of the patient under the sterile drape (as shown in b), with the traces shown with the lower left LFP trace showing the signal grounded to the BOVIE versus grounded to a scalp needle electrode. j. Examples of considerable noise in the LFP and high frequency range (AP range) when crossing the ground and reference together. k. We did test using the internal reference on the Neuropixels probe and found the noise increased considerably in the two cases we attempted the switch. l. The placement of the sterile ground and reference leads made a difference. Ground and reference in the scalp had an improved signal. Placing the ground (but not the reference) in the saline in the craniotomy caused the LFP signal to saturate and degraded the signal. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [499 x 650] intentionally omitted <==**

**Extended Data Fig. 2 | See next page for caption.** 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

## **NAtuRE NEuRoScIENcE** 

**Extended Data Fig. 2 | Putative Neuropixels probe location based on photographic evidence and identification of intracranial access to the cortical surface.** Putative Neuropixels probe location based on photographic evidence and identification of intracranial access to the cortical surface. a. preoperative MRI (Pt. 01) (displayed with Mango software10–12) with an overlay of the postoperative CT including the DBS leads and burr hole used to implant the DBS leads. As the Neuropixels probe was inserted through the burr hole, there was only a limited number of areas and approaches using angles in three dimensions to insert the Neuropixels probe. b. Taking measures of the burr hole (upper right in a), we reconstructed the burr hole relative to the participant’s brain (produced using FreeSurfer and MMVT5–9, to identify the possible locations for the Neuropixels probe insertion taking into account the size of the 3D structure of the headstage and insertion into a cortical gyrus. Grey surface is the pial surface and white reconstructed volume is the white matter for the participant. c-d. The resultant putative location of the Neuropixels probe based on these measures in 3D (c) and overlaid on the MRI (d). e-g. Same process but for Pt. 02. h. Photographs of the open craniotomy (Pt. 03) and process of tracing the sulci to identify location of the craniotomy. i. Reconstructed brain with the overlaid trace of the craniotomy photograph of the lateral temporal lobe, with the putative location of the inserted Neuropixels probe shown on the brain. j-k. The resultant putative location of the Neuropixels probe based on the projected photograph to the 3D location on the brain. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [509 x 591] intentionally omitted <==**

**Extended Data Fig. 3 | Realigning the data relative to heartbeat-induced movement artifact.** Realigning the data relative to heartbeat-induced movement artifact. a. Illustration of evidence of tissue movement relative to the electrode recordings in the LFP (shown in red-blue color scale with the range in µvolts shown in b). This is quantified by manually tracing these ‘band shifts’ using the Blender program, followed by detection of these movements in the LFP and tracking of these movements across channels (white line, second to rightmost plot). b. LFP before (left) and after (right) adjusting for movement effects. c. High frequency (action potential) frequency signal before (left) and after (right) adjusting for movement effects. d. Top row: Kilosort 3.0 registration and alignment alone could not compensate for the drift evident in the detected spike waveforms (left) and the estimated drift spanned hundreds of microns (right). Bottom row: manual alignment (a-b) followed by Kilosort 3.0 sorting resulted in improved spike alignment through time (left) and reduced drift (right). 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [509 x 650] intentionally omitted <==**

**==> picture [166 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
Extended Data Fig. 4 | See next page for caption.<br>**----- End of picture text -----**<br>


**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

**NAtuRE NEuRoScIENcE** 

## Technical RepoRT 

**Extended Data Fig. 4 | Cross correlation between the interpolated sorted units and the raw data.** Cross correlation between the interpolated sorted units and the raw data. a. tracked movement from the LFP for the three participants, including zoomed in views in the grey boxes. b. Log power of the tracked movement from LFP for one participant for 0-50 Hz (power curves, left, and spectrogram, right). c. Log power of the tracked movement from LFP for one participant for 0–5 Hz (power curves, left, and spectrogram, right). d. Power of two different frequency bands (1.5 and 0.02 Hz) of the tracked movement from LFP through time for one participant (power curves). e. Moving average calculated velocity (µm/sec) of the movement as tracked in the LFP per participant. f. Left: We could correlate the 12 channels with the waveforms on a per-unit and per channel level and overlay the raw data (black lines) and the sorted movement tracked data (red lines). Right: Approach for cross correlating the movement-corrected neural data and the raw signals by cross correlating the 12 channels of the sorted spikes with the raw data with tracking of individual units along the raw channel data (top, middle, purple dots) based on the cross-correlation values (shown in color map) which was paired with the LFP tracked movement (white lines). g. Mean and median velocity (µm/sec) of the movement as tracked in the LFP per participant. h. Correlation values between sorted units and raw data per unit across 12 channels per unit (Kruskal-Wallis multiple comparisons test; Chi-sq.=12.29; p = 0.0019). Scatter plots are individual unit correlation values per participant. i. Correlation values on the per-channel waveform basis between the interpolated and raw data sets versus the log spike rates per unit. Each dot indicates a unit. j. Mean variance in tracked cross-correlated single units. Asterisk indicates significant differences between each participant in the variance (Kruskal-Wallis multiple comparisons test; Chi-sq.=399.39; p < 0.00001). 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [489 x 650] intentionally omitted <==**

**Extended Data Fig. 5 | Example complex waveforms for six different units (each color-coded set of waveforms) across the data set.** Example complex waveforms for six different units (each color-coded set of waveforms) across the data set. Original waveforms are overlaid relative to the recorded channels, with the grey bars to the right indicating the location of the units along the Neuropixels probe. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [509 x 205] intentionally omitted <==**

**Extended Data Fig. 6 | PCA with k-means clustering.** PCA with k-means clustering. a. Percent variance explained by each principal component calculated across the first 6 channels per unit. b. Silhouette values for each k-means cluster number for the first 40 principal components after re-running the k-means clustering analyses 20 times (including 1000 iterations). Error bars indicate SEM over the repeated clustering analyses. c. Scatter plot of seven clusters (using k-means clustering) in the first three principal components. Color coding reflects different clusters. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [431 x 647] intentionally omitted <==**

**Extended Data Fig. 7 | See next page for caption.** 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**Extended Data Fig. 7 | Waveform Features of units Clustered with WaveMAP per participant.** Waveform Features of Units Clustered with WaveMAP per participant. a. Waveforms per cluster per patient (indicated as Pt. xx). The sorted clusters (with WaveMAP) was performed on the per-patient level which is in contrast with the WaveMAP clustering performed across all three participants (Fig. 3). b. The remaining measures are per patient, showing mean firing rate, peak-trough ratio, spatial spread, and depth violin plots for the different clusters. * indicate significant differences between putative cell or waveform types, Kruskal-Wallis multiple comparison test, p < 0.001. c. Electrode locations relative to the cortical surface and cortical regions. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [509 x 620] intentionally omitted <==**

**Extended Data Fig. 8 | See next page for caption.** 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

**NAtuRE NEuRoScIENcE** 

## Technical RepoRT 

**Extended Data Fig. 8 | Waveform measures.** Waveform measures and PCA with k-means clustering. a. Waveform measures on an example, spike waveform including the spike duration, halfwidth, peak-trough ratio, repolarization slope, recovery slope, and amplitude measures. b. Largest waveforms per unit showing positive polarity (grey) and negative polarity (black) waveforms across the data sets. c. Distribution of positive polarity (grey) and negative polarity (black) half-peak width and spike duration (peak-trough duration) of the largest waveform per unit (Pt. 01-03). d. The peak-trough ratio, repolarization slope, recovery slope of the channel with the largest waveform violin plots for the different clustered waveforms using the single channel and multichannel classifications. * indicate significant differences between all putative cell or waveform types, Kruskal-Wallis multiple comparison test, p < 0.001 with post hoc Tukey-Kramer test. Grey letters a-c indicate statistically separable groups. Left: single channel classifications. Middle: multichannel classification based on the principal components and k-means clustering across patients. Right: multichannel classification based on the WaveMAP clustering across patients. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [509 x 591] intentionally omitted <==**

**Extended Data Fig. 9 | Spatial waveform measures.** a. Spatial spread examples of individual units (averaged across all waveforms attributed to a given unit) across the left and right columns of the Neuropixels probe. Voltage indicated by the greyscale color scheme. Bottom plot: diagram (arrows) demonstrating the spatial mapping calculations, including spatial spread, velocity above (yellow arrow), and velocity below (cyan arrow) the center point (channel with the largest waveform). (Measures shown in Extended Data Fig. 4). b. The spatial spread, depth, velocity above, and velocity below the center point (channel with the largest waveform) violin plots are shown for the different waveform types. * indicate significant differences between all putative cell or waveform types, Kruskal-Wallis multiple comparison test, p < 0.001 with post hoc Tukey-Kramer test. Grey letters a-c indicate statistically separable groups. Left: single channel classifications. Middle: multichannel classification based on the principal components and k-means clustering across patients. Right: multichannel classification based on the WaveMAP clustering across patients. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Technical RepoRT 

**NAtuRE NEuRoScIENcE** 

**==> picture [509 x 515] intentionally omitted <==**

**Extended Data Fig. 10 | Single units through time and correlation relationships between units.** Single units through time and correlation relationships between units. a. Left: the raster plots of spike times throughout the recording for the different classes of single units as clustered by WaveMAP (color coded relative to the waveform from the channel with the largest amplitude per unit) as well as the MUA activity (grey). Right: Spike counts binned in 5 second bins throughout the recordings for the three participants. b. Example cross-covariance of the spike times between individual units of different putative classes as clustered by WaveMAP (as titled). The vertical blue line shows the mean per plot. 

**NATuRE NEuRoSCiENCE** | www.nature.com/natureneuroscience 

Angelique C. Paulk, Ziv M Williams, Sydney S Corresponding author(s): Cash 

**==> picture [228 x 36] intentionally omitted <==**

Last updated by author(s): Nov 30, 2021 

## Reporting Summary 

Nature Portfolio wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency in reporting. For further information on Nature Portfolio policies, see our Editorial Policies and the Editorial Policy Checklist. 

## Statistics 

For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section. 

n/a Confirmed 

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

Data collection Open source acquisition software, SpikeGLX Release v20201103-phase30 (http://billkarsh.github.io/SpikeGLX/) and record the neural data. Additional proprietary software such a Brainlab (Brainlab, Inc.) was used to visualize the electrode placement in the operating room. 

Data analysis Open source acquisition software, SpikeGLX Release v20201103-phase30 (http://billkarsh.github.io/SpikeGLX/) and record the neural data. Single unit sorting was performed using Kilosort 3.0 26(https://github.com/MouseLand/Kilosort) as well as Phy2 (https://github.com/cortexlab/phy ) Custom Matlab code (version R2020a) and python code in combination with open source code from the Fieldtrip toolbox (http:// www.fieldtriptoolbox.org/ ) was used for the majority of the analyses with some code involving manual alignment available on Github (https://github.com/Center-For-Neurotechnology/CorticalNeuropixelProcessingPipeline).   The burst suppression ratio (BSR) was computed using an automated method 35,36 (https://github.com/drasros/bs_detector_icueeg). Reconstruction of electrode locations and the manual tracing was done using the open source, free software Blender (v2.92) (https://www.blender.org/ ). Violin plots showing the distribution of the data based on kernel density estimate using ksdensity in several figures were produced using code by Holger Hoffmann (2021) violin Plot (https://www.mathworks.com/matlabcentral/fileexchange/45134-violin-plot) on the MATLAB Central File Exchange. Retrieved April 15, 2021. 

For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Portfolio guidelines for submitting code & software for further information. 

Data 

## Policy information about availability of data 

All manuscripts must include a data availability statement. This statement should provide the following information, where applicable: 

- Accession codes, unique identifiers, or web links for publicly available datasets 

- A description of any restrictions on data availability 

- For clinical datasets or third party data, please ensure that the statement adheres to our policy 

The data will be available for download at Dryad (https://doi.org/10.5061/dryad.d2547d840) upon publication. Further data sets which were used were neural reconstructions of human neurons from NeuroMorpho.Org 61–65 relative to the Neuropixels array and 1.5 mm Utah array. Neural reconstructions were from Neuromorpho.Org ID: NMO_86955, NMO_86997, NMO_109433, NMO_61420, and NMO_61421. 

## - Field specific reporting 

Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection. Life sciences Behavioural & social sciences Ecological, evolutionary & environmental sciences 

For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf 

## Life sciences study design 

All studies must disclose on these points even when the disclosure is negative. 

|Sample size<br>Data exclusions<br>Replication<br>Randomization<br>Blinding|Sample size was determined on the per-participant data set which was a total of N=9 participants, with data from 3 participants appropriate<br>for further analysis. The sample sizes were determined by the availability of the cases and based on patient and clinical consent.|
|---|---|
|||
||Data exclusions were based on the quality of the neural signal and if the probe could be used in the case. Supplemental Table 1 explains<br>inclusion and exclusion criteria in detail.|
|||
||As this is a technical report detailing both the failures and successes, were able to detail replicable failures and replicable successes in our<br>testing. In terms of replications of neural recordings, Here, we report successful recordings from the cortex of temporal and frontal lobes in<br>patients undergoing brain tissue resection to treat epilepsy (N=1, under general anesthesia, lateral temporal lobe) or during the implantation<br>of DBS leads to treat movement disorders (N=2, one awake and one under general anesthesia, dorsolateral prefrontal cortex) using<br>Neuropixels probes. We also report unsuccessful recordings – and lessons learned -- from six other cases performed while developing these<br>approaches in the supplemental data. Unsuccessful recordings were either due to electrode fracture (N=2, with the devices and pieces fully<br>recovered) or excessive noise during the recordings (N=4).|
|||
||Randomization was not relevant to the study as this was a study performed in the human operating room and depended on patient consent<br>and recording during different conditions taking into account clinical considerations per participant. In addition, this was not a clinical trial<br>examining treatment effects so much as a technical report to demonstrate the feasibility to record in the human brain using a Neuropixels<br>probe.|
|||
||Human data were de-identified and assigned a unique numerical code. Subsequent preprocessing, analysis, detection of physiological events,<br>and sorting were performed blinded to the conditions of the data acquisition.|



## Reporting for specific materials, systems and methods 

We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material, system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response. 

Materials & experimental systems Methods n/a Involved in the study n/a Involved in the study Antibodies ChIP-seq Eukaryotic cell lines Flow cytometry Palaeontology and archaeology MRI-based neuroimaging Animals and other organisms Human research participants Clinical data Dual use research of concern 

## Human research participants 

|Policy information about|studies involving human research participants|studies involving human research participants|studies involving human research participants|||
|---|---|---|---|---|---|
|||||||
|Population characteristics|||Recordings in the operating room were acquired with 9 participants (mean= 59 years old, ranging from 34 to 75; 7 female;|||
||||Supplemental Table 1) who were already scheduled for a craniotomy for concurrent clinical intraoperative neurophysiological|||
||||monitoring or testing for mapping motor, language, and sensory regions and removal of tissue as a result of tumor or|||
||||epilepsy or undergo intra-operative neurophysiology as part of their planned deep brain stimulator (DBS) placement.|||
|||||||
|||||||
|Recruitment|||Ahead of their clinically required surgery, patients were contacted via phone or in person if they were interested in|||
||||participating in the research. Participants were informed that participation in the experiment would not alter their clinical|||
||||treatment in any way, and that they could withdraw at any time without jeopardizing their clinical care. While this means|||
||||there could be biases toward gathering data from patients who both consented and are being treated for neurological|||
||||diseases, this had a minimal effect on results as we were recording underlying neural activity in these cases to demonstrate|||
||||feasibility of the use of the Neuropixels devices in the neurosurgical operating room.|||
|||||||
|||||||
|Ethics oversight|||All patients voluntarily participated after|informed consent according to guidelines as monitored by the Partners Institutional||
||||Review Board (IRB) Massachusetts General Hospital (MGH).|||
|||||||



Note that full information on the approval of the study protocol must also be provided in the manuscript. 

