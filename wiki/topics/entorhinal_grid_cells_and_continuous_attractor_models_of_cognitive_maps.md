---
title: "Entorhinal grid cells and continuous attractor models of cognitive maps"
subtopic_id: cognitive_maps__04
parent_topic_id: cognitive_maps
page_type: topic
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:26:36.224337+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - baram2021_entorhinal_ventromedial_rl
  - yu2025_theta_sweeps_goal_direction
  - whittington2024_build_cognitive_map
  - piray2025_compositional_cognitive_map
  - wen2024_entorhinal_maps_flexible_navigation
core_papers:
  - baram2021_entorhinal_ventromedial_rl
  - piray2025_compositional_cognitive_map
  - wen2024_entorhinal_maps_flexible_navigation
  - whittington2024_build_cognitive_map
  - yu2025_theta_sweeps_goal_direction
---

# Entorhinal grid cells and continuous attractor models of cognitive maps

The strongest current account is that medial entorhinal cortex (MEC) supplies a low-dimensional, path-integrable state code that is well captured by continuous attractor dynamics, while hippocampus and frontal/striatal circuits read out, bind, and use that code for memory, planning, and structure-sensitive learning. The evidence is strongest for spatial navigation and rapid landmark-constrained remapping in MEC; extension to abstract, non-spatial “cognitive maps” is now supported at the level of relational/task structure in human entorhinal cortex, but not yet by direct cell-level demonstrations of grid-like or attractor dynamics outside space.

## Current view

Continuous attractor models remain one of the most mechanistically concrete explanations for grid-cell population dynamics. They explain why grid representations can support path integration, low-dimensional state evolution, and stable-but-correctable internal maps.

The best recent empirical support is that MEC population activity shows low-dimensional attractor-like dynamics and predictable landmark-driven distortions, rather than arbitrary remapping, in novel environments [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]]. This pushes the field beyond “grid cells correlate with position” toward explicit dynamical constraints.

A broader synthesis is that entorhinal maps are not sufficient by themselves for flexible behavior. Instead, MEC may provide reusable latent coordinates, while hippocampus stores episode- or environment-specific bindings and downstream circuits implement fast credit assignment and policy adaptation [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

For abstract cognition, the strongest claim currently justified is not “grid cells encode everything,” but that entorhinal cortex can represent relational structure in a sensory-general way during non-spatial reinforcement learning [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]]. That is compatible with cognitive-map theories and with models such as TEM/SR-like or compositional schemes, but does not by itself validate a continuous attractor mechanism in abstract task spaces.

## Strongest evidence

