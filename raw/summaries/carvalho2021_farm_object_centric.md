---
source_file: carvalho2021_farm_object_centric.md
paper_id: carvalho2021_farm_object_centric
title: "Feature-Attending Recurrent Modules for Generalizing Object-Centric Behavior"
authors:
  - "Wilka Carvalho"
  - "Andrew Lampinen"
  - "Kyriacos Nikiforou"
  - "Felix Hill"
  - "Murray Shanahan"
year: 2021
journal: "ICLR (inferred from venue context; paper references 2021 submissions)"
paper_type: computational
contribution_type: methodological
frameworks:
  - reinforcement_learning
keywords:
  - object_centric_reinforcement_learning
  - feature_attention
  - modular_recurrent_networks
  - generalisation
  - spatiotemporal_representations
  - inductive_biases
  - state_representation_learning
  - zero_shot_generalisation
  - pomdp
  - multi_module_architecture
  - object_induced_structural_regularities
  - recurrent_independent_mechanisms
  - feature
  - attending
  - recurrent
  - modules
  - generalizing
  - object
  - centric
  - behavior
---

### One-line summary

FARM (Feature-Attending Recurrent Modules), a modular recurrent architecture that distributes agent state across multiple modules using dynamic feature attention, outperforms spatial-attention-based architectures at generalizing object-centric RL tasks to larger, more complex settings.

---

### Background & motivation

Generalizing across object-centric tasks requires an RL agent to capture and exploit structure induced by objects across states, transitions, and reward functions. Prior approaches either hard-coded object features, used complex object-centric generative models requiring strong assumptions (e.g. full observability, regular shapes), or leveraged spatial attention — all with limited generalization success. The gap this paper addresses is the lack of a simple, broadly applicable architecture that can discover object-induced regularities across diverse environments using only weak inductive biases.

---

### Methods

- **Architecture**: FARM distributes agent state across n recurrent modules (each implemented as an LSTM). At each timestep, a shared convolutional observation encoder (ResNet + ConvLSTM) produces structured spatiotemporal features Z_t ∈ R^{m×d_z} — features shared across m spatial positions that capture both visual and temporal (motion) information.
- **Feature attention**: Each module generates a query from its previous state, action, and reward, then predicts feature coefficients applied uniformly across all spatial positions (dynamic feature attention). This allows attending to object-motion patterns anywhere in the observation.
- **Module communication**: Before updating, each module retrieves information from other modules via transformer-style (key-query-value) attention.
- **Training**: IMPALA distributed actor-learner setup, Adam optimiser, ~5–8M parameters per model. Sample budgets up to 2 billion frames.
- **Environments (three task suites)**:
  - *Ballet* (2D gridworld): agent must remember which of m ballet dancers (with distinct motions) was indicated by a post-hoc language instruction. Train on m={2,4}, test on m=8.
  - *3D Unity environment* (Hill et al., 2020): embodied agent must place objects on other objects in larger rooms with more distractors (zero-shot generalisation to novel object combinations).
  - *KeyBox* (2D gridworld, custom): agent navigates a sequence of hallways retrieving colour-matched keys; test levels (2n_max, 3n_max) are longer than training levels (up to n_max=10).
- **Baselines**: LSTM, Attention Augmented Agent (AAA; spatial attention), Recurrent Independent Mechanisms (RIMs; spatial attention + multiple modules).
- **Ablations**: presence/absence of recurrent encoder, feature attention, and multiple modules.

---

### Key findings

- FARM is the only architecture achieving above-chance performance on the Ballet task generalisation (m=8 dancers unseen at training), with success rates well above the 1/m chance level; LSTM, AAA, and RIMs all fail.
- Ablations on Ballet show that *either* multiple modules *or* feature attention (given spatiotemporal features) is sufficient for learning the task, but spatial attention actually removes the benefit of multiple modules.
- On the 3D Unity task, FARM achieves ~60–80% generalisation success; both spatial-attention baselines learn more slowly than even a plain LSTM, suggesting spatial attention interferes with RL in 3D object environments.
- On KeyBox (dense setting), FARM generalises ~20 percentage points better than AAA and ~30 points better than RIMs; in sparse setting, FARM matches or exceeds AAA on longer test levels.
- Ablations consistently show that both feature attention and multiple modules contribute to generalisation; their combination is synergistic (learning multiple modules improves memory, obstacle avoidance, and language-grounded tasks simultaneously).
- Analysis of module-state representations reveals that subsets of modules jointly represent distinct object-centric task events (e.g. obstacle avoidance, goal-key pickup), with rich correlation/anti-correlation patterns analogous to word-embedding dimensions — distinct from the specialisation pattern reported for RIMs.

---

### Computational framework

**Reinforcement learning + recurrent state representation learning.**

The paper frames the problem as a POMDP: the agent must learn a compressed agent state s^A_t = η(o_t, a_{t-1}, r_{t-1}, s^A_{t-1}) sufficient for policy optimisation. FARM's novelty is in how this state is structured: distributed across n module-LSTMs rather than a single recurrent unit. Key assumptions:
- Object-induced regularities are captured by subsets of spatial features shared across locations (motivating feature attention over spatial attention).
- Distributing state across modules enables flexible recombination of object-centric experience subsets, supporting zero-shot generalisation.
- Temporal regularities (motion) are best represented by a recurrent observation encoder that propagates feature information across time before modules attend to it.

