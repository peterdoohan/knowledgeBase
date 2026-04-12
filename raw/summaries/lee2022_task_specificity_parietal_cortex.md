---
source_file: lee2022_task_specificity_parietal_cortex.md
paper_id: lee2022_task_specificity_parietal_cortex
title: "Task specificity in mouse parietal cortex"
authors:
  - "Julie J. Lee"
  - "Michael Krumin"
  - "Kenneth D. Harris"
  - "Matteo Carandini"
year: 2022
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - t_maze
  - virtual_navigation
methods:
  - calcium_imaging
brain_regions:
  - hippocampus
  - amygdala
  - visual_cortex
frameworks:
  - reinforcement_learning
  - mixed_selectivity
keywords:
  - posterior_parietal_cortex
  - task_specificity
  - physical_context
  - neuronal_ensemble
  - two_photon_calcium_imaging
  - head_fixed_mouse
  - mixed_selectivity
  - context_dependent_gating
  - visual_decision_task
  - multi_task_recording
  - sparse_coding
  - virtual_reality_navigation
  - task
  - specificity
  - mouse
  - parietal
  - cortex
---

### One-line summary

Neurons in mouse parietal cortex are task specific — individual neurons are active in one physical task context and inactive in another — and this specificity is determined by the physical apparatus rather than sensory or cognitive demands.

---

### Background & motivation

Parietal cortex is implicated in a wide range of behaviours including motor planning, evidence accumulation, decision-making, navigation, and multisensory integration. A fundamental question is whether individual parietal neurons participate in multiple tasks (acting as generalists) or are recruited selectively for specific behavioural contexts. Prior studies comparing parietal activity across tasks typically manipulated sensory modality while keeping task apparatus constant, yielding inconsistent conclusions and leaving open the question of what drives cross-task similarity or specificity in parietal representations. Recording from the same neurons across two distinct tasks with different apparatus allowed the authors to address this directly.

---

### Methods

- **Subjects**: head-fixed mice (n = 6) trained to perform two visual two-alternative forced-choice tasks on the same days.
- **Task 1 (T-maze)**: mice ran on an air-suspended styrofoam ball to navigate a virtual T-maze; reported grating location by turning into the corresponding arm.
- **Task 2 (steering-wheel)**: mice sat on a platform and turned a steering wheel to centre a grating; different visual stimuli, different motor output, different apparatus.
- **Task 3 (hybrid / "steering T-maze")**: combined the T-maze's virtual visual scene with the steering-wheel apparatus; trained in a subset of mice (n = 2) to dissociate physical vs. visual context.
- **Neural recordings**: two-photon calcium imaging (GCaMP6) of hundreds of simultaneously recorded parietal neurons anterior to V1, overlapping with visual areas A and RL; cells identified with Suite2p.
- **Activity quantification**: "isolation distance" metric to classify neurons as active or inactive per task; deconvolved firing rate used as a complementary measure.
- **Cross-day stability**: same imaging plane re-recorded on subsequent days; Spearman rank correlations computed within and across tasks.
- **Passive conditions**: neurons recorded in each apparatus with a blank grey screen (no task stimuli) to isolate the role of physical context from task demands per se.
- **Encoding model**: linear regression model with predictors for stimulus onset, choice, and reward fitted separately per task to quantify task-variable encoding.

---

### Key findings

- Over half of parietal neurons with detectable activity were task specific: active in only one of the two tasks.
- Within-task correlations across days were strongly positive (r ≈ 0.83 and 0.77 for T-maze and steering-wheel respectively); cross-task correlations were negative or non-significant (r ≈ −0.24 to −0.27).
- Task specificity was stable and reproducible across consecutive days (cross-day task preference correlations r = 0.78–0.87).
- In passive conditions (grey screen), neurons showed the same context specificity as during active tasks, ruled out sensory stimuli and optic flow as the primary driver.
- Running speed, pupil diameter, and facial movement differences did not account for context specificity.
- The hybrid task confirmed the role of physical context: activity in the hybrid task was correlated with the steering-wheel task (same apparatus; r = 0.74) but uncorrelated with the T-maze task (different apparatus; r = −0.02).
- Encoding model variance explained was negatively correlated across tasks: neurons that well predicted task events in one task were poorly predicted in the other.
- The minority of neurons active in both tasks did not have correlated choice preferences across tasks, indicating that even shared neurons do not generalise their task-relevant signals.
- Task-specific subpopulations were spatially intermixed with no evident anatomical organisation within the imaged field.

---

### Computational framework

Not applicable in a formal sense. The paper does not implement or fit a computational model. The results constrain models of mixed selectivity and multi-task representations in parietal cortex. Specifically, the findings are relevant to frameworks of **neural population geometry** and **context-dependent gating**: the data show that parietal representations are not generalised across tasks, which challenges accounts in which parietal neurons maintain abstract, task-invariant signals (e.g., pure evidence accumulation or spatial-position codes). The findings are more consistent with a **sparse coding / ensemble** view where physical context deterministically gates which neuronal subpopulation is recruited.

---

### Prevailing model of the system under study

