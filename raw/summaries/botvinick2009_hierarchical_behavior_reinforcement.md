---
source_file: botvinick2009_hierarchical_behavior_reinforcement.md
paper_id: botvinick2009_hierarchical_behavior_reinforcement
title: "Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective"
authors:
  - "Matthew M. Botvinick"
  - "Yael Niv"
  - "Andrew C. Barto"
year: 2009
journal: Cognition
paper_type: computational
contribution_type: theoretical
tasks:
  - navigation_task
brain_regions:
  - prefrontal_cortex
  - orbitofrontal_cortex
  - dorsolateral_prefrontal_cortex
  - striatum
  - dorsolateral_striatum
  - ventral_striatum
frameworks:
  - reinforcement_learning
  - model_based_rl
  - hierarchical_rl
  - temporal_difference_learning
keywords:
  - hierarchical_reinforcement_learning
  - temporal_abstraction
  - options_framework
  - actor_critic_architecture
  - prefrontal_cortex_task_set_representation
  - option_discovery_subgoal_identification
  - pseudo_reward
  - temporal_difference_prediction_error
  - semi_markov_decision_process
  - positive_and_negative_transfer
  - intrinsic_motivation
  - frontostriatal_circuits
  - hierarchically
  - organized
  - behavior
  - its
  - neural
  - foundations
  - reinforcement
  - learning
wiki_pages:
  - wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning
  - wiki/topics/hierarchical_planning_and_successor_representations_in_prefrontal_hippocampal_cognitive_control
  - wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning
---

### One-line summary

Hierarchical reinforcement learning (HRL) — in which temporally abstract actions (options) are nested within an actor-critic architecture — provides a unifying computational framework for understanding both the psychological structure of hierarchical behavior and its neural substrates in prefrontal cortex, striatum, and orbitofrontal cortex.

---

### Background & motivation

Standard reinforcement learning suffers from a scaling problem: exploration and learning become computationally intractable as the number of states and actions grows. This limitation has been largely overlooked in neuroscience and psychology, where RL has been applied mainly to simple paradigms, yet it is directly relevant to understanding complex real-world behavior. HRL addresses scaling by introducing temporally abstract actions (options) that bundle sequences of primitive actions into reusable subroutines. The paper examines whether the computational machinery of HRL maps onto neural substrates and psychological constructs relevant to hierarchically organized behavior, filling a gap between machine-learning developments and cognitive/neural theory.

---

### Methods

This is a theoretical/computational paper with simulation illustrations.

- The options framework (Sutton et al., 1999) is implemented within an actor-critic architecture, enabling direct comparison with existing neuroanatomical mappings of RL.
- An option is defined by an initiation set, a termination function, and an option-specific policy; options learn via pseudo-reward at subgoal states.
- The actor maintains both a top-level policy and separate option-specific action strengths; the critic maintains both a top-level value function and option-specific value functions.
- Simulations use a "four-rooms" navigation task to illustrate (a) learning of option-specific policies, (b) faster convergence with options versus primitive actions only, and (c) negative transfer when options are poorly matched to the task.
- The framework is compared against other HRL implementations (HAM, MAXQ) and against psychological models (ACT-R, Soar, connectionist models of routine action).

---

### Key findings

- Adding options to the actor-critic framework reduces effective search-tree depth and accelerates learning on the four-rooms task; training time to reach goal state is lower with doorway options than with primitive actions alone.
- Mismatched options produce negative transfer: agents equipped with suboptimal options (targeting "windows" rather than doors) learn more slowly than agents using primitive actions only; agents with doorway options in a modified task with a shortcut converge on a suboptimal path and fail to exploit the shortcut (mean solution times 11.79 vs. 9.73 for primitive-only agents).
- Four key extensions to the actor-critic architecture required by HRL map plausibly onto distinct neural structures:
  1. Option representations and maintenance → dorsolateral prefrontal cortex (DLPFC)
  2. Option-specific policies → dorsolateral striatum (DLS), gated by frontal inputs
  3. Option-specific value functions → orbitofrontal cortex (OFC), given its connectivity with ventral striatum and DLPFC
  4. Extended temporal scope of prediction errors → OFC sustained activity and dopaminergic responses to delayed reward
