---
source_file: "wientjes2024_successor_representation.md"
paper_id: "wientjes2024_successor_representation"
title: "The successor representation subserves hierarchical abstraction for goal-directed behavior"
authors: "Sven Wientjes, Clay B. Holroyd"
year: 2024
journal: "PLOS Computational Biology"
paper_type: "empirical"
contribution_type: "empirical"
species: ["human"]
tasks: ["navigation_task"]
methods: ["computational_modeling", "behavioral_analysis"]
brain_regions: ["hippocampus", "prefrontal_cortex", "medial_prefrontal_cortex", "anterior_cingulate_cortex"]
frameworks: ["reinforcement_learning", "model_based_rl", "successor_representation", "hierarchical_rl"]
keywords: ["successor", "representation", "subserves", "hierarchical", "abstraction", "goal", "directed", "behavior"]
key_citations: ["dayan1993_successor_representation", "stachenfeld2017_hippocampus_predictive_map", "russek2017_model_based_reinforcement", "momennejad2017_successor_representation_humans", "schapiro2013_event_representation_memory", "botvinick2009_hierarchically_organized_behavior", "tomov2020_hierarchical_planning_representation"]
---

### One-line summary

The successor representation captures how humans learn predictive models of task structure that enable hierarchical abstraction for efficient goal-directed planning.

### Background & motivation

Naturalistic decision making involves long-range dependencies and temporally extended behaviors that are computationally challenging for standard reinforcement learning models due to combinatorial explosion of states and actions. Hierarchical reinforcement learning addresses this through state abstractions, but the neurocomputational mechanisms underlying hierarchical representation learning remain unclear. The successor representation (SR) has been proposed as a biologically plausible mechanism for learning task structure that could support hierarchical abstraction, but whether humans actually leverage SR-based representations for goal-directed behavior had not been demonstrated.

### Methods

- **Task design**: 120 participants (after exclusions) played a "museum tour guide" game where they navigated a virtual museum with 15 rooms organized in a "ring-of-cliques" structure (3 wings of 5 highly interconnected rooms each)
- **Action-outcome contingencies**: Binary choices (z/m keys) mapped probabilistically to two of four possible neighboring rooms; mappings engineered to allow hierarchical control at the wing level
- **Training phase**: 75 miniblocks with balanced start-goal combinations to ensure unbiased learning of the museum structure
- **Testing phase**: Goal-directed navigation with changing goals, budget of 1000 room transitions, reward for efficient pathfinding
- **Post-test**: Free-sort task where participants reconstructed the museum layout from memory
- **Computational models fit to behavior**:
  - Null model (intercept only for choices; nuisance regressors for RTs)
  - Model-based RL (optimal, one-step predictive model with perfect environment knowledge)
  - Explicit hierarchical model (perfect knowledge of wing-level structure, no room-level detail)
  - Successor representation (learned multi-step predictive representation with state-action conjunctions)
- **Model comparison**: Random-effects Bayesian model selection with PSIS-LOO cross-validation
- **Response time modeling**: Shifted log-normal distribution with regressors for expected value, reward prediction error, state prediction error, and conflict
- **Choice modeling**: Response-coded logistic regression

### Key findings

- **Choice behavior**: The explicit hierarchical model accounted best for choice behavior (protected exceedance probability = 1, BOR < 10^-26). Participants consistently selected the action rotating toward the goal wing (M = 1.172, HDI95% = [0.992, 1.350]), dynamically switching responses upon entering/leaving the goal wing.
- **Response times**: The successor representation model accounted best for response times (protected exceedance probability = 1, BOR < 10^-10). Key SR predictors: state prediction error (SPE) showed slowing between wings (M = 0.015), expected value (EV) showed slowing near goal (M = 0.033), reward prediction error (RPE) showed speeding toward goal (M = -0.023).
- **Modularity correlations**: Individual differences in SR modularity (derived from discount factor) correlated with:
  - Better hierarchical choice behavior (β = 0.768, p = 0.037)
  - Higher accumulated reward bonus (β = 3.433, p < 0.001)
  - More accurate memory reconstruction of museum layout
  - Better discrimination of boundary rooms within same community
- **Dual representation**: Participants appear to use both detailed SR-based predictive representations (evident in RTs) and simplified hierarchical abstractions (evident in choices), with SR modularity predicting the quality of hierarchical abstraction.

### Computational framework

**Successor Representation (SR)**: The SR learns a matrix M of expected future (discounted) state-action visits: M_sa,sa' = E[Σ_t γ^t I(s_t = s', a_t = a')]. The discount factor γ arbitrates the temporal horizon—moderately high values emphasize community structure (higher-order wing organization), while lower values emphasize individual room locations. The SR is updated via temporal-difference learning with state prediction errors (SPE). Unlike optimal model-based RL, the SR holds multi-step predictive knowledge and its predictions depend on the policy being followed. For response time modeling, state prediction error was computed as angular distance between successor vectors, capturing the similarity between expected and observed state-occupation patterns without being sensitive to vector magnitude (which grows with discount factor).

### Prevailing model of the system under study

Before this study, the successor representation was proposed as a mechanism for learning task structure that could theoretically support hierarchical abstraction, but there was no direct evidence that humans actually use SR-based representations for goal-directed behavior. Previous work showed that SR-like representations emerge in the hippocampus during incidental learning and that humans are sensitive to community structure in prediction tasks, but the link between SR learning and hierarchical abstraction for planning remained theoretical. The prevailing assumption was that hierarchical abstraction might be computed from learned task structures through graph-theoretic algorithms (spectral methods, betweenness-centrality), but these approaches assumed accurate adjacency matrices without considering how the learning mechanism itself might influence abstraction quality.

### What this paper contributes

