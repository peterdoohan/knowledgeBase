---
source_file: schuck2019_hippocampal_replay_nonspatial.md
paper_id: schuck2019_hippocampal_replay_nonspatial
title: "Sequential replay of nonspatial task states in the human hippocampus"
authors:
  - "Nicolas W. Schuck"
  - "Yael Niv"
year: 2019
journal: Science
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - fmri
brain_regions:
  - hippocampus
  - orbitofrontal_cortex
frameworks:
  - reinforcement_learning
  - model_based_rl
  - model_free_rl
keywords:
  - hippocampal_replay
  - sequence_reactivation
  - nonspatial_decision_making
  - multivariate_decoding
  - fmri
  - task_states
  - wakeful_rest
  - orbitofrontal_cortex
  - cognitive_map
  - experience_replay
  - reinforcement_learning
  - partially_observable_states
  - offline_consolidation
  - sequential
  - replay
  - nonspatial
  - task
  - states
  - human
  - hippocampus
key_citations:
  - schuck2016_orbitofrontal_cortex_state
  - wilson2014_best_practices_scientific
  - russek2017_model_based_reinforcement
  - johnson2007_hippocampus_decision
---

### One-line summary

Hippocampal fMRI patterns during wakeful rest reflect sequential replay of nonspatial task states, with the extent of replay correlating with orbitofrontal task-state representation fidelity.

---

### Background & motivation

Rodent studies demonstrate that hippocampal place cells reactivate sequentially during rest and sleep (replay), supporting memory consolidation and planning. However, it remains unclear whether human hippocampal replay occurs for nonspatial, abstract tasks and whether replay supports nonspatial decision-making. This study investigates whether sequential replay of task states can be detected noninvasively in the human hippocampus using fMRI, and whether such replay relates to task representation and performance.

---

### Methods

- **Participants**: 33 healthy adults (22 female, mean age 23.4 years)
- **Task**: Nonspatial decision-making task requiring integration of past and current trial information. Participants judged age (old/young) of either faces or houses from overlaid face-house images. Task rules created 16 distinct "task states" based on combinations of current and previous trial age/category.
- **Design**: Two sessions separated by 1-4 days; each session included task performance (~40 min) flanked by 5-minute resting-state scans (POST rest after task; PRE rest before task for n=10; INSTR control during instructions)
- **fMRI**: 3T Siemens Prisma, T2*-weighted EPI, 2×2×2 mm resolution, TR=3000 ms, TE=27 ms
- **Analysis**: 
  - Support vector machine (RBF kernel) trained to classify 16 task states from hippocampal fMRI during task performance
  - Trained classifier applied to resting-state volumes to decode sequences of states
  - "Sequenceness" analysis: tested whether consecutively decoded states were nearby in task state space (fewer steps apart)
  - Mixed-effects models with state distance as predictor, controlling for classifier bias
  - Simulations verified sensitivity to detect fast replay events (~60-80 ms per item) despite slow fMRI hemodynamics

---

### Key findings

- **Hippocampal state decoding during task**: SVM classifier achieved 11.6% accuracy (chance = 6.25%) in distinguishing 16 task states from hippocampal fMRI during task performance (t32 = 6.7, PFDR = 3.186 × 10⁻⁷)

- **Sequential replay during POST rest**: 
  - Consecutively decoded states in POST rest were separated by fewer steps in task state space compared to INSTR (t32 = 2.4, PFDR = 0.0165), PRE (t9 = 2.3, PFDR = 0.0272), and PERM controls (t32 = 4.6, PFDR = 7.897 × 10⁻⁵)
  - Low-distance transitions (<3 steps) occurred in clusters more frequently in POST than controls (INSTR: t32 = 1.7, PFDR = 0.0482; PRE: t9 = 1.9, PFDR = 0.0482; PERM: t32 = 4.5, PFDR = 9.152 × 10⁻⁵)

- **Sequenceness model**: Logistic mixed-effects models showed significantly better fit when including state distance (sequenceness) regressor in POST (AIC 3642.9 vs 3645.4) but not PRE rest; condition × sequenceness interaction significant (AIC 7219.6 vs 7228.3, PFDR = 3.119 × 10⁻³)

- **Full state representation**: Model comparison showed that sequences were best explained by replay of full task states (AIC 20,781) versus stimulus-only (AIC 20,808), category-only (AIC 20,808), category-memory (AIC 20,806), or backward replay (AIC 20,796) models (all PFDR < 2.2 × 10⁻¹⁶)

- **Hippocampal specificity**: No comparable sequenceness effects found in orbitofrontal cortex control region

