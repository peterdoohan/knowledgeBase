# Summary Integration Status

Tracks which summaries have been integrated into the wiki.
Agents should read this file before running any pipeline stage to avoid reprocessing.

**Per-summary stages**: `facts_done` → `routed` → `written` → moved to `integrated`.
Crashed runs resume from each summary's last completed stage.

---

```yaml
integrated:
  - path: raw/summaries/adams2018_attractor_schizophrenia.md
    integrated_at: 2026-04-05T16:50:07
  - path: raw/summaries/adams2021_pyramidal_synaptic_gain.md
    integrated_at: 2026-04-05T17:30:00
  - path: raw/summaries/adams_delusions_inference_attractors.md
    integrated_at: 2026-04-05T17:35:00
  - path: raw/summaries/ahmadlou2021_novelty_seeking_behavior.md
    integrated_at: 2026-04-05T17:40:00
  - path: raw/summaries/akam2015_two_step_task_habits.md
    integrated_at: 2026-04-05T17:45:00
  - path: raw/summaries/akam2015_two_step_task_simple_plans.md
    integrated_at: 2026-04-05T17:05:00
  - path: raw/summaries/alonso2021_hexmaze_cognitive_map.md
    integrated_at: 2026-04-05T18:00:00
  - path: raw/summaries/ambrose2016_reverse_replay_hippocampal.md
    integrated_at: 2026-04-05T18:05:00
  - path: raw/summaries/akam2021_anterior_cingulate_model.md
    integrated_at: 2026-04-05T18:10:00
  - path: raw/summaries/akam2021_dopamine_model_based_rl.md
    integrated_at: 2026-04-05T18:15:00
  - path: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
    integrated_at: 2026-04-05T18:20:00
  - path: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
    integrated_at: 2026-04-05T18:25:00
  - path: raw/summaries/anastasiades2021_circuit_medial_prefrontal.md
    integrated_at: 2026-04-05T18:30:00
  - path: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    integrated_at: 2026-04-05T18:35:00
  - path: raw/summaries/baram2024_abstract_relational_map_consolidation.md
    integrated_at: 2026-04-05T18:40:00
  - path: raw/summaries/boccara2019_grid_goal_attractor.md
    integrated_at: 2026-04-05T18:45:00
  - path: raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md
    integrated_at: 2026-04-05T18:50:00
  - path: raw/summaries/pfeiffer2017_hippocampal_replay_memory.md
    integrated_at: 2026-04-05T18:55:00
  - path: raw/summaries/schultz1997_neural_substrate_reward_pred.md
    integrated_at: 2026-04-05T19:00:00
  - path: raw/summaries/gershman2018_successor_representation_learning.md
    integrated_at: 2026-04-05T19:05:00

  - path: raw/summaries/miller2019_retrosplenial_spatial_learning.md
    integrated_at: 2026-04-05T23:00:00
  - path: raw/summaries/nyberg2022_spatial_goal_coding.md
    integrated_at: 2026-04-05T23:00:00
  - path: raw/summaries/ormond2022_goal_oriented_vector_fields.md
    integrated_at: 2026-04-05T23:00:00
  - path: raw/summaries/ouchi2024_predictive_grid_coding.md
    integrated_at: 2026-04-05T23:00:00
  - path: raw/summaries/piray2025_compositional_cognitive_map.md
    integrated_at: 2026-04-05T23:00:00
  - path: raw/summaries/fiete2008_grid_cells_position.md
    integrated_at: 2026-04-05T23:05:00
  - path: raw/summaries/burak2009_path_integration_grid_cells.md
    integrated_at: 2026-04-05T23:05:00
  - path: raw/summaries/eldar2020_replay_planning.md
    integrated_at: 2026-04-05T23:05:00
  - path: raw/summaries/decothi2022_predictive_spatial_navigation.md
    integrated_at: 2026-04-05T23:05:00
  - path: raw/summaries/garvert2017_relational_knowledge_maps.md
    integrated_at: 2026-04-05T23:05:00
  - path: raw/summaries/elgaby2023_behavioral_structure_mapping.md
    integrated_at: 2026-04-05T23:10:00
  - path: raw/summaries/schapiro2013_event_representation_memory.md
    integrated_at: 2026-04-05T23:10:00
  - path: raw/summaries/stoianov2020_hierarchical_generative_model.md
    integrated_at: 2026-04-05T23:10:00
  - path: raw/summaries/duncan1996_intelligence_frontal_goal.md
    integrated_at: 2026-04-05T23:10:00
  - path: raw/summaries/goel2013_prefrontal_planning_real_world.md
    integrated_at: 2026-04-05T23:10:00
  - path: raw/summaries/spiers2015_detour_problem_navigation.md
    integrated_at: 2026-04-05T23:15:00
  - path: raw/summaries/mcnaughton2022_route_cognitive_map.md
    integrated_at: 2026-04-05T23:15:00
  - path: raw/summaries/patai2021_versatile_wayfinder_prefrontal.md
    integrated_at: 2026-04-05T23:15:00
  - path: raw/summaries/steffenach2005_spatial_memory_entorhinal.md
    integrated_at: 2026-04-05T23:15:00
  - path: raw/summaries/vann2009_retrosplenial_cortex_memory.md
    integrated_at: 2026-04-05T23:15:00
  - path: raw/summaries/khona2022_attractor_integrator.md
    integrated_at: 2026-04-05T23:20:00
  - path: raw/summaries/knudsen2020_ofc_theta_learning.md
    integrated_at: 2026-04-05T23:20:00
  - path: raw/summaries/knudsen2022_ofc_cognitive_map.md
    integrated_at: 2026-04-05T23:20:00
  - path: raw/summaries/liu2019_human_replay_reorganizes.md
    integrated_at: 2026-04-05T23:20:00
  - path: raw/summaries/makino2022_arithmetic_value_hierarchical.md
    integrated_at: 2026-04-05T23:20:00
  - path: raw/summaries/miller2019_retrosplenial_spatial_learning.md
    integrated_at: 2026-04-05T23:25:00
  - path: raw/summaries/nyberg2022_spatial_goal_coding.md
    integrated_at: 2026-04-05T23:25:00
  - path: raw/summaries/ormond2022_goal_oriented_vector_fields.md
    integrated_at: 2026-04-05T23:25:00
  - path: raw/summaries/ouchi2024_predictive_grid_coding.md
    integrated_at: 2026-04-05T23:25:00
  - path: raw/summaries/piray2025_compositional_cognitive_map.md
    integrated_at: 2026-04-05T23:25:00
  - path: raw/summaries/fiete2008_grid_cells_position.md
    integrated_at: 2026-04-05T23:30:00
  - path: raw/summaries/burak2009_path_integration_grid_cells.md
    integrated_at: 2026-04-05T23:30:00
  - path: raw/summaries/eldar2020_replay_planning.md
    integrated_at: 2026-04-05T23:30:00
  - path: raw/summaries/decothi2022_predictive_spatial_navigation.md
    integrated_at: 2026-04-05T23:30:00
  - path: raw/summaries/garvert2017_relational_knowledge_maps.md
    integrated_at: 2026-04-05T23:30:00
  - path: raw/summaries/elgaby2023_behavioral_structure_mapping.md
    integrated_at: 2026-04-05T23:35:00
  - path: raw/summaries/schapiro2013_event_representation_memory.md
    integrated_at: 2026-04-05T23:35:00
  - path: raw/summaries/stoianov2020_hierarchical_generative_model.md
    integrated_at: 2026-04-05T23:35:00
  - path: raw/summaries/duncan1996_intelligence_frontal_goal.md
    integrated_at: 2026-04-05T23:35:00
  - path: raw/summaries/goel2013_prefrontal_planning_real_world.md
    integrated_at: 2026-04-05T23:35:00
  - path: raw/summaries/spiers2015_detour_problem_navigation.md
    integrated_at: 2026-04-05T23:40:00
  - path: raw/summaries/mcnaughton2022_route_cognitive_map.md
    integrated_at: 2026-04-05T23:40:00
  - path: raw/summaries/patai2021_versatile_wayfinder_prefrontal.md
    integrated_at: 2026-04-05T23:40:00
  - path: raw/summaries/steffenach2005_spatial_memory_entorhinal.md
    integrated_at: 2026-04-05T23:40:00
  - path: raw/summaries/vann2009_retrosplenial_cortex_memory.md
    integrated_at: 2026-04-05T23:40:00
  - path: raw/summaries/khona2022_attractor_integrator.md
    integrated_at: 2026-04-05T23:45:00
  - path: raw/summaries/knudsen2020_ofc_theta_learning.md
    integrated_at: 2026-04-05T23:45:00
  - path: raw/summaries/knudsen2022_ofc_cognitive_map.md
    integrated_at: 2026-04-05T23:45:00
  - path: raw/summaries/liu2019_human_replay_reorganizes.md
    integrated_at: 2026-04-05T23:45:00
  - path: raw/summaries/makino2022_arithmetic_value_hierarchical.md
    integrated_at: 2026-04-05T23:45:00
  - path: raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/jeong2022_mesolimbic_dopamine_causal.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/kaplan2018_active_inference_navigation.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/behrens2007_learning_value_information_uncertain.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/behrens2018_cognitive_map_organizing_knowledge.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/balleine1998_goal_directed_instrumental_action.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/botvinick2012_planning_inference.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/daw2011_model_based_prefrontal_spectrum.md
    integrated_at: 2026-04-05T23:50:00
  - path: raw/summaries/wang2020_allen_mouse_brain_atlas.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/paulk2022_neuropixels_human_cortex.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/pachitariu2023_kilosort_spike_sorting.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/chung2022_neural_recording_neuropixels.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/gridchyn2020_replay_selective_memory.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/denbakker2024_mpfc_spatial_swr.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/samborska2021_hippocampus_prefrontal_gen.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/schmidt2021_mpfc_swr_dreadd.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/reinert2021_mouse_prefrontal_categorization.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/campbell2025_hardwired_circuit_td_learning.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/brunec2022_predictive_representations_hierarchies.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/bowler2023_cortical_inputs_hippocampal_ca1.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/brown2016_prospective_goals_hippocampus.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/hok2005_goal_coding_prefrontal.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/hok2013_prefrontal_place_cells.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/hasz2020_spatial_encoding_deliberation.md
    integrated_at: 2026-04-05T23:55:00
  - path: raw/summaries/rouach2008_astrocyte_metabolism.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/yi2018_gap_junction_astrocytes.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/devuyst2009_calcium_connexin43_hemichannels.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/paulson2000_cyclic_amp_gap_junction.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/solan2007_phosphorylation_connexin43.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/rackauskas2007_gap_junction_permeability.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/muller1996_bergmann_glial_coupling.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/davis2013_homeostatic_signaling_neural_stabilization.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/anderson2021_cannabigerolic_seizures.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/anderson2019_cannabidiol_clobazam_seizure.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/izquierdo2024_prefrontal_cortex_homology.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/jazi2023_hippocampal_path_integration_homing.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/jiang2022_learning_options_compression.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/johnson2007_hippocampus_decision.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/jones2005_theta_hippocampal_prefrontal.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/jonesgotman1977_design_fluency_frontal.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/kaar2019_parvalbumin_schizophrenia.md
    integrated_at: 2026-04-06T02:00:00
  - path: raw/summaries/kashay2022_anterior_cingulate_effort.md
    integrated_at: 2026-04-06T02:00:00

in_progress: []

pending: []
```
