---
source_file: muhlekarbe2023_goal_seeking_spatial_compression.md
paper_id: muhlekarbe2023_goal_seeking_spatial_compression
title: "Goal-seeking compresses neural codes for space in the human hippocampus and orbitofrontal cortex"
authors:
  - "Paul S. Muhle-Karbe"
  - "Hannah Sheahan"
  - "Giovanni Pezzulo"
  - "Hugo J. Spiers"
  - "Samson Chien"
  - "Nicolas W. Schuck"
  - "Christopher Summerfield"
year: 2023
journal: Neuron
paper_type: empirical
contribution_type: empirical
species:
  - human
methods:
  - fmri
  - representational_similarity_analysis
  - computational_modeling
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - orbitofrontal_cortex
  - visual_cortex
frameworks:
  - neural_manifold
keywords:
  - cognitive_map
  - goal_directed_navigation
  - spatial_compression
  - representational_geometry
  - hippocampus
  - orbitofrontal_cortex
  - place_cells
  - fmri
  - neural_state_space
  - prospective_coding
  - context_dependent_remapping
  - sequential_decision_making
  - goal
  - seeking
  - compresses
  - neural
  - codes
  - space
  - human
  - orbitofrontal
key_citations:
  - basu2021_ofc_navigation_goals
  - nyberg2022_spatial_goal_coding
  - brown2016_prospective_goals_hippocampus
  - schuck2016_orbitofrontal_cortex_state
wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
---

### One-line summary

During goal-directed navigation in a grid-world fMRI task, spatial maps in the human hippocampus and orbitofrontal cortex are "compressed" so that locations sharing prospective goals are coded as more similar in neural state space, an effect that predicts navigation performance and is captured by a place-cell model that jointly encodes current and goal locations.

---

### Background & motivation

The hippocampus encodes allocentric space via place cells, but spatial goals and context also modulate this code — through remapping, rate changes, or over-representation of reward locations. It remains unclear how context-dependent goals distort the large-scale geometry of spatial representations in the human brain, especially during tasks that require sequential multi-step navigation. Prior human fMRI work has decoded spatial location and goal proximity, but the representational geometry across contexts had not been formally characterised. This paper asks how goals warp the neural manifold for space and whether that warping is functionally relevant.

---

### Methods

- **Participants**: n = 27 human participants scanned with fMRI.
- **Task**: Context-dependent spatial navigation in a partially observable four-room grid world. On each trial, a contextual cue (food image) indicated whether rewards were in vertically or horizontally adjacent rooms; participants navigated an avatar to find two successive rewarded boulders. Three cue sets were used across scanner runs to test generalisation.
- **Design**: Day 1 training; Day 2 scanning (96 trials, 6 runs). A "robot control" phase on each trial moved the avatar to off-path locations to balance room occupancy and measure BOLD signals across all rooms/contexts.
- **fMRI analysis**: Multivariate BOLD signals modelled with a design matrix of room × context (8 conditions). Representational dissimilarity matrices (RDMs) computed for each ROI (visual cortex, PPC, PFC, hippocampus, OFC); model RDMs regressed competitively against data RDMs; model-free score analyses; whole-brain searchlight.
- **Computational model**: Simulated Gaussian place fields tiling the four-room environment, with three free parameters: (1) remapping fraction β (orthogonalisation), (2) context-coding gain g (separation), and (3) current-vs-goal mixture weight u (compression/anti-compression). Human behavioural trajectories used as model inputs to generate predicted RDMs.
- **Geometry visualisation**: Multidimensional scaling (MDS) of group-average RDMs.
- **Behaviour–brain correlations**: Compression scores correlated with transition bias and first-choice accuracy across participants.

---

### Key findings

