---
source_file: corbit2018_goal_directed_habitual.md
title: "Understanding the balance between goal-directed and habitual behavioral control"
authors: Laura H. Corbit
year: 2018
journal: Current Opinion in Behavioral Sciences
paper_type: review
contribution_type: review
---

### One-line summary

This review synthesises animal research on the neural circuits and factors governing the balance between goal-directed and habitual behavioral control, with emphasis on pathological habits and their relevance to neuropsychiatric disorders.

---

### Background & motivation

Instrumental behavior can be governed by two dissociable systems: a goal-directed system sensitive to action-outcome contingencies and outcome value, and a habit system driven by stimulus-response (S-R) associations that is insensitive to outcome value. Early S-R accounts of instrumental learning could not explain behavioral flexibility, prompting a dual-system framework. Understanding how these systems interact is critical for explaining failures of behavioral control in addiction, OCD, and other disorders where pathological habits emerge. This review addresses the gap between well-established anatomy of the two systems and the poorly understood mechanisms by which they interact and compete dynamically.

---

### Methods

- **Scope**: Animal (rodent) behavioral neuroscience literature on habit learning; brief coverage of human parallels and neuropsychiatric disorder studies.
- **Inclusion**: Empirical studies using outcome devaluation, maze paradigms, electrophysiology, lesions, chemogenetics, and optogenetics to investigate goal-directed vs. habitual control.
- **Synthesis method**: Narrative review organized around paradigms, neural substrates, modulatory factors, and open questions.
- **Key paradigms covered**: Outcome devaluation (free-operant lever press), plus/T-maze response vs. place strategies, context-specific reinforcement schedule procedures (ratio vs. interval).

---

### Key findings

- Goal-directed actions depend on encoded action-outcome contingencies and current outcome value; habits rely on S-R associations and are insensitive to outcome devaluation.
- Extended ("over") training and lean variable-interval reinforcement schedules reliably shift control from goal-directed to habitual.
- Parallel corticostriatal circuits underlie the two systems: dorsomedial striatum (DMS) + medial prefrontal cortex for goal-directed control; dorsolateral striatum (DLS) + sensorimotor cortex (and infralimbic cortex) for habits.
- Inactivation of DLS after habitual responding is established restores goal-directed control, indicating competitive interaction between circuits.
- DLS neurons develop a "task-bracketing" (chunking) firing pattern early in training that persists through overtraining and is unaffected by devaluation; DMS activity peaks during choice and then decreases with overtraining.
- Orbitofrontal cortex (OFC) projections to dorsal striatum are necessary for goal-directed control; cannabinoid CB1 receptor signaling in the OFC-DS pathway gates habit formation.
- Drug exposure (alcohol, cocaine, amphetamine, methamphetamine, nicotine), chronic stress, and high-sugar/palatable diets all accelerate habit formation.
- Alcohol promotes habitual control partly via disinhibition of DLS medium spiny neurons (reduced GABAergic transmission, down-regulation of CB1-dependent LTD).
- Habitual over-reliance has been documented across many neuropsychiatric disorders: schizophrenia, OCD, alcoholism, cocaine dependence, social anxiety, autism, Tourette syndrome, obesity.
- Contexts paired with potent rewards (drugs, junk food) can acutely induce habitual responding in otherwise goal-directed animals, suggesting a Pavlovian-to-instrumental transfer-like mechanism.

---

### Computational framework

The paper does not adopt a formal computational framework but implicitly operates within the reinforcement learning (RL) dual-system framework. The goal-directed system corresponds loosely to model-based RL (prospective evaluation of action-outcome-value chains), while the habit system corresponds to model-free RL (cached S-R values updated by prediction errors without explicit outcome representation).

Key implicit constructs:
- **Goal-directed**: action selected by integrating contingency (P(outcome|action)) and current outcome value (incentive value).
- **Habitual**: response elicited by antecedent stimuli through strengthened S-R weights; insensitive to outcome revaluation.
- Competition between DMS and DLS circuits implements a form of arbitration between model-based and model-free controllers.

The paper does not formalise these computations mathematically but references empirical markers (devaluation sensitivity) that operationalise the distinction.

---

### Prevailing model of the system under study

The field's baseline view, as framed in the introduction, is a dual-process corticostriatal account. Goal-directed actions and habits are controlled by parallel circuits centred on DMS and DLS, respectively. Goal-directed control dominates early in training and under ratio schedules; habitual control emerges with overtraining or interval schedules. The model posits that these circuits can compete, and that the balance between them determines behavioral flexibility. Neural inactivation experiments established a causal role for each region. However, the precise mechanisms by which the two circuits interact under normal and pathological conditions—and why diverse insults (drugs, stress, diet) all shift the balance toward habits—remained poorly understood at the time of publication.

---

### What this paper contributes

This review consolidates evidence across several emerging lines of work that were extending the classical DMS/DLS dichotomy:

1. **OFC-DS pathway**: Identifies OFC projections to dorsal striatum as a necessary contributor to goal-directed control, with CB1 receptor signaling in this pathway gating habit formation—adding a prefrontal modulatory circuit beyond the canonical mPFC role.
2. **Chunking and sequence learning**: Links DLS task-bracketing activity to action sequence formation, providing a mechanistic account of how habits become outcome-insensitive (individual actions within a sequence are driven by prior actions, not outcome value).
3. **Pathological habits**: Systematically catalogues conditions that accelerate habit learning and begins connecting synaptic mechanisms (DLS disinhibition by alcohol, glutamate receptor changes by methamphetamine) to behavioral shifts.
4. **Context as a determinant of control**: Highlights that context can selectively engage goal-directed or habitual systems and that drug-paired contexts can acutely produce habitual responding even without prior S-R training in that context, pointing to a non-S-R mechanism.
5. **Clinical translation**: Provides a framework for understanding habit-based impairments across neuropsychiatric disorders, emphasising the importance of distinguishing direct habit-system strengthening from goal-directed system impairment.

