---
source_file: amengual2022_pfc_multiplexing_behavior.md
title: "The cost of multiplexing: PFC integrates multiple sources of information in non-orthogonal components accounting for behavioral variability"
authors: Julian L Amengual, Fabio Di Bello, Sameh Ben Hadj Hassen, Elaine Astrand, Suliann Ben Hamed
year: 2022
journal: bioRxiv (preprint, posted December 29, 2022)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

FEF neural populations encode multiple task- and behaviour-related parameters simultaneously through non-orthogonal low-dimensional components, and the degree of non-orthogonality directly predicts behavioural interactions between temporal expectation, attentional focus, and reaction time.

---

### Background & motivation

The prefrontal cortex integrates many sources of information during task performance, supported by mixed-selectivity neurons that allow high-dimensional representations. However, evidence suggests the PFC operates in a low-dimensional regime, visiting only a small fraction of its potential state space — which limits encoding capacity. It is unknown how PFC reconciles the need to multiplex multiple information streams with this dimensionality constraint. This paper addresses whether these streams are encoded in orthogonal or non-orthogonal components, and what the behavioural consequences of non-orthogonality are.

---

### Methods

- **Subjects**: Two adult rhesus macaque monkeys (M1, M2).
- **Task**: 100% validity endogenous spatial cue–target detection task with distractors. Monkeys manually released a bar 150–750 ms after a luminance change at the cued location; distractors (identical luminance changes at uncued locations) had to be ignored. The cue-to-target onset asynchrony (CTOA) was randomised from 750 to 3300 ms.
- **Recordings**: Bilateral simultaneous intracranial multiunit activity (MUA) recordings from the frontal eye field (FEF) using two 24-contact Plexon U-probes (848 total contacts across sessions); high-pass filtered at 300 Hz, digitised at 40 kHz.
- **Parameters of interest**: CTOA (temporal expectation), reaction time (RT), attentional focus (TA — distance between decoded attentional spotlight and target), and cued spatial position (POS).
- **Attentional spotlight decoding**: Regularised optimal linear estimator (RegOLE) trained on FEF MUA to decode the 2D spatial locus of attention on single trials; TA computed as Euclidean distance from decoded spotlight to target.
- **Single-unit selectivity analysis**: Friedman test (p < 0.05) to classify each unit as tuned to one or more parameters; mixed-selectivity proportions computed for all parameter pairs.
- **Dimensionality reduction**: Demixed PCA (dPCA; Kobak et al. 2016) applied (a) independently per parameter and (b) simultaneously across all parameters to extract parameter-specific latent components and measure the angle (dot product) between component pairs.
- **Statistical tests**: Spearman correlations, linear and quadratic regression, permutation tests (100 shuffles) for decoding accuracy; Monte Carlo leave-group-out cross-validation (100 iterations).

---

### Key findings

- 68.4% of FEF MUA contacts showed significant activation to cue and target onsets; 65% of active units showed attentional modulation (preferred > anti-preferred location).
- FEF firing rate (pre-target, −200 to 0 ms) was significantly modulated by CTOA (linear, rho = 0.95), RT (linear, rho = 0.92), and TA (quadratic, R² = 0.66).
- 72% of recorded neurons showed mixed selectivity (tuned to more than one parameter); only 27.2% of selective cells were tuned to a single parameter.
- dPCA (parameter-specific): CTOA variance was captured in two orthogonal components — one with a linear activation profile (R² = 0.98 at trial level) correlating with RT, and one with an inverted-U profile (R² = 0.97) correlating with TA. RT was captured in one component (R² = 0.81, linear); TA in one component (R² = 0.75, linear).
- dPCA (simultaneous, all parameters): 70% of total variance explained in the first 10 components. Variance partitioning: trial progression 46%, RT 22%, CTOA 17%, TA 16%.
- CTOA components were significantly non-orthogonal to both the RT and TA components; RT and TA components were orthogonal to each other.
- Behavioural interactions: CTOA predicted RT linearly (R² = 0.84) and TA quadratically (R² = 0.59); CTOA and TA each predicted hit rate (R² = 0.82 each).
- Activation of the first CTOA dPC correlated with RT across sessions (R² = 0.79); activation of the second CTOA dPC correlated with TA (R² = 0.49), directly linking the neural geometry to behaviour.

---

### Computational framework

The paper uses **dimensionality reduction / neural manifold geometry** as its computational framework, specifically demixed principal component analysis (dPCA). The core formalism decomposes high-dimensional population firing rate data into latent components whose variance is attributed to specific task or behavioural parameters, without enforcing orthogonality between components.

Key variables: parameter-specific latent components (neural modes) for CTOA, RT, and TA; the angle (dot product) between pairs of components as a measure of representational overlap. The key assumption is that the neural population operates within a low-dimensional manifold and that the geometry of this manifold — specifically the degree of non-orthogonality between parameter-specific subspaces — determines both encoding capacity and the pattern of cross-parameter behavioural interactions.

---

### Prevailing model of the system under study

