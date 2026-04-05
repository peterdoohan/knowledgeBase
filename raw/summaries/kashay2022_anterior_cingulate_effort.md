---
source_file: kashay2022_anterior_cingulate_effort.md
title: "Neural activity in the anterior cingulate cortex is required for effort-based decision making"
authors: Adrienne Q. Kashay, Jovian Y. Cheung, Rahil N. Vaknalli, Molly J. Delaney, Michael B. Navarro Jr., Christabelle Junaidi, Faith Veenker, Morgan E. Neuwirth, Christopher J. Gabriel, Laura A. DeNardo, Scott A. Wilke
year: 2022
journal: bioRxiv (preprint; doi: 10.1101/2022.03.22.485350; this version posted January 3, 2023)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Bilateral optogenetic silencing of ACC excitatory neurons during action selection rapidly and reversibly impairs mice's preference to exert greater physical effort for a larger reward in a barrier T-maze task, establishing a causal, temporally precise role for ACC activity in effort-based decision making.

---

### Background & motivation

Effort-based decision making (EBD) — choosing actions by weighing predicted gains against effort costs — is impaired in depression, schizophrenia, addiction, and Parkinson's disease. The anterior cingulate cortex (ACC) is consistently implicated in evaluating physical and cognitive effort costs, and lesion/pharmacology studies in rats link ACC to spatial EBD performance. However, prior work lacked temporal precision, preventing identification of *when* during a trial ACC is required, and used lesions that cannot isolate cell-type-specific contributions. The paper fills this gap by applying optogenetics in a newly validated mouse version of the barrier T-maze to establish the causal and temporally precise necessity of ACC excitatory neurons for effortful choice.

---

### Methods

- **Species and subjects**: C57BL/6J wildtype mice (12–18 weeks, either sex), food deprived to 80–85% _ad libitum_ weight.
- **Task**: Custom mouse-scaled barrier T-maze; high-reward (HR) arm: 3 pellets + 10 cm wire-mesh barrier; low-reward (LR) arm: 1 pellet, no barrier. Training criterion: >70% HR choices on 2 consecutive days.
- **Task validation**: Reward differential (3:1, 2:1, 1:1) and effort (second barrier in LR arm) were systematically manipulated in wildtype mice to verify sensitivity.
- **Optogenetics**: Bilateral stereotaxic injection of AAV1-CKIIa-stGtACR2-FusionRed (inhibitory soma-targeted anion channelrhodopsin) or mCherry control into ACC (Cg1; AP +1.4, ML ±0.35, DV -1.3 mm). Blue laser (473 nm, 5 mW total, 2.5 mW/side) delivered via implanted fibre cannulae.
- **Temporal dissection of silencing**: Light delivered pseudorandomly (light OFF vs. ON, 8 trials each) during one of several trial phases: (i) home cage ITI; (ii) start box; (iii) start box through choice point (trial); (iv) ITI + start box.
- **Choice trajectory analysis**: DeepLabCut keypoint tracking combined with custom BehaviorDEPOT software to quantify time in maze zones (approach, choice) and microstructure of ballistic movements (micropauses defined as >2 frames without forward progress).
- **Control assays**: Open field (OF; velocity) and tail suspension test (TST; struggling time) with the same optogenetic manipulation to assess generalized motor and effort effects.
- **Statistics**: Non-parametric tests or ANOVA; error bars ±SEM; within-subject light OFF vs. ON comparisons.

---

### Key findings

- Mice reliably learned the barrier T-maze, choosing the HR arm ~80% of trials when trained; choices scaled with reward differential and were sensitive to equalization of effort cost.
- At asymptotic performance, HR and LR trial durations were not significantly different, confirming minimal time-cost confound for climbing the barrier.
- Bilateral optogenetic silencing of ACC excitatory neurons significantly reduced HR (high effort) choices vs. light OFF trials; the largest effect occurred when silencing was restricted to the choice phase itself (start gate through choice point).
- Silencing during the start box (pre-trial preparation) also impaired HR choices; silencing confined to the home cage ITI had no effect.
- When a second barrier was added to equalize effort, mice initially persisted in choosing the formerly LR arm under silencing but quickly adjusted to select the more rewarded arm on both light OFF and ON trials, ruling out impaired spatial memory, capacity to climb, or reward preference as explanations.
- In a 3-day block design, ACC silencing during trials produced a stable, large disruption of high-effort choices when a barrier was present, but minimal effect in the no-barrier condition.
- ACC silencing significantly increased time in the approach zone (pre-choice-point) on HR trials, introducing frequent micropauses into otherwise ballistic trajectories; no effect on approach time for LR choices.
- Micropauses in the approach zone were nearly absent on light OFF trials but common on light ON trials, specifically for HR choices.
- ACC silencing did not reduce struggling in the TST or alter average velocity in an open field, indicating effects are specific to goal-directed decision-making contexts.

