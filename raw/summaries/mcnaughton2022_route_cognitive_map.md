---
source_file: mcnaughton2022_route_cognitive_map.md
paper_id: mcnaughton2022_route_cognitive_map
title: "Route selection with a cognitive map"
authors:
  - "Bruce L. McNaughton"
  - "Rajat Saxena"
year: 2022
journal: Neuron
paper_type: review
contribution_type: review
species:
  - rat
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - hippocampus_ca3
  - anterior_cingulate_cortex
  - striatum
keywords:
  - hippocampal_replay
  - place_cells
  - cognitive_map
  - route_planning
  - prospective_coding
  - rate_remapping
  - theta_phase_precession
  - hebbian_sequence_learning
  - hippocampal_indexing
  - barrier_navigation
  - spatial_memory
  - hippocampal_striatal_interaction
  - route
  - selection
  - cognitive
  - map
key_citations:
  - tolman1948_cognitive_maps_rats
  - widloski2022_hippocampal_replay_barriers
  - johnson2007_hippocampus_decision
wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

### One-line summary

A Neuron Preview commentary arguing that hippocampal place cell replay sequences constitute the neural substrate of cognitive-map-based route planning, as demonstrated by Widloski and Foster (2022)'s finding that CA1 replay rapidly adapts to reconfigured maze barriers without global place field remapping.

---

### Background & motivation

Since Tolman (1948), neuroscientists have sought to understand how animals make flexible, context-sensitive route choices using an internal spatial representation. The cognitive map hypothesis holds that the hippocampus encodes a stable coordinate framework of the environment, but the mechanism by which this map is used to plan novel or detour routes at decision points remained poorly understood. Prior replay studies were conducted in animals running simple, low-decision-point sequences, leaving open whether hippocampal sequences could flexibly encode structurally complex routes respecting physical barriers. Widloski and Foster (2022) provided a direct test of this in a reconfigurable barrier maze.

---

### Methods

This is a commentary/preview article; it does not report original methods. The methods described belong to the primary study (Widloski and Foster, 2022):

- Large-scale simultaneous recordings of CA1 neurons in rats navigating a complex maze with reconfigurable "jailbar"-style barriers (visible and smellable but not crossable).
- Each session required rats to learn a new goal route constrained by a novel barrier configuration.
- Analysis of place cell stability, rate remapping, and the content of hippocampal replay sequences (comparing alignment to future vs. past trajectories).
- Assessment of barrier conformity in replay sequences across sessions.

---

### Key findings

The following findings are from Widloski and Foster (2022) as reported and interpreted by the authors:

- Hippocampal CA1 place cells maintained stable location-specific firing (no global remapping) across barrier reconfigurations, preserving a stable spatial coordinate framework.
- Replay sequences rapidly adapted to new barrier configurations: 87% of sessions showed high barrier conformity in replay.
- Replay was more closely aligned to future trajectories than past trajectories across all sessions, consistent with a prospective planning function.
- "Rate remapping" — changes in within-field firing rates without place field displacement — correlated with barrier rearrangements, suggesting a mechanism for indexing different experiences at the same location.
- The stable cell subpopulation (mean ~58% per session) alone was sufficient to support barrier-respecting replay; unstable cells encoded local, barrier-specific features.

---

### Computational framework

The paper invokes the framework of Hebbian sequence learning and hippocampal indexing theory:

- **Hebbian phase sequences**: Theta-phase precession (Skaggs et al., 1996) facilitates asymmetric coupling of place cells activated along a route, allowing previously experienced sequences to be reactivated. A consequence is backward expansion of place fields (verified by Mehta et al., 1997).
- **Hippocampal indexing**: The hippocampus serves as an index of cortical representations, linking location-specific inputs with episodic context. Rate remapping is proposed as the mechanism by which the index distinguishes different experiences at the same location.
- **Prospective replay as route planning**: Fictive forward trajectories expressed in CA1 population activity are proposed to represent candidate routes, with successful trajectories potentially biasing synaptic plasticity to reinforce the corresponding neural sequence.

The framework is largely descriptive and theoretical rather than formally specified; no quantitative model is derived in this commentary.

---

### Prevailing model of the system under study

The authors situate the work within the Tolmanian cognitive map tradition. The prevailing model prior to Widloski and Foster held that: (1) hippocampal place cells provide a stable allocentric coordinate framework for the environment; (2) theta-phase precession and Hebbian plasticity enable the encoding of sequential routes through asymmetric place cell coupling; (3) during rest or sleep, previously experienced sequences are reactivated (replay), potentially serving memory consolidation and route evaluation. However, it was unclear whether replay sequences could flexibly represent novel, barrier-constrained routes in complex environments without triggering wholesale place field remapping. The dominant assumption was that route-specific representations required some form of remapping or that replay was largely a retrospective phenomenon.

