RESEARCH ADVANCE 

**==> picture [101 x 41] intentionally omitted <==**

## Phase-tuned neuronal firing encodes human contextual representations for navigational goals 

## Andrew J Watrous[1,2,3] *, Jonathan Miller[1] , Salman E Qasim[1] , Itzhak Fried[4,5,6,7] , Joshua Jacobs[1] * 

> 1Department of Biomedical Engineering, Columbia University, New York, United States;[2] Department of Neurology, Dell Medical School, University of Texas at Austin, Austin, Texas, United States;[3] Seton Brain and Spine Institute, Austin, Texas, United States;[4] Department of Neurosurgery, David Geffen School of Medicine, University of California, Los Angeles, Los Angeles, United States;[5] Semel Institute for Neuroscience and Human Behavior, University of California, Los Angeles, Los Angeles, United States;[6] Sackler Faculty of Medicine, Tel-Aviv University, Tel-Aviv, Israel;[7] Department of Neurosurgery, Tel-Aviv Medical Center, Tel-Aviv, Israel 

*For correspondence: andrew.j.watrous@gmail.com (AJW); joshua.jacobs@columbia.edu (JJ) 

Competing interests: The authors declare that no competing interests exist. 

Funding: See page 12 

Received: 12 October 2017 Accepted: 21 June 2018 Published: 22 June 2018 

Reviewing editor: Timothy E Behrens, University of Oxford, United Kingdom 

Copyright Watrous et al. This article is distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use and redistribution provided that the original author and source are credited. 

Abstract We previously demonstrated that the phase of oscillations modulates neural activity representing categorical information using human intracranial recordings and high-frequency activity from local field potentials (Watrous et al., 2015b). We extend these findings here using human single-neuron recordings during a virtual navigation task. We identify neurons in the medial temporal lobe with firing-rate modulations for specific navigational goals, as well as for navigational planning and goal arrival. Going beyond this work, using a novel oscillation detection algorithm, we identify phase-locked neural firing that encodes information about a person’s prospective navigational goal in the absence of firing rate changes. These results provide evidence for navigational planning and contextual accounts of human MTL function at the single-neuron level. More generally, our findings identify phase-coded neuronal firing as a component of the human neural code. DOI: https://doi.org/10.7554/eLife.32554.001 

## Introduction 

Single-neuron firing forms a fundamental basis of the neural code during perception and memory. In addition to the well-established role for behavior-related changes in neuronal firing rates, converging evidence across species and behaviors suggests that interactions between single-neuron spike timing and oscillations observed in the local field potential (LFP) also contribute to the neural code (Hyman et al., 2005; Huxter et al., 2003; Rutishauser et al., 2010; Belitski et al., 2008; Ng et al., 2013; Kayser et al., 2009). In rodents, hippocampal and medial prefrontal cells show phase precession relative to theta oscillations during navigation (O’Keefe and Recce, 1993; Terada et al., 2017; Jones and Wilson, 2005), in which the theta phase of neuronal firing represents information about the animal’s position (Jensen and Lisman, 2000). 

These observations have been incorporated into theoretical models of neural coding that hypothesize a general role for oscillatory phase for coding various types of behavioral information (Nadasdy, 2009; Kayser et al., 2012; Lisman and Jensen, 2013; Watrous and Ekstrom, 2014). For example, in Spectro-Contextual Encoding and Retrieval Theory (SCERT), we proposed that frequency-specific and phase-locked neuronal firing to low-frequency oscillations at different phases (i.e. phase coding) also forms a basis of the human neural code (Watrous and Ekstrom, 2014; 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

1 of 16 

Research advance 

Neuroscience 

Watrous et al., 2015b). We previously reported evidence for SCERT (Watrous et al., 2015a) using high-frequency activity in the LFP as a proxy for single-cell spiking (Crone et al., 1998; Manning et al., 2009; Miller et al., 2014). However, given the complex and variable relationship (Ekstrom et al., 2007; Manning et al., 2009; Rey et al., 2014) between the spiking of particular single neurons and high-frequency activity in the human medial temporal lobe (MTL), it is unclear whether human MTL neurons show phase coding of navigationally relevant information beyond an overall preference to fire at particular phases (Jacobs et al., 2007). We thus sought to extend our previous findings of LFP phase coding (Watrous et al., 2015a) to the single-neuron level in patients performing a virtual navigation task, hypothesizing that phase coding would occur to low-frequency oscillations based on both human studies (Jacobs et al., 2010; Watrous et al., 2011; Ekstrom et al., 2005; Mormann et al., 2008) and the above-described rodent work. 

An optimal navigator must both plan routes and recognize when they have arrived at their destination. Human imaging and lesion evidence indicate that activity in the human MTL and medial prefrontal cortex forms active representations of spatial context such as navigational goals (Ranganath and Ritchey, 2012; Brown et al., 2016; Ciaramelli, 2008; Spiers and Maguire, 2007; Wolbers et al., 2007) in support of navigational planning (Horner et al., 2016; Bellmund et al., 2016; Kaplan et al., 2017). Analyzing human single-neuron recordings from the MTL, previous studies have identified neurons that increase their firing rate when viewing goal locations (Ekstrom et al., 2003). To date, it is unclear whether phase-coding also exists for navigational goals. It is also unknown whether rate and phase-coding co-exist in humans, as suggested by rodent studies that indicated that phase coding was a distinct phenomenon compared to rate coding (Huxter et al., 2003; Hyman et al., 2005). Drawing upon the phase-coding hypotheses from SCERT and related findings in rodents (Hollup et al., 2001; Hok et al., 2007; Hyman et al., 2005; O’Neill et al., 2013), we hypothesized that spatial contextual representations for specific navigational goals would be implemented by distinctive patterns of phase coding by individual neurons. Moreover, based on rodent (Wikenheiser and Redish, 2015) and human studies (Viard et al., 2011; Howard et al., 2014; Brown et al., 2016; Horner et al., 2016; Bellmund et al., 2016) implicating medial temporal lobe structures and frontal cortex in navigational planning, we reasoned that spike-phase coding may support these behaviors at the single-neuron level, hypothesizing that distinctive spike phase patterns would correspond to the neural network states representing planning and searching for particular goals. SCERT generally predicts that oscillatory frequencies should match between encoding and retrieval and that phase coding should occur at the dominant oscillatory frequency that occurs in a particular behavior and brain region. Thus, based on the body of evidence indicating hippocampal slow-theta oscillations are the most prominent during human virtual navigation (Ekstrom et al., 2005; Watrous et al., 2011; Jacobs, 2014; Bush et al., 2017), we predicted here that phase coding should occur primarily at slow theta frequencies. 

To test these ideas, we analyzed a dataset that simultaneously measured human single-neuron and oscillatory activity from MTL (hippocampus, entorhinal cortex, amygdala, and parahippocampal gyrus) and frontal (medial prefrontal/cingulate, motor, orbitofrontal) regions during a goal-directed navigation task (Figure 1—figure supplement 1; Jacobs et al., 2010; Miller et al., 2015). After first assessing changes in firing rate related to goal activity, we then asked if additional goal-related information is encoded by considering oscillatory phase during spiking. Following the analytic strategy from our previous work (Watrous et al., 2015a), we tested for frequency-specific phase locking and then directly tested for phase coding, which would appear as individual neurons that spiked at different phases according to the prospective goal. In addition to cells that encode navigational variables using firing rate, our results confirmed the existence of phase coding for navigational goals in individual neurons, thus providing the first evidence for the oscillatory phase coding of spatial contextual information in the human brain. 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

2 of 16 

Research advance 

Neuroscience 

## Results 

## Behavior and neuronal firing during goal-directed navigational planning and arrival 

Patients performed a goal-directed navigation task in which they moved throughout a circular environment delivering passengers to one of six goal locations located on the outer edge of the environment (see Jacobs et al., 2010 for details). Upon arriving at a goal store, the patient paused and then was instructed to navigate to a new goal store. On each trial, patients thus had to make a navigation plan about which direction of movement in the environment would lead them most directly to the location of their goal. Driving time between stores significantly decreased throughout the task session (Kruskal-Wallis test across sessions, p=0.007), indicating that the patients successfully learned the environment and planned efficient paths between stores. 

