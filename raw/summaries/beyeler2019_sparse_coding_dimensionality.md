---
source_file: beyeler2019_sparse_coding_dimensionality.md
paper_id: beyeler2019_sparse_coding_dimensionality
title: "Neural correlates of sparse coding and dimensionality reduction"
authors:
  - "Michael Beyeler"
  - "Emily L. Rounds"
  - "Kristofor D. Carlson"
  - "Nikil Dutt"
  - "Jeffrey L. Krichmar"
year: 2019
journal: "PLoS Computational Biology"
paper_type: review
contribution_type: review
methods:
  - computational_modeling
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - striatum
  - retrosplenial_cortex
  - visual_cortex
  - primary_auditory_cortex
keywords:
  - nonnegative_sparse_coding
  - nonnegative_matrix_factorisation
  - dimensionality_reduction
  - efficient_coding_hypothesis
  - parts_based_representation
  - population_coding
  - receptive_field_modelling
  - basis_functions
  - corticostriatal_dimensionality_reduction
  - retrosplenial_cortex_spatial_navigation
  - spike_triggered_nmf
  - hebbian_plasticity_homeostatic_scaling
  - neural
  - correlates
  - sparse
  - coding
  - dimensionality
  - reduction
---

### One-line summary

Nonnegative sparse coding (NSC), a form of efficient population coding via dimensionality reduction and nonnegativity constraints, can account for a wide range of neuronal response properties across sensory areas, associative cortices, and the basal ganglia.

---

### Background & motivation

Brains must extract behaviorally relevant information from high-dimensional sensory inputs using anatomically constrained, convergent pathways — for example, compressing 100 million photoreceptors into 1 million optic nerve fibers. Sparse coding and dimensionality reduction are two related strategies for addressing this challenge. While sparse coding and efficient coding theories have been well developed for early visual cortex, it remains unclear how broadly these principles generalise across different brain systems. This review synthesises computational and empirical evidence bearing on whether nonnegative sparse coding (NSC) — which enforces parts-based, additive decompositions — applies beyond primary sensory areas.

---

### Methods

This is a narrative review of computational modelling studies and associated experimental evidence.

- Scope covers NSC and closely related approaches (nonnegative matrix factorisation, NMF; spike-triggered NMF; reinforcement-driven dimensionality reduction) applied to a range of brain areas.
- Brain regions reviewed: retina, V1, V2, inferotemporal cortex (IT), dorsal medial superior temporal area (MSTd), auditory cortex (A1), olfactory cortex, somatosensory cortex (S1/barrel cortex), retrosplenial cortex (RSC), basal ganglia, hippocampus, and parietal cortex.
- The review compares NSC model outputs against experimentally recorded single-unit and population responses, evaluating whether emergent basis functions resemble empirical receptive fields and population statistics.
- Related unsupervised methods (PCA, ICA, compressed sensing) are discussed as foils for NSC's distinctive parts-based, nonnegative decomposition.

---

### Key findings

- NSC applied to natural images yields V1-like oriented, spatially localised simple-cell receptive fields, providing an information-theoretic explanation for empirically observed tuning (Olshausen & Field; Hoyer).
- Spike-triggered NMF (STNMF) applied to retinal ganglion cells recovers individual presynaptic bipolar cell subunits verified against simultaneous multielectrode and sharp-electrode recordings.
- NMF applied to simulated MT input neurons recovers MSTd-like basis flow fields that match experimentally recorded MSTd response properties, including the relative overrepresentation of lateral headings and mixed selectivity for heading and eye-rotation velocity.
- NMF applied to rat RSC electrophysiology recovers sparse, parts-based representations of allocentric position, head direction, and route-based movement direction, with population statistics closely matching recorded RSC neurons; STDP with homeostatic scaling (STDPH) produces a biologically plausible approximation of the same NMF decomposition.
- NMF applied to olfactory perceptual data (144 monomolecular odors, 146-dimensional profiles) reveals 10 sparsely activated basis functions that span the space of behaviorally relevant odors, with a block-diagonal structure indicating each odor is dominated by a single basis.
- Sparse coding models explain response properties of A1 neurons (spectro-temporal receptive fields) and rodent barrel cortex neurons; the rectified latent variable model (RLVM, an NMF variant) outperforms PCA in reconstructing two-photon imaging data from mouse S1.
- The reinforcement-driven dimensionality reduction (RDDR) model provides a dopamine-modulated Hebbian/anti-Hebbian mechanism by which the basal ganglia could extract reward-relevant input dimensions from cortical convergence.
- NSC does not apply to prefrontal cortex or primary motor cortex, where population codes are dense, high-dimensional, and better described by recurrent network or random projection models.
- Recent evidence (Stringer et al. 2018/2019) shows that mouse V1 responses to natural images are high-dimensional and multiplex sensory and behavioral signals, suggesting efficient coding provides an incomplete picture of V1.

