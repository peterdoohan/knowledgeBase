Article 

## Cell-Type-Specific Control of Brainstem Locomotor Circuits by Basal Ganglia 

## Graphical Abstract 

**==> picture [286 x 287] intentionally omitted <==**

## Authors 

Thomas K. Roseberry, A. Moses Lee, Arnaud L. Lalive, Linda Wilbrecht, Antonello Bonci, Anatol C. Kreitzer 

## Correspondence 

akreitzer@gladstone.ucsf.edu 

## In Brief 

The basal ganglia bi-directionally regulate a population of brainstem glutamatergic neurons that encode features of running behavior. Cell-type-specific control of functionally distinct neuronal subpopulations may represent a more general principle underlying the regulation of motor behavior by basal ganglia. 

## Highlights 

- d Basal ganglion circuits regulate the mesencephalic locomotor region (MLR) 

- d Basal ganglion output neurons selectively target MLR glutamatergic neurons 

- d MLR glutamatergic neurons are necessary and sufficient for locomotion 

- d MLR glutamatergic neurons are required for basal ganglion locomotor control 

**==> picture [20 x 20] intentionally omitted <==**

Roseberry et al., 2016, Cell 164, 526–537 January 28, 2016 ª2016 Elsevier Inc. http://dx.doi.org/10.1016/j.cell.2015.12.037 

Article 

**==> picture [60 x 60] intentionally omitted <==**

## Cell-Type-Specific Control of Brainstem Locomotor Circuits by Basal Ganglia 

Thomas K. Roseberry,[1,2,9] A. Moses Lee,[1,2,3,9] Arnaud L. Lalive,[1] Linda Wilbrecht,[4] Antonello Bonci,[5,6,7] and Anatol C. Kreitzer[1,2,3,8,] * 

1The Gladstone Institutes, San Francisco, CA 94158, USA 

2Neuroscience Graduate Program, University of California, San Francisco, San Francisco, CA 94158, USA 

3Medical Scientist Training Program, University of California, San Francisco, San Francisco, CA 94158, USA 

4Department of Psychology, University of California, Berkeley, Berkeley, CA 94720, USA 

5Intramural Research Program, Synaptic Plasticity Section, National Institute for Drug Abuse, Baltimore, MD 21224, USA 

6Solomon H. Snyder Department of Neuroscience, Johns Hopkins University, Baltimore, MD 21205, USA 

7Department of Psychiatry, Johns Hopkins University, Baltimore, MD 21287, USA 

8Departments of Physiology and Neurology, University of California, San Francisco, San Francisco, CA 94158, USA 9 

*Correspondence: akreitzer@gladstone.ucsf.edu http://dx.doi.org/10.1016/j.cell.2015.12.037 

## SUMMARY 

The basal ganglia (BG) are critical for adaptive motor control, but the circuit principles underlying their pathway-specific modulation of target regions are not well understood. Here, we dissect the mechanisms underlying BG direct and indirect pathwaymediated control of the mesencephalic locomotor region (MLR), a brainstem target of BG that is critical for locomotion. We optogenetically dissect the locomotor function of the three neurochemically distinct cell types within the MLR: glutamatergic, GABAergic, and cholinergic neurons. We find that the glutamatergic subpopulation encodes locomotor state and speed, is necessary and sufficient for locomotion, and is selectively innervated by BG. We further show activation and suppression, respectively, of MLR glutamatergic neurons by direct and indirect pathways, which is required for bidirectional control of locomotion by BG circuits. These findings provide a fundamental understanding of how BG can initiate or suppress a motor program through celltype-specific regulation of neurons linked to specific actions. 

## INTRODUCTION 

The ability to move through the environment to obtain energy, escape predators, and reproduce is fundamental for an animal’s survival. In vertebrates, phylogenetically conserved brainstem and spinal circuitry mediates the control of axial muscles and limbs that drive locomotion (Garcia-Rill, 1986; Grillner et al., 2005; Orlovsky et al., 1999; Shik et al., 1966a). In addition, upstream circuitry responsible for deciding when and how to move must be engaged. The basal ganglia (BG) has long been hypothesized to be a key arbitrator of the decision process that results in goal-directed locomotion (Garcia-Rill, 1986; Grill- 

ner et al., 2008; Hikosaka et al., 2000). Canonically, the BG consists of two pathways that separate at the level of the striatum, the main input nucleus of the BG. Striatal medium spiny neurons (MSNs) expressing the dopamine D1 receptor mark the direct pathway (dMSNs) and are proposed to facilitate movement, and MSNs expressing the dopamine D2 and adenosine 2a (A2a) receptor mark the indirect pathway (iMSNs) and are proposed to suppress movement (Albin et al., 1989; DeLong, 1990; Kreitzer and Malenka, 2008). These pathways re-converge in the substantia nigra pars reticulata (SNr), the primary output nucleus of basal ganglia in rodents, which provides tonic inhibition of downstream structures responsible for the execution of motor programs (Hikosaka et al., 2000). Recent work from our laboratory has established that optogenetic activation of dMSNs increases locomotion, whereas activation of iMSNs suppresses locomotion (Kravitz et al., 2010). However, the effect of basal ganglia circuitry on downstream targets controlling locomotion remains unknown. 

The BG locomotor command is thought to be relayed to spinal cord central pattern generators through the mesencephalic locomotor region (MLR), a brainstem area first described in 1966 by Shik et al. (1966b). The MLR is defined functionally as a mesencephalic region in which increasing intensities of electrical stimulation induce a transition from a stationary state to walking and then running with short latencies (Shik et al., 1966a, 1966b). In mammals, the MLR overlaps with the cuneiform nucleus (Cun), mesencephalic reticular nucleus (MRN), and pedunculopontine tegmental nucleus (PPTg) (Garcia-Rill et al., 1986; Ryczko and Dubuc, 2013). The MLR is comprised of three neurochemically distinct cell types: glutamatergic, GABAergic, and cholinergic (Martinez-Gonzalez et al., 2011). Although the major cell populations of the MLR give rise to ascending projections into the forebrain that may be relevant for reward, arousal, and cortical state (Ehrich et al., 2014; Grace, 2010; Lee et al., 2014; Thompson and Felsen, 2013), the control of locomotion appears to be driven through descending outputs because locomotion is intact in decerebrate animals (Bedford et al., 1992; Whelan, 1996). 

Previous work has demonstrated that subsets of neurons in the MLR are correlated with locomotion (Lee et al., 2014; Norton 

**==> picture [20 x 20] intentionally omitted <==**

526 Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

et al., 2011; Thankachan et al., 2012). However, less is known about the activity of identified MLR glutamate neurons in vivo and whether their activity is actually necessary for locomotion. Moreover, the function of the cholinergic and GABAergic populations during locomotion is not clear. To investigate the locomotor function of MLR cell types and their control by BG circuitry, we combined cell-type-specific optogenetic manipulations, in vivo single-unit recording from identified cells, virus-based circuit mapping, and high-resolution behavioral assays to explore how signals from the BG are transduced into locomotion through the MLR. Our results highlight the functional differences among cell types in the MLR and the remarkable specificity of BG-brainstem projections. In addition to defining the pathway through which BG regulate locomotion, these results provide a more general framework for how BG can initiate or suppress action by specific modulation of neuronal sub-types associated with a motor program. 

