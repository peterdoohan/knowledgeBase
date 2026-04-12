---
title: "Prospective spatial coding in hippocampal–medial prefrontal circuits"
subtopic_id: hippocampal_prefrontal_coordination_and_planning__02
parent_topic_id: hippocampal_prefrontal_coordination_and_planning
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:48:16.939923+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - ito2015_prefrontal_thalamic_hippocampus
  - hok2005_goal_coding_prefrontal
  - avigan2020_spatial_learning_hippocampus
  - russek2017_model_based_reinforcement
  - jones2005_theta_hippocampal_prefrontal
core_papers:
  - avigan2020_spatial_learning_hippocampus
  - basu2023_goal_pointer_cognitive_map_ofc
  - denbakker2023_sharp_wave_prefrontal_rule
  - denbakker2024_mpfc_spatial_swr
  - hasz2020_spatial_encoding_deliberation
  - hok2005_goal_coding_prefrontal
  - hok2013_prefrontal_place_cells
  - huang2024_hippocampal_theta_goal_distance
related_wiki_pages:
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory
---

# Prospective spatial coding in hippocampal–medial prefrontal circuits

The strongest current claim is narrower than “the hippocampal–prefrontal circuit plans routes.” What is well supported is that, during memory-guided navigation, hippocampal CA1 and medial prefrontal cortex (mPFC) can represent future-relevant spatial variables—upcoming trajectory, goal location, or impending choice—and that their coordination increases at behaviorally critical moments. The best causal evidence points to an mPFC→nucleus reuniens (NR)→CA1 pathway as necessary for prospective CA1 trajectory coding [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]. Theta-band coupling is the clearest online coordination signature [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]]. But the literature does not support a single unified mechanism: some mPFC prospective signals are SWR-independent [[raw/summaries/denbakker2024_mpfc_spatial_swr|den Bakker et al. 2024]], some hippocampal goal-related coding survives mPFC inactivation after overtraining [[raw/summaries/hok2013_prefrontal_place_cells|Hok et al. 2013]], and neural effects can be larger than behavioral effects on simple tasks [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].

## Current view

Prospective spatial coding in this circuit is best viewed as a family of related phenomena, not a single code.

CA1 often carries trajectory-dependent activity before the choice point, especially in tasks that require remembering an intended turn or route. mPFC carries complementary signals about goals, trajectories, and upcoming choices. On current evidence, mPFC is not just reading out hippocampal state; it can shape hippocampal prospective coding via thalamic relay through NR [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].

Coordination is state-dependent. During working-memory and choice epochs, CA1–mPFC theta synchrony, spike coupling, and prefrontal phase-locking to hippocampal theta all increase, and they weaken on error trials [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]]. That makes theta the strongest candidate mechanism for online exchange during deliberation and action selection.

mPFC prospective coding is not reducible to generic “space cells.” Early work showed PL/IL neurons concentrated firing near behaviorally relevant goal locations rather than uniformly tiling space [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]]. More recent work suggests dmPFC can predict when hippocampus will enter a non-local, prospective encoding mode, while hippocampal goal-location representations can rapidly modulate reward-related coding in dmPFC on theta timescales [[raw/summaries/hasz2020_spatial_encoding_deliberation|Hasz et al. 2020]].

A reasonable computational framing is predictive representation rather than full symbolic planning. Successor-representation accounts provide useful language for future occupancy coding and partial flexibility, but they do not by themselves identify where the code lives or whether mPFC/CA1 signals are explicit SRs rather than mixed-selective, task-shaped predictors [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

## Strongest evidence

- **Causal circuit evidence for prospective CA1 coding**: On a T-maze, 55.1% of CA1 stem place cells were trajectory-dependent versus 17.7% in CA3. NR and mPFC also carried trajectory signals (42.2% and 38.2% of cells, respectively). NR lesions reduced trajectory-dependent CA1 cells to 15.9%, and acute NR silencing reduced them from 72% to 44% on laser trials, reversibly [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]. This is the clearest evidence that prefrontal input, relayed through thalamus, is required for CA1 prospective route coding.

- **Prospective rather than retrospective content**: In the same study, trajectory decoding on error trials supported a predominantly forward-looking interpretation rather than a mere memory trace of the previous lap [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].

- **Choice-specific theta coordination**: During a spatial alternation task, CA1–mPFC spike correlations were higher during choice than forced-turn runs on the same maze section, mPFC neurons phase-locked more strongly to CA1 theta, and CA1–mPFC theta coherence increased on correct choice runs but dropped on errors [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]]. This is strong correlational evidence that online cross-area coupling is behaviorally relevant.

- **Goal coding in mPFC**: In PL/IL, about 25% of neurons had spatial correlates, and ~77% of valid fields clustered near the two fixed goal-related locations rather than being evenly distributed. These effects were not explained by speed or simple reward-consumption confounds [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]]. This remains a foundational result for prefrontal spatial goal representation.

