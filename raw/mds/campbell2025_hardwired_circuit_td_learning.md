bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **A hardwired neural circuit for temporal difference learning** 

Malcolm G. Campbell[1,2,*] , Yongsoo Ra[1,2,3] , Zhiqin Chen[1,2,3] , Shudi Xu[1,2,4] , Mark Burrell[1,2] , Sara Matias[1,2] , Mitsuko Watabe-Uchida[1,2] , Naoshige Uchida[1,2,* ] 

1. Department of Molecular and Cellular Biology, Harvard University, Cambridge, MA, USA 

2. Center for Brain Science, Harvard University, Cambridge, MA, USA 

3. Program in Neuroscience, Harvard University, Boston, MA, USA 

4. Current address: Department of Neurobiology, Northwestern University, Evanston, IL, USA 

- Correspondence: mgcampb@fas.harvard.edu, uchida@mcb.harvard.edu 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 1 **Abstract** 

- 2 The neurotransmitter dopamine plays a major role in learning by acting as a teaching signal to update the 3 brain’s predictions about rewards. A leading theory proposes that this process is analogous to a 

- 4 reinforcement learning algorithm called temporal difference (TD) learning, and that dopamine acts as the 5 error term within the TD algorithm (TD error). Although many studies have demonstrated similarities 6 between dopamine activity and TD errors[1–5] , the mechanistic basis for dopaminergic TD learning remains 

- 7 unknown. Here, we combined large-scale neural recordings with patterned optogenetic stimulation to 8 examine whether and how the key steps in TD learning are accomplished by the circuitry connecting 

- 9 dopamine neurons and their targets. Replacing natural rewards with optogenetic stimulation of dopamine 

- 10 axons in the nucleus accumbens (NAc) in a classical conditioning task gradually generated TD error-like 11 activity patterns in dopamine neurons by specifically modifying the task-related activity of NAc neurons 12 expressing the D1 dopamine receptor (D1 neurons). In turn, patterned optogenetic stimulation of NAc D1 13 neurons in naïve animals drove dopamine neuron spiking according to the TD error of the stimulation 14 pattern, indicating that TD computations are hardwired into this circuit. The transformation from D1 15 neurons to dopamine neurons could be described by a biphasic linear filter, with a rapid positive and delayed 16 negative phase, that effectively computes a temporal difference. This finding suggests that the time horizon 17 over which the TD algorithm operates—the temporal discount factor—is set by the balance of the positive 

- 18 and negative components of the linear filter, pointing to a circuit-level mechanism for temporal discounting. 

- 19 These results provide a new conceptual framework for understanding how the computations and parameters 20 governing animal learning arise from neurobiological components. 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 21 **Introduction** 

22 The brain learns by comparing internal expectations against real outcomes and updating 23 expectations when they are wrong. This idea—that a major function of the brain is to learn accurate 24 predictions, and that it does so in part by computing and minimizing prediction errors—is an influential 25 organizing principle in neuroscience[6] . 

26 A prime example of this is the phasic activity of midbrain dopamine neurons, which canonically 27 reflects the difference between predicted and actual reward—i.e. reward prediction error (RPE)—and acts 28 as a teaching signal to update reward predictions (“value”)[1,3] . More specifically, phasic dopamine reflects 29 a specific form of RPE called temporal difference RPE (TD RPE, or TD error), the error term in a 30 reinforcement learning (RL) algorithm called temporal difference (TD) learning[7,8] ( **Fig. 1a** ). TD learning is 31 a cornerstone of most real-world successes of RL[8–11] . 

32 The TD algorithm relies on a core derivative-like computation, from which it derives its name: the 33 comparison of value estimates at adjacent time steps ( **Fig. 1a** ). The intuition is simple: If value suddenly 34 increases, then to the extent that this was predictable, previous states were undervalued, and vice versa. 35 This empowers the algorithm to leverage its internal estimates to drive learning in the absence of reward 36 feedback, using a temporally local computation to bridge events that are far apart in time. 

37 A profound implication of this is that the time horizon of the TD learning algorithm—its temporal 38 discount factor, 𝛾𝛾—depends on the relative weighting of current and recent time in the local comparison of 39 the value function at adjacent time steps. This suggests that microcircuit mechanisms underlying the 40 derivative computation in the dopamine system may quantitively explain animals’ preference for immediate 41 versus future rewards. Time discounting is a fundamental aspect of learning and decision making[12,13] and 42 may be a partly hardwired personality trait[14] , but its biological origins remain mysterious. The possibility 43 of quantitatively linking dopamine circuits to time preference is tantalizing but unrealized. 

44 While debates continue[15–18] , the canonical evidence supporting the TD RPE interpretation of 45 dopamine is that dopamine neurons in trained animals (1) respond strongly to unexpected rewards, but less 46 to expected rewards; (2) respond to reward-predicting sensory cues; and (3) become suppressed when 47 expected rewards are omitted[1] ( **Fig. 1b** ). In addition to these canonical TD RPE-like activity patterns, it 48 was recently discovered that ramping dopamine activity, which can occur before reward delivery[19,20] , 49 reflects the approximate derivative of a hidden function, and thus can also be interpreted as a TD error[5,21,22] 50 ( **Fig. 1b** ). Yet despite these and other pieces of correlational[2,4] and behavioral[3,23,24] evidence, the biological 51 mechanisms that produce TD error-like activity in dopamine neurons, including the core derivative-like 52 computation, remain unknown. 

53 We hypothesized that TD RPE-like activity in dopamine neurons arises through bidirectional 54 interactions between midbrain dopamine neurons and their primary output region, the striatum—a 55 longstanding idea[25–28] that remains unproven. Neural activity in the striatum correlates with value[29–32] and 56 influences dopamine signaling both directly and indirectly, via its two primary cell types, D1 and D2 57 medium spiny neurons (MSNs) ( **Fig. 1c** ). However, the idea that dopamine-striatum interactions generate 58 TD RPE signals in dopamine neurons has been difficult to test experimentally, for two reasons: (1) tasks 59 trained with natural rewards engage learning processes throughout the entire brain, not just the dopamine 60 system, so signaling patterns in dopamine neurons in natural tasks cannot be assumed to arise specifically 61 from dopamine-striatum interactions; and (2) dopamine neurons are themselves diverse, with distinct 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 62 properties and functions depending in part on projection target[33–37] , so dopamine neurons may not all 63 participate in value learning. 

- 64 To unravel this complexity step-by-step, we started with an artificial opto-conditioning task with 65 just two components: sensory stimuli (odors) and optogenetic stimulation of dopamine axons in the lateral 66 nucleus accumbens (lNAc), a subregion of the striatum with concentrated TD RPE-like dopamine 67 signaling[38,39] and value-related neuronal activity[31,32] in natural conditioning tasks. The results revealed that 68 dopamine neurons are hardwired to automatically compute a temporal difference of input from D1-MSNs, 69 resulting in patterns of TD error in dopamine signaling, and suggest that the balance of excitation and 70 inhibition in this pathway sets the temporal discount factor of the TD algorithm. 

- 71 

- 72 **Results** 

- 73 **Opto-conditioning in lNAc generates TD error signals in dopamine activity** 

- 74 Mice were prepared for opto-conditioning by virally expressing red excitatory opsin ChrimsonR[40] 75 unilaterally in ventral tegmental area (VTA) dopamine neurons and green dopamine sensor GRABDA3m[41] in 76 lNAc ( **Fig. 1d** ). An optic fiber was implanted targeting lNAc in the same hemisphere, through which 77 dopamine axons could be stimulated while simultaneously recording dopamine release using photometry 78 without optical crosstalk ( **Extended Data Fig. 1a,b** ) or movement artifacts ( **Extended Data Fig. 1c** ). To 79 ensure physiological relevance, optogenetic stimulation was calibrated to a natural reward (8 𝜇 droplet of 80 water) ( **Fig. 1e** , **Extended Data Fig. 1b** ). 

- 81 Mice underwent conditioning in which odors (CS+/CS-) preceded opto-stimulation (75% of CS+ 82 trials) or no outcome (100% of CS- trials, 25% of CS+ trials) ( **Fig. 1f** , **Extended Data Fig. 1d,e** ). In contrast 83 to a previous report[16] , lNAc dopamine in ChrimsonR mice ( _n_ = 5), but not control tdTomato mice ( _n_ = 3), 84 gradually developed classic signatures of TD error ( **Fig. 1g-j, Extended Data Fig. 1f-i** ): a positive response 85 to CS+ (“cue response”), preceding the time of predicted stimulation ( **Fig. 1g-i** ); a negative response aligned 86 to omission of predicted stimulation (“omission dip”) ( **Fig. 1g-i** ), which reflected the timing of stimulation 87 used during training ( **Extended Data Fig. 1j-l** ); and an expectation-dependent reduction in the opto88 stimulation response ( **Fig. 1j** ). 

- 89 To investigate these changes at the level of single dopamine neurons while preserving projection 90 target specificity, we recorded spiking activity of antidromically optotagged lNAc-projecting VTA 91 dopamine neurons in the same mice on a subset of sessions using Neuropixels probes ( **Fig. 1k-q** , **Extended** 92 **Data Fig. 2** ). Projection target was identified by stimulating dopamine axons in lNAc while recording 93 spikes at the cell body in VTA ( **Fig. 1k-m** ). As in the photometry data, cue responses and omission dips 94 could be detected in the spiking activity of individual dopamine neurons ( **Fig. 1k-q** , **Extended Data Fig.** 95 **2** ). While statistically significant both within and across mice, the cue response and omission dip were small 96 in both spiking and photometry signals (~5% of response to uncued water delivery, **Fig. 1i,j** , **Extended** 97 **Data Fig. 2** )[16] , likely reflecting the minimal nature of our calibrated, local, unilateral dopamine axon 98 stimulation, and/or possibly a missing factor that would normally accompany a natural reward. 

99 Opto-conditioning was sufficient to alter behavior: Mice exhibited greater anticipatory facial 100 movements following the CS+ than the CS- ( **Extended Data Fig. 3** ). However, behavioral and neural 101 changes were dissociable, as neural changes were observed even in mice that exhibited no detectable change 102 in movement following odor onset. 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 1** 

**==> picture [476 x 673] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b Key results supporting TD RPE model of dopamine: c Biological substrates<br>TD learning loop<br>1. Cue response Cue Outcome Striatum (dopamine axons)<br>Reward 2. Omission dip<br>( ) − ( −1 ) 3<br>State 3. Predicted reward  D1-MSN<br>inputs: ( ) Temporal difference(derivative-like) TD RPE: = +     < unpredicted reward 1 2 D2-MSN<br>(Schultz et al., 1997)<br>Time<br>( ) − ( −1 )<br>SNc<br>Value learning: 4. Derivative-like  Teleport<br>( ) ← ( ) +     ramping activity VTA<br>(Kim et al., 2020) lNAc Midbrain<br>Virtual space (dopamine neurons)<br>Opto-conditioning with calibrated dopamine axon stimulation<br>AAV-flex-<br>d AAV-in lNAcGRABDA3m ChrimsonRtdTomato (Exp) or (Ctrl) e Stimulus Calibration 3025 n.s. f Odor A (CS+)Opto-Conditioning TaskStim. trials 75%<br>in VTA Water (8 μL) 20<br>Optic fiber Optic fiber Opto stim 15 Odor A (CS+) Omission trials  25%<br>10<br>Odor B (CS-)<br>5<br>0<br>-5 0 0.5 1 1.5 2<br>DAPI GRABDA3m 2 sec Time (sec)<br>DAT-Cre [+/-]  mouse<br>lNAc GRABDA3m activity, late training (days 11+)<br>g OdorExp. mice (n=5)Stim. omission Ctrl. mice (n=3)Odor Stim. omission i 54 ** * j 30 **<br>CS+ CS+ 3 * * n.s. n.s. Exp. 25<br>CS- CS- mice<br>2 20<br>1 Ctrl.<br>15<br>0 mice<br>-1 10<br>1 sec 1 sec<br>-2 5<br>h Difference: CS+ – CS- -3<br>Odor Stim. omission 0<br>-4<br>Exp. mice (n=5) -5 -5<br>Ctrl. mice (n=3)<br>CS+ CS-<br>1 sec<br>Antidromically optotagged lNAc-projecting VTA dopamine neuron spiking activity (recorded on days 21-25)<br>k Neuropixels 2.0 l m Example antidromically<br>(acute insertion) Optic fiber Neuropixels optotagged dopamine neuron<br>probe<br>Dopamine<br>release Dopamine neuron<br>cell body (VTA)<br>(expressing ChrimsonR) LED<br>No LED<br>corr. = 0.975<br>(dopamine neurons)ChrimsonR DAPI ChrimsonR  DiD Dopamine axon(striatum) Back-propagatingaction potential -10ms from LED onset0 10 20 30 40 1 ms<br>**<br>n Example neurons o n=43 neurons p Difference: CS+ – CS- q Exp.<br>1 15 Odor Stim.omission CS+CS- 0.5 Odor Stim. omissionCS+ 0.5 CueOdor OmitStim. omission 1 Mice<br>0 CS-<br>15<br>2<br>0<br>3 6 0 0 0 4<br>0<br>4 4 3<br>0 -0.5 -0.5 -1 2 1<br>-1 0 1 2 3 4 5 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5<br>Time from odor onset (sec) Time from odor onset (sec) Time from odor onset (sec) -1 0 1<br>Cue<br>Δ z-score (CS+ – CS-)<br>WaterStim<br>Unpred StimPred Stim<br>Dopamine activity<br>activity<br>Dopamine<br>% dF/F<br>10% dF/F<br>2% dF/F 2% dF/F<br>% dF/F % dF/F<br>Cue Omit Cue Omit<br>2% dF/F<br>Optotag 1 )(40 trials<br>Optotag 2 )(40 trials 50 μV<br>)-CS+-<br>Spikes/sec z-score Omit ***<br>∆ z-score (CS<br>Δ z-score (CS+ – CS-)<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 1:** Opto-conditioning in lNAc generates TD error signals in dopamine activity. 

- a) Schematic of a temporal difference (TD) learning loop[8] . The red box highlights the temporal difference calculation, which is exactly a derivative when the temporal discount factor 𝛾𝛾= 1, but deviates from a derivative when 𝛾𝛾≠1.  𝑆𝑆𝑡𝑡: state at time 𝑡𝑡, 𝑉𝑉(𝑆𝑆𝑡𝑡): the value (expected discounted sum of future reward) associated with state 𝑆𝑆𝑡𝑡, 𝑅𝑅𝑡𝑡: reward at time 𝑡𝑡, 𝛿𝛿𝑡𝑡: TD RPE, 𝛾𝛾: temporal discount factor, 𝛼𝛼: learning rate. 

- b) Key results supporting the TD RPE model of dopamine. In addition to the classic results of Schultz et al. (1997)[1] in classical conditioning tasks (cue response, omission dip, and expectation-dependent suppression of reward response), the derivative-like property of dopamine signaling in the absence of reward feedback was shown by Kim et al. (2020)[5] . 

- c) Temporal difference learning is thought to involve bi-directional interactions between midbrain dopamine neurons and their primary output region, the striatum. We first focus on lateral nucleus accumbens (lNAc), a subregion of the striatum, because evidence suggests it plays a specialized role in value learning[32,38] . lNAc: lateral nucleus accumbens, VTA: ventral tegmental area, SNc: substantia nigra pars compacta, D1-MSN: D1 dopamine receptor-expressing medium spiny neuron, D2-MSN: D2 dopamine receptor-expressing medium spiny neuron. 

- d) _Left:_ Schematic of mouse surgery. ChrimsonR (exp. mice, _n_ = 5) or tdTomato (ctrl. mice, _n_ = 3) was expressed virally in VTA dopamine neurons and GRABDA3m in lNAc. The fiber targeting lNAc was implanted at an angle to allow acute Neuropixels penetrations targeting lNAc or VTA. _Right:_ Example histology image showing fiber tip and GRABDA3m expression in lNAc. Scale bar = 1 mm. 

- e) Stimulus calibration. Optogenetic stimulation parameters were chosen to match the dopamine response to a natural reward (8 𝜇 water). _Left:_ Each thin line represents the average GRABDA3m response to 8 𝜇 water (cyan) or opto-stimulation (black) for an individual mouse ( _n_ = 5); thick lines show means over mice. _Right:_ Average GRABDA3m signal in a 1-second window following water or stimulation delivery (mean %dF/F ± SEM, exp. mice [ _n_ = 5], water: 18.87 ± 1.16, stim: 19.52 ± 1.80, _P =_ 0.56, paired t-test). Colored lines represent individual mice, black lines represent means over mice. n.s., Not Significant. 

- f) Opto-conditioning task design. 

- g) lNAc GRABDA3m photometry signals on omission trials, in late training (days 11+), in exp. mice ( _n_ = 5, left) or ctrl. mice ( _n_ = 3, right). Each pair of red/black lines represents the average GRABDA3m response to CS+ or CSfor an individual mouse, first averaged within day, then across days (days 11+). 

- h) The average difference between CS+ and CS- GRABDA3m responses on omission trials, in late training (days 11+), for each mouse, colored by whether they expressed ChrimsonR (magenta) or tdTomato (blue) in dopamine neurons. Lines/shading show mean/SEM over late training sessions for each mouse. 

- i) Average GRABDA3m signal during the odor cue (0-1 seconds after odor onset) or omission of opto-stimulation (1.5-2.5 seconds after odor onset) for the CS+ and CS-, in late training (days 11+), for exp. mice (colored dots) and ctrl. mice (gray dots). Black lines indicate means. Stars indicate the significance level of paired or unpaired t-tests. Cue responses were significantly larger in the exp. group than the ctrl. group for the CS+ (mean %dF/F ± SEM, exp. mice [ _n_ = 5]: 0.66 ± 0.33, ctrl. mice [ _n_ = 3]: -0.67 ± 0.04, _P =_ 0.023, unpaired t-test) but not the CS(mean %dF/F ± SEM, exp. mice [ _n_ = 5]: -0.37 ± 0.23, ctrl. mice [ _n_ = 3]: -0.62 ± 0.06, _P =_ 0.46, unpaired t-test) ( _Property 1: Cue Response_ , **Fig. 1b** ). Omission responses were significantly more negative in the exp. group than the ctrl. group for the CS+ (mean %dF/F ± SEM, exp. mice [ _n_ = 5]: -3.23 ± 0.44, ctrl. mice [ _n_ = 3]: -1.23 ± 0.11, _P =_ 0.015, unpaired t-test) but not the CS- (mean %dF/F ± SEM, exp. mice [ _n_ = 5]: -1.21 ± 0.12, ctrl. mice [ _n_ = 3]: -1.13 ± 0.08, _P =_ 0.67, unpaired t-test) ( _Property 2: Omission Dip_ , **Fig. 1b** ). Within the exp. mice, cue responses were larger to the CS+ than the CS- (mean %dF/F ± SEM, exp. mice [ _n_ = 5], CS+: 0.66 ± 0.33, CS-: -0.37 ± 0.23, _P =_ 0.0019, paired t-test) and omission responses were more negative (mean %dF/F ± SEM, exp. mice [ _n_ = 5], CS+: -3.23 ± 0.44, CS-: -1.21 ± 0.12, _P =_ 0.018, paired t-test). 

- j) Average GRABDA3m responses to unpredicted opto-stimulation (0-1 seconds after opto-stimulation) or predicted opto-stimulation (0-1 seconds after opto-stimulation on stimulated CS+ trials). Note the y-axis scale difference compared to panel i. Predicted opto-stimulation responses were smaller than unpredicted opto-stimulation responses (mean %dF/F ± SEM, exp. mice [ _n_ = 5], unpred: 19.52 ± 1.80, pred: 17.13 ± 2.01, _P =_ 0.0051, paired t-test) ( _Property 3: Expectation-dependent reduction of outcome response_ , **Fig. 1b** ). 

- k) Schematic (left) and example histology image (right) showing insertion of a four-shank Neuropixels 2.0 probe into VTA (see also **Extended Data Fig. 1e** ). 

- l) Schematic of antidromic optotagging. Red light delivery in lNAc generates dopamine release (green) as well as back-propagating action potentials which travel antidromically along dopamine axons to VTA dopamine neuron 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

cell bodies, where they are detected by the Neuropixels probe, marking the recorded neuron as a dopamine neuron that projects to lNAc. 

- m) Example antidromically optotagged dopamine neuron (see Methods for criteria defining optotagged neurons). 

- n) The response of four example antidromically optotagged lNAc-projecting VTA dopamine neurons to CS+ (omission trials; red) and CS- (black) (see also **Extended Data Fig. 2c** ). 

- o) The average response of all optotagged neurons to CS+ (omission trials) and CS- (mean ± SEM, _n_ = 43 neurons). Firing rate traces were smoothed and then z-scored using the mean and standard deviation of the firing rate trace in ITI periods (Methods). (see also **Extended Data Fig. 2d** ). 

- p) Difference in z-scored response between the CS+ (omission trials) and CS- (mean ± SEM, _n_ = 43 neurons). The cue period was defined as 0-0.5 seconds after odor onset, and the omission period was defined as 0-0.5 seconds after omission of opto-stimulation (1.5-2.0 seconds after odor onset); these are used for quantification in panel q. 

- q) The average cue and omission response (difference in z-score between CS+, on omission trials, and CS-, in the time windows defined in panel p) for all optotagged neurons. Points indicate neurons, and colors indicate mice. The four example neurons in panel n are labeled. At the single neuron level, cue responses were significantly greater than zero (mean z-score difference ± SEM [CS+ − CS-] = 0.13 ± 0.04, _n_ = 43 neurons, _P =_ 0.0017, t- − 

- test), and omission responses were significantly less than zero (mean z-score difference ± SEM [CS+ CS-] = - 0.19 ± 0.05, _n_ = 43 neurons, _P =_ 0.00054, t-test). These were marginally anti-correlated (Pearson’s 𝜌𝜌 = -0.29, _P =_ 0.06). In histograms, neurons with significant cue responses or omission dips are depicted with black bars, and non-significant neurons with open bars. 

