# Hippocampal Replay

## Current understanding

Hippocampal replay is the time-compressed reactivation of place cell sequences during sharp-wave ripple (SWR) events, occurring during both sleep and awake pauses. Awake replay can occur in forward order (same as experienced) or reverse order (opposite to experience). Forward and reverse replay are functionally dissociable: reverse replay is reward-sensitive and implicated in temporal credit assignment, while forward replay is reward-insensitive and linked to planning and memory retrieval.

---

## Key evidence

- Reverse hippocampal replay rates track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Poisson GLMM analysis showed reverse replay increased at 4× reward end (z = 3.57, p = 3.60 × 10⁻⁴) and decreased when reward removed (z = −2.05, p = 0.041); forward replay showed no effect in either experiment (Exp. 1: p = 0.76; Exp. 2: p = 0.068).

- Forward and reverse hippocampal replay are functionally dissociable, with reverse replay mediating reward-based learning while forward replay supports planning or memory retrieval independent of reward ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The bidirectional control within same stopping periods shows forward replay unaffected by reward manipulation while reverse replay is strongly modulated.

- Reverse hippocampal replay encodes relative (adaptive) reward magnitude rather than absolute reward levels, with rate changes reflecting reward value relative to the environment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Increasing reward at one end simultaneously elevated reverse replay there and depressed it at the unchanged end.

- Reverse replay is elevated after reward reinstatement, consistent with sensitivity to reward prediction error-like signals ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, reverse (but not forward) replay was significantly elevated (z = 3.35, p = 0.0049).

- Both forward and reverse replay are predominantly locally initiated, beginning at the animal's current position during awake stopping periods ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% in Experiment 2 were locally initiated.

- Reverse replay can occur after a single traversal of a novel track, demonstrating that behavioral repetition is not strictly necessary for replay generation, though experience-dependent plasticity enhances replay expression ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Foster & Wilson (2006) showed reverse replay after first experience; experience-dependent plasticity subsequently enhances replay.

- Replay can encode trajectories in physically separate environments and novel "shortcut" paths never actually taken, indicating replay represents learned spatial relationships rather than mere replication of prior activity ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Karlsson & Frank (2009) demonstrated remote environment replay; Gupta et al. (2010) showed never-experienced shortcut paths.

- Reverse replay appears suited for memory consolidation (linking outcomes to prior actions), while forward replay serves memory retrieval for planning; sleep and awake replay may have distinct functions, with sleep replay primarily for consolidation and awake replay for retrieval and working memory ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Wilson & McNaughton (1994) discovered sleep reactivation; Foster & Wilson (2006) discovered awake reverse replay.

- Sharp-wave ripple (SWR) rates track reward magnitude changes, serving as a nonspecific marker of reward-related hippocampal activation ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). SWR rate increased significantly at 4× reward end (z = 5.24, p = 1.61 × 10⁻⁷) and decreased when reward removed (z = −6.66, p = 2.67 × 10⁻¹¹).

- Awake hippocampal SWRs coordinately excite and inhibit distinct prefrontal cortical ensembles in a content-specific manner, with CA1 population activity preceding PFC responses by ~50 ms, establishing hippocampal-to-prefrontal information flow during replay ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- The co-activation patterns between hippocampus and prefrontal cortex during awake SWRs mirror the co-activity structure from theta periods (movement), demonstrating that SWRs reactivate experience-specific hippocampal-prefrontal representations rather than just hippocampal ones ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- Structured hippocampal-prefrontal coordination during SWRs is experience-dependent: CA1-PFC correlations are absent during pre-task rest and are not predicted by rest-period activity, establishing that functional coordination is built up through behavioral experience rather than reflecting fixed connectivity ([Jadhav 2016](../../raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md)).

- Hippocampal forward replay parallels the rollouts of a recurrent meta-reinforcement learning agent, avoiding walls more than chance (P<0.001), over-representing goal locations (P<0.001), and predicting subsequent physical actions more accurately when successful than unsuccessful (P<0.001) ([Jensen 2024](../../raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md)).