- **Link to orbitofrontal representations**: Hippocampal sequenceness at rest correlated with orbitofrontal task-state decoding accuracy during task (r = 0.47, PFDR = 0.0327), but not with hippocampal on-task decoding (r = 0.05, PFDR = 0.769)

- **Behavioral relevance**: Orbitofrontal state decoding accuracy correlated with task error rates (r = –0.14), but hippocampal sequenceness did not directly correlate with behavior (r = –0.21 for error rates, r = 0.28 for reaction times, both PFDR > 0.05)

- **Simulation validation**: Simulations confirmed that the analysis pipeline could detect sequential neural events occurring at ~14 items/second (60-80 ms inter-event intervals) at significance level PFWE < 1 × 10⁻³, despite fMRI's slow temporal resolution

---

### Computational framework

The paper employs a reinforcement learning (RL) framework, specifically drawing on experience replay mechanisms from machine learning. The key computational concepts are:

- **Experience replay**: Originally developed in RL (Sutton, 1990; van Seijen & Sutton, 2015), experience replay involves reactivating past experiences to improve learning efficiency and stability. The paper frames hippocampal replay as a biological implementation of this mechanism.

- **Model-based RL and successor representations**: The paper cites work on predictive representations (SRs; Russek et al., 2017) that link model-based computation to model-free mechanisms through replay. The task requires maintaining and updating a cognitive map of state transitions.

- **Partially observable Markov decision processes (POMDPs)**: The task is explicitly designed as a partially observable decision problem where the current state depends on previous trials, requiring participants to integrate information over time.

The analysis uses multivariate pattern classification (SVM with RBF kernel) to decode latent task states from fMRI patterns, treating the brain as encoding discrete state representations that can be sequentially reactivated.

---

### Prevailing model of the system under study

The prevailing model, grounded in rodent literature, held that:

1. **Hippocampal replay is primarily spatial**: Replay was thought to reactivate spatial trajectories experienced during navigation, with place cells firing in sequences that reflect previously traveled paths (Skaggs & McNaughton, 1996; Nádasdy et al., 1999).

2. **Replay serves memory consolidation and planning**: Reactivation during rest and sleep was linked to memory consolidation (Carr et al., 2011) and planning/forward simulation (Johnson & Redish, 2007), but primarily in spatial contexts.

3. **Human replay is difficult to detect noninvasively**: Due to the temporal limitations of fMRI (slow hemodynamics) and the speed of replay events (~100 ms), detecting replay in humans was considered challenging. Prior human studies relied on sustained activity patterns or sleep-related measures rather than direct detection of sequential reactivation.

4. **Orbitofrontal cortex represents task states**: Previous work (Schuck et al., 2016) had established that the orbitofrontal cortex represents abstract task states during decision-making, but the relationship between hippocampal replay and these representations was unknown.

---

### What this paper contributes

This paper makes several key contributions to the understanding of hippocampal replay:

1. **First demonstration of sequential replay of nonspatial task states in humans**: The study shows that hippocampal replay is not limited to spatial contexts but extends to abstract, nonspatial decision-making tasks. Participants implicitly navigated through a state space defined by task rules, and these sequences were reactivated during rest.

2. **Feasibility of detecting fast replay with fMRI**: Despite fMRI's slow temporal resolution (TR=3s), the study demonstrates that multivariate decoding can detect sequential reactivation occurring on the order of ~100 ms. Simulations confirmed sensitivity to events at 60-80 ms intervals. This establishes a methodological pathway for investigating replay noninvasively.

3. **Link between hippocampal replay and cortical representations**: The study reveals a functional relationship between offline hippocampal replay and online orbitofrontal task-state representations. Hippocampal sequenceness correlated with orbitofrontal decoding accuracy (r=0.47), suggesting replay may train or maintain cortical cognitive maps.

4. **Evidence for forward-directed replay**: Model comparisons favored forward replay of full task states over backward replay or partial state representations (stimulus-only or category-only). This suggests replay may serve memory consolidation rather than planning in this context.

5. **Computational role for replay in nonspatial learning**: The findings support RL theories proposing that replay supports the formation of cognitive maps for complex tasks, extending the functional role of hippocampal replay beyond spatial memory to abstract decision-making.

---

### Brain regions & systems

- **Hippocampus**: Primary focus of the study. Contains sequentially reactivated task-state representations during rest (replay). Shows significant state decoding during task (11.6% accuracy, chance = 6.25%). Replay sequences during rest reflect task structure with nearby states in task space occurring consecutively. No direct relationship between hippocampal replay and behavioral performance.

