## **Temporal Abstraction in Reinforcement Learning with the Successor Representation** 

## **Marlos C. Machado** 

marlosm@deepmind.com 

_DeepMind Alberta Machine Intelligence Institute (Amii) Department of Computing Science, University of Alberta Edmonton, AB, Canada_ 

**Andr´e Barreto** _DeepMind London, United Kingdom_ 

## **Doina Precup** 

andrebarreto@deepmind.com 

doinap@deepmind.com 

_DeepMind Quebec AI Institute (Mila) School of Computer Science, McGill University Montreal, QC, Canada_ 

## **Abstract** 

Reasoning at multiple levels of temporal abstraction is one of the key attributes of intelligence. In reinforcement learning, this is often modeled through temporally extended courses of actions called _options_ . Options allow agents to make predictions and to operate at different levels of abstraction within an environment. Nevertheless, approaches based on the options framework often start with the assumption that a reasonable set of options is known beforehand. When this is not the case, there are no definitive answers for which options one should consider. In this paper, we argue that the successor representation, which encodes states based on the pattern of state visitation that follows them, can be seen as a natural substrate for the discovery and use of temporal abstractions. To support our claim, we take a big picture view of recent results, showing how the successor representation can be used to discover options that facilitate either temporally-extended exploration or planning. We cast these results as instantiations of a general framework for option discovery in which the agent’s representation is used to identify useful options, which are then used to further improve its representation. This results in a virtuous, never-ending, cycle in which both the representation and the options are constantly being refined based on each other. Beyond option discovery itself, we also discuss how the successor representation allows us to augment a set of options into a combinatorially large counterpart without additional learning. This is achieved through the combination of previously learned options. Our empirical evaluation focuses on options discovered for temporally-extended exploration and on the use of the successor representation to combine them. The results of our experiments shed light on important design decisions involved in the definition of options and demonstrate the synergy of different methods based on the successor representation, such as eigenoptions and the option keyboard. 

**Keywords:** Reinforcement Learning, Options, Successor Representation, Eigenoptions, Covering Options, Option Keyboard, Temporally-Extended Exploration. 

1 

Machado, Barreto, and Precup 

## **1. Introduction** 

In the reinforcement learning problem, an agent interacts with its environment such that the agent both receives an observation from the environment and takes an action based on that observation. This interaction takes place at every time step, which is often the fundamental unit of time in this problem formulation. Nevertheless, several decision making problems involve operating over different time scales. The options framework (Precup, 2000; Sutton et al., 1999) is maybe the most common formalism that allows us to do so, giving agents the ability to reason in terms of actions extended in time. This framework models courses of actions as _options_ , which have the ability to accelerate learning in different ways, allowing, for example, faster credit assignment (e.g., Mann and Mannor, 2014; Solway et al., 2014), better exploration (e.g., Baranes and Oudeyer, 2013; Fruit and Lazaric, 2017), and transfer (e.g., Brunskill and Li, 2014; Konidaris and Barto, 2007). 

Despite the attention received by the options framework, it is still not clear where options should come from—a problem referred to as _option discovery_ . In this paper we argue that the _successor representation_ (SR) is a natural substrate for temporal abstractions in reinforcement learning. The SR (Dayan, 1993) is a representation that generalizes between states using the similarity between their successors, that is, the similarity between the states that follow the current state given the environment’s dynamics and the agent’s policy. It allows us to discover options that are effective not only for planning (e.g., Ramesh et al., 2019; Stachenfeld et al., 2017), but also for temporally-extended exploration (e.g., Jinnai et al., 2019b; Machado et al., 2017). The SR also allows us to combine existing options without additional learning (Barreto et al., 2019). Furthermore, recent studies suggest that the SR might be encoded in the brain (e.g., Momennejad et al., 2017; Stachenfeld et al., 2014, 2017). 

In this paper, we present a general framework for option discovery in which the agent learns a representation that is used to identify meaningful options, which are then used to improve the agent’s representation in a virtuous, never-ending, cycle (§3). To support our claim about the role of the SR for temporal abstraction, we show how we can instantiate this cycle with the SR, and how the SR is conducive to option discovery. We summarize existing methods that use the SR for option discovery, providing intuitions about the motivation behind them, and we connect papers from different contexts (§5 and §9). Moreover, regardless of how effective a discovery method is, while more options means a more expressive set of behaviors, more options often makes learning and using these options more difficult. Thus, we also discuss an approach based on the SR for combining options, the _option keyboard_ (Barreto et al., 2019), which addresses this issue by allowing the agent to extend, without extra learning, a finite set of options to a combinatorially large counterpart (§7). 

We perform numerical simulations to assess how effective options discovered by different methods are in capturing environment properties. Such an ability is particularly important for problems in which a fixed reward function is not easily defined, such as continual (Brunskill and Li, 2014; Mankowitz et al., 2018), multitask (Teh et al., 2017), and transfer learning (Taylor and Stone, 2009). We evaluate the impact of different design decisions every option discovery method needs to make (§6), and on the synergy of different approaches based on the SR (§8). We focus our discussion mostly on toy domains to provide 

2 

Temporal Abstraction in RL with the Successor Representation 

intuition without confounding factors. We review the extensions to more complex solutions when discussing relevant related work. 

Besides the sections already discussed, we present the required background in Sections 2 and 4, the related work in Section 9, and the conclusion in Section 10. While the main contributions in Sections 5 and 7 are on presenting existing results under a single formulation, the results in Sections 3, 6, and 8 are novel and have not been presented anywhere else. 

## **2. Background** 

In this section we introduce the formalism behind reinforcement learning and the options framework (Precup, 2000; Sutton et al., 1999). Throughout this paper, as a convention, we indicate scalar-valued random variables by capital letters (e.g., _St_ , _Rt_ ), vectors by bold lowercase letters (e.g., _**θ** ,_ _**φ**_ ), matrices by bold capital letters (e.g., **P** _π,_ **Ψ** _π_ ), functions by non-bold lowercase letters (e.g., _v_ , _q_ ), and sets with a calligraphic font (e.g., S _,_ A). 

## **2.1 Reinforcement Learning** 

Reinforcement learning (RL) is a problem formulation that allows us to tackle sequential decision making problems. In RL we consider an agent interacting with an unknown environment in a sequential manner, aiming to maximize cumulative reward. We often assume that the environment can be modeled as a finite Markov decision process (MDP). An MDP is formally defined as a 4-tuple _⟨_ S _,_ A _, p, r⟩_ . Starting from state _S_ 0 _∈_ S, at each time step _t_ the agent takes an action _At ∈_ A, to which the environment responds with a state _St_ +1 _∈_ S, according to a transition probability kernel _p_ ( _s[′] |s, a_ ) = _[.]_ Pr( _St_ +1 = _s[′] |St_ = _s, At_ = _a_ ), and with a bounded reward signal _Rt_ +1 _∈_ R, with _r_ ( _s, a_ ) indicating the expected reward for a transition from state _s_ under action _a_ , that is, _r_ ( _s, a_ ) = _[.]_ E[ _Rt_ +1 _| St_ = _s, At_ = _a_ ]. 

The agent’s goal is to learn a policy _π_ : S _×_ A _→_ [0 _,_ 1] that maps each state to a probability distribution over actions. Specifically, the agent seeks a policy that maximizes, in expectation, the (discounted) cumulative sum of rewards, also known as _return_ , defined as 

**==> picture [274 x 31] intentionally omitted <==**

with _γ ∈_ [0 _,_ 1), the discount factor, defining the relative value of future rewards. 

In this paper we focus on value-based methods. To obtain the policy _π_ , we estimate the state-value function, _vπ_ : S _→_ R, or the state-action value function, _qπ_ : S _×_ A _→_ R. The value of a state _s_ when following a policy _π_ , _vπ_ ( _s_ ), is defined to be the return from that state: _vπ_ ( _s_ ) = _[.]_ E _π_ � _Gt|St_ = _s_ �. The state-action value function is defined similarly, but it takes into consideration the action taken, that is, _qπ_ ( _s, a_ ) = _[.]_ E _π_ � _Gt|St_ = _s, At_ = _a_ �, where the expectation in both definitions is with respect to the policy _π_ and the probability kernel _p_ . Importantly, these functions can be defined recursively (Bellman, 1957), for example: 

**==> picture [344 x 52] intentionally omitted <==**

Machado, Barreto, and Precup 

These equations can also be written in matrix form. The state-value function, for example, can be defined with **v** _π_ , **r** _∈_ R _[|]_[S] _[|]_ , and **P** _π ∈_ R _[|]_[S] _[|×|]_[S] _[|]_ : 

**==> picture [307 x 13] intentionally omitted <==**

where **P** _π_ is the transition probability induced by _π_ , i.e., **P** _π_ ( _s, s[′]_ ) =[�] _a[π]_[(] _[a][|][s]_[)] _[p]_[(] _[s][′][|][s, a]_[).] 

In the RL problem we assume the agent does not know **P** _π_ nor _r_ beforehand. Instead, RL approaches directly estimate _vπ_ or _qπ_ from samples ( _s, a, r, s[′]_ ). Most approaches alternate between a _policy evaluation_ step, that is, estimating the value of the agent’s current policy, and a _policy improvement_ step, which defines a new policy from these estimates: 

**==> picture [282 x 19] intentionally omitted <==**

Q-Learning (Watkins and Dayan, 1992) is the most well-known algorithm that implements these ideas. It has the following update rule for the _qπ_ estimate, _Q_ : 

**==> picture [384 x 21] intentionally omitted <==**

where _α_ is the algorithm’s step-size parameter. 

When the value of each state (or state-action pair) is individually stored, this is a _tabular_ method. Nevertheless, generalization is required, and desirable, in problems with large state spaces, where it is unfeasible to learn an individual value for each state. This is done by parameterizing the function _V_ or _Q_ with a set of parameters _**θ**_ . We write, given the parameters _**θ**_ , _V_ ( _s_ ; _**θ**_ ) _≈ vπ_ ( _s_ ) and _Q_ ( _s, a_ ; _**θ**_ ) _≈ qπ_ ( _s, a_ ). In the past, a common approach was to use linear function approximation where _Q_ ( _s, a_ ; _**θ**_ ) = _**θ**[⊤]_ _**φ**_ ( _s, a_ ), in which _**θ**_ is a vector of weights and _**φ**_ ( _s, a_ ) denotes a static feature representation of the state _s_ when taking action _a_ . It is now common to use a neural network to compute a non-linear function approximation of the value function, an approach popularized by Mnih et al. (2013, 2015) with Deep Q-Network (DQN). The study of algorithms that use neural networks as function approximators has since then been dubbed _deep reinforcement learning_ . 

## **2.2 Temporal Abstraction in RL: The Options Framework** 

Sequential decision making usually involves planning, acting, and learning about temporally extended courses of actions over different time scales. In reinforcement learning, _options_ are a well-known formalization of the notion of actions extended in time that allow us to represent courses of actions (Precup, 2000; Sutton et al., 1999). We discuss them below. An option _ω ∈_ Ωis a 3-tuple 

**==> picture [267 x 12] intentionally omitted <==**

where _Iω ⊆_ S denotes the option’s initiation set, _πω_ : S _×_ A _→_ [0 _,_ 1] denotes the option’s policy, such that[�] _a[π][ω]_[(] _[·][, a]_[)][=][1,][and] _[β][ω]_[:][S] _[→]_[[0] _[,]_[ 1]][denotes][the][option’s][termination] condition, that is, the probability that option _ω_ will terminate at a given state. In this paper, we consider the _call-and-return_ option execution model in which a high-level policy, _µ_ : S _×_ Ω _→_ [0 _,_ 1], dictates the agent’s behavior. Notice that the actions originally defined in the MDP are a special case of options, that is, A _⊆_ Ω. Finally, we often write that 

4 

Temporal Abstraction in RL with the Successor Representation 

an agent _follows or takes_ an option _ω_ , meaning that the agent, in a state in _Iω_ , commits to act according to the option’s policy, _πω_ , until its termination condition is satisfied. To distinguish between options and actions, we often refer to the actions originally defined in the problem formulation as _primitive actions_ . 

Options have different use cases, including planning, exploration, and credit assignment. In this paper we mostly focus on exploration. Specifically, we discuss the _option discovery_ problem, which consists in discovering useful options from the agent’s stream of experience. In other words, we discuss different algorithms that, given a set of samples ( _s, a, s[′] , r_ ), autonomously define extended courses of actions, represented by an initiation set, a policy, and a termination condition, such that they allow for temporally-extended exploration. The algorithms we discuss can all be cast as part of a general framework for option discovery, which we discuss in the next section. In subsequent sections we show how different algorithms instantiate this framework. 

## **3. A Framework for Option Discovery from Representation Learning** 

We first introduce a general approach for option discovery that is driven by the representation learning process. It follows a constructivist approach (Piaget, 1963) depicted as a cycle in which options discovered from previous iterations act as a scaffold for more complex behaviours discovered in subsequent iterations. The framework depicted in Figure 1 distills the main steps of this cycle. Note that, while we present these steps sequentially, they can be executed concurrently, at different time scales. Below we further discuss each step. 

**==> picture [344 x 107] intentionally omitted <==**

**----- Start of picture text -----**<br>
Derive intrinsic<br>Collect Learn<br>reward function<br>samples representation<br>from learned repr.<br>Option Define Learn to maximize<br>set option intrinsic reward<br>**----- End of picture text -----**<br>


Figure 1: Representation-driven Option Discovery (ROD) cycle (Machado, 2019). The option discovery algorithms discussed in this paper can be seen as instantiating this cycle. The incoming arrow to _collect samples_ depicts the start of the process. The arrow from _define option_ to _option set_ highlights the output generated by the ROD cycle. Note that other generated artifacts can also be used by the agent outside the ROD cycle, such as the learned representation. 

**Collect samples:** The first step in each iteration of the ROD cycle is to have the agent collect data in the form of trajectories. Selecting actions uniformly at random is an obvious first choice for the agent’s policy because the agent has no information about the environment: it is at the start of its life. Once the agent starts to be able to follow the options’ policies, more possibilities for this step become available. 

5 

Machado, Barreto, and Precup 

**Learn representation:** In most problems of interest, the agent should learn a representation of its environment while acting in the world. Methods that are reward agnostic can be easier to implement, especially in early learning. In this paper, we focus on the _successor representation_ as the output of this step, because, as we discuss in the next section, it naturally captures the dynamics of the environment. 

**Derive intrinsic reward function from learned representation:** After a representation is learned, the agent can use it to define an intrinsic reward function which an option should maximize. The algorithms we discuss here either use spectral analysis or some clustering of the successor representation to define this _intrinsic_ reward function. The first is often associated with more efficient exploration while the latter usually leads to more efficient credit assignment. 

**Learn to maximize intrinsic reward:** Once a representation has been learned and the intrinsic reward function has been defined, the agent needs to learn to maximize the (discounted) sum of these rewards, which is a standard reinforcement learning problem. The learned policy is the policy of this new option being discovered. This can be done in parallel for multiple options, with off-policy learning. 

**Define option:** Finally, there are different ways to define the option’s initiation set and termination condition, which give rise to different algorithms (e.g., Jinnai et al., 2019b; Machado et al., 2017). We discuss several possibilities in Sections 5 and 6 when introducing and evaluating instantiations of this framework. The output of this step can be immediately incorporated into the agent’s option set, but it can also be used in the next iteration of the ROD cycle, improving the data collection step, which then allows the discovery of more complex options. 

As previously mentioned, the ROD cycle can be agnostic to the ultimate reward function that the agent may want to optimize. This is particularly important when aiming at discovering options for temporally-extended exploration. If the option discovery process consists in learning options that, for example, replicate new observations (e.g., new feature activations, state visitation), new options might allow the agent to better navigate in the environment by making events that were rare, or virtually impossible, more likely. Figure 2 presents a concrete example of this behaviour. 

## **4. The Successor Representation** 

