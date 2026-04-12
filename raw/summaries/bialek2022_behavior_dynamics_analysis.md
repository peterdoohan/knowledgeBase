---
source_file: bialek2022_behavior_dynamics_analysis.md
paper_id: bialek2022_behavior_dynamics_analysis
title: "On the dimensionality of behavior"
authors:
  - "William Bialek"
year: 2022
journal: PNAS
paper_type: computational
contribution_type: theoretical
keywords:
  - behavioral_dimensionality
  - predictive_information
  - past_future_kernel
  - gaussian_stochastic_process
  - correlation_function
  - maximum_entropy
  - maximum_caliber
  - power_law_correlations
  - effectively_infinite_dimensionality
  - dynamical_systems
  - computational_neuroethology
  - physics_of_behavior
  - dimensionality
  - behavior
---

### One-line summary

Bialek proposes a precise information-theoretic definition of behavioral dimensionality — as the minimum number of features of the past required for maximally predictive forecasting of the future — and shows that this reduces, in tractable cases, to analyzing the rank of a matrix derived from the behavioral correlation function.

---

### Background & motivation

The rapid growth of high-resolution behavioral measurement tools (video tracking, pose estimation, etc.) has produced enormous, high-dimensional datasets of animal movement. A common response is to search for low-dimensional descriptions of posture or movement, motivated by the small number of muscles/joints and by empirical evidence of low-dimensional motor behavior. However, the dynamical systems literature warns that even a single observed variable can reflect higher-dimensional underlying dynamics; the brain generating behavior has many degrees of freedom. The field lacks a rigorous, general definition of what "the dimensionality of behavior" actually means, one that applies comparably across species, behavioral paradigms, and data types (continuous trajectories vs. discrete state sequences). This paper aims to supply that definition.

---

### Methods

This is a theoretical/mathematical paper; no empirical data are collected. The approach proceeds as follows:

- **Gaussian continuous processes**: Models behavior as a Gaussian stochastic process x(t). Constructs the kernel K(t) as the operator inverse of the correlation function C(t), then isolates the past-future coupling matrix K_pf. If K_pf has finite rank D, the system is defined as D-dimensional. Shows formally that if C(t) is a sum of M exponentials, then K_pf has rank M, so D = M.
- **Power-law correlations**: Demonstrates that if C(t) ~ t^{-α} (power-law decay), the rank of K_pf grows without bound with observation window T, making the system "effectively infinite dimensional."
- **Discrete behavioral states**: Extends the framework to binary (Ising) behavioral sequences. Uses maximum entropy (maximum caliber) models consistent with observed mean and two-point correlations to derive a latent continuous variable x(t), then applies the same kernel-rank criterion.
- **General information-theoretic formulation**: Unifies both cases via predictive information I_pred(T; d) — the mutual information between past and future captured by d features of the past. Defines dimensionality as the smallest d at which I_pred(T; d) saturates as T → ∞.
- **Numerical illustration**: Simulates finite-dimensional (3D) and infinite-dimensional (power-law) systems and plots the eigenvalue spectrum of K_pf to illustrate the rank criterion in practice.

---

### Key findings

- The dimensionality of behavior equals the rank of the past-future coupling matrix K_pf derived from the behavioral correlation function — equivalently, the minimum number of features of the past sufficient to capture all predictive information about the future.
- For Gaussian processes: if C(t) is a sum of M exponentials, then the underlying dynamical dimensionality is exactly D = M. Numerical simulations of a 3D system yield exactly three clearly nonzero eigenvalues of K_pf (others below 10^{-10}), stable across observation windows of T = 100Δt and T = 1000Δt.
- Power-law correlations (C(t) ~ t^{-α}) imply effectively infinite dimensionality: the rank of K_pf grows without bound as the observation window increases, and predictive information diverges logarithmically (I_pred ~ log T).
- The discrete-state (Ising/maximum-entropy) case maps exactly onto the continuous-variable case: the dimensionality is again determined by the rank of a kernel, this time derived from the effective temporal interactions J(t) rather than C(t) directly.
- The general definition (minimum sufficient features for prediction) unifies both Gaussian and non-Gaussian behavioral trajectories, and reduces to the rank criterion whenever the underlying dynamics are finite dimensional.
- Distinguishing finite from infinite dimensionality from finite data is hard: sample noise generates a continuous spectrum; random matrix theory is identified as the appropriate tool to separate signal from noise in the eigenvalue spectrum.

---

### Computational framework

**Dynamical systems + information theory + maximum entropy statistical mechanics.**

The core formalism uses:

1. **Dynamical systems**: behavior is modeled as a stochastic dynamical system. The key quantity is the observed trajectory x(t), generated by D coupled Langevin-type equations driven by white noise. Dimensionality = number of independent variables needed to specify the state.

2. **Correlation function analysis**: C(τ) = ⟨x(t)x(t+τ)⟩ is inverted to obtain the kernel K(τ). The past-future block K_pf is analyzed for its rank.

3. **Predictive information**: I_pred(T; d) = mutual information between past and future when d features of the past are used. The dimensionality D is the smallest d for which I_pred saturates at large T. This generalizes the rank criterion beyond Gaussian processes.

4. **Maximum entropy / maximum caliber**: For discrete behavioral states, the minimally-structured model consistent with observed mean and two-point correlations is the maximum entropy model (equivalent to a 1D Ising model with pairwise interactions). This model can be re-expressed as a latent continuous-variable model, linking the discrete and continuous frameworks.

