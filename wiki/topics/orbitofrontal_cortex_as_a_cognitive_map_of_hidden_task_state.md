---
title: "Orbitofrontal cortex as a cognitive map of hidden task state"
subtopic_id: ofc_task_state_and_value_maps__03
parent_topic_id: ofc_task_state_and_value_maps
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:48:25.031737+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - behrens2018_cognitive_map_organizing_knowledge
  - constantinescu2016_gridlike_conceptual_knowledge
  - schuck2016_orbitofrontal_cortex_state
  - garvert2017_relational_knowledge_maps
  - brunec2022_predictive_representations_hierarchies
core_papers:
  - behrens2018_cognitive_map_organizing_knowledge
  - botvinick2020_deep_reinforcement_learning_neuro
  - brunec2022_predictive_representations_hierarchies
  - comrie2024_hippocampal_representations
  - constantinescu2016_gridlike_conceptual_knowledge
  - costa2022_orbitofrontal_cognitive_maps
  - garvert2017_relational_knowledge_maps
  - kleinflugge2022_medial_orbital_frontal
related_wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
---

# Orbitofrontal cortex as a cognitive map of hidden task state

The strongest current claim is narrower than “OFC encodes a general cognitive map.” The best-supported version is that OFC carries compact representations of task-relevant, partially observable state—especially latent variables needed for flexible choice, credit assignment, and inference. The cleanest direct evidence is human fMRI decoding in [[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]]. Broader “map” and predictive-representation frameworks from hippocampal–entorhinal work make this interpretation plausible, but those adjacent literatures should not be mistaken for direct proof that OFC universally implements map-like or successor-like state spaces.

## Current view

OFC is now commonly treated as more than a value register. In tasks where the observable stimulus is insufficient, OFC appears to represent the hidden task state that links observations to outcomes and appropriate actions, consistent with model-based or belief-state style accounts.

The key idea is selective state compression, not exhaustive sensory coding. OFC seems to prioritize information that is currently hidden but behaviorally necessary, while dropping observable or task-irrelevant variables. That pattern is central to the task-state interpretation in [[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]].

This view fits broader arguments that flexible behavior requires an internal representation of transition structure or latent state space, articulated in [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]]. But the strongest evidence for full geometric or predictive-map coding still comes from hippocampal–entorhinal systems, not OFC.

A useful working synthesis is: OFC likely represents task states in a way that is tightly coupled to expected outcomes and value, rather than representing value and state as cleanly separable channels.

## Strongest evidence

[[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]] is the anchor paper.

- In a task requiring inference over 16 hidden states, multivariate fMRI decoding from OFC reached 12.2% accuracy versus 6.25% chance.
- OFC selectively encoded hidden, task-relevant components:
  - previous category
  - previous age
  - current category
- OFC did not decode the directly observable current age, and did not decode task-irrelevant information from two trials back.
- Medial OFC was the only region in which all three hidden state components could be decoded together in a conjunction analysis.
- Better hidden-state decoding predicted better behavior: classification accuracy correlated negatively with error rate (r = -0.58).
- State decoding weakened before behavioral errors, linking the representation to impending failure rather than epiphenomenal task engagement.

This is unusually strong evidence because it shows all three of the critical features at once: hidden-state content, task relevance, and behavioral significance.

Causal support is thinner but important. [[raw/summaries/costa2022_orbitofrontal_cognitive_maps|Costa et al. 2022]] reported that chemogenetic inactivation of lateral OFC during initial Pavlovian conditioning impaired the specificity, but not the existence, of later cognitive maps. That result fits the idea that OFC helps construct precise task-state or cue–outcome structure during learning, though it does not by itself establish a general latent-state code across tasks.

The lesion and theory synthesis in [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] adds convergent support: OFC/vPFC lesions impair credit assignment and the use of latent-state structure, which is the behavioral deficit expected if state-space representations are degraded.

## Landmark papers

[[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]]  
Direct human evidence that OFC represents hidden task state. Still the clearest empirical foundation for the claim.

[[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]]  
Placed OFC into a broader computational story: flexible behavior depends on representations of transition structure, with OFC/vPFC implicated in latent-state and credit-assignment problems.

[[raw/summaries/costa2022_orbitofrontal_cognitive_maps|Costa et al. 2022]]  
Provided causal evidence that lateral OFC contributes to building specific cognitive maps during learning, not merely reading them out at choice.

[[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]]  
Important nearby result: vmPFC/OFC showed sixfold grid-like fMRI signal during navigation of a 2D conceptual space. This supports non-spatial map-like coding in frontal cortex, but it is not direct evidence about hidden task-state representation in OFC.

