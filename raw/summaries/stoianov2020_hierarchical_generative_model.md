---
source_file: "stoianov2020_hierarchical_generative_model.md"
paper_id: "stoianov2020_hierarchical_generative_model"
title: "The hippocampal formation as a hierarchical generative model supporting generative replay and continual learning"
authors: "Ivilin Stoianov, Domenico Maisto, Giovanni Pezzulo"
year: 2020
journal: "bioRxiv (preprint)"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["navigation_task"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "striatum", "ventral_striatum"]
keywords: ["hippocampal", "formation", "hierarchical", "generative", "model", "supporting", "replay", "continual", "learning"]
key_citations: ["stella2019_hippocampal_reactivation_brownian", "liu2019_human_replay_reorganizes"]
---

### One-line summary

The hippocampal formation functions as a hierarchical generative model that organizes sequential experiences into spatiotemporal contexts, with internally generated sequences arising from generative replay (resampling fictive experiences from the learned model) rather than verbatim replay from a memory buffer.

### Background & motivation

A fundamental problem in both neuroscience and machine learning is preventing novel knowledge from interfering with past memories (catastrophic forgetting). The hippocampus has been proposed to solve this through replay of experiences during offline periods. However, empirical findings challenge the view that hippocampal sequences simply replay old memories: they can depict future goals, novel paths never experienced, and follow Brownian diffusion-like statistics different from navigation. This paper proposes a theoretical framework unifying these findings.

### Methods

- **Model architecture**: Three-layer hierarchical generative model with:
  - Layer 1 (items): latent codes for individual observations (e.g., spatial locations), putatively corresponding to place cells
  - Layer 2 (sequences): latent codes organizing items into temporal sequences
  - Layer 3 (maps): latent codes clustering sequences into mutually exclusive spatial contexts (cognitive maps)

- **Inference**: Approximate Bayesian inference using predictive coding-like mechanisms; items inferred from observations, sequences from items, and maps from sequences

- **Learning**: Dirichlet-categorical mixture model with hyperparameter updates based on visitation counts; Chinese Restaurant Process extension for nonparametric model

- **Replay mechanisms compared**:
  - Baseline: no replay
  - Experience replay: verbatim replay from unbounded memory buffer (biologically infeasible upper bound)
  - Generative replay: resampling fictive trajectories from currently inferred map
  - Prioritized generative replay: same but sampling from maps weighted by surprise rather than visitation

- **Task**: Continual learning of five 15x15 spatial mazes presented sequentially in blocks; 20 trajectories per maze

### Key findings

- **Generative replay enables effective continual learning**: Generative replay and prioritized generative replay agents significantly outperformed the baseline agent (t=3.47, p=0.002 and t=4.18, p<0.001) and showed no difference from the ideal experience replay agent with perfect memory

- **Nonparametric setting shows generative replay advantages**: In the more challenging nonparametric setting (unknown number of clusters), generative replay agents outperformed both baseline and experience replay agents during learning and retention (p<0.001)

- **Hierarchical structure is essential**: Reduced models lacking the sequence layer or capable of only single-cluster learning showed significantly degraded performance (all p<0.001) and generated more impossible trajectories violating maze constraints

- **Generative replay produces novel trajectories**: On average, replayed trajectories differed by 35% from the most similar experienced trajectories and included 8.6 novel locations never visited during navigation; only a minority were physically impossible (traversing walls)

- **Replays follow Brownian diffusion statistics**: Log-log regression showed replay trajectories followed power-law diffusion (alpha=0.46, s.d.=0.031) consistent with empirical findings (Stella et al., 2019), while navigation showed directed motion (alpha=0.75)

- **Pre-run dynamics predict post-run replay**: Rank-order correlation analysis showed pre-run (preplay) and post-run (replay) activity were more strongly correlated (r=0.66) than post-run and run activity (r=0.36, t=17.05, p<0.001), matching empirical findings (Liu et al., 2019)

- **Run-post-run correlations decrease over learning**: A novel prediction of the model - run-post-run correlations decreased linearly across blocks (beta=-0.05, t=-3.9, p<0.001) while pre-run-post-run correlations remained stable (beta=0.02, n.s.)

