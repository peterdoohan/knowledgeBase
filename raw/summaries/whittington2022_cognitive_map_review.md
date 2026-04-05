---
source_file: whittington2022_cognitive_map_review.md
title: How to build a cognitive map
authors: James C. R. Whittington, David McCaffary, Jacob J. W. Bakermans, Timothy E. J. Behrens
year: 2022
journal: Nature Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

This review organizes hippocampal and entorhinal models into a unified ontology based on learning and representing the statistical structure of sequences, revealing how cognitive maps for both physical and abstract spaces may be constructed.

### Background & motivation

Cognitive maps—internal neural representations that enable flexible behavior—have been central to understanding hippocampal function since Tolman, but recent years have seen an explosion of computational models that are difficult to compare. This review addresses the need for a clear organizational framework that can relate models to each other and to empirical findings, while also accounting for recent evidence that spatial and nonspatial cognition share representational mechanisms.

### Methods

- **Scope**: Comprehensive review of computational models of hippocampal-entorhinal function from 2017-2022
- **Organization principle**: Models classified by how they learn and represent state-spaces from sequences
- **Key models reviewed**:
  - Successor Representation (SR) and extensions
  - Clone-Structured Cognitive Graph (CSCG)
  - Tolman-Eichenbaum Machine (TEM)
  - Spatial Memory Pipeline (SMP)
  - Continuous Attractor Neural Networks (CANNs) for path integration
  - Default Representation (DR) model
- **Validation approach**: Simulations comparing model predictions to empirical cellular recordings (place cells, grid cells, splitter cells, lap cells, etc.)

### Key findings

- **Unifying principle**: Understanding cognitive maps requires understanding sequence learning—both individual sequences and their statistical structure
- **Two complementary hippocampal roles**: 
  - Hippocampus-as-map models (SR, CSCG): rapid learning of environment-specific maps without generalization
  - Hippocampus-as-memory models (TEM, SMP): slower learning but enables generalization via cortical maps
- **Latent state representations**: Many nonspatial hippocampal cells (splitter cells, lap cells, evidence cells) can be unified as representing latent states that disambiguate identical sensory observations based on different futures
- **Path integration in abstract spaces**: Grid-like codes in nonspatial domains (sound frequency, bird features, social hierarchies) suggest a common mechanism for building cognitive maps across domains
- **Factorization enables generalization**: Compositional representations (grid cells, object-vector cells, boundary-vector cells, goal-vector cells) allow rapid transfer of structural knowledge to novel environments
- **Predictions for replay**: Models suggest replay serves to compose state-spaces from pre-learned basis representations offline, reducing online computational burden
- **Credit assignment through generalization**: Pre-credit-assigned compositional representations can transfer value information to novel goals without slow RL learning

### Computational framework

**Reinforcement Learning (RL) and state-space learning**: The review frames cognitive mapping as the problem of learning appropriate state-spaces for RL. Rather than learning from rewards, the models learn from sensory/state predictions to construct good representations that can later support reward-based learning when rewards appear.

**Key formalisms**:
1. **Successor Representation (SR)**: S = Σ_n γ^n T^n, where T is the transition matrix. SR encodes expected future occupancy and enables efficient value computation (v = Sr).

2. **Path Integration in CANNs**: τ(dg/dt) = -g + f(Wg + Ba), where velocity inputs a update latent state g through recurrent weights W. Enables integration of self-motion vectors.

3. **Clone-Structured Cognitive Graph (CSCG)**: Probabilistic model inferring discrete latent states Z from observation sequences X and actions A: p(X,Z|A) = Π_t p(x_t|z_t)p(z_t,a_t|z_{t-1}). Uses EM algorithm to learn transitions and infer clones.

4. **TEM/SMP**: Combines path-integrating abstract representations (MEC) with sensory predictions (LEC) via hippocampal conjunctive memories. Enables generalization through factorized representations.

### Prevailing model of the system under study

Before this review's synthesis, the field viewed hippocampal cognitive mapping through somewhat fragmented lenses:

