---
source_file: epstein2017_cognitive_maps_humans.md
title: "The cognitive map in humans: spatial navigation and beyond"
authors: Russell A Epstein, Eva Zita Patai, Joshua B Julian, Hugo J Spiers
year: 2017
journal: Nature Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

Recent human neuroimaging and intracranial recording work confirms that the hippocampus and entorhinal cortex instantiate map-like and grid-like spatial codes, that retrosplenial and parahippocampal cortices anchor these maps to environmental landmarks, and that hippocampal–frontal circuits support route planning — a system that may extend beyond physical space to social, conceptual, and temporal domains.

---

### Background & motivation

The cognitive map hypothesis, originating with Tolman (1948) and given a neural substrate by O'Keefe and Nadel (1978), holds that the hippocampal formation builds a unified representation of space supporting flexible navigation. Forty years of rodent electrophysiology established place, grid, head-direction, and border cells as the cellular machinery of this map. However, it remained unresolved whether the same functional organisation is implemented in humans, partly because non-invasive neuroimaging cannot access single-unit resolution. The paper synthesises recent advances — particularly MVPA, fMRI adaptation, encoding models, and intracranial recordings in presurgical patients — that together allow a more direct test of cognitive map theory in humans.

---

### Methods

This is a narrative review covering human neuroimaging (fMRI) studies of spatial navigation, complemented by intracranial electrophysiology in epilepsy patients and cross-reference to the rodent literature.

- Scope: Studies of spatial coding, landmark anchoring, and route planning in humans, published primarily in the 2000s–2017.
- Key neuroimaging approaches reviewed: fMRI adaptation (repetition suppression), multivariate pattern analysis (MVPA) / representational similarity analysis (RSA), and encoding models (predicting voxel responses from hypothesised neuronal features such as grid orientation).
- Complementary methods: Intracranial single-unit and multi-unit recordings in humans; structural MRI (hippocampal volume); neuropsychological case studies.
- Extensions reviewed: social spaces, conceptual spaces, episodic memory, and prospective thinking.

---

### Key findings

- Human hippocampus supports map-like spatial codes: fMRI adaptation scales with real-world distance between successively viewed campus landmarks; MVPA patterns in hippocampus reflect spatial and temporal proximity of life-logged events.
- Entorhinal cortex displays grid-like coding: a 60° periodic modulation of fMRI response by movement direction during virtual navigation (Doeller et al., 2010), replicated during imagined navigation; grid-like coding is also present in ventromedial PFC for abstract conceptual spaces (Constantinescu et al., 2016).
- Intracranial recordings confirm place cells in human hippocampus (25% of recorded neurons in a taxi-driver task) and grid-cell-like activity in entorhinal cortex.
- Hippocampal multivoxel patterns show attractor-like all-or-nothing switching between environmental representations under ambiguous conditions, mirroring rodent remapping.
- Retrosplenial cortex (RSC) encodes heading direction in both local (POS subregion) and global (BA29/30) reference frames; local heading codes generalise across geometrically equivalent sub-environments, providing a mechanism for aligning the cognitive map to the world.
- Parahippocampal place area (PPA) represents scene identity and colocated object ensembles; occipital place area (OPA) is causally involved in processing environmental boundaries.
- Entorhinal cortex tracks Euclidean distance to goal; posterior hippocampus tracks path distance; posterior parietal cortex computes egocentric goal direction.
- Posterior hippocampus encodes local street connectivity (degree centrality); anterior hippocampus encodes global connectivity (closeness centrality) during city navigation.
- Lateral prefrontal cortex scales with breadth-first search demands during route replanning; dorsomedial PFC supports hierarchical spatial planning; hippocampal–PFC coupling increases during sequential multi-step route planning.
- Evidence reviewed for extension of spatial coding principles (context retrieval, orientation, route planning) to social hierarchies (hippocampus/posterior cingulate), abstract feature spaces (entorhinal grid-like codes), and episodic/prospective thought.

---

### Computational framework

The review is organised around the cognitive map framework, which proposes that the brain constructs an allocentric Euclidean (or metric) coordinate system in which locations, landmarks, and goals are encoded.

Key sub-frameworks discussed:

