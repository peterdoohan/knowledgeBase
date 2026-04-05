---
source_file: tsao2022_neural_bases_timing_durations.md
title: The neural bases for timing of durations
authors: Albert Tsao, S. Aryana Yousefzadeh, Warren H. Meck, May-Britt Moser, Edvard I. Moser
year: 2022
journal: Nature Reviews Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

This review proposes that prospective timing (tracking ongoing durations) and retrospective timing (estimating past durations from memory) rely on distinct computational mechanisms both using population state dynamics: stable neural trajectories for prospective timing versus event trajectories generated through event segmentation for retrospective timing.

---

### Background & motivation

Time perception research has historically been divided between studies of prospective timing (attending to ongoing time intervals) and retrospective timing (reconstructing duration from memory). These two forms of timing have largely been studied in isolation using different experimental paradigms and theoretical frameworks. This review integrates these perspectives by proposing that both rely on population-level neural representations but implement distinct computational strategies: prospective timing uses ongoing population dynamics directly as the computation, while retrospective timing uses event-segmented population states that are later recalled and converted into duration estimates.

---

### Methods

This is a comprehensive review paper synthesizing literature across multiple domains:

- **Literature scope**: Extensive coverage of timing research from human behavioural studies, human fMRI, and animal single-unit recordings
- **Key domains integrated**:
  - Prospective timing (sensory, motor, and implicit timing)
  - Retrospective timing and episodic memory
  - Event segmentation theory
  - Computational modelling (recurrent neural networks)
- **Cross-species comparison**: Human, monkey, and rodent studies
- **Analytical approaches reviewed**: Dimensionality reduction of neural population activity, representational similarity analysis, computational modelling

---

### Key findings

**Prospective timing mechanisms**:
- Neural population activity evolves along stable trajectories during ongoing durations, providing reliable temporal information
- Inactivation of brain areas exhibiting trajectories impairs timing behaviour
- Trial-to-trial trajectory variability correlates with timing variability
- Three distinct trajectory implementations:
  - **Sensory timing**: Common trajectory reaches different terminal states for different durations
  - **Motor timing**: Common trajectory reaches common terminal state at different speeds (temporal scaling)
  - **Temporal expectation**: Trajectory shifts reflect learned temporal structures

**Timescales of prospective timing**:
- Neural trajectories operate from ~1 second to several minutes
- Hippocampus plays a central role for durations of tens of seconds and longer
- Potential overlap with path integration mechanisms for longer durations

**Retrospective timing mechanisms**:
- Duration estimates correlate with number of remembered events (event segmentation)
- Manipulating event structure affects retrospective duration estimates
- Neural event trajectories encode event structure through discretized population states
- Event boundaries correspond to greater changes in population state
- Event trajectories evolve at different rates across hippocampal subfields and entorhinal cortex

**Computational insights**:
- Recurrent neural networks can generate stable trajectories without specialized structure
- Speed modulation in motor timing emerges from interaction of duration input with nonlinear activation functions
- Temporal context models based on Laplace transform provide potential mechanism for converting event trajectories into duration estimates

**Neuromodulatory influences**:
- Dopamine controls trajectory speed (increased dopamine → time overestimation)
- Dopamine also influences trajectory formation through reinforcement learning
- Acetylcholine affects memory of learned intervals rather than ongoing trajectory evolution

**Bidirectional interactions**:
- Learning temporal structures can transform event trajectories into stable trajectories (episodic to semantic)
- Repeated experience generates temporal schemas
- Learned schemas can influence online event segmentation

---

### Computational framework

The review operates within a **dynamical systems framework** for understanding neural computation of time:

**Core formalism**:
- Time is encoded through changes in neural population activity (population state dynamics)
- Each moment in time corresponds to a unique point in neural state space
- The evolution of population states traces a trajectory that inherently contains temporal information

**Key computational principles**:
- **Population clocks**: Time emerges from the dynamics of recurrently connected neural networks rather than dedicated pacemaker mechanisms
- **State-dependent computation**: The network's current state determines how it evolves, enabling self-sustaining trajectories
- **Temporal scaling**: Duration can be encoded by modulating the speed of trajectory evolution while maintaining the same geometric path

**Computational modelling approaches reviewed**:
- Recurrent neural networks (RNNs) trained on timing tasks
- State-dependent network models for sensory timing
- Laplace transform-based temporal context models for retrospective timing
- Predictive coding models of event segmentation

