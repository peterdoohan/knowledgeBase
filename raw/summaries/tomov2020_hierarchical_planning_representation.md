---
source_file: tomov2020_hierarchical_planning_representation.md
title: Discovery of hierarchical representations for efficient planning
authors: Momchil S. Tomov, Samyukta Yagati, Agni Kumar, Wanqian Yang, Samuel J. Gershman
year: 2020
journal: PLOS Computational Biology
paper_type: computational
contribution_type: theoretical
---

### One-line summary

A Bayesian model of hierarchy discovery explains how humans discover hierarchical state abstractions from environment topology, task distributions, and rewards to enable efficient planning.

### Background & motivation

Planning in complex environments requires managing working memory constraints and computational resources. Humans organize environments into hierarchical clusters of states that support efficient planning, but the computational mechanisms underlying discovery of such hierarchical representations remain poorly understood. This paper proposes a normative Bayesian framework for how agents infer hidden hierarchical structure from observations.

### Methods

- **Computational model**: Bayesian generative model of hierarchical environments with Chinese Restaurant Process prior over cluster assignments, graph density parameters for within-cluster and between-cluster connectivity, and extensions for task distributions and reward distributions
- **Inference**: Metropolis-within-Gibbs MCMC sampling to approximate posterior over hierarchies P(H|D)
- **Planning algorithm**: Hierarchical Breadth-First Search (HBFS) that first plans at high-level between clusters, then within clusters
- **Simulations**: Five simulations replicating published behavioral effects from Schapiro et al. (2013), Solway et al. (2014), and Lynn et al. (2018)
- **Experiments**: Eight behavioral experiments (N=87-386 per experiment) testing novel predictions about task distributions, rewards, and learning dynamics using virtual navigation tasks on Amazon MTurk

### Key findings

- **Simulation 1**: Model replicates detection of community boundary transitions (bottleneck detection) as in Schapiro et al. (2013)
- **Simulation 2**: Model selects bottleneck states as optimal subgoals as in Solway et al. (2014)
- **Simulation 3**: Model plans hierarchically by considering high-level transitions first as in Solway et al. (2014)
- **Simulation 4**: Model prefers paths crossing fewer community boundaries as in Solway et al. (2014) Towers of Hanoi experiment
- **Simulation 5**: Model shows slower reaction times to longer cross-cluster violations as in Lynn et al. (2018)
- **Experiment 1**: Task distributions alone (without topological structure) induce hierarchical clustering that influences planning (58/87 participants preferred route with fewer cluster boundaries, p=0.003)
- **Experiment 2**: Task-induced clusters can lead to suboptimal planning (53/78 participants chose suboptimal path when "bad" clusters were induced, p=0.002)
- **Experiment 3**: Learning dynamics show progressive hierarchy discovery with uncertainty reduction and mode shifts in posterior (probe trial preferences changed significantly across training stages, p=0.05 and p=0.005)
- **Experiment 4**: Task effects persist with full graph visibility (51/77 participants showed cluster bias, p=0.0014)
- **Experiment 5**: Suboptimal planning from task distributions occurs even with full visibility (bad clusters condition significantly worse than control, p=0.002-0.006)
- **Experiment 6**: Rewards generalize within clusters (24/32 participants preferred state in same cluster as rewarded state, p=0.007)
- **Experiment 7**: Reward boundaries induce clusters that influence planning (102/174 participants preferred path with fewer reward cluster boundaries, p=0.03)

### Computational framework

**Bayesian structure learning for hierarchy discovery**: The model treats hierarchy discovery as Bayesian inference over a generative model of environments with hidden hierarchical structure. The generative model uses a Chinese Restaurant Process (CRP) prior over cluster assignments, with separate graph density parameters for within-cluster edges (p), between-cluster edges (q), and high-level graph connectivity (p0). Extensions incorporate task distributions (preferring to cluster start-goal pairs) and reward distributions (clustering states with similar rewards). The posterior P(H|D) is approximated via MCMC sampling.

**Hierarchical planning (HBFS)**: Planning uses Hierarchical Breadth-First Search, which first plans at the high level between clusters, then plans within the current cluster to reach the next high-level cluster. This reduces complexity from O(N) to O(√N) for 2-level hierarchies.

### Prevailing model of the system under study

