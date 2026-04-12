---
source_file: "moneta2024_ofc_vmpfc_representational_spaces.md"
paper_id: "moneta2024_ofc_vmpfc_representational_spaces"
title: "Representational spaces in orbitofrontal and ventromedial prefrontal cortex: task states, values, and beyond"
authors: "Nir Moneta, Shany Grossman, Nicolas W. Schuck"
year: 2024
journal: "Trends in Neurosciences"
paper_type: "review"
contribution_type: "review"
species: ["human"]
methods: ["electrophysiology", "fmri", "lesion"]
brain_regions: ["hippocampus", "prefrontal_cortex", "medial_prefrontal_cortex", "orbitofrontal_cortex", "ventromedial_prefrontal_cortex", "striatum"]
frameworks: ["reinforcement_learning", "model_based_rl", "successor_representation", "latent_state_inference", "mixed_selectivity"]
keywords: ["representational", "spaces", "orbitofrontal", "ventromedial", "prefrontal", "cortex", "task", "states", "values", "beyond"]
key_citations: ["padoaschioppa2006_orbitofrontal_economic_value"]
---

### One-line summary

OFC and vmPFC do not merely encode a scalar expected value signal but represent rich, multidimensional task-state spaces that intertwine value with latent context, and this representational structure parallels the late-layer activations of deep reinforcement learning models.

---

### Background & motivation

A dominant view in decision neuroscience has held that OFC and vmPFC provide a "common currency" value signal — an abstract, content-independent scalar encoding expected reward — that guides choice across incommensurable options. However, accumulating evidence that these regions also encode context, task states, and task-irrelevant information challenges this view. This review addresses the gap by integrating findings from human fMRI, primate single-unit recording, rodent lesion work, and deep RL modelling to argue that OMPFC (orbital and medial prefrontal cortex) representations are fundamentally structured around partially observable task states rather than pure value. Understanding this broader function is necessary to explain why value signals in OMPFC are context-sensitive, goal-dependent, and intermixed with non-value variables.

---

### Methods

This is a narrative review. The authors:

- Surveyed human fMRI, non-human primate electrophysiology, and rodent lesion/recording studies examining value and task-state encoding in OFC and vmPFC.
- Focused on studies demonstrating mixed selectivity, context-dependence of value signals, partially observable state representations, and goal-dependency.
- Drew on a key original study by Moneta et al. (2023, Nat. Commun.) from the authors' own group, in which fMRI multivariate decoding showed that vmPFC simultaneously encodes task context and expected value, and that the strength of the context signal modulates which value representation dominates.
- Used deep reinforcement learning (DRL) models — particularly deep Q-networks (DQNs) and actor-critic recurrent architectures — as computational comparison points, examining whether late hidden-layer representations in such networks share properties with OMPFC representations.
- Discussed extensions including meta-RL, model-based RL, and hippocampus-OFC interactions as mechanisms supporting flexible long-term learning.

---

### Key findings

- Value signals in OFC/vmPFC are systematically modulated by task context: neurons and voxels encoding value also encode contextual and state information, exhibiting mixed selectivity.
- In Moneta et al. (2023): vmPFC simultaneously encodes task context and expected value; stronger context decoding was correlated with stronger value decoding within participants; participants with stronger context-value coupling showed less behavioral interference from irrelevant context.
- vmPFC also represents the "alternative expected value" — the hypothetical value under the currently irrelevant context — and context signal strength modulates competition between the relevant and alternative value signals.
- Single neurons in macaque OFC show mixed selectivity for probability and flavor, and for spatial and reward information simultaneously; population-level orthogonality allows independent readout of each variable.
- OFC lesions in rats disrupt reward-related dopamine firing in a way consistent with OFC signalling latent, partially observable task states.
- Human fMRI shows partially observable states can be decoded from medial OFC.
- Late layers of deep RL models spontaneously develop mixed-selectivity representations including non-value task-state information (e.g., game-state abstractions in Atari DQNs, chess concepts in AlphaZero), paralleling OMPFC coding.
- However, a direct quantitative correspondence between deep RL late-layer geometry and human OMPFC fMRI signals has not yet been established; one study explicitly failed to find such a link.
- Evidence suggests hippocampus-OFC interactions support reinstatement of prior value knowledge and model-based flexibility via offline replay.