## 103 **Opto-conditioning in lNAc generates a value-like signal in D1- but not D2-MSNs** 

104 To understand how opto-conditioning in lNAc generated TD error-like signals in dopamine 105 neurons, we used Neuropixels probes to record extracellular spiking activity in the striatum, on a subset of 106 late-training days in the same mice ( **Fig. 2a** ). We selected neurons with a positive response to either the 107 CS+ and CS- (Methods) and plotted their activity on omission trials. In contrast to the biphasic response 108 observed in dopamine neuron spiking ( **Fig. 1o,p** ) and dopamine release ( **Fig. 1g,h** ), striatal spiking was 109 positively enhanced to the CS+ relative to the CS- throughout the trial ( **Fig. 2b** , **Extended Data Fig. 4** ), 110 reminiscent of a “value”-like signal as opposed to the TD error-like patterns observed in dopamine 111 activity[42] . This change was observed specifically within lNAc (the stimulation site) and not dorsal striatum 112 (DS) ( **Fig. 2c** ), indicating that opto-conditioning was confined to the target region (lNAc). Selecting 113 neurons inhibited by either odor did not reveal a clear enhancement of inhibition to the CS+; if anything, 114 these neurons’ responses were also potentiated ( **Extended Data Fig. 4e** ), suggesting that the primary effect 115 of opto-conditioning was to positively enhance odor-evoked spiking in a subset of neurons. 

116 We next aimed to determine which striatal cell types contribute to the changes in striatal spiking 117 generated by opto-conditioning. The two primary striatal cell types are D1- and D2-MSNs, expressing the 118 D1 and D2 dopamine receptor, respectively. We used double transgenic mice to virally express a calcium 119 indicator (GCaMP8m) in lNAc D1- or D2-MSNs along with ChrimsonR in VTA dopamine neurons ( _n_ = 7 120 D1 mice, _n_ = 6 D2 mice; **Fig. 2d** , **Extended Data Fig. 5a,b** ; Methods). These mice then underwent the 121 same two-odor opto-conditioning paradigm as above. Consistent with asymmetric plasticity rules in D1122 and D2-MSNs[43–45] , phasic dopamine stimulation selectively potentiated D1-MSN but not D2-MSN 123 responses to preceding odor stimuli ( **Fig. 2e-i** , **Extended Data Fig. 5c-f** ). We conclude that the changes in 124 lNAc spiking activity ( **Fig. 2b** ) primarily reflect changes in D1-MSNs. 125 A key feature of a value-like signal is that it reflects a prediction of upcoming reward but does not 126 respond directly to reward itself. Consistent with this, D1-MSN odor responses gradually increased over 127 training ( **Fig. 2h** ), but D1-MSNs did not respond directly to dopamine release ( **Fig. 2h** , **Extended Data** 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 2** 

**==> picture [507 x 409] intentionally omitted <==**

**----- Start of picture text -----**<br>
Striatal spiking activity, omission trials (recorded on days 15-20)<br>a Neuropixels 1.0 b lNAc neurons c DS neurons<br>(acute insertion) excited by CS+ or CS- excited by CS+ or CS-<br>Optic fiber (n=177/415) (n=98/350)<br>1.6 Odor Stim. omission 1.6 Odor Stim. omission<br>1.2 CS+ 1.2 CS+<br>ChrimsonR CS- CS-<br>(dopamine DS 0.8 0.8<br>axons)<br>GRABDA3m lNAc 0.4 0.4<br>(lNAc)<br>0 0<br>DAPI GRABDA3m DiD -1 Time from odor onset (sec)0 1 2 3 4 5 -1 Time from odor onset (sec)0 1 2 3 4 5<br>Late training omission trials (days 11+)<br>d D1 mice: D2 mice:  Tac1-CreAdora2a-Cre [+/-] ;DAT-Flp [+/-] ;DAT-Flp [+/-] [+/-] e D1 mice (n=7) f D2 mice (n=6) g 2 *<br>Opticfiber D1 mouseExample D2 mouseExample 3 Odor Stim. omission 3 Odor Stim. omission 1.5<br>2 CS+CS- 2 CS+CS- 1<br>ChrimsonR 1 1<br>(dopamine 0.5<br>axons) 0 0<br>0<br>GCaMP8m -1 -1<br>(lNAc D1-<br>or D2-MSNs) DAPI GCaMP8m -1Time from odor onset (sec)0 1 2 3 4 5 -1Time from odor onset (sec)0 1 2 3 4 5 -0.5 D1 D2<br>mice mice<br>Development of odor responses over training and extinction j D1 and D2 MSN calcium signals respond k Putative TD computation<br>to red light delivery, but not dopamine itself underlying TD learning<br>h D1 mice i D2 mice D1 mice D2 mice<br>Novel odor Train Ext. Train Ext. No masking light D1-MSN spiking<br>response Unpredicted (value-like)<br>Late training Late training opto stim.<br>(days 11+) CS+ (days 11+)<br>CS-<br>TD Dopamine neuron spiking<br>(TD error-like)<br>Masking light<br>Trials (ticks mark days) Trials (ticks mark days)<br>1 sec<br>z-score z-score<br>z-score z-score (CS+ – CS-)<br>mean z-score, Odor Window<br>1 z<br>1 z<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 2:** Opto-conditioning in lNAc generates a value-like signal in D1- but not D2- MSNs. 

- a) Left: Schematic of Neuropixels 1.0 recording targeting lNAc during the opto-conditioning task. Right: Example histology image with lNAc (defined as 3.5-4.5 mm from brain surface) and dorsal striatum (DS; defined as 2-3 mm from brain surface) marked along the Neuropixels probe path. Scale bar = 1 mm. lNAc Neuropixels recordings were performed in the same mice as shown in Figure 1, on days 15-20 of training ( **Extended Data Fig. 1e** ). 

- b) Mean z-scored striatal spiking response of lNAc odor-responsive neurons to the CS+ (omission trials; red) and CS- (black). Lines and shaded areas show mean ± SEM over neurons ( _n_ = 177 odor-responsive neurons). Odorresponsive neurons were defined as those having a significantly elevated firing rate relative to baseline in any 1- second bin from 0-5 seconds after odor onset, to either the CS+ or the CS- (177/415 neurons; see Methods). Odor responses (defined as the average z-scored activity from 0-1 second after odor onset) of odor-responsive lNAc neurons were significantly greater for the CS+ than the CS-, at both the neuron and mouse level (mean z- score ± SEM, neurons: CS+ = 0.78 ± 0.13, CS- = 0.36 ± 0.05, _n_ = 177 neurons, _P =_ 6.2×10[-6] , sign-rank test; mice: CS+ = 0.75 ± 0.13, CS- = 0.29 ± 0.08, _n_ = 5 mice, _P =_ 0.032, t-test). 

- c) Same as panel b, but for DS neurons. Unlike lNAc neurons, odor-responsive DS neurons did not differ in their response to the CS+ versus the CS-, at the neuron or mouse level (mean z-score ± SEM, neurons: CS+ = 0.30 ± 0.06, CS- = 0.25 ± 0.04, _n_ = 98 neurons, _P =_ 0.41, sign-rank test; mice: CS+ = 0.45 ± 0.24, CS- = 0.30 ± 0.10, _n_ = 5 mice, _P =_ 0.34, t-test). 

- d) Left: Schematic of experimental approach to record from D1- and D2-MSNs during opto-conditioning. Using double transgenic mice, Flp-dependent ChrimsonR was expressed in VTA dopamine neurons and Credependent GCaMP8m was expressed in lNAc D1-MSNs (DAT-Flp x Tac1-Cre mice, i.e. “D1 mice”, _n_ = 7) or D2-MSNs (DAT-Flp x A2a-Cre mice, i.e. “D2 mice”, _n_ = 6). An optic fiber was implanted targeting lNAc, through which dopamine axons could be stimulated while recording bulk calcium signals from D1- or D2MSNs. Opto-stimulation was calibrated to water reward in separate DAT-Flp mice ( **Extended Data Fig. 5b** ). Right: Example histology images showing fiber placement in lNAc (arrows) and GCaMP8m expression. Scale bars = 1 mm. 

- e) Average z-scored bulk calcium response of D1-MSNs to CS+ (omission trials) and CS- in late training (days 11+) of the same opto-conditioning task as in **Fig. 1** ( _n_ = 7 D1 mice). For each mouse, there is one red line (CS+ response on omission trials) and one black line (CS- response). 

- f) Same as panel e, but for D2 mice ( _n_ = 6). 

- g) Average difference in z-score between CS+ (omission trials) and CS- for D1 mice (blue) and D2 mice (green) during odor delivery (0-1 seconds after odor onset). For D1 mice, this difference was greater than zero (marginally significant) (mean z-score ± SEM = 0.62 ± 0.25, _n_ = 7, _P =_ 0.0504, t-test), but for D2 mice it was not (mean z-score ± SEM = -0.02 ± 0.08, _n_ = 6, _P =_ 0.84, t-test), and the D1 odor response was significantly greater than the D2 odor response in a head-to-head comparison ( _P =_ 0.047, unpaired t-test). 

- h) Development of odor responses (average z-score GCaMP signal 0-1 seconds after odor onset) to CS+ (red) and CS- (black) in D1 mice over training (“train”) and extinction (“ext.”). Single trial responses were averaged in the given time window, concatenated across days, and smoothed with a Gaussian filter (S.D. = 15 trials). Thin lines represent individual mice; thick lines show the mean over mice. 

- i) Same as panel h, but for D2 mice. 

- j) D1- and D2-MSN calcium signals respond to red light delivery, but not dopamine itself. Top row: z-scored GCaMP responses to unpredicted opto-stimulation (shaded red area) in D1 mice (left) and D2 mice (right). Ten unpredicted opto-stimulation trials were delivered at the end of the opto-conditioning task each day ( **Extended Data Fig. 1e** ). The average response to these trials is shown, averaged first within day then across days for each mouse (mean z-score ± SEM, 0-1 sec after light onset: D1 mice = 0.26 ± 0.06, _n_ = 7, _P =_ 0.0062, t-test vs zero; D2 mice = 0.20 ± 0.09, _n_ = 6, _P =_ 0.071, t-test vs zero). Each thin line shows an individual mouse; thick lines and shaded areas show means ± SEM over mice. Bottom row: Several days after the completion of optoconditioning (including extinction sessions), a session was run in which unpredicted opto-stimulation was delivered while the recording rig was illuminated with two bright red lamps directed at the mouse’s eyes. The 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

response to unpredicted opto-stimulation was eliminated in both D1 and D2 mice (mean z-score ± SEM, 0-1 sec after light onset: -0.12 ± 0.09, _n_ = 7, _P =_ 0.24, t-test vs zero; D2 mice = -0.09 ± 0.06, _n_ = 6, _P =_ 0.22, t-test vs zero; paired t-test vs no masking light: _P =_ 0.0012, D1 mice; _P =_ 0.0096, D2 mice), indicating that these responses were visual rather than a response to dopamine itself. 

k) Putative TD computation underlying TD learning. Opto-conditioning in lNAc potentiates lNAc (but not DS) D1-MSN spiking to CS+ relative to CS-, generating a value-like signal reflecting a prediction of upcoming dopamine stimulation but not dopamine stimulation itself. Monophasic lNAc D1-MSN spiking activity undergoes a temporal difference transformation to produce biphasic TD error-like patterns of VTA dopamine spiking activity (and lNAc dopamine release) in response to the CS+. 

130 Together, these activity patterns are suggestive of a TD learning loop: Dopamine release gradually 131 potentiates the odor-evoked response in D1-MSNs (“value”); in turn, D1-MSNs stimulate lNAc-projecting 132 VTA dopamine neurons via a temporal difference transformation, generating a positive dopamine response 133 at onset and a negative omission dip at offset of their activity, closely recapitulating TD RPE ( **Fig. 2k** ). 

## 134 

## 135 

## **Activation of lNAc D1-MSNs drives lNAc dopamine release via a TD transformation** 

136 To directly test this idea, we asked whether activation of D1-MSNs alone could generate the TD 137 error-like patterns of dopamine activity observed in our opto-conditioning task, and more generally, whether 138 D1-MSNs drive dopamine release according to a temporal difference transformation—the core computation 139 in TD learning (red box, **Fig. 1a** ). We prepared mice for simultaneous opto-stimulation of lNAc D1-MSNs 140 with photometric recording of lNAc dopamine release and Neuropixels recordings of lNAc D1-MSNs ( **Fig.** 141 **3a** ) and designed 7 opto-stimulation patterns that generate both qualitative and quantitative predictions for 142 a TD error-like response ( **Fig. 3b** ): (1) A 1 second pulse train at 20 Hz, (2) a 2 second pulse train at 20 Hz, 143 (3) an upward ramp from 0 to 40 Hz, (4) a downward ramp from 40 to 0 Hz, and (5-7) 3 second pulse trains 144 at 5, 10, and 20 Hz (all light pulses 1 ms at 40 mW/mm[2] ). 145 The simulated TD error of these 7 patterns is shown in the right of **Fig. 3b** , with the temporal 146 discount factor 𝛾𝛾 ranging from 1 (green; a pure derivative) to 0.1 (blue) in units of discount/sec. As has 147 been previously noted[5,21,22] , TD error is similar (but not identical) to a time derivative. Indeed, in the 148 schematics in **Fig. 3b** , the TD error shows several qualitative derivative-like features that are shared 149 between TD in general (𝛾𝛾≤ 1) and the strict derivative (𝛾𝛾 = 1): (1) Transient positive/negative responses 150 to the onset/offset of stimulation, which scale with the intensity of stimulation (patterns 5-7), (2) A 151 prominent negative response to the offset of pattern 3, with a smaller positive response during the ramp-up 152 phase, and (3) A prominent positive response to the onset of pattern 4, followed by a prolonged negative 153 response as stimulation ramps down. 

154 Remarkably, actual dopamine responses to D1-MSN stimulation displayed all of these derivative155 like features ( **Fig. 3c** , right). In contrast, D1-MSNs responded faithfully to the stimulation patterns 156 themselves ( **Fig. 3c** , left; **Extended Data Fig. 6a** ). Notably, even though striatal MSNs are inhibitory 157 neurons and directly project to VTA, the initial dopamine response was excitatory, especially for stimulation 158 patterns with a rapid onset. This counterintuitive response pattern supports the existence of a derivative159 like transformation between lNAc D1-MSNs and lNAc dopamine release, exactly as needed to implement 160 TD learning ( **Fig. 1a** ). 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 3** 

lNAc D1-MSNs drive lNAc dopamine release via a TD-like transformation 

**==> picture [506 x 640] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b Stimulation patterns(pulse trains) Stimulation patterns(smoothed) TD error γ c lNAc D1-MSNsOptotagged dopaminelNAc<br>Tac1-Cre [+/-]  mouse (discount/sec):<br>Optic Neuropixels 1.0 1 1 sec. square(20 Hz) 1 (derivative)0.7<br>fiber (acute insertion) 0.4<br>0.1<br>GRABDA3m 2 2 sec. square<br>(VTA axons) (20 Hz)<br>ChrimsonR<br>(lNAc D1--MSNs) 3 Upwardramp<br>4 Downward<br>ramp<br>5 3 sec. square<br>(5 Hz)<br>6 3 sec. square<br>(10 Hz)<br>7 3 sec. square<br>(20 Hz)<br>3 seconds -1 0 1 2 3 4 -1 0 1 2 3 4 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5<br>Time from stim. (sec)<br>Time from stim. (sec)<br>Modeling the TD transformation as an LTI system<br>d Linear time-invariant (LTI) e Stimulation patterns f 1 n = 2 mice Stim. patterns<br>1 2 3 4 5 6 7<br>system identification analysis D1-MSNs<br>Input 30 D1-MSNs<br>(e.g. D1-MSNs) 2010 Estimatedfilter 0 TD D1-MSNs<br>* 0 0 1 2 3 4 Dopamine<br>Filter Model order<br>(fit to data) Predict 42 DopaminePrediction g 1<br>0<br>Output -2 0 1 2<br>(e.g. dopamine) Data -4 sec 0<br>Prediction 2 sec<br>TD-like responses of optotagged lNAc-projecting VTA dopamine neurons<br>h i 1 2 3 4 5 6 7 j<br>0.2 Stim.<br>Tac1-Cre [+/-] ;DAT-Flp [+/-]  mouse Stimulation patterns Estimated patterns<br>Optic Neuropixels 2.0 filter 0.1 Dopamine<br>fiber (acute insertion) TD neurons<br>Dopamine neurons (mean) 0<br>0 1 2 3 4<br>ChR2 Prediction Model order<br>(dopamine ***<br>axons) k<br>ChrimsonR 0 1 2 0.2<br>(lNAc D1- 2 sec sort sec 0.1<br>-MSNs) ChR2 0.5<br>(dopamine neurons) 0<br>0<br>-0.5<br>Extracting γ from neural responses to D1 stimulation<br>l (transfer function, Laplace domain):TD LTI model m n A biphasic filter approximates TD o Bootstrapped dopamine neurons4<br>100<br>= − + ln1 TD − 2 8060 MedianMasset et al. 2025 P N * ( ≈ P ( − ( N −1 ) 32<br>40<br>scaling smoothing 1<br>20 Ratio of positive and negative lobes sets γ<br>0 0<br>Fit model to data to extract gamma 0 0.5γ (discount/sec)1 1.5 2 2.5 3 NP ~ γ 0.6 0.8 P/N1 1.2 1.4<br>Derivative TD<br>Derivative TD<br>5 z<br>20 spikes/sec<br>2CV R<br>spikes/sec<br>2<br>z-score CV R<br>2CV R<br>1 z<br>2CV R<br>Dopamine neurons z-score<br> (discount/sec)γ<br>Count (bootstrap)<br>( (<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- **Figure 3:** Activation of lNAc D1-MSNs drives lNAc dopamine neurons via a temporal difference transformation, suggesting a circuit-level origin of temporal discounting. 

- a) Experimental approach. GRABDA3m was expressed pan-neuronally in the VTA and ChrimsonR was expressed in D1-MSNs in lNAc using _Tac1-Cre[+/-]_ mice. An optic fiber was implanted at an angle targeting lNAc allowing for acute insertion of a Neuropixels probe as in **Fig. 2a** . This enabled simultaneous stimulation of lNAc D1MSNs, electrophysiological recording of optotagged lNAc D1-MSNs, and photometric recording of lNAc dopamine release from VTA axons at the same site, such that the transfer function from D1-MSN activity to lNAc dopamine release could be directly quantified. 

- b) _Left:_ The 7 opto-stimulation patterns used in the experiment (trains of 1 ms red light pulses at 40 mW/mm[2] ). _Middle:_ Smoothed pulse trains. _Right:_ The TD equation applied to the smoothed pulse trains, with varying 𝛾𝛾. When 𝛾𝛾= 1, TD becomes a pure derivative. For 𝛾𝛾< 1, TD deviates from a derivative, most notably in its negative steady-state response (e.g. Patterns 1, 2, 7). 

- c) The responses of optotagged lNAc D1-MSNs (left) and lNAc dopamine (right) to the 7 stimulation patterns ( _n_ = 2 mice). Individual D1-MSNs were averaged within mice ( _n_ = 6, 10 D1-MSNs in mouse 1, 2 respectively). Faint lines show individual mice, solid lines show the average over mice. Whereas D1-MSN activity closely followed the stimulation patterns themselves, dopamine release qualitatively resembled TD error of the stimulation patterns, including a negative steady-state response, which distinguishes TD from a pure derivative. 

- d) Schematic of linear time-invariant (LTI) systems identification analysis, which models an input-output system as a linear filter (also called the impulse response) convolved with the input to produce the output (Methods). 

- e) LTI model fit to data from panel c. _Top_ : Average lNAc D1-MSN responses to the 7 stimulation patterns (red; averaged over _n_ = 2 mice). _Bottom_ : The average response of lNAc dopamine to the 7 stimulation patterns (green; averaged over _n_ = 2 mice) and the LTI model fit (black) predicting lNAc dopamine (output) from optotriggered D1-MSN activity (input) (cross-validated [CV] R[2] = 0.81). _Right:_ Estimated filter of LTI model (Methods). 

- f) Cross-validated R[2] for LTI models of varying order (number of zeros; Methods), predicting D1-MSN activity from stimulation patterns (red) or dopamine activity from D1-MSN activity (green). Individual lines show individual mice ( _n_ = 2). The TD equation is order 1 (Methods; panel l). Consistent with a TD transformation between D1-MSNs and dopamine, predicting dopamine from D1-MSNs required a minimum model order of 1, and higher model orders did not improve performance. In contrast, an order 0 model was sufficient to predict D1-MSN activity from stimulation patterns. 

- g) A derivative LTI model performed worse than a TD LTI model at predicting dopamine from D1-MSNs. The derivative model is equivalent to the TD LTI model with 𝛾𝛾 fixed at 1 (Methods). 

- h) Experimental design to record from optotagged lNAc-projecting VTA dopamine neurons with Neuropixels probes while optogenetically stimulating lNAc D1-MSNs. 

- i) _Top_ : The 7 stimulation patterns, concatenated. _Middle:_ Average dopamine neuron response (z-score) to 7 stimulation patterns (green) and the LTI model fit (black) predicting dopamine from stimulation patterns. Note the qualitative similarity to the bottom of panel e (CV R[2] = 0.69). _Bottom:_ Heatmap of activity of single optotagged lNAc-projecting VTA dopamine neurons, sorted by the response to pattern 7 ( _n_ = 55 neurons). _Right:_ Estimated filter of LTI model fit to average dopamine neuron spiking activity. Note the temporally sharper shape compared to panel e, befitting the higher temporal resolution of electrophysiological recording. 

- j) Same as panel f, but for models predicting single optotagged dopamine neuron activity from stimulation patterns. Lines and error bars indicate mean ± SEM ( _n_ = 55 neurons). 

- k) Same as panel g, but for models predicting single optotagged dopamine neuron activity from stimulation patterns. *** _P <_ 0.001, paired t-test ( _n_ = 55 neurons). 

