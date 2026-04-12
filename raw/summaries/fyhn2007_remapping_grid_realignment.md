---
source_file: fyhn2007_remapping_grid_realignment.md
paper_id: fyhn2007_remapping_grid_realignment
title: "Hippocampal remapping and grid realignment in entorhinal cortex"
authors:
  - "Marianne Fyhn"
  - "Torkel Hafting"
  - "Alessandro Treves"
  - "May-Britt Moser"
  - "Edvard I. Moser"
year: 2007
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - foraging_task
methods:
  - tetrode_recording
brain_regions:
  - hippocampus
  - hippocampus_ca3
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - grid_cells
  - place_cells
  - hippocampal_remapping
  - global_remapping
  - rate_remapping
  - entorhinal_cortex
  - spatial_phase_structure
  - population_cross_correlation
  - path_integration
  - pattern_separation
  - attractor_network
  - cognitive_map
  - hippocampal
  - remapping
  - grid
  - realignment
  - entorhinal
  - cortex
---

### One-line summary

During hippocampal global remapping, ensembles of medial entorhinal grid cells undergo a coherent coordinate shift (realignment) while preserving their internal spatial phase structure, whereas rate remapping in the hippocampus is accompanied by no change in grid cell alignment.

---

### Background & motivation

Hippocampal place cells can represent the same environment with statistically independent codes across different contexts ("global remapping") or modulate firing rates while preserving spatial locations ("rate remapping"). The medial entorhinal cortex (MEC) provides the major spatial input to the hippocampus via grid cells, which tile space with a periodic triangular lattice. It was unclear how the two distinct modes of hippocampal remapping relate to upstream dynamics in MEC grid cell ensembles, and whether grid cells themselves maintain a fixed metric framework across environments. This paper addresses that gap by simultaneously recording from MEC and hippocampal CA3 under controlled remapping conditions.

---

### Methods

- **Subjects**: 19 Long-Evans rats implanted with tetrode microdrives targeting dorsocaudal MEC and/or dorsal hippocampal CA3.
- **Task design**:
  - *Global remapping protocol 1*: Alternation between a square and a circular enclosure in the same room location.
  - *Global remapping protocol 2*: Foraging in similar square boxes in two different rooms with distinct distal cues.
  - *Global remapping protocol 3*: Alternation between light and dark sessions in the same enclosure.
  - *Rate remapping protocol*: Wall colour reversal in a square box (three black + one white vs. one black + three white).
- **Simultaneous recordings**: 5 out of 15 MEC rats also had CA3 electrodes; 21 experiments with ≥5 simultaneously recorded grid cells.
- **Analysis**: Spatial cross-correlation of rate maps for individual cells and population vectors; cross-correlograms computed by 5 cm spatial shifts (and 3° rotation steps for inter-room comparisons); Shannon mutual information of temporal population vectors (150 ms bins); Wilcoxon signed-ranks test and Rayleigh test for statistical comparisons.

---

### Key findings

- **Global remapping is accompanied by grid realignment**: When hippocampal CA3 place cells underwent global remapping (different enclosure shapes or different rooms), population cross-correlograms of MEC grid cell ensembles showed a coherent spatial offset from the origin.
  - Square-vs-circle protocol: displacement 10.0–23.8 cm across experiments (significantly larger than within-box repeats of 0.1–2.3 cm; Z = 2.4, P < 0.01); offset direction uniformly distributed.
  - Two-rooms protocol: grid displacement 5.7–27.5 cm after optimal rotation (66° CW to 78° CCW); significantly larger than same-room repeats (Z = 2.5, P < 0.01).
- **Intrinsic spatial phase structure is preserved during realignment**: Despite the coordinate shift, the triangular lattice structure, spacing, and relative phases among co-recorded grid cells remained intact across environments — the ensemble realigns as a rigid unit.
- **Rate remapping is not accompanied by grid realignment**: During colour-reversal rate remapping, grid cross-correlogram peaks remained at the origin in 6 of 7 experiments (displacement 0–2.7 cm), indistinguishable from same-colour repeat sessions (Z = 1.4, P > 0.05).
- **CA3 population vectors are orthogonalised during global remapping**: Shannon mutual information between trial type and temporal population vectors was significantly above baseline in CA3 (square vs. circle: t(7) = 5.6, P < 0.001; two rooms: t(4) = 3.8, P < 0.01) but not in MEC, consistent with pattern separation downstream of the grid representation.
- **Temporal coincidence of grid realignment and hippocampal remapping**: In a light/dark switching paradigm, turning on lights caused simultaneous global remapping in CA3 and coherent realignment in MEC, supporting a mechanistic link between the two phenomena.
- **No rate changes in grid fields during rate remapping**: Individual grid field firing rates were not significantly modulated by the colour-reversal manipulation that drove rate remapping in CA3.

---

### Computational framework

The paper is grounded in the framework of **pattern separation via attractor networks and path integration**. Grid cells are conceptualised as implementing a universal, path-integration-based metric for space: the MEC ensemble encodes position through a fixed phase-offset structure that is translated coherently as the animal moves. This is consistent with continuous attractor network models in which local coupling among MEC neurons enforces a rigid phase structure. The key variables are the spatial phases (firing vertex positions) of individual grid cells and the population cross-correlation vector capturing ensemble-level displacement. The framework assumes: (1) the internal phase relationships within a grid ensemble are fixed by network connectivity; (2) different environments trigger different "read-in" states of the grid attractor, shifting all cells coherently; (3) the hippocampus receives this shifted input and performs further decorrelation (pattern separation) to produce orthogonal place codes.

