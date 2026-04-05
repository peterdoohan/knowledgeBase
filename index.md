# Knowledge Base Index

This file is the primary navigation and search index for the wiki.
Agents should read this file to locate relevant wiki pages before globbing the directory tree.
Update this file whenever wiki pages are created, renamed, or deleted.

---

## Wiki structure

```yaml
wiki:
  brain_regions:
    anterior_cingulate_cortex.md: Anterior cingulate cortex (ACC) and model-based action selection
    anterior_lateral_motor_cortex.md: Anterior lateral motor cortex (ALM) and discrete attractor dynamics
    brainstem_oculomotor_integrator.md: Brainstem oculomotor integrator and line attractor dynamics
    frontal_eye_field.md: Frontal eye field (FEF) and spatial attention, temporal expectation, multiplexing
    head_direction_circuit.md: Head direction circuit and ring attractor dynamics
    prefrontal_cortex.md: Prefrontal cortex and executive function
    medial_prefrontal_cortex.md: Medial prefrontal cortex (mPFC) circuit organization and cell-type-specific wiring
    prelimbic_cortex.md: Prelimbic cortex (PL) and investigatory control
    infralimbic_cortex.md: Infralimbic cortex (IL) and emotion/motivation circuits
    basolateral_amygdala.md: Basolateral amygdala (BLA) and emotional learning
    mediodorsal_thalamus.md: Mediodorsal thalamus (MD) and working memory
    ventromedial_thalamus.md: Ventromedial thalamus (VM) and arousal regulation
    ventral_hippocampus.md: Ventral hippocampus (vHPC) and emotional/contextual processing
    striatum.md: Striatum and basal ganglia function in reinforcement learning
    zona_incerta.md: Zona incerta and cell-type-specific circuit functions
    periaqueductal_gray.md: Periaqueductal gray and behavior gating
    primary_auditory_cortex.md: Primary auditory cortex (A1) and auditory processing
    inferior_frontal_gyrus.md: Inferior frontal gyrus (IFG) / Broca area
    superior_temporal_gyrus.md: Superior temporal gyrus (STG)
    hippocampus.md: Hippocampus and episodic memory formation
    hippocampus_ca1.md: Hippocampus CA1 subregion and place cells
    hippocampus_ca3.md: Hippocampus CA3 subregion and attractor dynamics
    ventral_tegmental_area.md: Ventral tegmental area (VTA) and dopamine reward signals
    substantia_nigra.md: Substantia nigra (pars compacta) and dopamine prediction errors
    medial_entorhinal_cortex.md: Medial entorhinal cortex (MEC) and grid cells, spatial navigation
    entorhinal_cortex.md: Entorhinal cortex and relational structure representation in abstract RL
    orbitofrontal_cortex.md: Orbitofrontal cortex (OFC) and state-value computation in cognitive maps
    ventromedial_prefrontal_cortex.md: Ventromedial prefrontal cortex (vmPFC) and structure-sensitive prediction errors
    ventral_striatum.md: Ventral striatum and structure-dependent reward prediction errors
    posterior_cingulate_cortex.md: Posterior cingulate cortex and structure-sensitive learning signals
    retrosplenial_cortex.md: Retrosplenial cortex and translation between egocentric/allocentric reference frames
    dorsolateral_entorhinal_cortex.md: Dorsolateral band of entorhinal cortex necessary for spatial memory recall
    ventromedial_entorhinal_cortex.md: Ventromedial band of entorhinal cortex mediating defensive behavior
    insular_cortex.md: Insular cortex (IC) and incentive learning for goal-directed action
  behaviours:
    conditioning.md: Classical conditioning and associative learning mechanisms
    five_choice_serial_reaction_time_task.md: 5-Choice Serial Reaction Time Task (5-CSRTT) for attention and impulsivity
    auditory_steady_state_response.md: 40-Hz auditory steady-state response (ASSR) paradigm
    belief_updating.md: Belief updating in probabilistic inference tasks
    cognitive_impairment.md: General cognitive impairment and its relationship to computational phenotypes
    cognitive_map.md: Cognitive map formation and spatial representation
    decision_making.md: Decision making processes and computational mechanisms
    detours.md: Detour problem and route replanning during navigation
    delusions.md: Delusions as self-reinforcing attractor states in belief updating
    goal_directed_behaviour.md: Goal-directed behaviour and action-outcome learning
    grid_cells.md: Grid cells in entorhinal cortex and spatial representation
    habits.md: Habit learning and stimulus-response associations
    hallucinations.md: Hallucinations and auditory perceptual abnormalities
    memory_consolidation.md: Memory consolidation and systems consolidation
    mismatch_negativity.md: Mismatch negativity (MMN) paradigm
    mood_disorders.md: Mood disorders and belief updating abnormalities
    novelty_seeking.md: Novelty-seeking and curiosity-driven exploration
    investigatory_behavior.md: Deep vs shallow investigatory behavior states
    planning.md: Prospective planning and mental simulation
    event_segmentation.md: Event segmentation and temporal community structure
    psychosis.md: Psychosis and positive symptoms
    response_stochasticity.md: Response stochasticity in probabilistic inference
    schema_learning.md: Schema learning and prior knowledge effects
    schizophrenia.md: Schizophrenia and related computational phenotypes
    spatial_navigation.md: Spatial navigation and allocentric behavior
    temporal_expectation.md: Temporal expectation and predictive timing
    two_step_task.md: Two-step task for dissociating model-based and model-free RL
    hippocampal_replay.md: Hippocampal replay during SWRs
    reverse_replay.md: Reverse replay and temporal credit assignment
    forward_replay.md: Forward replay and prospective planning
    sharp_wave_ripples.md: Sharp-wave ripples (SWRs) and memory reactivation
    place_cells.md: Hippocampal place cells and spatial representation
    reward_processing.md: Reward processing in the hippocampus
    path_integration.md: Path integration and dead reckoning via velocity integration
    learning.md: Learning and spatial learning across stages
  computational_frameworks:
    temporal_difference_learning.md: Temporal difference (TD) learning and dopamine prediction errors
    active_inference.md: Active inference and the free energy principle
    attractor_networks.md: Attractor network dynamics in neural computation
    mixed_selectivity.md: Mixed selectivity coding in neural populations
    neural_manifold.md: Neural manifold and low-dimensional population dynamics
    successor_representation.md: Successor representation for model-based RL
    extended_finite_state_machine.md: Extended finite state machines for task formalisms
    extended_finite_state_machine.md: Extended finite state machines for task formalisms
    bayesian_inference.md: Bayesian inference and probabilistic reasoning
    cortical_microcircuit.md: Canonical cortical microcircuit and neural mass models
    hierarchical_gaussian_filter.md: Hierarchical Gaussian Filter for belief updating
    latent_state_inference.md: Latent state inference for flexible behaviour
    model_based_rl.md: Model-based reinforcement learning with prospective planning
    model_free_rl.md: Model-free reinforcement learning through cached values
    reinforcement_learning.md: Reinforcement learning computational framework
    residue_number_system.md: Residue number system for grid cell position encoding
    state_representation.md: State representation in learning and decision-making
    temporal_credit_assignment.md: Temporal credit assignment in reinforcement learning
    compositionality.md: Compositionality in cognitive maps and predictive representations
  methods:
    pycontrol.md: pyControl open-source behavioral control system
    high_throughput_behavioral_testing.md: High-throughput behavioral testing methods
    optogenetics.md: Optogenetics for causal neural manipulation
    neuropixels.md: Neuropixels high-density silicon probes for large-scale recordings
    kilosort.md: Kilosort spike sorting framework
    allen_mouse_brain_atlas.md: Allen Mouse Brain Common Coordinate Framework v3
    computational_psychiatry.md: Computational approaches to psychiatric phenotyping
    dynamic_causal_modelling.md: Dynamic Causal Modelling for inferring neural mechanisms
    parametric_empirical_bayes.md: Parametric Empirical Bayes for group-level DCM analysis
    state_vs_trait.md: State versus trait distinctions in computational psychiatry
    computational_modeling.md: Computational modeling methods for behavioral analysis
```

