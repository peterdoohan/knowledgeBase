---
source_file: "martinet2011_spatial_learning_action_planning.md"
paper_id: "martinet2011_spatial_learning_action_planning"
title: "Spatial Learning and Action Planning in a Prefrontal Cortical Network Model"
authors: "Louis-Emmanuel Martinet, Denis Sheynikhovich, Karim Benchenane, Angelo Arleo"
year: 2011
journal: "PLoS Computational Biology"
paper_type: "computational"
contribution_type: "theoretical"
species: ["rat"]
tasks: ["detour_task", "navigation_task"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "prefrontal_cortex", "striatum", "ventral_tegmental_area", "amygdala"]
keywords: ["spatial", "learning", "action", "planning", "prefrontal", "cortical", "network", "model"]
key_citations: ["hok2005_goal_coding_prefrontal"]
---

### One-line summary

A neurocomputational model of the prefrontal cortex (PFC), organised as a network of cortical columns and minicolumns, learns sparse topological maps from hippocampal place cell inputs and uses an activation diffusion mechanism to plan goal-directed trajectories, successfully reproducing Tolman & Honzik's cognitive "insight" detour task and matching the discharge properties of real rat PFC neurons.

---

### Background & motivation

Spatial navigation planning — the ability to mentally evaluate alternative action sequences and infer optimal routes to a goal — requires compact neural representations that go beyond route-based stimulus-response associations. The hippocampus provides redundant, distributed place codes that are not well suited for learning compact topological maps on their own. Anatomical and lesion evidence implicates the PFC in planning, yet no mechanistic account existed linking the PFC's columnar architecture to the computational process of building topological maps, performing graph-search planning, and generating the diversity of neural response types (spatial, prospective, reward-distance, strategy-switching) observed electrophysiologically. This paper fills that gap with a unified PFC network model validated against both behaviour and single-unit recordings.

---

### Methods

