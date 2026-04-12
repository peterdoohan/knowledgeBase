---
source_file: nishimori2024_feature_learning_benign_overfitting.md
paper_id: nishimori2024_feature_learning_benign_overfitting
title: "Feature learning and generalization error analysis of two-layer linear neural networks for high-dimensional inputs"
authors:
  - "Hayato Nishimori"
  - "Taiji Suzuki"
year: 2024
journal: "Information Geometry"
paper_type: computational
contribution_type: theoretical
keywords:
  - benign_overfitting
  - feature_learning
  - two_layer_linear_neural_network
  - high_dimensional_regression
  - natural_gradient_descent
  - bias_variance_tradeoff
  - overparametrisation
  - interpolation_regime
  - minimum_norm_estimator
  - spectral_decay
  - gradient_descent
  - perturbation_theory
  - feature
  - learning
  - generalization
  - error
  - analysis
  - two
  - layer
  - linear
---

### One-line summary

One-step feature learning in a two-layer linear neural network reduces bias without increasing variance in the high-dimensional interpolation regime, with natural gradient descent (NGD) outperforming vanilla gradient descent (GD) for difficult regression instances where the true signal is not well-aligned with the principal components of the input.

---

### Background & motivation

Deep learning models are empirically observed to generalise well even when overparametrised, a phenomenon called benign overfitting. Prior theoretical work on benign overfitting largely addressed one-layer linear (kernel/random feature) models, which cannot adaptively learn basis functions. A key open question was whether feature learning — the adaptive adjustment of input representations that makes deep networks outperform kernel methods — also supports or is compatible with benign overfitting, particularly in the regime where input dimensionality exceeds sample size (d > n). This paper fills that gap by providing finite-dimensional, non-asymptotic theory for a minimal deep learning model with one step of feature learning.

---

### Methods

- **Model**: fully-connected two-layer linear neural network with N neurons (taken to infinity for analysis), trained by (i) one gradient step on the first layer and (ii) minimum-norm ridge regression on the second layer using held-out or re-sampled data.
- **Three first-layer update rules** compared: (P1) vanilla gradient descent (GD), (P2) natural gradient descent (NGD) or a mixture of NGD and GD controlled by regularisation λ(1), (P3) one-step weighted linear regression.
- **Setting**: finite d, n with d > n (overparametrised/interpolation regime); covariance matrix Σ = diag(λ1,...,λd) with polynomially decaying eigenvalues λi = i^{-(1+α)}.
- **Theoretical analysis**: bias-variance decomposition of L2 predictive error; perturbation theory for eigenvalues/eigenvectors used to derive explicit formulas in the small-step-size regime; separate large-step-size analysis via bounding bias in terms of first-layer estimation error.
- **Numerical validation**: synthetic Gaussian data with n=100, d=200, N=1000 across varying α, k*, σε², λ(1), λ(2) and η; 1000–10000 Monte Carlo replications.

---

### Key findings

- **Feature learning reduces bias without increasing variance**: one-step feature learning (all three update rules) decreases bias relative to one-layer ridge regression, while leaving variance essentially unchanged. This contrasts with preconditioning results (Amari et al. 2021) where bias-variance tradeoffs exist.
- **NGD is superior for difficult instances**: when the true signal direction k* is large (not aligned with leading principal components of the input, α < 0), NGD feature learning reduces bias whereas GD does not. Formally: for polynomially-decaying eigenvalues with α < 0, the threshold on k* for NGD improvement grows as k*^{1+α}, and improvement is substantial as k* → d.
- **GD is superior for easy instances**: when k* is small (signal aligns with dominant input directions), GD achieves greater relative bias reduction than NGD because GD's first-layer estimate is more accurate in that setting.
- **Intermediate gradient direction is optimal**: a mixture of NGD and GD (intermediate λ(1)) can reduce bias beyond either extreme alone by balancing estimation bias and variance in the first layer.
- **Large step size**: bias of GD and WLR feature learning decreases monotonically with step size η when the true signal is sparse; NGD bias is insensitive to η because NGD estimation error is spread isotropically across all directions.
- **Variance invariance**: the rank-1 update to the first-layer weight matrix W0 does not significantly alter the spectral structure of the data covariance, explaining why variance is unchanged by feature learning regardless of step size or update rule.
- **Finite-dimensional generality**: analysis holds for all finite n, d without requiring the proportional limit n/d → const, extending the scope of Ba et al. (2022).

---

### Computational framework

**Framework**: statistical learning theory — bias-variance decomposition, ridge regression, and perturbation theory of eigenvalues/eigenvectors, applied to a two-layer linear neural network.

**What is modelled**: the predictive (L2) error of a minimum-norm interpolating estimator obtained after one gradient step of feature learning in the first layer, followed by ridge regression in the second layer.

**Key variables**:
- Σ: input covariance matrix (diagonal, polynomially decaying eigenvalues indexed by α)
- η: step size for the first-layer update
- λ(1), λ(2): regularisation parameters for the first and second layer respectively
- k*, a*: index and direction of the true sparse signal
- Bias B and Variance V: components of L2 predictive error

