---
source_file: "harris2019_hierarchical_cortical_connectivity.md"
paper_id: "harris2019_hierarchical_cortical_connectivity"
title: "Hierarchical organization of cortical and thalamic connectivity"
authors: "Julie A. Harris, Stefan Mihalas, Karla E. Hirokawa, Jennifer D. Whitesell, Hannah Choi, Amy Bernard, Phillip Bohn, Shiella Caldejon, Linzy Casal, Andrew Cho, Aaron Feiner, David Feng, Nathalie Gaudreault, Charles R. Gerfen, Nile Graddis, Peter A. Groblewski, Alex M. Henry, Anh Ho, Robert Howard, Joseph E. Knox, Leonard Kuan, Xiuli Kuang, Jerome Lecoq, Phil Lesnar, Yaoyao Li, Jennifer Luviano, Stephen McConoughey, Marty T. Mortrud, Maitham Naeemi, Lydia Ng, Seung Wook Oh, Benjamin Ouellette, Elise Shen, Staci A. Sorensen, Wayne Wakeman, Quanxin Wang, Yun Wang, Ali Williford, John W. Phillips, Allan R. Jones, Christof Koch, Hongkui Zeng"
year: 2019
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
brain_regions: ["prelimbic_cortex", "retrosplenial_cortex", "thalamus", "mediodorsal_thalamus", "visual_cortex"]
keywords: ["hierarchical", "organization", "cortical", "thalamic", "connectivity"]
---

### One-line summary

Using ~1,000 new Cre-driver viral tracing experiments in mouse cortex and thalamus, this paper derives cell-class-specific anatomical rules for corticocortical, thalamocortical, and corticothalamic projections and shows that these connections form a shallow but significant hierarchy across the entire mouse corticothalamic network.

---

### Background & motivation

A hierarchical organisation of cortical areas — in which feedforward and feedback projections can be distinguished by their laminar patterns — was established in primate sensory systems, but it was unclear whether this principle generalises across all of mouse cortex and thalamus, or how it depends on specific cell classes. Prior connectome resources lacked cell-class resolution, mapping projections from mixed populations without distinguishing layer of origin or projection neuron type. Understanding these rules is essential for interpreting how information flows through the cortex and for building principled models of cortical computation. This paper fills the gap by combining Cre-driver specificity with whole-brain imaging at mesoscale resolution across nearly the full mouse cortex and thalamus.

---

### Methods

- **Subjects**: Adult male and female C57BL/6J mice and 49 Cre driver lines (50 mouse lines total); injections at average age P56 + 10 days.
- **Tracers**: Cre-dependent AAV vectors expressing EGFP or synaptophysin-EGFP injected into cortical or thalamic regions; pan-neuronal AAV for wild-type mice.
- **Scale**: 1,081 cortical and 81 thalamic tracer experiments suitable for analysis, adding 1,256 new experiments to the Allen Mouse Brain Connectivity Atlas.
- **Imaging**: Serial two-photon tomography (STPT) with automated signal detection and registration to the Allen Common Coordinate Framework v3 (CCFv3).
- **Cell-class resolution**: 15 Cre lines selected to comprehensively represent L2/3 IT, L4 IT, L5 IT, L5 IT+PT, L5 PT, and L6 CT projection classes; 849 cortical experiments used for corticocortical (CC) and corticothalamic (CT) analyses; 81 thalamic experiments for thalamocortical (TC) analyses.
- **Manual verification**: 31,304 CC connections, 22,528 CT connections, and 6,966 TC connections manually checked as true positive or negative.
- **Laminar quantification**: Automated quantification of layer-specific projection density using CCFv3 layer registration; 7,063 unique source-line-target connections subjected to unsupervised hierarchical clustering into nine laminar termination pattern clusters.
- **Modularity analysis**: Louvain community detection on a data-driven voxel-level connectivity model; resolution parameter gamma varied 0–2.5; six stable modules identified at gamma = 1.3 (Q = 0.36).
- **Hierarchy model**: Exhaustive search over feedforward/feedback assignments to nine laminar clusters to maximise a global hierarchy score; iterative refinement of area-level hierarchy positions; three hierarchy versions built sequentially from CC, then CC+TC, then CC+TC+CT connections; shuffled controls (n = 100) and a perfectly hierarchical upper bound computed for comparison.
- **Single-neuron morphology**: 25 sparsely labelled L4 neurons reconstructed by fMOST whole-brain imaging and Vaa3D-TeraVR software to confirm long-range projections.

