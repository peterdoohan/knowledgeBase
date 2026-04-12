---
source_file: padoaschioppa2006_orbitofrontal_economic_value.md
paper_id: padoaschioppa2006_orbitofrontal_economic_value
title: "Neurons in the orbitofrontal cortex encode economic value"
authors:
  - "Camillo Padoa-Schioppa"
  - "John A. Assad"
year: 2006
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - macaque
  - monkey
methods:
  - electrophysiology
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - posterior_cingulate_cortex
keywords:
  - economic_choice
  - orbitofrontal_cortex
  - subjective_value_coding
  - offer_value
  - chosen_value
  - good_based_decision_making
  - action_based_decision_making
  - neuroeconomics
  - single_unit_electrophysiology
  - macaque
  - visuomotor_independence
  - value_representation
  - neurons
  - orbitofrontal
  - cortex
  - encode
  - economic
  - value
---

### One-line summary

Neurons in macaque orbitofrontal cortex (area 13) encode the economic value of offered and chosen goods independently of visuospatial configuration and motor response, supporting a good-based rather than action-based model of economic choice.

---

### Background & motivation

Economic choice is typically explained by the concept of subjective value, yet the neural mechanisms and locus of value representation were unclear at the time of this study. Prior work had shown that value modulates neural activity in several sensory and motor areas (e.g., lateral intraparietal cortex), leading to an "action-based" model in which decision-making arises from competition among action-coding neurons. The OFC had been implicated in value-based behaviour through lesion studies, but direct single-unit evidence that OFC neurons encode economic value — independently of sensorimotor contingencies — was lacking. This paper fills that gap.

---

### Methods

- **Species**: Two adult macaque monkeys.
- **Task**: Economic choice task in which monkeys chose between two juice types (A preferred, B less preferred) offered in variable amounts (0–10 drops), indicated by saccade to a spatial target. Left/right positions of offers were counterbalanced.
- **Recordings**: Single-unit electrophysiology targeting area 13 of the OFC; 931 cells recorded.
- **Analysis time windows**: Seven windows: pre-offer (control), post-offer, late delay, pre-go, reaction time, pre-juice, post-juice; also 50 ms non-overlapping time bins for temporal analysis.
- **Statistical approach**: Three-way ANOVA (position × movement direction × offer type); linear regression of neural responses onto 19 candidate behavioural variables; stepwise and best-subset variable selection to identify parsimonious predictors; bilinear regression to characterise U-shaped (chosen-value) responses.
- **Value measurement**: Relative juice values estimated from sigmoid fits to choice behaviour in each session; allowed trial-by-trial computation of offer value, chosen value, and juice taste.

---

### Key findings

- 54% of recorded OFC neurons (505/931) had activity significantly modulated by offer type in at least one time window.
- Three variables — offer value, chosen value, and taste — best explained 79% (1,085/1,379) of offer-type-modulated responses, with mean R² = 0.63.
- Fewer than 5% of neurons showed dependence on spatial position of the offer or direction of the motor response, establishing value coding as largely independent of visuospatial and motor factors.
- U-shaped responses encoding chosen value were confirmed to track subjective (not physical) value: the regression slope ratio k* covaried with the behavioural relative value n* across sessions and juice pairs (b₁ = 1.05 ± 0.15, consistent with k* = n*).
- Temporal analysis revealed an orderly sequence: offer-value coding predominated shortly after the offer; chosen-value coding emerged during the delay (before the go signal, i.e., while choice was still covert); taste coding dominated before and after juice delivery.
- Results were statistically indistinguishable between the two monkeys.

---

### Computational framework

The paper uses a subjective expected utility / value-based decision framework. The core quantity is the scalar subjective value V(x) of a good, assumed to follow a linear value function. Relative value (n*) is estimated from choice indifference points and used to place different goods on a common value scale. The framework assumes that economic choice involves a dedicated stage of good-valuation prior to action selection — a modular, "good-based" architecture — as opposed to an "action-based" architecture in which value is computed only in the context of specific motor plans.

---

### Prevailing model of the system under study

At the time of publication, a prominent view (associated with neuroeconomics work in parietal cortex, e.g., Platt & Glimcher 1999; Glimcher, Dorris & Bayer 2005) held that economic choice is fundamentally choice between actions: value signals in areas like LIP reflect the value of competing motor plans, and the resolution of this competition constitutes the decision. According to this "action-based" model, value representations are inherently tied to sensorimotor contingencies. The OFC was known to be important for value-guided behaviour (from lesion and imaging work), but the field had not established whether OFC neurons encoded value in a modality- and action-independent format.

