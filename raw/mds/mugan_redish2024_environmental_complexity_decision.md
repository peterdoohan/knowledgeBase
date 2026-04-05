Article 

# Environmental complexity modulates information processing and the balance between decisionmaking systems 

## Highlights 

- d HC theta sequences elongated under uncertainty and more so in complex environments 

## Authors 

Ugurcan Mugan, Samantha L. Hoffman, A. David Redish 

- d DLS task bracketing arose as behaviors automated, but only in simple environments 

- d HC planning and DLS task bracketing correlated inversely across all environments 

- d Dorsal mPFC mediated the inverse relationship between planning and automation 

## Correspondence 

redish@umn.edu 

## In brief 

Mugan et al. compare neural representations in the hippocampus, dorsolateral striatum, and medial prefrontal cortex as rats made decisions in environments of varying complexity. They find that the dynamic interplay of information processing underlying the balance between decision-making systems changed with that environmental complexity. 

**==> picture [17 x 17] intentionally omitted <==**

Mugan et al., 2024, Neuron 112, 4096–4114 December 18, 2024 ª 2024 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies. https://doi.org/10.1016/j.neuron.2024.10.004 

**ll** 

**ll** 

## Article 

# Environmental complexity modulates information processing and the balance between decision-making systems 

Ugurcan Mugan,[1] Samantha L. Hoffman,[2] and A. David Redish[1][,][3][,] * 

1Department of Neuroscience, University of Minnesota, Minneapolis, MN, USA 

2University of Wisconsin School of Medicine and Public Health, Madison, WI, USA 3Lead contact 

*Correspondence: redish@umn.edu https://doi.org/10.1016/j.neuron.2024.10.004 

## SUMMARY 

Behavior in naturalistic scenarios occurs in diverse environments. Adaptive strategies rely on multiple neural circuits and competing decision systems. However, past studies of rodent decision making have largely measured behavior in simple environments. To fill this gap, we recorded neural ensembles from hippocampus (HC), dorsolateral striatum (DLS), and dorsomedial prefrontal cortex (dmPFC) while rats foraged for food under changing rules in environments with varying topological complexity. Environmental complexity increased behavioral variability, lengthened HC nonlocal sequences, and modulated action caching. We found contrasting representations between DLS and HC, supporting a competition between decision systems. dmPFC activity was indicative of setting this balance, in particular predicting the extent of HC non-local coding. Inactivating mPFC impaired short-term behavioral adaptation and produced long-term deficits in balancing decision systems. Our findings reveal the dynamic nature of decision-making systems and how environmental complexity modulates their engagement with implications for behavior in naturalistic environments. 

## INTRODUCTION 

Naturalistic behaviors often occur in complex and uncertain environments, and animals adapt their behaviors to that environmental complexity. For example, a busy intersection requires more complex decision-making than an empty racetrack. Similarly, navigating through a maze of undergrowth requires different decision processes than the more uniform grassland. Past research has shown that animals adapt their behavioral strategies based on experience, environmental complexity, and environmental geometry[1–3] and that environmental richness can affect brain structure and overall cognition.[4–6] Neurophysiologically, adaptive decision-making is mediated by circuit dynamics that are distributed and coordinated across multiple brain areas that represent different components of these complex conditions.[7–15] Yet, the role that environmental complexity plays in adaptive decision-making and the role of environmental demands on the interactions between multiple brain regions are not well understood.[16][,][17] To bridge this gap, we simultaneously recorded from multiple, interconnected brain regions on a foraging decision task with changing reward rules across a systematic variation of environment complexity. 

Planning relies on internally generated models of the environment and expectations of the future.[18–21] Conversely, procedural learning uses cached situation-action associations.[22–24] While 

deliberative behaviors are flexible but slow,[25][,][26] procedural behaviors are computationally efficient but inflexible.[8][,][12][,][13][,][27][,][28] Previous evolutionary analyses have found that environmental complexity and topology affect the usefulness of these strategies.[3][,][17] However, it remains unclear how environmental parameters influence the neural representations that guide action selection. 

Three regions—hippocampus (HC), dorsolateral striatum (DLS), and medial prefrontal cortex (mPFC)—are hypothesized to make distinct contributions to decision-making. HC is hypothesized to encode the state space enabling flexible behaviors,[8][,][12][,][13][,][29–32] while DLS is hypothesized to encode inflexible action chains underlying automated behaviors.[24][,][33–40] The hypothesis that decision-making arises from at least two competing systems raises questions about how they are balanced to create adaptive behaviors.[9][,][14][,][21][,][41][,][42] Dorsomedial prefrontal cortex (dmPFC) has been shown to encode various task-relevant features, such as the problem space and strategy, and thus has been put forward as a candidate.[43–50] 

HC is a crucial component of the network supporting memory function and cognitive, spatial, and non-spatial information processing.[8][,][12][,][13][,][51–56] Furthermore, HC pyramidal cells (‘‘place cells’’) are tuned to environmental parameters such as geometry and space.[12][,][57–61] Decoding methods applied to HC ensemble activity have revealed time-compressed sequential 

**==> picture [16 x 17] intentionally omitted <==**

4096 Neuron 112, 4096–4114, December 18, 2024 ª 2024 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

**ll** 

## Article 

extra-field firing at decision times that suggest imagination of future outcomes.[18][,][62–70] However, how environmental geometry changes HC network-level representations and thus how it influences planning and deliberative systems remains unknown. 

By contrast, DLS is hypothesized to encode cached action sequences for procedural learning and decision-making.[23][,][24][,][27][,][35][,][71] DLS ensembles show punctate bursting activity at the start and end of action sequences.[33][,][37][,][42] Decoding striatal activity during these bursts reflects the current state and past experiences more than future options.[72] These results suggest that DLS is involved in initiating stereotyped behaviors associated with procedural decision-making. However, how environmental geometry changes these firing patterns, and thus how it influences procedural responses, remains unknown. 

While there have been numerous studies looking at procedural and deliberative decision-making and their neural instantiations, existing evidence has not addressed the role that task and environmental structure play in modifying the usefulness of procedural or prospective decision-making in differently complex environments and the balance between them. 

To address these questions, we developed a dynamic, complex spatial foraging task for rats. We added a complex central path to the left/right/alternation (LRA) task, a spatial rule-switching task in which rats are required to adjust their behavioral strategies after uncued changes to the reward contingency.[42–44][,][50][,][66][,][73–78] We quantitively varied complexity to evaluate its impact on behavior and neural activity. Using simultaneous silicon probe recordings of HC, mPFC, and DLS ensembles in freely behaving rats, we found that environmental geometry impacted task-relevant neural representations and changed the timing of the transition between decision-making systems. Furthermore, chemogenetic inactivation of dorsal mPFC impaired the ability of the rats to recognize task regularity and stability and led to both acute and long-term learning deficits, highlighting mPFC’s role in balancing between these decision systems. 

## RESULTS 

## Environmental complexity differentially impacted deliberative and procedural systems 

Tostudythedeliberativeandproceduraldecision-making,weused the LRA foraging task (Figures 1A, S1A, and S1B)[42–44][,][50][,][66][,][73–78] and collected pairs of simultaneous recordings from dorsal HC CA1, dorsal mPFC, and DLS (Figures 1B, S1C, and S1D, Table S1; nHC = 7; nDLS = 4; nmPFC = 7). To study the role of mPFC in selecting the appropriate decision system, in a separate cohort of rats, we chemogenetically inactivated dorsal mPFC (CaMKIIa-hM4Di DREADDs) (Figures 1C, S7A, and S7B; nDREADDs Virus = 8, nControl Virus = 8). 

In the LRA task, rats traversed a central maze segment that included three low-cost decision points with dead ends on either side, followed by a high-cost choice point between the left and right return arms (Figures 1A and S1A).[42–44][,][50][,][66][,][73–78] Three rules determined which return arm would be rewarded as a function of the behavior of the rat: left (L)—reward was presented on the left side; right (R)—reward was presented on the right side; alternation (A)—reward was presented on the opposite side of the previous run, forcing rats to alternate between left and right. If the 

rats made the correct decision, they received food at the reward arm and at the start of the maze. If the rats made an incorrect decision, they received no reward at either location. There were two uncued rule switches per session that occurred roughly at 15 and 30 min through the 45 min session. Each session included all three rules (Figure 1D). 

In line with previous research,[42–44][,][50][,][66][,][73–78] rats rapidly adjusted their behavior to the new rule (Figures 1E and S2A) and performed similarly under each rule with a slight decrease in performance under the alternation condition (Figures S2B and S2C; mean ± SD 45.7 ± 12.9 laps/block; mean ± SD 82.7 ± 10 correct lap percentage L and R and 70.3 ± 12 correct lap percentage Alt.). 

This task probes the interaction between deliberative and procedural decision-making (Figure 1D).[44][,][50][,][77][,][79][,][80] Prior work has found that rats display vicarious trial and error (VTE) behaviors around rule switches at high-cost choice points, pausing and orienting back and forth toward the two arm options before making a decision, quantified by the integrated angular velocity (measured as "IdPhi" or, when Z scored, zIdPhi; Figures 1F, 1G, and S2D; see STAR Methods).[21][,][81][,][82] Neural recordings indicate that VTE is often accompanied by HC cell assemblies sweeping forward of the animal serially assessing each option, and thus is believed to reflect a behavioral correlate of deliberation.[18][,][62][,][66][,][74] In line with previous research, we found that VTE behaviors significantly increased after rule switches (Figure 1G).[43][,][75][,][76] 

By contrast, prior work has shown that rats develop stereotyped responses on this task under stable contingencies and after the contingency has been learned.[34][,][42][,][72][,][80] We quantified behavioral stereotypy as the reciprocal of the Euclidean distance between pairs of path trajectories through the central maze segment on a lap-by-lap basis (Figure 1H). Notably, rats showed increased stereotypy as they adopted the appropriate behavioral strategy (Figure 1I). Both pre-switch and post-switch periods were characterized by an increase in path similarity, with the rule changes disrupting this pattern. 

Prior research suggests that environmental complexity advantages different decision systems.[17][,][83] We modulated environmental complexity by parametrically changing the central maze segment (central path) (Figures 2A and S1A). To quantify environmental complexity, we created a graph of the topologically discretized space. Structural complexity was defined as the total information content across all sets of equivalent trees that could be created from a given maze configuration (see STAR Methods).[84–87] Walls used to manipulate the interior navigational sequence (A: open middle, B: open left, C: open right) created 27 unique mazes with different levels of complexity (Figure 2A). These mazes formed three clusters, which we partitioned into low, mid, and high complexity for subsequent analysis (Figure 2A). 

Theoretically, if rats are using different decision-making algorithms, they should show predictably different behaviors, neurophysiological representations, and behavioral-neurophysiological interactions. Environments that feature multiple decision points are hypothesized to encourage decision-making that relies more on deliberation, thus resulting in more variable behaviors, longer hippocampal nonlocal sequences, and differential 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 112, 4096–4114, December 18, 2024 4097 

**ll** 

Article 

