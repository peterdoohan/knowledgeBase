---
source_file: "knudsen2021_hippocampal_value_place.md"
paper_id: "knudsen2021_hippocampal_value_place"
title: "Hippocampal neurons construct a map of an abstract value space"
authors: "Eric B. Knudsen, Joni D. Wallis"
year: 2021
journal: "Cell"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human", "macaque"]
methods: ["fmri"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "orbitofrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl"]
keywords: ["okeefe_and_dostrovsky_1971_original_hippocampal_place_cell_discovery", "okeefe_and_nadel_1978_cognitive_map_hypothesis", "behrens_et_al_2018_what_is_a_cognitive_map", "scoville_and_milner_1957_hippocampal_amnesia_in_h_m", "aronov_et_al_2017_non_spatial_auditory_hippocampal_mapping_in_rodents", "theves_et_al_2019_human_hippocampal_fmri_distances_in_abstract_feature_space", "constantinescu_et_al_2016_grid_like_coding_of_conceptual_knowledge_in_humans", "knudsen_and_wallis_2020_prior_behavioural_ofc_hippocampal_paper_with_the_same_task", "mehta_et_al_2000_experience_dependent_asymmetric_place_field_shaping", "fyhn_et_al_2007_hippocampal_remapping_and_grid_realignment", "baram_et_al_2021_entorhinal_vmpfc_abstract_structure_and_generalisation", "baraduc_et_al_2019_schema_cells_in_macaque_hippocampus", "named_models_or_frameworks", "cognitive_map_okeefe_and_nadel", "1978", "temporal_difference_rl_softmax_choice_model_sutton_and_barto", "1998", "spatial_information_content_metric_skaggs_et_al", "1993", "sparseness_index_treves_and_rolls"]
key_citations: ["behrens2018_cognitive_map_organizing_knowledge", "constantinescu2016_gridlike_conceptual_knowledge"]
---

### One-line summary

Single neurons in the primate anterior hippocampus encode "value place fields" — spatially localised firing patterns in an abstract three-dimensional reward-value space — exhibiting all four canonical properties of rodent spatial place cells: stability across passes, multidimensional tuning, directional selectivity, and contextual remapping.

---

### Background & motivation

The hippocampus supports both episodic memory and spatial navigation via place cells in rodents, and the cognitive map hypothesis proposes a common representational substrate for both. However, direct single-neuron evidence that the primate hippocampus maps purely abstract, cognitive variables (rather than sensory stimuli or physical space) was lacking. Prior human fMRI work suggested distance coding in abstract feature spaces, but lacked the cellular resolution to identify mechanism. This paper asks whether hippocampal neurons encode abstract relational structure — specifically the relative reward values of choice options — using the same place-cell-like code used for space.

---

### Methods

