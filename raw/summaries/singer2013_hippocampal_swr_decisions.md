---
source_file: singer2013_hippocampal_swr_decisions.md
paper_id: singer2013_hippocampal_swr_decisions
title: "Hippocampal SWR Activity Predicts Correct Decisions during the Initial Learning of an Alternation Task"
authors:
  - "Annabelle C. Singer"
  - "Margaret F. Carr"
  - "Mattias P. Karlsson"
  - "Loren M. Frank"
year: 2013
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - rat
methods:
  - tetrode_recording
  - bayesian_decoding
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - prefrontal_cortex
frameworks:
  - attractor_networks
keywords:
  - sharp_wave_ripples
  - awake_replay
  - place_cells
  - spatial_alternation_task
  - memory_guided_decision_making
  - coactivation_probability
  - coordinated_activity
  - trajectory_reactivation
  - hippocampal_cortical_interaction
  - learning_dependent_plasticity
  - hippocampal
  - swr
  - activity
  - predicts
  - correct
  - decisions
  - during
  - initial
  - learning
  - alternation
key_citations:
  - girardeau2009_ripples_spatial_memory
  - davidson2009_hippocampal_replay_extended
  - gupta2010_replay_not_simple_function
  - johnson2007_hippocampus_decision
---

### One-line summary

Hippocampal sharp-wave ripple (SWR) reactivation strength, measured as place cell pair coactivation probability, predicts correct versus incorrect choices on a trial-by-trial basis during early learning of a spatial alternation task.

---

### Background & motivation

The hippocampus exhibits coordinated memory reactivation during SWR events, frequently replaying behavioral trajectories representing past or possible future locations. While SWR disruption impairs spatial learning, the specific role of awake reactivation in memory-guided decision making remains unclear. This study addresses whether SWR reactivation contributes to the evaluation of upcoming choices during hippocampal-dependent spatial learning.

---

### Methods

- **Task**: W-track continuous alternation task where rats must alternate between outer arms (center → left → center → right → center, etc.)
- **Subjects**: 5 male Long-Evans rats, food-deprived to 85-90% baseline weight
- **Recording**: Tetrode recordings from hippocampal CA3 and CA1 during SWR events (150-250 Hz filtered LFP, threshold = mean + 3 SD for ≥15 ms)
- **Analysis focus**: SWR activity when animals were within 20 cm of center well, moving <1 cm/s, preceding outbound trials
- **Performance categories**: (1) <65% correct (initial), (2) 65-85% correct (early learning), (3) >85% correct (first high performance), (4) >85% correct asymptotic
- **Key measures**: 
  - Coactivation probability: proportion of SWRs where both cells in a pair were active
  - Z score for difference in coactivation probability between correct and incorrect trials
  - Coordinated activity: actual coactivation vs. predicted from independent firing
  - Trajectory decoding: Bayesian decoding of spatial locations from SWR spiking

---

### Key findings

- **Greater SWR coactivation precedes correct trials during learning**: Median Z scores for coactivation probability difference were significantly >0 during performance categories 2 and 3 (early learning and first high performance) in both tracks (T1: p < 10⁻⁵, T2: p < 10⁻⁴ vs. 0 and vs. shuffled). No significant difference in categories 1 (initial exposure) or 4 (asymptotic).

- **Trial-by-trial prediction of choices**: Logistic regression using proportion of coactive cell pairs predicted trial outcomes at ~60% accuracy (p < 10⁻⁵ vs. 50% chance) for performance categories 2 and 3. Single-cell activity predictions were only slightly above chance (52%), and previous trial outcome predictions were 56%.

- **Coordinated activity is specific to correct trials**: During learning (categories 2 and 3), coordinated activity (actual > predicted from independent firing) was present on correct trials (p < 10⁻⁵) but not detectable on incorrect trials (p > 0.1). 79% of cell pairs showed coordinated activity on correct trials vs. 54% on incorrect trials.

- **Trajectory representation during SWRs**: SWRs preceding correct trials showed bias toward outbound trajectories (p < 0.005). Both correct and incorrect future paths were reactivated during SWRs on correct trials (no significant bias toward either). Similarly, both actual past and alternative past paths were reactivated during inbound events.

- **Mechanism of prediction**: Lower coactivation on incorrect trials was largely due to high proportion of cell pairs that were never coactive (605/778 pairs for incorrect vs. 27/778 for correct in categories 2 and 3). Excluding these "never coactive" pairs eliminated significant differences between correct and incorrect trials.

---

### Computational framework

The paper employs a **dynamical systems/ensemble coding** framework combined with **Bayesian decoding** of spatial trajectories. The core computational ideas are:

- **Coactivation probability**: Treats place cell pairs as encoding units whose joint activity during SWRs represents spatial trajectories. The probability of pairwise coactivation is the fundamental quantity that predicts behavioral outcomes.

- **Z-score normalization**: Statistical framework comparing observed coactivation differences to what would be expected under null hypothesis of no difference between correct/incorrect trials, accounting for varying numbers of SWRs.

- **Bayesian trajectory decoding**: Probabilistic inference of spatial location from ensemble spiking activity, treating the posterior over locations as representing the content of replay/reactivation events.

- **Coordinated vs. independent activity**: Mathematical comparison of actual joint activity to product of marginal activation probabilities tests whether cells fire independently or are coordinated (assembly-like activity).

The framework assumes that SWR reactivation provides a substrate for memory-based decision making by reactivating representations of possible trajectories that can be evaluated by downstream structures.

---

### Prevailing model of the system under study

Prior to this work, the field understood that:

1. **SWRs reactivate spatial memories**: Hippocampal SWR events replay past experiences and possible future trajectories, with reactivation strength correlating with subsequent memory performance.

2. **SWRs are necessary for learning**: Disrupting SWRs impairs spatial memory consolidation during sleep and spatial learning during behavior.

3. **SWR reactivation is strongest in novel environments**: New experiences drive high levels of coordinated activity during SWRs, which decreases with familiarity.

4. **SWRs may aid navigation**: Reactivation events could represent recent and possible future paths to support ongoing memory-guided navigation, but this hypothesis had not been directly tested with respect to choice behavior during learning.

The specific relationship between SWR reactivation content/strength and trial-by-trial decision-making during learning was unknown.

---

### What this paper contributes

This paper establishes that **SWR reactivation strength predicts correct decisions on a trial-by-trial basis during early learning**, but not after task mastery:

1. **Quantitative link between reactivation and decisions**: Greater place cell pair coactivation during SWRs preceding correct trials (vs. incorrect) can predict trial outcomes with ~60% accuracy, significantly better than single-cell activity or previous trial history.

2. **Specificity to learning phase**: The predictive relationship is strongest during initial task acquisition (65-85% correct performance) and disappears once animals reach asymptotic performance, suggesting SWR reactivation is particularly important for early learning but not for well-learned habit performance.

3. **Mechanism**: Errors during learning reflect a failure to reactivate possible choices—low coactivation probability on incorrect trials is due to many cell pairs never being coactive, rather than reduced single-cell activity. Coordinated activity (above independent firing) is present on correct trials but not detectable on incorrect trials during learning.

4. **Content of reactivation**: SWRs preceding correct trials represent multiple possible trajectories (both correct and incorrect future paths), suggesting reactivation provides information about possible choices to downstream evaluation systems rather than directly signaling the correct answer.

5. **Temporal dynamics**: Coactivation preceding correct trials remains high from first exposure through initial high performance, then drops during asymptotic performance. Coactivation preceding incorrect trials drops early in learning and stays low.

---

### Brain regions & systems

- **Hippocampus CA1**: Primary recording location; locus of SWR events and place cell reactivation. Coactivation probability during SWRs in CA1 predicts trial outcomes.

- **Hippocampus CA3**: Secondary recording location; some cells recorded from CA3. Similar coactivation patterns observed in CA3 and CA1 when analyzed separately.

- **Prefrontal cortex (implied)**: Not directly recorded, but discussed as potential downstream evaluator of reactivated trajectory information for decision making.

---

### Mechanistic insight

This paper provides **partial mechanistic insight** at the algorithmic level but does not fully meet the high bar for complete mechanistic explanation (which would require explicit neural data linking model variables to specific physiological mechanisms).

**Computational level**: The brain must solve the problem of using past experience to evaluate possible future choices during memory-guided decision making. SWR reactivation provides a mechanism for sampling possible trajectories based on past experience.

**Algorithmic level**: The paper proposes that hippocampal place cell pairs encode spatial trajectories through their joint activity during SWRs. Coactivation probability serves as a readout of memory reactivation strength. The algorithm involves: (1) reactivation of place cell pairs during SWRs at the decision point, (2) representation of multiple possible trajectories (both correct and incorrect future paths), (3) coordinated activity (above independent firing) that is stronger before correct trials, and (4) downstream evaluation of these reactivated representations to guide choices.

**Implementational level**: The paper does not address specific biophysical mechanisms (ion channels, synaptic plasticity rules, specific cell types, neuromodulators) that implement the algorithm. It focuses on ensemble-level spiking activity rather than intracellular mechanisms. The physical implementation is at the level of CA3-CA1 place cell assemblies and their coordinated firing during SWR events, but the specific biophysical basis of this coordination is not addressed.

---

### Limitations & open questions

- **Causal role not established**: While the paper shows a predictive relationship between SWR coactivation and correct choices, it does not establish causality. The correlation could reflect other processes that co-occur with successful decision making.

- **Downstream mechanisms unknown**: The paper proposes that reactivation provides information to downstream brain regions for evaluation, but the specific circuits and mechanisms of this evaluation are not identified.

- **Content-behavior relationship unclear**: While reactivation events represent both correct and incorrect future paths, the specific relationship between reactivation content and behavioral choice on individual trials remains weak and unclear.

- **Reverse vs. forward replay ambiguity**: Place cells in this study were active in both directions of motion, making it impossible to unambiguously distinguish forward from reverse replay events.

- **Limited to early learning**: The predictive relationship disappears after asymptotic performance, raising questions about what mechanisms support decision making after initial task acquisition.

- **No specific biophysical mechanism**: The paper does not address the cellular or synaptic mechanisms that generate coordinated activity or that differ between correct and incorrect trials.

---

### Connections & keywords

**Key citations**: Foster and Wilson (2006); Cheng and Frank (2008); Karlsson and Frank (2008, 2009); Jadhav et al. (2012); Dupret et al. (2010); Girardeau et al. (2009); Ego-Stengel and Wilson (2010); Davidson et al. (2009); Gupta et al. (2010); Johnson and Redish (2007); Carr et al. (2011); Frank et al. (2000, 2004); Kim and Frank (2009)

**Named models or frameworks**: Sharp-wave ripple (SWR) reactivation; Coactivation probability framework; Bayesian trajectory decoding; Prospective/retrospective coding; Attractor network dynamics (implied)

**Brain regions**: Hippocampus CA1; Hippocampus CA3

**Keywords**: sharp-wave ripples, awake replay, place cells, spatial alternation task, memory-guided decision making, coactivation probability, coordinated activity, trajectory reactivation, hippocampal-cortical interaction, learning-dependent plasticity
