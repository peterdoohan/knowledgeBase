---
source_file: reinert2021_prefrontal_categorization.md
title: "Mouse prefrontal cortex represents learned rules for categorization"
authors: Sandra Reinert, Mark Hübener, Tobias Bonhoeffer, Pieter M. Goltstein
year: 2021
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Chronic two-photon calcium imaging of mouse medial prefrontal cortex throughout rule-based category learning reveals that category-selective neurons emerge gradually, with Go-category and NoGo-category populations showing distinct learning dynamics and differential engagement during rule-switches.

---

### Background & motivation

The prefrontal cortex (PFC) is known to represent learned categories in extensively trained primates, but it was unknown whether flexible category representations first emerge gradually as part of semantic memory formation or are recruited ad hoc once the animal encounters task demands. This question requires following individual neurons from a naive state through the full course of learning — a study design that prior primate work had not achieved. Mice offer an opportunity to perform chronic longitudinal imaging during the entire learning process, starting from completely naive animals.

---

### Methods

- **Subjects**: 11–20 head-fixed female C57BL/6 mice implanted with a prism for optical access to medial PFC (mPFC)
- **Task**: Go/NoGo rule-based categorization using 36 sinusoidal gratings varying in orientation and spatial frequency; mice learned to categorise stimuli by one feature dimension (rule 1), then switched to the other (rule 2); a subset underwent a further switch from Go/NoGo to a left/right choice paradigm to decouple category identity from motor response
- **Imaging**: Longitudinal two-photon calcium imaging (GCaMP6m) at up to 8 time points across learning (T1 = naive baseline through T8 = post rule-switch), tracking the same cells across sessions via structural mRuby2 channel
- **Analysis**: Category-tuning index (CTI) to quantify selectivity; cross-validated Bayesian decoding; linear regression to partition contributions of category identity, choice, and reward; hierarchical clustering of task-responsive population; DeepLabCut tracking of uninstructed body movements as nuisance regressors

---

### Key findings

- In naive mice, virtually no mPFC neurons showed category selectivity (0.03% ± 0.03%); after learning rule 1, ~9.8% ± 2.2% were category-selective
- After rule-switch to rule 2, selectivity for rule 1 categories dropped and a comparable fraction (~8.6% ± 2.8%) became selective for rule 2 categories
- **Two distinct populations** with different dynamics:
  - **Go category-selective neurons** emerged rapidly early in training (ad hoc, T2–T5), remapped to track the new Go category after rule-switch, and were modulated by category, choice, and reward (mixed selectivity)
  - **NoGo category-selective neurons** emerged gradually with increasing categorization demand (T4–T5), did not remap after rule-switch (lost selectivity; a new independent population formed), and were selectively modulated by category identity alone
- Go-selective populations across rule 1 and rule 2 overlapped more than chance; NoGo-selective populations did not
- Rule 2 was learned significantly faster than rule 1 (P = 9.77 × 10⁻⁴), suggesting faster re-use of existing representations
- Left/right choice experiment revealed a subset of uniquely category-modulated neurons (~4.3%) whose selectivity was invariant to motor contingency changes
- Category contribution remained significant even after accounting for uninstructed body movements (pupil, posture, tail angle, etc.)

---

### Computational framework

Not a computational paper in the primary sense; no formal model is fitted. However, the study is framed around the debate between two competing accounts of PFC category representations:

1. **Gradual learning hypothesis**: category representations are built up incrementally during learning as part of semantic memory
2. **Ad hoc / adaptive coding hypothesis**: PFC flexibly and rapidly assigns representations to whatever is currently task-relevant

The paper provides direct empirical evidence resolving this debate — neither account is wholly correct. The NoGo population follows the gradual learning trajectory; the Go population shows an ad hoc component (rapid emergence tied to choice/reward learning) but also a slow-learning component. The mPFC thereby contains a mixture of learning strategies in parallel populations.

A circuit model mentioned in the Discussion (Villagrasa et al. 2018; Antzoulatos & Miller 2011) proposes that slow-learning PFC circuits acquire category selectivity using rapidly learned stimulus-specific striatal activity as a teaching signal.

---

### Prevailing model of the system under study

Prior to this paper, primate work had established that PFC neurons represent visual categories after extensive training, and that these representations are flexible across rule changes. However, the existing view was based on already-trained animals, leaving open whether the representations were gradually acquired or assigned ad hoc. The adaptive coding model (Duncan 2001; Miller & Cohen 2001) proposed that PFC flexibly represents whatever is task-relevant, implying rapid, on-the-fly assignment. Conflicting evidence from primates pointed toward rapid (ad hoc) assignment of category representations. The mouse mPFC was known to contribute to cognitive flexibility and rule learning but had not been studied longitudinally at cellular resolution through the full learning process. The field thus lacked direct evidence on the developmental trajectory of category selectivity from naive animals.

---

### What this paper contributes

This paper provides the first longitudinal cellular-resolution account of how category representations in a rodent mPFC emerge from scratch. Key advances:

- Establishes definitively that NoGo category selectivity is **gradually acquired** as part of category learning (not ad hoc), consistent with a semantic memory account for this subpopulation
- Shows that Go category selectivity emerges **more rapidly**, reflecting co-mingling of category learning with reward and choice representations that are acquired earlier in training
- Demonstrates **flexibility** of the Go-selective population (remapping to track new category after rule-switch) versus **replacement** of the NoGo-selective population
- Identifies a sparse (~4.3%) but genuine category-invariant subpopulation in mPFC whose responses survive changes in motor contingency — showing that the mPFC does contain abstract category representations, not merely stimulus-action or stimulus-reward associations
- Opens the door to causal circuit dissection of category learning in mice, which is not easily achievable in primates

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC), layer 2/3** — primary focus; site of category-selective neuron formation and longitudinal imaging; proposed locus of rule-based category memory
- **Striatum** — discussed in the context of a circuit model where rapid striatal stimulus-specific activity may provide a teaching signal to slower-learning PFC circuits (cited but not directly recorded)
- **Posterior parietal cortex** — mentioned as another area contributing to categorization; not directly studied in this paper
- **Sensory areas** — mentioned as contributors to categorization; not directly studied here

---

### Mechanistic insight

The paper meets the bar for mechanistic insight at the algorithmic level but only partially at the implementational level.

- **Computational**: The mPFC solves the problem of mapping novel sensory stimuli onto behaviorally relevant categories in a way that generalizes across exemplars and survives rule changes — i.e., it computes a flexible abstract categorical code that decouples stimulus identity from specific motor responses.

- **Algorithmic**: Two parallel learning processes run concurrently in mPFC: (1) a fast process linking stimuli to reward/choice associations (Go-preferring neurons, mixed selectivity, ad hoc onset); (2) a slow process extracting pure category identity from increasing categorization demand (NoGo-preferring neurons, pure category selectivity, gradual onset). The left/right task change experiment shows that the slow process generates stimulus-invariant category representations. The longitudinal CTI tracking maps these processes to identifiable single neurons followed across sessions.

- **Implementational**: Partially addressed. The paper records from layer 2/3 pyramidal neurons (implied by GCaMP6m expression under the hSyn promoter), but does not identify specific cell types (e.g., interneurons vs. excitatory neurons) or connectivity that would explain why these two populations exist. The prism imaging method provides cellular resolution but not cell-type specificity. The Discussion proposes a circuit model invoking local inhibitory circuits to generate NoGo representations from conjunctive Go/choice signals, but this is not tested here.

---

### Limitations & open questions

- Imaging is restricted to mPFC layer 2/3; deeper layers (5/6), which project to downstream targets, are not accessible with the prism preparation
- GCaMP6m provides calcium proxy of spiking but does not resolve fast temporal dynamics at single-spike level
- The cell-type identity of category-selective neurons is not resolved; it is unclear whether Go and NoGo populations correspond to distinct genetic or projection-defined classes
- Causal necessity of mPFC category-selective neurons for behaviour is not established (no optogenetic or chemogenetic silencing experiments)
- The proposed circuit model (striatum → PFC teaching signal) is not directly tested in this paper
- The left/right task change was performed after only rule 1 learning, so it is unknown whether the 4.3% uniquely category-selective population changes in size or composition after rule 2 learning
- Only female mice were used; potential sex differences in categorization or mPFC function are not addressed
- The study tracks 8 imaging time points but daily resolution of selectivity emergence is coarse during the earliest stages; finer resolution could better distinguish ad hoc vs. gradual onsets

---

### Connections & keywords

**Key citations**:
- Freedman, Riesenhuber, Poggio & Miller 2001 (Science) — primate PFC categorical representation
- Roy, Riesenhuber, Poggio & Miller 2010 (J. Neurosci.) — flexible PFC categorization in primates
- Antzoulatos & Miller 2011 (Neuron) — PFC vs. striatum during abstract category learning
- Duncan 2001 (Nat. Rev. Neurosci.) — adaptive coding model of PFC
- Miller & Cohen 2001 (Annu. Rev. Neurosci.) — integrative theory of PFC function
- Rigotti et al. 2013 (Nature) — importance of mixed selectivity in complex cognitive tasks
- Villagrasa et al. 2018 (J. Neurosci.) — cortico-basal ganglia circuit model for category learning
- Low, Gu & Tank 2014 (PNAS) — prism implant method for mPFC imaging

**Named models or frameworks**:
- Category-tuning index (CTI) — quantitative measure of category selectivity adapted from Freedman et al. 2002
- Adaptive coding model (Duncan 2001) — PFC as flexible, on-the-fly representation engine
- Go/NoGo categorization task (rule-based categorization paradigm)
- Left/right choice task — motor decoupling paradigm to isolate category-invariant signals
- DeepLabCut — markerless pose estimation for nuisance covariate control

**Brain regions**:
- Medial prefrontal cortex (mPFC), layer 2/3
- Striatum
- Posterior parietal cortex

**Keywords**:
- rule-based categorization
- medial prefrontal cortex
- two-photon calcium imaging
- longitudinal neural recording
- category selectivity
- mixed selectivity
- cognitive flexibility
- rule-switch
- Go/NoGo task
- semantic memory
- category-tuning index
- learning dynamics
