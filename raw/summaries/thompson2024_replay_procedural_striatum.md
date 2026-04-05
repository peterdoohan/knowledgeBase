---
source_file: thompson2024_replay_procedural_striatum.md
title: Replay of procedural experience is independent of the hippocampus
authors: Emmett J. Thompson, Lars Rollik, Benjamin Waked, Georgina Mills, Jasvin Kaur, Ben Geva, Rodrigo Carrasco-Davis, Tom George, Clementine Domine, William Dorrell, Marcus Stephenson-Jones
year: 2024
journal: bioRxiv
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Replay of task-related neural sequences occurs in the dorsal striatum during sleep-dependent consolidation of procedural memory, and this replay is generated entirely independently of the hippocampus.

---

### Background & motivation

Sleep is critical for consolidating both episodic and procedural memories, with offline replay of neuronal firing patterns thought to be a core mechanism. While hippocampal replay is well-established as driving consolidation of declarative memories, procedural (non-declarative) memories do not require the hippocampus for learning or consolidation, leaving the mechanism driving their consolidation unknown. This paper investigates whether replay occurs in the dorsal striatum during procedural memory consolidation and whether it depends on the hippocampus.

---

### Methods

- **Behavioural task**: Multi-step procedural memory task where mice learned to nose-poke in the correct sequence of five ports to receive reward. Task had 50 training levels with progressive removal of visual guidance and intermediate rewards.
- **Subjects**: Adult male and female C57BL/6J mice (wild-type), 8-50 weeks old.
- **Lesions**: Bilateral DLS lesions (viral caspase strategy), DMS lesions (control), and bilateral hippocampal lesions (viral caspase) to test hippocampal independence.
- **Pharmacology**: NMDA receptor antagonist AP5 infused into DLS post-training to block offline plasticity.
- **Recordings**: Neuropixel 1.0 probes implanted through DLS to record neural activity during task execution and post-task sleep.
- **Replay detection**: PP-Seq (unsupervised point process model) adapted to detect neural sequences without template-based assumptions. Trained on awake data and applied to sleep recordings.
- **Analysis**: Bayesian decoding methods used for comparison/validation; sleep state classification using LFP and video tracking.

---

### Key findings

- **DLS is required for procedural learning**: DLS-lesioned mice showed impaired learning of the motor sequence from memory, while DMS lesions did not affect learning. Post-learning DLS lesions impaired task performance and increased movement variability.

- **Offline plasticity in DLS supports consolidation**: Infusing NMDA antagonist AP5 into DLS immediately after training significantly impaired performance the next day. AP5 infusions for 4 consecutive days in expert animals led to significant performance drops, indicating offline activity in DLS is critical for both learning and maintaining procedural memory.

- **Neural sequences in DLS during task execution**: Using PP-Seq, multiple distinct neural sequence types were identified in DLS during task performance. Different sequence types aligned to distinct phases of the behavioural sequence (port approaches, movements between ports). Neurons showed precise timing within sequences and were relatively sequence-specific.

- **Procedural replay occurs in DLS during sleep**: Awake-trained PP-Seq models applied to post-task sleep recordings revealed reactivation of task-related neural sequences. Replay events occurred at both real-world and time-compressed speeds (ranging from 5x slower to 20x faster than awake). Both forward and reverse replay were observed in roughly equal proportions.

- **Replay is prioritized**: Task-related sequences were more likely to be replayed than non-task sequences. Neurons that most consistently contributed to awake sequences were more likely to be involved in replay (non-linear relationship). Sequences preferentially involved central neurons rather than boundary neurons of each task-related sequence.

- **Compositionally structured replay**: Individual neural sequences could be replayed in isolation or in concatenated combinations. When concatenated, sequences were more likely to occur in the order they appeared during the behavioural sequence (task-ordered) than in random orders.

- **Hippocampal lesions do not affect procedural memory**: Mice with complete bilateral hippocampal lesions learned the procedural task normally, reaching expert levels in equivalent trials. Lesioned mice showed comparable movement speeds, error rates, and task focus to controls.

- **Striatal replay is independent of hippocampus**: All replay characteristics were preserved after hippocampal lesions: replay rate, length, extent, and decay; forward and reverse replay proportions; time-compressed vs. real-world speeds; compositional ordering; task-related replay proportion; and single neuron prioritization. No significant differences were found between lesioned and control groups on any replay measure.

---

### Computational framework

The study employs an unsupervised point process model (PP-Seq) for sequence detection. This is a probabilistic generative model that attributes individual neuronal spikes to latent causes (instances of particular neural sequences). The model uses iterative collapsed Gibbs sampling to fit parameters determining the number of latent events and attributes spikes to sequences based on features of activity (temporal offset, amplitude, and width). Unlike template-based approaches (Bayesian decoding), PP-Seq does not assume sequences progress linearly at constant speed, allowing detection of replay at variable speeds and in both forward and reverse directions. The model was trained on awake data and then applied to sleep recordings with fixed parameters to detect recapitulated sequences.

---

### Prevailing model of the system under study

The prevailing model in the field has been that the hippocampus is critical for active consolidation of all types of memory, including procedural memories. According to this view, the hippocampus triggers reactivation of cortical memory traces via replay during sleep, which strengthens these traces over time until they can be activated independently. Even for ultimately hippocampus-independent memories (like procedural skills), initial consolidation was thought to be organized by hippocampal dynamics. Hippocampal sharp-wave ripples (SWRs) were believed to drive or trigger replay in other regions including cortex and striatum. This model suggested a hierarchical memory system where the hippocampus serves as the central coordinator of offline consolidation across all memory types.

---

### What this paper contributes

This paper fundamentally challenges the prevailing model by demonstrating that procedural memory consolidation and replay in the dorsal striatum occur entirely independently of the hippocampus. The key contributions are:

1. **Establishing replay as a mechanism for procedural memory consolidation**: The study shows that neural sequences in the DLS that encode procedural actions are reactivated during post-task sleep, providing direct evidence for replay-based consolidation of procedural memory.

2. **Demonstrating hippocampal independence**: Complete bilateral hippocampal lesions had no effect on either procedural memory formation or any feature of striatal replay (rate, speed, direction, compositional ordering, or prioritization). This directly contradicts the model that hippocampus coordinates consolidation of all memory types.

3. **Revealing detailed replay features**: The study characterizes striatal replay as showing: (a) both real-world and time-compressed speeds; (b) forward and reverse replay; (c) prioritization of task-related sequences and consistently-firing neurons; (d) compositional structure where sequences replay individually or in task-ordered combinations.

4. **Methodological advance**: The adaptation of PP-Seq provides an unsupervised method for replay detection that outperforms template-based Bayesian decoding approaches and does not require assumptions about linear sequence progression or SWR biomarkers.

These findings support an alternative "parallel memory systems" view where declarative and procedural memories are consolidated independently, with replay as a common mechanism but different sources driving replay in distinct circuits.

---

### Brain regions & systems

- **Dorsolateral striatum (DLS)** — Primary region of focus. Required for learning and executing the procedural motor sequence. Site of offline replay during sleep. Shows NMDA-dependent plasticity critical for consolidation. Contains task-related neural sequences that align to distinct behavioural phases.

- **Dorsomedial striatum (DMS)** — Control lesion site. Lesions here did not impair procedural learning, demonstrating specificity of DLS involvement.

- **Hippocampus** — Complete bilateral lesions showed no effect on procedural memory formation or striatal replay characteristics. Demonstrates independence of procedural consolidation from hippocampal circuits.

- **Motor cortex** — Implicated as potential source of inputs to DLS; cortical-striatal connectivity is discussed as relevant for replay generation.

---

### Mechanistic insight

This paper provides substantial mechanistic insight into procedural memory consolidation, meeting both criteria: (1) it presents a formal algorithmic process (replay of neural sequences) and (2) it provides neural data supporting this algorithm. The findings map onto Marr's three levels as follows:

**Computational level**: The brain solves the problem of consolidating procedural motor skills during sleep. The goal is to strengthen task-relevant neural patterns to improve subsequent performance. The system prioritizes task-relevant sequences and consistently-firing neurons for reactivation, optimizing the consolidation process.

**Algorithmic level**: The consolidation mechanism involves reactivation (replay) of neural sequences that were active during task execution. These sequences are reactivated during sleep with specific algorithmic features: (a) sequences can replay at variable speeds (real-world to 20x compressed); (b) replay can occur in forward or reverse direction; (c) individual sequences or combinations can be replayed; (d) when combined, sequences tend to respect task order; (e) neurons that consistently fire in awake sequences are prioritized for replay. The PP-Seq algorithm formalizes this as a point process model where spikes are attributed to latent sequence events.

**Implementational level**: The implementation is in the dorsolateral striatum (DLS), specifically using NMDA-dependent plasticity. The replay is physically realized through reactivation of DLS neurons during sleep, with sequence timing preserved from awake activity. The mechanism does not require hippocampal input or coordination, suggesting intrinsic striatal or cortico-striatal circuit mechanisms can generate replay. The paper suggests future work should investigate coordination with dopamine release, as dopamine has been shown to have a causal role in offline memory consolidation.

---

### Limitations & open questions

- **Causal link not established**: While the study shows correlation between replay and consolidation, and shows NMDA-dependent plasticity is required, it does not prove that selectively disrupting replay itself (as opposed to other offline processes) impairs memory formation. Without a biomarker for striatal replay, closed-loop disruption as done in hippocampus is not currently possible.

- **Source of replay unknown**: The study demonstrates hippocampal independence but does not identify what generates striatal replay. Possible sources include intrinsic striatal circuits, cortical inputs (motor cortex), or other subcortical structures.

- **Dopamine coordination unexplored**: The paper notes that dopamine has a causal role in offline consolidation and that VTA neurons coordinate with hippocampal replay during quiet wakefulness. Whether striatal replay is coordinated with dopamine release remains to be investigated.

- **Generalization to other procedural tasks**: The study uses a specific multi-step motor sequence task. Whether similar replay mechanisms operate for other types of procedural learning (perceptual learning, habit formation, etc.) requires further study.

- **Long-term consolidation**: The study focuses on overnight consolidation. Whether striatal replay contributes to longer-term systems consolidation (weeks to months) is not addressed.

---

### Connections & keywords

**Key citations**: Wilson & McNaughton 1994 (hippocampal replay discovery); Buzsaki 1998, Rasch & Born 2013 (sleep and memory consolidation); Packard & McGaugh 1996 (multiple memory systems); Jin & Costa 2015 (striatal sequences); Williams et al. 2020 (PP-Seq algorithm); Denovellis et al. 2021 (real-world speed replay); Girardeau et al. 2009, Jadhav et al. 2012 (causal role of hippocampal replay).

**Named models or frameworks**: PP-Seq (point process model for sequence detection); Bayesian decoding (template-based replay detection); NMDA-dependent plasticity; Sharp-wave ripples (SWRs); Parallel memory systems theory.

**Brain regions**: Dorsolateral striatum (DLS), dorsomedial striatum (DMS), hippocampus, motor cortex, ventral tegmental area (VTA).

**Keywords**: procedural memory, motor skill learning, replay, sleep, consolidation, dorsolateral striatum, hippocampus, neural sequences, point process model, NMDA receptor, offline reactivation, time-compressed replay, unsupervised learning, multiple memory systems, Neuropixel, PP-Seq.
