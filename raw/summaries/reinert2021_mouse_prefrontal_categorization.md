---
source_file: reinert2021_mouse_prefrontal_categorization.md
title: Mouse prefrontal cortex represents learned rules for categorization
authors: Sandra Reinert, Mark Hübener, Tobias Bonhoeffer, Pieter M. Goltstein
year: 2021
journal: Nature
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Using longitudinal two-photon calcium imaging in mice learning a rule-based visual categorization task, this study shows that medial prefrontal cortex (mPFC) neurons gradually acquire category selectivity during learning, with Go- and NoGo-preferring populations following distinct dynamics and a sparse subset encoding categories independently of motor contingencies and reward.

---

### Background & motivation

Flexible categorization — grouping stimuli by abstract rules rather than memorizing individual exemplars — is computationally advantageous and depends on the prefrontal cortex in primates. Primate PFC neurons rapidly and flexibly represent learned categories, but whether these representations are built up gradually as semantic memory or recruited ad hoc during task execution has remained unresolved because prior studies could not track neurons from a naive state through the full learning process. The mouse mPFC offers a tractable model for chronic imaging across learning, yet it was unclear whether mice could perform rule-based categorization and whether their mPFC would contain analogous category representations.

---

### Methods

- **Subjects**: 20 female C57BL/6 mice; head-fixed, water-restricted.
- **Task**: Go/NoGo rule-based visual categorization using 36 sinusoidal gratings varying in orientation and spatial frequency. Mice learned two successive rules (orientation vs. spatial frequency boundary), with stepwise addition of stimuli up to 18 per category, followed by a generalization test with 18 novel stimuli.
- **Rule-switch**: After mastering rule 1 (n = 11 mice), the previously irrelevant stimulus dimension became the new categorization rule.
- **Task-change experiment**: After learning rule 1 (n = 9 mice), the Go/NoGo motor contingency was replaced with a left/right choice task, decoupling category identity from motor response and reward.
- **Imaging**: Chronic longitudinal two-photon calcium imaging of layer 2/3 mPFC neurons via a microprism implant (GCaMP6m), at 5–8 time points spanning naive through expert stages (T1–T8); individual cells tracked across sessions.
- **Analysis**: Category-tuning index (CTI) to quantify selectivity; cross-validated Bayesian decoding; linear regression to decompose contributions of category, choice, and reward; hierarchical clustering of task-responsive neurons; DeepLabCut tracking of uninstructed body movements as control.

---

### Key findings

- Before learning (T1), mPFC neurons did not respond to visual stimuli; after learning rule 1 (T5), 9.8 ± 2.2% of neurons became category-selective (CTI > 0.1).
- After the rule-switch (T8), a similar fraction encoded new categories (8.6 ± 2.8% for rule 2), while selectivity for the now-irrelevant rule 1 categories dropped to 0.07 ± 0.05%.
- Go- and NoGo-preferring populations showed distinct learning dynamics: Go category-selective neurons emerged rapidly (ad hoc, T2–T5) and remapped their stimulus selectivity after the rule-switch; NoGo category-selective neurons emerged gradually as categorization demand increased (T4–T5), were lost after the rule-switch, and were replaced by a new population.
- Go category-selective neurons showed mixed selectivity (modulated by category, choice, and reward); NoGo category-selective neurons were modulated predominantly by category identity alone.
- After the task change (Go/NoGo → left/right), category-selective neurons identified at T5 retained selectivity for the same stimulus categories across the change in motor contingency.
- Regression analysis identified 4.3% of mPFC neurons as uniquely category-modulated, not explained by choice, reward, or any tracked uninstructed behaviour (whisking, eye movements, posture).
- Mice generalised learned rules to 18 novel stimuli upon first presentation, with performance on novel and experienced stimuli not significantly different (d′ comparison, p = 0.50 for rule 1; p = 0.09 for rule 2).
- Rule 2 was learned significantly faster than rule 1 (p = 9.77 × 10⁻⁴, Wilcoxon matched-pairs signed-rank test).

---

### Computational framework

Not applicable as a formal computational framework. The paper is primarily an empirical characterisation of how category representations emerge in mPFC during learning. The analysis employs the **category-tuning index (CTI)** — a ratio that captures whether between-category firing rate differences exceed within-category differences — and a **Bayesian decoder** to confirm that CTI captures decodable category information. Linear regression is used to decompose neural variance into contributions from category, choice, and reward, but no mechanistic computational model is developed or fitted.

The results are interpreted in the context of a circuit-level model (discussed, not formalised here) in which slow-learning PFC circuits acquire category selectivity using rapidly learned stimulus-specific activity from striatum as a teaching signal, with local inhibitory circuits in mPFC computing NoGo category representations from Go/choice-selective neurons.

---

### Prevailing model of the system under study

Prior to this paper, the dominant view was that PFC — particularly in primates — contains neurons that flexibly represent task-relevant categories, and that these representations are somehow linked to rule-based categorization. Two competing hypotheses existed: (1) category representations are **gradually built up** as part of semantic/long-term memory over the course of learning; (2) they are **recruited ad hoc** (instantaneously) during task execution when something becomes relevant. Evidence from primate studies (e.g., Freedman et al., Roy et al.) showed that PFC neurons represent categories in extensively trained animals, but could not discriminate between these hypotheses because recording began only after training. The field also assumed that category-selectivity in PFC is confounded with choice and reward selectivity, since in standard Go/NoGo tasks these co-vary. The role of mouse mPFC in rule-based categorization (as opposed to simpler discrimination) was largely unexplored.

