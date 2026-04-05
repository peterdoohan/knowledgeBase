Neuron Article 

**==> picture [60 x 60] intentionally omitted <==**

## Hippocampal Replay of Extended Experience 

## Thomas J. Davidson,[1][,][2] Fabian Kloosterman,[1][,][2][,] * and Matthew A. Wilson[1] 

1Picower Institute for Learning and Memory, Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, 77 Massachusetts Avenue, 46-5233, Cambridge, MA 02139, USA 

2These authors contributed equally to this work 

*Correspondence: fkloos@mit.edu DOI 10.1016/j.neuron.2009.07.027 

## SUMMARY 

During pauses in exploration, ensembles of place cells in the rat hippocampus re-express firing sequences corresponding to recent spatial experience. Such ‘‘replay’’ co-occurs with ripple events: shortlasting (�50–120 ms), high-frequency (�200 Hz) oscillations that are associated with increased hippocampal-cortical communication. In previous studies, rats exploring small environments showed replay anchored to the rat’s current location and compressed in time into a single ripple event. Here, we show, using a neural decoding approach, that firing sequences corresponding to long runs through a large environment are replayed with high fidelity and that such replay can begin at remote locations on the track. Extended replay proceeds at a characteristic virtual speed of �8 m/s and remains coherent across trains of ripple events. These results suggest that extended replay is composed of chains of shorter subsequences, which may reflect a strategy for the storage and flexible expression of memories of prolonged experience. 

## INTRODUCTION 

Place cells in the hippocampal formation fire selectively when an animal moves through particular locations (‘‘place fields’’) in the environment (O’Keefe and Dostrovsky, 1971; Wilson and McNaughton, 1993). As a consequence, when the animal travels along a given trajectory, hippocampal cells with place fields on that trajectory are activated in sequence. During pauses in locomotion and during slow-wave sleep, many place cells are recruited in intermittent population bursts, which are accompanied by ripples in the hippocampal local field potential (Buzsa´ ki et al., 1992; Chrobak and Buzsa´ ki, 1996). The firing order of place cells during those bursts reflects a memory for the order in which they were activated during previous exploration. Such ‘‘replay’’ has been observed during slow-wave sleep (Ji and Wilson, 2007; Lee and Wilson, 2002; Na´ dasdy et al., 1999; Wilson and McNaughton, 1994) as well as during immobility on linear tracks (Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006) and in an open field (Csicsvari et al., 2007). 

During replay events in rats, place cell firing sequences are reexpressed at a faster rate than during actual experience (Diba 

and Buzsa´ ki, 2007; Foster and Wilson, 2006; Ji and Wilson, 2007; Lee and Wilson, 2002). For the small 1–2 m long linear tracks used in previous studies, the firing sequence of a set of place cells that spans the complete environment can be reexpressed at the same timescale of a single ripple (50–120 ms [Ylinen et al., 1995]). These results can be accounted for by a model in which sensory input drive to place cells is ‘‘read out,’’ possibly by a sweeping release of inhibition during a single sharp-wave ripple (Csicsvari et al., 2007; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006). 

The limited duration of single ripple events suggests that awake replay in a large environment should be limited to a small region of space. In the wild, however, rats typically navigate over tens or even hundreds of meters (Jackson, 1982). Can the hippocampus support replay across larger spatial scales? If so, is such extended replay further compressed in time or is there a fixed rate at which replay progresses? If the latter, how are longer sequences mapped onto short-lasting ripple events? 

## RESULTS 

## Extended Replay Detected by Neural Decoding 

Simultaneous recordings of multiple single units in hippocampal area CA1 were made (n = 47, 34, 23, and 32 units with consistent place-related firing in rats 1–4; see Experimental Procedures) while rats explored a 10.3 m long track (Figures 1A and 1B). Food reward was provided at both ends of the track, but since rats were not pretrained, behavior was variable and the animals frequently paused at many locations on the track (Figure 1C). We linearized the animal’s position, such that it represented the distance from one end of the track (Figure 1C), and the behavior of the rat was classified as either ‘‘RUN’’ (linear speed >15 cm/s) or ‘‘STOP’’ (linear speed <5 cm/s) (Figure 1E). Candidate replay events (‘‘CAND’’) were identified as periods during STOP with elevated multiunit activity across all electrodes (Figures 1D and 1E; see Experimental Procedures; mean rate during STOP of 0.36, 0.40, 0.32, 0.40 events/s in rats 1–4). Candidate events were characterized by sharp on- and offsets (Figures 1G and 1H), and event durations ranged from 40 to 1018 ms (Figure 1F), with 19% of events (17%, 22%, 16%, 14% in rats 1–4) characterized as ‘‘long’’ (>250 ms; chosen to be more than twice the typical duration of a single ripple [Ylinen et al., 1995]). 

To evaluate whether candidate events contained replayed spatial memory sequences, we employed a probabilistic neural decoding strategy to estimate the animal’s position on the track from the ensemble of spike trains (Brown et al., 1998; Wilson and 

Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 497 

Neuron 

Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

Figure 1. Behavior and Candidate Replay Events (A) Top view of the 10.3 m long track. Rat visible at right. (B) Head position during 100 s of exploration. Labels ‘‘A’’ and ‘‘B’’ denote the two ends of the track as used throughout the paper. 

**==> picture [288 x 313] intentionally omitted <==**

(C) Linearized position (meters from ‘‘A’’); same data as (B). (D) Multiunit activity (MUA) across all electrodes. Note distinct peaks corresponding to elevated population activity. 

(E) Identified periods of RUN (>15 cm/s), STOP (<5 cm/s), and candidate replay events (CAND; extracted from the MUA in D). 

(F) Histogram of candidate event durations in all rats. (G and H) Average MUA aligned to start (G) and end (H) of long (>250 ms) candidate events for rat 1. Note steep onset and offset of events. 

(Figures 2 and 3A–3C). The decoding algorithm we use is memoryless, and therefore the observed trajectories are not the result of temporal smoothing across neighboring estimates. 

In order to characterize individual events, we determined the best linear fit to the observed pattern of position estimates for each candidate event by maximizing a ‘‘replay score.’’ The resulting fit specifies the most likely constant-speed trajectory being replayed, and the replay score corresponds to the mean estimated likelihood that the rat was on the specified trajectory (see Experimental Procedures and Figure S2). To test for statistical significance, we compared the observed replay score for each event to sample distributions of scores obtained after shuffling the original data. Three distinct shuffling regimes were employed to control for nonspecific factors possibly contributing to the replay score (Figure S2). First, to control for the chance linear alignment of position estimates, we circularly shifted the estimate at each time point by a random distance (‘‘column-cycle shuffle’’). Second, to control for the contribution to the replay score of firing characteristics of single units (e.g., bursting), we randomly permuted the mapping between spiking records and spatial tuning curves (‘‘unit identity shuffle’’). Third, to control for a bias of the decoding procedure toward particular locations, we constructed artificial candidate events by combining position estimates taken randomly from the complete set of candidate events in each session (‘‘pseudoevent shuffle’’). We performed each shuffle 1500 times and conservatively consider only events with a Monte Carlo p value <0.01 under all three shuffles to be significant. 

McNaughton, 1993; Zhang et al., 1998). We reasoned that during reactivation of previous experience the position estimate would deviate systematically from the actual position (Johnson and Redish, 2007). 