- l) Schematic describing how the temporal discount factor 𝛾𝛾 can be extracted from dopamine responses to D1MSN stimulation using an order-1 LTI model (Methods). 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- m) Histogram of estimated 𝛾𝛾 from bootstrapped optotagged dopamine neuron population activity (1000 bootstraps; Methods). The median bootstrapped estimate (𝛾𝛾� = 0.53) closely matched the estimate of 𝛾𝛾 from a previously published paper using a cued delay task (𝛾𝛾� = 0.56, Masset et al. 2025[47] ). 

- n) Schematic demonstrating how convolution with a biphasic filter approximately implements a TD transformation, and the intuition for why the ratio of the filter’s positive and negative lobes (P and N respectively) should set the temporal discount factor, 𝛾𝛾. 

- o) The ratio of the positive and negative lobes of the fit impulse response (P/N) versus the parameter 𝛾𝛾 of the LTI fit estimated as in panel l. Green points show individual bootstrapped estimates (Methods) and the black line shows an exponential fit. 

161 While TD error is derivative-like, it deviates from a derivative when 𝛾𝛾 < 1, most prominently in the 162 steady-state response to sustained stimulation: The steady-state response is zero for 𝛾𝛾 = 1 (derivative) but 163 negative for 𝛾𝛾< 1. Dopamine responses better matched TD, with negative steady state responses that scaled 164 with stimulus intensity ( **Fig. 3c** ). Computationally, this key distinction gives the TD algorithm its preference 165 for current over future rewards. These data raise the possibility that the temporal discount parameter 𝛾𝛾 could 166 be set by a neural circuit mechanism between D1-MSNs and dopamine neurons—a possibility we explore 167 in greater depth below. 

- 168 

- 169 **Capturing the TD transformation as convolution with a biphasic linear filter** 

170 In theory, a TD transformation can be viewed as convolution with a _biphasic filter,_ which applies 171 positive weights to recent input, negative weights to preceding input, and sums these to generate the output 172 ( **Fig. 3n** )[25] . To describe our results quantitatively, we therefore used linear time-invariant (LTI) systems 173 identification analysis, a standard approach in engineering[48] , to estimate the linear filter that best captures 174 the transformation from an input (e.g. D1 MSN spiking) to an output (e.g. lNAc dopamine release) ( **Fig.** 175 **3d** ) (Methods). 

176 Whereas the best-fit filter from stimulus to D1 MSN spiking resembled a delta function, scaling 177 the input to produce the output ( **Extended Data Fig. 6d** ), the best-fit filter from D1 MSN spiking to 178 dopamine release was biphasic, with a rapid positive component followed by a delayed negative 179 component, thus implementing an approximate temporal difference ( **Fig. 3e** ; order 1 LTI model; Methods). 180 The LTI models accurately predicted held-out data for both transformations (cross-validated R[2] : stimulation 181 patterns → D1-MSNs = 0.95, D1-MSNs → dopamine release = 0.81). These results argue that our data can 182 be adequately understood as the result of a linear system implementing a TD transformation between D1183 MSNs and dopamine release. 

184 To examine how well the dopamine response matches TD as opposed to more complex models, we 185 fit LTI models of varying order, using a standard model formulation which assumes a particular functional 186 form of the filter (Methods)[48] . Briefly, in this formulation the 𝑛𝑛th order LTI model is composed of 𝑛𝑛 TD 187 transformations, applied sequentially, followed by smoothing and scaling. Each TD transformation is given 188 by convolution with the “TD filter,” ℎ𝑇 (𝑡𝑡): 

189 

ℎ𝑇 (𝑡𝑡) = 𝛿𝛿(𝑡𝑡) + ln 𝛾𝛾𝛿𝛿(𝑡𝑡) 

190 Where 𝛿𝛿(𝑡𝑡) and 𝛿𝛿(𝑡𝑡) are the Dirac delta function and its derivative, respectively. Convolving an input 𝑉𝑉(𝑡𝑡) 191 with this filter generates an output 𝑉𝑉[̇ ] (𝑡𝑡) + ln 𝛾𝛾𝑉𝑉(𝑡𝑡) , which is exactly the continuous form of the TD 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

192 equation[21] . The TD LTI model is order 1: It applies exactly 1 TD transformation, followed by smoothing 193 and scaling. In contrast, the zeroth order model applies smoothing and scaling but lacks a TD 194 transformation, whereas higher order models apply multiple TD transformations before smoothing and 195 scaling, enabling higher order derivatives of the input to influence the output. 

196 To capture the transformation from D1-MSNs to dopamine release, an order 1 LTI model was 197 required, but higher order models did not improve performance (green lines, **Fig. 3f** ). In contrast, a zeroth 198 order LTI model was sufficient to capture the transformation from the stimulation patterns to D1-MSNs 199 (red lines, **Fig. 3f** ). This tightens the link between dopamine responses and the TD equation: simpler models 200 are insufficient, and more complex models are not needed. 201 Next, we used the LTI framework to demonstrate that dopamine responses are better fit by the TD 202 equation than by a pure derivative. We refit the order 1 LTI model while fixing 𝛾𝛾 = 1, thus implementing a 203 pure derivative, as ln(1) = 0. This model performed substantially worse on held-out data than the order 1 204 LTI model in which 𝛾𝛾 was free to vary ( **Fig. 3g** ). 205 The pattern of dopamine results was replicated in a larger cohort without D1-MSN recordings, 206 receiving only patterns 1-4 ( _n_ = 13 mice; **Extended Data Fig. 6e,h,k** ), and no dopamine responses were 207 observed in mice with tdTomato instead of ChrimsonR in D1-MSNs ( _n_ = 6 mice; **Extended Data Fig.** 208 **6f,i,l** ), ruling out optical artifacts or visual responses. Mice with GFP instead of GRABDA3m in VTA axons 209 showed slow biphasic fluctuations in GFP fluorescence following opto-stimulation, potentially reflecting a 210 hemodynamic response, but GFP signals were small compared to GRABDA3m ( _n_ = 3 mice; **Extended Data** 211 **Fig. 6g,j,m** ). 

## 212 

## 213 **TD-like response in optotagged lNAc-projecting VTA dopamine neurons** 

214 To gain insight into the TD computation at the level of single neurons in the VTA and better estimate 215 the rapid dynamics of the dopamine response, we recorded spiking signals of antidromically optotagged 216 lNAc-projecting VTA dopamine neurons while stimulating lNAc D1-MSNs with the same 7 stimulation 217 patterns ( **Fig. 3h** ). The same TD-like patterns as in **Fig. 3c** were observed in dopamine spiking activity ( **Fig.** 218 **3i** ), well-captured by a biphasic filter with a sharper time course (cross-validated R[2] = 0.69; **Fig. 3i** , right). 219 Like photometry signals, single dopamine neurons required an order 1 LTI model, but not higher ( **Fig. 3j** ), 220 and were better fit by TD than a pure derivative model ( **Fig. 3k** ). The latency of the onset of the excitatory 221 response to pattern 4 was less than 50 ms, and the response peaked between 50 and 100 ms ( **Extended** 222 **Data Fig. 6c** ). Importantly, these data localize the TD-like transformation downstream of D1-MSN spiking 223 but upstream of VTA DA neuron spiking, and constrain the time course of activation, narrowing down 224 potential mechanisms. 

225 

## 226 **Extracting the temporal discount parameter** 𝜸𝜸 **from dopamine neuron responses to D1-MSN** 227 **stimulation** 

228 The LTI modeling framework allows us to extract the temporal discount parameter 𝛾𝛾 directly from 229 dopamine responses to D1 stimulation ( **Fig. 3l** ). We derived an exact mathematical relationship between 𝛾𝛾 230 and a parameter of the LTI model, namely 𝛾𝛾= 𝑒𝑒[−𝜎𝜎] , where 𝜎𝜎 is the zero of the order 1 LTI model fit 231 (Methods). Bootstrapped estimates of 𝛾𝛾 from optotagged dopamine neurons closely matched a previous 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 4** 

**==> picture [410 x 394] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>muscimol Trial<br>or saline optic fiber frequency: Water (90%)<br>(VTA) Odor A (CS+)<br>10/21 Omission (10%)<br>10/21 Odor B (CS-) Nothing (100%)<br>1/21 Unpredicted water<br>lNAc<br>Some<br>Novel odor (~1/40 trials)<br>sessions:<br>0 0.5 1 1.5 2<br>GCaMP6f in dopamine neurons<br>Time (sec)<br>c Example mouse (MC193) d All mice (n = 6)<br>SALINE MUSCIMOL SALINE MUSCIMOL<br>20 Odor Water Odor Water 20 Odor Water Odor Water Unpredicted<br>reward<br>CS+,<br>10 10<br>rewarded/<br>unrewarded<br>0 0 CS-<br>-2 0 2 4 6 -2 0 2 4 6 -2 0 2 4 6 -2 0 2 4 6<br>sec sec sec sec<br>e Unpredicted Predicted Rewarded Reward Unrewarded Novel<br>Reward Reward Odor Omission Odor Odor<br>35 n.s. ** ** n.s. *** n.s.<br>Mouse:<br>30 MC190<br>MC191<br>25<br>MC193<br>20 MC194<br>MC195<br>15 MC196<br>10<br>5<br>0<br>-5<br>-10<br>sal mus sal mus sal mus sal mus sal mus sal mus<br>%dF/F %dF/F<br>%dF/F<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- **Figure 4:** lNAc contributes a value-like signal to VTA dopamine neuron activity. 

- a) Mouse preparation. GCaMP6f was expressed transgenically in dopamine neurons using _DAT-Cre[+/-] ;Ai148[+/-]_ mice ( _n_ = 6). An optic fiber was implanted targeting the VTA. After training in a classical conditioning task (panel b), muscimol or saline was injected into the lNAc on alternating days. 

- b) Classical conditioning task design. 

- c) Average VTA dopamine neuron calcium response to task events during example saline (left) and muscimol (right) sessions from the same mouse. Under muscimol, the response to the CS+ decreased and the response to the predicted reward increased, whereas the response to unpredicted reward remained relatively unchanged, consistent with lNAc signaling the reward expectation (value) associated with the CS+, and VTA dopamine neurons responding as the TD error of this value. Note that the response to the CS- also decreased, which may reflect generalization of value across odor stimuli within lNAc (e.g. the response to the CS- was positive in **Fig. 2b** and for some mice in **Fig. 2e** ). 

- d) Same as panel c, but averaged over mice ( _n_ = 6). Lines with shaded areas indicate mean ± standard error over mice for each trial type. 

- e) Quantification of the traces in panel d. Points indicate the maximum (unpredicted reward, predicted reward, rewarded cue, novel odor) or minimum (reward omission, unrewarded cue) of the average %dF/F trace within a 1-second window following the given task event within individual sessions. Lines connect the average saline and average muscimol session for each mouse. Colors indicate mice. Stars indicate the significance of the injection type coefficient (saline vs. muscimol) in a linear mixed effect model with a random effect per mouse. Muscimol increased predicted reward responses (estimated muscimol coefficient [%dF/F] ± SEM = 5.47 ± 1.45, _n_ = 26 sessions, _P =_ 0.0013); decreased CS+ responses (-2.30 ± 0.67, _n_ = 26 sessions, _P =_ 0.0029); and decreased CS- responses (-0.93 ± 0.22, _n_ = 26 sessions, _P =_ 0.00046), but did not significantly affect unpredicted reward responses (-0.73 ± 2.23, _n_ = 26 sessions, _P =_ 0.75), reward omission responses (-0.21 ± 0.58, _n_ = 26 sessions, _P =_ 0.73), or novel odor responses (-0.28 ± 1.21, _n_ = 21 sessions, _P =_ 0.82). *** _P <_ 0.001, ** _P <_ 0.01, * _P <_ 0.05, n.s. Not Significant. 

232 estimate, measured in mice performing a cued delay task (𝛾𝛾� = 0.53 discount/sec in our data, 𝛾𝛾� = 0.56 233 discount/sec in Masset et al.[47] ; **Fig. 3m** ). 𝛾𝛾 in the LTI model is linked to the ratio of the positive and negative 234 lobes of the impulse response (P/N) via an exponential relationship ( **Fig. 3n,o** ). This points to the relative 235 magnitude and timing of the net-excitatory and net-inhibitory components of the dopamine response to D1 236 MSN activation as a key determinant of 𝛾𝛾, grounding a higher order cognitive parameter (the time horizon 237 of reward preference) in a concrete neural circuit mechanism. 

- 238 

239 **lNAc contributes a value-like signal to VTA dopamine** 

240 Because these experiments relied exclusively on artificial paradigms, we next asked whether lNAc 241 contributes to dopamine TD RPE signaling in tasks with natural rewards. GCaMP6f was expressed 242 transgenically in dopamine neurons by crossing _DAT-Cre_[+/-] and _Ai148_[+/+] mice. We then prepared mice for 243 injection of muscimol (a GABAA receptor agonist) or saline into the lNAc with photometry recording in 244 VTA ( **Fig. 4a** ). We chose to record somatic rather than axonal calcium signals because muscimol may 245 directly inhibit dopamine axons, which express GABA receptors[49] . 

246 Mice were water-deprived and trained in a classical conditioning task in which one odor (CS+) was 247 associated with delivery of a natural reward (4 𝜇 water; delivered on 90% of CS+ trials) and another odor 248 (CS-) was associated with nothing ( **Fig. 4b** ). In addition, unpredicted rewards were delivered without a 249 preceding odor on ~5% of trials. After several days of training, we injected muscimol or saline into lNAc 

16 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

250 on alternating days while recording dopamine neuron calcium signals in the VTA. Muscimol dramatically 251 increased calcium responses to predicted rewards, but not unpredicted rewards, and reduced responses to 252 the CS+ ( **Fig. 4c-e, Extended Data Fig. 7** ). This pattern is consistent with a suppression of the reward 253 expectation (value) associated with the CS+: the reward expectation of the CS+ decreases, so the cue 254 response is suppressed, and at the same time the predicted (but not unpredicted) reward becomes more 255 surprising, and so the reward response increases. 256 We tested for the specificity of this effect to odor value by also delivering novel odors in a subset 257 of mice (4/6 mice). In contrast to the reduction in the dopamine response to the CS+, the response to novel 258 odors did not change ( **Fig. 4e** ), arguing for a specific effect on odor value rather than novelty. 259 Because dopamine activity can reflect movements[50–52] , we analyzed face videos to check whether 260 muscimol changed odor- and reward-triggered movements ( **Extended Data Fig. 8** ). Under muscimol, mice 261 discriminated CS+ and CS- odors, consumed rewards, and detected novel odors ( **Extended Data Fig. 8b** ), 262 suggesting that muscimol did not eliminate animals’ ability or motivation to perform the task. We did, 263 however, detect changes in total mouth movement during the CS+ and after rewards and odor cues 264 ( **Extended Data Fig. 8b** ), but muscimol similarly increased mouth movements to both predicted and 265 unpredicted rewards, whereas VTA dopamine neuron calcium dramatically increased to predicted but not 266 unpredicted rewards ( **Fig. 4e** ), indicating that movements cannot explain the main pattern of our results. 267 Together, these results demonstrate that lNAc contains a reward expectation (value)-like signal that 268 contributes to TD RPE dopamine activity during classical conditioning with natural rewards, consistent 269 with the TD error-like response of dopamine neurons to opto-stimulation of lNAc D1-MSNs. 270 

## 271 

## **The temporal difference computation is a widespread feature of striatal-dopamine circuitry** 

272 Dopamine neurons have heterogenous functions depending in part on their projection 273 target[33,39,50,53–55] , and may not all signal TD errors or participate in value learning. To investigate whether 274 the TD computation identified here generalizes to striatal dopamine systems beyond lNAc, we stimulated 275 D1-MSNs in lNAc, dorsomedial striatum (DMS), and dorsolateral striatum (DLS) while recording 276 dopamine release in each site ( **Fig. 5a,b** , **Extended Data Fig. 9** ). To our surprise, the estimated impulse 277 response for each stimulation site was biphasic ( **Fig. 5c** ), indicating that the temporal difference 278 transformation is a ubiquitous feature of the circuitry connecting striatal D1-MSNs to midbrain dopamine 279 neurons. However, the parameters of the impulse response, including the estimated temporal discount factor 280 𝛾𝛾, varied by striatal subregion, with the estimated 𝛾𝛾 being closer to 1 for DMS and DLS than lNAc (though 281 not significantly so; **Fig. 5d,e** ). This points to a unified computational account of phasic dopamine’s role in 282 learning as a prediction error machine, with parameters and input/output spaces that vary by striatal 283 subregion[56–58] . 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Figure 5** 

**==> picture [470 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
Dopamine recording site<br>a Optic fibers AP = 1.3 mm AP = 0.5 mm b Stim lNAc DMS DLS<br>lNAc DMS DLS<br>Patterns:<br>DMS<br>1 n=13 n=7 n=6<br>lNAc DLS 2<br>3 n=7 n=7 n=2<br>Tac1-Cre mouse   DAPI ChrimsonR<br>GRABDA3m (VTA/SNc axons) 4<br>ChrimsonR (D1-MSNs) n=6 n=2 n=6<br>Power = 1 mW<br>1s<br>lNAc<br>DMS<br>D1 MSN stimulation site<br>DLS<br>1z<br>**----- End of picture text -----**<br>


**==> picture [373 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
P N P ~<br>Dopamine recording site N<br>c<br>lNAc DMS DLS d e<br>2 n.s. **<br>1<br>1.5 0.8<br>0.6<br>1<br>0.4<br>0.5<br>0.2<br>0<br>0<br>0 1 2 lNAc DMS DLS lNAc DMS DLS<br>sec<br>lNAc<br>P/N<br>DMS<br>Time of minimum (sec)<br>D1 MSN stimulation site<br>DLS<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Figure 5:** The temporal difference computation is a widespread feature of striatal-dopamine circuitry. 

- a) Experimental design (left) and example histology images (right). GRABDA3m was expressed in VTA and SNc and ChrimsonR was expressed in D1-MSNs in lNAc, dorsomedial striatum (DMS), and/or dorsolateral striatum (DLS). Optic fibers were implanted targeting lNAc, DMS, and/or DLS. A mirrored fiber was used in DLS to restrict light delivery to DLS. Scale bar = 1 mm. 

- b) Z-scored striatal dopamine responses to one stimulation pattern (Pattern 4, sharp onset followed by gradual downward ramp) (for responses to all patterns see **Extended Data Fig. 9** ). The 3 x 3 matrix displays responses by dopamine recording site (columns) and D1 MSN stimulation site (rows). Each entry in the matrix contains a different number of mice ( _n_ = 13 mice total). Two mice had fibers in all three regions; the others had fibers in one or two of the three. All mice had fibers in lNAc. Gray lines = individual mice, black lines = mean over mice. Note the biphasic responses along the diagonal of the matrix, indicating a temporal difference computation for all three stimulation sites. 

- c) Estimated impulse responses from LTI model predicting dopamine responses from stimulation patterns, as in **Fig. 3** , for all nine pairs of stimulation and recording sites. Gray lines = individual mice, black lines = mean over mice. Y-axis units are arbitrary. 

- d) Ratio of the positive and negative areas of the impulse response (P/N, a proxy for 𝛾𝛾; **Fig. 3n,o** ) for lNAc, DMS, and DLS (when stimulating D1-MSNs in the same site; the diagonal of panel c). While estimated discount factors were closer to 1 for DMS and DLS compared to lNAc, this was not statistically significant (mean P/N ± SEM: lNAc = 0.50 ± 0.07, _n_ = 13 mice; DMS = 0.94 ± 0.22, _n_ = 7 mice; DLS = 0.65 ± 0.18, _n_ = 6 mice; _P =_ 0.23, linear mixed effects model). Gray points = individual mice, black points and error bars = means ± SEM over mice. 

- e) Minimum time point of estimated impulse response for lNAc, DMS, and DLS (when stimulating D1-MSNs in the same site). Minimum time points were closer to zero for dorsal striatal areas, indicating faster dynamics[59,60] (mean 𝑡𝑡𝑚 𝑚𝑚 ± SEM [sec]: lNAc = 0.52 ± 0.03, _n_ = 13 mice; DMS = 0.49 ± 0.08, _n_ = 7 mice; DLS = 0.24 ± 0.05, _n_ = 6 mice; _P =_ 0.01, linear mixed effects model). Gray points = individual mice, black points and error bars = means ± SEM over mice. * _P <_ 0.05, n.s. Not Significant. 

284 **Discussion** 

285 Collectively, our experiments reveal how key TD learning operations are accomplished by the 286 circuitry connecting lNAc-projecting dopamine neurons and lNAc D1-MSNs _:_ phasic lNAc dopamine 287 release selectively potentiates lNAc D1-MSN responses to preceding sensory stimuli, and D1-MSNs drive 288 VTA dopamine neurons spiking and lNAc dopamine release via a TD transformation, generating TD error289 like activity (a “minimal TD learning loop”; **Extended Data Fig. 10a** ). As a counterpoint to recent 290 arguments over whether TD RL is a good description of dopamine’s role in learning at the behavioral 291 level[15–18] , these results demonstrate that TD error calculations are hard-wired into the dopamine system at 292 the microcircuit level. 

293 While the response of dopamine neurons to D1-MSN stimulation is derivative-like, it is not a strict 294 derivative, but instead more closely matches the temporal difference equation 𝛾𝛾𝑉𝑉(𝑆𝑆𝑡𝑡) −𝑉𝑉(𝑆𝑆𝑡𝑡−1), with 𝛾𝛾 < 295 1. This is revealed most clearly by the response to long pulse trains (patterns 5-7, **Fig. 3c** ), to which the 296 dopamine response plateaus at a negative value that becomes more negative as stimulation frequency 297 increases. In the LTI framework, this corresponds to a biphasic impulse response with total negative area 298 (N) greater than total positive area (P). The ratio of these areas (P/N) determines the temporal discount 299 parameter 𝛾𝛾 of the TD algorithm ( **Fig. 3n,o** ). 