---

### What this paper contributes

This study resolves the gradual vs. ad hoc debate in favour of **both**, by showing that the two populations follow different timecourses: the Go category representation partly arises rapidly (reflecting choice/reward learning that predates full categorization) while the NoGo representation accumulates gradually with increasing categorization demand. By tracking the same neurons from the naive state through expert performance and across a rule-switch, the paper establishes that category representations are flexible but partly persistent (Go-selective cells remap rather than disappear), whereas NoGo-selective cells are rule-specific and replaced after a rule-switch. The task-change experiment further demonstrates that a sparse but genuine category signal (4.3% of mPFC neurons) exists independently of motor contingencies and reward, providing direct evidence for an abstract categorical representation — previously established only in primates — in rodent mPFC. The work also establishes that mice can serve as a model for studying rule-based categorization and the formation of semantic category memory.

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC), layer 2/3** — primary region of interest; locus of gradually acquired category-selective neurons, mixed-selective neurons (category + choice + reward), and uniquely category-modulated neurons.
- **Striatum** — cited in the discussion as a potential source of fast-arising, stimulus-specific teaching signals that may drive slow mPFC category learning (via Antzoulatos & Miller 2011; Villagrasa et al. 2018 circuit model).
- **Posterior parietal cortex** — mentioned as another area contributing to categorization behaviour; not directly studied here.
- **Sensory cortices** — noted as contributors to categorization; not directly studied here.

---

### Mechanistic insight

The paper partially meets the bar. It proposes and characterises a process (gradual acquisition of category selectivity) and provides neural data (chronic two-photon imaging) supporting this account over the ad hoc alternative. However, the paper does not formalise an algorithm linking specific neural computations to the observed dynamics, nor does it provide data directly linking the learning trajectory to a mechanistic model's variables.

- **Computational**: The brain is solving the problem of abstracting category identity from individual stimulus exemplars in a rule-dependent way, to enable generalisation to novel stimuli.
- **Algorithmic**: Two populations with distinct dynamics — a fast-learning population that builds a conjunctive category/choice/reward representation early (reflecting reward learning), and a slow-learning population that incrementally extracts pure category structure as categorization demand increases. A rule-switch leads to remapping in Go-selective cells and replacement of NoGo-selective cells by a new population.
- **Implementational**: Recorded from layer 2/3 of mPFC (pyramidal cell-dominated but not cell-type resolved); no data on cell types, connectivity, or neuromodulators. The paper notes that local inhibitory circuits may compute NoGo representations from Go/choice-selective inputs, but this is speculative and not directly tested.

---

### Limitations & open questions

- The paper cannot determine the cellular or circuit mechanisms generating the two populations' distinct dynamics (e.g., role of local inhibition, long-range inputs from striatum or sensory cortex).
- Two-photon imaging captures only layer 2/3; deeper layers and cell-type-specific contributions are not assessed.
- The task-change experiment is limited to a single session immediately after T5; longer-term stability of uniquely category-selective neurons is not established.
- The study does not causally test whether mPFC category representations are necessary for categorization behaviour (e.g., via optogenetic perturbation).
- The circuit model proposing striatal teaching signals driving mPFC category learning is not tested here; it remains an open hypothesis.
- Whether the gradual/ad hoc distinction generalises to other types of categorization (e.g., prototype-based or non-rule-based) is unaddressed.
- The question of how category representations in mPFC relate to consolidation into long-term semantic memory is raised but not addressed.

---

### Connections & keywords

**Key citations**:
- Freedman et al. 2001 (Science) — categorical representation of visual stimuli in primate PFC
- Roy et al. 2010 (J. Neurosci.) — PFC activity during flexible categorization
- Antzoulatos & Miller 2011 (Neuron) — PFC vs. striatum during novel category learning
- Rigotti et al. 2013 (Nature) — importance of mixed selectivity in complex cognitive tasks
- Villagrasa et al. 2018 (J. Neurosci.) — cortex-basal ganglia interactions in category learning
- Low et al. 2014 (PNAS) — microprism imaging of mPFC
- Ashby & Maddox 2005 (Annu. Rev. Psychol.) — human category learning framework
- Duncan 2001 (Nat. Rev. Neurosci.) — adaptive coding model of PFC

**Named models or frameworks**:
- Category-tuning index (CTI)
- Go/NoGo rule-based categorization task
- Left/right task-change paradigm (motor decoupling)
- Cortico-basal ganglia category learning circuit model (Villagrasa et al.)
- DeepLabCut (uninstructed behaviour tracking)
- GCaMP6m two-photon calcium imaging

**Brain regions**:
- Medial prefrontal cortex (mPFC)
- Striatum (cited)
- Posterior parietal cortex (cited)

**Keywords**:
- rule-based visual categorization
- medial prefrontal cortex
- two-photon calcium imaging
- longitudinal chronic imaging
- category-selective neurons
- mixed selectivity
- Go/NoGo task
- category-tuning index
- semantic memory
- cognitive flexibility
- rule-switch
- mouse mPFC
