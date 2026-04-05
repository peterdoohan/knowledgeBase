---
source_file: botvinick2012_planning_inference.md
title: "Planning as inference"
authors: Matthew Botvinick, Marc Toussaint
year: 2012
journal: Trends in Cognitive Sciences
paper_type: review
contribution_type: theoretical
---

### One-line summary

This forum piece argues that planning can be reframed as probabilistic inference over a generative model of actions, outcomes, and rewards, and sketches how this planning-as-inference (PAI) framework maps onto neural circuits and connects to broader Bayesian accounts of cognition.

---

### Background & motivation

Goal-directed decision making requires prospective planning — selecting actions based on forecasts of their outcomes — yet the information-processing operations underlying this capacity remain poorly understood. While habitual action selection has been well characterised through temporal-difference reinforcement learning and dopaminergic reward-prediction error signals, no comparable mechanistic account exists for goal-directed planning. Classical cognitive and operations-research approaches (dynamic programming, model-based RL, tree search) offer partial answers but do not unify planning with other cognitive functions or with known neural substrates. The paper identifies this gap and introduces PAI as a candidate unifying framework.

---

### Methods

This is a theoretical review / position paper. No original data are collected. The approach consists of:

- Reviewing the AI/machine learning lineage of PAI, from 1980s roots through contemporary formulations using KL-divergence minimisation and expectation-maximisation.
- Describing the core formalism: an agent maintains a generative model (Bayesian network) over states, actions, and rewards; planning corresponds to inferring the policy that maximises the probability of receiving reward.
- Summarising computational benefits observed in robotics and AI applications of PAI (faster convergence, tractability on hard problems).
- Reviewing Solway and Botvinick (2012) as a case study: a neural-network implementation of PAI applied to reward-based choice tasks previously studied with single-unit recording in primates.
- Drawing analogies between PAI's iterative inference and drift-diffusion models of perceptual decision-making.

---

### Key findings

- PAI recasts planning as minimisation of the KL divergence between the agent's current policy distribution and the posterior distribution over actions conditioned on future reward.
- Message-passing in the PAI graphical model produces two sets of signals — forward messages (probability of reaching states) and backward messages (likelihood of states given reward) — whose integration yields action probabilities that can update the policy iteratively.
- A neural-network implementation of PAI (Solway & Botvinick, 2012) reproduced the response profiles of individual neurons in dorsal striatum (action-value coding) and orbitofrontal cortex (offer-value and chosen-value coding) observed in primate electrophysiology during reward-based choice.
- Iterative inference in PAI is formally equivalent to drift-diffusion integration under certain conditions, suggesting that reward-based and perceptual decision making share a common algorithmic substrate.
- PAI extends naturally to partially observable MDPs (POMDP) via belief-state representations.
- Sampling-based approximations to PAI are proposed as a potential account of bounded rationality and capacity-limited planning in humans.

---

### Computational framework

**Planning-as-inference (PAI) / Bayesian inference over MDPs.**

The agent maintains an internal generative model represented as a Bayesian network with nodes for states (s), actions (a), and reward (r) at successive time steps. The policy π specifies conditional distributions over actions given states. Planning is accomplished by conditioning on reward receipt and performing inverse inference to find the maximum-likelihood (or posterior) policy. Formally, this involves minimising the KL divergence between the marginal distribution under the current policy and the posterior distribution conditioned on r=1. The EM algorithm provides a practical iterative solution: the E-step computes forward and backward messages through the graphical model; the M-step updates the policy. Key assumptions: (1) the agent possesses an accurate internal model of state transitions and rewards; (2) future reward can be treated as an observed variable to condition on; (3) approximate inference (message passing, sampling) can substitute for exact inference when the state space is large.

---

### Prevailing model of the system under study

The introduction frames the field as having a well-developed account of habitual action selection — mediated by dopaminergic reward-prediction error signals driving striatal value representations, formalised by temporal-difference RL — but lacking any equivalent mechanistic account for goal-directed, prospective planning. The dominant computational tools available for planning (dynamic programming, model-based RL tree search) are presented as useful but theoretically isolated: they do not connect planning to other cognitive or neural processes in any principled way. The paper thus assumes a landscape where planning is treated as a distinct, computationally opaque capacity, in contrast to perception and motor control, which have been productively analysed in Bayesian/inference terms.

---

### What this paper contributes

