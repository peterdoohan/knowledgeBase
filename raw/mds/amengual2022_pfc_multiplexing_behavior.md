bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## **The cost of multiplexing: PFC integrates multiple sources of information in** 

## **non-orthogonal components accounting for behavioral variability** 

Julian L Amengual[1] , Fabio Di Bello[1] , Sameh Ben Hadj Hassen[1] , Elaine Astrand[1] and Suliann Ben 

Hamed[1] 

1. Institut des Sciences Cognitives Marc Jeannerod, CNRS UMR 5229, Université Claude Bernard Lyon I, Bron, 69500 France. 

## Abstract 

The frontal eye field (FEF) is a prefrontal cortical area classically associated with spatial attention, perception, and oculomotor functions. FEF exhibits complex response properties through mixed selectivity neurons, allowing a high dimensional representation of the information. However, recent studies have shown that FEF encodes information in a low-dimensional regime hence limiting the coding capacity of the neural population. How the FEF encodes multiple sources of information with such limited encoding capacity remains elusive. To address this question, we trained two macaques to perform a visual attention task while we recorded FEF neuronal activity using multi-contact electrodes. FEF neurons encoded task- (spatial location of cue, POS; time in trial, CTOA) and behaviour(reaction time, RT; focus of attention, TA) related parameters prior to target onset. We found a clear modulation of the RT and TA as a function of the CTOA. Using dPCA, we characterized the functional relationship between neural populations associated with each parameter and investigated how this functional relationship predicts behavior. We found that CTOA variability was associated to two different components the activation of which was correlated with the TA and the RT, respectively. These CTOA related components were non-orthogonal with the RT and TA related components. These results suggest that when different sources of information are implemented during task performance, they show a very precise geometrical configuration in non-orthogonal components. This allows high simultaneous information encoding capacity at the cost of an impaired capacity to use attention information and an enhanced responsiveness toward external stimuli. 

1 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## Keywords 

Prefrontal cortex, FEF, Attention, temporal discounting, reaction times, Multiplexing, Mixed-selectivity, Low-Dimensional representation, Behavior 

## Introduction 

One fundamental question in neuroscience is how the brain organizes multiple sources of information to produce behavior. In this context, it is essential to identify which components explain variability in performance, how these components interact at neural level and how cognition emerges from this interaction. Given its rich connectivity with cortical sensory and high-order association areas, and subcortical structures associated with different cognitive aspects such as memory, the prefrontal cortex (PFC) is a crucial brain node that codes and combines multiple sources of information during task performance (1–5). Neurophysiology studies have revealed that the PFC holds neurons that exhibit complex response properties that reflect _simultaneously_ the coding of different task- and behavior- related parameters, a property that is called mixed-selectivity (6–9). This property plays a crucial computational role because it is related to the dimensionality of the neural representations (7), as these cells allow a high dimensional representation of the information in orthogonal (i.e. mathematically independent) components. This is considered an advantage both in facilitating the readout of the information of interest and in implementing a larger number of cognitive computations. On the other hand, it has been proposed that prefrontal cortex actually works in a low-dimensional regime, as the brain activity only visits a small fraction of all its potential states, hence reducing the coding capacity of the neural population (10–12). An open question in the field is thus how the PFC encodes multiple sources of information with such a limited capacity of encoding imposed by the lowdimensional representation of the activity. To address this, it is necessary to have access to the lowdimensional representation of the neuronal populations and to study whether these components are associated with specific sources of neuronal variance and how these components interact to produce specific patterns of behavior. In other words, the question is to what extent the coding of different parameters is performed by orthogonal representations of the information in the PFC and, if not, what are the behavioral implications of the non-orthogonalization. 

The low-dimensional structure of the neural recordings can be analyzed using dimensionality reduction methods (13). In particular, demixed PCA (14) allows the extraction of components the variance of 

2 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

which are linked to specific parameters related with the task or to the subjects behavior without imposing the orthogonalization constraint (11,15) (in contrast to the PCA where principal axes are all orthogonal). In a recent study, we used dPCA to show that the decoded position of attention in space and the behavioral outcome lie in different but non-orthogonal components. The degree of nonorthogonality varied from one session to the next and accounted for the behavioral gain associated with the prefrontal implementation of attention: the more orthogonal these components were, the higher the behavioral gain associated with prefrontal attentional function. This observation suggests that non-orthogonality might be a strategy of the PFC to encode multiple sources of information and might come at the cost of a functional and behavioral interaction between these sources. 

In the present study, we analyzed electrophysiology data from intracranial recordings in the frontal eye field (FEF, bilaterally) of two monkeys performing 100% validity-cued visual attention task. This PFC region plays a key role in the voluntary (16,17) and dynamic (18–22) allocation of attention. We show that the recorded cells encode multiple sources of information simultaneously accounting for the instructed attention position, the attentional focus (i.e. the spatial precision with which attention instruction was implemented), the time progression in the trial and the reaction time. Using dPCA, we identify the demixed components accounting for the variance associated with these sources of information. We show that the components associated with the time progression in the trial are nonorthogonal to the components associated with both the reaction time and the attentional focus. In addition, we show that each of these components account for behavioral variability and information overlap between components. Overall, this work provides evidence of the rich capacity of the FEF to encode multiple sources of information in non-orthogonal representations, and describes the behavioral implications of such coding strategies. 

## Results 

Two rhesus macaque monkeys (M1 and M2) performed a 100% validity spatially cued target detection task consisting in responding to a change in luminosity of a spatially pre-cued landmark located in one of the four quadrants of a screen (Figure 1A), receiving liquid rewards for correct detection. In ~60% (IQR: 3) of the trials, monkeys were exposed to one or several changes of luminosity of uncued landmarks during the cue-to-target time interval (CTOA). These acted as distractors and had to ignore. 

3 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

When monkeys responded to these distractors, the current trial was considered a False Alarm (FA) 

and they were not rewarded. 

**==> picture [427 x 117] intentionally omitted <==**

_**Figure 1.**_ (A) 100% validity cued target-detection task with distractors. In order to initiate the trial, monkeys had to hold a bar with the hand and fixate their gaze on a central cross on the screen. Monkeys received liquid reward for releasing the bar manually 150-750 ms after target presentation onset. Target location was indicated by a spatial cue presented centrally (green square). Monkeys had to ignore any uncued event (distractors). (B) Barplot showing the percentage of hit rate, the percentage of false alarms, reaction time of hits and reaction time of false alarms of each monkey (M1 and M2) separately. 

Monkeys M1 and M2 achieved 55.6% and 76.2% correct responses, respectively. Median reaction times of these responses were 502 ms (IQR: 14) for M1 and 472 ms (IQR: 7) for M2. FA rate to distractors was 10.5% (IQR: 3.7) for M1 and 13.4% (IQR: 6) for M2. Median reaction times of FA responses were 524 ms (IQR: 63) for M1 and 439 ms (IQR: 78) for M2 (Figure 1B). This type of behaviour is classically taken as an indication that the cue provides monkeys with advanced knowledge about relevant task items, allowing them to orient their spatial attention towards expected target location (18,23,24), enhance their perceptual sensitivity (25,26) and prepare their behavioural response (21,27). In the following, we further show that this task imposes the interaction between different cognitive processes (attention, temporal expectation and motor readiness) all of which are encoded in the FEF and contribute to overall neuronal variance. 

## Selective spatial attention is encoded in the FEF 

MUA was obtained from 848 contacts implanted in the FEF (Figure 2A), a structure that is known to play a key role in covert spatial attention (16,28,29), while monkeys were performing the cued detection task. Overall, we found that 68.4% of all units had a significant activation to both the cue and target onsets (Wilcoxon paired test, p < 0.05), and 65% of these active units showed higher spiking rate in the post target epoch ([0-400] ms) than in the pre-target epoch. Reproducing previous reports on FEF neuronal responses (21,22,30,31), we studied task-related modulations of MUA responses by comparing neuronal activity when attention was cued to the most preferred or the least preferred 

4 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

