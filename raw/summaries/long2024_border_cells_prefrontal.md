---
source_file: "long2024_border_cells_prefrontal.md"
paper_id: "long2024_border_cells_prefrontal"
title: "Border cells without theta rhythmicity in the medial prefrontal cortex"
authors: "Xiaoyang Long, Bin Deng, Rui Shen, Lin Yang, Liping Chen, Qingxia Ran, Xin Du, Sheng-Jia Zhang"
year: 2024
journal: "PNAS (Proceedings of the National Academy of Sciences)"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["virtual_navigation", "foraging_task", "navigation_task"]
methods: ["electrophysiology", "tetrode_recording"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "medial_entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "anterior_cingulate_cortex", "infralimbic_cortex"]
keywords: ["border", "cells", "without", "theta", "rhythmicity", "medial", "prefrontal", "cortex"]
key_citations: ["zielinski2019_theta_hippocampus_prefrontal", "sauer2022_prefrontal_spatial_representation"]
---

### One-line summary

Border-tuned neurons — firing preferentially near environmental boundaries — exist in the medial prefrontal cortex of freely foraging rats, exhibiting both allocentric and egocentric tuning but almost no theta rhythmicity, suggesting a spatially specific mPFC computation that is largely independent of hippocampal theta entrainment.

---

### Background & motivation

The medial prefrontal cortex (mPFC) is implicated in higher cognitive functions including spatial navigation, working memory, and goal-directed behaviour, yet its role in encoding spatial information during unconstrained, task-free foraging was unclear. Prior studies failed to find place-cell-like activity in mPFC during free exploration, and spatially tuned responses had only been reliably observed during explicit cognitive tasks. A key open question was whether mPFC contributes to online spatial coding independent of task demands, and whether such coding is entrained by hippocampal theta oscillations as is commonly assumed for hippocampal–prefrontal interactions.

---

### Methods

- **Subjects**: 10 male Long-Evans adult rats implanted with microdrives carrying four tetrodes targeting prelimbic (PrL) and infralimbic (IL) cortices of mPFC.
- **Recording paradigm**: Chronic single-unit extracellular recordings during free foraging in a 1 × 1 m open square arena with 50 cm walls.
- **Unit isolation**: 983 well-isolated single units recovered; classified as putative pyramidal (regular-spiking) or fast-spiking interneurons based on firing rate and spike waveform width.
- **Border cell classification**: Border score and spatial stability both required to exceed the 99th percentile of shuffled distributions; threshold border score = 0.58.
- **Egocentric/allocentric classification**: CW vs. CCW firing rate ratio used to assign border cells to allocentric (ratio 0.5–2), left egocentric (ratio > 2), or right egocentric (ratio < 0.5) categories; confirmed with egocentric boundary ratemaps (EBRs).
- **Stability tests**: Sequential recordings in light/darkness/light, whisker trimming, square vs. circular arenas, familiar vs. novel rooms, and environments with/without physical walls (elevated platform).
- **Insert experiments**: A discrete wall insert added to the arena to test whether border responses generalise to new boundaries.
- **Theta rhythmicity**: Theta rhythmicity index (TRI) computed from spike-train autocorrelograms; compared between border and nonborder cells.

---

### Key findings

- 110 of 983 units (11.19%) qualified as border cells — significantly above chance (Z = 32.11, p < 0.001).
- The overwhelming majority (90.91%, 100/110) of mPFC border cells fired along all four walls, in contrast to MEC border cells, of which 75.36% fire along only a single wall.
- Border cells subdivided into allocentric (46.36%), right egocentric (35.45%), and left egocentric (18.18%) subtypes.
- Clear hemispheric lateralisation: 100% of right egocentric border cells were recorded from the left hemisphere; egocentric tuning direction was contralateral to the recording hemisphere.
- Border firing was stable across light and darkness (no significant change in firing rate or border score), across different room contexts (familiar vs. novel), and across environment geometries (square vs. circle).
- Inserting a wall into the open arena evoked new border-tuned firing fields along the insert, with direction tuning that mirrored the egocentric/allocentric classification.
- Responses were also observed around small objects placed in the arena, with CW/CCW ratio reversed relative to wall-evoked responses — consistent with egocentric coding.
- Border score was significantly reduced on an elevated platform without physical walls, confirming responses require physical boundaries (not merely somatosensory cues from proximity).
- Only 3/110 (2.73%) of border cells were theta-rhythmic, comparable to 5.15% of nonborder cells (chi-squared, p = 0.27); mean TRI did not differ between groups (Mann-Whitney U, p = 0.30).

---

### Computational framework

Not applicable in a formal sense — the paper is descriptive/empirical and does not implement a computational model. However, the results are discussed in terms of **egocentric-to-allocentric coordinate transformation**: computational models have predicted that neurons sensitive to boundaries in egocentric coordinates could enable integration of egocentric and allocentric representations for spatial memory and navigation. The coexistence of both reference frames within mPFC is interpreted as supporting local coordinate transformation for context-dependent behaviour.

The border score metric and egocentric boundary ratemap (EBR) methods are quantitative tools adapted from prior work on MEC and retrosplenial cortex, using polar-coordinate firing maps anchored to the animal's head direction.

---

### Prevailing model of the system under study

Prior to this paper, the dominant view was that the mPFC's spatial role was restricted to task-dependent or memory-guided contexts: it encodes goal locations, task rules, and spatial working memory through theta-coherent coupling with the hippocampus, but does not support online, naturalistic spatial coding in free exploration. Earlier recording studies found no place-cell-like spatial tuning in mPFC during free foraging. The hippocampal–entorhinal system (place cells, grid cells, border cells in MEC/subiculum) was considered the primary substrate for geometric boundary coding, with mPFC as a downstream recipient that transforms these signals for executive control. Theta oscillations were understood as a key carrier of hippocampal–prefrontal communication during spatial tasks.

---

### What this paper contributes

This paper establishes that the mPFC contains a genuine class of border-tuned neurons active during spontaneous, unconstrained locomotion — not merely during task demands. Several specific updates to the prevailing model:

1. **Spatial coding in mPFC is not task-gated**: border representations persist in free foraging, novel environments, darkness, and altered geometries without any task instruction.
2. **mPFC border cells differ qualitatively from MEC**: the near-universal four-wall firing pattern (vs. MEC's predominantly single-wall tuning) suggests a distinct, possibly more integrated or higher-order form of boundary representation.
3. **Both reference frames coexist within mPFC**: allocentric and egocentric border cells are intermingled, pointing to mPFC as a site of coordinate transformation rather than purely allocentric encoding.
4. **Theta-independence during spontaneous behaviour**: near-absent theta rhythmicity indicates that mPFC spatial coding during free exploration is largely decoupled from hippocampal theta, challenging the assumption that hippocampal–prefrontal spatial interaction is always theta-mediated.
5. **Physical boundary dependence**: the requirement for physical walls (not drop edges) distinguishes mPFC border cells from subicular boundary vector cells, implying a distinct computational niche or sensory input pathway.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC) — prelimbic (PrL) and infralimbic (IL) cortices**: primary locus of investigation; site of border cell recordings, predominantly from deep layer V/VI.
- **Medial entorhinal cortex (MEC)**: key comparator; classical source of border cells, head direction cells, and grid cells; provides direct input to mPFC via deep layers.
- **Hippocampus (ventral CA1, subiculum)**: provides direct projections to mPFC; source of theta oscillations implicated in hippocampal–prefrontal communication during spatial tasks.
- **Anterior cingulate cortex (ACC)**: mentioned as reciprocally connected with mPFC; prior work identified annulus cells (periphery-preferring) in ACC, contextualising mPFC border findings.
- **Subiculum**: mentioned as another locus of boundary vector cells, compared against mPFC findings.

---

### Mechanistic insight

The paper meets neither criterion for full mechanistic insight at Marr's algorithmic level. It characterises what mPFC border cells do (phenomenology) but does not formalise an algorithm, and it does not provide causal evidence linking specific inputs (e.g., MEC or hippocampal projections) to border tuning in mPFC.

The paper is primarily a characterisation study: it identifies a new cell type, classifies its tuning properties, and tests its stability across conditions. The near absence of theta rhythmicity is consistent with — but does not mechanistically demonstrate — independence from hippocampal theta entrainment. The authors acknowledge that optogenetic manipulation of the hippocampal–prefrontal pathway would be needed to establish causal relationships.

---

### Limitations & open questions

- Recordings were confined to deep layer V/VI of ventral mPFC (PrL/IL); layer II/III and dorsal mPFC (ACC) remain uncharacterised for border tuning during free foraging.
- The large asymmetry in sampling between hemispheres (91 border-proximal cells from left, 19 from right) makes the 100% contralateral lateralisation of right egocentric cells difficult to interpret unambiguously.
- The paper does not resolve the source of egocentric signals in mPFC — whether derived from somatosensory, visual, vestibular, or hippocampal inputs.
- Causal sufficiency of mPFC border cell activity for spatial behaviour is not demonstrated; recordings are correlational.
- Theta-independence during free foraging leaves open whether theta modulation emerges specifically during memory-guided tasks or spatial working memory (as suggested by prior literature), and what switches this on.
- Only male rats were used; sex differences in mPFC spatial coding are not addressed.
- The relationship between mPFC border cells and downstream or upstream circuits (thalamus, BLA, claustrum) is not explored.

---

### Connections & keywords

**Key citations**:
- Solstad et al. (2008) *Science* — border cells in MEC
- Lever et al. (2009) *J. Neurosci.* — boundary vector cells in subiculum
- Boccara et al. (2010) *Nat. Neurosci.* — grid/border cells in pre- and parasubiculum
- Hafting et al. (2005) *Nature* — grid cells in entorhinal cortex
- Zielinski et al. (2019) *J. Neurosci.* — coherent spatial coding via theta in hippocampus and mPFC
- Sauer et al. (2022) *PNAS* — topographic spatial representation in mPFC during virtual navigation
- Alexander et al. (2020) *Sci. Adv.* — egocentric boundary vector tuning in retrosplenial cortex
- Hinman et al. (2019) *Nat. Commun.* — egocentric environmental boundary representation
- Weible et al. (2012) *J. Neurosci.* — annulus cells in ACC

**Named models or frameworks**:
- Border score (adapted from MEC/subiculum literature)
- Egocentric boundary ratemaps (EBRs)
- Theta rhythmicity index (TRI)

**Brain regions**:
- Medial prefrontal cortex (mPFC), prelimbic cortex, infralimbic cortex
- Medial entorhinal cortex (MEC)
- Hippocampus (ventral CA1, subiculum)
- Anterior cingulate cortex (ACC)

**Keywords**:
- border cells, boundary representation, medial prefrontal cortex, spatial navigation, allocentric coding, egocentric coding, theta rhythmicity, hippocampal–prefrontal interaction, coordinate transformation, free foraging, extracellular recording, spatial tuning
