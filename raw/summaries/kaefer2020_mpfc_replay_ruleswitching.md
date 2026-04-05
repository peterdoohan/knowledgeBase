---
source_file: kaefer2020_mpfc_replay_ruleswitching.md
title: "Replay of Behavioral Sequences in the Medial Prefrontal Cortex during Rule Switching"
authors: Karola Kaefer, Michele Nardin, Karel Blahna, Jozsef Csicsvari
year: 2020
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

The medial prefrontal cortex (mPFC) replays temporally ordered sequences of generalized spatial positions during awake immobility, independently of hippocampal replay, and this mPFC replay positively correlates with rule-switching performance in rats.

---

### Background & motivation

Replay — the reactivation of sequential neural activity patterns during immobility — is well established in the hippocampus, where it is thought to support memory consolidation and future planning. The mPFC is critical for flexible, rule-guided behavior, and sleep replay in the mPFC has been reported, but whether the mPFC can replay sequential experiences during the awake state to support task execution was unknown. This paper fills that gap by testing awake mPFC replay in a task that specifically requires mPFC function (rule switching), comparing its content, timing, and behavioral relevance to simultaneous hippocampal replay.

---

### Methods

- **Subjects**: 4 male Long-Evans rats implanted with 32-tetrode microdrives targeting dorsal CA1 (HPC, unilateral) and prelimbic mPFC (bilateral); 817 mPFC and 1,025 HPC putative principal cells recorded across 13 sessions.
- **Task**: Plus-maze rule-switching task requiring animals to alternate between a spatial rule (always go east/west) and a light-guided rule (follow cue light); unannounced rule changes produced pre-switch, switching, and post-switch behavioral blocks.
- **Spatial coding analysis**: Linearized 1D Bayesian decoding of position from spiking activity; population vector correlations between symmetric maze arms to quantify generalization.
- **Replay detection**: Position decoding during immobility using fixed-spike-count windows; trajectory score combining decoding probability score and smoothness score, compared against place-field rotation shuffles; significant events defined as above the 95th percentile of their shuffled distribution; events extended iteratively if additional windows remained significant.
- **Coordination analysis**: Cross-correlation of HPC and mPFC trajectory replay event times; co-occurrence with hippocampal sharp-wave ripples (SWRs).
- **Behavioral correlates**: Spearman correlations between trajectory replay rate (events per immobility time) in switching block and number of trials to switch; replay rates separated by correct vs. error trials and by ahead vs. behind replay direction.

---

### Key findings

- **mPFC generalized spatial code**: mPFC neurons fired symmetrically in both start arms and both goal arms, representing relative position (start-to-goal) rather than specific allocentric locations. 1D Bayesian decoding of relative position yielded error of 16 ± 3 cm vs. 46 ± 3 cm for 2D decoding (p = 0.0015). HPC showed no such improvement with 1D decoding (14 ± 1 cm in both cases).
- **mPFC awake trajectory replay**: During awake immobility, mPFC replayed temporally ordered sequences of generalized positions (9% of immobility time contained significant events). Both forward and reverse replays were detected. Replay events in mPFC were longer (median 0.74 s) than in HPC (median 0.33 s, p < 0.00001) but showed slower replay speeds (95% CI: ±186 cm/s vs. ±491 cm/s in HPC).
- **HPC and mPFC replay are temporally independent**: Cross-correlation of replay event times showed no peaks; only ~5% of mPFC replay events co-occurred with HPC replay events. However, 40% of mPFC replay events co-occurred with hippocampal SWRs (significantly above chance, p = 0.02), suggesting association with hippocampal population events without precise temporal coupling.
- **mPFC replay correlates positively with performance**: mPFC trajectory replay rate during the switching block negatively correlated with trials needed to switch (center: r = −0.76, p = 0.01; goal: r = −0.63, p = 0.02) — i.e., more mPFC replay predicted faster rule switching. HPC replay at the goal positively correlated with trials to switch (r = 0.71, p = 0.009), indicating a negative correlation with performance.
- **Replay during error vs. correct trials**: mPFC goal replay was higher during error trials (p = 0.009). At the maze center, mPFC ahead replay (pointing toward goal) was increased during error trials while behind replay was increased during correct trials, suggesting forward and reverse mPFC replays serve distinct functions.
- **mPFC replay at goal replays current goal arm**: Replay events at the goal preferentially decoded the current goal arm (p < 0.00001 vs. chance, binomial test).

