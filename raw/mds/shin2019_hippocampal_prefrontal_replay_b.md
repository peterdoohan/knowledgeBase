Article 

## Dynamics of Awake Hippocampal-Prefrontal Replay for Spatial Learning and Memory-Guided Decision Making 

## Graphical Abstract 

**==> picture [286 x 287] intentionally omitted <==**

## Authors 

Justin D. Shin, Wenbo Tang, Shantanu P. Jadhav 

## Correspondence 

wbtang@brandeis.edu (W.T.), shantanu@brandeis.edu (S.P.J.) 

## In Brief 

Shin, Tang, and Jadhav use continuous activity tracking to show that awake CA1 reverse- and forward-replay events predict past and future choices, respectively, with opposing spatial learning gradients. CA1-PFC replay supports recall and planning for spatial working memory tasks. 

## Highlights 

- d Continuous hippocampal-prefrontal (CA1-PFC) replay tracking during spatial learning 

- d Reverse replay for retrospective evaluation, forward replay for prospective planning 

- d Opposing learning gradients for CA1 reverse- and forwardreplay prediction of paths 

- d CA1-PFC replay supports past recall and future decisions for spatial working memory 

**==> picture [17 x 17] intentionally omitted <==**

Shin et al., 2019, Neuron 104, 1110–1125 December 18, 2019 ª 2019 Elsevier Inc. https://doi.org/10.1016/j.neuron.2019.09.012 

Neuron Article 

**==> picture [60 x 60] intentionally omitted <==**

# Dynamics of Awake Hippocampal-Prefrontal Replay for Spatial Learning and Memory-Guided Decision Making 

Justin D. Shin,[1][,][3] Wenbo Tang,[1][,][3][,] * and Shantanu P. Jadhav[1][,][2][,][4][,] * 

1Graduate Program in Neuroscience, Brandeis University, Waltham, MA 02453, USA 

2Neuroscience Program, Department of Psychology, and Volen National Center for Complex Systems, Brandeis University, Waltham, MA 02453, USA 

3These authors contributed equally 

4Lead Contact 

*Correspondence: wbtang@brandeis.edu (W.T.), shantanu@brandeis.edu (S.P.J.) https://doi.org/10.1016/j.neuron.2019.09.012 

## SUMMARY 

Spatial learning requires remembering and choosing paths to goals. Hippocampal place cells replay spatial paths during immobility in reverse and forward order, offering a potential mechanism. However, how replay supports both goal-directed learning and memory-guided decision making is unclear. We therefore continuously tracked awake replay in the same hippocampal-prefrontal ensembles throughout learning of a spatial alternation task. We found that, during pauses between behavioral trajectories, reverse and forward hippocampal replay supports an internal cognitive search of available past and future possibilities and exhibits opposing learning gradients for prediction of past and future behavioral paths, respectively. Coordinated hippocampal-prefrontal replay distinguished correct past and future paths from alternative choices, suggesting a role in recall of past paths to guide planning of future decisions for spatial working memory. Our findings reveal a learning shift from hippocampal reverse-replay-based retrospective evaluation to forward-replay-based prospective planning, with prefrontal readout of memory-guided paths for learning and decision making. 

## INTRODUCTION 

The hippocampus is necessary for formation and retrieval of episodic memories to guide daily behavior, including goaldirected spatial learning and navigation (Eichenbaum and Cohen, 2004; Squire, 1992). Hippocampal place cells are active in specific spatial locations during exploration (O’Keefe and Nadel, 1978). While this spatial code provides information about current location, spatial memories require learning links between sequences of locations that encode specific paths and choices that lead to goals, which is likely to be supported by another 

phenomenon called ‘‘replay’’. Hippocampal replay is associated with high-frequency sharp-wave ripple (SWR) events prevalent during offline periods in both sleep and non-exploratory waking states (‘‘awake replay’’) (Buzsa´ ki, 2015). During replay, temporally compressed sequences of place cells reactivate spatial trajectories in explored environments in either forward or reverse order (Ambrose et al., 2016; Diba and Buzsa´ ki, 2007). Notably, while sleep replay is associated with offline memory consolidation, awake replay during pauses in exploration is ideally suited to support processes associated with ongoing memory-guided behavior, including retrospection, retrieval, prospection, and planning (Carr et al., 2011; Foster, 2017; Joo and Frank, 2018). 

Converging evidence from rodents (Buzsa´ ki, 2015; Carr et al., 2011; Foster, 2017), primates (Leonard et al., 2015), and humans (Vaz et al., 2019) suggests that awake replay is important for memory-guided behavior and cognition. In rodents, awake reverse and forward replay represents behavioral trajectories in spatial environments (Ambrose et al., 2016; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006; Gupta et al., 2010; Karlsson and Frank, 2009; Xu et al., 2019), and both loss-of-function (Jadhav et al., 2012) and gain-of-function experiments (Ferna´ ndezRuiz et al., 2019) have shown a causal role of awake replay in spatial working memory tasks. Several reported features of hippocampal awake replay are suggestive of its functional roles. First, replay is enhanced by reward and novelty (Ambrose et al., 2016; Cheng and Frank, 2008; Foster and Wilson, 2006; Singer and Frank, 2009), specifically for reverse replay on linear tracks (Ambrose et al., 2016), and is coordinated with subcortical reward activity (Gomperts et al., 2015; Lansink et al., 2009), pointing to a role in temporal credit assignment and reinforcement learning of paths leading to goals (Foster, 2017; Foster and Knierim, 2012; Haga and Fukai, 2018). Additionally, replay is hypothesized to support memory retrieval for planning upcoming choices (Carr et al., 2011; Singer et al., 2013)—there is evidence that replay is involved in fear memory retrieval (Wu et al., 2017), and specifically forward replay is associated with planning of future trajectories (Pfeiffer and Foster, 2013; Xu et al., 2019). Further, awake replay can represent random (Gupta et al., 2010; Stella et al., 2019) and remote trajectories (Karlsson and Frank, 2009), suggesting a role in free recall. In agreement with rodent studies, recent evidence identifies an analogous 

**==> picture [16 x 17] intentionally omitted <==**

1110 Neuron 104, 1110–1125, December 18, 2019 ª 2019 Elsevier Inc. 

**==> picture [60 x 60] intentionally omitted <==**

role of human and primate awake replay in cognitive processing (Leonard and Hoffman, 2017; Liu et al., 2019; Norman et al., 2019; Vaz et al., 2019). 

Despite this mounting evidence, how reverse and forward replay together support the proposed roles in learning, retrieval, and memory-guided decision making remains unclear. Further, whether and how replay content changes over the course of learning to support memory-guided choices is not known. Addressing these questions requires monitoring the evolution of replay content in the same neural populations over the entire duration of learning. 

In addition, it is hypothesized that hippocampal replay of behavioral paths may contribute to a cognitive search process based on previous experience, which can influence target regions (Joo and Frank, 2018; Singer et al., 2013; Tang and Jadhav, 2019). Indeed, goal-directed behavior relies on a wider neural network for evaluation and selection of task-relevant memories during retrieval and decision making, and the cognitive processes of learning, deliberation, and spatial navigation are known to require the prefrontal cortex (PFC; Eichenbaum 2017; Epstein et al., 2017; Ito et al., 2015; Pezzulo et al., 2014; Redish 2016; Tang and Jadhav 2019; Yu and Frank 2015). How hippocampal and PFC networks together support learning and planning, especially for replay-dependent working memory tasks, remains an open question. Hippocampal-prefrontal (area CA1-PFC) neural activity is coordinated during SWRs for reactivation of spatial paths (Jadhav et al., 2016; Peyrache et al., 2009; Tang et al., 2017), but whether this coordinated CA1-PFC reactivation can distinguish hippocampal replay content in a behavioral context, and how it plays a role in memory-guided behavior, is not known. 

We therefore used continuous and simultaneous tracking of neural ensembles in CA1 and PFC throughout the course of learning of a replay-dependent W-track spatial alternation task to address three key questions: (1) how is awake CA1 replay involved in choice behavior during decision making; particularly, how do reverse and forward replay relate to past and future choices; (2) how replay content changes over learning and the evolution of reverse and forward replay as learning progresses; and (3) whether coordinated CA1-PFC replay can distinguish hippocampal replay content and its relationship to ongoing behavioral choices. 

## RESULTS 

## Continuous Tracking of Forward and Reverse Replay throughout Learning 

We used continuous and simultaneous electrophysiological monitoring of ensembles of CA1 and PFC neurons in rats learning a novel W-track spatial alternation task within a single day (Figures 1 and S1). This task involves continuous alternation between reward wells on the three maze arms (Figure 1A). Animals are rewarded upon completion of a correct inbound or outbound sequence according to the following rules: (1) starting from either side well, animals have to return to the center well (inbound trajectories 2 and 4), and (2) starting from the center well, animals have to recall the previous inbound trajectory and choose the opposite side well from the previously visited one (outbound trajectories 1 and 3). 

Awake replay, as well as functional hippocampal-prefrontal interactions, is important for learning the outbound, spatial working memory component of this task (Ferna´ ndez-Ruiz et al., 2019; Jadhav et al., 2012; Maharjan et al., 2018). The historydependent, spatial working-memory behavioral sequence consists of two consecutive trajectories with a center-well transition (Figure 1Bi), where the past path is an inbound trajectory terminating at the center well, and the future path is an outbound trajectory proceeding to the opposite side-arm. In contrast, the inbound component requires implementation of a ‘‘return-tocenter’’ rule based only on the current location from each side well (Figure 1Bii), and this reference memory rule is history independent. For side-well transitions, the past path is outbound, and the future path is inbound; the past and future paths are thus reversed at the center and side wells (Figure 1B). 

Animals (n = 6 rats) were tasked with learning the W-maze rules in eight behavioral sessions (epochs 1–8, or E1–8, 15–20 min per session) in a single experimental day, interleaved with rest sessions in a sleep box (single-day learning; learning curves in Figure S1; see STAR Methods) (Maharjan et al., 2018). We continuously and simultaneously recorded from the same stable ensembles in dorsal CA1 (n = 216 cells with place fields on the track) and PFC (pre-limbic and anterior cingulate cortical regions; n = 154 cells) for all 8 sessions over the course of learning (5.5–6.5 h; see STAR Methods; recording locations in Figures S1A–S1C; isolation and stability parameters for simultaneously recorded neurons in six rats shown in Figures S1D– S1G). This experimental design thus enabled investigation of CA1-PFC replay dynamics using the same ensembles, starting from initial acquisition through later memory performance. 

CA1 place cells exhibited spatial and direction selectivity, with unique sequential representations of different trajectories (Figures 1C–1H). Figure 1C shows responses of all recorded CA1 place cells for the 4 trajectories in each behavioral session. Place cell encoding of spatial locations enabled accurate decoding of animal position during trajectory running (Figures 1D–1F) (Ambrose et al., 2016). Comparison of opposing outbound-inbound trajectory pairs (Figure 1C shows linearized place-cell responses in pairs of trajectories with opposite running directions; 1 versus 2, and 3 versus 4) confirmed that place cells were directionally selective starting with the first session on the novel track (Foster and Wilson, 2006), and direction selectivity significantly improved over experience (Figures 1G and 1H) (Frank et al., 2004; Navratilova et al., 2012; Xu et al., 2019). Despite the presence of bidirectional cells (37.7% ± 17.1%, mean ± SD; number of unidirectional cells in Table S1), place-field templates for all trajectories were distinguishable for all sessions (illustrated in the confusion matrices in Figures 1D–1F; cross-validated decoding error: 3.81 ± 0.13 cm in median ± SEM). Further, the stability and specificity of place-cell activity increased with familiarity (Frank et al., 2004; Jadhav et al., 2012), although the proportion of place cells remained constant (Figures S2A–S2C). Thus, there was a change in average decoding error over sessions, but, notably, the highest decoding error (session 1: 6.30 ± 0.47 cm) was comparable to previous reports (Ambrose et al., 2016; Davidson et al., 2009; Farooq and Dragoi, 2019; O’Neill et al., 2017). Therefore, CA1 ensembles exhibited independent population representations of the 4 behavioral trajectories starting 

Neuron 104, 1110–1125, December 18, 2019 1111 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [409 x 332] intentionally omitted <==**

**----- Start of picture text -----**<br>
A C<br>B<br>D F<br>E<br>G<br>H<br>**----- End of picture text -----**<br>


**==> picture [15 x 31] intentionally omitted <==**

**==> picture [14 x 31] intentionally omitted <==**

**==> picture [14 x 31] intentionally omitted <==**

**==> picture [14 x 31] intentionally omitted <==**

**==> picture [15 x 30] intentionally omitted <==**

**==> picture [14 x 30] intentionally omitted <==**

**==> picture [14 x 30] intentionally omitted <==**

**==> picture [14 x 30] intentionally omitted <==**

**==> picture [15 x 30] intentionally omitted <==**

**==> picture [14 x 30] intentionally omitted <==**

**==> picture [14 x 30] intentionally omitted <==**

**==> picture [14 x 30] intentionally omitted <==**

**==> picture [15 x 31] intentionally omitted <==**

**==> picture [14 x 31] intentionally omitted <==**

**==> picture [14 x 31] intentionally omitted <==**

**==> picture [14 x 31] intentionally omitted <==**

**==> picture [72 x 150] intentionally omitted <==**

**==> picture [59 x 43] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [37 x 34] intentionally omitted <==**

**==> picture [59 x 39] intentionally omitted <==**

