---
source_file: alonso2021_hexmaze_cognitive_map.md
paper_id: alonso2021_hexmaze_cognitive_map
title: "The HexMaze: A Previous Knowledge Task on Map Learning for Mice"
authors:
  - "Alejandra Alonso"
  - "Levan Bokeria"
  - "Jacqueline van der Meij"
  - "Anumita Samanta"
  - "Ronny Eichler"
  - "Ali Lotfi"
  - "Patrick Spooner"
  - "Irene Navarro Lobato"
  - "Lisa Genzel"
year: 2021
journal: eNeuro
paper_type: empirical
contribution_type: empirical
species:
  - mouse
tasks:
  - hexmaze
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
frameworks:
  - reinforcement_learning
  - hierarchical_rl
keywords:
  - spatial_navigation
  - cognitive_map
  - schema
  - memory_consolidation
  - previous_knowledge
  - learning_set
  - mouse_behavior
  - allocentric_navigation
  - spatial_memory
  - systems_consolidation
  - offline_learning
  - map_updating
  - hippocampus
  - medial_prefrontal_cortex
  - maze_learning
  - hexmaze
  - previous
  - knowledge
  - task
  - map
---

### One-line summary

Mice learning a complex spatial environment (the HexMaze) show three distinct phases of cognitive map formation: initial goal learning, faster learning after 2 weeks, and one-session learning with rapid consolidation after 12 weeks, with map buildup dependent on time elapsed rather than training frequency.

### Background & motivation

Most rodent behavioral tasks test naive animals on simple spatial problems, unlike human research where participants bring rich prior knowledge. The study addresses how mice build and use cognitive maps of complex environments over extended periods, and how prior knowledge accelerates new learning—mirroring schema effects observed in associative learning tasks (Tse et al., 2007). Understanding the dynamics of spatial map formation could inform models of memory consolidation and the hippocampal-cortical dialogue.

### Methods

- **Subjects**: 16 male C57BL/6J mice across 4 cohorts (2 groups: 8 trained 3 days/week, 8 trained 2 days/week); pilot cohort excluded
- **Apparatus**: HexMaze—large hexagonal gangway maze (2 × 1.9 m) with 30 gangways, 24 triangular intersections, local and global visual cues; 36.3 cm center-to-center between nodes
- **Training paradigm**: 
  - Build-Up phase (12 weeks): mice learned 5 sequential goal locations (GL1–5), each held constant for 5–7 sessions
  - Updates phase (9 weeks): goal location or barriers changed every 3 sessions; three update types: barrier only (Bar), location only (Loc), both (L+B)
- **Measurements**: log-normalized path length (actual path/shortest path), first-trial performance (long-term memory), probe trials (no food for 60s), video tracking with custom Python/OpenCV software
- **Analysis**: repeated-measures ANOVA with Greenhouse-Geisser correction when sphericity violated

### Key findings

- **Three phases of map learning**: (1) GL1 required 7+ sessions to reach good performance; (2) by GL2 (week 3), performance improved significantly in session 2, showing offline gains; (3) by Updates (week 12+), animals showed good performance in session 1 with additional offline gains in session 2
- **Time-dependent, not training-dependent**: comparing 2 vs 3 days/week training, performance aligned by weeks since start, not by training days; cognitive map buildup requires time (offline remodeling), not just experience
- **Learning set effects**: three-step progression—naive (no offline gains), offline gains (intermediate), online and offline gains (expert); suggests rule learning plus spatial map knowledge
- **Rapid updating**: during Updates, barrier-only changes showed immediate adaptation (schema-like), while location changes required within-session learning; one session sufficient for consolidation by second session
- **Memory persistence**: one session produced 2-day memory but not 5-day memory; two sessions produced 5-day memory, indicating threshold for long-term stability
- **Goal location retention**: probe trials showed animals crossed both current and previous goal locations more than control nodes, indicating old memories not overwritten

### Computational framework

Not applicable. This is a purely empirical behavioral study. However, the results constrain models of spatial memory and cognitive map formation. The findings suggest that cognitive maps are not simply accumulated associations but undergo qualitative reorganization over time (consistent with systems consolidation models). The time-dependent nature of map formation suggests computational models should incorporate offline processes (sleep-dependent replay/reactivation) rather than treating learning as purely online, experience-driven association formation. The three-phase learning progression could inform hierarchical reinforcement learning models where policy learning accelerates as state representations become more structured.

### Prevailing model of the system under study

