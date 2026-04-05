---
source_file: kriegeskorte2019_encoding_decoding_models.md
title: "Interpreting encoding and decoding models"
authors: Nikolaus Kriegeskorte, Pamela K Douglas
year: 2019
journal: Current Opinion in Neurobiology
paper_type: review
contribution_type: methodological
---

### One-line summary

Encoding and decoding models are powerful tools for analysing brain-activity data, but their results require careful interpretation: decoder weight maps are unreliable, single-model significance provides only weak theoretical constraints, and the success of a linear encoding model cannot be attributed to any particular set of basis features without additional assumptions.

---

### Background & motivation

Encoding and decoding models have become the dominant analytical framework in systems and cognitive neuroscience for characterising what information is present in brain regions and in what format. Despite their widespread use, common misinterpretations persist — including treating decoder weight maps as maps of information location, assuming that significant model performance confirms a specific computational account, and conflating the presence of information with a representational interpretation. This paper addresses these pitfalls to help experimentalists draw correct inferences from brain-activity data.

---

### Methods

This is a narrative review covering conceptual and mathematical issues in the interpretation of encoding and decoding models. Its scope includes:

- Linear decoding models (classifiers, continuous decoders, stimulus reconstruction), with analysis of when and why weight maps are misleading.
- Linear and nonlinear encoding models predicting brain responses from stimulus features, including deep neural network-based models.
- Three approaches to evaluating encoding models against brain data: (1) predicting raw measurements via a linear mapping, (2) representational similarity analysis (RSA), and (3) pattern component modelling (PCM).
- Generalisation levels and their interpretive implications (same stimuli / new stimuli from same distribution / stimuli from a different population).
- The "feature fallacy" — the ambiguity in attributing model success to a specific basis set.
- The "single-model-significance fallacy" — the error of treating a significant model fit as evidence in favour of that model's computational account.
- The distinction between detecting information and making a representational interpretation.

---

### Key findings

- Decoding models reveal whether information is present in a format the decoder can exploit, but cannot in general be interpreted as models of brain-information processing; their weight maps are difficult to interpret when predictor noise is correlated or penalties are applied.
- Encoding models operating in the direction of information flow (stimulus → brain response) can serve as brain-computational models, but only if tested for generalization to novel stimuli and inferentially compared against multiple alternatives.
- The level of generalization a model achieves (to new measurements, new stimuli from the same population, or stimuli from a different population) defines the scope of claims that can be made.
- The same distribution of activity profiles can be expressed by infinitely many alternative feature sets (even with a Gaussian weight prior), so a model's predictive success does not constitute evidence for the particular features used — the "feature fallacy."
- Significant performance of a single model provides only a very low bar: it demonstrates that information is present but does not show that the model captures the computational process — the "single-model-significance fallacy." Multiple models must be tested and compared against a noise ceiling.
- RSA, PCM, and linear encoding models all test hypotheses about the representational geometry and are best viewed as a complementary toolbox; RSA naturally handles noise correlations and reduces training-data requirements, PCM can have higher model-comparison sensitivity but relies on stronger assumptions.
- Interpreting detected information as a representation requires the additional assumption that the activity serves a functional role — conveying information to downstream regions that use it to drive behaviour.

---

### Computational framework

The paper uses a **representational modelling** framework grounded in linear algebra and statistics. The core formalisms are:

- **Encoding model**: predicts brain response patterns as (nonlinear plus linear) functions of stimulus features; the representational geometry is captured by the second-moment matrix or representational dissimilarity matrix (RDM) of the stimulus-evoked activity profiles.
- **Decoding model**: predicts stimulus properties (or behavioral responses) as linear functions of brain response patterns; performance assessed by cross-validated accuracy.
- **Representational similarity analysis (RSA)**: compares model and brain at the level of pairwise dissimilarities, using the crossnobis estimator to handle noise correlations.
- **Pattern component modelling (PCM)**: models the second moment of activity profiles directly, offering higher sensitivity for model comparison.

Key variables: stimulus-response matrix, weight matrices (encoding/decoding), RDM, second-moment matrix, noise ceiling, crossvalidated prediction accuracy.

Core assumptions: linearity of the mapping component fitted to brain data, independence of train and test sets for valid generalization, and that measurement noise is distinct from representational structure.

---

### Prevailing model of the system under study

The paper addresses the field's analytical practices rather than a specific brain region or process. The background model it critiques is the widespread assumption that:

1. Decoder weight maps reveal where in the brain the decoded information lives.
2. Significant decoding or encoding performance of a given model constitutes evidence in favour of that model's computational account.
3. Information detected in a brain region can straightforwardly be interpreted as a representation served by that region.

The introduction frames encoding and decoding as grounded in an information-processing view of the brain, where neural activity represents information about the world insofar as it conveys that information to downstream regions. The conceptual split of processing around a region of interest into an "encoder" and "decoder" is acknowledged as a useful simplification that also introduces interpretive risks (because the direction of the encoder/decoder is relative, because brain regions are not strictly serial chains, and because decoding is anti-causal when it maps back to stimuli).