- **Orbitofrontal cortex (OFC)**: Comparator region. Shows task-state representations during decision-making (replicating prior findings). No replay sequences detected during rest. OFC state decoding accuracy during task correlates with hippocampal sequenceness at rest (r = 0.47), suggesting a functional relationship where hippocampal replay supports OFC task representations. OFC decoding accuracy predicts behavioral performance (error rates).

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight. It provides both algorithmic formalism and neural evidence supporting that algorithm.

**Algorithmic level**: The paper frames hippocampal replay as a biological implementation of **experience replay** from reinforcement learning (Sutton, 1990). The algorithm involves: (1) storing past experiences (task states), (2) reactivating sequences of these experiences during offline periods (rest), and (3) using these reactivations to update value functions or transition models. The study tests whether the hippocampus implements this algorithm by decoding task states and measuring sequential reactivation.

**Neural evidence**: The paper provides neural data specifically supporting the replay algorithm:
- Multivariate decoding of hippocampal fMRI patterns revealed sequential reactivation of task states during rest
- The sequential structure matched the task state diagram (nearby states reactivated consecutively)
- Model comparison favored full state replay over partial representations (stimulus-only, category-only)
- Simulations confirmed sensitivity to detect 60-80 ms sequential events, matching known replay timescales

**Implementation level**: The paper identifies specific neural implementations:
- **Hippocampus**: Locus of sequential replay during rest
- **Orbitofrontal cortex**: Recipient of replay benefits, showing improved task-state representations correlated with hippocampal sequenceness
- **Temporal dynamics**: Replay events occur on ~100 ms timescales, compressed relative to original experience (~4.5 s trials)

**Marr's levels summary**:
- **Computational**: The brain solves the problem of learning and maintaining a cognitive map of task structure to support flexible decision-making. Replay serves to consolidate or refine this map offline.
- **Algorithmic**: Experience replay algorithm reactivates sequences of past task states during rest, with transition probabilities reflecting the true task structure. The algorithm operates on partially observable state representations (integrating past and current information).
- **Implementational**: The hippocampus implements sequential reactivation through brief (~100 ms) multistep replay events. The orbitofrontal cortex maintains online task-state representations that benefit from hippocampal replay. fMRI detects these events through multivariate pattern analysis despite slow hemodynamics.

---

### Limitations & open questions

- **Temporal resolution**: The exact speed of replay events could not be directly determined from fMRI data. Simulations suggest sensitivity to 60-80 ms events, but direct measurement requires electrophysiological methods.

- **Replay direction**: Inferences about forward versus backward replay remain indirect. Forward replay was favored by model comparison, but this could reflect hemodynamic response dynamics rather than true directional bias.

- **Pre-task control sample size**: The pre-task resting-state control (PRE condition) was only collected in 10 participants (group 2), limiting statistical power for some comparisons.

- **Vigilance control**: While heart rates were equated across conditions, more direct measures of vigilance during rest could provide additional insight into the relationship between vigilance and replay.

- **Causal mechanisms**: The correlational link between hippocampal replay and orbitofrontal representations does not establish causality. Whether replay actively trains cortical representations or merely reflects concurrent consolidation processes remains to be determined.

- **Generalization to other tasks**: Whether replay of nonspatial sequences generalizes to other abstract tasks, or is specific to the particular task structure used here, requires further investigation.

---

### Connections & keywords

**Key citations**:
- Skaggs & McNaughton (1996) - seminal rodent replay paper
- Johnson & Redish (2007) - awake replay and planning
- Karlsson & Frank (2009) - awake replay of remote experiences
- Schuck et al. (2016) - orbitofrontal cognitive map of state space
- Wilson et al. (2014) - OFC as cognitive map of task space
- Sutton (1990) - experience replay in reinforcement learning
- Russek et al. (2017) - predictive representations linking model-based and model-free RL

**Named models or frameworks**:
- Experience replay (reinforcement learning)
- Partially observable Markov decision processes (POMDPs)
- Cognitive map theory (Tolman)
- Successor representations
- Multivariate pattern classification (SVM with RBF kernel)

**Brain regions**:
- Hippocampus - site of sequential replay during rest
- Orbitofrontal cortex (OFC) - task-state representation during decision-making, correlated with hippocampal replay

**Keywords**:
- hippocampal replay
- sequence reactivation
- nonspatial decision-making
- multivariate decoding
- fMRI
- task states
- wakeful rest
- orbitofrontal cortex
- cognitive map
- experience replay
- reinforcement learning
- partially observable states
- offline consolidation