---

### What this paper contributes

The paper provides direct single-unit evidence that OFC neurons encode economic value in an abstract, good-based format — independently of the spatial arrangement of offers and the direction of the motor response required to claim the reward. This distinguishes OFC from value-modulated activity in sensorimotor areas (LIP, FEF, SC, etc.) and supports a good-based model in which the OFC is the locus of value assignment, with downstream motor planning occurring subsequently. The temporal sequence of offer-value → chosen-value → taste coding adds a process-level account of how evaluation unfolds within a trial. The demonstration that chosen-value responses track behavioural relative value (not physical juice quantity) rules out simple perceptual confounds and establishes genuine subjective value coding.

---

### Brain regions & systems

- **Orbitofrontal cortex (area 13)** — primary recording site; proposed locus of good-based economic value assignment, encoding offer value, chosen value, and taste independently of visuomotor contingencies.
- **Lateral intraparietal area (LIP)** — discussed as a contrast case: value in LIP modulates activity related to planned saccades, consistent with the action-based model the paper argues against.
- **Anterior cingulate cortex, superior colliculus, dorsolateral prefrontal cortex, frontal/supplementary eye fields, premotor cortex, posterior cingulate cortex** — briefly mentioned as areas where value modulates sensorimotor activity, cited to motivate the distinction from OFC coding.

---

### Mechanistic insight

The paper meets both criteria for this section. It proposes a computational algorithm (good-based value assignment in OFC prior to action selection) and provides neural recording data specifically supporting that algorithm over the action-based alternative.

- **Computational**: The problem is to assign subjective values to available goods and select the higher-valued option. Why? To maximise reward in the absence of a fixed correct action. The OFC solves the value-assignment sub-problem in a good-specific, action-independent manner.
- **Algorithmic**: Representations are scalar value signals (offer value, chosen value, taste) encoded by OFC neurons. The process unfolds sequentially: individual good values are represented first (offer value), an integrated choice emerges next (chosen value, covertly during the delay), and the identity of the selected good is encoded last (taste/post-choice). This suggests a feedforward computation from valuation to selection to consumption coding, distinct from the visuomotor competition account.
- **Implementational**: The paper does not address cell types, laminar organisation, connectivity, or neuromodulatory mechanisms. The implementation level is therefore uncharacterised.

---

### Limitations & open questions

- Offer-value responses are ambiguous between encoding subjective value and encoding a variable proportional to juice quantity (the two are correlated under a linear value function); the authors note this cautiously.
- The study is limited to a single OFC sub-area (area 13) in macaques; generalisation to other OFC subregions, other species, or humans remains open.
- The paper does not address how chosen-value signals in OFC are computed or read out — the upstream inputs and downstream targets are not investigated.
- Value coding for non-food goods (e.g., social stimuli, monetary reward) is flagged as a necessary extension.
- The action-based versus good-based framing treats these as mutually exclusive; the paper does not rule out that both mechanisms coexist and contribute to choice under different conditions.
- Neural mechanisms of how choice is resolved (e.g., competition, threshold, timing) are not addressed.

---

### Connections & keywords

**Key citations**:
- Platt & Glimcher (1999) — LIP value coding; foundational action-based model reference
- Glimcher, Dorris & Bayer (2005) — physiological utility theory; neuroeconomics of choice
- Tremblay & Schultz (1999) — OFC relative reward preference in primates
- Wallis & Miller (2003) — OFC and DLPFC during reward preference task
- Roesch & Olson (2004) — frontal cortex reward value and motivation
- Padoa-Schioppa, Jandolo & Visalberghi (2006) — multi-stage value processing in capuchins

**Named models or frameworks**:
- Good-based model of economic choice
- Action-based model of economic choice (Glimcher et al.)
- Subjective expected utility framework

**Brain regions**:
- Orbitofrontal cortex (area 13)
- Lateral intraparietal area (LIP)
- Anterior cingulate cortex
- Dorsolateral prefrontal cortex
- Superior colliculus
- Posterior cingulate cortex

**Keywords**:
- economic choice
- orbitofrontal cortex
- subjective value coding
- offer value
- chosen value
- good-based decision-making
- action-based decision-making
- neuroeconomics
- single-unit electrophysiology
- macaque
- visuomotor independence
- value representation
