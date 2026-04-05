---
source_file: brunec2022_predictive_representations_hierarchies.md
title: Predictive Representations in Hippocampal and Prefrontal Hierarchies
authors: Iva K. Brunec, Ida Momennejad
year: 2022
journal: The Journal of Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

During naturalistic virtual navigation of a real city, fMRI representational similarity analyses reveal that anterior PFC encodes the longest predictive horizons (up to ~875 m) while posterior hippocampus encodes the shortest, demonstrating a multiscale successor-representation hierarchy across hippocampal and prefrontal gradients.

---

### Background & motivation

How the brain guides goal-directed behaviour across realistically long distances is poorly understood. Most studies of relational knowledge and planning use small, highly controlled environments, leaving unclear how predictive cognitive maps scale to naturalistic navigation. Computational models based on the successor representation (SR) predict that the brain should maintain multiscale predictive representations simultaneously, and that these scales should be organised along posterior-anterior axes of both the hippocampus and PFC. This paper is the first to test these predictions using fMRI during naturalistic, city-scale virtual navigation of a personally familiar environment.

---

### Methods

- **Participants**: 19 healthy right-handed adults (9 male; mean age 22.6 years) who had lived in Toronto for at least 2 years.
- **Task**: Reanalysis of an existing fMRI dataset (Brunec et al., 2018). Participants navigated a virtual version of Toronto using 360° panoramic Google Street View imagery. Two conditions: (1) goal-directed navigation to personally familiar destinations (~3.5 km average routes); (2) GPS/arrow-following navigation along unfamiliar routes (~2.5 km average routes).
- **fMRI acquisition**: 3T Siemens scanner; TR = 2000 ms; EPI 30 axial slices; no spatial smoothing; standard preprocessing plus motion scrubbing.
- **Representational similarity analyses (RSA)**:
  - *Unweighted analysis*: correlation between each TR's voxelwise pattern and the mean of future 1–10 TRs within a priori ROIs (anterior/posterior hippocampus split into 6 segments; antPFC; mPFC).
  - *Discount-weighted SR analysis*: correlation between each TR and the gamma (γ)-weighted sum of future TR patterns, for γ = 0.1, 0.6, 0.8, 0.9; γ values correspond to predictive horizons of approximately 25 m, 175 m, 375 m, and 800 m respectively.
  - *PFC searchlight*: spherical 6 mm searchlights across a PFC mask to map predictive horizons spatially.
- **Path distance analysis**: Mixed-effects models including navigated path distance as a predictor, controlling for number of TRs; Euclidean distance used as a comparison control.
- Statistical approach: linear mixed-effects models in R (lme4/lmerTest); Bonferroni correction for ROI comparisons.

---

### Key findings

- **Posterior-to-anterior hippocampal gradient**: Anterior hippocampus (aHPC) maintained significant above-zero predictive similarity for longer horizons than posterior hippocampus (pHPC); pHPC showed significant negative similarity at γ = 0.8, possibly reflecting pattern differentiation across fine-grained spatial units.
- **Prefrontal hierarchy**: antPFC showed the longest predictive horizons of all regions — significantly above zero for all horizons tested (including 10 TRs ahead, ~250 m) in the goal-directed condition; mPFC, OFC (BA 11), ACC (BA 32/25) showed intermediate horizons. Posterior PFC showed negligible predictive similarity.
- **Goal-directed > GPS effects**: All ROIs showed higher predictive similarity in the goal-directed condition than GPS condition; the condition difference was particularly pronounced in aHPC and antPFC for longer horizons (γ × condition interaction, F(2,1448) = 7.49, p < 0.001).
- **Main ROI effect**: Overall, antPFC > mPFC > aHPC > pHPC in magnitude of predictive similarity (F(3,1448) = 547.38, p < 0.001, η²p = 0.53); overall model R²M = 0.57.
- **Path distance interactions**: In antPFC, longer routes were associated with greater representational similarity (F(1,149) = 91.51, p < 0.001, η²p = 0.38); hippocampal regions showed the opposite trend — shorter routes were associated with higher representational similarity, suggesting the hippocampus is more tightly coupled to local navigational context.
- **Euclidean vs. path distance**: The ROI × path distance interaction was specific to navigated (path) distance, not Euclidean distance, confirming that predictive representations track the actual trajectory structure.
- **PFC searchlight**: Anterior/polar PFC (BA 10) showed the largest coverage of significantly predictive voxels across γ values; OFC (BA 11) and ACC (BA 25/32) followed; dorsolateral PFC (BA 9, 46) showed modest overlap; IFG (BA 45) showed none.
- **Matched-distance control**: After equating route distances between conditions, goal-directed routes still showed greater predictive similarity in several PFC clusters, with dorsal and rostral PFC clusters differentiating the conditions at larger γ values.