Figure 1. Hippocampal Place-Cell Sequences Distinctly Represent Different Behavioral Trajectories during Learning of a W-Maze Spatial Memory Task 

(A) W-maze spatial alternation task design, depicting the correct behavioral sequence of outbound (blue) and inbound (teal) trajectories (labeled 1–4) for reward. Right-left is indicated according to animal direction. 

(B) Past and future trajectories during transitions at reward wells. (i) Two correct behavioral sequences at the center well. (ii) One correct behavioral sequence for each side well (left or right well). 

(C) Place fields of all CA1 place cells (n = 216) recorded from 6 rats continuously across 8 learning sessions (or epochs; denoted as E1–8) in single-day learning. The fields for trajectories 1 and 2, sorted according to peak positions on trajectory 1 or 2, are shown on the top two rows. The bottom two rows are for trajectories 3 and 4. Horizontal axes denote normalized position along the start to end of the corresponding trajectory. 

(D–F) Position reconstruction based on CA1 ensemble spiking during active running behavior on trajectories (>5 cm/s). Decoding performance was estimated using leave-one-out cross-validation. (D) Example confusion matrices depicting true and estimated positions during running on trajectories 1–4. (E) Illustrative estimated position probabilities using data from a single animal for individual sessions. Cyan line: actual animal trajectory. (F) Cumulative position decoding errors across all animals. Dashed lines: individual animals; red line: all animals; solid black line: the example animal shown in (D) and (E). Median error of all sessions (vertical red line) noted on top. Decoding error: 6.30 ± 0.47 cm for session 1; 3.58 ± 0.35 cm for session 8 (in median ± SEM). 

(G and H) Directional selectivity of place cells. (G) Directionality index (DI) of place cells across learning sessions. Red and blue bars above indicate significant increases from the first session (p < 0.05, Friedman tests with Dunn’s post hoc). Error bars: SEM. (H) Similarity of the place-cell population in two running directions was computed using the population vector overlap (PVO). Gray shadings: 95% confidence intervals (CIs) of the shuffled distributions from each animal using trial-label shuffles. Blue and red lines with error bars: means with SEMs for right (i.e., trajectories 1 versus 2) and left (i.e., trajectories 3 versus 4) trajectories, respectively. Note that distinct templates for each direction are apparent in the first session (p < 0.0001 compared to the shuffled data for individual rats, permutation tests). See also Figure S1 and Table S1. 

from the first novel session, enabling accurate position decoding. 

We used these template place-cell sequence representations from stably recorded ensembles to detect and continu- 

ously track forward and reverse CA1 replay events throughout learning (Figures 2 and S2). To investigate replay content, we used established methods to detect SWRs and candidate events during immobility periods at reward wells and used 

1112 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [481 x 404] intentionally omitted <==**

**----- Start of picture text -----**<br>
A C E<br>B D F<br>G H I J K<br>**----- End of picture text -----**<br>


Figure 2. Continuous Tracking of Forward and Reverse Replay throughout Learning 

(A–F) Six examples of forward and reverse replay of behavioral trajectories in different learning sessions using continuously tracked CA1 ensembles in one animal. (A) Reverse replay event in Session 2; (B) reverse replay event in Session 3; (C) forward replay event in Session 4; (D) reverse replay event in Session 4; (E) forward replay event in Session 7; (F) forward replay event in Session 8. (i) Left: place-cell activity during a SWR, with ripple-filtered local field potential (LFP) (150–250 Hz) from one tetrode shown on top. Right: corresponding linearized place fields on trajectories 1–4 sorted by their peak locations on the replayed trajectory (red). (ii) Bayesian reconstruction of the decoded behavioral trajectories with the replay quality (r) and p value based on time-shuffled data denoted on top. Cyan lines: the linear fit maximizing the likelihood along the replayed trajectory. Color bars: posterior probability. See also Figure S2 for additional replay examples. (G–I) Distributions of (G) animals’ immobility times at reward wells, (H) the number of SWRs, and (I) candidate events (open bars) and replay events (solid bars) detected in immobility periods per choice (i.e., per transition). Only correct trials are shown. Vertical dashed lines on the histograms represent the mean values (immobility time: 10.3 ± 5.7 s; SWRs: 7.3 ± 5.5 events; candidate events: 2.3 ± 2.4 events; replay events: 0.9 ± 1.2 events; data are presented in mean ± SD). (J and K) Number (J) and percentage (K) of forward- and reverse-replay events of different trajectory types (i.e., C-to-R, center-to-right; C-to-L, center-to-left; R- to-C, right-to-center; L-to-C, left-to-center). Each dot represents a session, summing over all 6 animals (sessions 1 and 2 were combined). Error bars: mean ± SEM. Note that the number of replay events of different trajectories was similar (F(7, 42) = 3.062 and p = 0.053 for J, F(7, 42) = 2.227 and p = 0.12 for K; repeatedmeasures ANOVA). 

Bayesian decoding to identify CA1 replay events, with each event distinctly determined as forward or reverse replay of one of the four trajectories (Ambrose et al., 2016; Davidson et al., 2009; Tang et al., 2017; see STAR Methods). Examples of forward- and reverse-replay sequences from the same CA1 ensembles in different learning stages of one animal are shown 

in Figures 2A–2F (additional examples in Figure S2). During immobility periods at reward-well transitions (immobility time: 10.3 ± 5.7 s in mean ± SD; Figure 2G), multiple SWRs and replay candidate events were detected (Figures 2H and 2I; immobility periods with R2 events, 85.7% or 1,313/1,533 trials for SWRs; 53.4% or 818/1,533 trials for replay candidate events). Further, 

Neuron 104, 1110–1125, December 18, 2019 1113 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [481 x 266] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C<br>C<br>C<br>D E F H J<br>G I K<br>**----- End of picture text -----**<br>


Figure 3. Reverse Replay of Possible Past Paths, Forward Replay of Possible Future Paths (A–E) Illustration of past and future trajectories replayed by reverse and forward place-cell sequences at reward wells. (A–C) Example of side reward well transition. (A) CA1 neural activity during an outbound-inbound sequence (RUN1 to RUN2), with replay events at the left side well. From top to bottom, the behavioral sequence, animal speed, broadband and ripple-filtered LFPs from one CA1 tetrode, and raster plot of 20 place cells ordered by the positions of their place-field peaks (red ticks; linearized animal position in overlaid blue line). CA1 exhibits theta oscillations (8–10 Hz; blue LFP shading) during running, and SWRs during immobility, coincident with synchronous activity of place cells (indicated by arrowheads and shadings). Five synchronous candidate events were seen, with 3 events detected as significant replay sequences (yellow shadings). (B) Expanded view of the 3 replay events from (A), identified as reverse replay of RUN1 (past) and forward replay of RUN2 (future). (Bi–Biii) Each column shows the Bayesian reconstruction of the animal’s trajectory during replay (top), ripple-filtered LFP (middle), and spike raster of place cells (bottom) sorted as in (A) (raster corresponding to replayed trajectory, red). (Ci–Ciii) Bayesian reconstructions of the decoded behavioral trajectories 1–4 for replay events in Bi–Biii, (replayed trajectory bordered as red). Color bars: posterior probability. See also Figure S3 for similar center reward well example. 

(D and E) Replay events during two example transitions at the center well. (i) Behavioral sequences for the center-well transition. (ii) A single replay event at the center well. Top: Bayesian reconstruction of the replayed trajectory. Colored points overlaid on the replay trajectory (black arrowhead line) indicate the Bayesiandecoded positions (see STAR Methods), with the color denoting relative time within the replay event. Bottom: ripple-filtered LFP and the sequential SWR spiking of place cells. (iii) Bayesian reconstructions of the decoded behavioral trajectories. See also Figure S3 for additional examples for replay of past and future paths. (F) At the center well, inbound (past paths) and outbound trajectories (future paths) were preferentially replayed in a reverse and forward order, respectively. At the side wells, outbound (past) and inbound trajectories (future) were preferentially replayed in a reverse and forward order, respectively. ****p < 1e-4, session-bysession rank-sum paired test. Error bars: SEM. 

(G) The bias in (F) is consistent in each rat (circles; n = 6). 

(H and I) The bias in (F) at the center (H) and side (I) wells appeared similarly across all 8 behavioral sessions (E1–8). n.s., non-significant (center well: main effect of group, p = 0.52 and 0.44 for inbound and outbound, respectively; side wells: main effect of group, p = 0.30 and 0.59 for inbound and outbound, respectively; Kruskal-Wallis tests). ****p < 1e-4, session-by-session rank-sum paired test. 

(J) Patterns of reverse and forward replay can discriminate goal-locations (n = 3 wells). The cross-validated decoder using the support vector machine (SVM) is significantly better than chance (error bars) defined by permutation tests (****p < 0.0001; see STAR Methods). Only correct trials were used for (A)–(J). (K) Comparison of well-prediction accuracy for correct and incorrect future outbound trials originating at the center well. Error bars indicate 95% confidence intervals based on bootstrapped data (n.s., p = 0.06; **p = 0.01). See also Figures S3 and S4 and Table S2. 

there was no overall bias toward reverse or forward replay of any particular trajectory type (Figures 2J and 2K). 

## Reverse Replay of Possible Past Paths, Forward Replay of Available Future Paths 

In order to examine the relationship between replay content and behavioral choices, we focused on transition periods between 

trajectories. A correct behavioral sequence comprising two consecutive trajectories is illustrated for a side-well transition (Figures 3A–3C; similar example for a center-well transition in Figures S3A and S3B). This transition comprises an outbound past trajectory (RUN1, center-to-left), followed by an inbound future trajectory (RUN2, left-to-center), with the place-cell sequences ordered for RUN1 and RUN2 shown in the sorted 

1114 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

CA1 activity (Figure 3A). Three replay events during this transition were identified as two reverse-replay events of the past (RUN1) and one forward-replay event of the future trajectory (RUN2) (Figures 3B and 3C) in an inter-mixed order of occurrence (reverse-forward-reverse). Replay events at the side well thus reactivated the past outbound trajectory in reverse and the future inbound trajectory in a forward order. 

A similar pattern of replay was seen at center-well transitions (Figures 3D, 3E, and S3), with preferential reverse replay of past inbound trajectories and forward replay of future outbound trajectories (examples show reverse replay of the alternative, not-taken past path in Figure 3D, and forward replay of the behaviorally actualized, taken future path in Figure 3E). Thus, for both center- and side-well transitions, reverse and forward replay preferentially reactivated past and future trajectories (both actual and alternative paths), respectively (additional examples in Figure S3). 

We quantified this relationship of forward- and reverse-replay content with ongoing behavioral trajectories and found a strong and consistent prevalence of reverse replay of the two possible past choices (actual taken and alternative past paths to reward well) and forward replay of the two possible future choices (actual taken and alternative future paths from reward well), at the respective reward well location (Figures 3F–3I and S4). At the center well, this manifested as reverse replay of inbound trajectories (possible past paths; reverse/forward events, 324/91, p < 1e-4, z-test for proportions) and forward replay of outbound trajectories (possible future paths; reverse/forward events, 116/ 202, p < 1e-4, z-test for proportions), which was reversed at the side wells (reverse/forward events for outbound trajectories: 267/115, reverse/forward events for inbound trajectories: 101/ 272, p’s < 1e-4, z-tests for proportions; session-by-session comparison in Figure 3F; see also Table S2). This effect was consistent across all six animals (Figure 3G) and in different learning stages (Figures 3H and 3I). 

This phenomenon persisted when we included only significantly unidirectional CA1 cells to rule out any unintended bias due to bidirectional cells (Figure S4A). Further, we ruled out the effect of ‘‘splitter’’ cells, which exhibit trajectory-dependent firing on the central arm of the maze (Ainge et al., 2007; Frank et al., 2000; Ito et al., 2015; Wood et al., 2000) (Figures S4B–S4D). Most replay events had at least two active side-arm cells, which can unambiguously detect left versus right trajectory replays, and, further, the bias in reverse and forward replay persisted with exclusion of center-arm cells (Figures S4C and S4D). 

We next asked whether there was a tendency for reverse and forward replay to occur at the end of previous trajectory and prior to the upcoming trajectory, respectively (Diba and Buzsa´ ki, 2007). As previously reported (Ambrose et al., 2016), no such bias was apparent, and reverse replay of past paths and forward replay of future paths continued in an inter-mixed order in immobility periods (Figures S4E and S4F). We did, however, find that replay rate was significantly higher during ‘‘disengaged’’ compared to ‘‘engaged’’ periods during reward-well transitions (O[´ ] lafsdo´ ttir et al., 2017) (Figures S4G–S4I; engaged periods defined by proximity to arrival and departure times, see STAR Methods). Finally, we also confirmed that the observed effect was not a result of bias in the distribution of place fields or 

decoded replay positions (Figures S4J–S4N). In fact, the distribution of decoded positions in replay events again revealed the over-representation of past paths in reverse replay and future paths in forward replay (Figures S4K and S4L). 

