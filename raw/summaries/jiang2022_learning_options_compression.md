---
source_file: jiang2022_learning_options_compression.md
paper_id: jiang2022_learning_options_compression
title: "Learning Options via Compression"
authors:
  - "Yiding Jiang"
  - "Evan Zheran Liu"
  - "Benjamin Eysenbach"
  - "J. Zico Kolter"
  - "Chelsea Finn"
year: 2022
journal: "NeurIPS 2022 (36th Conference on Neural Information Processing Systems)"
paper_type: computational
contribution_type: methodological
brain_regions:
  - ventral_tegmental_area
frameworks:
  - reinforcement_learning
  - hierarchical_rl
keywords:
  - skill_learning
  - temporal_abstraction
  - hierarchical_reinforcement_learning
  - minimum_description_length
  - compression_objective
  - latent_variable_model
  - options_framework
  - multi_task_reinforcement_learning
  - offline_reinforcement_learning
  - underspecification
  - variational_inference
  - sample_efficiency
  - learning
  - options
  - via
  - compression
---

### One-line summary

LOVE (Learning Options via Compression) addresses the underspecification problem in skill learning by combining a maximum likelihood objective with a minimum description length penalty, producing skills that are semantically meaningful and accelerate learning of new tasks in hierarchical reinforcement learning.

---

### Background & motivation

In multi-task reinforcement learning, extracting reusable skills from offline demonstrations can accelerate learning of new tasks. Prior methods learn skills by maximising the likelihood of pre-collected experience using latent variable models, but this maximum likelihood objective is underspecified: many decompositions of experience into skills achieve equally high likelihood, including degenerate solutions (e.g. single-timestep skills or one skill per full trajectory). This underspecification means the learned skills may be of limited use for downstream task learning. The paper asks whether compression — specifically the minimum description length (MDL) principle — can serve as a principled objective that resolves this underspecification by forcing skills to capture common reusable structure.

---

### Methods

- **Model architecture**: Extends Variational Temporal Abstraction (VTA; Kim et al., 2019) to interaction data (state-action sequences). A graphical model segments trajectories using binary boundary variables **m** and labels each segment with a discrete skill variable **z**. Three learned components: a skill policy, a termination policy, and a skill posterior.
- **Objective**: Combines the ELBO of the maximum likelihood objective (L_ELBO) with a compression objective (L_CL) that minimises the expected number of bits required to encode trajectories using the learned skill representation. The compression term equals the marginal entropy of the skill distribution multiplied by the average number of skills per trajectory. Optimisation is framed as a constrained problem (minimise L_CL subject to L_ELBO ≤ C), solved via dual gradient descent.
- **Implementation**: Discrete skills using Gumbel-softmax; a minimum skill length of 3 timesteps is enforced during training to avoid local optima from single-action skills. Best model selected across 3 random restarts.
- **Downstream use**: Learned skills augment the agent's action space; a new hierarchical policy is trained using dueling double DQN with epsilon-greedy exploration over the augmented space.
- **Validation datasets**:
  - Simple synthetic sequential datasets (Simple Colors, Conditional Colors) for isolated evaluation of the compression objective.
  - 2D multi-task 10×10 grid world (object-collection tasks, adapted from Kipf et al. 2019) with sparse and dense reward variants.
  - 3D visual multi-task domain with high-dimensional egocentric pixel observations (400×60×3 RGB arrays).
- **Comparisons**: VTA (Kim et al. 2019), DDO (Fox et al. 2017), and variants of each with the minimum skill length constraint. Behavior cloning baseline also included.

---

### Key findings

- On Simple Colors, LOVE achieves an F1 boundary recovery score of 0.91 ± 0.02 vs 0.82 ± 0.13 for VTA, while achieving a similar ELBO (demonstrating that underspecification occurs even in trivially simple sequential data).
- On the 2D grid world, LOVE is the only method achieving high returns under both sparse and dense reward conditions and for both N_pick=3 and N_pick=5 (generalisation setting). With sparse reward and N_pick=5, LOVE achieves near-optimal returns while all other methods achieve approximately 0.
- In the generalisation setting (N_pick=5, sparse), DDO with minimum skill length eventually learns but requires more than 8× the environment interactions.
- On the 3D visual domain (high-dimensional pixel observations, sparse reward, N_pick=4), LOVE is the only method achieving near-optimal returns; all VTA and DDO variants (with and without minimum skill length) fail to learn.
- LOVE's compression objective with dual gradient descent consistently outperforms hand-tuned λ weighting (F1 of 0.99 ± 0.00 vs up to 0.95 ± 0.06 for best fixed λ).
- Skill quality analysis: LOVE achieves precision/recall of 0.90/0.94 for identifying natural segmentation boundaries (move-to-object + pick-up), vs 0.19/0.99 for VTA and DDO (high recall but near-zero precision due to single-action degenerate skills).

