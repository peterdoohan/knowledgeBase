---
source_file: nadasdy1999_hippocampal_spike_sequence_replay.md
title: "Replay and Time Compression of Recurring Spike Sequences in the Hippocampus"
authors: Zoltán Nádasdy, Hajime Hirase, András Czurkó, Jozsef Csicsvari, György Buzsáki
year: 1999
journal: The Journal of Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal CA1 pyramidal cell spike sequences recorded during active wheel-running are replayed in a time-compressed form during subsequent slow-wave sleep, specifically during sharp-wave ripple events, at above-chance rates, providing direct evidence for experience-dependent sequence reactivation.

---

### Background & motivation

The hippocampus is known to encode spatial experience through the sequential firing of place cells, and it had been proposed — but not rigorously demonstrated at the level of precise multi-neuron spike sequences — that these sequences are subsequently reactivated during sleep to support memory consolidation. Prior work by Wilson and McNaughton (1994) and Skaggs and McNaughton (1996) had shown increased pairwise correlations between co-active place cells during post-experience sleep, but pairwise cross-correlograms cannot resolve the full temporal structure of multi-neuron sequences. This paper addresses that gap by developing and applying methods capable of detecting and characterising repeating spatiotemporal spike sequences in parallel recordings, and asking whether behaviorally-acquired sequences reappear during sleep beyond what chance coincidences predict.

---

### Methods

- **Subjects and recording**: 18 Sprague-Dawley rats; tetrodes or silicon electrode arrays implanted in CA1 pyramidal layer; 6 rats trained on a wheel-running task.
- **Task design**: Three-session design — Sleep1 (home cage, pre-run), Run (wheel-running for water reward), Sleep2 (home cage, post-run). 4–13 simultaneously recorded pyramidal cells per dataset.
- **Sequence detection — template-matching method**: Modified sliding-sweeps algorithm. Templates defined by spike identity and timing within a 200 ms window; a match required spikes within 10–20 ms tolerance. Significance assessed by Monte Carlo comparison against 100 surrogate spike trains.
- **Sequence detection — joint probability map (JPM) method**: Detected repeating spike triplets within a predefined window; constructed a difference map by subtracting expected triplet rates (estimated from pairwise cross-correlograms) from observed triplet rates; significance by Fisher's exact test.
- **Spike shuffling controls**: Four shuffling procedures used — within-train ISI shuffling, temporal spike displacement (0–50 ms), across-train shuffling, and theta-phase-invariant shuffling — to preserve progressively more of the population dynamics while eliminating temporal correlations of interest.
- **EEG analysis**: Power spectra computed around short (<50 ms) and long (>100 ms) spike sequences to determine EEG correlates (ripple vs. theta bands).

---

### Key findings

- Repeating spike sequences occurred in every animal tested (n = 5) and exceeded chance levels under all four shuffling methods (p < 0.01), ruling out Poisson coincidence, theta phase locking, or elevated firing rate as sole explanations.
- Both the template-matching and JPM methods converged on detecting the same sequences from the same datasets.
- Short sequences (<50 ms) were associated with elevated power in the ripple band (140–200 Hz); long sequences (>100 ms) were associated with elevated theta power — indicating that theta-timescale sequences are replayed at compressed, ripple timescales during slow-wave sleep.
- In two rats with stable recordings across all three sessions: 9% of triplets were shared between Run and Sleep2 (vs. 5% between Sleep1 and Run; χ²(2) = 21.58, p < 0.01), and the number of significant pixels of common triplets correlated significantly between Run and Sleep2 (Pearson r = 0.737, p < 0.001).
- Sleep1 triplet patterns were independent of both Run and Sleep2 patterns, confirming that the increased overlap is experience-dependent rather than a baseline property.
- Pyramidal cell participation probability in SPW events was non-uniform (2–40%) and predicted by individual firing rate during theta (r = 0.59, p < 0.0001), suggesting structured rather than random SPW recruitment.

---

### Computational framework

The paper does not employ a formal computational model, but it is framed within Buzsáki's (1989) two-stage memory consolidation hypothesis. The implicit framework is:

- **Stage 1 (encoding)**: During theta-associated waking behaviour, information is encoded in CA3 recurrent and Schaffer collateral synapses via synaptic plasticity driven by sequential place cell activation.
- **Stage 2 (consolidation)**: During slow-wave sleep, the CA3 network switches to a SPW-burst state in which previously potentiated circuits are spontaneously reactivated, replaying sequences at ~7× compression within ripple oscillations.

The time-compression ratio (theta timescale ~200 ms replayed within SPW/ripple timescale ~20–50 ms) is consistent with the NMDA receptor time constant for Hebbian synaptic modification, suggesting the replay serves to bring temporally discontiguous experience-related neurons within the plasticity window.

---

### Prevailing model of the system under study

The prevailing model at the time held that the hippocampus encodes spatial experience via the sequential activation of place cells during theta-associated exploration, and that some form of offline reactivation occurred during subsequent sleep. Wilson and McNaughton (1994) had provided correlational evidence for increased pairwise co-activation during post-sleep. Buzsáki (1989) had proposed a two-stage model where sharp-wave bursts during slow-wave sleep replay hippocampal activity to transfer information to neocortex. However, it had not been established that multi-neuron spatiotemporal sequences — not just pairwise correlations — recur above chance during sleep, nor that these sequences constitute time-compressed versions of the waking sequences rather than structurally similar but independently generated patterns.