The behavioral relevance of this replay pattern was confirmed by using the identity of reverse- and forward-replay events during a specific reward-well transition to predict the current location of the animal (i.e., left, center, or right reward well; see STAR Methods). For correct trials, we observed prediction accuracies that were significantly higher than chance level (Figure 3J), indicating the existence of unique replay patterns that discriminate between goal locations. Thus, replay content was dependent on the current goal location and further was also associated with an initiation bias (Davidson et al., 2009; Foster and Wilson, 2006; Karlsson and Frank, 2009) and over-representation of current position specifically for reverse replay (Figures S4L–S4N). We compared this effect of reverse past replay and forward future replay for correct and error outbound working-memory trials that originated from the center well and observed an impairment specifically in forward replay of future paths. For these trials, animals were located at the center well after performing a correct past trajectory (inbound; rewarded) and about to choose the next outbound trajectory either correctly or incorrectly. Thus, both future correct and error trials were preceded by a rewarded inbound trajectory, with no differences in immobility time, SWR number, or replay rate between correct versus error trials (Figures S3I–S3J). We found, however, that there was a significant decrease in prediction accuracy using forward replay during error trials compared with correct trials (Figure 3K), corresponding to absence of future bias in forward replay (for error trials, forward replay of future: 45%, p = 0.53; reverse replay of past: 68.5%, p = 0.008; z-test for proportions). Further, for trials that were unrewarded (which occurred at the side wells upon the completion of an incorrect outbound trajectory), the bias in both forward and reverse replay was absent (Figures S3K–S3M). 

## Contrasting Evolution of Reverse and Forward Replay with Learning 

Since reverse- and forward-replay events consisted of both actual taken and alternative (not-taken) past and future paths, respectively (Figures 3, S3, and S4), we next asked whether there was any relationship between replay content and memory demands at different learning stages. First, even as performance improved over learning sessions (Figures 4A and S1H), there was no change in the balance of overall reverse- and forward-replay events (Figures 4B–4E). SWR rate, amplitude, and frequency did not change (Figures 4B and S5A), but there was a decrease in replay rate over learning for both reverse and forward replay (Figures 4C and S5G). The decrease in replay rate corresponded to a decrease in place-cell activation during SWRs, which was attributed specifically to a decrease in activation for non-replay events, thus leading to a reduction in candidate events (Figures S5C–S5F). In addition, as animals became increasingly proficient in the task, there was a decrease in immobility duration at reward wells (Figure S5B), resulting in an overall reduction in the total number of SWRs and replay events at reward wells (Figures S5H–S5M). However, the fraction of reverse- and forwardreplay events of any trajectory type did not change throughout 

Neuron 104, 1110–1125, December 18, 2019 1115 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [325 x 188] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B C D<br>E F G<br>**----- End of picture text -----**<br>


**==> picture [69 x 42] intentionally omitted <==**

Figure 4. Dynamics of SWR Replay Properties over the Course of Learning (A) Task performance, showing proportion correct of outbound trajectories per session for all animals (n = 6 rats). (B) Total SWR rate did not change across sessions (p = 0.28 and F(6, 30) = 1.44, repeated-measures ANOVA). 

(C) Replay rate decreased over learning (p = 0.0005, F(6, 30) = 14.21, repeated-measures ANOVA; **p = 0.003, Tukey’s post hoc tests). (D) Percentage of reverse replay out of all replay events did not change across sessions (p = 0.12, F(6, 30) = 2.370, repeated-measures ANOVA). (E) Number of forward- and reverse-replay events of the 4 behavioral trajectory types across 8 learning sessions (E1–8). The trajectory types are color coded with red arrowheads indicating 50% level for forward and reverse replay. 

(F) Duration of SWR events decreased over learning (p < 1e-4, Kruskal-Wallis test; ***p = 0.0003, ****p < 0.0001, Dunn’s post hoc tests). (G) Decoded length of replay trajectories increased over learning (p = 0.0004, Kruskal-Wallis test; ***p = 0.0001, *p = 0.039, Dunn’s post hoc tests). Dashed lines in (A)–(D): individual animals. Solid line and error bars: mean and SEMs. See also Figure S5. 

learning (Figures 4D, 4E, and S5G). Interestingly, we observed a decrease in SWR duration but an increase in decoded replay length over learning (Figures 4F and 4G). Enhanced SWR duration in novel environments agrees with previous reports (Ferna´ ndez-Ruiz et al., 2019), and the increase in replay length suggests that the speed of replay increases over learning. Together, the shorter SWR duration, sparser place-cell activity and longer trajectories reactivated during SWRs may reflect enhanced efficiency of replay over learning. 

We further examined replay content at different learning stages independently at center- and side-well transitions, since outbound and inbound trajectories originating from these reward wells entail distinct memory demands (spatial working memory and spatial reference memory, respectively) (Jadhav et al., 2012). Examples of replay events during early learning in initial sessions (E1–3) and late performance in final sessions (E6–8) are shown in Figures 5A–5D and S3 (behavioral performance on the outbound and inbound component, 59.9% ± 9.1% and 65.5% ± 28.2% for early learning, and 83.8% ± 9.6% and 97.14% ± 0.03% for late performance, respectively, in mean ± SD; see STAR Methods and Figure S1H). At the side wells, reverse-replay events preferentially reactivated the actual taken past path during early learning, with this bias lost as performance improved (Figures 5A and 5E). On the other hand, forward-replay events at side wells shifted their content from no initial bias during early learning to preferential replay of the future taken path during late sessions, when animals started performing well above chance levels (Figures 5C and 5E; overall, forward-replay 

events of future taken versus not-taken paths: 169/387 versus 103/387, 43.7% versus 26.7%, p < 1e-4; reverse-replay events of past taken versus not-taken paths: 200/376 versus 67/376, 53.2% versus 17.7%, p < 1e-4, z-test for proportions; see also Table S2). 

In contrast, at the center well, reverse- and forward-replay events continued to reactivate, in an unbiased manner, both the actual taken and the alternative (not-taken) past and future paths, respectively, throughout learning (Figures 5B, 5D, and 5F; overall, reverse-replay events of past taken versus not-taken paths: 146/439 versus 177/439, 33.6% versus 40.3%; forwardreplay events of future taken versus not-taken paths: 111/293 versus 91/293, 37.9% versus 31.6%; p = 0.55, z-test for proportions). Replay content thus exhibited distinct dynamics over learning at the side and center wells. We also confirmed that changes in splitter cells are not the primary reason for the observed changes in replay content (Figures S6A and S6B). 

At the side wells, consistent with the correlation of replay content with behavioral performance (Figure 5E), reverse-replay content accurately predicted the actual past path during early learning stages but not later performance (Figure 5G, left; see STAR+Methods), whereas accurate prediction of actual future path based on forward replay emerged only after learning during later performance sessions (Figure 5G, right). In contrast, at the center well, reverse replay could not predict the actual taken past path (Figure 5H, left), and, although there was a non-significant correlation trend for increase in forward replay of taken path (Figure 5F, right), forward-replay content was unable to 

1116 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [253 x 369] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>C D<br>E G<br>F H<br>**----- End of picture text -----**<br>


**==> picture [146 x 60] intentionally omitted <==**

**==> picture [140 x 55] intentionally omitted <==**

**==> picture [156 x 156] intentionally omitted <==**

Figure 5. Contrasting Evolution of Reverse and Forward Replay during the Course of Learning (A and B) Example reverse-replay events during early learning at (A) the side well and (B) the center well. Data are presented as in Figure 3. (C and D) Example forward-replay events during late performance at (C) the side well and (D) the center well. See also Figure S3 for additional examples. (E and F) Relationship between task performance and fraction of reverse replay of past taken paths (left) or forward replay of future taken paths (right) at (E) the side wells and (F) the center well. Each dot represents one session from a subject. Note the significant negative correlation for reverse replay (r = �0.57*, p < 0.0001) and positive correlation for forward replay (r = 0.28*, p = 0.035; permutation tests) at the side wells, but not the center well (r = 0.08, p = 0.64 for reverse replay; r = 0.22, p = 0.09 for forward replay). (G) At side wells, reverse-replay events predict taken past paths during early learning sessions (left), while forward-replay events predict future taken paths during late performance sessions (right). Cross-validated SVM decoders were trained during early, middle, and late sessions (sessions 1–3, 4–5, and 6–8, respectively). Significant prediction power was only observed during early and middle sessions for reverse replay (left; p < 0.0001****, 0.0001****, and = 0.43 for early, middle, and late sessions, respectively) and late sessions for forward replay (right; p = 0.23, 0.35, and 0.003** for early, middle, and late sessions, respectively). (H) Taken paths cannot be predicted from patterns of replay events at the center well (p = 0.36, 0.08, and 0.68 for reverse replay, p = 0.38, 0.56, and 0.15 for forward replay during early, middle, and late sessions, respectively). Red horizontal lines on columns represent chance levels calculated by permutation tests. Only correct trials are shown. See also Figure S6. 

Neuron 104, 1110–1125, December 18, 2019 1117 

**==> picture [60 x 60] intentionally omitted <==**

predict the actual taken future path (Figure 5H, right). A similar lack of prediction ability was seen for incorrect trials at the center well (Figures S6C and S6D). We therefore hypothesized that behaviorally relevant replayed trajectories are distinguished in networks outside the hippocampus, with PFC a likely candidate (Shin and Jadhav, 2016; Tang and Jadhav, 2019; Yu and Frank, 2015; Zielinski et al., 2017). 

## Coordinated Hippocampal-Prefrontal Replay 

## Distinguishes Past-Future Trajectory Sequences 

We therefore examined the relationship of coherent CA1-PFC replay of spatial paths (Tang et al., 2017) to ongoing behavioral trajectories. Similar to CA1 (Figure 1), PFC neurons exhibited spatially and directionally selective firing, and PFC ensembles formed unique spatial representations of trajectories for all sessions (Figure 6). PFC neurons have significantly lower spatial specificity and multi-peaked fields as compared with CA1 neurons (Jadhav et al., 2016; Tang et al., 2017; Yu et al., 2018; Zielinski et al., 2019), but PFC ensembles can still represent spatial location with high accuracy (Fujisawa et al., 2008; Mashhoori et al., 2018; Zielinski et al., 2019). Just as in CA1, although spatial stability and specificity of PFC cells increased across sessions (Figures S7A and S7B), spatial- and directional-selective firing was seen starting with the first novel track session (Figures 6A–6F), supporting accurate position decoding of individual trajectories (position reconstruction and confusion matrices in Figures 6C–6E; crossvalidated decoding error: 9.61 ± 0.21 cm in median ± SEM). Trajectory-dependent firing on the center arm was also observed in PFC cells (Baeg et al., 2003; Fujisawa et al., 2008; Ito et al., 2015), similar to CA1 splitter cells, and the fraction of PFC splitter cells did not significantly change over learning (Figure S7C). PFC ensembles thus uniquely represent different trajectories on the maze for all sessions (Tang et al., 2017; Zielinski et al., 2019). 

Prefrontal reactivation occurs during hippocampal SWRs (Benchenane et al., 2010; Jadhav et al., 2016; Peyrache et al., 2009) and we have previously reported coordinated CA1-PFC replay of spatial representations during awake SWRs (Tang et al., 2017). We therefore examined the relationship between coherent CA1-PFC replay and ongoing behavioral choices. Here, coherent CA1-PFC reactivation is defined as a CA1 replay event where the same trajectory is also significantly reactivated by CA1-PFC ensembles, detected as ‘‘reactivation strength’’ using a template matching method established in previous reports for hippocampal-cortical and -subcortical networks (Figures 7, S7, and S8; see STAR Methods; a comparison of the template matching method with Bayesian decoding and line-fitting methods is detailed in Figure S8) (Girardeau et al., 2017; Lansink et al., 2009; Peyrache et al., 2009; Tang et al., 2017). Using template spatial maps of CA1 and PFC neurons for candidate coherent replay events (R5 PFC and CA1 place cells active; Figures 7A–7D), we measured the reactivation strength of CA1-PFC ensembles during each candidate SWR event as the correlation of population activity during the SWR event and during running for each of the four possible trajectories. Illustrative coherent CA1-PFC replay events, with both forward and reverse CA1 replay, are shown in Figures 7A–7D. 

We found that coherent CA1-PFC reactivation (quantified as the fraction of coherent CA1-PFC replay events) was higher 

when CA1 replayed taken paths as compared to not-taken paths (Figure 7E). Crucially, measuring reactivation strength enabled us to compare the strength of coherent CA1-PFC replay when CA1 replayed either the behaviorally taken path, or the not-taken path, as a paired comparison with the corresponding alternative path during each event (see STAR Methods; for each replay event, CA1-PFC reactivation strength for either past or future trajectories was compared for the actually replayed CA1 trajectory versus that for the alternative trajectory). Using this measure for correct trials, we found that coherent CA1-PFC reactivation was significantly stronger when CA1 replayed the actual taken paths as compared with the alternative trajectory, but not when CA1 replayed the not-taken paths (Figure 7F; effect seen at both center and side wells). This stronger coherent CA1-PFC replay for behaviorally actualized trajectories was true for both forward CA1 replay of future taken paths, as well as reverse CA1 replay of past taken paths (Figure 7G). 

Coherent CA1-PFC replay can thus distinguish, through stronger reactivation, actual (i.e., behaviorally instantiated) past and future paths during reverse and forward CA1 replay, respectively (Figures 7E–7G), suggesting differential PFC coupling based on CA1 replay content. This was not a result of any difference in average activation probabilities or firing rates of PFC neurons for taken versus not-taken paths (Figure S7E), or difference in CA1 replay quality (Figure S7F). Further, this differential PFC coupling was not detected for incorrect outbound trials originating at the center well (Figures 7F and 7G, right panels). Finally, we also found a significant positive correlation between higher CA1-PFC reactivation (Figures S7J–S7L) and the peak working-memory performance levels achieved by each animal, but, surprisingly, a negative correlation for CA1 reactivation that can partially be attributed to longer immobility times and disengagement periods (Figures S7M and S7N). This is suggestive of a relationship between stronger coherent CA1-PFC replay and better memory performance on the task. 