- **Grid-cell encoding model**: Predicts fMRI responses from the expected hexagonal symmetry of conjunctive grid cells; the 60° periodic modulation of BOLD by movement direction is used as the empirical signature.
- **Path integration / dead reckoning**: HD cells and grid cells compute a displacement vector from self-motion signals; error accumulates and landmarks are used for recalibration.
- **Attractor network dynamics**: Hippocampal pattern separation and global/rate remapping are framed in terms of attractor networks that discretise overlapping inputs into distinct representations.
- **Vector-based goal coding**: Models (e.g., Byrne et al., 2007) propose that the entorhinal grid network computes a Euclidean goal vector, the hippocampus derives the path around obstacles, and parietal cortex converts to an egocentric turn direction.
- **Graph / topological coding**: Hippocampal representations of street connectivity reflect topological rather than purely metric structure, relevant to planning.
- **Reinforcement learning**: Briefly noted as a framework for linking neural activity during navigation to model-based planning computations.

---

### Prevailing model of the system under study

Prior to the studies reviewed, cognitive map theory was established primarily in rodents: place cells in CA1/CA3, grid cells in medial entorhinal cortex (mEC), HD cells in several structures, and border/boundary cells in subiculum and mEC constituted a well-characterised spatial navigation system. O'Keefe and Nadel's hypothesis placed the hippocampus as the site of an allocentric Euclidean map. In humans, the evidence was largely indirect: hippocampal activation during navigation tasks, increased hippocampal volume in taxi drivers, and broad memory deficits from medial temporal lobe damage. The precise cellular codes described in rodents were assumed likely to exist in humans (given anatomical homology) but could not be directly verified using standard fMRI. The roles of parahippocampal, retrosplenial, and parietal cortices in navigation were documented but mechanistically underspecified. Whether cognitive map mechanisms extended to non-spatial domains was theoretical speculation.

---

### What this paper contributes

The review establishes that the three core elements of cognitive map navigation — spatial coding, landmark anchoring, and route planning — have now been empirically confirmed in humans using convergent methods:

1. Map-like and grid-like codes are demonstrably present in human hippocampus and entorhinal cortex respectively, confirmed by both fMRI and intracranial recording.
2. The division of labour among landmark-sensitive regions is clarified: PPA handles perceptual recognition; RSC mediates reference-frame transformation (local-to-global heading alignment), with a gradient from local (POS) to global (BA29/30) representations; OPA contributes to processing navigational affordances and boundaries.
3. The computational structure of route planning is dissected: entorhinal cortex codes Euclidean distance, hippocampus codes path distance and topological connectivity, and prefrontal cortex evaluates route options and performs hierarchical planning.
4. The review makes the case that the same mechanisms — particularly hippocampal context coding and entorhinal grid-like coding — extend to social spaces and abstract conceptual spaces, moving from metaphor to empirically testable hypothesis.

---

### Brain regions & systems

- **Hippocampus** — encodes map-like spatial codes (distance relationships between locations), pattern-separates environments, codes path distance and street connectivity during navigation; also activated during recall of real-world spatial memories and social navigation.
- **Entorhinal cortex (medial)** — supports grid-like coding (60° periodic fMRI modulation); codes Euclidean distance to goal; extended to grid-like coding of abstract conceptual spaces.
- **Retrosplenial cortex (RSC) / medial parietal cortex (BA29/30, POS)** — anchors cognitive map to environmental landmarks; represents heading direction in local (POS) and global (BA29/30) reference frames; stores long-term spatial knowledge; activated in semantic memory tasks.
- **Parahippocampal place area (PPA)** — represents local scene identity, spatial layout, colocated objects; involved in context retrieval; responds preferentially to stable/large/distant objects.
- **Occipital place area (OPA)** — processes environmental boundaries and navigational affordances; causally involved in boundary representation (shown by TMS).
- **Posterior parietal cortex** — computes egocentric goal direction from allocentric codes; involved in path integration.
- **Lateral prefrontal cortex** — scales with breadth-first search demands during route replanning; implicated in detour problem solving.
- **Dorsomedial / rostrodorsal medial prefrontal cortex** — supports hierarchical spatial planning; shows increased hippocampal coupling during sequential path planning.
- **Caudate nucleus** — associated with response-based (stimulus–response) navigation strategy, contrasting with hippocampal map-based strategy.
- **Posterior cingulate cortex** — codes social distance in the context of social space navigation.
- **Ventromedial prefrontal cortex** — shows grid-like coding for abstract conceptual spaces; performance on spatial knowledge tasks correlates with strength of grid signal here.
- **Subiculum** — contains boundary cells; contributes to long-term spatial memory storage alongside retrosplenial cortex.

---

### Mechanistic insight

