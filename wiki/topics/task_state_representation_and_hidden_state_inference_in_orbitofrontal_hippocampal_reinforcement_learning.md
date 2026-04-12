---
title: "Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning"
subtopic_id: striatal_and_dopaminergic_reinforcement_learning__02
parent_topic_id: striatal_and_dopaminergic_reinforcement_learning
page_type: topic
page_worthiness: 3
status: draft_llm
generated_at: "2026-04-12T19:50:33.963572+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - wilson2013_ofc_cognitive_map
  - wikenheiser2016_cognitive_maps_hippocampus
  - niv2019_representation_learning_task_states
  - odoherty2017_learning_reward_decision
  - mishchanchuk2024_hidden_state_inference
core_papers:
  - badre2019_hierarchical_cognitive_control_lobes
  - botvinick2008_hierarchical_behavior_prefrontal
  - botvinick2012_planning_inference
  - botvinick2020_deep_reinforcement_learning_neuro
  - haber2000_striatonigrostriatal_pathways
  - janssen2022_hierarchical_rl_motor_sequences
  - jeong2022_mesolimbic_dopamine_causal
  - jiang2022_learning_options_compression
---

# Task-state representation and hidden-state inference in orbitofrontal–hippocampal reinforcement learning

In this slice of reinforcement learning, the central problem is often not value updating but state construction: animals must infer which latent task state they are in when sensory input alone is insufficient. The best-supported synthesis is that orbitofrontal cortex (OFC) represents abstract task states or belief-like pointers to the current situation, while hippocampus contributes contextual/relational codes that can support hidden-state inference; these representations then shape downstream striatal learning and dopamine prediction errors. This is more directly supported than broad claims about hierarchical RL or options in these circuits, though the OFC–hippocampus division of labor and the circuit path into dopamine remain unsettled.

## Current view

Partially observable RL appears to depend heavily on internal state representations. In this literature, OFC is not primarily framed as a generic value area, but as a representation of the current task state when that state depends on memory, context, or inferred latent structure [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]].

Hippocampus is increasingly treated as a partner in this process rather than a purely spatial system. Reviews argue that hippocampus and OFC encode complementary cognitive maps: hippocampus emphasizes relational, spatial, and contextual structure, while OFC emphasizes task-relevant, outcome-linked state identity [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]].

For striatal and dopaminergic RL, the implication is specific: prediction errors are computed over the state representation the animal is using. If the animal infers a latent context, dopamine can look like an inference-conditioned RPE rather than a flat-state Q-learning error [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]].

This topic aligns more closely with model-based RL, Bayesian latent-cause inference, and belief-state accounts than with classical hierarchical RL or options. The key empirical question is hidden-state inference, not temporal abstraction per se [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]] [[raw/summaries/odoherty2017_learning_reward_decision|O'Doherty et al. 2017]].

## Strongest evidence

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] gave the clearest mechanistic OFC account.
  - A model with explicit hidden/task-state representation reproduced classic control behavior in reversal learning, delayed alternation, extinction, and devaluation.
  - A single-state version reproduced the pattern of impairments seen after OFC lesions.
  - The strength here is explanatory compression across tasks.
  - The limitation is equally clear: this paper is mainly computational/theoretical, not direct neural evidence for OFC state coding.

- [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]] is the strongest direct causal evidence in the provided set.
  - In probabilistic reversal, all mice were better fit by hidden-state/state-inference models than by Q-learning.
  - Ventral CA1 lesions impaired performance and selectively reduced state-inference-consistent choices.
  - Unilateral ventral CA1 lesions removed hidden-state signatures from ipsilateral nucleus accumbens dopamine.
  - Population activity in ventral CA1 represented the two abstract latent contexts.
  - This is unusually strong because behavior, neural representation, causality, and dopamine all line up in one task.
  - Main caveats: small samples and unresolved downstream pathway.

- [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]] sharpened the computational problem.
  - It argues that RL in complex tasks requires learning low-dimensional task states via selective attention and latent-cause inference.
  - It also places OFC as the likely locus of abstract task-state representation.
  - This is an important synthesis, but it is still a perspective rather than a decisive empirical test.

- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] and [[raw/summaries/odoherty2017_learning_reward_decision|O'Doherty et al. 2017]] converge on a distributed-map view.
  - Hippocampus: relational/contextual map.
  - OFC: abstract current state and outcome identity.
  - Striatum/dopamine: value learning conditioned on those maps.
  - Useful synthesis, but mostly review-level support.

## Landmark papers

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]]
  - Landmark for reframing OFC as a cognitive map of task space rather than a simple value signal.
  - Important because it explains why OFC lesions spare simple learning but impair tasks requiring hidden-state disambiguation.

- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]]
  - Landmark for explicitly pairing hippocampus and OFC as interacting cognitive maps.
  - Helped move the field away from a hippocampus=space / OFC=value caricature.

- [[raw/summaries/odoherty2017_learning_reward_decision|O'Doherty et al. 2017]]
  - Landmark systems-level synthesis placing OFC and hippocampus inside a distributed model-based RL architecture.
  - Useful for linking task-state representation to striatal and dopaminergic learning rather than treating it as an isolated cortical phenomenon.

- [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]]
  - Landmark for making state-representation learning itself the core RL problem.
  - Especially influential in tying latent-cause inference and attention to OFC-centered task-state representations.

- [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]]
  - Landmark empirical paper showing that abstract hidden-state inference can be causally dependent on ventral hippocampus and can shape dopamine signals.

## Boundaries and tensions

The OFC account is compelling, but in the provided literature it is stronger as a unifying theory than as direct causal neural evidence. [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] explicitly noted this gap, and [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]] did not close it.

