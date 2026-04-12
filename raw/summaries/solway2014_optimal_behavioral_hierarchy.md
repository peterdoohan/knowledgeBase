---
source_file: solway2014_optimal_behavioral_hierarchy.md
paper_id: solway2014_optimal_behavioral_hierarchy
title: "Optimal Behavioral Hierarchy"
authors:
  - "Alec Solway"
  - "Carlos Diuk"
  - "Natalia Córdova"
  - "Debbie Yee"
  - "Andrew G. Barto"
  - "Yael Niv"
  - "Matthew M. Botvinick"
year: 2014
journal: "PLoS Computational Biology"
paper_type: computational
contribution_type: theoretical
species:
  - human
brain_regions:
  - striatum
frameworks:
  - reinforcement_learning
  - hierarchical_rl
keywords:
  - hierarchical_reinforcement_learning
  - behavioral_hierarchy
  - bayesian_model_selection
  - options_framework
  - subgoal_discovery
  - topological_bottleneck
  - community_detection
  - graph_decomposition
  - task_decomposition
  - planning
  - shortest_path_navigation
  - tower_of_hanoi
  - statistical_learning
  - representational_efficiency
  - learning_efficiency
  - optimal
  - behavioral
  - hierarchy
key_citations:
  - schapiro2013_event_representation_memory
  - sutton1999_temporal_abstraction_rl
---

### One-line summary

Human learners spontaneously discover optimal behavioral hierarchies that maximize learning efficiency, as formalized by a Bayesian model selection framework that identifies topological bottlenecks as optimal subgoal locations.

---

### Background & motivation

Behavior exhibits hierarchical organization, with actions grouped into subtasks that combine into extended goal-directed activities. While hierarchy offers computational benefits (efficient representation and faster learning/planning), not all hierarchies are equally beneficial. The specific way actions are organized into a hierarchy critically determines its utility. This paper addresses the fundamental question of what makes a behavioral hierarchy optimal and whether humans spontaneously discover such optimal hierarchies.

---

### Methods

**Computational Framework:**
- Applied Bayesian model selection to compare hierarchical reinforcement learning (HRL) agents equipped with different action hierarchies
- Focused on episodic Markov decision problems (MDPs) with discrete states, deterministic transitions, and reversible actions
- Represented domains as undirected graphs with vertices as states and edges as feasible transitions
- Task ensemble comprised all shortest-path problems within each graph
- Used options framework (Sutton et al., 1999) where options are temporally extended actions with initiation sets, termination conditions, and policies
- Graph decompositions defined regions; options created for transitions between regions via bottleneck states
- Model evidence computed as proportion of compatible policy parameterizations; optimal hierarchy maximizes model evidence

**Behavioral Experiments:**
- **Experiment 1 (n=40):** Participants learned a 10-location graph with a central bottleneck through adjacency training, then selected optimal bus-stop locations before making deliveries. Predicted bottleneck locations would be preferred.
- **Experiment 2 (n=10):** Participants navigated a 19-location bottleneck graph. Interleaved path identification trials tested whether participants hierarchically planned by selecting bottleneck locations first when identifying shortest paths.
- **Experiment 3 (n=21):** Same graph as Experiment 2. Participants answered Yes/No queries about whether a location lay on shortest paths between start and goal. Measured response times for bottleneck vs. non-bottleneck queries.
- **Experiment 4 (n=35):** Tower of Hanoi task. Optimal decomposition creates three regions based on largest disk position. Tested whether participants preferred solution paths crossing fewer region boundaries (assuming hierarchical planning has costs).

---

### Key findings

**Computational Results:**
- The optimal hierarchy (maximizing model evidence) minimizes the geometric mean number of trial-and-error attempts needed to discover optimal policies for any task or subtask
- The optimal hierarchy also minimizes the expected number of information-theoretic bits needed to encode hierarchical policies consistent with target behaviors (shortest code length under Shannon coding)
- Optimal hierarchies correspond to partitions at topological bottlenecks (community structure), carving the state-space at narrow segments bridging densely interconnected clusters
- The rooms domain (Figure 1) and Tower of Hanoi (Figure 2F) both show optimal decompositions at natural bottlenecks

**Behavioral Results:**
- **Experiment 1:** After adjusting for chance, the two bottleneck locations were chosen as first-choice bus-stop locations 4.4 times as often as non-bottleneck locations (χ²(1, N=40) = 35.16, p < 0.001). Among participants who could perfectly draw the underlying graph, 94% chose a bottleneck location first (χ²(1, N=17) = 58.37, p < 0.001).
- **Experiment 2:** When asked to identify all locations on shortest paths, participants selected the bottleneck location first on 84% of correct responses (Monte Carlo test, p < 0.007). When asked to identify any single location on the path, participants selected the bottleneck on 74% of correct responses (Monte Carlo test, p < 0.01).
- **Experiment 3:** Correct response times were faster when the probe location lay at the bottleneck between subregions than when it lay elsewhere (F(1, 1474) = 6.838, p < 0.01), consistent with hierarchical planning that first considers region transitions.
- **Experiment 4:** When presented with two equally short solution paths (one crossing one region boundary, the other crossing two), participants chose the single-boundary path in 72% of cases (right-tail sign test, p < 0.05). Seventeen subjects showed the single-boundary preference, while only seven showed the opposite pattern (one-tailed t-test, p < 0.05).

---

### Computational framework

