---
source_file: "brown2016_prospective_goals_hippocampus.md"
paper_id: "brown2016_prospective_goals_hippocampus"
title: "Prospective representation of navigational goals in the human hippocampus"
authors: "Thackery I. Brown, Valerie A. Carr, Karen F. LaRocque, Serra E. Favila, Alan M. Gordon, Ben Bowles, Jeremy N. Bailenson, Anthony D. Wagner"
year: 2016
journal: "Science"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["virtual_navigation"]
methods: ["fmri"]
brain_regions: ["hippocampus", "prefrontal_cortex", "orbitofrontal_cortex", "striatum", "ventral_striatum", "retrosplenial_cortex", "medial_temporal_lobe"]
frameworks: ["successor_representation"]
keywords: ["prospective", "representation", "navigational", "goals", "human", "hippocampus"]
key_citations: ["johnson2007_hippocampus_decision", "spiers2015_detour_problem_navigation"]
---

### One-line summary

Using high-resolution fMRI and multi-voxel pattern classification, this study demonstrates that distributed hippocampal activity patterns prospectively represent future navigational goal states — and intervening sub-goal locations along the planned route — during a pre-navigation planning period, with hippocampal goal coding coupled to activity in a prefrontal-MTL-retrosplenial network.

---

### Background & motivation

Prospective thought — the ability to mentally simulate future experiences — is theorised to rely on hippocampal episodic memory mechanisms. Rodent studies show hippocampal place cells exhibit prospective sequential firing during planning that reflects upcoming goals, but direct non-invasive evidence that the human hippocampus supports analogous prospective goal coding during route planning was lacking. Multi-voxel fMRI approaches can potentially detect the distributed multifeatural engrams that encode spatial contexts, and this paper exploits that capability to test whether a hippocampal-cortical network mediates goal-state simulation in humans.

---

### Methods

- **Subjects**: 17 participants scanned with whole-brain high-resolution fMRI (1.6 mm isotropic voxels) at Stanford.
- **Task**: Two-session virtual navigation paradigm. Day 1 (outside scanner): participants learned to navigate to five goal locations in a circular virtual environment, each marked by a distinct fractal pair. Day 2 (during fMRI): fractals were absent; on each trial participants began at a known location, were cued with a goal fractal, planned their route (cue + fixation period), then actively navigated.
- **Design**: 160 trials (32 per goal location, visiting every location from every other location equally), enabling analysis of planning-period neural patterns that generalise across cues, start positions, and routes.
- **Analyses**:
  - Multi-voxel pattern classification (MVPA) of the planning period: "current" classifier (current location) and "future" classifier (upcoming goal location), tested against empirically validated chance.
  - Probabilistic evidence scores used for trial-by-trial analyses.
  - A priori anatomical ROIs: hippocampus and subfields (subiculum), perirhinal cortex (PRC), parahippocampal cortex (PHC), retrosplenial complex (RSC), ventral striatum (VS), frontopolar cortex (FPC).
  - Whole-brain searchlight analysis for goal decoding and for regions correlating with hippocampal goal evidence.
  - Correlation of trial-by-trial hippocampal "future" classifier evidence with univariate PFC activity.

---

### Key findings

- Hippocampal activity patterns during the planning period significantly decoded the future goal location (classifier accuracy 29.4%; t16 = 7.54, P = 1.19 × 10^-6).
- Hippocampal patterns also coded the current location (29.9%; t16 = 5.55, P = 4.40 × 10^-5), confirming both current-state and prospective-state representations.
- During planning, the location most confusable with the true goal was the intervening sub-goal along the optimal route — consistent with sequential trajectory simulation (replay-like coding of route waypoints).
- Future goal coding was also significantly above chance in PRC, PHC, and RSC; ventral striatum showed only marginal goal coding.
- Trial-by-trial "future" classifier evidence in PHC, PRC, and RSC positively correlated with hippocampal goal evidence, supporting a coupled multifeatural network.
- Planning-period univariate activity in lateral and medial FPC positively correlated with trial-by-trial hippocampal (and subiculum) goal classifier evidence.
- Whole-brain searchlight identified significant future goal decoding in the OFC, a region with direct anatomical connections to the hippocampus; OFC evidence also correlated with hippocampal goal evidence.
- A follow-up analysis indicated that reinstatement of goal-arrival neural patterns contributes to prospective goal coding during planning.

---

### Computational framework

Not applicable in the sense that no formal computational model is specified or fitted. However, the paper is implicitly organised around a **pattern reinstatement / episodic simulation** framework: the central idea is that planning recruits the same distributed multifeatural neural patterns active at the goal location during prior experience (episodic engram reinstatement). This is operationalised via linear MVPA classifiers trained on navigation-period data and applied to planning-period data.

The conceptual framework also draws on **predictive / prospective coding** ideas from rodent place-cell literature: during planning, hippocampal activity sequences "look ahead" along the intended route, reinstating representations of future locations in temporal order. These results could be formalised within a **successor representation** or **cognitive map** framework (not explicitly stated by the authors), where the hippocampus encodes future-state value or expected future occupancy during deliberation.

---

### Prevailing model of the system under study

The dominant model entering this paper posits that the hippocampus is a core substrate for episodic memory and, by extension, for mental simulation of future events ("mental time travel"). In rodents, hippocampal place cells are known to fire prospectively during navigational decision-making — at choice points, the cell assembly transiently represents upcoming locations along candidate routes (vicarious trial and error / forward sweeps). A broader hippocampal-cortical network — involving MTL cortex for contextual/item content, RSC for location coding, and VS for motivational signals — is hypothesised to support prospective simulation. Hippocampal interactions with PFC are further proposed to provide top-down control for flexibly accessing episode-specific mnemonic details and integrating them into goal plans. However, prior to this paper, direct non-invasive evidence in humans that hippocampal distributed patterns specifically encode future goal states (rather than just distance-to-goal or grid-cell-like responses) during an explicit planning phase was absent.

