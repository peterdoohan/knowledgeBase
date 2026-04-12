---
source_file: reinert2021_prefrontal_categorization_b.md
paper_id: reinert2021_prefrontal_categorization_b
title: "Mouse prefrontal cortex represents learned rules for categorization"
authors:
  - "Sandra Reinert"
  - "Mark Hübener"
  - "Tobias Bonhoeffer"
  - "Pieter M. Goltstein"
year: 2021
journal: Nature
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - calcium_imaging
  - bayesian_decoding
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - anterior_cingulate_cortex
  - prelimbic_cortex
  - striatum
  - visual_cortex
frameworks:
  - mixed_selectivity
keywords:
  - rule_based_categorization
  - category_learning
  - prefrontal_cortex
  - two_photon_calcium_imaging
  - chronic_imaging
  - semantic_memory
  - category_selectivity
  - go_nogo_task
  - cognitive_flexibility
  - rule_switch
  - mixed_selectivity
  - category_tuning_index
  - neural_representation
  - learning_dynamics
  - generalization
  - mouse
  - prefrontal
  - cortex
  - represents
  - learned
---

### One-line summary

Chronic two-photon imaging in mouse medial prefrontal cortex reveals that category-selective neurons develop gradually during rule-based category learning, with distinct dynamics for Go-preferring (fast, ad hoc) and NoGo-preferring (gradual) populations, suggesting mPFC neurons form part of semantic memory for visual categories.

---

### Background & motivation

Categorization enables flexible behavior by allowing generalization from learned exemplars to novel stimuli. While primate prefrontal cortex (PFC) contains neurons that flexibly represent learned categories, it remains unknown how these representations first emerge—whether they are gradually built up as part of semantic memory or assigned instantaneously during task execution. This question can only be answered by tracking individual neurons throughout the entire learning process, starting from naive animals.

---

### Methods

- **Subjects**: 11 female C57BL/6 mice (chronic imaging through microprism implant in mPFC layer 2/3)
- **Task**: Head-fixed 'Go'/'NoGo' rule-based categorization of sinusoidal gratings varying in orientation and spatial frequency
- **Category rules**: Mice learned to categorize based on either orientation (rule 1) or spatial frequency (rule 2), with rule-switch training after mastering first rule
- **Imaging**: Two-photon calcium imaging (GCaMP6m) at 5–8 time points (T1–T8) spanning naive to expert performance
- **Analysis**: Category-tuning index (CTI) to quantify selectivity; Bayesian decoding; linear regression to disentangle category, choice, and reward contributions; hierarchical clustering of neuronal response types

---

### Key findings

- **Behavioral learning**: Mice learned rule-based categorization and generalized to novel stimuli upon first presentation (d′ for novel vs. experienced stimuli: P = 0.50, n = 11 mice). Rule 2 learning was significantly faster than rule 1 (P = 9.77 × 10⁻⁴).

- **Category selectivity emergence**: Before learning (T1), mPFC neurons showed no stimulus selectivity. After learning rule 1 (T5), 9.8% ± 2.2% of neurons were category-selective (CTI > 0.1), compared to 0.03% ± 0.03% before learning (P = 0.006).

- **Distinct dynamics for Go vs. NoGo populations**: Go category-selective neurons showed large, stable responses early in learning (T2–T5, ad hoc acquisition), while NoGo category-selective neurons developed selectivity gradually with increasing categorization demand (T4–T5).

- **Rule-switch dynamics**: After rule-switch, Go category-selective cells remapped their stimulus selectivity to the new Go category (retaining category selectivity), while NoGo category-selective cells lost selectivity and a new independent population emerged. Go populations for different rules overlapped more than expected by chance.

- **Uniquely category-modulated neurons**: In a task-change experiment (Go/NoGo → left/right choice), 4.3% of mPFC neurons remained category-selective despite changed motor contingencies, representing categories independent of choice, reward, or uninstructed behaviors (controlled via DeepLabCut tracking).

- **Mixed selectivity**: Hierarchical clustering revealed clusters of neurons modulated by single parameters (category, choice, reward) and clusters with mixed selectivity (combinations of task parameters), similar to primate PFC.

---

### Computational framework

The paper operates within a **category learning and neural representation framework** rather than a formal computational model. Key concepts include:

- **Category-tuning index (CTI)**: A metric quantifying category selectivity based on the difference between within-category and across-category response variation, normalized by their sum. Values near 1 indicate strong category selectivity; values near 0 indicate no selectivity.

- **Bayesian decoding**: Used to assess whether population activity patterns contain sufficient information to decode stimulus category, enabling quantification of how category selectivity at the single-neuron level translates to population-level coding.

- **Linear regression models**: Used to disentangle contributions of category identity, choice, reward, and motor behavior to neural responses, allowing identification of "pure" category-selective neurons versus mixed-selective neurons.

The paper contrasts with "ad hoc recruitment" models of PFC function (where flexible representations are instantaneously assigned during task execution) by providing evidence for gradual, learning-dependent formation of category representations consistent with semantic memory formation.

---

### Prevailing model of the system under study

Before this study, the prevailing understanding of prefrontal category representations was based primarily on studies in extensively trained primates. These studies established that:

1. **PFC neurons flexibly represent learned categories**: Primate PFC contains neurons that rapidly and flexibly represent learned categories, with selectivity emerging after extensive training on categorization tasks.

2. **Flexible representations enable cognitive flexibility**: The PFC's ability to flexibly remap representations supports cognitive flexibility, allowing animals to adapt when rules change.

3. **Two competing hypotheses about representation formation**: It remained unclear whether flexible PFC representations are:
   - **Gradually built up** as part of semantic memory formation during learning (requiring accumulated experience)
   - **Instantaneously assigned** during task execution (ad hoc recruitment, where PFC represents anything currently relevant without requiring gradual learning)

This fundamental question could not be resolved by studies in extensively trained animals alone—it required tracking the same neurons throughout the entire learning process in initially naive animals.

---

### What this paper contributes

This paper provides the first chronic imaging study tracking individual prefrontal neurons throughout the entire process of rule-based category learning, from naive to expert performance. The key contributions are:

1. **Gradual formation of category representations**: The study demonstrates that category-selective responses in mouse mPFC develop gradually during learning rather than being recruited ad hoc. This supports the hypothesis that PFC category representations are built up as part of semantic memory formation, not instantaneously assigned.

2. **Distinct learning dynamics for Go and NoGo representations**: The discovery of two distinct populations with different temporal dynamics:
   - Go category-selective neurons emerge rapidly and early (ad hoc-like), modulated by reward and choice as well as category
   - NoGo category-selective neurons emerge gradually, are purely category-modulated, and remap completely during rule-switch
   This suggests multiple mechanisms for category representation within the same circuit.

3. **Evidence for uniquely category-selective neurons**: Through a task-change experiment decoupling category from motor response, the study identifies a sparse (4.3%) but distinct population of mPFC neurons that represent categories independent of choice, reward, or uninstructed behaviors.

4. **Mouse model for studying semantic memory formation**: The study establishes a behavioral and imaging paradigm in mice that enables causal investigation of circuit mechanisms underlying category learning and semantic memory formation, opening avenues for genetic and circuit-level manipulations not readily available in primates.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC)**: Primary region of interest. Layer 2/3 neurons were chronically imaged using two-photon microscopy through a microprism implant. The mPFC contains neurons that develop category-selective responses during learning, with distinct dynamics for different subpopulations.

- **Prelimbic cortex (PL)**: Subregion of mPFC where imaging was performed (Extended Data Fig. 4g). Stereotaxic coordinates: AP 1.4–2.8 mm, ML 0.25 mm, DV 2.3 mm.

- **Anterior cingulate cortex (ACC)**: Adjacent mPFC subregion discussed in the context of anatomical localization (Extended Data Fig. 4g).

- **Posterior parietal cortex**: Mentioned as another brain area contributing to category learning (in Discussion), but not directly studied here.

- **Sensory areas (visual cortex)**: Mentioned as contributing to category learning (in Discussion), but not directly studied here.

- **Striatum**: Mentioned in Discussion as part of circuit models for category learning (interacting with PFC), but not directly studied here.

---

### Mechanistic insight

This paper provides substantial mechanistic insight into how category representations form in the prefrontal cortex, meeting the high bar for this section.

**Phenomenon**: The formation of category-selective neural representations during rule-based category learning, with distinct dynamics for Go-preferring and NoGo-preferring neurons.

**Marr's three levels analysis**:

- **Computational**: The brain must solve the problem of categorizing visual stimuli according to learned rules, enabling generalization to novel stimuli. This is crucial for behavioral flexibility in complex environments. The categorization problem requires mapping continuous visual feature spaces (orientation, spatial frequency) onto discrete category boundaries, then associating categories with appropriate motor responses.

- **Algorithmic**: The mPFC implements this computation through the gradual development of category-selective neural responses. Two distinct algorithms appear to operate:
  1. **Fast, ad hoc recruitment for Go categories**: Go-preferring neurons rapidly acquire selectivity early in learning, show mixed selectivity (category + choice + reward), and remapped their stimulus selectivity during rule-switch while maintaining category selectivity.
  2. **Slow, gradual learning for NoGo categories**: NoGo-preferring neurons develop selectivity gradually with increasing categorization demand, show pure category modulation (no choice/reward modulation), and are completely replaced during rule-switch.
  
  The algorithm involves competition between category-specific populations, with Bayesian decoding from population activity supporting category judgments.

- **Implementational**: The implementation is in layer 2/3 pyramidal neurons of the mouse mPFC (prelimbic cortex), imaged using two-photon microscopy. The physical substrate includes:
  - **Cell types**: 73% of category-selective neurons at T5 were Go-preferring; 27% were NoGo-preferring
  - **Circuit mechanisms**: The different dynamics suggest distinct microcircuits—fast ad hoc recruitment (possibly involving disinhibition or rapid plasticity) for Go representations, and slower Hebbian learning for NoGo representations
  - **Neuromodulation**: Not directly tested, but reward associations are implied in the faster Go learning
  - **Inhibitory circuits**: Implicated in the Discussion as potentially mediating the computation of NoGo representations from Go activity via local inhibitory circuits

The paper also provides evidence that uniquely category-selective neurons (4.3% of population) maintain their selectivity even when motor contingencies change, suggesting a stable categorical representation that is independent of action planning.

---

### Limitations & open questions

- **Causal manipulation**: The study is observational (imaging-only). Causal tests of whether mPFC category-selective neurons are necessary or sufficient for categorization behavior were not performed.
- **Cell-type specificity**: The imaging did not distinguish between excitatory and inhibitory neurons, or between different interneuron types. The distinct dynamics of Go and NoGo populations may reflect different cell types or circuit motifs that were not identified.
- **Circuit mechanism**: While the Discussion proposes that NoGo representations might be computed from Go activity via local inhibition, this was not tested experimentally. The source of teaching signals for gradual category learning remains speculative.
- **Molecular mechanisms**: The synaptic plasticity mechanisms underlying the gradual formation of category representations were not investigated.
- **Generalization to other modalities**: The study used only visual gratings. Whether similar dynamics occur for other sensory modalities or abstract categories is unknown.
- **Long-term stability**: The study tracked neurons through rule-switch but did not test whether category representations persist over longer timescales (weeks to months) without ongoing task performance.
- **Comparison to primates**: While the study discusses parallels to primate PFC, direct comparison of learning dynamics and representation structure between species was not performed.

---

### Connections & keywords

**Key citations**:
- Freedman et al. (2001) - Categorical representation in primate PFC (foundational)
- Wallis et al. (2001) - Single neurons in PFC encode abstract rules
- Antzoulatos & Miller (2011) - Differences between PFC and striatum during category learning
- Ashby & Maddox (2005) - Human category learning theory
- Miller & Cohen (2001) - Integrative theory of PFC function

**Named models or frameworks**:
- Category-tuning index (CTI) - metric for quantifying category selectivity
- Bayesian decoding - for assessing population-level category information
- Mixed selectivity framework - for understanding conjunctive representations
- Semantic memory formation - theoretical context for gradual learning

**Brain regions**:
- Medial prefrontal cortex (mPFC) - primary region
- Prelimbic cortex (PL) - specific subregion imaged
- Anterior cingulate cortex (ACC) - adjacent subregion
- Posterior parietal cortex - mentioned as contributing to category learning
- Visual cortex (sensory areas) - mentioned as contributing
- Striatum - mentioned in circuit models

**Keywords**:
rule-based categorization, category learning, prefrontal cortex, two-photon calcium imaging, chronic imaging, semantic memory, category selectivity, Go/NoGo task, cognitive flexibility, rule-switch, mixed selectivity, category-tuning index, neural representation, learning dynamics, generalization