- **Model architecture**: A recurrent network of cortical columns, each comprising three unit populations (s, p, v) and a population of minicolumns with two unit types (q, d); no layer IV, consistent with rat medial PFC cytoarchitecture.
- **Two-level hierarchy**: A first population C1 receives direct hippocampal place cell (HP) input; a second population C2 integrates C1 output plus a proprioceptive signal (w) encoding the probability of sharp direction changes, enabling the model to represent alleys and corridors at coarser resolution.
- **Learning rule**: Unsupervised Hebbian plasticity shapes projections from HP cells onto s neurons (state encoding) and lateral projections (wpd, wqv) encoding forward and reverse associations between adjacent states.
- **Planning mechanism**: Activation diffusion — a reward signal is injected at the goal column, back-propagates through reverse associations (wqv), and then triggers a forward path signal (wpd) that reads out the optimal action sequence via winner-take-all competition among d neurons.
- **Simulation environment**: Tolman & Honzik's three-path detour maze implemented in the Webots 3D simulator, at 1:1 and 4:1 scales; 40 simulated animals per condition; 168 training trials plus 7 probe trials.
- **Neural analysis**: Shannon mutual information, PCA, and k-means clustering applied to both simulated and real rat medial PFC extracellular recordings (from S.I. Wiener's laboratory) to characterise spatial selectivity, distance-to-goal coding, prospective coding, and strategy-switching.

---

### Key findings

- The model reproduced Tolman & Honzik's behavioural results quantitatively: preference for path P1 (shortest) without blocks, preference for P2 (shortest detour) with block A, and the insight response (preference for P3 over P2) during probe trials with block B (all ANOVA p < 0.0001).
- Removing the C2 population impaired performance in the scaled-up (4:1) maze: no significant preference between P2 and P3 during block-A trials (p > 0.001) and failure on probe trials (p > 0.6756), demonstrating the functional necessity of hierarchical representations for large environments.
- The model produces progressive sparsification from HP to C1 to C2: population size, receptive field density, and redundancy decrease significantly at each stage (ANOVA p < 0.0001), consistent with Jung et al. (1998) recordings.
- C1 s neurons showed place fields consistent with experimental PFC recordings; C2 s neurons captured corridor-level structure with larger fields.
- v neurons encoded distance-to-goal via an exponentially decaying firing rate and showed frequency-selective responses matching a subset of real PFC neurons with no spatial correlate but distributed preferred discharge frequencies.
- p neurons displayed asymmetric, negatively skewed tuning curves and prospective coding: their discharge anticipated s neuron activity by ~1.6 s (SD ±0.6 s) and the rank ordering of p neuron firing rates before trajectory execution predicted the serial order of upcoming states, consistent with Averbeck et al. (2002) monkey PFC data.
- q and d neurons showed reward contingency-sensitive switching: when block A was encountered the ranking of q/d activities reversed within seconds, consistent with Rich & Shapiro (2009) strategy-switching PFC data.
- Unsupervised k-means clustering on six discharge statistics identified three clusters in both simulated and real PFC data with matching profiles in spatial information per spike, mean firing rate, and receptive field skewness, supporting the hypothesis that real PFC subpopulations correspond to the functional groups predicted by the model.

---

### Computational framework

The paper uses a **graph-based topological mapping** framework with **Hebbian unsupervised learning** and **activation diffusion** (spreading activation / breadth-first search) for planning.

- **What is being modelled**: The encoding of a topological-metrical cognitive map in a recurrent columnar network, and the retrieval of shortest goal-directed paths via forward/backward signal propagation.
- **Key variables**: State (location) activations in s neurons; forward associations (wpd) and reverse associations (wqv) as synaptic weight matrices; motivational (reward) signal injected into v neurons at the goal column; proprioceptive signal w encoding turning probability for C2 recruitment.
- **Assumptions**: (1) Cortical columns and minicolumns are the basic computational units; (2) strong propagation of neural activity (analogous to propagating waves) is physiologically plausible; (3) planning proceeds by mentally simulating both backward (goal) and forward (path) signal sweeps through the network; (4) a single appetitive motivational signal drives the reward representation.

---

### Prevailing model of the system under study

Before this paper, the dominant view was that the hippocampal formation — particularly CA3 recurrent collaterals — was the primary substrate for spatial map-based planning, with evidence from place cells and grid cells supporting a hippocampo-centric account. The PFC's role in spatial cognition was acknowledged through lesion and imaging data (impaired navigation planning after medial PFC lesions; PFC activation during navigation) and by recordings of spatially and reward-selective PFC neurons, but no mechanistic model linked the PFC's specific columnar architecture to the computational operations of topological map learning and trajectory planning. The extra-hippocampal planning system was hypothesised but lacked a concrete algorithmic implementation. The paper's introduction frames the hippocampal code as too redundant for compact topological representation and positions the PFC as the site where sparsification and hierarchical map construction occur.

---

### What this paper contributes

The model provides a concrete mechanistic proposal — grounded in cortical columnar anatomy and Hebbian learning — for how the PFC could build compact topological representations from redundant hippocampal inputs and use them for trajectory planning via activation diffusion. Key advances:

1. **Functional decomposition of PFC neuron types**: The model predicts five functionally distinct neuron classes (s, v, p, q, d) corresponding to spatial coding, distance-to-goal, prospective sequence coding, state-action value, and local action selection — and shows that corresponding subpopulations can be identified in real rat PFC recordings via unsupervised clustering.
2. **Hierarchical (two-level) representation**: Introduces a C1/C2 architecture where C2 encodes corridor-level features, allowing planning to scale to large environments — a prediction absent from prior hippocampus-centred models.
3. **Mechanistic account of Tolman insight**: The model explains the detour insight as goal-signal propagation through a topological graph in which common path sections are represented as shared nodes/edges — ruling out the sufficiency of stimulus-response or pure route-based models.
4. **Prospective coding and sequence planning**: Provides an algorithmic basis for the observed prospective firing and serial-order coding in PFC, linking it to the forward propagation of a planned trajectory signal.

---

### Brain regions & systems

- **Prefrontal cortex (medial PFC / prelimbic-infralimbic area)** — primary focus; proposed site of sparse topological map learning, action planning via activation diffusion, and prospective/distance-to-goal coding.
- **Hippocampal formation (CA1/CA3/subiculum, place cells)** — modelled as providing redundant distributed spatial input (HP cells with Gaussian place fields) to PFC; proposed to contribute to episodic/route memory rather than compact topological representations.
- **Entorhinal cortex (grid cells)** — cited as part of the hippocampal spatial system providing multiscale spatial input; not explicitly modelled.
- **Ventral tegmental area / dopaminergic system** — modelled implicitly as the source of the motivational reward signal driving v-neuron activation; role in sustaining PFC activity patterns noted.
- **Amygdala** — cited as a potential source of motivational signals to PFC; not modelled explicitly.
- **Basal ganglia / striatum** — cited as a potential neural substrate for the proprioceptive/habit signal w driving C2 recruitment; not modelled explicitly.
- **Posterior parietal cortex** — cited as part of the extra-hippocampal navigation planning network; not modelled.

---

### Mechanistic insight

The paper partially meets the bar. It formalises an algorithm (activation diffusion through a Hebbian-learned topological graph) and validates it against real PFC single-unit recordings. However, the neural data used are archival extracellular recordings from navigating rats (Wiener lab data), not recordings designed to test the specific model variables (e.g., manipulating goal-signal propagation or testing forward/backward sweep dynamics directly). The comparison between model and real data is correlational (matching statistical profiles of discharge properties) rather than a critical test of the activation diffusion algorithm versus alternatives.

- **Computational level**: The brain must solve the problem of finding the shortest path to a goal in a topological graph, while remaining robust to dynamic changes in path availability (blocked routes).
- **Algorithmic level**: Representations are sparse location codes in cortical columns; planning uses backward propagation of a reward signal (through wqv reverse associations) to assign goal-proximity values, followed by forward propagation of a path signal (through wpd) to read out the action sequence; a winner-take-all competition among d neurons selects actions locally.
- **Implementational level**: Addressed qualitatively. The columnar/minicolumnar anatomy of rat medial PFC is used to justify the architecture. Dopaminergic modulation is invoked as the mechanism sustaining reward signals in v neurons. The propagating activity is linked to observed travelling waves in cortex. However, cell-type-specific mechanisms, connectivity matrices, or biophysical properties are not modelled in detail — the model uses mean-field firing rates with scalar synaptic weights.

---

### Limitations & open questions

- The hippocampal model is highly simplified and does not capture remapping, extrafield firing, theta phase precession, or theta-frequency synchronisation with PFC — all of which are likely relevant to the hippocampal–PFC interaction at decision points.
- The motivational system represents only a single appetitive goal; the model cannot compare relative values of multiple goals or account for effort costs or delayed rewards influencing PFC-dependent decisions.
- The model was validated only in a structured alley maze (Tolman & Honzik); extension to open-field environments requires additional considerations around sensory aliasing and continuous action spaces.
- The w proprioceptive signal driving C2 recruitment is postulated but not implemented with a known neural substrate; habit learning in the striatum is one candidate but is not modelled.
- The comparison with real PFC recordings is statistical rather than causal: no manipulation (lesion, pharmacology, optogenetics) tests whether the model-predicted variables (e.g., disrupting the backward goal signal) produce the expected behavioural deficit.
- Sleep-dependent memory consolidation and hippocampal sharp-wave replay to PFC are not addressed, though acknowledged as an important future direction.
- The model makes the untested prediction that C2-like neurons (with corridor-level, alley-scale receptive fields) should exist in PFC of animals navigating large structured mazes.

---

### Connections & keywords

**Key citations**:
- Tolman & Honzik (1930) — original insight/detour task
- O'Keefe & Nadel (1978) — hippocampus as cognitive map
- Mountcastle (1957, 1997) — cortical column organisation
- Hasselmo (2005) — PFC columnar model for goal-directed behaviour
- Jung et al. (1998) — PFC place cell properties in rats
- Hok et al. (2005) — spatial goal coding in prelimbic/infralimbic PFC
- Benchenane et al. (2010) — hippocampal–PFC theta coherence at decision points
- Averbeck et al. (2002) — serial order coding in monkey PFC
- Rich & Shapiro (2009) — strategy-switching neurons in rat PFC
- Sheynikhovich et al. (2009) — hippocampal place cell model used as input

**Named models or frameworks**:
- Cortical column / minicolumn model (Mountcastle)
- Activation diffusion / spreading activation
- Tolman & Honzik detour maze
- C1/C2 hierarchical columnar architecture
- Hebbian unsupervised learning
- Breadth-first graph search (activation diffusion implementation)
- Cortical automaton (Burnod 1988/1991)

**Brain regions**:
- Medial prefrontal cortex (prelimbic / infralimbic area)
- Hippocampus (CA1, CA3, subiculum)
- Entorhinal cortex
- Ventral tegmental area
- Amygdala
- Striatum / basal ganglia
- Posterior parietal cortex

**Keywords**:
- topological map learning
- prefrontal cortex columnar organisation
- activation diffusion planning
- hippocampal–prefrontal interaction
- spatial navigation planning
- cognitive insight / detour navigation
- prospective coding
- distance-to-goal coding
- sparse population code
- hierarchical spatial representation
- Hebbian synaptic plasticity
- spreading activation