visual quadrant of each neuron. Figure 2B shows that the spiking rates were higher when preferred location was cued (time period 100 ms to 400 ms post cue onset, Figure 2B, left). This higher firing rate regime associated to the preferred cueing location was sustained along the trial up to target presentation (Figure 2B, right). 

Firing rate differences between the preferred and the anti-preferred quadrant were converted into a modulation index, ranging from -1 to 1. Positive (negative) values of this index indicated higher activity at the preferred (anti-preferred) location. Median modulation index of the entire population was 0.008 (65% of units showing significant modulation, median significantly modulated units: 0.023, Figure 2C in red) and the distribution of index values was significantly greater than zero (p < 0.0001, Wilcoxon paired test) (Figure 2C). In addition, we tested whether the FEF encoded the cue position (selective spatial attention). Supplementary figure 1A shows the firing rates averaged across all MUA channels (n=848) locked to the cue, per each cue position. At the post cue interval of [0-400 ms], the 75% of cells showed cue-position tuning. Overall, these results show that the recorded activity is sensitive to spatial attention, a well-documented property of FEF neurons. 

**==> picture [238 x 231] intentionally omitted <==**

**Figure 2 Location of electrophysiological recordings and characterization of their attentional modulation** . (A) On each session, one 24-contact recording probe was placed in each FEF. (B) Single MUA mean (± s.e.) locked to the cue onset (left) and target onset (right) associated to when the cue is orienting attention towards the preferred (black) or the anti-preferred (gray) spatial locations (C) Distribution of attention modulation index (Preferred - Anti-preferred)/(Preferred + Anti-Preferred), computed over 200 ms before target onset across all MUAs of all sessions. Red histogram corresponds to channels in which the neuronal activity during this time interval was significantly different between the preferred and the anti-preferred spatial attention responses (Wilcoxon test, p<0.05). 

5 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## FEF encodes time-expectation, focus of attention and motor response related information 

In addition to the cued spatial attention information, we investigated whether other sources of information related with task (time expectation) and behaviour (focus of attention in space and response times) were encoded in the FEF. To address the time expectation, we used the randomized time interval between the cue and the target onset (the cue-to-target onset asynchrony, CTOA) as a measure of target onset expectation. The distribution of the CTOA is shown in Figure 3, upper panels. We observed that the distribution of the CTOA is not unimodal (Kolmogorov-Smirnov test, p < 0.001). We measured the number of modes of distribution of the CTOA using smooth bootstrapping method (number of repetitions = 5000) described in (32), which consists in testing parsimoniously whether the distribution of CTOA shows an increasing number of modes until reaching significance. We found that the distribution of the CTOA showed five significant modes (p = 0.04) at CTOA = 1080 ms, 1400 ms, 2000 ms, 2600 ms and 3000 ms. Reaction times (RT) were calculated as the time passed between the target onset and the manual response onset. In order to get rid of early responses, we applied the linear approach to threshold with ergodic rate (LATER) model (33) and we eliminated those reaction times that were below the early response upper threshold. The distribution of the resultant RTs are shown in Figure 3 (intermediate panels, Median = 464 ms, IQ = 68). The focus of attention was calculated as the distance between the decoded position of the attentional spotlight to the real position of the target (see methods and (18,19,30,34,35)). Therefore, the focus of attention is defined as the Target-to-Attention distance (TA) measured shortly before the target onset. It has been previously described that this overt measure is linked with the probability to hit the target (18–21) and with the reaction time (19), accounting for how well subjects are orienting attention in space (19,21,34). The distribution of the TA is shown in Figure 3 (lower panels, Median = 11.9°, IQR = 11.02). 

We studied the firing rate modulation as a function of these three different parameters. For each recording session, we sorted ascendingly the CTOA, TA and RT respectively and we binned these vectors in ten different bins (Figure 3, coloured from lighter shades to darker shades, middle right column). We selected the trials based on each of these bins for each of these three parameters, focusing our analysis on hit trials. After equalizing the number of trials per each bin in each session, we obtained an average of 110 trials per bin (max = 149, min = 86).  We averaged the firing rate obtained from trials in each bin and parameter immediately prior the target onset (-200 to 0 ms) 

6 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

(Figure 3, right column). Figure 3 shows that firing rate was modulated as a function of time progression in the task and expectation of task events (CTOA; blue, upper panel), reaction time (RT; red, intermediate panel) and focus of attention (TA, yellow, lower panel). We found that FEF activity encoded these three different parameters (Friedman test, p< 0.0001 for all parameters). More specifically, we found that firing rate increases linearly as a function of the CTOA (activity sampled in the -200 to 0ms pre-target; Spearman correlation, rho = 0.95, p < 0.0001). Similarly, firing rate increased linearly as a function of the RT (Spearman correlation, rho = 0.92, p < 0.001). However, firing rates showed a quadratic relationship with the TA (quadratic fit, R[2] = 0.66, p = 0.02) but not linear (Linear fit, R^2 = 0.23, p = 0.15). The same results are reproduced for each monkey separately (Supplementary figure 2). 

**==> picture [427 x 218] intentionally omitted <==**

**Figure 3 MUA activity in the FEF encodes time progression in trial, reaction time and attentional focus.** Averaged MUA activity across all contacts (N = 848) grouped by time in trial (CTOA, blue), reaction time (RT, red) and attention focus (TA, yellow). CTOA reflect the time between the cue and the target, the reaction time reflect the time passed between target onset and manual response onset, and the TA is the distance between the decoded attentional spotlight and the target position 100 ms before the target onset. Histograms of these parameters across all trials are shown (middle left column). Tone colors represent the gradient of the parameter values (darker tones, higher values) for each of the parameters. The evolution of the time series MUA locked to the target onset for each parameter bin are shown (middle right column). Boxplots showing the median and the interquartile range of the MUA activity before the target onset (shaded rectangles in middle right column) is shown (right column, Friendman test, *** p<0.001). 

Thus, FEF shows mixed-selectivity for time-progression in trial, focus of attention and reaction time related information. Mixed selectivity in the prefrontal cortex allows encoding simultaneously multiple 

7 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

sources of information  (6,36,37). Accordingly, we investigated the characterization of mixed selectivity between these three parameters, their interplay and how mixed selectivity fluctuated in time. Figure 4A shows that the selectivity of the neural population for each parameter is dynamic. Overall, we found a higher proportion of position- selective cells (cells significantly tuned to the cued position) compared with the proportion of cells tuned to the rest of parameters. However, this proportion changes between before and after target presentation. Specifically, there is an increase of proportion of position-cells after the target onset (73% before the target onset vs 82% after the target onset), due to the fact that pre-target epoch identifies spatial attention information while post-target epoch identifies visual responses to the target. The same effect is observed for RT-cells (37% before the target onset vs. 65% after the target onset). In contrast, the proportion of time-estimation cells tends to decay during the post-target interval (45% pre-target vs. 32% post-target). The proportion of TA-cells remained constant irrespective of the target onset. We measured the percentage of neurons that showed random tuning. To do this, we randomly selected 10 subsets of trials, and we assigned them blindly to random CTOA, RT, position and TA conditions. We then measured the percentage of neurons that showed significant tuning (using non-parametric Friedman test). After repeating this process 1000 times, we selected the 95[th] percentile of the distribution of the percentages of tuned cells. Using this approach, only 6% of cells showed significant random tuning, indicating that the tuning of the neural population to all these parameters was significant. We also measured the proportion of cells that were tuned _only_ to one single parameter, just before the target onset (-100 ms to 0). We found that 27.2% of selective cells were tuned to only one parameter (17.7% to the cued position, 2.1% to the TA, 2.7% to the RT and a 4.5% to the CTOA). In the following we sought to investigate the proportion of cells that showed mixed selectivity in the pre-target interval that is during the period in which the attention information was held (Figure 4A, shaded area). Per each pair of parameters, we measured the proportion of recorded units that were tuned to each of the parameters (simple selectivity), to both parameters simultaneously (mixed selectivity) and to any of the two parameters (non-selective cells). The results are shown in figure 4B. We observed that per each pair of parameters we found a proportion of neurons that were tuned to both parameters simultaneously (minimum proportion, RT and TA, 6%; maximal proportion, Position and TA, 39%). We confirmed this rich and complex mixture of tuning selectivities by computing the proportion of cells that were tuned simultaneously to any 

