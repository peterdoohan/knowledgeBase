---
source_file: niv2019_representation_learning_task_states.md
title: Learning task-state representations
authors: Yael Niv
year: 2019
journal: Nature Neuroscience
paper_type: review
contribution_type: theoretical
---

### One-line summary

This Perspective argues that the brain solves reinforcement learning in complex environments by constructing low-dimensional task-state representations through two mechanisms — selective attention to relevant dimensions and latent-cause inference for hidden contextual states — with the orbitofrontal cortex serving as the neural locus of these abstract task-state representations.

---

### Background & motivation

Reinforcement learning (RL) algorithms require a pre-specified state space, but living agents must learn their own task representations from experience. This "representation learning" problem — deciding what aspects of the environment are causally relevant and should be encoded into states — is computationally formidable given the high dimensionality of sensory input and the absence of direct feedback for representations. The field had largely sidestepped this problem by hand-crafting state representations in computational models, leaving open how brains achieve rapid, efficient, sample-efficient representation learning across diverse tasks. This Perspective synthesises a decade of research from the Niv lab to propose a unified account of the algorithms and neural substrates involved.

---

### Methods

This is a Perspective/review article synthesising empirical and computational findings from the author's own research programme. Key studies reviewed include:

- **Dimensions Task** (human fMRI + attention-weighted RL modelling): participants learned which of several stimulus dimensions (e.g., shape, colour, texture; or face, tool, scene) was reward-relevant; model comparison tested attention-weighted RL against uniform-attention RL and Bayesian ideal observer accounts.
- **Latent-cause inference framework** (Bayesian clustering model applied to fear conditioning and perception): a non-parametric Bayesian model in which experiences are assigned probabilistically to latent causes (clusters = states); validated against rat fear conditioning (standard vs gradual extinction), human perceptual estimation, and human memory experiments.
- **Gradual extinction study** (rat behaviour): shocks tapered gradually across extinction trials to test whether keeping acquisition and extinction experiences similar prevents generation of a new latent-cause state.
- **Partially observable state task** (human fMRI + MVPA decoding): participants performed an age-judgement task whose correct execution required representing 16 hidden task states; multivariate pattern classification was applied to decode task-state identity from OFC and other regions.
- Literature synthesis covers attention networks, hippocampal lesion data, OFC electrophysiology and lesion studies in rodents and humans.

---

### Key findings

- Participants in the Dimensions Task learned via attention-weighted RL rather than as Bayesian ideal observers or whole-stimulus RL; attention weights shaped both valuation and prediction-error-driven learning, and BOLD signals in value-sensitive (dlPFC) and prediction-error-sensitive (ventral striatum) areas correlated more strongly with model quantities from the attention-weighted model than from a uniform-attention model.
- Latent-cause inference (Bayesian clustering based on similarity) provides a normative account of why extinction of conditioned fear is typically ineffective: acquisition and extinction trials are inferred to have separate latent causes, preserving the original fear memory.
- Gradual extinction — making the shock-to-no-shock transition incremental to keep extinction trials similar to acquisition trials — prevented reinstatement and spontaneous recovery of fear in rats, consistent with clustering all trials into one state.
- In a human circles-estimation task, participants spontaneously grouped trials into separate states only when the underlying distributions were sufficiently dissimilar; otherwise they averaged across colors, consistent with Bayesian latent-cause inference obeying Occam's razor.
- In the partially observable state fMRI task, multivariate classifiers could decode all unobservable task-state components from the OFC but not from other regions; OFC decoding fidelity correlated with lower error rates, and task-irrelevant information (from two trials back) was not decodable in OFC but was decodable in hippocampus.
- The hippocampus is implicated in novelty detection and state creation: hippocampal lesions abolish context-sensitivity of extinction and latent inhibition; immature hippocampus leads to over-generalisation consistent with a coarser state representation.
- Sequential replay of task states in the hippocampus (at rest) was found to improve subsequent OFC state representations (Schuck & Niv, 2019).

---

### Computational framework

