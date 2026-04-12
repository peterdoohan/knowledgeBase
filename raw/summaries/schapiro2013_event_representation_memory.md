---
source_file: schapiro2013_event_representation_memory.md
paper_id: schapiro2013_event_representation_memory
title: "Neural representations of events arise from temporal community structure"
authors:
  - "Anna C Schapiro"
  - "Timothy T Rogers"
  - "Natalia I Cordova"
  - "Nicholas B Turk-Browne"
  - "Matthew M Botvinick"
year: 2013
journal: "Nature Neuroscience"
paper_type: empirical
contribution_type: theoretical
species:
  - human
methods:
  - fmri
  - computational_modeling
  - behavioral_analysis
brain_regions:
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - superior_temporal_gyrus
  - inferior_frontal_gyrus
keywords:
  - event_segmentation
  - event_representation
  - temporal_community_structure
  - statistical_learning
  - fmri_adaptation
  - multivoxel_pattern_analysis
  - medial_prefrontal_cortex
  - inferior_frontal_gyrus
  - predictive_learning
  - sequence_learning
  - hidden_layer_representations
  - connectionist_model
  - artificial_grammar_learning
  - chunking
  - anterior_temporal_lobe
  - semantic_cognition
  - neural
  - representations
  - events
  - arise
---

### One-line summary

Event representations emerge from temporal community structure—clusters of stimuli with overlapping temporal associations—rather than from predictive uncertainty or surprise at event boundaries.

---

### Background & motivation

Traditional accounts of event segmentation rely on prediction error or surprise, where event boundaries are identified when observations are unpredictable from preceding context. This presupposes non-uniform transition probabilities. The authors propose an alternative: event representations form around "communities" of stimuli that share temporal associations (overlapping predictive contexts), analogous to how semantic categories form from shared object features. This theory can explain event segmentation even when transition probabilities are uniform.

---

### Methods

- **Stimuli**: 15 glyphs (Exp 1) or abstract images (Exps 2-3) assigned to nodes of a graph with three 5-node communities; internal connectivity dense within communities, sparse between communities
- **Design**: Random walk on graph (uniform transition probabilities) for exposure; Hamiltonian paths (visiting each node once) interspersed for testing
- **Task**: Covert orientation judgment during exposure; explicit event segmentation (parsing) during test
- **Participants**: Exp 1: n=30; Exp 2: n=10; Exp 3: n=20
- **fMRI (Exp 3)**: 3T Siemens, EPI sequence, TR=2s, TE=30ms; preprocessing with AFNI/SPM; GLM analyses and whole-brain searchlight multivoxel pattern analysis
- **Computational model**: Three-layer feedforward neural network (15 input, 50 hidden, 15 output units) trained with backpropagation to predict next item in sequence

---

### Key findings

- **Parsing behavior**: Participants consistently segmented sequences at community boundaries, even when transition probabilities were uniform and local statistics controlled (Exps 1-2; t(29)=2.27, P<0.05; t(9)=2.30, P<0.05)
- **mPFC activity**: Medial prefrontal cortex showed sustained activity during within-community periods and transient disengagement at community boundaries (P<0.05 corrected), consistent with tracking event structure
- **Repetition enhancement**: Bilateral IFG and insula showed progressively stronger responses as participants viewed more items from the same community (P<0.05 corrected), suggesting neural populations representing community membership
- **Pattern similarity**: Multivoxel patterns in left IFG, insula, ATL, and STG represented items within the same community as more similar than items from different communities (P<0.05 corrected)
- **Computational model**: The neural network developed clustered internal representations mirroring graph communities (t(19)=140.84, P<0.0001) and showed representational dynamics that could support parsing

---

### Computational framework