The prevailing model, based on rodent spatial navigation research (Morris et al., 1982; O'Keefe & Nadel, 1978), holds that: (1) rodents rapidly learn spatial environments through hippocampal-dependent place learning; (2) with repeated exposure, spatial memories consolidate to neocortical structures; (3) prior knowledge (schemas) accelerates new learning and enables rapid consolidation. The specific mechanism of cognitive map formation over extended periods was less clear—specifically whether map quality depends on experience amount or time elapsed. The introduction positions this work within the schema literature (Tse et al., 2007) and learning set literature (Harlow, 1949), suggesting that the field was exploring how prior knowledge structures facilitate memory but had not yet characterized the time course of spatial map formation in complex environments.

### What this paper contributes

- **Established a new behavioral paradigm**: The HexMaze enables separate measurement of online learning, offline consolidation, and map updating while holding task difficulty constant across phases
- **Demonstrated time-dependent map formation**: Cognitive map quality depends on weeks elapsed, not training frequency—suggesting offline biological processes (synaptic consolidation, systems consolidation) are rate-limiting
- **Characterized three-phase learning progression**: From naive (slow learning, no offline gains), to intermediate (offline gains but no one-session learning), to expert (online and offline gains, rapid consolidation)
- **Showed learning set effects in spatial domain**: The three-phase progression mirrors Harlow's learning sets but in a complex spatial environment, suggesting rule abstraction plus map knowledge
- **Demonstrated schema-like rapid updating**: Barrier updates showed immediate adaptation (schema-like), while location updates required learning but consolidated rapidly
- **Quantified memory persistence thresholds**: One session → 2-day memory; two sessions → 5-day memory—providing behavioral benchmarks for consolidation studies
- **Provided large open dataset**: >30,000 trials from 16 mice over ~10 months enables secondary analysis and computational modeling

### Brain regions & systems

- **Hippocampus**: Central to spatial map formation and initial encoding; authors hypothesize hippocampal involvement in early phases of learning, with potential shift to hippocampal independence in later phases (schema-like updating)
- **Medial prefrontal cortex (mPFC)**: Implicated in schema effects based on prior literature (Tse et al., 2011; Wang et al., 2012); authors speculate mPFC may be involved in later learning phases when schema-like rapid updating occurs
- **Entorhinal cortex**: Grid cells provide spatial coordinate system for cognitive map (referenced in discussion regarding neural basis of cognitive maps)
- **Neocortical networks**: Discussion suggests systems consolidation involves transfer of spatial knowledge from hippocampus to neocortical structures over the 12-week training period

Note: No direct neural recordings or manipulations in this study; brain regions discussed as context and hypotheses for future work based on behavioral findings and literature review.

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight as defined in the instructions. While the paper proposes that cognitive map formation involves time-dependent processes (likely offline consolidation), it does not present a formal algorithmic model or provide neural data that specifically supports that algorithm over alternatives. The behavioral findings constrain possible mechanisms but do not identify the specific algorithmic or implementational mechanisms.

The paper does not:
- Present a formal computational model of map learning
- Provide neural recordings that identify specific representations or algorithms
- Manipulate neural circuits to test algorithmic hypotheses

What the paper does provide is rich behavioral data that constrains future mechanistic work—specifically, the finding that map formation is time-dependent (not experience-dependent) suggests that future models must incorporate offline processes (sleep, consolidation) rather than purely online learning.

### Limitations & open questions

- **No neural data**: The study is purely behavioral; neural correlates of the three learning phases remain unknown
- **Only male mice**: Gender differences in spatial map formation not addressed
- **No direct schema manipulation**: The study discusses schema-like effects but does not manipulate neural circuits (e.g., hippocampal inactivation) to confirm schema-like neural mechanisms
- **No sleep recording**: The time-dependent nature of map formation suggests offline consolidation, but sleep/wake states were not monitored
- **Mice vs rats**: Mice show more random movement strategies than rats; generalizability to other species unclear
- **Causality of time vs. experience**: While the 2 vs 3 day/week comparison suggests time dependency, other explanations (e.g., different spacing effects) cannot be fully ruled out
- **Neural mechanism of rapid consolidation**: One-session learning leading to 5-day memory in expert mice suggests rapid systems consolidation, but neural basis untested

### Connections & keywords

**Key citations**:
- Tse et al. (2007) — foundational schema study in rodents
- Harlow (1949) — learning set theory
- Bartlett (1932) — schema concept origins
- O'Keefe & Nadel (1978) — cognitive map theory
- Morris et al. (1982) — watermaze task, reference memory
- Ghosh & Gilboa (2014) — schema features framework

**Named models or frameworks**:
- Cognitive map (O'Keefe & Nadel, 1978)
- Schema theory (Bartlett, 1932; Tse et al., 2007)
- Learning set (Harlow, 1949)
- Systems consolidation theory
- Reference memory vs. working memory framework

**Brain regions**:
- Hippocampus
- Medial prefrontal cortex (mPFC)
- Entorhinal cortex
- Neocortical networks

**Keywords**: spatial navigation, cognitive map, schema, memory consolidation, previous knowledge, learning set, mouse behavior, allocentric navigation, spatial memory, systems consolidation, offline learning, map updating, hippocampus, medial prefrontal cortex, maze learning
