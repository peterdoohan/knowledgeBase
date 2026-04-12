---
source_file: eichenbaum2017_prefrontal_hippocampal_episodic.md
paper_id: eichenbaum2017_prefrontal_hippocampal_episodic
title: "Prefrontal–hippocampal interactions in episodic memory"
authors:
  - "Howard Eichenbaum"
year: 2017
journal: "Nature Reviews Neuroscience"
paper_type: review
contribution_type: review
species:
  - mouse
  - rat
methods:
  - optogenetics
  - electrophysiology
  - lesion
brain_regions:
  - hippocampus
  - hippocampus_ca1
  - entorhinal_cortex
  - medial_entorhinal_cortex
  - lateral_entorhinal_cortex
  - prefrontal_cortex
  - medial_prefrontal_cortex
  - orbitofrontal_cortex
  - thalamus
  - ventral_hippocampus
keywords:
  - prefrontalhippocampal_interactions
  - episodic_memory_retrieval
  - theta_oscillatory_synchrony
  - nucleus_reuniens
  - ventral_hippocampus
  - context_guided_memory
  - bidirectional_information_flow
  - top_down_memory_control
  - oscillatory_coherence
  - memory_interference_suppression
  - hippocampal_conjunctive_coding
  - remote_memory_consolidation
  - prefrontalhippocampal
  - interactions
  - episodic
  - memory
key_citations:
  - jadhav2016_hippocampal_prefrontal_swr
wiki_pages:
  - wiki/topics/hippocampal_prefrontal_replay_in_planning
---

### One-line summary

This review synthesises evidence on the complementary roles of the hippocampus and medial prefrontal cortex (mPFC) in episodic memory, proposing a circuit model in which the nucleus reuniens coordinates bidirectional, stage-dependent information flow: ventral hippocampus sends contextual cues to mPFC during encoding/delay, while mPFC exerts top-down retrieval control over dorsal hippocampus via perirhinal and entorhinal cortex.

---

### Background & motivation

The hippocampus and PFC have each been individually implicated in episodic memory, but their interactions — and the specific pathways mediating those interactions — remained poorly characterised until recently. Classic neuropsychological dissociations established that hippocampal damage impairs new episodic encoding while PFC damage causes source-confusion and intrusion errors rather than outright amnesia, suggesting complementary rather than redundant roles. The emergence of optogenetic, chemogenetic, and electrophysiological tools in rodents created an opportunity to ask which specific pathways carry which signals, and at which stage of a memory trial. This review integrates that new work into a unified circuit-level model.

---

### Methods

This is a narrative review. Key features of the literature reviewed:

- **Scope**: Studies in rodents (rat and mouse), non-human primates, and humans; covers lesion/disconnection studies, single-unit electrophysiology, LFP oscillatory synchrony analyses, optogenetics, chemogenetics, and human neuroimaging/MEG.
- **Behavioural paradigms covered**: Context-guided object–reward association tasks, delayed non-match/match to place, delayed spatial alternation, plus-maze place vs. response learning, contextual fear conditioning, object exploration (recency/location), and odour list-learning tasks.
- **Anatomical focus**: Three mPFC–hippocampal pathways in rodents — direct vHPC→mPFC projection, bidirectional thalamic pathway via nucleus reuniens (Re), and bidirectional cortical pathway via perirhinal cortex (PRC) and lateral entorhinal cortex (LEC).
- **Synthesis method**: Narrative integration; no formal inclusion criteria or meta-analytic statistics.

---

### Key findings

- The hippocampus (especially dorsal) is necessary for encoding and retrieving context-specific episodic memories; the mPFC is necessary for suppressing intrusions from competing (contextually inappropriate) memories. Hippocampal lesions reduce hits; mPFC lesions increase false alarms in the same odour-list task.
- Crossed-lesion (disconnection) experiments in rats demonstrate that an intact ipsilateral mPFC–hippocampal pathway is both necessary and sufficient for episodic memory performance across multiple task paradigms.
- Strong theta-band (4–12 Hz) oscillatory coherence between mPFC and hippocampus correlates with accurate memory; coherence is higher during correct than error trials even when overt behaviour is matched.
- Information flow is directional and phase-dependent: hippocampal theta precedes mPFC theta by ~30 ms during context presentation and memory delays (hippocampus→mPFC), whereas mPFC leads hippocampus by ~30 ms during choice/retrieval (mPFC→hippocampus). These 30 ms leads correspond approximately to one gamma cycle.
- Optogenetic inactivation of vHPC terminals in mPFC during the sample phase (but not delay or choice phase) disrupts mPFC place coding and subsequent choice accuracy, confirming the direct vHPC→mPFC pathway is specifically engaged for context encoding.
- Inactivation of the mPFC-to-Re pathway causes overgeneralisation of contextual fear but does not impair fear acquisition per se; Re inactivation abolishes bidirectional mPFC–hippocampal functional connectivity and eliminates CA1 trajectory-specific rate coding.
- Bilateral mPFC inactivation specifically degrades object selectivity (not spatial specificity) of dHPC CA1 neurons; MEC inactivation causes broader remapping, suggesting MEC sets the overall organisational framework while mPFC sharpens object-specific representations.
- Remote memory consolidation: mPFC engagement is initially low after learning but increases over days, eventually becoming necessary for retrieval of remotely acquired memories; early plasticity markers are present in mPFC even before it becomes functionally required.
- The proposed model has potential translational relevance to schizophrenia, where reduced PFC–hippocampal connectivity and impaired context-guided retrieval are prominent features.

