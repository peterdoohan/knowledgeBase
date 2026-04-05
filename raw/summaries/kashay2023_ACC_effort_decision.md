---
source_file: kashay2023_acc_effort_decision.md
title: "Neural activity in the anterior cingulate cortex is required for effort-based decision making"
authors: Adrienne Q. Kashay, Jovian Y. Cheung, Rahil N. Vaknalli, Molly J. Delaney, Michael B. Navarro Jr., Christabelle Junaidi, Faith Veenker, Morgan E. Neuwirth, Christopher J. Gabriel, Laura A. DeNardo, Scott A. Wilke
year: 2023
journal: bioRxiv (preprint)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Optogenetic silencing of ACC excitatory neurons during action selection acutely and reversibly impairs mice's preference to exert greater effort for a larger reward in a barrier T-maze, without affecting general mobility or effortful behavior outside a goal-directed context.

---

### Background & motivation

Effort-based decision making (EBD) — weighing predicted gains against effort costs — is disrupted in depression, schizophrenia, addiction, and Parkinson's disease. The anterior cingulate cortex (ACC) has long been implicated in EBD via lesion and pharmacological studies in rats, but these approaches lack temporal precision and cell-type specificity, leaving open the question of when during a trial ACC activity is actually required. Furthermore, conflicting results across species (rat vs. mouse) and paradigms (barrier T-maze vs. operant lever-pressing) have not been resolved. This paper addresses those gaps by applying optogenetics with spatiotemporal precision in a newly validated mouse version of the barrier T-maze.

---

### Methods

- **Subject population**: C57BL/6J wildtype mice (12–18 weeks, both sexes); food-restricted to 80–85% ad libitum weight.
- **Task**: Custom mouse-scaled barrier T-maze. High-reward (HR) arm contained 3 pellets behind a 10 cm wire-mesh barrier; low-reward (LR) arm contained 1 pellet with no barrier. Mice trained to >70% HR choices before optogenetic testing.
- **Behavioral validation**: Reward differential (3:1, 2:1, 1:1) and effort cost (barrier present/absent in LR arm) were systematically manipulated to confirm sensitivity to effort-reward tradeoffs.
- **Optogenetics**: Bilateral AAV1-CaMKII-stGtACR2 (inhibitory opsin) or mCherry control injected into dorsal ACC (Cg1; AP +1.4, ML +/-0.35, DV -1.3 mm). Blue light (473 nm, 5 mW total, 2.5 mW/side) delivered via implanted fiber-optic cannulae. Light ON and OFF trials pseudorandomly interleaved (8 each per day).
- **Temporal manipulation windows**: ACC silenced during (a) ITI only, (b) start box + ITI, (c) trial (stem through choice point), or (d) start box through choice point. Across experiments, 3-day silencing blocks were also used.
- **Behavior tracking**: DeepLabCut (DLC) for markerless pose tracking; BehaviorDEPOT software for zone-based trajectory analysis; manual frame-by-frame analysis of micropauses.
- **Control tasks**: Open field (OF) for general locomotion; tail suspension test (TST) for non-goal-directed effortful behavior. Both conducted with ACC silencing.

---

### Key findings

- Bilateral optogenetic silencing of ACC excitatory neurons during the choice period (stem to choice point) robustly and significantly reduced HR choices on light-ON vs. light-OFF trials across multiple experiments.
- The largest effect was when silencing was restricted to the trial itself (choice period only); silencing during the ITI in the home cage had no effect.
- Silencing during the start box (pre-trial preparation period) also significantly impaired HR choices, suggesting ACC is required during choice planning as well as action selection.
- When effort was equalized (second barrier added to LR arm), silencing ACC no longer produced a persistent deficit — mice adjusted to choose the more rewarded arm on both light-ON and light-OFF trials (with a transient perseveration toward the formerly low-effort arm on light-ON trials on the first day).
- Before barrier introduction (no effort cost condition), silencing ACC had minimal effect on choice, indicating the deficit is specific to effort-based cost-benefit evaluation.
- ACC silencing increased time in the approach zone (pre-choice-point) on light-ON trials, particularly for HR choices; no significant effect was observed for LR choices.
- Silencing introduced frequent micropauses in the approach zone trajectory (occurring almost exclusively on light-ON HR-choice trials), disrupting the normally continuous ballistic movement toward the choice point; pause duration was not affected.
- ACC silencing had no effect on velocity in the open field, nor on effortful struggling in the tail suspension test — indicating effects are specific to goal-directed decision making.
- mCherry control mice showed no effect of laser stimulation in any condition.

---

### Computational framework

Not applicable in the sense that the paper does not develop or fit a formal computational model. However, the authors interpret their findings within existing frameworks:

- The results are consistent with action-value computation models in which ACC encodes the integrated value of actions (combining effort cost and reward magnitude), and this representation is necessary to override effort-averse default systems in the striatum (referencing Holroyd & McClure, 2015).
- The microstructure findings (micropauses during approach) are interpreted through the lens of online action sequence monitoring and control — a role for ACC in tracking progress toward a goal and maintaining continuity of ballistic goal-directed movements.
- The paper's framing is broadly compatible with top-down prefrontal control over subcortical systems, where ACC activity is required at specific temporal windows (trial preparation and action selection) to implement effort-based choices.

---

### Prevailing model of the system under study

Prior to this paper, the field's working model — grounded primarily in rat lesion and pharmacology studies — held that ACC (but not prelimbic or orbitofrontal cortex) is necessary for spatial EBD in the barrier T-maze. Electrophysiology in rats had further shown that ACC neurons encode choice value integrating effort cost and reward magnitude, and that population activity is temporally aligned with decision-relevant task events. However, because causal manipulations had relied on permanent lesions or slow-acting pharmacology, the precise temporal window during which ACC activity is required was unknown. It also remained unclear whether ACC's role was specifically in evaluating/selecting effortful actions or more generally in motivation or motor execution. Conflicting results in mice (one null result with medial PFC lesions) left cross-species generalizability open. The introduction explicitly frames the paper as resolving these temporal precision and species-translation gaps.

