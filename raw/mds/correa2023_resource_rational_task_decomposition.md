Humans decompose tasks by trading off utility and computational cost 

Carlos G. Correa[1] , Mark K. Ho[2,3] , Frederick Callaway[2] , Nathaniel D. Daw[1,2] , Thomas L. Griffiths[2,3] 

**1** Princeton Neuroscience Institute, Princeton University, Princeton, NJ, USA 

**2** Department of Psychology, Princeton University, Princeton, NJ, USA 

**3** Department of Computer Science, Princeton University, Princeton, NJ, USA 

* cgcorrea@princeton.edu 

## **Abstract** 

Human behavior emerges from planning over elaborate decompositions of tasks into goals, subgoals, and low-level actions. How are these decompositions created and used? Here, we propose and evaluate a normative framework for task decomposition based on the simple idea that people decompose tasks to reduce the overall cost of planning while maintaining task performance. Analyzing 11,117 distinct graph-structured planning tasks, we find that our framework justifies several existing heuristics for task decomposition and makes predictions that can be distinguished from two alternative normative accounts. We report a behavioral study of task decomposition ( _N_ = 806) that uses 30 randomly sampled graphs, a larger and more diverse set than that of any previous behavioral study on this topic. We find that human responses are more consistent with our framework for task decomposition than alternative normative accounts and are most consistent with a heuristic—betweenness centrality—that is justified by our approach. Taken together, our results provide new theoretical insight into the computational principles underlying the intelligent structuring of goal-directed behavior. 

## **Introduction** 

Human thought and action are hierarchically structured: We rarely tackle everyday problems in their entirety and instead routinely decompose problems into more manageable subproblems. For example, you might break down the high-level goal of “cook dinner” into a series of intermediate subgoals such as “choose a recipe,” “get the ingredients from the store,” and “prepare food according to the recipe.” Task decomposition—identifying subproblems and reasoning about them—lies at the heart of human general intelligence. It allows people to tractably solve problems that occur at many different timescales, ranging from everyday tasks such as cooking a meal to more ambitious projects such as completing a Ph.D. 

At least two questions arise in the context of human task decomposition. First, how do people use decompositions? Second, how do people decompose tasks to begin with? Existing research provides answers to these two questions, but does so largely by considering each one in isolation. For example, we know that, when given hierarchical structure, people readily use it to bootstrap learning [Botvinick et al., 2009,Eckstein and Collins, 2020] and to organize planning [Balaguer et al., 2016,Cushman and Morris, 2015]. Separately, studies show how hierarchical structure emerges from graph-theoretic properties of tasks (e.g., “bottleneck” states) [Stachenfeld et al., 2017], latent causal structure in the environment [Collins and Frank, 2013,Tomov et al., 2020], or efficient encoding of optimal behaviors [Solway et al., 2014]. These accounts provide insights into the function and mechanisms of hierarchically structured, action-guiding representations, but, again, they largely consider _the use_ and _the creation_ of such representations separately. 

In this paper we bridge this gap, developing an integrated account of how using a decomposition interacts with the task decomposition process itself. Our proposal is organized around a deceptively simple idea: Task decompositions are learned to facilitate efficient planning (Fig 1). Based on this intuition, we develop a normative framework that specifies how an idealized agent should choose a hierarchical structure for a domain, given the need to balance task performance with the costs of planning. We quantify planning costs straightforwardly as the run-time of a planning algorithm, which means that our framework predicts that task decomposition is the result of interactions between task structure and the algorithm used to plan. Because we quantitatively examine how cognitive costs are balanced with task performance in the style of a 

1 

_resource-rational analysis_ [Lewis et al., 2014,Gershman et al., 2015a,Griffiths et al., 2015], we refer to our framework as _resource-rational task decomposition_ . 

Although much prior research is motivated by the idea that hierarchical task decomposition has the potential to reduce planning costs [Sacerdoti, 1974a,Korf, 1985b,Sutton et al., 1999,S¸im¸sek et al., 2005,Ramkumar et al., 2016,Solway et al., 2014,Huys et al., 2015,Jinnai et al., 2019], our framework differs from many existing accounts because we directly incorporate planning costs into the criteria used to choose a task decomposition. By contrast, existing normative accounts typically formulate task decomposition as _structure inference_ with the goal of inferring the hierarchical structure of the environment [Collins and Frank, 2013,Tomov et al., 2020] or sequential behavior [Solway et al., 2014,Maisto et al., 2015], which only indirectly connect to the computations involved in planning or their efficiency. Our framework explicitly considers how planning efficiency shapes hierarchical representations, which we use to demonstrate how resource-rational task decompositions change with varied search algorithms. Additionally, normative accounts often have limited ability to explain human behavior without the specification of algorithmic details necessary to be efficient or psychologically plausible. Because our account focuses on efficient use of planning, it is even more critical to spell out these details. We conduct an initial exploration of these issues by examining the capacity of existing heuristics to serve as efficient algorithmic approximations to our normative account. 

Using this framework, we conduct a systematic comparison of resource-rational task decomposition with four alternative formal models previously reported in the literature [S¸im¸sek et al., 2005,S¸im¸sek and Barto, 2009,Solway et al., 2014,Tomov et al., 2020] using 11,117 different graph-structured planning tasks. One key insight from this analysis is that our framework can justify several previously proposed _heuristics_ for task decomposition based on graph-theoretic properties (e.g., those that capture the idea of “bottleneck states” [S¸im¸sek and Barto, 2009, S¸im¸sek et al., 2005]). Our framework thus provides a normative justification for these heuristics within a broader framework of resource-rational decision-making. Critically, these connections between our framework and heuristics also demonstrates the existence of efficient approximations to our formal framework. We also show that our framework produces predictions that are distinguishable from previous normative models of task decomposition. 

To empirically evaluate this framework, we report results from a pre-registered experiment ( _N_ = 806) that uses 30 distinct graph-structured tasks sampled from the larger set of 11,117 graphs. To our knowledge, this set of graph-structured tasks is larger and more diverse than that of any other experiment previously reported in the literature on how people decompose tasks. As such, it enables us to draw more general conclusions about task decomposition than previous studies. Across this large stimulus set, we find that our framework provides the best explanation for participant responses among normative accounts, which supports the thesis that people’s hierarchical decomposition of tasks reflects a rational allocation of limited computational resources in service of effective planning and acting. 

## **Results** 

## **A Formal Framework for Task Decomposition** 

How should an agent decompose a task? When purely optimizing behavior on a task (e.g., taking a shortest path in a graph), decomposing a task is only worthwhile in some larger context, such as making learning or computation more efficient. The computational efficiency of planning is a critical concern – as one attempts to plan into an increasingly distant future, over a larger state space, or under conditions of greater uncertainty, computation quickly becomes intractable, a challenge termed the _curse of dimensionality_ [Bellman, 1957a]. In some cases, task decomposition can ameliorate this curse by splitting a task into more manageable subtasks. The difficulty comes in choosing among task decompositions since a bad choice can make the task at hand even more difficult [Botvinick et al., 2009]. In this work, we formulate a framework for task decomposition where _planning costs_ directly factor into people’s choices—quite literally, our framework decomposes tasks into subtasks based on the run-time and utility of the plan that results from planning algorithms that solve the subtasks. 

To demonstrate the role planning costs play in how people break down tasks, consider the following scenario: After leaving work for the day, you plan to go to the post office to send a letter. Since you rarely navigate directly from your workplace to the post office, you’ll have to do some planning. You could determine some efficient way to get from work to the post office, but an alternative is to first get somewhere 

2 

