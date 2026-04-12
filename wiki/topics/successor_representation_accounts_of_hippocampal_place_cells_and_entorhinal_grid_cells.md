---
title: "Successor representation accounts of hippocampal place cells and entorhinal grid cells"
subtopic_id: predictive_maps_and_successor_representation__04
parent_topic_id: predictive_maps_and_successor_representation
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:26:27.951750+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - stachenfeld2017_hippocampus_predictive_map
  - whittington2020_tolman_eichenbaum_machine
  - whittington2024_build_cognitive_map
  - whittington2022_cognitive_map_review
  - widloski2022_hippocampal_replay_barriers
core_papers:
  - momennejad2017_successor_representation_humans
  - stachenfeld2017_hippocampus_predictive_map
  - tacikowski2024_temporal_structure_hippocampal
  - tomov2020_hierarchical_planning_representation
  - whittington2020_tolman_eichenbaum_machine
  - whittington2022_cognitive_map_review
  - whittington2024_build_cognitive_map
  - widloski2022_hippocampal_replay_barriers
---

# Successor representation accounts of hippocampal place cells and entorhinal grid cells

The successor representation (SR) account proposes that hippocampal place cells encode predictive occupancy over future states, while entorhinal grid cells provide a low-dimensional basis for that predictive map. This has become a major computational framing because it explains several classic place/grid phenomena within one formalism and extends naturally to nonspatial structure. But the case is still uneven: the strongest support is theoretical and indirect, direct neural tests are newer and narrower, and several findings imply that place fields alone are not the whole predictive map.

## Current view

The SR is now a serious candidate description of what hippocampal maps compute, not just where the animal is. In the canonical version, each state representation is weighted by expected discounted future occupancy under the current policy, so place fields should reflect transition structure, barriers, and behavioral direction, not only instantaneous position [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

That framework is attractive because it unifies spatial and nonspatial results. The same predictive-map machinery can explain hippocampal similarity effects over graph structure and can be extended to temporal structure in human hippocampal-entorhinal recordings [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]].

The grid-cell claim is more specific and more tentative. SR eigenvectors generate grid-like basis functions with geometry-dependent distortions, giving a normative reason for grid codes as a spectral basis for prediction [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]. But this is not the only viable account of grid cells; later syntheses place SR alongside attractor/path-integration models rather than above them [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

A broader shift in the field is from “literal SR everywhere” toward hybrid views. Models such as the Tolman-Eichenbaum Machine (TEM) preserve the predictive/structural intuition but factorize abstract structural knowledge from hippocampal sensory memory, capturing remapping and generalization more flexibly than simple SR formulations [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

## Strongest evidence

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] is the core theoretical result.
  - SR place fields reproduce backward skewing on directed tracks.
  - They distort around barriers and obstacles in the right qualitative direction.
  - They cluster near reward locations without adding reward-specific assumptions.
  - The same SR applied to nonspatial graph stimuli reproduces hippocampal community-structure effects in human fMRI.
  - SR eigenvectors generate grid-like fields across several environment geometries.

- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] provides behavioral support for SR-like learning in humans.
  - Performance in sequential decision tasks is better fit by hybrid SR models than by purely model-free accounts.
  - The key signature is asymmetric sensitivity to reward revaluation versus transition revaluation, as expected if subjects cache multi-step predictions rather than a full transition model.

- [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]] extends the predictive-map idea beyond space.
  - Human hippocampal and entorhinal neurons encode temporal structure of experience in a way consistent with predictive successor-like coding.
  - Offline replay is implicated, linking predictive coding to sequence dynamics rather than static map structure alone.

- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] shows that many “SR-like” successes survive in a richer model.
  - Grid-like entorhinal representations and place-like hippocampal remapping emerge from factorized structural learning.
  - This matters because it suggests the key explanatory ingredient may be predictive relational structure, not necessarily a literal tabular SR in hippocampal neurons.

- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] is strong negative/constraint evidence for simple readings of the theory.
  - Replay rapidly reroutes around barriers.
  - Place fields remain largely stable across many barrier configurations.
  - So flexible prediction/planning can update faster than the static place code, implying that any predictive-map theory needs a dynamic component beyond place fields themselves.

## Landmark papers

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]
  - Seminal formulation of hippocampus as an SR-based predictive map and entorhinal grid cells as SR eigenvectors.

- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]]
  - Established SR as a psychologically relevant strategy in human reinforcement learning, giving the hippocampal theory a behavioral foundation.

- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]]
  - Major extension beyond simple SR, showing how predictive relational structure can support remapping and generalization.

- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]]
  - Important empirical constraint: flexible route prediction can dissociate from stable place fields.

- [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]]
  - Direct human neural evidence that hippocampal-entorhinal coding tracks predictive temporal structure, not just space.

## Boundaries and tensions

The cleanest SR account is policy-dependent. That is a feature for explaining directionality and reward-related distortions, but it is also a limitation: when transition structure changes, cached predictions must be relearned, so SR is less flexible than full model-based inference [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]].

The place-cell fit is not complete. Stachenfeld et al. explicitly note that SR-predicted reward-related place-field enlargement does not cleanly match all reward-field data, so the theory should not be treated as a full account of reward coding in hippocampus [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

The grid-cell account is elegant but underdetermined. SR eigenvectors produce grid-like structure, yet they can also yield anisotropies in rectangular environments that are not obviously biological, and reviews continue to treat attractor/path-integration models as strong alternatives or complements [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

Replay creates an additional tension. If place cells literally are the predictive map, then rapid barrier-sensitive rerouting should often appear in place codes themselves. Instead, replay can adapt while global place maps stay stable [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]]. That pushes the field toward multi-component accounts: stable map-like codes plus flexible sequence generation and inference.

TEM sharpens this tension rather than resolving it away. It retains predictive relational structure but moves away from a one-to-one identity between hippocampal place cells and SR rows, or entorhinal grid cells and SR eigenvectors [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]]. In practice, this means the field increasingly treats SR as a computational principle, not a settled neural implementation.

## Open questions

How directly do identified place cells encode SR quantities, as opposed to participating in a broader predictive/inferential system that only approximates SR at the population level?

Are grid cells best understood as SR eigenvectors, path-integration attractor states, or a synthesis of both? Current evidence does not force a single answer [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]].

What mechanism updates predictive maps quickly after environmental change? Replay is a prime candidate, but the exact relationship between replay, online remapping, and SR learning remains unclear [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]].

Does the hippocampal longitudinal axis truly implement a gradient of prediction horizons, as proposed in the SR framework? This remains an appealing but still indirect part of the theory [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

How far does the account generalize beyond space? Human temporal-structure data and graph-learning results are promising, but nonspatial “cognitive map” phenomena can also be captured by latent-state and compositional models that are not reducible to simple SR [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]].

## Key papers

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] — foundational predictive-map theory; place cells as SR, grid cells as SR eigenvectors.
- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] — strongest behavioral evidence that humans use SR-like predictive learning.
- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] — broader relational model that preserves predictive structure while explaining remapping and generalization.
- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] — key empirical constraint showing flexible replay without global place remapping.
- [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]] — human hippocampal-entorhinal evidence for predictive temporal coding.
- [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] — useful synthesis of SR with latent-state, attractor, and compositional frameworks.
- [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] — updated synthesis emphasizing path integration, generalization, and hybrid accounts.

## Source papers
- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] | [[raw/mds/stachenfeld2017_hippocampus_predictive_map|source md]]: The hippocampus as a predictive map
- [[raw/summaries/whittington2020_tolman_eichenbaum_machine|Whittington et al. 2020]] | [[raw/mds/whittington2020_tolman_eichenbaum_machine|source md]]: The Tolman-Eichenbaum Machine: Unifying Space and Relational Memory through Generalization in the Hippocampal Formation
- [[raw/summaries/whittington2024_build_cognitive_map|Whittington et al. 2024]] | [[raw/mds/whittington2024_build_cognitive_map|source md]]: How to build a cognitive map: insights from models of the hippocampal formation
- [[raw/summaries/whittington2022_cognitive_map_review|Whittington et al. 2022]] | [[raw/mds/whittington2022_cognitive_map_review|source md]]: How to build a cognitive map
- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski and Foster 2022]] | [[raw/mds/widloski2022_hippocampal_replay_barriers|source md]]: Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping
- [[raw/summaries/momennejad2017_successor_representation_humans|Momennejad et al. 2017]] | [[raw/mds/momennejad2017_successor_representation_humans|source md]]: The successor representation in human reinforcement learning
- [[raw/summaries/tacikowski2024_temporal_structure_hippocampal|Tacikowski et al. 2024]] | [[raw/mds/tacikowski2024_temporal_structure_hippocampal|source md]]: Human hippocampal and entorhinal neurons encode the temporal structure of experience
- [[raw/summaries/tomov2020_hierarchical_planning_representation|Tomov et al. 2020]] | [[raw/mds/tomov2020_hierarchical_planning_representation|source md]]: Discovery of hierarchical representations for efficient planning
