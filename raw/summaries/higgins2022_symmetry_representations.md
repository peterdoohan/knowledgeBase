---
source_file: higgins2022_symmetry_representations.md
title: Symmetry-Based Representations for Artificial and Biological General Intelligence
authors: Irina Higgins, Sébastien Racanière, Danilo Rezende
year: 2022
journal: Frontiers in Computational Neuroscience
paper_type: review
contribution_type: theoretical
---

### One-line summary

Symmetry transformations from physics, formalised via group theory, provide a principled framework for understanding what makes a "good" representation in both machine learning and the brain, with emerging neuroscience evidence suggesting the ventral visual stream learns such symmetry-based (equivariant/disentangled) representations.

---

### Background & motivation

A central question shared by neuroscience and machine learning is what form of representation best supports general intelligence — one that is data efficient, generalisable, and transferable across tasks. The dominant paradigm in both fields has favoured invariant representations (collapsing identity-preserving transformations), but these discard information potentially needed for diverse task learning. The authors argue this framing is wrong: intelligence evolved within physical constraints, and physics has shown that symmetry transformations — the "joints" of the world — are the key to discovering and categorising stable objects and properties. Bringing this symmetry-theoretic framework explicitly into representation learning may resolve the longstanding debate about what a good representation should look like.

---

### Methods

This is a narrative review covering three domains: physics/mathematics, machine learning, and neuroscience.

- **Scope**: Focuses primarily on vision, as the most studied sensory modality in both ML and neuroscience; RL applications of symmetry are acknowledged but largely set aside.
- **Mathematical framework introduced**: Group theory — formal definitions of groups, group actions, invariant maps, equivariant maps, discrete vs. continuous symmetries, and disentangled representations defined via group product decompositions.
- **ML literature surveyed**: Equivariant architectures (CNNs, GNNs, transformers), data augmentation approaches, disentangled representation learning (VAE-based methods including β-VAE), and symmetry-based approaches in scientific ML (protein folding, quantum chemistry).
- **Neuroscience literature surveyed**: Single-unit recordings in primate inferotemporal cortex (IT) and face patches (Chang & Tsao 2017; Kayaert et al. 2005; Higgins et al. 2021a); fMRI studies of the ventral stream; recordings from PFC, anterior cingulate cortex, and hippocampus (Bernardi et al. 2020); comparison of infant visual statistics with ML disentangling requirements.
- **Synthesis method**: Narrative review; no meta-analytic quantification.

---

### Key findings

For **reviews**, the major conclusions drawn across the literature:

- **Invariant vs. equivariant representations**: The historically dominant strategy of learning invariant representations (discarding transformation information) is problematic for general intelligence; equivariant representations, which preserve but reformat transformation information, are better suited to diverse task reuse.
- **Formal definition of disentanglement via symmetries**: A representation is disentangled with respect to a decomposition of a symmetry group into subgroups if it decomposes into independent subspaces each affected by exactly one subgroup. This grounds the intuitive "disentanglement" concept in group theory.
- **ML evidence**: Building symmetries into architecture (CNNs for translation, GNNs for permutation) yields substantially better data efficiency and generalisation than unstructured MLPs; explicit symmetry-based architectures outperform data augmentation alone.
- **Neuroscience evidence — IT cortex**: Single IT neurons in primate face patches show axis-aligned, factorised tuning (Chang & Tsao 2017): each cell is sensitive to one axis in face-space and insensitive to orthogonal dimensions — the hallmark of equivariant/disentangled coding.
- **Neuroscience evidence — direct ML/brain comparison**: Higgins et al. (2021a) showed strong one-to-one alignment between IT face-patch neurons and disentangled units from a β-VAE trained on the same stimuli; alignment was stronger than with supervised classifiers (invariant representations) or the generative model used in Chang & Tsao (2017); novel faces could be decoded from only 12 aligned neurons.
- **Neuroscience evidence — PFC and hippocampus**: Bernardi et al. (2020) found that dorsolateral PFC, anterior cingulate cortex, and hippocampus of primates, as well as RL-trained MLP final layers, exhibit "disentangled-like" geometry (high abstraction scores and high shattering dimensionality), even when not axis-aligned.
- **Developmental plausibility**: The smooth, single-object-dominated visual statistics of infant experience closely resemble the data distributions that enable ML disentangling, suggesting a common inductive constraint.
- **Key open disagreement**: Whether axis-aligned (strictly equivariant) or rotated (disentangled-like geometry) representations are the dominant form in the brain remains unresolved.