## DISCUSSION 

Our results provide novel insights into the role of replay and suggest a role of coordinated hippocampal-prefrontal replay in spatial learning and memory-guided decision making. Continuous tracking of replay over the course of spatial choice learning revealed an association of reverse replay with retrospective evaluation of possible past paths leading to goals, and that of forward replay with prospective planning of available future choices toward goals. Further, these findings reveal dynamic changes in functional roles of replay depending on the learning stage and a mechanism of coherent hippocampal-prefrontal replay for learning and performance of spatial memory tasks. 

Previous studies have established a causal role of awake replay in W-maze learning (Ferna´ ndez-Ruiz et al., 2019; Jadhav et al., 2012), but how replay supports such memory tasks is not clear; neither are the specific roles of reverse and forward replay, which have been primarily reported on linear-trajectory tracks with a single back-and-forth path between reward wells (Ambrose et al., 2016; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006). Singer et al. (2013) reported that CA1 co-activity during SWRs was enhanced prior to correct trials during initial 

1118 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [476 x 450] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>C<br>D E<br>F<br>**----- End of picture text -----**<br>


Figure 6. Spatial Coding and Distinct Representations of Behavioral Trajectories by Prefrontal Ensembles (A) Spatial maps of all PFC cells (n = 154) recorded from 6 rats continuously across 8 learning sessions (E1–8). Data are presented as Figure 1C. Note that mirrorimage patterns between pairs of trajectories on each row reflect path equivalent properties of PFC neurons (Yu et al., 2018). (B) Spatial maps of all PFC cells (n = 38) recorded from an example animal in the first and last sessions. (C and D) Position reconstruction based on PFC ensemble spiking from the example animal in (B) during active running. Decoding performance was estimated using leave-one-out cross-validation. (C) Confusion matrices (estimated versus true position). (D) Estimated position probabilities. Cyan line: actual animal trajectory. Data are presented as Figures 1D and 1E. (E) Cumulative PFC decoding errors across all animals (n = 6 rats). Dashed lines: individual animals; red line: all animals; solid black line: the example animal shown in (B)–(D). Median error of all sessions (vertical red line) noted on top. Decoding error: 14.58 ± 0.63 cm for session 1, 8.99 ± 0.57 cm for session 8 (in median ± SEM). 

(F) Population vector overlap (PVO) of PFC population activity in two running directions across 8 learning sessions. Data are presented as in Figure 1H. Note that the spatial maps of PFC population in two running directions became less similar across sessions, but distinct templates for each direction were apparent in the first session (p < 0.0001 compared to the shuffled data for individual rats, trial-label permutation tests). See also Figure S7. 

Neuron 104, 1110–1125, December 18, 2019 1119 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [384 x 440] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>C D<br>E F G<br>**----- End of picture text -----**<br>


**==> picture [79 x 112] intentionally omitted <==**

**==> picture [73 x 41] intentionally omitted <==**

**==> picture [79 x 113] intentionally omitted <==**

**==> picture [75 x 46] intentionally omitted <==**

**==> picture [480 x 76] intentionally omitted <==**

Figure 7. Coherent Hippocampal-Prefrontal Replay of Past and Future Trajectories (A–D) Four examples of coherent CA1-PFC reactivation of future and past taken paths. (A) CA1-PFC reactivation of future taken path at the left well; (B) CA1-PFC reactivation of past taken path at the center well; (C) CA1-PFC reactivation of past taken path at the left well; (D) CA1-PFC reactivation of past taken path at the center well. (i) Linearized CA1-PFC spatial-map template with cell IDs on y axis (left) and the corresponding raster plot during the SWR (right). (ii) Detailed view of CA1-PFC coordination during RUN and the SWR using example cells. Left (RUN): the spiking pattern from a single running trial (ticks) with linearized spatial maps obtained by averaging over all trials (overlaid lines). Right (SWR): spikes (ticks) during the SWR and the response curves (overlaid lines) created by smoothing observed spikes with a Gaussian kernel. Arrowheads indicate the peak locations. (iii) CA1 trajectory replay, with data presented as in Figure 5A. Green circle: animal’s current position; black arrowhead line: trajectory taken; colored dots: decoded CA1-replay path. (iv) Reactivation strength, measured as the correlation 

(legend continued on next page) 

