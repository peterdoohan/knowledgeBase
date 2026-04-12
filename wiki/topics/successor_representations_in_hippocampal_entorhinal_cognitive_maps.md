---
title: "Successor representations in hippocampal-entorhinal cognitive maps"
subtopic_id: schemas_and_generalization__03
parent_topic_id: schemas_and_generalization
page_type: topic
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:27:32.034891+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - wikenheiser2016_cognitive_maps_hippocampus
  - barron2020_neuronal_computation_inferential
  - whittington2024_build_cognitive_map
  - whittington2022_cognitive_map_review
  - baram2024_abstract_relational_map_consolidation
core_papers:
  - akam2021_dopamine_model_based_rl
  - baram2024_abstract_relational_map_consolidation
  - barron2020_neuronal_computation_inferential
  - whittington2022_cognitive_map_nature
  - whittington2022_cognitive_map_review
  - whittington2022_cognitive_maps_learning
  - whittington2024_build_cognitive_map
  - wikenheiser2016_cognitive_maps_hippocampus
---

# Successor representations in hippocampal-entorhinal cognitive maps

The useful claim here is narrow: hippocampal-entorhinal “cognitive maps” often look more like predictive maps of future states than static sensory maps, and the successor representation (SR) gives a compact reinforcement-learning formalism for that idea. But the evidence is stronger for *SR-like* computation than for a literal one-to-one implementation of vanilla SR in place cells or grid cells. Current synthesis papers increasingly treat SR as one component in a broader family of map-building mechanisms that also includes path integration, attractor dynamics, latent-state inference, replay, and cortical abstraction [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

## Current view

SR remains a productive bridge between reinforcement learning and hippocampal map theories because it formalizes a representation of each state in terms of its expected future occupancy under the current transition structure and policy. That matches the intuition that hippocampal maps support prediction, planning, and generalization, not just localization.

Within current hippocampal-entorhinal modeling, however, SR is not the whole story. Reviews now place SR alongside:
- latent-state sequence models for disambiguating aliased observations,
- entorhinal path-integration and continuous-attractor accounts for grid-like structure,
- compositional/factorized schemes that support transfer across environments,
- hippocampal replay and prospective sequence generation during inference [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

A practical synthesis is:
- hippocampus can rapidly learn environment- or task-specific relational structure;
- entorhinal/path-integration-like codes provide compressed, reusable structure;
- prefrontal regions acquire more abstract relational maps with experience or consolidation [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].

So the field’s center of gravity has moved from “hippocampus implements SR” to “SR captures an important predictive aspect of cognitive maps, but biological maps likely combine SR-like prediction with non-SR mechanisms.”

## Strongest evidence

The strongest support is indirect but convergent.

Hippocampal activity is prospective, sequential, and causally relevant for inference. In humans and mice, hippocampus expresses a prospective code for the intermediate associated cue during inference, preserves learned temporal order in ensemble spiking, and dCA1 silencing impairs inference without disrupting simpler learned discriminations [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]]. This is strong evidence for predictive relational computation, though not a unique signature of SR.

Offline hippocampal replay appears to incorporate inferred structure, not just replay experienced pairs. During rest, sharp-wave/ripples increasingly co-represent reward relationships that were never directly experienced together [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]]. That supports the broader idea that hippocampal maps propagate transition knowledge in a way compatible with SR-like updating.

Theoretical syntheses show why SR became attractive for place/grid-cell interpretation. SR naturally turns local transition structure into predictive state maps; eigenvector structure of transition graphs can produce grid-like bases; and place-like codes can be understood as policy- and transition-sensitive rather than purely geometric [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]]. But this evidence is computational and organizational, not decisive biological proof.

The best evidence against an overly broad SR account is that abstraction seems to shift beyond hippocampal-entorhinal cortex with time. Human fMRI suggests medial temporal regions retain concrete graph structure, while mPFC develops a more stimulus-independent relational map across days [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]]. That fits a division between specific predictive maps and later abstract schema-like maps, rather than a single SR mechanism doing everything.

## Landmark papers

[[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]]  
A key conceptual bridge from Tolman-style cognitive maps to modern RL/state-representation language. Important for framing hippocampus as predictive/prospective and for situating it alongside OFC rather than as an isolated spatial system.

[[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]]  
Probably the clearest synthesis placing SR in a broader taxonomy. Its main contribution is to show that SR explains some map phenomena, but latent-state models, path integration, and compositional coding are needed to explain generalization and abstract cognition more fully.

[[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]]  
The strongest causal/physiological anchor in this set. It shows hippocampal prospective computation during inference and replay-based relational linking, which are highly compatible with predictive-map views.

