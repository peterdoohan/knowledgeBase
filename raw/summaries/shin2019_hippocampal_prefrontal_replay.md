---
source_file: "shin2019_hippocampal_prefrontal_replay.md"
paper_id: "shin2019_hippocampal_prefrontal_replay"
title: "Dynamics of Awake Hippocampal-Prefrontal Replay for Spatial Learning and Memory-Guided Decision Making"
authors: "Justin D. Shin, Wenbo Tang, Shantanu P. Jadhav"
year: 2019
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["rat"]
methods: ["bayesian_decoding"]
brain_regions: ["hippocampus", "hippocampus_ca1", "prefrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl"]
keywords: ["dynamics", "awake", "hippocampal", "prefrontal", "replay", "spatial", "learning", "memory", "guided", "decision"]
key_citations: ["ambrose2016_reverse_replay_hippocampal"]
---

### One-line summary

Awake hippocampal reverse replay supports retrospective evaluation of past paths while forward replay supports prospective planning of future paths, with coordinated hippocampal-prefrontal replay distinguishing behaviorally relevant trajectories during spatial learning.

---

### Background & motivation

Hippocampal place cells replay spatial trajectories during sharp-wave ripples (SWRs) in both forward and reverse order during awake immobility, offering a potential mechanism for learning and memory-guided decision making. While previous studies established that awake replay is important for spatial memory, how reverse and forward replay together support learning, retrieval, and decision making remained unclear. Additionally, whether replay content changes over the course of learning and how hippocampal-prefrontal interactions contribute to replay-dependent behaviors were open questions.

---

### Methods

- **Task**: Rats (n=6) learned a novel W-maze spatial alternation task within a single day (8 behavioral sessions, 15-20 min each, interleaved with rest sessions)
- **Task structure**: Continuous alternation between reward wells on three maze arms requiring (1) return-to-center from side wells (inbound, reference memory), and (2) alternate side choice from center well based on previous visit (outbound, working memory)
- **Recordings**: Continuous simultaneous electrophysiological monitoring of stable ensembles in dorsal CA1 (n=216 place cells) and PFC (prelimbic and anterior cingulate; n=154 cells) across all 8 sessions (5.5-6.5 hours)
- **Replay detection**: Bayesian decoding of spatial position during SWRs; candidate events with ≥5 active place cells; significance assessed via time-shuffled comparison (p < 0.05); forward vs. reverse determined by slope of linear fit
- **CA1-PFC reactivation**: Template matching method measuring correlation between CA1-PFC population synchronization matrices during running vs. SWR periods

---

### Key findings

- **Reverse vs. forward replay bias**: At center wells, reverse replay preferentially reactivated inbound (past) trajectories (324/91 reverse/forward events, p < 1e-4), while forward replay preferentially reactivated outbound (future) trajectories (116/202 reverse/forward events, p < 1e-4); pattern reversed at side wells
- **Learning gradients at side wells**: Reverse replay bias for past taken paths decreased over learning (r = -0.57, p < 0.0001), while forward replay bias for future taken paths emerged over learning (r = 0.28, p = 0.035); SVM prediction accuracy for past paths using reverse replay was significant only in early/middle sessions, while prediction of future paths using forward replay was significant only in late sessions
- **Center well cognitive search**: At center well (working memory component), hippocampus replayed both taken and not-taken past and future paths throughout learning without bias, suggesting a cognitive search/evaluation process
- **Coherent CA1-PFC replay**: Reactivation strength was significantly higher when CA1 replayed behaviorally taken paths vs. not-taken paths (p = 0.032 at center wells, p = 0.0075 at side wells for correct trials); this discrimination was absent during incorrect trials
- **Replay dynamics over learning**: Replay rate decreased over learning (p = 0.0005), SWR duration decreased (p < 1e-4), while decoded replay trajectory length increased (p = 0.0004), suggesting enhanced replay efficiency

---

### Computational framework

The paper frames hippocampal replay within a reinforcement learning and planning framework. Reverse replay is proposed to support retrospective evaluation and temporal credit assignment (consistent with model-based reinforcement learning), while forward replay supports prospective planning of future trajectories. The hippocampal-prefrontal interaction is conceptualized as a readout mechanism where PFC distinguishes behaviorally relevant replayed paths through differential reactivation strength. This connects to Marr's three levels:
- **Computational**: The brain must solve spatial credit assignment and trajectory planning problems for goal-directed behavior
- **Algorithmic**: Reverse and forward replay implement retrospective evaluation and prospective search, respectively; CA1-PFC coordination tags behaviorally relevant experiences
- **Implementational**: Sharp-wave ripples in CA1 coordinate with PFC reactivation during awake immobility at decision points

---

### Prevailing model of the system under study

