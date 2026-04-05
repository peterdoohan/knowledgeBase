---
source_file: maisson2023_navigational_variables_prefrontal.md
title: "Widespread coding of navigational variables in prefrontal cortex"
authors: David J.-N. Maisson, Roberto Lopez Cervera, Benjamin Voloh, Indirah Conover, Mrunal Zambre, Jan Zimmermann, Benjamin Y. Hayden
year: 2023
journal: Current Biology
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Single neurons across six prefrontal regions in freely moving macaques encode navigational variables (position, head direction, boundary distance, linear and angular velocity) with random mixed selectivity and a ventral-to-dorsal gradient of coding strength.

---

### Background & motivation

Navigation has traditionally been considered a specialised function of the hippocampal complex, reflecting a modular view of functional neuroanatomy. A growing literature challenges this modularity, showing that motor and reward signals are encoded far beyond their canonical regions. The authors ask whether navigational variables are similarly distributed across the prefrontal cortex (PFC), which is typically studied for its roles in action planning, conflict resolution, and value comparison rather than spatial encoding. The paper tests whether such navigational signals exist in PFC and, if so, how they are organised across areas and neurons.

---

### Methods

- **Subject population**: Two adult rhesus macaques (subjects Y and W) performing a freely moving foraging task.
- **Task design**: Animals foraged in a large open enclosure (245 × 245 × 275 cm) with four reward stations. Approaching and lever-pressing a station delivered juice reward; each station deactivated after five presses for 3 min.
- **Neural recordings**: 8,276 neurons recorded across 196 sessions from six PFC regions: orbitofrontal cortex (OFC), dorsal anterior cingulate cortex (dACC), supplementary motor area (SMA), ventrolateral PFC (vlPFC), dorsolateral PFC (dlPFC), and dorsal premotor cortex (PMd), via 128 independently moveable electrodes.
- **Pose tracking**: OpenMonkeyStudio used for markerless 3D tracking of body and head position.
- **Encoding model**: Linear-Nonlinear Poisson-distributed Generalized Additive Model (LN-GAM) fit to eight variables: lever pressing, 3D body position, head elevation, allocentric head direction (yaw), head tilt (pitch/roll), egocentric boundary distance, angular velocity, and linear velocity. Ten-partition, 5-fold cross-validation to control false positives.
- **Non-navigational variables**: Lever pressing, rewards remaining in environment, rewards remaining at current patch, stay/leave choice, and estimated stay/leave probability (from sigmoid fit).
- **Population analyses**: ePAIRS (elliptical projection angle index of response similarity) to test for functional clustering; linear SVM decoder to assess decodability of position from population activity.
- **Gradient analysis**: Spearman and Pearson correlations of encoding weight with anatomical position (area rank and electrode depth) along medial and lateral ventral-to-dorsal series.

---

### Key findings

- A statistically significant proportion of neurons in all six PFC regions encoded each of the five navigational variables (position, head direction, boundary distance, angular velocity, linear velocity; p < 0.0001, binomial tests in all structures).
- In OFC, ~42–43% of neurons showed selectivity to 3D position or 3D head orientation; proportions were broadly similar in the other five regions.
- Encoding was stable within sessions (first/second-half correlations typically r > 0.5–0.9 across structures).
- Navigational tuning was not place-cell-like: tuning curves were spatially unstructured and broadly distributed rather than confined to discrete fields.
- Non-navigational task variables (reward count, stay/leave choice, leave probability) were also encoded in significant proportions across regions, at comparable rates to navigational variables.
- ePAIRS analysis revealed significantly negative clustering indices in all structures, indicating that neurons encoding navigational and non-navigational variables are randomly intermixed with no evidence of functional subpopulations.
- A linear SVM decoder reliably classified the animal's 2D position from population activity in all six regions (well above 11.1% chance).
- Encoding strength for all navigational variables (and non-navigational variables) increased along a ventral-to-dorsal gradient, on both medial (OFC→dACC→SMA→PMd) and lateral (OFC→vlPFC→dlPFC→PMd) axes. Effect sizes: Spearman r² ranged from ~0.05 to 0.125 across variables and gradient series (p < 0.0001 in all cases).

---

### Computational framework

Not applicable in a strict formal sense — no computational model is developed or fit. The paper uses an encoding model (LN-GAM) as an analysis tool to quantify neural selectivity, but the LN-GAM is a statistical fitting procedure rather than a process-level computational account.

The results are framed within the conceptual framework of **distributed/mixed-selectivity coding** and **cognitive mapping**. The key theoretical claim is that navigation is a special case of the general problem of encoding relational structure: navigational variables are not computed in a dedicated hippocampal module but are encoded widely, in the same neurons that encode reward and choice, via high-dimensional mixed selectivity. The ventral-to-dorsal gradient is interpreted within a hierarchical view of PFC in which more dorsal regions represent information in an "untangled" format more accessible to the motor system.

---

### Prevailing model of the system under study

The dominant model at the time of publication held that spatial navigation is predominantly subserved by hippocampal and parahippocampal circuits — a modular view in which place cells, grid cells, head-direction cells, and boundary cells implement an allocentric spatial map. The PFC was assigned an indirect role in navigation (goal representation, planning, spatial working memory) rather than a direct role in encoding moment-to-moment navigational variables. This view was reinforced by the relative absence of place-cell-like activity in PFC and by theories that assign PFC functions such as action control, conflict resolution, and value comparison rather than spatial coding. The introduction acknowledges a small body of rodent and human evidence suggesting navigational signals outside the hippocampus, but frames this as limited, species-specific, and contested, particularly in primates.