295 

297 298 299 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

300 A natural extension of these findings is that the same neural circuit mechanism underlies the 301 cognitive phenomenon of temporal discounting—the tendency for animals and humans to prefer immediate 302 over future rewards. The time horizon of this preference—set by 𝛾𝛾—is a fundamental aspect of learning 303 and decision making with implications for human health and economic choices[13,61–64] . For instance, discount 304 rates for money correlate with individuals’ choices to engage in unhealthy behaviors, such as smoking[63] 305 and excessive alcohol consumption[65] . Yet despite its importance, the biological basis of 𝛾𝛾 is unknown. Our 306 findings suggest a compelling mechanism: 𝛾𝛾 is set at the level of individual dopamine neurons by the 307 balance of the net-excitatory and net-inhibitory components of the circuit connecting D1-MSNs to VTA. 308 This could explain why 𝛾𝛾 is a conserved property of single dopamine neurons across tasks[47] and potentially 309 explain the diversity of temporal discounting factors across striatal subregions[59,66] and across individual 310 animals in healthy and pathological conditions[63] . Notably, at the behavioral level temporal discounting is 311 not exponential, as would be the case for a TD algorithm with a single discount factor, but hyperbolic, with 312 a special status given to the current moment in time[12,67,68] (but see[69] ). A reservoir of dopamine neurons with 313 private 𝛾𝛾, each set individually by the balance the of positive and negative lobes of its impulse response to 314 D1-MSN stimulation ( **Extended Data Fig. 10b** ), could combine to produce hyberbolic discounting on 315 aggregate[47,70] . Further experiments linking the shape of the impulse response described here to 316 neurophysiological and behavioral data in time discounting tasks would be needed to test this hypothesis 317 ( **Extended Data Fig. 10c** ). 

318 The TD transformation was a widespread feature of circuitry connecting D1-MSNs to dopamine 319 release across both lNAc and dorsal striatum, revealing a conserved learning motif across striatal 320 subsystems, despite their distinct roles in behavior[33,58] . This suggests that a single conserved TD-learning 321 mechanism may have been repurposed by evolution to learn predictive maps across different input 322 spaces[58,71] and timescales[59,66] . Consistent with this, while the biphasic shape of the learned filter was 323 conserved across the striatal areas we tested, the time resolution differed (time to minimum; **Fig. 5e** ). The 324 region-specific filters are likely shaped by a combination of both dopamine reuptake dynamics, which vary 325 systematically across the striatum[60] , and circuit dynamics between striatum and dopamine neurons. Further 326 experiments involving projection-specific electrophysiological recording of the type developed here would 327 be needed to distinguish between these alternatives. 328 Our experiments did not exhaustively cover striatal subregions, leaving several intriguing targets 329 for future work, notably the medial nucleus accumbens, where dopamine release has value-like properties[39] 330 and the tail of the striatum, where dopamine may contribute to learning to predict threatening or salient 331 outcomes[35,57,72] or act as a value-neutral teaching signal[73] . If the hardwired TD computation extends to these 332 regions, this would suggest dopaminergic learning follows an analogous algorithm despite notably different 333 dopamine activity patterns. Outside striatum, the amygdala receives strong dopamine inputs from VTA, but 334 appears to play a qualitatively distinct role in reinforcement learning compared to nucleus accumbens, with 335 amygdala being more important for the initial acquisition of a behavioral response to motivationally salient 336 cues (both rewarding and aversive)[74] , and nucleus accumbens subsequently refining the quantitative value 337 estimate associated with these cues[75] . Distinct computations between amygdala/striatal neurons and 338 dopamine neurons could help to explain this difference. 339 What are the possible biological mechanisms by which the temporal difference is computed? By 340 recording lNAc D1-MSN optotagged neurons, antidromically optotagged lNAc-projecting VTA dopamine 341 neurons, and lNAc dopamine photometry signals in the same paradigm, we show that the calculation occurs 342 between the spiking of lNAc D1-MSNs and the spiking of lNAc-projecting VTA dopamine neurons, which 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

343 argues against significant roles for local modulation of dopamine release[20,76] or spiking adaptation in D1344 MSNs in the TD error computation. We identify three categories of possible mechanisms: cell intrinsic 345 mechanisms in dopamine neurons[77–79] , synaptic mechanisms in inputs to dopamine neurons[80,81] , and circuit 346 mechanisms between D1-MSNs and dopamine neurons[27,80,82–84] . Cell intrinsic mechanisms could include 347 depolarization block[79,85,86] or D2 autoreceptor activation triggered by dopamine neuron spiking[87] . However, 348 barring a spiking-independent mechanism, these mechanisms alone could not explain the pronounced 349 suppression of action potential firing locked to the offset of pattern 3, which typically did not strongly 350 activate spiking during the ramp-up phase ( **Fig. 3i** ). Next, synaptic mechanisms could include short-term 351 synaptic depression (e.g. depletion of vesicle pools), which can create derivative-like responses in post352 synaptic cells, wherein they respond proportionally to the percentage change of the input[81] . While short353 term synaptic plasticity may play a role within a larger circuit computation[80] , a single depressing synapse 354 cannot explain our finding that the dopamine response to lNAc D1-MSN stimulation plateaus at a level 355 below baseline, which distinguishes TD error from a strict derivative. For these reasons, we hypothesize 356 that circuit-level mechanisms play a major role in the temporal difference calculation. Importantly, although 357 D1-MSNs are inhibitory neurons, activating them induced a burst of spikes in dopamine neurons (latency 358 = 50-100 ms, **Extended Data Fig. 6c** ), implying a disinhibitory mechanism. Disinhibitory circuit 359 mechanisms could involve local inhibitory microcircuits within the VTA[80,82,88] and neighboring substantia 360 nigra pars reticulata (SNr), both of which receive innervation from lNAc D1-MSNs, or long-range 361 multisynaptic basal ganglia circuits, such as from lNAc D1-MSNs to ventral pallidum (VP) to VTA/SNr[27,84] . 362 Indeed, a recent study found that NAc D1-MSNs either (net) excite or (net) inhibit VTA dopamine neurons, 363 depending on whether they project to the ventral midbrain (including VTA and SNr) or ventral pallidum[84] . 364 If properly tuned in magnitude and timing, these oppositely signed responses could combine to form the 365 temporal difference response reported here. The balance of these pathways would determine the temporal 366 discount factor 𝛾𝛾, thus grounding the TD learning algorithm’s sensitivity to time in a biological circuit 367 mechanism ( **Extended Data Fig. 10b** ). 368 Altogether, our results show how TD computations are built into the circuitry of the basal ganglia, 369 potentially explaining a wealth of neurophysiological observations, including ramping dopamine signals 370 that possess a derivative-like property[5,19,20] . The same circuit mechanism may underlie temporal discounting 371 at the level of single dopamine neurons[47] . While this shows that TD-like learning is a core property of the 372 dopamine-striatum system when probed in isolation, natural behavior recruits additional circuits that may 373 modulate or expand the functionality of the dopamine system. Therefore, the extent to which the LTI model 374 proposed here can explain the contribution of dopamine and striatum to learning in more naturalistic 375 contexts remains an important direction for future study. 

21 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 1** 

**==> picture [466 x 657] intentionally omitted <==**

**----- Start of picture text -----**<br>
Calibrated dopamine axon stimulation<br>a 475 nm LEDPhotometry Stimulation b Water rewardsExample mouse8 µL Opto stim.50 Hz c 4 8 µL water rewardGFP mice (n=2)<br>635 nm LED 4 µL 40 Hz<br>2 µL1 µL 30 Hz20 Hz50 Hz, Ctrl 2<br>Optic Dichroic BP filter (tdTomato) 0<br>fiber mirror (630-690 nm)<br>Mouse (550 nm) -2<br>1 sec -1 0 1 2 3 4 5<br>sec<br>d Opto-conditioning task trial structure e Training and recording scheduleLate training (days 11+)<br>1 2 3 4 5 6 lNAc GRABDA3m photometry<br>Optotag 1 Water 1 Odors Water 2 Unpredicted Optotag 2 lNAc GRABDA3m photometry<br>opto stim + lNAc Neuropixels<br>40 trials 20 trials 160 trials 20 trials 10 trials 40 trials lNAc GRABDA3m photometry<br>(only on VTA (only on VTA + VTA Neuropixels<br>recording days) recording days)    (antidromically optotagged<br>lNAc-projecting dopamine neurons)<br>1 7 14 21 28<br>~50-60 mins<br>Task Day<br>f Example session, day 1 (mouse 1) h Responses to task events over training<br>Water rewards Odor trials Unpredicted opto stim Exp. mice (n=5) Ctrl. mice (n=3)<br>Late training (days 11+) Late training (days 11+) Exp.<br>40 mice<br>30 20 Ctrl.<br>20 0 mice<br>10<br>0 40<br>-10 20<br>0<br>40 40 40<br>2 µL CS+ omitCS+ stim<br>20 8 µL 20 CS- 20 40<br>0 0 0 20<br>0 2 4 0 2 4 0 2 4<br>Time from water (sec) Time from odor (sec) Time from stim (sec) 0<br>2<br>g Example session, day 19 (mouse 1) 0<br>Water rewards Odor trials Unpredicted opto stim<br>-2<br>2<br>20 0<br>15 -2<br>10 -4<br>5 -6<br>0<br>-5 2<br>0<br>20 2 µL 20 CS+ omitCS+ stim 20 -2<br>10 8 µL 10 CS- 10 2<br>0 0 0 0<br>-2<br>Time from water (sec)0 2 4 Time from odor (sec)0 2 4 Time from stim (sec)0 2 4 -4<br>-6<br>0 10 20 30 0 10 20 30<br>day day<br>i Development of cue response and omission dip over trainingExp. mice Ctrl. mice<br>Novel odor Late training Late training Omission dip reflects learned timing of opto stimulation<br>response (days 11+) CS+ (days 11+)<br>CS- j Group 1: Stim. at 1.5 sec(same data as above)  k 5 Odor l 6 *<br>Odor A (CS+) 5<br>Group 1 (n=5 mice)<br>Odor B (CS-) Group 2 (n=5 mice) 4<br>3<br>0 0.5 1 1.5 2 2.5 0<br>Group 2: Stim. at 2 sec  2<br>Odor A (CS+) 1<br>Odor B (CS-) -5 0<br>0 2 4 6 8<br>0 0.5 1 1.5 2 2.5 Time from odor (sec)<br>Trials (ticks mark days) Trials (ticks mark days) Time (sec)<br>OmissionOmission<br>Group 1 Group 2<br>%dF/F<br>20% dF/F<br>(n=5)<br>Exp. mice<br>(n=3)<br>Ctrl. mice<br>% dF/F<br>Water (8 µL)<br>Trial % dF/F<br>% dF/F<br>Unpred stim<br>% dF/F<br>Pred stim % dF/F<br>Cue % dF/F<br>CS+<br>Omit % dF/F<br>Trial % dF/F<br>Cue % dF/F<br>% dF/F CS-<br>Omit % dF/F<br>Cue<br> (CS+ – CS-)<br>tmin<br>% dF/F (CS+ – CS-)<br>Omission<br>2% dF/F<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 1:** Calibration of opto-stimulation, opto-conditioning task design and training details, and opto-conditioning task responses over training. 

- a) Schematic of experimental setup for optogenetic stimulation and photometry recording through the same optic fiber. 

- b) Calibration of optical stimulation in an example mouse expressing ChrimsonR in VTA dopamine neurons and GRABDA3m in lNAc. _Left:_ lNAc GRABDA3m signal in response to water rewards of various volumes (1, 2, 4, or 8 𝜇 ). _Right:_ lNAc GRABDA3m signal in response to opto-stimulation pulse trains of various frequencies. All pulse trains lasted for 500 ms (e.g. 10 pulses at 20 Hz, 15 pulses at 30 Hz, etc.), individual pulses were 5 ms in duration, and red light power density was 40 mW/mm[2] (5 mW through a 400 𝜇 diameter fiber). The gray line shows the response to a 50 Hz pulse train in a different mouse expressing tdTomato instead of ChrimsonR in VTA dopamine neurons. Stimulation frequency was chosen to best match the response to 8 𝜇 water reward (40 or 50 Hz, depending on the mouse). 

- c) Photometry response to 8 𝜇 water reward in mice expressing GFP instead of GRABDA3m in lNAc ( _n_ = 2 mice). We used 8 𝜇 water delivery as a task event that elicited robust movements (licking) to check whether movement artifacts influence our photometry signals. The peak change in dF/F relative to baseline was < 0.15% for both mice, compared to > 60% in panel b, indicating that movement artifacts were negligible in our head-fixed setup. Because movement artifacts were negligible, and the isosbestic wavelength for GRABDA3m is unknown, we did not correct GRABDA3m recordings using an isosbestic channel. However, we did correct GCaMP recordings ( **Fig. 2** , **Fig. 4** ) using an isosbestic channel at 𝜆𝜆 = 415 nm, which is close to the known isosbestic wavelength for GCaMP sensors. 

- d) Trial structure of the opto-conditioning task. 

- e) Training and recording schedule. Mice expressing ChrimsonR (Exp. Mice; _n_ = 5) or tdTomato (Ctrl. Mice; _n_ = 3) in VTA dopamine neurons were trained on the opto-conditioning task for up to 28 days. In exp. mice, Neuropixels recordings were performed during late training (defined as days 11+), in lNAc (on days 15-20) or VTA (on days 21-25). 

- f) lNAc GRABDA3m signals in response to task events from an example Exp. Mouse on day 1 of training in the opto-conditioning task. Heatmaps show single trial responses, separated by trial type, and lines with shaded areas show mean responses ± SEM by trial type. Photometry signals were baseline-subtracted (the average response in the 1 second window before trial onset was subtracted before plotting the data). 

- g) Same as panel f, but on day 19 of training. 

- h) GRABDA3m responses to task events over training for Exp. Mice (left column) and Ctrl. Mice (right column) in VTA dopamine neurons. The period defined as “late training” (days 11+) is indicated by a black line above the first plot. Thin colored lines show individual mice, and the thick black line shows the average over mice. Event responses are defined as the mean photometry signal (dF/F, baseline subtracted) in the time window 0-1 second after event onset. 

- i) The development of GRABDA3m responses to odors over training, at cue time (top row, 0-1 sec after odor onset) or omission time (bottom row, 1.5-2.5 sec after odor onset; only omission trials included for CS+), for exp. mice (left column) or ctrl. mice (right column). Single trial responses were averaged in the given time window, concatenated across days, and smoothed with a Gaussian filter (S.D. = 15 trials for all trial types except CS+ omission, which were 3x rarer and 

23 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

smoothed with an S.D. of 5 trials). Thin lines represent individual mice; thick lines show the mean over mice. 

- j) To test whether the timing of the omission dip reflected the timing of opto-stimulation delivered during training, a second group of 5 mice (“Group 2”; green) was trained with opto-stimulation delivered at 2 seconds instead of 1.5 seconds. The original 5 exp. mice are shown for comparison (“Group 1”; magenta). 

- k) Average difference in the GRABDA3m signal between CS+ omission trials and CS- in late training (days 11+) for Group 1 and Group 2 mice. The time of the omission dip was defined as the time of the minimum point of each trace, marked with a dot. 

- l) Omission dip time was significantly later for Group 2 mice compared to Group 1 mice (mean minimum time ± SEM, Group 1 = 2.35 ± 0.10 sec, _n_ = 5 mice; Group 2 = 3.79 ± 0.42 sec, _n_ = 5 mice; _P =_ 0.0102, unpaired t-test). 

24 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 2** 

**==> picture [470 x 371] intentionally omitted <==**

**----- Start of picture text -----**<br>
a 10 b 8<br>8 6<br>6 4<br>4<br>2<br>2<br>0 0<br>0 2 4 6 8 10 12 14 16 18 20 0 1 2 3 4 5 6 7 8 9 10<br>Response latency (ms) Mean firing rate (spikes/sec)<br>c Example optotagged lNAc-projecting VTA dopamine neurons<br>Example 1: YR1_20230410_c418 Example 2: MC100_20230404_c237 Example 3: MC97_20230328_c277 Example 4: MC97_20230327_c423<br>CS+<br>CS-<br>15 15 6 4<br>105 105 42 2<br>0 0 0 0<br>-1 0 1 2 3 4 5 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5<br>Time from odor onset (sec) Time from odor onset (sec) Time from odor onset (sec) Time from odor onset (sec)<br>Example 5: MC98_20230327_c437 Example 6: YR2_20230412_c356 Example 7: YR1_20230410_c157 Example 8: MC98_20230327_c163<br>10 6 3<br>5 42 21<br>0 0 0 [246] 0<br>-1 0 1 2 3 4 5 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5<br>Time from odor onset (sec) Time from odor onset (sec) Time from odor onset (sec) Time from odor onset (sec)<br>d Mouse CS+ (omit) CS+ (stim) CS- CS+ – CS- (no stim) 1 e f<br>Water Unpredicted opto stimulation<br>0.5 2 μL<br>8 μL<br>0 Difference:<br>8 μL-2 μL<br>-0.5<br>0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 -1 1 sec 1 sec<br>Time from odor onset (sec)<br>Count Count<br>Trial Trial Trial Trial<br>Spikes/sec Spikes/sec Spikes/sec Spikes/sec<br>Trial Trial Trial Trial<br>Spikes/sec Spikes/sec Spikes/sec Spikes/sec<br>z-score<br>Optotagged neurons (n = 43) 1 z 1 z<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 2:** Additional detail on antidromic optotagging of lNAc-projecting VTA dopamine neurons during opto-conditioning. 

- a) Histogram of spiking response latency to opto-stimulation pulse onset for optotagged lNAcprojecting VTA dopamine neurons (first significant bin ± SEM = 8.9 ± 0.4 ms, _n_ = 43 neurons). 

- b) Histogram of mean firing rate for optotagged lNAc-projecting VTA dopamine neurons (mean ± SEM = 2.8 ± 0.3 spikes/sec, _n_ = 43 neurons). 

- c) Example optotagged neuron responses to CS+ (omission trials, red) and CS- (black). Cell IDs are listed above each plot. The top panel of each plot shows spike rasters, split by trial type, and the bottom panel shows average firing rate by trial type (mean ± SEM). 

- d) Heatmaps of all optotagged neurons’ z-scored responses to odors. Firing rates were z-scored to intertrial intervals (mean and standard deviation). The colored bars on the left indicate the mouse for each neuron. The four panels show: CS+ omission trials, CS+ stimulation trials (note the large response to opto-stimulation at 1.5 seconds, which exceeds the limits of the color scale; see panel f for response to unpredicted opto-stimulation), CS- trials, and the difference between CS+ and CS- trials. 

- e) Z-scored response of optotagged neurons to unpredicted water delivery (mean ± SEM, _n_ = 43 neurons). 

- f) Z-scored response of optotagged neurons to unpredicted opto-stimulation (mean ± SEM, _n_ = 43 neurons). 

26 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 3** 

## **a** 

## **b** 

**==> picture [223 x 87] intentionally omitted <==**

**----- Start of picture text -----**<br>
Camera 1 (face) Camera 2 (body)<br>Eye<br>Nose WhiskerPad<br>Tongue<br>**----- End of picture text -----**<br>


## Nose motion, late training (days 11+) 

**==> picture [488 x 280] intentionally omitted <==**

**----- Start of picture text -----**<br>
MC97 (Hex) MC98 (Lim) MC100 (Hex) YR1 (Lim) YR2 (Hex)<br>DAT-Cre [+/-] Odor Stim. omission CS+ (omission trials)<br>stim. delay = 1.5 sec CS-<br>(n=5)<br>MC104 (Hex) MC107 (Lim) MC108 (Lim) MC113 (Hex) MC114 (Lim) MC117 (Lim) MC118 (Hex)<br>Tac1-Cre [+/-] ;DAT-Flp [+/-]<br>stim. delay = 1.5 sec<br>(n=7)<br>MC105 (Hex) MC106 (Lim) MC111 (Lim) MC112 (Hex) MC115 (Hex) MC116 (Lim)<br>A2a-Cre [+/-] ;DAT-Flp [+/-]<br>stim. delay = 1.5 sec<br>(n=6)<br>MC120 (Lim) MC121 (Lim) MC122 (Hex) MC123 (Hex) MC124 (Lim)<br>DAT-Cre [+/-]<br>stim. delay = 2.0 sec<br>(n=5)<br>YR3 (Hex) YR4 (Lim) YR6 (Hex)<br>DAT-Cre [+/-]<br>stim. delay = 1.5 sec<br>(n=3)<br>1 sec<br>(n=23)<br>ChrimsonR mice<br>(n=3)<br>1 z<br>tdTomato mice<br>**----- End of picture text -----**<br>


Nose motion, late training (days 11+) (n=23 ChrimsonR mice) 

**==> picture [352 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
c *** d P = 0.064 e<br>Water<br>Odor Odor<br>CS+ (omission trials) Odor identity: 2 μL<br>CS- Hexanol 8 μL<br>Limonene<br>1 sec 1 sec 1 sec<br>1 z 1 z 1 z<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 3:** Opto-conditioning enhances facial movements following odor delivery. 

- a) Example frames from the face camera (Camera 1; left) and body camera (Camera 2; right). To quantify behavioral responses to task events, motion energy (sum of absolute value of difference of subsequent frames) was computed within 5 ROIs, which were drawn manually for each video: WhiskerPad, Nose, Tongue, Eye (from Camera 1); and Body (the entire frame of Camera 2). 

- b) Motion energy within the nose ROI, in late training of the opto-conditioning task (days 11+), in response to the CS+ (omission trials; red) or CS- (black) (mean ± SEM). Rows separate experimental conditions, which were combined for the analysis in panels c-e. Across the experiments of Figures 1 and 2, there were 23 ChrimsonR mice (top) and 3 tdTomato mice (bottom). The identity of the CS+ odor is listed above each plot (Hex = hexanol, Lim = limonene). 