---

### Computational framework

NSC is a specialisation of linear sparse coding with nonnegative constraints on both basis functions (W) and activation coefficients (H), implemented via nonnegative matrix factorisation (NMF). The core formalism:

- Data matrix V (F features × S stimuli) is decomposed as V ≈ WH, where W is F × B and H is B × S.
- Optimisation minimises a cost combining reconstruction error and an L1 sparsity penalty on H, controlled by a trade-off parameter λ.
- Nonnegativity of W and H enforces parts-based (additive) representations — features can only combine, never cancel.
- The number of basis functions B < F implements dimensionality reduction; B > F implements expansion (as in V1 overcomplete codes).
- Model neurons are interpreted as having connection weights given by columns of W; their response to a stimulus is the dot product of their weights with the stimulus vector, passed through an activation function.
- Key assumption: neural responses and synaptic weights are nonnegative (or can be separated into ON/OFF channels to preserve this).
- Related: STDPH (Carlson et al.) provides a biologically plausible spiking implementation that approximates NMF through Hebbian STDP stabilised by homeostatic scaling.

---

### Prevailing model of the system under study

The paper engages with the efficient coding hypothesis, rooted in Barlow (1961) and Attneave (1954), which posits that sensory systems are tuned to the statistics of the natural environment to maximise information transmission by minimising redundancy. Olshausen and Field's sparse coding showed that this principle predicts V1-like simple cell receptive fields. The implicit baseline model is that efficient coding and sparse coding are well-established for early sensory areas but are generally not assumed to operate in higher-order sensory, associative, or subcortical areas, where neurons are often thought to encode task-relevant variables in complex, mixed-selectivity patterns without a straightforward efficient-coding interpretation.

---

### What this paper contributes

The review consolidates and extends the case that NSC, as a specific form of efficient coding with nonnegativity constraints, generalises beyond early sensory cortex. Key additions to the prevailing model:

- NSC can account for complex, multi-variable, reference-frame-conjunctive responses in an associative area (RSC) that had not previously been considered sparse or parts-based.
- NSC provides a plausible mechanism for dimensionality compression in the cortico-basal ganglia pathway, and the RDDR model links this to dopamine-modulated plasticity and Parkinson's disease symptoms.
- Parts-based representations in IT, MSTd, and RSC are unified under a single computational principle, suggesting that basis-function coding may be a general strategy for encoding high-dimensional stimulus and navigational spaces.
- The STDPH mathematical result establishes a direct link between NSC and a biologically plausible synaptic learning rule, connecting the computational framework to a neural implementation.
- The review also clearly delineates where NSC fails (PFC, M1, high-dimensional V1 responses), providing boundary conditions for the framework.

---

### Brain regions & systems

- **Retina (retinal ganglion cells)** — NSC/STNMF recovers individual presynaptic bipolar cell subunits underlying ganglion cell receptive fields.
- **V1 (primary visual cortex)** — NSC predicts orientation-tuned, spatially localised simple-cell receptive fields from natural image statistics; recent evidence challenges the extent of sparsity in V1.
- **V2** — NSC explains edge-like pooling of spatial frequency channels, end-stopping, and contour integration.
- **Inferotemporal cortex (IT)** — NMF recovers parts-based face representations consistent with IT neurons encoding individual facial features; whole faces reconstructable from ~200 neurons.
- **MSTd (dorsal medial superior temporal area)** — NSC model recovers basis flow fields matching empirical MSTd receptive fields and population statistics for heading and eye-rotation encoding.
- **Primary auditory cortex (A1)** — NSC describes spectro-temporal receptive fields of A1 neurons; efficient sparse coding of natural sounds.
- **Olfactory cortex (piriform cortex / olfactory bulb)** — Sparse combinatorial coding in granule cells and ~10% activation of piriform cortex neurons consistent with NSC; NMF applied to perceptual odor data recovers meaningful olfactory dimensions.
- **Somatosensory cortex (S1 / barrel cortex)** — Sparse coding models explain rodent barrel cortex responses; RLVM outperforms PCA for mouse S1 two-photon data; evidence against NSC in primate area 2.
- **Retrosplenial cortex (RSC)** — NSC and STDPH recover conjunctive, reference-frame-specific spatial navigation representations; prime example of NSC outside sensory cortex.
- **Basal ganglia** — RDDR model proposes dopamine-modulated Hebbian/anti-Hebbian learning implements NMF-like dimensionality reduction in cortico-striatal pathway.
- **Prefrontal cortex (PFC) and primary motor cortex (M1)** — Dense, high-dimensional population codes; NSC not supported; better described by recurrent networks or random projections.