---

### Computational framework

The paper uses **reinforcement learning (RL)** as its primary computational lens, specifically extending to **deep reinforcement learning (deep RL)** as a model of OMPFC function.

Core formalism:

- In RL, an agent learns to maximise cumulative reward by estimating the expected value of actions or states. The key formal objects are: states (collections of observable/latent information sufficient to predict outcomes), values (expected future reward from a state), and a policy (mapping from states to actions).
- States are defined as elements of a Markov decision process (MDP); in partially observable MDPs, the current state cannot be fully inferred from current sensory input alone, requiring inference over history.
- Deep RL models extend this by learning representations directly from high-dimensional sensory input via multilayer neural networks, with the objective function (typically reward maximisation) shaping late-layer representations into compact, task-relevant world models.
- The review argues that OMPFC corresponds computationally to the late (fully-connected) layers of such networks: its representations emerge from a value-maximisation objective but are not reducible to a single value variable.
- Meta-RL and model-based RL are discussed as extensions enabling flexible generalisation across tasks and planning via state-transition models.

---

### Prevailing model of the system under study

Prior to this review's contribution, the dominant account of OFC/vmPFC function was the **common currency hypothesis**: these regions compute a scalar, abstract expected value that places incommensurable options on a single cardinal scale, enabling comparison and choice. This view was supported by findings that OFC value signals are invariant to sensory features, motor aspects, and menu composition (Padoa-Schioppa & Assad, 2006), and that vmPFC value signals generalise across tasks with different goals, effort types, and commodity types. Lesion studies confirmed that damage to these regions impairs value-based choice. The working assumption was that OMPFC's role in decision-making was predominantly to provide this generalised value signal, with other information (context, state) represented elsewhere and merely modulating OMPFC output.

---

### What this paper contributes

The review establishes that the common currency framing is insufficient. The key contributions are:

1. **Value and task-state representations are intertwined in OMPFC**, not separable. Context and value signals co-reside in the same voxels/neurons, interact quantitatively, and together determine behaviour — OMPFC is not a downstream value readout but an upstream integrator.
2. **OMPFC encodes latent, partially observable task states**, not just the current sensory description of value-relevant options. This extends prior evidence for state encoding to include the competitive interaction between states and their associated values.
3. **Mixed selectivity is the rule, not the exception**: single neurons multiplex value, context, reward history, and alternative values; population-level orthogonality nonetheless permits independent readout.
4. **Deep RL models provide a normative account**: value-maximising architectures spontaneously develop mixed-selectivity, task-state-rich representations in their late layers, suggesting that OMPFC's representational complexity is not an add-on but an expected consequence of solving partially observable reward-maximisation problems.
5. **Value should be reconceptualised** as a multidimensional signal tracking distance to task-relevant goals rather than a scalar accumulation of reward.

Outstanding gaps identified: direct quantitative correspondence between deep RL layer geometry and OMPFC signals remains unconfirmed; the role of hippocampus-OFC interactions in meta-learning and long-horizon generalisation needs further investigation; the functional significance of task-irrelevant representations in OMPFC is unresolved.

---

### Brain regions & systems

- **Orbitofrontal cortex (OFC)** — primary region under study; proposed to encode latent task states, mixed-selectivity value and context representations, and to interact with hippocampus for state-based learning.
- **Ventromedial prefrontal cortex (vmPFC)** — closely related region; shown by multivariate fMRI to simultaneously encode expected value and task context, with context signal modulating value competition.
- **Orbital and medial prefrontal cortex (OMPFC)** — umbrella term used in the review, broadly corresponding to OFC + vmPFC as defined by Ongur & Price (2000).
- **Hippocampus** — discussed as a key interacting partner: provides relational/cognitive map representations, supports offline replay linked to OFC state representations, and is proposed to enable reinstatement of prior value knowledge.
- **Striatum / dopamine system** — referenced as the locus of prediction error signals and actor-critic learning signals that interact with OMPFC computations.
- **Lateral prefrontal and frontal cortex** — noted as broader context for mixed-selectivity phenomena, which are not unique to OMPFC.

---

### Mechanistic insight

