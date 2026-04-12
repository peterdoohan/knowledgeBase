---
source_file: lee2022_task_specificity_parietal.md
paper_id: lee2022_task_specificity_parietal
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
  - task_specificity
  - parietal_cortex
  - context_dependent_neural_activity
  - ensemble_selectivity
  - two_photon_calcium_imaging
  - physical_context_gating
  - mixed_selectivity
  - cross_task_recording
  - mouse_decision_making
  - neural_subpopulations
  - context_remapping
  - virtual_reality_navigation
  - task
  - specificity
  - mouse
  - parietal
  - cortex
---

### One-line summary

Neurons in mouse parietal cortex are strongly task specific — different subpopulations are active in different physical task contexts — and this specificity is determined by the physical apparatus of the task rather than sensory or cognitive demands.

---

### Background & motivation

Parietal cortex has been implicated in a wide range of functions including motor planning, evidence accumulation, spatial navigation, and decision-making, leading to the expectation that individual parietal neurons might participate flexibly across multiple behavioural tasks. Prior studies had compared parietal activity across different sensory modalities (visual vs. auditory/tactile) within the same apparatus and found relatively stable choice representations, but no study had systematically recorded the same neurons across tasks that differed in their full physical context. The key unresolved question was whether parietal neurons are generalists that engage across tasks or specialists tied to specific behavioural contexts.

---

### Methods

- **Subjects**: 6 head-fixed mice expressing GCaMP6s or GCaMP6f in excitatory neurons; all mice were trained to asymptotic performance on both tasks.
- **Task 1 (T-maze)**: Mice ran on an air-suspended styrofoam ball navigating a virtual T-maze; they reported grating location (left/right wall) by turning into the corresponding arm.
- **Task 2 (Steering-wheel task)**: Mice turned a Lego steering wheel with their forepaws to bring a Gabor stimulus to the centre of the screen.
- Both tasks used visual gratings at variable contrast (0–50%); tasks were performed consecutively in the same session.
- **Task 3 (hybrid "steering T-maze")**: A subset of mice (n = 2) were trained on a third task combining the steering-wheel apparatus with the T-maze visual scene, to dissociate physical from visual context.
- **Imaging**: Two-photon calcium imaging (layer 2/3, two planes) of a parietal region anterior to V1, overlapping with visual areas A and RL, identified by widefield retinotopy.
- **Activity quantification**: "Isolation distance" (Bhattacharyya distance between cell and neuropil distributions) was used as the primary activity measure, supplemented by mean deconvolved firing rate.
- **Cross-day analysis**: The same imaging plane was aligned across consecutive days using Suite2p to assess repeatability.
- **Passive conditions**: Mice were imaged in each physical apparatus without any task stimuli (gray screen) to test whether context specificity persisted in the absence of task demands.
- **Encoding models**: Ridge regression was used to predict single-neuron activity from behavioural predictors (stimulus onset, choice, reward, apparatus velocity) separately for each task; cross-validated variance explained was compared across tasks.
- **Choice selectivity**: Combined-conditions choice probability (ccCP) was computed to assess choice preferences and compare them across tasks for neurons active in both.

---

### Key findings

- More than half of active parietal neurons were active in only one task (either T-maze or steering-wheel), forming largely distinct but spatially intermingled subpopulations.
- Task specificity was robust across consecutive days: within-task activity correlations were high (r ≈ 0.83 for T-maze, r ≈ 0.77 for steering-wheel), while cross-task correlations were negative or near zero.
- Activity in passive conditions (gray screen, no task) was highly correlated with the active task using the same apparatus (r ≈ 0.63–0.65 within context) and uncorrelated or negatively correlated across contexts (r ≈ −0.10 to −0.16), ruling out task demands, optic flow, and measured movements as the primary driver.
- Running speed, pupil diameter, and facial/whisker movements could not account for context specificity.
- The hybrid steering T-maze task engaged the same neurons as the steering-wheel task (r = 0.74, p ≈ 0), not the T-maze neurons (r = −0.02, p = 0.72), confirming that physical apparatus context — not visual context — determines neural participation.
- Encoding of task-relevant variables (stimulus, choice, reward) was also task specific: neurons well predicted by the encoding model in one task were poorly predicted in the other (negative cross-task correlation of explained variance).
- Neurons inactive in one task nevertheless significantly encoded task-relevant signals of the other task (significant explained variance in 12/21 sessions for SW-inactive cells encoding T-maze variables, and 20/21 sessions for TM-inactive cells encoding SW variables).
- Among the minority of neurons active in both tasks, choice preferences were not correlated across tasks, indicating that even shared-active neurons represent context-specific choice signals.

---

### Computational framework

Not applicable in the sense that the paper does not develop or test a formal computational model. The study is purely empirical. The results constrain theories of mixed selectivity and population coding in parietal cortex. They suggest that parietal cortex does not implement a context-independent, abstract task representation; instead, distinct neural ensembles are selectively recruited by physical context, analogous to pattern separation or remapping in hippocampal circuit models. The results are most naturally interpreted in frameworks concerning context-dependent neural manifolds or ensemble-level state-space dynamics where physical context gates which neural subspace is active.

---

### Prevailing model of the system under study