Key assumptions: noise sources are white (i.e., not themselves carriers of hidden memory); behavioral observations are either discretely sampled in time (video frames) or contaminated by white measurement noise (to make predictive information finite).

---

### Prevailing model of the system under study

The paper's introduction reflects a field in transition. The prevailing view, grounded in both classical motor neuroscience and recent computational neuroethology, holds that animal behavior is well described by low-dimensional dynamics: behavioral posture and movement trajectories lie on low-dimensional manifolds, matching the small number of muscles/joints, and consistent with empirical findings from C. elegans, Drosophila, rodents, and primates. Machine learning tools (DeepLabCut, etc.) have operationalized this by automatically extracting a few degrees of freedom from video data.

At the same time, the introduction acknowledges that the dynamical systems literature (Packard et al. 1980; Abarbanel et al. 1993) warns that a single observable time series can encode higher-dimensional structure, and that neural dynamics might themselves be high-dimensional even if motor outputs are low-dimensional. No prior formal definition of behavioral dimensionality is attributed to the existing literature — the paper's implicit claim is that the field has been using the term loosely, relying on heuristics such as PCA variance explained or the number of posture eigenmodes, without a principled theoretical foundation.

---

### What this paper contributes

Before this paper, the field lacked a precise, general definition of behavioral dimensionality that applied equally to continuous and discrete behaviors, and that distinguished finite from genuinely infinite dimensionality. The contribution is threefold:

1. **Formal definition**: dimensionality = rank of the past-future coupling kernel K_pf = minimum number of predictive sufficient statistics. This is grounded in information theory and dynamical systems theory, making it rigorous rather than heuristic.

2. **Tractable recipe**: for Gaussian processes, dimensionality is simply the number of exponential components in C(t) — i.e., the number of nonzero eigenvalues of K_pf. This provides a concrete spectral analysis procedure.

3. **Identifies effectively infinite-dimensional regimes**: power-law behavioral correlations (long debated empirically) are shown to imply infinite dimensionality in a precise sense (diverging predictive information, growing rank). The paper argues these regimes are not just mathematical curiosities but may describe real animal behavior (citing preprint by Alba et al. 2020).

The paper does not provide new empirical findings; rather, it supplies the theoretical scaffolding needed to interpret existing and future dimensionality analyses of behavior.

---

### Brain regions & systems

Not applicable. The paper operates purely at the behavioral/algorithmic level and makes no reference to specific brain regions, circuits, or neural mechanisms. The level of analysis is the time series of observable behavior, abstracted from any anatomical substrate. The framework is explicitly framed as phenomenological — asking "what is it about behavior that we would like to explain?" rather than "how does the brain generate behavior?"

---

### Mechanistic insight

The paper does not meet the bar for this section. It is a purely theoretical contribution: it proposes a formal definition and analysis method for behavioral dimensionality. No neural data (recordings, imaging, lesion, pharmacology) are presented, and the paper deliberately brackets the mechanistic question of how the brain generates behavior. The framework could in principle constrain mechanistic models — e.g., a high behavioral dimensionality would be inconsistent with purely low-dimensional neural manifolds — but no such linking is made here.

---

### Limitations & open questions

- **Finite data problem**: estimating the rank of K_pf from finite behavioral records is challenging. Noise inflates all eigenvalues and can make it difficult to distinguish finite-rank from infinite-rank spectra. Random matrix theory is proposed as a corrective tool but no worked example is provided.
- **Gaussian assumption**: the core spectral recipe applies cleanly only to Gaussian processes. Most real behavioral data (especially discrete state sequences) require the maximum entropy detour, which is computationally more demanding to fit.
- **White noise requirement**: the framework assumes that measurement noise and internal noise sources are white (temporally uncorrelated). Colored noise is equivalent to additional hidden degrees of freedom, potentially inflating apparent dimensionality.
- **No empirical validation**: no real behavioral dataset is analyzed. The tractability of applying this framework to, e.g., worm locomotion or rodent behavioral syllable sequences is undemonstrated.
- **Relation to existing methods**: the paper does not systematically compare its definition to the PCA/variance-explained approaches commonly used in the field, leaving it unclear when the two would give discordant answers.
- **Open question**: does strongly non-Markovian animal behavior (power-law correlations) truly represent infinite-dimensional dynamics, and if so, what neural architecture produces it? This is flagged but not addressed.

---

### Connections & keywords

**Key citations**:
- Stephens et al. 2008 (PLOS Comput. Biol.) — dimensionality of C. elegans behavior
- Berman et al. 2014 (J. R. Soc. Interface) — discrete behavioral states in Drosophila
- Packard et al. 1980 (Phys. Rev. Lett.) — geometry from time series / delay embedding
- Abarbanel et al. 1993 (Rev. Mod. Phys.) — analysis of chaotic data in physical systems
- Bialek, Nemenman, Tishby 2001 (Neural Comput.) — predictive information, complexity, and learning
- Jaynes 1957 (Phys. Rev.) — maximum entropy principle
- Alba, Berman, Bialek, Shaevitz 2020 (arXiv preprint) — strongly non-Markovian animal behavior
- Schneidman et al. 2006 (Nature) — maximum entropy models of neural populations

**Named models or frameworks**:
- Maximum entropy model / maximum caliber
- Predictive information (I_pred)
- 1D Ising model with long-range interactions
- Autoregressive processes

**Brain regions**: None.

**Keywords**: behavioral dimensionality, predictive information, past-future kernel, Gaussian stochastic process, correlation function, maximum entropy, maximum caliber, power-law correlations, effectively infinite dimensionality, dynamical systems, computational neuroethology, physics of behavior