The introduction frames FEF/PFC as a region supporting mixed-selectivity coding: individual neurons simultaneously encode multiple task parameters, enabling high-dimensional, approximately orthogonal representations that facilitate downstream readout and the implementation of many cognitive computations (Rigotti et al. 2013; Fusi et al. 2016). Concurrently, the prevailing view holds that PFC population activity is confined to a low-dimensional manifold, limiting the total number of simultaneously encodable information streams to roughly three (Gao et al. 2017). Before this paper, it was assumed that mixed-selectivity cells would tend to implement orthogonal representations when possible, with non-orthogonality being a drawback rather than a deliberate coding strategy. The introduction is explicit that the relationship between this low-dimensional constraint, non-orthogonality, and overt behavioural interactions had not been formalised.

---

### What this paper contributes

The paper demonstrates that FEF simultaneously encodes at least four parameters (spatial position, CTOA, RT, TA) and that the resulting low-dimensional geometry is specifically non-orthogonal between the temporal-expectation components and the behavioural-outcome components. This is not a deficiency but a measurable, structured configuration: the two CTOA components selectively map onto RT and TA respectively, and this mapping is mirrored in the observed behavioural correlations between CTOA, RT, TA, and hit rate. The contribution is thus showing that non-orthogonal coding is a systematic strategy for maximising encoding capacity under a dimensionality constraint, and that this strategy has a precise and predictable behavioural cost — specifically, an impaired capacity to use attentional information independently and an enhanced responsiveness to external stimuli as time in trial advances.

---

### Brain regions & systems

- **Frontal eye field (FEF)** — primary locus of investigation; shown to multiplex spatial attention position, temporal expectation (CTOA), attentional focus (TA), and motor response speed (RT) in non-orthogonal low-dimensional components. Framed as a "hub" region projecting to dlPFC, cingulate, parietal, and posterior cortices.
- **Prefrontal cortex (PFC) broadly** — the paper situates FEF findings within the wider debate about PFC dimensionality and mixed-selectivity coding.

---

### Mechanistic insight

This paper meets both criteria: it formalises an algorithm (non-orthogonal multiplexing in a low-dimensional manifold) and provides neural recordings that specifically link the geometry of that manifold to behavioural outcomes.

- **Computational**: The brain must simultaneously track temporal expectation, spatial attention, and motor preparedness during a cued detection task. Given metabolic and dimensionality constraints on PFC, the problem is to maximise the number of information streams encoded while accepting predictable cross-stream interference.
- **Algorithmic**: FEF population activity is organised into a low-dimensional manifold with parameter-specific subspaces. CTOA is encoded in two components (linear and inverted-U), one of which partially spans the RT subspace and the other the TA subspace (non-orthogonal overlap). This geometric arrangement means that as CTOA increases, the neural state drifts in a direction that simultaneously shifts the RT- and TA-encoding dimensions — producing the observed behavioural co-variations. RT and TA subspaces remain orthogonal, preserving their independent decodability.
- **Implementational**: The paper does not identify specific cell types, neuromodulators, or microcircuit mechanisms. Evidence is at the population level (MUA from multi-contact probes). The anatomical projection targets of FEF are noted as a possible substrate for transmitting this multiplexed code to downstream regions, but this is speculative.

---

### Limitations & open questions

- The study uses MUA rather than isolated single units, which limits inference about the properties of individual neurons contributing to each component.
- Only two monkeys were used, and behavioural performance differed substantially between them (55.6% vs 76.2% hit rate), raising questions about generalisability.
- The causal direction of the relationship between neural geometry and behaviour is not established; it is unclear whether manipulating the angle between components would causally alter behaviour.
- The inverted-U CTOA component is discussed speculatively in terms of curved manifolds and efficient readout (following Okazawa et al. 2021) but this interpretation is not tested directly.
- It remains untested whether non-orthogonality is a deliberate optimisation or an emergent property of circuit constraints.
- The dataset is not publicly available, limiting reproducibility.
- The paper is a preprint and has not undergone peer review at time of posting.

---

### Connections & keywords

**Key citations**:
- Rigotti et al. 2013 (Nature) — importance of mixed selectivity in complex cognitive tasks
- Fusi, Miller & Rigotti 2016 (Curr Opin Neurobiol) — why neurons mix; high dimensionality for higher cognition
- Kobak et al. 2016 (eLife) — demixed principal component analysis (dPCA)
- Amengual et al. 2022 (Nat Commun) — distractibility and impulsivity neural states in FEF; non-orthogonality and attentional gain
- Gaillard et al. 2020 (Nat Commun) — rhythmic prefrontal attentional saccades
- Astrand et al. 2016 (Curr Biol) — direct 2D decoding of covert attention locus from FEF
- Okazawa et al. 2021 (Cell) — representational geometry in parietal cortex; curved manifolds
- Gao et al. 2017 (bioRxiv) — theory of multineuronal dimensionality

**Named models or frameworks**:
- Demixed PCA (dPCA)
- Regularised optimal linear estimator (RegOLE) for attention decoding
- LATER model (linear approach to threshold with ergodic rate) for RT filtering
- Neural manifold / low-dimensional manifold framework

**Brain regions**:
- Frontal eye field (FEF)
- Prefrontal cortex (PFC)

**Keywords**:
- mixed selectivity
- non-orthogonal coding
- low-dimensional neural manifold
- demixed principal component analysis (dPCA)
- temporal expectation
- spatial attention
- attentional focus
- reaction time variability
- multiplexing
- frontal eye field
- population geometry
- cue-to-target onset asynchrony (CTOA)
