---
source_file: "sauer2022_prefrontal_spatial_representation.md"
paper_id: "sauer2022_prefrontal_spatial_representation"
title: "Topographically organized representation of space and context in the medial prefrontal cortex"
authors: "Jonas-Frederic Sauer, Shani Folschweiller, Marlene Bartos"
year: 2022
journal: "PNAS"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
tasks: ["virtual_navigation"]
brain_regions: ["hippocampus_ca1", "entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "prelimbic_cortex"]
keywords: ["spellman_et_al_2015_hippocampal_prefrontal_input_supports_spatial_encoding", "hainmueller_and_bartos_2018_hippocampal_remapping_dynamics", "jay_and_witter_1991_hippocampal_pfc_projection_topography", "ito_et_al_2015_prefrontal_thalamic_hippocampal_circuit_for_navigation", "harvey_et_al_2012_parietal_cortex_spatial_sequences", "mao_et_al_2017_retrosplenial_spatial_context_coding", "named_models_or_frameworks", "virtual_reality_navigation_paradigm", "spatial_information_si_metric", "theta_oscillation_coupling_analysis", "support_vector_machine_position_decoding", "global_remapping_hippocampal_framework", "brain_regions", "medial_prefrontal_cortex_mpfc", "dorsal_mpfc_secondary_motor_cortex", "cingulate_cortex", "ventral_mpfc_prelimbic_cortex", "medial_orbital_cortex", "hippocampal_ca1", "entorhinal_cortex"]
---

### One-line summary

Prefrontal pyramidal neurons display spatially tuned activity during spontaneous unrewarded navigation that remaps in novel environments and exhibits a dorsoventral gradient of tuning strength opposite to hippocampal input density.

---

### Background & motivation

While spatially tuned neurons have been extensively studied in the hippocampal-entorhinal system, their properties in neocortical regions like the medial prefrontal cortex (mPFC) remain poorly understood. Three key questions were unresolved: whether mPFC spatial tuning requires task engagement or reward learning; whether mPFC inherits context-dependent remapping from hippocampal CA1 inputs; and how the topography of hippocampal-prefrontal connections affects spatial tuning depth along the dorsoventral axis.

---

### Methods

- **Subjects**: C57Bl6/J mice (n = 20 for mPFC recordings, n = 2 for CA1 recordings)
- **Task**: Head-fixed mice running on a virtual circular track (1.5 or 2 m length) in self-paced, unrewarded spontaneous locomotion
- **Recording**: Single-unit recordings using 64-channel linear silicon probes acutely lowered into mPFC; spike sorting with MountainSort
- **Cell classification**: Pyramidal cells (n = 1,272 for analysis) vs. GABAergic interneurons based on waveform kinetics
- **Analysis**: Spatial information (SI) content calculated from occupancy-normalized spatial firing rate maps; spatial consistency assessed via correlation between odd/even runs; position decoding using linear support vector classifier; theta coupling analysis using pairwise phase consistency

---

### Key findings

- 35.1% of prefrontal pyramidal neurons displayed significant spatial information (SI) during spontaneous unrewarded navigation
- Average SI of prefrontal pyramidal cells was significantly above chance (P = 1.3 × 10⁻⁵, n = 20 mice)
- Spatial tuning showed significant consistency across runs (correlation between odd/even runs: 0.49 ± 0.02, P = 6.5 × 10⁻¹⁴)
- Position could be decoded from pyramidal cell spike trains above chance level using linear classifiers
- Exposure to a novel environment caused global remapping (mean correlation fam-nov: 0.057 ± 0.028) with rapid formation of new spatial representation
- Re-exposure to familiar environment showed partial reinstatement of original spatial patterns (mean correlation fam-fam': 0.362 ± 0.045, significantly higher than fam-nov, P = 2.4 × 10⁻⁵)
- **Dorsoventral gradient**: Dorsal mPFC showed stronger mean SI than ventral mPFC (P = 0.03, n = 17 mice), opposite to hippocampal input density which is denser ventrally
- Dorsal neurons showed higher spatial consistency (P = 6.9 × 10⁻⁵) and better position decoding accuracy than ventral neurons
- No significant differences in SI were found along laminar (superficial vs. deep) or left-right axes

---

### Computational framework

Not applicable. This is an empirical electrophysiology study characterizing spatial tuning properties without formal computational modeling. However, the findings constrain models of how spatial information propagates from hippocampus to cortex and suggest that prefrontal spatial coding cannot be explained solely by feedforward hippocampal input.

---

### Prevailing model of the system under study

Prior to this study, the prevailing understanding was that: (1) spatial tuning in mPFC requires engagement in cognitive tasks with learned reward locations or rule learning, with little evidence for spatial tuning during spontaneous exploration; (2) hippocampal inputs provide the primary source of spatial information to mPFC, with denser projections targeting ventral prefrontal regions; and (3) the dynamics of spatial coding (e.g., remapping) in hippocampal output regions like CA1 would be inherited by mPFC neurons receiving these inputs.

---

### What this paper contributes

This paper demonstrates that: (1) spatial tuning in mPFC emerges spontaneously during unrewarded self-paced locomotion without task demands, suggesting it represents a "default state" of the network; (2) prefrontal neurons exhibit context-dependent remapping similar to hippocampal CA1, with partial reinstatement of familiar representations upon re-exposure; and (3) counter to predictions based on hippocampal input density, spatial tuning is stronger in dorsal mPFC than ventral mPFC, suggesting spatial tuning depends on additional mechanisms beyond direct hippocampal innervation (e.g., entorhinal inputs, cortico-cortical connections from other spatially tuned areas, or local computation).

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — primary recording site; contains spatially tuned pyramidal neurons during spontaneous navigation
- **Dorsal mPFC** (secondary motor cortex, cingulate cortex) — site of stronger spatial tuning and higher consistency
- **Ventral mPFC** (prelimbic cortex, medial orbital cortex) — site of weaker spatial tuning despite higher hippocampal input density
- **Hippocampal CA1** — source of spatial input to mPFC; shows remapping that may be inherited by prefrontal neurons
- **Entorhinal cortex** — alternative source of spatial signals to mPFC via direct projections
- **Somatosensory cortex** — proposed alternative spatial navigation system with projections to mPFC
- **Thalamic nucleus reuniens** — relays hippocampal afferents to ventral mPFC

---

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight as defined in the instructions. While it provides detailed neural data characterizing spatial tuning properties and their topographical organization, it does not present a formal computational algorithm or specify the precise circuit mechanisms that generate the observed dorsoventral gradient. The authors propose that spatial tuning depends on mechanisms beyond direct hippocampal input (e.g., entorhinal projections, cortico-cortical connections, or local computation), but these hypotheses remain speculative without causal manipulation or computational modeling. The study provides correlational evidence for how spatial information is organized but not algorithmic or implementational-level explanations of how it is computed.

---

### Limitations & open questions

- Whether spatial tuning depends on specific behavioral states (e.g., arousal, attention) not captured by the head-fixed virtual reality setup
- Whether findings generalize to freely moving conditions with naturalistic behaviors (grooming, rearing) that modulate prefrontal activity
- The exact circuit mechanisms producing the dorsoventral gradient in spatial tuning
- Whether dopaminergic or other neuromodulatory inputs contribute to context-dependent remapping in mPFC
- How prefrontal spatial codes interact with hippocampal sequences during behavior
- Whether the dorsoventral functional gradient reflects distinct behavioral roles (sensorimotor vs. limbic integration) as suggested by connectivity patterns
- Whether entorhinal or somatosensory cortical inputs contribute to the dorsal mPFC spatial code

---

### Connections & keywords

**Key citations:**
- Spellman et al. 2015 (hippocampal-prefrontal input supports spatial encoding)
- Hainmueller & Bartos 2018 (hippocampal remapping dynamics)
- Jay & Witter 1991 (hippocampal-PFC projection topography)
- Ito et al. 2015 (prefrontal-thalamic-hippocampal circuit for navigation)
- Harvey et al. 2012 (parietal cortex spatial sequences)
- Mao et al. 2017 (retrosplenial spatial context coding)

**Named models or frameworks:**
- Virtual reality navigation paradigm
- Spatial information (SI) metric
- Theta oscillation coupling analysis
- Support vector machine position decoding
- Global remapping (hippocampal framework)

**Brain regions:**
- Medial prefrontal cortex (mPFC)
- Dorsal mPFC (secondary motor cortex, cingulate cortex)
- Ventral mPFC (prelimbic cortex, medial orbital cortex)
- Hippocampal CA1
- Entorhinal cortex
- Somatosensory cortex
- Thalamic nucleus reuniens

**Keywords:**
- spatial representation
- place cells
- prefrontal cortex
- medial prefrontal cortex
- topographical organization
- dorsoventral gradient
- remapping
- context discrimination
- virtual reality
- spatial information
- theta oscillations
- pyramidal neurons
- head-fixed recordings
- spontaneous locomotion