Our algorithm does not require that each cluster used for decoding contains only spikes emitted by a single neuron; successful estimation requires only that the spatial tuning of each unit is stable across the training and decoding epochs. This property of the decoder allows us to make optimal use of the spatial information present in the neural data by including units that are less well isolated but which nevertheless have a stable spike amplitude signature and carry consistent spatial information. We therefore interpret our results in terms of the behavior of the hippocampal ensemble rather than that of individual place cells; we use the term ‘‘unit’’ rather than ‘‘cell’’ throughout the paper to emphasize this distinction. All reported results were qualitatively similar when calculated using only well-isolated units (see Supplemental Results). 

Using these criteria, 16% of all analyzed candidate events contained significant replay trajectories (118/657, 109/699, 12/ 137, 24/163 events significant for rats 1–4; p < 10[�][7] for each rat under a binomial distribution assuming a false-positive rate of 1%). Of long (>250 ms) candidate events, 33% were significant (59/145, 60/203, 9/36, 10/38 candidate events in rats 1–4; p < 10[�][10] for each rat). (Using a significance threshold of p < 0.05, 29% of all events and 50% of long events were found to contain replayed memory sequences; however, we chose to use a threshold of p < 0.01 to reduce the likelihood of false positives.) 

We first confirmed that we could use our decoder to accurately estimate the animal’s position during RUN using 500 ms time windows. Median error for rats 1–4 was 7, 9, 8, and 8 cm, with good performance across the entire environment (Figures 2A– 2C; see also Figure S1 and Movie S1). 

We next applied the decoding algorithm to nonoverlapping 20 ms time windows in all candidate events lasting at least 100 ms. During many candidate events, the sequence of position estimates described a rapid traversal of a section of the track at a relatively constant speed, even though the animal was stationary 

498 Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 

Neuron 

## Hippocampal Replay of Extended Experience 

**==> picture [324 x 594] intentionally omitted <==**

**==> picture [60 x 60] intentionally omitted <==**

## Figure 2. Replay Detection Using Position Reconstruction 

(A–E) Behavior and position reconstruction for a 80 s epoch during which rat 1 runs �7 m (from 10.3 m to 3.5 m), while pausing frequently. (A) True position of animal. (B) Estimated position. Each column is a probability density function estimated from unit activity in a 500 ms window. White, p = 0; black, p = 1. (C) Raster plots of spike times. Units are ranked by their preferred firing location; unit 1 has a place field closest to 0 m. Note bursts at 17 s, 27 s, and 78 s, which recruit a large fraction of all units. (D) Multiunit activity (MUA; average spike rate per tetrode, including unclustered spikes). (E) Identified periods of RUN and STOP and candidate replay events (CAND). (F–I) Position reconstruction applied to a candidate event revealing extended replay. (F) Estimated position (20 ms bins) describes a trajectory from 8 m to 2 m while the animal remains stationary at 9 m (black arrowhead). The direction of the arrowhead indicates that the animal is facing in the B/A direction. (G) Raster plot of unit firing. (H) MUA. (I) Candidate event. This event is the third example shown in Movie S2. 

Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 499 

Neuron 

Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [492 x 158] intentionally omitted <==**

Figure 3. Extended Replay (A–C) Examples of extended replay from rats 1–3. (Top) Estimated position across time (20 ms bins). Arrowheads indicate animal’s location and facing direction. Asterisks indicate start/end of detected linear trajectory. (Middle) MUA. (Bottom) Extent of replay event. (D) Length of replayed trajectory versus event duration for all replays. Solid line: linear regression (slope = 11.1 m/s; R[2] = 0.59; p < 10[�][10] ). (E) Kernel density estimate (Gaussian kernel, width = 1.5 m/s) of the distribution of replay speeds. (F and G) Distribution of start (F) and end (G) locations of replay trajectories relative to the animal’s position and heading on the track. A negative distance indicates the replayed trajectory starts or ends behind the animal (along the track). 

## Speed and Location of Replayed Trajectories 

Individual replay events could cover long sections of the track (Figures 3A–3C), and the length of replayed trajectories was linearly correlated with the duration of the events (Figure 3D), indicating a characteristic speed for replay (Figure 3E; median speed of 8.1 m/s for all significant events; median of 8.7/7.6/10.8/ 10.5 m/s in rats 1–4). These replay speeds are 15–20 times faster than a typical rat running speed (�0.5 m/s), consistent with previous reports of compression factors for shorter-duration replay events (Lee and Wilson, 2002; Na´ dasdy et al., 1999). 

We next analyzed the relation between the actual position of the animal during replay and the location of the replayed trajectories on the track. Replay occurred while the animal stopped at the ends of the track to consume reward as well as at other locations (Figures S3A–S3D). Replay in both the A/B and B/A directions was common, with no clear trend across rats (58%, 51%, 25%, 21% of replays from A/B in rats 1–4). Since rats spent a significant amount of time at the reward sites facing away from the track, a higher proportion of replayed trajectories occurred behind the animal (Figure S3; 35% ahead, 65% behind). This bias was not significantly different from chance (33% ahead; p = 0.58, two-sided Monte Carlo p value), computed under the null hypothesis that there is no relation between the stopping location of the rat and the position of the replayed trajectory. 

## Locally and Remotely Initiated Replay 