8 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

combination of parameters (see Figure 4C). All in all, we found that the recorded neural population 

showed a complex pattern of mixed selectivities involving all these parameters simultaneously. 

**==> picture [427 x 116] intentionally omitted <==**

**Figure 4. Mixed selectivity in the FEF. (A).** Time series reflecting the selectivity of the cells (measured as the proportion of cells) for each parameter (CTOA in blue, RT in red, TA in yellow and Position in purple) locked to target onset. Dashed line represents the 95[th] C.I. of cells tuned to a random process. **(B)** Pie charts showing the proportion of cells showing no selectivity, single selectivity and mixed selectivity to each pair of parameters. **(C)** Venn diagram showing the proportion of selectivity for each combination of parameters. Percentages reflect the proportion of cells tuned to each of the intersections of tuning populations. 

Neural population holds a low-dimensional representation of time expectation, focus of attention and motor response in the FEF 

Previous literature has reported evidence that the activity in the prefrontal cortex is contained in a lowdimensional manifold that can be extracted projecting the firing rates from the high-dimensional recording space onto few latent variables that represent the majority of the variance in the recordings (7,13,38). In the previous section, we have demonstrated the ability of the PFC to encode simultaneously different sources of information. The question we address now is how the PFC organizes geometrically the representation of these different sources of information. To solve this issue, we have applied a demixed principal component analysis (dPCA) (14,39) which consist on a supervised dimensionality reduction method that decomposes (or demixes) the data in components by marginalizing it over different parameters. Differently to the principal components analysis where the variance is described in the direction of the eigenvectors of the covariance data matrix, with this model each component describe variance only in the direction of the eigenvectors of the covariance of each of marginalization. 

First, we sought to unmix each of the parameters from the rest of parameter independent activity. Supplementary figure 1B shows how the dPCA succeeds in extracting specific position-related variance (65% of the total variance). We projected the firing rates corresponding to trials categorized 

9 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

as a function of each cue position presentation (activity locked to the target onset) onto the first three components that accounted together for 79% of the total variance in the data. The second and third component were associated to position-related variance, whereas the first component showed the task-related variance independent on position. Therefore, this analysis shows that the recorded MUA activity in the FEF might be confined in a three-dimensional space containing position information (dimensions two and three) and task-related dynamics in different axis (dimension 1). 

In the following, we investigated whether we could reconstruct a low-dimensional representation of the recorded neural population, the axis (or neural mode) of which represents variance specific for each parameter of interest (time-expectation, focus of attention and motor response). Demixed PC analysis showed that 23% of the variance in data was explained by time progression (Figure 5A, top). Firing rates locked to the target onset (-400 ms to 400 ms) were projected onto the third and fourth demixed principal component (associated with CTOA). These two components showed a different pattern of dynamics as a function of the CTOA bin (Figure 5A, bottom). MUA activity projected onto the component 3 (8.2% of variance) showed that activity regime changed linearly (trial level projection, Linear Fit, R^2 = 0.98, p = 2e-14) as a function of the CTOA. Indeed, the higher the time between the cue and the target, the larger was the firing rate projected onto this component.  A different pattern was observed when MUA activity was projected onto the forth demixed component (2.2% of variance). Activity projected onto this component showed a quadratic relationship between the normalized firing rate and the CTOA (trial-level projection, quadratic fit, R^2 = 0.97, p = 3e-15). Specifically, activity was maximal at CTOA bin = 2000 ms. We used a stratified Monte Carlo leave-group-out cross-validation (100 iterations) to test whether these components decoded the CTOA bin. These results were fully reproducible per monkey (Supplementary figure 3). We found that the accuracy of decoding CTOA was significantly above chance level before target onset until 200 ms after the target onset (permutation test, 100 shuffles, p <0.05). These results showed that time expectation was contained within a two-dimensional space, components of which represent the time-expectation through two different functional mechanisms. 

10 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [427 x 206] intentionally omitted <==**

**Figure 5. dPC analysis of each parameter.** Demixed PC analysis reduces the dimensionality of the recordings and extracts variance specific of CTOA (A), RT (B) and TA (C). Pie chart represents the variance distributed between parameter-specific (black) and parameter-independent (gray). Bar plot shows the % variance (parameter specific, black; parameter independent, gray) attributed to the first 10 demixed components. Stars represent the parameter-specific components that decode the parameter at trial level above chance level. Only those are represented in time. Time series reflect the projection of the data onto the decoding parameter-specific components for each dPC analysis (CTOA, blue; RT, red: TA; yellow). Tone colors represent the gradient of the parameter values (darker tones, higher values) for each of the parameters. (*** p<0.001, regression model) 

Similarly, we conducted the same analysis for the focus of attention and reaction time. For RT, dPCA showed that the 59% of the variance was linked to the reaction time (Figure 5B, top). MUA activity projected onto the component 2 (9.8% of variance) showed that activity regime changed linearly (trial level projection, Linear Fit, R^2 = 0.81, p < 0.001) as a function of the RT, the projected firing rate onto this component decreasing as a function of the RT (Figure 5B, bottom). We found that this component significantly decoded RT between 200 ms before the target until 400 ms after the target (permutation test, 100 shuffles, p < 0.05). No other component showed decoding accuracy higher than the chance level. Therefore, dPCA extracted only one component containing the variance linked to the speed of response. Finally, dPCA showed that 19% of the variance was linked to the focus of attention (Figure 5C, top). MUA activity projected onto the component 3 (3.2% of the variance) showed that the projected firing rate increased as a function of the TA (Figure 5C, bottom, trial level projection, Linear Fit, R^2 = 0.75, p < 0.01). We found that this component significantly decoded TA bin during -400 ms to 400 ms with respect to the target onset (permutation test, 100 shuffles, p <0.05). No other 

11 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

component showed decoding accuracy higher than the chance level. Therefore, dPCA found one single component that contained the variance linked to the focus of attention. 

## CTOA, RT and TA interact both in the neural low-dimensional representation and in behaviour 

In the previous section, we described low-dimensional representations in the neural population associated to parameter specific variance in the data. The next question is to what extend these representations are independent one from each other or to what extend they overlap. If they overlap, the expectation is that the angle between the neural modes corresponding to each of these parameters are found to be non-orthogonality. In order to measure this angle, we conducted a dPC analysis with the aim to obtain simultaneously different neural modes associated to CTOA, TA, RT and task dynamics (independent from) the other three parameters. Demixed PCA succeeded in reconstructing a low-dimensional representation of the data. More specifically, the 70% of the total variance of data was represented in the first 10 demixed principal components (Figure 6).  Most of the variance was explained by trial-progression (46 %), followed by RT (22%), CTOA (17%) and TA (16%) (Figure 6B). Firing rates projected onto the first principal components of each parameter are clearly modulated by the task parameters, similar to what was described in the previous section (Figure 6A). Importantly, we found that these components were non-orthogonal, except for the RT and TA components (Figure 6C). 

12 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [345 x 209] intentionally omitted <==**

**Figure 6: Low-dimensional representation of MUA recordings in a parameter-based space. (A)** Time series corresponding to the projection of the MUA recording onto the condition-independent, reaction Time (RT), time in trial (CTOA) and attention focus (TA) specific components extracted simultaneously from a single dPCA. Red and green colors represent CTOA early and late (respectively), continuous and dashed lines represent fast and slow RT (respectively), and tones represent close (brighter), medium and long (darker) TA. Time series are locked to the target onset. **(B)** Cumulative signal variance explained by PCA (black) and dPCA (red) across the first 15 components. dPCA explains similar amount of variance than PCA. Pie chart shows how the total signal variance is split between CTOA, TA, RT and condition independent. **(C)** Representation of the angle between pairs of axes. Dark section reflects the angle values where angle values are considered statistically orthogonal. Red arrow indicates the actual angle between each pair of axes. Stars mark the pairs that are significantly and robustly nonorthogonal. 

