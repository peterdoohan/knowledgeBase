---
source_file: moser2008_place_cells_grid_cells.md
paper_id: moser2008_place_cells_grid_cells
title: "Place Cells, Grid Cells, and the Brain's Spatial Representation System"
authors:
  - "Edvard I. Moser"
  - "Emilio Kropff"
  - "May-Britt Moser"
year: 2008
journal: "Annual Review of Neuroscience"
paper_type: review
contribution_type: review
methods:
  - electrophysiology
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - lateral_entorhinal_cortex
  - striatum
  - retrosplenial_cortex
  - thalamus
frameworks:
  - attractor_networks
keywords:
  - place_cells
  - grid_cells
  - path_integration
  - continuous_attractor_network
  - oscillatory_interference
  - theta_phase_precession
  - sharp_wave_replay
  - pattern_completion_and_separation
  - spatial_map
  - entorhinal_hippocampal_circuit
  - cognitive_map
  - self_location
  - place
  - cells
  - grid
  - brains
  - spatial
  - representation
  - system
key_citations:
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/debates/grid_cells_as_a_mechanism_for_path_integration
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration
---

### One-line summary

This review synthesises three decades of research on hippocampal place cells and entorhinal grid cells to argue that these cell types form the core of a preconfigured, metric neural map for self-location, path integration, and spatial memory.

---

### Background & motivation

Understanding how the brain represents space and self-location has been a central question in systems neuroscience since O'Keefe & Dostrovsky's 1971 discovery of hippocampal place cells. The discovery of entorhinal grid cells in 2005 (Hafting et al.) radically expanded the picture, suggesting that the spatial map is not confined to the hippocampus but is part of a broader entorhinal-hippocampal circuit. This review integrates findings on place cells, grid cells, head-direction cells, path integration, sequence coding, and memory to assess how these components cooperate to produce a dynamic, internally updated representation of self-location and experience.

---

### Methods

This is a narrative review covering approximately 35 years of empirical and theoretical work. The authors synthesise:

- Single-unit electrophysiology studies in rodents recording place cells (hippocampal CA1/CA3) and grid cells (medial entorhinal cortex, MEC) during free exploration.
- Landmark manipulation, environment morphing, and sensory cue rotation experiments probing the control of spatial firing.
- Lesion and pharmacological studies (e.g., NMDA receptor blockade) testing synaptic plasticity requirements.
- Theoretical and computational models of grid field formation (attractor network models, oscillatory interference models).
- Sleep and awake replay studies using ensemble recordings.
- Developmental and comparative evidence bearing on the innate vs. experience-dependent origins of spatial maps.

---

### Key findings

- Place cells in hippocampal CA1/CA3 fire at single, spatially confined locations; the full population provides an allocentric map of the environment.
- Grid cells in MEC have periodic, triangular firing fields tiling the entire environment; grid spacing increases systematically from dorsomedial to ventrolateral MEC, mirroring hippocampal place-field size along the dorsoventral axis.
- Grid representations are primarily driven by path integration (self-motion signals): they persist after landmark removal and reset gradually with cumulative error corrected by sensory anchoring.
- Two main classes of grid formation models are evaluated: (1) recurrent attractor network models (Fuhs & Touretzky 2006; McNaughton et al. 2006), in which grids arise from population-level dynamics with toroidal topology; (2) oscillatory interference models (Burgess et al. 2007), in which grids emerge from interference between somatic and dendritic theta oscillators with speed-dependent frequency differences. The gradient of oscillation frequencies along the MEC dorsoventral axis (Giocomo et al. 2007) supports the interference account.
- Place fields can be formed by summing convergent grid-cell input across a range of spacings, equivalent to a Fourier-like basis function decomposition (Solstad et al. 2006; Rolls et al. 2006).
- Hippocampal attractor dynamics underlie pattern completion (stable firing after landmark removal) and pattern separation (remapping after environmental change); a sharp transition between square and circular environment representations supports discrete attractor states (Wills et al. 2005).
- Theta-phase precession in place cells and grid cells encodes sequences; compressed firing within theta cycles provides a candidate mechanism for spike-timing-dependent plasticity along routes.
- Sharp-wave reactivation during sleep and awake rest replays and reverse-replays behavioural sequences, implicating the hippocampus in memory consolidation and goal-directed planning.
- Forward "preplay" at choice points (Johnson & Redish 2007) suggests hippocampal networks are involved in prospective evaluation of possible trajectories.