PAI provides a principled reframing of planning as a special case of probabilistic inference, unifying it with Bayesian accounts of perception, motor control, language, and social cognition. This is conceptually significant: it suggests that the brain does not require a separate, specialised planning mechanism but may instead reuse domain-general inference machinery. More concretely, the framework generates a specific architectural prediction — that goal-directed behaviour should implicate a generative model linking plans → actions → outcomes → rewards — and preliminary neural network simulations show that this architecture reproduces known firing-rate profiles in OFC, dorsal striatum, and DLPFC without being directly fitted to those data. The paper also identifies a novel connection between planning and perceptual decision-making through the shared role of iterative integration, suggesting that integrator neurons in parietal/frontal cortex previously studied in perceptual choice may have a functional analogue in reward-based planning.

---

### Brain regions & systems

- **Dorsal striatum** — proposed site of action-value representations; PAI neural network units matching action-value coding of primate striatal neurons.
- **Orbitofrontal cortex (OFC)** — proposed site of offer-value and chosen-value coding; PAI units match OFC neurophysiology from Padoa-Schioppa & Assad (2006).
- **Dorsolateral prefrontal cortex (DLPFC)** — proposed site of policy representation and iterative integration, analogous to evidence-accumulation integrators in perceptual decision making; modelled as threshold-crossing accumulators in PAI simulations.
- **Lateral intraparietal area (LIP)** — cited as locus of evidence integration in perceptual decision making (Gold & Shadlen, 2007); provides the neural analogy for iterative inference in PAI.
- **Middle temporal area (MT)** — cited as source of momentary motion evidence feeding LIP; analogous to OFC's role as evidence source in the reward domain.

---

### Mechanistic insight

The paper does not meet the full bar. It proposes a specific algorithm (PAI with message passing and iterative policy updating) and cites neural data from other studies (Lau & Glimcher 2008; Padoa-Schioppa & Assad 2006; Gold & Shadlen 2007) that are consistent with the algorithm's predicted response profiles. However, the neural data cited were not collected to test PAI specifically — the simulations in Solway & Botvinick (2012) retroactively show that PAI units can match existing recordings, but no experiment was designed to adjudicate between PAI and alternative algorithms (e.g., standard model-based RL or dynamic programming) using neural measurements. The paper thus sits at the level of a computational/algorithmic proposal with suggestive post-hoc neural alignment, not a mechanistically validated account.

---

### Limitations & open questions

- **Empirical predictions lacking**: the authors explicitly acknowledge that PAI has no distinctive, empirically tested predictions that differentiate it from other computational accounts of planning. Generating and testing such predictions is identified as the primary next step.
- **Bounded rationality**: PAI as formulated assumes tractable inference; real human planning operates under severe capacity constraints. Sampling-based approximations are proposed but not developed, and it remains unclear whether they produce the right behavioural signatures.
- **Model accuracy**: PAI relies on an accurate internal generative model of the environment. How such a model is acquired, updated, and represented neurally is not addressed.
- **Scope of the neural story**: the mapping between PAI components and brain regions is based on a single simulation paper (Solway & Botvinick, 2012) and remains preliminary.
- **Relationship to free-energy / active inference**: the paper notes Friston et al.'s (2010) related framework but does not systematically compare the two approaches or identify where they diverge empirically.

---

### Connections & keywords

**Key citations:**
- Solway, A. & Botvinick, M.M. (2012) — neural network implementation of PAI matched to primate data
- Toussaint, M. & Storkey, A. (2006) — foundational PAI formulation using EM
- Rawlik, K. et al. (2012) — stochastic optimal control via approximate inference
- Kappen, H.J. et al. (2012) — optimal control as graphical model inference
- Friston, K. et al. (2010) — free-energy / active inference framework
- Gold, J.I. & Shadlen, M.N. (2007) — neural basis of perceptual decision making / drift-diffusion
- Lau, B. & Glimcher, P.W. (2008) — action-value coding in primate striatum
- Padoa-Schioppa, C. & Assad, J.A. (2006) — value coding in orbitofrontal cortex
- Niv, Y. (2009) — reinforcement learning in the brain
- Balleine, B.W. & O'Doherty, J.P. (2010) — habitual vs goal-directed action

**Named models or frameworks:**
- Planning-as-inference (PAI)
- Expectation-maximisation (EM) for policy optimisation
- KL-divergence minimisation (Botvinick/Rawlik/Kappen formulation)
- Drift-diffusion model (perceptual decision making)
- Active inference / free-energy principle (Friston)
- Model-based reinforcement learning
- Partially observable Markov decision process (POMDP)

**Brain regions:**
- Dorsal striatum
- Orbitofrontal cortex (OFC)
- Dorsolateral prefrontal cortex (DLPFC)
- Lateral intraparietal area (LIP)
- Middle temporal area (MT)

**Keywords:**
- planning as inference
- probabilistic inference
- Markov decision process
- goal-directed decision making
- habitual vs goal-directed action
- generative model
- message passing
- drift-diffusion model
- bounded rationality
- Bayesian brain
- reward-based decision making
- iterative policy optimisation