Previous reports suggested that replay might be influenced by strong local place-related inputs (Csicsvari et al., 2007; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006). Consistent with this model for replay generation, we found that the start locations of the replay trajectories were strongly biased toward the rat’s current location (Figure 3F), with 40% of significant replay trajectories starting within 50 cm of the rat’s current location, which we refer to as ‘‘local replay’’ (chance = 17%, calculated by boot- 

strapping under the null hypothesis that replay trajectories and the rat’s position are uncorrelated, p < 0.0005 pooled across rats). The location of the ends of replay trajectories were not similarly biased toward current location (Figure 3G), with only 5% ending nearer than 50 cm (chance = 8%, p = 0.99 pooled across rats). 

We also observed many significant replay trajectories that began at remote locations (Figure 3F; see examples in Figures 3B, 4C, and 4D). Indeed, 51% of events started at least 1 m away from the rat’s current location. Such trajectories could be artifacts of our replay detection method, if we made an error in determining the start time of the candidate event. A remote event could be either a truncated fragment of a long trajectory that actually begins at the current location (i.e., event start time too late; see Figure S7C for a possible example) or an incorrect extrapolation of a shorter trajectory that actually begins at the current location (i.e., start time too early). We conservatively exclude these two classes of possible errors by selecting only trajectories that proceed from a remote location toward the animal and that never proceed past the current location. Twenty percent of significant replay events (52/263) meet these more stringent criteria and are termed ‘‘remote replay’’ (dashed lines in Figure S3). There are significantly more remote replay events than the number of false positives expected to be generated by our replay detection procedure (52 of 1656 events; p < 10[�][11] under a binomial distribution, using false-positive rate of 1%). 

## Forward- and Reverse-Ordered Replay 

Previous studies have taken advantage of the joint tuning of many CA1 cells to running direction and location on the linear track (McNaughton et al., 1983; Muller et al., 1994) to demonstrate that spiking sequences can be replayed in either the forward or reverse temporal order (Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006). In order to determine the ordering of 

500 Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 

Neuron Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

**==> picture [491 x 429] intentionally omitted <==**

Figure 4. Forward and Reverse Extended Replay 

(A) Joint reconstruction of position and running direction (500 ms bins). Color indicates estimated running direction (see color mapping on the right). Direction is correctly estimated for both the A/B (6750–6770 s) and B/A directions (6820–6850 s). 

(B–F) Examples of forward (FWD), reverse (REV), and mixed (MIX) replay from rat 1, each labeled with its replay order score. The events in (B) and (C) are the first two examples shown in Movie S2. (Top) Joint position and direction estimates (20 ms bins). Arrowhead indicates animal’s position and facing direction. Asterisks indicate start and end of detected replay trajectory. (Middle) Multiunit activity. (Bottom) Extent of replay event. (B) Forward replay in the A/B direction proceeding ahead of the animal. (C) Forward replay in the B/A direction, starting 2 m behind the animal and proceeding behind the animal. (D) Reverse replay, starting remotely and proceeding toward the animal. Trajectory is similar to (C), but this is a reverse-ordered replay because the estimated running direction (i.e., A/B [blue]) does not agree with the direction in which the replay proceeds (i.e., from B/A). (E) Mixed replay proceeding behind the animal. (F) Mixed replay proceeding ahead of the animal. This event begins as an apparently forward-ordered replay then switches to reverse-ordered after �240 ms. (G) (Left) Distribution of observed (gray bars) and expected (pseudoevent shuffles; black line) replay order scores. (Right) Scatter plot of replay order score and replay duration for all significant replay events in all animals. Green, forward replay; yellow, reverse replay; gray, mixed replay. (H) Kernel density estimates (Gaussian kernel, width = 1.5 m/s) of the distribution of replay speeds for forward and reverse replay. 

the observed replay trajectories, we extended our decoding procedure to estimate both the rat’s position and its instantaneous running direction (i.e., whether the rat is running from A/B or B/A) from the entire ensemble (Figure 4A; see Experimental Procedures). Running direction was estimated correctly 

during RUN 89%, 83%, 83%, and 89% of time in rats 1–4 (chance 50%; p < 10[�][12] in each rat). 

For each replay event, we computed a ‘‘replay order score’’ that reflected the degree to which our estimate of instantaneous running direction agreed with (+1, forward replay) or disagreed 

Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 501 

Neuron 

Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

with (�1, reverse replay) the overall direction of the trajectory being replayed (see Experimental Procedures). For example, the reverse replay event in Figure 4D proceeds in the B/A direction (from 7.5 to 2.5 m on the track) but uses the hippocampal ensemble code associated with running in the opposite A/B direction, as indicated by the blue color. Overall, replay order scores were significantly biased away from 0 and toward �1 and 1 (Figure 4G; p < 0.02 for each rat, one-sided Kolmogorov-Smirnov two-sample test, compared to pseudoevent shuffle distribution), indicating that the hippocampal ensemble tends to represent one running direction consistently within a replay event. Statistical significance of the replay order score was next tested for each event by comparison to a distribution of order scores obtained from shuffled data. Significantly (p < 0.05) forward- and reverse-ordered replays were observed in all sessions (Figures 4B–4D and S5–S7 and Movie S2) across the full range of event durations (Figure 4G). 

Forward replay is significantly more frequent than reverse replay (p < 0.005 by two-sided binomial test), consistent with a previous report (Diba and Buzsa´ ki, 2007). Of all replay events, 40% (106/263) were significantly forward ordered, 26% (68/ 263) were significantly reverse ordered, with the remaining 33% of events (89/263) classified as ‘‘mixed’’ replay. This difference was also significant (p < 0.002) among replay events longer than 250 ms: 48% (66/138) were significantly forward ordered, and 25% (34/138) were significantly reverse ordered. Mixed replay events contain significant replay in decoded position but do not exhibit a consistent directional estimate. Most mixed events exhibit weak or variable direction tuning (e.g., Figure 4E), but we also occasionally observe events that apparently switch represented directions in mid-replay (e.g., Figures 4F, S5D, and S7C). 

We observed no significant difference in the speeds of forward and reverse replay trajectories (Figure 4H; median speed 8.6 versus 7.9 m/s; Kolmogorov-Smirnov two-sample test, p = 0.24). Forward and reverse replay trajectories did not preferentially correspond to runs in the A/B or B/A direction (47% of forward, and 52% of reverse replay trajectories proceeded from A/B). Similar proportions of both forward and reverse replay trajectories were initiated locally or remotely (p > 0.5 by two-proportion z test): 42% of forward and 38% of reverse replay events were local (greater than the respective chance levels of 17% and 19%, p < 0.0005); and 19% of forward and 20% of reverse replay events were remote. 

