---
source_file: ito2018_prefrontal_hippocampal_navigation.md
paper_id: ito2018_prefrontal_hippocampal_navigation
title: "Prefrontal–hippocampal interactions for spatial navigation"
authors:
  - "Hiroshi T. Ito"
year: 2018
journal: "Neuroscience Research"
paper_type: review
contribution_type: review
species:
  - rat
methods:
  - electrophysiology
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - ventromedial_prefrontal_cortex
  - thalamus
keywords:
  - spatial_navigation
  - cognitive_map
  - place_cells
  - grid_cells
  - prospective_coding
  - trajectory_dependent_firing
  - hippocampal_replay
  - sharp_wave_ripples
  - nucleus_reuniens
  - prefrontalhippocampal_interactions
  - goal_representation
  - theta_sequences
  - prefrontalhippocampal
  - interactions
  - spatial
  - navigation
key_citations:
  - ito2015_prefrontal_thalamic_hippocampus
  - buzsaki2015_hippocampal_sharp_wave_ripple
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits
---

### One-line summary

This review synthesises evidence that goal-directed spatial navigation depends on functional interactions between the hippocampus and medial prefrontal cortex (mPFC), mediated in part by the thalamic nucleus reuniens (NR), with each structure contributing distinct computations — spatial mapping versus goal representation — to route planning.

---

### Background & motivation

Decades of research established that the hippocampus and parahippocampal structures encode an internal spatial map via place cells and grid cells, but how this map is used to plan routes to remembered goals remained unclear. Goal-directed navigation requires the animal to estimate future positions and direct behaviour toward an out-of-sight destination — operations that place-cell activity alone, which primarily reflects an animal's current position, does not straightforwardly explain. The review asks how prospective (future-oriented) hippocampal activity arises, and what role prefrontal–hippocampal interactions play in generating it.

---

### Methods

- **Paper type**: Narrative review of empirical and computational literature.
- **Scope**: Rodent (primarily rat) electrophysiology and lesion studies, with some human neuroimaging and clinical case evidence; includes a single bat study. Covers behavioural studies of map-based navigation, place-cell and grid-cell physiology, replay/sharp-wave ripple (SWR) research, mPFC lesion and inactivation work, and circuit studies of the mPFC–NR–CA1 pathway.
- **Synthesis method**: Narrative; studies organised thematically around (1) hippocampal spatial representation, (2) prospective coding in place cells, (3) mPFC contributions to goal representation, and (4) bidirectional prefrontal–hippocampal circuit interactions.

---

### Key findings

- Place cells exhibit multiple forms of prospective activity: theta phase precession extends to represent upcoming path segments; trajectory-dependent firing at T-maze decision points reflects the animal's next route choice; and brief (~100 ms) population spike sequences during rest/awake-immobility (replay events) often correspond to the animal's future planned trajectory.
- Disrupting replay events by electrical stimulation locked to SWR onset (Jadhav et al., 2012) impairs spatial working memory performance, establishing a causal role for replay in navigation.
- mPFC lesions and inactivation impair flexible route planning (novel start positions, delayed alternation), and mPFC neurons exhibit goal-zone coding independent of reward location.
- The thalamic nucleus reuniens (NR) is a critical relay for mPFC-to-hippocampus communication: NR projects to CA1 but not CA2/CA3/DG; NR lesions or optogenetic silencing abolishes trajectory-dependent firing in CA1 place cells; CA3 (which lacks NR input) does not show such trajectory coding. This supports a mPFC→NR→CA1 circuit for prospective coding.
- The reverse pathway (CA1→mPFC, originating from intermediate and ventral CA1) is important for goal-location encoding: disrupting hippocampal–mPFC projections impairs the spatial working memory encoding phase (Spellman et al., 2015).
- Bat hippocampal CA1 neurons encode vectorial direction and distance to a goal location, suggesting goal-vector representations may be a general hippocampal computation (Sarel et al., 2017).

---

### Computational framework

The paper does not formalise an explicit computational model. However, the reviewed work is framed within **cognitive map** and **predictive/prospective coding** concepts:

