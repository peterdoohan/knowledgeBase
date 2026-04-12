---
source_file: elgaby2023_behavioral_structure_mapping.md
paper_id: elgaby2023_behavioral_structure_mapping
title: "A Cellular Basis for Mapping Behavioural Structure"
authors:
  - "Mohamady El-Gaby"
  - "Adam Loyd Harris"
  - "James C. R. Whittington"
  - "William Dorrell"
  - "Arya Bhomick"
  - "Mark E. Walton"
  - "Thomas Akam"
  - "Tim E. J. Behrens"
year: 2023
journal: "bioRxiv (preprint, doi: 10.1101/2023.11.04.565609)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - electrophysiology
  - behavioral_analysis
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - prelimbic_cortex
  - striatum
  - thalamus
frameworks:
  - attractor_networks
  - tolman_eichenbaum_machine
keywords:
  - goal_progress_cells
  - structured_memory_buffers
  - behavioural_schema
  - task_space_mapping
  - ring_attractor
  - modular_organisation
  - zero_shot_inference
  - abstract_task_structure
  - prelimbic_cortex
  - sequence_memory
  - mnemonic_fields
  - cognitive_map
  - cellular
  - basis
  - mapping
  - behavioural
  - structure
key_citations:
  - behrens2018_cognitive_map_organizing_knowledge
  - whittington2020_tolman_eichenbaum_machine
  - samborska2021_hippocampus_prefrontal_gen_b
  - basu2021_ofc_navigation_goals
---

### One-line summary

Neurons in the mouse medial frontal cortex implement a "Structured Memory Buffer" algorithm — organised into goal-progress-tuned, modular attractor rings — that encodes entire behavioural sequences and enables zero-shot transfer of abstract task structure to new scenarios.

---

### Background & motivation

Flexible behaviour requires not just maps of the external world but also maps of one's own behavioural structure — the hierarchical relationships among goals and the sequences of actions linking them. While algorithms for mapping world structure (place cells, grid cells) are increasingly well characterised, the biological algorithms the brain uses to map complex, structured behavioural sequences remain largely unknown. The frontal cortex has been implicated in schema formation, goal encoding, and sequence generation, but no mechanistic, cellular-level account of how frontal activity generates an abstract map of task structure that transfers across tasks had been demonstrated. This paper directly addresses that gap.

---

### Methods

