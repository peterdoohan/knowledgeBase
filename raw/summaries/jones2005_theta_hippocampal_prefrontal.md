---
source_file: "jones2005_theta_hippocampal_prefrontal.md"
paper_id: "jones2005_theta_hippocampal_prefrontal"
title: "Theta Rhythms Coordinate Hippocampal\u2013Prefrontal Interactions in a Spatial Memory Task"
authors: "Matthew W. Jones, Matthew A. Wilson"
year: 2005
journal: "PLoS Biology"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
tasks: ["t_maze"]
methods: ["tetrode_recording"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex", "infralimbic_cortex"]
keywords: ["theta_oscillations", "hippocampalprefrontal_synchrony", "spatial_working_memory", "phase_locking", "lfp_coherence", "cross_structural_coordination", "spike_cross_correlation", "decision_making", "place_cells", "prefrontal_cortex", "temporal_coding", "oscillatory_synchrony", "theta", "rhythms", "coordinate", "hippocampalprefrontal", "interactions", "spatial", "memory", "task"]
---

### One-line summary

Theta-frequency (4–12 Hz) synchronisation between hippocampal CA1 and medial prefrontal cortex is selectively enhanced during the working-memory and decision-making epochs of a spatial alternation task, and is attenuated on error trials, demonstrating that theta rhythms provide a dynamic mechanism for cross-structural coordination.

---

### Background & motivation

Working memory requires the transient integration of information across brain regions, with the prefrontal cortex thought to act as a hub that incorporates hippocampal spatial information into decision-making. Prior work (Siapas et al.) had shown that mPFC neurons phase-lock to hippocampal theta, but had not related this to task demands or behaviour. The paper addresses whether hippocampal–prefrontal coordination via theta rhythms is specifically recruited during epochs of high mnemonic load, or is a fixed anatomical property independent of task state.

---

### Methods

- **Species/subjects**: 6 male Long-Evans rats trained to asymptotic performance (≥80% correct) on a continuous spatial-alternation T-maze task.
- **Task design**: Each trial had a forced-turn (sample) epoch and a choice (test) epoch; stages were dissected to compare central-arm crossings during choice direction (working-memory load) vs. forced-turn direction (no working-memory demand) while controlling for running speed and spatial location.
- **Recordings**: Simultaneous tetrode recordings from dorsal CA1 (139 units) and medial prefrontal cortex (165 units); local field potentials (LFP) sampled continuously; 8 sessions from 6 rats.
- **Analyses**:
  - Spike-train cross-correlations between CA1–mPFC neuron pairs during different task epochs.
  - Theta phase-locking of individual neurons to CA1 LFP (circular-concentration coefficient, κ; Rayleigh test).
  - Multi-taper LFP coherence between CA1 and mPFC in the 4–12 Hz range.
  - Comparisons across choice-correct, choice-error, and forced-turn runs; correct trials vs. error trials used to link synchrony to behavioural outcome.

---

### Key findings

- **Spike cross-correlations**: CA1–mPFC neuron-pair cross-correlations were significantly higher during choice (working-memory) epochs than forced-turn epochs on the same section of maze (0.024 vs. 0.009; p < 0.01). Error trials showed intermediate but significantly reduced correlations (0.015; p < 0.05 vs. correct).
- **Phase-locking**: mPFC neurons showed significantly higher circular-concentration (κ) to CA1 theta during choice-correct runs than forced-turn runs (0.19 vs. 0.10; p < 0.01). CA1 phase-locking to its own theta was stable across epochs (κ ≈ 0.43–0.53), indicating the modulation was specific to mPFC coupling.
- **LFP coherence**: Theta-band (4–12 Hz) CA1–mPFC coherence was significantly elevated during choice-correct vs. forced-turn epochs (0.32 vs. 0.19; p < 0.05) and reduced on error trials (0.20; p < 0.05 vs. correct). No consistent coherence was observed at delta or frequencies above 12 Hz.
- **Spatial information**: mPFC firing carried more spatial information (bits per spike) during choice epochs coinciding with enhanced phase-locking.
- All three measures (cross-correlation, phase-locking, LFP coherence) converged to show that theta-frequency coordination is specifically recruited by working-memory demand and predicts behavioural accuracy.

---

### Computational framework

The paper does not employ a formal computational model but is grounded in a **temporal coding / oscillatory synchrony** framework. The key principle is that neurons phase-locked to the same oscillatory reference signal will have consistent temporal relationships, enabling coordinated firing across structures. Specifically:

- **What is modelled**: The probability of coincident firing across CA1–mPFC pairs is determined by shared phase-locking to theta. Neurons locked to the same phase (~50 ms windows per cycle) have elevated co-firing probability.
- **Key variables**: Theta phase of each spike (0–360°), circular-concentration coefficient (κ) quantifying phase-locking strength, and LFP coherence as a population-level correlate.
- **Assumptions**: Theta rhythms act as a common clock; mPFC phase-locks to CA1 theta rather than the reverse (consistent with CA1 leading mPFC by ~30 ms); coherence is independent of power, reflecting phase alignment rather than amplitude.

---

### Prevailing model of the system under study

The paper's introduction frames the working assumption as follows: prefrontal cortex is the hub for working memory and decision-making, but must integrate spatial information from the hippocampus. Lesion studies had established that both mPFC and hippocampus are required for spatial working memory. Prior electrophysiology (Siapas et al. 2005; Hyman et al.) had demonstrated that mPFC neurons phase-lock to CA1 theta during spatial tasks, and that this phase-locking correlated with stronger mPFC–CA1 spike covariance. However, neither prior study had manipulated or measured task epoch to show that phase-locking is *behaviourally gated* rather than a static property of the anatomical connection. The field therefore lacked evidence that theta synchrony is dynamically recruited according to cognitive demand rather than simply co-occurring with movement.

---

### What this paper contributes

The paper establishes that hippocampal–prefrontal theta synchrony is not a fixed correlate of running or hippocampal activation, but is **dynamically modulated by working-memory demand** within a trial. Key advances:

1. CA1–mPFC coordination (at spike, phase-locking, and LFP levels) is selectively elevated during the choice epoch — the stage with the highest mnemonic load — relative to a matched forced-turn epoch with equivalent running speed and spatial location.
2. Synchrony predicts behavioural outcome: reduced on error trials, providing a causal implication that functional hippocampal–prefrontal communication is necessary for correct performance.
3. The modulation is specific to mPFC: CA1 phase-locking to its own theta is constant across epochs, so the change reflects dynamic coupling on the prefrontal side.
4. Multiple levels of analysis (unit pairs, single-unit phase-locking, population LFP coherence) converge on the same conclusion, strengthening the interpretation.

The paper therefore supports a model in which theta rhythms constitute a **flexible routing mechanism**: mPFC can selectively join the hippocampal theta network when current task demands require hippocampal spatial information for decision-making.

---

### Brain regions & systems

- **Dorsal CA1 (hippocampus)**: Source of the theta rhythm reference signal; provides place-cell spatial information; leads mPFC activity by ~30 ms; its own phase-locking to theta is stable across task epochs.
- **Medial prefrontal cortex (prelimbic/infralimbic cortex)**: Dynamically increases phase-locking to CA1 theta and spike–LFP coherence during working-memory epochs; proposed site of integration of hippocampal spatial information with decision-making processes.
- **Hippocampal–prefrontal monosynaptic projection** (discussed, not directly recorded): Proposed as the anatomical route through which CA1 influences mPFC interneurons to achieve synchronisation; noted that most projections arise from ventral CA1/subiculum rather than dorsal CA1, raising questions about the relevant pathway.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

1. **Algorithm presented**: Theta phase-locking as a mechanism for coordinating temporally precise coincident firing across CA1 and mPFC; the algorithm is that shared phase alignment to ~50 ms theta windows creates a common temporal reference that elevates co-firing probability of phase-locked neurons.
2. **Neural data supporting the algorithm**: Simultaneous spike and LFP recordings show that the predicted consequence of enhanced phase-locking — increased spike-train cross-correlations — is indeed observed, and that both measures co-vary with LFP coherence and with behavioural accuracy.

**Marr's levels:**

- **Computational**: The brain must dynamically route spatial information from hippocampus to prefrontal cortex during decision-making epochs while keeping the two structures functionally independent during routine navigation. The problem is selective, on-demand integration across anatomically separate structures.
- **Algorithmic**: Shared theta phase-locking provides a temporal code: mPFC neurons adjust their preferred firing phase relative to CA1 theta to synchronise with hippocampal output during high-demand epochs. The metric is the circular-concentration coefficient (κ) of spike phase distributions; enhanced κ directly predicts increased cross-correlations.
- **Implementational**: Monosynaptic hippocampal projections to deep-layer mPFC interneurons are proposed as the substrate. Local inhibitory interneuronal networks in mPFC may be entrained by hippocampal theta inputs, synchronising pyramidal-cell firing to CA1 theta. The authors note that the most prominent projections arise from ventral CA1/subiculum (not dorsal CA1), leaving open which anatomical route is functionally engaged. No direct interneuron recordings or pharmacological manipulations were performed to confirm this mechanism.

**Bonus**: The paper discusses interneuron-mediated synchrony as the likely implementation, citing evidence that hippocampal projections contact mPFC interneurons, consistent with a role for inhibitory networks in aligning theta phase across structures.

---

### Limitations & open questions

- **Directionality**: The data do not unequivocally establish that CA1 drives mPFC (rather than a common third-party input). While the ~30 ms CA1-leading phase lag is consistent with a hippocampal drive account, the source of task-epoch modulation (hippocampal, prefrontal, or neuromodulatory) is unresolved.
- **Ventral vs. dorsal CA1**: Most hippocampal projections to mPFC originate from ventral CA1/subiculum, yet recordings focused on dorsal CA1. Whether dorsal CA1 drives mPFC directly or via ventral CA1 is unresolved.
- **Error origin**: It cannot be determined at which task stage errors arose, or whether they reflect attentional, mnemonic, or decision-making failures — all of which predict attenuated synchrony.
- **Alternative confounds**: Attention and reward expectancy may also differ between choice and forced-turn epochs, potentially contributing to the synchrony differences.
- **Residual synchrony**: Some phase-locking and coherence persists during forced-turn epochs; its functional significance (updating of route/task-rule information?) is unaddressed.
- **Generalisation**: 8 sessions from 6 rats; ventral CA1 sample too small for systematic comparison; task is specific to spatial working memory.

---

### Connections & keywords

- **Key citations**: Siapas et al. (2005) — mPFC phase-locking to CA1 theta; Hyman et al. — mPFC phase-locking on linear tracks; O'Keefe & Nadel (1978) — hippocampus as cognitive map; Buzsaki (2002) — theta oscillations in hippocampus; Raghavachari et al. (2001) — human theta gating by working memory; Lee et al. (2005) — phase-locking in primate extrastriate cortex during working memory; Friston & Frith (1995) — schizophrenia as disconnection syndrome.
- **Named models or frameworks**: Temporal coding hypothesis; theta phase-locking as a cross-structural coordination mechanism; Complex Spike Index (for pyramidal cell classification); multi-taper spectral analysis (Jarvis & Mitra coherence).
- **Brain regions**: Dorsal CA1 (hippocampus), medial prefrontal cortex (prelimbic/infralimbic), ventral CA1/subiculum (discussed), mPFC interneurons (proposed implementation).
- **Keywords**: theta oscillations, hippocampal–prefrontal synchrony, spatial working memory, phase-locking, LFP coherence, cross-structural coordination, spike cross-correlation, decision-making, place cells, prefrontal cortex, temporal coding, oscillatory synchrony