- c) Average motion energy within the nose ROI across ChrimsonR mice for CS+ omission trials (red) and CS- trials (black) (lines and shaded areas indicate mean ± SEM over _n_ = 23 mice). Nose motion was greater following the CS+ compared to the CS- (mean ± SEM, 0.5 - 2.5 sec after odor onset, CS+ = 0.19 ± 0.04, CS- = 0.02 ± 0.03, _n_ = 23 mice, _P =_ 9×10[-6] , t-test). *** _P <_ 0.001. 

- d) Same as panel c, but split by odor identity (hexanol, magenta, and limonene, green). There was a marginal effect of odor identity, with greater nose motion to limonene compared to hexanol (mean ± SEM, 0.5 - 2.5 sec after odor onset, hexanol = 0.07 ± 0.03, limonene = 0.15 ± 0.04, _n_ = 23 mice, _P =_ 0.064, t-test). 

- e) Motion energy within the nose ROI following water reward delivery, for comparison with odorevoked nose movements. 

28 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 4** 

**==> picture [548 x 309] intentionally omitted <==**

**----- Start of picture text -----**<br>
a b<br>lNAc neurons excited by CS+ (n=151/415) lNAc neurons excited by CS- (n=104/415) Example neuron 1 Example neuron 2<br>CS+ omission trials (sorted by CS+ stim trials) CS- even trials (sorted by CS- odd trials) Odor Stim/No stim Odor Stim/No stim CS+ trials (stimulation omitted)<br>CS+ trials (stimulation delivered)<br>CS+ Stim. omission CS- 50  50  CS- trials<br>1 3 100 100<br>20 20 12 2 150 150<br>40 40 1510 1510<br>60 60 4 1 50-1 0 1 2 3 4 5 50 -1 0 1 2 3 4 5<br>80 2 80 0 Time from odor onset (sec) Time from odor onset (sec)<br>Example neuron 3 Example neuron 4<br>100 100 -1 Odor Stim/No stim Odor Stim/No stim<br>120 50  50<br>-2<br>3 100 100<br>140<br>-3 150 150<br>-1 0 1 2 3 4 5 -1 0 1 2 3 4 5 10 20<br>Time from odor (sec) Time from odor (sec) 50 100<br>-1 0 1 2 3 4 5 -1 0 1 2 3 4 5<br>Time from odor onset (sec) Time from odor onset (sec)<br>c d e<br>lNAc neurons excited by CS+ or CS- (n=177/415) Mean lNAc neuron activity from individual mice (n=5) lNAc neurons inhibited by CS+ or CS- (n=125/415)<br>1.6 Odor Stim/No stim 2 Odor Stim. omission 0.8 Odor Stim/No stim<br>1.2 CS+ trials (stimulation omitted)CS+ trials (stimulation delivered) 1.5 CS- trialsCS+ trials (stimulation omitted) 0.6 CS+ trials (stimulation omitted)CS+ trials (stimulation delivered)<br>CS- trials 1 0.4 CS- trials<br>0.8<br>0.2<br>0.5<br>0.4 0<br>0 -0.2<br>0<br>-0.5 -0.4<br>-1 0 1 2 3 4 5 -1 0 1 2 3 4 5 -1 0 1 2 3 4 5<br>Time from odor onset (sec) Time from odor onset (sec) Time from odor onset (sec)<br>Trial Trial<br>Rate (Hz) Rate (Hz)<br>Neurons Neurons z-score<br>Trial Trial<br>Rate (Hz) Rate (Hz)<br>z-score z-score z-score<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- **Extended Data Fig. 4:** Additional detail on striatal Neuropixels recordings during opto-conditioning. 

   - a) Heatmaps of z-scored spiking responses of lNAc neurons to odors (CS+/CS-) in the optoconditioning task. Only neurons identified as significantly excited by CS+ (left; _n_ = 151/415 lNAc neurons) or by CS- (right; _n_ = 104/415 lNAc neurons) are shown (Methods). For CS+, neurons were sorted based on the time of their peak response in CS+ stimulation trials, and responses on CS+ omission trials are shown (this was done due to the small number of omission trials and the lack of a difference between stimulation and omission trials; see e.g. panel c). For CS-, neurons were sorted based on the time of their peak response on odd CS- trials, and the response on even CS- trials is shown. The four example neurons shown in panel b are indicated. 

   - b) Spiking responses of four example neurons indicated in panel a. In this panel as well as panels c and e, trials are split into three groups: CS+ trials on which opto-stimulation was omitted (red), CS+ trials on which opto-stimulation was delivered (blue), and CS- trials (black). 

   - c) The average odor responses of lNAc neurons significantly excited by either CS+ or CS- in the opto-stimulation task ( _n_ = 177/415 lNAc neurons; same as **Fig. 2b** but including CS+ stimulation trials for comparison [blue trace]). Lines and shaded areas indicate mean ± SEM. 

   - d) The average odor responses of lNAc neurons significantly excited by either CS+ or CS-, averaged by mouse ( _n_ = 5 mice), on CS+ omission trials (red) or CS- trials (black). Thin red/black lines indicate individual mice; thick red/black lines show the average over mice. 

   - e) Same as panel c, but for neurons significantly inhibited by either CS+ or CS- ( _n_ = 125/415 lNAc neurons; Methods). Because CS+ responses were still positively enhanced relative to CSresponses in this group of neurons, we conclude that the primary effect of opto-stimulation was to positively enhance CS+ responses in a subset of neurons (as opposed to bidirectional positive/negative changes in CS+ response). 

30 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 5** 

## **b** 

**==> picture [488 x 533] intentionally omitted <==**

**----- Start of picture text -----**<br>
a DAT-Flp [+/-]  mouse Calibration of opto-stimulation in  DAT-Flp [+/-]  mouse<br>AAV8-FLPX-ChrimsonR-tdTomato AAV-in lNAcGRABDA3m AAV-FLPX-ChrimsonR Water 8 μL Opto stim.50 Hz<br>in VTA 4 μL 40 Hz<br>Optic fiber 2 μL 30 Hz<br>1 μL 20 Hz<br>TH     tdTomato DAT-Flp [+/-]  mouse 1 sec<br>c Example D1 mouse (MC108) d Example D2 mouse (MC111)<br>Water rewards Odor trials Unpred stim Water rewards Odor trials Unpred stim<br>3 3<br>2 2<br>1 1<br>0 0<br>-1 -1<br>321 2 μL8 μL 321 CS+ omitCS+ stimCS- 321 321 2 μL8 μL 321 CS+ omitCS+ stimCS- 321<br>0 0 0 0 0 0<br>-1 -1 -1 -1 -1 -1<br>0 2 4 0 2 4 0 2 4 0 2 4 0 2 4 0 2 4<br>Time from water (sec) Time from odor (sec) Time from stim (sec) Time from water (sec) Time from odor (sec) Time from stim (sec)<br>Water rewards Odor trials Unpred stim Water rewards Odor trials Unpred stim<br>3 3<br>2 2<br>1 1<br>0 0<br>-1 -1<br>321 2 μL8 μL 321 CS+ omitCS+ stimCS- 321 321 2 μL8 μL 321 CS+ omitCS+ stimCS- 321<br>0 0 0 0 0 0<br>-1 -1 -1 -1 -1 -1<br>0 2 4 0 2 4 0 2 4 0 2 4 0 2 4 0 2 4<br>Time from water (sec) Time from odor (sec) Time from stim (sec) Time from water (sec) Time from odor (sec) Time from stim (sec)<br>D1 Mice (n=7)<br>e<br>Mouse 1 (MC104) Mouse 2 (MC107) Mouse 3 (MC108) Mouse 4 (MC113) Mouse 5 (MC114) Mouse 6 (MC117) Mouse 7 (MC118)<br>CS+ CS- CS+ CS- CS+ CS- CS+ CS- CS+ CS- CS+ CS- CS+ CS-<br>3<br>0<br>-3<br>Time<br>f D2 Mice (n=6)<br>Mouse 1 (MC105) Mouse 2 (MC106) Mouse 3 (MC111) Mouse 4 (MC112) Mouse 5 (MC115) Mouse 6 (MC116)<br>CS+ CS- CS+ CS- CS+ CS- CS+ CS- CS+ CS- CS+ CS-<br>3<br>0<br>-3<br>Time<br>20% dF/F<br>Trial % dF/F Trial % dF/F<br>Day 1 Day 1<br>% dF/F % dF/F<br>Day 11 Trial % dF/F Day 11 Trial % dF/F<br>% dF/F % dF/F<br>Trials<br>z-score<br>Extinction<br>Trials<br>z-score<br>Extinction<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 5:** Validation and calibration of dopamine axon stimulation in _DAT-Flp[+/-]_ mice, and development of D1- and D2-MSN responses to opto-conditioned odors over training. 

- a) Confocal image of VTA in a _DAT-Flp[+/-]_ mouse injected with AAV8-FLPX-ChrimsonR-tdTomato and stained for TH, showing co-expression of tdTomato and TH. Scale bar = 100 𝜇 . 

- b) Calibration of opto-stimulation to water reward in a _DAT-Flp[+/-]_ mouse. Calibration could not be performed in the same mice as used for the experiment in **Fig. 2** because GCaMP8m was expressed in MSNs. Therefore, based on this panel, opto-stimulation frequency of 40 Hz was used for all mice, approximately matching an 8 𝜇 water reward while remaining below the sensor’s ceiling. 

- c) Example GCaMP8m photometry responses to task events (water rewards, odors, and unpredicted opto-stimulation) in a D1 mouse, on day 1 of training (top row) and day 11 of training (bottom row). Heatmaps show photometry responses on single trials, split by trial types. Traces and shaded areas show mean ± SEM for each trial type, averaged over trials. Note the emergence of a sustained photometry response to the CS+ odor, which was similar between trials on which optostimulation was delivered (blue) or omitted (red). 

- d) Same as panel c, but in an example D2 mouse. Note that unlike the D1 mouse, photometry signals showed no difference between CS+ and CS- trials on day 11 of training. This was not due to a failure of sensor expression, as responses to water delivery and novel odors (first few trials) were observed. 

- e) Heatmaps showing the development of odor responses in all individual D1 mice ( _n_ = 7) over training and extinction. The white line indicates the end of training and beginning of extinction. Single trials of each type (CS+ or CS-; CS+ omission and stimulation trials combined) were concatenated, forming a matrix of trials x time. To improve visualization, this matrix was smoothed over trials by applying a Gaussian filter to each column (corresponding to an individual time point within the trial) with SD = 15 trials. Note that some mice showed a photometry response to opto-stimulation which decays away over trials. Based on the experiment in **Fig. 2j** , we argue that this was a visual response to the red opto-stimulation light, not a response to dopamine release itself (no red masking light was used in this experiment). 

- f) Same as panel e, but for D2 mice ( _n_ = 6). 

32 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 6** 

**==> picture [500 x 508] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Example optotagged D1-MSN b Example optotagged dopamine neuron c Latency of<br>(MC180_20240711_c241) (MC230_20250515_c389) excitatory response<br>First Stim Stim<br>pulse Pattern Optotag Pattern 20 n = 55 optotagged dopamine neurons<br>1 1 10 30<br>0<br>2 20 25<br>2 10<br>3 200 20<br>3 10 15<br>4 0<br>150<br>100 20 10<br>50 600 4 10<br>0 5 400200 0 5<br>-5 0 5 10 0 20<br>ms -10 0 10 20 30 5 10 0<br>6 ms 0<br>20<br>6 10 -50 0 50 100 150<br>7 0 Time from pattern 4 onset (ms)<br>20<br>7 10<br>-1 0 1 2 3 4 -1 0 1 2 3 4 0<br>Time from stim (sec) -1 0 1 2 3 4 -1 0 1 2 3 4<br>Time from stim (sec)<br>d<br>1 2 3 4 5 6 7<br>50<br>40<br>30 Stimulation patterns (concatenated)<br>20<br>10 Estimated<br>0 filter<br>40<br>30 D1-MSNsPrediction<br>20<br>10<br>0 0 1 2<br>sec<br>2 sec<br>ChrimsonR tdTomato GFP<br>Stim e (n=13 mice)ChrimsonR f (n=6 mice)tdTomato g (n=3 mice)GFP h 1 (n=13 mice) i 1 (n=6 mice) j 1 (n=3 mice)<br>Patterns 0.8 0.8 0.8<br>0.6 0.6 0.6<br>1 0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>-0.2 -0.2 -0.2<br>-0.4 -0.4 -0.4<br>2 -0.6-0.8 -0.6-0.8 -0.6-0.8<br>-1 -1 -1<br>0 1 2 3 4 0 1 2 3 4 0 1 2 3 4<br>Model order Model order Model order<br>3 k 1 *** l 1 * m 1 *<br>0.8 0.8 0.8<br>0.6 0.6 0.6<br>0.4 0.4 0.4<br>0.2 0.2 0.2<br>0 0 0<br>4 -0.2 -0.2 -0.2<br>-0.4 -0.4 -0.4<br>-0.6 -0.6 -0.6<br>-0.8 -0.8 -0.8<br>-1 0 1 2 3 4 5 6 -1 0 1 2 3 4 5 6 -1 0 1 2 3 4 5 6 -1 -1 -1<br>Time from stim (sec)<br>Derivative TD Derivative TD Derivative TD<br>Trial<br>Trial<br>Spikes/sec<br>Spikes/sec Spikes/sec<br>Spikes/sec<br>20 spikes/sec<br>pulses/sec<br>spikes/sec<br>2CV R 2CV R 2CV R<br>2CV R 2CV R 2CV R<br>10% dF/F<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 6:** Additional detail on dopamine response to stimulation of lNAc D1 MSNs. 

- a) Responses of an example single optotagged lNAc D1-MSN to opto-stimulation patterns of **Fig. 3** . _Left:_ The response to the first pulse in the stimulus pulse train (used to identify optotagged neurons, Methods). _Middle:_ Spike raster showing the response to each of the 7 stimulation patterns (same patterns as in **Fig. 3b** ). _Right:_ The firing rate in response to each of the 7 stimulation patterns. Lines and shaded area indicate mean ± SEM over trials. 

- b) Responses of example antidromically optotagged lNAc-projecting VTA dopamine neuron to opto-stimulation patterns of **Fig. 3** . _Left:_ The response to the optotagging pulses (blue light; used to identify optotagged neurons, Methods). _Middle:_ Spike raster showing the response to each of the 7 stimulation patterns (same patterns as in **Fig. 3b** ). _Right:_ The firing rate in response to each of the 7 stimulation patterns. Lines and shaded area indicate mean ± SEM over trials. 

- c) Average PSTH of optotagged dopamine neurons ( _n_ = 55) aligned to the onset of pattern 4, which typically elicited a rapid burst of action potentials. Time scale is zoomed in to visualize the latency of the spiking response. Line and shaded area indicate mean ± SEM over neurons ( _n_ = 55). 

- d) LTI model fit predicted D1-MSN response to the 7 stimulation patterns. _Top_ : The 7 stimulation patterns, concatenated. _Bottom_ : Average lNAc D1-MSN responses to the 7 stimulation patterns (red; averaged over _n_ = 2 mice) and the LTI model fit (black) predicting D1-MSN response (output) from stimulation patterns (input) (cross-validated [CV] R[2] = 0.95 Methods). _Right_ : Estimated filter of the LTI model. Note that the filter is approximately a delta function, which scales the input to produce the output. 

- e) The GRABDA3m photometry response to opto-stimulation patterns 1-4 in mice prepared as in **Fig. 3a** , with optogenetic stimulation of lNAc D1-MSNs and photometric recording of lNAc dopamine release, but without stimultaneous Neuropixels recording of optotagged lNAc D1MSNs. The stimulation parameters differed: here, we used 5 ms instead of 1 ms pulses, and power was reduced 5x from 40 mW/mm[2] to 8 mW/mm[2] (1 mW through a 400 µm diameter fiber) (same parameters used in panels e-g). The TD error-like response patterns were the same as in **Fig. 3c** and **Fig. 3e** , with positive/negative transients locked to the onset/offset of constant stimulation and a negative plateau before offset; a strong positive response to pattern 4 (ramp down) but not pattern 3 (ramp up); and a negative response to the offset of pattern 3. Thick line and shaded area indicate mean ± SEM over mice ( _n_ = 13). Thin lines indicate individual mice. 

- f) Same as panel e but for mice with tdTomato expressed instead of ChrimsonR in lNAc D1-MSNs. No significant responses to optical stimulation were observed, ruling out optical crosstalk and visual responses. 

- g) Same as panel e, but for mice with GFP expressed instead of GRABDA3m in VTA axons in lNAc. In contrast to the no-opsin (tdTomato) control, small fluctuations in the GFP signal were observed following optical stimulation of D1-MSNs, possibly due to hemodynamic responses to optogenetic stimulation. 

- h) Same as **Fig. 3f** , but for the mice in panel e ( _n_ = 13). In panels h-j, thin lines indicate individual mice and thick lines and error bars indicate mean ± SEM over mice. In panels h-m, LTI models were fit predicting dopamine responses directly from stimulation patterns, as D1-MSN activity was not recorded in these mice. 

- i) Same as panel h, but for tdTomato control mice ( _n_ = 6). 

- j) Same as panel h, but for GFP control mice ( _n_ = 3). 

34 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- k) Same as **Fig. 3g** , but for the mice in panel e ( _n_ = 13). In panels k-m, lines indicate individual mice and bars/error bars indicate mean ± SEM over mice. *** _P =_ 6.8 × 10[-5] , paired t-test. 

- l) Same as panel k, but for tdTomato control mice ( _n_ = 6). * _P =_ 0.022, paired t-test. 

- m) Same as panel k, but for GFP control mice ( _n_ = 3). * _P =_ 0.029, paired t-test. 

35 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 7** 

|MC190<br>MC191<br>MC193<br>%dF/F<br>MC194<br>MC195<br>MC196<br>saline<br>muscimol<br>Mouse:<br>-10<br>0<br>10<br>20<br>30<br>-10<br>0<br>10<br>20<br>30<br>-10<br>0<br>10<br>20<br>30<br>-10<br>0<br>10<br>20<br>30<br>-10<br>0<br>10<br>20<br>30<br>-10<br>0<br>10<br>20<br>30||Unpredicted<br>Reward<br>0<br>2<br>4<br>6|Cued<br>Reward<br>0<br>2<br>4<br>6|Reward<br>Omission<br>sec<br>0<br>2<br>4<br>6|Unrewarded<br>Odor<br>0<br>2<br>4<br>6|Novel<br>Odor|
|---|---|---|---|---|---|---|
||||||||
||||||||
||||||||
||||||||
||||||||
|||||||0<br>2<br>4<br>6|



bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 7:** Additional detail on VTA dopamine neuron calcium activity during injection of muscimol or saline into lNAc (related to **Fig. 4** ). 

Average VTA dopamine neuron calcium response aligned to task events for each session in the data set ( _n_ = 26 session from 6 mice). Rows indicate mice, columns indicate trial types, lines show the average response for that trial type within an individual session, and colors indicate saline (black) versus muscimol (red) injection. Note that novel odors were only delivered for 4 of 6 mice (21/26 sessions). 

37 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 8** 

**==> picture [469 x 484] intentionally omitted <==**

**----- Start of picture text -----**<br>
a Setup 1: MC190, MC193 Setup 2: MC191, MC194, MC195, MC196<br>MC193_20240804 - SALINE MC193_20240803 - MUSCIMOL MC191_20240818 - SALINE MC191_20240819 - MUSCIMOL<br>Nose Nose Nose Nose<br>Mouth<br>Mouth Mouth Mouth<br>Odor Reward<br>reward<br>CS+,<br>rewarded/<br>CS-<br>2 sec<br>b Mouth<br>Unpredicted Reward Predicted Reward Rewarded Cue Reward Omission Unrewarded Cue Novel Odor Mouse:<br>** * ** n.s. * n.s. MC190<br>3 MC191<br>MC193<br>MC194<br>2<br>MC195<br>MC196<br>1<br>0<br>-1<br>sal mus sal mus sal mus sal mus sal mus sal mus<br>Nose<br>Unpredicted Reward Predicted Reward Rewarded Cue Reward Omission Unrewarded Cue Novel Odor<br>*** *** n.s. *** * *<br>3<br>2<br>1<br>0<br>-1<br>sal mus sal mus sal mus sal mus sal mus sal mus<br>Mouth<br>Nose<br>Motion energy (z-score)<br>2 z<br>Motion energy (z-score)<br>Motion energy (z-score)<br>**----- End of picture text -----**<br>


**==> picture [227 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
Setup 2: MC191, MC194, MC195, MC196<br>MC191_20240818 - SALINE MC191_20240819 - MUSCIMOL<br>Nose Nose<br>Mouth Mouth<br>Unpredicted<br>reward<br>CS+,<br>rewarded/<br>unrewarded<br>CS-<br>Novel Odor<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 8:** Facial movements in classical conditioning task with muscimol versus saline in lNAc. 

- a) Example video frames (top) and task-aligned motion energy traces (bottom) from the muscimol experiment ( **Fig. 4** ). Two different odor/water delivery setups were used in the experiment: Setup 1 (left) was used for mice MC190 and MC193, and Setup 2 (right) was used for mice MC191, MC194, MC195, and MC196. Example frames and average motion energy traces are shown for an example saline day and muscimol day for each setup. ROIs were manually drawn around the nose and mouth, motion energy (sum of absolute value of the difference between subsequent frames) was computed within each ROI, and z-scored across the entire session. Novel odors were not delivered in every session, but an example pair of sessions is shown in which novel odors were also delivered (green traces, right). 

- b) Average z-scored motion energy in the mouth ROI (top) and nose ROI (bottom) in 1-second windows following task events during saline (sal) and muscimol (mus) sessions. Lines indicate average over sessions for each mouse and points indicate individual sessions; colors indicate mice. Significance stars indicate significance of treatment (saline versus muscimol) in a linear mixed effects model with a fixed effect of treatment and random effect per mouse. n.s. Not Significant, * _P <_ 0.01, ** _P <_ 0.001, *** _P <_ 0.0001. 

39 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 9** 