- **Goal sensitivity in replay**: During sleep-like replay (no external input), generative replay tended to start from and visit behaviorally relevant locations (goals, junctions), consistent with empirical findings that replay during sleep starts from rewarded locations

- **Flickering between maps**: Simulations showed flickering (rapid switching between map representations) during maze transitions, consistent with theta-paced flickering observed empirically (Jezek et al., 2011)

### Computational framework

**Hierarchical generative model with generative replay for continual learning**

The paper advances a hierarchical generative model framework based on three core principles:

1. **Hierarchical latent structure**: The model organizes experiences at three levels - items (individual observations), sequences (temporal organization), and maps (spatial/relational context). This hierarchy provides inductive biases: items are organized into sequences (temporal continuity), and sequences into maps (spatial clustering).

2. **Mixture model for context separation**: Maps are represented as clusters in a mixture model with mutually exclusive selection. Only the currently inferred map is updated during learning, preventing interference between experiences in different contexts. This is key to avoiding catastrophic forgetting.

3. **Generative replay**: Rather than storing verbatim memories, the model resamples fictive experiences from its learned generative model to self-train. This uses bounded resources (the model parameters) rather than unbounded memory storage.

**Mathematical formalism**:
- Observations: one-hot vectors over spatial locations
- Items: inferred via predictive coding integrating bottom-up observations, top-down map predictions, lateral sequence information, and movement dynamics
- Sequences: graded representations (exponential decay) encoding temporal order
- Maps: Dirichlet-categorical distributions over location occupancy; hyperparameters updated via visitation counts
- Inference: MAP estimation with Bayesian filtering for map selection
- Learning: Hyperparameter updates after each observation; selective updating of only the currently inferred map

### Prevailing model of the system under study

The paper positions itself against two prevailing views in the literature:

1. **Complementary Learning Systems (CLS) theory**: The hippocampus as an episodic memory buffer that stores novel experiences rapidly and reactivates them offline to train a separate cortical semantic memory system. While the paper retains the idea of offline replay supporting learning, it challenges the assumption that the hippocampus simply stores and replays verbatim memories.

2. **Auto-associative memory networks**: The view of hippocampal CA3 as storing static memory patterns or sequences that can be spontaneously replayed. The paper argues these approaches require unbounded memory resources and cannot explain the flexible, prospective aspects of hippocampal sequences.

The paper also engages with empirical findings that challenge simple replay theories: that hippocampal sequences can depict future paths, random Brownian trajectories, shortcuts, and preplay of future experiences. These findings suggest a more generative, constructive process rather than verbatim memory replay.

### What this paper contributes

This paper advances a novel theoretical framework that:

1. **Recharacterizes hippocampal replay as generative replay**: Internally generated hippocampal sequences are proposed to arise from resampling fictive experiences from a learned hierarchical generative model, rather than from verbatim replay of stored memories. This explains why replay can generate novel, never-experienced sequences.

2. **Proposes a hierarchical generative model of the hippocampal formation**: The model organizes experiences at three levels - items (place cells), sequences (temporal trajectories), and maps (spatial contexts). This hierarchy provides inductive biases for organizing experiences into coherent spatiotemporal contexts.

3. **Explains flexible and prospective aspects of hippocampal sequences**: The model accounts for empirical findings that are difficult for replay theories: Brownian diffusion-like replay statistics, preplay of future experiences, goal sensitivity, and the correlation between pre-run and post-run dynamics.

4. **Provides a biologically plausible mechanism for continual learning**: Generative replay uses bounded resources (model parameters) rather than unbounded memory storage, yet achieves comparable or better performance than idealized experience replay in continual learning tasks.

5. **Makes novel predictions**: The model predicts that run-post-run correlations should decrease over learning while pre-run-post-run correlations remain stable - a prediction not yet tested empirically.

### Brain regions & systems

- **Hippocampal formation (entire structure)**: Proposed locus of the hierarchical generative model, organizing sequential experiences into coherent spatiotemporal contexts

- **Hippocampus (CA3, CA1, dentate gyrus)**: Putative encoding of items (place cells) and sequences; CA3 recurrent circuits may support generation dynamics during replay; CA1 may mediate outputs to entorhinal cortex

