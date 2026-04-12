---
title: "Hippocampal sharp-wave ripple replay and prefrontal coordination during planning"
subtopic_id: hippocampal_prefrontal_coordination_and_planning__03
parent_topic_id: hippocampal_prefrontal_coordination_and_planning
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:47:50.824935+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - jadhav2016_hippocampal_prefrontal_swr
  - bernerslee2021_prefrontal_cortex_hippocampal
  - wikenheiser2015_theta_sequences_goals
  - findlay2021_replay_wake_sleep
  - jensen2024_recurrent_planning_hippocampal_replay
core_papers:
  - bernerslee2021_prefrontal_cortex_hippocampal
  - buzsaki2015_hippocampal_sharp_wave_ripple
  - findlay2021_replay_wake_sleep
  - foster2017_replay_memory_consolidation
  - gillespie2021_replay_past_experiences
  - gridchyn2020_replay_selective_memory
  - jadhav2016_hippocampal_prefrontal_swr
  - jensen2024_recurrent_planning_hippocampal_replay
related_wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/sharp_wave_ripple_associated_hippocampal_replay
---

# Hippocampal sharp-wave ripple replay and prefrontal coordination during planning

The clearest evidence that hippocampus–prefrontal interactions support planning comes from awake sharp-wave ripple (SWR) events, not from place coding per se. During awake immobility, hippocampal replay is coupled to structured medial prefrontal cortex (mPFC) ensemble responses, and a subset of PFC neurons is selective for the content of non-local hippocampal representations rather than the animal’s actual location. This supports a view in which replay can transiently route candidate or remembered trajectories into prefrontal population states relevant for memory-guided choice. But the literature does not justify a simple “replay = upcoming plan” claim: causal direction is unresolved, replay content is not uniformly choice-predictive, and some prefrontal replay-like activity can occur independently of hippocampal replay.

## Current view

Awake hippocampal SWRs are a major coordination window between CA1 and PFC. The best-supported claim is that these events reactivate cross-structural ensemble relationships formed during behavior, rather than merely replaying hippocampal trajectories in isolation [[raw/summaries/jadhav2016_hippocampal_prefrontal_swr|Jadhav et al. 2016]].

PFC does not just register that an SWR happened. A subset of PFC neurons is tuned to what hippocampus is representing during replay, especially non-local spatial content. This sharpens the planning interpretation: the relevant signal is replay content, not ripple occurrence alone [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]].

Planning-related non-local representation is not confined to SWRs. During movement, hippocampal theta sequences also show goal-dependent look-ahead. This suggests that prospective coding exists in at least two regimes: online theta sequences during action and off-line SWR replay during pauses [[raw/summaries/wikenheiser2015_theta_sequences_goals|Wikenheiser and Redish 2015]].

A reasonable synthesis is that hippocampus generates candidate/non-local state trajectories, while PFC selects, contextualizes, or gates them for behavioral use. That synthesis is plausible, but still mostly inferential. Direct evidence that SWR-linked hippocampus→PFC coordination causes a specific planned choice remains limited.

## Strongest evidence

- [[raw/summaries/jadhav2016_hippocampal_prefrontal_swr|Jadhav et al. 2016]] provides the strongest direct awake SWR coordination result.
  - 35% of recorded PFC neurons were significantly SWR-modulated.
  - Awake SWRs drove both excitation and inhibition in PFC, roughly equally, unlike the mostly excitatory picture often emphasized for sleep SWRs.
  - CA1 population activity peaked before PFC responses (mean latencies: CA1 54 ms; SWR-excited PFC 100 ms; SWR-inhibited PFC 84 ms).
  - 16% of CA1–PFC pairs were significantly SWR-correlated versus ~5% expected by chance.
  - SWR coupling mirrored theta-state co-activity during movement, arguing that awake SWRs reinstate experience-linked hippocampus–PFC ensemble structure.
  - Critically, inhibition was structured rather than nonspecific: PFC cells were most suppressed when replay content was inconsistent with their preferred representation.