The hippocampal story is currently more causal in this narrow domain than the OFC story. [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]] directly implicates ventral CA1 in abstract hidden-state inference, but it does not show whether hippocampus computes the belief update, stores contextual structure, or simply supplies a context code used elsewhere.

Division of labor remains fuzzy. Reviews present hippocampus and OFC as complementary maps [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]], but the operational boundary between “relational/contextual” and “task-state/outcome-linked” representations is not yet crisp.

This literature is narrower than hierarchical RL in the options sense. It supports latent-state representation and inference under partial observability, not a broad claim that OFC–hippocampal circuits implement temporal abstraction or option discovery.

The dopamine result is important but bounded. [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]] shows that accumbens dopamine can reflect hidden-state-inference RPEs in one reversal paradigm. That does not by itself settle the broader theory of dopamine across tasks.

Behavioral identifiability is a persistent problem. Subjects can often solve nominally identical tasks with different internal state spaces, making neural interpretation under-constrained [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]].

## Open questions

- How are latent task states learned online, trial by trial, rather than merely represented once established [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]]?
- What exactly is computed in OFC versus hippocampus during hidden-state inference: belief update, context retrieval, outcome tagging, or all of these?
- Through which pathway do hippocampal context representations influence striatal dopamine: direct hippocampus→NAc routes, prefrontal intermediates, or broader loops [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]]?
- Are OFC and hippocampus representing the same latent states in different formats, or genuinely different variables?
- How are state prediction errors generated and used to update the task model in cortical circuits [[raw/summaries/odoherty2017_learning_reward_decision|O'Doherty et al. 2017]]?
- Which task designs can cleanly separate hidden-state inference from simpler heuristics or recency-weighted RL?
- How general is the ventral hippocampus result outside reversal-style tasks and beyond two-state environments?

## Key papers

- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] — core OFC “cognitive map of task space” theory.
- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser et al. 2016]] — hippocampus and OFC as complementary cognitive maps.
- [[raw/summaries/odoherty2017_learning_reward_decision|O'Doherty et al. 2017]] — distributed model-based RL architecture linking map-like state representations to striatal and dopaminergic learning.
- [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]] — task-state learning via attention and latent-cause inference.
- [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]] — causal evidence that ventral hippocampus supports abstract hidden-state inference and shapes dopamine signals.

## Source papers
- [[raw/summaries/wilson2013_ofc_cognitive_map|Wilson et al. 2014]] | [[raw/mds/wilson2013_ofc_cognitive_map|source md]]: Orbitofrontal Cortex as a Cognitive Map of Task Space
- [[raw/summaries/wikenheiser2016_cognitive_maps_hippocampus|Wikenheiser and Schoenbaum 2016]] | [[raw/mds/wikenheiser2016_cognitive_maps_hippocampus|source md]]: Over the river, through the woods: cognitive maps in the hippocampus and orbitofrontal cortex
- [[raw/summaries/niv2019_representation_learning_task_states|Niv 2019]] | [[raw/mds/niv2019_representation_learning_task_states|source md]]: Learning task-state representations
- [[raw/summaries/odoherty2017_learning_reward_decision|O'Doherty et al. 2017]] | [[raw/mds/odoherty2017_learning_reward_decision|source md]]: Learning, Reward, and Decision Making
- [[raw/summaries/mishchanchuk2024_hidden_state_inference|Mishchanchuk et al. 2024]] | [[raw/mds/mishchanchuk2024_hidden_state_inference|source md]]: Hidden state inference requires abstract contextual representations in ventral hippocampus
- [[raw/summaries/badre2019_hierarchical_cognitive_control_lobes|Badre and Desrochers 2019]] | [[raw/mds/badre2019_hierarchical_cognitive_control_lobes|source md]]: Hierarchical cognitive control and the frontal lobes
- [[raw/summaries/botvinick2008_hierarchical_behavior_prefrontal|Botvinick 2008]] | [[raw/mds/botvinick2008_hierarchical_behavior_prefrontal|source md]]: Hierarchical models of behavior and prefrontal function
- [[raw/summaries/botvinick2012_planning_inference|Botvinick and Toussaint 2012]] | [[raw/mds/botvinick2012_planning_inference|source md]]: Planning as inference
- [[raw/summaries/botvinick2020_deep_reinforcement_learning_neuro|Botvinick et al. 2020]] | [[raw/mds/botvinick2020_deep_reinforcement_learning_neuro|source md]]: Deep Reinforcement Learning and Its Neuroscientific Implications
- [[raw/summaries/haber2000_striatonigrostriatal_pathways|Haber et al. 2000]] | [[raw/mds/haber2000_striatonigrostriatal_pathways|source md]]: Striatonigrostriatal Pathways in Primates Form an Ascending Spiral from the Shell to the Dorsolateral Striatum
- [[raw/summaries/janssen2022_hierarchical_rl_motor_sequences|Janssen et al. 2022]] | [[raw/mds/janssen2022_hierarchical_rl_motor_sequences|source md]]: Hierarchical Reinforcement Learning, Sequential Behavior, and the Dorsal Frontostriatal System
- [[raw/summaries/jeong2022_mesolimbic_dopamine_causal|Jeong et al. 2022]] | [[raw/mds/jeong2022_mesolimbic_dopamine_causal|source md]]: Mesolimbic dopamine release conveys causal associations
- [[raw/summaries/jiang2022_learning_options_compression|Jiang et al. 2022]] | [[raw/mds/jiang2022_learning_options_compression|source md]]: Learning Options via Compression
