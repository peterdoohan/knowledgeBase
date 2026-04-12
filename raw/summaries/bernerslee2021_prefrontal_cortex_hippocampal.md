---
source_file: bernerslee2021_prefrontal_cortex_hippocampal.md
paper_id: bernerslee2021_prefrontal_cortex_hippocampal
title: "Prefrontal Cortical Neurons Are Selective for Non-Local Hippocampal Representations during Replay and Behavior"
authors:
  - "Alice Berners-Lee"
  - "Xiaojing Wu"
  - "David J. Foster"
year: 2021
journal: "The Journal of Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - y_maze
methods:
  - tetrode_recording
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - prefrontal_cortex
  - medial_prefrontal_cortex
keywords:
  - hippocampal_replay
  - sharp_wave_ripples
  - prefrontal_cortex
  - non_local_representation
  - theta_sequences
  - hp_pfc_coordination
  - spatial_memory
  - decision_making
  - y_maze_alternation
  - bayesian_decoding
  - memory_consolidation
  - prospective_coding
  - prefrontal
  - cortical
  - neurons
  - selective
  - non
  - local
  - hippocampal
  - representations
key_citations:
  - jadhav2016_hippocampal_prefrontal_swr
  - davidson2009_hippocampal_replay_extended
  - shin2019_hippocampal_prefrontal_replay_b
  - wikenheiser2015_theta_sequences_goals
---

### One-line summary

A subset of PFC neurons is selectively tuned to the content of hippocampal replay — and, more generally, to any non-local hippocampal position representation — rather than to the animal's actual location, identifying a novel mechanism by which HP-PFC communication might support memory-guided decision-making.

---

### Background & motivation

The hippocampus (HP) represents current spatial position via place cells, but during rest also generates "replay" — sequential reactivation of place-cell patterns that depict trajectories through space, co-occurring with sharp-wave ripples (SWRs). The prefrontal cortex (PFC) is implicated in both memory consolidation and decision-making, and PFC neurons are known to be modulated during SWRs. However, prior work could not determine whether PFC neurons were selective for the spatial content (i.e., which trajectory or arm) depicted in HP replay, because resolving replay content requires simultaneous recordings from large numbers of HP neurons — technically challenging when also recording from PFC. This paper exploits 40-tetrode implants split between HP and PFC to ask whether individual PFC neurons track what the HP is replaying, not merely whether a SWR occurred.

---

### Methods

- **Subjects**: 4 male Long-Evans rats; 11 recording sessions (1–4 per rat).
- **Task**: Y-maze spatial alternation task; recordings taken during early learning (days 1–5), before asymptotic performance.
- **Implant**: Custom 40-tetrode microdrives split between right dorsal CA1 (HP) and right medial prelimbic/infralimbic PFC.
- **Neural yield**: Mean 88 HP neurons (range 62–137; 968 total) and 14.4 PFC neurons (range 7–25; 158 total) per session.
- **Replay decoding**: Bayesian decoding of HP ensemble activity during SWRs; replays classified by which arm of the Y-maze they depicted ("arm-replays"). Stricter criteria (weighted correlation >0.6) used as a control and produced similar results.
- **PFC arm-replay selectivity**: Permutation test comparing sum of squared differences (SSD) of PFC firing rates across replay of each arm vs. shuffled arm labels; 18.5% threshold for significance.
- **Population decoding**: Leave-one-out linear discriminant analysis (diaglinear) classifying arm identity of replay from PFC population activity.
- **Non-local vs. local HP representations during running**: Bayesian decoding of HP activity during locomotion (40-ms bins); bins classified as local (decoded position near actual position) or non-local (decoded position far from actual position). PFC firing rates compared across local vs. non-local bins.
- **Theta cycle analysis**: HP theta cycles split into early (local) and late (non-local) halves; PFC cross-covariance with HP spikes computed separately for each half.
- **Choice prediction**: Discriminant analysis of future arm choice from PFC spikes locked to local vs. non-local theta-cycle epochs.

---

### Key findings