|Pattern 1<br>1z<br>1s<br>Pattern 2<br>Pattern 3<br>Pattern 4<br>1<br>2<br>3<br>4<br>Stim<br>Patterns:<br>1<br>2<br>3<br>4<br>Stim<br>Patterns:<br>Pattern 1<br>1z<br>1s<br>Pattern 2<br>Pattern 3<br>n=6<br>Pattern 4<br>n=3<br>n=3<br>n=13<br>n=7<br>n=6<br>**a**<br>**b**<br>**c**<br>lNAc<br>lNAc<br>lNAc<br>lNAc<br>DMS<br>DLS<br>D1-MSN stimulation site<br>lNAc<br>DMS<br>DLS<br>D1-MSN stimulation site<br>lNAc<br>DMS<br>DLS<br>D1-MSN stimulation site<br>R2= 0.92<br>R2= 0.85<br>R2= 0.71||ChrimsonR mice<br>Dopamine recording site|||
|---|---|---|---|---|
|||Pattern 1<br>Pattern 2<br>Pattern 3<br>Pattern 4<br>n=7<br>n=7<br>n=2<br>tdTomato mice<br>Dopamine recording site<br>DMS|Power = 1 mW<br>Pattern 1<br>Pattern 2<br>Pattern 3<br>Pattern 4<br>n=6<br>n=2<br>n=6<br>DLS||
|||Pattern 1<br>Pattern 2<br>Pattern 3<br>Pattern 4<br>n=3<br>n=3<br>n=3<br>Dopamine recording site<br>DMS|Power = 1 mW<br>Pattern 1<br>Pattern 2<br>Pattern 3<br>Pattern 4<br>n=3<br>n=3<br>n=3<br>DLS||
||lNAc<br>R2= 0.92<br>R2= 0.85<br>R2= 0.71|DMS<br>R2= 0.76<br>R2= 0.82<br>R2= 0.68|DLS<br>R2= 0.64||
||||||
||||||
||||R2= 0.09||
||||||
||||R2= 0.62||
||||||
||||Actual dopamine<br>response<br>Predicted dopamine<br>response||



bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 9:** Additional detail on dopamine responses to stimulation of D1 MSNs in multiple striatal subregions (lNAc, DMS, DLS). 

- a) In this experiment, only the first 4 of the 7 stimulation patterns were used. Photometry responses to the 4 stimulation patterns (schematized to the left of the figure) for each pair of D1-MSN stimulation site (rows) and dopamine sensor photometry recording site (columns), as in **Fig. 5b** but showing the response to all 4 patterns. As in **Fig. 3** and **Fig. 5** , dopamine photometry recordings were made by expressing GRABDA3m non-specifically in VTA neurons and recording photometry signals from VTA axons in the given striatal recording site. Black lines show the mean response across animals and gray lines show individual animals. The number of animals for each pair of stimulation and recording sites is listed above the response to Pattern 4. Red light stimulation power was 1mW through a 400 𝜇 diameter optical fiber (8 mW/mm[2] ). 

- b) Same as panel a, but for control mice expressing tdTomato instead of ChrimsonR in D1-MSNs. No significant responses were observed, indicating that optical crosstalk was successfully eliminated, and that the red stimulation light alone was not sufficient to drive visual dopamine responses (red masking lamps were used in these experiments to mask red stimulation light). 

- c) For each pair of D1-MSN stimulation site (rows) and dopamine sensor photometry recording site (columns), the actual response to the four stimulation patterns of panels a and b (black; averaged over mice) and the predicted response of an LTI model with 2 poles and 1 zero (red; fit using the function _tfest_ in MATLAB, from the Systems Identification Toolbox, as in **Fig. 3, Fig. 5** ). The 𝑅𝑅[2] between the data and model fit is listed above each plot, corresponding to the given pair of stimulation and recording sites. 

41 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **Extended Data Figure 10** 

## **a** Minimal TD learning loop 

**==> picture [256 x 102] intentionally omitted <==**

**----- Start of picture text -----**<br>
Patient<br>Dopamine<br>impulse<br>VTA response<br>Potentiation<br>lNAc<br>Temporal<br>Dopamine neurons difference<br>D1-MSNs Impatient<br>Discount factor<br>**----- End of picture text -----**<br>


## **b** 

## Hypothesized circuit 

**==> picture [377 x 106] intentionally omitted <==**

**----- Start of picture text -----**<br>
VTA microcircuit for temporal difference Dopamine impulse response<br>D1- VTA (D1 pathway)<br>MSNs 1 3 GABAtype 2 4 P =N 1= +12+ 3 + 4<br>VTA<br>D2- 5 VP 6 GABA 2 VTA<br>MSNs GABA type 1 DA P<br>Discount factor (γ) ≈<br>γ is a  single-neuron  property N<br>set by the balance of<br>2 and 3 + 4<br>**----- End of picture text -----**<br>


**==> picture [434 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
Dopamine<br>c Impulse γ Patient diversityneuron Individualvariability Develop-ment Addiction/Drug use Training<br>response<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>Impatient<br>**----- End of picture text -----**<br>


bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

**Extended Data Fig. 10:** Summary of findings and hypotheses for future work. 

- a) Minimal TD learning loop, based on the experiments of **Fig. 1-3** . Calibrated dopamine release in lNAc potentiates the response of lNAc D1-MSNs to preceding sensory stimuli (green line, indicating dopaminergic axons projecting from VTA to lNAc); in turn, lNAc D1-MSNs generate TD error-like signals in lNAc-projecting VTA dopamine neurons via a temporal difference calculation which occurs between lNAc and VTA (red dashed line, indicating a net circuit effect). The temporal difference calculation can be captured by convolution with a biphasic linear filter, whose shape sets the temporal discount factor of the TD algorithm. 

- b) Schematic of a possible neural circuit computing a temporal difference involving inhibitory and disinhibitory microcircuits within the VTA[80,82,89] . VP: ventral pallidum, SNr: substantia nigra pars reticulata, VTA: ventral tegmental area. 

- c) Potential connections of the shape of the dopamine impulse response to temporal discounting at the neuronal and behavioral levels. 

43 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 376 **Methods** 

## 377 

## 378 

## **Experimental procedures** 

## 379 

- 380 

## **Animals** 

- 381 A total of 74 mice (39 male, 35 female, aged 2-12 months at time of surgery) were used in the 382 experiments. Mice were housed on a 12 hr / 12 hr dark/light cycle and experiments were performed in the 383 dark phase. All procedures were performed in accordance with the National Institutes of Health Guide for 384 the Care and Use of Laboratory Animals and approved by the Harvard Institutional Animal Care and Use 385 Committee. 

- 386 

- 387 

## **Surgeries** 

- 388 All surgical procedures were performed in aseptic conditions. Mice were anesthetized using isoflurane 389 (4% induction, 1-2% maintenance) and given an intraperitoneal injection of buprenorphine HCl (0.1 390 mg/kg) for analgesia. They were then head-fixed within a stereotactic surgical setup (Narishige). The hair 391 was removed, the scalp was cleaned with 70% ethanol then 10% povidone-iodine, and a local anesthetic 392 (2% lidocaine, 0.05 mL) was injected under the scalp. The scalp and periosteum were removed and the 393 skull was dried and scored with a scalpel blade to ensure good adhesive binding. The skull was leveled by 394 ensuring bregma and lambda were at the same DV position; no ML leveling was performed. Fiducial 395 marks were made above the target sites (for virus injections, fiber implants, electrophysiology recording, 396 or muscimol injection) using a fine-tipped pen. The following coordinates were used, with all distances in 397 mm (AP and ML measured relative to bregma and DV measured from the surface of the brain): 

- 398 VTA, virus injection ( **Fig. 1-3, 5** ): -3.0 AP, 0.6 ML, 4.3→4.2→4.1 DV 

- 399 VTA, fiber implant ( **Fig. 4** ): -3.0 AP, 0.6 ML, 4.2 DV 

400 SNc, virus injection ( **Fig. 5** ): -3.0 AP, 1.6 ML, 4.2→4.1→4.0 DV 

401 lNAc virus injection ( **Fig. 1-3** , **5** ): 1.3 AP, 1.8 ML, 4.1 DV 

- 402 lNAc fiber implant ( **Fig. 2** , **3** , **5** ): 1.3 AP, 1.8 ML, 4.0 DV 

- 403 lNAc angled fiber implant ( **Fig. 1-3** ): 1.3 AP, -1.1 ML, 4.75 DV, angled 35º in coronal plane away 404 from midline 

405 DMS, virus injection ( **Fig. 5** ): 0.5 AP, 0.5-0.7 ML, 2.7→2.6 DV, angled 15º in coronal plane towards 406 midline 

407 DMS, fiber implant ( **Fig. 5** ): 0.5 AP, 0.5-0.7 ML, 2.5 DV, angled 15º in coronal plane towards midline 408 DLS, virus injection ( **Fig. 5** ): -0.3 AP, 2.8 ML, 2.6 DV, angled 15º in sagittal plane towards posterior 409 DLS, mirrored fiber implant ( **Fig. 5** ): -0.3 AP, 2.6 AP, 2.8 DV, angled 15º in sagittal plane towards 410 posterior, mirror facing towards lateral side 

44 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

411 The exact combinations of viruses, fibers, and target sites depended on the experiment and are given in 412 the corresponding sections. Craniotomies were made above virus injection and fiber implant target sites 413 using a high-speed dental drill. Virus injections were performed using glass pipettes (Drummond, pulled 414 using Narishige PC-10) with an oil hydraulic microinjector (Narishige MO-10). All virus injections were 415 300 nL volume with viral titer ranging from 5 × 10[12] to 2 × 10[13] gc/mL. The pipette was slowly 416 withdrawn 10 minutes after completing the injection. Optic fiber cannulae were scored using the dental 417 drill (to improve adhesive binding), slowly implanted using a stereotaxic cannula holder (SCH_1.25, 418 Doric Lenses), and temporarily held in place using a small amount of superglue (n-butyl cyanoacrylate) 419 and accelerant. After fiber implants, a custom titanium headplate was attached to the skull with dental 420 cement (Metabond, Parkell) containing a small amount of charcoal powder to reduce light leakage. The 421 cement also served to reinforce the optic fiber implants. For electrophysiology and muscimol 

- 422 experiments, a 3D-printed plastic well was glued to the headplate with epoxy or superglue, to hold saline 423 during recordings or injections. For electrophysiology experiments, a ground pin coated with a lead-tin 424 alloy (Mill-Max) was implanted above contralateral cortex. Apart from ground pin implants, all surgical 425 procedures (virus injections, fiber implants, craniotomies) were done in the left side of the brain. 

- 426 

- 427 Following surgery, mice recovered on a heating pad, and were given ketoprofen (20 mg/kg, injected SC) 428 and 0.5 mL of sterile saline (injected IP). Mice were then singly housed and post-operative analgesia 429 (ketoprofen, 20 mg/kg) was given twice daily for 48 hours. In experiments using viruses, we waited at 430 least 3 weeks for the virus to express before starting experiments. 

- 431 

- 432 **Behavioral training** 

- 433 All behavioral experiments took place inside custom-built, partially sound-proofed, enclosed behavioral 434 setups in which head-fixed mice ran freely on a cylindrical running wheel. White noise machines outside 435 the setups were used to mask background noise. Except for opto-stim experiments using red masking 436 lamps ( **Fig. 2j, Fig. 3, Fig. 5** ; see _Red masking lamp_ below), experiments were run in the dark, with 437 infrared lamps illuminating the mouse for face and body videos. Behavioral tasks were controlled using a 438 Bpod state machine (1027, Sanworks) and accessories (1004: Port Interface, 1020: Optical Lickometer, 439 1038: Analog Output Module, 1039: Valve Module; Sanworks) with custom software written in 440 MATLAB (R2021b) based on functionality in the Bpod MATLAB Software Repository 441 (github.com/Sanworks/Bpod_Gen2). 

- 442 

- 443 _Water deprivation_ 

- 444 Mice were water-deprived starting at least 7 days after surgery. After this, mice were weighed daily and 445 given water (1-2 mL) to maintain their bodyweight above 85% of baseline throughout the experiment. 

- 446 

- 447 _Water delivery and lick detection_ 

- 448 Water droplets were delivered to head-fixed mice through a spout attached to an optical lickometer (1020, 449 Sanworks), which detected licks as breaks of an infrared beam. Water delivery was controlled by a Bpod 450 port interface (1004, Sanworks) and valve (LHDA1231115H, The Lee Company). Water droplet volume 

45 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

451 was calibrated using a built-in Bpod protocol. In some experiments, to improve visibility of the face, the 452 beam-break lickometer was removed and licks were detected directly from face videos in post-processing 453 (e.g. **Extended Data Fig. 8a** , right). 

- 454 

## 455 

## _Habituation to recording setups_ 

456 All mice went through the same habituation protocol before starting experiments: 1 day of handling by 457 experimenter, 1 day of freely exploring head-fixation setup while receiving water from a syringe 458 (administered by experimenter), 1 day of head-fixation while receiving water from a syringe 459 (administered by experimenter), followed by several days of head-fixation with water droplets 460 administered from the same valve/spout used in experiments. Thus, when mice began experiments, their 461 weights had stabilized, and they were well habituated to handling by the experimenter, head-fixation, and 462 receiving water droplets within the recording setup. 

- 463 

- 464 _Odor preparation and delivery_ 

465 Pure odors (1-hexanol, (S)-(-)-limonene, isoamyl acetate, p-cymene, ethyl butyrate, (+)-carvone, (+/-)466 citronellal, eugenol, 1,4-cineole, L-fenchone, α-ionone; Sigma-Aldrich) were diluted to 10% in mineral 467 oil (Sigma-Aldrich). Each day, 30 𝜇 of each odor solution used in the current experiment was placed on 468 a syringe filter (Whatman Puradisc 6823-1327; 13 mm diameter, 2.7 𝜇 pore size) and the filters were 469 attached to a custom odor manifold made of polyetheretherketone (PEEK). Filtered air (0.9 L/min) was 470 constantly delivered to the mouse’s nose. A system of valves (LHDA1221111H, The Lee Company, 471 mounted in a manifold, LFMX0510528B, The Lee Company), controlled by the Bpod state machine 472 (1027, Sanworks) with an accessory valve module (1015, Sanworks), added 0.1 L/min to this air stream, 473 for a total flow of 1 L/min. By default, this added air passed through a filter containing only mineral oil 474 (“blank”). To deliver an odor, the valves switched the additional air flow from the blank filter to the 475 desired odor filter. A vacuum line inside the recording setup provided air circulation to remove odors. In 476 all experiments, odor identities assigned to CS+/CS- were counterbalanced across mice. 

477 

478 _Opto-conditioning task_ 

479 After standard habituation, mice started training on an odor-based opto-conditioning task ( **Fig. 1, Fig. 2** ). 480 The two odors used were 1-hexanol and limonene. One odor was associated with opto-stimulation of 481 dopamine axons in lNAc on 75% of trials (CS+) and the other was associated with nothing (CS-). 482 Dopamine axon stimulation was calibrated to a natural reward (8 𝜇 water) for each mouse ( **Fig. 1e,** 483 **Extended Data Fig. 1b, Extended Data Fig. 5b** ; see **Fiber photometry with optogenetics** for details). 484 Odors were delivered for 1 second followed by a 0.5 second trace period ( **Fig. 1, Fig. 2** ) or 1 second trace 485 period ( **Extended Data Fig. 1j-l** ) before opto-stimulation. Inter-trial intervals (ITIs) were drawn from a 486 truncated exponential distribution with mean 4 seconds and maximum 12 seconds and added to a fixed 487 8.5 second interval for a total ITI of 8.5-20.5 seconds with mean 12.5 seconds. 80 trials of each type (CS+ 488 and CS-) were delivered, pseudo-randomly interleaved, for a total of 60 CS+ stimulated trials, 20 CS+ 489 omission trials, and 80 CS- trials. Immediately before and after the odor trials, we delivered blocks of 490 water rewards, as a comparison point for the signals generated by odors and opto-stimulation. These 

46 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

491 blocks of water rewards consisted of 16-20 trials, split evenly between 2 𝜇 and 8 𝜇 droplets pseudo492 randomly interleaved, with the same ITI distribution as the odor trials. At the very end of the session 493 (after the second block of water rewards), 10 unpredicted opto-stimulation trials were delivered, with the 494 same ITI distribution, to compare predicted and unpredicted opto-stimulation responses. Mice were 495 trained in this task for up to 30 days, with photometry recording each day, and electrophysiology 496 recordings on some days in late training (days 11+) (see **Fiber photometry with optogenetics** and 497 **Electrophysiology recording and spike sorting** for details). 

- 498 

- 499 _Classical conditioning task with water rewards_ 

500 After standard habituation, mice started training on an odor-based classical conditioning task with water 501 rewards ( **Fig. 4** ). The two odors used were isoamyl acetate and p-cymene. In the first phase, odors were 502 paired with 100% reward delivery (4 𝜇 water) or nothing. Odors were delivered for 1 second followed 503 by a 1 second trace period. Inter-trial intervals (ITIs) were drawn from a truncated exponential 

504 distribution with mean 4 seconds and maximum 12 seconds and added to a fixed 8.5 second interval for a 505 total ITI of 8.5-20.5 seconds with mean 12.5 seconds. 80 trials of each type were delivered each day for 506 2-6 days. One mouse (MC190) started training with probabilistic reward delivery (80-90%) for 7 days 507 before switching to 100% reward delivery for 3 days. After this shaping phase, mice were switched to the 508 full task, in which the CS+ switched from 100% to 90% rewarded (in 1/10 trials, reward was omitted), 509 and rare unpredicted rewards were delivered (1 in 21 trials). After training in the full task for 1-3 days, a 510 craniotomy was performed over lNAc and muscimol or saline was injected into lNAc before the task each 511 day for up to 8 days (see **Muscimol injections** ). In some muscimol/saline sessions, we also delivered 512 novel odors (5 or 10 trials total), either interleaved with other trial types, or at the end of the recording 513 session. A different novel odor was used each day. The novel odors used were: 1-hexanol, (S)-(-)514 limonene, ethyl butyrate, (+/-)-citronellal, eugenol, 1,4-cineole, L-fenchone, α-ionone. 

- 515 

- 516 _Red masking lamp_ 

- 517 In some experiments, including all experiments in which D1-MSNs were stimulated while recording 518 dopamine signals ( **Fig. 3** , **Fig. 5** ) as well as the control experiment in **Fig. 2j** , the recording setups were 519 illuminated with red light to mask visual input from red optogenetic stimulation light. Red light 

- 520 illumination came from two lamps with red light bulbs pointed directly at the mouse’s eyes. This 521 eliminated visual dopamine responses to red light ( **Fig. 2j** ) so that optogenetic responses could be better 522 isolated. 

- 523 

- 524 **Face and body videos** 

