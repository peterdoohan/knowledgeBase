---
source_file: haber2022_prefrontal_connectomics.md
paper_id: haber2022_prefrontal_connectomics
title: "Prefrontal connectomics: from anatomy to human imaging"
authors:
  - "Suzanne N. Haber"
  - "Hesheng Liu"
  - "Jakob Seidlitz"
  - "Ed Bullmore"
year: 2022
journal: Neuropsychopharmacology
paper_type: review
contribution_type: review
species:
  - human
methods:
  - fmri
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - ventral_tegmental_area
  - retrosplenial_cortex
  - posterior_cingulate_cortex
keywords:
  - prefrontal_connectomics
  - monosynaptic_connectivity
  - tract_tracing
  - dmri_tractography
  - resting_state_fmri
  - graph_theory_hubs
  - connector_hubs
  - white_matter_pathways
  - anterior_limb_internal_capsule
  - deep_brain_stimulation
  - non_human_primate
  - cross_species_translation
  - network_modules
  - participation_coefficient
  - false_positive_streamlines
  - prefrontal
  - connectomics
  - anatomy
  - human
  - imaging
key_citations:
  - haber2014_reward_circuit_incentive_learning
---

### One-line summary

This review bridges non-human primate (NHP) tract-tracing data and human MRI-derived connectivity by systematically comparing monosynaptic prefrontal cortical connections in NHPs with diffusion MRI tractography and resting-state fMRI network organisation in humans.

---

### Background & motivation

Neuroimaging, particularly diffusion-weighted MRI (dMRI) and resting-state fMRI (rs-fMRI), has become the dominant tool for mapping human brain networks and implicating circuit dysfunction in psychiatric disorders. However, these methods are indirect and do not visualise axons or their directionality, raising the fundamental question of how well MRI-derived networks and hubs reflect the monosynaptic "hard wiring" established by NHP tract-tracing studies. A growing literature links psychiatric illnesses to hub and network abnormalities measured by MRI, yet the anatomical validity of those hubs remains insufficiently tested. This review addresses that gap by directly comparing what is known about monosynaptic PFC connectivity from tract tracing with what MRI-based methods reveal about network organisation and hubs.

---

### Methods

This is a narrative review synthesising three intersecting bodies of literature:

- **NHP tract-tracing anatomy**: anterograde and retrograde tracers, and viral tracers; coverage of all major PFC regions (OFC, ACC, dlPFC, vlPFC, frontal pole) and their white-matter pathways (SLF, uncinate fasciculus, cingulum bundle, anterior limb of the internal capsule [ALIC], medial forebrain bundle [MFB]).
- **Human and NHP MRI connectivity methods**: dMRI tractography, structural covariance, morphometric similarity, and resting-state fMRI functional connectivity; graph-theoretical analysis of hubs, modules, degree centrality, participation coefficient.
- **Cross-species, cross-modal validation studies**: specific examples where tracer injections and dMRI were carried out in the same NHP animals, then translated to human Human Connectome Project data. Three case studies are highlighted: (1) ascending VTA dopamine pathway versus false-positive ALIC streamlines; (2) topographic segmentation of the ALIC; (3) identification of a connectional hub within the rostral ACC (rACC).

---

### Key findings