---

### Computational framework

**Bayesian position decoding**: The paper applies a Poissonian-likelihood Bayesian decoder to reconstruct position from population spiking activity, using linearized 1D rate maps. The framework assumes neurons fire independently with Poisson statistics, and position is estimated as the maximum likelihood over spatial bins. This is used both to characterize the generalized spatial code and to detect and score sequential replay events.

**Trajectory scoring**: A custom trajectory score combines a decoding probability score (how well successive spiking windows follow a linear trajectory, using a Gaussian kernel transition model) and a smoothness score (how improbable it is that the observed sequence ordering could arise by permutation). This provides a formal, shuffle-validated measure of sequential structure in population activity.

The broader computational framing is that mPFC trajectory replay constitutes offline sequential reactivation that may support schema-based evaluation or rule learning — essentially using replay to re-run or abstract experience for flexible behavioral updating. No explicit mathematical model of mPFC function (e.g., RL or Bayesian inference) is proposed.

---

### Prevailing model of the system under study

Before this paper, the field understood awake replay as a predominantly hippocampal phenomenon, with the mPFC playing a supporting or recipient role. Sleep replay in the mPFC had been demonstrated (Euston et al., 2007; Peyrache et al., 2009), and the mPFC was known to have some spatial firing (Fujisawa et al., 2008; Hok et al., 2005). The dominant view was that coordinated hippocampal-mPFC reactivation during hippocampal SWRs is the mechanism by which the hippocampus communicates with the mPFC (Jadhav et al., 2016; Tang et al., 2017), and that the mPFC contributes to rule-guided behavior through persistent activity and ensemble dynamics (Durstewitz et al., 2010) rather than through independent sequential replay. Whether the mPFC could independently generate sequential trajectory replay in the awake state was an open question.

---

### What this paper contributes

This paper demonstrates, for the first time, that the mPFC can generate awake trajectory replay — temporally ordered sequential reactivation of generalized behavioral positions — independently of hippocampal replay. Key contributions:

1. The mPFC holds a generalized, trajectory-independent spatial code (relative position between start and goal), unlike the HPC's allocentric place code — establishing what information mPFC replay reactivates.
2. Awake mPFC replay is temporally independent from HPC replay (not cross-correlated), even though it co-occurs with hippocampal SWRs at above-chance rates. This dissociates mPFC replay from HPC-driven reactivation.
3. mPFC replay rate positively predicts rule-switching speed, while HPC replay rate at the goal negatively predicts it — demonstrating behavioral relevance and opposing functional roles.
4. Within-trial analysis shows mPFC ahead replay increases on error trials, consistent with a prospective evaluation or schema-updating function, whereas behind replay increases on correct trials.

The paper establishes sequential replay as a computation implemented across multiple brain areas, with the mPFC version serving mPFC-specific functions (flexible rule updating) rather than copying hippocampal content.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC) / prelimbic area** — primary region of interest; shown to generate generalized spatial representations and independent awake trajectory replay; replay rate predicts rule-switching performance.
- **Dorsal hippocampus CA1 (HPC)** — comparison region; provides allocentric place code; generates trajectory replay with different properties and opposite behavioral correlations; source of SWRs that temporally associate (but do not coordinate) with mPFC replay.

---

### Mechanistic insight

The paper meets criterion 1 (a computational process is described: sequential Bayesian-decoded trajectory reactivation in the mPFC) and criterion 2 (neural recordings directly support this in behaving rats). There is therefore a case for mechanistic insight, though it is partial.

