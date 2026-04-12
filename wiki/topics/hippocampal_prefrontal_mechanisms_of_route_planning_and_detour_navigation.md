---
title: "Hippocampal–prefrontal mechanisms of route planning and detour navigation"
subtopic_id: behavioral_paradigms_and_navigation_tasks__01
parent_topic_id: behavioral_paradigms_and_navigation_tasks
page_type: topic
page_worthiness: 4
status: draft_llm
generated_at: "2026-04-12T19:48:09.660464+00:00"
generated_by: generate_wiki_pages.py
prompt_version: wiki-page-v1
source_catalog: derived/coverage_subtopic_catalog.yaml
anchor_papers:
  - ekstrom2003_spatial_navigation
  - patai2021_versatile_wayfinder_prefrontal
  - hartley2003_wayfinding_route
  - spiers2015_detour_problem_navigation
  - yu2025_theta_sweeps_goal_direction
core_papers:
  - brown2016_prospective_goals_hippocampus
  - ciaramelli2008_vmPFC_navigation_wayfinding
  - dahmani2015_prefrontal_navigation_strategies
  - ekstrom2003_spatial_navigation
  - farzanfar2023_cognitive_maps_spatial
  - hartley2003_wayfinding_route
  - ito2015_prefrontal_thalamic_hippocampus
  - jazi2023_hippocampal_path_integration_homing
related_wiki_pages:
  - wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay
  - wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay
  - wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory
---

# Hippocampal–prefrontal mechanisms of route planning and detour navigation

Route planning and detour behavior are not well explained by a single “cognitive map” process. The strongest synthesis is a division of labor: hippocampus carries spatial, prospective, and goal-related structure that can support flexible route selection, while prefrontal cortex helps maintain goals, evaluate changed contingencies, generate subgoals, and arbitrate between planning and habitual strategies. The interaction matters as much as either region alone. That said, the literature is uneven: hippocampal signals during detours are less consistent than many theories predicted, prefrontal functional subdivisions are partly inferred from heterogeneous tasks, and most human evidence still comes from virtual navigation.

## Current view

Successful wayfinding depends more on hippocampal representations than simple route following does. In humans, hippocampal engagement tracks accurate wayfinding, whereas route following leans more on caudate/response systems [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]].

Prefrontal cortex is not just a generic “executive” add-on. Across species and methods, it is implicated in goal maintenance, route adaptation, planning at choice points, false-shortcut rejection, and spontaneous route revision/backtracking [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

For detours specifically, the cleanest current claim is that prefrontal responses are more reliable than hippocampal ones. Reviews of human imaging find consistent PFC recruitment during forced route changes, while hippocampal increases are not consistent; hippocampus may be tracking path distance, future states, or trajectory structure rather than “detour detection” itself [[raw/summaries/spiers2015_detour_problem_navigation|Spiers and Gilbert 2015]].

Mechanistically, hippocampal–prefrontal interaction appears necessary for prospective coding. Rodent circuit work shows a medial PFC → nucleus reuniens → CA1 pathway is required for prospective trajectory coding in hippocampus during goal-directed navigation [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]]. Supporting work also suggests mPFC can shape hippocampal sharp-wave ripple rate and content after learning and during decision periods [[raw/summaries/schmidt2021_mpfc_swr_dreadd|Schmidt et al. 2021]].

A further refinement from recent rodent work is that hippocampal planning-related activity can look vector-like and theta-organized: CA1 cells can form goal-oriented vector fields, and theta sweeps can align more strongly to goal direction than to current movement direction [[raw/summaries/ormond2022_goal_oriented_vector_fields|Ormond et al. 2022]] [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]].

## Strongest evidence

- **Human hippocampus carries place and goal-relevant signals during navigation.** Intracranial single-unit recordings in epilepsy patients navigating a virtual town found bona fide hippocampal place cells, plus goal-responsive and conjunctive cells across temporal and frontal regions. This is still foundational evidence that human navigation-related coding is not reducible to visual landmark responses [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]].