---

### Computational framework

Not applicable in the strict sense — no formal computational or mathematical model is presented. However, the review implicitly operates within a **cognitive control / top-down gating** framework:

- **What is being modelled (conceptually)**: Context-guided memory retrieval, in which a current contextual cue must selectively bias access to relevant stored representations while suppressing competing ones.
- **Key quantities**: Direction and timing of inter-regional information flow (phase leads in theta/gamma oscillations as proxies); firing-rate selectivity of hippocampal place/object cells; oscillatory coherence as a measure of functional coupling.
- **Assumptions**: Oscillatory synchrony implements selective routing of information between areas; the theta cycle provides a temporal scaffold within which gamma-nested packets of information are transferred in a directional manner; the Re acts as a synchronisation hub rather than a content-bearing relay.

The framework most closely resembles **oscillatory communication-through-coherence** (Fries 2005-style), combined with a hierarchical control account in which abstract contextual/rule representations in mPFC gate specific memory expressions in hippocampus. The results would constrain models of prefrontal-mediated gating of hippocampal output (e.g., attractor models of CA3/CA1 pattern completion) and oscillatory models of inter-regional coupling.

---

### Prevailing model of the system under study

Prior to this review, the dominant picture was one of anatomical and functional separability: the hippocampus forms and retrieves contextual/episodic memories, the PFC exerts strategic control (source monitoring, interference suppression, rule switching), and the two communicate — but the nature, directionality, and pathway-specificity of that communication were largely uncharacterised. The existence of PFC–hippocampal interactions was well-established through lesion and imaging work, and oscillatory coherence had been reported in several studies. What was missing was an account of which pathway carries what signal at what stage of memory processing, and how the system as a whole is coordinated.

The "railroad" metaphor from Miller and Cohen (2001) — hippocampus lays tracks, PFC switches between them — had been influential, but remained metaphorical without circuit-level specificity.

---

### What this paper contributes

This review synthesises the first wave of pathway-specific, tool-based studies into an explicit circuit model:

1. **vHPC→mPFC (direct)**: Carries contextual cue information to mPFC at encoding; functionally engaged specifically during the sample/encoding phase, not during delay or retrieval.
2. **Re-mediated (bidirectional)**: Serves as a synchronisation hub that coordinates the direction of inter-areal communication at each memory stage; modulatory rather than content-bearing.
3. **mPFC→PRC/LEC→dHPC (indirect cortical)**: The route for top-down mPFC control over retrieval; mPFC sharpens object-specific (but not spatial) representations in dHPC by gating entorhinal input, suppressing irrelevant representations.

The model reframes PFC–hippocampal interaction from a static complementarity to a dynamic, stage-dependent dialogue in which the direction of functional connectivity is reversed between encoding/delay and retrieval. It also clarifies that the vHPC specifically (not dHPC) is the hippocampal locus of input to PFC, consistent with the broader spatial coding of vHPC neurons. Key unresolved questions identified: the specific functional role of the PRC/LEC bidirectional pathway has not been directly tested; variation in synchronising frequencies across behavioural paradigms is unexplained; the contributions of mPFC during initial learning vs. remote memory consolidation remain speculative.

---

### Brain regions & systems

- **Hippocampus (dorsal, dHPC)** — encodes and retrieves context-specific episodic memories; contains place cells and object–place conjunctive cells; recipient of mPFC top-down control during retrieval.
- **Hippocampus (ventral, vHPC)** — broad spatial/contextual coding; source of direct monosynaptic projection to mPFC; conveys global contextual cues rather than detailed episodic content.
- **Medial prefrontal cortex (mPFC; prelimbic, infralimbic, anterior cingulate in rodents)** — suppresses contextually inappropriate memories; develops abstract rule/context representations; exerts top-down control over hippocampal object selectivity; increasingly engaged during remote memory retrieval.
- **Nucleus reuniens (Re) of midline thalamus** — bidirectional relay between mPFC and hippocampal CA1; coordinates synchrony and controls the direction of inter-areal information transfer; modulatory role rather than content-bearing.
- **Perirhinal cortex (PRC) and lateral entorhinal cortex (LEC)** — bidirectional cortical intermediaries for mPFC→hippocampus top-down pathway; encode specific objects and events; proposed locus at which mPFC suppresses competing representations before they enter hippocampus.
- **Medial entorhinal cortex (MEC)** — sets the overall organisational framework for CA1 spatial/contextual representations; distinct from the object-selective role of LEC.
- **Orbital PFC (OFC)** — receives direct vHPC input; distinguished from mPFC proper in its role in reward contingency switching.