- **Computational level**: The problem is flexible behavioral adaptation following unannounced rule changes. The mPFC must identify which rule is currently operative and update its behavioral policy. The paper proposes that replay of the generalized task structure (start-to-goal trajectories) supports this, possibly through repeated evaluation of choices and outcomes or schema-based assimilation of the new rule.
- **Algorithmic level**: The mPFC represents a compressed, trajectory-independent version of spatial experience (relative position), and during immobility reactivates sequential patterns of these generalized positions in both forward and reverse order. The rate of these reactivations (not a single event) predicts how efficiently the animal switches rules, suggesting an evidence-accumulating process across trials. Ahead replay at the goal (prospective) is elevated on error trials; behind replay at the center (retrospective) is elevated on correct trials — consistent with distinct computational roles for forward vs. reverse replay.
- **Implementational level**: Population activity increases transiently during mPFC replay events, resembling HPC replay dynamics. mPFC replay does not require local mPFC ripples (no difference in 100–150 Hz power during replay vs. baseline), but co-occurs with hippocampal SWRs, leaving open whether hippocampal input influences (without driving) mPFC replay timing. Specific cell types, connectivity patterns, or neuromodulatory mechanisms are not addressed.

The paper does not resolve what biophysical mechanism generates mPFC sequential reactivation in the absence of local ripples, and it does not test whether mPFC replay is causal to rule switching (e.g., via inhibition experiments). The mechanistic account is therefore incomplete at the implementational level.

---

### Limitations & open questions

- Only 4 rats; correlations between replay rate and switching performance are based on 13 sessions, limiting statistical power.
- Causality not established: mPFC replay is correlated with performance but not shown to be necessary (no disruption experiments analogous to SWR suppression studies in HPC).
- The mechanism generating awake mPFC sequential replay is unknown — there are no local ripples, so the trigger differs from hippocampal replay.
- The paper cannot fully exclude that mPFC replay is driven by upstream input (e.g., medial entorhinal cortex, which shows independent replay) rather than being intrinsically generated.
- Temporal independence of HPC and mPFC replay events is shown, but the paper notes this could reflect different functional modes (independent mPFC replay for within-mPFC computation; coordinated HPC-mPFC replay for consolidation) — these are not empirically distinguished.
- mPFC goal arm identity decoding was only 76% accurate, meaning replay content analysis (current vs. previous goal arm) has limited precision.
- The paper cannot determine whether mPFC replay causes improved switching or is a correlate of an underlying capacity that enables both.

---

### Connections & keywords

**Key citations**:
- Euston et al., 2007 (Science) — mPFC sleep replay
- Peyrache et al., 2009 (Nature Neuroscience) — mPFC sleep replay after rule switch
- Jadhav et al., 2016 (Neuron) — HPC-mPFC reactivation during SWRs
- Foster & Wilson, 2006 (Nature) — awake hippocampal reverse replay
- Davidson et al., 2009 (Neuron) — hippocampal replay of extended experience
- Singer et al., 2013 (Neuron) — HPC SWR activity predicts correct decisions
- O'Neill et al., 2017 (Science) — independent replay in entorhinal cortex
- Mashhoori et al., 2018 (eLife) — anterior cingulate non-local recall
- Durstewitz et al., 2010 (Neuron) — mPFC ensemble state transitions in rule learning
- Tse et al., 2007 (Science) — schemas and memory consolidation

**Named models or frameworks**:
- Bayesian position decoding (Zhang et al., 1998)
- Trajectory score (decoding probability + smoothness score)
- Schema theory (Tse et al., 2007) — invoked interpretively

**Brain regions**:
- Medial prefrontal cortex (prelimbic area)
- Dorsal hippocampus CA1

**Keywords**:
- awake trajectory replay
- medial prefrontal cortex
- rule switching
- generalized spatial code
- Bayesian decoding
- sharp-wave ripples
- hippocampal-prefrontal coordination
- sequential reactivation
- forward and reverse replay
- flexible behavior
- schema
- plus maze
