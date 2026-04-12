---
source_file: ouchi2024_predictive_grid_coding.md
paper_id: ouchi2024_predictive_grid_coding
title: "Predictive grid coding in the medial entorhinal cortex"
authors:
  - "Ayako Ouchi"
  - "Shigeyoshi Fujisawa"
year: 2024
journal: Science
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - open_field
  - foraging_task
methods:
  - optogenetics
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - entorhinal_cortex
  - medial_entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - predictive_grid_cells
  - medial_entorhinal_cortex
  - theta_sequences
  - theta_phase_precession
  - phase_locking
  - spatial_prediction
  - cognitive_map
  - goal_directed_navigation
  - bayesian_decoding
  - hippocampal_entorhinal_circuit
  - continuous_attractor_network
  - prospective_coding
  - predictive
  - grid
  - coding
  - medial
  - entorhinal
  - cortex
key_citations:
  - liu2023_hippocampus_amygdala_memory_formation
---

### One-line summary

A subset of medial entorhinal cortex (MEC) neurons — termed predictive grid cells — fire with grid fields shifted ahead of the animal's current position, encoding future locations and organising within-theta-cycle sequences from current to future positions during spatial navigation.

---

### Background & motivation

The hippocampal-entorhinal circuit is understood to construct cognitive maps of allocentric space, with MEC grid cells providing the core geometric scaffold via periodic spatial firing fields. Prior work established that grid cells encode current position and integrate self-motion signals (speed, head direction), while hippocampal place cells and grid cells show some prospective bias and theta phase precession. However, it remained unclear whether the entorhinal grid system itself actively encodes future spatial positions or participates in generating predictive sequences to support goal-directed planning. This paper addresses that specific gap by asking whether a distinct functional subtype of MEC grid cells can represent prospective spatial information.

---

### Methods

- **Species and task**: Rats performed a goal-directed two-dimensional open-field task requiring back-and-forth travel between changing reward port positions, designed to sample vertical, horizontal, and diagonal trajectories and thereby allow directionally resolved detection of predictive firing biases.
- **Recordings**: High-density multishank silicon probes (8 shanks, 16 sites per shank) implanted in MEC layers 2–3 and CA1; extracellular single-unit recordings from 6 rats (main experiment) and 3 additional rats (task-comparison experiment).
- **Cell identification**: Firing rate maps were constructed at the animal's actual position and at positions projected forward and backward along the trajectory; gridness scores (measuring 60° autocorrelation periodicity) were computed as a function of spatial shift. Predictive grid cells were defined as cells whose maximum gridness score occurred at a significantly positive (future) shift and whose theta phase-locking was around 180° of CA1 theta. Phase-precession and phase-locked grid cells were also categorised.
- **Theta phase analysis**: Spike–theta phase relationships were computed relative to CA1 pyramidal-layer LFP.
- **Bayesian decoding**: A Bayesian framework decoded spatial position from ensemble spike activity across 10-ms bins in each theta phase bin to characterise theta sequences.
- **Functional connectivity**: Cross-correlograms (CCGs) between predictive grid cells and CA1 place cells were analysed to assess spike transmission directionality.
- **Behavioural generalisation**: A subset of rats performed interleaved goal-directed and random-foraging tasks to test whether predictive coding was behaviour-specific.

---

### Key findings

- 305 predictive grid cells were identified across 6 rats; these cells had maximum gridness at a mean forward shift of 22.5 ± 10.2 cm (~0.27 of grid spacing, roughly one-quarter of grid spacing).
- Phase-precession grid cells had a smaller but positive mean shift (4.5 ± 8.8 cm); phase-locked grid cells had shifts near zero (0.8 ± 9.0 cm).
- Predictive grid cells fired at the trough (~180°) of CA1 theta oscillations, opposite to phase-locked grid cells and distinct from phase-precessing cells.
- Predictive grid cells were predominantly located in MEC layer 3; phase-precessing cells in layer 2; phase-locked cells in layer 3 (opposite phase preference).
- The overall firing rate distribution of predictive grid cells was skewed toward the start of trajectories, consistent with forward (not backward) field shifts within bounded environments.
- Bayesian decoding using the three cell types together revealed theta sequences sweeping from current to future positions across each theta cycle; removing predictive grid cell spikes significantly reduced the representation of future positions during descending theta phases.
- Disrupting spike synchronisation within theta cycles also abolished the future-position representation, implicating coordinated assembly activity.
- CCG analysis showed increased functional connectivity from predictive grid cells to CA1 place cells when the grid field of the predictive cell preceded the place field of the CA1 cell, suggesting directional spike transmission.
- Predictive coding properties of all three cell types were preserved across goal-directed and random-foraging tasks (grid spacing rescaled but position-shift bias and phase preferences were maintained).