- **Bidirectional, multiscale deliberation coupling**: Simultaneous dmPFC–CA1 recordings showed that dmPFC activity predicts whether hippocampus enters a prospective non-local encoding mode over seconds, while hippocampal goal-location representations drive fast, theta-cycle-locked increases in reward encoding in dmPFC [[raw/summaries/hasz2020_spatial_encoding_deliberation|Hasz et al. 2020]]. This argues against a purely one-way hippocampus→PFC story.

- **Behavioral necessity of hippocampal–prefrontal interaction for flexible spatial memory**: Crossed inactivation of mPFC with either dorsal or ventral hippocampus impaired discrimination/reversal learning [[raw/summaries/avigan2020_spatial_learning_hippocampus|Avigan et al. 2020]], and contralateral dHPC–PFC inactivation impaired spatial working-memory learning but not reference memory learning [[raw/summaries/maharjan2018_dorsal_hippocampal_prefrontal_spatial_learning|Maharjan et al. 2018]]. These studies do not isolate prospective codes, but they show the interaction matters behaviorally.

- **SWR-related update signals are real but not the whole story**: mPFC inhibition timed to hippocampal SWRs impaired spatial rule switching [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]], yet the mPFC neurons most responsible for spatial tuning, directional selectivity, and predictive non-local upcoming choice were reported to be largely SWR-unmodulated [[raw/summaries/denbakker2024_mpfc_spatial_swr|den Bakker et al. 2024]]. Online prospective coding and offline update mechanisms appear at least partly dissociable.

## Landmark papers

- [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]]  
  Early evidence that rat PL/IL contains neurons overrepresenting behaviorally relevant goal locations, establishing that mPFC can carry spatially specific goal information.

- [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]]  
  First strong demonstration that hippocampal–prefrontal theta coordination rises specifically during working-memory choice and falls on errors.

- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]  
  Key causal paper showing that an mPFC–NR–CA1 pathway is necessary for prospective trajectory coding in CA1.

- [[raw/summaries/hasz2020_spatial_encoding_deliberation|Hasz et al. 2020]]  
  Important update from simultaneous recordings: deliberation-related coordination is bidirectional and operates on multiple timescales.

- [[raw/summaries/denbakker2024_mpfc_spatial_swr|den Bakker et al. 2024]]  
  Reframes recent SWR-centric interpretations by showing that the main mPFC neurons carrying spatial/predictive choice signals may be SWR-unmodulated.

## Boundaries and tensions

The cleanest causal result is about **CA1 trajectory coding**, not behavior per se. In [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]], disrupting NR strongly reduced prospective CA1 coding, but simple alternation performance was spared. That weakens any claim that this specific neural pattern is always necessary for successful navigation.

Task demand and training history likely matter. [[raw/summaries/hok2013_prefrontal_place_cells|Hok et al. 2013]] reported that mPFC inactivation in overtrained rats left hippocampal goal-related firing largely intact while reducing overdispersion. This sits uneasily beside the stronger dependence reported by [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]. The simplest reading is not contradiction but context dependence: mPFC contribution may be larger when trajectories must be actively selected or maintained, smaller after heavy overtraining.

Theta is the main online coordination candidate, but not all prefrontal spatial coding is theta-bound. [[raw/summaries/long2024_border_cells_prefrontal|Long et al. 2024]] found border-tuned neurons in mPFC with almost no theta rhythmicity. So “mPFC spatial coding” is broader than hippocampal-theta entrainment.

SWR-related coordination is also mixed. [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]] shows mPFC activity during a narrow post-SWR window is necessary for rule switching, but [[raw/summaries/denbakker2024_mpfc_spatial_swr|den Bakker et al. 2024]] indicates the neurons carrying predictive choice signals are largely outside the canonical SWR-modulated subset. This argues against a single replay-centric account of prefrontal prospective coding.

Directionality is still unsettled. [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]] is fundamentally correlational. [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] provides a strong mPFC→NR→CA1 result, but indirect routes through entorhinal cortex were not fully dissected, and simultaneous evidence like [[raw/summaries/hasz2020_spatial_encoding_deliberation|Hasz et al. 2020]] supports reciprocal influence.

Computational interpretation is underconstrained. Predictive-map / successor-representation ideas fit the data at a coarse level, but current physiology does not cleanly distinguish SR-like future occupancy coding from mixed selectivity for task phase, intention, policy, and reward context [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]].

## Open questions

- Under what conditions is prospective CA1–mPFC coding behaviorally necessary, rather than epiphenomenal or redundant?
- How does training alter dependence on mPFC input—especially the contrast between flexible learning and overtrained navigation?
- What exactly is represented in mPFC: intended route, goal state, action policy, value, or a mixed-selective combination?
- When does coordination rely mainly on theta, and when do SWR-linked processes dominate?
- How much of the prefrontal influence on CA1 is routed through NR versus entorhinal or other intermediary pathways?
- How do dorsal and ventral hippocampal contributions differ during prospective coding, given that both interact behaviorally with mPFC [[raw/summaries/avigan2020_spatial_learning_hippocampus|Avigan et al. 2020]]?
- Can prospective coding explain detour and transition-revaluation behavior, where simple cached predictive maps should fail without updating [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]]?
- In humans, does hippocampal goal-distance theta couple to prefrontal prospective signals during planning, or is the rodent circuit story only partially conserved [[raw/summaries/huang2024_hippocampal_theta_goal_distance|Huang et al. 2024]]?

