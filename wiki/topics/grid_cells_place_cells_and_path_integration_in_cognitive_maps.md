---
title: "Grid cells, place cells, and path integration in cognitive maps"
subtopic_id: cognitive_maps__03
parent_topic_id: cognitive_maps
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:25:22.297731+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - whittington2020_tolman_eichenbaum_machine
  - baram2024_abstract_relational_map_consolidation
  - whittington2022_cognitive_map_nature
  - neupane2022_mental_navigation_entorhinal_cortex
  - whittington2023_disentanglement_constraints
core_papers:
  - baram2024_abstract_relational_map_consolidation
  - basu2023_goal_pointer_cognitive_map_ofc
  - farzanfar2023_cognitive_maps_spatial
  - neupane2022_mental_navigation_entorhinal_cortex
  - whittington2020_tolman_eichenbaum_machine
  - whittington2022_cognitive_map_nature
  - whittington2022_disentangling_biological
  - whittington2023_disentanglement_constraints
---

# Grid cells, place cells, and path integration in cognitive maps

The most defensible synthesis from this evidence set is that cognitive maps are not stored as a single unitary code. Instead, hippocampal-entorhinal computations appear partly factorized: entorhinal representations carry reusable structure and self-motion update signals useful for path integration, while hippocampal representations bind that structure to specific sensory episodes and contexts. This account is strongest for spatial navigation and internal position updating; extension to abstract relational knowledge is plausible and increasingly supported, but the evidence there is less direct and more model-dependent [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]].

## Current view

Grid cells are best treated here as a structural code, not the whole map. In current computational accounts, entorhinal grid-like representations provide a compact basis for transition structure and path integration, supporting generalization across environments with similar geometry or task structure [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]].

Place cells are the complementary, context-bound part of the system. In these models, hippocampal place-like units conjunctively bind structural location with local sensory content, producing environment-specific fields and remapping when those bindings change [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

Path integration is central because it updates latent position from self-motion when sensory input is absent or ambiguous. The strongest direct evidence in this set is that entorhinal neurons can express internally generated periodic structure during purely mental navigation, consistent with self-motion-based updating and continuous-attractor-like dynamics [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]].

A broader current view is that the same machinery may support non-spatial relational inference. But that claim rests mainly on computational unification and human fMRI generalization, not on direct cell-level evidence comparable to the spatial case [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].

## Strongest evidence

- **Endogenous entorhinal periodicity during mental navigation.** In monkeys navigating memorized landmark sequences without external sensory cues, 16% and 8.5% of entorhinal neurons showed significant periodic activity at the learned 0.65 s landmark interval. Periodicity was stronger during mental navigation than inter-trial intervals, dropped on error trials, and population coding of distance strengthened by the end of the navigation epoch. This is unusually direct evidence that entorhinal cortex can internally reconstruct structured progress through a learned space-like sequence [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]].

- **A mechanistic split between reusable structure and context-specific memory.** The Tolman-Eichenbaum Machine provides a concrete computational account in which entorhinal units represent structural regularities and hippocampal units represent conjunctive, remapping place-like codes. It reproduces grid-like periodicity, place-field remapping, and emergence of other entorhinal cell classes under different transition statistics. This is strong as unification, but still theoretical rather than biological proof [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

- **Path integration as a compressed representation of transitions.** The synthesis in [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]] makes an important computational point: path integration exploits relational constraints among transitions and therefore supports generalization better than storing every state-state relation explicitly. This is not a new experiment, but it organizes why grid-like codes are useful computationally and how they can complement sequence-based latent-state inference.

- **Human evidence for abstraction beyond concrete episodes.** Over days, medial prefrontal cortex develops cross-graph, stimulus-independent relational coding while medial temporal lobe retains concrete graph representations. This matters because it suggests hippocampal-entorhinal-style map computations may feed more abstract cortical maps after consolidation. Still, this is not direct evidence about place or grid cells per se, and the relevant RSA effects were mixed in strength [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].

- **Behavioral assay for vector-based navigation.** The honeycomb maze is notable because it isolates spatial choice structure and showed that hippocampal lesions impair learning by disrupting vector-based computations of goal direction. That strengthens the claim that hippocampal representations support more than simple cue-response behavior, though it does not directly identify grid or place cell mechanisms [[raw/summaries/wood2018_honeycomb_maze_spatial|Wood et al. 2018]].

## Landmark papers

