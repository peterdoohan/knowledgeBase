---
title: "Reward-modulated hippocampal replay in spatial reinforcement learning"
subtopic_id: striatal_and_dopaminergic_reinforcement_learning__05
parent_topic_id: striatal_and_dopaminergic_reinforcement_learning
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:49:25.726341+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - ambrose2016_reverse_replay_hippocampal
  - foster2017_replay_memory_consolidation
  - singer2009_reward_reactivation_hippocampus
  - patai2021_versatile_wayfinder_prefrontal
  - findlay2021_replay_wake_sleep
core_papers:
  - ambrose2016_reverse_replay_hippocampal
  - baram2021_entorhinal_ventromedial_rl
  - findlay2021_replay_wake_sleep
  - foster2017_replay_memory_consolidation
  - moneta2024_ofc_vmpfc_representational_spaces
  - nyberg2022_spatial_goal_coding
  - patai2021_versatile_wayfinder_prefrontal
  - singer2009_reward_reactivation_hippocampus
---

# Reward-modulated hippocampal replay in spatial reinforcement learning

The cleanest result in this area is not that “replay supports navigation” in general, but that awake hippocampal sharp-wave ripple (SWR) replay is selectively shaped by reward, especially in reverse sequence order after outcomes. That pattern fits a credit-assignment role better than a simple memory-rehearsal account, while forward replay looks comparatively less reward-sensitive and more compatible with prospective evaluation or planning. Still, the bridge from hippocampal replay to striatal/dopaminergic reinforcement learning remains mostly inferential: the strongest data show reward-sensitive replay in hippocampus, not direct dopamine-mediated value updating.

## Current view

Awake hippocampal replay is now best viewed as rapid sampling from a learned spatial model, not as a passive recapitulation of recent experience or a phenomenon confined to sleep [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]].

Within that broader shift, reward modulation is one of the most robust functional signatures. Reward increases SWR occurrence and the reactivation of task-relevant place-cell ensembles, especially around rewarded outcomes [[raw/summaries/singer2009_reward_reactivation_hippocampus|Singer and Frank 2009]].

Direction matters. Reverse replay is the strongest candidate mechanism for retrospective credit assignment because it is selectively sensitive to reward magnitude changes, whereas forward replay is comparatively insensitive in the same behavioral context [[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]].

This directional dissociation maps naturally onto RL-style ideas: reverse replay resembles backward propagation of outcome information; forward replay better fits prospective search, retrieval, or planning. But that mapping is still interpretive rather than decisive, because replay can also generate remote and novel trajectories, which pushes the phenomenon beyond simple temporal-difference backup accounts toward cognitive-map or model-based views [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]].

Circuit-level integration with striatum, dopamine, and prefrontal cortex is plausible but underspecified. Reviews place replay within larger hippocampal-prefrontal-striatal systems for navigation and value-based control, but direct evidence that specific replay events train striatal values via dopaminergic teaching signals is still thin in this literature set [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]].

## Strongest evidence

[[raw/summaries/singer2009_reward_reactivation_hippocampus|Singer and Frank 2009]] provides the clearest early evidence that reward gates hippocampal reactivation itself, not just ongoing behavior.

- In CA3, rewarded trials showed higher wake SWR rate, greater principal-cell activity during SWRs, and higher activation probability per SWR than unrewarded trials.
- These effects survived time-control analyses, arguing against a trivial dwell-time explanation.
- Reactivation was structured: place cells on reward-associated paths were preferentially reactivated, and relevant cell pairs coactivated more often.
- The effect was stronger when animals were learning new reward associations than when reward contingencies were already familiar.

That pattern is hard to reconcile with replay as a simple echo of recent firing. It is much easier to reconcile with outcome-gated prioritization of behaviorally relevant trajectories.

[[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]] is the strongest directional dissociation paper.

- Increasing reward at one end of a linear track increased SWRs and replay overall; removing reward decreased both.
- Critically, reverse replay tracked reward increases and decreases, while forward replay did not materially change in either manipulation.
- The effect was relative, not merely absolute: changing reward at one end shifted reverse replay toward that end and away from the unchanged alternative.
- Because forward and reverse events were measured during the same stopping periods, the dissociation is not easily explained by gross behavioral confounds.

This is the best evidence here that replay direction carries computational meaning: reverse replay is the component most tightly linked to reward learning.

The review synthesis in [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] and [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] strengthens that interpretation by showing that replay is often immediate, awake, compressed, and sometimes novel or remote. Reward therefore appears to bias access to an internal spatial model rather than merely amplifying a recent sensory-motor trace.

## Landmark papers

- [[raw/summaries/singer2009_reward_reactivation_hippocampus|Singer and Frank 2009]]  
  Established that rewarded outcomes enhance hippocampal wake-SWR reactivation, including structured coactivation of task-relevant place cells.

- [[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]]  
  Showed that reverse, but not forward, replay is selectively modulated by reward magnitude, making the strongest case for replay-direction dissociation in RL terms.

- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]]  
  Reframed replay from memory consolidation toward online use of a learned spatial model for planning, learning, and decision-making.

- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]]  
  Integrated replay findings with modern RL accounts, emphasizing prioritized access to memories and the special status of reverse replay in outcome-related learning.

## Boundaries and tensions

The central limitation is causal. These studies show that reward modulates replay, not that replay is necessary or sufficient for downstream value updating in striatum or cortex.

The dopamine link remains indirect. [[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]] is highly compatible with dopaminergic RL accounts, but it did not record dopamine neurons or manipulate dopamine. [[raw/summaries/singer2009_reward_reactivation_hippocampus|Singer and Frank 2009]] likewise left the neuromodulatory mechanism unresolved.

Replay detection is a real methodological fault line. [[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]] detected replay in only a minority of SWRs, and [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] emphasizes that replay scoring and false-positive rates vary substantially across methods. Claims about proportions and subtype frequencies should be treated cautiously.

Reverse-versus-forward is useful, but probably not exhaustive. The reward sensitivity of reverse replay is one of the most reproducible distinctions, yet reviews still argue that SWRs may be multifunctional and that event classes are not cleanly separated [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]].

Model interpretation is underdetermined. Reverse replay fits TD-like backup intuitions, but the same literature also shows replay can be generative, remote, and novel. That broader phenomenology is more compatible with cognitive-map, successor-like, or model-based mechanisms than with a purely model-free account [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]].

Prefrontal and entorhinal work suggests that navigation and RL rely on structured state representations extending beyond hippocampus [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]]. But those results do not by themselves show how reward-modulated hippocampal replay is read out or used online.

## Open questions

- What neuromodulatory signal actually gates reward-sensitive replay: dopamine, acetylcholine, both, or task-dependent combinations?
- Does reverse replay causally drive value updating in striatum or vmPFC/OFC, or is it an accompanying marker of a broader learning state?
- What determines whether a post-outcome SWR contains reverse replay, forward replay, or no decodable replay at all?
- Are forward and reverse replay generated by distinct circuit mechanisms, or are they different biases on a common SWR process?
- How are replay contents selected from a cognitive map when trajectories can be remote, novel, or counterfactual?
- How do hippocampal replay events interact with prefrontal route planning and latent-state inference during detours, foraging, or changing goals [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]]?
- Can reward-modulated spatial replay be unified with nonspatial state-space coding in entorhinal and ventromedial prefrontal cortex, or are these parallel but partially separate mechanisms [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]]?
- How much of the apparent computational specialization of replay depends on detection thresholds and decoder assumptions rather than biology?

## Key papers

- [[raw/summaries/singer2009_reward_reactivation_hippocampus|Singer and Frank 2009]] — Reward enhances wake-SWR reactivation of task-relevant hippocampal ensembles, especially during new reward learning.
- [[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]] — Reverse replay, but not forward replay, tracks reward magnitude changes.
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] — Replay is better understood as sampling from a learned spatial model than as simple consolidation.
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] — Modern synthesis linking replay to RL-style prioritized memory access and emphasizing methodological caveats.
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] — Circuit context for how hippocampus interacts with prefrontal systems during value-guided navigation.
- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] — Relevant broader evidence that entorhinal/vmPFC systems encode abstract RL structure, supporting map-like interpretations of replay-guided learning.

## Source papers
- [[raw/summaries/ambrose2016_reverse_replay_hippocampal|Ambrose et al. 2016]] | [[raw/mds/ambrose2016_reverse_replay_hippocampal|source md]]: Reverse Replay of Hippocampal Place Cells Is Uniquely Modulated by Changing Reward
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] | [[raw/mds/foster2017_replay_memory_consolidation|source md]]: Replay Comes of Age
- [[raw/summaries/singer2009_reward_reactivation_hippocampus|Singer and Frank 2009]] | [[raw/mds/singer2009_reward_reactivation_hippocampus|source md]]: Rewarded Outcomes Enhance Reactivation of Experience in the Hippocampus
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] | [[raw/mds/patai2021_versatile_wayfinder_prefrontal|source md]]: The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] | [[raw/mds/findlay2021_replay_wake_sleep|source md]]: The evolving view of replay and its functions in wake and sleep
- [[raw/summaries/baram2021_entorhinal_ventromedial_rl|Baram et al. 2021]] | [[raw/mds/baram2021_entorhinal_ventromedial_rl|source md]]: Entorhinal and ventromedial prefrontal cortices abstract and generalize the structure of reinforcement learning problems
- [[raw/summaries/moneta2024_ofc_vmpfc_representational_spaces|Moneta et al. 2024]] | [[raw/mds/moneta2024_ofc_vmpfc_representational_spaces|source md]]: Representational spaces in orbitofrontal and ventromedial prefrontal cortex: task states, values, and beyond
- [[raw/summaries/nyberg2022_spatial_goal_coding|Nyberg et al. 2022]] | [[raw/mds/nyberg2022_spatial_goal_coding|source md]]: Spatial goal coding in the hippocampal formation
