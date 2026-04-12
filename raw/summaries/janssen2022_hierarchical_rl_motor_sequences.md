---
source_file: "janssen2022_hierarchical_rl_motor_sequences.md"
paper_id: "janssen2022_hierarchical_rl_motor_sequences"
title: "Hierarchical Reinforcement Learning, Sequential Behavior, and the Dorsal Frontostriatal System"
authors: "Miriam Janssen, Christopher LeWarne, Diana Burk, Bruno B. Averbeck"
year: 2022
journal: "Journal of Cognitive Neuroscience"
paper_type: "review"
contribution_type: "theoretical"
species: ["human", "monkey"]
methods: ["optogenetics", "electrophysiology"]
brain_regions: ["prefrontal_cortex", "medial_prefrontal_cortex", "anterior_cingulate_cortex", "dorsolateral_prefrontal_cortex", "striatum", "ventral_striatum", "thalamus"]
frameworks: ["reinforcement_learning", "hierarchical_rl"]
keywords: ["hierarchical", "reinforcement", "learning", "sequential", "behavior", "dorsal", "frontostriatal", "system"]
key_citations: ["tomov2020_hierarchical_planning_representation", "badre2018_frontal_cortex_hierarchical_control", "ito2015_prefrontal_thalamic_hippocampus"]
---

### One-line summary

This review proposes that motor chunks identified in human sequence-learning tasks are functionally equivalent to options in hierarchical reinforcement learning (HRL), and that the dorsal frontostriatal system provides the neural substrate for both option discovery and hierarchical action control.

---

### Background & motivation

Standard (flat) reinforcement learning scales poorly to real-world behavior because the number of states and actions grows exponentially — the "curse of dimensionality." Hierarchical RL addresses this by grouping actions into temporally extended units called options, but how the brain discovers and implements useful options is unknown. Separately, the motor sequence literature has accumulated rich evidence for action chunking in humans and animals, yet this work has rarely been interpreted through an RL lens. The paper aims to bridge these two fields, using behavioral and neural evidence from motor sequence tasks to illuminate both the computational option-discovery problem and its neural implementation.

---

### Methods

This is a narrative review. Key elements of its scope and synthesis strategy:

- **Literature covered**: human motor sequence learning tasks (serial reaction time [SRT], discrete sequence production [DSP], M×N task), animal studies (rodent lever-press and optogenetic experiments, nonhuman primate neurophysiology), and computational HRL formalisms.
- **Synthesis approach**: the authors map behavioral signatures of motor chunks (inter-response interval patterns, devaluation insensitivity, transfer effects) onto formal properties of HRL options (option-specific policy, initiation/termination conditions, pseudo-reward prediction errors).
- **Neural framework**: the Averbeck & Murray (2020) dorsal/ventral frontostriatal circuit model is used as an organizing structure to assign specific HRL functions to individual nodes (dlPFC, dorsal striatum, pre-SMA/SMA, parietal cortex).
- **Inclusion**: primarily empirical studies with clear chunking measures and studies with single-unit recording or optogenetics in behaving animals performing sequential tasks.

---

### Key findings