Locally initiated forward replay will reflect possible future paths, while locally initiated reverse replay will reflect possible approaches to the animal’s current location. Do such replayed trajectories preferentially express the animal’s actual past and future paths rather than the paths not taken? To address this question, we analyzed periods when the animal was stopped in the middle of the track (at least 2 m from either end), where there are two possible paths associated with the animal’s current location. We did not find a strong bias for locally initiated forward replay trajectories to represent the actual future path (15 actual future path versus 12 opposite direction). Similarly, there was no strong bias for locally initiated reverse replay to represent the actual path taken by the animal to reach the current location (9 actual past path versus 7 opposite direction). 

## Relationship between Extended Replay and Ripples 

Replay events have consistently been found to co-occur with ripple oscillations in the hippocampal local field potential (Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006; Ji and Wilson, 2007; Lee and Wilson, 2002; Na´ dasdy et al., 1999). Consistent with these reports, we found that ripple emission rate was much higher during replay events than during noncandidate event STOP periods (8.8–11.8 s[–1] versus 0.17–0.27 s[–1] ; p < 10[�][4] in each rat). Detected ripples were associated with transient deflections in the LFP (‘‘sharp waves’’; Figures 5B–5D) and with transient increases in multiunit activity (78%–88% increase; p < 10[�][7] for each rat; Figures 5C and 5E), and singleunit firing rate (81%–94% increase; p < 0.0002 for each rat). These effects each lasted �50 ms, which is comparable to the duration of single sharp-wave ripple complexes as described previously (Ylinen et al., 1995). In order to characterize the relationship between ripple events and extended replay, we performed a linear regression and found a strong positive correlation between the number of emitted ripples and the duration of the replay event (Figure 5A; R[2] = 0.65, 0.45, 0.70, 0.67 for rats 1–4, p < 0.001 for each rat). These results demonstrate that extended replay spans trains of discrete sharp-wave ripple events. 

Next we explored whether the confidence of the position reconstruction during replay events was uniform across the ripple trains. We find that reconstruction quality during replay, as measured by the mode of the position estimate, is significantly elevated at ripple peak times (Figure 5F; 0.20–0.26 versus 0.32–0.41; p < 10[�][4] for each rat). We also find that the error between the replayed trajectory and the estimated position is significantly lower at ripple peak times (Figure 5G; 87–131 cm versus 182–227 cm, p < 0.003 for each rat). These data show that replay integrity is not uniform across the duration of an event but that it is modulated in association with ripple trains, suggesting that extended replay consists of chains of shorter rippleassociated subsequences. 

## DISCUSSION 

We have shown that time-compressed forward and reverse hippocampal replay of long behavioral sequences is common during pauses in exploration of a large environment and is associated with trains of ripple events. In contrast to studies conducted in smaller environments, we find that replay is neither limited to locations where reward is consumed nor exclusively tied to the animal’s current location. 

We developed and used a neural decoding approach for replay detection. Performing replay detection in the decoded spatial domain affords advantages over methods that examine firing order across individual units, such as pair-wise correlation (Wilson and McNaughton, 1994) and spike-sequence detection (Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006; Lee and Wilson, 2004). Our method allowed us to examine the fine spatial structure of replayed trajectories in a statistically rigorous manner and makes optimal use of the spatial information contained in hippocampal spikes, including the activity of cells with irregularly shaped place fields (such as those with multiple firing fields [Fenton et al., 2008]; Figure S8). 

502 Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 

Neuron 

## Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

Figure 5. Replay Spans Multiple Ripples 

(A) Scatter plot of number of detected ripples during significant replay events in all animals as a function of replay event duration. Random jitter added in y axis for visualization. Linear regression: 9.9 ripples/s, R[2] = 0.56. 

(B) Ripple-triggered averages of wide-band hippocampal local field potential (LFP) during replay events in rat 1. Even in multiple-ripple events, each ripple is associated with a sharp wave in the LFP. 

(C) Example of multiple ripples during a single extended replay event. (From top to bottom) LFP; average amplitude in the ripple band (150– 250 Hz) across all electrodes; detected ripples; probability at the mode of position estimate; position estimate; MUA; candidate event time. (D–G) Ripple-triggered averages of wide-band LFP (D), MUA (E), mode of position estimate (F), and error between estimated location and replay trajectory (G) for replay events in rat 1. Shaded regions: 95% confidence intervals for the mean. 

Using this decoding approach, we demonstrated that behavioral sequences spanning long sections of a 10 m track are re-expressed during population bursts lasting up to 700 ms. Replay trajectories proceedat a constant speed of �8 m/s, �15–20times faster than typical rat running speeds. Such values are consistent with the compression factors determined previously by analysis of spike-time lags in smaller environments (Diba and Buzsa´ ki, 2007; Lee and Wilson, 2002). The constant speed of replay contrasts strongly with the rats’ highly irregular behavior on the track, suggesting that the sequential structure of the behavioral experience, rather than the detailed time course of particular episodes, is re-expressed during replay. Constant-speed replay is also reminiscent of studies in humans showing that response timesare linearly dependent ondistance traveledacrossan imaginedmap(Kosslynet al.,1978)or onthemagnitude ofmentalrotation of three-dimensional objects (Shepard and Metzler, 1971). 

We confirmed previous reports that awake replay events are associated with sharp-wave ripples in the local field potential 

(Csicsvari et al., 2007; Diba and Buzsa´ ki, 2007; Foster and Wilson, 2006). However, the extended replay sequences we report last much longer than the duration of a single sharp-wave ripple event, and we demonstrate that they span trains of sharp-wave ripples. Such trains have been noted since the first reports of ripples (Buzsa´ ki et al., 1983; O’Keefe and Nadel, 1978; Suzuki and Smith, 1987), but no function has previously been ascribed to this phenomenon. CA1 unit activity is highest at the peak of individual ripples, corresponding to an increased confidence of the position estimate, which suggests that extended hippocampal replay may consist of chains of subsequences, each with a spatial extent of �50 cm (based on a ripple duration of 60 ms and a replay speed of 8 m/s). Temporally compressed place cell sequences with a similar duration and spatial extent also occur during individual theta cycles (Foster and Wilson, 2007) (Figure S9), as predicted from the observation of phase precession in single place cells (Skaggs et al., 1996). 