**==> picture [436 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>IDDFS<br>Task BFS<br>No subgoal<br>RW With subgoal<br>Monolithic  Task  Subtask-Level  Action-Level  0 200 400 600 800 1000<br>Task Decomposition Planning Planning Search Cost (iterations)<br>(c) Breadth-First Search (d) Iterative-Deepening (e) Random Walk<br>Depth-First Search<br>**----- End of picture text -----**<br>


**Figure 1.** Choosing task decompositions that make planning more efficient. (a) Our framework for task decomposition accounts for the computational cost of planning towards subgoals—task decompositions should jointly optimize task performance and the computational cost of search. We formalize this in three nested layers of optimization: Action-Level Planning solves for a plan to accomplish a subgoal, which has a computational cost. Subgoal-Level Planning constructs subgoal sequences that maximize reward and minimize computational cost. Task Decomposition selects subgoals based on their value in Subgoal-Level Planning. (b) Plot of search cost for Breadth-First Search (BFS), Iterative-Deepening Depth-First Search (IDDFS), and a Random Walk (RW) in the task depicted in (c-e), with and without subgoals. Use of subgoals results in decreased search cost for BFS and IDDFS, but not for RW. (c-e) Search costs under the algorithms. The depicted task requires navigating from the start state (green) to the goal state (orange) with fewest steps. Search cost is the number of iterations required for the search algorithm to find a solution. Larger states were considered more often during the search algorithm, resulting in greater search cost. _Top_ : Search cost without subgoals. _Bottom_ : Search cost when using the path midpoint as a subgoal (blue). 

that is easy to navigate to, but also along the way. Maybe the caf´e you stop by every morning before work—If it’s easier to plan a route from the caf´e to the post office, then you’ve simplified your problem by breaking it down into subtasks. This example suggests that the ways people break tasks down (e.g., navigating to the caf´e first) is a trade-off between efficiency (e.g., taking a quick route) and the cost of planning with that task decomposition (e.g., planning via the caf´e is simpler). 

We formalize our framework using three nested levels of planning and learning (Fig 1a). At the lowest level is _action-level planning_ , where concrete actions are chosen that solve a subtask (e.g., what direction do I walk to get to the caf´e). The next level is _subtask-level planning_ , where a sequence of subtasks is chosen (e.g., first navigating to the caf´e and then to the post office). Finally, the highest level is _task decomposition_ , where a set of subtasks that break up the environment are selected (e.g., setting the caf´e as a possible subgoal across multiple tasks). 

A central feature of our framework is the interdependence of choices made at each level: The optimal task decomposition depends on the computations occurring in the subtask-level planner, which depend on the computations that occur at the action-level. In particular, we are interested in how different decompositions can be evaluated as better or worse based on the cost of computing good action-level plans for a series of subtasks chosen by the subtask-level planner. In the next few sections, we discuss these different levels and 

3 

how they relate to one another. 

## **Action-level Planning** 

Action-level planning computes the optimal actions that one should take to reach a subgoal. Here, we focus on deterministic, shortest path problems. Formally, action-level planning occurs over a task ( _S, T, s_ 0 _, z_ ) defined by a set of states, _S_ ; an initial state, _s_ 0 _∈S_ ; a subgoal state, _z ∈S_ ; and valid transitions between states, _T ⊆S × S_ , so that _s_ can transition to _s[′]_ when ( _s, s[′]_ ) _∈ T_ . The neighbors of _s_ are the states _s[′]_ that it can transition to, _N_ ( _s_ ) = _{s[′] |_ ( _s, s[′]_ ) _∈ T }_ . We refer to the structure of a task ( _S, T_ ) as the task environment or the task graph. 

Given an initial state, _s_ 0, and a subgoal, _z_ , action-level planning seeks to find a sequence of states that begins at _s_ 0 and ends at _z_ , which we denote as a plan _π_ = _⟨s_ 0 _, s_ 1 _, ..., z⟩_ . An action-level plan is computed by a _planning algorithm_ , which is a stochastic function that takes in the initial state, valid transitions, and subgoal state and takes a certain amount of time to run, _t_ . Thus, we can think of a planning algorithm `Alg` as inducing a distribution over plans and run-times given a start and end state, _P_ `Alg` ( _π, t | s, z_ ). In this work, we considered four different planning algorithms [Russell and Norvig, 2009,Ghallab et al., 2016], which we summarize below. We start with a simple algorithm that hardly seems like one—the _random walk (RW) algorithm_ . The algorithm starts at the initial state _s_ 0 and repeatedly transitions to a uniformly sampled neighbor of the current state until it reaches the subgoal state _z_ . Because it does not keep track of previously visited states to inform state transitions, this algorithm can revisit states many times and can result in both path lengths and run-times that are unbounded. 

_Depth-first search (DFS)_ augments RW by keeping track of the states along its current plan—this helps minimize repeated state visits. Because DFS does this, it will sometimes reach a dead-end where it is unable to extend the current plan, so it backtracks to an earlier state to consider an alternative choice among the other neighbors. DFS ensures that resulting plans avoid revisiting states, but still might be suboptimal and repeatedly consider the same states during the search process. 

_Iterative Deepening Depth-first Search (IDDFS; [Korf, 1985a])_ consists of depth-limited DFS run to increasing depths until the goal is found; while based on DFS, IDDFS returns optimal paths because it systematically increases the depth limit. IDDFS is conceptually similar to “progressive deepening,” a search strategy proposed by de Groot in seminal studies of chess players [De Groot, 1965,Newell and Simon, 1972a]. 

_Breadth-first search (BFS)_ ensures optimal paths by systematically exploring states in order of increasing distance from the start state _s_ 0. The algorithm does so by considering all neighbors of the start state (which are one step away), then all of their unvisited neighbors (which are two steps away), and so on, successively repeating this process until the goal is encountered. Through this systematic process, BFS is able to guarantee optimal solutions and ensure states will only ever be considered once, making the algorithm run-time linear in the number of states. 

Having introduced various search algorithms, we now turn to the role algorithms play in subtask-level planning, where algorithm plans and run-times jointly influence the choice of hierarchical plan. 

## **Subtask-Level Planning** 

Here, we assume a simplified model of hierarchical planning that involves only a single level above action-level planning, which we call _subtask-level planning_ . Formally, subtask-level planning occurs over a set of subgoals, _Z ⊂S_ . Given a set of subgoals, subtask-level planning consists of choosing the best sequence of subgoals that accomplish a larger aim of reaching a goal state _g ∈S_ . Each subgoal is then provided to the action-level planner, and the resulting action-level plans are combined into a complete plan to reach the goal state. 

The objective of the subtask-level planner is to identify the sequence of subgoals that brings the agent to the goal state while maximizing task rewards and minimizing computational costs. Here, we focus on a domain in which the task is simply to reach the goal state in as few steps as possible. Formally, the task reward associated with executing a plan is then simply the negative number of states in that plan: _R_ ( _π_ ) = _−|π|_ . The computational cost that we consider is _cumulative expected run-time_ . Thus, we define a subgoal-level reward function when planning to a single subgoal _z_ from a state _s_ using a planning algorithm 

4 

that induces a distribution over plans and run-times _P_ `Alg` ( _π, t | s, z_ ) as: 

**==> picture [326 x 24] intentionally omitted <==**

This formulation is analogous to other resource-rational models that jointly optimize task rewards and run-time [Lieder et al., 2014,Callaway et al., 2022] but applied to the problem of task decomposition. 

Eq 1 defines the rewards for planning towards a single subgoal, but subtask-planning requires chaining plans together to form a larger plan that efficiently solves the task. This sequential optimization problem can be compactly expressed as a set of recursively defined Bellman equations [Bellman, 1957b]. Formally, given a task goal _g_ , a set of subgoals _Z_ , and an algorithm `Alg` , the optimal subtask-level planning utility for all non-goal states _s_ is then: 

**==> picture [317 x 18] intentionally omitted <==**

To ensure this recursive equation terminates, the utility of the goal state _g_ is _VZ[g]_[(] _[g]_[) = 0.][The][fixed][point][of] Eq 2 can be used to identify the optimal subtask-level policy [Puterman, 1994]. We permit the selection of the goal _g_ as a subgoal to ensure that it is possible for the subtask-level planner to solve the task. 

## **Task Decomposition** 

Having defined action-level planning and subtask-level planning over subgoals, we can now turn to our original motivating question: How should people decompose tasks? In this context, this reduces to the problem of selecting the best set of subgoals to plan over _Z_ . Importantly, we assume that people rely on a common set of subgoals for all the different possible tasks that they might have to accomplish in a given environment. Thus, the value of a task decomposition, _Z_ , is given by the value of the subtask-level plans averaged over the task distribution of an environment, _p_ ( _s_ 0 _, g_ ). That is, 

**==> picture [294 x 23] intentionally omitted <==**

To summarize, the value of a task decomposition (Eq 3) depends on how a subtask-level planner plans over the decomposed task (Eq 2), which is shaped by the resulting plans and run-time of action-level planning (Eq 1). This model thus captures how several key factors shape task decomposition: the structure of the environment, the distribution of tasks given by an environment, and the algorithm used to plan at the action level. 

To provide an intuition for our framework, we explore its predictions in a simple task in Figs 1c-1e. The environment is a grid with a single task that requires navigating from the green square to the orange square. Each column in the figure corresponds to a different search algorithm, showing how search costs change without subgoals (Top) and with a subgoal (Bottom; subgoal in blue). While the task seems like it would be extraordinarily trivial to a person—like walking from one side of a room to another—a critical attribute of these search algorithms is they have an entirely unstructured representation of the environment, giving them only very local visibility at a state. A more analogous task for a person might be navigating in a place with low visibility, such as a forest or a city in a blackout. Even in this simple task, some search algorithms (BFS and IDDFS) can be used more efficiently when the problem is split at its midpoint (Fig 1b). The random walk is a notable counterexample, where using a subgoal results in less efficient search. This result may initially seem puzzling, but occurs because a random walk is likely to get to the goal without passing through the subgoal. This example clearly demonstrates a few characteristics of our framework—that the choice of hierarchy critically depends on the algorithm used for search, and that hierarchy can have a normative benefit (since it reduces computational costs) even in the absence of learning or generalization. 

## **Comparing Accounts of Task Decomposition** 

A number of existing theories have been proposed for how people decompose tasks. These accounts can be divided into two broad categories: _heuristics_ for decomposition based on graph-theoretic properties of tasks and _normative_ accounts based on the functional role of a decomposition. Our account is normative, so 

5 

comparison with alternative normative accounts highlights the unique functional consequences of our framework. By comparing our framework to heuristics, we can characterize their predictions relative to normative theories as well as rationalize their use as heuristics for task decomposition. All models are listed and briefly described in Table 1. 

**Table 1.** Descriptions of Normative Algorithms and Heuristics 

|Normative Algorithm|Description|
|---|---|
|RRTD-RW|Resource-Rational<br>Task<br>Decomposition|
||(RRTD) using a Random Walk (RW) as a|
||search algorithm|
|RRTD-BFS|RRTD using Breadth-First Search (BFS) as a|
||search algorithm|
|RRTD-IDDFS|RRTD using Iterative-Deepening Depth-First|
||Search (IDDFS) as a search algorithm|
|Solway et al. (2014) [Solway et al., 2014]|Identifies partitions of the task into subtasks|
||that minimize the description length of opti-|
||mal solutions, given that subtask solutions are|
||reused across tasks.|
|Tomov et al. (2020) [Tomov et al., 2020]|Performs inference over partitions of the task|
||graph into regions based on a prior over hier-|
||archical graphs. Incorporates a preference for|
||tasks to start and end in the same region, and|
||for states in the same region to have similar|
||rewards.|
|Heuristic|Description|
|QCut [S¸im¸sek et al., 2005]|Partitions the task graph through spectral de-|
||composition of the graph.|
|Degree Centrality|Chooses subgoals based on Degree Centrality,|
||which is the number of transitions into or out of|
||a state _s_. For tasks where all state transitions|
||are reversible, Degree Centrality is the number|
||of neighbors _|N_(_s_)_|_.|
|Betweenness Centrality [S¸im¸sek and Barto, 2009]|Chooses subgoals based on Betweenness Cen-|
||trality, which is how often a state_s_ appears on|
||shortest paths, averaged over all possible start|
||and goal states. Takes into account cases with|
||multiple shortest paths.|



To begin with, one way to compare accounts is to relate them formally. We do so by relating resource-rational task decomposition with a random walk (RRTD-RW) to QCut and Degree Centrality in the Appendix. We prove a relationship between RRTD-RW and QCut that connects the two methods through spectral analysis, and examine how the relationship between RRTD-RW and Degree Centrality varies based on spectral graph properties. 

Another method we can use to compare theories is to compute their subgoal predictions on a fixed set of environments and compare them—qualitatively or quantitatively. This approach has been used in existing studies, but nearly always through qualitative comparison using a small number of hand-picked environments. For example, several published models perform qualitative comparisons to the graphs studied in Solway et al. 

6 

(2014) [Solway et al., 2014]. These environments contain states that most models agree should be subgoals [Tomov et al., 2020,McNamee et al., 2016,Donnarumma et al., 2016,Correa et al., 2020]—these states are typically one or few that connect otherwise disconnected parts of the environment, making them “bottleneck states.” Environments with these kinds of bottleneck states robustly elicit hierarchically-structured behavior in experiments, but make it difficult to distinguish among theoretical accounts because they are in strong agreement (see top row of Fig 2). 

**==> picture [94 x 45] intentionally omitted <==**

**==> picture [93 x 45] intentionally omitted <==**

**==> picture [94 x 42] intentionally omitted <==**

**==> picture [94 x 45] intentionally omitted <==**

**==> picture [94 x 48] intentionally omitted <==**

**==> picture [93 x 48] intentionally omitted <==**

**==> picture [94 x 46] intentionally omitted <==**

**==> picture [94 x 47] intentionally omitted <==**

**==> picture [94 x 67] intentionally omitted <==**

**==> picture [93 x 66] intentionally omitted <==**

**==> picture [94 x 68] intentionally omitted <==**

**==> picture [94 x 70] intentionally omitted <==**

**==> picture [432 x 10] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) IDDFS (b) Betweenness Centrality (c) Solway et al. (2014) (d) Tomov et al. (2020)<br>**----- End of picture text -----**<br>


**Figure 2.** Comparing predictions of the (a) RRTD-IDDFS, (b) Betweenness Centrality, (c) Solway et al. (2014), and (d) Tomov et al. (2020) models. State color and size is proportional to model prediction when using the state as a subgoal. (Top) The 10-node, regular graph from Solway et al. (2014). (Middle, Bottom) Two eight-node graphs selected from the 11,117 included in our analysis. 

