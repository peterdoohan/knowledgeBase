---
source_file: mugan_redish2024_environmental_complexity_decision.md
title: Environmental complexity modulates information processing and the balance between decision-making systems
authors: Ugurcan Mugan, Samantha L. Hoffman, A. David Redish
year: 2024
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Environmental spatial complexity modulates the balance between hippocampal deliberative and dorsolateral striatal procedural decision-making, with dorsomedial prefrontal cortex acting as the arbitrating structure that sets strategy and predicts hippocampal nonlocal coding.

---

### Background & motivation

Adaptive behavior in naturalistic settings depends on the interplay between at least two competing decision systems: a deliberative (model-based/prospective) system supported by hippocampus and a procedural (habit/cached) system supported by dorsolateral striatum. Most prior work has studied these systems in simple, uniform environments (e.g., T-mazes), leaving open how environmental topological complexity changes the relative engagement of each system and the neural representations that guide action selection. This paper addresses that gap by systematically varying maze complexity while simultaneously recording from hippocampus (HC), dorsolateral striatum (DLS), and dorsomedial prefrontal cortex (dmPFC).

---

### Methods

- **Task**: Left/right/alternation (LRA) foraging task in which rats navigated a maze with a configurable central path (27 unique maze configurations differing in internal wall placement, yielding low-, mid-, and high-complexity environments quantified via graph-theoretic information content). Two uncued rule switches per session changed which return arm was rewarded.
- **Subjects**: Fisher-Brown Norway F1 hybrid and Brown Norway inbred rats; recording cohort: nHC = 7, nDLS = 4, nmPFC = 7; DREADD cohort: nDREADDs = 8, nControl = 8.
- **Recordings**: Simultaneous silicon probe recordings from dorsal HC CA1, DLS, and dmPFC in freely behaving rats.
- **Key measurements**: Vicarious trial and error (VTE, quantified as zIdPhi), path stereotypy, proportion of exploratory laps, hippocampal theta sequence scores (Bayesian decoding within theta cycles), task-bracketing index in DLS, ensemble population correlation matrices, ensemble change-point analysis across brain regions, dmPFC prediction of HC theta-sequence state (5-fold cross-validated Bayesian decoding).
- **Causal manipulation**: Chemogenetic inactivation of dmPFC (CaMKIIa-hM4Di DREADDs + DCZ) with within- and across-subject controls; repeated sessions to assess short-term rebound and long-term learning effects.
- **Complexity quantification**: Graph entropy of topologically discretized maze space (information content across equivalent spanning trees).

---

### Key findings

- Rats made more errors in more complex environments (mixed-effects ANOVA F(18) = 2.35, p = 0.003); path stereotypy in the central segment developed more slowly and to a lower asymptote as complexity increased.
- Proportion of exploratory laps increased with complexity (F(18) = 2.61, p = 0.001), providing a complexity-sensitive behavioral correlate of deliberation.
- HC theta sequence scores (ordered nonlocal sequential activity during theta cycles) increased significantly with environmental complexity (Kruskal-Wallis H(2) = 765.94, p < 0.001); nonlocal decoding in the second half of each theta cycle was specifically enhanced in complex environments.
- Theta sequence scores correlated positively with VTE (t(80) = -6.8, p < 0.001) and exploration and inversely with path stereotypy (t(84) = 5.79, p < 0.001), supporting a direct link between HC nonlocal activity and deliberative behavior.
- DLS task-bracketing index (start/end boundary bursting) decreased with complexity (F(8) = 2.31, p = 0.037) and never fully developed in high-complexity environments; DLS spatial representations shifted from globally similar throughout the central path (simple) to locally distinct (complex).
- HC theta sequence score and DLS task bracketing were inversely correlated across time around rule switches, most clearly in simple environments.
- dmPFC ensemble representations changed before either HC or DLS after rule switches (mean lead over HC: 1.4 laps, p = 0.017; over DLS: 9.3 laps, p < 0.001). dmPFC activity predicted HC theta sequence scores at lap-timescale but not theta-cycle-by-cycle timescales, with stronger prediction after rule switches.
- dmPFC inactivation impaired behavioral adaptation to rule switches (slower change-point; F(3) = 3.51, p = 0.015) and reduced path stereotypy but, paradoxically, did not acutely reduce VTE or exploration.
- On the day after dmPFC inactivation, compensatory rebounds in VTE and exploration were observed (exploration rebound: z = 3.63, p < 0.001), and long-term progression of task performance was impaired throughout the multi-week experiment.