- [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]] shows that some PFC neurons are selective for replay content itself.
  - 18.5% of PFC neurons were significantly differentially modulated by replay of different maze arms, well above chance.
  - PFC population activity decoded hippocampal replay arm identity above chance.
  - Replay selectivity in PFC exceeded what could be predicted from the same neurons’ behavioral arm selectivity, arguing against a simple “PFC reactivates its own recent spatial firing” account.
  - The same general principle extended beyond rest: PFC neurons tracked non-local hippocampal representations during behavior as well, linking replay to a broader hippocampus–PFC non-local coding regime.

- [[raw/summaries/wikenheiser2015_theta_sequences_goals|Wikenheiser and Redish 2015]] is not an SWR-PFC paper, but it is important because it shows that hippocampal prospective sequencing scales with intended goal distance on single trials. That strengthens the interpretation that hippocampal non-local sequences can carry plan-relevant information, even if the PFC coordination piece was not directly tested there.

- Reviews such as [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] and [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] support the broader conceptual shift: replay is wake-active, often generative, and not reducible to sleep consolidation. This matters because planning accounts are much more plausible under a wake-active, generative replay framework than under a pure rehearsal framework.

## Landmark papers

- [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsáki 2015]]
  - Established SWRs as a central systems-level event for episodic memory and planning, helping define the phenomenon worth mechanistically explaining.

- [[raw/summaries/jadhav2016_hippocampal_prefrontal_swr|Jadhav et al. 2016]]
  - First strong evidence that awake SWRs coordinate structured excitation and inhibition in PFC ensembles, not just hippocampal replay.

- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]]
  - Consolidated the field’s move away from “replay as simple recapitulation” toward replay as sampling from an internal model with decision relevance.

- [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]]
  - Showed that PFC neurons can be selective for non-local hippocampal content itself, tightening the link between replay and decision variables.

- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]]
  - Synthesized the evidence that replay is wake-active, heterogeneous, and compatible with reinforcement-learning accounts.

## Boundaries and tensions

Replay is not uniformly prospective. [[raw/summaries/gillespie2021_replay_past_experiences|Gillespie et al. 2021]] reported that awake hippocampal replay in a dynamic spatial memory task was decoupled from subsequent choice and instead emphasized previously rewarded and non-recently visited locations. That is a real constraint on strong planning-only accounts.

The direction of influence is unresolved. In [[raw/summaries/jadhav2016_hippocampal_prefrontal_swr|Jadhav et al. 2016]], CA1 tended to lead PFC, but the data were correlational and did not exclude bidirectional interactions. The anatomical routing is also unclear because dorsal CA1 was sampled heavily despite weak direct dorsal CA1→PFC projections.

Not all prefrontal replay-like activity appears hippocampus-locked. [[raw/summaries/kaefer2020_mpfc_replay_ruleswitching|Kaefer et al. 2020]] found mPFC replay of generalized spatial sequences during rule switching that was reported to occur independently of concurrent hippocampal replay. This suggests that PFC can generate temporally structured non-local representations without being a passive readout of hippocampal SWRs.

SWR replay and theta sequences should not be collapsed. Both can carry non-local, goal-related information, but they occur in different behavioral states and may serve different computations. The current evidence does not cleanly map “theta = online planning” and “SWR = offline planning” onto distinct causal roles.

Methodology remains a serious issue. Replay detection depends strongly on Bayesian decoding choices, significance tests, and event definitions; false-positive rates are hard to estimate and different methods do not always agree [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]].

Normative RL accounts are attractive but not decisive. Models in which replay acts as prioritized backup or rollout-based planning explain many phenomenological features, but they do not yet identify the biological circuit mechanism of hippocampus–PFC coordination [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]].

## Open questions

- When does SWR replay influence the next choice, and when does it mainly stabilize memory?
- Which hippocampal pathway actually drives PFC during awake SWRs: dorsal CA1 indirectly, ventral/intermediate hippocampus, thalamic relays, or multi-step loops?
- What interneuron and cell-type mechanisms generate the structured excitation and inhibition seen in PFC during SWRs?
- Do PFC states merely read out replay content, or can PFC bias which hippocampal sequences are replayed?
- How are theta-sequence prospective signals integrated with SWR replay across a trial?
- How does learning stage matter? Existing replay-content work in PFC was done early in learning; it is unclear whether coupling strengthens, weakens, or becomes more abstract with expertise [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]].
- Can causal perturbations targeted to specific replay content, rather than SWRs globally, show a selective effect on planning variables in PFC and behavior?

