# Structural Form Discovery

## Current understanding

Structural form discovery is the problem of determining which structural form (tree, ring, order, clique, grid, etc.) best organizes a dataset, without pre-specifying the form. This is a higher-level learning problem than structure learning within a fixed form. A probabilistic hierarchical model using graph grammars can simultaneously discover the appropriate structural form and recover the specific instance of that form, mirroring the kind of structural discoveries made by scientists and children. The framework provides a third position in the nativism/empiricism debate: domain-specific structural constraints can be acquired through domain-general probabilistic inference over a structured hypothesis space.

## Key evidence

- On synthetic data with known ground-truth forms, the model correctly recovers the true underlying form in all tested cases ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Animal species (33 species, 106 features): best form is a tree; recovered subtrees correspond to taxonomic groupings (mammals, primates, rodents, birds, insects) ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- US Supreme Court votes (13 judges, 1,596 cases): best form is a chain (linear order) from liberal to conservative, consistent with the unidimensional hypothesis in political science ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Colour similarity (14 pure-wavelength hues): best form is a ring, corresponding to Newton's colour circle ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Face similarity (faces varying in masculinity and race): best form is a 2D grid recovering the two underlying dimensions ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- World city distances (35 cities): best form is a cylinder, with chain ≈ latitude and ring ≈ longitude ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Primate dominance (sooty mangabeys): best form is a linear order consistent with the dominance hierarchy identified by primatologists ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Bush administration interactions: best form is an undirected hierarchy matching the known organisational chart ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Prison friendships: best form is a partition (cliques), consistent with claims about social network structure ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Kula ring trade (20 New Guinea communities): best form is a ring, recovering the Kula exchange structure ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

- Developmental simulation: as feature count grows from 5 to 110, the model shifts from a partition to a tree of increasing resolution, qualitatively matching developmental transitions in children's categorisation ([Kemp 2008](../../raw/summaries/kemp2008_structural_discovery_form.md))

## History of ideas

Prior to this paper, structure learning in both machine learning and cognitive modelling operated with a fixed structural form. Clustering algorithms found partitions, hierarchical clustering found trees, dimensionality-reduction methods found spatial representations, and so on. The form had to be specified in advance. In cognitive development, the dominant framing was a tension between nativism (domain-specific constraints are innately given) and empiricism (generic learning mechanisms with no domain-specific representational commitments). Neither view offered a principled account of how a learner might discover which structural form is appropriate for a new domain. This paper established that form discovery can be formalised as Bayesian inference over a grammar-defined hypothesis space of forms, providing a third position between nativism and empiricism.

## Open questions

- The hypothesis space of eight forms, while broad, is not exhaustive; does not capture all cognitively natural or scientifically important forms
- The search algorithm is greedy and is not guaranteed to find the global MAP structure or form
- The parameter α (penalising many clusters) is fixed across all experiments; its sensitivity is not systematically explored
- The model assumes a fixed, pre-enumerated set of forms rather than generating new forms from first principles
- The framework does not currently handle compositional or mixed structures within a single dataset
- The connection to specific cognitive or neural mechanisms underlying form discovery is not addressed

## Related pages

- [Bayesian inference](bayesian_inference.md)
- [Cognitive development](../behaviours/cognitive_development.md)
- [Inductive inference](inductive_inference.md)
- [Knowledge representation](knowledge_representation.md)
- [Graph theory](graph_theory.md)
