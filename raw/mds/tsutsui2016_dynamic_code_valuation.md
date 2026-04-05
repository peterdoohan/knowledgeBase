# **Successor Feature Landmarks for Long-Horizon Goal-Conditioned Reinforcement Learning** 

**Christopher Hoang**[1] **Sungryull Sohn**[1][2] **Jongwook Choi**[1] **Wilka Carvalho**[1] **Honglak Lee**[1][2] 

1University of Michigan 2LG AI Research { `choang, srsohn, jwook, wcarvalh, honglak` } `@umich.edu` 

## **Abstract** 

Operating in the real-world often requires agents to learn about a complex environment and apply this understanding to achieve a breadth of goals. This problem, known as goal-conditioned reinforcement learning (GCRL), becomes especially challenging for long-horizon goals. Current methods have tackled this problem by augmenting goal-conditioned policies with graph-based planning algorithms. However, they struggle to scale to large, high-dimensional state spaces and assume access to exploration mechanisms for efficiently collecting training data. In this work, we introduce Successor Feature Landmarks (SFL), a framework for exploring large, high-dimensional environments so as to obtain a policy that is proficient for any goal. SFL leverages the ability of successor features (SF) to capture transition dynamics, using it to drive exploration by estimating state-novelty and to enable high-level planning by abstracting the state-space as a non-parametric landmarkbased graph. We further exploit SF to directly compute a goal-conditioned policy for inter-landmark traversal, which we use to execute plans to “frontier” landmarks at the edge of the explored state space. We show in our experiments on MiniGrid and ViZDoom that SFL enables efficient exploration of large, high-dimensional state spaces and outperforms state-of-the-art baselines on long-horizon GCRL tasks[1] . 

## **1 Introduction** 

Consider deploying a self-driving car to a new city. To be practical, the car should be able to explore the city such that it can learn to traverse from any starting location to any destination, since the destination may vary depending on the passenger. In the context of reinforcement learning (RL), this problem is known as goal-conditioned RL (GCRL) [12, 13]. Previous works [31, 1, 24, 26, 17] have tackled this problem by learning a goal-conditioned policy (or value function) applicable to any reward function or “goal.” However, the goal-conditioned policy often fails to scale to long-horizon goals [11] since the space of state-goal pairs grows intractably large over the horizon of the goal. 

for any state-goal pair it might observe during test time and (b) reduce the effective goal horizon for the policy learning to be tractable. Recent work [25, 11] has tackled long-horizon GCRL by leveraging model-based approaches to form plans consisting of lower temporal-resolution subgoals. The policy is then only required to operate for short horizons between these subgoals. One line of work learned a universal value function approximator (UVFA) [31] to make local policy decisions and to estimate distances used for building a landmark-based map, but assumed a low-dimensional state space where the proximity between the state and goal could be computed by the Euclidean distance [11]. Another line of research focused on visual navigation tasks conducted planning over 

> 1 The demo video and code can be found at `https://2016choang.github.io/sfl` . 

35th Conference on Neural Information Processing Systems (NeurIPS 2021) 

