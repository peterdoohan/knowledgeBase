# Schema Learning

## Current understanding

*(To be synthesized once sufficient evidence accumulates)*

## Key evidence

- Spatial schemas enable rapid updating of navigation strategies: barrier-only changes showed immediate adaptation (schema-like), while location changes required within-session learning but consolidated rapidly, with one session sufficient for consolidation by the second session ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Learning set effects (Harlow 1949) apply to complex spatial environments: a three-step progression from naive (slow learning, no offline gains), to intermediate (offline gains but no one-session learning), to expert (both online and offline gains, rapid consolidation), suggesting rule abstraction plus spatial map knowledge ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))
- Old goal location memories are not overwritten by new learning; probe trials showed animals crossed both current and previous goal locations more than control nodes, indicating retention of old spatial memories, consistent with schema-based memory organization ([Alonso 2021](../../raw/summaries/alonso2021_hexmaze_cognitive_map.md))

- Humans use relational structure in reinforcement learning tasks to generalize across sensory exemplars, as captured by a structure-aware model with cross-stimulus update terms. A STRUCT model (modified delta-rule with cross-terms H_XY) significantly outperformed structure-naive NAIVE/Rescorla-Wagner model in cross-validation (t(27)=4.29, p=0.0002), providing behavioral evidence for structure-based generalization in human RL analogous to learning-set phenomena ([Baram 2021](../../raw/summaries/baram2021_entorhinal_ventromedial_rl.md))

- The medial prefrontal cortex (mPFC) develops an abstract, stimulus-independent relational map of learned graph structure over the course of several days following initial learning, representing a form of schema abstraction. fMRI repetition suppression revealed a large mPFC cluster (peak t21 = 5.1, MNI [2, 42, 8]; FWE p = 0.003) showing cross-graph suppression that was significantly greater in session 2 than session 1 (SVC FWE p < 0.05, t21 = 3.66), indicating emergence of abstract representation via consolidation ([Baram 2024](../../raw/summaries/baram2024_abstract_relational_map_consolidation.md))

- RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

- mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation ([Basu2021](../../raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md))

## History of ideas

*(To be synthesized)*

The schema concept was introduced by Bartlett (1932) to describe how prior knowledge structures organize memory. Tse et al. (2007) demonstrated schema effects in rodent associative learning, showing that prior knowledge accelerates new learning and enables rapid consolidation. Harlow (1949) introduced learning set theory, showing that animals learn to learn across similar problems.

## Open questions

- What neural circuits support schema formation and use in spatial navigation?
- How do hippocampal and medial prefrontal cortex interactions enable schema-based rapid updating?
- What distinguishes schema-like updating from incremental learning at the computational level?

## Related pages

- [Cognitive map](cognitive_map.md)
- [Memory consolidation](memory_consolidation.md)
- [Spatial navigation](spatial_navigation.md)
- [Hippocampus](../brain_regions/hippocampus.md)
- [Prefrontal cortex](../brain_regions/prefrontal_cortex.md)
