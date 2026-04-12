---
source_file: redish2016_vicarious_trial_error.md
paper_id: redish2016_vicarious_trial_error
title: "Vicarious trial and error"
authors:
  - "A. David Redish"
year: 2016
journal: "Nature Reviews Neuroscience"
paper_type: review
contribution_type: review
species:
  - rat
tasks:
  - foraging_task
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - striatum
  - dorsomedial_striatum
  - dorsolateral_striatum
  - ventral_striatum
  - nucleus_accumbens
  - amygdala
keywords:
  - vicarious_trial_and_error
  - hippocampal_theta_sequences
  - deliberative_decision_making
  - episodic_future_thinking_mental_time_travel
  - cognitive_map
  - place_cells
  - ventral_striatum_reward_evaluation
  - task_bracketing
  - procedural_decision_making
  - hippocampal_prefrontal_coherence
  - dual_systems_decision_making
  - spatial_navigation
  - vicarious
  - trial
  - error
---

### One-line summary

Vicarious trial and error (VTE) — the pause-and-look behaviour of rats at maze choice points — reflects a deliberative decision-making process in which hippocampal theta sequences serially represent future path options, supported by convergent behavioural and neurophysiological evidence.

---

### Background & motivation

In the 1930s, Muenzinger, Gentry and Tolman observed that rats at maze choice points sometimes pause and look back and forth, and proposed that this behaviour (VTE) reflected prospective imagination of future options. This hypothesis fell out of favour because no mechanistic account existed, and the relevant computational and recording tools were unavailable. The 2007 discovery that hippocampal place-cell firing during VTE generates alternating forward representations of each path option revived the hypothesis. This review synthesises behavioural and neurophysiological evidence to argue that VTE is a genuine manifestation of deliberative decision making, with direct parallels to human episodic future thinking, working memory, and mental time travel.

---

### Methods

- **Scope**: Rodent literature on VTE, primarily from spatial tasks; primate and human parallels discussed where relevant.
- **Inclusion**: Studies of VTE behaviour and neurophysiology in rats, with emphasis on tasks where deliberative vs. procedural strategy can be distinguished (Tolman-Hull plus maze, multiple-T task, cued-T task, restaurant row, spatial delay-discounting task).
- **Synthesis**: Narrative review structured around (a) behavioural predictions derived from a deliberation hypothesis, (b) neurophysiological predictions, and (c) alternative theories that are evaluated and rejected.
- **Measurement of VTE**: Quantified using zIdPhi (integrated absolute angular velocity at the choice point), which distinguishes VTE laps (high reorientation) from non-VTE laps.

---

### Key findings

- VTE occurs when animals must use flexible, deliberative strategies (early learning, changing reward contingencies, difficult choices at threshold) and disappears as behaviour automates; this matches deliberation-hypothesis predictions.
- Hippocampal place-cell sequences during VTE project far ahead of the rat and alternate serially between the two path options within individual theta cycles, consistent with a search-and-evaluate process.
- Three stages of hippocampal sequence behaviour are described: (1) deliberation — sequences alternate between both goal options; (2) planning — sequences sweep only toward the chosen goal; (3) automation — sequences collapse to the animal's immediate location.
- Hippocampal lesions and cannabinoid agonists (CP55940) that disrupt theta sequences increase VTE; clonidine (which reduces noradrenaline) decreases VTE and limits hippocampal search to a single path.
- Covert reward signals in the ventral striatum precede the VTE turn-around point (pre-decision evaluation), while orbitofrontal cortex reward signals emerge only after the animal commits to a direction (post-decision expectation).
- Dorsolateral striatum does not show transient forward sweeps or covert reward signals during VTE; instead, it develops task-bracketing activity (start/end firing) as behaviour automates — the procedural system signature.
- VTE-like pause-and-reorient behaviour in primates (saccade-fixate-saccade) shows analogous hippocampal-dependent properties.

---

### Computational framework

The paper uses a **model-based / search-and-evaluate** framework, drawing on the theoretical distinction between two decision-making systems: deliberative (model-based) and procedural (model-free / cached action chains).