---

## Search index

A flat list of all wiki pages with keywords for primitive search.
Each entry maps a page path to the concepts it covers.

```yaml
pages:
  - path: wiki/brain_regions/anterior_cingulate_cortex.md
    keywords: [anterior cingulate cortex, ACC, model-based reinforcement learning, state prediction, action-outcome learning, goal-directed behaviour, calcium imaging, optogenetics, mice, two-step task, state representation]
  - path: wiki/brain_regions/prefrontal_cortex.md
    keywords: [prefrontal cortex, PFC, executive function, attractor networks, belief updating, schizophrenia, mPFC, agranular cortex, projection neurons, IT, PT, CT, interneurons, prospective coding, successor representation, STDP]
  - path: wiki/brain_regions/medial_prefrontal_cortex.md
    keywords: [medial prefrontal cortex, mPFC, agranular cortex, prelimbic, infralimbic, ACC, projection neurons, IT, PT, CT, interneurons, PV, SOM, CCK, NDNF, VIP, thalamus, amygdala, hippocampus, reciprocal loops, working memory, emotion]
  - path: wiki/brain_regions/infralimbic_cortex.md
    keywords: [infralimbic cortex, IL, mPFC, prefrontal, emotion, motivation, extinction, ventral hippocampus, amygdala]
  - path: wiki/brain_regions/basolateral_amygdala.md
    keywords: [basolateral amygdala, BLA, amygdala, emotional learning, fear, mPFC, prefrontal, reciprocal loops, L2, cortico-amygdalar]
  - path: wiki/brain_regions/mediodorsal_thalamus.md
    keywords: [mediodorsal thalamus, MD, thalamus, working memory, attention, mPFC, prefrontal, L3, IT, PV, SOM, VIP, reciprocal]
  - path: wiki/brain_regions/ventromedial_thalamus.md
    keywords: [ventromedial thalamus, VM, thalamus, arousal, cortical state, mPFC, prefrontal, L5, PT, apical dendrites, NDNF, Ca2+ spikes]
  - path: wiki/brain_regions/ventral_hippocampus.md
    keywords: [ventral hippocampus, vHPC, hippocampus, emotion, context, mPFC, prefrontal, IL, L5, IT, CCK, endocannabinoid]
  - path: wiki/brain_regions/zona_incerta.md
    keywords: [zona incerta, ZI, ZIm, ZIr, TAC1, GABAergic, novelty seeking, investigatory behavior, PAG, prefrontal cortex]
  - path: wiki/brain_regions/periaqueductal_gray.md
    keywords: [periaqueductal gray, PAG, defensive behavior, investigatory behavior, ZI, disinhibition, gating, deep investigation]
  - path: wiki/brain_regions/prelimbic_cortex.md
    keywords: [prelimbic cortex, PL, prefrontal cortex, ZI, investigatory behavior, novelty seeking]
  - path: wiki/brain_regions/primary_auditory_cortex.md
    keywords: [primary auditory cortex, A1, auditory processing, schizophrenia, MMN, ASSR, synaptic gain, disinhibition]
  - path: wiki/brain_regions/inferior_frontal_gyrus.md
    keywords: [inferior frontal gyrus, IFG, Broca area, schizophrenia, DCM, synaptic gain, auditory processing]
  - path: wiki/brain_regions/superior_temporal_gyrus.md
    keywords: [superior temporal gyrus, STG, auditory cortex, schizophrenia, psychosis, hallucinations]
  - path: wiki/behaviours/five_choice_serial_reaction_time_task.md
    keywords: [5-CSRTT, five choice serial reaction time task, sustained attention, impulsivity, atomoxetine, operant behavior, mouse, pharmacological validation]
  - path: wiki/behaviours/five_choice_serial_reaction_time_task.md
    keywords: [5-CSRTT, five choice serial reaction time task, sustained attention, impulsivity, atomoxetine, operant behavior, mouse, pharmacological validation]
  - path: wiki/behaviours/auditory_steady_state_response.md
    keywords: [auditory steady state response, ASSR, 40-Hz, gamma oscillations, schizophrenia, synaptic gain, DCM, biomarker]
  - path: wiki/behaviours/belief_updating.md
    keywords: [belief updating, probabilistic inference, decision making, HGF, beads task]
  - path: wiki/behaviours/hallucinations.md
    keywords: [hallucinations, auditory hallucinations, psychosis, schizophrenia, auditory perceptual abnormalities, disinhibition]
  - path: wiki/behaviours/mismatch_negativity.md
    keywords: [mismatch negativity, MMN, auditory processing, schizophrenia, synaptic gain, DCM, biomarker, prediction error]
  - path: wiki/behaviours/cognitive_impairment.md
    keywords: [cognitive impairment, IQ, working memory, schizophrenia, computational psychiatry]
  - path: wiki/behaviours/mood_disorders.md
    keywords: [mood disorders, depression, bipolar, belief updating, attractor networks, state dependent]
  - path: wiki/behaviours/novelty_seeking.md
    keywords: [novelty seeking, curiosity, exploration, ZI, TAC1, PAG, investigation, deep investigation]
  - path: wiki/behaviours/investigatory_behavior.md
    keywords: [investigatory behavior, deep investigation, shallow investigation, HMM, novelty seeking, ZI, PAG]
  - path: wiki/behaviours/planning.md
    keywords: [planning, prospective, mental simulation, forward search, model-based]
  - path: wiki/behaviours/event_segmentation.md
    keywords: [event segmentation, temporal community structure, prediction error, surprise, sequence learning, mPFC, IFG, statistical learning]
  - path: wiki/behaviours/psychosis.md
    keywords: [psychosis, positive symptoms, schizophrenia, disinhibition, synaptic gain, DCM]
  - path: wiki/behaviours/hallucinations.md
    keywords: [hallucinations, auditory hallucinations, psychosis, schizophrenia, auditory perceptual abnormalities, disinhibition]
  - path: wiki/behaviours/mismatch_negativity.md
    keywords: [mismatch negativity, MMN, auditory processing, schizophrenia, synaptic gain, DCM, biomarker, prediction error]
  - path: wiki/behaviours/auditory_steady_state_response.md
    keywords: [auditory steady state response, ASSR, 40-Hz, gamma oscillations, schizophrenia, synaptic gain, DCM, biomarker]
  - path: wiki/behaviours/cognitive_map.md
    keywords: [cognitive map, spatial navigation, hippocampus, O'Keefe, Nadel, place cells, allocentric, schema, memory consolidation]
  - path: wiki/behaviours/memory_consolidation.md
    keywords: [memory consolidation, systems consolidation, sleep, replay, reactivation, hippocampus, neocortex, long-term memory]
  - path: wiki/behaviours/schema_learning.md
    keywords: [schema, schema learning, prior knowledge, Bartlett, Tse, Harlow, learning set, memory consolidation, rapid learning]
  - path: wiki/behaviours/spatial_navigation.md
    keywords: [spatial navigation, allocentric navigation, cognitive map, maze learning, place learning, reference memory, working memory, hippocampus]
  - path: wiki/behaviours/two_step_task.md
    keywords: [two-step task, model-based, model-free, stay probability, transition, Daw task]
  - path: wiki/behaviours/hippocampal_replay.md
    keywords: [hippocampal replay, replay, sharp-wave ripples, SWR, place cells, memory consolidation, forward replay, reverse replay, awake replay, sleep replay]
  - path: wiki/behaviours/reverse_replay.md
    keywords: [reverse replay, hippocampal replay, sharp-wave ripples, SWR, reward modulation, temporal credit assignment, reinforcement learning, memory consolidation, dopamine]
  - path: wiki/behaviours/forward_replay.md
    keywords: [forward replay, hippocampal replay, sharp-wave ripples, SWR, planning, prospective memory, memory retrieval, reward-insensitive, model-based RL]
  - path: wiki/behaviours/sharp_wave_ripples.md
    keywords: [sharp-wave ripples, SWR, hippocampus, CA1, replay, memory consolidation, high-frequency oscillations, 150-250 Hz, reward modulation]
  - path: wiki/behaviours/place_cells.md
    keywords: [place cells, hippocampus, CA1, place fields, spatial representation, cognitive map, sequence replay, theta phase precession]
  - path: wiki/behaviours/reward_processing.md
    keywords: [reward processing, hippocampus, reward magnitude, adaptive coding, reward prediction error, reverse replay, dopamine, VTA]
  - path: wiki/behaviours/conditioning.md
    keywords: [conditioning, classical conditioning, associative learning, Pavlov, Rescorla-Wagner, blocking, secondary conditioning, prediction error, dopamine, TD learning, reward prediction]
  - path: wiki/methods/computational_psychiatry.md
    keywords: [computational psychiatry, psychiatric phenotyping, model-based analysis, schizophrenia, mental health]
  - path: wiki/methods/dynamic_causal_modelling.md
    keywords: [dynamic causal modelling, DCM, neural mass model, effective connectivity, Bayesian, PEB, schizophrenia]
  - path: wiki/methods/parametric_empirical_bayes.md
    keywords: [parametric empirical bayes, PEB, DCM, group analysis, hierarchical Bayesian, random effects]
  - path: wiki/methods/state_vs_trait.md
    keywords: [state vs trait, mood disorders, schizophrenia, longitudinal, computational psychiatry]
  - path: wiki/methods/pycontrol.md
    keywords: [pycontrol, pyControl, open-source, behavioral control, MicroPython, microcontroller, state machine, timing accuracy, high-throughput]
  - path: wiki/methods/high_throughput_behavioral_testing.md
    keywords: [high-throughput, behavioral testing, parallel experiments, scalability, pyControl]
  - path: wiki/methods/pycontrol.md
    keywords: [pycontrol, pyControl, open-source, behavioral control, MicroPython, microcontroller, state machine, timing accuracy, high-throughput, sub-millisecond latency]
  - path: wiki/methods/high_throughput_behavioral_testing.md
    keywords: [high-throughput, behavioral testing, parallel experiments, scalability, pyControl]
  - path: wiki/methods/computational_modeling.md
    keywords: [computational modeling, logistic regression, statistical correction, model comparison, behavioral analysis, two-step task]
  - path: wiki/methods/gap_junction_recordings.md
    keywords: [gap junction, gap-FRAP, FRAP, dye coupling, patch clamp, connexin, electrical coupling, metabolic coupling, sulforhodamine 101, carbenoxolone, coupling strength]
  - path: wiki/methods/dynamic_causal_modelling.md
    keywords: [dynamic causal modelling, DCM, neural mass model, effective connectivity, Bayesian, PEB, schizophrenia, synaptic gain]
  - path: wiki/methods/parametric_empirical_bayes.md
    keywords: [parametric empirical bayes, PEB, DCM, group analysis, hierarchical Bayesian, random effects]
  - path: wiki/computational_frameworks/extended_finite_state_machine.md
    keywords: [extended finite state machine, state machine, task formalism, pyControl, behavioral control, states, events, timers]
  - path: wiki/computational_frameworks/extended_finite_state_machine.md
    keywords: [extended finite state machine, state machine, task formalism, behavioral control, states, events, timers, pyControl]
  - path: wiki/computational_frameworks/cortical_microcircuit.md
    keywords: [cortical microcircuit, neural mass model, synaptic gain, pyramidal cells, interneurons, DCM, schizophrenia, excitation-inhibition balance]
  - path: wiki/brain_regions/primary_auditory_cortex.md
    keywords: [primary auditory cortex, A1, auditory processing, schizophrenia, MMN, ASSR, synaptic gain, disinhibition]
  - path: wiki/brain_regions/inferior_frontal_gyrus.md
    keywords: [inferior frontal gyrus, IFG, Broca area, schizophrenia, DCM, synaptic gain, auditory processing]
  - path: wiki/brain_regions/superior_temporal_gyrus.md
    keywords: [superior temporal gyrus, STG, auditory cortex, schizophrenia, psychosis, hallucinations]
  - path: wiki/behaviours/mismatch_negativity.md
    keywords: [mismatch negativity, MMN, auditory processing, schizophrenia, synaptic gain, DCM, biomarker, prediction error]
  - path: wiki/behaviours/auditory_steady_state_response.md
    keywords: [auditory steady state response, ASSR, 40-Hz, gamma oscillations, schizophrenia, synaptic gain, DCM, biomarker]
  - path: wiki/behaviours/psychosis.md
    keywords: [psychosis, positive symptoms, schizophrenia, disinhibition, synaptic gain, DCM]
  - path: wiki/behaviours/hallucinations.md
    keywords: [hallucinations, auditory hallucinations, psychosis, schizophrenia, auditory perceptual abnormalities, disinhibition]
  - path: wiki/computational_frameworks/successor_representation.md
    keywords: [successor representation, SR, model-based RL, reinforcement learning, state representation, vector-valued prediction error, dimensionality problem, efficiency-flexibility tradeoff, reward devaluation, transition revaluation, predictive map]
  - path: wiki/computational_frameworks/temporal_difference_learning.md
    keywords: [temporal difference learning, TD learning, prediction error, dopamine, reinforcement learning, classical conditioning, blocking, secondary conditioning, Rescorla-Wagner, Sutton, Barto, midbrain]
  - path: wiki/computational_frameworks/deep_reinforcement_learning.md
    keywords: [deep reinforcement learning, deep RL, deep learning, neural networks, emergent phenomena, reward-shaped representations, experience replay, meta-learning, distributional RL, sample efficiency, biological plausibility, backpropagation]
  - path: wiki/computational_frameworks/meta_reinforcement_learning.md
    keywords: [meta-reinforcement learning, meta-RL, fast adaptation, recurrent networks, learning to learn, prefrontal cortex, dopamine, working memory, in-context learning, activation dynamics, Wang 2018]
  - path: wiki/computational_frameworks/distributional_rl.md
    keywords: [distributional reinforcement learning, distributional RL, dopamine, reward prediction error, quantile, pessimistic, optimistic, population coding, risk, uncertainty, distributional dopamine hypothesis, Dabney 2020]
  - path: wiki/computational_frameworks/experience_replay.md
    keywords: [experience replay, replay, memory consolidation, hippocampal replay, prioritized replay, deep RL, learning efficiency, sleep, sharp-wave ripples, off-policy learning, DQN]
  - path: wiki/computational_frameworks/hierarchical_rl.md
    keywords: [hierarchical reinforcement learning, hierarchical RL, options, temporal abstraction, prefrontal cortex, cognitive control, automatic processing, controlled processing, cost of control, timescale gradients, Botvinick 2009]
  - path: wiki/brain_regions/striatum.md
    keywords: [striatum, basal ganglia, dopamine, cortico-striatal, reinforcement learning, action selection, habits, ventral striatum, dorsal striatum]
  - path: wiki/methods/optogenetics.md
    keywords: [optogenetics, optogenetic stimulation, channelrhodopsin, causal manipulation, neural circuits, unblocking, dopamine]
  - path: wiki/methods/neuropixels.md
    keywords: [Neuropixels, high-density probes, single-unit recording, silicon probes, intraoperative recording, human electrophysiology, spike sorting, motion correction]
  - path: wiki/methods/kilosort.md
    keywords: [Kilosort, spike sorting, template matching, graph-based clustering, drift correction, GPU acceleration, automated spike sorting]
  - path: wiki/methods/allen_mouse_brain_atlas.md
    keywords: [Allen Mouse Brain Atlas, CCFv3, brain atlas, common coordinate framework, mouse brain, neuroanatomy, image registration, parcellation]
  - path: wiki/brain_regions/ventral_tegmental_area.md
    keywords: [ventral tegmental area, VTA, dopamine, dopaminergic neurons, reward prediction error, RPE, surprise signal, hippocampus, model-based RL, reinforcement learning, successor representation, vector-valued prediction error, stimulus-stimulus learning, TD learning, prediction error, midbrain]
  - path: wiki/brain_regions/substantia_nigra.md
    keywords: [substantia nigra, SNc, pars compacta, dopamine, dopaminergic neurons, prediction error, dorsal striatum, reinforcement learning, TD learning, midbrain, action selection]
  - path: wiki/brain_regions/medial_entorhinal_cortex.md
    keywords: [medial entorhinal cortex, MEC, grid cells, entorhinal, spatial navigation, cognitive map, goal learning, field attraction, flickering, local remapping, memory consolidation]
  - path: wiki/brain_regions/retrosplenial_cortex.md
    keywords: [retrosplenial cortex, RSC, spatial memory, navigation, episodic memory, autobiographical memory, allocentric, egocentric, reference frame translation, head-direction cells, scene construction, default mode network, Alzheimer's disease]
  - path: wiki/brain_regions/dorsolateral_entorhinal_cortex.md
    keywords: [dorsolateral entorhinal cortex, dorsolateral band, entorhinal cortex, spatial memory, visuospatial input, postrhinal cortex, dorsal hippocampus, Morris water maze]
  - path: wiki/brain_regions/ventromedial_entorhinal_cortex.md
    keywords: [ventromedial entorhinal cortex, ventromedial band, entorhinal cortex, defensive behavior, elevated plus maze, ventral hippocampus, emotion]
  - path: wiki/behaviours/detours.md
    keywords: [detours, detour problem, spatial navigation, prefrontal cortex, hippocampus, route planning, model-based RL, prediction error, subgoal generation, frontopolar cortex, lateral PFC]
  - path: wiki/behaviours/hippocampal_replay.md
    keywords: [hippocampal replay, replay, sharp-wave ripples, SWR, place cells, memory consolidation, forward replay, reverse replay, awake replay, sleep replay]
  - path: wiki/behaviours/reverse_replay.md
    keywords: [reverse replay, hippocampal replay, sharp-wave ripples, SWR, reward modulation, temporal credit assignment, reinforcement learning, memory consolidation, dopamine]
  - path: wiki/behaviours/forward_replay.md
    keywords: [forward replay, hippocampal replay, sharp-wave ripples, SWR, planning, prospective memory, memory retrieval, reward-insensitive, model-based RL]
  - path: wiki/behaviours/sharp_wave_ripples.md
    keywords: [sharp-wave ripples, SWR, hippocampus, CA1, replay, memory consolidation, high-frequency oscillations, 150-250 Hz, reward modulation]
  - path: wiki/behaviours/place_cells.md
    keywords: [place cells, hippocampus, CA1, place fields, spatial representation, cognitive map, sequence replay, theta phase precession, successor representation, predictive map]
  - path: wiki/behaviours/grid_cells.md
    keywords: [grid cells, entorhinal cortex, MEC, spatial navigation, cognitive map, hexagonal firing, goal learning, field attraction, attractor networks, remapping, flickering]
  - path: wiki/behaviours/reward_processing.md
    keywords: [reward processing, hippocampus, reward magnitude, adaptive coding, reward prediction error, reverse replay, dopamine, VTA]
  - path: wiki/computational_frameworks/temporal_credit_assignment.md
    keywords: [temporal credit assignment, reinforcement learning, RL, reverse replay, hippocampus, reward propagation, eligibility trace, dopamine, VTA, memory consolidation]
  - path: wiki/computational_frameworks/anccr.md
    keywords: [ANCCR, Adjusted Net Contingency for Causal Relations, retrospective causal inference, dopamine, nucleus accumbens, reward learning, conditioning, TDRL alternative, mesolimbic]
  - path: wiki/behaviours/planning.md
    keywords: [planning, prospective, mental simulation, forward search, model-based, meta-RL, active inference, policy rollouts, iterative refinement, thinking time]
  - path: wiki/behaviours/hippocampal_replay.md
    keywords: [hippocampal replay, replay, sharp-wave ripples, SWR, place cells, memory consolidation, forward replay, reverse replay, awake replay, sleep replay, prefrontal coordination, mPFC replay, iterative refinement]
  - path: wiki/behaviours/forward_replay.md
    keywords: [forward replay, hippocampal replay, sharp-wave ripples, SWR, planning, prospective memory, memory retrieval, reward-insensitive, model-based RL, meta-RL, policy rollouts, mPFC replay]
  - path: wiki/behaviours/sharp_wave_ripples.md
    keywords: [sharp-wave ripples, SWR, hippocampus, CA1, replay, memory consolidation, high-frequency oscillations, 150-250 Hz, reward modulation, prefrontal coordination, PFC excitation, PFC inhibition]
  - path: wiki/computational_frameworks/meta_reinforcement_learning.md
    keywords: [meta-reinforcement learning, meta-RL, fast adaptation, recurrent networks, learning to learn, prefrontal cortex, dopamine, working memory, in-context learning, activation dynamics, policy rollouts, planning, iterative refinement]
  - path: wiki/computational_frameworks/active_inference.md
    keywords: [active inference, free energy principle, epistemic value, novelty, salience, spatial navigation, planning, exploration-exploitation, expected free energy, path cells, place cells, theta-gamma coupling]
  - path: wiki/brain_regions/medial_prefrontal_cortex.md
    keywords: [medial prefrontal cortex, mPFC, prelimbic, infralimbic, agranular cortex, hippocampal coordination, SWR modulation, replay, awake replay, rule switching, generalized spatial code, trajectory-independent coding]
  - path: wiki/brain_regions/ventral_striatum.md
    keywords: [ventral striatum, nucleus accumbens, NAcc, dopamine, prediction error, ANCCR, reward learning, causal inference, retrospective association, TDRL, conditioning]
  - path: wiki/computational_frameworks/temporal_difference_learning.md
    keywords: [temporal difference learning, TD learning, prediction error, dopamine, reinforcement learning, classical conditioning, blocking, secondary conditioning, Rescorla-Wagner, Sutton, Barto, midbrain, ANCCR challenge]
  - path: wiki/brain_regions/entorhinal_cortex.md
    keywords: [entorhinal cortex, EC, relational structure, reinforcement learning, cognitive map, remapping, fMRI, RSA, structure representation, generalization]
  - path: wiki/brain_regions/ventromedial_prefrontal_cortex.md
    keywords: [ventromedial prefrontal cortex, vmPFC, prediction error, reinforcement learning, value, fMRI, structure, credit assignment, HRF]
  - path: wiki/brain_regions/ventral_striatum.md
    keywords: [ventral striatum, vStr, nucleus accumbens, prediction error, reinforcement learning, reward, fMRI, structure, credit assignment]
  - path: wiki/brain_regions/posterior_cingulate_cortex.md
    keywords: [posterior cingulate cortex, PCC, prediction error, structure, reinforcement learning, fMRI, grid cells, schema]
  - path: wiki/behaviours/reinforcement_learning.md
    keywords: [reinforcement learning, RL, structure learning, generalization, relational structure, credit assignment, prediction error, learning set]
  - path: wiki/methods/fmri.md
    keywords: [fMRI, functional magnetic resonance imaging, hemodynamic response function, HRF, neuroimaging, prediction error, vmPFC]
  - path: wiki/brain_regions/medial_temporal_lobe.md
    keywords: [medial temporal lobe, MTL, entorhinal cortex, subiculum, hippocampus, memory consolidation, cognitive map, concrete representations, graph learning]
  - path: wiki/computational_frameworks/factorised_representations.md
    keywords: [factorised representations, factorization, Tolman-Eichenbaum Machine, mPFC, abstract relational map, cross-graph transfer, generalisation]
  - path: wiki/computational_frameworks/tolman_eichenbaum_machine.md
    keywords: [Tolman-Eichenbaum Machine, TEM, cognitive map, factorisation, relational structure, entorhinal cortex, hippocampus]
  - path: wiki/methods/representational_similarity_analysis.md
    keywords: [representational similarity analysis, RSA, RDM, computational modeling, fMRI, mPFC, abstract map]
  - path: wiki/methods/fmri_repetition_suppression.md
    keywords: [fMRI repetition suppression, repetition suppression, fMRI, mPFC, MTL, memory consolidation, abstract representation]
  - path: wiki/brain_regions/frontal_eye_field.md
    keywords: [frontal eye field, FEF, prefrontal cortex, PFC, spatial attention, temporal expectation, mixed selectivity, multiplexing, neural manifold, dPCA, reaction time, attentional focus]
  - path: wiki/computational_frameworks/mixed_selectivity.md
    keywords: [mixed selectivity, neural coding, population coding, prefrontal cortex, PFC, dimensionality, orthogonal coding, non-orthogonal coding, multiplexing]
  - path: wiki/computational_frameworks/neural_manifold.md
    keywords: [neural manifold, low-dimensional manifold, population geometry, dimensionality reduction, dPCA, neural dynamics, component orthogonality, representational overlap]
  - path: wiki/behaviours/temporal_expectation.md
    keywords: [temporal expectation, predictive timing, cue-to-target onset asynchrony, CTOA, attention, reaction time, FEF, prefrontal cortex]
  - path: wiki/computational_frameworks/model_based_rl.md
    keywords: [model-based RL, model-based reinforcement learning, planning, prospective planning, internal model, world model, value iteration, successor representation, SR, efficiency-flexibility tradeoff, hybrid systems]
  - path: wiki/computational_frameworks/model_free_rl.md
    keywords: [model-free RL, model-free reinforcement learning, cached values, TD learning, habitual, stimulus-response, successor representation, SR, efficiency-flexibility tradeoff]
  - path: wiki/brain_regions/hippocampus_ca3.md
    keywords: [hippocampus CA3, CA3, auto-associative network, attractor dynamics, reverse replay, symmetric STDP, spike-timing-dependent plasticity, pattern completion, preplay, place cells]
  - path: wiki/computational_frameworks/deep_reinforcement_learning.md
    keywords: [deep reinforcement learning, deep RL, deep learning, neural networks, emergent phenomena, reward-shaped representations, experience replay, meta-learning, distributional RL, sample efficiency, biological plausibility]
  - path: wiki/computational_frameworks/meta_reinforcement_learning.md
    keywords: [meta-reinforcement learning, meta-RL, fast adaptation, recurrent networks, learning to learn, prefrontal cortex, dopamine, working memory, in-context learning, activation dynamics]
  - path: wiki/computational_frameworks/distributional_rl.md
    keywords: [distributional reinforcement learning, distributional RL, dopamine, reward prediction error, quantile, pessimistic, optimistic, population coding, risk, uncertainty, distributional dopamine hypothesis]
  - path: wiki/computational_frameworks/experience_replay.md
    keywords: [experience replay, replay, memory consolidation, hippocampal replay, prioritized replay, deep RL, learning efficiency, sleep, sharp-wave ripples, off-policy learning]
  - path: wiki/computational_frameworks/hierarchical_rl.md
    keywords: [hierarchical reinforcement learning, hierarchical RL, options, temporal abstraction, prefrontal cortex, cognitive control, automatic processing, controlled processing, cost of control, timescale gradients]
  - path: wiki/behaviours/path_integration.md
    keywords: [path integration, dead reckoning, velocity integration, grid cells, entorhinal cortex, continuous attractor networks, spatial navigation, self-motion]
  - path: wiki/computational_frameworks/residue_number_system.md
    keywords: [residue number system, RNS, modulo code, grid cells, position encoding, carry-free arithmetic, combinatorial capacity, entorhinal cortex, path integration]
  - path: wiki/brain_regions/head_direction_circuit.md
    keywords: [head direction circuit, ring attractor, anterior dorsal nucleus, ADn, thalamus, spatial navigation, continuous attractor, bump attractor]
  - path: wiki/brain_regions/brainstem_oculomotor_integrator.md
    keywords: [oculomotor integrator, line attractor, brainstem, nucleus prepositus hypoglossi, medial vestibular nucleus, eye position, continuous attractor]
  - path: wiki/brain_regions/anterior_lateral_motor_cortex.md
    keywords: [anterior lateral motor cortex, ALM, premotor cortex, discrete attractor, bistability, motor planning, working memory, perturbation]
  - path: wiki/brain_regions/orbitofrontal_cortex.md
    keywords: [orbitofrontal cortex, OFC, value encoding, cognitive map, model-based RL, theta oscillations, hippocampal interaction, reward learning, state-value computation]
  - path: wiki/brain_regions/insular_cortex.md
    keywords: [insular cortex, IC, insula, incentive learning, goal-directed action, reward devaluation, gustatory cortex, motivational control, specific satiety]
  - path: wiki/brain_regions/astrocytes.md
    keywords: [astrocytes, gap junctions, connexin 43, connexin 30, metabolic networks, glucose, lactate, hippocampus, synaptic transmission, neuroglial interaction, gliotransmission]
  - path: wiki/brain_regions/cerebellum.md
    keywords: [cerebellum, Bergmann glial cells, gap junctions, electrical coupling, Purkinje cells, molecular layer, parallel fibers, glutamate receptors, calcium signaling]
  ```
  - path: wiki/behaviours/learning.md
    keywords: [learning, spatial learning, asymptotic performance, learning stages, retrosplenial cortex, goal-directed navigation, ConSink, experience-dependent plasticity]
  - path: wiki/computational_frameworks/compositionality.md
    keywords: [compositionality, predictive object representations, PORs, cognitive map, medial entorhinal cortex, MEC, object vector cells, grid cells, basis functions, eigenvectors, local remapping, efficient planning]
  - path: wiki/behaviours/learning.md
    keywords: [learning, spatial learning, asymptotic performance, learning stages, retrosplenial cortex, goal-directed navigation, ConSink, experience-dependent plasticity, training]
  - path: wiki/computational_frameworks/compositionality.md
    keywords: [compositionality, predictive object representations, PORs, cognitive map, medial entorhinal cortex, MEC, object vector cells, grid cells, basis functions, eigenvectors, local remapping, efficient planning, Woodbury identity]
  - path: wiki/brain_regions/mid_dlpfc.md
    keywords: [mid-DLPFC, dorsolateral prefrontal cortex, areas 45/46, hierarchical cognitive control, apex of frontal hierarchy, effective connectivity, dynamic causal modelling]
  - path: wiki/brain_regions/rostrolateral_prefrontal_cortex.md
    keywords: [RLPFC, rostrolateral prefrontal cortex, lateral frontopolar cortex, area 10, schematic control, sequential task control, schema-based knowledge, hippocampal interaction]
  - path: wiki/brain_regions/dorsolateral_prefrontal_cortex.md
    keywords: [dorsolateral prefrontal cortex, DLPFC, option representations, hierarchical RL, working memory, cognitive control, task sets, executive function]
  - path: wiki/brain_regions/dorsolateral_striatum.md
    keywords: [dorsolateral striatum, DLS, model-free RL, TD learning, punctate states, procedural decision making, task bracketing, habits, option-specific policies]
  - path: wiki/brain_regions/dorsomedial_striatum.md
    keywords: [dorsomedial striatum, DMS, successor representation, SR-based value, reward devaluation, deliberation, ventral striatum]
  - path: wiki/brain_regions/presupplementary_motor_area.md
    keywords: [pre-SMA, pre-supplementary motor area, sequential task control, RLPFC, medial frontal hierarchy, motivational signals]
  - path: wiki/behaviours/hierarchical_cognitive_control.md
    keywords: [hierarchical cognitive control, policy abstraction, frontal cortex, three-zone model, rostrocaudal organization, working memory gating]
  - path: wiki/behaviours/vicarious_trial_error.md
    keywords: [VTE, vicarious trial and error, deliberative decision making, hippocampal theta sequences, cognitive map, pause-and-look]
  - path: wiki/computational_frameworks/hierarchical_control_architecture.md
    keywords: [hierarchical control architecture, frontal hierarchy, three zones, mid-DLPFC apex, RLPFC schematic control, corticostriatal gating]
  - path: wiki/computational_frameworks/corticostriatal_gating.md
    keywords: [corticostriatal gating, working memory gating, frontostriatal loops, input gating, output gating, hierarchical control, striatum]
  - path: wiki/computational_frameworks/homeostatic_plasticity.md
    keywords: [homeostatic plasticity, synaptic scaling, presynaptic homeostasis, intrinsic excitability, set point, RIM, dysbindin, schizophrenia, autism, fragile X, TOR, S6K]
  - path: wiki/brain_regions/lateral_entorhinal_cortex.md
    keywords: [lateral entorhinal cortex, LEC, entorhinal cortex, goal-directed navigation, reward-vector coding, CA1 input, goal-biased representations, spatial navigation]
  - path: wiki/brain_regions/anterior_prefrontal_cortex.md
    keywords: [anterior prefrontal cortex, antPFC, frontopolar cortex, BA 10, successor representation, predictive horizons, hierarchical planning, spatial navigation, goal-directed navigation]
  - path: wiki/brain_regions/nucleus_accumbens.md
    keywords: [nucleus accumbens, NAc, ventral striatum, D1-MSN, temporal difference learning, dopamine, TD error, gamma, reward prediction error]
  - path: wiki/behaviours/categorization.md
    keywords: [categorization, rule-based categorization, visual categorization, generalization, category-selective neurons, mPFC, abstract representation, cognitive flexibility]
  - path: wiki/behaviours/epilepsy.md
    keywords: [epilepsy, seizures, Dravet syndrome, SCN1A, cannabidiol, CBD, cannabigerolic acid, CBGA, clobazam, GABAA receptor, GPR55, TRPV1, anticonvulsant, proconvulsant, SUDEP]
  - path: wiki/behaviours/design_fluency.md
    keywords: [design fluency, verbal fluency, frontal lobe, temporal lobe, lateralisation, generativity, nonsense drawings, neuropsychological dissociation, executive function]
  - path: wiki/behaviours/effort_based_decision_making.md
    keywords: [effort-based decision making, anterior cingulate cortex, ACC, barrier T-maze, action selection, cost-benefit evaluation, goal-directed behavior, optogenetics]
  - path: wiki/behaviours/hunting_behavior.md
    keywords: [hunting behavior, predatory behavior, striped field mouse, behavioral complexity, data compression, ethogram, behavioral stereotypy]
  - path: wiki/behaviours/locomotion.md
    keywords: [locomotion, hindlimb locomotion, spinal cord injury, motor recovery, central pattern generator, gait analysis]
  - path: wiki/behaviours/theta_sequences.md
    keywords: [theta sequences, hippocampal theta, phase precession, prospective coding, deliberation, planning]
  - path: wiki/behaviours/non_local_representation.md
    keywords: [non-local representation, prospective coding, theta phase, replay content, hippocampal-prefrontal interaction]
  - path: wiki/behaviours/semantic_memory.md
    keywords: [semantic memory, concept cells, medial temporal lobe, multimodal representation, associative encoding]
  - path: wiki/behaviours/working_memory.md
    keywords: [working memory, persistent activity, medial temporal lobe, medial frontal cortex, phase coding, multiplexing]
  - path: wiki/methods/closed_loop_optogenetics.md
    keywords: [closed-loop optogenetics, real-time decoding, brain-machine interface, content-specific manipulation, ArchT]
  - path: wiki/computational_frameworks/central_pattern_generator.md
    keywords: [central pattern generator, spinal cord, locomotion, rhythmic activity, autonomous dynamics]
  - path: wiki/computational_frameworks/permissive_vs_instructive_roles.md
    keywords: [permissive roles, instructive roles, circuit manipulation, off-target effects, diaschisis, homeostatic recovery]
  - path: wiki/computational_frameworks/take_the_best_heuristic.md
    keywords: [take-the-best heuristic, decision strategy, hierarchical decision-making, strategy selection]
  - path: wiki/computational_frameworks/content_specific_consolidation.md
    keywords: [content-specific consolidation, selective memory, replay content, closed-loop manipulation]
  - path: wiki/computational_frameworks/brain_machine_interface.md
    keywords: [brain-machine interface, closed-loop control, real-time decoding, memory modulation]
  - path: wiki/behaviours/hunting_behavior.md
    keywords: [hunting behavior, predatory behavior, striped field mouse, behavioral complexity, data compression, ethogram, behavioral stereotypy]
  - path: wiki/behaviours/locomotion.md
    keywords: [locomotion, hindlimb locomotion, spinal cord injury, motor recovery, central pattern generator, gait analysis]
  - path: wiki/behaviours/theta_sequences.md
    keywords: [theta sequences, hippocampal theta, phase precession, prospective coding, deliberation, planning]
  - path: wiki/behaviours/non_local_representation.md
    keywords: [non-local representation, prospective coding, theta phase, replay content, hippocampal-prefrontal interaction]
  - path: wiki/behaviours/semantic_memory.md
    keywords: [semantic memory, concept cells, medial temporal lobe, multimodal representation, associative encoding]
  - path: wiki/behaviours/working_memory.md
    keywords: [working memory, persistent activity, medial temporal lobe, medial frontal cortex, phase coding, multiplexing]
  - path: wiki/behaviours/theta_cycle_skipping.md
    keywords: [theta cycle skipping, theta oscillations, mPFC, predictive coding, burst firing]
  - path: wiki/methods/closed_loop_optogenetics.md
    keywords: [closed-loop optogenetics, real-time decoding, brain-machine interface, content-specific manipulation, ArchT]
  - path: wiki/computational_frameworks/central_pattern_generator.md
    keywords: [central pattern generator, spinal cord, locomotion, rhythmic activity, autonomous dynamics]
  - path: wiki/computational_frameworks/permissive_vs_instructive_roles.md
    keywords: [permissive roles, instructive roles, circuit manipulation, off-target effects, diaschisis, homeostatic recovery]
  - path: wiki/computational_frameworks/take_the_best_heuristic.md
    keywords: [take-the-best heuristic, decision strategy, hierarchical decision-making, strategy selection]
  - path: wiki/computational_frameworks/content_specific_consolidation.md
    keywords: [content-specific consolidation, selective memory, replay content, closed-loop manipulation]
  - path: wiki/computational_frameworks/brain_machine_interface.md
    keywords: [brain-machine interface, closed-loop control, real-time decoding, memory modulation]
   - path: wiki/behaviours/object_location_memory.md
     keywords: [object location memory, object memory, spatial memory, hippocampus, cognitive map, object identity, location coding, ensemble coding]
    - path: wiki/behaviours/obsessive_compulsive_disorder.md
      keywords: [obsessive-compulsive disorder, OCD, computational psychiatry, model-based RL, model-free RL, meta-controller, frontostriatal loops, indecisiveness, confidence, dmPFC, dACC]
    - path: wiki/computational_frameworks/plan_until_habit.md
      keywords: [plan-until-habit, depth-limited planning, model-based RL, model-free RL, hybrid RL, cognitive resources, time pressure, decision-making spectrum]
    - path: wiki/computational_frameworks/structural_form_discovery.md
      keywords: [structural form discovery, graph grammars, Bayesian structure learning, hierarchical generative model, unsupervised learning, cognitive development, inductive inference]
    - path: wiki/behaviours/hunting_behavior.md
      keywords: [hunting behavior, predatory behavior, striped field mouse, behavioral complexity, data compression, ethogram, behavioral stereotypy, Apodemus agrarius]
    - path: wiki/behaviours/monkey_pacman_strategy.md
      keywords: [monkey Pac-Man, compositional strategies, hierarchical decision-making, take-the-best heuristic, reinforcement learning, non-human primate cognition, strategy switching]
    - path: wiki/behaviours/theta_sweeps.md
      keywords: [theta sweeps, hippocampal theta, goal-directed navigation, spatial planning, prospective coding, continuous attractor networks, theta phase precession]
    - path: wiki/behaviours/hippocampal_cortical_interaction.md
      keywords: [hippocampal-cortical interaction, sharp-wave ripples, memory reactivation, prefrontal cortex, theta oscillations, coherent coding, spatial memory]
    - path: wiki/behaviours/hippocampal_inference.md
      keywords: [hippocampal inference, transitive inference, associative inference, relational memory, pattern completion, integrative encoding, memory integration]
    - path: wiki/behaviours/uncertainty_resolution.md
      keywords: [uncertainty resolution, Bayesian decision-making, partial observability, belief updating, entropy, anterior prefrontal cortex, medial prefrontal cortex]
    - path: wiki/brain_regions/thalamus.md
      keywords: [thalamus, thalamocortical loops, anterior lateral motor cortex, ALM, decision-making, task selectivity, tonic excitation, phasic excitation]

