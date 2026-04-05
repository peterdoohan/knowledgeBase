---
source_file: dolfen2022_hippocampus_motor_sequence_temporal.md
title: The hippocampus binds movements to their temporal position in a motor sequence
authors: Nina Dolfen, Serena Reverberi, Hans Op de Beeck, Bradley R. King, Genevieve Albouy
year: 2022
journal: bioRxiv (preprint)
paper_type: empirical
contribution_type: empirical
---

### One-line summary

Using multivoxel pattern similarity analysis of fMRI data acquired during motor sequence practice, this study demonstrates that hippocampal activation patterns encode the binding of finger movements to their learned temporal position in a sequence, but carry no information about movements or positions in isolation.

---

### Background & motivation

Learning complex motor tasks requires not just knowing which movements to make, but in what order. It remains unclear how the brain encodes sequential motor actions in a way that preserves their temporal order. Prior work in non-motor memory has established that the hippocampus represents the temporal order of episodic events and sequential items (e.g., letters, objects), and behavioural evidence hints that the hippocampus may similarly bind motor actions to their ordinal position in a sequence. However, this had not been directly tested with neuroimaging. The study also examines how motor network regions (striatum, premotor and supplementary motor cortex, primary motor cortex, superior parietal lobule) contribute to order coding alongside the hippocampus.

---

### Methods

- **Participants**: 33 healthy, right-handed young adults (mean age 23.4; 19 female) scanned at KU Leuven.
- **Task**: Explicit bimanual serial reaction time task (SRTT). Participants first learned an 8-finger sequence outside the scanner (1 hour, learning session), then performed the learned sequential (SEQ) and random (RND) SRTT interleaved within the scanner (8 fMRI runs), followed by an immediate retention test outside the scanner.
- **Sequence**: Fixed 8-element finger sequence (each finger pressed once per cycle); starting position counterbalanced across participants to dissociate finger identity from temporal position at the group level.
- **fMRI acquisition**: 3T Philips Achieva, whole-brain BOLD (T2*-EPI, TR=2000ms, TE=30ms, 2.5mm isotropic voxels).
- **Analysis approach**: Representational similarity analysis (RSA) using multivoxel pattern similarity. Two separate GLMs modelled neural responses per temporal position (position GLM) and per finger/key (key GLM) for SEQ and RND conditions. Five neural similarity matrices were constructed per ROI: SEQ (finger-position binding), Random Position (RP; position coding), Random Key (RK; finger coding), and two "mixed" matrices (Mixed Key and Mixed Position) comparing coding across conditions.
- **ROIs**: Seven bilateral ROIs — M1, SMA, PMC, aSPL (cortical, functionally defined), hippocampus, putamen, caudate (subcortical, anatomically defined via FSL FIRST).
- **Statistics**: One-tailed paired-sample t-tests (diagonal vs. off-diagonal similarity) with FDR correction across 21 within-condition and 14 mixed-condition comparisons. Boundary position analyses conducted to control for enhanced similarity at sequence edges (positions 1 and 8).

---

### Key findings

- **Finger-position binding (SEQ matrix)**: All seven ROIs showed significantly higher diagonal similarity in the SEQ condition (same finger + same position > different; all pFDR < 0.001), indicating that every region encoded some form of movement-position binding.
- **Hippocampal specificity**: The hippocampus showed SEQ binding but showed no significant finger coding (RK matrix: t32=0.489, pFDR=0.314) and no position coding (RP matrix: t32=0.919, pFDR=0.191) in the random condition, indicating that its binding effect is not attributable to finger or position coding per se. This pattern held after excluding boundary positions.
- **Striatum**: Both putamen and caudate showed SEQ binding but no finger coding (caudate: pFDR=0.122) beyond position-boundary effects. After removing boundaries, putamen and caudate showed no significant position coding, converging on the hippocampal profile of true finger-position binding.
- **Cortical regions (M1, SMA, aSPL)**: Showed SEQ binding, significant finger (and hand) coding in RND, and movement coding generalised across SEQ and RND conditions (Mixed Key analysis). Their SEQ binding is attributable at least in part to movement coding.
- **PMC**: Showed SEQ binding plus position coding (RND condition) that survived boundary exclusion, and both movement and position coding were shared across SEQ and RND conditions (Mixed Key: t32=8.023, pFDR<0.001; Mixed Position: t32=9.354, pFDR<0.001). PMC is the only region carrying abstract position information irrespective of task condition.
- **Behavioural learning**: Reaction time and accuracy improved across SEQ practice blocks and a sequence-specific performance advantage (faster, more accurate) was maintained throughout the fMRI session and at retention.

