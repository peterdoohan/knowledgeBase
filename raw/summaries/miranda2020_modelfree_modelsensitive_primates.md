---
source_file: "miranda2020_modelfree_modelsensitive_primates.md"
paper_id: "miranda2020_modelfree_modelsensitive_primates"
title: "Combined model-free and model-sensitive reinforcement learning in non-human primates"
authors: "Bruno Miranda, W. M. Nishantha Malalasekera, Timothy E. Behrens, Peter Dayan, Steven W. Kennerley"
year: 2020
journal: "PLOS Computational Biology"
paper_type: "computational"
contribution_type: "empirical"
species: ["human", "monkey"]
tasks: ["two_step_task"]
methods: ["computational_modeling", "behavioral_analysis"]
brain_regions: ["prefrontal_cortex", "striatum"]
frameworks: ["reinforcement_learning", "model_based_rl", "model_free_rl", "temporal_difference_learning"]
keywords: ["combined", "model", "free", "sensitive", "reinforcement", "learning", "non", "human", "primates"]
key_citations: ["daw2011_model_based_striatal_prediction"]
---

### One-line summary

Two rhesus monkeys performing a two-stage decision task display a stable combination of model-free and model-sensitive reinforcement learning strategies, with model-sensitive control dominant (~90% weight), and response vigour is influenced by both systems in dissociable ways.

---

### Background & motivation

Theoretical reinforcement learning (RL) distinguishes model-free (MF) strategies — which learn action values directly from reward history — from model-based or model-sensitive (MS) strategies, which exploit knowledge of task structure to plan. These complementary systems are widely proposed to coexist and interact in biological agents. However, most empirical support for this combination comes from human studies with limited trial counts, leaving open questions about long-run stability, species generality, and the nature of the interaction. Non-human primates offer a route to obtaining orders of magnitude more trials per subject, enabling finer-grained and more stable characterisation of MF/MS balance.

---

### Methods

- **Subjects**: Two adult male rhesus monkeys (Macaca mulatta), head-fixed, performing 27–30 sessions of ~520–543 trials each (total ~15,585 and ~14,664 trials per subject).
- **Task**: Two-stage Markov decision task (adapted from Daw et al. 2011). At a first-stage state subjects chose between two stimuli; transitions to one of two second-stage states were common (70%) or rare (30%). At the second stage, another choice was required and rewarded at one of three levels (high/medium/low, defined by juice amount and delay). Second-stage reward contingencies changed stochastically every 5–9 trials.
- **Behavioural analysis**: Multiple logistic regression on first-stage choice, regressing on reward, transition type, and their interaction up to five trials back. Reaction time (RT) and eye-fixation time (fixRT) analysed with linear regression using the same predictors.
- **Computational modelling**: Pure MF models (SARSA, Q-learning ± eligibility trace), pure MS models (Forward1/2/3, differing in how transition probabilities are represented), and hybrid combinations. A novel Hybrid+ model was developed to correct systematic residuals in the standard Hybrid model.
- **Model comparison**: Fixed-effects BIC and mixed-effects BICint; protected exceedance probability (PEP) via SPM12 Bayesian model selection. Validation by simulating choice data from best-fitting models and re-running all descriptive and regression analyses.

---

### Key findings

