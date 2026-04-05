---
source_file: piray2020_linear_reinforcement_learning.md
title: "Linear reinforcement learning: Flexible reuse of computation in planning, grid fields, and cognitive control"
authors: Payam Piray, Nathaniel D. Daw
year: 2020
journal: bioRxiv
paper_type: computational
contribution_type: theoretical
---

### One-line summary

Linear RL reformulates sequential decision-making as a linearly-solvable control problem, enabling efficient flexible planning via the Default Representation (DR)—a policy-independent cognitive map that explains grid cells, border cells, cognitive control costs, and Pavlovian biases within a unified framework.

### Background & motivation

Classic model-based reinforcement learning requires solving the Bellman equation, which involves interdependent nonlinear optimizations across states that are computationally expensive and biologically implausible. The Successor Representation (SR) offers a partial solution by caching state occupancy predictions, but it is policy-dependent and cannot solve replanning tasks where goals change future choice policies. A complete, neurally realistic account of flexible planning and its failures (habits, compulsions) remains lacking.

### Methods

- **Model formulation**: Adapted linearly-solvable Markov decision processes from control theory (Todorov 2007, 2009)
- **Core innovation**: Replaced discrete action optimization with stochastic policy optimization, adding a KL divergence control cost penalizing deviation from a default policy
- **Key derivation**: Showed this formulation yields a linear Bellman equation analytically solvable via matrix operations
- **Default Representation (DR)**: Computed as matrix M = (I - T_NT)^-1, where T_NT is the default policy transition matrix between nonterminal states
- **Simulations**: 
  - 7-level decision tree task comparing linear RL to pruned model-based algorithms
  - Tolman latent learning (reward devaluation) in maze environments
  - Policy revaluation task (Momennejad et al. 2017) with three-stage sequential decisions
  - Tolman detour task (transition revaluation) with barrier insertion
  - Grid field analysis: computed eigenvectors of DR in 2D maze environments
  - Border cell analysis: computed basis functions for DR updates with barriers
  - Stroop task simulation with biased default policy
  - Pavlovian-instrumental transfer (PIT) simulation following Corbit et al. (2007)

### Key findings

- Linear RL achieved near-optimal performance on 7-level decision trees, significantly outperforming depth-limited pruned model-based algorithms
- The DR enables one-shot replanning for reward revaluation: same representation supports planning to any goal without recomputation
- Successfully solved Tolman's latent learning task: correctly avoided devalued end-box on first test trial without re-experiencing trajectories
- Successfully solved policy revaluation task (which defeats SR): updated top-level choices based on new rewards at terminal states without recomputing DR
- Solved transition revaluation (detour tasks) via efficient matrix update using Woodbury identity—no need to recompute entire DR
- Grid cell prediction: Eigenvectors of DR produce periodic, multiscale spatial patterns resembling grid fields; crucially, these are stable under policy changes (unlike SR eigenvectors), consistent with experimental evidence that grid fields are sensitive to barriers but not behavioral patterns
- Border cell prediction: Columns of the low-rank correction matrix for barrier updates resemble entorhinal border cells, unifying grid and border cells as basis functions for map construction
- Cognitive control: Default policy biases explain Stroop effects (prepotent responses favored); control costs (KL divergence) quantified in reward units explain subjective effort; reward incentives reduce errors by offsetting control costs, matching experimental data
- Pavlovian-instrumental transfer: Default policy learned during Pavlovian training biases instrumental choices during test phase even when stimulus is objectively irrelevant; predicts PIT persists under reward devaluation (satiety), consistent with Corbit et al. (2007)

### Computational framework

**Linear Reinforcement Learning (Linear RL)**

A reformulation of Markov decision processes based on control theory (Todorov 2007, 2009) that makes three key modifications to the standard framework:

1. **Stochastic policies**: Actions are treated as probability distributions over successor states rather than discrete choices
2. **Control costs**: A KL divergence penalty penalizes deviation from a default policy π^M, with cost scaled by parameter λ
3. **Linear optimization**: These modifications convert the nonlinear Bellman equation into a linear system solvable by matrix operations

