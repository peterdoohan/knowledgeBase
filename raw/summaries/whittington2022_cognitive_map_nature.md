---
source_file: whittington2022_cognitive_map_nature.md
paper_id: whittington2022_cognitive_map_nature
title: "How to build a cognitive map"
authors:
  - "James C. R. Whittington"
  - "David McCaffary"
  - "Jacob J. W. Bakermans"
  - "Timothy E. J. Behrens"
year: 2022
journal: "Nature Neuroscience"
paper_type: review
contribution_type: review
species:
  - human
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - lateral_entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - striatum
frameworks:
  - reinforcement_learning
  - successor_representation
  - bayesian_inference
  - attractor_networks
  - latent_state_inference
  - tolman_eichenbaum_machine
keywords:
  - cognitive_map
  - hippocampus
  - entorhinal_cortex
  - grid_cells
  - place_cells
  - successor_representation
  - reinforcement_learning
  - latent_states
  - path_integration
  - sequence_learning
  - generalization
  - abstraction
  - replay
  - state_space
  - computational_neuroscience
  - tolman_eichenbaum_machine
  - clone_structured_cognitive_graph
  - build
  - cognitive
  - map
key_citations:
  - tolman1948_cognitive_maps_rats
  - stachenfeld2017_hippocampus_predictive_map
  - whittington2020_tolman_eichenbaum_machine
  - burak2009_path_integration_grid_cells
wiki_pages:
  - wiki/topics/grid_cells_place_cells_and_path_integration_in_cognitive_maps
  - wiki/topics/reward_modulated_hippocampal_replay_in_spatial_reinforcement_learning
---

### One-line summary

This review organizes hippocampal-entorhinal models into a unified ontology revealing that cognitive maps are built by learning the statistical structure of sequences, integrating latent state inference with path integration to enable generalization across spatial and abstract domains.

---

### Background & motivation

Cognitive maps were proposed as internal neural representations enabling flexible behavior such as planning and generalization. While traditionally studied in spatial contexts (place cells, grid cells), recent evidence shows similar representations in nonspatial domains (sound frequency, value, social hierarchies). The field has developed many models to explain these cellular responses, but it has been difficult to understand how these models differ, relate, and what each contributes. This review aims to organize these models into a clear ontology that reveals common computational principles underlying both spatial and abstract cognitive maps.

---

### Methods

This is a review paper that synthesizes existing literature. The reviewed modeling approaches include:

- **Successor Representation (SR) models**: Graph-based RL models where the hippocampus constructs predictive maps by learning expected future occupancies from sequences of states
- **Clone-Structured Cognitive Graph (CSCG)**: A Bayesian model using "clone" cells to disambiguate aliased sensory observations through sequence learning
- **Path-integration models**: Continuous attractor neural networks (CANNs) and velocity-coupled oscillators (VCOs) that build state-spaces by accumulating self-movement vectors
- **Tolman-Eichenbaum Machine (TEM)**: A model combining abstract path integration with relational memory to enable generalization across environments
- **Spatial Memory Pipeline (SMP)**: An extension of TEM that learns from egocentric pixel inputs rather than allocentric representations

The review evaluates these models against empirical data from rodent and human studies of spatial and nonspatial cognition.

---

### Key findings

The review identifies two core computational principles underlying cognitive map formation:

1. **Latent state inference from sequences**: Because sensory observations are aliased (same observation can occur in different states), states must be inferred from sequences rather than individual observations. Models like CSCG use "clone" cells where multiple cells represent the same sensory observation in different contexts, enabling disambiguation of states with different futures.

2. **Path integration as compressed representation**: Path integration treats all positions equally and exploits relational structure (e.g., "North + East + South + West = 0"), enabling generalization across environments. This contrasts with graph representations that require perfect alignment (an NP-hard problem).

Key empirical predictions and findings:

- The successor representation (SR) predicts that place cells resemble columns of the SR matrix and grid cells resemble eigenvectors of the transition matrix, accounting for many observed phenomena including place field asymmetry, grid realignment, and nonspatial grid-like coding in abstract tasks.

- Hippocampal "splitter cells" in alternation tasks represent latent states that disambiguate the same physical location depending on trajectory history, consistent with CSCG and TEM predictions.

- Entorhinal grid cells generalize across environments (realignment), while hippocampal place cells remap, suggesting entorhinal cortex learns abstract structural representations while hippocampus binds these to specific sensory experiences.

- Recent models (TEM, SMP) show that when artificial agents learn to generalize structural knowledge, they develop representations matching hippocampal place cells, grid cells, border cells, object-vector cells, and goal-vector cells.

