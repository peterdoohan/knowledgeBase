---
source_file: tanner2022_asymmetric_connectome.md
paper_id: tanner2022_asymmetric_connectome
title: "Redefining the connectome: A multi-modal, asymmetric, weighted, and signed description of anatomical connectivity"
authors:
  - "Jacob Tanner"
  - "Joshua Faskowitz"
  - "Andreia Sofia Teixeira"
  - "Caio Seguin"
  - "Ludovico Coletta"
  - "Alessandro Gozzi"
  - "Bratislav Misic"
  - "Richard F. Betzel"
year: 2022
journal: "bioRxiv (preprint, posted December 19, 2022)"
paper_type: computational
contribution_type: methodological
species:
  - mouse
methods:
  - fmri
keywords:
  - structural_connectome
  - multi_modal_connectivity
  - asymmetric_edge_weights
  - signed_connectivity_matrix
  - regression_based_weighting
  - structure_function_coupling
  - modularity_community_detection
  - network_neuroscience
  - diffusion_mri_tractography
  - fmri_bold_activity_prediction
  - lifespan_connectome_changes
  - state_dependent_reconfiguration
  - redefining
  - connectome
  - multi
  - modal
  - asymmetric
  - weighted
  - signed
  - description
---

### One-line summary

A regression-based framework is introduced for endowing white-matter fiber tracts with directed, signed, and subject-specific functional weights, producing a connectome that better captures known functional brain organization than traditional diffusion-derived edge weights.

---

### Background & motivation

Standard connectome edge weights (e.g. streamline density, fractional anisotropy) are derived from diffusion MRI and reflect microstructural properties rather than the efficacy of inter-regional communication. Effective connectivity methods can capture directionality and influence but are computationally prohibitive beyond small networks and are typically unconstrained by anatomical topology. This leaves a gap: a scalable, anatomically grounded method that yields directed, functionally interpretable weights for whole-brain networks is lacking. The paper fills this gap by combining the structural sparsity of diffusion tractography with functionally derived regression weights estimated from fMRI BOLD activity.

---

### Methods

- **Model**: For each brain region i, a multilinear regression model predicts region i's BOLD activity at time t from the activity of its structurally connected neighbours at time t-1 (ordinary least squares). Weights W are estimated per node; the resulting matrix is sparse (preserving binary white-matter topology), asymmetric (W_ij != W_ji in general), and signed (positive and negative weights allowed).
- **Human datasets**:
  - HCP 3T resting-state: 95 subjects, Schaefer 200 parcellation, used for model fitting, benchmarking, and asymmetry analyses.
  - HCP 7T resting-state and movie-watching: 117 subjects, Schaefer 400 parcellation, used for state-dependent reconfiguration analyses.
  - Nathan Kline Institute (NKI) Enhanced Rockland Sample: 474 subjects (age 7–85), used for lifespan analyses.
- **Mouse dataset**: Tract-tracing data (Allen Brain Institute, N=182 regions) plus rsfMRI from 18 anaesthetised mice, used for cross-species replication.
- **Benchmarking**: Model fitness (MSE, r between observed and predicted activity) compared against five null models (minimally wired, reordered, spin, topological, temporal).
- **Network analyses**: Modularity maximization (signed variant, Louvain algorithm, 1000 repetitions), graph-theoretic metrics (shortest paths, efficiency, clustering, node strength), asymmetry statistics (per-subject paired-sample tests with FDR correction), age-correlation analyses (spin tests, system-level aggregation).

---

### Key findings

