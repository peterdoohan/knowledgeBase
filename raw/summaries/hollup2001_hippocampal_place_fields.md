---
source_file: hollup2001_hippocampal_place_fields.md
title: "Accumulation of Hippocampal Place Fields at the Goal Location in an Annular Watermaze Task"
authors: Stig A. Hollup, Sturla Molden, James G. Donnett, May-Britt Moser, Edvard I. Moser
year: 2001
journal: The Journal of Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Hippocampal place fields accumulate preferentially at a behaviourally significant goal location in a spatially homogeneous environment, demonstrating experience-dependent over-representation of a remembered target even in the absence of any sensory cue marking that location.

---

### Background & motivation

Hippocampal place cells fire in spatially selective patterns and are widely assumed to support goal-directed navigation and spatial memory, but how the hippocampal map relates to specific locations of behavioural importance was unknown. Prior watermaze studies were confounded by restricted animal movement once the goal location was learned, making it impossible to compare place-field distributions across the arena. It was also unclear whether any over-representation of goal locations observed elsewhere depended on sensory properties of the reward object or on internally stored expectation. This paper addresses whether the spatial distribution of hippocampal place fields is shaped by what the animal has learned, independently of concurrent sensory input from the goal.

---

### Methods

- **Subjects:** 13 male Long-Evans rats (400–600 g); 9 trained with a constant platform location, 4 with a variable (pseudorandom) platform location.
- **Task:** Annular watermaze — rats swam in a continuous corridor (198 cm diameter pool with inner and outer transparent walls) with no proximal landmarks. The hidden escape platform was kept submerged for at least one full lap, so animals sampled the entire arena on every trial. Probe trials (platform submerged for 60 sec) were interleaved; all neuronal analyses used only these probe-trial data.
- **Recordings:** Tetrodes implanted in dorsal CA1; up to ~7 units recorded simultaneously per session. 139 units isolated in total (132 pyramidal cells, 7 interneurons). Manual cluster-cutting used for spike isolation.
- **Analysis:** Corridor divided into 60° or 30° segments; firing field location defined as segment of peak average firing rate across probe trials. Directional sorting applied to control for swim-direction confounds. Behavioral controls for linear speed, angular speed, LIA-related EEG changes, and arena coverage were all assessed.
- **Comparison condition:** Rats trained with variable platform location served as a control for non-specific effects of training or arena geometry.

---

### Key findings

- Place fields were non-uniformly distributed: 27/80 cells (33.8%) in constant-platform rats had peak firing in the 60° platform segment, versus an expected 13.3 cells (16.7% chance level); chi-squared test, p < 0.005.
- With 30° segmentation, 19/80 cells (23.8%) peaked in the goal segment versus 8.3% expected; this distribution was nonuniform (chi-squared, p < 0.001), and field accumulation was precisely centred on the platform location.
- The over-representation was independent of platform position in the room (observed across all four platform locations: NE, NW, SW, SE).
- Directional sorting (retaining only preferred swim-direction data) did not attenuate the effect; 24/80 cells peaked in the goal segment after sorting.
- More fields accumulated in the segment immediately preceding the goal (i.e., approaching it) than in the segment following it, consistent with an anticipatory or expectancy signal.
- Rats trained with a variable platform showed no clustering of place fields in any room-defined or platform-relative segment (chi-squared not significant, p > 0.50 in both analyses).
- The accumulation was not explained by slow swimming (no correlation between swim speed and firing rate), angular velocity, LIA-related EEG activity (theta power maintained in the goal segment), or differential arena coverage.
- Field size and peak-to-background firing ratios were comparable between goal-segment and off-target-segment cells.
- A subset of cells (12/19 with goal-area peaks) reduced firing upon the rat reaching the platform; ~42% dropped to <30% of swimming-period rate, consistent with "misplace cell" behaviour.

---

### Computational framework