---

### Computational framework

The review is organized around **reinforcement learning (RL) state-space representations** and **graph theory**, with particular emphasis on:

1. **Successor Representation (SR)**: A predictive map where S = Σ γⁿTⁿ, representing the expected discounted future occupancy of states. The SR provides a normative framework linking graph structure to neural representations.

2. **Latent variable models**: CSCG and related models frame cognitive mapping as Bayesian inference over hidden states given sequences of observations and actions, using the expectation-maximization algorithm.

3. **Path integration as dynamical systems**: CANNs implement path integration through recurrent neural network dynamics with specific weight matrices that maintain stable bump attractors, formally equivalent to plane wave representations.

4. **Generalization via factorized representations**: TEM and SMP use compositional representations combining abstract structural codes (MEC) with sensory codes (LEC) through conjunctive hippocampal representations, enabling transfer learning across environments.

The unifying insight is that these frameworks all address the same fundamental problem: learning structure from sequences to build state representations that enable prediction, planning, and generalization.

---

### Prevailing model of the system under study

Before this review's synthesis, the field held several related but largely separate perspectives:

1. **Hippocampus as spatial map**: Following O'Keefe and Nadel's cognitive map theory, the hippocampus was viewed primarily as representing physical space through place cells, with entorhinal grid cells providing a path integration substrate.

2. **Hippocampus as relational memory**: Following Eichenbaum and Cohen, the hippocampus was viewed as encoding relationships between items and events, supporting episodic and semantic memory beyond space.

3. **Separate model classes**: Various computational models (SR, CANNs, TEM, CSCG) were developed independently to explain different phenomena, with unclear relationships between them. Some models explained spatial navigation, others explained memory, with limited integration.

4. **Unclear relationship between spatial and nonspatial representations**: While grid-like codes were observed in nonspatial tasks, the computational principles linking these to spatial coding were not well articulated.

---

### What this paper contributes

This review provides a unified computational ontology that integrates previously disparate models and reveals common principles:

1. **Models unified under sequence learning**: The review shows that diverse models (SR, CSCG, TEM, path integration models) all address the same fundamental problem: learning structure from sequences. This reveals that "building cognitive maps" is equivalent to learning the statistical structure of sequences.

2. **Two-function synthesis of hippocampal role**: The review reconciles the "hippocampus as map" vs "hippocampus as memory" debate by proposing both functions operate: hippocampus builds relational maps in novel environments (like CSCG/SR), then transitions to binding cortical map representations via memory (like TEM) as cortical representations become available through generalization.

3. **Unified account of spatial and nonspatial cells**: The review demonstrates that "splitter cells," "lap cells," and other nonspatial hippocampal representations can be understood as latent state representations within the same computational framework that explains place cells—unifying diverse empirical findings under the principle of predicting different futures.

4. **Integration of credit assignment with cognitive mapping**: The review proposes that compositional representations (GVCs, BVCs, OVCs) enable "credit assignment through generalization"—a novel computational role for the cognitive map where state representations come "pre-credit assigned" to enable rapid behavioral adaptation.

5. **New predictions**: The unified framework generates novel predictions, including: contextually modulated vector cells depending on "location in task"; temporal remapping as an explanation for representational drift; and specific patterns of replay alignment between hippocampal, entorhinal, and prefrontal cortices.

---

### Brain regions & systems

- **Hippocampus (HPC)**: Represents the cognitive map through place cells; proposed to serve dual roles—as a relational map builder in novel environments and as a memory system binding cortical representations in familiar environments. Contains various cell types including place cells, splitter cells, lap cells, and conjunctive cells combining spatial and nonspatial information.

- **Medial Entorhinal Cortex (MEC)**: Contains grid cells that provide path integration-based spatial representations; represents abstract structural codes that generalize across environments. Contains grid cells, border cells, object-vector cells, and goal-vector cells. Proposed to learn abstract structural representations reusable across sensory environments.

- **Lateral Entorhinal Cortex (LEC)**: Provides sensory representations to the hippocampal system; codes for specific sensory experiences and item information.

- **Prefrontal Cortex (mPFC/OFC)**: Proposed to represent abstract task-level representations such as "location in task" or task schemas; interacts with hippocampal-entorhinal system for hierarchical task representation.

- **Striatum**: Proposed to interact with cortical-hippocampal systems for reinforcement learning; initially learns behavior in novel tasks, with cortical representations later enabling generalization-based behavior.

---

### Mechanistic insight

