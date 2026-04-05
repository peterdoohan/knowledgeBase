---
source_file: baram2021_entorhinal_ventromedial_rl.md
title: "Entorhinal and ventromedial prefrontal cortices abstract and generalize the structure of reinforcement learning problems"
authors: Alon Boaz Baram, Timothy Howard Muller, Hamed Nili, Mona Maria Garvert, Timothy Edward John Behrens
year: 2021
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Entorhinal cortex (EC) encodes the relational structure of a non-spatial reinforcement learning task in a way that generalises across different sensory exemplars of the same structure, mirroring its role in spatial remapping, while vmPFC and ventral striatum represent prediction errors in a pattern that depends on task structure.

---

### Background & motivation

Reinforcement learning theory has illuminated the brain's algorithms for learning (value, prediction error) but has said little about how problems are *represented*. A parallel literature on spatial navigation shows that EC and medial PFC harbour structural representations that generalise across environments and behavioural states, enabling rapid transfer of knowledge in 2D space. A natural hypothesis is that the same regions generalise structural knowledge in non-spatial, abstract RL problems — but this had not been directly tested. This paper addresses that gap by designing an RL task that mirrors a spatial remapping experiment, asking whether EC representations preserve relational structure across sensory contexts, and whether standard RL signals (prediction errors) in vmPFC and ventral striatum are also structure-sensitive.

---

### Methods

- **Subjects**: 28 healthy human participants (after exclusions from 32 scanned; aged 21–32, mean 23.4, 18 female); 4-day online training plus one fMRI scan day.
- **Task design**: A 2×2 factorial "task-remapping" paradigm with three 1-armed bandits. Two factors: (1) relational structure — positive (+Corr) vs. negative (−Corr) correlation between two of the bandit reward probabilities; (2) stimuli set — two distinct image triplets. This gave four block types (8 blocks of 30 trials each during scanning).
- **Behavioural modelling**: A modified delta-rule model with cross-terms (STRUCT) capturing how outcome on one stimulus updates estimates for correlated stimuli; compared against a structure-naive Rescorla–Wagner model (NAIVE).
- **fMRI acquisition**: 3T Siemens Prisma, 2×2×2 mm EPI, TR=1.235 s; no spatial smoothing for multivariate analyses, 5 mm FWHM for univariate.
- **Univariate fMRI (GLM1)**: Chosen action values from STRUCT and NAIVE models pitted against each other at stimulus onset to identify regions using relational structure in value coding.
- **Multivariate RSA (GLM2/2a)**: Surface-based searchlight (100-voxel geodesic neighbourhoods); cross-run representational dissimilarity matrices (RDMs) compared against a model RDM where conditions with different relational structures should be more dissimilar than those with the same structure.
- **Prediction error × structure interaction (GLM3)**: Univariate prediction error signal identified in vmPFC and ventral striatum; multivariate searchlight RSA tested whether voxel-pattern of prediction error regressors differed by relational structure.
- **Statistics**: Permutation tests with FWE correction (cluster-mass) for whole-surface results; one-tailed permutation tests for a priori ROIs (EC, vmPFC peaks, ventral striatum).

---

### Key findings

- **Behavioural**: Subjects used relational structure — STRUCT model cross-validated within-structure significantly outperformed NAIVE (t(27)=4.29, p=0.0002); fitted cross-terms confirmed correct use of +Corr/−Corr/0Corr structure (t(27)=13.06, p<10⁻¹²).
- **Univariate value (GLM1)**: mPFC, amygdala, anterior hippocampus, and EC coded positively for STRUCT chosen action value over NAIVE, replicating Hampton et al. (2006) with additional regions.
- **EC relational structure representation (GLM2)**: Strong effect in right EC (p=0.005 small-volume corrected; p=0.01 Bonferroni-corrected for bilateral EC; peak MNI [25,−5,−28]); this was the strongest whole-brain cluster. Representations for the same relational structure (different stimuli) were more similar than those for different structures; no effect in left EC (p=0.73). Effect held when stimuli were collapsed onto a single regressor (GLM2a).
- **Control**: Visual stimulus identity was encoded bilaterally in lateral occipital cortex (p<0.001 FWE), confirming the RSA approach is valid and that the EC effect is not artefactual.
- **Prediction error × structure interaction**: Strong univariate prediction error signal in bilateral vmPFC (t(27)≈9.3–9.4) and ventral striatum (t(27)=10.24). Multivoxel patterns of prediction error signals differed by relational structure in left vmPFC (p=0.014), right vmPFC (p=0.02), and ventral striatum (p=0.034), with exploratory effects also in posterior cingulate cortex and ventrolateral PFC.
- **HRF note**: vmPFC prediction error signal peaked at ~8.5 s post-outcome (vs. standard 6 s in vStr), suggesting a longer haemodynamic delay in vmPFC; results held with the adjusted HRF.