- **Wayfinding and route-following dissociate behaviorally and neurally.** Trial-by-trial and between-subject analyses showed hippocampal activity relates to successful wayfinding, while caudate activity tracks route-following skill. This is one of the strongest human demonstrations that flexible route computation is not the same as replaying a learned response sequence [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]].

- **The human hippocampus can represent future route states before movement begins.** High-resolution fMRI with multivoxel analyses showed prospective hippocampal representations of planned goal states and intervening subgoals during a planning period, coupled to a broader prefrontal–MTL–retrosplenial network [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]].

- **A specific prefrontal–thalamic–hippocampal circuit is causally required for prospective coding.** In rodents, trajectory-direction signals from mPFC reach CA1 via nucleus reuniens, and disrupting this pathway impairs prospective hippocampal coding during goal-directed navigation [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].

- **Detour responses are more consistently prefrontal than hippocampal.** A review of nine neuroimaging studies reported increased PFC activity in every detour comparison, especially frontopolar and lateral PFC, while hippocampal increases were absent or even decreased in some studies. This is the main reason current views place replanning pressure more heavily on PFC than on hippocampus per se [[raw/summaries/spiers2015_detour_problem_navigation|Spiers and Gilbert 2015]].

- **Goal maintenance can be a prefrontal bottleneck.** A bilateral vmPFC lesion case showed severe wayfinding impairment despite preserved landmark knowledge and spatial memory, with improvement when the goal was periodically rehearsed. The result is narrow but informative: some navigation failures may reflect failure to keep the destination online, not failure to know the environment [[raw/summaries/ciaramelli2008_vmPFC_navigation_wayfinding|Ciaramelli 2008]].

- **Recent rodent physiology links hippocampal dynamics to online goal direction.** Goal-oriented CA1 vector fields update when the goal moves [[raw/summaries/ormond2022_goal_oriented_vector_fields|Ormond et al. 2022]], and theta sweeps preferentially align to goal direction, strengthen with experience, and predict correct choices [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]]. These findings are compelling but still need broader cross-species and causal validation.

## Landmark papers

[[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] established the modern human dissociation between flexible wayfinding and route following, tying the former to hippocampus and the latter to caudate.

[[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] provided the first direct human single-unit evidence for hippocampal place coding during navigation, while also revealing distributed goal-related cells beyond hippocampus.

[[raw/summaries/ciaramelli2008_vmPFC_navigation_wayfinding|Ciaramelli 2008]] made the important lesion-based point that prefrontal damage can impair wayfinding even when basic spatial knowledge is spared.

[[raw/summaries/spiers2015_detour_problem_navigation|Spiers and Gilbert 2015]] shifted the detour literature away from a hippocampus-centric expectation by showing that PFC responses are the consistent imaging result.

[[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] supplied the key circuit mechanism: mPFC influence on prospective CA1 coding via nucleus reuniens.

[[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] showed that the human hippocampus can prospectively represent future goals and subgoals during planning itself, not just during movement.

## Boundaries and tensions

The biggest empirical tension is simple: detour navigation does not reliably produce stronger hippocampal activity. If anything, the most reproducible detour effects are prefrontal [[raw/summaries/spiers2015_detour_problem_navigation|Spiers and Gilbert 2015]]. Any account claiming hippocampus as the primary detour detector overstates the evidence.

“Hippocampal planning code” is also not a single thing. The literature variously reports place coding, place×goal interactions, prospective route states, path-distance signals, vector fields, and theta sweeps [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] [[raw/summaries/ormond2022_goal_oriented_vector_fields|Ormond et al. 2022]] [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]]. These may reflect one underlying computation at different resolutions, or several distinct ones. That is unresolved.

Prefrontal subregional mappings are useful but not settled. Reviews assign replanning, conflict, subgoal generation, goal maintenance, and state-space/value functions to different PFC sectors [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]], but this synthesis relies on heterogeneous tasks and imperfect homology across rodents, primates, and humans.

The hippocampal–prefrontal story is incomplete without striatum. Route following and response-based strategies can bypass detailed relational planning, and PFC may help arbitrate between hippocampal and striatal solutions rather than simply “assist hippocampus” [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani et al. 2015]] [[raw/summaries/mugan_redish2024_environmental_complexity_decision|Mugan and Redish 2024]].

Human evidence is still method-limited. Foundational studies used small samples, male-only cohorts, virtual navigation, or clinical recordings [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]]. These are important results, but they constrain what can be claimed about real-world navigation and general population mechanisms.