This paper is a **review**, not an empirical study, so it does not present new neural data. However, it synthesizes mechanistic insights from computational models that have been validated against neural data:

**Computational level**: The brain solves the problem of learning structured representations from sequences to enable prediction, planning, and generalization. Cognitive maps organize knowledge for flexible behavior by representing states (locations in physical or abstract spaces) and their relationships (transition structures).

**Algorithmic level**: The models propose specific algorithms:
- **CSCG**: Bayesian inference using EM algorithm to learn transition probabilities between "clone" cells that disambiguate aliased observations
- **SR**: Computing the discounted sum of future state occupancies via matrix operations on the transition graph
- **Path integration**: RNN dynamics implementing attractor states that track position through integration of velocity inputs
- **TEM/SMP**: Hebbian learning and Hopfield networks binding abstract cortical representations to sensory experiences via conjunctive hippocampal representations

**Implementational level**: The review connects these algorithms to specific neural circuits:
- MEC grid cells implement path integration via continuous attractor dynamics (evidenced by ring attractors in flies and toroidal topology in rodent grid cells)
- Hippocampal place cells emerge as conjunctions of MEC grid inputs and LEC sensory inputs
- Cortical-hippocampal interactions follow complementary learning systems principles with replay-mediated consolidation

The review synthesizes these across levels to propose that the hippocampal-entorhinal system implements a sequence-learning algorithm that constructs latent state representations enabling both episodic memory and structural generalization.

---

### Limitations & open questions

The review identifies several open questions and limitations in the current understanding:

1. **The role of time in memory and cognitive maps**: How do neural representations maintain stability while also encoding temporal information? Representational drift over time challenges traditional notions of engrams. The hypothesis that drift reflects temporal remapping (with time as a changing factor in hippocampal conjunctions) remains to be tested.

2. **Hierarchical levels of abstraction**: How do representations at different levels of abstraction (sensory, spatial, task-level) interact? The proposed role of prefrontal cortex in representing abstract "location in task" and contextualizing hippocampal representations needs empirical validation.

3. **When and why representations factorize vs. warp**: The tension between factorized representations (enabling generalization) and warped representations (optimized for specific tasks) is not fully resolved. What determines when each is used?

4. **Extension to other cognitive domains**: Can the sequence-learning principles explain representations in language, mathematics, and logical reasoning? The analogy between grid cells and Transformers is suggestive but requires further development.

5. **Biological implementation details**: How are the algorithms implemented at the synaptic and circuit level? The relationship between model variables (e.g., successor representations) and specific neural mechanisms (e.g., synaptic weights) remains incompletely specified.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) - The Hippocampus as a Cognitive Map
- Tolman (1948) - Cognitive maps in rats and men
- Stachenfeld et al. (2017) - The hippocampus as a predictive map (SR model)
- George et al. (2021) - Clone-structured cognitive graph (CSCG)
- Whittington et al. (2020) - Tolman-Eichenbaum Machine (TEM)
- Burak & Fiete (2009) - Continuous attractor network models of grid cells

**Named models or frameworks**:
- Successor Representation (SR)
- Clone-Structured Cognitive Graph (CSCG)
- Continuous Attractor Neural Networks (CANNs)
- Velocity-Coupled Oscillators (VCOs)
- Tolman-Eichenbaum Machine (TEM)
- Spatial Memory Pipeline (SMP)
- Reinforcement Learning (RL) state-space framework
- Predictive coding / free energy principle

**Brain regions**:
- Hippocampus (HPC) - place cells, splitter cells, lap cells, conjunctive representations
- Medial Entorhinal Cortex (MEC) - grid cells, border cells, object-vector cells, goal-vector cells, path integration
- Lateral Entorhinal Cortex (LEC) - sensory representations
- Prefrontal Cortex (mPFC/OFC) - abstract task representations, schemas
- Striatum - reinforcement learning, policy learning

**Keywords**:
cognitive map, hippocampus, entorhinal cortex, grid cells, place cells, successor representation, reinforcement learning, latent states, path integration, sequence learning, generalization, abstraction, replay, state-space, computational neuroscience, Tolman-Eichenbaum machine, clone-structured cognitive graph

### Related wiki pages
- [[wiki/topics/grid_cells_place_cells_and_path_integration_in_cognitive_maps|Grid cells, place cells, and path integration in cognitive maps]]
- [[wiki/topics/reward_modulated_hippocampal_replay_in_spatial_reinforcement_learning|Reward-modulated hippocampal replay in spatial reinforcement learning]]
