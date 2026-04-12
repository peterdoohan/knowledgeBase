---
source_file: "whittington2022_cognitive_map_b.md"
paper_id: "whittington2022_cognitive_map_b"
title: "How to build a cognitive map"
authors: "James C. R. Whittington, David McCaffary, Jacob J. W. Bakermans, Timothy E. J. Behrens"
year: 2022
journal: "Nature Neuroscience"
paper_type: "review"
contribution_type: "review"
tasks: ["navigation_task"]
brain_regions: ["hippocampus", "entorhinal_cortex", "medial_entorhinal_cortex", "lateral_entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex", "striatum"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl", "successor_representation", "attractor_networks", "latent_state_inference", "tolman_eichenbaum_machine"]
keywords: ["okeefe_and_nadel_1978_the_hippocampus_as_a_cognitive_map", "tolman_1948_cognitive_maps_in_rats_and_men", "stachenfeld", "botvinick_and_gershman_2017_the_hippocampus_as_a_predictive_map_successor_representation", "whittington_et_al_2020_the_tolman_eichenbaum_machine_tem", "uria_et_al_2020_the_spatial_memory_pipeline_smp", "george_et_al_2021_clone_structured_cognitive_graph_cscg", "burak_and_fiete_2009_continuous_attractor_network_models_of_grid_cells", "banino_et_al_2018_vector_based_navigation_using_grid_like_representations", "named_models_or_frameworks", "successor_representation_sr", "default_representation_dr", "clone_structured_cognitive_graph_cscg", "tolman_eichenbaum_machine_tem", "spatial_memory_pipeline_smp", "continuous_attractor_neural_networks_canns", "velocity_coupled_oscillators_vcos", "model_free_reinforcement_learning", "model_based_reinforcement_learning", "meta_reinforcement_learning"]
---

### One-line summary

This review organizes models of hippocampal cognitive maps into a formal ontology based on reinforcement learning and sequence learning, revealing how the brain builds latent state representations that enable flexible generalization across spatial and nonspatial domains.

---

### Background & motivation

Cognitive maps were proposed as internal neural representations enabling flexible behavior like planning and novel shortcuts. While substantial neural evidence exists for spatial cognitive maps (place cells, grid cells), recent findings show similar representations in nonspatial domains (sound frequency, value, social hierarchies). The field has developed many models to explain these phenomena, but their relationships and differences have been unclear. This review aims to organize these models into a coherent ontology that reveals parallels between empirical results and generates new predictions about hippocampal-cortical interactions.

---

### Methods

This is a review paper synthesizing existing computational models and empirical findings. The review covers:

- **Model taxonomy**: Organization of cognitive map models into categories based on their computational principles
- **Formal framework**: Reinforcement learning (RL) state-space formalization of cognitive maps
- **Successor representation (SR) models**: Including Stachenfeld et al. (2017) and default representation (DR) extensions
- **Clone-structured cognitive graph (CSCG)**: Hidden Markov model-based approach for learning latent state-spaces from sequences
- **Path integration models**: Continuous attractor neural networks (CANNs) and velocity-coupled oscillators (VCOs)
- **Generalization models**: Tolman-Eichenbaum machine (TEM) and spatial memory pipeline (SMP) that combine path integration with memory
- **Empirical validation**: Comparison of model predictions to recorded neural phenomena (place cells, grid cells, splitter cells, lap cells, time cells)

---

### Key findings

- **Unified computational principle**: The reviewed models share a common framework: cognitive maps are built by learning the structure of sequences. This applies to both spatial navigation (sequences of spatial locations) and nonspatial cognition (sequences of abstract states).

- **Latent state representations**: Many seemingly different hippocampal phenomena (splitter cells, lap cells, time cells) can be understood as latent state representations that disambiguate sensorially identical situations based on their different futures.

- **Two complementary hippocampal roles**: Models suggest two distinct functional roles for the hippocampus: (1) building relational maps (SR/CSCG) where hippocampal neurons represent states/locations, and (2) forming memories that bind cortical map representations to specific experiences (TEM/SMP).

- **Generalization through cortical maps**: Hippocampal representations do not generalize across environments (remapping), but entorhinal representations do (realignment). This suggests cortex learns generalizable structural knowledge while hippocampus binds this to specific sensory contexts.

- **Factorized representations enable composition**: When tasks can be decomposed into independent factors (e.g., space and reward location), the brain represents these factors separately (grid cells + goal-vector cells), enabling flexible composition. When tasks are fixed, warped non-factorized representations emerge.

- **Replay as offline state-space construction**: Hippocampal replay may serve to compose state-spaces offline by path-integrating away from goals and binding vector cells to locations, enabling rapid credit assignment through generalization when the animal returns to those states.

- **Representational drift as temporal remapping**: The observed drift of hippocampal representations over time may reflect remapping due to changing temporal codes in entorhinal cortex, with space and sensory codes remaining stable.

---

### Computational framework

The paper frames cognitive mapping within **reinforcement learning (RL) state-space theory**, with particular emphasis on:

1. **State-space representation**: The problem of building cognitive maps is equivalent to building appropriate state-spaces for RL. States must be latent (not directly observable) because the sensory world is aliased—identical observations can occur in different contexts with different consequences.

2. **Successor representation (SR)**: A specific computational framework where the value of a state is computed as the expected sum of future state occupancies. Mathematically, **S** = (I - γT)^(-1), where T is the transition matrix. The columns of S resemble place cells, and eigenvectors of S resemble grid cells.

3. **Path integration as metric state-space construction**: Continuous attractor neural networks (CANNs) implement path integration by accumulating self-movement vectors. This creates a metric representation of space where relative positions can be computed by vector operations rather than graph search.

4. **Sequence learning and latent state inference**: Hidden Markov model-based approaches (CSCG) learn to infer discrete latent states from sequences of observations and actions, naturally accounting for sensory aliasing by allowing the same observation to map to different latent states (clones).

5. **Generalization through factorized representations**: The Tolman-Eichenbaum machine (TEM) and spatial memory pipeline (SMP) combine path integration (for generalizable structural representations) with memory (for binding structure to specific sensory contexts), enabling generalization across environments with shared structure.

---

### Prevailing model of the system under study

Before this review, the field had several fragmented theoretical perspectives on hippocampal function:

1. **Cognitive map theory (O'Keefe & Nadel)**: The hippocampus constructs a spatial map enabling flexible navigation. This was well-supported by place cell findings but struggled to explain nonspatial hippocampal functions.

2. **Episodic memory theory**: The hippocampus encodes specific episodes and experiences. This explained memory deficits but had difficulty accounting for the spatial selectivity of hippocampal cells.

3. **Relational memory theory (Eichenbaum)**: The hippocampus encodes relations between items, explaining both spatial and nonspatial functions through a common representational principle.

4. **Multiple parallel map theory**: Different hippocampal subregions encode different types of spatial information (sketch maps vs. contour maps).

5. **Separate models for different cell types**: Grid cells were explained by continuous attractor models, place cells by feedforward summation of grid inputs, and various nonspatial cells by task-specific models without unifying principles.

The prevailing view was largely fragmented, with different models explaining different phenomena without clear connections between them. The relationship between spatial and nonspatial cognition remained unclear, and there was no unified computational framework explaining how diverse cell types (place cells, grid cells, splitter cells, time cells, etc.) could emerge from common principles.

---

### What this paper contributes

This review makes several important contributions to understanding hippocampal cognitive maps:

1. **Unified computational ontology**: The paper organizes diverse models into a coherent framework based on RL state-space theory and sequence learning. This reveals that seemingly different models (SR, CSCG, TEM, path integration models) are addressing related computational problems with shared underlying principles.

2. **Integration of spatial and nonspatial cognition**: The review demonstrates that the same computational mechanisms (latent state inference, path integration, generalization) explain both spatial navigation and abstract nonspatial cognition (family trees, social hierarchies, value spaces). This formalizes the long-suspected parallel between hippocampal spatial and nonspatial functions.

3. **Unification of diverse cell types**: The paper shows that place cells, grid cells, splitter cells, lap cells, time cells, and other hippocampal/entorhinal representations can all be understood as manifestations of latent state-space representations optimized for predicting future observations.

4. **Complementary roles of hippocampus and cortex**: The review proposes a functional division where hippocampus can serve as either map-builder (rapid learning of environment-specific state-spaces) or memory (binding cortical generalizations to specific experiences), with a transition between these roles as cortical representations become generalizable through experience.

5. **New predictions**: The framework generates testable predictions about factorized vs. warped representations depending on task structure, contextually modulated vector cells in hierarchical tasks, the role of replay in offline state-space construction, and representational drift as temporal remapping.

6. **Extension to higher cognition**: The review suggests how these principles might extend to language, mathematics, and logical reasoning, providing a pathway toward understanding cognitive maps as Tolman envisaged: the basis of reasoning across all domains of cognition.

---

### Brain regions & systems

- **Hippocampus (HPC)**: Central region for cognitive mapping. Proposed to serve dual roles: (1) building relational maps (successor representation, CSCG) where neurons represent states/locations, and (2) forming memories that bind cortical map representations to specific experiences (TEM/SMP framework). Contains place cells, splitter cells, lap cells, time cells, and conjunctive representations combining spatial and nonspatial information.

- **Entorhinal cortex**: Divided into medial (MEC) and lateral (LEC) subdivisions. MEC contains grid cells (global basis for path integration), head direction cells, and provides abstract structural representations that generalize across environments. LEC provides sensory-specific representations. The interaction between MEC and LEC representations in hippocampus enables generalization.

- **Prefrontal cortex (PFC)**: Specifically medial PFC (mPFC) and orbitofrontal cortex. Proposed to represent abstract task-level variables ("location in task") that can contextualize hippocampal-entorhinal representations. May enable hierarchical abstraction by representing task structure separately from spatial structure.

- **Postsubiculum**: Contains head direction cells that provide critical input for path integration in spatial navigation.

- **Subiculum**: Contains boundary vector cells (BVCs) that encode geometric borders.

- **Striatum/basal ganglia**: Proposed to interact with cortico-hippocampal systems through reinforcement learning. Initially learns behavior via model-free RL, with behavioral sequences replayed to cortex-hippocampus for learning compositional state representations, which are then fed back to improve striatal RL.

---

### Mechanistic insight

This paper does **not** meet the high bar for mechanistic insight as defined in the skill instructions. It is a **review paper** that synthesizes and organizes existing computational models rather than presenting new empirical data that specifically links an algorithm to neural implementation. The paper discusses multiple computational frameworks (successor representation, CSCG, TEM, path integration models) and their relationships to neural phenomena, but these are theoretical proposals rather than direct empirical demonstrations linking specific algorithmic variables to measured neural activity.

The paper reviews models where such links have been made in other studies (e.g., place cells as SR columns, grid cells as SR eigenvectors), but the review itself does not provide new neural data that constrains algorithmic mechanisms. The mechanistic insights discussed are therefore derived from the cited primary literature rather than being original contributions of this review.

---

### Limitations & open questions

The paper acknowledges several limitations and open questions:

- **Role of time in memory and cognitive maps**: The review acknowledges that learned representations cannot remain stable over time since we can remember events at the same place under same conditions but on different days. The mechanism and function of representational drift remain unknown, though the paper proposes temporal remapping as a hypothesis.

- **Interacting levels of abstraction**: While the paper proposes models for hierarchical task representations, how different levels of abstraction (e.g., spatial vs. task-level) interact in the brain remains to be fully understood. The proposal that prefrontal cortex represents abstract task variables while hippocampus-entorhinal cortex represents space requires further empirical validation.

- **Extension to higher cognition**: Whether principles from spatial cognitive maps extend to domains like language, mathematics, and logical reasoning remains largely theoretical. The paper suggests these extensions are plausible but acknowledges they are speculative.

- **Neural implementation details**: Many models make simplifying assumptions about neural implementation. For example, continuous attractor network models use hand-specified weights rather than learned weights, and how path integration is actually learned in biological circuits remains incompletely understood.

- **Factorized vs. warped representations**: While the paper generates predictions about when representations should be factorized versus warped, these predictions require systematic experimental testing.

- **Role of specific cell types**: The function of many entorhinal cell types (object-vector cells, border cells, etc.) in cognitive mapping remains to be fully integrated into computational frameworks.

---

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) - The Hippocampus as a Cognitive Map
- Tolman (1948) - Cognitive maps in rats and men
- Stachenfeld, Botvinick & Gershman (2017) - The hippocampus as a predictive map (successor representation)
- Whittington et al. (2020) - The Tolman-Eichenbaum machine (TEM)
- Uria et al. (2020) - The spatial memory pipeline (SMP)
- George et al. (2021) - Clone-structured cognitive graph (CSCG)
- Burak & Fiete (2009) - Continuous attractor network models of grid cells
- Banino et al. (2018) - Vector-based navigation using grid-like representations

**Named models or frameworks:**
- Successor Representation (SR)
- Default Representation (DR)
- Clone-Structured Cognitive Graph (CSCG)
- Tolman-Eichenbaum Machine (TEM)
- Spatial Memory Pipeline (SMP)
- Continuous Attractor Neural Networks (CANNs)
- Velocity-Coupled Oscillators (VCOs)
- Model-Free Reinforcement Learning
- Model-Based Reinforcement Learning
- Meta-Reinforcement Learning
- Path Integration

**Brain regions:**
- Hippocampus (HPC)
- Medial Entorhinal Cortex (MEC)
- Lateral Entorhinal Cortex (LEC)
- Prefrontal Cortex (PFC)
- Medial Prefrontal Cortex (mPFC)
- Orbitofrontal Cortex (OFC)
- Postsubiculum
- Subiculum
- Striatum
- Basal Ganglia

**Keywords:**
cognitive map, hippocampus, entorhinal cortex, grid cells, place cells, successor representation, reinforcement learning, latent states, path integration, generalization, sequence learning, state-space, relational memory, splitting cells, vector cells, model-based RL, model-free RL, remapping, replay, representational drift, Tolman-Eichenbaum machine, abstract cognition, spatial navigation, nonspatial cognition
