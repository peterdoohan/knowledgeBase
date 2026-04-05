---
source_file: schneider2022_cebra_joint_embeddings.md
title: Learnable latent embeddings for joint behavioral and neural analysis
authors: Steffen Schneider, Jin Hwa Lee, Mackenzie Weygandt Mathis
year: 2022
journal: Nature (manuscript, Oct 6, 2022)
paper_type: computational
contribution_type: methodological
---

### One-line summary

CEBRA is a contrastive learning method that produces consistent, interpretable, and high-performance latent embeddings by jointly using behavioral and neural data for hypothesis- or discovery-driven neural population analysis.

### Background & motivation

Mapping behavioral actions to neural activity is a fundamental goal in neuroscience. As large-scale neural and behavioral recording capabilities increase, there is growing need for dimensionality reduction methods that can leverage joint behavior and neural data. Existing tools are either linear (e.g., PCA) which sacrifice performance for interpretability, or non-linear (e.g., UMAP, tSNE, pi-VAE) which lack consistency across animals/sessions or require restrictive generative model assumptions. There is a gap for non-linear techniques that yield consistent, interpretable embeddings while explicitly leveraging behavioral information.

### Methods

- **CEBRA framework**: Combines non-linear Independent Component Analysis (ICA) with contrastive learning (InfoNCE loss) to learn latent embeddings conditioned on behavior (auxiliary variables) and/or time
- **Sampling strategies**: Novel positive and negative pair sampling based on time offsets, continuous behavioral variables, or discrete categorical labels
- **Three training modes**:
  - *CEBRA-Behavior*: hypothesis-driven with behavioral labels
  - *CEBRA-Time*: discovery-driven with time-contrastive learning
  - *Hybrid*: combines both behavior and time labels
- **Multi-session training**: Joint training across animals/sessions to produce consistent embeddings invariant to subject ID or recording modality
- **Encoder architecture**: CNN-based neural networks with varying receptive fields (1, 10, or 40 time bins) depending on dataset sampling rate
- **Validation datasets**:
  - Synthetic spiking data with known ground-truth latents
  - Rat hippocampus (CA1) electrophysiology during linear track navigation
  - Primate somatosensory cortex (S1) during center-out reaching (active/passive)
  - Mouse visual cortex (V1, HVAs, PPC) with Neuropixels and 2-photon calcium imaging during natural movie viewing

### Key findings

- **Superior reconstruction**: CEBRA-Behavior significantly outperformed pi-VAE, tSNE, and UMAP at reconstructing ground-truth synthetic latents (one-way ANOVA, F(3, 396)=278.31, p=3.95e-97)
- **Consistency across subjects**: CEBRA-Behavior produced significantly more consistent embeddings across rats compared to conv-pi-VAE with or without labels (one-way ANOVA F(5, 67)=28, p=3.4×10^-15)
- **Hippocampal decoding**: Achieved ~5 cm median absolute error for position decoding (vs. 12 cm reported for pi-VAE), with R² of 73.35% for position+direction labels vs. -49.90% with shuffled labels
- **Topological analysis**: CEBRA embeddings of hippocampal data revealed ring topology (Betti numbers 1,1,0) consistent with linear track place cells, confirmed via persistent co-homology
- **Multi-session benefits**: Joint training across animals increased consistency without sacrificing decoding performance; pretrained models adapted to new sessions in milliseconds (50-100 steps/second)
- **Primate S1 encoding**: Active vs. passive movements produced distinct embedding trajectories (start/stop vs. continuous); position information was more robustly encoded than direction
- **Cross-modality consistency**: CEBRA produced highly consistent embeddings from both Neuropixels (spiking) and 2-photon calcium imaging of mouse visual cortex when trained with DINO movie features as labels
- **Natural movie decoding**: Achieved >95% frame decoding accuracy (within 1-second window) from V1 activity using joint multi-modality training, significantly outperforming baseline kNN and naive Bayes decoders (one-way ANOVA, F(3,197)=5.88, p=0.0007)
- **Layer-specific decoding**: V1 layers 2/3 and 5/6 showed significantly higher decoding performance than layer 4 (one-way ANOVA, F(2,12)=9.88, p=0.003), suggesting non-thalamic input layers make frame information more explicit

