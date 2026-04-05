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

Optogenetic silencing of ACC excitatory neurons during or immediately before action selection causally disrupts mice's preference to exert greater effort for larger reward in a barrier T-maze, without impairing general movement or effort outside a decision context.

---

### Background & motivation

Effort-based decision making (EBD) — weighing predicted gains against effort costs — is disrupted in depression, schizophrenia, addiction, and Parkinson's disease, making its neural substrates clinically important. The ACC has been repeatedly implicated in spatial EBD using lesion and pharmacological approaches in rats, but these methods lack the temporal precision needed to determine when during a trial ACC is required, and cannot address cell-type specific contributions. A validated mouse T-maze EBD paradigm compatible with modern genetic tools was also lacking, limiting translational studies.

---

### Methods

- **Subject population**: Adult C57BL/6J mice (both sexes, 12–18 weeks), food restricted to 80–85% ad libitum weight.
- **Task design**: Custom-built scaled-down barrier T-maze; one arm high reward (3 pellets, 10 cm wire mesh barrier) vs. low reward (1 pellet, no barrier). Mice trained to >70% high-reward (HR) arm choice over ~5–10 days of barrier training. Reward differential and barrier presence were systematically varied for validation.
- **Optogenetics**: Bilateral AAV1-CKIIa-stGtACR2-FusionRed (inhibitory opsin) injected into ACC (Cg1 region; AP +1.4, ML ±0.35, DV −1.3 mm). Blue laser (473 nm, 5 mW total) delivered via implanted fiber optic cannulae at spatiotemporally precise trial phases. mCherry-only mice served as controls. Silencing applied during: ITI, start box, choice approach zone (stem + choice point), or post-choice/non-decision contexts.
- **Trajectory analysis**: DeepLabCut keypoint tracking combined with custom BehaviorDEPOT software for zone-based automated analysis of time in approach vs. choice zones; frame-by-frame manual analysis of micropauses.
- **Control assays**: Open field (OF) locomotion and tail suspension test (TST) performed with identical optogenetic protocols to assess generalized motor or effort effects.
- **Analysis**: Nonparametric tests and ANOVA; within-subject comparisons of pseudorandomly interleaved light-OFF vs. light-ON trials.

---

### Key findings

- Bilateral optogenetic silencing of ACC excitatory neurons during the choice phase (from start gate lift through choice point) robustly reduced HR choices (high effort, high reward) in favour of the low effort alternative on a trial-by-trial basis.
- The largest effect was observed when silencing was restricted to the choice approach period alone; silencing during the start box (trial preparation) also disrupted EBD, but silencing only during the home-cage ITI did not.
- When effort was equalised (second barrier added to LR arm), silencing-induced bias toward the LR arm resolved within one day, demonstrating that spatial memory, ability to climb, and reward preference were intact.
- Silencing ACC in the no-barrier training condition had minimal effect, confirming the effect is specific to effort-cost contexts.
- ACC silencing increased time in the approach zone specifically for HR trials (mice were slower approaching the choice point before high-effort choices) but not for LR trials.
- Micropauses — brief interruptions in otherwise ballistic movement toward the choice point — were significantly more frequent in the approach zone during light-ON trials, exclusively on trials ending in HR choices.
- Silencing ACC had no effect on overall velocity in the open field or on effortful struggling in the tail suspension test, confirming the effects are specific to goal-directed decision contexts.

---

### Computational framework

Not applicable as a formal computational framework. The paper is primarily causal-empirical. However, the discussion invokes computational models of ACC as a top-down controller that overrides effort-averse action selection in the striatum (citing models by Vassena and others). The implicit framing is that ACC computes action-value associations integrating effort cost and reward magnitude, and exerts online control over goal-directed action sequences. The results constrain reinforcement learning models of effort-based choice by establishing that ACC activity is necessary at the time of action selection (and preparation), not merely for outcome learning.

---

### Prevailing model of the system under study

The introduction presents ACC as a prefrontal region consistently implicated in evaluating cognitive and physical effort costs, supported by lesion and pharmacology studies in rats using the barrier T-maze (Walton et al. 2003; Rudebeck et al. 2006; Schweimer & Hauber 2005). ACC neurons encode effort-related value in electrophysiology studies (Hillman & Bilkey 2010, 2012; Cowen et al. 2012), and the region is associated with computing reward value, tracking outcomes, and model-based action selection. The prevailing view was that ACC is necessary for EBD, but because prior interventions used lesions and pharmacology, it was unknown (1) when during a trial ACC is required, (2) whether excitatory neurons specifically mediate the effect, and (3) how ACC disruption affects the fine structure of action sequences — as opposed to gross choice preference.

---

### What this paper contributes

The paper establishes, for the first time with temporal precision, that ACC excitatory neuron activity is causally required specifically during the action selection and preparation phase of EBD — not during effort execution or between-trial periods. This resolves ambiguity left by lesion/pharmacology work and defines a temporally specific window (approach to choice point; trial preparation in start box) during which ACC is necessary. The trajectory analyses further reveal that ACC supports the continuity of goal-directed movement (suppresses micropauses) specifically when mice are planning high-effort choices, suggesting a role in online control of goal-directed action sequences rather than purely choice preference. The finding that effort and movement are unimpaired outside a decision context places ACC's role squarely in the computation/selection of effortful actions when alternatives exist, not in general motor output or effort generation.

