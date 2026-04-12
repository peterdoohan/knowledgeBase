---
title: "Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)"
subtopic_id: cognitive_maps__01
parent_topic_id: cognitive_maps
page_type: topic
page_worthiness: 5
status: draft_llm
generated_at: "2026-04-12T19:25:57.460260+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/subtopic_catalog.yaml
anchor_papers:
  - stachenfeld2017_hippocampus_predictive_map
  - widloski2022_hippocampal_replay_barriers
  - ekstrom2003_spatial_navigation
  - patai2021_versatile_wayfinder_prefrontal
  - hok2005_goal_coding_prefrontal
core_papers:
  - boccara2019_grid_goal_attractor
  - butler2019_reward_locations_entorhinal_maps
  - decothi2022_predictive_spatial_navigation
  - dorrell2022_actionable_grid_cells
  - dorrell2023_actionable_grid_constraints
  - duvelle2023_temporal_hippocampal_inference
  - ekstrom2003_spatial_navigation
  - epstein2017_cognitive_maps_humans
---

# Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)

The hippocampal–entorhinal circuit is the strongest neural candidate for a spatial cognitive map, but the map is not well described as a static Euclidean chart. Across human and rodent work, place coding, grid-like coding, and replay all show sensitivity to barriers, goals, and task demands, pushing the field toward predictive and policy-sensitive accounts rather than purely sensory or purely geometric ones. At the same time, no single mechanism has won: metric/path-integration theories, successor-representation accounts, and replay-based planning models each explain part of the data, and flexible navigation appears to require hippocampal interaction with prefrontal and striatal systems rather than hippocampus alone [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]].

## Current view

The basic claim that hippocampus encodes location is on solid ground. Human single-unit recordings show hippocampal cells that respond to place rather than view, with a complementary parahippocampal view code, arguing against a purely visual explanation of navigation-related activity [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]].

Entorhinal grid coding is no longer treated as a rigid spatial metric only. Goal learning can deform entorhinal spatial maps and pull grid fields toward rewarded locations, implying that entorhinal representations incorporate memory and behavioral relevance, not just self-location [[raw/summaries/boccara2019_grid_goal_attractor|Boccara et al. 2019]] [[raw/summaries/butler2019_reward_locations_entorhinal_maps|Butler et al. 2019]].

Replay has become central because it dissociates stable map structure from flexible use of that structure. In barrier-rich environments, replay sequences rapidly reroute around new obstacles even when place fields remain largely stable, suggesting that online path computation can change faster than the underlying rate map [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]].

The most influential synthesis is predictive-map theory: hippocampal codes may represent expected future occupancy under a policy, with grid cells providing a low-dimensional basis for that representation [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]. But this is not settled. Grid cells can also be derived from metric/path-integration and coding-efficiency arguments, and recent behavioral data suggest humans use a mixture of SR-like and model-based strategies rather than a single algorithm [[raw/summaries/fiete2008_grid_cells_position|Fiete et al. 2008]] [[raw/summaries/dorrell2022_actionable_grid_cells|Dorrell et al. 2022]] [[raw/summaries/dorrell2023_actionable_grid_constraints|Dorrell et al. 2023]] [[raw/summaries/decothi2022_predictive_spatial_navigation|De Cothi et al. 2022]].

## Strongest evidence

- **Direct human place coding.** In epilepsy patients navigating a virtual town, 24% of hippocampal cells met a strict place-selective criterion after separating place from view and goal effects. Place responses were non-directional, while view coding was concentrated in parahippocampal regions [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]].

- **Replay tracks future, not just memory.** In rats, away-event replay was biased to terminate at the Home well, predicted subsequent visits, and aligned more with future than past trajectories. Replay sequences respected current barriers in 27/31 sessions (87%), even though place fields were largely stable across many barrier configurations [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]].

- **Goal locations reshape entorhinal maps.** Learned reward locations shift entorhinal/grid firing toward goals and improve decoding near those locations, showing that entorhinal spatial maps are behaviorally reweighted rather than purely metric [[raw/summaries/boccara2019_grid_goal_attractor|Boccara et al. 2019]] [[raw/summaries/butler2019_reward_locations_entorhinal_maps|Butler et al. 2019]].

