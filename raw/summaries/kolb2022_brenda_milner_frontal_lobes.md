---
source_file: kolb2022_brenda_milner_frontal_lobes.md
paper_id: kolb2022_brenda_milner_frontal_lobes
title: "Brenda Milner: Pioneer of the Study of the Human Frontal Lobes"
authors:
  - "Bryan Kolb"
year: 2022
journal: "Frontiers in Human Neuroscience"
paper_type: review
contribution_type: review
species:
  - human
methods:
  - lesion
brain_regions:
  - prefrontal_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
frameworks:
  - reinforcement_learning
  - hierarchical_rl
keywords:
  - frontal_lobe_lesions
  - focal_cortical_excision
  - wisconsin_card_sorting_task
  - cognitive_set_shifting
  - temporal_organisation_of_behaviour
  - recency_memory
  - verbal_fluency
  - design_fluency
  - conditional_associative_learning
  - hemispheric_specialisation
  - serial_order_memory
  - neuropsychological_dissociation
  - brenda
  - milner
  - pioneer
  - study
  - human
  - frontal
  - lobes
---

### One-line summary

A retrospective review of Brenda Milner's foundational contributions to understanding human frontal lobe function, documenting how her lesion studies at the Montreal Neurological Institute established key dissociations in cognitive, motor, and memory functions across frontal lobe regions.

---

### Background & motivation

Prior to Milner's work in the 1960s, there was no consensus on whether the frontal lobe played a meaningful role in cognition — some researchers argued it had little effect on intelligence in adults, and no systematic study had examined the cognitive consequences of circumscribed frontal excisions in humans. The field lacked both the methodology and the patient populations needed to draw clean brain-behaviour correlations. Milner's access to Penfield's surgical cohort at the MNI, combined with surgeon-drawn lesion maps (predating CT/MRI), created a unique opportunity to study focal frontal excisions with the same precision then being applied to non-human primates.

---

### Methods

This is a narrative review covering Milner's frontal lobe research from 1963 to approximately 2004.

- **Patient population**: Surgical epilepsy patients at the Montreal Neurological Institute (MNI) with circumscribed cortical excisions (frontal, temporal, or posterior cortical), assessed pre- and postoperatively.
- **Lesion documentation**: Surgeon-produced drawings of excisions (no imaging technology available in the early period).
- **Key tasks reviewed**:
  - Wisconsin Card Sorting Task (WCST): category learning and set-shifting.
  - Word Fluency (Chicago Word Fluency Test): verbal spontaneity and output.
  - Design Fluency (Jones-Gotman & Milner, 1977): non-verbal spontaneity.
  - Stylus Maze Learning: spatial learning and rule-following.
  - Serial Arm and Facial Movement Copying (Kolb & Milner, 1981): motor sequencing.
  - Recency vs. Recognition Memory (Milner et al., 1991): temporal order memory.
  - Conditional Associative Learning (Milner & Petrides, 1984; Petrides, 1985–1997): stimulus-response association learning.
- **Synthesis method**: Narrative review, organised by cognitive domain and chronological research programme.

---

### Key findings

- Dorsolateral frontal patients showed severe impairment on the WCST (mean categories completed: 1.4 postop vs. 4.9 for orbitofrontal/temporal controls), demonstrating cognitive — not merely motor — deficits with normal IQ.
- Dorsolateral and orbitofrontal lesions produced dissociable cognitive profiles, refuting a unitary frontal lobe function.
- Left frontal lesions selectively impaired verbal fluency (~50% of control output) while sparing verbal recall; left temporal lesions showed the reverse pattern — establishing a double dissociation.
- Right frontal lesions selectively impaired non-verbal design fluency and non-verbal recency memory, establishing hemispheric complementary specialisation within the frontal lobes.
- Both left and right frontal patients were impaired at recency discrimination (temporal order memory) but not item recognition, indicating a frontal-specific role in ordering rather than storage of memories.
- Frontal patients showed rule-breaking behaviour across multiple tasks (maze learning, design fluency), consistent with a role in behavioural regulation.
- Mid-dorsolateral frontal cortex was specifically implicated in serial order memory and conditional associative learning, consistent with later primate work (Petrides, 1991).
- Serial facial-movement copying was more impaired than arm-movement copying after frontal lesions, suggesting a special role in controlling face movements.

---

### Computational framework

Not applicable. The paper is a historical narrative review and does not employ a formal computational framework. The results constrain models of prefrontal cortex function, particularly those addressing working memory, cognitive control, and temporal organisation of behaviour — domains where computational frameworks such as active maintenance in recurrent networks, hierarchical reinforcement learning, and task-set gating have since been applied.

---

### Prevailing model of the system under study

Before Milner's work, views on the frontal lobe were polarised. An earlier extreme position attributed the "highest" cognitive and ethical functions to the frontal lobes, while a later counter-reaction (e.g., Hebb, 1945) argued the frontal lobe contributed primarily to developmental intelligence and had minimal function in adults. Teuber proposed a unitary "corollary discharge" hypothesis — that the frontal lobe sends anticipatory signals to posterior sensory regions to prepare for voluntary action — but this was vague on cognitive mechanisms and did not predict regional differentiation. Human data were largely from patients with diffuse tumours, vascular injuries, or war-wound penetrating trauma, precluding clear brain-behaviour mapping. The dominant implicit assumption was therefore that frontal lobe function was either negligible or unitary.

---

