import os
import re
from datetime import datetime

# Fact definitions for each summary
facts_data = {
    "basu2021_ofc_navigation_goals.md": [
        {"claim": "OFC neurons persistently encode the animal's future navigational destination throughout a journey, forming an internal goal map", "evidence": "80.8% of OFC neurons showed spatial tuning; 86.9% showed conjunctive coding of position and navigation phase; goal representation emerged ~1.1s before motion onset", "topics": ["orbitofrontal_cortex", "spatial_navigation", "goal_directed_behaviour"], "confidence": "high"},
        {"claim": "OFC goal coding is viewpoint-invariant and represents the animal's chosen (not correct) goal", "evidence": "LDA decoder successfully decoded goal well regardless of approach direction; in error trials, OFC decoded the incorrect destination as accurately as correct goal", "topics": ["orbitofrontal_cortex", "decision_making"], "confidence": "high"},
        {"claim": "OFC goal identity is encoded orthogonally to trajectory dynamics", "evidence": "LDA dimension analysis showed axis of maximal goal-well separability was nearly orthogonal to neural trajectory evolution direction", "topics": ["orbitofrontal_cortex", "neural_manifold"], "confidence": "high"},
        {"claim": "OFC activity at navigation onset is causally necessary for accurate goal selection", "evidence": "Optogenetic perturbation at motion onset increased navigational errors (P=0.020); pharmacogenetic silencing also increased error rates", "topics": ["orbitofrontal_cortex", "spatial_navigation"], "confidence": "high"}
    ],
    "basu2023_goal_pointer_cognitive_map_ofc.md": [
        {"claim": "OFC functions as a dedicated 'goal pointer' maintaining persistent representation of future navigational goals", "evidence": "Review of OFC neurons encoding goal location persistently from before motion onset until goal arrival, independent of intermediate locations", "topics": ["orbitofrontal_cortex", "hippocampus", "goal_directed_behaviour"], "confidence": "high"},
        {"claim": "Hippocampus-OFC implements two-system architecture: hippocampus encodes current position (SR/map), OFC encodes goal (reward vector)", "evidence": "Review proposes OFC provides persistent reward-state representation applied to hippocampal successor representation to compute goal-directed value gradients", "topics": ["orbitofrontal_cortex", "hippocampus", "successor_representation"], "confidence": "medium"},
        {"claim": "Ventral hippocampal inputs are necessary for OFC's representation of target direction during decision-making", "evidence": "Review cites evidence that hippocampus-to-OFC communication supports spatial map formation in OFC", "topics": ["orbitofrontal_cortex", "hippocampus", "decision_making"], "confidence": "medium"}
    ],
    "bein2024_schemas_reinforcement_learning_pfc.md": [
        {"claim": "RL mechanisms (prediction errors, hierarchical RL, dimensionality reduction) provide computational account of schema acquisition", "evidence": "Review synthesizes evidence that state prediction errors enhance memory for violating content; temporal abstraction in hierarchical RL maps onto schema hierarchy", "topics": ["medial_prefrontal_cortex", "schema_learning", "reinforcement_learning"], "confidence": "medium"},
        {"claim": "mPFC subserves both RL and schemas through dimensionality reduction and guided memory reactivation", "evidence": "fMRI shows mOFC/vmPFC encodes low-dimensional abstract task representations; mid-mPFC generalizes across schema instances", "topics": ["medial_prefrontal_cortex", "orbitofrontal_cortex", "schema_learning"], "confidence": "medium"},
        {"claim": "Gradient hypothesis: more abstract/future-oriented representations are found in anterior and dorsal mPFC", "evidence": "Review synthesizes findings showing anterior mPFC represents far future/counterfactual states while posterior mPFC represents specific schemas", "topics": ["medial_prefrontal_cortex"], "confidence": "medium"}
    ],
    "bendor2012_biasing_hippocampal_replay_sleep.md": [
        {"claim": "Auditory cues associated with specific spatial locations bias hippocampal replay during non-REM sleep", "evidence": "Place cells showed location-specific firing rate bias after associated sounds; Bayesian decoding confirmed ensemble-level bias", "topics": ["hippocampus", "memory_consolidation", "hippocampal_replay"], "confidence": "high"},
        {"claim": "Replay bias is specific to non-REM sleep and absent during awake reactivation", "evidence": "Bias was absent during awake reactivation (ANOVA, P = 0.82); consistent with human TMR studies", "topics": ["hippocampus", "memory_consolidation"], "confidence": "high"},
        {"claim": "Cue-biased replay represents selective content modulation rather than non-specific arousal", "evidence": "Acoustic cues did not change the number of replay events (Kruskal-Wallis, P > 0.05)", "topics": ["hippocampus", "memory_consolidation"], "confidence": "high"}
    ]
}

print(f"Defined facts for {len(facts_data)} summaries")
