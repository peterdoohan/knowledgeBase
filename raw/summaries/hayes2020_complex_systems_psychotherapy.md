---
source_file: hayes2020_complex_systems_psychotherapy.md
paper_id: hayes2020_complex_systems_psychotherapy
title: "A complex systems approach to the study of change in psychotherapy"
authors:
  - "Adele M. Hayes"
  - "Leigh A. Andrews"
year: 2020
journal: "BMC Medicine"
paper_type: review
contribution_type: theoretical
methods:
  - computational_modeling
keywords:
  - complex_adaptive_systems
  - attractor_dynamics
  - psychotherapy_change_processes
  - network_destabilization_and_transition
  - critical_fluctuations
  - critical_slowing
  - early_warning_signals
  - nonlinear_change
  - ecological_momentary_assessment
  - network_psychopathology
  - inhibitory_learning
  - process_based_psychotherapy
  - complex
  - systems
  - approach
  - study
  - change
  - psychotherapy
---

### One-line summary

Hayes and Andrews present the Network Destabilization and Transition (NDT) model, a conceptual framework that imports principles from dynamical systems theory, synergetics, and network science to explain and guide the study of therapeutic change in psychotherapy.

---

### Background & motivation

Traditional psychotherapy research has relied on RCT designs that measure symptom change at pre- and post-treatment snapshots, assuming gradual linear change. This approach fails to capture the multicomponent patterns of psychopathology and the nonlinear, discontinuous dynamics through which therapeutic change actually unfolds. While complexity science offers relevant theories and methods — including attractor dynamics, self-organization, and network analysis — uptake into psychotherapy research has been slow due to jargon barriers and the perceived inaccessibility of computational methods. This paper aims to translate core principles from complexity science into an integrative, accessible framework for psychotherapy researchers and clinicians.

---

### Methods

This is a theoretical review and framework paper. The synthesis approach includes:

- Narrative review of three subdisciplines of complexity science: dynamical systems theory, synergetics, and network science.
- Integration of principles of change from modern learning theory (inhibitory learning, competitive retrieval) with complex systems concepts.
- Presentation of the NDT model as an organizing framework, illustrated with attractor landscape diagrams depicting pathological and healthy network states.
- Review of empirical examples from the psychotherapy literature that demonstrate: nonlinear change trajectories, early warning signals (critical fluctuations and critical slowing), and network-level change.
- Description of data collection considerations (timescale, density, level of analysis) and analytic tools available for complex systems research in psychotherapy.

---

### Key findings

- Psychopathology can be conceptualised as an attractor state with strongly interconnected cognitive, emotional, behavioural, and physiological elements; therapeutic change involves destabilising this attractor and strengthening a new, healthier one.
- Three types of therapeutic change are distinguished: (1) within-attractor modifications (incremental adjustments without state transition), (2) switching to an alternative attractor without changing the pathological one, and (3) destabilising the pathological attractor and developing a qualitatively new pattern.
- Critical fluctuations (rising variability) and critical slowing (slower return to baseline after perturbation) are proposed as early warning signals of therapeutic transition, consistent with their function across other natural systems.
- Existing empirical studies (though limited in number) show that increased variability in symptoms and therapy process variables predicts sudden gains and better treatment outcomes across depression, personality disorders, OCD, anxiety, and trauma samples.
- Attractor competition — where newly learned patterns inhibit or compete with the old pathological attractor — is proposed as a key mechanism of relapse prevention, connecting complex systems principles to inhibitory learning and competitive retrieval theories.
- Technological advances (ecological momentary assessment, wearables, text mining) now make high-density longitudinal data collection feasible in psychotherapy research.
- Network analysis tools can quantify structure, density, connectivity, and activation thresholds of psychopathological and healthy patterns, enabling personalised treatment formulation.

---

### Computational framework

The paper draws on three overlapping frameworks from complexity science:

1. **Dynamical systems theory**: psychopathology and mental health are modelled as attractor states in a phase space. Key variables include attractor strength (well-depth), perturbation forces (deterministic and stochastic), control parameters (conditions that govern transitions between states), and early warning signals (variance, autocorrelation). The framework assumes that systems self-organise into preferred states and that transitions are often nonlinear and discontinuous.

2. **Synergetics (Haken)**: a thermodynamic-inspired framework for self-organisation in which order parameters (slow variables) capture system-level patterns and slave fast variables. In the psychotherapy context, an order parameter might represent a dominant mode of psychopathological functioning (e.g., a depressive pattern) that constrains lower-order cognitive, emotional, and physiological processes. Change involves disrupting the dominant order parameter and allowing a new one to emerge.

3. **Network science**: psychopathology is represented as a network of symptom/component nodes with weighted edges reflecting causal or co-activation relationships. Key quantities include network density, connectivity, and centrality. The paper integrates temporal network approaches to capture change over the course of therapy.

The NDT model does not present a formal mathematical model but specifies the conceptual structure and points to existing tools (nonlinear differential equations, recurrence quantification analysis, GridWare, the Synergetic Navigation System, dynamic complexity measures, and early warning sign toolboxes in R) for operationalising its constructs.

---

