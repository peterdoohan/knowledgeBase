---
source_file: bohm2020_pfc_spatial_working_memory.md
paper_id: bohm2020_pfc_spatial_working_memory
title: "Canonical goal-selective representations are absent from prefrontal cortex in a spatial working memory task requiring behavioral flexibility"
authors:
  - "Claudia Böhm"
  - "Albert K Lee"
year: 2020
journal: eLife
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - electrophysiology
  - neuropixels
  - behavioral_analysis
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - prelimbic_cortex
  - infralimbic_cortex
keywords:
  - spatial_working_memory
  - prefrontal_cortex
  - goal_representation
  - flexible_behavior
  - population_decoding
  - delay_period_activity
  - activity_silent_working_memory
  - neuropixels
  - rodent_electrophysiology
  - behavioral_flexibility
  - task_structure_encoding
  - null_result_working_memory
  - canonical
  - goal
  - selective
  - representations
  - absent
  - prefrontal
  - cortex
  - spatial
key_citations:
  - fujisawa2008_assembly_prefrontal_cortex
wiki_pages:
  - wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory
---

### One-line summary

In a novel flexible spatial working memory task in rats, medial prefrontal cortex (mPFC) neurons showed no evidence of current-goal-specific activity in any previously reported form during the delay period, suggesting canonical PFC working memory representations do not generalise to conditions requiring true behavioral flexibility.

---

### Background & motivation

The PFC is widely held to maintain working memory representations of current goals, supporting flexible goal-directed behavior. Prior rodent spatial working memory studies (T-mazes, single-start paradigms) confound goal-specific neural activity with direction, route, or motor plan representations, making it difficult to isolate a pure goal memory signal. This paper addresses that gap by designing a task that demands genuine flexibility — multiple start locations, multiple routes, and multiple goals — so that only the goal location itself is the invariant variable that must be held in memory. The question is whether the PFC holds a goal representation that can be deployed under such conditions.

---

### Methods

- **Task (MSMGMR — multi-start/multi-goal/multi-route)**: Rats navigated an elevated maze with 3 goal locations, 3 start locations, and 3 routes (bridges raised/lowered). On each trial, a cued sample phase guided the animal to the current goal; a 3 s nosepoke delay period followed; then a test phase required navigation to the same goal from a pseudorandomly assigned start via a pseudorandomly revealed route. This design dissociates goal identity from direction, route, and motor plan.
- **Subjects**: 3 male Long-Evans rats; additional 2 sessions from 2 animals in a rotation/relearning experiment.
- **Recording**: Chronic Neuropixels 1.0 probe implanted in mPFC (spanning anterior cingulate, prelimbic, infralimbic, and dorsal peduncular cortices); 98–182 units recorded per main session; 68–97 stable putative principal cells included per session after quality filtering.
- **Analyses targeting all major forms of working memory coding**:
  - Population vector (PV) correlation between delay period activity and sample-phase goal activity
  - Time-resolved goal decoding using sliding-window PV correlation
  - Single-cell firing rate analysis (H-score / Kruskal-Wallis) for allocentric, egocentric, and start-dependent goal coding
  - Population-level supervised classification (logistic regression, SVM, random forest, Naive Bayes) across a range of time bin resolutions
  - LFP phase analysis (2.5–5, 5–12, 15–30 Hz bands) for goal-specific phase tuning and phase-dependent spike count coding
  - Pairwise covariance analysis (cross-correlation selectivity index, CCSI) for activity-silent working memory (following Barbosa et al., 2020)
  - t-SNE of population vectors at key task locations
  - Relearning experiment: maze rotated 60° mid-session to elevate cognitive demand during re-acquisition

---

### Key findings