Thus, the low dimensional representations associated with CTOA and RT and TA, respectively are not orthogonal. The next question we wanted to answer was whether there was a behavioral interaction between these three parameters. To this aim, per each session, we divided the trials into 10 different bins based on their CTOA, and we measured the median RT and TA within each bin. We found a clear linear relationship between the CTOA and the averaged RT (averaged value per all sessions, linear regression R^2 = 0.84, p < 0.001) (Figure 7A), whereas the relationship between the CTOA and TA was quadratic (Linear regression, R^2 = 0.07, p = 0.4; quadratic regression, R^2 = 0.59, p<0.05, Figure 7B). In addition, we found that CTOA and TA also affected the likelihood to respond to the target onset (Figure 7C and 7D, Linear regression between CTOA and hit rate, R^2 = 0.82, p < 0.01; Linear regression between TA and hit rate, R^2 = 0.82, p<0.01). Finally, we observed that both reaction time and TA over CTOA highly correlated with the level of activation of the first and second CTOA demixed principal components, respectively (Linear Regression between RT and dPC1, R^2 = 

13 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

0.79, p < 0.01; Linear Regression between TA and dPC2, R^2 = 0.49, p < 0.01). These results indicate that changes in the RT and TA across CTOA correspond to specific levels of activation of the neural population variability linked with the CTOA. 

**==> picture [169 x 266] intentionally omitted <==**

**Figure 7: Behavioral results** . **(A)** RT as a function of CTOA averaged across sessions. Each square represents, per each CTOA bin, the mean RT value. Bars represent the standard error of the RT measure across sessions. **(B)** TA as a function of CTOA averaged across sessions. Each square represents, per each CTOA bin, the mean TA value. Bars represent the standard error of the TA measure across sessions. **(C)** Hit rate as a function of CTOA averaged across sessions. Each square represents, per each CTOA bin, the mean hit rate value. Bars represent the standard error of the hit rate measure across sessions. **(D)** Hit rate as a function of TA averaged across sessions. Each square represents, per each TA bin, the mean hit rate value. Bars represent the standard error of the hit rate measure across sessions. (E) RT as a function of the activity projected onto the first dPC associated to CTOA across sessions. For each session, and each CTOA bin, the mean projected firing rate at the time interval -300 to 0 ms previous to the target onset as well as median RT for those trials. Average RT across sessions (square symbols) and s.e. were plotted against average firing rate. (F) Same as in (E) but for TA. (* p<0.05, **p<0.001 regression model). 

14 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## Discussion 

In the present work, we have shown the FEF ability to encode simultaneously multiple sources of information in latent non-orthogonal components, describing how such computational organization explains specific behavioral interactions between these parameters. More precisely, we have analyzed electrophysiological data recorded bilaterally from both FEF in two macaque monkeys performing a 100% validity cued attention task. In each trial, they were presented with a cue located in one of the four quadrants of the screen, and they were instructed to respond to a target stimulus located in the same quadrant after a randomized time interval (CTOA) while avoiding distractors. Using a linear regression algorithm (18,19,35,40), we have decoded the position of the attentional locus in the space and estimated the distance between this decoded position of attention to the real target position before target onset (Attentional focus, TA). We divided our trials based on four different parameters that accounted for the CTOA, TA, response time (RT) and the cued position. We found that the firing rate regime in the FEF, measured before the target onset, differed based on each of these parameters, indicating that the FEF encoded these four different sources of information. In addition, we classified the recorded cells based on their selectivity to these parameters. While we found cells showing a very high single specificity to one parameter, we found cells showing mixed selectivity to more than one of these parameters. Using demixed PCA (14), we found that the variance in our recordings could be split into different components, the variability of which was explained by these parameters. Critically, CTOA components showed non-orthogonality with the RT and TA components. Finally, behavioral analysis revealed that RT and TA changed as a function of the CTOA, and in correlation with the amount of neural activation associated with the CTOA. Overall, these results show the high coding capacity of the FEF that can be attributed to concurrent multiple neural processes encoded using nonorthogonal representations, which in turn account for overt behavioral interactions. 

At neuronal level, we have shown that the average firing rate of the recorded neural population increases as a function of the CTOA. This is in line with previous studies showing an increase of the firing rate as a consequence of a reward expectation (41–43), or the effect of an iteration of recurrent processes along the cue to target interval, which contains the representation of when (temporal expectation) and where (spatial attention) the target will appear (44). All in all, our results replicate 

15 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

previous findings suggesting an upper-modulation of the activity in the FEF during the cue to target interval.  We also found a clear modulation of the firing rate before target onset as a function of the reaction time, such that faster responses were preceded by a higher firing rate than slower responses. Previous literature has shown that reaction times were reliably associated with the amount of time required by FEF cells to reach a certain firing rate threshold in saccadic (31,45–47) and manual responses (48). Concretely, these studies show that FEF neurons must be depolarized more vigorously for initiating responses with stronger input in order to speed up response times. This indicates that reaction times are sensitive to the modulation of the activity in the FEF, in agreement with our observation. Finally, we found that FEF cells were tuned to the attentional focus, understood as the distance between the decoded position of the attentional spotlight to the target onset, measured before the target onset (19–22). This is in line with recently reported evidence showing that attention is dynamic and rhythmic in space (22,49), and that when pooling trials based on attention to target distance, the spiking rate of FEF cells increased as closer was the attentional spotlight to the expected position of the target (21,24). 

Importantly, we found that the majority of the recorded neurons on the FEF encoded these parameters through mixed selectivity cells. More specifically, the 72% of the recorded cells showed tuning to more than a single parameter.  These mixed selectivity cells have been reported in different brain areas (6,37,50,51), including the  FEF (21,36), and they represent a signature of the high-dimensional neural representation of relevant information and task-related parameters (7). Particularly, our results show that certain recorded cells are tuned simultaneously to more than two parameters, namely, spatial attention, the focus of attention, RTs, and CTOA. To our knowledge, only one study has reported evidence of such capacity of mixing information in a neural population. Ledergerber and colleagues show simultaneous tuning of position, head direction and speed in cells recorded in the CA1 and subiculum in rats (52). They convey that such rich mixing of features in a specific neural population might indicate a high capacity of information transmission towards downstream regions, integrating simultaneously different covariates and ensuring that such a wide number of covariates are accessible to distant projection areas. Similarly, the FEF has been considered in the literature a “ _hub_ ” region, containing visual, motor and visuo-motor cells, projecting towards dorsolateral prefrontal cortex, cingulate, parietal and posterior cortices (45,46,53). Such rich anatomical connectivity might explain 

16 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

this multiple variety of tuning capacities for different task-parameters and behavior-related parameters as reported here. 

We studied how much variance in our data was related to each of our parameters (CTOA, TA and RT) by using different dPCA specific to each of these parameters. For both RT and TA, we found that the dPCA successfully encoded each of the parameters in two components the activation of which showed a linear relationship with these parameters. For the CTOA, we found a more complex picture that deserve further discussion. Specifically, we found that the dPCA successfully encoded the time in trial in two different and orthogonal components, showing two different activation regimes. The projection of the activity associated with each CTOA bin onto the first demixed CTOA-component revealed a linear increase of the activity state, being low in the early stages of the trial and linearly increasing for longer CTOAs. We found that these states of activation nicely correlated with the reaction time measured in these CTOA-based selected trials, suggesting a functional link between this CTOA-related component and reaction time variability. This result accounts for the observed correlation between CTOA and RT, whereby responses performed in early stages in the trial were slower than those responses performed in the late stages of the trial. In contrast, projected firing rates onto the second demixed CTOA-component showed an inverted U-shape, in which lower activity state corresponded in early and late trials, while intermediate CTOA trials showed the maximal activation. When the activation of this component was the lowest (coinciding with trials selected at early and late stages of the trial), the encoded position of the attentional spotlight was more distant to the expected position of the target, while this distance was shorter when the activation of this component was the highest. This finding suggest a functional link between the CTOA-related variability explained by this component and the attentional focus. Prior studies have addressed the functional relevance of highorder, non-linear components, as the one observed by this CTOA-component. Recently, Okazawa and colleagues (54) suggested that these curved components might arise automatically due to fundamental constraints on neural computations that limit the dynamics of the firing rates, including the fact that expected values of the firing rate are non-negative, that they are bounded by metabolic constraints (55) (Lennie 2003), and that there is a strong evolutionary pressure to precisely encode information (56). Following the arguments of Okazawa et al. (54), we speculate that these CTOArelated components might define a sub-region in the state space where sensory information is 