[[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] is the clearest direct neural evidence in this set for internally generated, path-integration-like entorhinal dynamics. Its main value is showing structured periodic activity without external sensory scaffolding.

[[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] is the key unifying model for the grid/place division of labor. It gives a coherent explanation of why grid-like structure can remain stable across environments while hippocampal place-like codes remap.

[[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]] is the best synthesis paper here. It reframes the field around two linked problems: inferring latent state from sequences and updating state by path integration.

[[raw/summaries/wood2018_honeycomb_maze_spatial|Wood et al. 2018]] matters methodologically because it provides a clean behavioral task for testing vector-based navigation and hippocampal dependence.

## Boundaries and tensions

A major unresolved issue is what grid codes fundamentally represent. The attractor/path-integration view treats them as a metric for self-location updating; successor-style accounts treat them more as basis functions over transition structure; TEM-style accounts treat them as reusable structural knowledge. These are not fully equivalent, and this evidence set does not decisively choose among them [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]].

The evidence is asymmetric across levels of analysis. There is direct neural evidence for entorhinal periodic dynamics during mental navigation, but many broader claims about abstraction, remapping rules, and non-spatial generalization come from computational models or fMRI rather than single-unit causal tests [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].

Biological plausibility remains a live problem for the strongest unifying models. TEM explains a large range of phenomena, but relies on learning machinery such as backpropagation through time and variational inference, which are not established neural mechanisms [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

Theories of disentanglement help explain why different task factors might separate into grid-, border-, and object-related cell classes under biological constraints, but they do not explain the specific geometry of grid periodicity. They address factorization more than hexagonal structure [[raw/summaries/whittington2023_disentanglement_constraints|Whittington et al. 2023]].

The abstract-map extension is promising but should be kept in proportion. Human mPFC effects after consolidation show abstraction of graph structure, yet this is downstream from the classic hippocampal-entorhinal story and does not establish that the same code or mechanism underlies spatial grid/place responses and abstract relational maps [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].

## Open questions

- What is the neural source of the velocity or self-motion signal that drives entorhinal path integration during internally generated navigation? [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]]
- How is path integration gain calibrated and corrected when movement statistics change or landmarks are unreliable? The continuous-attractor account predicts such gain adjustments, but this remains under-tested in the cited evidence [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]].
- Which aspects of hippocampal remapping are random versus structure-preserving? TEM predicts non-random remapping tied to shared relational structure, but this prediction still needs sharper empirical tests [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].
- Can successor-representation, attractor, and latent-state-inference models be separated with cell-level data, rather than all fitting the same broad phenomena post hoc? [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]]
- How far does the grid/place/path-integration architecture generalize beyond physical space? Current evidence supports extension to abstract relational structure, but the strongest demonstrations remain indirect compared with spatial navigation [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].
- How do cortical abstract maps in mPFC emerge from hippocampal-entorhinal computations over consolidation, and what role do replay or sleep-dependent processes play? [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]]

## Key papers

- [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] — direct entorhinal single-unit evidence for internally generated periodic structure during mental navigation.
- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] — major unifying model of entorhinal structural codes plus hippocampal conjunctive/place-like memory.
- [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]] — best integrative review of path integration, latent-state inference, and predictive map models.
- [[raw/summaries/wood2018_honeycomb_maze_spatial|Wood et al. 2018]] — strong task-level evidence that hippocampal integrity is needed for vector-based navigation.
- [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]] — relevant for the extension from spatial hippocampal-entorhinal maps to abstract cortical relational maps after consolidation.
- [[raw/summaries/whittington2023_disentanglement_constraints|Whittington et al. 2023]] — theoretical account of why distinct functional cell types may emerge under biological constraints, with implications for grid/border/object-vector segregation.
- [[raw/summaries/wientjes2024_successor_representation|Wientjes et al. 2024]] — useful for the predictive-map angle, especially hierarchical abstraction, though less directly about grid/place physiology.

## Source papers
- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] | [[raw/mds/whittington2020_tolman_eichenbaum_machine|source md]]: The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation
- [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]] | [[raw/mds/baram2024_abstract_relational_map_consolidation|source md]]: An abstract relational map emerges in the human medial prefrontal cortex with consolidation
- [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]] | [[raw/mds/whittington2022_cognitive_map_nature|source md]]: How to build a cognitive map
- [[raw/summaries/neupane2022_mental_navigation_entorhinal_cortex|Neupane et al. 2022]] | [[raw/mds/neupane2022_mental_navigation_entorhinal_cortex|source md]]: Vector production via mental navigation in the entorhinal cortex
- [[raw/summaries/whittington2023_disentanglement_constraints|Whittington et al. 2023]] | [[raw/mds/whittington2023_disentanglement_constraints|source md]]: Disentanglement with Biological Constraints: A Theory of Functional Cell Types
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu and Ito 2023]] | [[raw/mds/basu2023_goal_pointer_cognitive_map_ofc|source md]]: A goal pointer for a cognitive map in the orbitofrontal cortex
- [[raw/summaries/farzanfar2023_cognitive_maps_spatial|Farzanfar et al. 2023]] | [[raw/mds/farzanfar2023_cognitive_maps_spatial|source md]]: From cognitive maps to spatial schemas
- [[raw/summaries/whittington2022_disentangling_biological|Whittington et al. 2022]] | [[raw/mds/whittington2022_disentangling_biological|source md]]: Disentangling with biological constraints: A theory of functional cell types
