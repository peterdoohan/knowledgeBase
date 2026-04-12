---
source_file: "kemp2008_structural_discovery_form.md"
paper_id: "kemp2008_structural_discovery_form"
title: "The discovery of structural form"
authors: "Charles Kemp, Joshua B. Tenenbaum"
year: 2008
journal: "Proceedings of the National Academy of Sciences (PNAS)"
paper_type: "computational"
contribution_type: "theoretical"
frameworks: ["bayesian_inference", "structural_form_discovery"]
keywords: ["discovery", "structural", "form"]
---

### One-line summary

A probabilistic hierarchical model using graph grammars can simultaneously discover which structural form (tree, ring, order, clique, grid, etc.) best organises a dataset and recover the specific instance of that form, mirroring the kind of structural discoveries made by scientists and developing children.

---

### Background & motivation

Most structure-learning algorithms solve only a lower-level problem: given a pre-specified structural form (e.g. tree, low-dimensional space, partition), find the best instance of that form. But scientists and children routinely solve a higher-level problem — discovering which form is appropriate in the first place (e.g. Linnaeus recognising that species are tree-structured, Mendeleev recognising periodicity in the elements). Standard algorithms cannot perform this form discovery because the form must be fixed in advance. The paper addresses this gap by asking whether form discovery can be formalised as probabilistic inference over a space of structural forms.

---

### Methods

- **Model architecture**: A hierarchical generative model that jointly infers the structural form F and the structure S maximising the posterior P(S, F | D) = P(D | S) P(S | F) P(F).
- **Hypothesis space**: Eight structural forms (partition, chain, order, ring, hierarchy, tree, grid, cylinder) represented as node-replacement graph grammars. Complex forms (grid, cylinder) are combinations of simpler grammars. A uniform prior P(F) is placed over forms.
- **Structure prior P(S | F)**: Favours graphs with fewer clusters (penalises complexity); normalising constant ensures simpler forms are preferred when they suffice.
- **Likelihood P(D | S)**: For feature data, assumes features are generated from a multivariate Gaussian whose covariance encourages smooth variation over the graph. Extended to relational/frequency data by defining P(D | S) as high when large entries in the data matrix correspond to edges in S.
- **Search**: Greedy search per candidate form, starting with all entities in one cluster and iteratively splitting using the form's grammar production, followed by local improvement moves (entity reassignment, cluster swapping).
- **Validation**: Synthetic data with known ground-truth forms; multiple real-world datasets covering biological features, Supreme Court votes, colour similarity, face similarity, world city distances, primate dominance, organisational interactions, prison friendships, and Kula ring trade relations.
- **Developmental simulation**: Varied the number of observed animal features (5, 20, 110) to simulate how inferred form changes as data accumulates.

---

### Key findings

- On synthetic data, the model correctly recovers the true underlying form in all tested cases.
- Animal species (33 species, 106 features): best form is a tree; recovered subtrees correspond to taxonomic groupings (mammals, primates, rodents, birds, insects).
- US Supreme Court votes (13 judges, 1,596 cases): best form is a chain (linear order) from liberal to conservative, consistent with the unidimensional hypothesis in political science.
- Colour similarity (14 pure-wavelength hues): best form is a ring, corresponding to Newton's colour circle.
- Face similarity (faces varying in masculinity and race): best form is a 2D grid recovering the two underlying dimensions.
- World city distances (35 cities): best form is a cylinder, with chain ≈ latitude and ring ≈ longitude.
- Primate dominance (sooty mangabeys): best form is a linear order consistent with the dominance hierarchy identified by primatologists.
- Bush administration interactions: best form is an undirected hierarchy matching the known organisational chart.
- Prison friendships: best form is a partition (cliques), consistent with claims about social network structure.
- Kula ring trade (20 New Guinea communities): best form is a ring, recovering the Kula exchange structure.
- Developmental simulation: as feature count grows from 5 to 110, the model shifts from a partition to a tree of increasing resolution, qualitatively matching developmental transitions in children's categorisation.

---

### Computational framework

**Bayesian inference over graph grammars.** The paper uses a hierarchical generative model in which:

- The structural form F is drawn from a uniform prior over a grammar-defined hypothesis space.
- The structure S (a cluster graph) is drawn from P(S | F), which encodes form compatibility and a complexity penalty.
- The data D are generated from P(D | S), which rewards smooth variation of features (or concentrated relational ties) over the graph.