To perform a large-scale and unbiased comparison of these algorithms, we chose from a structurally rich set of environments: the set of all possible 11,117 simple, undirected, eight-node, connected graphs. We compare subgoal choice for several heuristic theories, several variants of our framework, and variants of the normative account proposed by Solway et al. (2014) [Solway et al., 2014] and Tomov et al. (2020) [Tomov et al., 2020] in Fig 3 (the theories are described in Table 1). Each cell of Fig 3 is the correlation between the subgoal predictions of a pair of theories, averaged across all environments. For simplicity, we assume the task distribution is a uniform distribution over pairs of distinct start and goal states. For the RRTD-based models, the model prediction for a state is the corresponding value of task decomposition when the state is the only possible subgoal. 

We find a few notable clusters of theories—one demonstrates that RRTD-IDDFS is well-correlated with subgoal sampling based on Betweenness Centrality—this suggests the potential of a formal connection between the two algorithms, though the authors are not aware of an existing proof connecting them. A second prominent cluster shows RRTD-RW and Degree Centrality are highly correlated and that both are moderately correlated with QCut, consistent with our formal analysis. The remaining algorithms—RRTD-BFS, Solway et al. (2014), and Tomov et al. (2020)—are singleton clusters, suggesting 

7 

**==> picture [292 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.00<br>RRTD-IDDFS 1 0.95 0.71 0.73 0.39 0.65 0.59 0.53<br>0.75<br>Betweenness Cent. (log) 0.95 1 0.74 0.78 0.33 0.58 0.51 0.53<br>0.50<br>RRTD-RW 0.71 0.74 1 0.98 0.57 0.4 0.39 0.42<br>0.25<br>Degree Cent. (log) 0.73 0.78 0.98 1 0.52 0.41 0.35 0.43<br>0.00<br>QCut 0.39 0.33 0.57 0.52 1 0.24 0.11 0.16<br>0.25<br>Solway et al. (2014) 0.65 0.58 0.4 0.41 0.24 1 0.35 0.33<br>0.50<br>RRTD-BFS 0.59 0.51 0.39 0.35 0.11 0.35 1 0.48<br>0.75<br>Tomov et al. (2020) 0.53 0.53 0.42 0.43 0.16 0.33 0.48 1<br>1.00<br>Betweenness Cent. (log)RRTD-IDDFS RRTD-RWDegree Cent. (log)Solway et al. (2014)QCut Tomov et al. (2020)RRTD-BFS<br>**----- End of picture text -----**<br>


**Figure 3.** Correlation matrix comparing model predictions. For each graph, correlations between two models are computed on the per-state subgoal values, then averaged across the 11,117 simple, connected, undirected, eight-node graphs. We discard correlations when either of the two models predicts a uniform distribution over subgoals, because the correlation is not defined in those instances. 

qualitative differences from the other algorithms. 

To better understand these large-scale quantitative patterns, we qualitatively examine some of the normative algorithms and one heuristic. We focus on the subgoal predictions for three graphs, shown in Fig 2. In the top row is a 10-node, regular graph that has been previously studied [Solway et al., 2014,Tomov et al., 2020]. In the middle row is a similar graph with critical differences: the graph is asymmetric about the graph bottleneck, and the bottleneck of the graph now corresponds to a single state instead of two connected states. In the bottom row is a graph notably distinct from graphs typically studied because it lacks an obvious hierarchical structure. All algorithms make similar predictions for the graph in the top row—an example of the difficulty in using typically studied graphs to distinguish among algorithms. Now, we look at the algorithms in more detail. 

We first examine RRTD-IDDFS (Fig 2a) and Betweenness Centrality (Fig 2b), noting their strong agreement—this is consistent with the large-scale correlation analysis in the previous section. These two algorithms prefer the same subgoals in both graphs. At middle, they prefer the bottleneck state. At bottom, they prefer states that are close to many states—in particular, the two most-preferred states can reach any other state in at most two steps. 

Now, we turn to the other normative accounts: Solway et al. (2014) (Fig 2c) and Tomov et al. (2020) (Fig 2d). Both rely on partition-based representations of hierarchical structure where states are partitioned into different groups. Mapping from partitions onto subgoal choices requires a step of translation. In particular, when considering a path that crosses from one group into another there are two natural subgoals which correspond to the boundary between the groups: either the last state in the first group, or the first state in the second group. In the context of a task distribution, there are many possible ways to map partitions onto subgoal choices, without clear consensus between the two partition-based accounts that we consider. While these analysis choices have little impact on symmetric graphs (e.g., top row of Fig 2), they are important for asymmetric graphs like the one in the middle row, which has a bottleneck state instead of a bottleneck edge. For simplicity, our implementation of Solway et al. (2014) uses the optimal hierarchy, placing uniform weight over all states at the boundaries between groups of the partition, as can be seen in Fig 2c. 

The algorithm from Tomov et al. (2020) introduces other subleties. It poses task decomposition as 

8 

inference of hierarchical structure, with two main criteria: 1) that there are neither too few nor too many groups (accomplished via a Chinese Restaurant Process) and 2) that connections within groups are dense while connections between groups are sparse. The latter leads to issues when connection counts do not reflect hierarchical structure, as shown in Fig 2d. At middle, the algorithm prefers partitions that minimize the number of cross-group connections, even when the bottleneck state is not on the boundary between groups. At bottom, the lack of hierarchical structure that can be detected by edge counts leads the algorithm to make diffuse predictions among many possible subgoals. 

The large-scale comparison of subgoal predictions in Fig 3 demonstrates connections between existing heuristics and our framework for subgoal choice based on search efficiency. These connections suggest a rationale for the efficacy of these heuristics, which may stand in as tractable approximations of our resource-rational framework. Our qualitative comparison in Fig 2 highlights some of the differing predictions among the accounts. But how do these different accounts relate to how people decompose tasks? We turn to this question in the next section. 

## **An Empirical Test of the Framework** 

**==> picture [462 x 331] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) (b)<br>(c) (d)<br>**----- End of picture text -----**<br>


**Figure 4.** Screenshots from the experimental interface. The depicted graph is the same as the top left graph of Fig 8. (a) An example _navigation trial_ . The current state has a green background and goal state has a yellow background. Only the edges connected to the current state are shown. (b) The interface used to show all graph edges between navigation trials. There is no indication of past or future trials on this screen. State icons are only shown when the cursor is placed on them. (c) An example _implicit subgoal probe_ . (d) The final post-task assessment with the _teleportation question_ . 

To measure people’s task decompositions, we ask research participants to report their subgoal use after experience navigating in an environment. A previously published experiment by Solway et al. (2014) [Solway 

9 

et al., 2014] tested task decomposition using three graph navigation tasks. We developed a similar paradigm, but used a set of 30 environments sampled randomly from among the 11,117 used in our large-scale model comparison above. This set of environments is larger and more diverse than those used in previous studies [Solway et al., 2014,Huys et al., 2012] which allows us to draw broader and more generalizable inferences about the task decomposition process. 

Inspired by prior studies [Solway et al., 2014], we conducted an experiment with two phases: participants were first familiarized with an environment by performing a series of _navigation trials_ (Fig 4a), then answered a series of questions about their subgoal choices (Figs 4c, 4d). 

Participants gained exposure to the environment by performing 30 navigation trials requiring navigation to a goal state from some initial state. These _long trials_ were randomly selected while ensuring the initial and goal states were not directly connected (Fig 4a). Participants moved from the current state to a neighboring state using numeric keys. The trial ended when the goal state was reached. In simulations and pilot studies, states with high visit rate coincided with the predictions of the RRTD-IDDFS model. This made it difficult to dissociate RRTD-IDDFS predictions from an alternative account that memorized frequently visited states. To address this confound, the long trials were interleaved with _filler trials_ requiring navigation to a state directly connected to the start state. These filler trials were adaptively selected to increase visits to states besides the most-frequently visited one; in pilot studies and simulations, this was sufficient to dissociate visit rate and model predictions. 

A critical methodological difficulty is visually representing the environment in a way that enables rapid learning, but does not introduce confounds. To prevent participants from relying on heuristics such as the Euclidean distance between states, states were assigned random locations in a circular layout. To encourage model-based reasoning instead of visual search, connections between states were only shown for the current state. So that participants could still easily learn the connections, participants were periodically shown the graph with all connections between trials (Fig 4b). 

To query participant subgoal choice, we used both direct and indirect probes to comprehensively and reliably measure subgoal choice, including novel as well as previously studied prompts [Solway et al., 2014]. In the context of 10 navigation trials, we first prompted participants “Plan how to get from A to B. Choose a location you would visit along the way,” the _implicit subgoal probe_ (Fig 4c). Then, in the context of the same trials after shuffling, we asked participants “When navigating from A to B, what location would you set as a subgoal? (If none, click on the goal),” the _explicit subgoal probe_ . In order to ensure familiarity with the concept of a subgoal, participants were introduced to the concept of a “subgoal” in the context of a cross-country road trip during the experiment tutorial. In a final post-task assessment, we asked participants “If you did the task again, which location would you choose to use for instant teleportation?”, the _teleportation question_ (Fig 4d). We asked this question outside the context of any particular navigation trial. 

## **Experiment Results** 

We recruited English-speaking participants in the United States on the Prolific recruiting platform, prescreening to exclude participants of previous experimental pilots and those with approval ratings below 95%. Of the 952 participants that completed the experiment, 806 (85%) satisfied the pre-registered exclusion criteria requiring participant solutions on navigation trials to use no more than 175% of the optimal number of actions, averaged over the last half of “long” trials. Number of participants per graph varied after exclusion criteria was applied, without significant differences per graph (before exclusion: range 27-34, after exclusion: range 21-30, two-factor _χ_[2] test comparing included to excluded, _p_ = _._ 985). Participants took an average of 17.17 minutes ( _SD_ = 8 _._ 02) to complete the experiment. 

Even though the experimental interface obfuscated task structure by showing the task states in a random circular layout, participants became more effective from the first to the second half of training: “long” trials were solved more quickly (from 10.30s ( _SD_ = 29 _._ 74) to 7.60s ( _SD_ = 11 _._ 19)), with more efficient solutions (from 136% to 120% of optimal number of actions; completely optimal solutions increased from 70% to 79%), and with decreased use of the map (on-screen duration decreased from 9.01s ( _SD_ = 20 _._ 97) to 2.98s ( _SD_ = 12 _._ 66)). 

Our findings are organized into two sections: First, an analysis of the subgoal probes, demonstrating their internal consistency and relationship to behavior. Then, model-based prediction of subgoal probe choice, as well as a subset of choice behavior. 

10 

## **Subgoal probes are internally consistent and predict behavior** 