## RESULTS 

## 

To identify the location of the MLR in the mouse, we used a headfixed preparation that allowed the subject to walk on a spherical treadmill (trackball) suspended by air (Figure 1A). All subsequent experiments were performed using this preparation unless stated otherwise. Five seconds of electrical stimulation at 20 Hz using a bipolar electrode placed near the PPTg elicited a transition from a stationary state to running (Figures 1B and 1C; mean latency to movement onset, 1580 ± 165 ms), confirming the existence of the MLR. To determine the anatomical extent of the MLR, we systematically stimulated across multiple areas in the mesencephalon and histologically confirmed electrode placements that elicited locomotion with latencies of <2 s. These experiments confirmed that the MLR overlaps with the Cun, PPTg, and MRN (Figure 1D), consistent with other species (Ryczko and Dubuc, 2013). 

## Bidirectional Modulation of MLR Neurons by the BG 

The direct and indirect pathways of the BG exert opposing effects on locomotion (Bateup et al., 2010; Kravitz et al., 2010). To determine how these pathways modulate activity in the MLR, we injected D1-Cre mice to activate dMSNs or A2a-Cre mice to activate iMSNs with an adeno-associated virus for Cre-dependent expression of channelrhodopsin (double-floxed inverted open reading frame [DIO]-ChR2) into the striatum. We then recorded from well isolated, single units in the MLR while stimulating ChR2-expressing neurons in the striatum (Figures 1E and 1I). Unilateral dMSN stimulation resulted in contraversive locomotion when initiated while the mouse was stationary (mean latency to movement onset, 565 ± 78 ms; Figure 1F). Although a majority of MLR neurons increased their firing rate in response to dMSN stimulation, a large fraction was either unmodulated or inhibited (Figures 1F and 1G). We continued to record these neurons after the stimulation session as the mice ran spontaneously on the trackball. Receiver operating characteristic (ROC) analysis revealed that neurons excited by dMSN stimulation were also significantly more predictive of the running state than the stationary state compared with dMSN-unmodulated or dMSN- 

inhibited neurons (Figure 1G; p < 0.01, Kruskal-Wallis one-way ANOVA, c[2] 2,39[= 15.96, with Dunn-Sidak post test). Conversely,] 5 s of bilateral iMSN stimulation resulted in a transition from running to the stationary state (mean deceleration onset, 651 ± 34 ms) and inhibition of a majority of recorded units in the MLR (Figures 1I and 1J). ROC analysis of spontaneous running revealed no relationship between iMSN modulation and prediction of the locomotor state (Figure 1J). These results demonstrate that the BG can modulate activity within the MLR, although the responses within the MLR are heterogeneous. 

## Functional Dissection of MLR Cell Types 

To better understand the relationship between MLR cell types and locomotion, we next examined how optogenetic activation of each cell type affects locomotion. Glutamatergic or GABAergic neurons were transduced by injecting a Cre-inducible virus expressing ChR2-YFP into vGLUT2-Cre or vGAT-Cre mice (Figures 2B and 2C). Whole-cell recordings confirmed that infected neurons released either glutamate or GABA by blocking excitatory postsynaptic currents (EPSCs) or inhibitory postsynaptic currents (IPSCs), respectively, with antagonists (Figures S1A–S1D). Cholinergic neurons were labeled in transgenic mice expressing ChR2-YFP under the choline acetyltransferase promoter (Zhao et al., 2011; Figure 2A). 10-ms light pulses delivered at 20 Hz to the glutamatergic population for 5 s elicited robust locomotion (Figures 2F and 2I) at significantly shorter latencies than electrical stimulation (mean movement onset, 211 ± 22 ms; p < 0.01; Wilcoxon rank-sum test). The speed reached at the end of stimulation was graded by stimulation frequency (Borgius et al., 2010; Lee et al., 2014), a canonical feature of the MLR (Figure 2K). In contrast, stimulation of the GABAergic population during running caused deceleration (mean deceleration onset, 837 ± 99 ms; Figures 2H and S2F) but no change when the mouse was stationary at the beginning of stimulation (Figures 2E and 2J). Choline acetyltransferase (ChAT) neuron stimulation resulted in a significant increase in speed during trials when the mouse was running but not when the mouse was stopped (Figures 2D, 2G, and 2J and S2F). Therefore, ChAT neurons appear to modulate locomotion but are not sufficient to drive locomotion at short latencies. This modulation did not appear to result from co-release of glutamate or GABA because no EPSCs or IPSCs were observed in the MLR during light stimulation in slice (Figure S1E). eYFP controls showed no significant changes in locomotion (Figures 2J and S2F). Together, these results indicate that increased activity within the glutamatergic population alone is sufficient to drive locomotion. 

## MLR Glutamatergic Neurons Encode Locomotion 

To understand how MLR glutamatergic neuron firing relates to locomotion, we injected vGLUT2-Cre mice with DIO-ChR2 in the MLR to optogenetically identify glutamatergic neurons and record their activity during spontaneous locomotion (Figure 3A). Experiments began with an identification session in which 473-nm light was pulsed for 10 ms at 1–2 Hz while evoked single-unit activity was recorded. Well isolated single units that displayed increased firing within 5 ms of light onset and had spontaneous and light-evoked waveform correlations of >0.9 (Pearson’s correlation coefficient) were considered 

Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 527 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 443] intentionally omitted <==**

Figure 1. Mapping and Bidirectional BG Regulation of the MLR 

(A) Illustration of the head-fixed trackball setup. 

- (B) Schematic of stimulation within the MLR. Th, thalamus; Str, striatum; Ctx, cortex. 

- (C) Population time course for mouse speed aligned to 20-Hz electrical stimulation (Elec. stim., n = 7 mice). 

(D) MLR mapping using electrical stimulation. Green circles represent electrode placement at which stimulation elicited locomotion (>5 cm/s) with short latency (<2 s), red Xs represent electrode placement where no running was observed. IC, inferior colliculus; RRF, retrorubral field; RR, retrorubral nucleus; LL, lateral lemniscus; PB, parabrachial nucleus (n = 13 mice). 

- (E) Schematic for stimulation of striatal dMSNs while recording activity in the MLR. 

(F) Example neuron excited during dMSN stimulation. Top: rasters of individual trials. Bottom: peristimulus time histogram (PSTH) of firing rate (purple line) and mouse speed (black line) aligned to onset of stimulation. (G) Histogram of AUCs for speed versus firing rate during a spontaneous locomotor session after dMSN stimulation. Black bars, neurons excited by dMSN stimulation (dMSN exc); gray bars, neurons unmodulated by dMSN stimulation (dMSN nm); open bars, neurons inhibited by dMSN stimulation (dMSN inhib) (n = 42 neurons from 4 mice). 

- (H) Schematic for stimulation of striatal iMSNs while recording activity in the MLR. 

- (I) Example neuron inhibited during iMSN stimulation as in (F). 

- (J) Histogram of AUCs for speed versus firing rate during a spontaneous locomotor session after iMSN stimulation. Gray bars, neurons unmodulated by iMSN stimulation (iMSN nm); open bars, neurons inhibited by iMSN stimulation (iMSN inhib) (n = 26 neurons from 4 mice). All shaded regions, SEM. 

528 Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

Figure 2. Distinct Functions of MLR Cell Types 

