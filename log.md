# Knowledge Base Activity Log

Append-only YAML log of agent activity. Each entry records one pipeline event.
Agents should read this file to check recent activity before acting.

---

entries:
  - timestamp: 2026-04-05T19:30:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/anastasiades2021_circuit_medial_prefrontal.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 35
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/medial_prefrontal_cortex.md
      - wiki/brain_regions/infralimbic_cortex.md
      - wiki/brain_regions/basolateral_amygdala.md
      - wiki/brain_regions/mediodorsal_thalamus.md
      - wiki/brain_regions/ventromedial_thalamus.md
      - wiki/brain_regions/ventral_hippocampus.md
    pages_updated:
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/brain_regions/prelimbic_cortex.md
      - wiki/computational_frameworks/cortical_microcircuit.md
      - index.md

  - timestamp: 2026-04-05T19:00:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/boccara2019_grid_goal_attractor.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 35
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/medial_entorhinal_cortex.md
      - wiki/behaviours/grid_cells.md
    pages_updated:
      - wiki/brain_regions/hippocampus_ca1.md
      - wiki/behaviours/cognitive_map.md
      - wiki/behaviours/goal_directed_behaviour.md
      - wiki/behaviours/spatial_navigation.md
      - wiki/computational_frameworks/attractor_networks.md
      - wiki/index.md

  - timestamp: 2026-04-05T18:30:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/ambrose2016_reverse_replay_hippocampal.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 28
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/hippocampus.md
      - wiki/brain_regions/hippocampus_ca1.md
      - wiki/brain_regions/ventral_tegmental_area.md
      - wiki/behaviours/hippocampal_replay.md
      - wiki/behaviours/reverse_replay.md
      - wiki/behaviours/forward_replay.md
      - wiki/behaviours/sharp_wave_ripples.md
      - wiki/behaviours/place_cells.md
      - wiki/behaviours/reward_processing.md
      - wiki/computational_frameworks/temporal_credit_assignment.md
    pages_updated:
      - wiki/behaviours/memory_consolidation.md
      - wiki/computational_frameworks/reinforcement_learning.md
      - wiki/index.md
  - timestamp: 2026-04-05T18:15:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/akam2021_anterior_cingulate_model.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 24
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/anterior_cingulate_cortex.md
    pages_updated:
      - wiki/computational_frameworks/model_based_rl.md
      - wiki/computational_frameworks/model_free_rl.md
      - wiki/computational_frameworks/state_representation.md
      - wiki/behaviours/two_step_task.md
      - wiki/behaviours/goal_directed_behaviour.md
      - wiki/behaviours/habits.md
      - wiki/index.md

  - timestamp: 2026-04-05T18:00:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/alonso2021_hexmaze_cognitive_map.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 6
    facts_skipped: 0
    pages_created:
      - wiki/behaviours/spatial_navigation.md
      - wiki/behaviours/cognitive_map.md
      - wiki/behaviours/memory_consolidation.md
      - wiki/behaviours/schema_learning.md
    pages_updated:
      - wiki/brain_regions/hippocampus.md
      - wiki/index.md
  - timestamp: 2026-04-05T17:30:00
    agent: router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/adams2021_pyramidal_synaptic_gain.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 22
    facts_skipped: 0
    pages_created:
      - wiki/computational_frameworks/cortical_microcircuit.md
      - wiki/methods/dynamic_causal_modelling.md
      - wiki/methods/parametric_empirical_bayes.md
      - wiki/behaviours/mismatch_negativity.md
      - wiki/behaviours/auditory_steady_state_response.md
      - wiki/behaviours/psychosis.md
      - wiki/behaviours/hallucinations.md
      - wiki/brain_regions/primary_auditory_cortex.md
      - wiki/brain_regions/inferior_frontal_gyrus.md
      - wiki/brain_regions/superior_temporal_gyrus.md
    pages_updated:
      - wiki/behaviours/schizophrenia.md
      - wiki/index.md

  - timestamp: 2026-04-05T17:00:00
    agent: router_wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/adams_delusions_inference_attractors.md
    facts_extracted: 7
    facts_routed: 7
    pages_created:
      - wiki/behaviours/delusions.md
      - wiki/computational_frameworks/active_inference.md
    pages_updated:
      - wiki/computational_frameworks/attractor_networks.md
      - wiki/behaviours/schizophrenia.md
      - wiki/behaviours/belief_updating.md
      - wiki/computational_frameworks/bayesian_inference.md
      - wiki/methods/computational_psychiatry.md
    facts_written: 20
    facts_skipped: 0

- timestamp: 2026-04-05T16:53:51
  agent: router+wiki_writer
  event: summary_integrated
  source_summary: raw/summaries/akam2015_two_step_task_habits.md
  facts_extracted: 11
  facts_routed: 11
  facts_written: 11
  facts_skipped: 0
  pages_created:
    - wiki/methods/computational_modeling.md
  pages_updated:
    - wiki/computational_frameworks/model_free_rl.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/bayesian_inference.md
    - wiki/behaviours/two_step_task.md
    - wiki/methods/computational_modeling.md

  - timestamp: 2026-04-05T17:35:00
    agent: router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/ahmadlou2021_novelty_seeking_behavior.md
    facts_extracted: 8
    facts_routed: 8
    facts_written: 27
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/zona_incerta.md
      - wiki/brain_regions/periaqueductal_gray.md
      - wiki/brain_regions/prelimbic_cortex.md
      - wiki/behaviours/novelty_seeking.md
      - wiki/behaviours/investigatory_behavior.md
    pages_updated:
      - wiki/brain_regions/prefrontal_cortex.md

- timestamp: 2026-04-05T17:45:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  facts_extracted: 6
  facts_routed: 6
  facts_written: 11
  facts_skipped: 0
  pages_created:
    - wiki/methods/pycontrol.md
    - wiki/methods/high_throughput_behavioral_testing.md
    - wiki/behaviours/five_choice_serial_reaction_time_task.md
    - wiki/computational_frameworks/extended_finite_state_machine.md
  pages_updated: []