A crucial methodological concern is the validity of the probes for subgoal choice—in existing studies various types of probes have been used, but not compared systematically. Choice on the explicit and implicit subgoal probes had high within-probe consistency across participants while choice on the teleportation question had low within-probe consistency across participants, based on the average correlation between per-participant choice rates and per-graph choice rates (Explicit Probe _r_ = 0 _._ 71, Implicit Probe _r_ = 0 _._ 63, Teleportation Question _r_ = 0 _._ 37). We also evaluated consistency between probes by comparing the per-graph, per-state choice rates. The Explicit and Implicit Probes were well-correlated ( _r_ = 0 _._ 98, _p < ._ 001), though the relationship between the Teleportation Question and the remaining probes was weaker (Teleportation Question and Explicit Probe: _r_ = 0 _._ 58, _p < ._ 001, Teleportation Question and Implicit Probe: _r_ = 0 _._ 58, _p < ._ 001). 

Beyond simply assessing consistency, it is also crucial to link the probes to participant behavior during navigation, ensuring there is a link between decision making and our indirect assessment via probes. On the Explicit Probe trials, participants were given the option of choosing the goal instead of a subgoal. On average, participants who chose the goal more frequently took longer paths in the navigation trials ( _r_ = 0 _._ 29, _p < ._ 001), which suggests that use of subgoals promotes efficiency. 

To further link the probes to behavior, we examine instances where participants performed the same task (matched by start and goal state) in the navigation trials and the probe trials. This allows us to ask whether participants took paths that passed through the states they later identified as subgoals. To simplify the interpretation of the analysis, we focus on navigation trials where the participant’s path was optimal and there were multiple optimal paths between the start and goal. Evaluated over these pairs of matched navigation and probe trials, we found that participants’ choices on probe trials were consistent with their choices among optimal paths (Explicit Probe: 75.3%, Implicit Probe: 70.7%) more often than would be expected by random choice among optimal paths (Explicit Probe: 70.5%, _p < ._ 001; Implicit Probe: 65.2%, _p < ._ 001; Monte Carlo test). Probe trial choice is also a significant predictor of choice among optimal paths when analyzed using multinomial regression (Explicit Probe: _χ_[2] (1) = 54 _._ 1, _p < ._ 001, Implicit Probe: _χ_[2] (1) = 64 _._ 1, _p < ._ 001). 

In sum, these results suggest the subgoal probes are robust and a valid construct for studying hierarchical planning. 

## **Comparing subgoal choice to theories** 

Having established that participants learned the task, as well as the validity of their probe responses, we now turn to our central claim, namely that subgoal choice is driven by the computational costs of hierarchical planning. Letting participants’ responses to the subgoal probes stand as reasonable proxies of subgoal choice, we relate the predictions of normative accounts and heuristics to participant probe choice across the three probes. 

We start by qualitatively examining participant subgoal choice in Fig 5, extending the qualitative analysis given above with two additional graphs, more model predictions (Fig 5b-5c), and behavioral data averaged across tasks, probes, and participants (Fig 5a). We first note that Betweenness Centrality and RRTD-IDDFS are consistent in the graphs (Fig 5b-5c), and are both relatively consistent with participant probe choice—as described above, states that are close to many other states are preferred. For brevity, we skip over RRTD-BFS and RRTD-RW in this description. The predictions of Solway et al. (2014) are less consistent with participant probe choices (Fig 5f)—as previously described, the predictions are unintuitive because of the difficulty in mapping between partitions and subgoals, particularly when graph bottlenecks correspond to states instead of edges. The predictions of Tomov et al. (2020) are also less consistent with participant probe choices (Fig 5g)—as previously described, the predictions do not correspond with intuitive subgoals because the model relies on between-group edges being sparser than within-group edges. 

We now quantitatively compare model predictions of participant subgoal choice. For each model and probe type, we predict participant choices using hierarchical multinomial regression, where the standardized model predictions are included as a factor with a fixed and per-participant random effect. We compare the relative ability of models to predict probe choice using the Akaike information criterion (AIC) in Fig 6 and report the results of likelihood-ratio tests to the null hypothesis of a uniformly random choice model in Table 2. As in the analysis above, we assume the task distribution is uniformly-distributed over all pairs of 

11 

**Table 2.** Estimated coefficients with standard errors from hierarchical multinomial regression predicting subgoal choice. Likelihood-ratio test statistics compare regression models to null hypothesis of sampling subgoals uniformly at random. 

|Normative<br>Algorithm|Explicit Probe|Implicit Probe|Teleportation Question|
|---|---|---|---|
||_β_ = 0_._37|_β_ = 0_._92|_β_ = 0_._29|
|RRTD-RW|_SE_ = 0_._02<br>_χ_2(2) = 686_._7|_SE_ = 0_._03<br>_χ_2(2) = 1822_._1|_SE_ = 0_._05<br>_χ_2(1) = 39_._9|
||_p < ._001|_p < ._001|_p < ._001|
||_β_ = 4_._98|_β_ = 4_._94|_β_ = 1_._45|
|RRTD-BFS|_SE_ = 0_._10<br>_χ_2(2) = 4412_._8|_SE_ = 0_._11<br>_χ_2(2) = 3402_._8|_SE_ = 0_._20<br>_χ_2(1) = 55_._1|
||_p < ._001|_p < ._001|_p < ._001|
||_β_ = 1_._78|_β_ = 1_._63|_β_ = 0_._73|
|RRTD-IDDFS|_SE_ = 0_._04<br>_χ_2(2) = 5183_._1|_SE_ = 0_._04<br>_χ_2(2) = 3941_._2|_SE_ = 0_._06<br>_χ_2(1) = 155_._7|
||_p < ._001|_p < ._001|_p < ._001|
||_β_ = 0_._75|_β_ = 0_._69|_β_ = 0_._37|
|Solway et al.|_SE_ = 0_._02|_SE_ = 0_._02|_SE_ = 0_._03|
|(2014)|_χ_2(2) = 3929_._7|_χ_2(2) = 3072_._7|_χ_2(1) = 114_._3|
||_p < ._001|_p < ._001|_p < ._001|
||_β_ = 1_._09|_β_ = 0_._97|_β_ = 0_._41|
|Tomov et al.|_SE_ = 0_._03|_SE_ = 0_._02|_SE_ = 0_._04|
|(2020)|_χ_2(2) = 3678_._7|_χ_2(2) = 3056_._4|_χ_2(1) = 102_._4|
||_p < ._001|_p < ._001|_p < ._001|
|Heuristic|Explicit Probe|Implicit Probe|Teleportation Question|
||_β_ =_−_0_._14|_β_ =_−_0_._19|_β_ = 0_._04|
|QCut|_SE_ = 0_._01<br>_χ_2(2) = 1504_._3|_SE_ = 0_._01<br>_χ_2(2) = 1236_._3|_SE_ = 0_._04<br>_χ_2(1) = 1_._4|
||_p < ._001|_p < ._001|_p_=_._238|
||_β_ = 0_._73|_β_ = 0_._64|_β_ = 0_._45|
|Degree Cent.|_SE_ = 0_._02|_SE_ = 0_._02|_SE_ = 0_._04|
|(log)|_χ_2(2) = 2534_._3|_χ_2(2) = 1923_._3|_χ_2(1) = 116_._0|
||_p < ._001|_p < ._001|_p < ._001|
||_β_ = 0_._86|_β_ = 0_._82|_β_ = 0_._58|
|Betweenness Cent.|_SE_ = 0_._02|_SE_ = 0_._02|_SE_ = 0_._03|
|(log)|_χ_2(2) = 5598_._2|_χ_2(2) = 4666_._1|_χ_2(1) = 307_._3|
||_p < ._001|_p < ._001|_p < ._001|



12 

**==> picture [48 x 34] intentionally omitted <==**

**==> picture [47 x 34] intentionally omitted <==**

**==> picture [48 x 34] intentionally omitted <==**

**==> picture [48 x 36] intentionally omitted <==**

**==> picture [48 x 35] intentionally omitted <==**

**==> picture [47 x 36] intentionally omitted <==**

**==> picture [48 x 82] intentionally omitted <==**

**==> picture [48 x 32] intentionally omitted <==**

**==> picture [47 x 32] intentionally omitted <==**

**==> picture [48 x 33] intentionally omitted <==**

**==> picture [48 x 34] intentionally omitted <==**

**==> picture [48 x 34] intentionally omitted <==**

**==> picture [47 x 36] intentionally omitted <==**

**==> picture [48 x 33] intentionally omitted <==**

**==> picture [464 x 31] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) Behavior (b) (c) RRTD- (d) (e) (f) Solway et (g) Tomov et<br>Betweenness IDDFS RRTD-BFS RRTD-RW al. (2014) al. (2020)<br>Centrality<br>**----- End of picture text -----**<br>


**Figure 5.** Visualization of behavior and model predictions on four eight-node graphs selected from the 30 graphs used for the experiment. (a) State color and size is proportional to subgoal choice, summed across participants and probe types. Visualized models are (b) RRTD-IDDFS, (c) RRTD-BFS, (d) RRTD-RW, (e) Betweenness Centrality, (f) Solway et al. (2014), and (g) Tomov et al. (2020). For model predictions, state color and size is proportional to model prediction when using the state as a subgoal. 

distinct states.[1] Among normative theories, we found the RRTD-IDDFS model best explained behavior as judged by AIC. For the Explicit and Implicit Probes, the next best models in sequence were RRTD-BFS, then both Solway et al. (2014) and Tomov et al. (2020) with similar performance, and finally RRTD-RW. For the Teleportation Question, the best models after RRTD-IDDFS were Solway et al. (2014), Tomov et al. (2020), RRTD-BFS, and finally RRTD-RW. This suggests that, among the normative theories, those based on search costs are most explanatory of subgoal choices. We additionally compare model predictions to participant state occupancy during navigation trials in order to assess whether people are relying on simple, memory-based strategies to respond to the probes. We find that participant behavior is better explained by all normative theories for the Explicit and Implicit Probes (with the exception of RRTD-RW), but only RRTD-IDDFS and Solway et al. (2014) for the Teleportation Question. 

Among the heuristic theories, we found Betweenness Centrality best explained behavior as judged by AIC. For all probes, Degree Centrality was next best, followed by QCut. As above, we compared model predictions to participant state occupancy and found that participant behavior is better explained by Betweenness Centrality for the Explicit and Implicit Probes, and both Betweenness and Degree Centrality for the Teleportation Question. These results are consistent with the empirical connection between RRTD-IDDFS and Betweenness Centrality found in the large-scale simulation above. Betweenness Centrality further improves on the behavioral fit of RRTD-IDDFS, suggesting that our participants may be using a metric like Betweenness Centrality to approximate resource-rational task decomposition. We return to this point in the discussion. 

In a final analysis, we predict participant navigation in the instances where their path was one of several optimal paths. We analyze participant choice as a simple two-stage process: a subgoal is sampled with log probability proportional to model predictions (weighted by a parameter _β_ 1), then an optimal path is sampled with log probability proportional to a free parameter _β_ 2 if it contains the subgoal and 0 otherwise. For each theory of subgoal choice, we optimized this two-stage choice model to maximize the likelihood assigned to 

