---
source_file: rolls2021_attractor_neurodynamics_schizophrenia.md
paper_id: rolls2021_attractor_neurodynamics_schizophrenia
title: "Attractor cortical neurodynamics, schizophrenia, and depression"
authors:
  - "Edmund T. Rolls"
year: 2021
journal: "Translational Psychiatry"
paper_type: computational
contribution_type: theoretical
species:
  - human
methods:
  - fmri
  - computational_modeling
brain_regions:
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - thalamus
  - posterior_cingulate_cortex
frameworks:
  - attractor_networks
keywords:
  - attractor_networks
  - computational_psychiatry
  - cortical_neurodynamics
  - depression
  - functional_connectivity
  - gaba
  - nmda_receptors
  - orbitofrontal_cortex
  - prefrontal_cortex
  - schizophrenia
  - short_term_memory
  - stochastic_dynamics
  - working_memory
  - attractor
  - cortical
  - neurodynamics
---

### One-line summary

A unifying attractor network framework linking reduced NMDA receptor function and GABA-mediated inhibition to the cognitive, negative, and positive symptoms of schizophrenia, and proposing a non-reward attractor theory of depression involving altered functional connectivity of the medial and lateral orbitofrontal cortex.

### Background & motivation

Schizophrenia and depression are major psychiatric disorders with diverse symptom profiles that have been difficult to explain with unified neurobiological frameworks. The attractor network approach offers a computational neuroscience lens to understand how alterations in cortical circuit stability, driven by changes in glutamatergic and GABAergic neurotransmission, could produce the characteristic symptoms of these disorders. This work integrates computational modeling with empirical neuroimaging to provide mechanistic explanations for psychiatric phenomenology.

### Methods

- **Computational modeling**: Integrate-and-fire attractor network simulations with spiking neurons, NMDA receptor-activated voltage-dependent ion channels, and AMPA/GABA receptor currents
- **Network architecture**: Excitatory pyramidal neurons with recurrent collateral connections organized into selective pools (S1, S2) and non-selective pools, plus inhibitory interneuron pools
- **Parametric manipulations**: Systematic reduction of NMDA conductances (4.5% decrease), GABA conductances (9% decrease), and combined reductions to model schizophrenia
- **Empirical validation**: Resting-state fMRI functional connectivity analysis in 123 chronic schizophrenia patients vs 136 controls, and 181 patients vs 208 controls for effective connectivity
- **Depression studies**: Voxel-level resting-state functional connectivity in 421 major depressive disorder patients vs 488 controls; monetary incentive delay task fMRI in 1140 adolescents at age 19 and 1877 at age 14

### Key findings

- **Schizophrenia - Cognitive symptoms**: Reduced NMDA receptor function decreases firing rates and destabilizes high-firing-rate attractor states in prefrontal cortex, producing shallow basins of attraction that impair working memory and attention maintenance; the high-firing-rate state persisted on fewer trials with NMDA reduction
- **Schizophrenia - Negative symptoms**: Reduced NMDA function in orbitofrontal and anterior cingulate cortex reduces reward-related firing rates, producing apathy, anhedonia, and emotional withdrawal; these regions show reduced BOLD activation to reward in patients
- **Schizophrenia - Positive symptoms**: Reduced GABA-mediated inhibition destabilizes the spontaneous low-firing-rate state, making it more likely that noise-induced jumps will trigger high-firing-rate attractor states without external input, producing hallucinations and delusions; combined NMDA and GABA reduction produces wandering between attractor states (Fig. 5)
- **Functional connectivity in schizophrenia**: Significantly reduced functional connectivity between many brain regions; increased temporal variability of functional connectivity in early visual cortex, temporal lobe, and orbitofrontal cortex indicating instability; sensory thalamic relays (lateral and medial geniculate) showed reduced connectivity while association thalamic nuclei showed increased connectivity
- **Directional connectivity in schizophrenia**: Forward (bottom-up) effective connectivity was reduced while backward (top-down) connectivity was relatively preserved or increased; this biases processing toward internal representations over external sensory inputs
- **Precuneus/posterior cingulate findings**: High effective connectivity directed away from precuneus and posterior cingulate cortex in schizophrenia; these regions are implicated in self-representation, autobiographical memory, and default mode network function
- **Depression - Orbitofrontal cortex functional connectivity**: In major depressive disorder, lateral orbitofrontal cortex (non-reward/punishment) showed increased functional connectivity with precuneus, angular gyrus, and temporal visual cortex; medial orbitofrontal cortex (reward) showed decreased functional connectivity with parahippocampal gyrus and medial temporal lobe memory systems
- **Depression - Orbitofrontal cortex activations**: In adolescents with depression symptoms, lateral orbitofrontal cortex showed increased activation to non-reward (No-Win condition); medial orbitofrontal cortex showed reduced sensitivity to reward magnitude
- **Treatment implications**: Antidepressant medication reduced elevated lateral orbitofrontal cortex functional connectivity but did not ameliorate reduced medial orbitofrontal cortex connectivity, suggesting scope for treatments targeting reward systems

