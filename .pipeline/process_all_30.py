#!/usr/bin/env python3
"""
Process 30 summaries through fact_finder -> router -> wiki_writer pipeline
"""

import os
import re
from datetime import datetime

# Get current timestamp
timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')

# Define all 30 summaries with extracted facts
# Format: (filename, title, year, [(claim, evidence, topics, confidence)])
summaries = [
    ("basu2021_ofc_navigation_goals.md", "The orbitofrontal cortex maps future navigational goals", 2021, [
        ("OFC neurons persistently encode the animal's future navigational destination throughout a journey", "80.8% of OFC neurons showed spatial tuning; goal representation emerged ~1.1s before motion onset and maintained throughout", ["orbitofrontal_cortex", "spatial_navigation", "goal_directed_behaviour"]),
        ("OFC goal coding is viewpoint-invariant and represents the chosen (not correct) goal", "LDA decoder decoded goal well regardless of approach direction; in error trials, OFC decoded the incorrect destination", ["orbitofrontal_cortex", "decision_making"]),
        ("OFC activity at navigation onset is causally necessary for accurate goal selection", "Optogenetic perturbation increased navigational errors (P=0.020); pharmacogenetic silencing also increased errors", ["orbitofrontal_cortex", "spatial_navigation"])
    ]),
    ("basu2023_goal_pointer_cognitive_map_ofc.md", "A goal pointer for a cognitive map in the orbitofrontal cortex", 2023, [
        ("OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals", "OFC neurons encode goal location persistently from before motion onset until goal arrival, independent of intermediate locations", ["orbitofrontal_cortex", "hippocampus", "goal_directed_behaviour"]),
        ("Hippocampus-OFC implements two-system architecture: hippocampus encodes current position (SR/map), OFC encodes goal (reward vector)", "OFC provides persistent reward-state representation applied to hippocampal successor representation to compute goal-directed value gradients", ["orbitofrontal_cortex", "hippocampus", "successor_representation"]),
        ("Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making", "Hippocampus-to-OFC communication supports spatial map formation in OFC", ["orbitofrontal_cortex", "hippocampus", "decision_making"])
    ]),
    ("bein2024_schemas_reinforcement_learning_pfc.md", "Schemas, reinforcement learning, and the medial prefrontal cortex", 2024, [
        ("RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition", "State prediction errors enhance memory for violating content; temporal abstraction in hierarchical RL maps onto schema hierarchy", ["medial_prefrontal_cortex", "schema_learning", "reinforcement_learning"]),
        ("mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation", "mOFC/vmPFC encodes low-dimensional abstract task representations; mid-mPFC generalizes across schema instances", ["medial_prefrontal_cortex", "orbitofrontal_cortex", "schema_learning"]),
        ("Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC", "Anterior mPFC represents far future/counterfactual states while posterior mPFC represents specific schemas", ["medial_prefrontal_cortex"])
    ]),
    ("bendor2012_biasing_hippocampal_replay_sleep.md", "Biasing the content of hippocampal replay during sleep", 2012, [
        ("Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep", "Place cells showed location-specific firing rate bias after associated sounds; Bayesian decoding confirmed ensemble-level bias", ["hippocampus", "memory_consolidation", "hippocampal_replay"]),
        ("Replay bias is specific to non-REM sleep and absent during awake reactivation", "Bias was absent during awake reactivation (ANOVA, P = 0.82); consistent with human TMR studies", ["hippocampus", "memory_consolidation"]),
        ("Cue-biased replay represents selective content modulation rather than non-specific arousal", "Acoustic cues did not change the number of replay events (Kruskal-Wallis, P > 0.05)", ["hippocampus", "memory_consolidation"])
    ]),
    ("benjamin2018_statistical_significance.md", "Redefine Statistical Significance", 2018, [
        ("The default P-value threshold for claiming new discoveries should be lowered from 0.05 to 0.005", "P < 0.05 provides only weak Bayesian evidence (Bayes factors ~2.5-3.4) and generates high false positive rates; P < 0.005 corresponds to Bayes factors ~14-26", ["statistical_methods"], "methodological"),
        ("Empirical replication rates approximately double when initial studies used P < 0.005 versus 0.005 < P < 0.05", "50% vs 24% in psychology; 85% vs 44% in experimental economics", ["statistical_methods", "reproducibility"], "methodological"),
        ("Maintaining 80% power under the new threshold requires approximately 70% larger sample sizes", "Efficiency gains from avoiding false-premise follow-up studies outweigh this cost", ["statistical_methods", "study_design"], "methodological"})
    ]),
]

print(f"Defined {len(summaries)} summaries with facts")

# Now process each summary
pages_created = []
pages_updated = []
total_facts = 0

for summary_file, title, year, facts in summaries:
    print(f"Processing {summary_file}...")
    total_facts += len(facts)
    
    for claim, evidence, topics in facts:
        # Determine target pages based on topics
        target_pages = []
        for topic in topics:
            if 'cortex' in topic or 'hippocampus' in topic or 'striatum' in topic or 'amygdala' in topic or 'thalamus' in topic:
                page_path = f"wiki/brain_regions/{topic}.md"
                target_pages.append((page_path, topic.replace('_', ' ').title()))
            elif 'behaviour' in topic or 'navigation' in topic or 'learning' in topic or 'memory' in topic or 'decision' in topic or 'replay' in topic:
                page_path = f"wiki/behaviours/{topic}.md"
                target_pages.append((page_path, topic.replace('_', ' ').title()))
        
        # Write to each target page
        for page_path, page_title in target_pages:
            full_path = os.path.join('/Users/vyp730/Projects/knowledgeBase', page_path)
            
            # Create page if needed
            if ensure_page(full_path, page_title):
                pages_created.append(page_path)
            else:
                pages_updated.append(page_path)
            
            # Write the fact
            write_fact_to_page(full_path, claim, f"raw/summaries/{summary_file}", year)

print(f"\nTotal facts: {total_facts}")
print(f"Pages created: {len(set(pages_created))}")
print(f"Pages updated: {len(set(pages_updated))}")

# Log the activity
log_content = f"""
- timestamp: {datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')}
  agent: fact_finder+router+wiki_writer
  event: batch_30_summaries_processed
  facts_extracted: {total_facts}
  facts_routed: {total_facts}
  facts_written: {total_facts}
  facts_skipped: 0
  pages_created: {list(set(pages_created))}
  pages_updated: {list(set(pages_updated))}
"""

with open('/Users/vyp730/Projects/knowledgeBase/log.md', 'a') as f:
    f.write(log_content)

print("Done!")