> 1The reported analyses have qualitatively similar results when the task distribution matches the experiment’s “full” trials, which only includes tasks ( _s_ 0 _, g_ ) where the start _s_ 0 and goal _g_ are not neighbors, so ( _s_ 0 _, g_ ) _∈/ T_ . 

13 

**==> picture [360 x 487] intentionally omitted <==**

**----- Start of picture text -----**<br>
Explicit Probe<br>Random Choice<br>RRTD-IDDFS<br>RRTD-BFS<br>RRTD-RW<br>Solway et al. (2014)<br>Tomov et al. (2020)<br>QCut<br>Degree Cent. (log)<br>Betweenness Cent. (log)<br>State Occupancy (log)<br>0 1000 2000 3000 4000 5000<br>AIC<br>Implicit Probe<br>Random Choice<br>RRTD-IDDFS<br>RRTD-BFS<br>RRTD-RW<br>Solway et al. (2014)<br>Tomov et al. (2020)<br>QCut<br>Degree Cent. (log)<br>Betweenness Cent. (log)<br>State Occupancy (log)<br>0 1000 2000 3000 4000<br>AIC<br>Teleportation Question<br>Random Choice<br>RRTD-IDDFS<br>RRTD-BFS<br>RRTD-RW<br>Solway et al. (2014)<br>Tomov et al. (2020)<br>QCut<br>Degree Cent. (log)<br>Betweenness Cent. (log)<br>State Occupancy (log)<br>0 100 200 300<br>AIC<br>**----- End of picture text -----**<br>


**Figure 6.** Comparison of statistical analysis using mixed-effects multinomial regression to predict subgoal choice behavior for each subgoal probe. AIC is relative to the minimum model AIC for each probe. Smaller values indicate better predictivity. 

observed choices. Because there were a relatively small number of trials per participant, we did not fit random effects for participants. The model results are shown in Fig 7. These results are again consistent with those previously observed—among normative theories RRTD-IDDFS is best, among heuristic theories Betweenness Centrality is best, and Betweenness Centrality is overall the most explanatory. 

14 

**==> picture [360 x 144] intentionally omitted <==**

**----- Start of picture text -----**<br>
Choice among optimal paths<br>Random Choice<br>RRTD-IDDFS<br>RRTD-BFS<br>RRTD-RW<br>Solway et al. (2014)<br>Tomov et al. (2020)<br>QCut<br>Degree Cent. (log)<br>Betweenness Cent. (log)<br>0 50 100 150<br>AIC<br>**----- End of picture text -----**<br>


**Figure 7.** Comparison of two-stage choice models to predict participant choice behavior among optimal paths. AIC is relative to the minimum model AIC. Smaller values indicate better predictivity. 

## **Discussion** 

In this work, we have proposed a resource-rational framework for task decomposition where tasks are broken down into subtasks based on planning costs. Our first contribution is a novel formal account of this idea based on a resource rational analysis [Lieder and Griffiths, 2020a]. Specifically, our proposal involves three levels of nested optimization: _Task decomposition_ identifies a set of subgoals for a given task, _subtask-level planning_ chooses sequences of subgoals to reach a goal, and _action-level planning_ chooses sequences of concrete actions to reach a subgoal. Optimal task decomposition thus depends on both the structure of the environment and the computational resource usage specific to the planning algorithm. We quantitatively compared the predictions of our framework to four heuristic and normative theories proposed in the literature across 11,117 graph-structured tasks. These analyses show that our framework provides different predictions from other normative accounts and aligns with heuristics. We argue that this provides a rationalization of these heuristics for task decomposition in terms of resource-rational planning that accounts for computational costs. 

To test our framework, we ran a pre-registered, large-scale study using 30 graph-structured environments and 806 participants. This study includes a more diverse set of tasks than that of any previous reported study in the literature, allowing us to draw more general conclusions about how people form task decompositions. The results of this study reveal that, among normative models, people’s responses most closely align with the predictions of our model. This provides support for our theory that people are engaged in a process of resource-rational task decomposition. Among heuristics for task decomposition, one heuristic is a better fit to behavior than our framework. Because the heuristic makes similar predictions as our framework, this might indicate that people use the heuristic as a tractable approximation to our framework. 

Our account, while normative, is not particularly interpretable. Identifying the qualitative patterns that guide human subgoal choice and relating them to the patterns resulting from our framework’s sensitive to search costs will be necessary to produce an interpretable account of human subgoal choice. A critical piece of the story is developing experimental paradigms that provide rich, but explainable behavior—our experiments extend those in the literature, but our results depend heavily on the self-reported subgoals of research participants. While we have already demonstrated relationships between self-reported subgoals and behavior, making more extensive comparisons to behavior is important for future research. For example, although we found a systematic relationship between participants’ responses to the subgoal probes and their previous navigation decisions, these two measurements were taken minutes apart. We chose to separate these two measurements so as to avoid possible measurement effects in which explicitly asking about subgoals may lead people to navigate through the state they identified. However, this likely weakens the observed relationship between the probe responses and the navigation decisions. Developing experimental techniques to measure subgoal choices in the process of navigation without biasing the planning process is an important direction for future work. 

Our framework is intended to be an idealized treatment of the problem of task decomposition, but an 

15 

essential next step for this line of research is to understand how people tractably approximate the expensive computations needed to determine search costs. Our results already make some progress in this direction. Specifically, we found that participant responses were best explained by the Betweenness Centrality model. This model’s predictions are highly correlated with the normative RRTD-IDDFS model, but require far less computation to produce. This suggests that people may be using Betweenness Centrality as a heuristic to approximate the task decomposition that minimizes planning cost. However, Betweenness Centrality is also expensive to compute since it requires finding optimal paths between all pairs of states–something our participants are not likely doing. Identifying even more efficient approximations to resource-rational task decomposition will be essential for a process-level account of human behavior, as well as for advancing a theory of subgoal discovery for problems with larger state spaces. 

The human capacity for hierarchically structured thought has proven difficult to formally characterize, despite its intuitive nature and long history of study [Newell and Simon, 1972b,Sacerdoti, 1974b]. In this study we propose a resource-rational framework that motivates and explains the use of hierarchical structure in decision making: People are modeled as having subgoals that reduce the computational overhead of action-level planning. Our framework departs from and complements other normative proposals in the literature. Most published accounts pose task decomposition as an _inference problem_ : People are modeled as inferring a generative model of the environment [Collins and Frank, 2013,Tomov et al., 2020] or as compressing optimal behavior [Solway et al., 2014,Maisto et al., 2015]. We quantitatively relate our framework to existing proposals in a simulation study; In addition, we conduct a large-scale behavioral experiment and find that our framework is effective at predicting human subgoal choice. The work presented here is consistent with other recent efforts within cognitive science to understand how people engage in computationally efficient decision-making [Griffiths et al., 2015,Lewis et al., 2014,Gershman et al., 2015b,Lieder and Griffiths, 2020b]. It is also complementary to recent work in artificial intelligence that explores the interaction between planning and task representations [Jinnai et al., 2019,Harb et al., 2018]. Our hope is that future work on human planning and problem solving will continue to investigate the relationships between computation, representation, and resource-rational decision-making. 

## **Methods** 

## **Experiment Design** 

To probe for participant subgoal choice, we employed an experiment inspired by those previously published in Solway et al. [Solway et al., 2014]. In our experiment, participants first navigated on a web-like representation of a graph to learn the graph’s structure (“navigation trials”; Fig 4), then answered a series of task-specific and task-independent questions about subgoal choices (“probe trials”). We then quantitatively analyzed their responses to these questions about subgoal choice. In the Design section, we motivate the choice of various experimental details. Then, in the Procedure section we detail the experimental procedure. The experiment pre-registration is available at . Our pre-registered analysis was a comparison of how well RRTD-IDDFS and Solway et al. (2014) could predict participant probe choice using hierarchical multinomial regression, a subset of the comparisons in Fig 6 and Table 2. 

## **Design** 

The navigation trials were intended to provide participants with an opportunity to learn the structure of the graph. Drawing from results in pilot experiments, we ensured participants could only see the graph edges connected to their current state (Fig 4a). Periodically, the graph with all edges was shown to participants (Fig 4b). Importantly, this was done without signalling any information about future tasks. From pilot experiments, these visual choices (minimizing displayed edges during tasks, but showing all edges periodically between tasks) ensured that participants quickly learned the graph structure instead of relying on the visual representation of the graph. 

From pilot experiments, we observed that states with high visit rate coincided with the predictions of the RRTD-IDDFS model. To address this confound, the experiment had two types of navigation trials: long and filler. Long trials were optimally solved with more than one action (i.e. the start and goal state were not directly connected) and were intended to give participants exposure to the graph structure. Filler trials were 

16 

optimally solved with one action (i.e. the start and goal state were directly connected) and were adaptively chosen to ensure a balanced visit rate that avoided overlapping predictions with our model. This adaptive procedure selected from all possible filler tasks by 1) excluding tasks where the start or goal state was most-visited, and then by 2) sampling uniformly from the remaining tasks with greatest sum of visits to the start and goal states. When all tasks had a most-visited state as a start or goal, the first step was skipped; this circumstance was uncommon and dependent on both participant behavior and the structure of the graph. In effect, this procedure increased the number of most-visited states by increasing visits to states that were nearly (but not) most-visited. In simulations and pilot experiments, this procedure was sufficient to dissociate visit rate and our model predictions. 

Our probes for subgoal choice included two inspired by prior studies [Solway et al., 2014]—the implicit probe and transportation question—and included a novel variant that explicitly asked about subgoal use—the explicit probe. We included these three probes to ensure a reliable and comprehensive measure of subgoal choice. The implicit probe was shown to participants before the explicit probe to avoid biasing participant responses. 

Typical visual layouts of graphs often have a relationship to pairwise state distances, which means that a variety of visual heuristics are effective strategies when problem solving. To avoid these confounding heuristics, we visually represented the graph states in a pseudo-random circular layout (Fig 4). The same circular layout was shown for all trial types, including the periodic display of all graph edges. 

## **Procedure** 

Before the experiment, people were asked to consent to participation in the experiment as approved by the Princeton University Institutional Review Board. 

Each participant was assigned a single graph for the entire experiment, with a fixed circular layout and fixed mapping from nodes to icons. We first introduced them to the experimental interface with an interactive tutorial, showing the visual cues used to mark the current node and goal node and how to navigate along graph edges using the numeric keys of the keyboard. We then introduced the concept of a “subgoal” through the example of a cross-country road trip with a “subgoal” located at the midpoint of the road trip. Participants were asked to describe what they thought “subgoal” meant. 

Navigation trials followed this introductory material. Participants completed a few short practice trials, then completed 60 trials alternating between long and filler trial types: 30 long trials were drawn uniformly from those optimally solved with more than one action, and 30 filler trials were adaptively selected from those optimally solved with one action (described in detail above). In navigation trials, participants started from a node and had to navigate to a goal node. They were also prompted to consider the use of subgoals with the message “It might be helpful to set subgoals.” At any point during a navigation trial, participants could only see the edges connected to their current node (Fig 4a). Every four trials (thus, 15 times total) participants were shown all the edges of the graph (Fig 4b). Since a photograph of the graph shown this way could simplify navigation trials, the icons at each node were only shown when the participant hovered over them. 

