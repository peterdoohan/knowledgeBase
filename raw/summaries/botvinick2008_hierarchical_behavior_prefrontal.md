---
source_file: botvinick2008_hierarchical_behavior_prefrontal.md
paper_id: botvinick2008_hierarchical_behavior_prefrontal
title: "Hierarchical models of behavior and prefrontal function"
authors:
  - "Matthew M. Botvinick"
year: 2008
journal: "Trends in Cognitive Sciences"
paper_type: review
contribution_type: review
species:
  - human
methods:
  - fmri
brain_regions:
  - prefrontal_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - striatum
frameworks:
  - reinforcement_learning
  - hierarchical_rl
keywords:
  - hierarchical_action_control
  - temporal_abstraction
  - policy_abstraction
  - state_abstraction
  - prefrontal_rostro_caudal_gradient
  - hierarchical_reinforcement_learning
  - options_framework
  - working_memory_gating
  - schema_nodes
  - correlational_vs_instrumental_hierarchical_structure
  - habit_system_vs_goal_directed_system
  - frontopolar_cortex_pending_task_maintenance
  - hierarchical
  - models
  - behavior
  - prefrontal
  - function
key_citations:
  - lashley1951_serial_order_behavior
---

### One-line summary

This review surveys recent computational models of hierarchically structured behavior, focusing on how they address learning, the distinction between correlational and instrumental hierarchical structure, and the topographic organisation of hierarchical representations in prefrontal cortex.

---

### Background & motivation

