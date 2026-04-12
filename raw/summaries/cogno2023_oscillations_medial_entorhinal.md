---
source_file: "cogno2023_oscillations_medial_entorhinal.md"
paper_id: "cogno2023_oscillations_medial_entorhinal"
title: "Minute-scale oscillatory sequences in medial entorhinal cortex"
authors: "Soledad Gonzalo Cogno, Horst A. Obenhaus, Ane Lautrup, R. Irene Jacobsen, Claudia Clopath, Sebastian O. Andersson, Flavio Donato, May-Britt Moser, Edvard I. Moser"
year: 2023
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
methods: ["calcium_imaging", "electrophysiology", "neuropixels", "computational_modeling"]
brain_regions: ["hippocampus", "hippocampus_ca1", "entorhinal_cortex", "medial_entorhinal_cortex", "visual_cortex"]
frameworks: ["attractor_networks"]
keywords: ["minute", "scale", "oscillatory", "sequences", "medial", "entorhinal", "cortex"]
---

### One-line summary

MEC neurons exhibit ultraslow oscillations (periods of tens of seconds to minutes) that are coordinated across nearly the entire recorded population into periodic sequential activation patterns — oscillatory sequences — that persist through both running and immobility and are absent in neighbouring parasubiculum and visual cortex.

---

### Background & motivation

Neural activity is coordinated across brain regions at sub-second time scales by oscillations, and there are prior reports of ultraslow oscillations (<0.1 Hz, periods of tens of seconds to minutes) in individual neurons and local field potentials across several areas. However, it was unknown how pervasive such oscillations are, whether they organise the activity of large neural populations, and whether the coordination takes on any structured (e.g. sequential) form. The MEC is an ideal region to investigate this question because it houses the cellular elements supporting spatial navigation and episodic memory — functions that require neural activity to be organised over second-to-minute behavioural time scales.

---

### Methods

- **Subjects**: Head-fixed male C57/Bl6 mice (5 MEC, 4 parasubiculum [PaS], 3 visual cortex [VIS] imaging mice; 2 MEC Neuropixels mice).
- **Task**: Self-paced running on a rotating wheel in complete darkness with no scheduled rewards, for 30–60 min sessions. This minimalist design eliminated external sensory modulation as a confound.
- **Neural recordings**:
  - Two-photon calcium imaging (GCaMP6m) of MEC, PaS, and VIS superficial layers via microprism (MEC/PaS) or cranial window (VIS); up to ~500 cells per session, 30.95 Hz frame rate.
  - Neuropixels 2.0 probes (4-shank) in MEC of 2 mice, yielding ~400–880 units per session.
- **Single-cell analysis**: Deconvolved calcium signals binarised at 7.73 Hz; power spectral density (PSD) via Welch's method on autocorrelations; primary oscillatory frequency identified as PSD peak.
- **Population analysis**: Cells sorted by seed-cell correlation or by PCA on the calcium activity matrix; ring-manifold visualised via PCA and Laplacian eigenmaps (LEM). Phase of the oscillation tracked by position on the ring.
- **Phase locking**: Computed per-cell locking degree and mutual information between phase and calcium events; significance assessed against per-cell shuffle distributions.
- **Travelling wave test**: Correlation of pairwise preferred-phase differences with anatomical distance.
- **Ensemble analysis**: 10 co-activity ensembles defined from PCA sorting; transition matrices computed; sequential activation compared to shuffled controls.
- **Computational model**: 500-unit feedforward network generating sequential activity used as input to a single output neuron; target patterns (ramp, stochastic) trained via weight optimisation; tested across different input sequence speeds.
- **Comparison regions**: Identical recordings and analyses applied to PaS (25 sessions, 4 mice) and VIS (19 sessions, 3 mice).

---

### Key findings