Following navigation trials, we probed for subgoal choice. For all probes, the graph was shown in the same circular layout, but edges were hidden. Between every two trials, the graph was shown with all edges as mentioned above. In the context of 10 different tasks, we queried for subgoal choice using the implicit probe: “Plan how to get from A to B. Choose a location you would visit along the way.” For this probe, we excluded both the start and goal node from the available options. Then, in the context of the same 10 tasks after shuffling, we queried for subgoal choice using the explicit probe: “When navigating from A to B, what location would you set as a subgoal? (If none, click on the goal).” For this probe, we only excluded the start node from the available options. Before each of the task-specific probes, participants also completed a few practice trials. Finally, we asked a single instance of the teleportation question: “If you did the task again, which location would you choose to use for instant teleportation?” For this probe, all nodes were available options. 

Finally, participants responded to a multiple-choice survey question: “Did you draw or take a picture of the map? If you did, how often did you look at it?” 

17 

## **Stimuli** 

The graphs we studied were sampled from among the 11,117 simple, connected, undirected, eight-node graphs with sufficient probe trials for the study design. For a given graph, probe trials were sampled uniformly from tasks that require at least 3 actions to optimally solve, a threshold selected based on model predictions that these tasks often require the use of hierarchy. After ensuring each graph had 10 distinct tasks that require 3+ actions to optimally solve, this limited the number of possible graphs to 1,676. The 30 graphs we studied were sampled uniformly at random from these 1,676 graphs (Fig 8). The order of graph nodes in the circular layout, icon assigned to each node, and sequence of navigation and probe trials were all sampled pseudo-randomly. We counter-balanced the assignment of participants to graph, circular layout, and trial orderings. 

All icons designed by OpenMoji, the open-source emoji and icon project. License: CC BY-SA 4.0. 

**==> picture [338 x 111] intentionally omitted <==**

**==> picture [338 x 41] intentionally omitted <==**

**==> picture [338 x 46] intentionally omitted <==**

**==> picture [338 x 107] intentionally omitted <==**

**Figure 8.** The 30 undirected, eight-node graphs that were used in the experiment. 

## **Analyses** 

## **Model Predictions** 

We define a model’s predictions over subgoals as proportional to a utility or log probability. We do so because model predictions are primarily used to predict probe choice using multinomial regression. This leads to a natural interpretation of the coefficients from multinomial regression. For a utility, multinomial regression is equivalent to a softmax choice model, so the coefficient can be equivalently interpreted as an 

18 

inverse temperature. For a log probability, the coefficient _w_ can predict a range of strategies, including random choice for _w_ = 0, probability matching for _w_ = 1, and maximizing based on probability as _w →∞_ . 

We define the task distribution, when applicable to a model, as a uniform distribution over all tasks with distinct start and goal states. 

## **Hierarchical multinomial regression of choice** 

We model participant choice among subgoals using hierarchical multinomial regression with the `mlogit` package in the R programming language. Regression models are fit with 100 draws from the default Halton sequence (parameters `halton=NA, R=100` ). 

For each model, we predict participant choices for each type of probe trial using multinomial regression with model predictions as regressors. Regressors were standardized to be mean-centered with a standard deviation of 1. Since each participant has multiple task-specific probe choices for the explicit and implicit probes, we include random effects for regressors when modeling those probe types. While not explicitly noted above, since the teleportation question was only asked once per participant, prediction of subgoal choice for it was fit without random effects (i.e. non-hierarchical multinomial regression). 

For task-specific probes, the set of possible choices available to the model are configured to match those available to participants, as described in the Procedure section. Additionally, the explicit probe instructs participants to select the goal if they did not use subgoals. For RRTD-based models, we model this with the predicted value for the use of no subgoals. This is equivalent to the sum of the reward and negated planning cost of navigating directly to the goal. 

## **Two-stage model of choice among optimal paths** 

Free parameters _β_ 1 and _β_ 2 were constrained to be greater than or equal to zero. Optimization started from initial parameters _β_ 1 = 1, _β_ 2 = 1. The random choice model selects subgoals uniformly at random which corresponds to a special case of the two-stage choice model with fixed parameter _β_ 1 = 0. 

## **Resource-Rational Task Decomposition** 

The model predictions for a state _s_ are the value of a task decomposition (Eq 3) where the state is a single subgoal, _V_ ( _Z_ ) = _V_ ( _{s}_ ). 

## **Random Walk** 

The search algorithm returns a plan _π_ = _⟨s_ 0 _, s_ 1 _, ..., z⟩_ and run-time _t_ = _|π|_ with probability _P_ `RW` ( _π, t | s, z_ ) =[�] _i>_ 0 _N_ (1 _si_ )[.][Since][we][defined][the][reward][for][a][plan][as] _[R]_[(] _[π]_[) =] _[ −|][π][|]_[,][the][expected][reward] over all plans is 

**==> picture [170 x 51] intentionally omitted <==**

Since a constant multiplier does not affect model predictions, we drop the constant and let _R_ `RW` ( _s, z_ ) = _−_[�] _π,t[P]_ `[RW]`[(] _[π, t][ |][ s, z]_[)] _[|][π][|]_[.] The negative expected reward _−R_ `RW` ( _s, z_ ) is the expected number of steps until the first visit to _z_ when starting at _s_ , also called the hitting time _H_ ( _s, z_ ). _H_ ( _s, z_ ) can be efficiently computed by a recursive equation 

**==> picture [158 x 29] intentionally omitted <==**

when _s ̸_ = _z_ , and with _H_ ( _s, s_ ) = 0 otherwise. We thus define _R_ `RW` ( _s, z_ ) = _−H_ ( _s, z_ ). 

19 

Since the use of subgoals will either maintain or increase the number of steps required to reach a goal for a random walk, we make note of implementation differences to accommodate this for RRTD-RW. Formally stated, _H_ ( _s, s[′]_ ) + _H_ ( _s[′] , s[′′]_ ) _≥ H_ ( _s, s[′′]_ ), with _H_ ( _s, s[′]_ ) + _H_ ( _s[′] , s[′′]_ ) = _H_ ( _s, s[′′]_ ) only when all state sequences from _s_ to _s[′′]_ must contain _s[′]_ . So, states _s[′]_ with _H_ ( _s, s[′]_ ) + _H_ ( _s[′] , s[′′]_ ) _> H_ ( _s, s[′′]_ ) will only increase the expected number of steps and would not be in the policy over subgoals defined by Eq 2. To avoid this issue, we require the subgoal policy for RRTD-RW to contain at least one subgoal. By the same argument, a second subgoal can not decrease the expected number of steps, so we can simplify Eq 2 for RRTD-RW to 

**==> picture [315 x 16] intentionally omitted <==**

or when the subgoals are a singleton set _Z_ = _{z}_ simply _VZ[g]_[(] _[s]_[) =] _[ −]_[[] _[H]_[(] _[s, z]_[) +] _[ H]_[(] _[z, g]_[)].] 

## **Depth-first Search** 

The algorithm is recursively defined to take a current state _s_ and plan-so-far _π_ . At each call of the algorithm, it iterates over neighbors of the current state _s[′] ∈N_ ( _s_ )—if the state _s[′]_ is not in the current plan _π_ then there is a recursive call to the algorithm with state _s[′]_ and an updated plan _π[′]_ that ends with _s[′]_ . When there are no unvisited neighbors _s[′]_ to consider, the algorithm backtracks to a previous state and plan until it finds one with unvisited neighbors. When the algorithm reaches the subgoal _z_ , it terminates, returning the plan and a run-time based on the number of calls to the algorithm. To avoid bias due to neighbor order, in each call of the algorithm neighbors are randomly shuffled. 

## **Breadth-first Search** 

The algorithm has a queue of states to visit and tracks all states that have been visited. At each iteration, it visits the next state _s_ from the queue, and adds all not-yet-visited neighbors _s[′] ∈N_ ( _s_ ) to the queue. When it visits the subgoal _z_ , it returns the path to _z_ and a run-time based on the number of iterations that were required. As in DFS, we shuffle the neighbors of the current state at each iteration to avoid bias due to neighbor order. 

## **Iterative Deepening Depth-first search** 

A depth-limited DFS augments a standard DFS by terminating when the current “depth” (i.e. the length of the current plan) exceeds a limit, in addition to terminating when the goal is reached. IDDFS iterates by running depth-limited DFS with incrementally larger depths, starting from a depth limit of 1. The algorithm returns when a depth-limited DFS finds a plan to the goal, counting the run-time as the number of recursive DFS calls across all uses of depth-limited DFS. As in other algorithms, neighbors are shuffled to avoid bias due to order. 

## **Alternative Models** 

## **Degree Centrality, Betweenness Centrality** 

Both centrality measures were computed in the Python programming language using the `networkx` library with all parameters left at their defaults except for `endpoints=True` for Betweenness Centrality. As computed by `networkx` , both centrality measures are a fraction—for a given state _s_ , Degree Centrality is proportional to the fraction of states that _s_ is connected to and Betweenness Centrality is the fraction of optimal paths that _s_ is part of. Thus, for both measures, we define the model predictions as the logarithm of these fractions for the reasons noted above. 

## **QCut** 

This section requires more extensive use of graph theory, so we first explicitly connect the task formalism used in the remainder of the text to graphs before describing QCut. An undirected graph consists of nodes _V_ and edges _{i, j} ∈E_ between nodes _i_ and _j_ , and we let _n_ = _|V|_ and _m_ = _|E|_ . The adjacency matrix of a graph _Aij_ = 1 if _{i, j} ∈E_ and 0 otherwise. The degree of a node _i_ is _di_ =[�] _j[A][ij]_[=][ �] _i[A][ij]_[and][the][degree] 

20 

matrix _D_ = _diag_ ( _d_ ). To connect the notation used in the rest of the paper, we contextually assume the following relationship between undirected graphs and task environments: For environments with reversible actions (formally, ( _s, s[′]_ ) _∈ T ⇐⇒_ ( _s[′] , s_ ) _∈ T_ ), we let states correspond directly to graph nodes and transitions in the environment ( _s, s[′]_ ) _∈ T_ correspond to graph edges _{s, s[′] } ∈E_ . 

QCut divides the states of a graph into two groups based on the Normalized Cut criterion, which admits an approximate solution based on a spectral decomposition of the graph [Shi and Malik, 2000,Menache et al., 2002,S¸im¸sek et al., 2005]. The approximate solution to the Normalized Cut criterion is based on the symmetric graph Laplacian _L_ sym = _D[−]_[1] 2 ( _D − A_ ) _D[−]_ 2[1] = _I − D[−]_ 2[1] _AD[−]_ 2[1] . 

