---
source_file: "bowling2022_reward_hypothesis_reinforcement.md"
paper_id: "bowling2022_reward_hypothesis_reinforcement"
title: "Settling the Reward Hypothesis"
authors: "Michael Bowling, John D. Martin, David Abel, Will Dabney"
year: 2022
journal: "DeepMind Technical Report"
paper_type: "computational"
contribution_type: "theoretical"
species: ["human"]
frameworks: ["reinforcement_learning"]
keywords: ["settling", "reward", "hypothesis"]
key_citations: ["silver2021_reward_artificial_intelligence"]
---

### One-line summary

The reward hypothesis — that all goals and purposes can be expressed as maximisation of expected cumulative scalar reward — holds if and only if an agent's preference relation satisfies the four von Neumann-Morgenstern rationality axioms plus a new "Temporal γ-Indifference" axiom, which together are necessary and sufficient for the existence of a Markov reward function.

---

### Background & motivation

Sutton's reward hypothesis asserts that any goal or purpose can be captured by maximising the expected cumulative sum of a scalar reward signal, providing a theoretical foundation for reinforcement learning as a sufficient framework for building intelligent systems. Prior work (Abel et al., 2021; Shakerinava & Ravanbakhsh, 2022) had examined expressivity limitations of Markov reward under specific environment-relative definitions of goals, but no general, conclusive account had been given for when the hypothesis holds and when it fails. This paper aims to fully settle the question by deriving the precise axiomatic conditions on preference relations under which the hypothesis is true.

---

### Methods

The paper is a formal theoretical analysis with no empirical component.

- Goals and purposes are formalised as binary preference relations over distributions of finite observation-action histories, decoupled from any particular environment dynamics.
- The four classical von Neumann-Morgenstern (vNM) rationality axioms (completeness, transitivity, independence, continuity) are adopted as baseline conditions.
- A new axiom — Temporal γ-Indifference — is derived and introduced; it states that prepending a transition t to two history distributions A and B scales the preference between them by a transition-dependent factor γ(t) ∈ [0,1].
- The main result (Theorem 2: Markov Reward Theorem) is proved: Axioms 1–5 are necessary and sufficient for a preference relation to be expressible as the expected cumulative sum of a Markov reward under a transition-dependent discount.
- The framework is extended to an "objective goals" setting in which preferences originate from an agent designer observing a potentially richer observation stream.
- A constructive algorithm (Algorithm 1) is provided that derives both a reward function r and discount function γ from any preference relation satisfying Axioms 1–5, with time complexity O((|A|×|O|)²).
- The axiomatic account is applied to explain why specific counterexamples from Abel et al. (2021) — steady-state and entailment types — violate particular assumptions or axioms.
- Challenges to the reward hypothesis (human irrationality, multiple objectives, constrained MDPs, risk-sensitive objectives) are analysed within the axiomatic framework to identify which axioms each violates.

---

### Key findings

- **Main theorem**: A preference relation admits a Markov reward representation (consistent with expected cumulative reward under transition-dependent discounting) if and only if it satisfies the four vNM axioms plus the Temporal γ-Indifference axiom (Axiom 5).
- **Unification of RL objectives**: The form of γ(t) in Axiom 5 determines the reward objective type — discounted (constant γ < 1), average reward (γ = 1), or episodic (γ = 0 at terminal transitions) — so the objective type is not a modelling choice but a consequence of the preference structure.
- **Explanation of known counterexamples**: Abel et al.'s steady-state failure violates Assumption 2 (policy preferences must be consistent with induced history distributions), and the entailment failure violates Axiom 5 directly.
- **Constrained MDPs violate independence and continuity**: Constrained MDP objectives can produce preferences that violate both Axiom 3 (independence) and Axiom 4 (continuity), and additionally violate the weaker Sequential Consistency axiom introduced in the appendix.
- **Risk-sensitive objectives**: Risk-sensitive (e.g., variance-penalised) objectives that require non-Markov optimal policies violate Axiom 5, but can be accommodated via the objective goals formulation through state augmentation.
- **Multi-objective RL**: Multi-dimensional reward is strictly more expressive than scalar reward (Miura, 2022) at the cost of violating at least one axiom, most naturally the independence axiom.
- **Generalisation of prior axioms**: Temporal γ-Indifference is shown to generalise both the Memoryless axiom and the Additivity axiom of Shakerinava & Ravanbakhsh (2022) as special cases (Theorems 3 and 4).

---

### Computational framework

The paper uses **utility theory and decision theory**, specifically the von Neumann-Morgenstern expected utility framework extended to sequential (infinite-horizon) settings.

**What is being modelled**: The representational capacity of scalar reward signals to encode arbitrary goal preferences in a general sequential decision-making setting.

**Key variables and quantities**:
- Preference relation ≿ over distributions in Δ(H), where H is the space of finite observation-action histories.
- Utility function u: Δ(H) → ℝ derived from the vNM theorem.
- Markov reward function r: T → ℝ where T = O × A (or designer observations in the objective setting).
- Transition-dependent discount function γ: T → [0,1] appearing in the new Temporal γ-Indifference axiom.
- Expected cumulative value V_n^π = E[Σ_{i=1}^{n} γ_{1:i} r_i] under a transition-dependent compounding discount.

