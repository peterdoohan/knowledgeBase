---
source_file: coutureau2003_infralimbic_prefrontal_goal.md
paper_id: coutureau2003_infralimbic_prefrontal_goal
title: "Inactivation of the infralimbic prefrontal cortex reinstates goal-directed responding in overtrained rats"
authors:
  - "Etienne Coutureau"
  - "Simon Killcross"
year: 2003
journal: "Behavioural Brain Research"
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - lesion
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - striatum
  - dorsolateral_striatum
  - nucleus_accumbens
  - amygdala
  - basolateral_amygdala
keywords:
  - habit_formation
  - goal_directed_behaviour
  - action_outcome_associations
  - stimulus_response_associations
  - reward_devaluation
  - specific_satiety_devaluation
  - muscimol_inactivation
  - infralimbic_cortex
  - medial_prefrontal_cortex
  - dual_process_instrumental_learning
  - behavioural_autonomy
  - instrumental_overtraining
  - inactivation
  - infralimbic
  - prefrontal
  - cortex
  - reinstates
  - goal
  - directed
  - responding
key_citations:
  - balleine1998_goal_directed_instrumental_action
---

### One-line summary

Temporary muscimol inactivation of the infralimbic (IL) medial prefrontal cortex in overtrained rats restores sensitivity to reward devaluation, demonstrating that habit formation actively suppresses intact goal-directed action-outcome associations rather than destroying them.

---

### Background & motivation

Instrumental behaviour in rodents transitions from goal-directed (action-outcome, A-O) control to habitual (stimulus-response, S-R) control with extended training, as measured by sensitivity to reward devaluation. Prior work established a double dissociation: prelimbic (PL) cortex lesions produce habit-only animals after minimal training, while infralimbic (IL) lesions prevent habit formation even after extensive training. However, this lesion work could not distinguish between two competing hypotheses: (1) overtraining degrades A-O associations themselves, or (2) overtraining reduces the *influence* of intact A-O associations via active inhibition. The present study was designed to discriminate between these possibilities by applying post-training, reversible IL inactivation.

---

### Methods

- **Subjects**: 16 male Lister-hooded rats
- **Design**: Between-subjects; Group MUS (muscimol, n=7) vs. Group VEH (vehicle, n=7)
- **Training**: 20 sessions of variable interval 60-s lever press training for either sucrose or pellet reward, followed by surgical cannula implantation targeting bilateral IL cortex (AP +3.0, L ±0.75, V −3.5 mm from Bregma), and 2 additional training sessions
- **Context extinction**: 6 sessions of unrewarded, lever-absent context exposure to reduce Pavlovian contextual influences on subsequent test performance
- **Pharmacological inactivation**: Bilateral infusions of muscimol (GABAA agonist; 0.5 µl, 1.0 µg/µl) or ACSF vehicle delivered immediately prior to each devaluation extinction test
- **Devaluation procedure**: Specific-satiety devaluation — rats pre-fed to satiety on either the training outcome or an alternative reward, then tested in a 15-min lever-press extinction session (no reward delivered); counterbalanced across two test days
- **Measurements**: Lever press rate (as proportion of baseline) and magazine approach during extinction tests; food consumption post-test to verify devaluation
- **Histology**: Cannula placement verified via cresyl violet-stained sections; one MUS animal excluded for dorsal cannula misplacement

---

### Key findings

- Control (VEH) animals showed no significant difference in lever pressing between devalued and non-devalued conditions, confirming habitual responding after extended training
- Muscimol (MUS) animals showed a significant reduction in responding when the training outcome was devalued relative to the non-devalued control condition (group × devaluation interaction: F(1,12) = 7.4, p < 0.05; simple effect in MUS: F(1,12) = 9.7, p < 0.05; F < 1 in VEH)
- MUS animals also showed higher non-devalued responding than VEH animals (F(1,19) = 4.7, p < 0.05), consistent with reinstatement of goal-directed motivational sensitivity
- Consumption tests confirmed equivalent devaluation of food reward in both groups (no group main effect, F < 1), ruling out differences in satiety as an explanation
- Baseline lever press rates did not differ between groups prior to tests (MUS ≈ 12–14 responses/min; VEH ≈ 11–12 responses/min), ruling out performance confounds
- Magazine approach data showed a numerically similar pattern (devalued ≈ 0.10 vs. non-devalued ≈ 0.27 in MUS; 0.17 vs. 0.17 in VEH) but did not reach statistical significance

---

### Computational framework

Not applicable as a formal computational framework. The paper is framed within a dual-process associative learning theory distinguishing action-outcome (A-O, goal-directed) from stimulus-response (S-R, habitual) control. The key theoretical distinction is between two algorithmic accounts of habit formation: (1) A-O association strength declines with extended training, or (2) A-O associations remain intact but are actively suppressed by an inhibitory mechanism. The results support the second account, implying that habit formation involves an active gating or inhibition process rather than simple associative decay. These findings constrain reinforcement-learning models: they suggest a competition mechanism in which S-R control is not achieved merely through stronger S-R weights, but through an active prefrontal inhibitory process that suppresses A-O-based responding.

---

### Prevailing model of the system under study

The field had established a two-process view of instrumental action in which early learning is controlled by A-O associations (goal-directed, flexible) and extended training yields domination by S-R associations (habitual, inflexible). The transition was generally understood to reflect a gradual shift in associative strength driven by perceived action-outcome contingency: as training proceeds, the correlation between responses and rewards decreases (under interval schedules), weakening A-O contributions and allowing S-R habits to dominate. The role of the medial PFC was known from prior lesion work (Killcross & Coutureau, 2003), which showed a dissociation between PL cortex (supporting goal-directed action) and IL cortex (required for habit formation). However, whether IL cortex was needed only during habit *acquisition* or also for ongoing habit *maintenance/expression* was unknown, and whether extended training had permanently degraded A-O representations remained an open question.