---

### Computational framework

The paper uses the **minimum description length (MDL) principle** applied to latent variable models for hierarchical reinforcement learning.

The core formalism is a latent variable graphical model (extending VTA) over state-action trajectories. Key variables: binary boundary indicators **m_t** (when a new skill begins), discrete skill descriptors **z_t** (shared within a skill segment), and state abstractions **s_t**. The framework assumes that a useful skill decomposition is one that minimises the expected code length of communicating the sequence of skill assignments at boundary points, under an optimal prior equal to the empirical marginal of skills. This compression cost decomposes as: L_CL = n_s × H[z], where n_s is the average number of skills per trajectory and H[z] is the marginal entropy of the skill distribution. The framework assumes that extracting common temporal structure (compression) and extracting useful reusable skills are equivalent objectives.

---

### Prevailing model of the system under study

The paper's introduction frames the prevailing approach as learning skills by maximising the likelihood of offline experience using latent variable models (e.g. VTA, DDO). The working model is that finding a good segmentation of trajectories into labelled subsequences that reconstructs the data well will yield useful, reusable temporal abstractions (options). Prior work treats the maximum likelihood objective as sufficient for this purpose. The paper argues this is incorrect: likelihood maximisation is fundamentally underspecified for skill learning because many decompositions achieve equally high likelihood without capturing the common structure that makes skills transferable.

---

### What this paper contributes

The paper demonstrates that the maximum likelihood objective is definitively insufficient for skill learning — even on trivially simple sequential data, degenerate solutions are found. It shows that augmenting the objective with an MDL compression penalty resolves this underspecification, producing skills with higher semantic coherence (recovering natural task boundaries) and substantially better downstream sample efficiency. The key new claim is that compression and useful skill learning are aligned objectives: skills that compress experience must extract common structure, and common structure is exactly what makes skills reusable. The method also scales to high-dimensional pixel observations, a regime where prior offline skill-learning methods had not been demonstrated.

---

### Brain regions & systems

Not applicable. This is a pure machine learning paper with no anatomical or neural focus. The level of analysis is computational/algorithmic: the paper concerns algorithms for temporal abstraction and skill discovery in sequential decision-making agents, with no reference to biological neural systems.

---

### Mechanistic insight

The paper does not meet the bar for this section. It proposes a novel objective (compression via MDL) for skill learning and validates it with behavioural metrics in simulated RL environments, but provides no neural data of any kind. There are no recordings, imaging, lesion, or pharmacological experiments. The paper operates entirely at the computational and algorithmic levels of Marr's hierarchy, with no claims about neural implementation.

---

### Limitations & open questions

- LOVE relies on the assumption that pre-collected demonstrations share consistent and reusable temporal structure. It may overfit to noisy or task-specific behaviours in more heterogeneous offline datasets (e.g. D4RL-style data).
- The MDL connection is formalised only for the message-length term of a crude two-part code; the model-length term (complexity of the neural network itself) is not directly minimised, and how to do so for neural networks remains an open challenge.
- The method learns closed-loop skills but the compression objective applies regardless of whether skills will generalise — there is no explicit mechanism ensuring transferability beyond the inductive bias from compression.
- The minimum skill length constraint (T_min = 3) is an ad hoc stabilisation heuristic rather than a principled design choice.
- Whether the approach extends beyond multi-task demonstration settings to fully offline or online RL without structured demonstrations is not addressed.

---

### Connections & keywords

**Key citations**:
- Kim, Ahn, Bengio (2019) — Variational Temporal Abstraction (VTA), the foundational graphical model extended by LOVE.
- Kipf et al. (2019) — CompILE; introduced the multi-task grid world benchmark and a competing skill-learning approach.
- Fox, Krishnan, Stoica, Goldberg (2017) — Discovery of Deep Options (DDO); primary comparison method.
- Rissanen (1978) — Minimum description length principle.
- Sutton, Precup, Singh (1999) — Options framework for temporal abstraction in RL.

**Named models or frameworks**:
- LOVE (Learning Options via Compression)
- VTA (Variational Temporal Abstraction)
- DDO (Discovery of Deep Options)
- CompILE (Compositional Imitation Learning and Execution)
- Minimum Description Length (MDL)
- Options framework / hierarchical reinforcement learning (HRL)
- Gumbel-softmax / vector quantisation for discrete latent variables

**Brain regions**: Not applicable.

**Keywords**: skill learning, temporal abstraction, hierarchical reinforcement learning, minimum description length, compression objective, latent variable model, options framework, multi-task reinforcement learning, offline reinforcement learning, underspecification, variational inference, sample efficiency