### Computational framework

**Contrastive learning with InfoNCE loss**: CEBRA extends standard InfoNCE contrastive learning by introducing flexible sampling strategies for positive and negative pairs based on time, behavior, or auxiliary variables. The objective optimizes a neural network encoder f that maps neural activity to an embedding space, using similarity measure φ (typically dot-product on normalized features or negative MSE). The key innovation is the systematic design of positive pair distribution p and negative pair distribution q to shape the embedding geometry based on scientific questions—enabling hypothesis-driven (behavior-guided), discovery-driven (time-only), or hybrid analysis modes.

### Prevailing model of the system under study

Prior to CEBRA, the field relied on linear dimensionality reduction methods (PCA, dPCA) for interpretability, or non-linear methods (UMAP, tSNE, pi-VAE) for performance. Linear methods were preferred when interpretability and cross-subject consistency were needed, but they sacrificed decoding performance. Non-linear methods like pi-VAE provided better decoding but relied on explicit generative models with restrictive assumptions about data statistics, and did not guarantee consistent embeddings across animals or repeated algorithm runs. UMAP and tSNE were widely used for visualization but lacked the ability to explicitly use time information and were inconsistent across concatenated data from different animals due to batch effects. The prevailing assumption was that there was a trade-off between performance, interpretability, and consistency that could not be simultaneously optimized.

### What this paper contributes

CEBRA breaks the trade-off between performance, interpretability, and consistency in neural dimensionality reduction. The method introduces a theoretically-grounded contrastive learning framework that:

1. **Achieves state-of-the-art decoding performance**: Outperforms pi-VAE, UMAP, tSNE, and PCA on synthetic and real neural datasets across species (rats, primates, mice) and recording modalities (electrophysiology, calcium imaging)

2. **Provides theoretical guarantees for consistency**: Leverages non-linear ICA theory to prove linear identifiability—embeddings from different runs, subjects, or sessions are guaranteed to be consistent up to a linear transformation, enabling cross-subject and cross-session analysis

3. **Enables flexible hypothesis- and discovery-driven analysis**: Three training modes (behavior-guided, time-contrastive, hybrid) allow users to test specific hypotheses about neural encoding or discover structure without prior assumptions

4. **Solves the cross-modality consistency problem**: Demonstrates that joint training produces consistent embeddings across radically different recording methods (Neuropixels spiking vs. 2-photon calcium imaging), enabling "pseudo-mouse" models that generalize across modalities

5. **Provides principled model selection**: InfoNCE loss value serves as a goodness-of-fit metric for comparing hypotheses and selecting models, with topological analysis (persistent co-homology) providing additional validation of embedding structure

6. **Enables real-time adaptive decoding**: Pretrained models can adapt to new subjects in milliseconds, making the method suitable for brain-machine interface applications

### Brain regions & systems

- **Hippocampus (CA1)**: Rat hippocampal place cells during linear track navigation; used to demonstrate consistent spatial encoding across animals and topology of place cell representations
- **Primary somatosensory cortex (S1, Area 2)**: Primate S1 during active and passive reaching movements; used to dissociate active vs. passive encoding and demonstrate robust kinematic representations
- **Primary visual cortex (V1)**: Mouse V1 recorded with both Neuropixels and 2-photon calcium imaging during natural movie viewing; used to demonstrate cross-modality consistency and frame-by-frame decoding
- **Higher visual areas (HVAs)**: Mouse visual areas VISl, VISal, VISam, VISpm; used to demonstrate area-specific consistency and decoding performance differences
- **Posterior parietal cortex (PPC/VISrl)**: Mouse PPC-like area; showed lower decoding performance compared to V1, consistent with known functional hierarchies

### Mechanistic insight

The paper provides a strong algorithmic foundation with theoretical guarantees but does not directly map algorithmic components to specific neural circuits or biophysical mechanisms. The core contribution is at the **algorithmic level** of Marr's hierarchy:

**Computational**: The brain must map high-dimensional neural activity to behaviorally-relevant latent representations that are consistent across time, subjects, and recording conditions. The problem is to find low-dimensional embeddings that preserve behavioral relevance while being identifiable (recoverable up to linear transformations).

**Algorithmic**: CEBRA implements this through contrastive learning with InfoNCE loss, where the key algorithmic components are:
- Encoder neural network (CNN or MLP) that maps neural activity to embedding space
- Positive pair sampling based on time proximity or behavioral similarity
- Negative pair sampling for contrastive discrimination
- Similarity measure (dot-product on hypersphere or negative MSE in Euclidean space)

The theoretical contribution proves that under diversity conditions (sufficient variability in latent space), the learned embeddings are identifiable up to linear transformations—ensuring consistency across runs, subjects, and modalities.

**Implementational**: The paper does not specify particular cell types, connectivity patterns, or biophysical mechanisms. However, the results suggest that neural population codes in different brain regions (hippocampus, S1, V1) are amenable to the same dimensionality reduction framework, and that cross-modality consistency (spikes vs. calcium) implies that both recording methods capture the same underlying latent dynamics. The finding that layer 2/3 and 5/6 of V1 decode movie frames better than layer 4 hints at feedback/recurrent processing for visual prediction, but this is not mechanistically elaborated.

### Limitations & open questions

- **Gap between latent spaces and neural computations**: While CEBRA provides consistent latent embeddings, how these map to specific neural-level computations (e.g., synaptic plasticity, circuit dynamics) remains unclear
- **Dependence on auxiliary variables**: Hypothesis-driven mode requires choosing appropriate behavioral labels; incorrect hypotheses lead to poor embeddings (as shown by shuffled label controls)
- **Limited biological validation**: The method is validated on decoding performance and consistency metrics, but not against ground-truth biological mechanisms (e.g., known synaptic connectivity, identified cell types)
- **Computational cost**: Training requires GPU resources for large datasets; while faster than pi-VAE, scaling to very large neural populations (10,000+ neurons) presents engineering challenges
- **Temporal dynamics**: While time-contrastive learning captures temporal structure, the framework does not explicitly model dynamics (e.g., attractor states, recurrent connectivity) that might be important for understanding neural computation
- **Cross-species generalization**: While demonstrated across rats, primates, and mice, the method has not been validated on other model organisms (e.g., songbirds, zebrafish) or human neural data

### Connections & keywords

**Key citations:**
- Zhou & Wei (2020) - pi-VAE, the primary benchmark comparison
- Grosmark & Buzsáki (2016) - rat hippocampus dataset
- Chowdhury et al. (2020) - primate somatosensory cortex dataset
- de Vries et al. (2020), Siegle et al. (2021) - Allen Institute visual cortex datasets
- Hyvärinen et al. (2019) - non-linear ICA using auxiliary variables
- Oord et al. (2018) - contrastive predictive coding
- Wang & Isola (2020) - alignment and uniformity on hypersphere
- Zimmermann et al. (2021) - contrastive learning inverts data generating process

**Named models or frameworks:**
- CEBRA (Consistent Embeddings of high-dimensional Recordings using Auxiliary variables)
- InfoNCE (contrastive loss function)
- pi-VAE / conv-pi-VAE (benchmark comparison)
- UMAP, tSNE, PCA (baseline methods)
- DINO (vision transformer for video feature extraction)
- Persistent co-homology (topological validation)
- k-Nearest Neighbors (kNN) decoder

**Brain regions:**
- Hippocampus (CA1, place cells)
- Primary somatosensory cortex (S1, Area 2)
- Primary visual cortex (V1, VISp)
- Higher visual areas (HVAs: VISl, VISal, VISam, VISpm)
- Posterior parietal cortex (PPC/VISrl)

**Keywords:**
- contrastive learning
- dimensionality reduction
- neural embeddings
- representation learning
- self-supervised learning
- InfoNCE loss
- cross-modal consistency
- latent variable models
- brain-machine interfaces
- population coding
- place cells
- visual cortex
- somatosensory cortex
- topology
- identifiability
