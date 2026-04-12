---
source_file: "balaguer2016_hierarchical_planning_subway.md"
paper_id: "balaguer2016_hierarchical_planning_subway"
title: "Neural Mechanisms of Hierarchical Planning in a Virtual Subway Network"
authors: "Jan Balaguer, Hugo Spiers, Demis Hassabis, Christopher Summerfield"
year: 2016
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["virtual_navigation"]
methods: ["fmri", "representational_similarity_analysis"]
brain_regions: ["hippocampus", "prefrontal_cortex", "ventromedial_prefrontal_cortex", "amygdala"]
frameworks: ["reinforcement_learning", "model_free_rl", "hierarchical_rl"]
keywords: ["botvinick", "niv_and_barto_2009_hierarchical_rl_and_neural_foundations", "ribas_fernandes_et_al_2011_neural_signature_of_hierarchical_rl", "subgoal_signal_in_medial_pfc", "holroyd_and_yeung_2012_anterior_cingulate_dmpfc_as_motivational_controller_of_extended_behaviour", "howard_et_al_2014_hippocampus_encoding_distance_to_goal_during_navigation", "van_den_heuvel_et_al_2003", "wagner_et_al_2006_rlpfc_and_plan_complexity_in_tower_of_london", "daw_et_al_2005", "2011_model_based_vs_model_free_rl", "sutton_and_barto_1998_options_framework_in_hierarchical_rl", "koechlin", "ody_and_kouneiher_2003", "koechlin_and_summerfield_2007_architecture_of_prefrontal_executive_control", "badre", "kayser_and_desposito_2010_frontal_hierarchy_and_abstract_action_rules", "named_models_or_frameworks", "hierarchical_reinforcement_learning_hrl_options_framework", "representational_similarity_analysis_rsa", "tower_of_london_task_comparison_paradigm"]
key_citations: ["botvinick2009_hierarchically_organized_behavior"]
---

### One-line summary

When humans navigate a virtual subway network, fMRI signals in dorsomedial prefrontal cortex and premotor cortex encode the cost of hierarchical plan representation (in units of contexts/line-changes), and the dmPFC additionally encodes the identity of the current context.

---

### Background & motivation

Planning in natural environments faces a combinatorial explosion: the number of possible action sequences grows exponentially with the planning horizon, making flat state-by-state search computationally intractable. A proposed solution is to cluster states hierarchically into "contexts," allowing plans to be described compactly in terms of context sequences and context switches rather than individual states. While prefrontal and hippocampal involvement in planning is well established, and computational models predict that hierarchical state abstraction should reduce representational cost, no prior neuroimaging study had identified brain regions specifically encoding hierarchical (context-level) plan complexity, or demonstrated that humans actually represent plans in this form during navigation.

---

### Methods

- **Task**: 20 healthy participants (2 excluded for poor performance) navigated a custom virtual subway network — 4 lines (contexts), each comprising named stations — from memory, pressing directional buttons to move station by station. No line/color information was shown during scanning. Training occurred 2 days prior in a separate behavioral session.
- **fMRI**: 3T BOLD imaging; 4 runs (~17 min each). Standard SPM12 preprocessing (realignment, normalization, 6 mm FWHM smoothing).
- **Distance measures**: Four indices of distance to goal were computed trial-by-trial: DS (stations), DL (lines/contexts), DX (exchange stations), and DU (U-turn cost — detour away from goal in cityblock space).
- **Univariate GLMs**: GLM1 included all four distance regressors as parametric modulators to identify brain regions tracking each type of plan complexity. GLM2 included DS alone for comparison with prior Tower of London literature.
- **Multivariate RSA**: Representational similarity analysis (searchlight, 15 mm sphere) identified regions where multivoxel patterns were more similar within than between subway lines (contexts), testing for abstract context encoding.
- **Brain-behavior correlations**: Across participants, RT sensitivity to each distance measure was correlated with BOLD sensitivity to the same measure in dmPFC and PMC.

---

### Key findings