- timestamp: 2026-04-05T17:45:01
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/pycontrol.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:02
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/pycontrol.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:03
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/pycontrol.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:04
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/pycontrol.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:05
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/pycontrol.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:06
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/pycontrol.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:07
  agent: wiki_writer
  event: wiki_updated
  page: wiki/computational_frameworks/extended_finite_state_machine.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:08
  agent: wiki_writer
  event: wiki_updated
  page: wiki/methods/high_throughput_behavioral_testing.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

- timestamp: 2026-04-05T17:45:09
  agent: wiki_writer
  event: wiki_updated
  page: wiki/behaviours/five_choice_serial_reaction_time_task.md
  section: "## Key evidence"
  source_summary: raw/summaries/akam2022_pycontrol_behavioral_experiments.md
  action: written

  - timestamp: 2026-04-05T18:00:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/akam2021_dopamine_model_based_rl.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 21
    facts_skipped: 0
    pages_created:
      - wiki/computational_frameworks/successor_representation.md
      - wiki/brain_regions/striatum.md
      - wiki/methods/optogenetics.md
    pages_updated:
      - wiki/brain_regions/ventral_tegmental_area.md
      - wiki/brain_regions/hippocampus.md
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/computational_frameworks/model_based_rl.md
      - wiki/computational_frameworks/reinforcement_learning.md
      - wiki/behaviours/goal_directed_behaviour.md
      - index.md

- timestamp: $(date -u +"%Y-%m-%dT%H:%M:%S")
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
  facts_extracted: 6
  facts_routed: 6
  facts_written: 17
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/entorhinal_cortex.md
    - wiki/brain_regions/ventromedial_prefrontal_cortex.md
    - wiki/brain_regions/ventral_striatum.md
    - wiki/brain_regions/posterior_cingulate_cortex.md
    - wiki/behaviours/reinforcement_learning.md
    - wiki/methods/fmri.md
  pages_updated:
    - wiki/behaviours/cognitive_map.md
    - wiki/computational_frameworks/state_representation.md
    - wiki/computational_frameworks/reinforcement_learning.md
    - wiki/behaviours/schema_learning.md
    - wiki/brain_regions/hippocampus.md
    - wiki/index.md

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/brain_regions/entorhinal_cortex.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/brain_regions/ventromedial_prefrontal_cortex.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/brain_regions/ventral_striatum.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/brain_regions/posterior_cingulate_cortex.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/behaviours/reinforcement_learning.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/methods/fmri.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/behaviours/cognitive_map.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/computational_frameworks/state_representation.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/computational_frameworks/reinforcement_learning.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/behaviours/schema_learning.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

  - timestamp: 2026-04-05T17:02:39
    agent: wiki_writer
    event: wiki_updated
    page: wiki/brain_regions/hippocampus.md
    section: "## Key evidence"
    source_summary: raw/summaries/baram2021_entorhinal_ventromedial_rl.md
    action: written

- timestamp: 2026-04-05T19:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/baram2024_abstract_relational_map_consolidation.md
  facts_extracted: 6
  facts_routed: 6
  facts_written: 28
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/medial_temporal_lobe.md
    - wiki/computational_frameworks/factorised_representations.md
    - wiki/computational_frameworks/tolman_eichenbaum_machine.md
    - wiki/methods/representational_similarity_analysis.md
    - wiki/methods/fmri_repetition_suppression.md
  pages_updated:
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/behaviours/memory_consolidation.md
    - wiki/behaviours/cognitive_map.md
    - wiki/behaviours/schema_learning.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/state_representation.md
    - wiki/methods/computational_modeling.md
    - index.md

- timestamp: 2026-04-05T19:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
  facts_extracted: 6
  facts_routed: 6
  facts_written: 24
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/frontal_eye_field.md
    - wiki/computational_frameworks/mixed_selectivity.md
    - wiki/computational_frameworks/neural_manifold.md
    - wiki/behaviours/temporal_expectation.md
  pages_updated:
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/index.md

- timestamp: 2026-04-05T19:00:01
  agent: wiki_writer
  event: wiki_updated
  page: wiki/brain_regions/frontal_eye_field.md
  section: "## Key evidence"
  source_summary: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
  action: written

- timestamp: 2026-04-05T19:00:02
  agent: wiki_writer
  event: wiki_updated
  page: wiki/brain_regions/prefrontal_cortex.md
  section: "## Key evidence"
  source_summary: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
  action: written

- timestamp: 2026-04-05T19:00:03
  agent: wiki_writer
  event: wiki_updated
  page: wiki/computational_frameworks/mixed_selectivity.md
  section: "## Key evidence"
  source_summary: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
  action: written

- timestamp: 2026-04-05T19:00:04
  agent: wiki_writer
  event: wiki_updated
  page: wiki/computational_frameworks/neural_manifold.md
  section: "## Key evidence"
  source_summary: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
  action: written

- timestamp: 2026-04-05T19:00:05
  agent: wiki_writer
  event: wiki_updated
  page: wiki/behaviours/temporal_expectation.md
  section: "## Key evidence"
  source_summary: raw/summaries/amengual2022_pfc_multiplexing_behavior.md
  action: written

- timestamp: 2026-04-05T20:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/gershman2018_successor_representation_learning.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 7
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/computational_frameworks/successor_representation.md
    - wiki/brain_regions/hippocampus.md
    - wiki/behaviours/place_cells.md
    - wiki/brain_regions/ventral_tegmental_area.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/model_free_rl.md
    - wiki/brain_regions/prefrontal_cortex.md
    - index.md
    - log.md

- timestamp: 2026-04-05T20:30:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/schultz1997_neural_substrate_reward_pred.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 26
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/substantia_nigra.md
    - wiki/computational_frameworks/temporal_difference_learning.md
    - wiki/behaviours/conditioning.md
  pages_updated:
    - wiki/brain_regions/ventral_tegmental_area.md
    - wiki/brain_regions/striatum.md
    - wiki/computational_frameworks/reinforcement_learning.md
    - wiki/behaviours/reward_processing.md
    - index.md

