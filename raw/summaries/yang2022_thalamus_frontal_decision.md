---
source_file: yang2022_thalamus_frontal_decision.md
paper_id: yang2022_thalamus_frontal_decision
title: "Thalamus-driven functional populations in frontal cortex support decision-making"
authors:
  - "Weiguo Yang"
  - "Sri Laasya Tipparaju"
  - "Guang Chen"
  - "Nuo Li"
year: 2022
journal: "Nature Neuroscience"
paper_type: empirical
contribution_type: empirical
species:
  - mouse
methods:
  - optogenetics
brain_regions:
  - prefrontal_cortex
  - thalamus
frameworks:
  - mixed_selectivity
keywords:
  - thalamus
  - frontal_cortex
  - decision_making
  - motor_cortex
  - mixed_selectivity
  - population_coding
  - optogenetics
  - working_memory
  - tactile_discrimination
  - activity_modes
  - cortico_cortical_connectivity
  - thalamocortical_loop
  - persistent_activity
  - dimensionality_reduction
  - driven
  - functional
  - populations
  - frontal
  - cortex
  - support
---

### One-line summary

Thalamic inputs drive functionally distinct subnetworks within mouse anterior lateral motor cortex (ALM) that encode stimulus, choice, and action during tactile decision-making, with thalamic inputs having stronger impact on task selectivity than cortico-cortical inputs.

### Background & motivation

Frontal cortical neurons exhibit diverse selectivity during decision-making, but the circuit basis for this selectivity remains unclear. One view posits randomly mixed selectivity across shared neuronal populations, while anatomically defined neurons suggest structured circuits with segregated populations. This study addresses how behavioral information is encoded in frontal cortex and how this encoding relates to underlying anatomical circuit organization, particularly the relative contributions of cortico-cortical versus thalamic inputs.

### Methods

- **Task**: Head-fixed mice performed a tactile decision task discriminating object location (anterior vs posterior) using whiskers, with directional licking after a delay epoch (1.3 s or 1.7 s)
- **Recordings**: Silicon probe recordings from left ALM (20,046 neurons total: 9,626 from primary dataset with 1.3-s delay, 10,420 from second dataset with 1.7-s delay)
- **Clustering analysis**: t-SNE embedding of PSTHs followed by density peak clustering to identify prototypical response profiles; ePAIRS test for non-uniform distribution
- **Activity modes**: Decomposition of population activity into orthogonal stimulus, choice, action, outcome, ramping, go, and response modes
- **Connectivity mapping**: ChR2-tagging and ChR2-assisted circuit mapping with whole-cell recordings to identify postsynaptic neurons; TTX pharmacology to verify monosynaptic connections
- **Optogenetic inactivation**: Photoinhibition of S1/S2, contralateral ALM (cALM), and thalamus (ThalALM) during behavior using VGAT-ChR2-EYFP or GtACR1 mice

### Key findings

- ALM neurons exhibit a repeatable collection of 94 prototypical response profiles (clusters) that are consistent across mice and datasets, contrary to the notion of randomly mixed selectivity
- Stimulus, choice, and action are encoded by distinct but partially overlapping functional populations that can be delineated by their response profiles (k-means clustering on activity mode weights)
- Neurons with similar response profiles exhibit significant trial-to-trial noise correlation, suggesting they belong to subnetworks
- S1/S2, cALM, and ThalALM inputs each connect to all functional populations (stimulus, choice, action coding) but with differing strengths: thalamic inputs have higher connection probability and elicit stronger EPSPs than cortico-cortical inputs
- Photoinhibition of thalamus (ThalALM) has stronger effects on ALM activity modes than photoinhibition of S1/S2 or cALM: thalamic inputs are required for stimulus selectivity, choice selectivity, and action mode
- Stimulus information in ALM persists after S1/S2 photoinhibition but is abolished by thalamic photoinhibition, suggesting redundant subcortical pathways signal stimulus information via thalamus
- Choice and ramping signals share the same neuronal population, supporting models where ramping plays a permissive role for choice development

### Computational framework

The study employs dynamical systems and dimensionality reduction approaches to analyze neural population activity:

- **Dimensionality reduction**: PCA and t-SNE for visualizing response profile clustering; demixed PCA (dPCA) for decomposing activity into task-relevant modes
- **Activity modes**: Linear decomposition of population activity into orthogonal directions (stimulus, choice, action, outcome, ramping, go, response) that capture distinct behavioral features
- **Population dynamics**: Analysis of neural trajectories in activity space, with examination of how selectivity evolves across trial epochs
- **Null models**: Synthetic populations with randomly mixed selectivity generated to contrast with actual ALM data; ePAIRS statistical test for non-uniform distribution of coding vectors

The computational framework treats population activity as evolving in a high-dimensional space where different task variables are encoded along distinct, near-orthogonal directions, contrasting with models of randomly mixed selectivity.

### Prevailing model of the system under study

The prevailing view in the field was that frontal cortical neurons exhibit randomly mixed selectivity during decision-making, where a shared neuronal population multiplexes multiple computations. This view was supported by neurophysiology recordings showing individual neurons exhibit a seeming continuum of time-varying responses and random combinations of task selectivity. Randomly mixed selectivity was thought to produce high-dimensional representations with greater computational capacity and could arise in recurrent neural networks with little circuit structure. In this scheme, single neuron responses cannot be readily interpreted in terms of anatomical circuit organization. The authors also note that frontal cortical circuits have highly organized anatomical structure with distinct long-range loops, and previous studies found distinct frontal cortex projection neurons carrying specific information to different brain regions.

### What this paper contributes

This paper challenges the prevailing model of randomly mixed selectivity by demonstrating that:

1. ALM neurons exhibit organized, repeatable prototypical response profiles rather than a continuum of responses
2. Stimulus, choice, and action are encoded by largely distinct (though partially overlapping) functional populations that can be delineated by their response profiles, rather than being randomly mixed across a shared population
3. These functional populations receive differential contributions from long-range inputs: while S1/S2, cALM, and thalamic inputs all contact all functional populations, thalamic inputs have the strongest impact on task selectivity
4. Thalamic inputs are required for maintaining stimulus information, choice selectivity, and action-related activity in ALM, suggesting the thalamus drives subnetworks within frontal cortex coding distinct decision features

The paper establishes that cortical task selectivity is more strongly dependent on thalamic inputs than cortico-cortical transmission, providing a revised model of frontal cortical circuit organization during decision-making.

### Brain regions & systems

- **Anterior lateral motor cortex (ALM)**: Primary region of study; contains neurons with diverse but organized response profiles coding stimulus, choice, and action during a tactile decision task
- **Somatosensory cortex (S1/S2)**: Provides ipsilateral inputs to ALM that preferentially innervate superficial layers; contributes to stimulus information during the sample epoch but not necessary for maintaining stimulus information during the delay
- **Contralateral ALM (cALM)**: Provides inputs to ipsilateral ALM that affect choice-related activity; photoinhibition biases upcoming lick direction
- **Thalamus (ThalALM)**: Includes ventral-medial nucleus, ventral-anterior-lateral nucleus (VAL), medial-dorsal nucleus, and intralaminar nuclei; provides the strongest excitatory drive to ALM; inputs target all functional populations but are required for stimulus selectivity, choice selectivity, and action mode; thalamic photoinhibition abolishes task selectivity even in neurons with unchanged spike rates

### Mechanistic insight

This paper provides strong mechanistic insight by mapping specific computational roles onto identified anatomical circuit elements, meeting both criteria: (1) it presents a circuit model where distinct functional populations carry specific decision-related computations, and (2) it provides neural data (recordings, optogenetic tagging, inactivation) that support this model over alternatives.

**Computational**: The brain must maintain sensory information across a delay, form a decision, and initiate appropriate actions. The paper frames this as distinct computational sub-problems (stimulus encoding, choice formation, action initiation) that are mapped onto distinct but partially overlapping neural populations.

**Algorithmic**: The paper proposes that ALM contains segregated functional populations coding specific features of behavior (stimulus, choice, action), rather than randomly mixed selectivity. Activity modes (orthogonal directions in neural population space) capture distinct behavioral features. The choice and ramping modes share a neuronal population, potentially enabling ramping signals to play a permissive role in choice development.

**Implementational**: The paper links these algorithmic components to specific anatomical structures: (1) S1/S2, cALM, and thalamic inputs all contact all functional populations but with different strengths; (2) thalamic inputs provide the strongest excitatory drive and are required for task selectivity; (3) cortico-cortical inputs preferentially affect superficial layers while thalamic inputs preferentially affect deep layers; (4) neurons with similar response profiles exhibit trial-to-trial noise correlation, suggesting they belong to subnetworks. The physical implementation thus involves thalamocortical loops driving distinct subnetworks within frontal cortex.

### Limitations & open questions

- The study focused on one brain region (ALM) and one task (tactile decision with delay); whether these findings generalize to other frontal regions and tasks remains to be determined
- The study does not fully resolve the interaction between thalamic and cortical inputs; more work is needed to understand how these inputs interact to produce task selectivity
- While the study found that thalamic inputs drive selectivity, it does not identify the specific thalamic nuclei or cell types involved; ThalALM includes multiple nuclei (ventral-medial, VAL, medial-dorsal, intralaminar)
- The study primarily used photoinhibition rather than cell-type-specific manipulations; the specific cell types within ALM that receive thalamic input and generate selectivity are not fully characterized
- The study does not trace the ultimate origin of ramping signals, which appear to originate outside the thalamocortical loop but are transmitted through thalamus to ALM
- Whether ALM responses fully conform to a finite set of discrete clusters or whether there is a continuum of responses remains unresolved; the smaller clusters were not reproducible across clustering methods
- The study does not determine whether functional populations receive like-to-like versus nonspecific thalamic connections
- The study does not determine whether the same stimulus and choice coding populations encode these variables across different tasks and modalities

### Connections & keywords

**Key citations**: 
- Machens, Romo & Brody (2010) - random mixed selectivity view
- Mante et al. (2013) - context-dependent computation in PFC
- Kobak et al. (2016) - demixed PCA
- Guo et al. (2017) - thalamocortical loops for persistent activity
- Li et al. (2016) - robust neuronal dynamics in premotor cortex
- Hirokawa et al. (2019) - cell-type-specific coding in frontal cortex
- Inagaki et al. (2022) - midbrain-thalamus-cortex circuit for movement initiation

**Named models or frameworks**:
- Mixed selectivity (randomly mixed selectivity across shared populations)
- Activity modes (orthogonal directions in neural population space)
- ePAIRS test (elliptical projection angle index of response similarity)
- Thalamocortical loop model
- Ramping/urgency signals

**Brain regions**:
- Anterior lateral motor cortex (ALM)
- Somatosensory cortex (S1/S2)
- Contralateral ALM (cALM)
- Thalamus (ventral-medial nucleus, VAL, medial-dorsal nucleus, intralaminar nuclei; collectively ThalALM)
- Vibrissal motor cortex (vM1)
- Vibrissal somatosensory cortex (vS1)
- Secondary motor cortex (M2)

**Keywords**: thalamus, frontal cortex, decision-making, motor cortex, mixed selectivity, population coding, optogenetics, working memory, tactile discrimination, activity modes, cortico-cortical connectivity, thalamocortical loop, persistent activity, dimensionality reduction