## Key papers

- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] — strongest causal evidence for an mPFC–NR–CA1 pathway supporting prospective trajectory coding in CA1.
- [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones et al. 2005]] — canonical evidence for theta-mediated hippocampal–prefrontal coordination during spatial working-memory choice.
- [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]] — foundational demonstration of goal-location coding in PL/IL.
- [[raw/summaries/hasz2020_spatial_encoding_deliberation|Hasz et al. 2020]] — simultaneous-recording evidence for bidirectional, multiscale coordination during deliberation.
- [[raw/summaries/avigan2020_spatial_learning_hippocampus|Avigan et al. 2020]] — causal evidence that flexible spatial memory depends on hippocampal–mPFC interactions.
- [[raw/summaries/maharjan2018_dorsal_hippocampal_prefrontal_spatial_learning|Maharjan et al. 2018]] — dHPC–PFC interaction is necessary for spatial working-memory learning.
- [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|den Bakker et al. 2023]] — mPFC activity in the post-SWR window is necessary for spatial rule switching.
- [[raw/summaries/denbakker2024_mpfc_spatial_swr|den Bakker et al. 2024]] — upcoming-choice and spatially tuned mPFC representations are largely SWR-independent.
- [[raw/summaries/hok2013_prefrontal_place_cells|Hok et al. 2013]] — useful counterpoint: mPFC modulates variability of hippocampal place coding more than its mean goal-related structure in overtrained animals.
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] — computational framework for interpreting prospective spatial codes as predictive representations, with clear limits.

## Related wiki pages
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]: Cross-link where Page A discusses goal/task-sensitive cognitive maps and replay-based planning, pointing readers to Page B for how prefrontal circuits coordinate or read out hippocampal map content for prospective navigation decisions.
- [[wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory|Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory]]: From Page B, link to Page A as the dedicated subpage on hippocampal–prefrontal prospective coding during navigation; from Page A, link back to Page B for the wider mPFC functional context beyond prospective coding.

## Source papers
- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] | [[raw/mds/ito2015_prefrontal_thalamic_hippocampus|source md]]: A prefrontal–thalamo–hippocampal circuit for goal-directed spatial navigation
- [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]] | [[raw/mds/hok2005_goal_coding_prefrontal|source md]]: Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex
- [[raw/summaries/avigan2020_spatial_learning_hippocampus|Avigan et al. 2020]] | [[raw/mds/avigan2020_spatial_learning_hippocampus|source md]]: Flexible spatial learning requires both the dorsal and ventral hippocampus and their functional interactions with the prefrontal cortex
- [[raw/summaries/russek2017_model_based_reinforcement|Russek et al. 2017]] | [[raw/mds/russek2017_model_based_reinforcement|source md]]: Predictive representations can link model-based reinforcement learning to model-free mechanisms
- [[raw/summaries/jones2005_theta_hippocampal_prefrontal|Jones and Wilson 2005]] | [[raw/mds/jones2005_theta_hippocampal_prefrontal|source md]]: Theta Rhythms Coordinate Hippocampal–Prefrontal Interactions in a Spatial Memory Task
- [[raw/summaries/basu2023_goal_pointer_cognitive_map_ofc|Basu and Ito 2023]] | [[raw/mds/basu2023_goal_pointer_cognitive_map_ofc|source md]]: A goal pointer for a cognitive map in the orbitofrontal cortex
- [[raw/summaries/denbakker2023_sharp_wave_prefrontal_rule|Bakker et al. 2023]] | [[raw/mds/denbakker2023_sharp_wave_prefrontal_rule|source md]]: Sharp-wave-ripple-associated activity in the medial prefrontal cortex supports spatial rule switching
- [[raw/summaries/denbakker2024_mpfc_spatial_swr|Bakker and Kloosterman 2024]] | [[raw/mds/denbakker2024_mpfc_spatial_swr|source md]]: Neurons in the medial prefrontal cortex are involved in spatial tuning and signaling upcoming choice independently from hippocampal sharp-wave ripples
- [[raw/summaries/hasz2020_spatial_encoding_deliberation|Hasz and Redish 2020]] | [[raw/mds/hasz2020_spatial_encoding_deliberation|source md]]: Spatial encoding in dorsomedial prefrontal cortex and hippocampus is related during deliberation
- [[raw/summaries/hok2013_prefrontal_place_cells|Hok et al. 2013]] | [[raw/mds/hok2013_prefrontal_place_cells|source md]]: Prefrontal Cortex Focally Modulates Hippocampal Place Cell Firing Patterns
- [[raw/summaries/huang2024_hippocampal_theta_goal_distance|Huang et al. 2024]] | [[raw/mds/huang2024_hippocampal_theta_goal_distance|source md]]: Human Hippocampal Theta Oscillations Organise Distance to Goal Coding