---

### Computational framework

**Group theory / symmetry-based representation learning.**

The core formalism treats the world as having a symmetry group G that acts on sensory inputs and on internal representations. Key quantities:

- **Groups and actions**: A group G is a set of invertible, composable transformations. G acts on input space X; representations should reflect this action structure.
- **Invariance**: A map F is invariant if F(g·x) = F(x) for all g ∈ G — transformation information is discarded.
- **Equivariance**: A map H is equivariant if H(g·x) = g·H(x) — the representation transforms in lockstep with the input transformation. Stacking equivariant maps followed by an invariant readout is the standard recipe.
- **Disentanglement (formal)**: Given a group G decomposed into commuting subgroups G = G₁ × G₂ × …, a representation is disentangled if it decomposes into independent subspaces where subspace i is affected only by Gᵢ. This makes transformation structure explicit and linearly readable.
- **Key assumption**: Natural tasks are constrained by physics; the symmetry group of the physical world therefore shapes which representations are useful, making physics-inspired representational principles applicable to biological and artificial intelligence.

---

### Prevailing model of the system under study

The paper's introduction identifies two prevailing models it pushes against:

1. **The invariant/"exemplar" model of visual representation**: The ventral visual stream was traditionally understood to progressively discard identity-preserving transformation information (Fukushima 1980; Tanaka 1996; Poggio & Bizzi 2004; Yamins et al. 2014). Higher areas collapse high-dimensional entangled manifolds into single points corresponding to object identities, yielding "exemplar" or "grandmother" neurons that fire maximally to a preferred stimulus and decrease monotonically with distance from that prototype. Deep classifiers trained on object recognition (Yamins & DiCarlo 2016) emerged as the main computational models of IT, reinforcing this view.

2. **The population-based, high-dimensional representation view**: Following advances in high-throughput recording and the success of large-scale deep learning, both neuroscience and ML shifted toward preferring opaque, high-dimensional, multiplexed representations that cannot be interpreted at the single-neuron level (Yuste 2015; Vaswani et al. 2017). Representation comparison methods (RSA, explained variance) were designed to be invariant to linear transformations, further obscuring any potential axis-aligned geometric structure.

Both views led to pessimism about single-neuron interpretability and about the possibility of discovering systematic representational structure at higher levels of the visual hierarchy.

---

### What this paper contributes

The review establishes the following updates to the prevailing model:

- **Conceptual reframing**: The invariant/exemplar account is insufficient for general intelligence. The field should adopt equivariant representations — not as an alternative to invariant output representations, but as the intermediate representational form from which invariant outputs can be derived as needed.
- **Formal grounding**: The paper provides the first accessible group-theoretic treatment aimed at neuroscientists, formally defining what "disentangled" representations are and why they are expected to be useful, linking the neuroscience concept of "untangling" (DiCarlo & Cox 2007) to the ML concept of "disentangling" (Bengio et al. 2013) via shared group-theoretic foundations.
- **Neural evidence synthesis**: Existing neuroscience data — particularly from IT face patches — are reinterpreted as consistent with equivariant/disentangled coding rather than exemplar coding, and recent direct comparisons between IT neurons and β-VAE units support this.
- **Methodological implication**: Standard representation comparison tools (RSA, explained variance) are insensitive to linear transformations and therefore blind to axis alignment, which is precisely the property that disentangled representations possess. The review identifies this as a reason why symmetry-based structure may have been systematically missed.
- **Unresolved question identified**: Whether symmetry-based representations arise from predictive coding / free energy minimisation, from multi-task supervised learning, or from some other learning pressure remains an open question.

---

### Brain regions & systems