This paper provides the first empirical demonstration that successor representation learning subserves hierarchical abstraction for goal-directed behavior. The key novel contributions are:

1. **Dual-process dissociation**: The study reveals that humans simultaneously maintain two distinct representations of the same task—a detailed SR-based predictive representation (evident in response times sensitive to state prediction errors, expected values, and community boundaries) and a simplified hierarchical abstraction (evident in choice behavior following a coarse "rotation" policy at the wing level).

2. **Individual differences link SR to abstraction**: Individual differences in SR modularity (how strongly the learned representation captures community structure) correlate with the effectiveness of hierarchical abstraction in choices, accumulated reward, and memory accuracy. This establishes a direct relationship between the quality of predictive learning and the quality of hierarchical planning.

3. **Model comparison evidence**: Bayesian model comparison strongly favors the SR model for response times over null, model-based, and explicit hierarchical alternatives (pxp = 1, BOR < 10^-10), while choice behavior is best explained by the explicit hierarchical model (pxp = 1, BOR < 10^-26).

4. **Response time signatures of SR learning**: The study replicates and extends previous findings of between-community slowing (higher response times for transitions between vs. within wings) and links this specifically to SR state prediction errors, expected values, and reward prediction errors, providing a fine-grained characterization of how predictive representations influence behavior.

### Brain regions & systems

Not applicable (behavioral study with computational modeling). The paper discusses potential neural substrates in the Discussion: hippocampus (successor-like representations during statistical learning), medial prefrontal cortex/anterior cingulate cortex (hierarchical decision making and model-based evaluation), and potential rostro-caudal abstraction gradients in frontal cortex, but no direct neural measures were obtained.

### Mechanistic insight

**Computational level**: The brain solves the problem of efficient planning in complex, temporally extended tasks by learning predictive representations that capture multi-step statistical structure of the environment. The discount factor in the successor representation arbitrates a trade-off between emphasizing fine-grained state transitions (low discount) vs. coarse community structure (high discount), with moderately high values optimal for hierarchical abstraction.

**Algorithmic level**: The successor representation is learned via temporal-difference updating with state prediction errors (SPE). The learned matrix M encodes expected future discounted state-action occupations. For decision making, this representation supports two distinct computations: (1) evaluation of expected values through multiplication with reward vectors (evident in response time effects of EV, RPE), and (2) extraction of hierarchical structure through identification of densely connected communities (evident in choice behavior following rotation policies). The angular distance between successor vectors provides a scalar surprise signal for response time modulation.

**Implementational level**: Not directly addressed—this is a behavioral study. However, the Discussion speculates that hippocampus may implement successor-like predictive maps (consistent with fMRI studies showing SR-like representations in hippocampus during incidental learning), while anterior cingulate/medial prefrontal cortex may represent hierarchical decision variables and action-outcome predictions. The dopaminergic system may encode vector prediction errors for updating successor representations. These neural hypotheses remain to be tested with the current task.

### Limitations & open questions

- **Causal neural mechanisms**: The study is purely behavioral; the proposed neural substrates (hippocampus, prefrontal cortex, dopamine) remain speculative and require direct testing with neuroimaging or lesion methods.
- **Model indistinguishability**: Alternative sequence learning mechanisms (free energy minimization, hidden Markov models) could produce isomorphic predictions if they implement equivalent discounting mechanisms; the SR is not uniquely identified.
- **State-action vs. state-state SR**: The study finds no reliable difference between state-action and state-state SR formulations, though the winning state-action model slightly underperforms in predicting boundary-room effects.
- **Direction of causality**: The correlation between SR modularity and hierarchical abstraction does not establish whether better SR learning causes better abstraction, or whether a common factor (e.g., task engagement) drives both.
- **Computational cost of hierarchical abstraction**: The hypothesis that hierarchical policies are chosen to reduce computational costs of low-level planning remains speculative; direct measures of cognitive effort or decision time were not obtained.
- **Generalization to other tasks**: The museum task's specific structure (ring-of-cliques, binary choices with probabilistic outcomes) may limit generalizability to other hierarchical planning domains.
- **Mechanism of abstraction extraction**: The specific algorithm by which hierarchical abstractions are extracted from SR representations remains unspecified—multiple graph-theoretic approaches are compatible with the data.

### Connections & keywords

**Key citations**: Dayan (1993) - original successor representation formulation; Stachenfeld et al. (2017) - hippocampus as predictive map; Russek et al. (2017), Momennejad et al. (2017) - successor representation in human reinforcement learning; Schapiro et al. (2013), Lynn et al. (2020) - community structure and statistical learning; Botvinick et al. (2009), Holroyd & Verguts (2021) - hierarchical reinforcement learning and anterior cingulate cortex; McNamee et al. (2016), Tomov et al. (2020) - algorithms for hierarchical abstraction.

**Named models or frameworks**: Successor representation (SR); Model-based reinforcement learning; Explicit hierarchical model; Graph-theoretic community structure; Ring-of-cliques graph structure; Temporal-difference learning; State prediction error (SPE); Reward prediction error (RPE); Expected value (EV); Bayesian model selection (GroupBMS); Pseudo-BMA+ weighting; PSIS-LOO cross-validation.

**Brain regions**: Hippocampus (discussed as potential locus of SR learning); Anterior cingulate cortex (discussed as potential locus of hierarchical decision making); Medial prefrontal cortex (discussed as potential locus of action-outcome prediction); Midbrain dopamine system (discussed as potential source of prediction error signals).

**Keywords**: successor representation, hierarchical reinforcement learning, goal-directed behavior, community structure, predictive learning, computational modeling, state prediction error, decision making, cognitive map, graph-theoretic abstraction, planning, model-based RL, behavioral experiments, museum navigation task, statistical learning.