### What this paper contributes

This review consolidates and contextualises Milner's programme of work as having established several framework-level conclusions that replaced the prevailing view:

1. The frontal lobe is necessary for specific cognitive functions even when general intelligence is preserved.
2. Frontal lobe function is not unitary: dorsolateral and orbitofrontal regions are dissociable.
3. There is complementary hemispheric specialisation within the frontal lobes (left: verbal fluency and verbal recency; right: non-verbal fluency and non-verbal recency).
4. The frontal lobe plays a specific role in temporal organisation (serial ordering, recency memory) rather than item storage.
5. Frontal lobe patients fail to follow rules, pointing to a role in behavioural regulation beyond task-specific cognition.
6. Findings from humans with focal excisions are directly comparable to non-human primate lesion data, supporting cross-species generalisability of frontal lobe function.

---

### Brain regions & systems

- **Dorsolateral prefrontal cortex (DLPFC)** — primary focus; implicated in set-shifting (WCST), verbal fluency, serial order memory, working memory, and conditional associative learning.
- **Mid-dorsolateral frontal cortex** — sub-region specifically linked to serial order memory and recency judgements; distinguished from more posterior frontal regions.
- **Orbitofrontal cortex** — shown to be functionally dissociable from DLPFC; patients performed normally on WCST and fluency tasks.
- **Left frontal lobe** — selectively impaired at verbal fluency and verbal recency; spared verbal recognition.
- **Right frontal lobe** — selectively impaired at non-verbal fluency (design fluency) and non-verbal recency; spared recognition memory.
- **Temporal lobes (left and right)** — used as comparison lesion groups; left temporal patients showed impaired verbal recall but normal verbal fluency, providing dissociations.
- **Posterior parietal cortex** — noted as showing overlap with some frontal functions (e.g., motor sequencing), and as part of extended cortical networks with frontal cortex.

---

### Mechanistic insight

The paper meets the bar partially: it reviews empirical neural data (lesion studies) linked to specific cognitive processes, but does not formalise an algorithm. The evidence supports a characterisation at Marr's computational and algorithmic levels, but implementational detail is absent.

- **Computational**: The frontal lobe solves the problem of temporally organising and flexibly controlling behaviour — specifically, maintaining and shifting rules, ordering sequences of actions or memories in time, and forming arbitrary stimulus-response associations.
- **Algorithmic**: The representations involved include task sets (WCST set-shifting), temporal tags on recent events (recency memory), sequential motor programmes (facial/arm movement copying), and conditional mappings (associative learning). The frontal lobe appears to maintain and monitor these representations rather than store the items themselves (item recognition is intact).
- **Implementational**: The paper does not address cell types, connectivity, or biophysical mechanisms. Regional dissociations (dorsolateral vs. orbital; left vs. right; mid-dorsolateral vs. posterior frontal) provide anatomical granularity but not circuit-level mechanism.

The key mechanistic claim — that dorsolateral prefrontal cortex specifically supports temporal organisation and serial order rather than item memory — is well supported by the double dissociations reported across multiple task types. The bonus criterion (specific cell types, neuromodulators) is not addressed.

---

### Limitations & open questions

- All findings rely on retrospective lesion-behaviour correlations; causal direction is inferred but the studies are quasi-experimental (patients selected for clinical need, not random assignment).
- Lesion boundaries in the early studies were documented by surgeon drawings, not neuroimaging, introducing uncertainty in anatomical localisation.
- The review does not address neuroimaging studies that have since tested and extended Milner's findings; the relationship between lesion-based and activation-based evidence is noted but not systematically synthesised.
- As acknowledged by Kolb, imaging studies have methodological limitations that lesion studies do not share, and vice versa — how the two bodies of evidence should be integrated is unresolved.
- The mechanisms by which the frontal lobe implements temporal organisation, rule-following, or conditional association remain unspecified at the circuit level.
- Complementary specialisation of the hemispheres is described phenomenologically but its developmental or computational origins are not addressed.

---

### Connections & keywords

**Key citations**:
- Milner (1963, 1964) — original WCST and frontal lobectomy studies
- Scoville and Milner (1957) — H.M. and hippocampal memory
- Jones-Gotman and Milner (1977) — design fluency
- Kolb and Milner (1981) — serial movement copying
- Milner et al. (1991) — recency vs. recognition memory
- Milner and Petrides (1984); Petrides (1985, 1990, 1991, 1997) — conditional associative learning and serial order
- Teuber (1964) — corollary discharge hypothesis
- Hebb (1945) — sceptical view of adult frontal lobe function
- Vaidya et al. (2019) — value of focal lesion studies in contemporary neuroscience

**Named models or frameworks**:
- Wisconsin Card Sorting Task (WCST)
- Teuber's corollary discharge hypothesis
- Conditional associative learning paradigm (Milner & Petrides)
- Chicago Word Fluency Test
- Design Fluency Task

**Brain regions**:
- Dorsolateral prefrontal cortex (DLPFC)
- Mid-dorsolateral frontal cortex
- Orbitofrontal cortex
- Left and right frontal lobes
- Left and right temporal lobes
- Posterior parietal cortex

**Keywords**:
- frontal lobe lesions, focal cortical excision, Wisconsin Card Sorting Task, cognitive set-shifting, temporal organisation of behaviour, recency memory, verbal fluency, design fluency, conditional associative learning, hemispheric specialisation, serial order memory, neuropsychological dissociation