- **Entorhinal cortex**: Proposed source of inputs to hippocampus (via dentate gyrus and CA1) and recipient of outputs (via CA1 and subiculum); may provide metric structure for spatial maps or encode transition models; medial entorhinal grid cells may modulate sequence continuity

- **Prefrontal cortex (mPFC)**: Facilitates hippocampal sequences during decision-making; coordinated replay across hippocampus-PFC supports memory-guided decisions

- **Ventral striatum**: Coordinated replay with hippocampus supports goal-directed spatial navigation

### Mechanistic insight

This paper provides a computational-level theory with suggestions for algorithmic and implementational mappings, though it does not provide direct neural data validating the specific algorithmic implementation.

**Computational level**: The hippocampal formation solves the problem of organizing sequential experiences into coherent spatiotemporal contexts to support continual learning without catastrophic forgetting. The computational goal is to learn a hierarchical generative model that can infer current context, predict future observations, and generate fictive experiences for self-training.

**Algorithmic level**: The hierarchical generative model uses three levels of representation:
- Items: inferred via predictive coding integrating observations, top-down predictions, lateral sequence information, and movement dynamics
- Sequences: graded representations with exponential decay encoding temporal order
- Maps: Dirichlet-categorical mixture components representing spatial contexts

Inference uses MAP estimation with Bayesian filtering for map selection. Learning updates hyperparameters via visitation counts, with selective updating of only the currently inferred map to prevent interference.

Generative replay samples fictive trajectories from the learned model by: (1) selecting a map based on current probabilities, (2) sampling a starting location from the map's occupancy distribution, (3) iteratively generating subsequent locations via the inference dynamics.

**Implementational level**: The paper speculates on neural implementations:
- Recurrent hippocampal-entorhinal loop may support both inference (encoding) and generation (decoding) functions
- Inference pathway: entorhinal cortex → dentate gyrus → CA3/CA1 (bottom-up)
- Generation pathway: CA3 → CA1 → entorhinal cortex (top-down)
- Theta rhythm may act as a gain modulator, switching between bottom-up (encoding) and top-down (prediction) phases

However, the paper does not provide direct neural data validating these specific implementational mappings. The model is validated against existing empirical findings (Brownian diffusion statistics, preplay-replay correlations, goal sensitivity) but these are correlational rather than causal evidence for the specific algorithmic mechanisms proposed.

### Limitations & open questions

- The model is simplified and does not fully include rich inputs (e.g., sensory and spatial codes) that the hippocampus receives from entorhinal cortex
- Theta sequences are not explicitly modelled but could potentially be incorporated by interleaving bottom-up recognition and top-down generation within theta cycles
- The model does not directly explain why some replay events show ballistic/superdiffusive rather than diffusive dynamics; modulation by grid cell activity may alter sequence continuity
- The paper does not provide direct empirical validation of the specific algorithmic mechanisms; validation is through correspondence with existing empirical patterns rather than new experiments
- The generalization to non-spatial domains (relational inference, episodic memory for arbitrary sequences) remains to be fully established
- Whether the three hierarchical levels localize to distinct anatomical structures or are distributed across the hippocampal formation remains to be empirically determined

### Connections & keywords

**Key citations**:
- McClelland et al. (1995) - Complementary Learning Systems theory
- Stella et al. (2019) - Brownian diffusion-like replay statistics
- Liu et al. (2019) - Preconfigured patterns driving replay
- Jezek et al. (2011) - Theta-paced flickering between maps
- Treves & Rolls (1992) - Auto-associative memory networks
- Buzsaki & Tingley (2018) - Hippocampus as sequence generator

**Named models or frameworks**:
- Hierarchical generative model
- Generative replay
- Prioritized generative replay
- Experience replay (comparison baseline)
- Complementary Learning Systems theory
- Predictive coding
- Chinese Restaurant Process (nonparametric extension)

**Brain regions**:
- Hippocampal formation
- Hippocampus (CA3, CA1, dentate gyrus)
- Entorhinal cortex
- Prefrontal cortex (mPFC)
- Ventral striatum

**Keywords**:
- hippocampus
- generative model
- generative replay
- cognitive map
- sequence generation
- continual learning
- catastrophic forgetting
- hierarchical Bayesian model
- mixture model
- spatial navigation
- place cells
- theta sequences
- preplay
- episodic memory
- prospective imagination