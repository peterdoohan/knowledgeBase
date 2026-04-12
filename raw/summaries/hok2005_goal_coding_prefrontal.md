---
source_file: hok2005_goal_coding_prefrontal.md
paper_id: hok2005_goal_coding_prefrontal
title: "Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex"
authors:
  - "V. Hok"
  - "E. Save"
  - "P. P. Lenck-Santini"
  - "B. Poucet"
year: 2005
journal: "Proceedings of the National Academy of Sciences USA"
paper_type: empirical
contribution_type: empirical
species:
  - rat
tasks:
  - foraging_task
  - navigation_task
methods:
  - electrophysiology
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - striatum
  - ventral_striatum
keywords:
  - goal_coding
  - spatial_navigation
  - medial_prefrontal_cortex
  - prelimbic_cortex
  - infralimbic_cortex
  - place_cells
  - motivational_salience
  - path_planning
  - hippocampus_prefrontal_interaction
  - unit_recording
  - place_preference_task
  - goal_directed_navigation
  - coding
  - spatial
  - goals
  - prelimbic
  - infralimbic
  - area
  - rat
  - frontal
key_citations:
  - hollup2001_hippocampal_place_fields
---

### One-line summary

Neurons in the rat medial prefrontal cortex (prelimbic/infralimbic area) preferentially fire at spatial goal locations during a place navigation task, suggesting mPFC encodes motivational salience of places for path planning.

---

### Background & motivation

Spatial navigation requires not only knowing one's current position (supported by hippocampal place cells) but also representing the location of goals. Prior work had established hippocampal place cells as the primary neural substrate for location coding, but failed to identify where goal-related spatial information is encoded. Earlier recordings of prelimbic/infralimbic (PL/IL) neurons during simple foraging found no location-specific firing, leaving open whether mPFC participates in spatial coding at all. This paper addresses the gap by asking whether PL/IL neurons display spatial correlates specifically during a task that demands goal-directed navigation.

---

### Methods

- **Subjects**: 10 Long Evans male rats, food-deprived to 85% body weight.
- **Task**: Place preference task in a gray cylinder (76 cm diameter). Rats had to locate and enter an unmarked 10 cm-radius trigger zone to release a single food pellet from an overhead feeder; the pellet scattered widely, so food consumption was spatially dissociated from the goal zone. This design allows goal value and reward value of locations to be independently assessed.
- **Neural recordings**: Driveable bundles of 10 nichrome microwires implanted in either PL/IL (n = 272 cells) or dorsal anterior cingulate area (CgAd; n = 135 cells) of mPFC. Single-unit activity recorded during 35-min sessions.
- **Analyses**: Spatial firing rate maps constructed; place fields defined as ≥9 contiguous pixels above mean firing rate; speed-firing correlations computed and cells with significant speed correlations excluded. Field centroids plotted to assess spatial distribution. Navigation vs. foraging episode comparisons performed to rule out task-event confounds. Rotation/relocation of cue card and feeder tested in a subset of sessions.

---

### Key findings

- ~25% of PL/IL neurons (69/272) had clear spatial correlates during the navigation task; only 4% of CgAd neurons (6/135) showed spatial correlates, consistent with known hippocampal projections preferentially targeting PL/IL.
- After excluding cells whose firing could be explained by speed covariation, 53 valid place fields remained.
- Place fields were not homogeneously distributed: 19/53 centroids fell near the trigger zone, 22/53 near the landing zone (where the food pellet typically landed), and only 12/53 in other locations (chi-squared = 47.6, df = 5, p < 0.0001). This means ~77% of fields were near the two fixed goal locations.
- PL/IL place fields were larger and less spatially coherent than hippocampal place cells (spatial coherence: 0.48 vs. 0.68; field size: 146 vs. 114 pixels at mean-rate threshold; much larger at low threshold).
- Firing in trigger and landing zone fields was comparable during task-related navigation episodes vs. foraging episodes (e.g., 4.27 vs. 4.33 AP/s for trigger zone cells), ruling out event-driven explanations.
- Rotating the cue card + trigger zone by 90° did not shift landing zone fields, but relocating the feeder (thus changing the landing zone location) did shift landing zone fields, confirming goal-related rather than reward-driven coding.

---

### Computational framework

The paper does not implement a formal computational model but proposes a conceptual framework grounded in spatial navigation modelling. The authors suggest that the broad, gradient-like place fields of PL/IL cells (centred on goals but covering wide areas of decrementing activity) could implement a form of gradient ascent for path planning: a rat distant from its goal would experience low but nonzero mPFC firing, which increases as it approaches the goal, allowing simple gradient-following to guide navigation. This is framed in terms of distributed spatial navigation models that assign distinct functions (position coding, goal localisation, path planning) to distinct areas connected in a network (referencing Banquet et al. 2002, Mizumori et al. 2000, Brown & Sharp 1995). The framework assumes motivational salience is spatially represented in a prefrontal network that interfaces with hippocampal position signals and downstream striatal motor output.

---

### Prevailing model of the system under study