- Consecutive hippocampal replays become increasingly goal-directed, with goal over-representation increasing with replay number (2nd replay P=0.068, 3rd replay P=0.009), consistent with iterative policy refinement as implemented in a meta-RL agent ([Jensen 2024](../../raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md)).

- The medial prefrontal cortex generates independent awake trajectory replay during rule-switching tasks, with replay temporally independent from hippocampal replay (~5% co-occurrence) despite co-occurring with hippocampal SWRs at above-chance rates (40%) ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md)).

- mPFC replay rate during rule-switching positively predicts behavioral performance: higher mPFC replay rates correlate with faster rule switching (center: r = −0.76, p = 0.01; goal: r = −0.63, p = 0.02), while hippocampal replay at the goal shows the opposite correlation (r = 0.71, p = 0.009), demonstrating distinct functional roles ([Kaefer 2020](../../raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md)).

- Generative replay from the learned model enables effective continual learning without catastrophic forgetting, outperforming experience replay in nonparametric settings. Generative replay and prioritized generative replay agents significantly outperformed baseline (t=3.47, p=0.002 and t=4.18, p<0.001) and showed no difference from ideal experience replay; in nonparametric settings with unknown cluster numbers, generative replay outperformed both baseline and experience replay (p<0.001). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Internally generated hippocampal sequences follow Brownian diffusion statistics distinct from directed navigation, consistent with generative model sampling. Log-log regression showed replay trajectories followed power-law diffusion (alpha=0.46, s.d.=0.031) consistent with empirical findings (Stella et al., 2019), while navigation showed directed motion (alpha=0.75); replayed trajectories differed by 35% from most similar experienced trajectories and included 8.6 novel locations never visited. ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Pre-run dynamics predict post-run replay more strongly than post-run predicts run, supporting generative model-based preplay. Rank-order correlation analysis showed pre-run (preplay) and post-run (replay) activity were more strongly correlated (r=0.66) than post-run and run activity (r=0.36, t=17.05, p<0.001), matching empirical findings (Liu et al., 2019). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Run-post-run correlations decrease over learning while pre-run-post-run correlations remain stable, a novel prediction of the generative model. A novel prediction of the model - run-post-run correlations decreased linearly across blocks (beta=-0.05, t=-3.9, p<0.001) while pre-run-post-run correlations remained stable (beta=0.02, n.s.). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Generative replay from the learned model enables effective continual learning without catastrophic forgetting, outperforming experience replay in nonparametric settings. Generative replay and prioritized generative replay agents significantly outperformed baseline (t=3.47, p=0.002 and t=4.18, p<0.001) and showed no difference from ideal experience replay; in nonparametric settings with unknown cluster numbers, generative replay outperformed both baseline and experience replay (p<0.001). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Internally generated hippocampal sequences follow Brownian diffusion statistics distinct from directed navigation, consistent with generative model sampling. Log-log regression showed replay trajectories followed power-law diffusion (alpha=0.46, s.d.=0.031) consistent with empirical findings (Stella et al., 2019), while navigation showed directed motion (alpha=0.75); replayed trajectories differed by 35% from most similar experienced trajectories and included 8.6 novel locations never visited. ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Pre-run dynamics predict post-run replay more strongly than post-run predicts run, supporting generative model-based preplay. Rank-order correlation analysis showed pre-run (preplay) and post-run (replay) activity were more strongly correlated (r=0.66) than post-run and run activity (r=0.36, t=17.05, p<0.001), matching empirical findings (Liu et al., 2019). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Run-post-run correlations decrease over learning while pre-run-post-run correlations remain stable, a novel prediction of the generative model. A novel prediction of the model - run-post-run correlations decreased linearly across blocks (beta=-0.05, t=-3.9, p<0.001) while pre-run-post-run correlations remained stable (beta=0.02, n.s.). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

### Human Replay and Abstract Structure