---

## Recent Updates (2026-04-05)

### Batch Processing: 30 Summaries

Successfully processed 30 summaries through the fact_finder → router → wiki_writer pipeline:

**Statistics:**
- Total summaries processed: 30
- Total facts extracted: 90
- Total facts routed: 90
- Total facts written: 90
- Facts skipped: 0
- Pages created: 19
- Pages updated: 18

**Key Topics Covered:**
- Orbitofrontal cortex (OFC) and goal-directed navigation
- Hippocampal replay and memory consolidation
- Prefrontal cortex and hierarchical reinforcement learning
- Grid cells and spatial navigation
- Meta-learning and cognitive architecture
- Psychiatric disorders and network dynamics
- Statistical methods and reproducibility
- Deep reinforcement learning advances

**Summaries Processed:**
1. Basu 2021 - OFC maps future navigational goals
2. Basu 2023 - Goal pointer for cognitive map in OFC
3. Bein 2024 - Schemas, RL, and mPFC
4. Bendor 2012 - Biasing hippocampal replay during sleep
5. Benjamin 2018 - Redefine statistical significance
6. Berner 2019 - Dota 2 with large-scale deep RL
7. Beyeler 2019 - Sparse coding and dimensionality reduction
8. Bhattacherjee 2022 - Prefrontal spatial transcriptomics
9. Bialek 2022 - Dimensionality of behavior
10. Binz 2024 - Meta-learned models of cognition
11. Blanco-Pozo 2024 - Dopamine-independent reward effects
12. Bongioanni 2021 - Neural mechanism for novel choice
13. Botvinick 2008 - Hierarchical models of behavior and prefrontal function
14. Botvinick 2009 - Hierarchically organized behavior and neural foundations
15. Botvinick 2009 - Hierarchical behavior and reinforcement learning
16. Botvinick 2019 - Reinforcement learning, fast and slow
17. Bowling 2022 - Settling the reward hypothesis
18. Braun 2018 - From maps to multi-dimensional network mechanisms of mental disorders
19. Carvalho 2021 - FARM for generalizing object-centric behavior
20. Craver 2013 - In search of mechanisms: discoveries across life sciences
21. Dordek 2016 - Extracting grid cell characteristics using non-negative PCA
22. Dorrell 2023 - Actionable neural representations: grid cells from minimal constraints
23. Durstewitz 2020 - Psychiatric illnesses as disorders of network dynamics
24. Fried 2020 - Systems all the way down: embracing complexity in mental health
25. Howes 2022 - Treatment resistance in psychiatry
26. Howes 2016 - Dopamine and the aberrant salience hypothesis of schizophrenia
27. Ivanov 2021 - Why psychotropic drugs don't cure mental illness