---

### Computational framework

The paper uses **reinforcement learning** as its core framework, specifically a delta-rule (Rescorla–Wagner) model augmented with cross-stimulus update terms to capture relational structure. Key variables are:

- Stimulus value estimates (gbS_t): tracked per stimulus per trial.
- Cross-terms (H_XY): free parameters quantifying how correlated learning is between stimuli; H=+1 (fully correlated), H=−1 (anti-correlated), H=0 (independent).
- Prediction error (ε): standard delta-rule error signal; a "correctness" PE is used in fMRI analyses (sign determined by congruence of choice and outcome).
- Chosen action value: magnitude equals stimulus value but sign reverses on rejection trials.

The authors explicitly note that the behavioural model is descriptive, not a process model of how the brain solves the task. The representational analysis uses **representational similarity analysis (RSA)** to formalise a structural prediction: EC and related regions should produce RDMs where between-structure distances exceed within-structure distances.

The broader theoretical framework draws on the hypothesis that entorhinal/hippocampal representations that encode relational structure in 2D space (grid cells, boundary-vector cells) may generalise to arbitrary abstract state-spaces — a "cognitive map" framework (Behrens et al., 2018).

---

### Prevailing model of the system under study

At the time of this paper, the dominant understanding was as follows. In spatial cognition, EC grid cells and related cells (boundary-vector, object-vector, border cells) are known to generalise their co-activation structure across different environments and behavioural states ("remapping" experiments), enabling efficient transfer of structural knowledge. In RL, success had been achieved in identifying BOLD correlates of value and prediction error (Hampton et al., 2006; Ramnani et al., 2004; Wimmer et al., 2012), but these analyses were univariate — treating prediction error as a scalar signal — and said nothing about the representational format of task structure. The extension of spatial representational mechanisms to abstract, non-spatial problems was a theoretical proposal (Behrens et al., 2018; Garvert et al., 2017; Stachenfeld et al., 2017; Whittington et al., 2020; Wilson et al., 2014), largely without direct empirical support in abstract RL tasks. vmPFC was known to be involved in value comparison and schema-based memory, but its role in fine-grained, structure-sensitive representations of RL learning signals was unexplored.

---

### What this paper contributes

The results extend the "cognitive map" framework from spatial to non-spatial RL by showing that:

1. EC represents the relational structure of an abstract RL task in a format that mirrors its role in spatial tasks — generalising across sensory exemplars of the same structure but differing across different structures. This is the first direct fMRI evidence that EC harbours abstract, non-spatial task-structure representations in humans.
2. vmPFC and ventral striatum do not merely encode a scalar prediction error; the multivoxel *pattern* of the prediction error signal depends on the current relational structure, suggesting these regions represent structure-conditioned learning signals that could support structure-specific credit assignment.
3. Together, these findings suggest a common representational framework for task structure across spatial and non-spatial domains, instantiated in EC, vmPFC, and ventral striatum.

---

### Brain regions & systems

- **Entorhinal cortex (EC), right hemisphere** — primary locus of relational task-structure representation; generalises across stimuli sets within the same structure but remaps between structures.
- **Ventromedial prefrontal cortex (vmPFC)** — (1) encodes STRUCT-model chosen action value in univariate analysis; (2) multivoxel prediction error pattern depends on relational structure; proposed to support structure-conditioned credit assignment and schema integration.
- **Ventral striatum (vStr)** — strong univariate prediction error signal; multivoxel prediction error pattern also depends on relational structure (p=0.034).
- **Medial prefrontal cortex (mPFC)** — positive STRUCT value coding; consistent with Hampton et al. (2006) replication.
- **Anterior hippocampus** — positive STRUCT value coding; consistent with role in model-based RL.
- **Amygdala** — positive STRUCT value coding (replication context).
- **Lateral occipital cortex (LOC)** — bilateral visual stimulus identity coding (control analysis).
- **Posterior cingulate cortex (PCC)** — exploratory: prediction error × structure interaction effect; region also shows grid-like coding and schema representations in other work.