---

### Brain regions & systems

- **Anterior cingulate cortex (ACC / Cg1)** — primary focus; dorsal, anterior subdivision. Required for evaluating and selecting effortful actions; mediates online control over goal-directed movement microstructure during decision making.
- **Prelimbic cortex** — noted in introduction as not required for spatial EBD (contrasting with ACC; Walton et al. 2003).
- **Orbitofrontal cortex** — noted as not required for spatial EBD.
- **Dorsal striatum** — discussed as downstream target of ACC projections; proposed site of effort-averse action selection that ACC overrides.
- **Mediodorsal thalamus** — noted as a dense ACC projection target; implicated in the circuit but not directly studied.
- **Basolateral amygdala** — discussed as ACC target whose disconnection disrupts EBD (Floresco & Ghods-Sharifi 2007).
- **Ventral striatum / nucleus accumbens** — dopaminergic inputs implicated in EBD; ACC projections relevant.
- **Habenula and anterior insula** — mentioned as additional ACC targets implicated in spatial EBD.

---

### Mechanistic insight

The paper meets criterion 1 (it proposes an algorithm: ACC computes effort-related action values and exerts online control to initiate and maintain goal-directed action sequences) and partially meets criterion 2 (it provides optogenetic causal evidence linking ACC excitatory neuron activity to specific trial phases and movement microstructure). However, it does not record neural activity during the task, so it cannot directly map specific model variables (e.g., value signals, prediction errors) onto measured neural activity. There is no claim about specific cell types beyond the use of a CaMKII promoter (targeting excitatory neurons broadly) and no data on downstream circuit implementation.

- **Computational**: The brain solves the problem of selecting an action with high effort cost when a lower-cost alternative is available; ACC represents action-value integrating effort cost and reward magnitude and must override default effort-averse tendencies.
- **Algorithmic**: ACC activity during the preparation and approach phase organises ballistic movement sequences and supports continuous goal-directed action selection; silencing disrupts both the choice itself and the kinematic microstructure (introduces micropauses), suggesting ACC monitors progress toward the goal in real time.
- **Implementational**: Excitatory neurons in dorsal ACC (Cg1) are required; projections to dorsal striatum and mediodorsal thalamus are proposed downstream effectors, but no recording or circuit-dissection data are provided in this study.

---

### Limitations & open questions

- The study used an inhibitory opsin under a CaMKII promoter, which broadly silences excitatory neurons — it cannot distinguish contributions of distinct ACC projection neuron subtypes or excitatory-inhibitory circuit dynamics.
- The effect of silencing during the start box (pre-trial period) raises the possibility of a delayed re-establishment of task-relevant ACC representations rather than purely a preparatory planning function; the study cannot disambiguate these accounts.
- Only excitatory neurons were targeted; inhibitory interneuron contributions and the balance of excitation/inhibition in ACC during EBD are not addressed.
- Downstream circuit targets (striatum, thalamus, amygdala) were not manipulated in this study, so the circuitry through which ACC effects on EBD are realised remains open.
- The paper uses a preprint version and was not peer-reviewed at time of posting.
- The mouse version of the barrier T-maze may differ behaviourally from the well-established rat paradigm in ways not fully characterised.
- The study does not record neural activity during the task, so it cannot specify what computation is disrupted at the level of individual neurons or ensembles.

---

### Connections & keywords

**Key citations**:
- Walton et al. (2003) — ACC lesions and spatial EBD in rats (Journal of Neuroscience)
- Rudebeck et al. (2006) — Separate neural pathways for decision costs (Nature Neuroscience)
- Floresco & Ghods-Sharifi (2007) — Amygdala-PFC circuitry and EBD (Cerebral Cortex)
- Hillman & Bilkey (2010, 2012) — ACC neurons encoding cost-benefit in rats
- Cowen et al. (2012) — ACC neurons mapping anticipated effort to action sequences
- Kolling et al. (2016) — Value, search, and persistence in ACC (Nature Neuroscience)
- Gabriel et al. (2022) / BehaviorDEPOT — open-source behavior analysis software
- Mathis et al. (DeepLabCut) — keypoint tracking neural network

**Named models or frameworks**:
- Barrier T-maze EBD task (Salamone and colleagues, rat version)
- Mouse barrier T-maze (developed and validated in this paper)
- BehaviorDEPOT (behaviour analysis software)
- stGtACR2 (soma-targeted inhibitory opsin)
- Top-down ACC control model (overriding striatal effort-aversion)

**Brain regions**:
- Anterior cingulate cortex (ACC / Cg1)
- Dorsal striatum
- Mediodorsal thalamus
- Basolateral amygdala
- Ventral striatum / nucleus accumbens
- Prelimbic cortex
- Orbitofrontal cortex
- Habenula
- Anterior insula

**Keywords**:
- effort-based decision making
- anterior cingulate cortex
- optogenetics
- barrier T-maze
- action selection
- cost-benefit tradeoff
- goal-directed behaviour
- movement microstructure
- DeepLabCut behaviour tracking
- neuropsychiatric disorders
- excitatory neuron silencing
- ballistic movement continuity