**Marr's levels applied**:
- **Computational**: The brain must represent time for both online tracking (prospective) and memory-based reconstruction (retrospective)
- **Algorithmic**: Different algorithms for prospective (direct trajectory evolution) vs retrospective (event segmentation + trajectory recall/conversion)
- **Implementational**: Population dynamics in cortico-striatal circuits (prospective) and medial temporal lobe (retrospective)

---

### Prevailing model of the system under study

The review synthesizes several established theoretical frameworks:

**For prospective timing**:
- The dominant model has been the **pacemaker-accumulator** mechanism, where a central pacemaker generates pulses that are integrated to estimate time
- Alternative proposals suggested **coincidence detection of oscillatory activity** as the neural implementation
- Both models assume a dedicated internal clock generating explicit linear metrical representations of time

**For retrospective timing**:
- The prevailing view is that retrospective timing relies on **reconstructive processes** using both temporal and non-temporal information from memory
- **Event segmentation theory** posits that continuous experience is parsed into discrete events, and the structure of these events provides temporal information
- Psychological models suggest duration estimates are inferred from contextual changes and number of remembered events

**The debate between dedicated vs distributed timing**:
- A long-standing debate exists between whether timing is supported by a **dedicated central clock** versus **distributed local representations** of time reflecting the inherent temporal nature of many brain functions
- The review proposes a synthesis: both prospective and retrospective timing use distributed population dynamics, but with different computational implementations

---

### What this paper contributes

This review makes several important contributions to our understanding of temporal cognition:

**Theoretical integration**:
- Proposes a **unified framework** for understanding both prospective and retrospective timing as relying on population state dynamics, while clearly distinguishing their distinct computational implementations
- Bridges the gap between the largely separate literatures on prospective timing (typically studied in sensorimotor contexts) and retrospective timing (typically studied in episodic memory contexts)

**Computational distinctions**:
- **Prospective timing**: Characterized as a **single-step process** where ongoing population dynamics directly serve as the computation of duration. The trajectory evolution is itself the estimation process.
- **Retrospective timing**: Characterized as a **two-step process**: (1) event segmentation generates population state dynamics during initial encoding, and (2) subsequent computation of duration from memory of those dynamics.

**Neural mechanism insights**:
- Identifies **stable neural trajectories** (for prospective timing) and **event trajectories** (for retrospective timing) as distinct neural implementations
- Maps these mechanisms onto specific brain systems: cortico-striatal circuits for prospective timing, medial temporal lobe (hippocampus and entorhinal cortex) for retrospective timing
- Proposes that the lateral entorhinal cortex plays a central role in generating event trajectories

**Timescale considerations**:
- Demonstrates how different neural mechanisms operate across different timescales, from subsecond to minutes and beyond
- Links shorter-timescale prospective timing to cortico-striatal dynamics and longer-timescale timing to hippocampal mechanisms

**Bidirectional interactions**:
- Proposes mechanisms by which prospective and retrospective timing systems interact: transformation of episodic memories into semantic temporal knowledge, formation of temporal schemas, and influence of learned schemas on online event segmentation

**Testable predictions**:
- Generates specific predictions about how manipulations of neural trajectory speed should affect timing behaviour (supported by temperature manipulation studies)
- Predicts how event segmentation manipulations should affect retrospective timing
- Suggests experimental approaches to test the transformation between event trajectories and stable trajectories

---

### Brain regions & systems

**Cortico-striatal circuits (prospective timing)**:
- **Premotor cortex**: Exhibits neural trajectories during temporal expectation tasks; neural population activity evolves reflecting windows of expectation
- **Prefrontal cortex (medial)**: Shows ramping activity and neural trajectories during motor timing; cooling studies demonstrate causal role in timing
- **Prefrontal cortex (dorsolateral)**: Contains temporal information during sensory timing tasks
- **Orbitofrontal cortex**: Contains temporal information during sensory timing but less than striatum
- **Striatum (dorsolateral)**: Exhibits sequential activity and greater temporal information than cortical areas; shows temporal scaling during motor timing; temperature manipulation affects duration judgments
- **Striatum (dorsomedial)**: Receives input from medial frontal cortex; involved in temporal processing
- **Cerebellum**: Implicated in event timing and subsecond timing mechanisms

