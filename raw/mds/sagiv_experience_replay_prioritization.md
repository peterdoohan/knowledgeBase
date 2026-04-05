## **Prioritizing experience replay when future goals are unknown** 

**Yotam Sagiv Thomas Akam** Princeton Neuroscience Institute Department of Experimental Psychology Princeton University Oxford University Princeton, NJ 08544 Oxford OX1 3SR United States of America United Kingdom ysagiv@princeton.edu thomas.akam@psy.ox.ac.uk 

**Ilana B. Witten Nathaniel D. Daw** Princeton Neuroscience Institute Princeton Neuroscience Institute Princeton University Princeton University Princeton, NJ 08544 Princeton, NJ 08544 United States of America United States of America iwitten@princeton.edu ndaw@princeton.edu 

## **Abstract** 

The ability to connect actions to their long-term consequences is key for intelligent behavior. In both neuroscience and AI, significant attention has been paid to experience replay as a mechanism by which this might be accomplished. Much of this work has envisioned replay as used to compute long-run returns, linking states and actions to their expected future rewards. In neuroscience, such value computation has been proposed to be a function of nonlocal “replay” of spatial trajectories in the hippocampus. Specifically, many findings about which trajectories are replayed in which circumstances are well explained by a rational prioritization account, in which locations are preferentially replayed when this would be most useful for computing future value. 

However, an alternative view of replay in neuroscience is that it is not specifically tied to propagating reward information, but instead involved in developing environmental models (e.g., of routes and barriers), called “cognitive maps.” Furthermore, researchers in both neuroscience and AI increasingly appreciate the importance of flexible transfer learning, such as by decomposing an (inflexible and task-specific) value function into components such as the successor representation that allow reusing computations to compute new policies when some elements of the task (such as reward location) change. 

Here we extend the notion of prioritized replay for value function computation to one in which the goal is computing a successor-representation-like long-run future occupancy map of the environment, when the reward function is unknown or may be expected to change in the future. This requires defining a prioritization rule that evaluates backups in terms of a distribution over possible future goal locations, rather than with respect to the current reward function. We derive such a rule and show that it yields coherent replay sequences in a variety of contexts. 

**Keywords:** Reinforcement learning; experience replay; transfer; navigation 

## **Acknowledgements** 

This work was supported by the John Templeton Foundation, grant 61454 (ND). 

## **1 Introduction** 

A key challenge in sequential decision tasks is connecting actions to their long-run consequences, as indeed can be seen directly in the definition of the objective in terms of maximizing cumulative long-run future reward. In both neuroscience and AI, it has been suggested [4, 7] that experience replay is well-suited for this function. The key idea behind this line of work is that revisiting memories allows an agent to propagate reward information obtained from temporallyseparated experiences to compute their consequences for value at distant states. For example, this is the basis of the Dyna reinforcement learning architecture, in which an agent learns offline from experiences simulated from a worldmodel [7]. In neuroscience, Dyna-like value propagation has been proposed as a function of replay of spatial trajectories in the hippocampal place cell system. In particular, by defining a rational prioritization rule for replay (favoring replay of those locations where update steps are expected to most affect future reward), it has been shown that replay patterns advantageous for value computation explain many qualitative features of replay observed in the rodent hippocampus [4]. 

In contrast, an alternative tradition in neuroscience envisions that place cell replay is not directly tied to action planning or reward propagation, but more generally to learning something akin to a world model (usually termed a “cognitive map”). To date, this general hypothesis has not been embodied in a formal model comparable to the Dyna proposal. However, it may relate to a second area of interest in both neuroscience and AI: the ability of model-based methods to flexibly transfer experience and computation to accomplish new tasks, such as when the reward function changes. One example is the successor representation [1, 5], which, rather than learning long-run values directly, represents long-run future state occupancies, which can be combined with information about current rewards to rapidly replan when the reward function changes. Signatures of these sorts of long-run state-state predictions have been detected in the brain [2]. 