(A–C) Confocal images of coronal sections through the MLR of ChAT-ChR2 (A), vGATCre::DIO-ChR2 (B), and vGLUT2-Cre::DIO-ChR2 (C) counterstained for ChAT, which demarcates the boundaries of the PPTg. Insets show the location of the image. Scale bars, 25 mm. (D–I) Population time course for mouse speed aligned to 20-Hz optical stimulation from stationary (D–F) and running (G–I) states in ChAT-ChR2 mice (D and G; n = 5 mice, 7 hemispheres), vGATCre::DIO-ChR2 mice (E and H; n = 4 mice, 6 hemispheres), and vGLUT2-Cre::DIO-ChR2 mice (F and I; n = 6 mice, 7 hemispheres). Shaded regions, SEM. 

(J) Summary of population speed 5 s after stimulation onset (***p < 10[�][4] , Kruskal-Wallis one-way ANOVA, c[2] 3,243[=][175.52,][p][<][10][�][10][,][with][Dunn-] Sidak post test). ns, not significant. (K) Summary of speed at 5 s during graded stimulation of glutamatergic neurons (***p < 10[�][4] , Kruskal-Wallis one-way ANOVA, c[2] 2,167[= 175.52,] p < 10[�][5] , with Dunn-Sidak post test). All shaded regions, SEM. See also Figures S1 and S2. 

glutamatergic (Figures 3B–3D). A locomotor session followed in which the same single-unit activity was recorded during spontaneous running (Figure 3E). A second identification session was run after the locomotor session to ensure that there was no drift. Neurons that were held for all three sessions (based on cluster analysis, see Experimental Procedures) and found to be inside the functional boundaries of the MLR were kept for analysis (Figures 3B–3D). To quantify how closely these neurons encode the running state, we performed ROC analysis on the firing rate and speed data. The firing rate of individual MLR glutamatergic neurons was highly predictive of the running state (Figure 3F). 

In contrast, unidentified neurons from a separate cohort of mice displayed significantly lower areas under the curve (AUCs), indicating functional heterogeneity among MLR neuronal subpopulations (Figure 3F). To further dissect this result, we tested the locomotor-predictive MLR glutamatergic neurons for correlations with speed using a linear regression model. This analysis yielded two distinct populations: one that predicts locomotor state alone and one that predicts state and correlates with speed (Figure 3G). We next tested whether the glutamatergic neuron firing rate was predictive of locomotor starts. Glutamatergic neurons as a population increased their firing rate prior to the onset of a spontaneous locomotor start (Figure 3H). However, in individual trials, spiking increase onset was highly variable, and an absolute threshold at which spiking would correlate with running onset was not observed (Figure 3H, inset). Therefore, we tested the prediction that spiking increases during the stationary state would result in an increased probability of running onset. Indeed, an increased firing rate during the stationary state was correlated with an increase in the probability of a start occurring within the next second (Figure 3I; Pearson’s correlation coefficient; p < 0.01). This suggests that, at the individual level, glutamatergic neurons do not predict the timing of locomotion onset. Rather, these neurons contribute to an increased probability of locomotion that is read out from the population. These findings indicate 

Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 529 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 331] intentionally omitted <==**

Figure 3. Characterization of MLR Glutamatergic Neurons 

(A) Schematic of the optical tagging and recording setup in vGLUT2-Cre::DIO-ChR2 mice. ID, identified. 

(B) Recording sites for ChR2-positive (glutamatergic) neurons. 

(C) Top: light-evoked and spontaneous waveforms of an identified neuron. Bottom: PC1 versus PC2 for the neuron. Light gray dots, noise; dark gray dots, spontaneous spikes; blue dots, light-evoked spikes. 

(D) Raster (top) and PSTH (bottom) for a light-reactive neuron showing 3-ms latency aligned to laser onset. 

(E) Smoothed firing rate of the neuron identified in (C) and (D) (green line, left axis) plotted with the speed of the mouse (black line, right axis). (F) Histogram of AUCs for all recorded neurons during spontaneous locomotion. Green bars, identified glutamatergic neurons (all significantly encoded the stationary or locomotor state); filled gray bars, unidentified neurons recorded in the MLR from a separate cohort that significantly encoded the stationary or running state; open gray bars, neurons that did not significantly encode either state; arrows, means (**p < 0.001, Wilcoxon rank-sum test). (G) Histogram of R[2] values for the glutamatergic neurons that predicted locomotion in (F) (n = 14). Light green bars, speed-correlated (corr) neurons; dark green bars, neurons not correlated with speed. 

(H) Population Z-scored firing rate of identified glutamatergic neurons (green trace) aligned to onset of locomotion. Black trace, speed. Inset, individual example firing rate traces (light green) and average (dark green) aligned to starts. 

(I) Probability of a start within 1 s given Z-scored firing rate. Each point represents one binned data point (0.1-SD bins) from one neuron. All shaded regions, SEM. See also Figure S3. 

that MLR glutamatergic activity is tightly linked with and predictive of an animal’s locomotor state and speed. 

## MLR Glutamatergic Neurons Are Required for Spontaneous Locomotion 

Because activity in MLR glutamatergic neurons is sufficient for locomotion and encodes locomotor state and speed, we next tested whether they are necessary for spontaneous running. Previous experiments examining inhibition of the MLR have reported mixed effects on locomotion, most likely because of the longterm and non-specific effects of pharmacological interventions 

(Saper et al., 1979; Sinnamon et al., 1987). To specifically inhibit the glutamatergic population on a millisecond timescale, we expressed halorhodopsin (eNpHR3.0) under the calcium/calmodulin-dependent kinase IIa (CaMKIIa) promoter, which targets glutamatergic neurons in the MLR with high selectivity (Lee et al., 2014; Figures 4A and S3A and S3B). Photo-inhibition of MLR glutamatergic neurons caused running animals to decelerate rapidly, often to a full stop (mean deceleration onset, 835 ± 103 ms; Figures 4B–4D), whereas control animals showed only a gradual decrease in mean speed over time, consistent with a low baseline probability of spontaneous stopping. This 

530 Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [192 x 398] intentionally omitted <==**

Figure 4. Inhibition of MLR Glutamatergic Neurons Impedes Running 

(A) Experimental schematic for inhibiting glutamatergic neurons in the MLR. WT, wild-type. 

(B) Speed aligned to laser onset or with no stimulation (eNpHR3.0 in MLR, orange line, n = 4 mice; eYFP in MLR, black line, n = 6 mice). (C) Number of stops during laser inhibition for each group. (D) Speed summary data 5 s after onset of laser inhibition. 

- *p < 0.05, **p < 0.01, Wilcoxon rank-sum test. Shaded regions, SEM. 

result indicates that MLR glutamatergic neurons are necessary for spontaneous locomotion. 

## MLR GABAergic Neurons Suppress Activity in the MLR 

Because activation of the MLR GABAergic population decreased locomotion, we next examined whether these neurons locally inhibited other MLR neurons. In MLR slices prepared from mice expressing ChR2-eYFP in GABAergic neurons, IPSCs and inhibition of spiking were observed during whole-cell recordings from ChR2-eYFP-negative cells in response to optogenetic stimulation (Figures S1C–S1DD and S4A). In vivo re- 