---

### Computational framework

Not applicable in the sense that the paper presents no formal computational model. However, the discussion explicitly invokes computational framing: the authors interpret their results as consistent with models (e.g., Holroyd & McClure, 2015) proposing that top-down ACC control is necessary to override effort-averse, low-cost action selection systems in the striatum. Within this framing, ACC computes or maintains action-value representations that integrate effort cost and reward magnitude, and this signal is required to bias choice away from the default low-effort option. The paper's results specifically constrain when such a signal is causally necessary (during pre-choice preparation and action selection, not during general effort exertion or unconstrained locomotion).

---

### Prevailing model of the system under study

Based on the paper's introduction, the field's working model at the time was as follows: ACC is a prefrontal region necessary for evaluating the value of effortful actions — encoding effort costs, reward magnitudes, and their integration to guide action selection. Lesion and pharmacology studies in rats established that ACC, but not prelimbic or orbitofrontal cortex, is required for spatial EBD in the barrier T-maze. Electrophysiological recordings showed ACC neurons encode effort-related value and choice options with highest utility. However, the causal role of ACC in mice was contested (one null result in mice), and the temporal specificity of ACC's contribution was unknown: it was not clear whether ACC was required during planning/preparation, action selection, effort exertion, or outcome evaluation. Furthermore, whether the relevant contribution was cell-type-specific (excitatory vs. inhibitory neurons) was unresolved. There was also a broader theoretical debate about ACC's primary function (conflict monitoring, value of cognitive control, action-value comparison), with all accounts consistent with an effort-related role but none directly tested with the temporal precision used here.

---

### What this paper contributes

The paper provides the first temporally precise, optogenetic demonstration that ACC excitatory neuron activity is causally required for effort-based action selection in mice, resolving the conflicting lesion literature across species. Key advances:

- Establishes a validated mouse barrier T-maze protocol, enabling use of genetic tools in this species.
- Demonstrates that ACC necessity is temporally specific: most critical during choice preparation (start box) and action selection (start gate to choice point), not during the ITI when decision demands are absent.
- Shows the effect is limited to contexts where effort costs must be weighed against reward — absent when effort is equalized or when mice are tested outside a decision-making context (OF, TST).
- Reveals that ACC silencing disrupts the kinematic microstructure of goal-directed trajectories (introducing micropauses specifically before high-effort choices), suggesting ACC supports online, continuous control of ballistic goal-directed movements during effortful action selection, not merely a single-point valuation signal.
- These results are consistent with ACC exerting top-down override of effort-averse striatal systems, and with ACC's role in maintaining/monitoring progress through goal-directed action sequences.

---

### Brain regions & systems

- **Anterior cingulate cortex (ACC / Cg1, dorsal)** — primary focus; causal locus of effort-based decision making; excitatory neurons required for evaluating and selecting high-effort actions and for maintaining smooth, ballistic goal-directed approach trajectories.
- **Prelimbic cortex** — mentioned as not required for spatial EBD (prior lesion work), contextualizing ACC specificity.
- **Orbitofrontal cortex** — mentioned as not required for spatial EBD (prior lesion work).
- **Dorsal striatum** — mentioned as a major downstream ACC target; implicated in effort-averse action selection that ACC may override.
- **Nucleus accumbens / ventral striatum** — mentioned in the context of dopaminergic modulation of EBD and ACC-striatum disconnection effects.
- **Basolateral amygdala** — ACC-BLA disconnection disrupts EBD (prior lesion work).
- **Mediodorsal thalamus** — dense ACC projection target mentioned as relevant circuit node.
- **Habenula and anterior insula** — mentioned as implicated in spatial EBD by other studies.

---

### Mechanistic insight

