---
source_file: "tanji2007_behavioral_planning_prefrontal.md"
paper_id: "tanji2007_behavioral_planning_prefrontal"
title: "Concept-based behavioral planning and the lateral prefrontal cortex"
authors: "Jun Tanji, Keisetsu Shima, Hajime Mushiake"
year: 2007
journal: "Trends in Cognitive Sciences"
paper_type: "review"
contribution_type: "review"
species: ["human", "macaque"]
methods: ["fmri"]
brain_regions: ["prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex", "dorsolateral_prefrontal_cortex"]
frameworks: ["reinforcement_learning", "hierarchical_rl"]
keywords: ["fuster_1977", "2004_perception_action_cycle_and_hierarchical_organization_of_frontal_function", "saito_et_al_2005_representation_of_immediate_and_final_behavioral_goals_in_lpfc", "shima_et_al_2007_categorization_of_behavioral_sequences_in_prefrontal_cortex", "freedman_et_al_2001_categorical_representation_of_visual_stimuli_in_primate_lpfc", "koechlin_et_al_2007_cascade_model_of_cognitive_control", "miller_and_cohen_2001_integrative_theory_of_prefrontal_cortex_function", "duncan_2001_adaptive_coding_model_of_prefrontal_function", "shima_and_tanji_1998", "tanji_and_shima_1994_role_of_sma_pre_sma_in_temporal_organization_of_multiple_movements", "named_models_or_frameworks", "script_based_action_planning_schank_and_abelson", "1977", "cascade_model_of_cognitive_control_koechlin_et_al", "2007", "perception_action_cycle_fuster", "adaptive_coding_model_duncan", "2001", "hierarchical_model_of_sequential_action_planning_lpfc_categories_sma_sequences_m1_actions", "brain_regions"]
---

### One-line summary

The lateral prefrontal cortex (LPFC) represents abstract action categories and behavioral goals during planning, rather than specific motor parameters, enabling hierarchical organization of sequential behavior.

---

### Background & motivation

Early theories of LPFC function focused on working memory, attentional control, and behavioral inhibition. However, accumulating evidence suggests the LPFC plays a broader role in executive control of behavior, including cross-modal and cross-temporal associations. This review synthesizes neurophysiological findings to argue that the LPFC is primarily involved in concept-based behavioral planning—representing abstract categories of action sequences and behavioral goals rather than specific motor commands.

---

### Methods

This is a review paper synthesizing evidence from:
- Single-cell recordings in macaque LPFC during behavioral planning tasks
- Human fMRI studies of prefrontal cortex function
- Clinical studies of frontal lobe patients
- Key experimental paradigms reviewed include:
  - Visuomotor association tasks examining object vs. movement representation
  - Behavioral rule tasks (match-to-sample, non-match, spatial rules)
  - Path-planning tasks in mazes requiring sequential goal achievement
  - Behavioral categorization tasks with alternate, paired, and repeat sequences

---

### Key findings

- **Object-centered representation**: LPFC neurons primarily represent the consequence of intended actions (e.g., cursor movement on screen) rather than the specific limb movements (hand/supination/pronation) used to achieve them.

- **Behavioral goal representation**: During planning, LPFC activity encodes final goals and intermediate subgoals in sequence, with activity shifting from final goal representation to immediate goal representation as planning progresses.

- **Category representation**: 51% of LPFC neurons active during planning showed selectivity for action categories (alternate, paired, or repeat sequences) rather than specific sequences. Individual sequence-specific activity was rare in LPFC but abundant in medial premotor areas.

- **Hierarchical organization**: The frontal cortex shows a hierarchical organization for sequential action planning: action categories in LPFC (highest level), action sequences in SMA/pre-SMA (middle level), and individual actions in primary motor cortex (lowest level).

- **Independence from reward**: Behavioral goal representation in LPFC can be independent of reward contingency, suggesting the LPFC is involved in representing goals as conceptual states rather than purely as reward-predictive outcomes.

---

### Computational framework

The review proposes a hierarchical, script-based framework for understanding behavioral planning:

- **Script-based action planning**: Action categories serve as "scripts" that describe general structures for appropriate event sequences. These scripts provide abstract templates (e.g., "alternate," "paired") that constrain the space of possible actions.

- **Slot-filling**: During planning, specific items are identified to fill "slots" in the script, transforming abstract category knowledge into concrete action sequences.

- **Hierarchical reinforcement learning**: The framework aligns with hierarchical RL models where high-level policies (categories) select lower-level policies (sequences), which in turn select individual actions.

- **Cascade model of cognitive control**: The LPFC's role in representing action categories is consistent with Koechlin's cascade model, where episodic control (selecting task sets based on prior events) operates at the highest level of the cognitive control hierarchy.

---

### Prevailing model of the system under study

Before the reviewed studies, the prevailing view of LPFC function centered on:

1. **Working memory**: The LPFC was primarily understood as a site for short-term retention of information, particularly for guiding forthcoming movements until execution.

2. **Attentional control**: The LPFC was thought to mediate selective attention, filtering relevant from irrelevant information.

3. **Behavioral inhibition**: The LPFC was believed to play a role in suppressing inappropriate responses.

4. **Motor representation**: Early single-cell studies suggested LPFC neurons might represent parameters of forthcoming movements similar to motor cortex, though this view was already being challenged by the time of the reviewed work.

The reviewed studies collectively moved beyond these classical frameworks to emphasize the LPFC's role in abstract, concept-level behavioral planning that is separable from both working memory and motor specification.

---

### What this paper contributes

This review synthesizes multiple lines of evidence to establish a new understanding of LPFC function:

1. **Concept-level representation**: The LPFC represents behavioral goals and action categories rather than specific motor plans. This shifts the understanding from "what movement to make" to "what outcome to achieve" and "what type of sequence structure applies."

2. **Hierarchical organization**: The review proposes a three-level hierarchy for sequential action planning: action categories (LPFC) → action sequences (medial premotor areas) → individual actions (primary motor cortex). This provides a framework for understanding how abstract intentions are translated into concrete movements.

3. **Script-based planning**: The "script" framework explains how category knowledge constrains planning without specifying all details. Categories serve as templates; slot-filling transforms templates into executable plans.

4. **Integration with cognitive control models**: The reviewed findings are linked to the cascade model of cognitive control, positioning LPFC category representation as a form of episodic control.

5. **Independence from reward**: The review highlights that LPFC represents behavioral goals independent of reward value, distinguishing LPFC function from orbitofrontal and medial prefrontal regions involved in reward-guided decision making.

---

### Brain regions & systems

- **Lateral prefrontal cortex (LPFC)** — Primary focus; represents action categories, behavioral goals, and subgoals during planning; involved in concept-level behavioral organization independent of motor specification.

- **Dorsolateral prefrontal cortex (DLPFC)** — Specifically implicated in representing action categories at the highest level of the planning hierarchy.

- **Supplementary motor area (SMA)** — Represents sequences of actions; intermediate level in the planning hierarchy between action categories (LPFC) and individual actions (M1).

- **Pre-supplementary motor area (pre-SMA)** — Involved in temporal organization of multiple actions; represents building blocks of time structures enabling sequential actions.

- **Primary motor cortex (M1)** — Specifies individual actions; lowest level in the planning hierarchy.

- **Orbitofrontal cortex** — Involved in reinforcement-guided decision making; contrasted with LPFC to emphasize that LPFC represents behavioral goals independent of reward.

- **Medial prefrontal cortex** — Principal division involved in reinforcement-guided decision making; contrasted with LPFC function.

---

### Mechanistic insight

This review paper does not present original mechanistic data but synthesizes findings from empirical studies. The mechanistic insights derived from the reviewed studies are:

The reviewed studies provide evidence for a **hierarchical, multi-level mechanism** for transforming abstract behavioral intentions into concrete actions:

**Computational level**: The brain solves the problem of planning complex, sequential behavior by representing abstract action categories (scripts) that constrain the space of possible action sequences. Behavioral goals are represented as conceptual states (e.g., "reach final goal via intermediate steps") rather than as reward values or motor parameters.