cordings during optogenetic stimulation of MLR GABA neurons demonstrated that the majority of non-light-sensitive neurons were inhibited for the duration of illumination (Figures S4B– S4C). Because activity in MLR glutamatergic neurons is required for running (Figure 4), deceleration and stopping because of optogenetic activation of GABAergic neurons is likely in part due to local inhibition of MLR glutamatergic neurons. However, in vivo recordings from optogenetically identified MLR GABA neurons during spontaneous locomotion revealed heterogeneous responses, indicating additional complexity in the composition and function of this subpopulation (Figure S4D). 

## Brain-wide Tracing of Monosynaptic Inputs to MLR Glutamatergic and GABAergic Neurons 

We next tested the connection strength between the BG and the two MLR populations displaying the most robust effects on locomotion. In theory, BG-driven locomotion could be initiated by disinhibition of MLR glutamatergic neurons (Grillner et al., 2008; Hikosaka et al., 2000) or inhibition of GABAergic neurons. A difference in connection strength from the BG could discriminate between these possibilities. We used a cell-type-specific G-deleted rabies virus strategy to map neurons that directly target MLR glutamatergic or GABAergic neurons (Wall et al., 2013). vGLUT2-Cre or vGAT-Cre mice were injected with an adeno-associated virus (AAV) encoding rabies virus glycoprotein (RG) and a separate virus encoding a Cre-inducible avian receptor (TVA-mCherry) in the MLR on day 1. Only Cre-expressing cells will express the avian tumor virus receptor A (TVA receptor), which is required for rabies transduction. On day 14, mice were injected in the same area with modified rabies virus. Nine days later, the mice were perfused, and the brains were processed (Figure 5A). Retrograde trans-synaptic labeling from MLR glutamatergic neurons revealed dense projections from several BG nuclei, whereas few, if any, projections targeted MLR GABAergic neurons (Figures 5C–5F). A brain-wide survey of long-range projections to these cell types revealed another strong projection to MLR glutamatergic neurons from the central amygdala and oval bed nucleus of the stria terminalis (ovBNST), GABAergic nuclei that could play a role in fear- and anxietyassociated behaviors such as freezing (Figure 5F; LeDoux, 2000). Major MLR GABAergic targeting regions included the superior colliculus, dorsal raphe, laterodorsal tegmentum, and ovBNST. Together, these results suggest a specific role for MLR glutamatergic neurons in the control of locomotion by upstream targets and, notably, the BG. 

## Modulation of MLR Glutamatergic Neurons Is Required for Bidirectional Control of Locomotion by BG Circuitry 

To test how the direct and indirect pathways specifically modulate the MLR glutamatergic population, we optogenetically identified MLR glutamatergic neurons and recorded their activity while simultaneously stimulating dMSNs or iMSNs in the striatum. We expressed ChR2 in dMSNs or iMSNs using Cre-dependent viruses injected into the striatum of D1- or A2A-Cre mice. In the same mice, we expressed ChR2 in MLR glutamatergic neurons for optogenetic identification using a virus expressing ChR2 under the CaMKIIa promoter (Figures 6A and 6E). Each 

Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 531 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 422] intentionally omitted <==**

Figure 5. Brain-wide Mapping of Inputs to MLR Glutamatergic and GABAergic Neurons (A) Schematic and time course of the experiment. (B) Left: coronal section through the MLR showing TVA-mCherry labeling (blue) around the PPTg (labeled with ChAT staining, pink) and center of mass of TVA and RG injection sites (blue dots, vGAT-Cre::TVA+RG; green dots, vGLUT2-Cre::TVA+RG). Right: close-up of infected cells. Scale bars, 500 mm. (C and D) Examples of eYFP expression in the SNr in vGLUT2-Cre::Rabies-eYFP (C) and vGAT-Cre::Rabies-eYFP (D) mice. Scale bars, 200 mm. (E) Quantification of labeled cell counts from all BG nuclei in vGLUT2-Cre::Rabies-eYFP (green bars) and vGAT-Cre::Rabies-eYFP mice (blue bars). **p < 0.01, Wilcoxon rank-sum test. (F) Quantification of ipsilateral inputs to MLR glutamatergic (green) and GABAergic (blue) neurons. SNc, substantia nigra pars compacta; DMS, dorsomedial striatum; VS, ventral striatum; VTA, ventral tegmental area; CeA, central amygdalar nucleus; LDTg, laterodorsal tegmental nucleus. Error bars, SEM. 

experiment began with an identification session to find putative glutamatergic neurons based on the criteria listed previously. CaMKIIa-ChR2 had similar light responses as the vGLUT2Cre::DIO-ChR2 strategy (Figures S3C–S3D). After MLR neuron identification, we stimulated striatal dMSNs or iMSNs (5 s of continuous light) while recording MLR glutamatergic neuron activity. This was followed by a second MLR neuron identification session. Fiber and electrode placements were confirmed post hoc (Figures S5A–S5F). 

Unilateral dMSN stimulation significantly increased the firing rate in 25 of 26 identified MLR glutamatergic neurons (Figure 6B). In each case, the increase in firing rate preceded movement onset (mean latency to excitation, 176 ± 18 ms; Figures 6B and S5J–S5K). In contrast, bilateral iMSN stimulation delivered while the mouse was running significantly decreased the firing rate in 25 of 27 identified MLR glutamatergic neurons (Figure 6F). Deceleration was preceded by a decreases in firing rate in the majority of identified MLR glutamatergic neurons (mean latency 

532 Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [419 x 399] intentionally omitted <==**

Figure 6. MLR Glutamatergic Neurons Are Necessary and Sufficient to Reverse the Effects of BG Stimulation (A) Schematic for recording MLR glutamatergic neurons while activating dMSNs in the striatum. (B) Left: Z-scored firing rate of identified glutamatergic neurons (green line, left axis) and speed (black line, right axis) aligned to onset of 5-s unilateral dMSN stimulation from stop. Right: fractions of excited (excite), inhibited (inhib), or non-modulated (nm) units in unidentified recordings (un-IDed, left) and in identified glutamatergic cells (IDed, right) (identified: 25 excited, 0 inhibited, 1 non-modulated from 4 mice; unidentified: 22 excited, 11 inhibited, 9 non-modulated from 4 mice; **p < 0.001, c[2] test). 

(C) Schematic for stimulating dMSNs in the striatum while inhibiting MLR glutamatergic neurons. (D) Left: speed aligned to unilateral dMSN stimulation. Orange line, trials in which green light was turned on in the MLR 5 s after dMSN stimulation; black line, interleaved trials in which green light was omitted; purple line, no stimulation trials when mouse was stopped. Right: speed 10 s after onset of dMSN stimulation (***p < 10[�][4] , Kruskal-Wallis one-way ANOVA, c[2] 3,136[= 92.35, p < 10][�][10][, with Dunn-Sidak post test).] (E) Schematic for recording identified MLR glutamatergic neurons while activating iMSNs in the striatum. (F) Left: Z-scored firing rate of glutamatergic neurons (green line, left axis) and speed (black line, right axis) aligned to onset of 5-s bilateral iMSN stimulation from running. Right: summaries for the number of inhibited or non-modulated units in unidentified (left) recordings and identified (right) glutamatergic neurons (identified: 25 inhibited, 2 unmodulated from 4 mice; unidentified: 18 inhibited, 8 unmodulated from 3 mice; p = 0.09, c[2] test). (G) Schematic for stimulating iMSNs in the striatum while stimulating glutamatergic cells in the MLR. 

(H) Left: time course of mouse speed aligned to bilateral iMSN stimulation. Red line, trials in which blue light was turned on in the MLR at 20 Hz 5 s after iMSN stimulation; black line, interleaved trials in which green light was omitted; purple line, no stimulation trials when the mouse was running. Right: summary of mouse speed 10 s after onset of iMSN stimulation (***p < 10[�][4] , Kruskal-Wallis one-way ANOVA, c[2] 3,105[= 75.06, p < 10][�][10][, with Dunn-Sidak post test).] Shaded regions, SEM. See also Figures S5 and S6. 

to inhibition, 460 ± 48 ms; Figures 6F and S5H–S5I). To better compare dMSN and iMSN stimulation latencies (Freeze et al., 2013; Oldenburg and Sabatini, 2015) we analyzed trials in which 