**Core formalism**:
- **Default Representation (DR)**: Matrix M = (I - T_NT)^-1 capturing expected future state occupancies and costs under the default policy
- **Value computation**: v* = M(P·r) where P is transition probabilities to terminal states and r is reward vector
- **Policy**: Softmax over values with default policy as prior: π(a|s) ∝ π^M(a|s) · exp(v*(s')/λ)

The framework treats planning as linear matrix-vector multiplication rather than iterative nonlinear optimization, enabling efficient, biologically plausible computation while introducing soft biases toward the default policy.

### Prevailing model of the system under study

The paper identifies two prevailing theoretical frameworks in the literature:

1. **Model-based planning**: The brain solves the Bellman equation through iterative search (e.g., tree search or replay), computing action values exhaustively. This offers flexibility but is computationally expensive and biologically implausible for complex tasks.

2. **Model-free caching**: The brain caches previously computed action values or policies (e.g., via TD learning), enabling fast choice but sacrificing flexibility. This explains habits and compulsive behaviors but not flexible replanning.

The Successor Representation (SR) was emerging as a compromise: it caches expected state occupancies under a policy, enabling some flexible replanning (reward revaluation) more efficiently than full model-based computation. However, the SR's policy-dependence limited its applicability—it cannot solve policy revaluation or transition revaluation tasks without recomputation.

The field lacked a unified account that could explain both flexible planning (replanning under changed goals or transitions) and the graded, soft biases observed in cognitive control and Pavlovian phenomena.

### What this paper contributes

Linear RL provides a unified computational framework that:

1. **Enables efficient flexible planning**: The DR is policy-independent (depends only on the default policy, not the optimized policy), allowing one-shot replanning for arbitrary goal changes without recomputation. This solves policy revaluation tasks that defeat the SR.

2. **Handles transition changes**: Efficient matrix update rules (Woodbury identity) allow local updates to the DR when barriers or shortcuts are introduced, solving detour/shortcut tasks without full recomputation.

3. **Explains grid cells**: The DR's eigenvectors produce periodic, multiscale spatial patterns resembling entorhinal grid cells. Unlike SR-based accounts, the DR predicts grid fields should be stable under policy changes (only affected by barriers/geometry), matching experimental data showing grid cells are sensitive to walls but not behavioral patterns.

4. **Unifies grid and border cells**: Border cells emerge naturally as columns of the low-rank correction matrix for updating the DR with barriers. Both cell types serve as basis functions for constructing spatial maps.

5. **Explains cognitive control phenomena**: The default policy and control costs (KL divergence) provide a normative account of Stroop effects, effort costs, and the reward-sensitivity of control demands. Deviations from default policies are literally costly in the objective function, quantified in reward units.

6. **Explains Pavlovian-instrumental transfer**: Default policy learning during Pavlovian training biases instrumental choices, even when the Pavlovian cue is objectively irrelevant. Predicts PIT persists under reward devaluation (satiety), consistent with empirical findings.

The framework unifies these diverse phenomena under a single computational principle: efficient planning via soft optimization around learned default policies.

### Brain regions & systems

- **Medial entorhinal cortex**: Contains grid cells and border cells; proposed as neural substrate for the Default Representation (DR). Grid cells encode eigenvectors of the DR (periodic, multiscale spatial basis functions). Border cells encode low-rank correction terms for updating the DR with barriers.

- **Hippocampus**: Contains place fields; proposed to represent one-step transition maps (local spatial adjacencies) that can be composed via the DR for planning.

- **Prefrontal cortex**: Implicated in cognitive control; proposed to implement the value computation and policy optimization components of linear RL, balancing expected rewards against control costs.

- **Ventral tegmental area / striatum**: Implicated in model-free learning; proposed as substrate for learning the default policy via reinforcement learning or habit formation.

Not applicable: The paper is primarily computational; brain region assignments are theoretical proposals rather than empirical findings.

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight as defined in the template. While it presents a formal algorithm (linear RL) and links it to neural representations (grid cells, border cells), it does not provide neural data (recordings, imaging, lesions, pharmacology) that specifically support the algorithm's variables over alternatives.

The paper is purely computational with simulation validation. It proposes that:
- Grid cells encode eigenvectors of the DR (rather than SR)
- Border cells encode low-rank correction terms for barrier updates
- Prefrontal cortex computes value functions and policies
- Striatum/VTA learns default policies

However, these are theoretical predictions rather than empirically validated mechanisms. The paper's contribution is to provide a normative computational framework that explains existing behavioral and neural data (grid cell properties, PIT effects, Stroop effects) under a unified theory, and to generate new testable predictions (e.g., grid cells should be stable under policy changes, DR should incorporate locomotion costs).

### Limitations & open questions

- **Deterministic environments only**: The model assumes deterministic, fully controllable state transitions (one-to-one action-state mapping). It does not directly handle stochastic transitions (e.g., two-step tasks with noisy outcomes) without further approximation.

- **Discrete state spaces**: The model is formulated for discrete state spaces; extension to continuous spaces is mentioned as future work.

- **Terminal state formulation**: The model requires partitioning states into terminal (goals) and nonterminal, which may not always be natural. The paper presents techniques for dynamically changing which states are goals, but this adds complexity.

- **Single goal optimization**: The model does not directly solve multi-goal sequencing problems (though these can be approximated as sequential episodes).

- **Learning the DR**: While the paper discusses several methods for learning or computing the DR (TD learning, matrix inversion, iterative updates), the relative plausibility and neural implementation of these methods remains to be explored.

- **Parameter setting**: The control cost parameter λ and how the default policy is learned or chosen are left open. The paper suggests connections to gain control and normalization, but these remain for future work.

- **Relationship to hierarchical models**: The relationship between linear RL's componential map construction and emerging hierarchical models of grid/place cells (e.g., Tolman-Eichenbaum Machine) remains to be explored.

- **Empirical validation**: Many predictions (e.g., grid cell stability under policy changes, DR incorporating locomotion costs) await direct experimental testing.

### Connections & keywords

**Key citations:**
- Todorov (2007, 2009) - Linearly-solvable MDPs and control theory foundations
- Dayan (1993) - Successor Representation
- Stachenfeld et al. (2017) - SR and hippocampal predictive maps
- Momennejad et al. (2017), Russek et al. (2017) - SR limitations for replanning
- Tolman (1948) - Cognitive maps and latent learning
- Hafting et al. (2005) - Grid cells
- Solstad et al. (2008) - Border cells
- Daw et al. (2005) - Model-based vs model-free RL
- Kappen (2005) - Linear control theory

**Named models or frameworks:**
- Linear Reinforcement Learning (Linear RL)
- Default Representation (DR)
- Successor Representation (SR)
- Markov Decision Processes (MDPs)
- Bellman equation
- Model-based RL
- Model-free RL
- KL divergence control cost
- Woodbury matrix identity
- Graph Laplacian

**Brain regions:**
- Medial entorhinal cortex (grid cells, border cells)
- Hippocampus (place cells)
- Prefrontal cortex (cognitive control)
- Ventral tegmental area
- Striatum

**Keywords:**
reinforcement learning, successor representation, grid cells, border cells, cognitive control, Pavlovian-instrumental transfer, planning, replanning, latent learning, default policy, control cost, KL divergence, linear Bellman equation, cognitive maps, model-based, model-free, entorhinal cortex, decision making, computational neuroscience