**Medial temporal lobe (retrospective timing)**:
- **Hippocampus (CA1)**: Shows event trajectories evolving over timescales of days; population states become increasingly dissimilar with temporal distance; time cells fire at specific moments tiling intervals
- **Hippocampus (CA2)**: Shows fastest rate of event trajectory evolution; distinguishes time points separated by hours
- **Hippocampus (CA3)**: Population states remain largely constant across days; involved in pattern completion and temporal order memory
- **Dentate gyrus**: Shows slow evolution of event trajectories; may operate on timescales of weeks
- **Entorhinal cortex (lateral)**: Generates event trajectories reflecting content of ongoing experience; evolves faster than hippocampus (distinguishes minutes); major hub for cortical input; integrates multimodal information; proposed as generator of event trajectories
- **Entorhinal cortex (medial)**: Does not differentiate between repeated experiences within same physical environment; involved in spatial representation and path integration
- **Perirhinal cortex**: Involved in pattern separation and event representation
- **Parahippocampal gyrus**: Contains boundary-responsive cells
- **Amygdala**: Contains boundary-responsive cells

**Sensory and motor areas**:
- **Primary visual cortex**: Shows modulation by temporal expectation; can learn reward timing through cholinergic mechanisms
- **Primary auditory cortex**: Shows enhanced frequency tuning approaching periods of high temporal expectation
- **Visual cortex (inferior temporal)**: Shows attentional modulation by temporal expectation
- **Motor cortex**: Shows temporal scaling of activity during motor timing; involved in generating timed actions
- **Supplementary motor area**: Contains neurons encoding interval times
- **Premotor cortex**: Shows neural trajectories during temporal expectation tasks

**Subcortical structures**:
- **Substantia nigra pars compacta**: Dopaminergic neurons show activity correlated with duration estimates; optogenetic manipulation shifts duration estimates
- **Basal ganglia (general)**: Proposed as site of coincidence detection for interval timing
- **Thalamus (sensory and motor)**: Contains neurons encoding temporal intervals and predictive timing

---

### Mechanistic insight

This review meets the high bar for mechanistic insight by synthesizing evidence that links computational algorithms to neural implementation through population dynamics.

**Computational level (what problem is the brain solving?)**:
- The brain must represent elapsed time for both online tracking (prospective timing) and memory-based reconstruction (retrospective timing)
- Both require uniquely representing each moment in time, but through different strategies
- The problem is solved without dedicated clocks, using intrinsic neural dynamics

**Algorithmic level (what representations and processes implement the solution?)**:
- **Prospective timing**: Population activity evolves along stable trajectories where each moment corresponds to a unique neural state. Duration is encoded either by:
  - Reaching different terminal states from common starting points (sensory timing)
  - Evolving at different speeds to reach common terminal states (motor timing)
  - Shifting to expectation-related states (temporal expectation)
- **Retrospective timing**: Experience is segmented into discrete events, creating event trajectories. Duration is computed post-hoc by:
  - Reinstating population states from memory
  - Converting the difference between event representations into duration estimates
  - Using contextual drift or counting state changes

**Implementational level (how is this realized in neural hardware?)**:
- **Prospective timing**: Implemented in cortico-striatal circuits
  - Recurrent connections within local circuits generate self-sustaining trajectories
  - External input shapes but does not solely drive trajectory evolution
  - Striatum refines cortical trajectories through cortico-striatal loops
  - Temperature manipulations in medial prefrontal cortex and striatum directly affect timing by altering neural dynamics speed
  - Dopamine modulates trajectory speed through D2 receptors
  - Individual neurons show diverse patterns: ramping, sequential (time cells), and complex non-monotonic activity

- **Retrospective timing**: Implemented in medial temporal lobe
  - Lateral entorhinal cortex (LEC) integrates multimodal cortical input and generates event trajectories
  - Hippocampal subfields (CA1, CA2, CA3, dentate gyrus) process event trajectories at different timescales
  - Event boundaries cause rapid changes in population state, creating discrete event representations
  - Pattern separation and pattern completion mechanisms segment continuous input into discrete events
  - Cells specifically responsive to event boundaries observed in hippocampus, parahippocampal gyrus, and amygdala
  - Event trajectories evolve at different rates across regions: minutes (LEC), hours (CA2), days (CA1), weeks (dentate gyrus)

**Physical implementation details**:
- Neuromodulatory systems provide control over timing mechanisms:
  - Dopamine: Controls trajectory speed and formation through reinforcement learning
  - Acetylcholine: Modulates memory consolidation of learned intervals
- Temperature manipulations demonstrate causal link between neural dynamics speed and timing behaviour
- Multiple timescales emerge from different brain regions and mechanisms

---

### Limitations & open questions

**Empirical limitations**:
- Direct evidence for neural event trajectories in retrospective timing remains limited; most evidence comes from prospective timing paradigms adapted to study memory
- Animal paradigms for pure retrospective timing (where subjects cannot anticipate timing requirements) are underdeveloped
- The actual computation converting event trajectories into duration estimates remains essentially unknown
- Whether neural trajectories can encode durations beyond several minutes is unknown