Following prior work [Shi and Malik, 2000,S¸im¸sek et al., 2005], we divide graph nodes into two groups based on the eigenvector _v_ with second-smallest eigenvalue of _L_ sym. This eigenvector is also the best, non-trivial one-dimensional embedding of the graph states that minimizes the distance between connected states (See Eq. 10 in [Shi and Malik, 2000]). Our implementation partitions states based on whether they are above or below a threshold in this one-dimensional embedding _v_ —a typical threshold is zero or the median. Since states _s_ with corresponding eigenvector entry _vs_ closest to the eigenvector mean are considered most central, we define the model prediction for a state _s_ as _−vs_[2][.] 

## **Solway et al. (2014)** 

Solway et al. (2014) [Solway et al., 2014] propose that people choose hierarchies that most efficiently encode problem-solving behavior. The efficiency of an encoding is quantified through the information-theoretic concept of minimum description length; when applied to encode problem-solving behavior through hierarchical structure, this involves choosing a task decomposition so that solutions have short description length and are composed of subtasks whose solutions can be reused in many tasks. This account takes optimal paths as the behavior to encode and selects hierarchies based on graph partitions. 

We now note our implementation details that depart from those of Solway et al. To predict behavioral choices, we use the optimal behavioral hierarchy to specify a binary regressor that takes a value of 1 for _boundary states_ (states with with at least one neighbor in a different region) and 0 otherwise—we discuss this choice in the main text. Since multiple state sequences can be optimal, random noise is added to graph edges for the purpose of tie-breaking—in our implementation, the description length of behavior is averaged across 10 samplings of these edge weights in order to reduce the effects of noise. In the original publication, optimization over partitions based on model evidence was performed using a genetic algorithm—in our implementation, we enumerate all graph partitions and select those with highest model evidence. For a given graph, the original article considers all possible partitions—for our analyses over eight-node graphs, we found it necessary to exclude trivial partitions. So, when possible for a graph, we only considered partitions with at least two regions and required that each region contained at least one state that was not a boundary state. The description length of behavior (the “model evidence”) was computed using R code supplied by Alec Solway. 

## **Tomov et al. (2020)** 

Tomov et al. (2020) [Tomov et al., 2020] propose an account of task decomposition as inference over hierarchical structure. Their generative model of hierarchical structure assumes partitions are drawn from a Chinese Restaurant Process and additionally assumes that edges between states are more likely when the states are in the same region. Their model also incorporates terms related to the task distribution and reward function that we expect to have minimal impact on our results because we do not vary the task distribution and the reward function for our task is a constant. 

To incorporate this model, we used the analysis in the “Simulation Two: Bottleneck States” section in the publication [Tomov et al., 2020]. The analysis models participants ( _N_ = 40) as sampling from a generative model over hierarchical graphs, then randomly sampling subgoals (three per participant) from the states connected to a “bridge” edge, which connect distinct regions in the hierarchical graph. Notably, pairs of regions are connected by a single “bridge” edge—this is subtly different from standard graph partitions, where different regions can be connected by any number of edges. All parameters were left as reported in the publication [Tomov et al., 2020], with the exception of choice stochasticity _ϵ_ which we made entirely deterministic by setting _ϵ_ = 1 _._ 0. To implement the published analyses, we used the publicly available code at 

21 

. We define the model prediction as the logarithm of the number of times a subgoal was sampled by this procedure—to avoid issues where a subgoal isn’t sampled due to noise, we add 1 to the subgoal counts before taking the logarithm. 

## **Appendix** 

## **A formal relationship between QCut and RRTD-RW** 

We prove a formal relationship between QCut and RRTD-RW for tasks based on undirected graphs. We show that a low-rank spectral approximation of RRTD-RW is equivalent to QCut for regular graphs. We use the notation introduced in the main text, recapitulated briefly here. An undirected graph has nodes _V_ and edges _{i, j} ∈E_ between nodes _i_ and _j_ . We define _n_ = _|V|_ and _m_ = _|E|_ . The adjacency matrix _Aij_ = 1 if _{i, j} ∈E_ and 0 otherwise. The degree of a node _i_ is _di_ =[�] _j[A][ij]_[=][ �] _i[A][ij]_[and][the][degree][matrix] _D_ = _diag_ ( _d_ ). For simplicity, we assume a uniform distribution over tasks _p_ ( _s_ 0 _, g_ ) = _|S|_ 1[2][and][optimize][for] single subgoals _z_ , so that _Z_ = _{z}_ . 

To start, we introduce notation from [Lov´asz, 1993] for the spectral definition of the hitting time. The matrix _N_ = _D[−]_ 2[1] _AD[−]_[1] 2 is symmetric, so it can be decomposed into eigenvalues _λk_ and eigenvectors _vk_ in the definition _N_ =[�] _[n] k_ =1 _[λ][k][v][k][v] k[T]_[,][with][1 =] _[ λ]_[1] _[> λ]_[2] _[≥· · · ≥][λ][n][≥−]_[1.][We][denote][the] _[i][th]_[element][of][an] eigenvector _vk_ as _vki_ . The hitting time _H_ ( _s, z_ ) can be computed using this spectral decomposition of _N_ [Lov´asz, 1993]—the hitting time from a state _s_ to _z_ and back from _z_ to _s_ is 

**==> picture [223 x 30] intentionally omitted <==**

Since we assume a uniform distribution over tasks, we can simplify the value of task decomposition _V_ ( _Z_ ) using the special case of _VZ[g]_[(] _[s]_[0][)][for][RRTD-RW][in][Eq][4.] 

**==> picture [182 x 119] intentionally omitted <==**

Having simplified, we can straightforwardly incorporate the spectral form of the hitting time. 

**==> picture [335 x 29] intentionally omitted <==**

We now apply this definition to develop a formal justification for QCut. 

## **Justifying the choice of eigenvector in QCut** 

To approximate _V_ ( _Z_ ) using a single eigenvector, a reasonable choice is _v_ 2 since it has largest weight 1 _−_ 1 _λk_[.] We can compare this choice of eigenvector to that of QCut, since the matrices _N_ and _L_ sym share eigenvectors because _L_ sym = _I − N_ . The eigenvalues _ek_ of _L_ sym are _ek_ = 1 _− λk_ with 0 = _e_ 1 _< e_ 2 _≤· · · ≤ en ≤_ 2, since 

22 

_L_ sym _vk_ = ( _I − N_ ) _vk_ = (1 _− λk_ ) _vk_ . The QCut algorithm makes use of the eigenvector of _L_ sym with second smallest eigenvalue [Shi and Malik, 2000,S¸im¸sek et al., 2005]—the second smallest eigenvalue is _e_ 2, which 1 means the eigenvector used by QCut is _v_ 2. Our approximation of _V_ ( _Z_ ) based on the weight 1 _−λk_[thus] provides an informal rationale for the choice of eigenvector _v_ 2 in QCut. To provide a rationale for the threshold used in QCut, we further simplify this equation for regular graphs. 

## **Justifying QCut thresholding in regular graphs** 

We can further connect RRTD-RW and QCut by limiting our consideration to regular graphs. We let _d_ be the degree of nodes in a regular graph. For regular graphs, note that _L_ = _I − D[−]_[1] _A_ = _L_ sym. 

We first establish a helpful lemma: for each eigenvector _vk_ of _L_ ,[�] _s[v][ks]_[= 0.][Note][that][in][general][for] matrices _M_ where the columns _j_ sum to zero (formally,[�] _i[M][ij]_[= 0),][it][is][the][case][that] � _i_[(] _[Mv]_[)] _[i]_[=][ �] _i,j[M][ij][v][j]_[=][ �] _j[v][j]_ � _i[M][ij]_[= 0.][The][columns] _[j]_[of] _[L]_[sum][to][zero,][since] � _i[L][ij]_[=][ �] _i_ � _I − D[−]_[1] _A_ � _ij_[= 1] _[ −] d_[1] � _i[A][ij]_[= 0.][So,][we][know][that][�] _s_[(] _[L][v]_[)] _[s]_[= 0.][In][particular,] � _s_[(] _[L][v][k]_[)] _[s]_[=][ �] _s[e][k][v][ks]_[= 0,][so][�] _s[v][ks]_[= 0.] We can now further simplify the above expression for _V_ ( _Z_ ) since the _vk_ are unit vectors and[�] _s[v][ks]_[= 0] by the above lemma. 

**==> picture [211 x 95] intentionally omitted <==**

Based on the rationale in the previous section, we can approximate this expression using a single eigenvector _v_ 2 as _V_[˜] ( _Z_ ) _∝−v_ 2[2] _z_[.][This][expression][is][maximized][by][subgoals][with][corresponding][eigenvector] entry closest to 0. In QCut, states are partitioned based on a threshold of their entry in an eigenvector—typically, values of 0 or the median are used. 

Altogether, these results establish a connection between RRTD-RW and QCut. We assume a uniform task distribution, rank-one approximation based on the weight 1 _−_ 1 _λk_[,][and][that][a][graph][is][regular.][With][these] assumptions, we can give a rationale for QCut that uses _v_ 2 with a threshold of 0. Connections between graph spectra, spectral clustering, and random walks have been noted in passing in previous research [Stachenfeld et al., 2017,Von Luxburg, 2007,Shi and Malik, 2000], though the authors are not aware of a result directly relating the models considered in this section. 

## **Explaining the relationship between RRTD-RW and Degree Centrality** 

The plot in Fig 3 validates our formal analysis by demonstrating an empirical result of modest correlation between QCut and RRTD-RW. However, Degree Centrality and RRTD-RW exhibit an even higher correlation which we examine in this section. A critical step in our above proof relating QCut and RRTD-RW requires a rank-one, spectral approximation to RRTD-RW. We examine how this approximation influences the relationships between models as the rank of the approximation is varied in Fig 9a, using this variant of Eq 5 to compute a rank- _k[′]_ spectral approximation of RRTD-RW: 

**==> picture [220 x 31] intentionally omitted <==**

We find that the relationship between QCut and RRTD-RW is highest when RRTD-RW is approximated with a single eigenvector, which is consistent with the rank-one approximation necessary in the proof. The 

23 

**==> picture [435 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
0.9<br>0.8<br>0.7<br>QCut<br>Degree Cent. (log)<br>0.6<br>0.5<br>0.4<br>(a) (b)<br>RRTD-RW (rank 1)RRTD-RW (rank 2)RRTD-RW (rank 3)RRTD-RW (rank 4)RRTD-RW (rank 5)RRTD-RW (rank 6)RRTD-RW (full rank)<br>Model Correlations<br>**----- End of picture text -----**<br>


**Figure 9.** a) Correlation of two models (QCut in blue and Degree Centrality in orange) plotted as a function of rank of a spectral approximation to RRTD-RW using the below formula for rank- _k[′]_ spectral approximation. Correlations were computed as in Fig 3. b) Bivariate histogram of the 11,117 eight-node graphs based on the spectral gap (1 - _λ_ 2) and correlation between Degree Centrality and RRTD-RW. A small spectral gap is associated with the existence of a bottleneck, explaining the relative decrease in Degree Centrality/RRTD-RW correlation for those values. 

correlation between QCut and RRTD-RW is also only higher than the correlation between Degree Centrality and RRTD-RW for the rank-one approximation. For ranks greater than one, Degree Centrality has the highest correlation to RRTD-RW, with maximum correlation to the full-rank RRTD-RW. 

