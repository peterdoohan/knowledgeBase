---
source_file: "dolan2013_goals_habits_brain_b.md"
paper_id: "dolan2013_goals_habits_brain_b"
title: "Goals and Habits in the Brain"
authors: "Ray J. Dolan, Peter Dayan"
year: 2013
journal: "Neuron"
paper_type: "review"
contribution_type: "review"
species: ["human"]
tasks: ["two_step_task"]
methods: ["fmri", "lesion"]
brain_regions: ["hippocampus", "prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "striatum", "dorsomedial_striatum", "dorsolateral_striatum", "ventral_striatum", "nucleus_accumbens", "ventral_tegmental_area", "substantia_nigra", "amygdala", "basolateral_amygdala"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl", "successor_representation", "temporal_difference_learning"]
keywords: ["goals", "habits", "brain"]
key_citations: ["tolman1948_cognitive_maps_rats", "balleine1998_goal_directed_instrumental_action", "daw2005_uncertainty_prefrontal_striatal"]
---

### One-line summary

This review traces five generations of research on goal-directed versus habitual instrumental control, showing how the model-based/model-free reinforcement learning framework has sharpened the behavioural, neural, and computational understanding of these two systems and their interactions.

---

### Background & motivation

A longstanding dichotomy in the psychology of action distinguishes reflective, prospective decision making from reflexive, experience-driven control. Although this distinction has been realised in many ways (goal-directed/habitual, model-based/model-free, System 1/System 2), one particular strand originating in animal behavioural work has been most productive for cognitive and computational neuroscience. This review asks how that strand has evolved from early rodent lesion studies through human neuroimaging and computational modelling to the current frontier of questions about how the two systems interact, compete, and break down in psychopathology.

---

### Methods

This is a narrative review organised around five "generations" of empirical and theoretical work. The authors do not apply formal inclusion criteria or meta-analytic methods; instead, they select representative studies that illustrate conceptual progress:

- Generation 0: classical animal learning studies (Tolman's cognitive maps vs. stimulus-response theories).
- Generation 1: first-generation behavioural dissociations using outcome devaluation and contingency degradation in rodents, plus lesion/inactivation studies.
- Generation 2: human fMRI adaptations of the same paradigms.
- Generation 3: introduction of model-based and model-free RL frameworks (temporal difference learning, sequential Markov decision tasks) and associated fMRI studies.
- Generation 4: pharmacological, structural connectivity, and novel task-based investigations of the balance between model-based and model-free control.
- Generation 5: forward-looking discussion of open questions (model-based realization, arbitration mechanisms, Pavlovian interactions, psychopathology).

---

### Key findings

- Behavioural criteria (outcome devaluation insensitivity; contingency degradation insensitivity) reliably dissociate goal-directed from habitual control, and extended interval-schedule training promotes the transition from goal-directed to habitual.
- Rodent lesion work establishes a double dissociation: dorsomedial striatum (caudate) and prelimbic prefrontal cortex support goal-directed control; dorsolateral striatum (putamen) and infralimbic prefrontal cortex support habitual control.
- Human fMRI confirms this dissociation: ventral orbitofrontal/vmPFC activity tracks value in goal-directed choice; posterior putamen/globus pallidus activity increases with extended, habit-promoting training.
- Model-free temporal difference (TD) prediction errors correlate with BOLD in ventral striatum across many studies; a separable state prediction error (reflecting model acquisition) is seen in posterior parietal and lateral prefrontal cortex.
- In the two-step Markov decision task (Daw et al., 2011), individual subjects vary continuously in the degree to which their behaviour is model-based versus model-free; ventral striatal BOLD tracks both model-free TD errors and model-based prediction errors, suggesting the model-based system trains the model-free system.
- Caudate encodes prospectively calculated action values consistent with tree-search (model-based); putamen encodes cached values from overtraining (model-free); vmPFC encodes the chosen value irrespective of which system generated it.
- Dopamine manipulation modulates the model-based/model-free balance: dopamine depletion (APTD) increases habitual slips of action; L-DOPA administration increases model-based behaviour; TMS disruption of prefrontal cortex renders behaviour more habitual.
- White matter connectivity between premotor cortex and posterior putamen predicts susceptibility to slips of action; connectivity between caudate and vmPFC predicts goal-directed flexibility.
- In OCD, outcome-devaluation insensitivity and elevated slips of action suggest dominance of the habitual system; drug addiction may reflect a dopamine-dependent spiral from ventral to dorsal striatum shifting control to stimulus-response habits; over-dominant model-based control is speculatively linked to psychotic phenomena.

---

### Computational framework

The paper's central computational framework is reinforcement learning (RL), specifically the contrast between model-free and model-based RL.

- **Model-free RL** (e.g., temporal difference learning, Q-learning, actor-critic): an agent learns cached estimates of long-run value via prediction errors (TD errors) based solely on experienced outcomes. Values are retrospective and insensitive to immediate devaluation. The TD prediction error — signalled by phasic dopamine activity — is the core learning signal.
- **Model-based RL**: an agent maintains an internal model of state-action-outcome transition structure, builds a prospective decision tree from the current state, and evaluates policies by forward or backward search. Values are computed on the fly and immediately sensitive to changes in outcome desirability. Computationally expensive, constrained by working memory capacity.
- **Hybrid / arbitration**: behaviour is often best described by a weighted combination of the two systems. Proposed arbitration criteria include relative uncertainty (Daw et al., 2005), cost-benefit analysis of computation time versus accuracy (Keramati et al., 2011), and DYNA-style replay in which the model-based system trains the model-free system offline (Sutton, 1991).
- Key formal quantities: state, action, transition probability, utility/reward, value function (V or Q), TD prediction error (δ = r + γV(s') − V(s)), state prediction error (surprise in a new state given the learned transition model).

---

### Prevailing model of the system under study

The paper's introduction situates itself within a dual-system tradition that stretches back to the Tolman-versus-S-R debate in mid-twentieth-century psychology. By 2013, the field broadly accepted that:

1. Instrumental behaviour can be controlled by two distinct systems — one flexible and outcome-sensitive (goal-directed), one automatic and outcome-insensitive (habitual) — with the balance shifting toward habits under extended training on interval schedules.
2. These systems have separable neural substrates, with converging rodent lesion and pharmacological evidence pointing to dorsomedial striatum / prelimbic PFC for goal-directed control and dorsolateral striatum / infralimbic PFC for habits.
3. Model-free RL (TD learning, dopamine as RPE signal) provided a good account of the habitual system, with phasic dopamine responses matching the TD prediction error.
4. Goal-directed control was computationally associated with model-based planning but its neural implementation and its interaction with the model-free system were poorly understood.
5. The two systems were commonly treated as in competition, with uncertainty about how arbitration occurs.

---

### What this paper contributes

By synthesising four generations of empirical and theoretical work and charting a fifth, Dolan and Dayan establish several advances over this baseline:

- They show that model-based and model-free signals are not cleanly segregated in the brain: vmPFC integrates both; ventral striatum carries model-based prediction errors even though it was thought to be exclusively model-free.
- They make explicit that the two systems are more richly intertwined than competitive: the model-based system likely trains the model-free one via replay (DYNA-like mechanisms), and both can run in parallel rather than purely competing.
- Pharmacological and structural connectivity evidence (dopamine, TMS, white matter tracts) begins to explain individual variation in the model-based/model-free balance.
- The review establishes the two-step Markov decision task and related paradigms as standard human tools for dissociating the two systems and fitting hybrid models.
- It extends the framework to Pavlovian conditioning (model-based vs. model-free Pavlovian predictions; specific vs. general PIT) and to psychopathology (OCD as habitual dominance, addiction as dopamine-driven striatal spiral, psychosis as model-based over-dominance).
- Key unresolved questions identified: how model-based tree-search is neurally implemented given working memory constraints; how arbitration is computed; how the present model-based/model-free dichotomy relates to other dual-system frameworks (declarative/procedural, episodic/semantic, hierarchical control); how Pavlovian and instrumental model-based predictions interact.

---

### Brain regions & systems

- **Dorsomedial striatum (caudate nucleus)** — supports goal-directed/model-based control; encodes prospectively computed action values during tree-search; impaired by lesions causing premature habitisation.
- **Dorsolateral striatum (putamen)** — supports habitual/model-free control; encodes cached values from overtraining; BOLD increases with extended habit-promoting training; white matter connectivity to premotor cortex predicts slip-of-action vulnerability.
- **Prelimbic medial prefrontal cortex (rodent)** — necessary for goal-directed performance; lesions abolish outcome-devaluation sensitivity and contingency-degradation sensitivity.
- **Infralimbic medial prefrontal cortex (rodent)** — necessary for expression of habitual behaviour; inactivation reinstates goal-directed responding in overtrained animals.
- **Ventromedial prefrontal cortex / orbitofrontal cortex (human)** — encodes current value of outcomes irrespective of whether they were computed model-based or model-free (chosen value); also encodes stimulus and outcome value; devaluation-sensitive BOLD changes in ventral OFC support goal-directed choice.
- **Ventral striatum (nucleus accumbens region)** — primary site of model-free TD prediction error signals (BOLD); also carries model-based prediction errors in proportion to subjects' model-based behaviour, suggesting MB-to-MF training.
- **Hippocampus** — provides cognitive maps and supports latent learning; place cell forward sweeps at choice points are a neural correlate of prospective model-based planning; lesions abolish vicarious trial-and-error; connected to ventral striatum via goal-oriented search mechanisms.
- **Dopaminergic system (substantia nigra / VTA)** — phasic firing encodes TD prediction errors; innervates both dorsomedial and dorsolateral striatum; L-DOPA boosts model-based behaviour; dopamine depletion increases habitual slips; dopamine to vmPFC modulates model-based valuation.
- **Basolateral amygdala** — implicated in goal-directed control and specific Pavlovian-instrumental transfer (model-based Pavlovian predictions).
- **Central amygdala / nucleus accumbens core and shell** — implicated in general (model-free) PIT.
- **Posterior inferior parietal and lateral prefrontal cortices** — carry state prediction errors associated with model acquisition.
- **Anterior caudate** — encodes multi-step planned values during explicit tree-search task (Wunderlich et al., 2012a).

---

### Mechanistic insight

The paper meets the bar for one partial mechanistic account but not a fully implemented one at all three of Marr's levels.

The two-step Markov decision task studies (Daw et al., 2011; Glascher et al., 2010; Wunderlich et al., 2012a, 2012b) together provide both a formal algorithm (hybrid model-based/model-free RL with fitted weighting parameters) and neural data (fMRI) that selectively link specific computational signals to specific regions. However, the neural implementation level (which cell types, which synaptic mechanisms, how the transition model is stored and searched) is largely absent.

- **Computational**: the brain must solve the problem of choosing actions that maximise long-run reward in environments where outcomes depend on multi-step action sequences and where outcome values can change. Two complementary strategies — prospective tree-search and retrospective cached-value lookup — offer different speed-accuracy trade-offs.
- **Algorithmic**: model-based control involves building and searching a state-action-outcome transition model to compute values on the fly; the model-free system stores TD-estimated values and updates them via prediction errors. A hybrid weighting (or DYNA-like cross-training) integrates the two. The caudate encodes prospective planned values; the putamen encodes cached values; vmPFC integrates both into chosen value; ventral striatum reports TD errors and receives model-based error signals proportional to individual subjects' model-based behaviour.
- **Implementational**: pharmacological evidence implicates dopamine as the TD error signal (via nigrostriatal projections to dorsolateral striatum for model-free) and as a modulator of prefrontal working memory (for model-based). TMS of PFC shifts the balance toward habits. White matter tract strength between specific corticostriatal circuits predicts individual differences in the balance. However, specific cell types, receptor subtypes, and biophysical mechanisms are not characterised — this level remains a significant open question.

---

### Limitations & open questions

- The neural implementation of model-based tree-search is unknown: how a decision tree of arbitrary depth is built, stored, searched, and pruned given working memory constraints is not resolved.
- The arbitration mechanism — how the brain decides when to rely on model-based versus model-free control — lacks a definitive neural account; multiple competing proposals (uncertainty-based, cost-benefit, DYNA-style) remain untested against each other.
- The degree to which different "dual-system" framings (model-based/model-free, goal-directed/habitual, declarative/procedural, episodic/semantic, spatial/abstract) are commensurable or dissociable is unresolved.
- The relationship between Pavlovian and instrumental model-based predictions is unclear; revaluation effects in purely Pavlovian paradigms occur even in decorticate animals, suggesting a different substrate than instrumental model-based control.
- Dopamine plays roles in both systems, complicating pharmacological dissections; disease-based depletion studies (Parkinson's) are difficult to interpret alongside experimental depletion and boosting studies.
- Psychopathological applications (OCD, addiction, psychosis) are promising but preliminary; drug confounds and the continuous nature of individual differences in model-based reliance make categorisation difficult.
- Whether there are multiple model-based controllers (mixture models) and how they interact is not settled.
- Animal-to-human homologies (e.g., rat infralimbic cortex to human subgenual ACC) remain uncertain.

---

### Connections & keywords

**Key citations**:
- Daw, Niv & Dayan (2005) — uncertainty-based competition between prefrontal and dorsolateral striatal systems
- Daw, Gershman, Seymour, Dayan & Dolan (2011) — model-based influences on human choices and striatal prediction errors (two-step task)
- Glascher, Daw, Dayan & O'Doherty (2010) — dissociable state vs. reward prediction errors for MB and MF RL
- Wunderlich, Smittenaar & Dolan (2012a) — caudate vs. putamen encoding of planned vs. cached values
- Wunderlich, Dayan & Dolan (2012b) — L-DOPA boosts model-based behaviour
- Balleine & Dickinson (1998) — goal-directed instrumental action and its cortical substrates
- Tricomi, Balleine & O'Doherty (2009) — emergence of habitual control in human fMRI
- Valentin, Dickinson & O'Doherty (2007) — goal-directed choice and OFC
- Sutton & Barto (1998) — reinforcement learning framework
- Schultz, Dayan & Montague (1997) — dopamine as TD prediction error
- Dickinson (1985) — actions and habits: development of behavioural autonomy
- Tolman (1948) — cognitive maps in rats

**Named models or frameworks**:
- Temporal difference (TD) learning / model-free RL
- Model-based RL / prospective tree-search
- Actor-critic architecture
- DYNA / DYNA-Q / DYNA-2 (model-based training of model-free system via replay)
- Successor representation (Dayan, 1993)
- Two-step Markov decision task (Daw et al., 2011)
- Hybrid model-based/model-free weighting model
- Pavlovian-instrumental transfer (PIT), specific and general

**Brain regions**:
- Dorsomedial striatum / caudate nucleus
- Dorsolateral striatum / putamen
- Prelimbic medial prefrontal cortex
- Infralimbic medial prefrontal cortex
- Ventromedial prefrontal cortex (vmPFC)
- Orbitofrontal cortex (OFC)
- Ventral striatum / nucleus accumbens
- Hippocampus
- Dopaminergic system (VTA, substantia nigra)
- Basolateral amygdala
- Central amygdala
- Posterior inferior parietal cortex

**Keywords**:
- goal-directed behaviour
- habitual behaviour
- model-based reinforcement learning
- model-free reinforcement learning
- temporal difference prediction error
- outcome devaluation
- corticostriatal circuits
- dopamine neuromodulation
- Pavlovian-instrumental transfer
- decision-making arbitration
- obsessive-compulsive disorder
- two-step Markov decision task