Finally, not all prefrontal spatial coding appears theta-bound. Border-tuned neurons have been reported in mPFC with little theta rhythmicity, which argues against a blanket model in which prefrontal navigation signals are uniformly inherited via hippocampal theta synchrony [[raw/summaries/long2024_border_cells_prefrontal|Long et al. 2024]].

## Open questions

How is goal information injected into hippocampal online dynamics? Recent work explicitly leaves open whether goal-directed input to theta sweeps comes from mPFC, retrosplenial cortex, or both, potentially via thalamus [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]].

Are planning-period prospective codes, theta sweeps, goal-vector fields, and sharp-wave ripple content different manifestations of one planning architecture, or distinct mechanisms for deliberation, execution, and consolidation? Current evidence does not yet unify them cleanly [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] [[raw/summaries/ormond2022_goal_oriented_vector_fields|Ormond et al. 2022]] [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] [[raw/summaries/schmidt2021_mpfc_swr_dreadd|Schmidt et al. 2021]].

Which prefrontal computations are actually necessary for detours in humans? The lesion literature is thin, and the clearest human case concerns vmPFC goal maintenance rather than detour-specific replanning [[raw/summaries/ciaramelli2008_vmPFC_navigation_wayfinding|Ciaramelli 2008]].

How do false shortcuts, forced detours, spontaneous backtracking, and open-ended foraging differ? These behaviors are often grouped together as “flexible navigation,” but they likely recruit overlapping rather than identical hippocampal–prefrontal computations [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]].

How does repeated experience change the system? One plausible trajectory is a shift from hippocampus-dependent route planning toward extra-hippocampal spatial schemas, but this remains more conceptual than settled for detour behavior [[raw/summaries/farzanfar2023_cognitive_maps_spatial|Farzanfar et al. 2023]].

At the algorithmic level, it remains unclear whether these signals are best formalized as model-based search, successor-like predictive structure, attractor dynamics with goal input, or mixtures that depend on task complexity and familiarity [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] [[raw/summaries/mugan_redish2024_environmental_complexity_decision|Mugan and Redish 2024]].

## Key papers

- [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] — canonical human dissociation between wayfinding and route following.
- [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] — first direct human single-unit evidence for place and goal-related navigation coding.
- [[raw/summaries/spiers2015_detour_problem_navigation|Spiers and Gilbert 2015]] — strongest synthesis that detour effects are reliably prefrontal, not consistently hippocampal.
- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] — causal mPFC–thalamic–CA1 mechanism for prospective trajectory coding.
- [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] — human hippocampal prospective representation of goals and subgoals during planning.
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai et al. 2021]] — best broad review of prefrontal contributions to navigation and replanning.
- [[raw/summaries/ciaramelli2008_vmPFC_navigation_wayfinding|Ciaramelli 2008]] — lesion evidence that goal maintenance deficits can produce major wayfinding failures.
- [[raw/summaries/ormond2022_goal_oriented_vector_fields|Ormond et al. 2022]] — hippocampal goal-vector fields in rodent CA1.
- [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] — hippocampal theta sweeps aligned to goal direction, with behavioral relevance.

