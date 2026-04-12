---
source_file: ito2015_prefrontal_thalamic_hippocampus.md
paper_id: ito2015_prefrontal_thalamic_hippocampus
title: "A prefrontal–thalamo–hippocampal circuit for goal-directed spatial navigation"
authors:
  - "Hiroshi T. Ito"
  - "Sheng-Jia Zhang"
  - "Menno P. Witter"
  - "Edvard I. Moser"
  - "May-Britt Moser"
year: 2015
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - open_field
  - t_maze
  - foraging_task
methods:
  - optogenetics
  - tetrode_recording
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - prelimbic_cortex
  - thalamus
frameworks:
  - reinforcement_learning
keywords:
  - trajectory_dependent_place_cells
  - nucleus_reuniens
  - medial_prefrontal_cortex
  - hippocampal_ca1
  - goal_directed_spatial_navigation
  - prospective_coding
  - thalamocortical_relay
  - optogenetic_silencing
  - population_decoding
  - spatial_working_memory
  - place_cell_rate_remapping
  - cortico_hippocampal_circuit
  - prefrontalthalamohippocampal
  - circuit
  - goal
  - directed
  - spatial
  - navigation
key_citations:
  - moser2008_place_cells_grid_cells
wiki_pages:
  - wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation
  - wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory
  - wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits
---

### One-line summary

The nucleus reuniens of the thalamus relays trajectory-direction signals from medial prefrontal cortex to hippocampal CA1, and this mPFC–NR–CA1 circuit is necessary for CA1 place cells to encode upcoming (prospective) spatial trajectories during goal-directed navigation.

---

### Background & motivation

Hippocampal place cells encode not only current position but also the trajectory an animal is about to take — a phenomenon called trajectory-dependent firing — but the circuit origin of this prospective information was unknown. Medial prefrontal cortex (mPFC) is implicated in action selection and goal-directed behaviour, yet it has no direct projections to the hippocampus. The nucleus reuniens (NR) of the midline thalamus has reciprocal connections with mPFC and strong excitatory projections specifically to CA1 (but not CA3), making it a candidate relay. This paper tests whether the mPFC–NR–CA1 route is a functional pathway for supplying goal-direction information to hippocampal place-cell representations.

---

### Methods

- **Task**: Continuous T-maze alternation task in rats; animals alternate left/right turns on successive laps. A delayed version (10–15 s barrier at stem base) was also used to dissociate prospective from retrospective components.
- **Subjects**: 36 male Long-Evans rats; multiple implant configurations targeting CA1, CA3, NR, and mPFC with independently movable tetrodes.
- **Recordings**: Simultaneous multi-tetrode recordings from CA1 (n = 363 cells), CA3 (n = 180 cells), NR (n = 64 cells), and mPFC (n = 338 cells) during task performance and open-field foraging.
- **Lesions**: Bilateral ibotenic acid lesions of NR in 4 rats; subsequent CA1 recordings compared to controls.
- **Optogenetics**: AAV-mediated expression of eNpHR3.1 (enhanced halorhodopsin) in NR neurons; 532 nm laser silencing of NR during task; simultaneous CA1 recording before, during, and after silencing.
- **Analysis**: Two-way ANOVA and ANCOVA (with speed, head direction, lateral position as covariates) to identify trajectory-dependent cells; linear support-vector-machine decoder applied bin-by-bin along the maze stem; bootstrap subsampling to isolate prospective and retrospective decoding components.

---

### Key findings

