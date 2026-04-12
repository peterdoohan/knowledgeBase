---
source_file: bouhadjar2022_coherent_noise_sequence_replay.md
paper_id: bouhadjar2022_coherent_noise_sequence_replay
title: "Coherent noise enables probabilistic sequence replay in spiking neuronal networks"
authors:
  - "Younes Bouhadjar"
  - "Dirk J. Wouters"
  - "Markus Diesmann"
  - "Tom Tetzlaff"
year: 2022
journal: "bioRxiv (preprint, June 2022)"
paper_type: computational
contribution_type: theoretical
keywords:
  - probabilistic_sequence_replay
  - coherent_noise_correlated_noise
  - winner_take_all_competition
  - population_encoding
  - noise_averaging
  - exploration_exploitation_trade_off
  - probability_matching
  - shared_synaptic_input_correlation
  - spatiotemporal_oscillations_travelling_cortical_waves
  - dendritic_action_potentials
  - spiking_neural_network
  - decision_strategies_under_ambiguity
  - coherent
  - noise
  - enables
  - probabilistic
  - sequence
  - replay
  - spiking
  - neuronal
---

### One-line summary

Locally correlated (coherent) noise — implemented as shared synaptic background inputs or random stimulus locking to spatiotemporal oscillations — enables a spiking neural network to switch between deterministic exploitation and probabilistic sequence replay strategies, while uncorrelated noise of any amplitude cannot achieve this due to population-level averaging.

---

### Background & motivation

Sequential memory recall in the face of ambiguous cues requires a mechanism that can flexibly select among multiple learned sequences according to their prior frequencies of occurrence. Previous spiking network models of sequence learning either deterministically replay the most frequent sequence or rely on uncorrelated noise to generate stochasticity — but uncorrelated noise averages out when decisions are encoded by populations of neurons, leaving recall effectively deterministic. This paper addresses how biologically plausible, locally coherent noise can overcome this averaging problem and enable a continuum of decision strategies ranging from maximisation (always replaying the most frequent sequence) through probability matching (replay frequency equals training frequency) to full exploration (uniform random replay).

---

### Methods

- **Base model**: The spiking temporal-memory (TM) model from Bouhadjar et al. (2021), extended to include a single inhibitory neuron mediating winner-take-all (WTA) competition between excitatory subpopulations. Network: 1200 excitatory LIF neurons divided into M=8 subpopulations (150 neurons each), plus 1 inhibitory LIF neuron. Sparse random recurrent EE connectivity (in-degree K=240, p=0.2).
- **Neuron model**: Leaky integrate-and-fire with nonlinear dendritic integration — dendritic action potentials (dAPs) triggered when dendritic current exceeds threshold, producing a plateau depolarisation that advances somatic firing.
- **Plasticity**: Homeostatic STDP on EE synapses only; plasticity disabled during replay.
- **Training protocol**: Repeated presentation of 2–3 overlapping sequences sharing the same first two elements (ambiguous cue). Each sequence shown with a specified relative frequency p. Network learns sequence-specific subnetworks with weight asymmetry proportional to training frequencies.
- **Replay conditions**: Ambiguous cue presented for N_t=150 trials. Three noise conditions tested: (1) noise-free; (2) uncorrelated Poissonian background input (σ=15 pA, c=0); (3) correlated Poissonian background input (σ=15 pA, c=1, shared presynaptic sources within each subpopulation).
- **Oscillatory noise**: Second noise mechanism — sinusoidal current injected into subpopulations with subpopulation-specific random phases, and stimulus onset times randomly drawn relative to the oscillation. Tested at f = 10, 30, 70 Hz and amplitudes a = 0, 8, 16 pA.
- **Performance measure**: Replay frequency of each sequence (and subsets) across trials as a function of training frequency p. Also monitored: failure rate (no sequence replayed) and joint replay rate (both sequences replayed simultaneously).
- **Simulations**: NEST 3.0 neural simulator; NESTML for neuron model implementation; 5 independent network realisations per condition.

---

### Key findings

