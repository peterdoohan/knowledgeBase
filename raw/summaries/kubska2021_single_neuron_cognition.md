---
source_file: kubska2021_single_neuron_cognition.md
title: "How Human Single-Neuron Recordings Can Help Us Understand Cognition: Insights from Memory Studies"
authors: Zuzanna Roma Kubska, Jan Kaminski
year: 2021
journal: Brain Sciences
paper_type: review
contribution_type: review
---

### One-line summary

This review synthesises what human single-neuron recordings have revealed about the cellular bases of long-term memory and working memory, focusing on concept cells, novelty-dependent neurons, and persistent activity, and outlines future research directions enabled by this technique.

---

### Background & motivation

Understanding human cognition requires methods that can resolve individual-neuron activity, because noninvasive techniques (fMRI, EEG, MEG) face irresolvable trade-offs between spatial and temporal resolution and cannot directly distinguish excitatory from inhibitory activity. Animal electrophysiology, while providing cellular-level resolution, cannot capture cognitive processes unique to humans (language, theory of mind, complex working memory) and is limited by the need for simplified tasks and long training regimes. Human single-neuron recordings — obtained opportunistically from epilepsy monitoring and deep brain stimulation (DBS) surgery patients — offer perfect spatial and temporal resolution with direct access to the human brain, but this literature is scattered across many primary studies. This review consolidates findings from that literature, contextualises them within major cognitive theories, and identifies open questions that only this technique can resolve.

---

### Methods

This is a narrative review. Scope and synthesis approach:

- Covers primary human single-neuron recording studies published from approximately 2005 to 2021, drawing mainly on epilepsy monitoring (Behnke-Fried hybrid electrodes) and DBS surgery cohorts.
- Organises findings thematically: (1) concept/grandmother cells, (2) long-term memory (LTM) encoding and novelty detection, (3) working memory (WM) maintenance via persistent activity.
- No formal inclusion/exclusion criteria or meta-analytic statistics are reported; synthesis is narrative and theory-driven.
- Also reviews electrode technology developments and discusses implications for studying pathological brains (temporal lobe epilepsy, Parkinson's disease, essential tremor).

---

### Key findings

- **Concept cells** (medial temporal lobe, MTL): Single MTL neurons respond to the semantic concept of a person or object regardless of sensory modality or visual format (images, sketches, written/spoken names). They are not found in other species to date and reflect perceptual decisions and conscious recognition rather than low-level visual features (Quian Quiroga et al., 2005, 2009, 2014).
- **Rapid associative encoding**: After brief exposure to photoshopped composite images, concept cells rapidly expand their tuning to fire to newly associated stimuli — direct cellular evidence for one-shot associative encoding in MTL (Ison et al., 2015).
- **Novelty-dependent neurons**: Populations of neurons in the hippocampus/amygdala, substantia nigra (SN), and posterior parietal cortex (PPC) signal novelty vs. familiarity independent of stimulus category. SN novelty neurons have longer response latency than hippocampal ones, consistent with a hippocampal-SN/VTA loop in which initial novelty screening in the hippocampus is relayed to dopaminergic midbrain circuits (Kaminski et al., 2018; Rutishauser et al., 2006, 2008, 2010).
- **Persistent activity in WM**: Concept cells (stimulus-specific) in MTL and maintenance neurons (non-stimulus-specific) in medial frontal cortex (dACC/preSMA) sustain firing throughout the WM delay period. Persistent activity magnitude predicts behavioral accuracy and decreases as a function of WM load. These are the first direct demonstrations of persistent activity as a WM maintenance mechanism in humans (Kaminski et al., 2017; Kornblith et al., 2017).
- **Phase coding**: The phase of slow oscillations at which a neuron fires can be used to read out WM content — combined phase-rate coding enables multiple items to be multiplexed across oscillatory cycles (Kaminski et al., 2020).
- **Hippocampal-cortical coupling**: Persistent hippocampal activity is coupled with scalp EEG, and this coupling increases with WM load, supporting a distributed account of WM (Boran et al., 2019).
- **PPC in memory-based decisions**: Two distinct populations in PPC — memory-selective novelty-dependent neurons and confidence-selective neurons — support memory-guided choices, demonstrating a direct cellular substrate for declarative memory influencing decision-making (Rutishauser et al., 2018).

---

### Computational framework

Not applicable in the strict sense — the paper is a narrative review and does not develop or apply a computational model. However, several theoretical frameworks are discussed and used to interpret the single-neuron data:

- **Hierarchical sparse coding**: Concept cells are interpreted as the top of a cortical representational hierarchy in which higher levels encode increasingly abstract and multimodal features, consistent with sparse, invariant coding theories (Olshausen & Field; Quian Quiroga).
- **Hippocampal-VTA/SN loop (Lisman & Grace)**: A functional circuit model in which hippocampal novelty signals drive dopaminergic novelty cells in SN/VTA, which in turn gate LTP and memory consolidation via dopamine feedback. Single-neuron data from both hippocampus and SN are framed as direct evidence for this loop.
- **Persistent activity framework for WM**: The classic framework (from animal prefrontal physiology) positing that neurons maintain WM representations by sustaining elevated firing rates throughout the delay period. Human data confirm this mechanism but extend it to MTL and frontal midline structures.
- **Phase coding / oscillatory multiplexing**: The Lisman-Idiart theta-subcycle model, in which items are encoded at distinct phases of theta, is implicitly invoked to interpret the Kaminski et al. phase-rate coding finding.

---

### Prevailing model of the system under study

The paper's introduction frames three main unsettled debates:

1. **Working memory architecture**: Baddeley & Hitch's domain-specific model (separate phonological loop and visuospatial sketchpad) versus Cowan's domain-general, attention-centric model. Even WM capacity is contested: 7±2 (Miller), ~4 chunks (Cowan), or 1 item in the focus of attention (Oberauer).
2. **Neural basis of memory**: MTL/hippocampus was established as critical for LTM formation (lesion data from H.M. and others), and animal electrophysiology in prefrontal and hippocampal areas had identified persistent activity as a candidate WM mechanism — but this had not been directly demonstrated in humans at the single-neuron level.
3. **Sparse vs. distributed coding at the apex of the visual hierarchy**: Theories of "grandmother cells" (Lettvin) and "gnostic cells" (Konorski) predicted highly selective cells for complex concepts at the top of the cortical hierarchy, but the existence of such cells in humans had been an open empirical question until the Quian Quiroga et al. (2005) discovery.

The baseline assumption was that noninvasive and animal methods were the primary tools, and that translating animal WM/memory physiology to humans was only weakly constrained by empirical data.

---

### What this paper contributes

The review establishes that human single-neuron recordings have, over roughly 15 years, provided four categories of otherwise-unobtainable evidence:

1. **Concept cells exist and are probably human-specific**: MTL neurons encode semantic concepts in a modality-invariant, association-based manner consistent with Konorski's gnostic cell hypothesis but distinct from simpler "grandmother cell" accounts. Their link to conscious perception and associative LTM encoding is now empirically grounded at the cellular level.
2. **Rapid one-shot associative encoding has a cellular correlate**: Individual concept cells update their tuning within a single session, providing a mechanistic foothold for rapid episodic encoding.
3. **Persistent activity is a confirmed WM maintenance mechanism in humans**: Stimulus-specific MTL neurons and non-stimulus-specific frontal neurons sustain activity during WM delays in a load-dependent, behaviorally predictive manner — directly extending animal findings to the human brain and to cognitive loads/tasks impossible in animals.
4. **Dopaminergic novelty signalling has a single-unit substrate in humans**: SN neurons with putative dopaminergic identity respond to novelty with longer latencies than hippocampal neurons, providing cellular-level support for the Lisman-Grace hippocampal-VTA loop.

The paper also identifies what remains unresolved: WM capacity limits, domain-generality vs. domain-specificity of WM maintenance, and the cellular mechanisms disrupted in epilepsy, PD, and ET.

---

### Brain regions & systems

- **Medial temporal lobe (MTL)** — primary locus of concept cells and novelty-dependent neurons; involved in associative encoding, conscious recognition, and WM maintenance.
- **Hippocampus** — highest node in MTL hierarchy; episodic memory, novelty/familiarity detection, WM persistent activity, phase coding of WM content.
- **Amygdala** — part of MTL complex where novelty-dependent neurons are also found.
- **Substantia nigra (SN)** — dopaminergic novelty-sensitive neurons; relays hippocampal novelty signals; role in LTP gating and memory consolidation via hippocampal-SN/VTA loop.
- **Ventral tegmental area (VTA)** — dopaminergic partner to SN in the Lisman-Grace loop; not directly recorded in the reviewed studies but invoked theoretically.
- **Medial frontal cortex / dACC / preSMA** — non-stimulus-selective WM maintenance neurons; proposed locus of central executive / attentional control component of WM.
- **Dorsolateral prefrontal cortex (dlPFC)** — recordings via DBS trajectories show neurons encoding abstract rules and subjective decisions; identified as an important future target.
- **Posterior parietal cortex (PPC)** — memory-selective novelty-dependent neurons and confidence-selective neurons; declarative memory influencing memory-based choice.
- **Basal ganglia (striatum, subthalamic nucleus)** — implicated in modulating novelty-dependent signals from frontal inputs; accessible via DBS trajectories; identified as a future research target.
- **Entorhinal cortex** — mentioned in context of new electrode technology (grid cell recordings); not a focus of the memory findings reviewed.

---

### Mechanistic insight

The paper partially meets the bar. It reviews studies that both propose algorithms (persistent activity for WM maintenance; hippocampal-SN/VTA novelty loop for LTM gating; phase coding for WM multiplexing) and provide supporting single-neuron data from humans. However, as a review, it does not pit these algorithms against alternatives in a single controlled design. The strongest mechanistic chain in the reviewed literature is:

- **Computational (what problem is being solved)**: Maintain a stimulus-specific WM representation over a delay period; gate which novel stimuli enter LTM.
- **Algorithmic (representations and processes)**: Persistent firing of concept cells (stimulus-specific) and maintenance neurons (load-tracking) during the delay period, combined with phase coding across theta cycles to multiplex multiple items. For LTM gating: hippocampal novelty signals drive dopaminergic SN neurons, which release dopamine back to the hippocampus to modulate LTP.
- **Implementational**: Sparse, high-impedance microwire recordings identify putative pyramidal cells (broad spike waveforms) in MTL and frontal midline as the cellular substrate of WM persistence. In SN, neurons with long spike waveforms — consistent with dopaminergic identity verified in animal optogenetics studies — are the candidate implementation of novelty-gating.

**Bonus**: The paper notes the putative dopaminergic identity of SN novelty neurons (spike waveform analysis) and the coupling of single-unit persistent activity to hippocampal and scalp theta oscillations, touching on biophysical implementation.

Caveat: the reviewed studies cannot fully rule out alternative WM mechanisms (activity-silent synaptic storage) because the recording technique is limited to a small, sparse sample of neurons; absence of persistent activity in unsampled neurons cannot be excluded.

---

### Limitations & open questions

- **Pathological brain**: All recordings are in patients undergoing surgery for epilepsy, PD, or ET. Although evidence suggests the recorded activity in non-epileptic tissue is not substantially different from healthy brain activity, this cannot be definitively confirmed.
- **Sparse sampling**: Only a tiny fraction of neurons is recorded; absence of persistent activity in unsampled populations cannot be excluded, leaving alternative WM mechanisms (e.g., activity-silent synaptic tagging) open.
- **Limited brain coverage**: Electrode placement is dictated by clinical necessity, restricting access to frontal and other regions outside standard implantation sites. DBS surgery offers access to frontal cortex and basal ganglia but this is not yet extensively exploited.
- **WM capacity unresolved**: Whether the limit is 7±2, ~4, or 1 item cannot yet be determined from existing single-neuron data; load-dependent decreases in persistent activity hint at a capacity signature, but a definitive test requires new experimental designs.
- **Domain generality vs. specificity of WM**: Whether the same cells maintain information from different sensory modalities (domain-general account) or separate populations handle different modalities (domain-specific account) has not been tested with single-neuron recordings.
- **Mechanism of high-speed serial scanning (Sternberg task)**: Whether load-dependent response times reflect a serial exhaustive search process can in principle be tested at the single-neuron level but has not been done.
- **Pathological mechanisms in TLE, PD, ET**: The cellular mechanisms by which interictal epileptiform discharges (IEDs) disrupt familiarity-based recognition, and how neurodegeneration in basal ganglia impairs the hippocampal-SN/VTA loop in PD, remain open and are proposed as future research directions.
- **Electrode technology lag**: Behnke-Fried electrodes remain the standard despite being introduced in the 1990s; newer technologies (NeuroGrid, linear probes, tetrode-depth hybrids) are not yet approved for widespread clinical use.

---

### Connections & keywords

**Key citations:**
- Quian Quiroga et al. (2005) *Nature* — original concept cell discovery (Jennifer Aniston neuron)
- Quian Quiroga et al. (2009) *Current Biology* — multimodal encoding by single MTL neurons
- Quian Quiroga (2012) *Nature Reviews Neuroscience* — concept cells review
- Ison et al. (2015) *Neuron* — rapid one-shot associative encoding by concept cells
- Kaminski et al. (2017) *Nature Neuroscience* — first evidence for persistent activity in human WM
- Kornblith et al. (2017) *Current Biology* — concurrent human MTL persistent activity in WM
- Kaminski et al. (2018) *Current Biology* — novelty-sensitive dopaminergic neurons in human SN
- Rutishauser et al. (2006, 2008, 2010) — novelty-dependent neurons in human hippocampus/amygdala
- Rutishauser et al. (2018) *Neuron* — memory strength and confidence neurons in human PPC
- Lisman & Grace (2005) *Neuron* — hippocampal-VTA loop model
- Kaminski et al. (2020) *Neuron* — phase-rate coding in human WM
- Boran et al. (2019) *Science Advances* — hippocampal persistent activity and cortical coupling in WM
- Baddeley & Hitch (1974); Cowan (2001); Oberauer (2002) — competing WM models

**Named models or frameworks:**
- Lisman-Grace hippocampal-VTA/SN loop
- Baddeley-Hitch working memory model
- Cowan's embedded processes model of WM
- Behnke-Fried hybrid electrode (recording technology)
- NeuroGrid (emerging electrode technology)
- Sternberg high-speed serial exhaustive scanning (SES) paradigm

**Brain regions:**
- Medial temporal lobe (MTL), hippocampus, amygdala, substantia nigra (SN), ventral tegmental area (VTA), medial frontal cortex (dACC, preSMA), dorsolateral prefrontal cortex (dlPFC), posterior parietal cortex (PPC), basal ganglia, entorhinal cortex

**Keywords:**
- human single-neuron recordings
- concept cells
- medial temporal lobe memory
- persistent activity working memory
- novelty-dependent neurons
- hippocampal-VTA dopamine loop
- WM capacity working memory
- phase coding theta oscillations
- Behnke-Fried electrode epilepsy monitoring
- deep brain stimulation cognitive neuroscience
- sparse invariant neural coding
- pathological brain single-unit recording