The paper partially meets the bar. It reviews evidence that connects a specific algorithm (grid-cell encoding) to neural data (fMRI encoding model results and intracranial recordings), and documents the neural implementation at a coarse level. However, as a review rather than a primary study, it aggregates rather than directly tests mechanistic claims.

- **Computational**: The brain must maintain a continuously updated metric representation of position and orientation in the environment to support flexible navigation (shortcuts, detours, goal-directed route planning).
- **Algorithmic**: Place cells in hippocampus encode location; grid cells in mEC provide a metric coordinate system via path integration; HD cells track heading; border cells anchor the map to environmental boundaries; RSC transforms between local and global reference frames; prefrontal circuits implement search and planning over the stored map.
- **Implementational**: In humans, the grid-like signal manifests as a 60° periodic BOLD modulation in entorhinal cortex consistent with the expected population response of conjunctive grid cells (encoding model approach). Intracranial recordings confirm place cells (~25% of hippocampal neurons) and grid-cell-like periodicity in human entorhinal cortex. Bidirectional cells in rodent RSC (Jacob et al., 2017) provide a specific cellular mechanism for local reference-frame coding that mirrors human fMRI findings. Specific cell types, neuromodulators, or synaptic mechanisms are not addressed in this review.

---

### Limitations & open questions

- Non-invasive fMRI signals reflect population activity across ~600,000 neurons per voxel; direct confirmation of place and grid cell properties requires intracranial recordings, available only in presurgical epilepsy patients.
- Most human navigation studies use virtual environments; vestibular and proprioceptive inputs are absent, which may alter spatial coding.
- The relationship between metric (Euclidean) and topological (graph-based) hippocampal codes is unresolved.
- How cognitive maps stored in neocortex (retrosplenial cortex) after long-term consolidation interact with hippocampal representations during retrieval remains unclear.
- The paper acknowledges no reports of neurons coding the 'boundary' of a concept or social milieu, leaving the extension of landmark-anchoring mechanisms to non-spatial domains speculative.
- How grid- and place-cell mechanisms are engaged in highly familiar environments where hippocampus may be less critical is an open question.
- The egocentric-to-allocentric transformation mechanisms in RSC are posited but not fully characterised computationally.
- Whether the social and conceptual space coding results reflect genuinely map-like representations or a more general hippocampal relational coding remains to be determined.

---

### Connections & keywords

**Key citations**:
- Tolman (1948) — original cognitive map hypothesis
- O'Keefe & Nadel (1978) — hippocampus as cognitive map
- Doeller, Barry & Burgess (2010) — grid cells in human memory network (fMRI)
- Jacobs et al. (2013) — direct recordings of grid-like activity in humans
- Ekstrom et al. (2003) — place cells in human hippocampus (intracranial)
- Morgan, Macevoy, Aguirre & Epstein (2011) — distance representation in human hippocampus (fMRI adaptation)
- Marchette, Vass, Ryan & Epstein (2014) — local spatial reference frames in human medial parietal lobe
- Howard et al. (2014) — entorhinal Euclidean distance coding in London navigation
- Javadi et al. (2017) — hippocampal street connectivity coding and PFC planning
- Constantinescu et al. (2016) — grid-like coding of abstract conceptual space
- Tavares et al. (2015) — hippocampal coding of social space
- Byrne, Becker & Burgess (2007) — computational model of spatial memory and imagery
- Jacob et al. (2017) — bidirectional cells in retrosplenial cortex

**Named models or frameworks**:
- Cognitive map hypothesis (Tolman; O'Keefe & Nadel)
- Grid-cell encoding model (Doeller et al., 2010)
- Path integration / dead reckoning
- Attractor network dynamics (hippocampal remapping)
- Successor representation (mentioned in context of place/goal coding)
- Posterior medial / anterior temporal input systems (Ranganath & Ritchey)
- Scene construction framework (Hassabis & Maguire)

**Brain regions**:
Hippocampus, entorhinal cortex, retrosplenial cortex (RSC), parahippocampal place area (PPA), occipital place area (OPA), posterior parietal cortex, lateral prefrontal cortex, dorsomedial prefrontal cortex, ventromedial prefrontal cortex, caudate nucleus, posterior cingulate cortex, subiculum

**Keywords**:
cognitive map, spatial navigation, place cells, grid cells, head direction cells, fMRI MVPA, entorhinal cortex, retrosplenial cortex, landmark anchoring, route planning, pattern separation, allocentric coding, abstract space, hippocampal-prefrontal circuits