The paper uses **reinforcement learning (RL)** as its primary framework, specifically focusing on the problem of state-space construction that RL presupposes but does not itself solve.

Two interacting computational mechanisms are proposed:

1. **Attention-weighted RL**: Stimulus dimensions are weighted by attention both during value computation (value = sum of feature values weighted by attention) and during learning (prediction errors update feature values weighted by attention). This implements dimensionality reduction — irrelevant dimensions receive near-zero weight, collapsing over them. Key variables: attention weights (phi), prediction error (delta = outcome - expected value), per-feature value estimates (v), learning rate (eta).

2. **Latent-cause inference (Bayesian non-parametric clustering)**: Incoming experiences are probabilistically assigned to latent causes (clusters) based on similarity to prior experiences. A Chinese Restaurant Process prior encourages parsimony (Occam's razor), creating new clusters only when current experience is sufficiently dissimilar to existing ones. Each cluster functions as a task state on which RL operates. This accounts for context-sensitivity of learning, extinction failure, and the structure of memory.

The two mechanisms interact: attention shapes perceptual similarity (by stretching attended dimensions), which in turn governs cluster assignment.

---

### Prevailing model of the system under study

Before this paper's contribution, the dominant frameworks for decision-making in the brain treated RL as operating on a fixed, externally specified state space. Model-free RL in the basal ganglia (dopaminergic prediction errors) and model-based RL in prefrontal-hippocampal circuits were well-characterised at the algorithmic and implementational levels. The OFC was most commonly understood as representing **expected reward outcomes** or economic value — i.e., its primary function was encoding what reward to expect, not encoding which state of the world the agent is currently in. Selective attention was generally understood as a neural processing bottleneck (a constraint), rather than as an adaptive computational mechanism in the service of learning efficiency. The problem of how the brain constructs the state representations that RL requires was largely unaddressed in computational neuroscience.

---

### What this paper contributes

The paper reframes selective attention as an adaptive solution to the curse of dimensionality in RL, rather than a capacity limitation. It argues that attention mechanisms construct the low-dimensional task-state representations on which RL operates, enabling rapid generalisation by collapsing over irrelevant dimensions.

It introduces latent-cause inference as the computational principle by which the brain decides when to treat two experiences as belonging to the same state versus different states — providing a normative, Bayesian account of phenomena previously treated as separate (extinction failure, renewal, reinstatement, memory reconsolidation, latent inhibition, context-sensitivity of generalisation).

Crucially, it reinterprets the OFC not as a reward-value area but as a "cognitive map of task space" — a region that represents abstract task-state identity (a pointer to the current state), deploying this representation for learning and decision-making in downstream structures (striatum, dopamine system). This challenges the dominant expected-value account of OFC. Before this synthesis, the OFC's role in state representation was proposed in individual papers (Wilson et al. 2014; Schuck et al. 2016) but had not been integrated with the attention and clustering accounts into a unified framework.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)** — proposed primary locus of abstract task-state representations; receives convergent sensory, limbic and higher-order inputs; represents the identity of the current (partially observable) task state, including unobservable components; fidelity of OFC representation correlates with behavioural accuracy; contrasted with the dominant view that OFC encodes expected reward value.
- **Ventral striatum** — locus of prediction-error signals (model-free RL); receives task-state representations from OFC to perform valuation and updating; BOLD prediction-error signals track attention-weighted model.
- **Dorsal basal ganglia (dorsal striatum)** — implements model-free, dopamine-dependent RL for habitual action selection.
- **Dorsolateral prefrontal cortex (dlPFC)** — involved in switching between state spaces when the global task representation changes; BOLD value signals track attention-weighted model; part of the frontoparietal attention control network.
- **Frontoparietal attention network** (including intraparietal sulcus, precuneus, dlPFC) — classically associated with attentional control; implicated in switching attention between task dimensions during learning, thereby switching between alternative task representations.
- **Hippocampus** — implicated in novelty detection and in determining when to create a new state versus update an existing one; lesions abolish context-sensitivity of extinction and latent inhibition; developmental immaturity associated with over-generalisation; sequential replay of task states in hippocampus at rest improves OFC state representations.
- **Dopaminergic system / VTA** — carries reward prediction errors; expectancy-related changes in dopamine neuron firing depend on OFC; locus coeruleus dopamine may support model-based learning in hippocampus.

---

### Mechanistic insight

The paper does not meet the full bar for mechanistic insight as defined. It synthesises evidence from fMRI MVPA, lesion studies, and electrophysiology, but:

- The attention-weighted RL algorithm is fitted to human behaviour and neural BOLD signals (showing better fit than alternatives), but the neural data (fMRI) do not specifically distinguish this algorithm from nearby alternatives at the level of individual trial-by-trial attention updates — the decoding is of value and prediction error signals, not of the attention-update process itself.
- The OFC-as-state-representation hypothesis is supported by multivariate decoding of task states from OFC fMRI data, and by rodent electrophysiology showing state-structure encoding in OFC above and beyond reward value. However, the paper does not identify specific cell types, microcircuit mechanisms, or neuromodulatory processes implementing the state pointer in OFC.
- The latent-cause inference framework is validated behaviourally (gradual extinction, circles task, memory experiments) but no neural recording data specifically adjudicates between the Bayesian clustering model and simpler alternatives at a mechanistic level.

The paper thus provides strong computational-level and some algorithmic-level evidence but falls short of implementational detail.

---

### Limitations & open questions

- The trial-by-trial mechanism by which feedback shapes attention (the "attention-update" rule) is unknown computationally and neurally: what statistics of task performance signal that the wrong dimensions are being attended?
- It is unclear whether selective attention operates via gating of cortical afferents to the striatum, weighting within the striatum, or shaping of cortical (OFC) representations.
- The neural algorithm for online learning of a task-state representation — as distinct from representing an already-learned state — remains unidentified.
- How the OFC generates "pointers" that are arbitrary and task-specific, and how it switches rapidly between representations for different tasks, is not explained.
- The role of unsupervised statistical learning of input structure (relevant to determining which features can in principle be task-relevant) is not addressed.
- The statistics of natural tasks — whether the brain is adapted to assume sparsity of relevant dimensions — are unknown.
- Deep RL provides a partial existence proof for learned representations but requires millions of trials and lacks flexible cross-task generalisation, leaving open whether the brain uses a fundamentally different approach.
- Individual differences in latent-cause inference (e.g., those who extinguish fear faster show more spontaneous recovery) are noted but not explained mechanistically.

---

### Connections & keywords

- **Key citations**: Sutton & Barto (RL textbook); Gershman, Blei & Niv 2010 (latent-cause inference framework); Leong et al. 2017 (attention-weighted RL, Neuron); Schuck et al. 2016 (OFC cognitive map of state space, Neuron); Wilson et al. 2014 (OFC as cognitive map of task space, Neuron); Gershman et al. 2013 (gradual extinction, Front. Behav. Neurosci.); Schuck & Niv 2019 (hippocampal replay of task states, Science); Niv et al. 2015 (RL in multidimensional environments, J. Neurosci.); Silver et al. 2017 (AlphaGo); Mnih et al. 2015 (DQN/Atari).
- **Named models or frameworks**: Attention-weighted reinforcement learning (AWRL); Latent-cause inference / Bayesian non-parametric clustering (Chinese Restaurant Process); Dimensions Task; Partially observable Markov decision process (POMDP, implicit); model-free vs. model-based RL; SUSTAIN (Love et al. 2004, cited as prior clustering model).
- **Brain regions**: Orbitofrontal cortex (OFC), ventral striatum, dorsal striatum, dorsolateral prefrontal cortex (dlPFC), intraparietal sulcus, precuneus, hippocampus, VTA, locus coeruleus.
- **Keywords**: representation learning, task-state representation, attention-weighted reinforcement learning, latent-cause inference, orbitofrontal cortex cognitive map, dimensionality reduction, partially observable states, fear extinction, spontaneous recovery, Bayesian clustering, prediction error, frontoparietal attention network