---

### Computational framework

The review is organised around two complementary computational frameworks:

**Attractor network models**: The hippocampal/MEC network is modelled as a continuous attractor, where a stable "bump" of activity represents current position and is shifted by velocity inputs. Recurrent connections with Mexican-hat connectivity (excitation at short range, inhibition at intermediate range) produce grid-like population activity patterns. The McNaughton et al. (2006) variant proposes a toroidal attractor topology trained by an early-postnatal topographic tutor network. Key variables: firing rates of grid/place cells, synaptic weight matrices, gain of velocity inputs.

**Oscillatory interference models**: Grid fields arise from the interference of a somatic oscillator (theta frequency, ~8 Hz) with multiple dendritic oscillators whose frequencies are theta plus a term proportional to running speed projected onto preferred directions. The interference envelope integrates velocity into a planar wave; combining three or more such waves at 60° offsets produces the triangular grid. Key variables: intrinsic oscillation frequencies, running speed, heading direction.

Both frameworks assume that path integration is the primary driver of positional updating, with sensory landmarks serving to anchor and correct cumulative drift.

---

### Prevailing model of the system under study

Before the work reviewed here, the dominant view was that the hippocampus was the primary locus of spatial representation, acting as a cognitive map (O'Keefe & Nadel 1978). Place cells were thought to derive their spatial specificity largely from sensory inputs processed within the hippocampus itself, with the entorhinal cortex serving mainly as a relay. The mechanisms of place-field formation were debated between feedforward sensory-driven accounts and attractor-based intrinsic computation, but the entorhinal contribution was poorly characterised. Theta-phase precession was known but mechanistically unexplained. The relationship between spatial coding and episodic memory was theorised but not mapped onto specific circuit elements. The discovery of grid cells (Hafting et al. 2005) disrupted the hippocampus-centric picture and prompted a major reassessment of where metric computation occurs.

---

### What this paper contributes

This review establishes that spatial representation is distributed across an entorhinal-hippocampal circuit, not localised to the hippocampus alone. The key advances it synthesises are: (1) grid cells in MEC provide a metric, path-integration-based coordinate system that is upstream of — and may generate — hippocampal place fields; (2) two quantitatively distinct model classes (attractor networks and oscillatory interference) can in principle account for grid periodicity, and the review delineates their differing empirical predictions; (3) place cells perform both pattern completion and pattern separation via attractor dynamics, with dissociable contributions from CA3 and CA1; (4) theta sequences and sharp-wave replay implement a temporal coding scheme that links spatial navigation with episodic memory storage and retrieval; (5) hippocampal forward preplay at choice points points to a role in planning. Key open questions identified: developmental origins of grid structure; cellular mechanism of phase precession; modular vs. continuous organisation of the entorhinal map; functional role of the lateral entorhinal cortex; hippocampal-neocortical transfer during consolidation.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — primary locus of grid cells; layers II and III contain grid cells and conjunctive (grid × head-direction) cells; proposed site of the metric path integration map and, possibly, attractor dynamics underlying global remapping.
- **Hippocampus (CA1, CA3, dentate gyrus)** — place cells; CA3 is proposed as the primary attractor network for pattern completion and pattern separation; dentate gyrus facilitates orthogonalisation of inputs; CA1 is more sensitive to ongoing sensory input.
- **Presubiculum** — head-direction cells; projects to MEC layers III and V, contributing directional input to grid cells.
- **Anterior thalamus** — head-direction system, upstream of presubiculum.
- **Retrosplenial cortex** — path integration-based navigation; strong connections with MEC; lesion studies indicate necessity for topographic memory.
- **Lateral entorhinal cortex** — major cortical input to hippocampus; neurons apparently lack spatial modulation; function unknown.
- **Parietal cortex** — lesion studies implicate it in path-integration-based navigation; neurons encode navigational epochs on fixed routes.
- **Striatum** — action-based spatial computations; key positions along trajectories reflected in local activity.

---

### Mechanistic insight

The paper partially meets the bar. It synthesises substantial neural recording data (place cells, grid cells, theta-phase precession, sharp-wave replay) alongside formal algorithmic proposals (attractor models, oscillatory interference). However, as a review rather than a primary empirical study, it does not itself provide neural data that pit the two algorithmic accounts against each other at the level of single-unit recordings. The mechanistic picture is as follows:

- **Computational**: The brain maintains a continuously updated, metric representation of self-location to support navigation, memory encoding, and planning. The problem requires integrating velocity signals over time while anchoring the representation to environmental landmarks.
- **Algorithmic**: Path integration is implemented either via a continuous attractor network (velocity shifts a bump of population activity in an abstract toroidal space) or via interference between theta-frequency oscillators with speed-dependent detuning. Hippocampal pattern completion and separation exploit attractor states stored via Hebbian plasticity. Theta sequences compress temporally extended routes into spike-timing windows suitable for STDP.
- **Implementational**: Grid cells in MEC layers II/III express the coordinate system; conjunctive cells (grid × head-direction × speed) in layer III/V provide the velocity input to update it. Stellate cells in MEC layer II exhibit intrinsic oscillations consistent with the interference model. CA3 recurrent collaterals support attractor storage. The dentate gyrus mossy fibre synapses enable pattern separation. Dopamine-modulated reverse replay at reward may implement a form of eligibility-trace reinforcement.

**Note**: direct causal evidence linking specific algorithmic variables (e.g., the velocity gain signal in attractor models; specific oscillation frequencies in interference models) to measured neural activity is noted as outstanding — the review identifies these as future issues.

---

### Limitations & open questions

- The developmental origin of grid structure is unknown: it is unclear whether a preconfigured toroidal attractor is genetically specified or requires postnatal experience.
- The cellular mechanism and anatomical locus of theta-phase precession remain undetermined; intrinsic oscillation, ramp-excitation, and network-level models remain viable.
- The entorhinal map may be modular or continuous; current data cannot distinguish these, and the functional implications differ between the two model classes.
- Direct evidence for information transfer from hippocampus to neocortex during sleep consolidation is lacking; the direction of the coupling during sharp-wave/up-state interactions is unresolved.
- The function of the lateral entorhinal cortex in hippocampal processing is entirely unknown.
- How parietal and striatal spatial computations interact with the entorhinal-hippocampal map is unresolved.
- The review notes that most data come from rodents running in 2D arenas; generalisability to 3D navigation, primate systems, and human spatial memory remains to be fully established.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — cognitive map theory
- Hafting et al. (2005) — discovery of grid cells
- McNaughton et al. (2006) — toroidal attractor model of grid formation
- Fuhs & Touretzky (2006) — spin-glass/Mexican-hat attractor model
- Burgess et al. (2007) — oscillatory interference model
- Wills et al. (2005) — discrete attractor states in hippocampal morphing
- Giocomo et al. (2007) — gradient of intrinsic oscillation frequencies in MEC
- Solstad et al. (2006) — place fields from grid cell summation
- Foster & Wilson (2006) — reverse replay during awake rest
- Johnson & Redish (2007) — forward preplay at choice points

**Named models or frameworks**:
- O'Keefe & Nadel cognitive map
- Continuous attractor network (toroidal topology, McNaughton et al. 2006)
- Mexican-hat attractor network (Fuhs & Touretzky 2006)
- Oscillatory interference model (Burgess et al. 2007; O'Keefe & Recce 1993)
- Hopfield network (discrete attractor)
- Theta-phase precession
- Sharp-wave reactivation / replay

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Hippocampus (CA1, CA3, dentate gyrus)
- Presubiculum
- Anterior thalamus
- Retrosplenial cortex
- Lateral entorhinal cortex
- Parietal cortex
- Striatum

**Keywords**:
- place cells
- grid cells
- path integration
- continuous attractor network
- oscillatory interference
- theta-phase precession
- sharp-wave replay
- pattern completion and separation
- spatial map
- entorhinal-hippocampal circuit
- cognitive map
- self-location

### Related wiki pages
- [[wiki/debates/grid_cells_as_a_mechanism_for_path_integration|Grid cells as a mechanism for path integration]]
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration|Hippocampal–entorhinal cognitive maps: place cells, grid cells, and path integration]]
