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

# Facts 5-26 (remaining summaries)
facts_to_process = [
    # benjamin2018
    ("benjamin2018_statistical_significance.md", "Benjamin", 2018, [
        ("P-value threshold for claiming new discoveries should be lowered from 0.05 to 0.005", "statistical_methods"),
        ("Empirical replication rates approximately double when initial studies used P < 0.005 versus 0.005 < P < 0.05", "statistical_methods"),
        ("Maintaining 80% power under the new threshold requires approximately 70% larger sample sizes", "statistical_methods"),
    ]),
    # berner2019
    ("berner2019_dota_reinforcement_learning.md", "Berner", 2019, [
        ("OpenAI Five demonstrates that existing deep RL methods scaled to ~770 PFLOPs/s·days can defeat Dota 2 world champions", "deep_reinforcement_learning"),
        ("Batch size scaling yields ~2.5× speedup to reach skill threshold; speedup increases at higher skill levels", "deep_reinforcement_learning"),
        ("Surgery methodology enables continuing training across model/environment changes at ~20% cost of restarting", "deep_reinforcement_learning"),
    ]),
    # beyeler2019
    ("beyeler2019_sparse_coding_dimensionality.md", "Beyeler", 2019, [
        ("Nonnegative sparse coding (NSC) can account for neuronal response properties across sensory areas, associative cortices, and basal ganglia", "sparse_coding"),
        ("NSC applied to natural images yields V1-like oriented, spatially localized simple-cell receptive fields", "visual_cortex"),
        ("NMF applied to rat RSC electrophysiology recovers sparse, parts-based representations of allocentric position, head direction, and route-based movement direction", "retrosplenial_cortex"),
    ]),
    # bhattacherjee2022
    ("bhattacherjee2022_prefrontal_spatial_transcriptomics.md", "Bhattacherjee", 2022, [
        ("MERFISH spatial transcriptomics reveals 52 distinct cell subtypes in mouse PFC organized in 3D anatomical space", "prefrontal_cortex"),
        ("PFC shows unique ion-channel gene expression signature with enrichment of voltage-gated potassium channels and AMPA receptor subunits", "prefrontal_cortex"),
        ("L5 ET1 neurons (marked by Pou3f1) projecting to PAG are preferentially deactivated in chronic neuropathic pain", "prefrontal_cortex"),
    ]),
]

pages_created = set()
pages_updated = set()
total_facts = 0

for filename, author, year, facts in facts_to_process:
    print(f"Processing {filename}...")
    total_facts += len(facts)
    
    for claim, topic in facts:
        # Determine page path
        if any(x in topic for x in ['cortex', 'hippocampus', 'striatum', 'amygdala', 'thalamus']):
            page_path = f"{base_path}/wiki/brain_regions/{topic}.md"
        elif any(x in topic for x in ['navigation', 'learning', 'memory', 'decision', 'replay', 'behaviour']):
            page_path = f"{base_path}/wiki/behaviours/{topic}.md"
        else:
            page_path = f"{base_path}/wiki/computational_frameworks/{topic}.md"
        
        page_title = topic.replace('_', ' ').title()
        
        if ensure_page(page_path, page_title):
            rel_path = page_path.replace(f"{base_path}/", "")
            pages_created.add(rel_path)
        else:
            rel_path = page_path.replace(f"{base_path}/", "")
            pages_updated.add(rel_path)
        
        write_fact(page_path, claim, filename, year, author)

print(f"\n=== PROCESSING COMPLETE ===")
print(f"Total facts: {total_facts}")
print(f"Pages created: {len(pages_created)}")
print(f"Pages updated: {len(pages_updated)}")