The paper does not fully meet the high bar for mechanistic insight as defined here. It presents a detailed **algorithmic account** — OMPFC computes partially observable task states via a value-maximisation objective, producing mixed-selectivity representations from which downstream neurons can independently read out value and context — and supports this with neural data (fMRI decoding, single-unit recordings). However, the paper does not provide neural data that specifically arbitrates between this task-state RL algorithm and alternative accounts at the level of individual experiments: the deep RL analogy remains largely qualitative, and the key fMRI study (Moneta et al., 2023) demonstrates correlation between context and value decoding strength but does not directly test the mechanistic claim that the architecture is implementing state-based RL.

At Marr's levels:

- **Computational**: OMPFC solves the problem of predicting outcomes in partially observable environments by integrating sensory, contextual, and historical information into a latent state representation that supports value computation.
- **Algorithmic**: Representations are structured as a high-dimensional mixed-selectivity code where context and value are non-linearly multiplexed at the single-unit level but orthogonally separable at the population level, analogous to late layers in deep RL.
- **Implementational**: Not addressed. The review does not discuss specific cell types, connectivity motifs, or biophysical mechanisms within OFC/vmPFC.

---

### Limitations & open questions

- No direct quantitative link has been established between deep RL late-layer representational geometry and OMPFC fMRI or electrophysiology; existing comparisons are qualitative.
- The paper acknowledges that OMPFC represents task-irrelevant information and irrelevant values — a finding in tension with pure state-compression accounts — and does not fully resolve whether this is a "feature" (adaptive latent knowledge) or "bug" (incomplete compression).
- Most deep RL models discussed are model-free; the relationship between model-based RL, hippocampal replay, and OMPFC is proposed but not systematically reviewed with strong empirical evidence.
- Anatomical subdivisions within OFC/vmPFC are noted but not tractably resolved due to cross-species terminological inconsistencies.
- The review does not address whether OMPFC's role is most prominent during early learning or stable performance.
- The conditions under which value-free versus value-based computations occur in OMPFC, and how to disentangle them empirically, remain open.
- The specific architecture (recurrent vs. feed-forward, layer depth, activation function) of the deep RL analog best matching OMPFC is unspecified.

---

### Connections & keywords

**Key citations**:
- Padoa-Schioppa & Assad (2006) — foundational single-unit OFC value encoding in monkeys
- Schuck et al. (2016, Neuron) — human OFC encodes partially observable task states (cognitive map of state space)
- Moneta et al. (2023, Nat. Commun.) — task state representations in vmPFC mediate relevant and irrelevant value signals
- Wilson et al. (2014, Neuron) — OFC as cognitive map of task space
- Niv (2019, Nat. Neurosci.) — learning task-state representations
- Mnih et al. (2015, Nature) — deep Q-networks achieving human-level control
- Rigotti et al. (2013, Nature) — importance of mixed selectivity in complex cognition
- Behrens et al. (2018, Neuron) — what is a cognitive map?
- Stachenfeld et al. (2017, Nat. Neurosci.) — hippocampus as predictive map (successor representation)
- Bartra et al. (2013, NeuroImage) — meta-analysis of value signals in BOLD fMRI
- Frömer et al. (2019, Nat. Commun.) — goal congruency dominates reward value in vmPFC
- Juechems & Summerfield (2019, Trends Cogn. Sci.) — where does value come from?

**Named models or frameworks**:
- Common currency hypothesis (OFC/vmPFC as scalar value encoder)
- Reinforcement learning (RL) / partially observable MDP framework
- Deep Q-network (DQN)
- Actor-critic architecture
- Meta-RL (slow weight / fast activity dynamics)
- Model-based RL
- Successor representation
- Mixed selectivity (Rigotti et al.)

**Brain regions**:
- Orbitofrontal cortex (OFC)
- Ventromedial prefrontal cortex (vmPFC)
- Orbital and medial prefrontal cortex (OMPFC)
- Hippocampus
- Striatum

**Keywords**:
- orbitofrontal cortex value encoding
- task state representation
- partially observable Markov decision process
- mixed selectivity
- deep reinforcement learning
- representational geometry
- cognitive map
- context-dependent value
- vmPFC multivariate decoding
- goal-dependent value signals
- hippocampus-OFC interaction
- latent state inference