[[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]]  
An updated synthesis that further weakens any “SR-only” interpretation. It explicitly integrates SR with attractor/path-integration models, latent-state inference, and hippocampus-as-memory accounts.

[[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]]  
Important for boundaries: abstract relational maps may emerge in mPFC with consolidation, while MTL remains more concrete. This constrains claims that hippocampal-entorhinal SR-like maps alone explain generalized relational knowledge.

## Boundaries and tensions

The main tension is between “SR as the map” and “SR as one useful approximation.” The newer reviews favor the latter [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

Grid cells are an especially contested case. One modeling line links grid-like structure to eigenvectors of predictive transition structure; another derives them from path integration and continuous attractor dynamics. On current evidence, both remain live, and the reviews treat them as complementary more than mutually exclusive [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

Generalization is another fault line. In the Whittington taxonomy, hippocampus-as-map models such as SR can rapidly capture environment-specific structure but do not by themselves explain the strongest forms of transfer. Models with factorized cortical/entorhinal structure do better on systematic generalization [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]].

There is also a systems-level tension over where “abstract state space” lives. Hippocampus and entorhinal cortex clearly encode relational structure, but OFC/mPFC appear critical when task states are abstract, hidden, biologically relevant, or consolidated across experiences [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]] [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]].

Finally, RL implementation claims remain underconstrained. Even outside hippocampus, the broader RL literature does not clearly support a simple “dopamine carries SR prediction errors” story [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]]. That matters because some strong SR interpretations assume a clean error-driven neural implementation that is not yet established.

## Open questions

What would count as a decisive neural signature of SR in place or grid cells, beyond generic prospective coding or replay?

Do entorhinal grid-like codes primarily reflect:
- eigenvectors of learned transition structure,
- path integration in attractor networks,
- or a hybrid solution that depends on task regime?

How are latent-state inference and SR-like predictive occupancy combined in the same circuit? Reviews increasingly treat both as necessary, but the circuit-level division is unclear [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

When learning unfolds over days, how does replay contribute to the shift from concrete MTL representations to abstract mPFC relational maps? [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]] identifies the shift, but not the mechanism.

How policy-dependent are hippocampal predictive maps in practice? SR is policy-sensitive by definition, but most available evidence here does not cleanly dissociate transition structure from policy or value.

What is the right division of labor across hippocampus, entorhinal cortex, OFC, and mPFC during inference and generalization? Current evidence is strongest for interaction, not for a settled allocation of functions [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]].

## Key papers

- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]] — foundational review connecting hippocampal cognitive maps to modern state-space and decision frameworks.
- [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]] — strongest causal evidence here for hippocampal prospective relational computation and replay-based inference.
- [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] — best compact synthesis of SR, latent-state, path-integration, and compositional models.
- [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] — updated theoretical integration; especially useful for understanding why SR is insufficient on its own.
- [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]] — evidence that abstract relational maps emerge in mPFC over consolidation while MTL remains more concrete.
- [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]] — useful boundary paper on whether SR-style RL signals have a straightforward dopaminergic implementation.

## Source papers
- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]] | [[raw/mds/wikenheiser2016_cognitive_maps_hippocampus|source md]]: Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex
- [[raw/summaries/barron2020_neuronal_computation_inferential|Barron et al. 2020]] | [[raw/mds/barron2020_neuronal_computation_inferential|source md]]: Neuronal Computation Underlying Inferential Reasoning in Humans and Mice
- [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] | [[raw/mds/whittington2024_build_cognitive_map|source md]]: How to build a cognitive map: insights from models of the hippocampal formation
- [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] | [[raw/mds/whittington2022_cognitive_map_review|source md]]: How to build a cognitive map
- [[raw/summaries/baram2024_abstract_relational_map_consolidation|Baram et al. 2024]] | [[raw/mds/baram2024_abstract_relational_map_consolidation|source md]]: An abstract relational map emerges in the human medial prefrontal cortex with consolidation
- [[raw/summaries/akam2021_dopamine_model_based_rl|Akam and Walton 2021]] | [[raw/mds/akam2021_dopamine_model_based_rl|source md]]: What is dopamine doing in model-based reinforcement learning?
- [[raw/summaries/whittington2022_cognitive_map_nature|Whittington et al. 2022]] | [[raw/mds/whittington2022_cognitive_map_nature|source md]]: How to build a cognitive map
- [[raw/summaries/whittington2022_cognitive_maps_learning|Whittington et al. 2022]] | [[raw/mds/whittington2022_cognitive_maps_learning|source md]]: How to build a cognitive map
