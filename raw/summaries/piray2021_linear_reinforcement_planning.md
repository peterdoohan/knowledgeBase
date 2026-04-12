---
source_file: piray2021_linear_reinforcement_planning.md
paper_id: piray2021_linear_reinforcement_planning
title: "Linear reinforcement learning in planning, grid fields, and cognitive control"
authors:
  - "Payam Piray"
  - "Nathaniel D. Daw"
year: 2021
journal: "Nature Communications"
paper_type: computational
contribution_type: theoretical
tasks:
  - detour_task
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - prefrontal_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - successor_representation
keywords:
  - linear_reinforcement_learning
  - default_representation
  - successor_representation
  - cognitive_maps
  - grid_cells
  - border_cells
  - planning
  - replanning
  - model_based_rl
  - cognitive_control
  - habits
  - pavlovian_instrumental_transfer
  - stroop_effect
  - reward_revaluation
  - policy_revaluation
  - detour_task
  - kl_divergence
  - temporally_abstract_representations
  - entorhinal_cortex
  - decision_making
key_citations:
  - dayan1993_successor_representation
  - stachenfeld2017_hippocampus_predictive_map
  - tolman1948_cognitive_maps_rats
  - momennejad2017_successor_representation_humans
  - russek2017_model_based_reinforcement
  - botvinick2012_planning_inference
---

### One-line summary

A linear reinforcement learning model that reuses a temporally abstracted map (the Default Representation) enables biologically realistic flexible planning while explaining cognitive biases, grid cells, border cells, and Pavlovian-instrumental transfer through a unified framework.

### Background & motivation

The brain exhibits both remarkable flexibility in planning and puzzling inflexibilities in habits and compulsions. Classic reinforcement learning models distinguish between model-based planning (flexible but computationally expensive) and model-free caching (inflexible but efficient). The successor representation (SR) offers a middle ground but fails to fully explain flexible replanning because it depends on a fixed policy. A key unresolved problem is the interdependence of optimal actions across states: the best action now depends on the best action at the next state, creating an exponentially complex optimization problem that lacks a biologically realistic solution.

### Methods