---

### What this paper contributes

This paper provides the first direct evidence that multi-neuron spike sequence structure (not merely pairwise correlation) is preserved from waking experience into post-experience slow-wave sleep at above-chance rates. Crucially, it demonstrates that:

1. The replayed sequences are time-compressed versions of waking theta-timescale sequences, and that this compression is specifically associated with the sharp-wave ripple complex.
2. The increase in shared sequences is experience-dependent: pre-experience sleep does not predict waking sequence structure, but post-experience sleep does.

Before this paper, it could only be said that pairs of cells with overlapping place fields tended to co-fire more during subsequent sleep. After this paper, it can be said that the precise temporal ordering of multi-neuron assemblies observed during theta behaviour re-emerges during SPW-ripple events at a compressed timescale — a finding consistent with, and substantially strengthening, the two-stage consolidation model.

---

### Brain regions & systems

- **Hippocampal CA1** — primary recording site; source of pyramidal cell place-selective sequences and sharp-wave ripple events.
- **Hippocampal CA3** — proposed origin of SPW bursts (cited as mechanistic basis; not directly recorded here); proposed site of associative memory encoding in recurrent collaterals.
- **Entorhinal cortex** — discussed as downstream target of CA1 SPW output and potential source of hippocampal drive; cited to argue that SPWs are internally generated (entorhinal lesion increases SPW incidence).

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Hippocampal CA1 place cell sequences acquired during theta-associated wheel-running are replayed during slow-wave sleep sharp-wave events at compressed timescales.

- **Computational level**: The brain solves the credit-assignment problem for episodic memory by replaying recently experienced event sequences offline, enabling Hebbian plasticity between neurons that were active at different times during the original experience (too separated in time to co-activate NMDA receptors during learning).
- **Algorithmic level**: Spatiotemporal spike sequences — multi-neuron orderings extending over ~200 ms during theta — are recapitulated in compressed form (~20–50 ms) during SPW-ripple bursts. The compression brings the sequence within the NMDA receptor time constant, enabling synaptic strengthening between sequence members. The JPM and template-matching analyses operationalise this as the recurrence of triplet and higher-order patterns above Poisson baselines, with the Run→Sleep2 increase (vs. stable Sleep1 baseline) confirming experience-dependence.
- **Implementational level**: The paper links short replayed sequences specifically to ripple-frequency (140–200 Hz) local field power and long waking sequences to theta-frequency power, directly associating the two sequence timescales with distinct oscillatory network states. SPW participation probability is predicted by individual theta firing rate, suggesting that the CA3 recurrent network preferentially reinstates neurons that were most active during learning. The authors propose that oscillatory interneuron networks provide "temporal windows of opportunity" that gate the impact of replayed sequences on postsynaptic targets. **Note**: cell-type specificity of replay mechanisms and the precise biophysics of time compression are not resolved here.

---

### Limitations & open questions

- Only two rats had stable simultaneous recordings across all three sessions, limiting statistical power for the key Sleep1/Run/Sleep2 comparison.
- The running wheel task is spatially degenerate (stereotyped trajectory), activating a restricted and repeated sequence of place cells; generalisability to complex spatial environments is assumed rather than demonstrated.
- The compression ratio and its relationship to SPW/ripple dynamics are characterised correlationally; the mechanism generating the compression (CA3 autoassociative dynamics, interneuron timing, etc.) is proposed but not tested.
- Whether replayed sequences drive downstream synaptic changes (the core consolidation claim) is not directly demonstrated; "Direct demonstration of SPW-induced synaptic changes remains a future challenge."
- Cross-train spike shuffling reduces individual firing-rate differences, potentially over- or under-estimating baseline sequence rates; no single shuffling method is ideal.
- The paper does not test whether disrupting SPW/ripple events during sleep impairs subsequent memory, which would be required to establish functional necessity.

---

### Connections & keywords

**Key citations**:
- Wilson & McNaughton (1994) — pairwise hippocampal reactivation during sleep
- Skaggs & McNaughton (1996) — replay of neuronal firing sequences in hippocampus
- Buzsáki (1989) — two-stage model of memory trace formation
- Csicsvari et al. (1999) — oscillatory coupling of hippocampal pyramidal cells and interneurons
- McClelland, McNaughton & O'Reilly (1995) — complementary learning systems
- Chrobak & Buzsáki (1994, 1996) — sharp-wave output to entorhinal cortex
- Abeles & Gerstein (1988) — detecting spatiotemporal firing patterns

**Named models or frameworks**:
- Two-stage memory consolidation model (Buzsáki 1989)
- Template-matching method (Dayhoff & Gerstein 1983; modified here)
- Joint probability map (JPM) / joint peri-event time histogram (JPTH) (Aertsen et al. 1989)
- Monte Carlo spike-train shuffling

**Brain regions**:
- Hippocampal CA1
- Hippocampal CA3
- Entorhinal cortex

**Keywords**:
- hippocampal replay
- spike sequence reactivation
- time compression
- sharp-wave ripples
- slow-wave sleep
- place cells
- memory consolidation
- theta oscillations
- spatiotemporal spike patterns
- template-matching
- joint probability map
- two-stage memory model
