---
source_file: "kaefer2020_replay_prefrontal_rule_switching.md"
paper_id: "kaefer2020_replay_prefrontal_rule_switching"
title: "Replay of Behavioral Sequences in the Medial Prefrontal Cortex during Rule Switching"
authors: "Karola Kaefer, Michele Nardin, Karel Blahna, Jozsef Csicsvari"
year: 2020
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["tetrode_recording", "bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex", "medial_prefrontal_cortex"]
keywords: ["replay", "behavioral", "sequences", "medial", "prefrontal", "cortex", "during", "rule", "switching"]
key_citations: ["davidson2009_hippocampal_replay_extended", "jadhav2016_hippocampal_prefrontal_swr"]
---

### One-line summary

During awake immobility on a rule-switching task, rat medial prefrontal cortex replays temporally ordered sequences of generalized spatial positions, and the rate of this replay positively correlates with rule-switching performance, occurring independently of concurrent hippocampal replay.

---

### Background & motivation

Replay of sequential neural activity patterns — first characterised in the hippocampus — is thought to underlie memory consolidation and flexible decision-making. The mPFC is known to be essential for rule switching and has been shown to replay task-related patterns during sleep, but whether it can produce ordered trajectory replay in the awake state, and whether such replay is functionally relevant to behaviour, was unknown. Critically, the relationship between mPFC replay and hippocampal replay during a task that requires both regions had not been examined. This paper fills that gap by directly comparing awake mPFC and hippocampal (CA1) replay during a mPFC-dependent rule-switching task.

---

### Methods

- **Subjects**: 4 male Long-Evans rats.
- **Task**: Rule-switching task on a plus maze; rats alternated between a spatial (go-east/go-west) and a light-guided rule. Rule changes were unannounced, requiring trial-and-error adaptation. Sessions divided into pre-switch, switching, and post-switch blocks.
- **Recordings**: Simultaneous 32-tetrode microdrive recordings targeting dorsal CA1 (hippocampus, HPC) and prelimbic mPFC bilaterally (817 mPFC and 1,025 HPC putative principal cells across 13 sessions).
- **Spatial coding analysis**: 2D vs. linearised 1D Bayesian positional decoding; population vector correlations between maze arms to quantify generalisation.
- **Replay detection**: Spiking-windows (fixed spike-count windows) during immobility; trajectory scores combining a decoding probability score and a smoothness score, validated against place-field rotation shuffles. Significant events extended iteratively if they passed the 95th-percentile threshold.
- **Behavioral correlates**: Spearman rank-order correlation between session-level mean trajectory replay rate and trials required to switch. Replay rates analysed separately at maze center and goal, and split by ahead vs. behind direction.
- **Network oscillations**: LFP analysis of hippocampal SWRs (150–250 Hz), mPFC ripples (100–150 Hz), and gamma power (30–90 Hz) during replay events.
- **Cross-correlation**: Temporal alignment of HPC and mPFC trajectory replay events tested with time-shift cross-correlation.

---

### Key findings

- **mPFC generalises spatial representations**: mPFC cells fired symmetrically at equivalent positions across both start arms and both goal arms (population vector correlation ~0.89–0.92), encoding relative position between start and goal rather than specific 2D locations. HPC cells had distinct representations for each arm (correlation ~0.06–0.07). 1D linearised decoding was far more precise for mPFC (error: 16 ± 3 cm) than 2D decoding (46 ± 3 cm; p = 0.0015).
- **mPFC generates awake trajectory replay**: During 9% of immobile time, mPFC replayed ordered sequences of generalised positions resembling full trajectories. Replay events occurred in both forward and reverse order. Duration was longer than HPC events (median: mPFC 0.74 s vs. HPC 0.33 s; p < 0.00001) and replay speed narrower (95th CI: ±191 cm/s vs. ±491 cm/s for HPC).
- **mPFC and HPC replay are temporally independent**: Cross-correlation of HPC and mPFC trajectory events showed no peak (only 5% of mPFC events co-occurred with HPC events). However, 40% of mPFC replay events co-occurred with hippocampal SWRs, significantly more than chance (p = 0.02), indicating mPFC replay is associated with SWR activity but not with concurrent trajectory replay in HPC.
- **mPFC replay correlates positively with rule-switching performance**: mPFC trajectory replay rate during the switching block negatively correlated with trials needed to switch (center: r = −0.76, p = 0.01; goal: r = −0.63, p = 0.02). Conversely, HPC goal replay positively correlated with trials to switch (r = 0.71, p = 0.009), i.e., more HPC replay was associated with worse switching performance.
- **mPFC replay is elevated during error trials**: mPFC replay at the goal was higher during error than correct trials (p = 0.009). At the center, mPFC ahead-replay was higher during error trials and behind-replay was higher during correct trials (p = 0.006 and p = 0.003, respectively), suggesting directionally specific functional roles.
- **mPFC replay is robust**: Results held across multiple alternative replay quality metrics (Davidson et al. and Gupta et al. scores), different spatial bin sizes (2.5–10 cm), and fixed time windows. Inclusion of cell identity shuffling did not invalidate results (85–87% of events survived additional shuffle).