- **Subjects**: Two adult male rhesus macaques (subjects V and T), head-fixed, interacting via saccades.
- **Task**: Subjects chose between pairs of three pictures, each with a slowly drifting reward probability. The evolving reward values traced designed trajectories (circular, helical, and double-lemniscate) through a three-dimensional "value space" (one axis per picture value). Sessions were 27 total (V: 16, T: 11).
- **Neural recordings**: Single-unit recordings from anterior hippocampus (CA1 and CA3) using 16- and 32-channel Plexon V-probes; 2307 neurons total. Location confirmed by sharp-wave ripples, theta power, and bursting patterns.
- **Analysis**: Firing rates were binned along the value-space trajectory (101 bins). Value place fields were identified using spatial information content (bits/spike) exceeding a shuffle-based null distribution (>2 SD) plus minimum firing rate criteria. Stability across passes was assessed by spatial correlation (Pearson's r) between traversals. Dimensionality was tested with a helical trajectory. Directionality was assessed using a double-lemniscate with overlapping segments traversed in congruent and opposing directions. Contextual remapping was tested with an A-B-A' block structure using two picture sets on a common circular trajectory.
- **Controls**: Temporal encoding was ruled out by GLMs with space and time as independent predictors; OFC neurons simulated on the same trajectories produced no value place fields.

---

### Key findings

- Approximately 40–44% of neurons with significant value-space encoding showed stable value place fields across two traversals of a circular path, far exceeding shuffle baselines (~1.3–1.5%).
- Value place fields spanned the full extent of three-dimensional value space (helical trajectory), with field tuning decaying quadratically with distance from the field centre.
- Value place fields were directionally selective: 29–41% of place neurons were positively correlated on congruent passes through overlapping value-space regions, versus only 7–9% on opposing passes (chi-squared tests, both p < 0.001).
- Fields were negatively skewed on the second pass along a previously experienced trajectory segment (consistent with experience-dependent asymmetric shaping of rodent place fields; Mehta et al., 2000), but not on novel passes.
- Introducing novel picture sets (block B) induced remapping: ~62–71% of neurons shifted their preferred value-space location. On return to the original pictures (block A'), three patterns emerged: reversion to original field (~19–22%), retention of B-block field (~17–27%), or retention of both fields (~24–25%). The net effect was low A–B correlation but high A–A' and B–A' correlation, suggesting progressive map generalisation.
- OFC neurons simulated on the same trajectories met no value place field criteria; hippocampal neurons showed significantly greater spatial information and lower sparseness than OFC neurons (Mann-Whitney, p < 10⁻⁶ in both subjects).
- Most value place neurons (73–86%) did not encode simpler value parameters (value sum, range, or difficulty) that are typically seen in OFC, confirming a distinct representational code.

---

### Computational framework

**Cognitive map / relational coding framework.** The paper interprets value place fields as a hippocampal implementation of the cognitive map concept (O'Keefe & Nadel, 1978; Behrens et al., 2018): the hippocampus constructs a metric, multi-dimensional representation of the relational structure of an abstract space, not just physical space.

Key variables: the three-dimensional value space is defined by the reward probabilities (V1, V2, V3) of three stimuli. Each neuron's "value place field" is a region of this space where the neuron fires at elevated rates, analogous to the spatial receptive field of a rodent place cell.

The framework assumes: (1) hippocampal neurons support a population code that tiles the relevant representational space; (2) the map is updated by experience (field skewing, remapping); (3) the map generalises across contexts as overlapping fields accumulate across blocks. A standard temporal-difference RL model fit to behaviour confirmed subjects were tracking values (best-fit α ≈ 0.1, β ≈ 4), providing a quantitative ground truth for the abstract value space the neurons were encoding.

---

### Prevailing model of the system under study

Prior to this paper, the predominant understanding was that hippocampal place cells encode physical/spatial maps, and that the hippocampus contributes to memory and flexible behaviour via episodic encoding and spatial navigation. The cognitive map hypothesis (O'Keefe & Nadel, 1978) proposed that the hippocampus might encode any relational structure, not just space. Supporting human fMRI data showed hippocampal signals correlated with distances in abstract feature space (Theves et al., 2019; Constantinescu et al., 2016), and one rodent study mapped a non-spatial sensory dimension (auditory tone frequency; Aronov et al., 2017). However, none of these had demonstrated single-neuron, place-cell-like encoding of a purely cognitive/abstract variable in primates, leaving it unclear whether the hippocampus truly constructs cognitive maps at the cellular level or merely provides mnemonic support for abstract tasks.

---

### What this paper contributes

This paper provides the first direct single-neuron evidence that the primate hippocampus constructs a map of a purely cognitive variable — relative reward value — using the same representational code as spatial place cells. It establishes that this value map is not simply a scalar value signal (as in OFC) but a multidimensional, directional, experience-sensitive, and remappable spatial code. This explains why hippocampal damage impairs value-based learning and decision-making (Knudsen & Wallis, 2020; Bakkour et al., 2019): the hippocampus provides a relational map of option values that supports flexible, model-based reward predictions. The remapping findings further suggest that value maps generalise across contexts as experience accumulates, providing a candidate mechanism for schema formation in the value domain. The paper resolves a long-standing gap between spatial and mnemonic accounts of hippocampal function by showing a common neural code underlies both.

---

### Brain regions & systems

- **Anterior hippocampus (CA1 and CA3)** — primary site of recording; locus of value place fields; proposed to map abstract relational value space analogously to how posterior hippocampus maps physical space in rodents.
- **Orbitofrontal cortex (OFC)** — contrasted as a control region; encodes scalar and ranked value parameters but does not produce value place fields; proposed to work in concert with hippocampus to construct task models, with theta-band synchrony as a transfer mechanism.
- **Entorhinal cortex** — discussed in relation to grid-cell-like abstract coding (Constantinescu et al., 2016) and as a potential source of relational structure that the hippocampus instantiates in a context-specific map (Baram et al., 2021).

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the algorithmic level, with caveats at the implementational level.

**Criterion 1 (algorithm):** The paper formalises value place fields as a multidimensional population code tiling abstract value space, with properties (stability, directionality, skewing, remapping) that map exactly onto the computational operations proposed for spatial place cells (path integration, experience-dependent prediction, context inference).

**Criterion 2 (neural data):** Single-unit recordings from identified hippocampal subregions (CA1/CA3) directly demonstrate all four properties in the same neurons, with OFC recordings as a within-experiment control.

- **Computational level**: The brain is solving the problem of representing relational structure among choice options (their relative reward values) in a format that supports flexible, model-based decisions. The hippocampus encodes where the agent "is" in the space of possible value configurations.
- **Algorithmic level**: A population of neurons with sparse, localised value place fields tiles the abstract value space. Directionality (sequential activation order) supports trajectory prediction; field skewing encodes anticipation of upcoming states; remapping distinguishes distinct stimulus contexts while generalisation across blocks reflects schema acquisition.
- **Implementational level**: The paper identifies CA1 and CA3 of the anterior hippocampus as the specific subregions, and confirms recordings via sharp-wave ripples, theta power, and complex spiking. However, it does not address cell-type specificity, local circuitry, or neuromodulatory mechanisms. The anterior–posterior axis distinction (value maps anterior, spatial maps posterior) is discussed theoretically but not directly tested.

---

### Limitations & open questions

- Value-space traversal was passive (trajectory was designed and imposed by the experimenter); active navigation of abstract spaces may reveal additional properties.
- Remapping types and their behavioural correlates (reversion, retention, dual-field) were described but not causally linked to generalisation or task performance.
- Functional differences along the hippocampal anterior-posterior axis for value vs. spatial place fields remain untested.
- Whether hippocampal replay, theta cycling, or phase precession occur in the value domain is unknown.
- Whether entorhinal grid-cell-like representations underlie value place fields (analogous to the spatial case) was not examined.
- How different magnitudes of contextual change produce different degrees of remapping (partial vs. global) was not explored.
- Rodent-style chronic recordings across days would be needed to test hierarchical schema formation (e.g., alternating ABA' and CDC' sessions).

---

### Connections & keywords

**Key citations:**
- O'Keefe & Dostrovsky (1971) — original hippocampal place cell discovery
- O'Keefe & Nadel (1978) — cognitive map hypothesis
- Behrens et al. (2018) — What is a Cognitive Map?
- Scoville & Milner (1957) — hippocampal amnesia in H.M.
- Aronov et al. (2017) — non-spatial (auditory) hippocampal mapping in rodents
- Theves et al. (2019) — human hippocampal fMRI distances in abstract feature space
- Constantinescu et al. (2016) — grid-like coding of conceptual knowledge in humans
- Knudsen & Wallis (2020) — prior behavioural/OFC/hippocampal paper with the same task
- Mehta et al. (2000) — experience-dependent asymmetric place field shaping
- Fyhn et al. (2007) — hippocampal remapping and grid realignment
- Baram et al. (2021) — entorhinal-vmPFC abstract structure and generalisation
- Baraduc et al. (2019) — schema cells in macaque hippocampus

**Named models or frameworks:**
- Cognitive map (O'Keefe & Nadel, 1978)
- Temporal difference RL / softmax choice model (Sutton & Barto, 1998)
- Spatial information content metric (Skaggs et al., 1993)
- Sparseness index (Treves & Rolls, 1991)

**Brain regions:**
- Anterior hippocampus (CA1, CA3)
- Orbitofrontal cortex (OFC)
- Entorhinal cortex

**Keywords:**
- hippocampal place cells
- cognitive map
- abstract value space
- value-based decision-making
- relational coding
- hippocampal remapping
- directional place fields
- experience-dependent field skewing
- primate hippocampus
- model-based reinforcement learning
- schema generalisation
- spatial information content
