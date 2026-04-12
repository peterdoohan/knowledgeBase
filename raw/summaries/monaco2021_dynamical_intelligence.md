---
source_file: monaco2021_dynamical_intelligence.md
paper_id: monaco2021_dynamical_intelligence
title: "A brain basis of dynamical intelligence for AI and computational neuroscience"
authors:
  - "Joseph D. Monaco"
  - "Kanaka Rajan"
  - "Grace M. Hwang"
year: 2021
journal: "Frontiers in Computational Neuroscience (perspective article)"
paper_type: review
contribution_type: theoretical
brain_regions:
  - hippocampus
  - entorhinal_cortex
  - prefrontal_cortex
  - medial_temporal_lobe
frameworks:
  - successor_representation
  - active_inference
keywords:
  - dynamical_systems_neuroscience
  - neural_oscillations
  - cross_frequency_coupling
  - quasiattractor_dynamics
  - cell_assembly
  - temporal_coding
  - sparse_connectivity
  - small_world_networks
  - rich_club_organisation
  - computational_neuroscience_ai_convergence
  - agentic_learning
  - token_based_neural_computation
  - brain
  - basis
  - dynamical
  - intelligence
  - computational
  - neuroscience
---

### One-line summary

This perspective argues that temporal dynamics — expressed through neural synchrony, nested oscillations, and flexible quasiattractor sequences — constitute a computational layer of biological intelligence that AI and computational neuroscience must jointly theorise to bridge the gap between current deep learning and brain-like cognition.

---

### Background & motivation

Current deep neural networks fail to achieve hallmark features of biological intelligence: abstraction, causal learning, compositional generalisation, and energy efficiency. Scaling up models has not resolved these gaps. The authors argue that the field needs new theories grounded in the brain's actual computational organisation, and that computational neuroscience (CN) should play a central mediating role between neuroscience and AI. The paper addresses the absence of a principled account of what computational machinery in the brain underlies flexible, adaptive, hierarchically organised behaviour.

---

### Methods

This is a theoretical perspective and review article. The synthesis approach:

- Draws on dynamical systems theory, network neuroscience, and cognitive science to construct an integrated framework.
- Reviews empirical findings on cortical network structure (sparsity, small-world properties, rich clubs, log-skewed connectivity).
- Reviews findings on neural oscillations (frequency bands, cross-frequency coupling, nested oscillations, travelling waves) and their computational interpretations.
- Introduces a novel conceptual unit — the "token" — grounded in the Lashley-Hebb cell assembly formalism and quasiattractor dynamics.
- Draws on one of the authors' own prior empirical work (Monaco et al. 2014, hippocampal place-cell formation via head scanning) as a case study of sparse, interactive learning.
- Covers literature on biologically plausible alternatives to backpropagation and agent-centred learning paradigms.

---

### Key findings