- Ultraslow oscillations (all primary frequencies <0.1 Hz; range across sessions 0.036–0.057 Hz) were detected in the majority of MEC neurons: 91% by calcium imaging (5,691/6,231 cells across 15 sessions, 5 mice) and 78% by Neuropixels (683/879 units).
- Population activity organised into periodic oscillatory sequences visible as ordered travelling waves in neural activity raster plots and as ring-shaped manifolds in PCA/LEM embedding space.
- 93.7% of all recorded MEC cells (5,841/6,231) were significantly phase-locked to the sequences across all 15 oscillatory sessions (median 94% per session).
- Sequence durations ranged from tens of seconds to minutes, with high variability across sessions/mice but low within-session variability.
- 69% of inter-sequence intervals were 0 s (consecutive sequences); maximum ISI was 452 s.
- Sequences were not travelling waves: pairwise preferred-phase-to-anatomical-distance correlations were small and non-significant (range −0.068 to 0.147 across 421 sequences).
- Sequences persisted during immobility (sequences observed continuously for up to 258 s during motionless epochs); sequence onset was 3.1× more likely during running bouts.
- Number of wheel laps per sequence was highly heterogeneous (0–86), confirming sequence progression was not tied to distance run.
- Oscillatory sequences were absent in PaS and VIS: all 44 PaS and VIS sessions fell below the MEC oscillation score threshold (0.72), despite individual cells in those regions showing some ultraslow periodicity.
- Computational model showed that a sequential network template can support output patterns only at time scales equal to or slower than the input sequence duration, suggesting a functional rationale for minute-scale sequences.

---

### Computational framework

**Dynamical systems / ring attractor network.**

The paper interprets the oscillatory sequences as low-dimensional population dynamics on a 1D manifold embedded in high-dimensional neural space — specifically, a ring topology identified by PCA and LEM. The key quantity is the "phase of the oscillation," the angular position of the population activity state on the ring, which advances monotonically and periodically. The framework assumes that the MEC network has recurrent connectivity that supports continuous rotational dynamics, consistent with a ring-shaped continuous attractor network (citing Ben-Yishai et al. 1995 and Skaggs et al. 1995). The paper also notes that recurrent networks, feedforward synfire chains, and slow plasticity rules are alternative mechanistic candidates. The computational model formalises a potential function: sequential activity at behavioural time scales enables downstream read-out neurons to reproduce target activity patterns of matching or slower duration, formalising a "template" mechanism.

---

### Prevailing model of the system under study

Before this paper, the MEC was well understood as the locus of spatially tuned cell types — grid cells, head-direction cells, border cells — whose activity encodes location and movement direction on spatial scales of metres. The dominant view was that MEC activity is coordinated at sub-second time scales by theta (~8 Hz) and gamma oscillations, coupling with hippocampal circuits during navigation and memory encoding. Slow temporal organisation of MEC neurons (seconds-to-minutes) was essentially uncharacterised. While hippocampal CA1 had been shown to generate internally recurring sequences, those sequences involved only a small fraction (~5%) of neurons and were tightly coupled to running distance. The MEC was thought to support a low-dimensional population code that covaries across environments, in contrast to the high-dimensional orthogonalising code of the hippocampus — but the temporal dimension of this low-dimensional code on minute scales had not been described. The introduction is explicit that it is unknown whether or how ultraslow oscillations are organised at the population level in any brain region.

---

### What this paper contributes

This paper establishes that MEC uniquely supports minute-scale oscillatory sequences that involve nearly all recorded neurons — a form of temporal population organisation that was not previously described in MEC or any other brain area. Key updates to the prevailing model:

1. MEC neural activity has a second temporal structure beyond spatial tuning: a slow population clock that advances at 0.006–0.057 Hz, independent of the animal's spatial position or running state.
2. The temporal organisation is collective and nearly complete: ~94% of cells are phase-locked, contrasting sharply with CA1 sequences that recruit ~5% of neurons, consistent with MEC's proposed low-dimensional code.
3. This organisation is specific to MEC network architecture and is not a generic feature of parahippocampal or sensory cortex, since PaS and VIS show no comparable population-level sequential structure despite individual cells showing ultraslow periodicity.
4. The sequences are not travelling waves in anatomical space, implying functional rather than topographic organisation.
5. A modelling result formalises how such sequences could act as a temporal template for downstream formation of activity patterns at behavioural time scales, potentially supporting memory encoding and temporal coding during extended experiences.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — primary focus; locus of the oscillatory sequences; proposed to harbour unique network mechanisms for sequential coordination, consistent with ring attractor dynamics.
- **Parasubiculum (PaS)** — parahippocampal region studied as comparison; individual cells show ultraslow periodicity but no population-level sequential organisation.
- **Visual cortex (VIS)** — used as a cortical control with known high-dimensional activity; individual cells show ultraslow periodicity but no population-level sequential organisation; activity more correlated with speed than MEC or PaS.
- **CA1 hippocampus** — referenced for comparison; generates internally recurring sequences but involving only ~5% of neurons and more tightly coupled to running distance.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the algorithmic level.