- **PFC neurons are non-selective for spatial position during running** (low spatial selectivity, high radial symmetry across arms), consistent with prior reports; best behavioral predictor of PFC firing was distance traveled within a trial.
- **18.5% of PFC neurons (28/151; p = 2.2e-9) were significantly differentially modulated by replay of different maze arms**, a level far exceeding chance. Using only one session per rat: 20% (14/69; p = 6.9e-6).
- **PFC population activity decoded HP replay arm identity better than chance** (p = 0.002); accuracy scaled with the number of simultaneously recorded PFC neurons. Decoding was robust to controls for ripple power, time within session, rat position at SWR onset, and replay duration.
- **PFC replay selectivity exceeded what could be predicted from behavioral arm selectivity**: simulated "reactivation" responses (derived from firing rates on each arm during running) were significantly less arm-selective than the observed responses (Wilcoxon signed-rank, p = 9.8e-4 across sessions; p = 1e-5 for significantly modulated neurons alone).
- **PFC neurons were more strongly driven by HP spikes from the late (non-local) half of theta cycles** than the early (local) half, across all PFC neurons (p = 4.9e-5) and in the replay-selective subset (p = 6.8e-5). The degree of late-theta preference correlated with replay arm selectivity (R = 0.32, p = 7.6e-5).
- **During running, PFC neurons' arm-modulation patterns matched non-local HP representations** better than local HP representations (one-sided Wilcoxon signed-rank, p = 0.0197 for significantly arm-replay modulated neurons), and this was above a shuffle control (p = 9.0e-3).
- **Remote HP theta cycles predicted upcoming arm choice** (permutation test, p < 0.001); PFC spikes locked to non-local theta epochs decoded future choice above chance (p < 0.001), while PFC spikes locked to local epochs did not (p > 0.8). Non-local PFC decoding significantly outperformed local (p < 1e-4).

---

### Computational framework

Not applicable in the sense of a formal computational model, but the paper implicitly adopts a **population-vector decoding / Bayesian neural decoding** framework for HP replay content, and interprets PFC activity within a **non-local representation** framework.