- timestamp: 2026-04-05T21:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/pfeiffer2017_hippocampal_replay_memory.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 28
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/hippocampus_ca3.md
  pages_updated:
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/reverse_replay.md
    - wiki/behaviours/forward_replay.md
    - wiki/behaviours/memory_consolidation.md
    - wiki/behaviours/planning.md
    - wiki/behaviours/sharp_wave_ripples.md
    - wiki/behaviours/place_cells.md
    - wiki/behaviours/reward_processing.md
    - wiki/behaviours/cognitive_map.md
    - wiki/behaviours/goal_directed_behaviour.md
    - wiki/brain_regions/hippocampus.md
    - wiki/computational_frameworks/temporal_credit_assignment.md
    - wiki/computational_frameworks/model_based_rl.md
     - wiki/computational_frameworks/attractor_networks.md
     - index.md

- timestamp: 2026-04-05T21:30:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/botvinick2020_deep_reinforcement_learning_neuro.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 48
    facts_skipped: 0
    pages_created:
      - wiki/computational_frameworks/deep_reinforcement_learning.md
      - wiki/computational_frameworks/meta_reinforcement_learning.md
      - wiki/computational_frameworks/distributional_rl.md
      - wiki/computational_frameworks/experience_replay.md
      - wiki/computational_frameworks/hierarchical_rl.md
    pages_updated:
      - wiki/computational_frameworks/reinforcement_learning.md
      - wiki/computational_frameworks/model_based_rl.md
      - wiki/computational_frameworks/temporal_difference_learning.md
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/brain_regions/ventral_tegmental_area.md
      - wiki/brain_regions/hippocampus.md
      - wiki/brain_regions/striatum.md
      - index.md

  - timestamp: 2026-04-05T17:14:05
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/spiers2015_detour_problem_navigation.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 5
    facts_skipped: 0
    pages_created:
      - wiki/behaviours/detours.md
    pages_updated:
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/brain_regions/hippocampus.md
      - wiki/behaviours/spatial_navigation.md
      - index.md

  - timestamp: 2026-04-05T17:14:05
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/mcnaughton2022_route_cognitive_map.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 5
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/hippocampus.md
      - wiki/behaviours/hippocampal_replay.md
      - wiki/behaviours/spatial_navigation.md
      - index.md

  - timestamp: 2026-04-05T17:14:05
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/patai2021_versatile_wayfinder_prefrontal.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 6
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/brain_regions/hippocampus.md
      - wiki/behaviours/spatial_navigation.md
      - wiki/behaviours/detours.md
      - index.md

  - timestamp: 2026-04-05T17:14:05
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/steffenach2005_spatial_memory_entorhinal.md
    facts_extracted: 4
    facts_routed: 4
    facts_written: 4
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/dorsolateral_entorhinal_cortex.md
      - wiki/brain_regions/ventromedial_entorhinal_cortex.md
    pages_updated:
      - wiki/brain_regions/entorhinal_cortex.md
      - wiki/brain_regions/hippocampus.md
      - wiki/behaviours/spatial_navigation.md
      - index.md

  - timestamp: 2026-04-05T17:14:05
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/vann2009_retrosplenial_cortex_memory.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 6
    facts_skipped: 0
    pages_created:
      - wiki/brain_regions/retrosplenial_cortex.md
    pages_updated:
      - wiki/brain_regions/hippocampus.md
      - wiki/behaviours/spatial_navigation.md
      - index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/fiete2008_grid_cells_position.md
  facts_extracted: 8
  facts_routed: 8
  facts_written: 32
  facts_skipped: 0
  pages_created:
    - wiki/computational_frameworks/residue_number_system.md
  pages_updated:
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/behaviours/grid_cells.md
    - wiki/behaviours/place_cells.md
    - wiki/behaviours/path_integration.md
    - wiki/index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/burak2009_path_integration_grid_cells.md
  facts_extracted: 5
  facts_routed: 5
  facts_written: 20
  facts_skipped: 0
  pages_created:
    - wiki/behaviours/path_integration.md
  pages_updated:
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/computational_frameworks/attractor_networks.md
    - wiki/index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/eldar2020_replay_planning.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 16
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/forward_replay.md
    - wiki/behaviours/memory_consolidation.md
    - wiki/behaviours/habits.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/model_free_rl.md
    - wiki/brain_regions/hippocampus.md
    - wiki/index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/decothi2022_predictive_spatial_navigation.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 16
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/computational_frameworks/successor_representation.md
    - wiki/index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/garvert2017_relational_knowledge_maps.md
  facts_extracted: 3
  facts_routed: 3
  facts_written: 12
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/entorhinal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/behaviours/cognitive_map.md
    - wiki/computational_frameworks/successor_representation.md
    - wiki/index.md

  - timestamp: 2026-04-05T22:00:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/elgaby2023_behavioral_structure_mapping.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 32
    facts_skipped: 0
    pages_created:
      - wiki/behaviours/event_segmentation.md
    pages_updated:
      - wiki/brain_regions/medial_prefrontal_cortex.md
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/behaviours/goal_directed_behaviour.md
      - wiki/behaviours/planning.md
      - wiki/computational_frameworks/attractor_networks.md
      - index.md

  - timestamp: 2026-04-05T22:05:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/schapiro2013_event_representation_memory.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 13
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/medial_prefrontal_cortex.md
      - wiki/brain_regions/inferior_frontal_gyrus.md
      - wiki/brain_regions/superior_temporal_gyrus.md
      - wiki/behaviours/event_segmentation.md

  - timestamp: 2026-04-05T22:10:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/stoianov2020_hierarchical_generative_model.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 20
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/hippocampus.md
      - wiki/behaviours/hippocampal_replay.md
      - wiki/behaviours/memory_consolidation.md
      - wiki/computational_frameworks/experience_replay.md

  - timestamp: 2026-04-05T22:15:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/duncan1996_intelligence_frontal_goal.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 20
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/behaviours/cognitive_impairment.md
      - wiki/behaviours/goal_directed_behaviour.md

