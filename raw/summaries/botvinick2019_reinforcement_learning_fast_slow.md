---
source_file: botvinick2019_reinforcement_learning_fast_slow.md
title: "Reinforcement Learning, Fast and Slow"
authors: Matthew Botvinick, Sam Ritter, Jane X. Wang, Zeb Kurth-Nelson, Charles Blundell, Demis Hassabis
year: 2019
journal: Trends in Cognitive Sciences
paper_type: review
contribution_type: theoretical
---

### One-line summary

Recent deep RL techniques — episodic deep RL and meta-RL — overcome the sample inefficiency of early deep RL by showing that fast learning is always parasitic on slower, incremental learning that builds representations and inductive biases, a principle the authors argue applies equally to biological brains.

---

### Background & motivation

Early deep RL systems achieved superhuman performance on games such as Atari and Go but required orders of magnitude more training data than human experts, prompting critics to argue that deep RL is too sample-inefficient to be a plausible model of human learning. Two structural causes of this slowness are (1) the need for incremental, small-step gradient-descent parameter updates to avoid catastrophic interference, and (2) the weak inductive bias of generic neural networks, which must consider a vast hypothesis space before converging on a solution. This review argues that subsequent AI advances — specifically episodic deep RL and meta-RL — address both causes, reviving deep RL as a scientifically productive framework for psychology and neuroscience.

---

### Methods

This is a narrative review covering the following topics:

- **Scope**: deep RL methods developed in AI research circa 2013–2019, with particular focus on episodic deep RL (e.g., Neural Episodic Control, model-free episodic control) and meta-RL (Wang et al. 2016/2018; Duan et al. 2016).
- **Synthesis approach**: conceptual analysis of two AI techniques, mapping of their computational principles onto psychological constructs (episodic memory, learning-to-learn) and neuroscientific data (prefrontal cortex physiology, dopamine RPE signals, hippocampal reinstatement).
- **Illustrative simulations cited**: meta-RL trained on two-armed bandit tasks (Box 3), Harlow learning-set task modelling (Wang et al. 2018), and episodic meta-RL in bandit and navigation tasks (Ritter et al. 2018).
- **Key frameworks reviewed**: complementary learning systems theory (Kumaran et al. 2016), hierarchical Bayesian models of inductive bias, evolutionary accounts of architectural bias.

---

### Key findings

For a review, the major conclusions drawn are:

- **Episodic deep RL** bypasses the incremental update bottleneck by storing raw experience and querying it by similarity at decision time, enabling one-shot generalisation from individual events. Its speed, however, depends critically on slow gradient-descent learning of the state-embedding metric.
- **Meta-RL** addresses weak inductive bias by training a recurrent network across a distribution of related tasks; the slow outer-loop weight learning sculpts the network's recurrent dynamics to implement a separate, fast inner-loop learning algorithm, embodying inductive biases suited to the task distribution.
- **Episodic meta-RL** (Ritter et al. 2018) combines both mechanisms: episodic memory reinstates hidden-unit activity patterns from prior task encounters, enabling immediate retrieval of previously discovered solutions on second or later visits.
- **Unifying principle**: in every case examined, fast learning is enabled by — and logically depends on — slow learning; fast learning cannot arise without a prior slow process that establishes useful representations or inductive biases.
- **Neural mapping (from Wang et al. 2018)**: meta-RL provides a single framework that accounts for (a) the coding of value-related decision variables (current value, last action, last reward, action×reward interaction) in individual dlPFC neurons; (b) the presence of model-based information in ventral striatal prediction error signals (fMRI); and (c) the emergence of a model-based inner-loop algorithm from a model-free outer-loop training signal.
- **Evolutionary extension**: the same fast–slow principle extends across timescales — evolutionary selection shapes architectural and algorithmic biases (the "slowest" loop) that enable faster lifetime learning.

---

### Computational framework

**Reinforcement learning**, specifically deep RL, with extensions to meta-learning and episodic control.