- **Goal-based spatial compression in HC and OFC**: During the pre-goal room period, rooms sharing a common goal axis (north–south in vertical context; east–west in horizontal context) were represented with more similar neural codes in hippocampus (t = 2.92, p < 0.01) and OFC (t = 5.70, p < 0.001). OFC compression was also significant during the goal-room period (t = 2.66, p < 0.01).
- **No orthogonalisation**: Neither HC nor OFC showed the random remapping (orthogonalisation) predicted by rodent remapping models; neural manifolds were largely aligned across contexts in all regions.
- **Spatial layout encoded in PPC and PFC**: Room-level and map-level codes were most reliable in PPC and PFC; HC and OFC did not reliably encode veridical spatial layout.
- **Compression tracks performance**: In HC, compression scores predicted both transition bias (r = 0.45, p = 0.019) and first-choice accuracy (r = 0.43, p = 0.025). In OFC, goal-room compression predicted first-choice accuracy (r = 0.41, p < 0.032).
- **Inverted geometry across periods**: Neural geometry in HC and OFC was "flipped" between the approach phase (pre-goal room) and the in-goal-room phase, confirmed by cosine angle analyses showing inversion of common spatial directions across periods (significant region × pair-type interaction: F = 20.8, p < 0.001).
- **Hierarchical goal representation in PPC/PFC**: A map of current goal location was nested within a map of current room location in PPC and PFC; this hierarchical structure was not recovered in HC or OFC (context averaging removed the relevant subspace).
- **Model**: Compression was best captured by u > 0 (joint encoding of current and prospective locations), not by orthogonalisation or separation variants.
- **Whole-brain searchlight**: Compression and map effects survived FWE correction at the whole-brain level, with significant clusters in HC, OFC, PPC, and PFC.

---

### Computational framework

**Representational geometry / cognitive map framework**, combined with a **place-cell population model**.

The paper models spatial coding via simulated Gaussian place fields tiling a four-room environment. The key variable is the mixture weight u controlling the relative contribution of current vs. prospective (goal) location to each place cell's population vector. When u > 0, the population jointly encodes where the agent is and where it is going, which geometrically compresses the representations of rooms that share a goal axis. The framework assumes that the macroscopic BOLD signal reflects the aggregate activity of such a place-code population, and that representational geometry (distances in neural state space, captured by RDMs) is the appropriate level of analysis. The model is compared against three alternative hypotheses formalised as distinct geometric signatures: orthogonalisation (random remapping), planar separation (factorised spatial/contextual coding), and compression/anti-compression (joint current-goal encoding).

---

### Prevailing model of the system under study

The paper's introduction frames the baseline understanding as follows: the rodent hippocampus encodes allocentric space through place cells forming a cognitive map, and changes in context cause place cells to remap — either globally (random reassignment of firing fields) or partially. Remapping is the dominant account of how the hippocampus handles distinct contexts or goals. Related work suggests context can also be represented as an orthogonal, factorised dimension in neural state space. In humans, fMRI studies have shown that spatial location and goal proximity can be decoded from hippocampal BOLD signals, and both hippocampus and OFC have been implicated in goal coding. However, the geometric relationship between current location and goal in the human neural manifold had not been characterised; the default expectation from the rodent literature would be either veridical spatial mapping or remapping, not systematic compression.

---

### What this paper contributes

The paper shows that the dominant effect of goals in human hippocampus and OFC is not remapping but goal-based compression: rooms sharing a prospective goal axis are pulled together in the neural state space. This is a new, specific geometric signature that could not previously be attributed to place codes alone. The compression effect is functionally meaningful (it correlates with navigation performance), generalises across three different cue sets, and is well-explained by the simple principle that current and goal locations are jointly encoded in the population vector. The paper also documents an inversion of the spatial geometry between approach and arrival phases, and a hierarchical nesting of goal maps within location maps in PPC/PFC, neither of which had been reported in human fMRI. Collectively, the findings shift the picture of hippocampal and OFC spatial coding from a passive map to one actively warped by prospective planning demands.

---

### Brain regions & systems