**Deliberation** is formalised as a serial search through a cognitive map (schema) in which potential future outcomes are mentally constructed, evaluated, and compared before action selection. Key components:
- A **schema** of world structure that supports forward prediction.
- A **search process** (identified with hippocampal theta sequences) that serially constructs individual episodic futures.
- An **evaluation process** (ventral striatum, OFC) that applies reward-value signals to imagined outcomes.

The framework assumes that imagination reactivates the same representational systems as perception (O'Craven & Kanwisher, 2000; Johnson et al., 2009) — enabling detection of mental time travel in non-human animals by decoding hippocampal population activity via an encoding-decoding-re-encoding loop (self-consistency measure).

The competing **procedural system** is formalised as situation-categorisation followed by release of cached action chains, implemented in the dorsolateral striatum.

---

### Prevailing model of the system under study

The paper's introduction situates VTE within a longstanding debate between two broad views of animal decision-making. The dominant mid-20th-century account (Hull) held that behaviour consists of stimulus-response chains: the animal recognises a situation and releases a well-learned action sequence. Under this view, VTE was an anomaly with no clear mechanistic status. The alternative Tolmanian view, largely dormant for decades, held that animals form cognitive maps and mentally search possible futures when making decisions. The paper frames the field as having recently revived the Tolmanian position, driven by hippocampal place-cell recordings, neural decoding methods, and the demonstration that imagination activates the same circuits as perception. By 2016, the dual-systems framework — deliberative (hippocampus/PFC) versus procedural (dorsal striatum) — had become the working model, but the mechanistic link between VTE behaviour and deliberation remained incompletely established.

---

### What this paper contributes

The review establishes VTE as a validated behavioural readout of deliberation in non-human animals, synthesising convergent evidence across behaviour, pharmacology, lesion studies, and neural ensemble recordings. It can now be said — rather than merely speculated — that:

1. The hippocampus supports a serial, forward-sweeping search through future path options during VTE, operating via theta sequences.
2. The ventral striatum provides pre-decision evaluative signals and the OFC provides post-decision expectation signals during VTE.
3. The dorsolateral striatum is the substrate of the procedural system and is disengaged during deliberation.
4. The transition from VTE to automation reflects a shift from hippocampal-PFC-driven deliberation to dorsolateral striatal task-bracketing.

Key unresolved questions identified are: how the search process selects which futures to construct; how options are ultimately evaluated and compared (integration-to-threshold vs. other models); and what neural mechanism ends deliberation and triggers action selection.

---

### Brain regions & systems

- **Hippocampus (dorsal)** — generates theta sequences that serially encode future path options during VTE; necessary for VTE expression; initiates the search component of deliberation.
- **Medial prefrontal cortex (prelimbic/infralimbic)** — proposed initiator of VTE; shows increased LFP coherence with hippocampus during VTE; necessary for flexible strategy switching.
- **Ventral striatum (nucleus accumbens)** — provides covert reward-evaluation signals prior to VTE decision point; encodes anticipated outcomes before the turn-around.
- **Orbitofrontal cortex (OFC)** — provides covert reward signals after the animal commits to a path; encodes outcome-specific reward expectations post-decision.
- **Dorsolateral striatum** — substrate of procedural decision making; develops task-bracketing (start/end firing) as behaviour automates; does not show VTE-related forward sweeps or covert reward signals.
- **Dorsomedial striatum** — may contribute to deliberative processes; specific roles incompletely understood.
- **Amygdala** — implicated in anxiety-related VTE variants (elevated plus maze stretch-attend posture); predicted to show hippocampal LFP coupling during VTE.

---

### Mechanistic insight

The paper meets the bar for mechanistic insight:

**Phenomenon**: At maze choice points, rats sometimes pause and reorient between alternatives (VTE); this correlates with flexible, deliberative decision-making and disappears upon automation.

**Computational level**: The brain is solving the problem of action selection under uncertainty in a world with a known schema. Rather than retrieving a cached action, it must predict the consequences of each available action and evaluate those consequences against current goals.

**Algorithmic level**: The hippocampus, operating in theta-frequency cycles (~140 ms), serially constructs self-consistent representations of future paths (theta sequences). Each theta cycle corresponds to one forward sweep toward one goal alternative. Alternatives are explored serially across cycles. Reward value of each imagined outcome is computed by the ventral striatum (pre-decision) and OFC (post-decision). The mPFC is proposed to issue requests to the hippocampus for successive searches; each theta sequence is a hippocampal response to one such request.

**Implementational level**: Hippocampal place cells fire phase-precessed within the theta LFP, generating compressed sequences representing paths forward of the rat. This phase relationship is disrupted by cannabinoid agonists (CP55940), which increase VTE — interpreted as failure of the hippocampus to produce a self-consistent imagined future, forcing additional search cycles. Clonidine (noradrenaline reduction) suppresses VTE by apparently collapsing search to a single path, possibly by driving the system into a planning rather than deliberation stage.

**Bonus (implementation)**: Noradrenergic modulation (clonidine), endocannabinoid modulation (CP55940), and hippocampal-prelimbic LFP theta coherence all point to specific neuromodulatory and connectivity mechanisms regulating the deliberative search process.

---

### Limitations & open questions

- How the search process selects which futures to construct (goal-cueing, priority signals) is unknown.
- The mechanism by which deliberation terminates and action is selected is not resolved; integration-to-threshold models have partial but not conclusive support from VTE data.
- Whether dorsal and ventral hippocampus encode unified or dissociable representations during VTE is unknown.
- The specific role of the dorsomedial striatum in deliberation remains incompletely explored.
- Whether task-bracketing disruption following automation reversal is directly caused by reinstated VTE (or occurs in parallel) is not fully characterised.
- The review focuses on spatial rodent tasks; generalisability to non-spatial domains and non-rodent species is inferred but not directly tested here.
- How the mPFC evaluates the quality of hippocampal representations to determine whether to issue another search request is unknown.

---

### Connections & keywords

**Key citations**:
- Johnson & Redish (2007, J. Neurosci.) — first demonstration that hippocampal sequences encode future path options during VTE.
- O'Keefe & Nadel (1978) — hippocampus as cognitive map.
- Foster & Wilson (2007, Hippocampus) — hippocampal theta sequences.
- Meer et al. (2010, Neuron) — triple dissociation of hippocampus, ventral striatum, and dorsolateral striatum on spatial decision task.
- Smith & Graybiel (2013, Neuron) — VTE negatively correlated with task-bracketing in dorsolateral striatum.
- Gupta et al. (2012, Nat. Neurosci.) — hippocampal theta sequences segment cognitive chunks and represent goals.
- Steiner & Redish (2014, Nat. Neurosci.) — neural correlates of regret and VTE on restaurant row task.
- Johnson et al. (2009, Trends Cogn. Sci.) — logic of identifying neural representations of mental time travel from neural signals.

**Named models or frameworks**:
- Vicarious trial and error (VTE)
- Cognitive map (Tolman)
- Dual-systems decision making (deliberative vs. procedural)
- Hippocampal theta sequences / hippocampal sweeps
- Task bracketing (dorsolateral striatum)
- zIdPhi (quantitative VTE measure)
- Self-consistency measure (encoding-decoding-re-encoding loop)
- Integration to threshold

**Brain regions**:
- Hippocampus (dorsal)
- Medial prefrontal cortex (prelimbic, infralimbic)
- Ventral striatum (nucleus accumbens)
- Orbitofrontal cortex
- Dorsolateral striatum
- Dorsomedial striatum
- Amygdala

**Keywords**:
- vicarious trial and error
- hippocampal theta sequences
- deliberative decision making
- episodic future thinking / mental time travel
- cognitive map
- place cells
- ventral striatum reward evaluation
- task bracketing
- procedural decision making
- hippocampal-prefrontal coherence
- dual-systems decision making
- spatial navigation
