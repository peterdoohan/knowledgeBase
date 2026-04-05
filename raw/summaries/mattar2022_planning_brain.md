---
source_file: mattar2022_planning_brain.md
title: "Planning in the brain"
authors: Marcelo G. Mattar, Máté Lengyel
year: 2022
journal: Neuron
paper_type: review
contribution_type: theoretical
---

### One-line summary

This perspective proposes a three-dimensional taxonomy of planning algorithms derived from AI and uses it to systematically review what neuroscientific data currently do — and do not — tell us about how the brain implements planning.

---

### Background & motivation

Planning — the selection of actions based on the anticipated desirability of their outcomes — is a fundamental but poorly understood cognitive process. Although neuroscience has made progress distinguishing goal-directed (planning-based) from habitual (reflexive) behaviour, the specific algorithm(s) the brain uses for planning remain largely unknown. Prior work has been limited by tasks too simple to differentiate between competing algorithms (most use only single-step decisions), and by a lack of a systematic framework for mapping the space of possible algorithms. This paper argues that recent AI breakthroughs in planning algorithms offer exactly such a framework, and that a closer AI–neuroscience symbiosis can drive more precise experimental hypotheses.

---

### Methods

This is a narrative review and theoretical perspective. The authors:

- Draw on classical and state-of-the-art AI planning algorithms (breadth-first search, A*, Monte Carlo tree search, dynamic programming, Dyna, etc.) to construct a taxonomy of planning algorithms organised along three dimensions.
- Survey behavioural and neural data across species (humans, non-human primates, rodents), recording modalities (fMRI, electrophysiology, lesion studies), and task paradigms (sequential decision tasks, navigation, motor control, Tower of Hanoi, board games).
- Evaluate what existing data can and cannot adjudicate regarding algorithmic details at each dimension of the taxonomy.
- Use illustrative computational examples (Box 1, Figure 6) to show how behavioural and neural data could in principle distinguish between specific algorithms (e.g., best-first search vs A*).

---

### Key findings

- **Dimension 1 — Internal model type**: Behavioural and neural data indicate the brain is capable of using stochastic internal models (closed-loop control), though it defaults to deterministic ones when tasks permit open-loop control. Evidence includes: primate PFC encoding planned action sequences, eye/arm movement studies demonstrating stochastic forward models.
- **Dimension 2 — Order of computation (model input)**: Converging evidence from multiple paradigms suggests the brain uses *focused* (heuristic-guided), *depth-limited* (truncated to ~3–6 steps), and *serial* (rather than parallel) evaluation of candidate actions. Hippocampal theta sequences during VTE alternate between candidate paths at ~8 Hz; OFC activity tracks only the currently attended option value.
- **Dimension 3 — Incorporation of outputs**: Evidence exists for both online (decision-time) and offline (background) planning. Hippocampal replay occurs during rest and sleep, extends backward, and can represent non-local states — features inconsistent with purely online planning. Disrupting replay impairs goal-directed behaviour. A normative model (Mattar & Daw, 2018) accounts for replay content and directionality via optimal ordering of Dyna updates.
- Current behavioural and neural data are insufficient to adjudicate between more detailed algorithmic variants (e.g., specific heuristics, exact tree-expansion strategies).
- State-of-the-art AI algorithms (AlphaGo/AlphaZero, MuZero) can be mapped onto the same three-dimensional taxonomy, implying their design insights are relevant — at an abstract level — to understanding biological planning.

---

### Computational framework

The paper uses a **reinforcement learning and classical AI planning** framework. The central formalism is the agent-environment interaction loop (perception-action cycle) formalised as a Markov decision process (MDP):

- **States** (s): representations of the environment.
- **Actions** (a): choices available to the agent.
- **Internal model** (transition function T and reward function R): the agent's representation of how the environment responds to actions.
- **Policy** (π): the mapping from states to actions.
- **Value** (V or Q): expected cumulative reward from a state (or state-action pair).

Planning is defined as querying the internal model to evaluate candidate actions and their sequences in order to select or improve a policy, contrasting with model-free (reflexive) control in which cached policies/values are directly applied. The taxonomy organises planning algorithms along: (1) type of internal model (deterministic vs stochastic; successor representation; abstraction level); (2) input ordering (uninformed vs informed/heuristic, truncation depth, pruning, chunking/options, serial vs parallel); (3) output incorporation (online/decision-time vs offline/background; anytime algorithms; iterative accumulation).

---

### Prevailing model of the system under study

Before this paper, the dominant framing in cognitive neuroscience distinguished *goal-directed* (model-based, planning) from *habitual* (model-free, reflexive) behaviour, supported largely by outcome devaluation and contingency degradation paradigms (Balleine & Dickinson, 1998). Key brain regions had been identified: PFC (especially OFC) for goal-directed control and representing expected outcomes; dorsomedial striatum/caudate for goal-directed behaviour; hippocampus for cognitive maps, episodic memory, and spatial coding. Hippocampal replay was known to occur during rest and sleep and was linked to memory consolidation and, tentatively, offline planning. However, the field lacked a principled framework specifying *which* planning algorithm(s) the brain uses beyond the broad habitual-vs-goal-directed dichotomy. The paper situates itself as trying to move from this binary to a fine-grained algorithmic description.

---

### What this paper contributes

The paper does not report new experimental data. Its contribution is theoretical and organisational:

1. It provides the first systematic **taxonomy** of planning algorithms grounded in AI, which can serve as a common language for neuroscientists.
2. It demonstrates that existing neuroscientific data, when viewed through this taxonomy, converge on a relatively specific algorithmic signature for biological planning: *focused, depth-limited, and serial*.
3. It clarifies what data remain insufficient — most neural findings constrain the broad algorithmic motifs but cannot distinguish between specific algorithms with different internal workings.
4. It proposes concrete directions for progress: richer multi-step behavioural paradigms (ideally navigation-based or game-based), joint behavioural and neural recording, and use of resource-rational or planning-as-inference normative frameworks to systematically generate candidate algorithms.
5. It explicitly shows, via a worked example (Box 1), how neural decoding of latent states could in principle adjudicate between algorithms that produce identical behaviour.

---

### Brain regions & systems

- **Prefrontal cortex (PFC)** — most directly associated with planning; PFC lesions produce stimulus-bound reflexive behaviour; lateral PFC encodes planned action sequences in monkeys.
- **Orbitofrontal cortex (OFC)** — encodes expected outcome value; represents task space; lesions impair outcome-guided behaviour; activity tracks value of the currently attended option (supporting serial evaluation).
- **Medial PFC** — codes for expected reward of chosen actions.
- **Dorsomedial striatum / caudate nucleus** — essential for goal-directed behaviour; lesions abolish devaluation sensitivity while leaving habitual behaviour intact.
- **Hippocampus** — central to the paper's discussion of internal model and planning; encodes cognitive maps (place cells); generates theta sequences (candidate path alternation during VTE) and replay (offline planning during rest/sleep); causally involved in planning; lesions impair outcome-based decisions.
- **Entorhinal cortex / medial temporal lobe** — involved in representing abstract cognitive spaces alongside the hippocampus.
- **Basal ganglia broadly** — implicated in both habitual and goal-directed control; emphasised as a key system whose interaction with PFC and hippocampus during planning is poorly understood.

---

### Mechanistic insight

The paper does not meet the full bar. It is a review/perspective and does not itself present an algorithm formalised at the level of neural implementation, nor does it provide new neural data linking specific algorithmic variables to measured neural activity.

Partial mechanistic content is discussed: hippocampal theta sequences are proposed as a candidate neural substrate for online lookahead (alternating rollouts of candidate paths at ~8 Hz), and hippocampal replay is proposed as a substrate for offline planning, supported by causal manipulations (replay disruption impairs goal-directed behaviour). The Mattar & Daw (2018) normative model accounts for replay content (forward/reverse sequences, reward representation) via optimal Dyna-update ordering. However, the review's own conclusion is that the data remain insufficient to specify the algorithm at a level that would adjudicate between specific competitors, let alone provide a full implementational account in terms of cell types, connectivity, or neuromodulation.

---

### Limitations & open questions

- Most neural evidence constrains broad algorithmic motifs (truncation, pruning, serial evaluation) but cannot adjudicate between specific algorithms within those classes.
- Existing tasks used in animal studies are often too simple (single-step or heavily overtrained) to require planning rather than reflexive strategies; paradigms with changing transition structures are needed.
- The internal model type (deterministic vs stochastic) used by the brain in different tasks remains under-determined: open- vs closed-loop behaviour does not unambiguously imply deterministic vs stochastic models.
- Hippocampal replay's role in planning is suggestive but contested: some evidence shows replay over-represents previously (not currently) rewarded locations, inconsistent with a purely prospective planning account.
- How planning in motor control (continuous state/action spaces, delays, noise) relates to planning in abstract cognitive spaces is unresolved.
- The relationship between offline planning (replay, memory consolidation) and other computational roles of replay (memory maintenance, consolidation, generalisation) is not resolved.
- The paper intentionally omits model learning — how the brain acquires its internal model — leaving open questions about how learning and planning interact.
- Whether state-of-the-art AI neural architectures (deep networks) have direct neural correlates, or are relevant only at an abstract algorithmic level, remains unclear.

---

### Connections & keywords

**Key citations**: Balleine & Dickinson (1998) — goal-directed vs habitual paradigm; Daw et al. (2005) — model-based/model-free competition; Mattar & Daw (2018) — normative model of hippocampal replay; Silver et al. (2016, 2017, 2018) — AlphaGo/AlphaZero; Schrittwieser et al. (2020) — MuZero; Foster & Wilson (2007) — hippocampal theta sequences; Johnson & Redish (2007) — VTE and theta sequences; Tolman (1948) — cognitive map; Dayan (1993) — successor representation; Huys et al. (2012, 2015) — pruning in human planning; van Opheusden et al. (2017) — lookahead in complex game; Sutton & Barto (2018) — reinforcement learning textbook.

**Named models or frameworks**: Markov decision process (MDP); model-based reinforcement learning; Dyna-Q; Monte Carlo tree search (MCTS); A* search; best-first search; successor representation (SR); planning-as-inference; resource-rational analysis; hierarchical reinforcement learning; options framework; vicarious trial and error (VTE); hippocampal replay.

**Brain regions**: prefrontal cortex (PFC), orbitofrontal cortex (OFC), medial PFC, dorsomedial striatum, caudate nucleus, putamen, hippocampus, entorhinal cortex, medial temporal lobe, basal ganglia.

**Keywords**: planning algorithms, model-based decision making, goal-directed behaviour, internal model, hippocampal replay, theta sequences, lookahead, tree search, cognitive map, reinforcement learning, sequential decision making, habitual vs goal-directed control