**Mechanistic gaps**:
- How trajectory speed is precisely controlled in motor timing remains unclear
- The transformation from event trajectories (retrospective) to stable trajectories (prospective) through learning has not been directly observed
- Whether the same neural circuits can flexibly switch between prospective and retrospective timing modes is unknown
- How temporal information from different timescales (subsecond to days) is integrated remains unclear

**Computational uncertainties**:
- Whether event trajectories are suitable as linear metrics of physical time is questionable given their nonlinear, event-driven nature
- Alternative mechanisms for sensory timing involving temporal arithmetic (comparing abstract temporal representations) have not been fully ruled out
- The relative contributions of different brain regions to the final duration estimate in retrospective timing remain unclear

**Methodological challenges**:
- Distinguishing whether observed neural activity represents time per se versus time-correlated variables (movement, reward expectation) remains difficult
- Determining whether temporal information in neural trajectories is actually used by the brain (vs. merely present) requires more sophisticated approaches
- Cross-species comparisons are complicated by differences in experimental paradigms and cognitive capabilities

**Future directions highlighted**:
- Development of experimental paradigms that can distinguish prospective and retrospective timing contributions
- Direct investigation of how event trajectories are converted into duration estimates
- Time-lapse studies tracking the transformation of event trajectories into stable trajectories through learning
- Investigation of how learned temporal schemas influence online event segmentation
- Examination of interactions between timing mechanisms across different timescales

---

### Connections & keywords

**Key citations**:
- Buhusi & Meck 2005 (Nat Rev Neurosci) - Neural mechanisms of interval timing
- Merchant, Harrington & Meck 2013 (Annu Rev Neurosci) - Neural basis of time perception
- Eichenbaum 2014 (Nat Rev Neurosci) - Hippocampal time cells
- Hicks et al. 1976 (Am J Psychol) - Prospective vs retrospective timing dissociation
- Mankin et al. 2012 (PNAS) - CA1 event trajectories over days
- Tsao et al. 2018 (Nature) - LEC stable vs event trajectories
- Baldassano et al. 2017 (Neuron) - Hierarchical event segmentation
- Jazayeri & Shadlen 2015 (Curr Biol) - Ready-set-go sensorimotor timing
- Wang et al. 2018 (Nat Neurosci) - Temporal scaling of cortical responses
- Gouvêa et al. 2015 (Elife) - Striatal dynamics explain duration judgments
- Roseboom et al. 2019 (Nat Commun) - Activity in perceptual networks as basis for subjective time
- Fountas et al. 2022 (Neural Comput) - Predictive processing model of episodic memory and time
- Howard & Kahana 2002 (J Math Psychol) - Distributed representation of temporal context
- Zacks & Tversky 2001 (Psychol Bull) - Event structure in perception and conception

**Named models or frameworks**:
- Pacemaker-accumulator model
- Oscillatory coincidence detection
- Population clock
- Neural trajectory
- Event trajectory
- Temporal context model (Laplace transform)
- Event segmentation theory
- Scalar property / Weber's law for timing
- State-dependent network model
- Recurrent neural network models of timing
- Laplace transform model of event history
- Predictive coding models of event segmentation

**Brain regions**:
- Hippocampus (CA1, CA2, CA3, dentate gyrus)
- Lateral entorhinal cortex
- Medial entorhinal cortex
- Dorsolateral striatum
- Dorsomedial striatum
- Medial prefrontal cortex
- Dorsolateral prefrontal cortex
- Orbitofrontal cortex
- Premotor cortex
- Motor cortex / supplementary motor area
- Primary visual cortex
- Primary auditory cortex
- Inferior temporal cortex
- Visual cortex (various areas)
- Angular gyrus
- Parahippocampal gyrus
- Amygdala
- Perirhinal cortex
- Substantia nigra pars compacta
- Basal ganglia
- Thalamus (sensory and motor)
- Cerebellum

**Keywords**:
prospective timing, retrospective timing, interval timing, neural trajectories, population clocks, population state dynamics, event segmentation, event trajectories, time cells, sequence coding, temporal context, corticostriatal circuits, lateral entorhinal cortex, hippocampal temporal hierarchy, medial temporal lobe, dopaminergic trajectory speed control, temporal scaling, episodic memory, duration estimation, reconstructive memory, state-dependent networks, recurrent neural networks, Marr's levels, neuromodulation, event boundaries, contextual drift, path integration