1120 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [174 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
A B<br>**----- End of picture text -----**<br>


**==> picture [6 x 5] intentionally omitted <==**

**==> picture [6 x 5] intentionally omitted <==**

**==> picture [5 x 4] intentionally omitted <==**

**==> picture [5 x 5] intentionally omitted <==**

**==> picture [55 x 132] intentionally omitted <==**

**==> picture [53 x 49] intentionally omitted <==**

**==> picture [165 x 132] intentionally omitted <==**

Figure 8. Schematic: Hippocampal-Prefrontal Replay Supports Retrospection and Prospection for Learning and Planning in Spatial Memory-Guided Tasks 

(A) The role of hippocampal-prefrontal replay in learning history-independent, spatial reference-memory rules. (Ai) Past and future paths at side wells. (Aii–Aiii) Hippocampal replay dynamics over learning. (Aiv) Stronger coherent CA1-PFC replay of taken paths. 

(B) The role of hippocampal-prefrontal replay in learning history-dependent, spatial working-memory rules. (Bi) Past and future paths at the center well. (Bii-Biii) Persistent trends of hippocampal replay over learning. (Biv) Discrimination of taken paths by coherent CA1-PFC replay. 

learning in the W-maze, and this activity did not correspond to specific paths, although this study did not examine replay of place-cell sequences. These findings hint, in agreement with hypotheses from other studies (Gupta et al., 2010; Jadhav et al., 2012; Stella et al., 2019), that hippocampal replay may support an evaluative process, and target regions outside the hippocampus are necessary to link hippocampal replay to ongoing behavioral choices. Our results suggest a model (Figure 8) with differing roles of replay in (1) history-independent spatial reference-memory tasks, where hippocampal replay showed dynamic changes over learning; and (2) history-dependent spatial working-memory tasks, with a role of coherent hippocampalprefrontal replay in recall of actual past experiences to guide planning of future choices. 

At the side wells, replay showed a shift from reverse-replaybased prediction of past path during early learning, to forwardreplay-based prediction of future path during late performance (Figure 8A). Reverse and forward hippocampal replay of past and future paths are in agreement with observations for deterministic spatial tasks (i.e., pre-determined correct paths between reward wells) on linear-trajectory tracks (Ambrose et al., 2016; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006; Wu et al., 2017). Our findings reveal a learning gradient for the role of replay in spatial reference memory, where the correct path to goal depends only on the animal’s current location, and indicate that with repeated experience of the same inbound return-to-center trajectory, forward replay prediction of future path leading to reward (Pfeiffer and Foster, 2013; Xu et al., 

coefficient of CA1-PFC activity during RUN versus SWR using template matching, for four possible trajectories (trajectory schematic on the bottom; red for CA1-replayed path, black for alternative path, blue for the other paths). Blue horizontal lines on columns represent 95% confidence intervals computed from shuffled data (SWR spike time shuffle). Selected PFC cells with highest contribution to the reactivation strength are shown for ease of presentation, illustrating the synchronized firing pattern for CA1-PFC cells during RUN, which is reactivated during the SWR event. 

(E) The proportion of coherent CA1-PFC reactivation events during correct trials is significantly higher during CA1 replay of taken versus not-taken trajectories (p = 0.02*, session-by-session rank-sum paired test). 

(F) Paired comparison of CA1-PFC reactivation strength for CA1-replay of taken versus alternative path during correct trials at center (left) and side (middle) wells and for incorrect trials (right). Note that during correct trials, CA1-PFC reactivation strength is significantly higher for the CA1-replayed path compared to its alternative (alter.), only when this replayed path was the behaviorally taken path at both center (p = 0.032*; n = 246 and 110 replay events for taken and not-taken, respectively) and side wells (p = 0.0075**; n = 244 and 212 replay events for taken and not-taken respectively), but not when the CA1-replayed path was the nottaken path (p = 0.35 and 0.16 for side and center wells, respectively; event-by-event rank-sum paired tests). This bias of CA1-PFC reactivation during correct trials is absent during incorrect trials (n = 49 and 56 replay events, and p = 0.20 and 0.96 for taken versus not-taken respectively; event-by-event rank-sum paired tests). (G) Left: stronger CA1-PFC reactivation of taken path compared to not-taken path during correct trials for both forward and reverse CA1 replay (p = 0.0058** and n = 215 events for forward replay of taken path; p = 0.039* and n = 275 events for reverse replay of taken path; event-by-event rank-sum paired tests). Right: during incorrect trials, CA1-PFC reactivation did not show significant difference for taken versus alternative path for either forward or reverse CA1 replay (p = 0.96 and n = 21 events for forward replay of taken path; p = 0.10 and n = 28 events for reverse replay of taken path; event-by-event rank-sum paired tests). See also Figures S7 and S8. 

Neuron 104, 1110–1125, December 18, 2019 1121 

**==> picture [60 x 60] intentionally omitted <==**

2019) emerges over learning, confirming previous hypotheses (Pfeiffer, 2017). Interestingly, disrupting SWR replay does not impair inbound learning (Jadhav et al., 2012), suggesting that other mechanisms can support this learning. 

Reverse replay at side wells supported retrospection of the past outbound (center-to-side) paths leading to reward. Notably, recall of this past path is not required for execution of the future inbound reference-memory path; rather, the observed reverse replay occurs at the completion of the outbound spatial working-memory trajectory and thus aligns with a role in working-memory updates, similar to previous reports in a radial-arm maze (Xu et al., 2019). Intriguingly, we found that the reverse bias toward taken past path to goals is present only during early learning and can thus play a role in temporal credit assignment during novel learning (Foster and Knierim, 2012; Haga and Fukai, 2018; Mattar and Daw, 2018). The observed loss of bias over learning (Figure 8A) suggests that this reinforcement is no longer required after task acquisition (Foster and Knierim, 2012). Finally, stronger CA1-PFC replay of taken (i.e., behaviorally actualized) paths at the side wells signifies that CA1-PFC replay of the future taken trajectory may support planning of the upcoming reference-memory trajectory, and that CA1-PFC replay of the past taken trajectory may support reinforcement of the completed working-memory path. 

In contrast, results at the center well indicate that hippocampal replay underlies a cognitive search role and not a predictive element, for execution of working-memory trajectories (Figure 8B). We found that the hippocampus persistently reverse-replayed both possible past choices and forward-replayed both available future choices throughout learning and performance. Replay of possible choices is indicative of a priming process for retrospective evaluation and prospective planning (Buzsa´ ki, 2015), underlying a cognitive exploration of possible paths (Redish, 2016; Singer et al., 2013; Stella et al., 2019) (Figure 8B). For individual hippocampal replay events, coherent CA1-PFC replay discriminates the behaviorally actualized past and future paths and can thus support planning of the future choice based on past experience. This PFC readout interpretation aligns with a bias toward CA1-leading-PFC directionality during replay (Jadhav et al., 2016; Rothschild et al., 2017). 

Our results thus suggest a mechanism by which replay supports acquisition and performance of spatial working memory tasks. Multiple paths to and from the center well underlie a nonMarkovian structure (Mattar and Daw, 2018), which requires animals to integrate across space and time to learn sequences of past and future choices that lead to reward (i.e., action-outcome associations). In our model, hippocampal reverse and forward replay underlie an evaluative process for retrospection and prospection, respectively, supporting a cognitive exploration of available paths that can be utilized by other networks for reinforcement learning and decision making. These processes involve prefrontal reactivation, since coherent CA1-PFC replay can distinguish behaviorally taken past and future paths in CA1 replay. It is important to point out that our experimental design enabled a rapid learning timescale, and it is possible that this replay role is not seen in repeatedly trained tasks, where other habitual systems can contribute to learning and performance (Kim and Frank, 2009; Packard and McGaugh, 1996). In addition, although PFC reactivation is known to occur during hippocampal SWRs 

(Khodagholy et al., 2017; Tang et al., 2017; Vaz et al., 2019), independent cortical reactivation cannot be ruled out (O’Neill et al., 2017). Further, since there is evidence that theta-mediated and SWR-mediated activity can play complementary roles in deliberation and cognition (Papale et al., 2016; Pezzulo et al., 2019; Redish, 2016), the relationship between theta- and SWR-mediated CA1-PFC interactions in memory-guided behavior (Gordon, 2011; Ito et al., 2015; Shin and Jadhav, 2016; Spellman et al., 2015) is an important avenue for future investigation. 

The suggested mechanism of hippocampal cognitive evaluation with differential coupling of prefrontal and other networks based on replay content has implications for neural mechanisms of model-based learning and planning, for spatial as well as nonspatial memories (Doll et al., 2012; Liu et al., 2019; Miller et al., 2017; Vikbladh et al., 2019). The results of this study also connect well to machine-learning literature based on hippocampal replay (Caze´ et al., 2018; Mattar and Daw, 2018) and thus may inspire improved algorithms. We hypothesize that replay in the awake state represents an internal cognitive state that engages a broad, multi-region network, similar to a default network mode (Buckner, 2010; Logothetis et al., 2012), to support ongoing learning, prospection, and abstraction. 

## STAR+METHODS 

Detailed methods are provided in the online version of this paper and include the following: 

- d KEY RESOURCES TABLE 

- d LEAD CONTACT AND MATERIALS AVAILABILITY d EXPERIMENTAL MODEL AND SUBJECT DETAILS 

- d METHOD DETAILS 

   - B The W-maze spatial memory task B Surgical implantation and electrophysiology B Unit inclusion 

   - B Behavioral state definition 

- d QUANTIFICATION AND STATISTICAL ANALYSIS 

   - B Sharp-wave ripple detection 

   - B Spatial maps 

   - B Place-field directionality 

   - B Trajectory-dependent firing 

   - B Bayesian decoding and replay detection 

   - B Replay prediction 

   - B CA1-PFC population reactivation analysis B Model simulations for reactivation analysis B CA1-PFC activation ratio and pairwise reactivation B Statistical analysis 

- d DATA AND CODE AVAILABILITY 

## SUPPLEMENTAL INFORMATION 

Supplemental Information can be found online at https://doi.org/10.1016/j. neuron.2019.09.012. 

## ACKNOWLEDGMENTS 

This work was supported by NIH grant R01 MH112661, a Sloan Research Fellowship in Neuroscience (Alfred P. Sloan Foundation), and a Whitehall Foundation award to S.P.J. 

1122 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

## AUTHOR CONTRIBUTIONS 

J.D.S. performed all experiments, W.T. designed and implemented all analyses, and S.P.J. conceived the study and supervised all aspects. All authors wrote the manuscript. 

## DECLARATION OF INTERESTS 

The authors declare no competing interests. 

Received: April 23, 2019 Revised: August 6, 2019 Accepted: September 6, 2019 Published: October 30, 2019 

## SUPPORTING CITATIONS 

The following references appear in the Supplemental Information: Dragoi and Tonegawa (2011); Dragoi and Tonegawa (2013); Farooq et al. (2019); Kapellush et al. (2018); Paxinos and Watson (2004). 

## REFERENCES 

Ainge, J.A., van der Meer, M.A., Langston, R.F., and Wood, E.R. (2007). Exploring the role of context-dependent hippocampal activity in spatial alternation behavior. Hippocampus 17, 988–1002. 

Ambrose, R.E., Pfeiffer, B.E., and Foster, D.J. (2016). Reverse replay of hippocampal place cells is uniquely modulated by changing reward. Neuron 91, 1124–1136. 

Baeg, E.H., Kim, Y.B., Huh, K., Mook-Jung, I., Kim, H.T., and Jung, M.W. (2003). Dynamics of population code for working memory in the prefrontal cortex. Neuron 40, 177–188. 

Benchenane, K., Peyrache, A., Khamassi, M., Tierney, P.L., Gioanni, Y., Battaglia, F.P., and Wiener, S.I. (2010). Coherent theta oscillations and reorganization of spike timing in the hippocampal- prefrontal network upon learning. Neuron 66, 921–936. 

Buckner, R.L. (2010). The role of the hippocampus in prediction and imagination. Annu. Rev. Psychol. 61, 27–48. 

Buzsa´ ki, G. (2015). Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. Hippocampus 25, 1073–1188. 

Carr, M.F., Jadhav, S.P., and Frank, L.M. (2011). Hippocampal replay in the awake state: a potential substrate for memory consolidation and retrieval. Nat. Neurosci. 14, 147–153. 

Caze´ , R., Khamassi, M., Aubin, L., and Girard, B. (2018). Hippocampal replays under the scrutiny of reinforcement learning models. J. Neurophysiol. 120, 2877–2896. 

Chang, C.-C., and Lin, C.-J. (2011). Libsvm. ACM Trans. Intell. Syst. Technol. 2, 1–27. 

Cheng, S., and Frank, L.M. (2008). New experiences enhance coordinated neural activity in the hippocampus. Neuron 57, 303–313. 

Davidson, T.J., Kloosterman, F., and Wilson, M.A. (2009). Hippocampal replay of extended experience. Neuron 63, 497–507. 

Diba, K., and Buzsa´ ki, G. (2007). Forward and reverse hippocampal place-cell sequences during ripples. Nat. Neurosci. 10, 1241–1242. 

Doll, B.B., Simon, D.A., and Daw, N.D. (2012). The ubiquity of model-based reinforcement learning. Curr. Opin. Neurobiol. 22, 1075–1081. 

Dragoi, G., and Tonegawa, S. (2011). Preplay of future place cell sequences by hippocampal cellular assemblies. Nature 469, 397–401. 

Dragoi, G., and Tonegawa, S. (2013). Selection of preconfigured cell assemblies for representation of novel spatial experiences. Philos. Trans. R. Soc. Lond. B Biol. Sci. 369, 20120522. 

Dupret, D., O’Neill, J., Pleydell-Bouverie, B., and Csicsvari, J. (2010). The reorganization and reactivation of hippocampal maps predict spatial memory performance. Nat. Neurosci. 13, 995–1002. 

Eichenbaum, H. (2017). Prefrontal-hippocampal interactions in episodic memory. Nat. Rev. Neurosci. 18, 547–558. 

Eichenbaum, H., and Cohen, N.J. (2004). From Conditioning to Conscious Recollection: Memory Systems of the Brain (Oxford University Press). 

Epstein, R.A., Patai, E.Z., Julian, J.B., and Spiers, H.J. (2017). The cognitive map in humans: spatial navigation and beyond. Nat. Neurosci. 20, 1504–1513. Euston, D.R., Tatsuno, M., and McNaughton, B.L. (2007). Fast-forward playback of recent memory sequences in prefrontal cortex during sleep. Science 318, 1147–1150. 

Farooq, U., and Dragoi, G. (2019). Emergence of preconfigured and plastic time-compressed sequences in early postnatal development. Science 363, 168–173. 

Farooq, U., Sibille, J., Liu, K., and Dragoi, G. (2019). Strengthened Temporal Coordination within Pre-existing Sequential Cell Assemblies Supports Trajectory Replay. Neuron 103, 719–733. 

Ferbinteanu, J., and Shapiro, M.L. (2003). Prospective and retrospective memory coding in the hippocampus. Neuron 40, 1227–1239. 

Ferbinteanu, J., Shirvalkar, P., and Shapiro, M.L. (2011). Memory modulates journey-dependent coding in the rat hippocampus. J. Neurosci. 31, 9135–9146. 

Ferna´ ndez-Ruiz, A., Oliva, A., Fermino de Oliveira, E., Rocha-Almeida, F., Tingley, D., and Buzsa´ ki, G. (2019). Long-duration hippocampal sharp wave ripples improve memory. Science 364, 1082–1086. 

Foster, D.J. (2017). Replay comes of age. Annu. Rev. Neurosci. 40, 581–602. Foster, D.J., and Knierim, J.J. (2012). Sequence learning and the role of the hippocampus in rodent navigation. Curr. Opin. Neurobiol. 22, 294–300. 

Foster, D.J., and Wilson, M.A. (2006). Reverse replay of behavioural sequences in hippocampal place cells during the awake state. Nature 440, 680–683. 

Frank, L.M., Brown, E.N., and Wilson, M. (2000). Trajectory encoding in the hippocampus and entorhinal cortex. Neuron 27, 169–178. 

Frank, L.M., Stanley, G.B., and Brown, E.N. (2004). Hippocampal plasticity across multiple days of exposure to novel environments. J. Neurosci. 24, 7681–7689. 

Fujisawa, S., Amarasingham, A., Harrison, M.T., and Buzsa´ ki, G. (2008). Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex. Nat. Neurosci. 11, 823–833. 

Girardeau, G., Inema, I., and Buzsa´ ki, G. (2017). Reactivations of emotional memory in the hippocampus-amygdala system during sleep. Nat. Neurosci. 20, 1634–1642. 

Gomperts, S.N., Kloosterman, F., and Wilson, M.A. (2015). VTA neurons coordinate with the hippocampal reactivation of spatial experience. eLife 4, e05360. 

Gordon, J.A. (2011). Oscillations and hippocampal-prefrontal synchrony. Curr. Opin. Neurobiol. 21, 486–491. 

Gupta, A.S., van der Meer, M.A., Touretzky, D.S., and Redish, A.D. (2010). Hippocampal replay is not a simple function of experience. Neuron 65, 695–705. 

Haga, T., and Fukai, T. (2018). Recurrent network model for learning goaldirected sequences through reverse replay. eLife 7, e34171. 

Ito, H.T., Zhang, S.J., Witter, M.P., Moser, E.I., and Moser, M.B. (2015). A prefrontal-thalamo-hippocampal circuit for goal-directed spatial navigation. Nature 522, 50–55. 

Jadhav, S.P., Kemere, C., German, P.W., and Frank, L.M. (2012). Awake hippocampal sharp-wave ripples support spatial memory. Science 336, 1454–1458. 

Jadhav, S.P., Rothschild, G., Roumis, D.K., and Frank, L.M. (2016). Coordinated excitation and inhibition of prefrontal ensembles during awake hippocampal sharp-wave ripple events. Neuron 90, 113–127. 

Joo, H.R., and Frank, L.M. (2018). The hippocampal sharp wave-ripple in memory retrieval for immediate use and consolidation. Nat. Rev. Neurosci. 19, 744–757. 

Neuron 104, 1110–1125, December 18, 2019 1123 

**==> picture [60 x 60] intentionally omitted <==**

Kapellusch, A.J., Lester, A.W., Schwartz, B.A., Smith, A.C., and Barnes, C.A. (2018). Analysis of learning deficits in aged rats on the W-track continuous spatial alternation task. Behav. Neurosci. 132, 512–519. 

Karlsson, M.P., and Frank, L.M. (2009). Awake replay of remote experiences in the hippocampus. Nat. Neurosci. 12, 913–918. 

Kay, K., Sosa, M., Chung, J.E., Karlsson, M.P., Larkin, M.C., and Frank, L.M. (2016). A hippocampal network for spatial coding during immobility and sleep. Nature 531, 185–190. 

Khodagholy, D., Gelinas, J.N., and Buzsa´ ki, G. (2017). Learning-enhanced coupling between ripple oscillations in association cortices and hippocampus. Science 358, 369–372. 

Kim, S.M., and Frank, L.M. (2009). Hippocampal lesions impair rapid learning of a continuous spatial alternation task. PLoS ONE 4, e5494. 

Kudrimoti, H.S., Barnes, C.A., and McNaughton, B.L. (1999). Reactivation of hippocampal cell assemblies: effects of behavioral state, experience, and EEG dynamics. J. Neurosci. 19, 4090–4101. 

Lansink, C.S., Goltstein, P.M., Lankelma, J.V., McNaughton, B.L., and Pennartz, C.M. (2009). Hippocampus leads ventral striatum in replay of place-reward information. PLoS Biol. 7, e1000173. 

Leonard, T.K., and Hoffman, K.L. (2017). Sharp-Wave Ripples in Primates Are Enhanced near Remembered Visual Objects. Curr. Biol. 27, 257–262. 

Leonard, T.K., Mikkila, J.M., Eskandar, E.N., Gerrard, J.L., Kaping, D., Patel, S.R., Womelsdorf, T., and Hoffman, K.L. (2015). Sharp Wave Ripples during Visual Exploration in the Primate Hippocampus. J. Neurosci. 35, 14771–14782. 

Li, Q., Ko, H., Qian, Z.M., Yan, L.Y.C., Chan, D.C.W., Arbuthnott, G., Ke, Y., and Yung, W.H. (2017). Refinement of learned skilled movement representation in motor cortex deep output layer. Nat. Commun. 8, 15834. 

Liu, Y., Dolan, R.J., Kurth-Nelson, Z., and Behrens, T.E.J. (2019). Human Replay Spontaneously Reorganizes Experience. Cell 178, 640–652. 

Logothetis, N.K., Eschenko, O., Murayama, Y., Augath, M., Steudel, T., Evrard, H.C., Besserve, M., and Oeltermann, A. (2012). Hippocampal-cortical interaction during periods of subcortical silence. Nature 491, 547–553. 

Maharjan, D.M., Dai, Y.Y., Glantz, E.H., and Jadhav, S.P. (2018). Disruption of dorsal hippocampal - prefrontal interactions using chemogenetic inactivation impairs spatial learning. Neurobiol. Learn. Mem. 155, 351–360. 

Mallory, C.S., Hardcastle, K., Bant, J.S., and Giocomo, L.M. (2018). Grid scale drives the scale and long-term stability of place maps. Nat. Neurosci. 21, 270–282. 

Mashhoori, A., Hashemnia, S., McNaughton, B.L., Euston, D.R., and Gruber, A.J. (2018). Rat anterior cingulate cortex recalls features of remote reward locations after disfavoured reinforcements. eLife 7, e29793. 

Mattar, M.G., and Daw, N.D. (2018). Prioritized memory access explains planning and hippocampal replay. Nat. Neurosci. 21, 1609–1617. 

Middleton, S.J., Kneller, E.M., Chen, S., Ogiwara, I., Montal, M., Yamakawa, K., and McHugh, T.J. (2018). Altered hippocampal replay is associated with memory impairment in mice heterozygous for the Scn2a gene. Nat. Neurosci. 21, 996–1003. 

Miller, K.J., Botvinick, M.M., and Brody, C.D. (2017). Dorsal hippocampus contributes to model-based planning. Nat. Neurosci. 20, 1269–1276. 

Navratilova, Z., Hoang, L.T., Schwindel, C.D., Tatsuno, M., and McNaughton, B.L. (2012). Experience-dependent firing rate remapping generates directional selectivity in hippocampal place cells. Front. Neural Circuits 6, 6. 

Norman, Y., Yeagle, E.M., Khuvis, S., Harel, M., Mehta, A.D., and Malach, R. (2019). Hippocampal sharp-wave ripples linked to visual episodic recollection in humans. Science 365, eaax1030. 

O’Keefe, J., and Nadel, L. (1978). The hippocampus as a cognitive map (Oxford University Press). 

O’Neill, J., Boccara, C.N., Stella, F., Schoenenberger, P., and Csicsvari, J. (2017). Superficial layers of the medial entorhinal cortex replay independently of the hippocampus. Science 355, 184–188. 

O[´ ] lafsdo´ ttir, H.F., Carpenter, F., and Barry, C. (2016). Coordinated grid and place cell replay during rest. Nat. Neurosci. 19, 792–794. 

O[´ ] lafsdo´ ttir, H.F., Carpenter, F., and Barry, C. (2017). Task Demands Predict a Dynamic Switch in the Content of Awake Hippocampal Replay. Neuron 96, 925–935. 

Packard, M.G., and McGaugh, J.L. (1996). Inactivation of hippocampus or caudate nucleus with lidocaine differentially affects expression of place and response learning. Neurobiol. Learn. Mem. 65, 65–72. 

Papale, A.E., Zielinski, M.C., Frank, L.M., Jadhav, S.P., and Redish, A.D. (2016). Interplay between hippocampal sharp-wave-ripple events and vicarious trial and error behaviors in decision making. Neuron 92, 975–982. 

Paxinos, G., and Watson, C. (2004). The Rat Brain in Stereotaxic Coordinates (Academic Press). 

Peyrache, A., Khamassi, M., Benchenane, K., Wiener, S.I., and Battaglia, F.P. (2009). Replay of rule-learning related neural patterns in the prefrontal cortex during sleep. Nat. Neurosci. 12, 919–926. 

Pezzulo, G., van der Meer, M.A., Lansink, C.S., and Pennartz, C.M. (2014). Internally generated sequences in learning and executing goal-directed behavior. Trends Cogn. Sci. 18, 647–657. 

Pezzulo, G., Donnarumma, F., Maisto, D., and Stoianov, I. (2019). Planning at decision time and in the background during spatial navigation. Curr. Opin. Behav. Sci. 29, 69–76. 

Pfeiffer, B.E. (2017). The content of hippocampal ‘‘replay’’. Hippocampus. Published online December 20, 2017. https://doi.org/10.1002/hipo.22824. 

Pfeiffer, B.E., and Foster, D.J. (2013). Hippocampal place-cell sequences depict future paths to remembered goals. Nature 497, 74–79. 

Ramirez-Villegas, J.F., Logothetis, N.K., and Besserve, M. (2015). Diversity of sharp-wave-ripple LFP signatures reveals differentiated brain-wide dynamical events. Proc. Natl. Acad. Sci. USA 112, E6379–E6387. 

Ravassard, P., Kees, A., Willers, B., Ho, D., Aharoni, D.A., Cushman, J., Aghajan, Z.M., and Mehta, M.R. (2013). Multisensory control of hippocampal spatiotemporal selectivity. Science 340, 1342–1346. 

Redish, A.D. (2016). Vicarious trial and error. Nat. Rev. Neurosci. 17, 147–159. Rothschild, G., Eban, E., and Frank, L.M. (2017). A cortical-hippocampalcortical loop of information processing during memory consolidation. Nat. Neurosci. 20, 251–259. 

Schmitzer-Torbert, N., Jackson, J., Henze, D., Harris, K., and Redish, A.D. (2005). Quantitative measures of cluster quality for use in extracellular recordings. Neuroscience 131, 1–11. 

Shin, J.D., and Jadhav, S.P. (2016). Multiple modes of hippocampal-prefrontal interactions in memory-guided behavior. Curr. Opin. Neurobiol. 40, 161–169. 

Singer, A.C., and Frank, L.M. (2009). Rewarded outcomes enhance reactivation of experience in the hippocampus. Neuron 64, 910–921. 

Singer, A.C., Carr, M.F., Karlsson, M.P., and Frank, L.M. (2013). Hippocampal SWR activity predicts correct decisions during the initial learning of an alternation task. Neuron 77, 1163–1173. 

Smith, A.C., Frank, L.M., Wirth, S., Yanike, M., Hu, D., Kubota, Y., Graybiel, A.M., Suzuki, W.A., and Brown, E.N. (2004). Dynamic analysis of learning in behavioral experiments. J. Neurosci. 24, 447–461. 

Spellman, T., Rigotti, M., Ahmari, S.E., Fusi, S., Gogos, J.A., and Gordon, J.A. (2015). Hippocampal-prefrontal input supports spatial encoding in working memory. Nature 522, 309–314. 

Squire, L.R. (1992). Memory and the hippocampus: a synthesis from findings with rats, monkeys, and humans. Psychol. Rev. 99, 195–231. 

Stella, F., Baracskay, P., O’Neill, J., and Csicsvari, J. (2019). ). Hippocampal Reactivation of Random Trajectories Resembling Brownian Diffusion. Neuron 102, 450–461. 

