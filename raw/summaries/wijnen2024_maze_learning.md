---
source_file: "wijnen2024_maze_learning.md"
paper_id: "wijnen2024_maze_learning"
title: "Rodent maze studies: from following simple rules to complex map learning"
authors: "Kjell Wijnen, Lisa Genzel, Jacqueline van der Meij"
year: 2024
journal: "Brain Structure and Function"
paper_type: "review"
contribution_type: "review"
species: ["mouse", "rat"]
tasks: ["hexmaze", "navigation_task"]
brain_regions: ["hippocampus", "prefrontal_cortex", "striatum"]
keywords: ["rodent", "maze", "studies", "following", "simple", "rules", "complex", "map", "learning"]
key_citations: ["alonso2021_hexmaze_cognitive_map", "redish2016_vicarious_trial_error_b"]
---

### One-line summary

A comprehensive review of over 100 years of rodent maze research, mapping how different maze designs and training paradigms engage distinct navigational strategies (egocentric vs. allocentric) and memory systems (habit vs. explicit memory).

### Background & motivation

Maze studies have been central to understanding spatial learning and memory for over a century, yet there is no consensus on which maze or training paradigm is optimal for studying specific cognitive processes. The choice of maze critically determines what animals learn—ranging from simple stimulus-response habits to complex cognitive maps—but these relationships are often underappreciated. This review provides a historical framework to guide researchers in selecting appropriate maze tasks based on their specific research questions.

### Methods

