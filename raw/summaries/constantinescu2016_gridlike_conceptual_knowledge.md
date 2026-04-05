---
source_file: constantinescu2016_gridlike_conceptual_knowledge.md
title: "Organizing conceptual knowledge in humans with a gridlike code"
authors: Alexandra O. Constantinescu, Jill X. O'Reilly, Timothy E. J. Behrens
year: 2016
journal: Science
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Humans navigating a two-dimensional abstract conceptual space (defined by bird morphology features) exhibit the same hexagonally symmetric fMRI signal as during spatial navigation, localised to entorhinal cortex and ventromedial prefrontal cortex, suggesting grid-cell-like codes organise non-spatial conceptual knowledge.

---

### Background & motivation

Grid cells in the entorhinal cortex use a hexagonally symmetric firing pattern to represent spatial location and are the likely neural source of a precise sixfold (hexagonal) periodicity in the fMRI BOLD signal measured during virtual navigation. It has long been hypothesised — from Tolman's cognitive map onward — that the brain organises conceptual knowledge using map-like structures analogous to spatial maps. Prior work had shown that brain regions hosting grid cells (entorhinal, medial prefrontal, medial parietal, lateral temporal cortices) are also active during non-spatial tasks involving conceptual generalisation, imagination, and memory, raising the question of whether a common neural code underlies both spatial and conceptual representation. This paper directly tests whether the hexagonal grid signal, previously validated as a proxy for grid-cell activity, extends to abstract conceptual space.

---

### Methods

- **Subjects**: 28 healthy adults; 2–4 fMRI sessions each, across two days separated by at least one week.
- **Task design**: Participants first trained extensively (over two days) to associate bird stimuli — varying continuously along two dimensions (neck length and leg length) — with Christmas-symbol outcomes, without being told the stimuli formed a 2D "bird space." Training involved free morphing to find outcomes and ballistic recall tasks.
- **fMRI paradigm**: During scanning, participants watched a bird morph along a trajectory in the 2D conceptual space and imagined the outcome if morphing continued. On some trials they chose among three options (two trained outcomes plus a null). Trajectory direction θ was defined by the neck:legs ratio of change.
- **Hexagonal symmetry analysis**: The BOLD signal was regressed on sin(6θ) and cos(6θ) to detect sixfold (hexagonal) modulation. Confounds (visual properties of stimuli, accuracy, presence of outcomes) were verified to share <5% variance with these regressors.
- **Grid angle consistency**: Grid orientation φ estimated from one session was used to generate an aligned/misaligned regressor [cos(6(θ−φ))] for a separate session, cross-validated and counterbalanced, testing consistency within-day (~30 min apart) and across days (>1 week apart).
- **Control periodicities**: Four-, five-, seven-, and eightfold symmetries were used as controls to confirm specificity of the sixfold effect.
- **ROIs**: Whole-brain cluster-corrected maps were used to define unbiased ROIs; analyses focused on vmPFC and entorhinal cortex (ERH), where human grid cells have been directly recorded.

---

### Key findings

- A significant hexagonally symmetric (sixfold) fMRI signal was found across a network including vmPFC (peak Z = 4.09), medial entorhinal cortex (ERH; Z = 4.41), OFC (Z = 4.27), posterior cingulate (Z = 4.30), retrosplenial cortex (Z = 4.73), lateral parietal cortex (Z = 4.96), and TPJ (Z = 4.13) — anatomically overlapping with both the spatial navigation network and the default mode network.
- vmPFC hexagonal signal correlated positively with task performance (r = 0.432, P = 0.039).
- Grid angle was consistent across sessions acquired ~30 min apart in vmPFC (t26 = 2.61, P < 0.05) and ERH (t27 = 2.36, P < 0.05); within-session consistency also correlated with task accuracy (r = 0.431, P = 0.039).
- Grid angle was consistent across sessions acquired more than a week apart in vmPFC (t20 = 3.65, P < 0.01).
- Cross-region consistency: grid angle in ERH and vmPFC were aligned to the same orientation (t21 = 2.18, P < 0.05), suggesting the two regions share a common grid reference frame.
- None of these effects were present for control (four-, five-, seven-, or eightfold) periodicities (all P > 0.15).
- Participants were unaware of the 2D spatial structure of the bird space (0/28 reported conceiving of it as a spatial map), indicating the grid signal does not require explicit spatial awareness.
- The hexagonal signal during conceptual navigation overlapped strongly with the brain network activated during virtual spatial navigation, despite profound differences in perceptual and cognitive demands.

