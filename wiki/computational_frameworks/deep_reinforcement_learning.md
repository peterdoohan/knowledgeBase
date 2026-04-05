# Deep Reinforcement Learning

Deep reinforcement learning (deep RL) is the integration of deep neural networks with reinforcement learning algorithms, enabling agents to learn directly from high-dimensional sensory inputs and develop complex representations shaped by reward signals.

---

## Current understanding

Deep RL represents a fundamental advance over classical RL and deep learning applied separately. When deep neural networks are trained end-to-end to maximize long-term reward, emergent phenomena arise that neither framework produces alone. These include meta-learning (learning to learn), distributional reward coding, hierarchical control structures, and representations that are actively shaped by reward contingencies rather than merely reflecting sensory statistics.

The framework treats representation, learning, and decision making as mutually constitutive rather than independent problems. This integration provides neuroscience with models of how neural representations might be progressively structured by reward signals, and how those representations in turn support flexible learning and adaptive behavior.

---

## Key evidence

- Deep RL produces genuinely novel emergent phenomena not present in either deep learning or RL alone, including meta-RL (fast adaptation via recurrent network dynamics) and distributional reward coding (multiple value predictions at different quantiles) ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Deep RL systems learn task-relevant internal representations that are actively shaped by reward signals, not merely by sensory statistics, paralleling neuroscientific evidence that even primary visual cortex representations depend on task and reward contingency ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Spontaneous model-based-like behavior can emerge from purely model-free training in deep RL systems, with the successor representation proposed as a potential mechanism for this transition ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Experience replay in deep RL serves analogous learning-efficiency functions to hippocampal replay, with non-uniform prioritization mechanisms in both systems that preferentially reactivate surprising or high-error experiences ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Multi-level RL architectures in deep RL recapitulate features of frontal cortex organization, including cost-of-control mechanisms, automatic versus controlled processing distinctions, and timescale gradients across cortical areas ([Botvinick 2020](../../raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md))

- Fast learning in deep RL is always parasitic on slower incremental learning that builds representations and inductive biases, a principle that applies equally to biological brains ([Botvinick 2019](../../raw/summaries/botvinick2019_reinforcement_learning_fast_slow.md))

- Episodic deep RL enables one-shot generalization by storing raw experience and querying by similarity, but depends critically on slow learning of state-embedding metric ([Botvinick 2019](../../raw/summaries/botvinick2019_reinforcement_learning_fast_slow.md))

- Meta-RL trains recurrent networks across task distributions to implement fast inner-loop learning algorithms through slow outer-loop weight learning, embodying inductive biases suited to the task distribution ([Botvinick 2019](../../raw/summaries/botvinick2019_reinforcement_learning_fast_slow.md))

---

## History of ideas

Before deep RL, neuroscience applied deep learning and reinforcement learning largely in isolation. Deep learning models captured neural representations (primarily in sensory cortex), while classical RL accounted for dopaminergic reward prediction errors and reward-based learning in basal ganglia and prefrontal circuits. The representation problem—how states come to be encoded in ways that support generalization and task-adaptive behavior—was largely unaddressed by RL theory, and the learning problem was decoupled from representation in deep learning approaches.

Deep RL emerged as a distinct framework when Mnih et al. (2013, 2015) demonstrated that deep neural networks could be trained end-to-end to play Atari games from raw pixels using Q-learning (DQN). This breakthrough showed that deep RL could learn complex representations shaped by reward signals. The subsequent development of AlphaGo/AlphaZero (Silver et al., 2016-2018) demonstrated the scalability of deep RL to complex planning and model-based reasoning tasks.

The neuroscientific engagement with deep RL began with vanguard studies showing representational correspondences between deep RL agents and neural systems: Song et al. (2017) demonstrated that recurrent deep RL models could match orbitofrontal and prefrontal neuron response profiles; Banino et al. (2018) showed that grid-like representations emerge spontaneously in deep RL navigation agents. The distributional dopamine hypothesis (Dabney et al., 2020) and meta-RL framework (Wang et al., 2018) represent the most concrete mechanistic translations from deep RL to neuroscience.

---

## Open questions

- **Sample efficiency**: Deep RL systems require vastly more experience than humans to reach comparable performance. What biological mechanisms (episodic memory, meta-learning, innate structure) close this gap?

- **Biological plausibility of backpropagation**: Deep RL relies on backpropagation for credit assignment. How might biological circuits approximate backpropagation, or what alternative algorithms achieve similar learning?

- **Flexible structured generalization**: Current deep RL struggles to leverage background knowledge for systematic generalization to novel situations. How do humans achieve this, and can deep RL be extended to capture it?

- **Long-term temporal credit assignment**: Attributing rewards to actions taken far in the past remains challenging. How do biological systems solve this, and can deep RL mechanisms be improved?

- **Catastrophic forgetting**: Deep RL networks lose old knowledge when learning new tasks. How does the brain maintain stable memories while learning new ones?

- **Bidirectional influence**: How can neuroscience inform deep RL development, particularly regarding biological constraints (energy efficiency, heritability, developmental constraints) that current deep RL ignores?

---

## Related pages

- [Reinforcement Learning](reinforcement_learning.md)
- [Model-based RL](model_based_rl.md)
- [Model-free RL](model_free_rl.md)
- [Meta-reinforcement Learning](meta_reinforcement_learning.md)
- [Distributional RL](distributional_rl.md)
- [Hierarchical RL](hierarchical_rl.md)
- [Experience Replay](experience_replay.md)
- [Successor Representation](successor_representation.md)
- [Prefrontal Cortex](../brain_regions/prefrontal_cortex.md)
- [Ventral Tegmental Area](../brain_regions/ventral_tegmental_area.md)
- [Hippocampus](../brain_regions/hippocampus.md)
- [Striatum](../brain_regions/striatum.md)