---

### What this paper contributes

The central contribution is a mechanistic clarification: A-O associations are not destroyed by overtraining; they persist but are actively suppressed. The post-training reversible inactivation approach is critical — because habits were already established before IL cortex was silenced, the reinstatement of goal-directedness cannot be attributed to prevention of habit acquisition. This rules out the passive-decay account and supports a model in which the IL cortex actively inhibits goal-directed responding during habitual performance. This has implications beyond basic learning theory: it implies that in habitual or compulsive behavioural states (e.g., addiction), the goal-directed system may remain intact and potentially recoverable if IL inhibitory control is lifted. The paper also extends the analogy with the dorsolateral striatum (Yin et al., 2002), suggesting the IL cortex may govern competition between prefrontal goal-directed and striatal habit systems rather than directly mediating S-R storage.

---

### Brain regions & systems

- **Infralimbic (IL) medial prefrontal cortex** — primary focus; proposed to actively suppress goal-directed A-O responding, enabling habitual S-R performance to dominate; inactivation reinstates goal-directedness in overtrained animals
- **Prelimbic (PL) medial prefrontal cortex** — contrasted with IL; cited as supporting active maintenance of goal representations and A-O associations (from prior work); lesions produce habit-only performance
- **Dorsolateral striatum** — cited as the substrate of S-R habit development; lesions (Yin et al., 2002) produce a parallel reinstatement of goal-directedness, suggesting IL-striatal competition
- **Nucleus accumbens (shell and core)** — noted as a projection target of IL cortex and potential interface in a cortico-striatal hierarchy governing goal-directed vs. habitual control
- **Basolateral amygdala** — mentioned as a likely partner to PL cortex in maintaining goal-sensitive representations (Balleine, Killcross & Dickinson, 2003)

---

### Mechanistic insight

This paper meets the bar for mechanistic insight at the algorithmic and implementational levels, with some caveats.

**Criterion 1 (algorithm)**: The paper formalises an inhibitory algorithm — habit expression requires the IL cortex to actively suppress A-O-driven responding; without IL activity, the goal-directed system reasserts control.

**Criterion 2 (neural data)**: Pharmacological inactivation of IL cortex (muscimol) directly demonstrates that the habitual behavioural state is dependent on ongoing IL activity, and that its removal restores goal-directed performance. This goes beyond lesion studies by showing the effect is reversible and post-training, ruling out developmental or acquisition explanations.

**Marr's levels:**

- **Computational**: The brain must arbitrate between goal-directed and habitual response strategies. In overtrained animals, the computational problem is to suppress flexible but computationally expensive A-O-based control in favour of efficient S-R responding.
- **Algorithmic**: The IL cortex implements an inhibitory gate on A-O association expression. A-O associations remain encoded (their representations are intact), but their influence on motor output is suppressed when IL is active during habitual performance. Silencing IL removes this gate, allowing A-O representations to drive responding.
- **Implementational**: IL cortex projects to nucleus accumbens shell and reciprocally to PL cortex. The paper proposes a contention-scheduling account (Shallice, 1988) in which IL modulates competition between PFC goal-directed and striatal habit circuits. No cell-type or neuromodulator specificity is identified. **Bonus**: The dorsolateral striatum is identified as the likely physical locus of S-R habit storage, with IL cortex governing the balance of control rather than storing habits itself.

---

### Limitations & open questions

- Small sample size (n=7 per group) limits statistical power, particularly for the magazine approach analysis which was non-significant despite a numerically clear pattern
- The context extinction procedure was necessary to unmask devaluation effects but may have altered the nature of Pavlovian associations, complicating interpretation of magazine approach data
- It remains unknown whether the reinstatement of goal-directedness by IL inactivation applies to all routes to habit formation (e.g., pre-training reward exposure, ratio vs. interval schedule habits) or is specific to overtraining
- The connectivity between IL cortex and dorsolateral striatum is indirect (via accumbens shell and a proposed spiral from ventral to dorsal striatum); the precise circuit through which IL suppresses A-O control is not established
- Whether IL inactivation would be effective after even more extreme overtraining, or whether there is a point at which A-O associations are genuinely degraded, is not addressed

---

### Connections & keywords

**Key citations:**
- Adams (1982) — original demonstration of devaluation sensitivity as function of training extent
- Dickinson (1985) — foundational dual-process (A-O vs. S-R) theory of instrumental action
- Dickinson et al. (1995) — motivational control after extended training; contingency-based account of habit formation
- Killcross & Coutureau (2003) — prior lesion study establishing PL/IL double dissociation
- Balleine & Dickinson (1998) — cortical substrates of goal-directed action
- Yin, Knowlton & Balleine (2002) — dorsolateral striatum lesion produces analogous reinstatement of goal-directedness
- Everitt, Dickinson & Robbins (2001) — neuropsychological basis of addiction, habit dominance

**Named models or frameworks:**
- Dual-process theory of instrumental action (A-O vs. S-R)
- Specific-satiety devaluation paradigm
- Contention scheduling (Shallice, 1988)
- Variable interval (VI-60) schedule of reinforcement

**Brain regions:**
- Infralimbic (IL) medial prefrontal cortex
- Prelimbic (PL) medial prefrontal cortex
- Dorsolateral striatum
- Nucleus accumbens (shell and core)
- Basolateral amygdala

**Keywords:**
- habit formation, goal-directed behaviour, action-outcome associations, stimulus-response associations, reward devaluation, specific-satiety devaluation, muscimol inactivation, infralimbic cortex, medial prefrontal cortex, dual-process instrumental learning, behavioural autonomy, instrumental overtraining