- **Behavior**: Log RT scaled significantly with DL (lines to goal; t19 = 3.46, p = 0.003) and DU (U-turn cost; t19 = 4.26, p < 0.001) in a joint regression. DS (stations to goal) and DX failed to predict RT once hierarchical measures competed, indicating that the dominant planning cost was contextual, not state-by-state.
- **dmPFC (BA8/32) and premotor cortex (BA6/8)**: BOLD signals scaled with DL and DU (hierarchical cost measures) but not DX, in both regions. The pmC also showed DS sensitivity; the dmPFC did not when all regressors competed.
- **dmPFC context encoding**: RSA identified the dmPFC (peak −10, 8, 54; t19 = 7.49, p < 0.000001) as encoding the identity of the current subway line (context), even though line color was never shown during scanning. Context-specific distance-to-goal representations were also decodable in the dmPFC.
- **Bottleneck (exchange) stations**: Both dmPFC and PMC showed elevated BOLD at exchange stations vs. regular stations. PMC BOLD was tonically elevated before a context switch and dropped after (t19 = 3.24, p < 0.003), consistent with maintaining the hierarchical representation until the context switch resolves.
- **vmPFC and hippocampus**: Both tracked proximity to goal in units of stations (DS, negative correlation with distance), but showed no evidence of hierarchical (context-level) signals.
- **Brain-behavior correlations**: In dmPFC (but not PMC), the strength of DS and DL encoding predicted the corresponding RT costs across participants (DS: R = 0.60, p < 0.005; DL: R = 0.39, p < 0.05).
- **rlPFC**: Consistent with Tower of London literature, rlPFC tracked DS in GLM2 but did not encode DL — hierarchical cost was expressed caudally, not rostrally.

---

### Computational framework

The paper uses a **hierarchical reinforcement learning (HRL)** framework, drawing on the options framework (Sutton & Barto, 1998; Botvinick et al., 2009). The core idea is that states (stations) are clustered into contexts (subway lines), and a hierarchical plan is a sequence of context-level transitions rather than individual state transitions. Plan complexity (description length) is the key quantity: under a flat policy it scales with DS; under a hierarchical policy it scales with DL. "Bottleneck" states are those affording transitions between contexts (analogous to subgoal states in HRL). The paper operationalises these computationally as parametric regressors and tests whether neural activity encodes the relevant quantities.

Key variables: DL (hierarchical distance/plan cost), DS (flat distance), context identity (current subway line), and context switches at bottleneck stations.

---

### Prevailing model of the system under study

The paper frames its contribution against a backdrop in which:
1. Planning is broadly understood as mental search through a decision tree (model-based control), with PFC and hippocampus as key structures.
2. Prior neuroimaging had implicated rostrolateral PFC (and dorsolateral PFC) in encoding plan complexity for multistep problems (Tower of London), in proportion to the number of moves (flat distance, DS).
3. Hierarchical structure was theorised to reduce planning cost in both machine learning and computational neuroscience, but no neuroimaging study had identified regions specifically responsive to hierarchical plan complexity.
4. The dmPFC/pre-SMA was associated with conflict monitoring, subgoal attainment signals (Ribas-Fernandes et al., 2011), and motivational signals (Holroyd & Yeung, 2012), but its role in hierarchical planning per se was unestablished.
5. The hippocampus was known to track distance to goal during navigation; whether this involved hierarchical representations was unknown.

---

### What this paper contributes

The paper demonstrates empirically that humans represent plans hierarchically during navigation, and identifies the specific neural substrates of this hierarchy:
- It shows for the first time that BOLD signals in **caudal prefrontal cortex** (dmPFC and PMC/BA6-8) encode plan cost in units of contexts, not merely stations — establishing these regions, rather than rostral PFC, as the locus of hierarchical plan representation.
- It demonstrates that **dmPFC encodes current context identity** in an abstract, multivariate form (even without explicit cue display), suggesting a role in maintaining the contextual variable required for hierarchical policy execution.
- It dissociates the roles of medial PFC subregions: dmPFC carries the hierarchical signal and context representation; vmPFC carries a goal-proximity signal in flat (station-level) units.
- It shows that **hippocampus and vmPFC do not encode hierarchical plan structure**, constraining theories of hippocampal involvement in planning.
- The lack of hierarchical signal in **rlPFC** (contra Tower of London literature) is explained by the compression hypothesis: hierarchical chunking renders complex plans representable in a small number of steps, expressible in caudal rather than rostral prefrontal regions.

---

### Brain regions & systems