- **Hippocampus (HC)** — primary locus of goal-based spatial compression during navigation (pre-goal room period); compression predicts performance; no reliable encoding of veridical spatial layout; shows geometry inversion between approach and arrival phases.
- **Orbitofrontal cortex (OFC)** — second primary locus of goal-based compression (both pre-goal and goal-room periods); strongest overall compression effect; associated with coding task/reward state space; shows geometry inversion.
- **Posterior parietal cortex (PPC)** — encodes veridical spatial layout reliably (room and map codes); shows hierarchical nesting of goal map within location map; does not show strong compression.
- **Prefrontal cortex (PFC)** — encodes spatial layout and shows some map coding; hierarchical goal representation; weaker compression than HC/OFC.
- **Visual cortex** — encodes individual room identity but with a high-dimensional, unstructured geometry; no reliable map or compression effects.

---

### Mechanistic insight

The paper meets one of the two required criteria: it proposes a clear algorithm (joint encoding of current and prospective locations in a place-code population, producing goal-based compression), and it provides human fMRI data. However, the fMRI data cannot resolve the specific cellular or circuit mechanism implementing joint encoding. The paper explicitly acknowledges this limitation, noting that prospective locations could arise through dedicated "goal cell" populations, forward/backward replay, or other mechanisms that cannot be distinguished at the BOLD level. Therefore, the mechanistic insight bar is not fully met.

The paper proposes an algorithmic-level account (joint encoding of current and goal locations in a population code explains the compression geometry), and it shows that the BOLD signal in HC and OFC is consistent with this algorithm. But it does not provide direct evidence linking the model's specific variable (the mixture weight u, or the prospective-location component of the code) to measured neural activity at the single-neuron or circuit level, and it does not address the implementational level (cell types, connectivity, neuromodulation). The fMRI signal is too coarse to distinguish between the candidate mechanisms that could realise joint encoding.

---

### Limitations & open questions

- fMRI spatial and temporal resolution precludes distinguishing between candidate mechanisms for joint encoding (dedicated goal cells, replay, attractor dynamics).
- The place cell model is a phenomenological proxy; it is not established that macroscopic BOLD compression directly reflects the same process as single-unit place field distortions in rodents.
- Compression emerged under conditions where goals were cued and flexibly changed trial-to-trial; it is unknown whether compression would appear during routine navigation with fixed goals.
- The inverted geometry between pre-goal and goal-room periods is unexplained — the authors suggest a possible link to retrieval-based repulsion but do not test this.
- The study used a grid-world with discrete rooms; generalisability to continuous environments is unestablished.
- Goal-based compression was not observed in HC or OFC when collapsing over contexts, suggesting the effect is subspace-specific and may be missed by analyses that do not respect context structure.
- The relationship between hippocampal compression and OFC compression (whether they reflect a common or distinct source) is not resolved.

---

### Connections & keywords

**Key citations**:
- O'Keefe & Dostrovsky (1971) — place cells in the hippocampus
- Gauthier & Tank (2018) — dedicated reward-coding population in CA1
- Basu et al. (2021) — OFC maps future navigational goals (rodents)
- Nieh et al. (2021) — geometry of abstract learned knowledge in the hippocampus
- Nyberg et al. (2022) — spatial goal coding in the hippocampal formation (review)
- Brown et al. (2016) — prospective representation of navigational goals in human hippocampus (Science)
- Schuck et al. (2016) — human OFC represents a cognitive map of state space
- Flesch et al. (2022) — orthogonal representations for robust context-dependent task performance
- Chanales et al. (2017) — hippocampal representational repulsion for overlapping spatial memories
- Pfeiffer & Foster (2013) — hippocampal place-cell sequences depict future paths (replay)

**Named models or frameworks**:
- Place-cell population model with mixture weight for current/goal locations
- Representational dissimilarity matrix (RDM) / representational similarity analysis (RSA)
- Multidimensional scaling (MDS) for neural geometry visualisation
- Goal-based spatial compression (authors' term)
- Neural structure alignment

**Brain regions**:
- Hippocampus (HC)
- Orbitofrontal cortex (OFC)
- Posterior parietal cortex (PPC)
- Prefrontal cortex (PFC)
- Visual cortex

**Keywords**:
- cognitive map, goal-directed navigation, spatial compression, representational geometry, hippocampus, orbitofrontal cortex, place cells, fMRI, neural state space, prospective coding, context-dependent remapping, sequential decision-making

### Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]