**Algorithmic level**: The LPFC implements category representation through population-level neural activity. Category-selective neurons (comprising ~51% of planning-related cells in LPFC) signal which abstract script applies. The algorithm proceeds through stages: (1) represent final goal; (2) generate intermediate goals/subgoals based on category constraints; (3) shift activity from final goal to immediate goal representation as execution approaches. This is distinct from sequence-specific representation, which is prominent in medial premotor areas but rare in LPFC.

**Implementational level**: The hierarchy is implemented across distinct frontal areas: DLPFC contains category-selective neurons; SMA/pre-SMA contains sequence-selective neurons; M1 contains movement-selective neurons. The LPFC's anatomical connectivity with multiple cortical and subcortical areas enables it to integrate information for conceptual-level planning. The reviewed studies do not specify cellular mechanisms (e.g., specific cell types, synaptic properties, neuromodulation) that might implement category selectivity within LPFC circuits.

**Limitation**: The reviewed papers provide correlational evidence (neural activity correlates with category/goal variables) but do not establish causal necessity or sufficiency of LPFC category representation for behavioral planning. The mechanism by which category signals in LPFC influence downstream sequence and motor representations remains unspecified.

---

### Limitations & open questions

The review explicitly identifies several unresolved questions and limitations:

- **Functional parcellation of LPFC**: The exact functional subdivisions within the LPFC remain unsolved. Current imaging techniques lack sufficient spatial resolution, and electrode placements in animal studies are inconsistent. Possible subdivisions along the dorsolateral axis and rostrocaudal axis require further investigation.

- **Neuronal mechanisms of category learning**: The mechanisms that allow category learning with respect to action sequences are not understood. A multidisciplinary approach is needed to analyze neuronal activity during learning and develop computational models explaining the development of category specificity.

- **Limits of abstract representation**: What is the limit of abstract representation in non-human primates? The review raises this as an open question for future research.

- **Reward-independent goal regulation**: Although reward relevance dominates current neuroscience research, a major part of higher-order behavioral goal characterization is independent of primary reinforcers. The review asks whether LPFC participates in developing behavioral goals that satisfy individuals at conceptual levels, leading to self-satisfaction.

- **Causal mechanisms**: The reviewed studies provide correlational evidence linking LPFC activity to category and goal representation, but causal necessity and sufficiency remain to be established.

- **Downstream influence**: How category signals in LPFC influence downstream sequence representation in medial premotor areas and motor execution in M1 remains unspecified at the mechanistic level.

---

### Connections & keywords

**Key citations:**
- Fuster (1977, 2004) — perception-action cycle and hierarchical organization of frontal function
- Saito et al. (2005) — representation of immediate and final behavioral goals in LPFC
- Shima et al. (2007) — categorization of behavioral sequences in prefrontal cortex
- Freedman et al. (2001) — categorical representation of visual stimuli in primate LPFC
- Koechlin et al. (2007) — cascade model of cognitive control
- Miller & Cohen (2001) — integrative theory of prefrontal cortex function
- Duncan (2001) — adaptive coding model of prefrontal function
- Shima & Tanji (1998); Tanji & Shima (1994) — role of SMA/pre-SMA in temporal organization of multiple movements

**Named models or frameworks:**
- Script-based action planning (Schank & Abelson, 1977)
- Cascade model of cognitive control (Koechlin et al., 2007)
- Perception-action cycle (Fuster)
- Adaptive coding model (Duncan, 2001)
- Hierarchical model of sequential action planning (LPFC categories → SMA sequences → M1 actions)

**Brain regions:**
- Lateral prefrontal cortex (LPFC)
- Dorsolateral prefrontal cortex (DLPFC)
- Supplementary motor area (SMA)
- Pre-supplementary motor area (pre-SMA)
- Primary motor cortex (M1)
- Orbitofrontal cortex
- Medial prefrontal cortex

**Keywords:**
- behavioral planning
- lateral prefrontal cortex
- action categories
- sequential behavior
- goal representation
- abstract representation
- cognitive control
- hierarchical organization
- macaque neurophysiology
- executive function
- concept formation
- script-based planning
