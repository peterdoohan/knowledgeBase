---
source_file: botvinick2009_hierarchically_organized_behavior.md
title: "Hierarchically organized behavior and its neural foundations: A reinforcement-learning perspective"
authors: Matthew M. Botvinick, Yael Niv, Andrew C. Barto
year: 2009
journal: Cognition
paper_type: computational
contribution_type: theoretical
---

### One-line summary

Hierarchical reinforcement learning (HRL) — specifically the options framework embedded in an actor-critic architecture — provides a computationally principled account of hierarchically structured behavior and maps naturally onto prefrontal and striatal neural circuits.

---

### Background & motivation

Standard reinforcement learning (RL) faces a scaling problem: exploration and learning become intractable as the number of states and actions grows, limiting applicability to realistic behavioral domains. The solution explored in machine learning — temporal abstraction, grouping sequences of primitive actions into reusable higher-level options — resonates with longstanding ideas about hierarchical action organization in psychology and neuroscience. However, no prior work had systematically mapped HRL algorithms onto neural structures using the actor-critic framework that already has established neuroanatomical correlates. This paper fills that gap by formalising HRL within an actor-critic model and tracing its implications for both behavioral theory and functional neuroanatomy.

---

### Methods

This is a computational/theoretical paper; there is no new empirical data collection. The approach involves:

- Exposition of the **options framework** (Sutton et al., 1999) as the canonical HRL implementation, supplemented by discussion of HAM and MAXQ alternatives.
- Implementation of the options framework within an **actor-critic architecture**, making explicit the added computational components (option-specific policies, option-specific value functions, extended prediction errors).
- **Simulation** of a toy four-rooms navigation task to illustrate: (a) learning of option-specific policies via pseudo-reward; (b) faster learning with options versus primitive actions only; (c) positive and negative transfer effects when options are (mis)aligned with task structure.
- **Mapping** of the extended actor-critic components onto known functional neuroanatomy via review of existing neurophysiological and imaging literature.
- **Comparative review** of HRL relative to psychological theories of hierarchical action control (ACT-R, Soar, task-set accounts, chunking models).

---

### Key findings

- Temporally abstract actions (options) reduce the effective size of the exploration search tree and reduce the number of decision points at which learning is required, jointly accelerating acquisition of reward-maximising policies.
- In the four-rooms simulation, agents equipped with doorway options reached the goal state faster than agents using only primitive actions, illustrating the scaling benefit of HRL.
- Options can cause **negative transfer**: when available options are poorly matched to a task (e.g., window-subgoal options in a door-navigated maze), learning is slowed relative to the primitive-action baseline.
- The actor extensions required by HRL — representations of active options and option-specific policies — map onto **dorsolateral prefrontal cortex** (DLPFC; task-set representations) and **dorsolateral striatum** (DLS; option-specific action strengths and policy selection).
- The critic extensions required by HRL — option-specific value functions and temporally extended prediction errors (SMDP framing) — map onto **orbitofrontal cortex** (OFC; context-dependent value representations, sustained reward-predictive activity).
- Phasic dopaminergic activity at subtask boundaries, scaling with option-level prediction errors, is a novel, testable prediction of the framework.
- The option discovery problem — how useful options are acquired — has parallels in psychology: trajectory-based bottleneck detection resonates with human sensitivity to sequential structure; intrinsic motivation approaches parallel developmental circular reactions and novelty-seeking; social transmission of subgoals parallels imitation and instruction.

---

### Computational framework

**Hierarchical reinforcement learning (HRL) — options framework within an actor-critic architecture.**

