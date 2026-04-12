---
title: "Hippocampal predictive maps: place cells, successor representation, and replay"
subtopic_id: schemas_and_generalization__01
parent_topic_id: schemas_and_generalization
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:27:03.076202+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - behrens2018_cognitive_map_organizing_knowledge
  - stachenfeld2017_hippocampus_predictive_map
  - constantinescu2016_gridlike_conceptual_knowledge
  - wilson2013_ofc_cognitive_map
  - russek2017_model_based_reinforcement
core_papers:
  - behrens2018_cognitive_map_organizing_knowledge
  - bein2024_schemas_reinforcement_learning_pfc
  - bernerslee2021_prefrontal_cortex_hippocampal
  - brunec2022_predictive_representations_hierarchies
  - buzsaki2015_hippocampal_sharp_wave_ripple
  - comrie2024_hippocampal_representations
  - constantinescu2016_gridlike_conceptual_knowledge
  - decothi2022_predictive_spatial_navigation
---

# Hippocampal predictive maps: place cells, successor representation, and replay

A useful working synthesis is that hippocampal–entorhinal circuits encode predictive structure over states, not just current location. In this framing, place-cell activity is often better described as reflecting expected future occupancy under a policy; grid-like codes provide a compact basis over transition structure; and replay supplies a mechanism for offline updating, consolidation, and sometimes prospective evaluation. This picture has substantial explanatory power for spatial navigation and some abstract-relational tasks, but it is not a complete or settled theory: canonical successor representations (SRs) are policy-dependent, do not by themselves solve all detour or transition-revaluation problems, and evidence for fully general non-spatial “cognitive maps” remains much thinner than the spatial case [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

## Current view

The strongest current view is not that the hippocampus stores a literal geometric map of space, but that hippocampal–entorhinal circuits represent the transition structure of an environment in a way that supports prediction and flexible behavior [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

Within that view, place cells are often modeled as encoding successor-like predictive states: activity at the current state reflects discounted future occupancy of other states under the current policy. This explains several classic place-field distortions more naturally than a purely local code, including backward skewing on directed tracks, obstacle-sensitive remapping, and reward-related redistribution of fields [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

Grid cells are commonly interpreted as a low-dimensional basis for those predictive maps, often via eigenvectors of the transition or SR matrix. This provides a normative reason why grid-like periodicity would be useful: it compresses future-state structure and can support vector-like navigation. But this is an interpretation, not a unique derivation; other minimal-constraint theories can also produce grid codes [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/dorrell2022_actionable_grid_cells|Dorrell et al. 2022]] [[raw/summaries/dorrell2023_actionable_grid_constraints|Dorrell et al. 2023]].

Replay is best viewed as a mechanism, not a single function. Sharp-wave ripple associated replay is implicated in consolidation, sequence generation, and prospective evaluation; in computational terms, it is a plausible substrate for Dyna-like updating of predictive representations, but replay findings do not by themselves distinguish SR, model-based search, or episodic retrieval accounts [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsáki 2015]] [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

A broader systems view places hippocampus within a predictive hierarchy. Posterior hippocampus appears to track shorter horizons, whereas prefrontal regions carry longer-range predictive structure; OFC/vmPFC likely contribute latent-state/task-space organization that interacts with hippocampal maps rather than simply reading them out [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

## Strongest evidence

- **Spatial place-field phenomena are captured by predictive-map models.**  
  SR models reproduce backward skewing on directed tracks, barrier-sensitive remapping, reward clustering, and other place-field regularities without task-specific patches [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]. This is one of the most compelling arguments that hippocampal codes are predictive, not merely local.

- **Behavior in navigation tasks often looks more SR-like than purely model-free.**  
  In a modular open-field maze tested in rats and humans, behavior was best matched overall by SR agents, with humans additionally showing early model-based signatures [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]]. That mixed pattern is important: SR-like predictive maps appear behaviorally useful, but they do not exhaust human planning.

- **Predictive structure is observed beyond literal physical space, though in limited regimes.**  
  Human hippocampal–entorhinal representations of discrete relational structure are better fit by SR than by simple Euclidean distance in non-spatial tasks [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]]. Separately, entorhinal and vmPFC fMRI show sixfold grid-like modulation during navigation of a 2D conceptual space, with signal strength related to performance [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]]. This supports extension beyond space, but mainly for low-dimensional relational domains.

