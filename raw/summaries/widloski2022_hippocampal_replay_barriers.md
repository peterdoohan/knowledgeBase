---
source_file: widloski2022_hippocampal_replay_barriers.md
title: Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping
authors: John Widloski, David J. Foster
year: 2022
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal replay sequences rapidly adapt to navigate around novel barrier configurations while place fields remain largely stable, dissociating flexible path planning from rigid spatial representations.

---

### Background & motivation

The hippocampus is essential for flexible navigation and spatial memory, yet how it adapts to environmental changes like blocked paths remains unclear. Place cells, which encode spatial location, typically show stable firing fields anchored to sensory cues, even when barriers are introduced. However, the hippocampus is also critical for replanning tasks requiring construction of novel routes around obstacles. This raises a fundamental question: if place fields remain stable, what neural mechanism supports flexible adaptation to changing spatial contingencies? Replay—rapid sequenced reactivations of place cells during awake immobility—has been linked to planning and memory consolidation. This study tests whether replay can adapt to barrier configurations independently of place field remapping.

---

### Methods

- **Subjects**: 4 Long-Evans rats (3-4 months old)
- **Surgery**: Bilateral implantation of 64-tetrode hyperdrives targeting dorsal CA1; wireless recording system to allow unrestricted movement around barriers
- **Task**: Goal-directed navigation in a square arena (90 x 90 cm) with 9 reward wells arranged in a 3x3 grid
  - **Home trials**: Navigate to a fixed, unmarked goal location (changes each session)
  - **Random trials**: Navigate to a cued, randomly selected well (LED indicator)
  - **Barrier manipulation**: 6 transparent "jail-bar" barriers placed in novel configurations each session (924 possible configurations); rats experienced 47 sessions total with up to 3 sessions per day
- **Recordings**: Mean of 156 simultaneously recorded CA1 place cells per session (up to 295 cells; rats 1-3 had >100 cells and were used for replay analysis)
- **Analysis**:
  - **Place cell identification**: Cells with firing rate >0.01 Hz and spatial information >0.5 bits/sec
  - **Bayesian decoding**: Memory-less position decoding from population activity (20-80 ms windows)
  - **Replay detection**: "Bottom-up" approach identifying smooth posterior trajectories during immobility (speed <5 cm/s) with spatial coverage >12 cm
  - **Barrier conformity scoring**: Quantified how replay vectors aligned parallel to nearby barriers vs. perpendicular to them
  - **Time-lag maps**: Cross-correlogram analysis of position representation during all candidate events (not just replays)
  - **Stability analysis**: Rate map and population vector correlations across sessions; cells designated stable if correlation exceeded 95th percentile of shuffle distribution

---

### Key findings

- **Goal-directed behavior**: Rats rapidly learned to navigate to the Home well, showing significantly higher visit probability and anticipatory licking during Home trials compared to Random trials (p < 0.001), demonstrating trial-selective spatial memory

- **Replay predicts behavior**: Away-event replays (during Random well consumption) were more likely to terminate at the Home well than other wells (p < 0.001). Probability of visiting the Home well was higher following Home-terminating replays (p < 0.001). Replay showed closer alignment to future trajectory than past trajectory (p < 0.001)

- **Rapid replay adaptation to barriers**: Replays consistently depicted trajectories that respected barrier configurations. For 87% of sessions (27/31), barrier conformity scores exceeded the 95th percentile of shuffle distribution (binomial test, p < 0.001). Barrier conformity developed rapidly within sessions and persisted up to 18 cm from barriers

- **Place field stability**: Despite 90+ different barrier configurations, place fields remained largely stable: 58% of cell rate map comparisons were stable across sessions (p < 0.001), and 87% of population vector comparisons were stable (p < 0.001). Stability was spatially distributed throughout the environment

- **Coexistence of two maps**: 
  - A **rigid map**: Majority of stable cells with spatially invariant firing, rapidly instantiated
  - A **flexible barrier-specific map**: Minority of unstable cells that encoded local barrier configurations, with fields that stabilized slowly within sessions and showed reinstatement when local environments were restored

- **Time-lag analysis confirms barrier avoidance**: Analysis of all candidate events (not just replays) showed barrier impermeability in time-lag maps, with greater time lags between positions straddling barriers. Multi-dimensional scaling revealed spatial deformations around barriers, indicating relative inaccessibility of states on opposite sides

- **Mechanistic insight**: Simulation using a continuous attractor network with mixed synaptic weights (reflecting both previous and current barrier configurations) reproduced the observed mix of barrier-conforming and barrier-crossing replays, suggesting that remnants of past experience encoded in connections between stable cells might act as "bridges" for replay

---

### Computational framework