---

### Mechanistic insight

The paper partially meets the bar. For RSC, it provides a computational model (NMF/STDPH) and compares outputs against electrophysiological recordings, showing that simulated neuron types and population statistics match experimental data. However, the neural recordings were not designed to test NSC specifically, and the comparison is post hoc rather than a prospective test of NSC against alternative models. For the retina (STNMF), the match between NMF-derived modules and identified bipolar cell subunits — verified by simultaneous sharp-electrode recordings — comes closest to a direct mechanistic test. That said, the paper does not use the data to discriminate NSC from alternative coding algorithms.

- **Computational**: The brain solves the problem of efficiently representing high-dimensional sensory and navigational inputs under bandwidth and energy constraints, using a parts-based, additive decomposition that maximises information per neuron.
- **Algorithmic**: NMF/NSC provides the representational scheme — sparse, nonnegative activation of basis functions — and STDPH provides the learning rule: Hebbian STDP stabilised by homeostatic synaptic scaling, approximating NMF.
- **Implementational**: Nonnegative synaptic weights modelled as excitatory ON/OFF pathways; lateral inhibitory connections supporting anti-Hebbian competition; dopamine-modulated LTP/LTD in corticostriatal projections. These are theoretically motivated but not all directly verified.

---

### Limitations & open questions

- NSC does not apply to all brain areas; PFC and M1 use dense, high-dimensional codes, and the conditions that determine which coding regime a region adopts are not fully understood.
- Recent high-density recordings from mouse V1 (Stringer et al.) show high-dimensional, mixed sensory-behavioral responses, challenging the extent to which efficient/sparse coding captures V1 activity.
- Apparent dimensionality of population responses depends on the complexity of the input space and the number of simulated neurons, making it difficult to set absolute dimensionality values.
- The exact number of basis functions (B) must be determined empirically; no principled biological criterion for this choice is established.
- The connection between NSC and the diverse synaptic plasticity rules found across species, brain regions, and developmental stages is not yet understood.
- NSC predictions for hippocampus, VIP, VPS, and parietal cortex remain untested; the review identifies these as candidate regions but does not provide evidence.
- Sparse population activity is not sufficient evidence for a sparse-coding scheme; distinguishing these empirically remains a challenge.
- The RDDR model's prediction that lateral connections in the basal ganglia shape corticostriatal correlations via dopamine-modulated LTP/LTD has not been experimentally validated.

---

### Connections & keywords

**Key citations:**
- Olshausen BA & Field DJ (1996, 1997) — sparse coding and V1 receptive fields
- Lee DD & Seung HS (1999) — NMF and parts-based face representations in IT
- Hoyer PO (2002, 2003) — nonnegative sparse coding, V1 modelling
- Bar-Gad I et al. (2000, 2003) — RDDR model; dimensionality reduction in basal ganglia
- Beyeler M et al. (2016) — NSC model of MSTd responses
- Rounds EL et al. (2018) — STDPH model of RSC conjunctive coding
- Liu JK et al. (2017) — spike-triggered NMF (STNMF), retinal subunit identification
- Castro JB et al. (2013) — NMF applied to olfactory perceptual space
- Stringer C et al. (2018, 2019) — high-dimensional V1 responses, behaviour-mixed representations
- Carlson KD et al. — STDPH as approximation of NMF

**Named models or frameworks:**
- Nonnegative sparse coding (NSC)
- Nonnegative matrix factorisation (NMF)
- Efficient coding hypothesis
- Spike-triggered nonnegative matrix factorisation (STNMF)
- Reinforcement-driven dimensionality reduction (RDDR)
- Rectified latent variable model (RLVM)
- Spike-timing-dependent plasticity with homeostatic synaptic scaling (STDPH)
- Independent component analysis (ICA)
- Principal component analysis (PCA)
- Compressed sensing

**Brain regions:**
- Retina, V1, V2, inferotemporal cortex (IT), MSTd, primary auditory cortex (A1), olfactory bulb, piriform cortex, somatosensory cortex (S1/barrel cortex), retrosplenial cortex (RSC), basal ganglia (striatum), prefrontal cortex (PFC), primary motor cortex (M1)

**Keywords:**
- nonnegative sparse coding
- nonnegative matrix factorisation
- dimensionality reduction
- efficient coding hypothesis
- parts-based representation
- population coding
- receptive field modelling
- basis functions
- corticostriatal dimensionality reduction
- retrosplenial cortex spatial navigation
- spike-triggered NMF
- Hebbian plasticity homeostatic scaling