Both theta sequences (Mehta et al., 2002) and ripple-associated replay (Foster and Wilson, 2006) have been proposed to arise from a translation of place cell excitability into a phase or latency offset by a sweeping decrease in inhibition. This model predicts that ripple-associated sequences in the hippocampus should be limited to roughly the spatial scale of a single place field and would therefore require that longer sequences consist of several sharp-wave-ripple-associated subsequences. One possible mechanism for the generation of trains of subsequences is provided by the re-entrant loops in the hippocampal-entorhinal circuitry (Canto et al., 2008; Kloosterman et al., 2004). Following each ripple, current hippocampal output 

Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 503 

Neuron 

Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

to the entorhinal cortex could be fed back to the hippocampus, providing the inputs required for expression of the next subsequence. Alternatively, extended replay may reflect the continuous operation of an autoassociative network, possibly in area CA3 (August and Levy, 1999). Recordings across multiple brain regions will be necessary to test these hypotheses. 

We found a bias for both forward- and reverse-ordered replay trajectories to begin near the animal, which suggests that such events could be used for evaluation of immediate future and past paths. We also found that when the rat was stopped in the middle of the track, where there are multiple possible paths away from (and possible approaches to) the current location, replayed trajectories were not strongly correlated with the animal’s actual behavior. In particular, forward replay trajectories were not predictive of the upcoming path, and reverse replay did not preferentially reflect the path just taken by the animal. These results suggest that replayed trajectories represent the set of possible future or past paths linked to the animal’s current position rather than the actual paths. Further study of the correspondence between replay order and behavior may benefit from the use of tasks that place specific demands on the animal’s evaluation of past and future experience. 

Diba and Buzsa´ ki (2007) found that forward replay beginning at the present location, moving along the upcoming path, was more common than forward replay beginning at a remote location and proceeding toward the animal’s current location along the preceding path. Similarly, they find a preference for reverse replay events to represent the previous path (which, since it is replayed in reverse, is also initiated locally). These results are consistent with our observation of a bias toward local initiation for both forward and reverse replay. 

We also report that a significant number of replay events express trajectories beginning at locations remote from the physical location of the rat. This indicates that during awake replay the hippocampus has access to a broad range of stored memory sequences that are not solely dependent on the current location or the behavior just prior to the replay event. In this respect, awake replay is similar to sequence reactivation during slow-wave sleep (Ji and Wilson, 2007; Lee and Wilson, 2002). In our experiments, the rat has visual access to the complete track, and it is possible that remotely initiated replay is cued by sensory inputs reaching the hippocampus through cortical pathways. Similarly, during slow-wave sleep, cortical inputs may bias or otherwise influence memory reactivation (Ji and Wilson, 2007), given the complex bidirectional interactions between the hippocampus and neocortex (Isomura et al., 2006; Mo¨ lle et al., 2006; Siapas and Wilson, 1998; Sirota et al., 2003; Wolansky et al., 2006). 

Interestingly, groups of ripples are also present during slowwave sleep, where they predominantly occur during periodic increases in neocortical population activity (‘‘up states’’) (Battaglia et al., 2004; Clemens et al., 2007; Mo¨ lle et al., 2006; Sirota et al., 2003) associated with slow oscillations in the cortical EEG (Isomura et al., 2006; Steriade, 2006; Wolansky et al., 2006). During these up states, coordinated memory reactivation has been observed in the hippocampus and visual cortex (Ji and Wilson, 2007). These data suggest that individual trains of ripples during both slow-wave sleep and in the awake state may consti- 

tute a higher-level organization, possibly sharing a common mechanism for their generation. 

Replay associated with single ripples may represent a building block for the expression of longer, more complex memories. Hippocampal replay has been proposed to contribute to memory consolidation during sleep (Buzsa´ ki, 1989; Marshall and Born, 2007; Stickgold, 2005). During wakefulness, highspeed replay of long sequences of behavior could also support learning processes that would benefit from prospective or retrospective evaluation, such as reinforcement learning (Foster and Wilson, 2006). Extended replay may also support tasks involving memory recall. This last possibility, while speculative, is lent some support by the recent finding of specific reactivation of hippocampal neurons during free recall in humans (GelbardSagiv et al., 2008) and by specific activation of the hippocampus during sequence recall tasks in humans (Lehn et al., 2009). This interpretation of the functional role of awake replay is also consistent with work suggesting a high degree of overlap in the cognitive processes supporting both episodic recall and the evaluation of future events in humans (Buckner and Carroll, 2007; Schacter et al., 2007). The link between awake replay and cognition can be further explored by studying replay in animals engaged in more cognitively demanding tasks and by the experimental disruption or bias of replay. 

## EXPERIMENTAL PROCEDURES 

## Electrophysiology and Behavior 

All procedures were approved by the Committee on Animal Care at Massachusetts Institute of Technology and followed US National Institutes of Health guidelines. Microdrive arrays carrying 9–18 independently adjustable goldplated tetrodes or octrodes (two octrodes in one animal) aimed at area CA1 of the right dorsal hippocampus (2.4 mm lateral and 4.0 mm posterior, relative to bregma) were implanted under isoflurane anesthesia in five male LongEvans rats (400–500 g). Tetrode and octrode construction is as previously described for tetrodes (Wilson and McNaughton, 1993): each electrode consists of a twisted bundle of four or eight polyimide-insulated microwires, fused and cut to create a blunt tip. Wire used for tetrodes was either 13 mm diameter nichrome resistance wire (RediOhm-800, Kanthal, Palm Coast, FL) electroplated with gold or 15 mm diameter nickel-iron wire (Nickel Alloy-120; California Fine Wire, Grover Beach, CA) with all recording sites plated with gold simultaneously using an electroless dip-plating process (Immersion Gold CF, Transene, Danvers, MA). Octrode wires were polyimide-coated tungsten (8 mm diameter, California Fine Wire, Grover Beach, CA). Electrodes were slowly lowered into the CA1 pyramidal cell layer over the course of 1–2 weeks. Individual units were isolated by manual clustering on peak spike waveform amplitudes across all channels using custom software (xclust; M.A.W.). For each electrode, the local field potential (LFP) was recorded from a single channel, filtered from 1–475 Hz and sampled at 2 kHz. All recordings were differential against a reference electrode placed in white matter overlying CA1. A screw in the skull overlying cerebellum served as ground. For each rat, a single electrode showing clear sharp waves was selected for plotting of LFP. 