---

### Mechanistic insight

The paper partially meets the bar. It proposes an algorithm (structure-conditioned credit assignment via cross-stimulus prediction error updates) and provides neural data (fMRI RSA) that link representational geometry in EC and vmPFC/vStr specifically to task structure rather than sensory identity. However, the evidence is indirect: fMRI RSA shows that voxel-pattern distances track structure-similarity, but does not resolve the specific cellular or synaptic mechanism. The paper does not provide recordings of identified cell types, nor does it test alternative algorithms against one another at the neural level.

- **Computational**: The brain must represent the relational structure of a problem (which stimuli have correlated outcomes) separately from the sensory particulars, enabling generalisation of structural knowledge to new stimulus sets — an efficient solution to the "learning-set" problem.
- **Algorithmic**: EC encodes a relational geometry over stimuli that is preserved within a structure but changes across structures (analogous to grid-cell co-activation structure preserved across spatial environments). vmPFC and vStr encode prediction errors in structure-specific voxel patterns, consistent with structure-conditioned credit assignment.
- **Implementational**: Not addressed. The paper acknowledges it cannot determine whether hexagonal grid patterns or specific cell types underlie the EC effect, only that the functional computation — structure-generalising representation — is present at the population level in fMRI.

---

### Limitations & open questions

- **Spatial specificity**: Only right EC shows the effect; the hemispheric asymmetry was post hoc and should be treated cautiously.
- **Univariate vs. multivariate**: The prediction error × structure interaction is multivariate and reported at uncorrected p values for pre-specified ROIs; whole-brain FWE-corrected maps are exploratory.
- **No causal evidence**: The study is purely correlational. Whether EC or vmPFC representations are *necessary* for structural generalisation behaviour is unknown.
- **Cellular mechanism unknown**: The paper explicitly disclaims any claim about hexagonal grid patterns or specific cell types; the computational function is established but the implementation is not.
- **Generalisation across task types**: The task manipulates correlation structure of serial bandits; whether the same mechanism operates for other forms of task structure (e.g., hierarchical, graph-structured) is open.
- **Training artefacts**: Subjects underwent 4 days of pre-training and entered the scanner knowing the structure. Whether EC representations develop during learning or require pre-existing structure knowledge is unaddressed.
- **vmPFC HRF**: The delayed HRF in vmPFC (~8.5 s vs. standard 6 s) is noted but not systematically explained; standard analyses may underestimate vmPFC effects.

---

### Connections & keywords

**Key citations**:
- Hampton et al. (2006) — original fMRI demonstration of model-based relational RL in vmPFC (directly replicated)
- Behrens et al. (2018) — "What Is a Cognitive Map?" theoretical framework directly motivating the study
- Garvert et al. (2017) — map of abstract relational knowledge in hippocampal-entorhinal cortex
- Whittington et al. (2020) — Tolman-Eichenbaum Machine unifying space and relational memory
- Stachenfeld et al. (2017) — hippocampus as a predictive map
- Fyhn et al. (2007) — grid cell remapping across environments (spatial analogue of the paradigm)
- Kriegeskorte et al. (2008) — RSA methodology
- Niv (2019) — learning task-state representations

**Named models or frameworks**:
- STRUCT model (extended delta-rule with cross-terms)
- NAIVE / Rescorla-Wagner model
- Representational similarity analysis (RSA) with searchlight
- Cognitive map / abstract state-space framework
- Task-remapping paradigm

**Brain regions**:
- Entorhinal cortex (EC)
- Ventromedial prefrontal cortex (vmPFC)
- Ventral striatum (vStr)
- Medial prefrontal cortex (mPFC)
- Anterior hippocampus
- Lateral occipital cortex (LOC)
- Posterior cingulate cortex (PCC)
- Amygdala

**Keywords**:
- entorhinal cortex, structural generalisation
- reinforcement learning, task structure
- representational similarity analysis, fMRI
- cognitive map, abstract state space
- prediction error, credit assignment
- relational structure, serial bandits
- vmPFC, schema representations
- task remapping, cross-stimulus learning