- During rest, human hippocampal replay does not simply recapitulate visual experience but spontaneously reorders novel objects according to previously learned abstract structural rules. MEG sequenceness followed the rule-defined "true" sequence order but not the order of visual experience (Study 1: peak sequenceness at 40 ms lag, b = 0.017 ± 0.005; Study 2: peak at 40 ms, b = 0.021 ± 0.009). ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

- Even when all pairwise transitions in the scrambled stream were disrupted, replay still followed the rule-defined order, demonstrating genuine structural transfer rather than Hebbian chain-association. This rules out simple associative mechanisms as the basis for replay organization. ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

- Factorized structural codes (position and sequence identity) are actively co-replayed during human rest, preceding sensory representations by ~50 ms. During rest, both position and sequence codes were reactivated ~40–60 ms before the corresponding stimulus code. Position-code replay led stimulus-code replay by 50 ms (Wilcoxon p = 0.013). ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

- Abstract position codes replay in reverse order during a rest period *before* participants had ever seen the novel objects (peak at 30 ms lag, b = −0.036 ± 0.008). Greater pre-exposure transfer replay correlated with faster reduction in position-code activation across learning (interaction p = 0.007), suggesting that pre-existing structural templates scaffold the rapid integration of new experiences. ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

- At replay onset, power in the 120–150 Hz band (SWR-band) was significantly elevated compared to baseline in both studies; source localisation placed this increase in the medial temporal lobe / hippocampus (peak MNI: X = 18, Y = −12, Z = −27). These convergent features substantially strengthen the homology between human MEG-measured replay and rodent hippocampal SWR-associated replay. ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