- **Core RL formalism**: an agent learns a policy mapping states to actions to maximise cumulative discounted reward; in deep RL the policy (or value function) is parameterised by a deep neural network trained via gradient descent on temporal-difference or policy-gradient objectives.
- **Episodic deep RL**: value of a new state is estimated as a weighted sum of stored reward sums from past states, weighted by similarity between stored and current state embeddings. Embeddings are learned slowly; value retrieval is fast and non-parametric.
- **Meta-RL**: an outer RL loop (gradient descent on weights θ) trains a recurrent network (LSTM) over a distribution of tasks; the inner loop is the emergent activity-dynamics algorithm implemented by the trained recurrent network, which adjusts behavior within each episode without weight updates.
- **Key assumptions**: (1) task distributions have shared structure the outer loop can exploit; (2) similar states warrant similar actions (smoothness prior embedded in episodic RL); (3) slow learning is generic and domain-general; fast learning is rapid but constrained to the task distribution encountered during slow learning.

---

### Prevailing model of the system under study

The paper addresses the systems-level organisation of learning and memory in the brain, and frames its argument against two prior models. First, the **standard deep RL model of brain learning**: dopamine neurons carry a reward prediction error (RPE) signal that drives incremental, model-free synaptic change in corticostriatal connections, habituating the animal to repeat reinforced actions — a framework widely seen as disconnected from the fast, flexible learning that characterises human cognition. Second, the **complementary learning systems (CLS) model** (McClelland, Kumaran et al.): hippocampus supports rapid episodic encoding while neocortex slowly abstracts statistical regularities; the two systems interact but are largely independent in their learning modes. The prevailing critique of deep RL (Lake et al. 2015; Marcus 2018) is that it is too slow to model human learning, and that its internal representations lack the structured, compositional character of human knowledge.

---

### What this paper contributes

The review establishes that the sample-inefficiency critique applies only to first-generation deep RL; more recent techniques can learn rapidly, partially reinstating deep RL as a candidate model of biological learning. More substantively, the paper contributes the theoretical claim that **fast learning necessarily depends on slow learning** — a principle it argues is not merely an engineering choice but a logical necessity traceable to the bias–variance trade-off. This reframes the relationship between multiple memory systems: rather than treating fast (hippocampal/episodic) and slow (neocortical/weight-based) learning as parallel and complementary, the paper proposes a **hierarchical dependency** in which the slow system's products (representations, inductive biases) are prerequisites for the fast system's operation. It also extends this logic to evolutionary timescales, proposing that evolution acts as the slowest outer learning loop, sculpting architectural biases that enable faster lifetime learning. Finally, by linking meta-RL to specific neural phenomena (dlPFC neuron tuning, model-based striatal RPEs), the paper identifies concrete empirical predictions for neuroscience.

---

### Brain regions & systems

- **Prefrontal cortex (PFC), especially dorsolateral PFC** — proposed locus of the inner-loop learning algorithm in meta-RL; neurons in dlPFC code for the key decision variables (current value, previous action, previous reward, action×reward interaction) that an efficient bandit-learning policy requires, and meta-RL trained on the same task acquires the same coding properties.
- **Midbrain dopamine system / ventral striatum** — proposed substrate of the outer-loop (slow, model-free) weight-update signal; classically thought to carry model-free RPEs, but Wang et al. (2018) show that meta-RL's RPEs contain model-based information, paralleling fMRI evidence of model-based signals in ventral striatum (Daw et al. 2011).
- **Hippocampus** — central to episodic deep RL and episodic meta-RL; implicated in storing state–reward associations and reinstating cortical (including PFC working-memory) activity patterns; the reinstatement mechanism in episodic meta-RL was directly inspired by hippocampal-to-cortical reinstatement data.
- **Corticostriatal circuits broadly** — the proposed site of slow synaptic plasticity driven by dopamine that tunes recurrent PFC dynamics over the course of learning.

---

### Mechanistic insight

