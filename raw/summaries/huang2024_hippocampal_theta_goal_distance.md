---
source_file: huang2024_hippocampal_theta_goal_distance.md
paper_id: huang2024_hippocampal_theta_goal_distance
title: "Human Hippocampal Theta Oscillations Organise Distance to Goal Coding"
authors:
  - "Zimo Huang"
  - "James A Bisby"
  - "Neil Burgess"
  - "Daniel Bush"
year: 2024
journal: "bioRxiv (preprint)"
paper_type: empirical
contribution_type: empirical
species:
  - human
tasks:
  - navigation_task
methods:
  - fmri
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - medial_temporal_lobe
keywords:
  - hippocampal_theta_oscillations
  - goal_distance_coding
  - theta_gamma_phase_amplitude_coupling
  - spatial_navigation
  - meg_source_localisation
  - fast_gamma
  - slow_gamma
  - entorhinal_cortex
  - theta_sequences
  - working_memory
  - abstract_state_space
  - path_distance
  - human
  - hippocampal
  - theta
  - oscillations
  - organise
  - distance
  - goal
  - coding
key_citations:
  - liu2023_hippocampus_amygdala_memory_formation
wiki_pages:
  - wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits
---

### One-line summary

Human hippocampal theta power during both spatial planning and active navigation scales with distance to a hidden goal, and theta-gamma phase-amplitude coupling increases dynamically as the goal is approached, with fast gamma in entorhinal cortex active during encoding of novel paths and slow gamma in hippocampus active during retrieval of familiar paths.

---

### Background & motivation

The hippocampal theta rhythm (6–12 Hz in rodents, 2–9 Hz in humans) is implicated in spatial coding and memory, with rodent studies showing that theta power correlates with running speed and that theta sequences of place-cell activity encode upcoming spatial trajectories. Whether these functions generalise to humans navigating in abstract state spaces — and whether theta-gamma phase-amplitude coupling mediates the encoding of upcoming path sequences — had not been directly tested in a healthy population using non-invasive neuroimaging. Prior evidence came mainly from intracranial EEG in epilepsy patients, leaving open questions about generalisability and the specific role of distinct gamma sub-bands. This paper addresses that gap using MEG in healthy participants performing an abstract navigation task.

---

### Methods

- **Participants**: 23 healthy adults (16 male, mean age 24.1 ± 4.89 years) recorded with whole-head 275-channel MEG (CTF-Omega, 600 Hz).
- **Task**: Abstract navigation in a 4x4 grid of images; participants moved step-by-step to a cued goal location using the shortest possible path (100 trials across 3 blocks). Crucially, the full map was never shown — only immediately adjacent locations were visible — so participants had to learn the layout over trials.
- **Trial structure**: 3 s fixation → 3 s goal cue (planning period) → 3 s frozen period → free navigation.
- **Key manipulation**: Trials classified as "correct" (shortest path taken, goal location known) vs. "incorrect" (suboptimal path, goal location uncertain); novel paths vs. previously traversed paths.
- **MEG analysis**: Time-frequency power estimated with Morlet wavelets (20 log-spaced bands, 1–30 Hz). LCMV beamformer source reconstruction on 10-mm MNI grid. Linear regression of trial-by-trial theta power (and TG-PAC) against step distance to goal in each source voxel; one-sample t-tests across participants; cluster-level FWE correction (p < 0.05), with hippocampal and entorhinal small-volume corrections.
- **Phase-amplitude coupling (PAC)**: Resultant vector length of theta phase (2–5 Hz) weighted by instantaneous gamma amplitude (30–70 Hz slow gamma; 70–140 Hz fast gamma) per trial per voxel; residualised for concurrent power changes before regression against goal distance.

---

### Key findings

- **Planning period (cue, 3 s)**: Right hippocampal 2–5 Hz theta power increased with shortest path distance to the goal in correct trials (t(22) = 4.11, p < 0.001) but not incorrect trials. This effect was driven by previously traversed paths (t(22) = 3.44, p = 0.0023) rather than novel paths.
- **Navigation period (step-by-step)**: Bilateral hippocampal theta power (both 2–5 Hz and 6–9 Hz) decreased iteratively as the goal was approached in correct trials. Regression against distance to goal was significant for 2–5 Hz (t(22) = 3.51, p = 0.002) and 6–9 Hz (t(22) = 5.71, p < 0.001) correct trials, but significantly weaker in incorrect trials (p < 0.003 for both bands). During navigation (unlike planning), goal-distance coding was present for both novel and previously traversed paths.
- **Theta-fast gamma PAC (2–5 Hz theta, 70–140 Hz fast gamma)**: PAC in right entorhinal cortex increased as the goal was approached (negative correlation with distance) in correct trials (t(22) = −2.90, p = 0.0082), driven specifically by novel paths (t(22) = −3.32, p = 0.0031) not previously traversed paths.
- **Theta-slow gamma PAC (2–5 Hz theta, 30–70 Hz slow gamma)**: PAC in right hippocampus increased as the goal was approached specifically for previously traversed paths (t(22) = −2.78, p = 0.0109), not novel paths; the difference between novel and traversed was significant (t(22) = −2.09, p = 0.048).
- Wide frontal theta increases during planning were not correlated with subsequent path length, consistent with a cognitive control rather than distance-coding role.

