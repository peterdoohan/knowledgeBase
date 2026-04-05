---
source_file: rosen2025_distributed_cognition.md
title: How distributed is the brain-wide network that is recruited for cognition?
authors: Matthew C. Rosen, David J. Freedman
year: 2025
journal: Nature Reviews Neuroscience
paper_type: review
contribution_type: review
---

### One-line summary

Cognitive variables are broadly but not ubiquitously distributed across the brain, engaging movement-related areas to a surprising degree while sparing primary sensory regions, with the breadth of recruitment scaling with cognitive demand.

---

### Background & motivation

A traditional "localization of function" view has parcellated the brain into distinct sensory, motor, and cognitive regions, with abstract cognitive functions ascribed to association cortical areas like parietal-frontal regions. However, recent high-throughput measurement techniques in rodents have revealed that neural activity is modulated by uninstructed movements across nearly the entire brain, including primary sensory areas, prompting a "distributed" alternative view. This Perspective evaluates whether cognitive variables follow similar distributed encoding patterns and identifies principles governing the brain-wide network engaged for cognition.

---

### Methods

This is a review/synthesis paper that integrates findings across multiple experimental approaches:

- **Rodent brain-wide recording studies**: Analysis of large-scale Neuropixels electrophysiology (hundreds of channels) and two-photon calcium imaging (thousands to millions of neurons) in mice during decision-making tasks
- **Deep task sampling in primates**: Aggregation of electrophysiological recordings across multiple brain areas using standardized behavioral tasks (motion discrimination, vibrotactile discrimination, delayed match-to-category) performed by macaque monkeys
- **Optogenetic perturbation surveys**: Systematic photoinhibition across cortical arrays in mice to identify regions necessary for task performance
- **Cross-species anatomical comparisons**: Analysis of cortical area expansion and connectivity differences between rodents (mouse), marmosets, and macaques
- **Behavioral tracking**: Quantification of uninstructed movements using machine learning-based pose estimation (DeepLabCut, SLEAP)

---

### Key findings

- **Movement-related activity is widespread**: In rodents, ~30-40% of variance in neural activity across cortex, including primary sensory areas, is explained by uninstructed facial and body movements rather than task variables
- **Cognitive signals are broadly distributed but not ubiquitous**: Decision signals appear throughout frontal motor/premotor areas and basal ganglia in both rodents and primates, but are absent in primary visual cortex (V1) and primary somatosensory cortex (S1)
- **Cognitive demand scales network breadth**: Optogenetic perturbation studies in mice show that simple visually-guided tasks require only sensory/premotor areas, while memory-guided and evidence accumulation tasks engage all 29 tested cortical sites; similar demand-dependent recruitment observed in primate parietal cortex
- **Movement areas encode abstract cognition**: Even when decisions are dissociated from specific actions (e.g., manual responses for visual motion categories), movement-related areas including LIP, SC, premotor cortex, and FEF show robust cognitive encoding
- **Cognitive signals correlate with uninstructed movements**: Category-correlated fixational eye movements emerge during memory delays, even under strict fixation requirements; these movements are attenuated by SC but not LIP inactivation, suggesting they arise from alignment of cognitive representations with motor output axes
- **Training history shapes neural engagement**: Prior training on simpler tasks alters neural tuning and engagement patterns in higher areas during more complex tasks; similar effects observed in sensory areas (MT) for different training histories
- **Species differences in connectivity predict functional distribution**: Mouse cortex has ~97% direct interareal connectivity vs. ~60% in macaques and marmosets, suggesting rodent areas may be recruited more diversely than primate areas

---

### Computational framework

The paper employs several computational and theoretical frameworks:

**Representational geometry**: The paper discusses how cognitive variables may be encoded in different "formats" across brain areas, using representational geometry as a framework for understanding how the same information can be rendered in different neural codes. This provides a normative rationale for why recruiting more areas might be beneficial — access to more representational formats enables more flexible computation.

**Dynamical systems**: The discussion of premotor "null space" — dimensions of neural activity that do not drive movement — draws on dynamical systems frameworks for understanding how preparatory activity can be movement-potent or movement-null, with cognitive encoding potentially occupying the latter.

**Network connectivity analysis**: The comparison of interareal connectivity across species (mouse vs. primate) uses graph-theoretic concepts to relate anatomical connection density to functional distribution.

**Signal detection/decoding**: The paper cites decoding performance (R² relative to chance) as a metric for quantifying the strength and distribution of cognitive signals across areas.

---

### Prevailing model of the system under study

The paper identifies two prevailing viewpoints on brain functional organization:

**Localized view**: The traditional "localization of function" view holds that complex behavior results from computations carried out across distinct brain areas, each with specialized roles. This view emerged from 19th-20th century stimulation and lesion studies (Fritsch & Hitzig, Ferrier, Penfield) and single-electrode recordings revealing specialized sensory (Hubel & Wiesel) and motor representations. A looser version of this view ascribes abstract cognitive functions to association cortical areas (parietal-frontal regions, PFC) while maintaining that early sensory areas encode present sensory contents.

**Distributed view**: An emerging alternative, prompted by high-throughput recording techniques in rodents, posits that neural encoding of behavioral variables is distributed across a wide range of areas — "everything, everywhere, all at once." This view is supported by findings that ~30% of cortical activity variance is explained by uninstructed movements even in primary sensory areas, and that choice signals appear broadly across the rodent brain.

The paper evaluates which of these viewpoints better describes abstract cognition specifically, synthesizing evidence that points toward an intermediate position: cognitive variables are broadly distributed but not ubiquitous, with systematic patterns governing their distribution.

---

### What this paper contributes

This Perspective makes several key contributions to understanding the neural basis of cognition:

**Synthesis of rodent and primate findings**: The paper integrates evidence from both rodent brain-wide recording studies and primate "deep task sampling" approaches to establish convergent principles about cognitive encoding across species. This synthesis reveals that both systems show similar patterns: cognitive variables engage movement-related areas but spare primary sensory areas.

**Cognitive demand as a determinant of network breadth**: The paper establishes that the breadth of brain recruitment scales with cognitive demand — simple tasks engage localized circuits while complex tasks recruit broader networks. This principle emerges from both optogenetic perturbation studies in mice and electrophysiological recordings in primates, providing a unified framework for understanding task-dependent neural engagement.

**Identification of uninstructed movements as cognitive indicators**: The paper highlights a previously underappreciated phenomenon — small, uninstructed movements (especially eye movements) that reflect ongoing cognitive contents. These "poker tells" emerge across species (rodents, monkeys, humans) and tasks, suggesting they arise from fundamental properties of how cognitive networks interface with motor control systems. The paper presents evidence that these movements may result from transient alignment of cognitive representations with motor output axes.

**Causal role of movement areas in abstract cognition**: Through discussion of inactivation studies, the paper establishes that cognitive encoding in areas like LIP and SC is not merely correlative but causally necessary for performance of abstract categorization tasks, even when decisions are reported manually rather than through the effector associated with those areas.

**Reconciling distributed and localized views**: The paper advances a nuanced position that reconciles the "distributed" and "localized" viewpoints — cognitive variables are distributed across a network of higher-order areas but not ubiquitously (they spare primary sensory areas). The distribution is systematic and governed by functional principles rather than reflecting "everything, everywhere, all at once."

**Future directions and theoretical framework**: The paper proposes that different brain areas may encode the same cognitive information in different "formats," and that recruiting more areas may provide access to more representational formats, enabling more flexible computation. This hypothesis connects to representational geometry frameworks and suggests testable predictions for future research.

---

### Brain regions & systems

- **Primary visual cortex (V1/striate cortex)**: Early sensory area that primarily encodes present visual stimulation; does not encode choice or cognitive variables during decision tasks
- **Middle temporal area (MT)**: Visual motion processing area; encodes instantaneous motion evidence but not integrated decision signals or categories
- **Middle superior temporal area (MST)**: Visual motion area; encodes both veridical motion direction and learned categories during short-term memory delays
- **Lateral intraparietal area (LIP)**: Parietal area associated with gaze control; strongly encodes decision variables, category information, and working memory; shows task-dependent engagement (stronger during cognitively demanding tasks)
- **Medial intraparietal area**: Parietal area; encodes categorical decisions and spatial information during delayed response tasks
- **Superior colliculus (SC)**: Subcortical oculomotor structure; shows strongest category encoding among recorded areas; causally necessary for categorization performance even for manual responses; linked to cognitively correlated eye movements
- **Dorsolateral prefrontal cortex (PFC)**: Executive area; encodes abstract rules, task context, and categorical information; source of top-down feedback that may regulate network engagement
- **Supplementary motor area (SMA)**: Premotor area; encodes remembered sensory frequencies and decision variables during vibrotactile discrimination
- **Pre-supplementary motor area (pre-SMA)**: Premotor area; encodes working memory and decision variables during vibrotactile tasks
- **Dorsal premotor cortex (PMd)**: Premotor area; encodes decision difficulty, abstract categorical decisions, and working memory content
- **Frontal eye fields (FEF)**: Oculomotor area; encodes changes in decision criteria and cognitive control signals
- **Primary somatosensory cortex (S1)**: Early sensory area; primarily encodes present tactile stimulation, not working memory or decision variables
- **Secondary somatosensory cortex**: Somatosensory area; shows some modulation by remembered stimulus frequency during delay and comparison periods
- **Basal ganglia (caudate, subthalamic nucleus)**: Subcortical circuit; encodes multiple computations for perceptual decisions and contributes causally to decision-making
- **Anterolateral motor cortex (mouse)**: Frontal premotor area in mice; necessary for voluntary licking behaviors and tactile decisions
- **Locus coeruleus**: Neuromodulatory nucleus; activation modulates arousal and broadly increases functional connectivity across brain areas

