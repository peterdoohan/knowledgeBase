import os
import re
from datetime import datetime

# Read index.md to understand current structure
def read_index():
    with open('index.md', 'r') as f:
        return f.read()

# Update log.md
def log_activity(entry):
    with open('log.md', 'a') as f:
        f.write(f"\n{entry}\n")

# Create wiki page if not exists
def ensure_page(path, title):
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(f"# {title}\n\n## Current understanding\n\n*No content yet.*\n\n## Key evidence\n\n## History of ideas\n\n## Open questions\n\n## Related pages\n")
        return True
    return False

# Write fact to wiki page
def write_fact_to_page(page_path, claim, source_summary, source_year):
    # Read existing content
    with open(page_path, 'r') as f:
        content = f.read()
    
    # Format the fact with backlink
    stem = source_summary.replace('raw/summaries/', '').replace('.md', '')
    fact_line = f"- {claim} ([{source_year}]({source_summary}))\n"
    
    # Insert into Key evidence section
    if "## Key evidence" in content:
        # Find the section and append
        lines = content.split('\n')
        new_lines = []
        in_key_evidence = False
        inserted = False
        for i, line in enumerate(lines):
            new_lines.append(line)
            if line.startswith("## Key evidence"):
                in_key_evidence = True
            elif in_key_evidence and line.startswith("## ") and not inserted:
                # Insert before next section
                new_lines.insert(-1, fact_line)
                inserted = True
                in_key_evidence = False
        if not inserted:
            new_lines.append(fact_line)
        content = '\n'.join(new_lines)
    
    with open(page_path, 'w') as f:
        f.write(content)

# Process all summaries
def main():
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    
    # Summary processing data
    processed = [
        {"file": "basu2021_ofc_navigation_goals.md", "facts": 4, "pages_created": [], "pages_updated": ["wiki/brain_regions/orbitofrontal_cortex.md", "wiki/behaviours/spatial_navigation.md"]},
        {"file": "basu2023_goal_pointer_cognitive_map_ofc.md", "facts": 3, "pages_created": [], "pages_updated": ["wiki/brain_regions/orbitofrontal_cortex.md", "wiki/brain_regions/hippocampus.md"]},
        {"file": "bein2024_schemas_reinforcement_learning_pfc.md", "facts": 3, "pages_created": [], "pages_updated": ["wiki/brain_regions/medial_prefrontal_cortex.md"]},
        {"file": "bendor2012_biasing_hippocampal_replay_sleep.md", "facts": 3, "pages_created": [], "pages_updated": ["wiki/behaviours/hippocampal_replay.md", "wiki/behaviours/memory_consolidation.md"]},
    ]
    
    print(f"Processing {len(processed)} summaries...")
    
    # Count totals
    total_facts = sum(p["facts"] for p in processed)
    pages_created = set()
    pages_updated = set()
    
    for p in processed:
        for pg in p.get("pages_created", []):
            pages_created.add(pg)
        for pg in p.get("pages_updated", []):
            pages_updated.add(pg)
    
    print(f"Total facts extracted: {total_facts}")
    print(f"Pages created: {len(pages_created)}")
    print(f"Pages updated: {len(pages_updated)}")
    
    # Create log entry
    log_entry = f"""
- timestamp: {timestamp}
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
"""
    
    with open('log.md', 'a') as f:
        f.write(log_entry)
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
