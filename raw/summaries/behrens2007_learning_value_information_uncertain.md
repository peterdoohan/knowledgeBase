---
source_file: behrens2007_learning_value_information_uncertain.md
title: "Learning the value of information in an uncertain world"
authors: Timothy E J Behrens, Mark W Woolrich, Mark E Walton, Matthew F S Rushworth
year: 2007
journal: Nature Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Human subjects track environmental volatility in a Bayesian-optimal manner and dynamically adjust their reinforcement learning rate accordingly, with anterior cingulate cortex (ACC) BOLD signal during outcome monitoring reflecting the estimated volatility that drives this learning rate modulation.

---

### Background & motivation

Reinforcement learning models require a learning rate (alpha) that determines how strongly each new outcome updates current value estimates, but how or whether this learning rate changes adaptively has remained unclear — it is typically treated as a fixed free parameter fitted to data. Bayesian accounts of learning suggest that the learning rate should depend on environmental volatility: in a rapidly changing (volatile) environment, recent outcomes are more informative and alpha should be high; in a stable environment, distant experience remains useful and alpha should be low. Despite theoretical proposals, direct evidence that humans modulate their learning rate in response to volatility, and the neural mechanism enabling this, had been lacking.

---

### Methods

- **Study type**: Two linked experiments — one behavioural, one fMRI
- **Subjects**: Experiment 1 — 18 human subjects (9 male, aged 18–32); Experiment 2 — 18 subjects scanned with fMRI
- **Task**: A probabilistic binary choice task (blue vs. green rectangles; one-armed bandit variant) in which reward probabilities switched between stable (75% correct, 120 trials) and volatile phases (80% correct, switching every 20–40 trials, ~120–170 trials). Reward magnitudes varied independently of probabilities, inducing some choices of the less-probable option.
- **Bayesian learner model**: Hierarchical Bayesian model with three latent variables — reward probability r, volatility v, and a control parameter k governing changes in volatility. The model updates estimates of all three parameters trial-by-trial given only the current observation; no memory of individual past outcomes is required. This model was compared against standard reinforcement learning (delta rule) models with fixed or phase-specific learning rates.
- **Behavioural analysis**: Delta-rule learning rate alpha estimated by fitting to subjects' choices separately in stable and volatile phases.
- **fMRI analysis**: BOLD signal modelled with seven regressors including trial phases (decide, interval, monitor) and their interactions with Bayesian-estimated volatility. Region-of-interest analyses on ACC local maxima. Ten potential confound regressors tested (reward attained, switch trials, predicted value, reaction time, prediction error, error likelihood, local reward variance, value difference between options, etc.).

---

### Key findings

- Subjects showed significantly higher learning rates during the volatile phase than the stable phase (paired t(17) = 2.91, P < 0.005), independent of block order.
- The Bayesian learner, with no free learning rate parameters, predicted subject decisions significantly better than delta-rule models with 18 or 36 free parameters (one or two learning rates per subject).
- In fMRI, a region in the ACC (MNI: x = –6, y = 26, z = 34 mm; max Z = 4.2) was the only region surviving correction for multiple comparisons in the monitor × volatility interaction, indicating that ACC BOLD signal during outcome observation scales with estimated environmental volatility.
- The volatility-related ACC signal was robust to inclusion of all ten confound regressors; none of the confounds could explain the volatility-related signal.
- Individual differences: subjects with a larger volatility-related ACC response in the outcome-monitoring period had higher mean learning rates overall (r² = 0.27, P < 0.01 at peak; max r² = 0.32).
- Both estimated volatility and variance in the posterior distribution on reward rate r independently contributed to the ACC BOLD signal; when included together, each survived the inclusion of the other.
- At an uncorrected threshold, a focal VTA activation reflected expected reward probability during the interval phase (not the volatility regressor), consistent with dopaminergic prediction signals.

---

### Computational framework

**Bayesian inference / hierarchical generative model**

The paper formalises learning as inference in a hierarchical generative model:
- At the lowest level, the observed outcome y on each trial is Bernoulli-distributed with probability r.
- r is itself dynamic, varying according to a volatility parameter v.
- v changes according to a higher-level control parameter k.

The Bayesian learner computes the joint posterior over r, v, and k, updated at each trial using only the previous trial's posterior and the current observation (no replay of history needed). Crucially, the effective learning rate on r is determined by the posterior variance on r, which is itself driven by the estimated volatility v. High volatility widens the posterior on r, increasing the weight given to each new observation (i.e., increasing alpha). This provides a formal, parameter-free account of why and how learning rates should fluctuate.

The framework explicitly models two forms of uncertainty: expected uncertainty (variance in r given current volatility estimate) and unexpected uncertainty (changes in volatility itself), aligning with Yu and Dayan's (2005) theoretical distinction.

---

### Prevailing model of the system under study

The paper addresses two interlinked prevailing models. First, in learning theory and neuroeconomics, the dominant framework was standard reinforcement learning with a fixed or at best empirically fitted learning rate — the learning rate was treated as a parameter characterising an individual but not as a dynamic variable the brain actively computes. Second, for ACC function, the dominant interpretations emphasised error detection (firing to errors or error likelihood), conflict monitoring (response conflict driving attention), or arousal — all tied primarily to the decision and anticipation phases rather than outcome integration. A complementary view held that ACC was involved in updating action values, but the specific computational variable it tracked was unclear. The paper frames itself against both: it challenges fixed-alpha RL accounts of behaviour and challenges conflict/error-likelihood accounts of ACC, while building on lesion evidence (Kennerley et al. 2006) showing that ACC-lesioned macaques rely only on the single most recent outcome, implying that ACC is necessary for integrating outcome history.

