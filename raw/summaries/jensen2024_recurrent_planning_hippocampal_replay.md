---
source_file: jensen2024_recurrent_planning_hippocampal_replay.md
title: "A recurrent network model of planning explains hippocampal replay and human behavior"
authors: Kristopher T. Jensen, Guillaume Hennequin, Marcelo G. Mattar
year: 2024
journal: Nature Neuroscience
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A recurrent meta-reinforcement learning agent augmented with imagined policy rollouts learns to plan when beneficial, reproducing human thinking-time variability and matching the spatiotemporal statistics of rodent hippocampal forward replays.

---

### Background & motivation

Planning — the deliberate simulation of future action sequences before committing to a physical action — is ubiquitous in human and animal behaviour, yet its neural implementation is poorly understood. Prevailing theories propose either dopamine-driven synaptic plasticity from replays or separate model-based and model-free systems arbitrating at decision time, but neither account explains how hippocampal replays could feed back into ongoing cortical decision-making fast enough to guide immediate choices. This paper addresses two specific gaps: (1) how a brain circuit could meta-learn *when* to plan rather than having to pre-commit to a fixed planning strategy, and (2) how hippocampal replay could influence behaviour through rapid network dynamics rather than slow synaptic updates.

---

### Methods

- **Model architecture**: A gated recurrent network (GRU, 100 units) trained via meta-reinforcement learning (policy gradients) on a dynamic 4×4 maze navigation task across ~8×10⁶ episodes drawn from ~2.7×10⁸ possible environments.
- **Planning mechanism**: The agent's action space is augmented with a "rollout" option — sampling imagined action sequences (up to 8 steps) from its own policy using a learned internal world model. Each rollout costs 120 ms of episode time vs. 400 ms for a physical action. Rollout feedback (imagined action sequence + goal-reach indicator) is appended as input to the RNN, modulating the hidden state and thereby the policy.
- **Training**: Parameters frozen after training; all subsequent adaptation occurs through recurrent dynamics alone (meta-RL framework).
- **Human behavioural experiment**: 94 participants recruited online performed the same maze task. Thinking times were estimated for each action by decomposing response time into a perception–action delay (fitted from guided trials with known optimal paths) and a residual thinking-time component.
- **Hippocampal data reanalysis**: Reanalysis of published electrophysiological data from Widloski & Foster (2022) — 37 sessions from 3 rats navigating a dynamic maze; Bayesian decoding of position from tetrode recordings; forward replays defined as spatially and temporally contiguous sequences of ≥3 decoded grid locations during stationary epochs.
- **Key comparisons**: Model rollout probability π(rollout) correlated with human thinking times; replay wall-avoidance, goal over-representation, and behavioural alignment of successful vs. unsuccessful replays compared between model and biological data.

---

### Key findings

- **Human thinking times are structured**: Participants (n=94) spent more time thinking when further from the goal (r=0.272±0.006 with distance) and on the first action of each trial, ruling out random noise as an explanation for response-time variability.
- **Model matches human thinking-time patterns**: The trained RNN performed more rollouts earlier in trials and farther from the goal, mirroring human data. π(rollout) correlated positively with human thinking time (r=0.186±0.007, above chance at r=0±0.004), with a residual correlation of r=0.070±0.006 after conditioning on distance to goal.
- **Rollouts causally improve policy**: Forcing more rollouts at the start of trial 2 monotonically reduced steps-to-goal and decreased policy entropy. Preventing rollouts impaired average reward; randomising rollout timing while preserving count also impaired performance, confirming the agent uses rollouts specifically when beneficial.
- **Successful vs. unsuccessful rollouts have opposite effects**: Successful rollouts (reaching the imagined goal) increased the probability of taking the first rolled-out action, while unsuccessful rollouts decreased it (both effects significant vs. matched controls).
- **Hippocampal replays parallel model rollouts**: Biological replays (i) avoided walls more than chance (P<0.001), consistent with a rapidly updating internal model; (ii) over-represented the goal location (P<0.001); and (iii) predicted subsequent physical actions more accurately when successful than unsuccessful (P<0.001 in home trials, P=0.129 in away/control trials).
- **Consecutive replays become increasingly goal-directed**: In trials with ≥3 replays, goal over-representation increased with replay number (2nd replay P=0.068, 3rd replay P=0.009), consistent with iterative policy refinement — an effect absent in away trials and mirrored in the RL agent.

---

### Computational framework

