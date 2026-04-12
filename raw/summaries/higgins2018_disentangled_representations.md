---
source_file: higgins2018_disentangled_representations.md
paper_id: higgins2018_disentangled_representations
title: "Towards a Definition of Disentangled Representations"
authors:
  - "Irina Higgins"
  - "David Amos"
  - "David Pfau"
  - "Sebastien Racaniere"
  - "Loic Matthey"
  - "Danilo Rezende"
  - "Alexander Lerchner"
year: 2018
journal: "arXiv preprint (December 2018)"
paper_type: computational
contribution_type: theoretical
keywords:
  - disentangled_representations
  - group_theory
  - representation_theory
  - symmetry_transformations
  - equivariant_maps
  - latent_variable_models
  - variational_autoencoders
  - irreducible_representations
  - direct_product_decomposition
  - data_generative_factors
  - unsupervised_representation_learning
  - active_perception
  - towards
  - definition
  - disentangled
  - representations
---

### One-line summary

This paper proposes the first formal definition of disentangled representations by grounding the concept in group and representation theory: a representation is disentangled if it decomposes into independent subspaces, each transformed exclusively by a distinct subgroup of the world's symmetry group.

---

### Background & motivation

Disentangled representation learning has been motivated by the hypothesis that separating the independent factors of variation in data improves data efficiency and generalisation in intelligent agents. However, there was no agreed-upon formal definition of "disentangling", making it difficult to evaluate models, compare metrics, or measure progress. In particular, the notion of "data generative factors" remained ill-defined outside of toy datasets with known ground truth. This paper attempts to bridge this gap by importing the mathematics of symmetry transformations — already deeply productive in physics via Noether's Theorem and group theory — into the representation learning setting.

---

### Methods

This is a purely theoretical/computational paper with no empirical data collection; methods consist of mathematical formalisation and a single illustrative model demonstration.

- **Conceptual grounding**: The paper identifies world symmetry transformations (actions that change some properties of world state while leaving others invariant) as the appropriate formalisation of "structure" underlying disentanglement.
- **Group-theoretic formalism**: Uses group theory (groups, subgroups, direct products, group actions on sets) and group representation theory (linear group representations, irreducible representations, direct sums, tensor products) to define disentangled representations formally.
- **Equivariant mapping**: Formalises the inference process as a composition f: W → Z (world states to representation vector space) and requires this map to be a G-morphism (equivariant) between the group action on world states and the group action on representations.
- **Two definitions**: (1) *Disentangled representation* — the action of G on Z decomposes into independent subspace actions, each governed by a single subgroup Gi; (2) *Linear disentangled representation* — the additional constraint that the subgroup actions on their respective subspaces are linear (group representations).
- **Worked examples**: A grid world (cyclic groups for x/y translation and colour) illustrates both definitions. CCI-VAE is trained on grid world data to show the learned latent space approximately satisfies equivariance.
- **Backward compatibility analysis**: The new definition is compared against three previously proposed desiderata — modularity, compactness, and explicitness — to show where it agrees and where it provides principled resolution to prior disagreements.

---

### Key findings

- A representation is disentangled with respect to a particular decomposition G = G1 × ... × Gn if the representation vector space Z decomposes into independent subspaces Z1, ..., Zn such that each Zi is affected only by Gi and left invariant by all other subgroups.
- The definition requires the symmetry group to admit a direct product decomposition into subgroups; factors that do not commute (e.g. 3D rotations, SO(3)) cannot be disentangled by this definition — SO(3) is not a direct product, so rotations about x, y, z axes cannot be treated as independently disentangled factors.
- Each disentangled subspace can be *multi-dimensional*, resolving a long-standing debate: compactness (one factor = one latent dimension) is not required.
- The group action need not be linear for basic disentanglement; linearity is an additional, stronger constraint that defines *linear disentangled representations*, encoded via irreducible representations in each subspace.
- A single dataset can have multiple valid disentangled representations corresponding to different group decompositions (e.g. {x, y, colour} vs {position, colour}); the "natural" decomposition is not uniquely determined by the formalism alone and requires additional inductive bias (e.g. active perception).
- Unsupervised learning of disentangled representations is impossible without inductive biases (consistent with Locatello et al. 2018); active perception or causal manipulation is identified as a path to discovering natural group decompositions.
- CCI-VAE trained on the grid world learns a latent representation that approximately satisfies the equivariance condition, though it loses the cyclic structure and the group action is non-linear in the learned space.

---

### Computational framework

**Group theory and representation theory** (mathematics/physics-inspired).

The paper models the structure of the world as a symmetry group G acting on a set of world states W. The core formalism:

- **World states W**: abstract set of states.
- **Symmetry group G**: set of transformations that leave object identity invariant, with binary composition operator; decomposes as direct product G = G1 × ... × Gn.
- **Generative process b: W → O**: maps world states to observations (e.g. pixel images).
- **Inference process h: O → Z**: maps observations to the agent's representation vector space Z.
- **Composition f = h ∘ b: W → Z**: the combined mapping from world states to representations.
- **Equivariance condition**: f must be a G-morphism satisfying f(g · w) = g · f(w), ensuring the group action structure of W is preserved in Z.
- **Disentangled group action**: the action of G on Z is disentangled if Z = Z1 ⊕ ... ⊕ Zn such that Gi acts only on Zi and all other Gj (j ≠ i) leave Zi fixed.
- **Linear disentangled representations**: the group action on Z is additionally required to be linear (a group representation ρ: G → GL(Z)), decomposing into irreducible representations one per subgroup.

