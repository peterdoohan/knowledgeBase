---
source_file: braun2018_maps_network_mental_disorders.md
paper_id: braun2018_maps_network_mental_disorders
title: "From Maps to Multi-dimensional Network Mechanisms of Mental Disorders"
authors:
  - "Urs Braun"
  - "Axel Schaefer"
  - "Richard F. Betzel"
  - "Heike Tost"
  - "Andreas Meyer-Lindenberg"
  - "Danielle S. Bassett"
year: 2018
journal: Neuron
paper_type: review
contribution_type: theoretical
species:
  - human
brain_regions:
  - prefrontal_cortex
  - striatum
  - ventral_striatum
keywords:
  - network_neuroscience
  - graph_theory
  - connectome
  - multilayer_networks
  - temporal_network_flexibility
  - generative_network_models
  - wiring_rules
  - wiring_cost
  - network_control_theory
  - controllability
  - control_energy
  - schizophrenia
  - dysconnectivity
  - state_instability
  - nmda_receptor
  - glutamate
  - pharmacological_imaging
  - trans_diagnostic_psychiatry
  - rdoc
  - structure_function_relationships
wiki_pages:
  - wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction
---

### One-line summary

This review argues that moving from descriptive graph-theoretical mapping of brain networks to three mechanistic tools — multilayer networks, generative network models, and network control theory — is necessary to explain the circuit-level dysfunction underlying mental disorders.

---

### Background & motivation

Network neuroscience has produced detailed maps of the human connectome and identified graph-theoretical abnormalities in psychiatric disorders, yet translational impact remains limited because these approaches are fundamentally descriptive. Statistical differences in graph parameters and correlations with behaviour do not constitute mechanistic explanations. The authors contend that understanding why network differences exist and how structural aberrations causally produce dysfunction requires a shift from mapping to mechanism, and that three families of methods from complex systems science are positioned to enable this shift. The review is explicitly framed around the NIMH Research Domain Criteria (RDoC) goal of identifying trans-diagnostic mechanisms of psychopathology.

---

### Methods

This is a narrative review covering three computational approaches and their translational potential:

- **Multilayer networks**: extension of single-layer graphs by adding dimensions of time, imaging modality, or frequency band; enables modelling of dynamic network reconfiguration and integration of multi-modal data.
- **Generative network models**: simulate network growth under hypothesised wiring rules (e.g., penalising long-distance connections, favouring overlap of neighbourhoods); goodness-of-fit to real connectomes is used to infer which rules plausibly drive actual network formation or development.
- **Network control theory**: treats the structural connectome as the coupling matrix of a linear dynamical system; defines average controllability (ease of reaching many states) and modal controllability (ability to reach hard-to-reach states); computes minimum control energy for state transitions.

Literature covered spans graph-theoretical connectomics, developmental neuroimaging, psychiatric neuroscience (schizophrenia, autism, bipolar disorder, depression, TBI, epilepsy), and pharmacological imaging. Synthesis is narrative with illustrative empirical examples drawn primarily from the authors' own group (Braun et al. 2015, 2016; Betzel et al. 2016a/b; Gu et al. 2015, 2017).

---

### Key findings

- Traditional graph-theoretical measures are descriptive and cannot by themselves explain the causal mechanisms by which structural network differences produce pathological dynamics.
- Multilayer temporal network analyses show that functional networks dynamically reconfigure during working memory, learning, and attention; schizophrenia patients and first-degree relatives display less efficient reconfiguration (higher flexibility/instability), and this can be mimicked in healthy controls by NMDA receptor antagonism (dextromethorphan), implicating glutamate in network state instability.
- Generative models demonstrate that healthy human functional networks evolve under an economic trade-off between minimising wiring distance and preserving topological complexity; schizophrenia patients show a lower penalty for wiring cost, suggesting aberrant regulation of axon guidance and neuronal migration. The relative influence of distance versus topological overlap as wiring rule changes across healthy aging.
- Network control theory in healthy adults identifies a double dissociation: default-mode network regions support average controllability (easy-to-reach states), while frontoparietal cognitive control regions support modal controllability (hard-to-reach states). Following mild traumatic brain injury, mean control efficiency is significantly reduced.
- The structural randomisation observed in schizophrenia (less modular, fewer hubs) predicts reduced energetic cost of state transitions in control-theoretic terms, offering a potential mechanistic account of impaired state stability.
- Psychiatric heterogeneity (e.g., 636,120 valid PTSD symptom combinations; 1,030 unique depression profiles in 3,703 outpatients) and high comorbidity rates argue that DSM-categorical neuroimaging studies will remain underpowered to detect biological mechanisms; RDoC-aligned trans-diagnostic approaches are advocated.

