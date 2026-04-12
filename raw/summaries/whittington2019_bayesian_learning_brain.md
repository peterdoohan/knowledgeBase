---
source_file: "whittington2019_bayesian_learning_brain.md"
paper_id: "whittington2019_bayesian_learning_brain"
title: "A Bayesian account of learning and generalising representations in the brain"
authors: "James C.R. Whittington"
year: 2019
journal: "DPhil Thesis, University of Oxford"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["navigation_task"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex", "prefrontal_cortex", "striatum", "thalamus"]
frameworks: ["bayesian_inference", "attractor_networks", "tolman_eichenbaum_machine"]
keywords: ["predictive_coding", "backpropagation", "biological_credit_assignment", "tolman_eichenbaum_machine", "grid_cells", "place_cells", "cognitive_maps", "relational_memory", "structural_generalization", "zero_shot_inference", "factorized_representations", "path_integration", "attractor_networks", "entorhinal_cortex", "hippocampus", "transitive_inference", "social_hierarchy", "bayesian_inference", "hebbian_plasticity", "neural_representation_learning"]
key_citations: ["behrens2018_cognitive_map_organizing_knowledge", "tolman1948_cognitive_maps_rats", "stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

This thesis demonstrates that predictive coding networks can implement backpropagation for learning, and proposes the Tolman-Eichenbaum Machine (TEM), a unified computational framework for relational learning that explains both spatial navigation and abstract relational memory through factorized representations.

### Background & motivation

Two fundamental questions in neuroscience remain unresolved: (1) how do biological neural networks learn given that backpropagation appears biologically implausible, and (2) what computational principles allow the brain to generalize knowledge across different situations? The hippocampus exhibits both spatial representations (cognitive maps) and relational memory, yet these phenomena have been treated separately. This thesis aims to unify these under a common Bayesian framework.

### Methods

- **Predictive coding networks for learning**: Developed a mathematically exact equivalence between backpropagation in artificial neural networks and predictive coding in biological networks
- **Tolman-Eichenbaum Machine (TEM)**: A generative model that factorizes representations into structural variables (entorhinal-like, "g") and sensory variables (hippocampal-like, "p")
- **Model training**: Trained TEM on multiple tasks including transitive inference, social hierarchies, 2D spatial navigation, and complex sequential tasks
- **Neural predictions**: Compared model representations to published electrophysiological data from rodent hippocampus and entorhinal cortex

### Key findings

- Predictive coding networks implementing local Hebbian learning rules can perform exact backpropagation, achieving identical performance to artificial neural networks on machine learning benchmarks
- TEM learns grid-like cells in entorhinal cortex representations that generalize across environments, preserving correlation structure (grid cells in different environments maintain same relative firing relationships)
- TEM learns place-like cells in hippocampal representations that remap between environments (global remapping), showing conjunctive coding of structure and sensory identity
- TEM exhibits zero-shot inference on novel tasks after learning structural regularities, including transitive inference and social hierarchy reasoning
- TEM reproduces diverse entorhinal cell types (grid cells, band cells, border cells, object vector cells) depending on behavioral transition statistics
- Model predictions confirmed in neural data: TEM's predicted entorhinal-hippocampal relationships match empirical correlations from Barry et al. (2012) and Chen et al. (2018)

### Computational framework

**Bayesian predictive coding and the Tolman-Eichenbaum Machine**

The framework combines two key ideas:

1. **Predictive coding for learning**: Networks minimize prediction error through local computation. The key insight is that prediction error nodes in predictive coding networks have activities mathematically equivalent to error terms in backpropagation, allowing weight updates via simple Hebbian learning rather than global credit assignment.

2. **Factorized representations for generalization**: TEM separates knowledge into:
   - **Structural representations (g)**: Encode transition statistics and relational structure, generalize across environments
   - **Sensory representations (x)**: Encode specific sensory observations
   - **Conjunctive memories (p)**: Bind structure and sensory experience via outer product, enabling specific episodic memories

The model uses a generative architecture (predicting next states from current) and an inference architecture (inferring latent states from sensory observations), trained with wake-sleep-like algorithm. An attractor memory module allows rapid retrieval of previous experiences for path integration correction.

### Prevailing model of the system under study

**Before this work, the field held several disconnected views:**

1. **Learning algorithms**: Backpropagation was considered biologically implausible due to requirements for weight symmetry, precise error feedback, and non-local credit assignment. Alternative models (e.g., XCAL, O'Reilly's models) sacrificed efficiency for biological plausibility.

2. **Hippocampal function**: Two separate literatures existed:
   - **Spatial navigation**: Hippocampal place cells and entorhinal grid cells formed a cognitive map for spatial navigation (O'Keefe & Nadel, Moser et al.)
   - **Relational memory**: Hippocampus supported memory for arbitrary relations between items (Eichenbaum & Cohen), but the relationship to spatial representations was unclear

3. **Generalization**: Was typically explained as pattern completion in attractor networks or gradual transfer in multi-task learning, without formal computational framework for structural generalization.

**The tension**: How could the same hippocampal system support both spatial maps and relational memory? And how could biological networks learn with anything approaching the efficiency of backpropagation?

### What this paper contributes

**This thesis makes several transformative contributions:**

1. **Biologically plausible backpropagation**: Shows that predictive coding networks with local Hebbian learning can implement backpropagation exactly. This overturns decades of assumptions about biological implausibility. The key insight is that prediction error nodes in predictive coding encode the same information as backpropagation error terms, allowing weight updates without global credit assignment.

2. **Unified framework for hippocampal function**: The Tolman-Eichenbaum Machine unifies spatial cognition and relational memory under a common computational framework. Both phenomena emerge from factorizing representations into structural (generalizable) and sensory (specific) components, bound together in hippocampal conjunctive memories. This explains why hippocampus shows both spatial and non-spatial responses.

3. **Explanation of diverse cell types**: TEM provides a unified account of diverse entorhinal cell types (grid cells, band cells, border cells, object vector cells) as basis functions for transition statistics. Different cell types emerge from different behavioral patterns, not from hardwired circuitry. This suggests entorhinal "zoo" of cell types reflects learned statistical structure.

4. **Structural generalization and zero-shot inference**: Formalizes how knowledge learned in one environment can generalize to novel environments through learned structural representations. TEM demonstrates zero-shot inference on transitive inference and social hierarchy tasks—capacities previously thought to require explicit symbolic reasoning or extensive multi-task training.

5. **Testable neural predictions**: Generates specific predictions about neural representations that were confirmed in existing data (e.g., correlation structure between grid cells across environments, relationship between entorhinal and hippocampal representations). Also makes novel predictions (e.g., entorhinal cells should show lap-specific modulation in Sun et al. task) awaiting experimental test.

6. ** Marr's levels integration**: The work integrates across Marr's levels—from computational theory (Bayesian inference over relational structure) through algorithm (predictive coding with factorized representations) to implementation (specific cell types, connectivity, learning rules). This provides a rare example of complete computational-to-biological mapping.

### Brain regions & systems

- **Hippocampus (CA1, CA3)**: Site of conjunctive memory representations ("p" cells in TEM); place cells that remap between environments; landmark cells for object-specific representations; stores episodic memories binding structural and sensory information
- **Medial entorhinal cortex (MEC)**: Site of structural representations ("g" cells in TEM); grid cells representing 2D spatial topology; band cells; border cells; object vector cells; all representing transition statistics that generalize across environments
- **Prefrontal cortex**: Implied role in goal-directed behavior using structured representations; not explicitly modeled but discussed in context of cognitive control
- **Basal ganglia/thalamus**: Briefly mentioned in context of motor control and action selection; not primary focus

### Mechanistic insight

**This paper meets the high bar for mechanistic insight.**

The thesis provides a complete mapping from computational problem to neural implementation:

**Computational level**: The brain must solve two fundamental problems—learning from error signals (credit assignment) and representing knowledge in ways that support generalization to novel situations. The computational solution is Bayesian inference over latent structural variables that capture environmental statistics.

**Algorithmic level**: 
- For learning: Predictive coding networks implement approximate Bayesian inference using local message passing. Prediction errors (difference between observed and predicted activity) are propagated through the network. The key insight is that these prediction error nodes encode mathematically equivalent information to backpropagation error terms, allowing weight updates via Hebbian plasticity (product of pre- and post-synaptic activity) rather than global credit assignment.
- For representation: The Tolman-Eichenbaum Machine factorizes knowledge into structural variables (g) encoding transition statistics and sensory variables (x). An attractor memory module allows rapid retrieval of previous experiences for path integration correction. The outer product of structural and sensory representations creates conjunctive memory representations (p) that bind specific experiences to structural locations.

**Implementational level**:
- **Cell types**: Grid cells emerge from path integration requirements (maximally different representations at different locations, invariant to approach trajectory). Place cells emerge from conjunctive coding of structure and sensory identity. Border cells and object vector cells emerge from non-diffusive behavioral transition statistics.
- **Connectivity**: Predictive coding requires both feedforward (prediction) and feedback (prediction error) connections. The attractor memory requires recurrent connectivity for pattern completion.
- **Learning rules**: Weight updates follow Hebbian principles (product of pre- and post-synaptic activity). The equivalence to backpropagation arises because prediction error nodes in predictive coding encode the same quantity as error terms in backpropagation.
- **Dynamics**: Inference involves iterative convergence to steady-state (minimizing prediction error). Learning involves weight updates after convergence.

The thesis thus provides a complete mechanistic account spanning from the computational problem (how to learn and generalize) through the algorithm (predictive coding with factorized representations) to the implementation (specific cell types, connectivity patterns, and learning rules).

### Limitations & open questions

- **Biological implementation details**: While the predictive coding framework provides a proof of principle that backpropagation-equivalent learning can be implemented locally, specific biophysical mechanisms (e.g., how prediction errors are computed precisely, role of different interneuron types) remain to be determined.
- **Scalability to complex behaviors**: TEM was tested on relatively simple graph-structured tasks. How well the framework scales to the full complexity of real-world behavior (continuous time, high-dimensional sensory inputs, hierarchical action spaces) remains an open question.
- **Developmental emergence**: The models assume mature networks with learned representations. How the factorized representations develop during learning, and whether developmental trajectories match model predictions, is not addressed.
- **Alternative frameworks**: While predictive coding provides one solution to biological backpropagation, whether the brain actually uses this specific algorithm or alternative biologically plausible credit assignment mechanisms (e.g., target propagation, feedback alignment) remains an empirical question.
- **Causal manipulations**: The model makes specific predictions about neural representations (e.g., lap-specific entorhinal cells in Sun et al. task), but these predictions have not yet been tested with causal manipulations (e.g., optogenetic silencing of entorhinal cortex should eliminate lap-specific hippocampal responses).
- **Relationship to sleep and consolidation**: The model includes generative replay mechanisms, but the relationship to actual sleep replay, systems consolidation, and memory replay during wake remains to be fully explored.

### Connections & keywords

- **Key citations**: Whittington & Bogacz (2017, 2019), Behrens et al. (2018), Tolman (1948), Eichenbaum & Cohen (2014), O'Keefe & Nadel (1978), Rao & Ballard (1999), Friston (2003, 2005), Hafting et al. (2005), Sun et al. (2019), Stachenfeld et al. (2017), Kumaran et al. (2012), Bunsey & Eichenbaum (1996)
- **Named models or frameworks**: Predictive coding, Tolman-Eichenbaum Machine (TEM), Backpropagation, Hebbian learning, Wake-Sleep algorithm, Helmholtz Machine, Bayesian inference, Attractor networks, Path integration, Cognitive map theory
- **Brain regions**: Hippocampus (CA1, CA3), Medial entorhinal cortex (MEC), Prefrontal cortex, Basal ganglia
- **Keywords**: predictive coding, backpropagation, biological credit assignment, Tolman-Eichenbaum Machine, grid cells, place cells, cognitive maps, relational memory, structural generalization, zero-shot inference, factorized representations, path integration, attractor networks, entorhinal cortex, hippocampus, transitive inference, social hierarchy, Bayesian inference, Hebbian plasticity, neural representation learning

STATUS: success | input=whittington2019_bayesian_learning_brain.md | output=whittington2019_bayesian_learning_brain.md | renamed=no