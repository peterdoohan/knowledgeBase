---
title: "Successor representation as a predictive-map account of hippocampal place cells"
subtopic_id: predictive_maps_and_successor_representation__03
parent_topic_id: predictive_maps_and_successor_representation
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:26:21.264023+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - behrens2018_cognitive_map_organizing_knowledge
  - garvert2017_relational_knowledge_maps
  - nyberg2022_spatial_goal_coding
  - gershman2018_successor_representation_learning
  - basu2023_goal_pointer_cognitive_map_ofc
core_papers:
  - basu2023_goal_pointer_cognitive_map_ofc
  - behrens2018_cognitive_map_organizing_knowledge
  - decothi2022_predictive_spatial_navigation
  - garvert2017_relational_knowledge_maps
  - george2022_stdp_predictive_maps
  - gershman2018_successor_representation_learning
  - momennejad2020_successor_representations_replay
  - nyberg2022_spatial_goal_coding
---

# Successor representation as a predictive-map account of hippocampal place cells

The successor-representation (SR) account treats a hippocampal place code as predictive rather than purely locational: a state is represented by the states likely to be visited next, discounted over time. This framework explains several classic place-field distortions and extends naturally to entorhinal/grid-like coding and even non-spatial relational graphs. The case is strongest at the computational and representational level, not the circuit-identity level: the literature supports hippocampal–entorhinal codes as predictive maps, but does not yet show that place cells are *nothing but* SR units, nor that SR alone explains goal coding or rapid replanning.

## Current view

The SR is now a serious candidate account of what hippocampal place-cell maps encode: expected future occupancy under the animal’s policy, rather than just current position [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

Its appeal is that it captures a middle ground between model-free and model-based reinforcement learning. Because rewards are factored from transition statistics, SR-like codes can support fast reward revaluation without recomputing everything from scratch, but they remain partly tied to previously learned transition structure [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]].

For hippocampus specifically, the account is most compelling where place fields depend on direction, barriers, reward proximity, or policy. Those are exactly the regimes where a predictive code should diverge from a pure current-location code [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]].

The broader trend is to treat hippocampal–entorhinal maps as representations of transition structure across both spatial and abstract state spaces. But that generalization is still better established for simple graph and low-dimensional conceptual tasks than for rich abstract cognition [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]].

## Strongest evidence

The cleanest support is explanatory fit to place-field geometry. SR-style place codes predict radially symmetric fields in open arenas, barrier-sensitive distortions, directional skew on one-way tracks, and overrepresentation near rewards. These are standard empirical regularities that are awkward for a strictly instantaneous location code and are highlighted as strong matches between hippocampal data and SR predictions [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

The best direct evidence that the code is predictive rather than merely geometric comes from non-spatial relational structure. In humans, entorhinal and hippocampal fMRI adaptation tracked graph distance in an implicitly learned object graph, and the signal was better explained by communicability—a parameter-free SR-like metric—than by Euclidean distance [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]]. That matters because it shows the same predictive-map logic outside physical navigation.

Cross-species behavior also lines up with SR-like navigation. In a modular open-field maze, both rats and humans reportedly navigated most similarly to SR agents, though humans also showed model-based signatures early in learning [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]]. This supports SR as a behavioral strategy, but also argues against SR as the whole story.

Mechanistic plausibility has improved. A biologically grounded hippocampal model using STDP plus theta phase precession can rapidly learn an approximation to the SR [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]]. This does not prove hippocampus uses that mechanism, but it removes a common objection that SR is only a convenient algorithmic abstraction.

Replay is a natural bridge between hippocampal physiology and SR updating. Reviews argue that offline replay can update predictive structure and support generalization, though direct evidence isolating replay-specific SR learning remains incomplete [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] [[raw/summaries/nyberg2022_spatial_goal_coding|Nyberg et al. 2022]].

## Landmark papers

[[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]] crystallized the computational claim: SR is a distinct RL strategy with a plausible neural substrate in hippocampus, explaining why place fields reflect future occupancy and why behavior should show asymmetric sensitivity to reward versus transition revaluation.