- **Literature scope**: Historical review covering rodent maze studies from 1901 (Small's Hampton Court maze) to 2024
- **Inclusion criteria**: Studies using mazes to examine navigational learning and memory in rodents (primarily rats and mice)
- **Classification approach**: Mazes categorized by:
  - Navigational strategy required (egocentric vs. allocentric)
  - Complexity level (simple binary choice vs. complex map-based)
  - Start/goal location flexibility (fixed vs. variable)
  - Memory type engaged (reference memory, working memory, short-term memory)
- **Synthesis method**: Narrative synthesis organized chronologically and by maze type, with expert commentary on training effects and cognitive engagement

### Key findings

- **Historical trajectory**: Early mazes (1900s-1940s) were large with fixed start/goal locations, primarily testing egocentric path learning; mid-century innovations introduced specialized mazes (radial arm, watermaze, Barnes) capable of testing allocentric strategies; recent designs (2000s+) emphasize configurability, naturalistic features, and large-scale environments.

- **Maze design determines cognitive engagement**:
  - **Simple mazes** (T-, Y-, W-maze): Best for rule learning (win-stay, win-shift) and short-term memory; quickly become automated habits involving striatum rather than hippocampus
  - **Path-learning mazes** (Hampton Court, repeated T-maze): Test sequence learning and kinaesthetic memory; can engage hippocampus due to sequence component but become egocentric with overtraining
  - **Reference memory mazes** (watermaze, Barnes maze, radial arm maze): Test allocentric navigation with fixed goal and variable starts; engage hippocampus longer but reversal learning reveals habit formation
  - **Every-day memory mazes** (DMP watermaze, cheeseboard, event arena): Test rapid learning of new daily locations; initially hippocampal but can become stereotyped with overtraining
  - **Large-scale configurable mazes** (HexMaze, honeycomb maze, Tartarus maze): Permit testing of cognitive maps, schema formation, and flexible path planning with completely variable start/goal locations

- **Training effects are critical**: The same maze can engage different cognitive strategies depending on training duration and protocol:
  - **Early learning**: Engages explicit memory systems (hippocampus, cortex), characterized by vicarious trial-and-error (VTE) behavior at choice points
  - **Late learning/overtraining**: Shifts to automatic habits (striatum), with stereotyped paths and absent deliberation; difficult to reverse
  - **Shaping strategies**: Varying start/goal locations, limiting trials per day, and creating pause-thinking moments can maintain explicit system engagement longer

- **Species differences**: Mice generally require more habituation and shaping time than rats; mice prefer tighter, more enclosed environments and darker safe choice points to exhibit deliberation behavior; rats are more confident in open spaces.

### Computational framework

Not applicable. This is a narrative review without formal computational modeling. However, the paper discusses navigation within established conceptual frameworks:

- **Dual-strategy framework**: The distinction between egocentric (self-centered, body-turn-based) and allocentric (world-centered, map-based) navigation strategies, with mazes varying in which strategy they optimally engage.

- **Multiple memory systems**: The paper implicitly follows the framework of multiple parallel memory systems (habit/memory; striatum/hippocampus) and how training drives consolidation from cognitive to automatic control.

- **Schema theory**: Discussion of how extensive training in complex environments permits schema formation (structured knowledge that supports rapid new learning), referencing Tse et al. (2007).

### Prevailing model of the system under study

The prevailing model in the field, as presented in this review, holds that:

1. **Maze navigation engages multiple strategies**: Rodents can solve maze tasks using either egocentric strategies (body-turn sequences, stimulus-response habits) or allocentric strategies (cognitive maps based on environmental cues), with the strategy depending on maze design and training.

2. **Simple mazes → habits; complex mazes → cognitive maps**: The field has historically assumed that simple binary mazes (T-, Y-maze) primarily test rule learning and short-term memory, while complex mazes with multiple start/goal locations (watermaze, radial arm maze) test allocentric reference memory.

3. **Overtraining drives automaticity**: It is well-established that extended training on the same task leads to a shift from hippocampal-dependent explicit memory to striatal-dependent habit memory, with stereotyped behavior and reduced cognitive flexibility.

4. **Species-specific training needs**: There is awareness that mice and rats differ in their behavioral tendencies—mice being more anxious, requiring more habituation, and preferring enclosed spaces—though optimal training protocols remain empirically determined.

### What this paper contributes

This review makes several important contributions to understanding rodent maze research:

1. **Integrated historical and conceptual framework**: The paper provides the first comprehensive synthesis mapping the historical development of maze designs onto the cognitive strategies they engage, allowing researchers to make informed choices about which maze to use for specific research questions.

2. **Training paradigm as critical variable**: The review emphasizes that training duration and protocol are as important as maze design in determining what animals learn. It demonstrates that the same maze can engage different neural systems (hippocampus vs. striatum) depending on training length, with practical guidance for maintaining explicit memory engagement.

3. **Classification of maze types by cognitive demand**: The paper establishes a useful taxonomy of mazes based on what animals actually learn: simple rules/body turns, path/multi-body turns, reference memory with fixed goals, every-day memory with daily-changing goals, and large-scale cognitive maps.

4. **Identification of overtraining risks**: The review highlights that overtraining not only produces habits but can also interfere with subsequent cognitive testing (e.g., reversal learning deficits), and provides specific recommendations for shaping behavior to prevent premature automatization.

5. **Methodological recommendations**: The paper offers concrete guidance on species-specific shaping (mice vs. rats), cue configuration, trial timing, and environmental design to optimize engagement of target cognitive processes.

### Brain regions & systems

- **Hippocampus** — Explicit/declarative memory system engaged during early learning and allocentric navigation; involved in spatial memory formation, cognitive map construction, and episodic-like memory; place cells encode spatial locations; associated with vicarious trial-and-error (VTE) behavior at choice points

- **Striatum** — Habit/memory system engaged during late learning/overtraining; mediates stimulus-response learning and automatic behaviors; involved when animals develop stereotyped paths and egocentric strategies through extended training

- **Prefrontal cortex** — Involved in deliberation and planning; associated with VTE behavior and flexible decision-making at choice points

- **Cortex (general)** — Part of the explicit memory system; involved in long-term memory storage and schema formation with extended training

- **Locus coeruleus** — Mentioned in context of memory consolidation; noradrenergic modulation of spatial memory

- **Dopaminergic system** — Referenced in relation to reward processing and memory consolidation in spatial tasks

### Mechanistic insight

This review does not present new mechanistic data linking specific algorithms to neural implementations. It is a conceptual synthesis paper that organizes existing literature rather than providing novel experimental findings. Therefore, it does not meet the bar for mechanistic insight.

### Limitations & open questions

- **Limited species scope**: While the paper briefly mentions maze use in other species (Box 1), the primary focus is on rodents, limiting generalization to other model organisms.

- **No quantitative meta-analysis**: The review relies on narrative synthesis rather than systematic meta-analysis, limiting the ability to quantify effect sizes or resolve contradictory findings.

- **Unexplored individual differences**: The paper notes that animals within the same species and strain show variable strategy preferences but does not systematically address the sources of this variability.

- **Neural mechanism depth**: While brain regions are associated with different strategies, the cellular and circuit mechanisms driving strategy shifts remain to be fully elucidated.

- **Translation to human cognition**: The implications of rodent maze findings for human spatial cognition and clinical conditions are not extensively discussed.

### Connections & keywords

**Key citations**: O'Keefe (1979, 1993) - hippocampal place cells; Morris (1981, 1984) - watermaze; Olton and Samuelson (1976) - radial arm maze; Tolman et al. (1946) - Sunburst maze/path integration; Tse et al. (2007) - schema theory; Eichenbaum et al. (1999) - hippocampal memory systems; Barnes (1979) - Barnes maze; Genzel et al. (2017, 2019) - memory consolidation; Alonso et al. (2021) - HexMaze; Redish (2016) - vicarious trial-and-error

**Named models or frameworks**: Egocentric navigation; Allocentric navigation; Win-stay paradigm; Win-shift paradigm; Spontaneous Alternation Behaviour (SAB); Cognitive map; Schema theory; Vicarious trial-and-error (VTE); Path integration; Rule learning; Reference memory; Working memory; Every-day memory; Habit learning

**Brain regions**: Hippocampus; Striatum; Prefrontal cortex; Cortex; Locus coeruleus; Dopaminergic system

**Keywords**: Spatial navigation; Maze learning; Rodent behavior; Egocentric strategy; Allocentric strategy; Hippocampus; Striatum; Cognitive map; Spatial memory; Reference memory; Working memory; Habit formation; Vicarious trial-and-error; Overtraining; Schema
