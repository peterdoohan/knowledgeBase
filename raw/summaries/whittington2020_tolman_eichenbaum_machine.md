---
source_file: "whittington2020_tolman_eichenbaum_machine.md"
paper_id: "whittington2020_tolman_eichenbaum_machine"
title: "The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation"
authors: "James C.R. Whittington, Timothy H. Muller, Shirley Mark, Guifen Chen, Caswell Barry, Neil Burgess, Timothy E.J. Behrens"
year: 2020
journal: "Cell"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["navigation_task"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus", "entorhinal_cortex", "medial_entorhinal_cortex", "lateral_entorhinal_cortex", "prefrontal_cortex"]
frameworks: ["successor_representation", "bayesian_inference", "attractor_networks", "tolman_eichenbaum_machine", "compositionality"]
keywords: ["structural_generalization", "relational_memory", "spatial_navigation", "grid_cells", "place_cells", "remapping", "factorized_representations", "conjunctive_coding", "path_integration", "transitive_inference", "social_hierarchy", "object_vector_cells", "border_cells", "attractor_networks", "hebbian_learning", "variational_inference", "cognitive_map", "successor_representations", "latent_states", "lap_specific_cells"]
key_citations: ["tolman1948_cognitive_maps_rats", "stachenfeld2017_hippocampus_predictive_map", "manns2006_declarative_memory_evolution"]
---

### One-line summary

A computational model (TEM) unifies spatial and relational memory by factorizing structural knowledge (represented in entorhinal cortex) from sensory experience (represented in hippocampus), explaining diverse cell types and predicting non-random hippocampal remapping.

### Background & motivation

The hippocampal-entorhinal system is critical for both spatial navigation and relational memory, but it has been unclear how these functions relate mechanistically. While spatial cells (place cells, grid cells) are well-characterized, their relationship to non-spatial relational memory tasks remains mysterious. This paper proposes that both domains can be understood as structural generalization—learning abstract relational structures that transfer across different sensory instantiations.

### Methods

- **Model architecture**: The Tolman-Eichenbaum Machine (TEM) is a generative model with approximate variational inference implemented as a neural network
- **Key components**:
  - Abstract location variables (g) representing structural knowledge, mapped to medial entorhinal cortex (MEC)
  - Grounded/conjunctive variables (p) binding location to sensory experience, mapped to hippocampus
  - Sensory input (x), mapped to lateral entorhinal cortex (LEC)
  - Hebbian memory weights (M) for rapid episodic storage
- **Learning**: Network weights learned via backpropagation through time; Hebbian weights updated at each timestep for memory formation
- **Training environments**: Multiple graph-structured tasks including 2D spatial grids, transitive inference, social hierarchies, and complex lap-based tasks
- **Hierarchical structure**: Multiple parallel streams with different temporal and spatial scales (mimicking grid cell modules)

### Key findings

- TEM successfully learns and generalizes structural knowledge across both spatial and non-spatial tasks, enabling correct first-presentation inferences in novel environments sharing the same structure
- **Grid-like representations** (g): TEM's abstract location cells develop grid cell-like periodic firing patterns in 2D environments, with hexagonal symmetry in hexagonal worlds and square symmetry in square worlds
- **Grid cells generalize**: Grid representations preserve their correlation structure across different environments (same frequency, phase relationships maintained), consistent with empirical observations
- **Place cell-like representations** (p): Conjunctive memory cells develop place fields of varying sizes that remap between environments (global remapping), mimicking hippocampal place cells
- **Diverse entorhinal cell types**: Different behavioral transition statistics produce different cell types—border cells emerge with boundary-seeking behavior, object-vector cells emerge with object-approach behavior
- **Structural remapping prediction**: TEM predicts that hippocampal remapping is not random; place cells retain their relationship to underlying grid cell phases across environments
- **Empirical validation**: Analysis of simultaneously recorded place and grid cells from two datasets (Barry et al., 2012; Chen et al., 2018) confirms that place cell remapping preserves structural relationships to grid cells (significant correlations between grid cell firing at place cell peaks across environments)
- **Complex non-spatial tasks**: TEM reproduces hippocampal cell types observed in a 4-lap reward task (Sun et al., 2020)—place-like cells, lap-specific cells, and lap-counting cells—and predicts corresponding entorhinal representations
- **Non-spatial remapping**: TEM predicts that lap-specific cells should remap spatially but retain their lap specificity across environments, a prediction confirmed in the Sun et al. (2020) data

### Computational framework

**Factorized representation learning with predictive coding and structural abstraction**

TEM formalizes spatial and relational memory as structural generalization—learning abstract graph structures that generalize across different sensory instantiations. The framework combines several computational principles:

1. **Factorization**: Structural knowledge (g) is factorized from sensory content (x), enabling generalization across environments sharing the same structure but different sensory features
2. **Conjunction**: Hippocampal representations (p) bind structural and sensory information, creating episodic memories that are specific to particular experiences
3. **Path integration on arbitrary graphs**: The abstract location variable g implements learned path integration—updating location representations based on relational actions/actions, generalizing beyond spatial coordinates to arbitrary graph structures
4. **Generative modeling with variational inference**: TEM uses a generative model with approximate Bayesian inference (variational autoencoder framework), where an inference network learns to invert the generative model
5. **Dual-timescale learning**: Slow learning (backpropagation) acquires generalizable structural knowledge across many environments; fast learning (Hebbian) stores specific episodic memories within each environment
6. **Hierarchical representation**: Multiple parallel streams with different spatial/temporal scales enable efficient encoding of structure at multiple resolutions (analogous to grid cell modules)

### Prevailing model of the system under study

Before this work, the hippocampal-entorhinal system was understood through two largely separate frameworks:

1. **Spatial navigation perspective**: The hippocampus contains place cells encoding spatial location, while entorhinal cortex contains grid cells providing a spatial metric. These were thought to form a cognitive map for navigation (O'Keefe & Nadel, 1978; Hafting et al., 2005).

2. **Relational memory perspective**: The hippocampus supports relational memory—binding together objects, events, and their relationships—enabling flexible inference beyond simple associations (Cohen & Eichenbaum, 1993; Eichenbaum & Cohen, 2014).

While Eichenbaum and others had suggested these functions might be related, the mechanistic link remained unclear. Grid cells were viewed as specialized for spatial coding, and hippocampal remapping was widely believed to be random. Computational models of grid cells typically used hand-coded mechanisms specific to spatial coordinates, lacking generalization to non-spatial relational tasks.

### What this paper contributes

This paper provides a unifying computational framework that bridges spatial navigation and relational memory:

1. **Unified theory of hippocampal-entorhinal function**: TEM demonstrates that spatial and relational memory rely on the same computational principles—structural abstraction through factorized representations. Spatial navigation emerges as a special case of relational memory, where the relational structure is Euclidean space.

2. **Mechanistic account of diverse cell types**: The model explains the "zoo" of entorhinal cell types (grid cells, border cells, object-vector cells, band cells) as emergent properties of learning optimal representations for predicting transitions under different behavioral statistics. These are not hardcoded but learned basis functions for structural knowledge.

3. **Explanation of hippocampal remapping**: TEM predicts that hippocampal remapping is not random—place cells preserve their relationship to underlying grid cell phases across environments. This structural preservation enables generalization while allowing sensory-specific remapping. The prediction is empirically validated in simultaneously recorded place and grid cell data.

4. **Extension to non-spatial tasks**: The model accurately reproduces hippocampal cell types in complex non-spatial tasks (lap-specific cells, counting cells) and predicts that these cells should show the same remapping properties as spatial cells—preserving non-spatial (lap) specificity while remapping spatially. This prediction is confirmed in empirical data.

5. **Novel predictions**: TEM generates multiple testable predictions, including: (1) LEC-hippocampus relationships should be preserved across remapping; (2) MEC should remap when task structure changes; (3) Multiple place fields within an environment should correlate with MEC firing patterns; (4) Lap-specific cells in non-spatial tasks should exist in MEC.

### Brain regions & systems

- **Medial entorhinal cortex (MEC)**: Represents abstract structural knowledge (g variables). Contains learned basis functions for predicting transitions on graphs. In spatial tasks, these manifest as grid cells, border cells, object-vector cells, and band cells. These representations generalize across environments sharing the same structure.

- **Lateral entorhinal cortex (LEC)**: Provides sensory input (x variables) to the hippocampus. Encodes processed sensory information about objects and experiences. TEM predicts that LEC-hippocampal relationships should be preserved across hippocampal remapping.

- **Hippocampus (CA)**: Forms conjunctive representations (p variables) binding MEC structural codes with LEC sensory inputs. Creates episodic memories through Hebbian learning between co-active neurons. These representations are specific to particular environments and remap between contexts. Place cells, landmark cells, lap-specific cells, and counting cells are all manifestations of this conjunctive coding.

- **Prefrontal cortex (PFC)**: Not explicitly modeled but discussed as potential source of task structure input to MEC, particularly in non-spatial tasks. TEM predicts prefrontal input should influence MEC representations and remapping.

### Mechanistic insight

This paper provides a strong mechanistic insight that maps across Marr's three levels:

**Computational level**: The brain solves the problem of predicting future sensory observations in structurally regular environments. The key computational challenge is generalization—learning abstract structural knowledge that transfers across different sensory instantiations of the same underlying relational structure. This applies equally to spatial navigation (Euclidean space as a relational structure) and non-spatial relational memory (social hierarchies, transitive inference).

**Algorithmic level**: The solution uses factorized representations: (1) abstract location variables (g) encode structural knowledge about transition relations, enabling path integration on arbitrary graphs; (2) sensory variables (x) encode object/experience identity; (3) conjunctive variables (p) bind these through element-wise multiplication, creating episodic memories. Memory storage uses Hebbian learning (fast, within-environment), while structural learning uses gradient descent (slow, across environments). An attractor network enables pattern completion for memory retrieval.

**Implementational level**: The model maps onto specific neural populations: g → medial entorhinal cells (grid, border, object-vector cells), x → lateral entorhinal cells, p → hippocampal cells (place, landmark, lap-specific cells). The Hebbian memory weights M correspond to CA3 recurrent connections. The model explains why grid cells generalize across environments while place cells remap—g is purely structural, while p combines structure with sensory information. The theory predicts that remapping is not random: place cells preserve their relationship to underlying grid phases, enabling structural generalization despite apparent randomness.

### Limitations & open questions

- **Biological implementation**: TEM is not a biophysically realistic model. It uses backpropagation through time and variational inference that lack direct biological implementations. The model abstracts over many known anatomical and biophysical details of the hippocampal formation.

- **Learning mechanisms**: The dual-timescale learning (backpropagation for structure, Hebbian for memory) is computationally powerful but its biological implementation remains unclear. How the brain performs gradient descent over long timescales is an open question.

- **Testing non-spatial predictions**: While spatial predictions are validated, many non-spatial predictions (e.g., MEC remapping in task-switching, lap-specific cells in MEC) await experimental confirmation.

- **Causal manipulations**: The model makes predictions about causal interventions (e.g., LEC-hippocampus correlations), but these have not yet been tested.

- **Extension to continuous spaces**: The model currently uses discrete graph structures. Extension to continuous spaces and more complex, naturalistic environments is a future direction.

- **Integration with reinforcement learning**: While TEM explains representation and inference, integration with action selection and value-based decision-making remains to be fully developed.

### Connections & keywords

- **Key citations**: Tolman (1948) - cognitive maps; Eichenbaum & Cohen (1993, 2014) - relational memory; O'Keefe & Nadel (1978) - hippocampus as cognitive map; Hafting et al. (2005) - grid cells; Manns & Eichenbaum (2006) - factorization of LEC/MEC inputs; Stachenfeld et al. (2017) - successor representation models; Sun et al. (2020) - lap-specific hippocampal cells; Barry et al. (2012), Chen et al. (2018) - simultaneous place/grid cell recordings

- **Named models or frameworks**: Tolman-Eichenbaum Machine (TEM), complementary learning systems (McClelland et al., 1995), wake-sleep algorithm (Hinton et al., 1995), Helmholtz machine (Dayan et al., 1995), variational autoencoder (Kingma & Welling, 2013), successor features/representations (Stachenfeld et al., 2017; Momennejad, 2020)

- **Brain regions**: medial entorhinal cortex (MEC), lateral entorhinal cortex (LEC), hippocampus (CA1, CA3), prefrontal cortex (PFC)

- **Keywords**: structural generalization, relational memory, spatial navigation, grid cells, place cells, remapping, factorized representations, conjunctive coding, path integration, transitive inference, social hierarchy, object-vector cells, border cells, attractor networks, Hebbian learning, variational inference, cognitive map, successor representations, latent states, lap-specific cells
