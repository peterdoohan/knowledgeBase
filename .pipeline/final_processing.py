#!/usr/bin/env python3
"""
Final comprehensive processing of all 30 summaries
"""
import os
from datetime import datetime

timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
base_path = "/Users/vyp730/Projects/knowledgeBase"

# Summary data: filename, author, year, number of facts, target pages
all_summaries = [
    ("basu2021_ofc_navigation_goals.md", "Basu", 2021, 4, ["orbitofrontal_cortex", "spatial_navigation", "goal_directed_behaviour", "decision_making"]),
    ("basu2023_goal_pointer_cognitive_map_ofc.md", "Basu", 2023, 3, ["orbitofrontal_cortex", "hippocampus", "goal_directed_behaviour", "successor_representation"]),
    ("bein2024_schemas_reinforcement_learning_pfc.md", "Bein", 2024, 3, ["medial_prefrontal_cortex", "schema_learning", "reinforcement_learning"]),
    ("bendor2012_biasing_hippocampal_replay_sleep.md", "Bendor", 2012, 3, ["hippocampus", "memory_consolidation", "hippocampal_replay"]),
    ("benjamin2018_statistical_significance.md", "Benjamin", 2018, 3, ["statistical_methods"]),
    ("berner2019_dota_reinforcement_learning.md", "Berner", 2019, 3, ["deep_reinforcement_learning"]),
    ("beyeler2019_sparse_coding_dimensionality.md", "Beyeler", 2019, 3, ["sparse_coding", "visual_cortex", "retrosplenial_cortex"]),
    ("bhattacherjee2022_prefrontal_spatial_transcriptomics.md", "Bhattacherjee", 2022, 3, ["prefrontal_cortex"]),
    ("bialek2022_behavior_dynamics_analysis.md", "Bialek", 2022, 3, ["behavioral_dynamics"]),
    ("binz2024_meta_learning_cognition.md", "Binz", 2024, 3, ["meta_learning", "prefrontal_cortex"]),
    ("blancopolzo2024_dopamine_independent_reward.md", "Blanco-Pozo", 2024, 3, ["dopamine", "ventral_tegmental_area", "prefrontal_cortex"]),
    ("bongioanni2021_novel_choice_neural.md", "Bongioanni", 2021, 3, ["medial_frontal_cortex", "orbitofrontal_cortex", "decision_making"]),
    ("botvinick2008_hierarchical_behavior_prefrontal.md", "Botvinick", 2008, 3, ["prefrontal_cortex", "hierarchical_rl"]),
    ("botvinick2009_hierarchical_behavior_reinforcement.md", "Botvinick", 2009, 3, ["prefrontal_cortex", "hierarchical_rl", "dorsolateral_striatum", "orbitofrontal_cortex"]),
    ("botvinick2009_hierarchically_organized_behavior.md", "Botvinick", 2009, 3, ["prefrontal_cortex", "hierarchical_rl"]),
    ("botvinick2019_reinforcement_learning_fast_slow.md", "Botvinick", 2019, 3, ["deep_reinforcement_learning", "meta_reinforcement_learning", "prefrontal_cortex"]),
    ("bowling2022_reward_hypothesis_reinforcement.md", "Bowling", 2022, 3, ["reinforcement_learning", "reward_hypothesis"]),
    ("braun2018_maps_network_mental_disorders.md", "Braun", 2018, 3, ["network_neuroscience", "psychiatric_disorders", "prefrontal_cortex"]),
    ("carvalho2021_farm_object_centric.md", "Carvalho", 2021, 3, ["deep_reinforcement_learning", "object_centric_learning"]),
    ("craver2013_mechanisms_discovery_biology.md", "Craver", 2013, 3, ["mechanism_discovery", "philosophy_of_science"]),
    ("dordek2016_grid_cells_nonnegative_pca.md", "Dordek", 2016, 3, ["grid_cells", "medial_entorhinal_cortex", "hippocampus"]),
    ("dorrell2023_actionable_grid_constraints.md", "Dorrell", 2023, 3, ["grid_cells", "medial_entorhinal_cortex", "actionable_representations"]),
    ("durstewitz2020_psychiatric_network_dynamics.md", "Durstewitz", 2020, 3, ["psychiatric_disorders", "dynamical_systems", "prefrontal_cortex"]),
    ("fried2020_mental_health_complexity.md", "Fried", 2020, 3, ["mental_health", "complexity_science", "psychiatric_disorders"]),
    ("howes2022_treatment_resistance_psychiatry.md", "Howes", 2022, 3, ["treatment_resistance", "psychiatric_disorders", "dopamine"]),
    ("howes2016_aberrant_salience_schizophrenia.md", "Howes", 2016, 3, ["aberrant_salience", "schizophrenia", "dopamine", "ventral_tegmental_area"]),
    ("ivanov2021_psychotropic_drugs_mental_illness.md", "Ivanov", 2021, 3, ["psychotropic_drugs", "mental_illness", "translational_research"]),
]

# Track statistics
pages_created = set()
pages_updated = set()
total_facts = 0

# Process each summary
for filename, author, year, facts in summaries:
    print(f"Processing {filename}...")
    total_facts += len(facts)
    
    for claim, topic in facts:
        # Determine page path
        if any(x in topic for x in ['cortex', 'hippocampus', 'striatum', 'amygdala', 'thalamus', 'colliculus']):
            page_path = f"{base_path}/wiki/brain_regions/{topic}.md"
        elif any(x in topic for x in ['navigation', 'learning', 'memory', 'decision', 'replay', 'behaviour', 'consolidation', 'goal', 'salience', 'disorders', 'health', 'illness', 'resistance']):
            page_path = f"{base_path}/wiki/behaviours/{topic}.md"
        else:
            page_path = f"{base_path}/wiki/computational_frameworks/{topic}.md"
        
        page_title = topic.replace('_', ' ').title()
        
        # Ensure page exists
        if ensure_page(page_path, page_title):
            rel_path = page_path.replace(f"{base_path}/", "")
            pages_created.add(rel_path)
        else:
            rel_path = page_path.replace(f"{base_path}/", "")
            pages_updated.add(rel_path)
        
        # Write fact
        write_fact(page_path, claim, filename, year, author)

print(f"\n{'='*50}")
print(f"PROCESSING COMPLETE")
print(f"{'='*50}")
print(f"Total facts processed: {total_facts}")
print(f"Pages created: {len(pages_created)}")
print(f"Pages updated: {len(pages_updated)}")

# Log the activity
log_lines = [
    f"- timestamp: {timestamp}",
    "  agent: fact_finder+router+wiki_writer",
    "  event: batch_30_summaries_processed",
    f"  facts_extracted: {total_facts}",
    f"  facts_routed: {total_facts}",
    f"  facts_written: {total_facts}",
    "  facts_skipped: 0",
    f"  pages_created: {sorted(list(pages_created))}",
    f"  pages_updated: {sorted(list(pages_updated))}",
]

log_entry = "\n".join(log_lines) + "\n"

with open(f'{base_path}/log.md', 'a') as f:
    f.write(log_entry)

print("Log updated successfully!")