**==> picture [488 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>E F G H I<br>**----- End of picture text -----**<br>


**==> picture [8 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [9 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [9 x 5] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [9 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [10 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 6] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 6] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 6] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 6] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 6] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 5] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [7 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [7 x 7] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [73 x 72] intentionally omitted <==**

**==> picture [54 x 32] intentionally omitted <==**

Figure 1. Behavior in left/right/alternation task 

(A) The left/right/alternation (LRA) foraging task. Three different wall types: open middle (wall A), open left side (wall B), and open right side (wall C) were used to create intermediary decision points. 

- (B) Recording sites from dorsal mPFC, DLS, and dorsal HC. 

(C) Example histology and illustration of viral spread for DREADDs (red) and control virus animals (blue). 

(D) Example behavior from a single session and the hypothesized arbitration between deliberative and procedural decision-making systems. 

(E) Rat performance aligned to rule switches. 

- (F) Example vicarious trial and error (VTE) and non-VTE paths. 

- (G) Z scored IdPhi aligned to rule switches. 

- (H) Two example paths (orange and green) through the central maze segment showing low (top) and high (bottom) path stereotypy. 

(I) Trajectory stereotypy between pairs of paths through the central maze segment around rule switches. (E and G) Black line and shaded error bars show mean ± SEM. 

engagement of DLS. By contrast, low-complexity environments are hypothesized to encourage decision-making that relies more on habit, thus resulting in the development of stereotyped responses with shorter, less sequential hippocampal nonlocal sequences (Figure 2B). 

To directly assess the role environmental complexity plays in modulating decision systems, we analyzed the impact of complexity on task performance. Rats made more errors in more complex environments (Figure S2E; mixed-effects ANOVA F(18) = 2.35, p = 0.0033). While there were significant interaction effects between environmental complexity and performance across contingency and rule blocks (mixed-effects ANOVA laps/contingency 3 complexity F(36) = 2.85, p < 0.001; mixed-effects ANOVA performance/contingency 3 complexity F(36) = 2.16, p < 0.001), there was no systematic pattern (Figures S2F and S2G). Looking at the effect of environmental complexity on VTE, we found that there was a slight increase in VTE on complex environments (Figure 3A; mixed-effects ANOVA F(18) = 1.59, p = 0.072, Levene’s test F(2,141) = 0.79, p = 0.45). 

Rats explored the central path (Figure S1A) by taking unrepeated paths to the corners and edges of the dead-end spaces (Figure 3B). Exploration increased around rule switches (Figures 3C, S2H, and S2I) and was correlated with the prominence of reorientation behaviors (Figures 3D and S2J). These data suggest that exploration also provides a behavioral correlate of deliberation that, unlike VTE, is associated with the central path. Notably, the proportion of exploratory laps increased with environmental complexity (Figure 3E; mixed-effects ANOVA F(18) = 2.61, p = 0.0011), which is in line with the idea that environmental complexity modulates the competition between deliberative and procedural decision-making.[17] 

Central path stereotypy was also modulated by complexity. Increased complexity resulted in lower behavioral stereotypy and slower development of stereotypy following rule switches (Figures 3F and 3G). Concurrently, we found that path stereotypy in the return rails (choice point exit to start of maze entry) decreased (Figure S2K), and side feeder linger times increased after rule switches (Figure S2O), with errors inducing more deviation from stereotyped paths (Figure S2L) and longer feeder wait 

4098 Neuron 112, 4096–4114, December 18, 2024 

Article 

**==> picture [8 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


**==> picture [139 x 161] intentionally omitted <==**

**==> picture [8 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
B<br>**----- End of picture text -----**<br>


**==> picture [35 x 60] intentionally omitted <==**

**==> picture [36 x 51] intentionally omitted <==**

**==> picture [47 x 91] intentionally omitted <==**

**==> picture [47 x 70] intentionally omitted <==**

**==> picture [44 x 54] intentionally omitted <==**

**==> picture [57 x 94] intentionally omitted <==**

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [48 x 70] intentionally omitted <==**

**==> picture [47 x 70] intentionally omitted <==**

**==> picture [46 x 35] intentionally omitted <==**

Figure 2. Quantification of environmental complexity (A) Environmental complexity of different maze. The colored circles indicate the low-, mid-, and high-complexity designations. (B) Illustration of hypothesized behavior and neurophysiology. 

times (Figure S2P). However, neither metric was modulated by side choice (Figures S2M and S2Q) or environmental complexity (Figures S2N and S2R). The effects of environmental complexity on behavioral stereotypy were restricted to the central segment of the maze, where, unlike the return rails, there exists variable navigational paths (Figure 2A).[17] 

These results indicate that modulating the environmental structure has important consequences on deliberative and procedural behaviors. 

## Hippocampal sequences were modulated by environmental complexity 

Place cells commonly found within the CA1 region of the HC have been shown to provide insight into how the brain’s deliberative decision system represents information.[18][,][21][,][26][,][88–91] Place fields appeared in both simple and complex environments (Figures 4A and 4B), and the number of place cells and their distribution through the maze did not differ across environments (Figures S3A and S3B). The firing of putative pyramidal cells (89.3% ) was largely local throughout the maze (Figure 4B). However, place fields were significantly smaller in more complex environments, suggesting differences in network-level representations of space (Figure S3C; one-way ANOVA F(2) = 9.91, p < 0.001). These differences were not driven by differences in speed (Figure S3D; mixed-effects ANOVA F(18) = 1.29, p = 0.20). To investigate how these network-level differences may affect nonlocal HC representations, we looked at theta sequences (Figure 4C). 

Theta oscillations (6–12 Hz) are prominent in CA1 and can contain sequentially active place cells.[18][,][62][,][69][,][92–97] To find signif- 

icant theta-timescale sequential activity, theta cycles were identified and limited to those that had R5 cells active. The spike trains within each candidate theta cycle were analyzed using Bayesian decoding[98] (20 ms bins) to relate firing activity to underlying behavior, and the correlation between decoded position and time was measured as a metric of sequential activation (theta sequence score).[99–101] Intuitively, this metric indicates the ordered nature and clarity of the decoded representations in each theta cycle (Figures 4D and 4E) Using this method, we found significant theta sequences during the entire navigational period. 

While the proportion of significantly sequential theta cycles did not differ between environments (Figure 4F; mixed-effects ANOVA F(12) = 1.23, p = 0.28; Figure S3E), we found that the average theta sequence score and sequence scores restricted to the central path significantly increased with complexity (Figures 4G and 4H; Kruskal-Wallis test H(2) = 765.94, p < 0.001 and mixed-effects ANOVA F(12) = 2.48, p = 0.01). Similar results were found when taking the slope of the decoded sequences (Figures S3E and S3F; Kruskal-Wallis test H(2) = 66.67, p < 0.001). These results suggest that increasing environmental complexity produced more robust nonlocal sequence representations in HC. 

Prior research suggests that theta cycles consist of two components: (1) local representation during the first half of theta, and (2) nonlocal sequential representations during the second half of theta.[64] To quantify the prevalence of nonlocality, we used Bayesian decoding to compute the difference in the posterior probability of the decoded location between the second and first 

Neuron 112, 4096–4114, December 18, 2024 4099 

Article 

## **ll** 

**==> picture [417 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>**----- End of picture text -----**<br>


**==> picture [37 x 39] intentionally omitted <==**

**==> picture [38 x 39] intentionally omitted <==**

**==> picture [39 x 54] intentionally omitted <==**

**==> picture [34 x 105] intentionally omitted <==**

**==> picture [58 x 6] intentionally omitted <==**

**==> picture [177 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
F G<br>**----- End of picture text -----**<br>


**==> picture [144 x 56] intentionally omitted <==**

Figure 3. Behavioral effects of environmental complexity (A) Proportion of VTE laps (zIdPhi > 0.25) in low-, mid-, and high-complexity environments. 

(B) Top: example of a low exploration session, and Bottom: example of a high exploration session. 

- (C) Percentage of exploratory laps aligned to rule switches. Black line indicates mean, and the shaded gray region ± SEM. 

(D) Distribution zIdPhi values at the choice point for non-exploratory and exploratory laps. Horizontal line denotes the boundary for identifying VTE events (Kruskal-Wallis test H(1) = 46.41, p < 0.001). 

- (E) Percentage of exploratory laps per session broken down by maze complexity. 

- (F) Examples of trajectory stereotypy in different environments. 

- (G) Development of stereotypy around rule switches. 

(A and E) n = 144; mixed-effects ANOVA; n.s. p > 0.05, ***p < 0.001. 

half of theta aligned to the rat’s position (Figure 4I). We found that environmental structure modulated this balance such that nonlocal decoding during the second half of theta was more prominent in more complex environments (Figure 4I). 

Together, these results suggest that environmental structure modulated sequential hippocampal activity during theta cycles. This network level modulation of HC activity implies important changes to the deliberative decision-making system based on environmental structure, with more complex environments giving rise to stronger neural representations of future options. 

## Theta sequence scores were correlated with deliberative behaviors 

Next, we asked whether there was a coherent relationship between HC nonlocal activity and deliberative behaviors. Consistent with this hypothesis, we found that average theta sequence scores at the choice point were significantly correlated to zIdPhi 

values (Figure 5A; t test(80) = �6.8, p < 0.001). In line with previous findings, theta sequence scores were higher on VTE laps (Figure 5B; Kruskal-Wallis H(1) = 7.78, p = 0.0053).[50][,][73] Similarly, the average theta sequence scores and the amount of exploration in the central path were also significantly correlated (Figure 5C; t test t(84) = �6.9, p < 0.001): theta sequence scores were significantly higher on exploratory laps (Figure 4D; Kruskal-Wallis H(1) = 37.94, p < 0.001). Sequence slopes produced equivalent results (Figures S4A–S4D). 

To examine HC representations during procedural decisionmaking, we calculated the average stereotypy of each lap, comparing the similarity of its trajectory to prior and subsequent laps (±5 laps). Trajectory stereotypy and theta sequence scores were inversely correlated (Figure 5E; t test t(84) = 5.79, p < 0.001; Figure S4E), in line with theories that hypothesize a competition between the deliberative and procedural decision-making systems. 

4100 Neuron 112, 4096–4114, December 18, 2024 

## Article 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**==> picture [487 x 247] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>D E<br>F G H I<br>**----- End of picture text -----**<br>


**==> picture [111 x 91] intentionally omitted <==**

Figure 4. Theta sequences in differently complex environments (A) Two example HC tuning curves. 

(B) Spatially binned activity of putative pyramidal cells on the linearized maze. 

(C) An example of HC ensemble representation of space. First row: the maze and an example trajectory (dark blue) along with raw (gray) and theta frequency filtered LFP (green). Second row: spike raster of simultaneously recorded HC cells on an example lap. Cells are ordered and colored by their respective centers. Gray line shows the actual trajectory of the rat. Third row: decoded activity from the HC ensemble. Black line shows the actual trajectory of the rat in linearized space. 

(D and E) Examples of (D) high and (E) low score theta sequences. Left: HC cell spiking during a theta cycle ordered and colored by field location. Raw LFP (gray) and theta filtered LFP (green) are shown below with vertical lines indicating the peaks and trough of the theta cycle. Right: Bayesian decoding during the theta cycle. The arrow and cyan line show the actual position of the rat. 

- (F) Average percent of significant theta sequences per session. 

- (G) Distribution of theta sequence scores for the different maze-complexity groups. Dashed lines indicate medians. Kruskal-Wallis test, ***p < 0.001. 

- (H) Session average theta sequence scores along the central path for the different maze-complexity groups. 

(I) Differences in posterior probability of the decoding in the 1[st] (peak to trough) and 2[nd] half (trough to peak) of each identified theta cycle aligned to rat’s position. Positive values indicate more local, and negative values indicate more non-local decoding. The red line indicates the shuffle distribution. Black lines indicate significant differences between pairs of environment complexity (top line low vs. mid, middle line mid vs. high; bottom line low vs. high) (repeated measures ANOVA for complexities across positions; interaction: F(34) = 51, p < 0.001, post hoc on each position bin via two-sided Wilcoxon rank-sum corrected for multiple comparisons). 

- (F and H) Mixed-effects ANOVA, n.s. p > 0.05, **p < 0.01. 

These results suggest that CA1 theta sequences accompanied deliberative behaviors and did not have the same level of sequential structure during procedural behaviors, consistent with hypotheses that theta sequences underlie fast timescale memory recall and deliberation.[70] 

## Environmental structure modulated representations of procedural behaviors 

This switch to behavioral automation after adaptation to the new task rule is hypothesized to be driven by DLS and is often associated with the development of characteristic firing patterns of 

Neuron 112, 4096–4114, December 18, 2024 4101 

Article 

## **ll** 

**==> picture [378 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D E<br>**----- End of picture text -----**<br>


**==> picture [93 x 115] intentionally omitted <==**

Figure 5. Relationship between theta sequence score and deliberative behaviors (A) Distribution of correlations between zIdPhi and mean theta sequence score at the choice point. (B) Average theta sequence score at the choice point for laps identified as VTE and non-VTE. (C) Distribution of correlations between exploration amount and mean theta sequence score in the central path. 

(D) Average theta sequence score through the central path for laps that were identified as exploratory and non-exploratory. 

(E) Distribution of correlations between central path stereotypy and average theta sequence score in the central path. (A, C, and E) Dashed lines indicate means. t test, ***p < 0.001. 

(B and D) Kruskal-Wallis test, **p < 0.01, ***p < 0.001. 

DLS cell assemblies, which are hypothesized to reflect the boundaries of well-learned action sequences—‘‘task bracketing.’’[27][,][33][,][36–38][,][102] To test this hypothesis, we quantified the average firing rates of putative medium spiny neurons across the linearized maze on each lap aligned to the start of a session and rule switches averaged across the different maze groups (Figure 6A). DLS firing was highly influenced by environmental complexity and structure (Figures 6A, S5A, and S5B). In simple environments, which are comparable to other experimental paradigms in which task bracketing has been studied, such as the classical T-maze, we found action boundaries at the start of the maze and the choice point (Figure 6A left). Increasing complexity changed DLS activity throughout the navigation sequence. The changes to DLS neuronal activity at discrete positions within the central path across the different mazes were not driven by other motor-related behavioral variables. We found similar residual activity patterns throughout the maze after regressing out either velocity (Figures S6A and S6B) or IdPhi as a proxy for head turning (Figures S6D and S6E). 

Previous research has quantified task bracketing as the subtraction of firing rate in the central path from the firing at the start of the maze (task-bracketing index; Figure 6B).[33][,][35][,][36][,][42] Positive values suggest the formation of meaningful action boundaries for automation. We found task-bracketing index decreased with environmental complexity (Figure 6C; mixed-effects ANOVA F(8) = 2.31, p = 0.037), as would be expected from slower behavioral automation with increased complexity. 

Given the firing patterns that we observed in mid- and highcomplexity environments, we hypothesized that the structure of the environment might influence how the environment was represented and the boundaries of cached action sequences. Spatial cross correlation of ensemble activity along a linearized projection of the path elucidates representational similarity between different 

portions of an environment. For example, local and distinct ensemble activity would produce high correlation along the diagonal (Figure S5C). In simple environments, DLS represented the central path with highly correlated activity throughout the central path (Figures 6D left, S5D, and S5E; broad block structure), with a representational switch appearing at the choice point (Figures S5D and S5E). Similar patterning was observed with mPFC activity (Figure S5F). By contrast, with increased environmental complexity, DLS representations became much more local (Figures 6D, S5D, and S5E). Despite increased local representation throughout the central path in both mPFC and DLS, wall identity and placement influenced representational similarity. In line with the broad representation of the central path in the AAA maze (Figures S5D–S5F), we found broad representational similarity throughout the central path in the BBB maze with a choke point occurring between entry into the first wall (Figures S5D– S5F). By contrast, we found non-uniform representational similarity in complex mazes when wall identities were not identical— environmental structure greatly influenced how the environment was chunked (Figures S5D–S5F). 

Theories hypothesizing a competition between decision systems predict that there should be an inverse relationship between theta sequence scores and task bracketing. We found that HC theta sequences were positively correlated with deliberative behaviors and inversely correlated with procedural behaviors (Figure 5E). Previous work suggests that task bracketing is related to the development of procedural behaviors and inversely correlated with VTE behaviors.[17][,][27][,][33][,][36–38][,][83][,][102] To compare them, we plotted HC (nRats = 7) theta sequence scores and DLS (nRats = 4) task bracketing aligned to rule changes. We found an increase in theta sequence score and corresponding decrease in task bracketing aligned to rule switches predominantly in simple environments. While there was a slight dynamic 

4102 Neuron 112, 4096–4114, December 18, 2024 

## Article 

**==> picture [16 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [46 x 35] intentionally omitted <==**

**==> picture [488 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>C D<br>E<br>**----- End of picture text -----**<br>


**==> picture [331 x 92] intentionally omitted <==**

Figure 6. DLS ensemble activity across the linearized maze and the arbitration between deliberative and procedural decision-making (A) Top row: average firing rate of all putative dorsolateral striatum medium spiny neurons over the linearized track averaged across the different complexity groups. Firing rates are plotted as a function of laps aligned to the start of rule blocks. Bottom row: average firing rates averaged across laps and maze group. Solid lines indicate mean, and the shading ± SEM. Dashed lines indicate the internal wall locations projected onto the linearized maze. (B) Quantification of task bracketing. 

(C) Average task-bracketing score for each session broken down by maze-complexity group. Kruskal-Wallis test, *p < 0.05. (D) Spatial cross correlation of DLS ensemble activity broken down by maze-complexity group. 

(E) Blue: mean HC theta sequence score across the central path aligned to rule switches. Orange: DLS task bracketing aligned to rule switches. For both plots, solid lines indicate mean, and the shading ± SEM. 

change in DLS task bracketing in mid-complexity environments, there was no corresponding decrease in task bracketing in complex environments, likely because task bracketing remained low (or never developed) in complex environments (Figure 6E). 

## dmPFC encoded strategy changes, engaging the deliberative system after rule switches 

The prefrontal cortex is hypothesized to encode ‘‘problem task space,’’ goals, subgoals, and strategy.[43–45][,][103][,][104] Accordingly, medial PFC has been associated with balancing deliberative 

Neuron 112, 4096–4114, December 18, 2024 4103 

Article 

## **ll** 

**==> picture [465 x 444] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>B C D<br>E F G<br>H I J K<br>**----- End of picture text -----**<br>


Figure 7. Representational transitions after rule switches and predictions of prospective representations (A) Lap-by-lap correlation of dmPFC, DLS, and HC population activity aligned to rule switches. Correlation matrices are averaged across the rule changes. The vertical and horizontal dashed lines correspond to the last lap of the previous rule block. (B) Distribution of physiology-based change points aligned to the task rule switch laps. 

(legend continued on next page) 

4104 Neuron 112, 4096–4114, December 18, 2024 

**ll** 

## Article 

and procedural decision-making.[48][,][105][,][106] Previous research has found that dorsal mPFC changes its representations around rule switches and behavioral shifts between the two decision systems on the LRA task.[43][,][44] One analysis for identifying these changes in dmPFC representations has been to correlate lapby-lap ensemble firing rates.[43] In line with previous results, population activity in dmPFC was highly consistent when behavior was automated (Figure 7A), i.e., prior to the switch and after �10 laps into a given rule. However, when the rule changed, so too did dmPFC ensemble activity.[43][,][44] Interestingly, we found similar ensemble dynamics in DLS and HC (Figure 7A). 

If dmPFC is responsible for setting strategy, we would expect dmPFC to change its firing patterns before either HC or DLS. To identify when ensemble changes occurred, we used a combination of hierarchical clustering[43] to identify reliable ensemble representations and a change point analysis[107] to identify moments that neural activity shifted. Across all recordings, representational transitions across all three regions predominantly occurred after rule switches; however, dmPFC ensembles changed firing patterns on average earlier than either HC or DLS (Figure 7B), in line with a putative role of dmPFC in setting a strategy and relaying this information downstream to HC and DLS.[44] 

To directly evaluate the change point timing between regions, we leveraged our simultaneous recordings between pairs of brain areas (dmPFC-HC nRats = 5; dmPFC-DLS nRats = 2). We found that changes to dmPFC ensemble firing patterns occurred prior to both HC (mean 1.4 laps; Wilcoxon signed-rank test z = �2.39, p = 0.017) and DLS (mean 9.3 laps; Wilcoxon signedrank test z = �4.01, p < 0.001) (Figure 7C). 

To study the information transfer between dmPFC and HC for strategy setting, we next looked at prediction of HC state by dmPFC activity. To determine whether dmPFC activity carried information about what HC was representing, we used a 5-fold cross-validated Bayesian decoding to predict theta sequence scores from dmPFC ensemble activity in rats with simultaneous recordings (dmPFC-HC nRats = 5). Critically, dmPFC activity predicted the nature of nonlocal representations in HC (Figure 7D). dmPFC activity was more predictive of the HC state compared with when dmPFC representations were destroyed (circularly shifted spike times) and when short-timescale coupling between dmPFC and HC state was destroyed, even though internal rep- 

resentations of dmPFC were preserved (across-session shuffled HC theta sequence scores). However, dmPFC did not predict HC theta sequence scores on a theta-cycle-by-theta-cycle basis. dmPFC activity was not more predictive than shuffled theta sequence scores when that shuffling was restricted to a lap (breaking short-timescale relationships but preserving longertimescale relationships) (Figure 7D). 

There was a significant coupling between dmPFC activity and HC state, only over longer behaviorally relevant timescales (Figure 7D), suggesting a role in strategy setting on any given lap.[50] Furthermore, dmPFC activity was more predictive of HC state following rule switches (Figure 7E). Notably, while there was no significant relationship between prediction posterior probability restricted to the choice point and zIdPhi values (Figure 7F; t test(41) = �1.18, p = 0.25), we found a significant correlation between dmPFC prediction power and exploration amount in the central path (Figure 7G; t test(41) = �2.74, p = 0.009), which suggests that these two deliberative behaviors (VTE and exploration) may be associated with different neural processes. 

Previous research suggests the existence of reward-related modulation of dorsal mPFC (anterior cingulate cortex and dorsal prelimbic) activity.[108–110] In line with that research, we found that dmPFC activity increased following rule switches (Figure 7H) and had an overall increase in firing rate following errors (Figure 7I). Specifically, the increase in firing rate at the feeders (Figure 7J), in which error signaling would be immediate (omission of expected reward), preceded the modulation of dmPFC activity in the central path (Figure 7K). 

## Inactivating mPFC reduced deliberative behaviors and delayed behavioral adaptations to rule switches 

While we found a relationship between dmPFC population activity and initiation of strategies, it remained unclear to what extent dmPFC causally influenced the balance between deliberative and procedural strategies. To test this question, we used inhibitory designer receptors activated by designer drugs (DREADDs)[111] in a separate cohort of rats (AAV5-CaMKIIa-hM4Di(Gi)-mCherry; nRats = 8, nSessions = 252; DREADDs) compared with an across-subject viral control (AAV5-CaMKIIa-mCherry; nRats = 8, nSessions = 256; control) to investigate the behavioral effects of dmPFC inactivation (deschloroclozapine [DCZ][112] condition) 

**==> picture [46 x 35] intentionally omitted <==**

(C) Distribution of the difference in physiology-based change points for simultaneously recorded rats (nRats HC-dmPFC = 5 and nRats DLS-dmPFC = 2). Black dots indicate mean physiology-based change point lap difference between region in non-simultaneously recorded rats. Wilcoxon signed-rank test, *p < 0.05, ***p < 0.001. (D) Distribution of the posterior probabilities of dmPFC activity predicting binned theta sequence score. The red line indicates actual data. The blue lines indicate the different shuffles. The dashed line indicates uniform probability. (E) Posterior probability of dmPFC activity predicting binned theta sequence score aligned to the first error lap at or closest to rule switches. Solid lines indicate mean (red: actual, blue: dmPFC spike time shuffle), and shading ± SEM. 

(F) Distribution of correlations between zIdPhi and mean posterior probability of dmPFC prediction of HC theta sequence score at the choice point. Red dashed line indicates the median of the actual data, and the blue lines indicate different shuffle medians. (G) Distribution of correlations between exploration amount and mean posterior probability of dmPFC prediction of HC theta sequence score in the central path. Representation as in (F). (H) Z scored dmPFC lap firing rate aligned to the first error lap at or closest to rule switches. Solid line indicates mean, and the shading ± SEM. (I) Distribution of Z scored dmPFC lap firing rate for correct (green) and error (red) trials. Dashed lines indicate the median. (J) Z scored dmPFC firing rate restricted to the side feeder zones aligned to the first error lap at or closest to rule switches. Representation as in (H). (K) Z scored dmPFC firing rate restricted the central path (start of maze exit to choice point entry) aligned to the first error lap at or closest to rule switches. Representation as in (H). (F and G) t test, n.s. p > 0.05, **p < 0.01. 

Neuron 112, 4096–4114, December 18, 2024 4105 

**==> picture [76 x 35] intentionally omitted <==**

**==> picture [17 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
ll<br>**----- End of picture text -----**<br>


**==> picture [47 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
Article<br>**----- End of picture text -----**<br>


**==> picture [414 x 364] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>D E F G<br>J<br>H I K<br>**----- End of picture text -----**<br>


**==> picture [117 x 41] intentionally omitted <==**

**==> picture [74 x 70] intentionally omitted <==**

**==> picture [44 x 41] intentionally omitted <==**

Figure 8. Behavioral effects of mPFC inactivation with DREADDs (A) Example histology (right) and illustration of viral spread (left) for DREADDs virus animals (red) and control virus animals (blue). 

(B) Distribution of rat performance for mPFC-inactivated rats (DREADDs: DCZ dark pink) and control virus animals (light pink). One-way ANOVA, ***p < 0.001. (C) Distribution of minimum distance between behavioral change points and rule switch laps for DREADDs virus rats under DCZ, post DCZ (2[nd] day saline repeat), and VEH, as well as all control virus animals. One-way ANOVA, n.s. p > 0.05, *p < 0.05. (D) Distribution of proportion of VTE events per session for inactivated animals (DREADDs: DCZ, red), for 2[nd] day after inactivation (DREADDs: post DCZ, blue), and controls (control, light pink). 

(E) Difference in the proportion of VTE events between 1[st] day manipulation and 2[nd] day rebound (day 2 � day 1) for DREADDs (dark pink) and control (light pink) animals with respect to drug condition (ANOVA virus 3 DCZ F(1) = 3.86, p = 0.05). (F) Per session distribution of the percentage occupied space in the central segment of the maze for inactivated animals for 2[nd] day after prefrontal inactivation and controls. 

(G) Difference in the percentage of the central segment of the maze occupied between 1[st] day manipulation and 2[nd] day rebound (day 2 � day 1) for DREADDs and control animals with respect to drug condition (ANOVA virus 3 DCZ F(1) = 25.41, p < 0.001). 

(legend continued on next page) 

4106 Neuron 112, 4096–4114, December 18, 2024 

**ll** 

## Article 

(Figures 8A, S7A, and S7B; see STAR Methods). To investigate the long-term effects of dmPFC inactivation and 2[nd] day compensatory changes after either dmPFC inactivation (hereafter referred to as DREADDs: DCZ) or within-subject control (hereafter referred to as DREADDs: VEH) conditions, we also included a post-manipulation saline repeat of the task (post DCZ or post VEH), which provided us with a washout day (Figure S7C). 

Interestingly, we found that dmPFC inactivation resulted in overall worse performance when compared with the across-subject control virus rats, pointing toward a fundamental involvement of dmPFC functioning in proper execution of the task (Figures 8B, S7D, and S7E; one-way ANOVA F(1) = 22.95, p = 0.0001, nSessions-DCZ = 64). Critically, the central component of the task is the rats’ ability to adapt their decision-making following a change to the task rule. To quantify how dmPFC manipulation changed the speed of behavioral adaptation, we computed the behavioral change point.[107] dmPFC inactivation (DREADDs: DCZ) led to slower behavioral adaptation to rule switches when compared with post-manipulation saline and VEH days, as well as control virus animals (Figure 8C; one-way ANOVA F(3) = 3.51, p = 0.015; Tukey’s HSD post hoc DCZ vs. all others p < 0.05, all other comparisons p > 0.05; nSessions-DCZ = 64, nSessions-postDCZ = 64, nSessions-VEH = 124). 

Given evidence that dmPFC activity may be influencing deliberative strategies through HC engagement, we investigated the effects of dmPFC inactivation on VTE and exploration. Surprisingly, we found that the proportion of VTE events under inactivation (DREADDs: DCZ) was not significantly different from the proportion of VTE events observed in dmPFC-intact animals (control) (Figure 8D; mixed-effects ANOVA F(8) = 2.58, p = 0.0094; Tukey’s HSD post hoc DCZ vs. post DCZ p = 0.0038 and DCZ vs. control p = 0.96). Similarly, the amount of space explored after dmPFC inactivation was comparable to control animals (Figure 8F; mixed-effects ANOVA F(8) = 6.25, p < 0.001; Tukey’s HSD post hoc DCZ vs. post DCZ p < 0.001 and DCZ vs. control p = 0.47). Thus, while dmPFC inactivation impaired the rats’ ability to adapt to new task rules, we paradoxically found no evidence for acute deficits in rats’ ability to employ deliberative behaviors. One possibility is that while rats engaged in deliberative behaviors, inactivation of dmPFC impaired their ability to use the information that they gained about the task and rules to perform efficiently. 

Building on this hypothesis that dmPFC serves a critical role in the use of gained information, we leveraged a unique component of our experimental design. By repeating each behavioral condition on a second day in a saline washout condition between manipulations (DCZ rebound nSessions-Active = 64 and nSessions-Control = 65, or VEH rebound nSessions-Active = 62 and nSessions-Control = 63), we were able to directly evaluate prolonged 

short-term impacts of dmPFC inactivation on task performance through compensatory behavior rebounds following acute dmPFC inactivation. The effects of dmPFC manipulation were much more pronounced when we considered these rebound effects. VTE behaviors showed significant compensatory increase following mPFC inactivation on the previous day (Figure 8E, DREADDs: DCZ rebound; Wilcoxon signed-rank test z = 2.53, p = 0.0043); but a significant decrease if dmPFC functioning was not manipulated (Figure 8E, DREADDs: VEH rebound; Wilcoxon signed-rank test z = �1.65, p = 0.049; Figure S7F). Similarly, exploration increased on the second day following dmPFC inactivation (Figure 8G, DREADDs: DCZ rebound; Wilcoxon signed-rank test z = 3.63, p < 0.001), but decreased on the second day if dmPFC functioning was not manipulated (Figure 8G, DREADDs: VEH rebound; Wilcoxon signed-rank test z = � 2.41, p = 0.0079; Figure S7G). Neither of these compensatory effects after dmPFC manipulation were seen in control animals (Figure 8E; control: DCZ rebound Wilcoxon signed-rank test z = 0.13, p = 0.9, control: VEH rebound Wilcoxon signed-rank test z = �0.38, p = 0.7 and Figure 8G; control: VEH rebound; Wilcoxon signed-rank test z = �1.63, p = 0.1, VEH condition: Wilcoxon signed-rank test z = �0.18, p = 0.89). 

Given the impact that dmPFC inactivation had in eliciting compensatory behavioral rebounds, we hypothesized that our manipulation may be causing long-term deficits in strategy setting and learning. We compared the changes to VTE and exploration around rule switches in DREADDs and control animals by pooling across all drug and rebound conditions. In line with our previous findings, we found that both the prominence of reorientation behaviors (zIdPhi) and the proportion of exploratory laps increased around rule switches in both all animals. However, this increase happened earlier in control animals, especially when looking at zIdPhi, suggesting that control animals switched decision-making strategies faster (Figure 8H; repeated measures ANOVA around switch interaction F(5) = 2.61, p = 0.023 and Figure 8I; repeated measures ANOVA around switch interaction F(6) = 2.12, p = 0.048, post hoc on each position bin via two-sided Wilcoxon ranksum corrected for multiple comparisons). While we found significance, the increase in exploration appeared just before rule switches and was very small, suggesting caution in interpretation (Figure 8I). 

To determine if dmPFC inactivation affected rats’ ability to employ procedural strategies, we compared the development of behavioral stereotypy around rule switches. We found that DREADDs animals developed behavioral stereotypy slower and showed overall less stereotypy compared with controls (Figures 8J and S8A), even when their exploration level was the same as controls (Figures 8F and S8A, DCZ) likely due to subtle 

**==> picture [46 x 35] intentionally omitted <==**

(H) zIdPhi aligned to rule switches for DREADDs and control virus animals. The horizontal dashed line indicates the threshold for which events were identified as binary VTE and non-VTE events. The vertical dotted line corresponds to the last lap of the previous rule block. The black line above indicates laps in which there was a significant difference between active and control groups. Data are shown as mean ± SEM. 

(I) Proportion of exploratory laps aligned to rule switches for DREADDs and control animals. Representation as in (H). 

(J) Trajectory stereotypy between pairs of paths through the central maze segment around rule switches for DREADDs and control virus animals. 

(K) Rat performance across the experimental weeks for DREADDs and control animals. Each ‘‘week’’ is an 8-day sequence (Figure S8C). (D and F) Mixed-effects ANOVA, n.s. p > 0.05, **p < 0.01. 

(E and G) Wilcoxon signed-rank test, n.s. p > 0.05, *p < 0.05, **p < 0.01, ***p < 0.001. 

Neuron 112, 4096–4114, December 18, 2024 4107 

Article 

## **ll** 

differences through the central track. This is in line with previous findings that suggest dmPFC disruption causes long-term deficits in habit formation.[113] 

Finally, we evaluated the long-term progression of task performance over the course of our multi-week experiment. Notably, we found that DREADDs animals performed worse throughout the entire experimental sequence (Figure 8K; oneway ANOVA virus F(1) = 9.9, p = 0.071). In considering how rats’ behavioral strategies may have evolved over the course of the experimental timeline, we hypothesized that as rats became more familiar with the general task structure (rule changes and adaptation), deliberation became less critical. In line with this hypothesis, we found that control rats exhibited progressively less exploratory behavior over the course of the 4-week experiment (Figure S8B; mixed-effects ANOVA week F(6) = 3.96, p = 0.0032), though VTE remained stable (Figure S8C; mixed-effects ANOVA week F(6) = 0.7, p = 0.65). By contrast, DREADDs rats did not exhibit this observed decrease in exploration or VTE. 

Collectively, these data suggest that dmPFC inactivation impaired long-term behavioral adaptation and recognition of task regularities. Furthermore, it impaired effective engagement and balancing between deliberative and procedural decision-making systems, thus highlighting the importance of dmPFC in setting strategy. 

## DISCUSSION 

Prior research into decision-making suggests that adaptive decision-making necessitates the interaction between multiple competing decision-making systems, two of which are deliberative (or prospective) and procedural (or habit) systems.[7–9][,][12][,][13][,][114][,][115] However, the environment in which these decision-making processes are taking place is often overlooked. In this study, we examined how behavior, neural representations, and the interactions between HC, DLS, and dorsomedial prefrontal cortex (dmPFC) changed with environmental spatial complexity. The LRA foraging task with changing internal barriers, coupled with simultaneous recordings across dorsal HC, DLS, and dmPFC, allowed us to study the effects of environmental complexity on neural representations and decision-making strategies. 

Past research has emphasized the competition between deliberative and procedural control of behavior and has suggested that they arise based on the animal’s experience and the consistency of the environment.[10][,][13][,][22][,][71][,][116] Deliberative control is favored when the optimal actions remain variable.[8][,][12][,][13][,][21][,][117–120] By contrast, procedural control is favored when the optimal behavior is relatively consistent across time.[8][,][12][,][13][,][33][,][102][,][114][,][121] In line with this idea, decision-making strategy in our task changed from initially deliberative on entry into the environment to procedural as the rats settled into a behavioral flow, but then transitioned back to deliberative around rule switches before becoming automatic again under the procedural system after adaptation to the new rule. Importantly, environmental structure affected this process, slowing behavioral adaptation in complex environments (Figures 3A, 3E, and 3G). 

## Competition between deliberative and procedural 

## decision-making in differently complex environments 

The role of HC is often thought of as providing an adequate model of the environment (or cognitive map) to support future thinking of potential action sequences and their outcomes to aid deliberative decision-making.[8][,][13][,][18][,][21][,][26][,][63][,][66][,][88][,][122][,][123] We found that time-compressed HC nonlocal sequences predominantly occurred during deliberative behaviors such as VTE (Figures 5A and 5B). Importantly, we observed another deliberative behavior, which we identified as exploration, that was also affected by maze complexity and was correlated with the prominence of HC nonlocal sequences, significantly more than VTE, thus further buttressing the role of HC in model-building (Figures 3B–3D, 5A–5D, and S4A–S4D). Furthermore, complex environments featured more theta-timescale nonlocal activity that was longer and more prominent (Figure 4). Together, these data suggest that prolonged deliberation in complex environments may indicate increased cognitive/memory load due to the need to create fine-scale schema of the environment to learn the consistencies therein. 

Prior research has shown that there is a parallel between deliberative decision-making and curiosity, which is often associated with the intrinsic motivation and natural tendency to proactively explore the environment to gather information about its structure.[119][,][124] This structural knowledge can be flexibly used when planning actions in new environments or when reward locations change.[8][,][12][,][25][,][26][,][68][,][90][,][119][,][125] Here, the complexity of the environment, which quantifies the diversity and length of available paths within the central segment of the maze, may be changing the utility of exploration (Figures 3E and S2H–S2J). In low-complexity environments, the ability of the animal to visually observe the high-cost choice point at the end of the central path may be enough for it to infer the structure of the environment, decreasing the overall usefulness of physical exploration. Another possibility is that the diversity of the number of paths increases the perceived state space of the problem, favoring increased physical exploration to organize the mental search and planning occurring over the state space. 

The difference in the strength of relationship between dmPFC prediction of HC state during VTE events and exploration suggests that these two behaviors likely reflect different neural processes. Exploration may be facilitating the encoding of a new model of the environment, which is then retrieved during VTE events. The significant relationship between exploration and dmPFC may be indicative of a role in dmPFC in map-related changes (Figures 7F and 7G). 

Procedural decision-making is often thought to be encoded by DLS bursts aligned to boundaries of well-learned action sequences.[24][,][27][,][33][,][34] Task bracketing and DLS representations of cached action sequences have primarily been studied in simple environments, such as T-mazes. Consistent with previous research,[42][,][72][,][102] we found increased firing at the beginning and end of action sequences in simple mazes (Figures 6A, 6C, S5A, and S5B). In more complex environments, DLS ensemble firings were modulated by the internal structure of the maze. Furthermore, DLS representations of space changed with environmental complexity, from highly similar throughout the 

4108 Neuron 112, 4096–4114, December 18, 2024 

**ll** 

## Article 

navigation sequence in simple environments to local and distinct in complex environments (Figure 6C). 

DLS receives most of its excitatory inputs from sensorimotor cortex and thalamus and can influence movements by modulating motor cortical activity.[126–128] This raises questions as to cognitive vs. motor components in DLS firing patterns. While it is possible that the increased firing and shared representations in the central path in more complex environments may be a byproduct of distinct motor actions, these observations are also consistent with theories that suggest these bursts are indicative of action selection and initiation through the integration of sensorimotor, cognitive, and motivational information. 

Our findings suggest that the potential balance between the deliberative and procedural decision-making systems may not be as distinct in environments that require significant cognitive/ memory load and that striatum may not be encoding classical task-bracketing representations in complex environments aligned to task start and end points. The hypothesis that environmental complexity increases memory load is in line with computational research that suggests that planning and deliberation grow quadratically with the state space.[3] Task bracketing in complex environments may not be the right metric to understand how DLS may be representing the boundaries of cached action sequences. 

## The role of dorsal prefrontal cortex in balancing between decision systems 

The hypothesis that behavior arises from an interaction between multiple algorithms leaves open the critical question about how disagreements between decision-making systems are resolved. Current theories suggest that these are resolved through information processing in the medial prefrontal cortex.[43–49][,][129][,][130] Consistent with this hypothesis, we found that dmPFC ensemble firing patterns changed before either HC or DLS after rule switches (Figures 7A–7C, and that dmPFC activity better predicted HC state after rule switches) (Figures 7D–7G). Prior research has shown that HC and mPFC exhibit oscillatory synchronization at choice points, particularly after rule switches, which is interpreted as information transfer and integration between mPFC and HC.[19][,][131–134] mPFC may be integrating contextual information to balance between deliberative and procedural decision-making by updating the current task rule and inhibiting prepotent responses to enable flexible behaviors. 

In line with previous research that found disruptions in working memory and perseverative errors with dmPFC lesions,[135–137] we found that the inactivation of dmPFC led to acute and long-term behavioral deficits. Consistent with prior research that found neural activity in anterior cingulate cortex shifting between exploration and choice repetition,[138][,][139] we found that dmPFC inactivation caused perseveration of left or right choices after rule changes leading to maladaptive behaviors (Figure 8C). Surprisingly, dmPFC inactivation did not decrease the prevalence of deliberative behaviors but resulted in long-term changes to strategy setting, suggesting instead inadequate learning from deliberative behaviors. Therefore, dmPFC manipulations may be having long-term strategy effects, where continuous inactivation may be leading to global impairments in building context associations that are necessary for 

connecting potentially complex environments with a decision strategy that is appropriate for the degree of behavioral flexibility perceived to be required. 

## RESOURCE AVAILABILITY 

## Lead contact 

Further information and requests for resources should be directed and will be fulfilled by the lead contact, A. David Redish (redish@umn.edu). 

## Materials and availability 

This study did not generate new unique reagents. 

## Data and code availability 

Data and code to generate the figures are publicly available at OSF https://osf. io/c4fjm/. 

## ACKNOWLEDGMENTS 

We thank G. Cannan, T. Lawrence, and J. Williams for help with experiments as well as C. Boldt, K. Seeland, and A. Sheehan for technical assistance. We thank E. Krook-Magnusson, C.J. Walters, and members of the Redish lab for comments and useful discussions. This work was supported by NIH grants R01-MH112688 and R01-MH080318. 

## AUTHOR CONTRIBUTIONS 

U.M., S.L.H., and A.D.R. designed the study. U.M. collected the recording data, and S.L.H. collected the DREADD manipulation data. U.M. analyzed the recording and S.L.H. and U.M. analyzed the DREADD manipulation data. U.M. and A.D.R. wrote the manuscript. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

d EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS B Subjects d METHOD DETAILS B Surgical procedures B Left/Right/Alternation Task B Initial task training B Experimental sequence B Recordings B DREADD validation B Histology B Data Analysis B Quantification of maze complexity B Behavior B Behavioral change point B Running speed B Vicarious trial and error (VTE) B Exploration B Behavioral trajectory stereotypy B Maze linearization B Place field analysis B Hippocampal Theta cycle identification B Bayesian decoding and sequence analysis B Correlation between theta metrics and behavior B Linearized firing rate by lap 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 112, 4096–4114, December 18, 2024 4109 

Article 

## **ll** 

B Task-bracketing index 

   - B Spatial cross correlation of ensemble activity 

   - B Stepwise regression between DLS firing and behavior 

   - B Population correlation of ensemble activity 

   - B Ensemble population activity change point 

   - B mPFC activity prediction of theta score 

   - B Correlation between mPFC prediction of theta score and behavior 

   - B Lap peri-event time histograms of mPFC activity 

- d QUANTIFICATION AND STATISTICAL ANALYSIS B Statistical analysis 

## SUPPLEMENTAL INFORMATION 

Supplemental information can be found online at https://doi.org/10.1016/j. neuron.2024.10.004. 

Received: April 4, 2024 Revised: August 12, 2024 Accepted: October 3, 2024 Published: October 29, 2024 

## REFERENCES 

1. Coutrot, A., Manley, E., Goodroe, S., Gahnstrom, C., Filomena, G., Yesiltepe, D., Dalton, R.C., Wiener, J.M., Ho¨ lscher, C., Hornberger, M., et al. (2022). Entropy of city street networks linked to future spatial navigation ability. Nature 604, 104–110. https://doi.org/10.1038/s41586022-04486-7. 

2. Shettleworth, S.J. (2010). Cognition, Evolution, and Behavior, Second Edition (Oxford University Press). 

3. Hunt, L.T., Daw, N.D., Kaanders, P., MacIver, M.A., Mugan, U., Procyk, E., Redish, A.D., Russo, E., Scholl, J., Stachenfeld, K., et al. (2021). Formalizing planning and information search in naturalistic decisionmaking. Nat. Neurosci. 24, 1051–1064. 

4. Bennett, E.L., Diamond, M.C., Krech, D., and Rosenzweig, M.R. (1964). Chemical and Anatomical Plasticity Brain. Science 146, 610–619. https://doi.org/10.1126/science.146.3644.610. 

5. Kempermann, G. (2019). Environmental enrichment, new neurons and the neurobiology of individuality. Nat. Rev. Neurosci. 20, 235–245. https://doi.org/10.1038/s41583-019-0120-x. 

6. Zocher, S., Schilling, S., Grzyb, A.N., Adusumilli, V.S., Bogado Lopes, J., Gunther, S., Overall, R.W., Winter, Y., and Kempermann, G. (2020). Early-€ life environmental enrichment generates persistent individualized behavior in mice. Sci. Adv. 6, eabb1478. https://doi.org/10.1126/ sciadv.abb1478. 

7. Balleine, B.W., and Dickinson, A. (1998). Goal-directed instrumental action: contingency and incentive learning and their cortical substrates. Neuropharmacology 37, 407–419. https://doi.org/10.1016/s0028-3908 (98)00033-1. 

8. O’Keefe, J., and Nadel, L. (1978). The Hippocampus as a Cognitive Map (Oxford University Press). 

9. Daw, N.D., Niv, Y., and Dayan, P. (2005). Uncertainty-based competition between prefrontal and dorsolateral striatal systems for behavioral control. Nat. Neurosci. 8, 1704–1711. https://doi.org/10.1038/nn1560. 

10. Dezfouli, A., and Balleine, B.W. (2013). Actions, action sequences and habits: evidence that goal-directed and habitual action control are hierarchically organized. PLoS Comput. Biol. 9, e1003364. https://doi.org/10. 1371/journal.pcbi.1003364. 

11. Balleine, B.W., Doya, K., O’Doherty, J., and Sakagami, M. (2007). Current trends in decision making. Ann. N. Y. Acad. Sci. 1104. xi–xv. https://doi. org/10.1196/annals.1390.2226. 

12. Redish, A.D. (1999). Beyond the Cognitive Map: from Place Cells to Episodic Memory (MIT Press). 

13. Redish, A.D. (2013). The Mind within the Brain: How We Make Decisions and How Those Decisions Go Wrong (Oxford University Press). 

14. van der Meer, M., Kurth-Nelson, Z., and Redish, A.D. (2012). Information processing in decision-making systems. Neuroscientist 18, 342–359. https://doi.org/10.1177/1073858411435128. 

15. Samborska, V., Butler, J.L., Walton, M.E., Behrens, T.E.J., and Akam, T. (2022). Complementary task representations in hippocampus and prefrontal cortex for generalizing the structure of problems. Nat. Neurosci. 25, 1314–1326. https://doi.org/10.1038/s41593-022-01149-8. 

16. MacIver, M.A., Schmitz, L., Mugan, U., Murphey, T.D., and Mobley, C.D. (2017). Massive increase in visual range preceded the origin of terrestrial vertebrates. Proc. Natl. Acad. Sci. USA 114, E2375–E2384. https://doi. org/10.1073/pnas.1615563114. 

17. Mugan, U., and MacIver, M.A. (2020). Spatial planning with long visual range benefits escape from visual predators in complex naturalistic environments. Nat. Commun. 11, 3057. https://doi.org/10.1038/s41467-02016102-1. 

18. Johnson, A., and Redish, A.D. (2007). Neural ensembles in CA3 transiently encode paths forward of the animal at a decision point. J. Neurosci. 27, 12176–12189. https://doi.org/10.1523/JNEUROSCI. 3761-07.2007. 

19. Ito, H.T., Zhang, S.-J., Witter, M.P., Moser, E.I., and Moser, M.-B. (2015). A prefrontal–thalamo–hippocampal circuit for goal-directed spatial navigation. Nature 522, 50–55. 

20. Pastalkova, E., Itskov, V., Amarasingham, A., and Buzsa´ ki, G. (2008). Internally generated cell assembly sequences in the rat hippocampus. Science 321, 1322–1327. https://doi.org/10.1126/science.1159775. 

21. Redish, A.D. (2016). Vicarious trial and error. Nat. Rev. Neurosci. 17, 147–159. https://doi.org/10.1038/nrn.2015.30. 

22. Balleine, B.W., and O’Doherty, J.P. (2010). Human and rodent homologies in action control: corticostriatal determinants of goal-directed and habitual action. Neuropsychopharmacology 35, 48–69. https://doi. org/10.1038/npp.2009.131. 

23. Graybiel, A.M. (2008). Habits, rituals, and the evaluative brain. Annu. Rev. Neurosci. 31, 359–387. https://doi.org/10.1146/annurev.neuro.29. 051605.112851. 

24. Balleine, B.W., Delgado, M.R., and Hikosaka, O. (2007). The role of the dorsal striatum in reward and decision-making. J. Neurosci. 27, 8161– 8165. https://doi.org/10.1523/JNEUROSCI.1554-07.2007. 

25. Gupta, A.S., van der Meer, M.A.A., Touretzky, D.S., and Redish, A.D. (2010). Hippocampal replay is not a simple function of experience. Neuron 65, 695–705. https://doi.org/10.1016/j.neuron.2010.01.034. 

26. Pfeiffer, B.E., and Foster, D.J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. Nature 497, 74–79. https://doi. org/10.1038/nature12112. 

27. Jog, M.S., Kubota, Y., Connolly, C.I., Hillegaart, V., and Graybiel, A.M. (1999). Building neural representations of habits. Science 286, 1745– 1749. https://doi.org/10.1126/science.286.5445.1745. 

28. Yin, H.H., Knowlton, B.J., and Balleine, B.W. (2006). Inactivation of dorsolateral striatum enhances sensitivity to changes in the actionoutcome contingency in instrumental conditioning. Behav. Brain Res. 166, 189–196. https://doi.org/10.1016/j.bbr.2005.07.012. 

29. Eichenbaum, H. (1993). Memory, Amnesia, and the Hippocampal System (MIT Press). 

30. Knierim, J.J., Kudrimoti, H.S., and McNaughton, B.L. (1995). Place cells, head direction cells, and the learning of landmark stability. J. Neurosci. 15, 1648–1659. https://doi.org/10.1523/JNEUROSCI.15-03-01648.1995. 

31. Lee, J.Q., LeDuke, D.O., Chua, K., McDonald, R.J., and Sutherland, R.J. (2018). Relocating cued goals induces population remapping in CA1 related to memory performance in a two-platform water task in rats. Hippocampus 28, 431–440. https://doi.org/10.1002/hipo.22843. 

32. Bradfield, L.A., Leung, B.K., Boldt, S., Liang, S., and Balleine, B.W. (2020). Goal-directed actions transiently depend on dorsal 

4110 Neuron 112, 4096–4114, December 18, 2024 

## Article 

   - hippocampus. Nat. Neurosci. 23, 1194–1197. https://doi.org/10.1038/ s41593-020-0693-8. 

33. Barnes, T.D., Kubota, Y., Hu, D., Jin, D.Z., and Graybiel, A.M. (2005). Activity of striatal neurons reflects dynamic encoding and recoding of procedural memories. Nature 437, 1158–1161. https://doi.org/10.1038/ nature04053. 

34. Graybiel, A.M. (1998). The basal ganglia and chunking of action repertoires. Neurobiol. Learn. Mem. 70, 119–136. https://doi.org/10.1006/ nlme.1998.3843. 

35. Smith, K.S., and Graybiel, A.M. (2013). A dual operator view of habitual behavior reflecting cortical and striatal dynamics. Neuron 79, 361–374. https://doi.org/10.1016/j.neuron.2013.05.038. 

36. Thorn, C.A., Atallah, H., Howe, M., and Graybiel, A.M. (2010). Differential dynamics of activity changes in dorsolateral and dorsomedial striatal loops during learning. Neuron 66, 781–795. https://doi.org/10.1016/j. neuron.2010.04.036. 

37. Jin, X., and Costa, R.M. (2010). Start/stop signals emerge in nigrostriatal circuits during sequence learning. Nature 466, 457–462. 

38. Jin, X., Tecuapetla, F., and Costa, R.M. (2014). Basal ganglia subcircuits distinctively encode the parsing and concatenation of action sequences. Nat. Neurosci. 17, 423–430. https://doi.org/10.1038/nn.3632. 

39. Yin, H.H., and Knowlton, B.J. (2006). The role of the basal ganglia in habit formation. Nat. Rev. Neurosci. 7, 464–476. https://doi.org/10.1038/ nrn1919. 

40. Schmitzer-Torbert, N.C., and Redish, A.D. (2008). Task-dependent encoding of space and events by striatal neurons is dependent on neural subtype. Neuroscience 153, 349–360. https://doi.org/10.1016/j.neuroscience.2008.01.081. 

41. Gahnstrom, C.J., and Spiers, H.J. (2020). Striatal and hippocampal contributions to flexible navigation in rats and humans. Brain Neurosci. Adv. 4, 2398212820979772. https://doi.org/10.1177/2398212820979772. 

42. Regier, P.S., Amemiya, S., and Redish, A.D. (2015). Hippocampus and subregions of the dorsal striatum respond differently to a behavioral strategy change on a spatial navigation task. J. Neurophysiol. 114, 1399–1416. https://doi.org/10.1152/jn.00189.2015. 

43. Powell, N.J., and Redish, A.D. (2016). Representational changes of latent strategies in rat medial prefrontal cortex precede changes in behaviour. Nat. Commun. 7, 12830. https://doi.org/10.1038/ncomms12830. 

44. Hasz, B.M., and Redish, A.D. (2020). Dorsomedial prefrontal cortex and hippocampus represent strategic context even while simultaneously changing representation throughout a task session. Neurobiol. Learn. Mem. 171, 107215. https://doi.org/10.1016/j.nlm.2020.107215. 

45. Durstewitz, D., Vittoz, N.M., Floresco, S.B., and Seamans, J.K. (2010). Abrupt transitions between prefrontal neural ensemble states accompany behavioral transitions during rule learning. Neuron 66, 438–448. https://doi.org/10.1016/j.neuron.2010.03.029. 

46. Euston, D.R., Gruber, A.J., and McNaughton, B.L. (2012). The role of medial prefrontal cortex in memory and decision making. Neuron 76, 1057–1070. https://doi.org/10.1016/j.neuron.2012.12.002. 

47. McLaughlin, A.E., Diehl, G.W., and Redish, A.D. (2021). Potential roles of the rodent medial prefrontal cortex in conflict resolution between multiple decision-making systems. Int. Rev. Neurobiol. 158, 249–281. https://doi. org/10.1016/bs.irn.2020.11.009. 

48. Wirt, R.A., and Hyman, J.M. (2017). Integrating Spatial Working Memory and Remote Memory: Interactions between the Medial Prefrontal Cortex and Hippocampus. Brain Sci. 7, 43. https://doi.org/ 10.3390/brainsci7040043. 

49. Kidder, K., Gillis, R., Miles, J., and Mizumori, S.J.Y. (2024). The medial prefrontal cortex during flexible decisions: Evidence for its role in distinct working memory processes. Hippocampus 34, 141–155. https://doi.org/ 10.1002/hipo.23594. 

## **ll** 

50. Hasz, B.M., and Redish, A.D. (2020). Spatial encoding in dorsomedial prefrontal cortex and hippocampus is related during deliberation. Hippocampus 30, 1194–1208. https://doi.org/10.1002/hipo.23250. 

51. O’Keefe, J., and Dostrovsky, J. (1971). The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res. 34, 171–175. https://doi.org/10.1016/0006-8993(71)90358-1. 

52. Morris, R.G.M., Garrud, P., Rawlins, J.N.P., and O’Keefe, J. (1982). Place navigation impaired in rats with hippocampal lesions. Nature 297, 681–683. https://doi.org/10.1038/297681a0. 

53. Fortin, N.J., Agster, K.L., and Eichenbaum, H.B. (2002). Critical role of the hippocampus in memory for sequences of events. Nat. Neurosci. 5, 458–462. https://doi.org/10.1038/nn834. 

54. Behrens, T.E.J., Muller, T.H., Whittington, J.C.R., Mark, S., Baram, A.B., Stachenfeld, K.L., and Kurth-Nelson, Z. (2018). What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior. Neuron 100, 490–509. https://doi.org/10.1016/j.neuron.2018.10.002. 

55. Aronov, D., Nevers, R., and Tank, D.W. (2017). Mapping of a non-spatial dimension by the hippocampal-entorhinal circuit. Nature 543, 719–722. https://doi.org/10.1038/nature21692. 

56. Cohen, N.J., and Eichenbaum, H. (1993). Memory, Amnesia, and the Hippocampal System (MIT Press). 

57. Leutgeb, S., Leutgeb, J.K., Barnes, C.A., Moser, E.I., McNaughton, B.L., and Moser, M.B. (2005). Independent codes for spatial and episodic memory in hippocampal neuronal ensembles. Science 309, 619–623. https://doi.org/10.1126/science.1114037. 

58. Lever, C., Wills, T., Cacucci, F., Burgess, N., and O’Keefe, J. (2002). Long-term plasticity in hippocampal place-cell representation of environmental geometry. Nature 416, 90–94. https://doi.org/10.1038/416090a. 

59. Jeffery, K.J., and Anderson, M.I. (2003). Dissociation of the geometric and contextual influences on place cells. Hippocampus 13, 868–872. https://doi.org/10.1002/hipo.10162. 

60. Fenton, A.A., Kao, H.Y., Neymotin, S.A., Olypher, A., Vayntrub, Y., Lytton, W.W., and Ludvig, N. (2008). Unmasking the CA1 ensemble place code by exposures to small and large environments: more place cells and multiple, irregularly arranged, and expanded place fields in the larger space. J. Neurosci. 28, 11250–11262. https://doi.org/10.1523/JNEUROSCI. 2862-08.2008. 

61. Duvelle, E[´ ] ., Grieves, R.M., Liu, A., Jedidi-Ayoub, S., Holeniewska, J., Harris, A., Nyberg, N., Donnarumma, F., Lefort, J.M., Jeffery, K.J., et al. (2021). Hippocampal place cells encode global location but not connectivity in a complex space. Curr. Biol. 31, 1221–1233.e9. https:// doi.org/10.1016/j.cub.2021.01.005. 

62. Kay, K., Chung, J.E., Sosa, M., Schor, J.S., Karlsson, M.P., Larkin, M.C., Liu, D.F., and Frank, L.M. (2020). Constant Sub-second Cycling between Representations of Possible Futures in the Hippocampus. Cell 180, 552– 567.e25. https://doi.org/10.1016/j.cell.2020.01.014. 

63. Foster, D.J., and Wilson, M.A. (2007). Hippocampal theta sequences. Hippocampus 17, 1093–1099. https://doi.org/10.1002/hipo.20345. 

64. Lisman, J., and Redish, A.D. (2009). Prediction, sequences and the hippocampus. Philos. Trans. R. Soc. Lond. B Biol. Sci. 364, 1193–1201. 

65. Dragoi, G., and Buzsa´ ki, G. (2006). Temporal encoding of place sequences by hippocampal cell assemblies. Neuron 50, 145–157. https:// doi.org/10.1016/j.neuron.2006.02.023. 

66. Gupta, A.S., van der Meer, M.A.A., Touretzky, D.S., and Redish, A.D. (2012). Segmentation of spatial experience by hippocampal q sequences. Nat. Neurosci. 15, 1032–1039. https://doi.org/10.1038/nn.3138. 

67. Ambrose, R.E., Pfeiffer, B.E., and Foster, D.J. (2016). Reverse Replay of Hippocampal Place Cells Is Uniquely Modulated by Changing Reward. Neuron 91, 1124–1136. https://doi.org/10.1016/j.neuron.2016.07.047. 

68. Wu, X., and Foster, D.J. (2014). Hippocampal replay captures the unique topological structure of a novel environment. J. Neurosci. 34, 6459–6469. https://doi.org/10.1523/JNEUROSCI.3414-13.2014. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 112, 4096–4114, December 18, 2024 4111 

Article 

## **ll** 

69. Buzsa´ ki, G. (2002). Theta oscillations in the hippocampus. Neuron 33, 325–340. https://doi.org/10.1016/s0896-6273(02)00586-x. 

70. Zheng, C., Hwaun, E., Loza, C.A., and Colgin, L.L. (2021). Hippocampal place cell sequences differ during correct and error trials in a spatial memory task. Nat. Commun. 12, 3373. https://doi.org/10.1038/ s41467-021-23765-x. 

71. Dezfouli, A., Lingawi, N.W., and Balleine, B.W. (2014). Habits as action sequences: hierarchical action control and changes in outcome value. Phil. Trans. R. Soc. B 369, 20130482. https://doi.org/10.1098/rstb. 2013.0482. 

72. Cunningham, P.J., Regier, P.S., and Redish, A.D. (2021). Dorsolateral Striatal Task-initiation Bursts Represent Past Experiences More than Future Action Plans. J. Neurosci. 41, 8051–8064. https://doi.org/10. 1523/JNEUROSCI.3080-20.2021. 

73. Amemiya, S., and Redish, A.D. (2018). Hippocampal Theta-Gamma Coupling Reflects State-Dependent Information Processing in Decision Making. Cell Rep. 22, 3328–3338. https://doi.org/10.1016/j.celrep. 2018.02.091. 

74. Amemiya, S., and Redish, A.D. (2016). Manipulating Decisiveness in Decision Making: Effects of Clonidine on Hippocampal Search Strategies. J. Neurosci. 36, 814–827. https://doi.org/10.1523/JNEUROSCI.259515.2016. 

75. Powell, N.J., and Redish, A.D. (2014). Complex neural codes in rat prelimbic cortex are stable across days on a spatial decision task. Front. Behav. Neurosci. 8, 120. https://doi.org/10.3389/fnbeh.2014.00120. 

76. Steiner, A.P., and Redish, A.D. (2012). The road not taken: neural correlates of decision making in orbitofrontal cortex. Front. Neurosci. 6, 131. https://doi.org/10.3389/fnins.2012.00131. 

77. van der Meer, M.A.A., Johnson, A., Schmitzer-Torbert, N.C., and Redish, A.D. (2010). Triple dissociation of information processing in dorsal striatum, ventral striatum, and hippocampus on a learned spatial decision task. Neuron 67, 25–32. https://doi.org/10.1016/j.neuron.2010.06.023. 

78. Blumenthal, A., Steiner, A., Seeland, K., and Redish, A.D. (2011). Effects of pharmacological manipulations of NMDA-receptors on deliberation in the Multiple-T task. Neurobiol. Learn. Mem. 95, 376–384. https://doi.org/ 10.1016/j.nlm.2011.01.011. 

79. Schmitzer-Torbert, N., and Redish, A.D. (2004). Neuronal activity in the rodent dorsal striatum in sequential navigation: separation of spatial and reward responses on the multiple T task. J. Neurophysiol. 91, 2259–2272. https://doi.org/10.1152/jn.00687.2003. 

80. Schmitzer-Torbert, N., and Redish, A.D. (2002). Development of path stereotypy in a single day in rats on a multiple-T maze. Arch. Ital. Biol. 140, 295–301. 

81. Papale, A.E., Stott, J.J., Powell, N.J., Regier, P.S., and Redish, A.D. (2012). Interactions between deliberation and delay-discounting in rats. Cogn. Affect. Behav. Neurosci. 12, 513–526. https://doi.org/10.3758/ s13415-012-0097-7. 

82. George, A.E., Stout, J.J., and Griffin, A.L. (2023). Pausing and reorienting behaviors enhance the performance of a spatial working memory task. Behav. Brain Res. 446, 114410. https://doi.org/10.1016/j.bbr.2023. 114410. 

83. Mugan, U., Amemiya, S., Regier, P.S., and Redish, A.D. (2023). Navigation through the complex world—the neurophysiology of decision-making processes. Preprint at arXiv. https://doi.org/10.48550/ arXiv.2306.03162. 

84. Trucco, E. (1956). A note on the information content of graphs. Bull. Math. Biophys. 18, 129–135. 

85. Newman, M.E.J., Baraba´ si, A.-L.s., and Watts, D.J. (2006). The Structure and Dynamics of Networks (Princeton University Press). 

86. Dehmer, M., and Mowshowitz, A. (2011). A history of graph entropy measures. Inf. Sci. 181, 57–78. 

87. Bonchev, D.G. (2009). Information Theoretic Complexity Measures. In Encyclopedia of Complexity and Systems Science, 5 (Springer), pp. 4820–4838. 

88. Wikenheiser, A.M., and Redish, A.D. (2015). Hippocampal theta sequences reflect current goals. Nat. Neurosci. 18, 289–294. https://doi. org/10.1038/nn.3909. 

89. Buzsa´ ki, G. (2015). Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. Hippocampus 25, 1073– 1188. https://doi.org/10.1002/hipo.22488. 

90. Widloski, J., and Foster, D.J. (2022). Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping. Neuron 110, 1547–1558.e8. https://doi.org/10. 1016/j.neuron.2022.02.002. 

91. O[´ ] lafsdo´ ttir, H.F., Barry, C., Saleem, A.B., Hassabis, D., and Spiers, H.J. (2015). Hippocampal place cells construct reward related sequences through unexplored space. eLife 4, e06063. https://doi.org/10.7554/ eLife.06063. 

92. Zielinski, M.C., Shin, J.D., and Jadhav, S.P. (2019). Coherent Coding of Spatial Position Mediated by Theta Oscillations in the Hippocampus and Prefrontal Cortex. J. Neurosci. 39, 4550–4565. https://doi.org/10. 1523/JNEUROSCI.0106-19.2019. 

93. Mizuseki, K., Sirota, A., Pastalkova, E., and Buzsa´ ki, G. (2009). Theta oscillations provide temporal windows for local circuit computation in the entorhinal-hippocampal loop. Neuron 64, 267–280. https://doi.org/10. 1016/j.neuron.2009.08.037. 

94. Maurer, A.P., Cowen, S.L., Burke, S.N., Barnes, C.A., and McNaughton, B.L. (2006). Organization of hippocampal cell assemblies based on theta phase precession. Hippocampus 16, 785–794. https://doi.org/10.1002/ hipo.20202. 

95. Maurer, A.P., and McNaughton, B.L. (2007). Network and intrinsic cellular mechanisms underlying theta phase precession of hippocampal neurons. Trends Neurosci. 30, 325–333. https://doi.org/10.1016/j.tins. 2007.05.002. 

96. Skaggs, W.E., McNaughton, B.L., Wilson, M.A., and Barnes, C.A. (1996). Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. Hippocampus 6, 149–172. https://doi.org/10.1002/(SICI)1098-1063(1996)6:2<149::AID-HIPO6>3.0. CO;2-K. 

97. O’Keefe, J., and Recce, M.L. (1993). Phase relationship between hippocampal place units and the EEG theta rhythm. Hippocampus 3, 317–330. https://doi.org/10.1002/hipo.450030307. 

98. Zhang, K., Ginzburg, I., McNaughton, B.L., and Sejnowski, T.J. (1998). Interpreting neuronal population activity by reconstruction: unified framework with application to hippocampal place cells. J. Neurophysiol. 79, 1017–1044. https://doi.org/10.1152/jn.1998.79.2.1017. 

99. Farooq, U., and Dragoi, G. (2019). Emergence of preconfigured and plastic time-compressed sequences in early postnatal development. Science 363, 168–173. https://doi.org/10.1126/science.aav0502. 

100. Feng, T., Silva, D., and Foster, D.J. (2015). Dissociation between the experience-dependent development of hippocampal theta sequences and single-trial phase precession. J. Neurosci. 35, 4890–4902. https:// doi.org/10.1523/JNEUROSCI.2614-14.2015. 

101. Drieu, C., Todorova, R., and Zugaro, M. (2018). Nested sequences of hippocampal assemblies during behavior support subsequent sleep replay. Science 362, 675–679. https://doi.org/10.1126/science.aat2952. 

102. Smith, K.S., and Graybiel, A.M. (2016). Habit formation coincides with shifts in reinforcement representations in the sensorimotor striatum. J. Neurophysiol. 115, 1487–1498. https://doi.org/10.1152/jn.00925.2015. 

103. Hok, V., Save, E., Lenck-Santini, P.P., and Poucet, B. (2005). Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex. Proc. Natl. Acad. Sci. USA 102, 4602–4607. https://doi.org/10.1073/ pnas.0407332102. 

4112 Neuron 112, 4096–4114, December 18, 2024 

## Article 

104. Botvinick, M.M. (2008). Hierarchical models of behavior and prefrontal function. Trends Cogn. Sci. 12, 201–208. https://doi.org/10.1016/j.tics. 2008.02.009. 

105. Belluscio, M.A., Mizuseki, K., Schmidt, R., Kempter, R., and Buzsa´ ki, G. (2012). Cross-frequency phase-phase coupling between theta and gamma oscillations in the hippocampus. J. Neurosci. 32, 423–435. https://doi.org/10.1523/JNEUROSCI.4122-11.2012. 

106. Zielinski, M.C., Tang, W., and Jadhav, S.P. (2020). The role of replay and theta sequences in mediating hippocampal-prefrontal interactions for memory and cognition. Hippocampus 30, 60–72. https://doi.org/10. 1002/hipo.22821. 

107. Gallistel, C.R., Fairhurst, S., and Balsam, P. (2004). The learning curve: implications of a quantitative analysis. Proc. Natl. Acad. Sci. USA 101, 13124–13131. https://doi.org/10.1073/pnas.0404965101. 

108. Hayden, B.Y., Heilbronner, S.R., Pearson, J.M., and Platt, M.L. (2011). Surprise signals in anterior cingulate cortex: neuronal encoding of unsigned reward prediction errors driving adjustment in behavior. J. Neurosci. 31, 4178–4187. https://doi.org/10.1523/JNEUROSCI. 4652-10.2011. 

109. Cole, N., Harvey, M., Myers-Joseph, D., Gilra, A., and Khan, A.G. (2024). Prediction error signals in anterior cingulate cortex drive task-switching. Nat. Commun. 15, 7088. 

110. Laubach, M., Amarante, L.M., Caetano, M.S., and Horst, N.K. (2021). Reward signaling by the rodent medial frontal cortex. Int. Rev. Neurobiol. 158, 115–133. https://doi.org/10.1016/bs.irn.2020.11.012. 

111. Roth, B.L. (2016). DREADDs for neuroscientists. Neuron 89, 683–694. 112. Nagai, Y., Miyakawa, N., Takuwa, H., Hori, Y., Oyama, K., Ji, B., Takahashi, M., Huang, X.P., Slocum, S.T., DiBerto, J.F., et al. (2020). Deschloroclozapine, a potent and selective chemogenetic actuator enables rapid neuronal and behavioral modulations in mice and monkeys. Nat. Neurosci. 23, 1157–1167. https://doi.org/10.1038/s41593-0200661-3. 

113. McLaughlin, A.E., and Redish, A.D. (2023). Optogenetic disruption of the prelimbic cortex alters long-term decision strategy but not valuation on a spatial delay discounting task. Neurobiol. Learn. Mem. 200, 107734. https://doi.org/10.1016/j.nlm.2023.107734. 

114. Hull, C.L. (1943). Principles of Behavior: an Introduction to Behavior Theory (Appleton-Century-Crofts). 

115. Botvinick, M.M., Niv, Y., and Barto, A.G. (2009). Hierarchically organized behavior and its neural foundations: a reinforcement learning perspective. Cognition 113, 262–280. https://doi.org/10.1016/j.cognition.2008. 08.011. 

116. Niv, Y. (2009). Reinforcement learning in the brain. J. Math. Psychol. 53, 139–154. https://doi.org/10.1016/j.jmp.2008.12.005. 

117. Averbeck, B., and O’Doherty, J.P. (2022). Reinforcement-learning in fronto-striatal circuits. Neuropsychopharmacology 47, 147–162. 

118. Buckner, R.L., and Carroll, D.C. (2007). Self-projection and the brain. Trends Cogn. Sci. 11, 49–57. https://doi.org/10.1016/j.tics.2006.11.004. 

119. Tolman, E.C. (1948). Cognitive maps in rats and men. Psychol. Rev. 55, 189–208. https://doi.org/10.1037/h0061626. 

120. Gardner, R.S., Uttaro, M.R., Fleming, S.E., Suarez, D.F., Ascoli, G.A., and Dumas, T.C. (2013). A secondary working memory challenge preserves primary place strategies despite overtraining. Learn. Mem. 20, 648–656. https://doi.org/10.1101/lm.031336.113. 

121. Packard, M.G., and McGaugh, J.L. (1996). Inactivation of hippocampus or caudate nucleus with lidocaine differentially affects expression of place and response learning. Neurobiol. Learn. Mem. 65, 65–72. https://doi.org/10.1006/nlme.1996.0007. 

122. Wikenheiser, A.M., and Redish, A.D. (2015). Decoding the cognitive map: ensemble hippocampal sequences and decision making. Curr. Opin. Neurobiol. 32, 8–15. https://doi.org/10.1016/j.conb.2014.10.002. 

## **ll** 

123. Miller, K.J., Botvinick, M.M., and Brody, C.D. (2017). Dorsal hippocampus contributes to model-based planning. Nat. Neurosci. 20, 1269– 1276. https://doi.org/10.1038/nn.4613. 

124. Gottlieb, J., and Oudeyer, P.Y. (2018). Towards a neuroscience of active sampling and curiosity. Nat. Rev. Neurosci. 19, 758–770. https://doi.org/ 10.1038/s41583-018-0078-0. 

125. Ormond, J., and O’Keefe, J. (2022). Hippocampal place cells have goaloriented vector fields during navigation. Nature 607, 741–746. https:// doi.org/10.1038/s41586-022-04913-9. 

126. Hunnicutt, B.J., Jongbloets, B.C., Birdsong, W.T., Gertz, K.J., Zhong, H., and Mao, T. (2016). A comprehensive excitatory input map of the striatum reveals novel functional organization. eLife 5, e19103. https://doi.org/10. 7554/eLife.19103. 

127. Wolff, S.B.E., Ko, R., and O[¨ ] lveczky, B.P. (2022). Distinct roles for motor cortical and thalamic inputs to striatum during motor skill learning and execution. Sci. Adv. 8, eabk0231. https://doi.org/10.1126/sciadv. abk0231. 

128. Alexander, G.E., DeLong, M.R., and Strick, P.L. (1986). Parallel organization of functionally segregated circuits linking basal ganglia and cortex. Annu. Rev. Neurosci. 9, 357–381. https://doi.org/10.1146/annurev.ne. 09.030186.002041. 

129. Tang, W., and Jadhav, S.P. (2022). Multiple-Timescale Representations of Space: Linking Memory to Navigation. Annu. Rev. Neurosci. 45, 1–21. https://doi.org/10.1146/annurev-neuro-111020-084824. 

130. Diehl, G.W., and Redish, A.D. (2023). Differential processing of decision information in subregions of rodent medial prefrontal cortex. eLife 12, e82833. 

131. Benchenane, K., Peyrache, A., Khamassi, M., Tierney, P.L., Gioanni, Y., Battaglia, F.P., and Wiener, S.I. (2010). Coherent theta oscillations and reorganization of spike timing in the hippocampal- prefrontal network upon learning. Neuron 66, 921–936. https://doi.org/10.1016/j.neuron. 2010.05.013. 

132. Colgin, L.L. (2011). Oscillations and hippocampal-prefrontal synchrony. Curr. Opin. Neurobiol. 21, 467–474. https://doi.org/10.1016/j.conb. 2011.04.006. 

133. Spellman, T., Rigotti, M., Ahmari, S.E., Fusi, S., Gogos, J.A., and Gordon, J.A. (2015). Hippocampal-prefrontal input supports spatial encoding in working memory. Nature 522, 309–314. https://doi.org/10.1038/ nature14445. 

134. Stout, J.J., Hallock, H.L., George, A.E., Adiraju, S.S., and Griffin, A.L. (2022). The ventral midline thalamus coordinates prefrontal-hippocampal neural synchrony during vicarious trial and error. Sci. Rep. 12, 10940. https://doi.org/10.1038/s41598-022-14707-8. 

135. Rich, E.L., and Shapiro, M. (2009). Rat prefrontal cortical neurons selectively code strategy switches. J. Neurosci. 29, 7208–7219. 

136. Rich, E.L., and Shapiro, M.L. (2007). Prelimbic/infralimbic inactivation impairs memory for multiple task switches, but not flexible selection of familiar tasks. J. Neurosci. 27, 4747–4755. https://doi.org/10.1523/ JNEUROSCI.0369-07.2007. 

137. Guise, K.G., and Shapiro, M.L. (2017). Medial Prefrontal Cortex Reduces Memory Interference by Modifying Hippocampal Encoding. Neuron 94, 183–192.e8. https://doi.org/10.1016/j.neuron.2017.03.011. 

138. Boorman, E.D., Behrens, T.E.J., Woolrich, M.W., and Rushworth, M.F.S. (2009). How green is the grass on the other side? Frontopolar cortex and the evidence in favor of alternative courses of action. Neuron 62, 733–743. https://doi.org/10.1016/j.neuron.2009.05.014. 

139. Procyk, E., Tanaka, Y.L., and Joseph, J.P. (2000). Anterior cingulate activity during routine and non-routine sequential behaviors in macaques. Nat. Neurosci. 3, 502–508. https://doi.org/10.1038/74880. 

140. Pachitariu, M., Sridhar, S., and Stringer, C. (2023). Solving the spike sorting problem with Kilosort. Preprint at bioRxiv. https://doi.org/10.1101/ 2023.01.07.523036. 

**==> picture [46 x 35] intentionally omitted <==**

Neuron 112, 4096–4114, December 18, 2024 4113 

Article 

## **ll** 

141. Rossant, C., Kadir, S., Goodman, D., Hunter, M., and Kenneth, H. (2016). Phy. Version 1.0.9. https://github.com/cortex-lab/phy. 

142. Chung, J., Sharif, F., Jung, D., Kim, S., and Royer, S. (2017). Micro-drive and headgear for chronic implant and recovery of optoelectronic probes. Sci. Rep. 7, 2773. https://doi.org/10.1038/s41598-017-03340-5. 

143. Janabi-Sharifi, F., and Marey, M. (2010). A kalman-filter-based method for pose estimation in visual servoing. IEEE Trans. Robot. 26, 939–947. 

144. Lubenov, E.V., and Siapas, A.G. (2009). Hippocampal theta oscillations are travelling waves. Nature 459, 534–539. https://doi.org/10.1038/ nature08010. 

145. Cole, S., and Voytek, B. (2019). Cycle-by-cycle analysis of neural oscillations. J. Neurophysiol. 122, 849–861. https://doi.org/10.1152/jn. 00273.2019. 

146. Schmidt, B., Duin, A.A., and Redish, A.D. (2019). Disrupting the medial prefrontal cortex alters hippocampal sequences during deliberative decision making. J. Neurophysiol. 121, 1981–2000. https://doi.org/10.1152/ jn.00793.2018. 

147. Davidson, T.J., Kloosterman, F., and Wilson, M.A. (2009). Hippocampal replay of extended experience. Neuron 63, 497–507. https://doi.org/10. 1016/j.neuron.2009.07.027. 

4114 Neuron 112, 4096–4114, December 18, 2024 

**ll** 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE|SOURCE|SOURCE|IDENTIFIER|IDENTIFIER|
|---|---|---|---|---|
||||||
|Antibodies|||||
||||||
|Rabbit Anti-MOR1|Gifted by Maureen Riedl||N/A||
|Mouse Anti-mCherry antibody (1C51)|Abcam||Abcam Cat# ab125096;<br>RRID:AB_11133266||
|Rabbit anti-NeuN (D3S3I)|Cell Signaling||Cell Signaling Technology Cat# 12943;<br>RRID:AB_2630395||
|Goat Anti-Rabbit IgG Alexa Fluor 488|Invitrogen||Catalog# A-11008||
|Goat Anti-Mouse IgG Alexa Fluor 594|Invitrogen||Catalog # A-11032||
|Goat Anti-Rabbit IgG Alexa Fluor 594|Invitrogen||Catalog # A-11037||
|Bacterial and virus strains|||||
||||||
|AAV5-CamKIIa-hM4D(Gi)-mCherry|Gifted by Bryan Roth||Addgene Catalog # 50477-AAV5;<br>RRID:Addgene_50477||
|AAV5-CamKIIa-mCherry|Gifted by Karl Deisseroth||Addgene Catalog # 114469-AAV5;<br>RRID:Addgene_114469||
|Deposited Data|||||
|Analyzed data and original code|This paper||Data and code to generate the<br>fgures are publicly available at OSF<br>https://osf.io/c4fjm/||
||||||
|Experimental models: Organisms/strains|||||
|Fisher-Brown Norway F1 hybrid rats Rattus<br>norvegicus (8 M, 6 F)<br>Bred in house|||N/A||
|Brown Norway inbred rats (5 M, 6 F)|Envigo||BN/RijHsd||
|Software and algorithms|||||
||||||
|MATLAB v2015b|Mathworks||https://www.mathworks.com||
|MATLAB v2021a|Mathworks||https://www.mathworks.com||
|Kilosort v2.0|Marius Pachitariu140||https://github.com/MouseLand/Kilosort||
|KilosortWrapper|Peter C. Petersen & Brendon Watson||https://github.com/petersenpeter/<br>KilosortWrapper||
|Phy v2.0 Beta 1|Cyrille Rossant141||https://github.com/cortex-lab/phy||
|Python (v.3.8.12) networkX package|Python||https://networkx.org/||
|Other|||||
||||||
|10uL syringe|Hamiton Company||Model 7635-01||
|Pump11 Elite Syringe Pumps|Harvard apparatus||Cat. #70-4501||
|Food Pellets (45 mg, 5TUL)|TestDiet||Cat #: 1811155||
|Reagent or Resource|||||
||||||
|64 Ch Silicon H3 Probe|Cambridge Neurotech||ASSY-156-H3||
|64 Ch Silicon P1 Probe|Cambridge Neurotech||ASSY-156-P1||
|64 Ch Silicon H6 Probe|Cambridge Neurotech||ASSY-156-H6||
|3D printed microdrives|Chung et al.142||https://doi.org/10.1038/s41598-017-<br>03340-5||
|256 Ch Intan RHD Recording System|Intan||Cat #: C3100||
|64 Ch Intan RHD Headstage|Intan||Cat #: C3325||
|Chemicals, peptides, and recombinant proteins|||||
|Isofurane|UMN Research Animal Resources (RAR)||<br>N/A||
|Carprofen|UMN RAR||N/A||
||||(Continued on next page)||



Neuron 112, 4096–4114.e1–e10, December 18, 2024 e1 

**ll** 

Article 

|Continued|||||
|---|---|---|---|---|
|REAGENT or RESOURCE||SOURCE||IDENTIFIER|
|Baytril|UMN RAR||N/A||
|C&B Metabond|Patterson Dental|||Cat #: 553-3484|
|Pentobarbitol|UMN RAR|||N/A|
|Paraformaldehyde|Sigma-Aldrich|||Cat #: 158127|



## EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS 

## Subjects 

Eight adult Fisher-Brown Norway F1 hybrid rats (FBNF-1) (5M, 3F) and one adult Brown Norway (BN) female were used in the recording study (n = 9 rats). FBNF-1 rats (1[st] generation hybrid of F344 female and BN male) were bred in-house, and the BN rat was purchased from Envigo. All rats were aged between 6-11 months old during experiments. While two strains of rats were used in the reported study, we found no evidence for differences in behavior or physiology between FBNF-1 and BN rats, so data were combined. 

Ten adult BN rats (5M, 5F) and six FBNF-1 (3M, 3F) were used in the manipulation (DREADDs) study (n = 16 rats). All rats were aged between 7-15 months old during experiments. While two strains of rats were used in the reported study, we found no evidence for differences response to manipulations between FBNF-1 and BN rats, so data were combined. 

Rats were single housed in a temperature-controlled colony room with a 12 hr light/dark cycle (lights on at 8:00 AM). Throughout the experiments the rats were food restricted and had to maintain a weight of at least 80% of their free feeding weight. Rats were given full access to food one-week prior to probe implantation or DREADDs (designer receptors activated by designer drugs) viral infusion. Surgeries were conducted when the rats were at least at 100% of their prior free feeding weight. All training and experimental sessions were conducted at around the same time and during the rats’ light phase. All procedures were approved by the University of Minnesota Institutional Animal Care and Use Committee (IACUC) and were in accordance with the NIH guidelines. 

## METHOD DETAILS 

## Surgical procedures 

Of the 25 rats used in the study, 9 rats were used for in vivo electrophysiology recordings, and 16 rats underwent viral infusions. Of the 16 virus rats, 8 rats were bilaterally injected with DREADDs[111] virus AAV5-CaMKIIa-hM4Di-mCherry (titer, 2.3310[13] ; Addgene http:// addgene.org/50477) and 8 rats were bilaterally injected with AAV5-CaMKIIa-mCherry control virus (titer, 2.3310[13] ; Addgene http:// addgene.org/114469). 

For the recording study (n = 9), rats were anesthetized with isoflurane (1-2% in O2) and mounted in a stereotaxic frame (Kopf, Tujunga CA). Prior to surgery Carprofen (5 mg/kg SC) and sterile saline (3 mL SC) were administered for analgesia and hydration, respectively. A pair of ground screws were implanted over cerebellum and a pair of anchor screws were implanted to ensure proper bonding to the 3D printed ring that was attached to the skull with C&B Metabond adhesive. Craniotomies were drilled over either HC and DLS contralaterally, HC and mPFC ipsilaterally, or DLS and mPFC ipsilaterally (Male coordinates HC: ± 3 ML -4 AP; DLS: ± 3.3 ML 0.7 AP; mPFC: ± 0.7 ML 2.8 AP; Female coordinates were adjusted by 93%). One 64-channel silicon probe was chronically implanted targeting each region, for a total of two probes in each rat. HC and DLS were always implanted with four shank 64-channel Cambridge Neurotech P-1 probes, while four mPFC rats were implanted with linear 64-channel Cambridge Neurotech H3 probes, one mPFC rat was implanted with two shank 64-channel Cambridge Neurotech H6 probe (R786 – simultaneous recordings from mPFC & HC), and one mPFC rat was implanted with four shank 64-channel Cambridge Neurotech P-1 probe (R787 – simultaneous recordings from mPFC & HC). Targeting for the left and right hemisphere was counterbalanced across rats accounting only for sex (Figures S1C and S1D; Table S1). 

The probes were mounted on custom-made 3D printed micro-drives for precise and independent adjustment of the vertical position. The probes were lowered to �1.5mm and �2.5 mm from skull surface for P-1 and H3/H6 probes respectively to ensure all recording sites were in the brain. The craniotomies were then filled with a sterile mixture of bone wax and mineral oil (3/1 by weight) and the micro-drives were adhered to the skull with Metabond. A 3D printed shell that was painted with conductive paint, head cap, and LED mount were attached to the skull ring, and the ground screw was attached to the inside of the shell via conductive epoxy. 

For viral vector injections, rats went through the same pre-surgery protocol. Craniotomies were made bilaterally over mPFC (±0.7 ML 2.8 AP), and bilateral cannulae were lowered into depth -3.8 DV for females and -4 DV for males (Figure S7A). Rats were randomly assigned to receive either the active virus (CaMKIIa-hM4Di(Gi)-mCherry; n = 8) or control virus (CaMKIIa-mCherry; n = 8). 1mL of virus was delivered at a rate of 200 nL/min. The cannulae were slowly raised following a 15-minute wait period after infusion. The craniotomies were then filled with sterile bonewax. Finally, an LED attachment was adhered to the skull using C&B Metabond to facilitate video tracking during behavior. 

At the completion of the surgery rats were given Baytril (10 mg/kg SC), additional saline (20 ml/kg SC), and Children’s Tylenol (0.8 mL, orally) for antibiotic, hydration and analgesia, respectively. 

e2 Neuron 112, 4096–4114.e1–e10, December 18, 2024 

**ll** 

Article 

**==> picture [46 x 35] intentionally omitted <==**

## Left/Right/Alternation Task 

The left/right/alternation task has been detailed in prior works.[43][,][44][,][50][,][66][,][78] Briefly, in the left/right/alternation task (LRA), rats started from the Start of Maze region at the bottom of the track, and ran through a navigation sequence, in this version, that consisted of three low-cost choice points (Wall 1, Wall 2, Wall 3) to a high-cost choice point at the top of the track (Figure S1A). At the high-cost choice point the rats had to choose whether to proceed to the left or to the right, where each return track consisted of one feeder that automatically delivered one food pellet (45 mg, Test Diet, Richmond IN) if the choice was correct. The rats would then proceed back to the Start of Maze where one food pellet would be delivered if the current choice was correct. We refer to the region between Start of Maze and Choice Point as the central track. The walls of the maze were constructed using DUPLO LEGO bricks with vinyl flooring under the maze. Permanent walls had unique patterns but did not change throughout the experiment. The interior walls of the central path could change daily, but they remained constant within the day. For the recordings experiment, the maze was 108 cm 3 163 cm with 25 cm wide tracks, and for the DREADDs virus study the maze was 94 cm 3 100 cm with 13 cm wide tracks. 

There were three different reward criteria that specified the correct choice on each lap, left reward (L) where food was delivered on the left return rail and Start of Maze, right reward (R) where food was delivered on the right return rail and Start of Maze, and alternation (A) where the rats had to alternate between the left and right return rails to receive reward at the chosen side and Start of Maze. For the left and right reward criteria a choice was considered correct if on each lap rats ran to the left and right sides of the track, respectively. For alternation, a choice was considered correct if on each lap rats alternated which side of the track they went (e.g., if prior choice was left the next choice had to be right and vice versa). If the starting rule was alternation, the rats always received a reward (both at side feeder and Start of Maze) on their first lap of the session. 

At the beginning of the session, rats were placed on the track at the Start of Maze, and then were allowed to run continuously for 45 minutes. Rats were pre-trained to run in a loop. Each correct lap resulted in the automated delivery of two reward pellets, one at the chosen side and one at Start of Maze, thus witheach correct lap, rats earned 90mg of full-nutrition food reward (2 x 45 mg5TUL TestDiet pellets). All pellets were unflavored and performance on the task constituted the sole opportunity for rats to earn food each day. 

All behavioral events were operated through custom built Matlab software (Matlab v2015b, Mathworks) to track rat position, control task state, and trigger reward delivery. Video was collected via an overhead camera sampled at 30 Hz, tracking either the backpack LED (pre-op) or head-mounted LED (post-op). Food delivery was via a Matlab-Arduino interface (Arduino UNO) sending TTL pulses to Med-Associate feeders (Fairfax VT). 

## Initial task training 

Prior to training all rats were handled by the experimenter for 3 to 7 days until they were acclimated. The rats were then food restricted for 5 to 7 days and were offered 30 min of access to unflavored pellets (45 mg/pellet, TestDiet). After the rats were familiar and ate the available food, they were placed back on free feeding for 7 days to return them to their original free-feeding weight. Training started after food acclimation and weight rebound. The training took place before probe implantation for the recording study, and after the virus surgery for the manipulation study to ensure viral expression prior to the experimental phase. Behavioral tracking was done using backpacks with an LED for the recording rats, and a head-mounted LED for the virus rats. Rats were trained over three phases where each ranged from 5 to 15 days. During the first two phases there were no walls (low-cost choice points) within the central track, i.e., it was an open arena. 

In the first training phase, rats were trained to run in a loop starting from the Start of Maze. L and R rules were alternated each day. The incorrect (opposite to the session rule) arm was blocked such that rats were forced to turn congruent with the rule, and thus make the correct choice (e.g., if the reward contingency was L, the right arm was blocked). During this initial phase each feeder (side feeder and Start of Maze) delivered to 2 unflavored pellets/feeder (total of 4 pellets/lap, 180mg of food). Training continued until the rats were running continuously and were completing at least 50 laps/session for each reward contingency (left/right). 

In the second phase of training, blocks were removed, and alternation was introduced as a rule. During the rest of the training days rats experienced one pseudo-randomly chosen reward criterion per day. Rats remained in this phase until they reached 80% correct for each reward criterion (left, right, or alternation) and ran �100 laps continuously (10-15 days). 

In the third phase of training, interior walls were introduced. All possible mazeconfigurations within a given complexity (Figure 2A) were randomly assigned to either be part of the training or the test set. Each day, a maze configuration from the training set was pseudorandomly chosen without replacement, such that everyday had a unique maze configuration. LEGO DUPLO bricks were used to create themazestructure.Similartotraining phasetwo,animalsexperienced apseudo-randomlychosensinglerewardcriterion.Ratsremained in this phase until they reached 80% correct for each reward criterion (left, right, alternation) and ran �100 laps (5-7 days). 

For the recording animals, surgery was conducted after training phase two. After the rats underwent probe implantation, they were reacclimated with the task starting from training phase two, during which the probes were lowered to their appropriate targets (7-12 days). After rats reached phase two criterion, they moved onto phase three, where along with the introduction of the maze walls, rats ran the task with the recording tether attached, familiarizing them with the process of performing the task under full task and recording conditions. 

## Experimental sequence 

Once rats completed their training sequence and the probes were positioned at their appropriate targets, the rats immediately entered the experimental sequence, where all three reward rules were presented to the animal within a single session. Each 

Neuron 112, 4096–4114.e1–e10, December 18, 2024 e3 

**ll** 

Article 

45 min session had two un-cued rule changes that occurred roughly 15 and 30 minutes into the session. A random amount of time between ± 2.2 mins was added or subtracted from the target switch times to reduce predictability. The rule sequence for a given session was pseudo-randomly drawn from one of six possibilities: LRA, LAR, RLA, RAL, ALR, ARL and maze configurations were pseudo-randomly chosen from the test set. 

Recording animals (n = 9 rats) underwent a 16-day experimental sequence (1 session/day). Recordings were performed over these 16 days, totaling 144 recording sessions. Before the task start and after the task end rats sat on a flowerpot for 5 min to record baseline neural activity during quiet resting. The pre/post session recording data were processed but were otherwise not included in analysis. 

The 16-day sequence was further broken up into two experimental sequences spanning 8 days. Each 8-day sequence consisted of 4 unique mazes that were randomly chosen without replacement along the complexity axis; however, each 8-day sequence included the simplest maze (AAA). Rats were run on the same maze configuration under the same task rules for 2 consecutive days (Figure S1B). 

The same experimental protocol was used for the DREADDs rats; however, the experimental sequence was extended to 32-days (nSessions = 508), such that every maze configuration within the test set was used. Deschloroclozapine (DCZ; Hello Bio. Inc., Princeton NJ)[112] was used to activate the DREADDs, or VEH (saline) was used as a control (Figure S7B). The active and control virus animals were paired such that each pair had the same exact same experimental sequence (mazes and switches). DCZ and VEH conditions were presented in a pseudorandomized order, controlling for first-order effects. Importantly, the 2[nd] day-repeat of a given maze/rule configuration was always a saline washout day (Figure S7C). Every day the rats received subcutaneous (SC) injections of either DCZ, VEH, or saline 30 min prior to the start of the experiment. DCZ was dissolved in saline to a concentration of 0.05mg/mL and a single dosage of 0.1mg/kg of DCZ was used throughout the study. For VEH and saline a comparable volume was injected SC. All experimenters were blind to the identity of the solution (DCZ or VEH) injected on a given day. 

## Recordings 

All recordings were collected at 30kHz sampling rate using a 256 channel Intan RHD recording system connected to two 64-channel Intan RHD headstages. An Arduino interface between Matlab and the Intan system facilitated time synchronization of neural data to ongoing behavior. In DLS and mPFC, throughout the 16-day recording sequence probes were periodically lowered (�30mm intervals) to increase the likelihood of recording a diverse array of units. All movement of probes occurred after completion of day’s recordings leaving at least 23 hrs for probes to restabilize before the next recording session. After reaching the CA1 layer in dorsal HC during the training phase, the probes were not subsequently moved, unless there was visible spontaneous movement of the probe from one day to the next. In those cases, HC probes were either lowered or raised to ensure recordings from the CA1 cell layer. While we took appropriate efforts to record diverse ensemble sets of units across days, we are unable to claim that all recorded cells are unique. No attempts were made to identify recordings of the same cells across successive days. 

Spikes were extracted and classified using Kilosort v1.0 for HC, and Kilosort v2.0 for DLS and mPFC using a custom pipeline. Kilosort v1.0 clustering for HC used previously published parameters tuned for HC (https://github.com/brendonw1/KilosortWrapper), and Kilosort v2.0 clustering for mPFC and DLS used default parameters.[140] Automated sorting was followed by manual curation of the waveform clustersusing Phy(https://github.com/cortex-lab/phy).[141] Eachsilicon probewas analyzedindependently and includedthe entire45min task data along with the 5 min pre/post recordings (�55 min total recording time). Prior to Kilosort processing, a median reference subtraction was performed across the 64 channels and a 600 Hz high-pass filter was used for spike identification. Collectively we identified 4292 single units from HC, 2293 single units from DLS, and 2609 single units from mPFC. All unit isolation and manual curation was performed blind to the session’s corresponding behavioral data. 

HC units were separated into putative pyramidal cells and interneurons using their waveform characteristics and firing rates. DLS units were separated as phasic and nonphasic based on the distribution of inter-spike-intervals (ISIs).[40] Phasic cells were those with at least 40% of all ISIs greater than 2 seconds, which we take as putative medium spiny neurons (MSNs). Otherwise, the DLS cell was classified as a nonphasic firing cell. Following previous studies, if a cell that had a post-spike suppression index longer than 100 ms it was classified as tonic firing (putative tonically active cholinergic interneurons). If it did not meet either the MSN or TAN criterion, it was classified as high firing (putative high firing interneurons). Non-phasic (non-MSNs) cells were not analyzed further here. 

## DREADD validation 

In one additional rat (Male FBNF-1) we bilaterally transfused the dorsal mPFC (± 0.7 ML 2.8 AP -3 DV) with the same active inhibitory DREADDs used in the main study (AAV5-CaMKIIa-hM4Di(Gi)-mCherry) (Figure S7B histology). Roughly six weeks after the viral injection, a single 64-channel Cambridge Neurotech H3 probe was chronically implanted into the infusion craniotomy on the right hemisphere and was lowered to 2.3 mm from skull surface. These surgeries used the same procedures outlined above. Over four days the probe was lowered to 4.13 mm (2.86 mm top of probe) from skull surface to span the volume around the DREADD infusion site (Figure S7B histology). 

We performed two recording sessions, one with a DCZ[112] injection and one with a VEH (saline) injection. The recordings were taken for �3hrs during quiet rest of the rat on a flowerpot. We first recorded a 30 min baseline period before drug injection. At 30 mins the rat was injected with either DCZ or VEH (1 session/drug), while the recordings were ongoing. The rat was then placed back on to the pot 

e4 Neuron 112, 4096–4114.e1–e10, December 18, 2024 

**ll** 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

for another 2.5 hrs to establish a time course of drug effect. Multiunit spiking activity (18 isolated units taken collectively for VEH injection Figure S7B left panel, and 5 units for DCZ injection Figure S7B right panel) was binned into 30s bins to calculate the average firing rate over the 3-hour experiment. 

## Histology 

Following the conclusion of all experiments, rats were overdosed with pentobarbital. Rats were perfused transcardially with phosphate-buffered saline and paraformaldehyde. For recording rats, probes were left in place for 3-5 hrs and were then carefully removed from the brain, leaving a visible track of their final position (Figures 1B and S1D). Brains were then extracted and post fixed in paraformaldehyde for 24 hrs before being transferred to a mixture of paraformaldehyde and sucrose for cryoprotection. Coronal sections (40mm sections) surrounding the probe location were cut on a cryostat, mounted to slides. For recording rats, mounted sections were stained with cresyl violet for visualization. In two rats with DLS recordings we performed immunohistochemical staining for MOR1 on a subset of the tissue (anti-m-Opioid Receptor gifted by Maureen Riedl). For virus rats, we used immunohistochemical procedures to amplify the endogenous -mCherry fluorophore. Mounted tissue was labeled with an anti-RFP antibody to visualize viral expression and with an anti-NeuN antibody to counter stain cell bodies. In both cases fluorescent secondary antibodies were used for visualization. 

## Data Analysis 

Most data analyses were performed using custom Matlab software (Matlab v2021a, Mathworks). Quantification of environment complexities were performed using the Networkx package for Python. Each subject was treated independently. No formal replication was performed, but our results agree with previously published work. For all analyses, data were pooled across all subjects (physiology or behavioral responses), but in all cases, we confirmed that reported findings were qualitatively consistent across rats and not driven by a single subject. 

## Quantification of maze complexity 

Three different wall configurations were used to change the maze structure: A: two walls with open space in the middle, B: one wall with open space on the left, and C: one wall with open space on the right. Combinatorial combination with repetition of the three different wall types (A, B, C) created 27 unique mazes (3[3] = 27) (Figure 2A). 

Graph theoretic measures have been previously used to quantify the complexity of an environment.[17][,][84–87] To determine the structural complexity of a maze, we first discretized the inner navigation sequence into 15 bins. These bins corresponded to graph nodes, and each node was connected to another node if it could be reached by a cardinal action—i.e., an edge existed between the two nodes if there was no wall between the two bins. Starting from each node we created 15 generalized trees, with each root node being one of the 15 nodes of the discretized maze. The structural complexity of a tree graph is defined as the Shannon entropy of the distribution of the number of nodes at each level of the tree—e.g., the distribution of the number of nodes across all possible trees one step from the root node. The total structural complexity of the space was then defined as the total information content across all equivalent generalized trees that could be created from a given maze configuration.[86][,][87] The distribution of the total information across mazes was then min-max normalized. This distribution had 3 distinct clusters denoted by the colored circles in Figure 2A that were labeled as low (light green), mid (teal), and high complexity (dark blue) environments, respectively. 

## Behavior 

Each lap (Start of Maze to Start of Maze) was identified as correct or error dependent on whether the rat chose the action congruent with the current contingency/rule and was subsequently rewarded. Percent correct for a given session was calculated based on the ratio between the number of correct laps and the total number of laps. 

The percent correct for a given lap was calculated based on the ratio between the number of sessions in which that lap was correct and the total number of sessions, analyzed for each rat separately. Given that the sessions did not have equal number of laps and the switch times did not occur on the same lap, analyses were restricted to 10 laps pre- and 20 laps post-switch. Everything was computed for each switch independently and then averaged across the switches. 

## Behavioral change point 

To identify laps where rats stabilized their behavior after rule switches, we used a modified version of the change point analysis developed by Gallistel et al.[107] Briefly, behavior in each lap was identified as a left or a right choice and was subsequently coded as either a 1 (left turn) or a 2 (right turn). Note that this differs slightly from prior implementations of this method which consider the correct/error nature of each choice as these methods can generate artificial change points when rats make an error on the first lap following a rule change (before they have any information about the change). This created a num. of Laps x 1 length vector. We then calculated the cumulative sum along this choice vector. Following Ref. Gallistel et al.,[107] we identified behavioral change points as those where the slope of the cumulative sum changed most abruptly. Computationally, this was done using the findchangepts function in Matlab with linear change point detection (statistic = linear) and minimum improvement in total residual set to 2 (minthreshold = 2) so as to not limit the number of change points that could be identified. After detection, change points in every session were visually confirmed by an experimenter blind to all information about maze configuration, task rules, and drug conditions. 

Neuron 112, 4096–4114.e1–e10, December 18, 2024 e5 

**ll** 

Article 

## Running speed 

We computed the running speed as the change in Cx; yD position Cdx; dyD using an adaptive windowing of best-fit velocity vectors.[143] 

## Vicarious trial and error (VTE) 

To quantify vicarious trial and error (VTE) behaviors at the choice point, we calculated the time integrated change in angular movement of the head (IdPhi),which capturesboth pause durationand the prominenceofheadre-orientationbehaviors (Figures 1F and 1G).[76][,][81] IdPhi is calculated by the integral of the absolute value of the arctangent of the velocity over the duration that the rat is in the choice point. Velocity Cdx; dyD was calculated as the first derivative of the rat’s head position Cx; yD using the Janabi-Sharifi and Marey[143] method. 

**==> picture [121 x 31] intentionally omitted <==**

zIdPhi was then computed as the z-scored IdPhi on a lap-by-lap basis for each session. In line with previous work, the distribution of the calculated zIdPhi created a positively skewed bimodal distribution, where the prominent distribution (larger proportion of the overall data centered near 0) captured non-VTE events, and the smaller distribution tail captured VTE events. Based on this distribution, and similar to prior work, we identified a cutoff threshold between VTE or non-VTE laps as z = 0.25 (Figure S2D).[43][,][76] 

## Exploration 

To calculate the amount of space explored, we binned the 2D space into �2cm bins. We then calculated the per session aggregate occupancy in the central path to create a 2D histogram (Figures 3B and S2I). The percentage of space explored was quantified as the total number of counts divided by the number of bins. 

To classify a lap as explorative vs. non-explorative, we first found the median path through the central track. For each lap the trajectory through the central maze segment was resampled to 500 positional points to create a [num. of laps 3 500] matrix for each x and y position. The median path was taken to be the median Cx; yD location across laps for each interpolated sample. We then calculated the point-by-point distance between the resampled lap trajectory and the median path using the dsearchn function in Matlab. If more than 2.5% of the points in a given lap had distances that were above the 95% percentile of the overall distances across all laps, the lap in question was labeled as exploration. 

## Behavioral trajectory stereotypy 

We calculated behavioral trajectory stereotypy from times that the rat was navigating through the central maze segment (central path) (Figures 1H, 1I, 3F, and 3G). Each central path trajectory was resampled to 500 positional points for each x and y position. For lap-bylap stereotypy quantification, we found the reciprocal of the average Euclidean distance between lap i and lap j for each interpolated point.[72] The stereotypy of a given lap i was calculated as the average of the trajectory similarity between lap i and ±5 laps around the diagonal of the stereotypy matrix (i.e., laps i-2, i-1, i+1, i+2-). 

## Maze linearization 

The 2D maze was broken into 2 chunks: central path that spanned Start of Maze to Choice Point and return rails that spanned Choice Point to Start of Maze for each left and right turn (Figure S1A). To avoid any potential overlaps, the zone entry times for each lap were aligned such that the entry of one zone corresponded to the exit of another zone. We subsequently reflected the positional data that corresponded to the time when the rat was in the return rail zone to one side. Similar to above, we found both the median central path and the median return rail path and resampled them to 200 equidistant points. We then combined the resampled median central and return rail paths to form a single path across the whole track. This was done using the polyshape function in Matlab which created a fully enclosed polygon while respecting the overall structure of the input trajectory. This median track path was then resampled in 2D using the interparc function, which interpolates points along a 2D perimeter. All laps were then compared against this median template. The 2D Cx; yD location of the actual position tracking was then reflected onto this median path using the dsearchn function, where the linearized 1D coordinate corresponded to the closest 2D position index, and thus binning the positional data in to 200 bins, which correspond to �2cm bins. All laps that were further than 20 cm away from the idealized path were excluded from further analysis. For each maze, we used the length of the median path through the entire maze (polygon perimeter) to calculate actual bin sizes in cm. For all analyses the binning was then down sampled from 200 to 150 bins resulting in 2.67 ± 0.03 cm bins for the simplest (AAA) maze and 2.89 ± 0.05 cm bins for the most complex (CBC) maze. 

To account for any inconsistencies in linearized maze space due to different maze configurations, we identified the particular bins corresponding to relevant maze locations (e.g., Start of Maze, Wall, Choice Point) in each individual session. These identified bins were used for task bracketing analyses that depended on these designations. 

## Place field analysis 

Tuning curves of HC pyramidal cells were calculated based on the linearized maze by first binning the space, and then generating the maps of bin spike counts over bin occupancy. Bins with occupancies less than 200 ms were omitted. A smoothed tuning curve 

e6 Neuron 112, 4096–4114.e1–e10, December 18, 2024 

**ll** 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

(smoothing size: 2 bins) was constructed by convolving a Gaussian with the generated tuning curve. The smoothed tuning curves were then thresholded to 25% of their maximum firing rate, and place fields were defined as regions within the thresholded maps with an area greater than 15 cm and minimum firing rate of 1Hz. We then extracted the field centers and sizes using regionprops Matlab function on the binarized rate map.[61] 

## Hippocampal Theta cycle identification 

The raw recordings taken from HC were decimated to 2 kHz to extract LFPs. Recordings were bandpass filtered with a Hilbert transform between 6-12 Hz to obtain the theta signal.[18][,][62][,][69][,][93–97][,][144] The instantaneous phase and amplitude were estimated via the Hilbert transform. The channel to identify theta cycles from was chosen based on the probe channel that had maximal theta power. Given that Hilbert transform assumes the data is sinusoidal and because theta is asymmetric, using previous approaches,[145] we first found the peaks and troughs using the filtered signal. We then took these estimated peak and trough times in the raw signal and found the local minima (trough) and maxima (peak) around the estimated times. Theta cycles were limited to 80 to 200 ms. A single theta cycle was defined as peak-to-peak. 

## Bayesian decoding and sequence analysis 

We used Bayesian decoding to calculate ensemble neural representations at both behavioral time-scales and theta-timescales.[98] Briefly, this method computes the posterior probability of the ensemble representing each position in space given spike counts from each single unit in the ensemble. Posterior distributions were normalized to sum to one. Probability of an animal’s position x given all observed spikes from recorded units can be operationalized by: 

**==> picture [119 x 21] intentionally omitted <==**

where x is the set of all linear positions on the track, binned in to �3cm bins. This method assumes that every cell is independent from each other and follows a Poisson process.[98] For decoding of behavioral sequences, as in Figure 4C, we decoded spiking in 120 ms time windows using a uniform spatial prior. 

Bayesian decoding was 5-fold cross-validated. To implement k-fold cross-validation we divided the data into k equally sized subsamples. Of the k-subsamples, k � 1 subsamples were used as the training data and the remaining single subsample was used as the test data. The spikes and position were masked for the duration of the test data to create a PðspikesjxÞ likelihood function from the training data (created using the k � 1 subsamples). The posterior probability was calculated using the above equation for the test data (i.e., PðspikesÞ and PðxÞ were distributions based on the single subsample). 

For all theta-timescale decoding analyses we used two criteria: 1) minimum of 5 cells had to be spiking in the given theta cycle, and 2) the running speed of the rat had to be faster than 2 cm/s. To examine the spatial decoding in theta cycles (Figure 4I), we decoded spiking in each half of the theta cycle — peak to trough and trough to subsequent peak — to obtain a probability distribution across the linearized maze. The obtained posterior probability distribution was subsequently aligned to the rat’s position (± 50 cm around the rat). Posterior probabilities obtained from the two halves of theta were subtracted from each other (2[nd] half – 1[st] half) to obtain the local vs non-local decoding.[73][,][146] The null distribution was obtained by shuffling (n = 1000) the identity of the decoding, 1[st] vs 2[nd] half (red line in Figure 4I). 

To identify sequential structure of theta cycles, we adapted two widely used measures: 1) theta sequence score,[99][,][100] and 2) theta sequence slope.[100][,][101][,][147] In both cases we used Bayesian decoding methods with time bins defined by 1/6 of a theta cycle measure (measure 1) or 20ms bins (measure 2). In the first method, we used weighted correlation coefficients between time and the decoding posterior rðx; tjPÞ. The posterior probability matrix P [num. of spatial bins 3 num. of time points] was used as weights. In a general sense, correlation coefficient is simply the ratio of the covariances of the two variables, normalized by the square root of their variances. Thus, in this case, the weighted means for location x and time t can be written as: 

**==> picture [84 x 46] intentionally omitted <==**

**==> picture [82 x 46] intentionally omitted <==**

Neuron 112, 4096–4114.e1–e10, December 18, 2024 e7 

**ll** 

Article 

where Pij is the probability at time i and spatial bin j. The weighted covariance therefore can be written as: 

**==> picture [172 x 46] intentionally omitted <==**

Finally, the weighted correlation can be calculated by: 

**==> picture [145 x 22] intentionally omitted <==**

Weighted correlation for each reconstructed theta sequence was calculated from the decoded probabilities of positions 50 cm ahead and 20 cm behind the animal’s current position, and decoding was performed for time windows corresponding to p 6 phase intervals of each theta cycle. Intuitively, a sequential structure sweeping along the animal’s running direction would yield a large positive correlation, whereas lack of structure would be close to 0. 

In the second method we computed theta sequence slope by fitting a line that yielded maximum decoded probability within a ± 20 cm window around the rat. For a given line with slope v and intercept r, the average likelihood Rðv;rÞ, that the decoded position is located within a distance d of that line can be written as: 

**==> picture [148 x 23] intentionally omitted <==**

where k is the temporal bin of the posterior probability matrix and Dt is the moving step of the decoding window, in this case 20 ms. The value of d was set to be 10 cm around the rat. In line with prior research, we densely sampled the parameter space for v to find the value that maximized R. 

To calculate the significance of either theta sequences (both sequence score and sequence slope), we circularly shifted the spacebins of the posterior probability distribution (n = 1000) for each time point. As previously described this shuffle conserves the structure of decoded probabilities within a bin but randomizes association between bins. A theta sequence was significant if its score was above the 95[th] or below the 5[th] percentile of the shuffled distribution to account for both forward and reverse sequences.[99–101] 

## Correlation between theta metrics and behavior 

Three behavioral metrics were correlated to theta sequence score and theta sequence slope (Figures 5 and S4). For exploration and stereotypy correlations, only theta sequences within the central path were considered. For zIdPhi correlations, only theta sequences at the choice point were considered. For each session we performed a lap-by-lap correlation between the median theta sequence metric and the behavioral metric (Figures 5A, 5C, 5E, S4A, S4C, and S4E). For binarized exploration vs. no exploration or VTE vs. no VTE, for each session we calculated the median theta score of explorative laps, VTE laps, non-explorative laps, and non-VTE laps, thus the distributions reflect session means (Figures 5B, 5D, S4B, and S4D). 

## Linearized firing rate by lap 

To construct the firing rate maps in Figure 6A, we created rate maps for every lap and every DLS cell as a function of the linear location on the maze (binned into �3cm bins) resulting in a [laps 3 num. of spatial bins 3 num. of cells] matrix (35.8 ± 2.8 SEM number of single units/session). For each session we took the 25 laps from the start of the session and 25 laps following a rule switch (overall rats ran 45.7 ± 12.9 number of laps/rule block), and averaged firing rates across sessions for each maze complexity (low, mid, and high). 

## Task-bracketing index 

Following previous research, we calculated the task bracketing index by subtracting the mean normalized firing rate in the central path from the mean normalized firing rate at the Start of Maze for each cell (Figure 6B).[33][,][35][,][36][,][42][,][72] Zones were defined based on entry and exit times for each session. Positive task bracketing indices indicate relatively strong firing in the Start of Maze compared to the subsequent navigation through the central path, while indices near 0 indicate that there is little to no difference in firing rate at the start compared to the rest of the maze. Given the observed firing rates of DLS cells across the linearized maze, we replicated the analysis using the start and end positions as Start of Maze and Choice point, and this analysis also yielded qualitatively similar results. 

## Spatial cross correlation of ensemble activity 

To investigate how spatial representations were similar to each other across the linearized maze we calculated the spatial cross correlation of ensemble activity (Figures 6D and S5C–S5F). We correlated neural rate maps between pairs of spatial bins. For each cell, we calculated the firing rate in each of the spatial bins throughout the entire maze. For each pair of spatial bins, we computed the correlation between the normalized firing rate vectors for those bins. Therefore, if representations are local (e.g., as is in HC Figure S5C) the spatial cross correlation would appear as highly restricted around the diagonal of the matrix. 

e8 Neuron 112, 4096–4114.e1–e10, December 18, 2024 

**ll** 

## Article 

**==> picture [46 x 35] intentionally omitted <==**

## Stepwise regression between DLS firing and behavior 

To account for linear relationships between behavioral variables (velocity and head direction), we used a stepwise linear regression procedure to relate firing of DLS cells to independent behavioral variables. We performed a sequential and single variable stepwise linear regression to progressively remove the influence of a given behavioral variable on neural firing. Starting from fitting both variables to DLS firing rates, after each step regression subsequent behaviors were fit to the residual firing rates. 

For each lap, velocity in a given linearized spatial bin was averaged to create a lap by bin matrix. Given that we did not have access to exact head reorientation behaviors, we used a proxy, IdPhi, which was independently calculated for each linearized spatial bin. For single variable regressions, each behavior of interest was regressed out separately. For the stepwise linear regression, velocity was regressed out first followed by IdPhi. 

## Population correlation of ensemble activity 

Following previous research, to measure the similarity between population activity across laps, we correlated neural rate maps between pairs of laps.[43][,][44] For each cell, we calculated the firing rate in each of the 5 zone bins (Figure S1A) along the central stem (Start of Maze, Wall 1, Wall 2, Wall 3, Choice point). For each pair of laps, we computed the correlation between the normalized firing rate vectors for the lap. We averaged windows of 10 laps prior and 20 laps post rule switch across sessions to generate switch-aligned average correlation matrices for mPFC, HC, and DLS (Figure 7A). 

## Ensemble population activity change point 

To calculate the population activity change point we used the individual session population correlations. To determine where there are abrupt changes to the population correlation matrix, we used hierarchical clustering to identify reliable neural representations. Briefly, this method seeks to cluster data in an input matrix by constructing a hierarchical cluster tree. Unlike k-means clustering, because the linking tree is fixed, the starting point is not random. 

We first created the linking tree for the population correlation matrix using the linkage function in Matlab and set the method to minimize the inner Euclidean distance between elements (method = ward). Subsequently, we performed agglomerative clustering of the created hierarchical cluster tree (linkage tree) by using cluster function in Matlab. Because the clustering depends on the number of allowed clusters, we followed previous work and repeated our analysis multiple times allowing the maximum clusters to range from 3 to 7.[43][,][44] We then applied a change point analysis similar to that for detecting behavioral changes,[107] but based on cluster identity number instead of choice identity. For each cluster size and session, we cumulatively summed the output cluster IDs, and used the findchangepts function in Matlab to find the laps in which there was a significant change in the cumulative sum of cluster IDs based on slope and mean (statistic = linear). Intuitively, this change point reflects the moment in which neural ensemble data shifted from one consistent representation to another. For each cluster size and session, to calculate the null distribution for lap change points, we shuffled (nshuffles = 75) the cluster IDs across laps and found the change point of the shuffled data. 

We calculated the distribution of change points aligned to change points as the difference between all the change points identified by the clustering in a given switch block to the block’s switch lap. The minimum distance was set as the minimum of the above distribution. 

## mPFC activity prediction of theta score 

We used 5-fold cross-validated Bayesian decoding to decode whether ensemble activity in mPFC predicted hippocampal theta sequence score. For each theta cycle, we calculated the spiking activity of mPFC ensembles. We only took theta cycles in which there were at least 5 mPFC and HC cells active ensuring that we were only using theta cycles in which we had a valid theta sequence score. 

Bayesian decoding requires the expected firing of a cell given the variable of interest to create the likelihood function. We defined our variable of interest as the theta sequence score (15 bins), such that our likelihood function was the expected firing of mPFC cells given binned theta sequence score. Similar to before, we assumed a uniform prior over theta sequence scores. Subsequently, for each theta cycle, we identified the discretized bin of its respective theta sequence score and found the decoded posterior probability for that particular bin — the probability of identifying the correct theta sequence score bin for the particular theta cycles, given a set of mPFC activity. Similar to Bayesian decoding of position, to cross-validate our data, we equally partitioned our data into 5 subsamples. 4 subsamples were used as the training data to create the above likelihood function, and the other remaining subsample was used to calculate the posterior. 

We used three different shuffle methods to create null distributions[50] : 1) shuffled mPFC spike timings, which breaks any relationships within mPFC and/or between mPFC and HC, 2) across session shuffled theta sequence scores, which preserves the mPFC representations, but breaks any moment-by-moment relationship between mPFC and HC, 3) within-lap shuffled theta sequence scores, which breaks the relationship between mPFC and HC within a given lap, but preserves longer behaviorally-relevant timescale relationships. 

In the first method, we shuffled mPFC spike times by circularly shifting the full spike train of each cell by a random amount ranging from 1 min to 45 mins to disassociate neural spiking from variable of interest. In the second method, we shuffled all theta sequence scores within a session by randomly permuting the vector of theta sequence scores to disassociate theta sequence scores from neural spiking in mPFC. Finally, in the third method, we isolated theta sequence scores for each lap, and similarly, randomly permuted 

Neuron 112, 4096–4114.e1–e10, December 18, 2024 e9 

**ll** 

Article 

theta sequence scores within a given lap. For each shuffle we used 5-fold Bayesian decoding to create null distributions. All shuffles were performed 5 times and the mean value was taken across the shuffles as the respective null value. 

Per lap mPFC posterior probability around rule switches were computed by first restricting the data (theta cycles and mPFC activity) to start of maze to side feeder entry and then decoding sequence scores for those theta cycles given restricted mPFC activity. Similar to what was done above, we shuffled the restricted mPFC spike times by circularly shifting them and using the shuffled activity to predict the restricted HC sequence score. 

## Correlation between mPFC prediction of theta score and behavior 

Similar to the analysis done relating theta sequence scores to exploration and zIdPhi for a given pass through the central path for exploration or a pass through the choice point for zIdPhi, we calculated the median posterior probability and correlated that to each metric independently. For each lap, we calculated the correlation between mean deviation through the central path and zIdPhi at the choice point and the median posterior probability of mPFC prediction of HC theta sequence score. We also did the same calculation for null distributions created by the shuffles. 

## Lap peri-event time histograms of mPFC activity 

Full lap switch-aligned mPFC activity were computed using standard methods. For each lap (Start of Maze to Start of Maze), we totaled the spike count and divided by the total lap time to compute average firing rate in each lap. We then normalized mPFC activity across laps for each cell. To compute mPFC activity in different zones, we restricted per lap mPFC activity to either side feeder times (from Feeder entry to Feeder exit) or to the central path (Start of Maze exit to Choice Point entry) and computed spike counts for each of the zones and divided it by the time spent in each zone to calculate firing rates. Similarly, we normalized mPFC activity across laps for each cell. 

To examine mPFC activity for correct and error trials, we labeled each lap as either correct or error based on choice and used the normalized full lap mPFC activity for each correct and error trial across all sessions to create the full distributions. 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

## Statistical analysis 

Data analyses were performed using custom MATLAB (MATLAB 2021a, Mathworks) functions. For comparison across environmental complexity we used mixed effects ANOVAs setting rat as a nested variable for either %Correct or proportion of VTE events and rat as a random factor when evaluating behavioral data and a Kruskal-Wallis test when evaluating physiology. For comparisons between pairs of groups, we used a Wilcoxon rank-sum test. When relating exploratory and procedural behavioral parameters to HC theta sequence score, we used one sample t-tests. For comparison of behavioral responses to different drug conditions, we used mixed effects ANOVAs and set rat as a nested variable and as a random factor. Post-hoc analyses between conditions was done using rank-sum with Bonferroni corrections. For comparison of behavioral responses in DREADD experiments across days, we used a Wilcoxon signed-rank test and mixed effects ANOVAs with rat as a nested variable in the behavior of interest and as a random factor. All assessments of behavior and physiologic responses across laps around a rule switch was done with a one-way repeated measures ANOVA with pairwise post-hoc via rank-sum with Bonferroni corrections. All significance was assessed at a = 0.05. 

e10 Neuron 112, 4096–4114.e1–e10, December 18, 2024 