The key computational idea is the distinction between *local* HP representations (place-cell activity encoding the animal's current position) and *non-local* HP representations (place-cell activity encoding remote positions, occurring during replay events and the late phase of theta sequences). The paper proposes that PFC neurons are preferentially tuned to read out non-local HP state rather than local HP state — i.e., PFC acts downstream of an internally-generated representational variable, not of the sensory-driven position signal.

The results are interpreted as evidence against the Indexing Theory of memory consolidation (Teyler & Rudy, 2007), which predicts that HP replay should re-activate the corresponding cortical patterns from encoding; instead, PFC selectivity during replay is stronger than during the associated behavioral experience, suggesting a distinct coupling mechanism.

---

### Prevailing model of the system under study

Prior to this paper, the dominant view of HP-PFC interaction during replay was essentially a **reactivation hypothesis**: PFC neurons (like neurons in other cortical regions) would be reactivated during HP SWRs in a pattern reflecting the cortical activity that occurred during the original behavioral experience. This was supported by observations that PFC neurons are broadly modulated by SWRs, that this modulation is stronger during task-relevant states, and that HP-PFC co-activity during SWRs tends to reflect recently experienced trajectories rather than unchosen ones. The Indexing Theory formalised a version of this, predicting that HP replay re-engages cortical patterns at encoding, gradually consolidating them. A related assumption was that any HP-PFC coordination during behavior would reflect the animal's actual current location.

---

### What this paper contributes

The paper overturns the expectation that PFC activity during HP replay is a reactivation of PFC patterns from behavioral experience. Key contributions:

1. **First demonstration** that individual PFC neurons are selective for the *content* (which arm/trajectory) of HP replay, not merely the occurrence of a SWR.
2. **Dissociation of replay selectivity from behavioral selectivity**: PFC arm selectivity during replay is stronger than during running, ruling out simple reactivation and ruling out content inherited from PFC's own spatial coding.
3. **Unification across states**: PFC's tuning to HP replay content is a special case of a broader principle — PFC neurons track non-local HP representations whether they arise during rest (replay) or during behavior (non-local theta sweep phases), and this non-local tracking predicts future choice.
4. **Reframing HP-PFC communication**: Rather than HP driving cortical reactivation of past experience (as Indexing Theory posits), HP communicates internally generated non-local representations to PFC, which is selectively tuned to read them out. This suggests a prospective or deliberative function.

---

### Brain regions & systems

- **Hippocampus (dorsal CA1)** — source of place-cell activity, sharp-wave ripples, theta sequences, and replay; provides the non-local spatial representations that PFC neurons track.
- **Medial prefrontal cortex (prelimbic and infralimbic areas)** — the main region of interest; neurons here are selectively modulated by HP replay content and by non-local HP representations during running, and their spiking predicts future choice.
- **HP-PFC network** — the coordinated system under study; theta oscillations (6–12 Hz) are proposed as a gating mechanism through which PFC preferentially reads out non-local HP activity during late theta phases.

---

### Mechanistic insight

The paper meets one of the two criteria: it provides **neural data** (electrophysiological recordings of both HP and PFC populations) specifically linking PFC activity to HP non-local representations. It does not, however, formalise an explicit algorithm that specifies in detail how PFC neurons compute their selectivity for non-local HP content, nor does it address specific cell types, layer structure, or biophysical mechanisms.

At the level of Marr's framework:

- **Computational**: The brain needs to integrate information about possible future or past trajectories (non-local states) into PFC-mediated decision-making. PFC must selectively attend to internally generated HP representations rather than to current sensory input.
- **Algorithmic**: The data suggest that PFC neurons are tuned to non-local HP population vectors — with a lag of 10–50 ms — regardless of whether those vectors arise during rest (replay) or running (late theta sweeps). Theta phase gating is proposed as a mechanism: PFC preferentially receives or responds to HP input arriving during late theta phases, when HP representations are most non-local. The pattern of arm selectivity is consistent across replay and running non-local epochs for the same neurons.
- **Implementational**: Not addressed. The paper notes that PFC receives inputs from striatum and amygdala as well as HP, and speculates that theta gating could allow PFC to selectively tune into HP during specific phases, but no cell-type, layer, connectivity, or pharmacological evidence is provided.

---

### Limitations & open questions

- **Small sample**: 4 rats, 11 sessions; PFC yield was low (mean 14.4 neurons/session), limiting statistical power. Authors note that decoding accuracy scaled with neuron number, suggesting results would be stronger with more recorded cells.
- **Early learning only**: Recordings were taken during days 1–5 of task learning before asymptotic performance. It is unknown whether the same HP-PFC coupling persists or changes at high performance levels, or whether PFC neurons eventually become tuned to more abstract task variables.
- **Direction of information flow**: The paper focuses on HP-leading-PFC activity (10–50 ms lag), but does not rule out bidirectional communication or contributions from a common driver. PFC activity preceding SWRs is acknowledged but not analysed.
- **Mismatch with Indexing Theory**: While the data challenge this model, the paper leaves open how PFC does use HP replay — the exact computations PFC performs on non-local HP inputs are not specified.
- **Theta phase vs. decoded content as the defining feature of "non-local"**: Both approaches yield similar conclusions, but the relationship between phase and position decoding is complex and not fully resolved.
- **Anatomical specificity**: Only prelimbic/infralimbic PFC was recorded; whether deep vs. superficial layers or other PFC subregions differ was not examined.
- **Replay direction**: Forward vs. reverse replays were not separated in the main analyses (no bias was found), but the functional implications of directional selectivity were not explored.

---

### Connections & keywords

**Key citations**:
- Wu & Foster (2014) — prior study using subset of this dataset; HP replay in Y-maze
- Jadhav et al. (2016) — HP-PFC coordination during SWRs; methods for PFC modulation analysis
- Foster & Wilson (2006) — reverse replay during awake states
- Davidson et al. (2009) — Bayesian decoding algorithm for replay
- Teyler & Rudy (2007) — Hippocampal Indexing Theory (challenged by this paper)
- McClelland et al. (1995) — Complementary Learning Systems theory
- Wikenheiser & Redish (2015) — theta sequences and goal-directed navigation
- Siapas et al. (2005) — PFC phase-locking to HP theta
- Benchenane et al. (2010) — HP-PFC theta coherence and learning
- Tang et al. (2017); Yu et al. (2017) — context-dependent HP-PFC reactivation
- Shin et al. (2019) — awake replay and HP-PFC dynamics in spatial learning
- Pfeiffer & Foster (2013) — HP place-cell sequences depicting future paths

**Named models or frameworks**:
- Hippocampal Indexing Theory (Teyler & Rudy, 2007)
- Complementary Learning Systems (McClelland et al., 1995)
- Theta sequences / theta sweeps
- Bayesian decoding (Davidson et al., 2009)
- Sharp-wave ripple replay

**Brain regions**:
- Hippocampus (dorsal CA1)
- Medial prefrontal cortex (prelimbic, infralimbic)

**Keywords**:
- hippocampal replay
- sharp-wave ripples
- prefrontal cortex
- non-local representation
- theta sequences
- HP-PFC coordination
- spatial memory
- decision-making
- Y-maze alternation
- Bayesian decoding
- memory consolidation
- prospective coding