- timestamp: 2026-04-05T23:00:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 36
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/behaviours/sharp_wave_ripples.md
      - wiki/behaviours/hippocampal_replay.md
      - wiki/brain_regions/medial_prefrontal_cortex.md
      - wiki/brain_regions/hippocampus_ca1.md
      - wiki/brain_regions/prefrontal_cortex.md

- timestamp: 2026-04-05T23:15:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 25
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/computational_frameworks/meta_reinforcement_learning.md
      - wiki/behaviours/forward_replay.md
      - wiki/behaviours/hippocampal_replay.md
      - wiki/behaviours/planning.md
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/brain_regions/hippocampus.md

- timestamp: 2026-04-05T23:30:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/jeong2022_mesolimbic_dopamine_causal.md
    facts_extracted: 7
    facts_routed: 7
    facts_written: 35
    facts_skipped: 0
    pages_created:
      - wiki/computational_frameworks/anccr.md
    pages_updated:
      - wiki/brain_regions/ventral_striatum.md
      - wiki/brain_regions/ventral_tegmental_area.md
      - wiki/computational_frameworks/temporal_difference_learning.md
      - wiki/behaviours/conditioning.md

- timestamp: 2026-04-05T23:45:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md
    facts_extracted: 6
    facts_routed: 6
    facts_written: 30
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/medial_prefrontal_cortex.md
      - wiki/behaviours/hippocampal_replay.md
      - wiki/behaviours/forward_replay.md
      - wiki/behaviours/spatial_navigation.md
      - wiki/brain_regions/hippocampus.md

- timestamp: 2026-04-06T00:00:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/kaplan2018_active_inference_navigation.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 20
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/computational_frameworks/active_inference.md
      - wiki/behaviours/planning.md
      - wiki/behaviours/spatial_navigation.md
      - wiki/behaviours/exploration.md
      - wiki/brain_regions/hippocampus.md

  - timestamp: 2026-04-05T22:20:00
    agent: fact_finder+router+wiki_writer
    event: facts_routed_and_written
    source_summary: raw/summaries/goel2013_prefrontal_planning_real_world.md
    facts_extracted: 5
    facts_routed: 5
    facts_written: 20
    facts_skipped: 0
    pages_created: []
    pages_updated:
      - wiki/brain_regions/prefrontal_cortex.md
      - wiki/behaviours/planning.md
      - wiki/behaviours/goal_directed_behaviour.md

- timestamp: 2026-04-05T23:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/miller2019_retrosplenial_spatial_learning.md
  facts_extracted: 5
  facts_routed: 5
  facts_written: 5
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/retrosplenial_cortex.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/behaviours/goal_directed_behaviour.md
    - wiki/behaviours/learning.md

- timestamp: 2026-04-05T23:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/nyberg2022_spatial_goal_coding.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 7
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/hippocampus_ca1.md
    - wiki/brain_regions/hippocampus_ca3.md
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/brain_regions/ventral_tegmental_area.md
    - wiki/behaviours/place_cells.md
    - wiki/behaviours/grid_cells.md
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/behaviours/goal_directed_behaviour.md

- timestamp: 2026-04-05T23:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/ormond2022_goal_oriented_vector_fields.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 7
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/hippocampus_ca1.md
    - wiki/behaviours/place_cells.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/behaviours/goal_directed_behaviour.md
    - wiki/behaviours/decision_making.md
    - wiki/behaviours/learning.md

- timestamp: 2026-04-05T23:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/ouchi2024_predictive_grid_coding.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 7
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/brain_regions/hippocampus_ca1.md
    - wiki/behaviours/grid_cells.md
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/spatial_navigation.md

- timestamp: 2026-04-05T23:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/piray2025_compositional_cognitive_map.md
  facts_extracted: 6
  facts_routed: 6
  facts_written: 6
  facts_skipped: 0
  pages_created:
    - wiki/computational_frameworks/compositionality.md
    - wiki/behaviours/learning.md
  pages_updated:
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/behaviours/grid_cells.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/behaviours/planning.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/successor_representation.md
    - index.md

- timestamp: 2026-04-05T23:30:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/khona2022_attractor_integrator.md
  facts_extracted: 7
  facts_routed: 7
  facts_written: 31
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/head_direction_circuit.md
    - wiki/brain_regions/brainstem_oculomotor_integrator.md
    - wiki/brain_regions/anterior_lateral_motor_cortex.md
  pages_updated:
    - wiki/computational_frameworks/attractor_networks.md
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/brain_regions/prefrontal_cortex.md
    - index.md

- timestamp: 2026-04-05T23:45:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/knudsen2020_ofc_theta_learning.md
  facts_extracted: 5
  facts_routed: 5
  facts_written: 16
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/orbitofrontal_cortex.md
  pages_updated:
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/prefrontal_cortex.md
    - index.md

- timestamp: 2026-04-05T23:50:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/knudsen2022_ofc_cognitive_map.md
  facts_extracted: 6
  facts_routed: 6
  facts_written: 18
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/successor_representation.md
    - index.md

- timestamp: 2026-04-05T23:55:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/liu2019_human_replay_reorganizes.md
  facts_extracted: 8
  facts_routed: 8
  facts_written: 30
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/forward_replay.md
    - wiki/behaviours/reverse_replay.md
    - wiki/behaviours/sharp_wave_ripples.md
    - wiki/brain_regions/hippocampus.md
    - index.md

- timestamp: 2026-04-06T00:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/makino2022_arithmetic_value_hierarchical.md
  facts_extracted: 11
  facts_routed: 11
  facts_written: 33
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/computational_frameworks/hierarchical_rl.md
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/brain_regions/primary_motor_cortex.md
    - wiki/brain_regions/secondary_motor_cortex.md
    - wiki/brain_regions/posterior_parietal_cortex.md
    - index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/steffenach2005_spatial_memory_entorhinal.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 4
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/dorsolateral_entorhinal_cortex.md
    - wiki/brain_regions/ventromedial_entorhinal_cortex.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/vann2009_retrosplenial_cortex_memory.md
  facts_extracted: 5
  facts_routed: 5
  facts_written: 5
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/retrosplenial_cortex.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/wang2020_allen_mouse_brain_atlas.md
  facts_extracted: 3
  facts_routed: 3
  facts_written: 3
  facts_skipped: 0
  pages_created:
    - wiki/methods/allen_mouse_brain_atlas.md
  pages_updated: []

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/paulk2022_neuropixels_human_cortex.md
  facts_extracted: 3
  facts_routed: 3
  facts_written: 3
  facts_skipped: 0
  pages_created:
    - wiki/methods/neuropixels.md
  pages_updated: []

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/pachitariu2023_kilosort_spike_sorting.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 4
  facts_skipped: 0
  pages_created:
    - wiki/methods/kilosort.md
  pages_updated: []

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/chung2022_neural_recording_neuropixels.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 4
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/methods/neuropixels.md

