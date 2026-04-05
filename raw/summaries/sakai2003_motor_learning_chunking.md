---
source_file: sakai2003_motor_learning_chunking.md
title: Chunking during human visuomotor sequence learning
authors: Katsuyuki Sakai, Katsuya Kitaguchi, Okihide Hikosaka
year: 2003
journal: Experimental Brain Research
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Human subjects spontaneously chunk visuomotor sequences into hierarchical memory units during learning, with these chunks being subject-specific, functionally necessary for efficient performance, and asymmetrically transferable from the nondominant to dominant hand.

### Background & motivation

Motor sequence learning involves recoding elementary movements into efficient representations, but whether chunking reflects genuine memory organization or merely external sequence structure remained unclear. Previous studies found chunk patterns that corresponded to physical parameters (repetition, inversion, transposition, or temporal delays), raising the question of whether chunks are epiphenomenal or representational. This study investigates whether chunk patterns emerge spontaneously, are independent of physical parameters, and have functional significance for sequence performance.

### Methods

- **Task**: "2×10 task" — explicit visuomotor sequence learning through trial and error. Subjects pressed 10 consecutive sets of two LED buttons (hyperset) in a predetermined correct order learned through feedback
- **Subjects**: 26 subjects (Experiment 1), 6 subjects (Experiment 2), 8 subjects (Experiment 3); mostly right-handed
- **Design**: 
  - Experiment 1: 1 session (20 trials) or 4 sessions learning with dominant hand; 8 subjects performed identical hypersets to assess intersubject differences
  - Experiment 2: 3 sessions learning, then session 4 with shuffled hyperset — "between" condition (preserved chunks) vs "within" condition (destroyed chunks)
  - Experiment 3: 3 sessions with one hand, session 4 with same or other hand — D→D, ND→ND, D→ND, ND→D conditions
- **Measures**: Choice time (ChT: time from LED illumination to first button press — reflects memory/selection) and movement time (MvT: time between first and second button press — reflects motor execution)

### Key findings

- **Spontaneous chunk emergence**: Subjects performed 10-set sequences as 2-5 clusters (chunks) separated by long ChTs; chunk patterns became clearer and more consistent with learning (Experiment 1)
- **Subject-specific chunking**: Different subjects learning the same sequence formed different chunk patterns; no significant correlation in ChT patterns across subjects (only 1 of 28 pairs correlated), while MvT patterns were highly correlated (Experiment 1)
- **Independence from physical parameters**: ChT patterns were uncorrelated with movement distances (ChT-distance: r not significant), while MvT strongly correlated with movement distance (r=0.48); chunk patterns were not determined by motor demands
- **Chunks are functional memory units**: When sequences were shuffled, performance was significantly more accurate (55% vs 154% error increase) and faster (10% vs 32% time increase) when chunks were preserved vs destroyed; ChT patterns changed more when chunks were destroyed (Experiment 2)
- **Asymmetric intermanual transfer**: Chunk patterns (ChT) transferred from nondominant to dominant hand but not vice versa; significant Set×Session×Condition interaction for ChT patterns; MvT patterns changed in both transfer directions (Experiment 3)
- **Neural implications**: Results suggest dominant hemisphere (likely parietal cortex) stores learned chunks; basal ganglia may select chunks; presupplementary motor area (pre-SMA) may be involved in chunk formation and retrieval

### Computational framework

Not applicable — this is a purely empirical behavioral study. However, the findings constrain models of sequence learning and memory organization. The results suggest a hierarchical memory structure where sequences are represented as chunks (memory units containing multiple elementary movements), with chunk boundaries marked by increased retrieval/selection times. The spontaneous and subject-specific nature of chunking suggests that chunk formation is an active, individually-variable process rather than passive stimulus-driven segmentation.

### Prevailing model of the system under study

Prior to this work, the field understood motor sequence learning as involving hierarchical organization, but chunking was thought to be externally determined by sequence structure (repetition, inversion, transposition patterns) or temporal delays. The prevailing view held that chunk patterns reflected physical parameters of movements rather than internal representational organization. The functional significance of chunks — whether they were epiphenomenal or necessary for efficient sequence processing — remained unresolved. Additionally, the neural basis of chunking was unclear, though the pre-SMA, basal ganglia, and parietal cortex had been implicated in sequence learning generally.

### What this paper contributes

This paper establishes that chunking is a spontaneous, representational process during human visuomotor sequence learning, not merely an epiphenomenon of sequence structure or motor demands. Key advances include:

1. **Spontaneous chunk formation**: Demonstrates that chunks emerge without external structuring cues (repetition, delays, or pattern changes), and that different subjects form different chunk patterns for the same sequence

2. **Functional significance of chunks**: Shows that chunks are necessary for efficient sequence performance — destroying chunks impairs accuracy and speed more than preserving them when sequences are shuffled