To conclude, we briefly and informally interpret the correlation between Degree Centrality and RRTD-RW by using the spectral gap _λ_ 1 _− λ_ 2 = 1 _− λ_ 2 as a characterization of graph modularity. The spectral gap can be bounded by the Cheeger constant [Lov´asz, 1993], a graph theoretic property related to the modularity of a graph—because of this connection, we will informally interpret the spectral gap as we would the Cheeger constant. In graphs with a small spectral gap, we expect more modularity with sparse connectivity between groups. In graphs with a large spectral gap, we expect the absence of obvious groups because of dense connectivity. In Fig 9b we plot the correlation between Degree Centrality and RRTD-RW against the spectral gap as a bivariate histogram. In graphs with large spectral gaps, we find that Degree Centrality and RRTD-RW are very correlated—This is consistent with intuitive predictions for a densely connected graph, where the most useful subgoals are those with higher degree because this means they are well-connected. In graphs with small spectral gaps, we find that Degree Centrality and RRTD-RW tend to be less correlated with greater variability. This is consistent with intuitive predictions for a modular graph, where a well-connected subgoal is less useful than a bottleneck. 

## **Acknowledgments** 

This work was funded by John Templeton Foundation grant 61454, U.S. Air Force Office of Scientific Research grant FA 9550-18-1-0077, and U.S. Army Research Office ARO W911NF-16-1-0474. 

## **References** 

- Balaguer et al., 2016. Balaguer, J., Spiers, H., Hassabis, D., and Summerfield, C. (2016). Neural mechanisms of hierarchical planning in a virtual subway network. _Neuron_ , 90(4):893 – 903. 

Bellman, 1957a. Bellman, R. (1957a). _Dynamic programming_ . Princeton University Press. 

Bellman, 1957b. Bellman, R. (1957b). _Dynamic programming_ . Princeton University Press. 

Botvinick et al., 2009. Botvinick, M. M., Niv, Y., and Barto, A. G. (2009). Hierarchically organized behavior and its neural foundations: a reinforcement learning perspective. _Cognition_ , 113(3):262–280. 

24 

- Callaway et al., 2022. Callaway, F., van Opheusden, B., Gul, S., Das, P., Krueger, P. M., Lieder, F., and Griffiths, T. L. (2022). Rational use of cognitive resources in human planning. _Nature Human Behaviour_ , 6(8):1112–1125. 

- Collins and Frank, 2013. Collins, A. G. and Frank, M. J. (2013). Cognitive control over learning: Creating, clustering, and generalizing task-set structure. _Psychological Review_ , 120(1):190–229. 

- Correa et al., 2020. Correa, C. G., Ho, M. K., Callaway, F., and Griffiths, T. L. (2020). Resource-rational task decomposition to minimize planning costs. In _Proceedings of the 42nd Annual Conference of the Cognitive Science Society_ . 

- S¸im¸sek et al., 2005. S¸im¸sek, O.,[¨] Wolfe, A. P., and Barto, A. G. (2005). Identifying useful subgoals in reinforcement learning by local graph partitioning. In Proceedings of the 22nd International Conference on Machine Learning. 

- Cushman and Morris, 2015. Cushman, F. and Morris, A. (2015). Habitual control of goal selection in humans. _Proceedings of the National Academy of Sciences_ , 112(45):13817–13822. 

- De Groot, 1965. De Groot, A. D. (1965). _Thought and choice in chess_ . Mouton Publishers. 

- Donnarumma et al., 2016. Donnarumma, F., Maisto, D., and Pezzulo, G. (2016). Problem solving as probabilistic inference with subgoaling: explaining human successes and pitfalls in the tower of hanoi. _PLoS computational biology_ , 12(4):e1004864. 

- Eckstein and Collins, 2020. Eckstein, M. K. and Collins, A. G. (2020). Computational evidence for hierarchically structured reinforcement learning in humans. _Proceedings of the National Academy of Sciences_ , 117(47):29381–29389. 

- Gershman et al., 2015a. Gershman, S. J., Horvitz, E. J., and Tenenbaum, J. B. (2015a). Computational rationality: A converging paradigm for intelligence in brains, minds, and machines. _Science_ , 349(6245):273–278. 

- Gershman et al., 2015b. Gershman, S. J., Horvitz, E. J., and Tenenbaum, J. B. (2015b). Computational rationality: A converging paradigm for intelligence in brains, minds, and machines. _Science_ , 349(6245):273–278. 

- Ghallab et al., 2016. Ghallab, M., Nau, D., and Traverso, P. (2016). _Automated planning and acting_ . Cambridge University Press. 

- Griffiths et al., 2015. Griffiths, T. L., Lieder, F., and Goodman, N. D. (2015). Rational Use of Cognitive Resources: Levels of Analysis Between the Computational and the Algorithmic. _Topics in Cognitive Science_ , 7(2):217–229. 

- Harb et al., 2018. Harb, J., Bacon, P.-L., Klissarov, M., and Precup, D. (2018). When waiting is not an option: Learning options with a deliberation cost. Thirty-Second AAAI Conference on Artificial Intelligence. 

- Huys et al., 2012. Huys, Q. J. M., Eshel, N., O’Nions, E., Sheridan, L., Dayan, P., and Roiser, J. P. (2012). Bonsai trees in your head: how the pavlovian system sculpts goal-directed choices by pruning decision trees. _PLOS Computational Biology_ , 8(3):e1002410. 

- Huys et al., 2015. Huys, Q. J. M., Lally, N., Faulkner, P., Eshel, N., Seifritz, E., Gershman, S. J., Dayan, P., and Roiser, J. P. (2015). Interplay of approximate planning strategies. _Proceedings of the National Academy of Sciences_ , 112(10):3098–3103. 

- Jinnai et al., 2019. Jinnai, Y., Abel, D., Hershkowitz, D. E., Littman, M., and Konidaris, G. (2019). Finding options that minimize planning time. In Proceedings of the 36th International Conference on Machine Learning. 

25 

- Korf, 1985a. Korf, R. E. (1985a). Depth-first iterative-deepening: An optimal admissible tree search. _Artificial intelligence_ , 27(1):97–109. 

- Korf, 1985b. Korf, R. E. (1985b). _Learning to Solve Problems by Searching for Macro-Operators_ . Pitman Publishers. 

- Lewis et al., 2014. Lewis, R. L., Howes, A., and Singh, S. (2014). Computational rationality: Linking mechanism and behavior through bounded utility maximization. _Topics in Cognitive Science_ , 6(2):279–311. 

- Lieder and Griffiths, 2020a. Lieder, F. and Griffiths, T. L. (2020a). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. _Behavioral and Brain Sciences_ , 43. 

- Lieder and Griffiths, 2020b. Lieder, F. and Griffiths, T. L. (2020b). Resource-rational analysis: understanding human cognition as the optimal use of limited computational resources. _Behavioral and Brain Sciences_ , pages 1–60. 

- Lieder et al., 2014. Lieder, F., Plunkett, D., Hamrick, J. B., Russell, S. J., Hay, N., and Griffiths, T. (2014). Algorithm selection by rational metareasoning as a model of human strategy selection. Advances in Neural Information Processing Systems 28. 

- Lov´asz, 1993. Lov´asz, L. (1993). Random walks on graphs: a survey. In Mikl´os, D., S´os, V. T., and Sz¨onyi, T., editors, _Combinatorics, Paul Erd¨os is Eighty_ , volume 2, pages 353–397, Budapest. J´anos Bolyai Math Society. 

- Maisto et al., 2015. Maisto, D., Donnarumma, F., and Pezzulo, G. (2015). Divide et impera: subgoaling reduces the complexity of probabilistic inference and problem solving. _Journal of The Royal Society Interface_ , 12(104):20141335–20141335. 

- McNamee et al., 2016. McNamee, D., Wolpert, D. M., and Lengyel, M. (2016). Efficient state-space modularization for planning: theory, behavioral and neural signatures. Advances in Neural Information Processing Systems 30. 

- Menache et al., 2002. Menache, I., Mannor, S., and Shimkin, N. (2002). Q-cut—dynamic discovery of sub-goals in reinforcement learning. European conference on machine learning. 

- Newell and Simon, 1972a. Newell, A. and Simon, H. A. (1972a). _Human problem solving_ . Prentice-Hall. 

- Newell and Simon, 1972b. Newell, A. and Simon, H. A. (1972b). _Human problem solving_ . Prentice-Hall, Englewood Cliffs, NJ. 

- Puterman, 1994. Puterman, M. L. (1994). _Markov Decision Processes: Discrete Stochastic Dynamic Programming_ . John Wiley & Sons, Inc. 

- Ramkumar et al., 2016. Ramkumar, P., Acuna, D. E., Berniker, M., Grafton, S. T., Turner, R. S., and Kording, K. P. (2016). Chunking as the result of an efficiency computation trade-off. _Nature communications_ , 7(1):1–11. 

- Russell and Norvig, 2009. Russell, S. and Norvig, P. (2009). _Artificial Intelligence: A Modern Approach_ . Prentice Hall Press, USA, 3rd edition. 

- Sacerdoti, 1974a. Sacerdoti, E. D. (1974a). Planning in a hierarchy of abstraction spaces. _Artificial intelligence_ , 5(2):115–135. 

- Sacerdoti, 1974b. Sacerdoti, E. D. (1974b). Planning in a hierarchy of abstraction spaces. _Artificial Intelligence_ , 5(2):115–135. 

- Shi and Malik, 2000. Shi, J. and Malik, J. (2000). Normalized cuts and image segmentation. _IEEE Transactions on pattern analysis and machine intelligence_ , 22(8):888–905. 

26 

- S¸im¸sek and Barto, 2009. S¸im¸sek, O.[¨] and Barto, A. G. (2009). Skill characterization based on betweenness. Advances in Neural Information Processing Systems 23. 

- Solway et al., 2014. Solway, A., Diuk, C., C´ordova, N., Yee, D., Barto, A. G., Niv, Y., and Botvinick, M. M. (2014). Optimal behavioral hierarchy. _PLOS Computational Biology_ , 10(8):1–10. 

- Stachenfeld et al., 2017. Stachenfeld, K. L., Botvinick, M. M., and Gershman, S. J. (2017). The hippocampus as a predictive map. _Nature Neuroscience_ , 20(11):1643–1653. 

- Sutton et al., 1999. Sutton, R. S., Precup, D., and Singh, S. (1999). Between mdps and semi-mdps: A framework for temporal abstraction in reinforcement learning. _Artificial intelligence_ , 112(1-2):181–211. 

- Tomov et al., 2020. Tomov, M. S., Yagati, S., Kumar, A., Yang, W., and Gershman, S. J. (2020). Discovery of hierarchical representations for efficient planning. _PLOS Computational Biology_ , 16(4):1–42. 

- Von Luxburg, 2007. Von Luxburg, U. (2007). A tutorial on spectral clustering. _Statistics and computing_ , 17(4):395–416. 

27 