The paper proposes a connectionist/associative learning framework where event representations emerge from shared temporal context. The computational model is a three-layer feedforward neural network that learns to predict subsequent observations. Key features:
- **Input/output**: Localist representations of 15 stimuli
- **Learning rule**: Error-driven learning (backpropagation) with learning rate 0.2
- **Key principle**: Items generating similar predictions (shared temporal context) develop similar hidden-layer representations
- **Result**: Community structure emerges in representational space without explicit community detection mechanism

This framework connects to semantic cognition models (Rogers & McClelland 2004) where category structure emerges from feature overlap, but here the "features" are temporal associations rather than intrinsic object properties.

---

### Prevailing model of the system under study

The prevailing model of event segmentation, as described in the paper's introduction, holds that event boundaries are identified based on transient elevations in predictive uncertainty or surprise. In this framework:
- Within-event observations are highly predictable from preceding context
- Event boundaries occur when observations are less predictable
- Non-uniform transition probabilities are necessary for segmentation
- Prediction error signals (e.g., in neuromodulatory systems) drive boundary detection

This uncertainty-based account has been formalized in computational models (e.g., Reynolds, Zacks & Braver 2007) and supported by fMRI studies showing transient responses at event boundaries in regions including hippocampus and prefrontal cortex.

---

### What this paper contributes

This paper challenges the uncertainty-based account by demonstrating that event segmentation can occur without predictive uncertainty or surprise. The key contributions are:

1. **Theoretical alternative**: Event representations can form based on temporal community structure—clusters of stimuli with overlapping temporal associations—even when all transitions are equally probable.

2. **Behavioral evidence**: Participants parse sequences at community boundaries despite uniform transition probabilities, ruling out uncertainty/surprise as the sole mechanism.

3. **Neural evidence**: fMRI adaptation and multivoxel pattern analysis reveal that left IFG, insula, ATL, and STG represent community-structured stimuli as more similar, while mPFC tracks event boundaries through sustained/disengaged activity patterns.

4. **Computational demonstration**: A simple predictive learning model develops community-structured representations through error-driven learning, providing a mechanism for how temporal context shapes neural representations.

5. **Connection to semantic cognition**: The work bridges event segmentation and semantic category learning, suggesting both rely on similar associative mechanisms operating on different types of structure (temporal vs. featural).

---

### Brain regions & systems

- **Medial prefrontal cortex (mPFC, BA 9/10/24)**: Shows sustained activity during within-community periods and transient disengagement at community boundaries; may track changes in representational patterns in other regions to support parsing decisions
- **Left inferior frontal gyrus (IFG, BA 44/45) and insula (BA 13)**: Show repetition enhancement effects (progressively stronger responses with more items from same community) and represent items within same community as more similar in multivoxel patterns; implicated in representing event/community structure
- **Right inferior frontal gyrus (IFG, BA 44/45) and insula (BA 13)**: Show repetition enhancement effects similar to left hemisphere
- **Cuneus (BA 18/19)**: Shows repetition enhancement during community traversal
- **Left anterior temporal lobe (ATL, BA 38)**: Multivoxel patterns represent community structure; involved in semantic processing
- **Left superior temporal gyrus (STG, BA 21/22)**: Multivoxel patterns represent community structure; shows greater correlation between internal community items than boundary items

---

### Mechanistic insight

This paper provides a mechanistic account of how event representations emerge from temporal structure, meeting the criteria for algorithm specification and neural data support.

**Phenomenon**: Event segmentation and representation formation in structured sequences with uniform transition probabilities.

**Marr's levels analysis**:

- **Computational level**: The problem is to segment continuous experience into discrete events and form representations that capture the structure of the environment. The solution involves detecting community structure—clusters of stimuli with overlapping temporal associations. This is accomplished by learning which stimuli predict similar future observations.

- **Algorithmic level**: A three-layer feedforward neural network implements the solution. The network learns to predict the next stimulus given the current one via error-driven learning (backpropagation). Critical representational change occurs in the hidden layer: stimuli that generate similar predictions (share temporal context) develop similar hidden-layer representations. This creates clustered representations reflecting community structure without explicit community detection.