17 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

encoded, defining a curved manifold subserving efficient readout from other brain regions (here, readout corresponding to efficient attentional orientation). This needs to be tested experimentally. 

Finally, we applied a dPCA to simultaneously decompose our variance dataset in components associated to the CTOA, RT and TA. As reported in Kobak et al. (14), this dimensionality reduction method does not assume the orthogonality of the components when efficiently linking specific sources of variance to each of the principal components. We studied the geometrical properties of the lowdimensional manifold containing the first principal components associated to each parameter in terms of the orthogonality between these components. We found that the CTOA component was significantly non-orthogonal to both the TA- and RT-related components. This result indicates that the FEF encodes these sources of information through non-orthogonal, partially overlapping codes. Previous literature has reported that encoding multiple sources of information in orthogonal codes through mixed-selectivity cells might ease the accessibility of the information to the downstream neurons (7,57). However, the low-dimensional manifold in which the recorded data is embedded limits the number of different encoding information that may be implemented in the system. It has indeed been reported that primate prefrontal neuronal populations have an informational capacity often limited to 3 sources of information (58). We argue that the FEF might therefore code multiple sources of information in non-orthogonal components as a strategy to maximize its encoding capacities. However, this strategy of encoding might come with a cost. We observe in our data a clear interaction between the CTOA and RT (responses get faster as CTOA advances) and CTOA and TA (attention is closer to the target in middle stages of the trial). Therefore, these results suggest that encoding through non-orthogonal components might drive the way the monkey uses attention and responsiveness as a dynamic cognitive resource to accurately perform the task. In support of this, we have recently reported evidence that the degree of non-orthogonality between the attentional component and a component which variance is associated with the reported behavior of the monkey, accounts for the degree to which the monkeys can use attentional information to guide behavior (21). In conclusion, we report converging evidence showing that different sources of information are implemented simultaneously in the FEF in a very precise geometrical configuration that leverages nonorthogonal components. This configuration is proposed to allow for high capacity of information coding, at the cost of modulating both the capacity of the monkey to use attention information and its responsiveness toward the stimulus. This finding sheds light onto the dynamic changes of the 

18 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

computational mechanisms of the attentional system during task performance, and it is expected to have profound implications in the development of efficient decoding algorithms aimed to extract 

specific cognitive information from electrophysiological recordings. 

19 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## Material and Methods 

## Endogenous cued detection task and Experimental setup 

The task is a 100% validity endogenous cued luminance change detection task (Figure 1A). The animals were placed in front of a PC monitor (1920×1200 pixels, refresh rate of 60Hz) with their heads fixed. Stimulus presentation and behavioral responses were controlled using Presentation® (Neurobehavioral Systems, Inc.). To start a trial, the monkeys had to hold a bar placed in front of their chair, thus interrupting an infrared beam. The appearance of a central fixation cross (size 0.7°×0.7°) at the center of the screen, instructed the monkeys to maintain their eye position (Eye tracker - ISCAN, Inc.) inside a 2°×2° window, throughout the duration of the trial, so as to avoid aborts. Four gray landmarks (LMs size 0.5°×0.5°) were displayed, simultaneously with the fixation cross, at the four corners of a hypothetical square having a diagonal length of ~28° and a center coinciding with the fixation cross. The four LMs (up-right, up-left, down-left, down-right) were thus placed at the same distance from the center of the screen having an eccentricity of ~14°. After a variable delay from fixation onset, ranging between 700 to 1200 ms, a 350 ms spatial cue (small green square - size 0.2°×0.2°) was presented next to the fixation cross (at 0.3°), indicating the LM in which the rewarding target change in luminosity would take place. Thus, the cue presentation instructed the monkeys to orient their attention towards the target in order to monitor it for a change in luminosity. The change in target luminosity occurred unpredictably between 750 to 3300 ms from cue onset. In order to receive their reward (a drop of juice), the monkeys were required to release the bar between 150 and 750 ms after target onset (hit). To test the monkeys’ ability at distractor filtering, on half of the trials, one of the two distractor typologies was randomly presented during the cue-to-target delay. In ~17% of the trials (D trials), a change in luminosity, identical to the awaited target luminosity change, took place at one of the three uncued LMs. In these trials, the distractor D was thus identical in all respects to the expected target, except for being displayed in an uncued position. In ~33% trials (d trials), a local change in luminosity (square) was displayed at a random position in the workspace. The size of the local change in luminosity was adjusted so as to account for the cortical magnification factor, growing from the center to the periphery (Schwartz 1994). In other words, d distractors had the same size as D distractors when presented at the same eccentricity as D. The absolute luminosity change with respect 

20 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

to the background was the same for both d and D. The monkeys had to ignore both distractor typologies (correct rejections – RJ). Responding to such distractors within 150 to 750ms (false alarm - FA) or at any other irrelevant time in the task interrupted the trial. Failing to respond to the target (miss) similarly aborted the ongoing trial. 

## Electrophysiological recordings and spike detection 

Bilateral simultaneous recordings in the FEF in both hemispheres were carried out using two 24contact Plexon U-probes (Figure 1B). The contacts had an interspacing distance of 250 μm. Neural data was acquired using a Plexon Omniplex® neuronal data acquisition system. The data was amplified 500 times and digitized at 40,000Hz. Neuronal activity was high-pass filtered at 300Hz and a threshold defining the multiunit activity (MUA) was applied independently for each recording contact and before the actual task-related recordings started. 

## Decoding procedure & attentional focus (TA) estimation 

**Training procedure.** In prior studies, we showed that the endogenous orienting of attention (Figure 1C) can be reliably decoded from the FEFs activity using a regularized optimal linear estimator (RegOLE) with the same accuracy as exogenous visual information(18,21,22,35 for review,40,59). Here, we used the same approach to train a RegOLE to associate the neural responses prior to target onset ([-220 + 30] from target onset), based on a leave-one-out training/testing procedure, with the attended location, i.e., with the expected target presentation LM, based on cue information. Neural responses consisted in a vector containing the MUA signals collected at each of the 48 recording contacts during this pre-defined pre-target onset epoch. Our general objective here was to have as precise as possible an estimate of the attention position before a specific visual event, averaging activities over large enough windows to have a reliable single-trial estimate of the neuronal response on this window, while at the same time a not-too-large time window to have a reliable estimate of where attention was placed by the subject at a specific time in the task(20–22,60,61). 

The RegOLE defines the weight matrix W that minimizes the mean squared error of ���������, where **C** is the class (here, four possible spatial locations), **b** is the bias and **R** is the neural response. To avoid over-fitting, we used a Tikhonov regularization(40) which gives us the following minimization equation�����������[�] � λ*���[�] . 

The scaling factor λ was chosen to allow for a good compromise between learning and generalization. Specifically, the decoder was constructed using two independent regularized linear regressions, one 

21 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

classifying the _x_ -axis (two possible classes: -1 or 1) and one classifying the _y_ -axis (two possible classes: -1 or 1). 

**Testing procedure.** In order to identify the locus of attention at the moment of target or distractor presentation in the 20 next new trials following the initial training set, the weight matrix defined during training was applied to the average neuronal activity recorded in the 150 ms prior to target. The described training (over 200 previous trials) / testing (over 20 novel trials) procedure was repeated after every 20 correct responses, by re-training the decoder with the new database composed by the last 200 correct trials. This continuous updating of the weight matrix W is implemented in order to minimize the impact of possible uncontrolled for changes in the recorded signal during a given recording session onto the decoding procedure. 