---

### What this paper contributes

The review consolidates and formalises three major interpretive caveats that were not all simultaneously or clearly articulated in prior literature:

1. **Weight maps are unreliable**: it provides a clear explanation (Figure 3) of why correlated noise and regularisation penalties cause uninformative voxels to receive large weights and informative voxels to receive small or zero weights in both encoding and decoding models.
2. **The feature fallacy**: it clearly names and illustrates (Figure 2) the ambiguity in attributing model success to specific features, showing that infinitely many feature sets can induce the same distribution of activity profiles even under a Gaussian weight prior.
3. **The single-model-significance fallacy**: it articulates why significant variance explained is a very low bar for computational inference, and why theoretical progress requires testing and inferentially comparing multiple models against each other and against the noise ceiling.

The review also provides a unified view of RSA, PCM, and linear encoding models as a single toolbox of representational analyses, clarifying their mathematical relationships and relative strengths. It specifies how the level of generalization achieved determines the scope of interpretive claims.

---

### Brain regions & systems

The paper does not focus on any single brain region. It draws illustrative examples primarily from visual neuroscience:

- **Ventral visual stream / IT cortex** — used as the canonical case for encoding/decoding studies of object and category representations.
- **V1** — discussed in the context of retinotopic encoding models and stimulus reconstruction.
- **Motor cortex** — mentioned briefly as a case where all conditions of interest can be measured exhaustively (finger representations), justifying generalization only to new measurements.

The paper's arguments apply broadly to any brain region studied with neuroimaging (fMRI) or electrophysiology.

---

### Mechanistic insight

This paper does not meet the bar. It is a methodological review that formalises interpretive principles; it does not present new empirical neural data, nor does it test a specific algorithm against neural recordings. It does not provide Marr-level mapping from algorithmic account to neural implementation.

The paper's contribution is at the level of statistical and conceptual analysis: it clarifies what kinds of inferences are licensed by encoding/decoding model results, and what assumptions underlie representational interpretations. The framework it articulates (compare multiple models, test generalization, use noise ceiling) constrains what kinds of computational claims are justified — but the mechanistic content must come from empirical studies that apply these principles.

---

### Limitations & open questions

- **Hypothesis testing for model weights**: the paper notes that "systems and cognitive neuroscience has yet to develop a proper set of methods for hypothesis testing" about the parameters of fitted models.
- **Representational interpretation**: distinguishing whether detected information is actively used as a representation (read out by downstream regions to drive behaviour) from mere presence of information remains an open methodological challenge requiring causal experimental tools (e.g. microstimulation, optogenetics).
- **Generalisation to subject populations**: the review focuses on within-subject prediction, which precludes straightforward generalisation to the population of subjects without additional random-effects modelling.
- **Priors complicate reconstruction interpretation**: complex generative priors used in stimulus reconstruction can inject information not present in the brain region, making quality of reconstruction an unreliable guide to representational richness.
- The paper does not address non-linear decoders or deep-network-based decoders in depth; the interpretive status of these remains underspecified.

---

### Connections & keywords

**Key citations**:
- Kriegeskorte et al. 2008 — RSA introduction
- Diedrichsen & Kriegeskorte 2017 — unified framework for encoding, PCM, and RSA
- Diedrichsen 2018 — "feature fallacy" named
- Haufe et al. 2014 — weight vector interpretation in linear models
- Naselaris et al. 2011 — encoding and decoding in fMRI
- Kay et al. 2008 — seminal natural-image encoding/decoding study
- Haxby et al. 2001 — seminal distributed decoding study
- Kamitani & Tong 2005 — orientation decoding from fMRI
- Weichwald et al. 2015 — causal interpretation rules for encoding/decoding
- Yamins & DiCarlo 2016 — goal-driven deep learning models of sensory cortex
- Khaligh-Razavi & Kriegeskorte 2014 — deep supervised models and IT cortex

**Named models or frameworks**:
- Representational similarity analysis (RSA)
- Pattern component modelling (PCM)
- Crossnobis (crossvalidated Mahalanobis) estimator
- Searchlight analysis
- Ridge regression / L2-penalised encoding
- LASSO / L1-penalised decoding

**Brain regions**:
- Ventral visual stream / IT cortex
- V1 (primary visual cortex)
- Motor cortex

**Keywords**:
- encoding model, decoding model, brain-computational model
- representational geometry, representational dissimilarity matrix
- feature fallacy, single-model-significance fallacy
- linear decodability, explicit representation
- noise ceiling, crossvalidation, generalisation
- weight interpretation, regularisation, ridge regression
- multivariate pattern analysis (MVPA), fMRI decoding
- stimulus reconstruction, prior, generative model