Animals were not introduced to the �10.3 m long linear track (Figures 1A and 1B) until stable unit recordings were obtained and only had one track session per day. Animals received food reward at the track ends (‘‘A’’ and ‘‘B’’; see Figures 1A and 1B) only after the rat completed a full length of the track. For each animal, we selected a session in which the animal ran several complete laps, but behavior was still variable and the number of recorded units was large. These criteria limited the number of sessions we could use for each animal, and we chose one session per animal in order to preserve independence across sessions and to avoid overrepresentation of one animal in the data (track session 3, 3, 3, 4, and 3, duration of 60, 55, 26, 28, 74 min for rats 1–5). 

504 Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 

Neuron 

## Hippocampal Replay of Extended Experience 

Animal location and head direction were captured at 30 Hz by video tracking of two head-mounted LEDs using an overhead camera. The linearized position along the track was found by projecting the x,y coordinates of the animal’s position onto a hand-fitted spline model of the track (A = 0 m, B z10.3 m). Linearized velocity was smoothed with a Gaussian kernel (SD = 0.25 s) and epochs during which linearized speed is >15 cm/s (RUN) or linearized speed is <5 cm/s (STOP) were detected. Positive velocity indicates movement from A/B. 

## Place/direction Tuning and Unit Selection 

For each unit, we constructed a joint tuning curve over linearized position (10 cm bins) and running direction (A/B and B/A) from all spikes emitted during RUN (Figures S8E and S8F). This curve was smoothed in position (Gaussian kernel; SD = 5 cm). We excluded putative interneurons (mean firing rate >5 Hz) and units with weak place-related firing (peak rate in tuning curve <3 Hz), leaving 47, 34, 23, 32, and 21 spatially tuned single units in rats 1–5 (cluster quality measures: L ratio 0.12 ± 0.17; isolation distance 17 ± 9; calculated using peak amplitude on each channel [Schmitzer-Torbert et al., 2005]). 

## Candidate Replay Events 

A smoothed histogram (1 ms bins; Gaussian kernel, SD = 15 ms) was constructed of multiunit activity (MUA) including all spikes with a peak amplitude greater than 100 mV on any channel, whether or not they are part of an isolated cluster. Mean and standard deviation of MUA during STOP was calculated, and candidate replay events were defined as epochs during which MUA was higher than the mean and peak rate was at least three standard deviations above the mean. Only candidate events within 30 s of RUN were analyzed to exclude possible sleep periods. 

## Position Estimation and Validation 

We used a Bayesian reconstruction algorithm (Zhang et al., 1998) to compute the joint probability distribution of position and running direction from neuronal firing in nonoverlapping time bins using the place-by-direction tuning curves described above (see Supplemental Experimental Procedures). In cases where only position estimates were needed, we computed the marginal distribution of these estimates over position. In order to validate our estimation procedure, RUN epochs in each session were divided into ‘‘training’’ and ‘‘testing’’ periods (alternating 1 s epochs). We calculated tuning curves using data from the training period and used these to estimate position and direction during the testing period. Confusion matrices were calculated to assess reconstruction accuracy across the track (Figures S1B–S1F), and maximum-likelihood estimates of position and running direction were compared with the rat’s true behavior (Figure S1A). Data from rat 5 were excluded from further analysis because of poor position estimation during RUN (median error 23 cm; uneven coverage of track). 

## Replay Detection 

We define ‘‘replay’’ as a sequence of hippocampal firing patterns that encodes a trajectory along the track at a constant velocity (Figure S2). The most likely such trajectory is detected using a line-finding algorithm (Toft, 1996) across the set of position estimates obtained during each candidate event (see Supplemental Experimental Procedures). Each replay trajectory is characterized by its velocity, location on the track, and its likelihood (‘‘replay score’’). For each candidate event, replay scores were compared to score distributions of three types of shuffled versions of the data to test for significance (Monte Carlo p value [Davison and Hinkley, 1997] < 0.01 for each shuffle type; see Supplemental Experimental Procedures). 

To determine if significant replay events represented forward or reverse replay, we computed a ‘‘replay order’’ score as the difference between the mean likelihoods that the estimated running direction on the trajectory was in the same or opposite direction as the actual replayed trajectory (see Supplemental Experimental Procedures). 

To test if the magnitude of the replay order score for a replay event is statistically significant, it was compared to the distribution of replay order magnitudes of 2000 randomly generated pseudoevents of the same duration (see Supplemental Experimental Procedures). Replay events with a Monte Carlo p value < 0.05 are classified as ‘‘forward’’ or ‘‘reverse’’ replay; the remaining 

**==> picture [60 x 60] intentionally omitted <==**

events are classified as ‘‘mixed’’ replay. Throughout the paper, ‘‘significant replay’’ includes forward-, reverse-, and mixed-order replay. 

To measure overall bias of replay toward forward and reverse replay (scores of +1 and �1) and away from mixed replay (score of 0), we performed a onesided two-sample Kolmogorov-Smirnov test on the absolute values of the observed replay order scores and of the scores obtained under pseudoevent shuffling, as described above. 

## Replay Trajectory Analysis 

For each detected replay trajectory, we calculate whether that trajectory lies mostly ahead of or behind (along the track) the rat’s true position and report the fraction of events lying mostly ahead. We test the significance of this measure by nonparametric bootstrapping. The chance level pooled across animals is estimated by randomly pairing within each session the observed replay trajectories to the location of the rat at the time of the replay events (2000 simulations, Monte Carlo p value reported), under the null hypothesis that these two variables are independent. Because the rats spent a significant amount of time at the ends of the track facing away from the track, the chance level for replay trajectories lying behind the animal is higher than for those lying ahead of the animal. 

The same approach is used to analyze the relationship between the rat’s location and the start and end locations of detected replay trajectories. The test statistic in this case is the fraction of start or end locations within 50 cm of the rat’s true location. Similar results were obtained for thresholds ranging from 25 cm to 2 m. 

## Ripple Detection and Ripple-Triggered Analyses 