## Related wiki pages
- [[wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay|Hippocampal predictive maps: place cells, successor representation, and replay]]: Link A -> B for predictive-map theories of spatial prospecting that may support route planning; link B -> A for the limits of SR/predictive maps in detour and transition-revaluation settings, where prefrontal goal maintenance, subgoaling, and strategy arbitration become critical.
- [[wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay|Hippocampal–entorhinal cognitive maps (place cells, grid cells, and replay)]]: Link B -> A as 'how cognitive-map representations are recruited for flexible route planning and detours'; link A -> B as 'representational mechanisms in hippocampal–entorhinal circuits that may supply planning-relevant spatial structure.'
- [[wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory|Medial prefrontal cortex in goal-directed spatial navigation and spatial working memory]]: Link A to B for readers wanting a deeper treatment of mPFC-specific goal representation, policy updating, and spatial working-memory evidence; link B to A for the navigation-task context where mPFC functions are expressed as route planning and detour behavior.

## Source papers
- [[raw/summaries/ekstrom2003_spatial_navigation|Ekstrom et al. 2003]] | [[raw/mds/ekstrom2003_spatial_navigation|source md]]: Cellular networks underlying human spatial navigation
- [[raw/summaries/patai2021_versatile_wayfinder_prefrontal|Patai and Spiers 2021]] | [[raw/mds/patai2021_versatile_wayfinder_prefrontal|source md]]: The Versatile Wayfinder: Prefrontal Contributions to Spatial Navigation
- [[raw/summaries/hartley2003_wayfinding_route|Hartley et al. 2003]] | [[raw/mds/hartley2003_wayfinding_route|source md]]: The Well-Worn Route and the Path Less Traveled: Distinct Neural Bases of Route Following and Wayfinding in Humans
- [[raw/summaries/spiers2015_detour_problem_navigation|Spiers and Gilbert 2015]] | [[raw/mds/spiers2015_detour_problem_navigation|source md]]: Solving the detour problem in navigation: a model of prefrontal and hippocampal interactions
- [[raw/summaries/yu2025_theta_sweeps_goal_direction|Yu et al. 2025]] | [[raw/mds/yu2025_theta_sweeps_goal_direction|source md]]: Hippocampal theta sweeps indicate goal direction
- [[raw/summaries/brown2016_prospective_goals_hippocampus|Brown et al. 2016]] | [[raw/mds/brown2016_prospective_goals_hippocampus|source md]]: Prospective representation of navigational goals in the human hippocampus
- [[raw/summaries/ciaramelli2008_vmPFC_navigation_wayfinding|Ciaramelli 2008]] | [[raw/mds/ciaramelli2008_vmPFC_navigation_wayfinding|source md]]: The role of ventromedial prefrontal cortex in navigation: A case of impaired wayfinding and rehabilitation
- [[raw/summaries/dahmani2015_prefrontal_navigation_strategies|Dahmani and Bohbot 2015]] | [[raw/mds/dahmani2015_prefrontal_navigation_strategies|source md]]: Dissociable contributions of the prefrontal cortex to hippocampus- and caudate nucleus-dependent virtual navigation strategies
- [[raw/summaries/farzanfar2023_cognitive_maps_spatial|Farzanfar et al. 2023]] | [[raw/mds/farzanfar2023_cognitive_maps_spatial|source md]]: From cognitive maps to spatial schemas
- [[raw/summaries/ito2015_prefrontal_thalamic_hippocampus|Ito et al. 2015]] | [[raw/mds/ito2015_prefrontal_thalamic_hippocampus|source md]]: A prefrontal–thalamo–hippocampal circuit for goal-directed spatial navigation
- [[raw/summaries/jazi2023_hippocampal_path_integration_homing|Jazi et al. 2023]] | [[raw/mds/jazi2023_hippocampal_path_integration_homing|source md]]: Hippocampal firing fields anchored to a moving object predict homing direction during path-integration-based behavior