3. **Independence from physical parameters**: Establishes that chunk patterns are determined by representational/memory organization (ChT patterns), not motor demands (MvT patterns correlate with movement distance, ChT patterns do not)

4. **Hierarchical memory structure**: Provides evidence that learned sequences are hierarchically represented as chunks containing elementary movements, with chunks acting as single memory units that can be rearranged

5. **Asymmetric intermanual transfer**: Reveals that chunk representations transfer from nondominant to dominant hand but not vice versa, suggesting dominant hemisphere storage of chunks

6. **Neural predictions**: Generates specific predictions about neural substrates — dominant parietal cortex for chunk storage, basal ganglia for chunk selection, pre-SMA for chunk formation and retrieval

### Brain regions & systems

- **Dominant parietal cortex** — proposed locus for storage of learned chunks; suggested by asymmetric intermanual transfer (nondominant→dominant only); previous imaging studies showed learning-related increases in parietal activity; lesion studies link dominant parietal damage to apraxia (temporal sequencing deficits)
- **Basal ganglia (posterior putamen, caudate nucleus)** — proposed role in selection and execution of chunked representations; inactivation studies show impaired performance of learned sequences; dopaminergic deficits in Parkinson's disease impair sequence production
- **Presupplementary motor area (pre-SMA)** — predicted role in formation and retrieval of chunks; unit recording shows activity at chunk boundaries; learning-related decrease in activation as chunks consolidate; "first trial activity" may reflect chunk loading/retrieval
- **Cerebellar dentate nucleus** — involved in storage/execution of learned sequences (previous studies using same paradigm); not specifically linked to chunking in this study
- **Prefrontal cortex** — involved in acquisition of new sequences (not learned chunk storage)

### Mechanistic insight

The paper provides substantial mechanistic insight into motor sequence learning, though it does not present a formal computational model. The key algorithmic insight is the **hierarchical chunking mechanism**: sequences are not stored as linear chains of individual movements, but as hierarchically organized chunks where each chunk contains multiple elementary movements and functions as a single memory unit.

**Computational level**: The brain solves the problem of representing and executing long motor sequences efficiently by recoding them into a hierarchical structure with fewer, larger units (chunks), overcoming working memory limitations.

**Algorithmic level**: 
- **Chunk formation**: Spontaneous grouping of sets into clusters based on learning history (errors create breakpoints)
- **Chunk as memory unit**: Each chunk is retrieved and executed as a single unit, evidenced by preserved performance when chunks are rearranged but destroyed performance when chunks are split
- **Hierarchical representation**: Sequences represented as chunks containing elementary movements; chunks can be linked to form longer sequences

**Implementational level**: The paper proposes specific neural substrates:
- **Dominant parietal cortex**: Stores the chunk representations (supported by asymmetric transfer data)
- **Basal ganglia**: Selects and initiates chunked actions
- **Pre-SMA**: Forms new chunks and retrieves stored chunks at sequence boundaries

While no formal model is presented, the findings constrain computational models of sequence learning to include hierarchical chunking as a core mechanism, and provide empirical grounding for Marr's three levels of analysis in motor sequence learning.

### Limitations & open questions

- **Explicit vs implicit components**: The study did not segregate explicit and implicit learning components; chunking may reflect either or both
- **Long-term memory maintenance**: Whether chunk patterns are maintained as long-term memory like habits remains unresolved
- **Grade of learning differences**: Asymmetric transfer could be explained by different learning stages between dominant and nondominant hands rather than hemispheric specialization
- **Verbal/spatial strategies**: While unlikely based on reported strategies and previous imaging data, the possibility of non-motor learning strategies cannot be fully excluded
- **Neural correlates**: The proposed roles of parietal cortex, basal ganglia, and pre-SMA are predictions based on previous studies; direct evidence for neural chunking patterns is still needed
- **Individual differences**: The basis for why different subjects form different chunk patterns for the same sequence remains unexplained

### Connections & keywords

- **Key citations**: Miller (1956) — chunk concept; Hikosaka et al. (1995, 1996, 1998, 1999) — previous work using same paradigm; Restle and Burnside (1972); Povel and Collard (1982); Nissen and Bullemer (1987); Stadler (1989, 1993); Cohen et al. (1990); Keele and Jennings (1992); Curran and Keele (1993); Koch and Hoffmann (2000) — previous chunking studies
- **Named models or frameworks**: 2×10 task (visuomotor sequence learning paradigm); hierarchical chunking model of motor sequence representation; Marr's three levels of analysis (computational, algorithmic, implementational)
- **Brain regions**: dominant parietal cortex, basal ganglia (posterior putamen, caudate nucleus), presupplementary motor area (pre-SMA), prefrontal cortex, cerebellar dentate nucleus
- **Keywords**: motor sequence learning, chunking, hierarchical memory representation, visuomotor learning, explicit learning, intermanual transfer, motor memory, choice time, movement time, dominant hemisphere, procedural memory, motor skill acquisition, sequence organization, working memory limitations