**Key assumptions**:
- Goals and purposes are preference relations over history distributions, independent of environment dynamics.
- Preferences over policies are grounded in the eventually-dominating distributions over histories they induce.
- A Markov reward is one that depends only on the most recent transition (observation-action pair), not on the full history.

---

### Prevailing model of the system under study

The paper's introduction characterises the prevailing view as follows: Sutton's reward hypothesis is widely assumed in RL as an informal but foundational claim about the sufficiency of scalar reward for expressing any goal. Silver et al.'s "reward is enough" hypothesis extends this to intelligence more broadly. However, the hypothesis had not been formally proved or refuted in full generality. Prior formalisation attempts either grounded goals relative to environment state spaces (Abel et al., 2021), which exposed expressivity gaps for Markov reward, or used controlled MDPs with vNM-style axioms (Shakerinava & Ravanbakhsh, 2022), but remained tied to Markovian environment structures. The field lacked a general, environment-independent axiomatic account of when the hypothesis holds. The implicit working assumption was that the hypothesis is "probably true for sufficiently rich reward functions" but with acknowledged holes in edge cases involving non-Markov behaviours, multiple objectives, and risk-sensitive objectives.

---

### What this paper contributes

The paper provides the first complete, environment-independent axiomatic characterisation of the conditions under which the reward hypothesis holds. Before this paper, it was known that Markov reward has expressivity limitations in certain environments (Abel et al., 2021) and that utility-theoretic axioms could justify reward in controlled MDPs (Shakerinava & Ravanbakhsh, 2022), but no general necessary-and-sufficient condition was established. After this paper:

- We can say precisely that any preference relation satisfying vNM rationality plus Temporal γ-Indifference admits a Markov reward representation — and no further conditions are needed.
- We have a principled explanation for why specific classes of goals (constrained MDPs, risk-sensitive objectives, entailment-type preferences) cannot be captured by Markov reward: they violate specific named axioms.
- The objective type (discounted, average-reward, episodic) is shown to be a consequence of the preference structure, not an external modelling choice.
- A constructive polynomial-time algorithm for deriving a reward function and discount factor from a rational preference relation is provided.
- The framework accommodates both "subjective goals" (agent-internal reward) and "objective goals" (designer-specified reward), unifying reward learning and reward design under the same theoretical account.

---

### Brain regions & systems

Not applicable. The paper is a formal theoretical analysis in reinforcement learning / decision theory with no anatomical, neural, or cognitive neuroscience content. The level of analysis is purely computational/algorithmic in Marr's sense — specifying what problem is being solved and under what representational conditions it can be solved with expected cumulative reward.

---

### Mechanistic insight

The paper does not meet the bar for this section. It proposes a formal axiomatic framework and proves a representation theorem, but presents no neural data, no empirical experiments, and no claims about how reward computations are implemented in biological or artificial systems. It operates entirely at Marr's computational level — characterising what goals can be represented as reward — with no algorithmic link to measured neural processes.

---

### Limitations & open questions

- **Finiteness assumption**: Observations O and actions A are assumed finite (possibly countable). Whether results generalise to uncountable spaces is noted as an open question.
- **Policy preference formalisation**: The "eventually dominates" definition of policy preferences (Assumption 2) is acknowledged as one of several possible resolutions for infinite sequences; alternatives (Sobel, 1975; Pitis, 2019) are noted but not fully compared.
- **Human irrationality**: The framework requires rational preference relations; the paper explicitly brackets irrationality (Kahneman-Tversky violations of vNM axioms) as outside its scope. It does not address how to handle agents with irrational goals.
- **Multiple objectives**: Multi-objective RL is more expressive than scalar reward; the paper explains why (axiom violations) but does not resolve how to extend the framework to capture it within a reward-hypothesis-like account.
- **Non-Markov reward structures**: The objective goals framework can accommodate reward bundles and non-Markov reward expressed relative to designer observations, but the full scope of this extension is not worked out in detail.
- **Computability**: The constructive algorithm assumes oracle access to the preference relation; practical elicitation of preferences for large observation-action spaces is not addressed.

---

### Connections & keywords

**Key citations**:
- Sutton (2004) and Sutton & Barto (2018) — original reward hypothesis
- Silver et al. (2021) — reward-is-enough hypothesis
- Abel et al. (2021) — expressivity of Markov reward; steady-state and entailment counterexamples
- Shakerinava & Ravanbakhsh (2022) — utility theory for sequential decision making; Memoryless and Additivity axioms
- Pitis (2019) — decision-theoretic analysis of RL objectives; state-action dependent discount
- von Neumann & Morgenstern (1953) — expected utility theory and rationality axioms
- White (2017) — transition-dependent discounting in RL
- Abel et al. (2022) — expressing non-Markov reward to a Markov agent (reward bundles)

**Named models or frameworks**:
- Reward hypothesis (Sutton)
- Reward-is-enough hypothesis (Silver et al.)
- von Neumann-Morgenstern (vNM) expected utility theory
- Temporal γ-Indifference axiom (new, introduced in this paper)
- Markov Reward Theorem (Theorem 2, main result)
- Constrained MDP
- Partially Observable MDP (POMDP)

**Brain regions**: None.

**Keywords**: reward hypothesis, Markov reward, expected utility theory, utility axioms, temporal discounting, transition-dependent discount, preference relation, sequential decision making, reinforcement learning theory, reward expressivity, multi-objective reinforcement learning, axiomatic decision theory