---

### Computational framework

**Successor Representation (SR) / Reinforcement Learning**

The SR (Dayan, 1993) is the core computational framework. In a Markov Decision Process, the SR M(s, s') encodes the expected discounted future occupancy of state s' when starting from state s:

M = (I − γT)⁻¹

where T is the one-step transition matrix and γ is a discount factor (0 < γ < 1). The discount parameter controls the predictive horizon: low γ gives a myopic representation (only near-future states), high γ gives a far-sighted one.

The paper operationalises this by predicting that neural activity at time t (current state) should be similar to the γ-weighted sum of neural activity at future TRs (successor states). Different brain regions are hypothesised to instantiate different γ values — i.e., different timescales or radii of predictive integration — forming a representational hierarchy.

A key assumption is that the transition probabilities along a goal-directed route are approximately deterministic (T(s_i, s_{i+1}) ≈ 1), so the SR reduces to the discounted sum of future states along the navigated path. The analysis does not require a fully learned SR matrix; it tests for the pattern similarity signature that the SR predicts at each point along a trajectory.

---

### Prevailing model of the system under study

The introduction signals two pre-existing bodies of theory that this paper builds on:

1. **Hippocampal long-axis gradient**: Prior rodent electrophysiology established that dorsal (posterior in humans) hippocampus contains small, precise place fields while ventral (anterior) hippocampus contains large, overlapping place fields. Human fMRI had extended this to a posterior-anterior representational scale gradient. Stachenfeld et al. (2017) formalised the hippocampus as encoding a predictive map (SR) with scale varying along the dorsoventral axis.

2. **Prefrontal rostrocaudal hierarchy**: A separate line of work (Koechlin, Badre, Christoff) proposed that PFC is organised rostrocaudally, with more anterior regions supporting higher levels of abstraction, longer temporal integration, and relational reasoning. This had been supported by working memory, prospective memory, and relational reasoning studies, but not by model-based RSA during continuous navigation.

The paper's contribution is to unite these two hierarchies under a single SR framework and to test both simultaneously in naturalistic navigation at ecologically realistic spatial scales — something previous controlled lab paradigms could not do.

---

### What this paper contributes

1. **Direct neural evidence for multiscale SR in naturalistic navigation**: This is the first study to show that fMRI similarity patterns during city-scale navigation conform to SR predictions at multiple γ values (25–875 m horizons), not just near-future states.

2. **Quantitative mapping of predictive horizons across the hippocampal-PFC hierarchy**: The paper establishes a continuous gradient — posterior HPC (~25 m) → anterior HPC (~175 m) → OFC/mPFC (~375 m) → anterior PFC (~800+ m) — grounding the abstract computational hierarchy in specific anatomical regions.

3. **Goal-directedness modulates predictive horizons**: The goal-directed condition consistently showed longer and stronger predictive representations than GPS-guided navigation (which shares motor and visual demands), implying that top-down goal representations actively shape the spatial scale of hippocampal-prefrontal predictive coding rather than this being a purely bottom-up sensory signal.

4. **Path distance as a modulator**: The opposing effects of path distance in antPFC (longer route → stronger predictive signal) versus hippocampus (longer route → weaker predictive signal) suggests that as navigation scale increases, the PFC increasingly carries the global planning representation while hippocampal representations remain locally scoped.

---

### Brain regions & systems

- **Posterior hippocampus (pHPC)** — smallest predictive horizons (~25 m, γ = 0.1); may support fine-grained spatial pattern separation and local route coding; showed negative similarity at γ = 0.8, suggesting active differentiation of nearby states.
- **Anterior hippocampus (aHPC)** — intermediate predictive horizons (~175 m); integrates spatial context at broader scales; shows goal-directedness sensitivity; bridging role between pHPC and PFC in the hierarchy.
- **Orbitofrontal cortex / OFC (BA 11)** — intermediate-to-long predictive horizons; proposed to maintain state-state relational maps supporting model-based RL and value computation; representationally most similar to aHPC.
- **Medial PFC / mPFC (BA 25, 32, ACC-adjacent)** — intermediate predictive horizons; overlap with subgenual and anterior cingulate areas; involved in goal and task-set representations.
- **Anterior/polar PFC (BA 10)** — longest predictive horizons (~800+ m); largest cytoarchitectonic region of human PFC; proposed locus of highest-level spatial abstraction, global route structure, and hierarchical planning.
- **Dorsolateral PFC (BA 9, 46)** — weaker overlap with predictive voxels; present but not the primary gradient driver.

---

### Mechanistic insight

The paper meets the threshold for this section in part but not fully.

**Criterion 1 (algorithm)**: Yes — the SR provides an explicit algorithm. Neural activity at state s should equal the γ-weighted sum of neural activity at successor states, where γ parameterises the predictive horizon.

**Criterion 2 (neural data supporting this algorithm over alternatives)**: Partially. The study provides fMRI RSA data that is consistent with SR predictions and shows a graded γ-dependent hierarchy across regions. However, the analysis cannot fully disambiguate SR-based predictive similarity from alternative accounts (activation spread, recent memory reinstatement, hippocampal replay), as acknowledged in the Discussion. Electrophysiology or MEG would be needed for that dissociation.

At Marr's levels:

- **Computational**: The brain solves the problem of planning across multiple spatial scales simultaneously — representing both immediate surroundings and distant goals — enabling flexible, hierarchical goal-directed navigation.
- **Algorithmic**: The SR instantiated at different γ values organises representations along the hippocampal and prefrontal posterior-anterior axes. Each region's γ determines the radius of predictive integration: posterior HPC ≈ myopic SR (γ ~ 0.1), anterior PFC ≈ far-sighted SR (γ ~ 0.9). Goal-directedness amplifies the predictive signal by biasing the effective transition structure toward goal-relevant paths.
- **Implementational**: Not directly addressed. The paper suggests BA 10's dense recurrent connectivity and long temporal decay constants as a plausible substrate for high-γ integration, but no cellular or circuit-level data are provided.

---

### Limitations & open questions

- **Route asymmetry**: Goal-directed routes were significantly longer than GPS routes, creating potential confounds. Distance-matched control analyses were conducted with n = 16 and showed consistent results, but the mismatch limits direct between-condition inference.
- **No pretraining representations**: The analysis cannot estimate the baseline (pre-associative) neural similarity between locations, so the RSA operationalises SR as a relative measure rather than an absolute one.
- **Single path per state**: Routes did not include multiple trajectories through each state or to each goal, limiting the ability to test the full graph structure of the SR and dissociate path-specific from goal-specific encoding.
- **Alternative interpretations**: Predictive similarity could reflect spreading activation in memory networks, replay of prior routes, or temporal proximity effects rather than genuine SR encoding. Distinguishing these requires higher spatiotemporal resolution data.
- **Small sample**: N = 19 (down to 16 in the matched-distance analysis); no a priori power analysis.
- **Open questions**: How are compressed representations (eigenvectors, Laplace-domain SR) implemented in PFC? Do subgoal states (e.g., turns, intersections) show enhanced predictive representations? How do these hierarchies update dynamically during novel environment learning?

---

### Connections & keywords

**Key citations**:
- Stachenfeld, Botvinick & Gershman (2017) — hippocampus as predictive map
- Momennejad & Howard (2018) — multiscale SR theory
- Momennejad et al. (2017) — SR in human reinforcement learning behaviour
- Brunec et al. (2018) — source fMRI dataset; hippocampal scale gradient
- Dayan (1993) — original SR formulation
- Behrens et al. (2018) — cognitive maps and flexible behaviour
- Badre & D'Esposito (2007) — prefrontal hierarchical organisation
- Koechlin & Hyafil (2007) — anterior PFC limits of decision-making
- Poppenk et al. (2013) — human hippocampal long-axis specialisation
- Schuck et al. (2016) — OFC as cognitive map of state space

**Named models or frameworks**:
- Successor Representation (SR)
- Model-based reinforcement learning
- Representational Similarity Analysis (RSA)

**Brain regions**:
- Posterior hippocampus
- Anterior hippocampus
- Orbitofrontal cortex (OFC, BA 11)
- Medial PFC / mPFC (BA 25, 32)
- Anterior/polar PFC (BA 10)
- Dorsolateral PFC (BA 9, 46)

**Keywords**:
- successor representation
- predictive representations
- hippocampal long axis
- prefrontal hierarchy
- cognitive maps
- naturalistic navigation
- representational similarity analysis
- discount factor / predictive horizon
- model-based fMRI
- goal-directed navigation
- spatial scale gradient
- hierarchical planning