- timestamp: 2026-04-06T01:00:00
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/reinert2021_mouse_prefrontal_categorization.md
    - raw/summaries/campbell2025_hardwired_circuit_td_learning.md
    - raw/summaries/brunec2022_predictive_representations_hierarchies.md
    - raw/summaries/bowler2023_cortical_inputs_hippocampal_ca1.md
    - raw/summaries/brown2016_prospective_goals_hippocampus.md
    - raw/summaries/hok2005_goal_coding_prefrontal.md
    - raw/summaries/hok2013_prefrontal_place_cells.md
    - raw/summaries/hasz2020_spatial_encoding_deliberation.md
    - raw/summaries/denbakker2024_mpfc_spatial_swr.md
    - raw/summaries/gridchyn2020_replay_selective_memory.md
  facts_extracted: 58
  facts_routed: 58
  facts_written: 58
  facts_skipped: 0
  pages_created:
    - wiki/behaviours/categorization.md
    - wiki/brain_regions/lateral_entorhinal_cortex.md
    - wiki/brain_regions/anterior_prefrontal_cortex.md
    - wiki/brain_regions/nucleus_accumbens.md
  pages_updated:
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/ventral_tegmental_area.md
    - wiki/brain_regions/striatum.md
    - wiki/computational_frameworks/temporal_difference_learning.md
    - wiki/computational_frameworks/successor_representation.md
    - wiki/behaviours/planning.md
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/memory_consolidation.md
    - index.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/gridchyn2020_replay_selective_memory.md
  facts_extracted: 3
  facts_routed: 3
  facts_written: 3
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/hippocampus.md
    - wiki/behaviours/hippocampal_replay.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/denbakker2024_mpfc_spatial_swr.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 4
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/behaviours/sharp_wave_ripples.md

- timestamp: 2026-04-05T22:00:00
  agent: fact_finder+router+wiki_writer
  event: facts_routed_and_written
  source_summary: raw/summaries/samborska2021_hippocampus_prefrontal_gen.md
  facts_extracted: 4
  facts_routed: 4
  facts_written: 4
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/brain_regions/hippocampus.md


- timestamp: 2026-04-05T23:30:00
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/jadhav2016_hippocampal_prefrontal_swr.md
    - raw/summaries/jensen2024_recurrent_planning_hippocampal_replay.md
    - raw/summaries/jeong2022_mesolimbic_dopamine_causal.md
    - raw/summaries/kaefer2020_mpfc_replay_ruleswitching.md
    - raw/summaries/kaplan2018_active_inference_navigation.md
    - raw/summaries/behrens2007_learning_value_information_uncertain.md
    - raw/summaries/behrens2018_cognitive_map_organizing_knowledge.md
    - raw/summaries/balleine1998_goal_directed_instrumental_action.md
    - raw/summaries/botvinick2012_planning_inference.md
    - raw/summaries/daw2011_model_based_striatal_prediction.md
  facts_extracted: 59
  facts_routed: 59
  facts_written: 59
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/insular_cortex.md
  pages_updated:
    - wiki/brain_regions/anterior_cingulate_cortex.md
    - wiki/brain_regions/prelimbic_cortex.md
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/behaviours/sharp_wave_ripples.md
    - wiki/computational_frameworks/meta_reinforcement_learning.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/active_inference.md
    - index.md
    - log.md

- timestamp: 2026-04-06T02:00:00
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/rouach2008_astrocyte_metabolism.md
    - raw/summaries/yi2018_gap_junction_astrocytes.md
    - raw/summaries/devuyst2009_calcium_connexin43_hemichannels.md
    - raw/summaries/paulson2000_cyclic_amp_gap_junction.md
    - raw/summaries/solan2007_phosphorylation_connexin43.md
    - raw/summaries/rackauskas2007_gap_junction_permeability.md
    - raw/summaries/muller1996_bergmann_glial_coupling.md
    - raw/summaries/davis2013_homeostatic_signaling_neural_stabilization.md
    - raw/summaries/anderson2021_cannabigerolic_seizures.md
    - raw/summaries/anderson2019_cannabidiol_clobazam_seizure.md
  facts_extracted: 63
  facts_routed: 63
  facts_written: 63
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/astrocytes.md
    - wiki/brain_regions/cerebellum.md
    - wiki/computational_frameworks/homeostatic_plasticity.md
    - wiki/behaviours/epilepsy.md
    - wiki/methods/gap_junction_recordings.md
  pages_updated:
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/prefrontal_cortex.md
    - index.md

- timestamp: 2026-04-05T17:36:03
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/badre2018_frontal_cortex_hierarchical_control.md
    - raw/summaries/badre2019_hierarchical_cognitive_control_lobes.md
    - raw/summaries/russek2017_model_based_reinforcement.md
    - raw/summaries/schuck2016_orbitofrontal_cortex_state.md
    - raw/summaries/padoaschioppa2006_orbitofrontal_economic_value.md
    - raw/summaries/stoianov2020_hierarchical_generative_model.md
    - raw/summaries/niv2019_representation_learning_task_states.md
    - raw/summaries/redish2016_vicarious_trial_error.md
    - raw/summaries/berners2022_hippocampal_replay_experience.md
    - raw/summaries/gillespie2021_replay_past_experiences.md
  facts_extracted: 63
  facts_routed: 63
  facts_written: 276
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/mid_dlpfc.md
    - wiki/brain_regions/rostrolateral_prefrontal_cortex.md
    - wiki/brain_regions/dorsolateral_striatum.md
    - wiki/brain_regions/dorsomedial_striatum.md
    - wiki/brain_regions/presupplementary_motor_area.md
    - wiki/behaviours/hierarchical_cognitive_control.md
    - wiki/behaviours/vicarious_trial_error.md
    - wiki/computational_frameworks/hierarchical_control_architecture.md
    - wiki/computational_frameworks/corticostriatal_gating.md
  pages_updated:
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/behaviours/hippocampal_replay.md
    - index.md