- The regression model predicts held-out fMRI BOLD activity well (group-level r = 0.76 ± 0.03, MSE = 0.43 ± 0.05) and outperforms all five null models (p < 10^-15).
- Weights stabilise rapidly: using ~6% of available frames (64 per scan) yields weights with r = 0.993 vs full-sample weights.
- Weights are subject-specific: model error on held-out same-subject scans is lower than on any other subject's scans (p < 10^-15).
- Within-system connections are predominantly positive and stronger than between-system connections; negative connections show no within/between preference.
- Modular structure of the asymmetric, weighted, and signed network is less lateralised (more bilaterally spanning) and better aligned with known functional systems (higher ARI, higher induced modularity Q*) than the fiber density network (p < 10^-15 for all comparisons).
- 97.5% of edges participate in at least one shortest path in the asymmetric network, compared to only 14.2% in the fiber density network.
- ~30% of connections (8,850 of 29,024) show statistically significant asymmetries across subjects; asymmetries concentrate within control, default, and visual networks. Unimodal regions show greater in/out similarity than heteromodal regions.
- Movie-watching vs rest: 2,463 edges show significant state-dependent weight differences (FDR q = 0.01), concentrated in visual and dorsal attention networks.
- Lifespan (NKI): age-related weight decreases concentrate within somatomotor network B; increases found from default mode B to control B and from dorsal attention A to central visual. Within-system effects dominate over between-system effects (p = 7.65 × 10^-13).
- Mouse replication is consistent with human results (Fig. S13).

---

### Computational framework

The paper uses a **linear dynamical systems / regression** framework. The core formalism models each brain region's BOLD activity as a linear function of its structurally connected neighbours' activity at the previous time step:

y_i(t) = sum_{j in Gamma_i} W_ji * y_j(t-1) + c_i

Key variables: W (n x n sparse, asymmetric, signed weight matrix), y_i(t) (BOLD activity of region i at time t), Gamma_i (structurally connected neighbours). The model assumes linear, first-order Markov dynamics and uses OLS estimation independently per node. No generative/sampling component is used; the model is explanatory rather than generative. Two biophysical neural mass models (Galán/Wilson-Cowan linearisation; reduced Wong-Wang mean field) are used in supplementary analyses to compare the new weighting scheme against fiber density as a structural constraint for forward simulations of FC.

---

### Prevailing model of the system under study

The paper pushes against the standard approach in network neuroscience in which structural connectome edges are weighted using microstructural parameters from diffusion MRI (fractional anisotropy, streamline density), which are interpreted as proxies for communication efficacy but do not reflect directionality or functional influence. The alternative — effective connectivity (DCM, Granger causality) — provides directed, signed weights but is computationally intractable at the whole-brain scale (~10^2 nodes) and typically does not enforce sparsity from white-matter anatomy. The prevailing assumption is thus that structural connections are undirected, positive, and fixed over typical scanning sessions. The paper also challenges the implicit assumption that white-matter topology and community structure are sufficient to recover functional brain systems; in practice, fiber density–weighted networks yield lateralised, functionally misaligned modules.

---

### What this paper contributes

The paper demonstrates that embedding functional information (fMRI BOLD regression weights) into the anatomical white-matter scaffold yields a connectome with several empirically superior properties: community structure aligned with functional systems and brain maps, near-complete edge participation in shortest paths (vs ~14% for fiber density), robust and anatomically localised directional asymmetries, and detectable state- and age-dependent reconfiguration at structurally defined edges. This establishes a practical middle ground between diffusion-based weighting (tractable but undirected and functionally misaligned) and dynamic causal modelling (directed but intractable). A key conceptual contribution is that connectome edge weights need not be static or undirected: when weighted via this scheme, structural edges inherit dynamic, context-dependent, and signed properties typically attributed to functional connections, suggesting a tighter structure-function bridge. The approach also reduces the multiple-comparisons burden in brain-wide association studies by restricting tests to sparse structural edges.

---

### Brain regions & systems

The paper operates at the level of parcellated cortical regions and canonical brain systems rather than individual anatomical areas. Named systems include:

- **Default mode network (DMNa, DMNb, DMNc)** — shows asymmetric within-system weights and age-related increases in weights toward control networks.
- **Somatomotor network (SMNa, SMNb)** — exhibits greater in/out weight similarity (unimodal); within-system weights decrease with age.
- **Visual networks (central visual, peripheral visual)** — state-dependent weight changes during movie-watching concentrate here; asymmetries found between central and peripheral visual.
- **Dorsal attention network (DANa, DANb)** — shows age-related weight changes and state-dependent modulation toward visual networks.
- **Control/frontoparietal network (ContC)** — asymmetric within-system weights; age-related increases from DMN.
- **Temporo-parietal network** — between-system asymmetries noted.
- **Salience/ventral attention network** — age-related decreases detected at fine scale.

Subcortical and cerebellar regions are explicitly excluded and noted as a limitation.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It proposes and characterises a regression-based algorithm for assigning functional edge weights to structural connections, and validates it against null models and alternative weighting schemes using fMRI and tractography data. However, it does not provide neural recordings, pharmacology, or perturbation data that specifically adjudicate between the regression-weight algorithm and alternative accounts of how inter-regional influence is implemented. The paper acknowledges that signed edge weights likely reflect feed-forward/feedback inhibition or glutamate/GABA balance at the circuit level, but these remain post-hoc speculations rather than tested mechanistic claims. The study operates at Marr's computational and (to some extent) algorithmic levels but does not address implementational questions about cell types, neuromodulators, or biophysical mechanisms.

---

### Limitations & open questions

- Relies on diffusion MRI and tractography for the structural scaffold, which has well-documented biases (false positives/negatives, inability to resolve directionality of tracts). Partially mitigated by mouse tract-tracing replication.
- Analysis is restricted to neocortex; subcortical and cerebellar contributions to regional time series are ignored.
- Regression weights vary with the number and identity of included nodes: adding subcortical regions would change estimated weights.
- The model is explanatory but not generative; it cannot simulate novel brain dynamics.
- Signed edges are statistical constructs: assigning excitatory/inhibitory labels requires additional assumptions not tested here.
- The model is not easily compared to established effective connectivity methods (DCM, GEVI); formal benchmarking is proposed as future work.
- State-based weight reconfiguration is demonstrated for rest vs movie-watching but sensitivity/specificity for other cognitive states is unknown.
- The regression framework assumes linear, first-order Markov dynamics, which may not capture nonlinear or longer-lag interactions.

---

### Connections & keywords

**Key citations**:
- Sporns, Tononi & Kotter 2005 (human connectome concept)
- Hagmann et al. 2008 (structural core of cerebral cortex)
- Betzel & Bassett 2018 (specificity of long-distance connections in weighted connectomes)
- Honey et al. (Galán model, structure-function coupling)
- Oh et al. 2014 (Allen Brain Institute mouse connectome)
- Human Connectome Project (Van Essen et al.)
- Schaefer et al. (200/400 parcellations)
- Bassett & Sporns 2017 (network neuroscience review)
- Sporns & Betzel 2016 (modular brain networks)
- Frässle et al. 2018 (whole-brain effective connectivity)

**Named models or frameworks**:
- Louvain modularity maximization (signed variant, Gomez et al.)
- Galán/Wilson-Cowan neural mass model
- Reduced Wong-Wang mean field model
- Balloon-Windkessel hemodynamic model
- Distance-dependent consensus connectome (Betzel et al.)
- Spin test null model

**Brain regions**:
- Default mode network (DMNa/b/c)
- Somatomotor network (SMNa/b)
- Central and peripheral visual networks
- Dorsal attention network (DANa/b)
- Control/frontoparietal network (ContC)
- Temporo-parietal network
- Salience/ventral attention network

**Keywords**:
- structural connectome
- multi-modal connectivity
- asymmetric edge weights
- signed connectivity matrix
- regression-based weighting
- structure-function coupling
- modularity / community detection
- network neuroscience
- diffusion MRI / tractography
- fMRI BOLD activity prediction
- lifespan connectome changes
- state-dependent reconfiguration