- Structural sparsity (< 1–2% connectivity in cortico-limbic circuits) combined with log-skewed (scale-free) afferent and efferent distributions produces a pseudohierarchical physical layer enabling flexible abstraction and generalisation — a property absent in standard dense ANNs.
- Neural oscillations across frequency bands (from circadian to ripples ~100–200 Hz) follow log-spaced intervals (~e ratio between bands), are evolutionarily conserved across mammals, and form a spatiotemporal hierarchy via phase-amplitude cross-frequency coupling (CFC).
- Slow oscillations entrain remote areas into directional sender/receiver channels in under one cycle, enabling flexible inter-regional communication through phase organisation rather than merely rate coding.
- The authors propose "tokens" as the functional unit of cortical computation: discrete, ergodically self-sustaining causal invariance classes that arise from the activation of latent cell-assembly memory states into quasiattractor orbits; tokens bridge the gap between dynamical microstates and functional cognitive states.
- Short-term synaptic depression and neuronal adaptation can robustly destabilise active attractor states and drive sequential token production without requiring asymmetric connectivity.
- Sparse, volitional, interactive learning events (e.g., rats' head scans predicting hippocampal place-field formation on the next lap) are proposed as a model for global learning signals that current CN frameworks underemphasise.
- The paper critiques both fields: neuroscience for reductionist necessary-and-sufficient circuit logic lacking ethological relevance; AI for entrenchment around backpropagation and benchmark culture that disincentivises qualitatively new models.

---

### Computational framework

The paper proposes a **dynamical systems** framework centred on quasiattractor networks and oscillatory hierarchy:

- **Core formalism**: Intelligence is modelled as temporally ordered sequences of discrete tokens — causal invariance classes — that are discretised by quasiattractor basins in the brain's complex energy landscape. Tokens transiently self-sustain activation through reentrant synaptic loops (cell assemblies) and competitively suppress successor states.
- **Key variables**: oscillatory phase (especially cross-frequency coupling), token identity (active attractor state), quasiattractor energy landscape, sparse connectivity structure (specialists vs. generalists).
- **Assumptions**: (1) Biological intelligence is fundamentally temporal and action-oriented; (2) computation "bottoms out" in mechanistic sublevels of neural organisation rather than abstract rate-coded representations; (3) structural sparsity and log-skewed connectivity are necessary preconditions for, not incidental to, flexible cognition.
- The framework integrates elements of **predictive coding** (beta/gamma carrying prediction/error), **Hebbian cell assemblies**, **Hopfield-style attractors**, and **free energy / active inference** (briefly invoked via Friston citations).

---

### Prevailing model of the system under study

The paper's introduction frames current understanding as dominated by two inadequate paradigms:

1. **In AI**: deep neural networks trained with backpropagation on large datasets achieve impressive performance on perception and language tasks but are implicitly treated as sufficient models of intelligence. The scaling hypothesis (more data, larger models) is the dominant strategy.
2. **In computational neuroscience**: the field prioritises local, microscale plasticity mechanisms and necessary-and-sufficient circuit explanations of experimenter-defined behaviours, with little integration of global learning signals or temporal dynamics. Connectomics is presented as the dominant neurotechnology thrust.

The paper argues that both paradigms share a blind spot: they treat timing as incidental (computationalism's "timing agnosticism") rather than as a primary computational resource. The prevailing brain model implicitly assumes that synaptic weights are the primary carrier of computation, with oscillations as epiphenomenal.

---

### What this paper contributes

The paper contributes a unified theoretical vocabulary for a **dynamical intelligence** framework that neither pure AI nor pure CN currently provides:

- It elevates temporal dynamics (oscillatory hierarchy, phase codes, CFC) from epiphenomenon to primary computational layer.
- It introduces the "token" concept to bridge the Lashley-Hebb cell assembly (latent memory state) and dynamical microstates, providing a mechanistic unit of cortical computation that is discrete, syntactic, and causally grounded.
- It argues that structural sparsity and log-skewed connectivity are not just efficiency constraints but active ingredients of the brain's computational architecture.
- It proposes that agentic, interactive, sparse learning events provide the global learning signal that current models (both RL-based AI and local-plasticity CN) lack.
- The paper sets an agenda for convergence: AI needs richer temporal and structural inductive biases; CN needs global, ethologically relevant learning theories and more transparent computational practices.

---

### Brain regions & systems

- **Cortico-limbic system (hippocampus, neocortex, entorhinal cortex)** — primary focus; discussed as the substrate for hierarchical long-term memory networks, cell assemblies, and oscillatory dynamics.
- **Hippocampus** — specific locus of place-cell map formation via volitional head-scanning; also discussed for sharp-wave ripples, theta sequences, and systems consolidation.
- **Medial temporal lobe / hippocampal-entorhinal complex** — discussed as the hub for systems consolidation and grounding of general conceptual knowledge.
- **Prefrontal cortex** — discussed in the context of oscillatory control flow (CFC stimulation modulating cognitive functions), episodic memory interactions, and the spectral connectome.
- **Brainstem / subcortex** — mentioned as the source of conserved arousal and neuromodulatory states that gate learning bouts.

The paper is primarily theoretical and does not report new neural data; brain regions are invoked to contextualise the framework.

---

### Mechanistic insight

The paper does not meet the bar for full mechanistic insight as defined here. It proposes an algorithm (quasiattractor token sequences organised by nested oscillations) and provides extensive theoretical motivation, but it does not present new neural data linking the specific variables of the token/oscillation model to measured neural activity. The empirical evidence cited is from prior literature, not new experiments designed to test the token framework against alternatives.

At the **computational level**, the paper is strong: it articulates that the brain solves the problem of flexible, compositional, hierarchically organised behaviour through temporally ordered sequences of causally discrete computational states.

At the **algorithmic level**, it offers the token/quasiattractor formalism and the oscillatory communication model, but these remain proposals rather than tested algorithms.

At the **implementational level**, it points to cell assemblies, reentrant synaptic loops, E/I network dynamics, and short-term plasticity as candidate mechanisms, but does not provide experimental validation of the specific mapping.

---

### Limitations & open questions

- The "token" concept and quasiattractor framework are not formalised mathematically beyond a conceptual sketch; the conditions under which tokens emerge, stabilise, and transition are not derived.
- The claim that oscillatory hierarchies implement the reading and updating of long-term memory models is plausible but not directly tested; causal evidence (e.g., from optogenetic phase disruption targeted to specific cognitive operations) is lacking.
- The paper does not specify how tokens would be discriminated experimentally from other dynamical descriptions of neural state sequences.
- The critique of backpropagation's biological implausibility is standard but the alternatives proposed (equilibrium propagation, dendritic compartmentalisation, neuropeptide-based credit assignment) are listed without evaluating which is most consistent with the dynamical intelligence framework.
- The paper acknowledges but does not resolve the trade-off between biological detail and computational tractability in CN models.
- The year of publication is uncertain from the PDF text alone (references extend to early 2021 preprints); the venue is not explicitly stated in the converted text.

---

### Connections & keywords

**Key citations**:
- Buzsaki, G. — multiple works: log-dynamic brain (2014), The Brain from Inside Out (2019), sharp-wave ripples (2015), neural syntax (2010)
- van Gelder, T. — dynamical hypothesis in cognitive science (1998)
- Friston, K. — active inference, free energy, hierarchical generative models
- Krakauer et al. (2017) — neuroscience needs behavior
- Monaco et al. (2014) — attentive head-scanning and hippocampal place-field potentiation
- Watts & Strogatz (1998) — small-world networks
- Miłkowski (2013, 2018) — mechanistic computationalism
- Lillicrap et al. (2020) — backpropagation and the brain
- Sinz et al. (2019) — engineering less artificial intelligence

**Named models or frameworks**:
- Lashley-Hebb cell assembly
- Quasiattractor / chaotic itinerancy (Tsuda)
- Winnerless competition (Rabinovich & Varona)
- Cross-frequency coupling (CFC) / phase-amplitude coupling
- Predictive coding (Bastos et al. canonical microcircuits)
- Successor representation (mentioned implicitly via cognitive map literature)
- Equilibrium propagation (Scellier & Bengio)
- Network of networks (Perich & Rajan)
- BRAID (NSF Emerging Frontiers program)

**Brain regions**:
- Hippocampus
- Neocortex
- Entorhinal cortex
- Medial temporal lobe
- Prefrontal cortex
- Brainstem / subcortical arousal systems

**Keywords**:
- dynamical systems neuroscience
- neural oscillations
- cross-frequency coupling
- quasiattractor dynamics
- cell assembly
- temporal coding
- sparse connectivity
- small-world networks
- rich club organisation
- computational neuroscience / AI convergence
- agentic learning
- token-based neural computation