- timestamp: 2026-04-05T17:43:02
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/botvinick2008_hierarchical_behavior_prefrontal.md
    - raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md
    - raw/summaries/botvinick2009_hierarchically_organized_behavior.md
    - raw/summaries/botvinick2019_reinforcement_learning_fast_slow.md
    - raw/summaries/bouhadjar2022_coherent_noise_sequence_replay.md
    - raw/summaries/bowling2022_reward_hypothesis_reinforcement.md
    - raw/summaries/braun2018_maps_network_mental_disorders.md
    - raw/summaries/carvalho2021_farm_object_centric.md
    - raw/summaries/craver2013_mechanisms_discovery_biology.md
    - raw/summaries/dordek2016_grid_cells_nonnegative_pca.md
    - raw/summaries/dorrell2023_actionable_grid_constraints.md
  facts_extracted: 40
  facts_routed: 40
  facts_written: 40
  facts_skipped: 0
  pages_created:
    - wiki/brain_regions/dorsolateral_prefrontal_cortex.md
  pages_updated:
    - wiki/computational_frameworks/hierarchical_rl.md
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/dorsolateral_striatum.md
    - wiki/computational_frameworks/attractor_networks.md
    - wiki/computational_frameworks/deep_reinforcement_learning.md
    - wiki/computational_frameworks/meta_reinforcement_learning.md
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - index.md
    - log.md

- timestamp: 2026-04-05T17:53:09
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/izquierdo2024_prefrontal_cortex_homology.md
    - raw/summaries/janssen2022_hierarchical_rl_motor_sequences.md
    - raw/summaries/jazi2023_hippocampal_path_integration_homing.md
    - raw/summaries/jiang2022_learning_options_compression.md
    - raw/summaries/johnson2007_hippocampus_decision.md
    - raw/summaries/jones2005_theta_hippocampal_prefrontal.md
    - raw/summaries/jonesgotman1977_design_fluency_frontal.md
    - raw/summaries/kaar2019_parvalbumin_schizophrenia.md
    - raw/summaries/kaefer2020_replay_prefrontal_rule_switching.md
    - raw/summaries/kashay2022_anterior_cingulate_effort.md
  facts_extracted: 60
  facts_routed: 60
  facts_written: 60
  facts_skipped: 0
  pages_created:
    - wiki/behaviours/design_fluency.md
    - wiki/behaviours/effort_based_decision_making.md
  pages_updated:
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/brain_regions/anterior_cingulate_cortex.md
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/hippocampus_ca3.md
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/computational_frameworks/hierarchical_rl.md
    - wiki/computational_frameworks/mixed_selectivity.md
    - wiki/behaviours/path_integration.md
    - wiki/behaviours/schizophrenia.md
    - index.md

- timestamp: 2026-04-05T17:53:53
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/reznikova2017_hunting_behavior_mouse.md
    - raw/summaries/leblond2003_locomotion_spinal.md
    - raw/summaries/otchy2015_neural_circuit_motor.md
    - raw/summaries/yang2022_monkey_pacman_strategy.md
    - raw/summaries/yang2022_thalamus_frontal_decision.md
    - raw/summaries/kubska2021_single_neuron_cognition.md
    - raw/summaries/redish2016_vicarious_trial_error.md
    - raw/summaries/samborska2021_hippocampus_prefrontal_gen.md
    - raw/summaries/gridchyn2020_replay_selective_memory.md
    - raw/summaries/schmidt2021_mpfc_swr_dreadd.md
    - raw/summaries/denbakker2024_mpfc_spatial_swr.md
    - raw/summaries/berners2022_hippocampal_replay_experience.md
    - raw/summaries/gillespie2021_replay_past_experiences.md
    - raw/summaries/bouhadjar2022_coherent_noise_sequence_replay.md
    - raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal.md
  facts_extracted: 78
  facts_routed: 78
  facts_written: 78
  facts_skipped: 0
  pages_created: 18
  pages_updated: 22

- timestamp: 2026-04-05T17:58:29
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/keramati2016_plan_until_habit.md
    - raw/summaries/kennerley2009_frontal_outcome_value.md
    - raw/summaries/kemp2008_structural_discovery_form.md
    - raw/summaries/kashay2023_ACC_effort_decision.md
    - raw/summaries/zhou2021_schema_orbitofrontal.md
    - raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md
    - raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md
    - raw/summaries/benjamin2018_statistical_significance.md
    - raw/summaries/berner2019_dota_reinforcement_learning.md
    - raw/summaries/bernerslee2021_prefrontal_cortex_hippocampal.md
    - raw/summaries/beyeler2019_sparse_coding_dimensionality.md
    - raw/summaries/bhattacherjee2022_prefrontal_spatial_transcriptomics.md
    - raw/summaries/bialek2022_behavior_dynamics_analysis.md
    - raw/summaries/binz2024_meta_learning_cognition.md
    - raw/summaries/blancopolzo2024_dopamine_independent_reward.md
    - raw/summaries/bongioanni2021_novel_choice_neural.md
    - raw/summaries/basu2021_ofc_navigation_goals.md
    - raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md
    - raw/summaries/durstewitz2020_psychiatric_network_dynamics.md
    - raw/summaries/fried2020_mental_health_complexity.md
  facts_extracted: 127
  facts_routed: 127
  facts_written: 127
  facts_skipped: 0
  pages_created:
    - wiki/behaviours/effort_based_decision_making.md
  pages_updated:
    - wiki/brain_regions/anterior_cingulate_cortex.md
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/behaviours/hippocampal_replay.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/meta_reinforcement_learning.md
    - index.md
    - log.md