The successor representation (SR; Dayan, 1993) is a classic method for automatically extracting a representation from the agent’s observation, giving an answer to what representations one should use when performing function approximation. In this paper, we claim that the SR could be the natural substrate for temporal abstraction in reinforcement learning, as it is a representation learning method conducive to the discovery and use of options. The algorithms we present, one way or another, use the SR as representation when 

6 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [423 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) collected samples (c) collected samples<br> …<br>(b) discovered option (d) discovered option<br>**----- End of picture text -----**<br>


- Figure 2: Two ROD cycles in the Pinball domain (Konidaris and Barto, 2009), originally presented by Jinnai et al. (2020). Blue dots denote state visitation, green lines the options’ trajectories, and shaded regions the states in which the options terminate. The agent follows a random walk in every iteration. The agent first struggles to go through some narrow passages, as we can see in the samples collected at the first iteration of the ROD cycle (Fig. 2a). At the end of the cycle, the discovered option takes the agent to the boundary of the region it visited often (Fig. 2b). This new option enables the agent to visit regions that were originally hard to reach with a random walk, as we can see when looking at the samples collected in the second iteration (Fig. 2c). These samples were generated by the agent following a policy that uniformly chooses between the primitive actions and the option discovered in the previous iteration. This process can, of course, be further refined. Fig. 2d depicts the option discovered at the end of the second iteration. 

instantiating the ROD cycle. This is due to the fact that it has a particular structure that captures the dynamics of the environment, as we discuss below. 

## **4.1 Tabular Setting** 

The SR is a representation that captures the underlying environment dynamics. It does so by assigning similar values to states that are close in time; in other words, the notion of similarity between states is based on how similar their successor states are under a policy _π_ . Formally, the SR is defined to be the current and expected future occupancy of state _s[′]_ given the agent’s policy is _π_ and its starting state is _s_ . 

The SR, with respect to a policy _π_ , **Ψ** _π_ , is defined as 

**==> picture [314 x 33] intentionally omitted <==**

where 1 denotes the indicator function and _γ ∈_ [0 _,_ 1). Thus, each state _s_ is represented as an _|S|_ -dimensional vector whose _i_ -th component is the expected discounted visitation to each state in the environment. Figure 3 illustrates this concept. 

7 

Machado, Barreto, and Precup 

**==> picture [412 x 124] intentionally omitted <==**

**----- Start of picture text -----**<br>
C A<br>B<br>**----- End of picture text -----**<br>


- Figure 3: Example similar to Dayan’s (1993) of the SR, w.r.t. the uniform random policy, of state A (left). Recall the SR of a state, in the tabular case, is an _|S|_ -dimensional representation, thus allowing us to depict it as a heatmap over the state space. Red represents larger values while blue represents smaller values (states that are temporally further away). The Euclidean distance between states A and C is smaller than the Euclidean distance between states A and B. However, if one considers the gray tiles to be walls, an agent in state A can reach state B much _quicker_ than state C. The SR captures this distinction, ensuring that, in this representation, state A is closer to state B than it is to state C. 

Importantly, the SR can be estimated from samples with temporal-difference learning methods (Sutton, 1988), where the reward function is state occupancy: 

**==> picture [364 x 34] intentionally omitted <==**

for all _j ∈_ S, where _η_ is the step-size. In fact, the SR can also be seen as a collection of general value functions (Sutton et al., 2011) with a fixed discount factor and individual state visitation as cumulants. In this case, instead of seeing the SR as a representation, one would see it as a collection of predictions. 

The SR also corresponds to the Neumann series of _γP_ : 

**==> picture [305 x 31] intentionally omitted <==**

Thus, one can see the SR as an estimate of how often the agent expects to visit each state in the future, weighted by the discount factor. In fact, the SR is part of the solution when computing a value function (see Eq. 3): 

**==> picture [292 x 13] intentionally omitted <==**

In words, one can compute the return by multiplying the SR and the estimates of expected _immediate_ rewards in each state. This sum of weighted rewards relies on the SR to provide the weights, which encodes expected future state visitation. 

8 

Temporal Abstraction in RL with the Successor Representation 

The SR can be presented in multiple ways based on the several connections it has to other results in the field. The matrix in Eq. 9 is also known, for example, as the LSTD matrix (Lagoudakis and Parr, 2003). We further discuss some of these connections after presenting the generalization of the SR to the function approximation case. 

## **4.2 Successor Features: From States to Features** 

The definitions given so far for the SR are limited to the tabular case. We now discuss _successor features_ (SFs; Barreto et al., 2017), which are a generalization of the SR that can be extended to the function approximation setting. 

Let _**φ**_ : S _×_ A _�→_ R _[d]_ be a function that computes _features_ . The SFs of policy _π_ are 

**==> picture [345 x 34] intentionally omitted <==**

In words, _**ψ** π,i_ ( _s, a_ ) encodes the discounted expected value of the _i_ -th feature in the vector _**φ**_ ( _·, ·_ ) when the agent starts in state _s_ , executes action _a_ , and follows policy _π_ thereafter. The features _**φ**_ ( _·, ·_ ) can be either given to the agent or learned, as we discuss in Section 9. The update rule presented in Eq. 8 can be naturally extended to this definition. 

SFs are a strict generalization of the SR. To see why this is so, suppose that S is finite and let _**φ**_ ( _s, a_ ) = _**φ**_ ( _s_ ) for all ( _s, a_ ) _∈_ S _×_ A (that is, _**φ**_ is a function of states only). Then, we can rewrite the definition of SFs in matrix form as 

**==> picture [304 x 31] intentionally omitted <==**

where **Φ** _∈_ R _[|]_[S] _[|×][d]_ is a matrix encoding the feature representation of each state. When _d_ = _|_ S _|_ , if we define _**φ** i_ ( _sj_ ) = 1 _{i_ = _j}_ , Eq. 12 reduces to Eq. 9. Again, this highlights the fact that the SR can be seen as the discounted state visitation distribution induced by policy _π_ . 

The connection between the SR and SFs also allows us to generalize Eq. 10. Assume there exists a _**w** ∈_ R _[d]_ such that 

**==> picture [316 x 14] intentionally omitted <==**

Based on the definition of _qπ_ one can to show that (Barreto et al., 2017) 

**==> picture [321 x 14] intentionally omitted <==**

Again, when _d_ = _|_ S _|_ and _**φ** i_ ( _sj, a_ ) = 1 _{i_ = _j}_ for all _a ∈_ A, Eq. 14 reduces to Eq. 10. Note that, once we have the SFs _**ψ** π_ of a policy _π_ , Eq. 14 allows us to instantaneously evaluate _π_ under any reward that can be represented as a linear combination of the features _**φ**_ (Eq. 13). This has been exploited in the past for transfer between tasks (Barreto et al., 2017, 2018). 

9 

Machado, Barreto, and Precup 

## **4.3 Proto-value Functions and their Equivalence to the Eigenvectors of the SR** 

As aforementioned, the SR is present in several RL algorithms, either explicitly or implicitly. An important result for this paper is that the eigenvectors of the SR are equivalent to protovalue functions (PVFs; Mahadevan, 2005; Machado et al., 2018).[1] We rely on this result to be able to also discuss algorithms originally presented under the PVFs formalism. The properties of the eigenvectors of the SR (i.e., PVFs) are particularly relevant to justify option discovery methods. Because these properties were first discussed in the PVFs literature, we further discuss PVFs and their properties in this section. 

PVFs were originally introduced as representations that reflect the geometry of the environment. Specifically, they are basis functions based on the notion of diffusion models (Coifman et al., 2005; Kondor and Lafferty, 2002), which capture how information flows in the environment by modeling it as a graph connecting states that are one action away from each other. This is motivated by the fact that value functions can be seen as the result of rewards diffusing through the state space, governed by the environment dynamics (Mahadevan and Maggioni, 2007). Formally, PVFs are the eigenvectors of a symmetric diffusion operator such as the _normalized Laplacian_ , 

**==> picture [285 x 16] intentionally omitted <==**

where **W** is the graph’s adjacency matrix and **D** the diagonal matrix whose entries are the row sums of **W** . In the simplest setting, for states _si_ and _sj_ , the _ij_ -th entry of matrix **W** is 

**==> picture [154 x 28] intentionally omitted <==**

for any action _a ∈_ A. Notice the matrix **W** can potentially be extended to a weight matrix. 

These diffusion models are tightly related to the random walk diffusion model **D** _[−]_[1] **W** . A diffusion model works as a surrogate that is easier to estimate than the full transition matrix, while being useful for value function approximation because we can represent the value function as a linear combination of the eigenvectors of the transition matrix, as shown in Eq. 3. See the work by Mahadevan and Maggioni (2007) for a detailed discussion. 

The formal result of equivalence between PVFs and the eigenvectors of the SR is below. 

**Theorem 1 (Machado et al. 2018)** _The i-th eigenvalue (λSR,i) of the SR, defined with respect to a uniform random policy, and the j-th eigenvalue (λPVF,j) of the normalized Laplacian are related as follows when in a symmetric and deterministic environment :_ 

**==> picture [142 x 21] intentionally omitted <==**

_The i-th eigenvector (_ **e** _SR,i) of the SR and the j-th eigenvector (_ **e** _PVF,j) of the normalized Laplacian are related as follows:_ 

**==> picture [114 x 14] intentionally omitted <==**

_where i_ + _j_ = _n_ + 1 _, for both the eigenvectors and the eigenvalues; with n being the total number of rows (and columns) of matrix_ **P** _π._ 

> 1. This holds when the SR is defined w.r.t. the uniform random policy in a deterministic and symmetric environment. The cardinality of the action set should also be the same across all states. 

10 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [74 x 78] intentionally omitted <==**

**==> picture [63 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) Four-room<br>**----- End of picture text -----**<br>


**==> picture [100 x 81] intentionally omitted <==**

**==> picture [100 x 81] intentionally omitted <==**

**==> picture [100 x 81] intentionally omitted <==**