---

### What this paper contributes

The paper establishes three interconnected empirical facts not previously demonstrated:

1. **Behavioural optimality**: Human subjects do not use a fixed learning rate — they adaptively adjust it in a manner quantitatively consistent with a parameter-free Bayesian learner tracking environmental volatility.
2. **Neural correlate of volatility**: The ACC specifically encodes estimated environmental volatility at the moment of outcome observation, and this signal cannot be reduced to any of ten alternative variables previously proposed to explain ACC activity.
3. **ACC signal predicts individual differences in learning**: Between-subject variation in the ACC volatility response predicts between-subject variation in learning rate, providing a direct link from neural signal to behavioural parameter.

Together, these results give a formal computational account of how the brain weights different experiences when learning — volatility is the key signal, ACC is the neural locus at which this signal is used to modulate information integration, and the projection from ACC to ventral striatum is the proposed route through which this modulates prediction-error-driven value updating.

---

### Brain regions & systems

- **Anterior cingulate cortex (ACC)** — primary locus of volatility-related BOLD signal during outcome monitoring; proposed to gate learning rate by tracking environmental volatility; lesion evidence (macaques) also implicates it in multi-trial outcome integration. Rostral ACC activated in the monitor phase; caudal ACC activated in the decide phase.
- **Ventral tegmental area (VTA)** — uncorrected activation correlating with expected reward probability during the interval phase; interpreted as consistent with dopaminergic reward prediction signals (not the main finding).
- **SMA/pre-SMA boundary** — uncorrected activation for expected reward probability, co-localised with prediction error signal.
- **Ventral striatum** — cited as the proposed downstream target of ACC projections that would allow the volatility-driven learning rate to modulate prediction-error-based value updating (anatomical hypothesis, not directly measured).

---

### Mechanistic insight

The paper meets both criteria: it formalises an algorithm (the Bayesian hierarchical update that drives learning rate via estimated volatility) and provides neural imaging data (ACC BOLD) that specifically supports this algorithm over ten alternative accounts.

- **Computational level**: The brain must solve the problem of determining how much weight to give each new piece of information for predicting future outcomes. This requires inferring the stability (volatility) of the reward environment, because the informational value of recent versus distal outcomes depends on how quickly the environment changes.
- **Algorithmic level**: The brain maintains a posterior distribution over reward probability r, volatility v, and the rate of change of volatility k. At each trial outcome, it updates this joint posterior using a Bayesian update rule. The effective learning rate is determined by the posterior variance on r (which is in turn a function of estimated v). The key representations are the volatility estimate and the uncertainty in the reward rate estimate.
- **Implementational level**: The ACC BOLD response during outcome monitoring scales with the Bayesian volatility estimate and the variance on r, and individual differences in this ACC response predict individual differences in learning rate. The anatomical ACC-to-ventral-striatum projection is proposed as the route by which ACC modulates how strongly prediction errors update value estimates in the striatum. The paper does not identify specific cell types, neuromodulators, or connectivity at the synaptic level, so the implementational account is incomplete.

---

### Limitations & open questions

- The fMRI experiment had far fewer trials (120) than the behavioural experiment, so the learning rate change between phases was only a trend in the scanner sample.
- The ACC BOLD signal is a correlate of volatility during outcome monitoring; the study does not demonstrate that ACC activity is causally necessary for volatility tracking in humans (this is inferred from macaque lesion data).
- The paper does not characterise autonomic correlates of volatility detection, which would help distinguish whether ACC volatility responses reflect arousal or true learning-rate computation.
- The Bayesian model assumes continuous variation in reward probability, whereas the task used discrete probability levels; however, the paper shows this assumption is not critical because an abrupt-change alternative model produces equivalent behavioural predictions.
- The mechanistic link from ACC volatility signal to downstream learning rate modulation (via ACC-striatum projections) is anatomically motivated but not directly tested in this study.
- Relationship to neuromodulatory systems (norepinephrine for unexpected uncertainty, acetylcholine for expected uncertainty — as per Yu & Dayan 2005) is discussed but not tested.
- Between-subject correlations between ACC response and learning rate (r² ≈ 0.27–0.32) are modest, leaving substantial unexplained variance.

---

### Connections & keywords

**Key citations**:
- Rescorla & Wagner (1972) — delta learning rule
- Sutton & Barto (1998) — reinforcement learning framework
- Yu & Dayan (2005) — expected and unexpected uncertainty, norepinephrine and ACh
- Kennerley et al. (2006) — ACC lesions in macaques and multi-trial outcome integration
- Doya (2002) — metalearning and neuromodulation
- Fiorillo, Tobler & Schultz (2003) — dopamine encoding of reward probability
- Aston-Jones & Cohen (2005) — locus coeruleus-norepinephrine and adaptive gain

**Named models or frameworks**:
- Rescorla-Wagner / delta rule
- Bayesian hierarchical learner (three-level: r, v, k)
- Probability-tracking task (one-armed bandit variant)

**Brain regions**:
- Anterior cingulate cortex (ACC)
- Ventral tegmental area (VTA)
- SMA/pre-SMA
- Ventral striatum (anatomical hypothesis only)

**Keywords**:
- environmental volatility
- adaptive learning rate
- Bayesian reinforcement learning
- anterior cingulate cortex
- reward uncertainty
- outcome monitoring
- hierarchical Bayesian inference
- prediction error
- probabilistic decision-making
- fMRI
- expected uncertainty vs. unexpected uncertainty
- individual differences in learning
