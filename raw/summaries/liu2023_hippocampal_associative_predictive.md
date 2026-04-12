---
source_file: "liu2023_hippocampal_associative_predictive.md"
paper_id: "liu2023_hippocampal_associative_predictive"
title: "Associative and predictive hippocampal codes support memory-guided behaviors"
authors: "Can Liu, Ralitsa Todorova, Wenbo Tang, Azahara Oliva, Antonio Fernandez-Ruiz"
year: 2023
journal: "Science"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["linear_track"]
methods: ["optogenetics", "computational_modeling", "bayesian_decoding"]
brain_regions: ["hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "medial_entorhinal_cortex"]
frameworks: ["successor_representation"]
keywords: ["stachenfeld", "botvinick_and_gershman_2017_hippocampus_as_a_predictive_map_nat_neurosci", "el_gaby_et_al_2021_emergent_neural_coactivity_code_for_dynamic_memory_nat_neurosci", "wang_et_al_2015_theta_sequences_essential_for_internally_generated_hippocampal_firing_fields_nat_neurosci", "girardeau_et_al_2009_swr_suppression_impairs_spatial_memory_nat_neurosci", "jadhav_et_al_2012_awake_swrs_support_spatial_memory_science", "fernandez_ruiz_et_al_2017_entorhinal_ca3_dual_input_control_via_theta_gamma_coupling_neuron", "dragoi_and_buzsaki_2006_temporal_encoding_of_place_sequences_by_ca3_assemblies_neuron", "harvey_et_al_2023_hippocampo_cortical_circuits_for_memory_encoding", "routing", "and_replay_neuron", "oliva_et_al_2020_ca2_swrs_reactivate_social_memory_nature", "named_models_or_frameworks", "associative_code_predictive_code_distinction_this_papers_framework", "successor_representation_stachenfeld_et_al", "cognitive_map_okeefe_and_nadel", "theta_sequences", "sharp_waveripple_swr_replay", "spike_timing_dependent_plasticity_stdp_symmetric_ca3ca3_and_asymmetric_ca3ca1", "conditioned_place_preference_cpp_task"]
key_citations: ["stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

An optogenetic dissociation in rats shows that hippocampal cell-assembly coactivity (associative code) and sequential cell-assembly activation (predictive code) are mechanistically separable, with only the predictive code required for flexible memory-guided navigation and sequential replay.

---

### Background & motivation

The hippocampus supports both associative memory (binding features of experience) and predictive functions (generating internal models of state transitions to guide flexible behavior). Two prominent dynamic phenomena — synchronous coactivity of cell assemblies and temporally compressed sequential firing — have traditionally been viewed as inseparable aspects of the same underlying process. It remained unknown whether these represent distinct coding schemes with distinct behavioral roles, because no prior study had selectively disrupted one while preserving the other.

---

### Methods

- **Species and setup**: Adult male Long-Evans rats (n = 5 per task cohort); silicon probe recordings from dorsal CA1 during behavior and sleep.
- **Optogenetic perturbation**: AAV-mediated ChR2 expression in MEC GABAergic interneurons (mDlx promoter); 53 Hz blue-light entrainment of MEC GABAergic cells selectively disrupted medial gamma oscillations (gammaM, 60–110 Hz) in CA1 stratum lacunosum-moleculare while preserving theta power, theta phase modulation, CA3-driven slow gamma, and local fast gamma.
- **Experimental design**: Light delivered in one running direction on a linear track (Stim ON) but not the other (Stim OFF), creating within-session controls. Two additional behavioral tasks: cheeseboard maze (daily novel reward configurations requiring flexible navigation; n = 5 rats, ~33 Stim OFF and 11 Stim ON sessions) and conditioned place preference (CPP; context–reward associative learning; n = 5 rats).
- **Key measurements**: Place field formation and tuning, theta phase precession, theta sequences (Bayesian decoding; quadrant scores and weighted correlation), place field backward shift, sharp wave–ripple (SWR) detection, sequential replay scoring, cell-assembly detection (PCA/ICA), assembly reactivation strength, and explained variance in post-task sleep.
- **Computational model**: Spiking CA3–CA1 network (1,250 pyramidal + 100 interneurons per region; leaky integrate-and-fire) with asymmetric STDP (CA3→CA1) and symmetric STDP (CA3→CA3); Stim ON condition simulated by replacing phase-precessing theta component with phase-locking component, preserving coactivity but abolishing sequential order.

---

### Key findings

- **Selective disruption of the predictive code**: MEC GABAergic optogenetic perturbation abolished theta phase precession and theta sequences in the Stim ON direction without affecting place field formation, spatial information, population vector stability, or theta-cycle cofiring (P = 0.067 for cofiring difference between directions; theta compression slope impaired: P = 9 × 10⁻⁵).
- **Predictive map properties disrupted**: Experience-dependent increase in theta sequence look-ahead index and backward shift of place field centers-of-mass occurred only in the Stim OFF direction (backward COM shift OFF vs. ON: P = 1.3 × 10⁻⁶⁹ vs. P = 0.16); place field elongation near boundaries also disrupted in Stim ON.
- **Replay abolished, reactivation preserved**: Post-task sleep SWRs showed robust replay of Stim OFF trajectories (proportion significant replay improved: P = 7 × 10⁻¹¹; sequence scores: P = 3 × 10⁻¹⁷) but no above-chance replay for Stim ON trajectories (P = 0.29 for both metrics). Assembly reactivation strength increased significantly for both directions (Stim ON post-task vs. baseline: P = 0.0026); explained variance was similar across directions (P = 0.81). Reactivation and replay were correlated at the individual SWR level in Stim OFF (r = 0.11, P = 3 × 10⁻¹²) but not in Stim ON (r = −0.028, P = 0.06).
- **Pre-formed maps not disrupted**: When rats explored a linear track without perturbation first and then experienced Stim ON, replay of both trajectories was intact, confirming the perturbation specifically blocks encoding of the predictive map, not its subsequent readout.
- **Flexible navigation impaired, associative learning intact**: In the cheeseboard task, learning performance (distance ratio to optimal) was significantly worse in Stim ON sessions (F₁,₄₃ = 133.4, P < 10⁻¹⁰); memory recall at 2 h and 22 h was also impaired (P = 6.8 × 10⁻⁴ / 7.9 × 10⁻⁴). In the CPP task, both Stim OFF and Stim ON animals showed equivalent context–reward preference after pairing (Stim ON: P = 2.10 × 10⁻⁵), demonstrating the associative code is sufficient for contextual associative learning.
- **Circuit mechanism**: Computational modelling showed that asymmetric STDP at CA3→CA1 synapses (which requires consistent temporal ordering of pre- and postsynaptic spikes within theta cycles) mediates replay, while symmetric STDP at CA3→CA3 synapses (sensitive only to coactivity regardless of ordering) supports assembly reactivation — explaining the empirical dissociation.

---

### Computational framework

The paper uses a **Hebbian plasticity / spike-timing-dependent plasticity (STDP)** framework within a recurrent neural network (CA3–CA1 architecture). Two distinct STDP rules are proposed to implement the two codes:

- **Symmetric STDP** at CA3→CA3 recurrent synapses: strengthens connections between coactive cells regardless of firing order, implementing the associative code. This rule depends only on whether cells fire in the same theta cycle, not on their sequential ordering.
- **Asymmetric STDP** at CA3→CA1 feedforward synapses: requires consistent temporal ordering of spikes within theta cycles (i.e., phase precession) to potentiate directional connections. This rule encodes transitional structure and thus implements the predictive code.

Key variables: theta-cycle phase of each spike (determines eligibility for asymmetric STDP), synaptic weight matrices for CA3→CA3 and CA3→CA1 connections, and the downstream capacity of the CA1 network to generate sequential SWR replay. The framework assumes that offline replay is a consequence of the synaptic weights laid down during behavior, not an independently generated process.

---

### Prevailing model of the system under study

Prior to this paper, hippocampal coactivity (assembly formation and reactivation) and sequential activity (theta sequences, replay during SWRs) were widely considered to be two inseparable manifestations of the same underlying process — namely Hebbian strengthening of co-active place cells — mediated by common circuit and synaptic mechanisms. Both phenomena were assumed to depend on intact place cell expression and the same global network dynamics, making them empirically non-dissociable. The literature also contained two partially competing theories of hippocampal function: one centred on episodic/associative memory (O'Keefe, Eichenbaum) and one on predictive map generation (Stachenfeld et al. 2017; Buckner 2010), with no consensus on which aspects of hippocampal activity implement which function.

---

### What this paper contributes

The paper provides the first mechanistic and functional dissociation between coactivity and sequential codes in the hippocampus. It establishes that:

1. Assembly reactivation and sequence replay are not the same process and do not require the same mechanisms — the sequential order of firing during online experience, not merely the coactivity, is what drives replay.
2. The associative code (coactivity) is sufficient for some forms of episodic memory (context–reward associations) but not for flexible, trajectory-dependent navigation.
3. The predictive code (sequences) is specifically required for learning novel optimal routes and for the subsequent offline replay that presumably consolidates this knowledge.
4. Distinct STDP rules at CA3→CA3 (symmetric) and CA3→CA1 (asymmetric) synapses offer a plausible circuit-level mechanism for this dissociation.

This unifies previously competing accounts of hippocampal function by assigning each to a distinct dynamic code operating over the same cell populations.

---

### Brain regions & systems

- **CA1 (hippocampal output region)**: Primary recording site; the locus of the two coding schemes being dissociated. Phase precession, theta sequences, and SWR replay were measured here.
- **CA3 (hippocampal recurrent network)**: Modelled as the source of recurrent excitation driving both assembly coactivity (via CA3→CA3 STDP) and sequential replay (via CA3→CA1 STDP); CA3 inputs to CA1 are identified with slow gamma oscillations in stratum radiatum.
- **Medial entorhinal cortex (MEC)**: Targeted with optogenetics; MEC GABAergic cells entrain CA1 distal dendrites (stratum lacunosum-moleculare) through midfrequency gamma (gammaM, 60–110 Hz). MEC inputs provide the fine temporal structure (phase precession) enabling theta sequences. MEC optogenetic perturbation selectively disrupted gammaM while leaving CA3-driven slow gamma and local fast gamma intact.
- **Sharp wave–ripple (SWR) network**: Hippocampal-wide population bursts during which both reactivation (preserved under perturbation) and sequential replay (disrupted) occur; these were dissociated.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Criterion 1 — Algorithm**: The paper formalises distinct STDP algorithms at two sets of synapses (symmetric CA3→CA3; asymmetric CA3→CA1) as the computational substrate for the associative and predictive codes, respectively.

**Criterion 2 — Neural data**: In vivo optogenetic perturbation and silicon-probe recordings provide causal neural evidence that the fine temporal ordering of CA1 spikes within theta cycles (phase precession) — driven by MEC inputs — specifically supports theta sequences and subsequent replay, while theta-cycle cofiring (coactivity) is preserved and sufficient for assembly reactivation. The dissociation is replicated across two behaviorally distinct tasks.

**Marr's three levels:**

- **Computational**: The brain must both learn discrete states of the world (associative memory) and learn the transitional structure between states (predictive model). These are distinct computational problems that benefit from different solutions.
- **Algorithmic**: The associative code operates via synchronous coactivity of place cell assemblies within theta cycles, strengthened by symmetric Hebbian plasticity (order-independent). The predictive code operates via temporally ordered activation of assemblies across successive theta cycles (theta sequences / phase precession), strengthened by asymmetric STDP that encodes the direction of state transitions.
- **Implementational**: MEC GABAergic interneurons, acting via midfrequency gamma (60–110 Hz) in CA1 distal dendrites, provide the temporal scaffolding (phase precession) that enables asymmetric STDP at CA3→CA1 synapses. CA3 recurrent collaterals, operating through slow gamma in stratum radiatum, support symmetric STDP and thus assembly coactivity independently of MEC input timing. Local CA1 fast gamma and perisomatic inhibition are unaffected by the manipulation.

**Bonus — Implementational specificity**: The paper identifies distinct gamma sub-bands tied to distinct anatomical input layers (gammaF in pyramidal layer from local inhibition; gammaS in stratum radiatum from CA3; gammaM in stratum lacunosum-moleculare from MEC) as the physiological signature of each input's contribution, providing layer-resolved circuit evidence.

---

### Limitations & open questions

- **MEC pathway specificity**: The optogenetic manipulation targeted all MEC GABAergic cells, which project both directly (layers II/III) and indirectly (via dentate gyrus, CA3, CA2) to CA1. The relative contributions of these sub-pathways to theta sequence generation cannot be resolved.
- **Long-range MEC GABAergic projections**: A sparse subset of MEC GABAergic cells sends direct long-range projections to CA1; these may have been partly affected, though their sparsity limits their likely contribution.
- **Replay generation mechanisms**: The paper shows initial theta-sequence-dependent STDP is necessary for replay of novel trajectories, but other processes (preconfigured patterns, intrinsic CA3 dynamics) may also contribute and are not ruled out.
- **Generality beyond spatial tasks**: The behavioral dissociation is demonstrated in spatial paradigms. Whether the same distinction between associative and predictive codes applies to non-spatial episodic memory remains to be tested.
- **Non-REM specificity**: The model focuses on non-REM-like offline epochs; the contribution of REM sleep to either code was not examined.
- **Postnatal development**: The paper cites evidence that assembly reactivation precedes theta sequences and replay developmentally (PN17 vs. PN21), consistent with the proposed hierarchy, but this is not experimentally tested in the current study.

---

### Connections & keywords

**Key citations:**
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as a predictive map (Nat. Neurosci.)
- El-Gaby et al. (2021) — emergent neural coactivity code for dynamic memory (Nat. Neurosci.)
- Wang et al. (2015) — theta sequences essential for internally generated hippocampal firing fields (Nat. Neurosci.)
- Girardeau et al. (2009) — SWR suppression impairs spatial memory (Nat. Neurosci.)
- Jadhav et al. (2012) — awake SWRs support spatial memory (Science)
- Fernández-Ruiz et al. (2017) — entorhinal-CA3 dual-input control via theta-gamma coupling (Neuron)
- Dragoi & Buzsáki (2006) — temporal encoding of place sequences by CA3 assemblies (Neuron)
- Harvey et al. (2023) — hippocampo-cortical circuits for memory encoding, routing, and replay (Neuron)
- Oliva et al. (2020) — CA2 SWRs reactivate social memory (Nature)

**Named models or frameworks:**
- Associative code / predictive code distinction (this paper's framework)
- Successor representation (Stachenfeld et al.)
- Cognitive map (O'Keefe & Nadel)
- Theta sequences
- Sharp wave–ripple (SWR) replay
- Spike-timing-dependent plasticity (STDP) — symmetric (CA3→CA3) and asymmetric (CA3→CA1)
- Conditioned place preference (CPP) task
- Cheeseboard maze task

**Brain regions:**
- CA1 (hippocampus)
- CA3 (hippocampus)
- Medial entorhinal cortex (MEC)

**Keywords:**
- hippocampal place cells
- theta sequences
- sharp wave–ripples
- memory replay
- cell assembly reactivation
- predictive coding
- associative memory
- spike-timing-dependent plasticity
- phase precession
- optogenetics
- MEC GABAergic interneurons
- theta-gamma coupling