## Estimating the (x,y) spatial locus of the attentional spotlight (AS) 

The readout of the RegOLE was not assigned to one of the four possible quadrants by applying a hardlim rule, as usually done for classification purposes. Rather, it was taken as reflecting the error of the decoder estimate to the target location, i.e., in behavioral terms, as the actual ( _x,y_ ) spatial estimate of the locus of the attentional focus to the expected target location(18). We show here and elsewhere(18,21,22) that this ( _x,y_ ) estimate of the attentional spotlight (AS) accounts for variations in behavioral responses. In order to analyze how the distance of the decoded attentional spotlight to the target affected both behavior and neuronal MUA responses, we computed, for each target presentation, the distance between the decoded AS and the target (TA) as follows: � _TA_ = ���� ����[�] � ���� ����[�] where ��� and ��� correspond to the Cartesian coordinates of the � attentional spotlight ( _AS_ ), and �� and �� correspond to the Cartesian coordinates of the target position ( _T_ ). 

## Partitioning of the neural data 

Similarly to the decoding procedure, only neuronal data from correct trials were analysed. Neural data was partitioned based on four different parameters: 1) CTOA, i.e. time from cue onset and target onset; 2) RT, response reaction time, considered as the time between target onset and manual response and 3) TA or focus of attention, i.e., the distance between the decoded attention spotlight position and the cued LM position. For each of these three, we pooled trials in 10 different bins based 

22 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

on the deciles distribution of each parameter (Mean number of trials per class, 101 ±8). Trials in which the TA was longer than 18° were discarded. 

## Behavioral Performance 

Main task performance was measured through four different parameters: Hit rate (number of hits divided by the number of hits and misses), False alarm rate (Number of false alarms divided by the number of distractors), and the reaction time for hits and false alarms. Hit rate and reaction time to target responses were also calculated in each CTOA and TA bins. 

We use a linear approach to threshold with ergodic rate (LATER) model to estimate the reciprobit distribution of latencies from responses to hits in the main task performance(33). This method was used to identify express responses from the distribution of responses in each session, and discard them for RT analysis. 

## Characterizing MUA selectivity 

In order to quantify the magnitude of the modulation of FEF individual to the orientation of the cue location, we pooled trials based on whether the cue oriented attention in the preferred spatial location within the neuron’s receptive field (RF), or non-preferred spatial location outside the RF, considering only correct trials. We defined a modulation index as: 

��� ������������������������� ��� ���������������������������������� where ����������� and ����������������� correspond to the median 

firing rate when the preferred and the least-preferred cue are presented. Firing rates were computed on the -300 to -50 ms pre target epoch, z-scored with respect to a [-300 to -0 ] ms pre-cue epoch. The statistical significance of the MI was performed with a non-parametric Wilcoxon rank test (p < 0.05). We measured the selectivity of each neuron for each of the parameters (CTOA, RT, TA and position) across the time interval -400 to 400 ms locked to the target onset. To this end, we calculated the main parameter effect across the interval (sliding window of 50 ms, step of 25 ms) by using a nonparametric Friedman test. With this method, we obtained per each time-subinterval the proportion of cells that were significantly tuned to each parameter. For each time point, we additionally measured the proportion of cells that showed tuning when trials were selected randomly. We repeated this process 1000 times obtaining a distribution of values corresponding to the proportion of cells that were tuned to random variability pear each randomization. For each time point, we selected the 95[th] value of this distribution as threshold for random tuning. 

23 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

Per each pair of parameters (CTOA-TA, CTOA-RT, CTOA-Position, TA-RT, TA-Position and RTPosition) we measured the selectivity of each cell for each of the two parameters (single selectivity) and for both parameters simultaneously (mixed-selectivity). To do this, we averaged the firing rate in the interval -300 ms to 0 ms before the target onset, and we used a non-parametric test Friedman test to measure the tuning for each parameter (p <0.05). A cell was considered to present single selectivity for a given parameter if its activity was tuned to this parameter and not tuned to the other parameter of the pair. A cell was considered to present mixed selectivity if it was significantly tuned to both parameters simultaneously. Cells without significant tuning to any of the two parameters of the pair were considered as non-selective. 

## Demixed PCA 

Recent research points that neural function is built on population activity patterns rather than on independent modulation of individual neurons (62). These patterns reflect the coordination of responses across neurons that corresponds to a specific neural mechanism underlying a specific behaviour (13). The population activity structure can be estimated by applying a dimensionality reduction technique to the recorded activity such as Principal Component analysis (PCA). Using this method, we can extract a number of latent variables (principal components) that capture independent sources of data variance providing a description of the statistical features of interest (13). However, this method does not take task- or behaviour-related parameters into account, mixing these sources of information within each of the extracted latent variables(14). With the aim of describing how much variance in the neural population can be explained by each parameter (CTOA, RT and TA), we performed a demixed principal component analysis (dPCA (14)), which captures the maximum amount of variance specifically explained by each of the above-defined parameters in each extracted latent variable and reconstructs the time course of the parameter-specific response modulation. 

First, we described the amount of variance explained specifically for each parameter.  To do so, we applied an independent dPCA analysis for each parameter, selecting trials based on the deciles of the distribution of the values in the parameter. In each of these analyses, the aim was to decompose the data into latent variables that estimate over time both the variance attributed to a parameter of interest and the variance independent to the parameter. Second, we aimed to describe how the different subpopulations associated to each parameter overlapped. To this end, we applied a single dPCA with the aim to decompose the variance attributed in CTOA-related, TA-related and RT-related 

24 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

components from the original dataset. In this case, trials were classified based on its CTOA (below the 40[th] percentile or above the 60[th] percentile of the CTOA distribution), its RT (below the 40[th] percentile or above the 60[th] of the RT distribution) and its TA (TA close (0°<TA≤6°), TA medium (6°<TA≤12°) and TA far (12°<TA<18°)), giving rise to 2x2x3 = 12 different potential classes where a trial can belong to. Procedures to perform the dPCA analysis were performed using the MATLAB © (The Mathworkds Inc., Natick, Massachussetts) written scripts available from (14). Averaged MUA firing rate for each channel in each condition and each session were concatenated in a single dataset representing the entire recorded neural population, in the interval between -400 to 400 ms locked to the target onset. In each analysis, we used the decoding axis of each dPC assigned to each parameter as a linear classifier to decode trials belonging to the different categories (specific class for each parameter). To extract the statistical significance of this accuracy, we shuffled 100 times all available trials between classes and we thereby computed the distribution of classification accuracies expected by chance. Since the coordinates of the components reflect the level of contribution to the activity of each neuron, the size of the dot product values between two components indicate that neurons that contribute to one component tend also to contribute to the other component. Therefore, the angle between two components can be interpreted as a marker of the functional overlapping between these components. When we applied the single dPCA analysis aimed to decompose the entire recorded population in latent variables associated to each parameter, we used the dot product between the first demixed principal components associated to each parameter to estimate the angle between these two components. For each pair of parameters, we measure the dot product between the subspaces obtained from first demixed principal component that maximally explained each parameter. Nonorthogonality is considered if the dot product between these two subspaces is greater than 3.3/N[1/2] , N being the number of total components considered in the decomposition (see (14) for details). 

## Conflicts of interest 

The authors declare no competing financial interests. 

25 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## Authors contributions 

Conceptualization, J.A. and S.B.H.; Data Acquisition, F.D.B. and S.B.H.H.; Methodology, J.A. and S.B.H.; Investigation, J.A., S.B.H.; Writing – Original Draft, J.A.; Writing – Review and Editing, J.A. and S.B.H 

## Acknowledgments 