The paper meets criterion 1 (it proposes an algorithmic account — ACC activity provides action-value signals integrating effort cost and reward magnitude, required to select high-effort choices over a low-effort default) and partially meets criterion 2 (it provides causal neural manipulation data — optogenetic silencing — that directly support this account). However, it does not include recordings that link specific model variables (e.g., value signals, prediction errors) to measured neural activity during the task; the evidence is loss-of-function only.

At the **computational level**: the problem is evaluating effort-reward tradeoffs to select the utility-maximising action when a low-effort, lower-reward alternative is available. The brain must compute or retrieve the expected value of exerting effort and use this to bias choice.

At the **algorithmic level**: ACC excitatory neurons appear to maintain or compute action-value representations that integrate effort cost with reward, and to provide online monitoring/control of goal-directed action sequences. Loss of this signal during approach shifts mice to default low-effort choices and disrupts the continuous, ballistic movement trajectory to the choice point. The pre-trial preparation phase (start box) is also critical, suggesting ACC activity builds up in anticipation of choice before movement begins.

At the **implementational level**: The paper identifies the relevant cell type as CaMKII-positive (excitatory) neurons in dorsal ACC (Cg1) and uses bilateral fibre optics, but does not resolve specific projection targets, layer identity, or the circuit mechanisms by which ACC normally biases striatal action selection. The authors note that ACC projects densely to dorsal striatum and mediodorsal thalamus, and that ACC-BLA and ACC-ventral striatum disconnections disrupt EBD, but this circuit-level implementation is not directly tested here.

---

### Limitations & open questions

- CaMKII promoter targets excitatory neurons but is not perfectly cell-type-specific; contributions of inhibitory neurons are not assessed.
- Optogenetic silencing with stGtACR2 is somatic but light spread means a broader region of dorsal ACC is affected; cell-type-specific projection targeting is not achieved.
- The paper does not record neural activity during the task, so specific computations attributed to ACC (value encoding, action sequence monitoring) are inferred from behaviour, not directly observed.
- The role of ACC in carrying out or completing effort (after choice but before reward) is not fully tested; the current silencing is restricted to pre-choice periods.
- The transition dynamics when effort is equalized show initial perseveration of LR choices under silencing — whether this reflects impaired model updating or impaired translation of updated models into action is unresolved.
- Circuit targets mediating ACC's influence on effort-based choice (dorsal striatum, BLA, thalamus, insula, habenula) are not dissected.
- Mouse vs. rat differences in ACC function for EBD are partially clarified but not fully resolved; the mouse ACC null result from prior work (Solinsky & Kirby 2013) used lesions, not optogenetics.
- Whether findings generalise beyond physical/spatial effort (e.g., cognitive effort) is not tested in this study.

---

### Connections & keywords

**Key citations**:
- Walton et al. (2002, 2003) — rat lesion studies establishing ACC necessity for spatial EBD in barrier T-maze
- Salamone & Cousins (1994, 1996) — original barrier T-maze cost/benefit paradigm
- Hillman & Bilkey (2010, 2012) — electrophysiological recordings of ACC cost-benefit encoding in rats
- Holroyd & McClure (2015) — computational model of hierarchical ACC control over effortful behavior
- Hart et al. (2020) — chemogenetics + calcium imaging in ACC during effortful decisions in mice
- Mathis et al. (2018) — DeepLabCut markerless pose estimation
- Gabriel et al. (2022) — BehaviorDEPOT automated behavioural detection
- Akam et al. (2021) — ACC predicts future states to mediate model-based action selection
- Tervo et al. (2021) — ACC directs exploration of alternative strategies

**Named models or frameworks**:
- Barrier T-maze EBD task (Salamone et al.)
- stGtACR2 optogenetic inhibitory opsin (somatic targeted)
- DeepLabCut (DLC) keypoint tracking
- BehaviorDEPOT behavioural analysis software
- Holroyd & McClure (2015) hierarchical control model

**Brain regions**:
- Anterior cingulate cortex (ACC / Cg1)
- Prelimbic cortex
- Orbitofrontal cortex
- Dorsal striatum
- Nucleus accumbens
- Basolateral amygdala
- Mediodorsal thalamus
- Anterior insula
- Lateral habenula

**Keywords**:
- effort-based decision making
- anterior cingulate cortex
- optogenetics
- barrier T-maze
- action selection
- cost-benefit evaluation
- goal-directed behavior
- choice trajectory microstructure
- excitatory neuron silencing
- mouse prefrontal cortex
- ballistic movement control
- neuropsychiatric disorders motivation
