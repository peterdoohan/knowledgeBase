---
source_file: loosen2020_computational_psychiatry_ocd.md
paper_id: loosen2020_computational_psychiatry_ocd
title: "Towards a computational psychiatry of juvenile obsessive-compulsive disorder"
authors:
  - "Alisa M. Loosen"
  - "Tobias U. Hauser"
year: 2020
journal: "Neuroscience and Biobehavioral Reviews"
paper_type: review
contribution_type: theoretical
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - striatum
  - amygdala
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
  - hierarchical_rl
keywords:
  - juvenile_ocd
  - developmental_computational_psychiatry
  - model_based_reinforcement_learning
  - model_free_reinforcement_learning
  - meta_controller
  - frontostriatal_loops
  - indecisiveness
  - metacognition
  - habit_formation
  - prediction_error
  - set_shifting
  - neurodevelopment
  - towards
  - computational
  - psychiatry
  - juvenile
  - obsessive
  - compulsive
  - disorder
key_citations:
  - daw2011_model_based_striatal_prediction
  - schultz1997_neural_substrate_reward_pred
  - russek2017_model_based_reinforcement
---

### One-line summary

This review synthesises neuropsychological and neuroimaging findings in juvenile OCD and proposes a neurocomputational meta-controller framework in which OCD symptoms arise from disrupted complex (model-based) reasoning systems embedded in frontostriatal loops.

---

### Background & motivation

OCD most commonly emerges during adolescence, yet the overwhelming majority of computational and neuroimaging research has been conducted in adults, leaving the developmental mechanisms of onset poorly understood. Three problems motivate the review: sparse juvenile-specific data, unclear links between brain, cognition and symptoms, and inconsistent neuropsychological findings both within and across age groups. The authors argue that computational psychiatry provides the conceptual tools to bridge these gaps by formalising how aberrant neural processes generate observable cognitive biases and clinical symptoms.

---

### Methods

This is a narrative review synthesising literature across multiple cognitive domains relevant to OCD.

- **Scope**: studies on decision making, habit formation, indecisiveness, confidence/metacognition, and neuroimaging in juvenile OCD, cross-referenced with the adult OCD and normative developmental literature.
- **Inclusion approach**: narrative, not systematic; studies are selected for their relevance to a reinforcement-learning and computational psychiatry framework.
- **Synthesis method**: findings are integrated into a theoretical multi-systems neurocomputational framework, accompanied by simulations described in supplementary material.

---

### Key findings

- Juvenile OCD patients show consistent difficulties in complex decision making and set-shifting (extra-dimensional shifts, planning), but not in simple reward learning or basic reversal learning, distinguishing OCD from disorders such as depression and schizophrenia.
- Evidence for an excessive habitual (model-free) system in juvenile OCD is absent or inconsistent; the observed reduction in model-based reasoning in adult OCD may be a *consequence* rather than a cause of OCD, with longitudinal data suggesting compulsive symptoms precede model-based deficits.
- Indecisiveness — operationalised as excess information sampling and elevated decision thresholds — is a robust and early feature of both juvenile and adult OCD; computational modelling attributes it to a delayed urgency signal rather than general cognitive impairment.
- Confidence impairments (underconfidence, reduced metacognitive accuracy) are well-established in adult OCD but are largely unstudied in juveniles; some evidence suggests low confidence is partially driven by anxiety/depression rather than compulsivity per se.
- Neuroimaging consistently implicates frontostriatal circuits — particularly the dmPFC/dACC and orbitofrontal/striatal regions — with heightened prediction errors in the dACC and aberrant myelination trajectories in OCD adolescents.
- Effect sizes are smaller in paediatric than adult OCD literature (meta-analyses: medium-to-large in adults vs. small in children), possibly reflecting shorter disease duration or that remitting patients are included in juvenile samples.

---

### Computational framework

**Reinforcement learning (model-based vs. model-free) with a multi-systems meta-controller.**

The paper adopts a hierarchical RL framework in which multiple parallel reasoning systems coexist, ranging from simple motor-outcome caches (model-free RL) to sophisticated cognitive models of task structure (model-based RL). Key elements:

- **State-action values**: each system maintains predictions about the value of actions in states; systems differ in the richness of their world model.
- **Dopaminergic prediction errors (PEs)**: serve as teaching signals across systems, with distinct PE signals for distinct frontostriatal loops.
- **Meta-confidence**: each system accrues a reliability estimate (formed from its absolute PEs); a meta-controller in the dmPFC/dACC uses these reliability signals to arbitrate between competing action policies.
- **Assumptions**: functional complexity of reasoning systems increases along a posterior-to-anterior gradient in prefrontal cortex; a corresponding ventromedial-to-dorsolateral gradient exists in the striatum; complex systems mature late in adolescence.

Three proposed pathomechanisms: (i) impaired construction or use of complex reasoning systems; (ii) faulty meta-confidence updating leading to over-reliance on simpler systems; (iii) impaired arbitration by the meta-controller itself. All three can produce the observed pattern of intact simple learning with impaired complex reasoning, habit-like behaviour, indecisiveness, and confidence-action dissociation.

---

### Prevailing model of the system under study

