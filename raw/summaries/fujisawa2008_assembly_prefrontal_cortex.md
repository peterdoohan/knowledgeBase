---
source_file: fujisawa2008_assembly_prefrontal_cortex.md
paper_id: fujisawa2008_assembly_prefrontal_cortex
title: "Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex"
authors:
  - "Shigeyoshi Fujisawa"
  - "Asohan Amarasingham"
  - "Matthew T Harrison"
  - "György Buzsáki"
year: 2008
journal: "Nature Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - t_maze
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - prelimbic_cortex
keywords:
  - short_term_synaptic_plasticity
  - cell_assemblies
  - medial_prefrontal_cortex
  - monosynaptic_interactions
  - cross_correlogram_analysis
  - working_memory
  - pyramidal_interneuron_connectivity
  - synaptic_facilitation_and_depression
  - coincidence_detection
  - jitter_resampling
  - silicon_probe_recording
  - sparse_coding
  - behavior
  - dependent
  - short
  - term
  - assembly
  - dynamics
  - medial
  - prefrontal
---

### One-line summary

Large-scale in vivo recordings from rat medial prefrontal cortex during a working memory task reveal that monosynaptic efficacy between pyramidal cells and interneurons varies dynamically with task demands, consistent with short-term synaptic facilitation and depression supporting transient cell assemblies.

---

### Background & motivation

Short-term synaptic plasticity — the sub-second modulation of synaptic efficacy — has been characterised extensively in vitro and is heavily implicated in theoretical accounts of cortical computation and working memory. However, direct empirical evidence for its operation in the intact behaving brain was scarce, leaving its behavioural significance largely speculative. This paper addresses that gap by asking whether signatures of short-term plasticity are detectable in the fine-timescale spiking relationships of simultaneously recorded mPFC neurons during active behaviour, and whether those dynamics are tied to task demands.

---

### Methods

- **Subjects**: four adult male rats trained to criterion (>85% correct) on an odour-based delayed match-to-sample task in a figure-eight T-maze (mean performance during recording: 91.9%).
- **Task**: rats associated a sample odour (chocolate or cheese) presented at a nose-poke start box with the spatial location (left or right arm) of a reward; working memory required maintaining the odour-place association across the traversal of the central stem.
- **Recordings**: chronic implantation of 8-shank, 64-channel silicon probes in anterior cingulate (area 24) and dorsal prelimbic (area 32) cortex, targeting layers 2/3 or layer 5; 633 well-isolated single units recorded across sessions.
- **Cell classification**: pyramidal cells and interneurons identified physiologically using short-latency cross-correlogram peaks (excitatory, <5 ms onset) and troughs (inhibitory) from population pairwise analysis.
- **Spike transmission / monosynaptic detection**: jitter-based resampling (±5 ms, 1,000 surrogates) used to identify short-latency excess coincidences (1–4 ms) beyond what slow-timescale rate co-variation could explain.
- **Position-dependent efficacy**: firing rate confounds controlled using a spike-thinning procedure to equate rates across maze segments before testing for position-dependent monosynaptic activity.
- **Plasticity mechanisms**: spike transmission probability conditioned separately on first spikes (ISI >200 ms) vs. subsequent spikes (ISI <40 ms) to detect facilitation and depression; cooperative effects tested by conditioning on simultaneous discharge of multiple presynaptic neurons within 2–20 ms windows.

---

### Key findings

- mPFC neurons fired transiently and sequentially across maze positions, with individual cells active for mean normalised distances of 0.27 ± 0.17 (approximately 62 ± 39 cm); approximately 10–20% of active neurons fired in any 100-ms window.
- A substantial fraction of neurons discriminated left vs. right trajectories: 40% (layer 5) and 22% (layer 2/3) in the side arms; 16–18% in the central stem where motor trajectories were indistinguishable, suggesting internally generated (goal) representations.
- 0.79% of 62,408 cell pairs showed significant monosynaptic interactions (0.55% excitatory, 0.24% inhibitory); most monosynaptically excited targets were interneurons (50.7% of postsynaptic targets were themselves inhibitory).
- Monosynaptic efficacy varied as a function of maze position and trajectory: 67 of 343 excitatory pairs showed identifiable position dependence (P < 0.01); in several cases this was demonstrable after spike-thinning to control for rate confounds.
- Approximately 12.7% of pairs showed firing-pattern-dependent depression and 10.7% showed facilitation (first vs. subsequent spikes, permutation test P < 0.10).
- Coincident firing of two or more presynaptic neurons within 5 ms produced supralinear increases in postsynaptic discharge probability; windows >10 ms produced only linear summation.
- Only approximately 1–5% of all neurons (active and silent) fired synchronously in any 100-ms window, indicating sparse, distributed encoding.