---

### What this paper contributes

- Establishes that ACC activity is causally and acutely required for effort-based action selection in mice, extending prior rat lesion work and resolving the cross-species conflict.
- Defines the temporal window of necessity: ACC is required during active choice preparation (start box) and action selection (stem to choice point), but not during the inter-trial interval in the home cage. The effect during choice execution was the largest observed.
- Demonstrates that the deficit is specific to effortful cost-benefit evaluation: silencing has no effect when there is no effort cost or when effort is equalized, ruling out impairment in spatial memory, reward preference, or capacity to exert effort.
- Reveals that ACC silencing disrupts the microstructure of goal-directed movement — introducing micropauses in the approach trajectory specifically on HR-choice trials — suggesting ACC supports online control of action sequences in a decision-making context, not just value computation.
- Shows that effects are context-specific: general mobility and non-goal-directed effortful behavior are unaffected, pointing to a role tied to goal-directed cognition rather than generalized motor or motivational function.

---

### Brain regions & systems

- **Anterior cingulate cortex (ACC / Cg1, dorsal subdivision)** — primary locus of investigation; excitatory neurons silenced optogenetically; proposed to encode action-value integrating effort cost and reward magnitude, and to exert online control over goal-directed action sequences during EBD.
- **Striatum (dorsal and ventral / nucleus accumbens)** — cited as downstream target of ACC projections; dopaminergic input to ventral striatum is well established in EBD; invoked as the site of effort-averse default action selection that ACC top-down control must override.
- **Basolateral amygdala** — cited from prior disconnection studies as part of the distributed circuit with ACC for EBD.
- **Mediodorsal thalamus** — noted as a major projection target of ACC excitatory neurons.
- **Anterior insula and lateral habenula** — cited as additional ACC-connected regions implicated in spatial EBD.

---

### Mechanistic insight

The paper meets criterion 1: it proposes an algorithm — that ACC excitatory neuron activity during action selection computes or retrieves effort-weighted action value representations necessary to override effort-averse default choices, and also supports online monitoring/control of goal-directed movement sequences.

However, it does not meet criterion 2: the paper records no neural activity from ACC or downstream targets during the task, so it cannot link specific algorithmic variables (e.g., value signals, sequence state representations) to measured neural activity. The silencing results establish necessity but cannot identify the specific computation being disrupted.

The paper therefore does not meet the full bar for mechanistic insight. It establishes a causal behavioral role for ACC excitatory neurons in effort-based choice with temporal precision and identifies a movement microstructure phenotype consistent with disrupted action sequence control, but the specific algorithmic mechanism (action-value representation vs. sequence monitoring vs. online motor control) cannot be disambiguated from the behavioral data alone.

---

### Limitations & open questions

- No neural recordings were made, so the computations disrupted by silencing (value encoding, sequence tracking, online motor control) cannot be distinguished.
- The inhibitory opsin (stGtACR2) was driven by CaMKII, which has incomplete specificity for excitatory neurons; contributions of inhibitory neurons cannot be fully excluded.
- Silencing is bilateral and affects a broad excitatory population; cell-type-specific projection circuits (e.g., ACC to dorsal striatum, BLA, or mediodorsal thalamus) are not dissected.
- The start-box silencing effect is ambiguous: it could reflect importance of ACC during choice planning, or a delay in re-establishing task-relevant representations after extended silencing.
- Effects of silencing during barrier climbing or outcome consumption were not systematically tested; whether ACC is required beyond the pre-choice period remains open.
- The mechanism by which ACC silencing biases mice toward the LR arm (rather than random choice) — consistent with striatal default effort-avoidance — is not directly tested.
- Cell-type-specific and projection-specific contributions are identified as a key future direction.

---

### Connections & keywords

**Key citations**:
- Walton et al. (2002, 2003) — foundational rat lesion studies establishing ACC's role in barrier T-maze EBD
- Rudebeck et al. (2006) — separate neural pathways for different decision costs
- Salamone & Cousins (1994, 1996) — original barrier T-maze task development; nucleus accumbens dopamine and EBD
- Hillman & Bilkey (2010, 2012) — electrophysiology showing ACC neurons encode cost-benefit and competitive effort in rats
- Cowen et al. (2012) — ACC neurons map anticipated effort and reward to action sequences
- Hart et al. (2020) — chemogenetics and calcium imaging in ACC for effort-based decisions in mice
- Holroyd & McClure (2015) — computational model of hierarchical ACC control over effortful behavior
- Gabriel et al. (2022) — BehaviorDEPOT software
- Mathis et al. (2018) — DeepLabCut pose tracking

**Named models or frameworks**:
- Barrier T-maze EBD task (Salamone et al.)
- BehaviorDEPOT (Gabriel et al., 2022)
- DeepLabCut (Mathis et al., 2018)
- stGtACR2 inhibitory opsin (soma-targeted GtACR2)
- Hierarchical ACC control model (Holroyd & McClure, 2015)

**Brain regions**:
- Anterior cingulate cortex (ACC / Cg1)
- Dorsal striatum
- Nucleus accumbens (ventral striatum)
- Basolateral amygdala
- Mediodorsal thalamus
- Anterior insula
- Lateral habenula

**Keywords**: anterior cingulate cortex, effort-based decision making, optogenetics, barrier T-maze, action selection, cost-benefit tradeoff, action-value encoding, goal-directed behavior, movement microstructure, excitatory neuron silencing, mouse prefrontal cortex, neuropsychiatric disorders
