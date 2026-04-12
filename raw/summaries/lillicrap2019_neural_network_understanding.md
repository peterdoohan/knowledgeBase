---
source_file: lillicrap2019_neural_network_understanding.md
paper_id: lillicrap2019_neural_network_understanding
title: "What does it mean to understand a neural network?"
authors:
  - "Timothy P. Lillicrap"
  - "Konrad P. Kording"
year: 2019
journal: "arXiv preprint (July 2019)"
paper_type: review
contribution_type: theoretical
species:
  - human
keywords:
  - neural_network_interpretability
  - compressibility
  - knowledge_distillation
  - network_compression
  - learning_rules
  - synaptic_plasticity
  - developmental_neuroscience
  - algorithmic_complexity
  - mid_level_models
  - nature_vs_nurture_in_neural_computation
  - post_hoc_analysis_limitations
  - neuroscience_methodology
  - what
  - does
  - mean
  - understand
  - neural
  - network
---

### One-line summary

Neural networks trained on complex tasks are likely incompressible and therefore uninterpretable at the level of weights and representations, suggesting that neuroscience should redirect effort toward understanding learning rules, developmental principles, and architecture rather than trained circuit properties.

---

### Background & motivation

A deep learning system can be fully specified by a few pages of code, yet after training its millions of weights resist compact, human-readable description. The authors use this familiar tension from machine learning as a lens on neuroscience: if artificial networks — which we have complete access to — cannot be meaningfully understood post-training, the same limitation likely applies to biological neural circuits. The paper addresses the gap between the field's implicit hope of finding a compact mid-level description of brain computation (analogous to thermodynamics for gases) and the theoretical reasons why such a description may not exist for systems trained on a complex, incompressible world.

---

### Methods

This is a theoretical/perspective paper; no experiments are conducted. The argument proceeds by:

- Introducing the concept of **compressibility**: the degree to which a system's behaviour can be expressed in fewer parameters than the system itself contains.
- Using tic-tac-toe (compressible: three rules) vs. Go (incompressible: no known compact policy description) as illustrative anchors.
- Reviewing empirical evidence from network distillation and compression literature to establish that ImageNet-trained networks cannot be reduced below ~100k free parameters without performance loss, and that even MNIST classifiers resist human-readable compression.
- Drawing an analogy between artificial and biological neural networks, grounded in the observation that the brain acquires knowledge from a complex, incompressible world via plasticity.
- Discussing the physics analogy (statistical mechanics as a successful mid-level description) and arguing it breaks down for brains due to the non-exchangeability and long memory of neurons.

---

### Key findings

- A system achieving human-level performance across a broad range of tasks must encode information from a complex, incompressible world; this information cannot be compressed into a compact, human-readable form.
- Networks trained on ImageNet cannot readily be compressed to fewer than ~100k free parameters (citing Han et al. 2015; Li et al. 2018; Wu et al. 2016), and even that compression is not humanly interpretable.
- Humans store roughly 1.5 MB of information during language acquisition alone (Mollica & Piantadosi 2019), and know detailed information across ~30,000 object categories — underscoring the incompressibility of the knowledge a brain encodes.
- Existing post-hoc interpretability techniques (sensitivity analysis, adversarial inputs, unit visualisation, ablation) do not provide practitioners with enough understanding to improve model performance — suggesting they fall short of genuine understanding.
- The physics analogy (gas → temperature/pressure) fails for brains: gas atoms are exchangeable with short memory; neurons are individually unique with lifelong memory.
- The more tractable target for understanding is the **generative process**: objectives, learning rules, architectures, and developmental principles — the "nature" component — rather than the trained weights — the "nurture" component.

---

### Computational framework

The paper does not formalise a single computational model. Its central concept is **algorithmic compressibility** (closely related to Kolmogorov complexity): the minimum description length needed to specify a system's input-output behaviour. The paper uses this informally rather than mathematically.

The key claim is that systems performing well on complex, high-dimensional tasks must have description lengths that scale with the complexity of the training environment, not with any compact set of rules. This places an in-principle upper bound on interpretability: if the world is incompressible, so is the model trained on it.

The framework implicitly invokes Marr's levels by distinguishing what a system learns to do (computational level), how it encodes that knowledge (algorithmic/representational level — argued to be opaque), and how learning rules and architecture set up the computation (implementational/developmental level — argued to be tractable).