- **Inferotemporal cortex (IT) / face patches** — primary focus; evidence that single neurons exhibit axis-aligned, factorised tuning consistent with equivariant/disentangled representations (Kayaert et al. 2005; Chang & Tsao 2017; Higgins et al. 2021a).
- **V1** — early visual processing stage; known to have factorised tuning to orientation and spatial frequency, and motion/direction (Hubel & Wiesel 1959; Grunewald & Skoumbourdis 2004), consistent with early-stage equivariant coding.
- **Dorsolateral prefrontal cortex (dlPFC)** — cited as exhibiting disentangled-like geometry in Bernardi et al. (2020); geometry correlated with task performance.
- **Anterior cingulate cortex (ACC)** — also found to exhibit disentangled-like geometry in Bernardi et al. (2020).
- **Hippocampus** — found to exhibit disentangled-like geometry (Bernardi et al. 2020); hypothesised as a site that benefits from symmetry-based factorised representations for supporting abstract cognitive maps and concept navigation (Behrens et al. 2018; Bellmund et al. 2018).

---

### Mechanistic insight

The paper does not meet the bar for this section. It is a review that synthesises existing findings rather than presenting a new algorithm with supporting neural data. The empirical results it cites (e.g., Chang & Tsao 2017; Higgins et al. 2021a; Bernardi et al. 2020) are consistent with equivariant/disentangled representations being present in the brain, but the review itself does not present a specific algorithm and directly test it against neural alternatives at the implementational level. The paper proposes symmetry-based equivariant coding as the computational-level answer to "what makes a good representation," and the cited ML and neuroscience evidence supports this framework at the algorithmic level, but no neural implementation (specific cell types, connectivity, neuromodulators) is addressed.

---

### Limitations & open questions

- **Unsupervised disentanglement is provably impossible without inductive biases** (Locatello et al. 2019): current VAE-based methods work through implicit data and optimisation biases rather than principled symmetry-based objectives; scaling to complex natural scenes remains an open challenge.
- **Axis-aligned vs. rotated geometry**: The review acknowledges that some evidence (Bernardi et al. 2020 and others) points to disentangled-like geometry that is not axis-aligned, while Higgins et al. (2021a) find strong axis alignment. Whether the brain uses strictly equivariant (axis-aligned) or more loosely disentangled-like codes is unresolved.
- **Learning mechanism**: Whether symmetry-based representations arise via predictive coding / free energy minimisation (which is compatible with generative disentangling models), via multi-task supervised learning (Johnston & Fusi 2021; Bernardi et al. 2020), or from other pressures is not established.
- **Scope limitation**: The review focuses on vision and largely omits RL and motor domains where symmetry principles may also apply.
- **Continuous symmetries**: Most ML methods approximate continuous symmetry groups by discrete subgroups; handling full continuous groups at scale remains a research frontier.
- **Cross-species generalisation**: Neural evidence cited is primarily from non-human primates; how well the framework applies to rodents and other species is unclear.
- **Population-level vs. single-neuron analysis**: The review identifies that RSA and related tools, dominant in systems neuroscience, are insensitive to axis alignment and therefore may have systematically missed equivariant structure; new tools are needed.

---

### Connections & keywords

**Key citations:**
- Chang & Tsao (2017) — axis-based coding in primate IT face patches
- Higgins et al. (2021a) — direct comparison of IT neurons and disentangled ML units
- Bernardi et al. (2020) — disentangled-like geometry in PFC and hippocampus
- Kayaert et al. (2005) — factorised shape tuning in IT
- Bengio et al. (2013) — disentangled representation learning review
- Locatello et al. (2019) — impossibility of unsupervised disentanglement
- Cohen & Welling (2016) — group equivariant convolutional networks
- DiCarlo & Cox (2007) — untangling invariant object recognition
- Yamins & DiCarlo (2016) — deep neural networks as models of ventral stream
- Bronstein et al. (2021) — geometric deep learning
- Higgins et al. (2019) — formal definition of disentangled representations via symmetries

**Named models or frameworks:**
- β-VAE (variational autoencoder for disentangled representation learning)
- Group equivariant CNNs (G-CNNs)
- Geometric deep learning
- Disentangled representation learning
- Predictive coding / free energy principle (Friston 2010)
- Representational Similarity Analysis (RSA)
- Noether's Theorem (physics grounding)

**Brain regions:**
- Inferotemporal cortex (IT) / face patches
- V1
- Dorsolateral prefrontal cortex (dlPFC)
- Anterior cingulate cortex (ACC)
- Hippocampus

**Keywords:**
- symmetry transformations
- group theory
- equivariant representations
- disentangled representations
- invariant representations
- ventral visual stream
- representation learning
- general intelligence
- convolutional neural networks
- variational autoencoder
- inferotemporal cortex
- geometric deep learning