[[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] is the clearest direct support here.

- Neuropixels recordings in 1D virtual reality showed grid-cell population activity evolving on a low-dimensional manifold consistent with a continuous attractor.
- In darkness, the activity bump drifted diffusively, as attractor models predict under path integration without anchoring.
- Visual landmarks rapidly pinned and distorted the attractor trajectory, producing one-shot remapping after a single exposure.
- A model with fixed landmark-to-grid connectivity and weak pinning explained the data better than short-timescale Hebbian rewiring.

This is unusually strong because it constrains both geometry and dynamics. The paper supports a specific class of mechanisms, not just a descriptive “map” metaphor.

[[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] provides the strongest evidence that entorhinal representations generalize beyond physical space.

- In human fMRI, right entorhinal cortex encoded relational structure across different sensory instantiations of the same RL problem.
- Behavior showed subjects actually used that structure.
- vmPFC and ventral striatum carried structure-dependent prediction-error patterns.

What this establishes is abstract structural coding in EC. What it does not establish is a grid code, hexadirectional signal, or continuous attractor implementation for abstract tasks.

[[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] adds a planning-relevant dynamical link.

- Hippocampal theta sweeps aligned with goal direction more than with movement or head direction.
- Goal modulation strengthened with learning and predicted correct choices.
- A hierarchical attractor model with goal-directed input reproduced the sweep bias.

This supports the broader idea that attractor-based map dynamics can be coupled to goal information for online planning. But the recordings are hippocampal, so this is indirect evidence for MEC-centered attractor accounts.

## Landmark papers

[[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] is a landmark for direct population-level evidence that grid codes behave like a continuous attractor under path integration plus landmark anchoring. It also sharpens an important systems claim: map stability in MEC can be rapid and largely non-plastic over short timescales, while behavioral flexibility is delegated downstream.

[[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] is a landmark for extending entorhinal cognitive-map ideas into non-spatial reinforcement learning. Its key contribution is not “abstract grid cells,” but showing entorhinal structure representations that generalize across sensory content.

[[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] is the clearest recent synthesis of how continuous attractors, successor-like predictive structure, latent-state inference, and hippocampal memory accounts can be made complementary rather than mutually exclusive.

[[raw/summaries/piray2025_compositional_cognitive_map|Piray 2025]] is a notable computational attempt to reconcile efficiency and flexibility by treating MEC as a compositional predictive map, including object-related perturbations to baseline open-space maps. It is theoretically fertile, but still a model awaiting decisive empirical adjudication.

## Boundaries and tensions

The cleanest evidence for continuous attractor dynamics is spatial and sensorimotor. Claims about abstract cognitive maps are presently stronger at the representational level than at the mechanistic level. In other words: “entorhinal cortex encodes structure” is supported; “abstract structure is implemented by continuous attractor grid dynamics” is still mostly extrapolation.

There is also a division-of-labor tension. [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] argues for fixed landmark-to-grid coupling over short timescales and downstream plasticity for flexible navigation. That sits uneasily with simpler views in which MEC itself rapidly learns the whole task model.

Model pluralism remains unresolved. Continuous attractors explain path integration and low-dimensional grid dynamics well, but successor-representation, latent-state, and compositional models explain other aspects of generalization and planning that attractor models alone do not fully capture [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]]. The field increasingly treats these as partially complementary, but the exact interface is still underspecified.

Abstract generalization findings in entorhinal cortex are also limited by method. [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] is fMRI RSA, with a right-lateralized effect and no cellular or causal resolution. It is compelling evidence for relational coding, not for a specific circuit mechanism.

Finally, recent planning results implicate goal-biased sequential dynamics in hippocampus [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]], but the origin of the goal input and the specific MEC-hippocampal contribution remain uncertain.

## Open questions

- Do non-spatial entorhinal task-structure codes actually have continuous attractor geometry, or only abstract relational similarity?
- How are recurrent weights that support grid-like attractor dynamics acquired: developmentally, through experience, or both? [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]]
- What exactly provides landmark/object input to the attractor, and how do border, object-vector, and sensory inputs interact with grid dynamics? [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]]
- If MEC maps are relatively fixed over short timescales, where is fast task-specific adaptation implemented—CA1, other hippocampal subfields, PFC, striatum, or some combination?
- Can compositional object- and barrier-based predictive maps proposed for MEC be validated physiologically, especially in dynamic environments? [[raw/summaries/piray2025_compositional_cognitive_map|Piray 2025]]
- How are goal signals injected into map dynamics during planning, and are the relevant control signals top-down from mPFC/retrosplenial routes? [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]]
- Under what conditions does hippocampus act as a map versus as a memory system linking cortical map fragments? [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]]

## Key papers

- [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] — strongest direct empirical support that MEC grid populations exhibit continuous-attractor-like dynamics, including diffusion, pinning, and one-shot remapping.
- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] — strongest evidence that entorhinal cortex encodes abstract relational structure in non-spatial RL, generalizing across sensory instantiations.
- [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] — best current synthesis integrating attractor networks with latent-state, SR-like, and hippocampal memory frameworks.
- [[raw/summaries/piray2025_compositional_cognitive_map|Piray 2025]] — important compositional MEC model linking grid-like maps, object-vector-like coding, and efficient planning; promising but currently theoretical.
- [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] — shows goal-directed hippocampal sweep dynamics and offers an attractor-based planning mechanism, though not direct MEC evidence.

## Source papers
- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] | [[raw/mds/baram2021_entorhinal_ventromedial_rl|source md]]: Entorhinal and ventromedial prefrontal cortices abstract and generalize the structure of reinforcement learning problems
- [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] | [[raw/mds/yu2025_theta_sweeps_goal_direction|source md]]: Hippocampal theta sweeps indicate goal direction
- [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] | [[raw/mds/whittington2024_build_cognitive_map|source md]]: How to build a cognitive map: insights from models of the hippocampal formation
- [[raw/summaries/piray2025_compositional_cognitive_map|Piray and Daw 2025]] | [[raw/mds/piray2025_compositional_cognitive_map|source md]]: Reconciling flexibility and efficiency: medial entorhinal cortex represents a compositional cognitive map
- [[raw/summaries/wen2024_entorhinal_maps_flexible_navigation|Wen et al. 2024]] | [[raw/mds/wen2024_entorhinal_maps_flexible_navigation|source md]]: One-shot entorhinal maps enable flexible navigation in novel environments