**==> picture [286 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
(b) First PVF (c) Second PVF (d) Third PVF<br>**----- End of picture text -----**<br>


- Figure 4: First three PVFs in the **(a)** four-room domain. Gray squares represent walls and white squares represent accessible states. Four actions are available: _up_ , _down_ , _right_ , and _left_ . The transitions are deterministic and the agent is not allowed to move into a wall. **(b–d)** These plots depict the first, second, and third eigenvectors associated with each state. The axes are rotated for clarity. The bottom left corner of the four-room domain is the state closer to the reader. 

## **Proof** See Appendix A. 

This result highlights the connection between SR and PVFs in a symmetric and deterministic MDP, that is, when every transition is reversible and action outcomes are deterministic. Importantly, the SR reduces to PVFs in a more restrictive case, but the SR is also applicable to the more general case, allowing us to more easily capture stochasticity and asymmetries in the environment. 

Figure 4 presents a visualization of the first three PVFs in the four-room domain (those with the corresponding smallest eigenvalues). Intuitively, PVFs capture temporal properties of an environment, with different eigenvectors capturing different time-scales of diffusion, a hallmark of Fourier analysis. The eigenvectors with corresponding smaller eigenvalues capture longer time-scales, such as in Figures 4b and 4c, in which the biggest difference is seen between the two states that are furthest apart: the different diagonals in the environment. On the other hand, eigenvectors with corresponding larger eigenvalues exhibit shorter timescales, such as in Figure 4d, in which the period of the curves depicted is already shorter – the distance between the states with largest and smallest values is smaller. Similar to value functions, PVFs are smooth, with the value of each state being a function of its neighbors. 

As previously mentioned, PVFs were introduced as basis functions for function approximation. Nevertheless, PVFs ended up not being widely adopted. We are not interested in the use of PVFs as basis functions. This is a major difference from how PVFs were used in the past. We are advocating the use of these concepts for the discovery and combination of temporal abstractions. Moreover, the singular vectors of the SR can already be seen as a generalization of PVFs. Thus, the shortcomings of PVFs in the past should not be carried over when discussing their use for temporal abstraction. 

11 

Machado, Barreto, and Precup 

## **5. Temporally-Extended Exploration** 

To exemplify how the SR can be used for option discovery, we now discuss different methods that instantiate the ROD cycle using the SR as representation. In this section, we focus on discovering options useful for temporally-extended exploration. Specifically, we consider options that can be used by the agent, alongside primitive actions, when following a random walk. When an option is selected, instead of a primitive action, the agent acts according to the option’s policy until its termination condition is satisfied. 

Temporally-extended exploration with options is based on the intuition that agents explore the environment more effectively if they operate at a higher-level of abstraction. When acting according to options’ policies, agents exhibit more directed behavior in contrast to the aimless dithering commonly observed when selecting primitive actions uniformly at random (Dabney et al., 2020; Jinnai et al., 2019b; Machado and Bowling, 2016; Machado et al., 2017). Intuitively, if one needs to explore, say, a building, it makes more sense to do so in terms of rooms than in terms of motor twitches. In fact, such an approach has been used as a solution for the exploration problem in one of the recent high-profile success stories in artificial intelligence: the deployment of a reinforcement learning algorithm to navigate superpressure balloons in the stratosphere (Bellemare et al., 2020). 

In this section, we discuss _eigenoptions_ (Machado et al., 2017, 2018) and _covering options_ (Jinnai et al., 2019b, 2020). They instantiate the ROD cycle in different ways while using the SR as representation. These methods, and others (e.g., Bar et al., 2020), use the eigenspectrum of the learned representation to guide the option discovery process. They are representative of a class of methods that is motivated by the fact that the eigenvectors of the SR naturally encode the diffusion properties of the environment due to their close relationship to the graph Laplacian, as discussed in the previous section. 

In this and in the next section, we use the differences between eigenoptions and covering options to highlight (and evaluate) some of the choices one can make when instantiating the ROD cycle. Specifically, we discuss different ways of using the eigenvectors of the SR, the design of the intrinsic reward function that guides learning of the options’ policy, the definitions of the options’ initiation set and termination condition, and how these choices impact the design of online versions of these algorithms. 

## **5.1 Eigenoptions** 

Eigenoptions are options defined by the eigenvectors of the SR.[2] Each eigenvector assigns an intrinsic reward to every state in the environment. An eigenoption is an option, defined with respect to a specific eigenvector, that takes the agent to the state with largest (or smallest) value. Intuitively, what an eigenoption does is to ensure that there is an option that directly takes the agent to the state that was originally difficult to get to. 

This description becomes clearer with an example. In the four-room domain, the second largest eigenvector of the SR, defined w.r.t. a uniform random policy, is depicted in Figure 5 (the top eigenvector of the SR is constant). In this environment, the two states that are 

> 2. Machado et al. (2017) originally defined eigenoptions in terms of PVFs. Later, Machado et al. (2018) used the equivalence between PVFs and the eigenvectors of the SR to generalize eigenoptions to the setting in which the representation, that is, the SR, is learned online. 

12 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [139 x 111] intentionally omitted <==**

**==> picture [111 x 111] intentionally omitted <==**

**==> picture [111 x 111] intentionally omitted <==**

Figure 5: Second eigenvector of the SR and the two corresponding eigenoptions in the fourroom domain. The actions of the deterministic policy are depicted as arrows and the state in which the option terminates is depicted in red (in the corners). 

furthest apart are the states diagonally opposed in the corners, which is what the depicted eigenvector captures. The corresponding eigenoptions take the agent to one of those states. 

**Learning the eigenoptions’ policies.** To specify an option we need to define its policy, initiation set, and termination condition. An eigenoption’s policy is defined by the intrinsic reward function _r_ **[e]** ( _s, s[′]_ ), obtained from the eigenvector **e** _∈_ R _[d]_ of the SR. It is defined as 

**==> picture [292 x 15] intentionally omitted <==**

where _**φ**_ ( _s_ ) denotes the feature representation of state _s_ . Notice that, in the tabular case, if we define _**φ**_ ( _s_ ) to be an _|_ S _|_ -dimensional one-hot encoding of state _s_ , _r_ **[e]** ( _s, s[′]_ ) becomes 

**==> picture [106 x 13] intentionally omitted <==**

Importantly, the sign of an eigenvector is arbitrary. Thus, as aforementioned, this reward function can be interpreted as incentivizing the agent to go to either the highest or the lowest point of the graph shown in Figure 5. In this example, these correspond to the top right and bottom left states in the environment. 

We learn the option’s policy in a newly defined MDP _M_ **[e]** = _⟨_ S _,_ A _∪{⊥}, r_ **[e]** _, p, γ⟩_ , where the state space and the transition probability kernel remain unchanged. The reward function is defined as in Eq. 16 and the action set is augmented by the action _terminate_ ( _⊥_ ), which allows the agent to leave _M_ **[e]** at no cost, returning to the original MDP in the same state it was when it left _M_ **[e]** . The discount factor can be chosen arbitrarily, although it impacts the timescale the option encodes by defining how myopic the agent will be w.r.t. _r_ **[e]** . In this formulation, eigenoptions ignore the reward signal provided by the original MDP, but it is not difficult to imagine extensions in which this is not the case (e.g., Liu et al., 2017). 

With _M_ **[e]** , we define the state-value function _vπ_ **[e]**[(] _[s]_[), for policy] _[ π]_[, as the expected value of] the cumulative discounted intrinsic reward if the agent starts in state _s_ and follows policy _π_ until termination. We define the action-value function _qπ_ **[e]**[(] _[s, a]_[)][similarly.][The][optimal][value] function for any intrinsic reward function obtained through **e** is then described as 

**==> picture [254 x 16] intentionally omitted <==**

13 

Machado, Barreto, and Precup 

The option’s policy, _π∗_ **[e]**[, is the optimal policy w.r.t.][the intrinsic reward function] _[ r] i_ **[e]**[, i.e.,] 

**==> picture [118 x 19] intentionally omitted <==**

Thus, finding the option’s policy _π∗_ **[e]**[becomes][a][traditional][RL][problem,][with][a][different][re-] ward function. Importantly, the reward received for transitioning from one state to another is rarely zero, avoiding challenging exploration issues caused by sparse non-zero rewards. **Defining the eigenoptions’ initiation sets and termination conditions.** When defining the MDP to learn the option’s policy, we augment the agent’s action set with the _terminate_ action so the agent can terminate the option. The termination condition is deterministic, with eigenoptions terminating when the agent is unable to accumulate further positive intrinsic rewards. This happens when the agent reaches the state with largest value assigned by the corresponding eigenvector (or a local maximum when _γ <_ 1). Any subsequent sum of rewards will be at most zero. We formalize this condition by defining 

**==> picture [160 x 27] intentionally omitted <==**

where _qπ_ **[e]**[+] denotes the state-action value function, defined by _π_ and _r_ **[e]** , augmented by the terminate action, which has value zero. When the terminate action is selected, control is returned to the higher level policy. In summary, because we break ties in favour of the terminate action, an option following a policy _π_ **[e]** terminates when _qπ_ **[e]**[(] _[s, a]_[)] _[ ≤]_[0 for all] _[ a][ ∈]_[A][.] The initiation set is defined to be the complement of the set of states in which an option terminates, i.e., all states in which there exists an action _a ∈_ A s.t. _qπ_ **[e]**[(] _[s, a]_[)] _[ >]_[ 0. In summary,] an eigenoption consists of a policy _π_ **[e]**[+] , which is augmented by the _terminate_ action, 

**==> picture [292 x 22] intentionally omitted <==**

The termination and initiation sets are implicitly defined. That is, for an eigenoption _ω_ **[e]** , _βω_ **[e]** ( _s_ ) = 1 if _qπ_ **[e]**[(] _[s,][ ·]_[)] _[ ≤]_[0,][and] _[β][ω]_ **[e]**[(] _[s]_[) = 0][if][there][is][an][action] _[a][ ∈]_[A][such][that] _[q] π_ **[e]**[(] _[s, a]_[)] _[ >]_[ 0.] In this second case, _s ∈Iω_ **[e]** . In practice, this means the option terminates in states that are assigned the (locally) largest values in the eigenvector; the option can be initialized in all other states. Importantly, for any eigenoption, there is always at least one state in which it terminates. The theorem below formalizes this result. 

**Theorem 2 (Machado et al. 2017)** _Let ω_ = _⟨Iω, πω, βω⟩ denote an eigenoption. In a finite and ergodic MDP with γ ∈_ [0 _,_ 1) _, there is at least one state s ∈_ S _such that βω_ ( _s_ ) = 1 _._ 

**Proof** See Appendix A. 

This result is due to the fact that the reward function resembles a potential function (Ng et al., 1999). It is not clear if it would be possible to obtain such a natural termination criteria if the agent maximized, for example, the feature itself, as in _r_ **[e]** ( _s_ ) = **e** _[⊤]_ _**φ**_ ( _s_ ). 

14 

Temporal Abstraction in RL with the Successor Representation 

Eigenoptions have several interesting properties that allow them to improve exploration. One of them is that different eigenoptions have different durations, effectively letting the agent operate at different time scales. We exemplify this in Figure 6, where we show how the eigenoptions discovered first tend to be longer (i.e., those discovered from eigenvectors with corresponding larger eigenvalues). We overlay a linear regression of the data to emphasize this trend. Besides their duration, eigenoptions can be easily sequenced, and they are taskindependent because, as the SR, they do not depend on information related to the reward function. Nevertheless, there could be twice as many eigenoptions as states in the environment and it is not clear how to choose the number of desired options. Covering options (Jinnai et al., 2019b), discussed next, are an attempt to address this issue. 

**==> picture [196 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
Linear regression<br>**----- End of picture text -----**<br>


- Figure 6: Average length of different eigenoptions by the order they are discovered. The linear regression emphasizes the downward trend on the option length. 

## **5.2 Covering Options** 

Covering options are options defined by the bottom eigenvector of the graph Laplacian, that is, the eigenvector with the smallest corresponding eigenvalue.[3] They have the explicit goal of minimizing the environment’s expected cover time – the number of steps required for a random walk to visit every state (Broder and Karlin, 1989). The intuition behind them is similar to the one behind eigenoptions, as they exploit the fact that the bottom eigenvector of the graph Laplacian captures the states that are furthest apart in the environment. Nevertheless, a covering option is defined as a _point option_ (Jinnai et al., 2019a) connecting only two states. It explicit adds an edge to the graph representing the underlying MDP to connect the two furthest vertices in that graph, in an attempt to shrink its diameter. They are obtained with an iterative procedure in which, after the discovery of each option, the environment’s underlying graph is updated and the option discovery procedure is executed again. Eigenoptions can be seen as adding multiple edges to the graph, connecting every state in the initiation set to one of the terminal states. Covering options are discovered one at a time and connect only two states. We analyze the impact of these choices in Section 6. 

The description of covering options becomes clearer with an example. In the four-room domain, the bottom eigenvector of the graph Laplacian, defined w.r.t. a uniform random policy, is depicted in Figure 7, as well as its corresponding covering options (notice the eigenvector is equivalent to the one depicted in Figure 5). In this environment, the two 

> 3. The eigenvector of the graph Laplacian with corresponding smallest eigenvalue is constant, so we refer to the second smallest one here. Notice that when using the SR, the order of these eigenvectors is flipped, explaining why eigenoptions use the top eigenvector of the SR (see Theorem 1). 

15 

Machado, Barreto, and Precup 

**==> picture [134 x 110] intentionally omitted <==**

**==> picture [110 x 110] intentionally omitted <==**

**==> picture [110 x 109] intentionally omitted <==**

Figure 7: Second eigenvector of the graph Laplacian and corresponding covering options in the four-room domain. The actions of the deterministic policy are depicted as arrows and the state in which the option terminates is depicted in red. 

states that are furthest apart are the states diagonally opposed in the corners. Covering options connect those two states, allowing the agent to easily navigate between them. 

**Learning the covering options’ policies.** Formally, a covering option’s policy is defined by the intrinsic reward function _r_ **[e]** ( _s, s[′]_ ), obtained from the non-constant eigenvector **e** _∈_ R _[d]_ of the graph Laplacian that has the smallest corresponding eigenvalue. It is defined as 

**==> picture [181 x 34] intentionally omitted <==**

In words, arriving at the state in which the eigenvector has the corresponding largest value leads to a reward of 1. The same reward function is applied to the negation of the eigenvector so the agent can also learn an option that leads to the state with smallest value. 

This reward function is arguably simpler than the reward function used by eigenoptions, but it does not provide the agent with a gradient to follow when learning the option’s policy, which might lead to exploration issues. We further discuss the pros and cons of each choice in the next sections. 

**Defining the covering options’ initiation sets and termination conditions.** Because these are point options, their initiation sets and termination conditions are trivially defined. The initiation set has a single state, the one with corresponding smallest value in the considered eigenvector. Covering options terminate with probability 1 when they reach the state with corresponding largest value. Formally, for a covering option _ω_ **[e]** , 

**==> picture [365 x 34] intentionally omitted <==**

In which we overloaded the notation to have _Iω_ **[e]** ( _s_ ) denoting whether state _s_ belongs to the initiation set of option _ω_ **[e]** or not. As before, we evaluate _±_ **e** . This can obviously lead to problems when reaching an individual state is unlikely (e.g., large/continuous state-spaces). Recently, Jinnai et al. (2020) extended this notion to a region of the state-space. 

16 

Temporal Abstraction in RL with the Successor Representation 

**Iterative discovery of covering options.** While the formulation of eigenoptions does not prescribe the number of options to be used, there always exist exactly two covering options associated with an SR. In order to get more covering options, one must compute an updated SR induced by the newly-added options and then use its dominant eigenvectors to compute two new options. This process can be repeated multiple times, resulting in an iterative procedure in which two covering options are added at each iteration. Thus, while eigenoptions work well with a single iteration of the option discovery cycle, learning multiple options in parallel, covering options require a much lighter iteration, but several of them. 

Importantly, essentially every iteration is guaranteed to improve the upper bound of the expected number of steps an agent would need, when following a uniform random policy, in order to visit every state in the environment. We refer the reader to the work by Jinnai et al. (2019b) for the formal statement behind this result. 

Covering options provide a much simpler approach for option discovery. This approach discovers a fixed number of options at each iteration, the intrinsic reward function the agent needs to maximize is trivial, as well as the definitions of the initiation set and termination condition. Nevertheless, it is not clear that this simplicity implies better empirical performance. Is it empirically better to use the full spectrum of the graph Laplacian or only the bottom eigenvector? Do covering options face an exploration issue when learning the option’s policy? Are point options more effective than options defined in the whole state space? We empirically evaluate these different choices in the next section, further discussing the differences between eigenoptions and covering options. 

## **6. Evaluation of Temporally-Extended Exploration with Options** 

Machado et al. (2017, 2018) and Jinnai et al. (2019b, 2020) have already presented empirical evidence about the efficacy of the approaches discussed in the previous section. Thus, we focus instead on comparing components of these approaches. Our goal is to better understand the impact of the choices made by eigenoptions and covering options on how they use the eigenvectors of the SR, and on the initiation and termination sets. We evaluate these choices in the context of temporally-extended exploration, when using options to provide persistent behaviors inside uniformly random policies. This analysis also allows us to highlight different choices that can be made when instantiating the ROD cycle. 

Because we are interested in the agent’s exploration capabilities in a given environment, irrespective of a specific reward function, we use the _diffusion time_ as the main evaluation metric. The diffusion time reflects the expected number of decisions[4] required to navigate between any two states while following a random walk (Dayan and Hinton, 1992; Machado et al., 2017). A small expected number of decisions implies that the agent is more likely to reach any state with a random policy. The diffusion time captures the agent’s ability to learn about the structure of the environment, and it is particularly relevant in settings without a single, fixed task, such as continual (Brunskill and Li, 2014; Mankowitz et al., 2018), multitask (Teh et al., 2017), and transfer learning (Taylor and Stone, 2009). Moreover, the diffusion time allows us to summarize more easily a large number of results. While we 

> 4. We use the term _decisions_ instead of steps to estimate the likelihood that a sequence of random choices will lead to the desired state. 

17 

Machado, Barreto, and Precup 

will use this metric throughout most of the paper, in Section 6.2 we will also evaluate how eigenoptions and covering options impact the speed at which agents accumulate rewards. 

In tabular domains, we can easily compute the diffusion time with dynamic programming. We do so by defining an MDP in which the value function of a state _s_ , under a uniform random policy, encodes the expected number of decisions required to navigate between state _s_ and a chosen goal state. We can compute the expected number of decisions between any two states by setting one as the goal and checking the value of the other. We can then compute the expected number of decisions across the entire state space by averaging over all possible pairs of initial state and goal state. The MDP in which the value function of state _s_ encodes the expected number of decisions from _s_ to a goal state has _γ_ = 1 and a reward function of +1 at every decision that does not lead to the goal state. Policy evaluation computes the expected number of decisions the agent will take before arriving to the goal state. When computing the diffusion time, we iterate over all possible states, defining them as terminal states. We report both average and median as summary statistics of diffusion time in this paper. 

To provide a direct comparison between eigenoptions and covering options, in Section 6.1 we evaluate the agent’s diffusion time induced by these approaches. In Section 6.2, we check how the insights obtained from this comparison impact reward maximization. In Section 6.3, we evaluate the impact of different approaches for defining the options’ initiation sets and termination conditions, and of using the whole eigenspectrum of the successor representation. We report our last set of experiments in Section 6.4, when we discuss how these algorithms behave in the online setting. We summarize our findings in Section 6.5. 

## **6.1 Diffusion Time of Eigenoptions and Covering Options** 

We report the diffusion time obtained by eigenoptions and covering options in Figure 8. We use the four-room domain (Sutton et al., 1999), which we implemented with Gym-Minigrid (Chevalier-Boisvert et al., 2018). For simplicity, we consider deterministic transitions and we compute both sets of options in closed form. 

The average diffusion time we report for eigenoptions is similar to what Machado et al. (2017) reports. Covering options had not been evaluated under this metric yet.We observe that after a sufficient number of options becomes available, eigenoptions lead to a smaller diffusion time, although they lead to much worse performance with fewer options. Figure 8 shows that once options start to outperform primitive actions, given the same number of options, eigenoptions lead to a lower diffusion time. This can be interpreted that it is better to use options derived from, say, the top ten eigenvectors of the SR, as done by eigenoptions, than to use the top eigenvector of the SR in ten successive iterations, as done by covering options.[5] This is supported by other results that also show the benefits of looking beyond the first eigenvector of time-based representations (Bar et al., 2020). 

Aside from the number of eigenvectors they use, another difference between eigenoptions and covering options is with respect to how the options are defined. While an eigenoption is 

> 5. In these experiments, for covering options, we used the eigenvectors of the Laplacian because we are computing them in closed form and also because, differently than the SR, it does not lead to eigenvectors with a complex component. We further discuss this issue in Section 6.4 and Appendix D. 

18 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [359 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 [6]<br>1400 10 [7] 1400<br>10 [4]<br>10 [4]<br>1100 1100<br>10 [2]<br>800 0 10 20 30 800 0 10 20 30<br>500 500 Eigenoptions<br>Covering Options<br>Primitive Actions<br>200 200<br>0 10 20 30 0 10 20 30<br>Number of Options Number of Options<br>Diffusion Time Diffusion Time<br>**----- End of picture text -----**<br>


Figure 8: Comparison between the agent’s average (left) and median (right) diffusion time in the four-room domain when using covering options and eigenoptions. The inset plots depict, in log-scale, the range in which the diffusion time lies. 

defined in the whole state space, the initiation set of a covering option has a single state. The main consequence of this is that at the beginning, before the options sufficiently connect the underlying graph, eigenoptions tend to create some sink states. The agent needs to take enough random actions to reach a state while also _not_ choosing, by chance, options that move it away from the desired state. This explains the much worse performance of eigenoptions when fewer options are added. Point options have a less pervasive effect. 

There is a stark difference between the reported average and median diffusion time. The average diffusion time is heavily impacted by outliers while the median diffusion time is more representative of performance for a random pair of states. As options are added, most of the states become easier to reach. However, without enough options, it is very difficult to reach states that are far from the options’ terminal states. The average diffusion time captures this dichotomy. It has very high values at first because the options (mainly eigenoptions) make some states almost impossible to reach. The median is not impacted by these worst-case scenarios. It is particularly impressive to see that covering options, even with a single option, are already capable of reducing an agent’s median diffusion time. 

## **6.2 Maximizing Rewards after Temporally-Extended Exploration** 

A natural question to ask is how eigenoptions and covering options impact an agent’s ability to accumulate reward in a single, fixed task. We answer this question in the setting in which agents learn the values of primitive actions while being allowed to also act according to the options’ policies. In this setting, options do not incur an additional cost in terms of sample complexity (Brunskill and Li, 2014) because the agent does not learn state-option values. Nevertheless, the agent is still able to exhibit temporally extended-exploration when acting with respect to an option’s policy. Specifically, we use Q-learning (Watkins and Dayan, 1992) to learn the agent’s policy with _ϵ_ -greedy exploration. When an exploratory step is chosen, the agent randomly chooses amongst all primitive actions and options with 

19 

Machado, Barreto, and Precup 

**==> picture [427 x 126] intentionally omitted <==**

**----- Start of picture text -----**<br>
800 800<br>No options<br>600 600 4 options<br>S 8 options<br>16 options<br>400 400<br>200 200<br>G<br>0 10 20 30 40 50 0 10 20 30 40 50<br>Number of Episodes Number of Episodes<br>(a) Task (b) Eigenoptions (c) Covering options<br>Number of Steps to Goal Number of Steps to Goal<br>**----- End of picture text -----**<br>


Figure 9: Performance of Q-learning augmented with eigenoptions and covering options. In the task, S and G denote the start and goal state. Results are averaged across 50 runs and shaded regions denote a 99% confidence interval. See text for details. 

equal probability. When an option is selected, the agent acts according to the option’s policy until it terminates, while updating, off-policy, the value of each of the primitive actions taken. Additionally, this evaluation allows us to evaluate the setting in which the number of steps taken by the agent matter. While the diffusion time ignores the set of states visited by the agent when following an option, the off-policy updates we use do not. 

We evaluated our agents in the four-room domain with the agent having access to a varied number of options. We used ten tasks defined by different, randomly sampled, start and goal states. Episodes were at most 1000 steps long and we evaluated the agents for 50 episodes. The agent observes a reward signal of 0 until reaching the goal, when it observes a reward signal of +1. We use Q-learning with parameters _α_ = 0 _._ 1, _γ_ = 0 _._ 9, and _ϵ_ = 0 _._ 05. We use the options pre-computed from the previous section, adding them to the agent’s option set according to their corresponding eigenvalue (or iteration), as previously discussed. 

Figure 9 depicts the performance of an agent augmented with eigenoptions or covering options. We chose a representative setting amongst the ten tasks. The results for the other nine tasks can be found in Appendix B. We observe that, for eigenoptions, as few as four options are enough to accelerate learning. We did not observe four eigenoptions hurting agent’s performance in any of the ten tasks we randomly sampled. On the other hand, surprisingly, covering options did not improve the agent’s performance. This was consistent across the ten tasks. We conjecture this is due to the sparse initiation set that reduces the effectiveness of covering options in the online setting because they are rarely sampled. Although this may be alleviated by the use of an agent that also learns option values, this strategy can have unforeseen consequences, such as a higher sample complexity for learning the optimal policy. 

These results can also be interpreted in light of Liu and Brunskill’s (2018) work, which characterizes the properties of an environment that make exploration hard or easy. Informally, Liu and Brunskill show that, if, asymptotically, a random walk can explore well, then it is possible to obtain a polynomial sample complexity bound for finite sample exploration. We conjecture eigenoptions transform the problem to one where random walks are more effective, making the problem more amenable to _ϵ_ -greedy exploration. Covering options, on 

20 

Temporal Abstraction in RL with the Successor Representation 

- Table 1: The different dimensions of variation between eigenoptions and covering options. Covering options with a broad initiation set are defined such that the terminal state of these options is the same as in covering options, but the initiation set, instead of being a single state, is now every state that is not terminal. Conversely, point-based eigenoptions are eigenoptions that have a single start state, defined to be the state with smallest value in the corresponding eigenvector. 

|**Algorithm description**|**Single**<br>**iteration**|**Options broadly**<br>**available (init. set)**|
|---|---|---|
|Covering options (CO)|||
|CO w/ Broad Initiation Set|||
|Point-based Eigenoptions|||
|Eigenoptions|||



the other hand, fail to make random walks more effective. This is due to the fact that each option is available in a single state, and, when the agent happens to be in that state, it still needs to sample the option instead of primitive actions. Recent extensions of covering options to problems that require function approximation define the initiation set as a region of the state space instead of a single state (Jinnai et al., 2020). 

## **6.3 The Impact of Different Initiation Sets and Uses of the Eigenspectrum** 

In this section, we quantify the impact different choices have when designing option discovery algorithms for temporally-extended exploration. We answer the following questions: 

- Is it better to have options that are broadly available, i.e., with large initiation sets? 

- Is it beneficial to use more than one eigenvector of the SR when discovering options? 

We ask these questions because eigenoptions and covering options are based on the same principles but, as previously discussed, their effectiveness is not the same. These questions are motivated by how these methods differ. 

We use a factorial design to evaluate the impact of these different choices, which are outlined in Table 1. 

We use the diffusion time induced by the discovered options as evaluation metric. As aforementioned, the diffusion time is task-agnostic and it concisely describes the effectiveness of different sets of options across multiple potential tasks by assessing how options capture relevant properties of the environment. We compare, given the same number of options, how the diffusion time induced by different methods varies. 

Figure 10 depicts the performance of the algorithms described in Table 1. These results show that a broad initiation set eventually leads to a smaller diffusion time but, until a minimum number of options is available, they hinder performance. Eigenoptions, for example, obtain the smallest diffusion time but requires more options before doing so – the 

21 

Machado, Barreto, and Precup 

**==> picture [433 x 137] intentionally omitted <==**

**----- Start of picture text -----**<br>
3  2  1 4<br>1. Eigenoptions<br>2. Covering Options<br>3. Point-based<br>      Eigenoptions<br>5 5 4. Covering Options<br>Broad Init. Set<br>5. Primitive Actions<br>2<br>4 1 3<br>**----- End of picture text -----**<br>


Figure 10: Average (left) and median (right) diffusion time in the four-room domain induced by the options generated with the algorithms in Table 1. The inset plots depict, in log-scale, the range the diffusion time lies. See text for details. 

same applies, in a smaller scale, to using covering options with a broad initiation set. There is a bigger difference in the median diffusion time, as point-based options always reduce the median diffusion time while broad initiation sets can create attractor states that are difficult to escape from. Additionally, another trade-off to be considered is that, depending on how the options are used, a sparse initiation reduces the likelihood agents will have access to the corresponding options. 

In the setting we analyzed here, additional eigenvectors provide benefits when compared to using only the top eigenvector of the SR, even when we discard the cost of collecting more samples at each iteration. Notice that, because we use the closed-form solution, it is as if the agent had covered the whole state-space before starting the option discovery process. However, it is likely these results also generalize to settings in which the agent does not cover the whole state space. Bar et al. (2020), for example, also present results showing the benefits of using the full spectrum of the graph Laplacian for option discovery. 

It is also interesting to mention that when we compare eigenoptions and covering options, one can raise the question of whether multiple iterations of the ROD cycle improve an agent’s ability to explore. We do not explicitly perform experiments to answer this question because it would be challenging to evaluate the impact of using multiple iterations of eigenoptions, or of using covering options using more than one eigenvector per iteration in a fair way, since they lead to a larger number of options, which is what we hold fixed in our comparisons. Regardless, there is ample evidence (e.g., Jinnai et al., 2020; Machado and Bowling, 2016) of the benefits of instantiating multiple iterations of the option discovery cycle. 

We can also analyze other successes of temporally extended-exploration in light of the insights we obtained here. Dabney et al. (2020) recently introduced _ϵz_ -greedy, an extended form of _ϵ_ -greedy exploration in which an agent, when taking an exploratory action, repeats the sampled action for a random duration, often sampled from a zeta distribution. Such an approach achieves remarkable success in standard benchmarks such as Atari 2600 games. Despite not being based on time-based representations, such an approach gives us evidence to support our conclusions. In _ϵz_ -greedy exploration, the agent is allowed to sample an ex- 

22 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [359 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
1400 10 [7] 1400 100 episodes<br>500 episodes<br>1100 10 [4] 1100 1000 episodes<br>Closed-form<br>Primitive Actions<br>800 0 10 20 30 800<br>500 500<br>200 200<br>0 10 20 30 0 10 20 30<br>Number of Options Number of Options<br>Diffusion Time Diffusion Time<br>**----- End of picture text -----**<br>


Figure 11: Average (left) and median (right) diffusion time, in the four-room domain, induced by eigenoptions computed with the SR, online and in closed-form. Episodes were 1000 steps long. We report, averaged across 50 different runs, the impact of using different number of episodes for computing the SR online. The inset plot on the left figure depicts, in log-scale, the range the diffusion time lies. 

tended sequence of actions at any time, corroborating the intuition that restrictive initiation sets might prevent the agent from exploring the environment. Moreover, the duration in which the sampled action will be repeated is random, showing the benefits of varying timescales, one of the features we get from using additional eigenvectors of the SR (c.f. Figure 6). Similarly, the temporally-extended exploration used when learning to control superpressure balloons in the stratosphere (Bellemare et al., 2020) is also based on options that are not constrained to a small region of the state space and they too have varying duration. 

## **6.4 Online Option Discovery** 

The results so far were obtained in closed-form, which can only be achieved after the agent has thoroughly explored the environment. This allowed us to evaluate algorithmic ideas in a conceptually simpler way, without approximation errors. However, this is not a realistic setting. In this section, we evaluate the impact of using options discovered from online estimates of the SR, instead of assuming access to an adjacency matrix representing the environment. We use TD learning to estimate the SR from samples, what allows us to compute options before the environment has been exhaustively explored. 

Eigenoptions are robust to using online estimates of the SR, as one can see in Figure 11. This result is similar to Machado et al.’s (2018). To minimize the number of interactions with the environment, we re-use the data used to compute the SR to learn the eigenoptions’ policies. We use Q-learning to learn these policies. The agent always starts at the bottom left corner. Episodes were 1000 steps long and we used a step-size of 0 _._ 1 and _γ_ = 0 _._ 9 to learn the SR. 

Surprisingly, covering options are not as effective in the setting in which the representation is learned online. This is depicted in Figure 12. While the results for the median 

23 

Machado, Barreto, and Precup 

**==> picture [359 x 127] intentionally omitted <==**

**----- Start of picture text -----**<br>
1400<br>10 [7] 1400 100 episodes<br>500 episodes<br>1100 10 [4] 1100 1000 episodes<br>Closed-form<br>Primitive Actions<br>800 0 10 20 30 800<br>500 500<br>200 200<br>0 10 20 30 0 10 20 30<br>Number of Options Number of Options<br>Diffusion Time<br>Diffusion Time (x10)<br>**----- End of picture text -----**<br>


Figure 12: Average (left) and median (right) diffusion time, in the four-room domain, induced by covering options computed with the SR, online and in closed-form. Episodes were 1000 steps long. We report, averaged across 50 different runs, the impact of using different number of episodes for computing the SR online. The inset plot on the left figure depicts, in log-scale, the range the diffusion time lies. The y-axis in the left plot is scaled by 10 to be able to depict the average diffusion time induced by the covering options discovered online. 

diffusion time are consistent with the other results in this section, the results for the average diffusion time are not. Covering options are not able to reduce the average diffusion time in the environment; in fact, they increase it substantially. The reason becomes clearer when we look at the first options discovered. When estimating the SR online,[6] the agent rarely samples an option because it is available in a single state. This leads to similar options being discovered in multiple iterations. Moreover, covering options are less robust because they rely only on the maximum and minimum values of the top eigenvector of the SR to define the state in which an option is available. Using a single eigenvector adds to this brittleness because the agent cannot rely on other eigenvectors to capture different dimensions of the state space, or to correct for an option that captures the wrong timescale at which the agent should act. As an example, the top two eigenvectors of the SR capture the two diagonals of the four-rooms domain (c.f. Figure 7). If an agent tries to use the top eigenvector of the SR to capture, in two different iterations, these two diagonals, it may fail to do so if the random walk of the agent in the second iteration does not sample the option that navigates the dimension the first iteration captured. The mismatch between the closed-form as online solutions only increases in later iterations – Appendix C presents visualizations of eigenoptions and covering options learned online. 

Finally, using the SR to compute covering options violates the symmetry assumption of Theorem 1. After the first iteration of covering options, in some states the agent has access to four primitive actions and one option, while in others only four actions are available. In 

> 6. When the agent selects an option, we ignore individual transitions when estimating the SR, assuming the the agent “teleports” to the state in which the option terminates. This mimics the closed-form solution, which sees an option as creating an edge between two vertices. Moreover, we observed that estimating the SR from individual transitions leads to much worse results. 

24 

Temporal Abstraction in RL with the Successor Representation 

practice, at least in the four-room domain, this mismatch does not meaningfully impact the diffusion time induced by covering options discovered from the SR and those discovered from the graph Laplacian. We provide an empirical evaluation of this mismatch in Appendix D. 

## **6.5 Summary** 

In this section, we showed that eigenoptions and covering options reduce the diffusion time in a given environment, meaning that they capture properties of the environment that are useful when subsequent tasks are posed to the agent. Eigenoptions do so both when computed in closed-form and online, while covering options only do so when discovered closed-form, the setting they were originally introduced. We also investigated the impact of the different choices these approaches make. Specifically, whether it is beneficial to discover more than one option per iteration, with our results showing that discovering multiple options leads to a lower diffusion time, more robust solutions, and a more judicious sample use. Moreover, we evaluated different approaches for defining options’ initiation sets and termination conditions. Our results highlight an interesting trade-off: while making options available in fewer states avoids the creation of sink states that increase the diffusion time, these options end up not being so useful to the agent when learning to maximize rewards. They can also be quite detrimental in the online setting. While our analysis was focused on the four-room domain, our findings are intuitive and likely to generalize to other environments. 

## **7. Combining Options with the Option Keyboard** 

In the previous sections we discussed the ROD cycle, a general framework for option discovery based on representation learning (c.f. Figure 1). We also described two instantiations of the ROD cycle that build on the SR, one based on eigenoptions and one based on covering options. In both cases, options are derived from the eigenvectors of the SR matrix. 

Options derived from the eigenvectors of the SR are particularly suitable for exploration because they induce complementary distributions that collectively cover the state space in a structured way. At first this suggests a straightforward strategy for exploration: compute one option per eigenvector and then use them together to explore the environment. The problem with this strategy is that, since each option must be _learned_ , there is an inherent cost associated with adding them to the library of available behaviors. Moreover, adding the options associated with _all_ the eigenvectors may be unnecessary, since some of them provide little benefit in terms of exploration in the presence of others. To illustrate this point, note that, even in a simple domain like four-room, this exploration scheme would result in more than 100 options. Our experiments clearly demonstrate that using this many options is not really necessary (c.f. Figures 10, 11, and 12). 

This leads us to the second nice property of options induced by the eigenvectors of the SR: their associated eigenvalues provide a natural ordering of the options according to their time scale—this roughly corresponds to the option’s expected time before termination, as shown in Figure 6. Based on this observation, we can improve the exploration strategy outlined above: instead of adding the options all at once, we rank them based on their eigenvalues 

25 

Machado, Barreto, and Precup 

and add them one by one until they collectively form a good basis for exploration. This is the basic recipe underlying both eigenoptions and covering options. But can we do better? 

It has been argued that the ability to _combine_ options may be key to extend the range of available behaviors without incurring the otherwise inevitable cost in terms of sample transitions (Sutton, 2016; Heess et al., 2016; Haarnoja et al., 2018). By exploiting compositionality, one can potentially grow a finite number of options into a combinatorially larger counterpart without additional learning. In the context of eigenoptions and covering options, this benefit manifests itself in two complementary ways. First, by combining higher-order options, it may be possible to approximately emulate their lower-order counterparts, which will thus no longer need to be learned. Second, and perhaps more important, depending on how options are combined they may give rise to new options whose behavior differ significantly from that of _any_ option induced by the eigenvectors of the SR—i.e., the combined options might effectively extend the SR behavioral basis used for exploration. 

The question then arises as to how to actually implement the combination of options. In this context, a natural choice is the _option keyboard_ (Barreto et al., 2019). The option keyboard is particularly suitable to be used with options induced by the SR because it is itself based on the concept of SR, making the integration between the two approaches natural and transparent. Given a set of options evaluated under different rewards, the option keyboard provides a way to instantaneously generate options induced by any linear combination of the rewards, without any learning involved. Although simple, this way of combining options provides all the benefits mentioned above in the context of options induced by the eigenvectors of the SR. In the next section we elaborate on how to build and use the option keyboard using options derived from the SR. 

## **7.1 Generalized Policy Evaluation and Generalized Policy Improvement** 

The option keyboard is based on generalizations of the concepts of policy evaluation and policy improvement introduced in Section 2. Simply put, _generalized policy evaluation_ (GPE) is the computation of a policy’s value function under different reward functions. Given the value function of a set of policies under a specific reward function, _generalized policy improvement_ (GPI) is the computation of a new policy whose performance is no worse, and generally better, than that of the original policies. GPE and GPI are strict generalizations of their standard counterparts, which are recovered as special cases (Barreto et al., 2020). 

To accommodate the generalization provided by GPE, we will use _vπ[r]_[and] _[q] π[r]_[to][denote] the state-value and action-value functions of policy _π_ under reward _r_ . We start by noting that the SR provides a particularly efficient form of GPE: as shown in Eq. 10, once we have the SR of a policy _π_ , Ψ _π_ , we can evaluate it under _any_ reward function **r** by simply making **v** _π_ **[r]**[= Ψ] _[π]_ **[r]**[.][As discussed in Section 4, SFs generalize the SR by replacing its features] _**φ** i_ ( _sj_ ) = 1 _{i_ = _j}_ with arbitrary features _**φ**_ : S _×_ A _�→_ R _[d]_ . Once we have the SFs of a policy _π_ , _**ψ** π_ , we can compute its value function under any linear combination of the features, _r_ ( _s, a_ ) = _**φ**_ ( _s, a_ ) _[⊤]_ _**w**_ , by making _qπ[r]_[(] _[s, a]_[) =] _**[ ψ]**[π]_[(] _[s, a]_[)] _[⊤]_ _**[w]**_[,][where] _**[w]**[∈]_[R] _[d]_[(see][Eq.][13][and][14).] Note that, because the features _**φ**_ ( _s, a_ ) can be any function, one can in principle use an intrinsic reward _ri_ ( _s, a_ ) as the _i_ -th feature: _φi_ ( _s, a_ ) = _ri_ ( _s, a_ ). This will be important for the option keyboard. 

26 

Temporal Abstraction in RL with the Successor Representation 

GPI is the computation of a policy whose performance under a given reward is generally better than that of its precursors. The mechanics of GPI are actually very similar to that of its standard counterpart shown in Eq. 4: given policies _π_ 1, _π_ 2, ..., _πn_ , and their value functions under reward _r_ , _qπ[r]_ 1[,] _[q] π[r]_ 2[,][...,] _[q] π[r] n_[,][the][GPI][policy] _[π][′]_[is][given][by] 

**==> picture [318 x 17] intentionally omitted <==**

Barreto et al. (2017) have shown that, starting from the execution of any action _a ∈A_ on any state _s ∈S_ , the GPI policy _π[′]_ will do at least as well as, and generally better than, any of its precursors _πi_ . More formally, we have that _qπ[r][′]_[(] _[s, a]_[)] _[ ≥][q] π[r] i_[(] _[s, a]_[)][for][all] _[i][ ∈{]_[1] _[,]_[ 2] _[, ..., n][}]_ and all ( _s, a_ ) _∈_ S _×_ A. This result can also be extended to the case in which GPI is applied with approximations _q_ ˜ _π[r] i[≈][q] π[r] i_[(Barreto][et][al.,][2017).] 

## **7.2 Synthesizing Options with GPE and GPI** 

Now that we have introduced the concepts of GPE and GPI, we describe how to use these operations to create options without any learning involved. For clarity, instead of presenting the option keyboard in its most general form, we will use the formalism of eigenoptions introduced in Section 5 (the adaptation to covering options is straightforward). 

Let **e** 1, **e** 2, ..., **e** _d_ be eigenvectors of the SR, Ψ _π_ , induced by a policy _π_ . As per Eq. 16, each **e** _i_ gives rise to a reward function _r_ **[e]** _[i]_ ( _s, s[′]_ ) = **e** _[⊤] i_ � _**φ**_ ( _s[′]_ ) _−_ _**φ**_ ( _s_ )�, which in turn gives rise to an eigenoption _ω_ **[e]** _[i]_ . As shown in Eq. 17, the eigenoption _ω_ **[e]** _[i]_ can be compactly represented as a policy over an extended action space _π_ **[e]** _[i]_[+] . For ease of exposition, we will use _π_ **[e]** _[i]_[+] to refer to _ω_ **[e]** _[i]_ in this section. Suppose we have the value function of all the eigenoptions _π_ **[e]** _[i]_[+] under all the rewards _r_ **[e]** _[j]_ , that is, we have _qπ[r]_ **[e][e]** _[j][i]_[+][for] _[ i, j][∈{]_[1] _[,]_[ 2] _[, ..., d][}]_[.][We] will now show how to instantaneously generate options associated with linear combinations of the eigenvectors **e** _i_ without any learning involved. 

Let _**w** ∈_ R _[d]_ and let 

**==> picture [248 x 24] intentionally omitted <==**

We want to compute an approximation of the option induced by the reward _r_ **[c]** ( _s, s[′]_ ) = **c** _[⊤]_[�] _**φ**_ ( _s[′]_ ) _−_ _**φ**_ ( _s_ )� without resorting to learning. First, we note that 

**==> picture [248 x 25] intentionally omitted <==**

Connecting the above with Eq. 13, we see that here we are using the intrinsic rewards _r_ **[e]** _[i]_ as features. This view allows us to resort to Eq. 14 to compute the value function of the eigenoptions _π_ **[e]** _[i]_[+] under the reward _r_ **[c]** as 

**==> picture [289 x 27] intentionally omitted <==**

Once we have _qπ[r]_ **[c][e]** _[i]_[+][for][all] _[i][ ∈{]_[1] _[,]_[ 2] _[, ..., d][}]_[,][we][can][use][GPI][defined][in][Eq.][18][to][compute] 

**==> picture [344 x 18] intentionally omitted <==**

27 

Machado, Barreto, and Precup 

Note that, since _π_ ˜ **[c]**[+] is defined over an extended action space which also includes the terminate action _⊥_ , it gives rise to a well-defined option, including the initiation and termination sets (see discussion in Section 5). 

The option computed in Eq. 21 is an approximation of the option _π_ **[c]**[+] induced by **c** , that is, _π_ ˜ **[c]**[+] _≈ π_ **[c]**[+] . The advantage of using _π_ ˜ **[c]**[+] is that, unlike _π_ **[c]**[+] , it can be obtained without any learning involved. Based on the results regarding GPI, we know that _π_ ˜ **[c]**[+] will perform at least as well as, and generally better than, any of the options _π_ **[e]** _[i]_[+] under the reward _r_ **[c]** . This means that the larger the number of options _π_ **[e]** _[i]_[+] used in Eq. 21 the closer ˜ _π_ **[c]**[+] will be to _π_ **[c]**[+] . In any case, it is worth noting that, since we are using options mostly to generate diverse behavior, an eventual sub-optimal performance of _π_ ˜ **[c]**[+] should not have a catastrophic effect. 

**Putting it all together** We now summarize how the procedure above can be combined with eigenoptions to considerably enlarge the number of options used for exploration. Given a set of eigenvectors **e** 1, **e** 2, ..., **e** _d_ , the first thing we do is to compute the induced eigenoptions _ω_ **[e]**[1] _, ω_ **[e]**[2] _, ..., ω_ **[e]** _[d]_ , which here we represent as policies defined over an augmented action space: _π_ **[e]**[1][+] _, π_ **[e]**[2][+] _, ..., π_ **[e]** _[d]_[+] . Then, we evaluate each _π_ **[e]** _[i]_[+] under the reward functions induced by the eigenvectors, that is, we compute _qπ[r]_ **[e][e]** _[j][i]_[+][for] _[i, j][∈{]_[1] _[,]_[ 2] _[, ..., d][}]_[(obviously,][we] can compute _qπ[r]_ **[e][e]** _[j][i]_[+] _[while]_[we learn the options] _[ π]_ **[e]** _[i]_[+][— see, for example, Barreto et al.’s (2019)] Algorithm 3). Once we have the value functions _qπ[r]_ **[e][e]** _[j][i]_[+][,][the][successive][application][of][Eq.][19,] 20 and 21 with _any_ _**w** ∈_ R _[d]_ results in an option _π_ ˜ **[c]**[+] that approximates the option _π_ **[c]**[+] induced by **c** =[�] _i[w][i]_ **[e]** _[i]_[.] 

We can think of the process above as implementing a mapping from _**w** ∈_ R _[d]_ to an approximation of the corresponding option _π_ **[c]**[+] , where _**c**_ =[�] _i[w][i]_ **[e]** _[i]_[.][This][means][that][we] immediately have at our disposal a potentially very large set of options induced by all possible instantiations of the vector _**w**_ . If _**w**_ happens to only have one non-zero element that is positive, we recover one of the eigenoptions _π_ **[e]** _[i]_[+] induced by the eigevectors **e** _i_ . For other instantiations of _**w**_ we have options whose behavior can significantly deviate from that of the original eigenoptions (Barreto et al., 2019). In the next section we use experiments to illustrate the benefits of combining the option keyboard with eigenoptions. 

## **8. Combining Eigenoptions with the Option Keyboard** 

In this section, we demonstrate the synergy between eigenoptions and the option keyboard. As mentioned above, the option keyboard allows one to extend a finite set of options to a combinatorially large counterpart without additional learning. Nevertheless, the option keyboard assumes an initial set of basis options is available beforehand, with existing results in the literature relying on handcrafted options as basis options. When considering discovered options, eigenoptions are natural candidates as basis options. They are autonomously discovered from the SR, the same object that makes the option keyboard computationally efficient, and they are generated by orthogonal vectors obtained from the agent’s behavior. Intuitively, using the option keyboard to combine eigenoptions is the equivalent of computing linear combinations of orthogonal bases of behaviors. 

28 

Temporal Abstraction in RL with the Successor Representation 

1 _st_ eigenoption 2 _nd_ eigenoption 3 _rd_ eigenoption _4th_ eigenoption _10th_ eigenoption 

Figure 13: Eigenoptions discovered in the open-room. As in previous results, their ordering is defined by the eigenvalues corresponding to the eigenvectors that gave rise to each option. Both directions of the eigenvectors are taken into consideration. 

We first present a qualitative analysis of the options generated by combining eigenoptions with the option keyboard. We present multiple eigenoptions and the options the option keyboard generates from them. We discuss the number of unique combinations and how diverse the generated options are. We then present a quantitative analysis focused on the diffusion time induced by these new options generated by the option keyboard. We conclude this section with a higher-level discussion about the benefits of combining eigenoptions with the option keyboard, and potential avenues for future work. 

## **8.1 Options Combined through the Option Keyboard are Diverse** 

We define the set of basis options to be the first ten eigenoptions and we linearly combine these options with the option keyboard. Because there are infinite possible weight combinations, we constrain ourselves to _{_ 0 _,_ 1 _}_ combinations at first, meaning weights can be either 0 or 1. We perform our experiments in the four-room domain and in an open 10 _×_ 10 gridworld, which we name open-room (see Figure 13). The latter is particularly useful for this set of experiments because it allows us to build intuitions about the algebra of the options without being distracted by walls and asymmetries. For reference, some of the eigenoptions used as basis options are depicted in Figures 13 and 25, the latter in Appendix C. 

In the open-room, when combining the first four eigenoptions in sets of two, the agent recovers cardinal directions, as shown in Figure 14. This is an interesting result because it shows a general method naturally discovering important abstractions. Besides that, we also observe the union of different options (e.g., going to the closest corner) and, once an eigenoption that takes the agent to the center of the room is available, the option keyboard generates combinations that together terminate in most states in the environment. In the four-room domain, we can draw similar conclusions, despite the walls preventing behaviors as interpretable as those in the open-room. We see options that take the agent to specific walls/directions, to specific rooms, and to bottleneck states, as shown in Figure 15. 

The option keyboard also leads to a combinatorial explosion of new options, even when we only consider _{_ 0 _,_ 1 _}_ combinations. This is shown in Figure 16, which reports the number of _unique_ options generated by the option keyboard. The number of new options is not 2 _[n]_ , where _n_ is the number of basis options, because two options can be added together to 

29 

Machado, Barreto, and Precup 

**==> picture [433 x 189] intentionally omitted <==**

**----- Start of picture text -----**<br>
[1,0,0,1,0,0,0,0,0,0]  [1,0,1,0,0,0,0,0,0,0]  [0,1,0,1,0,0,0,0,0,0]  [0,1,1,0,0,0,0,0,0,0]  [0,0,0,0,0,0,1,0,0,1]<br>[1,1,0,0,0,0,0,0,1,0]  [1,1,0,0,0,0,0,1,0,0]  [0,0,0,0,0,1,1,0,0,0]  [0,0,1,0,0,1,0,0,0,1]  [1,0,0,1,0,1,0,0,0,1]<br>**----- End of picture text -----**<br>


Figure 14: Options obtained by combining eigenoptions with the option keyboard. The weights used to generate them are above the option, where the _i_ -th entry corresponds to the weight given to the _i_ -th eigenoption. 

**==> picture [433 x 187] intentionally omitted <==**

Figure 15: Options obtained by combining eigenoptions with the option keyboard. The weights used to generate them are above the option, where the _i_ -th entry corresponds to the weight given to the _i_ -th eigenoption. 

cancel each other, for example, when they are derived from both directions of the same eigenvector. Additionally, different combinations can lead to the same option. 

So far we have shown that combining eigenoptions with the option keyboard leads to interesting, semantically meaningful, options, as well as a large number of options. We conclude this section showing these options are diverse. We do so by looking at the frequency 

30 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [413 x 127] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 × 10 Gridworld Four-room Domain<br>150 150<br>137<br>115<br>100 100<br>72<br>62<br>55<br>50 50<br>33 34<br>1 2 5 8 9 10 1 2 5 7 8 11 21<br>0 0<br>0 5 10 0 5 10<br>Number of Basis Options Number of Basis Options<br>Number of New Options Number of New Options<br>**----- End of picture text -----**<br>


Figure 16: Number of unique options generated by combining eigenoptions. We consider two options to be the same if they have the same set of terminal states. In the open-room, for example, the 1 _st_ eigenoption leads to a single option: itself. Adding a 2 _nd_ eigenoption only leads to an extra option because the 1 _st_ and 2 _nd_ eigenoptions stem from the same eigenvector, thus they cancel each other when combined. Adding a 3 _rd_ eigenoption leads to two extra options (combination of the 1 _st_ and 3 _rd_ , as well as the 2 _nd_ and 3 _rd_ ), totalling 5 options (instead of 3). This difference becomes starker as more basis options become available. 

at which these options terminate in different states. Figures 17 and 18 depict heatmaps contrasting the set of terminal states induced by eigenoptions and those induced by the combinations of those eigenoptions. The numbers in each tile report the number of times, across the considered options, that the corresponding state is a terminal state. Colors represent the relative frequency of termination across all states. 

It is reassuring to see that the few basis options depicted on the left of Figures 17 and 18 can be combined to generate the diverse behaviors depicted on the right. In these environments, even when considering only _{_ 0 _,_ 1 _}_ combinations, ten options are enough for the option keyboard to generate options that visit most states in the environment. Eigenoptions are orthogonal _bases of behavior_ that span most of the behaviors one would be interested in. In the open-room, for example, eigenoptions terminating in 16 states end up being combined to terminate in 96 states. In the next section we show this diversity in fact allows the agent to better explore the environment. 

## **8.2 Options Combined through the Option Keyboard Improve Exploration** 

In this section, we show that the diversity introduced by the option keyboard in fact impacts an agent’s ability to explore the environment. Figures 19 and 20 depict the diffusion time induced by the first ten eigenoptions and by the options generated by the option keyboard when using the same eigenoptions as basis options. We term _OK-Eigenoptions [0, 1]_ the set of options generated by _{_ 0 _,_ 1 _}_ combinations of eigenoptions, and _OK-Eigenoptions [-1, 0, 1]_ the set of options generated by _{−_ 1 _,_ 0 _,_ 1 _}_ combinations, which we discuss later. 

We compare the diffusion time induced by these different option sets based on the number of basis options (i.e., eigenoptions) in them. This might seem unfair at first, as 

31 

Machado, Barreto, and Precup 

**==> picture [282 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
Eigenoptions Options from eigenoptions<br>combined with the OK<br>**----- End of picture text -----**<br>


Figure 17: Open-room domain: freq. options terminate in each state. See text for details. 

**==> picture [282 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
Eigenoptions Options from eigenoptions<br>combined with the OK<br>**----- End of picture text -----**<br>


Figure 18: Four-room domain: freq. options terminate in each state. See text for details. 

more options are used by OK-Eigenoptions, but this is exactly one of the benefits of the option keyboard: with an almost negligible computational cost, and no additional agentenvironment interactions, a large combinatorial counterpart of the original options becomes available to the agent. 

Shortly, using the option keyboard to augment an agent’s option set can drastically reduce the number of eigenoptions the agent needs to effectively explore the environment. In the open-room and four-room domains, the agent needs 10 and 12 eigenoptions to make the induced exploration more effective than that obtained by a uniform random policy. When augmenting the agent with the options generated by the option keyboard, this number is reduced by 30% and 42%, respectively. Also, the median diffusion time is not affected when adding the options generated by the option keyboard, suggesting that these additional options improve exploration by making eigenoptions much more robust. 

Finally, it is important to stress that we obtained these results using only _{_ 0 _,_ 1 _}_ weights. A trivial improvement to what we have done so far is to generate only one (instead of two) eigenoption from each eigenvector of the SR. The option corresponding to the opposite direction of each eigenvector can be obtained with the option keyboard by assigning a _−_ 1 weight to the corresponding eigenoption. This immediately reduces the number of options to be learned by half! We use the green line in Figures 19 and 20 to make this point obvious. Shortly, by leveraging the option keyboard in the simplest possible way we are able to show, in both environments, that 4 eigenoptions are enough to improve exploration beyond what 

32 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [432 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>1. Eigenoptions<br>2. OK- Eigenoptions [0,1]<br>3 2<br>3. OK-Eigenoptions [-1,0,1]<br>3 2<br>1 4. Primitive Actions<br>1<br>4<br>**----- End of picture text -----**<br>


Figure 19: Average and median diffusion time in the open-room domain. Each curve depicts a function of the number of primitive options the agent has access to, but the actual number of options used may vary, as described in the text. The performance of primitive actions is not depicted in the plot on the right because it is out of the reported range. The scale on the left is 100 times bigger than in the other plots due to the big impact individual options have at first. 

**==> picture [432 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>3 2<br>1. Eigenoptions<br>2. OK- Eigenoptions [0,1]<br>3. OK-Eigenoptions [-1,0,1]<br>4. Primitive Actions<br>2<br>1<br>3<br>1<br>**----- End of picture text -----**<br>


Figure 20: Average and median diffusion time in the four-room domain. Each curve depicts a function of the number of primitive options the agent has access to, but the actual number of options used may vary, as described in the text. The performance of primitive actions is not depicted in the plot on the right because it is out of the reported range. The scale on the left is 100 times bigger than in the other plots due to the big impact individual options have at first. 

the uniform random policy does. This is an important result because, for the first time, we are able to obtain results that match the intuition that four options should suffice in these environments. It was not clear how to discover (and combine) such options until now. 

## **8.3 A Big Picture View of Combining Eigenoptions with the Option Keyboard** 

The combination of eigenoptions and the option keyboard allow these approaches to heavily benefit from each other. Eigenoptions, by construction, provide a diverse set of behaviors to 

33 

Machado, Barreto, and Precup 

the agent, but dozens of options are necessary for better exploration. The option keyboard, on the other hand, combines different options to generate a large set of new behaviors, but only once basis options are provided. The combination of the eigenoptions and the option keyboard leads to more diverse behavior that improves exploration while drastically reducing the number of options that need to be discovered. The option keyboard is also able to drastically reduce the computational cost of learning eigenoptions. 

Our experiments demonstrated the potential of combining an option discovery method based on the SR with the option keyboard. There are multiple directions one could pursue in a future work. An interesting direction is how to define the weights used by the option keyboard. While we used _{−_ 1 _,_ 0 _,_ 1 _}_ weights, different weights are likely to be more expressive, generating even more diverse behaviors. From a theoretical perspective, it would be interesting to characterize the number of basis options needed by an agent in order to, for example, ensure that there is at least one combined option that terminates in each state. This number could also be used as a measure of task complexity (or similarity). 

From an algorithmic perspective, it would be valuable to understand the impact of using the option keyboard to combine options estimated online. It would also be useful to see these ideas evaluated in the function approximation case. An immediate challenge in this case would be to identify equivalent options, something trivially done in the tabular case. Scaling these ideas to more challenging domains might also require non-linear function approximation and representation learning, problems tackled by deep reinforcement learning. As previously mentioned, for clarity purposes, we decided to not discuss these ideas in this paper, but there are several advances and successes of this line of work in the deep reinforcement learning case. We discuss some of the main ideas in the next section. 

## **9. Related Work** 

So far, we discussed the role of the SR for temporal abstraction in reinforcement learning, focusing on options for temporally-extended exploration. Additionally, we explored how the SR can be used to seamlessly combine different options without additional learning. It is unfeasible to thoroughly discuss the diverse set of methods for option discovery that do not aim at exploration. Instead, here we outline only the main ideas behind these other approaches. Moreover, we discuss existing extensions of the ideas we presented to the function approximation setting, and we conclude drawing connections between the topics we discussed and recent results in neuroscience. 

## **9.1 Additional Option Discovery Methods based on the SR** 

Planning and faster credit assignment are common use cases for options. These ideas are often associated with bottleneck options, that is, options that lead to states that connect different closely connected regions of the environment. The SR has also been used by option discovery methods in this setting. Stachenfeld et al. (2014, 2017), for example, explicitly searched bottleneck states by using the eigenvectors of the SR to obtain an approximate solution to the _k_ -way normalized min-cut problem. In this case, the eigenvectors of the SR are used in a different way from what we described so far, with positive and negative elements of an eigenvector approximating different partitions, a known result from spectral graph 

34 

Temporal Abstraction in RL with the Successor Representation 

theory (Shi and Malik, 2000). Kulkarni et al. (2016), in the context of deep reinforcement learning, also discovered bottleneck options through normalized cuts. Another relevant idea in this context is the algorithm named _successor options_ (Ramesh et al., 2019). This method clusters the SR vectors and defines the clusters centroids as the options’ terminal states. In this case, even though the method is not explicitly designed to seek for bottleneck states, the empirical evidence provided shows that successor options tend to find bottleneck states much more often than eigenoptions (see Figure 5 by Ramesh et al., 2019). 

In the context of bottleneck options and the framework presented in Section 3, Continual Curiosity-driven Skill Acquisition (CCSA; Kompella et al., 2017) is also relevant to our discussion. CCSA also discovers options that maximize an intrinsic reward obtained from a learned representation, which in this case is obtained from Slow Feature Analysis (SFA; Wiskott and Sejnowski, 2002). Importantly, Sprekeler (2011) has shown that, given a specific choice of adjacency function, proto-value functions are equivalent to SFA. SFA becomes an approximation of proto-value functions if the function space used in the SFA does not allow arbitrary mappings from the observed data to an embedding. Recall that one can see proto-value functions as a special case of the eigenvectors of the SR (Machado et al., 2018), making SFA, by transitivity, connected to the ideas discussed in this paper. 

In the context of options for temporally-extended exploration, Bar et al. (2020) recently introduced _diffusion options_ , which were inspired by the ideas discussed here. Instead of looking at individual eigenvectors, this approach sets out to use the full eigenspectrum of the adjacency matrix. Specifically, it uses the eigenvalues as weights to linearly combine the right and left eigenvectors of the non-symmetric lazy random walk matrix, a variation of the graph Laplacian matrix we discussed in Section 2. Despite the intuitive similarity between the eigenvectors of the non-symmetric lazy random walk matrix and the eigenvectors of the SR, there is still not a formal connection between these two objects. However, it is interesting to note that Bar et al.’s empirical results corroborate what we present in this paper. Shortly, (1) these options provide temporal-extended exploration, (2) eigenoptions tend to be more effective than covering options, and (3) diffusion options also needs to use 10 _−_ 20 eigenvectors to be effective in gridworld domains, similar to our results before combining discovered options with the option keyboard. 

Finally, the eigenoption-critic (Liu et al., 2017) is also relevant to this overview. It extends eigenoptions to continuous state spaces with the Nystr¨om approximation (Mahadevan and Maggioni, 2007). It also combine eigenoptions to the option-critic architecture (Bacon et al., 2017) for a single online phase for option discovery and option learning, while also taking the reward generated by the environment into consideration. Also, it is applicable to settings in which non-linear function approximation is required, which we discuss next. 

## **9.2 Function Approximation and the SR** 

In this paper, we focused on the tabular case for conceptual clarity. Nevertheless, in several problems one cannot uniquely identify the states in the environment and function approximation is required. Scaling these ideas up has been an active topic of research, with solutions proposed to both the linear and non-linear function approximation cases. 

In the **linear function approximation** case, given a set of features _**φ**_ ( _·_ ), Machado et al. (2017) proposed to generate the options’ intrinsic reward function with the singular vectors 

35 

Machado, Barreto, and Precup 

of the matrix obtained from the difference between current and previous observations. If all transitions in the graph are sampled once, for tabular representations, this matrix recovers the same options we obtain with the combinatorial Laplacian. This is formalized below. 

**Theorem 3 (Machado et al. 2017)** _Consider the singular value decomposition of the matrix_ **T** _s.t._ **T** = **UΣV** _, with each row of_ **T** _consisting of the difference between observations, i.e.,_ _**φ**_ ( _s[′]_ ) _−_ _**φ**_ ( _s_ ) _. In the tabular case, if all transitions in the MDP have been sampled once, the orthonormal vectors of_ **L** = **D** _−_ **W** _are the columns of_ **V** _[⊤] ._ 

**Proof** See Appendix A. 

In the **non-linear function approximation** case, when neural networks are used to approximate the value function, there are many more solutions to the problem of scaling up the ideas we presented here. A direct way of doing so is by having the network also outputting successor features (e.g. Barreto et al., 2020; Borsa et al., 2019; Hansen et al., 2020; Kulkarni et al., 2016; Liu and Abbeel, 2021; Machado et al., 2018, 2020). This is often done by training the neural network to also minimize the loss 

**==> picture [342 x 34] intentionally omitted <==**

or one of its variations, where _**ψ**_ denotes successor features. Sometimes it is assumed the representation _**φ**_ ( _·_ ) is known beforehand (e.g. Borsa et al., 2019), while other times it is defined as the output of an inner layer of the neural network (e.g., Machado et al., 2018). The latter can be unstable and, because the representation is also being learned, one needs to be careful since _**φ**_ ( _·_ ) = **0** is a fixed point of this minimization problem. In this case, it is common to prevent gradients to backpropagate to the representation layer, and to introduce auxiliary tasks to shape the representation learning process (Jaderberg et al., 2017). 

Alternatively, researchers have also been using results from graph drawing theory (Koren, 2003) to design loss functions that allow the network to explicitly estimate the eigenvectors of the Laplacian (e.g., Erraqabi et al., 2021; Wang et al., 2021; Wu et al., 2019). The loss function originally proposed, with later methods introducing variations, was 

**==> picture [403 x 73] intentionally omitted <==**

where **e** 1 _, . . . ,_ **e** _d_ are the first _d_ eigenvectors, _u_ and _v_ are different states, _β_ is a penalty weight parameter, and _δjk_ is a soft constraint used to capture the orthogonality constraint between different eigenvectors. 

Intuitively, the loss function above has an attractive and a repulsive term, which is common in contrastive losses (e.g., Li et al., 2021). The first term, the attractive one, tries to ensure consecutive states are put together in the embedding, as in the SR. The repulsive term repels the embedding of states independently sampled from the stationary distribution 

36 

Temporal Abstraction in RL with the Successor Representation 

of the induced Markov chain, trying to make eigenvectors orthogonal to each other. In the first term, the state _u_ is assumed to be (uniformly) sampled from the state distribution and _v_ is defined by the environment’s dynamics. In the second, _v_ is randomly sampled. We did not depict this in the expectations to avoid cluttering the equations. Wu et al. presents a precise discussion and the accompanying derivations. This approach, based on the graph drawing objective, has also been used to scale covering options to the deep reinforcement learning case (Jinnai et al., 2020). This is what was used to generate Figure 2. 

Finally, there have also been attempts to scale up the ideas discussed here by generating abstract transition graphs, with a neural network being used to generate the state abstractions (Mendon¸ca et al., 2019). Nevertheless, only anecdotal evidence of the efficacy of such an approach has been provided, with more results being needed to validate it. 

## **9.3 The Relationship of the SR to Other Ideas in RL and Other Fields** 

As mentioned in Section 4, the SR is directly related to several other ideas in reinforcement learning. As already discussed, it is related to proto-value functions (Machado et al., 2018) and slow-feature analysis (Sprekeler, 2011), and it can be seen as encoding the LSTD matrix (Lagoudakis and Parr, 2003). Moreover, the SR can be seen, for example, as a form of dual approach to value-function based methods (Wang et al., 2007). In this formalism, which has been shown to avoid the risk of divergence, one maintains an explicit representation of visit distributions instead of value functions. For exploration, it has been shown that the norm of the SR implicitly encodes state-visitation counts (Machado et al., 2020). 

It is particularly interesting to observe that methods introduced for computational reinforcement learning are related to recent results in neuroscience and human behavior. From a neuroscience perspective, Stachenfeld et al. (2014, 2017) have suggested that the hippocampus encodes the SR. Specifically, they argue that hippocampal place fields encode a predictive representation of the current and future states under the current transition distribution. Additionally, and directly related to the option discovery methods we presented here, Stachenfeld et al. (2014, 2017) present results demonstrating that the eigenvectors of the SR resemble grid cells, also suggesting that the entorhinal cortex may use that information to aid hierarchical reinforcement learning. This result is motivated by the fact that the eigenvectors of the SR allow one to capture natural boundaries, potentially enconding metric information about the space. From a planning perspective, they show how one can use the eigenvectors of the SR to identify bottleneck states, which are convenient waypoints for likely being traversed along many optimal trajectories (see Solway et al., 2014). 

On a higher level of abstraction, the SR has also been used to explain human behavior. Momennejad et al. (2017), for example, has suggested the SR allows the brain to tradeoff computational costs and suboptimality when solving complex, dynamic decision tasks. They argue that the SR can be seen as an underlying computational procedure that ends up allowing humans to have more flexible choices, something more rigid than habits, described by model-free methods, and more more flexible than deliberative decision making, described by model-based approaches. Even more directly related to the concepts we presented, Tomov et al. (2021) also discusses the SR in the context of human decision making, suggesting it can be used, alongside GPI, as a model for human decision making in multi-task scenarios. 

37 

Machado, Barreto, and Precup 

In summary, the ideas discussed in this paper around the SR, such as using it as a representation, for efficient transfer learning, or for option discovery, seem to model well data collected from intelligent, biological animals. Although this does not necessarily mean that these ideas are the correct way of tackling the problems discussed here, these results are encouraging evidence that it might be worth investigating these ideas further. 

## **10. Conclusion** 

In this paper, we discussed the role of the successor representation (SR) when using temporal abstractions in reinforcement learning. We presented a general framework for option discovery that follows a constructivist approach and we examined two instantiations of this cycle. These instantiations use the eigenvectors of the SR to discover options for temporally-extended exploration, thoroughly evaluating them and shedding light on decisions every option discovery method should make, such as on how to define the initiation set and termination condition of each option. Moreover, we discussed how the SR can also be used to address the inevitable trade-off every agent is subject to: to discover more options in order to have access to a more expressive set of behaviours, or to restrict them to facilitate learning. This is done through the option keyboard, which extends, without additional learning, a finite set of options to a combinatorially large counterpart. The empirical evaluation of using the option keyboard to combine options discovered with the SR provides encouraging evidence of the synergy of these approaches, drastically reducing the computational cost while increasing the expressivity of the options available to the agent. 

The goal of this paper was to provide a unified perspective over different approaches for temporal abstraction in reinforcement learning, showing how they can all be cast as discovering options from the SR, and how these ideas have evolved throughout the time. Naturally, there are several extensions of these approaches in order to scale them up to problems with large state spaces. Moreover, there is increasing evidence that the SR also plays an important role, at different levels of abstraction, in human and animal decisionmaking. We believe using the SR as the main substrate for temporal abstraction is a promising research direction and we hope this paper serves as a catalyst to this line of work. In particular, we believe that a cycle such as the one described here might end up being a core component of agents that are capable to continually learn and to acquire increasingly complex skills. Intelligent agents should be constantly acquiring new data, and this data should allow the agent to refine its representation of the world, which in turn should serve to inform which temporal abstractions an agent should learn, further empowering the agent’s ability to collect new data, in a virtuous cycle of discovery. 

## **Acknowledgements** 

This work was partially developed while Marlos C. Machado was at Google Research, Brain Team. The authors would like to thank Tom Schaul and Adam White for their thorough feedback on an earlier draft; and Dale Schuurmans, Yuu Jinnai, Marc G. Bellemare, Patrick Pilarski, and Michael Bowling for useful discussions. Marlos C. Machado and Doina Precup are supported by a Canada CIFAR AI Chair. 

38 

Temporal Abstraction in RL with the Successor Representation 

## **References** 

- Pierre-Luc Bacon, Jean Harb, and Doina Precup. The option-critic architecture. In _Proceedings of the National Conference on Artificial Intelligence (AAAI)_ , 2017. 

- Amitay Bar, Ronen Talmon, and Ron Meir. Option Discovery in the Absence of Rewards with Manifold Analysis. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2020. 

- Adrien Baranes and Pierre-Yves Oudeyer. Active Learning of Inverse Models with Intrinsically Motivated Goal Exploration in Robots. _Robotics and Autonomous Systems_ , 61(1): 49–73, 2013. 

- Andr´e Barreto, Will Dabney, R´emi Munos, Jonathan Hunt, Tom Schaul, David Silver, and Hado van Hasselt. Successor Features for Transfer in Reinforcement Learning. In _Advances in Neural Information Processing Systems (NeurIPS)_ , pages 4058–4068, 2017. 

- Andr´e Barreto, Diana Borsa, John Quan, Tom Schaul, David Silver, Matteo Hessel, Daniel J. Mankowitz, Augustin Zidek, and R´emi Munos. Transfer in Deep Reinforcement Learning Using Successor Features and Generalised Policy Improvement. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 510–519, 2018. 

- Andr´e Barreto, Diana Borsa, Shaobo Hou, Gheorghe Comanici, Eser Ayg¨un, Philippe Hamel, Daniel Toyama, Jonathan Hunt, Shibl Mourad, David Silver, and Doina Precup. The Option Keyboard: Combining Skills in Reinforcement Learning. In _Advances in Neural Information Processing Systems (NeurIPS)_ , 2019. 

- Andr´e Barreto, Shaobo Hou, Diana Borsa, David Silver, and Doina Precup. Fast Reinforcement Learning with Generalized Policy Updates. _Proceedings of the National Academy of Sciences_ , 117(48):30079–30087, 2020. 

- Marc G. Bellemare, Salvatore Candido, Pablo Samuel Castro, Jun Gong, Marlos C. Machado, Subhodeep Moitra, Sameera S. Ponda, and Ziyu Wang. Autonomous Navigation of Stratospheric Balloons using Reinforcement Learning. _Nature_ , 588:77–82, 2020. 

- Richard E. Bellman. _Dynamic Programming_ . Princeton University Press, Princeton, NJ, 1957. 

- Diana Borsa, Andr´e Barreto, John Quan, Daniel J. Mankowitz, Hado van Hasselt, R´emi Munos, David Silver, and Tom Schaul. Universal Successor Features Approximators. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2019. 

- Andrei Z. Broder and Anna R. Karlin. Bounds On The Cover Time. _Journal of Theoretical Probability_ , 2(1):101–120, 1989. 

- Emma Brunskill and Lihong Li. PAC-Inspired Option Discovery in Lifelong Reinforcement Learning. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 316–324, 2014. 

39 

Machado, Barreto, and Precup 

- Maxime Chevalier-Boisvert, Lucas Willems, and Suman Pal. Minimalistic Gridworld Environment for OpenAI Gym. `https://github.com/maximecb/gym-minigrid` , 2018. 

- R. R. Coifman, S. Lafon, A. B. Lee, M. Maggioni, B. Nadler, F. Warner, and S. W. Zucker. Geometric Diffusions as a Tool for Harmonic Analysis and Structure Definition of Data: Diffusion Maps. _Proceedings of the National Academy of Sciences_ , 102(21):7426–7431, 2005. 

- Will Dabney, Georg Ostrovski, and Andr´e Barreto. Temporally-Extended _ϵ_ -Greedy Exploration. _CoRR_ , abs/2006.01782, 2020. 

- Peter Dayan. Improving Generalization for Temporal Difference Learning: The Successor Representation. _Neural Computation_ , 5(4):613–624, 1993. 

- Peter Dayan and Geoffrey E. Hinton. Feudal Reinforcement Learning. In _Proceedings of Advances in Neural Information Processing Systems (NeurIPS)_ , pages 271–278, 1992. 

- Akram Erraqabi, Mingde Zhao, Marlos C. Machado, Yoshua Bengio, Sainbayar Sukhbaatar, Ludovic Denoyer, and Alessandro Lazaric. Exploration-Driven Representation Learning in Reinforcement Learning. In _ICML Workshop on Unsupervised Reinforcement Learning_ , 2021. 

- Ronan Fruit and Alessandro Lazaric. Exploration-Exploitation in MDPs with Options. In _Proceedings of the International Conference on Artificial Intelligence and Statistics (AISTATS)_ , pages 576–584, 2017. 

- Tuomas Haarnoja, Kristian Hartikainen, Pieter Abbeel, and Sergey Levine. Latent Space Policies for Hierarchical Reinforcement Learning. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2018. 

- Steven Hansen, Will Dabney, Andr´e Barreto, David Warde-Farley, Tom Van de Wiele, and Volodymyr Mnih. Fast Task Inference with Variational Intrinsic Successor Features. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2020. 

- Nicolas Heess, Gregory Wayne, Yuval Tassa, Timothy P. Lillicrap, Martin A. Riedmiller, and David Silver. Learning and Transfer of Modulated Locomotor Controllers. _CoRR_ , abs/1610.05182, 2016. 

- Max Jaderberg, Volodymyr Mnih, Wojciech Marian Czarnecki, Tom Schaul, Joel Z. Leibo, David Silver, and Koray Kavukcuoglu. Reinforcement Learning with Unsupervised Auxiliary Tasks. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2017. 

- Yuu Jinnai, David Abel, David Ellis Hershkowitz, Michael L. Littman, and George D. Konidaris. Finding Options that Minimize Planning Time. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 3120–3129, 2019a. 

- Yuu Jinnai, Jee Won Park, David Abel, and George D. Konidaris. Discovering Options for Exploration by Minimizing Cover Time. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 3130–3139, 2019b. 

40 

Temporal Abstraction in RL with the Successor Representation 

- Yuu Jinnai, Jee Won Park, Marlos C. Machado, and George D. Konidaris. Exploration in Reinforcement Learning with Deep Covering Options. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2020. 

- Varun Raj Kompella, Marijn F. Stollenga, Matthew D. Luciw, and J¨urgen Schmidhuber. Continual Curiosity-driven Skill Acquisition from High-Dimensional Video Inputs for Humanoid Robots. _Artificial Intelligence_ , 247:313–335, 2017. 

- Risi Kondor and John D. Lafferty. Diffusion Kernels on Graphs and Other Discrete Input Spaces. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 315–322, 2002. 

- George D. Konidaris and Andrew G. Barto. Building Portable Options: Skill Transfer in Reinforcement Learning. In _Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)_ , pages 895–900, 2007. 

- George D. Konidaris and Andrew G. Barto. Skill Discovery in Continuous Reinforcement Learning Domains using Skill Chaining. In _Advances in Neural Information Processing Systems (NeurIPS)_ , pages 1015–1023, 2009. 

- Yehuda Koren. On Spectral Graph Drawing. In _Proceedings of the International Computing and Combinatorics Conference (COCOON)_ , pages 496–508, 2003. 

- Tejas D. Kulkarni, Ardavan Saeedi, Simanta Gautam, and Samuel J. Gershman. Deep Successor Reinforcement Learning. _CoRR_ , abs/ 1606.02396, 2016. 

- Michail G. Lagoudakis and Ronald Parr. Least-Squares Policy Iteration. _Journal of Machine Learning Research_ , 4:1107–1149, 2003. 

- Siyuan Li, Lulu Zheng, Jianhao Wang, and Chongjie Zhang. Learning Subgoal Representations with Slow Dynamics. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2021. 

- Hao Liu and Pieter Abbeel. APS: active pretraining with successor features. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2021. 

- Miao Liu, Marlos C. Machado, Gerald Tesauro, and Murray Campbell. The EigenoptionCritic Framework. _CoRR_ , abs/1712.04065, 2017. Presented at the NeurIPS-17 Workshop on Hierarchical Reinforcement Learning. 

- Yao Liu and Emma Brunskill. When Simple Exploration is Sample Efficient: Identifying Sufficient Conditions for Random Exploration to Yield PAC RL Algorithms. _CoRR_ , abs/1805.09045, 2018. Presented at the 14th European Workshop on Reinforcement Learning (EWRL). 

- Marlos C. Machado. _Efficient Exploration in Reinforcement Learning through Time-Based Representations_ . PhD thesis, University of Alberta, Canada, 2019. 

- Marlos C. Machado and Michael Bowling. Learning Purposeful Behaviour in the Absence of Rewards. _CoRR_ , abs/1410.4604, 2016. Presented at the ICML-16 Workshop on Abstraction in Reinforcement Learning. 

41 

Machado, Barreto, and Precup 

- Marlos C. Machado, Marc G. Bellemare, and Michael Bowling. A Laplacian Framework for Option Discovery in Reinforcement Learning. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 2295–2304, 2017. 

- Marlos C. Machado, Clemens Rosenbaum, Xiaoxiao Guo, Miao Liu, Gerald Tesauro, and Murray Campbell. Eigenoption Discovery through the Deep Successor Representation. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2018. 

- Marlos C. Machado, Marc G. Bellemare, and Michael Bowling. Count-Based Exploration with the Successor Representation. In _Proceedings of the National Conference on Artificial Intelligence (AAAI)_ , 2020. 

- Sridhar Mahadevan. Proto-Value Functions: Developmental Reinforcement Learning. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 553– 560, 2005. 

- Sridhar Mahadevan and Mauro Maggioni. Proto-value Functions: A Laplacian Framework for Learning Representation and Control in Markov Decision Processes. _Journal of Machine Learning Research (JMLR)_ , 8:2169–2231, 2007. 

- Daniel J. Mankowitz, Augustin Z´ıdek, Andr´e Barreto, Dan Horgan, Matteo Hessel, John Quan, Junhyuk Oh, Hado van Hasselt, David Silver, and Tom Schaul. Unicorn: Continual Learning with a Universal, Off-policy Agent. _CoRR_ , abs/1802.08294, 2018. 

- Timothy A. Mann and Shie Mannor. Scaling Up Approximate Value Iteration with Options: Better Policies with Fewer Iterations. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 127–135, 2014. 

- Matheus R. F. Mendon¸ca, Artur Ziviani, and Andr´e Barreto. Laplacian using Abstract State Transition Graphs: A Framework for Skill Acquisition. In _Proceedings of the Brazilian Conference on Intelligent Systems (BRACIS)_ , pages 263–268, 2019. 

- Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. Playing Atari With Deep Reinforcement Learning. In _NeurIPS Deep Learning Workshop_ . 2013. 

- Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness, Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik, Ioannis Antonoglou, Helen King, Dharshan Kumaran, Daan Wierstra, Shane Legg, and Demis Hassabis. Human-level Control through Deep Reinforcement Learning. _Nature_ , 518:529–533, 2015. 

- Ida Momennejad, Evan Russek, Jin Hyun Cheong, Matthew Botvinick, Nathaniel Daw, and Samuel Gershman. The Successor Representation in Human Reinforcement Learning. _Nature Human Behaviour_ , 1:680––692, 2017. 

- Andrew Y. Ng, Daishi Harada, and Stuart J. Russell. Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping. In _Proceedings of the International Conference on Machine Learning (ICML)_ , pages 278–287, 1999. 

42 

Temporal Abstraction in RL with the Successor Representation 

- Jean Piaget. _The Origins of Intelligence in Children_ . W. W. Norton & Company, New York, NY, 1963. 

- Doina Precup. _Temporal Abstraction in Reinforcement Learning_ . PhD thesis, University of Massachusetts Amherst, 2000. 

- Rahul Ramesh, Manan Tomar, and Balaraman Ravindran. Successor Options: An Option Discovery Framework for Reinforcement Learning. In _Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)_ , pages 3304–3310, 2019. 

- Jianbo Shi and Jitendra Malik. Normalized Cuts and Image Segmentation. _IEEE Transactions on Pattern Analysis and Machine Intelligence (T-PAMI)_ , 22(8):888–905, 2000. 

- Alec Solway, Carlos Diuk, Natalia C´ordova, Debbie Yee, Andrew G. Barto, Yael Niv, and Matthew M. Botvinick. Optimal Behavioral Hierarchy. _PLOS Computational Biology_ , 10(8):1–10, 2014. 

- Henning Sprekeler. On the Relation of Slow Feature Analysis and Laplacian Eigenmaps. _Neural Computation_ , 23(12):3287–3302, 2011. 

- Kimberly Stachenfeld, Matthew Botvinick, and Samuel Gershman. Design Principles of the Hippocampal Cognitive Map. In _Advances in Neural Information Processing Systems (NeurIPS)_ , pages 2528–2536, 2014. 

- Kimberly Stachenfeld, Matthew Botvinick, and Samuel Gershman. The Hippocampus as a Predictive Map. _Nature Neuroscience_ , 20:1643–1653, 2017. 

- Gilbert Strang. _Linear Algebra and Its Applications_ . Brooks Cole, 2005. 

- Richard Sutton. Toward a New View of Action Selection: The Subgoal Keyboard. Slides presented at the Barbados Workshop on Reinforcement Learning, 2016. URL `http: //barbados2016.rl-community.org/RichSutton2016.pdf?attredirects=0&d=1` . 

- Richard S. Sutton. Learning to Predict by the Methods of Temporal Differences. _Machine Learning_ , 3:9–44, 1988. 

- Richard S. Sutton, Doina Precup, and Satinder Singh. Between MDPs and semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning. _Artificial Intelligence_ , – 

- 112(1–2):181 211, 1999. 

- Richard S. Sutton, Joseph Modayil, Michael Delp, Thomas Degris, Patrick M. Pilarski, Adam White, and Doina Precup. Horde: A Scalable Real-Time Architecture for Learning Knowledge from Unsupervised Sensorimotor Interaction. In _International Conference on Autonomous Agents and Multiagent Systems (AAMAS)_ , 2011. 

- Matthew E. Taylor and Peter Stone. Transfer Learning for Reinforcement Learning Domains: A Survey. _Journal of Machine Learning Research (JMLR)_ , 10:1633–1685, 2009. 

43 

Machado, Barreto, and Precup 

- Yee Whye Teh, Victor Bapst, Wojciech M. Czarnecki, John Quan, James Kirkpatrick, Raia Hadsell, Nicolas Heess, and Razvan Pascanu. Distral: Robust Multitask Reinforcement Learning. In _Advances in Neural Information Processing Systems (NeurIPS)_ , pages 4496– 4506, 2017. 

- Momchil S. Tomov, Eric Schulz, and Samuel J. Gershman. Multi-task Reinforcement Learning in Humans. _Nature Human Behaviour_ , 5:764–773, 2021. 

- Kaixin Wang, Kuangqi Zhou, Qixin Zhang, Jie Shao, Bryan Hooi, and Jiashi Feng. Towards Better Laplacian Representation in Reinforcement Learning with Generalized Graph Drawing. In _Proceedings of the International Conference on Machine Learning (ICML)_ , 2021. 

- Tao Wang, Michael Bowling, and Dale Schuurmans. Dual Representations for Dynamic Programming and Reinforcement Learning. In _Proceedings of the IEEE International Symposium on Approximate Dynamic Programming and Reinforcement Learning (ADPRL)_ , pages 44–51, 2007. 

- Christopher J. C. H. Watkins and Peter Dayan. Technical Note: Q-Learning. _Machine Learning_ , 8(3-4), May 1992. 

- Laurenz Wiskott and Terrence J. Sejnowski. Slow Feature Analysis: Unsupervised Learning of Invariances. _Neural Computation_ , 14(4):715–770, 2002. 

- Yifan Wu, George Tucker, and Ofir Nachum. The Laplacian in RL: Learning Representations with Efficient Approximations. In _Proceedings of the International Conference on Learning Representations (ICLR)_ , 2019. 

44 

Temporal Abstraction in RL with the Successor Representation 

## **Appendix A. Theoretical Results** 

We present the theoretical results below for completeness. These results were obtained in other works and we present them, as well as their proofs, in their original version. We cite them accordingly before each theorem. We refer the reader to the works by Machado et al. (2017, 2018) for further details. 

**Theorem 1 (Machado et al. 2018)** _The i-th eigenvalue (λSR,i) of the SR, defined with respect to a uniform random policy, and the j-th eigenvalue (λPVF,j) of the normalized Laplacian are related as follows when in a symmetric and deterministic environment :_ 

**==> picture [142 x 21] intentionally omitted <==**

_The i-th eigenvector (_ **e** _SR,i) of the SR and the j-th eigenvector (_ **e** _PVF,j) of the normalized Laplacian are related as follows:_ 

**==> picture [114 x 15] intentionally omitted <==**

_where i_ + _j_ = _n_ + 1 _, for both the eigenvectors and the eigenvalues; with n being the total number of rows (and columns) of matrix_ **P** _π._ 

**Proof** Let _λi_ , **e** _i_ denote the _i_ -th eigenvalue and eigenvector of the SR, respectively. Using the fact that the SR converges to ( **I** _− γ_ **P** _π_ ) _[−]_[1] (through the Neumann series), we have: 

**==> picture [365 x 292] intentionally omitted <==**

45 

Machado, Barreto, and Precup 

**Lemma 1 (Machado et al. 2017)** _Suppose_ ( **I** + **A** ) _is a non-singular matrix, with ||_ **A** _|| ≤_ 1 _. We have:_ 

**==> picture [120 x 26] intentionally omitted <==**

## **Proof** 

**==> picture [362 x 168] intentionally omitted <==**

Where the first inequality is due to the fact that _||_ **A** + **B** _|| ≤||_ **A** _||_ + _||_ **B** _||_ and the second inequality comes from the fact that _||_ **AB** _|| ≤||_ **A** _|| · ||_ **B** _||_ . 

**Lemma 2 (Machado et al. 2017)** _The induced infinity norm of_ ( **I** _− γ_ **T** ) _[−]_[1] **T** _is bounded by_ 

**==> picture [138 x 26] intentionally omitted <==**

## **Proof** 

**==> picture [390 x 100] intentionally omitted <==**

46 

Temporal Abstraction in RL with the Successor Representation 

**Theorem 2 (Machado et al. 2017)** _Let ω_ = _⟨Iω, πω, βω⟩ denote an eigenoption. In a finite and ergodic MDP with γ ∈_ [0 _,_ 1) _, there is at least one state s ∈_ S _such that βω_ ( _s_ ) = 1 _._ 

**Proof** We can write the Bellman equation in the matrix form: **v** = **r** + _γ_ **P** _π_ **v** , for a fixed policy _π_ , where **v** is a _finite_ column vector with one entry per state encoding its value function. From Equation 16 we have **r** = **P** _π_ **w** _−_ **w** with **w** = Φ **e** , where **e** denotes the eigenvector of interest and Φ _∈_ R _[|]_[S] _[|×][d]_ denotes the matrix representing the _d_ -dimensional feature representation for each state. I use _r_ : S _→_ R for simplicity. This function can be seen as the expected reward in a given state. With that we have: 

**==> picture [266 x 112] intentionally omitted <==**

where the last step is true because ( **I** _− γ_ **P** _π_ ) _[−]_[1] is guaranteed to be nonsingular since _||_ **P** _π|| ≤_ 1, where _||_ **P** _π||_ = sup **v** : _||_ **v** _||∞_ =1 _||_ **P** _π_ **v** _||∞_ . By the Neumann series we have ( **I** _− γ_ **P** _π_ ) _[−]_[1] =[�] _[∞] n_ =0 _[γ][n]_ **[P]** _[πn]_[.][Using][the][induced][norm][we][have:] 

**==> picture [380 x 78] intentionally omitted <==**

We can shift **w** by any finite constant without changing the reward, that is, **P** _π_ **w** _−_ **w** = **P** _π_ ( **w** + _**δ**_ ) _−_ ( **w** + _**δ**_ ) because **P** _π_ **1** _**δ**_ = **1** _**δ**_ since[�] _j[P][π] i,j_[=][1.] Therefore, we can assume **w** _≥_ **0** . Let _s[∗]_ = arg max _s_ **w** _s[∗]_ , so that **w** _s[∗]_ = _||_ **w** _||∞_ . Clearly **v** _s[∗] ≤_ **0** , otherwise _||_ **v** + **w** _||∞ ≥|_ **v** _s[∗]_ + **w** _s[∗] |_ = **v** _s[∗]_ + **w** _s[∗] >_ **w** _s[∗]_ = _||_ **w** _||∞_ , arriving at a contradiction. 

47 

Machado, Barreto, and Precup 

**Lemma 3 (Machado et al. 2017)** _In the tabular case, if all transitions in the MDP have been sampled once,_ **T** _[⊤]_ **T** = 2 **L** _._ 

**Proof** Let _tij_ and _ttij_ denote the entries in the _i_ -th row and _j_ -th column of matrices **T** and **T** _[⊤]_ **T** . We can write _tt_ as: _ij_ 

**==> picture [262 x 25] intentionally omitted <==**

In the tabular case, _tij_ has three possible values: 

- _tij_ = +1, meaning that the agent arrived in state _j_ at time step _i_ , 

- _tij_ = _−_ 1, meaning that the agent left state _j_ at time step _i_ , 

- _tij_ = 0, meaning that the agent did not arrive nor leave state _j_ at time step _i_ . 

We decompose **T** _[⊤]_ **T** in two matrices, **K** and **Z** , such that **T** _[⊤]_ **T** = **K** + **Z** . Here **Z** is a diagonal matrix such that _zii_ = _ttii_ , for all _i_ ; and **K** contains all elements from **T** _[⊤]_ **T** that lie outside the main diagonal. 

When computing the elements of **Z** we have _i_ = _j_ . Thus _zii_ =[�] _k[t]_[2] _ik_[.][Because][we] square all elements, we are in fact summing over all transitions leaving ( _−_ 1[2] ) and arriving (1[2] ) in state _i_ , counting the node’s degree twice. Thus, **Z** = 2 **D** _s_ . 

When not computing the elements in the main diagonal, for the element _ttij_ , we add all transitions that leave state _i_ arriving in state _j_ ( _−_ 1 _×_ 1), and those that leave state _j_ arriving in state _i_ (1 _× −_ 1). We assume each transition has been sampled once, thus: 

**==> picture [290 x 27] intentionally omitted <==**

Therefore, we have **K** = _−_ 2 **W** and **T** _[⊤]_ **T** = **K** + **Z** = 2( **D** _−_ **W** ). 

**Theorem 3 (Machado et al. 2017)** _Consider the singular value decomposition of the matrix_ **T** _s.t._ **T** = **UΣV** _, with each row of_ **T** _consisting of the difference between observations, i.e.,_ _**φ**_ ( _s[′]_ ) _−_ _**φ**_ ( _s_ ) _. In the tabular case, if all transitions in the MDP have been sampled once, the orthonormal vectors of_ **L** = **D** _−_ **W** _are the columns of_ **V** _[⊤] ._ 

**Proof** Given the SVD decomposition of a matrix **A** = **UΣV** _[⊤]_ , the columns of **V** are the eigenvectors of **A** _[⊤]_ **A** (Strang, 2005). We know that **T** _[⊤]_ **T** = 2 **L** , where **L** = **D** _−_ **W** (Lemma 3 in the Appendix). Thus, the columns of **V** are the eigenvectors of **T** _[⊤]_ **T** , which can be rewritten as 2( **D** _−_ **W** ). Therefore, the columns of **V** are also the eigenvectors of **L** . 

48 

Temporal Abstraction in RL with the Successor Representation 

## **Appendix B. Additional Results for Return Maximization with Eigenoptions and Covering Options** 

**==> picture [390 x 296] intentionally omitted <==**

**----- Start of picture text -----**<br>
Task Eigenoptions Covering options<br>G<br>S<br>S<br>G<br>G<br>S<br>**----- End of picture text -----**<br>


Figure 21: Performance of Q-learning augmented with eigenoptions and covering options in additional tasks as described in Section 6.2. In the task, S and G denote the start and goal state. Results are averaged across 50 runs and shaded regions denote a 99% confidence interval. See text for details. 

49 

Machado, Barreto, and Precup 

**==> picture [390 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
Task Eigenoptions Covering options<br>G<br>S<br>G<br>S<br>G<br>S<br>**----- End of picture text -----**<br>


Figure 22: Performance of Q-learning augmented with eigenoptions and covering options in additional tasks as described in Section 6.2. In the task, S and G denote the start and goal state. Results are averaged across 50 runs and shaded regions denote a 99% confidence interval. See text for details. 

50 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [390 x 297] intentionally omitted <==**

**----- Start of picture text -----**<br>
Task Eigenoptions Covering options<br>G S<br>G S<br>G S<br>**----- End of picture text -----**<br>


Figure 23: Performance of Q-learning augmented with eigenoptions and covering options in additional tasks as described in Section 6.2. In the task, S and G denote the start and goal state. Results are averaged across 50 runs and shaded regions denote a 99% confidence interval. See text for details. 

51 

Machado, Barreto, and Precup 

## **Appendix C. Eigenoptions and Covering Options Learned Online** 

**==> picture [390 x 282] intentionally omitted <==**

**----- Start of picture text -----**<br>
100 episodes 500 episodes 1000 episodes closed-form<br>1st eigenvector<br>2nd eigenvector<br>3rd eigenvector<br>4th eigenvector<br>**----- End of picture text -----**<br>


Figure 24: Top four eigenvectors of the SR when learning eigenoptions online for a varied number of episodes. We randomly selected one of the fifty runs to plot. The agent interacted with the environment for 1000 steps in each episode. 

52 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [390 x 276] intentionally omitted <==**

**----- Start of picture text -----**<br>
100 episodes 500 episodes 1000 episodes closed-form<br>1st eigenvector<br>2nd eigenvector<br>3rd eigenvector<br>4th eigenvector<br>**----- End of picture text -----**<br>


Figure 25: First four eigenoptions discovered online for a varied number of episodes, computed from the eigenvectors in Figure 24. We plot only one eigenoption per eigenvector (instead of two). Policies were learned off-policy from the data collected when learning the SR. 

53 

Machado, Barreto, and Precup 

**==> picture [390 x 289] intentionally omitted <==**

**----- Start of picture text -----**<br>
100 episodes 500 episodes 1000 episodes closed-form<br>1st iteration<br>2nd iteration<br>3rd iteration<br>4th iteration<br>**----- End of picture text -----**<br>


Figure 26: Top four eigenvectors of the SR when learning covering options online for a varied number of episodes. We randomly selected one of the fifty runs to plot. The agent interacted with the environment for 1000 steps in each episode. 

54 

Temporal Abstraction in RL with the Successor Representation 

**==> picture [390 x 274] intentionally omitted <==**

**----- Start of picture text -----**<br>
100 episodes 500 episodes 1000 episodes closed-form<br>1st iteration<br>2nd iteration<br>3rd iteration<br>4th iteration<br>**----- End of picture text -----**<br>


Figure 27: First four covering options discovered online for a varied number of episodes, computed from the eigenvectors in Figure 26. We plot only one covering option per eigenvector (instead of two). Policies were learned off-policy from the data collected when learning the SR. Notice how the covering options discovered online in the second and third iteration already overlap, and how none of the first four options capture the NW-SE diagonal when discovered online. 

55 

Machado, Barreto, and Precup 

## **Appendix D. Impact of using the Eigenvectors of the SR instead of the Eigenvectors of the Laplacian when Discovering Covering Options** 

The theoretical guarantees we discussed for the equivalence between the eigenvectors of the graph Laplacian and the eigenvectors of the SR do not hold in later iterations of covering options. In the four-room domain, for example, after the first iteration of covering options, in some states the agent has access to four primitive actions and one option, while only four actions are available in the other states. This creates an asymmetry that violates one of the assumptions of Theorem 1. One of the consequences of this is that, in practice, when estimating the SR instead of the graph Laplacian, we sometimes observe eigenvectors with a non-zero complex part. We empirically evaluated, in closed-form, the impact of using the SR to learn covering options, ignoring its complex component, which is what we actually used in Section 6.4. We used the same parameters we used when learning eigenoptions, also learning the options’ policies off-policy. The results are depicted in Figure 28. Despite some variations, at least in the four-room domains, when computing covering options in closed-form, the mismatches between the eigenvectors of the Laplacian and of the SR do not lead to very different results.[7] 

**==> picture [359 x 128] intentionally omitted <==**

**----- Start of picture text -----**<br>
10 [4]<br>1400 1400 Covering Options (Laplacian)<br>Covering Options (SR)<br>10 [3]<br>Primitive Actions<br>1100 1100<br>10 [2]<br>800 0 10 20 30 800<br>500 500<br>200 200<br>0 10 20 30 0 10 20 30<br>Number of Options Number of Options<br>Diffusion Time Diffusion Time<br>**----- End of picture text -----**<br>


Figure 28: Average (left) and median (right) diffusion time in the four-room domain induced by covering options when computed with the SR and the eigenvectors of the graph Laplacian, in closed-form. The inset plot on the left figure depicts, in log-scale, the range the diffusion time lies. 

> 7. Because the environment we consider is ultimately symmetric, to avoid asymmetries in the SR, after we estimate the SR matrix Ψ, we actually compute the eigendecomposition of the matrix (Ψ + Ψ _[⊤]_ ) _/_ 2. Alternative solutions for dealing with the asymmetry of time-based representations include using a singular value decomposition (Machado et al., 2018) or applying spectral analysis on the result of a polar decomposition (Bar et al., 2020). We consider this problem to be outside the scope of our paper. 

56 

