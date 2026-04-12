---
source_file: "whittington2024_build_cognitive_map.md"
paper_id: "whittington2024_build_cognitive_map"
title: "How to build a cognitive map: insights from models of the hippocampal formation"
authors: "James C.R. Whittington, David McCaffary, Jacob J.W. Bakermans, Timothy E.J. Behrens"
year: 2024
journal: "Unknown (preprint/perspective)"
paper_type: "review"
contribution_type: "theoretical"
brain_regions: ["hippocampus", "entorhinal_cortex", "medial_entorhinal_cortex", "lateral_entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "striatum"]
frameworks: ["reinforcement_learning", "successor_representation", "attractor_networks", "latent_state_inference", "tolman_eichenbaum_machine", "compositionality"]
keywords: ["build", "cognitive", "map", "insights", "models", "hippocampal", "formation"]
key_citations: ["stachenfeld2017_hippocampus_predictive_map", "whittington2020_tolman_eichenbaum_machine", "dayan1993_successor_representation", "behrens2018_cognitive_map_organizing_knowledge", "burak2009_path_integration_grid_cells"]
---

### One-line summary

This Perspective synthesizes computational models of the hippocampal formation to provide a unified framework for how cognitive maps are built through latent state inference, path integration, and generalisation, unifying spatial and abstract cognition.

---

### Background & motivation

Cognitive maps are internal neural representations that afford flexible behaviour by organising knowledge for generalisation to novel experiences. While experimentalists have detailed neural substrates (place cells, grid cells), theorists have developed models bridging neurons, computation, and behaviour. These models often differ in formalism and focus, obscuring their common theoretical foundations. This paper unifies these models into a common language, providing novel interpretations of neural phenomena and speculating on extensions to higher cognitive capacities.

---

### Methods

This is a Perspective/review paper that:
- Synthesises existing computational models of hippocampal and entorhinal function
- Formalises models using reinforcement learning (RL) and probabilistic frameworks
- Demonstrates model behaviour through simulations (TEM, CSCG, SMP)
- Derives novel predictions from integrating model principles

Key models reviewed:
- **Successor Representation (SR)**: Predictive map for value-based RL; rows resemble place cells, eigenvectors resemble grid cells
- **Clone-Structured Cognitive Graph (CSCG)**: Learns latent states from sequences using "clone" cells for sensory aliasing
- **Tolman-Eichenbaum Machine (TEM)** and **Spatial Memory Pipeline (SMP)**: Generalisation models combining path integration with relational memory
- **Default Representation (DR)**: Linear RL model for compositional state-space construction

---

### Key findings

- **Latent state representations** are critical for disambiguating sensory aliasing. Models like CSCG learn these from sequences, capturing phenomena like splitter cells in T-maze alternation tasks.

- **Path integration** provides a compressed, generalisable representation of space. Continuous attractor neural networks (CANNs) naturally produce grid-like periodic representations that extend to unseen space and support error correction.

- **Generalisation** arises from factorised, compositional representations. Grid cells (and their eigenvector equivalents) generalise across environments through realignment, while place cells remap. Models like TEM and SMP achieve systematic generalisation by combining abstract path-integrable representations with flexible sensory associations via hippocampal memory.

- **Complementary systems**: Hippocampus serves dual roles—(1) as a relational map encoding connections between states, and (2) as memory linking cortical representations. With experience, there may be a transition from hippocampus-as-map to hippocampus-as-memory as cortex learns statistical structure.

- **Credit assignment through generalisation**: Compositional representations like goal-vector cells (GVCs) come "pre-credit assigned"—they can immediately provide state-spaces that predict value, enabling rapid behavioural adaptation without new RL learning.

- **Representational drift** may reflect temporal abstraction: If entorhinal cortex represents time as well as space, hippocampal drift could be "temporal remapping"—changing cells due to progressing temporal codes while spatial representations remain stable.

- **Interacting levels of abstraction**: Prefrontal cortex may represent abstract task structure (e.g., "location in task") that contextualises hippocampal-entorhinal spatial representations. Predicts novel cell types like contextually modulated goal-vector cells.

---

### Computational framework

The paper employs multiple interconnected computational frameworks:

**Reinforcement Learning (RL) and State-Space Models**: Cognitive mapping is framed as learning state-spaces for RL. The successor representation (SR) formalises predictive maps where value computation decomposes into state connectedness (SR) and reward. Graphs define state-spaces with nodes as states and edges as transitions, enabling planning through matrix operations.

**Latent Variable Models**: Partially observable environments require inferring latent states from sequences. CSCG uses hidden Markov model-like structure with emission distributions linking sensory observations to latent "clone" states. This de-aliases identical sensory inputs that have different futures.

**Path Integration and Continuous Attractor Networks**: Spatial representations emerge from continuous attractor neural networks (CANNs) that integrate velocity inputs. The dynamics follow: τ(dh/dt) = -h + f(Wh + Ba), where W is recurrent weights, B is velocity coupling, and a is action/velocity. Different cell types (head-direction, place, grid) emerge from different weight structures.

**Generalisation and Compositional Models**: TEM and SMP combine:
- Abstract path-integrable representations (medial entorhinal cortex, MEC)
- Sensory representations (lateral entorhinal cortex, LEC)  
- Relational memory binding them (hippocampus)

This factorisation enables generalisation: the same abstract map (MEC) binds to different sensory inputs (LEC) in different environments via different hippocampal associations.

**Eigenvector Analysis**: Grid cells relate to eigenvectors of transition matrices or place cell correlations. Diagonalisation T = VΛV^T reveals that eigenvectors V are shared across all powers of T (multi-step transitions), enabling efficient planning and path integration by operating in eigenspace.

---

### Prevailing model of the system under study

Before this paper's synthesis, the field held several partially overlapping but often disconnected views:

**Spatial vs. Memory Debate**: The hippocampus was seen as either primarily a spatial map (O'Keefe & Nadel's cognitive map theory) or a memory system (Eichenbaum's relational memory theory). These views were often treated as competing rather than complementary.

**Separate Models for Different Phenomena**: Different models addressed different aspects of hippocampal function with little unification:
- Place cells were modelled as learned responses to sensory inputs or attractor dynamics
- Grid cells were modelled as path integrators via continuous attractor networks or oscillatory interference
- Non-spatial cells were treated as separate phenomena without unifying principles
- Remapping was modelled as network instability or input changes

**Spatial-Only or Abstract-Only Representations**: Grid cells were initially thought to represent only physical space; their appearance in non-spatial tasks was surprising. Conversely, hippocampal "time cells" and splitter cells were treated as distinct from spatial representations rather than manifestations of a common latent state mechanism.

**Fixed Representations**: The prevailing view assumed stable representations over time, with representational drift viewed as noise or error rather than a potentially functional mechanism.

**Distinct Computational Frameworks**: Models used different formalisms (attractor networks, reinforcement learning, hidden Markov models, memory networks) without clear connections between them, making it difficult to compare predictions or integrate findings.

---

### What this paper contributes

This Perspective provides a unifying theoretical synthesis that reframes disparate models and phenomena within a common computational language:

**Unified Theoretical Framework**: The paper integrates multiple computational models (SR, CSCG, TEM, SMP, CANNs) into a coherent framework based on reinforcement learning state-spaces, latent state inference, and generalisation. This allows comparison of model predictions and identification of complementary strengths.

**Resolution of Spatial-Memory Debate**: Rather than treating hippocampus-as-map and hippocampus-as-memory as competing views, the paper proposes a unified account where hippocampus serves both roles situationally: as a relational map when no prior cortical structure exists, and as memory linking cortical representations when cortex has learned statistical structure. This predicts a transition from map-to-memory with experience, tied to generalisation ability.

**Unified Account of Non-Spatial Cells**: The paper demonstrates that diverse non-spatial hippocampal phenomena (splitter cells, time cells, lap cells, evidence cells) can be understood as latent state representations for disambiguation and generalisation. Using TEM simulations, it shows these cells emerge naturally from learning state-spaces that predict different futures in sensorially identical situations.

**Novel Interpretation of Representational Drift**: Reframing representational drift as "temporal remapping"—where changing hippocampal representations reflect progressing temporal codes while spatial codes remain stable. This connects drift to existing models of hippocampal remapping and suggests it may enhance generalisation by providing data augmentation.

**Credit Assignment Through Generalisation**: Introduces the concept that compositional representations (like goal-vector cells) can come "pre-credit assigned," enabling immediate value prediction without new RL learning. This reframes the role of cognitive maps in behaviour as composing pre-learned basis representations rather than online value computation.

**Hierarchical Extension to Prefrontal Cortex**: Extends the framework to include prefrontal cortex as representing abstract task structure that contextualises hippocampal-entorhinal spatial representations. Predicts novel cell types like route-dependent, contextually modulated goal-vector cells.

**Integration of Eigenvector-Based Mechanisms**: Unifies path integration, successor representation, and exploration through eigenvector analysis of transition matrices, showing how grid-like codes enable efficient multi-step prediction and planning.

**Falsifiable Predictions**: Derives specific testable predictions from the integrated framework, including: (1) factorised vs. warped representations depending on task structure; (2) transition from hippocampal map-to-memory with experience; (3) temporal structure in representational drift; (4) contextually modulated vector cells in PFC; (5) coordinated replay of abstract and sensory representations.

---

### Brain regions & systems

**Hippocampus (HC)**:
- Dual role: (1) relational map encoding connections between states (CSCG-like), and (2) memory linking cortical representations (TEM-like)
- Contains conjunctive cells binding abstract (MEC) and sensory (LEC) representations
- Exhibits remapping (non-generalising) to distinguish different environments/contexts
- Site of representational drift over time, potentially reflecting temporal remapping
- Source of splitter cells, time cells, lap cells, and other latent state representations

**Medial Entorhinal Cortex (MEC)**:
- Contains grid cells: periodic path-integrating representations that generalise across environments (realignment)
- Represents abstract structural knowledge through path integration
- Provides eigenvector-like representations enabling efficient planning and navigation
- Contains object-vector cells (OVCs), border-vector cells (BVCs), and goal-direction cells (GVCs) as local bases
- Drives place cells more than vice versa (path integration signals dominate)

**Lateral Entorhinal Cortex (LEC)**:
- Represents sensory/non-spatial information ("what" in the cognitive map)
- Provides sensory input to hippocampal conjunctive representations
- Together with MEC, enables factorisation of abstract structure from sensory content

**Prefrontal Cortex (PFC) / Medial Prefrontal Cortex (mPFC)**:
- Represents abstract task structure and "location in task"
- May contain contextually modulated goal-vector cells
- Provides contextual input to hippocampal-entorhinal system for hierarchical task organisation
- Engaged in relational processing and structural abstraction
- Shows hexagonal symmetry in abstract navigation tasks (fMRI evidence)

**Striatum**:
- Locus of initial reinforcement learning (RL) for generating behaviour
- Provides training signals for cortico-hippocampal learning from action sequences
- Engaged in model-free value learning that can bootstrap cortical map construction

---

### Mechanistic insight

This paper provides mechanistic insight at Marr's three levels, though as a review/synthesis it primarily formalises and integrates existing models rather than presenting new empirical data:

**Computational level**: The brain solves the problem of flexible behaviour by learning and using cognitive maps—structured internal representations that afford generalisation to novel situations. The key computational challenge is learning appropriate state-space representations that: (1) disambiguate aliased sensory observations (latent states), (2) generalise across environments (path integration/periodic representations), and (3) compose to support novel task configurations (factorisation). This is framed as learning "so that you do not have to learn"—minimising online computation through appropriate prior structure.

**Algorithmic level**: Multiple algorithmic implementations are reviewed and unified:

- **Successor Representation (SR)**: M = Σ γⁿTⁿ, where T is the transition matrix. Rows resemble place cells; eigenvectors resemble grid cells. Decomposes value computation into state connectedness and reward.

- **Clone-Structured Cognitive Graph (CSCG)**: Learns latent states via EM algorithm, where emission distributions p(x|z) link sensory observations to latent "clone" states. Captures sensory aliasing through multiple clones per observation.

- **Tolman-Eichenbaum Machine (TEM) / Spatial Memory Pipeline (SMP)**: Combine path integration p(zₜ|zₜ₋₁, aₜ) with relational memory M linking abstract (MEC) and sensory (LEC) representations. Enables generalisation via factorised structure.

- **Continuous Attractor Neural Networks (CANNs)**: τ(dh/dt) = -h + f(Wh + Ba) for path integration. Different weight structures produce head-direction, place, and grid cell responses.

**Implementational level**: The paper maps algorithmic components to neural substrates:

- **MEC/Grid cells**: Implement path integration through CANNs or eigenvector representations. Periodic firing enables generalisation across environments via realignment.

- **Hippocampus**: Implements dual functions—(1) relational maps via recurrent connections (CSCG-like), and (2) conjunctive memory binding MEC and LEC representations (TEM-like). Conjunctive cells receive both abstract and sensory input.

- **LEC**: Provides sensory/non-spatial input to hippocampal conjunctive representations.

- **PFC**: Represents abstract task structure and "location in task" that contextualises hippocampal-entorhinal processing.

- **Striatum**: Initial RL-based behaviour generation that provides training signals for cortical map learning.

The paper notes that while these models provide mechanistic insight, they often rely on hand-tuned weights (CANNs) or simplified learning rules. Recent progress has shown learned grid-like representations in trained RNNs, and the integration of biological constraints (positive firing rates) can explain transitions from 4-fold to 6-fold grid symmetry.

---

### Limitations & open questions

- **Model learning**: Many path integration models (CANNs, VCOs) use hand-tuned recurrent weights rather than learned from experience. Whether biological circuits learn these weights through development or evolution remains unclear.

- **Representational drift**: The mechanism and function of drift are unknown. The temporal remapping hypothesis makes testable predictions (ordered drift, temporal structure) but requires empirical validation.

- **Hierarchical abstraction**: While the framework extends to PFC, specific predictions about how abstract task representations develop and interact with spatial codes need experimental testing.

- **Non-sequence cognition**: Whether path integration principles extend to non-sequential domains (e.g., understanding object categories) remains speculative. The mapping from grid cells to language/mathematics is suggestive but not established.

- **Biological implementation details**: How precisely eigenvector-like representations are computed, how compositional binding occurs at the synaptic level, and how prefrontal-hippocampal-thalamic circuits implement hierarchical control all require further mechanistic detail.

- **Optimal replay patterns**: Under the credit assignment through generalisation framework, formal predictions about replay patterns and their alignment with cortical replay remain to be developed and tested.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) - The Hippocampus as a Cognitive Map
- Stachenfeld et al. (2017) - Successor representation model
- George et al. (2021) - CSCG model
- Whittington et al. (2020) - Tolman-Eichenbaum Machine (TEM)
- Uria et al. (2020) - Spatial Memory Pipeline (SMP)
- Burak & Fiete (2009) - CANN model of grid cells
- Dayan (1993) - Successor representation
- Marr (1971), McClelland et al. (1995) - Complementary learning systems
- Behrens et al. (2018) - What is a cognitive map?

**Named models or frameworks**:
- Successor Representation (SR)
- Clone-Structured Cognitive Graph (CSCG)
- Tolman-Eichenbaum Machine (TEM)
- Spatial Memory Pipeline (SMP)
- Continuous Attractor Neural Networks (CANNs)
- Default Representation (DR) / Linear RL
- Velocity-Coupled Oscillators (VCOs)
- Reinforcement Learning (RL) state-space models
- Complementary Learning Systems theory
- Hippocampal indexing theory
- Path integration
- Predictive cognitive map
- Credit assignment through generalisation
- Meta-RL framework

**Brain regions**:
- Hippocampus (HC) - place cells, conjunctive representations, relational maps, memory
- Medial Entorhinal Cortex (MEC) - grid cells, path integration, object-vector cells, border-vector cells, goal-vector cells
- Lateral Entorhinal Cortex (LEC) - sensory representations, non-spatial input
- Prefrontal Cortex (PFC) / Medial Prefrontal Cortex (mPFC) - abstract task structure, location in task
- Striatum - reinforcement learning, action generation
- Postsubiculum - head-direction cells
- Subiculum - boundary vector cells
- Nucleus reuniens - potential thalamic relay between PFC and hippocampus

**Keywords**:
cognitive map, hippocampus, entorhinal cortex, grid cells, place cells, successor representation, latent states, path integration, generalisation, reinforcement learning, continuous attractor networks, compositionality, TEM, CSCG, representational drift, prefrontal cortex, replay, credit assignment