Previous work in humans has identified single neurons responsive to navigational goals (Ekstrom et al., 2003) and imaging work suggests that the MTL is involved in navigational planning ( Bellmund et al., 2016; Horner et al., 2016; Brown et al., 2016). We investigated the single-neuron correlates of these phenomena in our task. We assessed neuronal firing rate as a function of the identity of the navigational goal and of different task periods using a two-way ANOVA, with factors for goal and task period (‘planning’ vs. ‘arriving’, see Materials and methods). Figure 1A shows an example entorhinal neuron who’s firing significantly increased during deliveries to goal store 3 (main effect of goal, p<0.0001). We identified 53 such goal-responsive cells (11% of 466 MTL neurons; main effect of goal, p<0.05), which were present in 11 of 12 patients. We observed significant counts of goal-responsive neurons in the hippocampus, entorhinal cortex, orbitofrontal cortex, and premotor cortex (Figure 1B; Binomial tests, p’s < 0.05). 

We also identified cells that showed significantly enhanced firing during either the navigational planning or the arrival period of each trial (main effect of task period, p<0.05). Figure 1C shows an example hippocampal neuron whose firing rate significantly increased during navigational planning compared to goal arrival (main effect of task period, two-way ANOVA, p<0.0001, followed by posthoc analysis). We observed significant counts of navigational planning neurons in the hippocampus of 9 of 12 patients and in all areas except the amygdala (Figure 1E; Binomial test, p<0.05). Furthermore, we observed modulation of firing rate by arrival at goals in parahippocampal and motor areas (Figure 1D–E). We found 24 cells with significant interactions between goal and task period (p<0.05). These results provide single-neuron evidence that the MTL encodes information about navigational goals, and supports navigational planning towards reaching these goals, using modulations in firing rate, extending previous findings (Ekstrom et al., 2003; Watrous et al., 2011; Brown et al., 2016). 

## Slow theta oscillations (3 Hz) in the MTL during virtual navigation 

Our primary hypothesis was that human MTL neurons encode behavioral information by modulating their spiking based on the phase of slow oscillations beyond changes in firing rate. Examining this hypothesis required that we accurately identify the presence and phase of slow oscillations, particularly because human MTL oscillations are lower frequency and less stationary compared to the stable theta oscillations observed in rodents (Watrous et al., 2013; Vass et al., 2016). We developed and benchmarked a novel method, the Multiple Oscillations Detection Algorithm (‘MODAL’; Figure 2A– C), to detect and characterize neural oscillations in adaptively identified band(s) whose frequency ranges are customized for each recording site according to its spectral properties. MODAL identifies narrow-band oscillations exceeding the background 1/f spectrum (Figure 2A) and calculates the instantaneous phase and frequency of oscillations in each band (see Materials and methods) while excluding time points without oscillations or that exhibited epileptogenic activity (Gelinas et al., 2016). Thus, MODAL allowed us to test for phase coding of spikes during the presence of narrowband oscillations in our dataset. 

MODAL reliably identified oscillations at multiple frequencies that were visible in the raw trace (Figure 2B–C). Analyzing each of 385 LFP channels from the MTL across the entire task period using MODAL, we found that most channels showed a band of activity centered at ‘slow theta’ ( `~` 3 Hz; 93% of electrodes; Figure 2D, gray line). Analyzing the overall amount of time each frequency was detected on these electrodes, we found that slow theta was detected most often (Figure 2D, black 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

3 of 16 

Research advance 

Neuroscience 

**==> picture [515 x 460] intentionally omitted <==**

Figure 1. Firing rate modulations by navigational goal and task phase. (A) Neuron from the entorhinal cortex of patient four whose firing rate was significantly goal-modulated when delivering to goal 3 (p<0.001). Firing rate is plotted as a function of each navigational goal (error bars indicate s.e. m.). (B) Proportion of goal-responsive neurons in each brain area. Asterisk indicates significant counts using binomial test. (C) Example neuron from the hippocampus of patient 12 whose firing rate was modulated during goal planning (p<0.0001). (D) Example neuron from the parahippocampal gyrus of patient eight whose firing rate was modulated during goal arrival (p=0.0002). (E) Proportion of task-responsive neurons in each brain area, shown separately for planning and arrival. See methods for region acronyms. 

DOI: https://doi.org/10.7554/eLife.32554.002 

The following figure supplement is available for figure 1: 

Figure supplement 1. Task and recording methods. DOI: https://doi.org/10.7554/eLife.32554.003 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

4 of 16 

Research advance 

Neuroscience 

**==> picture [514 x 184] intentionally omitted <==**

Figure 2. Multiple Oscillation Detection Algorithm (‘MODAL’). (A-C) Key steps in the algorithm, shown for an example electrode from the right hippocampus of patient 9. (A) Mean log power averaged over time (black) and a fit line of the 1/f background spectrum (gray). A slow theta band (blue) and a beta band (green) are identified as contiguous frequencies exceeding the fit line. (B) Example output from MODAL depicting a raw trace example of the LFP (upper) with the detected oscillations in each band (lower). The instantaneous frequency of the detected oscillation in each band is overlaid on a spectrogram and gray portions of the spectrogram indicate power values exceeding a local fit (similar to A but using a 10 s epoch). (C) Accumulating detections over time reveals the prevalence of oscillations at each frequency on this electrode (black). Blue and green bars indicate the overall prevalence of oscillations in each frequency, independent of the exact frequency within a band. (D) Population data for MTL channels demonstrating low frequency oscillations. Grey line indicates the percent of LFP channels with a detected band as a function of frequency. Of those channels with a detected band, the black line indicates the average amount of time each frequency was detected. Slow theta oscillations (below 5 Hz) are observed using both metrics. 

DOI: https://doi.org/10.7554/eLife.32554.004 

The following figure supplements are available for figure 2: 

Figure supplement 1. Proportion of channels with oscillations detected using MODAL in each brain region. DOI: https://doi.org/10.7554/eLife.32554.005 

Figure supplement 2. Analysis of rodent CA1 and medial prefrontal cortex LFPs using MODAL. DOI: https://doi.org/10.7554/eLife.32554.006 

line). Similar results were identified in different brain areas (Figure 2—figure supplement 1). We then verified that MODAL can capture multiple narrowband oscillatory signals using a published rodent recording dataset (Fujisawa et al., 2008; crcns.org PFC-2 dataset), and observed canonical rodent hippocampal CA1 theta oscillations and a more variable low-frequency rhythm in the medial prefrontal cortex (Figure 2—figure supplement 2). These results indicate that MODAL is able to identify and track the dynamics of narrowband signals, providing cross-validation for our human findings which are consistent with previous work showing the prevalence of slow theta in the human MTL (Watrous et al., 2011, 2013; Vass et al., 2016; Jacobs, 2014; Bohbot et al., 2017). We subsequently restricted our analysis of phase coding to this low-frequency band (1–10 Hz) because it was most prominently detected by MODAL and because activity in this band has been shown to modulate human single-neuron firing (Jacobs et al., 2007). 

## Slow theta phase modulates neuronal firing 

As a precursor to testing for phase coding, we asked if phase coordinated the activity of individual neurons across the entire task session in the bands identified by MODAL. Focusing first on the MTL, we analyzed 466 neurons that each had a simultaneously recorded LFP with an oscillation in a lowfrequency band (1–10 Hz). In many cells we observed significant phase-locking, an overall tendency for firing to increase at particular phases of the LFP oscillation (Jacobs et al., 2007; Rey et al., 2014). Phase locking is evident by examining the LFP phase distribution for all spikes that occurred during oscillations from a given cell (Figure 3A upper panel, Rayleigh p<0.005). Across our 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

5 of 16 

Research advance 

Neuroscience 