**Hierarchical Reinforcement Learning (options framework):** The paper adopts the options framework (Sutton et al., 1999) where options are temporally extended actions consisting of initiation sets, termination functions, and policies. The hierarchy has two levels: root-level policies can invoke options or primitive actions; option policies only invoke primitive actions.

**Bayesian Model Selection:** The core formalism reframes hierarchy evaluation as Bayesian model selection. Each candidate hierarchy (graph decomposition) induces a probability distribution over behaviors. The model evidence (marginal likelihood) quantifies how well each hierarchy explains the target data (optimal behaviors for all shortest-path tasks). The optimal hierarchy maximizes model evidence.

**Key insight:** The optimal hierarchy places the greatest probability mass on target behaviors, which mathematically entails:
1. Minimizing expected trial-and-error attempts to discover optimal policies (learning efficiency)
2. Minimizing expected code length for encoding hierarchical policies (representational efficiency)

---

### Prevailing model of the system under study

Prior to this work, the field understood that hierarchical organization offers computational benefits for behavior: more efficient representations and faster learning/planning. Hierarchical reinforcement learning (HRL) provided frameworks for representing and learning with hierarchical structure (options, MAXQ, etc.). Previous work had also proposed heuristic methods for discovering useful subgoals, including betweenness centrality (Simsek & Barto, 2008) and information-theoretic approaches (van Dijk & Polani, 2011). However, these approaches lacked a normative foundation—there was no formal account of what makes one hierarchy objectively better than another. The relationship between heuristic methods (like bottleneck detection) and optimal solutions was unclear.

---

### What this paper contributes

This paper provides the first normative framework for determining optimal behavioral hierarchies. By formalizing hierarchy evaluation as Bayesian model selection, the authors show that:
1. The optimal hierarchy maximizes model evidence, which provably minimizes both learning time (expected trial-and-error attempts) and representational cost (expected code length)
2. Optimal hierarchies correspond to partitions at topological bottlenecks (community structure), providing formal justification for previous heuristic approaches
3. The framework applies to arbitrary tasks, not just spatial navigation

The four behavioral experiments demonstrate that human learners spontaneously discover these optimal hierarchies without explicit instruction, suggesting that humans have built-in mechanisms for identifying task-relevant subgoal structures. This raises the question of what learning procedure humans actually use to approximate Bayesian optimality—a question the paper identifies as important for future research (suggesting statistical learning/predictive coding as one possibility).

---

### Brain regions & systems

Not applicable. This paper focuses on behavioral and computational analysis without direct neural measurements. The work has implications for understanding prefrontal function and basal ganglia (referenced in discussion of hierarchical behavior and previous work), but no specific brain regions are investigated empirically.

---

### Mechanistic insight

The paper does not meet the high bar for mechanistic insight as defined in the instructions. While it proposes a formal algorithm (Bayesian model selection for evaluating hierarchies) and demonstrates behavioral data consistent with hierarchical planning, it does not provide neural data that specifically links the model's variables to measured neural activity. The paper is purely behavioral and computational.

The computational framework (Bayesian model selection applied to hierarchical RL) could in principle guide future neuroscience research, but the current paper does not test neural predictions. The framework suggests that the brain might represent behavioral hierarchies that maximize model evidence, but this is not directly tested.

---

### Limitations & open questions

1. **Implementation unknown**: The paper explicitly notes that humans do not literally compute Bayesian model evidence. The actual learning procedure humans use to approximate optimal hierarchy discovery remains unknown. The authors suggest statistical learning/predictive coding as a possible mechanism but do not test this.

2. **Limited hierarchy depth**: The implementation was restricted to two-level hierarchies (options only call primitive actions, not other options) for computational tractability. The theoretical framework generalizes to deeper hierarchies, but this was not empirically tested.

3. **Deterministic, reversible actions**: The analysis assumed deterministic state transitions and reversible actions. Real-world behavior often involves stochastic dynamics and irreversible actions.

4. **Shortest-path tasks only**: The behavioral experiments focused on shortest-path navigation tasks. While the framework applies to arbitrary tasks, generalization to other task types was not demonstrated.

5. **No neural data**: The paper is purely behavioral and computational. Neural mechanisms of hierarchy discovery and representation are not investigated.

6. **Small sample sizes**: Experiments 2-4 had relatively small samples (n=10, 21, 35).

---

### Connections & keywords

**Key citations:**
- Sutton, Precup & Singh (1999) - options framework for hierarchical RL
- Simsek & Barto (2008) - betweenness centrality for subgoal discovery
- van Dijk & Polani (2011) - information-theoretic approach to subgoals
- Schapiro et al. (2013) - related work on temporal community structure
- Botvinick & Weinstein (2014) - hierarchical models of behavior
- Sutton & Barto (1998) - reinforcement learning textbook
- Brandes et al. (2008) - community detection via modularity clustering

**Named models or frameworks:**
- Hierarchical Reinforcement Learning (HRL)
- Options framework (Sutton et al., 1999)
- Bayesian model selection
- Markov Decision Processes (MDPs)
- Interaction graph / betweenness centrality (Simsek & Barto, 2008)
- Community detection in networks
- Tower of Hanoi task paradigm

**Brain regions:**
- Not applicable (no neural data)

**Keywords:**
- hierarchical reinforcement learning
- behavioral hierarchy
- Bayesian model selection
- options framework
- subgoal discovery
- topological bottleneck
- community detection
- graph decomposition
- task decomposition
- planning
- shortest path navigation
- Tower of Hanoi
- statistical learning
- representational efficiency
- learning efficiency