- **Predictive-map theory explains disparate place/grid phenomena with one formalism.** A successor representation reproduces backward-skewed place fields on directed tracks, obstacle-sensitive distortions, reward clustering, and nonspatial graph-structure effects; its eigenvectors generate grid-like fields across multiple geometries [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

- **Cross-species behavior matches predictive navigation better than simple model-free accounts.** In a modular open-field maze used in rats and humans, navigation was best matched by SR agents, with humans additionally showing model-based signatures early in learning [[raw/summaries/decothi2022_predictive_spatial_navigation|De Cothi et al. 2022]].

- **Navigation depends on map–goal interaction, not map alone.** Rat mPFC neurons overrepresent goal locations, and broader literature implicates PFC in detours, replanning, and value-based route choice, constraining strong claims that hippocampal maps themselves are sufficient for planning [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]] [[raw/summaries/ito2018_prefrontal_hippocampal_navigation|Ito et al. 2018]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]].

## Landmark papers

- [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] — first direct single-unit evidence for human place cells, with a clean place vs view dissociation.

- [[raw/summaries/fiete2008_grid_cells_position|Fiete et al. 2008]] — established grid coding as a high-capacity positional code, influential for metric/path-integration views.

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] — reframed hippocampus as a predictive map and grid cells as a spectral basis of future-state occupancy.

- [[raw/summaries/boccara2019_grid_goal_attractor|Boccara et al. 2019]] — showed grid maps can be attracted toward learned goals.

- [[raw/summaries/butler2019_reward_locations_entorhinal_maps|Butler et al. 2019]] — demonstrated remembered reward locations restructure entorhinal spatial maps.

- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] — strong dissociation between stable place fields and rapidly flexible replay around barriers.

- [[raw/summaries/decothi2022_predictive_spatial_navigation|De Cothi et al. 2022]] — important bridge from rodent/human behavior to SR-like navigation models.

## Boundaries and tensions

- **Metric code vs predictive code remains unresolved.** Grid cells can be explained as a positional/path-integration code [[raw/summaries/fiete2008_grid_cells_position|Fiete et al. 2008]], as SR eigenvectors [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]], or as the optimal solution under actionable biological constraints [[raw/summaries/dorrell2022_actionable_grid_cells|Dorrell et al. 2022]] [[raw/summaries/dorrell2023_actionable_grid_constraints|Dorrell et al. 2023]]. These accounts are not equivalent, and current data do not cleanly adjudicate among them.

- **Policy sensitivity is explanatory but costly.** SR naturally explains barrier and reward effects, but because it is policy-dependent, large goal changes can require relearning or additional model-based machinery. This limitation is explicit in the predictive-map account and consistent with human behavior showing mixed SR and model-based signatures [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/decothi2022_predictive_spatial_navigation|De Cothi et al. 2022]].

- **Reward effects are real but not uniform.** Goal-related distortions in entorhinal maps are robust in the cited studies [[raw/summaries/boccara2019_grid_goal_attractor|Boccara et al. 2019]] [[raw/summaries/butler2019_reward_locations_entorhinal_maps|Butler et al. 2019]], but SR-based predictions about reward-related place-field changes are not a complete fit to all prior place-cell findings, as noted by [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]].

- **Replay is strongly implicated in flexible navigation, but causality is still limited.** The best barrier data are correlational: replay predicts future behavior and respects obstacles, yet this does not fully separate planning from evaluation or consolidation [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] [[raw/summaries/epsztein2022_mental_replays_navigation|Epsztein et al. 2022]].

- **Human evidence is thinner than rodent evidence.** Human single-unit results are powerful but come from small clinical samples in virtual environments lacking full vestibular/proprioceptive input [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]]. Broader human imaging supports map-like coding, but with less cellular specificity [[raw/summaries/epstein2017_cognitive_maps_humans|Epstein et al. 2017]].

- **Hippocampal maps are not the whole navigation system.** mPFC, OFC, ACC, retrosplenial cortex, and striatum contribute goal coding, detour handling, and route selection [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]]. Strong “hippocampus-alone” interpretations are therefore too narrow.

## Open questions

- What circuit mechanism allows replay to adapt to new barriers within-session while place fields stay mostly stable [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]]?

- Which replay events are causally necessary for immediate route choice, as opposed to memory consolidation or evaluation [[raw/summaries/epsztein2022_mental_replays_navigation|Epsztein et al. 2022]]?

- Are grid cells primarily a metric/path-integration code, a predictive basis, or a representation that multiplexes both [[raw/summaries/fiete2008_grid_cells_position|Fiete et al. 2008]] [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]?

- How are multiple predictive timescales implemented biologically, including the proposed longitudinal gradient in hippocampus [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]]?

