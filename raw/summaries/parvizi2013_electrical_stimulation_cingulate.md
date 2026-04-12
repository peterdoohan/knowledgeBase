---
source_file: "parvizi2013_electrical_stimulation_cingulate.md"
paper_id: "parvizi2013_electrical_stimulation_cingulate"
title: "The Will to Persevere Induced by Electrical Stimulation of the Human Cingulate Gyrus"
authors: "Josef Parvizi, Vinitha Rangarajan, William Shirer, Nikita Desai, Michael D. Greicius"
year: 2013
journal: "Neuron"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
methods: ["electrophysiology", "fmri", "lesion"]
brain_regions: ["retrosplenial_cortex", "amygdala", "medial_temporal_lobe"]
keywords: ["electrical_brain_stimulation", "intracranial_electrophysiology", "emotional_salience_network", "cingulo_opercular_network", "autonomic_arousal", "heart_rate", "interoception", "motivation", "perseverance", "endurance", "effort", "challenge", "epilepsy", "resting_state_fmri", "functional_connectivity", "anterior_cingulate_cortex", "midcingulate_cortex", "will", "persevere", "induced"]
---

### One-line summary

Electrical stimulation of the anterior midcingulate cortex (aMCC) elicits a stereotyped set of autonomic changes and subjective experiences characterized by foreboding coupled with determination to overcome imminent challenges, which the authors term "the will to persevere."

---

### Background & motivation

The anterior cingulate cortex (ACC) is implicated in emotion, pain, and cognitive control, but the subjective correlates of ACC activity have remained largely unexplored due to its deep anatomical location. Understanding the brain networks mediating perseverance and endurance could provide new therapeutic avenues for disorders like depression and chronic pain, which are characterized by reduced motivation and capacity to endure distress.

---

### Methods

- **Participants**: Two patients with refractory epilepsy implanted with intracranial depth electrodes for seizure localization
- **Electrical brain stimulation (EBS)**: Bipolar square-wave stimulation between adjacent electrode contacts (1 and 2) at 2–8 mA (real trials) or 0 mA (sham trials); 200 μs pulse width at 50 Hz
- **Stimulation sites**: Anterior midcingulate cortex (aMCC) in both patients; control sites included subgenual cingulate, retrosplenial cortex, and adjacent white matter
- **Physiological monitoring**: Simultaneous EEG recording to detect after-discharges/seizures; heart rate monitoring in 5-second windows post-stimulation
- **Resting-state fMRI**: Pre-operative scans used for seed-based functional connectivity analysis with a 3-mm spherical ROI centered between stimulation electrodes
- **Network identification**: Goodness-of-fit analysis comparing subject-specific connectivity maps to 14 canonical functional networks

---

### Key findings

- **EBS in aMCC produced stereotyped subjective experiences**: Both patients reported autonomic symptoms ("shakiness," "hot flashes" in chest and neck), increased heart rate, and a distinct psychological state combining foreboding/worry with strong motivation to persevere through an anticipated challenge
- **Patient descriptions**: Patient 1 described the feeling as "driving into a storm" with determination to "push harder, push harder, push harder to try and get through this"; Patient 2 reported feeling worried but knowing "I have to fight to make it" and "I can't give up"
- **Heart rate effects**: Mean heart rate increased from sham (P1: 77±6, P2: 81±8 bpm) to sub-threshold (P1: 86±9, P2: 90±5 bpm) to real EBS (P1: 92±7, P2: 94±7 bpm)
- **Dose-response relationship**: Sub-threshold currents (6 mA in P1, 4 mA in P2) and sham trials did not produce the subjective effects
- **Specificity of effects**: Stimulation of control sites (subgenual cingulate, retrosplenial cortex, adjacent white matter) did not elicit the same cognitive, emotional, or autonomic changes
- **Functional connectivity**: The aMCC stimulation site in both patients was at the core of the "emotional salience" (or cingulo-opercular) network, linking aMCC to frontoinsular cortex, frontopolar regions, temporoparietal junction, and subcortical structures (amygdala, hypothalamus, brainstem)

---

### Computational framework

Not applicable. This is a direct empirical study using electrical brain stimulation and functional connectivity analysis. However, the findings constrain models of how the brain integrates autonomic, cognitive, and emotional signals to generate motivated behavior. The results suggest that the aMCC functions as part of a broader emotional salience network that computes the significance of anticipated challenges and coordinates appropriate physiological and psychological responses.

---

### Prevailing model of the system under study

Prior to this study, the anterior cingulate cortex (particularly the mid-cingulate region) was understood to be essential for initiating behavioral changes, making associations between reward and action, determining actions necessary to obtain goals, and synthesizing information about reinforcers ranging from pain to aversive cues. Anatomical and functional connectivity studies indicated strong connections between ACC and structures important for pain, pleasure, emotion, and decision-making. Lesion studies in humans implicated ACC in decision-making and emotional processing, but the anatomical imprecision of lesions made it difficult to attribute deficits specifically to ACC versus adjacent tissue. The subjective correlates of ACC activity had remained largely unexplored due to methodological challenges.

---

### What this paper contributes

This paper provides the first detailed, first-person accounts of the subjective experience associated with electrical stimulation of the anterior midcingulate cortex. The findings establish that:

1. **Specific subjective state**: aMCC activation produces a distinct phenomenological state combining foreboding/worry with determination to overcome anticipated challenges ("will to persevere"), distinct from simple fear, anxiety, or positive motivation alone

2. **Autonomic integration**: This psychological state is tightly coupled with specific autonomic changes (increased heart rate, chest/neck sensations), suggesting the aMCC integrates cognitive and physiological preparedness for challenge