- The basic RL problem is a Markov decision process (MDP): states S, actions A, transition function T, reward function R; the agent learns a policy π maximising discounted cumulative reward.
- The **actor-critic** architecture divides the agent into an actor (maintains action strengths π(s), selects actions) and a critic (maintains state-value function V(s), computes temporal-difference prediction errors δ).
- HRL extends this by introducing **options** o, each defined by an initiation set, a termination function, and an option-specific policy πo(s). Options are temporally abstract actions — upon selection, they execute their policy until reaching a termination state.
- The critic is extended to maintain **option-specific value functions** Vo(s), which predict cumulative reward (including pseudo-reward) under option o's policy.
- **Pseudo-reward** is delivered at subgoal attainment, shaping option-specific policies independently of external reward.
- Prediction errors for options are computed over the full duration of option execution (semi-Markov decision process, SMDP), comparing the value at option initiation against cumulated reward plus value at termination.
- Key assumptions: options can be hierarchically nested; the agent tracks the currently controlling option; learning rates and discount factors apply both at the primitive and option level.

---

### Prevailing model of the system under study

The paper's introduction frames the baseline understanding as follows: RL (especially temporal-difference learning in actor-critic architectures) had already been successfully mapped onto mesolimbic dopamine, basal ganglia, and prefrontal cortex. The prevailing view held that dopamine signals reward prediction errors, the ventral striatum serves as critic, the dorsolateral striatum as actor, and prefrontal cortex supports goal-directed and working-memory functions. Behaviorally, hierarchy in action control was recognised and linked broadly to prefrontal function, but lacked a unifying computational framework that could specify how hierarchical structure is learned, what exactly is represented, and how the system scales to complex tasks. Psychological accounts (ACT-R, Soar, task-set theories) addressed aspects of hierarchical organisation but did not ground them in reward-maximisation or temporal-difference learning.

---

### What this paper contributes

The paper extends the prevailing actor-critic/RL mapping to hierarchically structured behavior by specifying the additional computational machinery HRL requires and identifying plausible neural correlates for each component. Concretely:

- It demonstrates that the DLPFC can be re-interpreted not merely as a working-memory buffer but as the locus of **option representations** (task sets that persist, specify policies, and participate in hierarchical nesting).
- It proposes that the OFC computes **option-specific state values** and sustains reward predictions across temporally extended subtasks — a more specific functional hypothesis than prior accounts of OFC as a generic value region.
- It predicts phasic dopaminergic discharge at **subtask boundaries** (not only at task completion), a specific, testable departure from single-level RL accounts.
- It reframes the psychological problem of **skill acquisition and transfer** (positive and negative) as the option discovery problem, providing a normative account of when acquired routines help or hurt.
- It identifies the scaling problem as the key reason biological agents would benefit from HRL-like mechanisms, providing a functional justification for hierarchical prefrontal control that pure performance accounts lack.

---

### Brain regions & systems

- **Dorsolateral prefrontal cortex (DLPFC)** — proposed locus of option representations (task sets); maintains the identity of the currently active option and supports its persistence across time (working memory for abstract action policy); corresponds to Extension 1 of the HRL actor.
- **Dorsolateral striatum (DLS)** — proposed locus of option-specific action strengths (policies); integrates current option identity from frontal cortex with environmental state to select primitive actions or sub-options; corresponds to Extension 2.
- **Orbitofrontal cortex (OFC)** — proposed locus of option-specific state-value functions; represents reward value in a context- and option-dependent manner; sustains reward-predictive activity across temporally extended option execution; corresponds to Extensions 3 and 4 of the HRL critic.
- **Ventral striatum (VS) / mesolimbic dopamine system** — standard critic in actor-critic RL; compute and broadcast reward prediction errors; in HRL, also involved in option-level prediction errors at subtask boundaries.
- **Pre-supplementary motor area (pre-SMA) and premotor cortex (PMC)** — secondary loci of task-set and action-sequence representations; project to DLS to support option-specific policies.
- **Midbrain dopaminergic neurons (VTA/SNc)** — carry reward prediction errors to actor and critic; also respond to novel stimuli, linking novelty responses to intrinsic motivation for option discovery.

---

### Mechanistic insight

The paper does not present new neural data; it is a theoretical proposal. It therefore does not meet the high bar (both algorithm + neural data supporting that algorithm over alternatives).

