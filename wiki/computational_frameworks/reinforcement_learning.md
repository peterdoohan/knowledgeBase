# Reinforcement Learning

An overview of reinforcement learning as a computational framework for understanding decision-making and learning.

---

## Current understanding

*Placeholder: Awaiting synthesis of key evidence.*

---

## Key evidence

- An alternative account of dopamine in model-based RL — well-informed scalar reward prediction error (RPE) plus a separate scalar surprise signal — can explain dopamine's involvement without requiring high-dimensional signaling ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- A scalar dopaminergic surprise signal, evaluated early in the sensory hierarchy but projected to high-level cortical areas, can upregulate learning rates in cortical and hippocampal predictive models ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- The successor representation (SR) account of dopamine does not naturally predict the large body of quantitative RPE-consistent data, including findings that dopamine neuron stimulation is strongly reinforcing — a phenomenon well-explained by scalar RPE theory ([Akam 2021](../../raw/summaries/akam2021_dopamine_model_based_rl.md))

- Reverse hippocampal replay rates track changes in reward magnitude—increasing at higher reward and decreasing at lower reward—while forward replay rates remain unchanged, supporting reverse replay's role in temporal credit assignment for reinforcement learning ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). This is the core prediction of the RL-based credit assignment hypothesis: that reverse replay propagates reward information backward along trajectories to enable credit assignment.

- Forward and reverse hippocampal replay are functionally dissociable, with reverse replay mediating reward-based learning (temporal credit assignment) while forward replay supports planning or memory retrieval independent of reward ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). This dissociation maps onto the RL distinction between value learning (backward propagation via reverse replay) and planning (forward simulation via forward replay).

- Reverse hippocampal replay encodes relative (adaptive) reward magnitude rather than absolute reward levels, supporting an RL-based credit assignment mechanism where relative values guide learning ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). The adaptive coding matches the known adaptive range coding of reward by dopamine neurons, which would provide the reward signal for credit assignment.

- Reverse replay is elevated after reward reinstatement, consistent with sensitivity to reward prediction error-like signals that would drive value updating in RL ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). When baseline reward was restored at a previously unrewarded location, reverse replay was significantly elevated (z = 3.35, p = 0.0049), suggesting it signals positive prediction errors that trigger learning.

- Both forward and reverse replay are predominantly locally initiated, beginning at the animal's current position during awake stopping periods, supporting the RL-based hypothesis that reverse replay from reward locations propagates value information backward along the just-experienced trajectory ([Ambrose 2016](../../raw/summaries/ambrose2016_reverse_replay_hippocampal.md)). Approximately 86% of replays in Experiment 1 and 78% in Experiment 2 were locally initiated.

- vmPFC and ventral striatum encode prediction errors in structure-specific multivoxel patterns, suggesting structure-conditioned credit assignment mechanisms in RL. Multivoxel patterns of prediction error signals differed by relational structure in left vmPFC (p=0.014), right vmPFC (p=0.02), and ventral striatum (p=0.034), suggesting these regions represent structure-conditioned learning signals that could support structure-specific credit assignment ([Baram 2021](../../raw/summaries/baram2021_entorhinal_ventromedial_rl.md))

- Deep RL produces genuinely novel emergent phenomena not present in either deep learning or RL alone, including meta-RL (fast adaptation via recurrent network dynamics) and distributional reward coding (multiple value predictions at different quantiles). These emergent properties provide new hypotheses for neural function that neither framework alone could generate ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- The RL formalism defines an agent in an environment selecting actions to maximize cumulative reward; the central quantities are state values V(s), action values Q(s,a), and reward-prediction errors (RPEs) δ = r + γV(s') − V(s). This TD error serves as the learning signal for value updates and matches dopaminergic activity patterns ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Deep RL research has produced intrinsic motivation algorithms (novelty, uncertainty, learned curiosity) and meta-RL-based structured exploration that parallel neuroscientific observations about strategic exploration. These computational frameworks provide models for how biological systems might balance exploration and exploitation in complex environments ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Key open questions identified in deep RL research include: sample efficiency vs. humans, flexible structured generalization, long-term temporal credit assignment, biological plausibility of backpropagation, and bidirectional influence between neuroscience and AI. These challenges define the frontier for both artificial and biological reinforcement learning ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

---

## History of ideas

---

## Open questions

---

## Related pages

- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [[temporal_credit_assignment]]
- [[reverse_replay]]
- [[forward_replay]]
- [[reward_processing]]
- [[ventral_tegmental_area]]
