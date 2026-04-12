---
source_file: kashay2023_ACC_effort_decision.md
paper_id: kashay2023_ACC_effort_decision
title: "Neural activity in the anterior cingulate cortex is required for effort-based decision making"
authors:
  - "Adrienne Q. Kashay"
  - "Jovian Y. Cheung"
  - "Rahil N. Vaknalli"
  - "Molly J. Delaney"
  - "Michael B. Navarro Jr."
  - "Christabelle Junaidi"
  - "Faith Veenker"
  - "Morgan E. Neuwirth"
  - "Christopher J. Gabriel"
  - "Laura A. DeNardo"
  - "Scott A. Wilke"
year: 2023
journal: "bioRxiv (preprint)"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
  - rat
tasks:
  - open_field
  - t_maze
methods:
  - calcium_imaging
  - optogenetics
  - electrophysiology
  - computational_modeling
  - lesion
brain_regions:
  - anterior_cingulate_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
  - thalamus
  - mediodorsal_thalamus
  - amygdala
  - basolateral_amygdala
keywords:
  - anterior_cingulate_cortex
  - effort_based_decision_making
  - optogenetics
  - barrier_t_maze
  - action_selection
  - cost_benefit_tradeoff
  - action_value_encoding
  - goal_directed_behavior
  - movement_microstructure
  - excitatory_neuron_silencing
  - mouse_prefrontal_cortex
  - neuropsychiatric_disorders
  - neural
  - activity
  - anterior
  - cingulate
  - cortex
  - required
  - effort
  - based
key_citations:
  - gabriel2022_behaviordepot_detection
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

- **Validation**: Mice rapidly learned the barrier T-maze, adjusting choices based on effort-reward tradeoffs. When effort was equalized (both arms had barriers), mice switched to nearly 100% HR choices, demonstrating intact spatial memory and reward preference. Trial time differences between HR and LR choices diminished with training, indicating minimal time cost confound.

- **Acute necessity of ACC for EBD**: Optogenetic silencing of ACC excitatory neurons during choice trials robustly reduced preference for high-effort, high-reward choices (stGtACR2: ~75% HR light OFF vs. ~45% HR light ON; mCherry controls: no effect). The largest effects occurred when silencing was restricted to the choice period (start gate through choice point).

- **Temporal specificity**: Silencing during the ITI alone had no effect. Silencing during the start box (6s pre-trial wait) plus ITI reduced HR choices. Silencing during the choice period itself produced the strongest disruption. This indicates ACC activity is required during action selection and trial preparation, but not during rest.

- **Mechanism of disruption**: When effort was equalized (two barriers), silencing ACC no longer produced a persistent deficit — mice adjusted to choose the high-reward arm on both light OFF and ON trials (with initial perseveration toward formerly low-effort arm on light-ON trials). This demonstrates that silencing does not impair spatial memory, reward preference, or motor capacity. Instead, silencing biases mice toward low-effort choices by disrupting the evaluation/selection process.

- **Choice trajectory analysis**: Silencing ACC increased time in the approach zone, particularly for high-effort choices. DeepLabCut tracking revealed that silencing introduced frequent "micropauses" (>2 frames without progress toward goal) into the approach trajectory, chunking movements into discrete segments. Micropauses were rare in light OFF trials and primarily occurred in the approach zone during high-effort choices when ACC was silenced.

- **Specificity to goal-directed context**: Silencing ACC had no effect on overall mobility in open field (mean velocity unchanged) or on effortful struggling behavior in tail suspension test. This demonstrates that ACC is not required for general movement or effort production, but specifically for goal-directed effort-based decision making.

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
- Demonstrates that the deficit is specific to effortful cost-benefit evaluation: silencing has no effect when there is no effort cost or when effort is equalized, ruling out impairment in spatial memory, reward preference, or motor capacity. Instead, silencing biases mice toward low-effort choices by disrupting the evaluation/selection process.
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

The paper partially meets the bar for mechanistic insight. It presents an **algorithmic-level** account of ACC function in effort-based decision making, but does not provide direct **implementational-level** evidence linking specific circuit mechanisms to the algorithm.

**Computational level**: The ACC is proposed to solve the problem of integrating effort costs with reward benefits to compute action values that guide selection between alternative actions. The brain must decide whether to exert high effort for high reward or conserve energy for lower reward.

**Algorithmic level**: The paper proposes that ACC excitatory neurons encode action-value representations that integrate reward magnitude and effort cost. During decision making, ACC activity is required to: (1) maintain or retrieve action-value associations, (2) select high-effort actions when they have higher utility, and (3) support continuous goal-directed action sequences (preventing "micropauses" during approach). The findings suggest ACC provides top-down control over effort-averse selection systems, possibly in the striatum.

**Implementational level**: The paper does not provide direct evidence for specific biophysical or circuit mechanisms (e.g., specific cell types, synaptic plasticity rules, or connectivity patterns) that implement the algorithm. While the study uses cell-type-specific optogenetic manipulation (CaMKII promoter targeting excitatory neurons), it does not identify which specific projection targets or microcircuits within ACC are responsible for the observed effects. The authors explicitly note that future studies should investigate cell-type-specific circuits by targeting genetically encoded opsins to specific projection pathways.

---

### Limitations & open questions

- **No neural recordings**: The computations disrupted by silencing (value encoding, sequence tracking, online motor control) cannot be distinguished without simultaneous recording of ACC activity.
- **Incomplete cell-type specificity**: CaMKII promoter was used to target excitatory neurons, but this has incomplete specificity; contributions of inhibitory neurons cannot be fully excluded.
- **Projection-specific circuits not dissected**: Bilateral silencing affects broad excitatory populations; which specific output pathways (ACC→striatum, ACC→thalamus, ACC→amygdala) mediate the observed effects is unknown.
- **Start-box effect ambiguity**: The silencing effect during the start box could reflect either choice planning or a delay in re-establishing task representations after extended silencing.
- **Post-choice ACC function not tested**: Whether ACC is required during barrier climbing, outcome consumption, or inter-trial model updating was not systematically tested.
- **Biasing mechanism unclear**: Why silencing biases toward LR (rather than random choice) suggests striatal default effort-avoidance, but this was not directly tested.
- **Cell-type and projection-specific contributions**: Identified by the authors as a key future direction requiring targeted optogenetic approaches.

---

### Connections & keywords

**Key citations**:
- Walton et al. (2002, 2003) — foundational rat ACC lesion studies establishing ACC's role in barrier T-maze EBD
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