---

### Computational framework

Not an explicitly computational paper — no formal model is constructed. However, the analyses rely heavily on **Bayesian positional decoding**, treating mPFC population activity as a probabilistic representation of linearised maze position. The decoding algorithm assumes Poissonian, independent firing from each cell, and infers position as the maximum-likelihood estimate over spatial bins given measured firing rates. Trajectory detection computes a composite score (decoding probability × smoothness), tested against a shuffle distribution.

Implicitly, the paper is framed around a **schema/associative structure** account: the mPFC holds a generalised, task-context representation (start-to-goal abstraction) rather than an allocentric map, and replay of this structure is proposed to support evidence accumulation and rule updating across trials.

---

### Prevailing model of the system under study

The introduction presents a clear prior landscape. The hippocampus is the canonical site of awake trajectory replay, supported by sharp-wave ripples; disrupting SWRs impairs spatial task performance (Jadhav et al., 2012). The mPFC is known to be critical for flexible rule switching (lesion studies: Floresco et al., 2008; Ragozzino et al., 1999; Milner, 1963), and mPFC-hippocampal synchrony increases during rule switching (Benchenane et al., 2010). Previous work had shown mPFC replay during sleep (Euston et al., 2007; Peyrache et al., 2009) and correlated reactivation of mPFC-HPC cell pairs during task performance (Jadhav et al., 2016; Tang et al., 2017), but the prevailing assumption was that awake mPFC replay had not been demonstrated and that mPFC replay, if it occurred, would likely be coordinated with hippocampal SWRs. The mPFC was not thought to represent spatial trajectories in the granular, location-specific way the hippocampus does.

---

### What this paper contributes

The paper establishes three novel findings. First, mPFC spatial representations are genuinely generalised — not merely noisy place fields — forming a trajectory-invariant (start-to-goal) code that differs fundamentally from hippocampal allocentric coding. Second, the mPFC is capable of awake trajectory replay during immobility, extending beyond single non-local event reactivations to full ordered sequences, occurring in both forward and reverse directions — a property previously attributed primarily to the hippocampus. Third, and most importantly, mPFC replay is functionally dissociated from hippocampal replay: the two are temporally independent (no cross-correlation peak), show opposite correlations with rule-switching performance, and show opposite patterns across error versus correct trials. This challenges the assumption that mPFC replay is simply downstream of or coordinated with hippocampal SWR-driven replay, instead suggesting that mPFC replay serves a distinct computational role — possibly evidence accumulation or schema-based evaluation of the new rule — that is separable from hippocampal mnemonic functions.

---

### Brain regions & systems

- **Medial prefrontal cortex (prelimbic area, mPFC)** — primary locus of investigation; shown to encode generalised start-to-goal position, to generate awake trajectory replay, and to have replay rate that predicts rule-switching performance.
- **Dorsal hippocampus CA1 (HPC)** — comparison region; encodes discrete allocentric positions, generates awake trajectory replay, but replay rate inversely predicts rule-switching performance (more HPC goal replay = worse switching); replay events occur independently of mPFC replay events.
- **Hippocampal sharp-wave ripple system** — mPFC replay co-occurs with hippocampal SWRs at above-chance rates (40%), even though mPFC and HPC trajectory events are not temporally correlated; implicates SWR-related activity as a permissive context for mPFC replay without requiring co-replay.

---

### Mechanistic insight

The paper meets both criteria for mechanistic insight.

