---
source_file: "binz2024_meta_learning_cognition.md"
paper_id: "binz2024_meta_learning_cognition"
title: "Meta-Learned Models of Cognition"
authors: "Marcel Binz, Ishita Dasgupta, Akshay Jagadish, Matthew Botvinick, Jane X. Wang, Eric Schulz"
year: 2024
journal: "Psychological Review (preprint / in press)"
paper_type: "review"
contribution_type: "theoretical"
species: ["human"]
tasks: ["two_step_task"]
brain_regions: ["hippocampus", "prefrontal_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "bayesian_inference"]
keywords: ["meta", "learned", "models", "cognition"]
key_citations: ["kemp2008_structural_discovery_form"]
---

### One-line summary

Meta-learning — training recurrent neural networks on distributions of tasks — can produce Bayes-optimal learning algorithms, and this connection to Bayesian inference makes it a principled and more powerful replacement for traditional Bayesian models in the rational analysis of cognition.

---

### Background & motivation

Computational models of human cognition have traditionally been hand-designed: researchers specify prior distributions and likelihood functions for Bayesian models, or fixed structures for cognitive architectures. This reliance on a priori specification limits the scope of rational analysis: exact Bayesian inference is often computationally intractable, the correct prior or likelihood may be unknowable for real-world problems ("large world" settings), and incorporating computational constraints or neuroscientific knowledge is cumbersome. A coherent framework that addresses all these limitations simultaneously was lacking. The authors argue that meta-learning — learning learning algorithms from data — fills this gap and substantially extends the scope of rational analysis.

---

### Methods

This is a theoretical synthesis and research-program paper. Methods consist of:

- **Formal argument**: The authors present a simplified proof (following Ortega et al., 2019) that maximising the log-likelihood of future observations over a distribution of tasks yields a recurrent neural network that approximates the Bayes-optimal posterior predictive distribution. This establishes meta-learning as a constructive route to Bayes-optimal inference.
- **Four arguments for meta-learning over Bayesian inference**: (1) Handles intractable inference — no explicit posterior computation required; (2) Handles unspecified problems — requires only samples from the data-generating distribution, not an explicit prior or likelihood; (3) Enables resource-rational modelling — network size directly constrains algorithmic and/or computational complexity; (4) Integrates neuroscientific constraints — architectural choices encode domain knowledge about the brain.
- **Literature review**: Prior empirical and computational studies applying meta-learning to cognition are reviewed and reinterpreted under these four arguments. Topics covered: heuristics and cognitive biases, language understanding, inductive biases, model-based reasoning, exploration, and cognitive control.
- **Illustrative simulation**: A simple recurrent-network meta-learning implementation (insect-length prediction) is used throughout to demonstrate convergence to Bayesian posterior predictions.

---

### Key findings

- A recurrent neural network trained by maximising log-predictive likelihood over a distribution of tasks converges to the Bayes-optimal posterior predictive distribution under mild conditions (sufficient expressivity, good optimisation); this was demonstrated analytically and shown empirically in a simple Gaussian example.
- This equivalence implies that any behavioural phenomenon explainable by a Bayesian model is also explainable by a meta-learned model — but not vice versa.
- Meta-learning uniquely addresses Savage's "large world" problem: it requires only samples from the environment, not an explicit prior or likelihood, enabling rational models for problems where Bayesian inference cannot even be posed.
- Resource-rational models are naturally produced by constraining network size: limiting weights constrains algorithmic complexity (Kolmogorov-like), limiting activations constrains computational complexity — a capability unique to the meta-learning framework among rational model classes.
- Meta-learned models with restricted complexity spontaneously reproduce human cognitive biases (conservatism, base-rate neglect — Dasgupta et al., 2020) and heuristic strategies (single-cue, equal-weighting — Binz et al., 2022).
- Model-based reasoning, causal inference, compositional generalisation, directed and random exploration, and context-sensitive cognitive control all emerge naturally in meta-trained agents without being explicitly programmed.
- The meta-reinforcement learning framework maps onto prefrontal-dopaminergic circuitry (Wang et al., 2018): slow synaptic changes (outer loop ~ dopamine-driven) give rise to fast within-activity-dynamics learning (inner loop ~ PFC dynamics), unifying neuroscientific and computational perspectives.
- Limitations: meta-learned models lack analytical interpretability; training is time-consuming; convergence to the Bayes-optimal solution is not guaranteed and can fail on complex problems.

---

### Computational framework

**Meta-learning / in-context learning via recurrent neural networks.**

The core formalism is as follows. A recurrent neural network with parameters **Θ** processes a sequence of observations x₁:t and outputs a predictive distribution q(x_{t+1} | x_{1:t}, **Θ**) for the next observation. The outer-loop training objective maximises the expected log-predictive likelihood across tasks sampled from the data-generating distribution p(µ):

E_{µ, x_{1:t+1}} [log q(x_{t+1} | x_{1:t}, **Θ**)]

At convergence, the global optimum of this objective is the Bayesian posterior predictive distribution p(x_{t+1} | x_{1:t}). The network therefore implements Bayesian inference in its forward pass without ever explicitly computing posteriors.

Key variables: the data-generating distribution p(µ) plays the role of the prior; the network weights encode the meta-learned prior implicitly; network activations at inference time encode the sufficient statistics of the posterior. The framework assumes stationarity of the task distribution during meta-training, and that the function class is expressive enough to represent the target predictive distribution.

The same logic extends to reinforcement learning (meta-RL): the network is trained to maximise cumulative reward averaged over a distribution of MDPs, yielding an approximate Bayes-optimal policy implemented in the network's forward dynamics.

---

### Prevailing model of the system under study

The paper targets the rational analysis tradition in cognitive science, which takes Bayesian inference as its normative standard. Under this view, human learning is optimally explained by a researcher-specified prior and likelihood function; behaviour is compared against the resulting Bayesian posterior predictive distribution. Hand-designed Bayesian models have been successfully applied to perception, motor control, everyday judgements, and associative learning, and they are taken as the benchmark for optimality. However, the field has long recognised that (a) exact inference is computationally intractable for realistic models, (b) the correct prior/likelihood for real-world problems is often unknown or unspecifiable (Savage's large vs. small world distinction), and (c) observed deviations from Bayesian optimality suggest that resource constraints must be incorporated. Existing resource-rational approaches (MCMC approximation, variational inference, rational meta-reasoning) address computational complexity but not algorithmic complexity, and none provides a principled path to modelling cognition in large-world settings.

---

### What this paper contributes

The paper establishes meta-learning as a principled extension of rational analysis. It shows formally that meta-learned models can implement Bayes-optimal inference, making them legitimate rational models in the sense of Anderson (1990) and Tenenbaum (2021). Beyond equivalence, four distinct advantages are argued: meta-learning is applicable when Bayesian inference is intractable; it is applicable when the inference problem cannot be posed at all (large worlds); it enables resource-rational modelling at both algorithmic and computational levels within a single framework; and it allows neuroscientific knowledge to be encoded as architectural inductive biases.

By reviewing prior empirical work, the paper demonstrates that meta-learned models have already produced qualitatively new results unavailable to classical Bayesian models: context-dependent heuristic emergence, compositional language generalisation, model-based reasoning from model-free training, and resource-rational exploration. The paper thus establishes meta-learning not merely as a numerical tool but as a theoretical framework that extends — rather than replaces — rational analysis, bridging Bayesian cognitive science, connectionism, and computational neuroscience.

For reviews: the key unresolved question is whether a domain-general meta-learned cognitive model is achievable, requiring: (1) diverse task distributions, (2) natural-language instruction-following, (3) embodiment in realistic environments, and (4) scalable architectures (e.g., transformers).

---

### Brain regions & systems

The paper is primarily theoretical/computational; most analysis is at Marr's computational and algorithmic levels. Where neuroscience is invoked:

- **Prefrontal cortex (PFC)** — proposed locus of the fast inner-loop learning algorithm implemented in neural activity dynamics, analogous to the meta-RL base learner.
- **Dopaminergic system** — maps onto the slow outer-loop meta-learning process; dopamine-driven synaptic plasticity encodes the meta-learned prior. The meta-RL framework (Wang et al., 2018) predicts that dopamine signals should reflect inferred (not just experienced) reward values, consistent with Bromberg-Martin et al. (2010).
- **Hippocampus** — implicated in episodic memory components of meta-RL architectures (Ritter et al., 2018); hippocampal replay patterns resemble model rollouts in planning simulations (Jensen et al., 2023).
- **Functional specialisation circuits** — the paper speculates that training neural networks on diverse tasks produces emergent functional specialisation analogous to that seen in biological brain regions (following Dobs et al., 2022; Yang et al., 2019).

---

### Mechanistic insight

The paper does not meet the full bar: it does not present neural recordings, imaging, or pharmacological data directly linking meta-learning model variables (e.g., hidden-unit activations as approximate posteriors, network weights as prior) to measured neural activity. The neuroscientific content is largely interpretive — mapping the meta-RL framework onto PFC/dopamine circuitry by analogy — and the empirical support cited (Wang et al., 2018; Bromberg-Martin et al., 2010) comes from prior studies rather than new data collected for this paper.

The paper does, however, articulate a candidate mechanistic account at Marr's computational and algorithmic levels: the brain solves the problem of fast, flexible learning in uncertain environments (computational level) by implementing a recurrent inference algorithm in PFC dynamics, shaped by dopamine-driven synaptic plasticity on a slower timescale (algorithmic level). The physical implementation — specific cell types, connectivity, neuromodulators — is referenced from prior work (Wang et al., 2018) but not developed further here.

---

### Limitations & open questions

- **Interpretability**: Meta-learned models do not yield analytical expressions, making structured theoretical exploration harder than with Bayesian models.
- **Training cost**: Modifying assumptions requires retraining from scratch; iterating over hypotheses is conceptually easy but practically slow.
- **No convergence guarantee**: There is no theorem ensuring that training reaches the globally Bayes-optimal solution; failures have been documented (Wang et al., 2021).
- **Domain specificity**: Current meta-learned cognitive models are trained on narrow task families and do not generalise across domains — a domain-general model remains aspirational.
- **Task distribution construction**: How to define a meta-training distribution that captures the full range of human cognition is an open engineering and theoretical problem.
- **Scaling**: It is unknown whether current architectures and outer-loop algorithms scale to the complexity needed for a unified cognitive model.
- **Process vs. outcome**: The paper focuses on fully converged meta-learned algorithms as rational models but does not address how or on what timescale the meta-learning process itself occurs in humans (evolutionary, developmental, within-lifetime?).

---

### Connections & keywords

**Key citations**:
- Ortega et al. (2019) — formal proof that meta-learning produces Bayes-optimal algorithms
- Anderson (2013a/b) — rational analysis of cognition; cognitive architectures
- Griffiths, Kemp & Tenenbaum (2008) — Bayesian models of cognition
- Wang et al. (2016, 2018) — meta-RL and prefrontal-dopamine correspondence
- Dasgupta et al. (2020) — meta-learned cognitive biases (theory of learning to infer)
- Binz, Gershman, Schulz & Endres (2022) — heuristics from bounded meta-learned inference
- Finn, Abbeel & Levine (2017) — MAML (model-agnostic meta-learning)
- Lake (2019) — compositional generalisation via meta-learning
- Savage (1972) — small vs. large world distinction
- Jones & Love (2011) — critique of rational Bayesian models
- Bromberg-Martin et al. (2010) — inferred value signals in dopamine

**Named models or frameworks**:
- Meta-reinforcement learning (meta-RL)
- Model-agnostic meta-learning (MAML)
- Rational analysis of cognition (Anderson)
- Resource rationality
- Bayesian posterior predictive distribution / Bayes-optimal inference
- Rescorla-Wagner model
- Matching networks / prototypical networks (few-shot classification)
- Episodic meta-reinforcement learning (Ritter et al., 2018)
- Two-step task (Daw et al., 2011)

**Brain regions**:
- Prefrontal cortex (PFC)
- Dopaminergic system
- Hippocampus

**Keywords**:
- meta-learning
- rational analysis of cognition
- Bayes-optimal inference
- resource rationality
- recurrent neural networks
- cognitive biases and heuristics
- model-based reinforcement learning
- algorithmic complexity
- computational complexity
- prefrontal cortex meta-RL
- in-context learning
- domain-general cognitive model