---

### Computational framework

Not applicable in the formal sense — the paper uses no explicit computational model or fitting procedure. The analytic framework is representational similarity analysis (RSA / multivoxel pattern similarity), a method grounded in the idea that if a brain region encodes a particular type of information, pairs of trials sharing that information should produce more similar distributed activation patterns than pairs not sharing it (Kriegeskorte et al. 2008).

The paper operationalises three representational variables — finger identity, temporal position, and finger-position binding — and tests for each independently by comparing diagonal vs. off-diagonal cells in appropriately structured neural similarity matrices. This approach dissociates which information dimension a region encodes without committing to a specific coding scheme.

The results constrain theories of how temporal order in motor sequences is computed: they are consistent with an associative binding account (hippocampus binds response goals to ordinal positions) and a stimulus-response chaining account (striatum binds effector-specific movements to positions), and suggest that cortical motor regions primarily represent individual movement components.

---

### Prevailing model of the system under study

The dominant view at the time of publication held that motor sequence learning recruits a hippocampal-striatal competition or complementarity: the striatum supports an effector-dependent, motoric representation of the sequence via stimulus-response associations, while the hippocampus supports a more abstract, goal-based or spatial representation that is effector-independent. Hippocampal involvement was thought to be important mainly early in learning for encoding the overall structure of the sequence and for consolidation during offline periods (sleep), with the striatum taking over for automatised performance. It was well established that multivoxel patterns in primary and secondary motor cortices differentiate individual movements and, after extensive training, can discriminate between different sequences. The specific capacity of the hippocampus to bind individual movements to their serial position — as opposed to encoding sequence structure more generally — had not been directly demonstrated; only behavioural work had implicated such a binding process.

---

### What this paper contributes

The study provides direct neuroimaging evidence that the hippocampus encodes finger-position binding — representing each movement in the context of its specific ordinal slot in the learned sequence — and that this is not reducible to independent coding of finger identity or temporal position. This refines the prevailing model in two ways: (1) it specifies a representational content for hippocampal involvement in motor sequence learning (temporal order binding, not just sequence engagement broadly), and (2) it demonstrates that the hippocampus's role in preserving temporal order appears to generalise across memory domains (episodic, non-motor sequence, and now motor sequence). The study also reveals that the striatum shows a similar binding profile, but likely via effector-specific stimulus-response associations rather than goal-based representations — a mechanistic dissociation supported by the putamen's effector-specific (finger/hand) coding in the random condition that is absent in the hippocampus. Additionally, the PMC is shown to carry abstract position information independent of task condition, pointing to a temporal scaffolding role in motor planning, while M1, SMA, and aSPL are primarily movement-coding regions early in learning.

---

### Brain regions & systems

- **Hippocampus** — primary region of interest; shown to encode finger-position binding but not finger or position coding in isolation; proposed to bind response goals to their ordinal position in the sequence.
- **Caudate nucleus** — shows finger-position binding profile similar to hippocampus after boundary exclusion; no independent finger or position coding; implicated in sequence order encoding via striatal mechanisms.
- **Putamen** — shows finger-position binding and independent finger/hand coding in random practice; binding likely reflects effector-specific stimulus-response associations; distinct from the goal-based hippocampal binding.
- **Premotor cortex (PMC)** — shows finger-position binding, position coding that survives boundary exclusion and generalises across task conditions, and finger coding; interpreted as providing a temporal positional scaffold for movement planning.
- **Supplementary motor area (SMA)** — shows finger-position binding and independent finger/hand coding in random condition; coding similar across SEQ and RND conditions; contributes via movement representations.
- **Primary motor cortex (M1)** — shows strong finger and hand coding generalising across conditions; SEQ binding attributable to movement coding; consistent with prior RSA studies of M1 during sequence learning.
- **Anterior superior parietal lobule (aSPL)** — shows finger-position binding and finger/hand coding; movement coding shared across task conditions; contributes through movement-based representations.

