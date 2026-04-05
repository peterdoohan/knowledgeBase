---
source_file: zeithamova2012_hippocampal_inference.md
title: "The hippocampus and inferential reasoning: building memories to navigate future decisions"
authors: Dagmar Zeithamova, Margaret L. Schlichting, Alison R. Preston
year: 2012
journal: Frontiers in Human Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

The hippocampus supports inferential reasoning through flexible memory representations that enable both retrieval-based recombination of discrete memories and integrative encoding that links overlapping experiences during learning.

### Background & motivation

Inferential reasoning—the ability to form relationships between items or events not experienced together—is fundamental to everyday decision-making. While traditionally viewed as a retrieval-based logical process, emerging evidence suggests the hippocampus contributes through multiple mechanisms, including specialized encoding processes that construct memory networks anticipating future use.

### Methods

This review synthesizes evidence from:
- Animal lesion studies (rodents: hippocampal lesions, fornix transection, entorhinal/perirhinal disconnection; non-human primates: hippocampal system lesions)
- Human neuropsychological studies (patients with hippocampal atrophy, Parkinson's disease patients with basal ganglia damage)
- Human fMRI studies of transitive inference, acquired equivalence, and associative inference tasks
- Computational modeling of CA3 function and pattern completion/separation mechanisms
- Single-unit electrophysiology in rodents (hippocampal replay, place cell activity)

### Key findings

- Hippocampal lesions impair inferential judgments while sparing acquisition of trained premise associations (Bunsey and Eichenbaum, 1996; Dusek and Eichenbaum, 1997; DeVito et al., 2010a)
- Post-training hippocampal lesions eliminate representations of relationships among items while leaving reinforcement history information intact (DeVito et al., 2010a)
- Hippocampal lesions performed prior to learning produce greater deficits than post-training lesions, highlighting the critical role of hippocampus during encoding (van der Jeugd et al., 2009)
- Anterior hippocampus shows selective activation during inferential (AC) vs. trained (AB, BC) probes in associative inference tasks (Preston et al., 2004)
- Left hippocampus shows greater activation for inferential vs. non-inferential probes in transitive inference; right hippocampal activation tracks distance between items in hierarchy (Zalesak and Heckers, 2009)
- Hippocampal encoding activation during overlapping associations (BC) predicts trial-by-trial inference success (Zeithamova and Preston, 2010)
- Hippocampal activation increases across training correlate with individual differences in inference performance in acquired equivalence tasks (Shohamy and Wagner, 2008)
- Sleep enhances transitive inference performance, particularly for items with greater separation in hierarchy (Ellenbogen et al., 2007)
- Prefrontal cortex (medial, dorsolateral, inferior frontal gyrus) shows coupled activation with hippocampus during inference and differentiates correct from incorrect performance

### Computational framework

The review discusses several computational perspectives on hippocampal function:

**Pattern completion and relational binding**: The hippocampus codes event elements discretely in terms of their relationships to one another (Cohen and Eichenbaum, 1993; O'Reilly and Rudy, 2001). This enables pattern completion—retrieval of complete memories from partial cues—which supports recombination of retrieved associations during inference.

**CA3 context fields**: Computational models suggest CA3 neurons develop "context fields" that bind elements within single events; through recurrent connections, these can integrate experiences sharing common features beyond temporal context (Wallenstein et al., 1998).

**Pattern separation vs. integration**: Alternative accounts propose:
- Single integrated representations: overlapping events encoded into composite traces (loss of individual event details)
- Pattern-separated representations: distinct representations for each event, linked through common elements (preserves event details)
- Relational networks: separate event representations with direct lateral connections between overlapping events

### Prevailing model of the system under study

Prior to this review, the field largely viewed inferential reasoning as a retrieval-based logical process where existing memories are accessed and recombined to answer novel questions. The hippocampus was understood to support this through flexible, elemental representations that allow discrete access to event details. However, the specific mechanisms—particularly the role of hippocampal encoding processes and the representational format of integrated memories—remained unresolved.

### What this paper contributes

This review advances the understanding of hippocampal function in inferential reasoning by:

1. **Integrating dual mechanisms**: Synthesizes evidence for both retrieval-based recombination AND integrative encoding as hippocampal mechanisms supporting inference. Previously, these were often discussed separately.

2. **Emphasizing encoding contributions**: Highlights that hippocampal processes during initial learning—not just retrieval—are critical for inference, with encoding activation patterns predicting subsequent inference success.

3. **Connecting to schema theory**: Links integrative encoding processes to emerging literature on hippocampal contributions to schema formation, suggesting shared neural mechanisms for binding across experiences.

4. **Proposing prospective function**: Advances the view that hippocampal function is "intrinsically prospective"—memories are constructed to anticipate future decisions, not merely to record past events.

5. **Evaluating representational accounts**: Critically evaluates competing computational accounts of hippocampal representations (integrated vs. pattern-separated vs. relational networks) and their implications for inference.

### Brain regions & systems

- **Hippocampus (anterior/posterior)**: Anterior hippocampus shows selective activation during inferential judgments; posterior hippocampus engaged for all associative retrieval; left hippocampus for inferential vs. non-inferential discriminations; right hippocampal activation tracks relational distance in hierarchies
- **Prefrontal cortex (dorsolateral, medial, inferior frontal gyrus)**: Coupled with hippocampus during inference; involved in relational reasoning, manipulation/recombination of memory contents; differentiates correct from incorrect inference performance
- **Ventromedial prefrontal cortex (VMPFC)**: Interacts with hippocampus during schema application; associated with speeded transfer to novel tasks with similar structure
- **Entorhinal cortex / Perirhinal cortex**: Cortical connections with hippocampus; lesion studies demonstrate necessity for transitive inference performance
- **Basal ganglia**: Supports reinforcement learning of stimulus-response associations; double dissociation with hippocampal contributions in acquired equivalence (Parkinson's patients show slow acquisition but intact inference; hippocampal patients show intact acquisition but impaired inference)
- **CA3 region**: Proposed locus of context field formation and binding processes supporting memory integration

### Mechanistic insight

This review does not present new mechanistic data but synthesizes existing evidence relevant to Marr's levels:

**Computational level**: The brain solves the problem of inferring unobserved relationships between items experienced at different times. This enables flexible decision-making without requiring direct experience of all possible item combinations.

**Algorithmic level**: Two complementary mechanisms are proposed:
1. **Retrieval-based inference**: Elemental representations allow pattern completion from partial cues; retrieved associations are recombined to support novel judgments
2. **Integrative encoding**: Overlapping elements trigger reactivation of prior memories; new events are encoded in context of reactivated information, forming direct links between experiences

**Implementational level**: 
- CA3 region proposed as neural substrate for context field formation and binding
- Recurrent connections in CA3 may support both pattern completion and integration across experiences
- Hippocampal-neocortical interactions (particularly with prefrontal cortex) support retrieval and manipulation of relational information
- Sleep-based replay provides offline mechanism for memory integration and network formation

**Assessment**: The review does not provide direct neural data linking specific algorithmic variables to measured neural activity. The proposed mechanisms are derived from computational models and fMRI studies showing correlated activation patterns. The causal evidence comes from lesion studies, which demonstrate necessity but not the specific algorithmic implementation.

### Limitations & open questions

- **Cross-species inconsistencies**: Hippocampal contributions to acquired equivalence differ between rodents (intact performance with hippocampal lesions, impaired with entorhinal lesions) and humans (impaired with hippocampal damage)
- **Training effects**: The number of training trials and learning procedures may influence whether integrative encoding or retrieval-based mechanisms dominate
- **Sleep and consolidation**: Whether sleep enhances inference specifically through memory integration or simply consolidates individual premise associations remains unresolved
- **Representational format**: Whether hippocampal representations supporting inference are integrated (composite), pattern-separated (linked through common elements), or relational (direct lateral connections between events) remains empirically undetermined
- **Loss of episodic details**: Whether integrated representations lose idiosyncratic event details (as in schemas) and under what circumstances is not fully understood
- **Prefrontal-hippocampal interactions**: The respective roles of hippocampus (retrieval/storage) vs. prefrontal cortex (manipulation/reasoning) in inference remain to be precisely determined
- **Causal evidence from fMRI**: Neuroimaging correlations do not establish necessity; more lesion/intervention studies needed to complement fMRI findings

### Connections & keywords

**Key citations:**
- Eichenbaum and Cohen (2001); Squire et al. (2004); Eichenbaum et al. (2007); Preston and Wagner (2007) — foundational hippocampal memory theory
- Cohen and Eichenbaum (1993); O'Reilly and Rudy (2001) — relational memory theory and conjunctive representations
- Bunsey and Eichenbaum (1996); Dusek and Eichenbaum (1997) — animal lesion studies of associative and transitive inference
- Heckers et al. (2004); Preston et al. (2004); Zalesak and Heckers (2009) — human fMRI studies of hippocampal activation during inference
- Shohamy and Wagner (2008); Zeithamova and Preston (2010) — integrative encoding processes
- McClelland et al. (1995); Wallenstein et al. (1998) — computational models of hippocampal function
- Tse et al. (2007, 2011) — schema-dependent learning in rodents
- Tolman (1948); O'Keefe and Nadel (1978) — cognitive map theory
- Marr (1971) — pattern completion theory

**Named models or frameworks:**
- Relational memory theory (Cohen and Eichenbaum)
- Cognitive map theory (Tolman; O'Keefe and Nadel)
- Pattern completion / Pattern separation (Marr; McClelland et al.)
- Complementary learning systems (McClelland et al., 1995)
- CA3 context field models (Wallenstein et al., 1998)
- Schema theory (Tse et al.; Bartlett)
- Prospective consolidation / Constructive episodic simulation (Buckner; Addis and Schacter)
- Integrative encoding (Shohamy and Wagner; Zeithamova and Preston)

**Brain regions:**
- Hippocampus (anterior, posterior, CA3, dentate gyrus)
- Entorhinal cortex
- Perirhinal cortex
- Fornix
- Prefrontal cortex (dorsolateral, medial, inferior frontal gyrus, ventromedial)
- Basal ganglia
- Medial temporal lobe (MTL)

**Keywords:**
hippocampus, inferential reasoning, transitive inference, associative inference, acquired equivalence, memory integration, pattern completion, relational memory, schema, sleep consolidation, prospective memory, CA3, elemental encoding, medial temporal lobe
