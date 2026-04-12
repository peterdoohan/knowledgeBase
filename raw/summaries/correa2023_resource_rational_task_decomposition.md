---
source_file: "correa2023_resource_rational_task_decomposition.md"
paper_id: "correa2023_resource_rational_task_decomposition"
title: "Humans decompose tasks by trading off utility and computational cost"
authors: "Carlos G. Correa, Mark K. Ho, Frederick Callaway, Nathaniel D. Daw, Thomas L. Griffiths"
year: 2023
journal: "Unknown (preprint or journal \u2014 publication venue not stated in source text)"
paper_type: "computational"
contribution_type: "theoretical"
species: ["human"]
methods: ["computational_modeling"]
frameworks: ["reinforcement_learning", "bayesian_inference"]
keywords: ["humans", "decompose", "tasks", "trading", "off", "utility", "computational", "cost"]
key_citations: ["solway2014_optimal_behavioral_hierarchy", "tomov2020_hierarchical_planning_representation", "botvinick2009_hierarchically_organized_behavior", "stachenfeld2017_hippocampus_predictive_map"]
---

### One-line summary

People decompose tasks into subgoals in a way that trades off task performance against the computational cost of planning, a principle formalised as resource-rational task decomposition (RRTD) and validated against human subgoal choices in graph navigation.

---

### Background & motivation

Hierarchical task decomposition — breaking a goal into subgoals — is central to human intelligence, yet existing accounts treat subgoal *use* and subgoal *creation* largely in isolation. Prior normative models frame decomposition as structure inference (inferring a generative model of the environment or compressing optimal behaviour), without directly incorporating planning costs. This paper bridges the gap by developing an integrated, resource-rational framework in which the choice of subgoals is driven by the computational efficiency of the planning algorithms that operate over them.

---

### Methods

- **Framework**: Three nested levels of optimisation are formalised: (1) action-level planning (concrete actions to reach a subgoal), (2) subtask-level planning (choosing sequences of subgoals), and (3) task decomposition (selecting which states to designate as subgoals). The value of a decomposition integrates task reward and cumulative expected planning run-time.
- **Planning algorithms considered**: Random Walk (RW), Depth-First Search (DFS), Iterative-Deepening DFS (IDDFS), and Breadth-First Search (BFS), yielding model variants RRTD-RW, RRTD-IDDFS, and RRTD-BFS.
- **Large-scale simulation**: RRTD model predictions compared against four existing accounts (Solway et al. 2014, Tomov et al. 2020, QCut, Degree Centrality, Betweenness Centrality) on all 11,117 simple, undirected, connected eight-node graphs.
- **Behavioural experiment** (pre-registered, N = 806, Prolific):
  - Participants navigated 30 randomly sampled eight-node graphs (30 long trials + 30 adaptive filler trials).
  - Subgoal probes: implicit subgoal probe, explicit subgoal probe, and a teleportation question.
  - Analysis: hierarchical multinomial regression predicting probe choice; two-stage choice model predicting navigation among optimal paths. AIC used for model comparison.

---

### Key findings

- RRTD-IDDFS produces subgoal predictions highly correlated with Betweenness Centrality (r = 0.95 across 11,117 graphs), while RRTD-RW correlates strongly with Degree Centrality (r = 0.98); a formal spectral proof links RRTD-RW to QCut for regular graphs.
- Among normative models, RRTD-IDDFS best explains human subgoal probe choices by AIC for both the explicit probe (χ²(2) = 5183.1, p < .001) and implicit probe (χ²(2) = 3941.2, p < .001).
- Among heuristics, Betweenness Centrality best predicts human responses across all three probes, outperforming RRTD-IDDFS overall, suggesting participants may use betweenness as a tractable approximation to resource-rational decomposition.
- Subgoal probe responses are internally valid: explicit and implicit probes are highly correlated (r = 0.98), and probe choices predict actual navigation path choices among optimal routes (explicit: 75.3% vs. 70.5% baseline, p < .001; implicit: 70.7% vs. 65.2%, p < .001).
- The two-stage model of navigation choice reproduces the same ordering: RRTD-IDDFS best among normative accounts, Betweenness Centrality best overall.
- Participants improved significantly across training: optimal navigation solutions increased from 70% to 79%, and solution time decreased from 10.30s to 7.60s.

---

### Computational framework

**Resource-rational analysis** applied to hierarchical planning. The framework models task decomposition as a joint optimisation over task reward (negative path length) and computational cost (expected run-time of the action-level search algorithm). The key quantities are:

- *Action-level utility*: expected reward minus expected run-time when planning from state s to subgoal z under algorithm Alg.
- *Subtask-level value*: defined recursively via Bellman equations over sequences of subgoals.
- *Task decomposition value*: the subtask-level utility of a candidate subgoal set, averaged over the task distribution.

The framework makes the choice of planning algorithm explicit as a parameter, yielding different predictions for RW, BFS, and IDDFS. A key assumption is that people select a fixed set of subgoals that generalises across tasks in an environment, rather than recomputing subgoals per task.

---

### Prevailing model of the system under study

Prior to this work, the dominant normative accounts of subgoal discovery framed the problem as **structure inference**: people are modelled as inferring a hierarchical generative model of the environment (Collins & Frank 2013; Tomov et al. 2020) or as compressing optimal behavioural sequences via minimum description length (Solway et al. 2014). Graph-theoretic heuristics such as betweenness centrality and QCut were treated as plausible but theoretically unmotivated approximations. The unifying gap acknowledged by the field is that these accounts do not directly connect the selection of subgoals to the computational efficiency gains that subgoals are supposed to provide during planning.

---

### What this paper contributes

The paper provides the first normative framework that directly incorporates planning costs — not just task structure or behavioural compression — into the criterion for choosing subgoals. Key advances:

1. **Theoretical unification**: RRTD gives a formal rationale for betweenness centrality and QCut as efficient heuristic approximations to a resource-rational objective, rather than ad hoc graph-theoretic choices.
2. **Empirical differentiation**: Using 11,117 graphs and 806 participants — a substantially larger and more diverse stimulus set than any prior study — RRTD-IDDFS is shown to outperform structure-inference accounts (Solway et al. 2014, Tomov et al. 2020) in predicting human subgoal choices.
3. **Process-level pointer**: The dominance of Betweenness Centrality over all normative models suggests that people approximate resource-rational task decomposition using a tractable graph-structural heuristic, providing a candidate process-level account.

---

### Brain regions & systems

Not applicable. The paper is a purely computational and behavioural study with no neuroimaging, recording, or anatomical focus. The level of analysis is algorithmic/computational: the paper characterises what problem people solve when decomposing tasks and what algorithm(s) they appear to use, without addressing neural implementation.

---

### Mechanistic insight

The paper does not meet the bar for this section. It proposes a computational algorithm (RRTD) and fits it to behaviour, but provides no neural data of any kind (no imaging, no recordings, no lesion or pharmacology studies) linking the model's specific variables to measured neural activity. The paper is a behavioural-computational study only.

---

### Limitations & open questions

- **Interpretability**: RRTD is normative but not easily interpretable; the qualitative rules humans use to approximate it remain unclear.
- **Self-report validity gap**: Subgoal probes and navigation behaviour were measured minutes apart; stronger concurrent measurement methods are needed.
- **Tractable approximation**: Betweenness centrality itself is computationally expensive (requires finding optimal paths between all state pairs); identifying even more efficient approximations is an open question.
- **Graph structure scope**: The study used small (8-node) graphs; generalisability to larger, real-world state spaces is untested.
- **Single subgoal assumption**: The framework was primarily evaluated with single-subgoal decompositions; richer hierarchical structures were not tested empirically.
- **Year uncertainty**: The source text does not state the publication venue or year explicitly; Callaway et al. (2022) is the latest dated citation, placing the paper no earlier than 2022.

---

### Connections & keywords

**Key citations**:
- Solway et al. (2014) — optimal behavioural hierarchy via minimum description length
- Tomov et al. (2020) — task decomposition as Bayesian inference over hierarchical graphs
- Simsek et al. (2005) — QCut / local graph partitioning for subgoal discovery
- Simsek & Barto (2009) — betweenness centrality for skill characterisation
- Lieder & Griffiths (2020) — resource-rational analysis framework
- Botvinick et al. (2009) — hierarchically organised behaviour and RL
- Stachenfeld et al. (2017) — hippocampus as a predictive map
- Callaway et al. (2022) — rational use of cognitive resources in planning

**Named models or frameworks**:
- Resource-Rational Task Decomposition (RRTD)
- Resource-rational analysis
- QCut (Simsek et al. 2005)
- Betweenness Centrality (Simsek & Barto 2009)
- Solway et al. (2014) MDL hierarchy model
- Tomov et al. (2020) Bayesian hierarchical graph model
- Iterative-Deepening Depth-First Search (IDDFS)
- Breadth-First Search (BFS), Random Walk (RW)

**Brain regions**: Not applicable.

**Keywords**: resource-rational analysis, hierarchical planning, task decomposition, subgoal discovery, betweenness centrality, graph navigation, planning cost, computational efficiency, bounded rationality, heuristic approximation, spectral graph theory, multinomial regression