J.A., F.D.B., S.B.H.H, and S.B.H. were supported by ERC BRAIN3.0 # 681978 and ANR-11-BSV40011 & ANR-14-ASTR-0011-01, LABEX CORTEX funding (ANR-11-LABX-0042) from the Université de Lyon, within the program Investissements d’Avenir (ANR-11-IDEX-0007) operated by the French National Research Agency (ANR) to S.B.H. We acknowledge Inovarion for their fruitful scientific discussions. We also extend our thanks to Serge Pinède for hardware and software assistance and Jean-Luc Charieau and Fidji Francioly for animal care. F.B.is now affiliated to _Department of Physiology and Pharmacology, Sapienza University of Rome, 0018, Rome, Italy;_ S.B.H.H. is now affiliated to _Laboratory in Sensory Physiology, Otto Von Guericke University, 39120, Magdeburg, Germany;_ E.A. is now affiliated to _Laboratory in Sensory Physiology, Otto Von Guericke University, 39120, Magdeburg, Germany;_ E.A. is now affiliated to _School of Innovation, Design, and Engineering, Mälardalen University, IDT, 721 23 Västerås, Sweden._ 

## Data availability 

The datasets supporting the current study have not been deposited in a public repository and are still under investigation. They are available from the corresponding author upon reasonable request. 

## Code availability 

Analysis were performed on Matlab, with custom codes, deposited onto a private github. They are available from the corresponding author upon reasonable request. 

26 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## References 

1. Goldman-Rakic PS. Cellular basis of working memory. Neuron. 1995 Mar;14(3):477–85. 

2. Fuster JM. Unit activity in prefrontal cortex during delayed-response performance: neuronal correlates of transient memory. Journal of Neurophysiology. 1973 Jan;36(1):61–78. 

3. Petrides M. The role of the mid-dorsolateral prefrontal cortex in working memory. Exp Brain Res. 2000 Jul;133(1):44–54. 

4. Badre D, Nee DE. Frontal Cortex and the Hierarchical Control of Behavior. Trends in Cognitive Sciences. 2018 Feb;22(2):170–88. 

5. Astrand E, Wardak C, Ben Hamed S. Selective visual attention to drive cognitive brain-machine interfaces: from concepts to neurofeedback and rehabilitation applications. Front Syst Neurosci. 2014;8:144. 

6. Rigotti M, Barak O, Warden MR, Wang XJ, Daw ND, Miller EK, et al. The importance of mixed selectivity in complex cognitive tasks. Nature. 2013 May;497(7451):585–90. 

7. Fusi S, Miller EK, Rigotti M. Why neurons mix: high dimensionality for higher cognition. Current Opinion in Neurobiology. 2016 Apr;37:66–74. 

8. Mendoza-Halliday D, Martinez-Trujillo JC. Neuronal population coding of perceived and memorized visual features in the lateral prefrontal cortex. Nat Commun. 2017 Aug;8(1):15471. 

9. Asaad WF, Rainer G, Miller EK. Neural Activity in the Primate Prefrontal Cortex during Associative Learning. Neuron. 1998 Dec;21(6):1399–407. 

10. Gallego JA, Perich MG, Miller LE, Solla SA. Neural Manifolds for the Control of Movement. Neuron. 2017 Jun;94(5):978–84. 

11. Raposo D, Kaufman MT, Churchland AK. A category-free neural population supports evolving demands during decision-making. Nat Neurosci. 2014 Dec;17(12):1784–92. 

12. Okun M, Steinmetz NA, Cossell L, Iacaruso MF, Ko H, Barthó P, et al. Diverse coupling of neurons to populations in sensory cortex. Nature. 2015 May 28;521(7553):511–5. 

13. Cunningham JP, Yu BM. Dimensionality reduction for large-scale neural recordings. Nat Neurosci. 2014 Nov;17(11):1500–9. 

14. Kobak D, Brendel W, Constantinidis C, Feierstein CE, Kepecs A, Mainen ZF, et al. Demixed principal component analysis of neural population data. eLife [Internet]. 2016 Apr 12 [cited 2019 Dec 3];5. Available from: https://elifesciences.org/articles/10989 

15. Rishel CA, Huang G, Freedman DJ. Independent Category and Spatial Encoding in Parietal Cortex. Neuron. 2013 Mar;77(5):969–79. 

16. Armstrong KM, Chang MH, Moore T. Selection and Maintenance of Spatial Information by Frontal Eye Field Neurons. Journal of Neuroscience. 2009 Dec 16;29(50):15621–9. 

17. Gregoriou GG, Gotts SJ, Zhou H, Desimone R. High-frequency, long-range coupling between prefrontal and visual cortex during attention. Science. 2009 May 29;324(5931):1207–10. 

18. Astrand E, Wardak C, Baraduc P, Ben Hamed S. Direct Two-Dimensional Access to the Spatial Location of Covert Attention in Macaque Prefrontal Cortex. Curr Biol. 2016 11;26(13):1699–704. 

27 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

19. Astrand E, Wardak C, Ben Hamed S. Neuronal population correlates of target selection and distractor filtering. Neuroimage. 2020 01;209:116517. 

20. Di Bello F, Ben Hadj Hassen S, Astrand E, Ben Hamed S. Prefrontal Control of Proactive and Reactive Mechanisms of Visual Suppression. Cerebral Cortex. 2022 Jun 16;32(13):2745–61. 

21. Amengual JL, Di Bello F, Ben Hadj Hassen S, Ben Hamed S. Distractibility and impulsivity neural states are distinct from selective attention and modulate the implementation of spatial attention. Nat Commun. 2022 Aug 15;13(1):4796. 

22. Gaillard C, Ben Hadj Hassen S, Di Bello F, Bihan-Poudec Y, VanRullen R, Ben Hamed S. Prefrontal attentional saccades explore space rhythmically. Nat Commun. 2020 Dec;11(1):925. 

23. Posner MI. Orienting of Attention. Quarterly Journal of Experimental Psychology. 1980 Feb;32(1):3–25. 

24. Ibos G, Duhamel JR, Ben Hamed S. A Functional Hierarchy within the Parietofrontal Network in Stimulus Selection and Attention Control. Journal of Neuroscience. 2013 May 8;33(19):8359–69. 

25. Bashinski HS, Bacharach VR. Enhancement of perceptual sensitivity as the result of selectively attending to spatial locations. Perception & Psychophysics. 1980 May 1;28(3):241–8. 

26. Pestilli F, Carrasco M. Attention enhances contrast sensitivity at cued and impairs it at uncued locations. Vision Research. 2005 Jun;45(14):1867–75. 

27. Cohen MR, Maunsell JHR. A neuronal population measure of attention predicts behavioral performance on individual trials. J Neurosci. 2010 Nov 10;30(45):15241–53. 

28. Moore T, Armstrong KM. Selective gating of visual signals by microstimulation of frontal cortex. Nature. 2003 Jan;421(6921):370–3. 

29. Corbetta M, Akbudak E, Conturo TE, Snyder AZ, Ollinger JM, Drury HA, et al. A Common Network of Functional Areas for Attention and Eye Movements. Neuron. 1998 Oct;21(4):761–73. 

30. Di Bello F, Ben Hadj Hassen S, Astrand E, Ben Hamed S. Selection and suppression of visual information in the macaque prefrontal cortex [Internet]. Neuroscience; 2020 Mar [cited 2021 Mar 1]. Available from: http://biorxiv.org/lookup/doi/10.1101/2020.03.25.007922 

31. Schall JD. On the role of frontal eye field in guiding attention and saccades. Vision Research. 2004 Jun;44(12):1453–67. 

32. Efron B, Tibshirani R. An introduction to the bootstrap. New York: Chapman & Hall; 1993. 436 p. (Monographs on statistics and applied probability). 

33. Noorani I, Carpenter RHS. The LATER model of reaction time and decision. Neuroscience & Biobehavioral Reviews. 2016 May;64:229–51. 

34. Amengual JL, Di Bello, F, Gaillard C, Ben Hamed S. Spatial attention and cognitive control interplay in goal-directed behaviors: evidences from prefrontal cortex. Bioarxiv. 2021; 