The core formalism involves: (1) structured spatiotemporal features Z_t from a ConvLSTM encoder; (2) dynamic feature attention u^k_t = f_att^k(Z_t, q^k_{t-1}) via element-wise feature coefficients; (3) inter-module transformer attention ν^k_t = f_share^k(s^A_{t-1}, q^k_{t-1}); and (4) per-module LSTM updates. Training uses V-trace (IMPALA) with entropy regularisation.

---

### Prevailing model of the system under study

The paper's introduction situates it against prevailing approaches to object-centric generalisation in deep RL. The dominant assumption is that objects are best captured through *spatial* attention — attending to individual spatial locations to isolate object representations — as demonstrated by AAA (Mott et al., 2019) and RIMs (Goyal et al., 2020b), both of which achieved strong distractor-generalisation results. An alternative strand hard-codes object features (object-oriented MDPs, successor features). The implicit working model is that spatial locality is the right inductive bias for isolating objects, and that more complex object-centric generative models (e.g. COBRA/MONet) provide the best representations at the cost of strong assumptions. The paper pushes against both: it argues that *feature*-level (non-spatial) attention is a weaker, more general inductive bias that works across diverse task types where spatial attention fails.

---

### What this paper contributes

The key contribution is empirical and methodological: FARM demonstrates that *feature attention* (attending to what is present across all spatial positions simultaneously) generalises across a broader range of object-centric tasks than spatial attention, particularly for tasks defined by object *motions* and 3D object navigation where spatial attention actively hurts performance. The paper establishes that the synergy between feature attention and multiple modules — rather than either alone — is what drives strong generalisation across memory and navigation tasks. It also challenges the finding from RIMs that modules "specialise": in FARM, multiple modules *jointly* represent task regularities, suggesting a qualitatively different representational strategy. Before this paper, it was unclear whether spatial attention's success in distractor generalisation would extend to motion-defined tasks; this paper shows it does not, and provides a working alternative.

---

### Brain regions & systems

Not applicable. This is a purely computational/machine learning paper with no neurobiological measurements. The level of analysis is algorithmic and implementational within artificial neural network architectures. The results may constrain theories of how biological systems represent object-induced structure — particularly regarding whether spatial vs. feature-based attention mechanisms are used in hippocampal-entorhinal or prefrontal circuits for generalisation — but the paper makes no direct claims about neural systems.

---

### Mechanistic insight

The paper does not meet the bar. It proposes an architectural mechanism (feature attention + distributed modular state) and provides behavioural generalisation evidence in RL agents, along with representational analyses of module activity. However, it contains no neural data (recordings, imaging, lesions, pharmacology) linking the proposed algorithm to measured biological activity. The mechanistic claim is that distributing state across modules with feature attention enables flexible recombination of object-centric experiences, supported only by ablation results and module-state analyses in artificial agents.

---

### Limitations & open questions

- Feature attention in FARM is not spatially invariant: by treating all spatial positions as unique after flattening, the architecture cannot generalise to the same feature pattern appearing at a new location in a spatially-invariant way. The authors flag this as a limitation and suggest future work on spatially invariant feature attention.
- FARM's ability to capture long temporal regularities is limited by the LSTM memory horizon; the authors suggest integrating FARM with Transformers for longer sequences.
- The experiments use deterministic, partially-observable, pixel-based environments. Generalisation to stochastic or fully observable settings is untested.
- The "top-k" sparse activation used in RIMs was excluded from comparison due to computational cost, which may have disadvantaged RIMs.
- The paper does not address whether FARM's advantages scale to real-world or continuous-control settings.
- The claim that subsets of modules jointly represent regularities is supported by correlational analyses but not by causal intervention experiments.

---

### Connections & keywords

**Key citations**:
- Mott et al. (2019) — Attention Augmented Agent (AAA), spatial attention baseline
- Goyal et al. (2020b) — Recurrent Independent Mechanisms (RIMs), modular + spatial attention baseline
- Lampinen et al. (2021) — Ballet environment; hierarchical memory for RL agents
- Hill et al. (2020) — 3D Unity environment; environmental drivers of systematicity
- Chevalier-Boisvert et al. (2019) — BabyAI environment; hyperparameter tuning task
- Perez et al. (2018) — FiLM conditioning; feature-coefficient attention mechanism
- Chaplot et al. (2018) — Gated-attention for language grounding; related feature attention
- Espeholt et al. (2018) — IMPALA; training algorithm
- Vaswani et al. (2017) — Transformer attention; inter-module communication

**Named models or frameworks**:
- FARM (Feature-Attending Recurrent Modules) — the proposed architecture
- LSTM (Long Short-Term Memory) — baseline
- AAA (Attention Augmented Agent) — spatial attention baseline
- RIMs (Recurrent Independent Mechanisms) — modular + spatial attention baseline
- IMPALA — distributed RL training algorithm
- POMDP — problem formulation
- Ballet, KeyBox, 3D Unity — task/environment suites

**Brain regions**: Not applicable (no neurobiological content).

**Keywords**: object-centric reinforcement learning, feature attention, modular recurrent networks, generalisation, spatiotemporal representations, inductive biases, state representation learning, zero-shot generalisation, POMDP, multi-module architecture, object-induced structural regularities, recurrent independent mechanisms
