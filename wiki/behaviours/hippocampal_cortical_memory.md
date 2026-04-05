# Hippocampal-Cortical Memory Interaction

## Current understanding

Specific hippocampal place representations are preferentially reactivated with generalized prefrontal cortical task representations during awake memory reactivation events (sharp-wave ripples), suggesting a mechanism linking specific experiences to general knowledge. This reveals a "many-to-one" mapping where multiple specific hippocampal location representations can converge onto single generalized prefrontal task representations during memory reactivation. The framework extends the complementary learning systems theory by showing that hippocampal-cortical networks maintain structured links between specific and general representations, which could support memory abstraction and the embedding of individual experiences in broader knowledge structures. The transformation from experience-specific to generalized associations emerges through learning, as the network enriches links between frequently co-occurring features across multiple experiences.

## Key evidence

- CA1 cells showed location-specific firing with low all-trial similarity (Rmedian) but high within-trajectory reliability (Rmax), consistent with specific spatial representations ([Yu 2018](../../raw/summaries/yu2018_hippocampal_cortical_memory.md))

- PFC cells showed heterogeneous activity patterns, with a subset showing high all-trial similarity (Rmedian > 0.5) representing general task features across trajectories ([Yu 2018](../../raw/summaries/yu2018_hippocampal_cortical_memory.md))

- PFC cells with high all-trial similarity were significantly enriched in SWR reactivation events compared to non-reactivated PFC cells (Kolmogorov-Smirnov test: p < 10^-3) ([Yu 2018](../../raw/summaries/yu2018_hippocampal_cortical_memory.md))

- Trial similarity measures (Rmedian, Rmax, Intertraj. Rmedian) were better predictors of SWR reactivation than firing rate, speed correlation, or trial coverage variables (GLM: 7.4-10.8% variance explained vs. 3.8%) ([Yu 2018](../../raw/summaries/yu2018_hippocampal_cortical_memory.md))

- Reactivated PFC cells showed a "many-to-one" mapping: different hippocampal path location reactivations engaged similar PFC firing patterns, whereas hippocampal path vs. well location reactivations engaged different PFC patterns ([Yu 2018](../../raw/summaries/yu2018_hippocampal_cortical_memory.md))

- Pairwise CA1-PFC coactivity during ongoing experience was a poor predictor of reactivation, consistent with learned transformations in hippocampal-cortical associations ([Yu 2018](../../raw/summaries/yu2018_hippocampal_cortical_memory.md))

## History of ideas

Prior to this study, the prevailing understanding was that the hippocampus and prefrontal cortex maintain stored associations that are transiently reinstated during hippocampal sharp-wave ripple (SWR) events. Earlier work established that early in learning, the degree of hippocampal-PFC co-firing during ongoing experience predicts their coactivity during SWRs. However, once the environment and task become familiar, hippocampal-PFC coactivity during ongoing experience is no longer predictive of SWR coactivity. This raised the question of what determines which PFC representations are reactivated with hippocampal representations in familiar settings, and whether these associations could reflect links between specific hippocampal representations and potentially more general PFC task representations. This study demonstrated that specific hippocampal place representations are preferentially reactivated with a subset of prefrontal cortical representations that generalize across different spatial trajectories (high all-trial similarity), rather than with PFC representations that are specific to individual trajectories.

## Open questions

- The study was conducted in well-trained animals with at least 5 days of task exposure; the transformation of hippocampal-cortical associations with learning was inferred by comparing to prior studies rather than tracked longitudinally within the same animals
- The mechanism by which coordinated hippocampal-cortical communication during sleep drives changes in hippocampal-cortical associations remains unknown
- Whether the content of hippocampal-cortical memory reactivation during sleep SWRs reflects the same specific-to-general associations as awake SWRs is not directly tested
- The specific cellular and circuit mechanisms (e.g., specific cell types, neuromodulators) that enable selective reactivation of generalized PFC representations are not identified
- The computational principles governing how the network learns to map specific hippocampal representations to general cortical representations remain to be formalized

## Related pages

- [Sharp-wave ripples](sharp_wave_ripples.md)
- [Hippocampal replay](hippocampal_replay.md)
- [Memory consolidation](memory_consolidation.md)
- [Prefrontal cortex](../brain_regions/prefrontal_cortex.md)
- [Hippocampus](../brain_regions/hippocampus.md)
- [Complementary learning systems](../computational_frameworks/complementary_learning_systems.md)
- [Generalization](generalization.md)
- [Abstraction](abstraction.md)
