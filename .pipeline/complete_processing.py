#!/usr/bin/env python3
import os
from datetime import datetime

timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
base_path = "/Users/vyp730/Projects/knowledgeBase"

def ensure_page(page_path, title):
    if not os.path.exists(page_path):
        os.makedirs(os.path.dirname(page_path), exist_ok=True)
        with open(page_path, 'w') as f:
            f.write(f"# {title}\n\n## Current understanding\n\n*No content yet.*\n\n## Key evidence\n\n## History of ideas\n\n## Open questions\n\n## Related pages\n")
        return True
    return False

def write_fact(page_path, claim, source_file, year, author):
    with open(page_path, 'r') as f:
        content = f.read()
    
    fact_line = f"- {claim} ([{author}{year}](../../raw/summaries/{source_file}))\n"
    
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

# Define facts for processing
facts_to_process = [
    # basu2021
    ("basu2021_ofc_navigation_goals.md", "Basu", 2021, [
        ("OFC neurons persistently encode the animal's future navigational destination throughout a journey", "orbitofrontal_cortex"),
        ("OFC goal coding is viewpoint-invariant and represents the chosen (not correct) goal", "orbitofrontal_cortex"),
        ("OFC activity at navigation onset is causally necessary for accurate goal selection", "orbitofrontal_cortex"),
    ]),
    # basu2023
    ("basu2023_goal_pointer_cognitive_map_ofc.md", "Basu", 2023, [
        ("OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals", "orbitofrontal_cortex"),
        ("Hippocampus-OFC implements two-system architecture: hippocampus encodes current position (SR/map), OFC encodes goal (reward vector)", "orbitofrontal_cortex"),
        ("Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making", "orbitofrontal_cortex"),
    ]),
    # bein2024
    ("bein2024_schemas_reinforcement_learning_pfc.md", "Bein", 2024, [
        ("RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition", "medial_prefrontal_cortex"),
        ("mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation", "medial_prefrontal_cortex"),
        ("Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC", "medial_prefrontal_cortex"),
    ]),
    # bendor2012
    ("bendor2012_biasing_hippocampal_replay_sleep.md", "Bendor", 2012, [
        ("Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep", "hippocampus"),
        ("Replay bias is specific to non-REM sleep and absent during awake reactivation", "hippocampus"),
        ("Cue-biased replay represents selective content modulation rather than non-specific arousal", "hippocampus"),
    ]),
]

# Process all facts
pages_created = set()
pages_updated = set()
total_facts = 0

for filename, author, year, facts in facts_to_process:
    print(f"Processing {filename}...")
    total_facts += len(facts)
    
    for claim, topic in facts:
        page_path = f"{base_path}/wiki/brain_regions/{topic}.md"
        page_title = topic.replace('_', ' ').title()
        
        if ensure_page(page_path, page_title):
            rel_path = f"wiki/brain_regions/{topic}.md"
            pages_created.add(rel_path)
        else:
            rel_path = f"wiki/brain_regions/{topic}.md"
            pages_updated.add(rel_path)
        
        write_fact(page_path, claim, filename, year, author)

print(f"\n=== PROCESSING COMPLETE ===")
print(f"Total facts: {total_facts}")
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
  pages_created: {sorted(list(pages_created))}
  pages_updated: {sorted(list(pages_updated))}
"""

with open(f'{base_path}/log.md', 'a') as f:
    f.write(log_entry)

print("Log updated!")
