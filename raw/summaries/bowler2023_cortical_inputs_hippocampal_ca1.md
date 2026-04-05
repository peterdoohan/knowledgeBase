---
source_file: bowler2023_cortical_inputs_hippocampal_ca1.md
title: "Direct cortical inputs to hippocampal area CA1 transmit complementary signals for goal-directed navigation"
authors: John C. Bowler, Attila Losonczy
year: 2023
journal: Neuron
paper_type: empirical
contribution_type: empirical
---

### One-line summary

In vivo two-photon axon imaging in mice shows that LEC and MEC direct inputs to CA1 carry distinct yet overlapping navigational signals: LEC representations are biased by navigational goals and remap with goal relocation, while MEC provides more stable, context- and location-specific codes.

---

### Background & motivation

The entorhinal cortex (EC) is the primary cortical input to the hippocampus, with medial EC (MEC) classically associated with global spatial mapping (including grid cells) and lateral EC (LEC) with non-spatial, sensory, and item-specific information. However, almost all prior characterisations examined general EC cell populations rather than the specific subset of EC neurons projecting directly to CA1, and the two subregions were rarely compared under identical conditions. It remained unknown how goal-related and contextual information are jointly routed through MEC and LEC to CA1, and what functional responsibilities each pathway holds for goal-directed navigation.

---

### Methods

- **Subjects**: Mice (n = 10 LEC, n = 6 MEC cohorts across tasks), expressing GCaMP6s in MEC or LEC via stereotaxic viral injection.
- **Imaging**: In vivo two-photon Ca2+ imaging of EC axons (putative boutons/axonal segments) within stratum lacunosum moleculare (SLM) of CA1; 41,617 LEC ROIs and 34,604 MEC ROIs recorded across all tasks.
- **Behaviour**: Mice ran on a virtual reality (VR) linear track (4 m) in head-fixed conditions with 2-s inter-trial intervals between laps. Tasks included:
  - Goal-directed navigation with VR-On (visual cues) vs. VR-Off (cue-less) conditions;
  - Reward zone (RZ) alternation task (RZ switching every 10 laps between two locations);
  - Probabilistic reward delivery (stochastic reward omission);
  - Context alternation (two distinct VR environments, fixed goal location, alternating every 10 laps);
  - Shuffled reward task (reward at a novel random location each lap).
- **Analysis**: Spatial tuning scores, population vector (PV) correlations, Bayesian position decoders, RZ-condition decoders, GLM-based feature modelling of Ca2+ transients.
- **Causal manipulation**: Retrograde-Cre + cre-dependent hM4D DREADD selectively expressed in LEC-CA1 or MEC-CA1 projecting neurons; deschloroclozapine (DCZ) applied to silence each pathway during novel reward location learning.

---

### Key findings

- **Spatial tuning in both pathways**: During VR-On, ~43–44% of both LEC and MEC ROIs were significantly spatially tuned; position could be decoded equally well from either projection when a reliable reward location was present.
- **Goal enrichment in LEC**: A significantly higher fraction of LEC (vs. MEC) axons had spatial fields in the 50 cm preceding the reward zone, across all tasks and conditions including VR-Off (cue-less) laps.
- **Goal-driven remapping of LEC**: When reward zone location changed, LEC tuning curves reorganised within one lap (11.7% of LEC ROIs tracked reward vs. 3.5% MEC; p = 0.039); cross-condition position decoding was significantly worse for LEC (p = 0.0047). MEC tuning remained spatially stable across reward conditions.
- **Reward omission**: Probabilistic reward omission disrupted LEC representations at and after the expected reward location but left MEC representations unchanged.
- **Context remapping in MEC**: Following a complete visual context change (fixed goal), MEC axons remapped strongly; LEC representations were more stable, especially near the reward zone. More MEC ROIs had context-specific tuning (p = 0.0003); more LEC ROIs had reward-distance tuning (p = 0.0003).
- **Goal-location information in ITI**: Both LEC and MEC axons could decode the previous reward condition during the inter-trial interval (LEC: 83.5%, MEC: 77.8%; both above chance).
- **Shuffled reward task**: LEC lost spatial specificity when goals changed every lap, while MEC maintained higher PV correlations, more tuned ROIs, and better position decoding.
- **Feature modelling**: Across tasks, a higher proportion of MEC models included position features; more LEC models relied on reward-distance (goal-vector) features.
- **Causal necessity of LEC**: Chemogenetic silencing of LEC-CA1 (but not MEC-CA1) projection significantly impaired learning of novel reward locations (p ≤ 0.001 for all DCZ days; effect not seen for MEC or tdTomato controls).