- **Implementational level**: The neural network model maps onto specific brain regions identified in the fMRI study. Left IFG, insula, ATL, and STG show representational clustering (items within communities represented more similarly), potentially implementing the hidden layer function. mPFC shows activity patterns consistent with tracking boundaries based on representational changes in these regions. The repetition enhancement effect in IFG/insula suggests accumulating evidence for community membership, potentially reflecting the dynamics of the model's hidden representations during sequence processing.

**Why the paper meets the mechanistic insight bar**: 

1. The paper specifies a concrete algorithm (predictive neural network with error-driven learning) that explains how community-structured representations emerge from sequence exposure.

2. The paper provides neural data (fMRI adaptation and multivoxel pattern analysis) showing that specific brain regions (left IFG, insula, ATL, STG) develop community-structured representations as predicted by the model.

3. The correspondence between model dynamics (Fig. 6c) and neural activity patterns in mPFC suggests the model captures not just static representations but the temporal dynamics of event processing.

The paper thus bridges algorithm and implementation, demonstrating that a specific learning mechanism (predictive learning with shared temporal context) can explain both behavioral and neural signatures of event segmentation.

---

### Limitations & open questions

- **Parsing data in fMRI (Exp 3)**: Data collected during anatomical scan was unreliable due to scanner noise interference, preventing a direct test of whether parsing behavior correlates with mPFC activity in the same participants
- **Limited exposure duration**: Only ~1 hour of sequence exposure; long-term stability of learned representations unknown
- **Hamiltonian path constraints**: The specific control conditions used to isolate community structure may not generalize to all naturalistic sequential domains
- **Network model limitations**: The feedforward model captures representational clustering but not the full temporal dynamics of event processing; recurrent architectures may be needed for more complete account
- **Region interactions**: The relationship between mPFC and IFG/insula (whether mPFC tracks representational changes in IFG to support parsing) remains speculative and requires direct functional connectivity analysis
- **Scope of mechanisms**: The paper does not claim that community structure is the only mechanism for event segmentation, nor that prediction error is never relevant; the relationship between these mechanisms in naturalistic settings needs further investigation
- **Stimulus domain**: Findings from abstract visual stimuli need validation in more naturalistic domains (language, action sequences, etc.)

---

### Connections & keywords

**Key citations:**
- Reynolds, Zacks & Braver (2007) - computational model of event segmentation from prediction
- Zacks et al. (2001) - brain activity time-locked to event boundaries
- Zacks et al. (2011) - prediction error in event segmentation
- Rogers & McClelland (2004) - semantic cognition/PDP approach
- Cleeremans & McClelland (1991) - learning structure of event sequences
- Elman (1990) - Finding structure in time
- Schapiro, Kustner & Turk-Browne (2012) - temporal regularities shaping object representations
- Saffran, Aslin & Newport (1996) - statistical learning in infants
- Rosch & Mervis (1975) - family resemblances/category structure

**Named models or frameworks:**
- Temporal community structure theory of event representation
- Prediction error/surprise-based event segmentation (contrastive framework)
- Parallel Distributed Processing (PDP) / connectionist models of semantic cognition
- PARSER model (chunking model; contrasted with community structure approach)
- Hidden-layer representational clustering
- Statistical learning framework
- Artificial grammar learning (AGL) framework

**Brain regions:**
- Medial prefrontal cortex (mPFC)
- Left inferior frontal gyrus (IFG)
- Right inferior frontal gyrus (IFG)
- Left insula
- Right insula
- Cuneus
- Left anterior temporal lobe (ATL)
- Left superior temporal gyrus (STG)

**Keywords:**
event segmentation, event representation, temporal community structure, statistical learning, fMRI adaptation, multivoxel pattern analysis, medial prefrontal cortex, inferior frontal gyrus, predictive learning, sequence learning, hidden-layer representations, connectionist model, artificial grammar learning, chunking, anterior temporal lobe, semantic cognition