---

### Computational framework

The paper draws on the **theta-gamma neural code** framework (Lisman & Jensen, 2013; Lisman & Idiart, 1995). The core hypothesis is that individual memory items (here: upcoming spatial locations) are encoded by transient bursts of gamma-band activity nested at successive phases of each theta cycle. Under this model:
- Sequences of upcoming locations are represented as gamma bursts distributed across the theta cycle ("theta sweeps").
- Longer sequences (more locations remaining to the goal) produce a wider distribution of gamma across theta phases, resulting in *lower* theta-gamma phase-amplitude coupling.
- As the goal is approached and the remaining sequence shortens, gamma concentrates at fewer theta phases, increasing PAC.

The paper additionally invokes the **two-gamma-channel model** (Colgin et al., 2009) in which entorhinal-driven fast gamma (~70–140 Hz) supports encoding of new information, while intra-hippocampal slow gamma (~30–70 Hz) supports retrieval of previously stored sequences.

Key variables: theta phase (2–5 Hz), fast gamma amplitude (70–140 Hz), slow gamma amplitude (30–70 Hz), PAC (resultant vector length), step distance to goal.

---

### Prevailing model of the system under study

The paper's introduction situates itself within the established view that hippocampal theta oscillations serve as a temporal scaffold for spatial and mnemonic coding across mammalian species. The dominant prior model holds that:
1. Theta power in rodents covaries with running speed and reflects active engagement with the environment.
2. Hippocampal place cells fire at progressively earlier theta phases as an animal traverses their firing fields (theta phase precession), generating theta-scale sweeps of prospective spatial trajectories.
3. These theta sweeps are longer when animals plan routes to more distant goals (Wikenheiser & Redish, 2015).
4. In humans, intracranial theta power increases with distance to a goal during virtual navigation (Bush et al., 2017; Liu et al., 2023), but this evidence comes from patients with epilepsy.
5. Theta-gamma PAC is hypothesised to support sequential working memory (Lisman & Jensen, 2013), with fast gamma from entorhinal cortex and slow gamma from intra-hippocampal circuitry differentially supporting encoding and retrieval (Colgin et al., 2009).

The authors treat these as complementary but largely unintegrated frameworks, and test whether all three phenomena — goal-distance coding in theta power, dissociated fast/slow gamma channels, and PAC dynamics during navigation — can be observed non-invasively in healthy human participants.

---

### What this paper contributes

This paper extends previous intracranial findings to a healthy population using MEG, confirming that hippocampal theta power scales with goal distance during both planning and navigation. It goes further in several respects:
1. **Awareness dependence**: Goal-distance coding occurs only when participants know the shortest path, establishing that it reflects a cognitive representation rather than a pure spatial or motor correlate.
2. **Novel-vs-familiar dissociation during planning vs. navigation**: During planning, distance coding in the right hippocampus is restricted to familiar paths; during navigation, it is present for both novel and familiar paths.
3. **Entorhinal fast gamma for encoding, hippocampal slow gamma for retrieval**: For the first time in humans using non-invasive MEG, distinct theta-coupled gamma channels are shown to support navigation of novel vs. previously traversed routes, replicating the rodent framework in Colgin et al. (2009) and extending it to purposive goal-directed behaviour.
4. **Dynamic PAC increase approaching the goal**: TG-PAC increases dynamically within a trial as the goal is approached, consistent with the sequence-compression prediction of the theta-gamma code model.

---

### Brain regions & systems

- **Bilateral hippocampus** — primary locus of goal-distance coding in theta power during navigation; slow gamma theta-PAC for retrieval of familiar paths.
- **Right hippocampus** — dominant hemisphere for goal-distance coding during planning; also shows slow gamma PAC for previously traversed paths.
- **Prefrontal cortex / frontal midline** — large theta power increase during planning that does not covary with path distance; interpreted as reflecting cognitive control and working memory load rather than distance coding per se.
- **Right entorhinal cortex** — locus of fast gamma (70–140 Hz) theta-PAC that increases as the goal is approached, specifically during traversal of novel paths; consistent with its proposed role in encoding new spatial information.
- **Medial temporal lobe** — broader cluster including hippocampus and surrounding cortex showing theta power increases during planning.

