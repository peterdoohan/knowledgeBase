---
source_file: redish2016_vicarious_trial_error_b.md
title: Vicarious trial and error
authors: A. David Redish
year: 2016
journal: Nature Reviews Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

Vicarious trial and error (VTE) in rodents reflects a deliberative decision-making process characterized by serial mental search through imagined future outcomes, supported by hippocampal-prefrontal interactions and distinct from procedural action-selection systems.

### Background & motivation

Since the 1930s, researchers observed that rats pause and look back-and-forth at decision points in mazes, termed "vicarious trial and error" (VTE). Early hypotheses suggested rats were mentally simulating future options, but without mechanistic explanations, these ideas gave way to simpler situation-action theories. The advent of neural ensemble recording and decoding techniques in the 2000s enabled direct investigation of the neural substrates underlying VTE, allowing researchers to test whether this behaviour truly reflects internal deliberation. This review synthesizes behavioural and neurophysiological evidence to argue that VTE is indeed a behavioural manifestation of deliberative, model-based decision-making in non-human animals.

### Methods

This is a narrative review synthesizing literature on vicarious trial and error across multiple experimental paradigms. The review covers:

- **Behavioural tasks**: Tolman-Hull plus maze, multiple-T task, cued-T task, spatial delay-discounting task, restaurant row task, elevated plus maze
- **Quantification methods**: zIdPhi measure (integrated absolute angular velocity) to differentiate VTE from non-VTE laps
- **Neural recording techniques**: Hippocampal place cell ensemble recording, local field potential (LFP) analysis of theta and sharp-wave ripple (SWR) activity, simultaneous multi-structure recordings (hippocampus, prefrontal cortex, striatum, orbitofrontal cortex)
- **Intervention methods**: Lesion studies, pharmacological manipulations (cannabinoid agonist CP55940, clonidine), optogenetic silencing

### Key findings

- VTE occurs when animals use flexible, deliberative decision strategies and vanishes as behaviour automates to procedural strategies; VTE reappears following changes in reward-delivery contingencies or reward devaluation
- VTE is preferentially expressed at difficult choice points (near decision thresholds) and diminishes when choices are easy (very high or very low value options)
- During VTE, hippocampal place cells fire in theta sequences ("sweeps") that serially alternate between representations of potential future paths toward each goal option
- Hippocampal-prefrontal LFP coherence increases transiently at choice points during VTE episodes
- Ventral striatal neurons show covert reward-related firing during VTE, before the animal commits to a choice; orbitofrontal cortex shows reward-related activity only after the turn-around point (post-decision)
- Dorsolateral striatum does not show transient future representations during VTE; instead, it develops task-bracketing activity as behaviour automates, which is negatively correlated with VTE expression
- Cannabinoid agonists increase VTE while disrupting hippocampal theta sequences; clonidine decreases VTE while apparently limiting mental search to a single path

### Computational framework

The paper frames VTE within a **search-and-evaluate deliberative decision-making framework**, a model-based system distinct from procedural (cached action-chain) systems. The framework involves three key steps:

1. **Search**: Using a cognitive map (schema of how the world works), the animal mentally constructs potential future outcomes by simulating action consequences. This involves serial, alternating representations of different options.

2. **Evaluate**: Each imagined outcome is evaluated in light of current goals and needs. This involves assigning value to constructed futures.

3. **Select**: Based on the evaluation, an action is selected to achieve the desired future.

This deliberative system is contrasted with **procedural decision-making**, which uses cached action chains released in response to situation categorization without constructing future outcomes. The framework draws on concepts from reinforcement learning (model-based vs. model-free), Bayesian decision theory, and Marr's levels of analysis.

### Prevailing model of the system under study

Before the neurophysiological findings reviewed here, the field understood decision-making in rodents primarily through two competing frameworks:

1. **Situation-action chain hypotheses (Hull)**: Behavior arises from recognizing situations and releasing well-learned action sequences. This view suggests VTE might simply reflect information gathering or indecision during learning, not mental simulation.

