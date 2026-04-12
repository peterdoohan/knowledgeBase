## [2026-04-12] generate | First wiki topic pages from judged subtopics

- Generated 13 topic pages from selected subtopics under `wiki/topics/`
- Generated 1 debate page under `wiki/debates/`
- Rebuilt `wiki/indices/index.md` from the full generated page set
- Source layer: `derived/subtopic_catalog.yaml`
- Source layer: `derived/subtopic_judgments.jsonl`
- Source layer: `derived/paper_index.yaml`
- Source layer: `raw/summaries/*.md`
## [2026-04-12] generate | First wiki topic pages from judged subtopics

- Source catalog: `derived/coverage_subtopic_catalog.yaml`
- anterior_cingulate_future_state_and_model_based_control__02 -> wiki/topics/model_based_vs_model_free_reinforcement_learning_frameworks_in_anterior_cingulate_future_state_control.md (methods, worthiness 3)
- behavioral_paradigms_and_navigation_tasks__01 -> wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation.md (topic, worthiness 4)
- behavioral_paradigms_and_navigation_tasks__02 -> wiki/topics/successor_representations_and_grid_cell_predictive_maps_in_spatial_navigation.md (topic, worthiness 4)
- behavioral_paradigms_and_navigation_tasks__04 -> wiki/topics/successor_representation_and_hierarchical_planning_in_navigation.md (topic, worthiness 4)
- clinical_and_computational_psychiatry__01 -> wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction.md (topic, worthiness 3)
- hippocampal_prefrontal_coordination_and_planning__01 -> wiki/topics/hippocampal_prefrontal_replay_in_planning.md (topic, worthiness 3)
- hippocampal_prefrontal_coordination_and_planning__02 -> wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits.md (topic, worthiness 4)
- hippocampal_prefrontal_coordination_and_planning__03 -> wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning.md (topic, worthiness 4)
- ofc_task_state_and_value_maps__01 -> wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning.md (topic, worthiness 4)
- ofc_task_state_and_value_maps__03 -> wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_hidden_task_state.md (topic, worthiness 4)
- prefrontal_goal_representation_and_control__01 -> wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory.md (topic, worthiness 4)
- prefrontal_goal_representation_and_control__02 -> wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control.md (topic, worthiness 4)
- prefrontal_goal_representation_and_control__03 -> wiki/topics/hierarchical_planning_and_successor_representations_in_prefrontal_hippocampal_cognitive_control.md (topic, worthiness 3)
- striatal_and_dopaminergic_reinforcement_learning__01 -> wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning.md (debate, worthiness 4)
- striatal_and_dopaminergic_reinforcement_learning__02 -> wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning.md (topic, worthiness 3)
- striatal_and_dopaminergic_reinforcement_learning__03 -> wiki/topics/successor_representation_in_striatal_and_dopaminergic_reinforcement_learning.md (topic, worthiness 4)
- striatal_and_dopaminergic_reinforcement_learning__04 -> wiki/topics/dopamine_reward_prediction_error_and_temporal_difference_learning.md (topic, worthiness 4)
- striatal_and_dopaminergic_reinforcement_learning__05 -> wiki/topics/reward_modulated_hippocampal_replay_in_spatial_reinforcement_learning.md (topic, worthiness 4)
## [2026-04-12] prune | Merge overlapping successor-representation pages

- Deprecated 5 overlapping SR/navigation pages as redirect stubs
- Prune plan written to `derived/wiki_prune_plan.yaml`
- Canonical target pages kept active:
- `wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay.md`
- `wiki/topics/hierarchical_planning_and_successor_representations_in_prefrontal_hippocampal_cognitive_control.md`

## [2026-04-12] sync | Summary backlinks to active wiki pages

- Synced `wiki_pages` frontmatter backlinks into raw summaries
- Added or refreshed `### Related wiki pages` sections in represented summaries
- Rebuilt `wiki/indices/index.md` from active non-deprecated pages only
## [2026-04-12] maintain | Sync wiki-to-wiki crosslinks

- Source audit: `derived/wiki_editorial_audit.yaml`
- updated wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning.md
- updated wiki/debates/grid_cells_as_a_mechanism_for_path_integration.md
- updated wiki/topics/entorhinal_grid_cells_and_continuous_attractor_models_of_cognitive_maps.md
- updated wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_path_integration.md
- updated wiki/topics/hippocampal_entorhinal_cognitive_maps_place_cells_grid_cells_and_replay.md
- updated wiki/topics/hippocampal_predictive_maps_place_cells_successor_representation_and_replay.md
- updated wiki/topics/hippocampal_prefrontal_mechanisms_of_route_planning_and_detour_navigation.md
- updated wiki/topics/hippocampal_prefrontal_replay_in_planning.md
- updated wiki/topics/hippocampal_replay_and_schema_guided_generalization.md
- updated wiki/topics/hippocampal_sharp_wave_ripple_replay_and_prefrontal_coordination_during_planning.md
- updated wiki/topics/medial_prefrontal_cortex_in_goal_directed_spatial_navigation_and_spatial_working_memory.md
- updated wiki/topics/medial_prefrontal_cortex_in_rat_goal_directed_vs_habitual_control.md
- updated wiki/topics/model_based_vs_model_free_reinforcement_learning_frameworks_in_anterior_cingulate_future_state_control.md
- updated wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_hidden_task_state.md
- updated wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning.md
- updated wiki/topics/prospective_spatial_coding_in_hippocampal_medial_prefrontal_circuits.md
- updated wiki/topics/reward_modulated_hippocampal_replay_in_spatial_reinforcement_learning.md
- updated wiki/topics/sharp_wave_ripple_associated_hippocampal_replay.md
- updated wiki/topics/successor_representation_as_a_predictive_map_for_flexible_planning.md
- updated wiki/topics/task_state_representation_and_hidden_state_inference_in_orbitofrontal_hippocampal_reinforcement_learning.md