---

### Computational framework

The paper uses a **spatial decoding / theta-sequence** framework grounded in the idea that neural assemblies encode prospective trajectories by distributing activity across the phase of theta oscillations.

Core formalism: firing rate maps are constructed by projecting the animal's position forward or backward along the trajectory by a fixed distance d, and gridness scores are computed as a function of d. The key variable is the optimal spatial shift at which gridness is maximised. Bayesian population decoding reconstructs position from ensemble activity in each theta-phase bin, revealing a sweep of decoded positions from current to future across the descending phase of each theta cycle. The framework assumes that different functional cell subtypes (predictive, phase-precessing, phase-locked) tile different phases of the theta oscillation, collectively producing a compressed temporal sequence. Attractor network dynamics and continuous attractor models are invoked in the Discussion as a possible mechanistic substrate for predictive shift generation.

---

### Prevailing model of the system under study

Prior to this paper, the standard view was that MEC grid cells encode the animal's current allocentric position via a low-dimensional continuous attractor network, integrating speed and head direction signals to update location estimates. Grid cells were known to send positional information to hippocampal CA1 (via layer 2 and 3 projections), and both MEC and CA1 neurons showed modest prospective biases and theta phase precession in one-dimensional tasks. Theta sequences in CA1 — representing past-to-future trajectories within each theta cycle — were well established and thought to depend partly on MEC layer 3 input (the "dual input model" of CA1 sequence generation, with MEC driving at theta peak and CA3 driving near trough). However, MEC grid cells were not known to harbour a distinct cell population dedicated to representing future spatial positions, and the direct contribution of identifiable MEC subtypes to organising CA1 theta sequences was unclear.

---

### What this paper contributes

This paper establishes that the MEC contains a functionally distinct population of grid cells — predictive grid cells — whose spatial firing fields are systematically shifted to represent future locations, not simply current ones. This adds a new node to the circuit model of predictive spatial coding: predictive MEC grid cells are proposed to feed forward prospective spatial information to CA1, timed to fire at theta troughs just before CA1 encodes future positions in the late theta phase. The three-population MEC model (predictive, phase-precessing, phase-locked) producing a within-theta sweep from current to future positions is a new organisational principle not previously demonstrated in the entorhinal cortex. The cross-correlogram evidence linking predictive grid cell firing to CA1 place cell activity as a function of relative field positions provides a functional connectivity signature consistent with a feedforward predictive drive to hippocampus. The result that predictive coding is preserved during random foraging generalises the finding beyond goal-directed contexts.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC), layers 2–3** — locus of all three grid cell types; predictive grid cells predominantly in layer 3; phase-precessing cells in layer 2; phase-locked cells in layer 3 with opposite phase preference.
- **CA1 (hippocampus)** — reference site for theta LFP used to define theta phase; also the downstream target examined via cross-correlogram analysis; place cells here receive putative predictive drive from MEC predictive grid cells.
- **Hippocampal-entorhinal axis** — the broader circuit framework in which predictive spatial information is generated (MEC) and organised into sequences (CA1).

---

### Mechanistic insight

This paper meets both criteria for the high bar.

