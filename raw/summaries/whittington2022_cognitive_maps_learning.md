---
source_file: whittington2022_cognitive_maps_learning.md
title: How to build a cognitive map
authors: James C. R. Whittington, David McCaffary, Jacob J. W. Bakermans, Timothy E. J. Behrens
year: 2022
journal: Nature Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

This review organizes computational models of hippocampal-entorhinal cognitive maps into a unified ontology, revealing that understanding cognitive maps requires modeling sequences and the statistical structure of sequences, with implications extending from spatial navigation to abstract reasoning.

### Background & motivation

Cognitive maps enable flexible behavior by organizing knowledge for generalization, allowing rapid inference from sparse observations. While the hippocampal formation has been implicated in spatial cognition through place cells and entorhinal grid cells, recent evidence suggests these same representations code abstract nonspatial dimensions (sound frequencies, social hierarchies, reward spaces). The challenge is understanding how diverse models of hippocampal function relate to each other and what each contributes to building cognitive maps that generalize across domains.

### Methods

This is a review paper that synthesizes multiple computational modeling approaches:

- **Review scope**: Computational models of hippocampal-entorhinal cognitive maps, including successor representation (SR), clone-structured cognitive graphs (CSCG), continuous attractor neural networks (CANNs), the Tolman-Eichenbaum Machine (TEM), and the Spatial Memory Pipeline (SMP)
- **Organizational framework**: Models are organized by their treatment of state-space construction (latent state learning vs. path integration), generalization mechanisms, and the division of labor between hippocampus and cortex
- **Integration approach**: The ontology reveals how models can be combined (e.g., TEM + CSCG) and generates new predictions about neural representations and behavior

### Key findings

- **Unified computational principle**: Building cognitive maps reduces to learning sequences and the statistical structure of sequences. Models that learn from sensory predictions (rather than rewards) create useful state representations for future reinforcement learning.

- **Two complementary hippocampal roles**: 
  - "Hippocampus-as-map" models (SR, CSCG) rapidly learn environment-specific maps but do not generalize
  - "Hippocampus-as-memory" models (TEM, SMP) slowly learn generalizable cortical maps that can be immediately transferred to new environments

- **Latent state representations unify diverse neural phenomena**: "Splitter cells," "inbound/outbound cells," "lap cells," and abstract position/evidence cells in nonspatial tasks can all be understood as latent state representations that disambiguate sensorially identical situations with different futures.

- **Path integration enables generalization**: Grid cells emerge from path integration and provide a compressed, generalizable representation of space that extends to all locations and supports vector-based navigation.

- **Compositional representations enable credit assignment through generalization**: Goal-vector cells (GVCs), object-vector cells (OVCs), and boundary-vector cells (BVCs) serve as reusable basis functions that can be composed to represent novel task configurations without relearning value functions.

- **Representational drift as temporal remapping**: The slow drift of hippocampal representations over time can be understood as remapping driven by changing temporal representations in entorhinal cortex, rather than spatial or sensory changes.

- **Predictions for hierarchical tasks**: The framework predicts contextually modulated vector cells in prefrontal-hippocampal interactions, where abstract task representations in PFC contextualize spatial representations in the hippocampal formation.

### Computational framework

The review synthesizes models within the **reinforcement learning (RL) framework**, particularly emphasizing state-space construction rather than reward learning. Key formalisms include:

- **Successor Representation (SR)**: A predictive map representing the expected future occupancy of states. Mathematically, **S** = Σ_n γ^n **T**^n, where **T** is the transition matrix. The SR provides a geometric representation where value computation simplifies to **v** = **Sr**.

- **Graph representations**: States as nodes, transitions as edges. Planning becomes matrix multiplication (**T**^n**v** gives n-step future distributions). Shortest path problems can be solved by repeated multiplication until the goal state becomes active.

- **Path integration in Continuous Attractor Neural Networks (CANNs)**: Neural dynamics τ d**g**/dt = −**g** + f(**Wg** + **Ba**), where **g** is neural activity, **W** is recurrent weights, **B** projects velocity inputs **a**. With appropriate weights, these networks implement path integration, supporting grid cells, place cells, and head direction cells.