the mouse was stationary prior to iMSN stimulation. Latencies to inhibition were markedly shorter relative to running trials (latency to inhibition, 276 ± 30 ms; Figure S5G) but still longer than 

Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 533 

**==> picture [60 x 60] intentionally omitted <==**

excitation during dMSN stimulation. Finally, in contrast to data obtained from identified glutamatergic neurons, unidentified MLR neurons displayed significantly more heterogeneous responses to stimulation of either pathway (Figures 6B and 6F), indicating that more complex circuit dynamics are controlling the activity of other neuronal subpopulations in the MLR. 

Given that MLR glutamatergic neurons are sufficient for locomotion, correlated with locomotion, and modulated by the BG, we next asked whether they are necessary for BG-driven locomotion. To investigate this, we expressed eNpHR3.0 in the MLR under the CaMKIIa promoter and ChR2 in dMSNs using a Cre-dependent virus injected into the striatum of D1-Cre mice (Figures 6D and S5E–S5F). Unilateral activation of dMSNs for 10 s elicited locomotion throughout the duration of the stimulation (Figure 6D). During interleaved trials, MLR glutamatergic neurons were optogenetically inhibited from 5–10 s after the onset of dMSN stimulation, which led to a striking decrease in running speed despite continued activation of dMSNs (Figure 6D). As a control, we looked at 1,000 time points when the mouse had been stationary for the same amount of time as ‘‘dMSN stim only’’ and ‘‘dMSN stim + MLR inhibition’’ trials and found that this similar baseline resulted in a spontaneous speed trajectory that did not resemble either stimulation condition. No change in locomotion was observed in trials without MLR inhibition or when light was delivered to MLR glutamatergic neurons expressing only YFP. Qualitatively similar results were observed in freely moving mice (Figure S6). 

We then tested whether inhibition of MLR neurons was necessary for locomotor suppression observed with iMSN stimulation. In these experiments, we expressed ChR2 in the MLR under the CaMKIIa promoter and ChR2 in iMSNs using a Cre-dependent virus injected into the striatum of A2a-Cre mice (Figures 6G and S5A–S5B). Bilateral activation of iMSNs for 10 s induced locomotor suppression throughout the duration of the stimulation (Figure 6H). This arrest was completely reversed by 20-Hz optical stimulation of MLR glutamatergic neurons delivered 5 s after the onset of the 10-s iMSN stimulation (Figure 6H). This reversal was not observed in eYFP controls. In addition, control trials with similar baselines but no stimulation of the iMSN or MLR glutamatergic neurons showed no changes in running speed. Taken together, these results demonstrate that bidirectional control of locomotion by basal ganglia circuitry requires modulation of MLR glutamatergic neurons. 

## DISCUSSION 

## Cell-Type-Specific Control of Locomotion by MLR Neurons 

Previous work has shown that the MLR has robust descending projections to the gigantocellular nucleus (Martinez-Gonzalez et al., 2014; Mitani et al., 1988; Rye et al., 1988), also referred to as the ventromedial medulla (Sherman et al., 2015; Skinner et al., 1990). In addition, MLR axons and terminals have been found in the pontine reticular formation (Takakusaki et al., 1996) and nucleus pontine oralis (Garcia-Rill et al., 2001). Collectively, these nuclei form the origin of reticulospinal tracts that project into the spinal cord and mediate various aspects of posture and movement. There may also be spinally projecting 

glutamatergic neurons within the boundaries of the MLR (Sherman et al., 2015). Indeed, lesions of the major non-spinal targets of the MLR do not reduce the gross aspects of locomotor function (Noga et al., 1988; Sherman et al., 2015), raising the possibility that the MLR acts as a comprehensive coordinator of locomotion. 

Our optogenetic dissection of MLR cell types revealed that only the glutamatergic population was sufficient to elicit running at short latencies, consistent with the classical definition of the MLR (Grillner et al., 2008; Ryczko and Dubuc, 2013; Shik et al., 1966b). This is in agreement with a recent study showing that cells targeted with a CaMKIIa-ChR2 virus in the MLR could elicit running (Lee et al., 2014) and consistent with current hypotheses about brainstem locomotor control (Grillner et al., 2005; Sherman et al., 2015). In spite of previous experiments that were unable to stop locomotion via pharmacologic inhibition or lesion of the MLR (Saper et al., 1979; Sinnamon et al., 1987), rapid optogenetic suppression of the MLR glutamatergic population revealed that these neurons are indeed necessary for locomotion. 

In contrast to glutamatergic neurons, the MLR GABAergic population caused cessation of locomotion. Although this population encoded both running and stationary states (Figure S4), the deceleration and stopping observed during stimulation could be in part due to local inhibition of the MLR glutamatergic population. However, inhibition of downstream targets is also a possibility. MLR GABA neurons received dense input from limbic centers (amygdala, periaqueductal gray [PAG] and BNST), suggesting that they could be involved in fear-related behavior. GABAergic neurons in neighboring regions have also been shown to suppress locomotion (Giber et al., 2015; Shang et al., 2015), suggesting that GABAergic cells at this level of the mesencephalon share similar functions. 

Finally, stimulation of the MLR cholinergic population demonstrated that, although these neurons can modulate locomotion, they are insufficient to initiate it with short latency. This population has been hypothesized previously to control locomotion (Skinner et al., 1990). PPTg cholinergic neurons send projections to the ventromedial medulla, depolarizing glutamatergic cells that, in turn, project to reticulospinal neurons (Brudzynski et al., 1988; Mamiya et al., 2005; Smetana et al., 2010). However, other work has shown that these neurons play a major role in gating the brain state as part of the ascending reticular activating system (Mena-Segovia et al., 2008; Van Dort et al., 2015). Because locomotion and brain state are clearly linked (Lee et al., 2014; Niell and Stryker, 2010), the time course of behavioral changes is critical to consider. 

## Non-canonical Projections from the BG and Other Nuclei 

The BG interface strongly with the MLR, making reciprocal connections from most of its nuclei (Martinez-Gonzalez et al., 2011; Mena-Segovia et al., 2004). Our rabies tracing showed that it is the glutamatergic population—and not the GABAergic population—that is the primary target of these BG connections. In addition, our tracing highlighted a number of non-canonical pathways to the MLR from the BG (entopeduncular nucleus [EP], external globus pallidus [GPe], subthalamic nucleus [STN]) to MLR glutamatergic neurons. The STN projection is of interest because it is predicted to arrive in the MLR prior to the classical 

