---
source_file: "george2022_stdp_predictive_maps.md"
paper_id: "george2022_stdp_predictive_maps"
title: "Rapid learning of predictive maps with STDP and theta phase precession"
authors: "Tom M George, William de Cothi, Kimberly Stachenfeld, Caswell Barry"
year: 2022
journal: "bioRxiv (preprint)"
paper_type: "computational"
contribution_type: "theoretical"
tasks: ["open_field", "foraging_task"]
methods: ["electrophysiology"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "striatum", "nucleus_accumbens"]
frameworks: ["reinforcement_learning", "successor_representation", "temporal_difference_learning"]
keywords: ["rapid", "learning", "predictive", "maps", "stdp", "theta", "phase", "precession"]
key_citations: ["dayan1993_successor_representation", "momennejad2018_offline_replay_planning"]
---

### One-line summary

Spike-timing dependent plasticity (STDP) acting on theta-compressed spike sequences is sufficient to rapidly learn an accurate approximation to the successor representation in a biologically plausible hippocampal model.

---

### Background & motivation

The successor representation (SR) is a leading candidate principle for hippocampal function, proposing that place cells encode the expected future discounted occupancy of locations. It is typically formalised as being learned via temporal difference (TD) learning, yet there is no clear evidence that TD learning is implemented in hippocampal circuits. Meanwhile, hippocampal STDP and theta phase precession are well-established biological phenomena whose computational roles in learning predictive maps have not been formally reconciled. This paper addresses the gap by asking whether STDP, acting on theta-compressed trajectories ("theta sweeps"), can implement SR learning without recourse to error-driven TD updates.

---

### Methods

- **Model architecture**: Spiking network comprising N CA3 "basis feature" place cells (thresholded Gaussian receptive fields, σ = 1 m, peak 5 Hz) driving N CA1 "STDP successor feature" cells via a learnable synaptic weight matrix W_ij.
- **Phase precession**: Implemented via a Von Mises modulation of firing rate at each theta cycle (10 Hz), with preferred phase advancing as the animal traverses each place field; parameters fitted to Jeewajee et al. (2014) electrophysiology.
- **STDP rule**: Asymmetric Hebbian rule with τ_pre = 20 ms, τ_post = 40 ms, a_post = −0.4 (matched to Bi & Poo, 1998); pre-before-post potentiates, post-before-pre depresses.
- **Baseline comparison**: TD learning applied to the same CA3 basis features, yielding a ground-truth "TD successor matrix" M_ij; element-wise Pearson R² used to quantify approximation quality.
- **Environments tested**: 1D circular loop (biased policy), 1D corridor (unbiased policy), 2D two-room open-field maze (foraging policy with wall and doorway biases).
- **Multiscale extension**: Three populations of differently sized place cells (σ = 0.5, 1.0, 1.5 m) tested with homogeneous vs. dorso-ventral ordered distributions to examine cross-scale STDP binding.
- **Hyperparameter sweep**: Grid search over STDP parameters (τ_pre, τ_post, a_post, firing rate) to determine whether biological values are near-optimal.

---

### Key findings

- STDP with theta phase precession learns a weight matrix W_ij that closely approximates the TD successor matrix: R² = 0.87 on the 1D loop (biased), R² = 0.88 on the 1D corridor (unbiased), R² = 0.74 on the 2D two-room maze.
- Theta phase precession is essential for capturing behavioural policy bias: removing it reduces R² from 0.87 to 0.63 on the loop and abolishes the characteristic asymmetry (ratio of mass either side of diagonal: 4.54 with vs. 0.99 without phase precession).
- Phase precession accelerates learning: time to reach 75% of final R² is ~5 min with theta sweeps vs. ~10.5 min without (1D loop).
- STDP successor features reproduce hallmark SR phenomena: backward skewing of place fields on biased tracks (STDP peak shift −0.38 ± 0.03 m, skewness −0.24 ± 0.07; TD: −0.28 m, −0.39), elongation of fields parallel to walls in 2D (near-wall eccentricity 0.57 vs. 0.33 for centre cells), and clustering/expansion of fields toward doorways.
- Hyperparameter sweep confirms biological STDP parameters (Bi & Poo, 1998) are near-optimal for SR approximation; only peak firing rate shows monotonic improvement beyond biological values.
- Homogeneously mixed multiscale place cells cause STDP cross-scale binding that overwrites short-timescale SR with long-timescale representations; segregating field sizes along the dorso-ventral axis prevents this, preserving distinct multiscale successor features.
- Cells without theta phase precession (a subset of CA3 neurons) may learn a policy-independent "default" SR, while theta-precessing cells learn the on-policy SR — giving the animal simultaneous access to both representations.