Prior to this study, the field understood that: (1) hippocampal place cells fire sequentially during SWRs, replaying trajectories in both forward and reverse order; (2) awake replay is associated with memory-guided behavior and is enhanced by reward and novelty; (3) reverse replay on linear tracks is specifically enhanced by changing reward; (4) causal manipulation studies showed awake replay is necessary for spatial working memory tasks; (5) hippocampal-prefrontal activity is coordinated during SWRs. However, how reverse and forward replay together support learning and decision making, and whether replay content changes over learning, remained unclear. The role of PFC in discriminating hippocampal replay content for behavior was not known.

---

### What this paper contributes

This paper establishes that:
1. **Reverse and forward replay have distinct functional roles**: Reverse replay supports retrospective evaluation of past paths, while forward replay supports prospective planning of future paths
2. **Opposing learning gradients**: At side wells (reference memory), reverse replay bias for past paths decreases with learning while forward replay bias for future paths emerges with learning, suggesting a shift from retrospective evaluation to prospective planning
3. **Hippocampal cognitive search**: At center wells (working memory), hippocampus replays both taken and not-taken paths throughout learning, supporting a cognitive search process for evaluating options
4. **PFC readout of hippocampal replay**: Coherent CA1-PFC replay distinguishes behaviorally taken paths from alternatives through stronger reactivation, providing a mechanism for memory-guided decision making

---

### Brain regions & systems

- **Hippocampus (dorsal CA1)**: Contains place cells with spatial and direction-selective firing; source of reverse and forward replay events during SWRs; replays both taken and not-taken paths during decision points
- **Prefrontal cortex (PFC, prelimbic and anterior cingulate)**: Exhibits spatially and directionally selective firing with multi-peaked fields; shows coherent reactivation with CA1 during replay; discriminates behaviorally relevant paths through differential reactivation strength
- **Hippocampal-prefrontal circuit**: Coordinated activity during SWRs; CA1-leading-PFC directionality during replay; supports memory-guided spatial decision making

---

### Mechanistic insight

This paper provides strong mechanistic insight by combining neural recordings with behavioral predictions. The key mechanistic contribution is demonstrating that:

1. **Algorithmic distinction between replay types**: Reverse and forward replay serve distinct computational functions—retrospective evaluation vs. prospective planning—demonstrated by their differential prediction of past and future choices, respectively

2. **Neural data supporting the algorithm**: The finding that reverse replay predicts past choices while forward replay predicts future choices is grounded in simultaneously recorded hippocampal and prefrontal ensemble activity

3. **Multi-region coordination for behavior**: Coherent CA1-PFC replay, measured through template matching of population synchronization, distinguishes behaviorally taken from not-taken paths, providing a readout mechanism for hippocampal replay content

**Marr's levels analysis**:
- **Computational**: The brain solves credit assignment and planning problems for goal-directed navigation, requiring evaluation of past actions and simulation of future trajectories
- **Algorithmic**: Reverse replay implements retrospective evaluation (temporal credit assignment), while forward replay implements prospective planning; CA1-PFC coordination tags behaviorally relevant experiences for decision making
- **Implementational**: SWR events in CA1 coordinate sequential reactivation of place cells and synchronous reactivation of PFC neurons; replay speed increases with learning (longer trajectories in shorter SWRs); PFC shows many-to-one mapping with CA1 place fields

---

### Limitations & open questions

- Rapid single-day learning paradigm may not generalize to repeatedly trained tasks where habitual systems contribute
- Independent cortical reactivation outside of hippocampal coordination cannot be ruled out
- The relationship between theta-mediated and SWR-mediated CA1-PFC interactions remains to be investigated
- Whether replay findings in rodents generalize to primates and humans requires further investigation
- The specific cellular and circuit mechanisms underlying the differential CA1-PFC reactivation for taken vs. not-taken paths remain unknown

---

### Connections & keywords

**Key citations**: Foster and Wilson 2006 (reverse replay discovery), Diba and Buzsáki 2007 (forward/reverse replay), Jadhav et al. 2012 (causal role of replay in W-maze), Ambrose et al. 2016 (reward modulation of reverse replay), Tang et al. 2017 (CA1-PFC reactivation during sleep and wake), Pfeiffer and Foster 2013 (forward replay of future paths), Karlsson and Frank 2009 (awake replay of remote experiences), Carr et al. 2011 (review of awake replay functions)

**Named models or frameworks**: Sharp-wave ripple (SWR), place cells, reverse replay, forward replay, template matching reactivation, Bayesian decoding, reinforcement learning, model-based planning, cognitive search, credit assignment

**Brain regions**: Hippocampus (dorsal CA1), prefrontal cortex (PFC, prelimbic, anterior cingulate), hippocampal-prefrontal circuit

**Keywords**: hippocampal replay, sharp-wave ripples, prefrontal cortex, spatial learning, spatial working memory, reverse replay, forward replay, place cells, awake replay, memory-guided decision making, trajectory reactivation, W-maze alternation task, reinforcement learning, cognitive search, credit assignment