- Both subjects showed clear signatures of MF and MS RL: first-stage choice repetition was elevated after high reward through a common transition and suppressed after high reward through a rare transition (canonical MS signature), while also being influenced by reward history alone (MF signature).
- MS influence significantly exceeded MF influence: reward × transition interaction weight was greater than the main reward effect in all sessions (F-tests p < 0.001 for both subjects).
- Effects of both reward history and reward × transition decayed approximately exponentially across the preceding five trials (decay constants ~0.78–1.62 for reward; ~0.94–1.50 for reward × transition).
- The best-fitting Hybrid model confirmed MS dominance: MS weight parameter ω ≈ 0.86–0.88 (both subjects; significantly different from 0 and 1, p < 0.001 all sessions). Learning rates were high (~0.78–0.82), consistent with non-stationary reward structure.
- The standard Hybrid model (Daw et al. 2011) systematically over-weighted the immediately preceding trial. A novel Hybrid+ model correcting this — by adding a reward-and-transition-dependent credit assignment boost/suppression to the first-stage action value after each trial — provided a significantly better fit (PEP > 0.99 over all alternatives), with three additional parameters (L1, L2, L3 quantifying reinforcement strength per outcome level).
- High reward produced positive reinforcement strength (L1 > 0); medium and low rewards produced aversive effects (L2, L3 < 0).
- MS dominance and MF ω parameter were stable across sessions; the logistic reward × transition coefficient declined across sessions, explained by increasing choice stochasticity (lower β1) rather than a genuine change in MS strategy.
- First-stage RTs were slower precisely when MS-dictated choice switching was highest (after high reward on rare transition; after low reward on common transition), consistent with a speed-accuracy trade-off between MF (fast) and MS (slow) computation.
- FixRT (time to acquire eye fixation) showed only a MF main-effect of reward with no reward × transition interaction, suggesting tonic MF vigor signals influence fixation while phasic MS computations affect joystick RT.

---

### Computational framework

The paper uses standard reinforcement learning — specifically temporal difference (TD) learning — as its primary framework, extended to include model-sensitive (MS) strategies.

**MF component (SARSA)**: Updates state-action values Q(s,a) via TD prediction errors δ; state s_{i+1} is evaluated according to the action actually taken. An eligibility trace parameter λ allows second-stage prediction errors to propagate back to first-stage values.

**MS component (Forward1)**: Computes first-stage action values by weighting second-stage Q values by known state-transition probabilities (T = 0.7/0.3). State-transition probabilities are treated as known from task onset, consistent with extensive pre-training.

**Hybrid model**: First-stage action values Q_HYB = (1 − ω)·Q_MF + ω·Q_MS, where ω ∈ (0,1) arbitrates between MF and MS control. Actions chosen by softmax with inverse temperature β and perseveration parameter κ.

**Hybrid+ extension**: After computing Q_HYB, the value of the chosen (or unchosen) first-stage action is boosted/suppressed by a factor Lj (per outcome level j), applied positively if the previous transition was common and negatively if rare (or vice versa for unchosen action). This encodes a one-step MS credit assignment, interpretable as a MF implementation of a MS effect via a working-memory-for-state representation.

Key variables: Q(s,a) (state-action values), δ (prediction error), ω (MS weight), α (learning rate), β (inverse temperature), κ (perseveration), L1/L2/L3 (outcome-level reinforcement strengths).

---

### Prevailing model of the system under study

The paper works within the established dual-system RL framework, in which MF and MB/MS strategies are implemented by distinct neural systems (striatum/basal ganglia for MF habit-like learning; prefrontal cortex and associative striatum for MS/goal-directed control) that compete or cooperate based on their relative uncertainty or computational cost. The two-stage task (Daw et al. 2011) had previously demonstrated this combination in humans, with ω typically ~40–60%. The prevailing assumption was that MS control might be fragile, resource-limited, and possibly unstable over extended training. Rodent studies using outcome devaluation provided an earlier and cruder dissociation. Prior to this paper, only modest trial numbers were available from human experiments, and primate data on MF/MS arbitration were essentially absent.

---

### What this paper contributes

The paper establishes that non-human primates robustly employ both MF and MS strategies in the two-stage task, but with substantially stronger MS dominance (~90%) than typically found in humans (~40–60%), and that this MS dominance is stable across weeks of testing rather than collapsing into habit. This refines the prevailing model in several ways:

1. **Species generality and training duration**: MF/MS coexistence is not uniquely human, and extensive training does not simply produce habit (MF dominance) — MS control can consolidate and remain primary.
2. **Hybrid+ model**: The paper identifies a systematic failure of the standard Hybrid model (excess first-trial influence) and introduces a novel MS-perseveration mechanism (reward-and-transition-dependent credit assignment boost) that substantially improves fit. This mechanism is interpretable as a MF implementation of MS reasoning via one-step working-memory-for-state representations, blurring the MF/MS boundary at a process level.
3. **Vigor dissociation**: RT and fixRT show dissociable MF and MS influences — RT is sensitive to both, fixRT only to MF reward signals — suggesting the two systems contribute differently to action initiation and deliberation speed.
4. **SARSA over Q-learning in primates**: The best-fitting MF model is SARSA (consistent with prior NHP electrophysiology) rather than Q-learning (as in rodents), suggesting a species difference in the implementation of the MF controller.

---

### Brain regions & systems

Not applicable — the paper is a purely behavioural/computational study with no neural recordings or imaging. The authors explicitly note that identifying the biological substrates of these computational mechanisms is left for future work.

The computations modelled are commonly attributed to:
- Striatum (dorsolateral) — MF habit-like value learning
- Prefrontal cortex and ventral/associative striatum — MS goal-directed planning
- Dopamine system — reward prediction errors and response vigor

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined. It presents and validates a detailed RL algorithm (Hybrid+) that explains choice behaviour, but provides no neural data (recordings, imaging, lesions, pharmacology) linking the model's specific variables — prediction errors, MS weight ω, or the L-parameters — to measured neural activity. The authors explicitly call for future neural studies to uncover the biological substrates.

---

### Limitations & open questions

- Only two subjects (standard for primate electrophysiology), precluding population-level generalisation of RL parameter estimates.
- Extensive pre-training means the paper cannot characterise the acquisition phase of MF/MS strategies — how the task model is learned remains unaddressed.
- The paper cannot distinguish between different implementations of MS reasoning (e.g., genuine prospective planning vs. MF representations of MS-relevant state transitions); any task-structure dependence is classified as "model-sensitive".
- The Hybrid+ MS perseveration persisted for only one trial; the mechanism underlying this bounded working memory for state is not identified.
- Whether the greater MS dominance in monkeys versus humans reflects species differences, training duration, task design differences, or motivational factors (fluid restriction) cannot be separated.
- No neural data are presented; the computational dissection remains at the algorithmic level.
- The reduction in the reward × transition logistic coefficient across sessions may partly reflect a genuine shift in strategy rather than purely increased stochasticity, but this cannot be fully disentangled with current analyses.

---

### Connections & keywords

**Key citations**:
- Daw ND et al. (2011) — original two-stage task in humans (Neuron); primary comparison model
- Daw ND, Niv Y, Dayan P (2005) — uncertainty-based competition between prefrontal and striatal systems (Nature Neuroscience)
- Akam T, Costa R, Dayan P (2015) — simple plans vs. sophisticated habits in the two-step task (PLOS Comput Biol)
- Morris G et al. (2006) — SARSA in non-human primates (Nature Neuroscience)
- Roesch MR et al. (2007) — Q-learning in rodents (Nature Neuroscience)
- Glascher J et al. (2010) — states vs. rewards, model-based vs. model-free neural prediction errors (Neuron)
- Niv Y et al. (2007) — tonic dopamine and response vigor (Psychopharmacology)

**Named models or frameworks**:
- SARSA (model-free TD learning)
- Q-learning (model-free TD learning)
- Forward1/2/3 (model-sensitive planning models with different transition probability representations)
- Hybrid model (Daw et al. 2011)
- Hybrid+ model (novel; introduces MS-perseveration credit assignment)
- Two-stage (two-step) Markov decision task

**Brain regions**: None directly studied (behavioural/computational paper).

**Keywords**: model-free reinforcement learning, model-sensitive reinforcement learning, model-based reinforcement learning, two-stage decision task, non-human primates, habit vs. goal-directed, response vigour, reaction time, credit assignment, SARSA, hybrid RL model, Bayesian model comparison