---

### What this paper contributes

The paper provides the first human fMRI evidence that the hippocampus encodes the actual goal destination as a multifeatural pattern during a pre-navigation planning period — not merely a scalar distance signal. It additionally shows that sub-goal (waypoint) locations along the planned route are preferentially represented, extending the rodent forward-sweep concept to humans. The coupling of hippocampal goal codes to PRC, PHC, RSC, and OFC on a trial-by-trial basis establishes that prospective simulation is a network-level phenomenon. The correlation between FPC activity and hippocampal goal evidence provides human evidence for the hypothesised PFC-hippocampal top-down control mechanism during prospective planning. Collectively, the work bridges rodent prospective coding literature with human cognitive neuroscience of future thinking.

---

### Brain regions & systems

- **Hippocampus (and subiculum)** — primary locus of prospective goal-state coding; subiculum specifically showed goal evidence correlated with FPC activity.
- **Perirhinal cortex (PRC)** — item/content coding of goal locations; goal decoding above chance and correlated with hippocampal evidence.
- **Parahippocampal cortex (PHC)** — contextual reinstatement and location coding; goal decoding above chance and correlated with hippocampal evidence; searchlight identified local patches.
- **Retrosplenial complex (RSC)** — planning and future-event simulation via location coding; goal decoding above chance and correlated with hippocampal evidence.
- **Ventral striatum (VS)** — motivational/reward signals in space; only marginally significant goal coding.
- **Frontopolar cortex (FPC, lateral and medial)** — planning-period univariate activity correlated with hippocampal goal evidence; interpreted as providing cognitive control for accessing mnemonic details and forming route plans.
- **Orbitofrontal cortex (OFC)** — identified by whole-brain searchlight as encoding future goal states; anatomically connected to hippocampus; goal evidence correlated with hippocampal evidence.

---

### Mechanistic insight

The paper partially meets the bar. It identifies a specific algorithm (prospective reinstatement of multifeatural goal-location engrams, including sequential sub-goal coding consistent with trajectory simulation) and provides fMRI pattern-classification data that specifically support this algorithm. The coupling of hippocampal prospective codes with PFC activity provides neural data bearing on the hypothesised top-down control mechanism. However, because the neural data are fMRI BOLD (not single-unit recordings), the paper cannot resolve the implementational level in detail (e.g., specific cell types such as place cells, time cells, or grid cells; precise connectivity; neuromodulatory mechanisms).

- **Computational**: The brain solves the problem of representing where one intends to go before navigating there, enabling flexible goal-directed planning.
- **Algorithmic**: During planning, the hippocampus reinstates the distributed multifeatural representation (engram) associated with the goal location and, sequentially, with intermediate sub-goal locations along the intended route — a look-ahead simulation. PFC (FPC) modulates the strength of this prospective reinstatement, providing control over which goal-relevant memories are accessed.
- **Implementational**: Not resolved at single-neuron level; the data are consistent with rodent place-cell forward sweeps but cannot confirm the specific cell-type or connectivity implementation in humans.

---

### Limitations & open questions

- The virtual environment is small (five locations in a circular arena), making it uncertain whether similar prospective coding occurs in large-scale real-world navigation.
- fMRI spatial resolution, while high (1.6 mm isotropic), does not allow disambiguation of hippocampal subfield contributions beyond a coarse subiculum analysis; individual place-cell dynamics cannot be observed.
- The design controls well for perceptual confounds during planning, but the precise timing and mechanism of reinstatement (e.g., whether it is sequential or simultaneous) cannot be determined from univariate or even MVPA fMRI.
- VS goal coding was only marginally significant, leaving the role of motivational signals in prospective planning underspecified.
- The correlation between FPC activity and hippocampal goal codes is associative; causal directionality (PFC → hippocampus vs. hippocampus → PFC) is not established.
- It remains open whether this hippocampal prospective code reflects spatial goals specifically or generalises to non-spatial episodic future events.

---

### Connections & keywords

**Key citations**:
- Schacter & Addis (2009) — episodic future thinking framework
- Buckner & Carroll (2007) — self-projection and the default network
- Wikenheiser & Redish (2015, Nat Neurosci) — rodent prospective hippocampal coding during planning
- Johnson & Redish (2007) — vicarious trial and error in rodents
- Ito et al. (2015, Nature) — hippocampal-PFC circuit for goal-directed navigation
- Hassabis et al. (2009, Curr Biol) — hippocampal pattern similarity for spatial contexts
- Spiers & Gilbert (2015) — FPC and route planning
- Doeller, Barry & Burgess (2010) — grid-cell-like coding in humans

**Named models or frameworks**:
- Episodic simulation / mental time travel (Schacter & Addis)
- Prospective/look-ahead coding (rodent place-cell forward sweeps)
- Hippocampal-PFC top-down control model (Spiers & Gilbert; Ito et al.)

**Brain regions**:
- Hippocampus, subiculum, perirhinal cortex, parahippocampal cortex, retrosplenial complex (RSC), ventral striatum, frontopolar cortex (FPC), orbitofrontal cortex (OFC)

**Keywords**:
- prospective goal coding, hippocampus, multi-voxel pattern analysis (MVPA), episodic simulation, virtual navigation, route planning, trajectory replay, hippocampal-prefrontal interaction, sub-goal representation, pattern reinstatement, medial temporal lobe, high-resolution fMRI
