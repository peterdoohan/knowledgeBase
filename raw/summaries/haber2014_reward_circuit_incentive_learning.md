---
source_file: haber2014_reward_circuit_incentive_learning.md
paper_id: haber2014_reward_circuit_incentive_learning
title: "The Neural Network Underlying Incentive-Based Learning: Implications for Interpreting Circuit Disruptions in Psychiatric Disorders"
authors:
  - "Suzanne N. Haber"
  - "Timothy E.J. Behrens"
year: 2014
journal: Neuron
paper_type: review
contribution_type: review
species:
  - human
tasks:
  - foraging_task
methods:
  - electrophysiology
  - fmri
  - lesion
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - striatum
  - ventral_striatum
  - nucleus_accumbens
  - ventral_tegmental_area
  - substantia_nigra
  - thalamus
  - mediodorsal_thalamus
  - amygdala
frameworks:
  - reinforcement_learning
  - temporal_difference_learning
keywords:
  - reward_circuit
  - incentive_based_learning
  - cortico_basal_ganglia_loops
  - striato_nigro_striatal_spiral
  - reward_prediction_error
  - dopamine
  - orbitofrontal_cortex
  - ventromedial_prefrontal_cortex
  - anterior_cingulate_cortex
  - corticostriatal_convergence
  - habit_formation
  - psychiatric_circuit_disruption
  - white_matter_tractography
  - deep_brain_stimulation
  - neural
  - network
  - underlying
  - incentive
  - based
  - learning
key_citations:
  - behrens2007_learning_value_information_uncertain
---

### One-line summary

This review synthesises the anatomical circuitry and functional organisation of the cortico-basal ganglia reward network — including OFC, ACC, vmPFC, ventral striatum, and midbrain dopamine neurons — and connects circuit-level disruptions to psychiatric disorders including addiction, OCD, and major depressive disorder.

---

### Background & motivation

Incentive-based learning — the development of goal-directed behaviour and habit formation through coupling stimuli and actions with rewarding or aversive outcomes — depends on a distributed network of cortical and subcortical structures. Although the nucleus accumbens and VTA dopamine neurons have long been identified as the core of the reward circuit, the cortical and higher-order subcortical structures that attribute value, associate it with choices, and select action plans are less well integrated in a single account. The review is motivated by a need to synthesise NHP anatomical tracing studies with human neuroimaging (fMRI, dMRI), to resolve the connectivity of white matter pathways linking reward-related regions, and to provide a circuit-level framework for interpreting the pathophysiology of psychiatric diseases.

---

### Methods

This is a narrative review drawing primarily on:

- NHP (non-human primate) neuroanatomical tract-tracing studies establishing connectivity of OFC, vmPFC, dACC, ventral striatum, ventral pallidum, lateral habenula, and midbrain dopamine cells.
- Human structural and functional neuroimaging studies (fMRI, diffusion MRI tractography) used to translate NHP circuitry to the human brain.
- Lesion and electrophysiology studies in NHPs providing functional dissociations across circuit nodes.
- Human fMRI studies of reward prediction errors, reversal learning, valuation, and exploration/exploitation.
- Clinical imaging literature on MDD, OCD, and addiction highlighting circuit-level changes.
- No primary data are collected; synthesis is narrative rather than meta-analytic.

---

### Key findings