- Motor chunks and HRL options share three key structural properties: both are treated as single action units, both reduce computational complexity, and both facilitate more efficient learning of new sequences (transfer effects in M×N task; faster RTs with chunks in DSP task).
- In the M×N task, participants who retained previously learned chunks outperformed those whose chunks were disrupted by set shuffling, directly paralleling the efficiency gains predicted by HRL for option reuse.
- In the DSP task, participants can spontaneously discover more efficient chunk patterns even when instructed to use suboptimal ones, suggesting a biological analogue of the option-discovery process.
- Devaluation experiments in rodents show that dorsomedial PFC lesions eliminate sequence-level suppression, implicating this region in representing sequences as chunks.
- dlPFC represents movement sequences at multiple levels of abstraction simultaneously (shape, current movement, serial order), consistent with tracking option-specific policies and preparation before execution.
- Dorsal striatum (DS) activity shows task bracketing (start/stop signals for sequences) that closely parallels HRL initiation and termination conditions; this emerges with training and is present in rats, monkeys, and humans (caudate, putamen).
- Caudate neurons with outcome and cost representations become more tightly linked to sequence end with overlearning, consistent with the pseudo-RPE update signal required for option learning.
- In the Geddes et al. (2018) rodent optogenetics study, direct-pathway spiny projection neurons (dSPNs) preferentially signal sequence-level start/stop, while indirect-pathway SPNs (iSPNs) signal transitions between subsequences (options); stimulation of either population disrupts the option-specific policy.
- Disruption of striatal dopamine (pharmacologically or in Parkinson's patients off levodopa) impairs sequence chunking, implicating dopamine in option formation.
- Pre-SMA activity is higher for novel than overlearned sequences, suggesting a role in option discovery; SMA is more strongly activated for familiar chunked sequences, suggesting a role in option execution.

---

### Computational framework

**Hierarchical reinforcement learning (HRL)** — specifically the options framework (Sutton, Precup & Singh, 1999).

- **What is being modelled**: an agent learning to act in a large, structured state space by grouping primitive actions into temporally extended macro-actions (options).
- **Key variables**: option-specific policy π_o (mapping states to actions within an option); initiation set I_o (states in which the option may be invoked); termination condition β_o; pseudo-reward prediction error δ_o (computed at option termination as cumulative discounted reward minus expected value at initiation).
- **Core formalism**: a softmax over option weights selects among available options; once an option is selected, the option-specific policy governs primitive action selection until termination; pseudo-RPEs update option-level value functions analogously to standard TD RPEs.
- **Key assumption**: the option discovery problem (which actions to group) is separate from the learning problem and must itself be solved — the paper argues biology solves this through chunking mechanisms in dorsal frontostriatal circuits.

---

### Prevailing model of the system under study

The introduction situates the paper against a well-established view that cortico-striato-pallido-thalamo-cortical circuits underlie motor sequence learning and execution (Alexander, DeLong & Strick, 1986). Within this view, basal ganglia (BG) input from frontal cortex supports automated execution of learned motor plans. More recent work, reviewed by Badre & Nee (2018) and Balleine et al. (2015), extended this to hierarchical action control, identifying a medial BG loop (dlPFC/pre-SMA → caudate) for hierarchical selection and a lateral loop (SMA → putamen) for chunk execution. Cortico-BG-thalamic loops are understood to underlie both standard RL and HRL processes, with ventral circuitry handling value learning and dorsal circuitry handling action specification. However, the specific mapping of HRL computational components (option-specific policies, initiation/termination conditions, pseudo-RPEs) onto individual circuit nodes had not been articulated, and the behavioral motor sequence literature had not been systematically connected to this framework.

---

### What this paper contributes

The paper makes three integrative contributions:

1. **Chunks = options**: It formalises the functional equivalence between motor chunks and HRL options, translating the behavioral signatures of chunking (RT patterns, IRI variability, transfer, devaluation insensitivity) into the language of HRL option properties. This provides a concrete account of how biological agents may be solving the option discovery problem through practice.

2. **Circuit mapping**: It assigns specific HRL functions to individual nodes of the dorsal frontostriatal circuit. dlPFC is proposed as the locus of option-specific policy representation and sequence planning; dorsal striatum is proposed to implement initiation/termination signalling (task bracketing) and pseudo-RPE update signals; pre-SMA is proposed to be involved in discovering new options; SMA in executing familiar ones. This is more granular than prior accounts.

3. **Bidirectional agenda**: By recasting motor sequence findings in HRL terms, the paper generates predictions for motor neuroscience (e.g., where to look for pseudo-RPEs, what disrupting specific circuit nodes should do to option-level behaviour), and by grounding HRL in biological data, it constrains computational models of option discovery.

---

### Brain regions & systems

- **Dorsolateral prefrontal cortex (dlPFC)** — represents movement sequences at multiple levels of abstraction; encodes option-specific policy and sequence planning; top of the action hierarchy within frontal cortex.
- **Dorsal striatum (DS; caudate and putamen)** — option/chunk formation (policy mapping), task bracketing (initiation and termination conditions), pseudo-RPE update signals; dopamine-dependent; direct (dSPN) and indirect (iSPN) pathway neurons dissociate sequence-level from subsequence-level control.
- **Pre-SMA** — acquiring new action sequences; proposed locus for option discovery; activity decreases as sequences become overlearned.
- **SMA** — executing familiar chunked sequences; preferentially active for chunked, well-learned sequences; option execution rather than discovery.
- **Inferior parietal cortex (Area 7a)** — provides action metric information (distance, duration, object number) to dlPFC; sequence segmentation activity during DSP task.
- **Posterior parietal cortex / parietal reach region** — encodes future sequence movements before initiation; correlated with sequence segmentation in frontoparietal networks.
- **Medial frontal cortex (including ACC)** — potential role in pseudo-RPE encoding (ACC; evidence mixed and replication failures noted); sequential error processing.
- **Globus pallidus (GP) and medial dorsal thalamus** — relay nodes in the dorsal circuit loop; not directly discussed in terms of novel HRL-specific functions.
- **Ventral striatum (VS)** — mentioned as activated in SRT meta-analysis; associated with state/value learning in the ventral circuit, but not the primary focus.

---

### Mechanistic insight

The paper does not meet the full bar. It synthesises neural data pointing toward the dorsal frontostriatal circuit for hierarchical sequence control and maps HRL algorithm components onto circuit nodes. However, it does not itself present an algorithm and then provide neural data specifically supporting that algorithm over alternatives. The closest case is the Geddes et al. (2018) rodent optogenetics study (reviewed, not original), which dissociates dSPN and iSPN roles in option-level vs. subsequence-level control with causal evidence. But this is a single reviewed study, not the primary contribution. The paper proposes algorithmic-level mappings (dlPFC = policy, DS = initiation/termination + pseudo-RPE) as a theoretical synthesis rather than a direct empirical test.

At Marr's levels: the computational problem (hierarchically organising actions to reduce dimensionality) and algorithmic proposals (options framework mapped onto circuits) are addressed in detail, but the implementational level (specific cell types, synaptic mechanisms, neuromodulatory dynamics beyond dopamine's general role in chunking) is largely left to future work.

