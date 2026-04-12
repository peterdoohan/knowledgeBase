---
source_file: sagiv_experience_replay_prioritization.md
paper_id: sagiv_experience_replay_prioritization
title: "Prioritizing experience replay when future goals are unknown"
authors:
  - "Yotam Sagiv"
  - "Thomas Akam"
  - "Ilana B. Witten"
  - "Nathaniel D. Daw"
year: unknown
journal: unknown
paper_type: computational
contribution_type: theoretical
tasks:
  - open_field
  - linear_track
brain_regions:
  - hippocampus
  - prefrontal_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - successor_representation
keywords:
  - reinforcement_learning
  - experience_replay
  - successor_representation
  - cognitive_map
  - hippocampus
  - spatial_navigation
  - transfer_learning
  - model_based_rl
  - prioritized_sweeping
  - latent_learning
  - prioritizing
  - experience
  - replay
  - when
  - future
  - goals
  - unknown
key_citations:
  - dayan1993_successor_representation
  - russek2017_model_based_reinforcement
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
  - wiki/topics/successor_representation_as_a_predictive_map_for_flexible_planning
---

### One-line summary

Extends rational prioritization accounts of hippocampal replay from value computation to learning flexible cognitive maps via the Geodesic representation, enabling efficient transfer learning when reward functions are unknown or change.

### Background & motivation

Experience replay in the hippocampus has been theorized to support value computation by propagating reward information across states. However, an alternative view suggests replay builds flexible "cognitive maps" for transfer learning. The successor representation (SR) enables such flexibility by decomposing value into state occupancies and reward weights, but prioritization rules for learning SR-like representations in reward-free regimes were lacking.

### Methods

- Developed the Geodesic representation (GR), an off-policy variant of the successor representation suited for task transfer learning
- Derived a Bellman equation for the GR that operates across all goal states simultaneously
- Extended rational prioritization theory to the GR by factorizing expected utility into "need" and "gain" terms
- Need term: expected state occupancy under policy (SR evaluated at current state)
- Gain term: magnitude of policy improvement from the update
- Implemented multi-step replay extension: if current replay step continues an optimal trajectory, perform full n-step backup
- Simulated prioritized replay in three environments: linear track, open field, and bottleneck chamber
- Agent initialized with full one-step transitions; tested prospective planning over initial state distributions with unknown goal locations

### Key findings

- Prioritized GR replay produces coherent sequential sequences without external sequential structure specification
- Linear track: replay proceeds sequentially forward through the entire track when planning prospectively over uniform initial and goal distributions
- Open field: replay meanders forward sequentially through 2D space under uniform distributions
- Bottleneck chamber: replay proceeds backward from goal states toward the bottleneck (corridor entry), building independent sequences from each goal toward the bottleneck before consolidating at the bottleneck and propagating back to the start state
- Consolidation at bottlenecks allows stacking distances to multiple goals before pushing information toward start states
- Prioritization rule enables replay before any rewards are observed, evaluated with respect to a distribution over possible future goals rather than current reward function

### Computational framework

Reinforcement learning with successor representations. The Geodesic representation (GR) is an off-policy variant of the successor representation (SR) that learns shortest-path distances in deterministic MDPs. Unlike standard SR which learns expected discounted state occupancies under a fixed policy, GR treats each state as a potential goal and learns the optimal policy to reach it. The framework assumes: (1) deterministic state transitions, (2) a single absorbing goal state, (3) the agent can perform Bellman backups across all goal states simultaneously, and (4) prioritization follows rational principles of maximizing expected utility decomposed into need (state relevance) and gain (policy improvement) terms. The GR formalism enables transfer learning by separating state occupancy predictions from reward information, allowing rapid replanning when reward functions change.

### Prevailing model of the system under study

Prior to this work, two competing views of hippocampal replay existed. The first, grounded in Dyna-style reinforcement learning, proposed that replay propagates reward information to compute value functions, with prioritization rules explaining observed replay patterns (Mattar & Daw, 2018). The second view suggested replay builds flexible "cognitive maps" or world models for navigation and planning, not specifically tied to reward propagation. However, this cognitive map hypothesis lacked formal computational implementation comparable to the Dyna/value-based account. Additionally, the successor representation had been proposed as a mechanism for transfer learning in reinforcement learning, with neural signatures detected in humans, but its relationship to replay dynamics and prioritization was unexplored.