- **No goal-specific delay period activity in any tested form**: Neither firing rates, sequential activity patterns, LFP phase tuning, nor pairwise covariances (excitatory or inhibitory pairs) distinguished the currently remembered goal during the delay period — across all three animals, all mPFC subareas, all time bin resolutions, and all classification methods.
- **Current start location was robustly decodable**: The animal's current position (nosepoke start) was readily decoded at all time resolutions, confirming the dataset was large enough to detect real effects and that the null result for goal decoding is not a power failure.
- **Goal decoding outside the delay period tracks behavior**: Goal identity could be decoded from neural data at various other task time points (sample phase arrival, test phase choice point, etc.), but the same decoding accuracy was achieved from behavioral tracking data (head-LED position) alone — suggesting these signals reflect the animal's physical location or posture, not mnemonic content.
- **No evidence during relearning**: After 60° maze rotation, performance dropped then gradually recovered. Even during this cognitively demanding relearning phase, goal-selective delay activity was not detectable, while start location remained decodable.
- **mPFC encodes task structure, not current goal**: t-SNE analysis revealed that mPFC population activity organized locations by behavioral equivalence class (goals together, starts together, routes together), rather than by current goal identity. Spatial selectivity within each location class was also present.
- **Error information**: Activity during the delay period did not predict upcoming or past errors, further arguing against a role in moment-to-moment goal memory storage.

---

### Computational framework

Not applicable in the sense that the paper does not develop or fit a computational model. The study uses population decoding methods (linear classifiers, correlation-based decoding, dimensionality reduction via t-SNE) as analysis tools to test whether the neural population state contains information about goal identity. These tools implicitly assume a linear readout framework: if goal identity is decodable by a linear classifier from population vectors, a downstream area could read it out.

The paper's argument is essentially a null result against multiple candidate neural codes for working memory (persistent rate codes, sequential codes, phase codes, covariance / activity-silent codes). The positive finding — that mPFC organises activity by behavioural equivalence class — is consistent with the idea that PFC encodes long-term task structure rather than transiently maintained goal representations. The results constrain attractor-network models (e.g. bump attractor, Wimmer et al., 2014) and synaptic working memory models (Mongillo et al., 2008) by showing that, under conditions of genuine flexibility, neither sustained firing nor detectable synaptic trace variants are present in mPFC.

---

### Prevailing model of the system under study

The paper opens against the backdrop of a strong consensus view: the PFC is the primary neural substrate for working memory, particularly the temporary maintenance of goal-relevant information. This view is grounded in decades of primate electrophysiology showing sustained, stimulus-selective delay period firing in PFC (Fuster & Alexander 1971; Funahashi et al., 1989; Miller et al., 1996; Romo et al., 1999), and reinforced by rodent PFC studies showing memory-correlated activity in spatial tasks (Baeg et al., 2003; Fujisawa et al., 2008). Various coding schemes have been proposed and supported: tonic elevated/suppressed firing in single cells, sequential activity patterns tiling the delay, LFP phase coding, and covariance-based activity-silent storage (Barbosa et al., 2020). The authors accept that simpler tasks do sometimes reveal goal-correlated delay activity in PFC; their challenge is to the claim that such representations constitute a general working memory mechanism capable of supporting flexible, context-independent behavior.

---

### What this paper contributes

The paper provides the strongest evidence to date that canonical PFC working memory representations — including all major forms documented in the literature — are absent when the task genuinely requires flexible use of the memorised goal. Prior positive findings may have been driven by confounds between goal identity and direction, route, or motor plan in simpler task designs. The key new claims are:

1. No form of goal-selective delay period activity (rate, sequence, phase, or covariance) is detectable in mPFC when goal information must be deployed flexibly across starting positions and routes.
2. The apparent goal decoding found at other task time points is fully explained by the animal's concurrent physical location and posture — not by a goal memory signal.
3. mPFC does represent task structure: it groups behaviorally equivalent locations together in its population code, consistent with a role in encoding long-term structural knowledge rather than transient working memory content.
4. The null result holds even during relearning (elevated cognitive demand), making it unlikely the effect was masked by expertise.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)** — primary recording site; the study tests and rejects the hypothesis that mPFC holds goal-specific working memory representations under flexible task conditions; positive evidence for mPFC encoding of spatial context and behavioural equivalence classes.
  - Subareas recorded: anterior cingulate cortex (ACC), prelimbic cortex (PrL), infralimbic cortex (IL), dorsal peduncular cortex (DP). Results were similar across subareas.

---

### Mechanistic insight