2. **Cognitive map hypothesis (Tolman)**: Animals construct internal representations of the world (cognitive maps) that enable flexible, goal-directed behavior. This view suggests VTE reflects mental exploration of options, but lacked mechanistic details about how such mental search might be implemented neurally.

The prevailing model also distinguished between flexible cognitive strategies (hippocampus-dependent) and habitual/procedural strategies (dorsal striatum-dependent), but the specific neural mechanisms by which deliberation occurred—and whether VTE truly reflected mental simulation—remained unresolved and debated.

### What this paper contributes

This review synthesizes behavioural and neurophysiological evidence to establish that:

1. **VTE is a behavioural signature of deliberation**: The evidence supports the original 1930s hypothesis that VTE reflects mental search through imagined future outcomes, not merely sensory information gathering or exploratory behaviour. VTE occurs specifically when animals must make flexible, model-based decisions, and disappears when behaviour becomes procedural.

2. **Neural mechanisms of deliberation are identified**: The hippocampus generates serial, alternating representations of potential future paths (theta sequences/sweeps) during VTE. These sweeps are coordinated with prefrontal cortex and evaluated by ventral striatum and orbitofrontal cortex, constituting a neural circuit for model-based decision-making.

3. **Two distinct decision systems are characterized**: The review distinguishes a deliberative system (hippocampus-PFC-ventral striatum) that constructs and evaluates future outcomes, from a procedural system (dorsolateral striatum) that caches action chains. These systems show distinct neural signatures and are differentially engaged during VTE versus automated behaviour.

4. **Non-human animals engage in mental time travel**: The evidence demonstrates that rodents, like humans, can engage in episodic future thinking—mentally simulating potential futures to guide decisions—providing an animal model for studying the neural basis of deliberation, working memory, and mental time travel.

### Brain regions & systems

- **Hippocampus**: Generates theta sequences (sweeps) that serially represent potential future paths during VTE; encodes the cognitive map enabling mental simulation; shows theta oscillations during deliberation. Damage disrupts VTE during learning and increases VTE during later automated stages.

- **Prefrontal cortex (prelimbic cortex)**: Proposed initiator of VTE process; sends requests to hippocampus for episodic future simulation; shows increased theta coherence with hippocampus during VTE; necessary for flexible strategy switching but not well-learned behaviors.

- **Ventral striatum (nucleus accumbens)**: Encodes evaluation of imagined outcomes during deliberation; shows covert reward-related firing before the turn-around point during VTE; involved in representing motivational significance and expected reward value.

- **Orbitofrontal cortex (OFC)**: Represents expected rewards after decision commitment; shows covert reward signals after the turn-around point (post-decision); involved in outcome-specific representations and economic value coding.

- **Dorsolateral striatum**: Critical for procedural decision-making; develops task-bracketing activity as behavior automates; shows local firing without future sweeps during VTE; disruption shifts behavior toward deliberative strategies.

- **Dorsomedial striatum**: May have roles in deliberative component; shows differential dynamics during learning; specific roles in decision-making remain incompletely explored.

- **Infralimbic cortex**: May have contrasting roles to prelimbic cortex; involved in learned, automated procedural strategies.

- **Amygdala**: Involved in anxiety-related VTE behaviors; shows coupling with hippocampus during stretch-attend postures; signals during foraging in hazardous environments.

### Mechanistic insight

This paper provides strong mechanistic insight at all three of Marr's levels:

**Computational level**: The paper frames deliberation as a search-and-evaluate process wherein an agent uses a cognitive map (schema) to construct potential future outcomes, evaluates them against current goals, and selects actions accordingly. This contrasts with procedural decision-making, which caches action chains. The computational problem is mental time travel—simulating episodic futures to guide present decisions.

**Algorithmic level**: The algorithm involves serial, alternating construction of potential future paths via hippocampal theta sequences (sweeps). The prefrontal cortex initiates requests for future simulation; the hippocampus responds by computing consequences of potential action sequences. Evaluation occurs through ventral striatum (pre-decision) and orbitofrontal cortex (post-decision) value representations. The algorithm is serial rather than parallel, with options constructed and evaluated individually.

