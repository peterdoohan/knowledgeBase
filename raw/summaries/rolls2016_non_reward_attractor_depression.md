---
source_file: rolls2016_non_reward_attractor_depression.md
paper_id: rolls2016_non_reward_attractor_depression
title: "A non-reward attractor theory of depression"
authors:
  - "Edmund T. Rolls"
year: 2016
journal: "Neuroscience and Biobehavioral Reviews"
paper_type: review
contribution_type: theoretical
species:
  - macaque
methods:
  - fmri
  - lesion
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - amygdala
  - medial_temporal_lobe
frameworks:
  - attractor_networks
keywords:
  - depression
  - mania
  - bipolar_disorder
  - orbitofrontal_cortex
  - attractor_networks
  - non_reward
  - punishment
  - reward_reversal
  - nmda_receptors
  - ketamine
  - resting_state_functional_connectivity
  - systems_neuroscience
  - computational_psychiatry
  - top_down_cognitive_effects
  - ruminative_thoughts
  - non
  - reward
  - attractor
  - theory
---

### One-line summary

Depression arises from overly sensitive and persistent attractor states in the lateral orbitofrontal cortex non-reward system that maintain negative cognitive states through positive feedback with language and cognitive systems.

### Background & motivation

Major depressive disorder is a leading cause of disability worldwide, characterized by altered reward processing, inflexibility of thought, and ruminative negative cognition. While neuroimaging studies have identified multiple brain regions implicated in depression (amygdala, subgenual cingulate, medial prefrontal cortex), there was no unifying theory linking these findings to the mechanisms of persistent negative mood states. This paper proposes a theory grounded in attractor network dynamics to explain how depression becomes self-maintaining.

### Methods

This is a theoretical/review paper that synthesizes evidence from multiple sources:

- **Neurophysiological studies**: Single-unit recordings in macaque orbitofrontal cortex showing "error neurons" that respond to non-reward and maintain persistent firing (Thorpe et al., 1983)
- **Human neuroimaging**: fMRI studies of reward reversal, stop-signal tasks, and monetary loss (Kringelbach & Rolls, 2003; Deng et al., 2016; O'Doherty et al., 2001)
- **Lesion studies**: Effects of orbitofrontal cortex damage on reversal learning in humans and non-human primates (Fellows & Farah, 2003; Hornak et al., 2004; Murray & Izquierdo, 2007)
- **Resting-state connectivity**: Large-scale analysis (n=421 patients, 488 controls) showing altered functional connectivity patterns in depression (Cheng et al., 2016)
- **Pharmacological interventions**: Effects of ketamine, antidepressants, and ECT on orbitofrontal activity (Lally et al., 2015; Carlson et al., 2013; Ma, 2015)

### Key findings

- The lateral orbitofrontal cortex contains neurons that respond to non-reward and maintain firing for many seconds, indicating attractor state dynamics that sustain memory of negative events
- Human neuroimaging shows lateral OFC activation during reward reversal, stop-signal tasks, and monetary loss - situations requiring behavior change after non-reward
- Damage to the OFC impairs reward reversal learning, with patients continuing to choose previously rewarded stimuli despite non-reward
- In depression, the lateral OFC shows increased functional connectivity with language areas (angular gyrus) and self-representation areas (precuneus), potentially explaining ruminative thoughts and negative self-esteem
- The medial OFC (reward-related) shows decreased functional connectivity with memory systems in depression, potentially explaining anhedonia
- Ketamine reduces metabolism in the lateral OFC, and this reduction correlates with increased hedonia, supporting the theory that quashing the non-reward attractor alleviates depression
- Mania may represent the opposite pattern: decreased sensitivity of lateral OFC non-reward systems (increased impulsivity) combined with increased sensitivity of medial OFC reward systems

### Computational framework

The paper uses **attractor network dynamics** as its core computational framework. Attractor networks are neural networks with strong recurrent excitatory connections that can maintain persistent high firing rates (attractor states) after external input ceases. Key features:

- **Energy landscape**: Attractor states correspond to local minima in an energy landscape; the depth of the minimum determines stability
- **Stochastic dynamics**: Noise from Poisson-like spike timing means attractors can be triggered by subthreshold inputs or maintained longer than appropriate
- **In depression**: The non-reward attractor in lateral OFC has a deeper energy well (more stable), making it easier to trigger and harder to escape
- **Reciprocal inhibition**: Reward (medial OFC) and non-reward (lateral OFC) systems inhibit each other; facilitating reward can suppress non-reward attractors
- **NMDA receptors**: Control the stability of attractor states via excitatory transmission in recurrent collaterals; NMDA blockers (ketamine) reduce attractor stability

### Prevailing model of the system under study

The prevailing view of depression, as described in the paper's introduction, involves:
- Dysfunction in a distributed network including amygdala, subgenual anterior cingulate cortex, medial prefrontal cortex, hippocampus, and dorsolateral prefrontal cortex
- Altered functional connectivity between these regions during emotional processing
- Reduced reward sensitivity (anhedonia) and increased sensitivity to negative information
- The learned helplessness framework: depression arises when no actions can restore rewards

The paper notes that while these neuroimaging findings identify regions involved in depression, they do not provide a mechanistic explanation of how depression becomes persistent or how the mood state is maintained over time.

### What this paper contributes

This paper provides a unified theoretical framework linking depression to the dynamics of attractor networks in the lateral orbitofrontal cortex:

1. **Mechanistic explanation of persistence**: Depression is explained not just as negative mood but as a stable attractor state that self-maintains through recurrent excitation in OFC non-reward neurons. This explains why depressive episodes persist long after triggering events.

2. **Integration of cognitive and emotional factors**: The theory explicitly links OFC non-reward attractors to cognitive systems (language, self-representation, planning) via top-down feedback loops, explaining ruminative thinking as part of the systems-level attractor.

3. **Testable predictions about neuroimaging**: The theory predicts specific patterns of functional connectivity (increased lateral OFC-language connectivity, decreased medial OFC-memory connectivity) that were subsequently confirmed in large-scale resting-state studies.

4. **Treatment implications**: The attractor framework generates specific predictions about how treatments work (ketamine quashes attractors via NMDA blockade; ECT knocks systems out of attractor states; antidepressants facilitate reward systems to reciprocally inhibit non-reward attractors).

5. **Extension to bipolar disorder**: The theory extends naturally to mania as the opposite pattern—decreased lateral OFC non-reward sensitivity (impulsivity) and increased medial OFC reward sensitivity—providing a unified framework for mood disorders.

### Brain regions & systems

- **Lateral orbitofrontal cortex (BA 47/12)**: Core region for non-reward and punishment representation; contains attractor networks that maintain persistent firing after non-reward; overactive in depression; shows increased functional connectivity with language and self-representation areas
- **Medial orbitofrontal cortex (BA 13)**: Reward-related region; shows decreased functional connectivity with memory systems in depression; reciprocally inhibits lateral OFC non-reward system
- **Supracallosal anterior cingulate cortex**: Activated by non-reward and punishment; receives inputs from lateral OFC; involved in action-outcome learning
- **Pregenual cingulate cortex**: Activated by pleasant/rewarding stimuli; receives inputs from medial OFC
- **Subgenual cingulate cortex (BA 24, 25)**: Implicated in depression and autonomic function; target for deep brain stimulation; activated by social rejection
- **Anterior insula**: Involved in autonomic/visceral responses; activated by punishing stimuli; shows increased activity in depression
- **Amygdala**: Activated by pleasant and unpleasant stimuli; implicated in depression but less involved in rule-based reversal learning
- **Dorsolateral prefrontal cortex**: Involved in cognitive control, attention, and short-term memory; provides top-down feedback to OFC; maintains negative cognitive states in depression
- **Angular gyrus**: Language-related area; shows increased functional connectivity with lateral OFC in depression; may contribute to ruminative thoughts
- **Precuneus**: Self-representation and sense of agency; shows increased functional connectivity with lateral OFC in depression; may relate to negative self-esteem
- **Parahippocampal gyrus/medial temporal lobe**: Memory systems; shows reduced functional connectivity with medial OFC in depression

### Mechanistic insight

This paper provides a Marr's three-level analysis of the mechanisms underlying depression:

**Computational level**: The brain must solve the problem of maintaining information about non-reward events to guide behavior change, while not allowing this memory to become pathologically persistent. Depression represents a failure of this computational goal—non-reward information is maintained too stably, leading to persistent negative mood states that no longer track current environmental contingencies.

**Algorithmic level**: The paper proposes that non-reward is represented and maintained via attractor network dynamics in the lateral orbitofrontal cortex. Key algorithmic features include:
- Recurrent excitatory connections among non-reward neurons create stable high-firing-rate states
- Noise from Poisson-like spiking allows attractors to be triggered by subthreshold inputs or to persist longer than appropriate  
- Adaptation in reward neurons can trigger non-reward attractors when expected rewards are not received
- Reciprocal inhibition between reward (medial OFC) and non-reward (lateral OFC) attractor populations
- Systems-level coupling between OFC attractors and cognitive/language systems creates persistent ruminative states

**Implementational level**: The paper identifies specific neural implementations:
- **Lateral orbitofrontal cortex (BA 47/12)**: Contains neurons with persistent non-reward firing; shows altered structure (reduced grey matter) and function (increased connectivity) in depression
- **NMDA receptors**: Control stability of attractor states via excitatory transmission in recurrent collaterals; NMDA blockers (ketamine) reduce attractor stability and alleviate depression
- **GABA**: Stabilizes spontaneous firing rate state; anti-anxiety drugs may increase inhibition to destabilize non-reward attractors
- **Reciprocal circuits**: Medial OFC (reward) and lateral OFC (non-reward) inhibit each other; antidepressants may facilitate reward systems to suppress non-reward attractors
- **Systems-level connectivity**: Lateral OFC connects to language (angular gyrus) and self-representation (precuneus) areas; enhanced connectivity in depression may implement ruminative states

### Limitations & open questions

- The theory focuses specifically on lateral OFC non-reward attractors, but acknowledges that alterations in other cortical areas may relate to other psychiatric disorders (e.g., different attractor alterations in OCD, schizophrenia)
- The relative contributions of orbitofrontal cortex versus subgenual cingulate cortex in depression remain unclear; the paper notes that subgenual cingulate may be an autonomic output region receiving OFC inputs rather than independently computing non-reward
- Whether the reward and non-reward systems have their sensitivity set by independent genes, providing a basis for different patient phenotypes (pure depression vs. bipolar disorder), requires empirical validation
- The paper notes that the longer-term attractor process for mood states (operating on timescales of days to weeks) is less well characterized than the short-term attractors (1-10 seconds)
- The specific biophysical mechanisms that might make lateral OFC attractors more sensitive in depression (e.g., specific genetic variants, chronic stress effects on synaptic properties) are not fully specified

### Connections & keywords

**Key citations**: Thorpe et al. (1983) - original neurophysiological evidence for non-reward neurons; Kringelbach & Rolls (2003) - human imaging of reversal; Deco & Rolls (2005b, 2010, 2016) - attractor network models; Drevets (2007) - neuroimaging of depression; Cheng et al. (2016) - resting state connectivity in depression; Lally et al. (2015) - ketamine effects on OFC; Nusslock et al. (2014) - reward hypersensitivity in mania

**Named models or frameworks**: Attractor network theory; Rolls' theory of emotion; Marr's three levels of analysis; Energy landscape model; Learned helplessness framework; Integrate-and-fire neuronal models

**Brain regions**: Lateral orbitofrontal cortex (BA 47/12); Medial orbitofrontal cortex (BA 13); Supracallosal anterior cingulate cortex; Pregenual cingulate cortex; Subgenual cingulate cortex (BA 24, 25); Anterior insula; Amygdala; Dorsolateral prefrontal cortex; Angular gyrus; Precuneus; Parahippocampal gyrus; Medial temporal lobe

**Keywords**: depression, mania, bipolar disorder, orbitofrontal cortex, attractor networks, non-reward, punishment, reward reversal, NMDA receptors, ketamine, resting state functional connectivity, systems neuroscience, computational psychiatry, top-down cognitive effects, ruminative thoughts