[[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] broadened the theory from place cells to a general cognitive-map framework. It connected SR-like predictive maps, grid-cell eigenvector ideas, and prefrontal/orbitofrontal latent-state representations into one organizing view.

[[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] supplied a key empirical step beyond space: hippocampal–entorhinal activity recovered a discrete relational graph and was better fit by an SR-like predictive metric than by Euclidean distance.

[[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] is important because it links the theory to actual navigation behavior in both rats and humans, while also showing residual model-based components.

[[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]] matters for implementation: it shows how known hippocampal timing rules could, in principle, learn predictive maps quickly.

## Boundaries and tensions

The main strength of the SR is also its main limitation: it compiles expected future occupancy under a policy. That makes it efficient and reward-flexible, but less immediately adaptable when transition structure changes. Reviews explicitly emphasize this asymmetry [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]]. If animals instantly replan after transition changes, plain SR is insufficient.

Goal coding is only partly explained by hippocampal predictive maps. Hippocampal fields and replay often overrepresent goals or future routes, but persistent destination-specific coding throughout a journey appears more characteristic of OFC than hippocampus [[raw/summaries/nyberg2022_spatial_goal_coding|Nyberg et al. 2022]] [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]]. This fits a division where hippocampus provides predictive state structure and OFC carries a goal or reward vector, but that architecture is still a proposal.

There is also a representational tension between spatial SR theory and some abstract-task results. In the abstract graph study, the neural metric was effectively non-directional/symmetrized [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]], whereas the classic SR is policy-dependent and directional. That mismatch could reflect the task, the measurement method, or averaging over bidirectional experience, but it means “SR-like” should not be read too literally in every dataset.

Most evidence is indirect. Reviews summarize close fits between place-field distortions and SR predictions, but the decisive experiments are often model-comparison exercises rather than neural tests that uniquely identify SR over competing mechanisms [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]] [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]]. The account is therefore strongest as an intermediate-level theory of representational content.

Finally, the extension from spatial to abstract cognition remains promising but not settled. Evidence for grid-like or predictive-map coding in non-spatial domains exists, yet direct demonstrations are still sparse outside relatively simple continuous or graph-structured tasks [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

## Open questions

How directly can SR be read out from hippocampal population activity? The field still lacks decisive neural signatures that separate current-location coding, SR coding, and model-based planning in the same task.

How is SR updated online versus via replay? Replay is a plausible mechanism for learning or refining predictive maps, but its specific causal role in SR updating remains unresolved [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] [[raw/summaries/nyberg2022_spatial_goal_coding|Nyberg et al. 2022]].

What is the division of labor between hippocampus and OFC? A useful synthesis is “hippocampus = predictive map, OFC = goal pointer,” but the interaction between these codes during planning is still hypothetical [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]].

Are grid cells literally an eigenbasis for SR-like transition structure, or is that mainly a mathematically elegant analogy? The theory is powerful, but direct biological adjudication is still limited [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

Can simple synaptic rules really learn the relevant predictive map at behavioral timescales in vivo? Model work says yes in principle [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]], but experimental validation is still missing.

How far does the framework generalize beyond navigation? The abstract-graph result is strong [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]], but evidence across richer conceptual, hierarchical, or partially observable tasks remains thin [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]].

## Key papers

- [[raw/summaries/gershman2018_successor_representation_learning|Gershman et al. 2018]] — Core computational review linking SR to hippocampal place fields and RL tradeoffs.
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] — Broad theoretical synthesis connecting predictive maps, grid/place codes, and abstract cognition.
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] — Strong empirical support that hippocampal–entorhinal representations of abstract graphs are better fit by an SR-like metric than Euclidean distance.
- [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] — Cross-species behavioral evidence that navigation often resembles SR agents, with some model-based contributions in humans.
- [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]] — Mechanistic model showing biologically plausible learning of predictive maps.
- [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad et al. 2020]] — Review emphasizing replay as a route to SR learning and generalization.
- [[raw/summaries/nyberg2022_spatial_goal_coding|Nyberg et al. 2022]] — Useful boundary paper on what hippocampal goal coding does and does not explain.
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]] — Important counterweight showing that persistent remote goal coding may live outside hippocampus, especially in OFC.

## Source papers
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] | [[raw/mds/behrens2018_cognitive_map_organizing_knowledge|source md]]: What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] | [[raw/mds/garvert2017_relational_knowledge_maps|source md]]: A map of abstract relational knowledge in the human hippocampal–entorhinal cortex
- [[raw/summaries/nyberg2022_spatial_goal_coding|Nyberg et al. 2022]] | [[raw/mds/nyberg2022_spatial_goal_coding|source md]]: Spatial goal coding in the hippocampal formation
- [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]] | [[raw/mds/gershman2018_successor_representation_learning|source md]]: The Successor Representation: Its Computational Logic and Neural Substrates
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu and Ito 2023]] | [[raw/mds/basu2023_goal_pointer_cognitive_map_ofc|source md]]: A goal pointer for a cognitive map in the orbitofrontal cortex
- [[raw/summaries/decothi2022_predictive_spatial_navigation|Cothi et al. 2022]] | [[raw/mds/decothi2022_predictive_spatial_navigation|source md]]: Predictive maps in rats and humans for spatial navigation
- [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]] | [[raw/mds/george2022_stdp_predictive_maps|source md]]: Rapid learning of predictive maps with STDP and theta phase precession
- [[raw/summaries/momennejad2020_successor_representations_replay|Momennejad 2020]] | [[raw/mds/momennejad2020_successor_representations_replay|source md]]: Learning Structures: Predictive Representations, Replay, and Generalization