Hierarchical structure in human behavior — the nesting of actions into coherent sub-tasks and goals — was a founding insight of the cognitive revolution, yet the computational mechanisms underlying it remain poorly understood. A resurgence of interest across cognitive psychology, developmental psychology, neuropsychology, and neuroscience has prompted a new generation of models. The review aims to synthesise these developments, identify what is genuinely new relative to earlier proposals (going back to Miller, Galanter and Pribram's TOTE model), and highlight open questions for empirical research.

---

### Methods

- **Scope**: Narrative review of computational and neuroscientific research on hierarchical action control, published primarily in the 2000s, with historical context extending back to the 1950s.
- **Inclusion**: Computational models of routine and goal-directed hierarchical behavior, neuroimaging and neurophysiological findings on frontal cortex organisation, and machine-learning work on hierarchical reinforcement learning.
- **Synthesis method**: Narrative and comparative — models are evaluated against shared desiderata (temporal abstraction, working memory requirements, learning) and against empirical findings on prefrontal topography.

---

### Key findings

- All existing models share the core assumption that hierarchical action organisation is mirrored by separable internal representations at multiple levels (temporal abstraction); they diverge on whether this requires an explicitly hierarchical architecture or can emerge from domain-general learning in recurrent networks.
- Cooper and Shallice's schema-node model uses a constitutively hierarchical architecture with explicit goal nodes encoding instrumental structure, accounting for everyday action slips and apraxic errors.
- Botvinick and Plaut's recurrent network model acquires hierarchical task structure implicitly through learning, encoding correlational (rather than instrumental) structure in distributed activation patterns; it does not require pre-specified schema nodes.
- O'Reilly and Frank's gating model learns via reinforcement mechanisms to store hierarchically nested context in multiple independently gated prefrontal "stripes", providing a biologically grounded account of rapid, selective working-memory updating.
- Hierarchical reinforcement learning (the options framework) offers a formal account of temporally abstract actions: options accelerate learning, but only when they are well-matched to task structure; poorly matched options slow learning.
- Recent neuroimaging evidence (Koechlin, Badre, Christoff and colleagues) points to a rostro-caudal gradient in lateral PFC, with progressively more abstract behavioral representations represented more anteriorly.
- Botvinick's recurrent network simulation showed that a functional gradient (context vs. current-stimulus coding) can emerge spontaneously from learning given only an initial architectural hierarchy, without pre-specifying what each level encodes.
- Reynolds and O'Reilly found that the gradient does not emerge spontaneously in a gating model without additional constraints; a maturational gradient (rostral stripes coming online later) may instead drive topographic organisation.
- Frontopolar cortex (Brodmann area 10) has been alternatively interpreted as: (a) the apex of a single hierarchical context system (Reynolds and O'Reilly), or (b) a mechanism for maintaining a pending task while a concurrent task completes (Koechlin and Hyafil) — effectively enabling switching among independent hierarchies.
- The rostro-caudal axis may reflect not only temporal abstraction but also policy abstraction (Badre and D'Esposito) and state abstraction (Christoff et al.), with a natural computational relationship among these three forms.

---

### Computational framework

The review covers several distinct frameworks:

1. **Schema / connectionist networks** (Cooper-Shallice; Botvinick-Plaut): discrete schema nodes with scalar activations, or recurrent networks where hierarchy emerges in distributed internal representations. Key variables: unit activations, top-down excitation, goal-gating signals.

2. **Gating model with reinforcement learning** (O'Reilly and Frank): prefrontal "stripes" act as independently gatable working-memory slots. Basal ganglia learn (via dopaminergic reward-prediction errors) when to gate information in or out. Key variables: stripe activations, gating signals, RPEs.

3. **Hierarchical reinforcement learning (HRL)** (Sutton-Precup-Singh options framework; Botvinick-Niv-Barto): the action set is augmented with temporally abstract actions ("options"), each with an option-specific sub-policy and termination condition. The actor-critic architecture is extended to include an option representation that modulates both policy and value estimates. Key variables: option identity, option-specific value functions, RPEs at multiple temporal scales.

A unifying thread across frameworks is **temporal abstraction** — the use of a single representation to span and coordinate a sequence of lower-level events — combined with the working-memory requirements this imposes (robust maintenance, rapid updating, selective updating).

---

### Prevailing model of the system under study

The paper's introduction frames the background as follows. Hierarchical structure in behavior has been recognised since Lashley (1951) and Miller, Galanter and Pribram (1960), and has been modeled computationally for decades. The dominant pre-existing models (TOTE units, Rumelhart-Norman typing model, Norman-Shallice supervisory attentional system, Cooper-Shallice contention scheduling) assumed that the processing architecture directly mirrors the task hierarchy — one schema node per task node — with little principled account of learning. The PFC, particularly DLPFC, was understood (following Fuster) as the locus of temporal integration, maintaining context across nested sub-goals. The review's contribution is to characterise what the new generation of models has added beyond this baseline.

---

### What this paper contributes

The review establishes several conceptual clarifications and open questions:

1. **Correlational vs. instrumental structure**: The distinction between these two forms of hierarchy, and their relationship to habitual vs. goal-directed action-control systems, is newly articulated. Prior models had conflated them.

2. **Learning as a central problem**: Older models hand-coded hierarchical structure; the new generation (O'Reilly-Frank gating, Botvinick-Plaut recurrent net, HRL) addresses how hierarchical representations are acquired through experience, and how good option sets transfer across tasks.

3. **Topographic organisation in PFC**: Recent neuroimaging data motivate — and constrain — computational models. Two mechanisms have been proposed (emergent gradient via learning vs. maturational gradient); both remain consistent with available data, leaving an empirical gap.

4. **Multiple forms of abstraction**: The review proposes that temporal, policy, and state abstraction may naturally co-vary along the rostro-caudal axis, providing a unifying account of seemingly disparate neuroimaging findings.

5. **FPC function**: Two competing computational roles for frontopolar cortex are clearly articulated for the first time in this comparative framework — apex of a single hierarchy vs. pending-task maintenance enabling multi-hierarchy switching.

---

### Brain regions & systems

- **Dorsolateral prefrontal cortex (DLPFC)** — primary locus of hierarchical context representation; proposed to maintain context at multiple nested levels of task structure; subject of rostro-caudal topography findings.
- **Frontopolar cortex (FPC; Brodmann area 10)** — apex of the frontal hierarchy; contested role: either represents the highest level of temporal context (Reynolds and O'Reilly) or maintains a pending task during concurrent task execution (Koechlin and Hyafil).
- **Striatum / basal ganglia** — in the O'Reilly-Frank model, the gating signal to PFC stripes is learned through cortico-striato-thalamo-cortical loops; dopaminergic signals drive gating learning.
- **Orbitofrontal cortex (OFC)** — in the Botvinick-Niv-Barto HRL mapping, OFC is proposed to encode option-level value information.
- **Lateral PFC (posterior to FPC)** — encodes progressively finer-grained (more caudal) levels of task context according to Koechlin's model.

---

### Mechanistic insight

The paper does not present original neural data. As a review it synthesises computational models and neuroimaging findings but does not provide recordings, lesion data, or pharmacology that directly map a specific algorithm's variables onto measured neural activity. Individual cited studies (e.g., Koechlin's fMRI work, O'Reilly-Frank simulations) each partially address mechanism, but as reviewed here they do not jointly satisfy the dual criterion of formalised algorithm + specific neural evidence for that algorithm over alternatives.

At the level of the review's own contribution: the Botvinick-Niv-Barto HRL framework proposes a mapping (option representation → DLPFC; option-value → OFC; RPE → dopamine/striatum), but this is a theoretical proposal supported by analogy to existing single-unit and imaging literature, not by new data specifically discriminating HRL from flat RL.

The review does not meet the bar for the Mechanistic insight section.

---

### Limitations & open questions

- Whether two distinct systems (habit/correlational vs. goal-directed/instrumental) are both capable of encoding hierarchy, and how they interact, remains unresolved.
- The computational factors driving the emergence — or not — of rostro-caudal topography in PFC are unclear; the discrepancy between Botvinick's and Reynolds-O'Reilly's simulation results has not been resolved.
- How good option sets (abstract actions useful across tasks) are learned remains an open problem in both machine learning and neuroscience.
- The relative contributions of temporal, policy, and state abstraction to the functional gradient in DLPFC are not empirically disentangled.
- The paper does not address how the proposed mechanisms interact with other cognitive systems (e.g., episodic memory, language) that also exhibit or exploit hierarchical structure.

---

### Connections & keywords

**Key citations**:
- Lashley (1951) — serial order in behavior
- Miller, Galanter and Pribram (1960) — TOTE model, Plans and the Structure of Behavior
- Cooper and Shallice (2000, 2006) — schema-node model of hierarchical action
- Botvinick and Plaut (2004, 2006) — recurrent network model of routine sequential action
- O'Reilly and Frank (2006) — gating model of PFC/basal ganglia working memory
- Sutton, Precup and Singh (1999) — options framework for HRL
- Botvinick, Niv and Barto (in press) — HRL and neural foundations
- Koechlin et al. (2003); Koechlin and Hyafil (2007); Koechlin and Summerfield (2007) — frontal architecture and FPC function
- Badre and D'Esposito (2007) — fMRI evidence for hierarchical PFC organisation
- Fuster (1990, 2001, 2004) — DLPFC and temporal integration

**Named models or frameworks**:
- TOTE (Test-Operate-Test-Exit) unit
- Contention scheduling (Norman-Shallice supervisory attentional system)
- Cooper-Shallice schema-node model
- Botvinick-Plaut recurrent network model
- O'Reilly-Frank gating model (PFC stripes)
- Options framework / hierarchical reinforcement learning (HRL)
- Botvinick-Niv-Barto actor-critic HRL model
- Koechlin cascade/branching model of PFC

**Brain regions**:
- Dorsolateral prefrontal cortex (DLPFC)
- Frontopolar cortex (FPC; Brodmann area 10)
- Orbitofrontal cortex (OFC)
- Striatum / basal ganglia
- Lateral PFC

**Keywords**:
- hierarchical action control
- temporal abstraction
- policy abstraction
- state abstraction
- prefrontal rostro-caudal gradient
- hierarchical reinforcement learning
- options framework
- working memory gating
- schema nodes
- correlational vs. instrumental hierarchical structure
- habit system vs. goal-directed system
- frontopolar cortex pending-task maintenance