---

### Prevailing model of the system under study

Prior to this paper, it was established that hippocampal place cells can remap in at least two modes — global remapping (independent place and rate changes) and rate remapping (stable place fields, modulated rates) — and that these modes can be experimentally dissociated (Leutgeb et al., 2005). The MEC had been identified as housing grid cells with a periodic spatial code (Hafting et al., 2005), and MEC was understood to be one synapse upstream of hippocampus and a likely source of the hippocampal spatial signal. However, it was not known whether grid cells themselves remap across environments, whether their ensemble structure is rigid or flexible, or how the mode of hippocampal remapping relates to activity patterns in the entorhinal input. The implicit assumption was that grid cells might represent individual environments differently (analogous to place cells), but this had not been tested.

---

### What this paper contributes

This paper establishes that, unlike hippocampal place cells, local ensembles of MEC grid cells do not form environment-specific representations. Instead, the grid network maintains a single, universal metric framework that is rigidly translated (and sometimes rotated or slightly rescaled) when the animal enters a new environment. The paper further dissociates the two modes of hippocampal remapping at the level of their entorhinal input: global remapping requires a shift in the entorhinal coordinate frame, whereas rate remapping does not. This places the origin of rate orthogonalization downstream of MEC, in the dentate gyrus or CA3. It also provides the first evidence for temporal coincidence of entorhinal grid realignment and hippocampal global remapping, suggesting these are part of a single integrated process rather than independent phenomena.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC), layer II** — locus of grid cell recordings; site of the universal spatial metric that realigns coherently during global remapping.
- **Hippocampal area CA3** — simultaneously recorded in a subset of rats; displays global or rate remapping depending on condition; population vectors become orthogonalised (flat cross-correlograms) relative to MEC during global remapping.
- **Dentate gyrus** (referenced, not directly recorded) — proposed locus of rate orthogonalization based on convergence of MEC spatial and lateral entorhinal nonspatial inputs.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight.

**Phenomenon**: Hippocampal global remapping is correlated with a coherent rigid translation (and sometimes rotation) of the MEC grid ensemble, while the internal phase structure is preserved. Rate remapping is not accompanied by any grid shift.

- **Computational level**: The brain solves the problem of representing location in multiple distinct contexts while maintaining a single, updateable metric for path integration. The MEC provides a universal spatial coordinate system; the hippocampus maps this onto context-specific codes.
- **Algorithmic level**: The MEC grid ensemble operates as a rigid attractor state in which all cells shift together, preserving pairwise phase offsets. The transition between attractor states (environments) involves a coherent displacement vector applied to the entire ensemble. Pattern separation from MEC input to CA3 involves decorrelation of the shifted grid input, producing statistically independent hippocampal representations. Rate remapping, by contrast, originates downstream without any change in the grid coordinate frame.
- **Implementational level**: The paper does not directly address specific cell types, connectivity motifs, or neuromodulators. The recordings are from layer II MEC grid cells and CA3 pyramidal cells, but the biophysical or circuit mechanisms that enforce rigid phase coupling or that trigger coordinate shifts are not investigated.

**Bonus**: The paper does not address implementational mechanisms in terms of cell types or synaptic physiology, so the third Marr level remains unaddressed.

---

### Limitations & open questions

- Recordings are from a small number of simultaneously recorded cells (≥5 grid cells per experiment) in the dorsocaudal MEC; it is unknown whether the same coherence holds across the full dorsoventral extent of MEC with its varying grid scales.
- The paper does not identify what triggers the coordinate shift — whether it is driven by sensory input, self-motion signals, or a combination. The light/dark experiment suggests sensory context can reset the grid, but the mechanism is not characterised.
- The relationship between grid realignment and place cell remapping is correlational; the causal direction is not established (does grid realignment drive hippocampal remapping, or vice versa, or are both driven by a common input?).
- Rate remapping in hippocampus is not accompanied by rate changes in individual grid fields, and the source of rate orthogonalization is inferred to be dentate gyrus or CA3, but this is not directly tested here (Leutgeb et al., 2007, cited as in press).
- Small sample sizes in some conditions (e.g., the light/dark coincidence experiment used only two rats with hippocampal electrodes).
- The computational model connecting grid ensemble dynamics to hippocampal pattern separation is speculative and not formally developed in this paper.

---

### Connections & keywords

**Key citations**:
- Hafting et al. (2005), Nature — discovery of grid cells in MEC
- Leutgeb et al. (2005), Science — global vs. rate remapping dissociation
- Leutgeb et al. (2004), Science — distinct ensemble codes in CA3 and CA1
- Fyhn et al. (2004), Science — spatial representation in entorhinal cortex
- McNaughton et al. (2006), Nature Reviews Neuroscience — path integration and cognitive map
- Marr (1971) — archicortex memory theory (pattern separation motivation)
- Battaglia & Treves (1998) — attractor networks storing multiple space representations

**Named models or frameworks**:
- Global remapping / rate remapping (Leutgeb et al., 2005)
- Path integration model of grid cells
- Continuous attractor network (implicit framework)
- Pattern separation (Marr 1971; Treves & Rolls 1992)

**Brain regions**:
- Medial entorhinal cortex (MEC), layer II
- Hippocampal area CA3
- Dentate gyrus

**Keywords**:
- grid cells
- place cells
- hippocampal remapping
- global remapping
- rate remapping
- entorhinal cortex
- spatial phase structure
- population cross-correlation
- path integration
- pattern separation
- attractor network
- cognitive map
