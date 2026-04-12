---
source_file: "bongioanni2021_novel_choice_neural.md"
paper_id: "bongioanni2021_novel_choice_neural"
title: "Activation and disruption of a neural mechanism for novel choice in monkeys"
authors: "Alessandro Bongioanni, Davide Folloni, Lennart Verhagen, J\u00e9r\u00f4me Sallet, Miriam C. Klein-Fl\u00fcgge, Matthew F. S. Rushworth"
year: 2021
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human", "macaque", "monkey"]
methods: ["fmri", "repetition_suppression", "computational_modeling", "behavioral_analysis"]
brain_regions: ["entorhinal_cortex", "prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex", "striatum"]
keywords: ["activation", "disruption", "neural", "mechanism", "novel", "choice", "monkeys"]
---

### One-line summary

Macaque medial frontal cortex (MFC) supports novel value-based decisions via a grid-cell-like hexagonal code representing reward magnitude and probability in an abstract two-dimensional value space, and its causal disruption with transcranial ultrasound selectively impairs the multiplicative integration of option attributes during novel choice.

---

### Background & motivation

Value-based decision-making research in animals has largely focused on circuits trained over thousands of trials, particularly orbitofrontal cortex (OFC), which encodes incrementally learned option values. Human neuroimaging studies, however, consistently find decision-related activity in medial frontal cortex (MFC), possibly because human paradigms require participants to infer novel option values from component attributes rather than recall values from long training. This gap raises the question of whether separate neural circuits mediate familiar versus novel choice and whether non-human primates possess a comparable inferential decision mechanism. The paper asks whether macaques can make first-time decisions by inferring novel option values from previously experienced component features, and identifies the neural substrate and computational mechanism underlying this ability.

---

### Methods

- **Subjects**: 4 male rhesus macaques (experiments 1 and 2); 3 macaques (experiment 3).
- **Training**: Monkeys learned two one-dimensional stimulus sets over ~13,000 trials across 3 months: set 1 cued reward magnitude (1–10 drops, fixed probability 0.6) via colour; set 2 cued reward probability (0.1–1.0, fixed magnitude 5 drops) via dot number. Training stimuli covered only part of the 2D magnitude × probability space.
- **Experiment 1 (fMRI + choice)**: 12 sessions × 180 binary choice trials per monkey. Factorial design: familiarity (familiar vs. novel options) × dimensionality (consistent, one-dimensional, inconsistent). Novel options were untrained combinations in the unexplored region of value space. fMRI (1.5 mm isotropic, macaque 7T-equivalent setup) acquired during task. Whole-brain univariate GLMs tested for value comparison signals (chosen minus unchosen value; GLMs 1 and 2).
- **Experiment 2 (fMRI + single options)**: 5 sessions × ~235 trials per monkey; single novel options presented sequentially (no choice required). Two analyses: (a) repetition suppression (BOLD adaptation) to probe stimulus identity representations in OFC; (b) grid-code analysis testing for sixfold (60°) periodic modulation of BOLD as a function of the trajectory angle between successive options in value space (GLM 4, quadrature test).
- **Experiment 3 (TUS + choice)**: Offline transcranial ultrasound stimulation (TUS; 40 s) to MFC target, a posterior medial frontal control site, or sham, followed by ~47 min of inconsistent novel/familiar binary choice. 4 sessions per condition per monkey. Computational modelling extracted an "integration coefficient" (η) capturing the mixture of multiplicative vs. additive value computation.
- **Computational model**: Nested model comparison (2^9 models) using BIC. Winning model: softmax choice driven by a mixture of multiplicative value (magnitude × probability) and additive value ((magnitude + probability)/2), with parameters η (integration coefficient), β (magnitude/probability weighting ratio), θ (inverse temperature), and ζ₁ (side bias).

---

### Key findings