---

### Computational framework

The paper does not develop a new computational model but is framed around the **cognitive map** hypothesis and the established grid-cell formalism.

The key formalism exploits the fact that grid cells across a population share a common grid axis (orientation) and that conjunctive grid cells fire more when movement is aligned to that axis. This predicts that bulk fMRI activity will be modulated as cos(6(θ−φ)), i.e. with sixfold periodicity as a function of movement direction θ, where φ is the population-level grid orientation. The authors apply this as a model-based fMRI regressor, treating the hexagonally modulated BOLD signal as a proxy readout of grid-cell-like activity. The framework assumes (a) a shared grid axis across cells in a region, (b) that this axis is stable over time (hence testable cross-session), and (c) that the same mechanism generalises from physical to abstract 2D spaces.

---

### Prevailing model of the system under study

Prior to this paper, grid cells were understood primarily as spatial navigation cells: they fire in a hexagonally arranged pattern across the environment, tiling 2D physical space, and are found in entorhinal cortex and surrounding medial temporal lobe structures. The prevailing view, grounded in rodent electrophysiology, was that grid cells are a core component of a path-integration and spatial mapping system. Human fMRI work had confirmed a hexagonally symmetric BOLD signal during virtual spatial navigation (Doeller et al., 2010; Kunz et al., 2015), plausibly reflecting grid-cell population activity. The theoretical extension — that grid cells or analogous codes might organise non-spatial, conceptual knowledge — was an established hypothesis (Tolman, 1948; O'Keefe & Nadel, 1978; Buzsáki & Moser, 2013; Eichenbaum & Cohen, 2014), but direct empirical evidence in humans was lacking. The default mode network regions overlapping with the grid-cell network were known to be active during conceptual tasks, but no study had demonstrated that the precise hexagonal signature — rather than just broad regional overlap — extended to abstract conceptual spaces.

---

### What this paper contributes

This paper provides the first direct empirical evidence that the hexagonally symmetric grid-cell-like fMRI signal extends beyond physical space to abstract conceptual representations in humans. The finding establishes that:

1. The grid code is not spatially exclusive — it generalises to at least one type of continuous 2D abstract knowledge space.
2. The same brain regions (vmPFC, ERH) that carry this signal during spatial navigation carry it during purely conceptual navigation, and the signal is stable for over a week.
3. The strength of the gridlike signal correlates with behavioural performance, linking the neural measure to function rather than mere presence.
4. The grid orientation is shared between ERH and vmPFC, suggesting a coordinated, network-level representational geometry for conceptual space.

Before this paper, it could only be speculated that a gridlike code might support conceptual knowledge; this paper elevates that from theoretical hypothesis to experimental finding, while acknowledging that the coarse fMRI signal cannot confirm single-neuron grid firing in conceptual domains.

---

### Brain regions & systems

- **Ventromedial prefrontal cortex (vmPFC)** — primary locus of the conceptual hexagonal signal; strength correlates with task performance and grid angle is stable across sessions and weeks; also the region with strongest cross-session consistency.
- **Medial entorhinal cortex (ERH)** — shows hexagonal signal consistent with grid-cell activity; grid angle aligns with vmPFC, suggesting shared reference frame; known locus of human grid cells from direct recordings.
- **Orbitofrontal cortex (OFC)** — part of the hexagonally modulated network.
- **Posterior cingulate cortex (PCC)** — part of the network; belongs to default mode network.
- **Retrosplenial cortex (RSC)** — highest peak Z score in whole-brain map (Z = 4.73); part of spatial/conceptual navigation network.
- **Lateral parietal cortex (LPC)** — hexagonally modulated (Z = 4.96); also part of default mode network.
- **Temporoparietal junction (TPJ)** — hexagonally modulated (Z = 4.13); default mode network region active in theory of mind and conceptual tasks.

The network overlaps substantially with both the human spatial navigation network (replicating Doeller et al. 2010) and the default mode network.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the algorithmic and computational levels, but only partially at the implementational level.

**Computational**: The brain solves the problem of representing structured relational knowledge — specifically, the positions and trajectories within a continuous 2D conceptual space — in a way that supports flexible generalisation to novel situations. The grid code provides a metric geometry over this space, enabling efficient inference about relationships between concepts.

**Algorithmic**: The representation uses a hexagonally symmetric basis, with population-level activity modulated by the direction of traversal through the conceptual space. The grid orientation (φ) is a stable feature of the representation for a given individual, shared across brain regions and sessions, consistent with the grid-cell population sharing a common axis. The regressor cos(6(θ−φ)) captures the alignment effect: fMRI signal is higher when conceptual trajectory direction aligns with the grid axis.

**Implementational**: The paper provides fMRI evidence (not single-unit recordings) and notes that human intraoperative recordings (Jacobs et al., 2013) have previously confirmed gridlike firing in entorhinal and frontal regions during spatial tasks. There is no direct implementational evidence for conceptual grid cells specifically (e.g., cell-type identification, laminar specificity, connectivity). The authors explicitly note that the coarse BOLD signal urges caution at the level of neuronal codes.

The paper therefore provides strong computational and algorithmic evidence, with the implementational level inferred from the known biology of grid cells rather than directly demonstrated in the conceptual domain.

---

### Limitations & open questions

- The fMRI BOLD signal is a coarse measure; it cannot confirm that individual neurons exhibit grid-like firing during conceptual processing — this requires direct recordings.
- The task uses a two-dimensional, continuous conceptual space (bird morphology). It is unknown whether gridlike codes apply to conceptual problems that are not naturally two-dimensional or continuous, or to higher-dimensional conceptual spaces.
- Participants were unaware of the 2D structure, but it remains unclear whether the gridlike code reflects subconscious remapping of conceptual dimensions onto pre-existing spatial maps, or whether a genuinely new conceptual organisation emerges.
- The cross-region ERH–vmPFC alignment is suggestive of a shared grid frame, but the causal direction (which region drives alignment) is not established.
- The study does not address whether the conceptual grid cells (if they exist) share phase relationships with spatial grid cells — which would illuminate whether the same cells or circuits are reused.
- The relationship between the hexagonal signal and the speed or trajectory of learning (as opposed to current performance) was tested but null, leaving open how the map is initially formed.
- Generalisability to non-visual, non-morphological conceptual spaces (e.g., social, temporal, or semantic dimensions) remains to be tested.

---

### Connections & keywords

**Key citations**:
- Tolman (1948) — cognitive map hypothesis
- O'Keefe & Nadel (1978) — hippocampus as cognitive map
- Hafting et al. (2005) — discovery of grid cells (Nature)
- Doeller, Barry & Burgess (2010) — fMRI hexagonal signal in virtual spatial navigation (Nature)
- Jacobs et al. (2013) — human intraoperative grid-cell recordings (Nature Neuroscience)
- Kunz et al. (2015) — hexagonal fMRI signal and spatial memory (Science)
- Buzsáki & Moser (2013); Eichenbaum & Cohen (2014) — theoretical frameworks for cognitive map generalisation
- Kumaran et al. (2009); Barron, Dolan & Behrens (2013) — vmPFC role in conceptual generalisation

**Named models or frameworks**:
- Cognitive map (Tolman)
- Grid cell hexagonal symmetry model / fMRI hexagonal signal proxy (Doeller et al. 2010)
- Default mode network (Fox & Raichle 2007)

**Brain regions**:
- Ventromedial prefrontal cortex (vmPFC)
- Medial entorhinal cortex (ERH)
- Orbitofrontal cortex (OFC)
- Posterior cingulate cortex (PCC)
- Retrosplenial cortex (RSC)
- Lateral parietal cortex (LPC)
- Temporoparietal junction (TPJ)

**Keywords**:
- grid cells
- cognitive map
- conceptual knowledge representation
- hexagonal symmetry
- entorhinal cortex
- ventromedial prefrontal cortex
- fMRI
- abstract space navigation
- default mode network
- relational coding
- generalisation
- path integration
