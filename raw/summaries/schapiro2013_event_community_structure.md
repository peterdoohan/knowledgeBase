---
source_file: schapiro2013_event_community_structure.md
title: Neural representations of events arise from temporal community structure
authors: Anna C. Schapiro, Timothy T. Rogers, Natalia I. Cordova, Nicholas B. Turk-Browne, Matthew M. Botvinick
year: 2013
journal: Nature Neuroscience
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Event representations emerge from temporal community structure in sequences, where stimuli with overlapping temporal associations cluster together and form representational boundaries that guide event segmentation, independent of transition probability or predictive uncertainty.

### Background & motivation

Most theories of event segmentation rely on predictive uncertainty or surprise at boundaries—when transition probabilities shift, event boundaries are detected. However, these accounts cannot explain segmentation when transition probabilities are uniform. This paper proposes an alternative: event representations form around "communities" of stimuli that share temporal associations, even when all transitions are equally probable.

### Methods

- **Experimental design**: Three experiments using sequences generated from a graph with community structure (three clusters of 5 nodes each, uniform transition probabilities)
- **Stimuli**: Experiment 1 used 15 Sabaean alphabet glyphs; Experiments 2-3 used 15 abstract non-verbalizable images
- **Task**: Cover task requiring detection of rotated stimuli (to ensure attention without explicit sequence learning instructions)
- **Parsing phase**: Participants pressed spacebar at perceived event boundaries during alternating blocks of random walk and Hamiltonian path sequences
- **fMRI (Experiment 3)**: 20 participants, rapid event-related design, 5 scanning runs, analyzed GLM responses and multivoxel pattern similarity
- **Model**: Three-layer feedforward neural network (15 input, 50 hidden, 15 output units) trained to predict next stimulus in sequence using backpropagation

### Key findings

- **Parsing behavior**: Participants reliably parsed sequences at community boundaries in both random walk and Hamiltonian path conditions (Experiment 1: t(29) = 2.27, P < 0.05; Experiment 2: t(9) = 2.30, P < 0.05), despite uniform transition probabilities
- **mPFC engagement**: Medial prefrontal cortex showed sustained activity within communities and transient disengagement at boundaries (negative correlation with boundary regressor, P < 0.05 corrected), consistent with tracking event structure
- **Repetition enhancement**: Bilateral IFG and insula showed progressively increasing BOLD responses as more items from the same community were viewed (adaptation regressor, P < 0.05 corrected), suggesting neural populations increasingly engaged by community membership
- **Pattern similarity**: Left IFG, insula, ATL, and STG showed higher multivoxel pattern similarity for within-community vs. between-community item pairs (P < 0.05 corrected), indicating clustered representational geometry
- **Model results**: Neural network trained on same sequences developed hidden layer representations that clustered by community (t(19) = 140.84, P < 0.0001), with boundary items represented more distantly from internal community items (t(19) = 22.82, P < 0.0001), reproducing the representational structure found in fMRI

### Computational framework

The paper employs a **connectionist/parallel distributed processing** framework. The computational model is a three-layer feedforward neural network trained via backpropagation to predict the next stimulus in a sequence. The key insight is that when items share temporal contexts (predict similar successors), their hidden layer representations become similar through learning—analogous to how semantic categories emerge from feature overlap in models of semantic cognition. This framework demonstrates how community structure can drive learning without relying on explicit chunking or n-gram frequency differences.

### Prevailing model of the system under study

Prior to this work, the dominant account of event segmentation held that boundaries are detected when predictive uncertainty or surprise is elevated—i.e., when transition probabilities shift. This "prediction error" framework assumes that within-event transitions are highly predictable while between-event transitions are less predictable. The introduction to this paper notes that prior work on event perception focused on "transient elevations in predictive uncertainty or surprise as the primary signal driving event segmentation."

### What this paper contributes

This paper demonstrates that event segmentation can occur independently of predictive uncertainty or surprise. The key advances are:

1. **Segmentation without probability shifts**: Event boundaries can be identified when all transitions have equal probability, provided the sequence has community structure (clusters of mutually predicting stimuli).

2. **Temporal community structure as organizing principle**: Events emerge from representational clustering driven by shared temporal associations—items that predict and are predicted by similar other items become represented similarly.

3. **Neural evidence for representational clustering**: Left IFG, insula, ATL, and STG show community-structured pattern similarity after brief exposure, and mPFC tracks event boundaries through sustained/discharged activity patterns.

4. **Computational demonstration**: A simple predictive neural network learns community-structured representations from the same exposure that drives human behavior and neural responses, providing a mechanistic account of how temporal structure shapes representations.

5. **Link to semantic cognition**: The paper bridges event segmentation and semantic category learning, proposing that both arise from the same underlying learning mechanism—clustering based on contextual overlap.

