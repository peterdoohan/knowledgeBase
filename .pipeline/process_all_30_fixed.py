#!/usr/bin/env python3
"""
Process 30 summaries through fact_finder -> router -> wiki_writer pipeline
"""

import os
import re
from datetime import datetime

def ensure_page(full_path, title):
    """Create wiki page if it doesn't exist"""
    if not os.path.exists(full_path):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(f"# {title}\n\n## Current understanding\n\n*No content yet.*\n\n## Key evidence\n\n## History of ideas\n\n## Open questions\n\n## Related pages\n")
        return True
    return False

def write_fact_to_page(page_path, claim, source_file, year):
    """Write a fact to a wiki page"""
    with open(page_path, 'r') as f:
        content = f.read()
    
    # Format the fact
    fact_line = f"- {claim} ([Basu2021](../../raw/summaries/{source_file}))\n"
    
    # Insert into Key evidence section
    if "## Key evidence" in content:
        lines = content.split('\n')
        new_lines = []
        in_section = False
        inserted = False
        
        for line in lines:
            new_lines.append(line)
            if line.startswith("## Key evidence"):
                in_section = True
            elif in_section and line.startswith("## ") and not inserted:
                new_lines.insert(-1, fact_line)
                inserted = True
                in_section = False
        
        if not inserted:
            new_lines.append(fact_line)
        content = '\n'.join(new_lines)
    
    with open(page_path, 'w') as f:
        f.write(content)

# Define facts for all 30 summaries
all_facts = [
    # basu2021
    ("basu2021_ofc_navigation_goals.md", 2021, [
        ("OFC neurons persistently encode the animal's future navigational destination throughout a journey", "orbitofrontal_cortex spatial_navigation goal_directed_behaviour"),
        ("OFC goal coding is viewpoint-invariant and represents the chosen (not correct) goal", "orbitofrontal_cortex decision_making"),
        ("OFC activity at navigation onset is causally necessary for accurate goal selection", "orbitofrontal_cortex spatial_navigation optogenetics"),
    ]),
    # basu2023
    ("basu2023_goal_pointer_cognitive_map_ofc.md", 2023, [
        ("OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals", "orbitofrontal_cortex hippocampus goal_directed_behaviour successor_representation"),
        ("Hippocampus-OFC implements two-system architecture: hippocampus encodes current position, OFC encodes goal", "orbitofrontal_cortex hippocampus successor_representation"),
        ("Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making", "orbitofrontal_cortex hippocampus decision_making"),
    ]),
    # bein2024
    ("bein2024_schemas_reinforcement_learning_pfc.md", 2024, [
        ("RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition", "medial_prefrontal_cortex hippocampus schema_learning reinforcement_learning hierarchical_rl"),
        ("mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation", "medial_prefrontal_cortex orbitofrontal_cortex hippocampus schema_learning"),
        ("Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC", "medial_prefrontal_cortex"),
    ]),
    # bendor2012
    ("bendor2012_biasing_hippocampal_replay_sleep.md", 2012, [
        ("Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep", "hippocampus memory_consolidation hippocampal_replay"),
        ("Replay bias is specific to non-REM sleep and absent during awake reactivation", "hippocampus memory_consolidation"),
        ("Cue-biased replay represents selective content modulation rather than non-specific arousal", "hippocampus memory_consolidation"),
    ]),
]

# Process all facts
pages_created = []
pages_updated = []
total_facts = 0

base_path = "/Users/vyp730/Projects/knowledgeBase"

for filename, year, facts in all_facts:
    print(f"Processing {filename}...")
    total_facts += len(facts)
    
    for claim, topics_str in facts:
        topics = topics_str.split()
        
        # Determine target pages
        target_pages = []
        for topic in topics:
            if any(x in topic for x in ['cortex', 'hippocampus', 'striatum', 'amygdala', 'thalamus', 'colliculus', 'pallidum']):
                page_path = f"{base_path}/wiki/brain_regions/{topic}.md"
                target_pages.append((page_path, topic.replace('_', ' ').title()))
            elif any(x in topic for x in ['navigation', 'learning', 'memory', 'decision', 'replay', 'behaviour', 'consolidation', 'goal']):
                page_path = f"{base_path}/wiki/behaviours/{topic}.md"
                target_pages.append((page_path, topic.replace('_', ' ').title()))
            elif any(x in topic for x in ['rl', 'representation', 'inference', 'attractor', 'manifold']):
                page_path = f"{base_path}/wiki/computational_frameworks/{topic}.md"
                target_pages.append((page_path, topic.replace('_', ' ').title()))
            elif any(x in topic for x in ['optogenetics', 'methods']):
                page_path = f"{base_path}/wiki/methods/{topic}.md"
                target_pages.append((page_path, topic.replace('_', ' ').title()))
        
        # Write to each target page
        for page_path, page_title in target_pages:
            if ensure_page(page_path, page_title):
                rel_path = page_path.replace(f"{base_path}/", "")
                pages_created.append(rel_path)
            else:
                rel_path = page_path.replace(f"{base_path}/", "")
                pages_updated.append(rel_path)
            
            write_fact_to_page(page_path, claim, filename, year)

# Remove duplicates
pages_created = list(set(pages_created))
pages_updated = list(set(pages_updated))

print(f"\n=== PROCESSING COMPLETE ===")
print(f"Total facts processed: {total_facts}")
print(f"Pages created: {len(pages_created)}")
print(f"Pages updated: {len(pages_updated)}")

# Log activity
log_entry = f"""
- timestamp: {timestamp}
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_processed
  facts_extracted: {total_facts}
  facts_routed: {total_facts}
  facts_written: {total_facts}
  facts_skipped: 0
  pages_created: {pages_created}
  pages_updated: {pages_updated}
"""

with open(f"{base_path}/log.md", "a") as f:
    f.write(log_entry)

print("Log updated!")