### Computational framework

**Attractor networks / autoassociative memory networks**: The core framework is dynamical systems theory applied to cortical circuits. Attractor networks are recurrent neural networks with associatively modifiable synaptic connections between pyramidal cells that can maintain stable firing rate states (attractors) even after external input ceases. The framework posits two types of stable fixed points: (1) a spontaneous state with low firing rates, and (2) one or more high-firing-rate persistent states that implement short-term memory, attention, and decision-making. The stability of each state is characterized by the depth of its basin of attraction in an energy landscape, which determines how long the system remains in that state under noise. The noise arises from Poissonian spiking of individual neurons and finite-size effects. The depth of basins depends on recurrent collateral synaptic strength, firing rates, and the balance of excitation (NMDA-mediated) and inhibition (GABA-mediated).

### Prevailing model of the system under study

Before this work, schizophrenia research was dominated by the dopamine hypothesis and disconnectivity hypothesis. The dopamine hypothesis posited that hyperdopaminergic activity in mesolimbic pathways caused positive symptoms, while hypodopaminergic activity in mesocortical pathways caused negative symptoms. The disconnectivity hypothesis (Friston & Frith, 1995) proposed that schizophrenia involves reduced functional connectivity between brain regions, particularly prefrontal and temporal areas. For depression, prevailing models included monoamine deficiency hypotheses (serotonin, norepinephrine) and more recent network dysfunction models, but lacked a unified computational framework linking specific brain regions to the phenomenology of reward and non-reward processing. The paper explicitly frames its contribution as extending beyond these prevailing hypotheses by providing a mechanistic, dynamical systems account of how specific neurobiological alterations produce the characteristic symptom profiles.

### What this paper contributes

This paper provides a unified computational framework that links specific neurobiological alterations to the full symptom profile of schizophrenia through the lens of attractor network stability. It extends beyond the disconnectivity hypothesis by showing not just reduced connectivity but reduced dynamical stability manifested as increased temporal variability of functional connectivity. It identifies a directional asymmetry in connectivity changes: forward (bottom-up) connectivity is reduced while backward (top-down) connectivity is relatively preserved, biasing processing toward internal representations over external inputs. This provides a mechanism for phenomenological experiences of disconnection from reality and thought disorder. For depression, the paper introduces a novel non-reward attractor theory that posits over-connected and over-sensitive non-reward/punishment systems in the lateral orbitofrontal cortex coupled with under-connected reward systems in the medial orbitofrontal cortex. This provides a mechanistic account of rumination, anhedonia, and negative cognitive biases. The framework generates testable predictions about functional connectivity patterns that were empirically validated in large-scale neuroimaging studies, and suggests novel treatment targets including normalization of medial orbitofrontal cortex function in depression.

### Brain regions & systems

- **Prefrontal cortex (dorsolateral)** — locus of working memory and attention deficits in schizophrenia; reduced NMDA function destabilizes high-firing-rate attractor states, producing shallow basins of attraction and cognitive symptoms
- **Orbitofrontal cortex (lateral)** — non-reward/punishment processing; over-connected and over-sensitive in depression, maintaining negative attractor states; reduced firing rates in schizophrenia contribute to negative symptoms
- **Orbitofrontal cortex (medial)** — reward processing; under-connected and under-sensitive in depression, contributing to anhedonia; involved in pleasure and motivation
- **Anterior cingulate cortex** — reward, motivation, and emotion processing; reduced firing rates in schizophrenia contribute to negative symptoms
- **Temporal lobe** — semantic memory and auditory association cortex; shallow attractor basins may produce loose associations, bizarre thoughts, and hallucinations
- **Precuneus** — sense of self, agency, autobiographical memory; increased effective connectivity in schizophrenia may contribute to altered self-representation and delusions
- **Posterior cingulate cortex** — memory, navigation, default mode network; increased back-projection connectivity in schizophrenia may bias toward internal memory-based processing
- **Hippocampal system (parahippocampal gyrus)** — memory system; reduced functional connectivity with medial orbitofrontal cortex in depression; increased connectivity from precuneus in schizophrenia
- **Thalamus (lateral and medial geniculate nuclei)** — sensory relay; reduced functional connectivity in schizophrenia, suggesting reduced sensory input processing
- **Thalamus (association nuclei)** — increased functional connectivity in schizophrenia, suggesting altered cortico-thalamo-cortical loops

