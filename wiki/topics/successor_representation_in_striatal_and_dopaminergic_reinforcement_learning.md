---
title: "Successor representation in striatal and dopaminergic reinforcement learning"
subtopic_id: striatal_and_dopaminergic_reinforcement_learning__03
parent_topic_id: striatal_and_dopaminergic_reinforcement_learning
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:49:21.707215+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - russek2017_model_based_reinforcement
  - momennejad2018_offline_replay_planning
  - gershman2018_successor_representation_learning
  - basu2023_goal_pointer_cognitive_map_ofc
  - piray2020_linear_reinforcement_learning
core_papers:
  - basu2023_goal_pointer_cognitive_map_ofc
  - decothi2022_predictive_spatial_navigation
  - george2022_stdp_predictive_maps
  - gershman2018_successor_representation_learning
  - kaplan2018_active_inference_navigation
  - kravitz2010_basal_ganglia_optogenetic
  - mcnamara2017_dopamine_hippocampus
  - mizes2023_sensorimotor_striatum
---

# Successor representation in striatal and dopaminergic reinforcement learning

The successor representation (SR) is best understood here as a predictive state code that lets temporally-difference-trained cortico-striatal circuits express some planning-like flexibility without full online search. In this view, dopamine can still train value estimates with TD-like errors, but the learned features are future occupancies rather than bare current states. That idea is attractive because it explains why behavior can look more flexible than classic model-free RL while remaining cheaper than full model-based planning. The evidence is strongest for this middle-ground computational profile and for hippocampal predictive-map correlates; it is weaker for the sharper claim that dopamine neurons literally carry vector-valued SR prediction errors or that striatum itself is the primary SR substrate.

## Current view

SR has become a serious candidate for the representational format linking hippocampal predictive maps to striatal value learning, rather than a niche alternative to model-free or model-based RL. The core claim is that value can be learned with standard TD machinery if state inputs already encode expected future state occupancy [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]].

This account naturally predicts asymmetric flexibility. Reward revaluation should be relatively easy, because rewards are separated from the predictive map; transition revaluation should be harder, because cached occupancies become stale when the environment changes [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]].

The likely neural division of labor is distributed. Hippocampus and possibly prefrontal cortex are candidate sources of predictive-map-like state features; striatum is a plausible site for reward readout and action valuation over those features; dopamine is a candidate teaching signal for updating values and possibly the predictive map itself [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]]. But this remains an architectural proposal more than a settled circuit fact.

Replay is now central to the story. Vanilla SR is too rigid for detours and policy changes. Replay-based or model-based updates can restore flexibility, making the empirical question less “SR or planning?” than “which updates are computed online, and which are compiled offline?” [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]].

## Strongest evidence

- **Computationally precise flexibility profile**
  - [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] showed that SR-TD captures reward revaluation without retraining, unlike pure model-free TD, but fails on transition revaluation.
  - The same paper showed that adding either model-based recomputation of the SR (SR-MB) or sufficient replay (SR-Dyna) recovers more flexible behavior.
  - This is not direct neural evidence, but it gives unusually sharp behavioral signatures for distinguishing SR-like computation from both classic habits and full planning.

- **Behavioral evidence for SR-like navigation**
  - [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] reported that rats and humans navigating a modular open field were best matched by SR agents, with humans also showing early model-based signatures.
  - That pattern fits the current consensus: SR often explains average navigation behavior well, but it does not eliminate a contribution from online planning.

- **Replay predicts replanning in humans**
  - In [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]], MVPA evidence for replay of a distal task state during rest predicted subsequent replanning in revaluation blocks.
  - Replay was condition-specific, and neural sensitivity to unsigned prediction error in ACC, posterior medial cortex, and basal ganglia/putamen predicted both replay and replanning.
  - This is among the strongest empirical links between offline memory processes and the extra flexibility that vanilla SR lacks.

- **Hippocampal predictive-map correspondence**
  - [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]] synthesized evidence that hippocampal place fields have properties expected of SR-like predictive maps: barrier-related distortions, directional skew, and clustering near reward.
  - [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]] further showed in a biologically plausible model that STDP plus theta phase precession can rapidly learn an SR approximation.
  - Together, these make hippocampus the strongest current neural candidate for SR-like coding.

## Landmark papers

