---
source_file: baker2022_representation_neuroscience_three_aspects.md
paper_id: baker2022_representation_neuroscience_three_aspects
title: "Three aspects of representation in neuroscience"
authors:
  - "Ben Baker"
  - "Benjamin Lansdell"
  - "Konrad P. Kording"
year: 2022
journal: "Trends in Cognitive Sciences"
paper_type: review
contribution_type: theoretical
species:
  - human
methods:
  - computational_modeling
brain_regions:
  - hippocampus
  - visual_cortex
frameworks:
  - reinforcement_learning
keywords:
  - neural_representation
  - teleology
  - causal_role
  - correlation
  - misrepresentation
  - neural_coding
  - philosophy_of_neuroscience
  - mechanistic_explanation
  - teleosemantics
  - representation_hunger
  - c_elegans_chemotaxis
  - sparse_coding
  - three
  - aspects
  - representation
  - neuroscience
---

### One-line summary

This paper argues that a rigorous account of neural representation requires three jointly necessary aspects — correlation, causal role, and teleology — and shows how each is grounded in both philosophical theory and common neuroscientific practice.

---

### Background & motivation

The term "representation" is ubiquitous in neuroscience yet lacks a widely agreed-upon definition; a survey of researchers revealed substantial variation in what the term is taken to imply, and recent theoretical work has identified a gap between what representation claims suggest and what experimental evidence typically supports. This inconsistency causes neuroscientists to talk past one another: two researchers may nominally agree that neural activity represents feature F while holding deeply incompatible views about what that entails for perception or cognition. Meanwhile, philosophy of mind has developed extensive, rigorous accounts of representation that neuroscience has largely failed to engage with. The paper aims to bridge this gap by articulating a three-aspect account that can serve as a reference for future empirical and theoretical work.

---

### Methods

This is a theoretical/conceptual review employing the following approach:

- Synthesis of neuroscientific literature across three contexts in which representation is invoked: (1) correlational studies of neural activity and environmental features, (2) behavioral inference of internal representations, and (3) algorithmic or computational accounts of cognition.
- Broad engagement with philosophical literature on representation, intentionality, teleology, mechanistic explanation, and misrepresentation, spanning analytic philosophy of mind, ancient and early modern philosophy, and philosophy of science.
- Repeated use of a single running example — chemotaxis in *C. elegans* (Soh et al. 2018) — to concretely illustrate each of the three aspects and their interactions.
- Additional examples include motion perception in humans, place cells in the hippocampus, looming-stimulus avoidance, and visual representations of faces.

---

### Key findings

- Correlation alone (Aspect 1) is insufficient for representation: any neural process will correlate with countless environmental features it does not represent; no purely statistical measure can determine semantic content.
- Causal role (Aspect 2) is required to distinguish the specific neural activity that implements the representation from the broader set of activity that merely carries correlated information; only the causally relevant part explains how blocking or inducing activity changes behavior.
- Teleology (Aspect 3) is required to account for misrepresentation: a representation of F can be wrong, which presupposes a goal or purpose that the representation is supposed to serve — a standard of correctness absent from correlation and causation alone.
- These three aspects map onto the three main investigative contexts already present in neuroscience (stimulus–response correlations, behavior-based inference, and algorithm-level modelling) but each aspect is relevant across all three contexts.
- In practice, most systems neuroscience experiments address only Aspect 1; Aspect 2 is studied by causal perturbation methods (optogenetics, lesions, stimulation); Aspect 3 is often implicit but is foregrounded by evolutionary/phylogenetic approaches, inverse RL, and efficient-coding frameworks.
- For simple organisms (e.g., *C. elegans*) where the behavioral repertoire is narrow and purposes unambiguous, implicit teleology causes little harm; in complex organisms studying abstract representations (e.g., hippocampus), unstated teleological assumptions generate significant ambiguity.
- The paper identifies a legitimate dissenting view (Box 4) in which representation is equated with encoding/information (Aspect 1 only), and argues this deflates the explanatory role that "representation" is meant to play.

---

### Computational framework

The paper does not introduce or apply a single computational model. It engages with several computational framings as examples and object of analysis:

- **Shannon information theory / neural coding**: the paper discusses the encode-decode metaphor and its limitations as a full account of representation.
- **Marr's three levels**: the paper references Marr's framework (computational, algorithmic, implementational) as a context in which representation at the algorithmic level is central.
- **Reinforcement learning / inverse RL**: cited as an approach that foregrounds teleology by inferring goals from behavior.
- **Efficient coding / sparse coding**: cited as an approach that makes teleological commitments explicit (V1 as optimising sparse representation of natural scenes).
- **Deep neural networks as brain models**: cited as approaches linking task-defined teleology to neural architecture.

The core formal claim is conceptual rather than mathematical: a neural state N is a representation of feature F if and only if (i) N correlates with F, (ii) this correlation plays a distinctive causal role in F-related behavior within a mechanistic account, and (iii) there is a goal or purpose such that N is supposed to correlate with F, grounding the possibility of misrepresentation.

---

### Prevailing model of the system under study

