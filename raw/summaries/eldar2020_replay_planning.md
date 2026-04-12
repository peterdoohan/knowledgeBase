---
source_file: "eldar2020_replay_planning.md"
paper_id: "eldar2020_replay_planning"
title: "The roles of online and offline replay in planning"
authors: "Eran Eldar, Ga\u00eblle Li\u00e8vre, Peter Dayan, Raymond J Dolan"
year: 2020
journal: "eLife"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["two_step_task", "navigation_task"]
methods: ["computational_modeling"]
brain_regions: ["hippocampus"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl"]
keywords: ["roles", "online", "offline", "replay", "planning"]
key_citations: ["momennejad2018_offline_replay_planning", "daw2011_model_based_striatal_prediction", "kurth_nelson2016_sequences_non_spatial", "liu2019_human_replay_reorganizes", "stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

Online (on-task) replay of state trajectories, measured via MEG sequenceness, correlates with model-based planning flexibility and is coupled with policy re-evaluation, whereas offline (rest-period) replay correlates with model-free rigidity and reflects the consolidation of habitual policies.

---

### Background & motivation

Both on-task and off-task neural replay are believed to support flexible decision making, but their relative contributions have remained unclear. One perspective holds that both forms of replay support the same goal — building and maintaining a model of the environment — such that they are complementary. A competing perspective proposes a trade-off: online replay mediates on-the-fly model-based planning, while offline replay compiles a more rigid model-free decision policy (akin to Dyna-style planning). Previous studies lacked the ability to relate replay events directly to ongoing planning behaviour or to individual differences in planning strategy. The paper addresses this gap using MEG sequenceness methodology alongside a decision task specifically designed to dissociate model-based and model-free strategies.

---

### Methods

- **Subjects**: 40 healthy human adults (18–33 years; 25 female) recruited at UCL; sample size set to roughly double prior MEG sequenceness studies.
- **Task**: A 2×4 state-space navigation task in which 8 unique images (each with a known reward value) were arranged at fixed locations. Subjects had to learn state transitions by trial and error and collect reward by moving to high-value states in one or two steps.
- **Flexibility manipulations**: (1) reward-contingency changes mid-experiment (new image-reward associations); (2) spatial structure changes (two pairs of images switched locations); (3) interleaved 1-move and 2-move trial blocks requiring moment-to-moment strategy adjustment. An individual **Index of Flexibility (IF)** was derived from the difference in the proportion of move choices optimal for the actual vs. counterfactual trial type.
- **Behavioural modelling**: Model-free (MF), model-based (MB), and MF-MB hybrid reinforcement learning algorithms were fit to each subject's choices using iterative hierarchical expectation-maximisation; model comparison via integrated BIC.
- **MEG acquisition**: Whole-head 275-channel axial gradiometer system at 600 Hz; low-pass filtered at 20 Hz; resampled to 100 Hz.
- **MEG decoding**: SVMs trained on pre-task stimulus exposure data (8-way image classifiers) and image-reward training data (4-way move classifiers); applied to main-task and rest data.
- **Sequenceness analysis**: Cross-correlation of decoded image probability time series (within 400 ms windows, lags up to 200 ms) to detect sequential forward or backward replay; Bayesian hierarchical Gaussian Process models used to assess timepoints where sequenceness correlated with IF and outcome surprise.
- **Off-task replay**: Sequenceness computed in 2-minute rest MEG epochs preceding each experimental block, for the 5 most and 5 least frequently chosen transitions.

---

### Key findings

- Subjects showed substantial individual differences in decision flexibility; IF correlated with coping with reward-contingency changes, spatial changes, and with accurate post-task map sketching.
- An MF-MB hybrid algorithm outperformed either algorithm alone (iBIC: hybrid = 39908 vs. MF = 40821 vs. MB = 43249); 84% of variance in IF was explained by three parameters controlling the MF-MB balance.
- **On-task replay**: Significant forward sequenceness encoding the just-traversed state transition was found 50–330 ms and 820–950 ms post-outcome, plus encoding of the penultimate transition at the end of 2-move trials. Sequenceness was positively correlated with IF (mean β = 0.17, 95% CI = 0.13–0.20) and with outcome surprise (β = 0.06), with a significant interaction (β = 0.19).
- On-task forward sequenceness predicted subsequent **policy change** (moves preceded by high sequenceness were less likely to be re-chosen; this re-evaluation increased reward by +11.1%, SEM 1.5%, p = 0.001).
- **Off-task replay**: Significant forward sequenceness was found during rest for frequently chosen transitions (p = 0.01) but not for rarely chosen ones (p = 0.47); off-task sequenceness correlated **negatively** with IF (i.e., more rest-replay in less flexible, more model-free subjects).
- Off-task replay during the critical rest period following reward-contingency change included replay of **subsequently chosen** (newly planned) transitions, indicating a model-based offline re-planning component, but this did not correlate with IF.
- Advance planning was evident in MEG: chosen second moves were decodeable during first-move choices and prior to first-outcome onset; early decodability correlated with IF (β = 0.29, 95% CI = 0.24–0.34).

---

### Computational framework

The paper uses **model-based vs. model-free reinforcement learning** as its primary framework, supplemented by a **Dyna-style** (Sutton 1991) interpretation of offline replay.

- **Model-free (MF) algorithm**: Learns cached action values Q(state, move) updated by reward prediction errors; separate Q tables for 1-move and 2-move policies.
- **Model-based (MB) algorithm**: Learns a transition matrix T(s, move, s') updated by transition prediction errors; uses this model at decision time to compute expected values by forward simulation.
- **Hybrid MF-MB**: Combines both sets of Q-values via weighted sum (β parameters); individual flexibility is primarily a function of the relative weights.
- **Sequenceness as proxy for replay**: Detects temporally ordered reactivation of state representations in MEG, interpreted as the neural substrate of trajectory replay that underpins both forms of planning.
- The normative framework of Mattar & Daw (2018) — replay should be prioritised where policy improvement is highest — is used as a reference point for interpreting when forward vs. backward replay occurs.

---

### Prevailing model of the system under study

The introduction presents two competing views: (1) both online and offline replay contribute to the same purpose — building and using a flexible cognitive model of the environment — with online replay enabling on-the-fly model-based evaluation and offline replay consolidating a map of state transitions; (2) online and offline replay support **distinct** planning strategies in a trade-off: online replay enables flexible model-based planning, while offline replay builds a rigid, pre-computed model-free policy (Dyna). The paper characterises the field as having strong theoretical frameworks but insufficient human data linking replay directly to planning flexibility or to the MF-MB distinction. Prior MEG work had detected human sequenceness but had difficulty connecting it to ongoing behaviour.

---

### What this paper contributes

The results support the **trade-off hypothesis**: online replay is the neural signature of active, flexible, model-based planning (it follows surprising outcomes, encodes recently traversed paths, and predicts policy revisions), while offline replay reflects the consolidation of habitual, model-free policies (it encodes frequently repeated paths during rest and correlates with inflexibility). This dissociation had been theorised but not demonstrated in humans. The paper also shows that offline replay can contain forward-looking (yet-to-be-chosen) content during a specific re-planning rest period, indicating that offline replay is not purely retrospective but can also serve model-based re-planning — though this capacity does not appear to confer trial-to-trial flexibility. The task design is a further contribution: it provides converging behavioural measures of the MF-MB balance and efficiently incentivises model-based planning (93% vs. 80% potential reward).

---

### Brain regions & systems

The paper is MEG-based and does not resolve specific anatomical sources. No region-level localisation is reported. The analysis is at the level of whole-brain decoded representational dynamics.

- **Hippocampus / medial temporal system** — implicitly invoked as the presumed locus of replay, consistent with the rodent literature on sharp-wave ripple replay, but not directly measured or localised in this study.
- The paper operates at the **algorithmic level** of the MF-MB distinction without mapping specific computations to specific brain regions.

---

### Mechanistic insight

The paper does not fully meet the bar. It provides an algorithm (sequenceness as operationalisation of trajectory replay underpinning MB or MF planning) and MEG data linking replay to behaviour, but it does not provide neural data that isolate a specific algorithmic mechanism over alternatives at the neural level.

Specifically: the sequenceness measure detects that state representations are reactivated in sequence, which is consistent with a replay mechanism, but the measure cannot distinguish between different possible neural implementations (e.g., sharp-wave ripple-driven vs. theta-sequence-driven replay, or representational drift vs. active reactivation). The paper also relies on correlational evidence — sequenceness predicts policy changes, but causality is not established. No recordings from identified cell types, no oscillatory decomposition, and no manipulation of replay is performed.

---

### Limitations & open questions

- The IF measure probes one specific form of flexibility (1-move vs. 2-move trial adjustment); the task is less suited to testing other forms of flexibility (e.g., retrospective revaluation as in Momennejad et al.).
- The sequenceness metric compares forward to backward sequences as a relative measure, making it difficult to independently quantify each direction; large autocorrelation in neural decoding complicates this.
- The experiment was not designed to induce compound state representations linking states to their successors, leaving open how such representations interact with replay.
- Causal role of online vs. offline replay not established — experiments disrupting replay (e.g., targeted memory reactivation, TMS, sleep manipulation) are needed.
- The lack of correlation between IF and prospective offline replay raises the question of whether offline planning is inherently unsuited to trial-to-trial flexibility, or whether the task simply did not allow sufficient time.
- Potential confound: individual differences in replay could reflect differences in memory encoding strength rather than in planning strategy per se.

---

### Connections & keywords

**Key citations**:
- Mattar & Daw (2018) — normative theory of when replay should occur
- Sutton (1991) — Dyna framework for offline model-free replay
- Gershman et al. (2014); Momennejad et al. (2018) — offline replay and retrospective revaluation
- Daw et al. (2011) — two-step task for MF-MB distinction
- Kurth-Nelson et al. (2016); Eldar et al. (2018); Liu et al. (2019) — MEG sequenceness methodology
- Pfeiffer & Foster (2013) — rodent preplay before choice
- Stachenfeld et al. (2017) — hippocampus as predictive map

**Named models or frameworks**:
- Model-free (MF) reinforcement learning
- Model-based (MB) reinforcement learning
- MF-MB hybrid algorithm
- Dyna (Sutton 1991)
- Sequenceness analysis (Kurth-Nelson et al. 2016)
- Bayesian hierarchical Gaussian Process time series analysis
- Index of Flexibility (IF)

**Brain regions**:
- Whole-brain MEG (no anatomical localisation); hippocampus implicitly invoked as replay substrate

**Keywords**:
- hippocampal replay, MEG sequenceness, model-based planning, model-free planning, decision flexibility, offline replay, online replay, individual differences, reinforcement learning, state-space navigation, prediction error, policy update