- **Predictive horizons are organized across hippocampal–prefrontal gradients.**  
  During naturalistic virtual navigation, representational similarity analyses suggest short predictive scales in posterior hippocampus and longer scales in anterior PFC [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]. This fits a multiscale predictive-map account better than a single-map view.

- **Replay and non-local representations are functionally coupled to decision circuitry.**  
  PFC neurons can be selective for non-local hippocampal representations during replay and behavior [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]], and hippocampal non-local representations can flexibly track value and uncertainty during active navigation [[raw/summaries/comrie2024_hippocampal_representations|Comrie et al. 2024]]. These results strongly support a role for replay/non-local coding in decision-relevant computation, though not a uniquely SR-specific one.

- **SR theory makes precise, falsifiable distinctions from model-based planning.**  
  SR-TD solves reward revaluation but fails transition revaluation; SR-MB improves flexibility but remains policy-dependent; SR-Dyna can in principle solve all three major revaluation classes if replay is sufficient [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]]. This computational decomposition is a major strength because it clarifies what “predictive map” accounts should and should not explain.

## Landmark papers

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]  
  The core formalization of hippocampus as a predictive map. It ties place cells to SR and grid cells to spectral bases of predictive structure.

- [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]]  
  The first high-profile demonstration that grid-like signals can appear in an abstract 2D conceptual task, extending the map idea beyond physical space.

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]]  
  Crucial for separating what SR can explain from what requires fuller model-based computation or replay-mediated updates.

- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]]  
  The main synthesis paper linking hippocampal–entorhinal maps, latent task structure, OFC/PFC, and flexible generalization.

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]]  
  Important for broadening “cognitive map” from spatial navigation to hidden task state, especially in OFC.

- [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsáki 2015]]  
  The canonical review positioning replay-bearing sharp-wave ripples as a systems mechanism for consolidation and planning.

## Boundaries and tensions

- **SR is not full model-based planning.**  
  Canonical SR handles reward revaluation well, but transition revaluation and detours require additional machinery, such as explicit transition models or replay-mediated updating [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- **Policy dependence is a real limitation.**  
  The SR is learned under a policy, so sudden policy shifts are not automatically accommodated. This matters when goals or action contingencies change quickly [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- **Not all reward effects on place fields fit cleanly.**  
  Stachenfeld et al. explicitly note reward-related place-field findings that the basic SR does not fully capture [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

- **Grid-cell periodicity is not unique evidence for SR.**  
  Spectral/SR accounts are elegant, but alternative theories deriving grids from actionability, biological constraints, and discriminability also work [[raw/summaries/dorrell2022_actionable_grid_cells|Dorrell et al. 2022]] [[raw/summaries/dorrell2023_actionable_grid_constraints|Dorrell et al. 2023]]. Gridness alone does not adjudicate the theory.

- **Abstract-map claims are promising but narrow.**  
  Evidence outside spatial navigation is strongest for 2D continuous conceptual spaces and some discrete relational structures [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]] [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]]. Generalization to high-dimensional, symbolic, or strongly hierarchical domains remains more conjectural.

- **Replay is multifunctional and therefore hard to interpret.**  
  Replay supports consolidation, planning, and perhaps other forms of memory-guided computation [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsáki 2015]]. Observing replay does not by itself tell us whether the brain is updating an SR, simulating a model, or retrieving specific episodes.