- **Behavioural**: Macaques chose near-optimally for both familiar and novel options, with comparable response times, demonstrating spontaneous inferential decision-making.
- **OFC — value comparison signal**: A parametric value comparison signal (chosen minus unchosen value, negative sign as expected in macaques) was found in OFC ([−9.5 15 4.5], cluster-corrected Z > 2.3, P = 0.017, max Z = 4.53) for both familiar and novel decisions. One-dimensional (non-integrated) trials contributed more to this signal.
- **MFC — novelty-specific comparison signal**: A prominent novelty-specific value comparison signal was found in anterior MFC ([0 24.5 7.5], area 32; P = 10⁻⁷, max Z = 4.14), dissociable from the OFC signal and present regardless of dimensionality condition (F₂,₁₄₁ < 0.3, P > 0.75).
- **OFC — object-specific representations**: Repetition suppression in anterior OFC ([−7 27 9]) indexed representations tied to specific option identities (probability × magnitude combinations), building up over sessions. Suppression was absent for options sharing only value but differing in components.
- **MFC — grid code**: Significant sixfold (hexagonal) symmetric BOLD modulation was found in MFC (Bonferroni-corrected P = 0.004), consistent with grid-cell-like encoding of the 2D value space. No such signal was found in OFC. Grid orientations from interleaved trial subsets were significantly consistent within sessions (mean phase difference 11.4°, KS test P = 0.009) but not across sessions, suggesting grid remapping.
- **TUS causal disruption**: MFC TUS selectively reduced the integration coefficient η relative to both sham and control-site TUS (F₂,₄ = 24.2, adjusted P = 0.024; Cohen's d = −5.8 for MFC vs. sham), with no effect on choice stochasticity or other parameters. This shift toward additive-only value computation was specific to novel choices.
- **Cross-species replication**: The same winning computational model (mixed multiplicative/additive) best described human binary choice data from an independent dataset (ΔBIC = 75).

---

### Computational framework

The paper uses a **mixed multiplicative/additive decision model** within a broader value-based decision-making framework. The key computational construct is the integration coefficient η, which captures how much a subject's novel choices rely on fully integrated (multiplicative: magnitude × probability = expected value) versus component-wise (additive: (magnitude + probability)/2) valuation.

The grid-code analysis draws on the **cognitive map / abstract space navigation** framework (Bellmund et al., 2018; Doeller et al., 2010): the two value dimensions (magnitude, probability) define a two-dimensional non-physical space analogous to physical space. Grid cells in entorhinal cortex represent physical position with hexagonal receptive field patterns; the paper tests whether MFC uses an analogous hexagonal code to represent positions (option identities) in value space. Trajectories between successive options in this space are analogous to navigation paths, and alignment versus misalignment with hypothetical grid axes produces periodic (60°-symmetric) modulation of fMRI BOLD signal.

Key variables: option value (multiplicative and additive), trajectory angle in value space, BOLD modulation periodicity, integration coefficient η. Core assumption: the grid-like neural representation supports multidimensional value inference, enabling novel choices by interpolation/extrapolation within a structured internal map.

---

### Prevailing model of the system under study

The paper's introduction frames the prevailing model as follows: the neural substrates of value-guided decision-making are well characterised in macaques — OFC neurons encode option values learned through repeated exposure, and these representations drive value comparison signals during choice. This circuit is the dominant model for how primate brains evaluate options, and it has been extensively validated in animals with long training histories.

A key tension introduced is that human decision-making neuroimaging studies routinely implicate MFC (near area 32/vmPFC) rather than OFC, and these human studies typically feature novel value inference rather than recall of trained values. The authors suggest this discrepancy may reflect two distinct neural systems: one (OFC-centred) for experienced, identity-based value retrieval, and another (MFC-centred) that has been largely unexplored in macaques due to paradigm design. The macaque MFC is noted to be relatively unstudied, and although its cytoarchitecture and functional connectivity parallel human vmPFC, its role in decision-making had not been established experimentally in macaques.

---

### What this paper contributes

Prior to this work, the prevailing view was that macaque OFC was the principal substrate for value comparison, and that non-human primates were largely studied in paradigms requiring extended training — leaving the question of first-time, inferential choice unaddressed in animals. The paper establishes several new facts:

1. Macaques can spontaneously make novel inferential decisions by combining attribute knowledge from different training sets — they are not limited to recall of trained values.
2. MFC (area 32) carries a novelty-specific value comparison signal that is dissociable from the general OFC signal: MFC engagement scales with value difference specifically for novel options, whereas OFC encodes value comparison regardless of familiarity.
3. MFC encodes the two-dimensional value space via a grid-cell-like hexagonal code — the first demonstration of such a code in macaque MFC, and the first in a non-spatial, abstract value domain in non-human primates.
4. OFC holds specific option-identity representations (object-value associations) that are distinct from MFC's dimensional/structural representations.
5. Causal disruption of MFC (but not adjacent cortex or sham) selectively impairs multiplicative value integration for novel choices, confirming a functional and not merely correlational role. The shift is specifically from multiplicative toward additive computation, consistent with losing the 2D grid representation.
6. The same computational signature (mixed multiplicative/additive model) describes both macaque and human novel choice, suggesting a conserved mechanism.

---

### Brain regions & systems

- **Medial frontal cortex (MFC), area 32** ([0 24.5 7.5], F99 space) — primary region of interest; carries a novelty-specific value comparison signal; contains a grid-cell-like hexagonal representation of the 2D value space (magnitude × probability); causally required for multiplicative value integration during novel choice (TUS disruption effect).
- **Orbitofrontal cortex (OFC)** ([−9.5 15 4.5]) — general value comparison signal (chosen minus unchosen) for both familiar and novel choices; holds object-specific (identity-based) value representations that build up with experience; distinct from MFC in both representation type and connectivity.
- **Anterior OFC / frontal pole region** ([−7 27 9]) — specifically shows repetition suppression for identical option identities (probability × magnitude combinations), indexing the formation of object-value memories.
- **Striatum** — additional novelty-related effects noted (Extended Data); not the primary focus.
- **Entorhinal cortex** — limited hexagonal grid-code modulation observed at uncorrected threshold; serves as the expected locus of grid cells in spatial navigation; included as an a priori ROI for comparison but showed weaker effects than MFC.
- **Lateral frontal and cingulate cortex, insula, midbrain** — additional value comparison effects noted in supplementary analyses; not central to the paper's main claims.

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: Macaques make accurate first-time (novel) value-based decisions by integrating reward magnitude and probability dimensions they previously encountered only separately.

**Computational level**: The brain must infer the integrated expected value of a novel option from its component attributes, without prior experience of that specific combination. This requires constructing a structured internal representation of the multi-dimensional value space that supports generalisation to unvisited regions.

**Algorithmic level**: MFC implements a grid-cell-like hexagonal code over the 2D magnitude × probability value space. Successive options presented rapidly correspond to "navigation" through this space; BOLD signal in MFC modulates with sixfold (60°) periodicity as a function of the trajectory angle between options, consistent with hexagonal grid receptive fields. This code allows the integrated value of novel options to be read out by their position in the space, enabling multiplicative (expected value) computation. OFC, by contrast, implements an object-specific (non-structural) value memory: repetition suppression reveals identity-coded representations that require experiencing specific option combinations.

**Implementational level**: The paper does not resolve which specific cell types, connectivity, or neuromodulators implement the grid code in macaque MFC area 32. Focal offline TUS to a 40-s window at the MFC site — but not to adjacent posterior medial frontal cortex — disrupts the multiplicative integration parameter, establishing that the effect is anatomically specific and not merely a general frontal lobe contribution. The paper notes that MFC is anatomically interconnected with medial temporal lobe structures (including entorhinal cortex, the known locus of spatial grid cells), which may provide the neural substrate for transferring the grid-coding principle to abstract value space. Full characterisation of the implementational level (cell types, layers, microcircuitry) is not achieved here.

**Bonus**: The spatial specificity of TUS (MFC vs. posterior medial frontal control site) provides a coarse anatomical constraint on implementation. The paper explicitly invokes the analogy with entorhinal grid cells and cites the spatial navigation literature as the mechanistic precedent.

---

### Limitations & open questions

- Sample size is small (n = 4 macaques for fMRI, n = 3 for TUS), as acknowledged; practical and ethical constraints limit non-human primate work.
- Grid orientation was consistent within sessions but not across sessions, suggesting grid remapping — the functional significance and conditions governing remapping are unexplained.
- The paper cannot determine whether the grid code is the mechanism underlying novel choice or a correlate of some other MFC process; TUS disruption impairs integration but does not directly demonstrate disruption of the grid code itself.
- The implementational substrate of the grid code in MFC (cell types, laminar organisation, neuromodulatory control) is entirely unresolved.
- fMRI resolution in macaque (1.5 mm isotropic) may not be sufficient to dissociate subregions within area 32; the grid-code analysis required non-parametric statistics due to the skewness of F-distributions, limiting sensitivity.
- The additive-versus-multiplicative modelling framework, while well-validated behaviourally and cross-species, does not identify the neural computations underlying the additive heuristic, which presumably does not require MFC.
- It remains unknown whether the MFC grid representation is truly metric (hexagonally symmetric receptive fields at the single-cell level) or an emergent statistical pattern at the population/BOLD level; the two are not distinguishable with fMRI.
- Whether the same MFC mechanism generalises to value spaces with more than two dimensions, or to non-reward abstract spaces, is untested.

---

### Connections & keywords

**Key citations**:
- Murray & Rudebeck (2018) — OFC specialisation for reward-guided decisions (ref 1)
- Papageorgiou et al. (2017) — macaque fMRI value comparison signal in vmPFC (ref 3)
- Chau et al. (2014); Hunt et al. (2012) — human MFC value comparison signals (refs 4, 5)
- Hafting et al. (2005) — grid cells in entorhinal cortex (ref 8)
- Doeller, Barry & Burgess (2010) — fMRI grid-cell-like signal in human entorhinal cortex (ref 9)
- Bellmund et al. (2018) — navigating cognition; spatial codes for human thinking (ref 10)
- Constantinescu, O'Reilly & Behrens (2016) — grid-like code for conceptual knowledge in humans (ref 20)
- Klein-Flügge et al. (2013) — option-identity representations in human OFC (ref 11)
- Fouragnan et al. (2019) — macaque anterior cingulate cortex and counterfactual choice (ref 13)
- Folloni et al. (2019) — TUS manipulation of deep cortical activity in primates (ref 14)
- Neubert et al. (2015) — connectivity of reward areas in human and monkey frontal cortex (ref 7)

**Named models or frameworks**:
- Mixed multiplicative/additive value model (integration coefficient η)
- Grid-cell-like code / hexagonal symmetry (quadrature test)
- Repetition suppression / BOLD adaptation paradigm
- Transcranial ultrasound stimulation (TUS), offline protocol
- Prospect theory (as tested and rejected alternative)
- Value comparison signal (chosen minus unchosen)

**Brain regions**:
- Medial frontal cortex (MFC), area 32
- Orbitofrontal cortex (OFC)
- Anterior OFC / frontal pole
- Entorhinal cortex
- Striatum

**Keywords**:
- novel value-based decision-making
- medial frontal cortex area 32
- grid-cell-like code in abstract space
- cognitive map value space
- multiplicative vs additive value integration
- transcranial ultrasound stimulation (TUS)
- fMRI macaque decision-making
- value comparison signal
- repetition suppression BOLD adaptation
- orbitofrontal cortex object-value representations
- inferential generalisation
- two-dimensional reward space