### Prevailing model of the system under study

The paper's introduction identifies two prevailing — and limiting — assumptions in psychotherapy research. First, the dominant methodology (the RCT with pre/post assessment) implicitly treats therapeutic change as gradual and linear, reducing multicomponent functioning to single-symptom outcomes measured at discrete snapshots. Second, the dominant theoretical framing has treated psychopathology as a collection of separable components (cognitions, emotions, behaviours) rather than as an integrated, self-organising system. The authors note that complex systems approaches were introduced to psychotherapy approximately 30 years before this paper, but the mainstream has been slow to adopt them due to methodological barriers and the incompatibility with RCT infrastructure.

---

### What this paper contributes

The NDT model provides a common organisational structure that: (a) maps disparate empirical findings about nonlinear change, early warning signals, and network dynamics onto a unified framework; (b) distinguishes qualitatively different types of therapeutic change (within-attractor modification, attractor switching, attractor destabilisation and replacement) with distinct clinical and research implications; (c) connects complexity science with modern learning theories (inhibitory learning, competitive retrieval), bridging frameworks that have previously not been related; and (d) proposes a research agenda with concrete design and analytic recommendations for leveraging high-density longitudinal data. The review establishes that nonlinear, discontinuous change trajectories and early warning signals have been observed in psychotherapy samples, but also that the empirical base is still small and that firm conclusions about early warning signals cannot yet be drawn.

---

### Brain regions & systems

Not applicable. The paper operates entirely at the psychological/behavioural and computational modelling levels. It discusses patterns of cognition, emotion, behaviour, and physiological responding as interacting nodes in a network, but does not specify or discuss anatomical substrates. The level of analysis is the person-level dynamic system in the context of psychotherapy.

---

### Mechanistic insight

The paper does not meet the bar for mechanistic insight as defined here. It proposes a computational-level framework (what the system is doing: transitioning between attractor states representing psychopathology and health) and an algorithmic-level description (what the process looks like: critical fluctuations, critical slowing, network densification/decoupling), but it does not present neural data linking these constructs to measured neural activity. The paper is explicitly a theoretical and framework paper, and its empirical examples are drawn from behavioural/self-report time-series in psychotherapy contexts, not neuroscience recordings. The framework could in principle constrain models of how neural systems implement attractor dynamics in affective and cognitive disorders (e.g., how prefrontal-limbic circuitry encodes maladaptive versus adaptive attractor states), but this connection is not made in the paper.

---

### Limitations & open questions

- Too few empirical studies on early warning signals in psychotherapy to draw firm conclusions; most evidence comes from case studies or small samples.
- It is unclear whether the signatures of early warning signals differ when predicting disorder onset, therapeutic improvement, or relapse — clinically important distinctions.
- The NDT model depicts two discrete attractors (pathological vs. healthy) for illustrative purposes, but acknowledges this may be an oversimplification; multistability and the question of whether pathological and healthy states are best modelled as separate networks or one larger network with excitatory/inhibitory pathways remain open.
- Distinguishing variability that constitutes meaningful early warning signals from noise, personality-based lability (e.g., neuroticism), or random fluctuation is methodologically unresolved.
- Whether early warning signal principles apply to all three types of therapeutic change described in the NDT model (or only to the destabilisation type) is unknown.
- The old-new attractor competition principle — central to the model's account of relapse prevention — has very little direct empirical testing in psychotherapy; existing studies use statistical interactions as rough approximations.
- Many analytic tools (network analysis, nonlinear differential equations) assume or require stationarity or large numbers of data points that remain challenging to obtain in standard clinical contexts.

---

### Connections & keywords

**Key citations**:
- Scheffer et al. (2009, Nature) — early warning signals for critical transitions
- Scheffer et al. (2012, Science) — anticipating critical transitions
- Tschacher & Haken (2019) — The Process of Psychotherapy (book)
- Kelso (1995) — Dynamic Patterns (book)
- Borsboom & Cramer (2013) — network analysis of psychopathology
- Hayes et al. (2015, Clin Psychol Rev) — NDT model original presentation for depression
- Haken & Tschacher (2017) — computational model of how to modify psychopathological states
- Craske et al. (2014) — inhibitory learning approach to exposure therapy
- Brewin (2006) — retrieval competition account of CBT
- Burger et al. — computational model of panic disorder (cited in text as [112])

**Named models or frameworks**:
- Network Destabilization and Transition (NDT) model
- Synergetics (Haken)
- Dynamical systems theory
- Network theory / network analysis of psychopathology
- Synergetic Navigation System (SNS)
- Group Iterative Multiple Model Estimation (GIMME)
- Recurrence quantification analysis
- GridWare
- Dynamic complexity (Schiepek & Strunk)
- Inhibitory learning theory (Craske)
- Competitive retrieval theory (Brewin)

**Brain regions**: Not applicable (see Brain regions section).

**Keywords**: complex adaptive systems, attractor dynamics, psychotherapy change processes, network destabilization and transition, critical fluctuations, critical slowing, early warning signals, nonlinear change, ecological momentary assessment, network psychopathology, inhibitory learning, process-based psychotherapy