Here we extend our earlier account of prioritized replay for value function computation [4] to address the possibility of replay for building an SR-like cognitive map (SR-Dyna [5]), which may be useful for multiple future tasks. To this end, we employ a variant of the successor representation (that we call the geodesic representation, GR), which is better suited for task transfer learning because it operates off-policy [3]. Our goal is to develop a formal account of the cognitive map building hypothesis, comparable to that for value propagation, which might ultimately enable comparing their predictions in light of hippocampal replay data. We derive, from first principles, a prioritization rule for the GR analogous to the Q-value prioritization rule in [4] and show that it yields coherent replay sequences in a variety of contexts. (Note that in keeping with the previous work, we aim to define which replay trajectories are most adaptive in this setting, but leave for future work the discovery of an efficiently-realizable algorithm for discovering them.) Crucially, prioritization in this context does not depend on the current goals — indeed, the reward function may not yet be known or may be expected to change; instead, replay is evaluated with respect to a distribution over future goals. For this reason, the model predicts that replay can be worthwhile even before any rewards are observed. 

## **2 Theory** 

## **2.1 The Geodesic representation** 

For simplicity, we take as our setting the family of shortest-path problems with a single (initially unknown) goal state, though our method extends straightforwardly to maximizing an arbitrary reward function over an unknown set of terminal states. In this section we describe the Geodesic representation (GR; [3]), an off-policy variant of the successor representation (SR) that can be used to solve the shortest-path problem. We begin by first building intuition and then describe the formal framework. Consider a deterministic Markov Decision Process (MDP) with a single absorbing state _g_ . Then for any policy _π_ and state _s_ , the induced SR _M[π]_ ( _s, g_ ) measures the expected (discounted) number of time-steps it takes to reach _g_ from _s_ under _π_ . If we further assume that _g_ is the only rewarding state in this MDP, then _M[π]_ ( _s, g_ ) is equal to the value function _V[π]_ ( _s_ ) =[�] _a[π]_[(] _[a][|][s]_[)] _[Q][π]_[(] _[s, a]_[)][.][Exploiting][this,][we][can][learn][the][distance][between][any][pair] of source and target states under a given policy by considering an altered version of the underlying MDP in which the target is absorbing — the SR induced by the policy in this modified MDP is a monotonic function of the desired distance. Furthermore, we can learn optimally to navigate between those states simply by performing Q-learning in the modified MDP. In the GR, we will exploit this property; the core intuition is that we can define one of these modified MDPs for each state, treating that state as the destination, and perform Q-learning simultaneously across all of them. 

Accordingly, we define the GR: 

**==> picture [359 x 28] intentionally omitted <==**

where _γ_ is a temporal discount rate, _πg_ is the policy that is expected to reach _g_ as fast as possible (i.e., is rewardmaximizing in the modified MDP where _g_ is absorbing and rewarding), and I _•_ is the indicator function that is 1 if _•_ is true and 0 otherwise. It can be shown straightforwardly that the GR obeys a Bellman equation. Let ( _s, a, s[′]_ ) be a 

1 

transition from _s_ to _s[′]_ after taking action _a_ . Then: 

**==> picture [366 x 19] intentionally omitted <==**

Intuitively, if _s[′]_ is the goal state _g_ , then we have accrued a reward of 1 and if _s[′]_ is not, then the current value should be _γ_ times the best value at wherever we arrived[1] . This can be also written compactly in vector form: 

**==> picture [361 x 19] intentionally omitted <==**

where _⊙_ denotes the Hadamard (elementwise) product, 1 _s′_ is a one-hot vector at _s[′]_ , 0 _s′_ is a vector that is 0 at _s[′]_ and 1 everywhere else, and the max is taken separately over each goal state. 

## **2.2 Prioritizing updates to the Geodesic representation** 

Previous work considered the problem of prioritizing experience replay in Dyna models for Q value updating [4]. In particular, it was suggested that replay of a particular state-action-state event (so as to perform Q-value update, known as a Bellman backup, there) be prioritized greedily according to its expected utility, i.e. the difference between the expected return after vs. before the replay (which may increase if the replay is policy-improving). This “expected value of backup” can be decomposed as a product of a “need” term and a “gain” term. Briefly, the need term roughly corresponds to how often the agent expects to be in the updated state (i.e., the state’s relevance) and the gain term roughly corresponds to the magnitude of the change in the updated state’s value (i.e., how much more reward it expects to accrue should it be in that state by virtue of the update improving the policy). 

The GR also admits such a factorization. We begin by defining an analogue of the state-value function in the Geodesic space: 

**==> picture [330 x 22] intentionally omitted <==**