The paper employs a **graph-based cognitive map framework** combined with **continuous attractor network dynamics**. The hippocampus is conceptualized as encoding a "cognitive graph" (Muller et al., 1996; Burgess and O'Keefe, 1996) where nodes represent spatial locations and edges represent traversable paths between them. The core formalism includes:

1. **Bayesian decoding framework**: Position is decoded from population activity using Poisson likelihood assumptions and uniform spatial priors. The posterior probability P(x|k) represents the decoded position given spike counts k across neurons.

2. **Barrier potential gradient**: A spatial function Vb(x) encoding barrier locations, used to compute barrier conformity scores by measuring alignment between replay vectors and the barrier gradient.

3. **Continuous attractor network model**: A bump attractor network with spike-frequency adaptation where recurrent weights Wij are modulated by barrier-induced shortest-path distances. The model mixes weights from previous and current barrier configurations (parameterized by λ) to simulate replay dynamics.

4. **Multi-dimensional scaling**: Applied to time-lag matrices to transform temporal relationships between spatial representations into geometric deformations, revealing how barriers "warp" the representational space.

The framework assumes that replay reflects traversal of a learned graph structure, where the graph connectivity (edge weights) can be rapidly updated to reflect new barrier configurations while node representations (place fields) remain stable.

---

### Prevailing model of the system under study

Prior to this study, the prevailing understanding of hippocampal function included several key assumptions:

1. **Place cells as readouts of hippocampal memory**: The propensity of place cells to remap between environments and their sensitivity to context, events, and motivation led to speculation that place cells are the readouts of memories stored in the hippocampus (Moser et al., 2015).

2. **Remapping enables contextual coding**: The hippocampus was thought to form distinct representations across contexts through remapping, enabling the formation of new cognitive maps adapted to context-specific needs (Smith and Mizumori, 2006; Stachenfeld et al., 2017).

3. **Place field stability during barrier manipulation**: Several studies had shown that place cells remain largely stable when barriers are introduced in familiar environments, even when large behavioral policy changes are required (Muller and Kubie, 1987; Rivard et al., 2004; Alvernhe et al., 2008, 2011; Duvelle et al., 2021).

4. **Hippocampal dependence on replanning tasks**: Despite place field stability, the hippocampus was known to be essential for spatial replanning tasks requiring construction of novel routes around barriers (Thompson et al., 1984; Winocur et al., 2010; Maguire et al., 2006; Rosenbaum et al., 2015).

5. **Replay as a mechanism for planning and memory**: Replay was increasingly seen as a generative process reflecting learned relationships between task states, suited to subserve behavioral flexibility (Gupta et al., 2010; Foster, 2017).

This created a puzzle: if place fields remained stable during barrier manipulations, yet the hippocampus was required for flexible navigation, what neural mechanism bridged this gap? The prevailing model lacked a clear account of how flexible behavior was supported without place field remapping.

---

### What this paper contributes

This paper provides a mechanistic resolution to the puzzle of how the hippocampus supports flexible navigation without global place field remapping. The key contributions are:

1. **Dissociation between place field stability and replay flexibility**: The paper demonstrates that hippocampal replay sequences rapidly adapt to new barrier configurations while place fields remain largely stable. This dissociates the neural representation of space (stable place fields) from the neural mechanism for flexible path planning (adaptive replay).

2. **Rapid replay adaptation**: Replays exhibited barrier conformity within sessions, with 87% of sessions showing significant barrier avoidance. This adaptation occurred even after 90+ different barrier configurations, demonstrating remarkable plasticity in replay generation.

3. **Evidence for two coexisting hippocampal maps**: The paper identifies two distinct neural populations:
   - A **stable majority** (58% of cells, 87% of spatial bins) with rigid place fields that persist across barrier changes
   - A **flexible minority** of unstable cells that encode local barrier configurations and show reinstatement when barriers return to previous positions

4. **Replay as the substrate for flexible memory**: By showing that replays are goal-directed, predictive of future behavior, and rapidly adaptable to new contingencies, the paper establishes replay (and potentially other sequenced reactivations like theta sequences) as the principal hippocampal mechanism for reading out flexible memories.

5. **Mechanistic model**: The paper provides a computational framework using continuous attractor networks with mixed synaptic weights to explain how replay can navigate around barriers while occasionally leaking through them, suggesting that remnants of past experience in synaptic connections act as "bridges" between states.

6. **Generalization to broader memory principles**: The results suggest a novel mechanism for memory flexibility: a stable "cognitive graph" of locations combined with rapidly adaptable trajectory generation through that graph, potentially explaining how the hippocampus supports both generalization across experiences and flexible behavior.

---

### Brain regions & systems

- **Hippocampus CA1 (dorsal)**: Primary recording site. The paper focuses on CA1 place cells and their participation in replay sequences. CA1 is the proposed locus where stable place field representations coexist with flexible replay generation.

- **Hippocampus CA3**: Mentioned as a potential source of replay generation given its role in sharp-wave ripple production, though not directly recorded.

- **Entorhinal cortex**: Mentioned in passing as part of the hippocampal circuit but not directly studied.

- **Prefrontal cortex**: Cited as area involved in replay and sharp-wave ripples, with potential role in control and adaptation of replay (Berners-Lee et al., 2021).

- **Ventral striatum**: Mentioned as area involved in replay and sharp-wave ripples (Lansink et al., 2009).

- **Ventral tegmental area (VTA)**: Mentioned as area involved in replay and sharp-wave ripples (Gomperts et al., 2015; Valdés et al., 2015).

The paper emphasizes that while the hippocampus (particularly CA1) is the focus, the mechanism for encoding and controlling replay adaptation may involve intra-hippocampal synaptic plasticity or upstream structures (prefrontal cortex, striatum, VTA, cortex).

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight by providing both an algorithmic framework and neural data supporting that algorithm over alternatives.

**Algorithm**: The paper proposes that the hippocampus encodes a "cognitive graph" (Muller et al., 1996)—a stable map of locations (nodes) with traversable connections (edges)—and that replay sequences represent planned trajectories through this graph. The key algorithmic innovation is that edge weights (representing path connectivity) can be rapidly updated to reflect new barrier configurations while node representations (place fields) remain stable.

**Neural data supporting the algorithm**: The paper provides direct neural evidence:
1. Place fields remain stable (58% of cells, 87% of spatial bins) across 90+ barrier configurations, supporting stable nodes
2. Replay sequences rapidly adapt to respect new barriers (87% of sessions show significant barrier conformity), supporting flexible edge weights
3. Time-lag analysis shows barrier impermeability extends to all candidate events, not just selected replays
4. A minority of unstable cells encode local barrier configurations and show reinstatement when barriers return, suggesting a mechanism for learning local structure

**Marr's three levels analysis**:

- **Computational**: The brain must solve the problem of planning efficient paths to goals while avoiding obstacles, using a representation that supports both generalization (stable positions) and flexibility (adaptable connectivity). This is formalized as traversing a cognitive graph where edge weights encode traversability.

- **Algorithmic**: The hippocampus implements this through a dual representation system:
  1. **Stable place fields**: CA1 pyramidal cells encode position via stable firing fields, providing a consistent coordinate system (nodes)
  2. **Flexible replay generation**: During sharp-wave ripples, sequences of place cell activation traverse paths that respect current barrier configurations (edges), generated via modified synaptic weights or external control signals
  3. **Barrier-specific cells**: A minority population encodes local barrier structure, potentially guiding replay adaptation

- **Implementational**: At the neural hardware level, the mechanism involves:
  - **CA1 place cells**: Stable firing fields tied to anatomical location and idiothetic cues
  - **Synaptic plasticity**: The continuous attractor network simulation suggests that mixed synaptic weights (combining previous and current barrier configurations) can produce the observed mix of barrier-conforming and barrier-crossing replays
  - **Network dynamics**: Spike-frequency adaptation in attractor networks drives bump movement along learned paths
  - **Potential upstream control**: The ventral striatum, VTA, prefrontal cortex, and other structures may modulate replay content

---

### Limitations & open questions

1. **Causal manipulations absent**: The study is correlational; causal tests (e.g., optogenetic disruption of replay) would strengthen claims about replay's role in flexible behavior

2. **Limited behavioral readout**: While replay predicts future behavior, the precise computational function (planning vs. evaluation vs. memory consolidation) remains unclear

3. **Mechanism of replay adaptation unspecified**: The paper proposes synaptic weight changes in attractor networks but does not directly measure these; alternative mechanisms (e.g., external modulation from PFC or VTA) are not ruled out

4. **Generalization to non-spatial domains unclear**: The findings are specific to spatial navigation; whether similar dissociations occur in non-spatial memory tasks is unknown

5. **Role of unstable cells ambiguous**: The minority of barrier-sensitive cells may support replay adaptation, but their causal role and connectivity patterns are not established

6. **Potential contribution of theta sequences**: The paper mentions theta sequences as potentially similar to replay in supporting flexibility, but this was not directly tested

---

### Connections & keywords

**Key citations**:
- Pfeiffer and Foster (2013) — prior work on goal-directed replay
- Gupta et al. (2010) — replay as generative process
- Foster (2017) — review on replay function
- Muller et al. (1996); Burgess and O'Keefe (1996) — cognitive graph theory
- Alvernhe et al. (2008, 2011) — place field stability during barrier manipulation
- Thompson et al. (1984); Winocur et al. (2010); Maguire et al. (2006) — hippocampal dependence on detour tasks

**Named models or frameworks**:
- Cognitive graph theory (Muller et al., 1996)
- Cognitive map framework (O'Keefe and Nadel, 1978)
- Continuous attractor network model (Hopfield, 2010; Burak and Fiete, 2009)
- Bayesian decoding framework
- Successor representation (mentioned; Stachenfeld et al., 2017)
- Tolman-Eichenbaum machine (mentioned; Whittington et al., 2020)

**Brain regions**:
- Hippocampus CA1 (dorsal) — primary recording site, place cells and replay
- Hippocampus CA3 — mentioned as potential replay source
- Entorhinal cortex — mentioned as part of hippocampal circuit
- Prefrontal cortex — cited for involvement in replay control
- Ventral striatum — cited for replay involvement
- Ventral tegmental area (VTA) — cited for replay involvement

**Keywords**:
hippocampal replay, place cells, spatial navigation, barrier conformity, cognitive graph, flexible behavior, awake replay, sharp-wave ripples, sequence reactivation, spatial memory, attractor networks, Bayesian decoding, remapping, trajectory planning, goal-directed behavior, rat, CA1, dendritic computation, synaptic plasticity