- How do hippocampus, entorhinal cortex, mPFC/OFC, and striatum divide labor during detours, hidden-state inference, and hierarchical planning [[raw/summaries/ito2018_prefrontal_hippocampal_navigation|Ito et al. 2018]] [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]]?

- How far do these spatial coding principles generalize to nonspatial graphs, latent states, or conceptual domains without becoming too unconstrained [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] [[raw/summaries/epstein2017_cognitive_maps_humans|Epstein et al. 2017]]?

## Key papers

- [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] — direct human single-unit evidence for place coding distinct from view coding.

- [[raw/summaries/fiete2008_grid_cells_position|Fiete et al. 2008]] — classic computational account of why grid codes are powerful for position representation.

- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] — the central predictive-map/SR formulation for hippocampus and entorhinal cortex.

- [[raw/summaries/boccara2019_grid_goal_attractor|Boccara et al. 2019]] — goal attraction of grid fields.

- [[raw/summaries/butler2019_reward_locations_entorhinal_maps|Butler et al. 2019]] — remembered rewards restructure entorhinal maps.

- [[raw/summaries/decothi2022_predictive_spatial_navigation|De Cothi et al. 2022]] — cross-species behavioral evidence for SR-like navigation.

- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski et al. 2022]] — replay reroutes around barriers without global remapping.

- [[raw/summaries/epsztein2022_mental_replays_navigation|Epsztein et al. 2022]] — focused synthesis of replay as a mechanism for flexible navigation.

- [[raw/summaries/ito2018_prefrontal_hippocampal_navigation|Ito et al. 2018]] — concise review of hippocampal–prefrontal interactions in goal-directed navigation.

- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] — broader framing of prefrontal contributions that constrain map-only accounts.

## Source papers
- [[raw/summaries/stachenfeld2017_hippocampus_predictive_map|Stachenfeld et al. 2017]] | [[raw/mds/stachenfeld2017_hippocampus_predictive_map|source md]]: The hippocampus as a predictive map
- [[raw/summaries/widloski2022_hippocampal_replay_barriers|Widloski and Foster 2022]] | [[raw/mds/widloski2022_hippocampal_replay_barriers|source md]]: Flexible rerouting of hippocampal replay sequences around changing barriers in the absence of global place field remapping
- [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] | [[raw/mds/ekstrom2003_spatial_navigation|source md]]: Cellular networks underlying human spatial navigation
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] | [[raw/mds/patai2021_versatile_wayfinder_prefrontal|source md]]: The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation
- [[raw/summaries/hok2005_goal_coding_prefrontal|Hok et al. 2005]] | [[raw/mds/hok2005_goal_coding_prefrontal|source md]]: Coding for spatial goals in the prelimbic/infralimbic area of the rat frontal cortex
- [[raw/summaries/boccara2019_grid_goal_attractor|Boccara et al. 2019]] | [[raw/mds/boccara2019_grid_goal_attractor|source md]]: The entorhinal cognitive map is attracted to goals
- [[raw/summaries/butler2019_reward_locations_entorhinal_maps|Butler et al. 2019]] | [[raw/mds/butler2019_reward_locations_entorhinal_maps|source md]]: Remembered reward locations restructure entorhinal spatial maps
- [[raw/summaries/decothi2022_predictive_spatial_navigation|Cothi et al. 2022]] | [[raw/mds/decothi2022_predictive_spatial_navigation|source md]]: Predictive maps in rats and humans for spatial navigation
- [[raw/summaries/dorrell2022_actionable_grid_cells|Dorrell et al. 2022]] | [[raw/mds/dorrell2022_actionable_grid_cells|source md]]: Actionable Neural Representations: Grid Cells from Minimal Constraints
- [[raw/summaries/dorrell2023_actionable_grid_constraints|Dorrell et al. 2023]] | [[raw/mds/dorrell2023_actionable_grid_constraints|source md]]: Actionable Neural Representations: Grid Cells from Minimal Constraints
- [[raw/summaries/duvelle2023_temporal_hippocampal_inference|Duvelle et al. 2023]] | [[raw/mds/duvelle2023_temporal_hippocampal_inference|source md]]: Temporal context and latent state inference in the hippocampal splitter signal
- [[raw/summaries/epstein2017_cognitive_maps_humans|Epstein et al. 2017]] | [[raw/mds/epstein2017_cognitive_maps_humans|source md]]: The cognitive map in humans: spatial navigation and beyond