The paper meets one of the two required criteria: it provides neural recordings that test specific candidate algorithms for working memory (rate codes, sequential codes, phase codes, covariance codes). However, it does not propose or formalise a new algorithm — it is primarily a null result against existing frameworks. The positive finding (behavioural equivalence grouping) is descriptive rather than mechanistic.

**Why the bar is not fully met**: The paper exhaustively rules out several algorithms using neural data, but does not provide evidence specifically supporting one particular algorithm over alternatives. The t-SNE / PV clustering result is consistent with PFC encoding task structure, but does not constitute a formal algorithmic account. No neural implementation (cell types, connectivity, neuromodulation) is investigated.

That said, the data do constrain the mechanistic landscape at Marr's algorithmic level: the mPFC is not implementing a pattern-completion or bump-attractor readout of goal identity during the delay; it is instead maintaining a map of behavioural equivalence that may support long-term task knowledge retrieval rather than moment-to-moment working memory.

---

### Limitations & open questions

- Small sample (n = 3 rats, one session per animal for main analyses); results are consistent across animals but statistical power is limited for detecting weak or sparse goal-coding signals.
- Only mPFC was recorded; other areas that might hold flexible goal representations (e.g. hippocampus, orbitofrontal cortex, posterior parietal cortex) were not examined simultaneously.
- The null result for delay period goal coding could in principle reflect an as-yet-undiscovered coding scheme not tested here (e.g. sparse or low-dimensional codes that escape the classifiers used, or coding in subthreshold synaptic dynamics not accessible to spiking data).
- The relearning experiment used only 2 animals and a single session each; conclusions about learning-related changes in PFC coding are therefore tentative.
- The paper does not determine what brain area does hold the flexible goal memory — this remains an open and pressing question.
- Whether the positive findings (behavioural equivalence grouping) reflect a genuine long-term structural code or are an epiphenomenon of the training history is not established.
- The task required months of training; it is possible that well-trained animals offloaded goal memory to other circuits (e.g. hippocampus) in a way that would not occur in humans or primates performing analogous tasks.

---

### Connections & keywords

**Key citations**:
- Funahashi, Bruce & Goldman-Rakic (1989) — classic primate PFC delay activity
- Fuster & Alexander (1971) — original PFC delay period firing report
- Miller, Erickson & Desimone (1996) — PFC working memory in macaque
- Romo et al. (1999) — parametric working memory in PFC
- Spellman et al. (2015) — rodent PL mPFC hippocampal-prefrontal working memory
- Bolkan et al. (2017) — thalamo-prefrontal working memory
- Barbosa et al. (2020) — activity-silent working memory via pairwise covariances
- Mongillo, Barak & Tsodyks (2008) — synaptic theory of working memory
- Wimmer et al. (2014) — bump attractor dynamics in PFC working memory
- Kim et al. (2016) — interneuron types and working memory
- Freedman et al. (2001) — PFC long-term categorical representations
- Jung et al. (1998) — deep layer PFC neurons in spatial working memory
- Inagaki et al. (2019) — discrete attractor dynamics in frontal cortex

**Named models or frameworks**:
- Multi-start/multi-goal/multi-route (MSMGMR) task — novel task paradigm introduced in this paper
- Population vector (PV) decoding
- Cross-correlation selectivity index (CCSI, from Barbosa et al. 2020)
- t-distributed stochastic neighbor embedding (t-SNE)
- Activity-silent working memory framework (Barbosa et al. 2020)
- Bump attractor model (Wimmer et al. 2014)
- Synaptic working memory model (Mongillo et al. 2008)

**Brain regions**:
- Medial prefrontal cortex (mPFC)
- Anterior cingulate cortex (ACC)
- Prelimbic cortex (PrL)
- Infralimbic cortex (IL)
- Dorsal peduncular cortex (DP)

**Keywords**: spatial working memory, prefrontal cortex, goal representation, flexible behavior, population decoding, delay period activity, activity-silent working memory, Neuropixels, rodent electrophysiology, behavioral flexibility, task structure encoding, null result working memory

### Related wiki pages
- [[wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory|Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory]]