We used a variation of Skaggs’ (Skaggs et al., 2007) ripple-detection procedure, which allows for the detection of closely spaced ripples. The ripple amplitude at each recording site was estimated by band-pass filtering the local field potential (LFP) signal between 150 and 250 Hz, then taking the absolute value of the Hilbert-transformed signal (Siapas et al., 2005). The mean ripple amplitude across all recording sites was then smoothed (Gaussian kernel, SD = 12.5 ms) to give a single continuous measure of ripple activity. Individual ripples were detected as local peaks in this signal with an amplitude larger than 2.5 SD above the mean (mean and SD measured during STOP epochs). Ripple emission rates were calculated separately for each replay event and compared with the mean ripple emission rate across all non-CAND STOP periods using a one-sample t test. For plots in Figures 5B and 5D (but not for any statistical analysis), ripple times were aligned (±�2 ms) to the closest ripple cycle peak of the channel being plotted, in order to show local ripple structure. 

Comparisons between ripple and nonripple times during replay events were performed using either: a one-sided two-sample t test assuming unequal variances (used for MUA; single-unit firing rate); or, if the data did not appear to be normally distributed, the Mann-Whitney U test (used for mode of estimate; replay line error). For all tests, we used the same 20 ms nonoverlapping time bins used for position reconstruction, and the comparison was between bins that contained a detected ripple and those that did not. 

## SUPPLEMENTAL DATA 

Supplemental Data include Supplemental Experimental Procedures, Supplemental Results, nine figures, and two movies and can be found with this article online at http://www.cell.com/neuron/supplemental/S0896-6273(09)00582-0. 

## ACKNOWLEDGMENTS 

We thank E.N. Brown, D. Ji, M.S. Fee, B.B. Scott, A.S. Andalman, D.P. Nguyen, and Z. Chen for helpful discussions and comments on the manuscript. This research was supported by National Institutes of Health (NIH) grant MH061976 (M.A.W.) and a Singleton Fellowship (T.J.D.). 

Accepted: July 28, 2009 Published: August 26, 2009 

Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 505 

Neuron 

Hippocampal Replay of Extended Experience 

**==> picture [60 x 60] intentionally omitted <==**

## REFERENCES 

August, D.A., and Levy, W.B. (1999). Temporal sequence compression by an integrate-and-fire model of hippocampal area CA3. J. Comput. Neurosci. 6, 71–90. 

Battaglia, F.P., Sutherland, G.R., and McNaughton, B.L. (2004). Hippocampal sharp wave bursts coincide with neocortical ‘‘up-state’’ transitions. Learn. Mem. 11, 697–704. 

Brown, E.N., Frank, L.M., Tang, D., Quirk, M.C., and Wilson, M.A. (1998). A statistical paradigm for neural spike train decoding applied to position prediction from ensemble firing patterns of rat hippocampal place cells. J. Neurosci. 18, 7411–7425. 

Buckner, R.L., and Carroll, D.C. (2007). Self-projection and the brain. Trends Cogn. Sci. 11, 49–57. 

Buzsa´ ki, G. (1989). Two-stage model of memory trace formation: a role for ‘‘noisy’’ brain states. Neuroscience 31, 551–570. 

Buzsa´ ki, G., Leung, L.W., and Vanderwolf, C.H. (1983). Cellular bases of hippocampal EEG in the behaving rat. Brain Res. Brain Res. Rev. 6, 139–171. 

Buzsa´ ki, G., Horva´ th, Z., Urioste, R., Hetke, J., and Wise, K. (1992). Highfrequency network oscillation in the hippocampus. Science 256, 1025–1027. 

Canto, C.B., Wouterlood, F.G., and Witter, M.P. (2008). What does the anatomical organization of the entorhinal cortex tell us? Neural Plast. 2008, 381243. 

Chrobak, J.J., and Buzsa´ ki, G. (1996). High-frequency oscillations in the output networks of the hippocampal-entorhinal axis of the freely behaving rat. J. Neurosci. 16, 3056–3066. 

Clemens, Z., Mo¨ lle, M., Eross, L., Barsi, P., Hala´ sz, P., and Born, J. (2007). Temporal coupling of parahippocampal ripples, sleep spindles and slow oscillations in humans. Brain 130, 2868–2878. 

Csicsvari, J., O’Neill, J., Allen, K., and Senior, T. (2007). Place-selective firing contributes to the reverse-order reactivation of CA1 pyramidal cells during sharp waves in open-field exploration. Eur. J. Neurosci. 26, 704–716. 

Davison, A.C., and Hinkley, D.V. (1997). Bootstrap Methods and Their Application (Cambridge, UK; New York, NY, USA: Cambridge University Press). 

Diba, K., and Buzsa´ ki, G. (2007). Forward and reverse hippocampal place-cell sequences during ripples. Nat. Neurosci. 10, 1241–1242. 

Fenton, A.A., Kao, H.Y., Neymotin, S.A., Olypher, A., Vayntrub, Y., Lytton, W.W., and Ludvig, N. (2008). Unmasking the CA1 ensemble place code by exposures to small and large environments: more place cells and multiple, irregularly arranged, and expanded place fields in the larger space. J. Neurosci. 28, 11250–11262. 

Foster, D.J., and Wilson, M.A. (2006). Reverse replay of behavioural sequences in hippocampal place cells during the awake state. Nature 440, 680–683. 

Foster, D.J., and Wilson, M.A. (2007). Hippocampal theta sequences. Hippocampus 17, 1093–1099. 

Gelbard-Sagiv, H., Mukamel, R., Harel, M., Malach, R., and Fried, I. (2008). Internally generated reactivation of single neurons in human hippocampus during free recall. Science 322, 96–101. 

Isomura, Y., Sirota, A., Ozen, S., Montgomery, S., Mizuseki, K., Henze, D.A., and Buzsa´ ki, G. (2006). Integration and segregation of activity in entorhinalhippocampal subregions by neocortical slow oscillations. Neuron 52, 871–882. 

Jackson, W.B. (1982). Norway Rat and Allies. In Wild Mammals of North America, J.A. Chapman and G.A. Feldhamer, eds. (Baltimore, MD: Johns Hopkins University Press), pp. 1077–1088. 

Ji, D., and Wilson, M.A. (2007). Coordinated memory replay in the visual cortex and hippocampus during sleep. Nat. Neurosci. 10, 100–107. 