## Key papers

- [[raw/summaries/jadhav2016_hippocampal_prefrontal_swr|Jadhav et al. 2016]] — strongest direct evidence for awake SWR-linked CA1–PFC ensemble coordination.
- [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]] — PFC neurons are selective for non-local hippocampal replay content.
- [[raw/summaries/wikenheiser2015_theta_sequences_goals|Wikenheiser and Redish 2015]] — hippocampal theta sequences reflect current goals; important adjacent evidence for prospective non-local coding.
- [[raw/summaries/gillespie2021_replay_past_experiences|Gillespie et al. 2021]] — key counterpoint showing replay need not predict subsequent choice.
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] — best concise review of the modern, wake-active, generative replay view.
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] — influential synthesis arguing replay exceeds simple memory consolidation.
- [[raw/summaries/kaefer2020_mpfc_replay_ruleswitching|Kaefer et al. 2020]] — evidence that mPFC can replay generalized sequences independently of hippocampal replay.
- [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] — computational account linking forward replay to rollout-based planning, useful but not yet direct circuit evidence.

## Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]: Crosslink via replay: from Page A to Page B for the theoretical interpretation of replay as predictive/non-local state representation, and from Page B to Page A for evidence that replay interfaces with prefrontal planning circuits during choice.
- [[wiki/topics/sharp_wave_ripple_associated_hippocampal_replay|Sharp-wave ripple-associated hippocampal replay]]: From Page B, link to Page A as the main page on prefrontal coordination and planning-related interpretation of replay; from Page A, link back to Page B for the underlying SWR/replay phenomenon, methods, and broader evidence base.

## Source papers
- [[raw/summaries/jadhav2016_hippocampal_prefrontal_swr|Jadhav et al. 2016]] | [[raw/mds/jadhav2016_hippocampal_prefrontal_swr|source md]]: Coordinated Excitation and Inhibition of Prefrontal Ensembles during Awake Hippocampal Sharp-Wave Ripple Events
- [[raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal|Berners-Lee et al. 2021]] | [[raw/mds/bernerslee2021_prefrontal_cortex_hippocampal|source md]]: Prefrontal Cortical Neurons Are Selective for Non-Local Hippocampal Representations during Replay and Behavior
- [[raw/summaries/wikenheiser2015_theta_sequences_goals|Wikenheiser and Redish 2015]] | [[raw/mds/wikenheiser2015_theta_sequences_goals|source md]]: Hippocampal theta sequences reflect current goals
- [[raw/summaries/findlay2021_replay_wake_sleep|Findlay et al. 2021]] | [[raw/mds/findlay2021_replay_wake_sleep|source md]]: The evolving view of replay and its functions in wake and sleep
- [[raw/summaries/jensen2024_recurrent_planning_hippocampal_replay|Jensen et al. 2024]] | [[raw/mds/jensen2024_recurrent_planning_hippocampal_replay|source md]]: A recurrent network model of planning explains hippocampal replay and human behavior
- [[raw/summaries/buzsaki2015_hippocampal_sharp_wave_ripple|Buzsaki 2015]] | [[raw/mds/buzsaki2015_hippocampal_sharp_wave_ripple|source md]]: Hippocampal Sharp Wave-Ripple: A Cognitive Biomarker for Episodic Memory and Planning
- [[raw/summaries/foster2017_replay_memory_consolidation|Foster 2017]] | [[raw/mds/foster2017_replay_memory_consolidation|source md]]: Replay Comes of Age
- [[raw/summaries/gillespie2021_replay_past_experiences|Gillespie et al. 2021]] | [[raw/mds/gillespie2021_replay_past_experiences|source md]]: Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice
- [[raw/summaries/gridchyn2020_replay_selective_memory|Gridchyn et al. 2020]] | [[raw/mds/gridchyn2020_replay_selective_memory|source md]]: Assembly-Specific Disruption of Hippocampal Replay Leads to Selective Memory Deficit
