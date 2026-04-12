---
source_file: peng2023_grid_cells_path_integration.md
paper_id: peng2023_grid_cells_path_integration
title: "Grid cells perform path integration in multiple reference frames during self-motion-based navigation"
authors:
  - "Jing-Jie Peng"
  - "Beate Throm"
  - "Maryam Najafian Jazi"
  - "Ting-Yun Yen"
  - "Hannah Monyer"
  - "Kevin Allen"
year: 2023
journal: bioRxiv
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - foraging_task
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - grid_cells
  - path_integration
  - reference_frames
  - toroidal_manifold
  - entorhinal_cortex
  - spatial_navigation
  - attractor_networks
  - deep_learning_decoding
  - multiple_reference_frames
  - re_anchoring
  - orientation_drift
  - homing_behavior
  - self_motion_cues
  - autopi_task
  - grid
  - cells
  - perform
  - path
  - integration
  - multiple
key_citations:
  - fyhn2007_remapping_grid_realignment
  - jazi2023_hippocampal_path_integration_homing
  - burak2009_path_integration_grid_cells
---

### One-line summary

Grid cells perform path integration in multiple reference frames during self-motion-based navigation, with grid modules re-anchoring to task-relevant objects via translation and accumulated orientation drift predicting homing behavior.

---

### Background & motivation

Path integration is a cognitive process whereby animals estimate their movement from self-motion cues to maintain position and orientation representations. While grid cells in the medial entorhinal cortex (MEC) have been proposed as the neural substrate for path integration, their activity has mainly been studied during random foraging with little navigational demand. How grid cells operate during actual path integration-based navigation in 2D environments remains largely unknown.

---

### Methods

- **Subjects**: 17 male C57BL/6 mice (5-9 months old)
- **Task**: AutoPI (autonomous path integration) homing task—mice left a home base, searched for a lever on a circular arena, pressed it to trigger food reward delivery, then returned to home base to collect reward
- **Conditions**: Light trials (visible LED lights) and dark trials (infrared only, no visual cues); arena rotated randomly after each trial; lever moved to new random location every 4 trials
- **Recordings**: Extracellular recordings in MEC using NeuroNexus or Cambridge Neurotech probes; 5746 neurons recorded, 931 classified as grid cells based on significant grid scores during random foraging
- **Analysis framework**: Deep learning (LSTM RNN) decoder trained on random foraging data to predict animal position in toroidal space from instantaneous grid cell firing rates; movement vectors reconstructed from toroidal position changes; directional precision and grid rotation quantified from predicted directional error distributions
- **Grid anchoring analysis**: Bivariate von Mises distribution fitted to inferred lever positions in toroidal space to quantify anchoring strength to lever vs. room reference frames

---

### Key findings

- Grid cells showed strong spatial periodicity during random foraging but significantly reduced grid scores during AutoPI light and dark trials, even when the lever was present on the arena during random foraging; this was not merely due to lever presence
- Information scores and peak firing rates were lower during dark than light trials
- An LSTM RNN decoder trained on random foraging data could predict movement vectors from grid cell activity with high directional precision (median 0.76 for sessions with ≥15 grid cells, speeds >10 cm/s), comparable to head-direction cells
- Directional precision decreased from random foraging to AutoPI light trials and further to dark trials, but remained above chance in all 24 dark trial sessions tested, demonstrating that grid cell modules perform path integration even without stable grid patterns
- Grid orientation was maintained between random foraging and AutoPI task in all but one mouse
- Grid cells exhibited lever-anchored firing fields: many grid cells fired when the mouse was in specific directions relative to the lever center, with different field locations between light and dark trials (median within-cell correlation r = 0.048)
- During dark trials, firing rate map stability was higher in the lever-centered reference frame than in the room/arena reference frame for grid cells with lever-anchored fields
- Grid modules re-anchored to the lever via translation of the grid pattern (no change in orientation), with significant anchoring strength in 23/24 dark trial sessions and 16/24 light trial sessions
- Grid anchoring strength evolved during trials: modules were firmly anchored to the room reference frame at the beginning of search paths, transitioned to lever anchoring after reaching the lever, then decreased during later homing stages
- Grid orientation drift accumulated during search paths: directional precision was higher at the beginning than the end of long search paths, with absolute predicted directional error increasing as a function of search duration
- Directional precision and drift at the lever were worse after long vs. short search paths, indicating accumulated error carries over
- Trial drift (peak in predicted directional error distribution) during search, at the lever, and during homing was positively correlated with the animal's homing heading direction, with the distribution of correlation coefficients significantly shifted toward positive values, demonstrating that accumulated grid orientation drift predicts homing behavior