---

### What this paper contributes

This commentary synthesises the Widloski and Foster (2022) findings to argue that hippocampal replay is genuinely prospective and planning-relevant, not merely retrospective. The key update to the prevailing model is: place field stability and route-sequence flexibility are dissociable — the brain can maintain a stable spatial map while rapidly updating the navigational sequences encoded within it. Rate remapping, rather than global remapping, appears to be the mechanism enabling this dissociation. The commentary also identifies several unresolved questions that the Widloski and Foster results open up, constituting the current frontier of the field (see Limitations & open questions).

---

### Brain regions & systems

- **Hippocampal CA1** — primary locus of place cell recording and replay sequence generation in the reviewed study; proposed site where fictive route trajectories are expressed.
- **Hippocampal CA3** — discussed as a candidate origin of replay sequences due to its recurrent connectivity, which CA1 lacks and which is theoretically necessary for auto-associative sequence generation.
- **Neocortex** — proposed as an alternative or complementary source of hippocampal trajectory initiation; known to show activity sequences correlated with hippocampal replay (Rothschild et al., 2017).
- **Striatum** — discussed as the structure that likely takes over route execution once a route becomes habitual (Packard and McGaugh, 1996); some coordination of reactivation between hippocampus and striatum is noted.
- **Anterior cingulate cortex** — cited (Mashhoori et al., 2018) as a region showing reactivation of remote reward sites, relevant to the broader hippocampal-cortical circuit discussion.

---

### Mechanistic insight

This paper does not itself meet the bar: it is a commentary that interprets another paper's data and does not present a formalised algorithm or new neural recordings.

The primary study discussed (Widloski and Foster, 2022) comes close to meeting the bar — it provides neural recordings linked to a specific proposed computation (barrier-respecting prospective replay) — but this commentary does not develop the algorithmic account in sufficient detail to map onto Marr's levels. The authors explicitly leave open the key algorithmic questions: how replay sequences are initiated, how they are selected from competing alternatives, and how they trigger motor output. The paper is best read as framing the empirical phenomenon and its theoretical stakes rather than resolving the mechanistic account.

---

### Limitations & open questions

The authors explicitly identify the following open questions:

- How do hippocampal fictive trajectories trigger the motor system to execute the corresponding route? What circuits mediate hippocampal output to motor areas (directly or via cortex/striatum)?
- How are appropriate hippocampal trajectories initiated at decision points — random selection from recently encoded routes, or biased by prior success?
- Where do replay sequences originate: CA3 (recurrent connectivity) or externally driven from neocortex?
- How do representations of new barrier configurations suppress or erase old, now-inconsistent ones — erasure or inhibitory suppression?
- What is the precise role of the striatum in route learning and eventual automatisation of familiar routes?
- Whether variability in replay content could support flexible memory storage at different levels of abstraction, enabling generalisation.

---

### Connections & keywords

**Key citations**:
- Widloski and Foster (2022) — primary study being previewed
- Tolman (1948) — cognitive map hypothesis
- O'Keefe — place cell discovery
- Skaggs, McNaughton et al. (1996) — theta-phase precession and temporal sequence compression
- Mehta, Barnes, and McNaughton (1997) — backward expansion of place fields
- Skaggs and McNaughton (1996) — replay of place cell sequences during sleep
- Johnson and Redish (2007) — CA3 forward sweeps at decision points
- Leutgeb et al. (2005) — rate remapping
- Packard and McGaugh (1996) — hippocampus vs. striatum in place vs. response learning
- Rothschild, Eban, and Frank (2017) — cortical-hippocampal-cortical loop during consolidation
- Mashhoori et al. (2018) — anterior cingulate cortex and remote reward reactivation
- McNaughton (2010) — hippocampal indexing theory

**Named models or frameworks**:
- Cognitive map (Tolman)
- Hippocampal indexing theory
- Hebbian phase sequence / theta-phase precession
- Rate remapping
- Prospective replay

**Brain regions**:
- Hippocampal CA1
- Hippocampal CA3
- Neocortex
- Striatum / caudate nucleus
- Anterior cingulate cortex

**Keywords**:
- hippocampal replay
- place cells
- cognitive map
- route planning
- prospective coding
- rate remapping
- theta-phase precession
- Hebbian sequence learning
- hippocampal indexing
- barrier navigation
- spatial memory
- hippocampal-striatal interaction

### Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]