The dominant view at the time held that the hippocampus, via its place cells, was the central structure for spatial navigation, with head direction cells providing complementary directional information. While models acknowledged the need for a distributed network including goal representation and path planning modules, the locus of goal coding was unspecified. PL/IL area of mPFC was known to be involved in higher-order cognition, working memory, and to receive monosynaptic, LTP-modifiable input from the ventral hippocampus, but prior recordings during simple foraging had found no location-specific firing in mPFC. The assumption was therefore that mPFC contributes to spatial behaviour through working memory or temporal organisation rather than through direct spatial coding.

---

### What this paper contributes

This paper provides the first direct electrophysiological evidence that rat mPFC (PL/IL) neurons encode spatial goals — not just current position or reward. By dissociating goal locations from reward consumption locations, the authors demonstrate that the overrepresentation of goal locations in PL/IL firing maps reflects motivational salience rather than reward itself. This establishes a new functional property for mPFC neurons in spatial navigation: goal-cell activity. The results support the existence of a prefrontal goal-coding system that, combined with hippocampal position coding and ventral striatal motor selection, would form the substrate for path planning. The paper also establishes that this property is specific to PL/IL (not CgAd) and is task-contingent (absent during simple foraging).

---

### Brain regions & systems

- **Prelimbic/infralimbic cortex (PL/IL)** — primary region of interest; identified as the locus of goal-related spatial coding, with ~25% of recorded neurons showing place fields overrepresented at goal locations.
- **Dorsal anterior cingulate area (CgAd)** — comparison region; very few spatial correlates (4%), consistent with its weaker hippocampal connectivity and suggesting spatial goal coding is specific to PL/IL.
- **Medial prefrontal cortex (mPFC)** — broader label encompassing PL/IL and CgAd; implicated in higher-order cognition and path planning.
- **Hippocampus** — discussed as the partner structure providing place (position) information via direct projections to PL/IL; hippocampal place cells are the comparative standard throughout.
- **Ventral striatum** — proposed as a downstream target where PL/IL goal signals could bias motor output for goal-directed navigation.

---

### Mechanistic insight

The paper meets the first criterion (it proposes a computational algorithm — gradient ascent over goal-centred place fields — as a mechanism for path planning) and the second criterion (it provides neural recording data from mPFC during behaviour). The data show that PL/IL neurons fire most strongly at goal locations, and that this signal is stable across behavioural contexts and tracks goal relocation. Together, these results directly support the proposed algorithm over purely reward-driven or event-driven alternatives.

**Computational level**: The problem the brain must solve is locating and navigating to a spatial goal that is not sensorily marked. The mPFC must represent the motivational salience of places to enable path planning.

**Algorithmic level**: PL/IL neurons maintain broad, goal-centred place fields covering large areas with a spatial gradient of firing rates. A gradient ascent mechanism — moving in the direction that increases firing — could guide navigation to the goal even from distant starting positions. The ensemble signal effectively creates an activity landscape peaked at goal locations.

**Implementational level**: The paper identifies the specific subregion (deep layers of PL/IL) and relies on established anatomy (monosynaptic hippocampal-to-PL/IL LTP-modifiable projections) as the substrate. However, specific cell types, microcircuitry, or neuromodulatory mechanisms are not addressed. This level is therefore only partially supported.

---

### Limitations & open questions

- The recording technique cannot guarantee perfect single-unit isolation on all occasions; rare false assignments acknowledged but argued not to affect main conclusions.
- Only male rats were used; generalizability across sexes is unknown.
- The role of odour cues cannot be completely ruled out despite floor cleaning between sessions.
- Simultaneous recording of hippocampal and mPFC neurons was not performed; how the two systems interact dynamically during navigation remains unknown.
- Whether similar goal-coding neurons exist in other species or under other task demands is not tested.
- The gradient ascent speculation, while plausible, is not tested computationally or behaviourally in this paper.
- CgAd showed very few spatial cells; the basis for this dissociation beyond anatomical connectivity differences is not explored.
- How goal representations are initially acquired and updated during learning is not addressed.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Nadel (1978) — *Hippocampus as a Cognitive Map* (foundational hippocampal spatial framework)
- Banquet et al. (2002) — distributed spatial navigation model with motivational nodes
- Jay et al. (1995); Ferino et al. (1987) — hippocampal projections to PL/IL
- Lenck-Santini et al. (2002) — hippocampal place cell recording under same task conditions
- Hollup et al. (2001) — hippocampal place field accumulation near escape platform
- Jung et al. (1998, 2000) — mPFC activity correlates on radial arm maze
- Poucet (1997); Gemmell et al. (2002) — prior failures to find spatial correlates in mPFC during foraging

**Named models or frameworks**:
- Place preference task (Rossier et al. 2000)
- Distributed spatial navigation network (Brown & Sharp 1995; Mizumori et al. 2000; Banquet et al. 2002)
- Gradient ascent path planning (proposed but not formalised)

**Brain regions**:
- Prelimbic cortex (PL)
- Infralimbic cortex (IL)
- Dorsal anterior cingulate area (CgAd)
- Medial prefrontal cortex (mPFC)
- Hippocampus
- Ventral striatum

**Keywords**:
- goal coding
- spatial navigation
- medial prefrontal cortex
- prelimbic cortex
- infralimbic cortex
- place cells
- motivational salience
- path planning
- hippocampus-prefrontal interaction
- unit recording
- place preference task
- goal-directed navigation
