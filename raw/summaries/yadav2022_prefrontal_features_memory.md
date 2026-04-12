---
source_file: "yadav2022_prefrontal_features_memory.md"
paper_id: "yadav2022_prefrontal_features_memory"
title: "Prefrontal feature representations drive memory recall"
authors: "Nakul Yadav, Chelsea Noble, James E. Niemeyer, Andrea Terceros, Jonathan Victor, Conor Liston, Priyamvada Rajasethupathy"
year: 2022
journal: "Nature"
paper_type: "empirical"
contribution_type: "empirical"
species: ["mouse"]
methods: ["calcium_imaging", "optogenetics"]
brain_regions: ["hippocampus", "hippocampus_ca1", "hippocampus_ca3", "entorhinal_cortex", "lateral_entorhinal_cortex", "prefrontal_cortex", "anterior_cingulate_cortex"]
frameworks: ["attractor_networks", "mixed_selectivity", "neural_manifold"]
keywords: ["rajasethupathy_et_al_2015_projections_from_neocortex_mediate_top_down_control_of_memory_retrieval_nature", "tomita_et_al_1999_top_down_signal_from_prefrontal_cortex_in_executive_control_of_memory_retrieval_nature", "oreilly_and_rudy_2001_conjunctive_representations_in_learning_and_memory_psychological_review", "wills_et_al_2005_attractor_dynamics_in_hippocampal_representation_science", "rigotti_et_al_2013_importance_of_mixed_selectivity_in_complex_cognitive_tasks_nature", "mante_et_al_2013_context_dependent_computation_by_recurrent_dynamics_in_prefrontal_cortex_nature", "named_models_or_frameworks", "attractor_network_dynamics_hippocampal_ca3_ca1", "mixed_selectivity_coding_prefrontal_cortex", "pattern_completion_memory_retrieval_from_partial_cues", "marrs_three_levels_of_analysis_implicit_in_mechanistic_approach", "conjunctive_vs_feature_representations_dual_memory_system", "brain_regions", "anterior_cingulate_cortex_ac", "hippocampal_ca1", "lateral_entorhinal_cortex_lec", "hippocampal_ca3", "prefrontal_cortex_general", "keywords", "contextual_memory"]
---

### One-line summary

The anterior cingulate cortex (AC) encodes feature representations that dynamically reorganize during memory retrieval to lead and target recruitment of conjunctive context representations in hippocampal CA1.

---

### Background & motivation

Memory formation involves binding of contextual features into a unitary conjunctive representation in the hippocampus, whereas memory recall can occur using partial combinations of these contextual features. The neurobiological substrates of feature representations have remained unclear—specifically, where individual features are stored in the brain and how they access hippocampal conjunctive representations to drive memory recall. This paper addresses whether feature representations are embedded within hippocampus or laid out in separate or distributed brain areas with targeted access to hippocampal representations.

---

### Methods

- **Behavioural task**: Head-fixed virtual reality memory retrieval task in which mice navigated an endless corridor and experienced three randomly sequenced multi-modal contexts (reward, neutral, aversive), each defined by unique combinations of auditory, visual, olfactory, and texture cues
- **Training phase**: 3 days with 20 s context presentations and paired reinforcement (sucrose for reward, water for neutral, airpuff for aversive); 20% probe trials without reinforcement to assess learning
- **Retrieval phase**: Trials with full (AVOT) or partial features (O, T, AT, AO, OT, AOT) of original contexts presented without reinforcement
- **Imaging**: Longitudinal two-photon calcium imaging (GCaMP6f) of dorsal CA1 and AC in same field of view across training and retrieval; simultaneous dual-region imaging using 2p random access mesoscope
- **Optogenetic inhibition**: Soma-targeted stGtACR2 expressed in AC or LEC with simultaneous CA1 imaging; bilateral optogenetic inhibition during retrieval with behavioural assessment
- **TRAP2 targeting**: Activity-dependent expression of stGtACR2 in feature-coding neurons using TRAP2 mice to specifically inhibit neurons activated during feature presentation
- **Viral tracing**: Retrograde (AAVrg) and anterograde (AAV1) tracing to map AC and LEC projections to CA1
- **Subjects**: Wild-type C57Bl6/J male mice, 6–8 weeks old at start

---

### Key findings