Sullivan, D., Csicsvari, J., Mizuseki, K., Montgomery, S., Diba, K., and Buzsa´ ki, G. (2011). Relationships between hippocampal sharp waves, ripples, and fast gamma oscillation: influence of dentate and entorhinal cortical activity. J. Neurosci. 31, 8605–8616. 

1124 Neuron 104, 1110–1125, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

Tang, W., and Jadhav, S.P. (2019). Sharp-wave ripples as a signature of hippocampal-prefrontal reactivation for memory during sleep and waking states. Neurobiol. Learn. Mem. 160, 11–20. 

Tang, W., Shin, J.D., Frank, L.M., and Jadhav, S.P. (2017). Hippocampal-prefrontal reactivation during learning is stronger in awake compared with sleep states. J. Neurosci. 37, 11789–11805. 

Trimper, J.B., Trettel, S.G., Hwaun, E., and Colgin, L.L. (2017). Methodological caveats in the detection of coordinated replay between place cells and grid cells. Front. Syst. Neurosci. 11, 57. 

Vaz, A.P., Inati, S.K., Brunel, N., and Zaghloul, K.A. (2019). Coupled ripple oscillations between the medial temporal lobe and neocortex retrieve human memory. Science 363, 975–978. 

Vikbladh, O.M., Meager, M.R., King, J., Blackmon, K., Devinsky, O., Shohamy, D., Burgess, N., and Daw, N.D. (2019). Hippocampal Contributions to ModelBased Planning and Spatial Memory. Neuron 102, 683–693. 

Wilber, A.A., Skelin, I., Wu, W., and McNaughton, B.L. (2017). Laminar Organization of Encoding and Memory Reactivation in the Parietal Cortex. Neuron 95, 1406–1419. 

Wood, E.R., Dudchenko, P.A., Robitsek, R.J., and Eichenbaum, H. (2000). Hippocampal neurons encode information about different types of memory episodes occurring in the same location. Neuron 27, 623–633. 

Wu, C.-T., Haggerty, D., Kemere, C., and Ji, D. (2017). Hippocampal awake replay in fear memory retrieval. Nat. Neurosci. 20, 571–580. 

Xu, H., Baracskay, P., O’Neill, J., and Csicsvari, J. (2019). Assembly Responses of Hippocampal CA1 Place Cells Predict Learned Behavior in Goal-Directed Spatial Tasks on the Radial Eight-Arm Maze. . Neuron 101, , 119–132.. 

Yu, J.Y., and Frank, L.M. (2015). Hippocampal-cortical interaction in decision making. Neurobiol. Learn. Mem. 117, 34–41. 

Yu, J.Y., Liu, D.F., Loback, A., Grossrubatscher, I., and Frank, L.M. (2018). Specific hippocampal representations are linked to generalized cortical representations in memory. Nat. Commun. 9, 2209. 

Zielinski, M.C., Tang, W., and Jadhav, S.P. (2017). The role of replay and theta sequences in mediating hippocampal-prefrontal interactions for memory and cognition. Hippocampus. Published online December 18, 2017. https://doi. org/10.1002/hipo.22821. 

Zielinski, M.C., Shin, J.D., and Jadhav, S.P. (2019). Coherent Coding of Spatial Position Mediated by Theta Oscillations in the Hippocampus and Prefrontal Cortex. J. Neurosci. 39, 4550–4565. 

Neuron 104, 1110–1125, December 18, 2019 1125 

**==> picture [60 x 60] intentionally omitted <==**

## STAR+METHODS 

## KEY RESOURCES TABLE 

|REAGENT or RESOURCE|SOURCE|SOURCE|IDENTIFIER|
|---|---|---|---|
|||||
|Chemicals||||
|Cresyl Violet|~~A~~cros Organics||Cat#: AC229630050|
|Formaldehyde|~~F~~isher||~~C~~at#: 50-00-0,67561,7732-18-5|
|Isofurane|~~P~~atterson Veterinary||Cat#: 07-806-3204|
|Ketamine|~~P~~atterson Veterinary||Cat#: 07-803-6637|
|Xylazine|~~P~~atterson Veterinary||Cat#: 07-808-1947|
|Atropine|~~P~~atterson Veterinary||Cat#: 07-869-6061|
|Bupivacaine|~~P~~atterson Veterinary||Cat#: 07-890-4881|
|Beuthanasia-D|~~P~~atterson Veterinary||Cat#: 07-807-3963|
|Sucrose|~~S~~igma-Aldrich||~~C~~at#: S8501-5KG|
|Experimental Models: Organisms/Strains||||
|Rat: LongEvans|~~C~~harles River||Cat#: Crl:LE 006;RRID: RGD_2308852|
|Software and Algorithms||||
|MATLAB 2017a|~~M~~athworks, MA||RRID: SCR_001622|
|Trodes|~~S~~pikeGadgets||~~h~~ttp://www.spikegadgets.com|
|Matclust|Mattias P. Karlsson||https://www.mathworks.com/matlabcentral/<br>~~f~~leexchange/39663-matclust, V1.7|
|Libsvm|~~C~~hang and Lin 2011||https://www.csie.ntu.edu.tw/�cjlin/libsvm/, V3.12|
|Chronux|~~P~~artha Mitra||~~h~~ttp://chronux.org/, V2.12|
|Prism 8|~~G~~raphPad Software||RRID: SCR_002798|
|Other||||
|128 Channel electrophysiology data acquisition<br>system<br>SpikeGadgets|||http://www.spikegadgets.com|
|12.7mm NiCr tetrode wire<br>Sandvik|||Cat#: PX000004|



## LEAD CONTACT AND MATERIALS AVAILABILITY 

Further information and requests for resources and reagents should be directed to the Lead Contact, Shantanu P. Jadhav (shantanu@brandeis.edu). This study did not generate new unique reagents. 

## EXPERIMENTAL MODEL AND SUBJECT DETAILS 

All procedures were approved by the Institutional Animal Care and Use Committee at the Brandeis University and conformed to US National Institutes of Health guidelines. Six adult male Long-Evans rats (450-550 g, 4-6 months; RRID: RGD_2308852) were used in this study. Animals were individually housed and kept on a 12-hr regular light/dark cycle. 

## METHOD DETAILS 

## The W-maze spatial memory task 

Animals learned a novel W-maze continuous spatial alternation task within a single day. During this experimental day, all animals ran eight 15-20 min sessions on a W-maze interleaved with 20-30 min rest sessions in a sleep box (W-maze sessions: 17.9 ± 1.0 mins per session, 8 sessions per rat; rest sessions: 23.0 ± 4.9 mins per session, 9 sessions per rat; total recording duration: 6.04 ± 0.37 hr per rat; mean ± SD). The W-maze was novel in the first behavioral session (sleep box was opaque, and the animal had no visibility of the W-maze until it was introduced in the first run session), and had dimensions of �80 3 80 cm with �7-cm-wide track sections. Three reward food wells (i.e., right, center, and left wells) were located at the end of three arms of the W-maze (Figure 1). Calibrated 

e1 Neuron 104, 1110–1125.e1–e7, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

evaporated milk reward was automatically delivered in the reward wells triggered by crossing of an infrared beam by the animal’s nose. Rewards were delivered according to the following rules (Figure 1A): returning to the center well after visits to either side well (inbound trajectories), and choosing the opposite side well from the previously visited side well when starting from the center well (outbound trajectories). Incorrect alternations (visiting the same side well in consecutive outbound components – outbound error), or incorrect side-to-side well visits (without visiting the center arm – inbound error) were not rewarded. Repeated visits to the same well were also not rewarded (i.e., turn-around error). Therefore, animals performed four types of trajectories during correct behavioral sequences (Figure 1A): center-to-right (C-to-R), right-to-center (R-to-C), center-to-left (C-to-L) and left-to-center (L-to-C). Among these trajectory types, C-to-R and C-to-L are outbound trajectories, while R-to-C and L-to-C are inbound trajectories. When animals paused at one reward well during correct trials, two of these four trajectory types represented the immediate past and future paths taken, and the other two represented the alternative not-taken paths (Figure 1B). For visualization purposes, the alternative, not-taken trajectories corresponding to a taken behavioral sequence were selected from the adjacent trials (e.g., Figure 3D). Only behaviorally correct trials were included for replay and reactivation analyses, unless otherwise specified. At the end of each W- maze session, animals were transferred to a black opaque box for rest (�30 3 30 cm with a 50-cm high wall). The raw performance of the task was calculated as proportion correct (Singer et al., 2013) (Figure 4A), and the learning curves were estimated using a statespace model (Jadhav et al., 2012; Smith et al., 2004) (Figure S1H). Each animal’s maximal performance level (Figures S7M and S7N) was measured as the highest performance reached on the outbound learning curve (Figure S1H). All 6 animals performed > 80% correct in the W-maze task toward the end of learning (maximal proportion correct of outbound for individual animals: 91.2 ± 4.1%; mean ± SD). 