- **Without noise**, the network deterministically replays only the highest-frequency sequence for all training frequencies except near p=0.5, where occasional simultaneous replay occurs. This arises because weight asymmetry produces a shorter response latency for the dominant subpopulation in every trial.
- **Uncorrelated noise** (c=0) does not enable exploration regardless of amplitude. Due to population averaging, the across-trial variance of population response latency vanishes for large ρ. Increasing uncorrelated noise amplitude instead breaks the WTA mechanism and increases failure/simultaneous-replay rates without producing probability matching.
- **Correlated noise** (c=1, shared inputs within each subpopulation) broadens the response latency distributions and produces trial-to-trial variability that allows the less-frequent sequence to be replayed occasionally. With σ=15 pA and c=1, replay frequencies closely match training frequencies (probability matching).
- **Strategy control**: Increasing noise amplitude (with c fixed) shifts replay from max-prob → probability matching → full exploration. Increasing correlation level (with σ fixed) similarly shifts from non-explorative to explorative dynamics.
- **Multiple sequences**: The model generalises to three competing sequences (training frequencies 0.2, 0.5, 0.3); probability matching is achieved with σ=15 pA, c=1.
- **Oscillatory noise**: Random stimulus locking to sinusoidal background oscillations replicates the full range of strategies (max-prob to probability matching) across physiological frequencies (alpha 10 Hz, beta 30 Hz, gamma 70 Hz). Higher oscillation frequencies produce weaker exploratory effects due to low-pass neuronal filtering. This mechanism is proposed as more biologically plausible than shared-input correlation because it requires only spatial proximity (matching oscillation phase) rather than high anatomical overlap between presynaptic inputs.
- **Noise correlations are essential for WTA robustness**: Correlated noise promotes within-trial synchrony, enabling the winning subpopulation to reliably trigger inhibition and preventing spurious simultaneous replay. Thus coherent noise simultaneously enables exploration and maintains replay fidelity.

---

### Computational framework

**Framework**: Spiking neural network / population coding / winner-take-all competition / noise-driven probabilistic computation.

**Core formalism**: The network implements sequence storage via Hebbian (STDP + homeostasis) weight modification. After learning, context-specific subnetworks are formed. During replay, competing subpopulations race to trigger the global inhibitory neuron (WTA). The key quantity is the population-averaged response latency t = (1/ρ) Σ t_{s,i}, whose across-trial variance v depends on population size ρ, single-neuron spike-time variance v_s, and spike-time correlation c_s:

v = v_s/ρ · (1 + (ρ−1)·c_s)

For c_s=0, v → 0 as ρ → ∞ (noise averaging). For c_s > 0, v remains finite and proportional to c_s·v_s, enabling explorative behavior without requiring large noise amplitudes.

**Key assumptions**: Population encoding (decisions made from ensemble activity, not single spikes); within-subpopulation correlation is the relevant noise parameter; across-subpopulation noise is uncorrelated; WTA mediated by a single fast inhibitory neuron.

---

### Prevailing model of the system under study

The paper builds on a prior consensus that spiking network models of sequence learning (Klampfl & Maass 2013; Klos et al. 2018; Maes et al. 2020; Bouhadjar et al. 2021) can learn and replay sequences via STDP, but that decision-making under ambiguity in such networks is either deterministic (replay the most frequent sequence) or requires stochastic neural dynamics. The predominant assumption in the field is that single-neuron or synaptic noise — typically modelled as uncorrelated Poissonian background input or synaptic stochasticity — is sufficient to generate explorative behavior. The paper's own introduction signals this as the prevailing approach (citing Buesing et al. 2011; Legenstein & Maass 2014; Hartmann et al. 2015; Neftci et al. 2016; Jordan et al. 2019), and the Bouhadjar et al. (2021) predecessor model itself was deterministic and always replayed the highest-frequency sequence. The theoretical problem of noise averaging in population-coded models was raised by Dold et al. (2019) but not previously resolved with a biologically plausible noise mechanism in a sequence context.

---

### What this paper contributes

The paper establishes that **noise correlation structure, not noise amplitude, is the critical parameter** for enabling probabilistic recall in population-coded spiking networks. It provides a formal derivation of why uncorrelated noise cannot achieve exploration in population-encoded systems (the averaging argument), and then demonstrates two biologically plausible solutions: (1) shared synaptic inputs within a subpopulation, and (2) random stimulus locking to spatiotemporal oscillations (travelling waves). The oscillation mechanism in particular is novel — it repurposes a widely observed cortical phenomenon (travelling waves, coherent oscillations) as a controllable source of locally coherent noise. The model also explains how a single circuit can flexibly switch between exploitation and exploration by modulating noise amplitude or frequency, offering a potential mechanistic account of the exploration-exploitation trade-off observed behaviourally. Before this work, there was no concrete spiking network model showing how probability matching or tunable exploration could arise from coherent network activity during sequence replay.

---

### Brain regions & systems

Not applicable in the strict sense — the paper does not commit to a specific anatomical instantiation. However, the model is implicitly framed as a model of cortical sequence processing circuits, and the paper makes contact with the following:

- **Neocortex (generic)** — the model's architecture (E/I populations, sparse random connectivity, STDP, dendritic nonlinearities) is intended as a generic cortical microcircuit model for sequence storage and replay.
- **Cortical travelling waves / spatiotemporal oscillations** — proposed as the natural substrate for the oscillatory coherent noise mechanism; cited evidence includes travelling waves in visual and motor cortex (Sato et al. 2012; Takahashi et al. 2015; Nauhaus et al. 2009).
- **Frontal/decision-making areas** — referenced obliquely via the exploration-exploitation literature (Daw et al. 2006: BOLD signal in decision cortex during exploration). Neuromodulatory control of noise amplitude is mentioned as a biologically plausible control mechanism.

---

### Mechanistic insight

The paper does **not** meet the bar for this section. It is a purely computational modelling study: it proposes and formalises an algorithm (coherent-noise-driven probabilistic WTA) but provides no neural data (recordings, imaging, lesion, pharmacology) that specifically support this algorithm over alternatives. The paper does not report any empirical neural measurements.

The model nonetheless makes a clear mechanistic proposal at two levels:
- **Computational**: the brain solves the exploration-exploitation trade-off in sequential recall by tuning the correlation structure of background input noise.
- **Algorithmic**: within-subpopulation correlated noise broadens the latency distribution of competing populations, allowing the WTA to sometimes select the lower-weight (less frequent) option; the degree of exploration is parametrically controlled by noise correlation and amplitude.

Implementational-level evidence linking these processes to specific cell types, connectivity motifs, or neuromodulators is speculative and not empirically validated in this paper.

---

### Limitations & open questions

- The shared-input correlation mechanism requires c ≈ 1 (near-perfect correlation) to achieve probability matching, which is anatomically implausible given the low connection probabilities in local cortical circuits (~20% here, yet requiring nearly all inputs to be shared within a subpopulation).
- The oscillatory noise mechanism requires neurons within the same subpopulation to share identical oscillation phase. The paper assumes this is warranted by spatial proximity but does not demonstrate it for realistic cortical topographies or in empirical data.
- The model uses a single global inhibitory neuron, which is a simplification of real cortical inhibitory circuits; this may affect the generality of the WTA dynamics.
- Plasticity is disabled during replay — the interaction between ongoing learning and probabilistic replay is not explored.
- The model does not address the neural origin of the control signal that adjusts noise amplitude or correlation (e.g., which neuromodulatory system, what triggers exploration vs. exploitation, how this is timed relative to decisions).
- The model assumes fixed sequences with a predetermined ambiguous cue; generalisation to partially ambiguous or noisy stimuli is not investigated.
- The link between this abstract model and specific decision-making paradigms (e.g., two-armed bandit, sequential prediction tasks) is illustrative rather than quantitatively fitted to behavioural data.

---

### Connections & keywords

**Key citations**:
- Bouhadjar et al. (2021) — predecessor temporal memory (TM) model (ArXiv)
- Legenstein & Maass (2014) — population-based probabilistic inference with spiking noise
- Dold et al. (2019) — noise averaging problem in deterministic networks
- Jordan et al. (2019) — deterministic networks for probabilistic computing
- Buesing et al. (2011) — neural dynamics as sampling
- Klampfl & Maass (2013) — STDP-based sequence learning
- Sato et al. (2012) — travelling waves in visual cortex
- Daw et al. (2006) — cortical substrates for exploration (BOLD)
- Cohen et al. (2007) — exploration-exploitation trade-off
- Kriener et al. (2008) — shared-input correlations in cortical networks

**Named models or frameworks**:
- Spiking temporal-memory (TM) model (Bouhadjar et al. 2021)
- Winner-take-all (WTA) circuit
- Leaky integrate-and-fire (LIF) neuron model with dendritic action potentials (dAPs)
- Homeostatic spike-timing-dependent plasticity (STDP)
- NEST neural simulator; NESTML modelling language

**Brain regions**:
- Neocortex (generic cortical microcircuit, not anatomically specified)
- Cortical regions exhibiting travelling waves (visual cortex, motor cortex; referenced, not directly modelled)

**Keywords**:
- probabilistic sequence replay
- coherent noise / correlated noise
- winner-take-all competition
- population encoding
- noise averaging
- exploration-exploitation trade-off
- probability matching
- shared synaptic input correlation
- spatiotemporal oscillations / travelling cortical waves
- dendritic action potentials
- spiking neural network
- decision strategies under ambiguity
