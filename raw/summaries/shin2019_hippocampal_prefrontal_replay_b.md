---
source_file: shin2019_hippocampal_prefrontal_replay_b.md
title: Dynamics of Awake Hippocampal-Prefrontal Replay for Spatial Learning and Memory-Guided Decision Making
authors: Justin D. Shin, Wenbo Tang, Shantanu P. Jadhav
year: 2019
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Awake hippocampal reverse and forward replay events predict past and future choices respectively with opposing learning gradients, while coordinated hippocampal-prefrontal replay distinguishes correct paths from alternatives to support spatial working memory.

---

### Background & motivation

Hippocampal place cells replay spatial trajectories during immobility in both forward and reverse order, potentially supporting memory-guided behavior including retrospection, retrieval, prospection, and planning. However, how reverse and forward replay together support learning, retrieval, and memory-guided decision making remains unclear. This study addresses how replay content changes over learning and how coordinated hippocampal-prefrontal activity distinguishes behaviorally relevant replay content.

---

### Methods

- **Task**: W-maze spatial alternation task requiring rats to alternate between side wells and center well to receive reward
  - Outbound trajectories (center-to-side): spatial working memory component requiring recall of previous visit
  - Inbound trajectories (side-to-center): spatial reference memory component requiring return-to-center rule
- **Subjects**: 6 adult male Long-Evans rats
- **Design**: Single-day learning with 8 behavioral sessions (15-20 min each) interleaved with rest sessions; continuous recording from same ensembles throughout
- **Recordings**: Simultaneous electrophysiological recording from dorsal CA1 (n = 216 place cells) and prefrontal cortex (prelimbic and anterior cingulate; n = 154 cells) using tetrodes
- **Analysis approaches**:
  - Bayesian decoding of position from place-cell activity
  - Detection of sharp-wave ripples (SWRs) during immobility
  - Identification of forward and reverse replay events using time-shuffled significance testing
  - Template matching for CA1-PFC reactivation strength analysis
  - Support vector machine (SVM) classifiers for replay prediction of well identity and taken paths

---

### Key findings

- **Reverse vs forward replay dissociation**: During reward-well transitions, reverse replay preferentially reactivated past trajectories while forward replay preferentially reactivated future trajectories (p < 1e-4 for both center and side wells)
- **Learning gradients differ by location**:
  - At side wells (reference memory): Reverse replay showed bias toward taken past paths during early learning that decreased with performance (r = -0.57, p < 0.0001); forward replay showed bias toward taken future paths emerging only during late performance (r = 0.28, p = 0.035)
  - At center well (working memory): Both reverse and forward replay continued to represent both taken and alternative paths without bias throughout learning
- **Replay supports prediction**: Reverse replay predicted taken past paths during early learning; forward replay predicted future taken paths during late performance at side wells
- **Coordinated CA1-PFC reactivation**: CA1-PFC reactivation strength was significantly higher for replay of behaviorally taken paths compared to not-taken paths during correct trials (center well: p = 0.032; side wells: p = 0.0075)
- **PFC readout of replay content**: CA1-PFC reactivation distinguished taken from not-taken paths for both forward replay of future paths and reverse replay of past paths during correct trials (forward: p = 0.0058; reverse: p = 0.039)
- **Performance correlation**: Higher CA1-PFC reactivation correlated with better working memory performance; higher CA1 reactivation alone correlated with lower performance
- **Replay properties over learning**: SWR duration decreased while decoded replay trajectory length increased over learning, suggesting enhanced replay efficiency with experience

---

### Computational framework

The paper employs a reinforcement learning perspective on hippocampal replay function. Reverse replay is conceptualized as supporting retrospective evaluation and temporal credit assignment for paths leading to reward, consistent with model-based reinforcement learning. Forward replay is conceptualized as supporting prospective planning of future trajectories toward goals. The hippocampus is proposed to serve as a cognitive search mechanism that explores possible past and future paths, with the prefrontal cortex providing readout and selection of behaviorally relevant trajectories. This framework aligns with computational models of prioritized memory access (e.g., Mattar & Daw, 2018) and connects to machine learning literature on experience replay for reinforcement learning.

---

### Prevailing model of the system under study

Prior to this study, the field understood that: (1) hippocampal replay occurs during sharp-wave ripples in both sleep and awake states; (2) awake replay is important for spatial memory and decision making; (3) reverse replay is enhanced by reward and may support reinforcement learning; (4) forward replay may support planning of future trajectories; (5) hippocampal-prefrontal coordination occurs during SWRs; and (6) replay represents both random and remote trajectories suggesting a role in free recall. However, how reverse and forward replay together support learning, retrieval, and memory-guided decision making remained unclear, as did how replay content changes over learning and how coordinated hippocampal-prefrontal activity distinguishes behaviorally relevant replay.

---

### What this paper contributes

This study provides the first continuous tracking of awake replay in the same hippocampal-prefrontal ensembles throughout spatial learning, revealing several novel findings:

1. **Differential roles of reverse and forward replay**: Reverse replay supports retrospective evaluation of past paths, while forward replay supports prospective planning of future paths, with these roles manifesting in opposing learning gradients.

2. **Learning-dependent changes in replay content**: At side wells (reference memory), replay shifts from reverse-replay-based prediction of past paths during early learning to forward-replay-based prediction of future paths during late performance. At center wells (working memory), replay continues to represent both taken and alternative paths throughout learning.

3. **Prefrontal readout of hippocampal replay**: Coordinated CA1-PFC replay distinguishes behaviorally taken paths from alternatives, with stronger reactivation for actual taken paths during correct trials. This discrimination is absent during incorrect trials.

4. **Mechanism for memory-guided decision making**: The findings suggest a model where hippocampal replay supports cognitive search over possible paths, while PFC provides selective readout of behaviorally relevant trajectories to guide learning and decision making.

---

### Brain regions & systems

- **Hippocampus (dorsal CA1)**: Primary locus of place-cell replay sequences; exhibits reverse and forward replay of spatial trajectories during SWRs; shows direction-selective place fields starting from first session; replay rate decreases over learning while replay efficiency increases.

- **Prefrontal cortex (PFC, prelimbic and anterior cingulate regions)**: Receives hippocampal replay information; exhibits spatially and directionally selective firing; shows coordinated reactivation with CA1 during replay events; provides readout of behaviorally relevant replay content through differential reactivation strength for taken versus not-taken paths.

- **Hippocampal-prefrontal circuit**: Coordinated replay activity between CA1 and PFC during SWRs; CA1 leads PFC during replay; stronger coherent reactivation for behaviorally taken paths; correlation between CA1-PFC reactivation strength and working memory performance.

---

### Mechanistic insight

This paper provides mechanistic insight into how hippocampal replay supports spatial learning and memory-guided decision making, though it does not fully meet the highest bar for Marr's three levels because it does not provide a formal algorithm implemented in neural hardware. However, it does provide substantial mechanistic insight:

**Computational level**: The paper frames hippocampal replay as supporting a cognitive search process over possible past and future paths, enabling retrospective evaluation and prospective planning. The prefrontal cortex provides readout and selection of behaviorally relevant trajectories. This aligns with reinforcement learning frameworks where replay supports credit assignment (reverse replay) and planning (forward replay).

**Algorithmic level**: The paper identifies key algorithmic components: (1) reverse replay sequences reactivate past trajectories for retrospective evaluation; (2) forward replay sequences preactivate future trajectories for prospective planning; (3) coordinated CA1-PFC reactivation selectively strengthens for behaviorally taken paths, serving as a readout mechanism; (4) learning shifts the relative balance of reverse versus forward replay-based prediction depending on task demands.

**Implementational level**: The neural implementation involves: (1) CA1 place cells with direction-selective firing forming sequence templates; (2) SWR events during immobility providing temporal windows for replay; (3) Temporally compressed sequential reactivation of place cells during SWRs; (4) Synchronous reactivation of PFC cells coordinated with CA1 replay; (5) Strengthened CA1-PFC coupling for behaviorally relevant replay content. The paper does not address specific cell types, synaptic mechanisms, or neuromodulatory influences in detail.

---

### Limitations & open questions

- The study used rapid single-day learning; replay roles may differ in repeatedly trained tasks where habitual systems contribute
- Independent cortical reactivation not ruled out (though CA1-PFC coordination was measured)
- Relationship between theta-mediated and SWR-mediated CA1-PFC interactions not investigated
- Specific synaptic or cellular mechanisms of CA1-PFC coordination not addressed
- Whether findings generalize to non-spatial memories and non-spatial decision making remains to be determined
- The role of other brain regions (e.g., ventral striatum, amygdala) in reading out replay content not investigated

---

### Connections & keywords

- **Key citations**: Jadhav et al., 2012 (causal role of awake replay); Ambrose et al., 2016 (reverse replay and reward); Foster and Wilson, 2006 (reverse replay discovery); Pfeiffer and Foster, 2013 (forward replay for planning); Tang et al., 2017 (CA1-PFC reactivation); Mattar and Daw, 2018 (prioritized memory access); Fernández-Ruiz et al., 2019 (long-duration SWRs and memory)

- **Named models or frameworks**: Reinforcement learning framework for replay function; cognitive search model; model-based planning; temporal credit assignment; prioritized memory access

- **Brain regions**: Hippocampus (dorsal CA1), prefrontal cortex (prelimbic, anterior cingulate), hippocampal-prefrontal circuit

- **Keywords**: awake replay, sharp-wave ripples, place cells, reverse replay, forward replay, spatial learning, working memory, prefrontal cortex, hippocampus, decision making, trajectory reactivation, spatial alternation, memory-guided behavior, neural ensembles, Bayesian decoding, reinforcement learning