### What this paper contributes

This paper formalizes the cognitive map hypothesis of replay by extending rational prioritization theory to the reward-free regime. It provides the first normative account of which replay trajectories are most useful for building flexible cognitive maps (as opposed to computing values). Specifically: (1) It derives a prioritization rule for the Geodesic representation that evaluates backups with respect to a distribution over possible future goals rather than the current reward function; (2) It shows this rule yields coherent, sequential replay patterns in simulated environments without requiring external sequential structure; (3) It predicts specific replay dynamics including backward replay from goals, bottleneck consolidation, and prospective replay before reward observation; (4) It bridges the gap between model-based cognitive map theories and reinforcement learning accounts by showing how SR-like representations can be learned through prioritized replay. These contributions enable direct comparison between value-based and cognitive map-based predictions of replay and generate testable predictions for hippocampal recording experiments in pre-reward phases of tasks.

### Brain regions & systems

Hippocampus — proposed locus of prioritized replay for building flexible cognitive maps via the Geodesic representation; replay sequences simulated here match qualitative features of rodent hippocampal replay. Prefrontal cortex — mentioned as potential site for detecting successor representation-like signals during latent learning paradigms. Dopaminergic system — discussed as potentially encoding Geodesic prediction errors as surprise or value-of-information signals during structure learning before reward delivery.

### Mechanistic insight

The paper presents a formal algorithm (the Geodesic representation with prioritized replay) but does not provide neural data supporting this specific algorithm over alternatives. The work proposes that prioritized replay in the hippocampus implements GR learning, but this is a theoretical prediction rather than an empirically validated mechanism. The paper suggests dopamine might encode GR prediction errors and that successor representation signals might be observable in prefrontal cortex or hippocampus, but these are hypotheses for future testing rather than established findings. Because the paper meets only the first criterion (presenting an algorithm) without empirical neural validation, mechanistic insight at Marr's three levels cannot be fully established.

### Limitations & open questions

The paper does not provide an efficiently realizable algorithm for discovering which replay trajectories are most adaptive; it defines optimal prioritization rules but leaves the discovery mechanism for future work. The assumption that the distribution over goals is known to the agent is acknowledged as an oversimplification; inferring this distribution is noted as an interesting question outside the scope. The framework assumes deterministic MDPs and single absorbing goal states, though extensions to arbitrary reward functions and stochastic environments are suggested as straightforward. Empirical validation of the model's predictions (particularly regarding pre-reward replay and bottleneck consolidation) has not yet been conducted. The relationship between Geodesic prediction errors and dopaminergic activity remains hypothetical.

### Connections & keywords

**Key citations:**
- Dayan (1993) — successor representation
- Garvert, Dolan & Behrens (2017) — abstract relational knowledge in hippocampus
- Kaelbling (1993) — learning to achieve goals
- Mattar & Daw (2018) — prioritized memory access and hippocampal replay
- Russek et al. (2017) — predictive representations linking model-based and model-free RL
- Sharpe et al. (2017) — dopamine and model-based associations
- Sutton (1990) — Dyna architecture for learning, planning, and reacting

**Named models or frameworks:**
- Dyna reinforcement learning architecture
- Successor representation (SR)
- Geodesic representation (GR)
- Prioritized experience replay
- Rational prioritization theory
- Cognitive map hypothesis
- Markov Decision Process (MDP)
- Q-learning

**Brain regions:**
- Hippocampus
- Prefrontal cortex

**Keywords:**
reinforcement learning, experience replay, successor representation, cognitive map, hippocampus, spatial navigation, transfer learning, model-based RL, prioritized sweeping, latent learning

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]
- [[wiki/topics/successor_representation_as_a_predictive_map_for_flexible_planning|Successor representation as a predictive map for flexible planning]]