where _πg_ is the policy that tries to reach _g_ as fast as possible. It can be shown that the expected improvement in _H_ after backing up the experience _ek_ = ( _sk, ak, s[′] k_[)][ with respect to a particular goal] _[ g]_[ factorizes:] 

**==> picture [520 x 25] intentionally omitted <==**

Here, _•pre_ and _•post_ refer to _•_ before and after learning, respectively (and so, while _ak_ and _s[′] k_[are not explicitly rendered] above, they affect the equation through the differences in _•pre_ and _•post_ ). _γ_ is a temporal discounting factor, and _P_ ( _s → sk, i, πg,pre_ ) is the probability that a trajectory starting in _s_ at time 0 arrives at _sk_ at time _i_ when following policy _πg,pre_ . Intuitively, the first term after the equals sign in the top line of Equation 5 is a need term – it measures how often the agent will reach the state being updated _sk_ given their current state _s_ and their policy. In fact, it is precisely SR _M[π][pre]_ ( _s, g_ ) evaluated under the policy that tries to reach _g_ from _s_ as quickly as possible. The second term is a gain term, it quantifies roughly the how much additional reward the agent should accumulate due to a change in policy. Trivially, the second line is also a need _×_ gain factorisation, with need = 0. Roughly, we can understand this equation as saying that the utility of backing up some experience _ek_ – measured through the expected improvement _Hpost_ ( _s, g_ ) _− Hpre_ ( _s, g_ ) – is driven by 1) how relevant that experience is and 2) by the magnitude of the change induced by the update. Given this factorization, an agent may prioritize replay by picking the memory that maximizes the expected improvement from the current state _s_ averaged over all possible goals[2] : 

**==> picture [354 x 21] intentionally omitted <==**

Once an experience is picked for replay, the GR can then be updated for _all_ goals towards the target in Equation 3. 

In some cases, we may wish our agent to maximize the improvement not just from its current state, but prospectively over some distribution capturing its prior over future initial states. For example, this might arise when the agent has reasonable belief that it will start in a particular state that is different to its current one. Accounting for this is relatively straightforward. In such cases, the need term from Equation 5 is not _M[π][pre]_ ( _s, g_ ) but E _s_ 0 _M[π][pre]_ ( _s_ 0 _, g_ ) . � � 

> 1for deterministic MDPs, it can be shown that this formulation yields _G_ ( _s, a, g_ ) = _γd_ ( _s,a,g_ ), where _d_ ( _s, a, g_ ) is the expected distance from _s_ to _g_ after taking action _a_ 

> 2Inferring the distribution over goals is an interesting question by itself, but outside the scope of this article; we assume that it is known to the agent. 

2 

**==> picture [238 x 220] intentionally omitted <==**

**==> picture [238 x 220] intentionally omitted <==**

(a) Linear track (b) Open field 

**==> picture [238 x 220] intentionally omitted <==**

(c) Bottleneck chamber 

Figure 1: _Simulated prioritized Geodesic replay sequences in a variety of contexts._ Throughout all plots, time proceeds from blue to green. **(a)** 50 steps of replay simulated on a linear track. All states are considered potential goal states and the initial state distribution is uniform over the entire track. **(b)** 20 steps of replay on an open field. All states are considered potential goal states and the initial state distribution is uniform over the entire environment. **(c)** 30 steps of replay in a bottleneck chamber. The bottleneck chamber is comprised of two rooms connected by a corridor. Inaccessible states are shaded black. Only the top- and bottom-right corners are considered potential goals and the state marked with a red ‘x’ is known to be the initial state. 

Finally, we briefly note a special case of the above computation. If the current step _ek_ is an optimal continuation of the previous step _ek−_ 1 with respect to _g_ , then we extend the one-step replay to a two-step replay (i.e., we update both _G_ ( _sk, ak, g_ ) and _G_ ( _sk−_ 1 _, ak−_ 1 _, g_ )). In general, if the previous sequence of replayed experiences constitutes an optimal ( _n −_ 1)-step trajectory towards _g_ , and _ek_ is an optimal continuation of that trajectory, we perform the full _n_ -step backup. When doing this, the need is computed identically, but the gains are added across all the updated states. This has been shown to favor coherent forward replays [4]. 

3 

## **3 Simulations** 