**Computational**: The brain must organise neural population activity across the second-to-minute time scales of behaviour to support navigation and episodic memory encoding. The oscillatory sequences provide a slow temporal scaffold that can tile behavioural experience.

**Algorithmic**: Nearly the entire MEC population (~94%) is locked to a phase variable that advances on a ring-shaped manifold at 0.006–0.057 Hz. Neurons activate in a fixed sequential order, the sequence repeats periodically, and the phase of the population on the ring carries a continuous readout of the elapsed cycle. This ring-phase variable is the algorithmic quantity; the paper provides neural data (calcium imaging of ~500 cells and Neuropixels recording of ~400–800 units) directly supporting its existence and its absence from anatomically adjacent regions.

**Implementational**: The paper does not identify specific cell types, connectivity patterns, or biophysical mechanisms generating the sequences. It raises the ring continuous attractor network as a candidate framework and notes that arousal-associated neuromodulatory circuits could drive the global oscillatory component, while the sequential structure is MEC-specific. The paper explicitly states that distinguishing between ring attractor, recurrent network, feedforward synfire chain, and slow-plasticity mechanisms remains an open question.

**Bonus note**: The paper does not address specific cell types (e.g. stellate vs. pyramidal, interneurons) or neuromodulatory identity of the mechanism, so the implementational level remains unresolved.

---

### Limitations & open questions

- Recordings were restricted to a minimalist task (running wheel, darkness, no rewards); whether oscillatory sequences occur during free exploration, sleep, or in the presence of salient landmarks is unknown. Sequences may reset with strong sensory stimulation.
- Only layer II/superficial layers of MEC were targeted with calcium imaging; deeper layers and interneurons were not systematically characterised (Neuropixels data were noisier and sampled more broadly).
- The mechanistic origin of the sequences is unresolved: ring continuous attractor, recurrent network, feedforward synfire chain, and slow synaptic plasticity are all compatible with the data.
- The paper does not identify the cell types (grid cells, head-direction cells, border cells) or specific connectivity generating the sequences.
- The relationship between the ultraslow oscillatory sequences and grid/head-direction cell firing fields during navigation was not directly examined.
- The computational model is a simple feedforward template — it does not implement biologically realistic learning rules or specify how downstream connections would be modified.
- Whether sequences interact with faster oscillations (theta, gamma) or with lateral entorhinal cortex drifting activity was not tested.

---

### Connections & keywords

**Key citations**:
- Hafting et al. 2005 (Nature) — grid cells in MEC
- Sargolini et al. 2006 (Science) — conjunctive MEC cells
- Buzsáki & Moser 2013 (Nat Neurosci) — hippocampal-entorhinal memory and theta
- Villette et al. 2015 (Neuron) — internally recurring hippocampal sequences
- Gardner et al. 2022 (Nature) — toroidal topology of grid cell population activity
- Stringer et al. 2019 (Nature) — high-dimensional VIS population activity
- Ben-Yishai et al. 1995 (PNAS) — ring attractor theory
- Lecci et al. 2017 (Sci Adv) — coordinated infraslow oscillations in sleep
- Aghajan et al. 2023 (Cell Rep) — minute-scale periodicity in human entorhinal neurons

**Named models or frameworks**:
- Ring-shaped continuous attractor network
- PCA/Laplacian eigenmaps (LEM) dimensionality reduction for manifold extraction
- Oscillation score (bimodal threshold = 0.72 for classifying oscillatory sessions)
- Sequence score (probability of 3+ ensemble transitions vs. shuffle)
- Locking degree (phase-locking of individual neurons to the oscillation)

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Parasubiculum (PaS)
- Visual cortex (VIS)
- CA1 hippocampus (comparison)

**Keywords**:
- Ultraslow oscillations
- Oscillatory sequences
- Medial entorhinal cortex
- Population dynamics
- Ring attractor
- Two-photon calcium imaging
- Neuropixels electrophysiology
- Phase locking
- Temporal coding
- Sequential neural activity
- Low-dimensional population code
- Behavioural time scale