---

### Computational framework

The paper is grounded in a **multi-system / competing decision-systems** framework, combining elements of model-based (deliberative) and model-free (procedural/habit) reinforcement learning with spatial cognition via cognitive-map theory. No formal mathematical model is derived; rather, the framework organizes predictions about how two systems — one encoding a flexible state-space model of the environment (HC) and one encoding cached action sequences (DLS) — should interact as a function of environmental demands.

Key variables: HC theta sequence score (proxy for prospective/deliberative processing intensity), DLS task-bracketing index (proxy for habitual action chunking), and dmPFC ensemble state (proxy for strategic context and arbitration signal). The framework assumes that more complex environments increase the state-space dimensionality, thereby increasing the cost-benefit advantage of deliberation and reducing the utility of cached habits.

---

### Prevailing model of the system under study

The paper's introduction presents a well-established dual-systems view: HC provides a flexible cognitive map enabling deliberative/prospective decision-making, while DLS encodes stereotyped, stimulus-response action chains supporting procedural behavior. Medial PFC is hypothesized to encode task strategy and arbitrate between the two systems. Prior empirical support for this division was derived almost entirely from simple, low-dimensional environments (T-mazes, linear tracks). The implicit assumption entering this study is that the relative engagement and neural signatures of each system are stable properties of the circuits, independent of the structural complexity of the environment being navigated.

---

### What this paper contributes

This paper demonstrates that the balance and neural signatures of competing decision systems are dynamically shaped by environmental topology, not solely by learning history or reward contingency. Specifically:

- HC nonlocal coding is not a fixed property of deliberation but scales with the dimensionality of the navigational problem — more complex environments generate more prominent theta sequences.
- The classical DLS task-bracketing signature, widely taken as a hallmark of habit formation, fails to emerge in complex environments. This means prior characterizations of DLS in procedural control may be specific to artificially simple task geometries.
- dmPFC does not merely respond to rule switches but leads HC and DLS representational changes, predicting HC state at a behaviorally relevant (lap) timescale and causally supporting the use of deliberative information (not the deliberation itself). The novel dissociation is that dmPFC inactivation leaves VTE and exploration intact but impairs the rat's ability to leverage them for rapid rule adaptation, suggesting dmPFC's role is in integrating deliberative outputs into updated task context rather than initiating the deliberative episode.

---

### Brain regions & systems

- **Hippocampus (HC) / dorsal CA1** — encodes flexible state-space representations; locus of theta sequences whose score increases with environmental complexity; tracks deliberative behavioral correlates (VTE, exploration).
- **Dorsolateral striatum (DLS)** — encodes cached action sequences; shows task-bracketing boundary bursts in simple but not complex environments; spatial representations become locally distinct rather than globally uniform as complexity increases.
- **Dorsomedial prefrontal cortex (dmPFC)** — proposed strategy-setting and arbitration structure; ensemble representations change before HC and DLS after rule switches; activity predicts HC theta-sequence state at lap timescale; causal inactivation impairs long-term strategy learning and rule-switch adaptation without acutely reducing deliberative behaviors.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the algorithmic and partial implementational levels.

**Phenomenon**: Animals must dynamically shift between deliberative and procedural control depending on both the consistency of environmental reward contingencies and the structural complexity of the environment.

**Computational**: The brain is solving a problem of adaptive policy selection — choosing when to invest computational resources in model-based forward simulation vs. executing cached action sequences. Environmental complexity increases the information gain from deliberation, tipping the cost-benefit calculation toward the deliberative system.

