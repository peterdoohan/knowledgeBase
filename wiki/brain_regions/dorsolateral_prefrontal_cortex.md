# Dorsolateral Prefrontal Cortex (DLPFC)

## Current understanding

The dorsolateral prefrontal cortex (DLPFC) is a key region for executive function, working memory, and cognitive control. Within the hierarchical reinforcement learning framework, DLPFC is proposed to house option representations — temporally abstract action policies that enable flexible, goal-directed behavior organized across multiple levels of abstraction.

## Key evidence

- Prefrontal cortex exhibits a rostro-caudal gradient where progressively more abstract behavioral representations are encoded more anteriorly, with hierarchical RL providing a computational framework for this organization ([Botvinick 2008](../../raw/summaries/botvinick2008_hierarchical_behavior_prefrontal.md))

- Dorsolateral prefrontal cortex houses option representations (task sets as temporally abstract policies) rather than merely transient working-memory buffers, according to the hierarchical RL framework ([Botvinick 2008](../../raw/summaries/botvinick2008_hierarchical_behavior_prefrontal.md))

- DLPFC is proposed to maintain the identity of the currently active option and support its persistence across time, corresponding to Extension 1 of the HRL actor that maintains representations of active options ([Botvinick 2009](../../raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md))

- Prefrontal cortex neurons code for key decision variables required for efficient learning including current value, last action, last reward, and action-reward interactions, as demonstrated by meta-RL models matching primate dlPFC neural coding patterns ([Botvinick 2019](../../raw/summaries/botvinick2019_reinforcement_learning_fast_slow.md))

- Prefrontal cortex delay-period activity exhibits diffusive bump dynamics on a 1-dimensional manifold, consistent with continuous attractor working memory models. Bump displacement predicts behavioural error in spatial working memory tasks; population activity flows on a low-dimensional manifold. ([Khona 2022](../../raw/summaries/khona2022_attractor_integrator.md))

## History of ideas

The DLPFC has been historically understood as the seat of working memory and executive function, following the work of Fuster and Goldman-Rakic. The hierarchical RL framework offers a reinterpretation: rather than merely maintaining transient information, DLPFC represents temporally abstract action policies (options) that organize behavior hierarchically. This aligns with the rostro-caudal gradient observed in frontal cortex, where more anterior regions represent more abstract, longer-timescale information.

## Open questions

- How does the brain discover useful options rather than having them hand-designed? What neural mechanisms support option discovery from experience?
- What is the precise neural implementation of option maintenance in DLPFC? How are option identities represented at the cellular and circuit level?
- How does DLPFC interact with other frontal regions to implement hierarchical control? What are the specific projection patterns involved?

## Related pages

- [Prefrontal Cortex](prefrontal_cortex.md)
- [Hierarchical RL](../computational_frameworks/hierarchical_rl.md)
- [Working Memory](../behaviours/working_memory.md) (if exists)
- [Cognitive Control](../behaviours/cognitive_control.md) (if exists)
- [Frontopolar Cortex](rostrolateral_prefrontal_cortex.md)
- [Dorsolateral Striatum](dorsolateral_striatum.md)