- **The neural division of labor is unresolved.**  
  Hippocampus, entorhinal cortex, OFC/vmPFC, and striatum all appear relevant, but the field still lacks a consensus decomposition of which area stores predictive maps, latent states, policy structure, and value readouts [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

## Open questions

- Does hippocampal population activity implement a literal SR, or only a broader family of predictive, policy-sensitive codes that sometimes resemble SR mathematically?

- What aspects of replay are causal for behavior: updating predictive maps, evaluating alternatives, consolidating episodes, or coordinating with PFC for choice?

- How is replay prioritized? SR-Dyna-style accounts need selective replay, but biologically realistic prioritization rules remain underspecified [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- How far do grid-like and map-like codes extend beyond space? Current evidence is strongest for 2D conceptual or relational tasks, not for arbitrary abstract knowledge structures [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

- How are hidden states and partial observability handled across hippocampus and OFC? This is central if predictive maps are meant to support schema-like generalization rather than only navigation [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

- How do multiscale predictive hierarchies in hippocampus and PFC relate to schema formation and abstraction over repeated experiences [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] [[raw/summaries/bein2024_schemas_reinforcement_learning_pfc|Bein et al. 2024]]?

- In mixed human behavior, when does control shift between SR-like prediction, explicit model-based search, and episodic replay? Current navigation evidence suggests coexistence rather than a single strategy [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]].

## Key papers

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] — foundational predictive-map/SR theory for hippocampus and grid-cell spectral coding.
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] — cleanest statement of what SR explains, where it fails, and how replay can extend it.
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] — broad synthesis linking cognitive maps, task structure, and flexible behavior.
- [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]] — key evidence for grid-like coding in conceptual space.
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] — human hippocampal–entorhinal evidence for SR-like coding of abstract relational structure.
- [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] — cross-species navigation behavior consistent with predictive maps, with additional model-based components in humans.
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] — multiscale predictive hierarchy across hippocampus and PFC.
- [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsáki 2015]] — replay/sharp-wave ripple review; essential for the systems-level replay literature.
- [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]] — PFC tuning to non-local hippocampal replay content.
- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] — OFC as task-state map; important for extending predictive-map ideas beyond spatial navigation.

## Source papers
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] | [[raw/mds/behrens2018_cognitive_map_organizing_knowledge|source md]]: What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior
- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] | [[raw/mds/stachenfeld2017_hippocampus_predictive_map|source md]]: The hippocampus as a predictive map
- [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]] | [[raw/mds/constantinescu2016_gridlike_conceptual_knowledge|source md]]: Organizing conceptual knowledge in humans with a gridlike code
- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] | [[raw/mds/wilson2013_ofc_cognitive_map|source md]]: Orbitofrontal Cortex as a Cognitive Map of Task Space
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] | [[raw/mds/russek2017_model_based_reinforcement|source md]]: Predictive representations can link model-based reinforcement learning to model-free mechanisms
- [[raw/summaries/bein2024_schemas_reinforcement_learning_pfc|Bein and Niv 2024]] | [[raw/mds/bein2024_schemas_reinforcement_learning_pfc|source md]]: Schemas, reinforcement learning, and the medial prefrontal cortex
- [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]] | [[raw/mds/bernerslee2021_prefrontal_cortex_hippocampal|source md]]: Prefrontal Cortical Neurons Are Selective for Non-Local Hippocampal Representations during Replay and Behavior
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec and Momennejad 2022]] | [[raw/mds/brunec2022_predictive_representations_hierarchies|source md]]: Predictive Representations in Hippocampal and Prefrontal Hierarchies
- [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsaki 2015]] | [[raw/mds/buzsaki2015_hippocampal_sharp_wave_ripple|source md]]: Hippocampal Sharp Wave-Ripple: A Cognitive Biomarker for Episodic Memory and Planning
- [[raw/summaries/comrie2024_hippocampal_representations|Comrie et al. 2024]] | [[raw/mds/comrie2024_hippocampal_representations|source md]]: Hippocampal representations of alternative possibilities are flexibly generated to meet cognitive demands
- [[raw/summaries/decothi2022_predictive_spatial_navigation|Cothi et al. 2022]] | [[raw/mds/decothi2022_predictive_spatial_navigation|source md]]: Predictive maps in rats and humans for spatial navigation