- The option discovery problem — how useful options are acquired — connects to psychological phenomena including positive/negative transfer, intrinsic motivation, statistical learning of sequential structure, and social transmission of action routines.
- Phasic dopaminergic activity at subtask boundaries and pseudo-reward signals at subgoal attainment are identified as specific, testable empirical predictions.

---

### Computational framework

**Hierarchical reinforcement learning (HRL) — options framework within an actor-critic architecture.**

- The environment is modelled as a semi-Markov decision process (SMDP): state set S, action set A (primitive and abstract), transition function, reward function.
- The actor maintains a top-level policy π(s) and option-specific policies π_o(s) — weighted state-to-action mappings. The critic maintains a top-level value function V(s) and option-specific value functions V_o(s).
- Learning proceeds via temporal-difference prediction errors (δ): for primitive actions, δ is the one-step TD error; for options, δ is computed at option termination as the difference between V at the terminal state (plus accumulated reward) and V at the initiation state.
- Pseudo-reward is issued at subgoal attainment, shaping option-specific policies independently of external reward.
- Key assumption: the agent can acquire a useful set of options either through evolution, statistical analysis of rewarded trajectories, graph-theoretic analysis of the state space, or intrinsic motivation mechanisms.

---

### Prevailing model of the system under study

The paper situates itself against two converging traditions. In neuroscience, the prevailing framework at the time was standard (flat) actor-critic RL, in which the dorsolateral striatum implements the actor (policy), the ventral striatum and mesolimbic dopamine implement the critic (value function and prediction error), and dopamine conveys one-step TD prediction errors. Prefrontal cortex was understood as housing task-set representations that guide temporally integrated, goal-directed behavior, but its formal relationship to the RL machinery was underspecified. In psychology, hierarchical structure in behavior was well-documented and theorised (e.g., in Soar, ACT-R, and connectionist schema models), but these accounts lacked a unified normative principle (reward maximization) and did not address how hierarchical structures are acquired through learning. The paper pushes against the implicit assumption that these traditions can proceed independently — it argues that neither standard RL alone nor psychological models of hierarchy alone are sufficient.

---

### What this paper contributes

By formalising HRL within an actor-critic framework, the paper provides a concrete mapping from computational components to neural structures that was previously missing. Specifically:

- It proposes for the first time that DLPFC houses option representations (task sets as temporally abstract policies, not merely transient working-memory buffers), that DLS implements option-specific policies gated by frontal context, and that OFC computes option-specific value functions with an extended temporal scope — going beyond the existing actor-critic mapping.
- It introduces the option discovery problem as a central organising question for cognitive and developmental neuroscience, connecting it to intrinsic motivation, statistical learning, and social learning.
- It shows that negative transfer is a natural prediction of HRL, providing a formal account of why prior procedural knowledge can hinder new learning.
- It identifies specific empirical predictions absent from prior theory: phasic DA at subtask boundaries scaling with option-level prediction errors; neural correlates of pseudo-reward at subgoal attainment; sustained OFC activity encoding option-level value predictions.

---

### Brain regions & systems

- **Dorsolateral prefrontal cortex (DLPFC)** — proposed locus of option representations (task sets as temporally abstract policies) and working-memory maintenance of the currently controlling option.
- **Dorsolateral striatum (DLS)** — proposed substrate of option-specific action strengths (policies); integrates frontal option-context signals with sensory state to select actions; also implicated in option initiation/termination via boundary-aligned phasic activity.
- **Ventral striatum (VS)** — associated with top-level state-value function (critic), as in standard actor-critic accounts.
- **Mesolimbic dopamine system / midbrain dopaminergic neurons** — proposed carrier of TD prediction errors at both the primitive-action and option level; also responds to novel stimuli, consistent with intrinsic motivation mechanisms.
- **Orbitofrontal cortex (OFC)** — proposed locus of option-specific value functions; receives input from DLPFC (option identity) and projects to VS; OFC neurons show sustained reward-predictive activity and context-sensitive value representations consistent with option-specific valuation.
- **Pre-SMA, SMA, premotor cortex (PMC)** — mentioned as additional frontal regions potentially carrying task-set / action-sequence representations and projecting to DLS.