- The reward circuit is embedded within the cortico-basal ganglia system, centred on the VS and VTA/SN dopamine neurons, but critically regulated by OFC, vmPFC, and dACC.
- OFC mediates stimulus-outcome associations: caudal OFC processes primary reward linked to sensory stimuli; rostral OFC handles secondary and abstract reward, with a caudorostral gradient supported by differential sensory and prefrontal connectivity.
- vmPFC provides the most robust and flexible valuation signal in the brain; it can compute values on the fly from environmental structure, prior experience, or social inference, and its damage leads to irrational choice (violations of economic transitivity).
- dACC is positioned at the intersection of reward and action networks; it integrates action values, codes prediction errors, tracks learning rate in volatile environments, signals exploration vs exploitation, and is critical for foraging-style decision making.
- Corticostriatal projections are topographically organised (vmPFC → NAcc shell; OFC → NAcc/rostral putamen; dACC → caudate head) but converge extensively within the striatum, forming "critical nodes" where inputs from functionally diverse cortical areas overlap (~15% overlap even between regions 3 cm apart).
- A striato-nigro-striatal spiral interconnects VS with progressively more dorsal (cognitive, then motor) striatal territories via midbrain dopamine cells, providing a mechanistic route through which reward learning leads to habit formation.
- The ventral striatal BOLD reward prediction error signal depends on the structural strength of the nigrostriatal connection (dMRI tractography), and can be restored pharmacologically by L-DOPA in ageing.
- Disruptions in the OFC/vmPFC/dACC-BG network underlie MDD, OCD, and addiction, with consistent changes in the cingulum bundle, uncinate fasciculus, and anterior internal capsule — precisely the white matter targets of DBS and capsulotomy therapies.
- In addiction, the striato-nigro-striatal spiral provides the anatomical substrate for the ventral-to-dorsal striatal recruitment that accompanies the transition from goal-directed drug-seeking to habitual, compulsive use.

---

### Computational framework

The paper does not introduce a new computational model but is organised around a reinforcement learning (RL) conceptual framework. The key computational constructs are:

- **Reward prediction error (RPE)**: the difference between received and expected reward, coded by midbrain DA neurons and reflected in VS BOLD activity. Consistent with temporal difference (TD) learning.
- **Model-based vs model-free learning**: implicitly framed through the distinction between goal-directed (outcome-sensitive) behaviour mediated by OFC/vmPFC/dACC and habitual (outcome-insensitive) behaviour emerging through striato-nigro-striatal transfer to dorsal striatum.
- **Exploration vs exploitation**: dACC is argued to track when new information should be used to update action policies (learning rate modulation, consistent with Bayesian volatility tracking as in Behrens et al., 2007).
- **Foraging**: dACC activity is discussed in the framework of optimal foraging theory (marginal value theorem), with ramping dACC activity signalling when to leave a patch.

The key assumption is that distinct circuit nodes implement distinct computations (stimulus-outcome associations in OFC, state-value integration in vmPFC, action-value integration and policy switching in dACC), and that the BG perform non-linear integration of these signals gated by dopamine.

---

### Prevailing model of the system under study

The baseline model the paper engages with is the **parallel, segregated cortico-basal ganglia loop** framework (Alexander et al., 1990): distinct functional loops (limbic, associative, motor) pass through anatomically separate striatal territories, pallidum/SN, thalamus, and back to cortex. In this model, the VS/NAcc and VTA dopamine neurons constitute the core reward circuit, essentially isolated from cognitive and motor circuits. Motivationally relevant information is thought to transit from the limbic loop to motor output through the "motivation-to-movement interface" (Mogenson et al., 1980), but the anatomical substrate of this interface was underspecified.

The paper's introduction also treats the OFC as primarily a reversal-learning and devaluation system, and the ACC as an error and conflict monitor, and acknowledges that these functional characterisations are contested and incomplete.

---

### What this paper contributes

