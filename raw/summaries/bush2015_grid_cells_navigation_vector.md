---
source_file: "bush2015_grid_cells_navigation_vector.md"
paper_id: "bush2015_grid_cells_navigation_vector"
title: "Using Grid Cells for Navigation"
authors: "Daniel Bush, Caswell Barry, Daniel Manson, Neil Burgess"
year: 2015
journal: "Neuron"
paper_type: "computational"
contribution_type: "theoretical"
brain_regions: ["hippocampus", "entorhinal_cortex", "medial_entorhinal_cortex"]
frameworks: ["attractor_networks"]
keywords: ["grid", "cells", "navigation"]
key_citations: ["fiete2008_grid_cells_position"]
---

### One-line summary

Grid cells can support large-scale vector navigation by encoding the displacement between arbitrary start and goal locations via the phase differences of their periodic firing patterns across modules, and this paper formalises the algorithmic solution and proposes several neural network implementations.

---

### Background & motivation

Mammals can navigate directly to hidden goal locations via novel routes — a capacity termed vector navigation — that requires an internal, context-independent representation of space rather than learned routes or sensory cues. Hippocampal lesions abolish this ability, implicating the hippocampal formation as the neural substrate. Prior models of vector navigation centred on place cells, but place cell representations lack a consistent spatial structure across environments and are limited in range, making them unsuitable for large-scale, context-independent navigation. Grid cells, with their regular hexagonal firing patterns that are conserved across environments and whose scales span a wide range, are better positioned to provide such a metric, but how the vector between two grid-coded locations could actually be computed remained unclear.

---

### Methods

- **Paper type**: Computational/modelling viewpoint (no new empirical data collected).
- **Algorithmic analysis**: The vector navigation problem is formalised at Marr's three levels. The computational problem is stated in 1D and 2D: given the grid cell phase representations of two locations, recover the displacement vector between them.
- **Fourier shift theorem insight**: The solution is derived by noting that phase differences across modules of different scales correspond to a residue number system. Plotting unwrapped phases against inverse grid scale produces a line (1D) or plane (2D) whose slope encodes the displacement — analogous to the Fourier shift theorem.
- **Neural network models**: Four biologically plausible implementations are described and simulated:
  1. **Distance cell model** — decodes absolute location from grid phases, then computes displacement via a readout neuron with graded weights.
  2. **Rate-coded vector cell model** — decodes displacement directly from phase differences across modules via multiplicative synapses.
  3. **Phase-coded vector cell model** — exploits theta phase precession in grid cells so that the displacement to a goal is encoded in the theta firing phase of grid cells at the current location.
  4. **Linear look-ahead model** — uses simulated self-motion signals to sequentially shift the grid cell activity bump, with goal arrival signalled by coincident activity across modules.
- **Simulations**: Each model is validated by demonstrating accurate recovery of 2D translation vectors across large-scale space (details in Supplemental Information).

---

### Key findings

- The displacement between two grid-coded locations can be recovered by finding the maximum slope of a plane fitted to phase differences plotted against inverse grid scale across modules — a solution inspired by the Fourier shift theorem.
- This algorithm is robust to differences in grid orientation and ellipticity across modules.
- All four neural network implementations (distance cell, rate-coded vector cell, phase-coded vector cell, linear look-ahead) accurately decode 2D translation vectors with accuracy and range comparable to the theoretical capacity of the grid cell system.
- Direct decoding models (distance and vector cell) compute vectors rapidly and in parallel but require additional neural circuitry and, in the rate-coded case, multiplicative synapses.
- The linear look-ahead model requires only existing path integration circuitry, but computation time scales with displacement distance, consistent with human response-time data on imagined paths.
- The phase-coded vector cell model predicts that grid cells encoding goal locations should fire at specific theta phases relative to the current location's theta trough — a testable prediction not yet verified experimentally.
- The linear look-ahead model predicts sequential band-like activation of grid cells during route planning, analogous to place cell preplay/replay.

---

### Computational framework

**Residue number system / Fourier shift theorem**

The paper models the grid cell system as a residue number system: each module encodes location modulo its spatial scale, and the combination of phases across modules with incommensurate scales uniquely identifies locations up to the system's capacity (approximately the lowest common multiple of all grid scales). The core formalism treats the displacement between two locations as the unknown to be recovered from a set of modular phase differences.

The key insight is that this recovery problem is equivalent to the Fourier shift theorem: if the phases at each module are treated as Fourier components of a spatial representation, the translation applied to those components (the displacement) appears as a linear phase ramp across components, recoverable by fitting a line or plane through the origin in phase vs. inverse-scale space.

Key variables: grid scale si, spatial phase pi for each module i, phase difference Dpi between start and goal, integer ambiguity ni (the "unwrapping" parameter), and displacement d. The framework assumes the grid cell representation is globally coherent across environments (i.e., relative phases between co-recorded grid cells are preserved), which recent empirical data supports at least for connected environments.

---

### Prevailing model of the system under study

