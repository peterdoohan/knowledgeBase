---
source_file: "zhang2026_neural_decoding_correlations.md"
paper_id: "zhang2026_neural_decoding_correlations"
title: "Exploiting correlations across trials and behavioral sessions to improve neural decoding"
authors: "Yizi Zhang, Hanrui Lyu, Cole Hurwitz, Shuqi Wang, Charles Findling, Yanchen Wang, Felix Hubert, International Brain Laboratory, Alexandre Pouget, Erdem Varol, Liam Paninski"
year: 2026
journal: "Neuron"
paper_type: "computational"
contribution_type: "methodological"
species: ["mouse", "monkey"]
methods: ["neuropixels", "behavioral_analysis"]
brain_regions: ["hippocampus_ca1", "nucleus_accumbens", "amygdala", "visual_cortex"]
frameworks: ["bayesian_inference"]
keywords: ["neural_decoding", "multi_session_learning", "reduced_rank_regression", "state_space_models", "hidden_markov_models", "trial_to_trial_correlations", "dimensionality_reduction", "neuropixels", "international_brain_laboratory", "empirical_bayes", "interpretable_machine_learning", "brain_wide_mapping", "latent_variable_models", "autoregressive_models", "beta_mixture_models", "exploiting", "correlations", "across", "trials", "behavioral"]
---

### One-line summary

Multi-session reduced-rank regression and state-space models that share neural and behavioral structure across trials and sessions outperform traditional single-trial, single-session decoders on large-scale electrophysiological datasets.

### Background & motivation

Traditional neural decoders operate on single trials within single sessions, ignoring correlations across trials and sessions. However, animals exhibit similar neural patterns when performing the same task, and behavior depends on prior experiences. This paper develops methods to exploit these correlations for improved decoding, offering interpretable alternatives to deep learning approaches.

### Methods

- **Multi-session reduced-rank regression (RRR)**: Factorizes the weight matrix into low-rank neural basis U and shared temporal basis V. RRR(M) shares V across sessions; RRR(MR) further factorizes V into region-specific and shared components.
- **BMM-HMM (beta mixture model with hidden Markov model)**: For binary behaviors, models latent behavioral states s and latent behaviors z using HMM transitions and beta mixture observations.
- **LG-AR1 (linear Gaussian autoregressive model)**: For continuous behaviors, models latent behavior z with first-order autoregressive dynamics and linear-Gaussian observations.
- **Empirical Bayes priors**: Multi-session versions learn parameter distributions from training sessions to constrain inference on test sessions.
- **Datasets**: IBL Neuropixels (433 sessions, 270 brain regions, mice), Allen Institute visual coding (58 sessions, mice), primate random target-reaching (Utah arrays, monkey).

### Key findings

- RRR(M) outperforms single-session RRR, ridge regression, and MLP baselines across choice (AUC), prior (Pearson correlation), wheel speed (R²), and whisker motion energy (R²) decoding in IBL data.
- Combined decoder (RRR(M) + multi-session BMM-HMM/LG-AR1) achieves highest performance for choice and prior.
- Multi-session RRR(M) outperforms multi-session linear and MLP baselines, showing gains come from both multi-session training and structured model design.
- RRR provides interpretability: neural basis U identifies task-relevant neurons (choice-selective firing patterns for important neurons, non-selective for unimportant).
- Brain-wide mapping (270 regions) reveals behaviorally relevant timescales: nucleus accumbens (ACB) and basomedial amygdala (BMA) show prolonged activation; hindbrain regions show shorter activation durations.
- Generalization across datasets: RRR(M) improves decoding on IBL trial-unaligned data, Allen Institute visual coding (orientation, running speed), and primate reaching task (finger velocity).
- BMM-HMM successfully infers latent states (engaged/disengaged) in Allen licking behavior.

### Computational framework

**Reduced-rank regression**: The framework factorizes the decoding weight matrix W into low-rank components U (neural basis, N × R) and V (temporal basis, R × T × P). This reduces parameters from NT to R(N + T), where R < min(N, T). The model maximizes Corr(X, d)² × Var(d), balancing neural-behavioral correlation with behavioral variance capture. Multi-session sharing of V enables transfer across sessions with different neurons.

**State-space models**: For binary behaviors, BMM-HMM uses hidden Markov models with beta mixture observations to model latent behavioral states and their transitions. For continuous behaviors, LG-AR1 uses first-order autoregressive dynamics with linear-Gaussian observations. Both employ empirical Bayes to share dynamic structure across sessions.

### Prevailing model of the system under study

Prior to this work, the field relied on single-trial, single-session decoders (linear regression, ridge, L2-regularized logistic) that treated each trial independently. While reduced-rank regression existed for neural encoding, its application to decoding with factorized neural/temporal bases was not established. Multi-session approaches typically required explicit neural alignment (CCA, hyperalignment) or complex black-box models (MLPs, transformers). State-space models like GLM-HMMs modeled behavior but did not integrate neural decoding with across-session sharing.