- Hippocampal replay emerges after a single lap on a novel track and progressively slows down with repeated experience by adding more, finer-grained hover locations. Replay duration increased (R = 0.14, p = 8e−9) and slope decreased (R = −0.054, p = 0.03) across the first 14 passes on novel tracks ([Berners-Lee 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

- Replay slowing is environment-specific and experience-dependent, not time-dependent. Remote replays of a previously explored track did not slow while local replays did; slowing resumed only upon return to active running, not during rest periods ([Berners-Lee 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

- Within the hover-and-jump framework, replay slows by increasing step number while decreasing step size; hover locations are consistent across experience (mean pairwise correlation = 0.54), supporting an insertion model of detail acquisition ([Berners-Lee 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

- Hippocampal interneuron modulation to replay increases across passes in two independent datasets (Z = 2.4, p = 9.3e−3 and Z = 2.9, p = 2.0e−3), suggesting inhibitory mechanisms contribute to replay slowing ([Berners-Lee 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

- Fast reverse sequences of up to four task-state representations occur spontaneously in human MEG during non-spatial planning, providing the first evidence for hippocampal-replay-like sequences in humans outside the spatial domain. Reverse sequenceness peaked at 40 ms state-to-state lag (p = 0.0015) and was consistent across all 12 participants ([Kurth-Nelson 2016](../../raw/summaries/kurth_nelson2016_sequences_non_spatial.md))

- Sequences of length 3 (p = 0.009) and length 4 (p = 0.004) were reliably detected at 40 ms lag in human MEG during non-spatial planning; a complete four-state sequence lasted approximately 120 ms — a temporal compression factor of ~9 relative to the 350 ms visual cross-fade during task execution ([Kurth-Nelson 2016](../../raw/summaries/kurth_nelson2016_sequences_non_spatial.md))

- No significant trial-by-trial relationship was found between sequenceness magnitude and earnings (p = 0.83), planning time (p = 0.27), or specific moves chosen (p = 0.85), suggesting the functional role of reverse sequences (prospective planning vs retrospective consolidation vs working memory maintenance) remains unresolved ([Kurth-Nelson 2016](../../raw/summaries/kurth_nelson2016_sequences_non_spatial.md))

- The dominant sequenceness direction was reverse (not forward), contrasting with theta sequences in rodents but resembling sharp-wave ripple (SWR) sequences, suggesting reverse sequences may serve different computational functions in humans during non-spatial planning ([Kurth-Nelson 2016](../../raw/summaries/kurth_nelson2016_sequences_non_spatial.md))

- Forward replay switched to reverse replay of the rule-defined sequence after value learning (b = −0.028 ± 0.010). Only the rewarded sequence reversed; the neutral sequence remained forward. Reward-triggered reverse replay appeared during value learning itself (b = −0.053 ± 0.016) and continued during subsequent decision-making (b = −0.055 ± 0.020). ([Liu 2019](../../raw/summaries/liu2019_human_replay_reorganizes.md))

- Sensory cues presented during non-REM sleep can selectively bias hippocampal replay toward the associated spatial memory. Place cells with right-sided fields showed positive rate bias after Sound R; left-sided cells showed negative rate bias after Sound L (r = 0.29, P < 1.1 × 10⁻⁴). ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay is specific to non-REM sleep and does not occur during awake reactivation. Bias was absent during awake reactivation events (ANOVA, P = 0.82), consistent with human TMR literature showing cue-enhancement specific to non-REM. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Acoustic cues bias replay content without changing the overall rate of replay events. Acoustic cues did not change number of replay events (Kruskal-Wallis, P > 0.05), indicating selective content modulation rather than non-specific arousal. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay shows a time-limited window of susceptibility during sleep. Bias was stronger in early sleep than late sleep (first half: P < 1.7 × 10⁻⁵; second half: not significant), suggesting capacity limits for replay modulation. ([Bendor 2012](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

---

- Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

## History of ideas

Hippocampal replay was first discovered in sleep, where place cell sequences were found to reactivate in compressed time. Foster and Wilson (2006) subsequently discovered reverse replay during awake pauses on a linear track and proposed it as a mechanism for temporal credit assignment—propagating reward information backward along trajectories. Diba and Buzsáki (2007) reported both forward and reverse replay on the linear track, but the functional relationship between them remained unclear. Ambrose et al. (2016) established the critical functional dissociation: reverse replay is reward-sensitive while forward replay is reward-insensitive, supporting distinct computational roles in credit assignment versus planning/retrieval.

---

## Open questions

- What is the precise circuit mechanism linking VTA dopamine signals to the initiation of reverse replay?
- Do the same dissociations between forward and reverse replay hold in 2D environments or during active decision-making tasks?
- Is the rate of reverse replay itself functionally meaningful, or merely a byproduct of reward-triggered initiation?
- What is the role of remote reverse replay (of non-current locations) in credit assignment?
- Whether the same directional dissociation holds in tasks requiring active decision making is unknown

---

## Related pages

- [[reverse_replay]]
- [[forward_replay]]
- [[place_cells]]
- [[sharp_wave_ripples]]
- [[hippocampus_ca1]]
- [[temporal_credit_assignment]]
- [[memory_consolidation]]

- Hippocampal replay during rest/pauses can represent future goal-directed routes but does so reliably only under high mnemonic demand, not on stereotyped tracks ([Nyberg 2022](../../raw/summaries/nyberg2022_spatial_goal_coding.md))

- Closed-loop optogenetic disruption of content-specific hippocampal reactivation during sleep selectively impairs recall of targeted memories while leaving undisrupted memories intact; animals showed significantly worse recall for target-environment goals than control-environment goals (dwell time p < 0.0009, goal-zone crossings p < 0.0006, path length p < 10⁻⁵) ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Place maps destabilized by disrupted replay can recover after relearning, suggesting replay is not required for long-term map stabilization but for context-association consolidation; place field similarity of target environment was significantly lower at probe and first post-learning trial (p < 0.0056 and p < 0.027), but recovered by trials 6-10 (all p > 0.34) ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Disrupting one memory trace via targeted replay blockade does not degrade other related memories, arguing against circuit reorganization; same animals in same rest period showed intact memory for control environment whose replay was spared, with impairment selective to environment whose reactivation was blocked ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

### Generative Replay and One-Trial Learning (Batch 2026-04-05)

- The hippocampal formation functions as a hierarchical generative model organizing experiences into items, sequences, and maps, enabling generative replay rather than verbatim memory replay ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Generative replay enables effective continual learning without catastrophic forgetting, using bounded resources rather than unbounded memory storage; generative replay agents significantly outperformed baseline (t=3.47, p=0.002) and matched ideal experience replay with perfect memory ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Internally generated hippocampal sequences follow Brownian diffusion statistics (alpha=0.46) distinct from directed navigation (alpha=0.75), consistent with generative model sampling ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Pre-run dynamics predict post-run replay more strongly than post-run predicts run, supporting generative model-based preplay; rank-order correlation analysis shows pre-run and post-run activity more strongly correlated (r=0.66) than post-run and run activity (r=0.36, t=17.05, p<0.001) ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Run-post-run correlations decrease over learning while pre-run-post-run correlations remain stable, a novel prediction of the generative model; run-post-run correlations decreased linearly across blocks (beta=-0.05, t=-3.9, p<0.001) while pre-run-post-run correlations remained stable (beta=0.02, n.s.) ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

### Replay and Experience-Dependent Plasticity (Batch 2026-04-05)

- Hippocampal replay emerges after a single pass on a novel track and persists for at least 1 hour, substantially lowering the learning threshold implied by prior work; significant replay detected after single pass (post-experience Rest p = 2.0e−4 vs. pre-experience Pre-Rest p = 0.39) ([Berners 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

- Replay becomes progressively slower and richer in spatial detail with each additional lap, not via changes to underlying gamma dynamics but by inserting new hover locations; replay duration increased (R = 0.14, p = 8e−9) and slope decreased (R = −0.054, p = 0.03) across first 14 passes; slowing was environment-specific (local replays slowed, remote did not) ([Berners 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

- Hippocampal interneuron modulation to replay increases across passes, and PFC neurons remain modulated for longer during longer replays; interneuron modulation increased across passes in two independent datasets (Z = 2.4, p = 9.3e−3 and Z = 2.9, p = 2.0e−3); PFC neurons showed prolonged modulation during long versus short replays (80–160 ms post-replay: Z = −2.7, p = 3.5e−3) ([Berners 2022](../../raw/summaries/berners2022_hippocampal_replay_experience.md))

### Replay Content and Planning (Batch 2026-04-05)

- Awake hippocampal replay content is decoupled from subsequent behavioral choice, instead preferentially representing previously rewarded locations and non-recently visited places; only 2 of 4 subjects showed small enrichment for future arm; no consistent trial-by-trial relationship between replay and choice; GLM classifiers predicting choice from replay performed at chance ([Gillespie 2021](../../raw/summaries/gillespie2021_replay_past_experiences.md))

- Replay is strongly enriched for the previous goal arm (~20% of pre-choice remote replay events), persisting for multiple trial blocks after the goal has changed; GLMs confirm ~2-fold increase in replay rate for previous-goal arm; enrichment persisted for at least two full subsequent trial blocks; previous goal replay did not deter or encourage visits (no correlation with subsequent arm visits) ([Gillespie 2021](../../raw/summaries/gillespie2021_replay_past_experiences.md))

- The immediate past arm is actively suppressed in replay, occurring significantly below chance levels; replay of the arm just visited occurred significantly below chance; among non-rewarded arms, replay rate was higher for arms not visited in the past 5 trials; visit recency was negatively correlated with replay rate ([Gillespie 2021](../../raw/summaries/gillespie2021_replay_past_experiences.md))

- Hippocampal theta sequences alternate serially between path options during VTE, with three stages described: (1) deliberation — sequences alternate between both goal options; (2) planning — sequences sweep only toward the chosen goal; (3) automation — sequences collapse to the animal's immediate location ([Redish 2016](../../raw/summaries/redish2016_vicarious_trial_error.md))

- Hippocampal lesions and cannabinoid agonists (CP55940) that disrupt theta sequences increase VTE; clonidine (which reduces noradrenaline) decreases VTE and limits hippocampal search to a single path, providing causal evidence for hippocampal involvement in deliberative decision-making ([Redish 2016](../../raw/summaries/redish2016_vicarious_trial_error.md))