The paper does not study a specific brain region or system; it studies the concept of neural representation across neuroscience as a discipline. The prevailing model it pushes against is an implicit one: the dominant practice in systems neuroscience of treating correlation between neural activity and an external variable as sufficient (or nearly sufficient) evidence for a neural representation of that variable. This is operationalised through tuning curve analysis, decoding/MVPA, and information-theoretic measures, and is tacitly assumed to support claims about what the brain "encodes" or "represents." The paper's introduction cites several authors (Brette 2018; Kragel et al. 2018; Ritchie et al. 2019; Mirski & Bickhard 2019) who have raised concerns about this correlational practice, and a survey (Vilarroya 2017) documenting the lack of consensus.

---

### What this paper contributes

The paper establishes that the explanatory role typically assigned to neural representations in neuroscience implicitly commits researchers to all three aspects (correlation, causal role, teleology), even when experiments only directly address Aspect 1. This has several concrete consequences:

- Claims about representation should be more limited or explicitly conditional when causal evidence is lacking or when the teleological framework is unspecified.
- Misrepresentation — essential to explaining perceptual errors and illusions — cannot be grounded in correlation or even causation alone; it requires a normative standard provided by teleology.
- The framework helps adjudicate apparent disputes about what some neural activity "really" represents by clarifying which aspect is actually contested.
- It provides a vocabulary for cross-disciplinary communication between neuroscience, philosophy, AI, and cognitive science.
- For complex systems (hippocampus, prefrontal cortex), the paper recommends that researchers be explicit and provisional about teleological assumptions rather than treating them as background.

---

### Brain regions & systems

The paper does not focus on any single brain region; brain regions appear as illustrative examples:

- **Lateral intraparietal cortex (LIP)** — used as an example of representing an internal algorithmic variable (accumulated evidence) rather than an external stimulus; discussed in Box 1.
- **Primary visual cortex (V1)** — classic example of correlational representation (Hubel & Wiesel receptive fields); also invoked in efficient-coding / sparse coding context.
- **Hippocampus / place cells** — used as a case where teleological ambiguity is substantial: place cells may represent spatial layout, but whether their function is navigation, exploration, memory consolidation, planning, or imagination remains unsettled.
- **C. elegans interneurons** — the paper's main running example (Soh et al. 2018); interneurons representing NaCl gradient direction illustrate each of the three aspects in turn.

---

### Mechanistic insight

The paper does not meet the bar for this section. It is a conceptual/theoretical review; it does not present original neural data and does not itself formalise or validate a specific algorithm linking measured neural activity to a computational process. It engages extensively with mechanistic explanation as a concept but does not provide empirical evidence for any specific representational mechanism.

The paper's framework does, however, articulate what mechanistic insight in neuroscience would require: evidence addressing all three aspects, i.e., showing that a neural state correlates with a content (Aspect 1), that causal perturbation of that state specifically alters content-related behavior (Aspect 2), and that this is situated within a teleological account that grounds what counts as correct and incorrect processing (Aspect 3). The running *C. elegans* example illustrates this structure at the conceptual level.

---

### Limitations & open questions

The paper explicitly flags the following as outstanding questions:

- What kinds of causal roles distinguish a representational neural state from one that is merely causally involved in behavior without representing anything?
- What experimental methods best discriminate between different causal roles that the same pattern of neural activity might play?
- Which teleological frameworks — backward-looking (etiological/evolutionary) or forward-looking (goal-contribution) — are appropriate for different subfields, scales of analysis, or organisms?
- How can performance standards (success vs. error) be operationalised and measured for different teleological frameworks?

Additional limitations implicit in the review:

- The account is conceptual and does not provide a formal criterion or decision procedure for empirically adjudicating representation claims.
- The paper acknowledges that resolving disputes about the precise causal role of specific neural activity is often intractable with current methods in complex organisms.
- The "problem of novel contents" for backward-looking teleology (representations of culturally novel objects) is acknowledged but not resolved.
- Conflicting or time-varying goals within a single organism (e.g., humans) complicate the forward-looking teleological account.

---

### Connections & keywords

**Key citations**:
- Brette (2018) — critique of the coding metaphor
- Kragel et al. (2018) — representation, pattern information, and brain signatures
- Ritchie et al. (2019) — limits of MVPA for representation claims
- Soh et al. (2018) — *C. elegans* chemotaxis computational model (running example)
- Marr (1982) — three levels of analysis
- Shea (2018) — *Representation in Cognitive Science* (philosophical framework)
- Millikan (1984, 1989) — proper functions and teleosemantics
- Dretske (1981, 1988) — information-based and causal accounts of representation
- Fodor (1987, 1990) — psychosemantics and causal theory of content
- Krakauer et al. (2017) — neuroscience needs behavior
- Cisek (2019) — phylogenetic refinement of behavior
- Yamins & DiCarlo (2016) — goal-driven deep learning models of sensory cortex
- Hubel & Wiesel (1959) — receptive fields in visual cortex

**Named models or frameworks**:
- Marr's three levels of analysis (computational / algorithmic / implementational)
- Teleosemantics (Millikan, Dretske, Neander)
- Shannon information theory / neural coding
- Sparse coding / efficient coding hypothesis (Olshausen & Field)
- Deep neural network models of visual cortex
- Inverse reinforcement learning (for teleology inference)
- *C. elegans* chemotaxis model (Soh et al. 2018)

**Brain regions**:
- Lateral intraparietal cortex (LIP)
- Primary visual cortex (V1)
- Hippocampus

**Keywords**: neural representation, teleology, causal role, correlation, misrepresentation, neural coding, philosophy of neuroscience, mechanistic explanation, teleosemantics, representation hunger, C. elegans chemotaxis, sparse coding
