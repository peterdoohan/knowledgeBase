---
source_file: "lowet2020_distributional_reinforcement_brain.md"
paper_id: "lowet2020_distributional_reinforcement_brain"
title: "Distributional Reinforcement Learning in the Brain"
authors: "Adam S. Lowet, Qiao Zheng, Sara Matias, Jan Drugowitsch, Naoshige Uchida"
year: 2020
journal: "Trends in Neurosciences"
paper_type: "review"
contribution_type: "review"
species: ["mouse"]
methods: ["lesion"]
brain_regions: ["prefrontal_cortex", "anterior_cingulate_cortex", "orbitofrontal_cortex", "striatum", "ventral_striatum", "nucleus_accumbens", "ventral_tegmental_area", "substantia_nigra", "amygdala"]
frameworks: ["reinforcement_learning", "temporal_difference_learning"]
keywords: ["distributional", "reinforcement", "learning", "brain"]
key_citations: ["schultz1997_neural_substrate_reward_pred"]
---

### One-line summary

This review synthesises the mathematical foundations of distributional reinforcement learning (RL) and evaluates emerging neurobiological evidence that VTA dopamine neurons collectively encode the full distribution of future rewards via an expectile code, rather than only the mean.

---

### Background & motivation

Classical studies established a close correspondence between VTA dopamine neuron firing and the reward prediction error (RPE) term of temporal difference (TD) RL — that is, the difference between actual and predicted mean reward. However, representing only the mean discards information about reward variability that could be behaviourally important, particularly when risk preferences change. Distributional RL, a family of algorithms originally developed for AI, learns the entire distribution of future returns rather than just its mean, and substantially improves agent performance on benchmark tasks. A recent empirical study (Dabney et al., 2020, Nature) suggested the brain may implement a version of these algorithms in the dopamine system, creating an opportunity to re-examine the heterogeneity of dopamine neuron responses through a normative distributional lens.

---

### Methods

This is a narrative review covering:

- Mathematical derivation of distributional RL algorithms from the Rescorla-Wagner learning rule and temporal difference learning, unified under a regression / loss-function minimisation framework.
- Exposition of quantile regression and expectile regression as two biologically plausible implementations of distributional RL, derived via stochastic gradient descent on asymmetric loss functions.
- Review of the key empirical study (Dabney et al., 2020) testing distributional RL predictions in optogenetically tagged VTA dopamine neurons in mice performing a variable-reward odour task.
- Discussion of biological plausibility: asymmetric scaling factors, independent dopamine-value predictor loops, plasticity mechanisms in striatum (D1/D2 circuitry), and modulatory roles of habenula, RMTg, serotonin, norepinephrine, and frontal cortices.
- Comparison with alternative population coding frameworks (probabilistic population codes, distributed distributional codes).

---

### Key findings

