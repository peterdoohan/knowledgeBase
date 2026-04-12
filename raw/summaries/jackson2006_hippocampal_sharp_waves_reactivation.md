---
source_file: jackson2006_hippocampal_sharp_waves_reactivation.md
paper_id: jackson2006_hippocampal_sharp_waves_reactivation
title: "Hippocampal Sharp Waves and Reactivation during Awake States Depend on Repeated Sequential Experience"
authors:
  - "Jadin C. Jackson"
  - "Adam Johnson"
  - "A. David Redish"
year: 2006
journal: "The Journal of Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - linear_track
  - foraging_task
methods:
  - tetrode_recording
  - computational_modeling
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - entorhinal_cortex
frameworks:
  - attractor_networks
keywords:
  - hippocampal_sharp_waveripple_complexes_swrs
  - awake_reactivation
  - place_cells
  - sequential_experience_dependent_plasticity
  - ca3_recurrent_collaterals
  - large_irregular_activity_lia
  - theta_oscillations
  - ensemble_cofiring
  - behavioral_entropy
  - memory_consolidation
  - experience_dependent_swr_emission
  - ca3ca1_interaction
  - hippocampal
  - sharp
  - waves
  - reactivation
  - during
  - awake
  - states
  - depend
---

### One-line summary

Awake hippocampal sharp wave–ripple (SWR) emission and ensemble reactivation both increase with experience within a session, and critically depend on the sequential regularity of the animal's behavior.

---

### Background & motivation

Hippocampal pyramidal cell firing patterns observed during spatial behavior are reactivated during subsequent slow-wave sleep, and theories propose this reactivation supports memory consolidation via sharp wave–ripple (SWR) events. These SWRs are thought to arise from noise cascading across synapses potentiated by asymmetric Hebbian plasticity during repeated sequential experience. Prior work had established sleep reactivation, but the experience-dependence of *awake* SWR emission and reactivation — and its dependence on behavioral regularity — had not been systematically tested. This paper fills that gap by comparing SWR emission and ensemble reactivation across tasks differing in spatial behavioral regularity.

---

### Methods

- **Subjects**: Male Fisher–Brown–Norway rats (n = 6 for Experiment I; n = 6 for Experiment II), chronically implanted with 14-tetrode microdrives.
- **Experiment I tasks**: Three tasks with different spatial regularities run daily in 20 min sessions each:
  - Linear track (LT): highly repetitive back-and-forth shuttling.
  - Cylinder-foraging (CF): random foraging in an open arena (low spatial regularity).
  - Cylinder-goal (CG): navigation to a hidden reward goal (intermediate regularity).
- **Experiment II**: Multiple-T (MT) sequence task; six rats split between CA1 (n = 3) and CA3 (n = 3) recordings on a novel 4T maze.
- **Recordings**: CA1 LFP and multi-unit activity (tetrodes); CA3 LFP and unit activity for Experiment II.
- **SWR detection**: Bandpass filtering (100–250 Hz), Hilbert transform envelope thresholding (2.5 SD above mean), restricted to non-theta LFP states to isolate LIA-associated SWRs.
- **Reactivation analysis**: Novel ensemble cofiring measure comparing binary co-firing patterns during theta (behavior) and SWR periods using XOR and binomial likelihood test across all cell pairs recorded on different tetrodes.
- **Behavioral entropy**: Shannon entropy of spatial transition probabilities used to quantify behavioral regularity per session.
- **Statistical approach**: Linear regression of SWR emission over laps; Wilcoxon signed-rank tests for within-session reactivation change; stepwise multiple regression for joint effects of lap number, behavioral entropy, and their interaction.

---

### Key findings