- **Task (ABCD paradigm):** 11 male C57BL/6J mice navigated a 3x3 grid maze, learning to visit 4 reward locations (a, b, c, d) in a repeating loop. Reward locations changed across up to 40 tasks, but the 4-goal ABCD loop structure was constant. Physical and task-space distances were orthogonalised across task configurations.
- **Behavioural regimes:** Early tasks (1–10) allowed learning to asymptote (~325 trials/task); late tasks (11–40) used a high-turnover regime (3 tasks/day, ~38 trials/task) to probe structure transfer. Zero-shot inference was assessed on the first trial of new tasks, specifically the d→a transition (never previously experienced).
- **Electrophysiology:** Silicon probe recordings from prelimbic medial frontal cortex (mFC) in 5 mice performing late tasks (tasks 21–40), yielding 1,438 neurons across 24 recording days (1,807 neuron-days). Each recording day comprised 3 new-task sessions + 1 repeated-task session (X') plus pre- and post-task sleep.
- **Neural analyses:**
  - Generalised linear model (GLM) decomposing variance attributable to goal-progress, place, speed, acceleration, time-from-reward, distance-from-reward, and task state.
  - Cross-task state-tuning coherence to characterise remapping and modular organisation; tSNE + hierarchical clustering on pairwise coherence distance matrix.
  - Three complementary cross-validation analyses of mnemonic field structure: (1) regression predicting state tuning from goal-progress/place anchors and task-space lags; (2) lagged spatial-correlation analysis; (3) single-anchor alignment analysis.
  - Logistic regression predicting upcoming behavioural choices from neuronal "bump-time" activity, controlling for 5 trials of autocorrelation.
  - Sleep co-activity analysis: linear regression of pairwise circular vs. forward task-distance against sleep cross-correlation for co-anchored neuron pairs.

---

### Key findings

- **Zero-shot inference:** Experienced mice (late tasks) took the most direct d→a path on the very first trial of new tasks significantly above chance (Wilcoxon, P=0.009), demonstrating transfer of abstract task structure without prior experience of that specific transition. First-trial performance improved across tasks (one-way repeated-measures ANOVA, F=3.10, P=0.010).
- **Goal-progress tuning is the dominant mFC signal:** 80% of mFC neurons were significantly tuned to the animal's fractional progress between consecutive goals, invariant to the specific goal location or trajectory taken (one-sample t-test vs. 0, N=1438, P=2.71×10⁻⁸²). Tuning was independent of elapsed time, physical distance, speed, and acceleration.
- **State tuning as a subset:** 56% of neurons showed state (ABCD position) tuning in at least one task; 87% of state-tuned neurons were also goal-progress tuned. 60% of goal-progress neurons had some state preference.
- **State tuning remaps but does not generalise:** Unlike goal-progress tuning, state-tuning angles shifted across distinct tasks (proportion generalising = 20%, below chance of 25%; z=9.04, P<0.001). State preferences were highly conserved across repeated sessions of the same task (87% stable, P<0.001).
- **Modular organisation:** Pairwise coherence analysis and hierarchical clustering revealed that mFC neurons are organised into modules — groups whose within-module state-tuning relationships are preserved across task instances (silhouette scores significantly above permuted controls, Wilcoxon, N=24 days, P=0.003). Coherent pairs showed a trend toward anatomical proximity (P=0.065).
- **Mnemonic fields at fixed task-space lags:** Three convergent cross-validation analyses confirmed that state-tuned neurons fire at a fixed lag in task-space from a specific goal-progress/place anchor, rather than at an abstract ordinal state. This held for neurons with non-zero lag (t-tests against 0, all P<0.001), including those lagged ≥90° from their anchor.
- **Distal behavioural prediction:** Neuronal activity at the neuron-specific "bump time" significantly predicted the animal's choice to visit the anchor location on the following trial (bump time regression coefficient significantly positive, P=0.017), while activity at random, decision, or 90/180/270° shifted times did not. Prediction was specific to low-probability (goal-directed) choices (P=0.047) and absent for high-probability (habitual) choices (P=0.747).
- **Ring-shaped offline organisation:** During sleep, co-anchored neuron pairs closer in circular task-space (ring distance) showed greater co-activity (regression coefficient for circular distance significantly negative, t=-1.656, P=0.049, controlling for forward distance, spatial map similarity, and goal-progress proximity). This ring structure was present in both pre- and post-task sleep.

---

### Computational framework

**Attractor network / ring attractor dynamics with structured memory buffers (SMBs).**

The paper proposes and validates the Structured Memory Buffer (SMB) model. The core formalism is:

- Each mFC neuron belongs to a module (ring attractor) anchored to a specific conjunction of goal-progress level and maze location (a "behavioural step"). Within a module, neurons tile the ring, each firing at a fixed task-space lag from the anchor.
- When the animal visits the anchor behavioural step, a bump of activity is initiated on that ring. The bump propagates around the ring paced by the animal's goal-progress (not elapsed time or distance), completing a full rotation after one task cycle (4 goals in the ABCD paradigm).
- Because the ring mirrors the 4-goal loop, when the bump circulates back near the anchor it biases the animal to repeat the same action at the same task phase — implementing policy retrieval without new synaptic plasticity.
- Multiple rings, each anchored to a different behavioural step, are active simultaneously. Their collective instantaneous activity encodes the entire history of recent behavioural steps, allowing distal (tens of seconds ahead) prediction of future choices.

Key variables: goal-progress (fractional progress between rewards), task-space lag, anchor (goal-progress × place conjunction), bump position on the ring.

Key assumptions: activity evolves as a function of goal-progress (not time/distance); the ring structure is pre-sculpted by prior learning; policy retrieval is achieved through network dynamics, not associative binding.

---

### Prevailing model of the system under study

The paper's introduction frames two competing frameworks for how frontal cortex supports task-structure generalisation:

1. **Associative binding model:** Neurons in frontal cortex develop abstract, invariant representations of task states (A, B, C, D) that are flexibly re-bound via synaptic plasticity to neurons representing specific sensorimotor details in each new task. This view predicted that state-tuned mFC neurons should maintain their state preferences across tasks.

2. **Network dynamics model (from recurrent neural network theory):** Schematic inferences can be made in new scenarios without new plasticity; instead, details of new task examples are encoded as patterns of neural activity shaped by the abstract structure of previously learned tasks. This view emphasised mnemonic representations tracking previous actions and rewards.

Both views agreed that frontal neurons track progress toward individual goals regardless of sensorimotor specifics, but neither had resolved how this goal-progress tuning relates to tracking position in a multi-goal hierarchy, nor had the cellular-level algorithm been demonstrated in vivo.

---

### What this paper contributes

- **Refutes the associative binding model at the multi-goal level:** State tuning does not generalise across tasks — neurons remap — contradicting the prediction that abstract state cells re-bind to new task content. State preferences are instead anchored to concrete goal-progress/place conjunctions.
- **Establishes goal-progress tuning as the scaffold for behavioural schema:** The invariant component is not ordinal task position but fractional progress toward individual goals. This scaffold enables representations to generalise across sequences of different durations, distances, and locations.
- **Provides a concrete cellular algorithm:** The SMB model, supported by three independent neural analyses plus offline sleep data, specifies how mFC neurons implement a ring-attractor memory buffer anchored to behavioural steps. This unifies mFC roles in sequential working memory and schema-based generalisation within a single mechanistic framework.
- **Demonstrates distal behavioural prediction:** mFC activity encodes the upcoming policy specifically at the "bump time" (not at decision time), showing that sequence retrieval is implemented via propagating attractor dynamics rather than just-in-time decision signals.
- **Identifies a modular attractor organisation analogous to grid cell modules:** Like medial entorhinal grid cells mapping physical space, mFC neurons are internally organised and modular, pointing to a general cortical strategy for mapping spaces from different reference points.

---

### Brain regions & systems

- **Medial frontal cortex (mFC) / prelimbic cortex** — primary recording site; proposed locus of goal-progress cells, structured memory buffers, and behavioural schema formation. Silicon probes targeted 1mm of the anterior-posterior extent of the prelimbic region.
- **Hippocampus and medial entorhinal cortex (mEC)** — discussed as providing spatial input (place/grid cell signals) to mFC to generate goal-progress/place anchor conjunctions; analogy with grid cell modules is central to the discussion.
- **mFC–thalamus–basal ganglia loops** — proposed circuit for learning task-structured memory buffers via recurrent plasticity (discussion only, not recorded in this study).

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Criterion 1 (algorithm):** The SMB model formalises a specific algorithm — ring-attractor dynamics anchored to goal-progress/place conjunctions, with activity bumps propagating as a function of task progress and cycling back to bias future behaviour.

**Criterion 2 (neural data supporting that algorithm over alternatives):** Three convergent electrophysiological analyses (regression-based mnemonic field fitting, lagged spatial correlation, single-anchor alignment) confirm the predicted fixed-lag structure of individual neurons and its cross-task invariance. Behavioural prediction analyses show that activity at the theoretically predicted "bump time" — not at other task-space phases — forecasts future choices. Sleep co-activity data confirm the ring geometry offline. The associative binding alternative (invariant abstract state tuning) is directly falsified.

**Marr's levels:**

- **Computational:** The brain needs to encode the structure of multi-goal behavioural sequences in a way that generalises across instances (same loop structure, different locations) and enables zero-shot transfer and policy retrieval without new plasticity.
- **Algorithmic:** Goal-progress-tuned neurons serve as a basis. A subset forms modules (ring attractors) anchored to specific goal-progress/place conjunctions. Activity bumps propagate around each ring paced by goal-progress, encoding the elapsed task-space from each visited behavioural step. The complete instantaneous population activity encodes the entire policy, and bump dynamics near the anchor bias future choices.
- **Implementational:** The implementation is partially characterised. The recording site is prelimbic mFC (single-unit silicon probe data). Modular clustering suggests anatomically localised assemblies (coherent pairs trend toward anatomical proximity, P=0.065). The paper proposes (but does not directly test) that spatial input from hippocampus/mEC generates goal-progress/place anchors, and that mFC–thalamus–basal ganglia recurrent loops support learning of the task-structured ring organisation.

---

### Limitations & open questions

- Recording from only 5 mice during late tasks; the cellular changes accompanying learning of the abstract structure from early to late tasks are not characterised.
- The circuit mechanism generating the ring organisation is hypothesised (hippocampus → mFC spatial input; thalamo-basal ganglia recurrent loops) but not directly tested via manipulation or connectivity analysis.
- The learning rule that sculpts naive goal-progress sequences into structured memory buffers is unknown. The paper notes that monitoring and manipulating mFC neurons during early task learning will be essential.
- Anatomical proximity of coherent neuron pairs was only a trend (P=0.065); the physical substrate of modularity within prelimbic cortex remains unresolved.
- How the associative binding and network-dynamics solutions coexist in the same or distinct circuits, and when each is used, remains an open question.
- Generality of the ABCD paradigm: the task uses a simple 4-reward loop; whether SMBs scale to more complex, branching or hierarchically deeper structures is not tested.
- The recording is from prelimbic (medial PFC) only; the contribution of other frontal subregions (orbitofrontal, anterior cingulate, supplementary motor) is not addressed.

---

### Connections & keywords

**Key citations:**
- Hafting et al. 2005 (*Nature*) — grid cells in entorhinal cortex, modular organisation
- Behrens et al. 2018 (*Neuron*) — cognitive maps and flexible behaviour
- Whittington et al. 2020 (*Cell*) — Tolman-Eichenbaum Machine
- Tse et al. 2007 (*Science*) — schemas and memory consolidation
- Wallis, Anderson & Miller 2001 (*Nature*) — abstract rule coding in PFC
- Samborska et al. 2021 (bioRxiv) — complementary task representations in hippocampus and PFC
- Chiang & Wallis 2018 (*PNAS*) — spatiotemporal encoding of search strategies by PFC neurons
- Basu et al. 2021 (*Nature*) — orbitofrontal cortex maps future navigational goals
- Bernardi et al. 2020 (*Cell*) — geometry of abstraction in hippocampus and PFC

**Named models or frameworks:**
- Structured Memory Buffer (SMB) model
- ABCD paradigm (task)
- Ring attractor dynamics
- Goal-progress cells

**Brain regions:**
- Medial frontal cortex (mFC) / prelimbic cortex
- Hippocampus
- Medial entorhinal cortex (mEC)
- Thalamus / basal ganglia (hypothesised circuit)

**Keywords:**
- goal-progress cells
- structured memory buffers
- behavioural schema
- task-space mapping
- ring attractor
- modular organisation
- zero-shot inference
- abstract task structure
- prelimbic cortex
- sequence memory
- mnemonic fields
- cognitive map
