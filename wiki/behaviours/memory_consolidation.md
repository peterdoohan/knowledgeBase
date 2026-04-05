# Memory Consolidation

## Current understanding

*(To be synthesized once sufficient evidence accumulates)*

## Key evidence

- Cognitive map buildup depends on time elapsed (weeks) rather than training frequency; mice trained 2 vs 3 days per week showed performance aligned by weeks since start, not training days, suggesting offline biological processes (consolidation) are rate-limiting ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Memory persistence thresholds in spatial learning: one training session produces 2-day memory but not 5-day memory; two sessions produce 5-day memory, indicating a threshold for long-term stability ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Cognitive map formation in mice shows offline gains: by week 3 (GL2), performance improved significantly in session 2 compared to session 1, showing offline consolidation benefits; by week 12+ (Updates phase), animals showed additional offline gains in session 2 beyond good initial performance ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))

- Reverse hippocampal replay rates track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged, supporting reverse replay's role in reward-based memory consolidation through temporal credit assignment ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)).

- Forward and reverse hippocampal replay are functionally dissociable, with reverse replay mediating reward-based memory consolidation while forward replay supports planning or memory retrieval independent of reward ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)).

- Reverse replay is elevated after reward reinstatement, consistent with sensitivity to reward prediction error-like signals that would drive memory updating and consolidation ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, reverse replay was significantly elevated (z = 3.35, p = 0.0049).

- Reverse replay appears suited for memory consolidation by linking outcomes to prior actions, while forward replay serves memory retrieval for planning; sleep and awake replay may have distinct functions, with sleep replay primarily for consolidation and awake replay for retrieval and working memory ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). This functional dissociation synthesizes evidence from Wilson & McNaughton (1994) on sleep reactivation and Foster & Wilson (2006) on awake replay.

- Reverse replay can occur after a single traversal of a novel track, demonstrating that behavioral repetition is not strictly necessary for consolidation-related replay, though experience-dependent plasticity enhances subsequent replay expression ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Foster & Wilson (2006) initially showed reverse replay after first experience.

- The medial prefrontal cortex (mPFC) develops an abstract, stimulus-independent relational map of learned graph structure over the course of several days following initial learning, demonstrating systems consolidation in humans. fMRI repetition suppression revealed a large mPFC cluster (peak t21 = 5.1, MNI [2, 42, 8]; FWE p = 0.003) showing cross-graph suppression that was significantly greater in session 2 than session 1 (SVC FWE p < 0.05, t21 = 3.66), indicating emergence of abstract representation via consolidation ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- Representational similarity analysis confirms the emergence of a full abstracted map in right pregenual mPFC from session 1 to session 2, converging with repetition suppression findings. RSA showed a cluster in right pregenual mPFC with emergence of full abstracted map (both within- and across-graph RDM elements) from session 1 to session 2 (SVC FWE p = 0.01) ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The MTL maintains concrete, stimulus-specific graph representations while mPFC develops abstract representations, suggesting a division of labour between these systems across consolidation. MTL showed both relevant and irrelevant graph representations simultaneously across both sessions (no abstraction), while mPFC showed emergence of cross-graph abstraction over days; this pattern aligns with systems consolidation theory where MTL maintains episodic specifics while neocortex extracts statistical structure ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- Offline (rest-period) replay correlates with model-free rigidity and reflects consolidation of habitual policies; off-task forward sequenceness during rest correlated negatively with Index of Flexibility (more rest-replay in less flexible, more model-free subjects) ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- Offline replay during the critical rest period following reward-contingency change included replay of subsequently chosen (newly planned) transitions, indicating offline replay can serve model-based re-planning as well as consolidation functions ([Eldar 2020](../../raw/summaries/eldar2020_replay_planning.md))

- Closed-loop optogenetic disruption of content-specific hippocampal reactivation during sleep selectively impairs recall of the disrupted memories while leaving undisrupted memories intact; animals showed significantly worse recall for target-environment goals than control-environment goals (dwell time p<0.0009, goal-zone crossings p<0.0006, path length p<10^-5), demonstrating content-specific memory consolidation ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Place map destabilization from disrupted replay is reversible: target-environment place maps recover to baseline levels after relearning; place field similarity of target environment was significantly lower at probe and first post-learning trial (p<0.0056 and p<0.027), but recovered by trials 6-10 (all p>0.34), suggesting sleep reactivation consolidates context-association rather than map itself ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Memory content rather than SWR event occurrence is the critical factor for consolidation: selective disruption of reactivation content impairs specific memories without affecting network parameters; network parameters (delta power, SWR counts, sleep duration) did not predict recall discrimination (all p>0.08), ruling out non-specific sleep-quality confounds ([Gridchyn 2020](../../raw/summaries/gridchyn2020_replay_selective_memory.md))

- Generative replay from the learned model enables effective continual learning without catastrophic forgetting, outperforming experience replay in nonparametric settings. Generative replay and prioritized generative replay agents significantly outperformed baseline (t=3.47, p=0.002 and t=4.18, p<0.001) and showed no difference from ideal experience replay; in nonparametric settings with unknown cluster numbers, generative replay outperformed both baseline and experience replay (p<0.001). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Run-post-run correlations decrease over learning while pre-run-post-run correlations remain stable, a novel prediction of the generative model. A novel prediction of the model - run-post-run correlations decreased linearly across blocks (beta=-0.05, t=-3.9, p<0.001) while pre-run-post-run correlations remained stable (beta=0.02, n.s.). ([Stoianov 2020](../../raw/summaries/stoianov2020_hierarchical_generative_model.md))

- Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Replay bias is specific to non-REM sleep and absent during awake reactivation ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

- Cue-biased replay represents selective content modulation rather than non-specific arousal ([Basu2021](../../raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md))

## History of ideas

*(To be synthesized)*

Systems consolidation theory posits that memories initially dependent on the hippocampus gradually become stabilized in neocortical networks through offline processes including sleep-dependent replay and reactivation.

## Open questions

- What are the specific biological processes that make consolidation time-dependent?
- How do consolidation thresholds (1 session vs 2 sessions) relate to synaptic and systems consolidation mechanisms?
- What role does sleep play in the observed offline gains?

## Related pages

- [Cognitive map](cognitive_map.md)
- [Spatial navigation](spatial_navigation.md)
- [Hippocampus](../brain_regions/hippocampus.md)
- [Schema learning](schema_learning.md)
- [[hippocampal_replay]]
- [[reverse_replay]]
- [[forward_replay]]
- [[temporal_credit_assignment]]
- [[reward_processing]]