---

### Computational framework

The paper's central computational thesis rests on three frameworks:

1. **Multilayer network theory** (Kivela et al. 2014): brain networks are represented as stacks of adjacency matrices linked across time or modality; intra-layer edges capture spatial connectivity, inter-layer edges capture temporal or modal dependencies. Community detection algorithms (e.g., Louvain with resolution parameter γ and inter-layer coupling ω) identify time-resolved modules. Key quantities: module allegiance, flexibility (fraction of time a node changes community assignment), and promiscuity.

2. **Generative network models**: a probability rule over node pairs (combining Euclidean distance and topological overlap) is used to grow synthetic networks iteratively; the model with highest Kolmogorov-Smirnov fitness across multiple topological metrics is selected. Underlying assumption: the winning wiring rule reflects actual evolutionary or developmental pressures on network formation.

3. **Network control theory** (linear time-invariant system): brain state x(t+1) = Ax(t) + Bu(t), where A is the normalised structural adjacency matrix, B identifies control nodes, and u(t) is the control input. Average controllability of region i = trace of the controllability Gramian when region i is the sole input node. Modal controllability relates to the smallest eigenvalue mode. The framework assumes linearity and time-invariance, known to be approximations. Minimum control energy defines how easily the system transitions between empirically observed brain states.

---

### Prevailing model of the system under study

The field had adopted the view that mental disorders are disorders of brain connectivity ("disconnection syndromes"), supported by graph-theoretical analyses showing altered hub structure, modularity, path length, and clustering in conditions including schizophrenia, depression, and autism. The prevailing analytical mode was to compare groups on topological metrics or correlate them with symptom severity. This gave rise to rich descriptive catalogues — "disease A has lower clustering coefficient than controls" — but offered no account of why structural differences produce the observed dynamics, or how perturbations propagate through circuits. The conceptual framework was implicitly static and correlative; dynamics were sometimes acknowledged but rarely formalised. The introduction acknowledges the Wernicke tradition of viewing mental illness as resulting from altered inter-regional interactions, but notes that the neuroimaging community had not yet developed the modelling tools to go beyond statistical characterisation of those interactions.

---

### What this paper contributes

The review establishes a conceptual roadmap for moving from description to mechanism in psychiatric neuroimaging. Its core contributions are:

- **Synthesis of three mechanistic frameworks** and explicit articulation of what each can offer that conventional graph theory cannot: time-resolved modularity (multilayer networks), inference about generative wiring rules (generative models), and energetic predictions about state transitions and intervention targets (control theory).
- **Mechanistic account of schizophrenia network instability**: the structural randomisation documented in schizophrenia (reduced modularity, fewer hubs) is linked, via control theory, to less energetically costly — and therefore less stable — state transitions. This is a concrete, falsifiable mechanistic hypothesis connecting structural and functional findings.
- **Glutamatergic mechanism for dynamic network instability**: the pharmacological mimicry of schizophrenia-like network flexibility increases using an NMDA antagonist in healthy subjects points to glutamate as a molecular driver of system-level dynamic instability.
- **Translational agenda**: the paper sketches how the three tools can be combined with pharmacological challenge, imaging genetics, cross-species approaches, and brain stimulation to probe mechanisms and identify therapeutic targets in a trans-diagnostic, RDoC-compatible framework.

---

### Brain regions & systems