## Surgical implantation and electrophysiology 

Surgical implantation procedures were as previously described (Jadhav et al., 2012; Jadhav et al., 2016; Tang et al., 2017). Animals were implanted with a microdrive array containing 30-32 independently moveable tetrodes targeting right dorsal hippocampal region � CA1 ( 3.6 mm AP and 2.2 mm ML) and right PFC (+3.0 mm AP and 0.7 mm ML). On the days following surgery, hippocampal tetrodes were gradually advanced to the desired depths using characteristic EEG patterns (sharp wave polarity, theta modulation) and neural firing patterns as previously described (Jadhav et al., 2012; Jadhav et al., 2016). One tetrode in corpus callosum served as hippocampal reference, and another tetrode in overlying cortical regions with no spiking signal served as prefrontal reference. A ground (GND) screw installed in skull overlying cerebellum also served as a reference. All spiking activity and ripple-filtered LFPs (150-250 Hz; see below) were recorded relative to the local reference tetrode. Electrodes were not moved at least 4 h before and during the recording day. 

Data were collected using a SpikeGadgets data acquisition system (SpikeGadgets LLC) (Tang et al., 2017). Spike data were sampled at 30 kHz and bandpass filtered between 600 Hz and 6 kHz. LFPs were sampled at 1.5 kHz and bandpass filtered between 0.5 Hz and 400 Hz. The animal’s position and running speed were recorded with an overhead color CCD camera (30 fps) and tracked by color LEDs affixed to the headstage. 

Spiking activity was continuously monitored during the experimental day for �6-7 hr. This design enabled us to link replay dynamics to behavioral learning, without the possible confound that different ensembles were monitored in different learning stages. Single units were identified by manual clustering based on peak and trough amplitude, principal components, and spike width using custom software (MatClust, M. P. Karlsson) as previously described (Jadhav et al., 2016; Tang et al., 2017). Only well isolated neurons with stable spiking waveforms and stable clusters across sessions were included – clusters that split or merged across sessions were discarded (Figure S1). Cluster quality was measured using isolation distance (Schmitzer-Torbert et al., 2005) and cluster center-ofmass shift (Mallory et al., 2018), and also assessed using spike-waveform correlation (Li et al., 2017) (Figure S1). Cluster center-ofmass shift between two different sessions was calculated as the Mahalanobis distance between the cluster centroids of the same single unit from these sessions. The spike-waveform correlation was quantified as the correlation coefficient between averaged spike waveforms of the same single unit from two consecutive sessions, and the resulting correlation was Fisher-transformed to make it normally distributed (Li et al., 2017). 

## Unit inclusion 

Units included in analyses fired at least 100 spikes in each session. Putative interneurons were identified and excluded based on spike width and firing rate criterion as previously described (Jadhav et al., 2016; Tang et al., 2017). Peak rate for each unit was defined as the maximum rate across all spatial bins in the linearized spatial map (see Spatial Maps). A peak rate R 3 Hz was required for a cell to be considered as a place cell. Only cells recorded continuously across all 8 behavioral sessions with stable spiking waveforms were analyzed (Figure S1). All manually clustered units included satisfied at least one of the cluster-quality criteria described above, and a majority of cells (98.6%, 213/216 for CA1 and 98.1%, 151/154 for PFC) met the thresholds for the primary criteria of isolation distance and center-of-mass shift. 93.1% (201/216) CA1 and 94.8% (146/154) PFC units met all 3 criteria, including spike-waveform correlation (Figures S1F and S1G). 

## Behavioral state definition 

Movement or exploratory states were defined as periods with running speed > 5 cm/s, whereas immobility was defined as periods with speed % 4 cm/s. The animal’s arrival and departure at a reward well was detected by an infrared beam triggered at the well. The 

Neuron 104, 1110–1125.e1–e7, December 18, 2019 e2 

**==> picture [60 x 60] intentionally omitted <==**

well entry was further refined as the first time point when the speed fell below 4 cm/s before the arrival trigger, whereas the well exit was defined as the first time point when the speed rose above 4 cm/s after the departure trigger (Figure 3A). The animal’s time spent at a reward well (i.e., immobility period at well) was defined as the period between the well entry and exit. For trials with an immobility duration at a reward well longer than 6 s, the total time spent at the well was equally divided into 4 parts; the first and last parts were defined as engaged periods, and the rest were considered as disengaged (Figures S4G–S4I; O[´ ] lafsdo´ ttir et al., 2017). 

## QUANTIFICATION AND STATISTICAL ANALYSIS 

## Sharp-wave ripple detection 

