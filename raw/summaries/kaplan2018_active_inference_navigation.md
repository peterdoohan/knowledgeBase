---
source_file: "kaplan2018_active_inference_navigation.md"
paper_id: "kaplan2018_active_inference_navigation"
title: "Planning and navigation as active inference"
authors: "Raphael Kaplan, Karl J. Friston"
year: 2018
journal: "Biological Cybernetics"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["navigation_task"]
methods: ["fmri"]
brain_regions: ["hippocampus", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "ventral_tegmental_area", "substantia_nigra"]
frameworks: ["reinforcement_learning", "model_free_rl", "successor_representation", "active_inference", "bayesian_inference", "hierarchical_rl"]
keywords: ["planning", "navigation", "active", "inference"]
key_citations: ["stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

Active inference over Markov decision processes provides a unified, normative account of epistemic (novelty-driven) exploration and pragmatic (goal-directed) navigation, dissolving the exploration–exploitation dilemma via minimisation of expected free energy.

---

### Background & motivation

Navigation and planning require integrating knowledge about world structure with current goals, but the optimal balance between exploring an uncertain environment and exploiting known routes has long posed a theoretical challenge. Reinforcement learning formulations typically treat exploration and exploitation as competing objectives and struggle with high-dimensional, partially observable state spaces. This paper offers both a normative and process theory for planning and navigation in novel environments, framed within the active inference (free-energy minimisation) framework, with the aim of generating testable predictions about behaviour and neurophysiological responses.

---

### Methods

- **Model architecture**: Active inference under discrete-state-space Markov decision processes (MDPs), using the standard (A, B, C, D) generative model parameterisation: likelihood matrix A, transition matrices B, prior preferences C, initial state priors D.
- **Task environment**: An 8×8 grid maze explored via simulated saccadic eye movements; two outcome modalities — *what* (open/closed cell) and *where* (veridical location); policies limited to two-step sequences (25 possible combinations of 5 actions).
- **Key variables**: Expected free energy G decomposed into epistemic value (novelty from uncertainty about model parameters A; salience from uncertainty about hidden states) and extrinsic/pragmatic value (prior preferences over outcomes); precision γ as an inverse-temperature parameter governing policy confidence.
- **Subgoal heuristic**: Prior preferences derived from a graph-Laplacian diffusion heuristic based on reachability from the target location, enabling hierarchical planning with finite-horizon policies.
- **Simulations**: (1) Pure epistemic exploration of a novel maze; (2) navigation in a familiar maze using task-set priors; (3) goal-directed exploration integrating both epistemic and pragmatic value simultaneously.
- **Predicted signals**: Simulated firing rates, local field potentials (including theta–gamma coupling), and dopaminergic precision-update signals as model outputs.
- **Implementation**: SPM MATLAB routines (spm_MDP_VB_X.m); reproducible via the SPM DEM toolbox "Maze learning demo".

---

### Key findings

- Epistemic foraging driven purely by novelty (parameter uncertainty) produces efficient, non-repetitive exploration of the maze without requiring stochastic noise or explicit memory of visited locations — "memory" is implicitly encoded via Hebbian updates to likelihood parameters.
- Goal-directed navigation emerges naturally once task-set prior preferences are introduced; a graph-Laplacian diffusion heuristic generates context-sensitive subgoals that lead the agent to the target across successive trials, with near-optimal performance achieved after approximately 16 seconds of prior exploration.
- When epistemic and pragmatic value are combined, exploration is initially dominated by novelty (curiosity) until uncertainty is sufficiently resolved, at which point goal-seeking takes over — the exploration–exploitation dilemma is dissolved without requiring explicit arbitration.
- Simulated electrophysiological responses show theta–gamma coupling arising naturally from slow (theta-rate) environmental sampling entraining fast (gamma-rate) belief-updating iterations.
- Simulated dopaminergic signals (precision updates) predict largest phasic responses at intermediate familiarity, not at the earliest or latest stages of learning — a testable, counter-intuitive prediction.
- The process theory predicts a continuum between "path cells" (units encoding hidden states at the *start* of a subpath, maintaining firing until a subgoal is reached) and "place cells" proper (units encoding hidden states at the *end* of a subpath, firing only upon arrival) — place cells are the limiting case of path cells.

---

### Computational framework

**Active inference / variational free energy minimisation** over discrete-state Markov decision processes.

The agent maintains approximate posterior beliefs Q over hidden states s, policies π, precision γ, and likelihood parameters A. It minimises variational free energy F (a functional of these beliefs) via gradient descent. Policy selection is governed by expected free energy G:

G(π) ≈ epistemic value (salience + novelty) + extrinsic value (negative expected surprise under prior preferences C)

Key assumptions:
- Bounded rationality: variational (approximate) rather than exact Bayesian inference.
- Finite policy horizon (two steps): forces hierarchical chunking into subgoals.
- Agents have prior beliefs about *policies* (not just states), so action selection is itself an inference problem.
- Precision γ plays the role of an inverse temperature / confidence parameter, updated analogously to dopamine reward-prediction-error signals.
- Parameter learning occurs via Dirichlet concentration updates (associative Hebbian-like plasticity on the likelihood matrix A).

---

### Prevailing model of the system under study

The paper situates itself against reinforcement learning (RL) formulations of navigation, including model-free habit caching (Sutton & Barto 1998), model-based tree search, pruning/plan-until-habit hybrids, bidirectional planning, hierarchical options frameworks, and successor representations (Dayan 1993; Stachenfeld et al. 2017). The prevailing view is that exploration and exploitation require separate mechanisms (or explicit trade-off parameters such as ε-greedy or softmax temperature) and that planning in deep trees is computationally intractable without approximations. Spatially, the hippocampus is assumed to provide a cognitive map via place cells — discrete neurons firing at specific locations — with entorhinal grid cells providing metric structure. The paper's introduction frames active inference as a candidate unified framework that subsumes these separate mechanisms.

---

### What this paper contributes

The paper demonstrates that a single objective function — expected free energy — can generate both exploratory and goal-directed behaviour without explicit trade-off mechanisms, resolving the exploration–exploitation dilemma normatively. Concretely:

- It establishes that novelty (epistemic value from parameter uncertainty) and salience (epistemic value from state uncertainty) are formally separable components of expected free energy, each driving qualitatively distinct exploratory behaviours.
- It introduces the graph-Laplacian subgoal heuristic as a specific, tractable formulation of prior preferences that enables finite-horizon agents to pursue distal goals by chunking into attainable subgoals.
- It proposes "path cells" as a more general class of spatial representation than place cells, predicting a continuous spectrum from trajectory-encoding to location-encoding neurons, with place cells as the limiting case — a novel empirical prediction.
- It generates specific, falsifiable predictions about dopaminergic responses (peak phasic activity at intermediate, not maximal, familiarity) and about theta–gamma coupling as an emergent property of the update dynamics.
- It unifies perception, planning, learning, and action selection under a single set of belief-propagation equations, providing a neurobiologically constrained process theory.

---

### Brain regions & systems

- **Hippocampal formation / parietal association cortex** — proposed locus of hidden-state (location) representations; linked to place and path cell predictions; increased coupling with rostro-dorsal medial prefrontal cortex during subgoal identification.
- **Caudate nucleus** — proposed site of policy evaluation (expected free energy G computation).
- **Putamen** — proposed site of posterior policy expectations; constructs Bayesian model averages of future outcomes.
- **Ventral tegmental area / substantia nigra (VTA/SN)** — proposed site of precision updates, identified with dopaminergic reward-prediction-error signals.
- **Superior colliculus (deep layers)** — proposed site of action specification (saccade execution); superficial layers linked to proprioceptive/where outcome modality via lateral geniculate nucleus.
- **Pontine–geniculate occipital system** — proposed representation of observed outcomes.
- **Dorsomedial entorhinal cortex** — grid cells discussed as providing metric spatial scaffolding; not directly modelled but contextualised as complementary.
- **Rostro-dorsal medial prefrontal cortex (rd-mPFC) / lateral frontopolar cortex** — cited from authors' own fMRI work (Kaplan et al. 2017a/b) as anterior prefrontal regions engaged by demanding subgoal choices in deep maze planning.

---

### Mechanistic insight

The paper meets the first criterion (it formalises an algorithm — active inference belief propagation) but does not provide neural data linking the model's specific variables to measured neural activity. The paper is a pure computational/simulation study; electrophysiological and fMRI responses are *simulated*, not empirical. The model generates predictions about theta–gamma coupling, dopamine phasic responses, and path vs. place cell activity profiles, but these remain untested in the paper itself (validation against empirical fMRI is deferred to future work, Kaplan et al. 2017a).

Therefore the bar for Mechanistic insight is not met. The paper proposes an active inference algorithm and provides simulated neural proxies, but does not supply empirical neural data that selectively support this algorithm over alternatives.

---

### Limitations & open questions

- The generative model assumes agents have perfect positional feedback (veridical *where* outcomes), which limits ecological validity.
- Policies are restricted to depth-two sequences; how the framework scales to longer horizons or continuous state spaces is not addressed.
- The graph-Laplacian subgoal heuristic is one of many plausible priors; the paper acknowledges it has not adjudicated among alternatives.
- All neurophysiological predictions (theta–gamma coupling, dopamine response profiles, path vs. place cell distinction) remain simulation-only; empirical validation is explicitly deferred.
- The model does not address how the maze is initially discretised or how continuous sensorimotor signals are mapped to the discrete state space.
- The paper does not model error correction when learned maze structure is wrong or when the environment changes.
- The relationship between path-cell/place-cell predictions and existing electrophysiology (e.g. theta sequences, sharp-wave replay) is discussed speculatively but not formalised.
- Dopamine prediction: largest phasic dopaminergic responses at intermediate familiarity is a novel and potentially falsifiable claim that has not, to the authors' knowledge, been empirically tested.

---

### Connections & keywords

**Key citations**:
- Friston et al. (2015) — active inference and epistemic value (core framework)
- Friston et al. (2017a) — active inference as a process theory
- Sutton & Barto (1998) — reinforcement learning baseline
- Daw et al. (2005, 2011) — model-based/model-free RL and habitual/goal-directed distinction
- Stachenfeld et al. (2017) — hippocampus as predictive map (successor representation)
- Gershman & Daw (2017) — RL with episodic memory
- Kaplan et al. (2017a) — companion fMRI study of spatial planning
- Pfeiffer & Foster (2013) — hippocampal place cell sequences depicting future paths
- Buzsaki & Moser (2013) — theta rhythm and hippocampal–entorhinal system

**Named models or frameworks**:
- Active inference (free energy principle)
- Markov decision process (MDP) / partially observed MDP (POMDP)
- Expected free energy decomposition (epistemic + extrinsic value)
- Graph-Laplacian diffusion subgoal heuristic
- Successor representation (Dayan 1993)
- Options framework (hierarchical RL)
- Plan-until-habit (Keramati et al. 2016)
- SPM MDP toolbox (spm_MDP_VB_X.m)

**Brain regions**:
- Hippocampal formation
- Entorhinal cortex (grid cells)
- Caudate nucleus
- Putamen
- Ventral tegmental area / substantia nigra
- Superior colliculus
- Rostro-dorsal medial prefrontal cortex
- Lateral frontopolar cortex

**Keywords**:
- active inference
- free energy minimisation
- epistemic value
- novelty and salience
- spatial navigation
- planning under uncertainty
- subgoal decomposition
- exploration–exploitation
- place cells vs. path cells
- theta–gamma coupling
- dopamine precision updating
- Markov decision process
