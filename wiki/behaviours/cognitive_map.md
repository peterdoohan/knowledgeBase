# Cognitive Map

## Current understanding

*(To be synthesized once sufficient evidence accumulates)*

## Key evidence

- Cognitive map formation in mice occurs in three distinct phases: initial slow learning requiring 7+ sessions (naive phase), intermediate phase showing offline gains by session 2 starting at week 3, and expert phase showing good performance in session 1 with additional offline gains by session 2 starting at week 12+ ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Cognitive map buildup depends on time elapsed (weeks) rather than training frequency; mice trained 2 vs 3 days per week showed performance aligned by weeks since start, not training days, suggesting offline biological processes (consolidation) are rate-limiting ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Spatial schemas enable rapid updating of navigation strategies: barrier-only changes showed immediate adaptation (schema-like), while location changes required within-session learning but consolidated rapidly, with one session sufficient for consolidation by the second session ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Old goal location memories are not overwritten by new learning; probe trials showed animals crossed both current and previous goal locations more than control nodes, indicating retention of old spatial memories ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))

- Grid cells in the medial entorhinal cortex shift their firing fields toward learned goal locations, causing long-lasting deformations of the spatial map and demonstrating that grid cells participate in mnemonic coding beyond providing a simple spatial metric. This challenges the view that grid cells provide a universal invariant metric for spatial cognition ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- The entorhinal cognitive map is deformable by behaviorally relevant information: grid scores significantly decrease in environments containing learned reward locations compared to open field, and the number of fields at goals increases while mean distance to closest reward decreases. Field attraction strength correlates with pre-probe distance to goal, with fields within ~30 cm showing attraction ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- The hippocampal-entorhinal circuit stores multiple spatial maps that can coexist and alternate rapidly during learning ("flickering" dynamics), with both MEC and CA1 showing rapid alternation between pre- and post-learning representations with no intermediate states. This suggests dynamic encoding and reorganization of cognitive maps during goal learning ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- Medial entorhinal cortex and hippocampal CA1 use different mechanisms for updating cognitive maps during goal learning: MEC exhibits local remapping (field-specific movement) while CA1 exhibits global remapping (population-wide reorganization). MEC changes are more stable overnight compared to CA1, indicating different memory trace lability between regions ([Boccara 2019](../../raw/summaries/boccara2019_grid_goal_attractor.md))

- The entorhinal cortex encodes the relational structure of abstract reinforcement learning problems, generalizing across different sensory exemplars of the same structure. This extends the cognitive map framework from spatial to non-spatial domains, showing EC represents abstract task structure in a manner analogous to spatial remapping ([Baram 2021](../../raw/summaries/baram2021_entorhinal_ventromedial_rl.md))