- Distributional RL requires only two simple modifications to the standard Rescorla-Wagner update rule: (1) binarising the prediction error (using only its sign), which drives convergence to quantiles; (2) using asymmetric learning rates for positive vs. negative RPEs (α⁺ ≠ α⁻), which determines which quantile or expectile each value predictor converges to.
- A population of value predictors with diverse asymmetric scaling factors τᵢ = α⁺ᵢ/(α⁺ᵢ + α⁻ᵢ) collectively encodes the full reward distribution via a nonparametric quantile (or parametric expectile) code.
- Dabney et al. (2020) found that optogenetically tagged VTA dopamine neurons in mice show diverse but reliable reversal points (reward magnitudes that elicit zero RPE), which tiled a wide range and were positively correlated with each neuron's asymmetric scaling factor — the key signature predicted by distributional RL (linear regression P = 8.1 × 10⁻⁵).
- The asymmetric scaling factors across the dopamine population spanned the full [0, 1] interval reliably (one-way ANOVA F(38,234) = 2.93, P = 4 × 10⁻⁷).
- Decoding the full reward distribution from the population expectile code successfully recovered the actual reward distribution, showing that the structured heterogeneity — not random noise — carries distributional information.
- The performance advantage of distributional RL in AI does not arise from changed action-selection policies but from richer state representations in hidden layers, which may have analogues in the brain.
- Lesions of the lateral habenula or RMTg preferentially reduce responses to negative RPEs, making animals behaviourally "optimistic", consistent with these structures shaping asymmetric scaling factors.
- L-DOPA treatment (but not untreated Parkinson's disease) impairs performance on the Iowa Gambling Task, consistent with disruption of a distributional code in the dopamine system.

---

### Computational framework

The framework is distributional reinforcement learning, situated within the broader temporal difference / Rescorla-Wagner RL tradition.

Key formalisation:

- Each value predictor Vᵢ maintains an estimate of a particular statistic (quantile or expectile) of the reward distribution, not the mean.
- Learning is driven by an asymmetric prediction error: the update increments or decrements Vᵢ using learning rates α⁺ᵢ (positive RPEs) and α⁻ᵢ (negative RPEs). The ratio τᵢ = α⁺ᵢ/(α⁺ᵢ + α⁻ᵢ) determines which quantile (or expectile) Vᵢ converges to.
- For quantiles: the loss function is the asymmetric absolute error; the update uses only the sign of the RPE, scaled by asymmetric constants.
- For expectiles: the loss function is the asymmetric squared error; the update retains the full RPE magnitude, scaled asymmetrically.
- Both can be derived as instances of stochastic gradient descent on their respective loss functions, which the authors argue is biologically plausible for single-layer (Rescorla-Wagner) settings.
- In the TD (multi-step) generalisation, the distributional Bellman equation replaces the scalar value with a return distribution Z(sₜ), and the distributional TD error requires sampling from Z(sₜ₊₁), raising additional challenges for biological implementation.

---

### Prevailing model of the system under study

Before distributional RL, the dominant model of the dopamine system in reward learning held that midbrain dopamine neurons (particularly VTA neurons projecting to nucleus accumbens) uniformly signal scalar RPEs: the difference between actual and mean expected reward. This view, strongly supported by Schultz et al. (1997) and subsequent work, treated observed heterogeneity in dopamine neuron responses as noise or irrelevant variation around a common signal. The field acknowledged that dopamine neurons had diverse projection targets and some variability in firing, but interpreted the average response function as the functionally meaningful signal. The implicit computational model was that the brain learns the mean reward (or mean discounted future reward in TD terms), with the RPE serving as a teaching signal to update this single scalar estimate.

---

### What this paper contributes

The review establishes that the structured heterogeneity of dopamine neuron RPE responses — previously treated as noise around a common mean signal — can be reinterpreted as a normative computational feature: a population-level code for the full reward distribution. Specifically, it shows that:

1. The mathematical machinery of distributional RL is simple, biologically plausible, and unifiable under a regression framework.
2. Empirical data from Dabney et al. (2020) support the prediction that asymmetric scaling factors and reversal points are positively correlated across VTA neurons — a signature that distinguishes distributional RL from classical mean-coding RL.
3. The full reward distribution can be decoded from the population expectile code, demonstrating that the heterogeneity is structured and informative rather than random.

The review also identifies a set of open questions and future experimental predictions, and draws connections to downstream plasticity mechanisms (D1/D2 striatal circuits), neuromodulatory gain control (serotonin, norepinephrine), and frontal modulation of distributional codes. It positions distributional RL as a normative framework for re-analysing existing dopamine datasets and designing new experiments.

---

### Brain regions & systems

- **Ventral tegmental area (VTA)** — primary focus; proposed locus of distributional RPE coding via a population of dopamine neurons with diverse asymmetric scaling factors.
- **Substantia nigra pars compacta (SNc)** — mentioned as the other major site of dopamine neurons; less central to the distributional RL argument here.
- **Nucleus accumbens (ventral striatum)** — primary downstream target of VTA dopamine neurons discussed; proposed to receive and implement value predictions (Vᵢ) that feed back to dopamine neurons.
- **Dorsal striatum** — mentioned in the context of dopamine axon branching and topographic organisation of optimistic/pessimistic neurons.
- **Lateral habenula** — lesions preferentially reduce negative RPE responses and produce "optimistic" behaviour, suggesting a role in shaping the asymmetric scaling factor.
- **Rostromedial tegmental nucleus (RMTg)** — GABAergic input to dopamine neurons; lesions reduce negative RPE responses; proposed contributor to asymmetric scaling via inhomogeneous inhibitory projections.
- **Prefrontal cortex / anterior cingulate cortex / orbitofrontal cortex** — proposed to modulate overall learning rate gain and potentially bias distributional codes toward more optimistic or pessimistic value predictors under uncertainty.
- **Amygdala** — mentioned as a dopamine projection target; not a primary focus.

---

### Mechanistic insight

This paper partially meets the bar. It reviews a computational algorithm (distributional RL with asymmetric learning rates) and discusses neural data (from Dabney et al., 2020) that link specific model variables (reversal points, asymmetric scaling factors τᵢ) to measured dopamine neuron activity. The correlation between reversal points and asymmetric scaling factors across individual neurons is a specific, quantitative prediction of the distributional RL algorithm that is supported over the null hypothesis of homogeneous mean-coding.

Mapping onto Marr's three levels:

- **Computational**: The brain needs to represent not only the expected reward but the full distribution of future returns, to support risk-sensitive decisions and efficient state representation learning.
- **Algorithmic**: A population of value predictors, each updated by an asymmetric RPE signal (α⁺ ≠ α⁻), collectively encodes quantiles or expectiles of the return distribution. Dopamine neuron diversity in asymmetric scaling factors implements this population code; each neuron's reversal point corresponds to its assigned expectile.
- **Implementational**: The asymmetry may arise from: (i) differential sensitivity of positive vs. negative RPE responses shaped by lateral habenula and RMTg inputs; (ii) intrinsic membrane properties (e.g., responses to hyperpolarising current) varying across dopamine neurons; (iii) D1- vs. D2-type receptor expression in downstream striatal neurons differentially processing positive and negative dopamine transients.

The physical implementation is discussed at a relatively coarse level; the review identifies these mechanisms as plausible but not yet definitively demonstrated. Topographic organisation of optimistic/pessimistic dopamine neurons and their striatal targets is proposed but not yet established.

---

### Limitations & open questions

- The expectile decoding in Dabney et al. (2020) relies on data from mice performing a task with a restricted reward distribution; whether the same distributional code generalises across varied environments and reward distributions remains untested.
- Whether asymmetric scaling factors are consistent for individual dopamine neurons across different reward distributions (a key model prediction) has not yet been experimentally verified.
- The mechanism establishing diversity of asymmetric scaling factors during development is unknown — it may arise from stochastic wiring or from specific developmental programmes.
- The assumption of independent value-predictor loops (no crosstalk between channels) is biologically unrealistic; the review notes that topographic organisation could partially preserve distributional coding under crosstalk, but this has not been tested in detail.
- Generalisation from the Rescorla-Wagner (single-step) to the full TD (multi-step) setting raises unsolved problems: distributional TD errors require sampling from the successor state's return distribution, which is not locally available and may be computationally expensive.
- It is unclear whether quantile/expectile codes outperform simpler parametric codes (e.g., encoding only mean and variance) or probabilistic population codes (PPCs/DDCs) for specific behavioural tasks.
- The relationship between distributional RL and other sources of uncertainty in RL (state uncertainty, policy uncertainty, perceptual uncertainty) remains unexplored.
- Clinical implications (anxiety, depression, addiction, pathological gambling under L-DOPA) are speculative and require direct testing.
- Whether distributional codes exist in brain regions beyond the dopamine system and how they interact with other population coding schemes is unknown.

---

### Connections & keywords

**Key citations**:
- Dabney, W. et al. (2020) — "A distributional code for value in dopamine-based reinforcement learning." *Nature* 577, 671–675. (The primary empirical paper reviewed.)
- Dabney, W. et al. (2018) — Distributional RL with quantile regression. AAAI. (Key algorithmic source.)
- Bellemare, M.G. et al. (2017) — Categorical distributional RL (C51). ICML. (Other key algorithmic source.)
- Schultz, W. et al. (1997) — RPE in dopamine neurons. *Science*.
- Rescorla, R.A. and Wagner, A.R. (1972) — The RW learning rule.
- Sutton, R.S. and Barto, A.G. (1998) — *Reinforcement Learning: An Introduction*.
- Eshel, N. et al. (2016) — Dopamine neurons share common response function. *Nature Neuroscience*.
- Tian, J. and Uchida, N. (2015) — Habenula lesions and dopamine optimism. *Neuron*.
- Ma, W.J. et al. (2006) — Probabilistic population codes. *Nature Neuroscience*.
- Tversky, A. and Kahneman, D. (1992) — Cumulative prospect theory.

**Named models or frameworks**:
- Distributional reinforcement learning (distributional RL)
- Quantile regression (QR-DQN)
- Expectile regression
- Deep Q-Network (DQN)
- Rescorla-Wagner (RW) rule
- Temporal difference (TD) learning
- Distributional Bellman equation
- Probabilistic population codes (PPCs)
- Distributed distributional codes (DDCs)
- Cumulative prospect theory
- Iowa Gambling Task (IGT)

**Brain regions**:
- Ventral tegmental area (VTA)
- Substantia nigra pars compacta
- Nucleus accumbens (ventral striatum)
- Dorsal striatum
- Lateral habenula
- Rostromedial tegmental nucleus (RMTg)
- Prefrontal cortex
- Anterior cingulate cortex
- Orbitofrontal cortex

**Keywords**:
- distributional reinforcement learning
- reward prediction error
- dopamine neuron heterogeneity
- expectile coding
- quantile regression
- asymmetric learning rates
- population code reward distribution
- VTA dopamine neurons
- temporal difference learning
- reward distribution decoding
- risk-sensitive decision making
- mesostriatal dopamine pathway
