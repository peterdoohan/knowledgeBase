---
source_file: fusi2016_mixed_selectivity_cognition.md
paper_id: fusi2016_mixed_selectivity_cognition
title: "Why neurons mix: high dimensionality for higher cognition"
authors:
  - "Stefano Fusi"
  - "Earl K Miller"
  - "Mattia Rigotti"
year: 2016
journal: "Current Opinion in Neurobiology"
paper_type: review
contribution_type: theoretical
species:
  - human
methods:
  - fmri
  - computational_modeling
brain_regions:
  - hippocampus
  - prefrontal_cortex
  - amygdala
frameworks:
  - mixed_selectivity
keywords:
  - mixed_selectivity
  - neural_dimensionality
  - population_coding
  - linear_readout
  - nonlinear_mixed_selectivity
  - cognitive_flexibility
  - working_memory
  - dimensionality_expansion
  - dimensionality_reduction
  - prefrontal_cortex
  - neural_geometry
  - vc_dimension
  - why
  - neurons
  - mix
  - high
  - dimensionality
  - higher
  - cognition
---

### One-line summary

Mixed selectivity in cortical neurons — where single cells respond to nonlinear combinations of task-relevant variables — creates high-dimensional population representations that enable a simple linear readout to implement an exponentially large number of distinct cognitive responses.

---

### Background & motivation

The traditional view of brain function holds that individual neurons and brain areas are highly specialised, each performing a single function. However, empirical observations, especially in higher-order cortex, conflict with this: large fractions of prefrontal and parietal neurons are engaged by cognitive tasks and appear to encode diverse combinations of variables across contexts. This review addresses why such "mixed selectivity" exists. The core question is whether apparent neural complexity is noise or is computationally meaningful — and if so, why.

---

### Methods

This is a narrative review synthesising theoretical arguments and empirical evidence from the computational neuroscience and systems neuroscience literature.

- Scope covers single-unit recordings in primates and rodents (PFC, PPC, hippocampus, amygdala, IT cortex), fMRI, and computational modelling studies.
- Theoretical framework drawn from machine learning (support vector machines, deep neural networks, random projections, linear readouts).
- Dimensionality estimation methods reviewed: PCA-based approaches (Machens et al. 2010), and cross-validation of linearly separable "colorings" of firing rate vectors (Rigotti et al. 2013).
- No new data or models are presented; synthesis is conceptual and theoretical.

---

### Key findings

- Neural representations based on nonlinear mixed selectivity are high-dimensional; those based on pure (specialised) selectivity are low-dimensional regardless of how many variables they encode.
- The number of distinct binary classifications implementable by a linear readout grows exponentially with the dimensionality of the input representation — this is the central computational advantage of mixed selectivity.
- Diversity among mixed selectivity neurons (heterogeneity in which combinations they respond to) is a necessary second ingredient for high dimensionality.
- Noise can inflate apparent dimensionality but not usefully: artifactual dimensions from noise do not generalise across trials; cross-validated dimensionality measurement corrects for this.
- PFC dimensionality in primates performing a working memory task reaches the maximum accommodated by the stimulus-response space (Rigotti et al. 2013).
- Dimensionality collapses on error trials in both rodents and primates, and this collapse is specifically due to loss of nonlinear mixed selectivity, not loss of information about individual stimuli.
- Pharmacological intervention (amphetamine) modulates PFC dimensionality in a dose-dependent manner.
- Random synaptic projections onto nonlinear neurons are sufficient to generate high-dimensional representations — consistent with the random glomerulus-to-Kenyon cell connectivity in the Drosophila olfactory system.
- High dimensionality is not always desirable: dimensionality reduction improves generalisation in classification tasks and is the computational strategy of the visual hierarchy (IT cortex, deep nets).
- The brain therefore requires a balance: dimensionality reduction for invariant perception, dimensionality expansion for flexible cognitive output.

---

### Computational framework

The paper uses a **linear readout / VC-dimension framework** drawn from statistical learning theory and machine learning.

- **Core formalism**: Population activity vectors are treated as points in an N-dimensional firing-rate space (N = number of neurons). A linear readout is a weighted sum and threshold, implementable by a single downstream neuron. The key quantity is the number of distinct binary classifications ("colorings") of P stimulus conditions that a linear readout can implement.
- **Key result**: The number of implementable classifications grows exponentially with the dimensionality of the representation. Dimensionality is defined as the rank of the condition-by-neuron firing-rate matrix (corrected for noise).
- **Assumptions**: (1) Downstream readout is no more powerful than a linear classifier — a conservative but biologically grounded assumption. (2) Repeated presentations of the same condition allow averaging out trial-to-trial noise. (3) The relevant unit of analysis is the population, not individual neurons.
- The framework connects directly to Support Vector Machines (margin maximisation) and echo-state / liquid-state machine models of recurrent networks.

---

### Prevailing model of the system under study

The paper's introduction frames the dominant prior view as a **modular, specialised cortex**: individual neurons and brain areas are each dedicated to specific computations, analogous to components in a machine. In this view, complex behaviour arises from combining outputs of many specialised modules. The observations that large fractions of PFC neurons are recruited by arbitrary tasks, and that individual neurons change their tuning across contexts, were known but typically treated as problematic or uninformative. The paper explicitly states that this view implies either a severe capacity limit (each new task monopolises dedicated cortical real estate) or that neurons are multifunctional — and it argues for the latter interpretation as computationally principled, not merely a curiosity.

---

### What this paper contributes