Not applicable in a formal sense. The paper does not deploy an explicit computational model or formalism. The results are interpreted in the framework of the **cognitive map** (O'Keefe & Nadel, 1978), in which hippocampal place cells collectively form an allocentric spatial representation. The specific finding — non-uniform density of place fields tied to learned behavioural significance — bears on models of how spatial representations are shaped by reinforcement history and expectancy. The results constrain associative or reinforcement-learning models of hippocampal map formation, in which repeated reward at a location could bias synaptic weights to recruit more cells to represent that zone.

---

### Prevailing model of the system under study

The dominant view at the time was that hippocampal pyramidal cells form a distributed, non-topographic cognitive map in which place fields tile the environment roughly uniformly (O'Keefe & Nadel, 1978; Muller et al., 1987). Each cell fires in a spatially selective manner determined primarily by the animal's current location relative to external landmarks. Place fields were thought to be established rapidly upon first environment exposure (within minutes) and to remain stable thereafter, with their distribution shaped mainly by geometric and sensory constraints (e.g., proximity to walls) rather than by learning history or reward. Goal-related modulation of firing had been observed when salient reward objects were present as landmarks, but no pure mnemonic or expectancy-driven modulation of the ensemble distribution had been demonstrated in the absence of any sensory goal cue.

---

### What this paper contributes

The paper shows that spatial learning causes an experience-dependent redistribution of hippocampal place fields, with a disproportionate number of cells representing the learned goal location even when that location is completely unmarked during testing. This cannot be attributed to any concurrent sensory input from the goal object, meaning the effect must arise from stored memory — an association between environmental landmarks and the remembered platform location. The finding moves the hippocampal cognitive map from a purely sensory–geometric representation to one whose structure reflects learned behavioural salience. It also provides the first evidence that the density of the spatial map (i.e., how many cells represent a given location) is a plastic quantity shaped by experience, rather than being fixed by arena geometry. The asymmetry favouring the segment preceding the goal over the segment following it further suggests that hippocampal representation encodes prospective information or expectation, not just current location.

---

### Brain regions & systems

- **Dorsal CA1 (hippocampus)** — primary recording site; proposed locus where goal-related, memory-driven redistribution of place fields occurs. Electrode traces confirmed in CA1 layer, approximately midway between CA3 and subiculum.

No other brain regions are examined or discussed as recording targets in this paper, though the hippocampus-dependence of the task is briefly noted (rats with hippocampal lesions fail to recognise the platform region on probe trials — unpublished data cited).

---

### Mechanistic insight

The paper meets the bar partially but not fully.

It presents neural data (single-unit recordings) supporting a claim about algorithm-level representation — that hippocampal place-field density is non-uniformly distributed in a way that tracks learned goal expectation. However, it does not propose or test a specific algorithm for how this redistribution is implemented. The paper identifies the phenomenon and rules out several confounds, but does not pit competing algorithmic accounts against one another with targeted neural evidence.

Mapped onto Marr's levels:
- **Computational:** The hippocampus solves the problem of representing locations of behavioural importance more richly than neutral locations, potentially supporting goal recognition and navigation via differential coding density.
- **Algorithmic:** Over-representation of the goal is expressed as an increase in the number of place cells whose firing fields are centred on the learned goal location; the asymmetry (more fields just before the goal than after) hints at prospective coding rather than purely retrospective position coding. The mechanism generating this redistribution is not specified.
- **Implementational:** Not addressed. The paper identifies the CA1 layer as the recording site but provides no account of the synaptic, cellular, or connectivity mechanisms by which repeated reward or expectation at a location recruits additional place cells to that region.

---

### Limitations & open questions

- The functional significance of goal-related over-representation is unproven: it is correlated with spatial memory but the causal role is not established.
- Whether place fields follow a relocated platform (reversibility / goal-specificity) was not fully tested; preliminary reversal data (Moser et al., 1999 abstract) were too small to be conclusive.
- The mechanism generating the redistribution is unknown — whether it reflects Hebbian plasticity at goal-location synapses, attentional modulation, neuromodulatory gating, or a combination is not addressed.
- Cells in the goal-segment population appear functionally heterogeneous: some fire like "misplace cells" (suppressed when the rat reaches the platform), others maintain or increase firing on platform contact. What distinguishes these subpopulations is unclear.
- The annular corridor may impose specific geometric or locomotor constraints not present in standard open fields; generalisability to other spatial memory paradigms is not directly assessed.
- Ensemble-level multitetrode recordings from large simultaneous populations were not performed; whether the observed over-representation is carried by a specific subpopulation or is distributed uniformly across CA1 is unknown.

---

### Connections & keywords

**Key citations:**
- O'Keefe & Nadel (1978) — The Hippocampus as a Cognitive Map (foundational cognitive map framework)
- Muller et al. (1987) — Spatial firing patterns in a fixed environment (uniform distribution baseline)
- Morris et al. (1982) — Place navigation impaired in hippocampal lesion rats (watermaze paradigm)
- O'Keefe & Dostrovsky (1971) — Discovery of place cells
- Wilson & McNaughton (1993) — Dynamics of hippocampal ensemble code for space
- Frank et al. (2000) — Trajectory encoding in hippocampus and entorhinal cortex (prospective coding context)
- Wood et al. (1999, 2000) — Goal-approach correlates and memory episode encoding in hippocampus

**Named models or frameworks:**
- Cognitive map (O'Keefe & Nadel, 1978)
- Annular watermaze task (novel paradigm introduced in this paper)
- Misplace cells (O'Keefe, 1976; Ranck, 1973)

**Brain regions:**
- Dorsal CA1 hippocampus

**Keywords:**
- hippocampal place cells
- place field redistribution
- goal representation
- spatial memory
- cognitive map plasticity
- experience-dependent remapping
- annular watermaze
- ensemble coding density
- prospective coding
- probe trial
- theta oscillations
- tetrode recording