- **Dorsomedial prefrontal cortex (dmPFC / pre-SMA, BA8/32)**: encodes hierarchical plan complexity (DL and DU); responds to bottleneck/exchange stations; encodes current context identity via multivariate patterns; shows brain-behavior correlation with hierarchical planning cost.
- **Premotor cortex (PMC, BA6/8)**: encodes both hierarchical (DL, DU) and flat (DS) plan complexity; elevated BOLD before context switches (tonically maintained hierarchical representation); no brain-behavior correlation with planning cost; likely participates in active plan maintenance.
- **Ventromedial prefrontal cortex (vmPFC)**: tracks proximity to goal in flat (station-level) units (DS); no hierarchical signal; consistent with episodic future thinking and goal-state tracking.
- **Hippocampus**: tracks distance to goal in flat (station-level) units; no hierarchical signal; consistent with prior navigation neuroimaging.
- **Rostrolateral PFC (rlPFC, BA46)**: encodes DS (flat distance) consistent with Tower of London literature; does not encode hierarchical cost — hierarchical planning is caudal.
- **Bilateral BA46 (lateral PFC)**: also elevated at exchange vs. regular stations.
- **Amygdala / putamen**: interaction between station type and response switch (context switch); marginal, did not survive FDR correction.
- **Parietal cortex**: encodes response switch (direction change), not context switch.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Criterion 1 (algorithm)**: The paper formalises a hierarchical planning algorithm in which states are chunked into contexts, the planning cost is computed in units of context transitions (DL), and bottleneck states signal context switches. The dmPFC is proposed to encode both the current context and its associated planning cost, enabling hierarchical policy execution.

**Criterion 2 (neural data)**: fMRI data directly link the specific computational variables (DL, current context identity) to measured neural activity in dmPFC, and the brain-behavior correlations across participants tie dmPFC encoding strength to behavioral signatures of hierarchical planning.

**Marr's levels:**

- **Computational**: The brain solves the problem of planning efficiently in a high-dimensional state space by exploiting hierarchical structure — compressing long action sequences into context-level descriptions, thereby reducing the representational cost (description length) of a plan.
- **Algorithmic**: The hierarchical plan is represented as a sequence of contexts and context switches. The dmPFC maintains the current context identity (decodable via RSA) and tracks the remaining context-level cost (DL). PMC tracks the overall plan cost (DL, DS, DU) and sustains an elevated signal until a context switch resolves. Context switches at bottleneck stations are flagged by both regions.
- **Implementational**: Neural implementation is characterised at the level of BOLD signals in macroscopic PFC subregions. The paper does not characterise specific cell types, layers, connectivity, or neuromodulatory mechanisms underlying these computations.

---

### Limitations & open questions

- The study cannot distinguish plan formation from plan maintenance/monitoring: BOLD signals on the cue screen did not reliably correlate with distance metrics, possibly due to low statistical power (few cue-screen events).
- The nature of context representation remains unclear: contexts could be encoded as clusters of perceptual states, as macro-policies, or as spatial/geometric features of the map. The V4 activation at context switches hints at perceptual (color) recall, but this is speculative.
- The design measures a "cost of plan representation" that grows linearly with remaining contexts/stations — it does not directly capture recursive tree search or pruning, so the study cannot resolve whether planning is prospective or emergent from online replanning.
- Individual differences in dmPFC encoding of DS (as well as DL) suggest variability in whether participants use hierarchical or flat strategies; the design does not allow full characterisation of individual planning strategies.
- Only one subway map was used (counterbalanced in orientation and labeling), limiting generalisability to other hierarchical structures.
- Brain-behavior correlations in PMC were not significant, leaving its precise computational role (plan maintenance vs. execution) unresolved.

---

### Connections & keywords

**Key citations:**
- Botvinick, Niv & Barto (2009) — hierarchical RL and neural foundations
- Ribas-Fernandes et al. (2011) — neural signature of hierarchical RL, subgoal signal in medial PFC
- Holroyd & Yeung (2012) — anterior cingulate/dmPFC as motivational controller of extended behaviour
- Howard et al. (2014) — hippocampus encoding distance to goal during navigation
- van den Heuvel et al. (2003); Wagner et al. (2006) — rlPFC and plan complexity in Tower of London
- Daw et al. (2005, 2011) — model-based vs. model-free RL
- Sutton & Barto (1998) — options framework in hierarchical RL
- Koechlin, Ody & Kouneiher (2003); Koechlin & Summerfield (2007) — architecture of prefrontal executive control
- Badre, Kayser & D'Esposito (2010) — frontal hierarchy and abstract action rules

**Named models or frameworks:**
- Hierarchical reinforcement learning (HRL) / options framework
- Representational similarity analysis (RSA)
- Tower of London task (comparison paradigm)
- Model-based control / decision tree search

**Brain regions:**
- Dorsomedial prefrontal cortex (dmPFC / pre-SMA)
- Premotor cortex (PMC, BA6/8)
- Ventromedial prefrontal cortex (vmPFC)
- Hippocampus
- Rostrolateral prefrontal cortex (rlPFC, BA46)
- Parietal cortex
- Amygdala / putamen

**Keywords:**
- hierarchical planning
- hierarchical reinforcement learning
- prefrontal cortex
- context representation
- bottleneck states
- description length / plan complexity
- fMRI
- representational similarity analysis
- model-based planning
- virtual navigation
- subgoal
- dorsomedial prefrontal cortex