- timestamp: 2026-04-05T18:03:54
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/kurth_nelson2016_sequences_non_spatial.md
    - raw/summaries/lacroix2002_medial_prefrontal_spatial.md
    - raw/summaries/leblond2003_locomotion_spinal.md
    - raw/summaries/loosen2020_computational_psychiatry_ocd.md
    - raw/summaries/manns2009_cognitive_map_object_memory.md
    - raw/summaries/meunier2024_nonlinear_metalearning.md
    - raw/summaries/otchy2015_neural_circuit_motor.md
    - raw/summaries/ouchi2024_predictive_grid_coding.md
    - raw/summaries/patai2021_versatile_wayfinder_prefrontal.md
    - raw/summaries/piray2025_compositional_cognitive_map.md
    - raw/summaries/reinert2021_mouse_prefrontal_categorization.md
    - raw/summaries/reznikova2017_hunting_behavior_mouse.md
    - raw/summaries/russek2017_model_based_reinforcement.md
    - raw/summaries/schuck2016_orbitofrontal_cortex_state.md
    - raw/summaries/spiers2015_detour_problem_navigation.md
    - raw/summaries/stoianov2020_hierarchical_generative_model.md
    - raw/summaries/niv2019_representation_learning_task_states.md
    - raw/summaries/redish2016_vicarious_trial_error.md
    - raw/summaries/berners2022_hippocampal_replay_experience.md
  facts_extracted: 127
  facts_routed: 127
  facts_written: 127
  facts_skipped: 0
  pages_created:
    - wiki/behaviours/object_location_memory.md
    - wiki/behaviours/obsessive_compulsive_disorder.md
  pages_updated:
    - wiki/behaviours/hippocampal_replay.md
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/computational_frameworks/meta_reinforcement_learning.md
    - wiki/behaviours/spatial_navigation.md
    - index.md

- timestamp: 2026-04-05T18:15:00
  agent: fact_finder+router+wiki_writer
  event: batch_facts_routed_and_written
  source_summaries:
    - raw/summaries/kashay2023_ACC_effort_decision.md
    - raw/summaries/kennerley2009_frontal_outcome_value.md
    - raw/summaries/keramati2016_plan_until_habit.md
    - raw/summaries/kemp2008_structural_discovery_form.md
    - raw/summaries/manns2009_cognitive_map_object_memory.md
    - raw/summaries/loosen2020_computational_psychiatry_ocd.md
    - raw/summaries/lacroix2002_medial_prefrontal_spatial.md
    - raw/summaries/leblond2003_locomotion_spinal.md
    - raw/summaries/otchy2015_neural_circuit_motor.md
    - raw/summaries/reznikova2017_hunting_behavior_mouse.md
    - raw/summaries/yang2022_monkey_pacman_strategy.md
    - raw/summaries/yang2022_thalamus_frontal_decision.md
    - raw/summaries/zhong2016_astrocytes_electrophysiology.md
    - raw/summaries/zhang2022_hyperbolic_geometry_hippocampus.md
    - raw/summaries/zeithamova2012_hippocampal_inference.md
    - raw/summaries/zutshi2022_extrinsic_intrinsic_ca1.md
    - raw/summaries/zutshi2023_sharp_wave_ripples_entorhinal.md
    - raw/summaries/zielinski2019_theta_hippocampus_prefrontal.md
    - raw/summaries/yu2025_theta_sweeps_goal_direction.md
    - raw/summaries/yu2018_hippocampal_cortical_memory.md
    - raw/summaries/yu2015_hippocampal_cortical_interaction.md
    - raw/summaries/yuan2024_experience_replay_successor.md
    - raw/summaries/yoshida2006_resolution_uncertainty.md
  facts_extracted: 142
  facts_routed: 142
  facts_written: 142
  facts_skipped: 0
  pages_created:
    - wiki/computational_frameworks/plan_until_habit.md
    - wiki/computational_frameworks/structural_form_discovery.md
    - wiki/behaviours/monkey_pacman_strategy.md
    - wiki/behaviours/theta_sweeps.md
    - wiki/behaviours/hippocampal_cortical_interaction.md
    - wiki/behaviours/hippocampal_inference.md
    - wiki/behaviours/uncertainty_resolution.md
    - wiki/brain_regions/thalamus.md
    - wiki/computational_frameworks/hyperbolic_geometry.md
  pages_updated:
    - wiki/brain_regions/anterior_cingulate_cortex.md
    - wiki/brain_regions/prefrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/hippocampus_ca1.md
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/medial_entorhinal_cortex.md
    - wiki/behaviours/object_location_memory.md
    - wiki/behaviours/obsessive_compulsive_disorder.md
    - wiki/behaviours/locomotion.md
    - wiki/behaviours/hunting_behavior.md
    - wiki/computational_frameworks/permissive_vs_instructive_roles.md
    - wiki/behaviours/effort_based_decision_making.md
    - wiki/behaviours/spatial_navigation.md
    - wiki/behaviours/goal_directed_behaviour.md
    - wiki/behaviours/memory_consolidation.md
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/sharp_wave_ripples.md
    - wiki/behaviours/place_cells.md
    - wiki/behaviours/planning.md
    - wiki/behaviours/decision_making.md
    - wiki/behaviours/learning.md
    - wiki/computational_frameworks/model_based_rl.md
    - wiki/computational_frameworks/successor_representation.md
    - wiki/computational_frameworks/attractor_networks.md
    - wiki/computational_frameworks/experience_replay.md
    - wiki/computational_frameworks/bayesian_inference.md
    - wiki/methods/computational_modeling.md
    - wiki/methods/optogenetics.md
    - index.md
    - log.md

- timestamp: 2026-04-05T18:29:52
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_processed
  source_summaries:
    - raw/summaries/basu2021_ofc_navigation_goals.md
    - raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md
    - raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md
    - raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md
  facts_extracted: 13
  facts_routed: 13
  facts_written: 13
  facts_skipped: 0
  pages_created: []
  pages_updated:
    - wiki/brain_regions/orbitofrontal_cortex.md
    - wiki/brain_regions/hippocampus.md
    - wiki/brain_regions/medial_prefrontal_cortex.md
    - wiki/behaviours/hippocampal_replay.md
    - wiki/behaviours/memory_consolidation.md
    - wiki/behaviours/spatial_navigation.md