534 Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

indirect pathway signal through the SNr, and it should drive activity in the opposite direction. Indeed, a small minority of cells displayed a small uptick in firing rate prior to inhibition (Figure 6F), consistent with the idea that this pathway modulates MLR activity, perhaps as a brief arousal signal prior to suppression of locomotion. 

Striatal neurons also send projections directly to MLR glutamate neurons. Interestingly, the PPTg, one of the MLR nuclei, also sends projections back to the striatum (Wall et al., 2013) thus forming a reciprocal connection. As iMSNs do not project past the GPe, it is most likely the dMSN population that sends axons to the MLR. As this connection is GABAergic, these cells may form synapses onto the small number of glutamatergic neurons that fire most during the stationary state. dMSNs in the DMS could therefore coordinate the initiation of locomotion by directly inhibiting these cells. 

## Comparison with Other BG Targets 

The BG output nuclei also project to the thalamus and superior colliculus (SC) (Bosch-Bouju et al., 2013; Hikosaka et al., 2000), enabling broad control of cortical and brainstem circuitry. Recent work has shown that direct and indirect pathway stimulation increases and decreases firing rates in the motor cortex, respectively, along with increasing and decreasing lever press frequency in an operant task (Oldenburg and Sabatini, 2015). However, the principles underlying BG control of the thalamus and cortex remain largely mysterious (Bosch-Bouju et al., 2013; Goldberg et al., 2013). In contrast, BG have long been proposed to act as a ‘‘gate’’ for motor behaviors originating from the SC, such as turning and saccades (Girard and Berthoz, 2005; Hikosaka et al., 2000), because the SNr is known to exert tonic inhibitory control over the SC (Chevalier et al., 1984). To initiate an orienting movement, SNr inhibition to the contralateral SC is released, allowing input from the cortex to excite SC neurons, which, in turn, drive the action (Hikosaka and Wurtz, 1983). The SC is topographically organized by the visual field (Schiller and Stryker, 1972), as are SNr inputs (Hikosaka and Wurtz, 1983). Because of this association, BG have been hypothesized to play a role in deciding important targets for orienting (Hikosaka et al., 2006). Between this SC-mediated orienting and MLRmediated running, these brainstem BG targets are fully capable of defining locomotor trajectories, consistent with decortication studies (Bjursten et al., 1976). In addition, our rabies result demonstrates that the SC connects directly with the MLR, consistent with previous studies (Martinez-Gonzalez et al., 2011; Perkins et al., 2014; Redgrave et al., 1987), providing another connection through which BG-brainstem connections could exert navigational control. 

## BG Pathway-Specific Selection and Suppression of Action 

Our cell-type-specific recordings from the MLR during iMSN and dMSN stimulation reveal a remarkable degree of homogeneity in the glutamatergic population response. The majority of responses preceded changes in locomotion, suggesting that they were causally related to behavior. In support of this, inhibition of the glutamatergic population during dMSN-induced locomotion caused the mouse to stop running. Although the functional re- 

sponses observed in the SNr in response to striatal stimulation are complex (Freeze et al., 2013), the signal becomes surprisingly uniform at the level of the MLR glutamatergic population. Together with the rabies results, this indicates a highly specific connection between BG and locomotor-encoding MLR neurons. 

Given its ability to drive a robust behavioral output, the MLR represents an ideal system for understanding the BG role in action selection. Classical models of BG suggest that movement occurs when the direct pathway is active and cessation of movement occurs with indirect pathway activation. However, both pathways appear to be co-active during normal movement (Cui et al., 2013). One possibility is that different information is encoded in the direct and indirect pathway circuits, which, together, form the basis for action selection. For example, indirect pathway activity could encode information about competing behavioral choices. Our data suggest that the balance of activity between the direct and indirect pathways is represented in the firing rate of glutamatergic MLR neurons, which is predictive of the initiation of running and sufficient to drive graded locomotion. Further experiments can help clarify the validity of this model for the MLR and other BG output structures. 

## EXPERIMENTAL PROCEDURES 

## Subjects 

86 adult transgenic or wild-type mice on a C57BL/6 background aged 50–100 days were used in the experiments. vGLUT2-Cre (The Jackson Laboratory, stock no. 016963), vGAT-Cre (The Jackson Laboratory, stock no. 016962), ChAT-ChR2 (The Jackson Laboratory, stock no. 014546), and wildtype C57BL/6 (The Jackson Laboratory, stock no. 000664) mice were used for optogenetic stimulation, inhibition, or recording experiments. vGLUT2Cre and vGAT-Cre mice were used for rabies tracing experiments. D1-Cre mice (GENSAT, catalog no. 030778-UCD) were used for dMSN stimulation while recording responses from identified glutamatergic neurons or inhibiting the MLR. A2a-Cre mice (GENSAT, catalog no. 031168-UCD) were used for iMSN stimulation while recording identified responses from identified glutamatergic neurons or stimulating the MLR. vGLUT2-Cre mice crossed into an Ai14 line (The Jackson Laboratory, stock no. 007914) were used for confirmation of CAMKIIa expression in vGLUT2-expressing neurons. All procedures were in accordance with protocols approved by the University of California, San Francisco Institutional Animal Care and Use Committee. 

## Surgery 

For dMSN or iMSN activation, AAV5-EF1a-DIO-ChR2-eYFP (University of Pennsylvania) was injected into the dorsomedial striatum at (0.8 mm anterior/posterior axis [AP]/�2.5 dorsal/ventral axis [DV]/± 1.5 medial/lateral axis [ML]) measured from the bregma. For activation of cells in the MLR, AAV5EF1a-DIO-ChR2-eYFP or AAV5-CAMKIIa- ChR2-eYFP (for glutamatergic neurons) was injected at (�0.8 mm AP/�3.6 DV/± 1.2 ML), measured from the lambda. Where appropriate, fiberoptic ferrules were implanted 0.5 mm above the injection sites. The virus was allowed to express for 2–6 weeks, after which the mice were implanted with a custom-built stainless steel headbar for head fixation. 7–10 days later, the mice were habituated to the trackball until able to run normally, at which point recordings took place. 

## Recording and Optogenetics 

Extracellular recordings were performed using a Plexon data acquisition system (Plexon). A blue laser (473 nm, 100 mW, OEM) was triggered through a transistor-transistor logic [TTL] pulse generator (PulseBlaster, SpinCore Technologies). Trackball velocity was monitored via two optical handheld pointing devices (computer mice) that were connected to the recording computer. 

Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 535 

**==> picture [60 x 60] intentionally omitted <==**

Custom MATLAB (MathWorks) data acquisition software was used to transform optical mouse data packets into speed and time data. 

## Data Analyses 

Data analyses were carried out using built-in (NeuroExplorer, Plexon) and custom-built software in MATLAB (MathWorks). Single units were sorted into clusters using commercially available software (Plexon Offline Sorter 2.4, Plexon). See the Supplemental Experimental Procedures for further details. 

## SUPPLEMENTAL INFORMATION 

Supplemental Information includes Supplemental Experimental Procedures and six figures and can be found with this article online at http://dx.doi.org/ 10.1016/j.cell.2015.12.037. 