---

### Computational framework

The paper does not adopt a formal computational framework, but the results are interpreted in terms of reference frame coding and goal-vector representations. Specifically:

- **Allocentric vs. egocentric coding**: MEC is interpreted as providing allocentric (global spatial map) signals largely independent of current goal state; LEC is interpreted as providing more egocentric or goal-distance (reward-vector) coding, consistent with proposals that LEC encodes vectors anchored to behaviorally relevant targets.
- **Goal-distance/reward-vector model**: Feature modelling reveals LEC axons best described by distance-to-reward, analogous to egocentric bearing-cell coding proposed previously (Wang et al., 2018).
- **Attractor-like dynamics**: The persistence of reward-condition information during inter-trial intervals is discussed in terms of EC circuits following attractor dynamics, consistent with models of latent-state encoding.

The results primarily constrain models of how spatial and non-spatial information is routed from cortex to hippocampus, and are relevant to any mechanistic model of CA1 place field formation that incorporates direct EC inputs.

---

### Prevailing model of the system under study

The dominant view entering this study was a clean functional dissociation between MEC and LEC: MEC, rich in grid cells and spatially modulated neurons, provides the hippocampus with a global allocentric spatial map; LEC, with little spatial selectivity, provides item-specific, sensory, and non-spatial contextual information. Both pathways project directly to CA1 via layer III (the temporo-ammonic pathway), but this direct projection had rarely been characterised at the axonal level during navigation. Prior work on MEC axons in CA1 (Cholvin et al., 2021) established that MEC inputs are dynamic and that CA1 stabilises them into place fields, but comparable LEC axon data were sparse. Lesion and silencing studies showed only partial deficits in CA1 tuning after disrupting either pathway, leaving the relative functional contributions unresolved. The introduction signals that the field widely assumed LEC axons would convey little spatial information compared with MEC.

---

### What this paper contributes

The paper revises the classical MEC-spatial / LEC-non-spatial dichotomy in several ways:

1. **LEC axons carry substantial spatial information** during goal-directed navigation—comparable in quantity to MEC—contradicting the dogma that LEC does not provide spatially tuned input to CA1.
2. **Functional dissociation is task-state-dependent**: both pathways can support position decoding when goal locations are known and stable, but they diverge when goals change or are omitted. The dissociation is not spatial-vs.-non-spatial but rather goal-anchored-vs.-context-anchored.
3. **LEC is necessary for novel goal learning**: Chemogenetic dissection confirms that the LEC-CA1 projection is causally required for forming new location-reward associations, while MEC-CA1 silencing had no measurable deficit.
4. **MEC provides context- and location-specific codes** that remap with environmental changes but not with goal changes—consistent with an allocentric, context-indexed map.
5. These findings have practical implications for interpreting prior MEC manipulation studies: because LEC can partially substitute for MEC's spatial role, MEC-specific perturbations likely produced incomplete deficits because LEC was intact.

---

### Brain regions & systems

- **Medial entorhinal cortex (MEC)** — source of one of the two characterised direct inputs to CA1; provides allocentric, context-specific spatial codes; contains grid cells; axons remap with context change but not with goal translocation.
- **Lateral entorhinal cortex (LEC)** — source of the other characterised direct input to CA1; provides goal-anchored, reward-distance-modulated spatial codes; axons remap when goal location changes; causally required for novel location-reward learning.
- **Hippocampal CA1 (stratum lacunosum moleculare, SLM)** — site of imaging; receives direct EC inputs onto distal dendrites of pyramidal cells; proposed to integrate and stabilise complementary MEC and LEC signals into place fields.
- **Ventral tegmental area (VTA)** — mentioned as source of dopaminergic reward signals to LEC, relevant to cue-reward association encoding (cited background, not directly studied here).