The paper uses **meta-reinforcement learning** (meta-RL) with an embedded **model-based planning** subroutine.

- **Meta-RL component**: A recurrent neural network (GRU) learns to adapt to new environments purely through changes in its hidden state, with synaptic weights fixed after training. This implements "fast adaptation via slow RL" — the network is trained over millions of environments so that its dynamics implement a general-purpose inference and decision-making algorithm.
- **Planning as hidden-state optimisation**: At each decision point, the agent can choose to perform a rollout — sampling a hypothetical trajectory from its own policy via a learned world model (predicting next state and goal location). The rollout output is fed back as input, modifying the hidden state hₖ and consequently the policy πθ(aₖ|hₖ). This is analogous to a policy gradient update in hidden-state space rather than parameter space.
- **Key variables**: Hidden state hₖ (carries task context); policy πθ; internal world model (predicts next state and goal); rollout probability π(rollout); temporal cost of rollouts (120 ms) vs. physical actions (400 ms).
- **Core assumption**: Policy refinement through rollouts operates via fast network dynamics, not synaptic plasticity. This allows planning to occur on the timescale of hundreds of milliseconds.

---

### Prevailing model of the system under study

The paper's introduction signals two dominant frameworks it is pushing against:

1. **Dopamine-mediated replay learning**: The standard view holds that hippocampal replays update state-action values (or successor representations) through dopamine-dependent synaptic plasticity, operating on a slower timescale. This account can explain gradual improvement across episodes but is invoked mainly for offline memory consolidation or within-session value updating, not for real-time within-trial decision-making.

2. **Separate model-based and model-free arbitration**: Prevailing computational accounts (Daw, Niv & Dayan 2005; Geerts et al. 2020) posit parallel systems — a fast, habitual model-free controller and a slower, flexible model-based planner — with arbitration determined by uncertainty or resource costs. In this view, model-based planning produces a separate plan that is then arbitrated against a cached value, rather than directly modulating a unified policy.

The paper also notes that prior recurrent meta-RL models (Wang et al. 2018) achieve rapid adaptation through hidden-state dynamics but cannot "think" — they make instantaneous decisions and have no mechanism for deliberate simulation before acting.

---

### What this paper contributes

- **Unification of planning and replay**: Rather than treating replay as a separate offline learning mechanism, the model proposes that hippocampal forward replays function as on-policy rollouts that iteratively refine a single unified policy through prefrontal recurrent dynamics.
- **Normative account of thinking-time variability**: The model provides a normative explanation for why humans think for variable durations — the agent learns to trade off the temporal cost of a rollout (120 ms lost to potential physical progress) against the expected policy improvement. Thinking is beneficial precisely when the policy is uncertain (far from goal, early in trial).
- **Policy refinement rather than system arbitration**: The model replaces the dual-system arbitration picture with a single policy whose quality is iteratively improved by rollouts. Model-based computation (the rollout) directly updates the hidden state of the same network used for model-free decisions.
- **Mechanistic bridge to hippocampal data**: The finding that consecutive biological replays become increasingly goal-directed — and that successful replays predict the animal's next action while unsuccessful ones do not, specifically in trials where the goal is known — provides novel quantitative support for the hypothesis that replays implement an iterative policy-refinement computation.

---

### Brain regions & systems

- **Prefrontal cortex (PFC)** — modelled as the RNN itself; proposed locus of recurrent dynamics that implement fast adaptation and maintain the hidden state encoding task context and current policy. The model follows Wang et al. (2018) in using PFC as a broad term encompassing associated striatal and thalamic areas.
- **Hippocampus / hippocampal formation** — modelled as the world model component; proposed to generate forward replay sequences (rollout content) that are fed back to PFC during stationary periods. Hippocampal replays are the biological correlate of model rollouts.
- **Prefrontal–hippocampal circuit** — the key interaction: hippocampal replays triggered during sharp-wave ripples are proposed to drive changes in PFC hidden-state dynamics, consistent with previous recordings showing coordinated excitation/inhibition of PFC ensembles during hippocampal SWRs (Jadhav et al. 2016).

---

### Mechanistic insight

The paper meets both criteria for this section: it formalises an algorithm and provides neural data that is specifically consistent with that algorithm.

**Computational (what problem is the brain solving, and why?)**
The brain must make near-optimal sequential decisions in novel environments without prohibitive amounts of physical experience. It does so by trading off time for additional computation: mental simulation of possible futures is faster and less risky than executing suboptimal physical actions. The planning computation is normatively justified when the expected policy improvement from a rollout exceeds its temporal opportunity cost.