- **SWR emission increases with experience**: SWR events per second in non-theta states increased significantly across laps on the linear track (R² = 0.098, p < 0.00002) and overall across all tasks (p = 0.0003); increase was stronger on LT than on the two-dimensional tasks.
- **Reactivation occurs during awake SWRs**: Ensemble co-firing patterns during awake SWRs were significantly more similar to theta-state co-firing than expected by chance across all tasks (overall p < 10⁻¹²; LT p < 10⁻⁸; CF p < 0.00001; CG p < 0.0001).
- **Reactivation similarity increases within a session**: On the linear track and overall, reactivation similarity between SWR and theta states increased from first to second half of each session (overall p = 0.01; LT p = 0.05); not significant for the two-dimensional tasks.
- **Behavioral regularity drives SWR emission and reactivation**: Stepwise regression showed significant effects of lap number, behavioral entropy, and their interaction on SWR emission rate (p < 0.00001 for each). Lower entropy (more regular spatial sequences) and more laps jointly predicted higher SWR emission.
- **Reactivation of other previously run tasks**: During the third task of a daily session, reactivation of the *other* tasks run earlier in the day was significantly stronger than during the first task (p < 0.001, sign test), demonstrating cumulative cross-task reactivation.
- **CA3 leads CA1 in early SWR emission**: On the multiple-T task, both CA3 and CA1 showed SWR emission rate increases over the first 20 laps (p < 10⁻¹⁰ for both), but CA3 showed higher rates during the first five laps (t-test, p < 0.001), with a significant lap × structure interaction (p = 0.008).
- **SWR amplitude and rate changes can dissociate**: On MT, SWR amplitude continued to increase after SWR emission rate plateaued at ~20 laps, ruling out detection-threshold artifacts as the sole explanation.

---

### Computational framework

The paper is grounded in a **Hebbian plasticity / attractor network** framework for hippocampal memory. The core model (developed in prior theoretical work by Buzsáki, Redish & Touretzky, and others) holds that:

- During theta-state behavior, repeated sequential co-activation of CA3 pyramidal cells potentiates recurrent synapses via asymmetric spike-timing-dependent plasticity (STDP).
- During LIA (non-theta states, including awake immobility and SWS), the network is decoupled from entorhinal input; uncorrelated noise drives cascades through these strengthened synapses, producing replay of stored sequences as SWR events.

Key variables: synaptic weight matrix (strengthened by sequence repetition), SWR emission rate (proxy for stored sequence strength), ensemble co-firing similarity between theta and SWR states (proxy for reactivation fidelity). The framework predicts that SWR emission and reactivation quality should increase monotonically with experience and behavioral regularity — predictions that this paper empirically tests.

---

### Prevailing model of the system under study

