# Striatum

The striatum is the main input structure of the basal ganglia, receiving dopaminergic projections from the midbrain and cortical inputs via cortico-striatal pathways. It plays a central role in reinforcement learning, action selection, and habit formation.

---

## Current understanding

*No content yet — will be synthesised from Key evidence once sufficient facts are collected.*

---

## Key evidence

- Dopamine heterogeneity is partially explained by partial summation of value over state features across parallel cortico-basal-ganglia loops; the radically different profile of tail-of-striatum dopamine neurons (threat-responsive, aversive) likely reflects a separate axis of reinforcement ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- The striatum receives widespread dopamine projections from VTA and substantia nigra that carry a scalar TD prediction error signal; dopamine terminals contact dendritic spines that also receive cortical input, providing a physical substrate for weight updates in reinforcement learning ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- Dopamine prediction error signals in the striatum can serve dual purposes: learning predictions (critic function) and guiding action selection (actor function) through connection to dynamic programming principles ([Schultz 1997](../../raw/summaries/schultz1997_neural_substrate_reward_pred.md))

- Deep RL clarifies the interaction between model-free and model-based systems; spontaneous model-based-like behavior can emerge from model-free training, and the successor representation may be a mechanism for this transition. The striatum is implicated in model-free RL and habit formation, while the interaction between striatal model-free and hippocampal model-based systems is a central topic in decision neuroscience ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- D1-MSN stimulation drives VTA dopamine neurons via a hardwired biphasic linear filter that computes a temporal difference, demonstrating that TD error calculations are built into the dopamine-striatum microcircuit; optogenetic stimulation of lNAc D1-MSNs with 7 graded patterns produced dopamine responses matching TD error predictions including negative steady-state, with LTI model CV R^2 = 0.81 ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- TD computation is conserved across striatal subregions with region-specific parameters: biphasic impulse responses observed in lNAc, DMS, and DLS with cross-validated R^2 = 0.64-0.92; DLS showed faster dynamics (shorter time to minimum, P=0.01); gamma closer to 1 for DMS and DLS vs lNAc (though not significantly different, P=0.23) ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

- D1-MSNs in the nucleus accumbens acquire a value-like signal during opto-conditioning that is selectively potentiated by reward-predictive cues; lNAc D1-MSN calcium responses to odors were selectively potentiated by the CS+ over training (mean z-score difference = +0.62 ± 0.25, marginally significant, P = 0.0504 in D1 mice) while D2-MSNs showed no such potentiation (P = 0.84) ([Campbell 2025](../../raw/summaries/campbell2025_hardwired_circuit_td_learning.md))

---

## History of ideas

---

## Open questions

---

## Related pages

- [Ventral Tegmental Area](ventral_tegmental_area.md)
- [Substantia Nigra](substantia_nigra.md)
- [Prefrontal Cortex](prefrontal_cortex.md)
- [Model-free RL](../computational_frameworks/model_free_rl.md)