**==> picture [358 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
1. Select frontier 2. Plan path to  3. Execute planned path with<br>landmark frontier landmark goal-conditioned policy<br>Initial state<br>Landmarks<br>Frontier landmark<br>Planned Path<br>Explored region<br>Planned path<br>Edge<br>Goal-conditioned policy<br>5. Update graph + SF<br>with trajectory Random policy<br>Trajectory<br>Graph<br>+  Graph + SF 4. Use random policy<br>Update  to explore<br>**----- End of picture text -----**<br>


Figure 1: High-level overview of SFL. **1.** During _exploration_ , select a frontier landmark (red circled dot) lying at the edge of the explored region as the target goal. During _evaluation_ (not shown in the figure), the actual goal is selected as the target goal. **2.** Use the graph to plan a landmark path (green lines) to the target goal. **3.** Execute the planned path with the goal-conditioned policy (black dotted arrow). **4.** During _exploration_ , upon reaching the frontier landmark, deploy the random policy (red dotted arrow) to reach novel states in unexplored areas. **5.** Use each transition in the trajectory to update the graph and SF (see Figure 2). **Note:** The agent is never shown the top-down view of the maze and only uses first-person image observations (example on left) to carry out these steps. Goals are also given as first-person images. 

graph representations of the environment [29, 9, 16, 4]. However, these studies largely ignored the inherent exploration challenge present for large state spaces, and either assumed the availability of human demonstrations of exploring the state space [29], the ability to spawn uniformly over the state space [9, 16], or the availability of ground-truth map information [4]. 

In this work, we aim to learn an agent that can tackle long-horizon GCRL tasks and address the associated challenges in exploration. Our key idea is to use successor features (SF) [15, 2] — a representation that captures transition dynamics — to define a novel distance metric, Successor Feature Similarity (SFS). First, we exploit the transfer ability of SF to formulate a goal-conditioned value function in terms of SFS between the current state and goal state. By just learning SF via self-supervised representation learning, we can directly obtain a goal-conditioned policy from SFS without any additional policy learning. Second, we leverage SFS to build a landmark-based graph representation of the environment; the agent adds observed states as landmarks based on their SFSpredicted novelty and forms edges between landmarks by using SFS as a distance estimate. SF as an abstraction of transition dynamics is a natural solution for building this graph when we consider the MDP as a directed graph of states (nodes) and transitions (edges) following [11]. We use this graph to systematically explore the environment by planning paths towards landmarks at the “frontier” of the explored state space and executing each segment of these planned paths with the goal-conditioned policy. In evaluation, we similarly plan and execute paths towards (long-horizon) goals. We call this framework _Successor Feature Landmarks_ (SFL), illustrated in Figure 1. 

Our contributions are as follows: (i) We use a single self-supervised learning component that captures dynamics information, SF, to build all the components of a graph-based planning framework, SFL. (ii) We claim that this construction enables knowledge sharing between each module of the framework and stabilizes the overall learning. (iii) We introduce the SFS metric, which serves as a distance estimate and enables the computation of a goal-conditioned Q-value function _without further learning_ . We evaluate SFL against current graph-based methods in long-horizon goal-reaching RL and visual navigation on **MiniGrid** [6], a 2D gridworld, and **ViZDoom** [37], a visual 3D first-person view environment with large mazes. We observe that SFL outperforms state-of-the-art navigation baselines, most notably when goals are furthest away. In a setting where exploration is needed to collect training experience, SFL significantly outperforms the other methods which struggle to scale in **ViZDoom** ’s high-dimensional state space. 

2 

## **2 Related Work** 

**Goal-conditioned RL** . Prior work has tackled GCRL by proposing variants of goal-conditioned value functions such as UVFAs which estimate cumulative reward for any given state-goal pair [23, 34, 31, 26]. HER [1] improved the sample efficiency in training UVFAs by relabeling reached states as goals. Mapping State Space (MSS) [11] then extended UVFAs to long-horizon tasks by using a UVFA as both a goal-conditioned policy and a distance metric to build a graph for high-level planning. MSS also addressed exploration by selecting graph nodes to be at edge of the map’s explored region via farthest point sampling. However, this method was only evaluated in low-dimensional state spaces. LEAP [25] used goal-conditioned value functions to form and execute plans over latent subgoals, but largely ignored the exploration question. Conversely, other works [27, 5] have worked on exploration for goal-reaching policies, but do not tackle the long-horizon case. ARC [10] proposed learning representations that measure state similarity according to the output of a maximum entropy goal-conditioned policy, which can be utilized towards exploration and long-horizon hierarchical RL. However, ARC assumes access to the goal-conditioned policy, which can be difficult to obtain in large-scale environments. Our method can achieve both efficient exploration and long-horizon goal-reaching in high-dimensional state spaces with a SF-based metric that acts as a goal-conditioned value function and distance estimate for graph-building. 

**Graph-based planning.** Recent approaches have tackled long-horizon tasks, often in the context of visual navigation, by conducting planning on high-level graph representations and deploying a low-level controller to locally move between nodes; our framework also falls under this paradigm of graph-based planning. Works such as SPTM [29] and SoRB [9] used a deep network as a distance metric for finding shortest paths on the graph, but rely on human demonstrations or sampling from the replay buffer to populate graph nodes. SGM [16] introduced a two-way consistency check to promote sparsity in the graph, allowing these methods to scale to larger maps. However, these methods rely on assumptions about exploration, allowing the agent to spawn uniformly random across the state space during training. To address this, HTM [19] used a generative model to hallucinate samples for building the graph in a zero-shot manner, but was not evaluated in 3D visual environments. NTS [4] achieved exploration and long-horizon navigation as well as generalization to unseen maps by learning a geometric-based graph representation, but required access to a ground-truth map to train their supervised learning model. In contrast, our method achieves exploration by planning and executing paths towards landmarks near novel areas during training. SFL also does not require any ground-truth data; it only needs to learn SF in a self-supervised manner. 

**Successor features.** Our work is inspired by recent efforts in developing successor features (SF) [15, 2]. They have used SF to decompose the Q-value function into SF and the reward which enables efficient policy transfer [2, 3] and to design transition-based intrinsic rewards [20, 39] for efficient exploration. SF has also been used in the options framework [35]; Eigenoptions [21] derived options from the eigendecomposition of SF, but did not yet apply them towards reward maximization. Successor Options [28] used SF to discover landmark states and design a latent reward for learning option policies, but was limited to low-dimensional state spaces. Our framework leverages a SF-based similarity metric to formulate a goal-conditioned policy, abstract the state space as a landmark graph for long-horizon planning and to model state-novelty for driving exploration. While the options policies proposed in these works have to be learned from a reward signal, we can obtain our goal-conditioned policy directly from the SF similarity metric without any policy learning. To our knowledge, this is first work that uses SF for graph-based planning and long-horizon GCRL tasks. 

## **3 Preliminaries** 

## **3.1 Goal-Conditioned RL** 

Goal-conditioned reinforcement learning (GCRL) tasks [12] are Markov Decision Processes (MDP) extended with a set of goals _G_ and defined by a tuple ( _S, A, G, RG, T , γ_ ), where _S_ is a state space, _A_ an action set, _RG_ : _S ⇥A ⇥G !_ R a goal-conditioned reward function, _T_ the transition dynamics, and _γ_ a discount factor. Following [11, 36], we focus on the setting where the goal space _G_ is a subset of the state space _S_ , and the agent can receive non-trivial rewards only when it can reach the goal ( _i.e_ ., sparse-reward setting). We aim to find an optimal goal-conditioned policy _⇡_ : _S ⇥G ! A_ to maximize the expected cumulative reward, _Vg[⇡]_[(] _[s]_[0][) =][ E] _[⇡]_[[][P] _t[γ][t][r][t]_[]][;] _[ i.e]_[., goal-conditioned value] function. We are especially interested in long-horizon tasks where goals are distant from the agent’s starting state, requiring the policy to operate over longer temporal sequences. 

3 

**Algorithm 1** Training 

1: **Initialize:** Graph _G_ = ( _L, E_ ), parameter _✓_ of SFS _[⇡] ✓_[¯][,][replay][buffer] _[D]_[,][hyperparameter] _[T]_[exp][,] landmark transition count _N[l]_ 2: **while** env not done **do** 3: _l_ front _⇠_ Softmax( Count(1 _L_ )[)] {Choose frontier landmark via count-based sampling} 4: **while** _l_ curr = _l_ front **do** 5: _l_ target PLAN( _G, l_ curr _, l_ front) {Plan path to frontier landmark} 6: _⌧_ traverse _, l_ curr Traverse( _⇡l, l_ target) {Traverse to _l_ target with _⇡l_ (Algorithm 3 in §H)} 7: _G, N[l]_ Graph-Update( _G, ⌧_ traverse _,_ SFS _[⇡] ✓_[¯] _[, N][ l]_[)] {Update graph (Algorithm 2)} 8: **end while** 9: _⌧_ rand = _{st, at, rt}[T] t_[exp] _⇠ ⇡_ ¯ {Explore with random policy for _T_ exp steps} 10: _G, N[l]_ Graph-Update( _G, ⌧_ rand _,_ SFS _[⇡] ✓_[¯] _[, N][ l]_[)] {Update graph (Algorithm 2)} 11: _D D [ ⌧_ random 12: Update _✓_ from TD error with mini-batches sampled from _D_ {Update SF parameters} 13: **end while** 

## **3.2 Successor Features** 

In the tabular setting, the successor representation (SR) [8, 15] is defined as the expected discounted occupancy of futures state _s[0]_ starting in state _s_ and action _a_ and acting under a policy _⇡_ : 

**==> picture [321 x 19] intentionally omitted <==**

The SR _M_ ( _s, a_ ) is then a concatenation of _M_ ( _s, a, s[0]_ ) _, 8s 2 S_ . We may view SR as a representation of state similarity extended over the time dimension, as described in [21]. In addition, we note that the SR is solely determined by _⇡_ and the transition dynamics of the environment _p_ ( _st_ +1 _|st, at_ ). 

Successor features (SF) [2, 15] extend SR [8] to high-dimensional, continuous state spaces in which function approximation is often used. SF’s formulation modifies the definition of SR by replacing enumeration over all states _s[0]_ with feature vector _φs0_ . The SF _[⇡]_ of a state-action pair ( _s, a_ ) is then 

**==> picture [301 x 19] intentionally omitted <==**

In addition, SF can be defined in terms of only the state, _[⇡]_ ( _s_ ) = E _a⇠⇡_ ( _s_ )[ _[⇡]_ ( _s, a_ )] _._ 

SF allows decoupling the value function into the successor feature (dynamics-relevant information) with task (reward function): if we assume that the one-step reward of transition ( _s, a, s[0]_ ) with feature _φ_ ( _s, a, s[0]_ ) can be written as _r_ ( _s, a, s[0]_ ) = _φ_ ( _s, a, s[0]_ ) _[>]_ **w** , where **w** are learnable weights to fit the reward function, we can write the Q-value function as follows [2, 15]: 

**==> picture [331 x 65] intentionally omitted <==**

Consequently, the Q-value function separates into SF, which represents the policy-dependent transition dynamics, and the reward vector **w** for a particular task. Later in Section 4.3, we will extend this formulation to the goal-conditioned setting and discuss our choices for **w** . 

## **4 Successor Feature Landmarks** 

We present Successor Feature Landmarks (SFL), a graph-based planning framework for supporting exploration and long-horizon GCRL. SFL is centrally built upon our novel distance metric: Successor Feature Similarity (SFS, §4.1). We maintain a non-parametric graph of state “landmarks,” using SFS as a distance metric for determining which observed states to add as landmarks and how these landmarks should be connected (§4.2). To enable traversal between landmarks, we directly obtain a local goal-conditioned policy from SFS between current state and the given landmark (§4.3). With these components, we tackle the long-horizon setting by planning on the landmark graph and finding 

4 

**==> picture [396 x 113] intentionally omitted <==**

**----- Start of picture text -----**<br>
Localization Edge Formation<br>Agent<br>trajectory * * Landmarks<br>Currently localized<br>Previously localized<br>Adding Landmarks Currest state<br>Agent trajectory<br>Localization status<br>Random Transition<br>Buffer<br>**----- End of picture text -----**<br>


Figure 2: The **Graph + SF Update** step occurs after every transition ( _s, a_ ). The agent computes SFS between current state _s_ (black dot) and all landmarks (blue dots). It then localizes itself to the nearest landmark (red circled dot). The agent records transitions between the previously localized landmark (green circled dot) and this landmark. If the number of transitions between two landmarks is greater than _δedge_ , then an edge is formed between them. If SFS between the current localized landmark and _s_ is less than _δadd_ , then _s_ is added as a landmark. Finally, transitions generated by the random policy are added to the random transition buffer, and SF is trained on batch samples from this buffer. 

the shortest path to the given goal, which decomposes the long-horizon problem into a sequence of short-horizon tasks that the local policy can then more reliably achieve (§4.4). In training, our agent focuses on exploration. We set the goals as “frontier” landmarks lying at the edge of the explored region, and use the planner and local policy to reach the frontier landmark. Upon reaching the frontier, the agent locally explores with a random policy and uses this new data to update its SF and landmark graph (§4.5). In evaluation, we add the given goal to the graph and follow the shortest path to it. Figure 1 illustrates the overarching framework and Figure 2 gives further detail into how the graph and SF are updated. Algorithm 1 describes the procedure used to train SFL. 

## **4.1 Successor Feature Similarity** 

SFS, the foundation of our framework, is based on SF. For context, we estimate SF as the output of a deep neural network parameterized byof state and _⇡_ is a fixed policy which we choose to be a uniform random policy denoted as _✓_ : _[⇡]_ ( _s, a_ ) _⇡ ✓[⇡]_[(] _[φ]_[(] _[s]_[)] _[, a]_[)][, where] _[ φ]_[ is a feature embedding] _⇡_ ¯. We update _✓_ by minimizing the temporal difference (TD) error [15, 2]. Details on learning SF are provided in Appendix C.3. 

Next, to gain intuition for SFS, suppose we wish to compare two state-action pairs ( _s_ 1 _, a_ 1) and ( _s_ 2 _, a_ 2) in terms of similarity. One option is to compare _s_ 1 and _s_ 2 directly via some metric such as _`_ 2 distance, but this ignores _a_ 1 _, a_ 2 and dynamics of the environment. 

To address this issue, we should also consider the states the agent is expected to visit when starting from each state-action pair, for a fixed policy _⇡_ . We choose _⇡_ to be uniform random, i.e. _⇡_ ¯, so that only the dynamics of the environment will dictate which states the agent will visit. With this idea, we can define a novel similarity metric, **Successor Feature Similarity (SFS)** , which measures the similarity of the expected discounted state-occupancy of two state-action pairs. Using the successor representation _M⇡_ ¯( _s, a_ ) as defined in Section 3.2, we can simply define SFS as the dot-product between the two successor representations for each state-action pair: 

**==> picture [98 x 12] intentionally omitted <==**

**==> picture [365 x 59] intentionally omitted <==**

We can extend SFS to the high-dimensional case by encoding states in the feature space _φ_ and replacing _M⇡_ ¯( _s, a_ ) with _[⇡]_[¯] ( _s, a_ ). The intuition remains the same, but we instead measure similarities in the feature space. In practice, we normalize _[⇡]_ ( _s, a_ ) before computing SFS to prevent high-value feature dimensions from dominating the similarity metric, hence defining SFS as the cosine similarity between SF. In addition, we may define SFS between just two states by getting rid of the action 

5 

dimension in SF: 

**==> picture [301 x 29] intentionally omitted <==**

## **4.2 Landmark Graph** 

The landmark graph _G_ serves as a compact representation of the state space and its transition dynamics. _G_ is dynamically-populated in an online fashion as the agent explores more of its environment. Formally, landmark graph _G_ = ( _L, E_ ) is a tuple of landmarks _L_ and edges _E_ . The landmark set _L_ = _{l_ 1 _, . . . , l|L|}_ is a set of states representing the explored part of the state-space. The edge set _E_ is a matrix R _[|][L][|⇥|][L][|]_ , where _Ei,j_ = 1 if _li_ and _lj_ is connected, and 0 otherwise. Algorithm 2 outlines the graph update process, and the following paragraph describes this process in further detail. 

**Agent Localization and Adding Landmarks** At every time step _t_ , we compute the landmark closest to the agent under SFS metric: _l_ curr = argmax _l2L_ SFS _[⇡]_[¯] ( _st, l_ ). If SFS _[⇡]_[¯] ( _st, l_ curr) _< δadd_ , the add threshold, then we add _st_ to the landmark set _L_ . Otherwise, if SFS _[⇡]_[¯] ( _st, l_ curr) _> δ_ local, the localization threshold, then the agent is localized to _l_ curr. If the agent was previously localized to a different landmark _l_ prev, then we increment the count of the landmark transition _N_ ( _[l] l_ prev _!l_ curr)[by 1] where _N[l] 2_ N _[|][E][|]_ is the landmark transition count, which is used to form the graph edges.[2] 

Since we progressively build the landmark set, we maintain all previously added landmarks. As described above, this enables us to utilize useful landmark metrics such as how many times the agent has been localized to each landmark and what transitions have occurred between landmarks to improve the connectivity quality of the graph. In comparison, landmarks identified through clustering schemes such as in Successor Options [28] cannot be used in this manner because the landmark set is rebuilt every few iterations. See Appendix B.3 for a detailed comparison on landmark formation. 

**Edge Formation** We form edge _Ei,j_ if the number of the landmark transitions is larger than the edge threshold, _i.e_ ., _Nl[l] i!lj[> δ][edge]_[,] with weight _Wi,j_ = exp( _−_ ( _Nl[l] i!lj_[))][.][We] apply filtering improvements to _E_ in **ViZDoom** to mitigate the perceptual aliasing problem where faraway states can appear visually similar due to repeated use of textures. See Appendix D for more details. 

## **4.3 Local Goal-Conditioned Policy** 

We want to learn a local goal-conditioned policy _⇡l_ : _S ⇥G ! A_ to reach or transition between landmarks. To accomplish this, _⇡l_ should maximize the expected return _V_ ( _s, g_ ) = E[[P] _[1] t_ =0 _[γ][t][r]_[(] _[s][t][, a][t][, g]_[)]][,][where] _r_ ( _s, a, g_ ) is a reward function that captures how close _s_ (or more precisely _s, a_ ) is to the goal _g_ in terms of feature similarity: 

**==> picture [146 x 13] intentionally omitted <==**

where _[⇡]_[¯] is the SF with respect to the random policy _⇡_ ¯. Recall that we can decouple the Q-value function into the SF representation and reward weights **w** as shown in 

## **Algorithm 2** Graph-Update (§4.2) 

**input** Graph _G_ = ( _L, E_ ), SFS _[⇡] ✓_[¯][, trajectory] _[ ⌧]_[,] landmark transition count _N[l]_ **output** updated graph _G_ and _N[l]_ 1: _l_ prev _;_ {Previously localized landmark} 2: **for** _s 2 ⌧_ **do** 3: _l_ curr argmax _l2L_ SFS _[⇡] ✓_[¯][(] _[s, l]_[)] {Localize} 4: **if** SFS _[⇡] ✓_[¯][(] _[s, l]_[curr][)] _[ < δ][add]_ **[then]** 5: _L L [ s_ {Add landmark} 6: **end if** 7: **if** SFS _[⇡] ✓_[¯][(] _[s, l]_[curr][)] _[ > δ][local]_ **[then]** 8: **if** _l_ prev = _;_ **and** _l_ prev = _l_ curr **then** 9: _N_ ( _[l] l_ prev _!l_ curr) _[N][ l]_ ( _l_ prev _!l_ curr)[+ 1][{Record] landmark transition} 10: **if** _N_ ( _[l] l_ prev _!l_ curr) _[> δ][edge]_ **[ then]** 11: _E E [_ ( _l_ prev _! l_ curr) {Form edge} 12: **end if** 13: **end if** 14: _l_ prev _l_ curr 15: **end if** 16: **end for** 17: **return** _G, N[l]_ 

Eq. (3). The reward function Eq. (7) is our deliberate choice rather than learning a linear reward regression model [2], so the value function can be instantly computed. If we let **w** be _[⇡]_[¯] ( _g_ ), we can 

2Zhang et al. [38] proposed a similar idea of recording the transitions between sets of user-defined attributes. We extend this idea to the function approximation setting where landmark attributes are their SFs. 

6 

have the Q-value function _Q[⇡]_[¯] ( _s, a, g_ ) for the goal-conditioned policy _⇡_ ( _a|s, g_ ) being equal to the SFS between _s_ and _g_ : 

**==> picture [297 x 13] intentionally omitted <==**

The goal-conditioned policy is derived by sampling actions from the goal-conditioned Q-value function in a greedy manner for discrete actions. In the continuous action case, we can learn the goal-conditioned policy by using a compatible algorithm such as DDPG [18]. However, extending SF learning to continuous action spaces is beyond the scope of this work and is left for future work. 

## **4.4 Planning** 

Given the landmark graph _G_ , we can plan the shortest-path from the landmark closest to the agent _l_ curr to a final target landmark _l_ target by selecting a sequence of landmarks [ _l_ 0 _, l_ 1 _, . . . , lk_ ] in the graph _G_ with minimal weight (see _§_ 4.2) sum along the path, where _l_ 0 = _l_ curr, _lk_ = _l_ target, and _k_ is the length of the plan. In training, we use frontier landmarks _l_ front which have been visited less frequently as _l_ target. In evaluation, the given goal state is added to the graph and set as _l_ target. See Algorithm 1 for an overview of how planning is used to select the agent’s low-level policy in training. 

## **4.5 Exploration** 

We sample frontier landmarks _l_ front proportional to the inverse of their visitation count ( _i.e_ ., with count-based exploration). We use two policies: a local policy _⇡l_ for traversing between landmarks and a random policy ¯ _⇡_ for exploring around a frontier landmark. Given a target frontier landmark _l_ front, we construct a plan [ _l_ 0 _, l_ 1 _, . . . , l_ front]. When the agent is localized to landmark _li_ , the policy at time _t_ is defined as _⇡l_ ( _a|st_ ; _li_ +1). When the agent is localized to a landmark that is not included in the current plan [ _l_ 0 _, l_ 1 _, . . . , l_ front], then it re-plans a new path to _l_ front. Such failure cases of transition between the landmarks are used to prevent edge between those landmarks from being formed (see Appendix D for details). We run this process until either _l_ front is reached or until the step-limit _N_ front is reached. At that point, random policyour graph as a new landmark. _⇡_ ¯While the random policy is deployed, its trajectoryis deployed for exploration for _N_ explore steps, adding novel states to _⌧ ⇠ ⇡_ ¯ is added to the random transition buffer. SF _✓[⇡]_[¯][is updated with batch samples from this buffer.] 

The random policy is only used to explore local neighborhoods at frontier regions for a short horizon while the goal-conditioned policy and planner are responsible for traveling to these frontier regions. Under this framework, the agent is able to visit a diverse set of states in a relatively efficient manner. Our experiments on large **ViZDoom** maps demonstrate that this strategy is sufficient for learning a SF representation that ultimately outperforms baseline methods on goal-reaching tasks. 

## **5 Experiments** 

SFL study how well our framework supports reaching long-horizon goals when the agent’s start state is randomized across episodes. Afterwards, we consider how SFL performs when efficient exploration is required to reach distant areas by using a setting where the agent’s start state is fixed in training. 

## **5.1** 

**ViZDoom** is a visual navigation environment with 3D first-person observations. In **ViZDoom** , the largescale of the maps and reuse of similar textures make it particularly difficult to learn distance metrics from the first-person observations. This is due to perceptual aliasing, where visually similar images can be geographically far apart. We use mazes from SPTM in our experiments, with one example shown in Figure 3 [29]. 

**MiniGrid** is a 2D gridworld with tasks that require the agent to overcome different obstacles to access portions of the map. We experiment on **FourRoom** , a basic 4-room map, and **MultiRoom** , where the agent needs to open doors to reach new rooms. 

**==> picture [179 x 57] intentionally omitted <==**

**==> picture [52 x 40] intentionally omitted <==**

**==> picture [53 x 40] intentionally omitted <==**

**==> picture [52 x 40] intentionally omitted <==**

Figure 3: Top-down view of a **ViZDoom** maze used in _fixed spawn_ with sampled goal locations. Examples of image goals given to the agent are shown at the bottom. Note that the agent cannot access the top-down view. 

7 

We study two settings: 

1. **Random spawn** : In training, the agent is randomly spawned across the map with no given goal. In evaluation, the agent is then tested on pairs of start and goal states, where goals are given as images. This enables us to study how well the landmark graph supports traversal between arbitrary start-goal pairs. Following [16], we evaluate on `easy` , `medium` , and `hard` tasks where the goal is sampled within 200m, 200-400m, and 400-600m from the initial state, respectively. 

2. **Fixed spawn** : In training, the agent is spawned at a fixed start state _s_ start with no given goal. This enables us to study how well the agent can explore the map given a limited step budget per episode. In evaluation, the agent is again spawned at _s_ start and is given different goal states to reach. In **ViZDoom** , we sample goals of varying difficulty accounting for the maze structure as shown in Figure 3. In **MiniGrid** , a similar setup is used except only one goal state is used for evaluation. 

## **5.2 Baseline Methods for Comparison** 

**Random spawn experiments** . We compare SFL against baselines used in SGM, as described below. For each difficulty, we measure the average success rate over 5 random seeds. We evaluate on the map used in SGM, _SGM-Map_ , and two more maps from SPTM, _Test-2_ and _Test-6_ . 

1. **Random Actions** : random acting agent. 

2. **Visual Controller** : model-free visual controller learned via inverse dynamics. Baseline highlights how low-level controllers struggle to learn long-horizon policies and the benefits of planning to create high-level paths that the controller can follow. 

3. **SPTM** [29]: planning module with a reachability network to learn a distance metric for localization and landmark graph formation. Baseline is used to measure how the SFS metric can improve localization and landmark graph formation. 

4. **SGM** [16]: data structure used to improve planning by inducing sparsity in landmark graphs. Baseline represents a recent landmark-based approach for long-horizon navigation. 

**Fixed spawn experiments** . In the _fixed spawn_ setting, we compare SFL against Mapping State Space (MSS) [11], a UVFA and landmark-based approach for exploration and long-horizon goalconditioned RL, as well as SPTM and SGM. Again, we measure the average success rate over 5 random seeds. We adapt the published code[3] to work on **ViZDoom** and **MiniGrid** . To evaluate SPTM and SGM, we populate their graphs with exploration trajectories generated by Episodic Curiosity (EC) [30]. EC learns an exploration policy by using a reachability network to determine whether an observation is novel enough to be added to the memory and rewarding the agent every time one is added. Appendix C further discusses the implementation of these baselines. 

## **5.3 Implementation Details** 

SFL is implemented with the _rlpyt_ codebase [33]. For experiments in **ViZDoom** , we use the pretrained ResNet-18 backbone from SPTM as a fixed feature encoder which is similarly used across all baselines. For **MiniGrid** , we train a convolutional feature encoder using time-contrastive metric learning [32]. Both feature encoders are trained in a self-supervised manner and aim to encode temporally close states as similar feature representations and temporally far states as dissimilar representations. We then approximate SF with a fully-connected neural network, using these encoded features as input. See Appendix C for more details on feature learning, edge formation, and hyperparameters. 

## **5.4 Results** 

**Random Spawn Results** . As shown in Table 1, our method outperforms the other baselines on all settings. SFL’s performance on the Hard setting particularly illustrates its ability to reach long-horizon goals. In terms of sample efficiency, SFL utilizes a total of 2M environment steps to simultaneously train SF and build the landmark graph. For reference, SPTM and SGM train their reachability and low-level controller networks with over 250M environment steps of training data collected on _SGM-Map_ , with SGM using an additional 114K steps to build and cleanup their landmark graph. For _Test-2_ and _Test-6_ , we fine-tune these two networks with 4M steps of training data collected from each new map to give a fair comparison. 

> 3 `https://github.com/FangchenLiu/map_planner` 

8 

|Method|_SGM-Map_<br>Easy<br>Medium<br>Hard|_Test-2_<br>Easy<br>Medium<br>Hard|_Test-6_<br>Easy<br>Medium<br>Hard|
|---|---|---|---|
|Random Actions<br>58%<br>22%<br>12%<br>70%<br>39%<br>16%<br>80%<br>31%<br>18%<br>Visual Controller<br>75%<br>35%<br>19%<br>83%<br>51%<br>30%<br>89%<br>39%<br>20%<br>SPTM [29]<br>70%<br>34%<br>14%<br>78%<br>48%<br>18%<br>88%<br>40%<br>18%<br>SGM [16]<br>**92**%<br>64%<br>26%<br>**86%**<br>54%<br>32%<br>83%<br>43%<br>27%<br>SFL [Ours]<br>**92**%<br>**82%**<br>**67%**<br>82%<br>**66%**<br>**48%**<br>**92%**<br>**66%**<br>**60%**||||



Table 1: ( _Random spawn_ ) The success rates of compared methods on three **ViZDoom** maps. 

|Method|_Test-1_<br>Easy<br>Medium<br>Hard<br>Hardest|_Test-4_<br>Easy<br>Medium<br>Hard<br>Hardest|
|---|---|---|
|MSS [11]<br>23%<br>9%<br>1%<br>1%<br>21%<br>7%<br>7%<br>7%<br>EC [30] + SPTM [29]<br>48%<br>16%<br>2%<br>0%<br>20%<br>10%<br>4%<br>0%<br>EC [30] + SGM [16]<br>43%<br>3%<br>0%<br>0%<br>28%<br>7%<br>4%<br>1%<br>SFL [Ours]<br>**85**%<br>**59%**<br>**62%**<br>**50%**<br>**66%**<br>**44%**<br>**27%**<br>**23%**|||



Table 2: ( _Fixed spawn_ ) The success rates of compared methods on three **ViZDoom** maps. 

**Fixed Spawn Results.** We see in Table 2 that SFL reaches significantly higher success rates than the baselines across all difficulty levels, especially on _Hard_ and _Hardest_ . Figure 4 shows the average success rate over the number of environment steps for SFL (red) and MSS (green). We hypothesize that MSS struggles because its UVFA is unable to capture geodesic distance in **ViZDoom** ’s highdimensional state space with first-person views. The UVFA in MSS has to solve the difficult task of approximating the number of steps between two states, which we conjecture requires a larger sample complexity and more learning capacity. In contrast, we only use SFS to relatively compare states, i.e. is SFS of state A higher than SFS of state B with respect to reference state C? EC-augmented SPTM and SGM partially outperform MSS, but cannot scale to harder difficulty levels. We suggest that these baselines suffer from disjointedness of exploration and planning: the EC exploration module is less effective because it does not utilize planning to efficient reach distant areas, which in turn limits the training of policy networks. See Appendix F and Appendix G for more analysis on the baselines. 

Figure 5 shows the average success rate on **MiniGrid** environments, where SFL (red) overall outperforms MSS (green). States in **MiniGrid** encode top-down views of the map with distinct signatures for the agent, walls, and doors, making it easier to learn distance metrics. In spite of this, the environment remains challenging due to the presence of doors as obstacles and the limited time budget per episode. 

**==> picture [195 x 144] intentionally omitted <==**

Figure 4: _Fixed spawn_ experiments on **ViZDoom** comparing SFL (red) to MSS (green) over number of environment steps for varying difficulty levels. 

**==> picture [195 x 144] intentionally omitted <==**

Figure 5: _Fixed spawn_ experiments on **MiniGrid** comparing SFL (red) to MSS (green) over number of environment steps for varying difficulty levels. 

9 

**==> picture [396 x 108] intentionally omitted <==**

Figure 6: SFS values relative to a reference state (blue dot) in the _Test-1_ **ViZDoom** maze. The left two heatmaps use the agent’s start state as the reference state while the right two use a distant goal state as the reference state. The first and third (colorful) heatmaps depict all states while the second and fourth (darkened) heatmaps only show states with SFS _> δ_ local = 0 _._ 9. 

## **5.5 SFS Visualization** 

SFL primarily relies on SFS and its capacity to approximate geodesic distance imposed by the map’s structure. To provide evidence of this ability, we compute the SFS between a reference state and a set of randomly sampled states. Figure 6 visualizes these SFS heatmaps in a **ViZDoom** maze. In the first and third panels, we observe that states close to the reference state (blue dot) exhibit higher SFS values while distant states, such as those across a wall, exhibit lower SFS values. The second and fourth panels show states in which the agent would be localized to the reference state, i.e. states with SFS _> δ_ local. With this SFS threshold, we reduce localization errors, thereby improving the quality of the landmark graph. We provide additional analysis of SFS-derived components, the landmark graph and goal-conditioned policy, in Appendix E. 

## **6 Conclusion** 

In this paper, we presented Successor Feature Landmarks, a graph-based planning framework that leverages a SF similarity metric, as an approach to exploration and long-horizon goal-conditioned RL. Our experiments in ViZDoom and MiniGrid, demonstrated that this method outperforms current graph-based approaches on long-horizon goal-reaching tasks. Additionally, we showed that our framework can be used for exploration, enabling discovery and reaching of goals far away from the agent’s starting position. Our work empirically showed that SF can be used to make robust decisions about environment dynamics, and we hope that future work will continue along this line by formulating new uses of this representation. Our framework is built upon the representation power of SF, which depends on a good feature embedding to be learned. We foresee that our method can be extended by augmenting with an algorithm for learning robust feature embeddings to facilitate SF learning. 

## **Acknowledgements** 

This work was supported by the NSF CAREER IIS 1453651 Grant. JC was partly supported by Korea Foundation for Advanced Studies. WC was supported by an NSF Fellowship under Grant No. DGE1418060. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the funding agencies. We thank Yunseok Jang and Anthony Liu for their valuable feedback. We also thank Scott Emmons and Ajay Jain for sharing and helping with the code for the SGM [16] baseline. 

10 

## **References** 

- [1] Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob McGrew, Josh Tobin, OpenAI Pieter Abbeel, and Wojciech Zaremba. Hindsight experience replay. In _Advances in Neural Information Processing Systems 30_ , pages 5048–5058. Curran Associates, Inc., 2017. 

- [2] Andre Barreto, Will Dabney, Remi Munos, Jonathan J Hunt, Tom Schaul, David Silver, and Hado van Hasselt. Successor Features for Transfer in Reinforcement Learning. In _Advances in Neural Information Processing Systems (NeurIPS)_ , pages 1–24, 2017. 

- [3] Diana Borsa, Andre Barreto, John Quan, Daniel Mankowitz, Remi Munos, Hado van Hasselt, David Silver, and Tom Schaul. Universal Successor Features Approximators. In _ICLR_ , 2019. 

- [4] Devendra Singh Chaplot, Ruslan Salakhutdinov, Abhinav Gupta, and Saurabh Gupta. Neural topological slam for visual navigation. In _CVPR_ , 2020. 

- [5] Tao Chen, Saurabh Gupta, and Abhinav Gupta. Learning exploration policies for navigation. In _Proceedings of (ICLR) International Conference on Learning Representations_ , May 2019. 

- [6] Maxime Chevalier-Boisvert, Lucas Willems, and Suman Pal. Minimalistic gridworld environment for openai gym. `https://github.com/maximecb/gym-minigrid` , 2018. 

- [7] Sumit Chopra, Raia Hadsell, and Yann Lecun. Learning a similarity metric discriminatively, with application to face verification. volume 1, pages 539– 546 vol. 1, 07 2005. 

- [8] Peter Dayan. Improving generalization for temporal difference learning: The successor representation. _Neural Computation_ , 5(4):613–624, 1993. 

- [9] Ben Eysenbach, Russ R Salakhutdinov, and Sergey Levine. Search on the replay buffer: Bridging planning and reinforcement learning. In _Advances in Neural Information Processing Systems_ , volume 32, 2019. 

- [10] Dibya Ghosh, Abhishek Gupta, and Sergey Levine. Learning actionable representations with goal-conditioned policies. In _Proceedings of (ICLR) International Conference on Learning Representations_ , May 2019. 

- [11] Zhiao Huang, Fangchen Liu, and Hao Su. Mapping state space using landmarks for universal goal reaching. In _Advances in Neural Information Processing Systems (NeurIPS_ , pages 1940– 1950, 2019. 

- [12] L. Kaelbling. Learning to achieve goals. In _IJCAI_ , 1993. 

- [13] Leslie Pack Kaelbling. Hierarchical learning in stochastic domains: Preliminary results. In _In Proceedings of the Tenth International Conference on Machine Learning_ , pages 167–173. Morgan Kaufmann, 1993. 

- [14] Diederick P Kingma and Jimmy Ba. Adam: A method for stochastic optimization. In _International Conference on Learning Representations (ICLR)_ , 2015. 

- [15] Tejas D. Kulkarni, Ardavan Saeedi, Simanta Gautam, and Samuel J. Gershman. Deep successor reinforcement learning, 2016. 

- [16] Michael Laskin, Scott Emmons, Ajay Jain, Thanard Kurutach, Pieter Abbeel, and Deepak Pathak. Sparse graphical memory for robust planning, 2020. 

- [17] Andrew Levy, Robert Platt, and Kate Saenko. Hierarchical reinforcement learning with hindsight. In _International Conference on Learning Representations_ , 2019. 

- [18] Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, and Daan Wierstra. Continuous control with deep reinforcement learning. In Yoshua Bengio and Yann LeCun, editors, _4th International Conference on Learning Representations, ICLR 2016, San Juan, Puerto Rico, May 2-4, 2016, Conference Track Proceedings_ , 2016. 

11 

- [19] Kara Liu, Thanard Kurutach, Christine Tung, P. Abbeel, and Aviv Tamar. Hallucinative topological memory for zero-shot visual planning. In _Proceedings of the 37th International Conference on Machine Learning_ , volume abs/2002.12336, 2020. 

- [20] Marlos C Machado, Marc G Bellemare, and Michael Bowling. Count-Based Exploration with the Successor Representation. 2018. 

- [21] Marlos C Machado, Clemens Rosenbaum, Xiaoxiao Guo, Miao Liu, Gerald Tesauro, and Murray Campbell. Eigenoption Discovery through the Deep Successor Representation. In _ICLR_ , 2018. 

- [22] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. Human-level control through deep reinforcement learning. _Nature_ , 518(7540):529–533, February 2015. 

- [23] Andrew W. Moore, Leemon C. Baird, and Leslie Kaelbling. Multi-value-functions: Efficient automatic action hierarchies for multiple goal mdps. In _Proceedings of the 16th International Joint Conference on Artificial Intelligence - Volume 2_ , IJCAI’99, page 1316–1321, San Francisco, CA, USA, 1999. Morgan Kaufmann Publishers Inc. 

- [24] Ashvin V Nair, Vitchyr Pong, Murtaza Dalal, Shikhar Bahl, Steven Lin, and Sergey Levine. Visual reinforcement learning with imagined goals. In S. Bengio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-Bianchi, and R. Garnett, editors, _Advances in Neural Information Processing Systems_ , volume 31. Curran Associates, Inc., 2018. 

- [25] Soroush Nasiriany, Vitchyr Pong, Steven Lin, and Sergey Levine. Planning with goalconditioned policies. 2019. 

- [26] Vitchyr Pong, Shixiang Gu, Murtaza Dalal, and Sergey Levine. Temporal difference models: Model-free deep RL for model-based control. _ICLR_ , abs/1802.09081, 2018. 

- [27] Vitchyr H. Pong, Murtaza Dalal, Steven Lin, Ashvin Nair, Shikhar Bahl, and Sergey Levine. Skew-fit: State-covering self-supervised reinforcement learning. _ICML_ , abs/1903.03698, 2020. 

- [28] Rahul Ramesh, Manan Tomar, and Balaraman Ravindran. Successor options: An option discovery framework for reinforcement learning. In _Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19_ , pages 3304–3310. International Joint Conferences on Artificial Intelligence Organization, 7 2019. 

- [29] Nikolay Savinov, Alexey Dosovitskiy, and Vladlen Koltun. Semi-parametric topological memory for navigation. In _International Conference on Learning Representations (ICLR)_ , 2018. 

- [30] Nikolay Savinov, Anton Raichuk, Raphaël Marinier, Damien Vincent, Marc Pollefeys, Timothy Lillicrap, and Sylvain Gelly. Episodic curiosity through reachability. In _International Conference on Learning Representations (ICLR)_ , 2019. 

- [31] Tom Schaul, Daniel Horgan, Karol Gregor, and David Silver. Universal value function approximators. In Francis Bach and David Blei, editors, _Proceedings of the 32nd International Conference on Machine Learning_ , volume 37 of _Proceedings of Machine Learning Research_ , pages 1312–1320, Lille, France, 07–09 Jul 2015. PMLR. 

- [32] Pierre Sermanet, Corey Lynch, Yevgen Chebotar, Eric Hsu, Jasmineand Jang, Stefan Schaal, and Sergey Levine. Time-contrastive networks: Self-supervised learning from video. _Proceedings of International Conference in Robotics and Automation (ICRA)_ . 

- [33] Adam Stooke and Pieter Abbeel. rlpyt: A research code base for deep reinforcement learning in pytorch. _CoRR_ , abs/1909.01500, 2019. 

- [34] Richard Sutton, Joseph Modayil, Michael Delp, Thomas Degris, Patrick Pilarski, Adam White, and Doina Precup. Horde : A scalable real-time architecture for learning knowledge from unsupervised sensorimotor interaction categories and subject descriptors. volume 2, 01 2011. 

12 

- [35] Richard S. Sutton, Doina Precup, and Satinder Singh. Between mdps and semi-mdps: A framework for temporal abstraction in reinforcement learning. _Artificial Intelligence_ , 112(1):181 – 211, 1999. 

- [36] Srinivas Venkattaramanujam, Eric Crawford, Thang Doan, and Doina Precup. Self-supervised learning of distance functions for goal-conditioned reinforcement learning. _arXiv preprint arXiv:1907.02998_ , 2019. 

- [37] Marek Wydmuch, Michał Kempka, and Wojciech Ja´skowski. Vizdoom competitions: Playing doom from pixels. _IEEE Transactions on Games_ , 2018. 

- [38] Amy Zhang, Sainbayar Sukhbaatar, Adam Lerer, Arthur Szlam, and Rob Fergus. Composable planning with attributes. In _Proceedings of the 35th International Conference on Machine Learning, ICML 2018, Stockholmsmässan, Stockholm, Sweden, July 10-15, 2018_ , volume 80 of _Proceedings of Machine Learning Research_ , pages 5837–5846. PMLR, 2018. 

- [39] Jingwei Zhang, Niklas Wetzel, Nicolai Dorka, Joschka Boedecker, and Wolfram Burgard. Scheduled Intrinsic Drive: A Hierarchical Take on Intrinsically Motivated Exploration. 2019. 

13 

