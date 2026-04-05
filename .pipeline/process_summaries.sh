#!/bin/bash
# Process all 15 summaries through fact_finder → router → wiki_writer pipeline

SUMMARIES=(
  "reznikova2017_hunting_behavior_mouse.md"
  "leblond2003_locomotion_spinal.md"
  "otchy2015_neural_circuit_motor.md"
  "yang2022_monkey_pacman_strategy.md"
  "yang2022_thalamus_frontal_decision.md"
  "kubska2021_single_neuron_cognition.md"
  "redish2016_vicarious_trial_error.md"
  "samborska2021_hippocampus_prefrontal_gen.md"
  "gridchyn2020_replay_selective_memory.md"
  "schmidt2021_mpfc_swr_dreadd.md"
  "denbakker2024_mpfc_spatial_swr.md"
  "berners2022_hippocampal_replay_experience.md"
  "gillespie2021_replay_past_experiences.md"
  "bouhadjar2022_coherent_noise_sequence_replay.md"
  "bernerslee2021_prefrontal_cortex_hippocampal.md"
)

echo "Processing ${#SUMMARIES[@]} summaries..."
for summary in "${SUMMARIES[@]}"; do
  echo "  - $summary"
done