---

### Limitations & open questions

- The option discovery problem remains unsolved both computationally and biologically; current state-abstraction models (e.g., Tomov et al., 2020) require knowledge of full graph structure, which biological agents may not have.
- The review focuses heavily on the dorsal circuit; the role of ventral circuitry in subgoal organisation and its interaction with dorsal action specification is acknowledged but not detailed.
- Evidence for pseudo-RPEs in ACC is mixed — a key HRL prediction that has not been successfully replicated.
- Most motor sequence tasks use simple key-press sequences, which are more restricted than the real-world hierarchical actions HRL is meant to model; tasks with flexible, multi-strategy goal achievement are needed.
- The directionality of information flow within dorsal circuit nodes during hierarchical learning is not well characterised.
- It is unclear whether the chunk/option analogy holds for cases where options span multiple levels of abstraction (e.g., making coffee vs. grabbing milk vs. pressing a button) beyond the two-level sequences studied empirically.
- The review does not address how the option hierarchy is initialised — how an agent decides how many levels of abstraction to use or when to form new options.

---

### Connections & keywords

**Key citations**:
- Sutton, Precup & Singh (1999) — original options framework
- Botvinick, Niv & Barto (2009) — HRL and hierarchical behavior in neuroscience
- Averbeck & Murray (2020) — dorsal/ventral circuit framework for RL
- Geddes, Li & Jin (2018) — optogenetic dissection of dSPN/iSPN roles in sequential action
- Badre & Nee (2018) — frontal hierarchy and hierarchical action control
- Balleine, Dezfouli, Ito & Doya (2015) — medial/lateral BG loop model
- Tomov et al. (2020) — Bayesian model of hierarchy/option discovery
- Sakai, Kitaguchi & Hikosaka (2003) — M×N task chunking evidence

**Named models or frameworks**:
- Options framework (Sutton, Precup & Singh, 1999)
- Hierarchical reinforcement learning (HRL)
- Flat / standard reinforcement learning
- Temporal-difference (TD) RL
- Rescorla-Wagner algorithm
- Discrete sequence production (DSP) task
- M×N task (Hikosaka)
- Serial reaction time (SRT) task
- Averbeck & Murray (2020) dorsal/ventral circuit model

**Brain regions**:
- Dorsolateral prefrontal cortex (dlPFC)
- Dorsal striatum (caudate, putamen)
- Pre-SMA / SMA (medial frontal cortex)
- Inferior parietal cortex (Area 7a)
- Posterior parietal cortex
- Anterior cingulate cortex (ACC)
- Globus pallidus (GP)
- Medial dorsal thalamus
- Ventral striatum

**Keywords**:
- hierarchical reinforcement learning
- options framework
- motor chunking
- action sequences
- option discovery problem
- dorsal frontostriatal circuit
- task bracketing
- pseudo-reward prediction error
- sequence learning
- discrete sequence production task
- direct and indirect pathway striatum
- temporal abstraction