---

### Computational framework

The paper does not develop or fit a formal computational model, but its findings are interpreted within the **Hebbian cell assembly** framework (Hebb 1949) extended by short-term synaptic plasticity. The core idea is that transiently formed coalitions of neurons — assemblies — are dynamically recruited and released on sub-second timescales via the modulation of synaptic weights. Two specific mechanisms are implicated:

1. **Firing-pattern-dependent short-term plasticity** (facilitation and depression at pyramidal-interneuron synapses): whether a presynaptic spike train potentiates or depresses its target depends on the history of recent spiking. This provides a time-varying gain on specific connections.
2. **Supralinear coincidence detection**: simultaneous discharge of multiple presynaptic neurons within a narrow window (<5 ms) boosts postsynaptic firing beyond linear summation, possibly via dendritic spike mechanisms.

Together these mechanisms provide a substrate for sequentially evolving assemblies with characteristic "lifetimes" of activity, linking the millisecond-timescale of synaptic dynamics to the second-timescale of behavioural states.

---

### Prevailing model of the system under study

The paper engages with two prevailing frameworks. First, theories of **working memory** in which persistent firing of mPFC neurons maintains a representation of a stimulus beyond its offset ("neuronal reverberation"), with mPFC as the locus of sustained goal representations. Second, in vitro studies had firmly established that pyramidal-interneuron synapses exhibit short-term facilitation and depression on timescales of tens to hundreds of milliseconds, and computational models had proposed roles for these dynamics in cortical processing. However, the dominant prior assumption was that such short-latency cross-correlogram peaks in behaving animals reflected pyramidal-pyramidal interactions and related to associative learning or reward expectancy — not specifically pyramidal-interneuron transmission. The in vivo behavioural significance of short-term plasticity remained largely assumed rather than demonstrated.

---

### What this paper contributes

The paper provides direct in vivo evidence, in a behaving animal, that monosynaptic efficacy at pyramidal-interneuron synapses is dynamically modulated as a function of task context — over and above changes attributable to co-varying firing rates. Before this work, modulation of short-latency cross-correlogram peaks during behaviour had been observed but was attributed to pyramidal-pyramidal interactions; Fujisawa et al. demonstrate, using physiological cell-type identification, that the relevant interactions are predominantly pyramidal-to-interneuron. They further show that the two mechanisms established in vitro — firing-pattern-dependent plasticity and supralinear coincidence summation — are detectable in the intact behaving brain and can explain, at least partially, why synaptic efficacy varies with task demands. The combined evidence supports the hypothesis that internally generated, sequentially organised cell assemblies — rather than moment-to-moment sensory or motor input — encode goal representations in mPFC, with short-term plasticity as a key mechanistic substrate.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC), anterior cingulate cortex (area 24) and dorsal prelimbic cortex (area 32)** — primary site of recording; proposed locus of goal representation, working memory, and the cell assemblies under study.
- **Layer 2/3 of mPFC** — lower fraction of trajectory-selective neurons (22% in side arms) relative to layer 5; superficial recording targets.
- **Layer 5 of mPFC** — higher fraction of trajectory-selective neurons (40% in side arms); deeper recording targets with generally higher synchrony (20% active per 100-ms window vs. 10% in layer 2/3).

---

### Mechanistic insight

This paper meets both criteria for mechanistic insight:

1. It proposes a specific algorithm — short-term synaptic plasticity (facilitation/depression) and supralinear coincidence summation — as computations that could explain dynamic assembly formation and behavioural coding.
2. It provides in vivo neural recordings that specifically test these mechanisms using cross-correlogram analysis conditioned on spike-train history and presynaptic coincidence.

**Computational level**: The brain must maintain and update goal representations across a working memory delay and translate them into directional motor choices. mPFC must sustain an internally generated representation (left vs. right goal) that is not reducible to concurrent sensory or motor signals.

**Algorithmic level**: Sequentially organised, transiently active cell assemblies encode trajectory-specific representations. Short-term synaptic plasticity dynamically gates which neurons are recruited into the active assembly: depressing synapses cause a neuron to disengage as the presynaptic partner continues firing (handing off to the next assembly); facilitating synapses increase a neuron's influence during sustained presynaptic bursting. Supralinear coincidence detection means that when multiple assembly members fire together within <5 ms, postsynaptic interneurons are recruited with disproportionate efficacy, sharpening and timing the assembly transitions.

**Implementational level**: The relevant connections are predominantly pyramidal-to-interneuron monosynaptic links (not pyramidal-pyramidal), detectable by narrow cross-correlogram peaks at 1–4 ms offsets. Facilitation and depression are target-cell specific (consistent with in vitro literature on neocortical interneuron subtypes). Supralinear summation may involve dendritic spikes, plausibly in interneurons with high densities of voltage-gated channels in distal dendrites. Recordings are from silicon probes spanning layers 2/3 and 5 of areas 24 and 32 in rat.

---

### Limitations & open questions

- Only a small minority of active neurons (approximately 10–25% of those within recording range) were isolated as single units; the silent majority prevents full characterisation of assembly composition and coordination.
- Monosynaptic interaction detection relies on indirect extracellular methods; cross-correlogram peaks between pyramidal cells are largely below detection threshold, so pyramidal-pyramidal dynamics remain unassessed.
- The jitter window (±5 ms) was chosen by judgment; the exact timescale at which co-modulation transitions from "broad" (rate-driven) to "fine" (synaptic) is not definitively resolved.
- Causal role of short-term plasticity in working memory is not established: the correlational evidence is consistent with a mechanistic role but does not rule out that synaptic dynamics are epiphenomenal to the observed assembly sequences.
- Whether the same dynamics operate in primate PFC, and how they relate to persistent-activity models of working memory (in which sustained firing, not sequential assembly transitions, maintains information), is not addressed.
- The supralinear coincidence effect was examined in a small number of satellite networks (n = 14); generality remains to be established.

---

### Connections & keywords

**Key citations**:
- Hebb, D.O. (1949) — The Organization of Behavior (cell assembly concept)
- Bartho et al. (2004) J. Neurophysiol. — physiological characterisation of pyramidal cells and interneurons by cross-correlogram
- Csicsvari et al. (1998) Neuron — pyramidal-interneuron synaptic reliability in behaving rat hippocampus
- Markram et al. (2004) Nat. Rev. Neurosci. — interneurons of the neocortical inhibitory system; in vitro short-term plasticity
- Mongillo, Barak & Tsodyks (2008) Science — synaptic theory of working memory
- Riehle et al. (1997) Science — spike synchrony and rate modulation in motor cortex
- Constantinidis, Williams & Goldman-Rakic (2002) Nat. Neurosci. — inhibition and temporal flow of information in PFC

**Named models or frameworks**:
- Hebbian cell assembly
- Synaptic theory of working memory (Mongillo et al.)
- Jitter-based resampling for monosynaptic detection
- Odour-based delayed match-to-sample task (figure-eight T-maze)

**Brain regions**:
- Medial prefrontal cortex (mPFC)
- Anterior cingulate cortex (area 24)
- Dorsal prelimbic cortex (area 32)

**Keywords**:
- short-term synaptic plasticity
- cell assemblies
- medial prefrontal cortex
- monosynaptic interactions
- cross-correlogram analysis
- working memory
- pyramidal-interneuron connectivity
- synaptic facilitation and depression
- coincidence detection
- jitter resampling
- silicon probe recording
- sparse coding