---

### Computational framework

The paper employs a **deep learning decoding framework** combined with **toroidal topology analysis** to monitor grid cell activity at the module level. The core formalism involves:

- **Toroidal coordinate transformation**: Cartesian position (x,y) is transformed into toroidal coordinates (v0, v1) based on grid orientation and spacing parameters extracted from the spatial autocorrelation of firing rate maps. This captures the known toroidal manifold structure of grid cell population activity.

- **LSTM recurrent neural network**: A two-layer LSTM with 256 hidden features is trained to predict the animal's position in toroidal space (cosine and sine of v0 and v1) from the instantaneous firing rates of simultaneously recorded grid cells from the same module. Input: 400 ms of binned firing rates (20 ms bins); Output: position on torus.

- **Path reconstruction**: Movement vectors in toroidal space are calculated from changes in predicted position, then transformed back to Cartesian space and cumulatively summed to reconstruct movement paths.

- **Directional error analysis**: The angle between predicted and actual movement vectors yields predicted directional error. Directional precision (mean vector length of error distribution) and grid rotation (circular mean of error distribution) quantify path integration quality.

This framework enables sub-second resolution monitoring of grid orientation and phase anchoring, removing the need for long behavioral epochs with extended spatial coverage.

---

### Prevailing model of the system under study

The prevailing model before this study held that:

- Grid cells in the medial entorhinal cortex provide a global coordinate system for spatial navigation, with their periodic firing patterns forming a metric for path integration ( updating position and orientation via self-motion cues).
- Grid cells maintain stable, continuous grid firing patterns during navigation, serving as a fundamental neural unit for path integration across different behavioral contexts.
- The grid pattern is anchored to environmental cues (room reference frame) and provides a consistent spatial metric for the hippocampal cognitive map.

This paper questions whether the continuous grid firing pattern observed mainly during random foraging generalizes to actual path integration-based navigation tasks, where animals navigate using self-motion cues without stable visual landmarks.

---

### What this paper contributes

This paper challenges and refines the prevailing model of grid cell function in several key ways:

- **Grid cells do not maintain stable grid patterns during path integration tasks**: Contrary to the assumption that grid cells provide a continuous global coordinate system, the study shows that grid periodicity is significantly reduced during the AutoPI task compared to random foraging, even when the same physical environment elements are present.

- **Grid cells operate in multiple reference frames and dynamically re-anchor**: Grid cell modules transition between room-centered and lever-centered reference frames within single trials. Re-anchoring to the lever occurs via translation of the grid pattern without orientation change, demonstrating flexible reference frame switching.

- **Grid cells perform path integration without stable periodicity**: Using a novel decoding framework, the study demonstrates that grid cell modules still perform path integration during the AutoPI task, even when grid patterns are not stable. Directional precision decreases but remains above chance.

- **Grid orientation drift predicts behavior**: The accumulated drift in grid orientation during search paths predicts the homing direction of the mouse, establishing a direct link between grid cell computation and navigational behavior.

- **Methodological contribution**: The toroidal decoding framework enables sub-second resolution analysis of grid cell activity at the module level, opening the possibility of studying grid cells during standard navigation and memory paradigms without requiring long behavioral epochs.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — Primary recording site; contains grid cells that perform path integration and show dynamic reference frame switching; grid cells recorded from same modules (similar orientation and spacing) were analyzed together
- **Hippocampus (CA1)** — Mentioned as downstream target of grid cells; prior work showed ~25% of CA1 pyramidal cells have lever-anchored firing fields during the same task, potentially explained by grid cell re-anchoring