1. It formalises and tests a specific algorithm: grid fields are shifted forward along the trajectory by ~one-quarter grid spacing; this shift, combined with theta-phase-locked firing at the trough, enables an assembly-level sweep encoding future positions within each theta cycle.
2. It provides neural recording data (single-unit extracellular recordings in MEC and CA1 of freely behaving rats) that specifically support this algorithm: the gridness-vs-shift analysis identifies the forward-biased representation quantitatively; theta phase histograms confirm the trough-locking of predictive cells and its contrast with other subtypes; Bayesian decoding of ensemble activity across theta phases directly demonstrates the future-position sweep; disrupting predictive cell contributions (by exclusion from decoding) or disrupting within-theta synchrony specifically reduces future-position representation; CCG evidence links predictive cells to CA1 place cells in a direction-dependent manner.

**Marr's three levels:**

- **Computational**: The brain solves the problem of forward planning by constructing a predictive spatial map — representing where the animal will be, not only where it is — to support goal-directed trajectory selection.
- **Algorithmic**: A subset of MEC grid cells maintain grid firing fields shifted ~one-quarter grid spacing ahead of current position. These cells fire at the trough of CA1 theta, while phase-precessing cells encode intermediate positions and phase-locked cells encode current positions. The coordinated assembly activity across theta phases implements a compressed temporal sequence sweeping from current to future positions within each ~100 ms theta cycle.
- **Implementational**: Predictive grid cells are concentrated in MEC layer 3, which projects directly to CA1 stratum lacunosum-moleculare at theta trough phases. The mechanism generating the forward shift is hypothesised to involve speed and head-direction inputs into recurrent MEC circuits with attractor dynamics, but this is not directly demonstrated in the paper.

**Bonus**: The paper notes layer specificity (layer 3 for predictive cells, layer 2 for phase-precessing cells) and references the dual-input model of CA1 activation, but does not provide direct causal manipulation or circuit-level data on cell types or neuromodulators.

---

### Limitations & open questions

- The mechanism by which predictive grid cells generate forward-shifted fields is unknown; the authors hypothesise self-motion inputs (speed and head direction) into recurrent attractor circuits but do not test this directly.
- Only spatial position shifts are characterised; it is unclear how these cells behave during non-spatial tasks or in representational contexts beyond physical navigation.
- The study is correlational; causal evidence that predictive grid cells are necessary for forward planning behaviour or CA1 theta sequence generation is absent.
- The paper notes that the optimal shift of predictive cells was also positive (but smaller) when computed in the time domain rather than the position domain, raising the question of whether prediction is primarily coded in distance or time.
- Whether predictive grid cells exist or serve the same role in other species, including primates, is unresolved.
- The relationship between predictive grid coding and hippocampal sharp-wave ripples (another mechanism for prospective planning) is not addressed.
- Recordings were limited to layers 2–3; whether deeper MEC layers contain analogous predictive populations is unknown.

---

### Connections & keywords

**Key citations:**
- Hafting et al. 2005 (Nature) — original discovery of grid cells in MEC
- Hafting et al. 2008 (Nature) — theta phase precession and phase locking of MEC grid cells
- Burak & Fiete 2009 (PLoS Comp Biol) — continuous attractor network model of MEC
- Dragoi & Buzsáki 2006 (Neuron) — theta sequences in CA1
- Fernández-Ruiz et al. 2017 (Neuron) — dual input model of CA1 sequence generation, MEC layer 3 at theta peak
- Liu et al. 2023 (Science) — optogenetic perturbation of MEC disrupts CA1 predictive theta sequences
- Chaudhuri-Vayalambrone et al. 2023 (Cell Reports) — spatial vs temporal domain of prospective coding in MEC/hippocampus
- Gardner et al. 2022 (Nature) — continuous attractor manifold of MEC grid cell population

**Named models or frameworks:**
- Continuous attractor network (MEC grid cell model)
- Dual input model of CA1 (MEC layer 3 + CA3 inputs at different theta phases)
- Oscillatory interference model of theta phase precession
- Soma-dendrite interference model of theta phase precession
- Cognitive map theory (O'Keefe & Nadel 1978)

**Brain regions:**
- Medial entorhinal cortex (MEC), layers 2–3
- CA1 hippocampus

**Keywords:**
- predictive grid cells
- medial entorhinal cortex
- theta sequences
- theta phase precession
- phase locking
- spatial prediction
- cognitive map
- goal-directed navigation
- Bayesian decoding
- hippocampal-entorhinal circuit
- continuous attractor network
- prospective coding