---

### Brain regions & systems

- **Dorsolateral striatum (DLS)** — primary neural substrate of habit learning; shows task-bracketing activity; disinhibited by alcohol; CB1 receptors here modulate habit formation.
- **Dorsomedial striatum (DMS)** — primary substrate of goal-directed action; activity peaks during choice, decreases with overtraining; lesion or inactivation causes premature habit emergence.
- **Medial prefrontal cortex (mPFC)** — provides input to DMS supporting goal-directed control.
- **Infralimbic cortex (IL)** — contributes to habitual control; inactivation restores goal-directed responding in overtrained animals.
- **Orbitofrontal cortex (OFC)** — projects to dorsal striatum; necessary for expression of goal-directed control; CB1 receptor deletion in OFC-DS projection prevents habit expression.
- **Sensorimotor cortex** — provides input to DLS, supporting S-R habit circuitry.
- **Hippocampus** — referenced in maze learning context for place vs. response strategy (lidocaine inactivation studies).

---

### Mechanistic insight

The paper does not meet the full bar: it is a review that synthesises existing findings rather than presenting a single algorithm tested against neural data. Several cited studies individually approach mechanistic accounts—for example, Patton et al. (2016) links alcohol-induced DLS disinhibition to habitual control, and Gremel et al. (2016) uses chemogenetics to show OFC-DS activity is necessary for goal-directed control—but the review itself does not provide a unified mechanistic account backed by neural data from a single study.

At the level the review reaches:
- **Computational**: The brain must arbitrate between a fast, efficient S-R system and a flexible, outcome-sensitive system; this arbitration must be sensitive to training history and environmental context.
- **Algorithmic**: DLS chunking/bracketing activity encodes action sequences that become outcome-insensitive; DMS activity encodes outcome-contingent choice. Competition between the two systems (potentially mediated by striatal interneurons, theta-band oscillations, and OFC inputs) determines which controls behavior.
- **Implementational**: CB1-dependent LTD in DLS, reduced GABAergic inhibition of DLS MSNs (by alcohol), glutamate receptor changes (by methamphetamine), cholinergic interneuron function, and OFC glutamatergic inputs are all implicated, but a coherent biophysical model integrating these elements does not yet exist.

---

### Limitations & open questions

- The stimuli that support S-R associations in free-operant paradigms are poorly defined; contextual cues are likely only one component, and the magnitude of context-shift effects does not scale with training as an S-R account would predict.
- Residual responding after effective devaluation is acknowledged but not fully explained; it may reflect an S-R component but its determinants are unclear.
- It is unresolved whether pathological habits (from drugs, stress, diet) arise from direct strengthening of the habit system, impairment of the goal-directed system, or both.
- Whether different insults (alcohol vs. cocaine vs. stress) act through common or distinct neural mechanisms is unknown.
- Recovery of goal-directed control after removal of drug/stress is poorly characterized.
- How the DMS and DLS circuits interact dynamically under normal conditions to allow flexible shifting between behavioral control modes remains largely unresolved.
- Human generalisability: the review focuses primarily on rodent data; the degree to which findings translate to human habit formation is noted but not extensively addressed.

---

### Connections & keywords

**Key citations**:
- Dickinson (1985) — foundational dual-system (goal-directed vs. habit) framework
- Balleine & Dickinson (1998) — goal-directed action, contingency and incentive learning
- Balleine & O'Doherty (2010) — corticostriatal determinants of goal-directed and habitual action
- Yin, Knowlton & Balleine (2004) — DLS lesions and habit formation
- Jog et al. / Graybiel (1999, 2013) — task-bracketing/chunking activity in DLS
- Killcross & Coutureau (2003) — infralimbic cortex and habit expression
- Gremel et al. (2016) — OFC-DS projection, CB1 receptors, goal-directed vs. habitual gating
- Patton et al. (2016) — ethanol disinhibition of DLS MSNs
- Gillan et al. (2016) — transdiagnostic framework for goal-directed deficits

**Named models or frameworks**:
- Outcome devaluation task (standard behavioral assay)
- Plus/T-maze place vs. response strategy paradigm
- Dual-process corticostriatal model (DMS goal-directed / DLS habitual)
- Model-based vs. model-free reinforcement learning (implicit framework)
- Two-step task (referenced in clinical disorder literature)

**Brain regions**:
- Dorsolateral striatum (DLS)
- Dorsomedial striatum (DMS)
- Medial prefrontal cortex (mPFC)
- Infralimbic cortex (IL)
- Orbitofrontal cortex (OFC)
- Sensorimotor cortex
- Hippocampus

**Keywords**:
- goal-directed action
- habit learning
- outcome devaluation
- dorsolateral striatum
- dorsomedial striatum
- corticostriatal circuits
- action-outcome contingency
- stimulus-response learning
- task-bracketing / chunking
- CB1 endocannabinoid signaling
- pathological habits
- neuropsychiatric disorders