---

### Mechanistic insight

The paper meets **both criteria** for mechanistic insight.

It formalises an algorithm (the theta-gamma sequence code: sequences of upcoming locations are represented as gamma bursts at successive theta phases, with PAC decreasing as sequence length grows) and provides neural data — MEG source-reconstructed oscillatory signals — that specifically support key predictions of this algorithm over alternatives.

**Computational level**: The brain computes and maintains a representation of the remaining path to goal, tracking the length of the upcoming sequence of locations to traverse. This enables goal-directed navigation by allowing flexible planning and error monitoring.

**Algorithmic level**: Upcoming locations are encoded as gamma-band bursts nested within theta cycles. As more locations remain (greater distance to goal), gamma is distributed more widely across theta phases, producing lower PAC. Theta power itself scales with sequence length as a proxy for total representational load. Importantly, two distinct algorithmic channels are used: fast gamma (~70–140 Hz) from entorhinal cortex for encoding new sequences (novel paths), and slow gamma (~30–70 Hz) from intra-hippocampal sources for retrieving previously stored sequences (familiar paths).

**Implementational level**: The paper localises these signals to specific anatomical structures (right hippocampus, right entorhinal cortex) using LCMV beamforming on MEG data, consistent with known anatomical projections (entorhinal→CA1 for encoding, CA3→CA1 recurrent collaterals for retrieval). However, specific cell types, receptor systems, or biophysical mechanisms are not addressed — this level is partially constrained but not directly measured.

---

### Limitations & open questions

- **Non-invasive MEG** provides lower spatial resolution than intracranial EEG; entorhinal and hippocampal signals may be difficult to fully disambiguate.
- **Abstract state space** (images on a grid) allows precise experimental control but may not fully generalise to real-world navigation, where egocentric and allocentric frames interact.
- **Theta frequency range**: Human hippocampal theta is often observed at 2–5 Hz in scalp/MEG recordings — lower than the canonical 6–12 Hz in rodents. The paper uses both a 2–5 Hz and a 6–9 Hz range but does not fully explain why two ranges are reported or how they differ mechanistically.
- **Directionality**: The study cannot determine the causal direction of interaction between frontal theta (possibly driving retrieval) and hippocampal theta (reflecting distance coding). The suggestion that frontal theta coordinates retrieval to produce hippocampal goal-distance signals is speculative.
- **Slow gamma PAC** for previously traversed paths in the right hippocampus is described as "marginally significant" at the corrected threshold (pFWE,SVC = 0.051), which requires some caution in interpretation.
- **Open question**: What drives the transition between entorhinal fast gamma (encoding) and hippocampal slow gamma (retrieval)? Are these competing or complementary channels, and what determines which is engaged on a given trial?
- The study does not examine grid-cell-like signals or entorhinal distance coding (Euclidean vs. path distance), which would be a natural extension of the Howard et al. (2014) fMRI framework.

---

### Connections & keywords

- **Key citations**: Bush et al. (2017, PNAS) — human hippocampal theta and movement onset/distance; Liu et al. (2023, Current Biology) — multi-scale goal distance in human hippocampus; Colgin et al. (2009, Nature) — fast/slow gamma channels in hippocampus; Lisman & Jensen (2013, Neuron) — theta-gamma neural code; Wikenheiser & Redish (2015, Nature Neuroscience) — hippocampal theta sequences reflect current goals; Howard et al. (2014, Current Biology) — hippocampal/entorhinal goal distance coding in fMRI; Heusser et al. (2016, Nature Neuroscience) — theta-gamma PAC and episodic sequence memory; Daume et al. (2024, Nature) — working memory control by theta-gamma coupling; Adams et al. (2020, Brain) — theta phase coupling impaired in schizophrenia.
- **Named models or frameworks**: Theta-gamma neural code (Lisman & Jensen, 2013); two-gamma-channel model (Colgin et al., 2009); theta phase precession; theta sweeps; LCMV beamformer; abstract navigation task (4x4 grid).
- **Brain regions**: Hippocampus (bilateral, right, left), entorhinal cortex (right), prefrontal cortex / frontal midline, medial temporal lobe.
- **Keywords**: hippocampal theta oscillations, goal distance coding, theta-gamma phase-amplitude coupling, spatial navigation, MEG source localisation, fast gamma, slow gamma, entorhinal cortex, theta sequences, working memory, abstract state space, path distance.

### Related wiki pages
- [[wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits|Prospective spatial coding in hippocampal–medial prefrontal circuits]]