**Key assumptions**:
- Sub-Gaussian input distribution; Gaussian noise; infinite-width first layer (N → ∞) for tractable analysis
- Independent re-sampling of second-layer training data (data-splitting approximation; shown qualitatively robust)
- Non-degenerate eigenvalues of Σ required for perturbation analysis in the small-step regime

---

### Prevailing model of the system under study

The paper addresses the theory of overparametrised learning rather than a biological neural system. The prevailing theoretical picture at the time of the paper's contribution was:

1. Benign overfitting — the ability of minimum-norm interpolating estimators to generalise despite zero training error — had been rigorously established for one-layer linear models (Bartlett et al. 2020, Tsigler & Bartlett 2020, Hastie et al. 2022) and random feature models (Mei & Montanari 2022).
2. Deep networks outperform kernel/random-feature methods at appropriate model sizes due to feature learning (Imaizumi & Fukumizu 2019, Suzuki 2019), but this relied on choosing the right model size.
3. It was unclear whether feature learning is compatible with benign overfitting (i.e., large-model generalisation without explicit model selection), especially when d > n.
4. The existing feature-learning analysis by Ba et al. (2022) required a proportional limit (n, d → ∞ at fixed ratio) and showed improvement only when n ≥ d, leaving the high-dimensional n < d case uncharacterised.

---

### What this paper contributes

The paper establishes that one-step feature learning is compatible with and beneficial for benign overfitting in the high-dimensional (d > n) finite regime. Specifically:

- It proves that feature learning reduces bias without inflating variance — refuting the natural conjecture that any preconditioner-like operation trades one for the other.
- It characterises precisely when NGD vs. GD feature learning is preferable in terms of the eigenvalue decay rate α and signal direction k*, providing a clear criterion for method selection.
- It demonstrates that improvement from NGD is greatest for the hardest regression instances (slowly decaying spectra, misaligned signals), which are exactly the settings where standard one-layer ridge regression generalises poorly.
- It extends the feature-learning theory of Ba et al. (2022) to the finite-d, finite-n, d > n setting, showing bias reduction even when d = ω(n).
- It identifies that intermediate gradient directions (between pure NGD and pure GD) can out-perform either extreme, opening a practical design principle for first-layer update rules.

---

### Brain regions & systems

Not applicable. This is a pure mathematical/computational machine learning paper with no anatomical or neural systems focus. The level of analysis is statistical learning theory — population risk of estimators under high-dimensional regression.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight at Marr's levels because it is a theoretical machine learning study with no neural data. It proposes and formally analyses an algorithm (one-step feature learning with various gradient rules), but provides only synthetic numerical experiments, not recordings, imaging, or any other neural evidence.

The paper characterises how one gradient step modifies the spectral structure of the effective input covariance (via a rank-1 update to W0), explaining the bias reduction and variance invariance mechanistically at the algorithmic level of the model, but this is not mapped to any biological neural implementation.

---

### Limitations & open questions

- **Linear networks only**: the analysis is restricted to two-layer linear neural networks with no nonlinear activation function. Generalisation to nonlinear (e.g., ReLU) networks is identified as a key open problem.
- **Finite width**: the theoretical analysis assumes N → ∞. Analysis for finite-width networks (N < ∞) remains open.
- **One gradient step**: only one step of gradient descent is analysed for the first layer. Multi-step and full gradient descent dynamics are not covered.
- **Data-splitting approximation**: second-layer training uses resampled (independent) data, which is not standard practice; the paper shows qualitative robustness but not exact equivalence.
- **Sparse signal assumption**: some key results (Corollaries 3, 4, 7) assume completely sparse true signal a*. Behaviour with dense signals is partially characterised but less explicit.
- **Proportional limit comparison**: the analysis does not give asymptotic rates comparable to Ba et al. (2022) in the proportional limit, making direct quantitative comparison difficult.
- **NGD in practice**: natural gradient descent requires inversion of the input covariance Σ, which is impractical in standard deep learning; the paper does not address how to approximate this efficiently.

---

### Connections & keywords

**Key citations**:
- Tsigler & Bartlett (2020) — benign overfitting in ridge regression (core technical scaffold)
- Ba et al. (2022) — high-dimensional asymptotics of feature learning (direct comparison)
- Amari et al. (2021) — preconditioning and bias-variance tradeoff (key contrast)
- Bartlett et al. (2020) — benign overfitting in linear regression
- Damian et al. (2022) — neural networks learn representations with gradient descent
- Hastie et al. (2022) — surprises in high-dimensional ridge regression
- Mei & Montanari (2022) — generalisation error of random features regression

**Named models or frameworks**:
- Two-layer linear neural network
- Benign overfitting
- Natural gradient descent (NGD)
- Minimum-norm interpolator / ridge regression
- Bias-variance decomposition
- Random feature model

**Brain regions**: Not applicable.

**Keywords**: benign overfitting, feature learning, two-layer linear neural network, high-dimensional regression, natural gradient descent, bias-variance tradeoff, overparametrisation, interpolation regime, minimum-norm estimator, spectral decay, gradient descent, perturbation theory