- **CA1 vs. CA3 trajectory-dependent firing**: 55.1% of CA1 stem place cells showed significant trajectory-dependent rate changes vs. only 17.7% of CA3 cells (Z = 3.78, P < 0.001); mean rate difference CA1: 32.8 ± 2.6%, CA3: 19.8 ± 3.1%.
- **NR carries trajectory signals**: 42.2% of NR cells (27/64) fired differentially on left vs. right trajectories; mean rate change 22.5 ± 2.5%; proportion not significantly different from CA1.
- **mPFC carries trajectory signals**: 38.2% of mPFC cells (129/338) were trajectory-dependent; mean rate change 29.6 ± 1.2%.
- **NR lesions reduce CA1 trajectory coding**: Only 15.9% of CA1 stem cells from NR-lesioned animals were trajectory-dependent (vs. 55.1% controls; Z = 4.36, P < 0.001); mean rate change fell to 18.7 ± 2.7%, comparable to CA3 controls.
- **Optogenetic NR silencing**: Acutely reducing NR activity by ~63% decreased the proportion of trajectory-dependent CA1 cells from 72% (36/50) to 44% (22/50; Z = 2.837, P = 0.005); effect was reversible on laser-off trials.
- **Prospective dominance**: On error trials, trajectory-decoding accuracy degraded toward chance near the decision point in all three regions, indicating the signal predicts the animal's next (correct) choice rather than merely reflecting prior history. The prospective component was maintained under delay conditions that suppressed retrospective working memory; the retrospective component was lost after delays.
- **Prospective decoding magnitude**: In mPFC, prospective decoding reached ~62–66% correct on the last half of the stem; similar gradients in NR and CA1. The prospective component in CA1 was abolished by NR lesions.
- **No spatial tuning in NR or mPFC**: Both regions showed negligible location-selective firing in open-field tests, confirming the trajectory signal is task-contingent, not a spatial map.

---

### Computational framework

Not a computational modelling paper; the analysis uses decoding (support vector machine classifier applied to population firing rates) as an analytical tool rather than as a model of neural computation. The framework is implicitly a **population vector / multiplexed rate coding** account: the distribution of firing rates across a CA1 ensemble collectively encodes both the animal's spatial position and its intended trajectory direction, with trajectory information supplied as a modulatory input via NR. The results constrain models of how prefrontal goal signals are routed to hippocampal spatial representations — relevant to any framework (e.g., predictive coding, goal-directed RL with a hippocampal map) that requires the hippocampus to combine current-location and future-goal information.

---

### Prevailing model of the system under study