Key assumption: the symmetry group decomposes naturally as a direct product of independent subgroups, and this decomposition is given (learning it is left to future work).

---

### Prevailing model of the system under study

The paper is not a neuroscience paper; it addresses the field of disentangled representation learning in machine learning. The prevailing landscape as characterised in the introduction:

Prior to this work, the field operated with an informal, intuition-driven understanding of disentangled representations, often described in terms of "data generative factors". There was no consensus on: (1) what constitutes a generative factor; (2) whether each factor should occupy one or many latent dimensions (compactness); (3) whether the representation must have a unique basis up to axis permutation; (4) whether each factor must be linearly decodable (explicitness). Prominent approaches included β-VAE and InfoGAN, along with several metrics (e.g. Eastwood & Williams 2018, Kim & Mnih 2018, Ridgeway & Mozer 2018) each operationalising different combinations of modularity, compactness, and explicitness. The connection between symmetry/group theory and disentangling had been gestured at but never formalised into a definition.

---

### What this paper contributes

The paper provides the first principled, formal definition of disentangled representations, resolving several prior disagreements:

- **Replaces "generative factors" with group-theoretic symmetry subgroups**, giving a mathematically precise referent for what it means to disentangle.
- **Resolves the compactness debate**: subspaces can be multi-dimensional; a single factor of variation may require a multi-dimensional subspace (e.g. colour in RGB vs. hue), and this is legitimate under the definition.
- **Resolves the uniqueness/basis debate**: any basis within a subspace is acceptable; the definition does not privilege a particular axis alignment.
- **Principled exclusion of non-disentanglable cases**: 3D rotations cannot be disentangled into per-axis rotations under this definition, because SO(3) is not a direct product — a result that matches the mathematical structure rather than intuition.
- **Introduces linear disentangled representations** as a stronger variant where group actions are required to be linear, connecting to the Maschke/irreducibility decomposition machinery.
- **Clarifies the role of active perception**: natural group decompositions may need to be discovered through causal manipulation of the world, not just from static i.i.d. data.

---

### Brain regions & systems

Not applicable. This is a purely theoretical machine learning paper with no anatomical or neural focus. The level of analysis is computational/representational: what properties a learned latent representation must have to count as disentangled, independent of any particular neural substrate.

---

### Mechanistic insight

The paper does not meet the bar for this section. It is a theoretical contribution that does not provide neural data (recordings, imaging, lesion, pharmacology) of any kind. There are no experimental subjects, no neural measurements, and no algorithm-versus-alternative comparison using empirical neural evidence. The one model demonstration (CCI-VAE on a grid world) is purely illustrative and validates approximate equivariance qualitatively, but does not provide mechanistic evidence linking any specific computational algorithm to measured neural activity or implementation.

---

### Limitations & open questions

- **Group decomposition is assumed, not learned**: the formalism requires a natural decomposition G = G1 × ... × Gn to be given; how to discover this decomposition from data (especially non-i.i.d. data from active perception) is left entirely to future work.
- **Linearity of learned group actions**: the worked CCI-VAE example shows that even a state-of-the-art model learns only an approximate, non-linear equivariant mapping; the gap between the formal definition and what is actually achievable by learning algorithms is not addressed.
- **Cyclic structure loss**: the learned representation loses the cyclic (periodic) structure of the true group action, a failure mode that is noted but not resolved.
- **Non-invertible generative processes**: the formalism handles injective f cleanly but the case where different world states map to identical observations (e.g. occlusion) requires active sensing to restore invertibility — this is acknowledged but not developed.
- **Multiple valid decompositions**: the framework provides no criterion for selecting among the many possible group decompositions of a given symmetry group; "natural" decompositions are identified informally with active perception but no algorithm is provided.
- **Continuous vs. discrete groups**: the paper focuses on discrete cyclic groups for worked examples; extension to continuous Lie groups (e.g. SO(3) for full 3D rotation) is noted but not fully worked out.
- **No learning algorithm**: the paper explicitly does not provide a recipe for learning disentangled representations; it only defines what the target is.

---

### Connections & keywords

**Key citations**:
- Higgins et al. 2017 (β-VAE) — foundational disentangling model built upon
- Burgess et al. 2017 (CCI-VAE) — the model demonstrated in the worked example
- Locatello et al. 2018 — proves impossibility of unsupervised disentangling without inductive bias
- Kim & Mnih 2018 (FactorVAE) — contemporary disentangling approach compared against
- Eastwood & Williams 2018 — disentanglement metric framework (modularity/compactness/explicitness)
- Ridgeway & Mozer 2018 — f-statistic disentanglement metric
- Soatto 2010 — actionable information and active perception theory
- Cohen & Welling 2014/2015 — learning irreducible representations; equivariant networks
- Noether 1915 — theoretical inspiration from physics symmetry conservation laws

**Named models or frameworks**:
- β-VAE
- CCI-VAE (Constrained Capacity Increase VAE)
- InfoGAN
- Group equivariant convolutional networks (Cohen & Welling 2016)
- Actionable information theory (Soatto)
- Modularity / compactness / explicitness framework (Eastwood & Williams)

**Brain regions**: Not applicable.

**Keywords**: disentangled representations, group theory, representation theory, symmetry transformations, equivariant maps, latent variable models, variational autoencoders, irreducible representations, direct product decomposition, data generative factors, unsupervised representation learning, active perception