SWRs were detected as described previously during immobility periods (%4 cm/s) (Jadhav et al., 2016; Karlsson and Frank, 2009; Tang et al., 2017). In brief, LFPs from CA1 tetrodes were filtered into the ripple band (150-250 Hz), and the envelope of the ripplefiltered LFPs was determined using a Hilbert transform. SWRs were initially detected as contiguous periods when the envelope stayed above 3 SD of the mean on at least one tetrode, and further refined as times around the initially detected events during which the envelope exceeded the mean. The amplitude of a SWR event was defined in terms of exceeded SDs above the mean as described previously (Figure S5A) (Tang et al., 2017). To determine the frequency of a SWR event, we first estimated the spectrogram of peri-event CA1 LFPs around the SWR onset using multi-taper time-frequency analysis (Chronux toolbox; http://chronux.org/), and the power at each frequency band was individually z-scored across a given session. The frequency of this event was then defined as the frequency with the highest power within the ripple band (100-250 Hz) during the event (Middleton et al., 2018; Ramirez-Villegas et al., 2015; Sullivan et al., 2011). For replay and reactivation analysis (see below, Replay Prediction and CA1-PFC Population Reactivation Analysis), only SWRs with a duration R 50 ms were included, similar to previous studies (Pfeiffer and Foster, 2013; Wu et al., 2017). 

## Spatial maps 

Spatial maps were calculated only during movement periods (> 5 cm/s; all SWR times excluded) at positions with sufficient occupancy (> 20 ms). Two-dimensional occupancy-normalized spatial rate maps were calculated as previously described (Jadhav et al., 2012; Jadhav et al., 2016; Tang et al., 2017). To construct the spatial-map templates of different trajectory types on a W-maze (Figure 1C), we calculated the linearized activity of each cell as previously described (Jadhav et al., 2012; Jadhav et al., 2016; Karlsson and Frank, 2009; Singer et al., 2013). The rat’s linear position was estimated by projecting its actual 2D position onto pre-defined idealized paths along the track, and was further classified as belonging to one of the four trajectory types. The linearized spatial maps were then calculated using spike counts and occupancies calculated in 2-cm bins of the linearized positions and smoothened with a Gaussian curve (4-cm SD) as previously described (Jadhav et al., 2012; Tang et al., 2017). To cross-validate the linearized positions, an alternative linearization method was also used based on nearest-neighbor Delaunay triangulation (Ferbinteanu et al., 2011). Completed trials detected based on both methods, i.e., linearized trajectories starting from and ending at reward wells, were used for replay and reactivation analyses. 

To quantify spatial coverage of place-cell populations, a spatial bin was considered as represented if at least one cell from the population had an occupancy-normalized rate R 3 Hz within the bin (Kay et al., 2016; Zielinski et al., 2019). The spatial coverage of the population was then expressed as the percentage of the spatial bins covered. Across the populations of recorded place cells, we found place fields at all positions along each trajectory type (spatial coverage per subject over sessions, shown as mean ± SD: 99.9 ± 0.1%, 99.4 ± 0.8%, 97.4 ± 2.1%, 99.5 ± 0.8%, 91.5 ± 9.3%, 96.2 ± 1.6%; n = 6 rats; see also Figures 1C and S4J). The stability of spatial maps was defined as the correlation between the linearized maps for all 4 trajectory types for two consecutive behavioral sessions (Figures S2A and S7A) (Jadhav et al., 2012). In addition, we calculated the correlation after shuffling the cell identity among all other simultaneously recorded cells in the latter session, and compared this shuffled measure to the actual correlation. The specificity of spatial maps was measured as (1 – spatial sparsity), where spatial sparsity is calculated as a fraction of linearized place field with a firing rate > 25% of its peak rate (Figures S2B and S7B) (Jadhav et al., 2016; Tang et al., 2017). 

## Place-field directionality 

For each place cell, a directionality index (DI) was calculated based on firing rates in the preferred (FRpref) and non-preferred (FRnpref) running directions of the left or right trajectories (Figure 1G) as (FRpref - FRnpref) / (FRpref + FRnpref), similar to previous studies (Navratilova et al., 2012; Ravassard et al., 2013). A directionality index of 0 indicates identical firing in both directions, whereas 1 indicates firing in one direction only. The similarity of the place-field population in two running directions was computed using the population vector overlap (PVO; Figures 1H and 6F) (Ravassard et al., 2013). The population vector (PV) was the activity vector of all place cells in a certain linear position bin. The PVO was defined as the vector dot product between the PVs across all linear positions in two running directions: 

**==> picture [182 x 39] intentionally omitted <==**

e3 Neuron 104, 1110–1125.e1–e7, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

where FRf,i(x) is the firing rate of the i-th place cell at the linear position x along the track in a forward running direction, and FRb,i(x) is for the backward running direction. The PVO ranges from 0 to 1, with 1 representing identical population place-field templates in two running directions. To determine the significance values for the PVO and DI, we created 1,000 shuffle surrogates by randomly shuffling running directions from trial to trial, and computed PVO and DI from the shuffled data. Unidirectional cells were defined as cells with a DI significantly higher than its shuffle surrogates (p < 0.05; See Table S1 for the number of unidirectional cells of each animal, and Figure S4A for replay analysis using the unidirectional cells). 

## Trajectory-dependent firing 

It has been shown that the spatial maps of both CA1 (Ainge et al., 2007; Ferbinteanu and Shapiro, 2003; Frank et al., 2000; Wood et al., 2000) and PFC (Baeg et al., 2003; Fujisawa et al., 2008; Ito et al., 2015) cells on the center stem of spatial mazes can discriminate among different trial types in the same running direction, termed ‘‘splitter cells’’. For cells with robust fields (> 2 Hz) on the center stem of the W-maze, we further analyzed their trajectory-dependent firing. The firing rate was calculated in 2-cm bins of the linearized positions on the stem and smoothened with a Gaussian curve (3-cm SD) for each trial, and then the firing rate difference between different trajectories was compared (i.e., center-to-left versus center-to-right outbound trajectories, and left-to-center versus right-to-center inbound trajectories) as firing rate (FR) index: 

**==> picture [126 x 38] intentionally omitted <==**

where FRL(i) is the firing rate in the i-th spatial bin on the stem during left trials (i.e., center-to-left trial for outbound, or left-to-center trial for inbound), and FRR(i) is for the right trials. To assess significance, the trial labels (left or right) were randomly shuffled 1,000 times, and cells with a FR index significantly higher than its shuffle surrogates (p < 0.05) were defined as splitter or trajectory-dependent cells (Figures S4B and S7C). Note that the method here is less conservative than that used in some previous studies for defining ‘‘splitter cells’’ (e.g., parameters such as running speed could potentially contribute to the differential firing; Ito et al., 2015; Wood et al., 2000), since we only used trajectory-dependent firing of center-stem cells to assess their contribution to templates for different replay sequences. Note that most replay events identified comprised at least two side-arm cells (Figures S4C, S4D, S6A, and S6B), which were defined as the cells that have the firing rate peak past the choice point and outside the center arm (Ferna´ ndez-Ruiz et al., 2019; Singer et al., 2013). 

## Bayesian decoding and replay detection 

Bayesian decoding of spatial location and replay was implemented as previously described (Ambrose et al., 2016; Davidson et al., 2009; Karlsson and Frank, 2009; Tang et al., 2017). A memoryless Bayesian decoder was built for each of the four trajectory types to estimate the probability of animals’ position given the observed spikes (Bayesian reconstruction; or posterior probability matrix): P(X, trj spikes) = P(spikesj X, tr)P(X, tr)/P(spikes), where X is the set of all linear positions on the track for different trajectory types (tr ˛ {center-to-right, right-to-center, center-to-left, left-to-center}), and we assumed a uniform prior probability over X and tr. Assuming that all N place cells active during a candidate event fired independently and followed a Poisson process: 

**==> picture [260 x 22] intentionally omitted <==**

where t is the duration of the time window (i.e., 10 ms for replay events, and 500 ms for active behavior), fi(X,tr) is the expected firing rate of the i-th cell as a function of sampled location X and trial type tr, and spikesi is the number of spikes of the i-th cell in a given time window. Therefore, the posterior probability matrix can be derived as follows: 

**==> picture [196 x 19] intentionally omitted <==**

## where C is a normalization constant. 

This Bayesian decoding algorithm was used to estimate the animal’s location during active running (speed > 5 cm/s) (Figures 1 and 6), similar to previous studies (Ambrose et al., 2016; Davidson et al., 2009; Farooq and Dragoi, 2019; O[´ ] lafsdo´ ttir et al., 2017). To decode spatial location during running, the population activity was binned into 500-ms non-overlapping bins. Decoding performance was estimated using a leave-one-out cross-validation as follows. For the trial that was chosen to be decoded (i.e., test data), the rest of the trials (i.e., training data) were used to estimate the spatial maps f(X,tr). For each time bin of the test trial, the location with maximum decoded probability was compared to the actual position of the animal in that bin, and decoding error in this bin was determined as the linear distance between estimated position and actual position. This procedure was repeated for all trials to be tested. 

We identified replay during SWRs based on the Bayesian decoder described above. First, candidate events were defined as the SWR events during which R 5 place cells fired. Each candidate event was then divided into 10-ms non-overlapping bins, and the spatial probability distribution (i.e., posterior probability matrix) was computed based on the Bayes’ rule. The assessment of replay events for significance was implemented as previously described (Karlsson and Frank, 2009). The p value was calculated based on a 

Neuron 104, 1110–1125.e1–e7, December 18, 2019 e4 

**==> picture [60 x 60] intentionally omitted <==**

Monte Carlo shuffle. First, we drew 10,000 random samples from the posterior probability matrix for each decoded bin and assigned the sampled locations to that bin. Then, we performed a linear regression on the bin number versus the location points. The resulting R-squared was compared with 1,500 regressions, in which the order of the temporal bins was shuffled (i.e., time shuffle) (Foster, 2017; Trimper et al., 2017). A candidate event with p < 0.05 based on the time shuffle was considered as a replay event. Since the shuffling procedure measured how well the decoded positions along SWR time matched a behavioral trajectory, we considered the trajectory with the lowest p value from the shuffling procedure as the replay trajectory (instead of the one with the highest summed posterior probability) (Tang et al., 2017), and its R-squared (or r) was reported as replay quality. Since there was a bias toward reward locations for place cells and their associated replay events (Figures S4J and S4L), similar to previous reports (Davidson et al., 2009; Dupret et al., 2010; Pfeiffer and Foster, 2013), we excluded the spatial positions within 15 cm of reward wells from the place-field templates to detect replay (all our main results were similar without the 15-cm exclusion) to ensure that this bias did not affect our detection of the replay events representing an animal’s moving path. For plotting purposes only, a moving window (20 ms advanced in steps of 10 ms) was used for displaying replay sequences (Figures 2, 3, S2, and S3) (Farooq and Dragoi, 2019). Only behavioral sessions with more than one replay event per analyzed category were included for calculating the percentage (Figures 3F–3I, 5E, and 5F). 

## Replay prediction 

For replay prediction (Figures 3J, 3K, 5G, and 5H), trial-by-trial classification analysis was performed using support vector machines (SVMs) through the libsvm library (version 3.12) (Chang and Lin, 2011). During immobility periods at a given reward well (see Behavioral State Definition), the number of each replay event type was used as a feature (n = 8 possible features, 4 trajectory types x 2 replay orders, i.e., forward and reverse). Unless otherwise noted, all classifiers were C-SVMs with a radial basis function (Gaussian) kernel and trained on behaviorally correct trials. Hyperparameter (C and g; regularization weight and radial basis function width, respectively) selection was performed using a random search method with leave-one-out cross-validation to prevent overfitting. The selected hyperparameters were then used to report the leave-one-out cross-validation accuracy. The percentage of correctly inferred trials was computed across all training/test trial combinations to give prediction accuracy. The significance of this prediction was determined by comparing to the distribution of shuffled data. Each ‘‘shuffled’’ dataset was constructed by randomly shuffling the trial labels (see below), and this shuffled dataset was used to train a classifier in the same way as the actual dataset. A prediction accuracy based on the actual dataset that was higher than the shuffled ones with p < 0.05 was considered as significant. 

Specifically, to classify well identity (Figures 3J and 3K), two independent SVMs were trained on forward and reverse replay, respectively. For a given replay order (i.e., forward or reverse), the number of each replay event type during immobility at a given well was used as a feature (n = 4 features; 4 trajectory types) and the well ID was used as the trial label (k = 3; center, right, and left wells). For this prediction, a trial (or transition) is therefore defined based on the immobility period at the well during a given behavioral sequence. Only transitions where at least one replay event occurred for a given replay order were used. Since incorrect trials mostly occurred during learning of the outbound rule across sessions (Figure S1H) (Jadhav et al., 2012), these incorrect trials were selected to compare the replay predictions of future correct versus incorrect choices that originated at the center well. During these incorrect trials, the animal was located at the center well after performing a correct past trajectory (inbound; rewarded), but was about to choose the next outbound trajectory incorrectly. Thus, both future correct and incorrect trials were preceded by the presence of reward at the center well. The numbers of the 4 replay event types during immobility at the center well for these incorrect trials were used as input features (n = 4 features) to predict the well IDs (k = 3; center, right, and left wells) using the SVMs trained on all correct trials. The percentage of these trials that correctly predicted the center well was reported as prediction accuracy. To calculate statistical significance, correct trials at the center well were randomly subsampled 1,000 times to match the number of incorrect trials for computing prediction accuracy (Figure 3K). 

To predict actual taken versus not-taken paths based on replay (Figures 5G and 5H), independent SVMs were trained for each learning stage (i.e., early, middle, and late) and replay order (n = 6 SVMs, 3 learning stages x 2 replay orders) at either center or side wells. Early (sessions 1-3), middle (sessions 4-5), late (sessions 6-8) learning stages were chosen to balance the number of trials per stage (n = 79, 85, and 85 trials for reverse, and n = 87, 95, and 104 trials for forward during early, middle, and late stages, respectively). For a given replay order (i.e., forward or reverse), the numbers of events replayed for all 4 possible paths during the immobility period at a given well were used as features (n = 4 features), and the taken behavioral sequence was used as the trial label (k = 2; taken versus not-taken sequences; see Figure 1B). To investigate the change of replay content during incorrect trials, the replay events during immobility at the center well for the incorrect trials (as described above) were used as input features of the SVMs trained on all correct trials (Figures S6C and S6D). Only trials with at least one replay event in the given replay order were used for prediction. 

## CA1-PFC population reactivation analysis 

In substance, the method to measure CA1-PFC reactivation here is similar to the ‘‘template matching’’ or ‘‘reactivation strength’’ approaches used in several previous studies (Euston et al., 2007; Girardeau et al., 2017; Kudrimoti et al., 1999; Lansink et al., 2009; Peyrache et al., 2009; Tang et al., 2017; Wilber et al., 2017), but operated on a timescale of replay dynamics to examine finer temporal structure of the reactivation activity (i.e., 10 ms instead of 50-100 ms binning in the previous studies). Reactivation candidate events were defined as the SWR events during which R 5 place cells and R 5 PFC cells fired; therefore, they represent a subset of replay candidate events that were defined using only the CA1 place cell criterion. For a candidate event with N CA1 and M PFC cells firing 

e5 Neuron 104, 1110–1125.e1–e7, December 18, 2019 

**==> picture [60 x 60] intentionally omitted <==**

(N R 5, and M R 5), a (N x M) synchronization matrix during RUN (CRUN) was calculated with each element (Ci,j) representing the Pearson correlation coefficient (Ci,j) of the linearized spatial maps on a certain trajectory type (2-cm bin) of the i-th CA1 cell and the j-th PFC cell. To measure the population synchronization pattern during the SWR, the spike trains during the candidate event were divided into 10-ms bins as in the CA1 replay analysis and z transformed: 

**==> picture [64 x 21] intentionally omitted <==**

where si(t) is the spike train of the i-th cell during the candidate event, and siðtÞ and ssi are the mean and standard deviation of si(t), respectively. The (N x M) synchronization matrix during the candidate event (CSWR) was then calculated with each element (Ci,j) representing the correlation of a CA1-PFC cell pair: Ci;j = Q[CA] i[1] Q[PFC] j =B, where i % N, j % M, and B is the total number of time bins during the SWR. The reactivation strength of this event was measured as the correlation coefficient (R) between the population matrices, CRUN and CSWR. To evaluate the significance of the reactivation strength, the spike times during the SWR were randomly shuffled 1,500 times, in order to randomize the synchronization between CA1 and PFC cells, but conserve the structure of their spatial maps. A candidate event with p < 0.05 versus its shuffled data was considered as a reactivation event. As in the replay analysis, the reactivated trajectory was determined as the one (among the four possible trajectory types) with the lowest p value determined by the shuffling procedure. This was used to identify coherent CA1-PFC ensemble reactivation that was aligned with CA1 replay, and a graphical illustration of the method is provided in Figure S8. We used this synchronization measure because a synchronous, rather than sequential, timing relationship of cross-regional reactivation, including CA1-PFC reactivation, was reported in previous studies (Girardeau et al., 2017; Lansink et al., 2009; Tang et al., 2017), and it also allows us to directly compute and examine the combined cross-regional reactivation, rather than detecting reactivation separately in each region and then measuring their correlation. 

## Model simulations for reactivation analysis 

We created a simulated neuronal population as an illustrative example of the reactivation method described above (Figure S8), in comparison to other potential methods. We used model simulations here because while the ‘‘true’’ connectivity of recorded CA1PFC populations is inaccessible, using the forward-modeling scheme, in which the ‘‘ground truth’’ is known and the neuronal connectivity among the simulated population can be defined, allows for validation of the method for identifying synchronous reactivation. For simplicity, we formulate the model for 5 CA1 and 5 PFC cells. From neurophysiological data, it is known that when an animal moves along a trajectory, CA1 place cells often exhibit narrowly tuned single-peaked place fields, whereas the spatial maps of PFC cells are often broadly tuned and multi-peaked, suggesting a many-to-one mapping between hippocampal and PFC representations (Jadhav et al., 2016; Tang et al., 2017; Yu et al., 2018). Motivated by these response properties, the estimated firing rate (i.e., place field) of each place cell i, riðtÞ, is defined as a Gaussian tuning curve, 

**==> picture [178 x 26] intentionally omitted <==**

where ri;max is the maximum firing rate of the i-th cell, xðtÞ is the linear position of the animal at time t, xi;max is the position evoking the maximum average rate ri;max of the cell, and sf determines the width of the tuning curve (sf = 5 cm for CA1 cells). The synchronization pattern between CA1 and PFC cells within the population is defined by a many-to-one connectivity matrix. If the activity of the k-th PFC cell is synchronized with that of n CA1 cells (n R 1), the estimated firing rate (i.e., spatial map) of the k-th PFC cell, rkðtÞ, is determined as, 

**==> picture [173 x 26] intentionally omitted <==**

where wi;k is the connectivity weight between the i-th CA1 cell (i = 1, 2, ., n) and the k-th PFC cell, ck is the baseline firing rate of the k-th PFC cell, and sf is 10 cm for PFC cells. Thus, the peak positions of the PFC spatial map were determined by the synchronized CA1 cells as fxi;maxg for i = 1, 2, ., n. We assume that the spiking activity of each neuron follows an inhomogeneous Poisson process. Thus, spike sequences were simulated by using the estimated firing rate rðtÞ to drive a Poisson process. The probability of observing Ni;t spikes of the i-th cell in a bin of size t is given by a Poisson distribution with a rate parameter riðtÞt, 

**==> picture [134 x 23] intentionally omitted <==**

As in the real data, t is 10 ms for SWR events and 500 ms for active behavior. Note that this Poisson process generates an irregular firing pattern during SWRs that reflects the underlying spatial map. The reactivation method was then applied to the simulated data as described above, and compared to Bayesian decoding (O’Neill et al., 2017) and line-fitting (O[´ ] lafsdo´ ttir et al., 2016, 2017) methods. 

Neuron 104, 1110–1125.e1–e7, December 18, 2019 e6 

**==> picture [60 x 60] intentionally omitted <==**

## CA1-PFC activation ratio and pairwise reactivation 

For each cell activated during a SWR synchronous event (i.e., candidate event), the average firing rate of the cell during the SWR divided by its average firing rate across the behavioral session was used as its activation ratio. The activation ratio for a SWR synchronous event was then measured as the mean activation ratio across all cells activated during the SWR (Figures S7J–S7N). Pairwise reactivation strength was measured as the correlation coefficient between spatial correlation and SWR cofiring of cell pairs (Figures S7L–S7N), as described previously (Tang et al., 2017). In brief, the spatial correlation of a cell pair was defined as the Pearson’s correlation coefficient between their linearized spatial maps across all 4 trajectory types. SWR cofiring of a cell pair was calculated as the Pearson’s correlation coefficient between their spike trains occurring during SWR events using 50-ms bins. 

## Statistical analysis 

Data analysis was performed using custom routines in MATLAB (MathWorks, Natick, MA). We used nonparametric and two-tailed tests for statistical comparisons throughout the paper, unless otherwise noted. We used repeated-measures ANOVA for multiple comparisons of paired Gaussian distributions, followed by a Tukey’s test, when appropriate. For non-Gaussian distributions of multiple groups, we used Kruskal-Wallis or Friedman test, with post hoc analysis performed using a Dunn’s test. p < 0.05 was considered the cutoff for statistical significance. Unless otherwise noted, values and errors in the text denote means ± SEM. 

## DATA AND CODE AVAILABILITY 

The published article includes all datasets generated or analyzed during this study. The code supporting the current study is available from the Lead Contact on reasonable request. 

e7 Neuron 104, 1110–1125.e1–e7, December 18, 2019 