[[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] is the key bridge paper. It reframed “model-based vs model-free” as partly a question about representation, showing how TD learning over predictive features can mimic some supposedly model-based behavior.

[[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]] consolidated the field’s logic: why SR is computationally attractive, why hippocampal place fields look SR-like, and why dopamine might need reinterpretation as more than a scalar reward error.

[[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] moved the account toward mechanism by linking offline replay to later replanning in humans.

[[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] is a major extension and partial challenge. Its Default Representation retains the predictive-map intuition but is more flexible than standard SR, especially for policy revaluation and some detour updates.

[[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]] sharpened an important decomposition: a predictive map may not be enough. Goal information may be carried persistently by OFC, with hippocampus tracking current or successor-like state structure.

## Boundaries and tensions

Vanilla SR is not a general planning solution. It handles reward revaluation well, but transition revaluation and policy revaluation expose its dependence on cached occupancies learned under an earlier world model or policy [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

The neural locus is unresolved. Hippocampus has the clearest representational evidence, but the theory often assigns striatum a central computational role as the value-learning readout over SR features. Direct evidence that striatum itself stores an SR-like predictive map is thinner than the hippocampal evidence summarized in [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]].

The dopamine story is still speculative at the strongest level. The appealing proposal is that dopamine carries state- or feature-prediction errors sufficient to train SR-like representations [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]]. But that vector-valued error account remains largely untested, and alternative interpretations of mesolimbic dopamine emphasize causal association rather than TD reward prediction error [[raw/summaries/namboodiri2023_mesolimbic_dopamine_causal|Namboodiri et al. 2023]].

Replay helps, but the causal chain is incomplete. [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] is strong correlational evidence, not definitive proof that replay implements SR updates or prioritized sweeping in humans.

SR may also be too map-centric. [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]] argues that OFC maintains a persistent goal pointer distinct from hippocampal map-like coding. If that is right, flexible behavior may require at least two separable ingredients: predictive state structure and explicit goal representation.

Competing predictive-map formalisms matter. [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] shows that a policy-independent Default Representation can solve cases that defeat standard SR and may better fit grid-field stability under policy changes. So some results interpreted as “SR” may only support a broader family of predictive representations.

## Open questions

How much of the SR is represented in hippocampus, prefrontal cortex, or corticostriatal synapses, and how much is merely read out by striatum?

What exactly does dopamine teach in these circuits: scalar reward prediction error, sensory/state prediction error, unsigned surprise for replay prioritization, or something closer to causal contingency? Current evidence does not settle this.

When behavior is flexible after environmental change, is that due to online model-based recomputation, offline replay, or a more policy-independent predictive map such as the Default Representation?

How are goals injected into the predictive map? The OFC “goal pointer” proposal [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]] suggests a clean factorization between map and reward, but the circuit interaction with hippocampus and striatum is still mostly hypothetical.

Can SR-based accounts scale to partial observability, hidden-state inference, and stochastic transitions? These are explicit limitations of current formulations [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]].

If hippocampus learns predictive maps, which dopamine source matters most for plasticity there? The presence of both VTA input and locus-coeruleus-derived dopamine complicates any simple single-source teaching-signal story [[raw/summaries/mcnamara2017_dopamine_hippocampus|McNamara et al. 2017]].

## Key papers

- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] — defining computational bridge from TD learning to planning-like behavior via SR.
- [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]] — canonical synthesis of SR logic, hippocampal substrate arguments, and dopamine hypotheses.
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]] — strongest human evidence linking offline replay to replanning.
- [[raw/summaries/decothi2022_predictive_spatial_navigation|de Cothi et al. 2022]] — cross-species navigation evidence favoring SR-like predictive maps, with residual model-based behavior in humans.
- [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]] — biologically plausible hippocampal learning mechanism for SR approximation.
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray et al. 2020]] — important alternative/extension showing where standard SR is too limited.
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu et al. 2023]] — goal coding in OFC as a complement, and possible challenge, to pure predictive-map accounts.
- [[raw/summaries/namboodiri2023_mesolimbic_dopamine_causal|Namboodiri et al. 2023]] — strong challenge to simple dopamine-as-TD-error interpretations relevant to SR learning.

## Source papers
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] | [[raw/mds/russek2017_model_based_reinforcement|source md]]: Predictive representations can link model-based reinforcement learning to model-free mechanisms
- [[raw/summaries/momennejad2018_offline_replay_planning|Momennejad et al. 2018]]: Offline replay supports planning in human reinforcement learning
- [[raw/summaries/gershman2018_successor_representation_learning|Gershman 2018]] | [[raw/mds/gershman2018_successor_representation_learning|source md]]: The Successor Representation: Its Computational Logic and Neural Substrates
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu and Ito 2023]] | [[raw/mds/basu2023_goal_pointer_cognitive_map_ofc|source md]]: A goal pointer for a cognitive map in the orbitofrontal cortex
- [[raw/summaries/piray2020_linear_reinforcement_learning|Piray and Daw 2020]] | [[raw/mds/piray2020_linear_reinforcement_learning|source md]]: Linear reinforcement learning: Flexible reuse of computation in planning, grid fields, and cognitive control
- [[raw/summaries/decothi2022_predictive_spatial_navigation|Cothi et al. 2022]] | [[raw/mds/decothi2022_predictive_spatial_navigation|source md]]: Predictive maps in rats and humans for spatial navigation
- [[raw/summaries/george2022_stdp_predictive_maps|George et al. 2022]] | [[raw/mds/george2022_stdp_predictive_maps|source md]]: Rapid learning of predictive maps with STDP and theta phase precession
- [[raw/summaries/kaplan2018_active_inference_navigation|Kaplan and Friston 2018]] | [[raw/mds/kaplan2018_active_inference_navigation|source md]]: Planning and navigation as active inference
- [[raw/summaries/kravitz2010_basal_ganglia_optogenetic|Kravitz et al. 2010]] | [[raw/mds/kravitz2010_basal_ganglia_optogenetic|source md]]: Regulation of parkinsonian motor behaviours by optogenetic control of basal ganglia circuitry
- [[raw/summaries/mcnamara2017_dopamine_hippocampus|McNamara and Dupret 2017]] | [[raw/mds/mcnamara2017_dopamine_hippocampus|source md]]: Two sources of dopamine for the hippocampus
- [[raw/summaries/mizes2023_sensorimotor_striatum|Mizes et al. 2023]] | [[raw/mds/mizes2023_sensorimotor_striatum|source md]]: Dissociating the contributions of sensorimotor striatum to automatic and visually guided motor sequences