---

### Mechanistic insight

This paper does not meet the high bar for mechanistic insight because it is a review/synthesis paper rather than a primary empirical or computational study. The paper does not present a new algorithm or formal model, nor does it provide new neural data directly linking a specific computational mechanism to measured neural activity.

However, the paper discusses several mechanistic hypotheses and frameworks that could guide future research:

1. **Null space encoding**: The paper discusses the hypothesis that cognitive variables may be encoded in premotor "null space" — dimensions of neural activity that do not drive movement. This could allow cognitive representations to utilize motor circuits without causing overt behavior.

2. **Transient alignment hypothesis**: The paper proposes that cognitively correlated movements (like category-correlated eye movements) may arise from transient alignment of cognitive representations with motor output axes in structures like the superior colliculus.

3. **Representational format hypothesis**: The paper proposes that different brain areas may encode the same cognitive information in different "formats," and that recruiting more areas provides access to more representational formats for flexible computation.

4. **Neuromodulatory recruitment**: The paper suggests that diffuse projections from neuromodulatory systems (e.g., locus coeruleus) may regulate the breadth of network engagement based on cognitive demand and arousal.

These ideas provide conceptual frameworks for understanding distributed cognitive encoding but have not yet been formalized into quantitative models and directly tested against neural data in the studies reviewed.

---

### Limitations & open questions

The paper identifies several acknowledged limitations and open questions:

**Limitations of current evidence:**
- **Species differences unresolved**: Direct comparison between rodents and primates is complicated by methodological differences and anatomical differences (mouse cortex has ~97% direct interareal connectivity vs. ~60% in primates)
- **Technical limitations in primates**: Brain-wide recording techniques available in rodents are not yet fully translated to non-human primates, limiting the ability to directly compare species
- **Training effects confounded**: Most neural data come from extensively trained subjects, making it difficult to distinguish task-specific engagement from training-induced plasticity effects

**Open questions identified:**
- **What are cognitive signals across different areas good for?** The functional role of distributed cognitive encoding remains unclear — do different areas contribute different representational formats, or is there redundancy?
- **What distinguishes encoding in one area from another?** If cognitive signals are distributed, what functional differences exist between areas that encode similar variables?
- **Do cognitively correlated movements have functional importance?** Small movements reflecting cognitive contents are ubiquitous, but it remains unknown whether they are epiphenomenal or functionally important for task performance
- **How does training history shape brain-wide engagement?** The effects of prolonged training on which regions become necessary for performance remain largely unexplored, especially for cognition
- **What is the representational format of distributed cognitive codes?** The paper suggests different areas may encode the same information in different formats, but this hypothesis remains to be tested systematically

---

### Connections & keywords

**Key citations:**
- Fritsch & Hitzig (1870) — foundational electrical stimulation studies establishing localization of function
- Hubel & Wiesel (1962) — localized sensory processing in visual cortex
- Shadlen, Newsome & colleagues — classic motion discrimination task and decision-making studies
- Romo & colleagues — vibrotactile discrimination task studies revealing working memory encoding
- Stringer et al. (2019) — widespread movement-related activity in mouse cortex
- International Brain Laboratory (2025) — brain-wide survey of neural activity during decision-making
- Freedman & Assad (2006) and subsequent studies — categorization in parietal cortex

**Named models or frameworks:**
- Localization of function (classical view)
- Distributed encoding / "everything, everywhere, all at once" (alternative view)
- Deep task sampling (methodological approach)
- Representational geometry (theoretical framework)
- Marr's three levels (computational, algorithmic, implementational — discussed indirectly)
- Null space encoding hypothesis
- Demand-dependent recruitment framework

**Brain regions:**
- Primary visual cortex (V1), Middle temporal area (MT), Middle superior temporal area (MST)
- Lateral intraparietal area (LIP), Medial intraparietal area, Superior colliculus (SC)
- Dorsolateral prefrontal cortex (PFC), Frontal eye fields (FEF)
- Supplementary motor area (SMA), Pre-supplementary motor area (pre-SMA), Dorsal premotor cortex (PMd)
- Primary somatosensory cortex (S1), Secondary somatosensory cortex
- Basal ganglia (caudate, subthalamic nucleus)
- Locus coeruleus

**Keywords:**
distributed cognition, brain-wide encoding, cognitive demand, uninstructed movements, premotor cortex, decision-making, working memory, neural encoding, representational geometry, task-dependent recruitment, category learning, superior colliculus, parietal cortex, deep task sampling, neuromodulation