The introduction positions parietal cortex as a high-level, multi-functional region whose neurons encode a diverse mixture of task-relevant variables (motor planning, evidence accumulation, spatial position, movement sequences, body posture). The "mixed selectivity" literature — primarily from single-task studies — suggests that individual parietal neurons are computationally versatile and participate in multiple task computations within a task. Prior multi-task comparisons in rodents found that parietal neurons had similar choice preferences when tasks differed in sensory modality but used the same apparatus, suggesting broad flexibility. The field therefore generally assumed that parietal neurons could generalise across different behavioural demands, particularly when the task structure (forced choice, same reward contingency) is shared.

---

### What this paper contributes

The paper establishes that parietal neurons in mice are not generalists but specialists: different physical contexts activate largely non-overlapping neuronal populations. This challenges the assumption that parietal mixed selectivity implies cross-task generality. Critically, by recording in passive conditions and using a hybrid task, the study isolates physical apparatus (not sensory stimuli, motor demands, or task difficulty) as the dominant factor driving this specificity. Prior evidence for cross-task similarity in parietal cortex can be reconciled — it came from studies that varied sensory modality but held apparatus constant, exactly the condition predicted by this framework to produce stable representations. The study thus reframes parietal cortex from a general-purpose decision area to a context-specific ensemble system, where different physical environments recruit distinct subpopulations.

---

### Brain regions & systems

- **Posterior parietal cortex (mouse, areas A and RL)** — primary region of interest; locus of task-specific neuronal subpopulations. Targeted as the region anterior to V1 overlapping with visual areas A and RL, identified by wide-field retinotopy.
- **Primary visual cortex (V1)** — used as a spatial landmark for imaging target localisation; not directly investigated.
- Implicit comparisons drawn to **hippocampus** (context-specific place cells in different environments) and **amygdala** (context-specific ensemble activity) in the discussion, suggesting the physical-context gating principle may be brain-wide.

---

### Mechanistic insight

The paper partially meets the bar. It provides neural recordings specifically linked to a proposed mechanism (context-dependent ensemble gating), and the passive-condition and hybrid-task experiments are tightly designed to isolate physical context as the causal factor. However, the paper does not formalise the mechanism as an algorithm and does not address the implementational level (cell types, connectivity, neuromodulators).

- **Computational**: the brain must deploy distinct parietal circuits for computations appropriate to each physical context, preventing cross-task interference.
- **Algorithmic**: context-specific gating of neuronal subpopulations: the physical apparatus (and associated motor/proprioceptive state) selects which parietal ensemble becomes active; these ensembles encode task-relevant variables (stimulus, choice, reward) only within their context.
- **Implementational**: not addressed. The paper shows that task-specific subpopulations are spatially intermixed, ruling out a coarse topographic implementation. The mechanism by which physical context gates specific subpopulations — whether via thalamic input, feedback from motor or somatosensory cortex, or neuromodulation — is left open.

---

### Limitations & open questions

- "Physical context" is operationally defined as the conjunction of apparatus, motor demands, and potentially proprioceptive/somatosensory state; the specific feature(s) within the context that drive selectivity are not disambiguated.
- The hybrid task isolates physical versus visual context, but does not resolve whether it is the motor report (wheel turning), body posture, or proprioceptive feedback from the apparatus that is the critical factor; EMG or more extensive video analysis was noted as needed.
- Silent neurons not detected by calcium imaging constitute the majority of parietal cells (estimated from anatomical density); their properties across contexts are unknown.
- Choice selectivity was very low in the steering-wheel task (<10% of active neurons), limiting the power to detect cross-task alignment of choice signals.
- Whether context specificity generalises to other parietal regions, other species, or non-visual tasks is not addressed.
- The cellular or circuit mechanism by which physical context gates ensemble activity is completely unresolved.
- Only 6 mice were used for the main comparison; the hybrid task was performed in only 2 mice.

---

### Connections & keywords

**Key citations**:
- Krumin et al. (2018) eLife — prior parietal decision study in the T-maze task
- Burgess et al. (2017) Cell Reports — steering-wheel task design
- Raposo et al. (2014) Nature Neuroscience — parietal neurons across sensory modalities, same apparatus
- Nikbakht et al. (2018) Neuron — parietal neurons across tactile and visual modalities
- Steinmetz et al. (2019) Nature — distributed choice coding across mouse brain
- Pachitariu et al. (2017) bioRxiv — Suite2p calcium imaging pipeline
- Harvey et al. (2012) Nature — choice sequences in parietal cortex during virtual navigation

**Named models or frameworks**:
- Suite2p (calcium imaging segmentation and demixing pipeline)
- Isolation distance (activity metric)
- Encoding model (linear regression with task-event predictors)

**Brain regions**:
- Posterior parietal cortex (mouse), visual areas A and RL
- Primary visual cortex (V1)

**Keywords**:
- posterior parietal cortex
- task specificity
- physical context
- neuronal ensemble
- two-photon calcium imaging
- head-fixed mouse
- mixed selectivity
- context-dependent gating
- visual decision task
- multi-task recording
- sparse coding
- virtual reality navigation