Before this paper, place cells were understood as part of an allocentric spatial map (O'Keefe & Nadel 1978; Moser et al. 2008) that faithfully encodes current position. The trajectory-dependent modulation of place-cell firing (Wood et al. 2000; Frank et al. 2000) had been documented but its source was unresolved. The prevailing assumption was that the hippocampus somehow integrates sensory context with an internally generated goal representation, but the circuit by which prefrontal goal/action-selection signals reach CA1 was unknown. mPFC was known to lack direct projections to the hippocampus proper; NR was anatomically characterized as a thalamic relay but its functional role in live navigation had not been established. The field had no causal evidence linking any upstream structure to trajectory-dependent CA1 firing.

---

### What this paper contributes

The paper establishes the mPFC–NR–CA1 pathway as causally necessary for trajectory-dependent place-cell firing. Before this work, the circuit source of prospective trajectory information in CA1 was entirely open. The study shows:
1. All three nodes (mPFC, NR, CA1) carry trajectory signals that are predominantly prospective.
2. Disrupting NR — whether permanently (lesion) or acutely (optogenetics) — collapses CA1 trajectory coding to levels seen in CA3, which lacks NR input.
3. The NR signal is not a working-memory echo of the past lap but a forward-pointing representation that builds as the animal approaches the choice point.
4. The thalamus acts as a functional relay enabling long-range cortical–hippocampal communication, extending the principle that cortico-cortical communication can be thalamically mediated (Sherman & Guillery 2006; Sommer & Wurtz 2006) into the spatial navigation domain.

---

### Brain regions & systems

- **CA1 (hippocampus)**: Primary target of NR input; locus where trajectory-direction signals are combined with spatial position signals to produce trajectory-dependent place-cell firing.
- **CA3 (hippocampus)**: Negative control — does not receive direct NR input; shows minimal trajectory-dependent firing, confirming NR specificity.
- **Nucleus reuniens (NR), midline thalamus**: Central relay node; relays trajectory/goal-direction signals from mPFC to CA1; NR neurons fire differentially on left vs. right trajectories; necessary for CA1 trajectory coding.
- **Medial prefrontal cortex (mPFC)**: Anterior cingulate and dorsal prelimbic cortex; source of goal/trajectory-direction signals; neurons fire differentially on alternating trajectories without location-selectivity; projects to NR.
- **Entorhinal cortex**: Mentioned as a possible indirect route (mPFC → NR → entorhinal → CA1) contributing in parallel; not directly recorded.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Criterion 1 (algorithm)**: The paper formalises a circuit algorithm: mPFC encodes the animal's intended next trajectory; this signal is relayed via NR to CA1, where it modulates the firing rates of spatially tuned cells, producing a combined position-×-trajectory representation.

**Criterion 2 (neural data supporting that algorithm)**: Simultaneous multi-site recordings show correlated trajectory signals across mPFC, NR, and CA1. Causal lesion and optogenetic experiments demonstrate that removing NR activity specifically reduces the trajectory-dependent component of CA1 firing, without affecting place-field location, overall firing rate, behaviour, or CA3 coding.

**Marr's levels:**

- **Computational**: The brain needs to represent not just where the animal is but where it is going, in order to implement map-based route planning. CA1 must integrate current-position information (from intrinsic hippocampal circuitry) with goal/trajectory information to guide future movement.
- **Algorithmic**: mPFC maintains a population-level representation of the intended trajectory direction (prospective signal); this is transmitted through NR to CA1, where it modulates the gain of spatially tuned cells without shifting their place fields — implementing a multiplicative or additive combination of location and trajectory codes. The prospective component builds progressively along the maze stem as the choice point approaches.
- **Implementational**: NR neurons are excitatory and project specifically to CA1 stratum lacunosum-moleculare (not to CA3); optogenetic silencing used CaMKIIa-driven halorhodopsin, suggesting the relevant NR projection neurons are glutamatergic. The paper does not resolve the specific cell types in CA1 that receive NR input (though anatomical literature cited notes NR innervates both pyramidal cells and GABAergic interneurons in CA1), nor the synaptic mechanism by which NR input modulates firing-rate gain.

---

### Limitations & open questions

- NR lesions were unilateral in some configurations; the full bilateral contribution and lateralization effects were not systematically explored.
- Alternation task performance was unaffected by NR lesions or silencing, suggesting trajectory-dependent CA1 firing is not required for this simple task. The conditions under which NR-dependent CA1 trajectory coding becomes behaviourally necessary remain unresolved.
- The paper does not establish what computations in mPFC generate the prospective trajectory signal, or how mPFC itself comes to represent the intended future trajectory.
- Potential contribution of the indirect mPFC → NR → entorhinal → CA1 route was not experimentally dissected.
- The cellular and synaptic mechanism by which NR input modulates CA1 firing-rate gain (additive vs. multiplicative; excitatory vs. disinhibitory via interneurons) is not resolved.
- Whether the same circuit is required for more complex navigation tasks (open-field goal-directed navigation, novel environments) was not tested.
- The paper used exclusively male Long-Evans rats; generalizability across sexes and species is untested.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — *The Hippocampus as a Cognitive Map* (foundational place-cell framework)
- Wood et al. (2000, *Neuron*) — original description of trajectory-dependent firing in CA1
- Frank et al. (2000, *Neuron*) — trajectory encoding in hippocampus and entorhinal cortex
- Ferbinteanu & Shapiro (2003, *Neuron*) — prospective and retrospective components in hippocampal coding
- Vertes et al. (2007, *Brain Res. Bull.*) — NR as mPFC–hippocampus link
- Xu & Sudhof (2013, *Science*) — NR circuit for memory specificity
- Sherman & Guillery (2006) — thalamus and cortical function
- Pfeiffer & Foster (2013, *Nature*) — hippocampal place-cell sequences for future paths

**Named models or frameworks**:
- Continuous T-maze alternation task (modified version of Wood et al. 2000)
- Support vector machine linear decoder (SVM for population trajectory decoding)
- eNpHR3.1 optogenetic silencing (CaMKIIa-driven halorhodopsin)

**Brain regions**:
- Hippocampus (CA1, CA3)
- Nucleus reuniens (NR), midline thalamus
- Medial prefrontal cortex (mPFC; anterior cingulate, dorsal prelimbic)
- Entorhinal cortex (indirect route, not recorded)

**Keywords**:
- trajectory-dependent place cells
- nucleus reuniens
- medial prefrontal cortex
- hippocampal CA1
- goal-directed spatial navigation
- prospective coding
- thalamocortical relay
- optogenetic silencing
- population decoding
- spatial working memory
- place cell rate remapping
- cortico-hippocampal circuit

### Related wiki pages
- [[wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation|Hippocampal–prefrontal mechanisms of route planning and detour navigation]]
- [[wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory|Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory]]
- [[wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits|Prospective spatial coding in hippocampal–medial prefrontal circuits]]