- The hippocampus is treated as maintaining an allocentric spatial map (O'Keefe & Nadel, 1978) in which place cells serve as nodes.
- Prospective activity (theta sequences, trajectory-dependent firing, replay) is interpreted as the map being queried to simulate future states — consistent with model-based planning and successor-representation frameworks (referenced implicitly via Pfeiffer & Foster, 2013; Wikenheiser & Redish, 2015).
- The mPFC–NR–CA1 circuit is framed as a top-down control pathway that biases the hippocampal map toward goal-relevant future states, consistent with a prefrontal working-memory or goal-maintenance module modulating hippocampal sequence generation.
- No formal equations or algorithmic specification are given; the framework is conceptual rather than quantitative.

---

### Prevailing model of the system under study

Prior to the reviewed work, the dominant view was that the hippocampus autonomously implements a cognitive map: place cells and grid cells encode position, and replay during rest transfers hippocampal memories to neocortex. The mPFC was known to be important for working memory and flexible strategy, but its interaction with the hippocampus during active navigation was underspecified. The anatomical link from mPFC to hippocampus was recognised as indirect (via NR), but the functional importance of this pathway had not been established. The prevailing assumption was that prospective activity in the hippocampus — if it existed — was an intrinsic hippocampal process rather than a consequence of top-down prefrontal input.

---

### What this paper contributes

The review establishes that prospective, goal-directed coding in hippocampal place cells is not purely intrinsic but depends critically on top-down input from mPFC via the nucleus reuniens. The mPFC–NR–CA1 circuit is identified as the circuit substrate for trajectory-dependent future coding. Reciprocally, the CA1→mPFC pathway is important for encoding goal locations in prefrontal neurons. Taken together, the reviewed evidence reframes the hippocampus from a passive repository of spatial maps into an active participant in a prefrontal–thalamo–hippocampal loop that generates goal-directed prospective representations. The review also proposes that insights from spatial navigation may generalise to prefrontal–hippocampal interactions underlying non-spatial (conceptual) knowledge (citing Constantinescu et al., 2016).

---

### Brain regions & systems

- **Hippocampal CA1** — primary locus of place-cell prospective activity; receives mPFC input via NR; projects back to mPFC; shows trajectory-dependent and replay-associated firing.
- **Hippocampal CA3** — also has place cells but lacks NR input; does not show trajectory-dependent firing, used as a within-hippocampus control.
- **Medial entorhinal cortex (MEC)** — upstream of hippocampus; contains grid cells, head-direction cells, and speed cells that provide the metric spatial input to place cells.
- **Medial prefrontal cortex (mPFC)** — goal representation; flexible route planning; sends top-down input to hippocampus via NR; receives hippocampal input from ventral/intermediate CA1.
- **Nucleus reuniens (NR), thalamus** — critical relay from mPFC to CA1; lesions abolish trajectory-dependent place-cell firing; involved in spatial working memory and memory consolidation.
- **Ventromedial prefrontal cortex (vmPFC) / anterior cingulate cortex** — noted as possible direct route back to hippocampus (Rajasethupathy et al., 2015), though sparse.

---

### Mechanistic insight

The paper partially meets the mechanistic bar. It reviews neural data (lesion, inactivation, optogenetics, electrophysiology) that specifically link the mPFC–NR–CA1 circuit to trajectory-dependent prospective coding — not merely to some general spatial function. However, the review does not itself present a formalised algorithm; it synthesises others' findings. Mapped onto Marr's levels:

- **Computational**: The problem is goal-directed navigation — estimating future positions and planning routes to a remembered goal that lies outside current sensory range.
- **Algorithmic**: The hippocampal cognitive map is queried prospectively via place-cell sequences (replay, theta sequences, trajectory coding); goal-related future states are preferentially activated. The mPFC provides a top-down goal signal that biases which sequences are generated; the CA1→mPFC pathway encodes goal locations into prefrontal working memory.
- **Implementational**: The mPFC→NR→CA1 glutamatergic circuit is the anatomical substrate for top-down modulation. NR provides strong excitatory drive to CA1 (comparable to CA3 input). Optogenetic silencing of NR disrupts trajectory-dependent place-cell firing specifically in CA1 but not CA3. Sharp-wave ripples (SWRs) are the local field potential correlate of replay events; disrupting SWRs causally impairs navigation.

The paper does not address cell-type specificity within these circuits or the biophysical mechanisms by which NR inputs gate place-cell sequence generation.

---

### Limitations & open questions

- The review is almost entirely from rodent studies; human evidence is limited to lesion cases and indirect inferences.
- The mechanism by which mPFC signals are transformed into trajectory-specific place-cell activity in CA1 is not established — the circuit anatomy is known but the computation within NR is uncharacterised.
- Phase precession as a mechanism for future-state representation is questioned: two-dimensional data suggest phase precession reflects heading direction rather than planned future trajectory per se.
- It is unclear whether prospective place-cell sequences are primarily a cause of route decisions or a reflection of them.
- Whether goal-vector representations (as found in bats) exist in rodents or humans remains an open question.
- The review does not address how the system handles multi-step or hierarchical route planning, or how competing goals are prioritised.
- The generality of the mPFC–NR–CA1 framework to non-spatial (episodic, conceptual) memory remains speculative, though the author suggests it as a future direction.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Dostrovsky (1971) — discovery of place cells
- O'Keefe & Nadel (1978) — cognitive map theory
- Hafting et al. (2005) — discovery of grid cells
- Wood et al. (2000); Frank et al. (2000) — trajectory-dependent place-cell firing
- Pfeiffer & Foster (2013) — replay of future paths
- Jadhav et al. (2012) — causal role of SWRs in spatial memory
- Ito et al. (2015) — mPFC–NR–CA1 circuit for trajectory coding
- Spellman et al. (2015) — hippocampal–mPFC pathway for goal encoding
- Sarel et al. (2017) — goal-vector representation in bat hippocampus
- Buzsaki (2015) — sharp-wave ripple review

**Named models or frameworks**:
- Cognitive map (O'Keefe & Nadel)
- Theta phase precession
- Sharp-wave ripple (SWR)
- Replay / reverse replay
- Theta sequences
- mPFC–NR–CA1 circuit (prefrontal–thalamo–hippocampal circuit)

**Brain regions**:
- Hippocampal CA1, CA3
- Medial entorhinal cortex
- Medial prefrontal cortex (mPFC)
- Nucleus reuniens (NR), thalamus
- Ventral/intermediate CA1 (source of CA1→mPFC projection)

**Keywords**:
- spatial navigation, cognitive map, place cells, grid cells, prospective coding, trajectory-dependent firing, hippocampal replay, sharp-wave ripples, nucleus reuniens, prefrontal–hippocampal interactions, goal representation, theta sequences

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits|Prospective spatial coding in hippocampal–medial prefrontal circuits]]