525 In all experiments, face and body videos were recorded using infrared cameras (Blackfly BFLY-U3526 03S2M, FLIR), running at least 30 frames per second, with custom software in Bonsai (https://bonsai527 rx.org). Videos were synchronized to other data streams using TTL pulses output by BPod at the start of 528 each trial, detected by cameras’ GPIO lines and saved to file for each video frame. 

- 529 

530 **Fiber photometry with optogenetics** 

47 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

531 Photometry recordings were performed using a commercial photometry imaging system (Bundle-imaging 532 Fiber Photometry System, Doric Lenses). A branching bundle patch cord (BBP(3)_400/440/900533 0.37_1m_FCM-3xFC_LAF, Doric Lenses) was imaged by a CMOS camera (Sony IMX249LLJ) through 534 an objective. The branching patch cord split into three branches, which could be used to image up to three 535 sites simultaneously. A blue excitation LED (470 nm, 50 𝜇 power at tip of each 400 𝜇 diameter patch 536 cord, 20 ms illumination at 20 Hz) was used to collect GRABDA3m ( **Fig. 1, 3, 5** ), GCaMP8m ( **Fig. 2** ), or 537 GCaMP6f ( **Fig. 4** ) signals. A purple excitation LED (415 nm, 50 𝜇 power at tip of patch cord, 20 ms 538 illumination at 20 Hz, interleaved with blue excitation pulses) was used to collect isosbestic signals, but 539 these were only used to correct GCaMP signals as the isosbestic wavelength for GRABDA3m is not known. 540 GRABDA3m recordings were not corrected by a control channel. Instead, control GFP mice were used to 541 rule out movement artifacts, which were minimal in our head-fixed setup ( **Extended Data Fig. 1c** ). In 542 experiments in which GRABDA3m and Neuropixels recordings were made at the same site ( **Fig. 2, Fig. 3** ), 543 blue excitation light power was reduced to 20 𝜇 and purple excitation light was turned off to minimize 544 light artifacts in the Neuropixels recording. 

545 To perform photometry and optogenetics through the same optic fiber implant, red excitation light was 546 independently coupled to each of the three patch cord branches using a fluorescence minicube 547 (FMC3_(390-540)_(560-1000)_S, Doric Lenses). Each minicube contained a dichroic mirror which 548 reflected blue/green photometry light and passed red optogenetic excitation light (cutoff wavelength ≈ 549 550 nm). Each minicube had three FC connectorized ports, which were connected to: (1) one branch of 550 the bundle-branching patch cord, the other end of which connected to the Doric photometry setup, (2) a 551 635 nm red LED (CLED_635, Doric Lenses), and (3) a patch cord (MFP_400/440/110-0.37_2m_FC552 ZH1.25(F)_LAF, Doric Lenses) connecting to the corresponding fiber implant on the animal. To further 553 reduce optical crosstalk, the output of the red LED was filtered by a band-pass filter (Semrock FF01554 630/92, transmitting 580-680 nm) installed in the corresponding minicube port. Each LED’s output was 555 triggered by TTL pulses from the Bpod state machine, which controlled the behavioral task. With this 556 setup, red optogenetic excitation light could be independently delivered to each of up to three optic fiber 557 implants while simultaneously collecting photometry recordings. The lack of optical crosstalk was 558 confirmed using recordings in tdTomato control animals ( **Extended Data Fig. 1b** ). 559 

- 560 **Electrophysiological recording** 

561 Spiking data were collected using Neuropixels 1.0 single shank probes[90] or Neuropixels 2.0 four shank 562 probes[91] . Neuropixels data were acquired via a National Instruments PXI chassis (NI PXIe-1061, with NI 563 PXIe-8381 and NI PCIe-8381) with an IMEC PXIe card (IMEC PXIE_1000), recorded with SpikeGLX 564 version 20190413-phase3B2 (https://billkarsh.github.io/SpikeGLX/). Craniotomies were performed the 565 day before recording and covered with Kwik-Cast (World Precision Instruments), and mice were allowed 566 to recover overnight. On the day of recording, a 3D-printed piece was placed over the head of the mouse, 567 blocking from the mouse’s sight the experimenter manipulating the probe above the mouse’s head. Probes 568 were coated in dye (DiD, DiI, or DiO; Thermo Fisher Scientific Vybrant Multicolor Cell-Labeling Kit) to 569 visualize probe tracks in histology. Neuropixels probes were lowered using a Thorlabs micromanipulator 570 (PT1-Z8) at 1-10 𝜇 /sec. Slower speeds were used for VTA insertions. The probe was inserted 100 𝜇 571 past the target depth, then retracted to the target depth, and allowed to settle for 10-30 minutes prior to 572 starting the recording. 

48 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 573 

## 574 **Optotagging dopamine neurons** 

575 Four shank Neuropixels 2.0 probes were used to record from antidromically optotagged VTA dopamine 576 neurons projecting to lNAc ( **Fig. 1k-q** , **Fig. 3h-n** ). In the experiments of **Fig. 1** , ChrimsonR was 577 expressed in dopamine neurons by injecting 300 nL of AAV8-hSyn-FLEX-ChrimsonR-tdTomato (UNC 578 Vector Core) into the VTA of _Dat-Cre[+/-]_ mice. During the experiment dopamine axons in lNAc were 579 illuminated with red light (635 nm LED, single pulses, 20 ms pulse duration, 40 mW/mm[2] ) at the 580 beginning and end of the recording session (40 trials each); these trials were used to identify lNAc581 projecting dopamine neurons (see **Definition of optotagged neurons** ). In the experiments of **Fig. 3** , 582 ChR2 was expressed in dopamine neurons by injecting 300 nL of AAV5-Ef1a-fDIO-hChR2(H134R)583 EYFP (UNC Vector Core) into the VTA of _Dat-Flp[+/-] ;Tac1Cre[+/-]_ mice. Dopamine axons in lNAc were 584 illuminated with blue light (473 nm laser, LaserGlow, single pulses, 20 ms pulse duration, 80 mW/mm[2] ). 

- 585 

- 586 **Optotagging D1-MSNs** 

- 587 Single shank Neuropixels 1.0 probes were used to record from optotagged D1-MSNs in lNAc ( **Fig. 3a-g** 588 ChrimsonR was expressed in D1-MSNs by injecting 300 nL of AAV8-hSyn-FLEX-ChrimsonR-tdTomato 589 (UNC Vector Core) into the lNAc of _Tac1-Cre[+/-]_ mice. Optogenetic light pulses (635 nm LED, 40 590 mW/mm[2] ) were 1 ms instead of 5 ms, to separate light artifacts from light-triggered spiking responses, 591 which typically had latency ≈ 2-3 ms ( **Extended Data Fig. 6a** ). The first light pulse of the opto-stim 592 patterns ( **Fig. 3a** ) was used to identify optotagged D1-MSNs (see **Definition of optotagged neurons** ). 

- 593 

## 594 **Muscimol injections** 

- 595 Muscimol (Sigma-Aldrich M1523) was dissolved at 1ng/nL in sterile saline (0.9% NaCl) and aliquots 596 were frozen at -20ºC. Prior to experiments, an aliquot was thawed, further diluted to a final concentration 597 of 0.5ng/nL in saline, and used for several days, stored at 4ºC. One day before starting muscimol/saline 598 injections, mice were anesthetized with isoflurane, and a craniotomy was made above lNAc (from 599 bregma: AP: 1.3 mm, ML: 1.8 mm) and covered with KwikCast (World Precision Instruments). Mice 600 were allowed to recover overnight. Injections of muscimol or saline (alternating days) then occurred the 601 next day and every subsequent day for up to 8 days. For injections, mice were head-fixed and awake 602 within the recording setup. The craniotomy was exposed, rinsed with saline, and visualized using a color 603 camera (Chameleon3 CM3-U3-13S2C, FLIR). Muscimol or saline (50-100 nL) was injected into the 604 lNAc (DV: 4.0 mm) using a glass pipette (Drummond, pulled using Narishige PC-10) and oil hydraulic 605 microinjector (Narishige MO-10). After 10 minutes, the pipette was extracted from the brain. Mice then 606 rested in their home cage for 1-2 hours before starting the behavioral task and photometry recording. 

- 607 

## 608 **Multisite D1-MSN stimulation with GRABDA3m photometry** 

609 In this experiment ( **Fig. 5** ), a mirrored angled fiber was used to target DLS (MFC_400/430610 0.48_3mm_MF1.25_MA45, Doric Lenses), facing towards the lateral side, to restrict red light 

- 611 illumination to DLS. Flat faced fibers were used to target lNAc and DMS. Mice had either 2 or 3 fibers 

- 612 implanted, targeting lNAc + DLS, or lNAc + DMS + DLS. An earlier cohort of mice had DLS implants 

49 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 613 which were not useable due to experimenter error (incorrect orientation of mirrored angled fiber); in these 614 mice, only data from lNAc + DMS were analyzed. 

- 615 

- 616 **Histology** 

- 617 Following experiments, mice were deeply anesthetized with an overdose of ketamine/medetomidine, 618 exsanguinated with 0.9% phosphate buffered saline (PBS), and transcardially perfused with cold 4% 619 paraformaldehyde (PFA) in PBS. The brain was extracted from the skull and stored in 4% PFA for 24-48 620 hours at 4 ° C, after which it was rinsed with PBS, stored in PBS, and cut into 100 𝜇 sections on a 

- 621 vibratome (VT1000S, Leica). In some experiments, sections were immunostained for tyrosine 

- 622 hydroxylase (AB152, Sigma Aldrich) to visualize dopamine axons or cell bodies. Sections were mounted 623 onto glass slides with a mounting medium containing 4’,6-diamidino-2-phenylindole (DAPI; Vectashield, 624 Vector Laboratories) and imaged with an automated fluorescence microscope (Axio Scan.Z1, Zeiss) or 625 confocal microscope (LSM 700, Zeiss). 

- 626 

- 627 **Data analysis** 

- 628 Unless otherwise noted, data were analyzed with custom code written in MATLAB (version 2024a). 

- 629 

630 **Data exclusion** 

- 631 In the muscimol experiment ( **Fig. 4** , **Extended Data Fig. 7** , **Extended Data Fig. 8** ), we excluded 632 sessions in which injection (saline or muscimol) visibly failed (no movement of meniscus in glass pipette, 633 possibly due to clogging). In total, 4/30 sessions were excluded (1 saline, 3 muscimol), leaving 26 

- 634 sessions from 6 mice (16 saline, 10 muscimol). Including these sessions did not change the main pattern 635 of results. 

- 636 

## 637 **Photometry preprocessing** 

𝑑 𝑑𝑑−𝑑𝑑0 638 Raw photometry signals (F) were converted to deltaF/F (dF/F) through the formula = ~~,~~ where 𝐹𝐹0 𝑑𝑑 𝑑𝑑0 639 was defined as the 10[th] percentile of F in a rolling 30 second window. dF/F traces were upsampled from 640 20 Hz to 1000 Hz through linear interpolation (MATLAB function _interp1_ ) and then smoothed with a 

- 641 Gaussian filter (SD = 50 ms). Smoothed dF/F traces were z-scored by subtracting the mean and dividing 642 by the standard deviation of signals in the ITI periods, where ITI periods were defined by excluding time 643 points from 0.5 seconds before to 3 seconds after the start of each trial. GCaMP signals ( **Fig. 2** , **Fig. 4** ) 

- 644 were corrected by regressing out the isosbestic signal, using linear regression (function _robustfit_ in 645 MATLAB) fit to ITI periods. GRABDA3m signals were not corrected by the isosbestic channel as the 646 isosbestic wavelength for GRABDA3m is unknown, and using an incorrect isosbestic wavelength is more 647 likely to distort the signal than correct it (motion artifacts were addressed for these animals using GFP 648 control mice, e.g. **Extended Data Fig. 1c** and **Extended Data Fig. 6g** ). Photometry data were 

- 649 synchronized to behavioral data using TTL sync pulses delivered to the photometry recording setup at the 650 start of each behavioral trial. 

50 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 651 

- 652 **Spike sorting** 

- 653 Neuropixels data were spike-sorted offline with Kilosort3[92] using the ecephys pipeline (Allen Institute, 654 adapted by Jennifer Colonell for SpikeGLX data; 

- 655 https://github.com/jenniferColonell/ecephys_spike_sorting), which includes CatGT to high-pass filter the 656 raw data and detect and remove artifacts (https://github.com/billkarsh/CatGT). Kilosort clusters were then 

- 657 manually curated in Phy (https://github.com/cortex-lab/phy). After manual curation, quality control (QC) 658 metrics and mean waveforms were computed for each unit using code from the ecephys pipeline. 

- 659 Neuropixels data were synchronized to behavioral data using TTL sync pulses delivered to the SMA input 660 of the IMEC PXIe acquisition module at the beginning of each behavioral trial. 

- 661 

- 662 **Peristimulus time histograms** 

- 663 Peristimulus time histograms (PSTHs) of neural activity (spike times or photometry) or behavioral data 664 (motion energy) were computed using a MATLAB toolbox written by HyungGoo Kim 665 (https://github.com/HRKimLab/libkm). 

- 666 

- 667 **Definition of optotagged neurons** 

- 668 _Optotagged dopamine neurons_ 

669 Dopamine neurons were optotagged antidromically[93] by stimulating dopamine axons in the striatum while 670 recording spiking activity in the VTA with a 4 shank Neuropixels 2.0 probe ( **Fig. 1k,l** ). To be defined as 671 optotagged, a unit had to meet the following criteria: 

- 672 1) Pass a stimulus-associated latency test (SALT)[94] independently in two sets of 40 ( **Fig. 1k-q** ) or 60 673 ( **Fig. 3h-n** ) optotagging trials (single 20 ms pulses of light, red light for ChrimsonR in **Fig. 1** and 674 blue light for ChR2 in **Fig. 3** ) delivered at the beginning and end of the recording session (SALT 675 _P_ < 0.01 for both sets of trials). SALT compared spiking histograms from 1 to 20 ms (1 ms bins) 676 following laser onset to a null distribution taken from ITI periods. 

- 677 2) Meet the following quality control criteria based on the QC metrics output by the ecephys 678 pipeline, as recommended by the Allen Institute 679 (https://allensdk.readthedocs.io/en/latest/_static/examples/nb/ecephys_quality_metrics.html): 680 _isi_viol_ < 0.5, _amplitude_cutoff_ < 0.1, _presence_ratio_ > 0.9. These metrics ensured neurons were 681 well-isolated and present throughout the recording session. 

- 682 3) Have Pearson’s correlation at least 0.9 between mean waveform computed during light delivery 683 (“light-triggered spikes”) and outside light delivery (“spontaneous spikes”). Waveforms were 684 extracted using the software C_Waves written by Bill Karsh 

- 685 (https://github.com/billkarsh/C_Waves). 

- 686 4) Pass a collision test, a classic test of antidromic activation[93] . The first 1 ms bin following light 687 onset in which firing rate differed significantly from a shuffle control was identified (z-score to 688 shuffle > 5), which we may call 𝑡𝑡𝑟 𝑟 . Trials were identified in which spontaneous spikes 689 occurred between 𝑡𝑡𝑟 𝑟 − 7 ms and 𝑡𝑡𝑟 𝑟 − 2 ms. To pass the collision test, these trials had to 

51 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

690 have 0 spikes in the 1 ms bin at 𝑡𝑡𝑟 𝑟 . If no spontaneous spikes occurred between 𝑡𝑡𝑟 𝑟 − 7 ms 691 and 𝑡𝑡𝑟 𝑟 − 2 ms, the neuron was allowed to pass the collision test. 

- 692 5) Have mean firing rate > 0.2 Hz and < 10 Hz. 

- 693 

- 694 _Optotagged D1-MSNs_ 

695 D1-MSNs were optotagged by illuminating lNAc while recording spiking activity with a Neuropixels 1.0 696 probe ( **Fig. 3a-g** ). To be defined as optotagged, a neuron had to pass a stimulus-associated latency test 697 (SALT)[94] using the first pulse of each of the 7 stimulation patterns, excluding patterns 3 and 4 (SALT _P_ 698 0.01). Light pulse duration was 1 ms in this experiment; SALT compared spiking histograms from 2 to 6 699 ms (1 ms bins) following laser onset to a null distribution taken from ITI periods. 

- 700 

- 701 **Generating z-scored firing rate traces of single neuron spiking activity** 

- 702 Spike trains of individual neurons were transformed into smoothed z-scored firing rate traces by binning 703 spikes (1 ms bins), smoothing the binned firing rate trace with a Gaussian kernel (SD = 50 ms), and z- 704 scoring the resulting trace to ITI periods ( **Fig. 1o-q** , **Fig. 2b,c** , **Extended Data Fig. 2d-f** , **Fig. 3h-n** , 705 **Extended Data Fig. 4** ). Here ITI was defined by excluding time points from 0.5 seconds before to 3 706 seconds after the start of each trial; all other time points were labeled “ITI”. Firing rate traces were z- 707 scored by subtracting the mean and dividing by the standard deviation of ITI time points. 

- 708 

- 709 **Definition of neurons significantly excited/inhibited by odors during opto-conditioning task** 

- 710 To define neurons as “significantly excited/inhibited” by an odor (CS+ or CS-) ( **Fig. 2b,c** , **Extended** 711 **Data Fig. 4** ), trials were split into 1 second bins, spanning 1 second before odor onset to 5 seconds after 712 odor onset. The number of spikes in each of the 5 1-second bins following odor onset was compared to 713 the number of spikes in the 1-second bin preceding odor onset using a one-tailed ranksum test, separately 714 for each odor ( _n_ = number of trials). Any neuron with _P <_ 0.001 in any of these 5 comparisons was 715 deemed “significantly excited” (right tail; **Fig. 2b,c** , **Extended Data Fig. 4a-d** ) or “significantly 716 inhibited” (left tail; **Extended Data Fig. 4e** ) by the odor. 

- 717 

- 718 **Behavioral analysis** 

- 719 _Video processing_ 

- 720 Motion energy was extracted from within ROIs in each video. ROIs were drawn manually around the 

- 721 whisker pad, nose, mouth, and eye for face videos using custom MATLAB code. For body videos, the 722 ROI was defined as the whole frame (full body motion). Within each ROI, motion energy was computed 723 as the absolute value of the difference between subsequent frames. 

- 724 

- 725 **Computational modeling** 

726 

52 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 727 **Linear time-invariant (LTI) systems identification analysis** 

728 Consider an input-output system ℱ, with input denoted by 𝑢𝑢(𝑡𝑡) and output denoted by 𝑦𝑦(𝑡𝑡), such that 729 𝑦𝑦(𝑡𝑡) = ℱ(𝑢𝑢(𝑡𝑡)). This system is called linear time-invariant (LTI) if it has two properties: 730 (1) Linearity: 731 ℱ�𝑎𝑎⋅𝑢𝑢(𝑡𝑡)�= 𝑎𝑎⋅ℱ�𝑢𝑢(𝑡𝑡)� (1) 732 ℱ�𝑢𝑢1(𝑡𝑡) + 𝑢𝑢2(𝑡𝑡)�= ℱ�𝑢𝑢1(𝑡𝑡)�+ ℱ�𝑢𝑢2(𝑡𝑡)� (2) 

733 (2) Time invariance: 734 

ℱ�𝑢𝑢(𝑡𝑡−𝜏𝜏)�= 𝑦𝑦(𝑡𝑡−𝜏𝜏) (3) 

735 A system is LTI if and only if it is completely characterized by its _impulse response_ , ℎ(𝑡𝑡), i.e. the 736 response of the system to a Dirac delta function input: 

ℎ(𝑡𝑡) = ℱ�𝛿𝛿(𝑡𝑡)� (4) 

737 ℎ(𝑡𝑡) = ℱ�𝛿𝛿(𝑡𝑡)� 738 Where 𝛿𝛿(𝑡𝑡) is the Dirac delta function (not to be confused with the TD error, which we denote 𝑇 (𝑡𝑡)). 739 This means that (with zero initial condition), the output of an LTI system is equal to the convolution of 740 the input with the impulse response (convolution denoted as ∗): 

𝑦𝑦(𝑡𝑡) = ℎ(𝑡𝑡) ∗𝑢𝑢(𝑡𝑡) (5) 

741 

742 By taking the Laplace transform of both sides of equation 5, we can turn the convolution into a product 743 (the _convolution theorem_ of Laplace transforms): 744 𝑌𝑌(𝑠𝑠) = 𝐻𝐻(𝑠𝑠) ⋅𝑈𝑈(𝑠𝑠) 

𝑌𝑌(𝑠𝑠) = 𝐻𝐻(𝑠𝑠) ⋅𝑈𝑈(𝑠𝑠) (6) 

745 𝐻𝐻(𝑠𝑠), known as the _transfer function_ of the system, is the Laplace transform of the system’s impulse 746 response, and conversely, the impulse response ℎ(𝑡𝑡) is the inverse Laplace transform of the transfer 747 function: 748 𝐻𝐻(𝑠𝑠) = ℒ{ℎ(𝑡𝑡)} 749 ℎ(𝑡𝑡) = ℒ[−1] {𝐻𝐻(𝑠𝑠)} 750 It is useful to consider the subset of all possible transfer functions 𝐻𝐻(𝑠𝑠) which can be expressed as the 

**==> picture [277 x 34] intentionally omitted <==**

751 ratio of two polynomials with real coefficients 𝐾𝐾, 𝑎𝑎𝑚𝑚, and 𝑏𝑏𝑗𝑗, with the numerator having order 𝜇𝜇 and the 752 denominator having order 𝑛𝑛: 

**==> picture [335 x 31] intentionally omitted <==**

753 𝐻𝐻(𝑠𝑠) = 𝐾𝐾 𝑠𝑠[𝑚𝑚] + 𝑎𝑎𝑚𝑚−1𝑠𝑠[𝑚𝑚−1] + ⋯+ 𝑎𝑎1𝑠𝑠+ 𝑎𝑎0 754 This ratio-of-polynomials form can be factored as follows (fundamental theorem of algebra): 

**==> picture [313 x 30] intentionally omitted <==**

755 

756 Where these roots, 𝜎𝜎𝑚𝑚 and 𝜌𝜌𝑗𝑗, are complex numbers and are known as the “zeros” and “poles” of the 757 system, respectively. As will be seen, the zeros and poles are very useful for interpreting and 758 understanding the system dynamics. Many real-world LTI systems have 𝐻𝐻(𝑠𝑠) with this form, but some do 759 not (e.g. a strict time delay between input and output cannot be expressed this way). 

53 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

760 When 𝐻𝐻(𝑠𝑠) has this form, then the system is equivalent to a linear differential equation with constant 761 coefficients, as follows: 

762 

**==> picture [382 x 31] intentionally omitted <==**

763 Rearranging terms: 

**==> picture [504 x 15] intentionally omitted <==**

765 Taking the inverse Laplace transform of both sides: 

766 

**==> picture [445 x 19] intentionally omitted <==**

767 Where the last step follows from the derivative property of Laplace transforms (ℒ{𝑓𝑓[′] (𝑡𝑡)} = 𝑠𝑠⋅ℒ{𝑓𝑓(𝑡𝑡)}). 768 Transforming the system into this form is useful for comparing it to the TD equation, which in the 

769 absence of rewards is a linear differential equation with 𝜇𝜇= 1 (1 zero), 𝑛𝑛= 0 (0 poles), K = 1, and 𝑏𝑏0 = 770 𝜎𝜎1 = ln 𝛾𝛾 (see **The TD equation is an LTI system in the absence of rewards** ). 

771 Real biological systems are neither linear (e.g. neurons have threshold non-linearities) nor time-invariant 772 (e.g. brain states like arousal fluctuate over seconds to minutes). We wished to understand the extent to 773 which the transformation from striatal D1-MSN spiking to midbrain dopamine activity (spiking or 774 release) can be described as an LTI system (i.e., how good of an approximation is this?), and to find the 775 best fit ℎ(𝑡𝑡) describing this transformation (what is its shape? How many zeros and poles are needed to 776 describe the system?). Finally, we wished to relate this empirical ℎ(𝑡𝑡) to the TD equation, which is itself 777 an LTI system in the absence of rewards, transforming the value function 𝑉𝑉(𝑡𝑡) into the TD error 𝑇 (𝑡𝑡) by 778 convolving with the TD impulse response, ℎ𝑇 (𝑡𝑡) (see **The TD equation is an LTI system in the** 779 **absence of rewards** ). 780 

781 **The TD equation is an (improper) LTI system in the absence of rewards** 

782 The continuous form of the TD equation is[21] : 

783 

**==> picture [313 x 12] intentionally omitted <==**

784 In the absence of rewards (𝑟𝑟(𝑡𝑡) = 0), this reduces to: 

785 

**==> picture [296 x 12] intentionally omitted <==**

786 This is an improper (non-causal) LTI system with 0 poles and 1 zero, 𝜎𝜎1 = −ln (𝛾𝛾). The TD equation 787 outputs zero when: 

**==> picture [504 x 27] intentionally omitted <==**

789 The TD equation with 𝑟𝑟(𝑡𝑡) = 0 is equivalent to convolving the value function 𝑉𝑉(𝑡𝑡) with an impulse 790 response function, which we call the “TD impulse response” or ℎ𝑇 (𝑡𝑡): 791 ℎ (𝑡𝑡) = 𝛿𝛿[′] (𝑡𝑡) + ln 𝛾𝛾⋅𝛿𝛿(𝑡𝑡) 

**==> picture [299 x 34] intentionally omitted <==**

792 

54 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

- 793 Where 𝛿𝛿(𝑡𝑡) is the Dirac delta function and 𝛿𝛿′(𝑡𝑡) is the derivative of the Dirac delta function. 

- 794 

- 795 

## **Fitting LTI models to data** 

796 To fit LTI models to data ( **Fig. 3d-n** , **Fig. 5c-e** , **Extended Data Fig. 6e-m** , **Extended Data Fig. 9** ), we 797 used MATLAB’s System Identification Toolbox, specifically the function _tfest_ . LTI models were fit to the 798 average PSTH for each stimulation pattern. To fit an order _n_ model we used _tfest_ with _n_ zeros and _n_ + 1 799 poles (e.g. **Fig. 3f** ). No regularization was used. Cross-validated R[2] was computed by fitting the model on 800 6 of 7 stimulation patterns and predicting the response to the held-out pattern; these held-out predictions − 801 were concatenated across the 7 patterns, and cross-validated R[2] was computed as 1 − ∑(𝑦𝑖 𝑦𝑦�𝑖)[2] , where 𝑦𝑦𝑚𝑚 ∑(𝑦𝑦𝑖𝑖−𝑦𝑦�)[2] 802 is the true value of the average PSTH at time-point 𝑖𝑖, 𝑦𝑦�𝚤𝚤 is the prediction of the LTI model, and 𝑦𝑦� is the 803 mean of all 𝑦𝑦𝑚𝑚. To fit to a derivative model (order 1 model with 𝜎𝜎1 fixed at 0), we first calculated the 804 derivative of the input (MATLAB function _diff_ ), forcing 𝜎𝜎1 = 0, and then fit an LTI model with 0 zeros 805 and 2 poles. The cross-validated R[2] of this model was compared against that of a full order 1 LTI model 806 with 1 zero and 2 poles ( **Fig. 3g,k** , **Extended Data Fig. j-l** ). 

- 807 

## 808 

## **Estimating** 𝜸𝜸 **from bootstrapped dopamine neuron population activity** 

- 809 We estimated 𝛾𝛾 from bootstrapped dopamine neuron population activity as follows. First, we sampled 55 810 optotagged dopamine neurons randomly with replacement from the full set of 55 neurons. Then we 811 computed the average PSTH of this bootstrapped population and re-fit the LTI model (1 zero, 2 poles) 

- 812 predicting the average PSTH from the stimulation patterns. The estimated gamma, 𝛾𝛾�, was computed using 813 the formula 𝛾𝛾�= 𝑒𝑒[−𝜎𝜎][1] , where 𝜎𝜎1 is the zero of the LTI fit (see above for derivation). This process was 

814 repeated 1000 times to generate the histogram in **Fig. 3m** . For each bootstrap, we also computed the ratio 815 P/N (the ratio of the positive and negative areas of the fit impulse response). We plotted P/N against 𝛾𝛾� 816 across all 1000 bootstraps in **Fig. 3o** . The black line in **Fig. 3o** shows an exponential curve of the form 817 𝑎𝑎𝑒𝑒[𝑏] + 𝑐𝑐, fit to the data using the MATLAB function _fit_ . 

55 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## 818 

## **Acknowledgements** 

- 819 We thank HyungGoo Kim for help setting up the antidromic optotagging technique; Ryunosuke Amo for 820 technical advice; Edward Soucy, Brett Graham, and Yuwei Li of the Harvard Neurotechnology Core for 

- 821 engineering assistance; the Harvard Center for Biological Imaging for imaging support; Harvard FAS 

- 822 Research Computing for computing support; Bernardo Sabatini, Samuel Gershman, and Peter Dayan for 

- 823 critical feedback; and all Uchida lab members for their input. This work was supported by grants from the 824 National Institute of Health (NIH) (5U19NS113201 to N.U. and 5R01DA05975 to N.U. and M.W.-U.) 

- 825 and the Simons Collaboration on Global Brain (to N.U.). M.G.C. is supported by a NIH K99/R00 826 Pathway to Independence Award (1K99DA060290). 

- 827 

- 828 **Author contributions** 

- 829 M.G.C. and N.U. designed the experiments. M.G.C., Y.R., Z.C., and S.X. collected data. S.M. assisted 

- 830 with establishing experimental procedures. M.G.C., Z.C., and M.B. developed the LTI analysis 

- 831 framework. M.G.C. analyzed the data. M.G.C. wrote the first draft of the manuscript and created the 832 figures. All authors edited the manuscript. 

- 833 

- 834 **Competing interests** 

- 835 The authors declare no competing interests. 

- 836 

## 837 **Data and code availability** 

- 838 Data and code will be posted to online repositories upon publication. 

56 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

## **References** 

1. Schultz, W., Dayan, P. & Montague, P. R. A neural substrate of prediction and reward. _Science_ **275** , 1593–1599 (1997). 

2. Bayer, H. M. & Glimcher, P. W. Midbrain dopamine neurons encode a quantitative reward prediction error signal. _Neuron_ **47** , 129–141 (2005). 

3. Steinberg, E. E. _et al._ A causal link between prediction errors, dopamine neurons and learning. _Nat. Neurosci._ **16** , 966–973 (2013). 

4. Amo, R. _et al._ A gradual temporal shift of dopamine responses mirrors the progression of temporal difference error in machine learning. _Nat. Neurosci._ 1–11 (2022). 

5. Kim, H. R. _et al._ A Unified Framework for Dopamine Signals across Timescales. _Cell_ **183** , 16001616.e25 (2020). 

6. Howhy, J. _The Predictive Mind_ . (Oxford University Press, Oxford, England, 2013). 

7. Sutton, R. S. Learning to predict by the methods of temporal differences. _Mach. Learn._ **3** , 9–44 (1988). 

8. Sutton, R. S. & Barto, A. G. _Reinforcement Learning, Second Edition: An Introduction_ . (MIT Press, 2018). 

9. Arulkumaran, K., Deisenroth, M. P., Brundage, M. & Bharath, A. A. Deep reinforcement learning: A brief survey. _IEEE Signal Process. Mag._ **34** , 26–38 (2017). 

10. Lillicrap, T. P. _et al._ Continuous control with deep reinforcement learning. _arXiv [cs.LG]_ (2015). 

11. Mnih, V. _et al._ Human-level control through deep reinforcement learning. _Nature_ **518** , 529–533 (2015). 

12. Ainslie, G. Specious reward: a behavioral theory of impulsiveness and impulse control. _Psychol. Bull._ **82** , 463–496 (1975). 

13. Frederick, S., Loewenstein, G. & O’donoghue, T. Time discounting and time preference: A critical review. _J. Econ. Lit._ **40** , 351–401 (2002). 

14. Mischel, W., Shoda, Y. & Rodriguez, M. I. Delay of gratification in children. _Science_ **244** , 933–938 (1989). 

15. Jeong, H. _et al._ Mesolimbic dopamine release conveys causal associations. _Science_ **378** , eabq6740 (2022). 

16. Coddington, L. T., Lindo, S. E. & Dudman, J. T. Mesolimbic dopamine adapts the rate of learning from action. _Nature_ **614** , 294–302 (2023). 

17. Hamid, A. A. _et al._ Mesolimbic dopamine signals the value of work. _Nat. Neurosci._ **19** , 117–126 (2016). 

18. Qian, L. _et al._ Prospective contingency explains behavior and dopamine signals during associative learning. _Nat. Neurosci._ 1–13 (2025). 

19. Howe, M. W., Tierney, P. L., Sandberg, S. G., Phillips, P. E. M. & Graybiel, A. M. Prolonged dopamine signalling in striatum signals proximity and value of distant rewards. _Nature_ **500** , 575–579 (2013). 

20. Mohebi, A. _et al._ Dissociable dopamine dynamics for learning and motivation. _Nature_ **570** , 65–70 (2019). 

21. Mikhael, J. G., Kim, H. R., Uchida, N. & Gershman, S. J. The role of state uncertainty in the dynamics of dopamine. _Curr. Biol._ **32** , 1077-1087.e9 (2022). 

57 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

22. Gershman, S. Dopamine ramps are a consequence of reward prediction errors. _Neural Comput._ **26** , 467–471 (2014). 

23. Chang, C. Y. _et al._ Brief optogenetic inhibition of dopamine neurons mimics endogenous negative reward prediction errors. _Nat. Neurosci._ **19** , 111–116 (2016). 

24. Maes, E. J. P. _et al._ Causal evidence supporting the proposal that dopamine transients function as temporal difference prediction errors. _Nat. Neurosci._ **23** , 176–178 (2020). 

25. Houk, J. C., Davis, J. L. & Beiser, D. G. _Models of Information Processing in the Basal Ganglia_ . (MIT Press, 1995). 

26. Kawato, M. & Samejima, K. Efficient reinforcement learning: computational theories, neuroscience and robotics. _Curr. Opin. Neurobiol._ **17** , 205–212 (2007). 

27. Keiflin, R. & Janak, P. H. Dopamine Prediction Errors in Reward Learning and Addiction: From Theory to Neural Circuitry. _Neuron_ **88** , 247–263 (2015). 

28. Parker, N. F. _et al._ Choice-selective sequences dominate in cortical relative to thalamic inputs to NAc to support reinforcement learning. _Cell Rep._ **39** , 110756 (2022). 

29. Cromwell, H. C. & Schultz, W. Effects of expectations for different reward magnitudes on neuronal activity in primate striatum. _J. Neurophysiol._ **89** , 2823–2838 (2003). 

30. Samejima, K., Ueda, Y., Doya, K. & Kimura, M. Representation of action-specific reward values in the striatum. _Science_ **310** , 1337–1340 (2005). 

31. Ito, M. & Doya, K. Distinct neural representation in the dorsolateral, dorsomedial, and ventral parts of the striatum during fixed- and free-choice tasks. _J. Neurosci._ **35** , 3499–3514 (2015). 

32. Lowet, A. S. _et al._ An opponent striatal circuit for distributional reinforcement learning. _Nature_ **639** 717–726 (2025). 

33. Cox, J. & Witten, I. B. Striatal circuits for reward learning and decision-making. _Nat. Rev. Neurosci._ **20** , 482–494 (2019). 

34. Lammel, S. _et al._ Input-specific control of reward and aversion in the ventral tegmental area. _Nature_ **491** , 212–217 (2012). 

35. Menegas, W., Akiti, K., Amo, R., Uchida, N. & Watabe-Uchida, M. Dopamine neurons projecting to the posterior striatum reinforce avoidance of threatening stimuli. _Nat. Neurosci._ **21** , 1421–1430 (2018). 

36. Saunders, B. T., Richard, J. M., Margolis, E. B. & Janak, P. H. Dopamine neurons create Pavlovian conditioned stimuli with circuit-defined motivational properties. _Nat. Neurosci._ **21** , 1072–1083 (2018). 

37. Farassat, N. _et al._ In vivo functional diversity of midbrain dopamine neurons within identified axonal projections. _Elife_ **8** , (2019). 

38. de Jong, J. W. _et al._ A Neural Circuit Mechanism for Encoding Aversive Stimuli in the Mesolimbic Dopamine System. _Neuron_ **101** , 133-151.e7 (2019). 

39. de Jong, J. W., Liang, Y., Verharen, J. P. H., Fraser, K. M. & Lammel, S. State and rate-of-change encoding in parallel mesoaccumbal dopamine pathways. _Nat. Neurosci._ **27** , 309–318 (2024). 

40. Klapoetke, N. C. _et al._ Independent optical excitation of distinct neural populations. _Nat. Methods_ **11** , 338–346 (2014). 

41. Zhuo, Y. _et al._ Improved green and red GRAB sensors for monitoring dopaminergic activity in vivo. _Nat. Methods_ 1–12 (2023). 

42. Oettl, L.-L. _et al._ Phasic dopamine reinforces distinct striatal stimulus encoding in the olfactory tubercle driving dopaminergic reward prediction. _Nat. Commun._ **11** , 3460 (2020). 

58 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

43. Yagishita, S. _et al._ A critical time window for dopamine actions on the structural plasticity of dendritic spines. _Science_ **345** , 1616–1619 (2014). 

44. Iino, Y. _et al._ Dopamine D2 receptors in discrimination learning and spine enlargement. _Nature_ **579** , 555–560 (2020). 

45. Lee, S. J. _et al._ Cell-type-specific asynchronous modulation of PKA by dopamine in learning. _Nature_ **590** , 451–456 (2021). 

46. Long, C. _et al._ Constraints on the subsecond modulation of striatal dynamics by physiological dopamine signaling. _Nat. Neurosci._ **27** , 1977–1986 (2024). 

47. Masset, P. _et al._ Multi-timescale reinforcement learning in the brain. _Nature_ **642** , 682–690 (2025). 

48. Ljung, L. _System Identification: Theory for the User, Second Edition_ . (Prentice Hall, 1998). 

49. Kramer, P. F., Twedell, E. L., Shin, J. H., Zhang, R. & Khaliq, Z. M. Axonal mechanisms mediating γ-aminobutyric acid receptor type A (GABA-A) inhibition of striatal dopamine release. _Elife_ **9** , (2020). 

50. Howe, M. W. & Dombeck, D. A. Rapid signalling in distinct dopaminergic axons during locomotion and reward. _Nature_ **535** , 505–510 (2016). 

51. Coddington, L. T. & Dudman, J. T. The timing of action determines reward prediction signals in identified midbrain dopamine neurons. _Nat. Neurosci._ **21** , 1563–1573 (2018). 

52. Engelhard, B. _et al._ Specialized coding of sensory, motor and cognitive variables in VTA dopamine neurons. _Nature_ **570** , 509–513 (2019). 

53. Watabe-Uchida, M. & Uchida, N. Multiple Dopamine Systems: Weal and Woe of Dopamine. _Cold Spring Harb. Symp. Quant. Biol._ **83** , 83–95 (2018). 

54. Tsutsui-Kimura, I. _et al._ Distinct temporal difference error signals in dopamine axons in three regions of the striatum in a decision-making task. _Elife_ **9** , (2020). 

55. Verharen, J. P. H., Zhu, Y. & Lammel, S. Aversion hot spots in the dopamine system. _Curr. Opin. Neurobiol._ **64** , 46–52 (2020). 

56. Bogacz, R. Dopamine role in learning and action inference. _Elife_ **9** , (2020). 

57. Akiti, K. _et al._ Striatal dopamine explains novelty-induced behavioral dynamics and individual variability in threat prediction. _Neuron_ **110** , 3789-3804.e9 (2022). 

58. Lee, R. S., Sagiv, Y., Engelhard, B., Witten, I. B. & Daw, N. D. A feature-specific prediction error model explains dopaminergic heterogeneity. _Nat. Neurosci._ **27** , 1574–1586 (2024). 

59. Mohebi, A., Wei, W., Pelattini, L., Kim, K. & Berke, J. D. Dopamine transients follow a striatal gradient of reward time horizons. _Nat. Neurosci._ **27** , 737–746 (2024). 

60. Calipari, E. S., Huggins, K. N., Mathews, T. A. & Jones, S. R. Conserved dorsal-ventral gradient of dopamine release and uptake rate in mice, rats and rhesus macaques. _Neurochem. Int._ **61** , 986–991 (2012). 

61. Critchfield, T. S. & Kollins, S. H. Temporal discounting: basic research and the analysis of socially important behavior. _J. Appl. Behav. Anal._ **34** , 101–122 (2001). 

62. _Time and Decision: Economic and Psychological Perspectives of Intertemporal Choice_ . (Russell Sage Foundation Publications, 2003). doi:10.7758/9781610443661. 

63. Story, G. W., Vlaev, I., Seymour, B., Darzi, A. & Dolan, R. J. Does temporal discounting explain unhealthy behavior? A systematic review and reinforcement learning perspective. _Front. Behav. Neurosci._ **8** , 76 (2014). 

64. Matousek, J., Havranek, T. & Irsova, Z. Individual discount rates: a meta-analysis of experimental evidence. _Exp. Econ._ **25** , 318–358 (2022). 

59 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

65. Vuchinich, R. E. & Simpson, C. A. Hyperbolic temporal discounting in social drinkers and problem drinkers. _Exp. Clin. Psychopharmacol._ **6** , 292–305 (1998). 

66. Enomoto, K., Matsumoto, N., Inokawa, H., Kimura, M. & Yamada, H. Topographic distinction in long-term value signals between presumed dopamine neurons and presumed striatal projection neurons in behaving monkeys. _Sci. Rep._ **10** , 8912 (2020). 

67. Ainslie, G. & Haslam, N. Hyperbolic discounting. _Choice over time_ **5** , 57–92 (1992). 

68. Laibson, D. Golden eggs and hyperbolic discounting. _Quarterly Journal of Economics_ **112** , 443–478 (1997). 

69. Hayden, B. Y. Time discounting and time preference in animals: A critical review. _Psychon. Bull. Rev._ **23** , 39–53 (2016). 

70. Kurth-Nelson, Z. & Redish, A. D. Temporal-difference reinforcement learning with distributed representations. _PLoS One_ **4** , e7362 (2009). 

71. Peters, A. J., Fabre, J. M. J., Steinmetz, N. A., Harris, K. D. & Carandini, M. Striatal activity topographically reflects cortical activity. _Nature_ (2021) doi:10.1038/s41586-020-03166-8. 

72. Tsutsui-Kimura, I. _et al._ Dopamine in the tail of the striatum facilitates avoidance in threat-reward conflicts. _Nat. Neurosci._ **28** , 795–810 (2025). 

73. Greenstreet, F. _et al._ Dopaminergic action prediction errors serve as a value-free teaching signal. _Nature_ 1–10 (2025). 

74. Lutas, A. _et al._ State-specific gating of salient cues by midbrain dopaminergic input to basal amygdala. _Nat. Neurosci._ **22** , 1820–1833 (2019). 

75. Costa, V. D., Dal Monte, O., Lucas, D. R., Murray, E. A. & Averbeck, B. B. Amygdala and Ventral Striatum Make Distinct Contributions to Reinforcement Learning. _Neuron_ **92** , 505–517 (2016). 

76. Liu, C. _et al._ An action potential initiation mechanism in distal axons for the control of dopamine release. _Science_ **375** , 1378–1385 (2022). 

77. Harkin, E. F. _et al._ Temporal derivative computation in the dorsal raphe network revealed by an experimentally driven augmented integrate-and-fire modeling framework. _Elife_ **12** , (2023). 

78. Nagel, K. I. & Wilson, R. I. Biophysical mechanisms underlying olfactory receptor neuron dynamics. _Nat. Neurosci._ **14** , 208–216 (2011). 

79. Liss, B. & Roeper, J. 3.4 Ion channels and regulation of dopamine neuron activity. _Dopamine handbook_ **118** , (2010). 

80. Stetsenko, A. & Koos, T. Neuronal implementation of the temporal difference learning algorithm in the midbrain dopaminergic system. _Proc. Natl. Acad. Sci. U. S. A._ **120** , e2309015120 (2023). 

81. Abbott, L. F., Varela, J. A., Sen, K. & Nelson, S. B. Synaptic depression and cortical gain control. _Science_ **275** , 220–224 (1997). 

82. Eshel, N. _et al._ Arithmetic and local circuitry underlying dopamine prediction errors. _Nature_ **525** , 243–246 (2015). 

83. Watabe-Uchida, M., Eshel, N. & Uchida, N. Neural Circuitry of Reward Prediction Error. _Annu. Rev. Neurosci._ **40** , 373–394 (2017). 

84. Liu, Z. _et al._ A distinct D1-MSN subpopulation down-regulates dopamine to promote negative emotional state. _Cell Res._ **32** , 139–156 (2022). 

85. Grace, A. A. & Bunney, B. S. Induction of depolarization block in midbrain dopamine neurons by repeated administration of haloperidol: analysis using in vivo intracellular recording. _J. Pharmacol. Exp. Ther._ **238** , 1092–1100 (1986). 

60 

bioRxiv preprint doi: https://doi.org/10.1101/2025.09.18.677203; this version posted September 18, 2025. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY 4.0 International license. 

86. Tucker, K. R., Huertas, M. A., Horn, J. P., Canavier, C. C. & Levitan, E. S. Pacemaker rate and depolarization block in nigral dopamine neurons: a somatic sodium channel balancing act. _J. Neurosci._ **32** , 14519–14531 (2012). 

87. Groves, P. M., Wilson, C. J., Young, S. J. & Rebec, G. V. Self-inhibition by dopaminergic neurons. _Science_ **190** , 522–528 (1975). 

88. Yang, H. _et al._ Nucleus Accumbens Subnuclei Regulate Motivated Behavior via Direct Inhibition and Disinhibition of VTA Dopamine Subpopulations. _Neuron_ **97** , 434-449.e4 (2018). 

89. Cohen, J. Y., Haesler, S., Vong, L., Lowell, B. B. & Uchida, N. Neuron-type-specific signals for reward and punishment in the ventral tegmental area. _Nature_ **482** , 85–88 (2012). 

90. Jun, J. J. _et al._ Fully integrated silicon probes for high-density recording of neural activity. _Nature_ **551** , 232–236 (2017). 

91. Steinmetz, N. A. _et al._ Neuropixels 2.0: A miniaturized high-density probe for stable, long-term brain recordings. _Science_ **372** , eabf4588 (2021). 

92. Pachitariu, M., Sridhar, S. & Stringer, C. Solving the spike sorting problem with Kilosort. _bioRxiv_ 2023.01.07.523036 (2023) doi:10.1101/2023.01.07.523036. 

93. Lipski, J. Antidromic activation of neurones as an analytic tool in the study of the central nervous system. _J. Neurosci. Methods_ **4** , 1–32 (1981). 

94. Kvitsiani, D. _et al._ Distinct behavioural and network correlates of two interneuron types in prefrontal cortex. _Nature_ **498** , 363–366 (2013). 

61 