Before this paper, OCD was predominantly framed as a disorder of habit learning — specifically, an imbalance between goal-directed and habitual control, with an over-dominant model-free (habitual) system driving compulsive behaviour. This view was supported by outcome-devaluation studies showing that OCD patients' behaviour persists after reward removal, and by the clinical parallel between compulsions and stimulus-response habits. Frontostriatal models attributed OCD to an imbalance between direct (excitatory) and indirect (inhibitory) corticostriatal pathways, and neuroimaging highlighted hyperactivation of caudate and OFC, with hypoactivation of lateral prefrontal cortex. The developmental dimension was largely absent: the dominant model did not account for why OCD peaks in adolescence or how developmental trajectories of specific neural circuits might create vulnerability.

---

### What this paper contributes

The review challenges the primacy of the habit/model-free account by marshalling evidence that (i) the habit literature in juvenile OCD is sparse or null, (ii) longitudinal data suggest model-based deficits follow rather than precede compulsive symptoms, and (iii) OCD patients' specific failures are in complex rather than simple learning, which a pure habit account cannot explain.

In its place, the framework shifts emphasis to the complex reasoning system and its supervisory meta-controller as the primary locus of dysfunction. This reframing makes concrete, dissociable predictions: different subgroups of OCD patients may differ in *which* component is impaired (complex system, meta-confidence, or arbitration), explaining heterogeneity without invoking separate disorders. It also embeds OCD within a developmental account: because complex systems mature late, perturbations during adolescence selectively compromise model-based reasoning, and the meta-controller may compound this by failing to promote these systems as they develop. The framework is explicitly agnostic about which pathomechanism predominates and calls for computational modelling combined with neural probing to dissociate them.

---

### Brain regions & systems

- **Dorsomedial prefrontal cortex (dmPFC) / dorsal anterior cingulate cortex (dACC)** — proposed locus of the meta-controller; shows increased grey matter, heightened prediction errors, and elevated error-related negativity (ERN) in juvenile OCD; altered myelination trajectory during adolescence.
- **Orbitofrontal cortex (OFC) / ventromedial PFC (vmPFC)** — proposed site of complex reasoning systems representing task structure and hidden states; altered structural and functional connectivity in juvenile OCD.
- **Striatum (caudate/putamen)** — embedded in parallel frontostriatal loops; ventromedial regions linked to complex future-oriented values, dorsolateral to habitual/associative actions; functional and structural abnormalities reported in juvenile OCD.
- **Inferior lateral PFC (ilPFC) and frontopolar cortex (FPC)** — implicated in cognitive control and arbitration between goal-directed and habitual systems; connectivity alterations noted in adult OCD literature.
- **Amygdala** — discussed as potentially relevant given anxiety prominence in OCD, but the literature on amygdala activity in juvenile OCD is scarce and inconsistent; not assigned a definitive role in the framework.

---

### Mechanistic insight

The paper does not meet the bar for full mechanistic insight. It proposes a detailed algorithmic account — the multi-systems meta-controller — and maps it onto frontostriatal anatomy, but does not itself provide neural data (recordings, imaging, pharmacology) that specifically support the meta-controller algorithm over alternatives. The neuroimaging findings reviewed (heightened dACC PEs, ERN, myelination deficits) are consistent with the framework but were collected in studies not designed to test this specific model. The paper therefore sits at the level of a theoretically motivated review: it advances a computationally explicit hypothesis with good face validity and specific testable predictions, but empirical validation of the framework's distinctive claims awaits dedicated studies.

---

### Limitations & open questions

- The computational framework is explicitly described as speculative; face validity has been established via simulation but not direct empirical validation.
- The juvenile OCD literature remains small, cross-sectional, and methodologically heterogeneous; many conclusions are extrapolated from adult studies.
- Longitudinal studies tracking cognitive and neural development in OCD from adolescence are largely absent.
- The directionality question — whether neurocognitive impairments precede, coincide with, or follow symptom onset — remains open for most domains except model-based reasoning (where one longitudinal dataset suggests symptoms come first).
- The precise developmental timing of when different frontostriatal loops mature, and how this interacts with OCD onset, is unknown.
- It is unclear how anxiety and depression comorbidities modulate the core OCD-specific computational impairments; confidence deficits, for example, may be partially driven by these rather than compulsivity per se.
- The framework does not specify how to distinguish its three pathomechanisms behaviourally, which is needed before it can be used for subtype classification.
- The role of the amygdala and its relationship to the frontostriatal framework remains unresolved.

---

### Connections & keywords

**Key citations**: Gillan et al. (2011, 2014a, 2014b, 2016, 2020) on goal-directed/habit imbalance in OCD; Daw et al. (2011) on model-based/model-free RL task; Hauser et al. (2017b, 2017c, 2017d) on juvenile OCD, prediction errors, and indecisiveness; Schultz et al. (1997) on dopaminergic PEs; Vaghi et al. (in press) on longitudinal model-based deficits; Abramovitch et al. (2015) on paediatric OCD neuropsychology meta-analysis; Shahar et al. (2019) on multiple RL systems; Russek et al. (2017) on intermediate RL systems; Alexander and Brown (2011) on dmPFC as action-outcome predictor.

**Named models or frameworks**: model-based vs. model-free reinforcement learning; meta-controller framework; urgency-gating model (Cisek et al., 2009); developmental computational psychiatry (Hauser et al., 2019); direct/indirect corticostriatal pathway model (Maia and Frank, 2011).

**Brain regions**: dmPFC, dACC, OFC, vmPFC, striatum (caudate, putamen), ilPFC, frontopolar cortex, amygdala.

**Keywords**: juvenile OCD, developmental computational psychiatry, model-based reinforcement learning, model-free reinforcement learning, meta-controller, frontostriatal loops, indecisiveness, metacognition, habit formation, prediction error, set-shifting, neurodevelopment
