---
source_file: durstewitz2020_psychiatric_network_dynamics.md
paper_id: durstewitz2020_psychiatric_network_dynamics
title: "Psychiatric Illnesses as Disorders of Network Dynamics"
authors:
  - "Daniel Durstewitz"
  - "Quentin J.M. Huys"
  - "Georgia Koppe"
year: 2020
journal: "Biological Psychiatry: Cognitive Neuroscience and Neuroimaging"
paper_type: review
contribution_type: theoretical
methods:
  - fmri
  - dynamic_causal_modelling
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - anterior_cingulate_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - striatum
frameworks:
  - attractor_networks
keywords:
  - dynamical_systems_theory
  - attractor_dynamics
  - bifurcation
  - metastability
  - limit_cycle
  - heteroclinic_channel
  - chaotic_itinerancy
  - recurrent_neural_network
  - computational_psychiatry
  - network_dynamics
  - psychiatric_nosology
  - working_memory_attractor
  - psychiatric
  - illnesses
  - disorders
  - network
  - dynamics
wiki_pages:
  - wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction
---

### One-line summary

Dynamical systems theory (DST) provides a unifying, hub-level framework for understanding mental illness, linking diverse biophysical changes and behavioural symptoms through common alterations in network-level dynamical phenomena such as attractor instability, bifurcations, limit cycles, and chaos.

---

### Background & motivation

Mental illnesses are temporally dynamic, heterogeneous phenomena that span multiple timescales and levels of organisation, yet most research has focused on cross-sectional, static snapshots rather than longitudinal trajectories. Existing computational approaches in psychiatry are largely linear and therefore incapable of capturing the rich phenomenology of real neural dynamics. The authors argue that DST represents a "hub" level of convergence at which diverse physiological aberrations can be understood through a common vocabulary, potentially transforming how psychiatric conditions are classified, predicted, and treated.

---

### Methods

This is a narrative review covering dynamical systems theory concepts and their proposed psychiatric relevance. The authors:

- Introduce core DST concepts (state space, flow fields, attractors, bifurcations, chaos) using a single formal running example: a two-unit recurrent neural network (RNN) simulated across varying parameter regimes.
- Map specific DST phenomena to specific symptom clusters across a range of psychiatric and neurological conditions (schizophrenia, depression, ADHD, OCD, PTSD, bipolar disorder, epilepsy, dementia, Parkinson's disease).
- Review current methods for inferring dynamical systems from empirical data (EEG, fMRI, ecological momentary assessment), including dynamic causal modelling, delay embeddings, and machine-learning-based RNN inference.
- Discuss treatment implications of conceptualising psychiatric conditions in dynamical terms.

---

### Key findings

- **Attractor instability and multistability**: Overly steep attractor basins map onto perseveration, dissociation, obsessions, and compulsions; overly flat basins or high noise map onto distractibility, associative hopping, and disorganised thought. Dopamine (via D1/D2 receptor actions) modulates basin width and depth in prefrontal circuits, providing a mechanistic link to schizophrenia working memory deficits and cognitive inflexibility.
- **Limit cycles and heteroclinic channels**: Stereotypical repeating thought or movement patterns (e.g., rumination, periodic symptom clusters) may arise from stable limit cycles; more flexible sequential cognition may be implemented via heteroclinic channels connecting saddle points.
- **Attractor ghosts and line attractors**: Semiattracting "ruins" slow trajectories and may underlie interval timing deficits in Parkinson's disease and ADHD; impaired line attractor configurations may account for deficits in parametric working memory.
- **Chaos**: Increased chaoticity is associated with disorganised thought in schizophrenia, mood instability in bipolar disorder, and high distractibility in ADHD; reduced variability (too little chaos) is associated with PTSD and impaired cognitive flexibility. Optimal computation occurs near the edge of chaos.
- **Bifurcations**: Abrupt qualitative changes at critical parameter values explain sudden clinical transitions (epileptic seizures, lucid moments in dementia, treatment resistance, phase transitions between depression and health including critical slowing-down signatures).
- **Treatment implications**: DST suggests that the same dynamical regime can be reached via multiple biophysical routes; pharmacological targets need not be the most compromised transmitter system but any that achieves the desired shift in dynamics. Deep-brain stimulation and ECT may be necessary when bifurcation points render pharmacological restoration impossible.

---

### Computational framework

The paper is organised around **dynamical systems theory** as its central framework. The core formalism treats the brain (and psychological variables) as a continuous- or discrete-time dynamical system defined by:

- **State space**: the space spanned by all system variables (membrane potentials, symptom strengths, mood, etc.)
- **Flow field**: differential (or recursive) equations specifying the direction and magnitude of change at every point in state space
- **Attractor objects**: stable fixed points, limit cycles, chaotic attractors, line attractors, and their basins of attraction
- **Bifurcation parameters**: parameters whose smooth variation causes qualitative changes in the system's dynamical landscape

Key assumptions: (1) generic DST phenomena are substrate-independent and therefore apply across biophysical, cognitive, and societal levels; (2) the same dynamical alteration (e.g., shallow attractor basins) can arise from many different biophysical causes; (3) recurrent neural networks (RNNs) are dynamically universal and can approximate any DS, making them suitable both as theoretical models and as inference tools.

---

### Prevailing model of the system under study

The paper positions itself against two dominant approaches: (1) cross-sectional, static biomarker-based psychiatry that neglects temporal dynamics; and (2) linear computational approaches (e.g., correlation, coherence, standard hidden Markov models) that cannot capture non-linear phenomena. The existing theoretical background acknowledged by the authors includes attractor network models of working memory (Durstewitz, Wang), computational psychiatry frameworks (Wang & Krystal, Breakspear), and symptom-network approaches (Borsboom). The prevailing implicit model of psychiatric illness is thus one of stable latent factors or static connectivity differences, which the review argues is fundamentally inadequate for capturing the dynamic, trajectory-dependent nature of mental illness.

---

### What this paper contributes

The review establishes DST as a principled, quantifiable, and clinically relevant framework that can unify phenomena across psychiatric nosology. Concretely:

- It provides a systematic mapping between specific DST phenomena and specific symptom profiles (Table 1), offering a taxonomy grounded in mechanistic principles rather than phenomenological description.
- It argues that dynamical properties—not just static biomarkers—should be the targets of diagnosis, prognosis, and intervention.
- It highlights that the same symptom can result from very different biophysical changes (convergence at the dynamical level), and that the same biophysical change can produce different symptoms depending on which brain area is affected (divergence at the symptom level).
- It identifies RNN-based machine-learning inference as the methodological frontier for bringing DST into clinical practice.

The key unresolved questions identified include: distinguishing empirically between limit-cycle, heteroclinic-channel, and metastable-hopping accounts of periodic symptoms; identifying which brain areas are most dynamically compromised in individual patients; and developing systematic empirical tests of DST mechanisms in psychiatric populations.

---

### Brain regions & systems

- **Prefrontal cortex (dorsolateral PFC)** — primary locus of attractor dynamics for working memory; dopamine modulates basin depth/width here; implicated in schizophrenia deficits and cognitive flexibility.
- **Ventral anterior cingulate cortex** — proposed emotional hub whose overly stable attractor states inhibit dorsolateral PFC activation in depression (Ramirez-Mahaluf & Compte model).
- **Orbitofrontal cortex** — mentioned as a site where hyperstable attractors may manifest as perseveration of suboptimal responses.
- **Auditory cortex** — hyperstable attractors here cited as potential mechanism for tinnitus.
- **Basal ganglia / dopaminergic system** — dopamine links to interval timing, cognitive flexibility, schizophrenia, and Parkinson's disease; basal ganglia mentioned in context of timing deficits.
- **Hippocampus** — attractor dynamics implicated in memory recollection and pattern completion.

The paper's primary level of analysis is network-level dynamics rather than specific anatomical circuits; many arguments are region-agnostic with brain areas invoked illustratively.

---

### Mechanistic insight

The paper does not meet the high bar for this section. It is a theoretical review that proposes DST mechanisms and cites supporting empirical evidence from the literature, but it does not itself present new neural data linking specific DST model variables to measured neural activity. The paper proposes algorithms (attractor dynamics, bifurcations, etc.) that could explain psychiatric phenomena, but the cited empirical support consists of secondary references rather than data specifically collected and analysed to adjudicate between the proposed mechanisms and alternatives.

At Marr's computational level the contribution is strong: DST clarifies what problem the brain is solving (stable representation, flexible switching, sequence generation) and why. At the algorithmic level, the RNN formalism provides candidate mechanisms. At the implementational level, isolated examples are given (dopamine modulating attractor basins, GABA/glutamate balance), but these are drawn from prior modelling studies rather than novel neural recordings.

---

### Limitations & open questions

- The DST framework is primarily conceptual in this review; systematic empirical validation of most proposed links (e.g., limit cycles vs. heteroclinic channels in periodic symptoms) is still lacking.
- Most DST inference methods require long, high-quality time series that are difficult to obtain clinically; current neuroimaging and EEG data impose strong temporal and spatial resolution constraints.
- Linear models dominate current clinical practice and cannot capture the non-linear phenomena described; transitioning to non-linear inference pipelines requires methodological and cultural change.
- The paper acknowledges that the same dynamical alteration can produce different symptoms depending on the brain region affected, but does not provide a principled account of the mapping between regions and symptom profiles.
- Distinguishing empirically between different dynamical accounts of the same symptom (e.g., metastable hopping vs. limit cycle for periodic episodes) remains an open challenge.
- The implications for personalised treatment are noted but underdeveloped; no clinical trial evidence for dynamically-targeted interventions is reviewed.

---

### Connections & keywords

**Key citations**:
- Durstewitz, Seamans & Sejnowski (2000) — neurocomputational working memory models
- Durstewitz & Seamans (2008) — dual-state theory of prefrontal dopamine
- Wang & Krystal (2014) — computational psychiatry
- Breakspear (2017) — dynamic models of large-scale brain activity
- Rabinovich et al. (2008) — transient cognitive dynamics and heteroclinic channels
- Koppe et al. (referenced) — RNN-based DS inference from neural data
- Ramirez-Mahaluf & Compte (2018) — serotonin and depression in PFC circuits
- Borsboom et al. (2011) — symptom network model of psychopathology
- Strogatz (2018) — Nonlinear Dynamics and Chaos (foundational text)

**Named models or frameworks**:
- Dynamical Systems Theory (DST)
- Recurrent Neural Networks (RNNs) as universal dynamical approximators
- Dual-state theory of prefrontal dopamine function
- Heteroclinic channel (HC) model of sequential cognition
- Dynamic Causal Modelling (DCM)
- Chaotic itinerancy

**Brain regions**:
- Dorsolateral prefrontal cortex
- Ventral anterior cingulate cortex
- Orbitofrontal cortex
- Hippocampus
- Basal ganglia / dopaminergic system
- Auditory cortex

**Keywords**:
- dynamical systems theory
- attractor dynamics
- bifurcation
- metastability
- limit cycle
- heteroclinic channel
- chaotic itinerancy
- recurrent neural network
- computational psychiatry
- network dynamics
- psychiatric nosology
- working memory attractor

### Related wiki pages
- [[wiki/topics/computational_models_of_schizophrenia_attractor_dynamics_and_nmda_hypofunction|Computational models of schizophrenia: attractor dynamics and NMDA hypofunction]]