3. **Network-level function**: The stimulation site is a core node of the emotional salience network (including frontoinsular cortex, frontopolar regions, subcortical structures), supporting the view that aMCC functions as part of a distributed network for detecting and responding to motivationally significant events

4. **Clinical relevance**: The findings provide a neurobiological anchor for understanding disorders characterized by reduced motivation and endurance (depression, chronic pain), suggesting that dysfunction in the aMCC and its network may underlie these symptoms

---

### Brain regions & systems

- **Anterior midcingulate cortex (aMCC)** — primary site of electrical stimulation; core node of the emotional salience network; implicated in generating the subjective "will to persevere" and coordinating autonomic responses to anticipated challenges
- **Frontoinsular cortex** — part of the emotional salience network functionally connected to the aMCC stimulation site; likely contributes to affective and interoceptive processing
- **Frontopolar cortex** — part of the emotional salience network; may contribute to prospective evaluation and decision-making about anticipated challenges
- **Temporoparietal junction** — part of the extended emotional salience network
- **Amygdala** — subcortical node of the emotional salience network; implicated in emotional processing and threat detection
- **Hypothalamus** — subcortical node; likely mediates autonomic changes (heart rate, body temperature) observed during stimulation
- **Brainstem** — subcortical node; involved in autonomic regulation
- **Subgenual cingulate** — control stimulation site; did not produce the same effects as aMCC stimulation
- **Retrosplenial cortex** — control stimulation site; did not produce the same effects
- **Medial temporal lobe** — implanted region for seizure monitoring; stimulation caused typical seizure auras but not the "will to persevere" phenomenon

---

### Mechanistic insight

This paper provides strong mechanistic insight at the algorithmic and implementational levels, though the computational level is described phenomenologically rather than formally.

**Computational level**: The aMCC and its associated network appear to solve the problem of detecting motivationally significant challenges and coordinating appropriate cognitive, emotional, and physiological responses to prepare the organism for action. This involves integrating predictive information about upcoming challenges with autonomic resource mobilization and psychological motivation.

**Algorithmic level**: The paper identifies the aMCC as a core node within the emotional salience network that implements a specific algorithm: the coupling of foreboding/worry about anticipated challenges with determination to overcome them. This is not a simple valence signal (positive or negative) but a complex integration of threat detection, autonomic arousal, and approach motivation. The resting-state functional connectivity analysis reveals the network architecture that likely implements this algorithm through interactions between aMCC, frontoinsular cortex, frontopolar regions, and subcortical structures.

**Implementational level**: The study provides direct evidence for the neural implementation through electrical stimulation of specific aMCC sites. The anatomical localization (gray matter contacts 1 and 2) and the dose-response relationship (threshold effects at 6-8 mA, no effects at subthreshold currents or sham) support the specificity of the implementation. The accompanying autonomic changes (heart rate increases, chest/neck sensations) implicate subcortical structures (hypothalamus, brainstem) in the implementation. The connectivity with frontoinsular cortex (a region implicated in interoception) suggests a mechanism for integrating visceral and cognitive signals.

**Limitations on mechanistic claims**: While the paper provides compelling first-person accounts and precise anatomical localization, it does not provide direct neural recordings (e.g., single-unit activity, local field potentials) that would reveal the specific neural dynamics implementing the algorithm. The causal role of network nodes other than aMCC is inferred from functional connectivity rather than demonstrated through stimulation or lesion of those nodes.

---

### Limitations & open questions

- **Small sample size**: Only two patients were studied, limiting generalizability
- **Epilepsy population**: Both patients had epilepsy and were taking antiepileptic medications, which may have influenced brain function and stimulation responses
- **Intracranial electrode coverage**: Limited to clinically determined sites; whole-brain network effects are inferred from resting-state fMRI rather than direct stimulation of other nodes
- **Subjective reporting**: First-person experiences are difficult to quantify and compare across individuals; the specific phenomenological content may vary between subjects despite the common themes
- **Duration of effects**: The study reports acute stimulation effects; long-term consequences or potential for therapeutic modification of the "will to persevere" through repeated stimulation were not investigated
- **Network specificity**: While the emotional salience network was identified, the relative contributions of different network nodes (beyond the aMCC stimulation site) to the subjective experience were not determined
- **Causal mechanisms**: The precise mechanism by which aMCC stimulation produces the specific combination of foreboding and determination remains unclear

---

### Connections & keywords

- **Key citations**: Talairach et al. 1973 (pioneering EBS of ACC); Seeley et al. 2007 (emotional salience network); Dosenbach et al. 2007 (cingulo-opercular network); Shackman et al. 2011 (integration of negative affect, pain, and cognitive control in cingulate); Rudebeck et al. 2006 (rodent cingulate lesions and effort-related decision-making); Selimbeyoglu and Parvizi 2010 (review of human EBS effects)
- **Named models or frameworks**: Emotional salience network; cingulo-opercular network; expected value of control (Shenhav et al.)
- **Brain regions**: anterior midcingulate cortex (aMCC), anterior cingulate cortex (ACC), frontoinsular cortex, frontopolar cortex, temporoparietal junction, amygdala, hypothalamus, brainstem, subgenual cingulate, retrosplenial cortex
- **Keywords**: electrical brain stimulation, intracranial electrophysiology, emotional salience network, cingulo-opercular network, autonomic arousal, heart rate, interoception, motivation, perseverance, endurance, effort, challenge, epilepsy, resting-state fMRI, functional connectivity, anterior cingulate cortex, midcingulate cortex