### What this paper contributes

This paper introduces a family of interpretable, efficient models for multi-session neural decoding:

1. **Multi-session RRR**: Shares temporal structure across sessions while allowing session-specific neural bases, enabling decoding without neuron alignment. The multi-region variant captures region-specific temporal dynamics.

2. **BMM-HMM and LG-AR1**: State-space models that exploit trial-to-trial correlations in binary and continuous behaviors, with empirical Bayes priors enabling cross-session parameter sharing.

3. **Interpretability**: Unlike black-box deep learning, RRR provides explicit neural and temporal bases, enabling identification of task-relevant neurons and brain-wide activation timescales.

4. **Scalability**: Linear models train orders of magnitude faster than transformers (2 hours vs. 2 days on 100 sessions), with competitive or superior performance.

5. **Generalization**: Methods work across trial-aligned and unaligned data, different species (mice, monkeys), recording hardware (Neuropixels, Utah arrays), and tasks (decision-making, visual coding, reaching).

### Brain regions & systems

- **Posterior thalamic nucleus (PO)**: Choice decoding; important neurons show choice-selective firing.
- **Lateral posterior nucleus (LP)**: Choice and prior decoding; choice-selective neurons identified.
- **Dentate gyrus (DG)**: Choice decoding; largest improvement in decodable information relative to linear baseline.
- **Cornu ammonis (CA1)**: Choice and prior decoding; choice-selective neurons identified.
- **Anterior visual cortex (VISa)**: Choice and prior decoding; choice-selective neurons identified.
- **Gigantocellular reticular nucleus (GRN)**: Short activation duration for choice.
- **Motor cortex (MOp)**: Peak activation around 1.5s for choice (reaction time).
- **Nucleus accumbens (ACB)**: Prolonged activation for choice.
- **Amygdala complex (CEA)**: Moderate activation duration for choice.
- **Basomedial amygdala (BMA)**: Prolonged activation for choice.

### Mechanistic insight

This paper does not meet the full mechanistic insight bar. While it presents algorithms (RRR, BMM-HMM, LG-AR1) and validates them on neural data, it does not provide neural data that specifically support the model's algorithmic variables over alternatives. The RRR identifies behaviorally relevant neurons and timescales, but does not establish how these neural representations are computed or implemented at a circuit level. The state-space models infer latent behavioral states but do not link these to specific neural mechanisms. The contribution is primarily methodological—providing efficient, interpretable decoders—rather than mechanistic.

### Limitations & open questions

- Multi-session RRR assumes shared temporal bases across sessions, which may not hold when animals are at different learning stages or performance levels.
- Scaling behavior is task-dependent: whisker motion energy improves with more sessions, but choice, prior, and wheel speed plateau or decline after 20-40 sessions.
- RRR does not always outperform nonlinear MLPs (e.g., primate reaching task), though it provides interpretability advantages.
- BMM-HMM is designed for binary variables; extension to multi-class requires one-vs-all classification.
- Models assume trial-to-trial correlations exist; performance gains depend on the strength of these correlations in the data.
- Future work could incorporate nonlinear time series models, dynamical systems, and additional data modalities (LFP, calcium imaging).

### Connections & keywords

- **Key citations**: Gallego et al. 2018 (shared neural manifolds), Ashwood et al. 2022 (GLM-HMM for decision states), Kobak et al. 2016 (demixed PCA), Sani et al. 2021 (PSID), Pandarinath et al. 2018 (LFADS), Ye et al. 2023 (Neural Data Transformer), Safaie et al. 2023 (preserved neural dynamics across animals).
- **Named models or frameworks**: Reduced-rank regression (RRR), multi-session RRR (RRR(M)), multi-region RRR (RRR(MR)), beta mixture model HMM (BMM-HMM), linear Gaussian AR1 (LG-AR1), Kalman smoother, expectation-maximization (EM), empirical Bayes, hidden Markov model (HMM).
- **Brain regions**: Posterior thalamic nucleus (PO), lateral posterior nucleus (LP), dentate gyrus (DG), cornu ammonis (CA1), anterior visual cortex (VISa), gigantocellular reticular nucleus (GRN), motor cortex (MOp), nucleus accumbens (ACB), amygdala complex (CEA), basomedial amygdala (BMA), olfactory bulb, cerebellum, thalamus, cortex, hippocampus, hindbrain, forebrain, midbrain.
- **Keywords**: neural decoding, multi-session learning, reduced-rank regression, state-space models, hidden Markov models, trial-to-trial correlations, dimensionality reduction, Neuropixels, International Brain Laboratory, empirical Bayes, interpretable machine learning, brain-wide mapping, latent variable models, autoregressive models, beta mixture models.