The paper does not present new empirical data. It reviews and synthesises computational modelling and prior empirical work (Wang et al. 2018; Ritter et al. 2018; Daw et al. 2011; Tsutsui et al. 2016).

The paper comes close to meeting the mechanistic bar via the Wang et al. (2018) work cited extensively in Box 4: that study trained meta-RL on tasks for which neural recordings and fMRI data exist, and found that the model's internal units and RPE signals match the empirical measurements. This constitutes a specific algorithm (meta-RL with LSTM recurrent dynamics) aligned with neural data. However, the present paper is a review that describes this correspondence rather than presenting it as new results.

At Marr's levels, the proposed account is:
- **Computational**: the brain solves the problem of efficient reward-maximisation across a structured distribution of tasks encountered over a lifetime.
- **Algorithmic**: slow dopamine-driven synaptic plasticity (outer loop) sculpts recurrent PFC dynamics to implement a fast inner-loop learning algorithm; episodic memory (hippocampus) further accelerates learning by reinstating prior task solutions.
- **Implementational**: LSTM-like recurrent units in PFC; dopaminergic RPE signals modifying corticostriatal weights; hippocampal–cortical reinstatement of hidden-unit patterns. The paper discusses these proposals but does not provide new mechanistic evidence.

---

### Limitations & open questions

- Whether the proposed mechanisms scale to the richness and diversity of real human environments is unresolved; current meta-RL and episodic deep RL demonstrations are in relatively simple bandit, navigation, and arcade-game settings.
- The neural implementation of gradient descent — or its biological analogue — remains unknown; it is unclear whether a synaptic plasticity rule in the brain genuinely mirrors the mathematical gradient descent assumed by the outer loop.
- What specific inductive biases are most important for human learning, and whether they are evolutionarily specified vs. acquired through early development, is left open.
- The role of active, strategic exploration — a major driver of human sample efficiency — is not addressed by either episodic deep RL or meta-RL as reviewed here.
- The review focuses on two techniques; other contributors to human learning speed (language, social transmission, causal reasoning, compositionality) are acknowledged but not integrated.
- The mapping of meta-RL to biology relies heavily on Wang et al. (2018), a single modelling study; independent empirical tests of the meta-RL account of PFC and dopamine are needed.

---

### Connections & keywords

**Key citations**:
- Wang et al. (2016/2018) — "Learning to reinforcement learn" / "Prefrontal cortex as a meta-reinforcement learning system"
- Duan et al. (2016) — RL² fast RL via slow RL
- Ritter et al. (2018) — episodic meta-RL / episodic control as meta-RL
- Pritzel et al. (2017) — Neural Episodic Control
- Blundell et al. (2016) — model-free episodic control
- Mnih et al. (2015) — DQN
- Kumaran et al. (2016) — complementary learning systems updated
- Harlow (1949) — learning sets / learning to learn
- Daw et al. (2011) — model-based influences on human choices and striatal prediction errors
- Gershman & Daw (2017) — RL and episodic memory integrative framework
- Lake et al. (2015) — human-level concept learning (the critique being countered)
- McClelland et al. (1995) — complementary learning systems

**Named models or frameworks**:
- Deep Q-Network (DQN)
- Neural Episodic Control (NEC)
- Meta-RL (Wang et al. / Duan et al.)
- Episodic meta-RL (Ritter et al.)
- Complementary learning systems (CLS) theory
- Harlow learning-set paradigm
- TD-gammon

**Brain regions**:
- Prefrontal cortex (PFC), dorsolateral PFC
- Ventral striatum
- Midbrain dopamine system
- Hippocampus
- Corticostriatal circuits

**Keywords**:
- deep reinforcement learning
- meta-learning / meta-RL
- episodic memory
- sample efficiency
- inductive bias
- complementary learning systems
- fast-and-slow learning
- reward prediction error
- prefrontal cortex recurrent dynamics
- dopamine-dependent synaptic plasticity
- learning to learn
- bias-variance trade-off