**==> picture [514 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
A. π/2 B. C. D.<br>Cells with phase-locking<br>1.5-5Hz Cells with oscillations<br>Trough Peak<br>-π/2<br>Rayleigh<br>1 sec p<.00001<br>7.5-9Hz<br>**----- End of picture text -----**<br>


Figure 3. Phase-Locked Neural Firing to low-frequency oscillations. (A) Spike-triggered average of a phase-locked neuron from the right hippocampus of Patient 1 (left). Red tick mark denotes a spike. Circular histograms (right) show phases at which spikes occurred relative to two detected bands. Spiking was phase-locked to the ascending phase in the 1.5–5 Hz band (red) but not in the 7.5–9 Hz band (Rayleigh test, p=0.004 and p=0.34, respectively). (B) MTL Population data: Pooling over frequencies, mean spike phases were significantly clustered near the initial ascending phase of the oscillation (Rayleigh test, p<0.00001). (C) Population scatter plot of the mean phase of firing and maximally detected frequency within the band for each phase-locked MTL neurons. (D) Population results showing proportion of phase-locked neurons in each brain region. Total bar height indicates the proportion of neurons recorded on an LFP channel with a band in the 1–10 Hz range. See methods for region acronyms. DOI: https://doi.org/10.7554/eLife.32554.007 

population of MTL neurons, we identified phase-locked neural firing in 144 neurons (144/466, 30%, Rayleigh test, p<0.005), a proportion significantly above chance (Binomial p<0.00001). We observed that phase locked neural firing was clustered just after the trough of the oscillation for these cells (Figure 3B, Rayleigh test p<0.00001) and most phase locking occurred to slow-theta oscillations below 5 Hz (Figure 3C). Significant counts of phase-locked neurons were observed in each brain region (Binomial test, p<0.0001) and we observed phase-locking most prominently in the hippocampus (Figure 3D). These results confirm the presence of phase-modulated neuronal activity in this dataset. 

The SCERT model predicts that neuronal activity is modulated by oscillations at particular frequencies. Because the LFPs associated with 44 neurons displayed oscillations at two distinct frequency bands in the 1–10 Hz range, we were able to test if the spike–LFP phase locking was specific to an individual frequency band or present for both bands. 13.6% of these cells (6/44) showed frequency-specific phase locking, showing phase-locked firing in only one LFP frequency band (Figure 3A; p<0.005 in one band, p>0.1 in all other bands). In the remaining cells, 75% did not show phase-locking to any band (n = 33) or showed phase-locking to both bands (n = 5). Thus, extending previous findings (Jacobs et al., 2007) by examining phase-locking to adaptively-identified narrowband signals, we find that human neuronal firing can be modulated by the phase of lowfrequency oscillations in a band and frequency-specific manner, as predicted by several models of neural coding (Cohen, 2014; Kayser et al., 2012; Lisman and Jensen, 2013; Watrous and Ekstrom, 2014). 

## LFP-spike phase coding of goal information 

To understand the behavioral relevance of phase-tuned neuronal activity, we tested whether neurons also used phase-tuned neural firing to encode spatial contextual information, analogous to the phase coding for location in the rodent hippocampus (O’Keefe and Recce, 1993). Our task tapped into goal-directed navigation and we therefore hypothesized that phase coding may be used to represent the patient’s prospective navigational goal and should appear as neuronal firing to different phases for different navigational goals. Visual inspection of raw traces (Figure 4—figure supplement 1) and circular histograms of spike-phases during deliveries to each goal revealed that this pattern was evident in individual neurons (Figure 4A–B). 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

6 of 16 

Research advance 

Neuroscience 

**==> picture [514 x 183] intentionally omitted <==**

Figure 4. Spike–Phase coding for navigational goals. (A) Example neuron from the right hippocampus of patient one showing significant spike-LFP phase coding for goal four compared to goals 5 and 6. Circular histograms show spike counts separately for different goals. Black line at center of each plot shows the resultant vector and the colored arc indicates the 95th percentile confidence interval of the circular mean. (B) Example cell from left entorhinal cortex of patient six showing phase coding for goal 6. (C) Population summary showing the proportion of significant neurons in each region that showed rate coding, phase coding, or both effects. Pooling over regions, we observed significant phase coding in 10% of cells. LEC: Left entorhinal cortex; RH: Right hippocampus. 

DOI: https://doi.org/10.7554/eLife.32554.008 

The following figure supplements are available for figure 4: 

Figure supplement 1. Single-trial examples of phase coding in Patient 1. DOI: https://doi.org/10.7554/eLife.32554.009 Figure supplement 2. Single-trial examples of data from a neuron in Patient 11. DOI: https://doi.org/10.7554/eLife.32554.010 

We used a cross-validated decoding approach (Watrous et al., 2015a; see Materials and methods) to confirm that goal-specific phase variations were robust, by testing whether the patient’s prospective goal could be predicted from the phase of neuronal spiking. This analysis identified 63 cells (10% of 627 cells tested) across all regions that showed individually significant decoding of goal information from spike phases (p<0.05, shuffle corrected). This proportion of neurons exceeded chance levels (Binomial test, p<0.0001) and spike phase coding differentially occurred in the hippocampus ( `c`[2] (6)=50, p<0.0001), with 28 of the phase coding cells coming from the hippocampus of nine different patients (Figure 4C). Roughly half (29/63) of phase coding cells exhibited significant phase-locking (Rayleigh test, p<0.005), consistent with the idea that phase-locking and phase coding are related but non-identical phenomena (Watrous et al., 2015a). Critically, 51 (80%) of the cells that showed significant phase coding did not show firing-rate effects (two-way ANOVA, p>0.1), indicating that phase coding for a specific goal state can exist independent of firing rate effects. We also observed intriguing examples of neurons that showed rate and phase-coding for different goals (Figure 4—figure supplement 2). These results indicate that rate and phase coding each contribute to the neural representation of goals during navigation. 

To further understand hippocampal phase coding and motivated by our findings of differential firing rate modulation during planning and arrival, we investigated if phase coding differentially occurred during different task periods. Observing such a distinction would indicate that phase coding for goals is behaviorally relevant because the effects relate to navigational planning or goal arrival. We thus re-ran our decoding analysis for hippocampal neurons and restricted the analysis to either planning or arrival periods of each trial. We identified a subset of 24 hippocampal neurons that showed significant decoding (p<0.05) during the planning period, a proportion significantly above chance (24/186 neurons, 12% Binomial test p<0.00001, chance = 9.3 neurons). Similarly, we identified a mostly distinct subset of neurons (e.g., Figure 4—figure supplements 1 and 2) that 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

7 of 16 

Research advance 

Neuroscience 

showed phase coding during goal arrival (24/186 neurons, 12%, Binomial test p<0.00001). Importantly, these were largely distinct subsets of hippocampal neurons and were found in different patient groups, with only two neurons significant for both planning and arrival. Because we imposed two statistical thresholds per cell for inclusion, this analysis is statistically more stringent than the preceding analysis, which assessed phase coding over the entire task period, and thus the neuron counts are expected to be substantially smaller. 

Although our primary analysis focused on phase coding to low-frequency (1–10 Hz) oscillations because they were most prevalent in the hippocampus, we also examined whether phase coding was present at the sites that showed alpha- or beta-band oscillations (10–30 Hz). However, we did not observe phase coding beyond chance levels in this population of hippocampal cells in this band (5.2%, n = 7 of 133 neurons, chance = 5%). 

In sum, we find evidence that phase-coding by individual neurons is specific to particular task periods and frequencies. We conclude that phase coding occurs in distinct hippocampal populations in support of navigational planning and goal arrival. More broadly, these findings suggest that phase-based coding to slow oscillations is a general phenomenon used by MTL neurons to represent contextual information. 

We performed several control analyses to exclude alternate accounts of our findings (see Control Analyses section for full details). Average firing rates did not differ between phase-coding and nonphase-coding cells (ranksum test, p=0.39). Phase coding was not related to the overall prevalence of oscillations detected by MODAL (rho = `�` 0.0049, p=0.9) nor to oscillatory bandwidth (rho = 0.008, p=0.85). The prevalence of oscillations was not modulated as a function of goal in the vast majority (94%) of phase-coding cells. These results indicate that phase coding for goals is more directly related to coupling between spikes and the LFP than to broader changes in LFP power or spike rates. Finally, to link these findings to our previous work using high-frequency activity (Watrous et al., 2015a), we observed a significant positive relationship (shuffle corrected p<0.01) between single-neuron firing rate and high-frequency activity in 41% of recorded neurons, suggesting that the phenomena are related in many cases. We thus conclude that phase coding is a robust mechanism for neural representation in the human brain during navigation. 

## Discussion 

Analyzing recordings from epilepsy patients performing a goal-directed navigation task, we expand our previous observation of phase-coding with high-frequency LFPs (Watrous et al., 2015a) to the domain of single neuron spiking. In addition to firing rate modulations (discussed below), we found a distinct population of `~` 10% of cells in which spike-LFP phase coding contributed to representations in the absence of significant changes in firing rate (Hyman et al., 2005; Rutishauser et al., 2010). In addition, we found neurons that were phase-locked to frequency-specific narrowband oscillations primarily in the slow-theta band. Together, these findings provide new, stronger evidence for SCERT and related models that posit a role for oscillatory phase in neural coding (Nadasdy, 2009; Kayser et al., 2012; Lisman and Jensen, 2013; Watrous and Ekstrom, 2014). 

We replicated the earlier finding of firing-rate coding of goal representations in human single-cell activity (Ekstrom et al., 2003) and provide novel evidence for MTL and medial prefrontal neuronal firing during navigational planning (Figure 1E). Consistent with its role in viewpoint-dependent scene processing (Epstein et al., 2003), we found neurons in parahippocampal gyrus that were modulated during navigational arrival. In our analysis of goal modulation, we identified a similar number of neurons that were rate-modulated (n = 53) or spike-LFP phase modulated (n = 63) and these were largely non-overlapping neuronal populations. Phase-coding also appeared to be modulated by current task demands such that it appeared during either navigational planning or goal arrival. Because different groups of cells show rate versus phase coding for goals, it indicates that these phenomena are partially distinct (Huxter et al., 2003) and that phase coding is not an epiphenomenon. 

Our analyses benefited from employing the MODAL algorithm, which combines features of earlier algorithms (Whitten et al., 2011; Lega et al., 2012; Cohen, 2014) to identify oscillatory bands in a manner that is customized for each recording site. MODAL is an improvement on these methods because it adaptively identifies oscillatory band(s) without introducing experimenter bias regarding bands of interest, excludes periods when phase is noisy because oscillations are absent, and 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

8 of 16 

Research advance 

Neuroscience 

provides exactly one estimate of power, phase, and frequency per band and timepoint. We focused on low-frequency oscillations in this study due to the nature of our task, but it should be understood that MODAL allows one to investigate oscillatory effects such as phase-coding at higher frequency bands such as beta or gamma (Siegel et al., 2009; Colgin, 2016). Prior work has argued that the unstable shifts in gamma frequency limit their utility in phase coding (Xing et al., 2012). This is likely distinct from phase coding at slow frequencies in which both modeling (Cohen, 2014) and empirical studies (Hutcheon and Yarom, 2000; Giocomo et al., 2007) support the idea that neurons may respond maximally to inputs at particular frequencies, likely manifesting as the aggregated LFP signal (Buzsa´ki et al., 2012). 

Our findings provide the first evidence of phase coding during human navigation and provide a theoretically important link to other model systems where phase coding is present (Siegel et al., 2009; Kayser et al., 2009; Turesson et al., 2012; Ng et al., 2013), such as phase-precession (O’Keefe and Recce, 1993; Terada et al., 2017). However, we also found prominent phase-locking and phase-coding to slower frequency oscillations below 5 Hz, suggesting that phase coding exists beyond the canonical 8-Hz theta signal seen in rats. These findings thus lend further credence to findings indicating that (virtual) navigation-related theta occurs at a slower frequency in humans (Watrous et al., 2013; Jacobs, 2014; Bohbot et al., 2017) and demonstrates that these oscillations play a functional role in modulating neuronal spiking. 

Epilepsy is marked by slowing of neural oscillations which might be considered a confound in the present study. However, numerous previous studies have identified `~` 3-Hz oscillations in the human MTL (Mormann et al., 2008; Watrous et al., 2011; Lega et al., 2012; Bush et al., 2017), some of which had removed electrodes from the seizure onset zone or had analyzed intracranial recordings from non-epileptic patients (Brazier, 1968). We thus conclude that the present results would generalize to healthy populations. 

These results align with work implicating the human MTL in spatial contextual representation (Ranganath and Ritchey, 2012) of navigational goals (Ekstrom et al., 2003; Watrous et al., 2011; Brown et al., 2016). Our results provide further evidence that the timing of MTL activity is critical for behavior (Reber et al., 2017; Rey et al., 2014). We speculate that the goal coding observed in this study reflects flexible coding of spatial contextual information in the service of ongoing behavior (Warren et al., 2012; Yee et al., 2014). Consistent with this interpretation, we observed cells that were phase coding either during navigational planning or goal arrival. Combined with previous human studies (Kraskov et al., 2007; Lopour et al., 2013; Watrous et al., 2015a; ten Oever and Sack, 2015), our work indicates that both firing rate and the precise timing of activity relative to LFP phase are general coding mechanisms in the human MTL across behaviors and tasks, suggesting that other types of contextual information may also be encoded using LFP phase. Future studies can build off these findings to directly assess phase coding of other types of contextual information in humans, such as phase-precession to space or time. 

## Materials and methods 

## Neural recordings and behavioral task 

We analyzed data from 12 patients with drug-resistant epilepsy undergoing seizure monitoring (surgeries performed by I.F.). The Medical Institutional Review Board at the University of California-Los Angeles approved this study (IRB#10–000973) involving recordings from patients with drug-resistant epilepsy who provided informed consent to participate in research. Patients were implanted with microwire depth electrodes (Fried et al., 1999) targeting the medial temporal lobe and medial frontal lobe sites (Figure 1—figure supplement 1, see Jacobs et al., 2010; Fried et al., 1999; Mukamel et al., 2010 for other example implantation images). Groups were formed for recordings in hippocampus, entorhinal cortex, parahippocampal gyrus, amygdala, orbitofrontal, (pre) motor, and cingulate/medial prefrontal cortex. (n = 282, 176, 68, 225, 200, 82, 137 neurons, respectively). Acronyms for these regions are Hipp, EC, PHG, Amy, OF, Motor, and mPFC, respectively. Subsets of these neurons were analyzed depending on the inclusion criteria for each specific analysis. For instance, only neurons with simultaneously recorded LFPs exhibiting 1–10 Hz oscillations were analyzed for phase locking and phase coding. Microwire signals were recorded at 28–32 kHz and 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

9 of 16 

Research advance 

Neuroscience 

captured LFPs and action potentials, which were spike-sorted using wave_clus (Quiroga et al., 2004). Signals were then downsampled to 2 kHz. 

We examined data from a total of 31 recording sessions in which patients performed a continuous virtual-taxi driver game in a circular environment. Patients were instructed to drive passengers to one of 6 goal stores in the virtual environment. Upon arrival, they were given a new goal destination. The task was self-paced in order to accommodate patient testing needs and therefore patients performed at ceiling. Patients performed an average of 73 deliveries in each session (standard deviation = 11 deliveries). To assess behavioral performance, we calculated the drive time for each delivery, defined as the amount of time to drive between goal stores. We binned each task session into quintiles and calculated a Kruskal-Wallis test across task sessions. The recordings and behavioral task have been detailed in prior publications that have characterized the spatial-tuning of neurons using firing rate alone (Jacobs et al., 2010; Miller et al., 2015). Here, our primary analyses focused on how contextual information about navigational goals may be encoded based on firing rates and spike-LFP interactions. 

## Detection and rejection of epileptogenic signals 

We implemented an automated algorithm to detect and exclude epochs of signal likely resulting from epileptic activity following prior work (Gelinas et al., 2016). We first low-pass filtered (fourth order Butterworth) the signal below 80 Hz to remove any spike-contamination at high frequencies. Epochs were marked for rejection if the envelope of the unfiltered signal was four standard deviations above the baseline or if the envelope of the 25–80 Hz bandpass filtered signal (after rectification) was four standard deviations above the baseline. In some cases, we noted short ‘bad data’ epochs lasting less than one second were not detected. We conservatively elected to exclude these epochs by marking any ‘good data’ epoch lasting less than one second as ‘bad’. Bad data epochs were excluded from all analyses. This algorithm identified and excluded `~` 5% (median across LFP channels) of data. Furthermore, the rate of excluded data did not differ between the LFP channels that did and did not contain phase-coding cells (rank-sum test, p=0.9). 

## Multiple oscillations detection algorithm (‘MODAL’) 

Numerous factors contribute to the presence and characteristics of band-limited neural oscillations, broadly including neuroanatomy, behavioral state, and recording equipment (Buzsa´ki et al., 2012). We developed an algorithm to adaptively detect and characterize neural oscillations in bands exceeding the background 1/f spectrum motivated by rodent studies that exclude periods of low amplitude theta oscillations when assessing phase coding (Lenck-Santini and Holmes, 2008). To this end, we modified the ‘frequency sliding’ algorithm (Cohen, 2014), which provides the instantaneous phase and frequency of oscillations in a band, in two important ways. 

First, rather than calculating frequency sliding in a priori bands, we defined bands for subsequent analysis on each electrode as those frequencies exceeding the background 1/f spectrum. We calculated power values in .5 Hz steps from 1 to 50 Hz using six cycle Morlet wavelet convolution. We then created a power spectrum by averaging values over time (and excluding bad data epochs), and fit a line to this spectrum in log-log space using robustfit in Matlab. Similar approaches have been used previously (Lega et al., 2012; Podvalny et al., 2015). Frequency band edges were defined as the lowest and highest frequencies in a contiguous set of frequencies that had values exceeding this fit; several bands could be detected on each electrode. We then calculated the instantaneous frequency and phase in each detected band using the ‘frequency sliding’ algorithm (Cohen, 2014). 

Second, frequency sliding provides a frequency and phase estimate at every moment in time, regardless of the presence or absence of an oscillation. We ensured that phase and frequency estimates were only obtained during time periods where there was increased power in the band of interest. We recomputed the power spectrum in 10s, non-overlapping windows and recomputed the fit line as described above. We excluded phase and frequency estimates at time points (1) in which the power was below the fit line or, (2) were during bad data epochs. Finally, we also excluded noisy frequency estimates outside of the band, which can occur based on ‘phase slips’ (Cohen, 2014). MODAL was implemented in Matlab using custom code that is available on Github (https://github. com/andrew-j-watrous/MODAL; copy archived at https://github.com/elifesciences-publications/ MODAL). 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

10 of 16 

Research advance 

Neuroscience 

## Statistical analyses 

To assess how neuronal activity may vary during navigational planning and goal arrival, we split each delivery in half and operationalized the first half of each delivery as the planning period and the second half of each delivery as the arrival period. This approach has the advantage of creating equally sized temporal windows for analysis but does not allow us to draw firm conclusions regarding the precise temporal dynamics of navigational planning or goal arrival. We analyzed neural firing rate using a two-way ANOVA with factors of navigational goal and task period. Cells which exhibited main effects of goal or task period (defined as p<0.05 uncorrected) were considered significant. 

We used Rayleigh tests to identify phase-locked neural firing, extracting the phase of the LFP during each spike in each detected frequency band. All analyses were done considering each band separately and statistical thresholding was set at p<0.005 for each cell. This was chosen to be stricter than p<0.05 (Bonferroni-corrected) across the number of bands detected in the 1–10-Hz range. To control for the possibility that non-sinusoidal oscillations led to spurious phase-locking, we tested if the distribution of spike phases was different from the distribution of all phases on the LFP. 96% of phase-locked cells had a significantly different phase-preference to that of the entire LFP (p<0.05; Watson Williams test), suggesting that phase-locked activity was not a byproduct of non-sinusoidal oscillations. 

## Assessment of phase coding using cross-validated decoding 

We used a decoding-based approach to identify phase coding, employing a linear decoder with fivefold cross-validation to predict the behavioral goal from the phase of the LFP during neural spiking. In each band detected by MODAL, we first computed the sine and cosine of the phase values before classification following previous work (Lopour et al., 2013; Watrous et al., 2015a). Chance performance varies across cells because we classified goal information associated with the LFP phase for each spike and the distribution of spikes across goals varied between cells. Similarly, circular statistics can be influenced by small sample sizes. We accounted for these issues using a permutation procedure, re-running our classification 500 times per cell using shuffled goal information (circshift in Matlab to maintain the temporal structure of the session) to get a surrogate distribution of classification accuracies per cell. We then obtained a p-value for classification by ranking our observed classification accuracy to the surrogate distribution; p-values less than .05 were considered significant. We additionally ruled out the possibility that our phase-decoding approach was biased to observe effects in more narrow oscillatory bands, finding no correlation between phase-decoding classifier accuracy and oscillatory bandwidth (rho = -0.008, p=0.85; see also Supplemental Materials). 

We then used the above decoding approach considering spikes in only the first half (planning) or second half (arrival) of each delivery to assess how phase coding varies by behavior. Each cell was categorized as phase coding during planning (p<0.05 with decoding approach), arrival (p<0.05), or both. 

## Control analyses 

We performed three analyses testing whether broader changes in the LFP, which may influence signal to noise ratio, may contribute to or confound our results. First, we correlated the phase-decoding classification accuracy in each band with the proportion of time oscillations were detected over the whole session. We did not observe a relation between the prevalence of oscillations and phase decoding (rho = `�` 0.0049, p=0.9). Second, we performed an analysis testing whether phase-coding, measured by classification accuracy of our decoder, was related to the oscillatory bandwidth. We did not observe any relationship between the two measures (rho = `�` 0.008, p=0.85), indicating that phase coding in the range we are considering (<10 Hz) is unrelated to bands with wider (possibly less stable) frequencies. Third, to determine if the prevalence of oscillations across goals could account for our phase coding results, we asked whether the prevalence of oscillatory bouts in each band varied by goal, focusing our analysis on channels where we observed phase coding cells. For each band between 1–10 Hz, we computed the prevalence of bouts for each goal. We assessed significant goal-related changes in bouts with chi-square tests, comparing the observed chi-square value to a surrogate distribution of values generated by shuffling goal information (n = 100 shuffles). We observed significant effects (p<0.05 shuffle corrected) in only 6.4% of cases which did not exceed chance levels (Binomial test, p=0.18). 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

11 of 16 

Research advance 

Neuroscience 

To determine how the present single-neuron results relate to our previous work (Watrous et al., 2015a), we tested whether (1) high frequency activity (HFA; 65–120 Hz) correlated with single-neuron spiking and (2) whether HFA demonstrated phase coding to low-frequency phase. First, excluding bad epochs and analyzing the entire recording session for each LFP with an associated singleneuron recording, we correlated z-scored HFA with a smoothed firing rate vector (500 ms kernel). We identified significant (shuffle-corrected p<0.01) positive correlations between HFA and singleneuron activity in 544/1311 (41%) of neurons. In contrast, negative correlations were only identified in 14 neurons. 

Second, to test whether the low-frequency phase when HFA events occurred correlated with goal state, we adapted our decoding framework to incorporate HFA events instead of spiking, using similar methods as our previous work (Watrous et al., 2015a). Briefly, for each channel we identified periods where the normalized HFA power exceeded z = 1.96 and labeled the center of each such period as an HFA ‘event’ (see Figure 2c in Watrous et al., 2015a). Each HFA event was then treated as if it were the timepoint of an action potential and used as the input to our main analysis of spike– phase coding. Using this approach, we found significant decoding using HFA events instead of spikes on 14% of channels (76/525), comparable to what we have previously reported (Watrous et al., 2015a). We then asked if the presence of HFA phase coding on a channel correlated with the existence of spike-phase coding on the same channel. However, we found that the presence of these two phenomena were unrelated across channels ( `c`[2] =0.01, p=0.9). Thus, while single-neuron firing is correlated with increases in HFA, both of which demonstrate phase coding, spike- and HFA-phase coding were not observed on the same channels. This counter-intuitive result may reflect a functional heterogeneity of information representation within the human MTL, whereby adjacent cells represent different types of information even as they contribute to the same LFP. This is similar to what has been observed in monkey orbitofrontal cortex regarding the differential information representation shown by single neurons compared to HFA (Rich and Wallis, 2017). 

## Data availability 

The raw human single-neuron recordings can be obtained upon request from Joshua Jacobs. At this point, the data has not been made publicly available to ensure controlled access to the dataset and that the patient’s anonymity is not compromised. 

## Acknowledgements 

We wish to thank the patients for their participation in this study. This work was supported by National Institutes of Health grants NS033221 and NS084017 (IF), MH061975, MH104606 (JJ), and National Science Foundation grants GRFP (SEQ) and BCS-1724243 (JJ). We also thank the editors and three anonymous reviewers for helpful feedback that greatly improved this manuscript. 

## Additional information 

|Funding|||
|---|---|---|
|Funder|Grant reference number|Author|
|National Science Foundation|DGE 16-44869|Salman E Qasim|
|National Institute of Neurolo-|NS033221|Itzhak Fried|
|gical Disorders and Stroke|||
|National Institute of Neurolo-|NS084017|Itzhak Fried|
|gical Disorders and Stroke|||
|National Institute of Mental|MH104606|Joshua Jacobs|
|Health|||
|National Science Foundation|BCS-1724243|Joshua Jacobs|
|National Institute of Mental|MH061975|Joshua Jacobs|
|Health|||



Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

12 of 16 

Research advance 

Neuroscience 

The funders had no role in study design, data collection and interpretation, or the decision to submit the work for publication. 

## Author contributions 

Andrew J Watrous, Conceptualization, Resources, Software, Formal analysis, Investigation, Methodology, Writing—original draft, Writing—review and editing; Jonathan Miller, Data curation, Software, Writing—review and editing; Salman E Qasim, Resources, Software, Writing—review and editing; Itzhak Fried, Resources, Funding acquisition, Investigation, Writing—review and editing; Joshua Jacobs, Conceptualization, Resources, Data curation, Supervision, Funding acquisition, Investigation, Visualization, Methodology, Writing—original draft, Project administration, Writing—review and editing 

## Author ORCIDs 

Andrew J Watrous http://orcid.org/0000-0002-3107-3726 Salman E Qasim http://orcid.org/0000-0001-8739-5962 Itzhak Fried http://orcid.org/0000-0002-5962-2678 Joshua Jacobs https://orcid.org/0000-0003-1807-6882 

## Ethics 

Human subjects: The Medical Institutional Review Board at the University of California-Los Angeles approved this study (IRB#10-000973) involving recordings from patients with drug-resistant epilepsy who provided informed consent to participate in research. 

## Decision letter and Author response 

Decision letter https://doi.org/10.7554/eLife.32554.016 Author response https://doi.org/10.7554/eLife.32554.017 

## Additional files 

## Supplementary files 

`.` Transparent reporting form DOI: https://doi.org/10.7554/eLife.32554.011 

## Data availability 

The raw data can be obtained upon request from Joshua Jacobs (joshua.jacobs@columbia.edu). At this point, the raw data have not been made publicly available to ensure controlled access to the dataset and that the patients’ anonymity is not compromised. 

The following previously published dataset was used: 

|||||Database, license,|
|---|---|---|---|---|
|||||and accessibility|
|Author(s)|Year|Dataset title|Dataset URL|information|
|Fujisawa S, Amara-|2015|Simultaneous electrophysiological|http://dx.doi.org/10.|Publicly available at|
|singham A, Harri-||recordings of ensembles of isolated|6080/K01V5BWK|CRCNS.org -|
|son MT, Peyrache||neurons in rat medial prefrontal||Collaborative|
|A, Buzsa´ki G||cortex and intermediate CA1 area||Research in|
|||of the hippocampus during a||Computational|
|||working memory task||Neuroscience|



## References 

Belitski A, Gretton A, Magri C, Murayama Y, Montemurro MA, Logothetis NK, Panzeri S. 2008. Low-frequency local field potentials and spikes in primary visual cortex convey independent visual information. Journal of Neuroscience 28:5696–5709. DOI: https://doi.org/10.1523/JNEUROSCI.0009-08.2008, PMID: 18509031 Bellmund JL, Deuker L, Navarro Schro¨ der T, Doeller CF. 2016. Grid-cell representations in mental simulation. eLife 5:e17089. DOI: https://doi.org/10.7554/eLife.17089, PMID: 27572056 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

13 of 16 

Research advance 

Neuroscience 

Bohbot VD, Copara MS, Gotman J, Ekstrom AD, Gotman ADE. 2017. Low-frequency theta oscillations in the human hippocampus during real-world and virtual navigation. Nature Communications 8:14415. DOI: https:// doi.org/10.1038/ncomms14415, PMID: 28195129 

- Brazier MA. 1968. Studies of the EEG activity of limbic structures in man. Electroencephalography and Clinical Neurophysiology 25:309–318. DOI: https://doi.org/10.1016/0013-4694(68)90171-5, PMID: 4176535 

- Brown TI, Carr VA, LaRocque KF, Favila SE, Gordon AM, Bowles B, Bailenson JN, Wagner AD. 2016. Prospective representation of navigational goals in the human hippocampus. Science 352:1323–1326. DOI: https://doi.org/ 10.1126/science.aaf0784, PMID: 27284194 

- Bush D, Bisby JA, Bird CM, Gollwitzer S, Rodionov R, Diehl B, McEvoy AW, Walker MC, Burgess N. 2017. Human hippocampal theta power indicates movement onset and distance travelled. PNAS 114:12297–12302. DOI: https://doi.org/10.1073/pnas.1708716114, PMID: 29078334 

- Buzsa´ki G, Anastassiou CA, Koch C. 2012. The origin of extracellular fields and currents–EEG, ECoG, LFP and spikes. Nature Reviews Neuroscience 13:407–420. DOI: https://doi.org/10.1038/nrn3241, PMID: 22595786 

- Buzsa´ki G, Moser EI. 2013. Memory, navigation and theta rhythm in the hippocampal-entorhinal system. Nature Neuroscience 16:130–138. DOI: https://doi.org/10.1038/nn.3304, PMID: 23354386 

- Ciaramelli E. 2008. The role of ventromedial prefrontal cortex in navigation: a case of impaired wayfinding and rehabilitation. Neuropsychologia 46:2099–2105. DOI: https://doi.org/10.1016/j.neuropsychologia.2007.11.029, PMID: 18201735 

- Cohen MX. 2014. Fluctuations in oscillation frequency control spike timing and coordinate neural networks. Journal of Neuroscience 34:8988–8998. DOI: https://doi.org/10.1523/JNEUROSCI.0261-14.2014, PMID: 24990 919 

- Colgin LL. 2016. Rhythms of the hippocampal network. Nature Reviews Neuroscience 17:239–249. DOI: https:// doi.org/10.1038/nrn.2016.21, PMID: 26961163 

- Crone NE, Miglioretti DL, Gordon B, Lesser RP. 1998. Functional mapping of human sensorimotor cortex with electrocorticographic spectral analysis. II. Event-related synchronization in the gamma band. Brain 121:2301– 2315. DOI: https://doi.org/10.1093/brain/121.12.2301, PMID: 9874481 

- Ekstrom A, Viskontas I, Kahana M, Jacobs J, Upchurch K, Bookheimer S, Fried I. 2007. Contrasting roles of neural firing rate and local field potentials in human memory. Hippocampus 17:606–617. DOI: https://doi.org/ 10.1002/hipo.20300, PMID: 17546683 

- Ekstrom AD, Caplan JB, Ho E, Shattuck K, Fried I, Kahana MJ. 2005. Human hippocampal theta activity during virtual navigation. Hippocampus 15:881–889. DOI: https://doi.org/10.1002/hipo.20109, PMID: 16114040 

- Ekstrom AD, Kahana MJ, Caplan JB, Fields TA, Isham EA, Newman EL, Fried I. 2003. Cellular networks underlying human spatial navigation. Nature 425:184–188. DOI: https://doi.org/10.1038/nature01964, PMID: 12968182 

- Epstein R, Graham KS, Downing PE. 2003. Viewpoint-specific scene representations in human parahippocampal cortex. Neuron 37:865–876. DOI: https://doi.org/10.1016/S0896-6273(03)00117-X, PMID: 12628176 

- Fried I, Wilson CL, Maidment NT, Engel J, Behnke E, Fields TA, MacDonald KA, Morrow JW, Ackerson L. 1999. Cerebral microdialysis combined with single-neuron and electroencephalographic recording in neurosurgical patients. technical note. Journal of Neurosurgery 91:697–705. DOI: https://doi.org/10.3171/jns.1999.91.4.0697, PMID: 10507396 

- Fujisawa S, Amarasingham A, Harrison MT, Buzsa´ki G. 2008. Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex. Nature Neuroscience 11:823–833. DOI: https://doi.org/10.1038/nn.2134, PMID: 18516033 

- Gelinas JN, Khodagholy D, Thesen T, Devinsky O, Buzsa´ki G. 2016. Interictal epileptiform discharges induce hippocampal–cortical coupling in temporal lobe epilepsy. Nature Medicine 22:641–648. DOI: https://doi.org/ 10.1038/nm.4084 

- Giocomo LM, Zilli EA, Franse´ n E, Hasselmo ME. 2007. Temporal frequency of subthreshold oscillations scales with entorhinal grid cell field spacing. Science 315:1719–1722. DOI: https://doi.org/10.1126/science.1139207, PMID: 17379810 

- Hok V, Lenck-Santini PP, Roux S, Save E, Muller RU, Poucet B. 2007. Goal-related activity in hippocampal place cells. Journal of Neuroscience 27:472–482. DOI: https://doi.org/10.1523/JNEUROSCI.2864-06.2007, PMID: 17234580 

- Hollup SA, Molden S, Donnett JG, Moser MB, Moser EI. 2001. Accumulation of hippocampal place fields at the goal location in an annular watermaze task. The Journal of Neuroscience 21:1635–1644. DOI: https://doi.org/ 10.1523/JNEUROSCI.21-05-01635.2001, PMID: 11222654 

- Horner AJ, Bisby JA, Zotow E, Bush D, Burgess N. 2016. Grid-like processing of imagined navigation. Current Biology 26:842–847. DOI: https://doi.org/10.1016/j.cub.2016.01.042, PMID: 26972318 

- Howard LR, Javadi AH, Yu Y, Mill RD, Morrison LC, Knight R, Loftus MM, Staskute L, Spiers HJ. 2014. The hippocampus and entorhinal cortex encode the path and Euclidean distances to goals during navigation. Current Biology 24:1331–1340. DOI: https://doi.org/10.1016/j.cub.2014.05.001, PMID: 24909328 

- Hutcheon B, Yarom Y. 2000. Resonance, oscillation and the intrinsic frequency preferences of neurons. Trends in Neurosciences 23:216–222. DOI: https://doi.org/10.1016/S0166-2236(00)01547-2, PMID: 10782127 

- Huxter J, Burgess N, O’Keefe J. 2003. Independent rate and temporal coding in hippocampal pyramidal cells. Nature 425:828–832. DOI: https://doi.org/10.1038/nature02058, PMID: 14574410 

- Hyman JM, Zilli EA, Paley AM, Hasselmo ME. 2005. Medial prefrontal cortex cells show dynamic modulation with the hippocampal theta rhythm dependent on behavior. Hippocampus 15:739–749. DOI: https://doi.org/10. 1002/hipo.20106, PMID: 16015622 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

14 of 16 

Research advance 

Neuroscience 

- Jacobs J, Kahana MJ, Ekstrom AD, Fried I. 2007. Brain oscillations control timing of single-neuron activity in humans. Journal of Neuroscience 27:3839–3844. DOI: https://doi.org/10.1523/JNEUROSCI.4636-06.2007, PMID: 17409248 

- Jacobs J, Kahana MJ, Ekstrom AD, Mollison MV, Fried I. 2010. A sense of direction in human entorhinal cortex. PNAS 107:6487–6492. DOI: https://doi.org/10.1073/pnas.0911213107, PMID: 20308554 

- Jacobs J. 2014. Hippocampal theta oscillations are slower in humans than in rodents: implications for models of spatial navigation and memory. Philosophical Transactions of the Royal Society B: Biological Sciences 369: 20130304. DOI: https://doi.org/10.1098/rstb.2013.0304, PMID: 24366145 

- Jensen O, Lisman JE. 2000. Position reconstruction from an ensemble of hippocampal place cells: contribution of theta phase coding. Journal of Neurophysiology 83:2602–2609. DOI: https://doi.org/10.1152/jn.2000.83.5. 2602, PMID: 10805660 

- Jones MW, Wilson MA. 2005. Phase precession of medial prefrontal cortical activity relative to the hippocampal theta rhythm. Hippocampus 15:867–873. DOI: https://doi.org/10.1002/hipo.20119, PMID: 16149084 

- Kaplan R, Bush D, Bisby JA, Horner AJ, Meyer SS, Burgess N. 2017. Medial prefrontal-medial temporal theta phase coupling in dynamic spatial imagery. Journal of Cognitive Neuroscience 29:507–519. DOI: https://doi. org/10.1162/jocn_a_01064, PMID: 27779906 

- Kayser C, Ince RA, Panzeri S. 2012. Analysis of slow (theta) oscillations as a potential temporal reference frame for information coding in sensory cortices. PLoS Computational Biology 8:e1002717. DOI: https://doi.org/10. 1371/journal.pcbi.1002717, PMID: 23071429 

- Kayser C, Montemurro MA, Logothetis NK, Panzeri S. 2009. Spike-phase coding boosts and stabilizes information carried by spatial and temporal spike patterns. Neuron 61:597–608. DOI: https://doi.org/10.1016/j. neuron.2009.01.008, PMID: 19249279 

- Kraskov A, Quiroga RQ, Reddy L, Fried I, Koch C. 2007. Local field potentials and spikes in the human medial temporal lobe are selective to image category. Journal of Cognitive Neuroscience 19:479–492. DOI: https:// doi.org/10.1162/jocn.2007.19.3.479, PMID: 17335396 

- Lega BC, Jacobs J, Kahana M. 2012. Human hippocampal theta oscillations and the formation of episodic memories. Hippocampus 22:748–761. DOI: https://doi.org/10.1002/hipo.20937, PMID: 21538660 

- Lenck-Santini PP, Holmes GL. 2008. Altered phase precession and compression of temporal sequences by place cells in epileptic rats. Journal of Neuroscience 28:5053–5062. DOI: https://doi.org/10.1523/JNEUROSCI.502407.2008, PMID: 18463258 

- Lisman JE, Jensen O. 2013. The `q` - `g` neural code. Neuron 77:1002–1018. DOI: https://doi.org/10.1016/j.neuron. 2013.03.007, PMID: 23522038 

- Lopour BA, Tavassoli A, Fried I, Ringach DL. 2013. Coding of information in the phase of local field potentials within human medial temporal lobe. Neuron 79:594–606. DOI: https://doi.org/10.1016/j.neuron.2013.06.001, PMID: 23932002 

- Manning JR, Jacobs J, Fried I, Kahana MJ. 2009. Broadband shifts in local field potential power spectra are correlated with single-neuron spiking in humans. Journal of Neuroscience 29:13613–13620. DOI: https://doi. org/10.1523/JNEUROSCI.2041-09.2009, PMID: 19864573 

- Miller JF, Fried I, Suthana N, Jacobs J. 2015. Repeating spatial activations in human entorhinal cortex. Current Biology 25:1080–1085. DOI: https://doi.org/10.1016/j.cub.2015.02.045, PMID: 25843029 

- Miller KJ, Honey CJ, Hermes D, Rao RP, denNijs M, Ojemann JG. 2014. Broadband changes in the cortical surface potential track activation of functionally diverse neuronal populations. NeuroImage 85:711–720. DOI: https://doi.org/10.1016/j.neuroimage.2013.08.070, PMID: 24018305 

- Mormann F, Osterhage H, Andrzejak RG, Weber B, Ferna´ndez G, Fell J, Elger CE, Lehnertz K. 2008. Independent delta/theta rhythms in the human hippocampus and entorhinal cortex. Frontiers in Human Neuroscience 2:3. DOI: https://doi.org/10.3389/neuro.09.003.2008, PMID: 18958204 

- Mukamel R, Ekstrom AD, Kaplan J, Iacoboni M, Fried I. 2010. Single-neuron responses in humans during execution and observation of actions. Current Biology 20:750–756. DOI: https://doi.org/10.1016/j.cub.2010.02. 045, PMID: 20381353 

- Nadasdy Z. 2009. Information encoding and reconstruction from the phase of action potentials. Frontiers in Systems Neuroscience 3:6. DOI: https://doi.org/10.3389/neuro.06.006.2009, PMID: 19668700 

- Ng BS, Logothetis NK, Kayser C. 2013. EEG phase patterns reflect the selectivity of neural firing. Cerebral Cortex 23:389–398. DOI: https://doi.org/10.1093/cercor/bhs031, PMID: 22345353 

- O’Keefe J, Recce ML. 1993. Phase relationship between hippocampal place units and the EEG theta rhythm. Hippocampus 3:317–330. DOI: https://doi.org/10.1002/hipo.450030307, PMID: 8353611 

- O’Neill PK, Gordon JA, Sigurdsson T. 2013. Theta oscillations in the medial prefrontal cortex are modulated by spatial working memory and synchronize with the hippocampus through its ventral subregion. Journal of Neuroscience 33:14211–14224. DOI: https://doi.org/10.1523/JNEUROSCI.2378-13.2013, PMID: 23986255 

- Podvalny E, Noy N, Harel M, Bickel S, Chechik G, Schroeder CE, Mehta AD, Tsodyks M, Malach R. 2015. A unifying principle underlying the extracellular field potential spectral responses in the human cortex. Journal of Neurophysiology 114:505–519. DOI: https://doi.org/10.1152/jn.00943.2014, PMID: 25855698 

- Quiroga RQ, Nadasdy Z, Ben-Shaul Y. 2004. Unsupervised spike detection and sorting with wavelets and superparamagnetic clustering. Neural Computation 16:1661–1687. DOI: https://doi.org/10.1162/ 089976604774201631, PMID: 15228749 

- Ranganath C, Ritchey M. 2012. Two cortical systems for memory-guided behaviour. Nature Reviews Neuroscience 13:713–726. DOI: https://doi.org/10.1038/nrn3338, PMID: 22992647 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

15 of 16 

Research advance 

Neuroscience 

- Reber TP, Faber J, Niediek J, Bostro¨ m J, Elger CE, Mormann F. 2017. Single-Neuron correlates of conscious perception in the human medial temporal lobe. Current Biology 27:2991–2998. DOI: https://doi.org/10.1016/j. cub.2017.08.025, PMID: 28943091 

- Rey HG, Fried I, Quian Quiroga R. 2014. Timing of single-neuron and local field potential responses in the human medial temporal lobe. Current Biology 24:299–304. DOI: https://doi.org/10.1016/j.cub.2013.12.004, PMID: 24462002 

- Rich EL, Wallis JD. 2017. Spatiotemporal dynamics of information encoding revealed in orbitofrontal highgamma. Nature Communications 8:1139. DOI: https://doi.org/10.1038/s41467-017-01253-5, PMID: 29074960 

- Rutishauser U, Ross IB, Mamelak AN, Schuman EM. 2010. Human memory strength is predicted by thetafrequency phase-locking of single neurons. Nature 464:903–907. DOI: https://doi.org/10.1038/nature08860, PMID: 20336071 

- Siegel M, Warden MR, Miller EK. 2009. Phase-dependent neuronal coding of objects in short-term memory. PNAS 106:21341–21346. DOI: https://doi.org/10.1073/pnas.0908193106, PMID: 19926847 

- Spiers HJ, Maguire EA. 2007. The neuroscience of remote spatial memory: a tale of two cities. Neuroscience 149:7–27. DOI: https://doi.org/10.1016/j.neuroscience.2007.06.056, PMID: 17850977 

- ten Oever S, Sack AT. 2015. Oscillatory phase shapes syllable perception. PNAS 112:15833–15837. DOI: https:// doi.org/10.1073/pnas.1517519112, PMID: 26668393 

- Terada S, Sakurai Y, Nakahara H, Fujisawa S. 2017. Temporal and rate coding for discrete event sequences in the Hippocampus. Neuron 94:1248–1262. DOI: https://doi.org/10.1016/j.neuron.2017.05.024, PMID: 28602691 

- Turesson HK, Logothetis NK, Hoffman KL. 2012. Category-selective phase coding in the superior temporal sulcus. PNAS 109:19438–19443. DOI: https://doi.org/10.1073/pnas.1217012109, PMID: 23132942 

- Vass LK, Copara MS, Seyal M, Shahlaie K, Farias ST, Shen PY, Ekstrom AD. 2016. Oscillations go the distance: low-frequency human hippocampal oscillations code spatial distance in the absence of sensory cues during teleportation. Neuron 89:1180–1186. DOI: https://doi.org/10.1016/j.neuron.2016.01.045, PMID: 26924436 

- Viard A, Doeller CF, Hartley T, Bird CM, Burgess N. 2011. Anterior hippocampus and goal-directed spatial decision making. Journal of Neuroscience 31:4613–4621. DOI: https://doi.org/10.1523/JNEUROSCI.4640-10. 2011, PMID: 21430161 

- Warren DE, Duff MC, Jensen U, Tranel D, Cohen NJ. 2012. Hiding in plain view: lesions of the medial temporal lobe impair online representation. Hippocampus 22:1577–1588. DOI: https://doi.org/10.1002/hipo.21000, PMID: 22180166 

- Watrous AJ, Deuker L, Fell J, Axmacher N. 2015a. Phase-amplitude coupling supports phase coding in human ECoG. eLife 4:e07886. DOI: https://doi.org/10.7554/eLife.07886, PMID: 26308582 

- Watrous AJ, Ekstrom AD. 2014. The spectro-contextual encoding and retrieval theory of episodic memory. Frontiers in Human Neuroscience 8:75. DOI: https://doi.org/10.3389/fnhum.2014.00075, PMID: 24600373 

- Watrous AJ, Fell J, Ekstrom AD, Axmacher N. 2015b. More than spikes: common oscillatory mechanisms for content specific neural representations during perception and memory. Current Opinion in Neurobiology 31: 33–39. DOI: https://doi.org/10.1016/j.conb.2014.07.024, PMID: 25129044 

- Watrous AJ, Fried I, Ekstrom AD. 2011. Behavioral correlates of human hippocampal delta and theta oscillations during navigation. Journal of Neurophysiology 105:1747–1755. DOI: https://doi.org/10.1152/jn.00921.2010, PMID: 21289136 

- Watrous AJ, Lee DJ, Izadi A, Gurkoff GG, Shahlaie K, Ekstrom AD. 2013. A comparative study of human and rat hippocampal low-frequency oscillations during spatial navigation. Hippocampus 23:656–661. DOI: https://doi. org/10.1002/hipo.22124, PMID: 23520039 

Watrous AJ. 2018. MODAL. Github. https://github.com/andrew-j-watrous/MODAL 

- Whitten TA, Hughes AM, Dickson CT, Caplan JB. 2011. A better oscillation detection method robustly extracts EEG rhythms across brain state changes: the human alpha rhythm as a test case. NeuroImage 54:860–874. DOI: https://doi.org/10.1016/j.neuroimage.2010.08.064, PMID: 20807577 

- Wikenheiser AM, Redish AD. 2015. Hippocampal theta sequences reflect current goals. Nature Neuroscience 18:289–294. DOI: https://doi.org/10.1038/nn.3909, PMID: 25559082 

- Wolbers T, Wiener JM, Mallot HA, Bu¨ chel C. 2007. Differential recruitment of the hippocampus, medial prefrontal cortex, and the human motion complex during path integration in humans. Journal of Neuroscience 27:9408–9416. DOI: https://doi.org/10.1523/JNEUROSCI.2146-07.2007, PMID: 17728454 

- Xing D, Shen Y, Burns S, Yeh CI, Shapley R, Li W. 2012. Stochastic generation of gamma-band activity in primary visual cortex of awake and anesthetized monkeys. Journal of Neuroscience 32:13873–13880. DOI: https://doi. org/10.1523/JNEUROSCI.5644-11.2012, PMID: 23035096 

- Yee LT, Warren DE, Voss JL, Duff MC, Tranel D, Cohen NJ. 2014. The hippocampus uses information just encountered to guide efficient ongoing behavior. Hippocampus 24:154–164. DOI: https://doi.org/10.1002/ hipo.22211, PMID: 24123615 

Watrous et al. eLife 2018;7:e32554. DOI: https://doi.org/10.7554/eLife.32554 

16 of 16 