- **Clone-Structured Cognitive Graphs (CSCG)**: A hidden Markov model where each sensory observation maps to multiple "clone" latent states. The model learns transition probabilities between clones using EM algorithm, enabling latent state inference from sequences.

- **Tolman-Eichenbaum Machine (TEM)**: Combines a path-integrating cortical module (abstract representation) with a hippocampal memory module that links abstract locations to sensory observations via Hebbian learning. Enables generalization across structurally similar environments.

### Prevailing model of the system under study

Before this review's synthesis, the field had developed several competing models of hippocampal-entorhinal function without a clear organizing framework:

- **Hippocampus as cognitive map** (O'Keefe & Nadel): The hippocampus builds allocentric spatial maps through place cells, enabling flexible navigation
- **Hippocampus as relational memory** (Eichenbaum): The hippocampus binds episodic experiences via memory, not spatial maps
- **Successor representation** (Stachenfeld et al.): The hippocampus constructs predictive maps for model-based RL
- **Path integration models** (CANNs, VCOs): Grid cells and place cells emerge from continuous attractor dynamics and velocity integration
- **Latent state models** (CSCG): The hippocampus infers hidden states from sequences to resolve sensory aliasing

These models were often treated as competing alternatives rather than complementary components. The relationships between spatial and nonspatial representations, between hippocampal and entorhinal contributions, and between learning fast maps versus generalizable abstractions remained unclear.

### What this paper contributes

This review provides a unifying ontology that reveals how diverse models of hippocampal-entorhinal function are complementary rather than competing:

- **Ontology of cognitive map models**: The review organizes models along key dimensions: (1) how state-spaces are constructed (latent state learning vs. path integration), (2) how representations generalize (compositional vs. monolithic), and (3) the division of labor between hippocampus and cortex (map vs. memory). This reveals that models like SR/CSCG (hippocampus-as-map) and TEM/SMP (hippocampus-as-memory) serve complementary functions with different learning speeds and generalization properties.

- **Unified computational principle**: The review establishes that building cognitive maps reduces to learning sequences and their statistical structure. This principle unifies spatial navigation with nonspatial cognition and connects diverse neural phenomena (place cells, grid cells, splitter cells, time cells) as manifestations of latent state representations for predicting future observations.

- **Integration of model classes**: The review shows how model classes can be integrated (e.g., CSCG + TEM for a hippocampus that builds both maps and memories; learned latent state-spaces as input to SR for planning). This generates new predictions about hippocampal-cortical interactions and the role of replay in offline state-space construction.

- **New predictions and reinterpretations**: The framework generates specific predictions: (1) contextually modulated vector cells in prefrontal-hippocampal interactions, (2) representational drift as temporal remapping (changing time representations in MEC causing hippocampal drift), (3) factorized vs. warped representations depending on task demands, (4) the role of replay in composing pre-learned basis representations for credit assignment.

- **Extension to higher cognition**: The review proposes that principles from sequence learning (state representation, factorization, path integration) may extend to understanding neural representations in language, mathematics, and logical reasoning, suggesting cognitive maps as envisaged by Tolman provide a foundation for reasoning across all cognitive domains.

### Brain regions & systems

- **Hippocampus (HPC)**: Proposed to serve dual roles—(1) rapidly learning environment-specific relational maps (in novel situations), and (2) binding abstract cortical representations to sensory experiences via memory (in familiar situations). Contains place cells, splitter cells, lap cells, and conjunctive representations that combine spatial and nonspatial information.

- **Medial entorhinal cortex (MEC)**: Contains grid cells that provide generalizable, path-integrating representations of space. Proposed to construct abstract structural representations that generalize across environments. Grid cells enable vector-based navigation and compression of spatial information.

- **Lateral entorhinal cortex (LEC)**: Provides sensory representations that are linked to abstract MEC representations via hippocampal memory. Contains object-related representations.

- **Prefrontal cortex (PFC) / Orbitofrontal cortex (OFC)**: Proposed to represent abstract task structure and "location in task" that contextualizes hippocampal representations. May contain factorized representations of task rules that combine with spatial representations via hippocampal memory (Fig. 4e,f).

- **Subcortical structures**: Head direction cells in postsubiculum and other regions provide velocity signals for path integration.

### Mechanistic insight

This review paper does not present new empirical data linking specific algorithms to neural mechanisms. However, it synthesizes models where such links have been established:

**Marr's levels analysis of integrated models:**

- **Computational**: The brain solves the problem of building predictive cognitive maps that enable flexible behavior and generalization across structurally similar environments. The goal is to minimize online computation by learning appropriate state abstractions from sequences of experience.

- **Algorithmic**: Multiple algorithmic approaches are reviewed:
  - **Successor representation (SR)**: Predictive map as discounted sum of future state occupancies
  - **Clone-structured cognitive graphs (CSCG)**: Hidden Markov models that infer latent states from sequences
  - **Path integration in CANNs**: Recurrent networks that update position estimates from velocity inputs
  - **TEM/SMP**: Compositional models combining path integration with memory-based binding of abstract and sensory representations

- **Implementational**: The review connects algorithms to specific neural circuits:
  - Grid cells in MEC implement path integration via continuous attractor dynamics
  - Place cells in hippocampus represent unique locations or conjunctive states
  - Hippocampal memory circuits (Hebbian learning, Hopfield networks) bind MEC and LEC representations
  - Prefrontal cortex may represent abstract task structures that contextualize hippocampal activity

**Limitation**: As a review without new empirical data, this paper does not itself provide novel mechanistic links between algorithms and neural implementations. Instead, it synthesizes and organizes existing mechanistic insights from the models it reviews.

### Limitations & open questions

- **Role of time in cognitive maps**: How representational drift in hippocampal cells over days relates to temporal coding in entorhinal cortex remains unclear. The hypothesis that drift reflects temporal remapping (changing time representations while spatial/sensory remain constant) requires empirical testing.

- **Hierarchical abstraction mechanisms**: While the review proposes that prefrontal cortex may represent abstract task structure ("location in task") that contextualizes hippocampal representations, the specific mechanisms by which these hierarchical interactions occur remain to be elucidated.

- **Generalization to higher cognition**: Whether principles of sequence learning, path integration, and factorization extend to language, mathematics, and logical reasoning is speculative. Empirical evidence linking these cognitive domains to hippocampal-entorhinal mechanisms is limited.

- **Neural implementation of composition**: How the brain arbitrates between factorized (generalizable) and warped (task-specific) representations depending on task demands is not fully understood. The mechanisms by which cortical-striatal interactions construct and update RL state-spaces require further investigation.

- **Replay function**: While the review proposes replay constructs state-spaces by composing pre-learned basis representations, direct empirical evidence for this specific computational role of replay is still emerging.

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) - The Hippocampus as a Cognitive Map
- Tolman (1948) - Cognitive maps in rats and men
- Stachenfeld, Botvinick & Gershman (2017) - The hippocampus as a predictive map (successor representation)
- Whittington et al. (2020) - The Tolman-Eichenbaum Machine
- George et al. (2021) - Clone-structured cognitive graphs
- Burak & Fiete (2009) - Grid cells via path integration in CANNs

**Named models or frameworks:**
- Successor Representation (SR)
- Clone-Structured Cognitive Graph (CSCG)
- Tolman-Eichenbaum Machine (TEM)
- Spatial Memory Pipeline (SMP)
- Continuous Attractor Neural Networks (CANNs)
- Default Representation (DR)
- Reinforcement Learning (RL) state-space framework
- Path integration models (velocity-coupled oscillators, VCOs)

**Brain regions:**
- Hippocampus (HPC) - place cells, splitter cells, conjunctive representations, relational memory
- Medial entorhinal cortex (MEC) - grid cells, path integration, abstract structural representations
- Lateral entorhinal cortex (LEC) - sensory representations, object-related coding
- Prefrontal cortex (PFC) / orbitofrontal cortex (OFC) - abstract task structure, location in task
- Subiculum - boundary vector cells
- Postsubiculum - head direction cells

**Keywords:**
cognitive map, successor representation, grid cells, place cells, latent state inference, path integration, reinforcement learning, generalization, hippocampal-entorhinal system, sequence learning, continuous attractor networks, Tolman-Eichenbaum Machine, compositional representations, representational drift, state-space abstraction