The paper's introduction indicates that the prevailing framework at the time was that grid cells serve primarily as a path integration input to place cells — updating the place cell representation of self-location based on movement vectors (the "forward problem"). Place cells themselves were the longstanding focus of vector navigation models, but the introduction explicitly notes their limitations: place fields lack consistent inter-environment structure, and place-cell-based navigation beyond the largest field diameter requires extensive experience-dependent learning and is biased toward familiar routes. Grid cells were known to provide a compact, context-independent, large-scale metric for space, and it was noted that they could in principle solve the inverse (vector navigation) problem, but no concrete algorithmic solution or biologically plausible implementation had been worked out in full generality for distances exceeding the largest grid scale.

---

### What this paper contributes

The paper converts the intuition that grid cells could support vector navigation into a worked algorithmic solution that handles displacements larger than any individual grid scale, extending earlier Chinese Remainder Theorem-based proposals that had limitations (hard-wired energy landscapes, outputs only correct modulo the LCM of scales, or gradient descent with local minima). By mapping the problem onto the Fourier shift theorem, the authors provide a clean, scale-robust solution. The four neural network implementations make the framework concrete and experimentally distinguishable: they predict specific firing patterns (distance cells with band-like allocentric fields; vector cells with translation-invariant displacement tuning; sequential grid band activation during look-ahead; goal-location grid cells firing at specific theta phases). The paper thus shifts the theoretical role of grid cells from purely supporting path integration to actively enabling prospective, allocentric vector navigation — including to locations never directly visited.

---

### Brain regions & systems

- **Medial entorhinal cortex (mEC)** — primary locus of grid cells; superficial layers contain the grid cell population proposed to implement vector navigation; deeper layers contain conjunctive grid × head-direction cells proposed to drive linear look-ahead via directional input.
- **Hippocampus proper** — contains place cells, implicated in anchoring grid representations to sensory context; place cells proposed as coincidence detectors signalling goal arrival during look-ahead.
- **Pre- and parasubiculum** — also contain grid cells, though their topographic organisation is less clear.
- **Subicular complex / deeper mEC layers** — contain head direction cells, relevant to directional components of vector computation.
- **Hippocampal formation (general)** — the paper notes bilateral lesion data and metabolic imaging implicating the formation broadly in vector navigation performance.

---

### Mechanistic insight

The paper proposes a formalised algorithm and describes multiple neural implementations, but does not provide new neural recordings, lesion data, or pharmacological evidence specifically linking any of the proposed model variables (distance cells, vector cells, look-ahead sweeps, theta phase patterns) to measured neural activity. The paper therefore does not meet the bar for mechanistic insight as defined here.

The paper proposes an algorithm and several plausible implementational substrates grounded in existing anatomical and electrophysiological knowledge (continuous attractor networks, theta phase precession, conjunctive cells), but the specific predictions it generates — goal-location grid cell reactivation, theta phase coding of displacement, sequential band activation during planning — had not been tested at the time of publication and are offered as future experimental targets rather than validated mechanisms.

---

### Limitations & open questions

- **Global coherence assumption**: The algorithm requires that grid cell representations are globally consistent across large spaces. Local boundary-induced distortions and fragmentation of grid patterns could impair vector navigation unless all modules are affected equally; this was not established by the data available.
- **Multiplicative synapses**: The rate-coded vector cell model requires multiplicative synaptic interactions, which are biologically controversial (though dendritic branch integration may approximate this).
- **Theta phase precession alignment**: The phase-coded model requires phase precession aligned with specific 1D axes, independent of trajectory direction — it was unclear whether such alignment exists in mEC grid cells.
- **Allocentric-to-egocentric conversion**: The models produce allocentric translation vectors; how these are converted to egocentric movement commands elsewhere in the brain is not addressed.
- **Sensory anchoring**: The models require that grid representations be anchored to environmental landmarks to prevent drift; the paper acknowledges this but does not model it.
- **Scale of look-ahead**: Whether mEC is necessary specifically for vector navigation (as opposed to path integration or other spatial computations) remained to be tested.
- **Band cells and VCOs**: The same algorithmic solution could be implemented by band cells or velocity-controlled oscillators rather than grid cells; distinguishing these experimentally is an open question.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — cognitive map theory
- Hafting et al. (2005) — discovery of grid cells in mEC
- Fiete et al. (2008) — capacity of the grid cell residue number system
- Erdem & Hasselmo (2012, 2014) — linear look-ahead with grid cells
- Kubie & Fenton (2012) — vector navigation with grid cells
- McNaughton et al. (2006) — path integration and grid cells
- Stensola et al. (2012) — discrete modular organisation of grid cells
- Orchard et al. (2013) — Fourier shift theorem and grid cells
- Barry et al. (2007) — experience-dependent rescaling and modular grid organisation
- Carpenter et al. (2015) — global grid representation across connected environments
- Pfeiffer & Foster (2013) — goal-directed place cell preplay

**Named models or frameworks**:
- Distance cell model
- Rate-coded vector cell model
- Phase-coded vector cell model
- Linear look-ahead model
- Residue number system (Chinese Remainder Theorem)
- Fourier shift theorem
- Continuous attractor network (grid cell path integration)
- Oscillatory interference model

**Brain regions**:
- Medial entorhinal cortex (mEC)
- Hippocampus
- Pre- and parasubiculum
- Subicular complex

**Keywords**:
- Grid cells
- Vector navigation
- Path integration
- Spatial phase
- Residue number system
- Fourier shift theorem
- Theta phase precession
- Linear look-ahead
- Cognitive map
- Hippocampal formation
- Distance cells
- Neural network implementation