1. **Against strict segregation**: The review consolidates anatomical evidence that corticostriatal convergence is extensive. Inputs from functionally diverse cortical regions overlap substantially in the striatum, undermining the strictly parallel loops model and providing anatomical support for integration across functional circuits.
2. **Striato-nigro-striatal spiral as the substrate for habit formation**: The review synthesises evidence that the VS influences a broad range of DA neurons projecting to more dorsal (associative and motor) striatal areas, while the dorsal striatum influences a more limited midbrain region. This asymmetry creates a feedforward spiral linking reward learning to habitual action — an explicit mechanistic account of how ventral and dorsal striatum interact.
3. **White matter pathways**: The paper uniquely maps the specific WM bundles (uncinate fasciculus, cingulum bundle, internal/external capsules) through which OFC, vmPFC, and dACC axons travel, providing a basis for interpreting dMRI changes in psychiatric populations and the targets of invasive treatments (DBS, capsulotomy).
4. **Cortical functional gradients**: The caudorostral gradient from primary reward (caudal OFC/insula) to abstract/secondary reward (rostral OFC and vmPFC), and from emotional processing (rostral dACC) to action selection and motor control (caudal dACC), is established as a unifying organisational principle of the network.
5. **Disease circuits**: The review synthesises imaging and lesion evidence showing that addiction, OCD, and MDD each involve characteristic disruption patterns within this shared network, supporting a transdiagnostic circuit-level interpretation of psychiatric illness.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)** — stimulus-outcome association; caudal regions code primary sensory reward; rostral regions code abstract/secondary reward; reversal learning; lies at crossroads of sensory, limbic, and cognitive PFC inputs.
- **Ventromedial prefrontal cortex (vmPFC, especially sACC areas 25/32/14)** — flexible, context-independent value computation; rational choice; core node of the default-mode network; strong links to hypothalamus, amygdala, and hippocampus.
- **Dorsal anterior cingulate cortex (dACC, areas 24/32)** — action-value integration; exploration vs exploitation; learning rate tracking; foraging decisions; positioned between reward and motor networks.
- **Ventral striatum (VS) / nucleus accumbens (NAcc)** — reward prediction error; integration of cortical, amygdala, hippocampal, and DA inputs; critical nodes for integrating cross-functional cortical information.
- **Nucleus accumbens shell (NAccS)** — innermost reward circuit node; receives vmPFC, hippocampus, central amygdala, VTA inputs; target of initial drug-seeking behaviour.
- **Ventral pallidum (VP)** — output target of VS; projects to STN and MD thalamus to complete the cortico-BG loop; responds during reward-incentive behaviour.
- **Lateral habenula (LHb)** — receives pallidal input; inhibits DA cells in response to non-reward signals via RMTg; codes negative prediction errors.
- **Midbrain dopamine neurons (VTA / substantia nigra pars compacta)** — reward prediction error signalling; organised topographically with respect to striatal targets; core of the striato-nigro-striatal spiral.
- **Subthalamic nucleus (STN)** — receives hyperdirect input from vmPFC, OFC, ACC; target of DBS for OCD/MDD.
- **Amygdala** — projects densely to VS (especially basal nucleus to NAcc); linked to OFC and vmPFC; involved in emotional valuation and cue-induced craving.
- **Hippocampus** — projects to NAccS and vmPFC; involved in context-dependent valuation and novel good evaluation via default-mode network.
- **Dorsal prefrontal cortex (dPFC)** — provides top-down cognitive control; projects throughout striatum; impaired in MDD and implicated in impaired inhibitory control in addiction.

---

### Mechanistic insight

The paper meets the bar for providing a mechanistic account at the level of circuitry, though primarily through anatomical and systems neuroscience evidence rather than single-neuron-to-circuit mapping.

**Computational level**: The brain solves the problem of translating reward-related learning into appropriate habits by routing information through a sequence of circuit nodes that progressively transform value signals into action policies. Incentive-based learning requires associating stimuli with outcomes (OFC), evaluating those outcomes in current motivational state (vmPFC), linking them to action options (dACC), and consolidating the most frequently rewarded actions into automatised habits (dorsal striatum).

**Algorithmic level**: The striato-nigro-striatal spiral implements a feedforward transfer algorithm: VS activity influences a broad band of VTA/medial SN DA neurons; these project to the associative striatum; that striatum in turn influences more lateral SN cells projecting to motor striatum. Repeated reward-driven activation propagates the signal ventrally to dorsally, progressively recruiting more habitual/motor circuits. The asymmetry in projection topology (VS projects broadly; dorsal striatum projects narrowly) is critical for this directionality. Within cortex, dACC performs adaptive learning rate computation: its BOLD activity tracks environmental volatility, and its cells code integrated action values with prediction error properties.