The introduction frames the field as operating under the **two-stage memory model** (Marr 1971; Buzsáki 1989): spatial sequences are encoded during theta-associated locomotion via plasticity in CA3 recurrent collaterals, and then spontaneously replayed during subsequent LIA/sleep via SWR events, supporting memory consolidation. Place cells provide the neural substrate for spatial sequence encoding. Prior empirical work had confirmed sleep-state reactivation (Wilson & McNaughton 1994; Kudrimoti et al. 1999; Nádasdy et al. 1999) and noted awake SWRs (O'Neill et al. 2006; Foster & Wilson 2006), but the specific dependence of awake reactivation on behavioral repetition — and its parametric relationship to sequential regularity — was assumed but not directly demonstrated. The paper also notes theoretical predictions that CA3 SWRs should precede and drive CA1 SWRs.

---

### What this paper contributes

This paper provides the first direct test of how behavioral repetition modulates *awake* hippocampal SWR emission and ensemble reactivation. Key updates to the prevailing model:

1. **Experience-dependent SWR emission is not specific to sleep**: SWR emission and reactivation fidelity increase within-session during wakefulness, confirming that consolidation-related reactivation begins immediately during the learning session itself.
2. **Behavioral regularity is a quantifiable driver**: By measuring spatial transition entropy, the paper demonstrates a parametric relationship — SWR emission rises faster and earlier with lower-entropy (more repetitive) behavior, providing strong evidence for the plasticity cascade theory.
3. **Cross-task reactivation occurs during wakefulness**: Representations of recently run tasks are reactivated during subsequent task performance, showing that awake replay incorporates a broader memory context, not just the current environment.
4. **CA3 anticipates CA1**: Early SWR generation in CA3 before CA1, on a novel task, is consistent with CA3 being the site of sequence storage that then drives CA1 — supporting the CA3-initiates-CA1 model of SWR generation, though the lack of simultaneous recordings limits causal inference.

---

### Brain regions & systems

- **Hippocampus CA1** — primary recording region for Experiments I; SWR emission and ensemble reactivation measured here; receives SWR input from CA3.
- **Hippocampus CA3** — recorded in Experiment II; proposed site of sequence storage via recurrent collateral plasticity; showed earlier SWR onset than CA1 on novel task, consistent with CA3 driving CA1 during SWRs.
- **Entorhinal cortex** — mentioned as the input that is gated out during LIA/SWS, allowing internally generated replay to dominate; not directly recorded.

---

### Mechanistic insight

The paper meets both criteria for this section.

**Phenomenon**: Awake hippocampal SWR emission and ensemble reactivation fidelity increase as a function of repeated sequential experience, and this increase depends on the spatial regularity of the behavior.

- **Computational level**: The hippocampus stores spatial sequence memories during active navigation and replays them during rest to support consolidation. The problem being solved is the offline strengthening or transfer of recently acquired sequential memories.
- **Algorithmic level**: During theta-state locomotion, CA3 recurrent synapses are strengthened between neurons with overlapping, sequentially activated place fields (asymmetric STDP). During LIA, noise in the network cascades through these potentiated synapses, re-activating the stored sequence as a SWR event. The ensemble co-firing measure (XOR-based binomial test) directly indexes the fidelity of this replay: the same cell assemblies co-active during theta are more likely to co-fire during SWRs, and this similarity grows with experience and behavioral regularity.
- **Implementational level**: CA3 pyramidal cell recurrent collaterals are the proposed site of plasticity and SWR initiation; CA3 SWRs project to and recruit CA1, where they are detected as ripple-associated multi-unit bursts. Experiment II provides direct evidence that CA3 leads CA1 in SWR emission on early laps of a novel task, supporting the CA3→CA1 cascade at the circuit level. The paper does not address specific cell types, neuromodulators, or biophysical synaptic mechanisms beyond citing STDP models.

---

### Limitations & open questions

- **No simultaneous CA3–CA1 recordings**: The CA3 lead over CA1 is inferred from separate animals, preventing direct measurement of cross-structure coherence or temporal ordering within individual SWR events.
- **Reactivation measure is temporally unordered**: The XOR ensemble cofiring analysis does not capture the sequential ordering of spikes within SWRs, so it cannot distinguish true forward/reverse replay from non-sequential ensemble reactivation. The paper explicitly acknowledges that some "reactivation" events may reflect self-localization (current position) rather than memory replay.
- **CA3 increase in time-in-LIA on MT**: On the multiple-T task, the proportion of time in LIA also increased with laps, confounding SWR rate increases with changes in brain state. Authors argue this is unlikely to explain all the effects, but cannot fully rule it out.
- **Reactivation analysis requires large ensembles**: The cofiring analysis was restricted to sessions with ≥20 simultaneously recorded neurons (only 10 sessions from 3 rats), limiting statistical power and generalisability.
- **Functional role of cross-task reactivation unclear**: The finding that prior-task representations are replayed during a subsequent task is described but not mechanistically explained — it is unclear whether this reflects memory interference, consolidation, or another process.
- **Specific behavioral variables not tracked**: Lack of video-based behavioral coding (only LED position) meant specific rest behaviors (grooming, sitting, etc.) during SWR events could not be characterised.

---

### Connections & keywords

**Key citations**:
- Buzsáki G (1989) — Two-stage memory model; SWRs as consolidation mechanism
- Wilson & McNaughton (1994) — Sleep reactivation of hippocampal ensembles
- Redish & Touretzky (1998) — Computational model of CA3 replay via potentiated recurrents
- Foster & Wilson (2006) — Reverse replay during awake SWRs on linear track
- O'Neill et al. (2006) — Place-selective firing during awake SWRs
- Nádasdy et al. (1999) — Replay and time compression of hippocampal sequences
- Skaggs & McNaughton (1996) — Sleep replay of neuronal firing sequences

**Named models or frameworks**:
- Two-stage memory model (Marr/Buzsáki)
- Asymmetric spike-timing-dependent plasticity (STDP) / Hebbian plasticity in CA3
- XOR ensemble cofiring reactivation measure (novel method introduced here)
- Multiple-T (MT) task (Schmitzer-Torbert & Redish 2002/2004)

**Brain regions**:
- Hippocampus CA1
- Hippocampus CA3
- Entorhinal cortex (indirect)

**Keywords**:
- hippocampal sharp wave–ripple complexes (SWRs)
- awake reactivation
- place cells
- sequential experience-dependent plasticity
- CA3 recurrent collaterals
- large irregular activity (LIA)
- theta oscillations
- ensemble cofiring
- behavioral entropy
- memory consolidation
- experience-dependent SWR emission
- CA3–CA1 interaction