- **Model architecture**: Linear RL is based on Todorov's linearly solvable Markov decision processes (MDPs), which reformulate the Bellman equation to make it linear rather than nonlinear.
- **Key innovation**: The model optimizes a stochastic policy over successor states while paying a control cost (KL divergence from a default policy) rather than computing a deterministic max over actions.
- **Default Representation (DR)**: A precomputed matrix M measuring expected aggregate cost to all future visits between states under the default policy, computed as M = (I - T_NN)^(-1) where T_NN is the default transition matrix between nonterminal states.
- **Policy form**: The optimal policy is a weighted softmax where weights are given by the default policy: π*(s'|s) ∝ π^d(s'|s) * exp(v*(s')/λ).
- **Simulation tasks**: Seven-level decision tree, 2D maze navigation (50×50 and 10×10), Tolman's latent learning task, policy revaluation task, Tolman's detour task, two-step Markov decision task, Stroop task simulation, Pavlovian-instrumental transfer task.

### Key findings

- Linear RL achieves near-optimal performance on a seven-level decision tree task while being computationally tractable, outperforming depth-limited pruned model-based algorithms (D1-D6) that approximate the SR.
- The DR is independent of goals and optimized policies, enabling efficient replanning for any reward function without recomputation (unlike the SR which requires policy-specific recomputation).
- Linear RL successfully solves Tolman's latent learning task (reward devaluation) by using the precomputed DR with updated reward values, matching rat behavior of avoiding devalued outcomes without direct experience.
- Linear RL solves "policy revaluation" tasks that defeat the SR, where changes in terminal state rewards imply changes in choice policies at intermediate states; the SR cannot handle this because it assumes fixed intermediate choices.
- Linear RL solves Tolman's detour task (environmental change) using a low-rank matrix update (Woodbury identity) to modify the DR when barriers are introduced, without full recomputation.
- The eigenvectors of the DR produce periodic grid-like patterns similar to entorhinal grid cells, but critically remain stable across changes in goals and policies (unlike SR eigenvectors which change with policy).
- The low-rank correction matrix for barrier updates resembles entorhinal border cells, unifying grid and border cells as basis functions for a componential map representation.
- Extended to stochastic environments, linear RL successfully produces model-based patterns in the two-step task (stay/switch behavior contingent on common vs. rare transitions).
- The control cost parameter λ quantifies the "cost of cognitive control" in units of reward; higher costs lead to stronger biases toward default (prepotent) responses, explaining Stroop effects and other cognitive control phenomena.
- Increasing rewards can overcome control costs, predicting that reward incentives reduce Stroop errors, which matches empirical findings.
- The default policy, when learned through overtraining, produces soft habits that are graded and context-dependent rather than all-or-none, explaining both beneficial transfer and maladaptive perseveration.
- Linear RL explains Pavlovian-instrumental transfer (PIT) as biases from the learned default policy; conditioned stimuli shift the default toward associated outcomes, biasing choice even when the stimulus is objectively irrelevant to action-outcome contingencies.
- PIT effects persist even without reward (under satiety), which linear RL explains because the default policy is based on sensory-state associations rather than reward value per se.

### Computational framework

The paper introduces **linear reinforcement learning** (linear RL), a framework based on Todorov's linearly solvable MDPs. The key insight is that by reformulating the decision problem to optimize a stochastic policy with a KL-divergence control cost (relative to a default policy), the nonlinear Bellman equation becomes linear and analytically solvable.

The core formalism:
- **State space**: Divided into terminal states (goals with rewards) and nonterminal states (traversal states with costs)
- **Default policy (π^d)**: A baseline stochastic policy representing soft assumptions about future actions
- **Control cost**: λ·KL(π||π^d), penalizing deviation from default in units of reward
- **DR (Default Representation)**: Matrix M = (I - T_NN)^(-1), encoding expected future visit costs between nonterminal states under the default policy
- **Optimal values**: Computed linearly as v* = M · P · exp(r/λ), where P connects nonterminal to terminal states
- **Optimal policy**: Softmax around default: π*(s'|s) ∝ π^d(s'|s) · exp(v*(s')/λ)

This framework replaces the recursive "max" operation with a log-average-exp (softmax) that is differentiable and enables linear solution. The control cost captures the approximation error between the true optimal and the linear solution.

### Prevailing model of the system under study

The prevailing model in decision neuroscience distinguishes between two systems: a computationally expensive but flexible "model-based" system that uses internal models for planning, and a fast but inflexible "model-free" system that caches previously computed values. The successor representation (SR) has emerged as an intermediate approach, storing expected future state occupancies under a learned policy to enable some flexible transfer. However, the SR inherits a critical limitation: because it computes values under a fixed policy, it cannot flexibly replan when goals change in ways that imply different choice policies at intermediate states. The prevailing view also lacks a unified account of how flexible planning relates to cognitive control phenomena and response biases, treating these as separate research areas.

### What this paper contributes

This paper introduces **linear RL** as a unified computational framework that addresses the interdependence problem in sequential decision-making. Unlike the SR, which is tied to a fixed policy, the Default Representation (DR) is stable across goal changes and can efficiently compute new optimal policies without recomputation. This enables the model to solve reward revaluation, policy revaluation, and detour tasks that defeat the SR.

The framework also provides a normative account of cognitive control costs: the KL-divergence penalty for deviating from the default policy quantifies control demands in reward units, explaining why prepotent responses are harder to override and why rewards can facilitate control. The learned default policy produces soft, graded habits rather than all-or-none cached values, explaining both adaptive transfer and maladaptive perseveration.

The paper unifies entorhinal grid cells and border cells within the same framework: grid cells encode eigenvectors of the DR (stable basis functions for planning), while border cells represent low-rank correction terms for environmental barriers. This explains why grid fields are robust to behavioral changes but sensitive to environmental geometry, and provides a componential code for cognitive maps.

Finally, the model explains Pavlovian-instrumental transfer as default policy biases learned from Pavlovian associations, predicting that PIT effects persist under satiety because they reflect sensory-state contingencies rather than reward value per se.

### Brain regions & systems

- **Medial entorhinal cortex**: Proposed locus of Default Representation (DR) encoding. Grid cells in this region are hypothesized to represent eigenvectors of the DR matrix, providing a stable, periodic basis for long-range spatial relationships under the default policy. The model predicts grid fields should be stable across changes in goals and policies but sensitive to environmental geometry (barriers).
- **Medial entorhinal cortex (border cells)**: Border cells are proposed to represent low-rank correction matrices for updating the DR when barriers are introduced. These cells, which fire near environmental boundaries, are unified with grid cells as part of a componential code for cognitive maps.
- **Hippocampus**: Implicitly involved in representing the one-step transition map and local state representations, though the paper focuses primarily on entorhinal representations for long-range planning.
- **Prefrontal cortex**: Not explicitly discussed, but the cognitive control mechanisms implied by the model (overriding default policies) likely engage prefrontal systems.

### Mechanistic insight

The paper provides a **computational-level** account that partially bridges to algorithmic and implementational levels.

**Computational**: The brain solves sequential decision problems by approximately maximizing expected reward subject to a control cost for deviating from default policies. This reformulation makes the problem linearly solvable, avoiding the exponential complexity of exact planning.

**Algorithmic**: The solution involves three key representations: (1) the Default Representation (DR) matrix encoding expected future state visit costs under the default policy, computed as M = (I - T_NN)^(-1); (2) the transition matrix P from nonterminal to terminal states; and (3) reward vector r over terminal states. Optimal values are computed linearly as v* = M·P·exp(r/λ), and policies are derived via softmax. The DR can be learned via TD learning, computed via matrix inversion, or updated incrementally using the Woodbury identity for barriers/shortcuts.

**Implementational**: The eigenvectors of the DR produce periodic grid-like fields similar to entorhinal grid cells, while the low-rank correction terms for barriers resemble border cells. This suggests entorhinal cortex implements the DR using basis function decomposition. The matrix-vector multiplication for value computation could be implemented in a single neural network layer.

The paper does not meet the full bar for mechanistic insight because it lacks direct neural data validating the specific algorithmic predictions (e.g., demonstrating that grid cells actually encode DR eigenvectors rather than SR eigenvectors, or that border cells compute barrier corrections). The evidence cited is correlational and theoretical rather than causal or recording-based.

### Limitations & open questions

- The model assumes deterministic, fully controllable environments (one-to-one action-state mapping), which excludes many real-world tasks with irreducibly stochastic transitions. While an approximation for stochastic tasks is demonstrated (two-step task), it fails in some constructed scenarios where action interdependence matters across stochastic transitions.
- The division between terminal and nonterminal states is theoretically flexible but empirically underconstrained. The model treats discrete outcomes (food, shock) as terminal, but the criteria for this classification are not fully specified.
- The model does not directly address multi-goal sequential planning (visiting multiple goals in sequence), though this can be approximated by episode segmentation or subgoal inclusion.
- The learning dynamics of the default policy and how it interacts with the DR over development and experience are simplified in the current model.
- The neural evidence for DR vs. SR encoding in entorhinal cortex is indirect; direct electrophysiological tests distinguishing these predictions are needed.
- The relationship between linear RL and other frameworks (Bayesian planning-as-inference, hierarchical RL, predictive coding) requires further theoretical development.

### Connections & keywords

**Key citations**: Todorov (2007, 2009) - foundational linear RL theory; Dayan (1993) - successor representation; Stachenfeld et al. (2017) - SR and grid cells; Daw et al. (2005, 2011) - model-based/model-free distinction; Tolman (1948) - cognitive maps and latent learning; Momennejad et al. (2017), Russek et al. (2017) - SR limitations for replanning; Derdikman et al. (2009), Barry et al. (2007) - grid cell experimental data; Solstad et al. (2008) - border cells; Shenhav et al. (2013, 2017) - cognitive control costs; Corbit et al. (2007) - Pavlovian-instrumental transfer; Botvinick & Toussaint (2012) - planning as inference.

**Named models or frameworks**: Linear reinforcement learning (linear RL), Default Representation (DR), Successor Representation (SR), Markov decision processes (MDPs), Model-based RL, Model-free RL, Z-learning, Soft Q-learning, Woodbury matrix identity, KL divergence control cost, Graph Laplacian, Tolman's latent learning, Tolman's detour task, Two-step Markov decision task, Stroop task, Pavlovian-instrumental transfer (PIT).

**Brain regions**: Medial entorhinal cortex (grid cells, border cells), hippocampus (place cells, one-step transition map), prefrontal cortex (implied for cognitive control).

**Keywords**: linear reinforcement learning, default representation, successor representation, cognitive maps, grid cells, border cells, planning, replanning, model-based RL, cognitive control, habits, Pavlovian-instrumental transfer, Stroop effect, reward revaluation, policy revaluation, detour task, KL divergence, temporally abstract representations, entorhinal cortex, decision making, control costs.