[[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]  
Showed OFC/medial PFC sit within a broader prefrontal predictive hierarchy during navigation. Relevant for predictive-map interpretations, but again not a direct test of latent task state in OFC.

## Boundaries and tensions

The phrase “cognitive map” is doing a lot of work. In the OFC literature it often means a representation of latent task state, not necessarily a metric map, grid code, or successor representation. Those should not be conflated.

Direct OFC evidence is concentrated in a small set of paradigms. [[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]] is strong, but much of the surrounding support is indirect, theoretical, lesion-based, or borrowed from hippocampal–entorhinal and vmPFC literatures.

Anatomical specificity remains unresolved. The strongest human hidden-state result localized to medial OFC, whereas [[raw/summaries/costa2022_orbitofrontal_cognitive_maps|Costa et al. 2022]] emphasizes lateral OFC in map construction. This could reflect subregional specialization, species/task differences, or both.

State and value are not cleanly separable in OFC. The literature motivating task-state accounts often emerged precisely because pure value accounts were insufficient, but that does not mean OFC is “state only.” A more realistic reading is that OFC carries state representations in a value-relevant format.

Successor-representation and predictive-map frameworks are nearby, not settled descriptions of OFC. They have stronger empirical traction in hippocampal–entorhinal work such as [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] and in broader prefrontal hierarchies such as [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]]. Whether OFC itself explicitly encodes multi-step predictive occupancy is still not well established.

## Open questions

Is OFC necessary for representing hidden state at decision time, or mainly for constructing precise state structure during learning? [[raw/summaries/costa2022_orbitofrontal_cognitive_maps|Costa et al. 2022]] points toward a learning-stage role, but that distinction remains unsettled.

What exactly is the representational format in OFC?
- discrete latent-state labels
- belief states under partial observability
- predictive/successor-like occupancy codes
- value-weighted outcome-state representations

How are roles divided across OFC subregions? The medial/lateral distinction is suggestive but not resolved.

How does OFC interact with hippocampal–entorhinal systems when latent states must be inferred from relational structure rather than directly learned from reinforcement history?

How general is the phenomenon across task classes? Evidence is strongest for carefully designed hidden-state paradigms, much weaker for claims that OFC supports domain-general abstract maps.

When frontal “grid-like” or predictive signals are observed, are they the same computation as hippocampal–entorhinal maps, or a different, more decision-oriented abstraction layered on top?

## Key papers

- [[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]] — direct decoding evidence that OFC encodes hidden, task-relevant state.
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] — theoretical synthesis linking latent-state structure, flexible behavior, and OFC/vPFC.
- [[raw/summaries/costa2022_orbitofrontal_cognitive_maps|Costa et al. 2022]] — causal evidence that lateral OFC contributes to building specific cognitive maps during learning.
- [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]] — grid-like conceptual coding in vmPFC/OFC; important adjacent evidence, not a direct hidden-state test.
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] — strong non-spatial predictive-map evidence in hippocampal–entorhinal cortex; relevant comparison class.
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec et al. 2022]] — places OFC within a broader prefrontal predictive hierarchy across horizons.
- [[raw/summaries/kleinflugge2022_medial_orbital_frontal|Kleinflügge et al. 2022]] — review emphasizing orbital/medial frontal cortex as representing environmental structure and causal relationships, not just reward.

## Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]: Link as complementary map frameworks: Page A should point to Page B for the broader predictive/cognitive-map background, while Page B should point to Page A as a distinct prefrontal application emphasizing partially observable task-state coding rather than canonical spatial/SR mapping.

## Source papers
- [[raw/summaries/behrens2018_cognitive_map_organizing_knowledge|Behrens et al. 2018]] | [[raw/mds/behrens2018_cognitive_map_organizing_knowledge|source md]]: What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior
- [[raw/summaries/constantinescu2016_gridlike_conceptual_knowledge|Constantinescu et al. 2016]] | [[raw/mds/constantinescu2016_gridlike_conceptual_knowledge|source md]]: Organizing conceptual knowledge in humans with a gridlike code
- [[raw/summaries/schuck2016_orbitofrontal_cortex_state|Schuck et al. 2016]] | [[raw/mds/schuck2016_orbitofrontal_cortex_state|source md]]: Human Orbitofrontal Cortex Represents a Cognitive Map of State Space
- [[raw/summaries/garvert2017_relational_knowledge_maps|Garvert et al. 2017]] | [[raw/mds/garvert2017_relational_knowledge_maps|source md]]: A map of abstract relational knowledge in the human hippocampal–entorhinal cortex
- [[raw/summaries/brunec2022_predictive_representations_hierarchies|Brunec and Momennejad 2022]] | [[raw/mds/brunec2022_predictive_representations_hierarchies|source md]]: Predictive Representations in Hippocampal and Prefrontal Hierarchies
- [[raw/summaries/botvinick2020_deep_reinforcement_learning_neuro|Botvinick et al. 2020]] | [[raw/mds/botvinick2020_deep_reinforcement_learning_neuro|source md]]: Deep Reinforcement Learning and Its Neuroscientific Implications
- [[raw/summaries/comrie2024_hippocampal_representations|Comrie et al. 2024]] | [[raw/mds/comrie2024_hippocampal_representations|source md]]: Hippocampal representations of alternative possibilities are flexibly generated to meet cognitive demands
- [[raw/summaries/costa2022_orbitofrontal_cognitive_maps|Costa et al. 2022]] | [[raw/mds/costa2022_orbitofrontal_cognitive_maps|source md]]: The role of the lateral orbitofrontal cortex in creating cognitive maps
- [[raw/summaries/kleinflugge2022_medial_orbital_frontal|Klein-Flügge et al. 2022]] | [[raw/mds/kleinflugge2022_medial_orbital_frontal|source md]]: Medial and orbital frontal cortex in decision-making and flexible behavior