1. **Algorithm**: The paper proposes that mPFC trajectory replay (a sequential reactivation process operating over generalised positional representations) implements evidence accumulation or schema-based rule evaluation across trials during the switching block.
2. **Neural data**: Electrophysiological recordings (tetrode-based multi-unit recordings from mPFC and CA1 simultaneously) directly support the proposed algorithm: replay events are statistically significant against shuffles, are associated with transient population firing rate changes, and the rate of these events specifically predicts behavioural performance on the rule-switching dimension (not general immobility duration or running speed).

**Marr's three levels:**

- **Computational**: The problem is determining the currently relevant rule after an unannounced switch. The mPFC must evaluate recent experience against a generalised task schema to identify whether the current reward contingency has changed and which rule is now in force.
- **Algorithmic**: Sequential reactivation of linearised start-to-goal position sequences during awake immobility, using population firing patterns that generalise across specific arm identities (symmetric code). The representation abstracts over trajectory-specific details, preserving task-structural relationships. Ahead-replay (pointing toward goal) during error trials and behind-replay (pointing toward start) during correct trials suggest directional asymmetry in the content of replay.
- **Implementational**: mPFC pyramidal cell ensembles; no SWR equivalent in mPFC (ripple power not elevated during mPFC replay). Replay co-occurs with hippocampal SWRs above chance, suggesting hippocampal network state may modulate mPFC replay probability without dictating its timing or content. Specific cell types and molecular mechanisms are not addressed.

**Bonus**: The paper does not address specific cell types, neuromodulators, or biophysical mechanisms of mPFC replay initiation.

---

### Limitations & open questions

- Only 4 rats (13 sessions), limiting statistical power; correlations with performance are based on session-level means.
- The replay detection method uses linearised 1D rate maps that collapse arm identity; most replay events cannot be assigned to a specific arm, limiting interpretation of what exactly is being replayed.
- The functional interpretation (evidence accumulation vs. evaluation vs. schema retrieval) remains speculative; causal interventions (e.g., SWR or mPFC replay disruption) were not performed.
- mPFC replay co-occurs with hippocampal SWRs at above-chance rates, but the direction of influence (hippocampus drives mPFC, mPFC drives hippocampus, or shared upstream input) is unresolved; medial entorhinal cortex is proposed as a possible upstream driver.
- The paper cannot distinguish whether mPFC replay is causal for rule switching or merely correlates with it; a single replay event at the goal did not improve next-trial performance, suggesting any effect is cumulative but the mechanism is unclear.
- Only prelimbic mPFC was targeted; other subregions (infralimbic, anterior cingulate) were not examined.
- Replay during sleep after the task was not investigated; any consolidation role is therefore unaddressed.

---

### Connections & keywords

**Key citations**:
- Euston et al. (2007) — first demonstration of mPFC replay during sleep
- Peyrache et al. (2009) — mPFC sleep replay after rule switching
- Jadhav et al. (2012) — awake hippocampal SWRs support spatial memory
- Davidson et al. (2009) — hippocampal replay of extended experience
- Foster & Wilson (2006) — reverse replay in hippocampal place cells
- Benchenane et al. (2010) — mPFC-HPC theta synchrony during rule switching
- O'Neill et al. (2017) — independent replay in medial entorhinal cortex
- Mashhoori et al. (2018) — awake non-local mPFC reactivation
- Jadhav et al. (2016) — coordinated mPFC-HPC ensemble activity during SWRs
- Tse et al. (2007) — schemas and memory consolidation

**Named models or frameworks**:
- Bayesian positional decoding (Zhang et al., 1998 formalism)
- Trajectory score (decoding probability + smoothness composite measure)
- Davidson et al. replay score; Gupta et al. replay score (used for validation)
- Schema theory (Tse et al., 2007) — invoked in discussion

**Brain regions**:
- Medial prefrontal cortex (prelimbic area, mPFC)
- Dorsal hippocampus CA1 (HPC)

**Keywords**:
- awake trajectory replay
- medial prefrontal cortex
- rule switching
- generalised spatial coding
- sharp-wave ripples
- Bayesian decoding
- immobility reactivation
- hippocampal-prefrontal interaction
- schema representation
- forward and reverse replay
- behavioural flexibility
- sequence reactivation