---

### Mechanistic insight

This paper does not fully meet the dual bar (formal algorithm + direct neural data supporting that algorithm over alternatives). It is a review that assembles converging evidence from multiple independent studies rather than presenting a single dataset.

That said, the body of evidence reviewed comes close to meeting the bar for the theta-phase communication mechanism:

- **Computational level**: The brain must selectively activate the contextually appropriate memory representation among competing alternatives, using a current contextual cue or recent experience as the selection signal.
- **Algorithmic level**: Context information is transferred from vHPC to mPFC during encoding/delay (hippocampus-leading theta coherence ~30 ms lead); during retrieval, mPFC transmits top-down selection/suppression signals to hippocampus via entorhinal gating (mPFC-leading theta ~30 ms). The ~30 ms lead corresponds to one gamma cycle, suggesting gamma-nested information packets within theta frames.
- **Implementational level**: Partially addressed — the Re is identified as the synchronisation coordinator (optogenetic and muscimol data); the direct vHPC terminal projection is isolated optogenetically; mPFC projections to superficial layers of PRC and deep layers of LEC are anatomically characterised. Specific cell types within circuits are not addressed. The bonus criterion (cell types, neuromodulators) is not met.

The main gap is that no single study reviewed simultaneously records from all nodes, manipulates a specific pathway, and demonstrates that the *algorithmic specificity* of the model (directional reversal, gamma-nested packets) is causally necessary. The evidence is convergent across separate experiments rather than internally controlled.

---

### Limitations & open questions

- The functional role of the bidirectional PRC/LEC cortical pathway has not been directly tested; the model makes specific predictions (mPFC inactivation should reduce PRC/LEC memory specificity; PRC/LEC inactivation should reduce dHPC stimulus specificity) that remain untested.
- The synchronising frequency band during choice/retrieval differs between the two key studies reviewed (gamma vs. theta lead from mPFC), and the reason is unclear; a more systematic analysis of which frequencies carry signals in which paradigms is needed.
- Comparative anatomy between rodent mPFC and primate dlPFC/vmPFC remains unresolved; functional parallels support some homology but the absence of a granular layer in rodents complicates direct comparison.
- The mechanisms underlying remote memory consolidation — specifically the temporal transition from hippocampal to mPFC dependency — are speculative. The proposed account (competition between memories increases over time, making mPFC integration increasingly necessary) is presented as highly tentative.
- The role of sharp-wave ripples and offline consolidation (sleep replay) in this PFC–hippocampal system is not addressed.
- The model is built primarily from rodent data; generalisation to primates and humans is supported by limited evidence (one MEG study on relational inference).

---

### Connections & keywords

**Key citations**:
- Miller, E. K. & Cohen, J. D. (2001) — integrative theory of PFC function ("railroad" metaphor)
- Preston, A. R. & Eichenbaum, H. (2013) — interplay of hippocampus and PFC in memory
- Komorowski et al. (2009) — conjunctive item–place coding by hippocampal neurons
- Jadhav et al. (2016) — coordinated PFC excitation/inhibition during hippocampal SWRs
- Vertes, R. P. (2002, 2006, 2007) — anatomy of Re and mPFC–hippocampal projections
- Guise & Shapiro (2017) — mPFC reduces memory interference by modifying hippocampal encoding
- Farovik et al. (2008) — mPFC supports recollection but not familiarity
- Fortin et al. (2004) — hippocampus-dependent recollection-like memory in rats

**Named models or frameworks**:
- Miller & Cohen (2001) "railroad" metaphor of PFC–hippocampal complementarity
- Communication-through-coherence (oscillatory synchrony as information routing)
- Context-guided memory retrieval model (proposed here; Figure 4)

**Brain regions**:
- Dorsal hippocampus (dHPC)
- Ventral hippocampus (vHPC)
- Medial prefrontal cortex (mPFC; prelimbic, infralimbic, anterior cingulate)
- Nucleus reuniens (Re)
- Perirhinal cortex (PRC)
- Lateral entorhinal cortex (LEC)
- Medial entorhinal cortex (MEC)
- Orbital PFC (OFC)

**Keywords**:
- prefrontal–hippocampal interactions
- episodic memory retrieval
- theta oscillatory synchrony
- nucleus reuniens
- ventral hippocampus
- context-guided memory
- bidirectional information flow
- top-down memory control
- oscillatory coherence
- memory interference suppression
- hippocampal conjunctive coding
- remote memory consolidation

### Related wiki pages
- [[wiki/topics/hippocampal_prefrontal_replay_in_planning|Hippocampal–prefrontal replay in planning]]