---

### Prevailing model of the system under study

The paper's target is not a specific brain region but the broader neuroscience enterprise. The prevailing model it pushes against is the assumption — widespread in systems neuroscience — that meaningful, communicable mid-level descriptions of brain computation exist and can be discovered by studying neural representations, connectivity, and dynamics post-hoc. This assumption is grounded in analogies to physics (where thermodynamic variables compactly describe gas behaviour) and in the success of cognitive models (e.g. drift-diffusion for simple decisions, the vestibuloocular reflex model). The paper accepts that such compact descriptions exist for simple, domain-specific behaviours but challenges their generalisability to the complex, open-ended tasks that characterise human cognition.

---

### What this paper contributes

The paper argues that the analogy to physics is misleading for complex cognitive systems, because it ignores the incompressibility of the information stored from a complex environment. This is not merely a practical limitation of current methods but a principled one: no compact mid-level description can both work on complex tasks and be communicable, because the knowledge required to perform those tasks cannot itself be compactly communicated.

Concretely, the paper reframes the question neuroscience should ask: not "how does the brain work?" but "how does it learn to work?" — i.e., what are the objectives, plasticity rules, and developmental/architectural principles that allow uncompressible environmental information to be converted into useful computation. This redirects effort toward properties of the generative process (anatomy, plasticity rules, cell types, genetic specification) rather than the resulting representations or connection strengths.

---

### Brain regions & systems

Not applicable in the sense of a primary anatomical focus. The paper operates at the level of the brain as a whole learning system. The only region mentioned in passing is the cerebellum (vestibuloocular reflex adaptation), cited as an example of a domain simple enough to admit a compact model — used as a contrast case to illustrate where mid-level descriptions do and do not work.

---

### Mechanistic insight

The paper does not meet the bar for this section. It is a theoretical perspective piece: it neither formalises an algorithm for a specific neural computation nor provides neural data linking any model variable to measured neural activity. Its contribution is a conceptual argument about the limits of interpretability, not an account of any particular neural mechanism.

---

### Limitations & open questions

- The argument is primarily informal; no formal proof is offered that human-level performance requires incompressible representations.
- The compression results cited (e.g., ~100k parameter floor for ImageNet) are empirical snapshots; future advances in distillation or representation learning could raise or lower this bound.
- The claim that the brain's generative process is tractable (compressible) is asserted rather than demonstrated — the effective information in non-coding DNA and gene regulatory networks is explicitly acknowledged as unknown.
- The paper does not address whether strong modularity, approximate linearity, or noise in biological networks could make them easier to understand than artificial networks — it raises this as an open question.
- The possibility of super-human AI systems that could understand trained networks (even if humans cannot) is noted but not developed.
- The paper does not engage with whether the incompressibility argument applies equally to all domains of neuroscience (e.g., motor control, sensory coding) or primarily to high-level cognition.

---

### Connections & keywords

**Key citations:**
- Krizhevsky, Sutskever & Hinton 2012 (AlexNet / ImageNet)
- Silver et al. 2016, 2017 (AlphaGo / AlphaGo Zero)
- Hinton, Vinyals & Dean 2015 (knowledge distillation)
- Han, Mao & Dally 2015 (deep compression)
- Li et al. 2018 (intrinsic dimensionality of objective landscapes)
- Mollica & Piantadosi 2019 (human language information content)
- Jonas & Kording 2017 (could a neuroscientist understand a microprocessor?)
- Ramaswamy 2019 (algorithmic barrier to neural circuit understanding)
- Robinson 1976 (vestibuloocular reflex — cited as tractable simple case)
- Frosst & Hinton 2017 (distilling a neural network into a soft decision tree)

**Named models or frameworks:**
- AlexNet, AlphaGo / AlphaGo Zero, GPT-2 (as exemplars of incompressible trained systems)
- ImageNet benchmark
- Kolmogorov/algorithmic compressibility (informal)
- Knowledge distillation
- Marr's levels (implicit)

**Brain regions:**
- Cerebellum (mentioned only as contrast case for vestibuloocular reflex)

**Keywords:**
- neural network interpretability
- compressibility
- knowledge distillation
- network compression
- learning rules
- synaptic plasticity
- developmental neuroscience
- algorithmic complexity
- mid-level models
- nature vs nurture in neural computation
- post-hoc analysis limitations
- neuroscience methodology