The paper proposes a detailed HRL algorithm and offers an extensive neural mapping, but the proposed correspondences rest on existing neurophysiological and imaging findings that were not designed to test HRL specifically. For example, OFC neurons show context-sensitive value responses and sustained reward-predictive activity, which is *consistent* with option-specific value functions, but no study has directly measured option-level prediction errors in OFC or compared them against alternative computational accounts. Similarly, DLS activity varying with task context is cited, but this evidence does not isolate the option-specific policy mechanism from other accounts of context-dependent striatal coding.

---

### Limitations & open questions

- **Option discovery**: The paper identifies this as the central unresolved computational and behavioral problem — how does a learning agent acquire options that will be useful across future tasks? Multiple candidate mechanisms are discussed (trajectory analysis, graph partitioning, intrinsic motivation, social transmission) but no single account is endorsed or empirically validated.
- **Subgoal pseudo-reward**: Whether neural structures responsive to exogenous reward also respond specifically to subgoal attainment during hierarchical task performance remains untested.
- **Phasic DA at subtask boundaries**: The prediction of option-level prediction errors signalled by phasic dopamine at subtask junctures is explicit but not yet empirically confirmed.
- **Non-hierarchical structure**: Many naturalistic tasks exhibit shared/overlapping subtask structure and context-sensitive subtask execution that resist a strictly hierarchical account; the paper acknowledges this tension but does not resolve it within the HRL framework.
- **Model-based HRL**: The paper focuses on model-free (cached) HRL; the neural correlates of model-based HRL with option models remain underspecified.
- **Algorithm-level differences between HRL frameworks**: HAM, MAXQ, and options make divergent predictions (e.g., regarding pseudo-reward and value function decomposition); the correct mapping to biology is unclear.
- **Integration with capacity-limited processing**: HRL does not address working-memory capacity limits, attentional bottlenecks, or task-switching costs that psychological models like ACT-R and Soar treat centrally.

---

### Connections & keywords

**Key citations:**
- Sutton, Precup & Singh (1999) — options framework (foundational)
- Barto & Mahadevan (2003) — overview of HRL paradigms
- Parr & Russell (1998) — HAM framework
- Dietterich (2000) — MAXQ framework
- Schultz, Dayan & Montague (1997) — dopamine and TD learning
- Daw, Niv & Dayan (2005) — model-free vs. model-based RL and basal ganglia
- O'Reilly & Frank (2006) — DA and prefrontal working memory learning
- Miller & Cohen (2001) — guided activation theory of PFC
- Koechlin, Ody & Kouneiher (2003) — rostro-caudal hierarchy in frontal cortex
- Botvinick & Plaut (2004) — connectionist model of routine sequential action
- Singh, Barto & Chentanez (2005) — intrinsic motivation for option discovery

**Named models or frameworks:**
- Options framework (Sutton et al., 1999)
- Actor-critic architecture
- HAM (Hierarchies of Abstract Machines)
- MAXQ framework
- Semi-Markov decision process (SMDP)
- Guided activation theory (Miller & Cohen, 2001)
- ACT-R (Anderson, 2004)
- Soar (Lehman, Laird & Rosenbloom, 1996)

**Brain regions:**
- Dorsolateral prefrontal cortex (DLPFC)
- Orbitofrontal cortex (OFC)
- Dorsolateral striatum (DLS)
- Ventral striatum (VS)
- Pre-supplementary motor area (pre-SMA)
- Premotor cortex (PMC)
- Midbrain dopaminergic system (VTA/SNc)

**Keywords:**
- hierarchical reinforcement learning
- options framework
- temporal abstraction
- actor-critic architecture
- option discovery / subgoal identification
- pseudo-reward
- semi-Markov decision process
- prefrontal cortex task-set representations
- orbitofrontal cortex option-specific value
- dorsolateral striatum option-specific policy
- positive and negative transfer
- intrinsic motivation