1. **Spatial domain dominance**: The dominant understanding was that cognitive maps primarily encoded physical space, with place cells representing unique locations and grid cells providing a spatial metric. Nonspatial responses were often treated as exceptions or epiphenomena.

2. **Multiple disconnected models**: Various models (SR, CANNs, predictive coding models) each explained different aspects of hippocampal function but their relationships were unclear. It was difficult to see whether they were complementary, competing, or simply addressing different phenomena.

3. **Hippocampus-as-map vs. memory debate**: Long-standing debate about whether hippocampus builds cognitive maps (Tolman/O'Keefe) or serves as an index to cortical memories (Eichenbaum/Teyler), with limited integration between these views.

4. **Limited theoretical bridge to nonspatial cognition**: While empirical studies showed nonspatial responses, there was no unified theoretical framework explaining how spatial and nonspatial representations could arise from the same underlying mechanism.

### What this paper contributes

This review synthesizes diverse models into a coherent ontology that reveals deep connections between apparently disparate phenomena:

1. **Unifying sequence-learning principle**: The review establishes that cognitive map construction is fundamentally about learning the statistical structure of sequences. This reframes cognitive mapping from a spatial-specific problem to a general computational principle applicable across domains.

2. **Model taxonomy and relationships**: The review organizes models by their computational approach (latent state inference via sequences vs. path integration), clarifying how SR, CSCG, TEM, SMP, and CANN models relate, complement, and constrain each other.

3. **Integration of hippocampal roles**: The review proposes that hippocampus serves dual roles—both as a rapid map-builder (for novel environments) and as memory-linker (for generalization)—and that these functions are complementary rather than contradictory. This suggests a developmental trajectory where hippocampal maps transition to cortical maps with experience.

4. **Unified account of nonspatial cells**: The review demonstrates that many nonspatial hippocampal phenomena (splitter cells, lap cells, evidence cells, time cells) can be understood as latent state representations that disambiguate sensory aliasing—essentially the same computational problem solved for physical space.

5. **Factorization and generalization framework**: The review formalizes how compositional representations (grid cells, vector cells) enable generalization and rapid transfer, providing normative explanations for why these cell types exist and predicting when they should vs. shouldn't be observed (factorized vs. warped representations).

6. **New predictions**: The synthesis generates novel predictions about replay patterns, cortico-hippocampal interactions, representational drift as temporal remapping, and contextually modulated vector cells that emerge from the integrated framework rather than any single model.

### Brain regions & systems

- **Hippocampus (HPC)**: Serves dual roles as (1) a map-builder that rapidly learns environment-specific state-spaces via SR/CSCG-type mechanisms, and (2) a memory system that binds cortical map representations to sensory experiences via conjunctive coding; contains place cells, splitter cells, lap cells, and time cells that represent latent states
- **Medial Entorhinal Cortex (MEC)**: Represents abstract structural maps that generalize across environments; contains grid cells that provide a global spatial metric via path integration, and their eigenvectors relate to successor representation distance; also contains border cells and head direction cells
- **Lateral Entorhinal Cortex (LEC)**: Represents sensory-specific information; provides sensory predictions that are bound to abstract MEC representations in hippocampus
- **Prefrontal Cortex (PFC)**: Particularly medial PFC/mPFC and orbitofrontal cortex; represents abstract task-level representations and "location in task" that contextualize hippocampal-entorhinal representations; enables hierarchical abstraction where PFC sets goals for spatial navigation
- **Striatum/Basal Ganglia**: Implements model-free RL and behavioral policy learning; interacts with cortico-hippocampal system in a virtuous cycle where RL learns initial policies that are replayed to cortex, which extracts statistical structure to build better state-spaces for subsequent RL

### Mechanistic insight

This review does not meet the high bar for mechanistic insight as defined in the skill, as it is a theoretical synthesis rather than a primary empirical study. However, the reviewed models collectively provide Marr's three-level analysis:

**Computational level**: The brain solves the problem of organizing knowledge for flexible behavior by constructing cognitive maps—structured internal representations that enable rapid inference, planning, and generalization. The core computational problem is learning latent state-spaces from sequences of observations, which provides a unified framework for understanding both spatial and nonspatial cognition.

**Algorithmic level**: Multiple algorithmic implementations are reviewed:
- **Successor Representation (SR)**: Computes expected future state occupancy via S = (I - γT)^(-1), enabling efficient value computation v = Sr
- **Path Integration in CANNs**: Uses recurrent dynamics τ(dg/dt) = -g + f(Wg + Ba) to integrate velocity inputs and maintain stable location representations
- **CSCG**: Uses Bayesian inference (EM algorithm) to infer discrete latent states from sequences, with clone cells disambiguating aliased observations
- **TEM/SMP**: Combines path-integrated abstract representations with sensory predictions via Hebbian learning and Hopfield networks, enabling generalization

**Implementational level**: The review connects these algorithms to specific neural substrates:
- **Grid cells in MEC**: Implement path integration via continuous attractor dynamics; their hexagonal firing patterns emerge as eigenvectors of transition matrices; physical attractor manifolds have been observed in rodent recordings
- **Place cells in HPC**: Represent unique locations via conjunctive coding of MEC grid inputs and LEC sensory inputs; emerge from SR or predictive coding objectives
- **Splitter/lap/time cells**: Represent latent states (trajectory, lap number, elapsed time) that disambiguate sensory aliasing; emerge naturally from sequence-learning models
- **Vector cells (OVCs, BVCs, GVCs)**: Local basis functions that encode relations to objects, boundaries, and goals; enable compositional generalization

The review does not provide new neural data specifically supporting one algorithm over alternatives, but synthesizes how existing data constrains the space of possible algorithms and reveals their computational equivalence at different levels.

### Limitations & open questions

- **Role of time in cognitive maps**: The review notes that representational drift over time challenges traditional notions of stable engrams, but the functional role of this drift remains unclear; one hypothesis is that drift reflects temporal remapping (time as a changing factor like space in remapping)
- **Mechanism of factorization**: While factorized representations are computationally advantageous, the biological mechanisms by which the brain learns to factorize representations remain unspecified
- **Hierarchical abstraction**: How multiple levels of abstraction (e.g., PFC task representations contextualizing HEC spatial representations) are learned and interact requires further theoretical and empirical development
- **From sequences to non-sequential cognition**: Whether principles from sequence learning (path integration, SR) extend to truly non-sequential problems (e.g., understanding that football and Earth are both spheres without sequence experience) remains an open question
- **Testing model predictions**: Many models make competing predictions (e.g., factorized vs. warped representations under different task demands) that require systematic empirical testing
- **Biological plausibility of learning rules**: Some models use EM algorithm or backpropagation; how these map onto biologically plausible learning rules requires further investigation

### Connections & keywords

**Key citations**: O'Keefe & Nadel (1978) The Hippocampus as a Cognitive Map; Tolman (1948) Cognitive maps in rats and men; Stachenfeld et al. (2017) The hippocampus as a predictive map; Whittington et al. (2020) The Tolman-Eichenbaum Machine; George et al. (2021) Clone-structured graph representations; Burak & Fiete (2009) Accurate path integration in continuous attractor network models; Behrens et al. (2018) What is a cognitive map?

**Named models or frameworks**: Successor Representation (SR); Clone-Structured Cognitive Graph (CSCG); Tolman-Eichenbaum Machine (TEM); Spatial Memory Pipeline (SMP); Continuous Attractor Neural Networks (CANNs); Default Representation (DR); Velocity-Coupled Oscillators (VCOs); Reinforcement Learning (RL) state-space learning; Predictive coding; Path integration; Factorized/compositional representations

**Brain regions**: Hippocampus (HPC); Medial Entorhinal Cortex (MEC); Lateral Entorhinal Cortex (LEC); Prefrontal Cortex (PFC); Orbitofrontal Cortex (OFC); Subiculum; Postsubiculum; Striatum/Basal Ganglia

**Keywords**: cognitive map, hippocampus, entorhinal cortex, grid cells, place cells, successor representation, latent state, path integration, generalization, sequence learning, reinforcement learning, computational model, spatial navigation, abstract knowledge, factorized representation, replay, vector cells, splitter cells, Tolman-Eichenbaum Machine, CSCG