---

### What this paper contributes

The paper provides direct single-neuron evidence that navigational variables are not confined to the hippocampal complex in primates: all five variables tested are robustly encoded across all six PFC regions examined. This extends and grounds in primary data the hypothesis that navigational encoding is distributed across cortex, at least in macaques. Crucially, the navigational signals are carried by the same neurons that encode reward and choice (mixed selectivity, no clustering), which supports the view that navigation is continuous with general associative cognition rather than implemented in a dedicated module. The ventral-to-dorsal gradient of encoding strength refines this by showing that not all PFC regions contribute equally: more dorsal areas encode navigational variables more strongly, suggesting a functional hierarchy within PFC. Together, these results challenge the modular hippocentric view and support the interpretation that PFC participates directly in spatial self-localisation during free behaviour.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)** — ventral anchor of the anatomical gradient; encodes navigational and task variables at rates comparable to other regions but with lower encoding strength; previously linked to spatial encoding and cognitive map functions.
- **Dorsal anterior cingulate cortex (dACC)** — encodes all navigational variables; part of the medial gradient; previously associated with value-based and conflict-related signals.
- **Supplementary motor area (SMA)** — encodes all navigational variables; part of the medial gradient; typically studied for motor planning and action sequencing.
- **Ventrolateral PFC (vlPFC)** — encodes all navigational variables; part of the lateral gradient.
- **Dorsolateral PFC (dlPFC)** — encodes all navigational variables; part of the lateral gradient; classically associated with working memory.
- **Dorsal premotor cortex (PMd)** — dorsal anchor of both medial and lateral gradients; highest encoding strength; typically associated with motor preparation and action selection.
- **Hippocampal complex** — the canonical navigational system, invoked as the baseline comparison; not directly recorded but central to the theoretical framing.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It provides neural recordings that establish correlational encoding of navigational variables across PFC, but it does not formalise an algorithm for how PFC computes or uses navigational information, nor does it provide evidence that specifically supports one algorithmic account over alternatives. The encoding model is descriptive. The paper cannot determine whether PFC navigational signals are generated intrinsically or received from hippocampus or entorhinal cortex, and it explicitly acknowledges this limitation. Causal manipulations are absent.

The paper documents what could be called the implementational substrate for navigational computation in PFC (which neurons, which regions, what gradient), but this is without a corresponding computational or algorithmic account.

---

### Limitations & open questions

- Gaze direction was not measured, preventing disambiguation between allocentric head direction (facing direction) and spatial view (where eyes are looking) — a distinction shown to matter in hippocampal studies of freely moving macaques.
- Non-navigational variables (rewards remaining, stay/leave choice, leave probability) could not be included simultaneously in the LN-GAM alongside navigational variables, preventing direct within-model comparisons of encoding strength.
- The lack of rigid trial structure limited analysis of navigational encoding specifically during task-engaged epochs versus passive movement.
- It is unknown whether navigational signals in PFC are generated locally or inherited from interconnected regions (hippocampus, entorhinal cortex, retrosplenial cortex).
- Whether PFC navigational signals play a causal role in navigation remains untested; correlational encoding does not establish functional necessity.
- Firing rates were notably lower than in standard primate physiology, raising questions about whether offline-selected neurons are representative.
- Findings are from only two subjects, and generalisability to other primates or humans requires further study.
- The relationship between the diffuse, non-place-cell-like PFC tuning and the more structured hippocampal tuning in macaques remains unclear — whether this reflects species differences or region differences is unresolved.

---

### Connections & keywords

**Key citations**:
- Mao et al. (2021) — navigational tuning in freely moving macaque hippocampus using the same LN-GAM approach
- Hardcastle et al. (2017) — LN-GAM methodology developed for medial entorhinal cortex
- Raposo et al. (2014) — category-free mixed selectivity in posterior parietal cortex; ePAIRS method
- Behrens et al. (2018) — cognitive map as organiser of flexible behaviour
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as predictive map
- Maisson et al. (2021) — ventral-to-dorsal gradient of economic variable encoding on medial PFC wall
- Fusi, Miller & Rigotti (2016) — why neurons mix: high-dimensional mixed selectivity
- Bala et al. (2020) — OpenMonkeyStudio pose tracking

**Named models or frameworks**:
- LN-GAM (Linear-Nonlinear Poisson Generalized Additive Model)
- ePAIRS (elliptical projection angle index of response similarity)
- Mixed selectivity framework
- Cognitive map theory
- Hierarchical PFC model

**Brain regions**:
- Orbitofrontal cortex (OFC)
- Dorsal anterior cingulate cortex (dACC)
- Supplementary motor area (SMA)
- Ventrolateral PFC (vlPFC)
- Dorsolateral PFC (dlPFC)
- Dorsal premotor cortex (PMd)
- Hippocampal complex (reference system)

**Keywords**:
- Spatial navigation, prefrontal cortex, macaque
- Mixed selectivity, distributed coding
- Place cells, head direction cells, boundary distance
- Allocentric position encoding
- Ventral-to-dorsal gradient, PFC hierarchy
- Freely moving primates, open-field foraging
- LN-GAM encoding model
- Navigational variables, non-modular navigation