- timestamp: 2026-04-05T18:32:28
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_processed
  facts_extracted: 12
  facts_routed: 12
  facts_written: 12
  facts_skipped: 0
  pages_created: []
  pages_updated: ['wiki/brain_regions/hippocampus.md', 'wiki/brain_regions/medial_prefrontal_cortex.md', 'wiki/brain_regions/orbitofrontal_cortex.md']

- timestamp: 2026-04-05T18:32:44
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_processed
  facts_extracted: 12
  facts_routed: 12
  facts_written: 12
  facts_skipped: 0
  pages_created: []
  pages_updated: ['wiki/brain_regions/hippocampus.md', 'wiki/brain_regions/medial_prefrontal_cortex.md', 'wiki/brain_regions/orbitofrontal_cortex.md']
- timestamp: 2026-04-05T18:33:48
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_complete
  source_summaries:
    - raw/summaries/basu2021_ofc_navigation_goals.md
    - raw/summaries/basu2023_goal_pointer_cognitive_map_ofc.md
    - raw/summaries/bein2024_schemas_reinforcement_learning_pfc.md
    - raw/summaries/bendor2012_biasing_hippocampal_replay_sleep.md
    - raw/summaries/benjamin2018_statistical_significance.md
    - raw/summaries/berner2019_dota_reinforcement_learning.md
    - raw/summaries/beyeler2019_sparse_coding_dimensionality.md
    - raw/summaries/bhattacherjee2022_prefrontal_spatial_transcriptomics.md
    - raw/summaries/bialek2022_behavior_dynamics_analysis.md
    - raw/summaries/binz2024_meta_learning_cognition.md
    - raw/summaries/blancopolzo2024_dopamine_independent_reward.md
    - raw/summaries/bongioanni2021_novel_choice_neural.md
    - raw/summaries/botvinick2008_hierarchical_behavior_prefrontal.md
    - raw/summaries/botvinick2009_hierarchical_behavior_reinforcement.md
    - raw/summaries/botvinick2009_hierarchically_organized_behavior.md
    - raw/summaries/botvinick2019_reinforcement_learning_fast_slow.md
    - raw/summaries/bowling2022_reward_hypothesis_reinforcement.md
    - raw/summaries/braun2018_maps_network_mental_disorders.md
    - raw/summaries/carvalho2021_farm_object_centric.md
    - raw/summaries/craver2013_mechanisms_discovery_biology.md
    - raw/summaries/dordek2016_grid_cells_nonnegative_pca.md
    - raw/summaries/dorrell2023_actionable_grid_constraints.md
    - raw/summaries/durstewitz2020_psychiatric_network_dynamics.md
    - raw/summaries/fried2020_mental_health_complexity.md
    - raw/summaries/howes2022_treatment_resistance_psychiatry.md
    - raw/summaries/howes2016_aberrant_salience_schizophrenia.md
    - raw/summaries/ivanov2021_psychotropic_drugs_mental_illness.md
  facts_extracted: 90
  facts_routed: 90
  facts_written: 90
  facts_skipped: 0
  pages_created: ['wiki/behaviours/decision_making.md', 'wiki/behaviours/goal_directed_behaviour.md', 'wiki/behaviours/hippocampal_replay.md', 'wiki/behaviours/memory_consolidation.md', 'wiki/behaviours/psychiatric_disorders.md', 'wiki/behaviours/schema_learning.md', 'wiki/behaviours/spatial_navigation.md', 'wiki/brain_regions/dorsolateral_striatum.md', 'wiki/brain_regions/hippocampus.md', 'wiki/brain_regions/medial_entorhinal_cortex.md', 'wiki/brain_regions/medial_prefrontal_cortex.md', 'wiki/brain_regions/orbitofrontal_cortex.md', 'wiki/brain_regions/prefrontal_cortex.md', 'wiki/brain_regions/ventral_tegmental_area.md', 'wiki/computational_frameworks/deep_reinforcement_learning.md', 'wiki/computational_frameworks/hierarchical_rl.md', 'wiki/computational_frameworks/meta_reinforcement_learning.md', 'wiki/computational_frameworks/reinforcement_learning.md', 'wiki/computational_frameworks/successor_representation.md']
  pages_updated: ['wiki/behaviours/decision_making.md', 'wiki/behaviours/goal_directed_behaviour.md', 'wiki/behaviours/hippocampal_replay.md', 'wiki/behaviours/memory_consolidation.md', 'wiki/behaviours/schema_learning.md', 'wiki/behaviours/spatial_navigation.md', 'wiki/brain_regions/dorsolateral_striatum.md', 'wiki/brain_regions/hippocampus.md', 'wiki/brain_regions/medial_entorhinal_cortex.md', 'wiki/brain_regions/medial_prefrontal_cortex.md', 'wiki/brain_regions/orbitofrontal_cortex.md', 'wiki/brain_regions/prefrontal_cortex.md', 'wiki/brain_regions/ventral_tegmental_area.md', 'wiki/computational_frameworks/deep_reinforcement_learning.md', 'wiki/computational_frameworks/hierarchical_rl.md', 'wiki/computational_frameworks/meta_reinforcement_learning.md', 'wiki/computational_frameworks/reinforcement_learning.md', 'wiki/computational_frameworks/successor_representation.md']

- timestamp: 2026-04-05T18:35:00
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_final_summary
  summary: "Successfully processed 30 summaries through full pipeline"
  facts_extracted: 90
  facts_routed: 90
  facts_written: 90
  facts_skipped: 0
  pages_created: 19
  pages_updated: 18
  status: success


- timestamp: 2026-04-05T18:40:00
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_final
  summary: "Successfully processed 30 summaries through full pipeline"
  facts_extracted: 90
  facts_routed: 90
  facts_written: 90
  facts_skipped: 0
  pages_created: 19
  pages_updated: 18
  status: success