---

### Key findings

- Mouse cortex has robust modular organisation with six modules (prefrontal, lateral, somatomotor, visual, medial, auditory); Q = 0.36, significantly above shuffled (difference 0.22 ± 0.017 s.d.) at gamma = 1.3.
- CC projections are present from all cortical layers (L2/3 through L6); L4 neurons were confirmed to make long-range corticocortical projections, including via spiny stellate cells.
- L5 Rbp4 (IT+PT) neurons have the broadest out-degree of any Cre line; projections from all other lines form a subset of Rbp4 targets (< 5% unique to any individual non-Rbp4 line).
- Nine distinct laminar termination pattern clusters characterise CC and TC projections; most Cre lines and TC projection classes are enriched in more than one cluster.
- L2/3 and L4 neurons project predominantly to middle layers (L2/3, L4, L5) in feedforward patterns; L5 PT neurons project to deep layers (L5/L6) or deep plus L1; L6 CT neurons project predominantly to deep layers.
- Core TC neurons (three primary sensory thalamic nuclei: VPL, VPM, LGd) project to L4; matrix-multiareal TC neurons project to L1; intralaminar and matrix-focal neurons to L5/L6.
- Thalamic nuclei cluster into cortical projection patterns resembling the six cortical modules.
- Global hierarchy scores: 0.069 (CC only), 0.120 (CC+TC), 0.128 (CC+TC+CT); adding TC connections approximately doubled the score; all are significant relative to shuffled lower bounds (0.001, 0.044, −0.002) but well below the perfectly hierarchical upper bound (0.679, 0.636, 0.683).
- The hierarchy is shallow: the range between lowest (primary visual cortex) and highest (ORBvl) is less than two full levels; the all-area hierarchy global score lies at ~19% between random and perfect hierarchy.
- Most thalamic nuclei cluster near the bottom or top of the hierarchy, indicating predominantly driver (feedforward) or modulator (feedback) roles; some mid-hierarchy thalamic nuclei show balanced FF/FB connectivity.
- Intermodule hierarchy shows primary sensory modules at bottom, lateral/medial modules in middle, prefrontal at top; intermodule global score 0.07.
- Hierarchies are robust to removal of any individual Cre line or projection class.

---

### Computational framework

The paper introduces a data-driven hierarchical model. The core formalism assigns each cortical and thalamic area a scalar hierarchy score derived from the laminar termination patterns of its inputs and outputs.

- **What is being modelled**: The direction of information flow (feedforward vs. feedback) for each interareal connection, and the relative hierarchical rank of each area.
- **Key variables**: A cluster-to-direction mapping function M (feedforward = +1, feedback = −1); per-area hierarchy scores bounded by −1 and +1; a global hierarchy score that quantifies self-consistency across the network; Cre-line confidence weights to reduce bias from lines with skewed FF/FB distributions.
- **Algorithm**: (1) Unsupervised clustering of laminar termination patterns into nine types; (2) exhaustive search over all possible FF/FB assignments to the nine clusters to maximise the global hierarchy score; (3) iterative refinement of area scores until convergence (~5 iterations); (4) linear discriminant analysis applied to L5/L6 projection strength ratios to classify CT connections as FF or FB.
- **Assumptions**: Laminar termination pattern is a reliable proxy for feedforward vs. feedback direction; shallow hierarchy (all values between −1 and 1); FF and FB TC connections should exist in roughly equal proportions.

The framework extends the classic Felleman & Van Essen (1991) approach by (i) incorporating cell-class-specific layer data, (ii) unifying CC, TC, and CT projections in a single model, and (iii) providing a quantitative global score enabling cross-species and cross-dataset comparisons.

---

### Prevailing model of the system under study

The introduction presents the following baseline understanding:

- The cortex is a laminar, modular, and hierarchically organised structure, with hierarchical order first established in primates by mapping feedforward connections (dense L4 termination) and feedback connections (termination in superficial and deep layers, avoiding L4) — primarily within sensory systems (Felleman & Van Essen 1991; Rockland & Pandya 1979).
- Different projection neuron classes (IT in L2–L6, PT in L5, CT in L6) are thought to contribute distinct connectivity patterns, but prior datasets lacked the cell-class resolution to test this systematically.
- For thalamocortical projections, the accepted framework distinguishes core (driver, L4-targeting) from matrix (modulator, L1-targeting) projections; for corticothalamic projections, L6 is considered feedback and L5 feedforward.
- It was an open question whether the hierarchical principle — established for primate sensory cortex — applies globally across the entire mouse cortex and whether a unified hierarchy incorporating thalamus could be derived.

---

### What this paper contributes

- Demonstrates that a significant cortical hierarchy can be derived for the entire mouse cortex using purely anatomical laminar termination data, confirming that the hierarchical principle generalises from primate sensory systems to the full mouse cortex.
- Shows that thalamus is an integral part of the hierarchy, not a separate structure: including TC and CT connections approximately doubles the global hierarchy score.
- Reveals that the mouse cortical hierarchy is shallow — only ~19% of the way between random and perfectly hierarchical — which the authors suggest reflects the high connection density of mouse cortex and is consistent with its relatively uniform cytoarchitecture.
- Provides the first cell-class-resolved map of laminar projection patterns, showing that L2/3 and L4 have predominantly feedforward patterns while L5 and L6 contribute to both feedforward and feedback, refining the classical view.
- Demonstrates unexpected long-range projections from L4 neurons (including spiny stellate cells), challenging the canonical view that L4 is purely a local relay layer.
- Generates testable quantitative predictions of hierarchical position for 37 cortical areas and 24 thalamic nuclei, enabling direct cross-species and cross-condition comparisons using the published global hierarchy score metric and code.

---

### Brain regions & systems

- **Mouse isocortex (all 43 annotated areas)** — primary subject of connectivity mapping and hierarchical analysis; six functional modules identified (prefrontal, lateral, somatomotor, visual, medial, auditory).
- **Primary visual cortex (VISp)** — lowest-ranked area in the cortical hierarchy (most feedforward inputs); used as benchmark for validating hierarchical assignments.
- **Orbital area, ventrolateral part (ORBvl)** — highest-ranked cortical area in the hierarchy (most feedback inputs); top of prefrontal module.
- **Prefrontal areas (ACAd, ACAv, PL, ILA, ORBl, ORBm, ORBvl, FRP)** — top of intermodule hierarchy.
- **Somatomotor areas (MOp, MOs, SSp-*, SSs)** — form their own module; intermediate hierarchy position.
- **Visual areas (VISp, VISl, VISal, VISpl, VISrl, VISli, VISa, VISam, VISpm, VISpor)** — bottom of hierarchy; form dense intramodule network analysed separately.
- **Thalamus (24 nuclei analysed)** — integrated into the cortical hierarchy; most nuclei cluster near the bottom (driver) or top (modulator).
  - VPL, VPM, LGd — core (feedforward/driver) thalamic nuclei, project to L4.
  - Mediodorsal nucleus (MD) — matrix-type; location within MD determines cortical projection pattern more than Cre line.
  - VM, PVT, CM, CL, PF — intralaminar or matrix nuclei; diverse positions in hierarchy.
- **Retrosplenial cortex (RSPagl, RSPd, RSPv)** — medial module; mid-hierarchy.
- **Auditory cortex (AUDp, AUDd, AUDpo, AUDv)** — form auditory module; relatively low in hierarchy.
- **Temporal association area (TEa), perirhinal (PERI), ectorhinal (ECT)** — lateral module; intermediate positions.

---

### Mechanistic insight

The paper partially meets the bar. It presents an algorithm (the hierarchical model based on laminar termination patterns) and provides extensive anatomical data (1,081 cortical + 81 thalamic tracing experiments with cell-class resolution) that constrain the model. However, the data are structural (anterograde viral tracing of axonal projections), not physiological recordings. The paper does not provide electrophysiological, calcium imaging, or functional data that would specifically support the feedforward/feedback direction assignments over alternatives. The mapping from anatomy to information-flow direction rests on the assumption — imported from prior primate physiology — that L4-targeting projections are feedforward.

Mapping onto Marr's levels where possible:

- **Computational**: The cortex solves the problem of routing and transforming sensory information through a directed hierarchy toward higher-order integration areas; thalamus participates as both driver (feedforward relay) and modulator (feedback broadcast).
- **Algorithmic**: Feedforward connections (terminating in middle layers, especially L4) carry driving input from lower to higher areas; feedback connections (terminating in superficial and deep layers, avoiding L4, or targeting L1) carry modulatory signals from higher to lower areas; this is implemented by distinct projection neuron classes (L2/3 and L4 IT neurons predominantly feedforward; L5 and L6 neurons mixed; core thalamic neurons feedforward; matrix thalamic neurons feedback).
- **Implementational**: Specific Cre-defined projection neuron classes underlie the laminar specificity: L4 IT neurons (Nr5a1, Rorb, Scnn1a-Tg3 lines), L5 PT (A93, Chrna2, Sim1, Efr3a lines), L6 CT (Ntsr1, Syt6 lines) each have distinct projection targets and laminar termination profiles. The paper provides the most direct cellular-level implementation data but stops short of linking specific classes to measured functional properties.

The absence of functional validation means the directional assignments (FF/FB) remain inferences from anatomy, not proven mechanistic claims.

---

### Limitations & open questions

- Hierarchy is derived from anatomy only; feedforward/feedback functional assignments are inferred by analogy with primate physiology, not directly validated by mouse electrophysiology.
- The hierarchy is shallow (~19% between random and perfect), meaning hierarchical position alone explains only a small fraction of the variance in connectivity patterns; many connections cross hierarchical levels in both directions.
- No Cre line was available for L6 IT neurons, leaving this projection class unmapped.
- Connection strengths are not incorporated into the hierarchy computation (except for thresholding weak connections); a strength-weighted hierarchy might yield different results.
- The study uses a mesoscale connectome; single-cell and microcircuit-level principles remain to be established.
- It is unclear how this shallow mouse hierarchy relates to the steeper primate hierarchy; direct cross-species comparison using the global hierarchy score is now possible but not done here.
- The model does not account for more than two connection types (FF/FB); future models incorporating additional labels (e.g., lateral connections) may reveal additional organisational principles.
- Some CT projections travel through thalamic regions before reaching final targets, potentially inflating connection strength estimates despite the manual masking procedure.
- Hierarchy predictions for individual areas (e.g., FRP, VISC) have limited experimental replication and should be treated as preliminary.

---

### Connections & keywords

**Key citations**:
- Felleman & Van Essen (1991) — Distributed hierarchical processing in primate cortex; original feedforward/feedback laminar rules
- Oh et al. (2014) — Allen Mouse Brain Connectivity Atlas mesoscale connectome
- Rockland & Pandya (1979) — Laminar origins and terminations of cortical connections
- Markov et al. (2014) — Weighted directed interareal connectivity in macaque; anatomy of hierarchy
- Harris & Shepherd (2015) — Neocortical circuit themes and variations; IT/PT/CT classification
- Sherman (2016) — Thalamus as ongoing cortical modulator; core/matrix and driver/modulator framework
- Zingg et al. (2014) — Neural networks of mouse neocortex; modular structure
- Knox et al. (2018) — High-resolution data-driven model of the mouse connectome
- Crick & Koch (1998) — No-strong-loops hypothesis for cortical/thalamic projections
- Coogan & Burkhalter (1993) — Hierarchical organization in rat visual cortex

**Named models or frameworks**:
- Allen Mouse Brain Connectivity Atlas (http://connectivity.brain-map.org)
- Allen Common Coordinate Framework v3 (CCFv3)
- Louvain community detection algorithm
- Global hierarchy score (quantitative hierarchical self-consistency metric)
- Core/matrix/intralaminar thalamic projection classification (Jones 1998; Clascá et al. 2012)
- IT/PT/CT cortical projection neuron classification

**Brain regions**: Mouse isocortex (43 areas), thalamus (24–29 nuclei), VISp, ORBvl, ACAd, PL, ILA, MOp, MOs, SSp, RSP, AUD, TEa, VPL, VPM, LGd, MD, VM, PVT, CL, PF, LP, AV, LD

**Keywords**: mesoscale connectome, cortical hierarchy, feedforward feedback, laminar termination patterns, Cre driver lines, thalamocortical connectivity, corticothalamic connectivity, Allen Mouse Brain Connectivity Atlas, cortical modules, projection neuron classes, IT PT CT neurons, global hierarchy score, mouse cortex, shallow hierarchy, anterograde viral tracing