**Algorithmic (what representations and processes implement the solution?)**
The solution is implemented as hidden-state optimisation in a recurrent network. On each decision step, the agent can invoke a world-model rollout: it simulates an action sequence from its current policy, evaluates whether the sequence reaches the goal, and feeds the result back as input to update its hidden state. Successful rollouts increase the probability of the rolled-out action; unsuccessful ones decrease it. Multiple successive rollouts iteratively refine the policy, increasing goal-directedness without any parameter updates. The same mechanism explains why consecutive hippocampal replays become increasingly goal-directed: the biological circuit implements the same iterative policy-refinement loop.

**Implementational (how is this realised in neural hardware?)**
The paper does not directly identify specific cell types or biophysical mechanisms, but proposes that hippocampal sharp-wave ripples carry forward-replay sequences that drive coordinated changes in PFC ensemble activity — consistent with Jadhav et al.'s recordings of coordinated PFC excitation/inhibition during SWRs. The specific prediction is that PFC representations should shift to make replayed actions more likely after a successful replay and less likely after an unsuccessful one, akin to an actor–critic update in hidden-state space. This implementational prediction is testable but not yet directly verified in the biological data.

**Bonus**: The paper explicitly discusses compatibility with theta sequences as a parallel short-timescale mechanism providing predictive feedback during active locomotion, while replays handle longer-horizon planning during stationary periods.

---

### Limitations & open questions

- **Causal role of replays in biological animals**: The correlation between replay success and subsequent physical action is consistent with the model but does not rule out the possibility that the baseline policy was already biased toward goal-directed actions before the replay. The paper acknowledges this confound and proposes recording simultaneous hippocampal and PFC activity to track within-replay changes in PFC representations.
- **Away trial null result**: The animal timing analysis (time spent at goal as a function of distance) did not replicate the human thinking-time pattern, plausibly because the rodent task imposed a fixed delay that decoupled thinking time from temporal opportunity costs.
- **Human meta-learning vs. model meta-learning**: Human participants performed well immediately from written instructions, while the model required millions of training episodes. The authors hypothesise that humans have pre-existing planning algorithms and world-model construction abilities, but the model does not capture this.
- **Non-local and reverse replays**: The paper focuses on local forward replays; the framework does not preclude a role for backward or non-local replays but does not model them.
- **Rollout mechanism**: The model assumes a flat, sequential rollout structure; the authors acknowledge that branching rollouts or hierarchical planning might be more efficient in certain environments.
- **Physical implementation**: Specific cell types, neuromodulatory mechanisms, and the precise circuit motif by which hippocampal replay output modifies PFC hidden states remain unspecified.

---

### Connections & keywords

**Key citations**:
- Wang et al. (2018) *Nat. Neurosci.* — prefrontal cortex as meta-RL system
- Mattar & Daw (2018) *Nat. Neurosci.* — prioritised memory access and hippocampal replay
- Widloski & Foster (2022) *Neuron* — hippocampal replay in dynamic maze (dataset reanalysed here)
- Pfeiffer & Foster (2013) *Nature* — hippocampal forward replay toward remembered goals
- Foster (2017) *Annu. Rev. Neurosci.* — replay comes of age (review)
- Hamrick et al. (2017) — metacontrol for imagination-based optimisation
- Pascanu et al. (2017) — learning model-based planning from scratch
- Jadhav et al. (2016) *Neuron* — coordinated PFC activity during hippocampal SWRs
- Daw, Niv & Dayan (2005) *Nat. Neurosci.* — model-free vs. model-based arbitration

**Named models or frameworks**:
- Meta-reinforcement learning (meta-RL)
- Recurrent neural network (RNN/GRU) as prefrontal model
- Policy rollouts / imagined action sequences
- Actor–critic reinforcement learning
- Prioritised memory access (Mattar & Daw)

**Brain regions**:
- Prefrontal cortex (PFC)
- Hippocampus / hippocampal formation
- Prefrontal–hippocampal circuit
- Striatum (implicitly, via Wang et al. framing)
- VTA (mentioned in context of dopamine-mediated plasticity alternatives)

**Keywords**: meta-reinforcement learning, hippocampal replay, prefrontal cortex, policy rollouts, planning, recurrent neural network, hidden-state optimisation, thinking time, model-based reinforcement learning, spatial navigation, forward replay, sharp-wave ripples