35. Amengual JL, Ben Hamed S. Revisiting Persistent Neuronal Activity During Covert Spatial Attention. Front Neural Circuits. 2021 Jun 30;15:679796. 

36. Parthasarathy A, Herikstad R, Bong JH, Medina FS, Libedinsky C, Yen SC. Mixed selectivity morphs population codes in prefrontal cortex. Nature Neuroscience. 2017 Dec 1;20(12):1770–9. 

37. Kondo S, Yoshida T, Ohki K. Mixed functional microarchitectures for orientation selectivity in the mouse primary visual cortex. Nat Commun. 2016 Dec;7(1):13210. 

28 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

38. Churchland AnneK, Kiani R, Chaudhuri R, Wang XJ, Pouget A, Shadlen MN. Variance as a Signature of Neural Computations during Decision Making. Neuron. 2011 Feb;69(4):818–31. 

39. Machens CK. Demixing Population Activity in Higher Cortical Areas. Front Comput Neurosci [Internet]. 2010 [cited 2021 Mar 2];4. Available from: http://journal.frontiersin.org/article/10.3389/fncom.2010.00126/abstract 

40. Astrand E, Enel P, Ibos G, Dominey PF, Baraduc P, Ben Hamed S. Comparison of Classifiers for Decoding Sensory and Cognitive Information from Prefrontal Neuronal Populations. Boraud T, editor. PLoS ONE. 2014 Jan 23;9(1):e86314. 

41. Glaser JI, Wood DK, Lawlor PN, Ramkumar P, Kording KP, Segraves MA. Role of expected reward in frontal eye field during natural scene search. Journal of Neurophysiology. 2016 Aug 1;116(2):645–57. 

42. Bendiksby MS, Platt ML. Neural correlates of reward and attention in macaque area LIP. Neuropsychologia. 2006 Jan;44(12):2411–20. 

43. Roesch MR, Olson CR. Neuronal Activity Related to Reward Value and Motivation in Primate Frontal Cortex. Science. 2004 Apr 9;304(5668):307–10. 

44. Crapse TB, Sommer MA. The frontal eye field as a prediction map. In: Progress in Brain Research [Internet]. Elsevier; 2008 [cited 2022 Dec 5]. p. 383–90. Available from: https://linkinghub.elsevier.com/retrieve/pii/S0079612308006560 

45. Bruce CJ, Goldberg ME. Primate frontal eye fields. I. Single neurons discharging before saccades. J Neurophysiol. 1985 Mar;53(3):603–35. 

46. Bruce CJ, Goldberg ME, Bushnell MC, Stanton GB. Primate frontal eye fields. II. Physiological and anatomical correlates of electrically evoked eye movements. J Neurophysiol. 1985 Sep;54(3):714–34. 

47. Funahashi S, Chafee MV, Goldman-Rakic PS. Prefrontal neuronal activity in rhesus monkeys performing a delayed anti-saccade task. Nature. 1993 Oct;365(6448):753–6. 

48. Wardak C, Vanduffel W, Orban GA. Searching for a Salient Target Involves Frontal Regions. Cerebral Cortex. 2010 Oct;20(10):2464–77. 

49. Busch NA, VanRullen R. Spontaneous EEG oscillations reveal periodic sampling of visual attention. PNAS. 2010 Sep 14;107(37):16048–53. 

50. Mante V, Sussillo D, Shenoy KV, Newsome WT. Context-dependent computation by recurrent dynamics in prefrontal cortex. Nature. 2013 Nov;503(7474):78–84. 

51. Diomedi S, Vaccari FE, Filippini M, Fattori P, Galletti C. Mixed Selectivity in Macaque Medial Parietal Cortex during Eye-Hand Reaching. iScience. 2020 Oct;23(10):101616. 

52. Ledergerber D, Battistin C, Blackstad JS, Gardner RJ, Witter MP, Moser MB, et al. Taskdependent mixed selectivity in the subiculum. Cell Reports. 2021 May;35(8):109175. 

53. Vernet M, Quentin R, Chanes L, Mitsumasu A, Valero-CabrÃ© A. Frontal eye field, where art thou? Anatomy, function, and non-invasive manipulation of frontal regions involved in eye movements and associated cognitive operations. Front Integr Neurosci [Internet]. 2014 Aug 22 [cited 2022 Nov 30];8. Available from: http://journal.frontiersin.org/article/10.3389/fnint.2014.00066/abstract 

54. Okazawa G, Hatch CE, Mancoo A, Machens CK, Kiani R. Representational geometry of perceptual decisions in the monkey parietal cortex. Cell. 2021 Jul;184(14):3748-3761.e18. 

55. Lennie P. The Cost of Cortical Computation. Current Biology. 2003 Mar;13(6):493–7. 

29 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

56. Smaers JB, Gómez-Robles A, Parks AN, Sherwood CC. Exceptional Evolutionary Expansion of Prefrontal Cortex in Great Apes and Humans. Current Biology. 2017 Mar;27(5):714–20. 

57. DiCarlo JJ, Zoccolan D, Rust NC. How Does the Brain Solve Visual Object Recognition? Neuron. 2012 Feb;73(3):415–34. 

58. Gao P, Trautmann E, Yu B, Santhanam G, Ryu S, Shenoy K, et al. A theory of multineuronal dimensionality, dynamics and measurement [Internet]. Neuroscience; 2017 Nov [cited 2022 Dec 13]. Available from: http://biorxiv.org/lookup/doi/10.1101/214262 

59. Astrand E, Ibos G, Duhamel JR, Ben Hamed S. Differential dynamics of spatial attention, position, and color coding within the parietofrontal network. J Neurosci. 2015 Feb 18;35(7):3174–89. 

60. De Sousa C, Gaillard C, Di Bello C, Ben Hadj Hassen F, Ben Hamed S. Behavioral validation of novel high resolution attention decoding method from multi-units & local field potentials. NeuroImage. 2021 May;231:117853. 

61. Farbod Kia S, Åstrand E, Ibos G, Ben Hamed S. Readout of the intrinsic and extrinsic properties of a stimulus from un-experienced neuronal activities: towards cognitive neuroprostheses. J Physiol Paris. 2011 Jun;105(1–3):115–22. 

62. Shenoy KV, Sahani M, Churchland MM. Cortical Control of Arm Movements: A Dynamical Systems Perspective. Annu Rev Neurosci. 2013 Jul 8;36(1):337–59. 

30 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

## Supplementary material 

**==> picture [427 x 119] intentionally omitted <==**

**==> picture [427 x 120] intentionally omitted <==**

**Supplementary Figure 1. Spatial selectivity in the FEF.** (A) Mean MUA activity across all contacts (N = 848 electrodes) divided as a function of cued position (Continuous Blue: Right U; Dashed Blue: Right Down; Continuous Red: Left Up; Dashed Red: Right Down) locked to the target onset (-400 ms to 400 ms). Pie chart shows the proportion of position-cells (black, selective attention, 75%) in the recorded population. (B) Pie chart showing the proportion of variance explained by position (black, 68%) and position-independent (gray, 32%) in the recorded population. Projection of the firing rates averaged per each position onto the first three demixed principal components. 

**==> picture [427 x 132] intentionally omitted <==**

**Supplementary figure 2.** Time series for the MUA activity locked to the target onset for each monkey (M1, N = 480 contact; M2, N = 384 contacts). Tone colors represent the gradient of the parameter values (darker tones, higher values) for each of the parameters: CTOA (blue), RT (red) and TA (yellow). Boxplots showing the median and the interquartile range of the MUA activity before the target onset (-200 ms to 0) are also represented (Friendman test, *** p<0.001). 

31 

bioRxiv preprint doi: https://doi.org/10.1101/2022.12.28.522139; this version posted December 29, 2022. The copyright holder for this preprint (which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made available under aCC-BY-NC-ND 4.0 International license. 

**==> picture [427 x 202] intentionally omitted <==**

**==> picture [427 x 202] intentionally omitted <==**

**Supplementary figure 3.** All as in figure 5. 

32 

