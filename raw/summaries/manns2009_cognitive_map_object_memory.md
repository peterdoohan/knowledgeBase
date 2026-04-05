---
source_file: manns2009_cognitive_map_object_memory.md
title: A cognitive map for object memory in the hippocampus
authors: Joseph R. Manns, Howard Eichenbaum
year: 2009
journal: Learning & Memory
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Simultaneous recordings from rat hippocampal pyramidal neurons show that object location is the primary dimension of ensemble coding, with object identity represented as a secondary cluster within location-based representations, supporting the cognitive map theory.

---

### Background & motivation

The hippocampus is well established as a spatial memory system in rodents, encoding location through place cells, but it is also necessary for nonspatial memory tasks including object recognition. A long-standing theoretical proposal (O'Keefe and Nadel 1978) holds that the hippocampus supports a cognitive map containing not just spatial layout but also the identities of objects encountered at specific locations. What was missing was a direct demonstration of how object-location associations are encoded at the level of neural ensembles — specifically, whether object identity and location are equally weighted or hierarchically organised within the population code.

---

### Methods

- **Subjects**: 4 male Long-Evans rats implanted with chronic tetrode arrays targeting dorsal CA1 and CA3.
- **Task**: Object recognition memory task on a circular track. Rats completed laps; objects (novel per block) were placed at 10 of 12 possible positions. Within each block, objects were encountered in one location for three laps, then moved to a new location — allowing dissociation of object identity and location memory.
- **Recordings**: 43–61 hippocampal pyramidal neurons recorded simultaneously per session (205 total: 149 CA1, 56 CA3).
- **Neural analysis**: Firing rates computed for 0.5 s object-encounter windows. Single-unit ANOVAs tested for effects of location (10 possible) and object identity (10 objects encountered 12 times each). Population-level analysis used Euclidean distance in firing-rate space as a similarity metric; nearest-neighbour classification (k=1) assigned each encounter to its closest match. PCA used for visualisation only. An average-similarity (all-pairs) analysis across four encounter categories (same/different location × same/different object) confirmed nearest-neighbour results.
- **Behavioural analysis**: Exploration duration measured for each object encounter as an index of recognition memory (repetition effect: shorter exploration for repeated objects; relocation effect: longer exploration when objects moved to new location).

---

### Key findings

- **Behavioural memory**: Rats explored repeated objects for shorter durations than novel objects (repetition effect, P < 0.05) and reinitiated exploration when objects were moved to a new location (relocation effect, P < 0.05), confirming episodic-like memory for both object identity and object location.
- **Single-unit location coding**: 60.0% of pyramidal cells (123/205) showed significant firing-rate modulation by location (ANOVA, alpha = 0.01; confirmed with Kruskal-Wallis); chance ~1.3% by shuffle.
- **Single-unit object coding**: 16.6% of cells (34/205) showed significant modulation by object identity; chance ~0.3% by shuffle.
- **Population location coding**: Nearest-neighbour classification correctly identified the same location for 72.7% of encounters on average (chance ~9.7%; P < 0.001 for each session by permutation).
- **Population object coding (within location)**: Restricted to objects at the same location, 19.9% of encounters had their nearest neighbour be another encounter with the same object (chance ~7.7%; P < 0.001 per session).
- **Object identity independent of location**: The nearest-neighbour rate for the same object at different locations (3.3%) did not significantly exceed chance (2.5%; t(3) = 0.19, P > 0.1), indicating that object identity is not represented independently of location.
- **ANOVA on similarity**: Two-factor repeated-measures ANOVA revealed significant main effects of location (F(1,3) = 102.45, P < 0.01), object identity (F(1,3) = 42.19, P < 0.01), and their interaction (F(1,3) = 75.96, P < 0.01). Same-object similarity was significantly higher than different-object similarity only within the same location (P < 0.01), not across locations (P = 0.07, non-significant).
- **Neural correlates of memory**: A neural repetition effect was observed (shorter nearest-neighbour distances for object identity on the second encounter vs. first; t(3) = 3.19, P < 0.05) and a neural relocation effect (longer nearest-neighbour distances for location when an object was moved; t(3) = 2.37, P < 0.05), paralleling the behavioural effects.

---

### Computational framework

Not applicable in the formal sense — the paper does not develop or fit a computational model. The analysis framework is multivariate pattern analysis of neural population activity using Euclidean distance in firing-rate space as a measure of representational similarity, combined with k-nearest-neighbour (k=1) classification. This is a representational geometry approach: the question asked is how object identity and location are arranged as dimensions in the high-dimensional space of ensemble firing rates, rather than fitting an algorithmic model of hippocampal function. The results constrain frameworks — such as attractor network models or cognitive map models — that need to account for the hierarchical (location-primary, identity-secondary) structure of object-location representations.

---

### Prevailing model of the system under study

The paper's introduction situates the work within the cognitive map hypothesis of O'Keefe and Nadel (1978): the hippocampus maintains a spatial map of the environment, with locations indexed by place cells, and can embed nonspatial information (specific objects, events) at those locations. Two parallel anatomical input streams were already established — spatial information arriving via postrhinal cortex and medial entorhinal cortex, and nonspatial information via perirhinal cortex and lateral entorhinal cortex — with both streams converging in hippocampus. Single-unit studies had shown that some individual hippocampal neurons respond to specific objects or odors (and their locations), but the ensemble structure of object-location representations — specifically whether location and identity are co-equal or hierarchically organised at the population level — was unknown.

---

### What this paper contributes

The results establish that the hippocampal population code is hierarchically organised: location is the dominant dimension, with object identity represented as a secondary modulation within location-specific subspaces. Objects are encoded as "points of interest" on the cognitive map rather than as independent representational entities. Critically, object identity cannot be decoded independently of location in the ensemble code — the same object encountered in different locations yields no significant representational similarity across those locations. This moves beyond single-unit accounts by characterising the geometry of object-location binding in neural population space, and provides a mechanistic substrate for episodic memory that grounds object recognition in spatial context.

---

### Brain regions & systems

- **Dorsal hippocampus (CA1 and CA3)** — primary locus of recording and analysis; the region in which place-cell-based location coding dominates and where object identity is represented secondarily within location-defined subspaces.
- **Medial entorhinal cortex** — mentioned as primary spatial input to hippocampus (grid cells); not directly recorded but part of the theoretical framing of parallel input streams.
- **Lateral entorhinal cortex / perirhinal cortex** — mentioned as primary nonspatial (object identity) input to hippocampus; not directly recorded.

---

### Mechanistic insight

The paper meets criterion 1 (it characterises a representational algorithm — hierarchical location-then-identity coding in population firing-rate space) and criterion 2 (it provides neural ensemble recordings specifically supporting this coding structure over alternatives such as equal-weight or identity-primary coding).

- **Computational**: The hippocampus solves the problem of binding object identity to spatial context for episodic recognition memory. The solution exploits location as an organising scaffold, allowing objects to be retrieved in the context of where they were encountered.
- **Algorithmic**: Population firing-rate patterns cluster primarily by location (72.7% nearest-neighbour accuracy), with object identity creating secondary sub-clusters within each location-defined cluster (19.9% within-location object accuracy vs. 3.3% across locations, the latter at chance). Object identity is encoded as a modulation of location-based firing patterns, not as an independent dimension.
- **Implementational**: Recordings are from CA1 and CA3 pyramidal neurons in the dorsal hippocampus using tetrode arrays. No cell-type-specific, connectivity, or neuromodulatory mechanisms are examined. The paper does not address how the hierarchical structure arises from synaptic or circuit-level properties.

---

### Limitations & open questions

- Only four rats, limiting statistical power; one-tailed t-tests used throughout based on a priori predictions.
- Recordings restricted to dorsal hippocampus; ventral hippocampus has larger place fields and might show different location-identity trade-offs.
- The task was incidental object encounter (no explicit reward for remembering objects), so stronger identity coding might emerge with object-directed reward contingencies.
- Objects were encountered in temporal sequence across a session; temporal coding (gradual drift of hippocampal representations over time) could partially contribute to object identity discrimination, and this was not fully disentangled.
- No recordings from upstream areas (entorhinal cortex, perirhinal cortex) to test where the location-primary hierarchy originates.
- The mechanism by which the hierarchical structure arises from hippocampal circuitry (e.g., whether it reflects attractor dynamics, pattern separation/completion, or input-stream weighting) is not addressed.
- Whether species differences in spatial attention could shift the location-identity hierarchy (as the authors speculate) remains untested.

---

### Connections & keywords

- **Key citations**: O'Keefe and Nadel (1978) — cognitive map hypothesis; Wood et al. (1999) — nonspatial correlates of hippocampal single units; Hafting et al. (2005) — grid cells in medial entorhinal cortex; Leutgeb et al. (2005) — independent spatial and episodic codes; McNaughton et al. (2006) — path integration and cognitive map; Kjelstrup et al. (2008) — dorsal-ventral scale of place fields; Manns and Eichenbaum (2006) — evolution of declarative memory; Manns et al. (2007) — temporal coding in hippocampus; Ennaceur and Delacour (1988) — novel object recognition task.
- **Named models or frameworks**: Cognitive map (O'Keefe and Nadel 1978); nearest-neighbour (k-NN) classification (Cover and Hart 1967); novel object recognition task (Ennaceur and Delacour 1988).
- **Brain regions**: Dorsal hippocampus (CA1, CA3); medial entorhinal cortex; lateral entorhinal cortex; perirhinal cortex; postrhinal cortex (parahippocampal cortex).
- **Keywords**: hippocampal ensemble coding, cognitive map, object-location binding, place cells, representational geometry, nearest-neighbour classification, object recognition memory, episodic memory, location primacy, multivariate population analysis, dorsal hippocampus, recognition memory task.