## AUTHOR CONTRIBUTIONS 

A.M.L. conceptualized and initiated the project in the laboratory of A.B., continued the project in the laboratory of L.W., and brought the project to the laboratory of A.C.K., where he conducted experiments together with T.K.R. and co-wrote the manuscript. T.K.R. performed experiments, analyzed all data, and co-wrote the manuscript. A.L.L. performed slice electrophysiology recordings. A.C.K. designed experiments, supervised the project, and co-wrote the manuscript. 

## ACKNOWLEDGMENTS 

We thank Delanie Schulte for assistance with genotyping, histology, and microscopy and the A.C.K. laboratory for comments on the manuscript. This work was funded by NIH R01 NS064984 and P01 DA010154 (to A.C.K.), F31 NS092253 (to T.K.R.), 5T32GM007618-38 (to A.M.L.), RR018928 (to the Gladstone Institutes), a grant from the Swiss National Science Foundation (to A.L.L.), funds from the State of California (to L.W.), and an NIDA intramural program (to A.B.). 

Received: September 9, 2015 Revised: October 27, 2015 Accepted: December 22, 2015 Published: January 28, 2016 

## REFERENCES 

Albin, R.L., Young, A.B., and Penney, J.B. (1989). The functional anatomy of basal ganglia disorders. Trends Neurosci. 12, 366–375. 

Bateup, H.S., Santini, E., Shen, W., Birnbaum, S., Valjent, E., Surmeier, D.J., Fisone, G., Nestler, E.J., and Greengard, P. (2010). Distinct subclasses of medium spiny neurons differentially regulate striatal motor behaviors. Proc. Natl. Acad. Sci. USA 107, 14845–14850. 

Bedford, T.G., Loi, P.K., and Crandall, C.C. (1992). A model of dynamic exercise: the decerebrate rat locomotor preparation. J. Appl. Physiol. 72, 121–127. Bjursten, L.M., Norrsell, K., and Norrsell, U. (1976). Behavioural repertory of cats without cerebral cortex from infancy. Exp. Brain Res. 25, 115–130. 

Borgius, L., Restrepo, C.E., Leao, R.N., Saleh, N., and Kiehn, O. (2010). A transgenic mouse line for molecular genetic analysis of excitatory glutamatergic neurons. Mol. Cell. Neurosci. 45, 245–257. 

Bosch-Bouju, C., Hyland, B.I., and Parr-Brownlie, L.C. (2013). Motor thalamus integration of cortical, cerebellar and basal ganglia information: implications for normal and parkinsonian conditions. Front. Comput. Neurosci. 7, 163. 

Brudzynski, S.M., Wu, M., and Mogenson, G.J. (1988). Modulation of locomotor activity induced by injections of carbachol into the tegmental pedunculopontine nucleus and adjacent areas in the rat. Brain Res. 451, 119–125. 

Chevalier, G., Vacher, S., and Deniau, J.M. (1984). Inhibitory nigral influence on tectospinal neurons, a possible implication of basal ganglia in orienting behavior. Exp. Brain Res. 53, 320–326. 

Cui, G., Jun, S.B., Jin, X., Pham, M.D., Vogel, S.S., Lovinger, D.M., and Costa, R.M. (2013). Concurrent activation of striatal direct and indirect pathways during action initiation. Nature 494, 238–242. 

DeLong, M.R. (1990). Primate models of movement disorders of basal ganglia origin. Trends Neurosci. 13, 281–285. 

Ehrich, J.M., Phillips, P.E., and Chavkin, C. (2014). Kappa opioid receptor activation potentiates the cocaine-induced increase in evoked dopamine release recorded in vivo in the mouse nucleus accumbens. Neuropsychopharmacology 39, 3036–3048. 

Freeze, B.S., Kravitz, A.V., Hammack, N., Berke, J.D., and Kreitzer, A.C. (2013). Control of basal ganglia output by direct and indirect pathway projection neurons. J. Neurosci. 33, 18531–18539. 

Garcia-Rill, E. (1986). The basal ganglia and the locomotor regions. Brain Res. 396, 47–63. 

Garcia-Rill, E., Skinner, R.D., Conrad, C., Mosley, D., and Campbell, C. (1986). Projections of the mesencephalic locomotor region in the rat. Brain Res. Bull. 17, 33–40. 

Garcia-Rill, E., Skinner, R.D., Miyazato, H., and Homma, Y. (2001). Pedunculopontine stimulation induces prolonged activation of pontine reticular neurons. Neuroscience 104, 455–465. 

Giber, K., Diana, M.A., Plattner, V.M., Dugue´ , G.P., Bokor, H., Rousseau, C.V., Maglo´ czky, Z., Havas, L., Hangya, B., Wildner, H., et al. (2015). A subcortical inhibitory signal for behavioral arrest in the thalamus. Nat. Neurosci. 18, 562–568. 

Girard, B., and Berthoz, A. (2005). From brainstem to cortex: computational models of saccade generation circuitry. Prog. Neurobiol. 77, 215–251. 

Goldberg, J.H., Farries, M.A., and Fee, M.S. (2013). Basal ganglia output to the thalamus: still a paradox. Trends Neurosci. 36, 695–705. 

Grace, A.A. (2010). Dopamine system dysregulation by the ventral subiculum as the common pathophysiological basis for schizophrenia psychosis, psychostimulant abuse, and stress. Neurotox. Res. 18, 367–376. 

Grillner, S., Hellgren, J., Me´ nard, A., Saitoh, K., and Wikstro¨ m, M.A. (2005). Mechanisms for selection of basic motor programs–roles for the striatum and pallidum. Trends Neurosci. 28, 364–370. 

Grillner, S., Walle´ n, P., Saitoh, K., Kozlov, A., and Robertson, B. (2008). Neural bases of goal-directed locomotion in vertebrates–an overview. Brain Res. Brain Res. Rev. 57, 2–12. 

Hikosaka, O., and Wurtz, R.H. (1983). Visual and oculomotor functions of monkey substantia nigra pars reticulata. IV. Relation of substantia nigra to superior colliculus. J. Neurophysiol. 49, 1285–1301. 

Hikosaka, O., Takikawa, Y., and Kawagoe, R. (2000). Role of the basal ganglia in the control of purposive saccadic eye movements. Physiol. Rev. 80, 953–978. 

Hikosaka, O., Nakamura, K., and Nakahara, H. (2006). Basal ganglia orient eyes to reward. J. Neurophysiol. 95, 567–584. 

Kravitz, A.V., Freeze, B.S., Parker, P.R., Kay, K., Thwin, M.T., Deisseroth, K., and Kreitzer, A.C. (2010). Regulation of parkinsonian motor behaviours by optogenetic control of basal ganglia circuitry. Nature 466, 622–626. 

Kreitzer, A.C., and Malenka, R.C. (2008). Striatal plasticity and basal ganglia circuit function. Neuron 60, 543–554. 

LeDoux, J.E. (2000). Emotion circuits in the brain. Annu. Rev. Neurosci. 23, 155–184. 

Lee, A.M., Hoy, J.L., Bonci, A., Wilbrecht, L., Stryker, M.P., and Niell, C.M. (2014). Identification of a brainstem circuit regulating visual cortical state in parallel with locomotion. Neuron 83, 455–466. 