- **Default-mode network** — identified as the seat of high average controllability; supports transitions to easy-to-reach brain states.
- **Frontoparietal / cognitive control network** — identified as the seat of high modal controllability; facilitates transitions to difficult, cognitively demanding states.
- **Prefrontal cortex** — central to state stability and executive function; target for deep brain stimulation and neurofeedback hypotheses.
- **White matter structural connectome (whole brain)** — backbone for control-theoretic modelling; diffusion spectrum imaging used to derive coupling matrices.
- **Functional brain networks (whole brain, resting and task)** — assessed via fMRI BOLD; community structure and temporal flexibility are the primary measures.
- The paper does not focus on specific subcortical regions in detail, though dopaminergic and glutamatergic systems (implicitly ventral striatum, prefrontal dopamine) are invoked at the circuit-mechanism level.

---

### Mechanistic insight

The paper does not meet the full bar for this section as defined: it is a review that proposes and synthesises mechanistic frameworks, but does not itself present neural recordings, imaging, or pharmacological data that directly pit one algorithm against another.

The closest approach is the Braun et al. (2016) result — cited within this review — showing that NMDA receptor antagonism in healthy subjects induces the same pattern of elevated network flexibility seen in schizophrenia patients, suggesting glutamatergic dysfunction as the implementational driver of dynamic network instability. However, this evidence points toward a neuropharmacological mechanism rather than a formally specified algorithm tested against alternatives.

The paper proposes but does not empirically demonstrate that network control theory provides a correct algorithmic account of how the brain navigates state transitions. The control-theoretic framework (linear time-invariant system) is acknowledged to be a first approximation; the authors explicitly note that transitions among more realistic, data-driven brain states remain to be modelled.

---

### Limitations & open questions

- Linear time-invariant assumption in network control theory is a simplification; real neural dynamics are nonlinear and non-stationary.
- Goodness-of-fit in generative models is necessary but not sufficient for mechanistic inference — similar structure can arise from different processes.
- It is unclear which topological parameters best evaluate synthetic network fitness for different disorder contexts.
- Psychiatric heterogeneity (diagnostic and biological) means that group-level neuroimaging comparisons may systematically obscure the mechanisms they seek to reveal; individual-level modelling approaches are needed but not yet operational.
- Translation from healthy-subject control-theoretic profiles to clinical target identification requires extensive validation not yet achieved.
- Most current generative models incorporate only intrinsic topological features; biologically derived parameters (gene expression, regional plaque load, neurotransmitter distributions) have not yet been systematically integrated.
- The relationship between observed neuroimaging signals and underlying neurovascular coupling and neural computation remains incompletely understood.
- Cross-species validation of network control principles is required but not yet available.

---

### Connections & keywords

**Key citations:**
- Kivela et al. (2014) — multilayer network theory
- Vertes et al. (2012) — generative models of functional brain networks and schizophrenia
- Betzel et al. (2016a) — generative models of structural connectome across aging
- Betzel et al. (2016b) — network control theory and the structural connectome
- Gu et al. (2015) — average and modal controllability in structural brain networks
- Gu et al. (2017) — altered controllability in mild traumatic brain injury
- Braun et al. (2015) — dynamic network reconfiguration and working memory/cognitive flexibility
- Braun et al. (2016) — schizophrenia genetic risk, NMDA receptor function, and network flexibility
- Bassett and Sporns (2017) — network neuroscience review
- Bullmore and Sporns (2009, 2012) — complex brain networks and economy of organisation
- Insel (2010) / RDoC framework

**Named models or frameworks:**
- Multi-dimensional network neuroscience (coined by authors)
- Research Domain Criteria (RDoC, NIMH)
- The Virtual Brain (whole-brain biophysical network modelling platform)
- Louvain community detection with multilayer extension
- Preferential attachment model (Barabasi-Albert)
- Linear time-invariant (LTI) control model of the connectome

**Brain regions:**
- Default-mode network
- Frontoparietal / cognitive control network
- Prefrontal cortex
- Whole-brain structural connectome

**Keywords:**
- network neuroscience, graph theory, connectome
- multilayer networks, temporal network flexibility
- generative network models, wiring rules, wiring cost
- network control theory, controllability, control energy
- schizophrenia, dysconnectivity, state instability
- NMDA receptor, glutamate, pharmacological imaging
- trans-diagnostic psychiatry, RDoC
- structure-function relationships, brain state transitions

### Related wiki pages
- [[wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction|Computational models of schizophrenia: attractor dynamics and NMDA hypofunction]]