**Algorithmic**: HC theta sequences implement time-compressed forward sweeps of the state space during deliberation; their score (sequential coherence) reflects the fidelity of prospective coding. DLS encodes action-chunk boundaries (task bracketing) when the state space is sufficiently low-dimensional for cached representations to be useful. dmPFC reads out or predicts the current HC representational state at a lap timescale, preceding transitions in both HC and DLS, and its activity conveys prediction-error-like signals after errors at feeders before modulating central-path activity — consistent with an error-gated strategy-update algorithm.

**Implementational**: The paper provides partial implementational evidence: simultaneous ensemble recordings from specific cell types (putative pyramidal cells in CA1, medium spiny neurons in DLS, and mPFC neurons) with pharmacological/chemogenetic manipulation of dmPFC. However, the precise synaptic mechanisms by which dmPFC communicates with HC and DLS are not directly measured. The lead-time of dmPFC representational change (up to 9.3 laps ahead of DLS) is a strong implementational constraint.

**Bonus**: The use of CaMKIIa-targeted DREADDs specifically implicates excitatory (glutamatergic) projection neurons in dmPFC in the arbitration function, providing a cell-type-level constraint.

---

### Limitations & open questions

- DLS recordings were available in only 4 animals (vs. 7 for HC and mPFC), limiting power for HC-DLS comparisons.
- The causal role of dmPFC was assessed only at a coarse population level (chemogenetic suppression); it remains unclear whether the predictive relationship between dmPFC activity and HC theta sequences reflects a direct projection or is mediated by intervening structures (e.g., thalamus, entorhinal cortex).
- The DREADD inactivation paradoxically spared acute deliberative behavior (VTE, exploration) while impairing adaptation; the mechanism — whether impaired encoding, retrieval, or integration of information gained during deliberation — is unresolved.
- The task-bracketing measure may not capture how DLS encodes action boundaries in complex environments; no alternative DLS metric is proposed to replace it in that regime.
- All recordings used rats in a single-session, relatively familiar task; how quickly these complexity-dependent signatures emerge during initial learning is not addressed.
- The relationship between VTE and exploration as distinct deliberative behaviors (dmPFC predicts exploration but not VTE at the choice point) is highlighted but not mechanistically explained.

---

### Connections & keywords

**Key citations**:
- Johnson & Redish (2007) — HC forward sweeps at decision points
- Jog et al. (1999) — task bracketing and habit formation in DLS
- Barnes et al. (2005) — DLS dynamic encoding of procedural memories
- Powell & Redish (2016) — dmPFC representational changes precede behavioral strategy shifts
- Hasz & Redish (2020) — dmPFC and HC during deliberation
- Gupta et al. (2012) — HC theta sequences segment spatial experience
- Redish (2016) — VTE review
- Daw, Niv & Dayan (2005) — uncertainty-based competition between prefrontal and striatal systems
- Mugan & MacIver (2020) — spatial planning benefits in complex naturalistic environments

**Named models or frameworks**:
- Left/right/alternation (LRA) task
- Dual (deliberative vs. procedural) decision systems framework
- Cognitive map theory (O'Keefe & Nadel)
- Task-bracketing index
- Theta sequence score (Bayesian decoding within theta cycles)
- VTE / zIdPhi measure of deliberation
- Graph-theoretic environmental complexity (information content)

**Brain regions**:
- Hippocampus (HC), dorsal CA1
- Dorsolateral striatum (DLS)
- Dorsomedial prefrontal cortex (dmPFC)

**Keywords**:
- deliberative vs. procedural decision-making
- environmental complexity
- hippocampal theta sequences
- place cells
- DLS task bracketing
- vicarious trial and error (VTE)
- medial prefrontal cortex arbitration
- multi-system competition
- cognitive map
- DREADDs chemogenetic inactivation
- silicon probe ensemble recording
- decision system balance