- The medial prefrontal cortex (mPFC) develops an abstract, stimulus-independent relational map of learned graph structure over the course of several days following initial learning. fMRI repetition suppression revealed a large mPFC cluster (peak t21 = 5.1, MNI [2, 42, 8]; FWE p = 0.003) showing cross-graph suppression that was significantly greater in session 2 than session 1 (SVC FWE p < 0.05, t21 = 3.66), indicating emergence of abstract representation via consolidation ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract relational map in mPFC is genuinely factorised, responding to positional commonality across isomorphic graphs rather than merely encoding within-graph distances. Cross-graph suppression (switch trials) was detected in mPFC, indicating representation of graph position independent of which specific stimulus occupies that position; this operationalises factorisation as defined by the Tolman-Eichenbaum Machine framework ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract mPFC representation emerges in the same pregenual mPFC region previously implicated in grid-like coding of abstract 2D spaces. The session-2 cross-graph effect emerged within an mPFC ROI defined by grid-like coding from Constantinescu et al. (2016) (SVC FWE p = 0.03, t21 = 2.38), and the peak coordinates (MNI [2, 42, 8]) overlapped with the grid-like coding region ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The medial temporal lobe (MTL), specifically left entorhinal cortex–subiculum, simultaneously represents both task-relevant and task-irrelevant graph structures at both immediate and delayed time points after learning. fMRI repetition suppression showed distance-dependent suppression for both relevant and irrelevant graphs in left MTL (peak t22 = 4.39, MNI [-24, -22, -28]), with no difference between sessions or graph relevance (2×2 ANOVA, all p > 0.2) ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The medial prefrontal cortex (mPFC) develops an abstract, stimulus-independent relational map of learned graph structure over the course of several days following initial learning. fMRI repetition suppression revealed a large mPFC cluster (peak t21 = 5.1, MNI [2, 42, 8]; FWE p = 0.003) showing cross-graph suppression that was significantly greater in session 2 than session 1 (SVC FWE p < 0.05, t21 = 3.66), indicating emergence of abstract representation via consolidation ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract relational map in mPFC is genuinely factorised, responding to positional commonality across isomorphic graphs rather than merely encoding within-graph distances. Cross-graph suppression (switch trials) was detected in mPFC, indicating representation of graph position independent of which specific stimulus occupies that position; this operationalises factorisation as defined by the Tolman-Eichenbaum Machine framework ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The abstract mPFC representation emerges in the same pregenual mPFC region previously implicated in grid-like coding of abstract 2D spaces. The session-2 cross-graph effect emerged within an mPFC ROI defined by grid-like coding from Constantinescu et al. (2016) (SVC FWE p = 0.03, t21 = 2.38), and the peak coordinates (MNI [2, 42, 8]) overlapped with the grid-like coding region ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- The medial temporal lobe (MTL), specifically left entorhinal cortex–subiculum, simultaneously represents both task-relevant and task-irrelevant graph structures at both immediate and delayed time points after learning. fMRI repetition suppression showed distance-dependent suppression for both relevant and irrelevant graphs in left MTL (peak t22 = 4.39, MNI [-24, -22, -28]), with no difference between sessions or graph relevance (2×2 ANOVA, all p > 0.2) ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- Replay can encode novel "shortcut" paths never actually taken and trajectories in physically separate environments, indicating the cognitive map enables construction of possible paths from learned spatial relationships rather than mere replication of prior activity ([Pfeiffer 2017](../../raw/summaries/pfeiffer2017_hippocampal_replay_memory.md)). Gupta et al. (2010) demonstrated never-experienced shortcut paths in replay; Karlsson & Frank (2009) showed remote environment replay.

- The human hippocampal-entorhinal system implicitly encodes a map-like metric representation of discrete non-spatial relationships between objects, best described by a successor representation (predictive map) rather than Euclidean distance ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- fMRI adaptation in bilateral entorhinal cortex decreased monotonically with link distance on hidden graphs (peak t22 = 4.75 right, t22 = 4.42 left, FWE-corrected); MDS of neural distance matrix recovered actual graph topology (r = 0.65, p = 0.003) even without explicit awareness of structure ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

- The neural metric for relational knowledge follows successor representation/communicability rather than Euclidean distance; when communicability competed with Euclidean distance, communicability alone predicted entorhinal activity (FWE p = 0.006) ([Garvert 2017](../../raw/summaries/garvert2017_relational_knowledge_maps.md))

## History of ideas

*(To be synthesized)*

The cognitive map concept was introduced by O'Keefe & Nadel (1978) based on hippocampal place cells. The schema concept originates from Bartlett (1932) and was applied to rodent memory by Tse et al. (2007).

## Open questions

- What are the neural mechanisms supporting cognitive map formation over extended periods?
- How do cognitive maps transition from hippocampal-dependent to schema-like representations?
- What determines when old spatial memories are retained versus overwritten?

## Related pages

- [Spatial navigation](spatial_navigation.md)
- [Hippocampus](../brain_regions/hippocampus.md)
- [Memory consolidation](memory_consolidation.md)
- [Schema learning](schema_learning.md)