---

### Mechanistic insight

This paper provides mechanistic insight meeting the high bar of presenting an algorithm with neural data supporting it over alternatives:

**Phenomenon**: Grid cells perform path integration while dynamically switching between multiple reference frames during self-motion-based navigation.

**Mapping to Marr's three levels**:

- **Computational**: The brain must maintain position and orientation estimates during navigation using self-motion cues (path integration) while integrating landmarks when available. The problem is that error accumulates during pure path integration, requiring mechanisms to correct or account for drift. The animal must also flexibly represent position relative to behaviorally relevant goals (lever) and global reference frames (room).

- **Algorithmic**: Grid cells implement path integration via a toroidal attractor network where population activity flows across a toroidal manifold in correspondence with movement. The grid pattern can be translated (phase shifted) to re-anchor to different reference frames without changing orientation. The RNN decoder demonstrates that instantaneous firing rates of simultaneously recorded grid cells from the same module contain sufficient information to reconstruct movement vectors, implying that the population code on the torus encodes displacement. The drift in grid orientation correlates with homing behavior, suggesting the accumulated error in the angular path integrator directly influences navigational decisions.

- **Implementational**: The implementation is in the medial entorhinal cortex, specifically within grid cell modules (populations with similar grid spacing and orientation). The toroidal manifold structure of population activity is preserved across behaviors (as shown in prior work by Gardner et al., 2022), and the same physical circuit appears to operate in different reference frames via dynamic re-anchoring. The paper does not address specific cell types, connectivity patterns, or biophysical mechanisms, though it implies that the path integration computation is distributed across the module-level population rather than being a property of individual cells.

---

### Limitations & open questions

- **No stable grid patterns during path integration**: The observation that grid periodicity is reduced during the AutoPI task raises questions about when and why grid cells maintain stable periodic firing versus dynamic, reference-frame-switching modes.
- **Error accumulation**: The drift in grid orientation during path integration demonstrates that the system accumulates error over time/distance, but the mechanisms that reset or correct this drift (beyond re-anchoring to the lever) are not fully characterized.
- **Causal role**: The correlation between grid orientation drift and homing behavior suggests a functional role, but causal manipulations (e.g., optogenetic disruption of grid cells during specific task phases) would be needed to establish necessity.
- **Generalization to other tasks**: The findings demonstrate reference frame switching in a specific homing task; whether this generalizes to other navigation paradigms (e.g., random foraging with goals, memory tasks) remains to be tested.
- **Neural mechanism of re-anchoring**: The paper demonstrates that re-anchoring occurs via translation of the grid pattern, but the circuit mechanisms (which inputs, which cell types, neuromodulatory influences) that trigger and implement this translation are not addressed.

---

### Connections & keywords

- **Key citations**: McNaughton et al. (1996, 2006) — path integration and cognitive maps; Hafting et al. (2005) — grid cell discovery; Burak & Fiete (2009) — continuous attractor models of grid cells; Gardner et al. (2022) — toroidal topology of grid cell activity; Fyhn et al. (2007) — grid realignment; Najafian Jazi et al. (2023) — lever-anchored hippocampal firing fields; Gil et al. (2018) — impaired path integration with disrupted grid cells

- **Named models or frameworks**: AutoPI (autonomous path integration) task; toroidal attractor network; continuous attractor network; path integration; reference frame switching; LSTM RNN decoder; bivariate von Mises distribution

- **Brain regions**: medial entorhinal cortex (MEC); hippocampus (CA1)

- **Keywords**: grid cells, path integration, reference frames, toroidal manifold, entorhinal cortex, spatial navigation, attractor networks, deep learning decoding, multiple reference frames, re-anchoring, orientation drift, homing behavior, self-motion cues, AutoPI task