---

### Mechanistic insight

The paper does not meet the full bar: it proposes an HRL algorithm and provides a plausible mapping to neural structures supported by citations to existing neurophysiology, but it does not itself collect neural data, and it does not pit the HRL algorithm against alternatives using measured neural activity. The proposed links between, e.g., OFC sustained activity and option-specific value functions, or phasic dopaminergic activity at subtask boundaries and option-level prediction errors, remain hypotheses grounded in indirect evidence from the literature rather than direct tests. The paper's contribution is at the computational and algorithmic levels of Marr's hierarchy; the implementational level is addressed only speculatively.

---

### Limitations & open questions

- The options framework is cast in a model-free (cached value) mode; model-based HRL with option models is discussed only briefly and its neural correlates are not worked out.
- Strict hierarchical compositionality assumed by HRL is acknowledged to be at odds with context-sensitive and overlapping subtask structure in naturalistic human behavior.
- The option discovery problem is surveyed but not solved: how the brain actually identifies useful subgoal states through experience is left as a central open question.
- Empirical predictions (phasic DA at subtask boundaries; pseudo-reward signals; DLPFC option coding in hierarchical tasks) are explicitly flagged as untested at the time of writing.
- Differences between HRL implementations (options, MAXQ, HAM) lead to divergent fine-grained predictions (e.g., whether pseudo-reward is used, how value functions are decomposed), complicating experimental tests.
- The relationship between the HRL framework and models of routine sequential action (e.g., Botvinick & Plaut, 2004 connectionist model) is noted as an open challenge.

---

### Connections & keywords

**Key citations:**
- Sutton, Precup, & Singh (1999) — options framework
- Barto & Mahadevan (2003) — review of HRL
- Dietterich (2000) — MAXQ framework
- Parr & Russell (1998) — HAM framework
- Daw, Niv, & Dayan (2005) — model-free vs. model-based RL and dual-mode action control
- Schultz, Dayan, & Montague (1997) — dopamine and TD learning
- O'Reilly & Frank (2006) — frontostriatal RL and working memory
- Miller & Cohen (2001) — guided activation theory of PFC
- Montague, Dayan, & Sejnowski (1996) — dopamine as prediction error

**Named models or frameworks:**
- Options framework (Sutton et al., 1999)
- Actor-critic architecture
- Hierarchical reinforcement learning (HRL)
- MAXQ (Dietterich, 2000)
- HAM (Parr & Russell, 1998)
- Semi-Markov decision process (SMDP)
- ACT-R (Anderson, 2004)
- Soar (Laird, Lehman, Rosenbloom)
- Guided activation theory (Miller & Cohen, 2001)
- Four-rooms task (Sutton et al., 1999)

**Brain regions:**
- Dorsolateral prefrontal cortex (DLPFC)
- Dorsolateral striatum (DLS)
- Ventral striatum (VS)
- Orbitofrontal cortex (OFC)
- Mesolimbic dopamine / midbrain dopaminergic neurons
- Pre-SMA, SMA, premotor cortex

**Keywords:**
- hierarchical reinforcement learning
- temporal abstraction
- options framework
- actor-critic architecture
- prefrontal cortex task-set representation
- option discovery / subgoal identification
- pseudo-reward
- temporal-difference prediction error
- semi-Markov decision process
- positive and negative transfer
- intrinsic motivation
- frontostriatal circuits

### Related wiki pages
- [[wiki/debates/goal_directed_vs_habitual_control_in_corticostriatal_reinforcement_learning|Goal-directed vs habitual control in corticostriatal reinforcement learning]]
- [[wiki/topics/hierarchical_planning_and_successor_representations_in_prefrontal_hippocampal_cognitive_control|Hierarchical planning and successor representations in prefrontal–hippocampal cognitive control]]
- [[wiki/topics/orbitofrontal_cortex_as_a_cognitive_map_of_task_state_for_model_based_reinforcement_learning|Orbitofrontal cortex as a cognitive map of task state for model-based reinforcement learning]]