---

### Computational framework

**Successor representation / reinforcement learning**, extended to continuous time and space.

The paper models hippocampal place cells as computing a continuous-time successor feature: the expected future discounted firing rate of a CA3 basis feature, integrated over trajectories from the current position with exponential temporal discount τ (set to 4 s). Formally, ψ_i(x) = E[∫₀^∞ e^(−t/τ) f_i(x(t)) dt | x(0) = x]. The synaptic weight matrix W_ij between CA3 and CA1 is shown to converge, under STDP with theta-modulated spiking, to an approximation of the TD successor matrix M_ij. Key assumptions: (1) place cell basis features are overlapping Gaussians (required for STDP to form associations); (2) theta sweeps compress behavioural sequences to the millisecond timescale of STDP; (3) learning and recall are temporally segregated (weights frozen during post-learning recall).

---

### Prevailing model of the system under study

The introduction presents two leading frameworks for hippocampal spatial coding. The dominant view is the "cognitive map" hypothesis (O'Keefe & Nadel 1978; Tolman 1948): place cells represent current self-location, and their population code provides a metric for flexible navigation. A more recent refinement is the **predictive map / successor representation** hypothesis (Stachenfeld, Botvinick & Gershman, 2017): place cells encode not just current position but expected future occupancy, accounting for phenomena like experience-dependent place field skewing and policy-dependent remapping. Within the SR framework, the prevailing learning mechanism is TD learning — which has empirical support in striatum (dopaminergic RPE signals) but whose implementation in hippocampus is unclear. There is no established account of how STDP, which operates on millisecond timescales, could learn temporal associations spanning seconds-long behavioural episodes. Theta phase precession is known to compress spatial sequences onto the theta timescale, but its role in enabling SR learning had not been formally demonstrated.

---

### What this paper contributes

This paper provides the first formal demonstration that STDP acting on theta-compressed spike trains is sufficient to approximate the successor representation without requiring TD learning or an explicit error signal. Specifically, it shows:

1. A biologically grounded STDP rule with experimentally matched parameters achieves ~87% explained variance of the true TD successor matrix in 1D and ~74% in 2D — comparable to TD learning itself.
2. Phase precession is not merely helpful but mechanistically necessary: it encodes the current policy in the relative ordering of spikes within a theta cycle, which is what allows STDP to learn a *policy-biased* SR rather than a symmetric (default/diffusive) one.
3. The dorso-ventral gradient of place field sizes, previously explained in terms of cognitive or anatomical factors, is here shown to have a functional necessity: it prevents STDP from collapsing multiscale SR representations into a single long-timescale representation.
4. The model provides a unified account of several SR-consistent experimental observations (field skewing, wall elongation, doorway clustering) within a single biologically plausible learning mechanism.
5. The finding that biological STDP parameters are near-optimal for SR approximation is used to argue that hippocampal plasticity rules may have evolved specifically to enable rapid predictive map learning.

---

### Brain regions & systems

- **CA3** — source of "basis feature" place cells; encodes current position via overlapping Gaussian firing fields; proposed to provide the population code over which the successor representation is built.
- **CA1** — site of "STDP successor features"; receives input from CA3 via plastic synapses; proposed to compute downstream successor representation through STDP-driven synaptic weight modification.
- **Hippocampus (dorsal-ventral axis)** — topographic gradient of place field sizes (small dorsal, large ventral); argued to be functionally necessary to segregate short- vs. long-timescale successor representations and prevent cross-scale STDP binding.
- **Striatum / nucleus accumbens** — mentioned as the putative site of TD/RPE learning (dopaminergic reward prediction error); contrasted with hippocampus as the site of SR learning in this model.
- **Entorhinal cortex** — briefly noted as providing grid-cell-based spatial metric; not directly modelled.

---

### Mechanistic insight

The paper meets both criteria for the high bar.

**Criterion 1 — Algorithm**: The paper formalises an algorithm: STDP acting on theta-phase-precessing spiking place cells computes an approximation to the continuous-time successor representation. The mechanism is precisely specified — within each theta cycle, spikes from place cells along the current trajectory are ordered by the phase precession rule, so that pre-before-post timing (potentiation) reliably encodes the direction of travel, yielding the characteristic forward-skewed weight structure of the SR.

**Criterion 2 — Neural data supporting the algorithm over alternatives**: The model's predictions are validated against published electrophysiology. Key empirical constraints used as model targets or tests: (a) backward skewing of CA1 place fields on biased tracks (Mehta et al., 2000); (b) greater skewing in CA1 than CA3 (Dong et al., 2021); (c) elongation of place fields near walls (Tanni et al., 2021); (d) clustering near doorways (Spiers et al., 2015); (e) STDP parameters matched to Bi & Poo (1998) culture data; (f) phase precession parameters fitted to Jeewajee et al. (2014) in vivo recordings; (g) place cell size gradient along dorso-ventral axis (Kjelstrup et al., 2008). The paper also makes a novel testable prediction: theta power should increase in novel environments because phase precession is required for SR learning, consistent with observed theta enhancement on novelty (Cavanagh et al., 2012).

**Marr's three levels:**

- **Computational**: The brain must represent the expected future structure of the agent's environment to support flexible, reward-adaptive navigation — i.e. it must compute a predictive map (successor representation) encoding expected future state occupancy discounted over time.
- **Algorithmic**: Place cells implement successor features as linear combinations of CA3 basis features. STDP on theta-modulated spike trains uses the temporal ordering of spikes within theta cycles as a proxy for the ordering of locations along the current trajectory, updating synaptic weights W_ij toward the TD successor matrix M_ij without an explicit error signal.
- **Implementational**: Theta oscillations (10 Hz LFP) modulate CA3 place cell firing via phase precession, compressing behavioural sequences to the 20–40 ms STDP window. Asymmetric STDP (τ_pre = 20 ms, τ_post = 40 ms; a_post = −0.4) at CA3→CA1 synapses implements the learning rule. The dorso-ventral size gradient of place fields serves as a physical barrier preventing cross-scale synaptic binding, preserving multiscale SR representations across hippocampal subregions.

**Bonus — physical implementation**: The paper maps the model onto specific cell types (CA3 pyramidal cells as basis features, CA1 pyramidal cells as successor features), specific synaptic pathways (Schaffer collaterals), a specific neuromodulatory oscillation (hippocampal theta), and a specific biophysical learning rule (STDP). It further proposes a role for the subset of non-phase-precessing CA3 neurons in learning a policy-independent default SR.

---

### Limitations & open questions

- The STDP successor features do not converge analytically to the true TD successor features; the approximation may introduce errors in downstream value computation.
- The model assumes distinct encoding and retrieval phases (synaptic weights are frozen during recall), but the mechanism enforcing this separation is not modelled.
- Phase precession is implemented as a simple Von Mises modulation; more complex empirical properties of phase precession (e.g., variability across environments, dependence on running speed) are not fully captured.
- The model does not include feedback from CA1 to CA3 or interactions with other hippocampal subregions (CA2, DG, subiculum) or neocortex.
- Reward learning (the R_j weights needed to compute the value function) is not modelled; the paper explicitly treats this as a separate, downstream process.
- The paper does not address how the SR is updated upon sudden environmental change (e.g., blocked routes) — only steady-state exploration is modelled.
- It remains unclear whether cells lacking phase precession genuinely learn a default policy SR, as the paper describes this as a proposal rather than a tested result.
- The prediction that theta suppression during novel exploration impairs subsequent navigation has not been directly tested in this paper.

---

### Connections & keywords

**Key citations**:
- Stachenfeld, Botvinick & Gershman (2017) — "The hippocampus as a predictive map" (Nature Neuroscience); the primary model this paper extends and provides a learning rule for.
- Dayan (1993) — original successor representation paper (Neural Computation).
- Bi & Poo (1998) — STDP rule parameters (Journal of Neuroscience).
- O'Keefe & Recce (1993) — theta phase precession discovery (Hippocampus).
- Skaggs et al. (1996) — theta sequence compression (Hippocampus).
- Mehta, Quirk & Wilson (2000) — experience-dependent place field skewing (Neuron).
- Kjelstrup et al. (2008) — dorso-ventral place field size gradient (Science).
- Momennejad & Howard (2018) — multiscale successor representations (bioRxiv).
- de Cothi & Barry (2020) — neurobiological successor features (Hippocampus).
- Bono et al. (2021) — concurrent Hebbian SR model with spiking neurons (bioRxiv).
- Jeewajee et al. (2014) — theta phase precession in open environments (Phil Trans R Soc B).

**Named models or frameworks**:
- Successor representation (SR) / predictive map hypothesis
- Temporal difference (TD) learning
- Spike-timing dependent plasticity (STDP)
- Theta phase precession / theta sweep
- Continuous-time successor features (Doya, 2000 formalism)
- Multiscale successor representations

**Brain regions**:
- CA3, CA1, hippocampus (dorsal-ventral axis), striatum/nucleus accumbens, entorhinal cortex

**Keywords**:
- successor representation, predictive map, STDP, theta phase precession, theta sweep, place cells, CA3-CA1 synaptic plasticity, Hebbian learning, dorso-ventral hippocampal axis, multiscale spatial representation, reinforcement learning, biologically plausible learning