The review establishes a formal computational account of why mixed selectivity is not noise or inefficiency but a core design principle: it is the mechanism by which cortex achieves high-dimensional population representations, and high dimensionality is what allows a simple downstream neuron to implement arbitrary complex conjunctive responses. This reframes mixed selectivity from an empirical puzzle into a predicted consequence of efficient population coding for flexible cognition. The paper also articulates a testable prediction: brain areas causally linked to complex behaviour should exhibit higher dimensionality than those not so linked, and tasks with more conditions should produce correspondingly higher-dimensional representations. The connection between dimensionality collapse and behavioural errors provides the primary empirical grounding for these claims.

---

### Brain regions & systems

- **Prefrontal cortex (PFC)** — primary focus; proposed as the locus of high-dimensional mixed selectivity representations supporting complex working memory and cognitive flexibility.
- **Posterior parietal cortex (PPC)** — supporting evidence for heterogeneous, category-free neural responses during multisensory decisions.
- **Hippocampus** — noted as a site of mixed selectivity to contextual and episodic features; hierarchical organisation of population responses described.
- **Amygdala** — noted for mixed selectivity to visual stimuli, temporal context, and reinforcement signals.
- **Inferotemporal (IT) cortex** — discussed as an example of dimensionality reduction (invariant object representations) at the end of the ventral visual hierarchy.
- **Perirhinal cortex (PRH)** — compared to IT; information shown to be more linearly accessible (higher-dimensional) in PRH than IT for target detection.
- **Lateral intraparietal area (LIP)** — cited for multiplexed decision signals during decision-making.
- **Drosophila mushroom body (Kenyon cells)** — cited as a biological instantiation of random projections for dimensionality expansion in olfaction.

---

### Mechanistic insight

The paper meets the first criterion (it formalises an algorithm: nonlinear mixed selectivity as a mechanism for dimensionality expansion enabling linear readout flexibility). It partially meets the second: it reviews neural recording data in PFC that correlate dimensionality with behaviour. However, the primary evidence is correlational (dimensionality collapses on error trials; Rigotti et al. 2013), not causal.

Mapping onto Marr's levels:

- **Computational**: The brain must implement a large number of context-dependent stimulus-response mappings using a fixed population of neurons. The problem is to make many such mappings simultaneously accessible to downstream readout without requiring dedicated circuitry for each.
- **Algorithmic**: Nonlinear mixed selectivity neurons create high-dimensional population representations. A linear readout on this high-dimensional basis can implement an exponentially large number of distinct response functions without architectural changes. Diversity among mixed selectivity neurons ensures broad coverage of the representational space.
- **Implementational**: The paper notes that random synaptic weights onto nonlinear units are sufficient to generate mixed selectivity (consistent with Drosophila mushroom body anatomy). For primate PFC, no specific cell types or connectivity motifs are identified; the implementational level is left largely unaddressed. Amphetamine effects on dimensionality hint at neuromodulatory control but are not mechanistically unpacked.

Because the neural data are correlational (error-trial dimensionality collapse) rather than causally linking the specific algorithm to specific neural mechanisms, full mechanistic closure is not achieved.

---

### Limitations & open questions

- The theoretical framework assumes a linear readout, which is convenient but may underestimate the computational power available to real downstream circuits; the authors acknowledge this is a conservative bound.
- Dimensionality measures depend on the number and choice of task conditions, making cross-study comparisons difficult without careful control of task complexity.
- The causal role of mixed selectivity is inferred from correlational data (error trials); perturbation experiments selectively targeting mixed selectivity neurons are not reviewed and may be technically difficult.
- It is unclear how high-dimensional representations are established developmentally or through learning — neither Hebbian mechanisms nor backpropagation-style training are straightforwardly biologically plausible for generating the required nonlinear mixed tuning.
- The relationship between mixed selectivity and attentional or task-rule signals that modulate PFC activity is not fully resolved.
- The paper notes a tension between dimensionality expansion (needed for flexibility) and dimensionality reduction (needed for generalisation/invariance) but does not specify how the brain dynamically balances these — this is flagged as a key open question.
- The review focuses on PFC; whether the same framework applies equally to parietal, temporal, or subcortical structures remains underexplored.

---

### Connections & keywords

**Key citations**:
- Rigotti et al. 2013 (Nature) — primary empirical grounding; PFC dimensionality and error correlates
- Mante et al. 2013 (Nature) — context-dependent computation in PFC via recurrent dynamics
- Yamins et al. 2014 (PNAS) — deep nets predict IT cortex responses
- Machens et al. 2010 — PCA-based dimensionality estimation
- Gao & Ganguli 2015 — formalisation of dimensionality bounds
- Caron et al. 2013 — random projections in Drosophila mushroom body
- Barak et al. 2013 — sparseness and generalisation-discrimination trade-off in mixed selectivity neurons
- Lapish et al. 2015 — amphetamine effects on PFC dimensionality
- LeCun, Bengio & Hinton 2015 — deep learning review

**Named models or frameworks**:
- Linear readout / VC-dimension framework
- Echo-state machines / liquid-state machines (Jaeger & Haas 2004; Maass et al. 2002)
- Support Vector Machines (Vapnik; Cortes & Vapnik 1995)
- Deep artificial neural networks (LeCun et al. 2015)
- PCA-based dimensionality estimation (Machens et al. 2010)
- Cross-validated linear separability dimensionality measure (Rigotti et al. 2013)

**Brain regions**:
- Prefrontal cortex (PFC)
- Posterior parietal cortex (PPC)
- Hippocampus
- Amygdala
- Inferotemporal cortex (IT)
- Perirhinal cortex (PRH)
- Lateral intraparietal area (LIP)
- Drosophila mushroom body

**Keywords**:
- mixed selectivity
- neural dimensionality
- population coding
- linear readout
- nonlinear mixed selectivity
- cognitive flexibility
- working memory
- dimensionality expansion
- dimensionality reduction
- prefrontal cortex
- neural geometry
- VC dimension