In this section, we examine the replay behavior of an agent given access to experiences from a variety of environments. For all environments, the agent is initialized with the full set of one-step transitions (as we are not concerned with learning the one-step adjacency structure, but with how that structure can be converted into a long-run future occupancy map), and assigned distributions over initial and goal states. 

Firstly, we examined prioritized Geodesic replay on the linear track. The agent planned prospectively over a uniform initial state distribution, and every state in the track is assigned as a possible goal. In Figure 1a, the first 50 replay steps have been plotted. Immediately, we see that replay proceeds in sequential fashion throughout the linear track. 

Next, we simulated replay in an open field (Fig. 1b. Similar to the previous case, we require the agent to plan with initial state and goal distributions that are uniform over the entire space. Plotting the first 20 steps of replay, we see that replay meanders forward, sequentially through the space. 

Finally, we reasoned that an algorithm concerned with navigation might pay special attention to bottleneck states. Accordingly, we designed an environment with clear bottleneck statistics – two rooms connected by a corridor. For this environment, we assigned the agent a single initial start state in the left room and two goal states in the far corners of the right room. Replay behavior in this case is interesting. Generally, we note that replay moves backwards from the goal states towards the initial start state. Specifically, the agent first builds independent sequences from the two goal states towards the bottleneck (the corridor entry state) and then from the bottleneck towards the start state. This order of operations allows the agent to consolidate goal information at the bottleneck (specifically, stacking the distances to each of the two goals) before pushing it back towards the start state. 

## **4 Discussion** 

We have presented a method for prioritizing replay in reward-free regimes that rests on the construct of the Geodesic representation [3], a variant of the successor representation that permits efficient learning of shortest path distances. In a variety of simulations, we have shown that this method consistently yields coherent replay sequences without the need for external specification of sequential structure. In doing so, we have provided a normative basis for sequence replay grounded in the development of a cognitive map subserving subsequent navigation. 

We expect this framework to be useful in several contexts. Firstly, it yields direct, quantitative predictions for replay dynamics in tasks where a subject is exposed to the underlying stimulus dynamics before reward is given – for example, sensory preconditioning [6] or latent graph traversal [2]. Though studies examining these behavioral paradigms have been performed, we are not aware of any that analyzed replay dynamics in the pre-reward phase. Measurements of replay in the hippocampus or prefrontal cortex during this phase would provide valuable insight into how the brain implements structure learning. Furthermore, it is possible that the Geodesic prediction error might correlate with dopaminergic activity during such learning paradigms (say, by encoding the magnitude of the GR error as a form of surprise or value-of-information signal); this is line with previous work, which has shown that dopamine is necessary for learning sensory-sensory associations even before reward has been given [6]. 

## **References** 

- [1] Peter Dayan. Improving generalization for temporal difference learning: The successor representation. _Neural Computation_ , 5(4):613–624, 1993. 

- [2] Mona M. Garvert, Raymond J. Dolan, and Timothy E.J. Behrens. A map of abstract relational knowledge in the human hippocampal–entorhinal cortex. _eLife_ , 6, April 2017. 

- [3] Leslie P. Kaelbling. Learning to achieve goals. In _Proc. of IJCAI-93_ , pages 1094–1098. Morgan Kaufmann, 1993. 

- [4] Marcelo G. Mattar and Nathaniel D. Daw. Prioritized memory access explains planning and hippocampal replay. _Nature Neuroscience_ , 21(11):1609–1617, November 2018. 

- [5] Evan M. Russek, Ida Momennejad, Matthew M. Botvinick, Samuel J. Gershman, and Nathaniel D. Daw. Predictive representations can link model-based reinforcement learning to model-free mechanisms. _PLOS Computational Biology_ , 13(9), September 2017. 

- [6] Melissa J. Sharpe, Chun Yun Chang, Melissa A. Liu, Hannah M. Batchelor, Lauren E. Mueller, Joshua L. Jones, Yael Niv, and Geoffrey Schoenbaum. Dopamine transients are sufficient and necessary for acquisition of model-based associations. _Nature Neuroscience_ , 20(5):735–742, May 2017. 

- [7] Richard S. Sutton. Integrated architectures for learning, planning, and reacting based on approximating dynamic programming. In _Machine Learning Proceedings 1990_ , pages 216–224. Morgan Kaufmann, San Francisco (CA), 1990. 

4 