**Implementational level**: The neural implementation involves:
- **Hippocampus**: Generates theta sequences (sweeps) representing future paths; theta oscillations (6-10 Hz) coordinate the sequential firing of place cells. Self-consistent representations are decoded from neural ensembles.
- **Prefrontal cortex (prelimbic)**: Shows increased theta coherence with hippocampus during VTE; initiates simulation requests; necessary for flexible deliberation.
- **Ventral striatum**: Shows covert reward-related firing during deliberation, before behavioral commitment.
- **Orbitofrontal cortex**: Shows reward expectation signals after decision commitment.
- **Dorsolateral striatum**: Shows task-bracketing activity during procedural (non-deliberative) behavior; no future sweeps during VTE.

The paper thus provides a comprehensive mechanistic account linking behavior (VTE) to algorithm (serial search-and-evaluate) to neural implementation (hippocampal-prefrontal-striatal circuits).

### Limitations & open questions

- **How does the process decide which potential futures to search?** Mental construction requires a recall process modulated by goals, but how preferences drive mental search representations remains unknown.

- **How are the options evaluated?** Whether evaluation during VTE works through processes homologous to human evaluative processes remains controversial; the specific mechanisms of applying perceptual valuation to imagined outcomes in rodents are unclear.

- **How is the action selected?** Studies have failed to find a relationship between the directions being represented during VTE and the eventual choice in normal animals; the action-selection process that ends deliberation remains unknown.

- **Integration-to-threshold signals**: Unlike perceptual decision-making, neural recordings in ventral striatum and orbitofrontal cortex have failed to find integration-to-threshold signals during VTE.

- **Relationship between reward devaluation and deliberative search**: The hypothesis that reward evaluation drives deliberative search may require a more complicated process model that separates one-step and multistep processes.

- **Dorsomedial striatum roles**: Specific roles of the dorsomedial striatum in deliberation remain incompletely explored.

- **Unified hippocampal representation**: Whether hippocampal ensembles encode unified representations across dorsal and ventral hippocampus during VTE remains unknown.

- **SWR-theta relationship**: The relationship between SWRs that occur before journey starts and theta sequences during VTE remains unknown.

- **Human parallels**: Although saccade-fixate-saccade (SFS) in primates may parallel VTE, direct comparative evidence remains limited.

### Connections & keywords

**Key citations:**
- Muenzinger & Gentry (1931) - Original VTE observation
- Tolman (1939, 1948) - Cognitive map and VTE as prospective imagination
- Hull (1943) - Situation-action chain hypothesis
- O'Keefe & Nadel (1978) - Hippocampus as cognitive map
- Johnson & Redish (2007) - Hippocampal sequences at choice points
- Daw, Niv & Dayan (2005) - Uncertainty-based competition between decision systems
- Redish (1999) - Beyond the Cognitive Map
- Buckner & Carroll (2007) - Self-projection and the brain
- Schacter & Addis (2011) - Episodic future thinking

**Named models or frameworks:**
- Cognitive map theory (Tolman)
- Search-and-evaluate deliberation framework
- Model-based vs. model-free reinforcement learning
- Multiple decision systems hypothesis (deliberative vs. procedural)
- Integration-to-threshold decision theory
- Episodic future thinking / mental time travel
- Visuospatial scratchpad (working memory)
- Task bracketing (dorsolateral striatum)

**Brain regions:**
- Hippocampus (CA3, CA1, dentate gyrus)
- Prefrontal cortex (prelimbic cortex, infralimbic cortex, medial PFC)
- Ventral striatum (nucleus accumbens)
- Orbitofrontal cortex (OFC)
- Dorsolateral striatum
- Dorsomedial striatum
- Amygdala
- Nucleus reuniens (thalamus)

**Keywords:**
vicarious trial and error, VTE, deliberation, decision-making, hippocampus, theta sequences, mental time travel, episodic future thinking, cognitive map, model-based reinforcement learning, place cells, prefrontal cortex, ventral striatum, orbitofrontal cortex, procedural learning, working memory, behavioral flexibility, spatial navigation, reward evaluation