---

### Mechanistic insight

The paper meets criterion 1 — it formalises a binding algorithm (finger-position association formed by RSA during practice) — and criterion 2 — it provides fMRI multivariate pattern data that specifically support this algorithm in the hippocampus over alternative explanations (pure finger coding or pure position coding).

- **Computational**: The brain must preserve the temporal order of a learned motor sequence, i.e., it must solve the problem of binding each movement to its ordinal position so that sequences of identical elements (same fingers) in different orders remain discriminable.
- **Algorithmic**: The hippocampus implements this by forming conjunctive (finger × position) representations. Pattern similarity between executions of the same finger at the same sequence position is elevated relative to different fingers or different positions, but no such selectivity is seen for finger identity or position identity in isolation in random movement patterns. This is operationally consistent with an associative map linking response goals to their ordinal slots.
- **Implementational**: The paper does not investigate cell types, connectivity, or neuromodulators. The hippocampal signal is measured at the level of BOLD fMRI, so implementational-level claims are not available. The authors hypothesise, based on earlier work, that the hippocampus encodes goal-based (effector-independent, spatial) representations, while the striatum encodes effector-specific representations, but this distinction is inferred from the random-condition coding profiles rather than from direct imaging of the underlying representations' specificity.

The paper does not meet the bonus bar for implementational detail.

---

### Limitations & open questions

- The study captures a single early learning time-point (one hour of training); it is unknown whether finger-position binding in the hippocampus changes with extended practice or consolidation, or whether it transfers to the striatum or cortex over time.
- The paper cannot definitively distinguish whether cortical regions (M1, SMA, aSPL) do not encode finger-position binding or simply that movement coding dominates early in learning. The analyses show movement coding contributes, but do not rule out simultaneous binding representations.
- The hippocampus and striatum show similar binding profiles but are hypothesised to encode different content (goal-based vs. motoric); this distinction is speculative and would require effector-transfer or sequence-generalisation paradigms to test directly.
- Boundary effects (enhanced similarity at positions 1 and 8) complicate the interpretation of position coding in several ROIs; the paper addresses this with follow-up analyses but cannot fully rule out attentional or visual-cue contributions.
- Signal-to-noise ratio in subcortical regions is acknowledged as a potential concern, though the striatal results make a global SNR explanation unlikely.
- The sequence starting-position counterbalancing dissociates finger from position at the group level, but individual-level confounding cannot be fully excluded.
- The use of a bioRxiv preprint means the work had not undergone peer review at the time of posting.

---

### Connections & keywords

**Key citations**:
- Davachi & DuBrow (2015) — hippocampus and temporal order preservation
- Hsieh et al. (2014, Neuron) — hippocampal patterns carry temporal context for objects
- Kalm, Davis & Norris (2013) — hippocampal sequence representations for auditory items
- Albouy et al. (2013, Hippocampus) — hippocampus/striatum dynamics in motor sequence learning
- Albouy et al. (2015, NeuroImage) — hippocampal goal-based vs. striatal motoric representations
- Pinsard et al. (2019, eLife) — consolidation alters sequence-specific distributed representations
- Berlot, Popp & Diedrichsen (2020, eLife) — critical re-evaluation of fMRI signatures of motor sequence learning
- Yokoi & Diedrichsen (2019, Neuron) — hierarchical motor sequence representations in neocortex
- King et al. (2019, Psych Science) — schema and motor-memory consolidation (behavioural binding hypothesis)
- Kriegeskorte, Mur & Bandettini (2008) — representational similarity analysis

**Named models or frameworks**:
- Representational similarity analysis (RSA) / multivoxel pattern similarity analysis
- Serial reaction time task (SRTT)
- CoSMoMVPA toolbox
- Human Motor Area Template (HMAT)

**Brain regions**:
- Hippocampus
- Caudate nucleus
- Putamen
- Premotor cortex (PMC)
- Supplementary motor area (SMA)
- Primary motor cortex (M1)
- Anterior superior parietal lobule (aSPL)

**Keywords**:
- hippocampus, motor sequence learning, temporal order coding, finger-position binding, representational similarity analysis, multivoxel pattern analysis, striatum, procedural memory, sequence learning, serial reaction time task, fMRI, motor memory consolidation