Johnson, A., and Redish, A.D. (2007). Neural ensembles in CA3 transiently encode paths forward of the animal at a decision point. J. Neurosci. 27, 12176–12189. 

Kloosterman, F., van Haeften, T., and Lopes da Silva, F.H. (2004). Two reentrant pathways in the hippocampal-entorhinal system. Hippocampus 14, 1026–1039. 

Kosslyn, S.M., Ball, T.M., and Reiser, B.J. (1978). Visual images preserve metric spatial information: evidence from studies of image scanning. J. Exp. Psychol. Hum. Percept. Perform. 4, 47–60. 

Lee, A.K., and Wilson, M.A. (2002). Memory of sequential experience in the hippocampus during slow wave sleep. Neuron 36, 1183–1194. 

Lee, A.K., and Wilson, M.A. (2004). A combinatorial method for analyzing sequential firing patterns involving an arbitrary number of neurons based on relative time order. J. Neurophysiol. 92, 2555–2573. 

Lehn, H., Steffenach, H.A., van Strien, N.M., Veltman, D.J., Witter, M.P., and Ha˚ berg, A.K. (2009). A specific role of the human hippocampus in recall of temporal sequences. J. Neurosci. 29, 3475–3484. 

Marshall, L., and Born, J. (2007). The contribution of sleep to hippocampusdependent memory consolidation. Trends Cogn. Sci. 11, 442–450. 

McNaughton, B.L., Barnes, C.A., and O’Keefe, J. (1983). The contributions of position, direction, and velocity to single unit activity in the hippocampus of freely-moving rats. Exp. Brain Res. 52, 41–49. 

Mehta, M.R., Lee, A.K., and Wilson, M.A. (2002). Role of experience and oscillations in transforming a rate code into a temporal code. Nature 417, 741–746. Mo¨ lle, M., Yeshenko, O., Marshall, L., Sara, S.J., and Born, J. (2006). Hippocampal sharp wave-ripples linked to slow oscillations in rat slow-wave sleep. J. Neurophysiol. 96, 62–70. 

Muller, R.U., Bostock, E., Taube, J.S., and Kubie, J.L. (1994). On the directional firing properties of hippocampal place cells. J. Neurosci. 14, 7235–7251. Nada´ sdy, Z., Hirase, H., Czurko, A., Csicsvari, J., and Buzsa´ ki, G. (1999). Replay and time compression of recurring spike sequences in the hippocampus. J. Neurosci. 19, 9497–9507. 

O’Keefe, J., and Dostrovsky, J. (1971). The hippocampus as a spatial map. Preliminary evidence from unit activity in the freely-moving rat. Brain Res. 34, 171–175. 

O’Keefe, J., and Nadel, L. (1978). The Hippocampus as a Cognitive Map (Oxford and New York: Clarendon Press and Oxford University Press). 

Schacter, D.L., Addis, D.R., and Buckner, R.L. (2007). Remembering the past to imagine the future: the prospective brain. Nat. Rev. Neurosci. 8, 657–661. 

Schmitzer-Torbert, N., Jackson, J., Henze, D., Harris, K., and Redish, A.D. (2005). Quantitative measures of cluster quality for use in extracellular recordings. Neuroscience 131, 1–11. 

Shepard, R.N., and Metzler, J. (1971). Mental rotation of three-dimensional objects. Science 171, 701–703. 

Siapas, A.G., and Wilson, M.A. (1998). Coordinated interactions between hippocampal ripples and cortical spindles during slow-wave sleep. Neuron 21, 1123–1128. 

Siapas, A.G., Lubenov, E.V., and Wilson, M.A. (2005). Prefrontal phase locking to hippocampal theta oscillations. Neuron 46, 141–151. 

Sirota, A., Csicsvari, J., Buhl, D., and Buzsa´ ki, G. (2003). Communication between neocortex and hippocampus during sleep in rodents. Proc. Natl. Acad. Sci. USA 100, 2065–2069. 

Skaggs, W.E., McNaughton, B.L., Wilson, M.A., and Barnes, C.A. (1996). Theta phase precession in hippocampal neuronal populations and the compression of temporal sequences. Hippocampus 6, 149–172. 

Skaggs, W.E., McNaughton, B.L., Permenter, M., Archibeque, M., Vogt, J., Amaral, D.G., and Barnes, C.A. (2007). EEG sharp waves and sparse ensemble unit activity in the macaque hippocampus. J. Neurophysiol. 98, 898–910. 

Steriade, M. (2006). Grouping of brain rhythms in corticothalamic systems. Neuroscience 137, 1087–1106. 

Stickgold, R. (2005). Sleep-dependent memory consolidation. Nature 437, 1272–1278. 

Suzuki, S.S., and Smith, G.K. (1987). Spontaneous EEG spikes in the normal hippocampus. I. Behavioral correlates, laminar profiles and bilateral synchrony. Electroencephalogr. Clin. Neurophysiol. 67, 348–359. 

Toft, P.A. (1996). The radon transform — theory and implementation. PhD thesis, Technical University of Denmark. URL: http://petertoft.dk/PhD/ 

506 Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 

Neuron 

## Hippocampal Replay of Extended Experience 

Wilson, M.A., and McNaughton, B.L. (1993). Dynamics of the hippocampal ensemble code for space. Science 261, 1055–1058. 

Wilson, M.A., and McNaughton, B.L. (1994). Reactivation of hippocampal ensemble memories during sleep. Science 265, 676–679. 

Wolansky, T., Clement, E.A., Peters, S.R., Palczak, M.A., and Dickson, C.T. (2006). Hippocampal slow oscillation: a novel EEG state and its coordination with ongoing neocortical activity. J. Neurosci. 26, 6213–6229. 

**==> picture [60 x 60] intentionally omitted <==**

Ylinen, A., Bragin, A., Na´ dasdy, Z., Jando´ , G., Szabo´ , I., Sik, A., and Buzsa´ ki, G. (1995). Sharp wave-associated high-frequency oscillation (200 Hz) in the intact hippocampus: network and intracellular mechanisms. J. Neurosci. 15, 30–46. 

Zhang, K., Ginzburg, I., McNaughton, B.L., and Sejnowski, T.J. (1998). Interpreting neuronal population activity by reconstruction: unified framework with application to hippocampal place cells. J. Neurophysiol. 79, 1017–1044. 

Neuron 63, 497–507, August 27, 2009 ª2009 Elsevier Inc. 507 