Mamiya, K., Bay, K., Skinner, R.D., and Garcia-Rill, E. (2005). Induction of longlasting depolarization in medioventral medulla neurons by cholinergic input from the pedunculopontine nucleus. J. Appl. Physiol. 99, 1127–1137. 

Martinez-Gonzalez, C., Bolam, J.P., and Mena-Segovia, J. (2011). Topographical organization of the pedunculopontine nucleus. Front. Neuroanat. 5, 22. 

536 Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

Martinez-Gonzalez, C., van Andel, J., Bolam, J.P., and Mena-Segovia, J. (2014). Divergent motor projections from the pedunculopontine nucleus are differentially regulated in Parkinsonism. Brain Struct. Funct. 219, 1451–1462. 

Mena-Segovia, J., Bolam, J.P., and Magill, P.J. (2004). Pedunculopontine nucleus and basal ganglia: distant relatives or part of the same family? Trends Neurosci. 27, 585–588. 

Mena-Segovia, J., Sims, H.M., Magill, P.J., and Bolam, J.P. (2008). Cholinergic brainstem neurons modulate cortical gamma activity during slow oscillations. J. Physiol. 586, 2947–2960. 

Mitani, A., Ito, K., Hallanger, A.E., Wainer, B.H., Kataoka, K., and McCarley, R.W. (1988). Cholinergic projections from the laterodorsal and pedunculopontine tegmental nuclei to the pontine gigantocellular tegmental field in the cat. Brain Res. 451, 397–402. 

Niell, C.M., and Stryker, M.P. (2010). Modulation of visual responses by behavioral state in mouse visual cortex. Neuron 65, 472–479. 

Noga, B.R., Kettler, J., and Jordan, L.M. (1988). Locomotion produced in mesencephalic cats by injections of putative transmitter substances and antagonists into the medial reticular formation and the pontomedullary locomotor strip. J. Neurosci. 8, 2074–2086. 

Norton, A.B., Jo, Y.S., Clark, E.W., Taylor, C.A., and Mizumori, S.J. (2011). Independent neural coding of reward and movement by pedunculopontine tegmental nucleus neurons in freely navigating rats. Eur. J. Neurosci. 33, 1885–1896. 

Oldenburg, I.A., and Sabatini, B.L. (2015). Antagonistic but Not Symmetric Regulation of Primary Motor Cortex by Basal Ganglia Direct and Indirect Pathways. Neuron 86, 1174–1181. 

Orlovsky, G.N., Deliagina, T., and Grillner, S. (1999). Neuronal Control of Locomotion: From Mollusc to Man. (Oxford University Press). 

Perkins, E., May, P.J., and Warren, S. (2014). Feed-forward and feedback projections of midbrain reticular formation neurons in the cat. Front. Neuroanat. 7, 55. 

Redgrave, P., Mitchell, I.J., and Dean, P. (1987). Descending projections from the superior colliculus in rat: a study using orthograde transport of wheatgermagglutinin conjugated horseradish peroxidase. Exp. Brain Res. 68, 147–167. 

Ryczko, D., and Dubuc, R. (2013). The multifunctional mesencephalic locomotor region. Curr. Pharm. Des. 19, 4448–4470. 

Rye, D.B., Lee, H.J., Saper, C.B., and Wainer, B.H. (1988). Medullary and spinal efferents of the pedunculopontine tegmental nucleus and adjacent mesopontine tegmentum in the rat. J. Comp. Neurol. 269, 315–341. 

Saper, C.B., Swanson, L.W., and Cowan, W.M. (1979). An autoradiographic study of the efferent connections of the lateral hypothalamic area in the rat. J. Comp. Neurol. 183, 689–706. 

Schiller, P.H., and Stryker, M. (1972). Single-unit recording and stimulation in superior colliculus of the alert rhesus monkey. J. Neurophysiol. 35, 915–924. 

Shang, C., Liu, Z., Chen, Z., Shi, Y., Wang, Q., Liu, S., Li, D., and Cao, P. (2015). BRAIN CIRCUITS. A parvalbumin-positive excitatory visual pathway to trigger fear responses in mice. Science 348, 1472–1477. 

Sherman, D., Fuller, P.M., Marcus, J., Yu, J., Zhang, P., Chamberlin, N.L., Saper, C.B., and Lu, J. (2015). Anatomical Location of the Mesencephalic Locomotor Region and Its Possible Role in Locomotion, Posture, Cataplexy, and Parkinsonism. Front. Neurol. 6, 140. 

Shik, M.L., Orlovskiĭ, G.N., and Severin, F.V. (1966a). [Organization of locomotor synergism]. Biofizika 11, 879–886. 

Shik, M.L., Severin, F.V., and Orlovskiĭ, G.N. (1966b). [Control of walking and running by means of electric stimulation of the midbrain]. Biofizika 11, 659–666. 

Sinnamon, H.M., Ginzburg, R.N., and Kurose, G.A. (1987). Midbrain stimulation in the anesthetized rat: direct locomotor effects and modulation of locomotion produced by hypothalamic stimulation. Neuroscience 20, 695–707. 

Skinner, R.D., Kinjo, N., Ishikawa, Y., Biedermann, J.A., and Garcia-Rill, E. (1990). Locomotor projections from the pedunculopontine nucleus to the medioventral medulla. Neuroreport 1, 207–210. 

Smetana, R., Juvin, L., Dubuc, R., and Alford, S. (2010). A parallel cholinergic brainstem pathway for enhancing locomotor drive. Nat. Neurosci. 13, 731–738. 

Takakusaki, K., Shiroyama, T., Yamamoto, T., and Kitai, S.T. (1996). Cholinergic and noncholinergic tegmental pedunculopontine projection neurons in rats revealed by intracellular labeling. J. Comp. Neurol. 371, 345–361. 

Thankachan, S., Fuller, P.M., and Lu, J. (2012). Movement- and behavioral state-dependent activity of pontine reticulospinal neurons. Neuroscience 221, 125–139. 

Thompson, J.A., and Felsen, G. (2013). Activity in mouse pedunculopontine tegmental nucleus reflects action and outcome in a decision-making task. J. Neurophysiol. 110, 2817–2829. 

Van Dort, C.J., Zachs, D.P., Kenny, J.D., Zheng, S., Goldblum, R.R., Gelwan, N.A., Ramos, D.M., Nolan, M.A., Wang, K., Weng, F.J., et al. (2015). Optogenetic activation of cholinergic neurons in the PPT or LDT induces REM sleep. Proc. Natl. Acad. Sci. USA 112, 584–589. 

Wall, N.R., De La Parra, M., Callaway, E.M., and Kreitzer, A.C. (2013). Differential innervation of direct- and indirect-pathway striatal projection neurons. Neuron 79, 347–360. 

Whelan, P.J. (1996). Control of locomotion in the decerebrate cat. Prog. Neurobiol. 49, 481–515. 

Zhao, S., Ting, J.T., Atallah, H.E., Qiu, L., Tan, J., Gloss, B., Augustine, G.J., Deisseroth, K., Luo, M., Graybiel, A.M., and Feng, G. (2011). Cell type–specific channelrhodopsin-2 transgenic mice for optogenetic dissection of neural circuitry function. Nat. Methods 8, 745–752. 

Cell 164, 526–537, January 28, 2016 ª2016 Elsevier Inc. 537 