- **CA1 encodes conjunctive, not feature, representations**: During retrieval, CA1 neurons exhibited robust conjunctive responses to all features of a context (9% of neurons) but rarely showed feature-selective responses (1.1% vs. 0.8% chance); population trajectories showed divergence of context-evoked but not feature-evoked trajectories; SVM trained on three features could decode context from a held-out fourth feature with >80% accuracy
- **AC is required for feature-based recall**: Inhibition of AC during retrieval caused significant deficits in feature-based recall across all partial-feature conditions (AOT, OT, AT), whereas LEC inhibition had no effect; AC inhibition specifically suppressed CA1 context-selective neurons without affecting non-context-selective neurons, while LEC inhibition caused broad, non-specific silencing of CA1
- **AC encodes feature representations**: AC neurons exhibited both feature selectivity and mixed selectivity to feature combinations during retrieval (9% conjunctive vs. 22% feature-selective), contrasting with CA1's predominantly conjunctive coding; feature-responsive ensembles in AC showed minimal response to other features of the same or opposite context, unlike CA1's highly overlapping feature ensembles
- **Dynamic AC-CA1 reorganization**: During training, CA1 context ensemble recruitment preceded AC context ensemble recruitment (CA1 mean onset: 10.41s, AC: 16.37s); during retrieval, AC feature ensemble recruitment preceded CA1 context ensemble recruitment (AC: 7.32s, CA1: 13.65s); this temporal reversal was statistically significant (P < 0.0001 for training, P < 0.01 for retrieval)
- **AC-CA1 functional coupling**: Significant correlations between AC feature ensembles and CA1 context ensembles, with stronger correlations for aversive than neutral context (q < 0.05, Friedman test); highly correlated cross-region pairs were predominantly aversive-responsive neurons with more synchronous activity in aversive context
- **Causal role of AC feature neurons**: TRAP2-mediated inhibition of feature-coding neurons (~20% of AC neurons) caused near-complete deficits in feature-based recall that was rescued when inhibition was removed (F(1,25) = 64.39, P < 0.0001), whereas inhibiting an equal-sized random population had no effect (F(1,20) = 0.14, P = 0.71)
- **Emergence of context representations**: Neurons initially responsive to shock (unconditioned stimulus) on early trials became context-selective (conditioned stimulus) on later trials in both AC and CA1 (~60% of CA1 shock neurons, ~30% of AC shock neurons became context neurons)
- **Anatomical segregation**: AC and LEC project to almost entirely separate subsets of CA1 neurons; AC inputs overlap more with FOS+ context neurons in CA1 than LEC inputs (P < 0.01, Welch's t-test)

---

### Computational framework

The paper employs several computational approaches:

**Attractor dynamics**: The paper references attractor dynamics in hippocampal representations (citing Wills et al., 2005) as the mechanism for conjunctive coding in CA1, where recurrent networks merge associated concepts into singular representations.

**Mixed selectivity and high-dimensional coding**: The paper draws on computational frameworks for mixed selectivity in cortex (Rigotti et al., 2013; Mante et al., 2013; Raposo et al., 2014), where single neurons encode multiple task variables, enabling robust population-level feature representations in a high-dimensional neural manifold.

**Pattern completion**: The hippocampal CA3-CA1 network is described as implementing pattern completion through recurrent connectivity, allowing full conjunctive representations to be retrieved from partial feature cues.

**Support Vector Machine (SVM) decoding**: Linear SVMs with 10-fold cross-validation were used to decode context from neural population activity, testing generalization across features.

**State-space analysis**: Singular value decomposition (SVD) was used to project high-dimensional neural activity onto low-dimensional subspaces for visualization of population trajectories.

---

### Prevailing model of the system under study

The prevailing model, as described in the paper's introduction, holds that:

1. **Hippocampal conjunctive coding**: The hippocampus (particularly CA3-CA1) encodes contextual memories as unified conjunctive representations through recurrent networks that merge associated concepts into singular representations. Global conjunctive representations of context are widely reported in hippocampus.

2. **Role of entorhinal cortex**: The lateral entorhinal cortex (LEC) provides the primary cortical input to hippocampus, conveying both conjunctive and feature-like information. LEC is considered a major route for cortical information to access hippocampal representations.

3. **Prefrontal involvement in retrieval**: Prefrontal cortex (particularly anterior cingulate) has been demonstrated to be required for memory retrieval, with identified direct monosynaptic prefrontal-to-hippocampus projections highlighting a top-down role in memory control.

4. **Theoretical frameworks for feature representation**: Where individual features are stored has remained unclear—whether embedded within hippocampus (as feature-selective neurons capable of recruiting contextual responses) or in separate/distributed brain areas with targeted access to hippocampal conjunctive representations.

---

### What this paper contributes

This paper provides the first mechanistic insights into where contextual features are represented, how they emerge, and how they access long-range episodic representations to drive memory recall:

1. **Discovery of feature representations in AC**: The paper demonstrates that individual features are not stored in hippocampus but are represented in the anterior cingulate cortex (AC), a prefrontal region. AC neurons exhibit feature selectivity and mixed selectivity during retrieval, contrasting with CA1's conjunctive coding.

2. **AC is necessary and sufficient for feature-based recall**: Unlike LEC, AC is specifically required for feature-based memory retrieval. Inhibition of AC (but not LEC) causes deficits in feature-based recall and selectively silences CA1 context neurons without broad non-specific effects. Chemogenetic and optogenetic inhibition of CA1 context neurons prevents AC feature representation emergence, showing hippocampal dependence.

3. **Dedicated retrieval circuit**: The AC-CA1 pathway functions as a dedicated retrieval circuit distinct from the LEC-CA1 storage circuit. AC and LEC project to largely separate CA1 neuron populations, with AC inputs overlapping more with FOS+ context neurons.

4. **Dynamic temporal reorganization**: The paper reveals a striking reversal of temporal dynamics between training and retrieval. During training, CA1 context ensembles lead AC context ensembles (CA1: 10.41s, AC: 16.37s); during retrieval, AC feature ensembles lead CA1 context ensembles (AC: 7.32s, CA1: 13.65s). This represents a shift from hippocampal-led encoding to cortical-led retrieval.

5. **Saliency-dependent coupling**: AC-CA1 functional coupling is enhanced by memory saliency, with stronger correlations between AC feature ensembles and CA1 context ensembles for aversive compared to neutral contexts.

6. **Causal role of feature-coding neurons**: Using TRAP2 to specifically inhibit feature-coding neurons demonstrates their causal necessity for recall—selective silencing of ~20% feature-coding neurons causes near-complete recall deficits, while silencing a random equal-sized population has no effect.

These findings provide direct neurophysiological support for theoretical frameworks regarding prefrontal contributions to memory recall and establish a model where parallel processing enables neocortex to parse experiences into details (features) that have targeted access to hippocampal conjunctive representations.

---

### Brain regions & systems

- **Anterior cingulate cortex (AC)**: Prefrontal region that encodes feature representations and mixed selectivity during retrieval; necessary for feature-based recall; projects directly to CA1; shows dynamic temporal lead during retrieval (7.32s vs CA1's 13.65s); feature ensembles correlate with CA1 context ensembles, especially for aversive contexts
- **Hippocampal CA1**: Encodes conjunctive representations of context (not individual features); shows context-selective neurons (~10% during training, 9% conjunctive during retrieval); during training, context ensemble recruitment precedes AC (10.41s vs 16.37s); during retrieval, follows AC feature ensembles (13.65s vs 7.32s); receives direct inputs from both AC and LEC
- **Lateral entorhinal cortex (LEC)**: Provides cortical input to CA1; inhibition causes broad non-specific silencing of CA1 (not selective to context neurons); not required for feature-based recall; projects to largely separate CA1 neuron population compared to AC; hypothesized to function primarily during memory storage rather than retrieval
- **Hippocampal CA3**: Mentioned as having recurrent architecture likely creating conjunctive rather than feature representations; receives tracer injections but not primary focus of study
- **Prefrontal cortex (general)**: Referenced in discussion as region previously demonstrated to be required for memory retrieval; AC identified as specific subregion with direct projections to hippocampus

---

### Mechanistic insight

This paper meets the high bar for mechanistic insight by presenting both an algorithmic framework and neural data that specifically support that framework over alternatives.

**Computational level**: The brain solves the problem of memory retrieval from partial cues by maintaining separate representations: conjunctive representations in hippocampus for unified context encoding, and feature representations in prefrontal cortex for flexible access. This enables pattern completion—full contextual memories can be retrieved from partial feature cues.

**Algorithmic level**: The algorithm involves:
1. **High-dimensional feature coding in AC**: Single AC neurons exhibit mixed selectivity (responding to multiple features), creating a high-dimensional population code where separate ensembles drive feature selectivity
2. **Low-dimensional conjunctive coding in CA1**: CA1 neurons bind features into coherent context representations through recurrent attractor-like dynamics, creating overlapping ensembles for features of the same context
3. **Targeted recruitment**: AC feature ensembles target and recruit appropriate CA1 context ensembles during retrieval, with temporal dynamics showing AC leads CA1 during recall (reversal from training phase)

**Implementational level**: 
- **Dedicated circuit**: Direct monosynaptic projections from AC to CA1 form a dedicated retrieval circuit, distinct from the LEC-CA1 storage circuit (AC and LEC project to largely separate CA1 neuron populations)
- **Cell-type specificity**: ~20% of AC neurons are feature-coding neurons (TRAPed by feature exposure); these show causal necessity for recall when selectively inhibited
- **Saliency-dependent plasticity**: AC-CA1 coupling is enhanced for aversive (salient) contexts, with stronger correlations and more synchronous activity
- **Dynamic temporal reorganization**: The physical circuit shows activity-dependent temporal reorganization, with hippocampus leading during encoding (CA1: 10.41s, AC: 16.37s) and AC leading during retrieval (AC: 7.32s, CA1: 13.65s)

The paper provides causal evidence through optogenetic inhibition paired with imaging, showing that AC feature representations are necessary for recruiting CA1 context representations and driving behaviour, establishing a mechanistic account of cortical-hippocampal interactions during memory retrieval.

---

### Limitations & open questions

- **Long-term stability**: The long-term stability of the observed feature and conjunctive codes remains to be determined—whether these representations persist, drift, or are reorganized over extended periods
- **Time-limited roles**: Whether the prefrontal-hippocampal retrieval circuit has time-limited roles (e.g., whether AC is required for recent but not remote memories, similar to systems consolidation patterns)
- **Molecular signatures**: Whether molecular signatures predict functional heterogeneity that defines varying levels of commitment individual neurons have within otherwise drifting population codes
- **Storage vs. retrieval circuit division**: The hypothesis that LEC-CA1 functions primarily for storage while AC-CA1 functions primarily for retrieval requires further validation; the paper notes this as a postulate based on their findings
- **Neutral context analysis**: Some mice did not reliably classify neutral context as distinct, limiting analysis primarily to reward and aversive contexts
- **Cell-type specificity**: The study focused on excitatory neurons (CamKII+); roles of inhibitory interneurons in the AC-CA1 circuit were not characterized
- **Potential indirect effects**: While the paper establishes direct AC-CA1 projections, they note that effects could also involve downstream collaterals of AC or indirect interactions with CA1

---

### Connections & keywords

**Key citations:**
- Rajasethupathy et al. (2015) — Projections from neocortex mediate top-down control of memory retrieval (Nature)
- Tomita et al. (1999) — Top-down signal from prefrontal cortex in executive control of memory retrieval (Nature)
- O'Reilly & Rudy (2001) — Conjunctive representations in learning and memory (Psychological Review)
- Wills et al. (2005) — Attractor dynamics in hippocampal representation (Science)
- Rigotti et al. (2013) — Importance of mixed selectivity in complex cognitive tasks (Nature)
- Mante et al. (2013) — Context-dependent computation by recurrent dynamics in prefrontal cortex (Nature)

**Named models or frameworks:**
- Attractor network dynamics (hippocampal CA3-CA1)
- Mixed selectivity coding (prefrontal cortex)
- Pattern completion (memory retrieval from partial cues)
- Marr's three levels of analysis (implicit in mechanistic approach)
- Conjunctive vs. feature representations (dual memory system)

**Brain regions:**
- Anterior cingulate cortex (AC)
- Hippocampal CA1
- Lateral entorhinal cortex (LEC)
- Hippocampal CA3
- Prefrontal cortex (general)

**Keywords:**
- Contextual memory
- Feature representations
- Conjunctive representations
- Memory retrieval
- Two-photon calcium imaging
- Optogenetic inhibition
- TRAP2 activity-dependent targeting
- Prefrontal-hippocampal circuit
- Anterior cingulate cortex
- Pattern completion
- Mixed selectivity
- Attractor dynamics
- Virtual reality behaviour
- Longitudinal imaging