---

### Mechanistic insight

This paper meets the bar for mechanistic insight.

**Phenomenon**: CA1 place fields are enriched near reward zones and remap when goals or contexts change. Which upstream inputs drive these properties, and through what computations?

**Computational level**: The brain must maintain a representation of current navigational goals (where is the reward?) alongside a stable spatial map of the environment, combining them to support flexible goal-directed navigation.

**Algorithmic level**: LEC-CA1 axons implement a goal-distance or reward-vector code — spatial fields anchored to reward proximity that update within a single lap when the goal relocates. MEC-CA1 axons implement a context-indexed allocentric code that remaps with environmental context change but is insensitive to goal position. Both streams can support location decoding, but through different representational strategies.

**Implementational level**: Two-photon imaging of identified EC axonal boutons in SLM of CA1 directly links these codes to activity in the specific projection neurons. Chemogenetic silencing (hM4D DREADD in retrograde-labelled CA1-projecting LEC neurons) demonstrates that the LEC-CA1 connection is specifically and causally required for novel reward-location learning. The paper does not resolve which specific cell types within MEC or LEC carry these signals, nor the synaptic mechanisms within CA1 by which these inputs drive plasticity, but the anatomical specificity (layer III EC → CA1 SLM) is explicit.

**Bonus**: The paper notes that LEC and MEC synapses are distributed along the transverse and radial axis of CA1 pyramidal cells in a gradient, raising the possibility that CA1 output neurons differentially weight the two inputs based on their dendritic location — an implementational detail that remains to be tested.

---

### Limitations & open questions

- Tasks are restricted to 1D linear virtual tracks; whether the goal-vector coding of LEC generalises to 2D open environments (where egocentric bearing vs. allocentric strategies are dissociable) is unclear.
- All reward locations tested were familiar ones learned over days; the dynamics of LEC representations during the initial acquisition of a completely novel goal location were not characterised.
- The study cannot resolve which specific cell types within LEC (e.g., fan cells, pyramidal cells of layer II/III) carry the goal-distance signal to CA1.
- No grid-like tuning was detected in MEC axons in these VR tasks, consistent with prior work but leaving uncertain how grid cell activity relates to the allocentric spatial code observed here.
- Velocity decoding from MEC axons was poor, suggesting speed cells do not prominently project to CA1, but this leaves open what MEC cell types form the allocentric code in CA1.
- The mechanism by which LEC maintains reward-condition information across inter-trial intervals (attractor dynamics, persistent firing, synaptic traces?) is not determined.
- Causal role of MEC-CA1 in tasks where MEC showed differential remapping (e.g., context alternation) was not tested with DREADD.

---

### Connections & keywords

**Key citations**:
- Cholvin, Hainmueller & Bartos (2021) — MEC axon imaging in CA1 during VR
- Grienberger & Magee (2022) — EC inputs drive learning-related CA1 changes
- Hargreaves et al. (2005) — MEC/LEC spatial selectivity dissociation
- Wang et al. (2018) — egocentric bearing coding in LEC
- Boccara et al. (2019) and Butler et al. (2019) — MEC grid cell remapping toward goals
- Dupret et al. (2010) — place field reorganisation around reward
- Gauthier & Tank (2018) — dedicated reward-coding population in CA1
- Priestley et al. (2022) — rapid plasticity signatures in CA1 during novelty

**Named models or frameworks**:
- Temporo-ammonic (EC layer III → CA1) pathway
- Behavioural time scale synaptic plasticity (BTSP; background)
- Goal-distance / reward-vector coding
- Allocentric vs. egocentric spatial reference frames
- Attractor network dynamics (for latent state encoding)

**Brain regions**:
- Medial entorhinal cortex (MEC)
- Lateral entorhinal cortex (LEC)
- Hippocampal CA1 (stratum lacunosum moleculare)

**Keywords**:
- entorhinal cortex axon imaging
- CA1 direct cortical input
- goal-directed navigation
- reward-vector coding
- place cell remapping
- context-specific spatial map
- two-photon calcium imaging
- virtual reality navigation
- DREADD chemogenetics
- population vector correlation
- goal-anticipatory tuning
- MEC-LEC functional dissociation