Prior work established that humans and animals organize behavior hierarchically, using action chunks (temporally extended action sequences) after extensive training. Research showed people spontaneously discover hierarchical structure based on environment topology, with neural correlates of high-level states. However, the computational mechanisms underlying discovery of hierarchical state representations (state chunks) remained poorly understood. Existing models included recurrent neural networks detecting community structure, formal optimality analyses requiring knowledge of all possible tasks, and various option discovery methods in hierarchical RL, but none could account for the full range of effects demonstrated in this paper (see Table 2 of paper).

### What this paper contributes

This paper provides a unified Bayesian account of hierarchy discovery that:
1. Explains how agents infer hierarchical state abstractions from environment structure, task distributions, AND reward distributions
2. Accounts for previously reported topological effects (bottleneck detection, community boundary parsing, hierarchical planning preferences)
3. Makes novel predictions about task-induced and reward-induced clustering that are validated in 8 new experiments
4. Explains learning dynamics through uncertainty reduction and posterior mode shifts
5. Unifies structure learning and hierarchical planning under a single normative framework
6. Provides a solution to the option discovery problem in hierarchical RL

The model demonstrates that hierarchy discovery is a form of Bayesian structure learning in which state chunks are treated as latent causes generating observations (transitions, tasks, rewards), with important implications for understanding how the brain builds internal models for adaptive decision-making.

### Brain regions & systems

Not applicable (computational-level theory). The paper discusses potential neural implementations in the Discussion section, suggesting relevance to:
- Hippocampus (long-term storage of relational information/graph structure)
- Working memory systems (for online planning)
- Hierarchical reinforcement learning circuits (cortico-striatal loops)
- Prefrontal cortex (planning and goal-directed behavior)

### Mechanistic insight

The paper provides a computational-level account (per Marr) of hierarchy discovery, with algorithmic-level suggestions. The framework posits:

**Computational level**: The brain solves the problem of efficient planning under resource constraints by inferring latent hierarchical structure in the environment. The computational goal is to discover state abstractions that minimize planning complexity while maintaining path quality.

**Algorithmic level**: The paper suggests MCMC sampling (Metropolis-within-Gibbs) as a plausible algorithmic implementation for hierarchy inference, consistent with previous work casting human probabilistic inference as Monte Carlo sampling. For planning, the HBFS algorithm provides a deterministic, efficient alternative to sampling-based planners. The paper also discusses how local updates could approximate the posterior efficiently.

**Implementational level**: Not explicitly addressed, but the Discussion suggests the hippocampus may store the graph structure, working memory systems support online planning, and cortico-striatal circuits may implement hierarchical RL. The paper relates the model to neural signatures of hierarchical RL and high-level state representations found in prior fMRI studies.

The paper does not provide direct neural data supporting the specific algorithm, but positions the framework as consistent with existing neural findings and amenable to future neuroscientific investigation.

### Limitations & open questions

- Action chunking (temporal abstraction) not addressed; model only addresses state chunking (state abstraction)
- Hard restriction that each node belongs to single cluster; could be relaxed with soft clustering
- Computational-level theory only; algorithmic and implementational details need further development
- Assumes perfect (lossless) memory for observations; memory constraints not modeled
- Tabular representations don't scale to real-world environments; extension to deep hierarchies and modular templates needed
- Model assumes deterministic, undirected, unweighted graphs; extensions to stochastic, directed, weighted graphs needed
- No direct neural data validating the specific Bayesian inference process

### Connections & keywords

**Key citations**: Schapiro et al. (2013), Solway et al. (2014), Lynn et al. (2018), Botvinick et al. (2009), Sutton & Barto (2018), Gershman et al. (2015), Fernández & González (2013)

**Named models or frameworks**: Bayesian structure learning, hierarchical reinforcement learning (HRL), options framework, model-based RL, model-free RL, Chinese Restaurant Process (CRP), Markov Decision Process (MDP), Breadth-First Search (BFS), Hierarchical BFS (HBFS), successor representation, Dyna architecture

**Brain regions**: Hippocampus, prefrontal cortex, striatum (dorsolateral, dorsomedial), cortico-striatal loops

**Keywords**: hierarchical planning, state abstraction, structure learning, Bayesian inference, hierarchy discovery, reinforcement learning, chunking, community structure, bottleneck states, task distribution, reward generalization, Markov chain Monte Carlo, graph theory, option discovery, behavioral hierarchy, working memory, computational efficiency