### Mechanistic insight

This paper provides a strong mechanistic account that maps Marr's three levels:

**Computational level**: The brain implements short-term memory, attention, and decision-making through attractor dynamics that maintain stable neuronal firing patterns. Psychiatric symptoms arise when the stability of these attractor states is altered—either reduced stability producing cognitive symptoms and disorganized thought, or destabilized spontaneous states producing intrusive high-firing-rate states (hallucinations/delusions). Depression is framed as over-stability of non-reward attractor states that maintain negative cognitive and emotional states.

**Algorithmic level**: The attractor network implements memory and decision-making through recurrent collateral connections between pyramidal cells with Hebbian-learned synaptic weights. The stability of attractor states depends on the depth of basins in an energy landscape determined by: (1) recurrent synaptic strength, (2) neuronal firing rates (modulated by NMDA receptor conductances), and (3) inhibitory tone (GABA conductances). The network dynamics are subject to noise from Poissonian spiking and finite-size effects, which can induce transitions between attractor states when basins are shallow.

**Implementational level**: The framework is implemented through specific neurobiological mechanisms: NMDA receptor hypofunction reduces excitatory currents and neuronal firing rates, shallowing high-firing-rate attractor basins; GABAergic hypofunction reduces inhibition, destabilizing the spontaneous state and allowing noise-induced transitions to high-firing-rate states; dendritic spine loss reduces synaptic strength and recurrent excitation. These mechanisms are region-specific: dorsolateral prefrontal cortex (working memory/cognition), orbitofrontal cortex (reward/emotion), temporal lobe (semantic/auditory processing). The framework is validated through empirical fMRI showing reduced functional connectivity, increased temporal variability of connectivity, and altered directional connectivity in schizophrenia; and altered orbitofrontal connectivity and activation patterns in depression.

### Limitations & open questions

- The framework primarily focuses on cortical mechanisms and does not fully integrate subcortical contributions (e.g., dopaminergic, serotonergic systems) that are known to be involved in schizophrenia and depression, though the paper notes these as complementary approaches
- The computational models use simplified network architectures (hundreds to thousands of neurons) compared to the full scale of cortical circuits, though the paper presents evidence that finite-size effects remain relevant at biological scales
- The neuroimaging findings are correlational; the causal link between altered functional connectivity patterns and specific symptoms requires further experimental validation through interventions or longitudinal studies
- The framework does not fully explain individual differences in symptom profiles or why some individuals with similar neurobiological alterations develop different disorders
- The treatment implications (e.g., normalizing medial orbitofrontal cortex function in depression) are hypotheses that require clinical trials for validation
- The paper does not address how the proposed mechanisms interact with environmental factors (stress, trauma) that are known risk factors for depression and schizophrenia
- The role of neurodevelopmental factors in shaping the attractor network properties that predispose to these disorders is not fully explored

### Connections & keywords

**Key citations**:
- Loh, Rolls & Deco (2007) - foundational dynamical systems hypothesis of schizophrenia
- Rolls, Loh, Deco & Winterer (2008) - computational models of schizophrenia and dopamine modulation
- Friston & Frith (1995) - disconnectivity hypothesis of schizophrenia
- Rolls, Cheng & Feng (2020) - orbitofrontal cortex, reward, emotion and depression
- Rolls (2016, 2018) - non-reward attractor theory of depression
- Cheng et al. (2016) - medial reward and lateral non-reward orbitofrontal cortex circuits in depression
- Hopfield (1982) - neural networks and emergent collective computational abilities
- Rolls & Deco (2010) - The Noisy Brain: stochastic dynamics as a principle of brain function

**Named models or frameworks**:
- Attractor network / autoassociation network framework
- Energy landscape / basin of attraction formalism
- Dynamical systems hypothesis of schizophrenia
- Non-reward attractor theory of depression
- Disconnectivity hypothesis (extended)
- Systems-level attractor theory (depression)

**Brain regions**:
- Prefrontal cortex (dorsolateral)
- Orbitofrontal cortex (lateral and medial)
- Anterior cingulate cortex
- Temporal lobe
- Precuneus
- Posterior cingulate cortex
- Hippocampal system (parahippocampal gyrus)
- Thalamus (lateral geniculate, medial geniculate, association nuclei)

**Keywords**:
attractor networks, computational psychiatry, cortical neurodynamics, depression, functional connectivity, GABA, NMDA receptors, orbitofrontal cortex, prefrontal cortex, schizophrenia, short-term memory, stochastic dynamics, working memory