Before this paper, the dominant view was that parietal cortex is a high-level multifunctional area whose individual neurons exhibit "mixed selectivity" — encoding conjunctions of multiple task variables — and that this mixed selectivity might enable flexible reuse of the same neurons across different behavioural demands. Evidence for this came largely from single-task studies showing that parietal neurons encode motor plans, sensory evidence, choice, spatial position, and other variables simultaneously. Cross-task studies in rodents comparing different sensory modalities (e.g., visual vs. tactile) but using the same physical apparatus had found relatively consistent choice representations, suggesting parietal neurons could generalise across sensory demands. The introduction signals that the authors were testing whether parietal neurons are generalists engaged across tasks, versus specialists confined to particular behavioural contexts.

---

### What this paper contributes

The paper demonstrates that parietal neurons are context specialists, not generalists: most are active only in a specific physical context. This overturns the expectation that mixed selectivity within a task predicts flexible re-engagement across tasks. The key new claim is that the gating mechanism for neural participation is the physical apparatus of the task, not sensory demands or task difficulty. This was established by the passive-condition experiment (showing that specificity persists with no task stimuli or optic flow) and the hybrid-task experiment (showing that visual scene alone does not determine which neurons are recruited). The paper also shows that task-relevant encoding (not just raw activity) is context specific, and that choice representations do not transfer between contexts even for neurons active in both. Together, these results reframe parietal cortex as a collection of context-specific ensembles rather than a unified, task-general decision or navigation circuit.

---

### Brain regions & systems

- **Posterior parietal cortex (PPC), mouse** — the primary region of study; specifically a zone anterior to V1 overlapping with retinotopic visual areas A and RL. Investigated as the candidate site for flexible multitask representation; found instead to contain context-specific subpopulations.
- **Primary visual cortex (V1)** — used as a landmark to localise PPC via widefield retinotopy; not directly studied.
- **Hippocampus** — mentioned in the Discussion as an analogous system showing context-specific place cell remapping (Guzowski et al., 1999; Leutgeb et al., 2005); not recorded.
- **Amygdala** — mentioned briefly as another region potentially showing spatial context specificity (Grundemann et al., 2019); not recorded.

---

### Mechanistic insight

The paper does not fully meet the bar for mechanistic insight at the algorithmic level. It provides rich neural data (two-photon imaging of identified neurons across tasks) and establishes the phenomenon clearly, but it does not propose or test a specific algorithm that explains *why* physical context gates parietal activity. The paper characterises the phenomenon (which neurons participate, when, and under what conditions) but does not map that to a formalised process model. No pharmacological, optogenetic, or connectivity data are provided to address the implementational level.

- **Computational**: The problem being solved is unclear from the paper's framing, but the Discussion speculates that context-specific populations may enable efficient downstream computations by routing context-appropriate signals to different target areas.
- **Algorithmic**: Not formalised. The paper identifies context (physical apparatus) as the relevant variable gating ensemble membership, but the mechanism by which context selects a subpopulation — e.g., through top-down inputs, neuromodulation, proprioception, or learned associations — is not addressed.
- **Implementational**: Not addressed. The paper notes that different parietal neurons project to different targets, raising the possibility that context-specific neurons serve different downstream circuits, but this is speculative.

---

### Limitations & open questions

- The physical apparatus encompasses multiple features simultaneously (posture, proprioceptive feedback, optic flow characteristics, motor report, spatial context). The paper uses "physical context" as a shorthand for this conjunction and acknowledges it cannot determine which specific component(s) are causally responsible.
- The hybrid task dissociates visual from physical context but does not dissociate the motor report from the postural/proprioceptive context; future work varying motor report within the same apparatus would be needed.
- Movement variables (running, pupil, whisking) were measured and found insufficient to explain the specificity, but extensive EMG or full-body motion capture was not performed; posture differences between tasks remain a candidate mechanism.
- The study used two-photon calcium imaging, which misses silent neurons, limits temporal resolution, and may underestimate the true fraction of neurons with cross-task activity.
- It is unknown whether the same context-specific recruitment pattern holds in other cortical regions or is specific to parietal cortex.
- The study was carried out in head-fixed mice; generalisability to freely moving animals is unclear.
- The minority of task-general neurons (active in both tasks) were not characterised in terms of laminar position, projection targets, or cell type.

---

### Connections & keywords

**Key citations**:
- Krumin et al. (2018) eLife — prior work on parietal activity in the T-maze task from the same group
- Burgess et al. (2017) Cell Reports — original steering-wheel task paper
- Raposo et al. (2014) Nature Neuroscience — cross-modality parietal recording showing consistent choice representations
- Nikbakht et al. (2018) Neuron — cross-modal parietal study in same apparatus
- Harvey et al. (2012) Nature — choice-specific sequences in parietal cortex during virtual navigation
- Steinmetz et al. (2019) Nature — distributed coding across mouse brain, including parietal cortex
- Pachitariu et al. (2017) bioRxiv — Suite2p pipeline used for imaging data analysis
- Stringer and Pachitariu (2019) — isolation distance metric used for activity quantification
- Guzowski et al. (1999); Leutgeb et al. (2005) — hippocampal context-specific remapping as analogy

**Named models or frameworks**:
- Isolation distance (Bhattacharyya distance-based activity metric)
- Combined-conditions choice probability (ccCP)
- Ridge regression encoding model
- Suite2p (cell detection and registration pipeline)
- OASIS (spike deconvolution algorithm)

**Brain regions**:
- Posterior parietal cortex (PPC), mouse
- Visual areas A and RL (mouse)
- Primary visual cortex (V1), mouse (landmark only)

**Keywords**:
- task specificity
- parietal cortex
- context-dependent neural activity
- ensemble selectivity
- two-photon calcium imaging
- physical context gating
- mixed selectivity
- cross-task recording
- mouse decision-making
- neural subpopulations
- context remapping
- virtual reality navigation