Inference targets the joint MAP estimate of (S, F). The core assumption is that cognitively natural structural forms are those generatable by simple context-free node-replacement productions — a metagrammar principle. Feature smoothness over graphs is formalised via a multivariate Gaussian whose covariance is derived from graph structure.

---

### Prevailing model of the system under study

Prior to this paper, structure learning in both machine learning and cognitive modelling operated with a fixed structural form. Clustering algorithms found partitions, hierarchical clustering found trees, dimensionality-reduction methods found spatial representations, and so on. The form had to be specified in advance. In cognitive development, the dominant framing was a tension between nativism (domain-specific constraints are innately given) and empiricism (generic learning mechanisms with no domain-specific representational commitments). Neither view offered a principled account of how a learner might discover which structural form is appropriate for a new domain. The paper's introduction frames this as a critical limitation shared by computational tools and theories of cognitive development alike.

---

### What this paper contributes

The paper establishes that form discovery — the qualitative leap of recognising that a domain has tree-structure, ring-structure, or clique-structure — can be formalised as Bayesian inference over a grammar-defined hypothesis space of forms. Concretely:

- It provides a single algorithm that, without pre-specifying the form, recovers the correct structural form across a diverse range of real-world and synthetic datasets.
- It offers a third position in the nativism/empiricism debate: domain-specific structural constraints need be neither innate nor absent; they can be acquired through domain-general probabilistic inference over a structured hypothesis space.
- It provides a computational account of developmental transitions in structural understanding (e.g. partition → tree as more data accumulate), consistent with the order in which children acquire hierarchical category structure and transitive ordering.
- It points toward a "Universal Structure Grammar" as a long-term research goal — a metagrammar generating all and only the cognitively natural structural forms.

---

### Brain regions & systems

Not applicable. The paper is a computational and behavioural modelling study with no anatomical or neural focus. The level of analysis is computational/algorithmic — it addresses the representations and inference procedures a learner uses to discover relational structure, without committing to a neural implementation.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It proposes an algorithm for structure discovery and demonstrates that it fits a range of human and real-world data, but provides no neural data (recordings, imaging, lesion, pharmacology) linking the model's specific variables (e.g. posterior probabilities over forms, cluster assignments) to measured neural activity. The contribution is a computational-level theory of what problem is being solved (form discovery) and an algorithmic proposal for how it is solved (Bayesian inference over graph grammars), without addressing the implementational level.

---

### Limitations & open questions

- The hypothesis space of eight forms, while broad, is not exhaustive; the authors acknowledge it does not capture all cognitively natural or scientifically important forms.
- The search algorithm is greedy and is not guaranteed to find the global MAP structure or form; exact inference is intractable.
- The parameter α (penalising many clusters) is fixed across all experiments; its sensitivity is not systematically explored.
- The model assumes a fixed, pre-enumerated set of forms rather than generating new forms from first principles; the proposed metagrammar is sketched but not fully developed or tested.
- The framework does not currently handle compositional or mixed structures within a single dataset (e.g. a domain that is partially hierarchical and partially ring-structured at different levels).
- The developmental simulation varies only the number of features, not the number of entities or the noisiness of data; broader developmental modelling remains to be done.
- The connection to specific cognitive or neural mechanisms underlying form discovery is not addressed.

---

### Connections & keywords

**Key citations**:
- Inhelder & Piaget (1964) — The Early Growth of Logic in the Child; foundational claim that classification (tree) and seriation (order) are elementary logical structures.
- Carey (1985) — Conceptual Change in Childhood; background on structural discovery in cognitive development.
- Kuhn (1970) — The Structure of Scientific Revolutions; motivation for form discovery as a paradigm-shifting activity.
- Tenenbaum, Griffiths & Kemp (2006) — Theory-based Bayesian models of inductive learning; precursor framework.
- Shepard (1980) — Multidimensional scaling, tree-fitting and clustering; taxonomy of structural forms in psychology.
- Girvan & Newman (2002) — Community structure in social and biological networks; comparison point for clique/partition models.
- Rogers & McClelland (2004) — Semantic Cognition (PDP approach); empiricist alternative.

**Named models or frameworks**:
- Graph grammars (node-replacement graph grammars)
- Hierarchical generative model / Bayesian hierarchical model
- Universal Structure Grammar (proposed goal)
- Multidimensional scaling (MDS), hierarchical clustering, PCA — prior methods contrasted against

**Brain regions**: Not applicable.

**Keywords**: structural form discovery, graph grammars, Bayesian structure learning, hierarchical generative model, unsupervised learning, cognitive development, inductive inference, knowledge representation, relational structure, partitions, trees, rings, orders, domain-general learning