**Implementational level**: Partially addressed. Topographic organisation of DA projections (medial VTA → VS shell; lateral SN → dorsolateral striatum) is described at a cell-population level. The role of specific DA cell subtypes, intrastriatal circuit elements (e.g., D1/D2 MSNs), or neuromodulatory details beyond dopamine are not treated. The paper notes the contribution of serotonin (densest in VS), acetylcholine (via nucleus basalis), and GABA (BG output) but does not elaborate mechanisms at the synaptic or cellular level.

**Bonus**: The paper explicitly addresses the physical implementation of the spiral at the level of tract-tracing and connectional topography, and notes that dMRI tractography in humans confirms these structural predictions. Pharmacological restoration of VS RPE signals with L-DOPA in ageing, and its dependence on nigrostriatal tract integrity (DTI), provides a rare bridge between structural connectivity, dopamine function, and RL-derived prediction error signals.

---

### Limitations & open questions

- The review acknowledges that most NHP anatomy studies document the endpoints of connections but not the fibre trajectories between them — a gap that limits direct translation to dMRI tractography findings in humans.
- Cross-species homology of prefrontal cortical areas (especially parts of area 32 and 10) is acknowledged as uncertain; some regions may not exist in NHPs.
- The functional boundary between VS and VP is often unresolvable at imaging resolution, complicating interpretation of human data.
- The corticostriatal convergence zones ("critical nodes") are identified anatomically but their functional role has not been empirically investigated using imaging in humans.
- The paper identifies a gap in simultaneous multi-region recordings that would be needed to test how different cortical processes are integrated into single behavioural outputs; current data are mostly from single-region approaches.
- Questions about how parallel cortical decision processes (OFC vs dACC) compete or are arbitrated remain speculative.
- The role of dMRI-identified white matter changes in psychiatric diseases is correlational; causal direction is unestablished.
- The paper does not systematically address how task demands, individual differences, or developmental factors modulate the relative dominance of different circuit nodes.

---

### Connections & keywords

**Key citations**:
- Alexander et al. (1990) — parallel cortico-BG loop model
- Olds and Milner (1954) — original reward self-stimulation discovery
- Mogenson et al. (1980) — motivation-to-movement interface
- Belin and Everitt (2008) — striato-nigro-striatal spiral and addiction
- Schultz (2002) — midbrain DA reward prediction error coding
- Haber et al. (2000, 2006) — primate corticostriatal connectivity
- Behrens et al. (2007) — dACC and learning rate in volatile environments
- Mayberg et al. (2005) — DBS for treatment-resistant MDD
- Rudebeck et al. (2008) — double dissociation OFC vs ACC
- Camille et al. (2011b) — double dissociation in humans
- D'Ardenne et al. (2008) — VTA BOLD reward prediction error
- Chowdhury et al. (2013) — nigrostriatal tract connectivity and RPE
- Kolling et al. (2012) — ACC foraging vs vmPFC neuroeconomic choice

**Named models or frameworks**:
- Parallel cortico-basal ganglia loops (Alexander et al., 1990)
- Striato-nigro-striatal spiral (Haber et al., 2000)
- Reward prediction error / temporal difference learning (Schultz framework)
- Default-mode network
- Optimal foraging / marginal value theorem (applied to dACC)
- Exploration-exploitation trade-off
- Reward devaluation paradigm
- Stimulus-outcome reversal learning

**Brain regions**:
Orbitofrontal cortex (OFC), ventromedial prefrontal cortex (vmPFC), subgenual anterior cingulate cortex (sACC), dorsal anterior cingulate cortex (dACC), dorsal prefrontal cortex (dPFC), ventral striatum (VS), nucleus accumbens (NAcc), nucleus accumbens shell (NAccS), ventral pallidum (VP), lateral habenula (LHb), ventral tegmental area (VTA), substantia nigra pars compacta (SNc), subthalamic nucleus (STN), amygdala, hippocampus, thalamus (MD nucleus), insula

**Keywords**:
reward circuit, incentive-based learning, cortico-basal ganglia loops, striato-nigro-striatal spiral, reward prediction error, dopamine, orbitofrontal cortex, ventromedial prefrontal cortex, anterior cingulate cortex, corticostriatal convergence, habit formation, psychiatric circuit disruption, white matter tractography, deep brain stimulation