### Brain regions & systems

- **Medial prefrontal cortex (mPFC, BA 9/10/24)**: Engaged throughout event duration, transiently disengaged at boundaries; proposed to track changes in representational patterns in other regions and provide a signal for parsing decisions
- **Left inferior frontal gyrus (IFG, BA 44/45)**: Showed repetition enhancement during community traversal and community-structured multivoxel pattern similarity; implicated in semantic processing and sequential structure processing
- **Right inferior frontal gyrus (IFG, BA 44/45)**: Showed repetition enhancement during community traversal
- **Left anterior insula (BA 13)**: Showed repetition enhancement and community-structured pattern similarity; neighboring/adjacent to IFG findings
- **Right anterior insula (BA 13)**: Showed repetition enhancement
- **Left anterior temporal lobe (ATL, BA 38)**: Showed community-structured multivoxel pattern similarity; implicated in semantic processing
- **Left superior temporal gyrus (STG, BA 21/22)**: Showed community-structured multivoxel pattern similarity; showed marginally significant internal vs. boundary item distinction
- **Cuneus (BA 18/19)**: Showed repetition enhancement during community traversal

### Mechanistic insight

This paper presents a mechanistic account that meets the high bar for this section. The authors propose and demonstrate a specific algorithmic mechanism for how event representations emerge from temporal structure, and provide neural evidence supporting this mechanism over alternatives.

**Computational level**: The problem is learning event structure from sequences where all transition probabilities are uniform. The solution involves clustering items based on shared temporal contexts—items that predict and are predicted by similar other items should be grouped together.

**Algorithmic level**: A three-layer feedforward neural network learns to predict the next item given the current item. Through backpropagation learning, the hidden layer develops representations where items with overlapping temporal associations (shared successor sets) become represented similarly. This creates a representational geometry that clusters items by community membership, with boundary items represented more distinctly.

**Implementational level**: The fMRI results provide evidence for this algorithm being implemented in specific neural circuits:
- Left IFG, insula, ATL, and STG show the predicted community-structured pattern similarity, indicating these regions instantiate the representational clustering
- mPFC shows activity patterns consistent with tracking representational changes, potentially receiving inputs from regions with community-structured representations
- The repetition enhancement effect in bilateral IFG/insula is consistent with accumulating evidence for community membership, as predicted by the model's representational dynamics

The paper thus bridges all three levels of Marr's framework, providing a rare example of a computational model that both explains behavior and is supported by specific neural implementation evidence.

### Limitations & open questions

- The paper acknowledges that prediction error may still play a role in event segmentation in some contexts; the findings don't exclude uncertainty-based mechanisms entirely, but establish that they are not necessary
- The relationship between the identified regions (IFG, insula, ATL, STG) and regions previously associated with prediction error in event segmentation studies remains unclear and requires further investigation
- The mPFC boundary signal is hypothesized to track changes in representational patterns in other regions, but functional connectivity between mPFC and community-structure regions was not directly tested
- The model demonstrates one mechanism for learning community structure, but doesn't address how different types of structure might affect representations in different brain regions (e.g., hippocampus vs. temporal lobe)
- The stimuli were abstract visual items without intrinsic meaning; whether the same mechanisms apply to meaningful, naturalistic events remains to be tested
- The brief exposure period (~1 hour) limits understanding of how representations might evolve with extended learning

### Connections & keywords

**Key citations:**
- Zacks et al. (2001) - prior work on event segmentation and brain activity time-locked to perceptual boundaries
- Zacks et al. (2007) - prediction error computational model of event segmentation
- Saffran et al. (1996) - statistical learning in infants
- Rogers & McClelland (2004) - semantic cognition and parallel distributed processing
- Elman (1990) - finding structure in time (simple recurrent networks)
- Cleeremans & McClelland (1991) - neural network model of event sequence learning
- Turk-Browne et al. (2012) - shaping object representations based on temporal regularities

**Named models or frameworks:**
- Temporal community structure theory of event representation
- Parallel distributed processing (PDP) / connectionist framework
- Simple feedforward neural network with backpropagation learning
- PARSER model (chunking model compared against)
- Latent Semantic Analysis (LSA) / context-based semantic learning models

**Brain regions:**
- Medial prefrontal cortex (mPFC)
- Inferior frontal gyrus (IFG), bilateral
- Anterior insula, bilateral
- Anterior temporal lobe (ATL), left
- Superior temporal gyrus (STG), left
- Cuneus

**Keywords:**
- event segmentation
- temporal community structure
- statistical learning
- representational similarity
- multivoxel pattern analysis (MVPA)
- predictive learning
- sequence learning
- fMRI adaptation
- medial prefrontal cortex
- inferior frontal gyrus