- All PFC regions have both short-distance (neighbouring cortical areas) and long-distance connections; fibers from different PFC subregions occupy topographically organised positions within the ALIC, enabling its segmentation into five functional zones.
- dMRI tractography reliably produces false-positive streamlines: e.g., VTA dopamine fibers do not travel through the IC (as claimed for the "superolateral MFB"), confirmed by tyrosine-hydroxylase immunostaining in both NHP and human brains.
- The relative topographic organisation of ALIC fiber bundles is conserved across individuals and species, enabling translation from NHP tracer experiments to human DBS targeting despite absolute positional variability.
- Within the large rACC region (a DMN hub identified by rs-fMRI), tract tracing in NHPs identified a discrete subregion with disproportionately diverse inputs (from dlPFC, vlPFC, OFC, FEFs, vmPFC); dMRI tractography and rs-fMRI seed analyses in both NHPs and humans converged on the same location.
- Graph-theoretical analysis confirms PFC contains connector hubs (high intermodular degree, long-distance connections to parietal, temporal, and posterior cingulate cortex), consistent with anatomical tracing showing transmodal connectivity.
- Hubs defined by MRI are disproportionately affected by neurological and psychiatric disorders (e.g., schizophrenia affects PFC hubs; Alzheimer's disease affects temporal hubs).
- Rs-fMRI functional connectivity is largely but not entirely determined by underlying monosynaptic anatomy; functional connections are most stable between regions with reciprocal structural connections.

---

### Computational framework

The paper does not develop a new computational model. It uses **graph theory** as its primary analytical framework for characterising connectome topology.

Key graph-theoretic concepts applied:
- **Degree centrality**: counting direct connections per node to identify hubs.
- **Weighted, directed, signed connectomes**: the paper discusses how tract-tracing data can produce weighted asymmetric connectomes (directional, variable density) while MRI is forced to produce undirected, symmetric ones.
- **Modularity and participation coefficient**: decomposing the connectome into modules and distinguishing provincial hubs (high intramodular degree) from connector hubs (high intermodular degree / participation coefficient).
- **Generative network models**: referenced as a framework for understanding how wiring cost minimisation plus topological homophily generate connectome topology; atypical connectomes in schizophrenia are modelled under the same framework.

The core computational question is how well MRI-derived statistical associations (streamline density, BOLD correlation) proxy the ground-truth directed monosynaptic connectivity measured by tract tracing.

---

### Prevailing model of the system under study

The field has long held that psychiatric illnesses reflect dysfunction in specific circuits or networks involving PFC subregions. The introduction situates the paper against a model in which:
- Tract-tracing studies in NHPs established the "hard wiring" of PFC connections, and this monosynaptic connectivity underlies the large-scale network organisation seen in humans.
- Neuroimaging, especially rs-fMRI, has since taken the empirical lead, identifying resting-state networks (DMN, SN, frontoparietal, ventral attention), PFC hubs, and their disruption in disease.
- Graph-theoretical analysis formalised hubs as connector or provincial nodes, and transmodal PFC areas (especially rACC, medial PFC) were proposed as "critical gateways" (following Mesulam's account).
- The implicit working model was that dMRI tractography and rs-fMRI connectivity reflect, even if imperfectly, the underlying monosynaptic anatomy—but this assumption had not been rigorously validated for PFC.

---

### What this paper contributes

The review makes three concrete contributions to the prevailing model:

1. **Establishing the limits and false positives of tractography**: By comparing tracer and dMRI data in the same animals, the paper demonstrates precisely where streamlines diverge from actual anatomy (e.g., false-positive IC entry for the dopamine pathway; false-positive streamlines splitting from the ALIC stalk). This constrains how tractography-based claims about PFC pathways should be interpreted.

2. **Validating topographic invariance as the basis for cross-species translation**: The relative (not absolute) organisation of fiber bundles within the ALIC is conserved across individuals and species. This validates using NHP anatomy to guide human DBS targeting and to interpret MRI-defined connectivity.

3. **Demonstrating multi-scale hub validation**: The rACC case study shows that a hub identified by rs-fMRI can be anatomically grounded and spatially refined using tract tracing, dMRI, and rs-fMRI in a convergent, cross-species framework. This demonstrates a methodology—not just a finding—for validating MRI-defined hubs against monosynaptic anatomy.

Together, the review establishes that MRI methods partially but imperfectly reflect hard wiring, that specific false positives are systematic and predictable, and that targeted cross-modal validation is both feasible and necessary for translating network neuroscience to clinical intervention.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC, areas 11, 13, 14)** — primary node of the limbic network; caudal OFC integrates multisensory inputs; rostral OFC connects to cognitive PFC regions.
- **Anterior cingulate cortex (ACC, areas 24, 25, 32)** — subdivided into sACC (emotion/motivation), rACC (emotion–cognition intersection, DMN hub), dACC (action/motor control, salience network); focus of hub analysis.
- **Dorsolateral PFC (dlPFC, areas 9, 46, 9/46)** — executive function and working memory; connects to parietal cortex via SLF; connector hub for frontoparietal network.
- **Ventrolateral PFC (vlPFC, areas 44, 45, 47/12)** — behavioral flexibility, language, memory retrieval; intermediate position between sensory, motor, and limbic systems.
- **Frontal pole (area 10)** — higher cognitive function and abstract reasoning; apex of PFC hierarchy in NHPs; large in humans.
- **Anterior limb of the internal capsule (ALIC)** — white-matter pathway carrying all PFC fibers to subcortex; topographically segmentable; target for DBS in OCD and depression.
- **Medial forebrain bundle (MFB)** — carries ascending VTA dopamine projections to PFC; distinguishable from false-positive ALIC streamlines by immunostaining.
- **Posterior cingulate cortex / retrosplenial cortex** — long-distance target of dlPFC and DMN connectivity.
- **Default mode network (DMN)** — medial PFC and posterior cingulate core; rACC is a key anchor; anatomically grounded via tract tracing in marmosets and macaques.
- **Salience network (SN)** — dACC and frontoinsular cortex; anatomically supported by dACC–insula connections via the extreme capsule.

---

### Mechanistic insight

The paper does not fully meet the high bar. It provides anatomical data (tract tracing) that validates specific aspects of dMRI streamlines and rs-fMRI connectivity, and it proposes an algorithm (convergent streamline mapping) for identifying hub subregions. However, it does not provide neural recordings, pharmacology, or lesion data that specifically test a computational algorithm over alternatives at the level of neural activity.

The rACC hub study comes closest: it formalises a criterion (voxel with highest weighted sum of probabilistic streamlines from all seeded frontal areas) and validates it against tract-tracing anatomy in the same animals. Lesion studies referenced in the text (sulcal vs. gyral ACC lesions producing dissociable behavioral deficits) provide indirect support for the hub's integrative function, but these are cited rather than reported primary data. The paper therefore sits at the boundary: it advances the mechanistic understanding of how PFC circuits are organized, but does not map an algorithm onto measured neural activity with the specificity required for full mechanistic insight.

---

### Limitations & open questions

- All MRI methods measure undirected associations and cannot recover the directionality or quantitative density variation (many orders of magnitude in axonal projection strength) that tract tracing provides.
- dMRI tractography produces systematic false positives (documented here) and false negatives, especially at fiber crossings and for thin/unmyelinated fibers; the full extent of these errors for PFC connectivity is not yet catalogued.
- Morphometric similarity and structural covariance as proxies for monosynaptic connectivity rest on two-step interpretive assumptions that need further experimental validation.
- The relationship between rs-fMRI functional connectivity and monosynaptic anatomy is partially understood; indirect polysynaptic connections can sustain near-normal functional connectivity even after monosynaptic disconnection (as shown in callosotomy studies).
- PFC areal heterogeneity (e.g., vmPFC is not anatomically well-defined; different studies include different areas) complicates translation of imaging results to specific monosynaptic circuits.
- Individual variability in the absolute location of PFC fiber bundles limits voxel-wise translation, even if topographic organisation is conserved.
- The generative network models (wiring cost plus homophily) explain normative connectome topology, but their extension to disease connectomes requires further development.
- How connectivity-defined hubs relate to physiological function (single-unit activity, oscillations) and to the specific mechanisms of disease vulnerability remains an open question.

---

### Connections & keywords

- **Key citations**: Mesulam (1998) — transmodal hub theory; Raichle (2015) — default mode network; Fornito et al. (2016) — *Fundamentals of Brain Network Analysis*; Buckner et al. (2009) — cortical hubs and DMN; Crossley et al. (2014) — hubs implicated in brain disorders; Safadi et al. (2018) — ALIC functional segmentation; Tang et al. (2019) — rACC connectional hub; Jbabdi et al. (2013) — ventral PFC fibers, tracing vs. tractography; Haber & Behrens (2014) — incentive learning neural network.
- **Named models or frameworks**: graph theory connectomics; small-world networks; provincial vs. connector hub distinction (Sporns & Honey framework); generative network models (wiring cost + homophily); deep brain stimulation (DBS) targeting framework; Human Connectome Project (HCP).
- **Brain regions**: orbitofrontal cortex, anterior cingulate cortex (sACC, rACC, dACC), dorsolateral PFC, ventrolateral PFC, frontal pole, anterior limb of the internal capsule, medial forebrain bundle, default mode network, salience network, posterior cingulate cortex, ventral tegmental area, striatum.
- **Keywords**: prefrontal connectomics, monosynaptic connectivity, tract tracing, dMRI tractography, resting-state fMRI, graph theory hubs, connector hubs, white matter pathways, anterior limb internal capsule, deep brain stimulation, non-human primate, cross-species translation, network modules, participation coefficient, false-positive streamlines
